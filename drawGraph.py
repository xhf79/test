#!usr/bin/env/python3
#-*- coding = utf-8 -*-

import numpy as np
from tkinter import Tk, Frame, Button,mainloop,messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class draw:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.root = Tk()
        self.root.title("Graph of f(x)")
        self.root.geometry("800x500")

        self.btn_changeXRange=Button(self.root,text="Quit Graph",command=self.quitGraph).place(x=20,y=70)
        self.btn_darwPlot=Button(self.root, text="Show Graph", command=self.drawPlot).place(x=20,y=20)
        self.btn_quitDraw = Button(self.root, text="Exit Calculator", command=self.quitCalculator).place(x=20,y=120)
        
        self.frame = Frame(self.root, width=600, height=400)
        self.frame.place(x=150, y=50)
        self.fig, self.ax = plt.subplots(figsize=(6,4))
        self.canvs = FigureCanvasTkAgg(self.fig, self.frame)
        self.canvs.get_tk_widget().pack()

    def quitGraph(self):
        quit_ask = messagebox.askokcancel('hints', 'Are you ready quit the Graph only?')
        if quit_ask == True:
            #self.root.quit()
            self.root.destroy()
            
    def quitCalculator(self):
        quit_ask = messagebox.askokcancel('hints', 'Are you ready to quit the Calculator?')
        if quit_ask == True:
            self.root.quit()
            self.root.destroy()

    def drawPlot(self):
        
        self.ax.spines['right'].set_visible(False)
        self.ax.spines['top'].set_visible(False)
        #plt.xlim(-3.14)
        #plt.xmax(3.14)
        #plt.ylim(-1.1)
        #plt.xlim(xLower, xUpper)
        #plt.ylim(yLower, yUpper)
        
        plt.xticks([-2*np.pi, -3*np.pi/2,-1*np.pi, -1*np.pi/2, 0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi],
           [r"$-2\pi$", r"$-3\pi/2$",r"$-\pi$",r"$-\pi/2$", r"$0$", r"$\pi/2$", r"$\pi$",
            r"$3\pi/2$", r"$2\pi$"]) 
        
        self.ax.plot(self.x,self.y)
        self.canvs.draw()

class drawElse(draw):
    def __init__(self,x,y):
        #draw.__init__(self,x,y)
        #super(drawElse,self).__init__(x,y)
        super().__init__(x,y)
       

    def drawPlot(self):
        
        self.ax.spines['right'].set_visible(False)
        self.ax.spines['top'].set_visible(False)
        
        self.ax.plot(self.x,self.y)
        self.canvs.draw()

class drawArcSin(draw):
    def __init__(self,x,y):
        super().__init__(x,y)
    def drawPlot(self):
        self.ax.spines['right'].set_visible(False)
        self.ax.spines['top'].set_visible(False)
        plt.yticks([-1*np.pi/2,-1*np.pi/3,-1*np.pi/4, 0,np.pi/4,1*np.pi/3, np.pi/2],
           [r"$-\pi/2$",r"$-\pi/3$",r"$-\pi/4$", r"$0$",r"$\pi/4$",r"$\pi/3$", r"$\pi/2$"
            ]) 
        self.ax.plot(self.x,self.y)
        self.canvs.draw()

class drawArcCos(draw):
    def __init__(self,x,y):
        super().__init__(x,y)
    def drawPlot(self):
        self.ax.spines['right'].set_visible(False)
        self.ax.spines['top'].set_visible(False)
        plt.yticks([0,np.pi/4,1*np.pi/3, np.pi/2, 3*np.pi/4,3*np.pi/2,np.pi,],
           [ r"$0$",r"$\pi/4$",r"$\pi/3$", r"$\pi/2$",r"$3\pi/4$",r"$3\pi/2$",r"$\pi$"
            ]) 
        self.ax.plot(self.x,self.y)
        self.canvs.draw()

class drawArcTan(draw):
    def __init__(self,x,y):
        super().__init__(x,y)
    def drawPlot(self):
        self.ax.spines['right'].set_visible(False)
        self.ax.spines['top'].set_visible(False)
        plt.yticks([-1*np.pi/2,-1*np.pi/3,-1*np.pi/4, 0,np.pi/4,1*np.pi/3, np.pi/2],
           [r"$-\pi/2$",r"$-\pi/3$",r"$-\pi/4$", r"$0$",r"$\pi/4$",r"$\pi/3$", r"$\pi/2$"
            ]) 
        self.ax.plot(self.x,self.y)
        self.canvs.draw()                   

def drawGraph(x,y):
    a = draw(x,y)
    mainloop()

def drawGraphElse(x,y):
    a = drawElse(x,y)
    mainloop()

def drawAntSin(x,y):
    a = drawArcSin(x,y)
    mainloop()
                   
def drawAntCos(x,y):
    a = drawArcCos(x,y)
    mainloop()

def drawAntTan(x,y):
    a = drawArcTan(x,y)
    mainloop()
    
