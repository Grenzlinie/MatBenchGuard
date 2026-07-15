# Electronic Structure and Transport Coefficient Reproduction for a Layered Intermetallic Superconductor

## Problem background
The ternary intermetallic compound LaNiGa₂ is a layered orthorhombic superconductor (space group Cmmm) that has been proposed to exhibit triplet pairing. Understanding its electronic structure and transport properties is essential for evaluating the superconducting mechanism. First-principles calculations can provide the Fermi-level density of states, Drude plasma frequencies, and thermopower, and when combined with experimental specific heat data, yield the electron‑phonon coupling constant. This task reproduces these key electronic and transport quantities from first principles.

## Approach
The reproduction relies on density functional theory in the generalized gradient approximation of Perdew, Burke, and Ernzerhof (PBE) with scalar‑relativistic treatment. The crystal structure is fixed at the experimental lattice constants (a = 4.29 Å, b = 17.83 Å, c = 4.273 Å) with the relaxed internal coordinates listed in the workflow. From the self‑consistent charge density and band structure, the total density of states at the Fermi energy N(E_F) and the diagonal components of the Drude plasma frequency tensor are extracted. Boltzmann transport theory within the constant relaxation time approximation (at 300 K) yields the Seebeck coefficient tensor. Finally, the electron‑phonon coupling constant λ is inferred by comparing the computed N(E_F) with the experimental specific heat coefficient γ_exp = 11.64 mJ mol⁻¹ K⁻², using the free‑electron formula γ_bare = (π²/3) k_B² N(E_F) (e N_A) × 1000 and λ = (γ_exp/γ_bare) − 1. Open‑source tools (Quantum ESPRESSO, SSSP pseudopotentials, BoltzTraP2) and standard Python packages are used throughout.

## Reproduction target
Produce the following quantities from the prescribed DFT and Boltzmann‑transport workflow:
- The total density of states at the Fermi level, N(E_F), in eV⁻¹ per formula unit (both spins).
- The diagonal Drude plasma frequencies ℏΩₚ for the three crystal directions (xx, yy, zz) in eV.
- The diagonal Seebeck coefficient components at 300 K for the three directions in μV/K.
- The electron‑phonon coupling constant λ derived from N(E_F) and the experimental γ_exp given above.
All results must be written to the exact output files and formats specified in the workflow steps.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP efficiency pseudopotentials: https://www.materialscloud.org/discover/sssp/table/efficiency
- BoltzTraP2: https://gitlab.com/sousaw/BoltzTraP2
- Python packages (numpy, scipy, pandas): https://pypi.org
- Experimental specific heat coefficient γ of LaNiGa₂: 10.1103/PhysRevB.66.092503

## Workflow steps

### Step 1: DFT electronic structure calculation
- Role: process
- Action: Perform a self-consistent DFT calculation for LaNiGa₂ using the experimental lattice parameters (a=4.29 Å, b=17.83 Å, c=4.273 Å) and the relaxed atomic coordinates (La at (0, 0.3591, 0.5); Ni at (0, 0.0719, 0.0); Ga1 at (0, 0.2092, 0.0); Ga2 at (0, 0, 0.5); Ga3 at (0, 0, 0.0)). Use the PBE functional, scalar relativistic treatment, and a plane-wave pseudopotential code (e.g., Quantum ESPRESSO). Compute the self-consistent charge density, the band structure on a dense k‑mesh suitable for transport, and the optical matrix elements. Save all outputs for post-processing.
- Evidence: `/app/outputs/dft_output.tar.gz`

### Step 2: Compute N(E_F)
- Role: scored (load-bearing)
- Action: From the DFT output, extract the total electronic density of states at the Fermi energy N(E_F). Report the value in eV⁻¹ per formula unit for both spins.
- Output file: `/app/outputs/step_03_N(E_F).txt`
- Format: txt
- Contract: Single line: N(E_F) in eV⁻¹ per formula unit.
- Scoring: scored by hidden verifier

### Step 3: Compute Drude plasma frequencies
- Role: scored
- Action: From the DFT optical matrix elements, compute the Drude plasma frequencies ℏΩ_p for the three diagonal directions (xx, yy, zz) in eV. Write a CSV file with one row per direction.
- Output file: `/app/outputs/step_04_plasma_frequencies.csv`
- Format: csv
- Contract: Columns: direction (string, one of xx,yy,zz), hbar_omega_p (numeric, in eV).
- Scoring: scored by hidden verifier

### Step 4: BoltzTraP2 transport calculation
- Role: process
- Action: Using the DFT band structure (energies on a dense k‑mesh), run BoltzTraP2 within the constant relaxation time approximation to compute the Seebeck coefficient tensor at 300 K. Save the BoltzTraP2 output for later extraction.
- Evidence: `/app/outputs/boltz_output.tar.gz`

### Step 5: Extract Seebeck coefficients
- Role: scored
- Action: From the BoltzTraP2 output, extract the diagonal components of the Seebeck coefficient at 300 K (S_xx, S_yy, S_zz) in μV/K. Write a CSV file with one row per direction.
- Output file: `/app/outputs/step_05_thermopower_300K.csv`
- Format: csv
- Contract: Columns: direction (string, one of xx,yy,zz), S_300K (numeric, in μV/K).
- Scoring: scored by hidden verifier

### Step 6: Compute superconducting coupling constant λ
- Role: scored
- Action: Compute the bare specific heat coefficient γ_bare from the calculated N(E_F) (step_02) using the standard free‑electron formula: γ_bare = (π²/3) k_B² N(E_F) (e N_A) × 1000, with k_B = 8.617333262e-5 eV/K, e = 1.602176634e-19 C, N_A = 6.02214076e23 mol⁻¹, giving γ_bare in mJ mol⁻¹ K⁻². Then compute λ = (γ_exp / γ_bare) − 1, where γ_exp = 11.64 mJ mol⁻¹ K⁻² is the experimental specific heat coefficient from literature (Zeng and Lee, Phys. Rev. B 66, 092503 (2002)). Write the resulting λ as a single number.
- Output file: `/app/outputs/step_06_lambda.txt`
- Format: txt
- Contract: Single line: λ (dimensionless).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_03_N(E_F).txt`
- `/app/outputs/step_04_plasma_frequencies.csv`
- `/app/outputs/step_05_thermopower_300K.csv`
- `/app/outputs/step_06_lambda.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_03_N(E_F).txt
- path: `/app/outputs/step_03_N(E_F).txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: Total electronic density of states at E_F, a key input for λ and a test of the DFT calculation.
- schema:
  - `type`: text
  - `description`: Single number: total DOS at the Fermi energy in eV⁻¹ per formula unit (both spins).

### step_04_plasma_frequencies.csv
- path: `/app/outputs/step_04_plasma_frequencies.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Diagonal components (xx, yy, zz) of the Drude plasma frequency ℏΩ_p.
- schema:
  - `type`: table
  - `required_columns`: `direction`, `hbar_omega_p`
  - `units`:
    - `hbar_omega_p`: eV

### step_05_thermopower_300K.csv
- path: `/app/outputs/step_05_thermopower_300K.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Seebeck coefficient components at 300 K.
- schema:
  - `type`: table
  - `required_columns`: `direction`, `S_300K`
  - `units`:
    - `S_300K`: μV/K

### step_06_lambda.txt
- path: `/app/outputs/step_06_lambda.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: Superconducting coupling constant λ derived from N(E_F) and experimental γ.
- schema:
  - `type`: text
  - `description`: Single number: electron‑phonon coupling constant λ.

Notes: All output values must be computed using the specified DFT method (PBE scalar‑relativistic, with the given relaxed coordinates and experimental lattice constants) and the Boltzmann transport code. The experimental γ value used for λ is fixed at 11.64 mJ mol⁻¹ K⁻².

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_03_N(E_F).txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "description": "Single number: total DOS at the Fermi energy in eV⁻¹ per formula unit (both spins)."
      },
      "description": "Total electronic density of states at E_F, a key input for λ and a test of the DFT calculation."
    },
    {
      "file": "step_04_plasma_frequencies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "direction",
          "hbar_omega_p"
        ],
        "units": {
          "hbar_omega_p": "eV"
        }
      },
      "description": "Diagonal components (xx, yy, zz) of the Drude plasma frequency ℏΩ_p."
    },
    {
      "file": "step_05_thermopower_300K.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "direction",
          "S_300K"
        ],
        "units": {
          "S_300K": "μV/K"
        }
      },
      "description": "Seebeck coefficient components at 300 K."
    },
    {
      "file": "step_06_lambda.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "description": "Single number: electron‑phonon coupling constant λ."
      },
      "description": "Superconducting coupling constant λ derived from N(E_F) and experimental γ."
    }
  ],
  "notes": "All output values must be computed using the specified DFT method (PBE scalar‑relativistic, with the given relaxed coordinates and experimental lattice constants) and the Boltzmann transport code. The experimental γ value used for λ is fixed at 11.64 mJ mol⁻¹ K⁻²."
}
```

## How you are scored
A hidden verifier independently inspects each scored output file. It compares your reported values to the correct results expected from a faithful implementation of the described workflow, using tolerances that accommodate legitimate differences in computational parameters and software versions. The overall reward is proportional to the number of correctly reproduced values across all scored files. You must execute the full pipeline; simply writing the correct numbers from an external source will not suffice, as the verifier assesses all required artifacts.
