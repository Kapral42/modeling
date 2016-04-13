#!/usr/bin/python

import sys
import random
import numpy as np

class Smo():
    def __init__(self, max_size):
        self.max_size =  max_size

    def compute(self, math_exp_step, t_sort):
        res_full = []
        # math_exp* - math expectation *
        math_exp_tau = math_exp_step

        # set of tau and sigma
        tau_sigma = []
        for i in range(self.max_size):
            tau_sigma.append([0.0, 0.0])
        # identificators
        taui = 0
        sigmai = 1

        while math_exp_tau < 1.00:
            self.d_uniform(tau_sigma, math_exp_tau, 'tau')
            math_exp_sigma = math_exp_step
            res = []
            while math_exp_sigma < 1.00:
                tau_sigma = self.d_uniform(tau_sigma, math_exp_sigma, 'sigma')

                # sort input tasks
                self.sort(tau_sigma, t_sort)

                omega = [0] * self.max_size
                math_exp_omega = 0
                for i in range(self.max_size)[1:]:
                    omega[i] = max(0, tau_sigma[i - 1][sigmai] + omega[i - 1] \
                                   - tau_sigma[i][taui])
                    math_exp_omega += omega[i]
                math_exp_omega /= self.max_size

                res.append(math_exp_omega)

                math_exp_sigma += math_exp_step
            math_exp_tau += math_exp_step
            res_full.append(res)
        return res_full

    def sort(self, set, t_key):
        if t_key.upper() == 'SF':
            # first - slow tasks
            set.sort(key=lambda x: x[-1], reverse=True)
        elif t_key.upper() == 'SL':
            # first - fast tasks
            set.sort(key = lambda x: x[1])
        # if FIFO or incorrect type - do nothing
        return set

    def d_uniform(self, set, math_exp, ident):
        """ uniform distribution"""

        k = 0 if ident.lower() == 'tau' else 1
        for i in range(self.max_size):
            set[i][k] = random.uniform(0,1) * math_exp
        return set

def main(argv=None):
    smo = Smo(10000)
    step = 0.1

    q_types = ['FIFO', 'SF', 'SL']
    for t in q_types:
        res = smo.compute(step, t)

        file = open(t + '.out', 'w')
        nstr = len(res[0])
        istep = 0.0
        for str in range(nstr):
            istep += step
            out = repr(istep)
            for col in range(len(res)):
                s = repr(float(res[col][str]))
                out = out + "\t" + s
            file.write(out + '\n')
        file.close()
        print t + " computed."

if __name__ == "__main__":
    sys.exit(main())
