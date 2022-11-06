class MA1_Model():
    def __init__(self, y):
        """initializes model with dataset y"""
        self.y = y
        self.n = len(y)
    
    def s(self, mu, theta):
        """returns sum of squared error"""
        m = np.zeros(self.n) # collate the mean
        m[0] = mu
        c0 = 1. - theta
        c1 = theta*self.y[0]
        for i in range(1, len(self.y)):
            m[i] = mu*c0 + c1
            c0 += (-theta)**(i+1)
            c1 *= (-theta)
            c1 += theta*self.y[i]
        return np.sum((self.y - m)**2)

    def log_posterior(self, mu, theta):
        """returns the log posterior for given (mu, theta)"""
        return -self.n/2.*np.log(self.s(mu, theta))

    def optimizer(self, mu_low=-2., mu_high=2., mu_step=0.1, theta_low=-1., theta_high=1., theta_step=0.01, k=0):
        """returns optimal (muhat, thetahat) that maximizes log posterior"""
        mu_grid, theta_grid = np.meshgrid(np.arange(mu_low, mu_high, mu_step), np.arange(theta_low, theta_high, theta_step))
        log_posterior_grid = np.zeros(mu_grid.shape)
        best_mu, best_theta = None, None
        maxi = None
        for i in range(mu_grid.shape[0]): # mu
            for j in range(theta_grid.shape[1]): # theta
                log_posterior_grid[i][j] = self.log_posterior(mu_grid[i][j], theta_grid[i][j])
                if maxi is None or maxi < log_posterior_grid[i][j]:
                    maxi = log_posterior_grid[i][j]
                    best_mu, best_theta = i, j
        muhat, thetahat = mu_grid[besti][bestj], theta_grid[besti][bestj]
        
        if k == 0:
            return muhat, thetahat
        
        return self.optimizer(mu_low=muhat-mu_step, 
                              mu_high=muhat+mu_step, 
                              mu_step=mu_step/10, 
                              theta_low=thetahat-theta_step, 
                              theta_high=thetahat+theta_step, 
                              theta_step=theta_step/10., 
                              k=k-1)
