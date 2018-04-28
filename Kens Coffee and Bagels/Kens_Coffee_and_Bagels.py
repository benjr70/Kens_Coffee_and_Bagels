from Tkinter import *
from DrinkClass import Drink
root = Tk()

#global varibles needed kinda ugly but it works
addonButtonsshown = False
labelFont = ('verdana', 20, 'bold')

#*****************************************************
#creates titel frame and put the title lable on it
#*****************************************************
titelCanvus = Canvas(root, height = 40, width = 1400, bg = "white")
titelCanvus.pack(side = TOP)
root.titelFrame = titelFrame = Frame(titelCanvus)
titelFrame_id = titelCanvus.create_window(0,0, window = titelFrame, anchor = NW)
CoffeeLabel = Label(titelFrame, text = "Coffees", bg = "white", padx = 175)
CoffeeLabel.pack(side = LEFT)
CoffeeLabel.config(font = labelFont)
CoffeeLabel = Label(titelFrame, text = "Add On's", bg = "white", padx = 175)
CoffeeLabel.pack(side = LEFT)
CoffeeLabel.config(font = labelFont)
CoffeeLabel = Label(titelFrame, text = "Cart", bg = "white", padx = 175)
CoffeeLabel.pack(side = LEFT)
CoffeeLabel.config(font = labelFont)

#*****************************************************
#creates Coffee frame
#this is the left most frame for all the kinda of coffee buttons
#*****************************************************
coffeeCanvas = Canvas(root, height = 970, width = 466, bg = "white")
coffeeCanvas.pack(side = LEFT)
root.coffeeFrame = coffeeFrame = Frame(coffeeCanvas)
coffeeFrame_id = coffeeCanvas.create_window(0,0, window = coffeeFrame, anchor = NW)

#*****************************************************
#creates Add On's frame
#this is the Middle frame for all the coffee Add On's buttons
#*****************************************************
AddOnsCanvas = Canvas(root, height = 970, width = 466, bg = "white")
AddOnsCanvas.pack(side = LEFT)
root.AddOnsFrame = AddOnsFrame = Frame(AddOnsCanvas)
AddOnsFrame_id = AddOnsCanvas.create_window(0,0, window = AddOnsFrame, anchor = NW)

#*****************************************************
#creates Cart frame
#this is the Right most frame for all thing things and buttons in the cart
#*****************************************************
CartCanvas = Canvas(root, height = 970, width = 466, bg = "white")
CartCanvas.pack(side = LEFT)
root.CartFrame = CartFrame = Frame(CartCanvas)
CartFrame_id = CartCanvas.create_window(0,0, window = CartFrame, anchor = NW)

#*****************************************************
#This function puts all the all ons on screen and manages the add on counters
#this gets called from Coffeeorder
#*****************************************************
def AddOnbuttons(currentDrink):
    global addonButtonsshown
    if (addonButtonsshown == False):
        addonButtonsshown = True

        WhiteChcoLabel = Label(AddOnsFrame, text = "White Chocolate", padx = 174.5).grid(column = 1, row =0)
        WCsub = Button(AddOnsFrame, text = "-", command = lambda: currentDrink.set_SubWhiteCoco()).grid(column = 0, row =1,sticky=NW)
        WCcounter = Label(AddOnsFrame, text = currentDrink.get_WhiteCoco())
        WCcounter.grid(column = 1, row =1)
        WCAdd = Button(AddOnsFrame, text = "+", command = lambda:currentDrink.set_addWhiteCoco()).grid(column = 2, row =1, sticky=NE)
        


#*****************************************************
# function gets call when user clicks add to cart this then adds that item to the cart
#*****************************************************
def Cart():
    item = Label(CartFrame, text = CoffeeName).pack()
    if DarkCoco != 0:
        subitem = Label(CartFrame, text = "Dark Chcolate ("+ str(DarkCoco) + ")").pack()

def coffeeSelect(Name ,WhiteCoco ,DarkCoco ,MilkCoco ,Milk ,WhipCream ,Strawberry):
    currentDrink = Drink(Name ,WhiteCoco ,DarkCoco ,MilkCoco ,Milk ,WhipCream ,Strawberry)
    AddOnbuttons(currentDrink)

#kinds of coffee buttons decleared and packed
mocha = Button(coffeeFrame, text = "Mocha", padx = 210, pady = 10, command = lambda : coffeeSelect("Mocha",0,2,0,1,1,0))
mocha.pack(expand = YES, fill = X, side = TOP)
latte = Button(coffeeFrame, text = "latte",pady = 10, command = lambda : coffeeSelect("Latte",0,2,0,1,1,0))
latte.pack(expand = YES, fill = X, side = TOP)
HotCoco = Button(coffeeFrame, text = "Hot Chocolate",pady = 10, command = lambda : coffeeSelect("Hot Chocolate",0,2,0,1,1,0))
HotCoco.pack(expand = YES, fill = X, side = TOP)
ChiTea = Button(coffeeFrame, text = "ChiTea",pady = 10, command = lambda : coffeeSelect("ChiTea",0,2,0,1,1,0))
ChiTea.pack(expand = YES, fill = X, side = TOP)


root.title("Kens Coffee and Bagels");
root.geometry("1400x849");
mainloop()
