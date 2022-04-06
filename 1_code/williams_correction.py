#!/usr/bin/env python
# coding: utf-8

# ***William's correction for small ns.***
# like so: q=1+(n{[1/(row 1 total)]+…+[1/(row R total)]}−1)(n{[1/(column 1 total)]+…[1/(column C total)]}−1)/ 6n(R−1)(C−1) 

# In[1]:

#import numpy and chi2
import numpy as np
from scipy.stats import chi2

#define the correction as a function
def williams_correction(obs, chiobs):
    #William's Correction
            # as calculated in R's package: Tests, function: DescTools
            ## https://rdrr.io/cran/DescTools/src/R/Tests.r
            
            n = np.sum(obs, axis = None)
            nrows = obs.shape[0]#count of rows
            ncols = obs.shape[1]#count of columns
            williams_deffre = (nrows - 1)*(ncols -1)
            
            
            # row_total = col_total = 0
            # for i in range(nrows):
            #     row_total = row_total + 1 / ( sum( obs[i,:] )
            #                                 ) 
            # for j in range(ncols):
            #     col_total = col_total + 1 / ( sum( obs[:,j] )
            #                                 ) 
            #without loops:
            row_total = sum(1/x for x in obs.sum(axis=0))
            col_total = sum(1/x for x in obs.sum(axis=1))
                
            q = 1 + ( (n*row_total - 1) * (n*col_total - 1 ) ) / (6*n*williams_deffre)
            
            williams_chi = chiobs / q
            williams_pvalue = chi2.sf(williams_chi, williams_deffre)
            return williams_chi, williams_pvalue, williams_deffre


# In[ ]:




