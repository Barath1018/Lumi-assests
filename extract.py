import cv2
import os

image = cv2.imread("sheet1.png")

sprite_width = 256
sprite_height = 256

output_folder = "output"
os.makedirs(output_folder, exist_ok=True)

count = 1

for y in range(0, image.shape[0], sprite_height):
    for x in range(0, image.shape[1], sprite_width):

        sprite = image[y:y+sprite_height, x:x+sprite_width]

        if sprite.shape[0] == sprite_height and sprite.shape[1] == sprite_width:
            cv2.imwrite(
                os.path.join(output_folder, f"sprite_{count}.png"),
                sprite
            )
            count += 1

print("Done")