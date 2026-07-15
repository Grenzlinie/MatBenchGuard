# Lattice Energy Deviations in Divalent Metal Halides

## Problem background
Ionic crystals of divalent metals often deviate from a purely ionic model. A standard way to quantify this deviation is to compare experimental lattice energies obtained from thermochemical cycles with theoretical lattice energies predicted by an ideal electrostatic model. This task computes, for a set of divalent metal halides, the experimental lattice energy via the Born-Haber cycle and the theoretical lattice energy using the Born equation; it then determines the difference Δ = U_exp − U_theo for each compound. The computed Δ values are subsequently examined for any systematic relationship with the cation's second ionization potential I₂.

## Approach
The workflow uses two well-established methods. (1) Experimental lattice energy U_exp is derived from the Born-Haber thermochemical cycle: U_exp = −ΔHf + L + I + 2D − 2E, where ΔHf is the heat of formation, L the sublimation energy of the metal, I the second ionization energy, D the atomization enthalpy of the halogen atom (taken twice for diatomic X₂), and E the electron affinity of the halogen atom (also taken twice). (2) Theoretical lattice energy U_theo starts from the Born electrostatic model: the zero-temperature energy U₀ = (e² z² N A_{r₀} / r₀) · (1 − 1/n) is calculated using the smallest cation–anion distance r₀ (or derived from the lattice constant), the Madelung constant A_{r₀} appropriate for the crystal structure type, and the Born exponent n. A small pressure–volume correction (a constant of a few kcal mol⁻¹) is then added to U₀ to approximate the room-temperature lattice energy U_theo. The difference Δ = U_exp − U_theo is computed for each compound. All needed input parameters—second ionization potentials, structure types and lattice parameters, Born exponents, heats of formation, sublimation energies, atomization enthalpies, and electron affinities—are taken from the public reference compilations listed in the Assets section. The relationship between Δ and I₂ is then evaluated across the compounds, grouped by anion (fluorides, chlorides, bromides, iodides).

## Reproduction target
Produce a CSV file (lattice_energies.csv) containing, for every divalent metal halide compound listed in the compiled reference data, the following columns: compound name, structure type, second ionization potential I₂ (eV), experimental lattice energy U_exp (kcal mol⁻¹), theoretical lattice energy U_theo (kcal mol⁻¹), and their difference Δ (kcal mol⁻¹). Additionally, within each of the four halide families (fluorides, chlorides, bromides, iodides), verify whether Δ increases monotonically with increasing I₂.

## Assets

- Ionization potentials (FINKELNBURG and HUMBACH, 1955)
- Crystallographic data (WYCKOFF)
- Born exponents (PAULING, 1940)
- Thermochemical data (ROSSINI et al., 1952 / LONG, 1953)
- Atomization enthalpy of fluorine (BARROW and CAUNT, 1953)
- Electron affinities (PRITCHARD, 1953)
- Physical constants and Madelung constants

## Workflow steps

### Step 1: Compile reference dataset
- Role: process
- Action: Collect the required parameters (I2, structure type, lattice constant a0 or nearest-neighbour distance r0, Born exponent n, ΔHf, L, D, E) for every compound listed in the divalent halide tables from the cited literature sources. Organise the values in a structured format (e.g., a table or CSV) for the next step.
- Evidence: `/app/outputs/compiled_inputs.csv`

### Step 2: Compute lattice energies and delta
- Role: scored (load-bearing)
- Action: For each compound from the compiled data: (1) compute U_exp using the Born-Haber relation U_exp = -ΔHf + L + I + 2D - 2E (note: for divalent halides, the halogen terms appear twice). (2) Obtain U0 from the Born equation U0 = e² z² N A_{r0} / r0 * (1 - 1/n), using the appropriate Madelung constant and Born exponent for the structure type. (3) Apply a small constant pressure-volume correction to U0 to get U_theo = U0 + correction. (4) Calculate Δ = U_exp - U_theo. (5) Output the results as a CSV with columns: compound, structure_type, I2 (in eV), U_exp (kcal/mol), U_theo (kcal/mol), delta (kcal/mol). Include all compounds from the original divalent halide tables.
- Output file: `/app/outputs/lattice_energies.csv`
- Format: csv
- Contract: CSV with columns: compound (string), structure_type (string), I2 (float, eV), U_exp (float, kcal/mol), U_theo (float, kcal/mol), delta (float, kcal/mol). One row per compound from the divalent halide tables.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/lattice_energies.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### lattice_energies.csv
- path: `/app/outputs/lattice_energies.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Computed lattice energies and deviations for all divalent metal halides listed in the paper. The checker verifies the delta values against the paper's reported values (with tolerance) and computes Spearman correlation between delta and I2 per halide family.
- schema:
  - `type`: table
  - `required_columns`: `compound`, `structure_type`, `I2`, `U_exp`, `U_theo`, `delta`
  - `units`:
    - `I2`: eV
    - `U_exp`: kcal/mol
    - `U_theo`: kcal/mol
    - `delta`: kcal/mol

Notes: The task requires the agent to compile input data from the specified public references and then perform the numerical calculations. No hidden test split is used; the scoring is based on comparison with the paper's reported delta values and the expected monotonic trend between delta and second ionization potential.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "lattice_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "compound",
          "structure_type",
          "I2",
          "U_exp",
          "U_theo",
          "delta"
        ],
        "units": {
          "I2": "eV",
          "U_exp": "kcal/mol",
          "U_theo": "kcal/mol",
          "delta": "kcal/mol"
        }
      },
      "description": "Computed lattice energies and deviations for all divalent metal halides listed in the paper. The checker verifies the delta values against the paper's reported values (with tolerance) and computes Spearman correlation between delta and I2 per halide family."
    }
  ],
  "notes": "The task requires the agent to compile input data from the specified public references and then perform the numerical calculations. No hidden test split is used; the scoring is based on comparison with the paper's reported delta values and the expected monotonic trend between delta and second ionization potential."
}
```

## How you are scored
A hidden verifier will independently evaluate your submitted lattice_energies.csv. It will compare each reported Δ value against a hidden reference and also check the monotonic trend between Δ and I₂ within each halide family. Your final reward is a weighted combination of the fraction of compounds whose Δ values agree within an acceptable tolerance and the strength of the monotonic correlation between Δ and I₂ per anion family. Reporting the correct trend and accurate values jointly determines your score. No gold values or tolerances are revealed in advance.
