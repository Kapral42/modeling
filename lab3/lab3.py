#!/usr/bin/python

import sys
import random
import numpy as np

class Smo():
    def __init__(self, max_size):
        self.max_size =  max_size
        self.distribs = { 'M' : 'exponencial', 'R' : 'uniform', 'D' : 'const'}

    def compute(self, d_type_tau, d_type_sigma, math_exp_step):
        res_full = []
        math_exp_tau = math_exp_step
        while math_exp_tau < 1.00:
            tau = self.gen_array(math_exp_tau, d_type_tau)
            math_exp_sigma = math_exp_step
            res = []
            while math_exp_sigma < 1.00:
                sigma = self.gen_array(math_exp_sigma, d_type_sigma)

                omega = [0] * self.max_size
                math_exp_omega = 0
                for i in range(self.max_size)[1:]:
                    omega[i] = max(0, sigma[i - 1] + omega[i - 1] - tau[i])
                    math_exp_omega += omega[i]
                math_exp_omega /= self.max_size

                res.append(math_exp_omega)

                math_exp_sigma += math_exp_step
            math_exp_tau += math_exp_step
            res_full.append(res)
        return res_full


    def gen_array(self, math_exp, type):
        if type.upper() == 'M': # exponencial distribution
            x = self.d_expo(math_exp)
        elif type.upper() == 'R': # uniform distribution
            x = self.d_uniform(math_exp)
        elif type.upper() == 'D': # const distribution
            x = self.d_const(math_exp)
        else:
            print("Incorrect distribution type!")
            exit()
        return x

    def d_uniform(self, math_exp):
        x = [ random.uniform(0,1) * math_exp \
             for i in range(self.max_size)]
        return x

    def d_expo(self, math_exp):
        lbd = 1 / math_exp
        x = [ (-1 * np.log(1 - random.uniform(0,1))) / lbd \
             for i in range(self.max_size)]
        return x

    def d_const(self, math_exp):
        x = [math_exp] * self.max_size
        return x

def main(argv=None):
    smo = Smo(10000)
    step = 0.1
    for i in smo.distribs:
        for j in smo.distribs:
            res = smo.compute(i, j, step)

            iv = smo.distribs[i]
            jv = smo.distribs[j]
            file = open(iv + '_' + jv + '.out', 'w')
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
            print i, j + " computed."

if __name__ == "__main__":
    sys.exit(main())
