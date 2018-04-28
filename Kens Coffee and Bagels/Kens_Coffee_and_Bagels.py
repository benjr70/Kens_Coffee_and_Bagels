from Tkinter import *
from DrinkClass import Drink
root = Tk()

#global varibles
CartLabel = Label()
cartRemove = Button()
checkout = Button()
SubtotalLabel = Label()
addonButtonsshown = False
checkoutShowing = False
subtotal = 0
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

        def WCupdater(add):
            currentDrink.set_addWhiteCoco(add)
            WCcounter.config(text = currentDrink.get_WhiteCoco())

        WhiteChcoLabel = Label(AddOnsFrame, text = "White Chocolate", padx = 174.5)
        WhiteChcoLabel.grid(column = 1, row =0)
        WCsub = Button(AddOnsFrame, text = "-", command = lambda: WCupdater(False))
        WCsub.grid(column = 0, row =1,sticky=NW)
        WCcounter = Label(AddOnsFrame, text = currentDrink.get_WhiteCoco())
        WCcounter.grid(column = 1, row =1)
        WCAdd = Button(AddOnsFrame, text = "+", command = lambda: WCupdater(True))
        WCAdd.grid(column = 2, row =1, sticky=NE)

        def DCupdater(add):
            currentDrink.set_addDarkCoco(add)
            DCcounter.config(text = currentDrink.get_DarkCoco())

        DarkChcoLabel = Label(AddOnsFrame, text = "Dark Chocolate", padx = 174.5)
        DarkChcoLabel.grid(column = 1, row =2)
        DCsub = Button(AddOnsFrame, text = "-", command = lambda: DCupdater(False))
        DCsub.grid(column = 0, row =3,sticky=NW)
        DCcounter = Label(AddOnsFrame, text = currentDrink.get_DarkCoco())
        DCcounter.grid(column = 1, row =3)
        DCAdd = Button(AddOnsFrame, text = "+", command = lambda: DCupdater(True))
        DCAdd.grid(column = 2, row =3, sticky=NE)

        def MCupdater(add):
            currentDrink.set_addMilkCoco(add)
            MCcounter.config(text = currentDrink.get_MilkCoco())

        MilkChcoLabel = Label(AddOnsFrame, text = "Milk Chocolate", padx = 174.5)
        MilkChcoLabel.grid(column = 1, row =4)
        MCsub = Button(AddOnsFrame, text = "-", command = lambda: MCupdater(False))
        MCsub.grid(column = 0, row =5,sticky=NW)
        MCcounter = Label(AddOnsFrame, text = currentDrink.get_MilkCoco())
        MCcounter.grid(column = 1, row =5)
        MCAdd = Button(AddOnsFrame, text = "+", command = lambda:MCupdater(True))
        MCAdd.grid(column = 2, row =5, sticky=NE)

        def Mupdater(add):
            currentDrink.set_addMilK(add)
            Mcounter.config(text = currentDrink.get_Milk())

        MilkLabel = Label(AddOnsFrame, text = "Milk", padx = 174.5)
        MilkLabel.grid(column = 1, row =6)
        Msub = Button(AddOnsFrame, text = "-", command = lambda: Mupdater(False))
        Msub.grid(column = 0, row =7,sticky=NW)
        Mcounter = Label(AddOnsFrame, text = currentDrink.get_Milk())
        Mcounter.grid(column = 1, row =7)
        MAdd = Button(AddOnsFrame, text = "+", command = lambda:Mupdater(True))
        MAdd.grid(column = 2, row =7, sticky=NE)

        def Whipcupdater(add):
            currentDrink.set_addWhipCream(add)
            Whipccounter.config(text = currentDrink.get_WhipCream())

        WhipcLabel = Label(AddOnsFrame, text = "Whip Cream", padx = 174.5)
        WhipcLabel.grid(column = 1, row =8)
        Whipcsub = Button(AddOnsFrame, text = "-", command = lambda: Whipcupdater(False))
        Whipcsub.grid(column = 0, row =9,sticky=NW)
        Whipccounter = Label(AddOnsFrame, text = currentDrink.get_WhipCream())
        Whipccounter.grid(column = 1, row =9)
        WhipcAdd = Button(AddOnsFrame, text = "+", command = lambda:Whipcupdater(True))
        WhipcAdd.grid(column = 2, row =9, sticky=NE)

        def Strawupdater(add):
            currentDrink.set_addStrawberry(add)
            Strawcounter.config(text = currentDrink.get_Strawberry())

        StrawLabel = Label(AddOnsFrame, text = "Strawberry", padx = 174.5)
        StrawLabel.grid(column = 1, row =10)
        Strawsub = Button(AddOnsFrame, text = "-", command = lambda: Strawupdater(False))
        Strawsub.grid(column = 0, row =11,sticky=NW)
        Strawcounter = Label(AddOnsFrame, text = currentDrink.get_Strawberry())
        Strawcounter.grid(column = 1, row =11)
        StrawAdd = Button(AddOnsFrame, text = "+", command = lambda:Strawupdater(True))
        StrawAdd.grid(column = 2, row =11, sticky=NE)

        def removeAddOns(currentDrink):
            global addonButtonsshown
            addonButtonsshown = False
            WhiteChcoLabel.grid_forget()
            WCsub.grid_forget()
            WCAdd.grid_forget()
            WCcounter.grid_forget()
            DarkChcoLabel.grid_forget()
            DCsub.grid_forget()
            DCAdd.grid_forget()
            DCcounter.grid_forget()
            MilkChcoLabel.grid_forget()
            MCsub.grid_forget()
            MCAdd.grid_forget()
            MCcounter.grid_forget()
            MilkLabel.grid_forget()
            Msub.grid_forget()
            MAdd.grid_forget()
            Mcounter.grid_forget()
            WhipcLabel.grid_forget()
            Whipcsub.grid_forget()
            WhipcAdd.grid_forget()
            Whipccounter.grid_forget()
            StrawLabel.grid_forget()
            Strawsub.grid_forget()
            Strawcounter.grid_forget()
            StrawAdd.grid_forget()
            AddToCartButton.grid_forget()
            AddToCart(currentDrink)

        AddToCartButton = Button(AddOnsFrame, text = "Add To Cart", padx = 174.5, pady = 10, command = lambda: removeAddOns(currentDrink))
        AddToCartButton.grid(column = 1, row = 14)

def AddToCart(currentDrink):
    global CartLabel
    global cartRemove 
    global checkout
    global checkoutShowing
    global subtotal
    global SubtotalLabel
    CartLabel = Label(CartFrame, text = currentDrink.GetCarttext())
    CartLabel.pack()
    cartRemove = Button(CartFrame, text = "Remove", command = lambda: removeFromCart(currentDrink.get_name(),currentDrink))
    cartRemove.pack()
    currentDrink.AddToCart(CartLabel, cartRemove)
    subtotal += currentDrink.get_price()
    if(len(currentDrink.cartList)>0):
        if(checkoutShowing == False):
            checkoutShowing = True
            checkout = Button(CartFrame, text = "Checkout",padx = 210, pady = 10)
            checkout.pack(side = BOTTOM)
        SubtotalLabel.pack_forget()
        SubtotalLabel = Label(CartFrame, text = "Total: $" + str(subtotal))
        SubtotalLabel.config(text = "Total: $" + str(subtotal))
        SubtotalLabel.pack(side = BOTTOM)

def removeFromCart(DrinkName, currentDrink):
    global CartLabel
    global cartRemove 
    global checkout
    global checkoutShowing
    global subtotal
    global SubtotalLabel
    CartLabel = currentDrink.get_label()
    CartLabel.pack_forget()
    cartRemove =currentDrink.get_button()
    cartRemove.pack_forget()
    subtotal -= currentDrink.get_price()
    SubtotalLabel.pack_forget()
    SubtotalLabel = Label(CartFrame, text = "Total: $" + str(subtotal))
    SubtotalLabel.config(text = "Total: $" + str(subtotal))
    SubtotalLabel.pack(side = BOTTOM)
    currentDrink.cartList.remove(currentDrink)
    if(len(currentDrink.cartList)<= 0):
        SubtotalLabel.pack_forget()
        checkout.pack_forget()
        checkoutShowing = False


#**************************************************************
# instantiates a Drink objects and passes object to add ons
#***************************************************************
def coffeeSelect(Name, price ,WhiteCoco ,DarkCoco ,MilkCoco ,Milk ,WhipCream ,Strawberry):
    currentDrink = Drink(Name, price ,WhiteCoco ,DarkCoco ,MilkCoco ,Milk ,WhipCream ,Strawberry)
    AddOnbuttons(currentDrink)

#kinds of coffee buttons decleared and packed
mocha = Button(coffeeFrame, text = "Mocha", padx = 210, pady = 10, command = lambda : coffeeSelect("Mocha", 3.50 ,1,2,0,1,1,0))
mocha.pack(expand = YES, fill = X, side = TOP)
latte = Button(coffeeFrame, text = "latte",pady = 10, command = lambda : coffeeSelect("Latte",3.50,0,2,0,1,1,0))
latte.pack(expand = YES, fill = X, side = TOP)
HotCoco = Button(coffeeFrame, text = "Hot Chocolate",pady = 10, command = lambda : coffeeSelect("Hot Chocolate",2.0,0,0,0,1,1,0))
HotCoco.pack(expand = YES, fill = X, side = TOP)
ChiTea = Button(coffeeFrame, text = "ChiTea",pady = 10, command = lambda : coffeeSelect("ChiTea",2.50,0,2,0,1,1,0))
ChiTea.pack(expand = YES, fill = X, side = TOP)

root.title("Kens Coffee and Bagels");
root.geometry("1400x849");
mainloop()
