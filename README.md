# ShapeDetector

## Guide to initalizing
1. (optional) Create a pyvenv
2. Run python install -r requirements.txt

## Using load_image.py
Images are taken from images/in and written to images/out
```
python load_image.py -i <input_file_name> -o <output_file_name>
```
```
python convolve_image.py -i <input_file_name> -o <output_file_name> -k <kernel_type>
```
```
python grayscale_histogram.py -i <input_file_name>
```
```
python color_histogram.py -i <input_file_name>
```
```
python histogram_with_mask.py -i <input_file_name>
```