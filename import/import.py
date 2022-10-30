import os
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
from datetime import date, timedelta
import gc
import pathlib
import datetime
from tqdm.auto import tqdm
import joblib
import json
from multiprocessing import Pool, cpu_count
import time
import requests as re
import datetime
from dateutil.relativedelta import relativedelta, FR
import numerapi
from time import time
from pprint import PrettyPrinter

# visualize
import matplotlib.pyplot as plt
import matplotlib.style as style
import seaborn as sns
from matplotlib import pyplot
from matplotlib.ticker import ScalarFormatter
import warnings
from sklearn import preprocessing