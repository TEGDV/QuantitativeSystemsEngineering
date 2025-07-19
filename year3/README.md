# Year 3 – Financial Engineering, Real-Time Systems, and Infrastructure Design

Year 3 transitions from foundational systems and math into full-stack financial engineering. You will design and implement real-time market data infrastructure, extend your mathematical toolkit with numerical methods and optimization, and begin working with financial models and execution logic. This year emphasizes integration: connecting low-latency components, analytics, and execution into a cohesive research and trading engine.

---

## Objectives

- Build a modular real-time backtesting and simulation framework
- Learn and apply numerical optimization techniques for model fitting
- Design and implement financial indicators, signal engines, and execution logic
- Explore distributed and concurrent architecture for strategy deployment
- Strengthen knowledge of financial derivatives, volatility modeling, and risk metrics
- Build confidence in performance-aware software design (caching, memory locality, branch prediction)

---

## Structure

### 1. Notes

Deeper theoretical topics are organized by domain:

- `notes/math/` – numerical methods, convex optimization, risk metrics
- `notes/finance/` – derivative pricing, volatility surfaces, order flow analysis
- `notes/systems/` – concurrency models, memory layout, SIMD, performance tuning
- `notes/infra/` – event buses, message passing, in-memory databases

### 2. Projects

High-level system components and quantitative tools:

- Modular backtest engine with plug-in strategy support
- Real-time market data processor and order book snapshot tool
- Execution engine with simulated slippage and PnL tracking
- Volatility estimator (historical, implied) with visualization
- Risk dashboard for live metrics (Sharpe ratio, drawdown, latency histogram)
- Strategy simulator for stat arb and mean-reversion

Projects are written in C++, Rust, and Python (for analytics) with clear separation between data ingestion, signal generation, and execution.

---

## Key Resources

- **Math & Optimization**
  - *Convex Optimization – Boyd & Vandenberghe*
  - *Numerical Analysis – Burden & Faires*
  - *Introduction to Statistical Learning – James et al.*

- **Finance**
  - *Options, Futures, and Other Derivatives – Hull*
  - *Volatility Trading – Sinclair*
  - *Quantitative Trading – Chan*

- **Systems & Design**
  - *Systems Performance – Brendan Gregg*
  - *Designing Data-Intensive Applications – Kleppmann*
  - *Mechanical Sympathy Blog – Martin Thompson*

---

## Expected Outcomes

By the end of Year 3, the learner should be able to:

- Design and implement complete real-time trading simulation engines
- Optimize performance at the system level (branch prediction, cache optimization)
- Quantify and track financial metrics in simulation environments
- Implement and evaluate statistical arbitrage and volatility-based models
- Understand and apply numerical techniques for calibration and optimization

---

## Notes

- This year represents the transition from isolated system components to fully integrated infrastructure
- Core trading strategies are implemented and tested under realistic market data conditions
- Projects are benchmarked using `perf`, latency profilers, and real data samples from open exchange APIs (Polygon, IEX, Binance)
