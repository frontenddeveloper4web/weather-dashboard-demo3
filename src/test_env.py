from dotenv import load_dotenv 
import os

# Load environment variables
load_dotenv()

# Print environment variables to check they're loaded
print("Environment variables:")
print(f"API Key: {os.getenv('OPENWEATHER_API_KEY')}")
print(f"Bucket Name: {os.getenv('AWS_BUCKET_NAME')}")

# Also print the path where it's looking for the .env file
print(f"\nWorking directory: {os.getcwd()}")