import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers
import time

# streamlit run app.py


# Function to get response from LLama 2 model
def getLLamaresponse(input_text, no_words, blog_style):
    # Create an LLM
    llm = CTransformers(
        model="model/llama-2-7b-chat.ggmlv3.q8_0.bin",
        model_type="llama",
        config={"max_new_tokens": 512, "temperature": 0.01},
    )

    # Create a prompt template
    prompt = PromptTemplate(
        input_variables=["input_text", "no_words", "blog_style"],
        template="Write a blog post in {blog_style} style about {input_text} within {no_words} words and complete it.",
    )

    # Generate the response from the LLama 2 model
    response = llm(
        prompt.format(blog_style=blog_style, input_text=input_text, no_words=no_words)
    )
    return response


# Simulated function to mimic ChatGPT typing responses
def chat_typing_effect(text):
    message_placeholder = st.empty()  # Create an empty placeholder for the message
    message = ""
    typing_speed = 0.05  # Adjust the speed of typing here

    # Simulate typing effect by adding characters one by one
    for char in text:
        message += char
        message_placeholder.markdown(
            f"<p style='font-family: Poppins, sans-serif; color: #FC00FF;'>{message}</p>",
            unsafe_allow_html=True,
        )
        time.sleep(typing_speed)


# Improved UI setup
st.set_page_config(
    page_title="LLama2 Blog Generator",
    page_icon="📝",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600&display=swap');
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  font-family: "Poppins", sans-serif;
}

h1{
    margin: 0;
  padding: 0;
  box-sizing: border-box;
  font-family: "Poppins", sans-serif;
}
#text_input_1{
    
  box-sizing: border-box;
  font-family: "Poppins", sans-serif;
}

aria-label{
   font-family: "Poppins", sans-serif; 
}
.st-emotion-cache-1inwz65 ew7r33m0{
    font-family: "Poppins", sans-serif !important;
}

#provide-the-blog-details{
    font-family: "Poppins", sans-serif;
}
#generated-blog-post{
    font-family: "Poppins", sans-serif;
}

    .reportview-container {
        background: linear-gradient(135deg, #f2f2f2 30%, #d9d9d9 100%);
        padding-top: 20px;
    }
    #bdac8952{
        font-family: 'Poppins', sans-serif;
        font-weight: 700;
        font-size: 2.5rem;
        background: linear-gradient(90deg, #00DBDE 0%, #FC00FF 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        padding: 2rem;
    }
    
    
    .sidebar .sidebar-content {
        background-color: #f7f7f7;
    }
     /* Custom style for buttons */
    .stButton>button {
        background: linear-gradient(90deg, #00DBDE 0%, #FC00FF 100%);
        color: white !important;
        padding: 10px 24px;
        border-radius: 8px;
        font-size: 16px;
        border: none !important;
    }

    /* Change button hover effect */
    .stButton>button:hover {
        background: linear-gradient(90deg, #00B5FF 0%, #FF0080 100%);
    }
    
    
    </style>
    """,
    unsafe_allow_html=True,
)

# Header
st.markdown("<h1>Generate Stunning Blogs with AI ✨</h1>", unsafe_allow_html=True)

# Sidebar for options
st.sidebar.title("Blog Configuration")
# input_text = st.sidebar.text_input(
#     "Enter the Blog Topic", placeholder="E.g. The Future of AI"
# )
no_words = st.sidebar.slider("Number of words", 100, 1000, 300, step=50)
blog_style = st.sidebar.radio(
    "Choose Blog Audience", ("Researchers", "Data Scientist", "Common People")
)

# Column Layout
# st.write("### Provide the Blog Details")
with st.form(key="blog_form"):
    input_text = st.text_input("Blog Topic", placeholder="Type the topic here...")

    # Submit Button
    submit_button = st.form_submit_button(label="Generate Blog")

# Adding a progress bar during processing
if submit_button:
    if input_text:
        with st.spinner("Generating your blog..."):
            blog_response = getLLamaresponse(input_text, no_words, blog_style)
        st.success("Blog generated successfully!")

        # Display the generated blog
        st.markdown("### Generated Blog Post")
        # st.write(blog_response)
        chat_typing_effect(blog_response)
    else:
        st.error("Please provide a blog topic.")

# Footer
st.sidebar.markdown(
    """
    ---
    Made with 💻 by Soumik Bose
    """
)
