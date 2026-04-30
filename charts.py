import matplotlib.pyplot as plt
import numpy as np

# Performance Data (Normalized for 10M rows)
tools = ('Pandas\n(read_csv)', 'Axiom v1.1\n(Precision)', 'Axiom v1.0\n(Naive Float)')
y_pos = np.arange(len(tools))
performance = [7.75, 2.7, 0.31] # Your real-world data points (seconds)

plt.style.use('seaborn-v0_8-darkgrid')
fig, ax = plt.subplots(figsize=(10, 6))

# Horizontal bar chart
bars = ax.barh(y_pos, performance, align='center', color=['#3498db', '#f1c40f', '#2ecc71'])
ax.set_yticks(y_pos, labels=tools)
ax.invert_yaxis()  # labels read top-to-bottom
ax.set_xlabel('Speed (Seconds - Lower is Better)')
ax.set_title('Axiom Protocol Ingestion Speed vs. Standard CPython', fontsize=16, fontweight='bold')

# Add labels to the end of each bar
for i, bar in enumerate(bars):
    ax.text(bar.get_width() + 0.1, bar.get_y() + bar.get_height()/2, 
            f'{performance[i]}s', va='center', fontweight='bold')

plt.tight_layout()
plt.savefig('performance_chart.png', dpi=300)
print("Performance chart generated successfully: performance_chart.png")
