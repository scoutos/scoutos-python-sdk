# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.unchecked_base_model import UncheckedBaseModel
from .trafilatura_output_trafilatura_type import TrafilaturaOutputTrafilaturaType


class TrafilaturaOutput(UncheckedBaseModel):
    text_extractor_type: typing.Literal["trafilatura"] = "trafilatura"
    trafilatura_type: TrafilaturaOutputTrafilaturaType = pydantic.Field()
    """
    Choose the Trafilatura extraction algorithm to use.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
