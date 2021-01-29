import cv2, os
import matplotlib.pyplot as plt
path = os.getcwd() + "\\Images\\Face.jpg"
image = cv2.imread(path, cv2.IMREAD_ANYCOLOR)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
# cv2.imshow("Face", image)
# cv2.waitKey(0)
#cv2.destroyAllWindows()
# print(image.shape) # H: 517, W: 926, C: 3  ( B G R )

plt.imshow(image)
plt.show()