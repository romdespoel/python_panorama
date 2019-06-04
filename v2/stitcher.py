import numpy as np
import imutils
import cv2

class Stitcher:

	def findKPandDescriptors(self, image):
		descriptor = cv2.xfeatures2d.SIFT_create()
		kps, feats = descriptor.detectAndCompute(image, None)
		kps = np.float32([kp.pt for kp in kps])
		return (kps, feats)

	#maybe add false positive tests...
	def matchKeypoints(self, KP_a, KP_b, feats_a, feats_b):
		matcher = cv2.DescriptorMatcher_create("BruteForce")
		rawMatches = matcher.knnMatch(feats_a, feats_b, 1)
		matches = [(m[0].trainIdx, m[0].queryIdx) for m in rawMatches]
		return matches

	def stitch(self, im_A, im_B):
		(KP_a, feats_a) = self.findKPandDescriptors(im_A)
		(KP_b, feats_b) = self.findKPandDescriptors(im_B)
		matchKeypoints(KP_a, KP_b, feats_a, feats_b)

	#Find matches, and draw line between images. To serve as test
	def showMatches(self, im_A, im_B):
		(KP_a, feats_a) = self.findKPandDescriptors(im_A)
		(KP_b, feats_b) = self.findKPandDescriptors(im_B)
		matches = self.matchKeypoints(KP_a, KP_b, feats_a, feats_b)

		(hA, wA) = im_A.shape[:2]
		(hB, wB) = im_B.shape[:2]
		combined = np.zeros((max(hA, hB), wA + wB, 3), dtype="uint8")
		combined[0:hA,0:wA] = im_A
		combined[0:hB,wA:] = im_B

		for (trainIdx, queryIdx) in matches:
			ptA = (int(KP_a[queryIdx][0]), int(KP_a[queryIdx][1]))
			ptB = (int(KP_b[trainIdx][0]) + wA, int(KP_b[trainIdx][1]))
			cv2.line(combined, ptA, ptB, (0, 255, 0), 1)

		return combined


if __name__ == "__main__":
	im_A = cv2.imread("tests/A.jpg")
	im_B = cv2.imread("tests/B.jpg")
	s = Stitcher()
	lines = s.showMatches(im_A, im_B)
	#cv2.imshow("keypoints", lines)
	#cv2.waitKey(0)
	cv2.imwrite("tests/lines.jpg", lines)