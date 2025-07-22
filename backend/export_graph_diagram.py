from graph import build_medical_graph

def export_mermaid():
    # Erstelle den Graphen wie im Backend
    graph = build_medical_graph()
    # Hole das Mermaid-Diagramm
    mermaid_code = graph.get_graph().draw_mermaid()
    print("--- Mermaid Diagram ---\n")
    print(mermaid_code)

if __name__ == "__main__":
    export_mermaid() 