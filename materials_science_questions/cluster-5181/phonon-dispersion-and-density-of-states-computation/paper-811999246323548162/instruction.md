# DFT-LDA Structural, Electronic, and Phonon Properties of Rocksalt GeSn

## Problem background
GeSn alloys in the rocksalt structure are technologically interesting for group-IV optoelectronic devices, yet accurate first-principles benchmarks of their structural, electronic, and vibrational properties remain limited. This work targets a first-principles investigation of rocksalt GeSn using density-functional theory within the local-density approximation (LDA), aiming to provide a consistent set of computed quantities that can serve as a reference for future studies. The quantities to establish are the equilibrium lattice constant, bulk modulus and its pressure derivative, the electronic band structure, and the phonon dispersion.

## Approach
The approach relies on plane-wave density-functional theory in the local-density approximation. Norm-conserving pseudopotentials are used to describe the ion-electron interactions. A two-atom rocksalt unit cell is employed. First, total energies are computed for a set of lattice constants spanning the expected equilibrium region. An equation of state (e.g., Birch-Murnaghan) is fitted to these energy-vs-volume data to extract the equilibrium lattice constant, bulk modulus, and its pressure derivative. Using the optimized lattice constant, a self-consistent charge-density calculation is performed, followed by a non-self-consistent band-structure calculation along the high-symmetry k-point path $\Gamma\rightarrow X\rightarrow W\rightarrow L\rightarrow \Gamma$ in the rocksalt Brillouin zone. Finally, phonon frequencies are obtained along the same high-symmetry path via density-functional perturbation theory (DFPT). All steps produce structured numerical outputs that are saved as JSON files.

## Reproduction target
Carry out the following computational workflow and produce the three specified output files.

1. **Total energy vs lattice constant scan**: Run DFT-LDA total-energy calculations for rocksalt GeSn at several lattice constants to collect energy-vs-volume data. Fit an equation of state to obtain the equilibrium lattice constant, bulk modulus, and pressure derivative. Save these three values as `structural_params.json` (format: JSON object with keys `lattice_constant_A`, `bulk_modulus_Mbar`, `bulk_modulus_pressure_derivative`).

2. **Electronic band structure**: At the equilibrium lattice constant, perform a self-consistent DFT-LDA calculation and then compute the electronic band energies along the high-symmetry k-point path $\Gamma\rightarrow X\rightarrow W\rightarrow L\rightarrow \Gamma$. Output a JSON array where each element is an object with a `kpoint` (crystal coordinates as a three-element array) and an `eigenvalues` array (band energies in eV). Save as `band_structure.json`.

3. **Phonon dispersion**: Using the same equilibrium lattice constant and the same high-symmetry path, compute phonon frequencies via density-functional perturbation theory. Output a JSON array where each element is an object with a `kpoint` (crystal coordinates) and a `frequencies_cm1` array (phonon frequencies in cm⁻¹). Save as `phonon_dispersion.json`.

All outputs must respect the schemas given in the output contract.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org
- Norm-conserving pseudopotentials for Ge and Sn (e.g., PseudoDojo library): http://www.pseudo-dojo.org

## Workflow steps

### Step 1: Total energy vs lattice constant scan
- Role: process
- Action: Perform DFT-LDA total energy calculations for rocksalt GeSn at several lattice constants spanning the expected equilibrium region. Use norm-conserving pseudopotentials and appropriate kinetic energy cutoff and k-point density. Record total energies and corresponding lattice constants.
- Evidence: `/app/outputs/total_energies.csv`

### Step 2: Structural parameters from E(a) fit
- Role: scored (load-bearing)
- Action: Fit an equation of state (e.g., Birch-Murnaghan) to the total energy versus lattice constant data to determine the equilibrium lattice constant, bulk modulus, and pressure derivative. Write the three values to structural_params.json.
- Output file: `/app/outputs/structural_params.json`
- Format: json
- Contract: {"lattice_constant_A": float, "bulk_modulus_Mbar": float, "bulk_modulus_pressure_derivative": float}
- Scoring: scored by hidden verifier

### Step 3: Electronic band structure
- Role: scored
- Action: Using the equilibrium lattice constant, perform a self-consistent DFT-LDA calculation and then compute the electronic band energies along the high-symmetry path Γ→X→W→L→Γ in the rocksalt Brillouin zone. Output a JSON array of k-point coordinates (crystal coordinates) and eigenvalues (eV).
- Output file: `/app/outputs/band_structure.json`
- Format: json
- Contract: [{"kpoint": [float, float, float], "eigenvalues": [float, ...]}, ...]
- Scoring: scored by hidden verifier

### Step 4: Phonon dispersion
- Role: scored
- Action: Using density functional perturbation theory (DFPT), compute phonon frequencies at the equilibrium lattice constant along the same high-symmetry path as the band structure. Output a JSON array of q-point coordinates (crystal coordinates) and phonon frequencies (cm⁻¹).
- Output file: `/app/outputs/phonon_dispersion.json`
- Format: json
- Contract: [{"kpoint": [float, float, float], "frequencies_cm1": [float, ...]}, ...]
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/structural_params.json`
- `/app/outputs/band_structure.json`
- `/app/outputs/phonon_dispersion.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### structural_params.json
- path: `/app/outputs/structural_params.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Equilibrium structural parameters extracted from the total-energy equation of state fit.
- schema:
  - `type`: object
  - `required`:
    - `lattice_constant_A`: float
    - `bulk_modulus_Mbar`: float
    - `bulk_modulus_pressure_derivative`: float
  - `units`:
    - `lattice_constant_A`: angstrom
    - `bulk_modulus_Mbar`: Mbar
    - `bulk_modulus_pressure_derivative`: dimensionless

### band_structure.json
- path: `/app/outputs/band_structure.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Electronic band energies along high-symmetry k-points. The array contains one object per k-point with its coordinates and a list of band eigenvalues.
- schema:
  - `type`: array
  - `items`:
    - `kpoint`: `float`, `float`, `float`
    - `eigenvalues`: `float`
  - `units`:
    - `kpoint`: crystal coordinates
    - `eigenvalues`: eV

### phonon_dispersion.json
- path: `/app/outputs/phonon_dispersion.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Phonon frequencies along high-symmetry q-points. The array contains one object per q-point with its coordinates and a list of phonon mode frequencies.
- schema:
  - `type`: array
  - `items`:
    - `kpoint`: `float`, `float`, `float`
    - `frequencies_cm1`: `float`
  - `units`:
    - `kpoint`: crystal coordinates
    - `frequencies_cm1`: cm^-1

Notes: Scoring compares the equilibrium lattice constant, bulk modulus, pressure derivative, selected band gaps, and phonon frequencies at high-symmetry points against hidden reference values with tolerances that accommodate typical toolchain variations (pseudopotential choice, convergence settings). No explicit gold values or tolerances are revealed to the solver.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "structural_params.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "lattice_constant_A": "float",
          "bulk_modulus_Mbar": "float",
          "bulk_modulus_pressure_derivative": "float"
        },
        "units": {
          "lattice_constant_A": "angstrom",
          "bulk_modulus_Mbar": "Mbar",
          "bulk_modulus_pressure_derivative": "dimensionless"
        }
      },
      "description": "Equilibrium structural parameters extracted from the total-energy equation of state fit."
    },
    {
      "file": "band_structure.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "array",
        "items": {
          "kpoint": [
            "float",
            "float",
            "float"
          ],
          "eigenvalues": [
            "float"
          ]
        },
        "units": {
          "kpoint": "crystal coordinates",
          "eigenvalues": "eV"
        }
      },
      "description": "Electronic band energies along high-symmetry k-points. The array contains one object per k-point with its coordinates and a list of band eigenvalues."
    },
    {
      "file": "phonon_dispersion.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "array",
        "items": {
          "kpoint": [
            "float",
            "float",
            "float"
          ],
          "frequencies_cm1": [
            "float"
          ]
        },
        "units": {
          "kpoint": "crystal coordinates",
          "frequencies_cm1": "cm^-1"
        }
      },
      "description": "Phonon frequencies along high-symmetry q-points. The array contains one object per q-point with its coordinates and a list of phonon mode frequencies."
    }
  ],
  "notes": "Scoring compares the equilibrium lattice constant, bulk modulus, pressure derivative, selected band gaps, and phonon frequencies at high-symmetry points against hidden reference values with tolerances that accommodate typical toolchain variations (pseudopotential choice, convergence settings). No explicit gold values or tolerances are revealed to the solver."
}
```

## How you are scored
A hidden verifier reads your submitted output files and assigns a score between 0 and 1. Each scored artifact is evaluated independently against reference quantities that are derived from the paper's own results. For `structural_params.json`, the verifier extracts the lattice constant, bulk modulus, and pressure derivative and compares them to hidden reference values. For `band_structure.json`, it computes band-gap related quantities at specific high-symmetry points from your reported eigenvalues and compares them to hidden reference values. For `phonon_dispersion.json`, it extracts phonon frequencies at selected high-symmetry points and compares them to hidden reference values. The comparisons use hidden tolerances that account for the expected spread due to different computational setups (e.g., pseudopotential choice, convergence settings). Better-than-paper results are never penalized. The three stages are weighted so that the final reward reflects the overall reproduction quality. Simply writing numbers without executing the required simulations will not yield a high score.
