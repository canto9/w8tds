# mrr_analysis.py
# Email: 23f2000738@ds.study.iitm.ac.in

import matplotlib.pyplot as plt

# Quarterly MRR growth data
quarters = ['Q1', 'Q2', 'Q3', 'Q4']
mrr_growth = [1.13, 5.71, 9.8, 8.34]
average_growth = sum(mrr_growth)/len(mrr_growth)
industry_target = 15

print(f"Quarterly MRR Growth: {mrr_growth}")
print(f"Average MRR Growth: {average_growth:.2f}")

# Plotting the trend
plt.figure(figsize=(8,5))
plt.plot(quarters, mrr_growth, marker='o', label='Company MRR Growth')
plt.axhline(industry_target, color='red', linestyle='--', label='Industry Target')
plt.title('Quarterly MRR Growth vs Industry Target')
plt.ylabel('MRR Growth (%)')
plt.xlabel('Quarter')
plt.ylim(0, max(industry_target, max(mrr_growth)) + 5)
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('mrr_growth_plot.png', dpi=150)
plt.show()
