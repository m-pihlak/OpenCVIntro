# ShapeDetector

## Guide to initalizing
1. (optional) Create a pyvenv
2. Run the following command:
```
pip install -r requirements.txt
```
## General usage
Images are taken from images/in and written to images/out

## Using load_image.py
General testing of loading and writing images. Allows to convert image filetypes (-i filename.jpg -o filename.png)
```
python load_image.py -i <input_file_name> -o <output_file_name>
```
## Using convolve_image.py
Kernel type is one of the following:
1. smallBlur
2. largeBlur
3. sharpen
4. laplacian
5. sobelX
6. sobelY

Generates an image with the selected convolution applied to it.
```
python convolve_image.py -i <input_file_name> -o <output_file_name> -k <kernel_type>
```
## Using grayscale_histogram.py
Creates a flattened grayscale histogram of the input image
```
python grayscale_histogram.py -i <input_file_name>
```
## Using color_histogram.py
Creates a flattened color histogram and 2D color histograms for input image.
```
python color_histogram.py -i <input_file_name>
```
## Using histogram_with_mask.py
Similar to color_histogram.py, but also applies a mask, which is made by the top left x, y coordinate and bottom right x, y coordinate pairs.
```
python histogram_with_mask.py -i <input_file_name>
```