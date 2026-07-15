# Superatomic properties of TM@Li14 D6d cage clusters

## Problem background
Transition-metal-doped lithium clusters can form stable cage-like structures with interesting electronic and magnetic properties. Starting from a lithium Li15 cluster, replacing one lithium atom with a transition metal (TM) atom from groups 3–6 (Sc, Ti, V, Y, Zr, Nb, Hf, Ta, W) can lead to a D6d symmetric cage where the TM sits at the centre of a Li14 shell. Understanding the energetic stability, electronic structure, and magnetic moments of such TM@Li14 clusters is relevant for designing nanoscale building blocks. The objective of this task is to compute these properties from first principles and to verify whether the D6d cage is the global minimum structure for each TM.

## Approach
The workflow combines a global structure search with density functional theory (DFT) calculations. First, an unbiased search (e.g., particle swarm optimization) identifies low-energy candidate isomers for each TM@Li14 system. The search is coupled to DFT energy evaluations at a fast but reliable level. The lowest-energy isomers are then reoptimized at a spin-polarized DFT level using the PW91 exchange-correlation functional and the SDD basis set (or an equivalent open-source setup). Multiple spin multiplicities are tested to locate the electronic ground state. Harmonic vibrational frequency calculations confirm that the final structures are true local minima with no imaginary frequencies. Additional calculations provide the total energies of isolated Li and TM atoms, and for TM@Li13 fragments. From these total energies, three stability metrics are computed: the average binding energy per atom (Eb), the fragmentation energy (Ef), and the embedding energy (De). The total magnetic moment and HOMO-LUMO gap are extracted from the converged wavefunction. The entire procedure is repeated for the full set of nine TM elements, with a focus on the four representative cases Sc, Ti, V, and W, for which all computed properties and (for W) relative isomer energies are reported.

## Reproduction target
Produce two output files under /app/outputs:

1. properties.json – For TM = Sc, Ti, V, W, report the following quantities obtained from the PW91/SDD (or equivalent) DFT calculations:
   * magnetic_moment (in μB)
   * HOMO_LUMO_gap (in eV)
   * Eb, Ef, De (all in eV)
   * symmetry (point group string, expected to be D6d for the cage structure)
   For W, additionally include an array "isomer_energies" listing the eight lowest-energy isomers (labeled A, B, C, D, E, F, G, H) with their relative energies in eV, where isomer A is the D6d cage and its relative energy is set to 0.00 eV.

2. all_structures.xyz – A multi-frame XYZ file containing the optimized Cartesian coordinates of the D6d cage structure for all nine TM@Li14 clusters: Sc, Ti, V, Y, Zr, Nb, Hf, Ta, W. Each frame must contain exactly 15 atoms. The comment line on the second line of each frame must include the TM symbol, the string "D6d", and the total DFT energy in atomic units (e.g., "TM=W D6d E=-1234.567890").

## Assets

- CALYPSO structure prediction code: http://www.calypso.cn/
- Open-source DFT software supporting PW91 functional
- Python with standard scientific libraries: numpy, json, csv

## Workflow steps

### Step 1: Global structure search for TM@Li14 clusters
- Role: process
- Action: For TM = Sc, Ti, V, Y, Zr, Nb, Hf, Ta, W, perform an unbiased global structure search using particle swarm optimization (e.g., CALYPSO) coupled to DFT energy evaluations. Generate a diverse set of low-energy candidate isomers for each TM.
- Evidence: `/app/outputs/search_summary.json`

### Step 2: DFT re-optimization and frequency validation
- Role: process
- Action: Re-optimize all selected low-energy isomers at the spin-polarized DFT level using the PW91 functional and the SDD basis set (or an equivalent open-source setup). Test multiple spin multiplicities to find the electronic ground state. Perform harmonic vibrational frequency calculations on all optimized structures to confirm they are local minima (no imaginary frequencies). Additionally, compute total energies for isolated Li and TM atoms, and for TM@Li13 clusters for TM = Sc, Ti, V, W at the same level.
- Evidence: `/app/outputs/optimization_log.txt`

### Step 3: Compute and export properties for TM@Li14
- Role: scored (load-bearing)
- Action: From the DFT calculations, extract for TM = Sc, Ti, V, W the total magnetic moment (μB), HOMO-LUMO gap (eV), symmetry (point group), average binding energy per atom Eb (eV), fragmentation energy Ef (eV), and embedding energy De (eV) using the formulas from the paper. For W, also list the relative energies of the eight low-lying isomers (labeled A–H), setting isomer A (the D6d cage) as reference (0.00 eV). Write the results to properties.json.
- Output file: `/app/outputs/properties.json`
- Format: json
- Contract: JSON object with keys "Sc", "Ti", "V", "W". Each value is an object with: "magnetic_moment" (float, μB), "HOMO_LUMO_gap" (float, eV), "Eb" (float, eV), "Ef" (float, eV), "De" (float, eV), "symmetry" (string). The "W" object additionally contains "isomer_energies": an array of objects with "isomer_label" (string, one of A–H) and "relative_energy" (float, eV), where A has relative_energy 0.00.
- Scoring: scored by hidden verifier

### Step 4: Export optimized D6d cage structures for all nine TM
- Role: scored
- Action: For each of the nine transition metals (Sc, Ti, V, Y, Zr, Nb, Hf, Ta, W), export the optimized Cartesian coordinates of the D6d cage structure to all_structures.xyz. Each molecular frame must contain exactly 15 atoms and include a comment line with the TM symbol, the point group "D6d", and the total DFT energy in atomic units.
- Output file: `/app/outputs/all_structures.xyz`
- Format: txt
- Contract: Multi-frame XYZ text file. Each frame: first line = 15 (number of atoms), second line = comment string containing 'TM=<symbol> D6d E=<total_energy_a.u.>', followed by atomic coordinates (element x y z). The file must contain exactly one frame for each TM = Sc, Ti, V, Y, Zr, Nb, Hf, Ta, W.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/properties.json`
- `/app/outputs/all_structures.xyz`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### properties.json
- path: `/app/outputs/properties.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Computed magnetic moments, HOMO-LUMO gaps, stability energies, and relative isomer energies for TM = Sc, Ti, V, W. Checked against paper-reported values with tolerances.
- schema:
  - `type`: object
  - `required`:
    - `Sc`: magnetic_moment, HOMO_LUMO_gap, Eb, Ef, De, symmetry
    - `Ti`: magnetic_moment, HOMO_LUMO_gap, Eb, Ef, De, symmetry
    - `V`: magnetic_moment, HOMO_LUMO_gap, Eb, Ef, De, symmetry
    - `W`: magnetic_moment, HOMO_LUMO_gap, Eb, Ef, De, symmetry, isomer_energies
  - `items`: object
  - `required_columns`:
  - `units`:
    - `magnetic_moment`: μB
    - `HOMO_LUMO_gap`: eV
    - `Eb`: eV
    - `Ef`: eV
    - `De`: eV
    - `symmetry`: string
    - `relative_energy`: eV

### all_structures.xyz
- path: `/app/outputs/all_structures.xyz`
- format: txt
- purpose: scored
- target_policy: structural_audit
- description: Optimized Cartesian coordinates of the D6d cage structures for all nine TM@Li14 clusters. Structural audit checks for presence of each TM, D6d label, 15 atoms per frame, and plausible total energies.
- schema:
  - `type`: text
  - `required`: object
  - `items`: object
  - `required_columns`:
  - `units`: object

Notes: All scored quantities are computed by the agent from DFT and structure search results. The checker will compare reported values to hidden paper references using appropriate tolerances (result-level compare) and perform a structural audit on the XYZ file. No hidden gold values or tolerances are disclosed here.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "Sc": "magnetic_moment, HOMO_LUMO_gap, Eb, Ef, De, symmetry",
          "Ti": "magnetic_moment, HOMO_LUMO_gap, Eb, Ef, De, symmetry",
          "V": "magnetic_moment, HOMO_LUMO_gap, Eb, Ef, De, symmetry",
          "W": "magnetic_moment, HOMO_LUMO_gap, Eb, Ef, De, symmetry, isomer_energies"
        },
        "items": {},
        "required_columns": [],
        "units": {
          "magnetic_moment": "μB",
          "HOMO_LUMO_gap": "eV",
          "Eb": "eV",
          "Ef": "eV",
          "De": "eV",
          "symmetry": "string",
          "relative_energy": "eV"
        }
      },
      "description": "Computed magnetic moments, HOMO-LUMO gaps, stability energies, and relative isomer energies for TM = Sc, Ti, V, W. Checked against paper-reported values with tolerances."
    },
    {
      "file": "all_structures.xyz",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "text",
        "required": {},
        "items": {},
        "required_columns": [],
        "units": {}
      },
      "description": "Optimized Cartesian coordinates of the D6d cage structures for all nine TM@Li14 clusters. Structural audit checks for presence of each TM, D6d label, 15 atoms per frame, and plausible total energies."
    }
  ],
  "notes": "All scored quantities are computed by the agent from DFT and structure search results. The checker will compare reported values to hidden paper references using appropriate tolerances (result-level compare) and perform a structural audit on the XYZ file. No hidden gold values or tolerances are disclosed here."
}
```

## How you are scored
A hidden verifier will read your submitted properties.json and all_structures.xyz. It will compare the reported magnetic moments, gaps, stability energies, and isomer energies against reference values derived from the published study, using appropriate tolerances. For the XYZ file, it will check that the file contains exactly one frame for each of the nine metals, that each comment line includes the correct TM symbol and the "D6d" label, and that the reported total energies are plausible. The final score is a weighted combination of these checks. This means you must actually run the global structure search and DFT calculations as described; simply reporting numbers without executing the workflow will not produce a valid result. The verifier does not disclose the reference values or tolerances; your goal is to produce physically accurate quantities by faithfully carrying out the computational protocol.
