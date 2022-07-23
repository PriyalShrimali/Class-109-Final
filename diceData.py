import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random

#Javascript :  Array , Python : List
dice_result = []

for i in range(0,1000):
    dice1= random.randint(1,6)
    dice2= random.randint(1,6)
    dice_result.append(dice1+dice2)

#Calculate mean, mode, median
mean= sum(dice_result)/ len(dice_result)
std_deviation = statistics.stdev(dice_result)
median = statistics.median(dice_result)
mode= statistics.mode(dice_result)

print(mean)
print(median)
print(mode)
print(std_deviation)

bozo=mean-std_deviation

bozos=mean+std_deviation

bozoses=mean+std_deviation+std_deviation

bozosesez = mean -std_deviation-std_deviation

bolozonolezes = mean +std_deviation+std_deviation+std_deviation

bozlonzonolezeslemesz = mean -std_deviation-std_deviation-std_deviation

fig = ff.create_distplot([dice_result], ['results'], show_hist=False)

fig.add_trace(go.Scatter(x=[mean,mean], y=[0,0.17], mode= "lines", name="MEAN"))

fig.add_trace(go.Scatter(x=[bozo,bozo], y=[0,0.17], mode= "lines", name= "First Standard Deviation"))

fig.add_trace(go.Scatter(x=[bozos,bozos], y=[0,0.17], mode= "lines", name= "First Standard Deviation"))

fig.add_trace(go.Scatter(x=[bozoses,bozoses], y=[0,0.17], mode= "lines", name= "Second Standard Deviation"))

fig.add_trace(go.Scatter(x=[bozosesez,bozosesez], y=[0,0.17], mode= "lines", name= "Second Standard Deviation"))

fig.add_trace(go.Scatter(x=[bolozonolezes,bolozonolezes], y=[0,0.17], mode= "lines", name= "Third Standard Deviation"))

fig.add_trace(go.Scatter(x=[bozlonzonolezeslemesz,bozlonzonolezeslemesz], y=[0,0.17], mode= "lines", name= "Third Standard Deviation"))
fig.show()


list_of_data_within_1_std_deviation = [result for result in dice_result if result > bozo and result < bozos]
list_of_data_within_2_std_deviation = [result for result in dice_result if result > bozosesez and result < bozoses]
list_of_data_within_3_std_deviation = [result for result in dice_result if result > bozlonzonolezeslemesz and result < bolozonolezes]

print(format(len(list_of_data_within_1_std_deviation )*100/len(dice_result)))
print(format(len(list_of_data_within_2_std_deviation )*100/len(dice_result)))
print(format(len(list_of_data_within_3_std_deviation )*100/len(dice_result))


