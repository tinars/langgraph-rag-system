from typing import Any, Dict

from dotenv import load_dotenv
from langchain_core.documents import Document
from langchain_tavily import TavilySearch

from graph.state import GraphStae

load_dotenv()
web_search_tool = TavilySearch(max_results=3)


def web_search(state: GraphStae) -> Dict[str, Any]:
    print("---WEB SEARCH---")
    question = state["question"]
    if "documents" in state:
        documents = state["documents"]
    else:
        documents = None

    tavily_results = web_search_tool.invoke({"query": question})["results"]
    joined_tavily_result = "\n".join(
        [tavily_result["content"] for tavily_result in tavily_results]
    )
    web_results = Document(page_content=joined_tavily_result)
    if documents is not None:
        documents.append(web_results)
    else:
        documents = [web_results]
    return {"documents": documents, "question": question}


if __name__ == "__main__":
    result=web_search(state={"question": "agent memory", "documents": None})
    print(result)