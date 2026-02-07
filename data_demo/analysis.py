import pandas as pd
import matplotlib.pyplot as plt


def analyze_data(csv_path):
    # Load data
    df = pd.read_csv(csv_path)

    # Basic info
    print("Data Info:")
    print(df.info())

    # Describe
    print("\nStatistics:")
    print(df.describe())

    # Plot
    df.plot()
    plt.title("Data Visualization")
    plt.savefig("output.png")

    print("Analysis finished. Saved as output.png")


if __name__ == "__main__":
    analyze_data("sample.csv")