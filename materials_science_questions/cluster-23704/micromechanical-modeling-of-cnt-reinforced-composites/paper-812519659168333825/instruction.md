# Dynamic Instability Region Calculation for Hybrid CNT/Carbon-Fiber Polymer Beams

## Problem background
Hybrid polymer beams reinforced with both carbon fibers (CFs) and carbon nanotubes (CNTs) are being explored for structural applications that may experience periodic axial loads. Such loading can induce parametric resonance, leading to dynamic instability. This task focuses on computing the dynamic instability region (DIR) — the boundaries in excitation-frequency vs. dynamic-load-factor space that separate stable and unstable regimes — for a hybrid CF/CNT/polymer beam. The goal is to quantify how the DIR depends on the CNT weight percentage and the CF volume fraction inside the composite, using a numerical model based on exponential shear deformation beam theory and Halpin‑Tsai micromechanics.

## Approach
First, the effective elastic constants, Poisson's ratio, and density of the multi‑phase nanocomposite are obtained from the constituent properties (epoxy matrix, carbon fibers, carbon nanotubes) via the Halpin‑Tsai model and rule‑of‑mixture relations. Then a structural model based on exponential shear deformation beam theory (ESDBT) is implemented. The governing equations of motion are discretized using the differential quadrature method (DQM), and Bolotin's procedure is applied to convert the time‑periodic problem into a standard eigenvalue problem whose solution gives the DIR boundaries. Before tackling the full parametric study, the solver is validated by reproducing benchmark results for natural frequencies, critical buckling loads, and fundamental frequencies from the literature, adapting the model to the published validation cases.

## Reproduction target
Compute the effective material properties of the hybrid composite for multiple CNT weight fractions and CF volume fractions. Implement the ESDBT‑DQM solver and first confirm its correctness by computing: (a) the first five natural frequencies of a clamped‑free sandwich beam, (b) non‑dimensional critical buckling loads of a CNT‑reinforced PMMA beam under simply‑supported (SS), clamped‑simply (CS), and clamped‑clamped (CC) boundary conditions, and (c) dimensionless fundamental frequencies of a CNT‑reinforced beam under five different shear deformation theories (FSDT, TSDT, ESDT, HSDT, TrSDT). Then use the validated solver to compute the dynamic instability region (DIR) boundaries (excitation frequency ω versus dynamic load factor β) for: (i) at least three CNT weight fractions (e.g. 0.01, 0.02, 0.03) while keeping the CF volume fraction constant (e.g. 0.2), and (ii) at least two CF volume fractions (e.g. 0.2, 0.3) while keeping the CNT weight fraction constant (e.g. 0.02). Use the beam geometry L = 2 m, h = 30 cm, a static load factor α = 0, and CC boundary conditions. Write all results — validation benchmarks and the parametric DIR data — to the file computed_results.json with the structure described in the output contract.

## Assets

- Python scientific libraries (numpy, scipy): numpy, scipy

## Workflow steps

### Step 1: Compute Effective Composite Material Properties
- Role: process
- Action: Using the given constituent properties of the matrix (epoxy), carbon fibers, and carbon nanotubes, along with the CNT weight fraction and CF volume fraction, compute the effective elastic constants (longitudinal modulus E11, transverse modulus E22, in-plane shear modulus G12), Poisson's ratio, and density of the hybrid nanocomposite using the Halpin-Tsai micromechanics model. The CNT volume fraction is obtained from the weight fraction via the density-based relation. Save the computed properties to a JSON file for later use.
- Evidence: `/app/outputs/material_properties.json`

### Step 2: Validate DQM Solver and Compute Dynamic Instability Regions
- Role: scored (load-bearing)
- Action: Implement the exponential shear deformation beam theory (ESDBT) and the differential quadrature method (DQM) with Bolotin’s method to solve the eigenvalue problem for parametric instability. First, validate the solver by computing: (a) natural frequencies for a clamped-free sandwich beam (geometry and material properties as in Joubaneh et al. [53], with a clamped-free boundary condition, for the first five modes), (b) non-dimensional critical buckling loads for a CNT-reinforced PMMA beam under SS, CS, and CC boundary conditions, and (c) dimensionless fundamental frequencies for a CNT-reinforced beam using different shear deformation theories (FSDT, TSDT, ESDT, HSDT, TrSDT). Then, using the effective material properties from step 1, compute the dynamic instability region (DIR) boundaries (excitation frequency ω as a function of dynamic load factor β) for: (i) at least three CNT weight fractions (e.g., 0.01, 0.02, 0.03) with a constant CF volume fraction (e.g., 0.2), and (ii) at least two CF volume fractions (e.g., 0.2, 0.3) with a constant CNT weight fraction (e.g., 0.02). In both cases use the beam geometry L=2 m, h=30 cm, a static load factor α=0, and clamped-clamped (CC) boundary conditions. Save all results to computed_results.json.
- Output file: `/app/outputs/computed_results.json`
- Format: json
- Contract: root object with keys: 'validation' (object containing 'natural_frequencies': array of {mode: int, frequency: float}, 'buckling_loads': array of {BC: string, buckling_load: float}, 'dimensionless_frequencies': array of {theory: string, dimensionless_frequency: float}), 'dir_cnt' (array of objects {cnt_weight_frac: float, beta: float, excitation_frequency: float}), 'dir_cf' (array of objects {cf_volume_frac: float, beta: float, excitation_frequency: float}).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/computed_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### computed_results.json
- path: `/app/outputs/computed_results.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Contains validation benchmarks (natural frequencies, buckling loads, dimensionless frequencies) and DIR curves for multiple CNT weight fractions and CF volume fractions. The validation values will be compared against paper-reported benchmarks; the DIR trends will be checked for the required monotonic increase with reinforcement content.
- schema:
  - `type`: object
  - `required`:
    - `validation`: object
    - `dir_cnt`: array
    - `dir_cf`: array
  - `items`:
    - `natural_frequencies`:
      - `mode`: int
      - `frequency`: float
    - `buckling_loads`:
      - `BC`: string
      - `buckling_load`: float
    - `dimensionless_frequencies`:
      - `theory`: string
      - `dimensionless_frequency`: float
    - `cnt_weight_frac`: float
    - `cf_volume_frac`: float
    - `beta`: float
    - `excitation_frequency`: float (rad/s)
  - `required_columns`:
  - `units`:
    - `excitation_frequency`: rad/s

Notes: The checker will verify that validation frequencies, buckling loads, and dimensionless frequencies match literature benchmarks within appropriate tolerances. For the DIR data, structural checks will confirm that excitation frequency increases monotonically with increasing CNT weight fraction at a fixed β, and similarly with increasing CF volume fraction.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "computed_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": {
          "validation": "object",
          "dir_cnt": "array",
          "dir_cf": "array"
        },
        "items": {
          "natural_frequencies": {
            "mode": "int",
            "frequency": "float"
          },
          "buckling_loads": {
            "BC": "string",
            "buckling_load": "float"
          },
          "dimensionless_frequencies": {
            "theory": "string",
            "dimensionless_frequency": "float"
          },
          "cnt_weight_frac": "float",
          "cf_volume_frac": "float",
          "beta": "float",
          "excitation_frequency": "float (rad/s)"
        },
        "required_columns": [],
        "units": {
          "excitation_frequency": "rad/s"
        }
      },
      "description": "Contains validation benchmarks (natural frequencies, buckling loads, dimensionless frequencies) and DIR curves for multiple CNT weight fractions and CF volume fractions. The validation values will be compared against paper-reported benchmarks; the DIR trends will be checked for the required monotonic increase with reinforcement content."
    }
  ],
  "notes": "The checker will verify that validation frequencies, buckling loads, and dimensionless frequencies match literature benchmarks within appropriate tolerances. For the DIR data, structural checks will confirm that excitation frequency increases monotonically with increasing CNT weight fraction at a fixed β, and similarly with increasing CF volume fraction."
}
```

## How you are scored
A hidden verifier independently checks each part of your submission. The validation frequencies, buckling loads, and dimensionless frequencies are compared against reference values (from the literature, not provided to you) with appropriate per‑quantity tolerances. For the dynamic instability regions, the verifier performs a structural audit: at a fixed dynamic load factor β, the excitation frequency must follow a well‑defined monotonic relationship with the reinforcement content (CNT weight fraction and CF volume fraction). The rewards from the validation and the DIR checks are combined by weight, with the DIR component carrying the largest share. Supplying the expected trend without correctly computed data, or reporting values that do not arise from a genuine numerical solution, will not earn full credit.
