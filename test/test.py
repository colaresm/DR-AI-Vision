from use_cases import segmentation
import cv2
import matplotlib.pyplot as plt

img = cv2.imread("./test/olho-esquerdo-8.jpg")
segmented = segmentation.segment_hard_exudates(img)
plt.imshow(segmented)
plt.show()
