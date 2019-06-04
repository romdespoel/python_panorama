# python_panorama
Messing about how to create a panorama from a video in Python with openCV

##V1
Lame approach at stripping an image.
Kinda want to see what my flattened out face looks like so that's where we're headed.
Here's my best shot at it so far:
![Alt text](v1/tests/face.jpg?raw=true "Faaaceeeee")

##V2 
Using computer vision, create a more sophisticated panorama from images/videos.

How I'm going to do this: 
	Detect keypoints (Difference of Gaussian)
	Extract features (SIFT?)
	Match features between images
	That's as far ahead as I can see. Will update in due time and will describe what these are

I stopped at: way too many keypoints found, false positives... WIll look into way to get rid of these
