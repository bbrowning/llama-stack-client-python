# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Union
from typing_extensions import Required, TypedDict

from .sdg_fn_params_param import SDGFnParamsParam

__all__ = ["GenerateConfigParam"]


class GenerateConfigParam(TypedDict, total=False):
    sdg_fn_params: Required[Dict[str, Union[bool, float, str, Iterable[object], object, None]]]
    """
    Runtime parameters for the specific SDG Function you want to run
    """
