import scan

num = []


def sorting():
   num = scan.iBeacon()
   top_sort = []

   for i in range(0, len(num)):
      top_sort.append(num[i][0])

   return top_sort

"""
import scan

num = []
determine = []



def sorting():
   num = scan.iBeacon()
   top_sort = []

   for i in range(0, len(num)):
      top_sort.append(num[i][0])

   print "beacon on:"+str(top_sort)
   
   determine = top_sort[0:4]
   determine.sort()

   print "beacon nearby: "+str(determine)

   return determine
"""

"""
while True:
   num = scan.iBeacon()
   top_sort = []

   for i in range(0, len(num)):
      top_sort.append(num[i][0])

   determine = top_sort[0:4]
   determine.sort()

   print determine

"""

"""
def sort_top():
   while True:
      num = scan.iBeacon()
      top_sort = []
      for i in range(0, len(num)):
         top_sort.append(num[i][0])
      return top_sort
"""
"""
def sorting():
   while True:
      num = scan.iBeacon()
      top_sort = []

      for i in range(0, len(num)):
         top_sort.append(num[i][0])

      determine = top_sort[0:4]
      determine.sort()
      return determine
"""
