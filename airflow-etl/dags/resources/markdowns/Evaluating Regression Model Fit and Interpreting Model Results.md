# Introduction



## Summary

In multiple regression, adjusted R2 is used as a measure of model goodness of fit since it does not automatically increase as independent variables are added to the model. Rather, it adjusts for the degrees of freedom by incorporating the number of independent variables., Adjusted R2 will increase (decrease) if a variable is added to the model that has a coefficient with an absolute value of its t-statistic greater (less) than 1.0., Akaike’s information criterion (AIC) and Schwarz’s Bayesian information criteria (BIC) are also used to evaluate model fit and select the “best” model among a group with the same dependent variable. AIC is preferred if the purpose is prediction, BIC is preferred if goodness of fit is the goal, and lower values of both measures are better., Hypothesis tests of a single coefficient in a multiple regression, using t-tests, are identical to those in simple regression., The joint F-test is used to jointly test a subset of variables in a multiple regression, where the “restricted” model is based on a narrower set of independent variables nested in the broader “unrestricted” model. The null hypothesis is that the slope coefficients of all independent variables outside the restricted model are zero., The general linear F-test is an extension of the joint F-test, where the null hypothesis is that the slope coefficients on all independent variables in the unrestricted model are equal to zero., Predicting the value of the dependent variable using an estimated multiple regression model is similar to that in simple regression. First, sum, for each independent variable, the estimated slope coefficient multiplied by the assumed value of that variable, and then add the estimated intercept coefficient., In multiple regression, the confidence interval around the forecasted value of the dependent variable reflects both model error and sampling error (from forecasting the independent variables); the larger the sampling error, the larger is the standard error of the forecast of Y and the wider is the confidence interval.

## Learning Outcomes

The member should be able to: evaluate how well a multiple regression model explains the dependent variable by analyzing ANOVA table results and measures of goodness of fit formulate hypotheses on the significance of two or more coefficients in a multiple regression model and interpret the results of the joint hypothesis tests calculate and interpret a predicted value for the dependent variable, given the estimated regression model and assumed values for the independent variable

## Technical Note

**Summary:**

- Adjusted R2 measures model fit without automatically increasing as variables are added.
- AIC and BIC are used to compare models and select the best one based on prediction or goodness of fit.
- Single-coefficient hypotheses are tested using t-tests, as in simple regression.
- Joint F-tests jointly test multiple coefficients, comparing restricted and unrestricted models.
- General linear F-tests test the equality of all coefficients to zero.
- Predicted dependent variable values are calculated by multiplying coefficients by corresponding independent variable values and adding the intercept.
- Confidence intervals around predicted values reflect both model and sampling error.