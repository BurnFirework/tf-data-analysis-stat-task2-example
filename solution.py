import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 860138765

def solution(p: float, x: np.array) -> tuple:
    left_bound = 0.074
    max_x = max(x)
    n = len(x)

    g1 = (1 - p) ** (1 / n)
    left = max_x
    right = (max_x - left_bound) / g1 + left_bound
    magic_size_add = (right - left) * 0.3

    return (left, right + magic_size_add)
