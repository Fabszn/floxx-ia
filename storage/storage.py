from abc import ABC, abstractmethod
from configuration.config import AppConfig
from configuration.config import CellarConfig
from PIL import Image
import time

from boto.s3.connection import S3Connection
from boto.s3.connection import OrdinaryCallingFormat
from PIL import Image
from io import BytesIO
import os


# Interface
class Storage(ABC):

    @abstractmethod
    def saveFile(self, image: Image, filename: str | None) -> None:
        pass


class LocalStorage(Storage):
    path: str = None

    def __init__(self, conf: AppConfig):
        self.path = conf.localconfig().path

    def saveFile(self, image: Image, filename: str | None) -> None:
        print(image)
        image.save(self.path + str(time.time_ns()) + '_' + filename, 'JPEG')


class CellarStorage(Storage):
    cellar_conf: CellarConfig = None

    def __init__(self, conf: AppConfig):
        self.cellar_conf = conf.cellarconfig()
        os.environ["AWS_ACCESS_KEY_ID"] = self.cellar_conf.user
        os.environ["AWS_SECRET_ACCESS_KEY"] = self.cellar_conf.key

    def saveFile(self, image: Image, filename: str | None) -> None:
        cf = OrdinaryCallingFormat()  # This mean that you _can't_ use upper case name
        conn = S3Connection(aws_access_key_id=self.cellar_conf.key, aws_secret_access_key=self.cellar_conf.user,
                            host=self.cellar_conf.url, calling_format=cf)

        image_bytes = BytesIO()
        image.save(image_bytes, format='JPEG')
        image_bytes.seek(0)

        k = conn.get_bucket("floxx-ia-images").new_key(filename)
        k.set_contents_from_file(image_bytes)


class StorageBuilder:
    currentStorage: Storage = None

    def __init__(self, conf: AppConfig):
        if conf.environment() == "CELLAR":
            print("CELLAR Storage")
            self.currentStorage = CellarStorage(conf)
        else:
            print("LOCAL Storage")
            self.currentStorage = LocalStorage(conf)

    def build(self) -> Storage:
        return self.currentStorage
