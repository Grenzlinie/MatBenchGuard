# First-principles adsorption energies and rotational spectra of H₂ in MOF-74

## Problem background
Molecular hydrogen (H₂) adsorption in nanoporous metal-organic frameworks (MOFs) is central to the development of practical hydrogen-storage materials. The material MOF-74, which features unsaturated metal sites, has attracted interest due to its strong H₂ affinity. Accurate first-principles prediction of H₂ binding energies, equilibrium geometries, and the low-lying rotational and translational quantum excitations of the adsorbed H₂ is crucial for interpreting inelastic neutron scattering (INS) experiments and for guiding material design. However, conventional density-functional approximations struggle to capture the van der Waals interactions that dominate H₂ binding. The present task uses the van der Waals density functional (vdW-DF) to compute the full adsorption energetics and quantum dynamics of H₂ in MOF-74, thereby providing a benchmark for the binding sites and spectral signatures.

## Approach
The task employs an open-source plane-wave or localized-basis DFT code (e.g., Quantum ESPRESSO, SIESTA, or Abinit) implementing the vdW-DF exchange-correlation functional. Starting from the experimental MOF-74 crystal structure, the workflow first maps the potential energy surface of a single H₂ molecule near the unsaturated Zn atom to locate the primary adsorption minimum. A secondary minimum above the oxygen triangle is identified by relaxing multiple H₂ molecules at a loading of 12 D₂ per primitive cell while keeping the host framework fixed. At both binding sites the orientational dependence of the interaction energy is sampled to build the hindered-rotor potential; this potential is fitted to spherical harmonics and the rigid-rotor Schrödinger equation is solved to obtain the rotational energy levels. Translational potentials along the three normal-mode coordinates are computed via small displacements, and the 1D Schrödinger equation is solved for each mode to extract the fundamental translational frequencies. Rotational and translational zero-point energies are then subtracted from the raw binding energies to yield effective binding energies. All derived quantities are consolidated into a single JSON artifact.

## Reproduction target
Using the experimental MOF-74 (CPO-27-Zn) crystal structure and the vdW-DF functional, compute the following quantities and write them to `/app/outputs/adsorption_properties.json`:

- For the primary Zn site (1 H₂ per primitive cell): the binding energy (meV) and the Zn–H₂ distance (Å) at the potential minimum.
- For the secondary O site (12 D₂ per cell, relaxed with fixed host): the closest sorbate–sorbent distance (Å).
- For both sites: the three para–ortho rotational transition energies (meV) obtained by solving the rigid-rotor Schrödinger equation on the orientation-dependent potential.
- For both sites: the three fundamental translational frequencies (meV/ħ) obtained by solving the 1D Schrödinger equation along each normal mode.
- For both sites: the effective binding energy (meV) after subtracting rotational and translational zero-point energies from the raw binding energy.

The output file must be a valid JSON object with the exact keys and array sizes specified in the Output contract.

## Assets

- Experimental MOF-74 (CPO-27-Zn) crystal structure: https://doi.org/10.1021/ja056088x
- Open-source DFT code with van der Waals density functional (vdW-DF) implementation: https://www.quantum-espresso.org

## Workflow steps

### Step 1: Acquire and prepare MOF-74 crystal structure
- Role: process
- Action: Obtain the experimental atomic coordinates of MOF-74 (Zn) from the public crystallographic database (CCDC deposition 279484) or supplementary material, and convert to a DFT input format.
- Evidence: `/app/outputs/structure_prepared.txt`

### Step 2: Zn-site potential energy surface scan
- Role: process
- Action: Using the prepared structure and vdW-DF, compute the MOF–H2 interaction energy on a grid of H2 positions near the unsaturated Zn atom for 1 H2 per primitive cell (1/6 H2 per Zn). Record the energy map.
- Evidence: `/app/outputs/zn_pes_data.json`

### Step 3: Fixed-host relaxation at the O site
- Role: process
- Action: With the same host structure and a loading of 12 D2 per cell, keep the MOF atoms fixed and relax the dihydrogen positions using vdW-DF until forces are converged to ~12 meV/Å. Identify the relaxed positions and the closest sorbate–sorbent distance above the oxygen triangle.
- Evidence: `/app/outputs/o_site_relaxation.json`

### Step 4: Orientational potential calculations
- Role: process
- Action: At the Zn-site minimum (1 H2/cell) and the O-site minimum (12 H2/cell), compute the MOF–H2 interaction energy as a function of molecular orientation (θ, φ) using vdW-DF. Output the orientation-dependent potential for each site.
- Evidence: `/app/outputs/orientational_potentials.json`

### Step 5: Translational potential curves via small displacements
- Role: process
- Action: For both the Zn and O sites, displace the H2 molecule along the normal coordinate directions (n1, n2, n3) and compute the vdW-DF energy and forces. Generate the 1D potential energy curves for each translational mode.
- Evidence: `/app/outputs/translational_potentials.json`

### Step 6: Full‑cell relaxation with 24 H2 (optional, for qualitative agreement)
- Role: process
- Action: Using the experimental host structure, place 24 H2 molecules per primitive cell with symmetry‑adapted initial positions and relax all H2 coordinates with fixed host using vdW-DF. The result provides the hydrogen uptake geometry but is not numerically scored.
- Evidence: `/app/outputs/full_cell_positions.xyz`

### Step 7: Compute derived adsorption properties and write final artifact
- Role: scored (load-bearing)
- Action: From the raw DFT data, locate the Zn-site minimum to extract binding energy (meV) and Zn–H2 distance (Å); from the O-site relaxation extract the closest sorbate–sorbent distance (Å); fit the orientational potentials to spherical harmonics, solve the rigid-rotor Schrödinger equation, and report the three para–ortho transition energies for Zn and O sites (meV); solve the 1D translational Schrödinger equation for each normal mode to obtain the three fundamental frequencies for Zn and O sites (meV/ħ); compute rotational and translational zero‑point energies and subtract them from raw binding energies to obtain zero‑point corrected effective binding energies (meV). Write all quantities to `/app/outputs/adsorption_properties.json`.
- Output file: `/app/outputs/adsorption_properties.json`
- Format: json
- Contract: JSON object with keys: binding_energy_Zn_meV (number), Zn_H2_distance_A (number), O_site_closest_distance_A (number), rotational_transitions_Zn_meV (array of 3 numbers), rotational_transitions_O_meV (array of 3 numbers), translational_frequencies_Zn_meVps (array of 3 numbers), translational_frequencies_O_meVps (array of 3 numbers), effective_binding_energy_Zn_meV (number), effective_binding_energy_O_meV (number).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/adsorption_properties.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### adsorption_properties.json
- path: `/app/outputs/adsorption_properties.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Consolidated adsorption properties from vdW-DF calculations: raw binding energies, sorbate–sorbent distances, rotational para–ortho transition energies, translational fundamental frequencies, and zero-point-corrected effective binding energies at the primary Zn site and secondary O site.
- schema:
  - `type`: object
  - `required`:
    - `binding_energy_Zn_meV`: number
    - `Zn_H2_distance_A`: number
    - `O_site_closest_distance_A`: number
    - `rotational_transitions_Zn_meV`: array of 3 numbers
    - `rotational_transitions_O_meV`: array of 3 numbers
    - `translational_frequencies_Zn_meVps`: array of 3 numbers
    - `translational_frequencies_O_meVps`: array of 3 numbers
    - `effective_binding_energy_Zn_meV`: number
    - `effective_binding_energy_O_meV`: number
  - `items`: object
  - `required_columns`:
  - `units`:
    - `binding_energy_Zn_meV`: meV
    - `Zn_H2_distance_A`: Å
    - `O_site_closest_distance_A`: Å
    - `rotational_transitions_Zn_meV`: meV
    - `rotational_transitions_O_meV`: meV
    - `translational_frequencies_Zn_meVps`: meV/ħ
    - `translational_frequencies_O_meVps`: meV/ħ
    - `effective_binding_energy_Zn_meV`: meV
    - `effective_binding_energy_O_meV`: meV

Notes: The full-cell relaxation of 24 H2 (step_06) is not scored; it provides qualitative geometry. All other quantities are compared to hidden paper-reported values within tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "adsorption_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "binding_energy_Zn_meV": "number",
          "Zn_H2_distance_A": "number",
          "O_site_closest_distance_A": "number",
          "rotational_transitions_Zn_meV": "array of 3 numbers",
          "rotational_transitions_O_meV": "array of 3 numbers",
          "translational_frequencies_Zn_meVps": "array of 3 numbers",
          "translational_frequencies_O_meVps": "array of 3 numbers",
          "effective_binding_energy_Zn_meV": "number",
          "effective_binding_energy_O_meV": "number"
        },
        "items": {},
        "required_columns": [],
        "units": {
          "binding_energy_Zn_meV": "meV",
          "Zn_H2_distance_A": "Å",
          "O_site_closest_distance_A": "Å",
          "rotational_transitions_Zn_meV": "meV",
          "rotational_transitions_O_meV": "meV",
          "translational_frequencies_Zn_meVps": "meV/ħ",
          "translational_frequencies_O_meVps": "meV/ħ",
          "effective_binding_energy_Zn_meV": "meV",
          "effective_binding_energy_O_meV": "meV"
        }
      },
      "description": "Consolidated adsorption properties from vdW-DF calculations: raw binding energies, sorbate–sorbent distances, rotational para–ortho transition energies, translational fundamental frequencies, and zero-point-corrected effective binding energies at the primary Zn site and secondary O site."
    }
  ],
  "notes": "The full-cell relaxation of 24 H2 (step_06) is not scored; it provides qualitative geometry. All other quantities are compared to hidden paper-reported values within tolerances."
}
```

## How you are scored
A hidden verifier reads your `/app/outputs/adsorption_properties.json` and compares each scalar and array entry to a hidden reference value derived from the paper's published results. Each quantity is checked within a tolerance that accounts for the typical spread between different vdW-DF implementations; you are not required to match the paper's values exactly. The verifier assigns partial credit per field, and the total reward is a weighted combination of all fields. Simply printing the paper's numbers without performing the DFT workflow will not produce the required intermediate potentials and thus will not satisfy the scoring. You must genuinely execute the pipeline steps to obtain the adsorption properties.
