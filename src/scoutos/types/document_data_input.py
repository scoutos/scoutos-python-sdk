# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import typing
from .document_content import DocumentContent
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class DocumentDataInput(UncheckedBaseModel):
    id: typing.Optional[str] = None
    columns: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = None
    display_name: typing.Optional[str] = None
    content: typing.Optional[typing.List[DocumentContent]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
