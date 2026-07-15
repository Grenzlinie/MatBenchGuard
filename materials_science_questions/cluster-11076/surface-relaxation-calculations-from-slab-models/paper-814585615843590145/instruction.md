# Wurtzite CdSe(1010) surface relaxation via empirical tight-binding energy minimization

## Problem background
Wurtzite-structure compound semiconductors, such as CdSe, expose cleavage faces for which the atomic geometry and electronic structure are not simply bulk truncations. Whether the (10\={1}0) surface develops a significant bond‑rotation relaxation that lowers a surface state near the top of the valence band is an open question – one that determines the physical mechanism driving the surface reconstruction. This task investigates that question computationally by implementing a nearest‑neighbour sp^3 tight‑binding model for CdSe, relaxing the surface via total‑energy minimisation, and determining whether a surface bound state appears and what relaxed structural parameters result.

## Approach
The central idea is that the surface atomic relaxation results from a balance between electronic energy (from surface dangling bonds) and an elastic energy that resists displacements from the bulk positions. An empirical nearest‑neighbour sp^3 tight‑binding Hamiltonian is constructed for CdSe using fixed on‑site energies and Slater–Koster interaction parameters (provided below). The surface is modelled as a slab derived from the wurtzite (10\={1}0) orientation, with the top few atomic layers allowed to move. The total energy, a sum of the electronic tight‑binding energy and a harmonic elastic energy with given parameters U₁ and U₂, is minimised to find the relaxed geometry. The elastic contribution follows from the bulk modulus and penalises atomic displacements. After relaxation, the surface band structure and surface density of states are computed using the final geometry. From these, the presence of a surface bound state near the top of the valence band and its energy at the M point of the surface Brillouin zone can be determined. The workflow thus successively obtains the relaxed structural parameters and then the surface electronic structure.

## Reproduction target
Compute, for the (10\={1}0) surface of wurtzite CdSe, the relaxed structural parameters Δ₁⊥, Δ₁y, d₁₂⊥, d₁₂y, Δ₂⊥ (all in Å) and ω₁ (in degrees). Report these in `/app/outputs/relaxed_parameters.json`. Subsequently, using that relaxed geometry, compute the surface band structure and identify the surface bound state S₁ near the top of the valence band. Report in `/app/outputs/surface_band_structure.json` the energy (in eV relative to the valence‑band maximum) of this state at the M point, as well as a boolean indicating whether the state is found. The evaluation is based solely on these two files; completing both steps is required.

## Assets

- Wurtzite CdSe crystal structure: https://next-gen.materialsproject.org/materials/mp-2691?formula=CdSe

## Parameters

The empirical sp3 tight‑binding parameters and elastic energy parameters from Table II are:

* On‑site energies (eV): E_s(Se) = -10.960, E_p(Se) = 1.640, E_s(Cd) = 1.360, E_p(Cd) = 4.560.
* Slater–Koster interactions (eV): V_{ssσ} = -0.659, V_{spσ}(Se→Cd) = 0.342, V_{spσ}(Cd→Se) = 2.814, V_{ppσ} = 3.361, V_{ppπ} = -0.655.
* Elastic parameters (eV/atom): U1 = -14.953, U2 = 66.872.

## Workflow steps

### Step 1: Surface relaxation and parameter extraction
- Role: scored (load-bearing)
- Action: Construct the ideal CdSe(101̄0) wurtzite slab using the bulk lattice constants. Implement the empirical sp3 nearest‑neighbour tight‑binding Hamiltonian with the given on‑site energies and Slater–Koster interactions (parameters provided in the instruction). Perform total‑energy minimisation that combines the electronic energy from the tight‑binding model with a harmonic elastic energy (elastic parameters U1, U2 given). Relax the top few atomic layers and write the final geometric parameters (Δ1⊥, Δ1y, d12,y, d12,⊥, Δ2⊥, ω1) to relaxed_parameters.json.
- Output file: `/app/outputs/relaxed_parameters.json`
- Format: json
- Contract: {"delta_1_perp": "float (Å)", "delta_1_y": "float (Å)", "d_12_y": "float (Å)", "d_12_perp": "float (Å)", "delta_2_perp": "float (Å)", "omega_1": "float (degrees)"}
- Scoring: scored by hidden verifier

### Step 2: Surface electronic structure and surface state identification
- Role: scored
- Action: Using the relaxed surface geometry, compute the surface band structure along high‑symmetry directions (including the M point) and the surface density of states. Identify the surface bound state S1 near the top of the valence band. Write a JSON file with the energy of S1 at the M point (in eV relative to the valence‑band maximum) and a boolean indicating whether the state exists.
- Output file: `/app/outputs/surface_band_structure.json`
- Format: json
- Contract: {"s1_energy_M_point": "float|null (eV relative to VBM)", "surface_state_exists": "boolean"}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/relaxed_parameters.json`
- `/app/outputs/surface_band_structure.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### relaxed_parameters.json
- path: `/app/outputs/relaxed_parameters.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Relaxed surface structural parameters obtained from the tight‑binding energy minimisation.
- schema:
  - `type`: object
  - `required`:
    - `delta_1_perp`: float (Å)
    - `delta_1_y`: float (Å)
    - `d_12_y`: float (Å)
    - `d_12_perp`: float (Å)
    - `delta_2_perp`: float (Å)
    - `omega_1`: float (degrees)

### surface_band_structure.json
- path: `/app/outputs/surface_band_structure.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Existence and energy of the surface state S1 at the M point of the surface Brillouin zone.
- schema:
  - `type`: object
  - `required`:
    - `s1_energy_M_point`: float or null (eV relative to VBM)
    - `surface_state_exists`: boolean

Notes: The tight‑binding parameters and elastic energy parameters are provided in the instruction as fixed inputs; the agent does not need to fit them. The scoring compares the submitted structural parameters and surface‑state energy to the paper’s theoretical values using tolerances. The relaxation step is load‑bearing: its output must be computed via total‑energy minimisation, not guessed.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "relaxed_parameters.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": {
          "delta_1_perp": "float (Å)",
          "delta_1_y": "float (Å)",
          "d_12_y": "float (Å)",
          "d_12_perp": "float (Å)",
          "delta_2_perp": "float (Å)",
          "omega_1": "float (degrees)"
        }
      },
      "description": "Relaxed surface structural parameters obtained from the tight‑binding energy minimisation."
    },
    {
      "file": "surface_band_structure.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": {
          "s1_energy_M_point": "float or null (eV relative to VBM)",
          "surface_state_exists": "boolean"
        }
      },
      "description": "Existence and energy of the surface state S1 at the M point of the surface Brillouin zone."
    }
  ],
  "notes": "The tight‑binding parameters and elastic energy parameters are provided in the instruction as fixed inputs; the agent does not need to fit them. The scoring compares the submitted structural parameters and surface‑state energy to the paper’s theoretical values using tolerances. The relaxation step is load‑bearing: its output must be computed via total‑energy minimisation, not guessed."
}
```

## How you are scored
A hidden verifier reads the two output files and independently compares each reported value (relaxation parameters, surface‑state energy, existence flag) against the expected theoretical predictions. Each scored artifact contributes a share to the final reward, with the relaxation parameters carrying the majority weight. The comparison is done with tolerances that account for legitimate implementation and convergence differences, and uses a threshold‑or‑better policy: meeting or exceeding the expected physical result earns full credit on that quantity, and the credit decreases only when the error grows beyond the tolerance. Reporting values without performing the required minimisation and band structure calculation will not earn full credit.
