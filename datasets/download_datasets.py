import gdown
import shutil
import os

zip_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'datasets.zip')
gdown.download(
    'https://drive.google.com/uc?id=1FaKT5C4T3gwz7TgzwWPlx7nzSPF73p8R',
    zip_path,
)
shutil.unpack_archive(zip_path, os.path.dirname(os.path.abspath(__file__)))
os.remove(zip_path)
