# Electronic Structure and Thermopower of CuRhO2 from DFT and Boltzmann Transport

## Problem background
CuRhO2 is a delafossite semiconductor that exhibits promising thermoelectric properties. Understanding its electronic structure and thermoelectric transport is essential for optimizing its performance. Density functional theory (DFT) and Boltzmann transport calculations can be used to predict the optical band gap and the Seebeck coefficient under hole doping, providing insight into the material's suitability for thermoelectric applications.

## Approach
The approach is based on first-principles density functional theory (DFT) within the generalized gradient approximation (GGA-PBE) to compute the electronic structure of CuRhO2. The equilibrium internal oxygen parameter is first determined by total-energy minimization. A full self-consistent DFT calculation then yields the band structure, density of states, and dielectric function. The optical band gap is extracted from these results. The Seebeck coefficient is obtained within the constant relaxation time approximation of the Boltzmann transport equation, applied to a rigid-band model with hole doping levels of 0.1, 0.2, and 0.3 per formula unit, for temperatures ranging from 100 K to 1000 K. All computations are performed using open-source codes (Quantum ESPRESSO for the DFT part, BoltzTraP2 for the transport coefficients).

## Reproduction target
Produce two output files intended for independent verification:

- **bandgap.txt**: a single floating-point number representing the optical band gap of CuRhO2 in eV.
- **thermopower.csv**: a CSV file with columns `doping` (hole concentration per formula unit, one of 0.1, 0.2, 0.3), `T` (temperature in K), and `S_xx` (in-plane Seebeck coefficient in μV/K). Provide at least 10 temperature points evenly covering the range 100–1000 K for each doping level.

The computed band gap and thermopower curves must arise from the DFT electronic structure and the Boltzmann transport calculation described in the workflow steps.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- BoltzTraP2: https://www.boltzp2.org/

## Workflow steps

### Step 1: Optimize internal oxygen coordinate
- Role: process
- Action: Using DFT with GGA-PBE, perform total-energy minimization of the internal oxygen parameter z_O for CuRhO2 in the delafossite structure (space group R-3m) with experimental lattice parameters a=3.08 Å, c=17.09 Å. The Cu atom occupies (0,0,0), Rh at (0,0,1/2), O at (0,0,z) and symmetry-equivalent positions. Vary z to find the equilibrium value.
- Evidence: `/app/outputs/optimized_z_O.txt`

### Step 2: DFT electronic structure calculation
- Role: process
- Action: Perform a scalar-relativistic GGA-DFT calculation (e.g., using Quantum ESPRESSO) with the optimized structure from step 1 to obtain the self-consistent ground state. Then compute the band structure, density of states, and dielectric function on a dense k-point grid. Save the necessary files (wavefunction, eigenvalues, and optionally the complex dielectric function) for band gap extraction and thermopower calculation.
- Evidence: `/app/outputs/dft_calculation.txt`

### Step 3: Extract optical band gap
- Role: scored
- Action: Determine the optical band gap from the DFT results (e.g., from the onset of the imaginary part of the dielectric function or from the energy difference between the highest occupied and lowest unoccupied states in the density of states). Write the value in eV to bandgap.txt.
- Output file: `/app/outputs/bandgap.txt`
- Format: txt
- Contract: The optical band gap is a key property that controls electronic properties. The value should be reported as a single floating-point number.
- Scoring: scored by hidden verifier

### Step 4: Compute Seebeck coefficient
- Role: scored (load-bearing)
- Action: Using the DFT eigenvalues and group velocities from step 2, compute the in-plane Seebeck coefficient S_xx within the constant relaxation time approximation for hole doping levels of 0.1, 0.2, and 0.3 per formula unit, at temperatures from 100 K to 1000 K. Use the rigid-band model and a Boltzmann transport code (e.g., BoltzTraP2). Output the results to thermopower.csv.
- Output file: `/app/outputs/thermopower.csv`
- Format: csv
- Contract: CSV with columns: doping (hole concentration per formula unit, e.g., 0.1, 0.2, 0.3), T (temperature in K), S_xx (Seebeck coefficient in μV/K). At least 10 T points per doping.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/bandgap.txt`
- `/app/outputs/thermopower.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### bandgap.txt
- path: `/app/outputs/bandgap.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: Optical band gap of CuRhO2 as extracted from the DFT dielectric function or DOS.
- schema:
  - `type`: number
  - `units`: eV
  - `description`: A single floating-point number representing the optical band gap

### thermopower.csv
- path: `/app/outputs/thermopower.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: In-plane Seebeck coefficient S_xx versus temperature for three hole doping levels, computed from Boltzmann transport within the constant relaxation time approximation.
- schema:
  - `type`: table
  - `required_columns`: `doping`, `T`, `S_xx`
  - `units`:
    - `S_xx`: μV/K
    - `T`: K
    - `doping`: hole concentration per formula unit
  - `description`: Each row contains a Seebeck coefficient value for a specific doping level and temperature. Doping values must be one of 0.1, 0.2, 0.3. Temperature range: 100–1000 K.

Notes: The bandgap.txt and thermopower.csv serve as the sole scored artifacts. The thermopower curves must be derived from the DFT electronic structure; pre-computed or generic curves will fail structural checks (monotonicity, doping ordering) and magnitude comparisons.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "bandgap.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "number",
        "units": "eV",
        "description": "A single floating-point number representing the optical band gap"
      },
      "description": "Optical band gap of CuRhO2 as extracted from the DFT dielectric function or DOS."
    },
    {
      "file": "thermopower.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "doping",
          "T",
          "S_xx"
        ],
        "units": {
          "S_xx": "μV/K",
          "T": "K",
          "doping": "hole concentration per formula unit"
        },
        "description": "Each row contains a Seebeck coefficient value for a specific doping level and temperature. Doping values must be one of 0.1, 0.2, 0.3. Temperature range: 100–1000 K."
      },
      "description": "In-plane Seebeck coefficient S_xx versus temperature for three hole doping levels, computed from Boltzmann transport within the constant relaxation time approximation."
    }
  ],
  "notes": "The bandgap.txt and thermopower.csv serve as the sole scored artifacts. The thermopower curves must be derived from the DFT electronic structure; pre-computed or generic curves will fail structural checks (monotonicity, doping ordering) and magnitude comparisons."
}
```

## How you are scored
A hidden verifier independently inspects the artifacts you submit. The band gap value is compared against an expected range that is consistent with the physics of this material. The thermopower curves are checked for structural validity: required columns, temperatures within 100–1000 K, monotonic increase of S_xx with temperature for each doping level, and the correct ordering S_xx(0.1) > S_xx(0.2) > S_xx(0.3) at a given temperature. The magnitude of the Seebeck coefficients is also assessed for plausibility. The final reward is a weighted combination of these checks. Simply reporting pre‑existing values without performing the actual DFT and Boltzmann transport calculations will not yield a passing score.
