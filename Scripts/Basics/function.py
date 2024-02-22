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



import requests
import pandas as pd

def get_dataset_from_github(url = str):
    """This function allows you to retrieve data from GitHub repositories.
    
    Input:
    - url: String from the GitHub repository for the dataset in raw data
    
    Output:
    - A dataset if successful code 200, 
      if not sucessfull != 200 it will return the erorr message and None
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Wirft eine Ausnahme, wenn der Statuscode nicht 200 (OK) ist
        dataset = pd.read_csv(url)
        return dataset
    except requests.exceptions.RequestException as e:
        print('Fehler beim Herunterladen des Datasets:', e)
        return None
    
df = get_dataset_from_github(url = 'https://raw.githubusercontent.com/jhnwr/auto-reporting/main/report1.csv')

print(df)




