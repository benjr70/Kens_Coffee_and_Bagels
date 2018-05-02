import Tkinter

class Pencial:
    def __init__(self,canvas,color= 'black',weight = 2, button = '<Button-1>', arrow = 'pencil'):
        self.canvas = canvas
        self.color = color
        self.width = weight
        self.button = button
        self.arrow = arrow
        self.status = 0
        self.bindings = []
        self.activate()

    def activate(self):
        if self.status == 0:
            self.bindings = []
            for i,j in [(self.button, self.create_line),('<B1-Motion>',self.line_drawing),('ButtonRelease',self.button_release)]:
                store = self.canvas.bind(i,j)
                self.bindings.append((i,store))
            self.status = 1
        return
    def button_release(self, event = None):
        self.canvas.config(cursor = 'arrow')
        return

    def create_line(self, event = None):
        self.line = self.canvas.create_line(event.x,event.y,event.x,event.y,fill = self.color, width = self.width)
        self.canvas.config(cursor = self.arrow)
        return

    def line_drawing(self, event=None):
        k = self.canvas.coords(self.line)
        k.append(event.x)
        k.append(event.y)
        self.canvas.coords(self.line, tuple(k))
        return
    
    def deactivate(self):
        if self.status == 1:
            for i,j in self.bindings:
                self.canvas.unbind(i,j)
            self.status = 0
        return

