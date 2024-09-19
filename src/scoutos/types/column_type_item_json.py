# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import typing
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class ColumnTypeItemJson(UncheckedBaseModel):
    column_id: typing.Optional[str] = None
    column_display_name: typing.Optional[str] = None
    column_type: typing.Literal["json"] = "json"
    default_value: typing.Optional[str] = None
    data_type: typing.Optional[typing.Literal["json"]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
