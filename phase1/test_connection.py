import os
from google.cloud import storage
from google.oauth2 import service_account

# Load credentials from the key file
credentials = service_account.Credentials.from_service_account_file(
    "../secrets/cme-desk-agent-key.json"
)

# Connect to GCS
client = storage.Client(
    credentials=credentials,
    project="cme-desk-dev"
)

# Write a test file to the bucket
bucket = client.bucket("cme-desk-market-data")
blob = bucket.blob("test/hello.txt")
blob.upload_from_string("CME Desk is alive.")

print("Successfully wrote to GCS")

# Read it back
content = blob.download_as_text()
print(f"Read back: {content}")

# Clean up
blob.delete()
print("Cleaned up test file")