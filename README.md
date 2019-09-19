# csv-combiner
Implementation of csv-combiner (PMG Developer coding challenge)

Implemented using python 3.7

#### Run as follows using CLI:
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
public method that return the filename(only the file's basename, not the entire path).

- _print_to_stdout()_ <br/>
public method that outputs the csv file into the stdout. </br>
checks to see if the file is being opened for the first time (in which case outputs the header, otherwise, outputs to stdout ignoring the header). <br />
error handling is also implemented (prints error and continues with the rest of the args, can also completely exit the program instead of continuing to run by removing comment on line no. 68 of csv-combiner.py).

2. __main__ <br /> 
checks if the arguments is provided properly (prints the error on the stdout). <br />
if arguments are provided properly, it iterates through the list of arguments and creates object for each args. </br>
uses the constuctor __Combiner(_path_to_file_)__ to create a new object of Combiner type. <br />
calls __print_to_stdout()__ method on each object.


Unit tests:
------
#### Run the unittest as follows using CLI:
      python -m unittest test_csv-combiner.py
      

- _test_get_file_name_ <br />
tests that the method _get_file_name()_ returns appropriate filename (without the abs path) and that the return type is a string.

- _test_print_to_stdout_ <br />
tests that the static boolean variable _first_file_opened_ is true if no file was opened before for reading.

- _test_print_to_stdout1_ <br />
tests that the method _print_to_std()_ outputs appropriate error message if the exception occured while opening the file for reading.  

- _test_print_to_stdout2_ <br />
tests that the method _print_to_std()_ outputs the csv file (along with added 'filename' column) with the header when being opened for the first time.

- _test_print_to_stdout3_ <br />
tests that the method _print_to_std()_ outputs the csv file (along with added 'filename' column) without the header if the header has been copied from the previous csv file. <br />
it also tests that the static boolean variable _first_file_opened_ is no longer true since a file was already opened before for reading.

  


  


