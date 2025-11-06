import os
from dotenv import load_dotenv
from typing import Any, Literal, Optional
from pydantic import BaseModel, Field
from utils.config_loader import load_config
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI


class ConfigLoader():

    def __init__(self):
        print(f"Loading configuration...")
        self.config = load_config()

    def __getitem__(self, key):
        return self.config[key]

class ModelLoader(BaseModel):
    
    model_provider: Literal["groq", "openai", "azure"] = "groq"
    config: Optional[ConfigLoader]=Field(default=None, exclude=True)


    def model_post_init(self, __context:Any)->None:
        self.config = ConfigLoader()


    class Config:
        arbitrary_types_allowed = True

    
    def load_llm(self):
        """Load and return the language model based on the provider specified."""

        print("LLM loading...")
        print(f"Loading model from provider: {self.model_provider}")
        if self.model_provider == "groq":
            print("Loading LLM from Groq...")
            groq_api_key = os.getenv("GROQ_API_KEY")
            model_name = self.config["llm"]["groq"]["model_name"]
            llm=ChatGroq(model=model_name, api_key=groq_api_key)

        elif self.model_provider == "openai":
            print("Loading LLM from OpenAI...")
            openai_api_key = os.getenv("OPENAI_API_KEY")
            model_name = self.config["llm"]["openai"]["model_name"]
            llm=ChatOpenAI(model="o4-mini", api_key=openai_api_key)

        # elif self.model_provider == "azure":
        #     print("Loading LLM from Azure...")
        #     azure_api_key = os.getenv("AZURE_API_KEY")
        #     model_name = self.config["llm"]["azure"]["model_name"]
        #     llm=ChatAzure(model=model_name, api_key=azure_api_key)

        
        
        else:
            raise ValueError(f"Unsupported model provider: {self.model_provider}")
        
        return llm