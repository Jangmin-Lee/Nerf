import torch

import numpy as np


# Misc
def img2mse(x, y):
    return torch.mean((x - y) ** 2)


def mse2psnr(x):
    return -10.0 * torch.log(x) / torch.log(torch.Tensor([10.0]))


def to8b(x):
    return (255 * np.clip(x, 0, 1)).astype(np.uint8)
