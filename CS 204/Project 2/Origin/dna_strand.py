"""
 File name: DNAStrand.py
 Author:
 VUnetid: 
 Email: 
 Class:
 Date: 
 Honor statement:
 Assignment Number:
 Description: This will be a DNAStrand implemented with a python list.
"""


class DNAStrand(object):
    """
    This class represents a DNA strand with an internal list of characters.
    Supported operations include searching, cleaving and splicing.
    """
    # NOTE: change this constant to True if you are a graduate student
    GRAD_STUDENT = False

    def __init__(self, data=None):
        """
        Constructor
        param data accepts an existing sequence of characters (string, list, tuple, or array)
        """
        # initialize the data list
        # this method is done for you
        if data is None:
            self._myDNA = []
        else:
            self._myDNA = [ch for ch in data]
            
    def __str__(self):
        """
        return string equivalent of the DNA
        """
        # your code here
        return ""
    
    def __len__(self):
        """
        return the size of the DNAStrand
        """
        # your code here
        return -1
    
    # alternate definition for size accessor
    # don't modify this line
    size = __len__
    
    def __iter__(self):
        """
        return an iterator for this DNAStrand
        """
        return self._myDNA.__iter__()    # this one is done for you
    
    def __eq__(self, rhs):
        """
        __eq__
        Compare this DNAStrand with rhs for equality. Returns true if the
        size()'s of the two DNAStrands are equal and all the elements of the
        list are equal, else false.
        """
        # your code here
        return False
    
    def __ne__(self, rhs):
        """
        Not equals operator.
        returns the negation of the equality operator for
        two given objects
        """
        # your code here
        return False
        
    def __setitem__(self, index, letter):
        """
        Set a letter in the DNAStrand at location index. Throws
        IndexError if index is out of range, i.e., larger than the
        current size() of the DNAStrand or less than zero. Throws
        ValueError if the letter is not a single character.
        """
        # your code here
        pass
    
    # alternate definition for item mutator
    # don't modify this line
    set = __setitem__
    
    def __getitem__(self, index):
        """
        Get a letter in the DNAStrand at location index. Throws
        IndexError if index is out of range, i.e., larger than the
        current size() of the DNAStrand or less than zero.
        """
        # your code here
        return None
    
    # alternate definition for item accessor
    # don't modify this line
    get = __getitem__
    
    def in_range(self, position):
        """
        inRange : helper function
        Returns true if position is within range, i.e., 0 <= position < length of DNA strand 
        else returns false.
        """
        # your code here
        pass
        
    def search(self, target, position=0):
        """
        search
        search with start position specified
        Look for target in current DNA strand and return index.
        Return -1 if not found.
        Pre: target is a string
        """
        # your code here
        return -1
    
    # Alternate definition of search
    # more consistent with python collection semantics
    # don't modify this line
    index = search
    
    def cleave(self, target, position=0):
        """
        cleave
        Removes from current DNA strand the sequence between the end of the 
        first occurrence of passed target sequence (e.g. "TTG"), through the end
        of the second occurrence of the target sequence.
        Returns the first index after the cleave
        pre: Array e.g. ACTTGACCTTGA and target is a string e.g. "TTG"
        post: ACTTGA  (ACCTTG removed), index 5 returned
        """
        # your code here
        return -1
        
    def cleave_all(self, target):
        """
        cleaveAll
        Removes from current DNA strand the sequence between pairs of target 
        sequence, i.e. from the end 1 through the end of 2, from the end of 3 
        through the end of 4, etc, but NOT from the end of 2 through the end 3,
        or from the end of 4 through the end of 5.
        (Make sure that you understand the specification)
        pre: Array e.g. ACTTGATTGGGTTGCTTGCC and target (a string) e.g. "TTG"
        post: ACTTGGGTTGCC (ATTG and CTTG removed)
        """
        # your code here
        pass
        
    def count_enzyme(self, target):
        """
        countEnzyme
        Counts the number of non-overlapping occurrences of a target sequence
        in the DNA strand
        Eg, the target "AAA" appears 3 non-overlapping times in the DNA "AAAAAAAAAA"
        Pre: target is a nonempty string. Raise ValueError if target length is zero
        """
        # your code here
        return -1
    
    # Alternate definition of count
    # more consistant with python collection semantics
    # don't modify this line
    count = count_enzyme
    
    def append(self, rhs):
        """
        Append the characters of the parameter to the end of the current DNA.
        Example: if _myDNA contained ACTTGA and 'ACCTG' was received as a parameter, 
        then afterward _myDNA will contain ACTTGAACCTG
        Pre: rhs is a string parameter
        """
        # your code here
        pass
        
    def splice(self, target, replacement, position=0):
        """
        splice (accepts 2 Strings representing sequences)
        finds first pair of targets in current DNA strand and replaces
        the sequence between the end of the first target through the end of the 
        second with the replacement. 
        If two instances of the target are not found, 
        then no changes are made.
        Returns the index of the position after the splice, or -1 if no splice was performed
        Pre: target & replacement are strings
        """
        # your code here
        return -1

    # ########################/
    # THE FOLLOWING METHODS ARE FOR GRAD STUDENTS ONLY
    if GRAD_STUDENT:
        _MARKER = '#'
        
        def insert_marker(self, target):
            """
            insertMarker
            Find all non-overlapping occurrences of the target sequence and insert
            the '#' marker AFTER each of them.
            pre: Array e.g. ACTTGATTGGGTTGCTTGCC and target e.g. "TTG"
            post: ACTTG#ATTG#GGTTG#CTTG#CC
            """
            # your code here
            pass
            
        def delete_marker(self):
            """
            deleteMarker
            Delete all the '#' markers that occur in the strand, shifting data to the
            left as appropriate
            """
            # your code here
            pass
            
        def count_marker(self):
            """
            count_MARKER
            return the number of _MARKERs that exist in the strand
            """
            # your code here
            return -1
            
        def splice_all(self, target, replacement):
            """
            spliceAll (accepts 2 Strings representing sequences)
            Similar to cleaveAll finds pairs of targets in current DNA strand and replaces
            the sequence between the end of the first target through the end of the 
            second with the insertSequence. If two instances of the target are not found, 
            then no changes are made.
            """
            # your code here
                
    # END GRAD STUDENT ONLY METHODS
    #########################/