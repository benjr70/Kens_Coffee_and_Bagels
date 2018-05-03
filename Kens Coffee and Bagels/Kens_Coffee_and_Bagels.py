from Tkinter import *
from DrinkClass import Drink
from draw import Pencial
root = Tk()

#global varibles
CartLabel = Label()
cartRemove = Button()
checkout = Button()
SubtotalLabel = Label()
addonButtonsshown = False
checkoutShowing = False
subtotal = 0
amountentered = ""
pin = ""
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

        WhiteChcoLabel = Label(AddOnsFrame, text = "White Chocolate", padx = 145)
        WhiteChcoLabel.grid(column = 1, row =0)
        WCsub = Button(AddOnsFrame, text = "-", width = 5,height = 2, command = lambda: WCupdater(False))
        WCsub.grid(column = 0, row =1,sticky=NW)
        WCcounter = Label(AddOnsFrame, text = currentDrink.get_WhiteCoco())
        WCcounter.grid(column = 1, row =1)
        WCAdd = Button(AddOnsFrame, text = "+",width = 5,height = 2, command = lambda: WCupdater(True))
        WCAdd.grid(column = 2, row =1, sticky=NE)

        def DCupdater(add):
            currentDrink.set_addDarkCoco(add)
            DCcounter.config(text = currentDrink.get_DarkCoco())

        DarkChcoLabel = Label(AddOnsFrame, text = "Dark Chocolate")
        DarkChcoLabel.grid(column = 1, row =2)
        DCsub = Button(AddOnsFrame, text = "-", width = 5,height = 2, command = lambda: DCupdater(False))
        DCsub.grid(column = 0, row =3,sticky=NW)
        DCcounter = Label(AddOnsFrame, text = currentDrink.get_DarkCoco())
        DCcounter.grid(column = 1, row =3)
        DCAdd = Button(AddOnsFrame, text = "+", width = 5,height = 2, command = lambda: DCupdater(True))
        DCAdd.grid(column = 2, row =3, sticky=NE)

        def MCupdater(add):
            currentDrink.set_addMilkCoco(add)
            MCcounter.config(text = currentDrink.get_MilkCoco())

        MilkChcoLabel = Label(AddOnsFrame, text = "Milk Chocolate")
        MilkChcoLabel.grid(column = 1, row =4)
        MCsub = Button(AddOnsFrame, text = "-", width = 5,height = 2, command = lambda: MCupdater(False))
        MCsub.grid(column = 0, row =5,sticky=NW)
        MCcounter = Label(AddOnsFrame, text = currentDrink.get_MilkCoco())
        MCcounter.grid(column = 1, row =5)
        MCAdd = Button(AddOnsFrame, text = "+", width = 5,height = 2, command = lambda:MCupdater(True))
        MCAdd.grid(column = 2, row =5, sticky=NE)

        def Mupdater(add):
            currentDrink.set_addMilK(add)
            Mcounter.config(text = currentDrink.get_Milk())

        MilkLabel = Label(AddOnsFrame, text = "Milk")
        MilkLabel.grid(column = 1, row =6)
        Msub = Button(AddOnsFrame, text = "-", width = 5,height = 2, command = lambda: Mupdater(False))
        Msub.grid(column = 0, row =7,sticky=NW)
        Mcounter = Label(AddOnsFrame, text = currentDrink.get_Milk())
        Mcounter.grid(column = 1, row =7)
        MAdd = Button(AddOnsFrame, text = "+", width = 5,height = 2, command = lambda:Mupdater(True))
        MAdd.grid(column = 2, row =7, sticky=NE)

        def Whipcupdater(add):
            currentDrink.set_addWhipCream(add)
            Whipccounter.config(text = currentDrink.get_WhipCream())

        WhipcLabel = Label(AddOnsFrame, text = "Whip Cream")
        WhipcLabel.grid(column = 1, row =8)
        Whipcsub = Button(AddOnsFrame, text = "-", width = 5,height = 2, command = lambda: Whipcupdater(False))
        Whipcsub.grid(column = 0, row =9,sticky=NW)
        Whipccounter = Label(AddOnsFrame, text = currentDrink.get_WhipCream())
        Whipccounter.grid(column = 1, row =9)
        WhipcAdd = Button(AddOnsFrame, text = "+", width = 5,height = 2, command = lambda:Whipcupdater(True))
        WhipcAdd.grid(column = 2, row =9, sticky=NE)

        def Strawupdater(add):
            currentDrink.set_addStrawberry(add)
            Strawcounter.config(text = currentDrink.get_Strawberry())

        StrawLabel = Label(AddOnsFrame, text = "Strawberry")
        StrawLabel.grid(column = 1, row =10)
        Strawsub = Button(AddOnsFrame, text = "-", width = 5,height = 2, command = lambda: Strawupdater(False))
        Strawsub.grid(column = 0, row =11,sticky=NW)
        Strawcounter = Label(AddOnsFrame, text = currentDrink.get_Strawberry())
        Strawcounter.grid(column = 1, row =11)
        StrawAdd = Button(AddOnsFrame, text = "+", width = 5,height = 2, command = lambda:Strawupdater(True))
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

        AddToCartButton = Button(AddOnsFrame, text = "Add To Cart",padx = 200, pady = 10, command = lambda: removeAddOns(currentDrink))
        AddToCartButton.grid(column = 0, row = 14, columnspan = 3)

def AddToCart(currentDrink):
    global CartLabel
    global cartRemove 
    global checkout
    global checkoutShowing
    global subtotal
    global SubtotalLabel
    global salesTax
    salesTax = 1.065
    CartLabel = Label(CartFrame, text = currentDrink.GetCarttext())
    CartLabel.pack()
    cartRemove = Button(CartFrame, text = "Remove", command = lambda: removeFromCart(currentDrink))
    cartRemove.pack()
    currentDrink.AddToCart(CartLabel, cartRemove)
    subtotal += currentDrink.get_price()
    if(len(currentDrink.cartList)>0):
        if(checkoutShowing == False):
            checkoutShowing = True
            checkout = Button(CartFrame, text = "Checkout",padx = 210, pady = 10, command = lambda: checkoutDisplay(currentDrink, subtotal))
            checkout.pack(side = BOTTOM)
        SubtotalLabel.pack_forget()
        SubtotalLabel = Label(CartFrame, text = "Total: $" + str(subtotal))
        SubtotalLabel.config(text = "Total: $" + str(subtotal))
        SubtotalLabel.pack(side = BOTTOM)

def removeFromCart(currentDrink):
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

#***********************************************
#function checkout screen
#***********************************************
def checkoutDisplay(currentDrink, total):
    lessSalesTax = total
    total *= salesTax
    checkoutdialog = Toplevel() 
    checkoutdialog.geometry("1400x849")
    optionsLabel = Label(checkoutdialog,  text = "Payment Options")
    optionsLabel.config(font = labelFont)
    optionsLabel.grid(column = 0, row = 0)
    Cash = Button(checkoutdialog, text = "Cash", padx = 140, pady = 10,command = lambda:  Cash(currentDrink,total))
    Cash.grid(column = 0, row = 1)
    Creditcardbutton = Button(checkoutdialog, text = "Credit Card", command = lambda: CreditCardScreen(currentDrink, total), padx = 123, pady = 10)
    Creditcardbutton.grid(column = 0, row = 2)
    debitcardbutton = Button(checkoutdialog, text = "Debit Card", command = lambda: DebitCard(currentDrink,total), padx = 125, pady = 10)
    debitcardbutton.grid(column = 0, row = 3)
    applepaybutton = Button(checkoutdialog, text = "Apple Samsung Pay",padx = 100, pady = 10)
    applepaybutton.grid(column = 0, row = 4)
    rowindex = 1
    ordertitle = Label(checkoutdialog, text = "Your Order")
    ordertitle.config(font = labelFont)
    ordertitle.grid(column = 1, row = 0)
    for x in currentDrink.cartList:
        cart = Label(checkoutdialog, text = x.get_cartText())
        cart.grid(column = 1, row = rowindex)
        rowindex +=1
    stlabel = Label(checkoutdialog, text = "Subtotal: $" + str(round(lessSalesTax,3)))
    rowindex +=1
    stlabel.grid(column = 1, row = rowindex)
    salestaxlabel = Label(checkoutdialog, text="Sales Tax: $" + str(round(total - lessSalesTax,2)))
    rowindex += 1
    salestaxlabel.grid(column=1, row=rowindex)
    totallabel = Label(checkoutdialog, text="Grand Total: $" + str(round(total,2)))
    rowindex += 1
    totallabel.grid(column=1, row=rowindex)
    #***********************************************
    #function for credit card screen
    #***********************************************
    def CreditCardScreen(currentDrink, total):
        CreditCard = Toplevel()
        CreditCard.geometry("1400x849")
        ordertitle = Label(CreditCard, text = "Your Order")
        ordertitle.config(font = labelFont)
        ordertitle.grid(column = 1, row = 0)
        rowindex = 1
        for x in currentDrink.cartList:
            cart = Label(CreditCard, text = x.get_cartText())
            cart.grid(column = 1, row = rowindex)
            rowindex +=1
        totallabel = Label(CreditCard, text = "$" + str(total))
        rowindex +=1 
        totallabel.grid(column = 1, row = rowindex)
        signherelabel = Label(CreditCard, text = "Sign Here")
        signherelabel.grid(column = 2, row = 1)
        drawingboard = Canvas(CreditCard, width = 1000, height = 250, bg = 'white')
        drawingboard.grid(column = 2, row = 2)
        mouse = Pencial(drawingboard)
  
        Preceipt = Button(CreditCard, text = "Print Receipt")
        Preceipt.grid(column = 2, row = 3, sticky = W)
        EMreceipt = Button(CreditCard, text = "Email Receipt")
        EMreceipt.grid(column = 2, row = 3)
        Noreceipt = Button(CreditCard, text = "No Receipt")
        Noreceipt.grid(column = 2, row = 3, sticky = E)

        emaillable = Label(CreditCard, text = "e-mail")
        emaillable.grid(column = 2, row = 4, sticky = W)
        emailTB = Text(CreditCard,width = 115, height = 1)
        emailTB.grid(column = 2, row = 4, sticky = E)
        tip = total*1.15
        tip15 = Button(CreditCard, text = "15% tip: " + str(tip))
        tip15.grid(column = 2, row = 5, sticky = W)
        tip = total*1.25
        tip25 = Button(CreditCard, text = "25% tip: " + str(tip))
        tip25.grid(column = 2, row = 5)
        customtip = Button(CreditCard, text = "Custom Tip")
        customtip.grid(column = 2, row = 5, sticky = E)
        Ctip = Text(CreditCard, width = 5,height = 1)
        Ctip.grid(column = 3, row = 5, sticky = W)
        
        donebutton = Button(CreditCard, text = "Done", command = lambda: Done(currentDrink, CreditCard))
        donebutton.grid(column = 2, row = 6)

    def DebitCard(currentDrink,total):
        global pin
        DebitCardwindow = Toplevel()
        DebitCardwindow.geometry("1400x849")
        ordertitle = Label(DebitCardwindow, text = "Your Order")
        ordertitle.config(font = labelFont)
        ordertitle.grid(column = 1, row = 0)
        rowindex = 1
        for x in currentDrink.cartList:
            cart = Label(DebitCardwindow, text = x.get_cartText())
            cart.grid(column = 1, row = rowindex)
            rowindex +=1
        totallabel = Label(DebitCardwindow, text = "$" + str(total))
        rowindex +=1 
        totallabel.grid(column = 1, row = rowindex)
        enterpin = Label(DebitCardwindow, text = 'Enter Pin Number')
        enterpin.grid(column = 2, row = 2)
        Pinnumber = Label(DebitCardwindow, text = "", height = 1, width = 6,bg = 'white')
        Pinnumber.grid(column = 2, row = 3)
        def updatepin(number):
            global pin
            if(len(pin) < 4):
                pin += str(number)
            Pinnumber.config(text = pin)

        numpad = Frame(DebitCardwindow)
        numpad.grid(column = 2, row = 4)
        num1 = Button(numpad, text = '1', width = 5, height = 3, command = lambda: updatepin("1"))
        num1.grid(column = 0, row = 0)
        num2 = Button(numpad, text = '2', width = 5, height = 3, command = lambda: updatepin("2"))
        num2.grid(column = 1, row = 0)
        num3 = Button(numpad, text = '3', width = 5, height = 3, command = lambda: updatepin("3"))
        num3.grid(column = 2, row = 0)
        num4 = Button(numpad, text = '4', width = 5, height = 3, command = lambda: updatepin("4"))
        num4.grid(column = 0, row = 1)
        num5 = Button(numpad, text = '5', width = 5, height = 3, command = lambda: updatepin("5"))
        num5.grid(column = 1, row = 1)
        num6 = Button(numpad, text = '6', width = 5, height = 3, command = lambda: updatepin("6"))
        num6.grid(column = 2, row = 1)
        num7 = Button(numpad, text = '7', width = 5, height = 3, command = lambda: updatepin("7"))
        num7.grid(column = 0, row = 2)
        num8 = Button(numpad, text = '8', width = 5, height = 3, command = lambda: updatepin("8"))
        num8.grid(column = 1, row = 2)
        num9 = Button(numpad, text = '9', width = 5, height = 3, command = lambda: updatepin("9"))
        num9.grid(column = 2, row = 2)
        num0 = Button(numpad, text = '0', width = 5, height = 3, command = lambda: updatepin("0"))
        num0.grid(column = 1, row = 3)

        Preceipt = Button(DebitCardwindow, text = "Print Receipt")
        Preceipt.grid(column = 2, row = 5, sticky = W)
        EMreceipt = Button(DebitCardwindow, text = "Email Receipt")
        EMreceipt.grid(column = 2, row = 5)
        Noreceipt = Button(DebitCardwindow, text = "No Receipt")
        Noreceipt.grid(column = 2, row = 5, sticky = E)
        emaillable = Label(DebitCardwindow, text = "e-mail")
        emaillable.grid(column = 2, row = 6, sticky = W)
        emailTB = Text(DebitCardwindow,width = 115, height = 1)
        emailTB.grid(column = 2, row = 6, sticky = E)
        tip = total*1.15
        tip15 = Button(DebitCardwindow, text = "15% tip: " + str(tip))
        tip15.grid(column = 2, row = 7, sticky = W)
        tip = total*1.25
        tip25 = Button(DebitCardwindow, text = "25% tip: " + str(tip))
        tip25.grid(column = 2, row = 7)
        customtip = Button(DebitCardwindow, text = "Custom Tip")
        customtip.grid(column = 2, row = 6, sticky = E)
        Ctip = Text(DebitCardwindow, width = 5,height = 1)
        Ctip.grid(column = 3, row = 7, sticky = W)
        donebutton = Button(DebitCardwindow, text = "Done", command = lambda: Done(currentDrink, DebitCardwindow))
        donebutton.grid(column = 2, row = 8)

    def Cash(currentDrink,total):
        Cashwindow = Toplevel()
        Cashwindow.geometry("1400x849")
        global amountentered
        ordertitle = Label(Cashwindow, text = "Your Order")
        ordertitle.config(font = labelFont)
        ordertitle.grid(column = 1, row = 0)
        rowindex = 1
        for x in currentDrink.cartList:
            cart = Label(Cashwindow, text = x.get_cartText())
            cart.grid(column = 1, row = rowindex)
            rowindex +=1
        totallabel = Label(Cashwindow, text = "$" + str(total))
        rowindex +=1 
        totallabel.grid(column = 1, row = rowindex)
        amountgiven = Label(Cashwindow, text = 'Amount Given')
        amountgiven.config(font = labelFont)
        amountgiven.grid(column = 2, row = 0)
        amount = Label(Cashwindow, text = "", height = 1, width = 6,bg = 'white')
        amount.grid(column = 2, row = 3)
        change = 0
        def updateamount(number):
            global amountentered
            amountentered += str(number)
            amount.config(text = amountentered)
            ChangeLable.config(text ="Change = $" + str(int(amountentered) - total))
            

        numpad = Frame(Cashwindow)
        numpad.grid(column = 2, row = 4)
        num1 = Button(numpad, text = '1', width = 5, height = 3, command = lambda: updateamount("1"))
        num1.grid(column = 0, row = 0)
        num2 = Button(numpad, text = '2', width = 5, height = 3, command = lambda: updateamount("2"))
        num2.grid(column = 1, row = 0)
        num3 = Button(numpad, text = '3', width = 5, height = 3, command = lambda: updateamount("3"))
        num3.grid(column = 2, row = 0)
        num4 = Button(numpad, text = '4', width = 5, height = 3, command = lambda: updateamount("4"))
        num4.grid(column = 0, row = 1)
        num5 = Button(numpad, text = '5', width = 5, height = 3, command = lambda: updateamount("5"))
        num5.grid(column = 1, row = 1)
        num6 = Button(numpad, text = '6', width = 5, height = 3, command = lambda: updateamount("6"))
        num6.grid(column = 2, row = 1)
        num7 = Button(numpad, text = '7', width = 5, height = 3, command = lambda: updateamount("7"))
        num7.grid(column = 0, row = 2)
        num8 = Button(numpad, text = '8', width = 5, height = 3, command = lambda: updateamount("8"))
        num8.grid(column = 1, row = 2)
        num9 = Button(numpad, text = '9', width = 5, height = 3, command = lambda: updateamount("9"))
        num9.grid(column = 2, row = 2)
        num0 = Button(numpad, text = '0', width = 5, height = 3, command = lambda: updateamount("0"))
        num0.grid(column = 1, row = 3)

        ChangeLable = Label(Cashwindow, text ="Change = $" + str(change))
        ChangeLable.config(font = labelFont)
        ChangeLable.grid(column = 2, row = 7)

        donebutton = Button(Cashwindow, text = "Done", command = lambda: Done(currentDrink, Cashwindow))
        donebutton.grid(column = 2, row = 8)
    def Done(currentDrink,paymentwindow):
        count = 0
        global CartLabel
        global cartRemove 
        global checkout
        global checkoutShowing
        global subtotal
        global SubtotalLabel
        for x in currentDrink.cartList:
            CartLabel = x.get_label()
            CartLabel.pack_forget()
            cartRemove =x.get_button()
            cartRemove.pack_forget()
            subtotal -= x.get_price()
            SubtotalLabel.pack_forget()
        currentDrink.deletcart()
        subtotal = 0
        checkout.pack_forget()
        checkoutShowing = False
        paymentwindow.withdraw()
        checkoutdialog.withdraw()


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
