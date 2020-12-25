import scipy.stats
import math 
import statistics 
import random.random as rand

l=[]
for _ in range(10):
  l.append(rand())

def Test_Random_Numbers(l):
  l_median=statistics.median(l)
  runs=0
  n1=0
  n2=0
  for ind, val in enumerate(l):
    if (val>=l_median and l[ind-1]<l_median) or (val<l_median and l[ind-1]>=l_median):
      runs+=1

    if (val>=l_median):
      n1+=1
      
    else: 
      n2 += 1
  exp_runs = ((2*n1*n2)/(n1+n2))+1
  std = math.sqrt((2*n1*n2*(2*n1*n2-n1-n2))/(((n1+n2)**2)*(n1+n2-1))) 

  result =(runs-exp_runs)/std 
  print("Z-Statistics : ", abs(result))



  alpha = 0.05
  #find Z critical value
  z_critical=scipy.stats.norm.ppf(abs(alpha))
  # z_critical


  print("H0 : distribution is random")
  print("H1 : distribution is not random\n")

  print("z-critical is {} with confidence {}\n".format(z_critical, alpha))

  if z_critical > alpha:
    print('reject H0: distribution is not random')
  else:
    print('fail to reject H0: distribution is random')


Test_Random_Numbers(l)