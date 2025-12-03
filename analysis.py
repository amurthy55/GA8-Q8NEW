"""
Retail Inventory Turnover Analysis - 2024
Author: 25ds2000003@ds.study.iitm.ac.in

This script was written with assistance from an LLM (e.g., ChatGPT / Jules / Codex).
"""

import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# 1. Define quarterly data
# -----------------------------
data = {
    "quarter": ["Q1", "Q2", "Q3", "Q4"],
    "inventory_turnover": [3.4, 7.7, 5.41, 6.31],  # 2024 data
}

INDUSTRY_TARGET = 8.0

df = pd.DataFrame(data)

# -----------------------------
# 2. Compute summary metrics
# -----------------------------
average_turnover = df["inventory_turnover"].mean()
gap_to_target = INDUSTRY_TARGET - average_turnover

print("=== Retail Inventory Turnover Analysis (2024) ===")
print(df)
print(f"\nAverage inventory turnover (2024): {average_turnover:.2f}")
print(f"Industry benchmark target: {INDUSTRY_TARGET:.2f}")
print(f"Gap to target: {gap_to_target:.2f} (positive means below target)")

# -----------------------------
# 3. Visualization: Trend vs Target
# -----------------------------
plt.figure(figsize=(8, 5))

# Line plot for quarterly turnover
plt.plot(df["quarter"], df["inventory_turnover"], marker="o", label="Company Turnover (2024)")

# Horizontal line for industry target
plt.axhline(INDUSTRY_TARGET, linestyle="--", label=f"Industry Target ({INDUSTRY_TARGET})")

for x, y in zip(df["quarter"], df["inventory_turnover"]):
    plt.text(x, y + 0.1, f"{y:.2f}", ha="center", fontsize=9)

plt.title("Inventory Turnover Ratio - 2024 vs Industry Target")
plt.xlabel("Quarter")
plt.ylabel("Inventory Turnover Ratio")
plt.ylim(0, max(df["inventory_turnover"].max(), INDUSTRY_TARGET) + 1)
plt.legend()
plt.tight_layout()

# Save the figure
plt.savefig("inventory_turnover_2024.png", dpi=150)
print("\nSaved chart as: inventory_turnover_2024.png")

# -----------------------------
# 4. Optional: Export data summary to CSV
# -----------------------------
df_summary = pd.DataFrame(
    {
        "metric": ["average_turnover_2024", "industry_target", "gap_to_target"],
        "value": [round(average_turnover, 2), INDUSTRY_TARGET, round(gap_to_target, 2)],
    }
)
df_summary.to_csv("summary_metrics.csv", index=False)
print("Saved summary metrics as: summary_metrics.csv")
