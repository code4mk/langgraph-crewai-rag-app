from crewai import Crew, Process
from .movie_agents import MovieAgents
from .movie_tasks import MovieTasks

class MovieCrew:
    def __init__(self, llm, movie_info):
        self.llm = llm
        self.movie_info = movie_info

    def run(self):
        agents = MovieAgents(self.llm)
        tasks = MovieTasks()

        theme_analyst = agents.theme_analyst_agent()
        technical_analyst = agents.technical_analyst_agent()

        theme_analysis_task = tasks.theme_analysis_task(theme_analyst, self.movie_info)
        technical_analysis_task = tasks.technical_analysis_task(technical_analyst, self.movie_info)

        crew = Crew(
            agents=[theme_analyst, technical_analyst],
            tasks=[theme_analysis_task, technical_analysis_task],
            verbose=True,
            process=Process.sequential,
        )

        results = crew.kickoff()
  
    
        return {
            'theme_analysis': results.tasks_output[0].raw,
            'technical_analysis': results.tasks_output[1].raw
        }