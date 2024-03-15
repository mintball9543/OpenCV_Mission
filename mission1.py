import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread('/home/minseok/OpenCV_Mission/test_image.png')

# 크기 재정의
width, height = 640, 480
resized_img = cv2.resize(img, (width, height))

# 하단 높이 1/3 크롭
end_x, end_y = resized_img.shape[:2]
cropped_img = resized_img[2 * end_x//3:, :end_y]
#cv2.imshow('cropped_img', cropped_img)
#cv2.waitKey(0)

# 케니 엣지 변환
canny = cv2.Canny(cropped_img,200,100)
#cv2.imshow('canny', canny)
#cv2.waitKey(0)

# 원본 이미지와 합치기
resized_img[2 * end_x//3:, :end_y] = cv2.bitwise_and(cropped_img,cropped_img,mask=canny)
cv2.imshow('result',resized_img)
cv2.waitKey(0)
"""
c_img = img[:end_x, :end_y]
cv2.copyTo(cropped_img, canny, c_img)
cv2.imshow('result', img)
cv2.waitKey(0)
"""
"""
# 이미지 자르기
# 시작 지점과 종료 지점 좌표 설정 (시작 y:y+h, 시작 x:x+w)
image = cv2.imread('/home/minseok/다운로드/test_image.png')
start_x, start_y, width, height = 100, 100, 200, 200
end_x, end_y = start_x + width, start_y + height
cropped_image = image[start_y:end_y, start_x:end_x]

# 이미지 저장
#cv2.imwrite('/home/minseok/다운로드/test_image.png', cropped_image)

# 이미지 출력
cv2.imshow("test",image)
cv2.imshow("Cropped Image", cropped_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""
