# Introduction

The member should be able to: describe how swap contracts are similar to but different from a series of forward contracts, and contrast the value and price of swaps.

## Summary

A swap contract is an agreement between two counterparties to exchange a series of future cash flows, whereas a forward contract is a single exchange of value at a later date., Interest rate swaps are similar to forwards in that both contracts are firm commitments with symmetric payoff profiles and no cash is exchanged at inception, but they differ in that the fixed swap rate is constant, whereas a series of forward contracts has different forward rates at each maturity., A swap is priced by solving for the par swap rate, a fixed rate that sets the present value of all future expected floating cash flows equal to the present value of all future fixed cash flows., The value of a swap at inception is zero (ignoring transaction and counterparty credit costs). On any settlement date, the value of a swap equals the current settlement value plus the present value of all remaining future swap settlements., A swap contract’s value changes as time passes and interest rates change. For example, a rise in expected forward rates increases the present value of floating payments, causing a mark-to-market (MTM) gain for the fixed-rate payer (floating-rate receiver) and an MTM loss for the fixed-rate receiver (floating-rate payer).

## Learning Outcomes

The member should be able to: describe how swap contracts are similar to but different from a series of forward contracts, and contrast the value and price of swaps.

## Technical Note

**Technical Note: Similarities and Differences between Swap Contracts and Forward Contracts**

**Similarities:**

* Firm commitments with symmetric payoff profiles
* No cash exchange at inception

**Key Differences:**

* Swaps involve exchanging a series of cash flows, while forward contracts involve a single exchange.
* Swap contracts have a constant fixed rate, while forward contracts have different forward rates at each maturity.

**Value and Price of Swaps:**

* Swaps are priced by solving for the par swap rate, which equalizes the present value of future floating and fixed cash flows.
* The initial value of a swap is zero, excluding transaction costs and counterparty credit risk.
* The value of a swap changes over time due to changes in interest rates.
* A rise in expected forward rates results in a MTM gain for the fixed-rate payer and a MTM loss for the fixed-rate receiver.

**Table: Key Similarities and Differences between Swaps and Forward Contracts**

| Feature | Swap Contract | Forward Contract |
|---|---|---|
| Type of exchange | Series of cash flows | Single exchange |
| Fixed rate | Constant | Varies with maturity |

**Equation for the Par Swap Rate:**

```
0 = Σ (PV[Fixed Rate Payment]) - Σ (PV[Floating Rate Payment])
```

**Conclusion:**

Swap contracts are similar to but distinct from forward contracts, offering advantages such as flexibility and customization. The value of swaps is determined by the par swap rate and can fluctuate over time based on interest rate movements.