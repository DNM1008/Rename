# Rename
Simple rename programs with options that lacks in Windows Powertoys PowerRename

Special thanks to @limited-1 for his help with the code!

limited-1 can be found at https://github.com/limited-1


You will need to install Python 3 for this. Some, if not all Linux distros, came with Python, on Windows, visit https://www.python.org/downloads/ for more information

Run the program, you will be asked the directory to the folders that contains files that needs renaming. Simply paste the directory in and hit "Enter"

The program will then ask you what do you want to do, and it expects you to enter a number from 0 to 8:

* 0 if you have done all you need to do and wish to continue to write the changes to the file names
* 1 if you want to replace a part of the name, in which the program treats each name as a string of character and replace what you want it to replace with what you tell it to
* 2 if you want to remove the first n characters of each name, the program will ask you to enter n as an interger
* 3 if you want to remove the last n characters of each name, the program will ask you to enter n as an interger
* 4 if you want to add a string (a series of characters) to the names at specific indice. You will need to tell it the index as an interger that's larger than 0 and less than the length of the shortest name (so that it would work on all files)
* 5 if you want to add a string (a series of characters) to the end of the names.
From 6 to 8 you can split the names into a list of strings, making rename a bit easier. You will be ask what are the strings in each name separeated by, then it will split the names into lists of strings.
* 6 if you want to remove the string at index n. You will need to give it an index that is an interger and is larger than 0 and less than the size of the smallest list (if the names of each of your files are separeated into differenct numbers of strings).
* 7 if you want to remove the first n strings. You will need to give it an index that is an interger and is larger than 0 and less than the size of the smallest list (if the names of each of your files are separeated into differenct numbers of strings).
* 8 if you want to remove the last n strings. You will need to give it an index that is an interger and is larger than 0 and less than the size of the smallest list (if the names of each of your files are separeated into differenct numbers of strings).
* 9 if you want to remove the string at index n from the end. You will need to give it an index that is an interger and is larger than 0 and less than the size of the smallest list (if the names of each of your files are separeated into differenct numbers of strings).
* 10 if you want add a string at the index n from the end. You will need to give it an index that is an interger and is larger than 0 and less than the size of the smallest list (if the names of each of your files are separeated into differenct numbers of strings).
    
    
    9 and 10 are added in v0.1.1
