


import streamlit as st
import random
import json

topwear_data = json.load(open("sub_catagories/Topwear.json"))
bottomwear_data = json.load(open("sub_catagories/Bottomwear.json"))
footwear_data = json.load(open("sub_catagories/Footwear.json"))

def get_random_product(data_set):
    return random.choice(data_set)

def display_product(product):
    image_style = "object-fit: contain; background-color: white; width: 100%; height: 200px; display: flex; justify-content: center; align-items: center;"
    st.write(f'<div style="{image_style}"><img src="{product["images"][0]}" /></div>', unsafe_allow_html=True)
    st.write(f"**Title:** {product['title']}")
    st.write(f"**Actual Price:** {product['actual_price']}")
    st.write(f"**Brand:** {product['brand']}")
    st.write(f"**Discount:** {product['discount']}")
    st.write(f"**Seller:** {product['seller']}")
    st.write(f"**Product URL:** [Link]({product['url']})")

st.title("![Flipkart Logo](https://www.freepnglogos.com/uploads/flipkart-logo-png/flipkart-logo-icon-flat-style-png-4.png)")
st.title("Outfit Generator")

st.header("TRENDING OUTFIT")
col1, col2, col3 = st.columns(3)
topwear_product = get_random_product(topwear_data)
col1.subheader("Topwear")
with col1: display_product(topwear_product)

bottomwear_product = get_random_product(bottomwear_data)
col2.subheader("Bottomwear")
with col2: display_product(bottomwear_product)

footwear_product = get_random_product(footwear_data)
col3.subheader("Footwear")
with col3: display_product(footwear_product)

st.header("TRENDING OUTFIT")
col4, col5, col6 = st.columns(3)
topwear_product2 = get_random_product(topwear_data)
col4.subheader("Topwear")
with col4: display_product(topwear_product2)

bottomwear_product2 = get_random_product(bottomwear_data)
col5.subheader("Bottomwear")
with col5: display_product(bottomwear_product2)

footwear_product2 = get_random_product(footwear_data)
col6.subheader("Footwear")
with col6: display_product(footwear_product2)

button_container = st.container()
with button_container: st.button("Generate New Outfit", key="generate_button")

prompt = st.text_input("Enter a prompt:")

if st.session_state.generate_button:
    col1.empty()
    col2.empty()
    col3.empty()
    col4.empty()
    col5.empty()
    col6.empty()