import os
import logging

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_groq import ChatGroq
from langchain_mistralai import ChatMistral

from config import (
    MODEL_NAME,
    TEMPERATURE,
    DEBUG,
)

load_dotenv()

logging.basicConfig(
    level=logging.DEBUG if DEBUG else logging.INFO
)

logger = logging.getLogger(__name__)


def initialize_models():
    models = []

    if os.getenv("GOOGLE_API_KEY"):
        try:
            gemini = ChatGoogleGenerativeAI(
                model=MODEL_NAME,
                temperature=TEMPERATURE,
            )
            models.append(("Gemini", gemini))
            logger.info("Gemini initialized.")
            return models
        except Exception as e:
            logger.error(f"Failed to initialize Gemini: {e}")
    else:
        logger.warning("Google API key is missing")

        if os.getenv("GROQ_API_KEY"):
            try:
                groq = ChatGroq(
                    model=MODEL_NAME,
                    temperature=TEMPERATURE,
                )
                models.append(("Groq", groq))
                logger.info("Groq initialized.")
                return models
            except Exception as e:
                logger.error(f"Failed to initialize Groq: {e}")
        else:
            logger.warning("There is no Groq API key found in the env folder please check")

            if os.getenv("MISTRAL_API_KEY"):
                try:
                    mistral = ChatMistral(
                        model=MODEL_NAME,
                        temperature=TEMPERATURE,
                    )
                    models.append(("Mistral", mistral))
                    logger.info("Mistral initialized.")
                    return models
                except Exception as e:
                    logger.error(f"Failed to initialize Mistral: {e}")
            else:
                logger.warning("There is no Mistral key")

                if not models:
                    raise RuntimeError(
                        "No LLM models could be initialized"
                    )

                return models    

