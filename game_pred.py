import numpy as np
import re
players = {0:'Alex',1:'Charlton',2:'Vineet'}
results = np.array(range(40),dtype='a20').reshape(4,10)
eachPrediction = np.array(range(20),dtype='a2').reshape(2,10)
score = np.zeros(3)
correctScore=3
correctResult=1
allPredictions = []
done = False

def takeFixtures():
    filename='bplinput.txt'
    file = open(filename)
    text = file.readlines()
    fixtures = [line.strip() for line in text]
    file.close()
    i=0
    for eachMatch in fixtures:
        x=re.match("(.*) ([0-9]+) ?- ?([0-9]+) (.*)", eachMatch)
        results[0,i]=x.group(1)
        results[1,i]=x.group(2)
        results[2,i]=x.group(3)
        results[3,i]=x.group(4)
        i+=1


def takePredictions(noOfParticipants):
    for i in range(0,noOfParticipants):
        print("Enter predictions by "+players[i]+" in x-y format")
        for i in range(0,10):
            eachFixturePrediction = raw_input("Enter prediction for "+results[0,i]+" vs "+results[3,i]+": ")
            x=eachFixturePrediction.split('-')
            eachPrediction[0,i]=str(x[0])
            eachPrediction[1,i]=str(x[1])
        allPredictions.append(eachPrediction)


def scoreEngine():
    for i in range(0,len(players)):
        for j in range(0,10):
            resultH=int(results[1,j])
            resultA=int(results[2,j])
            result=resultH-resultA
            predictionH=int(allPredictions[i][0][j])
            predictionA=int(allPredictions[i][1][j])
            pResult = predictionH-predictionA
            if result == pResult or (result<0 and pResult<0) or (result>0 and pResult>0):
                score[i]+=correctResult
                if resultH==predictionH and resultA==predictionA:
                    score[i]+=correctScore



noOfParticipants=len(players)
takeFixtures()
takePredictions(noOfParticipants)
scoreEngine()
print("Scores are:")
print(score)
for player in players:
    print(players[player]+" has scored "+ str(score[player])+" points" )



"""
West Bromwich Albion 0-1 Tottenham Hotspur
Manchester City 2-2 Liverpool
Queens Park Rangers 0-0 Norwich City
Arsenal 1-0 Stoke City
Everton 3-3 Aston Villa
Newcastle United 3-2 Chelsea
Reading 2-1 Sunderland
West Ham United 1-0 Swansea City
Wigan Athletic 2-2 Southampton
Fulham 0-1 Manchester United



#Opening files in Python should be done using the with idiom: your file is then guaranteed 
#to be close correctly. takeFixtures 

def takeFixtures():
    with open('bplinput.txt') as file:
        for eachMath in file:
            x=re.match("(.*) ([0-9]+) ?- ?([0-9]+) (.*)", eachMatch.strip)
            results[0,i]=x.group(1)
            results[1,i]=x.group(2)
            results[2,i]=x.group(3)
            results[3,i]=x.group(4)
            i+=1
"""