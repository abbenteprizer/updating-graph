# Automatically updating matplotlib script for python 
This program continuously reads from a file which contains raw data. Raw data can be continuously appended to the file from another program. The raw data needs to filtered in order to extract important data that one wants to display. This has to be implemented manually. 

This is not a program that works for a general case, but rather, it is a program that can easily be modified to filter and display application specific data. The program is not designed to work unless you provide data filtering and raw input data. 

## Use following arguments 
-l, --input_list\
-f, --input_file\
-p, --print_mode\
-w, --windowsize

```
python3 updating_graph.py -f 'data.csv' -p 0 -w 10
```

## Printmodes
print_mode = 0,	graph continuously updates values using a window \
print_mode = 1,	graph continuously updates and shows all values \
print_mode = 2,	graph shows all values, never updates 

## Examples
