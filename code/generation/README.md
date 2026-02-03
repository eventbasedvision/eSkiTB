# Event generation helpers

Use this folder for configs and scripts to convert RGB streams to events (e.g., v2e or rosbag pipelines).

Suggested contents:
- `v2e_config.yaml`: conversion parameters that match the paper.
- `convert_rgb_to_events.py`: wrapper that applies the config to a folder of videos.
- Notes on frame rate, resolution, and polarity accumulation used in the benchmark.
