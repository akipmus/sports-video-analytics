# Sports Video Analyzer

A Python-based computer vision application that analyzes sports videos using YOLO and OpenCV. The application provides a Streamlit web interface for uploading match clips, detecting objects, viewing annotated video output, and exploring detection statistics.

## Features

- Upload sports videos through a web interface.
- Detect objects in video frames using a pretrained YOLO model.
- Generate annotated videos with bounding boxes and class labels.
- Display detection statistics and object counts.
- Preview and download the processed video.

## Tech Stack

- **Python** — application logic
- **Ultralytics YOLO** — object detection
- **OpenCV** — video processing
- **Streamlit** — web interface

## Project Structure

```text
sports-video-analytics/
├── app.py
├── detector.py
├── test_detector.py
├── requirements.txt
├── README.md
├── .gitignore
├── uploads/
└── outputs/
```

Generated videos, local virtual environments, and downloaded model weights should not be committed unless intentionally required.

## Requirements

- Python 3.10 or a compatible version supported by the installed dependencies
- Internet connection for initial dependency and model downloads
- A supported video file, such as MP4

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/akipmus/sports-video-analytics.git
cd sports-video-analytics
```

### 2. Create a virtual environment

Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

If necessary, install the main dependencies directly:

```powershell
pip install streamlit ultralytics opencv-python
```

### 4. Run the application

```powershell
python -m streamlit run app.py
```

Open the local URL displayed in the terminal, usually `http://localhost:8501`.

## Usage

1. Launch the Streamlit application.
2. Upload a sports video.
3. Select the object detection action.
4. Review the annotated video and detection statistics.
5. Download the processed video if the download option is available.

## Testing

Run the detector test script:

```powershell
python test_detector.py
```

Use a short sample video first to verify that the detection pipeline and output generation work correctly.

## Current Limitations

- Detection performance depends on video length, resolution, hardware, and model configuration.
- Object detections counted across frames do not represent unique players.
- A pretrained general-purpose model may miss small or distant objects, including a football.
- Detection results are not equivalent to verified match events such as goals or assists.

## Future Improvements

- Player tracking and unique-player counting
- Football-specific detection and evaluation
- Team identification
- Processing-time and performance benchmarks
- Improved visualization of match statistics

## Author

Developed as a computer vision portfolio project exploring object detection and sports video analysis.
