import requests
import io
import PyPDF2
from typing import Optional


def extract_text_from_pdf(url: str) -> str:
    try:
        # Download with timeout
        response = requests.get(url, timeout=30)
        response.raise_for_status()

        # Check if we got data
        if not response.content:
            raise ValueError("Empty response from Cloudinary")

        # Try to read PDF
        pdf_file = io.BytesIO(response.content)
        reader = PyPDF2.PdfReader(pdf_file)

        # Check if PDF has pages
        if len(reader.pages) == 0:
            raise ValueError("PDF has no pages")

        text = ""
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"

        if not text.strip():
            raise ValueError("No text could be extracted from PDF")

        return text

    except PyPDF2.errors.PdfReadError as e:
        raise ValueError(
            f"PDF read error: {str(e)}. The PDF might be corrupted or password-protected."
        )
    except requests.exceptions.RequestException as e:
        raise ValueError(f"Failed to download PDF: {str(e)}")
    except Exception as e:
        raise ValueError(f"Error extracting text: {str(e)}")
