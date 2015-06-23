import numpy as np

gm = [None] * 8

gm[0] = np.matrix([[0, 1, 0],[1, 0, 0],[0, 0, 0]])
gm[1] = np.matrix([[0, -1j, 0],[1j, 0, 0],[0, 0, 0]])
gm[2] = np.matrix([[1, 0, 0],[0, -1, 0],[0, 0, 0]])
gm[3] = np.matrix([[0, 0, 1],[0, 0, 0],[1, 0, 0]])
gm[4] = np.matrix([[0, 0, -1j],[0, 0, 0],[1j, 0, 0]])
gm[5] = np.matrix([[0, 0, 0],[0, 0, 1],[0, 1, 0]])
gm[6] = np.matrix([[0, 0, 0],[0, 0, -1j],[0, 1j, 0]])
gm[7] = 3**(-1/2)*np.matrix([[1, 0, 0],[0, 1, 0],[0, 0, -2]])

def commutator(x, y):
    return x*y - y*x

def acommutator(x, y):
    return x*y + y*x

def f(a,b,c):
    ''' 1/4j normalisation constant '''
    return 1/4j * np.trace(commutator(gm[a],gm[b])*gm[c])

def d(a,b,c):
    ''' 1/4 normalisation constant '''
    return 1/4 * np.trace(acommutator(gm[a],gm[b])*gm[c])


''' Calculation of the total antisymmetric structure constants '''
i = 0
while i < 6:
    j = i + 1
    while j < 7:
        k = j + 1
        while k < 8:
            if f(i,j,k) != 0:
                print("f("+str(i+1)+str(j+1)+str(k+1)+") = "+str(abs(f(i,j,k))))
            k += 1
        j += 1
    i += 1

''' Calculation of the total symmetric structure constants '''
i = 0
while i < 8:
    j = i
    while j < 8:
        k = j
        while k < 8:
            if d(i,j,k) != 0:
                print("d("+str(i+1)+str(j+1)+str(k+1)+") = "+str(abs(d(i,j,k))))
            k += 1
        j += 1
    i += 1
