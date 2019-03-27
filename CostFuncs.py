import numpy as np

#As an example, this uses the cost function f(x) = norm(x) = sqrt(x_1^2 + x_2^2 ...)
class BasicCostFunc:
    
    def __init__(self):
        self.num_f_calls = 0
    
    def f(self,x):
        self.num_f_calls+=1
        return np.linalg.norm(x)

class DerivCostFunc( BasicCostFunc ):
    def __init__(self):
        self.num_f_calls=0
        self.num_df_calls=0
        
    def df(self,x):
        self.num_df_calls += 1
        return x / np.linalg.norm(x)
    
class SecondOrderCostFunc( DerivCostFunc ):
    def __init__(self):
        self.num_f_calls=0
        self.num_df_calls=0
        self.num_d2f_calls=0

    def d2f(self,x):
        self.num_d2f_calls += 1
        size_x = x.size
        if size_x[0] == 1:
            N = size_x[1]
        else:
            N = size_x[0]
        going_out = np.empty([N,N])
        norm_x = np.linalg.norm(x)
        norm_x_cubed = norm_x**3
        for i in range(N):
            for j in range(N):
                if i==j:
                    going_out[i,j] = 1/norm_x
                else:
                    going_out[i,j] = 0
                going_out[i,j] -= x[i] * x[j] / norm_x_cubed
        return going_out
