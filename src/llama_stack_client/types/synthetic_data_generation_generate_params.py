# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Union
from typing_extensions import Literal, Required, TypedDict

from .shared_params.message import Message

__all__ = ["SyntheticDataGenerationGenerateParams"]


class SyntheticDataGenerationGenerateParams(TypedDict, total=False):
    dataset_id: str

    pipeline_id: str

    metadata: Dict[str, Union[bool, float, str, Iterable[object], object, None]]
