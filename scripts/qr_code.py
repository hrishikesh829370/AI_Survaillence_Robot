import cv2

img = cv2.imread('/home/rishi/rpi/ROS2-Raspberry-PI-Intelligent-Vision-Robot/vision_rpi_bot/meshes/left.png')

decoder = cv2.QRCodeDetector()
data, points, _ = decoder.detectAndDecode(img)
print("results = " , data )

cv2.imshow('Detected QR code is ', img)
cv2.waitKey()
cv2.destroyAllWindows()