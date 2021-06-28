class Time:
      def __init__(self, hour=12, minute=12, second=0):
           self.hour = hour # Instance Variable
           self.minute = minute
           self.second = second
      def print_time(self):
          print('%.2d:%.2d:%.2d' % (self.hour,self.minute,self.second))
start = Time()
start.print_time()
start = Time(1)
start.print_time()