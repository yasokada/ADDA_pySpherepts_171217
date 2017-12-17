import numpy as np
import polarAzimuthCalc_171209 as pac
import getIcosNodes_171126 as gIN
import sys

'''
Dec. 17, 2017
This script requires the setup of [pySpherepts_171126] package shown at
    https://github.com/yasokada/pySpherepts_171126
for [getIcosNodes_171126]
'''

'''
v0.1 Dec. 17, 2017
   - add test_pySpherepts_IcosNodes()
'''


def test_pySpherepts_IcosNodes():
    xs, tris = gIN.getIcosNodes(4,0)
    pvecs = xs
    for elem in pvecs:
        beta_rad = pac.calc_beta_rad(elem)
        gamma_rad = pac.calc_gamma_rad(elem)
        beta_deg = np.rad2deg(beta_rad)
        gamma_deg = np.rad2deg(gamma_rad)

        fmt = "{0} \tbeta:{1:6.1f} gamma:{2:6.1f}"
        msg = fmt.format(elem, beta_deg, gamma_deg)
        print(msg)


if __name__ == '__main__':
    test_pySpherepts_IcosNodes()