# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .shared.return_type import ReturnType

__all__ = ["SDGFn"]


class SDGFn(BaseModel):
    identifier: str

    provider_id: str

    type: Literal["sdg_function"]

    description: Optional[str] = None
