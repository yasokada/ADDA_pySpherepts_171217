import numpy as np
import polarAzimuthCalc_171209 as pac
import sys

'''
v0.1 Dec. 17, 2017
  - add Test_group_run_axes()
'''


def Test_group_run_axes():
    print('---Test_group_run_axes---')
    pvecs = [
        [0, 0, 1],  # z direction
        [0, 0, -1],  # z direction
        [0, 1, 0],  # y direction
        [0, -1, 0],  # y direction
        [1, 0, 0],  # x direction
        [-1, 0, 0],  # x direction
        ]
    for elem in pvecs:
        beta_rad = pac.calc_beta_rad(elem)
        gamma_rad = pac.calc_gamma_rad(elem)
        beta_deg = np.rad2deg(beta_rad)
        gamma_deg = np.rad2deg(gamma_rad)

        fmt = "{0} \tbeta:{1:6.1f} gamma:{2:6.1f}"
        msg = fmt.format(elem, beta_deg, gamma_deg)
        print(msg)

if __name__ == '__main__':
    Test_group_run_axes()
