import numpy as np
import matplotlib.pyplot as plt

m= 90
g= 9.81
k1= 12
k2= 140
t_open= 20
t_max= 40
dt= 2

tiempo=[]
velocidades=[]

t= 0
v= 0

while t < t_max:
    if t < t_open:
        a= g - (k1/m)*v
    else:
        a= g - (k2/m)*v
    
    v= v + a*dt
    t= t + dt
    
    tiempo.append(t)
    velocidades.append(v)
    
    print(f"t={t:5.1f}  v={v:7.3f}")

print(tiempo) 
print(velocidades) 