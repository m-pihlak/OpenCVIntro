# OpenCVIntro

## Guide to initalizing
1. (optional) Create a pyvenv
2. Run the following command:
```
pip install -r requirements.txt
```
## General usage
Images are taken from ./images/in/ and written to ./images/out/

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
## Using haar_dog_detector.py
dog_face.xml is from https://github.com/metinozkan/DogAndCat-Face-Opencv <br>
Finds a dog (probably a cat as well, since the cascade should be for both dogs and cats) face in an image and draws a rectangle around it.<br>
Cascades are from ./cascades/
```
python haar_dog_detector.py [optional: -c <cascade_file_name>] -i <input_file_name> -o <output_file_name>
```
## Using haar_video_detector.py
dog_face.xml is from https://github.com/metinozkan/DogAndCat-Face-Opencv <br>
Finds a dog (probably a cat as well, since the cascade should be for both dogs and cats) face in the webcam and outputs a video stream with rectangle around the face.<br>
To stop the program, press key 'C'.<br>
Cascades are from ./cascades/ <br>
Good at detecting Golden Retrievers.
```
python haar_video_detector.py [optional: -c <cascade_file_name>]
```
# Installing dlib
Since dlib installation is architecture based, then it usually will not work with pip install.<br>
What is needed to make a dlib wheel:
1. CMake https://cmake.org/download/
2. VS Desktop development with C++ https://stackoverflow.com/questions/51668676/cmake-visual-studio-15-2017-could-not-find-any-instance-of-visual-studio
3. dlib source code (also contains instructions for building) https://github.com/davisking/dlib
After creating the wheel, place it in the ./wheels/ directory and run:
```
pip install wheels/dlib-<version>.whl
```
## Using facial_landmarks.py
dogHeadDetector.dat and landmarkDetector.dat are from https://github.com/kairess/dog_face_detector <br>
Finds a dog face in an image and draws a rectangle around it and adds landmarks on it.<br>
Shape predictors are from ./shape_predictors/
```
python facial_landmarks.py -i <input_file_name> -o <output_file_name>
```
## Using april_tag_detector.py
Finds AprilTags from an input image.
```
python apriltag_detector.py -i <input_file_name>
```
