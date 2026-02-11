# Grey Model Comparison: GM(1,1) vs DGM vs OSDGM

Compares three Grey forecasting models — GM(1,1), DGM, and OSDGM — against a 5-point historical dataset. Evaluates simulation accuracy and generates multi-step predictions with side-by-side visualizations.

## Features
- Side-by-side simulation accuracy comparison across all three models
- Percentage error calculation for each model against original values
- 3-step future predictions per model
- Two plots: simulative fit comparison and full predictive trajectory

## Models Compared
| Model | Description |
|---|---|
| GM(1,1) | Classic first-order single-variable Grey Model |
| DGM | Discrete Grey Model — avoids whitenization errors |
| OSDGM | Optimized Single-variable DGM — improved parameter estimation |

## Requirements
```
numpy
matplotlib
```

## Usage
```
python grey_model_comparison.py
```
The script will print error rates to the console and display two matplotlib plots.

## Output

**Console:**
- Original values and simulative values for each model
- Absolute percentage error per time step for GM(1,1), DGM, and OSDGM

**Plots:**
- *Simulative Values Comparison* — fitted values vs original across the 5 training points
- *Predictive Values Comparison* — full trajectory extending 3 steps beyond the training data

## Dataset
5-point time series: `[26.6, 36.1, 52.3, 80.1, 126.8]`

Predictions extend to time steps 6, 7, and 8.

## Technical Details
- **Error metric:** Absolute percentage error per step
- **Prediction horizon:** 3 steps
- **Visualization:** Matplotlib line plots with distinct markers per model

## Limitations
- Hardcoded dataset — swap `original_values` and pre-computed model outputs to use with different data
- Model parameters (simulative and predictive values) are pre-computed externally and passed in as arrays — no in-script model fitting
- No summary statistics (overall MAPE, RMSE) printed — only per-step errors

## License
MIT
