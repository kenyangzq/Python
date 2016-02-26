#
# Filename: project1.py
# Description: 
#
# Author: Ziqi Yang
# VUNetID: yangz9
# Email: ziqi.yang@vanderbilt.edu
# Date: 1.24.2016
#
# Honor Statement: 
#
# Caveats: 
#

from YZQdna_strand import *


# Program main method
def main():
    # test some basic functions of the DNA_Strand class
    dna_1 = DNAStrand()  # start with two empty strands
    dna_2 = DNAStrand()
    
    # test length. This will automatically invoke the __len__() member function
    if len(dna_1) != 0:
        print("Length test failed for default constructor.")
    
    # or you can call  __len__() directly
    if dna_1.__len__() != 0:
        print("Length test failed for default constructor.")
    
    # test equality. this invokes __eq__()
    if not dna_1 == dna_2:
        print("Equality test failed.")
    
    # test should be reflective
    if not dna_2 == dna_1:
        print("Equality test failed.")
    
    # create a non-empty DNA
    dna = DNAStrand("ACTTGATTGGGTTGCTTGCC")
    
    # test length
    if len(dna) != 20:
        print("Length test failed for parameterized constructor")
    

#pass




    # test to string
    if dna.__str__() != "ACTTGATTGGGTTGCTTGCC":
        print("To string test failed.")
    
    # you can also use str() to automatically call __str__()
    # the following call is identical to the one above
    if str(dna) != "ACTTGATTGGGTTGCTTGCC":
        print("To string test failed.")
        
    # test indexing - invokes the __getitem__() method
    if dna[0] != "A":
        print("__getitem__() test failed.")
    try:
        dna[100]
        print("__getitem__() test failed.")
    except:
        pass
    
    # test indexing - __setitem__
    dna[0] = "X"
    if dna[0] != "X":
        print("__setitem__() test failed.")
    try:
        dna[100] = "X"
        print("__setitem__() test failed")
    except:
        pass

    # test search
    if dna.search("G") != 4:
        print("Search test failed.")
    if dna.search("G", 100) != -1:
        print("Search test failed.")
        
    # add your testing code here
    # be sure to test as thoroughly as possible
    
    test1 = DNAStrand("ACTTGATTGGGTTGCTTGCC")

    if test1.count_enzyme("TTG") != 4:
        print "count_enzyme failed" 
        print "Unexpected return : %d" % test1.count_enzyme("TGG")


    cleave1 = test1.cleave("TTG")
    if cleave1 != 5:
        print "Cleave return failed"
        print "Unexpected return: %d" % cleave1

    if test1.__str__() != "ACTTGGGTTGCTTGCC" :
        print "Cleave failed"
        print "Unexpected return " + test1.__str__()

    cleave2 = test1.cleave("TTG", cleave1)
    if cleave2 != 10:
        print "cleave second times return failed"
        print "Unexpected return: %d" % cleave2

    if test1.__str__() != "ACTTGGGTTGCC":
        print "cleave second times failed"
        print "Unexpected return " + test1.__str__()


    test2 = DNAStrand("ACTTGATTGGGTTGCTTGCC")

    test2.cleave_all("TTG") 
    if  test2.__str__() != "ACTTGGGTTGCC":
        print "cleave_all test failed"
        print "Unexpected return " + test2.__str__()


    # YOUR CODE HERE
    
    print("Done testing")


# The following allows the main method
# to run automatically when this file
# is passed to python
if __name__ == "__main__":
    main()
