from pathlib import Path

print(Path.cwd())
fp_cwd = Path.cwd()/"just_a_marker.py"
print(fp_cwd.exists())