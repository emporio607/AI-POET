import os
#from dotenv import load_dotenv
from langchain.schema import HumanMessage
import streamlit as st

#load_dotenv()

#from langchain.llms import AzureOpenAI
from langchain.chat_models import AzureChatOpenAI

AzureOpenAI_api_base = os.getenv("AZURE_API_BASE")
AzureOpenAI_api_version = os.getenv("AZURE_API_VERSION")
deployment_name = os.getenv("DEPLOYMENT_NAME")
AzureOpenAI_api_key = os.getenv("AZURE_API_KEY")
AzureOpenAI_api_type = "azure"

# print(AzureOpenAI_api_base)
# print(AzureOpenAI_api_version)
# print(deployment_name)
# print(AzureOpenAI_api_key)
# print(AzureOpenAI_api_type)

llm_chain = AzureChatOpenAI(
    openai_api_base=AzureOpenAI_api_base,
    openai_api_version=AzureOpenAI_api_version,
    deployment_name = deployment_name,
    openai_api_key = AzureOpenAI_api_key,
    openai_api_type=AzureOpenAI_api_type)

st.title("인공지능 시인")

theme = st.text_input('시의 주제를 제시해주세요')

if st.button('시 작성 요청하기'):
    message = HumanMessage(content = theme + "에 대한 시를 써줘")
    with st.spinner('시 작성 중...'):
        result = llm_chain([message])
        st.write(result)
# message = HumanMessage(content = theme + "에 대한 시를 써줘")
# print(llm_chain([message]))


#title = st.text_input('시의 주제를 제시하세요.')
#st.title("'_Streamlit_ is :blue[cool] :sunglasses:'")
#st.write('시의 주제는',title)