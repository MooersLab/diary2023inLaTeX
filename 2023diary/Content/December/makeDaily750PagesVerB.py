#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division, print_function
import sys, os
Usage=""" 
 ./makeDaily750Pages.py year month startCalDay endCalDay
example:
./makeDaily750Pages.py 2017 'November' 6 30
"""

"""
Purpose: write out the plain text files for the month.
There is one file per day.

Read in from command line the following parameters:

year # as four digit integer
month # as string
startCalDay # as integer 
endCalDay

Thus script initially will write the files for one month or part of a month.

Write out plain tex files for each day with the following first line:
%!TEX root = ../../main.tex

%awk '/^\%TODO/' 22October2017.tex > 22October2017TODOawk.tex
%sed -n '/^\%TODO/p' 22October2017.tex > 22October2017TODOsed.tex
%grep '^\%TODO' 22October2017.tex > 22October2017TODOgrep.tex

Blaine Mooers

5 November 2017

Updated to write boilerplate to a comment environment at the bottom of the page.
This spares the need to use percent signs to comment out the boilerplate.

6 July 2019
"""

def makeDailyPages():
    year=sys.argv[1]
    syear=str(year)
    print(syear)

    month=sys.argv[2]
    smonth=str(month) 
    print(month)

    startCalDay=sys.argv[3]
    sstartCalDay=str(startCalDay)
    istartCalDay=int(startCalDay)
    print(sstartCalDay)

    endCalDay=sys.argv[4]
    sendCalDay=str(endCalDay)
    iendCalDay=int(endCalDay)  
    print(sendCalDay)

    print("Usage: ./makeDaily750Pages.py year month startday endday")
    print("Example: ./makeDaily750Pages.py 2017 'November' 6 30")
    inumAtJobs = ((iendCalDay - istartCalDay) + 1)
    print(str(inumAtJobs))
    writeJobs = [x for x in range(inumAtJobs)]
    day = istartCalDay
    sday =str(day)
    for job in writeJobs:
        sday = str(day)
        newfile = sday + month + syear + ".tex"
        h = open(newfile, 'w')
        h.write(r'%!TEX root = ../../main.tex' + '\n')
        h.write('\n')
        day = day + 1
        h.close()

if __name__ == '__main__':
    makeDailyPages()

"""
Enhancements could include making folders for each month
and writing the files to each folder.

Alternately, a bash script can be used to run this 
script to generate the files for a year.

#!/usr/bin/bash
./makeDaily750Pages.py 2017 'November' 6 30
./makeDaily750Pages.py 2017 'December' 1 31

"""
