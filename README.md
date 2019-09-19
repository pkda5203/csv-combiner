# csv-combiner
Implementation of csv-combiner (PMG Developer coding challenge)

Implemented using python 3.7

### Run as follows using CLI:
  python csv-combiner.py [path_to_file1] [path_to_file2] ...
  
EXAMPLE: <br />
python csv-combiner.py ./testSamples/accessories.csv ./testSamples/clothing.csv ./testSamples/household_cleaners.csv

Implementation details:
------
The solution is implemented using OOP approach

1. _Class Combiner_ <br /> 
this class is used as a blue print to create new objects for each argument provided.

|   Combiner    | 
| ------------- |
| - path_to_file : str <br />+ first_file_opened : bool <br />  -------------------------|
| + get_file_name() : str <br />+ print_to_stdout : void|

2. _main_ <br /> 
checks if the arguments is provided properly (prints the error on the stdout) <br />
if arguments are provided properly, it iterates through the list of arguments and creates object for each args </br>
calls __print_to_stdout()__ method on each object



  


  


