#!/usr/bin/env python

'''
lambdata - a collection of data science helper functions
'''

import pandas as pd
import numpy as np
from . import example_module

TEST = pd.DataFrame(np.ones(10))
Y = example_module.increment(example_module.x)
