import seaborn as sns
from scipy.stats import norm

data = norm.rvs(5,0.4,size=1000) 

sns.distplot(data)
plt.show()