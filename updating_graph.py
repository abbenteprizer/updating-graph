import csv
import argparse
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

'''
This programs reads messages from a file and displays filtered data in graph. 
Can automatically update graph depending on the graph-mode chosen as input
'''

### add argument to program ###
parser = argparse.ArgumentParser()
parser.add_argument("-f", "--input_file")
parser.add_argument("-p", "--print_mode")
parser.add_argument("-w", "--windowsize")
args = parser.parse_args()

### Initialize variables ###
# when print_mode is 0, graph continuously updates values using a windowsize of 30 
# when print_mode is 1, graph continuously updates and shows all values 
# when print_mode is 2, graph shows all values, never updates graph

### set input data ###
if int(args.file) > 0:
	input_file = int(args.input_file)
else:
	print("no input_file given, set file with -f flag, terminating")
	exit()

### set printing options ###
if int(args.print_mode) > 0:
	print_mode = int(args.print_mode)
else:
	print_mode = 0

if int(args.windowsize) > 0:
	windowsize = int(args.windowsize)
else:
	windowsize = 10

### matplotlib initialization ###
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

### Function info from file, filters the data and outputs a graph ###
def animate(i):
	### read file and initialize variables ###
	with open(input_file, 'r') as file:
	    lines = file.read().splitlines()

	### initialize variables ###


	### Filter the data ###

	# Example;
	# for index, line in enumerate(lines):
	# 	data = line.split(' ')
	# 	if data[0] == 'foo':
	# 		list1.append(data[2])
	# 	if data[0] == 'bar':
	# 		list2[total_pdr_counter] = [data[1],0]


	### store data you want to plot in variable print_list ###
	# print_list = 

	### set printing boundaries, and printouts ###
	print_length = len(print_list)

	x_lower = len(print_list) - windowsize
	x_higher = len(print_list) - 1
	y_lower = 0 # put something here
	y_higher = 100 # put something here

	x_label = 'Number of experiments'
	y_label = 'Times in ms'


	### print automatically with moving window ###
	if print_mode == 0:
		if len(print_list) > windowsize:
			x = range(print_length - windowsize, print_length)
			y = print_list[-windowsize:]
			ax1.clear()
			plt.axis([x_lower, x_higher, y_lower, y_higher])
			ax1.set_ylabel(x_label) 
			ax1.set_xlabel(y_label)
			ax1.plot(x, y, marker='o', color='blue')

			# for item in special_data: # print the vertical lines for special events
			# 	if item in x:
			# 		plt.vlines(item, ymin=y_lower, ymax=y_higher)
	
	### print everything automatically ###
	elif print_mode == 1:
		x = range(0,len(pdr_list))
		y = pdr_list
		ax1.clear()
		plt.axis([x_lower, x_higher, y_lower, y_higher])
		ax1.set_ylabel(x_label) 
		ax1.set_xlabel(y_label)
		ax1.plot(x, y, marker='o', color='blue', markersize=3)

		# for item in special_data: # print the vertical lines for special events
		# 	if item in x:
		# 		plt.vlines(item, ymin=y_lower, ymax=y_higher)
		

	### Print everything once ###
	else:
		x = range(0,len(pdr_list))
		y = pdr_list
		ax1.clear()
		plt.axis([x_lower, x_higher, y_lower, y_higher])
		ax1.set_ylabel(x_label) 
		ax1.set_xlabel(y_label)
		ax1.plot(x, y, marker='o', color='blue', markersize=3)

		# for item in special_data: # print the vertical lines for special events
		# 	if item in x:
		# 		plt.vlines(item, ymin=y_lower, ymax=y_higher)

### print the graph ###
if print_mode < 2:
	ani = animation.FuncAnimation(fig, animate, interval=1000)
else:
	animate(0)
plt.show()
