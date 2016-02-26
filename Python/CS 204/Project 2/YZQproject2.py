"""
 File name: project1.py
 Author: Ziqi Yang
 VUnetid: yangz9
 Email: ziqi.yang@vanderbilt.edu
 Class: 
 Date: 
 Honor statement:
 Assignment Number:
 Description: test driver for DNA_Strand.py
"""

from YZQdna_strand import *

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

    if dna.size() != 6:
        print "Test 5 FAIL."


    test1 = DNAStrand("ABCC")
    test2 = DNAStrand("ABCD")

    if test1 == test2:
        print "Test 6 FAIL."

    if not test1 != test2:
        print "Test 7 FAIL."

    if test1 == dna:
        print "Test 8 FAIL."

    if test1.search("CC") != 2:
        print "Test 9 FAIL."
        print test1.search("CC")

    test3 = DNAStrand("AAAAAAAAA")
    if test3.search("AAA", 5) != 5:
        print "Test 10 FAIL."
    
    test1.append("TG")
    if test1 != dna:
        print "Test 11 FAIL."

    if test3.count("AAA") != 3:
        print "Test 12 FAIL."

    test5 = DNAStrand("ACTTGGGTTGCTTGCC")
    test4 = DNAStrand("ACTTGATTGGGTTGCTTGCC")
    c1 = test4.cleave("TTG")
    if c1 != 5:
        print c1
        print "Test 13 FAIL."

    if test4 != test5:
        print str(test4)
        print "Test 14 FAIL."

    test4 = DNAStrand("ACTTGATTGGGTTGCTTGCC")
    test5 = DNAStrand("ACTTGGGTTGCC")

    test4.cleave_all("TTG")
    if test4 != test5:
        print str(test4)
        print "Test 15 FAIL."
        


    # add your testing code here
    # be sure to test as thoroughly as possible
    print("Done testing")

if __name__ == '__main__':
    main()
