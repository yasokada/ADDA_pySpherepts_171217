Updated: Feb. 07, 2018

### ADDA_pySpherepts_171217

A tool to obtain the [beta_gamma.tbl] using [the pySpherepts package](https://github.com/yasokada/pySpherepts_171126/).


### Files

- polarAzimuthCalc_171209.py
    - a main script
    - to calculate [beta] and [gamma] from the [x,y,z] values
- make_beta_gamma_tbl_pySphere_171217.py
    - sample script to obtain [beta_gamma.tbl] for
        - IcosNodes
        - HammersleyNodes
        - FibonacciNodes

`test_XXX.py` scripts are prepared to show how to use the main script.

### How to use

After the setup of the [pySpherepts](https://github.com/yasokada/pySpherepts_171126/), copy the following files to the same directory.

- polarAzimuthCalc_171209.py
- make_beta_gamma_tbl_pySphere_171217.py

Then, execute the following'

```bash
$ python3 make_beta_gamma_tbl_pySphere_171217.py 
[beta_gamma_gIN.tbl] is created
[beta_gamma_gHN.tbl] is created
[beta_gamma_gFN.tbl] is created
```

### Example plot

Using the `plot_beta_gamma_171217.ipynb` on the [Jupyter Notebook](http://jupyter.org/), the beta_gamma table can be plotted in 2D.

See [plot_beta_gamma_171217.ipynb](https://github.com/yasokada/ADDA_pySpherepts_171217/blob/master/plot_beta_gamma_171217.ipynb) on the GitHub project.


### How to use with ADDA

The [beta_gamma_XXX.tbl] can be used with a script named [loop_beta_gamma_171216.py](https://qiita.com/7of9/items/5c52189aba265d4c9d09).

