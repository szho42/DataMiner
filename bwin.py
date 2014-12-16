import gtk.gdk
import sys
import time
import sched
from datetime import datetime

class ScreenShotTaker:
  def __init__(self, start, offset, trails):
    self.starttime = start
    self.offset = offset
    self.trails = trails
    self.window = gtk.gdk.get_default_root_window()
    self.size = self.window.get_size()
    self.buf = None    
    self.timer = sched.scheduler(time.time, time.sleep)

    
  def take(self):
    for trail in range(self.trails):
      self.pixbuf = gtk.gdk.Pixbuf(gtk.gdk.COLORSPACE_RGB, False, 8, \
                            self.size[0],self.size[1])
      self.pixbuf = self.pixbuf.get_from_drawable(self.window, \
                                  self.window.get_colormap(), \
                                  0,0,0,0, self.size[0], self.size[1])

      filename = datetime.now().isoformat()
      
      self.save2file(filename)

      time.sleep(self.offset)
      
  def save2file(self, filename):
    self.pixbuf.save(filename, "png")  
  
  def print_hello(self):
    print "hello"

  def start(self):
    print self.starttime
    print timegm(self.starttime.timetuple())
    now = time.time()
    print now 
    print datetime.fromtimestamp(now).isoformat()

    self.timer.enterabs(time.mktime(self.starttime.timetuple()), 1, self.take, ()) 
    self.timer.run()

def main():
  if len(sys.argv) < 4:
    print "########################################"
    print "3 Arguments required: "
    print "	start time, offset, number of takes"
    print "e.g. python bwin.py 2014:11:14:1:30, 1, 10"
    print "	Means: take 10 screenshots every 1 min from 11:30"
    print "########################################"
 
  starttime = sys.argv[1]
  offset = int(sys.argv[2])
  takes = int(sys.argv[3])
 
  #proces the time
  exetime = datetime(int(starttime.split(":")[0]),\
			int(starttime.split(":")[1]),\
			int(starttime.split(":")[2]),\
			int(starttime.split(":")[3]),\
			int(starttime.split(":")[4]))   
  
  #init a screenshottaker
  sst = ScreenShotTaker(exetime, offset, takes) 
  sst.start()

  return 
  sst.take()
  sst.save2file("test.png") 
  
  time.sleep(2) 
  sst.take()
  sst.save2file("test2.png")

if __name__=='__main__':
  main()
