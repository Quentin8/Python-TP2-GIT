from noeud import noeud
from lien import lien

class graph :
    def __init__(self, graphId):
        self._graphId_ = graphId
        self._NbNodes_ = 0
        self._Nodes = {}
        self._Links_ = {}

    def getNbNodes(self):
        return self._NbNodes_

    def addNode(self):
        self._NbNodes_+= 1
        tmp = noeud()
        self._Nodes[tmp.getId()] = tmp

    def addLink(self, dep, arr, dist):
        tmp = lien(dep,arr,dist)
        self._Links_[tmp.getId()] = tmp
        for nodes in self._Nodes.keys() :
            if(str(nodes) == dep) :
                self._Nodes[int(dep)].ajoutIdentifiantLien(tmp.getId())
            if(str(nodes) == arr):
                self._Nodes[int(arr)].ajoutIdentifiantLien(tmp.getId())
    def obtenirProchainsNoeuds(self,currentNodeId):
        next = self._Nodes[currentNodeId].getConnectedLinks()
        counter = 0
        nextTable = {}
        for it in next:
            index = str(it).find(".")+1
            if it[index:] == str(currentNodeId):
                index -=1
                nextTable[counter] = it[:index]
            else:
                nextTable[counter] = it[index:]
            counter+=1
        return nextTable
    def __str__(self):
        tmp = "Le graphique qui a pour ID: " + str(self._graphId_ ) + " contient : \n Liste des liens : \n"
        for l in self._Links_.values():
            tmp+= str(l) +"\n"
        tmp+= "Liste des Noeuds :\n"
        for n in self._Nodes.values():
            tmp+= str(n) + "\n"
            n.affichageIdentifiantLien()
        return tmp
    def minimum(self, Q, precedent):#prend en argument la liste des liens connectés au noeud renvoi plus petite distance
        minDist = -1
        for connectedLinks in Q.getConnectedLinks():
            if minDist == -1 :
                minDist = float(self._Links_[connectedLinks].getDistance())
                node = connectedLinks
            if float(self._Links_[connectedLinks].getDistance()) < minDist and connectedLinks[:connectedLinks.index('.')] != str(precedent):
                node = connectedLinks
                minDist = float(self._Links_[connectedLinks].getDistance())
        return minDist, node



    def Dijkstra(self, source, destination):
        #init des distances et creation du tableau NOEUD=> distance
        d = {}
        p = {}#dans ce dictionnaire on met les noeuds deja passés
        nb_nodes = 0
        for i in self._Nodes.values():#_Nodes est tableau key values
            nb_nodes+=1
            if str(source) == str(i.getId()):
                d[i] = "0"
                Sdeb = i
            else:
                d[i] = "inf"
        #trouver distance minimu
        s = Sdeb #est un noeud
        P_counter = 0
        while P_counter != nb_nodes:
            P_counter+=1
            if(P_counter == 1):
                src = 0
            mini, node = self.minimum(s,src)
            src = node[:node.index('.')]
            p[src] = mini #on met dans un dictionnaire qui sauvegarde le min et sa distance
            node = node[node.index('.')+1:]
            if(node == str(destination)):
                print()#ici verif si la suite est la dest et arreter si oui
            s = self._Nodes[int(node)]


        print(p)



class orientedGraph(graph):
    def obtenirProchainsNoeuds(self,currentNodeId):
        next = self._Nodes[currentNodeId].getConnectedLinks()
        counter = 0
        nextTable = {}
        for it in next:
            index = str(it).find(".")+1
            if(it[index:] == str(currentNodeId) and str(currentNodeId)) != str(it.getSource()):
                index -=1
                nextTable[counter] = it[:index]
            else:
                nextTable[counter] = it[index:]
            counter+=1
        return nextTable
