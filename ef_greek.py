Q=[]
Q=[x for x in range(10,20)]

import numpy as np
import math

# for index,value in enumerate(Q):
#     print(index)
#     print(value)

tries=[x for x in range(0,10)]

print("max value's index:{0}".format(tries.index(max(tries))) )
initial_Q=0
last_Q=0
cur_Q=0

for index,reward in enumerate(tries): 
    tries=index+1
    if tries==1:
        last_Q=0
        cur_Q=last_Q+(1.0/tries)*(reward-last_Q)
        last_Q=cur_Q
    else:
        cur_Q=last_Q+(1.0/tries)*(reward-last_Q)
        last_Q=cur_Q
        if(tries==3):
            print("second time:{0}".format(cur_Q))
        print(cur_Q)



# If you absolutely don't know the final size of the array, you can increment the size of the array like this:

# print(np.random.normal(1,1,5))
# my_arr = np.zeros((0,5))
# for i in range(3):
#     my_arr=np.concatenate( ( my_arr, np.random.normal(i,1,5) ) )
# print(my_arr)

# rocker_arm=np.array([])
results=100
rocker_arm=np.zeros((5,results))
for i in range(1,len(rocker_arm)+1):
    rocker_arm[i-1]=np.random.normal(i,0.5,results)

# print(Q)
Q=np.zeros((1,5),dtype=float)
# Q=np.array(0,0,0,0,0)
counts=np.zeros((0,5),dtype=int)
acc_reward=0

print("random numbers:")
print (np.random.randint(1,5))


def rate_of_discovery(t):
    return 1/(math.sqrt(t))


def generate_random_int(low,high):
    return int(np.random.uniform(low,high))



# for i in range(10):
#     print (generate_random_int(1,5))
discovery_rate=rate_of_discovery(0.1)


for i in range(5):
    explore_or_not=np.random.rand()
    k_value=None
    if(explore_or_not<discovery_rate):
        k_value=generate_random_int(1,5)
    else:
        k_value=Q.index(max(Q))
    # cur_reward=
    random_index=generate_random_int(0,100)
    cur_reward=rocker_arm[k_value][random_index]
    acc_reward+=cur_reward
    Q[i]=(Q[i]*counts[i]+cur_reward)/(counts[i]+1)
    counts[i]+=1
print(acc_reward)

        
    


# print(rocker_arm)
# print(rocker_arm)
# for i in range(1,5):
#     new_arm=np.random.normal(i,1,100)
#     # np.append(rocker_arm,new_arm)
#     rocker_arm=np.concatenate((rocker_arm,new_arm))


# print(rocker_arm)


