import matplotlib.pyplot as plt
import numpy as np
import math
from scipy.linalg import lu, qr, svd, norm

fileName = 'myPhoto.jpg'
A = plt.imread(fileName)

#function to extract the desired color layers
def rgb(A_rgb, i):
    color = np.zeros(A.shape, dtype = 'uint8')
    color[:, :, i] = A_rgb[:, :, i]
    return color

Ared = rgb(A, 0)
Agreen = rgb(A, 1)
Ablue = rgb(A, 2)

#plot the 3 images
plt.imshow(Ared)
plt.axis('off')
plt.show()
plt.imshow(Agreen)
plt.axis('off')
plt.show()
plt.imshow(Ablue)
plt.axis('off')
plt.show()

m = len(A)
n = len(A[0])
originalsize = m*n

#function to extract the minimum rank to approximate if we want a compression at percentage%
def singular_value_calculation(percentage):
    c_compressed = percentage*originalsize/100
    return int(c_compressed/(m+n+1))

v = singular_value_calculation(50)

def compression(A, i, v):
    U, D, V = svd(A[:, :, i])
    A1 = U[:, 0:v]@np.diag(D[0:v])@V[0:v, :]
    return A1, D[v]/D[0]

#create the 3 layers
#red
Ared[:, :, 0], ered = compression(Ared, 0, v)


#green
Agreen[:, :, 1], egreen = compression(Agreen, 1, v)


#blue
Ablue[:, :, 2], eblue = compression(Ablue, 2, v)

total_error = math.sqrt(ered**2+egreen**2+eblue**2)

#create the matrix resulting from the compression at 50%
M = np.zeros(A.shape, dtype = 'uint8')
M[:, :, 0] = Ared[:, :, 0]
M[:, :, 1] = Agreen[:, :, 1]
M[:, :, 2] = Ablue[:, :, 2]

plt.imshow(Ared)
plt.axis('off')
plt.show()
plt.imshow(Agreen)
plt.axis('off')
plt.show()
plt.imshow(Ablue)
plt.axis('off')
plt.show()
plt.imshow(M)
plt.axis('off')
plt.show()
print("The global error of the compression is", total_error)
