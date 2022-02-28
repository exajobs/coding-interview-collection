#!/bin/bash
##------------------------------------------------##
# Author: Mark Nguyen
##------------------------------------------------##
# This script takes a list of date-time values and
# convert each to epoc equivalent.  It then 
# prints out the longest length of time between
# any two date-time in the list.
##------------------------------------------------##
# File name: datetime_epoc.sh
# 
# Usage: $0 [infile]
#   infile should contain a list of date-time values 
#
##------------------------------------------------##



#-----------------------function show_usage---------------------#
# This shows the program usage when invalid input args occured. #
#---------------------------------------------------------------#
function show_usage()
{
cat << EOF

This script takes an input text file containing date-time values

Usage: $0 [in_file]

Options:
   -h      Show this message.
    e.g.   $0 ./datetime.dat


EOF
}
export -f show_usage


#-----------------------function find_longest_time---------------------#
# Note:
# bash --date and -d option expects the date in US or ISO8601 format, 
# i.e. mm/dd/yyyy or yyyy-mm-dd, not in UK, EU, or any other format.
#----------------------------------------------------------------------#
function find_longest_time()
{
	local infile=$1
	if test -f $infile; then
		# read all line in file into an array
		IFS=$'\n' read -d '' -r -a std_dt < $infile

		# Explicitly report array content.
		let idx=0
		let MAX=0
		let MIN=$((X=2**32))

		if [[ "${#std_dt[@]}" -gt 0 ]]; then
			#-- process each line --#
			for line in "${std_dt[@]}" ; do
				# ignore comment line 
				[[ "$line" =~ ^#.*$ ]] && continue

				# convert to epoc value
				epoc_dt=$(date --date "${line}" +%s)

				# find max value
				if [ ${epoc_dt} -gt $MAX ] ; then
					MAX=${epoc_dt}
				fi

				# find min value
				if [ ${epoc_dt} -lt $MIN ] ; then
					MIN=${epoc_dt}
				fi
			done
			# calculate long length of time between for two set of date-time 
			DIFF=$(( $MAX - $MIN ))
			echo "The longest distance past (time length) is ${DIFF} seconds; starting from $(date -d @$MAX) and going back to $(date -d @$MIN)."
		fi
	else
		echo "Input not found"
	fi
}
export -f find_longest_time



#-- main program --#
# Checking input parameters 
if [ $# -lt 1 ]; then
    show_usage
    exit 1;
fi
find_longest_time $1
exit 0;



'
Run-time output:
===============
markn@raspberrypi3:~/devel/py-src/DailyCodingChallenge/bash_scripts $ bash datetime_epoc.sh ./datetime.dat
The longest distance past (time length) is 751565047 seconds; starting from Sat  1 Jan 21:51:09 PST 2022 and going back to Tue 10 Mar 05:47:02 PST 1998.

'
