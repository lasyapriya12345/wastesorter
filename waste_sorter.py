import streamlit as st
from PIL import Image

st.title("♻️ Waste Sorter Project")

# Classification function (simple rules)
def classify_item(text):
    text = text.lower()
    if "banana" in text or "apple" in text or "food" in text or "peel" in text:
        return "Compostable 🌱", "Put it in the compost bin."
    elif "bottle" in text or "plastic" in text or "can" in text or "paper" in text:
        return "Recyclable ♻️", "Place it in the recycling bin."
    else:
        return "Trash 🚮", "Dispose safely in the trash."

# --- Option 1: Text input ---
st.subheader("Type the waste item")
user_input = st.text_input("Example: banana peel, plastic bottle, paper cup")

if user_input:
    label, tip = classify_item(user_input)
    st.success(f"Prediction: *{label}*")
    st.info(f"Tip: {tip}")

# --- Option 2: Image upload ---
st.subheader("Or upload a waste image")
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # classify based on filename (simple demo version)
    label, tip = classify_item(uploaded_file.name)
    st.success(f"Prediction: *{label}*")
    st.info(f"Tip: {tip}")