### Simulations on Koala's Historical Data: An Overview

#### Scope of Data
- Only policies that have expired are considered in the simulation.

#### Risk Modules in Focus
- The simulations focus only on two specific risk modules. These correspond to the two most frequently observed loss probabilities in the historical records.
  - **First loss probability**: 0.1103
  - **Second loss probability**: 0.1208

#### Sampling Methodology
- The sample size for each simulation is set to be 20% of the total number of policies. These policies are selected randomly.

#### Temporal Aggregation
- The simulations aggregate policies in 10-day intervals. This means that every single step in the simulations represents a span of 10 days.

#### Policy Details
- Key attributes of the selected policies (like the payout amount, start date, duration, and outcome) are retained as per the historical data, without any randomization.

#### Margin of Conservatism (MoC)
- All the policies in the simulations are subject to a consistent Margin of Conservatism (MoC) set at 1.15. This is applied uniformly across the board.
