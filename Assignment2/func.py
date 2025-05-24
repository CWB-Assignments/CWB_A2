from datetime import datetime
from pandas import *
import numpy as np
def generate_random_datetimes(n):
    start_timestamp = int(datetime(2000, 1, 1).timestamp()) 
    end_timestamp = int(datetime(2025, 1, 1).timestamp())

    # Use int64-safe random generator
    rng = np.random.default_rng()
    random_timestamps = rng.integers(low=start_timestamp, high=end_timestamp, size=n, dtype='int64')
    return to_datetime(random_timestamps, unit='s')