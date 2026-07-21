from pathlib import Path

float(Path("/app/outputs/score.txt").read_text().strip())
