# Automatically updating matplotlib script for python 
There are two ways of using this program:
1: Send the program the data you want to display (using the flag -p)
As it is now, filtering data to view is done inside 

## Uses following arguments 
-f, --input_file
-p, --print_mode
-w, --windowsize

'''
python3 updating_graph.py -f 'data.csv' -p 0 -w 10
'''

## Printmodes
print_mode = 0, graph continuously updates values using a window
print_mode = 1, graph continuously updates and shows all values 
print_mode = 2, graph shows all values, never updates 

## Examples