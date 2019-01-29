import sys
sys.path.insert(0, '/home/pi/iBeacon-Scanner-')
import sort
import intertools
import operator

def node():
    node_list = {
        1 : {1: 0, 2: 0, 3: 0, 4: 0},
        2 : {3: 0, 4: 0, 5: 0, 6: 0},
        3 : {4: 0, 6: 0, 7: 0, 8: 0},
        4 : {7: 0, 8: 0, 9: 0, 10: 0},
        5 : {9: 0, 10: 0, 11: 0, 12: 0},
        6 : {11: 0, 12: 0, 13: 0, 14: 0},
        7 : {11: 0, 14: 0, 15: 0},
        8 : {11: 0, 15: 0, 16: 0, 17: 0},
        9 : {13: 0, 14: 0, 18: 0, 19: 0},
        10 : {18: 0, 19: 0, 20: 0, 21: 0},
        11 : {21: 0, 22: 0, 23: 0},
        12 : {22: 0, 23: 0, 24: 0, 25: 0},
        13 : {7: 0, 9: 0, 26: 0, 27: 0}
    }
    return node_list
    
def alarm(beacon, mapping):
    """
    beacon = []
    beacon = sort.sorting()
    print("beacon on: "+str(beacon))

    mapping = node()
    """
    for i in beacon:
        judge = [0]*50
        for key, value in mapping.items():
            for k, v in value.items():
                if k==i:
                    value[k]=1
        for key, value in mapping.items():
            for k, v in value.items():
                if v==1:
                    judge[key] = judge[key]+1
                if judge[key]==len(mapping[key]):
                    return key
                
def most_common(L):
  # get an iterable of (item, iterable) pairs
  SL = sorted((x, i) for i, x in enumerate(L))
  # print 'SL:', SL
  groups = itertools.groupby(SL, key=operator.itemgetter(0))
  # auxiliary function to get "quality" for an item
  def _auxfun(g):
    item, iterable = g
    count = 0
    min_index = len(L)
    for _, where in iterable:
      count += 1
      min_index = min(min_index, where)
    # print 'item %r, count %r, minind %r' % (item, count, min_index)
    return count, -min_index
  # pick the highest-count/earliest item
  return max(groups, key=_auxfun)[0]

count = 0
witch_list = []

while True:
    beacon = []
    beacon = sort.sorting()
    print("beacon on: "+str(beacon))

    mapping = node()

    witch = alarm(beacon, mapping)
    witch_list.append(witch)    

    if witch!=None:
        count=count+1
    if count==10:
        location = witch
        break

    print("drone at node: "+str(witch))

location = most_common(witch_list)
