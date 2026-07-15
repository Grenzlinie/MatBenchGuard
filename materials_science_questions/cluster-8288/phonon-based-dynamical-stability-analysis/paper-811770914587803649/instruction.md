# Dynamical stability and properties of zinc blende IrC

## Problem background
Transition-metal carbides are widely studied for hard-coating and cutting-tool applications because they can exhibit high hardness, high melting points, and good stability. Among them, iridium carbide (IrC) has been investigated theoretically in several crystal structures, but the existence of a stable, hard, cubic phase remains an open question. First-principles density functional theory calculations can predict the structural stability and mechanical/dynamical properties of candidate phases. In this task we focus on the zinc blende (ZB) form of IrC, a cubic structure that has been proposed as a potentially stable, conducting, hard material. The goal is to compute and characterize its ground-state properties, assessing whether it is mechanically and dynamically stable, metallic, and how hard it is, using standard DFT methods and open-source tools.

## Approach
The approach is a first-principles computational study using density functional theory (DFT) with the PBE generalized-gradient approximation. You will model the ZB-IrC unit cell, optimize its atomic positions and cell volume to find the ground-state total energy and relaxed lattice constant. From the relaxed structure you will compute the elastic stiffness tensor (C11, C12, C44) by applying small strains and extracting the stress or energy response; from these you will derive the bulk modulus B, shear modulus G, and the B/G ratio. Phonon dispersion will be calculated (e.g. via finite displacements) and the minimum frequency across the full Brillouin zone will be extracted to confirm no imaginary modes (indicating dynamical stability). The electronic density of states will be computed to check metallic character and to obtain the DOS at the Fermi level. Finally, a semi-empirical hardness model that uses bond length, electron density, overlap population, and a metallicity factor will be employed to estimate the Vickers hardness. All quantities refer to the ZB-IrC phase only.

## Reproduction target
Your task is to produce a single JSON file, `/app/outputs/zb_irc_properties.json`, containing the following computed quantities for zinc blende IrC: total energy (eV per formula unit), elastic constants C11, C12, C44 (GPa), bulk modulus B (GPa), shear modulus G (GPa), B/G ratio, Vickers hardness Hv (GPa), minimum phonon frequency (cm^{-1}), and the electronic density of states at the Fermi level (states/eV). You must set up the ZB-IrC crystal structure from its known atomic basis and lattice constant, carry out a full DFT geometry relaxation, and then run the required subsequent calculations. The JSON file must conform strictly to the output contract given below.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org
- Phonopy: https://phonopy.github.io/phonopy/
- SSSP Efficiency PBE pseudopotentials: https://www.materialscloud.org/discover/sssp

## Workflow steps

### Step 1: Setup ZB-IrC crystal structure
- Role: process
- Action: Create the zinc blende structure of IrC (space group F-43m) with a starting lattice constant of 4.663 Å, placing Ir at (0,0,0) and C at (1/4,1/4,1/4). Generate the required DFT input file.
- Evidence: `/app/outputs/zb_irc_input.in`

### Step 2: DFT geometry optimization and total energy
- Role: process
- Action: Perform a full DFT geometry relaxation (optimize atomic positions and cell parameters) for the ZB-IrC structure using the PBE exchange-correlation functional. Record the converged total energy per formula unit and the relaxed lattice parameter.
- Evidence: `/app/outputs/relaxed_structure.out`

### Step 3: Elastic constants calculation
- Role: process
- Action: Compute the elastic stiffness constants C11, C12, and C44 for the relaxed ZB-IrC using a suitable stress-strain or energy-strain method. Derive the bulk modulus B and shear modulus G via the Voigt-Reuss-Hill approximation, and compute the B/G ratio.
- Evidence: `/app/outputs/elastic_constants.dat`

### Step 4: Phonon dispersion calculation
- Role: process
- Action: Compute phonon frequencies on a uniform q-point mesh using the finite displacement or linear response method. Extract the minimum phonon frequency across the Brillouin zone (in cm^{-1}).
- Evidence: `/app/outputs/phonon_bands.dat`

### Step 5: Electronic density of states calculation
- Role: process
- Action: Compute the electronic density of states for the relaxed ZB-IrC structure. Extract the DOS value at the Fermi level (in states/eV).
- Evidence: `/app/outputs/dos_data.dat`

### Step 6: Semiempirical hardness estimation
- Role: process
- Action: Perform a Mulliken population analysis on the relaxed structure to obtain bond parameters (bond length d, electron density N_e, overlap population P, metallicity factor f_m). Use the semiempirical hardness model to estimate the Vickers hardness Hv of ZB-IrC.
- Evidence: `/app/outputs/hardness_inputs.dat`

### Step 7: Output ZB-IrC properties
- Role: scored (load-bearing)
- Action: Collect all computed quantities (total energy, C11, C12, C44, B, G, B/G, Hv, min phonon frequency, DOS at Fermi level) and write them as a JSON file.
- Output file: `/app/outputs/zb_irc_properties.json`
- Format: json
- Contract: {"total_energy": number (eV/f.u.), "C11": number (GPa), "C12": number (GPa), "C44": number (GPa), "bulk_modulus": number (GPa), "shear_modulus": number (GPa), "B_over_G": number, "hardness_Hv": number (GPa), "min_phonon_frequency": number (cm^{-1}), "DOS_at_Fermi": number (states/eV)}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/zb_irc_properties.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### zb_irc_properties.json
- path: `/app/outputs/zb_irc_properties.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: JSON file containing the computed key properties of ZB-IrC.
- schema:
  - `type`: object
  - `required`: `total_energy`, `C11`, `C12`, `C44`, `bulk_modulus`, `shear_modulus`, `B_over_G`, `hardness_Hv`, `min_phonon_frequency`, `DOS_at_Fermi`
  - `properties`:
    - `total_energy`:
      - `type`: number
      - `units`: eV/f.u.
    - `C11`:
      - `type`: number
      - `units`: GPa
    - `C12`:
      - `type`: number
      - `units`: GPa
    - `C44`:
      - `type`: number
      - `units`: GPa
    - `bulk_modulus`:
      - `type`: number
      - `units`: GPa
    - `shear_modulus`:
      - `type`: number
      - `units`: GPa
    - `B_over_G`:
      - `type`: number
    - `hardness_Hv`:
      - `type`: number
      - `units`: GPa
    - `min_phonon_frequency`:
      - `type`: number
      - `units`: cm^{-1}
    - `DOS_at_Fermi`:
      - `type`: number
      - `units`: states/eV
  - `additionalProperties`: False

Notes: The verifier will compare each numeric quantity to reference values derived from the paper's reported results, using tolerances appropriate for the computational method. It will also check that min_phonon_frequency > -1 cm^{-1} (no imaginary modes) and DOS_at_Fermi > 0 (metallic).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "zb_irc_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "total_energy",
          "C11",
          "C12",
          "C44",
          "bulk_modulus",
          "shear_modulus",
          "B_over_G",
          "hardness_Hv",
          "min_phonon_frequency",
          "DOS_at_Fermi"
        ],
        "properties": {
          "total_energy": {
            "type": "number",
            "units": "eV/f.u."
          },
          "C11": {
            "type": "number",
            "units": "GPa"
          },
          "C12": {
            "type": "number",
            "units": "GPa"
          },
          "C44": {
            "type": "number",
            "units": "GPa"
          },
          "bulk_modulus": {
            "type": "number",
            "units": "GPa"
          },
          "shear_modulus": {
            "type": "number",
            "units": "GPa"
          },
          "B_over_G": {
            "type": "number"
          },
          "hardness_Hv": {
            "type": "number",
            "units": "GPa"
          },
          "min_phonon_frequency": {
            "type": "number",
            "units": "cm^{-1}"
          },
          "DOS_at_Fermi": {
            "type": "number",
            "units": "states/eV"
          }
        },
        "additionalProperties": false
      },
      "description": "JSON file containing the computed key properties of ZB-IrC."
    }
  ],
  "notes": "The verifier will compare each numeric quantity to reference values derived from the paper's reported results, using tolerances appropriate for the computational method. It will also check that min_phonon_frequency > -1 cm^{-1} (no imaginary modes) and DOS_at_Fermi > 0 (metallic)."
}
```

## How you are scored
A hidden verifier reads your `zb_irc_properties.json` and checks each numeric field against reference values using tolerances that are realistic for DFT calculations performed with different codes and pseudopotentials. The verifier also confirms that the minimum phonon frequency is greater than -1 cm^{-1} (no imaginary modes) and that the DOS at the Fermi level is positive (metallic character). Additionally, the elastic constants are checked against the standard mechanical stability criteria for a cubic crystal. The final score is a weighted combination of these property checks; simply guessing or fabricating numbers will typically fail the physical consistency checks and the tolerance comparisons.
