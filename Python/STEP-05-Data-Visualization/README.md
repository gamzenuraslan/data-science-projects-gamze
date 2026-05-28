# STEP 5 — Data Visualization 📈

In this step, we start visualizing data using Python.

Data visualization helps us:
- understand datasets more easily,
- discover patterns,
- compare values,
- and make data more meaningful.

Using Matplotlib and Pandas, we create different types of charts and graphs 🚀

---

## Topics 📚

### 01 — Matplotlib Basics
- Basic line charts
- Titles & labels
- Multiple lines
- Grid system
- Figure size

### 02 — Line & Bar Charts
- Line charts
- Bar charts
- Horizontal bar charts
- Comparison charts

### 03 — Scatter Plot & Histogram
- Scatter plots
- Histogram charts
- Data distribution
- Visualization with bins

### 04 — Pandas Visualization
- Plotting directly from DataFrames
- Line charts
- Pie charts
- Histograms
- Scatter plots

### 05 — Mini Data Visualization Project
- Sales analysis
- Profit calculation
- Line charts
- Bar charts
- Basic data insights

---

## Goal 🎯

The goal of this step is to:
- improve data visualization skills,
- understand chart types,
- analyze data visually,
- and prepare for real-world analytics projects.

---

## Libraries Used 📦

- Matplotlib
- Pandas

---

## Mini Example 🚀

```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [10, 20, 30, 40]

plt.plot(x, y)

plt.title("Simple Line Chart")

plt.show()