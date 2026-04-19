import mediapipe as mp
import cv2
import time
import math
import numpy as np
import hand_tracking_module as htm

from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from ctypes import cast, POINTER

# Camera
wCam, hCam = 640, 480
cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

# Detector
detector = htm.handDetector(detectionCon=0.7)

# Volume control setup

from comtypes import CLSCTX_ALL



# Get default speaker
devices = AudioUtilities.GetSpeakers()

# Use this safe activation method
interface = devices.EndpointVolume
volume = cast(interface, POINTER(IAudioEndpointVolume))

# Volume range
volRange = volume.GetVolumeRange()
minVol = volRange[0]
maxVol = volRange[1]

volBar = 400
volPer = 0
pTime = 0

while True:
    success, img = cap.read()
    if not success:
        break

    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)

    if len(lmList) != 0:
        x1, y1 = lmList[4][1], lmList[4][2]
        x2, y2 = lmList[8][1], lmList[8][2]

        cx, cy = (x1 + x2)//2, (y1 + y2)//2

        # Draw
        cv2.circle(img, (x1, y1), 10, (255, 0, 255), cv2.FILLED)
        cv2.circle(img, (x2, y2), 10, (255, 0, 255), cv2.FILLED)
        cv2.line(img, (x1, y1), (x2, y2), (255, 0, 255), 2)
        cv2.circle(img, (cx, cy), 10, (255, 0, 255), cv2.FILLED)

        # Distance
        length = math.hypot(x2 - x1, y2 - y1)

        # Convert to volume
        # For volume calculation (0–1)
        volNorm = np.interp(length, [50, 300], [0, 1])
        volNorm = volNorm ** 1.3

        # Smooth
        smoothness = 0.02
        volNorm = smoothness * round(volNorm / smoothness)

        # Clamp useful range
        vol = np.interp(volNorm, [0, 1], [-30, maxVol])

        volume.SetMasterVolumeLevel(vol, None)


        # Volume bar values
        volBar = np.interp(length, [50, 300], [400, 150])
        volPer = np.interp(length, [50, 300], [0, 100])



        # Visual feedback
        if length < 50:

            cv2.circle(img, (cx, cy), 10, (0, 255, 0), cv2.FILLED)

    # Draw volume bar
    cv2.rectangle(img, (50, 150), (85, 400), (255, 0, 0), 3)
    cv2.rectangle(img, (50, int(volBar)), (85, 400), (255, 0, 0), cv2.FILLED)

    # Show percentage
    cv2.putText(img, f'{int(volPer)} %', (40, 450),
                cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 2)

    # FPS
    cTime = time.time()
    fps = 1/(cTime - pTime) if (cTime - pTime) != 0 else 0
    pTime = cTime

    cv2.putText(img, f'FPS: {int(fps)}', (40, 50),
                cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 2)

    cv2.imshow("Image", img)

    if cv2.waitKey(1) & 0xFF == ord('p'):
        break

cap.release()
cv2.destroyAllWindows()