"""
Placeholder evaluation script for eSkiTB tracking metrics.
Fill in model loading, dataloaders, and metrics to mirror the paper.
"""

import argparse
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Evaluate trackers on eSkiTB")
    parser.add_argument("--split", required=True, help="Path to split file (txt)")
    parser.add_argument("--annotations", required=True, help="Path to annotation JSON")
    parser.add_argument("--data-root", required=True, help="Root directory containing event data")
    parser.add_argument("--output", default="outputs/metrics.json", help="Where to save metrics")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    split_path = Path(args.split)
    ann_path = Path(args.annotations)
    data_root = Path(args.data_root)

    # TODO: implement loader, tracker inference, and metric computation (e.g., MOTA, HOTA).
    # This stub only checks for file presence to help users debug paths quickly.
    missing = [p for p in (split_path, ann_path, data_root) if not p.exists()]
    if missing:
        raise FileNotFoundError(f"Missing required paths: {[str(p) for p in missing]}")

    print("Paths look good. Plug in your evaluation logic here.")


if __name__ == "__main__":
    main()
