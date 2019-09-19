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

1. __Class Combiner__ <br /> 
this class is used as a blue print to create new objects for each argument provided.

|   Combiner    | 
| ------------- |
| - path_to_file : str <br />+ first_file_opened : bool <br />  -------------------------|
| + get_file_name() : str <br />+ print_to_stdout : void|

- _path_to_file_ <br />
stores path to the file for the object.

- _first_file_opened_ <br />
boolean variable; True if file is being opened for the first time.

- _get_file_name()_ <br />
public method that return the filename(only the file's basename, not the entire path)

- _print_to_stdout()_ <br/>
public method that outputs the csv file into the stdout. </br>
checks to see if the file is being opened for the first time (in which case outputs the header, otherwise, outputs to stdout ignoring the header). <br />
error handling is also implemented (prints error and continues with the rest of the args, can also completely exit the program instead of continuing to run by removing comment on line no. 68 of csv-combiner.py).

2. __main__ <br /> 
checks if the arguments is provided properly (prints the error on the stdout). <br />
if arguments are provided properly, it iterates through the list of arguments and creates object for each args. </br>
uses the constuctor __Combiner(_path_to_file_)__ to create a new object of Combiner type. <br />
calls __print_to_stdout()__ method on each object



  


  


