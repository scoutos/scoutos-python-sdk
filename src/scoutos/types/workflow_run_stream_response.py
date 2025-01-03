# This file was auto-generated by Fern from our API Definition.

import typing
from .workflow_run_started import WorkflowRunStarted
from .workflow_run_completed import WorkflowRunCompleted
from .workflow_run_failed import WorkflowRunFailed
from .block_run_started import BlockRunStarted
from .block_run_completed import BlockRunCompleted
from .block_run_failed import BlockRunFailed
from .block_state_updated import BlockStateUpdated

WorkflowRunStreamResponse = typing.Union[
    WorkflowRunStarted,
    WorkflowRunCompleted,
    WorkflowRunFailed,
    BlockRunStarted,
    BlockRunCompleted,
    BlockRunFailed,
    BlockStateUpdated,
]