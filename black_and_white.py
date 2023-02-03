import matplotlib.pyplot as plt
import numpy as np
from scipy.linalg import lu, qr, svd, norm

#load our photo
fileName = 'myPhoto.jpg'
A = plt.imread(fileName)

#since the photo is in color, we transform it into a black and white photo
def rgb2gray(A_rgb):
    return np.dot(A_rgb[...,:3], [0.2989, 0.5870, 0.1140])

A_rgb = rgb2gray(A)

#matrix decompositions are performed
P, L, U = lu(A_rgb)
Q, R =  qr(A_rgb)
U1, D, V = svd(A_rgb)

print('Introduce the rank to which you want to approximate')
k = int(input())

if k <= D.size:
    print("The rank is", k)

else:
    k = D.size
    print("Rank greater than the maximum, we recitify to the maximum rank")

#compute the approximations using the given rank 
ALU = P@L[:,0:k]@U[0:k, :]
AQR = Q[:,0:k]@R[0:k,:]
ASVD = U1[:,0:k]@np.diag(D[0:k])@V[0:k, :]

print("The image has %d singular values" % D.size)

#compute the relative error using the two-norm 
eLU = norm(A_rgb-ALU, 2)/norm(A_rgb, 2)
eQR = norm(A_rgb-AQR, 2)/norm(A_rgb, 2)
eSVD = norm(A_rgb-ASVD, 2)/norm(A_rgb, 2)


#to compute eSVD we can use the two-norm properties

if k == D.size:
    print("No hi ha error")
      
else:
    #||A-ASVD||_2/||A||_2 computed via singular values
    eSVD2 = D[k]/D[0]
    if abs(eSVD-eSVD2) < 10e-10:
        print("The calculation via singular values is correct")
  
#plot the obtained results
fig = plt.figure()
fig.add_subplot(2,2,1)
plt.imshow(A, cmap = 'gray')
plt.axis('off')
plt.title('Original Photo')
fig.add_subplot(2,2,2)
plt.imshow(ALU, cmap = 'gray')
plt.axis('off')
plt.title('LU using %d columns. \n'
'Relative error = %5.4f' % (k, eLU));
fig.add_subplot(2,2,3)
plt.imshow(AQR, cmap = 'gray')
plt.axis('off')
plt.title('QR using %d columns. \n'
'Relative error = %5.4f' % (k, eQR));
fig.add_subplot(2,2,4)
plt.imshow(ASVD, cmap = 'gray')
plt.axis('off')
plt.title('SVD using %d columns. \n'
'Relative error = %5.4f' % (k, eSVD));
plt.tight_layout()
plt.show()
