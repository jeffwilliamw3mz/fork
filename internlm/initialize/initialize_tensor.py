#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import math

import torch
from torch import Tensor, nn


def scaled_init_method_normal(sigma, num_layers):
    """Init method based on N(0, sigma/sqrt(2*num_layers)."""
    std = sigma / math.sqrt(2.0 * num_layers)

    def init_(tensor):
        return torch.nn.init.normal_(tensor, mean=0.0, std=std)

    return init_


def normal_(mean: float = 0.0, std: float = 1.0):
    r"""Return the initializer filling the input Tensor with values drawn from the normal distribution

     .. math::
        \mathcal{N}(\text{mean}, \text{std}^2)

    Args:
        mean (float): the mean of the normal distribution. Defaults 0.0.
        std (float): the standard deviation of the normal distribution. Defaults 1.0.
    """

    def initializer(tensor: Tensor):
        return nn.init.normal_(tensor, mean, std)

    return initializer
