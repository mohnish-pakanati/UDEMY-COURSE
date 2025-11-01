from langchain_classic.chains import RetrievalQA
from langchain_groq import ChatGroq
from src.prompt_template import get_anime_prompt

class AnimeRecommender:
    def __init__(self, retriever, api_key:str, model_name:str):

        # Initialize prompt template
        self.prompt_template = get_anime_prompt()

        # Initialize groq chat
        self.llm = ChatGroq(api_key=api_key, model=model_name, temperature=0)

        # Initialize retrieverqa
        self.qa_chain = RetrievalQA.from_chain_type(
            llm=self.llm,
            chain_type="stuff", # what it does is pull all the context/documents into a single prompt
            retriever=retriever,
            return_source_documents=True, # what it does is return the source documents along with the answer
            chain_type_kwargs={"prompt": self.prompt_template}
        )
    
    # create a class to run qa chain
    def get_recommendations(self, query:str):
        result = self.qa_chain.invoke({"query": query})
        return result['result']