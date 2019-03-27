import numpy as np

#As an example, this uses the cost function f(x) = norm(x) = sqrt(x_1^2 + x_2^2 ...)
class BasicCostFunc:
    
    def __init__(self):
        self.num_f_calls = 0
    
    def f(self,x):
        self.num_f_calls+=1
        raise NotImplementedError('You need to define a f method!')

class DerivCostFunc( BasicCostFunc ):
    def __init__(self):
        self.num_f_calls=0
        self.num_df_calls=0
        
    def df(self,x):
        self.num_df_calls += 1
        raise NotImplementedError('You need to define a df method!')
    
class SecondOrderCostFunc( DerivCostFunc ):
    def __init__(self):
        self.num_f_calls=0
        self.num_df_calls=0
        self.num_d2f_calls=0

    def d2f(self,x):
        self.num_d2f_calls += 1
        raise NotImplementedError('You need to define a d2f method!')
        