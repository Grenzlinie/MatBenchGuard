# DFT study of spin-state energetics and absorption spectra of Ru, Fe, Co quaterpyridine complexes with CNS ligands

## Problem background
Dye-sensitized solar cells (DSSCs) use coordination complexes as photosensitizers to harvest light and inject electrons into a semiconductor. The efficiency of a sensitizer depends on its absorption spectrum, the energy of its frontier orbitals, and the strength of its attachment to the semiconductor surface. Ambidentate thiocyanate (CNS) ligands, which can bind to the metal center through either the nitrogen or the sulfur atom, are often used in such complexes, but the effect of the binding mode on the geometry, spin-state energetics, and electronic absorption properties is not fully understood. This task investigates a family of mononuclear quaterpyridine complexes of ruthenium, iron, and cobalt with two axial CNS ligands, asking: how does the linkage isomerism (N-bonded vs S-bonded) affect the relative stability, ground spin state, molecular structure, and UV-vis absorption profile of these compounds?

## Approach
The approach uses spin‑unrestricted density functional theory (DFT) and time‑dependent DFT (TD‑DFT) calculations with the open‑source quantum chemistry package ORCA. All calculations employ the B3LYP hybrid functional. The 6‑311G(d) basis set is used for non‑metal atoms (C, H, N, O, S), and the Lanl2DZ effective core potential (ECP) is applied to the metals (Ru, Fe, Co).

For each of the 15 complexes (different metal/oxidation‑state combinations and linkage isomers NCS/NCS, NCS/SCN, SCN/SCN), both high‑spin (HS) and low‑spin (LS) states are considered, with multiplicities appropriate for the d‑electron count (singlet/quintet for d⁶, doublet/quartet for d⁷, doublet/sextet for d⁵). After generating initial three‑dimensional structures from the molecular connectivity, full geometry optimizations and harmonic vibrational frequency calculations are carried out in the gas phase. Minima are confirmed by the absence of imaginary frequencies.

From these DFT results, we compute:
- Relative energies of the linkage isomers to determine the energetic preference for N‑ vs S‑bonding.
- Energy differences between HS and LS states (ΔE_HS‑LS) to assign the ground spin state.
- Selected harmonic vibrational stretching frequencies (C≡N, C=O, O–H) for key complexes.
- Metal–ligand bond lengths (basal M–N distances and axial M–E distances).

Finally, for each complex in its ground‑state spin multiplicity and ground‑state linkage isomer, TD‑DFT calculations are performed in acetonitrile (polarizable continuum model) at the same level of theory. Electronic transitions with significant oscillator strength are extracted, and the light‑harvesting efficiency (LHE) at the maximum absorption is computed.

## Reproduction target
Compute, for all 15 [M(dcqtpy)E₂] complexes (M = Ru(II), Fe(II/III), Co(II/III); E = NCS⁻ or SCN⁻, with linkage isomer combinations NCS/NCS, NCS/SCN, SCN/SCN), the following quantities using the B3LYP functional with the 6‑311G(d) basis set and Lanl2DZ ECP (ORCA package):
1. Relative total energies (kcal/mol) of the linkage isomers for each metal/oxidation state set, identifying the most stable isomer.
2. Spin‑state energy differences ΔE_HS‑LS (kcal/mol) for every complex.
3. Harmonic vibrational frequencies (cm⁻¹) for the C≡N, C=O, and O–H stretches of [Ru(dcqtpy)(NCS)₂] in the LS state, and for the C≡N stretch of [Fe(dcqtpy)(NCS)₂] in both HS and LS states.
4. Metal–ligand bond lengths (Å): average M–N distance to the four quaterpyridine nitrogen atoms, and M–E distances to the first and second axial CNS ligands, for all complexes in both spin states.
5. TD‑DFT electronic absorption spectra in acetonitrile: for each ground‑state isomer, wavelength (nm), oscillator strength, and dominant transition character for all transitions with f > 0.01, and the light‑harvesting efficiency (LHE) at the wavelength of maximum absorption.
Output each quantity as a CSV file with the columns specified in the workflow steps.

## Assets

- ORCA: https://orcaforum.kofo.mpg.de
- RDKit: rdkit-pypi
- OpenBabel: openbabel

## Workflow steps

### Step 1: Generate starting structures
- Role: process
- Action: Generate 3D conformers for all 15 [M(dcqtpy)E2] complexes (1-9, 4'-9') in both high-spin and low-spin multiplicities and in all required linkage isomer configurations (NCS/NCS, NCS/SCN, SCN/SCN) as defined in Scheme 1. Use RDKit from SMILES or manually constructed connectivity to build molecules and perform a crude geometry pre-optimization (e.g., PM3 semi-empirical or GFN2-xTB) to obtain reasonable starting Cartesian coordinates for DFT optimizations.
- Evidence: `/app/outputs/starting_geometries.xyz`

### Step 2: DFT geometry optimization and frequency calculations
- Role: process
- Action: For each complex, perform spin-unrestricted DFT geometry optimization and harmonic vibrational frequency calculation in the gas phase using the B3LYP functional with the 6-311G(d) basis set for non-metal atoms and the Lanl2DZ effective core potential for metals (Ru, Fe, Co). Use ORCA. The calculations must be carried out for both the high-spin (HS) and low-spin (LS) states (singlet/quintet for d6 Fe(II) and Ru(II), doublet/quartet for Co(II) d7, doublet/sextet for Fe(III) d5, singlet/quintet for Co(III) d6). Verify stationary points as minima (no imaginary frequencies).
- Evidence: `/app/outputs/optimization_outputs.tar.gz`

### Step 3: Compute relative isomer energies
- Role: scored (load-bearing)
- Action: For each set of linkage isomers sharing the same metal and oxidation state (Ru(II): 1,2,3; Fe(II): 4,5,6; Fe(III): 4',5',6'; Co(II): 7,8,9; Co(III): 7',8',9'), identify the ground-state isomer (the one with the lowest total electronic energy from step 2). Compute relative energies (kcal/mol) for the remaining isomers as the difference between their total energies and that of the ground-state isomer. Use only the B3LYP functional results. Output a table with columns: complex, functional, relative_energy_kcal_mol.
- Output file: `/app/outputs/relative_energies.csv`
- Format: csv
- Contract: complex (string), functional (string), relative_energy_kcal_mol (float)
- Scoring: scored by hidden verifier

### Step 4: Compute spin-state energy differences (ΔE_HS-LS)
- Role: scored
- Action: For every complex, calculate the energy difference ΔE_HS-LS = E(HS) - E(LS) (in kcal/mol) using the B3LYP total electronic energies from step 2. Apply zero-point vibrational energy correction if available. Report a single value per complex. Output a table with columns: complex, functional, deltae_hs_ls_kcal_mol.
- Output file: `/app/outputs/deltae_hs_ls.csv`
- Format: csv
- Contract: complex (string), functional (string), deltae_hs_ls_kcal_mol (float)
- Scoring: scored by hidden verifier

### Step 5: Extract harmonic vibrational frequencies
- Role: scored
- Action: From the frequency calculations of step 2, extract the harmonic vibrational frequencies (cm⁻¹) for the C≡N, C=O, and O–H stretching modes of [Ru(dcqtpy)(NCS)₂] (complex 1 in LS state) and for the C≡N mode of [Fe(dcqtpy)(NCS)₂] (complex 4 in both HS and LS states). Output a table with columns: complex, spin, functional, freq_C_N, freq_C_O, freq_O_H.
- Output file: `/app/outputs/harmonic_frequencies.csv`
- Format: csv
- Contract: complex (string), spin (string), functional (string), freq_C_N (float, cm-1), freq_C_O (float, cm-1), freq_O_H (float, cm-1)
- Scoring: scored by hidden verifier

### Step 6: Extract geometry bond lengths
- Role: scored
- Action: From the optimized geometries of all complexes (both HS and LS states of each neutral form), extract the following metal–ligand bond lengths (Å): average M–N distance to the four quaterpyridine nitrogen atoms, M–E1 distance to the first axial CNS ligand, and M–E2 distance to the second axial CNS ligand. Use B3LYP results. Output a table with columns: complex, spin, M_N_avg_basal, M_E1, M_E2.
- Output file: `/app/outputs/geometry_bond_lengths.csv`
- Format: csv
- Contract: complex (string), spin (string), M_N_avg_basal (float, Angstrom), M_E1 (float, Angstrom), M_E2 (float, Angstrom)
- Scoring: scored by hidden verifier

### Step 7: TD-DFT absorption spectra and light-harvesting efficiency
- Role: scored
- Action: For each complex in its ground-state spin multiplicity (as identified in step 4) and ground-state linkage isomer, perform a TD-DFT calculation in acetonitrile (PCM solvent model) using the B3LYP functional and the same basis set/ECP combination. Use the gas-phase optimized geometry from step 2. Request at least the 40 lowest excited states. From the output, extract all electronic transitions with oscillator strength f > 0.01: list wavelength (nm), oscillator strength, and the dominant transition character (e.g., MLCT, ILCT, LLCT). Additionally, compute the light-harvesting efficiency (LHE) at the wavelength of maximum absorption using LHE = 1 - 10^(-f) and report it together with the corresponding wavelength. Output a table with columns: complex, wavelength_nm, oscillator_strength, character, LHE_max.
- Output file: `/app/outputs/absorption_spectra.csv`
- Format: csv
- Contract: complex (string), wavelength_nm (float), oscillator_strength (float), character (string, optional), LHE_max (float, optional)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/relative_energies.csv`
- `/app/outputs/deltae_hs_ls.csv`
- `/app/outputs/harmonic_frequencies.csv`
- `/app/outputs/geometry_bond_lengths.csv`
- `/app/outputs/absorption_spectra.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### relative_energies.csv
- path: `/app/outputs/relative_energies.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Quantifies the thermodynamic preference for N-bonding vs S-bonding of the CNS ligand.
- schema:
  - `type`: table
  - `required_columns`: `complex`, `functional`, `relative_energy_kcal_mol`

### deltae_hs_ls.csv
- path: `/app/outputs/deltae_hs_ls.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Determines the ground spin state for each complex; positive ΔE_HS-LS indicates LS ground state, negative indicates HS ground state.
- schema:
  - `type`: table
  - `required_columns`: `complex`, `functional`, `deltae_hs_ls_kcal_mol`

### harmonic_frequencies.csv
- path: `/app/outputs/harmonic_frequencies.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Provides a vibrational benchmark for the quality of the DFT functional; these frequencies can be compared against experimental literature values.
- schema:
  - `type`: table
  - `required_columns`: `complex`, `spin`, `functional`, `freq_C_N`, `freq_C_O`, `freq_O_H`

### geometry_bond_lengths.csv
- path: `/app/outputs/geometry_bond_lengths.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Documents the structural differences between spin states and isomer configurations.
- schema:
  - `type`: table
  - `required_columns`: `complex`, `spin`, `M_N_avg_basal`, `M_E1`, `M_E2`

### absorption_spectra.csv
- path: `/app/outputs/absorption_spectra.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Simulates the UV-vis absorption profiles of the sensitizers and evaluates their light-harvesting capability.
- schema:
  - `type`: table
  - `required_columns`: `complex`, `wavelength_nm`, `oscillator_strength`, `LHE_max`
  - `optional_columns`: `character`

Notes: All scored outputs are compared against hidden paper-reported reference values with tolerances appropriate for re-running DFT/TD-DFT with a different code (ORCA vs Gaussian) and basis set implementation. The specific tolerances are hidden.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "relative_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "complex",
          "functional",
          "relative_energy_kcal_mol"
        ]
      },
      "description": "Quantifies the thermodynamic preference for N-bonding vs S-bonding of the CNS ligand."
    },
    {
      "file": "deltae_hs_ls.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "complex",
          "functional",
          "deltae_hs_ls_kcal_mol"
        ]
      },
      "description": "Determines the ground spin state for each complex; positive ΔE_HS-LS indicates LS ground state, negative indicates HS ground state."
    },
    {
      "file": "harmonic_frequencies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "complex",
          "spin",
          "functional",
          "freq_C_N",
          "freq_C_O",
          "freq_O_H"
        ]
      },
      "description": "Provides a vibrational benchmark for the quality of the DFT functional; these frequencies can be compared against experimental literature values."
    },
    {
      "file": "geometry_bond_lengths.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "complex",
          "spin",
          "M_N_avg_basal",
          "M_E1",
          "M_E2"
        ]
      },
      "description": "Documents the structural differences between spin states and isomer configurations."
    },
    {
      "file": "absorption_spectra.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "complex",
          "wavelength_nm",
          "oscillator_strength",
          "LHE_max"
        ],
        "optional_columns": [
          "character"
        ]
      },
      "description": "Simulates the UV-vis absorption profiles of the sensitizers and evaluates their light-harvesting capability."
    }
  ],
  "notes": "All scored outputs are compared against hidden paper-reported reference values with tolerances appropriate for re-running DFT/TD-DFT with a different code (ORCA vs Gaussian) and basis set implementation. The specific tolerances are hidden."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier that reads the CSV files you produce and compares selected entries to reference data derived from the original study. Because the recomputation uses a different quantum‑chemistry code (ORCA instead of Gaussian) and basis‑set implementation, numerical values may differ slightly; the verifier uses tolerances appropriate for this level of theory. The reward is a weighted sum of pass/fail tests across the five scored artifacts, with the largest weight assigned to the relative isomer energies and spin‑state assignments. Simply reporting a value without genuinely running the DFT/TD‑DFT workflow will not satisfy the verifier, because tolerances are set to accept only results obtainable from a correct execution of the prescribed computational procedure.
