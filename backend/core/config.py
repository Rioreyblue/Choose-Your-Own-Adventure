# # from typing import List
# # from pydantic_settings import BaseSettings
# # from pydantic import field_validator

# # class Settings(BaseSettings):

# #     DATABASE_URL: str
    
# #     API_PREFIX: str = "/api"
# #     DEBUG: bool = False
# #     ALLOWED_ORIGINS: str = ""
# #     # ALLOWED_ORIGINS: List[str] = []

# #     AGENT_ROUTER_API_KEY: str = ""
# #     AGENT_ROUTER_BASE_URL: str = "https://agentrouter.org/v1"

# #     @field_validator("ALLOWED_ORIGINS")
# #     def parse_allowed_origins(cls, v: str) -> List[str]:
# #         return v.split(",") if v else []

# #     class Config:
# #         env_file = ".env"
# #         env_file_encoding = "utf-8"
# #         case_sensitive = True


# # settings = Settings()
# # #api key change

    

    

# import json
# from typing import List
# from pydantic_settings import BaseSettings
# from pydantic import field_validator

# class Settings(BaseSettings):

#     DATABASE_URL: str
    
#     API_PREFIX: str = "/api"
#     DEBUG: bool = False
#     ALLOWED_ORIGINS: str = ""

#     AGENT_ROUTER_API_KEY: str = ""
#     AGENT_ROUTER_BASE_URL: str = "https://generativelanguage.googleapis.com/v1beta/openai/"
#     MODEL_NAME: str = "gemini-2.0-flash"

#     @field_validator("ALLOWED_ORIGINS")
#     def parse_allowed_origins(cls, v: str) -> List[str]:
#         if not v:
#             return []
#         if v.startswith("["):
#             try:
#                 return json.loads(v)
#             except Exception:
#                 pass
#         return [origin.strip() for origin in v.split(",") if origin.strip()]

#     class Config:
#         env_file = ".env"
#         env_file_encoding = "utf-8"
#         case_sensitive = True


# settings = Settings()

import json
from typing import List
from pydantic_settings import BaseSettings
from pydantic import field_validator


class Settings(BaseSettings):

    DATABASE_URL: str
    
    API_PREFIX: str = "/api"
    DEBUG: bool = False
    ALLOWED_ORIGINS: str = ""

    AGENT_ROUTER_API_KEY: str = ""
    AGENT_ROUTER_BASE_URL: str = "https://openrouter.ai/api/v1"
    MODEL_NAME: str = "openrouter/free"

    @field_validator("ALLOWED_ORIGINS")
    def parse_allowed_origins(cls, v: str) -> List[str]:
        if not v:
            return []
        if v.startswith("["):
            try:
                return json.loads(v)
            except Exception:
                pass
        return [origin.strip() for origin in v.split(",") if origin.strip()]

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = True


settings = Settings()