# Introduction



## Summary

Two kinds of observations may potentially influence regression results: (1) a high-leverage point, an observation with an extreme value of an independent variable, and (2) an outlier, an observation with an extreme value of the dependent variable., A measure for identifying a high-leverage point is leverage. If leverage is greater than 3 ( k + 1 _ n ) , where k is the number of independent variables, then the observation is potentially influential., A measure for identifying an outlier is studentized residuals. If the studentized residual is greater than the critical value of the t-statistic with n – k – 2 degrees of freedom, then the observation is potentially influential., Cook’s distance, or Cook’s D (Di), is a metric for identifying influential data points. It measures how much the estimated values of the regression change if observation i is deleted. If D i > 2 √ _ k / n , then it is highly likely to be influential. An influence plot visually presents leverage, studentized residuals, and Cook’s D for each observation., Dummy, or indicator, variables represent qualitative independent variables and take a value of 1 (for true) or 0 (for false) to indicate whether a specific condition applies, such as whether a company belongs to a certain industry sector. To capture n possible categories, the model must include n – 1 dummy variables., An intercept dummy adds to or reduces the original intercept if a specific condition is met. When the intercept dummy is 1, the regression line shifts up or down parallel to the base regression line., A slope dummy allows for a changing slope if a specific condition is met. When the slope dummy is 1, the slope changes to (dj + bj) × Xj, where dj is the coefficient on the dummy variable and bj is the slope of Xj in the original regression line., A logistic regression model is one with a qualitative (i.e., categorical) dependent variable, so logistic regression is often used in binary classification problems, which are common in machine learning and neural networks., To estimate a logistic regression, the logistic transformation of the event probability (P) into the log odds, ln[P/(1 − P)], is applied, which linearizes the relation between the transformed dependent variable and the independent variables., Logistic regression coefficients are typically estimated using the maximum likelihood estimation (MLE) method, and slope coefficients are interpreted as the change in the log odds that the event happens per unit change in the independent variable, holding all other independent variables constant.

## Learning Outcomes

The member should be able to: describe influence analysis and methods of detecting influential data points formulate and interpret a multiple regression model that includes qualitative independent variables formulate and interpret a logistic regression model

## Technical Note

**Summary:**

Influential data points, such as high-leverage points and outliers, can impact regression results. Leverage, studentized residuals, and Cook's distance help identify these points. Dummy variables represent qualitative independent variables and include intercept and slope dummies. Logistic regression models use a log odds transformation of the event probability for binary classification problems.

**Key Points:**

* **Influence Analysis:**
    * High-leverage points have extreme independent variable values.
    * Outliers have extreme dependent variable values.
* **Detecting Influential Data Points:**
    * Leverage > 3(k + 1)/n
    * Studentized residuals > critical t-value
    * Cook's distance > 2√(k/n)
    * Influence plot visualizes these metrics.
* **Qualitative Independent Variables:**
    * Dummy variables represent categories (1 for true, 0 for false).
    * n-1 dummy variables needed for n categories.
* **Intercept Dummy:**
    * Shifts intercept up or down when condition is met.
* **Slope Dummy:**
    * Changes slope when condition is met.
* **Logistic Regression:**
    * Used for binary classification problems.
    * Linearizes relationship between event probability and independent variables.
    * Coefficients represent change in log odds per unit change in independent variable.