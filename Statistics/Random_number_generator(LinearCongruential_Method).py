class LinearCongruentialGenerator:
  def __init__(self, seed=20200420162000): 
    self.a=11282011637
    self.c=1140671485
    self.m=2**21
    global X_i
    X_i=seed

  def random(self):
    global X_i
    X_i=(self.a*X_i+self.c)%self.m
    return X_i
    
lcg=LinearCongruentialGenerator()
for _ in range(10):
  print(lcg.random())