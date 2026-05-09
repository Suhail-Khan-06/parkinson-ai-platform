import os
import shutil
import pandas as pd
import re

PNG_DIR = "data/raw/datscan_png"
METADATA_FILE = "data/raw/datscan_metadata.csv"

HEALTHY_DIR = os.path.join(PNG_DIR, "healthy")
PARKINSON_DIR = os.path.join(PNG_DIR, "parkinson")

os.makedirs(HEALTHY_DIR, exist_ok=True)
os.makedirs(PARKINSON_DIR, exist_ok=True)

# Load metadata
df = pd.read_csv(METADATA_FILE)

# Convert IDs to string
df["Image Data ID"] = df["Image Data ID"].astype(str)

count = 0
unmatched = []

for file in os.listdir(PNG_DIR):

    if file.endswith(".png"):

        matched = False

        # Extract IDs like I276943
        ids = re.findall(r'I\d+', file)

        for extracted_id in ids:

            for _, row in df.iterrows():

                image_id = row["Image Data ID"]
                group = row["Group"]

                if image_id == extracted_id:

                    src = os.path.join(PNG_DIR, file)

                    if group == "Control":
                        dst = os.path.join(HEALTHY_DIR, file)

                    elif group == "PD":
                        dst = os.path.join(PARKINSON_DIR, file)

                    else:
                        continue

                    shutil.move(src, dst)

                    count += 1
                    matched = True
                    break

            if matched:
                break

        if not matched:
            unmatched.append(file)

print(f"\n✅ Organized {count} PNG files")

print("\n❌ Unmatched files:")
for f in unmatched:
    print(f)