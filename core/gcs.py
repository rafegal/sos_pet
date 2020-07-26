from google.cloud import storage
from google.cloud.storage import Blob
import uuid

from django.conf import settings

class GoogleCloudStorage:
    def __init__(self):
        self.client = storage.Client()
        self.bucket = self.client.get_bucket(settings.GCS_BUCKET_NAME)

    def save_file(self, file, file_name):
        blob = Blob(file_name, self.bucket)
        blob.upload_from_file(file, content_type=file.content_type)
    
    def delete_file(self, file_name):
        blob = Blob(file_name, self.bucket)
        blob.delete()

    def get_file(self, file_name):
        return f'https://storage.cloud.google.com/sos-pet/{file_name}'