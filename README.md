# Image-compression
A black and white photo can be interpreted as a matrix $A$ with size the number of pixels in which each entry is an integer number from $0$ (black) to $255$ (white) 
forming a greayscale. Similarly, a color photo is usually represented in an RGB scale: for each pixel we have $3$ values instead of $1$, therefore the image is
reseprented in $3$ matrices, one corresponding to each color layer (Reg, Green and Blue).

We will approximate the matrices corresponding to our photo by matrices of lower rank via different matrix decomposition methods such as $LU$, $QR$ and $SVD$ and plot 
the resulting photo. The best approximation will be the one performed via the $SVD$, according to the Eckart–Young–Mirsky theorem.

# Use
Download the files `color.py` and `black_and_white.py`. Select your photo and place it in format `.jpg` under the name `myPhoto` in the same directory as the files.
