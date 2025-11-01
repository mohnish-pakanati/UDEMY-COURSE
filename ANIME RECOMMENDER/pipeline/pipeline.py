from src.vector_store import VectorStoreBuilder
from src.recommender import AnimeRecommender
from config.config import GROQ_API_KEY, MODEL_NAME
from utils.logger import get_logger
from utils.custom_exceptions import CustomException

logger = get_logger(__name__)

# Assume we already have db initialised
# Initialise vector store 
# Initialise recommender system

class AnimeRecommenderPipeline:
    def __init__(self, persist_directory="chroma_db"):
        try:
            logger.info("Initializing Anime Recommender Pipeline...")
            # Initialize vector store
            vector_builder = VectorStoreBuilder(csv_path='', persist_dir=persist_directory) # csv_path is not needed here as we are loading existing vector store

            retriever = vector_builder.load_vector_store().as_retriever()
            # Initialize recommender system
            self.recommender = AnimeRecommender(
                retriever=retriever,
                api_key=GROQ_API_KEY,
                model_name=MODEL_NAME
            )
            logger.info("Anime Recommender Pipeline initialized successfully.")
        except Exception as e:
            logger.error(f"Error initializing Anime Recommender Pipeline: {e}")
            raise CustomException(f"Initialization failed: {e}")

    def get_recommendations(self, query: str):
        try:
            logger.info('f" Received a query for recommendations: {query}')
            recommendations = self.recommender.get_recommendations(query)
            logger.info("Recommendations generated successfully.")
            return recommendations
        except Exception as e:
            logger.error(f"Error generating recommendations: {e}")
            raise CustomException(f"Recommendation generation failed: {e}")