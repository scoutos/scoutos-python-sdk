# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.unchecked_base_model import UncheckedBaseModel


class BlockRun(UncheckedBaseModel):
    block_archetype_id: str
    block_type: str
    block_id: str
    block_display_name: typing.Optional[str] = None
    block_inputs: typing.Dict[str, typing.Optional[typing.Any]]
    block_output: typing.Optional[typing.Any] = None
    config: typing.Dict[str, typing.Optional[typing.Any]]
    metadata: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = None
    elapsed_time_ms: typing.Optional[int] = None
    cost: typing.Optional[float] = None
    status: typing.Optional[str] = None
    timestamp_start: typing.Optional[dt.datetime] = None
    timestamp_end: typing.Optional[dt.datetime] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
