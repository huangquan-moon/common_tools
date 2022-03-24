import numpy as np
import statsmodels.api as sm


def univar_ols(y_field, x_field, data, x_order, add_constant=True):
    y = data[y_field].values
    X = np.transpose(np.vstack([data[x_field].values**i for i in range(1, 1+order)]))
    if add_constant:
        X = sm.add_constant(X)
    model = sm.OLS(y,X)
    results = model.fit()
    return results.params, results.rsquared, results
