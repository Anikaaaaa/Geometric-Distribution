import matplotlib.pyplot as plt
import math
import pandas as pd
import random
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
# !pip install joypy
# Import Data
def Generating_p_of_x(n,p):
P_of_X = []
X = []
i = 0
array_of_random_nums = [0] * n
# Codes for Theoritical Geometric Probability Distribution
while i <= n:
P_of_X.append(float(p * ((1 - p) ** i)))
X.append(i)
print(P_of_X[i])
i += 1
# Plotting Graph for Theoritical Geometric Probability Distribution
x = pd.np.arange(n + 1)
y1 = pd.np.array(P_of_X)
plt.bar(x + 0, y1, color='#d40b1e', width=0.4, label="Theoritical")
plt.xlabel('x')
plt.ylabel('p(x)')
plt.legend(loc="upper left")
plt.title("Theoritical Geometric Probability Distribution\n p=0.5")
plt.show()
#Codes for Practial Geometric Probability Distribution
#Taking random value within range
for i in range(n):
rand_num = random.random()
variable = 0
while rand_num < P_of_X[variable] and variable < n:
variable = variable + 1
array_of_random_nums[i] = variable
#Caculating frequency
frequency = {}
for num in array_of_random_nums:
if (num in frequency):
frequency[num] += 1
else:
frequency[num] = 1
#Frequency in sorted order
frequency1 = sorted(frequency.items())
xs = []
ps = []
variable = 0
#Calculating frequency/N
for item in frequency1:
xs.insert(variable, item[0] + 1)
ps.insert(variable, item[1] / n)
variable = variable + 1
# Plotting
y1 = pd.np.array(ps)
plt.bar(xs, y1, color='#800080', width=0.4, label="Practical")
plt.xlabel('x')
plt.ylabel('p(x)')
plt.legend(loc="upper right")
plt.title("Practical Geometric Probability Distribution\n p=0.5")
plt.show()
def main():
# Taking the how many number of random variable have to generate as input (N)
n = int(input("Enter Total Numbers to Generate"))
# Taking the parameter as input (P)
p = float(input("Enter value of P"))
#Theoritical and Practical Geometric Probability Distribution
Generating_p_of_x(n,p)
if __name__ == "__main__":
main()
