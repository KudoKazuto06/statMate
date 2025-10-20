# Verified statistical computation functions

import pandas as pd
from scipy import stats
import numpy as np

def independent_ttest(df, col1, col2):
    stat, p = stats.ttest_ind(df[col1], df[col2], nan_policy='omit')
    return f"Independent t-test between {col1} and {col2}: t = {stat:.3f}, p = {p:.3f}"

def paired_ttest(df, col1, col2):
    stat, p = stats.ttest_rel(df[col1], df[col2], nan_policy='omit')
    return f"Paired t-test between {col1} and {col2}: t = {stat:.3f}, p = {p:.3f}"

def correlation(df, col1, col2):
    r, p = stats.pearsonr(df[col1], df[col2])
    return f"Pearson correlation between {col1} and {col2}: r = {r:.3f}, p = {p:.3f}"

def anova(df, *cols):
    samples = [df[c].dropna() for c in cols]
    stat, p = stats.f_oneway(*samples)
    return f"One-way ANOVA for {cols}: F = {stat:.3f}, p = {p:.3f}"

def describe(df):
    return str(df.describe())