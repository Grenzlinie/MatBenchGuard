# DFT Study of Vacancy-Induced Magnetism in g-C3N4

## Problem background
Two-dimensional graphitic carbon nitride (g-C3N4) is a layered semiconductor with potential applications in optoelectronics, catalysis, and energy conversion. Pristine g-C3N4 is non-magnetic, but recent experimental observations suggest that ultrathin nanosheets of this material can exhibit weak ferromagnetism at room temperature. The origin of this magnetism is hypothesized to be carbon vacancies in the atomic lattice. This task investigates whether a single carbon vacancy, when introduced into a monolayer g-C3N4 supercell, can lead to spin-polarized electronic states and a net magnetic moment. You will use density functional theory (DFT) to compute the magnetic moment and spin-resolved band structure of the defective system, thereby testing the proposed vacancy-induced magnetism model.

## Approach
Use spin-polarized DFT within the generalized gradient approximation (GGA) of Perdew-Burke-Ernzerhof (PBE). The system is a 2×2 supercell of monolayer g-C3N4 in its hexagonal phase, with a single carbon atom removed. The vacancy is of the type that has been identified as potentially magnetic: the carbon atom that is the next-nearest neighbour to the central nitrogen atom. A vacuum layer of at least 15 Å is added perpendicular to the sheet to isolate it from its periodic images. After constructing this geometry, relax the atomic positions while keeping the cell dimensions fixed. Then perform a self-consistent field calculation to obtain the total magnetization, which is extracted as the net magnetic moment per supercell. Finally, compute the spin-resolved electronic band structure along a high-symmetry path (e.g., Γ–M–K–Γ) and refer the energies to the Fermi level. The open-source plane-wave DFT code Quantum ESPRESSO (pw.x and bands.x) is used throughout, with standard PBE pseudopotentials for carbon and nitrogen.

## Reproduction target
You must produce two output files from your calculations:

1. **`magnetic_moment.txt`** – a plain text file containing a single floating-point number that gives the total magnetic moment of the 2×2 supercell in Bohr magnetons (μB). This value is extracted from the spin-polarized SCF output.

2. **`band_structure.csv`** – a CSV file (no header) with columns: `kpoint_index` (integer), `kx`, `ky`, `kz` (floats, fractional coordinates of the k-point), `energy_spin_up` (eV), and `energy_spin_down` (eV). Energies must be referenced to the Fermi level (0 eV). The data should represent the spin-resolved band structure along a standard high-symmetry path that captures the key features of the electronic dispersion.

These artifacts are computed for the specific vacancy geometry described in the workflow steps; no other supercell or defect configuration should be used.

## Assets

- Quantum ESPRESSO (open-source DFT code): https://www.quantum-espresso.org/
- g-C3N4 monolayer crystal structure (hexagonal P6m2)
- PBE pseudopotentials (C, N) from SSSP efficiency library: https://www.materialscloud.org/discover/sssp/table/efficiency

## Workflow steps

### Step 1: Build defective supercell
- Role: process
- Action: Construct a 2×2 supercell of monolayer g-C3N4 in its hexagonal phase. Remove the carbon atom that is the next-nearest neighbour to the central nitrogen atom. Set a vacuum gap of at least 15 Å along the out-of-plane direction. Generate the input geometry file for Quantum ESPRESSO.
- Evidence: `/app/outputs/initial.in`

### Step 2: Relax defective supercell
- Role: process
- Action: Perform a spin-polarized geometry relaxation of the defective supercell using Quantum ESPRESSO (pw.x) with the PBE functional. Use an appropriate k-point mesh for relaxation and converge forces to a typical threshold. Keep the cell dimensions fixed.
- Evidence: `/app/outputs/relax.out`

### Step 3: Run spin-polarized SCF and extract magnetic moment
- Role: scored (load-bearing)
- Action: Perform a spin-polarized self-consistent field (SCF) calculation on the relaxed structure using Quantum ESPRESSO (pw.x) with a finer k-point mesh. Use the same functional and pseudopotentials. Read the total magnetization from the QE output and write the net magnetic moment as a single float (in μB) to magnetic_moment.txt under /app/outputs.
- Output file: `/app/outputs/magnetic_moment.txt`
- Format: txt
- Contract: Single floating-point number in Bohr magnetons (μB).
- Scoring: scored by hidden verifier

### Step 4: Compute band structure and output CSV
- Role: scored (load-bearing)
- Action: Perform a non-self-consistent (NSCF) band structure calculation using Quantum ESPRESSO (pw.x) on the SCF charge density, then use bands.x to extract the spin-resolved band energies along a standard high-symmetry path (e.g., Γ–M–K–Γ). Write the data to band_structure.csv under /app/outputs with columns: kpoint_index (int), kx (float), ky (float), kz (float), energy_spin_up (eV), energy_spin_down (eV). Energies must be referenced to the Fermi level (E_F = 0 eV).
- Output file: `/app/outputs/band_structure.csv`
- Format: csv
- Contract: CSV with no header. Columns: kpoint_index (int), kx (float), ky (float), kz (float), energy_spin_up (eV), energy_spin_down (eV). Energies referenced to Fermi level (0 eV).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/magnetic_moment.txt`
- `/app/outputs/band_structure.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### magnetic_moment.txt
- path: `/app/outputs/magnetic_moment.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: Total magnetic moment extracted from the spin-polarized SCF calculation.
- schema:
  - `type`: text
  - `description`: Single floating-point number representing total magnetic moment of the 2×2 supercell.
  - `units`: μB

### band_structure.csv
- path: `/app/outputs/band_structure.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Spin-resolved band structure along a high-symmetry path. The checker performs a structural audit (details not disclosed).
- schema:
  - `type`: table
  - `required_columns`: `kpoint_index`, `kx`, `ky`, `kz`, `energy_spin_up`, `energy_spin_down`
  - `column_types`:
    - `kpoint_index`: int
    - `kx`: float
    - `ky`: float
    - `kz`: float
    - `energy_spin_up`: float
    - `energy_spin_down`: float
  - `units`:
    - `energy_spin_up`: eV
    - `energy_spin_down`: eV

Notes: No gold values or tolerances are included in the public contract.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "magnetic_moment.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "description": "Single floating-point number representing total magnetic moment of the 2×2 supercell.",
        "units": "μB"
      },
      "description": "Total magnetic moment extracted from the spin-polarized SCF calculation."
    },
    {
      "file": "band_structure.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "kpoint_index",
          "kx",
          "ky",
          "kz",
          "energy_spin_up",
          "energy_spin_down"
        ],
        "column_types": {
          "kpoint_index": "int",
          "kx": "float",
          "ky": "float",
          "kz": "float",
          "energy_spin_up": "float",
          "energy_spin_down": "float"
        },
        "units": {
          "energy_spin_up": "eV",
          "energy_spin_down": "eV"
        }
      },
      "description": "Spin-resolved band structure along a high-symmetry path. The checker performs a structural audit (details not disclosed)."
    }
  ],
  "notes": "No gold values or tolerances are included in the public contract."
}
```

## How you are scored
A hidden verifier will independently evaluate your submitted artifacts. The verifier does not know your code or intermediate files; it only reads the final output files inside `/app/outputs`.

- **Magnetic moment** (`magnetic_moment.txt`): the verifier compares your reported value to a hidden reference magnetic moment obtained from a trusted DFT study of the same defective system. Full credit is awarded if your value falls within an absolute tolerance of the reference; the tolerance accounts for differences arising from implementation details (e.g., pseudopotentials, k-mesh, convergence criteria). The exact tolerance is not disclosed.
- **Band structure** (`band_structure.csv`): the verifier parses the CSV and performs a structural audit to ensure the band structure is physically consistent with the expected electronic behavior of a vacancy-containing g-C3N4 monolayer. The exact audit criteria are not disclosed. If the audit is satisfied, full credit for the band structure is awarded.

The final reward is a weighted combination of the scores from the two outputs, with the magnetic moment carrying the larger weight. Reporting the paper’s numbers without actually performing the DFT workflow will not suffice; the verifier performs a structural audit of the band structure and requires a physically meaningful magnetic moment consistent with the specific vacancy geometry you constructed.
