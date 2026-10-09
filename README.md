# Sports Video Analytics

A small Streamlit application that runs YOLO object detection on a sports video and displays an annotated MP4.

## Requirements

- Python 3.10 or newer
- The dependencies in `requirements.txt`

## Setup

From the project directory, create and activate a virtual environment, then install the dependencies:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

## Run the web app

```powershell
streamlit run app.py
```

Open the local URL printed by Streamlit. Upload an MP4, MOV, AVI, or MKV video, or put a sample video at `uploads/match.mp4` and select the included sample. Click **Run detection** to analyze the video. The first run downloads the YOLOv8n model weights automatically. The app shows the annotated video and detection counts, and lets you download the result.

The annotated output is also saved in `outputs/`.

## Run the detector from the command line

Place a video at `uploads/match.mp4`, then run:

```powershell
python test_detector.py
```

This writes `outputs/match_annotated.mp4` and prints the number of processed frames and detections. `detected_objects` counts each detected object in each frame, so an object visible across multiple frames is counted multiple times.

## GitHub and video files

Uploaded videos, generated outputs, the virtual environment, and downloaded model weights are local files and should not be committed. Add your own sample video to `uploads/match.mp4` after cloning the repository.
