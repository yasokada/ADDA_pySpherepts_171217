import numpy as np
import polarAzimuthCalc_171209 as pAC
import getIcosNodes_171126 as gIN
import getHammersleyNodes_171203 as gHN
import sys

'''
Dec. 17, 2017
This script requires the setup of [pySpherepts_171126] pACkage shown at
    https://github.com/yasokada/pySpherepts_171126
for [getIcosNodes_171126]
'''

'''
v0.1 Dec. 17, 2017
   - add Test_run_getIcosNodes()
   - add make_beta_gamma_tbl_gIN()
'''

kFile_output_gIN = 'beta_gamma_gIN.tbl'
kFile_output_gHN = 'beta_gamma_gHN.tbl'


def output_file(outlst, filename):
    hdrtxt = 'beta(deg),gamma(deg)'
    np.savetxt(filename, outlst, fmt='%.3f',
               delimiter=",", header=hdrtxt)
    msg = "[{0}] is created".format(filename)
    print(msg)


def make_beta_gamma_tbl_gIN(kIndex, typeIndex):
    xs, tris = gIN.getIcosNodes(kIndex, typeIndex)
    outlst = []
    for elem in xs:
        beta_rad = pAC.calc_beta_rad(elem)
        gamma_rad = pAC.calc_gamma_rad(elem)

        beta_deg = np.rad2deg(beta_rad)
        gamma_deg = np.rad2deg(gamma_rad)

        outlst += [[beta_deg, gamma_deg]]
    output_file(outlst, kFile_output_gIN)


def make_beta_gamma_tbl_gHN(nodeNumber):
    xs = gHN.getHammersleyNodes(nodeNumber)
    outlst = []
    for elem in xs:
        beta_rad = pAC.calc_beta_rad(elem)
        gamma_rad = pAC.calc_gamma_rad(elem)

        beta_deg = np.rad2deg(beta_rad)
        gamma_deg = np.rad2deg(gamma_rad)

        outlst += [[beta_deg, gamma_deg]]
    output_file(outlst, kFile_output_gHN)


def Test_run_gIN():
    make_beta_gamma_tbl_gIN(4, 0)  # 2562 points
    # make_beta_gamma_tbl_gIN(3, 0)  # 642 points


def Test_run_gHN():
    make_beta_gamma_tbl_gHN(2025)


if __name__ == '__main__':
    Test_run_gIN()
    Test_run_gHN()
