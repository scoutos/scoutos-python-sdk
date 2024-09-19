# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import typing
from .actor import Actor
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class WorkflowRunStartedData(UncheckedBaseModel):
    actor: typing.Optional[Actor] = None
    workflow_id: str
    workflow_run_id: typing.Optional[str] = None
    input: typing.Dict[str, typing.Optional[typing.Any]]
    session_id: typing.Optional[str] = None
    state: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = None
    workflow_config: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
