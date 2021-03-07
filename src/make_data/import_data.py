import os
import zipfile as zf
from kaggle.api.kaggle_api_extended import KaggleApi


KAGGLE_USERNAME = os.getenv("KAGGLE_USERNAME")
KAGGLE_KEY = os.getenv("KAGGLE_KEY")
DIR_RAW = os.getenv("DIR_DATA_RAW")

# initialise and authenticate
api = KaggleApi()
api.authenticate()

# list dataset files
api.dataset_list_files(dataset="pariza/bbc-news-summary").files

# download all files
api.dataset_download_files(dataset="pariza/bbc-news-summary", path=DIR_RAW)

# unzip
with zf.ZipFile("data/raw/bbc_news_summary.zip") as z:
    z.extractall("data/raw")


# delete zip file
os.remove("data/raw/bbc_news_summary.zip")
