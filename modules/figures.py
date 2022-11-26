
import numpy as np
import matplotlib.pyplot as plt
import math
import os, sys, shutil, gzip



class FigureSimple:
    ''''
        Une fonction qui montre le figure d'une fonction ou du donnée
    '''
    
    def __init__(self, x_list: list,y_list:list):
     
        self.x_list = x_list
        self.y_list = y_list         
        
    def figure2d(self):
        '''
            une fonction qui montre la figure
        '''
        plt.figure()
        
        if len(self.x_list) == len(self.y_list):
            
            for nbrImg in range(len(self.x_list)):
                plt.plot(self.x_list[nbrImg], self.y_list[nbrImg], label= f'fonction {nbrImg}')
        else:
            print('You have to verify the shape of x_list and y_list')
            
        plt.xlabel('mois')
        plt.ylabel('nombre du population')
        plt.show()
        plt.legend()
        ##if we want to save figure!
        plt.savefig('image2.png')
    
'''
x = np.linspace(0,20,50)
x1 = np.linspace(8,30,50)
x2 = np.linspace(0.2,7.3,50)
x3 = np.linspace(53,73,50)

x_list = [x, x1,x2,x3]
y_list = [np.sin(x), np.cos(x1), np.cos(x2), np.sin(x3)]


fig =FigureSimple(x_list, y_list)
fig.figure2d()

'''


class FigureSubPlot:
    '''
        Des figures dans une image
    '''
    
    def __init__(self,nbr_line, nbr_col,x_list,y_list):
        self.nbr_line = nbr_line
        self.nbr_col = nbr_col
        self.x_list = x_list
        self.y_list = y_list
    
    def getFigure(self):
        '''
            une fonction qui trace les courbes des foncions
        '''
        plt.figure()
        for position in range(1,len(self.x_list)+1):
            plt.subplot(self.nbr_line, self.nbr_col, position)
            plt.plot(self.x_list[position-1], self.y_list[position-1])
            plt.title(f'Figure ({position})')
        
        plt.show()
        plt.legend()
        ##if we want to save figure!!
        plt.savefig('image1.png')

'''
x = np.linspace(0,20,50)
x1 = np.linspace(8,30,50)
x2 = np.linspace(0.2,7.3,50)
x3 = np.linspace(53,73,50)

x_list = [x, x1,x2,x3]
y_list = [np.sin(x), np.cos(x1), np.cos(x2), np.sin(x3)]


fig =FigureSubPlot(2,2,x_list, y_list)
fig.getFigure()

'''


class Scatter:
    '''
        
    '''
    
    def __init__(self, x_list: list, y_liist:list):
        self.x_list = x_list
        self.y_list = y_liist

    def trace(self):
        #x_table = np.array(self.x_list)
        #y_table = np.array(self.y_list)
        for i in range(len(self.x_list)):
            plt.scatter(self.x_list[i],self.y_list[i])
        plt.show()
        plt.savefig('scattre.png')
        
'''
x = [1,2,5,4,6,86,2]
y = [53,45,16,78,5,5,8]

sary = Scatter(x,y)
sary.trace()
'''       


class Histogramme:
    '''
        figure histogramme
    '''
    
    def __init__(self) -> None:
        pass
    
    def trace(self):
        plt.figure()
        plt.hist2d(x=np.array([1,2,3]), y=np.array([10,12,5]))
        plt.show()

'''
sary = Histogramme()
sary.trace()
'''

class Compress:
    '''
        classe de compression du fichier
    '''
    
    def __init__(self):

        filename_in = "teste"
        filename_out = "compressed_data.tar.gz"

        with open(filename_in, "rb") as fin, gzip.open(filename_out, "wb") as fout:   
            shutil.copyfileobj(fin, fout)

        #print(f"Uncompressed size: {os.stat(filename_in).st_size}")
        #print(f"Compressed size: {os.stat(filename_out).st_size}")

        with gzip.open(filename_out, "rb") as fin:
            data = fin.read()
            
            ##Aficher la taille du fichier Decompresser
            print(f"Decompressed size: {sys.getsizeof(data)}")