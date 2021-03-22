"""
Second sorting algorithm
Principle : https://fr.wikipedia.org/wiki/Tri_fusion
"""

def TriFusion(l, reverse=False):
    """
    Implementation of the "tri fusion" alogorithm

    COMPLEXITY :
    ------------
    Low/Very Good : O(n log(n))

    PARAMETRES :
    ------------
    - it : iterable : list || str
        - iterable that needs to be sorted
    - reverse : bool
        - If False, sort in asending order
        - If True, sort in descending order
            - default = False
    
    RETURNS :
    - it : iterable (same type as it)
        sorted iterable
    """