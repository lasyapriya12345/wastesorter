import streamlit as st
from PIL import Image

# Title
st.title("♻️ Waste Sorter Project")

# --- Classify by Text ---
st.subheader("Classify by Text")
user_input = st.text_input("Enter an item:")

if user_input:
    if user_input.lower() in ["plastic bottle", "glass", "paper", "tin"]:
        st.success("Recyclable ✅")
        st.write("Tip: Clean before recycling.")
    elif user_input.lower() in ["apple", "banana peel", "leaves"]:
        st.success("Compostable 🌱")
        st.write("Tip: Add to compost bin.")
    else:
        st.error("Trash 🚮")
        st.write("Tip: Dispose responsibly.")

# --- Classify by Image ---
st.subheader("Classify by Image")
uploaded_file = st.file_uploader("Upload an image of waste", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Waste Image", use_column_width=True)
    st.info("⚠️ (Demo) Image classification not yet implemented.")

# --- Button to show code ---
if st.button("📜 Click here to view the code"):
    st.code
import streamlit as st
from PIL import Image

st.title("♻️ Waste Sorter Project")

# Classify by Text
st.subheader("Classify by Text")
user_input = st.text_input("Enter an item:")

if user_input:
    if user_input.lower() in ["plastic bottle", "glass", "paper", "tin"]:
        st.success("Recyclable ✅")
        st.write("Tip: Clean before recycling.")
    elif user_input.lower() in ["apple", "banana peel", "leaves"]:
        st.success("Compostable 🌱")
        st.write("Tip: Add to compost bin.")
    else:
        st.error("Trash 🚮")
        st.write("Tip: Dispose responsibly.")

# --- Classify by Image ---
st.subheader("Classify by Image")
uploaded_file = st.file_uploader("Upload an image of waste", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Waste Image", use_column_width=True)

    # Use filename keywords for simple classification
    filename = uploaded_file.name.lower()

    if "bottle" in filename or "glass" in filename or "paper" in filename or "tin" in filename:
        st.success("Recyclable ✅")
        st.write("Tip: Clean before recycling.")
    elif "banana" in filename or "apple" in filename or "peel" in filename or "leaves" in filename:
        st.success("Compostable 🌱")
        st.write("Tip: Add to compost bin.")
    else:
        st.error("Trash 🚮")
        st.write("Tip: Dispose responsibly.")