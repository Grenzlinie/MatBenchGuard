# Coupling strength of electrons to spin excitations in cuprate superconductors from t-J model

## Problem background
In cuprate superconductors, the coupling between electrons and spin excitations is a prime candidate for the pairing glue. This coupling is quantified by the normal and pairing Eliashberg functions α²F^{(n)}(k,ω) and α²F^{(p)}(k,ω). Within the kinetic-energy-driven superconductivity mechanism based on the t-J model, these functions can be computed from the underlying quasiparticle spectral functions and the electron-spin kernel. The task is to implement this formalism, compute the Eliashberg functions for specified conditions of doping, Fermi-surface momentum (antinode, hot spot, node), and temperature, and extract the characteristic energy scales (peak positions) that emerge. The outcome probes how the coupling strength varies with doping, momentum, and temperature, revealing whether distinct low- and high-energy features exist and how they evolve.

## Approach
The reproduction follows the kinetic-energy-driven superconductivity formalism. The t-J model is treated in the charge-spin recombination scheme, where the normal and pairing self-energies arise from the interaction between electrons mediated by spin excitations. From the full Green’s functions one obtains the normal quasiparticle spectral function A(p,ω) and the pairing spectral function A_ℑ†(p,ω). The coupling to spin excitations enters via a kernel K̅(k,p,ω) that involves a spin-bubble convolution. The normal and pairing Eliashberg functions are then computed as momentum-space integrals: α²F^{(n)}(k,ω) = (1/N) Σ_p A(p,ω) K̅(k,p,ω) and α²F^{(p)}(k,ω) = (1/N) Σ_p A_ℑ†(p,ω) K̅(k,p,ω).

The model parameters are fixed: t/J = 2.5, t′/t = 0.3, and J = 120 meV. The calculation is carried out for specific points on the Fermi surface — antinode, hot spot, and node — at four dopings (δ = 0.06, 0.09, 0.12, 0.15) and at low temperature T = 0.002J, as well as at T = 0.06J for δ = 0.09. Once the energy-dependent functions α²F^{(n)}(k,ω) and α²F^{(p)}(k,ω) are obtained over the binding-energy range 0–0.5J, the energy positions of any observed peaks are extracted to characterise the coupling strength.

## Reproduction target
Compute the normal and pairing Eliashberg functions for each of the following conditions:

- antinode, δ = 0.06, T = 0.002J
- antinode, δ = 0.09, T = 0.002J
- antinode, δ = 0.12, T = 0.002J
- antinode, δ = 0.15, T = 0.002J
- antinode, δ = 0.09, T = 0.06J
- hot spot, δ = 0.15, T = 0.002J
- node, δ = 0.15, T = 0.002J

The output consists of:

1. **Eliashberg functions** (`eliashberg_functions.csv`): a table with columns `condition` (a string naming the condition), `omega` (binding energy in meV), `alpha2F_n` (normal coupling), and `alpha2F_p` (pairing coupling). One row per (condition, omega) pair.

2. **Peak positions** (`peak_positions.json`): a JSON object whose keys are the condition strings. Each value contains the fields `low_peak_omega_n`, `broad_peak_omega_n`, `low_peak_omega_p`, `broad_peak_omega_p` (all in meV). If no peak is detected for a given channel, set the corresponding field to `null`.

The computation must use the model parameters t/J = 2.5, t′/t = 0.3, and J = 120 meV, and span the binding-energy range 0–0.5J. The resulting curves and peak positions will be checked against physical expectations — including the number of peaks, their energy scales, and how they vary with doping, momentum, and temperature — without revealing those values in advance.

## Assets

- numpy: numpy
- scipy: scipy
- matplotlib: matplotlib

## Workflow steps

### Step 1: Compute quasiparticle spectral functions and electron-spin kernel
- Role: process
- Action: Implement the kinetic-energy-driven superconductivity formalism of the t-J model with full charge-spin recombination. Compute the normal spectral function A(p,ω), pairing spectral function A_ℑ†(p,ω), and the electron-spin excitation kernel function K̅(k,p,ω) for all momenta and energies needed for the subsequent Eliashberg function integration. Use model parameters t=2.5J, t'=0.3t, J=120 meV, and specified dopings and temperatures.
- Evidence: `/app/outputs/tj_model_outputs.npy`

### Step 2: Compute Eliashberg functions α²F^(n) and α²F^(p)
- Role: scored (load-bearing)
- Action: Use the spectral functions and kernel from Step 1 to evaluate the normal and pairing coupling strengths via convolution (Eqs. 4 and 5 of the paper) for each specified condition: antinode, hot spot, node momenta at dopings δ=0.06,0.09,0.12,0.15, and temperatures T=0.002J and T=0.06J. Convert energy to meV assuming J=120 meV. Save the curves as a CSV file.
- Output file: `/app/outputs/eliashberg_functions.csv`
- Format: csv
- Contract: CSV with columns: condition (string, e.g., 'AN_delta0.15_T0.002J'), omega (float, binding energy in meV), alpha2F_n (float, normal coupling), alpha2F_p (float, pairing coupling). One row per (condition, omega) pair.
- Scoring: scored by hidden verifier

### Step 3: Extract peak positions from Eliashberg functions
- Role: scored
- Action: From the Eliashberg function curves in eliashberg_functions.csv, identify the low-energy peak and broad peak for each condition and channel (normal and pairing). Determine peak positions in meV by local maxima detection within the expected energy windows (0–20 meV for low peak, 20–60 meV for broad peak). For conditions where a peak is absent or nearly zero, set null. Save the results as a JSON file.
- Output file: `/app/outputs/peak_positions.json`
- Format: json
- Contract: JSON object where keys are condition strings matching those in eliashberg_functions.csv. Each value is an object with keys 'low_peak_omega_n', 'broad_peak_omega_n', 'low_peak_omega_p', 'broad_peak_omega_p' (in meV; set to null if no peak detected).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/eliashberg_functions.csv`
- `/app/outputs/peak_positions.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### eliashberg_functions.csv
- path: `/app/outputs/eliashberg_functions.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Raw Eliashberg function curves; the checker will recompute peak positions from this data and compare them against the paper-reported gold values.
- schema:
  - `type`: table
  - `required_columns`: `condition`, `omega`, `alpha2F_n`, `alpha2F_p`
  - `units`:
    - `omega`: meV
    - `alpha2F_n`: unitless
    - `alpha2F_p`: unitless

### peak_positions.json
- path: `/app/outputs/peak_positions.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Agent-reported peak positions; the checker will compare these against its own recomputed peaks and the hidden paper reference values.
- schema:
  - `type`: object
  - `required`: object
  - `items`:
    - `type`: object
    - `properties`:
      - `low_peak_omega_n`:
        - `type`: `number`, `null`
        - `unit`: meV
      - `broad_peak_omega_n`:
        - `type`: `number`, `null`
        - `unit`: meV
      - `low_peak_omega_p`:
        - `type`: `number`, `null`
        - `unit`: meV
      - `broad_peak_omega_p`:
        - `type`: `number`, `null`
        - `unit`: meV

Notes: The Eliashberg functions must be computed for the following conditions (condition strings as examples): AN_delta0.06_T0.002J, AN_delta0.09_T0.002J, AN_delta0.12_T0.002J, AN_delta0.15_T0.002J, AN_delta0.09_T0.06J, HS_delta0.15_T0.002J, ND_delta0.15_T0.002J. The hot spot and node positions are defined on the Fermi surface as per the paper. Parameters: t=2.5J, t'=0.3t, J=120 meV. All calculations start from the t-J model formulas in Ref. [50]; no external datasets are provided.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "eliashberg_functions.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "condition",
          "omega",
          "alpha2F_n",
          "alpha2F_p"
        ],
        "units": {
          "omega": "meV",
          "alpha2F_n": "unitless",
          "alpha2F_p": "unitless"
        }
      },
      "description": "Raw Eliashberg function curves; the checker will recompute peak positions from this data and compare them against the paper-reported gold values."
    },
    {
      "file": "peak_positions.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {},
        "items": {
          "type": "object",
          "properties": {
            "low_peak_omega_n": {
              "type": [
                "number",
                "null"
              ],
              "unit": "meV"
            },
            "broad_peak_omega_n": {
              "type": [
                "number",
                "null"
              ],
              "unit": "meV"
            },
            "low_peak_omega_p": {
              "type": [
                "number",
                "null"
              ],
              "unit": "meV"
            },
            "broad_peak_omega_p": {
              "type": [
                "number",
                "null"
              ],
              "unit": "meV"
            }
          }
        }
      },
      "description": "Agent-reported peak positions; the checker will compare these against its own recomputed peaks and the hidden paper reference values."
    }
  ],
  "notes": "The Eliashberg functions must be computed for the following conditions (condition strings as examples): AN_delta0.06_T0.002J, AN_delta0.09_T0.002J, AN_delta0.12_T0.002J, AN_delta0.15_T0.002J, AN_delta0.09_T0.06J, HS_delta0.15_T0.002J, ND_delta0.15_T0.002J. The hot spot and node positions are defined on the Fermi surface as per the paper. Parameters: t=2.5J, t'=0.3t, J=120 meV. All calculations start from the t-J model formulas in Ref. [50]; no external datasets are provided."
}
```

## How you are scored
A hidden verifier independently checks the two output artifacts against hidden reference data and physical constraints. First, the verifier recomputes peak positions from the raw data in `eliashberg_functions.csv` by detecting local maxima within defined energy windows (0–20 meV for a low-energy peak, 20–60 meV for a broad peak) and compares both the recomputed peaks and the agent-reported peaks to the expected energy scales. Second, the verifier validates that the results satisfy required trends: for example, a specific doping evolution of the broad peak energy, the momentum-dependent variation of the low-energy peak weight, the vanishing of the pairing channel at the node, and the persistence of the peak structure above Tc with reduced weight.

The total reward is a weighted combination of checks on the raw Eliashberg curves and the extracted peak positions, with the bulk of the weight on the correctness of the physical features and trends. The verifier’s recomputation ensures that simply reporting plausible numbers without having performed the full calculation does not earn a high score.
