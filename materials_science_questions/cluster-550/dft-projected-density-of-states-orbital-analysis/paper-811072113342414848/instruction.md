# DFT Structural and Electronic Properties of InAsNP Quaternary Alloys

## Problem background
III-V semiconductor alloys, particularly quaternary systems like InAsN_P, offer tunable lattice constants, bulk moduli, and band gaps, making them attractive for optoelectronic and photovoltaic applications. First-principles density functional theory (DFT) calculations can predict structural, electronic, and optical properties as functions of composition, providing guidance for band-gap engineering without immediate experimental synthesis. This task investigates the composition-dependent trends of equilibrium structural parameters, band gaps, and static refractive indices for a set of zinc-blende InAs_x N_y P_{1-x-y} alloys.

## Approach
The reproduction uses an open-source plane-wave DFT code (e.g., Quantum ESPRESSO) with pseudopotentials. For each binary (InN, InP, InAs) and quaternary (InAs₀.₂₅N₀.₂₅P₀.₅, InAs₀.₂₅N₀.₅P₀.₂₅, InAs₀.₅N₀.₂₅P₀.₂₅) composition, a zinc-blende supercell of 8 atoms is constructed. Structural parameters are obtained by performing total-energy calculations at a series of volumes, then fitting the resulting energy-volume data to the Birch-Murnaghan equation of state to extract the equilibrium lattice constant, bulk modulus, and its pressure derivative. For the electronic structure, the TB-mBJ meta-GGA functional is used to compute the band structure; the direct (Γ→Γ) and indirect (Γ→X) band gaps are extracted. Finally, for the three quaternary alloys the frequency-dependent dielectric function is calculated, and the static refractive index n(0) is derived from the real part at zero frequency, ε₁(0).

## Reproduction target
Produce three JSON files containing the computed properties.

- `structural_properties.json`: equilibrium lattice constant a (Å), bulk modulus B (GPa), and pressure derivative B' for each of the six compositions: InN, InP, InAs, InAs₀.₂₅N₀.₂₅P₀.₅, InAs₀.₂₅N₀.₅P₀.₂₅, InAs₀.₅N₀.₂₅P₀.₂₅.
- `band_gaps.json`: direct band gap E_g_direct (eV) and indirect band gap E_g_indirect (eV) for the same six compositions, from the meta-GGA calculation.
- `quaternary_refractive_index.json`: static refractive index n(0) for each of the three quaternary alloys.

## Assets

- Quantum ESPRESSO (or equivalent open-source DFT code): https://www.quantum-espresso.org/
- Pseudopotential library (e.g., SSSP efficiency): https://www.materialscloud.org/discover/sssp/table/efficiency
- LDA/GGA exchange-correlation functionals
- TB-mBJ meta-GGA functional

## Workflow steps

### Step 1: Build supercell models
- Role: process
- Action: Construct zinc-blende supercells of 8 atoms for the binary compounds InN, InP, InAs and the quaternary alloys InAs₀.₂₅N₀.₂₅P₀.₅, InAs₀.₂₅N₀.₅P₀.₂₅, InAs₀.₅N₀.₂₅P₀.₂₅. Use the standard zinc-blende structure and appropriate atomic positions for each composition.
- Evidence: none

### Step 2: Total-energy vs volume DFT calculations
- Role: process
- Action: For each composition, perform LDA or GGA DFT calculations at a range of unit cell volumes around the equilibrium. Use a sufficiently dense k-point mesh and a plane-wave cutoff to converge total energies. Record the volume and total energy for each calculation.
- Evidence: none

### Step 3: Fit equation of state and extract structural parameters
- Role: scored (load-bearing)
- Action: Fit the computed energy-volume data to the Birch-Murnaghan equation of state for each composition. Extract the equilibrium lattice constant a, bulk modulus B, and first pressure derivative of the bulk modulus B'. Output a JSON object where each composition is a key mapping to an object with fields a (Å), B (GPa), B' (dimensionless).
- Output file: `/app/outputs/structural_properties.json`
- Format: json
- Contract: {"InN": {"a": "float, Å", "B": "float, GPa", "B_prime": "float, dimensionless"}, ... (for InP, InAs, InAs0.25N0.25P0.5, InAs0.25N0.5P0.25, InAs0.5N0.25P0.25)}
- Scoring: scored by hidden verifier

### Step 4: Compute band structures and extract band gaps
- Role: scored (load-bearing)
- Action: Using the TB-mBJ meta-GGA functional, perform a band structure calculation at the equilibrium lattice parameters for all compositions. Extract the direct band gap (Γ→Γ) and the indirect band gap (Γ→X) in eV. Output a JSON object with compositions as keys, each having E_g_direct (eV) and E_g_indirect (eV).
- Output file: `/app/outputs/band_gaps.json`
- Format: json
- Contract: {"InN": {"E_g_direct": "float, eV", "E_g_indirect": "float, eV"}, ... (for InP, InAs, InAs0.25N0.25P0.5, InAs0.25N0.5P0.25, InAs0.5N0.25P0.25)}
- Scoring: scored by hidden verifier

### Step 5: Compute static refractive index for quaternary alloys
- Role: scored
- Action: Calculate the frequency-dependent dielectric function for the three quaternary alloys. Extract the real part at zero frequency ε₁(0) and compute the static refractive index n(0) = sqrt(ε₁(0)). Output a JSON object with each quaternary composition as a key and its n0 value (dimensionless).
- Output file: `/app/outputs/quaternary_refractive_index.json`
- Format: json
- Contract: {"InAs0.25N0.25P0.5": "float, dimensionless", "InAs0.25N0.5P0.25": "float, dimensionless", "InAs0.5N0.25P0.25": "float, dimensionless"}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/structural_properties.json`
- `/app/outputs/band_gaps.json`
- `/app/outputs/quaternary_refractive_index.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### structural_properties.json
- path: `/app/outputs/structural_properties.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Equilibrium structural parameters from Birch-Murnaghan equation-of-state fitting.
- schema:
  - `type`: object
  - `description`: Object keyed by composition string (e.g., "InN"). Each value is an object with numeric fields: a (lattice constant in Å), B (bulk modulus in GPa), B_prime (dimensionless). Compositions: InN, InP, InAs, InAs0.25N0.25P0.5, InAs0.25N0.5P0.25, InAs0.5N0.25P0.25.

### band_gaps.json
- path: `/app/outputs/band_gaps.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Band gap energies from TB-mBJ meta-GGA calculation.
- schema:
  - `type`: object
  - `description`: Object keyed by composition string. Each value is an object with numeric fields: E_g_direct (direct band gap Γ→Γ in eV), E_g_indirect (indirect band gap Γ→X in eV). Compositions: InN, InP, InAs, InAs0.25N0.25P0.5, InAs0.25N0.5P0.25, InAs0.5N0.25P0.25.

### quaternary_refractive_index.json
- path: `/app/outputs/quaternary_refractive_index.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Static refractive index from DFT dielectric function.
- schema:
  - `type`: object
  - `description`: Object keyed by quaternary composition string. Each value is a numeric static refractive index n(0) (dimensionless) derived from ε₁(0). Compositions: InAs0.25N0.25P0.5, InAs0.25N0.5P0.25, InAs0.5N0.25P0.25.

Notes: All values must be obtained from first-principles DFT calculations. The hidden checker compares against the paper's reported values using tolerances appropriate for different DFT implementations.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "structural_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "description": "Object keyed by composition string (e.g., \"InN\"). Each value is an object with numeric fields: a (lattice constant in Å), B (bulk modulus in GPa), B_prime (dimensionless). Compositions: InN, InP, InAs, InAs0.25N0.25P0.5, InAs0.25N0.5P0.25, InAs0.5N0.25P0.25."
      },
      "description": "Equilibrium structural parameters from Birch-Murnaghan equation-of-state fitting."
    },
    {
      "file": "band_gaps.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "description": "Object keyed by composition string. Each value is an object with numeric fields: E_g_direct (direct band gap Γ→Γ in eV), E_g_indirect (indirect band gap Γ→X in eV). Compositions: InN, InP, InAs, InAs0.25N0.25P0.5, InAs0.25N0.5P0.25, InAs0.5N0.25P0.25."
      },
      "description": "Band gap energies from TB-mBJ meta-GGA calculation."
    },
    {
      "file": "quaternary_refractive_index.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "description": "Object keyed by quaternary composition string. Each value is a numeric static refractive index n(0) (dimensionless) derived from ε₁(0). Compositions: InAs0.25N0.25P0.5, InAs0.25N0.5P0.25, InAs0.5N0.25P0.25."
      },
      "description": "Static refractive index from DFT dielectric function."
    }
  ],
  "notes": "All values must be obtained from first-principles DFT calculations. The hidden checker compares against the paper's reported values using tolerances appropriate for different DFT implementations."
}
```

## How you are scored
A hidden verifier reads your output files and compares each computed value against a reference value using appropriate tolerances. Each of the three scored artifacts carries a weight; the final reward is the weighted sum across them. Simply reporting numbers is not sufficient—the verifier checks that your results are physically reasonable and consistent with the expected composition trends. Correct execution of the full DFT workflow as outlined in the steps is required to receive credit.
