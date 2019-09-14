
""" 
Exercise 1.

A company is organized hierarchically in departments. 
Each department has one person in charge and exactly two subdepartments, or else is a single person.
We have a structure that records the productivity of every person in it, as a numerical value. 
We are asked to tell the (sub)department that has highest average productivity.

For example, the structure could look like this in Ptyhon:

[3, [-1, [4, [2], [0]], [1]],[5, [2], [-4]]]

This represents 9 employees. 
The top employee has productivity 3 and heads two subdepartments. 
The first of them is headed by an employee with productivity -1, etc. 
At the bottom there there are 5 departments formed by single employees with no further responsibilities, with productivities 2, 0, 1, 2, and -4.

The average productivity of the last employee is -4. 
The department to which s/he belongs is [5,[2],[-4]], with an average productivity of (5+2-4)/3 = 1. 
The whole organization has average productivity (3-1+4+2+...-4)/9=12/9.

Write a function (and subfunctions, if needed) that gets a structure like this one and returns the substructure corresponding to the department with the highest average productivity. 
Make it efficient meaning avoid redundant computations.

You can assume that the structure given is syntactically correct and encodes a set of hierarchical departments as described above - you don't need to check correctness.

Python is prefered but if you use another language, say how the structure is represented. 
Give also the tests cases that you use.

"""



"""
This is an aplication for The Maximum Average Subtree of a Binary Tree
The time and space complexity is O(N). 
The N is the number of the nodes in the tree, number of employees in the organization.
"""




"""
Output on my machine:

$ python3 Exercise1.py 


test_failure
F

test_left_branch
.

test_provided_case
.

test_right_branch
.

test_simple_negative
.

test_simple_positive
.

test_tie_depatments
.

test_tie_zeros_depatments
.
======================================================================
FAIL: test_failure (__main__.TestSum)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "Exercise1.py", line 196, in test_failure
    self.assertEqual (get_dep_hap(emp_prod), (22.0, [[4, [2], [0]]]), "FAIL")
AssertionError: Tuples differ: (2.0, [[4, [2], [0]]]) != (22.0, [[4, [2], [0]]])

First differing element 0:
2.0
22.0

- (2.0, [[4, [2], [0]]])
+ (22.0, [[4, [2], [0]]])
?  +
 : FAIL

----------------------------------------------------------------------
Ran 8 tests in 0.002s

FAILED (failures=1)
"""

import unittest


def get_dep_hap_helper(emp_prod, cnt, max_avg, res):
    """
    helper function
    """

    #base case of recursion
    if (len(emp_prod) == 1):
        #return leaf node and count 1
        return emp_prod[0],1

    #call it recursively on left subtree    
    left_dep, cnt[0] = get_dep_hap_helper(emp_prod[1], list(cnt), max_avg, res)
    #call it recursively on righh subtree
    right_dep, cnt[1] = get_dep_hap_helper(emp_prod[2], list(cnt), max_avg, res)
    #computer the sum
    sum_dep = left_dep + right_dep + emp_prod[0]
    #compute the number of nodes
    cnt = cnt[0] + cnt[1] + 1 
    #update the highest average
    if(sum_dep/cnt > max_avg[0]):
        max_avg[0] = sum_dep/cnt
        res.clear()
        res.append(emp_prod)
    #check for tie deparments    
    elif(sum_dep/cnt == max_avg[0]) :
        res.append(emp_prod)

    #return sum and nr of nodes    
    return sum_dep,cnt




def get_dep_hap(emp_prod):
    """
    function to get the department with the highest average productivity
    input: the employee productivity list
    output: highest average of department(s) and the substructure(s) coreponding to this average

    """

    #number of nodes in left subtree
    left_cnt = 0
    #number of nodes in right subtree
    right_cnt = 0
    #highest average
    max_avg = [float('-inf')]
    #substrucure(s) with highest average
    res = []
    #I am coming from C++ and I want to pass by refrence, I am not sure this is the best way to do it
    cnt = [left_cnt, right_cnt]
    #helper function called recursively to get the results using a Depth First Search Algorithm
    get_dep_hap_helper(emp_prod, cnt, max_avg, res) 
    #return highest average and the list with department havig that average
    return max_avg[0], res





class TestSum(unittest.TestCase):
    """
    Testing the function using unittest
    Test1: test_provided_case
    Test2: test_simple_negative
    Test3: test_simple_positive
    Test4: test_tie_depatments
    Test5: test_tie_zeros_depatments
    Test6: test_left_branch
    Test7: test_right_branch
    Test8: test_failure
    """
    
    def test_provided_case(self):
        emp_prod = [3, [-1, [4, [2], [0]], [1]],[5, [2], [-4]]]
        print('\n')
        print(self._testMethodName)
        self.assertEqual(get_dep_hap(emp_prod), (2.0, [[4, [2], [0]]]), "FAIL")

    def test_simple_negative(self):
        emp_prod = [-1, [-2], [-3]]
        print('\n')
        print(self._testMethodName)
        self.assertEqual(get_dep_hap(emp_prod), (-2.0, [[-1, [-2], [-3]]]), "FAIL")    
    
    def test_simple_positive(self):
        emp_prod = [1, [2], [3]]
        print('\n')
        print(self._testMethodName)
        self.assertEqual (get_dep_hap(emp_prod), (2.0, [[1, [2], [3]]]), "FAIL")

    def test_tie_depatments(self):
        emp_prod = [-11, [3, [-1, [4, [2], [0]], [1]],[5, [2], [-4]]], [3, [-1, [4, [2], [0]], [1]],[5, [2], [-4]]]]
        print('\n')
        print(self._testMethodName)
        self.assertEqual (get_dep_hap(emp_prod), (2.0, [[4, [2], [0]], [4, [2], [0]]]), "FAIL")

    def test_tie_zeros_depatments(self):
        emp_prod = [0, [0, [0, [0], [0]], [0]],[0, [0], [0]]]
        print('\n')
        print(self._testMethodName)
        self.assertEqual (get_dep_hap(emp_prod), (0.0,[[0, [0], [0]],[0, [0, [0], [0]], [0]],[0, [0], [0]],[0, [0, [0, [0], [0]], [0]], [0, [0], [0]]]]), "FAIL")
      
    def test_left_branch(self):
        emp_prod = [3, [100, [4, [2], [0]], [1]],[5, [2], [-4]]]
        print('\n')
        print(self._testMethodName)
        self.assertEqual (get_dep_hap(emp_prod), (21.4, [[100, [4, [2], [0]], [1]]]), "FAIL")

    def test_right_branch(self):
        emp_prod = [3, [5, [2], [-4]], [100, [4, [2], [0]], [1]]]
        print('\n')
        print(self._testMethodName)
        self.assertEqual (get_dep_hap(emp_prod), (21.4, [[100, [4, [2], [0]], [1]]]), "FAIL")    

    def test_failure(self):
        emp_prod = [3, [-1, [4, [2], [0]], [1]],[5, [2], [-4]]]
        print('\n')
        print(self._testMethodName)
        self.assertEqual (get_dep_hap(emp_prod), (22.0, [[4, [2], [0]]]), "FAIL") 

if __name__ == "__main__":
    unittest.main()



