
from picamera import PiCamera
from time import sleep
 
camera = PiCamera()
 
camera.start_preview()
sleep(120)
camera.stop_preview()
