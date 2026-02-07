import os
from dotenv import load_dotenv  
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch

load_dotenv(override=True)

gemini_api_key = os.getenv("GEMINI_API_KEY")

@tool
def triple(num: float) -> float:
    """
    param num: a number to triple
    return: the tripled of the input number
    """
    return float(num) * 3

tools = [TavilySearch(max_results=1), triple]

llm = ChatOpenAI(
    model="gemini-2.5-flash", 
    api_key= gemini_api_key,
    openai_api_base="https://generativelanguage.googleapis.com/v1beta/openai/",
    temperature=0
).bind_tools(tools)