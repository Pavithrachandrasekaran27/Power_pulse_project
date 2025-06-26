import matplotlib.pyplot as plt
import seaborn as sns

def plot_correlations(df):
    corr = df.corr()
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr, annot=True, cmap='coolwarm')
    plt.title('Feature Correlation')
    plt.tight_layout()
    plt.show()
