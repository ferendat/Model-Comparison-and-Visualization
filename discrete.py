import numpy as np
import matplotlib.pyplot as plt

# Define data
original_values = np.array([26.6, 36.1, 52.3, 80.1, 126.8])
gm_sim_values = np.array([22.4468, 33.9133, 51.2375, 77.4113, 116.955])
dgm_sim_values = np.array([22.8889, 34.7682, 52.813, 80.2229, 121.8586])
osdgm_sim_values = np.array([23.4805, 35.6746, 54.2014, 82.3499, 125.1167])

gm_pred_values = np.array([176.701, 266.966, 403.341])
dgm_pred_values = np.array([185.103, 281.172, 427.1])
osdgm_pred_values = np.array([190.0935, 288.8148, 438.8051])

# Function to calculate percentage errors
def calculate_percentage_error(true_values, predicted_values):
    return np.abs(true_values - predicted_values) / true_values * 100

# Calculate errors for each model
gm_errors = calculate_percentage_error(original_values, gm_sim_values)
dgm_errors = calculate_percentage_error(original_values, dgm_sim_values)
osdgm_errors = calculate_percentage_error(original_values, osdgm_sim_values)

# Display results
def display_results():
    print("Original Values:", original_values)
    print("GM(1,1) Simulative Values:", gm_sim_values)
    print("DGM Simulative Values:", dgm_sim_values)
    print("OSDGM Simulative Values:", osdgm_sim_values)
    print("\nError Rates:")
    print(f"  GM(1,1): {gm_errors}%")
    print(f"  DGM: {dgm_errors}%")
    print(f"  OSDGM: {osdgm_errors}%")

display_results()

# Function to plot data
def plot_comparison(data, labels, title, xlabel, ylabel, markers=None):
    plt.figure(figsize=(10, 5))
    for i, series in enumerate(data):
        marker = markers[i] if markers else None
        plt.plot(series, label=labels[i], marker=marker)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    plt.grid(True)
    plt.show()

# Simulative values comparison
plot_comparison(
    data=[original_values, gm_sim_values, dgm_sim_values, osdgm_sim_values],
    labels=["Original Values", "GM(1,1) Simulative Values", "DGM Simulative Values", "OSDGM Simulative Values"],
    title="Simulative Values Comparison",
    xlabel="Time Step",
    ylabel="Values",
    markers=["o", "x", "^", "s"]
)

# Predictive values comparison
time_steps = np.arange(1, len(original_values) + len(gm_pred_values) + 1)
full_values = [original_values] + [np.concatenate((original_values, preds)) for preds in [gm_pred_values, dgm_pred_values, osdgm_pred_values]]

plot_comparison(
    data=full_values,
    labels=["Original Values", "GM(1,1) Predictive Values", "DGM Predictive Values", "OSDGM Predictive Values"],
    title="Predictive Values Comparison",
    xlabel="Time Step",
    ylabel="Predictive Values",
    markers=["o", "x", "^", "s"]
)
