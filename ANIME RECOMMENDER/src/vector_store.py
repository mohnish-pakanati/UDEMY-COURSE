from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.document_loader.csv_loader import CSVLoader
from lanchain_huggingface_embedding import HuggingFaceEmbeddings

from dotenv import load_dotenv
load_dotenv()

class VectorStoreBuilder:
    def __init__(self, csv_path:str, persist_dir:str="chroma_db"):
        self.csv_path = csv_path
        self.persist_dir = persist_dir
        self.embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    
    def build_and_save_vectorstore(self):
        # load, split, embed, and save to disk

        loader = CSVLoader(file_path=self.csv_path, 
                           encoding='utf-8',
                           metadata_columns=[])
        data = loader.load()

        splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
        texts = splitter.split_documents(data)

        db = Chroma.from_documents(documents=texts, 
                                         embedding=self.embedding, 
                                         persist_directory=self.persist_dir)
        db.persist()

    def load_vector_store(self):
        db = Chroma(persist_directory=self.persist_dir, 
                    embedding_function=self.embedding)
        return db