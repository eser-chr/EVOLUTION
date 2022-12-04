import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def moving_average(a, n=3) :
    ret = np.cumsum(a, dtype=float)
    ret[n:] = ret[n:] - ret[:-n]
    return ret[n - 1:] / n

def plotter():
	data = pd.read_csv('data.csv')

	num = data['NUM'].values
	death = data['Death_prob'].values
	birth = data['Birth_prob'].values
	# plt.plot(num)
	plt.plot(moving_average(np.diff(num),n=10))
	plt.plot(100 *(birth-death))
	plt.plot(np.zeros(len(num)), 'k--')
	plt.show()

if __name__ == '__main__':
	plotter()