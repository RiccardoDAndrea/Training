# T R A I N _ F U N C T I O N 
def greet(name):
    print('Hello', name)
    return

def add_numbers(num1, num2):
    sum = num1 + num2
    print("Sum", sum)
    return 

def get_full_name(first_name, last_name):
    full_name = first_name + ' ' + last_name
    print('The full name is: ', full_name)
    return 


import matplotlib.pyplot as plt
import numpy as np

x_achse = [1,2,3,4,5,6]
y_achse = [6,5,4,3,2,1]

def create_lineplot(x = int ,y = int ,title_for_plot = str):
    plt.plot(x,y)
    plt.title(title_for_plot)
    plt.legend()
    plt.show()

create_lineplot(x_achse, y_achse, 'This is a test')
