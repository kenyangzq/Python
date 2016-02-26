#
# Filename: DNAStrand.py
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

# Represents a DNA strand using strings to store the data
#
# To reduce errors in the starter files, return statements have been
# included beneath each method. Make the decision on whether the return
# statement is necessary for a particular method.
class DNAStrand(object):
    
    # Graduate students set to true
    GRAD_STUDENT = False

    # Constructor
    #
    #  @param (optional) 
    #    dna is a string DNA sequence
    #    defaults to empty string
    def __init__(self, dna=""):
        self._mDNA = dna

    # Returns the DNAStrand as a string
    #
    # @return
    def __str__(self):
        # YOUR CODE GOES HERE
        return self._mDNA

    # Returns the length of the DNAStrand
    #
    # @return
    def __len__(self):
        # YOUR CODE GOES HERE
        return len(self._mDNA)
    
    # Compare this DNAStrand with rhs for equality.
    # @param rhs DNA to compare
    # @return
    #    True if the DNA strings are equal
    #    else, False
    def __eq__(self, rhs):
        # YOUR CODE GOES HERE
        return (self._mDNA == rhs._mDNA)

    # Get an item in the DNAStrand at location index. Throws
    # IndexError if index is out of range, i.e., larger than the
    # current size() of the DNAStrand.
    def __getitem__(self, position):
        # YOUR CODE GOES HERE
        if not self.in_range(position):
            raise IndexError("index out of range")
        return self._mDNA[position]
    
    # Set an item in the DNAStrand at location index. Throws
    # IndexError if index is out of range, i.e., larger than the
    # current size() of the DNAStrand.
    def __setitem__(self, position, letter):
        # YOUR CODE GOES HERE
        if not self.in_range(position):
            raise IndexError("index out of range")
        self._mDNA = self._mDNA[0:position] + letter + self._mDNA[position+1:]

    # Verifies that position is between 0 (inclusive) and the
    # length of the DNA sequence (exclusive)
    #
    # @param position
    # @return
    #    True if position within range
    #    False if not
    def in_range(self, position):
        # YOUR CODE GOES HERE
        return (position >= 0 and position < len(self._mDNA))

    # Locates the first instance of target
    #
    # @target character to locate
    # @position (optional) 
    #    the starting position
    #    defaults to 0
    # @return
    #    index of target if found
    #    -1 if target not found
    def search(self, target, position=0):
        # YOUR CODE GOES HERE
        return self._mDNA.find(target, position)

    # Removes from current DNA strand the sequence between the *end* of the
    # first occurrence of passed target sequence (e.g. "TTG"), through the 
    # *end* of the second occurence of the target sequence.
    #
    # @pre e.g. "ACTTGACCTTGA" and target e.g. "TTG"
    # @post ACTTGA  (ACCTTG removed)
    # @param target target sequence
    # @param position (optional)
    #    the starting position
    #    defaults to 0
    # @return index following the first instance of target post-cleave 
    #    -1 if fewer than two instances of target after position
    #    (hint: helpful for cleaveAll)
    def cleave(self, target, position=0):
        # YOUR CODE GOES HERE
        return self.splice(target, "", position)

    # Removes from current DNA strand the sequence between pairs of target
    # sequence, i.e. from the end 1 through the end of 2, from the end of 3 
    # through the end of 4, etc, but NOT from the end of 2 through the end 3,
    # or from the end of 4 through the end of 5.
    # (Make sure that you understand the specification)
    #
    # @pre DNA e.g. ACTTGATTGGGTTGCTTGCC and target e.g. "TTG"
    # @post DNA ACTTGGGTTGCC (ATTG and CTTG removed)
    # @param target target sequence
    def cleave_all(self, target):
        # YOUR CODE GOES HERE
        index = 0; # starting index to cleave, stop when it becomes -1
        while (index >= 0):
            index = self.cleave(target, index)

    # Counts the number of occurrences of a single character target sequence
    # in the DNA strand
    #
    # @param target single enzyme as character
    # @return number of occurrences of target
    def count_enzyme(self, target):
        # YOUR CODE GOES HERE
        return self._mDNA.count(target)

    # Append the characters of the parameter to the end of the current DNA
    # @pre DNA e.g. ACTTGA and rhs e.g. ACCTG
    # @post DNA ACTTGAACCTG
    # @param rhs the DNA strand to append to the right hand side of existing
    def append(self, rhs):
        # YOUR CODE GOES HERE
        self._mDNA = self._mDNA + rhs

    # Replaces the DNA sequence between the end of the first occurrence of
    # target and the end of the second occurrence of target with a new
    # DNA sequence.
    # @post
    #    if two targets found, target is replaced by replacement
    #    else, no change
    # @param target specifies the DNA sequence to replace
    # @param replacement DNA sequence replacing the removed sequence
    # @param position (optional)
    #    position to begin searching for target
    #    defaults to 0
    # @return 
    #    index following the first instance of replacement post-splice
    #    -1 if fewer than two instances of target after position
    #    (hint: helpful for spliceAll)
    def splice(self, target, replacement, position=0):
        # YOUR CODE GOES HERE
        length = len(target)
        position1 = self._mDNA.find(target, position) + length
        position2 = self._mDNA.find(target, position1) + length
        if position1 < length or position2 < length:
            return -1;
        self._mDNA = self._mDNA[0:position1] + replacement + self._mDNA[position2:]    
        return position1

    #########################
    # THE FOLLOWING METHODS ARE FOR GRAD STUDENTS ONLY
    if GRAD_STUDENT:
        MARKER = "#"    # you can reference this variable by using: self.__class__.MARKER
        
        # Find all non-overlapping occurrences of the target sequence and insert
        # the '#' marker AFTER each of them.
        #
        # @pre DNA e.g. ACTTGATTGGGTTGCTTGCC and target e.g. "TTG"
        # @post DNA ACTTG#ATTG#GGTTG#CTTG#CC
        def insert_marker(self, target):
            # YOUR CODE GOES HERE
            return

        # Delete all the '#' markers that occur in the strand
        # @pre DNA e.g. ACTTG#ATTG#GGTTG#CTTG#CC
        # @post DNA ACTTGATTGGGTTGCTTGCC
        def delete_marker(self):
            # YOUR CODE GOES HERE
            return
            
        # Returns the number of markers in the strand
        # @return
        def count_marker(self):
            # YOUR CODE GOES HERE
            return

        # Similar to cleaveAll finds pairs of targets in current DNA strand and replaces
        # the sequence between the end of the first target through the end of the 
        # second with the insertSequence. If two instances of the target are not found, 
        # then no changes are made.
        def splice_all(self, target, replacement):
            # YOUR CODE GOES HERE
            return
                
    # endif GRAD_STUDENT
    # END GRAD STUDENT ONLY METHODS
    #########################
