'''
Generate All Possible Matches
Your mission is to list all possible match flows with scores up to k (k is a parameter).
Meaning the first to reach k points wins the match.

For examples, Table Tennis (Ping-pong) is a game with 11-point system (up to 11).

In this kata your mission is to write a function getting a positive integer value k>0 and it should return
all possible match flows up to score of k. Players' scores can increment by one only.

NOTE: Pay attention to the order of possible matches.

Order of matches
If we take k=2 example we can draw the following tree describing all possible matches:

                 0:0
             /        \
            /          \
           /            \
          /              \
        1:0               0:1
        / \               / \
       /   \             /   \
    2:0     1:1         1:1   0:2
            / \         / \
           /   \       /   \
          2:1   1:2   2:1  1:2
The required order of matches is actually all the paths from root to leaves, from left to right.
In every node we go to the left option and then the right one.

Example 1
There are 2 possible matches up to score of k=1:

[['0:0', '1:0'], ['0:0', '0:1']]

Example 2
There are 6 possible matches up to score of k=2:

[['0:0', '1:0', '2:0'], ['0:0', '1:0', '1:1', '2:1'], ['0:0', '1:0', '1:1', '1:2'], ['0:0', '0:1', '1:1', '2:1'],
['0:0', '0:1', '1:1', '1:2'], ['0:0', '0:1', '0:2']]

Constraints
Your solution will be tested for 1<=k<=10
'''


def generate_all_possible_matches(k, root=''):
    tree[root] = f'{k}:{k}'



print(generate_all_possible_matches(1))
