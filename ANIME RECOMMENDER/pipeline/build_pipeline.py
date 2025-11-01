from src.data_loader import AnimeDataLoader
from src.vector_store import VectorStoreBuilder
from dotenv import load_dotenv
from utils.logger import get_logger
from utils.custom_exceptions import CustomException


load_dotenv()

logger = get_logger(__name__)

def main():
    try:
        logger.info("Starting the build pipeline...")
        # Load and preprocess data
        loader = AnimeDataLoader("data/anime.csv", "data/anime_updated.csv")
        processed_csv = loader.load_and_process()
        logger.info("Data loaded and processed successfully.")

        vector_builder = VectorStoreBuilder(csv_path=processed_csv)
        vector_builder.build_and_save_vectorstore()
        logger.info("Vector store built and persisted successfully.")

        logger.info("Build pipeline completed successfully.")
    
    except Exception as e:
        logger.error(f"Error in build pipeline: {e}")
        raise CustomException(f"Build pipeline failed: {e}")
    
if __name__ == "__main__":
    main()