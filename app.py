import streamlit as st
from products import products

# Page Config
st.set_page_config(page_title="Arya - Omnichannel AI", layout="centered")

# Title Section
st.title("ARYA – Your Omnichannel AI Stylist 👗")
st.subheader("Discover Sustainable and Festive Fashion Choices")

st.markdown("""
Welcome to **ARYA**, your personal AI stylist.  
Explore eco-friendly and festive fashion curated just for you 🌿
""")

# Session State
if "cart" not in st.session_state:
    st.session_state.cart = []

if "channel" not in st.session_state:
    st.session_state.channel = "Mobile"

st.success(f"🟢 Channel: {st.session_state.channel}")

# Product Section
st.subheader("🛍️ Recommended Products")

for p in products:
    st.markdown(f"### {p['name']}")
    st.write(f"💰 Price: ₹{p['price']} | 🏷️ Tag: {p['tag']}")

    if p["stock"] == 0:
        st.error("Out of Stock 😕")
    else:
        if st.button("Add to Cart", key=p["id"]):
            if p not in st.session_state.cart:
                st.session_state.cart.append(p)
                st.success("Added to cart!")
            else:
                st.info("Item already in cart")

st.divider()

# Cart Section
st.subheader("🛒 Your Cart")

total = 0
if st.session_state.cart:
    for item in st.session_state.cart:
        st.write(f"{item['name']} – ₹{item['price']}")
        total += item["price"]

    st.markdown(f"### **Total: ₹{total}**")
else:
    st.info("Your cart is empty")

# Channel Switch
if st.button("Continue on Kiosk 🏬"):
    st.session_state.channel = "Kiosk"
    st.success("Welcome back! Your cart is ready.")
