import numpy as np
import polarAzimuthCalc_171209 as pac
import sys

'''
v0.1 Dec. 17, 2017
  - add Test_from_xyz_file()
'''

kFile_xyz = 'xyz_position.tbl'  # position file


def Test_from_xyz_file():
    pvecs = np.genfromtxt(kFile_xyz, delimiter=',')
    for elem in pvecs:
        beta_rad = pac.calc_beta_rad(elem)
        gamma_rad = pac.calc_gamma_rad(elem)
        beta_deg = np.rad2deg(beta_rad)
        gamma_deg = np.rad2deg(gamma_rad)

        fmt = "{0} \tbeta:{1:6.1f} gamma:{2:6.1f}"
        msg = fmt.format(elem, beta_deg, gamma_deg)
        print(msg)


if __name__ == '__main__':
    Test_from_xyz_file()
