# MobileFaceNet PyTorch

This project is a **uv**-compatible fork of the [MobileFaceNet](https://github.com/foamliu/MobileFaceNet) repo.

- [MobileFaceNet PyTorch](#mobilefacenet-pytorch)
  - [Installation](#installation)
    - [Case 1: PyTorch already installed](#case-1-pytorch-already-installed)
    - [Case 2: PyTorch not installed yet](#case-2-pytorch-not-installed-yet)
  - [Typical Usage](#typical-usage)


> **Functionality Warning**
>
> This repo just simply preserves a `MobileFaceNet` implementation and a `mobile_face_net` function to get a pretrained
> version of it. The training and evaluation codes are deleted.

## Installation
Every project under the [Cylix's Reproduction of Papers](https://github.com/cylix-reproduction) organization adopts the
[uv](https://docs.astral.sh/uv) as the **only** package manager. Installing with other package manager is not guaranteed
to succeed.

Use this command:
```shell
uv add git+https://github.com/cylix-reproduction/mobilefacenet-pytorch
```
to download the latest version of this library. For more detailed information about **git installation**, see [Add a Git
dependency](https://docs.astral.sh/uv/concepts/projects/dependencies/#git).

> What about `pip`?
>
> `pip` support Git installation too, see [pip VCS Support](https://pip.pypa.io/en/stable/topics/vcs-support/#git). In
> fact, most package manager supports installing a Python package from a Git repository. I'm not publishing to PyPI
> because this is a forked repo. 

## Typical Usage
To fetch a pretrained model, run:
```python
from mobilefacenet_pytorch import mobile_face_net

net = mobile_face_net(pretrained=True)
```
and then you get a pretrained MobileFaceNet. Your network should be always unblocked because the pretrained parameters
binary is fetched from the [GitHub releases](https://github.com/cylix-reproduction/mobilefacenet-pytorch/releases) of
this repo.