#import the libraries that we need
from matplotlib import pyplot as plt
import pandas as pd

#get the data from a csv to Dataframe
#change the path to yours
data = pd.DataFrame.from_csv('C:\\Users\\JoseMaria\\Desktop\\codes\\exemples\\exemple0\\multiTimeline.csv',sep=',')

#split the data
x = data.index.values
C = data["C: (Todo el mundo)"]
Python = data["python: (Todo el mundo)"]
R = data["R: (Todo el mundo)"]
Cpp = data["C++: (Todo el mundo)"]

#know the types of this plot
print(plt.style.available)

#plot and save
with plt.style.context('seaborn-poster','presentation'):
    plt.plot(x, C,label='C')
    plt.plot(x, Python,label='Python')
    plt.plot(x, R,label='R')
    plt.plot(x,Cpp,label='C++')
    plt.legend()
    plt.savefig('C:\\Users\\JoseMaria\\Desktop\\codes\\exemples\\exemple0\\pythoncomparsion.png')


##Also we will use this data when we do TSA