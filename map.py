import copy
import random

departure_list = ['n1','n2','n3','n4','n5','n6','n7','n8','n9','n10','n11','n12','n13']

departure = random.choice(departure_list)

fire=departure

while fire ==departure:

    fire = random.choice(departure_list)

 

landscape = {

    'n1':   {'n2':1},
    'n2':   {'n1':1, 'n3':1},
    'n3':   {'n2':1, 'n4':1},
    'n4':   {'n3':1, 'n5':1, 'n13':1},
    'n5':   {'n4':1, 'n6':1},
    'n6':   {'n5':1, 'n7':1, 'n9':1},
    'n7':   {'n6':1, 'n8':1},
    'n8':   {'n7':1},
    'n9':   {'n6':1, 'n10':1},
    'n10':  {'n9':1, 'n11':1},
    'n11':  {'n10':1, 'n12':1},
    'n12':  {'n11':1},
    'n13':  {'n4':1}
}

 

for acc_1,acc_2 in landscape.items():

    for acc_3 in acc_2.keys():

        if acc_3==fire:

            landscape[acc_1][acc_3]=100

 
 

routing = {}

for place in landscape.keys():

    routing[place]={'shortestDist':0, 'route': [], 'visited': 0}

 

def visitPlace(visit):

    routing[visit]['visited'] = 1

    for toGo, betweenDist in landscape[visit].items():

        toDist = routing[visit]['shortestDist'] + betweenDist

        if (routing[toGo]['shortestDist'] >= toDist) or not routing[toGo]['route']:

            routing[toGo]['shortestDist'] = toDist

            routing[toGo]['route'] = copy.deepcopy(routing[visit]['route'])

            routing[toGo]['route'].append(visit)

 

visitPlace(departure)

exit_dis=100

exit_n=''

while 1:

    minDist = max(routing.values(), key=lambda x: x['shortestDist'])['shortestDist']

    toVisit = ''

    for name, search in routing.items():

        if 0 < search['shortestDist'] <= minDist and not search['visited']:

            minDist = search['shortestDist']

            toVisit = name

    if toVisit == '':

        break

    visitPlace(toVisit)

    if toVisit=='n1' or toVisit=='n8' or toVisit=='n13':

        if exit_dis>minDist:

            exit_dis=minDist

            exit_n=toVisit

    #print("[" + toVisit + "]")

    #print("Dist :", minDist)

    
print('fire: ', fire) 

if departure=='n1' or departure=='n8' or departure=='n13':

    print("[", departure, "->", departure, "]")

    print("Route : ", departure)

    print("ShortestDistance : ", 0)

else:

    print("[", departure, "->", exit_n, "]")
    routing[exit_n]['route'].append(exit_n)
    print("Route : ", routing[exit_n]['route'])

    print("ShortestDistance : ", routing[exit_n]['shortestDist'])
