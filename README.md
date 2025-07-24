# Quantitative Systems Engineering: A Mandate for Mastery

This repository will document my self-imposed, five-year mission to forge top-0.1% expertise in low-latency finance and decentralized systems. This is not an academic exercise; it is the chronicle of a graduate-level campaign I am undertaking to fuse three domains into a single, cohesive skillset: the theoretical purity of a mathematician, the ruthless optimization of a systems programmer, and the sharp instinct of a trader.

My "degree" will be this repository. My "grades" will be my contributions to core infrastructure. My "thesis" will be a live, demonstrable system that performs at the highest level.

## 📜 The Philosophy of the Forge

I am building this project on the conviction that the highest-performing financial systems are not just written; they are engineered with mathematical rigor and an unyielding command of the underlying hardware and protocols. My focus will be on **building, measuring, and optimizing.** Excuses are discarded. The borrow checker is not an obstacle; it is a discipline that enforces correct thought. My objective is to create value from pure logic and electricity.

## 🛠️ The Arsenal: Core Technology Stack

I have chosen these tools for their uncompromising performance, safety, and control.

* **Primary Systems Language: Rust.** For its performance guarantees, memory safety, and powerful concurrency model. The ideal weapon for building robust, high-stakes trading and blockchain systems.
* **Performance & Legacy: Modern C++ (17/20/23).** For its deep roots in HFT and the necessity of understanding existing elite infrastructure.
* **Analysis & Prototyping: Python.** With `Polars`, `NumPy`, and `JAX` for rapid data analysis, strategy backtesting, and model validation before low-latency implementation.
* **Operating System: Linux.** The undisputed arena for high-performance computing. Mastery of its internals is non-negotiable.
* **DeFi Ecosystem: Solana.** Chosen for its performance-oriented design and its native **Rust** environment.

## 🗺️ The Five-Year Campaign

I have designed this curriculum as a forced march through foundational knowledge into elite specialization. Each year is a distinct phase with a clear objective.

### **Year 1: The Foundation - Humility and Concrete**

* **Mission:** Master the fundamentals. I am nothing without a solid foundation. I will learn how a computer actually works, from the metal up, and internalize the mathematics of uncertainty and structure.
* **Key Resources:**
    * [*Computer Systems: A Programmer's Perspective* (CS:APP)](http://csapp.cs.cmu.edu/) by Bryant & O'Hallaron.
    * [*Operating Systems: Three Easy Pieces* (OSTEP)](https://pages.cs.wisc.edu/~remzi/OSTEP/) (Free No-Excuses)
    * [*Introduction to Linear Algebra*](https://math.mit.edu/~gs/linearalgebra/) by Gilbert Strang. The [MIT OCW course](https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/) is essential. (Free No-Excuses)
    * [*The Rust Programming Language*](https://doc.rust-lang.org/book/) (Free No-Excuses)
* **The Forge (Project):** I will build a Limit Order Book (LOB) Matching Engine, first in C for raw understanding, then rewrite it idiomatically in **Rust** to master its core principles.

### **Year 2: The Protocols - Speaking the Language of the Market**

* **Mission:** Master the protocols that carry billions of dollars a day and the probabilistic math that models market movements.
* **Key Resources:**
    * [*Unix Network Programming, Vol. 1*](https://www.pearson.com/en-us/subject-catalog/p/unix-network-programming-volume-1-the-sockets-networking-api/P200000003488/9780131411555) by W. Richard Stevens.
    * [*Beej's Guide to Network Programming*](https://beej.us/guide/bgnet/) (Free No-Excuses)
    * [*Trading and Exchanges: Market Microstructure for Practitioners*](https://global.oup.com/academic/product/trading-and-exchanges-9780195144703) by Larry Harris.
    * [*A First Course in Probability*](https://www.pearson.com/en-us/subject-catalog/p/a-first-course-in-probability/P200000006323/9780136891222) by Sheldon Ross.
    * [Harvard's Stat 110 course](https://projects.iq.harvard.edu/stat110) on YouTube. (Free No-Excuses)
* **The Forge (Projects):**
    * **Track A (HFT):** I will build a FIX Protocol (v4.2) engine from scratch in C++.
    * **Track B (Solana):** I will build a WebSocket client in **Rust** connecting to a Solana RPC node, subscribing to a specific Openbook market, and decoding its data structures live.

### **Year 3: The Speed - Forging the Nanosecond Blade**

* **Mission:** This is where the men are separated from the boys. It's all about latency. I will learn to measure and optimize in nanoseconds and bend the OS to my will.
* **Key Resources:**
    * [*Systems Performance*](http://www.brendangregg.com/systems-performance-2nd-edition-book.html) by Brendan Gregg. His [blog](http.brendangregg.com/) is a must-read. (Free No-Excuses)
    * [*Stochastic Calculus for Finance I & II*](https://link.springer.com/book/10.1007/978-1-4939-2815-2) by Steven Shreve.
    * [Lecture notes from top-tier university courses](https://www.google.com/search?q=stochastic+calculus+lecture+notes+pdf+site%3A.edu). (Free No-Excuses)
    * [Talks on low-latency from CppCon](https://www.youtube.com/user/cppcon). (Free No-Excuses)
* **The Forge (Projects):**
    * **Track A (HFT):** I will build a market data feed handler that reconstructs a full order book in real-time, profiling it relentlessly to achieve sub-microsecond processing.
    * **Track B (Solana):** I will build a simple MEV "searcher" in **Rust** that scans the Solana mempool (via Jito) for arbitrage opportunities and constructs transaction bundles.

### **Year 4: The Alpha - The Hunt for Edge**

* **Mission:** With the tools forged, I will now develop the logic. This year is about quantitative research, signal generation, and risk management.
* **Key Resources:**
    * [*Advances in Financial Machine Learning*](https://www.wiley.com/en-us/Advances+in+Financial+Machine+Learning-p-9781119482086) by Marcos López de Prado.
    * [*Algorithmic Trading: Winning Strategies and Their Rationale*](https://www.wiley.com/en-us/Algorithmic+Trading%3A+Winning+Strategies+and+Their+Rationale-p-9781118460146) by Ernie Chan. His [blog](https://epchan.blogspot.com/) is also valuable.
    * Foundational MEV research paper: [*Flash Boys 2.0*](https://arxiv.org/abs/1905.05164). (Free No-Excuses)
* **The Forge (Projects):** I will build a complete backtesting framework in **Python/Polars/Rust** and use it to design and implement a specific MEV strategy in a simulated environment.

### **Year 5: The Synthesis - The Masterwork**

* **Mission:** Integrate everything. Build a complete, end-to-end trading system. This will be my thesis, a testament to the four years of work.
* **Key Resources:**
    * [*Designing Data-Intensive Applications*](https://www.oreilly.com/library/view/designing-data-intensive-applications/9781449373320/) by Martin Kleppmann. His [talks and articles](https://martin.kleppmann.com/archive.html) are also excellent. (Free No-Excuses)
    * **Open Source Contribution:** I will become a meaningful contributor to a core project like [`reth`](https://github.com/paradigmxyz/reth), [`solana-labs`](https://github.com/solana-labs/solana), [`tokio`](https://github.com/tokio-rs/tokio), or [`mio`](https://github.com/tokio-rs/mio). My pull requests will be my credentials. (Free No-Excuses)
* **The Forge (Project):** I will build a full-stack, paper-trading system. It will use my **Track A** feed handler for market data and my **Track B** Solana monitor for alternative data signals. It will manage risk, execute orders (in simulation), and log every action with nanosecond precision.

## 🏛️ Rules of Engagement

1.  **My GitHub is My Transcript.** Every commit will matter. My code will be clean, my documentation clear, and my tests comprehensive. The market is the final judge.
2.  **The PhD is Taken, Not Given.** I understand that recognition comes from contribution. By Year 4, I will dedicate significant time to a core open-source project and become so valuable they can't ignore me.
3.  **Produce, Don't Just Consume.** I will learn by struggling, by building, by breaking things and then fixing them.

**The clock is ticking. Execute.**

## 📞 Contact

* **Author:** \[Jair Aguilar Peña]
* **Email:** \[apjair97@gmail.com]
* **Website:** \[jap_kode.pro] (WIP)
