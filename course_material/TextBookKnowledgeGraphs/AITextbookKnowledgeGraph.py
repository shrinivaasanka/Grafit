def ai_textbook_knowledgegraph(concept="",model="gpt-5.6"):
    from QuestionAnswering import OpenAIQuestionAnswering
    query="Create a knowledge graph for "+concept+" in DOT format and render it"
    OpenAIQuestionAnswering(question=query,model=model)

def langchain_rag(concept="",model="openai:gpt-5.6"):
    from deepagents import create_deep_agent
    from langchain.messages import HumanMessage
    baseline_agent = create_deep_agent( model=model, tools=[], system_prompt=("Textbook Knowledge Graphs for Competitive Examination Question-Answering"),)
    result = baseline_agent.invoke({"messages": [HumanMessage(content=concept)]}
)
    print(result["messages"][-1].text)

def examination_question_answer_knowledgegraph(examination="UPSC"):
    query="Create a knowledge graph for a random question and answer from " + examination + " and quantify the meaningfulness of knowledge graph"
    langchain_rag(concept=query)

if __name__=="__main__":
    #ai_textbook_knowledgegraph(concept="Michelsen Morley Interferometer")
    #ai_textbook_knowledgegraph(concept="Berry-Esseen Central Limit Theorem")
    #ai_textbook_knowledgegraph(concept="Proof of Lorentz transformation and Special relativity")
    #langchain_rag(concept="Choose a set of 2 random questions from IIT-JEE Mathematics syllabus and solve them from textbooks.")
    #langchain_rag(concept="Choose a set of 5 random questions from Tamilnadu state board class 12 physics syllabus (english medium) and solve them from textbooks.")
    #langchain_rag(concept="Choose a set of 5 random NEET questions and solve them from textbooks.")
    #langchain_rag(concept="Choose a set of 2 random UPSC Civil Services Examination questions and solve them from textbooks.")
    examination_question_answer_knowledgegraph(examination="UPSC")
    examination_question_answer_knowledgegraph(examination="NEET")
    examination_question_answer_knowledgegraph(examination="IIT-JEE")
    examination_question_answer_knowledgegraph(examination="Tamilnadu state board class 12 mathematics syllabus (english medium)")

