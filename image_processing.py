import cv2
import numpy as np

img=cv2.imread('***.***') #画像を選択
inv = cv2.bitwise_not(img)#ネガポジ変換

# 閾値
threshold_value=127

gray=cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
invgray = cv2.bitwise_not(gray)

# 出力画像用の配列生成
threshold_img = gray.copy()


# 方法1（NumPyで実装）
threshold_img[gray < threshold_value] = 0
threshold_img[gray >= threshold_value] = 255

# 結果を出力
cv2.imwrite('th.png', threshold_img)
cv2.imwrite('inv.jpg',inv)
cv2.imwrite('invgray.jpg',invgray)
