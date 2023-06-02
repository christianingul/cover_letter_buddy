from langchain.chains import LLMChain, LLMRequestsChain
from constants import JOB_DESCRIPTION_TEMPLATE
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
import streamlit as st

def scrape_company_page(company_url: str):
    openai_secret = st.secrets.get("openai")
    openai_api_key = openai_secret.get("key")

    llm = ChatOpenAI(
        temperature=0, model_name= 'gpt-3.5-turbo', openai_api_key=openai_api_key
    )
    PROMPT = PromptTemplate(
        input_variables=["requests_result"],
        template=JOB_DESCRIPTION_TEMPLATE,
    )

    chain = LLMRequestsChain(llm_chain=LLMChain(llm=llm, prompt=PROMPT))

    inputs = {
        "url": company_url,
    }
    result = chain.run(inputs)
    return result
