
from scipy.stats import kstest 
import random 
  
# N = int(input("Enter number of random numbers: ")) 
N = 5
actual = 21*np.random.normal(0, 0.5, 1000)+91


# print(actual) 
x = kstest(actual, "uniform")    
# print(x) 
result=x
print('Statistic: %.3f' % result.statistic)
p = 0
sl, cv = result.statistic, 0.05
print("pvalue : {}\ncritical value : {}".format(result.pvalue, cv))
if result.pvalue < cv:
  print('data looks normal (fail to reject H0)' )
else:
  print('data does not look normal (reject H0)')