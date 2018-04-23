from Tkinter import *
root = Tk()
labelFont = ('verdana', 20, 'bold')
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

coffeeCanvas = Canvas(root, height = 970, width = 466, bg = "white")
coffeeCanvas.pack(side = LEFT)
root.coffeeFrame = coffeeFrame = Frame(coffeeCanvas)
coffeeFrame_id = coffeeCanvas.create_window(0,0, window = coffeeFrame, anchor = NW)

mocha = Button(coffeeFrame, text = "Mocha", padx = 170, pady = 10)
mocha.pack(expand = YES, fill = X, side = TOP)
latte = Button(coffeeFrame, text = "latte",pady = 10)
latte.pack(expand = YES, fill = X, side = TOP)
HotCoco = Button(coffeeFrame, text = "Hot Chocolate",pady = 10)
HotCoco.pack(expand = YES, fill = X, side = TOP)
ChiTea = Button(coffeeFrame, text = "ChiTea",pady = 10)
ChiTea.pack(expand = YES, fill = X, side = TOP)

AddOnsCanvas = Canvas(root, height = 970, width = 466, bg = "white")
AddOnsCanvas.pack(side = LEFT)
root.AddOnsFrame = AddOnsFrame = Frame(AddOnsCanvas)
AddOnsFrame_id = AddOnsCanvas.create_window(0,0, window = AddOnsFrame, anchor = NW)

CartCanvas = Canvas(root, height = 970, width = 466, bg = "white")
CartCanvas.pack(side = LEFT)
root.CartFrame = CartFrame = Frame(CartCanvas)
CartFrame_id = CartCanvas.create_window(0,0, window = CartFrame, anchor = NW)

root.title("Kens Coffee and Bagels");
root.geometry("1400x849");
mainloop()
