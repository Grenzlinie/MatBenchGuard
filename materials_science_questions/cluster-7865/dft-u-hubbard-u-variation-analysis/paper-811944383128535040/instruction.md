# Spin-polarized LDA+U calculation of Eu 4f states and magnetic moments in Ga0.9375Eu0.0625N

## Problem background
Dilute magnetic semiconductors (DMS) based on rare-earth-doped GaN are of interest for spintronics and optoelectronics. This study investigates the electronic and magnetic properties of Eu-doped zinc-blende GaN (Ga₀.₉₃₇₅Eu₀.₀₆₂₅N) using first-principles LDA+U calculations. It aims to characterize the position and spin polarization of Eu 4f states, the effective f‑band exchange splitting, the valence‑band maximum exchange splitting, the total and local magnetic moments, and the exchange constants N₀α and N₀β, thereby providing insight into how rare-earth doping differs from transition-metal doping in DMSs.

## Approach
Perform spin‑polarized density‑functional theory (DFT) calculations within the LDA+U approximation to treat the strongly correlated Eu 4f electrons. Use a 32‑atom supercell of zinc‑blende GaN where one Ga atom is replaced by Eu, corresponding to a doping concentration of x = 0.0625. Adopt the equilibrium lattice constant (4.51 Å) obtained in the original study. From the self‑consistent electronic structure, compute total and partial densities of states (DOS) to identify the Eu 4f spin‑up and spin‑down peak positions. Derive the effective f‑band exchange splitting Δₓ(f) and the valence‑band maximum exchange splitting Δ. Extract the total magnetic moment and the local magnetic moments on Eu, N, Ga, and the interstitial region. Finally, evaluate the exchange constants N₀α and N₀β from the spin splitting of the conduction‑ and valence‑band edges.

## Reproduction target
Produce the following quantities from a spin‑polarized LDA+U calculation on the 32‑atom supercell of zinc‑blende Ga₀.₉₃₇₅Eu₀.₀₆₂₅N at lattice constant 4.51 Å: (1) majority‑spin (spin‑up) Eu 4f peak position (eV), (2) minority‑spin (spin‑down) Eu 4f peak positions (eV), (3) effective f‑band exchange splitting Δₓ(f) (eV), (4) valence‑band maximum exchange splitting Δ (eV), (5) total magnetic moment (μ_B/cell), (6) local magnetic moments on Eu, N, Ga atoms and interstitial (μ_B), and (7) exchange constants N₀α and N₀β (eV). Write all results into a single JSON file.

## Assets

- Quantum ESPRESSO (open-source DFT code): https://www.quantum-espresso.org/
- Pseudopotential library (PSLibrary or GBRV): https://pseudopotentials.quantum-espresso.org/legacy_tables/ps-library/

## Workflow steps

### Step 1: Self-consistent LDA+U calculation
- Role: process
- Action: Run a spin-polarized DFT+U calculation for the 32-atom supercell of zinc-blende Ga0.9375Eu0.0625N at the reported equilibrium lattice constant 4.51 A. Use Hubbard U=0.44 Ry, J=0.07 Ry (Ueff = U-J). Choose convergent plane-wave cutoff and k-point sampling to obtain a well-converged electronic structure.
- Evidence: `/app/outputs/scf.log`

### Step 2: Extract electronic structure properties
- Role: scored (load-bearing)
- Action: From the self-consistent results, compute total and partial density of states. Identify the Eu 4f majority-spin (spin-up) peak center and the minority-spin (spin-down) peak positions. Calculate the effective f-band exchange splitting Δ_x(f) (separation between corresponding spin-up and spin-down peaks) and the valence-band maximum exchange splitting Δ = Ev↑ − Ev↓. Extract the total magnetic moment and the local moments on Eu, N, Ga, and the interstitial region. Compute the exchange constants N0α and N0β from the spin splitting of the conduction- and valence-band edges. Write all quantities to a JSON file.
- Output file: `/app/outputs/computed_properties.json`
- Format: json
- Contract: {"Eu_4f_up_peak": float, "Eu_4f_down_peak1": float, "Eu_4f_down_peak2": float, "Delta_x_f": float, "Delta": float, "total_magnetic_moment": float, "Eu_magnetic_moment": float, "N_magnetic_moment": float, "Ga_magnetic_moment": float, "interstitial_magnetic_moment": float, "N0_alpha": float, "N0_beta": float}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/computed_properties.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### computed_properties.json
- path: `/app/outputs/computed_properties.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Numerical properties extracted from the LDA+U calculation, to be compared against paper-reported reference values with tolerances.
- schema:
  - `type`: object
  - `required`:
    - `Eu_4f_up_peak`: number (eV)
    - `Eu_4f_down_peak1`: number (eV)
    - `Eu_4f_down_peak2`: number (eV)
    - `Delta_x_f`: number (eV)
    - `Delta`: number (eV)
    - `total_magnetic_moment`: number (μ_B)
    - `Eu_magnetic_moment`: number (μ_B)
    - `N_magnetic_moment`: number (μ_B)
    - `Ga_magnetic_moment`: number (μ_B)
    - `interstitial_magnetic_moment`: number (μ_B)
    - `N0_alpha`: number (eV)
    - `N0_beta`: number (eV)
  - `items`: object
  - `required_columns`:
  - `units`:
    - `Eu_4f_up_peak`: eV
    - `Eu_4f_down_peak1`: eV
    - `Eu_4f_down_peak2`: eV
    - `Delta_x_f`: eV
    - `Delta`: eV
    - `total_magnetic_moment`: μ_B
    - `Eu_magnetic_moment`: μ_B
    - `N_magnetic_moment`: μ_B
    - `Ga_magnetic_moment`: μ_B
    - `interstitial_magnetic_moment`: μ_B
    - `N0_alpha`: eV
    - `N0_beta`: eV

Notes: The exchange constants and magnetic moments are compared to the paper's values using absolute tolerances appropriate for basis-set and pseudopotential differences. The spin-density contour plot is not scored.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "computed_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "Eu_4f_up_peak": "number (eV)",
          "Eu_4f_down_peak1": "number (eV)",
          "Eu_4f_down_peak2": "number (eV)",
          "Delta_x_f": "number (eV)",
          "Delta": "number (eV)",
          "total_magnetic_moment": "number (μ_B)",
          "Eu_magnetic_moment": "number (μ_B)",
          "N_magnetic_moment": "number (μ_B)",
          "Ga_magnetic_moment": "number (μ_B)",
          "interstitial_magnetic_moment": "number (μ_B)",
          "N0_alpha": "number (eV)",
          "N0_beta": "number (eV)"
        },
        "items": {},
        "required_columns": [],
        "units": {
          "Eu_4f_up_peak": "eV",
          "Eu_4f_down_peak1": "eV",
          "Eu_4f_down_peak2": "eV",
          "Delta_x_f": "eV",
          "Delta": "eV",
          "total_magnetic_moment": "μ_B",
          "Eu_magnetic_moment": "μ_B",
          "N_magnetic_moment": "μ_B",
          "Ga_magnetic_moment": "μ_B",
          "interstitial_magnetic_moment": "μ_B",
          "N0_alpha": "eV",
          "N0_beta": "eV"
        }
      },
      "description": "Numerical properties extracted from the LDA+U calculation, to be compared against paper-reported reference values with tolerances."
    }
  ],
  "notes": "The exchange constants and magnetic moments are compared to the paper's values using absolute tolerances appropriate for basis-set and pseudopotential differences. The spin-density contour plot is not scored."
}
```

## How you are scored
A hidden verifier independently evaluates each workflow stage's artifact. It reads your computed_properties.json and compares every numerical entry against reference values using appropriate absolute tolerances that account for the use of a different DFT code and pseudopotentials. A reward is assigned based on how many of the quantities fall within tolerance, with primary weight placed on the f‑band exchange splitting and the Eu 4f peak positions, and secondary weight on the magnetic moments and exchange constants. The final score is the weighted combination of these comparisons. Simply reporting the reference numbers without executing the computation will not succeed.
