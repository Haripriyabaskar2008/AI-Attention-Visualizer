import streamlit as st
from PIL import Image
import pytesseract
from pytesseract import Output


# Tesseract installation path
pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)


# Page configuration
st.set_page_config(
    page_title="AI Image Text Extractor",
    page_icon="📝",
    layout="centered"
)


# Title
st.title("📝 AI Image Text Extractor")

st.write(
    "Upload an image and convert the text inside it into editable text "
    "using OCR."
)


# Image upload
uploaded_file = st.file_uploader(
    "Upload an image",
    type=["png", "jpg", "jpeg"]
)


if uploaded_file is not None:

    # Display image
    image = Image.open(uploaded_file)

    st.subheader("Uploaded Image")

    st.image(
        image,
        caption="Uploaded Image",
        use_container_width=True
    )


    # Extract button
    if st.button(
        "Extract Text",
        type="primary",
        use_container_width=True
    ):

        with st.spinner("Extracting text from image..."):

            try:

                # OCR text extraction
                extracted_text = pytesseract.image_to_string(
                    image
                )


                # OCR confidence data
                data = pytesseract.image_to_data(
                    image,
                    output_type=Output.DICT
                )


                confidence_values = []

                for confidence in data["conf"]:

                    try:
                        value = float(confidence)

                        if value >= 0:
                            confidence_values.append(value)

                    except ValueError:
                        pass


                # Calculate average OCR confidence
                if confidence_values:

                    score = (
                        sum(confidence_values)
                        / len(confidence_values)
                    )

                else:
                    score = 0


                # Display extracted text
                st.subheader("Extracted Text")

                if extracted_text.strip():

                    st.text_area(
                        "OCR Result",
                        extracted_text,
                        height=300
                    )

                else:

                    st.warning(
                        "No readable text was detected in the image."
                    )


                # Display score
                st.subheader("OCR Confidence Score")

                st.metric(
                    "Recognition Score",
                    f"{score:.2f}%"
                )


                # Score explanation
                if score >= 85:

                    st.success(
                        "High confidence: the text was recognized clearly."
                    )

                elif score >= 60:

                    st.info(
                        "Moderate confidence: some text may need checking."
                    )

                else:

                    st.warning(
                        "Low confidence: try a clearer or higher-quality image."
                    )


            except Exception as e:

                st.error(
                    f"Unable to extract text: {e}"
                )