from langchain.prompts import PromptTemplate
from typing import Dict
from termcolor import colored

from .utils import get_openai_llm, get_pinecone_vectorstore
from .state import MovieState
from src.the_crewai.movie_crew import MovieCrew

class Nodes:
    def __init__(self):
        self.llm = get_openai_llm()
        self.vectorstore = get_pinecone_vectorstore()
        
    def research_movie(self, state: MovieState):
        query = state['question']
        docs = self.vectorstore.similarity_search(query, k=3)
        context = "\n".join([doc.page_content for doc in docs])
        
        template = """
        Based on the following question and context,
        provide detailed information about the movie:
        
        Question: {question}
        
        Context:
        {context}
        
        Provide a comprehensive overview of the movie,
        including its plot, cast, director, release
        date, and any other relevant details:
        """
        
        research_prompt_template = PromptTemplate(
            input_variables=["question", "context"],
            template=template
        )
        
        research_chain = research_prompt_template | self.llm
        ai_msg = research_chain.invoke({"question": state['question'], "context": context})
        response = ai_msg.content
        
        state['research_output'] = response
        print(colored(f"Researcher 👩🏿‍💻: {response}", 'cyan'))
        return state
    
    def analysis_movie(self, state: MovieState):
        movie_crew = MovieCrew(self.llm, state['research_output'])
        analysis_results = movie_crew.run()
        
        
        
        theme_analysis = analysis_results.get('theme_analysis', 'Theme analysis not available')
        technical_analysis = analysis_results.get('technical_analysis', 'Technical analysis not available')
        
        print(colored("Movie Analysis 🧑🏼‍💻:", 'green'))
        print(colored(f"\n\nTheme Analysis: {theme_analysis}", 'green'))
        print(colored(f"\n\nTechnical Analysis: {technical_analysis}", 'green'))
        state['analysis_output'] = analysis_results
        return state