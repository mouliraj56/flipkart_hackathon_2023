import gradio as gr
import random
import json

topwear_data = json.load(open("sub_catagories/Topwear.json"))
bottomwear_data = json.load(open("sub_catagories/Bottomwear.json"))
footwear_data = json.load(open("sub_catagories/Footwear.json"))

def get_random_product(data_set):
    return random.choice(data_set)

def generate_outfit():
    outfit = ""

    for category in ["Topwear", "Bottomwear", "Footwear"]:
        product = get_random_product(topwear_data) if category == "Topwear" else \
                  get_random_product(bottomwear_data) if category == "Bottomwear" else \
                  get_random_product(footwear_data)
        outfit += f"## {category}\n{display_product(product)}\n"

    return outfit

def display_product(product):
    image_style = "object-fit: contain; background-color: white; width: 100%; height: 200px; display: flex; justify-content: center; align-items: center;"
    return f'<div style="{image_style}"><img src="{product["images"][0]}" /></div>' \
           f"**Title:** {product['title']}\n" \
           f"**Actual Price:** {product['actual_price']}\n" \
           f"**Brand:** {product['brand']}\n" \
           f"**Discount:** {product['discount']}\n" \
           f"**Seller:** {product['seller']}\n" \
           f"**Product URL:** [Link]({product['url']})\n"

iface = gr.Interface(generate_outfit, live=True)
iface.launch()
