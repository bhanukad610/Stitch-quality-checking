import glob
import cv2

images = [cv2.imread(file) for file in glob.glob("*.jpg")]
print images
