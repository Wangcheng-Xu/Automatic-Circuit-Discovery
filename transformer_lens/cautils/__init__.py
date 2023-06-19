import warnings
from IPython import get_ipython
ipython = get_ipython()


if ipython is not None: # so this works as a script and in a notebook
    warnings.warn("Running load_ext autoreload...")
    ipython.run_line_magic("load_ext", "autoreload")
    ipython.run_line_magic("autoreload", "2")

import torch as t
import torch
warnings.warn("Setting grad enabled false...")
t.set_grad_enabled(False)

import numpy as np
from jaxtyping import Float, Int, Bool, jaxtyped
from typing import Union, List, Dict, Tuple, Callable, Optional, Any, Sequence, Iterable, Mapping, TypeVar, Generic, NamedTuple
from torch import Tensor
import torch.nn.functional as F
from tqdm.auto import tqdm
from rich import print as rprint
from transformer_lens import utils, HookedTransformer, ActivationCache
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from functools import partial
import re
from pathlib import Path
import einops
from IPython.display import display, clear_output

import transformer_lens
from transformer_lens import *
from transformer_lens.utils import *

def to_tensor(
    tensor,
):
    return t.from_numpy(to_numpy(tensor))

def old_imshow(
    tensor, 
    **kwargs,
):
    tensor = to_tensor(tensor)
    zmax = tensor.abs().max().item()

    if "zmin" not in kwargs:
        kwargs["zmin"] = -zmax
    if "zmax" not in kwargs:
        kwargs["zmax"] = zmax
    if "color_continuous_scale" not in kwargs:
        kwargs["color_continuous_scale"] = "RdBu"

    fig = px.imshow(
        to_numpy(tensor),
        **kwargs,
    )
    fig.show()


device = t.device("cuda" if t.cuda.is_available() else "cpu")

from transformer_lens.cautils.path_patching import Node, IterNode, act_patch, path_patch
from transformer_lens.cautils.plotly_utils import imshow, hist, line
from transformer_lens.cautils.ioi_dataset import NAMES, IOIDataset