# -*- coding: utf-8 -*-
"""class-111.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1XMic3673eJHcn09y7QWadC5WQupJkz8q
"""

from google.colab import files
a = files.upload()

import plotly.figure_factory as ff
import csv
import statistics
import pandas as pd
import random
import plotly.graph_objects as go

df = pd.read_csv("class_111.csv")
data = df["Math_score"].tolist()

population_mean = statistics.mean(data)
print("Population mean is: ", population_mean)

population_standard_deviation = statistics.stdev(data)
print("Population standard deviation is: ", population_standard_deviation)


def random_set_of_means(counter):
    dataset = []
    for i in range(0, counter):
        random_index = random.randint(0, len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean


mean_list = []
for i in range(0, 1000):
    set_of_means = random_set_of_means(100)
    mean_list.append(set_of_means)

# finding mean of mean_list
mean = statistics.mean(mean_list)
print("Mean of sample distribution: ", mean)

standard_deviation = statistics.stdev(mean_list)
print("standard deviation of sample distribution is: ", standard_deviation)


first_std_dev_start, first_std_dev_end = mean - \
    standard_deviation, mean + standard_deviation
print("std1: ", first_std_dev_start, first_std_dev_end)

second_std_dev_start, second_std_dev_end = mean - \
    (2*standard_deviation), mean + (2*standard_deviation)
print("std2: ", second_std_dev_start, second_std_dev_end)

third_std_dev_start, third_std_dev_end = mean - \
    (3*standard_deviation), mean + (3*standard_deviation)
print("std3: ", third_std_dev_start, third_std_dev_end)

# ploting sample distribution graph
# plotting the graphwith traces
fig = ff.create_distplot([mean_list], ["Students score"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[
              0, 0.17], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[first_std_dev_start, first_std_dev_start], y=[
              0, 0.17], mode="lines", name="standard deviation 1 start"))
fig.add_trace(go.Scatter(x=[first_std_dev_end, first_std_dev_end], y=[
              0, 0.17], mode="lines", name="standard deviation 1 end"))

fig.add_trace(go.Scatter(x=[second_std_dev_start, second_std_dev_start], y=[
              0, 0.17], mode="lines", name="standard deviation 2 start"))
fig.add_trace(go.Scatter(x=[second_std_dev_end, second_std_dev_end], y=[
              0, 0.17], mode="lines", name="standard deviation 2 end"))
fig.add_trace(go.Scatter(x=[third_std_dev_start, third_std_dev_start], y=[
              0, 0.17], mode="lines", name="standard deviation start"))
fig.add_trace(go.Scatter(x=[third_std_dev_end, third_std_dev_end], y=[
              0, 0.17], mode="lines", name="standard deviation 3 end"))
fig.show()

# plotting main data list
# fig = ff.create_distplot([data], ["Math_score"], show_hist=False)
# fig.show()

import plotly.figure_factory as ff
import csv
import statistics
import pandas as pd
import random
import plotly.graph_objects as go

df = pd.read_csv("class_111.csv")
data = df["Math_score"].tolist()

population_mean = statistics.mean(data)
print("Population mean is: ", population_mean)

population_standard_deviation = statistics.stdev(data)
print("Population standard deviation is: ", population_standard_deviation)


def random_set_of_means(counter):
    dataset = []
    for i in range(0, counter):
        random_index = random.randint(0, len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean


mean_list = []
for i in range(0, 1000):
    set_of_means = random_set_of_means(100)
    mean_list.append(set_of_means)

# finding mean of mean_list
mean = statistics.mean(mean_list)
print("Mean of sample distribution: ", mean)

standard_deviation = statistics.stdev(mean_list)
print("standard deviation of sample distribution is: ", standard_deviation)


first_std_dev_start, first_std_dev_end = mean - \
    standard_deviation, mean + standard_deviation
print("std1: ", first_std_dev_start, first_std_dev_end)

second_std_dev_start, second_std_dev_end = mean - \
    (2*standard_deviation), mean + (2*standard_deviation)
print("std2: ", second_std_dev_start, second_std_dev_end)

third_std_dev_start, third_std_dev_end = mean - \
    (3*standard_deviation), mean + (3*standard_deviation)
print("std3: ", third_std_dev_start, third_std_dev_end)

# ploting sample distribution graph
# plotting the graphwith traces
"""
fig = ff.create_distplot([mean_list], ["Students score"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[
              0, 0.17], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[first_std_dev_start, first_std_dev_start], y=[
              0, 0.17], mode="lines", name="standard deviation 1 start"))
fig.add_trace(go.Scatter(x=[first_std_dev_end, first_std_dev_end], y=[
              0, 0.17], mode="lines", name="standard deviation 1 end"))

fig.add_trace(go.Scatter(x=[second_std_dev_start, second_std_dev_start], y=[
              0, 0.17], mode="lines", name="standard deviation 2 start"))
fig.add_trace(go.Scatter(x=[second_std_dev_end, second_std_dev_end], y=[
              0, 0.17], mode="lines", name="standard deviation 2 end"))
fig.add_trace(go.Scatter(x=[third_std_dev_start, third_std_dev_start], y=[
              0, 0.17], mode="lines", name="standard deviation start"))
fig.add_trace(go.Scatter(x=[third_std_dev_end, third_std_dev_end], y=[
              0, 0.17], mode="lines", name="standard deviation 3 end"))
fig.show()

"""


# plotting main data list
# fig = ff.create_distplot([data], ["Math_score"], show_hist=False)
# fig.show()


# students learning from tablet
df = pd.read_csv("data_1.csv")
data_s1 = df["Math_score"].tolist()
mean_of_sample1 = statistics.mean(data_s1)
print("Mean of sample1:- ", mean_of_sample1)

fig = ff.create_distplot([mean_list], ["student marks"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[
              0, 0.17], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[mean_of_sample1, mean_of_sample1], y=[
              0, 0.17], mode="lines", name="MEAN OF STUDENTS WHO HAD tablets"))
fig.add_trace(go.Scatter(x=[first_std_dev_end, first_std_dev_end], y=[
              0, 0.17], mode="lines", name="STANDARD DEVIATION 1 END"))
fig.add_trace(go.Scatter(x=[second_std_dev_end, second_std_dev_end], y=[
              0, 0.17], mode="lines", name="STANDARD DEVIATION 2 END"))
fig.add_trace(go.Scatter(x=[third_std_dev_end, third_std_dev_end], y=[
              0, 0.17], mode="lines", name="STANDARD DEVIATION 3 END"))
fig.show()

z_score = (mean - mean_of_sample1)/standard_deviation

print("The z score is = ",z_score)

import plotly.figure_factory as ff
import csv
import statistics
import pandas as pd
import random
import plotly.graph_objects as go

df = pd.read_csv("class_111.csv")
data = df["Math_score"].tolist()

population_mean = statistics.mean(data)
print("Population mean is: ", population_mean)

population_standard_deviation = statistics.stdev(data)
print("Population standard deviation is: ", population_standard_deviation)


def random_set_of_means(counter):
    dataset = []
    for i in range(0, counter):
        random_index = random.randint(0, len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean


mean_list = []
for i in range(0, 1000):
    set_of_means = random_set_of_means(100)
    mean_list.append(set_of_means)

# finding mean of mean_list
mean = statistics.mean(mean_list)
print("Mean of sample distribution: ", mean)

standard_deviation = statistics.stdev(mean_list)
print("standard deviation of sample distribution is: ", standard_deviation)


first_std_dev_start, first_std_dev_end = mean - \
    standard_deviation, mean + standard_deviation
print("std1: ", first_std_dev_start, first_std_dev_end)

second_std_dev_start, second_std_dev_end = mean - \
    (2*standard_deviation), mean + (2*standard_deviation)
print("std2: ", second_std_dev_start, second_std_dev_end)

third_std_dev_start, third_std_dev_end = mean - \
    (3*standard_deviation), mean + (3*standard_deviation)
print("std3: ", third_std_dev_start, third_std_dev_end)

# ploting sample distribution graph
# plotting the graphwith traces
"""
fig = ff.create_distplot([mean_list], ["Students score"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[
              0, 0.17], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[first_std_dev_start, first_std_dev_start], y=[
              0, 0.17], mode="lines", name="standard deviation 1 start"))
fig.add_trace(go.Scatter(x=[first_std_dev_end, first_std_dev_end], y=[
              0, 0.17], mode="lines", name="standard deviation 1 end"))

fig.add_trace(go.Scatter(x=[second_std_dev_start, second_std_dev_start], y=[
              0, 0.17], mode="lines", name="standard deviation 2 start"))
fig.add_trace(go.Scatter(x=[second_std_dev_end, second_std_dev_end], y=[
              0, 0.17], mode="lines", name="standard deviation 2 end"))
fig.add_trace(go.Scatter(x=[third_std_dev_start, third_std_dev_start], y=[
              0, 0.17], mode="lines", name="standard deviation start"))
fig.add_trace(go.Scatter(x=[third_std_dev_end, third_std_dev_end], y=[
              0, 0.17], mode="lines", name="standard deviation 3 end"))
fig.show()

"""


# plotting main data list
# fig = ff.create_distplot([data], ["Math_score"], show_hist=False)
# fig.show()


# students learning from tablet
df = pd.read_csv("data_2.csv")
data_s1 = df["Math_score"].tolist()
mean_of_sample1 = statistics.mean(data_s1)
print("Mean of sample1:- ", mean_of_sample1)

fig = ff.create_distplot([mean_list], ["student marks"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[
              0, 0.17], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[mean_of_sample1, mean_of_sample1], y=[
              0, 0.17], mode="lines", name="MEAN OF STUDENTS WHO HAD Extra classes"))
fig.add_trace(go.Scatter(x=[first_std_dev_end, first_std_dev_end], y=[
              0, 0.17], mode="lines", name="STANDARD DEVIATION 1 END"))
fig.add_trace(go.Scatter(x=[second_std_dev_end, second_std_dev_end], y=[
              0, 0.17], mode="lines", name="STANDARD DEVIATION 2 END"))
fig.add_trace(go.Scatter(x=[third_std_dev_end, third_std_dev_end], y=[
              0, 0.17], mode="lines", name="STANDARD DEVIATION 3 END"))
fig.show()

z_score = (mean - mean_of_sample1)/standard_deviation

print("The z score is = ",z_score)

import plotly.figure_factory as ff
import csv
import statistics
import pandas as pd
import random
import plotly.graph_objects as go

df = pd.read_csv("class_111.csv")
data = df["Math_score"].tolist()

population_mean = statistics.mean(data)
print("Population mean is: ", population_mean)

population_standard_deviation = statistics.stdev(data)
print("Population standard deviation is: ", population_standard_deviation)


def random_set_of_means(counter):
    dataset = []
    for i in range(0, counter):
        random_index = random.randint(0, len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean


mean_list = []
for i in range(0, 1000):
    set_of_means = random_set_of_means(100)
    mean_list.append(set_of_means)

# finding mean of mean_list
mean = statistics.mean(mean_list)
print("Mean of sample distribution: ", mean)

standard_deviation = statistics.stdev(mean_list)
print("standard deviation of sample distribution is: ", standard_deviation)


first_std_dev_start, first_std_dev_end = mean - \
    standard_deviation, mean + standard_deviation
print("std1: ", first_std_dev_start, first_std_dev_end)

second_std_dev_start, second_std_dev_end = mean - \
    (2*standard_deviation), mean + (2*standard_deviation)
print("std2: ", second_std_dev_start, second_std_dev_end)

third_std_dev_start, third_std_dev_end = mean - \
    (3*standard_deviation), mean + (3*standard_deviation)
print("std3: ", third_std_dev_start, third_std_dev_end)

# ploting sample distribution graph
# plotting the graphwith traces
"""
fig = ff.create_distplot([mean_list], ["Students score"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[
              0, 0.17], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[first_std_dev_start, first_std_dev_start], y=[
              0, 0.17], mode="lines", name="standard deviation 1 start"))
fig.add_trace(go.Scatter(x=[first_std_dev_end, first_std_dev_end], y=[
              0, 0.17], mode="lines", name="standard deviation 1 end"))

fig.add_trace(go.Scatter(x=[second_std_dev_start, second_std_dev_start], y=[
              0, 0.17], mode="lines", name="standard deviation 2 start"))
fig.add_trace(go.Scatter(x=[second_std_dev_end, second_std_dev_end], y=[
              0, 0.17], mode="lines", name="standard deviation 2 end"))
fig.add_trace(go.Scatter(x=[third_std_dev_start, third_std_dev_start], y=[
              0, 0.17], mode="lines", name="standard deviation start"))
fig.add_trace(go.Scatter(x=[third_std_dev_end, third_std_dev_end], y=[
              0, 0.17], mode="lines", name="standard deviation 3 end"))
fig.show()

"""


# plotting main data list
# fig = ff.create_distplot([data], ["Math_score"], show_hist=False)
# fig.show()


# students learning from tablet
df = pd.read_csv("data_3.csv")
data_s3 = df["Math_score"].tolist()
mean_of_sample3 = statistics.mean(data_s3)
print("Mean of sample3:- ", mean_of_sample3)

fig = ff.create_distplot([mean_list], ["student marks"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[
              0, 0.17], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[mean_of_sample1, mean_of_sample1], y=[
              0, 0.17], mode="lines", name="MEAN OF STUDENTS WHO HAD Work sheets"))
fig.add_trace(go.Scatter(x=[first_std_dev_end, first_std_dev_end], y=[
              0, 0.17], mode="lines", name="STANDARD DEVIATION 1 END"))
fig.add_trace(go.Scatter(x=[second_std_dev_end, second_std_dev_end], y=[
              0, 0.17], mode="lines", name="STANDARD DEVIATION 2 END"))
fig.add_trace(go.Scatter(x=[third_std_dev_end, third_std_dev_end], y=[
              0, 0.17], mode="lines", name="STANDARD DEVIATION 3 END"))
fig.show()

z_score = (mean - mean_of_sample3)/standard_deviation

print("The z score is = ",z_score)