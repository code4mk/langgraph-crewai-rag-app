from typing import List

from typing_extensions import TypedDict


class MovieState(TypedDict):
    question: str
    research_output: str
    analysis_output: str