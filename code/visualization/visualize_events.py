"""
Minimal placeholder to visualize event frames and bounding boxes.
Replace with your actual visualization pipeline.
"""

import argparse
from pathlib import Path

import json
import cv2
import numpy as np


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Visualize eSkiTB sample")
    parser.add_argument("--events", required=True, help="Path to an event frame (image or npy)")
    parser.add_argument("--annotation", required=True, help="Path to annotation JSON for the frame")
    parser.add_argument("--out", default="vis.png", help="Output image path")
    return parser.parse_args()


def load_frame(path: Path) -> np.ndarray:
    if path.suffix.lower() in {".png", ".jpg", ".jpeg"}:
        frame = cv2.imread(str(path), cv2.IMREAD_GRAYSCALE)
    elif path.suffix.lower() == ".npy":
        frame = np.load(str(path))
    else:
        raise ValueError(f"Unsupported frame type: {path.suffix}")
    if frame is None:
        raise ValueError(f"Could not load frame at {path}")
    return frame


def draw_boxes(frame: np.ndarray, ann: dict) -> np.ndarray:
    vis = cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR) if frame.ndim == 2 else frame.copy()
    for obj in ann.get("objects", []):
        x, y, w, h = obj["bbox"]
        p1 = (int(x), int(y))
        p2 = (int(x + w), int(y + h))
        cv2.rectangle(vis, p1, p2, (0, 180, 255), 2)
        cv2.putText(vis, f"id {obj['track_id']}", (p1[0], p1[1] - 4), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 180, 255), 1)
    return vis


def main() -> None:
    args = parse_args()
    frame = load_frame(Path(args.events))
    with open(args.annotation, "r", encoding="utf-8") as f:
        ann = json.load(f)
    vis = draw_boxes(frame, ann["frames"][0] if "frames" in ann else ann)
    cv2.imwrite(args.out, vis)
    print(f"Saved visualization to {args.out}")


if __name__ == "__main__":
    main()
