# Email: 23f2000738@ds.study.iitm.ac.in
# This Marimo notebook demonstrates interactive data exploration

import marimo

app = marimo.App()


# ---------------------------------------------------------
# CELL 1: Import libraries and generate sample dataset
# ---------------------------------------------------------
# Data produced here is consumed by Cell 2

@app.cell
def _(np):
    import numpy as np
    import pandas as pd

    # Generate synthetic dataset
    x = np.linspace(0, 10, 200)
    y = 3 * x + np.random.normal(0, 3, size=len(x))
    df = pd.DataFrame({"x": x, "y": y})
    return df, pd, np
# ---------------------------------------------------------



# ---------------------------------------------------------
# CELL 2: Slider widget controlling filtering threshold
# ---------------------------------------------------------
# This slider value is used in Cell 3 for dynamic markdown

@app.cell
def _(mo):
    slider = mo.ui.slider(start=0, stop=10, step=1, value=5, label="X Threshold")
    slider
    return slider
# ---------------------------------------------------------



# ---------------------------------------------------------
# CELL 3: Dynamic markdown output based on slider state
# ---------------------------------------------------------
# Depends on:
#   - df from Cell 1
#   - slider from Cell 2

@app.cell
def _(df, slider, mo):
    threshold = slider.value
    filtered = df[df["x"] >= threshold]

    mo.md(
        f"""
        ## 🔍 Data Summary (Dynamic)
        You selected **X ≥ {threshold}**  
        Filtered rows: **{len(filtered)}**

        ### Sample Values
        - First x in filtered data: `{filtered['x'].iloc[0] if len(filtered)>0 else 'None'}`  
        - Mean y: `{filtered['y'].mean():.2f if len(filtered)>0 else 'N/A'}`  
        """
    )
    return filtered
# ---------------------------------------------------------



# ---------------------------------------------------------
# CELL 4: Simple plot depending on filtered data
# ---------------------------------------------------------
# Depends on "filtered" from Cell 3

@app.cell
def _(filtered):
    import matplotlib.pyplot as plt

    plt.scatter(filtered["x"], filtered["y"])
    plt.title("Filtered Data Scatter Plot")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()
# ---------------------------------------------------------



if __name__ == "__main__":
    app.run()
