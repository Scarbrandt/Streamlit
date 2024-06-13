import streamlit as st
import requests
from PIL import Image
import io

st.title("OCR with FastAPI and Streamlit")
st.write("Upload an image to get the text")

uploaded_file = st.file_uploader("Choose an image...", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    st.write("")
    st.write("Predict...")

    # Convert image to bytes
    img_bytes = io.BytesIO()
    image.save(img_bytes, format='PNG')
    img_bytes = img_bytes.getvalue()

    # Send image to FastAPI server
    response = requests.post("http://127.0.0.1:8000/predict/", files={"file": img_bytes})

    if response.status_code == 200:
        result = response.json()
        st.write("Prediction:", result["result"])
    else:
        st.write("Error:", response.status_code)