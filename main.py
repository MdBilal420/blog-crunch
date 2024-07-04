import streamlit as st
from langchain_openai import OpenAI
from langchain import PromptTemplate

st.set_page_config(
    page_title = "Blog Post Generator"
)

st.title("Blog Crunch")
st.write("For all of your tech blogs with their summaries.")

openai_api_key = st.sidebar.text_input(
    "OpenAI API Key",
    type = "password"
)




def generate_blog(topic):
    llm = OpenAI(openai_api_key=openai_api_key)
    template = """
    As experienced startup and venture capital writer, 
    generate a 400-word blog post about {topic}
    
    Your response should be in this format:
    First, print the blog post with header and subheader. Header and subheader should be bold
    Then, sum the total number of words on it and print the result like this: This post has X words.
    """

    prompt = PromptTemplate(
        input_variables = ["topic"],
        template = template
    )

    query = prompt.format(topic=topic)
    response = llm(query, max_tokens=2048)
    return response

def summarize_text(text):
    llm = OpenAI(openai_api_key=openai_api_key)
    template = """
    Summarize the full text about {text} in 50 to 100 words.
    """
    prompt = PromptTemplate(
        input_variables = ["text"],
        template = template
    )
    query = prompt.format(text=text)
    response = llm(query, max_tokens=2048)
    return response



topic_text = st.text_input("Enter topic: ")
blog = generate_blog(topic_text)

tab1, tab2= st.tabs(["Full Blog", "Blog Summary"])

with tab1:
    if(not openai_api_key):
        st.warning("Please enter API key")
    else:
        st.write(blog)


with tab2:
    if(not openai_api_key):
        st.warning("Please enter API key")
    else:
        summary = summarize_text(blog)
        st.write(summary)