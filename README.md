# EVOLUTION
Simple program that illustrates how evolution theory works.

HOW TO USE
Create a folder and copy paste all files.
From terminal navigate to that file and make the bash script executable 


(chmod +x run.sh)

Then run the executable, where you can specify number of Steps and number of blocks. e.g


./run.sh {step_value} {block_value}



MAIN DESCRIPTION
The program as writtern assignes a value 'theta' between -1 and 1 to each object. This value maps to a probability that the object will create a new object at each step (here via a normal distribution).

As soon as a new object it is created its theta value is his parents plus/minus a random deviation. At the same time based on the number of objects a death_probability is assigned to it. 

At each step each object via two random numbers gives birth to a new object, dies or remain as it is. (This part of the algorithm can be changed so that it uses only one random number.)

At the end of each block of steps the algorithm produces a histogramm depicting the distributiion of the theta value across the distribution. Moreover, at the end a csv file is created where the number of object, the birth rate (i.e the sum of the birth prob across the population) and the death rate are reported.

At the end of simulation the shell script calls the plotter which plots the csv file's quantities.

I would be happy to hear any corrections suggestions!
