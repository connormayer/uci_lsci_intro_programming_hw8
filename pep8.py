"""Part of a class that implements a finite state automaton."""

def RemoveDuplicates(my_list):
    """Remove duplicates from a list."""
    return list (set(my_list))

class Automaton():
    """Implements a finite state automaton."""

    def __init__(self, 
        start, ends, deltas):
        """Construct an Automaton instance."""
        self.start = start
        self.ends=ends
        self.deltas = deltas

    def targets(self, q, x) :
        """
        Find possible outcomes of transition from current state.

        Given a transition table, a state, and a symbol, find all the states
        we can get to by stepping away from that state and emitting that
        symbol.
        """
        return RemoveDuplicates([ q2 for (q1,y,q2) in self.deltas if q1==q and y==x ])