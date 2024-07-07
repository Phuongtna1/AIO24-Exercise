from yolov10.ultralytics import YOLOv10
import streamlit as st
from PIL import Image

TRAINED_MODEL_PATH = 'yolov10/runs/detect/train/weights/best.pt'
model = YOLOv10(TRAINED_MODEL_PATH)


def main():
    st.title('Safety Helmet Checking')
    file = st.file_uploader('Upload Image ', type=['jpg', 'png', 'jpeg'])
    if file is not None:
        st.image(file, caption="Uploaded Image")
        image = Image.open(file)
        processed_image = model.predict(source=image, conf=0.3)[0].plot()
        processed_image = processed_image[..., ::-1]
        st.image(processed_image)


if __name__ == "__main__":
    main()
