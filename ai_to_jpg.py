
import os

# Specify the path to the folder containing your .ai files
input_folder = '/path/to/your/ai/files'

# Specify the output folder for the JPG files
output_folder = '/path/to/your/output/folder'

# Ensure the output folder exists, create it if necessary
os.makedirs(output_folder, exist_ok=True)

# Set the JPEG quality
jpeg_quality = 90
resolution = 300  # Set the resolution to 300 DPI

# Iterate through all files in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith(".ai"):
        # Construct the input and output file paths
        input_file = os.path.join(input_folder, filename)
        output_file = os.path.join(output_folder, f'{os.path.splitext(filename)[0]}.jpg')

        # Use ghostscript to convert AI to JPG with specified quality and resolution
        os.system(f'gs -sDEVICE=jpeg -dJPEGQ={jpeg_quality} -r{resolution} -o "{output_file}" "{input_file}"')

print("Conversion complete.") 