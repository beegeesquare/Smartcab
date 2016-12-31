"""
Markov decision process (MDP):
Source: ~/aima-python/bolb/master/mdp.py

"""

class MDP:
    """A Markov Decision Process, defined by an initial state, transition model,
    and reward function. We also keep track of a gamma value, for use by
    algorithms. The transition model is represented somewhat differently from
    the text.  Instead of P(s' | s, a) being a probability number for each
    state/state/action triplet, we instead have T(s, a) return a
    list of (p, s') pairs.  We also keep track of the possible states,
    terminal states, and actions for each state """
    
    
    def __init__(self, init,actionlist,terminals,gamma=0.9):
        self.init=init
        self.actionlist=actionlist
        self.terminals=terminals # These are terminal states
        if not (0<=gamma < 1):
            raise ValueError('For MDP gamma has to be between [0,1)')
        self.gamma=gamma
        # Define the states
        self.states=set()
        self.reward={}
    
    def R(self,state):
        """
        Returns reward for a given state
        """
        return self.reward[state]
    
    def T(self,state,action):
        """
        Transtion model: From a state and an action, return a list of (probability,result-state) pairs
        """
        


def value_iteration(states,actions,transition_model,rewards,discounted_rate):
    """
    This function computes the 
    """
    
    
    return