# Fully relativistic LSDA+U electronic structure calculations for SmB6 and YbB12

## Problem background
Mixed-valence rare-earth hexaborides SmB6 and YbB12 are narrow-gap semiconductors whose electronic properties are dominated by correlated 4f electrons. Standard density functional calculations in the local spin-density approximation (LSDA) give an inadequate description of the 4f states and fail to open the correct hybridization gap. The LSDA+U method adds a static on-site Coulomb correction to the 4f orbitals, allowing a more realistic treatment of the occupied and unoccupied f bands. This task reproduces fully relativistic LSDA+U calculations with spin-orbit coupling for SmB6 and YbB12, aiming to determine the hybridization gap, the Sm valency, and the low-energy optical conductivity.

## Approach
The calculations are performed with a fully relativistic LSDA+U implementation that includes spin-orbit coupling. For SmB6, the initial configuration is divalent Sm²⁺ (4f⁶) and the effective Hubbard U is set to 7 eV; for YbB12, the initial configuration is divalent Yb²⁺ (4f¹⁴) and Ueff = 8 eV. Self‑consistent field iterations are run on dense k‑point meshes. After convergence, the hybridization gap ΔE is extracted as the energy separation between the top of the occupied hybridized band and the bottom of the unoccupied hybridized band at the Fermi level. The Sm valency is obtained from the 4f occupancy (2.0 + number of 4f holes). The real part of the diagonal optical conductivity σ₁xx(ω) is computed for the energy range 0–1 eV (SmB6) and 0–0.6 eV (YbB12) using the Kubo–Greenwood formula. All results are written into the two JSON files specified in the output contract.

## Reproduction target
Produce the two scored JSON artifacts described in the output contract. For SmB6, you must report the hybridization gap (meV), the mean Sm valency, and an array of optical conductivity data points covering 0 to 1 eV. For YbB12, you must report the hybridization gap (meV) and an array of optical conductivity data points covering 0 to 0.6 eV. The numbers must come from a fully relativistic LSDA+U calculation using the prescribed divalent starting configurations and Ueff values; they will be compared against hidden reference values by the automated verifier.

## Assets

- SmB6 crystal structure: https://materialsproject.org/materials/mp-1023/
- YbB12 crystal structure: https://materialsproject.org/materials/mp-10718/
- Elk FP-LAPW code (or equivalent open-source DFT code supporting LSDA+U with spin-orbit coupling): https://elk.sourceforge.io/
- Python 3 with NumPy: python3, numpy

## Workflow steps

### Step 1: Prepare crystal structures
- Role: process
- Action: Obtain the crystal structures of SmB6 (Cubic, Pm-3m, a=4.1333 Å) and YbB12 (Cubic, Fm-3m, a=7.464 Å) from public databases and generate input files for the chosen DFT code.
- Evidence: `/app/outputs/crystal_structures.log`

### Step 2: LSDA+U calculation for SmB6 (divalent start)
- Role: process
- Action: Perform a fully relativistic, spin-polarized LSDA+U calculation for SmB6 with U_eff = 7 eV, initial Sm²⁺ (4f⁶) configuration, a dense k‑point mesh, and spin‑orbit coupling included.
- Evidence: `/app/outputs/smb6_dft_output.tar.gz`

### Step 3: LSDA+U calculation for YbB12 (divalent start)
- Role: process
- Action: Perform a fully relativistic, spin-polarized LSDA+U calculation for YbB12 with U_eff = 8 eV, initial Yb²⁺ (4f¹⁴) configuration, a dense k‑point mesh, and spin‑orbit coupling included.
- Evidence: `/app/outputs/yb12_dft_output.tar.gz`

### Step 4: Extract SmB6 results
- Role: scored (load-bearing)
- Action: Post‑process the SmB6 LSDA+U output to compute: (1) hybridization gap ΔE (energy difference between top of occupied hybridized band and bottom of unoccupied hybridized band at EF); (2) mean Sm valency from 4f occupancy (2.0 + number of 4f holes); (3) optical conductivity σ₁ₓₓ(ω) in the 0–1 eV range using the Kubo–Greenwood formula and appropriate broadening. Write the results to smb6_results.json.
- Output file: `/app/outputs/smb6_results.json`
- Format: json
- Contract: {"gap_mev": <number>, "valency": <number>, "optical_conductivity": [{"energy_eV": <number>, "sigma_arb_units": <number>}, ...]}
- Scoring: scored by hidden verifier

### Step 5: Extract YbB12 results
- Role: scored (load-bearing)
- Action: Post‑process the YbB12 LSDA+U output to compute: (1) hybridization gap ΔE; (2) optical conductivity σ₁ₓₓ(ω) in the 0–0.6 eV range using the Kubo–Greenwood formula and appropriate broadening. Write the results to yb12_results.json.
- Output file: `/app/outputs/yb12_results.json`
- Format: json
- Contract: {"gap_mev": <number>, "optical_conductivity": [{"energy_eV": <number>, "sigma_arb_units": <number>}, ...]}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/smb6_results.json`
- `/app/outputs/yb12_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### smb6_results.json
- path: `/app/outputs/smb6_results.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Hybridization gap ΔE (meV), mean Sm valency, and optical conductivity σ₁ₓₓ(ω) for SmB6. The optical conductivity array covers 0–1 eV. The checker compares gap and valency to reference values with tolerance; optical conductivity is checked for expected peak positions.
- schema:
  - `type`: object
  - `required`:
    - `gap_mev`: number (meV)
    - `valency`: number (dimensionless)
    - `optical_conductivity`: array of objects
  - `items`:
    - `energy_eV`: number (eV)
    - `sigma_arb_units`: number (arb. units)

### yb12_results.json
- path: `/app/outputs/yb12_results.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Hybridization gap ΔE (meV) and optical conductivity σ₁ₓₓ(ω) for YbB12. The optical conductivity array covers 0–0.6 eV. The checker compares the gap to a reference value with tolerance and verifies optical peak positions.
- schema:
  - `type`: object
  - `required`:
    - `gap_mev`: number (meV)
    - `optical_conductivity`: array of objects
  - `items`:
    - `energy_eV`: number (eV)
    - `sigma_arb_units`: number (arb. units)

Notes: The optical conductivity arrays must contain enough points to resolve the low‑energy features. The checker uses result‑level comparison: gap and valency are compared to hidden paper values with tolerances; optical conductivity is checked by identifying peaks near expected energies. No gold values or tolerances are disclosed here.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "smb6_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": {
          "gap_mev": "number (meV)",
          "valency": "number (dimensionless)",
          "optical_conductivity": "array of objects"
        },
        "items": {
          "energy_eV": "number (eV)",
          "sigma_arb_units": "number (arb. units)"
        }
      },
      "description": "Hybridization gap ΔE (meV), mean Sm valency, and optical conductivity σ₁ₓₓ(ω) for SmB6. The optical conductivity array covers 0–1 eV. The checker compares gap and valency to reference values with tolerance; optical conductivity is checked for expected peak positions."
    },
    {
      "file": "yb12_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": {
          "gap_mev": "number (meV)",
          "optical_conductivity": "array of objects"
        },
        "items": {
          "energy_eV": "number (eV)",
          "sigma_arb_units": "number (arb. units)"
        }
      },
      "description": "Hybridization gap ΔE (meV) and optical conductivity σ₁ₓₓ(ω) for YbB12. The optical conductivity array covers 0–0.6 eV. The checker compares the gap to a reference value with tolerance and verifies optical peak positions."
    }
  ],
  "notes": "The optical conductivity arrays must contain enough points to resolve the low‑energy features. The checker uses result‑level comparison: gap and valency are compared to hidden paper values with tolerances; optical conductivity is checked by identifying peaks near expected energies. No gold values or tolerances are disclosed here."
}
```

## How you are scored
An automated verifier will read your JSON artifacts. The hybridization gap and (for SmB6) the mean valency are compared to hidden reference values with tolerances that accommodate the typical numerical spread between different implementations. The optical conductivity arrays are checked for the presence of characteristic peak features in the relevant energy windows. The final score is a weighted combination of these checks. Reporting plausible numbers without actually running the described LSDA+U calculations is unlikely to satisfy all tolerances simultaneously; you must execute the workflow to obtain a passing score.
