from src.vector_store import VectorStoreBuilder
from src.recommender import AnimeRecommender
from config.config import GROQ_API_KEY, MODEL_NAME
from utils.custom_exception import CustomException
from utils.logger import get_logger

logger  = get_logger(__name__)

class AnimeRecommendationPipeline:

    def __init__(self, persist_dir = 'chroma_db'):

        try:
            logger.info("Initializing Recommendation Pipeline")
            vector_build = VectorStoreBuilder(csv_path = "", persist_dir = persist_dir)
            retriever = vector_build.load_vector_store().as_retriever()
            self.recommender = AnimeRecommender(retriever,GROQ_API_KEY,MODEL_NAME)
            logger.info("Pipeline Initialized succesfully")
        
        except Exception as e:

            logger.error(f"Error initializing Recommendation pipeline {e}")
            raise CustomException("Error initializing Recommendation Pipeline",e)
        
    def recommend(self, query:str):

        try:
            logger.info(f"Recieved a Query : {query}")
            recommendation  = self.recommender.get_recommendation(query)
            logger.info("Recommendation succesfully made")
            return recommendation
        except Exception as e:

            logger.error(f"error making recommendation {e}")
            raise CustomException("Error while making recommendation",e)
