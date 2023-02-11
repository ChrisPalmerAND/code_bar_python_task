import pandas as pd
import matplotlib.pyplot as plt

def create_graph():

    # Example 

    data = pd.read_csv("data_file.csv")
    df = pd.DataFrame(data)
    X = list(df.iloc[:, 1])
    Y = list(df.iloc[:, 0])
    
    plt.bar(X, Y, color='g')
    plt.title("People and their age")
    plt.xlabel("People")
    plt.ylabel("Age")
    plt.show()

