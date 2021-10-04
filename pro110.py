import pandas as pd
import plotly.figure_factory as ff
import statistics
import random
import plotly.graph_objects as go

df = pd.read_csv("medium_data.csv")
data = df["reading_time"].tolist()
population_mean = statistics.mean(data)
std_dev = statistics.stdev(data)
print("Population mean : ",population_mean)
print("The standard deviation : ",std_dev)

def random_set_of_mean(counter):
    data_set = []
    for i in range(0,counter):
        random_index = random.randint(0,len(data)-1)
        value = data[random_index]
        data_set.append(value) 
    mean = statistics.mean(data_set)
    return mean

def show_fig(mean_list):
    df = mean_list
    mean = statistics.mean(df)
    figure =ff.create_distplot([df],["reading_time"],show_hist=False)
    figure.add_trace(go.Scatter(x = [mean,mean],y = [0,1],mode = "lines",name = "Mean"))
    figure.show()

def main():
    mean_list = []

    for i in range(0,100):
        set_of_means = random_set_of_mean(30)
        mean_list.append(set_of_means)

    show_fig(mean_list)
    mean = statistics.mean(mean_list)
    std_dev = statistics.stdev(mean_list)
    print("Sampling distribution mean :",mean)
    print("Sampling distribution standard deviation :",std_dev)

main()