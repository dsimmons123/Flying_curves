from djitellopy import Tello
import cv2
from time import sleep

tello = Tello()

tello.connect()
print(tello.get_battery())

tello.takeoff()
sleep(1)

tello.move_up(60)
sleep(2)

#move forward
tello.send_rc_control(0,40, 0, 0)
sleep(2)

#stop forward command
tello.send_rc_control(0,0,0,0)
sleep(2)

#rotate while turning x and y direction
tello.send_rc_control(30, 30, 0, 40)
sleep(6)

#stop turn and rotation
tello.send_rc_control(0, 0, 0, 0)
sleep(2)

tello.land()

