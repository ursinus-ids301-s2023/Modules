squared_loss = lambda u, y: (y-logistic(u))**2

logistic_loss = lambda u, y: -(np.log(logistic(u))*y + np.log(1-logistic(u))*(1-y))
