from pymycobot.mycobot import MyCobot
import time


mc = MyCobot('COM4',115200)
for count in range(100):
  mc.send_coords([27.5,51.2,217.4,(-87.21),(-32.86),81.63],20,0)
  mc.set_color(225,0,0)
  time.sleep(3)
  mc.set_color(0,225,0)
  time.sleep(3)
  mc.set_color(0,0,225)
  time.sleep(3)
  mc.set_color(225,0,225)
  time.sleep(3)
  mc.set_color(225,225,0)
  time.sleep(3)
  mc.set_color(0,225,225)
  time.sleep(3)
  mc.set_color(150,150,150)
  time.sleep(3)
  mc.set_color(100,50,150)
  time.sleep(3)
mc.release_all_servos()