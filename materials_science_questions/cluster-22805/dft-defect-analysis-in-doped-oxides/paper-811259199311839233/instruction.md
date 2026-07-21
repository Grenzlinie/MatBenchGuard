# DFT Defect Analysis in Doped Oxides

## Problem background
Technetium-99 is a long-lived radioactive fission product whose mobility in the environment is controlled by its oxidation state. Immobilizing Tc(IV) in durable waste forms such as spinels is critical for nuclear waste management. Magnetite (Fe₃O₄) can incorporate reduced Tc(IV) into its structure, but at elevated temperatures (e.g., glass vitrification conditions) re‑oxidation to volatile pertechnetate, Tc(VII)O₄⁻, can occur, driving Tc out of the solid. Doping magnetite with first‑row transition metals has been proposed as a strategy to hinder this high‑temperature migration. This task aims to reproduce the key computational result that quantifies how different dopants (Ni, Zn, Co) influence Tc retention in magnetite, using ab initio molecular dynamics simulations. The central quantities are the equilibrium constants for Tc inside versus outside the surface and the energetic driving force for Tc migration.

## Approach
The study uses periodic density-functional theory (DFT) in the PBE+U approximation to model a B-terminated Fe₃O₄(001) slab containing a Tc impurity, and ab initio molecular dynamics (AIMD) to simulate the thermal motion of atoms. A static DFT energy comparison between configurations with Tc at a subsurface lattice site and at the surface provides the thermodynamic driving force for Tc movement. AIMD trajectories are generated for the undoped slab at two temperatures (25 °C and 600 °C) and for the slab doped with Ni, Zn, or Co at 600 °C. From the high‑temperature trajectories, atomic density profiles along the surface normal are computed to separate the Tc population into a region inside the surface and a region outside the surface. The equilibrium constant Keq = [Tc_in]/[Tc_out] and the corresponding Gibbs free‑energy change ΔG = −RT ln Keq are derived for each doping condition. These quantities constitute the scored output of this reproduction.

## Reproduction target
Compute the energy difference (in eV) between the subsurface and surface Tc configurations in undoped magnetite, and the equilibrium constants Keq (dimensionless) and free‑energy changes ΔG (kJ/mol) for the undoped magnetite and for the Ni‑, Zn‑, and Co‑doped systems at 600 °C. Write all results into a single JSON file at /app/outputs/equilibrium_constants.json.

## Assets

- CP2K open-source quantum chemistry package: https://www.cp2k.org/

## Workflow steps

### Step 1: Build slab models
- Role: process
- Action: Construct B-terminated Fe3O4(001) slab models using a 2×2×2 supercell (384 atoms, 12.5 Å vacuum). Substitute one surface octahedral Fe with Tc to create the undoped Tc-magnetite. For doping, additionally replace a nearby surface Fe with Ni, Zn, or Co. Also prepare a model with Tc at a subsurface inner lattice site for later energy comparison.
- Evidence: `/app/outputs/model_slabs.zip`

### Step 2: Static DFT energy for Tc subsurface vs surface
- Role: process
- Action: Perform spin-polarized DFT (PBE+U, U−J=3.5 eV) geometry relaxation and total energy calculation for the undoped Tc-magnetite slab with Tc at the surface and with Tc at the inner lattice site, using the slab models from step 01. Compute the energy difference (E_sub − E_surf).
- Evidence: `/app/outputs/energy_diff.txt`

### Step 3: AIMD for undoped Tc-magnetite
- Role: process
- Action: Run ab initio molecular dynamics (AIMD) in the NVT ensemble at 25 °C and 600 °C using the undoped Tc-magnetite slab with Tc at the surface (from step 01). Use spin-polarized DFT with PBE+U (U−J=3.5 eV), a Nosé–Hoover thermostat, and a 1.0 fs time step. Equilibrate for at least 20 ps and save the production portion (last 10–12 ps) of the trajectories.
- Evidence: `/app/outputs/undoped_trajectories.zip`

### Step 4: AIMD for doped Tc-magnetite at 600 °C
- Role: process
- Action: Run AIMD at 600 °C for the Ni-, Zn-, and Co-doped Tc-magnetite slabs (from step 01) using the same protocol as in step 03. Save the production portion of each trajectory.
- Evidence: `/app/outputs/doped_trajectories.zip`

### Step 5: Compute equilibrium constants and energy difference
- Role: scored (load-bearing)
- Action: From the AIMD trajectories at 600 °C (steps 03 and 04), compute atomic density profiles along the surface normal. Integrate the Tc population inside and outside the surface to obtain Keq = [Tc_in]/[Tc_out] for each doping case. Calculate ΔG = −RT ln(Keq) with T = 873 K. Retrieve the subsurface‑surface energy difference from step 02. Write the results to equilibrium_constants.json.
- Output file: `/app/outputs/equilibrium_constants.json`
- Format: json
- Contract: {"energy_difference_subsurface_surface_ev": number, "keq_table": [{"doping": "none", "Keq": number, "delta_G_kJmol": number}, {"doping": "Ni", "Keq": number, "delta_G_kJmol": number}, {"doping": "Zn", "Keq": number, "delta_G_kJmol": number}, {"doping": "Co", "Keq": number, "delta_G_kJmol": number}]}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/equilibrium_constants.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### equilibrium_constants.json
- path: `/app/outputs/equilibrium_constants.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: JSON object with two fields: 'energy_difference_subsurface_surface_ev' (eV) and 'keq_table' (array of objects, each with 'doping' ('none','Ni','Zn','Co'), 'Keq' (dimensionless), 'delta_G_kJmol' (kJ/mol)). The values are verified against hidden reference values.
- schema:
  - `type`: object
  - `required`:
    - `energy_difference_subsurface_surface_ev`: number
    - `keq_table`: array
  - `items`:
    - `doping`: string
    - `Keq`: number
    - `delta_G_kJmol`: number

Notes: The scored artifact is the equilibrium constants and energy difference derived entirely from the DFT/AIMD pipeline. The checker verifies the energy difference and the Keq/ΔG values against hidden paper-reported references with appropriate tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "equilibrium_constants.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "energy_difference_subsurface_surface_ev": "number",
          "keq_table": "array"
        },
        "items": {
          "doping": "string",
          "Keq": "number",
          "delta_G_kJmol": "number"
        }
      },
      "description": "JSON object with two fields: 'energy_difference_subsurface_surface_ev' (eV) and 'keq_table' (array of objects, each with 'doping' ('none','Ni','Zn','Co'), 'Keq' (dimensionless), 'delta_G_kJmol' (kJ/mol)). The values are verified against hidden reference values."
    }
  ],
  "notes": "The scored artifact is the equilibrium constants and energy difference derived entirely from the DFT/AIMD pipeline. The checker verifies the energy difference and the Keq/ΔG values against hidden paper-reported references with appropriate tolerances."
}
```

## How you are scored
A hidden verifier inspects your submitted /app/outputs/equilibrium_constants.json. It compares the energy difference and the Keq values for each doping condition against hidden reference ranges that are based on the paper’s published computational results, using tolerances appropriate for independent re‑implementations. The verifier also checks that the required process artifacts (model_slabs.zip, energy_diff.txt, undoped_trajectories.zip, doped_trajectories.zip) are present; while these do not carry a direct numeric score, their absence indicates that the intermediate steps were not performed and may affect the assessment of the final result. Simply reporting a set of numbers without executing the workflow will not earn a passing score.
