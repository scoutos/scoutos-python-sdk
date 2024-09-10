# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class ColumnTypeItemJson(UniversalBaseModel):
    column_id: typing.Optional[str] = None
    column_display_name: typing.Optional[str] = None
    default_value: typing.Optional[str] = None
    data_type: typing.Optional[typing.Literal["json"]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
