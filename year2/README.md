# Year 2 – Systems Programming, Stochastic Processes, and Market Microstructure

Year 2 builds upon the low-level programming and mathematical foundations established in Year 1. The primary focus shifts toward systems programming in C++ and Rust, concurrent programming, basic networking, and foundational financial modeling. This year also introduces more formal probabilistic thinking through stochastic processes and begins the construction of trading system components.

---

## Objectives

- Master core systems-level concepts: concurrency, threads, memory safety, event-driven design
- Transition from C to modern C++ and begin Rust for low-latency, safe systems development
- Understand and implement socket-based networking and event loops
- Study stochastic models and their application in trading and simulation
- Gain deeper insight into market mechanics, order flow, and execution
- Build the foundations of a modular exchange simulator and research environment

---

## Structure

### 1. Notes

Theoretical materials and summaries organized by topic:

- `notes/programming/` – C++17/20, Rust, multithreading, networking (TCP/UDP)
- `notes/systems/` – epoll, memory alignment, ring buffers, profiling tools
- `notes/math/` – stochastic processes, expectations, Markov chains
- `notes/finance/` – market microstructure, latency arbitrage, order types

### 2. Projects

Practical implementations designed to reinforce key concepts:

- Basic TCP/UDP echo servers in C and Rust
- Event-driven order matching engine with simulated latency
- Market replay tool for order flow analysis
- Circular buffer and lock-free queue implementations
- Black-Scholes options pricer (C++)

Each project includes source code, documentation, performance benchmarks, and testing notes.

---

## Key Resources

- **Programming & Systems**
  - *Effective Modern C++ – Scott Meyers*
  - *A Tour of C++ – Bjarne Stroustrup*
  - *The Rust Programming Language – Klabnik & Nichols*
  - *Linux Programming Interface – Kerrisk*
  - *Beej’s Guide to Network Programming*

- **Math & Stochastics**
  - *Introduction to Stochastic Processes – Ross*
  - *Introduction to Probability Models – Sheldon Ross*
  - *Markov Chains and Mixing Times – Levin, Peres*

- **Finance**
  - *Trading and Exchanges – Larry Harris* (continuation)
  - *Latency Arbitrage, Market Design, and Market Efficiency – Budish et al.*
  - *Introduction to Financial Markets – Coursera/Yale*

---

## Expected Outcomes

By the end of Year 2, the learner should be able to:

- Write high-performance, thread-safe code in C++ and Rust
- Design and benchmark non-blocking I/O systems using `epoll` and raw sockets
- Analyze real-time market behavior through replay and simulation tools
- Understand and model random processes relevant to finance and queuing
- Construct basic infrastructure components of a trading system

---

## Notes

- All projects in Year 2 are written in C++ and/or Rust, compiled with strict optimization flags
- Network code follows raw socket interfaces (IPv4/IPv6) and profiles latency behavior
- Mathematical modeling is tied directly to simulation and analysis of trading behaviors
