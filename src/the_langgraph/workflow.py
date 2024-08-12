from langgraph.graph import StateGraph
from .state import MovieState
from .nodes import Nodes

class Workflow:
    def __init__(self):
        # Initialize the state graph with the GraphState type
        workflow = StateGraph(MovieState)
        
        # Create an instance of the Nodes class
        nodes = Nodes()
        
        # Add nodes to the workflow with associated methods
        workflow.add_node('research_movie', nodes.research_movie)
        workflow.add_node('analysis_movie', nodes.analysis_movie)
        
        # Define the edges between nodes
        workflow.set_entry_point("research_movie")
        workflow.add_edge('research_movie', 'analysis_movie')
        
        # Compile the workflow into an executable application
        self.app = workflow.compile()
