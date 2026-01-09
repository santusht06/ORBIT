import cloudinary
import os


cloudinary.config(
    cloud_name=os.getenv("CLOUDINARY_CLOUD_NAME"),  # ✅ Fixed from CLOUDINARY_API_NAME
    api_key=os.getenv("CLOUDINARY_API_KEY"),
    api_secret=os.getenv("CLOUDINARY_API_SECRET"),
    secure=True,
)

# Optional: Debug print to verify config loads
print("✅ Cloudinary configured:")
print(f"  Cloud Name: {os.getenv('CLOUDINARY_CLOUD_NAME')}")
print(
    f"  API Key: {os.getenv('CLOUDINARY_API_KEY')[:10]}..."
    if os.getenv("CLOUDINARY_API_KEY")
    else "  API Key: None"
)


me = os.getenv("SANTUSHT")


print("this is me = ", me)
