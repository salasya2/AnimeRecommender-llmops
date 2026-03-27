from src.dataloader import AnimeDataLoader
from utils.custom_exception import CustomException
from utils.logger import get_logger
from src.vector_store import VectorStoreBuilder
from dotenv import load_dotenv

load_dotenv()

logger = get_logger(__name__)

def main():
    try:
        logger.info("Initializing Pipeline Building")
        dataloader = AnimeDataLoader("data/anime_with_synopsis.csv","data/anime_updated.csv")
        processed_data = dataloader.load_and_process()
        logger.info("Data Loaded and Processed Successfully")

        vector_builder = VectorStoreBuilder(processed_data)
        vector_builder.build_and_save_vectorstore()
        logger.info("Vector Store built successfully")
        logger.info("Pipeline built successfully")

    except Exception as e:

        logger.error(f"Error building the pipeline {e}")
        raise CustomException("Error building the pipeline",e)


if __name__=="__main__":
    main()