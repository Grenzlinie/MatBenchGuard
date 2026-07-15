# DFT Stability and Electronic Structure of IrPTe

## Problem background
IrPTe is a candidate small-gap semiconductor with a paracostibite structure containing heteroatomic P–Te dumbbells. First-principles DFT calculations are used to predict its thermodynamic stability relative to the elements and its electronic properties, including whether it exhibits a direct band gap suitable for semiconductor applications. Reproducing the computed formation energy and band gap verifies the computational prediction that supports this material's discovery.

## Approach
The reproduction uses plane-wave DFT with the GGA/PBE functional. Initial crystal structures are obtained from public crystallographic databases: the orthorhombic IrPTe phase (paracostibite type, Pbca) and a cubic polymorph (ullmannite type, P2₁3) are modelled starting from known structure types. Elemental reference phases (Ir, black P, Te) and binary reference phases (IrP₂, IrTe₂) are also considered. Full geometry optimizations are performed for all structures. From the relaxed total energies, the formation energy of o-IrPTe from the elements is calculated. A band-structure calculation on the optimized o-IrPTe geometry is then carried out to determine the direct band gap and its character (direct or indirect). The comparison with the cubic polymorph and reference binaries provides the context for stability predictions.

## Reproduction target
Compute and report the following for orthorhombic IrPTe (o-IrPTe, paracostibite type): (1) the formation energy from the elements (Ir, black P, Te) in kJ mol⁻¹, (2) the direct band gap in eV, and (3) whether the band gap is direct or indirect. Output these as a JSON file containing the fields formation_energy_kJ_per_mol, band_gap_direct_eV, and band_gap_type.

## Assets

- Quantum ESPRESSO (open-source DFT code): https://www.quantum-espresso.org/download
- SSSP pseudopotential library (PBE): https://www.materialscloud.org/discover/sssp/table/pseudopotentials
- Paracostibite (CoSbS) crystal structure CIF: COD 1011032
- Ullmannite (NiSbS) crystal structure CIF: COD 9000008
- Elemental and binary crystal structures (Ir, P, Te, IrP2, IrTe2)

## Workflow steps

### Step 1: Prepare crystal structures
- Role: process
- Action: Obtain initial crystal structures for o-IrPTe (paracostibite type, Pbca), c-IrPTe (ullmannite type, P2₁3), elemental Ir (fcc), black P (orthorhombic), Te (trigonal), and binaries IrP₂ (marcasite type) and IrTe₂ (CdI₂ type) from public crystallographic databases. Prepare DFT input files for structural relaxation.
- Evidence: `/app/outputs/structure_preparation.log`

### Step 2: DFT structural relaxations
- Role: process
- Action: Using an open-source plane‑wave DFT code (e.g., Quantum ESPRESSO) with GGA/PBE functional and SSSP pseudopotentials, perform full geometry optimization for all structures (o‑IrPTe, c‑IrPTe, Ir, P, Te, IrP₂, IrTe₂) on a dense k‑mesh. Extract relaxed geometries and total energies.
- Evidence: `/app/outputs/relaxation_summary.txt`

### Step 3: Formation energy and band gap
- Role: scored (load-bearing)
- Action: From the relaxed total energies of o‑IrPTe and the elements, calculate the formation energy of o‑IrPTe in kJ/mol (negative for exothermic). Perform a band‑structure calculation on the optimized o‑IrPTe geometry; determine the direct band gap (eV) and its type. Write the results to main_results.json.
- Output file: `/app/outputs/main_results.json`
- Format: json
- Contract: JSON object with keys: formation_energy_kJ_per_mol (float), band_gap_direct_eV (float), band_gap_type (string, 'direct' or 'indirect'), and optionally o_lattice_parameters (list of three floats).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/main_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### main_results.json
- path: `/app/outputs/main_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Scored artifact containing the DFT-calculated formation energy of o‑IrPTe from elements, its direct band gap, and the energy difference between orthorhombic and cubic IrPTe polymorphs.
- schema:
  - `type`: object
  - `required`:
    - `formation_energy_kJ_per_mol`: number (kJ/mol)
    - `band_gap_direct_eV`: number (eV)
    - `band_gap_type`: string (direct/indirect)
    - `delta_E_kJ_per_mol`: number (kJ/mol)
  - `optional`:
    - `o_lattice_parameters`: [a,b,c] in Angstrom
    - `transition_pressure_kbar`: number (kbar)
  - `units`:
    - `formation_energy_kJ_per_mol`: kJ/mol
    - `band_gap_direct_eV`: eV
    - `delta_E_kJ_per_mol`: kJ/mol
    - `o_lattice_parameters`: Angstrom
    - `transition_pressure_kbar`: kbar

Notes: Checker compares formation energy, band gap, and polymorph energy difference to paper's reported GGA values within expected tolerances and verifies band_gap_type is 'direct'.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "main_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "formation_energy_kJ_per_mol": "number (kJ/mol)",
          "band_gap_direct_eV": "number (eV)",
          "band_gap_type": "string (direct/indirect)",
          "delta_E_kJ_per_mol": "number (kJ/mol)"
        },
        "optional": {
          "o_lattice_parameters": "[a,b,c] in Angstrom",
          "transition_pressure_kbar": "number (kbar)"
        },
        "units": {
          "formation_energy_kJ_per_mol": "kJ/mol",
          "band_gap_direct_eV": "eV",
          "delta_E_kJ_per_mol": "kJ/mol",
          "o_lattice_parameters": "Angstrom",
          "transition_pressure_kbar": "kbar"
        }
      },
      "description": "Scored artifact containing the DFT-calculated formation energy of o‑IrPTe from elements, its direct band gap, and the energy difference between orthorhombic and cubic IrPTe polymorphs."
    }
  ],
  "notes": "Checker compares formation energy, band gap, and polymorph energy difference to paper's reported GGA values within expected tolerances and verifies band_gap_type is 'direct'."
}
```

## How you are scored
A hidden verifier independently examines the produced main_results.json. It compares the formation energy and band gap to reference values obtained from the original study, using appropriate tolerances that reflect typical variations between different DFT implementations. The verifier also checks that the band gap type is direct and that the formation energy is negative (indicating exothermic formation). Each of these checks contributes a weighted share to the final reward (total 1.0). The reward reflects how closely the computed quantities match the reference, not whether the agent reports any particular numbers; simply reporting the paper's values without genuine computation will not pass.
