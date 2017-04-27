import numpy as np

#rozwiązywanie układów równań
a = np.array([[3],[1]])
b = np.array([9])
x = np.linalg.solve(a,b)
print(x)
print(np.allclose(np.dot(a,x),b))
#koniec


