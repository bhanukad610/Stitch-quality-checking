import cv2

img = cv2.imread('frame-VID_20190212_170922.mp4-154.jpg')
cv2.imshow('test', img)
cv2.waitKey(1000)
imghsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)


imghsv[:,:,2] = [[max(pixel - 25, 0) if pixel < 190 else min(pixel + 25, 255) for pixel in row] for row in imghsv[:,:,2]]
cv2.imshow('contrast', cv2.cvtColor(imghsv, cv2.COLOR_HSV2BGR))
cv2.waitKey(1000)
raw_input()
cv2.imwrite('out.jpg', out)
