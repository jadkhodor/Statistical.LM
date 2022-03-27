import time

import numpy as np

import matplotlib.pyplot as plt

import statistics as st

from sklearn import linear_model

start_time = time.time()


quantities = list(range(10,200,10))
iterations = 10000
def sim_r_sq(n):
    x = np.random.normal(size=n)
    y = np.random.normal(size=n)+x+1
    lm = linear_model.LinearRegression()
    lm.fit(X=x.reshape(-1,1),y=y)
    return lm.score(X=x.reshape(-1,1),y=y)
r_sq_mean = []
r_sq_q95 = []
r_sq_q5 = []


for size in quantities:
    print(size)
    result = []
    for i in range(iterations):
        result.append(sim_r_sq(size))
    r_sq_mean.append(st.mean(result))
    r_sq_q95.append(np.quantile(result,0.95))
    r_sq_q5.append(np.quantile(result,0.05))

execution_time = time.time()-start_time



print("Execution time: "+str(execution_time))
plt.scatter(quantities, r_sq_mean)
plt.plot(quantities,r_sq_q5)
plt.plot(quantities,r_sq_q95)
plt.ylim(min(r_sq_q5),max(r_sq_q95))
plt.xlabel("Sample Size")
plt.ylabel("$R^2$")
plt.show()