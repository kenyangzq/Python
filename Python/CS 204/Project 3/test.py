"""
 File name: test.py
 Author:
 VUnetid: 
 Email: 
 Class:
 Date: 
 Honor statement:
 Assignment Number:
 Description: Unit tests of breast_cancer.py
     Use this file to test each of your functions individually.
"""

from breast_cancer import *
import numpy


def file_io_test():
    # YOUR CODE HERE
    print ("KK")




def gauss_test():
    # YOUR CODE HERE
    a = get_patient_data("patients.txt")
    b = get_diagnoses("results.txt")
    tmp1 = (my_solve(a, b))
    tmp2 = (numpy.linalg.lstsq(a, b)[0])
    print (tmp1)
    print (tmp2)




def transpose_test():
    # YOUR CODE HERE
    a = [[1, 2, 3], [2, 3, 4]]
    b = numpy.array(a)



# The correctness of your my_solve function is part of the main analysis

if __name__ == "__main__":
    file_io_test()
    gauss_test()
    transpose_test()
