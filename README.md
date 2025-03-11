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

### Case 1: PyTorch already installed

If you have **`torch` installed already**, use this command:
```shell
uv add git+https://github.com/cylix-reproduction/mobilefacenet-pytorch
```
to download the latest version of this library. For more detailed information about **git installation**, see [Add a Git
dependency](https://docs.astral.sh/uv/concepts/projects/dependencies/#git).

### Case 2: PyTorch not installed yet
If you haven't install `torch` yet, you can specify a extra dependency like this:
```shell
uv add git+https://github.com/cylix-reproduction/mobilefacenet-pytorch[cpu]
```

Note the **`[cpu]`** suffix is required to install a CPU version of PyTorch. There's more options if a GPU version is
desired:
- `[cu118]` for CUDA 11.8
- `[cu124]` for CUDA 12.4 
- `[cu126]` for CUDA 12.6
- `[rocm624]` for ROCm 6.2.4

> **Dependency Warning**
>
> This library does not require `torch` dependency in order to support `[extra_dependency]` installation feature.
> However, it does not mean that this library is free of it. PyTorch is needed to use this library.

## Typical Usage
To fetch a pretrained model, run:
```python
from mobilefacenet_pytorch import mobile_face_net

net = mobile_face_net(pretrained=True)
```
and then you get a pretrained MobileFaceNet. Your network should be always unblocked because the pretrained parameters
binary is fetched from the [GitHub releases](https://github.com/cylix-reproduction/mobilefacenet-pytorch/releases) of this repo.