# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Required, TypedDict

from .shared_params.url import URL
from .shared_params.param_type import ParamType

__all__ = ["PipelineRegisterParams"]


class PipelineRegisterParams(TypedDict, total=False):
    pipeline_id: Required[str]

    input_dataset_schema: Required[Dict[str, ParamType]]

    metadata: Dict[str, Union[bool, float, str, Iterable[object], object, None]]

    provider_pipeline_id: str

    provider_id: str
