'''
Date: 01/15/2019

Problem description:
====================
This problem was asked by Facebook.

Given a array of numbers representing the stock prices of a company in 
chronological order, write a function that calculates the maximum profit 
you could have made from buying and selling that stock once. You must 
buy before you can sell it.

For example, given [9, 11, 8, 5, 7, 10], you should return 5, since you 
could buy the stock at 5 dollars and sell it at 10 dollars.


Algorithm:
=========
Input: An array of integers
Output: An integer

Pseudo code:

1.  Check for valid input
2.  Create a generator that yield sublists containing no trailing accending numbers
3.  For each yielded sublist, find the min value and its index from the array.  This 
    will be the buy item.  Find the min value in this sublist.  It will be the sell item.
    Calulate the difference and append it to the list of profits
4.  Return the max value n the profit list as the maximum gain in investing base on the price list.  


'''


#
# generator that yields sublist with possible investment gain
#
def subpricelist(price_list=[]):
	start, end = 0, len(price_list)
	j = end
	sublist = []
	while start < end - 1:
		temp = price_list[start:j]

		j-=1
		# eliminate lists with decending numbers, they indicate market down turn
		if all(temp[i] < temp[i+1] for i in range(len(temp)-1)):
			yield temp

		if j < start + 2:
			start+=1
			j = end

#
# Calculate the difference between the max and min values in the sublist
# Return the max value in the list of differences
#
def profit(price_list=[]):
	if len(price_list) == 0:
		return 0

	sublist = subpricelist(price_list)
	all_profits = []
	for PList in sublist:
		# buy low
		buyAtIdx = price_list.index(min(PList))
		buyPrice = price_list[buyAtIdx]

		#new_price_list = PList[buyAtIdx:]

		# sell high
		sellPrice = max(PList)
		sellAtIdx = price_list.index(sellPrice)

		#profit
		gain = sellPrice - buyPrice
		all_profits.append(gain)

	# verbish
	if len(all_profits) > 0:
		print("For maximum profit we buy at {} and sell at {} for the profit of {}.".format(buyPrice, sellPrice, max(all_profits)))
	else:
		print("We bought at {}, We haven't sold it yet.  Price is still equaled or lower than the invested capital.".format(buyPrice, profit=0))
	
	# return profit
	return int(max(all_profits))

#
# unittest
#	
def test_profit():
	A = [19, 157, 163, 99, 200, 215, 189, 201, 205, 199]
	assert profit(A) > 0
	assert profit(A) == 144

#
# client program 
#
def main():
	stock_prices = [9, 11, 8, 5, 7, 10]
	print("Test1:\nGiven progressing stock prices {}".format('->'.join(str(i) for i in stock_prices)))
	profit(stock_prices)

	stock_prices = [157 , 160, 99, 88, 77, 66, 66, 66]
	print("Test2:\nGiven progressing stock prices {}".format('->'.join(str(i) for i in stock_prices)))
	profit(stock_prices)

if __name__ == '__main__':
	main()

'''
Run-time output:
===============
(DailyCodingChallenge-wC3ocw3s) markn@raspberrypi3:~/devel/py-src/DailyCodingChallenge $ python codechallenge_033.py
Test1:
Given progressing stock prices 9->11->8->5->7->10
For maximum profit we buy at 7 and sell at 10 for the profit of 5.
Test2:
Given progressing stock prices 157->160->99->88->77->66->66->66
For maximum profit we buy at 157 and sell at 160 for the profit of 3.
(DailyCodingChallenge-wC3ocw3s) markn@raspberrypi3:~/devel/py-src/DailyCodingChallenge $ pytest codechallenge_033.py
=================================== test session starts ====================================
platform linux2 -- Python 2.7.13, pytest-3.6.3, py-1.5.4, pluggy-0.6.0
rootdir: /home/markn/devel/py-src/DailyCodingChallenge, inifile:
collected 1 item

codechallenge_033.py .                                                               [100%]

================================= 1 passed in 0.07 seconds =================================

'''
