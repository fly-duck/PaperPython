

# reference 
# https://mpatacchiola.github.io/blog/2016/11/12/the-simplest-classifier-histogram-intersection.html
import numpy as np 



def return_intersection(hist_1, hist_2):
    minima = np.minimum(hist_1,hist_2)
    # this is the minima value in each bin 
    print(minima)
    intersection = np.true_divide(np.sum(minima), np.sum(hist_1))
    # the higher the better 
    print(intersection)
    return intersection


mu_3=4
mu_m3=-4
data_3=np.random.normal(mu_3,2,100)
# data_3=[]
# for i in range(100):
#     data_3.append(np.random.uniform(1,2))
data_m3=np.random.normal(mu_m3,2,100)
#if you not  specific the range the intersection will be really large 
#range means that you put those random numbers in range(-15,15) and range(-15,15) separate equally into 10 parts
histogram_3,edge_3=np.histogram(data_3,bins=10,range=[-15,15])
print(histogram_3)
print("edge_3\n")
print(edge_3)
histogram_m3,_=np.histogram(data_m3,bins=10,range=[-15,15])
print(data_3)
print(data_m3)
#the first array is the numbers in each bin (the value of the histogram)
#the second array is the bin edge 
print(histogram_3)
print(histogram_m3)
return_intersection(histogram_3,histogram_m3)