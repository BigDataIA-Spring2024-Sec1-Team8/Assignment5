# Introduction

The member should be able to: explain how to value a derivative using a one-period binomial model, and describe the concept of risk neutrality in derivatives pricing.

## Summary

The one-period binomial model values contingent claims, such as options, and assumes the underlying asset will either increase by Ru (up gross return) or decrease by Rd (down gross return) over a single period that corresponds to the expiration of the derivative contract., The binomial model combines an option with the underlying asset to create a risk-free portfolio in which the proportion of the option to the underlying security is determined by a hedge ratio., The hedged portfolio must earn the prevailing risk-free rate of return; otherwise, riskless arbitrage profit opportunities would be available., Valuing a derivative through risk-free hedging is equivalent to computing the discounted expected payoff of the option using risk-neutral probabilities rather than actual probabilities., Neither the actual (real-world) probabilities of underlying price increases or decreases nor the expected return of the underlying are required to price an option., The one-period binomial model can be extended to multiple periods as well to value more complex contingent claims.

## Learning Outcomes

The member should be able to: explain how to value a derivative using a one-period binomial model, and describe the concept of risk neutrality in derivatives pricing.

## Technical Note

**Technical Note: One-Period Binomial Model and Risk Neutrality**

**Summary:**

* **One-Period Binomial Model:** Values derivatives assuming the underlying asset can only move up or down by specific percentages (Ru and Rd) over a single period.
* **Hedge Ratio:** Determines the proportion of the option to the underlying asset needed to create a risk-free portfolio.
* **Risk-Free Rate:** The portfolio must earn the risk-free rate to prevent arbitrage opportunities.
* **Risk-Neutral Probabilities:** Used to calculate the expected payoff of the option, replacing actual probabilities.
* **Risk Neutrality:** Neither actual probabilities nor underlying asset expectations are required for pricing.
* **Multi-Period Extension:** The binomial model can be extended to multiple periods to value more complex derivatives.

**Equation:**

```
Option Price = e^(-rf*T) * [(Pu * Value(S(u,T)) + Pd * Value(S(d,T))]
```

where:

* rf is the risk-free rate
* T is the time to maturity
* Pu and Pd are the risk-neutral probabilities
* S(u,T) and S(d,T) are the up and down values of the underlying asset at maturity

**Table: Binomial Model Variables**

| Variable | Description |
|---|---|
| Ru | Up gross return |
| Rd | Down gross return |
| Pu | Risk-neutral probability of up move |
| Pd | Risk-neutral probability of down move |