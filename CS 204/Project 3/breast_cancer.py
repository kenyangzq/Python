"""
 File name: breast_cancer.py
 Author:
 VUnetid: 
 Email: 
 Class:
 Date: 
 Honor statement:
 Assignment Number:
 Description: Given a set of training data, generates a
     prediction vector for breast cancer biopsies.
"""

import numpy
import timeit

"""
Be sure to read thoroughly the project specification as it
provides necessary information pertinent to the understanding
and implementation of these methods.

While Python allows for object oriented design, it is also a
very popular scripting language. This program will differ from 
your previous two in that it will not make use of the class structure.
"""


def get_patient_data(filename):
    """
    @param filename as string
    @return numpy array of data
    """

    # YOUR CODE HERE
    fin = open(filename,'r')
    numOfRow = 0
    b = []
    for row in fin:
        tmp1 = row.split(" ")
        a = [float(i) for i in tmp1]
        b = b + a
        numOfRow += 1
    result = numpy.array(b).reshape(numOfRow, 10)
    fin.close()
    return result


def get_diagnoses(filename):
    """
    @param filename as string
    @return numpy array of data
    """

    # YOUR CODE HERE
    fin = open(filename, 'r')
    result = [[int(row)] for row in fin]
    fin.close()
    return result


def transpose(matrix):
    """
    @param matrix - a numpy matrix
    @return transposed numpy matrix
    """
    
    # YOUR CODE HERE
    return numpy.transpose(matrix).copy()


def gauss(a, b):
    """
    Note: be sure to read the project specification for this function
    @param a as matrix (2D numpy array)
    @param b as column vector (2D numpy array)
    @return result of the gauss as a numpy array
    """
    
    # YOUR CODE HERE
    shape = list(a.shape)
    shape[-1] += 1
    aug = numpy.zeros(shape)
    aug[:, :-1] = a
    aug[:, -1:] = b
    for i in range(0, shape[0]):
        tmp = aug[i, :]
        pivot = tmp[i]
        aug[i, :] = [k/pivot if k!=0 else 0 for k in tmp]
        for j in range(0, shape[0]):
            if j != i:
                tmp1 = aug[j, :]
                scale = tmp1[i]
                tmp1[i:] = tmp1[i:] - scale*tmp[i:]
                aug[j, :] = tmp1
    return aug[:, -1:]


def my_solve(a, b):
    """
    @param a training data as matrix (2D numpy array)
    @param b classifications as column vector (2D numpy array with only 1 column)
    @return solution as numpy array
    """
    # YOUR CODE HERE
    trans = numpy.transpose(a)
    tmp1 = numpy.dot(trans, a)
    tmp2 = numpy.dot(trans, b)
    return gauss(tmp1, tmp2)





# normally we would have this line call our main method, but to make
# calls to timeit simpler, we will implement our driver code below
if __name__ == '__main__':
    # a =  [[-3, 1], [1, 1], [-7, 1], [5 ,1]]
    # b = [[70], [21], [110], [-35]]
    # solution to the above equation should be
    # c = [[-12.1],[29.4]]

    # load the training set
    a = get_patient_data('patients.txt')
    b = get_diagnoses('results.txt')

    # first, time the execution of your my_solve vs numpy's solution
    x = timeit.timeit('numpy.linalg.lstsq(a,b)', 'from __main__ import a,b; import numpy', number=300)
    y = timeit.timeit('my_solve(a,b)', 'from __main__ import a,b,my_solve', number=300)
    print('numpy:', x)
    print('custom:', y)

    # solve both ways
    # z is the learned knowledge base / decision set
    z = my_solve(a, b)
    # w is the solution from numpy.linalg
    w = numpy.linalg.lstsq(a, b)[0]

    # test your solution against the numpy solution
    # Percent correct (if < 1.0 (100%) you need to check your work)
    correct = 0
    if len(z) != len(w):
        print('Regression performed incorrectly.')
    for i in range(len(z)):
        if abs(z[i][0]-w[i][0]) < .00001:
            correct += 1

    print('\nLibrary Test')
    print('percent correct: ',float(correct)/z.shape[0])

    # test your code against the test set
    # load the test set
    a = get_patient_data('patients1.txt')
    b = get_diagnoses('results1.txt')

    # Check the percent correct
    # Percent incorrect
    # Percent of total that are false positives
    # Percent of total that are false negatives
    correct = 0
    f_pos = 0
    f_neg = 0
    for row in range(a.shape[0]):
        sol = 0
        for col in range(a.shape[1]):
            sol += a[row][col]*z[col][0]
        sol = 0 if sol < 0.5 else 1
        if sol == b[row][0]:
            correct += 1
        elif sol == 1:
            f_pos += 1
        else:
            f_neg += 1

    print('\nData Test')
    print('percent correct: ', (float(correct)/a.shape[0]))
    print('false positives: ', (float(f_pos)/a.shape[0]))
    print('false negatives: ', (float(f_neg)/a.shape[0]))
