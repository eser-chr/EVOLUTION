import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm
import pandas as pd
from plotter import plotter
import sys


STEPS = int(sys.argv[1])
BLOCKS = int(sys.argv[2]) 
PARENTS = 1000

def sum_birth_prob():
	s = 0
	for i in Be.catalog:
		s += i.prob_to_born
	return s

def sum_death_prob():
	s = 0
	for i in Be.catalog:
		s += i.prob_to_die
	return s

def show(step):
	x = [i.theta for i in Be.catalog]
	counts, bins = np.histogram(x, bins = 20)
	plt.stairs(counts,bins)
	plt.savefig(f'./{step}.png')
	plt.clf()

def writer(step):
	dic = {}
	dic['NUM'] = [len(Be.catalog)]
	dic['Birth_prob'] = [sum_birth_prob()]
	dic['Death_prob'] = [sum_death_prob()]
	data = pd.DataFrame(dic)
	h = 1 if step == 0 else 0
	data.to_csv('data.csv', mode = 'a', index = False, header = h)



class Be:
	catalog = []
	
	def __init__(self, theta, death=None):
		self.theta = theta
		self.prob_to_born = self.birth_prob_generator(self.theta)
		if death == None:
			self.prob_to_die = self.death_prob_generator()
		else:
			self.prob_to_die = death
		# self.prob_to_die = self.death_prob_generator()
		self.age = 0
		Be.catalog.append(self)	

	def death_prob_generator(self):
		x = len(self.catalog)
		if x==0:
			return 1
		else:
			return sum_birth_prob() / x

	def birth_prob_generator(self, val):  # Return value in range [0,1) SIgmoid function and proper trans
		out = self.o(self.theta)
		return 0.1 * np.exp(-out**2)

	def o(self, val):  # o inf range. 0 is ideal value and +- are equally disliked
		return val

	def create_baby(self):
		new_theta = self.theta + 0.1 * (np.random.random()-0.5)
		Be(new_theta)
		
	def try_birth(self):
		r = np.random.random()
		if r < self.prob_to_born:
			self.create_baby()	

	def try_death(self):
		r = np.random.random()
		if r < self.prob_to_die:
			self.__delete__()

	def __delete__(self):
		Be.catalog.remove(self)

	def __repr__(self):
		return str(self.theta)

	def step(self):		
		self.try_death()
		self.age +=1	
		self.try_birth()	

	def run(steps):
		for i in range(steps):
			for obj in Be.catalog:
				obj.step()








if __name__ == '__main__':

	for i in range(PARENTS):
		val = 2*(np.random.random() -0.5)
		Be(val, 0.05)

	
	for i in tqdm(range(BLOCKS)):
		show(i)
		writer(i)
		Be.run(STEPS//BLOCKS)


	


	
