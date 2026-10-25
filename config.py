
# Forge application configuration

APP_NAME = "Forge.AI"
APP_VERSION = "1.0.0"


# LLM configuration
MODEL_PROVIDER = "google"
MODEL_NAME = "gemini-2.5-flash"
TEMPERATURE = 0.2


# Investigation configuration
SEARCH_DEPTH = "medium"

SEARCH_PROFILES = {
    "low": {
        "max_directory_depth": 2,
        "max_files_to_inspect": 10,
        "max_investigation_steps": 3,
    },
    "medium": {
        "max_directory_depth": 4,
        "max_files_to_inspect": 25,
        "max_investigation_steps": 6,
    },
    "high": {
        "max_directory_depth": 6,
        "max_files_to_inspect": 50,
        "max_investigation_steps": 10,
    },
}


# Debug configuration
DEBUG = True


# Execution limits
REQUEST_TIMEOUT = 60
MAX_REPAIR_ATTEMPTS = 2
