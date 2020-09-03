# PIMP-Python [![DOI](https://zenodo.org/badge/292594530.svg)](https://zenodo.org/badge/latestdoi/292594530)
This repository contains a functionally equivalent reimplementation of the PIMP algorithm by Altmann et al. (https://academic.oup.com/bioinformatics/article/26/10/1340/193348) as found in the Vita library available for R (https://cran.r-project.org/web/packages/vita/index.html). 

The aim is to evolve this reimplementation into a fully equivalent implementation of the original algorithm as proposed by Altmann et al., found at http://www.altmann.eu/documents/PIMP.R

The motivation for this reimplementation is given by the considerable speed advantages of running this code in Python. On a test data set composed of almost half a million observations, the expected running time of the Vita version is of 26 hours, while our reimplementation computes the results in ~50 minutes. 

Source code for the Vita version, Altmann's version and our own reimplementation is provided in this repository for ease of comparison. We have currently tested our own reimplementation with respect to the output provided by the Vita implementation on a small dataset, with an absolute tolerance for error of 1e-10, and have found that the outputs are functionally equivalent.

Our implementation in Python requires Pandas, Numpy, Scipy, Scikit-learn and Statsmodels to work.

This being said, THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
