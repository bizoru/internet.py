import os
import time
import sys

args = sys.argv
cancion = args[1]
os.system('ping google > result &')
internet = 0
f = open('result','r')
#os.system('killall ping')

while True:
   lines = f.readlines()
   print 'Waiting for Internet Connection'
   if(len(lines) > 0):
      print 'Hay Internet!'
      internet = 1
   if(internet):
      os.system('rvlc '+cancion)
      os.remove('result')
      os.system('killall ping')
      break
   time.sleep(1)
   


