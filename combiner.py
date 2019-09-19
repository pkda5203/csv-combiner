'''
 PMG Developer interview Assignment
 Implementation of csv-combiner using python 3.7


 @author Prabesh Khadka

 '''

# !usr/bin/env python3

import csv
import sys
import os.path as path


class Combiner:
    # static bool variable true for file being opened for first time
    first_file_opened = True

    def __init__(self, path_to_file):
        self.__path_to_file = path.abspath(path_to_file)

    def get_file_name(self):
        return path.basename(self.__path_to_file)

    def print_to_stdout(self):
        # read the file
        try:
            with open(self.__path_to_file, 'r', encoding='utf-8') as file:
                reader = csv.reader(file)
                stdout_writer = csv.writer(sys.stdout, doublequote=False, escapechar='\\', quoting=csv.QUOTE_ALL)

                # if this the first ever file being read
                if Combiner.first_file_opened == True:
                    row = 0
                    # go through each line including the header line
                    for rows in reader:
                        if row == 0:
                            rows_to_write = rows
                            # add an extra column for the header
                            rows_to_write.append('filename')
                            stdout_writer.writerow(rows_to_write)
                            row = row + 1
                        else:
                            rows_to_write = rows
                            rows_to_write.append(self.get_file_name())
                            stdout_writer.writerow(rows_to_write)
                    Combiner.first_file_opened = False

                # if the header has been already copied
                else:
                    row = 0
                    for rows in reader:
                        if row == 0:
                            # skip the first line
                            row = row + 1
                        # starts with the second line
                        else:
                            rows_to_write = rows
                            rows_to_write.append(self.get_file_name())
                            stdout_writer.writerow(rows_to_write)

        # if file cant be read
        except IOError:
            # print the error message to the stdout
            print('Error! The file "' + self.get_file_name() + '" could not be opened for reading, -, - ')

            # sys.exit() #uncomment this line to exit if error happened instead of continuing with rest of the file.


def main():
    # checks if the argument in valid, exits program if invalid
    if len(sys.argv) == 1:
        print("input argument required (csv-combine.py [file 2] [file 2] [file 3] ...)")
        sys.exit()

    for i in sys.argv[1:]:
        # create individual objects for each given argument and print to std
        Combiner(i).print_to_stdout()


if __name__ == '__main__':
    main()
