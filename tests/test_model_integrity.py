import unittest

from src.mobilefacenet_pytorch import mobile_face_net


class ModelIntegrityTestcase(unittest.TestCase):
    def test_model_integrity(self) -> None:
        net = mobile_face_net(pretrained=True)
        print(net)
