#
# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project.
#

"""LLM Types."""
from typing import Generic, Protocol, TypeVar

from typing_extensions import Unpack

from .llm_io import (
    LLMInput,
    LLMOutput,
)

TIn = TypeVar("TIn", contravariant=True)
TOut = TypeVar("TOut")


class LLM(Protocol, Generic[TIn, TOut]):
    """LLM Protocol definition."""

    async def __call__(
        self,
        input: TIn,
        **kwargs: Unpack[LLMInput],
    ) -> LLMOutput[TOut]:
        """Invoke the LLM, treating the LLM as a function."""
        ...