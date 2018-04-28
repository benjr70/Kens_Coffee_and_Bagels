class Drink:
    def __init__(self,Name = "",WhiteCoco = 0,DarkCoco = 0,MilkCoco = 0,Milk = 0,WhipCream = 0,Strawberry = 0):
        self.__default__name = Name
        self.__default__WhiteCoco = WhiteCoco 
        self.__default__DarkCoco = DarkCoco 
        self.__default__MilkCoco = MilkCoco  
        self.__default__Milk = Milk 
        self.__default__WhipCream = WhipCream 
        self.__default__Strawberry = Strawberry
        self.__actual__WhiteCoco = self.__default__WhiteCoco

            
    def set_addWhiteCoco(self, add):
        if(add == True):
            self.__actual__WhiteCoco +=1
        else:
            if(self.__actual__WhiteCoco > 0):
                self.__actual__WhiteCoco -=1

    def get_WhiteCoco(self):
        return self.__actual__WhiteCoco
