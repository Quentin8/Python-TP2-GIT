from noeud import noeud
from lien import lien
from graph import graph
from graph import orientedGraph

def creationGraph(GraphID, pathToFolder):
   import csv
   with open(pathToFolder) as file:
       reader = csv.reader(file)
       counter = 0
       Graphique = graph(GraphID)
       for row in reader:
           if counter == 0:
               for i in range(0, int(row[0])):
                   Graphique.addNode()
               counter += 1
           else:
               CurrentRow = row[0].replace('\t', ',')
               depart = row[0][:CurrentRow.index(',')]
               arrive = row[0][CurrentRow.index(',')+1:CurrentRow.index(',',2)]
               distance = row[0][CurrentRow.index(',',2)+1:]
               Graphique.addLink(depart,arrive,distance)
               counter+=1
       return Graphique
def creationOrientedGraph(GraphID, pathToFolder):
   import csv
   with open(pathToFolder) as file:
       reader = csv.reader(file)
       counter = 0
       Graphique = orientedGraph(GraphID)
       for row in reader:
           if counter == 0:
               for i in range(0, int(row[0])):
                   Graphique.addNode()
               counter += 1
           else:
               CurrentRow = row[0].replace('\t', ',')
               depart = row[0][:CurrentRow.index(',')]
               arrive = row[0][CurrentRow.index(',')+1:CurrentRow.index(',',2)]
               distance = row[0][CurrentRow.index(',',2)+1:]
               Graphique.addLink(depart,arrive,distance)
               counter+=1
       return Graphique







MonGraphe = creationGraph('1','fileGraph1.csv')
Oriente = creationOrientedGraph('2','fileGraph1.csv')
print(MonGraphe)
table = MonGraphe.Dijkstra(1,4)
print("rg")
