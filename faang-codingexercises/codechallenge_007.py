'''
Date: 12/19/2018

Problem description:
====================
A builder is looking to build a row of N houses with K different colors. 
His goal is to minimize total cost while making sure that no two neighboring 
houses have the same color. 

Given an NxK matrix where the nth row and kth column represents the cost to 
build the nth house with kth color, find the minimum cost which achieves this goal

====== !!! This is not my code !!! =======
90% OF THIS CODE BELONGS TO YOUTUBE AUTHOR: 'Happy Chuck Programming' 

Building a cost tree is a very nice solution.  I keep this code for reference.
'''

import random, math
class Node:
    global cost_fn
 
    def __init__(self, \
            num_homes=1, \
            num_colors=1, \
            index=0, \
            prev_color=0, \
            total_cost_so_far=0, \
            debug_list_colors_homes_so_far=[]):
        self.m_children_nodes={}
        self.m_num_homes = num_homes
        self.m_num_colors = num_colors
        self.m_curr_index = index
        self.m_prev_color = prev_color
        self.m_color = 0
        self.m_total_cost_so_far = total_cost_so_far
        self.m_cost = 0
        self.m_debug_list_colors_homes_so_far = debug_list_colors_homes_so_far
        
    def build_cost_tree(self):
        if self.m_curr_index == self.m_num_homes:
            return

        if self.m_curr_index == 0:
            # first house has 3 ways to pain
            for j in range(self.m_num_colors):
                self.m_color = j
                self.m_cost = cost_fn[self.m_curr_index][self.m_color]
                self.m_children_nodes[self.m_color] = Node(self.m_num_homes, \
                        self.m_num_colors, \
                        self.m_curr_index+1, \
                        self.m_color, \
                        self.m_total_cost_so_far + self.m_cost, \
                        self.m_debug_list_colors_homes_so_far + [self.m_color])

        else:
            # subsequent houses, two colors remained
            for q in range(self.m_num_colors):
                if q == self.m_prev_color:
                    pass
                else:
                    self.m_color = q
                    self.m_cost = cost_fn[self.m_curr_index][self.m_color]
                    self.m_children_nodes[self.m_color] = Node(self.m_num_homes, \
                          self.m_num_colors, \
                          self.m_curr_index+1, \
                          self.m_color, \
                          self.m_total_cost_so_far + self.m_cost, \
                          self.m_debug_list_colors_homes_so_far + [self.m_color])

        # build the cost tree:
        for key in self.m_children_nodes:
            self.m_children_nodes[key].build_cost_tree()



    '''count ways to pain houses'''
    def print_cost_homes(self, count=0):
        global colors_of_homes_and_total_cost
        if self:
            if self.m_curr_index == self.m_num_homes:
                print("colors: ", self.m_debug_list_colors_homes_so_far, \
                        "total cost: ", self.m_total_cost_so_far)
                tempstr = "_".join([str(i) for i in self.m_debug_list_colors_homes_so_far])
                colors_of_homes_and_total_cost[tempstr] = self.m_total_cost_so_far
                return count+1
            else:
                for key in self.m_children_nodes:
                    count = self.m_children_nodes[key].print_cost_homes(count)
                return count




n=5 # number of houses
k=3 # number of colors available

# hash table for color values
switcher = {
    '0': "BambooGreen",
    '1': "LondonFog",
    '2': "ArizonaBrown",
    '3': "ChicpeaBlue",
    '4': "Turquoi",
    '5': "CaliforniaPoppy",
    '6': "HoneyBrown",
    '7': "CiscoMist",
}	


def print_cost_fn(m):
    for r in m:
        print(r)

'''
# generate a sample of cost matrix interpreted from the given statement.
cost_fn = [
        [3, 0, 3],  # i = 0 iterate over house number
        [8, 3, 0],  # i = 1
        [4, 5, 0],  # i = 2
        [3, 4, 4],  # i = 3
        [7, 8, 1]   # i = 4
        ]
'''
# generate a random matrix of cost
cost_fn = [[int(10*random.random()) for i in range(k)] for j in range(n)]

colors_of_homes_and_total_cost = {} # each entry is stringified colors of all homes and total cost

print_cost_fn(cost_fn)
root = Node(n, k)
root.build_cost_tree()
print("Number of ways of painting n=5 houses", root.print_cost_homes())

min_cost_colors = ''
min_cost = math.pow(2,30)
for mkey in colors_of_homes_and_total_cost:
    if colors_of_homes_and_total_cost[mkey] < min_cost:
        min_cost = colors_of_homes_and_total_cost[mkey]
        min_cost_colors = mkey

print('Min cost of {} is achieved by coloring houses this way {}'.format(min_cost, min_cost_colors))
print("Where,")
for color in min_cost_colors.split('_'):
    coulor = switcher.get(color)
    tmpstr = ';'.join(coulor)
    print("\tcolor code: {} color: {}".format(color, coulor))

'''
Run-time output:
===============

[1, 7, 8]
[1, 1, 3]
[2, 5, 0]
[2, 1, 4]
[5, 4, 1]
('colors: ', [0, 1, 0, 1, 0], 'total cost: ', 10)
('colors: ', [0, 1, 0, 1, 2], 'total cost: ', 6)
('colors: ', [0, 1, 0, 2, 0], 'total cost: ', 13)
('colors: ', [0, 1, 0, 2, 1], 'total cost: ', 12)
('colors: ', [0, 1, 2, 0, 1], 'total cost: ', 8)
('colors: ', [0, 1, 2, 0, 2], 'total cost: ', 5)
('colors: ', [0, 1, 2, 1, 0], 'total cost: ', 8)
('colors: ', [0, 1, 2, 1, 2], 'total cost: ', 4)
('colors: ', [0, 2, 0, 1, 0], 'total cost: ', 12)
('colors: ', [0, 2, 0, 1, 2], 'total cost: ', 8)
('colors: ', [0, 2, 0, 2, 0], 'total cost: ', 15)
('colors: ', [0, 2, 0, 2, 1], 'total cost: ', 14)
('colors: ', [0, 2, 1, 0, 1], 'total cost: ', 15)
('colors: ', [0, 2, 1, 0, 2], 'total cost: ', 12)
('colors: ', [0, 2, 1, 2, 0], 'total cost: ', 18)
('colors: ', [0, 2, 1, 2, 1], 'total cost: ', 17)
('colors: ', [1, 0, 1, 0, 1], 'total cost: ', 19)
('colors: ', [1, 0, 1, 0, 2], 'total cost: ', 16)
('colors: ', [1, 0, 1, 2, 0], 'total cost: ', 22)
('colors: ', [1, 0, 1, 2, 1], 'total cost: ', 21)
('colors: ', [1, 0, 2, 0, 1], 'total cost: ', 14)
('colors: ', [1, 0, 2, 0, 2], 'total cost: ', 11)
('colors: ', [1, 0, 2, 1, 0], 'total cost: ', 14)
('colors: ', [1, 0, 2, 1, 2], 'total cost: ', 10)
('colors: ', [1, 2, 0, 1, 0], 'total cost: ', 18)
('colors: ', [1, 2, 0, 1, 2], 'total cost: ', 14)
('colors: ', [1, 2, 0, 2, 0], 'total cost: ', 21)
('colors: ', [1, 2, 0, 2, 1], 'total cost: ', 20)
('colors: ', [1, 2, 1, 0, 1], 'total cost: ', 21)
('colors: ', [1, 2, 1, 0, 2], 'total cost: ', 18)
('colors: ', [1, 2, 1, 2, 0], 'total cost: ', 24)
('colors: ', [1, 2, 1, 2, 1], 'total cost: ', 23)
('colors: ', [2, 0, 1, 0, 1], 'total cost: ', 20)
('colors: ', [2, 0, 1, 0, 2], 'total cost: ', 17)
('colors: ', [2, 0, 1, 2, 0], 'total cost: ', 23)
('colors: ', [2, 0, 1, 2, 1], 'total cost: ', 22)
('colors: ', [2, 0, 2, 0, 1], 'total cost: ', 15)
('colors: ', [2, 0, 2, 0, 2], 'total cost: ', 12)
('colors: ', [2, 0, 2, 1, 0], 'total cost: ', 15)
('colors: ', [2, 0, 2, 1, 2], 'total cost: ', 11)
('colors: ', [2, 1, 0, 1, 0], 'total cost: ', 17)
('colors: ', [2, 1, 0, 1, 2], 'total cost: ', 13)
('colors: ', [2, 1, 0, 2, 0], 'total cost: ', 20)
('colors: ', [2, 1, 0, 2, 1], 'total cost: ', 19)
('colors: ', [2, 1, 2, 0, 1], 'total cost: ', 15)
('colors: ', [2, 1, 2, 0, 2], 'total cost: ', 12)
('colors: ', [2, 1, 2, 1, 0], 'total cost: ', 15)
('colors: ', [2, 1, 2, 1, 2], 'total cost: ', 11)
('Number of ways of painting n=5 houses', 48)
Min cost of 4 is achieved by coloring houses this way 0_1_2_1_2
Where,
        color code: 0 color: BambooGreen
        color code: 1 color: LondonFog
        color code: 2 color: ArizonaBrown
        color code: 1 color: LondonFog
        color code: 2 color: ArizonaBrown
'''
