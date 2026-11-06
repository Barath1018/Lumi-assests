from PIL import Image
import os

input_folder = "sprites"
output_folder = "split"

os.makedirs(output_folder, exist_ok=True)

for file in os.listdir(input_folder):

    if file.endswith(".png"):

        img = Image.open(os.path.join(input_folder, file))

        w, h = img.size

        left = img.crop((0, 0, w // 2, h))
        right = img.crop((w // 2, 0, w, h))

        name = os.path.splitext(file)[0]

        left.save(f"{output_folder}/{name}1.png")
        right.save(f"{output_folder}/{name}2.png")

print("Finished")