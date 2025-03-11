import pathlib

import requests
import torch
from tqdm import tqdm

from .model import MobileFaceNet

__all__ = ["MobileFaceNet", "mobile_face_net"]

_URL = "https://github.com/cylix-reproduction/mobilefacenet-pytorch/releases/download/pretrained/mobilefacenet.pt"
_CACHE_DIR = pathlib.Path(__file__).parent / "cache"
_CACHE_PATH = _CACHE_DIR / "mobilefacenet.pt"
_DEFAULT_DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")
_DOWNLOAD_CHUNKSIZE = 1024


def mobile_face_net(*args, pretrained: bool = False, map_location=_DEFAULT_DEVICE, **kwargs) -> MobileFaceNet:
    """
    Create a MobileFaceNet.

    This function provides a easy way to get a pretrained MobileFaceNet from the binary at GitHub. When
    `pretrained=True`, the other parameters passed in this function are ignored, of course.
    """

    if not pretrained:
        return MobileFaceNet(*args, **kwargs)

    if not _CACHE_PATH.exists():
        # prepare cache path
        if not _CACHE_DIR.exists():
            _CACHE_DIR.mkdir()
        # and download pretrained binary
        with _CACHE_PATH.open("wb") as cache:
            response = requests.get(_URL, stream=True)
            file_size = int(response.headers.get("content-length", 0))
            with tqdm(total=file_size, desc="MobileFaceNet Params") as progress:
                for data in response.iter_content(_DOWNLOAD_CHUNKSIZE):
                    progress.update(cache.write(data))

    with _CACHE_PATH.open("rb") as cache:
        return torch.jit.load(cache, map_location=map_location)
