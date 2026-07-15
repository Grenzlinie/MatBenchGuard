#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: benchmark_errors.json ===
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy scikit-learn
python3 << 'PYEOF'
import numpy as np
from sklearn.ensemble import ExtraTreesRegressor
import json

def f(x):
    return 1.0 / (x * (1.0 + np.exp(-150.0*(x-0.5))))

x_min, x_max = 0.001, 1.0
n_trees = 200
train_frac = 0.7
leaf_size = 1
max_features = 1
v_th = 0.2
d_th = 0.5
OOB_th = 0.014
RAD_th = 0.01

X = np.linspace(x_min, x_max, 4).reshape(-1, 1)
y = f(X).ravel()

OOB_first = None
prev_model = None
prev_new_points = None
iteration = 0

while True:
    iteration += 1
    model = ExtraTreesRegressor(
        n_estimators=n_trees,
        max_features=max_features,
        min_samples_leaf=leaf_size,
        bootstrap=True,
        oob_score=True,
        random_state=42
    )
    model.fit(X, y)
    oob_pred = model.oob_prediction_
    OOB_mse = np.mean((y - oob_pred) ** 2)
    if OOB_first is None:
        OOB_first = OOB_mse
        normalized_OOB = 1.0
    else:
        normalized_OOB = OOB_mse / OOB_first

    idx = np.argsort(X.ravel())
    X_sorted = X.ravel()[idx]
    y_sorted = y[idx]
    X_new = []
    for i in range(len(X_sorted)-1):
        xi, xj = X_sorted[i], X_sorted[i+1]
        yi, yj = y_sorted[i], y_sorted[i+1]
        deriv = (yj - yi) / (xj - xi)
        if abs(deriv) > d_th:
            X_new.append((xi + xj) / 2.0)
    X_new = np.array([x for x in X_new if not np.any(np.isclose(X, x, atol=1e-12))])
    if X_new.size == 0:
        break
    y_new = f(X_new.reshape(-1, 1)).ravel()

    rad = 1.0
    if prev_model is not None and prev_new_points is not None:
        y_prev = prev_model.predict(prev_new_points.reshape(-1, 1))
        y_curr = model.predict(prev_new_points.reshape(-1, 1))
        rad = np.mean(np.abs((y_curr - y_prev) / (np.abs(y_curr) + 1e-12)))

    prev_model = model
    prev_new_points = X_new
    X = np.vstack([X, X_new.reshape(-1, 1)])
    y = np.append(y, y_new)

    if normalized_OOB < OOB_th and rad < RAD_th:
        break
    if iteration > 30:
        break

training_set_size = len(X)

np.random.seed(123)
x_bench = np.random.uniform(x_min, x_max, 1000).reshape(-1, 1)
y_true = f(x_bench).ravel()
y_pred = model.predict(x_bench)
rel_errors = np.abs((y_true - y_pred) / (y_true + 1e-12))
avg_rel_error = np.mean(rel_errors)
max_rel_error = np.max(rel_errors)

data = {
    "average_relative_error": float(avg_rel_error),
    "max_relative_error": float(max_rel_error),
    "training_set_size": training_set_size
}
with open('/app/outputs/benchmark_errors.json', 'w') as f:
    json.dump(data, f, indent=2)
PYEOF
