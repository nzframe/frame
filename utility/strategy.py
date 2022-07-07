from typing import Callable
import math


GAP_STRATEGY = Callable[[float, float], float]

def gap_strategy_default(defautl_gap: float, total_distance: float):
    return defautl_gap

def gap_strategy_avg(default_gap: float, total_distance: float):
    return (total_distance / math.ceil(total_distance / default_gap))
