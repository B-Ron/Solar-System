import tkinter as tk
import tkinter.font

class GUI:
    def __init__(self):
        self.main_window = tk.Tk()
        self.canvas = tk.Canvas(self.main_window,width =650,height = 500)
        self.canvas.create_oval(10,280,100,190,fill = 'yellow') #sun
        self.canvas.create_text(55,290, text = 'Sun')
        
        self.canvas.create_oval(115,250,145,225,fill = 'orange') #mercury
        self.canvas.create_text(125,280, text = 'Mercury')

        self.canvas.create_oval(155,220,205,270, fill = 'light blue') #venus
        self.canvas.create_text(180,285, text = 'Venus')
        
        self.canvas.create_oval(225,230,260,260, fill = 'blue')#earth
        self.canvas.create_text(240,280, text = 'Earth')
        
        self.canvas.create_oval(275,240,290,255, fill = 'red')#mars
        self.canvas.create_text(280,275, text = 'Mars')

        self.canvas.create_oval(315,220,380,280, fill = 'brown')#jupiter
        self.canvas.create_text(345,290, text = 'Jupiter')
        
        self.canvas.create_oval(385,240,475,260) #saturn ring
        self.canvas.create_oval(400,225,460,280, fill = 'beige')#saturn planet
        self.canvas.create_text(430,290, text = 'Saturn')

        self.canvas.create_oval(480,220,530,270,fill = 'cyan') #uranus
        self.canvas.create_text(505,285, text = 'Uranus')

        self.canvas.create_oval(535,225,575,270, fill = 'grey') #neptune
        self.canvas.create_text(560,285, text= 'Neptune')

        self.canvas.create_oval(595,240,610,255, fill = 'dark green') #pluto
        self.canvas.create_text(605,270, text = 'Pluto')

        self.font_options = tkinter.font.Font(family = 'Helvitica', size = 25, weight = 'bold')
        self.canvas.create_text(340,50, text = 'Byron Wilson\'s Solar System', font =self.font_options)
        self.canvas.pack()
        tk.mainloop()
final_gui = GUI()
