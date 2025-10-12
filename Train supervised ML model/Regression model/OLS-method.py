def ols(x, y):
    xmean = x.mean()
    ymean = y.mean()
    xvariance = sum([(x - xmean)**2 for x in x])
    xycovariance = 0
    for i in range(len(x)):
        xycovariance += (x[i] - xmean) * (y[i] - ymean)
    m = xycovariance / xvariance
    c = ymean - m * xmean
    return m, c