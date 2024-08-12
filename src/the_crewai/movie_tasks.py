from crewai import Task
from textwrap import dedent
from pydantic import BaseModel, Field


class MovieTasks:
    def theme_analysis_task(self, agent, movie_info):
        return Task(
            description=dedent(f"""
                Analyze the themes and symbolism in the following movie:
                {movie_info}
                Provide an in-depth analysis of the main themes, symbolic elements, and their significance in the context of the movie.
            """),
            agent=agent,
            expected_output="A comprehensive analysis of the movie's themes and symbolism, including main themes, symbolic elements, and their significance in the context of the movie.",
        )

    def technical_analysis_task(self, agent, movie_info):
        return Task(
            description=dedent(f"""
                Analyze the cinematography and visual style of the following movie:
                {movie_info}
                Provide a detailed analysis of the cinematographic techniques, visual aesthetics, and how they contribute to the storytelling.
            """),
            agent=agent,
            expected_output="A detailed analysis of the movie's cinematography and visual style, including cinematographic techniques, visual aesthetics, and their contribution to the storytelling.",
        )