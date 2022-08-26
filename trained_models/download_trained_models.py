import gdown
import shutil
import os

zip_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'trained_models.zip')
gdown.download(
    'https://drive.google.com/uc?id=1uF8rqZfYAxBvIQ7so1BadMmAKe6YtcYd',
    zip_path,
)
shutil.unpack_archive(zip_path, os.path.dirname(os.path.abspath(__file__)))
os.remove(zip_path)
