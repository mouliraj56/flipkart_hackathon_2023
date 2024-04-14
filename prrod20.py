import json
import random
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def main():
    # Read data from each file
    topwear_data = read_json_file('sub_catagories\Topwear.json')
    bottomwear_data = read_json_file('sub_catagories\Bottomwear.json')
    footwear_data = read_json_file('sub_catagories\Footwear.json')
    
    # Extract the list of products from each data
    topwear_products = topwear_data
    bottomwear_products = bottomwear_data
    footwear_products = footwear_data
    
    # Select 20 random products from each category
    selected_topwear = random.sample(topwear_products, min(20, len(topwear_products)))
    selected_bottomwear = random.sample(bottomwear_products, min(20, len(bottomwear_products)))
    selected_footwear = random.sample(footwear_products, min(20, len(footwear_products)))
    
    # Combine products
    combined_products = {
        'topwear': selected_topwear,
        'bottomwear': selected_bottomwear,
        'footwear': selected_footwear
    }
    
    # Generate PDF file
    generate_pdf('combined_products.pdf', combined_products)

def read_json_file(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    return data

def generate_pdf(filename, data):
    c = canvas.Canvas(filename, pagesize=letter)
    c.drawString(100, 750, "Combined Products Data")
    c.drawString(100, 730, "Generated using Python and ReportLab")
    c.drawString(100, 710, "=" * 40)
    
    y_position = 690
    for category, products in data.items():
        c.drawString(100, y_position, f"Category: {category}")
        y_position -= 15
        for product in products:
            c.drawString(120, y_position, f"Title: {product['title']}")
            c.drawString(120, y_position - 10, f"Brand: {product['brand']}")
            c.drawString(120, y_position - 20, f"Price: {product['actual_price']}")
            y_position -= 40
        y_position -= 20
    
    c.save()

if __name__ == "__main__":
    main()
