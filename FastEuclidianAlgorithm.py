from sys import argv

def FastEuclidianAlgorithm (a, b):
    
    if a < b:
        a, b = b, a
        
    
    while b != 0:
        
        a, b = b, a % b
    
    return max(a, b)

print(FastEuclidianAlgorithm(18, 24))

