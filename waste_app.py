import streamlit as st
from PIL import Image

st.title("♻️ Waste Sorter Project")

# --- Text classification ---
st.subheader("Classify by Typing")
waste_item = st.text_input("Type a waste item (e.g., banana peel, plastic bottle):")

if waste_item:
    item = waste_item.lower()
    if any(x in item for x in ["bottle", "glass", "paper", "tin"]):
        st.success("✅ Recyclable ♻️")
        st.write("💡 Tip: Clean before recycling.")
    elif any(x in item for x in ["banana", "apple", "peel", "leaves"]):
        st.success("✅ Compostable 🌱")
        st.write("💡 Tip: Add to compost bin.")
    else:
        st.error("❌ Trash 🗑️")
        st.write("💡 Tip: Dispose responsibly.")

# --- Image classification ---
st.subheader("Classify by Image")
uploaded_file = st.file_uploader("Upload an image of waste", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Waste Image", use_column_width=True)

    filename = uploaded_file.name.lower()
    if any(x in filename for x in ["bottle", "glass", "paper", "tin"]):
        st.success("✅ Recyclable ♻️")
        st.write("💡 Tip: Clean before recycling.")
    elif any(x in filename for x in ["banana", "apple", "peel", "leaves"]):
        st.success("✅ Compostable 🌱")
        st.write("💡 Tip: Add to compost bin.")
    else:
        st.error("❌ Trash 🗑️")
        st.write("💡 Tip: Dispose responsibly.")