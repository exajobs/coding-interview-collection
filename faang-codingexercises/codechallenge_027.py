'''
Date: 01/09/2019

Problem descriptions:
====================
This problem was asked by Facebook.

Given an unordered list of flights taken by someone, each represented as 
(origin, destination) pairs, and a starting airport, compute the person's itinerary. 
If no such itinerary exists, return null. If there are multiple possible itineraries, 
return the lexicographically smallest one. All flights must be used in the itinerary.

For example, given the list of flights [('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')] 
and starting airport 'YUL', you should return the list ['YUL', 'YYZ', 'SFO', 'HKO', 'ORD'].

Given the list of flights [('SFO', 'COM'), ('COM', 'YYZ')] and starting airport 'COM', 
you should return null.

Given the list of flights [('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')] and starting airport 'A', 
you should return the list ['A', 'B', 'C', 'A', 'C'] even though ['A', 'C', 'A', 'B', 'C'] is 
also a valid itinerary. However, the first one is lexicographically smaller.


Algorithm:
=========
Input: An array of tuples, and a string (representing available flights & starting airport)
Output: An array of tuples (representing connecting flights)
Psuedo code:
1.  Check for valid input
2.  Initialize an empty itinerary list. Assign departure points from the flight list
4.  Determine the destination point of the given starting airport.  
	4.1 If there are multiple detinations, then we create a secondary itineraries.  Copy current itinerary to them.  Append start,end points to the itnerary list(s).
	4.2 Else, just append start,end points to the primary itinerary list.
5.  determine the arrival airport from the above destination, next start point equals to arrival airport.
6.  keep doing step4,5 until the available flight list is exhausted
7.  return the itineray list


After thoughts:
==============
The solution above is not exacly what the task asks for.
Need to write lexicoItinerary().
'''
import itertools

def lexicoItinerary(FLIGHTS, START):
	DEP=[(i,d[0]) for i,d in enumerate(iter(FLIGHTS))]
	iterFts = itertools.combinations_with_replacement(DEP, 2)
	templist = []
	for flight in iterFts:
		templist.append(i)
	DEST = [list(i)[0] for i in DEP if list(i)[1] == START]

	# figure out the shortest path of connecting flights
	shortest_itin = []
	max_len = int(2**32)
	for itin in templist:
		if len(itin) < max_len:
			shortest_itin = itin
			max_len = len(shortest_itin)

	return shortest_itin

#
# (Real world application)
# return list of connecting flights
#
def getItin(FLIGHTS, START):
	ITINs = [] # intend to be multi-dimensional array for multiple destination
	try:
		for idx,val in enumerate(FLIGHTS):
			DEP=[(i,d[0]) for i,d in enumerate(iter(FLIGHTS))]
			destinations = [list(i)[0] for i in DEP if list(i)[1] == START]

			# treat it as if we might find more than one destinations
			for i in destinations:
				templist = []
				if len(ITINs) > 0:
					templist = ITINs[0]
				templist.append(FLIGHTS[int(i)])
				ITINs.append(templist) 
				START = list(templist[-1])[1]
				destinations = [list(i)[0] for i in DEP if list(i)[1] == START]

			#print(', '.join(str(i) for i in ITINs[0]))
	except IndexError:
		pass
	
	# figure out the shortest path of connecting flights
	shortest_itin = []
	max_len = int(2**32)
	for itin in ITINs:
		if len(itin) < max_len:
			shortest_itin = itin
			max_len = len(shortest_itin)

	return shortest_itin


def test_getItin():
	flights=[('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')]
	start='YUL'
	assert getItin(flights, start) == [('YUL', 'YYZ'), ('YYZ', 'SFO'), ('SFO', 'HKO'), ('HKO', 'ORD')]
 
	start='ORD'
	assert getItin(flights, start) == []

def main():
	flights=[('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')]
	start='A'
	itinerary = getItin(flights, start)
	if len(itinerary) > 0:
		print("Test1:\nGiven the starting airport is {} and available flights [{}]\nPossible itinerary is [{}]".format(start, ', '.join(str(f) for f in flights), start+'->'+'->'.join(str(i[1]) for i in itinerary)))
		print()

	
	flights=[('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')]
	start='YUL'
	itinerary = getItin(flights, start)
	if len(itinerary) > 0:
		print("Test2:\nGiven the starting airport is {} and available flights [{}]\nPossible itinerary is [{}]".format(start, ', '.join(str(f) for f in flights), start+'->'+ '->'.join(str(i[1]) for i in itinerary)))
		print()

	start='SFO'
	itinerary = getItin(flights, start)
	if len(itinerary) > 0:
		print("Test3:\nGiven the starting airport is {} and available flights [{}]\nPossible itinerary is [{}]".format(start, ', '.join(str(f) for f in flights), start+'->'+'->'.join(str(i[1]) for i in itinerary)))
		print()

	start='ORD'
	itinerary = getItin(flights, start)
	if len(itinerary) > 0:
		print("Test4:\nGiven the starting airport is {} and available flights [{}]\nPossible itinerary is [{}]".format(start, ', '.join(str(f) for f in flights), start+'->'+'->'.join(str(i[1]) for i in itinerary)))
		print()
	else:
		print("Test3:\nGiven the starting airport is {} and available flights [{}]\nPossible itinerary is [{}]".format(start, ', '.join(str(f) for f in flights), 'None'))


if __name__ == '__main__':
	main()


'''
Run-time output:
===============
(DailyCodingChallenge-wC3ocw3s) markn@raspberrypi3:~/devel/py-src/DailyCodingChallenge $ python codechallenge_027.py
Test1:
Given the starting airport is A and available flights [('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')]
Possible itinerary is [A->B->C->A->B->C->A]

Test2:
Given the starting airport is YUL and available flights [('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')]
Possible itinerary is [YUL->YYZ->SFO->HKO->ORD]

Test3:
Given the starting airport is SFO and available flights [('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')]
Possible itinerary is [SFO->HKO->ORD]

Test3:
Given the starting airport is ORD and available flights [('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')]
Possible itinerary is [None]
(DailyCodingChallenge-wC3ocw3s) markn@raspberrypi3:~/devel/py-src/DailyCodingChallenge $ pytest codechallenge_027.py
===================================== test session starts ======================================
platform linux2 -- Python 2.7.13, pytest-3.6.3, py-1.5.4, pluggy-0.6.0
rootdir: /home/markn/devel/py-src/DailyCodingChallenge, inifile:
collected 1 item

codechallenge_027.py .                                                                   [100%]

=================================== 1 passed in 0.08 seconds ===================================
'''
