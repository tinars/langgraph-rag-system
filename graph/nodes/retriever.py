from typing import Any, Dict

from graph.state import GraphStae
from ingestion import retriever

def retrieve(state: GraphStae) -> Dict[str, Any]:
    print("---RETRIEVE---")

    question = state["question"]
    documents = retriever.invoke(question)
    return {"documents": documents, "question": question}