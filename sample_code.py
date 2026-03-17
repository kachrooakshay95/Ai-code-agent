from azure.storage.blob import BlobServiceClient

conn_str = "YOUR_CONNECTION_STRING"
client = BlobServiceClient.from_connection_string(conn_str)

container = client.get_container_client("input-code")

blob = container.get_blob_client("sample.py")

blob.upload_blob("def test(): pass", overwrite=True)