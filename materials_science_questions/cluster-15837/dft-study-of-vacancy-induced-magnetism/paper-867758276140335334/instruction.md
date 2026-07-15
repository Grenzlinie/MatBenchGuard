# DFT study of vacancy-induced magnetism on Si(111)-√3×√3 surface

## Problem background
This task investigates magnetism induced by a silicon adatom vacancy (V_Siad) on the boron-doped Si(111)-√3×√3 surface, a surface that is stable for highly boron-doped silicon. When an adatom is removed, three silicon dangling bonds are exposed, creating a half-filled doubly degenerate defect state inside the band gap. The key questions are whether this defect can sustain a local magnetic moment and how hole doping influences the exchange coupling between adjacent defects. The goal is to determine, through first-principles density functional theory (DFT), the magnetic moment of an isolated defect, the energy gain from spin polarization, and the relative stability of ferromagnetic versus antiferromagnetic alignment for two nearby defects in both the undoped and hole-doped regimes, as well as the resulting magnetization and spin polarization at the Fermi level in the doped case.

## Approach
The study uses spin-polarized DFT with the Perdew-Burke-Ernzerhof (PBE) exchange-correlation functional and the projector augmented wave (PAW) method, with Quantum ESPRESSO as the computational engine. The Si(111)-√3×√3 surface is modelled as a slab containing 10 silicon monolayers with substitutional boron atoms in a 2×2 √3×√3 supercell, passivated on the bottom by hydrogen and separated from its periodic images by about 7 Å of vacuum. Three structural models are built: a perfect surface, a surface with a single V_Siad defect, and a supercell with two nearest-neighbor V_Siad defects. For each model the following calculations are performed: (i) a spin-unpolarized geometry optimization to obtain a non-magnetic reference energy, (ii) a spin-polarized relaxation to obtain the magnetic solution and its total energy, magnetic moment, and spin-resolved density of states. For the two-defect supercell both ferromagnetic (FM) and antiferromagnetic (AFM) spin alignments are optimized. The effect of hole doping is investigated by introducing a net charge corresponding to 0.6 hole per defect and repeating the FM and AFM relaxations. All runs share the same DFT technical parameters—plane-wave cutoff and k-point sampling—consistent with the original paper; the detailed numerical values are chosen by the agent based on standard practice and the paper’s description. The final step compares the computed total energies to extract energy gains and energy differences between FM and AFM configurations, and computes the magnetization per defect and the spin polarization at the Fermi level from the doped FM density of states.

## Reproduction target
Run the complete DFT workflow and collect in `/app/outputs/results.json` the following six quantities, each computed from the calculations described in the workflow steps:

1. **magnetic_moment_isolated** – total magnetic moment of the isolated V_Siad defect (in μB).
2. **delta_E_spin_polarization** – energy gain from spin polarization, defined as the non‑magnetic total energy minus the spin‑polarized total energy (positive when the spin‑polarized solution is lower; in meV).
3. **delta_E_FM_AFM_undoped** – energy difference between FM and AFM alignments for the undoped two‑defect supercell (E_FM – E_AFM; positive means AFM is favoured, in meV).
4. **delta_E_FM_AFM_doped** – same energy difference for the supercell with 0.6 hole per defect (negative means FM is favoured, in meV).
5. **magnetization_per_defect_doped** – magnetization per defect in the doped FM case (in μB).
6. **spin_polarization_at_EF** – spin polarization at the Fermi level for the doped FM case, defined as (DOS_up – DOS_dn) / (DOS_up + DOS_dn) (dimensionless fraction).

The quantities must be derived from your own DFT relaxations; do not enter the paper’s reported numbers.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- PBE PAW pseudopotentials for Si, B, H: Obtain from QE pseudopotential page or SSSP library.

## Workflow steps

### Step 1: Build slab supercells
- Role: process
- Action: Construct atomic structures for: (a) perfect Si(111)-√3×√3 surface 2×2 supercell (10 Si monolayers, bottom H passivation, ~7 Å vacuum) with substitutional boron atoms; (b) an isolated V_Siad defect by removing one Si adatom; (c) a supercell with two nearest-neighbor V_Siad defects. Use the experimental silicon lattice constant and the known atomic positions of the √3×√3 reconstruction.
- Evidence: none

### Step 2: Relax isolated V_Siad (non-magnetic)
- Role: process
- Action: Run spin-unpolarized DFT geometry optimization for the isolated V_Siad defect slab. Use PBE PAW pseudopotentials, plane-wave cutoff around 318 eV, and an 8×8×1 Monkhorst-Pack k-point grid. Record the relaxed geometry and total energy.
- Evidence: `/app/outputs/isolated_nm_energy.txt`

### Step 3: Relax isolated V_Siad (spin-polarized)
- Role: process
- Action: Run spin-polarized DFT geometry optimization for the isolated V_Siad defect slab, starting from the non-magnetic relaxed structure. Use the same DFT parameters. Record the spin-polarized total energy, spin density, and magnetic moment.
- Evidence: `/app/outputs/isolated_sp_energy.txt`

### Step 4: Relax two-defect NN (FM)
- Role: process
- Action: Run spin-polarized DFT geometry optimization for the supercell with two nearest-neighbor V_Siad defects, initialized with ferromagnetic (parallel) spin alignment. Use the same DFT parameters. Record the total energy.
- Evidence: `/app/outputs/twodef_FM_energy.txt`

### Step 5: Relax two-defect NN (AFM)
- Role: process
- Action: Run spin-polarized DFT geometry optimization for the same two-defect supercell but initialized with antiferromagnetic (antiparallel) spin alignment. Use the same DFT parameters. Record the total energy.
- Evidence: `/app/outputs/twodef_AFM_energy.txt`

### Step 6: Doped FM calculation (0.6 hole/defect)
- Role: process
- Action: For the two-defect supercell, introduce a net charge corresponding to 0.6 hole per defect (adjust total electron count or use a background charge) and perform a spin-polarized DFT geometry optimization with ferromagnetic spin alignment. Use the same DFT parameters. Record the total energy, magnetization, and spin-resolved density of states (DOS).
- Evidence: `/app/outputs/doped_FM_energy.txt`

### Step 7: Doped AFM calculation (0.6 hole/defect)
- Role: process
- Action: For the two-defect supercell with 0.6 hole per defect, perform a spin-polarized DFT geometry optimization with antiferromagnetic spin alignment. Use the same DFT parameters. Record the total energy and spin-resolved DOS.
- Evidence: `/app/outputs/doped_AFM_energy.txt`

### Step 8: Collect and compute final results
- Role: scored (load-bearing)
- Action: From the DFT outputs of the preceding steps, compute the following quantities and write them to results.json: (a) total magnetic moment of the isolated V_Siad defect; (b) energy gain from spin polarization, defined as the energy of the non-magnetic solution minus the spin-polarized solution (positive when spin-polarized is lower); (c) energy difference between FM and AFM alignments for the undoped two-defect supercell (E_FM - E_AFM, where a positive value means AFM is favored); (d) the same energy difference for the 0.6 hole/defect doped case (negative when FM is favored); (e) magnetization per defect in the doped FM case; (f) spin polarization at the Fermi level for the doped FM case, defined as P(E_F) = (DOS_up - DOS_dn) / (DOS_up + DOS_dn).
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: JSON object with keys: magnetic_moment_isolated (float, μB), delta_E_spin_polarization (float, meV), delta_E_FM_AFM_undoped (float, meV), delta_E_FM_AFM_doped (float, meV), magnetization_per_defect_doped (float, μB), spin_polarization_at_EF (float, fraction).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results.json
- path: `/app/outputs/results.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Scored artifact containing the six headline reproduction quantities. The hidden checker compares each field to the paper-reported gold values using absolute tolerances and directional overrides where the paper states that a larger or more negative value is better (e.g., larger spin-polarization energy gain, more negative energy difference for doped FM).
- schema:
  - `type`: object
  - `required`:
    - `magnetic_moment_isolated`: float
    - `delta_E_spin_polarization`: float
    - `delta_E_FM_AFM_undoped`: float
    - `delta_E_FM_AFM_doped`: float
    - `magnetization_per_defect_doped`: float
    - `spin_polarization_at_EF`: float
  - `units`:
    - `magnetic_moment_isolated`: μB
    - `delta_E_spin_polarization`: meV
    - `delta_E_FM_AFM_undoped`: meV
    - `delta_E_FM_AFM_doped`: meV
    - `magnetization_per_defect_doped`: μB
    - `spin_polarization_at_EF`: dimensionless fraction

Notes: All quantities are computed from the DFT relaxations specified in the workflow steps. The target policy for the file is 'exact_match' with per-field tolerances and directional logic implemented in the hidden checker. No further scored artifacts are required.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "magnetic_moment_isolated": "float",
          "delta_E_spin_polarization": "float",
          "delta_E_FM_AFM_undoped": "float",
          "delta_E_FM_AFM_doped": "float",
          "magnetization_per_defect_doped": "float",
          "spin_polarization_at_EF": "float"
        },
        "units": {
          "magnetic_moment_isolated": "μB",
          "delta_E_spin_polarization": "meV",
          "delta_E_FM_AFM_undoped": "meV",
          "delta_E_FM_AFM_doped": "meV",
          "magnetization_per_defect_doped": "μB",
          "spin_polarization_at_EF": "dimensionless fraction"
        }
      },
      "description": "Scored artifact containing the six headline reproduction quantities. The hidden checker compares each field to the paper-reported gold values using absolute tolerances and directional overrides where the paper states that a larger or more negative value is better (e.g., larger spin-polarization energy gain, more negative energy difference for doped FM)."
    }
  ],
  "notes": "All quantities are computed from the DFT relaxations specified in the workflow steps. The target policy for the file is 'exact_match' with per-field tolerances and directional logic implemented in the hidden checker. No further scored artifacts are required."
}
```

## How you are scored
A hidden verifier reads your `/app/outputs/results.json` and independently scores each of the six required quantities. For each quantity the verifier compares your computed value to the expected result derived from the original paper, using tolerances that account for the differences in DFT implementation and numerical settings. Quantities are directional where appropriate (e.g., a larger energy gain or a more negative energy difference for FM in the doped case is considered equally or more favourable). The per‑quantity scores are combined by weight into a final reward between 0 and 1. The verifier also checks that the JSON structure matches the required schema. Simply writing the paper’s numbers without performing the computation will not pass the verifier because the tolerances and the verifier’s internal logic make such an attempt detectable and insufficient to earn credit.
