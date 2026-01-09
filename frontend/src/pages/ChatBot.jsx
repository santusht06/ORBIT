import React, { useState, useEffect, useRef, useCallback } from "react";
import {
  Send,
  Paperclip,
  MessageSquare,
  X,
  Loader2,
  FileText,
  Image,
  File,
} from "lucide-react";

import { GiMoonOrbit } from "react-icons/gi";

const API_BASE_URL = "http://localhost:8000";

export default function ChatBot() {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");
  const [file, setFile] = useState(null);
  const [sessionId, setSessionId] = useState(null);
  const [loading, setLoading] = useState(false);
  const [conversations, setConversations] = useState([]);
  const [showSidebar, setShowSidebar] = useState(false);
  const [contextInfo, setContextInfo] = useState(null);

  const messagesEndRef = useRef(null);
  const fileInputRef = useRef(null);

  // Auto-scroll to bottom
  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  // Memoized loadConversations function
  const loadConversations = useCallback(async () => {
    try {
      const formData = new FormData();
      const response = await fetch(
        `${API_BASE_URL}/chat/?action=get_conversations`,
        {
          method: "POST",
          body: formData,
        }
      );
      const data = await response.json();
      if (data.status === "success") {
        // Filter out conversations with no messages
        const conversationsWithMessages = data.conversations.filter(
          (conv) => conv.message_count > 0
        );

        // Fetch first message for each conversation to generate title
        const conversationsWithTitles = await Promise.all(
          conversationsWithMessages.map(async (conv) => {
            try {
              const historyFormData = new FormData();
              const historyResponse = await fetch(
                `${API_BASE_URL}/chat/?action=get_history&session_id=${conv.session_id}`,
                { method: "POST", body: historyFormData }
              );
              const historyData = await historyResponse.json();

              // Get first user message for title
              const firstUserMessage = historyData.messages?.find(
                (msg) => msg.role === "user"
              );
              const generatedTitle =
                firstUserMessage?.content || "Untitled chat";

              return {
                ...conv,
                displayTitle: generatedTitle,
              };
            } catch (error) {
              return {
                ...conv,
                displayTitle: "Untitled chat",
              };
            }
          })
        );
        setConversations((prev) => {
          const map = new Map();

          prev.forEach((c) => map.set(c.session_id, c));

          conversationsWithTitles.forEach((c) => map.set(c.session_id, c));

          return Array.from(map.values());
        });
      }
    } catch (error) {
      console.error("Failed to load conversations:", error);
    }
  }, []);

  const loadContextInfo = useCallback(async () => {
    if (!sessionId) return;

    try {
      const formData = new FormData();
      const response = await fetch(
        `${API_BASE_URL}/chat/?action=get_context&session_id=${sessionId}`,
        {
          method: "POST",
          body: formData,
        }
      );
      const data = await response.json();
      setContextInfo(data);
    } catch (error) {
      console.error("Failed to load context:", error);
    }
  }, [sessionId]);

  const loadConversationHistory = useCallback(async (convSessionId) => {
    try {
      const formData = new FormData();
      const response = await fetch(
        `${API_BASE_URL}/chat/?action=get_history&session_id=${convSessionId}`,
        {
          method: "POST",
          body: formData,
        }
      );
      const data = await response.json();
      if (data.status === "success") {
        const formattedMessages = data.messages.map((msg) => ({
          role: msg.role,
          content: msg.content,
          model: msg.model_used,
          timestamp: msg.created_at,
        }));
        setMessages(formattedMessages);
        setSessionId(convSessionId);
        setShowSidebar(false);
      }
    } catch (error) {
      console.error("Failed to load history:", error);
    }
  }, []);

  // Load conversations on mount
  useEffect(() => {
    loadConversations();
  }, [loadConversations]);

  // Load context info when session changes
  useEffect(() => {
    if (sessionId) {
      loadContextInfo();
    }
  }, [sessionId, loadContextInfo]);

  const generateTitleFromMessage = (text) => {
    if (!text) return "Untitled chat";
    return text.trim().split(" ").slice(0, 6).join(" ");
  };

  const getFileIcon = (filename) => {
    const ext = filename?.toLowerCase().split(".").pop();
    if (["jpg", "jpeg", "png", "gif", "webp", "bmp"].includes(ext)) {
      return <Image className="w-4 h-4" />;
    } else if (ext === "pdf") {
      return <FileText className="w-4 h-4" />;
    }
    return <File className="w-4 h-4" />;
  };

  const handleSend = async () => {
    if (!input.trim() && !file) return;

    const userMessage = { role: "user", content: input, file: file?.name };
    setMessages((prev) => [...prev, userMessage]);

    const currentInput = input;
    const currentFile = file;
    setInput("");
    setFile(null);
    setLoading(true);

    try {
      const formData = new FormData();
      if (currentFile) {
        formData.append("file", currentFile);
      }
      if (currentInput.trim()) {
        formData.append("message", currentInput);
      }

      const url = sessionId
        ? `${API_BASE_URL}/chat/?session_id=${sessionId}`
        : `${API_BASE_URL}/chat/`;

      const response = await fetch(url, {
        method: "POST",
        body: formData,
      });

      const data = await response.json();

      if (!sessionId && data.session_id) {
        const newTitle = generateTitleFromMessage(currentInput);

        const newConversation = {
          session_id: data.session_id,
          message_count: 1,
          displayTitle: newTitle,
        };

        setSessionId(data.session_id);

        setConversations((prev) => [newConversation, ...prev]);
      }

      if (data.answer) {
        setMessages((prev) => [
          ...prev,
          {
            role: "assistant",
            content: data.answer,
            model: data.model_used,
            mode: data.mode,
            source: data.source,
          },
        ]);
      } else if (data.message) {
        setMessages((prev) => [
          ...prev,
          {
            role: "system",
            content: data.message,
          },
        ]);
      }

      // Immediately reload conversations after sending message
      await loadConversations();
      loadContextInfo();
    } catch (error) {
      setMessages((prev) => [
        ...prev,
        {
          role: "system",
          content: `Error: ${error.message}`,
        },
      ]);
    } finally {
      setLoading(false);
    }
  };

  const handleFileSelect = (e) => {
    const selectedFile = e.target.files[0];
    if (selectedFile) {
      setFile(selectedFile);
    }
  };

  const clearContext = async () => {
    if (!sessionId) return;

    try {
      const formData = new FormData();
      const response = await fetch(
        `${API_BASE_URL}/chat/?action=clear_context&session_id=${sessionId}`,
        {
          method: "POST",
          body: formData,
        }
      );
      const data = await response.json();
      if (data.status === "success") {
        setMessages((prev) => [
          ...prev,
          {
            role: "system",
            content: "Context cleared successfully",
          },
        ]);
        loadContextInfo();
      }
    } catch (error) {
      console.error("Failed to clear context:", error);
    }
  };

  const startNewChat = () => {
    setMessages([]);
    setSessionId(null);
    setFile(null);
    setInput("");
    setContextInfo(null);
    setShowSidebar(false);
  };

  return (
    <div className="flex h-screen bg-gray-50">
      {/* Sidebar */}
      <div
        className={`${
          showSidebar ? "translate-x-0" : "-translate-x-full"
        } lg:translate-x-0 fixed lg:relative z-30 w-64 bg-gray-900 text-white transition-transform duration-300 ease-in-out h-full flex flex-col`}
      >
        <div className="p-4 border-b border-gray-700">
          <button
            onClick={startNewChat}
            className="w-full px-4 py-2 bg-gray-800 hover:bg-gray-700 rounded-lg flex items-center gap-2 transition-colors"
          >
            <MessageSquare className="w-5 h-5" />
            <span>New Chat</span>
          </button>
        </div>

        <div className="flex-1 overflow-y-auto p-2">
          <h3 className="text-xs font-semibold text-gray-400 uppercase mb-3 px-2">
            Recent
          </h3>
          {conversations.length === 0 ? (
            <div className="text-sm text-gray-500 px-3 py-2">
              No conversations yet
            </div>
          ) : (
            conversations.map((conv) => {
              // Generate title from first user message
              const preview = generateTitleFromMessage(conv.displayTitle);
              const isActive = sessionId === conv.session_id;

              return (
                <button
                  key={conv.session_id}
                  onClick={() => loadConversationHistory(conv.session_id)}
                  className={`w-full text-left px-3 py-2.5 rounded-lg mb-1 transition-all group ${
                    isActive ? "bg-gray-800" : "hover:bg-gray-800"
                  }`}
                >
                  <div className="flex items-start gap-2">
                    <MessageSquare className="w-4 h-4 mt-0.5 flex-shrink-0 text-gray-400" />
                    <div className="flex-1 min-w-0">
                      <div className="text-sm font-medium truncate">
                        {preview}
                      </div>
                      <div className="text-xs text-gray-500 mt-0.5">
                        {conv.message_count}{" "}
                        {conv.message_count === 1 ? "message" : "messages"}
                      </div>
                    </div>
                  </div>
                </button>
              );
            })
          )}
        </div>

        {/* Context Info */}
        {contextInfo?.has_context && (
          <div className="p-4 border-t border-gray-700">
            <div className="text-xs text-gray-400 mb-2">Active Context</div>
            {contextInfo.file && (
              <div className="flex items-center gap-2 text-sm mb-2">
                {getFileIcon(contextInfo.file.filename)}
                <span className="truncate">{contextInfo.file.filename}</span>
              </div>
            )}
            <button
              onClick={clearContext}
              className="w-full px-3 py-1.5 bg-red-600 hover:bg-red-700 rounded text-xs transition-colors"
            >
              Clear Context
            </button>
          </div>
        )}
      </div>

      {/* Main Chat Area */}
      <div className="flex-1 flex flex-col">
        {/* Header */}
        <div className="bg-white border-b px-4 py-3 flex items-center justify-between">
          <div className="flex items-center gap-3">
            <button
              onClick={() => setShowSidebar(!showSidebar)}
              className="lg:hidden p-2 hover:bg-gray-100 rounded-lg"
            >
              <MessageSquare className="w-5 h-5" />
            </button>
            <GiMoonOrbit className="text-3xl" />

            <h1 className="text-xl font-semibold text-gray-800">ORBIT</h1>
          </div>
          {sessionId && (
            <div className="text-xs text-gray-500 hidden sm:block">
              Session: {sessionId.slice(0, 8)}...
            </div>
          )}
        </div>

        {/* Messages */}
        <div className="flex-1 overflow-y-auto p-4 space-y-4">
          {messages.length === 0 && (
            <div className="text-center text-gray-400 mt-20">
              <MessageSquare className="w-16 h-16 mx-auto mb-4 opacity-50" />
              <h2 className="text-2xl font-semibold mb-2">
                Start a Conversation
              </h2>
              <p className="text-sm">
                Upload a file or send a message to begin
              </p>
            </div>
          )}

          {messages.map((msg, idx) => (
            <div
              key={idx}
              className={`flex ${
                msg.role === "user" ? "justify-end" : "justify-start"
              }`}
            >
              <div
                className={`max-w-[80%] rounded-2xl px-4 py-3 ${
                  msg.role === "user"
                    ? "bg-blue-600 text-white"
                    : msg.role === "system"
                    ? "bg-yellow-100 text-yellow-800 border border-yellow-300"
                    : "bg-white text-gray-800 shadow-md border border-gray-200"
                }`}
              >
                {msg.file && (
                  <div className="flex items-center gap-2 mb-2 text-sm opacity-80">
                    {getFileIcon(msg.file)}
                    <span>{msg.file}</span>
                  </div>
                )}
                <div className="whitespace-pre-wrap break-words">
                  {msg.content}
                </div>
                {msg.model && (
                  <div className="text-xs opacity-60 mt-2">
                    {msg.mode && `${msg.mode} • `}
                    {msg.model}
                    {msg.source && ` • ${msg.source}`}
                  </div>
                )}
              </div>
            </div>
          ))}

          {loading && (
            <div className="flex justify-start">
              <div className="bg-white text-gray-800 shadow-md border border-gray-200 rounded-2xl px-4 py-3">
                <Loader2 className="w-5 h-5 animate-spin" />
              </div>
            </div>
          )}

          <div ref={messagesEndRef} />
        </div>

        {/* Input Area */}
        <div className="bg-white border-t p-4">
          {file && (
            <div className="mb-3 flex items-center gap-2 bg-blue-50 border border-blue-200 rounded-lg px-3 py-2">
              {getFileIcon(file.name)}
              <span className="text-sm flex-1 truncate">{file.name}</span>
              <button
                onClick={() => setFile(null)}
                className="p-1 hover:bg-blue-100 rounded"
              >
                <X className="w-4 h-4" />
              </button>
            </div>
          )}

          <div className="flex gap-2">
            <input
              type="file"
              ref={fileInputRef}
              onChange={handleFileSelect}
              className="hidden"
              accept=".pdf,.txt,.md,.jpg,.jpeg,.png,.webp,.gif,.doc,.docx"
            />

            <button
              onClick={() => fileInputRef.current?.click()}
              className="p-3 hover:bg-gray-100 rounded-lg transition-colors"
              disabled={loading}
            >
              <Paperclip className="w-5 h-5 text-gray-600" />
            </button>

            <input
              type="text"
              value={input}
              onChange={(e) => setInput(e.target.value)}
              onKeyPress={(e) =>
                e.key === "Enter" && !e.shiftKey && handleSend()
              }
              placeholder="Type your message..."
              className="flex-1 px-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
              disabled={loading}
            />

            <button
              onClick={handleSend}
              disabled={loading || (!input.trim() && !file)}
              className="px-6 py-3 bg-blue-600 text-white rounded-lg hover:bg-blue-700 disabled:opacity-50 disabled:cursor-not-allowed transition-colors flex items-center gap-2"
            >
              {loading ? (
                <Loader2 className="w-5 h-5 animate-spin" />
              ) : (
                <>
                  <Send className="w-5 h-5" />
                  <span className="hidden sm:inline">Send</span>
                </>
              )}
            </button>
          </div>

          <div className="text-xs text-gray-500 mt-2 text-center">
            Supports PDF, images, text files, and Word documents
          </div>
        </div>
      </div>

      {/* Overlay for mobile sidebar */}
      {showSidebar && (
        <div
          className="fixed inset-0 bg-black bg-opacity-50 z-20 lg:hidden"
          onClick={() => setShowSidebar(false)}
        />
      )}
    </div>
  );
}
