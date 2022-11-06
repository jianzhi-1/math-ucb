class MA1_Model():
    def __init__(self, y):
        """initializes model with dataset y"""
        self.y = y
        self.n = len(y)
        self.dmu = None
        self.dtheta = None
        self.muhat = None
        self.thetahat = None
    
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
        if self.dmu is None or mu_step < self.dmu: self.dmu = mu_step
        if self.dtheta is None or theta_step < self.dtheta: self.dtheta = theta_step
        
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
        muhat, thetahat = mu_grid[best_mu][best_theta], theta_grid[best_mu][best_theta]
        
        if k == 0:
            self.muhat = muhat
            self.thetahat = thetahat
            return muhat, thetahat
        
        return self.optimizer(mu_low=muhat-mu_step, 
                              mu_high=muhat+mu_step, 
                              mu_step=mu_step/10, 
                              theta_low=thetahat-theta_step, 
                              theta_high=thetahat+theta_step, 
                              theta_step=theta_step/10., 
                              k=k-1)
    
    def hessian_s(self, mu, theta, dmu=0.001, dtheta=0.001):
        """returns the hessian for uncertainty calculation"""
        if self.dmu is not None: dmu = self.dmu
        if self.dtheta is not None: dtheta = self.dtheta
        
        res = np.zeros((2,2))
        
        # partial^2 mu
        hi_mu, mid_mu, low_mu = self.s(mu + 2.*dmu, theta), self.s(mu, theta), self.s(mu - 2.*dmu, theta)
        hi_deriv_mu, low_deriv_mu = (hi_mu - mid_mu)/(2.*dmu), (mid_mu - low_mu)/(2.*dmu)
        res[0][0] = (hi_deriv_mu - low_deriv_mu)/(2*dmu)

        # partial mu partial theta
        hi_theta_mu, low_theta_mu = self.s(mu + dmu, theta + dtheta), self.s(mu + dmu, theta - dtheta)
        hi_theta_mu_2, low_theta_mu_2 = self.s(mu - dmu, theta + dtheta), self.s(mu - dmu, theta - dtheta)
        hi_deriv_theta_mu, low_deriv_theta_mu = (hi_theta_mu - low_theta_mu)/(2.*dtheta), (hi_theta_mu_2 - low_theta_mu_2)/(2*dtheta)
        res[0][1] = res[1][0] = (hi_deriv_theta_mu - low_deriv_theta_mu)/(2.*dmu)
        
        # partial^2 theta
        hi_theta, mid_theta, low_theta = self.s(mu, theta + 2.*dtheta), self.s(mu, theta), self.s(mu, theta - 2.*dtheta)
        hi_deriv_theta = (hi_theta - mid_theta)/(2.*dtheta)
        low_deriv_theta = (mid_theta - low_theta)/(2.*dtheta)
        res[1][1] = (hi_deriv_theta - low_deriv_theta)/(2.*dtheta)

        return res
    
    def uncertainty(self):
        hess = self.hessian_s(self.muhat, self.thetahat)
        mu_confidence_interval = stats.t.interval(0.95, self.n - 2, loc=self.muhat, scale=np.sqrt(1./(self.n-2)*self.s(self.muhat, self.thetahat)*(np.linalg.inv(1./2.*hess)[0][0])))
        theta_confidence_interval = stats.t.interval(0.95, self.n - 2, loc=self.thetahat, scale=np.sqrt(1./(self.n-2)*self.s(self.muhat, self.thetahat)*(np.linalg.inv(1./2.*hess)[1][1])))
        return mu_confidence_interval, theta_confidence_interval
