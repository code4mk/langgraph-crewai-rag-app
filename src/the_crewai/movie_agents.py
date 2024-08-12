from crewai import Agent

class MovieAgents:
    def __init__(self, llm):
        self.llm = llm

    def theme_analyst_agent(self):
        return Agent(
            role='Theme Analyst',
            goal='Analyze the themes and symbolism of the movie',
            backstory='You are an expert in film analysis, specializing in identifying and interpreting themes and symbols in movies.',
            llm=self.llm
        )

    def technical_analyst_agent(self):
        return Agent(
            role='Technical Analyst',
            goal='Analyze the cinematography, visual style, and technical aspects of the movie',
            backstory='You are a seasoned cinematographer and film technician with a keen eye for visual storytelling and technical excellence in movies.',
            llm=self.llm
        )