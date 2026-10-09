"""Run YOLO object detection on a video and save an annotated copy."""

from pathlib import Path
from typing import Any

import cv2
from ultralytics import YOLO


def detect_objects(
    video_path: str | Path,
    output_path: str | Path,
    model_path: str = "yolov8n.pt",
) -> dict[str, Any]:
    """Detect objects in every frame and write an annotated MP4.

    ``detected_objects`` is the total number of object detections across all
    processed frames (an object present in several frames is counted several
    times).
    """
    video_path = Path(video_path)
    output_path = Path(output_path)
    if not video_path.is_file():
        raise FileNotFoundError(f"Input video not found: {video_path}")

    output_path.parent.mkdir(parents=True, exist_ok=True)
    capture = cv2.VideoCapture(str(video_path))
    if not capture.isOpened():
        raise ValueError(f"Could not open input video: {video_path}")

    fps = capture.get(cv2.CAP_PROP_FPS)
    width = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
    if fps <= 0 or width <= 0 or height <= 0:
        capture.release()
        raise ValueError(f"Input video has invalid dimensions or frame rate: {video_path}")

    writer = cv2.VideoWriter(
        str(output_path), cv2.VideoWriter_fourcc(*"mp4v"), fps, (width, height)
    )
    if not writer.isOpened():
        capture.release()
        raise OSError(f"Could not create output video: {output_path}")

    model = YOLO(model_path)
    frames_processed = 0
    detected_objects = 0
    try:
        while True:
            ok, frame = capture.read()
            if not ok:
                break
            result = model.predict(frame, verbose=False)[0]
            detected_objects += len(result.boxes)
            writer.write(result.plot())
            frames_processed += 1
    finally:
        capture.release()
        writer.release()

    if frames_processed == 0:
        raise ValueError(f"Input video contains no readable frames: {video_path}")

    return {
        "frames_processed": frames_processed,
        "detected_objects": detected_objects,
        "output_path": str(output_path),
    }
