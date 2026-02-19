from dotenv import load_dotenv
load_dotenv()
from graph.graph import  app
import warnings

if __name__=="__main__":
    print("Hello Advanced RAG")
    warnings.filterwarnings("ignore")
    print(app.invoke(input={"question":"what is agent memory?"}))