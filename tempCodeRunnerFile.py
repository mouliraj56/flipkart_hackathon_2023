import os
import streamlit as st
import chainlit as cl
from langchain import HuggingFaceHub, PromptTemplate, LLMChain
import json
from fuzzywuzzy import fuzz

# Set the HuggingFace Hub API token
os.environ['API_KEY'] = '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'

# Load the LLM model
model_id = 'tiiuae/falcon-7b-instruct'
falcon_llm = HuggingFaceHub(huggingfacehub_api_token=os.environ['API_KEY'],
                            repo_id=model_id,
                            model_kwargs={"temperature": 0.8, "max_new_tokens": 2000})

template = """
You are an AI assistant that provides helpful answers to user queries.
{question}
"""
prompt = PromptTemplate(template=template, input_variables=['question'])

# Create an LLMChain
chain = LLMChain(llm=falcon_llm, prompt=prompt)

# Define a function to run the chain
def run_chain(question):
    return chain.run(question)

# Function to find the best-matched product
def find_best_matched_products(products, prompt, category):
    matched_products = []
    
    for product in products:
        if product["sub_category"] == category:
            description = product.get("description", "")
            similarity = fuzz.partial_ratio(prompt.lower(), description.lower())
            if similarity > 50:  # Adjust similarity threshold as needed
                matched_products.append(product)
    
    return matched_products

# Create a Streamlit app
st.title("Outfit Generator")

# Allow user to upload JSON file
uploaded_file = st.file_uploader("Upload a JSON file", type=["json"])

# Get the user's prompt
prompt_input = st.text_input("Provide a prompt for outfit suggestion")

# Process uploaded JSON file
if uploaded_file and prompt_input:
    json_data = json.load(uploaded_file)
    
    # Search uploaded JSON data based on the prompt
    best_match_bottomwear = find_best_matched_products(json_data, prompt_input, "Bottomwear")
    best_match_topwear = find_best_matched_products(json_data, prompt_input, "Topwear")
    best_match_footwear = find_best_matched_products(json_data, prompt_input, "Footwear")
    best_match_accessories = find_best_matched_products(json_data, prompt_input, "Accessory")  # Replace "Accessory" with the actual category name for accessories
    
    # Run the chain with the prompt and display results
    results = run_chain(prompt_input)
    st.write("Chatbot's Response:")
    st.write(results)
    
    # Display outfit suggestion if all categories have matches
    if best_match_bottomwear and best_match_topwear and best_match_footwear and best_match_accessories:
        st.write("Complete Outfit Suggestion:")
        st.image(best_match_topwear[0]["images"][0], caption=best_match_topwear[0]["title"], width=200)
        st.image(best_match_bottomwear[0]["images"][0], caption=best_match_bottomwear[0]["title"], width=200)
        st.image(best_match_footwear[0]["images"][0], caption=best_match_footwear[0]["title"], width=200)
        
        st.write("Accessory Suggestions:")
        for accessory in best_match_accessories:
            st.image(accessory["images"][0], caption=accessory["title"], width=200)
    else:
        st.write("No complete outfit found for the prompt.")

# If user hasn't provided prompt or uploaded file, display instructions
if not uploaded_file:
    st.write("Please upload a JSON file.")
if not prompt_input:
    st.write("Please provide a prompt for outfit suggestion.")

