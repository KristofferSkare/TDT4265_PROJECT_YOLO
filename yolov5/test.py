import torch

import cv2 as cv
model = torch.hub.load('ultralytics/yolov5', 'custom', path='runs/train/exp6/weights/best.pt')  # local model

I = cv.imread('data/tdt4265_2022/images/train/trip007_glos_Video00007_99.png')

res = model(I)
res.print()
res.show()