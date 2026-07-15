## Problem background

Organic photovoltaic devices based on blends of polymers and fullerenes can be improved by functionalizing the fullerene, e.g., with PCBM. The crystal packing of PCBM strongly influences its electronic properties, such as the band gap and its direct/indirect nature, which in turn affect solar cell efficiency. Understanding how different crystal structures (sc, bcc, fcc) modify the cohesive and electronic properties is important for designing better materials.

## Approach

Using density-functional theory with the local-density approximation and plane-wave pseudopotentials, compute the electronic structure of the three cubic PCBM crystal phases (simple cubic, body-centered cubic, face-centered cubic). The procedure consists of:

- Relax an isolated PCBM molecule to obtain a reference geometry and total energy.
- For each cubic lattice, construct a primitive cell containing one relaxed PCBM molecule, perform a full variable-cell DFT relaxation to find the optimal lattice parameters and the cell total energy, from which the binding energy per molecule relative to the isolated molecule is obtained.
- For each relaxed crystal, perform self-consistent and non-self-consistent band structure calculations along the high-symmetry k-paths appropriate for each Bravais lattice. From the band dispersion identify the valence band maximum (VBM) and conduction band minimum (CBM) in k-space, determine the Kohn-Sham band gap (Ecbm - Evbm), and record whether the gap is direct or indirect.

## Reproduction target

Produce a single JSON file `electronic_properties.json` containing, for each of the three cubic phases (sc, bcc, fcc), the following quantities:
- Kohn-Sham band gap Eg (eV)
- Gap type ("direct" or "indirect")
- High-symmetry k-point label of the VBM and CBM
- Binding energy Eb (eV) = total energy per cell minus reference molecular energy (negative values for bound systems).

## Assets

The following public resources are required for the computation:

- **Quantum ESPRESSO** – open-source plane-wave DFT code; required.
  - Access: https://www.quantum-espresso.org/
- **LDA PAW pseudopotentials for C, H, O** – use standard LDA pseudopotentials from the Quantum ESPRESSO library or SSSP; required.
  - Access: https://www.quantum-espresso.org/pseudopotentials
- **Atomic Simulation Environment (ASE)** – structure building/manipulation library; optional but useful.
  - Access: https://gitlab.com/ase/ase

## Workflow steps

### Step 1: Relax isolated PCBM molecule
- Role: process
- Action: Construct the PCBM molecule (C72H14O2) from its chemical structure (C60 cage with a phenyl-butyric-acid-methyl-ester tail) and place it in a large supercell sufficient to isolate it. Perform a DFT geometry relaxation using LDA exchange-correlation and PAW pseudopotentials, using only the Γ-point for Brillouin-zone sampling. Record the final total energy and the relaxed geometry.
- Evidence: `/app/outputs/pcbm_isolated_energy.txt` (total energy) and `/app/outputs/pcbm_isolated.xyz` (optimized coordinates).

### Step 2: Relax cubic crystal structures
- Role: process
- Action: For each crystal type (sc, bcc, fcc), build a primitive cell containing one PCBM molecule using the relaxed molecular geometry. Start from approximate initial lattice constants (e.g., 9.9 Å for sc, 11.1 Å for bcc, 12.1 Å for fcc). Perform variable-cell DFT relaxations with LDA and Γ-point (or coarse k-point) sampling to obtain the optimized lattice parameters and the total energy per cell. Compute the binding energy Eb = E_cell - E_mol for each structure.
- Evidence: `/app/outputs/crystal_relaxation_results.json` (list of relaxed lattice parameters, cell volumes, total energies, and Eb per crystal).

### Step 3: Compute band structures
- Role: process
- Action: For each relaxed crystal structure, run a self-consistent DFT calculation with a denser k-point mesh (e.g., 4×4×4 Monkhorst-Pack grid) to obtain the charge density. Then perform non-self-consistent calculations along the conventional high-symmetry k-paths of each lattice: sc (Γ-X-M-Γ-R-X|M-Γ), bcc (Γ-H-N-P-Γ-H|P-N), fcc (Γ-X-W-K-Γ-L-U-W-L-K|U-X). From the band eigenvalues, locate the valence band maximum (VBM) and conduction band minimum (CBM) in energy and k-point space.
- Evidence: `/app/outputs/band_data.json` (raw band eigenvalues along the paths, and the identified VBM/CBM energies and k-points per crystal).

### Step 4: Compile electronic properties (load-bearing)
- Role: scored (load-bearing)
- Action: Combine the results from Steps 1–3. For each of sc, bcc, fcc, record the band gap Eg (eV), gap type ("direct" or "indirect"), high-symmetry label of the VBM and CBM k-points, and the binding energy Eb (eV). Write the values to `/app/outputs/electronic_properties.json`.
- Output file: `/app/outputs/electronic_properties.json`
- Format: json
- Contract: see Output contract.
- Scoring: scored by hidden verifier.

## Output files

- `/app/outputs/pcbm_isolated_energy.txt` (process evidence)
- `/app/outputs/pcbm_isolated.xyz` (process evidence)
- `/app/outputs/crystal_relaxation_results.json` (process evidence)
- `/app/outputs/band_data.json` (process evidence)
- `/app/outputs/electronic_properties.json` (scored artifact)

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### electronic_properties.json
- path: `/app/outputs/electronic_properties.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: JSON file with computed band gaps, gap types, band-edge k-point labels, and binding energies for the three cubic PCBM crystal phases.
- schema:
  - `type`: object
  - `required`:
    - `sc`:
      - `Eg`: eV
      - `gap_type`: string
      - `VBM_kpoint`: string
      - `CBM_kpoint`: string
      - `Eb`: eV
    - `bcc`:
      - `Eg`: eV
      - `gap_type`: string
      - `VBM_kpoint`: string
      - `CBM_kpoint`: string
      - `Eb`: eV
    - `fcc`:
      - `Eg`: eV
      - `gap_type`: string
      - `VBM_kpoint`: string
      - `CBM_kpoint`: string
      - `Eb`: eV
  - `units`:
    - `Eg`: eV
    - `Eb`: eV

Notes: The hidden verifier compares each quantity against reference values with appropriate tolerances. Gap type and k-point labels must match exactly. Band gaps and binding energies must be within tolerance of the hidden references.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "electronic_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "sc": {
            "Eg": "eV",
            "gap_type": "string",
            "VBM_kpoint": "string",
            "CBM_kpoint": "string",
            "Eb": "eV"
          },
          "bcc": {
            "Eg": "eV",
            "gap_type": "string",
            "VBM_kpoint": "string",
            "CBM_kpoint": "string",
            "Eb": "eV"
          },
          "fcc": {
            "Eg": "eV",
            "gap_type": "string",
            "VBM_kpoint": "string",
            "CBM_kpoint": "string",
            "Eb": "eV"
          }
        },
        "units": {
          "Eg": "eV",
          "Eb": "eV"
        }
      },
      "description": "JSON file with computed band gaps, gap types, band-edge k-point labels, and binding energies for the three cubic PCBM crystal phases."
    }
  ],
  "notes": "The hidden verifier compares each quantity against reference values with appropriate tolerances. Gap type and k-point labels must match exactly. Band gaps and binding energies must be within tolerance of the hidden references."
}
```

## How you are scored

A hidden verifier reads `electronic_properties.json`. For each of the three crystal phases it compares your reported band gap, gap type, VBM/CBM labels, and binding energy against reference values derived from the published literature. Each field contributes a fraction; the final reward is the average of the per-structure scores. Reporting a number alone is not enough; the verifier checks that the values are physically plausible and consistent with the declared quantities.
