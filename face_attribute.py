import json
import pickle
import cv2
from deepface import DeepFace
import numpy as np
backends = [
  'opencv', 
  'ssd', 
  'dlib', 
  'mtcnn', 
  'retinaface', 
  'mediapipe',
  'yolov8',
  'yunet',
]
num = 10

def draw_arrow(image_in, pitchyaw, center, length, thickness=2, color=(0, 0, 0)):
    image_out = image_in.copy()
    pos = (int(center[0]), int(center[1]))
    dx = -length * np.sin(pitchyaw[1]) * np.cos(pitchyaw[0])
    dy = -length * np.sin(pitchyaw[0])
    print(length, pitchyaw[0], pitchyaw[1])
    cv2.circle(image_out, pos, int(length), color,2)
    cv2.arrowedLine(image_out, tuple(np.round(pos).astype(np.int32)), tuple(np.round([pos[0] + dx, pos[1] + dy]).astype(int)), color, thickness, cv2.LINE_AA, tipLength=0.2)
    return image_out

def find_closet_candidate(face, candidate):
    pass



for i in range(1, num + 1):
	image_name = f"/work/yuxiang1234/NTUIM-gazing/data/test2/images/{i}.jpg"
	data_name = "/work/yuxiang1234/NTUIM-gazing/results-test-2/" + str(i) + ".pkl"

	img_raw = cv2.imread(image_name, cv2.IMREAD_COLOR)
	#facial analysis
	with open(data_name, "rb") as f: 
		dets = pickle.load(f)

	for b in dets:
		if b[4] < 0.5:
			continue
		text = "{:.4f}".format(b[4])
		pitchyaw = [b[15], b[16]]
		b = list(map(int, b))
		cv2.rectangle(img_raw, (b[0], b[1]), (b[2], b[3]), (0, 0, 255), 2)
		cx = b[0]
		cy = b[1] + 12
		# cv2.putText(img_raw, text, (cx, cy),
					# cv2.FONT_HERSHEY_DUPLEX, 0.5, (255, 255, 255))
		le = np.maximum((b[2] - b[0]) / 2. , (b[3] - b[1]) / 2)
		# landms
		# cv2.circle(img_raw, (b[5], b[6]), 1, (0, 0, 255), 4)
		# cv2.circle(img_raw, (b[7], b[8]), 1, (0, 255, 255), 4)
		# cv2.circle(img_raw, (b[9], b[10]), 1, (255, 0, 255), 4)
		# cv2.circle(img_raw, (b[11], b[12]), 1, (0, 255, 0), 4)
		# cv2.circle(img_raw, (b[13], b[14]), 1, (255, 0, 0), 4)
		img_raw = draw_arrow(img_raw, (pitchyaw[0], pitchyaw[1]), center=( (b[2] + b[0]) / 2. , (b[3] + b[1]) / 2. ), length=le, color=(0, 0, 255))
	name = "/work/yuxiang1234/NTUIM-gazing/results-test-2/" + str(i) + ".jpg"
	print(name)

	results = DeepFace.analyze(img_path = image_name, 
			detector_backend = 'retinaface'
	)
	for face in results:
		x = face["region"]["x"]
		y = face["region"]["y"]
		emotion = face["dominant_emotion"]
		age = str(face["age"]) + " yr"
		gender = face["dominant_gender"]
		race = face["dominant_race"]
		cv2.putText(img_raw, emotion, (x, y - 40), cv2.FONT_HERSHEY_DUPLEX, 0.4, (0, 255, 255))
		cv2.putText(img_raw, age, (x, y - 20), cv2.FONT_HERSHEY_DUPLEX, 0.4, (0, 255, 255))
		cv2.putText(img_raw, gender, (x, y + 20), cv2.FONT_HERSHEY_DUPLEX, 0.4, (0, 255, 255))
		cv2.putText(img_raw, race, (x, y + 40), cv2.FONT_HERSHEY_DUPLEX, 0.4, (0, 255, 255))
		cv2.circle(img_raw, (x, y), 5, (0, 255, 255), 4)
	cv2.imwrite(name, img_raw)