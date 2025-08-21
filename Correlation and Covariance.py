import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'Math': [80, 90, 85, 70, 95],
    'Science': [75, 88, 92, 85, 70],
    'English': [82, 79, 85, 90, 88]
}
df = pd.DataFrame(data)

print(df.corr())
print(df.cov())

sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
plt.show()
