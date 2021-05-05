#####################   Necessary Imports   ##########################

import numpy as np
import pandas as pd
import networkx as nx
from amplify import BinaryMatrix, BinaryQuadraticModel, gen_symbols, Solver
from amplify.client import FixstarsClient
from amplify.client.ocean import DWaveSamplerClient, LeapHybridSamplerClient


########################################    Helper functions  ###############################

def Best_solution(result):         ## finds best sample from multiple samples
    sols = []                      ## based on highest frequency of occurrence
    for i in range(len(result)):
        y = result[i]
        x = [v for k, v in sorted(y.values.items())]
        e = y.energy
        f = y.frequency
        z = {'x':x,'energy':e,'frequency':f}
        sols.append(z)
    df = pd.DataFrame(sols)
    i = int(df[['frequency']].idxmax())
    X = sols[i]['x']
    return X



def Subset_result(solution, numbers):  ## Divide the input numbers into 2 subsets
    S1, S2 = [], []                    ## based on best bitarray sample
    subsets = [S1, S2]

    for i in range(len(solution)):
        if solution[i] == 0:
            S1.append(numbers[i])
        elif solution[i] == 1:
            S2.append(numbers[i])
    
    Label_Assignment(subsets)
    print("\nWow! Even and Odd numbers are separated")



def Label_Assignment(subsets):     ## Assigns label to groups as Evens and Odds
    P = None                       
    for i in range(len(subsets)):
        if len(subsets[i]) != 0:  # finding the non-null group
            P = i

    if subsets[P][0] %2 == 0: ### ONLY CHECKS THE FIRST ELEMENT
        even = subsets[P]
        odd = subsets[1-P]
    else:
        odd = subsets[P]
        even = subsets[1-P]
    print(' Even numbers:',even)
    print('  Odd numbers:',odd)



def QUBO(D):
    k = N.shape[0]
    m = BinaryMatrix(k)
    for i in range(k):
        for j in range(i,k):
            m[i,j] = (-1)**(1 + D[i] + D[j])
    return m


#########################################################################
choice = int(input("Do you want to choose random or custom input? If random press 0, if custom press 1\n\n" ))
if choice == 0:
    n = 10  # for simplicity and to avoid error
    N = np.random.randint(1,100,n) 
    print("{} random integers are:\n{}".format(n,N))
elif choice ==1:
    print("Input larger than 10 may introduce mis-classification")
    n = int(input("How many numbers do you want to input? "))
    M = []
    for i in range(n):
        r = int(input("Enter {}th integer: ".format(i+1)))
        M.append(r)
        N = np.array(M) 
    print("\nUser defined {} custom integers are:\n{}".format(n,N))





qubo = QUBO(N)
print("\n\n       Our QUBO for the problem is:\n\n",qubo.to_numpy())  # Prints QUBO matrix in Numpy array format

model = BinaryQuadraticModel(qubo)  # Converting Binary matrix into amplify native Binary Quadratic Model


################################### client setup   ############################

client = FixstarsClient()
client.token = "----- TOKEN---------"
client.parameters.timeout = 1000
# client.parameters.outputs.duplicate = True  
client.parameters.outputs.num_outputs = 0

################## Solution #########################


solver = Solver(client)
result = solver.solve(model)
for solution in result:
    print(f"\n\nvalues = {list(solution.values.values())} energy = {solution.energy} frequency = {solution.frequency}")

best_solution = Best_solution(result)
print('\n\nInput numbers:',N)
Subset_result(best_solution,N)