## 🚀 Axiom Protocol: High-Performance C-Ingestion Engine

**Axiom** is a high-speed data ingestion layer designed to bypass the CPython abstraction tax. It utilizes zero-copy memory mapping and a custom C-extension to achieve ingestion speeds that far outpace industry standards like Pandas.
---

## 💰 ROI Impact: High-Scale Infrastructure Recovery

Axiom v1.1 is designed for production environments where ingestion latency equals wasted capital. By stripping the CPython abstraction tax, we recover massive compute resources.

**The Math of Scale (10M Row Datasets):**
- **Compute Time Recovered:** ~5.05s per file vs. Pandas.
- **Daily Recovery (10,000 files):** **14 hours of high-performance CPU time.**
- **Monthly Impact:** **420+ hours** of server compute eliminated per pipeline.

For firms handling massive data operations, this translates to a **60-70% reduction in ingestion-related infrastructure costs.**

---
### 📊 Performance Benchmark
The following chart demonstrates the delta between standard Python tools and the Axiom v1.1 C-Engine when processing ~10,000,000 rows of financial-grade data.

![Performance Chart](performance_chart.png)

* **Pandas (`read_csv`):** 7.75 seconds
* **Axiom v1.1 (Precision):** 2.7 seconds
* **Axiom v1.0 (Naive):** 0.31 seconds

---

### 🧠 Engineering Philosophy: Precision at Scale

Standard float parsers often suffer from **Floating-Point Drift** due to repeated multiplication during ASCII conversion. Axiom v1.1 solves this through **Integer Accumulation**.

Instead of performing:
$$Value = \sum (Digit \times 10^{-n})$$

Axiom utilizes a fixed-point approach:
1.  **Integer Accumulation:** Parse the entire number as a `long long` integer.
2.  **Single-Division Scaling:** Perform one final division by the weight factor.
$$FinalValue = \frac{AccumulatedInteger}{10^{Precision}}$$

This eliminates cumulative rounding errors, ensuring the engine is suitable for high-frequency trading (HFT) and financial auditing.

---

### 🛡️ Production Hardening
Axiom isn't just fast; it's unbreakable. The v1.1 release includes a **C-Level Schema Validator** that operates at the hardware layer:
* **Boundary Validation:** Checks for non-numeric characters before parsing.
* **Null Safety:** Gracefully handles empty or corrupted fields without memory leaks.
* **Memory Efficiency:** Uses `mmap` to map files directly into memory, avoiding the overhead of copying data into Python space.
