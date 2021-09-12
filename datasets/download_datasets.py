from google_drive_downloader import GoogleDriveDownloader as gdd
import os

zip_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),'datasets.zip')
gdd.download_file_from_google_drive(file_id='1lnFhEnEv6rAF8apVj5issvA9lDxXq8T1',
                                    dest_path= zip_path,
                                    unzip=True)

os.remove(zip_path)