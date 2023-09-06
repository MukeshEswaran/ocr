import streamlit as st
import pytesseract
from io import BytesIO
from PIL import Image

# Define the path to the Tesseract executable (update this path accordingly)
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'

# Function to perform OCR using Tesseract
def perform_ocr(image_bytes, lang='eng+hin+tam'):
    text = pytesseract.image_to_string(Image.open(image_bytes), lang=lang)
    return text

# Streamlit UI for Document OCR
def document_ocr(document_type):
    st.title(f"{document_type} OCR")
    st.write(f"Upload an image of the {document_type} for OCR.")

    uploaded_image = st.file_uploader(f"Choose an image for {document_type} OCR...", type=["jpg", "png", "jpeg"])

    if uploaded_image is not None:
        st.image(uploaded_image, caption="Uploaded Image.", use_column_width=True)
        st.write("")
        st.write("Analyzing...")

        text = perform_ocr(uploaded_image)
        
        st.write("### Extracted Text:")
        
        # Display extracted details in a clean UI
        st.text_area("click inside the box to edit", value=text.replace('\n', '\n\n'), height=None, key="extracted_text_area", help="Recognized text will be displayed here.")

# Main Streamlit UI
def main():
    st.title("OCR")

    document_type = st.selectbox("Select Document Type", ["Aadhar Card", "PAN Card", "Driver's License"])

    if document_type == "Aadhar Card":
        document_ocr("Aadhar Card")
    elif document_type == "PAN Card":
        document_ocr("PAN Card")
    elif document_type == "Driver's License":
        document_ocr("Driver's License")

if __name__ == "__main__":
    main()
