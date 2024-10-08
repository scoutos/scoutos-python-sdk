# This file was auto-generated by Fern from our API Definition.

import typing

WorkflowRunEventNames = typing.Union[
    typing.Literal[
        "workflow_run_started",
        "workflow_run_completed",
        "workflow_run_failed",
        "block_run_started",
        "block_run_completed",
        "block_run_failed",
        "block_state_updated",
    ],
    typing.Any,
]
