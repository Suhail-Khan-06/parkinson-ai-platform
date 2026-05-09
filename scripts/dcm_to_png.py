import os
import cv2
import numpy as np
import pydicom

INPUT_DIR = "data/raw/datscan_dcm/all_dcm"
OUTPUT_DIR = "data/raw/datscan_png"

os.makedirs(OUTPUT_DIR, exist_ok=True)

count = 0

for file in os.listdir(INPUT_DIR):

    if file.endswith(".dcm"):

        dcm_path = os.path.join(INPUT_DIR, file)

        try:
            # Read dicom
            dicom = pydicom.dcmread(dcm_path)

            # Get pixel array
            image = dicom.pixel_array

            # Handle multi-frame / 3D scans
            if len(image.shape) == 3:
                middle_slice = image.shape[0] // 2
                image = image[middle_slice]

            # Normalize
            image = image.astype(np.float32)

            image = (image - image.min()) / (image.max() - image.min())

            image = (image * 255).astype(np.uint8)

            # Save png
            png_name = file.replace(".dcm", ".png")

            png_path = os.path.join(OUTPUT_DIR, png_name)

            cv2.imwrite(png_path, image)

            count += 1

        except Exception as e:
            print(f"Error processing {file}: {e}")

print(f"✅ Converted {count} DCM files to PNG")