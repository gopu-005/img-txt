import streamlit as st
from PIL import Image
import pytesseract
import os
pytesseract.pytesseract.tesseract_cmd = 'C:/OCR/Tesseract-OCR/tesseract.exe'

# Configure Tesseract path if necessary
# For Windows users: Uncomment the line below and set the Tesseract path
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Streamlit app title
st.title("Text Extractor from Image")

# Description
st.write("""
Upload an image, and this tool will extract the text from the image and allow you to save it to a notepad file.
""")

# File uploader for images
uploaded_file = st.file_uploader("Upload an Image", type=["png", "jpg", "jpeg"])

if uploaded_file:
    # Load the image
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_container_width=True)

    # Extract text from image using pytesseract
    with st.spinner("Extracting text..."):
        extracted_text = pytesseract.image_to_string(image)

    # Display the extracted text
    st.success("Text extraction complete!")
    st.subheader("Extracted Text:")
    st.text_area("Text", extracted_text, height=200)

    # Save extracted text to a notepad file
    if st.button("Save to Notepad"):
        file_path = "extracted_text.txt"
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(extracted_text)
        st.success(f"Text saved to {file_path}")

        # Option to download the file
        with open(file_path, "rb") as file:
            st.download_button(
                label="Download Notepad File",
                data=file,
                file_name="extracted_text.txt",
                mime="text/plain",
            )