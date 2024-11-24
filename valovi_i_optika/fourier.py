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


z=zica(1,0.25,0.15)
z.y0()
