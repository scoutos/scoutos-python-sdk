# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
from .workflow_run_event_names import WorkflowRunEventNames
from .workflow_run_event_data import WorkflowRunEventData
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import typing
import pydantic


class WorkflowRunEvent(UncheckedBaseModel):
    name: WorkflowRunEventNames
    data: WorkflowRunEventData

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
