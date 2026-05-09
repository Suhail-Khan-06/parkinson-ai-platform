import os
import shutil

SOURCE_DIR = "data/raw/datscan_dcm"
TARGET_DIR = "data/raw/datscan_dcm/all_dcm"

os.makedirs(TARGET_DIR, exist_ok=True)

for root, _, files in os.walk(SOURCE_DIR):
    for file in files:
        if file.endswith(".dcm"):
            src = os.path.join(root, file)
            dst = os.path.join(TARGET_DIR, file)

            shutil.copy(src, dst)

print("✅ Done: all DCM files collected")