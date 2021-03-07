import os
import logging.config
import zipfile as zf
from kaggle.api.kaggle_api_extended import KaggleApi


class KaggleData(KaggleApi):
    """
    Class to work with Kaggle API. It inherits methods from parent class, KaggleApi().
    References:
        - On parent class method inheritance: https://stackoverflow.com/a/805082/13416265

    Attributes
    __________
    kaggle_username : str
        Username for Kaggle account.
    kaggle_key : str
        Key for connecting to Kaggle API.
    dir_raw : str
        Path to download data to.

    Methods
    _______
    download_data(dataset_link)
        Downloads data via Kaggle API to local system.

    extract_data_zip(zip_name)
        Unzips a zip file.
    """

    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.kaggle_username = os.getenv("KAGGLE_USERNAME")
        self.kaggle_key = os.getenv("KAGGLE_KEY")
        self.dir_raw = os.getenv("DIR_DATA_RAW")
        KaggleApi.__init__(self)

        if self.kaggle_username is None or self.kaggle_key is None:
            raise ValueError(
                "Kaggle API credentials empty, please set as environment variables in the .secrets file"
            )
        else:
            self.logger.info("Initialise and authenticate Kaggle API connection")
            super(KaggleData, self).authenticate()

    def download_data(self, dataset_link: str):
        """
        Downloads data via Kaggle API to local system.

        :param dataset_link: String of the dataset link to get data from.
        :return:
        """

        # list dataset files
        data_set_files = (
            super(KaggleData, self).dataset_list_files(dataset=dataset_link).files
        )
        self.logger.info(f"Downloading {data_set_files} to {self.dir_raw}...")

        # download all files
        super(KaggleData, self).dataset_download_files(
            dataset=dataset_link, path=self.dir_raw
        )

    def extract_data_zip(self, zip_name: str):
        """
        Unzips a zip file.

        :param zip_name: String of the zip file to unzip.
        :return:
        """

        self.logger.info(f"Unzipping {zip_name} to {self.dir_raw}...")
        zip_path = f"{self.dir_raw}/{zip_name}.zip"
        with zf.ZipFile(zip_path) as z:
            z.extractall(self.dir_raw)

        self.logger.info(f"Deleting {zip_name}.zip...")
        os.remove(zip_path)
