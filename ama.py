import streamlit as st
import json

st.set_page_config(page_title="Amazon Demo", layout="wide")

# Load products
with open("products.json", "r") as f:
    products = json.load(f)

st.title("🛒 Amazon-Style Demo Store")

# Search bar
search_query = st.text_input("Search products...")

# Filter results
filtered_products = [
    p for p in products
    if search_query.lower() in p["name"].lower()
]

# Display products
cols = st.columns(3)

for idx, product in enumerate(filtered_products):
    with cols[idx % 3]:
        st.image(product["image"], width=200)
        st.subheader(product["name"])
        st.write(f"💲 Price: **${product['price']}**")
        st.write(f"⭐ Rating: **{product['rating']}**/5")
        if st.button(f"Add to Cart", key=product["name"]):
            st.success(f"Added {product['name']} to cart!")
