# Retail Inventory Turnover Analysis (2024)

**Author:** 25ds2000003@ds.study.iitm.ac.in  
**LLM Assistance:** Analysis and code written with help from an LLM (e.g., Jules / ChatGPT Codex).

---

## 1. Business Context

The company is facing **excess inventory and rising storage costs**.  
The current **average inventory turnover ratio is 5.7**, while the **industry benchmark target is 8**.

Management wants to understand:

- How inventory turnover behaved across **2024 quarters**
- How far the company is from the **industry target**
- What actions are needed to improve turnover and reduce costs

The ultimate goal is to **optimize supply chain and demand forecasting** to reach or exceed the benchmark.

---

## 2. Dataset

**Inventory Turnover Ratio – 2024 Quarterly Data:**

| Quarter | Inventory Turnover |
|--------:|--------------------|
| Q1      | 3.40               |
| Q2      | 7.70               |
| Q3      | 5.41               |
| Q4      | 6.31               |

- **Average (2024): 5.7**  
- **Industry Target: 8.0**

> The average value of 5.7 is used throughout this analysis and is also computed in the code.

---

## 3. Methodology

The analysis script (`analysis.py`) performs the following:

1. **Loads the quarterly turnover data** into a pandas DataFrame.
2. **Calculates the average inventory turnover** for 2024.
3. **Computes the gap to the industry benchmark** (target – average).
4. **Visualizes the quarterly trend** with a line chart overlaid with a horizontal line at the **industry target (8)**.
5. **Exports**:
   - `inventory_turnover_2024.png` – quarterly trend vs benchmark
   - `summary_metrics.csv` – key metrics (average, target, gap)

---

## 4. Key Findings

1. **Underperformance vs Target**
   - **Average inventory turnover (2024): 5.7**
   - **Industry target: 8.0**
   - **Gap: 2.3 points below target**
   - This indicates **slower-than-ideal stock movement** and elevated inventory holding levels.

2. **Quarterly Dynamics**
   - **Q1 (3.40)**: Significantly below target — suggests **overstocking**, sluggish sales, or new assortment misalignment.
   - **Q2 (7.70)**: Strong recovery, almost at the industry benchmark — suggests that **promotions, seasonality, or better alignment** boosted turnover.
   - **Q3 (5.41)** and **Q4 (6.31)**: Moderate performance but still **below target**, indicating that the improvement in Q2 was **not sustained**.

3. **Pattern Summary**
   - The company can **occasionally approach best practice levels (Q2)**, but performance is **inconsistent**.
   - The volatility across quarters hints at **reactive management** (e.g., ad-hoc promotions) rather than a stable, optimized **supply chain and demand planning process**.

---

## 5. Business Implications

1. **Excess Inventory & Storage Costs**
   - A turnover of **5.7 vs target 8** implies that inventory stays in storage **longer than optimal**, increasing:
     - Warehousing costs
     - Handling and insurance costs
     - Risk of shrinkage (damage, theft) and obsolescence

2. **Working Capital Inefficiency**
   - Capital is **locked up in slow-moving inventory**, reducing the cash available for:
     - Product innovation
     - Marketing and growth initiatives
     - Strategic investments

3. **Demand-Supply Mismatch**
   - The fluctuations suggest:
     - Poor **demand forecasting accuracy**
     - Over-ordering in certain periods
     - Possible stock-outs in others (if inventory is skewed toward the wrong SKUs)

4. **Customer Experience Risk**
   - Misaligned stock levels can hurt:
     - Fill rates and service levels
     - Customer satisfaction and loyalty
     - Brand perception, especially if popular items are missing while less relevant stock piles up

---

## 6. Recommendations to Reach the Target of 8

The recommended solution is to **optimize supply chain and demand forecasting**. Concretely:

### 6.1 Strengthen Demand Forecasting

- Implement **advanced forecasting models** (time series, machine learning) that incorporate:
  - Seasonality
  - Promotions
  - Macroeconomic factors
  - Channel-level and region-level trends
- Integrate **real-time sales data (POS)** into forecasting to detect demand shifts early.
- Use **forecast accuracy KPIs** (MAPE, bias) and review them regularly by category.

### 6.2 Refine Inventory Planning & Replenishment

- Introduce **ABC/XYZ analysis**:
  - Focus forecasting accuracy and service levels for A/high-value and X/stable-demand items.
- Optimize **reorder points and safety stock**:
  - Use statistical safety stock formulas based on demand variability and lead time.
- Shorten replenishment cycles where possible by:
  - Negotiating **shorter lead times** with suppliers
  - Exploring **local or regional suppliers** to reduce variability

### 6.3 Optimize the Supply Chain

- Improve **supplier collaboration** via:
  - Collaborative Planning, Forecasting, and Replenishment (CPFR)
  - Sharing forecasts and sales data with key suppliers
- Evaluate **multi-echelon inventory strategies** to position stock closer to demand while minimizing overall inventory.
- Introduce **vendor-managed inventory (VMI)** for stable product lines.

### 6.4 Tactical Levers for Slow-Moving Inventory

- Use targeted **markdowns** and **promotions** to clear aged inventory.
- Rationalize SKUs:
  - Remove or phase out **chronic low-turn items**.
  - Consolidate similar SKUs to reduce complexity.

### 6.5 Governance & Monitoring

- Establish a **monthly S&OP / IBP process**:
  - Align sales, marketing, finance, and supply chain on one consensus plan.
- Track a **dashboard** of:
  - Inventory turnover by quarter and by category
  - Days of inventory on hand (DOH)
  - Stock-out rate and service level

---

## 7. Files in This Pull Request

- `analysis.py`  
  - Python script that:
    - Processes the quarterly inventory turnover data
    - Computes the average (5.7) and gap to the industry target (8)
    - Generates the `inventory_turnover_2024.png` visualization

- `inventory_turnover_2024.png`  
  - Line plot showing **company quarterly turnover** vs **industry target**.

- `summary_metrics.csv`  
  - Simple table with:
    - `average_turnover_2024`
    - `industry_target`
    - `gap_to_target`

- `README.md` (this file)  
  - Contains the **data story**, **business implications**, and detailed **recommendations**
  - Explicitly mentions the solution: **"optimize supply chain and demand forecasting"**
  - Contains the required email: **25ds2000003@ds.study.iitm.ac.in**
  - Uses the correct **average value: 5.7**

---

## 8. LLM Usage Note

This analysis and code were developed with assistance from an **LLM (e.g., Jules / ChatGPT Codex / ChatGPT)**.  
To make this visible in the Git history, commit messages such as:

- `feat: add LLM-generated inventory analysis script`
- `docs: add LLM-assisted data story to README`

can be used to clearly signal that LLM tools were part of the workflow.
