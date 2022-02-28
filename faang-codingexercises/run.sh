#!/bin/bash
#
# This script executes the python program and pipes the output to the end of the python code
#
#
if [ $# -lt 1 ]; then 
    echo "Usage:" 
    echo "	bash run.sh codechallenge_###.py"
    echo "	Example:" 
    echo "		bash run.sh codechallenge_015.py"
    exit 0
else
    python $1 > output.txt
    echo -e "'''\nRun-time output:\n===============\n$(cat output.txt)" > input.txt; echo -e "'''\n" >> input.txt
    rm -f output.txt
    cat input.txt >> $1
    rm -f input.txt
fi
