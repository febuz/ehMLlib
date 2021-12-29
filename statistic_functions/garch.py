!pip install arch

# Import Built-Ins:
import math
import statistics

# Import Third-Party:
from random import gauss
from random import seed
from arch import arch_model

def GARCH(df):
    """
    Generalized AutoRegressive Conditional Hetroskedasiticity
    Returns: list of variance = jhta.GARCH(df, n, price='Close', xbar=None)
    """
    # seed pseudorandom number generator
    seed(1)
    if len(df) < 10:
        # create dataset
        data = [gauss(0, i*0.01) for i in range(0,100)]
    else:
        data = df
    # split into train/test
    n_test = 10
    train, test = data[:-n_test], data[-n_test:]
    # define model
    model = arch_model(train, mean='Zero', vol='GARCH', p=15, q=15)
    # fit model
    model_fit = model.fit()
    # forecast the test set
    yhat = model_fit.forecast(horizon=n_test)
    # plot the actual variance
    var = [i*0.01 for i in range(0,100)]
    return yhat.variance.values[-1, :]
