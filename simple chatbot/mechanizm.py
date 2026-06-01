from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
import os
load_dotenv()

llm=HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-V4-Flash",
    huggingfacehub_api_token=os.getenv("HUGGINGFACE_API_KEY")
)

model=ChatHuggingFace(llm=llm)

