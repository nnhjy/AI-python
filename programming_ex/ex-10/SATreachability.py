
from logic import *

# Mapping from actions and initial and goal states to a formula

# Turn variable name 'x' to an atomic formula 'x@t'.

def timedVar(varname,time):
    return ATOM(varname + "@" + str(time))

# Turn action name 'x' to an atomic formula 'x@t'.

def timedAction(varname,time):
    return ATOM("ACTION" + varname + "@" + str(time))

# Two actions cannot be taken at the same time?

def exclusive(c1,pe1,ne1,c2,pe2,ne2):
    return (bool(set(c1) & set(ne2))) or (bool(set(ne1) & set(c2)))

# DO NOT MODIFY ANY DEFINITION ABOVE THIS LINE

# Map a reachability problem to a propositional formula

def reachability2fma(init,goal,actions,T):
    initvars = { v for v in init }
    goalvars = { v for v in goal }
    actioncvars = { v for n,c,pe,ne in actions for v in c }
    actionpvars = { v for n,c,pe,ne in actions for v in pe }
    actionnvars = { v for n,c,pe,ne in actions for v in ne }
    varsets = [initvars,goalvars,actioncvars,actionpvars,actionnvars]
    allStateVars = set().union(*varsets)

    initformulas = [ timedVar(v,0) for v in initvars ] + [ NOT(timedVar(v,0)) for v in allStateVars if v not in initvars ]

    goalformulas = [ timedVar(v,T) for v in goalvars ]

    # a@t -> x@t if x belongs to 'condition' for action 'a' for all t in 0..T
    preconditions = [ IMPL(timedAction(n,t),timedVar(x,t)) for n,c,pe,ne in actions for t in range(0,T) for x in c ]

    # IMPLEMENT THE FORMULA FOR POSITIVE EFFECTS 
    # a@t -> x@(t+1) 
    # if x belongs to 'posEffects' for action 'a' for all t in 0..T-1
    posEffects = [ IMPL(timedAction(n,t),timedVar(x,t+1)) for n,c,pe,ne in actions for t in range(0,T-1) for x in pe ]

    # IMPLEMENT THE FORMULA FOR NEGATIVE EFFECTS 
    # a@t -> not x@(t+1) if x belongs to 'negEffects' for action 'a' for all t in 0..T-1
    negEffects = [ IMPL(timedAction(n,t),NOT(timedVar(x,t+1))) for n,c,pe,ne in actions for t in range(0,T-1) for x in ne ]

    # IMPLEMENT THE POSITIVE FRAME AXIOMS 
    # (not x@t & x@(t+1)) -> a1@t V a2@t V ... V an@t for all t in 0..T-1,
    # where a1,a2,...,an are all actions with x in posEffects.
    posFrameAxioms = AND()

    # IMPLEMENT THE NEGATIVE FRAME AXIOMS
    # (x@t & not x@(t+1)) -> a1@t V a2@t V ... V an@t for all t in 0..T-1, 
    # where a1,a2,...,an are all actions with x in negEffects.
    negFrameAxioms = 

    # IMPLEMENT THE ACTION EXCLUSION CONSTRAINTS 
    # not(a1@t & a2@t) for all t in 0..T-1
    actionMutexes = 

    return AND(initformulas + goalformulas + preconditions + posEffects + negEffects + posFrameAxioms + negFrameAxioms + actionMutexes)
