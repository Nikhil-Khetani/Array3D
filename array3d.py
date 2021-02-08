import numpy as np
import matplotlib.pyplot as plt

arr = np.array([[[1,4,5],[4,3,8],[2,7,2]],[[2,2,4],[8,5,2],[6,4,9]],[[5,8,2],[5,8,2],[5,9,2]]])
print(arr.shape)

def plot3dmatrix(arr):
    fig = plt.figure()
    x, y, z = arr.shape
    x_arr = np.arange(x)
    y_arr = np.arange(y)
    z_arr = np.arange(z)
    ax = plt.axes(projection='3d')
    ax.set_xlim(-0.5,x-0.5)
    ax.set_ylim (-0.5,y-0.5)
    ax.set_zlim(-0.5,z-0.5)

    

    for i in x_arr:
        for j in y_arr:
            for k in z_arr:
                number = str(arr[i,j,k])
                ax.text(i,j,k,label=number,s=number)
                #ax.scatter3D(i,j,k, label= number)
                
    plt.show()
    return

plot3darray(arr)

