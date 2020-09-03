import pandas as pd
import numpy as np
import scipy
from statsmodels.distributions.empirical_distribution import ECDF
from sklearn.ensemble import RandomForestClassifier
from sklearn.base import clone

def PIMP(rf, X, y, S, random_state, para=False):
    
    baseline_importances = {}
    for col in X.columns:
        baseline_importances[col] = []
    rf.fit(X, y)
    for t in set(zip(X.columns, rf.feature_importances_)):
        baseline_importances[t[0]].append(t[1])
        
        
    permutation_importances = {}
    for col in X.columns:
        permutation_importances[col] = []    
    #Permute the y column S times and compute feature importances
    for i in range(S):
        print('Permutation {} of {}'.format(i+1,S))
        y = np.random.permutation(y)
        rf_clone = clone(rf)
        rf_clone.random_state=random_state
        rf_clone.fit(X, y)
        for t in set(zip(X.columns, rf_clone.feature_importances_)):
            permutation_importances[t[0]].append(t[1])
    df_pimp = pd.DataFrame(permutation_importances)
    
    if para:
        #KS test on each column's distribution and a Gaussian distribution 

        ks_pvalues = {}
        for col in df_pimp:
            mean = df_pimp[col].mean()
            std = df_pimp[col].std()
            ks = scipy.stats.kstest(list(set(df_pimp[col])), scipy.stats.norm.cdf, args=(mean,std))
            ks_pvalues[col] = ks.pvalue

        #p value is the probability of observing the baseline or greater importance score given the distribution
        altmann_p = {}
        for col in df_pimp:
            #loc is mean and scale is std in scipy
            tmp = scipy.stats.norm.cdf(baseline_importances[col], loc=df_pimp[col].mean(), scale=df_pimp[col].std())
            pvalue = 1-tmp
            altmann_p[col] = pvalue
            
        return baseline_importances, df_pimp, ks_pvalues, altmann_p
    
    else:
        
        ecdfs = {}
        for col in df_pimp:
            mean = df_pimp[col].mean()
            std = df_pimp[col].std()
            #step function
            Fn = ECDF(list(df_pimp[col]), side='right')
            ecdfs[col] = Fn
            
        #p value is the probability of observing the baseline or greater importance score given the distribution
        altmann_p={}
        for col in ecdfs:
            tmp = ecdfs[col](baseline_importances[col])
            pvalue = 1-tmp
            altmann_p[col] = pvalue
            
        return baseline_importances, df_pimp, altmann_p