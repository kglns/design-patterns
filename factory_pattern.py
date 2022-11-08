class NewtonRaphson:
    '''
    Using scipy lib here - not going to implement the algorithm because this is an example
    Ref: https://docs.scipy.org/doc/scipy-0.15.1/reference/generated/scipy.optimize.newton.html#scipy.optimize.newton
    '''
    def __init__(self, tolerance=1.48e-8, maxiter=50):
        import scipy.optimize as optimize # lazy import
        self.tolerance = tolerance
        self.maxiter = maxiter
        self.solver = optimize.newton

    def __name__(self):
        return 'NewtonRaphson'
    
    def calculate(self, func, x0):
        return self.solver(func, x0, tol=self.tolerance, maxiter=self.maxiter)

class BisectRootFinder:

    # Ref: https://docs.scipy.org/doc/scipy-0.15.1/reference/generated/scipy.optimize.bisect.html#scipy.optimize.bisect
    def __init__(self, xtolerance=1e-12, rtolerance=4.44e-16, maxiter=100, disp=True):
        from scipy.optimize import bisect # lazy import
        self.xtolerance = xtolerance
        self.rtolerance = rtolerance
        self.maxiter = maxiter
        self.disp = disp
        self.solver = bisect

    def __name__(self):
        return 'Bisect'
    
    def calculate(self, func, a, b):
        return self.solver(func, a, b, xtol=self.xtolerance, rtol=self.rtolerance, maxiter=self.maxiter, disp=self.disp)

class RootFinderFactory:

    def __init__(self, instname='DefaultFactory'):
        from functools import partial # lazy import
        self.instname = instname # we may want more than one factories
        self.mapper = {
            'newton': partial(NewtonRaphson),
            'bisect': partial(BisectRootFinder)
        }

    def create(self, method='newton', **kwargs):
        return self.mapper.get(method)(**kwargs)

import unittest
class TestFactoryPattern(unittest.TestCase):

    def setUp(self):
        self.fac = RootFinderFactory()

    def test_factory_name(self):
        self.assertTrue(self.fac.instname, 'DefaultFactory')
    
    def test_newton_inst(self):
        self.assertTrue(self.fac.create('newton').__name__, 'NewtonRaphson')

    def test_bisect_inst(self):
        self.assertTrue(self.fac.create('bisect').__name__, 'Bisect')

if __name__ == '__main__':
    unittest.main()
