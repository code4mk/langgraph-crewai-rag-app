def invoke_workflow():
  from src.the_langgraph.workflow import Workflow
  inputs = {"question": "How did the rise of television in the 1950s impact the film industry?"}
  app = Workflow().app

  abc = app.invoke(input=inputs)
  print( f'question: {abc.get("question")}')
  print( f'final asnwer (analysis): {abc.get("analysis_output")}')


def stream_workflow():
  from src.the_langgraph.workflow import Workflow

  inputs = {"question": "How did the rise of television in the 1950s impact the film industry?"}
  app = Workflow().app

  # Assuming the app.stream() method directly supports yielding streaming responses
  for response_chunk in app.stream(input=inputs):
      print(response_chunk)
      
invoke_workflow()
#stream_workflow()



