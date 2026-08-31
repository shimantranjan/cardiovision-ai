import torch
import numpy as np
import pandas as pd
import cv2
import timm


def test_core_libraries():
    assert torch.__version__
    assert np.__version__
    assert pd.__version__
    assert cv2.__version__
    assert timm.__version__


def test_mps_available():
    assert torch.backends.mps.is_available()