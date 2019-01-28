import copy
import random
import requests
import json

def FromWeb(ID):
    data = {"ID":ID} 
    r = requests.get("http://dbwo4011.cafe24.com/KO/KOREA/loadData.php",params = data)

    r.encoding = 'UTF-8'
    Data = json.loads(r.text)

    length = len(Data)

    return Data[length-1]['DATA']

def DTU():
    departure = '1'

    landscape = {

        '1':   {'2':1},
        '2':   {'1':1, '3':1},
        '3':   {'2':1, '4':1},
        '4':   {'3':1, '5':1, '13':1},
        '5':   {'4':1, '6':1},
        '6':   {'5':1, '7':1, '9':1},
        '7':   {'6':1, '8':1},
        '8':   {'7':1},
        '9':   {'6':1, '10':1},
        '10':  {'9':1, '11':1},
        '11':  {'10':1, '12':1},
        '12':  {'11':1},
        '13':  {'4':1}
    }

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

        U = FromWeb(1)
        User = "'"+str(U)+"'"

        if toVisit==User: # user location / server

            if exit_dis>minDist:

                exit_dis=minDist

                exit_n=toVisit

        #print("[" + toVisit + "]")

        #print("Dist :", minDist)
                
    #print("[", departure, "->", exit_n, "]")
    routing[exit_n]['route'].append(exit_n)
    #print("Route : ", routing[exit_n]['route'])
    return routing[exit_n]['route']
    #print("ShortestDistance : ", routing[exit_n]['shortestDist'])
