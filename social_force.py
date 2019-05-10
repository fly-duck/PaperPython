import math
import numpy as np 

mass=80
intended_velocity=1
intended_direction=[1,1]

#  v_i the peerson's velocity 
# F_per:force 

# interaction force F_soc
# F_soc=sum(F_soci)+sum(obstacle)

# f_soc=a_k
ak=10
dik=1.3
rrk=0.4
bk=1
nik=np.array([1,1])
# print(nik)

def social_force_ik(ak,ri,rk,dik,bk,nik):
    force=ak*math.exp(((ri+rk)-dik)/bk)*nik
    return force


print(social_force_ik(ak,0.2,0.2,dik,bk,nik))


