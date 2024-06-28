from rembg import remove
from PIL import Image
import io
import time

input_path = 'IMG_6709.webp'
output_path = 'IMG_6709.png'

# Background color to add
background_color = (152, 231, 81)  

with open(input_path, 'rb') as i:
    with open(output_path, 'wb') as o:
        input_data = i.read()
        start = time.perf_counter()
        output_data = remove(input_data)
        print("process took: ", time.perf_counter() - start)
        # Create a PIL image from the output data
        output_image = Image.open(io.BytesIO(output_data))

        # Create a new image with the desired background color
        new_image = Image.new('RGBA', output_image.size, background_color)

        # Composite the output image onto the new image
        new_image.paste(output_image, (0, 0), output_image)

        # Save the result
        new_image.save(o)
