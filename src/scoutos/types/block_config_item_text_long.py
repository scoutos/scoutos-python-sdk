# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.unchecked_base_model import UncheckedBaseModel
from .block_config_item_text_long_value import BlockConfigItemTextLongValue


class BlockConfigItemTextLong(UncheckedBaseModel):
    id: str
    display_name: str
    type: typing.Literal["text-long"] = "text-long"
    default_value: typing.Optional[str] = None
    value: typing.Optional[BlockConfigItemTextLongValue] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
