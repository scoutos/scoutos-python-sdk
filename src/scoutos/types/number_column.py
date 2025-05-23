# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.unchecked_base_model import UncheckedBaseModel
from .number_column_default import NumberColumnDefault
from .number_column_max_value import NumberColumnMaxValue
from .number_column_min_value import NumberColumnMinValue


class NumberColumn(UncheckedBaseModel):
    column_id: typing.Optional[str] = None
    column_display_name: typing.Optional[str] = None
    column_type: typing.Literal["number"] = "number"
    data_type: typing.Optional[typing.Literal["number"]] = None
    hidden: typing.Optional[bool] = None
    default: typing.Optional[NumberColumnDefault] = None
    min_value: typing.Optional[NumberColumnMinValue] = None
    max_value: typing.Optional[NumberColumnMaxValue] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
