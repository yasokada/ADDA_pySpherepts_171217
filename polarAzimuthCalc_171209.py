import numpy as np
import sys

'''
v0.3 Dec. 17, 2017
    - refactor > rename functions by adding "_rad"
    - refactor > add function comment
v0.2 Dec. 10, 2017
    - fix bug: calc_gamma_rad() was too complicated
        _+ use arctan2()
    - add Test_group_run_random()
v0.1 Dec. 09, 2017
    - add Test_group_run_axes()
    - add calc_gamma_rad()
    - add calc_beta_rad()
'''


def calc_beta_rad(pvec):
    '''
    polar angle [0, pi]
    '''
    return np.arccos(pvec[2])  # arccos:[0, pi]


def calc_gamma_rad(pvec):
    '''
    azimuth angle [0, 2pi]
    '''
    gamma = np.arctan2(pvec[1], pvec[0])
    if gamma < 0.0:
        gamma += 2 * np.pi
    return gamma


def Test_group_run_axes():
    pvecs = [
        [0, 0, 1],  # z direction
        [0, 0, -1],  # z direction
        [0, 1, 0],  # y direction
        [0, -1, 0],  # y direction
        [1, 0, 0],  # x direction
        [-1, 0, 0],  # x direction
        ]
    for elem in pvecs:
        beta_rad = calc_beta_rad(elem)
        gamma_rad = calc_gamma_rad(elem)

        fmt = "{0} \tbeta:{1:.5f} gamma:{2:.5f}"
        msg = fmt.format(elem, beta_rad, gamma_rad)
        print(msg)


def Test_calc_xyz(beta_rad, gamma_rad):
    rad = 1.0  # radius
    resx = rad * np.cos(gamma_rad) * np.sin(beta_rad)
    resy = rad * np.sin(gamma_rad) * np.sin(beta_rad)
    resz = rad * np.cos(beta_rad)
    return resx, resy, resz


def Test_group_run_random():
    bt_stp = np.pi / 4.0  # beta step
    gm_stp = np.pi / 4.0  # gamma step
    for bt_in in np.arange(0.0, np.pi, bt_stp):
        for gm_in in np.arange(0.0, 2 * np.pi, gm_stp):
            # print(bt_in, gm_in)
            wrk = Test_calc_xyz(bt_in, gm_in)
            bt_out = calc_beta_rad(wrk)
            gm_out = calc_gamma_rad(wrk)
            if abs(gm_in - gm_out) > sys.float_info.epsilon:
                print("%+.5e" % (gm_in - gm_out), end=' ')
                print("NG:", end=" ")
            else:
                continue
            msg = ','.join("%+.5f" % elem for elem in wrk)
            print(msg, end=' -- ')
            fmt = "b{0:.5f} b{1:.5f} g{2:.5f} g{3:.5f}"
            msg = fmt.format(bt_in, bt_out, gm_in, gm_out)
            print(msg)


if __name__ == '__main__':
    Test_group_run_random()
    #Test_group_run_axes()
