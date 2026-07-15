# Inversion‑symmetry breaking, boson peak and shear modulus in harmonic network models

## Problem background
Amorphous solids and defective crystals often exhibit an excess of low-frequency vibrational modes called the boson peak, which deviates from the Debye ω² law. The microscopic structural origin of this anomaly remains debated—it is unclear whether it is controlled by bond-orientational order or by local inversion-symmetry breaking. This task addresses this problem by numerically studying harmonic spring-network models of a random-network glass and a defective FCC crystal.

## Approach
Two model systems are constructed: a random network glass and a defective FCC crystal, both based on harmonic springs with a fixed spring constant and density. For each system, the average atomic coordination number Z is varied from 6 to 9 by randomly cutting bonds while keeping a narrow distribution of Z. The vibrational density of states D(ω) is obtained by diagonalizing the dynamical (Hessian) matrix; the boson peak frequency ω_BP is identified as the maximum of the reduced density of states D(ω)/ω². The shear modulus is decomposed into an affine part G_A (Born-Huang) and a nonaffine correction G_NA computed from the affine force field vectors and the inverse Hessian, giving the total G = G_A − G_NA. Two order parameters are computed for each configuration: the inversion-symmetry order parameter F_IS (derived from the affine force field) and the bond-orientational order parameter F_6 (Steinhardt-Nelson spherical-harmonic correlations with threshold 0.7). By evaluating these quantities as functions of Z for both systems and comparing the trends, one can infer which structural descriptor correlates with the boson peak and shear elasticity.

## Reproduction target
Produce the following averaged quantities for the random-network glass and the defective FCC crystal at Z = 6, 7, 8, 9 (at least three independent realizations per condition): (i) shear modulus components G, G_A, G_NA; (ii) inversion-symmetry order parameter F_IS; (iii) bond-orientational order parameter F_6; (iv) boson peak frequency ω_BP; (v) the full vibrational density of states D(ω) curves. The outputs must be written as specified CSV and JSON files. The results should allow examining the scaling with connectivity and the comparison between the glass and crystal, to evaluate the correlation between the order parameters and the boson peak.

## Assets

- numpy: numpy
- scipy: scipy

## Workflow steps

### Step 1: Generate random network glass configurations
- Role: process
- Action: Generate harmonic random‑network (RN) glass configurations with N=4000 atoms, density ρ=N/V=1.467, harmonic spring constant κ=1, reference bond length R₀=0.94, covering average coordination numbers Z=6,7,8,9. Start from a soft‑sphere packing relaxed by Monte Carlo using a truncated Lennard‑Jones potential, replace all interactions with harmonic springs between nearest neighbours, then randomly cut bonds to achieve each target Z while keeping a narrow Z distribution. Produce at least 3 independent realizations per Z.
- Evidence: `/app/outputs/rn_config_log.txt`

### Step 2: Generate defective FCC crystal configurations
- Role: process
- Action: Generate defective FCC crystal configurations at the same density ρ=1.467 and harmonic spring constant κ=1, with average coordination Z=6,7,8,9. Start from a perfect FCC lattice with a lattice constant matching the density, introduce harmonic springs between nearest neighbours, then randomly cut bonds to reach each target Z while maintaining a narrow Z distribution. Produce at least 3 independent realizations per Z.
- Evidence: `/app/outputs/fcc_config_log.txt`

### Step 3: Build Hessian and diagonalize to obtain normal modes
- Role: process
- Action: For every realization of each system (RN and FCC) and each Z, construct the dynamical (Hessian) matrix from the harmonic spring network, then diagonalize it (e.g., using scipy.linalg.eigh) to obtain the eigenfrequencies ω = √λ and eigenvectors. Store the sets of eigenfrequencies for each condition; they are needed for DOS, boson peak, and shear modulus calculations.
- Evidence: `/app/outputs/hessian_diag_log.txt`

### Step 4: Calculate shear modulus (affine and nonaffine)
- Role: scored (load-bearing)
- Action: For each configuration (system, Z, realization), compute the affine shear modulus G_A via the Born‑Huang formula and the nonaffine correction G_NA = Ξ_i^T (H^{-1})_{ij} Ξ_j using the affine force field vectors. The total shear modulus is G = G_A − G_NA. Average over realizations and output one row per (system, Z) pair.
- Output file: `/app/outputs/shear_modulus.csv`
- Format: csv
- Contract: Columns: system, Z, G, G_A, G_NA
- Scoring: scored by hidden verifier

### Step 5: Calculate order parameters F_IS and F_6
- Role: scored
- Action: For each configuration, compute the inversion‑symmetry order parameter F_IS from the affine force field components (using the mean‑field normalization denominator κ² R₀² N Z) and the bond‑orientational order parameter F_6 from Steinhardt‑Nelson spherical‑harmonic correlations with threshold S₆⁰=0.7. Average over realizations and output one row per (system, Z) pair.
- Output file: `/app/outputs/order_parameters.csv`
- Format: csv
- Contract: Columns: system, Z, F_IS, F_6
- Scoring: scored by hidden verifier

### Step 6: Boson peak frequency
- Role: scored
- Action: From the eigenfrequencies, compute the vibrational density of states D(ω) as a histogram and the reduced DOS D(ω)/ω². Identify the boson peak frequency ω_BP as the frequency of the maximum in D(ω)/ω² (excluding the zero‑frequency limit). Average over realizations and output one row per (system, Z) pair.
- Output file: `/app/outputs/boson_peak.csv`
- Format: csv
- Contract: Columns: system, Z, omega_BP
- Scoring: scored by hidden verifier

### Step 7: Density of states data (JSON)
- Role: scored
- Action: Save the averaged D(ω) for each condition to a JSON file. Use uniformly spaced frequency bins and the averaged histogram over realizations.
- Output file: `/app/outputs/dos_data.json`
- Format: json
- Contract: Top-level dictionary with condition keys; each condition maps to a dictionary with keys 'frequencies' (list of floats) and 'dos' (list of floats).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/shear_modulus.csv`
- `/app/outputs/order_parameters.csv`
- `/app/outputs/boson_peak.csv`
- `/app/outputs/dos_data.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### shear_modulus.csv
- path: `/app/outputs/shear_modulus.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Shear modulus (affine and nonaffine) for RN glass and defective FCC crystal at Z=6,7,8,9. Reference values are the paper's reported G, G_A, G_NA; scoring tolerates ±10%.
- schema:
  - `type`: table
  - `required_columns`: `system`, `Z`, `G`, `G_A`, `G_NA`
  - `units`:
    - `G`: harmonic units
    - `G_A`: harmonic units
    - `G_NA`: harmonic units

### order_parameters.csv
- path: `/app/outputs/order_parameters.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Inversion‑symmetry order parameter F_IS and bond‑orientational order parameter F_6. F_IS is compared to the paper's values with ±5% tolerance; F_6 trend (≈1 for FCC, ≈0.3 for RN, constant across Z) is also verified.
- schema:
  - `type`: table
  - `required_columns`: `system`, `Z`, `F_IS`, `F_6`
  - `units`: object

### boson_peak.csv
- path: `/app/outputs/boson_peak.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Boson peak frequency (maximum of D(ω)/ω²) for each condition. Compared to paper values with ±3% tolerance, and the trend (increases with Z) is checked.
- schema:
  - `type`: table
  - `required_columns`: `system`, `Z`, `omega_BP`
  - `units`:
    - `omega_BP`: frequency units

### dos_data.json
- path: `/app/outputs/dos_data.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Averaged vibrational density of states D(ω) curves. The checker verifies that the maximum of D(ω)/ω² coincides with the reported omega_BP and that the overall shape is physically plausible (Debye regime, boson peak).
- schema:
  - `type`: object
  - `required`: `RN_Z6`, `RN_Z7`, `RN_Z8`, `RN_Z9`, `FCC_Z6`, `FCC_Z7`, `FCC_Z8`, `FCC_Z9`
  - `items`:
    - `type`: object
    - `required`: `frequencies`, `dos`

Notes: All scored numbers are the agent's computed averages over at least 3 independent realizations per condition. The checker compares reported values to hidden gold with the stated tolerances and verifies the qualitative trends (F_IS linear in Z, omega_BP increasing with Z). The process steps (configuration generation, Hessian diagonalization) are not directly scored but are required to produce the load‑bearing shear modulus and other quantities.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "shear_modulus.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "system",
          "Z",
          "G",
          "G_A",
          "G_NA"
        ],
        "units": {
          "G": "harmonic units",
          "G_A": "harmonic units",
          "G_NA": "harmonic units"
        }
      },
      "description": "Shear modulus (affine and nonaffine) for RN glass and defective FCC crystal at Z=6,7,8,9. Reference values are the paper's reported G, G_A, G_NA; scoring tolerates ±10%."
    },
    {
      "file": "order_parameters.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "system",
          "Z",
          "F_IS",
          "F_6"
        ],
        "units": {}
      },
      "description": "Inversion‑symmetry order parameter F_IS and bond‑orientational order parameter F_6. F_IS is compared to the paper's values with ±5% tolerance; F_6 trend (≈1 for FCC, ≈0.3 for RN, constant across Z) is also verified."
    },
    {
      "file": "boson_peak.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "system",
          "Z",
          "omega_BP"
        ],
        "units": {
          "omega_BP": "frequency units"
        }
      },
      "description": "Boson peak frequency (maximum of D(ω)/ω²) for each condition. Compared to paper values with ±3% tolerance, and the trend (increases with Z) is checked."
    },
    {
      "file": "dos_data.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": [
          "RN_Z6",
          "RN_Z7",
          "RN_Z8",
          "RN_Z9",
          "FCC_Z6",
          "FCC_Z7",
          "FCC_Z8",
          "FCC_Z9"
        ],
        "items": {
          "type": "object",
          "required": [
            "frequencies",
            "dos"
          ]
        }
      },
      "description": "Averaged vibrational density of states D(ω) curves. The checker verifies that the maximum of D(ω)/ω² coincides with the reported omega_BP and that the overall shape is physically plausible (Debye regime, boson peak)."
    }
  ],
  "notes": "All scored numbers are the agent's computed averages over at least 3 independent realizations per condition. The checker compares reported values to hidden gold with the stated tolerances and verifies the qualitative trends (F_IS linear in Z, omega_BP increasing with Z). The process steps (configuration generation, Hessian diagonalization) are not directly scored but are required to produce the load‑bearing shear modulus and other quantities."
}
```

## How you are scored
A hidden verifier will compare your reported values (G, G_A, G_NA, F_IS, F_6, ω_BP) against reference values derived from a correct re-implementation of this protocol. It will also check that the DOS data is self-consistent (the reported ω_BP matches the peak in D(ω)/ω²) and that key monotonic trends across Z are satisfied. The final reward is a weighted sum: the shear modulus and order parameters carry the most weight, while the DOS data provides lower-weight structural validation. Simply reporting the paper's numbers without executing the computational pipeline will not produce a consistent set of artifacts and will not pass.
