import numpy as np
import matplotlib.pyplot as plt

##Create test array
#test_arr = np.array([[[1,4,5],[4,3,8],[2,7,2]],[[2,2,4],[8,5,2],[6,4,9]],[[5,8,2],[5,8,2],[5,9,2]],[[5,8,2],[5,8,2],[5,9,2]]])

def plot3dmatrix(arr):
    #Visualizes a 3-dimensional numpy array
    fig = plt.figure()
    x, y, z = arr.shape
    #Create position arrays
    x_arr = np.arange(x)
    y_arr = np.arange(y)
    z_arr = np.arange(z)
    #Setup axes
    ax = plt.axes(projection='3d')
    ax.set_xlim(-0.5,x-0.5)
    ax.set_ylim (-0.5,y-0.5)
    ax.set_zlim(-0.5,z-0.5)
    plt.axis("off")
    #Plot each point
    for i in x_arr:
        for j in y_arr:
            for k in z_arr:
                number = str(arr[i,j,k])
                colors = ['Black','Blue','Red','Green']
                ax.text(i,j,k,label=number,s=number, color=colors[i])
    plt.show()
    return

##Print test result
#plot3dmatrix(test_arr)

