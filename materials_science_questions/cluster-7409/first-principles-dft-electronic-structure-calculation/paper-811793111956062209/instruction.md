# DFT+U calculations of Ta/Nb-doped CeO2(110) surface properties and NO2 adsorption

## Problem background
Cerium dioxide (CeO2) is a widely used metal oxide in catalysis, owing largely to the easy reduction of Ce4+ to Ce3+ that accompanies oxygen vacancy formation. However, generating Ce3+ ions without creating oxygen vacancies could offer a more controlled path to tune surface reactivity. This task investigates an alternative route: doping the CeO2(110) surface with +5 cations (Ta and Nb). The extra electron introduced by each dopant is expected to localize on a single Ce site, producing a Ce3+ ion, and this reduced site should then become active for NO2 reduction. The goal is to compute the structural and electronic consequences of doping and the resulting interaction with NO2.

## Approach
The computational approach uses spin‑polarized density functional theory with an on‑site Coulomb correction (DFT+U, U=5 eV) applied to the Ce 4f states. The exchange‑correlation functional is PBE, and the core–valence interaction is described by projector augmented wave (PAW) pseudopotentials (from the SSSP library).

First, slab models of the CeO2(110) surface are built with a (2×2) surface supercell, seven atomic layers, and a 15 Å vacuum gap. One surface Ce atom is substitutionally replaced by Ta and separately by Nb to create two doped surface models.

Geometry relaxations are performed for each doped slab with the bottom two layers fixed. From the relaxed structures, the dopant–oxygen distances (four surface and two subsurface) and the magnetic moment of the Ce ion that is reduced to Ce3+ are extracted.

The interaction with NO2 is then studied: the total energy of an isolated NO2 molecule is computed in a periodic box. For each doped surface, an NO2 molecule is placed over the reduced Ce3+ site (oxygen oriented towards the Ce) and its atomic positions are relaxed with the slab kept fixed. The adsorption energy is calculated as the energy difference between the adsorbed system and the sum of the isolated slab and NO2 molecule. The lengths of the N–O_s (oxygen bound to Ce) and N–O_n (remote oxygen) bonds are measured from the final relaxed geometry.

All calculations are carried out for both Ta‑ and Nb‑doped surfaces, allowing a comparison of the two dopants.

## Reproduction target
Using DFT+U with the parameters and pseudopotentials described, compute the following quantities for both Ta‑ and Nb‑doped CeO2(110) surfaces:

- The relaxed dopant–oxygen distances: four surface distances and two subsurface distances (in Å) for each dopant.
- The magnetic moment (in µB) of the Ce ion that becomes reduced to Ce3+ upon doping.
- The adsorption energy (in eV) of NO2 on each doped surface, defined as E(adsorbed system) – [E(slab) + E(isolated NO2)].
- The N–O bond lengths (in Å) after relaxation: the bond to the oxygen that coordinates to Ce (N–O_s) and the bond to the remote oxygen (N–O_n).

Report the results in the two JSON files specified in the workflow steps. The target is to reproduce the DFT+U predictions of these structural, electronic, and adsorption properties; a qualitative comparison of the Ta and Nb cases is also expected from the computed numbers.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- Ce PAW pseudopotential (PBE): 10.24435/materialscloud:2022.0026/v1
- O PAW pseudopotential (PBE): 10.24435/materialscloud:2022.0026/v1
- Ta PAW pseudopotential (PBE): 10.24435/materialscloud:2022.0026/v1
- Nb PAW pseudopotential (PBE): 10.24435/materialscloud:2022.0026/v1

## Workflow steps

### Step 1: Build CeO2 (110) slab models
- Role: process
- Action: Generate a (2x2) surface supercell of CeO2(110) with 7 atomic layers and 15 Å vacuum gap. Substitutionally dope one surface Ce with Ta and Nb to create Ta- and Nb-doped slab models.
- Evidence: none

### Step 2: DFT+U relaxation of Ta-doped CeO2(110)
- Role: process
- Action: Relax the Ta-doped slab using DFT+U (U=5 eV on Ce 4f) with PBE functional, PAW pseudopotentials, spin-polarized calculation. Fix bottom two layers during relaxation. Log energy and final structure.
- Evidence: `/app/outputs/ta_relaxation.log`

### Step 3: DFT+U relaxation of Nb-doped CeO2(110)
- Role: process
- Action: Relax the Nb-doped slab using the same DFT+U settings as for Ta. Log energy and final structure.
- Evidence: `/app/outputs/nb_relaxation.log`

### Step 4: Analysis of doped surface properties
- Role: scored (load-bearing)
- Action: From the relaxed Ta- and Nb-doped slab structures, extract the four surface dopant-O distances, two subsurface dopant-O distances, and the magnetic moment of the reduced Ce ion. Write the results to doped_surface_properties.json.
- Output file: `/app/outputs/doped_surface_properties.json`
- Format: json
- Contract: {"Ta": {"surface_distances": [4 floats, in Angstrom], "subsurface_distances": [2 floats, in Angstrom], "ce_magnetic_moment": float}, "Nb": {"surface_distances": [4 floats], "subsurface_distances": [2 floats], "ce_magnetic_moment": float}}
- Scoring: scored by hidden verifier

### Step 5: DFT+U NO2 molecule reference calculation
- Role: process
- Action: Perform a spin-polarized DFT+U calculation of an isolated NO2 molecule in a periodic box using the same functional and pseudopotentials to obtain its total energy.
- Evidence: `/app/outputs/no2_reference.log`

### Step 6: DFT+U NO2 adsorption on Ta-doped surface
- Role: process
- Action: Place an NO2 molecule over the reduced Ce3+ site of the relaxed Ta-doped slab (oxygen oriented toward Ce3+). Relax the adsorbate atomic positions while keeping the slab fixed. Log final structure and total energy.
- Evidence: `/app/outputs/ta_no2_adsorption.log`

### Step 7: DFT+U NO2 adsorption on Nb-doped surface
- Role: process
- Action: Place an NO2 molecule over the reduced Ce3+ site of the relaxed Nb-doped slab (oxygen toward Ce3+). Relax the adsorbate atomic positions while keeping the slab fixed. Log final structure and total energy.
- Evidence: `/app/outputs/nb_no2_adsorption.log`

### Step 8: Analysis of NO2 adsorption properties
- Role: scored (load-bearing)
- Action: Calculate the adsorption energy as E(adsorbed system) - [E(slab) + E(NO2)] using total energies from the relaxations. Extract N-Os and N-On bond lengths from the final relaxed structures. Write Ta and Nb results to no2_adsorption_properties.json.
- Output file: `/app/outputs/no2_adsorption_properties.json`
- Format: json
- Contract: {"Ta": {"adsorption_energy": float, "n_o_s": float, "n_o_n": float}, "Nb": {"adsorption_energy": float, "n_o_s": float, "n_o_n": float}}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/doped_surface_properties.json`
- `/app/outputs/no2_adsorption_properties.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### doped_surface_properties.json
- path: `/app/outputs/doped_surface_properties.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Dopant-oxygen distances and Ce magnetic moment for Ta- and Nb-doped CeO2(110) surfaces. Compared to paper-reported DFT+U values with tolerances.
- schema:
  - `type`: object
  - `required`:
    - `Ta`: object with keys surface_distances (array of 4 numbers), subsurface_distances (array of 2 numbers), ce_magnetic_moment (number)
    - `Nb`: object with keys surface_distances (array of 4 numbers), subsurface_distances (array of 2 numbers), ce_magnetic_moment (number)

### no2_adsorption_properties.json
- path: `/app/outputs/no2_adsorption_properties.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: NO2 adsorption energy and N-O bond lengths for Ta- and Nb-doped CeO2(110) surfaces. Adsorption energy scored threshold_or_better; bond lengths scored exact_match within tolerances.
- schema:
  - `type`: object
  - `required`:
    - `Ta`: object with keys adsorption_energy (number), n_o_s (number), n_o_n (number)
    - `Nb`: object with keys adsorption_energy (number), n_o_s (number), n_o_n (number)

Notes: HSE06 calculations and undoped surface tests omitted per taskability scope. Only DFT+U (U=5 eV on Ce 4f) is required.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "doped_surface_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "Ta": "object with keys surface_distances (array of 4 numbers), subsurface_distances (array of 2 numbers), ce_magnetic_moment (number)",
          "Nb": "object with keys surface_distances (array of 4 numbers), subsurface_distances (array of 2 numbers), ce_magnetic_moment (number)"
        }
      },
      "description": "Dopant-oxygen distances and Ce magnetic moment for Ta- and Nb-doped CeO2(110) surfaces. Compared to paper-reported DFT+U values with tolerances."
    },
    {
      "file": "no2_adsorption_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "Ta": "object with keys adsorption_energy (number), n_o_s (number), n_o_n (number)",
          "Nb": "object with keys adsorption_energy (number), n_o_s (number), n_o_n (number)"
        }
      },
      "description": "NO2 adsorption energy and N-O bond lengths for Ta- and Nb-doped CeO2(110) surfaces. Adsorption energy scored threshold_or_better; bond lengths scored exact_match within tolerances."
    }
  ],
  "notes": "HSE06 calculations and undoped surface tests omitted per taskability scope. Only DFT+U (U=5 eV on Ce 4f) is required."
}
```

## How you are scored
A hidden verifier reads the two scored JSON files you write and independently scores each artifact. Every numeric field is compared against a reference value derived from the original study. The final reward is a weighted sum of the per‑stage scores.

 *Important*: the verifier checks that your computed numbers are consistent with the reference; it does not merely confirm that a file is present and correctly shaped. You must run the described DFT+U workflow and write the results you obtain — reporting the original paper’s numbers without actually performing the calculations will not pass. No gold values or tolerances are revealed to you; the verifier makes the comparison automatically.
