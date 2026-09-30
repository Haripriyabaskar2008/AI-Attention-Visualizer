import streamlit as st
from PIL import Image
import pytesseract
from pytesseract import Output
import shutil


# --------------------------------------------------
# TESSERACT CONFIGURATION
# --------------------------------------------------

tesseract_path = shutil.which("tesseract")

if tesseract_path:
    pytesseract.pytesseract.tesseract_cmd = tesseract_path
else:
    # Local Windows fallback
    windows_path = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

    if __import__("os").path.exists(windows_path):
        pytesseract.pytesseract.tesseract_cmd = windows_path


# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="AI OCR Word Analyzer",
    page_icon="🔍",
    layout="wide"
)


# --------------------------------------------------
# TITLE
# --------------------------------------------------

st.title("🔍 AI OCR Word Analyzer")

st.write(
    "Upload an image to extract text and analyze "
    "word-wise OCR recognition confidence."
)


# --------------------------------------------------
# IMAGE UPLOAD
# --------------------------------------------------

uploaded_file = st.file_uploader(
    "Upload an image",
    type=["png", "jpg", "jpeg"]
)


# --------------------------------------------------
# PROCESS IMAGE
# --------------------------------------------------

if uploaded_file is not None:

    image = Image.open(uploaded_file)

    st.subheader("📷 Uploaded Image")

    st.image(
        image,
        caption="Uploaded Image",
        use_container_width=True
    )


    if st.button(
        "🚀 Analyze Image",
        type="primary",
        use_container_width=True
    ):

        with st.spinner("Analyzing image..."):

            try:

                # --------------------------------------------------
                # OCR DATA
                # --------------------------------------------------

                data = pytesseract.image_to_data(
                    image,
                    output_type=Output.DICT
                )


                detected_words = []
                confidence_values = []


                # --------------------------------------------------
                # EXTRACT WORDS + CONFIDENCE
                # --------------------------------------------------

                for word, confidence in zip(
                    data["text"],
                    data["conf"]
                ):

                    word = word.strip()

                    try:
                        confidence = float(confidence)
                    except ValueError:
                        continue


                    # Ignore empty values and invalid confidence
                    if word and confidence >= 0:

                        detected_words.append(
                            {
                                "Word": word,
                                "Confidence": confidence
                            }
                        )

                        confidence_values.append(
                            confidence
                        )


                # --------------------------------------------------
                # NO TEXT FOUND
                # --------------------------------------------------

                if not detected_words:

                    st.warning(
                        "No readable text was detected in this image."
                    )

                    st.info(
                        "Try uploading a clearer image containing text."
                    )

                    st.stop()


                # --------------------------------------------------
                # EXTRACTED TEXT
                # --------------------------------------------------

                extracted_text = " ".join(
                    item["Word"]
                    for item in detected_words
                )


                st.subheader("📝 Extracted Text")

                st.text_area(
                    "Detected Text",
                    extracted_text,
                    height=180
                )


                # --------------------------------------------------
                # WORD STATISTICS
                # --------------------------------------------------

                total_words = len(detected_words)

                average_confidence = (
                    sum(confidence_values)
                    / len(confidence_values)
                )


                # Count high-confidence words
                high_confidence_words = sum(
                    1
                    for confidence in confidence_values
                    if confidence >= 70
                )


                word_recognition_score = (
                    high_confidence_words
                    / total_words
                ) * 100


                # --------------------------------------------------
                # SUMMARY
                # --------------------------------------------------

                st.subheader("📊 Word Analysis")


                col1, col2, col3 = st.columns(3)


                with col1:

                    st.metric(
                        "Total Words",
                        total_words
                    )


                with col2:

                    st.metric(
                        "Recognized Words",
                        high_confidence_words
                    )


                with col3:

                    st.metric(
                        "Word Recognition Score",
                        f"{word_recognition_score:.2f}%"
                    )


                # --------------------------------------------------
                # WORD-WISE CONFIDENCE
                # --------------------------------------------------

                st.subheader(
                    "🔤 Word-wise Recognition Confidence"
                )


                for item in detected_words:

                    word = item["Word"]

                    confidence = item["Confidence"]


                    if confidence >= 85:

                        status = "🟢 High"

                    elif confidence >= 60:

                        status = "🟡 Medium"

                    else:

                        status = "🔴 Low"


                    col1, col2, col3 = st.columns(
                        [3, 2, 2]
                    )


                    with col1:

                        st.write(
                            f"**{word}**"
                        )


                    with col2:

                        st.progress(
                            min(
                                int(confidence),
                                100
                            )
                        )


                    with col3:

                        st.write(
                            f"{confidence:.1f}% — {status}"
                        )


                # --------------------------------------------------
                # SCORE EXPLANATION
                # --------------------------------------------------

                st.subheader("📌 Score Explanation")


                st.write(
                    "The Word Recognition Score represents the "
                    "percentage of detected words with an OCR "
                    "confidence of 70% or higher."
                )


                if word_recognition_score >= 85:

                    st.success(
                        "High word recognition: most detected "
                        "words were recognized confidently."
                    )

                elif word_recognition_score >= 60:

                    st.info(
                        "Moderate word recognition: some words "
                        "may require verification."
                    )

                else:

                    st.warning(
                        "Low word recognition: try a clearer "
                        "or higher-resolution image."
                    )


            except Exception as e:

                st.error(
                    f"Unable to extract text: {e}"
                )
