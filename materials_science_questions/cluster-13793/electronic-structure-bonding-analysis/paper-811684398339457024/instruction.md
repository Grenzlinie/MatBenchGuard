# First-Principles Investigation of BiMn2O5 Multiferroicity: Electronic Structure, Born Charges, and Polarization

## Problem background
Multiferroic BiMn2O5 is a crystalline oxide that simultaneously exhibits antiferromagnetic ordering and ferroelectric polarization. Understanding the microscopic origin of this coexistence requires a detailed electronic-structure analysis. This task computes several key quantities from first principles: the relative stability of different magnetic configurations, the electronic band gap in the ground state, the magnetic moments on the inequivalent Mn sites, the Born effective charge tensors (which quantify the atomic contributions to polarization), and the magnitude of the spontaneous polarization. These quantities provide quantitative insight into the hybridization, charge transfer, and driving forces behind the material's multiferroicity.

## Approach
Density functional theory (DFT) calculations within the generalized-gradient approximation (GGA-PBE) are employed. Starting from the experimental crystal structure (lattice parameters a=7.56078 Å, b=8.53299 Å, c=5.76066 Å and atomic positions reported by Munoz et al.), a 2×1×1 supercell is built. After structural relaxation, total energies are computed for several collinear spin configurations—non-magnetic, ferromagnetic, ferrimagnetic, and two antiferromagnetic arrangements (AFM C‑1 and AFM C‑2)—to identify the ground state. For the lowest-energy configuration, the band structure and magnetic moments on the two Mn sites are extracted. Born effective charge tensors are obtained via density functional perturbation theory (or linear response), and the spontaneous polarization is evaluated with the Berry‑phase method. All calculations are performed with an open‑source plane‑wave pseudopotential code using publicly available norm-conserving pseudopotentials.

## Reproduction target
Your goal is to produce five scored artifacts by executing the described DFT workflow:

1. **Total energies of spin configurations** — a CSV file containing the total energy per formula unit (eV) for the NM, FM, ferrimagnetic, AFM C‑1, and AFM C‑2 configurations.
2. **AFM band gap** — a JSON file with the electronic band gap (eV) and gap type (direct or indirect) for the antiferromagnetic ground state.
3. **Magnetic moments** — a JSON file reporting the magnetic moments (μB) on the two inequivalent Mn sites (Mn1 and Mn2).
4. **Born effective charges** — a CSV file with the Born effective charge tensor components for each unique atom (Bi, Mn1, Mn2, O1, O2, O3, O4).
5. **Spontaneous polarization** — a JSON file with the magnitude of the macroscopic spontaneous polarization (μC/cm²) obtained from the Berry‑phase calculation.

You must perform the DFT calculations yourself using the provided crystal structure and publicly available pseudopotentials; simply copying values from a reference is not sufficient. Write your computed results in the exact formats specified in the workflow steps.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- GBRV pseudopotentials (or SSSP efficiency library): https://www.physics.rutgers.edu/gbrv/
- Experimental crystal structure of BiMn2O5: 10.1103/PhysRevB.65.144423

## Workflow steps

### Step 1: Structural relaxation
- Role: process
- Action: Perform geometry optimization of BiMn2O5 starting from the experimental crystal structure (lattice parameters a=7.56078 Å, b=8.53299 Å, c=5.76066 Å and atomic positions from Munoz et al. 2002) using DFT with GGA-PBE functional and a 2×1×1 supercell. Save the relaxed atomic coordinates.
- Evidence: `/app/outputs/step_01_relaxed_geometry.in`

### Step 2: Total energies of spin configurations
- Role: scored (load-bearing)
- Action: Using the relaxed geometry, compute collinear spin-polarized total energies for the non-magnetic (NM), ferromagnetic (FM), ferrimagnetic, and two antiferromagnetic configurations (AFM C-1 and AFM C-2). Report total energy per formula unit (eV) for each configuration.
- Output file: `/app/outputs/step_02_total_energies.csv`
- Format: csv
- Contract: Columns: spin_configuration, total_energy_per_fu (eV).
- Scoring: scored by hidden verifier

### Step 3: AFM band gap
- Role: scored
- Action: For the AFM ground state, compute the electronic band structure and determine the band gap (eV). Report the gap value and indicate whether it is direct or indirect.
- Output file: `/app/outputs/step_03_band_gap.json`
- Format: json
- Contract: {"band_gap_GGA": float (eV), "gap_type": "indirect" or "direct"}
- Scoring: scored by hidden verifier

### Step 4: Magnetic moments
- Role: scored
- Action: From the spin-polarized AFM calculation, extract the magnetic moments (μB) on the Mn1 and Mn2 sites.
- Output file: `/app/outputs/step_04_magnetic_moments.json`
- Format: json
- Contract: {"Mn1_moment": float (μB), "Mn2_moment": float (μB), "method": "GGA"}
- Scoring: scored by hidden verifier

### Step 5: Born effective charges
- Role: scored
- Action: Using density functional perturbation theory (or linear response), compute the Born effective charge tensor (Z*) for each unique atom (Bi, Mn1, Mn2, O1, O2, O3, O4). Report all non-zero tensor components.
- Output file: `/app/outputs/step_05_born_effective_charge.csv`
- Format: csv
- Contract: Columns: atom, Zxx, Zyy, Zzz, Zxy, Zxz, Zyz, Zyx, Zzx, Zzy. One row per unique atom.
- Scoring: scored by hidden verifier

### Step 6: Spontaneous polarization
- Role: scored
- Action: Compute the macroscopic spontaneous polarization using the Berry‑phase method and report the magnitude (μC/cm²).
- Output file: `/app/outputs/step_06_polarization.json`
- Format: json
- Contract: {"spontaneous_polarization_P": float (μC/cm²)}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_02_total_energies.csv`
- `/app/outputs/step_03_band_gap.json`
- `/app/outputs/step_04_magnetic_moments.json`
- `/app/outputs/step_05_born_effective_charge.csv`
- `/app/outputs/step_06_polarization.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_02_total_energies.csv
- path: `/app/outputs/step_02_total_energies.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Total energy per formula unit for each spin configuration (NM, FM, ferri, AFM-C1, AFM-C2). Ground state identified by lowest energy.
- schema:
  - `type`: table
  - `required_columns`: `spin_configuration`, `total_energy_per_fu`

### step_03_band_gap.json
- path: `/app/outputs/step_03_band_gap.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Band gap of the AFM ground state and gap type.
- schema:
  - `type`: object
  - `required`:
    - `band_gap_GGA`: float (eV)
    - `gap_type`: string

### step_04_magnetic_moments.json
- path: `/app/outputs/step_04_magnetic_moments.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Computed magnetic moments on Mn1 and Mn2 sites.
- schema:
  - `type`: object
  - `required`:
    - `Mn1_moment`: float (μB)
    - `Mn2_moment`: float (μB)
    - `method`: string

### step_05_born_effective_charge.csv
- path: `/app/outputs/step_05_born_effective_charge.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Born effective charge tensors for each unique atom.
- schema:
  - `type`: table
  - `required_columns`: `atom`, `Zxx`, `Zyy`, `Zzz`, `Zxy`, `Zxz`, `Zyz`, `Zyx`, `Zzx`, `Zzy`

### step_06_polarization.json
- path: `/app/outputs/step_06_polarization.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Macroscopic spontaneous polarization magnitude.
- schema:
  - `type`: object
  - `required`:
    - `spontaneous_polarization_P`: float (μC/cm²)

Notes: All DFT calculations are performed with the GGA-PBE functional using a plane-wave pseudopotential method. The scoring checks each computed quantity against the paper’s reference values with appropriate tolerances reflecting code‑specific variability.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_02_total_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "spin_configuration",
          "total_energy_per_fu"
        ]
      },
      "description": "Total energy per formula unit for each spin configuration (NM, FM, ferri, AFM-C1, AFM-C2). Ground state identified by lowest energy."
    },
    {
      "file": "step_03_band_gap.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "band_gap_GGA": "float (eV)",
          "gap_type": "string"
        }
      },
      "description": "Band gap of the AFM ground state and gap type."
    },
    {
      "file": "step_04_magnetic_moments.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "Mn1_moment": "float (μB)",
          "Mn2_moment": "float (μB)",
          "method": "string"
        }
      },
      "description": "Computed magnetic moments on Mn1 and Mn2 sites."
    },
    {
      "file": "step_05_born_effective_charge.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "atom",
          "Zxx",
          "Zyy",
          "Zzz",
          "Zxy",
          "Zxz",
          "Zyz",
          "Zyx",
          "Zzx",
          "Zzy"
        ]
      },
      "description": "Born effective charge tensors for each unique atom."
    },
    {
      "file": "step_06_polarization.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "spontaneous_polarization_P": "float (μC/cm²)"
        }
      },
      "description": "Macroscopic spontaneous polarization magnitude."
    }
  ],
  "notes": "All DFT calculations are performed with the GGA-PBE functional using a plane-wave pseudopotential method. The scoring checks each computed quantity against the paper’s reference values with appropriate tolerances reflecting code‑specific variability."
}
```

## How you are scored
A hidden verifier will inspect each output file after the workflow completes. Every scored artifact contributes a portion of the total reward. The verifier compares your computed numbers to reference physical values with tolerances that accommodate the expected spread between different DFT implementations. For total energies, relative ordering among configurations may be checked. For the band gap, magnetic moments, and polarization, numeric values are compared. For Born effective charge tensors, individual components are examined. The final score is a weighted combination of these per‑artifact checks. You are not required to hit exact numbers; agreement within reasonable tolerance will earn full or partial credit. The verifier also validates that each output file follows the declared format and includes all required fields.
