from tkinter import * 
from tkinter import ttk,messagebox
from ttkbootstrap import *   
from numpy import random,linspace,uint16 
import time

class window: 
    sort_names = ['bubble','insertion','selection']
    sorts = {k:False for k in sort_names}
    buttons:list

    def __init__(self,root,title) -> None:
        self.root = root 
        self.root.title(title)
        self.root.resizable(width=0,height=0) 
        bubble_sort_btn = ttk.Button(self.root, text='Bubble Sort', style='info.TButton', padding=5, width=15,
                              command=self.bubble)
        bubble_sort_btn.grid(column=0, row=1, padx=5, pady=5)
        insertion_sort_btn = ttk.Button(self.root, text='Insertion Sort', style='info.TButton', padding=5, width=15,
                            command=self.insertion)
        insertion_sort_btn.grid(column=1, row=1, padx=5, pady=5)
        selection_sort_btn = ttk.Button(self.root, text='Selection Sort', style='info.TButton', padding=5, width=15,
                            command=self.selection)
        selection_sort_btn.grid(column=2, row=1, padx=5, pady=5)

        start_btn = ttk.Button(self.root, text='START', padding=5, width=15,
                            command=self.start)
        start_btn.grid(column=5, row=2, padx=5, pady=5)   

        BUTTONS = [bubble_sort_btn,insertion_sort_btn,selection_sort_btn,
                       start_btn]  
        ttk.Button(self.root, text='RESET', style='info.Outline.TButton', padding=5, width=15,
                        command=self.shuffle).grid(column=5, row=1, padx=5, pady=5)
        
        
        self.buttons = {k:v for k,v in zip(self.sort_names,BUTTONS[:-1])}
        
        ttk.Label(self.root, text='Array Size & Speed:').grid(row=2,column=0)
        self.arraysize=ttk.Scale(self.root,from_=6,to=15,length=200,style='success.Horizontal.TScale',value=10,
            command=lambda x:self.slide_function())
        self.arraysize.grid(row=2,column=1,columnspan=3)
        self.canvas=Canvas(self.root, width=800-5, height=400,highlightbackground="white",highlightthickness=2,
        bg='white')
        self.canvas.grid(row=4, padx=5, pady=10, columnspan=6)

        self.speed=0.2 #sorting speed
        self.N=10
        self.colours=['blue' for i in range(self.N)]
        self.shuffle() 

        self.__sorted_array = ['lime' for _ in range(self.N)]
        self.__default_colours = ['blue' for i in range(self.N)]

    def display(self,N: int,a: list,rong: list)-> None:
        self.canvas.delete('all')
        width=(1570)/(3*N-1)
        gap=width/2

        for i in range(N):
            self.canvas.create_rectangle(7+i*width+i*gap,0,
                                         7+(i+1)*width+i*gap,a[i],fill=rong[i])

        self.root.update_idletasks()    
    
    def slide_function(self):
        self.N=int(self.arraysize.get())
        self.data=linspace(5,400,self.N,dtype=uint16)
        self.speed=5/self.arraysize.get()
        self.colours=['blue' for _ in range(self.N)]
        self.shuffle()
            
    def shuffle(self):
        self.canvas.delete('all')
        self.data=linspace(5,400,self.N,dtype=uint16)
        random.shuffle(self.data)
        self.display(self.N,self.data,self.colours)


    
    def _helper(func):
        def inner(self):
            btn_name = func.__name__
            if self.sorts[btn_name] == False: 
                self.sorts[btn_name] = True
                for k in self.sorts.keys():
                    if k==btn_name:
                        self.buttons[k].config(style='success.TButton')
                    else: 
                        self.sorts[k]=False 
                        self.buttons[k].config(style='info.TButton')
            else: 
                self.sorts[btn_name]=False 
                self.buttons[btn_name].config(style='info.TButton')
        return inner


    @_helper
    def bubble(self):...
    @_helper
    def selection(self):...
    @_helper
    def insertion(self):...
 

    def start(self):
        if self.sorts['bubble'] is True:
            for i in range(self.N-1):
                for j in range(self.N-1-i):
                        self.display(self.N,self.data,['purple' if a==j or a==j+1 else 'green' if a>self.N-1-i else 'blue' for a in range(self.N)])
                        time.sleep(self.speed)
                        if self.data[j]>self.data[j+1]:
                            self.display(self.N,self.data,['red' if a==j or a==j+1 else 'green' if a>self.N-1-i else 'blue' for a in range(self.N)])
                            time.sleep(self.speed)
                            self.data[j],self.data[j+1]=self.data[j+1],self.data[j]
                            self.display(self.N,self.data,['lime' if a==j or a==j+1 else 'green' if a>self.N-1-i else 'blue' for a in range(self.N)])
                            time.sleep(self.speed)
            self.display(self.N,self.data,self.__sorted_array)

        elif self.sorts['insertion'] is True:
            for j in range(1,len(self.data)):
                key=self.data[j]
                i=j-1
                self.display(self.N,self.data,['purple' if a==i or a==i+1 else 'green' if a<=j else'blue' for a in range(self.N)])
                time.sleep(self.speed)
                while i>=0 and self.data[i]>key:
                        self.data[i+1]=self.data[i]
                        self.display(self.N,self.data,['purple' if a==i else 'green' if a<=j else'blue' for a in range(self.N)])
                        time.sleep(self.speed)
                        i-=1
                self.data[i+1]=key
            self.display(self.N,self.data,self.__sorted_array)

        elif self.sorts['selection'] is True:
            for i in range(len(self.data)-1):
                min_index=i
                # loop to find the minimum element and its index
                for j in range(i+1,len(self.data)):
                        self.display(self.N,self.data,['purple' if a==min_index or a==i else 'green' if a<=i else 'blue' for a in range(self.N)])
                        time.sleep(self.speed)
                        if self.data[min_index]>self.data[j]:
                            self.display(self.N,self.data,['red' if a==min_index or a==j else 'green' if a<=i else 'blue' for a in range(self.N)])
                            time.sleep(self.speed)
                            min_index=j
                if min_index!=i:
                        self.data[i], self.data[min_index]=self.data[min_index],self.data[i]
                        self.display(self.N,self.data,['lime' if a==min_index or a==i else 'green' if a<=i else 'blue' for a in range(self.N)])
                        time.sleep(self.speed)
            self.display(self.N,self.data,self.__sorted_array)

        else:
            messagebox.showerror("sorting", "You didn't select any sorting algorithm")
            

if __name__ == '__main__':
     win = Style(theme='classic').master
     obj = window(win, 'Sorting Algorithms')

     win.mainloop()
