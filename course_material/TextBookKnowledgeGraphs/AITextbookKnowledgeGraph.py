from QuestionAnswering import OpenAIQuestionAnswering

def ai_textbook_knowledgegraph(concept="",model="gpt-5.5"):
    query="Create a knowledge graph for "+concept+" in DOT format and render it"
    OpenAIQuestionAnswering(question=query,model=model)

if __name__=="__main__":
    ai_textbook_knowledgegraph(concept="Michelsen Morley Interferometer")
    ai_textbook_knowledgegraph(concept="Berry-Esseen Central Limit Theorem")
    ai_textbook_knowledgegraph(concept="Proof of Lorentz transformation and Special relativity")
