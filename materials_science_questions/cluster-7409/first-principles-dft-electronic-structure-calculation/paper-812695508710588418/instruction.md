# DFT electronic structure of TiO₂ (101) nanosheet

## Problem background
Anatase TiO₂ is a wide-bandgap semiconductor widely used in photocatalysis. Reducing its dimensionality to two-dimensional (2D) nanosheets can tune the electronic structure. This task explores the electronic properties of a TiO₂ sheet cleaved along the (101) plane, using first-principles density functional theory (DFT) to determine whether the 2D sheet remains semiconducting and to quantify the single-particle energy gap, compared to the bulk.

## Approach
A first-principles DFT approach is used. The slab model is built from bulk anatase TiO₂ by cleaving along the (101) plane, constructing a 2×1×1 supercell, and adding vacuum to form a 2D sheet. Geometry optimization is performed with the PBE functional, then a static calculation yields the projected density of states (PDOS), from which the bandgap is extracted as the energy separation between the valence-band maximum and conduction-band minimum.

## Reproduction target
Compute the projected density of states (PDOS) of the TiO₂-(101) 2D sheet using DFT with the PBE exchange-correlation functional. From the PDOS, determine the single-particle bandgap (in eV) as the energy difference between the highest occupied and lowest unoccupied states. The deliverables are the PDOS data file (pdos_TiO2_101.dat) and a one-line text file containing the bandgap value (bandgap_TiO2_101.txt).

## Assets

- Bulk anatase TiO₂ crystal structure (CIF): https://github.com/materialsproject/pymatgen/blob/master/test_files/TiO2_mp-390_computed.cif
- Open-source DFT code (e.g., Quantum ESPRESSO): https://www.quantum-espresso.org/
- Atomic Simulation Environment (ASE): ase

## Workflow steps

### Step 1: Construct TiO₂-(101) nanosheet model
- Role: process
- Action: Using the public bulk anatase TiO₂ crystal structure, cleave along the (101) plane, create a 2×1×1 supercell containing fourteen Ti and twenty-two O atoms, and add 20 Å of vacuum in the out-of-plane direction.
- Evidence: `/app/outputs/initial_slab_structure.xyz`

### Step 2: Geometry optimization
- Role: process
- Action: Perform DFT-based geometry relaxation of the TiO₂-(101) slab model using the PBE functional, a plane-wave cutoff of 550 eV, Monkhorst-Pack 3×3×1 k-point sampling, force convergence 0.001 eV/Å, and electronic convergence 10⁻⁷ eV.
- Evidence: `/app/outputs/optimized_structure.xyz`

### Step 3: Compute projected density of states (PDOS)
- Role: scored (load-bearing)
- Action: Perform a static DFT calculation on the optimized slab with a 16×16×1 Monkhorst-Pack k-point mesh and the same PBE functional and cutoff. Compute the total and projected density of states (Ti-3d and O-2p) and write the data to a formatted text file.
- Output file: `/app/outputs/pdos_TiO2_101.dat`
- Format: txt
- Contract: Columns: energy[eV], total_DOS[states/eV], Ti_3d_PDOS[states/eV], O_2p_PDOS[states/eV]. Header line optional. Values separated by whitespace.
- Scoring: scored by hidden verifier

### Step 4: Extract bandgap from PDOS
- Role: scored
- Action: Analyze the PDOS data to determine the bandgap as the energy separation between the valence-band maximum and conduction-band minimum. Write the bandgap value in eV to a text file.
- Output file: `/app/outputs/bandgap_TiO2_101.txt`
- Format: txt
- Contract: A single line containing the bandgap value in eV.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/pdos_TiO2_101.dat`
- `/app/outputs/bandgap_TiO2_101.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### pdos_TiO2_101.dat
- path: `/app/outputs/pdos_TiO2_101.dat`
- format: txt
- purpose: scored
- target_policy: structural_audit
- description: Projected density of states data for Ti-3d and O-2p orbitals. The file enables verification that a clear energy gap exists in the DOS around the Fermi level.
- schema:
  - `type`: table
  - `required_columns`: `energy[eV]`, `total_DOS[states/eV]`, `Ti_3d_PDOS[states/eV]`, `O_2p_PDOS[states/eV]`

### bandgap_TiO2_101.txt
- path: `/app/outputs/bandgap_TiO2_101.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: The PBE single-particle bandgap in eV, computed as the energy separation between the valence-band maximum and conduction-band minimum in the PDOS.
- schema:
  - `type`: text

Notes: Only the (101) electronic structure is scored. Optical properties, bulk bandgap, and (001) sheet are excluded per scope.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "pdos_TiO2_101.dat",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "energy[eV]",
          "total_DOS[states/eV]",
          "Ti_3d_PDOS[states/eV]",
          "O_2p_PDOS[states/eV]"
        ]
      },
      "description": "Projected density of states data for Ti-3d and O-2p orbitals. The file enables verification that a clear energy gap exists in the DOS around the Fermi level."
    },
    {
      "file": "bandgap_TiO2_101.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text"
      },
      "description": "The PBE single-particle bandgap in eV, computed as the energy separation between the valence-band maximum and conduction-band minimum in the PDOS."
    }
  ],
  "notes": "Only the (101) electronic structure is scored. Optical properties, bulk bandgap, and (001) sheet are excluded per scope."
}
```

## How you are scored
A hidden verifier inspects your pdos_TiO2_101.dat and bandgap_TiO2_101.txt. The PDOS file is checked for correct structure (four columns, sufficient resolution) and for a clear energy gap consistent with the bandgap you report. The bandgap value is compared to a hidden reference. The final reward is a weighted combination of these checks. Simply quoting a value without performing the DFT workflow will not pass, as the checker requires a self-consistent PDOS and bandgap derived from your calculations.
