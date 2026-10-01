def ai_textbook_knowledgegraph(concept="",model="gpt-6-astra"):
    from QuestionAnswering import OpenAIQuestionAnswering
    query="Create a knowledge graph for "+concept+" in DOT format and render it"
    OpenAIQuestionAnswering(question=query,model=model)

def langchain_rag(concept="",model="openai:gpt-6-astra"):
    from deepagents import create_deep_agent
    from langchain.messages import HumanMessage
    baseline_agent = create_deep_agent( model=model, tools=[], system_prompt=("Textbook Knowledge Graphs for Competitive Examination Question-Answering"),)
    result = baseline_agent.invoke({"messages": [HumanMessage(content=concept)]}
)
    print(result["messages"][-1].text)
    return result["messages"][-1].text

def langchain_graph_rag(concepts=[],query=""):
    from langchain_core.documents import Document
    from langchain_core.vectorstores.in_memory import InMemoryVectorStore
    from langchain_graph_retriever import GraphRetriever
    from langchain_core.embeddings import FakeEmbeddings
    import pprint
    n=0
    documents=[]
    for concept in concepts:
         result=langchain_rag(concept=concept,model="openai:gpt-6-astra")
         doc = Document(id="doc"+str(n), page_content=result,)
         documents.append(doc)
         n+=1
    store = InMemoryVectorStore.from_documents(documents, FakeEmbeddings(size=8))
    retriever = GraphRetriever(store=store, edges=[("mentions", "$id")])
    results=retriever.invoke(query)
    for result in results:
    	print("Graph RAG result for query ",query,":")
    	pprint.pprint(result)

def academic_publications_proofnet_knowledgegraph(publication,kgid=1):
    publicationfile=open(publication,"r")
    publicationtext=publicationfile.read()
    #resulttext=langchain_rag(concept=publicationtext)
    kggen_knowledge_graph(publicationtext,kgid=kgid)

def examination_question_answer_knowledgegraph(examination="UPSC",formattedquery="",kgid=1):
    resulttext=langchain_rag(concept=formattedquery)
    kggen_knowledge_graph(resulttext,kgid=kgid)

def kggen_knowledge_graph(resulttext,kgid):
    from kg_gen import KGGen
    import os
    import networkx as nx
    from networkx.drawing.nx_pydot import write_dot
    envapikey=os.environ["OPENAI_API_KEY"]
    kg = KGGen( model="openai/gpt-6-astra",temperature=1.0,api_key=envapikey)
    knowledgegraph = kg.generate(input_data=resulttext, context="Question-Answer Knowledge Graphs")
    print("KGGen Knowledge Graph:",knowledgegraph)
    nxknowledgegraph=nx.DiGraph()
    for subject,predicate,object in knowledgegraph.relations:
         nxknowledgegraph.add_edge(subject,object,label=predicate)
    #write_dot(knowledgegraph, "./testlogs/QAKnowledgeGraph"+str(kgid)+".dot")
    KGGen.visualize(knowledgegraph,"./testlogs/QAKnowledgeGraph"+str(kgid)+".html",open_in_browser=False)

if __name__=="__main__":
    #ai_textbook_knowledgegraph(concept="Michelsen Morley Interferometer")
    #ai_textbook_knowledgegraph(concept="Berry-Esseen Central Limit Theorem")
    #ai_textbook_knowledgegraph(concept="Proof of Lorentz transformation and Special relativity")
    #langchain_rag(concept="Choose a set of 2 random questions from IIT-JEE Mathematics syllabus and solve them from textbooks.")
    #langchain_rag(concept="Choose a set of 5 random questions from Tamilnadu state board class 12 physics syllabus (english medium) and solve them from textbooks.")
    #langchain_rag(concept="Choose a set of 5 random NEET questions and solve them from textbooks.")
    #langchain_rag(concept="Choose a set of 2 random UPSC Civil Services Examination questions and solve them from textbooks.")
    #query=f"Create a knowledge graph for a random question and answer from IIT-JEE and quantify the meaningfulness of knowledge graph"
    #langchain_rag(concept=query,model="openai:gpt-5.6")
    #exam="UPSC"
    #examination_question_answer_knowledgegraph(examination=exam,formattedquery=f"Choose a random question from {exam} and answer it",kgid=1)
    #exam="NEET"
    #examination_question_answer_knowledgegraph(examination=exam,formattedquery=f"Choose a random question from {exam} and answer it",kgid=2)
    #exam="IIT-JEE"
    #examination_question_answer_knowledgegraph(examination=exam,formattedquery=f"Choose a random question from {exam} and answer it",kgid=3)
    #exam="Tamilnadu state board class 12 physics english medium"
    #examination_question_answer_knowledgegraph(examination=exam,formattedquery=f"Choose a random question from {exam} and answer it",kgid=4)
    #academic_publications_proofnet_knowledgegraph("../NeuronRain/LinuxKernelAndCloud/code/Spark_Word2Vec_Bibliography.txt",kgid=5)
    #academic_publications_proofnet_knowledgegraph("../NeuronRain/LinuxKernelAndCloud/code/Spark_Word2Vec_SemanticScholar.txt",kgid=6)
    #academic_publications_proofnet_knowledgegraph("./GoogleScholarPublicationsAbstract.txt",kgid=7)
    #langchain_graph_rag(concepts=["Choose a set of 2 random questions from IIT-JEE Mathematics syllabus and solve them from textbooks","Choose a set of 5 random NEET questions and solve them from textbooks."],query="theorem")
    langchain_graph_rag(concepts=["Prime Number Theorem","Riemann Hypothesis","Distribution of Primes"],query="Function")
