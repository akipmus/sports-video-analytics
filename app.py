from pathlib import Path

import streamlit as st

from detector import detect_objects


ROOT = Path(__file__).resolve().parent
UPLOADS = ROOT / "uploads"
OUTPUTS = ROOT / "outputs"
SAMPLE_VIDEO = UPLOADS / "match.mp4"

st.set_page_config(page_title="Sports Video Analyzer", layout="wide")

st.title("Sports Video Analyzer")
st.write("Upload a match clip or use the included sample to detect and annotate objects.")

uploaded_file = st.file_uploader("Choose a video", type=["mp4", "mov", "avi", "mkv"])
use_sample = False
if uploaded_file is None and SAMPLE_VIDEO.is_file():
    use_sample = st.checkbox("Use the included soccer sample", value=True)

input_path = None
if uploaded_file is not None:
    UPLOADS.mkdir(parents=True, exist_ok=True)
    input_path = UPLOADS / Path(uploaded_file.name).name
    input_path.write_bytes(uploaded_file.getvalue())
elif use_sample:
    input_path = SAMPLE_VIDEO

if input_path is not None:
    st.caption(f"Selected video: {input_path.name}")
    with st.expander("Preview input video"):
        st.video(str(input_path))

if st.button("Run detection", type="primary", disabled=input_path is None):
    output_path = OUTPUTS / f"{input_path.stem}_annotated.mp4"
    with st.spinner("Analyzing video frames. This can take a little while."):
        try:
            result = detect_objects(input_path, output_path)
        except Exception as error:
            st.error(f"Detection failed: {error}")
        else:
            st.session_state["detection_result"] = result
            st.session_state["detection_output"] = str(output_path)

result = st.session_state.get("detection_result")
output_path = Path(st.session_state["detection_output"]) if st.session_state.get("detection_output") else None
if result and output_path and output_path.is_file():
    st.subheader("Detection result")
    metric1, metric2 = st.columns(2)
    metric1.metric("Frames processed", result["frames_processed"])
    metric2.metric("Object detections", result["detected_objects"])
    st.video(str(output_path))
    st.download_button(
        "Download annotated video",
        data=output_path.read_bytes(),
        file_name=output_path.name,
        mime="video/mp4",
    )
