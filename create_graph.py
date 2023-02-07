import pandas as pd
import matplotlib.pyplot as plt

def create_graph():

    # Example 

    data = pd.read_csv("data_file.csv")
    df = pd.DataFrame(data)
    X = list(df.iloc[:, 1])
    Y = list(df.iloc[:, 3])
    
    # Plot the data using bar() method
    plt.bar(X, Y, color='g')
    plt.title("People and their age")
    plt.xlabel("People")
    plt.ylabel("Age")
    plt.show()

    # This is where you create graphs, using the csv_of_data

    # Task 1

    # Task 2

    # Extension