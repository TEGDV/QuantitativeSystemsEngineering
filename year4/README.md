# Year 4 – Low-Latency Architecture, Signal Research, and Execution Optimization

Year 4 focuses on building ultra-low-latency infrastructure, advanced signal development, and optimized execution strategies. You will dive deeper into CPU and network internals, apply advanced time-series and statistical tools, and begin developing components that mirror production-grade HFT systems. This year bridges research and engineering, preparing you to compete with top talent in high-performance financial environments.

---

## Objectives

- Develop low-latency, event-driven infrastructure with nanosecond-level profiling
- Learn network optimization techniques including kernel bypass, zero-copy I/O, and PTP synchronization
- Implement robust signal engines based on time-series modeling, filters, and feature engineering
- Build a high-performance execution layer with dynamic throttling and risk-aware trade control
- Study and implement predictive modeling techniques for high-frequency signals

---

## Structure

### 1. Notes

Focused theoretical and research-oriented notes:

- `notes/infra/` – Linux networking, DPDK, kernel tuning, hardware timers
- `notes/math/` – time-series analysis, Kalman filters, spectral analysis
- `notes/finance/` – advanced execution strategies, market impact models
- `notes/ml/` – feature extraction, model validation, online learning

### 2. Projects

Performance-critical systems and signal research tools:

- Nanosecond-resolution logger using `rdtsc` and hardware timers
- Multicast market data receiver with lock-free queues
- Dynamic execution engine with risk guardrails and throttling logic
- Signal engine using exponential moving averages, FFTs, Kalman filters
- Latency-aware order router with venue selection and fallback logic
- Integrated simulation-research pipeline (tick data + model generation)

All projects are developed with a focus on deterministic latency, modularity, and production-readiness. Unit, integration, and latency regression tests are included.

---

## Key Resources

- **Systems & Latency Engineering**
  - *DPDK Documentation and Samples*
  - *Understanding Linux Network Internals – Benvenuti*
  - *Agner Fog’s CPU Optimization Manuals*
  - *Precision Time Protocol (IEEE 1588) specs*

- **Math & Time Series**
  - *Time Series Analysis and Its Applications – Shumway & Stoffer*
  - *Forecasting: Principles and Practice – Hyndman & Athanasopoulos*
  - *Applied Kalman Filtering – Grewal & Andrews*

- **Machine Learning (Targeted Use)**
  - *Vowpal Wabbit* documentation and tutorials
  - *Online Learning and Concept Drift* whitepapers

- **Finance**
  - *Algorithmic and High-Frequency Trading – Cartea et al.*
  - *Execution and Market Impact – Kissell*
  - *Research from SIG, Jane Street, Jump Trading (blog/papers)*

---

## Expected Outcomes

By the end of Year 4, the learner should be able to:

- Build and benchmark sub-microsecond trading system components
- Develop and test statistical and signal-processing-based alpha models
- Optimize data pipelines, memory alignment, and network stack behavior
- Integrate trading strategies into a live-testing or paper-trading environment
- Analyze market microstructure effects on signal decay and execution risk

---

## Notes

- Hardware profiling tools (`perf`, `ftrace`, `flamegraph`, `hwloc`) are used consistently
- Projects simulate realistic exchange behavior using historical data with nanosecond timestamps
- Rust and C++ are used in combination, leveraging FFI where appropriate for performance vs. safety tradeoffs
