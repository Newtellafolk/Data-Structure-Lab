"""Radio Stations"""
import json as j
 
def stanum(stations, find):
    count = 0
    for i in stations:
        if i in find:
            count += 1
    return count
 
def findstations(stations):
    count = int(input())
    sttn = []
    pick = []
    for _ in range(count):
        sttn.append(j.loads(input()))
    while stations:
        best = 0
        name = ""
        for i in sttn:
            if best < stanum(stations, i["Cities"]):
                best = stanum(stations, i["Cities"])
                name = i
        if name != "":
            pick.append(name["Name"])
            for i in name["Cities"]:
                if i in stations:
                    stations.remove(i)
            sttn.remove(name)
        else:
            break
    print(sorted(pick))
 
findstations(j.loads(input()))