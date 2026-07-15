# DFT prediction of stability, elastic moduli, and hardness of hcp CrN₂

## Problem background
Transition-metal nitrides are attractive for their potential superhard properties. This work investigates whether hexagonal CrN₂ compounds, formed by incorporating nitrogen-nitrogen units into the chromium lattice, can be stabilized under pressure and exhibit high hardness. Understanding the interplay between pressure, N–N precompression, and electronic structure is key. The goal is to determine the conditions under which these CrN₂ phases become thermodynamically stable and to quantify their mechanical and electronic properties from first-principles calculations.

## Approach
The reproduction uses density functional theory (DFT) calculations with the local density approximation plus a Hubbard U correction (LDA+U) on Cr 3d orbitals to capture strong electron correlations. The workflow evaluates the formation enthalpy of hexagonal CrN₂ phases relative to orthorhombic CrN and high‑pressure α‑N₂ as a function of pressure, employing energy‑volume scans and Birch–Murnaghan equation‑of‑state fitting to determine the minimum pressure where CrN₂ becomes thermodynamically stable. Elastic constants are computed from strain‑stress calculations, and the resulting bulk, shear, and Young’s moduli are obtained via Voigt–Reuss–Hill averaging. Vickers hardness is estimated from the moduli using an empirical electronegativity model, and the electronic band gap is extracted from the Kohn–Sham eigenvalues. The calculations use publicly available pseudopotentials and reference structures, with all computational steps performed inside the open‑source Quantum ESPRESSO package. This establishes a self‑contained pipeline from structural inputs to property outputs.

## Reproduction target
Re‑run the DFT workflow to compute for WC‑CrN₂ and AsNi‑CrN₂: (1) the thermodynamic stability pressure (in GPa), defined as the lowest pressure where the formation enthalpy H_form(P) = H(CrN₂) – H(orth‑CrN) – H(N₂) becomes ≤ 0; (2) the elastic moduli: bulk modulus B, shear modulus G, and Young’s modulus E (all in GPa), obtained from the elastic constants via Voigt–Reuss–Hill averaging; (3) the Vickers hardness Hv (in GPa) using the Chen et al. electronegativity model; and (4) the fundamental electronic band gap (in eV). All results must be written to /app/outputs/results.json as a JSON object with keys: stability_pressure, bulk_modulus, shear_modulus, young_modulus, vickers_hardness, band_gap. The final quantitative comparison is against the expected values produced by the same LDA+U treatment; the agent must obtain these values by executing the full computational pipeline, not by copying reference numbers.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- PAW pseudopotentials (SSSP or PSlibrary): https://www.materialscloud.org/discover/sssp/
- High-pressure α-N₂ structure (Pickard & Needs 2009): 10.1103/PhysRevLett.102.125702

## Workflow steps

### Step 1: Prepare crystal structures
- Role: process
- Action: Set up input structure files for orth-CrN (orthorhombic, AF²[110]), WC-CrN₂, AsNi-CrN₂, and the high-pressure α-N₂ phase using the lattice parameters and atomic positions from the paper’s Table I (LDA+U values) and the nitrogen reference structure from Pickard & Needs. Ensure the structures are ready for DFT calculations.
- Evidence: `/app/outputs/structures.json`

### Step 2: DFT energy-volume scans
- Role: process
- Action: For each phase (orth-CrN, WC-CrN₂, AsNi-CrN₂, α-N₂), perform a series of self-consistent field (SCF) total-energy calculations at several volumes around the equilibrium volume using LDA+U with U=3 eV on Cr 3d (Dudarev scheme) and a plane-wave cutoff high enough to converge total energies to ~1 meV/atom. Record total energy and volume for each point.
- Evidence: `/app/outputs/energy_scan.json`

### Step 3: Elastic constants calculation
- Role: process
- Action: For WC-CrN₂ and AsNi-CrN₂ at their equilibrium volumes, compute the second-order elastic constants (C₁₁, C₁₂, C₁₃, C₃₃, C₄₄, C₆₆) using the strain-stress method implemented in Quantum ESPRESSO. Use the same DFT settings as in step s2.
- Evidence: `/app/outputs/elastic_constants.json`

### Step 4: Electronic band structure and density of states
- Role: process
- Action: For WC-CrN₂ and AsNi-CrN₂ at their equilibrium volumes, compute the electronic band structure and total density of states using the same DFT settings. Determine the fundamental band gap from the Kohn-Sham eigenvalues.
- Evidence: `/app/outputs/band_dos.json`

### Step 5: Analysis and reporting
- Role: scored (load-bearing)
- Action: From the energy-scan data, fit a Birch-Murnaghan equation of state for each phase to obtain E(V) and derive H(P)=E+PV. Compute the formation enthalpy H_form(P) = H(CrN₂) – H(orth-CrN) – H(N₂) and determine the lowest pressure where H_form ≤ 0 (stability pressure). Using the elastic constants, apply Voigt-Reuss-Hill averaging to compute bulk modulus B, shear modulus G, and Young’s modulus E. Compute Vickers hardness Hv using the Chen et al. electronegativity model. Report the band gap from step s4. Write all results to a single JSON file.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: JSON object with keys: stability_pressure (number, GPa), bulk_modulus (number, GPa), shear_modulus (number, GPa), young_modulus (number, GPa), vickers_hardness (number, GPa), band_gap (number, eV).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results.json
- path: `/app/outputs/results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: The agent's computed stability pressure, elastic moduli, Vickers hardness, and electronic band gap for CrN₂. The hidden checker compares each field to the paper’s reported LDA+U values using appropriate tolerances.
- schema:
  - `type`: object
  - `required`:
    - `stability_pressure`: number (GPa)
    - `bulk_modulus`: number (GPa)
    - `shear_modulus`: number (GPa)
    - `young_modulus`: number (GPa)
    - `vickers_hardness`: number (GPa)
    - `band_gap`: number (eV)
  - `items`: object
  - `required_columns`:
  - `units`:
    - `stability_pressure`: GPa
    - `bulk_modulus`: GPa
    - `shear_modulus`: GPa
    - `young_modulus`: GPa
    - `vickers_hardness`: GPa
    - `band_gap`: eV

Notes: Only LDA+U results are scored. The workflow uses Quantum ESPRESSO instead of VASP; the checker applies tolerances that account for the expected spread between different DFT codes and pseudopotential libraries.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "stability_pressure": "number (GPa)",
          "bulk_modulus": "number (GPa)",
          "shear_modulus": "number (GPa)",
          "young_modulus": "number (GPa)",
          "vickers_hardness": "number (GPa)",
          "band_gap": "number (eV)"
        },
        "items": {},
        "required_columns": [],
        "units": {
          "stability_pressure": "GPa",
          "bulk_modulus": "GPa",
          "shear_modulus": "GPa",
          "young_modulus": "GPa",
          "vickers_hardness": "GPa",
          "band_gap": "eV"
        }
      },
      "description": "The agent's computed stability pressure, elastic moduli, Vickers hardness, and electronic band gap for CrN₂. The hidden checker compares each field to the paper’s reported LDA+U values using appropriate tolerances."
    }
  ],
  "notes": "Only LDA+U results are scored. The workflow uses Quantum ESPRESSO instead of VASP; the checker applies tolerances that account for the expected spread between different DFT codes and pseudopotential libraries."
}
```

## How you are scored
A hidden verifier reads the submitted /app/outputs/results.json and evaluates each scored quantity against independently held gold values using appropriate tolerances. Each metric is scored individually and then combined into a total reward between 0 and 1. Only the numerical results in results.json are considered; the verifier does not re‑run any DFT calculation. Producing results that faithfully reflect a correct execution of the described workflow earns high credit; simply reporting known numbers without genuine computation is discouraged and will not score well. The precise tolerances and weighting are pre‑defined and hidden.
