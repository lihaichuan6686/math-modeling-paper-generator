# Queuing Models Card

Purpose: support service-system analysis where arrivals, waiting, capacity, utilization, and delay determine performance.

## Use When

- The problem involves customers, vehicles, patients, jobs, packets, machines, or requests waiting for service.
- Arrival and service processes can be estimated or assumed transparently.
- Capacity decisions depend on waiting time, utilization, or congestion.
- Simulation or queueing formulas can validate operational recommendations.

## Avoid When

- Arrival or service data are absent and assumptions would dominate the result.
- The system has strong priority, blocking, batching, or network behavior but the model treats it as simple M/M/1 without justification.
- The objective is spatial routing or scheduling rather than waiting-system design.

## Required Inputs

- Arrival rate or arrival-time data.
- Service-time distribution or service rate.
- Number of servers.
- Queue discipline: FCFS, priority, batch, loss system, or finite capacity.
- Performance targets such as mean wait, queue length, or service level.

## Mathematical Objects

M/M/1 examples:

```text
rho = lambda / mu
L = rho / (1 - rho)
W = 1 / (mu - lambda)
```

Multi-server or complex systems may require discrete-event simulation.

## Outputs

- Utilization.
- Average waiting time.
- Average queue length.
- Service-level probability.
- Capacity recommendation.

## Figure and Table Expectations

- System flow diagram.
- Arrival/service distribution plots.
- Utilization and waiting-time table.
- Capacity-vs-wait curve.
- Simulation distribution plot if stochastic simulation is used.

## Validation

- Check stability condition such as `lambda < c mu`.
- Compare formula results with simulation for complex cases.
- Run sensitivity over arrival and service rates.
- Report assumptions about arrival and service distributions.
- Check peak-period behavior, not only averages.

## CUMCM Writing Pattern

1. Map the real system into arrivals, service, servers, and queue discipline.
2. Estimate or justify rates.
3. Apply analytic formulas or simulation.
4. Present capacity-performance tradeoff.
5. Recommend a configuration with stress tests.

## Common Risks

- Using M/M/1 automatically without checking assumptions.
- Ignoring peak periods.
- Confusing utilization with service quality.
- No stability check.
- Missing finite-capacity or priority effects.

## Review Checks

- Are arrival and service assumptions documented?
- Is the model stable?
- Is capacity recommendation tied to a target?
- Are stochastic variations shown?
- Are peak and average conditions distinguished?
