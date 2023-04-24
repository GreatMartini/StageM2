#A revisar

import numpy as np
import matplotlib.pyplot as plt

first_data_mom = np.loadtxt("/Users/bach/Desktop/Trabajos/Stage_M2/Codes/Data/scalar1/mom0.rl")
first_data_ham = np.loadtxt("/Users/bach/Desktop/Trabajos/Stage_M2/Codes/Data/scalar1/ham0.rl")

second_data_mom = np.loadtxt("/Users/bach/Desktop/Trabajos/Stage_M2/Codes/Data/scalar2/mom0.rl")
second_data_ham = np.loadtxt("/Users/bach/Desktop/Trabajos/Stage_M2/Codes/Data/scalar2/ham0.rl")

third_data_mom = np.loadtxt("/Users/bach/Desktop/Trabajos/Stage_M2/Codes/Data/scalar3/mom0.rl")
third_data_ham = np.loadtxt("/Users/bach/Desktop/Trabajos/Stage_M2/Codes/Data/scalar3/ham0.rl")

fourth_data_mom = np.loadtxt("/Users/bach/Desktop/Trabajos/Stage_M2/Codes/Data/scalar4/mom0.rl")
fourth_data_ham = np.loadtxt("/Users/bach/Desktop/Trabajos/Stage_M2/Codes/Data/scalar4/ham0.rl")


ham1 = np.reshape(first_data_ham[:,1],(51,int(np.size(first_data_ham[:,1])/51)))
ham2 = np.reshape(second_data_ham[:,1],(51,int(np.size(second_data_ham[:,1])/51)))
#ham3 = np.reshape(third_data_ham[:,1],(51,int(np.size(third_data_ham[:,1])/51)))
#ham4 = np.reshape(fourth_data_ham[:,1],(51,int(np.size(fourth_data_ham[:,1])/51)))
#ratio = ham2/ham1
#first_data_ham = np.reshape(first_data_ham,(51,503,2))
#print(r1)
plt.plot(ham1[25,3:503], label = "dr=0.1, t=50")
plt.plot(ham2[25,3:503], label = "dr=0.05, t=50")
plt.xlabel("r")
plt.ylabel("Hamiltonian Constrain")
#plt.plot(ham3[50,3:503], label = "dr=0.025")
#plt.plot(ham4[50,3:503], label = "dr=0.0125")
#plt.xlabel("Timestep")
#plt.ylabel("Hamiltonian Constraint")
#plt.legend()

#plt.scatter(t1,ham1,s=1)
#plt.xlim(0,max(t2))
#plt.savefig("Convergence.png")
plt.legend()
plt.show()
