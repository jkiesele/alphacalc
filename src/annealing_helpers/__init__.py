from . import alphacalc

def alpha(t :float, T :float, t0=1):
    '''
    Calculates alpha for a time t in minutes, temperature T in degree Celsius and a t0=1 in minutes
    '''
    return alphacalc.alpha(t,T,t0)
    
def equiv_annealing_time(T_ref: float, t_ref: float, T_target: float, rel_diff: float=1e-6):
    '''
    Calculates the equivalent annealing time for a reference temperature T_ref, 
    and a reference time t_ref to a target temperature of T_target.
    All times are in minutes, and temperatures in degrees Celsius
    '''
    return alphacalc.find_intersection(T_ref,t_ref,T_target,rel_diff)

