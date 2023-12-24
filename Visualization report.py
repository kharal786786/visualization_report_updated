# Importing required libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Function to set up the aesthetics for all plots
def set_plot_aesthetics():
    """
    Set the aesthetic style of the plots to 'whitegrid'.
    
    Returns:
    None
    """
    sns.set(style="whitegrid")

# Function to plot a line plot with multiple lines
def plot_multiple_lines(data, x, y_list, title, x_label, y_label):
    """
    Plot a line plot with multiple lines.
    
    Parameters:
    - data: pd.DataFrame - DataFrame containing the data.
    - x: str - Column name for x-axis.
    - y_list: list of str - List of column names for y-axis (multiple lines).
    - title: str - Title of the plot.
    - x_label: str - Label for x-axis.
    - y_label: str - Label for y-axis.
    
    Returns:
    None
    """
    plt.figure(figsize=(12, 6))
    for y in y_list:
        sns.lineplot(x=x, y=y, data=data, ci=None, label=y)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.legend()
    plt.show()

# Function to plot a histogram
def plot_histogram(data, column, title, x_label, y_label, bins=30):
    """
    Plot a histogram.
    
    Parameters:
    - data: pd.DataFrame - DataFrame containing the data.
    - column: str - Column name to plot.
    - title: str - Title of the plot.
    - x_label: str - Label for x-axis.
    - y_label: str - Label for y-axis.
    - bins: int - Number of bins for the histogram.
    
    Returns:
    None
    """
    plt.figure(figsize=(12, 6))
    sns.histplot(data[column], kde=True, bins=bins)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.show()

# Function to plot a box plot
def plot_boxplot(data, x, y, title, x_label, y_label):
    """
    Plot a box plot.
    
    Parameters:
    - data: pd.DataFrame - DataFrame containing the data.
    - x: str - Column name for x-axis.
    - y: str - Column name for y-axis.
    - title: str - Title of the plot.
    - x_label: str - Label for x-axis.
    - y_label: str - Label for y-axis.
    
    Returns:
    None
    """
    plt.figure(figsize=(12, 6))
    sns.boxplot(x=x, y=y, data=data)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.show()

# Main code
def main():
    # Set plot aesthetics
    set_plot_aesthetics()

    # Load the dataset
    dataset_path = 'heart_failure_clinical_records.csv'
    heart_failure_data = pd.read_csv(dataset_path)

    # Plotting the visualizations using the defined functions
    plot_multiple_lines(heart_failure_data, 'time', ['ejection_fraction', 'serum_creatinine'], 
                        'Clinical Measures Over Time', 'Time (Days)', 'Clinical Measures')

    plot_histogram(heart_failure_data, 'age', 'Age Distribution of Patients', 'Age', 'Frequency')

    plot_boxplot(heart_failure_data, 'diabetes', 'serum_sodium', 
                 'Serum Sodium Levels by Diabetes Status', 'Diabetes (0 = No, 1 = Yes)', 'Serum Sodium (mEq/L)')

# Calling the main function
if __name__ == "__main__":
    main()
