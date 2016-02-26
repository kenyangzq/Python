"""
 File name: project1.py
 Author:
 VUnetid: 
 Email: 
 Class:
 Date: 
 Honor statement:
 Assignment Number:
 Description: test driver for DNA_Strand.py
"""

from dna_strand import *

"""
Note: The way in which this assignment writes comments differs from the 
    first assignment. Python can make use of either system and you should
    be aware of both.
"""


def main():
    # test some basic functions of the DNA_Strand class
    dna_1 = DNAStrand()
    dna_2 = DNAStrand()
    
    if dna_1.size() != 0:
        print("Test 1 FAIL")
    
    if not dna_1.__eq__(dna_2):
        print("Test 2 FAIL")
    
    if not (dna_1 == dna_2):   # == operator calls __eq__
        print("Test 2a FAIL")
    
    # test should be reflective
    if not dna_2.__eq__(dna_1):
        print("Test 3 FAIL")

    # create a non-empty DNA
    dna = DNAStrand("ABCCTG")
    
    # toString should return the contents as a string
    if str(dna) != "ABCCTG":
        print("Test 4 FAIL.")

    # add your testing code here
    # be sure to test as thoroughly as possible
    print("Done testing")

if __name__ == '__main__':
    main()
