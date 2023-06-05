from abc import ABC, abstractmethod
from configuration.config import AppConfig
from configuration.config import CellarConfig
from PIL import Image
import time
import tinys3


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

    def saveFile(self, image: Image, filename: str | None) -> None:
        conn = tinys3.Connection(self.cellar_conf.key,
                                 self.cellar_conf.user,
                                 tls=True,
                                 endpoint=self.cellar_conf.url)
        conn.upload(filename, image, 'floxx-ia-images', rewind=False)


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
