import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as anim
from IPython import display


class zica:
    def __init__(self,L,d,h,v=343):
        self.L=L
        self.d=d
        self.h=h
        self.v=v
    def y0(self):
        self.lista_listi_y=[]
        for self.m in range(1,7):
            self.lista_x=[]
            self.lista_y=[]
            self.B0=((2*self.h*(self.L)**3)/((np.pi**2)*self.d*(self.L-self.d)))*(1/self.m**2)*np.sin(self.d*self.m*np.pi/self.L)
            for self.x in np.arange(0,self.L,0.005):
                self.y=self.B0*np.sin(self.m*np.pi*self.x/self.L)
                self.lista_x.append(self.x)
                self.lista_y.append(self.y)
            self.lista_listi_y.append(self.lista_y)
            plt.plot(self.lista_x,self.lista_y)
        self.zbroj_y=[]
        for self.i in range(0,len(np.arange(0,self.L,0.005))):
            self.lista_i=[]
            for self.e in self.lista_listi_y:
                self.lista_i.append(self.e[self.i])
            self.zbroj_y.append(sum(self.lista_i))
        #print(self.zbroj_y)
        plt.plot(self.lista_x,self.zbroj_y)
        plt.show()

    def yt(self):
        self.lista_y1 = []
        self.lista_y2 = []
        self.lista_y3= []
        self.lista_y4 = []
        self.lista_y5 = []
        self.lista_y6 = []
        fig, ax = plt.subplots()
        ax.set_xlim(0, self.L)
        ax.set_ylim(-0.1,0.1)
        line, = ax.plot([], [], lw=2)
        line1, = ax.plot([], [], lw=2)
        line2, = ax.plot([], [], lw=2)
        line3, = ax.plot([], [], lw=2)
        line4, = ax.plot([], [], lw=2)
        line5, = ax.plot([], [], lw=2)
        line6, = ax.plot([], [], lw=2)
        def update(t):
            self.lista_x = []
            self.lista_y = []
            self.lista_y1 = []
            self.lista_y2 = []
            self.lista_y3= []
            self.lista_y4 = []
            self.lista_y5 = []
            self.lista_y6 = []

            for self.x in np.arange(0, self.L, 0.005):
                y_t = 0
                for self.m in range(1, 7):
                    self.omega = self.v * (self.m * np.pi / self.L)
                    self.B0 = ((2 * self.h * (self.L) ** 3) / ((np.pi ** 2) * self.d * (self.L - self.d))) * (1 / self.m ** 2) * np.sin(self.d * self.m * np.pi / self.L)
                    y_t += self.B0 * np.sin(self.m * np.pi * self.x / self.L) * np.cos(self.omega * t)
                self.lista_y1.append(((2 * self.h * (self.L) ** 3) / ((np.pi ** 2) * self.d * (self.L - self.d))) * (1 / 1 ** 2) * np.sin(self.d * 1 * np.pi / self.L) * np.sin(1 * np.pi * self.x / self.L) * np.cos(self.v*np.pi/self.L * t))
                self.lista_y2.append(((2 * self.h * (self.L) ** 3) / ((np.pi ** 2) * self.d * (self.L - self.d))) * (1 / 2 ** 2) * np.sin(self.d * 2 * np.pi / self.L) * np.sin(2 * np.pi * self.x / self.L) * np.cos(2*self.v*np.pi/self.L * t))
                self.lista_y3.append(((2 * self.h * (self.L) ** 3) / ((np.pi ** 2) * self.d * (self.L - self.d))) * (1 / 3** 2) * np.sin(self.d * 3 * np.pi / self.L) * np.sin(3 * np.pi * self.x / self.L) * np.cos(3*self.v*np.pi/self.L * t))
                self.lista_y4.append(((2 * self.h * (self.L) ** 3) / ((np.pi ** 2) * self.d * (self.L - self.d))) * (1 / 4** 2) * np.sin(self.d * 4 * np.pi / self.L) * np.sin(4 * np.pi * self.x / self.L) * np.cos(4*self.v*np.pi/self.L * t))
                self.lista_y5.append(((2 * self.h * (self.L) ** 3) / ((np.pi ** 2) * self.d * (self.L - self.d))) * (1 / 5 ** 2) * np.sin(self.d * 5 * np.pi / self.L) * np.sin(5 * np.pi * self.x / self.L) * np.cos(5*self.v*np.pi/self.L * t))
                self.lista_y6.append(((2 * self.h * (self.L) ** 3) / ((np.pi ** 2) * self.d * (self.L - self.d))) * (1 / 6 ** 2) * np.sin(self.d * 6 * np.pi / self.L) * np.sin(6 * np.pi * self.x / self.L) * np.cos(6*self.v*np.pi/self.L * t))
                self.lista_x.append(self.x)
                self.lista_y.append(y_t)
            line.set_data(self.lista_x, self.lista_y)
            line1.set_data(self.lista_x,self.lista_y1)
            line2.set_data(self.lista_x,self.lista_y2)
            line3.set_data(self.lista_x,self.lista_y3)
            line4.set_data(self.lista_x,self.lista_y4)
            line5.set_data(self.lista_x,self.lista_y5)
            line6.set_data(self.lista_x,self.lista_y6)
            return line,line1,line2,line3,line4,line5,line6

        # Create the animation using FuncAnimation
        ani = anim.FuncAnimation(fig, update, frames=np.arange(0, 20, 0.0005), blit=True, interval=100)
        plt.show()
            




z=zica(2,0.25,0.05)
z.y0()
z.yt()
