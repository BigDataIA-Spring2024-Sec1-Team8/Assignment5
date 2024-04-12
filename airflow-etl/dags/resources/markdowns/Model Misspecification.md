# Introduction



## Summary

Principles for proper regression model specification include economic reasoning behind variable choices, parsimony, good out-of-sample performance, appropriate model functional form, and no violations of regression assumptions., Failures in regression functional form are typically due to omitted variables, inappropriate form of variables, inappropriate variable scaling, and inappropriate data pooling; these may lead to the violations of regression assumptions., Heteroskedasticity occurs when the variance of regression errors differs across observations. Unconditional heteroskedasticity is when the error variance is not correlated with the independent variables, whereas conditional heteroskedasticity exists when the error variance is correlated with the values of the independent variables., Unconditional heteroskedasticity creates no major problems for statistical inference, but conditional heteroskedasticity is problematic because it results in underestimation of the regression coefficients’ standard errors, so t-statistics are inflated and Type I errors are more likely., Conditional heteroskedasticity can be detected using the Breusch–Pagan (BP) test, and the bias it creates in the regression model can be corrected by computing robust standard errors., Serial correlation (or autocorrelation) occurs when regression errors are correlated across observations and may be a serious problem in time-series regressions. Serial correlation can lead to inconsistent coefficient estimates, and it underestimates standard errors, so t-statistics are inflated (as with conditional heteroskedasticity)., The Breusch–Godfrey (BG) test is a robust method for detecting serial correlation. The BG test uses residuals from the original regression as the dependent variable run against initial regressors plus lagged residuals, and H0 is the coefficients of the lagged residuals are zero., The biased estimates of standard errors caused by serial correlation can be corrected using robust standard errors, which also correct for conditional heteroskedasticity., Multicollinearity occurs with high pairwise correlations between independent variables or if three or more independent variables form approximate linear combinations that are highly correlated., Multicollinearity results in inflated standard errors and reduced t-statistics., The variance inflation factor (VIF) is a measure for quantifying multicollinearity. If VIFj is 1 for Xj, then there is no correlation between Xj and the other regressors. VIFj > 5 warrants further investigation, and VIFj > 10 indicates serious multicollinearity requiring correction., Solutions to multicollinearity include dropping one or more of the regression variables, using a different proxy for one of the variables, or increasing the sample size.

## Learning Outcomes

The member should be able to: describe how model misspecification affects the results of a regression analysis and how to avoid common forms of misspecification explain the types of heteroskedasticity and how it affects statistical inference explain serial correlation and how it affects statistical inference explain multicollinearity and how it affects regression analysis

## Technical Note

**Summary:**

Proper model specification in regression analysis is crucial to ensure accurate results. Misspecification can arise from omitted variables, inappropriate variable forms, scaling, or data pooling. Heteroskedasticity, where error variance differs across observations, can inflate Type I errors if conditional (correlated with independent variables). Serial correlation, where errors correlate across observations, also inflates standard errors and t-statistics. Multicollinearity, where independent variables are highly correlated, results in inflated standard errors and reduced t-statistics.

**Key Points:**

**Heteroskedasticity:**

* Occurs when error variance differs across observations.
* Conditional heteroskedasticity is problematic, leading to underestimation of standard errors and inflated t-statistics.
* Can be detected using the Breusch–Pagan test and corrected using robust standard errors.

**Serial Correlation:**

* Occurs when errors are correlated across observations.
* Can lead to inconsistent coefficient estimates and inflated standard errors.
* Can be detected using the Breusch–Godfrey test and corrected using robust standard errors.

**Multicollinearity:**

* Occurs when independent variables are highly correlated.
* Results in inflated standard errors and reduced t-statistics.
* Can be quantified using the Variance Inflation Factor (VIF).
* Solutions include dropping variables, using different proxies, or increasing sample size.

**Avoiding Misspecification:**

* Consider economic reasoning, parsimony, out-of-sample performance, appropriate functional form, and no violations of regression assumptions.
* Test for and correct heteroskedasticity and serial correlation using robust standard errors.
* Assess multicollinearity using VIF and address it appropriately.