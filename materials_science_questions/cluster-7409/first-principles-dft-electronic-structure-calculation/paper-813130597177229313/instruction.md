# DFT Study of Hydrogen Anion Incorporation in Amorphous Oxide Semiconductors: Structural and Vibrational Analysis

## Problem background
Amorphous In–Ga–Zn–O (a-IGZO) is a leading semiconductor for thin-film transistor (TFT) backplanes in high-resolution displays. However, a-IGZO TFTs suffer from negative bias illumination stress (NBIS) instability: a negative threshold-voltage shift under simultaneous negative gate bias and light illumination, which corresponds to the normal operating state of displays. NBIS instability is observed under sub-bandgap illumination, strongly suggesting that occupied subgap electronic states near the valence band maximum are responsible. One proposed origin of these subgap states is hydrogen impurities, which are inevitably incorporated during sputter deposition. Hydrogen can exist as hydride ions (H−) bonded to metal cations when stabilized at oxygen vacancy sites. The challenge is to determine, from first-principles calculations, whether such hydride ions can form in a-IGZO, what their local coordination is, and how their M–H bonding orbitals contribute to subgap electronic states. This task therefore asks: what are the relaxed geometries of hydrogen incorporated at an oxygen vacancy in a-IGZO, and what metal–hydrogen vibrational frequencies and subgap-state energy do they produce?

## Approach
The core idea is to model hydrogen incorporation in a-IGZO using density functional theory (DFT) and to compare the computed vibrational and electronic properties with experimental observations reported for sputtered thin films. The approach is as follows:

1. **Structural model:** Generate an amorphous InGaZnO₄ supercell via a melt-quench ab initio molecular dynamics protocol. This provides a realistic starting structure that captures the disordered network of the amorphous oxide.

2. **Hydrogen incorporation and relaxation:** Create a neutral oxygen vacancy in the a-IGZO model. Insert an H₂ molecule at the vacancy site and perform full geometry optimization within the PBE+U framework, with on-site Hubbard U corrections applied to the d orbitals of In, Ga, and Zn. This forces the system to find the lowest-energy configuration of hydrogen atoms bound to metal centers. The relaxation is continued until residual forces are very small, yielding a final atomic geometry with two distinct hydride ions.

3. **Vibrational analysis:** Using the relaxed structure, compute the force-constant matrix and Born effective charges via density functional perturbation theory or finite differences, thereby obtaining infrared-active vibrational modes. Identify the metal–hydrogen stretching modes. Independently, compute the vibrational stretching frequencies of isolated gas-phase hydride molecules (InH, GaH, ZnH) at the same level of theory. The difference between the gas-phase frequencies and the modes in the amorphous matrix gives the red-shifts that indicate the influence of the solid-state environment.

4. **Electronic structure:** Compute the total and partial electronic density of states (DOS) for the hydrogen-incorporated model. From the DOS, extract the energy position of any occupied subgap states relative to the valence band maximum (VBM).

The entire workflow is executed with an open-source plane-wave DFT code and standard pseudopotentials, reproducing the computational protocol reported in the literature for this system.

## Reproduction target
Produce two scored artifacts that together evaluate the computational model of hydrogen incorporation in a-IGZO:

- **Atomic geometry (step01_relaxed_geometry.xyz):** A relaxed XYZ file containing a hydrogen-incorporated a-IGZO supercell. The geometry must contain exactly two hydrogen atoms, with one (labeled Ht) coordinated to three metal atoms (In, Ga, Zn) and the other (labeled Hd) coordinated to two metal atoms (Ga, Zn), as defined by a nearest-neighbor cutoff of 2.5 Å. The file must explicitly identify which hydrogen is Ht and which is Hd (e.g., in the comment line).

- **Vibrational and electronic properties (step02_vibrational_and_dos.json):** A JSON object reporting: (a) the two metal–hydrogen stretching frequencies (cm⁻¹) and their mode characters (e.g., "In–H stretch", "Zn–H stretch"); (b) the computed gas-phase hydride stretching frequencies for InH, GaH, and ZnH at the same theoretical level; (c) the red-shift of each M–H mode in the solid relative to its gas-phase counterpart (cm⁻¹); (d) the energy of the occupied subgap state above the VBM (eV) derived from the density of states. The agent chooses which two M–H modes to report, based on the dominant mode character.

The target is to obtain results that are consistent with the experimentally determined M–H vibrational frequencies and subgap absorption threshold, as reported for self-standing a-IGZO thin films. The agent must execute the full ab initio pipeline; pre-existing coordinates or pre-computed properties may not be used.

## Assets

- Quantum ESPRESSO (or equivalent open-source DFT code): https://www.quantum-espresso.org/
- SSSP pseudopotential library (PBE PAW): https://www.materialscloud.org/discover/sssp/table/efficiency
- Melt-quench ab initio MD method for a-IGZO (Nomura et al. 2007): 10.1103/PhysRevB.75.35212

## Workflow steps

### Step 1: Generate amorphous IGZO model
- Role: process
- Action: Prepare an amorphous InGaZnO4 structural model using the melt-quench ab initio molecular dynamics method described in Nomura et al. (Physical Review B 75, 35212, 2007).
- Evidence: `/app/outputs/igzo_generation.log`

### Step 2: DFT relaxation of H-incorporated a-IGZO
- Role: scored (load-bearing)
- Action: Create a neutral oxygen vacancy in the generated a-IGZO model, place an H2 molecule at the vacancy site, and perform DFT geometry optimization using PBE+U (U_In=7 eV, U_Ga=8 eV, U_Zn=8 eV) with a plane-wave cutoff of 800 eV and a 3x3x3 k-point mesh, until forces are < 0.001 eV/Å. Label the two hydrogen atoms according to their coordination (Ht triply coordinated, Hd doubly coordinated) and save the final relaxed coordinates.
- Output file: `/app/outputs/step01_relaxed_geometry.xyz`
- Format: txt
- Contract: XYZ file: first line atom count, second line comment indicating Ht and Hd labeling, then lines with element_symbol x y z (units in Å). The checker verifies the coordination numbers of the two hydrogen atoms (Ht coordinated to In, Ga, Zn; Hd to Ga, Zn) within a reasonable cutoff (~2.5 Å).
- Scoring: scored by hidden verifier

### Step 3: Compute vibrational frequencies and electronic DOS
- Role: scored (load-bearing)
- Action: Using the relaxed structure, compute force constants and Born effective charges via DFPT or finite differences to obtain infrared-active vibrational modes. Identify the two M-H stretching modes, compute their frequencies, and compute the stretching frequencies of gas-phase InH, GaH, ZnH at the same level of theory. Also compute total and partial DOS using a 5x5x5 k-point mesh, locating the occupied subgap state energy relative to VBM. Write results as a JSON file.
- Output file: `/app/outputs/step02_vibrational_and_dos.json`
- Format: json
- Contract: JSON object with keys: 'M_H_stretching_frequencies_cm-1' (list of two floats), 'mode_characters' (list of two strings), 'gas_phase_hydride_frequencies_cm-1' (object with keys InH, GaH, ZnH as floats), 'red_shifts_cm-1' (list of two floats), 'subgap_energy_above_VBM_eV' (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step01_relaxed_geometry.xyz`
- `/app/outputs/step02_vibrational_and_dos.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step01_relaxed_geometry.xyz
- path: `/app/outputs/step01_relaxed_geometry.xyz`
- format: txt
- purpose: scored
- target_policy: structural_audit
- description: Relaxed atomic geometry after DFT optimization. The checker performs a structural audit: verifies that exactly two hydrogen atoms are present, one has trigonal coordination to In, Ga, Zn, and the other has twofold coordination to Ga, Zn, within a distance cutoff of 2.5 Å.
- schema:
  - `type`: text
  - `description`: XYZ file: first line number of atoms, second line comment with hydrogen labeling (Ht/Hd), then element_symbol x y z (Å).

### step02_vibrational_and_dos.json
- path: `/app/outputs/step02_vibrational_and_dos.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Computed vibrational and electronic properties. The checker compares the M-H stretching frequencies, red-shifts, and subgap energy against hidden reference values derived from the experimental data, with appropriate tolerances.
- schema:
  - `type`: object
  - `required`: `M_H_stretching_frequencies_cm-1`, `mode_characters`, `gas_phase_hydride_frequencies_cm-1`, `red_shifts_cm-1`, `subgap_energy_above_VBM_eV`
  - `properties`:
    - `M_H_stretching_frequencies_cm-1`:
      - `type`: array
      - `items`:
        - `type`: number
    - `mode_characters`:
      - `type`: array
      - `items`:
        - `type`: string
    - `gas_phase_hydride_frequencies_cm-1`:
      - `type`: object
    - `red_shifts_cm-1`:
      - `type`: array
      - `items`:
        - `type`: number
    - `subgap_energy_above_VBM_eV`:
      - `type`: number

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step01_relaxed_geometry.xyz",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "text",
        "description": "XYZ file: first line number of atoms, second line comment with hydrogen labeling (Ht/Hd), then element_symbol x y z (Å)."
      },
      "description": "Relaxed atomic geometry after DFT optimization. The checker performs a structural audit: verifies that exactly two hydrogen atoms are present, one has trigonal coordination to In, Ga, Zn, and the other has twofold coordination to Ga, Zn, within a distance cutoff of 2.5 Å."
    },
    {
      "file": "step02_vibrational_and_dos.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "M_H_stretching_frequencies_cm-1",
          "mode_characters",
          "gas_phase_hydride_frequencies_cm-1",
          "red_shifts_cm-1",
          "subgap_energy_above_VBM_eV"
        ],
        "properties": {
          "M_H_stretching_frequencies_cm-1": {
            "type": "array",
            "items": {
              "type": "number"
            }
          },
          "mode_characters": {
            "type": "array",
            "items": {
              "type": "string"
            }
          },
          "gas_phase_hydride_frequencies_cm-1": {
            "type": "object"
          },
          "red_shifts_cm-1": {
            "type": "array",
            "items": {
              "type": "number"
            }
          },
          "subgap_energy_above_VBM_eV": {
            "type": "number"
          }
        }
      },
      "description": "Computed vibrational and electronic properties. The checker compares the M-H stretching frequencies, red-shifts, and subgap energy against hidden reference values derived from the experimental data, with appropriate tolerances."
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden, offline verifier scores each artifact independently after the task run, then combines the scores by weight to produce the final reward in [0,1]. The verifier does not re-run the DFT calculations; it inspects your submitted files against criteria derived from the experimental evidence and structural expectations.

- **Geometry (weight ~0.4):** The verifier parses the XYZ file and checks that exactly two hydrogen atoms are present. It verifies that one hydrogen (Ht) is within 2.5 Å of three metal atoms (at least one each of In, Ga, and Zn) and that the other hydrogen (Hd) is within 2.5 Å of two metal atoms (Ga and Zn). This structural audit ensures the relaxed positions reflect the coordination environment expected for hydride ions substituting at an oxygen vacancy.

- **Vibrational and electronic properties (weight ~0.6):** The verifier reads the JSON and compares your reported M–H stretching frequencies, red-shifts, and subgap energy to hidden reference values. The reference values are drawn from the experimental infrared absorption spectra and subgap threshold reported in the a-IGZO literature. Comparisons use tolerances that account for the expected variability of the PBE+U method and the amorphous model. The mode character assignments are checked for consistency with the dominant displacement pattern. Partial credit is awarded if results fall close to, but outside, the tolerance; fabricating numbers unrelated to a genuine calculation will score zero.

All checks are performed deterministically; no human judgment is involved.
