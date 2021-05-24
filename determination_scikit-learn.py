import random
import numpy as np

def set_seeds(seed=0):
    random.seed(seed)
    np.random.seed(seed)