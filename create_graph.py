import pandas as pd
import matplotlib.pyplot as plt

def create_graph():

    # Example 

    data = pd.read_csv("data_file.csv")
    df = pd.DataFrame(data)
    X = list(df.iloc[:, 1])
    Y = list(df.iloc[:, 0])
    
    # Plot the data using bar() method
    plt.bar(X, Y, color='g')
    plt.title("People and their age")
    plt.xlabel("People")
    plt.ylabel("Age")
    plt.show()

    # This is where you create graphs, using the csv_of_data

    ## Task 1
    # Can you do a bar chart for people's names and height?

    # Task 2
    # Can you make a line graph of people and their number of siblings

    # Extension
    # Can you manipulate the data to create a chart that shows the number of people who are homeowners?