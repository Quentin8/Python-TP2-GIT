class noeud :
    id = 1
    def __init__(self):
        self.__identifiantNoeud= self.setId()
        self.__ConnectedLinks = []
        self.inc()

    def __str__(self):
        return str(self.__identifiantNoeud)

    def affichageIdentifiantLien(self):
        print('Les liens connectés au noeud ' + str(self.getId()) + ' sont :')
        for l in self.__ConnectedLinks:
            print('Lien ' + l)
    def ajoutIdentifiantLien(self, id):
        self.__ConnectedLinks.append(id)
        #Liste des liens connectés et après on va chercher dans le dictionnaires de Noeuds
    def getId(self):
        return self.__identifiantNoeud
    def getConnectedLinks(self):
        return self.__ConnectedLinks
    @classmethod
    def inc(cls):
        noeud.id+=1
    @classmethod
    def setId(cls):
        return noeud.id
