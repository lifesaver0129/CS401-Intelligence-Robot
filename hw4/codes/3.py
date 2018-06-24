import random as ran
import numpy as np
import matplotlib.pyplot as plt

def motion_model_velocity(u,x,a,d):
    new_v = u[0]+ran.gauss(0,a[0]*np.abs(v[0])+a[1]*np.abs(u[1]))
    new_w = u[1]+ran.gauss(0,a[2]*np.abs(v[0])+a[3]*np.abs(u[1]))
    new_g = ran.gauss(0,a[4]*np.abs(v[0])+a[5]*np.abs(u[1]))
    new_x = x[0]-new_v/new_w *np.sin(x[2]) +new_v/new_w*np.sin(x[2]+new_w+d)
    new_y = x[1]-new_v/new_w *np.cos(x[2]) +new_v/new_w*np.cos(x[2]+new_w+d)
    new_t = x[2]=new_w*d +new_g*d
    return [new_x,new_y,new_t]
    
def staic_model_velocity(u,x,d):
    new_x = x[0]-u[0]/u[1]*np.sin(x[2])+u[0]/u[1]*np.sin(x[2]+u[1]*d)
    new_y = x[1]+u[0]/u[1]*np.cos(x[2])-u[0]/u[1]*np.cos(x[2]+u[1]*d)
    new_t = x[2]+u[1]*d
    return [new_x, new_y, new_t]

def draw(u,x,a,d,x1,x2,y1,y2):
    t=1
    list_x = []
    list_y = []

    for i in range(500):
        temp = motion_model_velocity(u,x,a,d)
        if temp[0]>x1 and temp[0]<x2 and temp[1]>y1 and temp[1]<y2:
            continue
        list_x.append(temp[0])
        list_y.append(temp[1])
    d_temp = staic_model_velocity(u,x,a,d)
    s_temp = staic_model_velocity(u,x,a,d)
    plt.plot([x1, x1, x2, x2, x1], 
        [y2, y1, y1, y2, y2], 'black')
    plt.scatter(1, 1)
    plt.scatter(list_x, list_y)
    plt.show()

if __name__ == '__main__':
    u = [15,15]
    v = [0, 0, 2*np.pi]
    x1 = 3.3
    x2 = 5.7
    y1 = 3.25
    y2 = 3.65
    # if task1
    # a = [0.03 0.03 0.01 0.01 0.01 0.01]; 
    # elif task2
    # a = [0.03 0.03 0.001 0.001 0.001 0.001]; 
    # else task3
    # a = [0.01 0.01 0.02 0.02 0.01 0.01]; 
    # then try this
    draw(u,v,a,0.5,x1,x2,y1,y2)

