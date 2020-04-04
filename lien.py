class lien :
    LinkID = 0
    def __init__(self,depart,arrive,distance):
        self.__source = depart
        self.__destination = arrive
        self.__distance = distance
        self.__identifiant = str(depart) + "." + str(arrive)
    def __str__(self):
        return "Lien " + str(self.__identifiant)
    def getId(self):
        return self.__identifiant
    def getSource(self):
        return  self.__source
    def getDestination(self):
        return  self.__destination
    def getDistance(self):
        return self.__distance


