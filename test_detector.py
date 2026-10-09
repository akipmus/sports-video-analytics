from detector import detect_objects

result = detect_objects(
    video_path="uploads/match.mp4",
    output_path="outputs/match_annotated.mp4",
)

print("Detection completed!")
print("Frames processed:", result["frames_processed"])
print("Object detections:", result["detected_objects"])
print("Saved video:", result["output_path"])
