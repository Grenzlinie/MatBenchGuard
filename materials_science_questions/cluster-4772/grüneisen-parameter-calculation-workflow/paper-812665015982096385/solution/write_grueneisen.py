#!/usr/bin/env python3
import json

barite = [
  {"wavenumber(cm)": 127, "gamma_iP": 2.92, "gamma_iT": None, "a_i(x10^5_K^-1)": -7.30},
  {"wavenumber(cm)": 148, "gamma_iP": 3.45, "gamma_iT": None, "a_i(x10^5_K^-1)": -12.90},
  {"wavenumber(cm)": 155, "gamma_iP": 0.88, "gamma_iT": None, "a_i(x10^5_K^-1)": 10.3},
  {"wavenumber(cm)": 169, "gamma_iP": 1.67, "gamma_iT": None, "a_i(x10^5_K^-1)": -12.36},
  {"wavenumber(cm)": 188, "gamma_iP": 2.79, "gamma_iT": None, "a_i(x10^5_K^-1)": -15.26},
  {"wavenumber(cm)": 452, "gamma_iP": 0.54, "gamma_iT": 0.30, "a_i(x10^5_K^-1)": -1.97},
  {"wavenumber(cm)": 461, "gamma_iP": 0.57, "gamma_iT": 0.38, "a_i(x10^5_K^-1)": -1.38},
  {"wavenumber(cm)": 616, "gamma_iP": None, "gamma_iT": 0.11, "a_i(x10^5_K^-1)": 0.50},
  {"wavenumber(cm)": 623, "gamma_iP": 0.09, "gamma_iT": 0.19, "a_i(x10^5_K^-1)": 0.60},
  {"wavenumber(cm)": 646, "gamma_iP": 0.28, "gamma_iT": 0.18, "a_i(x10^5_K^-1)": -1.54},
  {"wavenumber(cm)": 988, "gamma_iP": 0.33, "gamma_iT": 0.23, "a_i(x10^5_K^-1)": -1.81},
  {"wavenumber(cm)": 1083, "gamma_iP": 0.39, "gamma_iT": None, "a_i(x10^5_K^-1)": -2.11},
  {"wavenumber(cm)": 1104, "gamma_iP": 0.49, "gamma_iT": None, "a_i(x10^5_K^-1)": -1.64},
  {"wavenumber(cm)": 1138, "gamma_iP": 0.39, "gamma_iT": 0.19, "a_i(x10^5_K^-1)": -2.14},
  {"wavenumber(cm)": 1166, "gamma_iP": 0.43, "gamma_iT": 0.71, "a_i(x10^5_K^-1)": -2.34}
]

celestine = [
  {"wavenumber(cm)": 131, "gamma_iP": 2.61, "gamma_iT": None, "a_i(x10^5_K^-1)": -14.26},
  {"wavenumber(cm)": 170, "gamma_iP": 3.35, "gamma_iT": None, "a_i(x10^5_K^-1)": -18.26},
  {"wavenumber(cm)": 197, "gamma_iP": 3.12, "gamma_iT": None, "a_i(x10^5_K^-1)": -9.79},
  {"wavenumber(cm)": 454, "gamma_iP": 0.61, "gamma_iT": 0.24, "a_i(x10^5_K^-1)": -0.74},
  {"wavenumber(cm)": 461, "gamma_iP": 0.33, "gamma_iT": 0.30, "a_i(x10^5_K^-1)": -1.81},
  {"wavenumber(cm)": 622, "gamma_iP": 0.02, "gamma_iT": 0.13, "a_i(x10^5_K^-1)": -1.25},
  {"wavenumber(cm)": 639, "gamma_iP": 0.27, "gamma_iT": 0.16, "a_i(x10^5_K^-1)": -0.66},
  {"wavenumber(cm)": 656, "gamma_iP": 0.47, "gamma_iT": 0.19, "a_i(x10^5_K^-1)": -2.03},
  {"wavenumber(cm)": 1000, "gamma_iP": 0.44, "gamma_iT": 0.22, "a_i(x10^5_K^-1)": -2.06},
  {"wavenumber(cm)": 1094, "gamma_iP": 0.51, "gamma_iT": 0.32, "a_i(x10^5_K^-1)": -1.90},
  {"wavenumber(cm)": 1111, "gamma_iP": 0.41, "gamma_iT": None, "a_i(x10^5_K^-1)": -2.13},
  {"wavenumber(cm)": 1158, "gamma_iP": 0.43, "gamma_iT": 0.16, "a_i(x10^5_K^-1)": -2.39},
  {"wavenumber(cm)": 1190, "gamma_iP": 0.55, "gamma_iT": None, "a_i(x10^5_K^-1)": -3.01}
]

result = {
  "barite": barite,
  "celestine": celestine
}

with open("/app/outputs/grueneisen_results.json", "w") as f:
    json.dump(result, f, indent=2)
