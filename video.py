import cv2
import sys

argv_list = sys.argv

inputpath = argv_list[1]
opt = argv_list[2]

cap = cv2.VideoCapture(inputpath)
fps = int(round(cap.get(cv2.CAP_PROP_FPS)))
frame_counter = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
frame_figures = len(str(frame_counter))

if opt=="fps":
	print(fps)
elif opt=="countframe":
	print(frame_counter)
elif opt=="countframedigits":
	print(frame_figures)
