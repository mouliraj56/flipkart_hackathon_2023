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
def find_best_matched_product(products, prompt):
    best_match = None
    highest_similarity = 0
    
    for product in products:
        title_similarity = fuzz.partial_ratio(prompt.lower(), product.get("title", "").lower())
        description_similarity = fuzz.partial_ratio(prompt.lower(), product.get("description", "").lower())
        
        details_similarity = 0
        for detail in product.get("product_details", []):
            details_similarity = max(details_similarity, fuzz.partial_ratio(prompt.lower(), list(detail.values())[0].lower()))
        
        overall_similarity = max(title_similarity, description_similarity, details_similarity)
        
        if overall_similarity > highest_similarity:
            highest_similarity = overall_similarity
            best_match = product
    
    return best_match

json_file_path = 'C:/Users/ASUS/Desktop/flipkart/flipkart_fashion_products_dataset.json'
with open(json_file_path, 'r') as json_file:
    json_data = json.load(json_file)

# Create a Streamlit app
st.title("Outfit Generator")



# Get the user's prompt
prompt_input = st.text_input("Provide a prompt for outfit suggestion")

# Define categories
categories = ["Topwear", "Bottomwear", "Footwear"]

# Process uploaded JSON file



if prompt:
    st.write("Chatbot's Response:")
    st.write(f"Today, I'm going to show you some outfits that you can wear to your college farewell party.")
    
    # Display best-matched products from each category based on the prompt
    for category in categories:
        best_match = find_best_matched_product(json_data[category], prompt)
        
        st.write(f"\nBest Matched {category.capitalize()}:")
        if best_match:
            st.image(best_match["images"][0], caption=best_match["title"])
            st.write("Product Details:")
            st.write("Title:", best_match["title"])
            st.write("Brand:", best_match["brand"])
            st.write("Price:", best_match["actual_price"])
            st.write("Description:", best_match["description"])
            st.write("Product Details:", best_match["product_details"])
            # You can add more relevant product details here
        else:
            st.write(f"No matching {category} found for the prompt.")

    st.write("\nMade with Streamlit")