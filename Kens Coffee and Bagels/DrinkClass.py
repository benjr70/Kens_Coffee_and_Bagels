from Tkinter import *

class Drink:
    cartList = []
    def __init__(self,Name = "",price = 0,WhiteCoco = 0,DarkCoco = 0,MilkCoco = 0,Milk = 0,WhipCream = 0,Strawberry = 0):
        self.__name = Name
        self.__price = price
        self.__default__WhiteCoco = WhiteCoco 
        self.__default__DarkCoco = DarkCoco 
        self.__default__MilkCoco = MilkCoco  
        self.__default__Milk = Milk 
        self.__default__WhipCream = WhipCream 
        self.__default__Strawberry = Strawberry
        self.__actual__WhiteCoco = self.__default__WhiteCoco
        self.__actual__DarkCoco = self.__default__DarkCoco
        self.__actual__MilkCoco = self.__default__MilkCoco
        self.__actual__Milk = self.__default__Milk
        self.__actual__WhipCream = self.__default__WhipCream
        self.__actual__Strawberry = self.__default__Strawberry
        self.__button = Button()
        self.__label = Label()
        self.__cartText = ""
            
    def get_name(self):
        return self.__name

    def get_cartText(self):
        return self.__cartText

    def set_addWhiteCoco(self, add):
        if(add == True):
            self.__actual__WhiteCoco +=1
        else:
            if(self.__actual__WhiteCoco > 0):
                self.__actual__WhiteCoco -=1

    def get_WhiteCoco(self):
        return self.__actual__WhiteCoco

    def set_addDarkCoco(self, add):
        if(add == True):
            self.__actual__DarkCoco +=1
        else:
            if(self.__actual__DarkCoco > 0):
                self.__actual__DarkCoco -=1

    def get_DarkCoco(self):
        return self.__actual__DarkCoco
    
    def set_addMilkCoco(self, add):
        if(add == True):
            self.__actual__MilkCoco +=1
        else:
            if(self.__actual__MilkCoco > 0):
                self.__actual__MilkCoco -=1

    def get_MilkCoco(self):
        return self.__actual__MilkCoco

    def set_addMilK(self, add):
        if(add == True):
            self.__actual__Milk +=1
        else:
            if(self.__actual__Milk > 0):
                self.__actual__Milk -=1

    def get_Milk(self):
        return self.__actual__Milk

    def set_addWhipCream(self, add):
        if(add == True):
            self.__actual__WhipCream +=1
        else:
            if(self.__actual__WhipCream > 0):
                self.__actual__WhipCream -=1

    def get_WhipCream(self):
        return self.__actual__WhipCream

    def set_addStrawberry(self, add):
        if(add == True):
            self.__actual__Strawberry +=1
        else:
            if(self.__actual__Strawberry > 0):
                self.__actual__Strawberry -=1

    def get_Strawberry(self):
        return self.__actual__Strawberry

    def GetCarttext(self):
        carttext = self.__name
        carttext += "\t\t$" + str(self.__price) + "\t\t"
        if (self.__actual__WhiteCoco != self.__default__WhiteCoco):
            carttext += "\n-White Chocolate(" + str(self.__actual__WhiteCoco) + ")\t"
            if(self.__actual__WhiteCoco > self.__default__WhiteCoco):
                temp =  self.__actual__WhiteCoco - self.__default__WhiteCoco
                carttext += "$" +  str(temp*0.10)
                self.__price += temp*0.1;
            else:
                carttext += "       "
        if (self.__actual__DarkCoco != self.__default__DarkCoco):
            carttext += "\n-Dark Chocolate(" + str(self.__actual__DarkCoco) + ")\t"
            if(self.__actual__DarkCoco > self.__default__DarkCoco):
                temp =  self.__actual__DarkCoco - self.__default__DarkCoco
                carttext += "$" +  str(temp*0.10)
                self.__price += temp*0.1;
            else:
                carttext += "       "
        if (self.__actual__MilkCoco != self.__default__MilkCoco):
            carttext += "\n-Milk Chocolate(" + str(self.__actual__MilkCoco) + ")\t"
            if(self.__actual__MilkCoco > self.__default__MilkCoco):
                temp =  self.__actual__MilkCoco - self.__default__MilkCoco
                carttext += "$" +  str(temp*0.10)
                self.__price += temp*0.1;
            else:
                carttext += "       "
        if (self.__actual__Milk != self.__default__Milk):
            carttext += "\n-Milk(" + str(self.__actual__Milk) + ")\t\t\t"
            if(self.__actual__Milk > self.__default__Milk):
                temp =  self.__actual__Milk - self.__default__Milk
                carttext += "$" +  str(temp*0.10)
                self.__price += temp*0.1;
            else:
                carttext += "       "
        if (self.__actual__WhipCream != self.__default__WhipCream):
            carttext += "\n-Whip Cream(" + str(self.__actual__WhipCream) + ")\t\t"
            if(self.__actual__WhipCream > self.__default__WhipCream):
                temp =  self.__actual__WhipCream - self.__default__WhipCream
                carttext += "$" +  str(temp*0.10)
                self.__price += temp*0.1;
            else:
                carttext += "       "
        if (self.__actual__Strawberry != self.__default__Strawberry):
            carttext += "\n-Strawberry(" + str(self.__actual__Strawberry) + ")\t\t"
            if(self.__actual__Strawberry > self.__default__Strawberry):
                temp =  self.__actual__Strawberry - self.__default__Strawberry
                carttext += "$" +  str(temp*0.10)
                self.__price += temp*0.1;
            else:
                carttext += "       "
        self.__cartText = carttext                                                    
        return carttext

    def AddToCart(self,button,label):
        Drink.cartList.append(self)
        self.__button = button
        self.__label = label

    def deletcart(self):
         Drink.cartList = []

    def get_button(self):
        return self.__button

    def get_label(self):
        return self.__label

    def get_price(self):
        return self.__price