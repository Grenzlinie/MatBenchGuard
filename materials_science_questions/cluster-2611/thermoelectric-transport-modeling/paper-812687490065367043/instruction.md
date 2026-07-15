# Electronic structure and effective masses of CsBi4Te6 from first-principles DFT

## Problem background
CsBi4Te6 is a recently discovered narrow-gap semiconductor that exhibits excellent thermoelectric performance at low temperatures, surpassing conventional Bi2Te3-based alloys around 225 K. Understanding the origin of this enhanced performance requires detailed knowledge of its electronic structure, particularly the size of the band gap and the anisotropy of the hole effective masses. First-principles density functional theory (DFT) calculations can provide this insight by revealing how spin-orbit coupling affects the band gap and how the crystal structure—especially the presence of Bi-Bi bonds—leads to quasi-two-dimensional hole transport with highly directional effective masses.

## Approach
The computational approach uses density functional theory within the generalized gradient approximation (GGA-PBE). The crystal structure is taken from a public database and transformed into a triclinic cell containing 44 atoms to reduce computational cost. Two sets of self-consistent DFT calculations are performed with an open-source plane-wave/pseudopotential code: one scalar-relativistic (no spin-orbit coupling) and one fully relativistic (with spin-orbit coupling). From the resulting band structures, the direct band gap at the Γ point is extracted for both cases. Using the spin-orbit band structure near the valence band maximum, the effective mass tensor is computed and diagonalized to obtain the three principal effective masses and their orientations relative to the needle axis, the Bi-Bi bond direction, and the Cs-layer direction. All computational parameters (k-point sampling, plane-wave cutoff, pseudopotential choice) are chosen by the solver to achieve converged results consistent with standard DFT practice.

## Reproduction target
Produce two scored output files: (1) a JSON file reporting the computed direct band gap (in eV) without spin-orbit coupling and with spin-orbit coupling, and (2) a CSV file containing the three principal effective masses (in units of electron mass) of the valence band maximum, along with their directions (X ≈ needle axis, Y ≈ Bi-Bi bond direction, Z ≈ Cs-layer direction) and the angles between the principal axes and those reference directions. These quantities must be derived from your DFT calculations and written to the specified paths under `/app/outputs`.

## Assets

- CsBi4Te6 crystal structure (CIF)
- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP pseudopotentials (Cs, Bi, Te): https://www.materialscloud.org/discover/sssp/

## Workflow steps

### Step 1: Prepare triclinic input cell
- Role: process
- Action: Obtain the monoclinic crystal structure of CsBi4Te6 from a public database and transform it into the reduced triclinic cell (44 atoms) using the unit vectors A' = (A-B)/2, B' = (A+B)/2, C' = C. Generate Quantum ESPRESSO input files.
- Evidence: `/app/outputs/triclinic_scf.in`

### Step 2: DFT scalar-relativistic without SOC
- Role: process
- Action: Perform a self-consistent DFT calculation using Quantum ESPRESSO with GGA-PBE, scalar-relativistic pseudopotentials, and adequate k-point sampling. Run to convergence.
- Evidence: `/app/outputs/scf_no_soc.out`

### Step 3: DFT with spin-orbit coupling
- Role: process
- Action: Perform a self-consistent DFT calculation using Quantum ESPRESSO with fully relativistic (spin-orbit) pseudopotentials for Cs, Bi, Te, using the same triclinic cell. Include spin-orbit coupling in the Hamiltonian.
- Evidence: `/app/outputs/scf_soc.out`

### Step 4: Extract band gaps
- Role: scored
- Action: From the SCF outputs of steps 2 and 3, compute the fundamental band gap (smallest energy difference between valence band maximum and conduction band minimum). Write the values into a JSON file.
- Output file: `/app/outputs/band_gap.json`
- Format: json
- Contract: JSON object: { "band_gap_without_soc": float, "band_gap_with_soc": float }
- Scoring: scored by hidden verifier

### Step 5: Effective mass computation
- Role: scored (load-bearing)
- Action: Using the SOC band structure near the valence band maximum, compute the effective mass tensor, diagonalize it, and extract the three principal effective masses (in units of electron mass) and the angles to the reference axes (X needle, Y Bi-Bi bonds, Z Cs layers). Write a CSV file.
- Output file: `/app/outputs/effective_masses.csv`
- Format: csv
- Contract: CSV with columns: direction (string: X (needle), Y (Bi-Bi bonds), Z (Cs layers)), effective_mass (float, in m_e), angle (float, degrees). Three rows.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/band_gap.json`
- `/app/outputs/effective_masses.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### band_gap.json
- path: `/app/outputs/band_gap.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Band gaps without and with spin-orbit coupling.
- schema:
  - `type`: object
  - `required`:
    - `band_gap_without_soc`: float
    - `band_gap_with_soc`: float

### effective_masses.csv
- path: `/app/outputs/effective_masses.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Principal effective masses of the valence band maximum.
- schema:
  - `type`: table
  - `required_columns`: `direction`, `effective_mass`, `angle`
  - `units`:
    - `effective_mass`: m_e
    - `angle`: degrees

Notes: The checker compares the agent's computed values to hidden reference values with appropriate tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "band_gap.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "band_gap_without_soc": "float",
          "band_gap_with_soc": "float"
        }
      },
      "description": "Band gaps without and with spin-orbit coupling."
    },
    {
      "file": "effective_masses.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "direction",
          "effective_mass",
          "angle"
        ],
        "units": {
          "effective_mass": "m_e",
          "angle": "degrees"
        }
      },
      "description": "Principal effective masses of the valence band maximum."
    }
  ],
  "notes": "The checker compares the agent's computed values to hidden reference values with appropriate tolerances."
}
```

## How you are scored
A hidden verifier reads your submitted `band_gap.json` and `effective_masses.csv` and compares the values against reference results obtained from the original study. Each scored artifact contributes a share of the total reward; the effective masses carry a higher weight because they serve as the load-bearing check. The verifier uses tolerances that account for legitimate differences between DFT codes. Simply reporting numbers that match the paper without executing the workflow is detectable and will not yield a full reward.
