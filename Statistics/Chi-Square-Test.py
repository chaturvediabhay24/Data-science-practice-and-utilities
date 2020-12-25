from scipy import stats
from scipy.stats.distributions import chi2
expected = [20,20,30,40,60,30]
observed = [30,14,34,45,57,20]
import numpy as np
def chi_square_test(expected, observed):
  X2=0
  for i in range(len(expected)):
    X2+=((observed[i]-expected[i])**2/expected[i])

  p=chi2.sf(X2,len(observed)-1)
  
  print("H0 : distribution is correct")
  print("H1 : distribution is not correct\n")

  alpha = 0.05
  print("P-value is {} and alpha is {}\n".format(p, alpha))

  if p > alpha:
    print('reject H0: distribution is not a correct fit')
  else:
    print('fail to reject H0: distribution is correct fit')

chi_square_test(np.array(expected), np.array(observed))