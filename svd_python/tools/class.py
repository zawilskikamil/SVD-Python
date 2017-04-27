import numpy as np

#rozwiązywanie układów równań
a = np.array([[4, 2],[4, 4]])
b = np.array([0,0])
x = np.linalg.solve(a,b)
print(x)
print(np.allclose(np.dot(a,x),b))
#koniec


