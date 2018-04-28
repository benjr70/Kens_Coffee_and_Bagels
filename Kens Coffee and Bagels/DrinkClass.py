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
        self.__button = Button()
        self.__label = Label()
            
    def get_name(self):
        return self.__name

    def set_addWhiteCoco(self, add):
        if(add == True):
            self.__actual__WhiteCoco +=1
        else:
            if(self.__actual__WhiteCoco > 0):
                self.__actual__WhiteCoco -=1

    def get_WhiteCoco(self):
        return self.__actual__WhiteCoco

    def GetCarttext(self):
        carttext = self.__name
        carttext += "\t\t$" + str(self.__price)
        Drink.cartList.append(self)
        if (self.__actual__WhiteCoco != self.__default__WhiteCoco):
            carttext += "\nWhite Chocolate(" + str(self.__actual__WhiteCoco) + ")\t"
            if(self.__actual__WhiteCoco > self.__default__WhiteCoco):
                temp =  self.__actual__WhiteCoco - self.__default__WhiteCoco
            carttext += "$" +  str(temp*0.10) + "\n"
            self.__price += temp*0.1;

        return carttext

    def AddToCart(self,button,label):
        self.__button = button
        self.__label = label


    def get_button(self):
        return self.__button

    def get_label(self):
        return self.__label

    def get_price(self):
        return self.__price