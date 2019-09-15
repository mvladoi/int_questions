
"""
Exercise 2. 
A group of friends want to play a football match. 
They know how good everybody is, and each friend has a numerical score. 
Split the group in two teams that are as balanced as possible based on the sum of their scores, to make for a fair game.

The goal is to minimize the absolute difference of the total score of the two teams. 
You can try first a version where the two teams do not need to have the same number of players, 
then improve it to another where both teams have the same size.

Implement this as a function

team1, team2 = player_split(ids, scores)

where:
ids is the list of player id’s (for example [“Alice”,”Bob”,”Coral,”David”]
Scores is the list of scores (same length as ids) (for example [4.5, 6.1, 5.2, 4.7])
Team1 is the list of ids assigned to team1
Team2 is the list of ids assigned to team2
Create tests for these functions and script to run them. Preferably in Python but not compulsory.
"""



"""
This is an aplication of partitioning  a set into two subsets such that the difference of subset sums is minimum
I assume: 
-list of players >= 2
-scores have only one floating point precission
-there are no players with the same name 
-there are no players with the same score
"""



"""
The teams do not have the same number of players.
The time and space complexity is O(N * sum). 
N is the number of the players and sum is the sum of their scores.

"""



"""
Output on my machine:

$ python3 Exercise2a.py

test_fail_case_diff
F

test_fail_case_name
F

test_fail_is_a_bug
F

test_greater_than_10
.

test_provided_case
.

test_provided_case_negative
.

test_running_time
.

test_splitting_teams
.
======================================================================
FAIL: test_fail_case_diff (__main__.TestSum)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "Exercise2.py", line 200, in test_fail_case_diff
    self.assertEqual(player_split(ids, scores) , (['Bob:6.1', 'Alice:4.5'], ['David:4.7', 'Coral:5.2'], 0.9), "FAIL")
AssertionError: Tuples differ: (['John:100.0'], ['David:4.7', 'Coral:5.2', 'Bob:6.1', 'Alice:4.5'], 79.5) != (['Bob:6.1', 'Alice:4.5'], ['David:4.7', 'Coral:5.2'], 0.9)

First differing element 0:
['John:100.0']
['Bob:6.1', 'Alice:4.5']

- (['John:100.0'], ['David:4.7', 'Coral:5.2', 'Bob:6.1', 'Alice:4.5'], 79.5)
+ (['Bob:6.1', 'Alice:4.5'], ['David:4.7', 'Coral:5.2'], 0.9) : FAIL

======================================================================
FAIL: test_fail_case_name (__main__.TestSum)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "Exercise2.py", line 214, in test_fail_case_name
    self.assertEqual(player_split(ids, scores) , (['David:4.7', 'Alice:4.5'], ['Bob:6.1', 'Coral:5.2'], 0.9), "FAIL")
AssertionError: Tuples differ: (['Bob:6.1', 'Alice:4.5'], ['David:4.7', 'Coral:5.2'], 0.7) != (['David:4.7', 'Alice:4.5'], ['Bob:6.1', 'Coral:5.2'], 0.9)

First differing element 0:
['Bob:6.1', 'Alice:4.5']
['David:4.7', 'Alice:4.5']

- (['Bob:6.1', 'Alice:4.5'], ['David:4.7', 'Coral:5.2'], 0.7)
?    ^^^ ^ ^                   ^^^^^ ^ ^                   ^

+ (['David:4.7', 'Alice:4.5'], ['Bob:6.1', 'Coral:5.2'], 0.9)
?    ^^^^^ ^ ^                   ^^^ ^ ^                   ^
 : FAIL

======================================================================
FAIL: test_fail_is_a_bug (__main__.TestSum)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "Exercise2.py", line 207, in test_fail_is_a_bug
    self.assertNotEqual(player_split(ids, scores) , ([], [], 0.0), "FAIL")
AssertionError: ([], [], 0.0) == ([], [], 0.0) : FAIL

----------------------------------------------------------------------
Ran 8 tests in 0.021s

"""
import unittest



def player_split_get_teams(scores, n, t1_score, t2_score, min_dif, t1_players, t2_players):

    """
    Function to get the teams scores and min difference using Dynamic Programming
    """
    

    #base case 
    if (n < 0):
        return abs(t1_score - t2_score), t1_players, t2_players
    
    #compute a unique key
    key = str(n) + '_' + str(t1_score)
    
    #teams to be returned
    t1 = str()
    t2 = str()
    min_diff = 0.0
    
    #check in the dictionary for the key in order to avoid same computations
    if key not in min_dif:
        
        #choose the player
        take, a, b = player_split_get_teams(scores, n - 1, t1_score + scores[n], t2_score, min_dif, t1_players + "," + str(scores[n]), t2_players)
        #do not choose the player
        not_take, not_a, not_b = player_split_get_teams(scores, n - 1, t1_score, t2_score + scores[n],min_dif, t1_players, t2_players + "," + str(scores[n]))
        
        if take < not_take:
            
            min_dif[key] = take
            t1 = a
            t2 = b
            
        else:
            min_dif[key] = not_take
            t1 = not_a
            t2 = not_b
        
        min_diff = round(min_dif[key], 1)
    #return min difference and scores of the teams
    return min_diff, t1, t2



def player_split_test(ids, scores, debug):

    """
    Function to split the ids in two teams with min absolute difference
    If debug true returns two list containing "player_id:score" and min absolute difference
    If debug false returns two list contining "player_id"
    """
    
    # number of players - 1
    n = len(scores) - 1
    #dict to accumulate the min difference
    min_dif = dict()
    #accumulate the scores of the players, coma separated
    t1_players = ""
    t2_players = ""
    
    #get the min differece and the teams (scores of the teams , coma separated)
    min_team_dif, team1, team2 = player_split_get_teams(scores, n, 0, 0, min_dif, t1_players, t2_players)
    
    
    #map scores to ids, if same key has more values then can be more solutions
    #I assume each player has different score
    scores_to_ids = dict()
    for score, name  in zip (scores, ids):
        if score in scores_to_ids:
            scores_to_ids[score].append(name)
        else:
            scores_to_ids[score] = [name]
            
     
    team1_ids = list()
    team2_ids = list()
    
    #build the teams ids sets by parsing the team scores strings previous created 
    for score in team1.split(',')[1:]:
        if debug:
            team1_ids.append(scores_to_ids[float(score)][0] + ':' + score)
        else:    
            team1_ids.append(scores_to_ids[float(score)][0])    
        
    for score in team2.split(',')[1:]:
        if debug:
            team2_ids.append(scores_to_ids[float(score)][0] + ':' + score)
        else:
            team2_ids.append(scores_to_ids[float(score)][0])
    
        
    if debug:    
        return team1_ids, team2_ids, min_team_dif
    return team1_ids, team2_ids
 
 

class TestSum(unittest.TestCase):
    """
    Testing the function using unittest
    Test1: test_provided_case
    Test2: test_provided_case_negative
    Test3: test_splitting_teams
    Test4: test_running_time
    Test5: test_greater_than_10
    Test6: test_fail_case_diff
    Test7: test_fail_is_a_bug
    Test8: test_fail_case_name
    """
    
    def test_provided_case(self):
        scores =[4.5, 6.1, 5.2, 4.7]
        ids = ['Alice','Bob','Coral', 'David']
        print('\n')
        print(self._testMethodName)
        self.assertEqual(player_split(ids, scores) , (['Bob:6.1', 'Alice:4.5'], ['David:4.7', 'Coral:5.2'], 0.7), "FAIL")

    def test_provided_case_negative(self):
        scores =[-4.5, -6.1, -5.2, -4.7]
        ids = ['Alice','Bob','Coral', 'David']
        print('\n')
        print(self._testMethodName)
        self.assertEqual(player_split(ids, scores) , (['Bob:-6.1', 'Alice:-4.5'], ['David:-4.7', 'Coral:-5.2'], 0.7), "FAIL")

    def test_splitting_teams(self):
        scores =[100.0 ,4.5, 6.1, 5.2, 4.7]
        ids = ['John','Alice','Bob','Coral', 'David']
        print('\n')
        print(self._testMethodName)
        self.assertEqual(player_split(ids, scores) , (['John:100.0'], ['David:4.7', 'Coral:5.2', 'Bob:6.1', 'Alice:4.5'], 79.5), "FAIL")

    def test_running_time(self):
        scores =[10.0, 202.2, 10.1, 99.9, 1.1, 2.9, 3.8, 22.9, 13.3, 44.7]
        ids = ['Jimy','Lola','Bob','Coral','Tom', 'Sam', 'Geo', 'Marvin', 'Sue', 'Kyle']
        print('\n')
        print(self._testMethodName)
        self.assertEqual(player_split(ids, scores) , (['Sam:2.9', 'Lola:202.2'],['Kyle:44.7','Sue:13.3','Marvin:22.9','Geo:3.8','Tom:1.1','Coral:99.9','Bob:10.1','Jimy:10.0'],0.7), "FAIL")

    def test_greater_than_10(self):
        scores =[10.0, 202.2, 10.1, 99.9, 1.1, 2.9, 3.8, 22.9, 13.3, 44.7,0.1]
        ids = ['Jimy','Lola','Bob','Coral','Tom', 'Sam', 'Geo', 'Marvin', 'Sue', 'Kyle','Momi']
        print('\n')
        print(self._testMethodName)
        self.assertEqual(player_split(ids, scores) , (['Kyle:44.7','Sue:13.3','Marvin:22.9','Geo:3.8','Tom:1.1','Coral:99.9','Bob:10.1','Jimy:10.0'],['Momi:0.1', 'Sam:2.9', 'Lola:202.2'],0.6), "FAIL")

    def test_fail_case_diff(self):
        scores =[100.0 ,4.5, 6.1, 5.2, 4.7]
        ids = ['John','Alice','Bob','Coral', 'David']
        print('\n')
        print(self._testMethodName)
        self.assertEqual(player_split(ids, scores) , (['Bob:6.1', 'Alice:4.5'], ['David:4.7', 'Coral:5.2'], 0.9), "FAIL")

    def test_fail_is_a_bug(self):
        scores =[1.0,1.1,1.2,1.3,1.4,1.5,1.6,1.7,1.8,1.9,2.0,2.1,2.2]
        ids = ['A','B','C','D','E','F','G','H','I','J','K','L','M']
        print('\n')
        print(self._testMethodName)
        self.assertNotEqual(player_split(ids, scores) , ([], [], 0.0), "FAIL")

    def test_fail_case_name(self):
        scores =[4.5, 6.1, 5.2, 4.7]
        ids = ['Alice','Bob','Coral', 'David']
        print('\n')
        print(self._testMethodName)
        self.assertEqual(player_split(ids, scores) , (['David:4.7', 'Alice:4.5'], ['Bob:6.1', 'Coral:5.2'], 0.9), "FAIL")



def player_split(ids, scores):
    debug = True
    return player_split_test(ids, scores, debug)



    
if __name__ == "__main__":
    unittest.main()    