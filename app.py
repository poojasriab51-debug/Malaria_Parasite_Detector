
import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

# ---------------- PAGE CONFIGURATION ----------------

st.set_page_config(
    page_title="Malaria Parasite Detection",
    page_icon="🔬",
    layout="wide"
)

# ---------------- LOAD TRAINED CNN ----------------

@st.cache_resource
def load_model():
    return tf.keras.models.load_model("malaria_cnn_best.keras")

model = load_model()

# ---------------- HEADER ----------------

st.title("🔬 Malaria Parasite Detection")
st.subheader("Deep Learning-Based Blood Cell Classification")

st.write(
    "This application uses a custom Convolutional Neural Network "
    "(CNN) to classify blood smear cell images into two categories."
)

st.info(
    "Educational and research project only. "
    "This tool is not intended for medical diagnosis."
)

# ---------------- IMAGE UPLOAD ----------------

st.markdown("### Upload Blood Cell Image")

uploaded_file = st.file_uploader(
    "Choose a blood smear image",
    type=["jpg", "jpeg", "png"]
)

# ---------------- IMAGE PREPROCESSING ----------------

def preprocess_image(image):
    image = image.convert("RGB")
    image = image.resize((128, 128))

    image_array = np.array(image, dtype=np.float32)
    image_array = image_array / 255.0

    image_array = np.expand_dims(image_array, axis=0)

    return image_array

# ---------------- PREDICTION ----------------

if uploaded_file is not None:

    image = Image.open(uploaded_file).convert("RGB")

    col1, col2 = st.columns(2)

    with col1:
        st.image(
            image,
            caption="Uploaded Blood Smear Image",
            use_container_width=True
        )

    with col2:
        st.markdown("### Image Information")
        st.write("Image dimensions:", image.size)
        st.write("Image format:", image.format or "Converted to RGB")

    if st.button("Analyze Image", type="primary"):

        processed_image = preprocess_image(image)

        with st.spinner("Analyzing blood cell image..."):

            prediction = float(
                model.predict(processed_image, verbose=0)[0][0]
            )

        st.markdown("---")
        st.markdown("## Prediction Result")

        if prediction >= 0.5:

            confidence = prediction * 100

            st.error("🦠 Parasitized")
            st.metric("Model score for Parasitized", f"{confidence:.2f}%")

        else:

            confidence = (1 - prediction) * 100

            st.success("✅ Uninfected")
            st.metric("Model score for Uninfected", f"{confidence:.2f}%")

        st.caption(
            "Scores represent the model's output, not a clinically "
            "validated probability of infection."
        )

