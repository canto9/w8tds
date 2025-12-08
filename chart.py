# chart.py
# Email: 23f2000738@ds.study.iitm.ac.in

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# -----------------------------
# Generate Synthetic Product Data
# -----------------------------
np.random.seed(42)

products = ["Product A", "Product B", "Product C", "Product D", "Product E"]
performance = np.random.randint(60, 100, size=5)

df = pd.DataFrame({
    "Product": products,
    "Performance": performance
})

# -----------------------------
# Styling
# -----------------------------
sns.set_style("whitegrid")         # clean professional look
sns.set_context("talk")            # presentation-ready sizing

# -----------------------------
# Create Chart (512x512 px)
# figsize(8,8) at dpi=64 → 512x512
# -----------------------------
plt.figure(figsize=(8, 8), dpi=64)

sns.barplot(
    data=df,
    x="Product",
    y="Performance",
    palette="viridis"
)

plt.title("Product Performance Analysis", fontsize=20)
plt.xlabel("Product", fontsize=16)
plt.ylabel("Performance Score", fontsize=16)

plt.tight_layout()

# Save EXACT SIZE heatmap
plt.savefig("chart.png", dpi=64, bbox_inches="tight")
plt.close()
