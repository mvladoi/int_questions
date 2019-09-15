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
This is an aplication of Equal partitioning with minimum difference in sum
I assume: 
-if number of elements are odd difference in partition size can be at most 1
-list of players >= 1
-scores have only one floating point precission
-there are no players with the same name 
-there are no players with the same score
"""



"""
Steps of the algorithm:
-sort the input array scores
-if number of elements in less than 4 then create partitions accordingly for each cases
 when we have 1 element or 2 element or 3 element in the array.
-else take 2 pair each time and put into two partition such that it minimizes the sum diff.

Running Time :
O(N^2) time and O(N) space implementation where N is the size of scores input array
"""



"""
Output on my machine:
$ python Exercise2b.py 


test_fail_case_diff
F

test_fail_case_name
F

test_fail_is_a_bug2a
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
  File "Exercise2b.py", line 341, in test_fail_case_diff
    self.assertEqual(player_split(ids, scores) , (['John:4.5', 'David:100.0'], ['Alice:4.7', 'Bob:5.2', 'Coral:6.1'], 89.5), "FAIL")
AssertionError: Tuples differ: (['John:4.5', 'David:100.0'], ['Alice:4.7', 'Bob:5.2', 'Coral:6.1'], 88.5) != (['John:4.5', 'David:100.0'], ['Alice:4.7', 'Bob:5.2', 'Coral:6.1'], 89.5)

First differing element 2:
88.5
89.5

- (['John:4.5', 'David:100.0'], ['Alice:4.7', 'Bob:5.2', 'Coral:6.1'], 88.5)
?                                                                       ^

+ (['John:4.5', 'David:100.0'], ['Alice:4.7', 'Bob:5.2', 'Coral:6.1'], 89.5)
?                                                                       ^
 : FAIL

======================================================================
FAIL: test_fail_case_name (__main__.TestSum)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "Exercise2b.py", line 348, in test_fail_case_name
    self.assertEqual(player_split(ids, scores) , (['Bob:4.7', 'David:6.1'], ['Alice:4.5', 'Coral:5.2'], 0.7), "FAIL")
AssertionError: Tuples differ: (['Alice:4.5', 'David:6.1'], ['Bob:4.7', 'Coral:5.2'], 0.7) != (['Bob:4.7', 'David:6.1'], ['Alice:4.5', 'Coral:5.2'], 0.7)

First differing element 0:
['Alice:4.5', 'David:6.1']
['Bob:4.7', 'David:6.1']

- (['Alice:4.5', 'David:6.1'], ['Bob:4.7', 'Coral:5.2'], 0.7)
+ (['Bob:4.7', 'David:6.1'], ['Alice:4.5', 'Coral:5.2'], 0.7) : FAIL

----------------------------------------------------------------------
Ran 7 tests in 0.002s

FAILED (failures=2)

"""



import unittest
from treeset import TreeSet


def player_split_get_teams_scores(A):
    #sort the array input 
    A.sort()  
    #initialize the variables
    partition1 = list()
    partition2 = list()
    i = 0
    j = len(A)-1
    part1Sum = 0
    part2Sum = 0
    diffSum = 0 
    unused = TreeSet([])
    
    for i in range (len(A)):
        unused.add(i)
        
    while len(unused) > 0:
        i = unused[0]
        j = unused[-1]
        diffSum = part1Sum-part2Sum

        #special case handling when the array is not multiple of 4 then 
        if len(unused) < 4:
            #remaining item placed smaller partition
            if len(unused) == 1:
                if diffSum > 0:
                    partition2.append(A[i])
                    part2Sum += A[i]
                else:
                    partition1.append(A[i])
                    part1Sum += A[i]
            #max in smaller and min in larger partition
            elif len(unused) == 2:
                maxx = max(A[i], A[j])
                minn = min(A[i], A[j])
                if diffSum > 0:
                    partition2.append(maxx)
                    partition1.append(minn)
                    part2Sum += maxx
                    part1Sum += minn

                else:
                    partition1.append(maxx)
                    partition2.append(minn)
                    part1Sum += maxx
                    part2Sum += minn

            #min, middle in smaller particion and max in larger particion 
            elif len(unused) == 3:
                unused.remove(i)
                unused.remove(j)
                middle = unused[0]
                if diffSum > 0:
                    if A[i]+A[middle] > A[j]:
                        partition2.append(A[i])
                        partition2.append(A[middle])
                        partition1.append(A[j])
                        part2Sum += A[i]+A[middle]
                        part1Sum += A[j]
                    else:
                        partition2.append(A[j])
                        partition1.append(A[i])
                        partition1.append(A[middle])
                        part1Sum += A[i]+A[middle]
                        part2Sum += A[j]
                else:
                    if A[i]+A[middle] > A[j]:
                        partition1.append(A[i])
                        partition1.append(A[middle])
                        partition2.append(A[j])
                        part1Sum += A[i]+A[middle]
                        part2Sum += A[j]
                    else:
                        partition1.append(A[j])
                        partition2.append(A[i])
                        partition2.append(A[middle])
                        part2Sum += A[i]+A[middle]
                        part1Sum += A[j]


            diffSum = part1Sum - part2Sum
            break

        #take the largest and the smallest element to create a pair
        pairSum = A[i]+A[j]
    
        if diffSum > 0:
            particion = 2
        else:
            particion = 1
        
        if particion == 1 :
            partition1.append(A[i])
            partition1.append(A[j])
            part1Sum += pairSum
        else:
            partition2.append(A[i])
            partition2.append(A[j])
            part2Sum += pairSum


        diffSum = part1Sum - part2Sum
        #used pair (i, j)
        unused.remove(i)
        unused.remove(j)
        #j last element
        j = unused[-1]

        buddyIndex = unused[0]
        minPairSumDiff = float('-inf')
        #find such buddy A[k], i<=k<j such that value of ((A[j]+A[k])-pairSum) is minimized
        for k in range(buddyIndex, j, 1):
            if k not in unused:
                continue

            compPairSum = A[j]+A[k]
            pairSumDiff = abs(pairSum-compPairSum)

            if pairSumDiff < minPairSumDiff:
                minPairSumDiff = pairSumDiff
                buddyIndex = k


        #add pair (j,buddyIndex) to the other partition
        if j != buddyIndex:
            pairSum = A[j]+A[buddyIndex]
            if particion == 2:
                partition1.append(A[j])
                partition1.append(A[buddyIndex])
                part1Sum += pairSum
            else:
                partition2.append(A[j])
                partition2.append(A[buddyIndex])
                part2Sum += pairSum
            
            #used pair (j, buddyIndex)
            unused.remove(j)
            unused.remove(buddyIndex)

    #optimize by swapping a larger elements in large partition with an small element in smaller partition
    if diffSum != 0:
        partition1.sort()
        partition2.sort()

        diffSum = part1Sum-part2Sum
    
        if diffSum > 0:
            largerPartition = partition1
            smallerPartition = partition2
        else:
            largerPartition = partition2
            smallerPartition = partition1
        
    
        prevDiff = abs(diffSum)
        largePartitonSwapCandidate = -1
        smallPartitonSwapCandidate = -1

        #swap largest element from large partition and smallest from the smaller partition so that sum difference is minimized
        for i in range(len(smallerPartition)):
            for j in range(len(largerPartition)-1, -1, -1):
                largerVal = largerPartition[j]
                smallerVal = smallerPartition[i]

                if largerVal <= smallerVal:
                    continue

                diff = abs(prevDiff - 2* abs(largerVal - smallerVal))
                if diff == 0:
                    largerPartition[j] =  smallerVal
                    smallerPartition[i] =  largerVal
                    return [largerPartition, smallerPartition]

                elif diff < prevDiff:
                    prevDiff = diff
                    largePartitonSwapCandidate = j
                    smallPartitonSwapCandidate = i



        #if found such a pair then swap it.
        if largePartitonSwapCandidate >=0 and smallPartitonSwapCandidate >=0:
            largerVal = largerPartition[largePartitonSwapCandidate]
            smallerVal = smallerPartition[smallPartitonSwapCandidate]
            largerPartition[largePartitonSwapCandidate] =  smallerVal
            smallerPartition[smallPartitonSwapCandidate] =  largerVal
            return [largerPartition, smallerPartition]

                   
    return [partition1, partition2]               


  

def player_split_help(ids, scores, debug):
       
    #get the teams scores partitioned 
    teams = player_split_get_teams_scores(scores)
    
    
    #map scores to ids, if same key has more values then can be more solutions
    #I assume each player has different score
    scores_to_ids = dict()
    for score, name  in zip (scores, ids):
        scores_to_ids[score] = name
            
    team1_ids = list()
    team2_ids = list()
    
    #build the teams ids sets by parsing the team scores list
    team1_sum = 0
    team2_sum = 0
    
    for score in teams[0]:
        if debug:
            team1_ids.append(scores_to_ids[score] + ':' + str(score))
            team1_sum += score
        else:
            team1_ids.append(scores_to_ids[score])
        
    for score in teams[1]:
        if debug:
            team2_ids.append(scores_to_ids[score] + ':' + str(score))
            team2_sum += score
        else:
            team2_ids.append(scores_to_ids[score])
        
    if debug:
        return team1_ids, team2_ids, round(abs(team1_sum - team2_sum), 1)
    
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
        self.assertEqual(player_split(ids, scores) , (['Alice:4.5', 'David:6.1'], ['Bob:4.7', 'Coral:5.2'], 0.7), "FAIL")

    def test_provided_case_negative(self):
        scores =[-4.5, -6.1, -5.2, -4.7]
        ids = ['Alice','Bob','Coral', 'David']
        print('\n')
        print(self._testMethodName)
        self.assertEqual(player_split(ids, scores) , (['Alice:-6.1', 'David:-4.5'], ['Bob:-5.2', 'Coral:-4.7'], 0.7), "FAIL")

    def test_splitting_teams(self):
        scores =[100.0 ,4.5, 6.1, 5.2, 4.7]
        ids = ['John','Alice','Bob','Coral', 'David']
        print('\n')
        print(self._testMethodName)
        self.assertEqual(player_split(ids, scores) , (['John:4.5', 'David:100.0'], ['Alice:4.7', 'Bob:5.2', 'Coral:6.1'], 88.5), "FAIL")

    def test_running_time(self):
        scores =[10.0, 202.2, 10.1, 99.9, 1.1, 2.9, 3.8, 22.9, 13.3, 44.7, 22.8, 90.9, 96.1, 121.0, 123.5]
        ids = ['Jimy','Lola','Bob','Coral','Tom', 'Sam', 'Geo', 'Marvin', 'Sue', 'Kyle', 'Luli', 'Ama', 'Hans', 'Papi', 'Kiki']
        print('\n')
        print(self._testMethodName)
        self.assertEqual(player_split(ids, scores) , (['Jimy:1.1','Coral:10.0','Tom:10.1','Sue:44.7','Kyle:90.9','Ama:99.9','Kiki:202.2'],['Lola:2.9','Bob:3.8','Sam:13.3','Geo:22.8','Marvin:22.9','Luli:96.1','Hans:121.0','Papi:123.5'],52.6), "FAIL")

    def test_fail_is_a_bug2a(self):
        scores =[1.0,1.1,1.2,1.3,1.4,1.5,1.6,1.7,1.8,1.9,2.0,2.1,2.2]
        ids = ['A','B','C','D','E','F','G','H','I','J','K','L','M']
        print('\n')
        print(self._testMethodName)
        self.assertEqual(player_split(ids, scores) , (['A:1.0', 'B:1.1', 'E:1.4', 'G:1.6', 'I:1.8', 'K:2.0', 'M:2.2'],['C:1.2', 'D:1.3', 'F:1.5', 'H:1.7', 'J:1.9', 'L:2.1'],1.4), "FAIL")
    
    def test_fail_case_diff(self):
        scores =[100.0 ,4.5, 6.1, 5.2, 4.7]
        ids = ['John','Alice','Bob','Coral', 'David']
        print('\n')
        print(self._testMethodName)
        self.assertEqual(player_split(ids, scores) , (['John:4.5', 'David:100.0'], ['Alice:4.7', 'Bob:5.2', 'Coral:6.1'], 89.5), "FAIL")

    def test_fail_case_name(self):
        scores =[4.5, 6.1, 5.2, 4.7]
        ids = ['Alice','Bob','Coral', 'David']
        print('\n')
        print(self._testMethodName)
        self.assertEqual(player_split(ids, scores) , (['Bob:4.7', 'David:6.1'], ['Alice:4.5', 'Coral:5.2'], 0.7), "FAIL")



def player_split(ids, scores):
    debug = True
    return player_split_help(ids, scores, debug)



if __name__ == "__main__":
    unittest.main()      