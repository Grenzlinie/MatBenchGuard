# Hydrogen adsorption and diffusion in non-interpenetrating and interpenetrating IRMOFs via classical molecular dynamics

## Problem background
This work investigates how the interlocking of framework backbones (interpenetration) changes the local environment for hydrogen molecules and, consequently, their adsorption and mobility in microporous cavities. The goal is to quantify the H₂–framework interaction energy for two standard force fields (UFF and DREIDING) and to measure the distribution of adsorbed hydrogen and the self‑diffusion coefficients in representative isoreticular metal–organic frameworks (IRMOFs) with and without interpenetration. The results shed light on whether small pores created by interpenetration can lead to denser hydrogen packing and restricted diffusion – a key question for hydrogen storage applications.

## Approach
The conceptual method builds atomistic models of three IRMOFs (IRMOF‑1, IRMOF‑10, IRMOF‑13) from their published crystallographic data. The pore space is partitioned into distinct types (A, B for non‑interpenetrating frameworks; A′, B′, C, E for the interpenetrating one) based on the coordination environment. Classical molecular dynamics simulations are then conducted at 77 K using the UFF and DREIDING force fields, without any charge parametrisation. First, a series of short scans on IRMOF‑1 provides the optimum H₂–framework interaction energy for each force field. Next, longer production runs on all three frameworks are performed under four different hydrogen loadings (1 wt%, 2 wt%, 5 wt%, and a liquid‑density equivalent loading). Trajectories are analysed to extract the volumetric density of hydrogen molecules adsorbed within 3.1 Å of the framework surface, resolved per pore type, and to compute the self‑diffusion coefficient of hydrogen from the mean‑squared displacement via the Einstein relation. The workflow thus compares force fields on the reference system and then, using the selected force field, contrasts adsorption and transport behaviour between non‑interpenetrating and interpenetrating frameworks.

## Reproduction target
Produce all the following numerical quantities, saved in `/app/outputs/results.json` according to the output contract schema:

1. The optimum H₂–framework interaction energy (kcal/mol) for both UFF and DREIDING on IRMOF‑1 at 77 K.
2. For IRMOF‑1, the pore‑resolved volumetric density of adsorbed hydrogen (1/Å³ × 10⁻²) in the A and B pores, and the total density, at each loading (1 wt%, 2 wt%, 5 wt%, liquid‑density equivalent).
3. For IRMOF‑13, the same density values for the A′, B′, C, and E pores (D pore excluded) and the total density at each loading.
4. The self‑diffusion coefficient of hydrogen (Å²/ps) in IRMOF‑10 and IRMOF‑13 at each of the four loadings.

All numbers must be derived from molecular dynamics trajectories generated with open‑source simulation software and the UFF force field (except the DREIDING scan in step (1)).

## Assets

- IRMOF‑1 crystal structure (CIF): 10.1126/science.1067208
- IRMOF‑10 crystal structure (CIF): 10.1126/science.1067208
- IRMOF‑13 crystal structure (CIF): 10.1126/science.1067208
- Universal Force Field (UFF) parameters: https://github.com/numat/RASPA2
- DREIDING force field parameters: https://github.com/numat/RASPA2
- Open‑source molecular simulation package: https://github.com/numat/RASPA2

## Workflow steps

### Step 1: Model preparation and pore volume calculation
- Role: process
- Action: Build cleaned unit‑cell models of IRMOF‑1, IRMOF‑10 and IRMOF‑13 from their public CIFs (to P1 symmetry, remove disorder). Assign UFF/DREIDING atom types as needed. Using a 0.5 Å probe radius, compute the accessible free volume of each pore type (A and B for non‑interpenetrating frameworks; A′, B′, C and E for interpenetrating IRMOF‑13; D pore is excluded) and record the volumes for later density calculations.
- Evidence: `/app/outputs/model_pore_volumes.json`

### Step 2: Force‑field comparison MD on IRMOF‑1
- Role: process
- Action: For IRMOF‑1 only, perform two sets of molecular dynamics simulations at 77 K with a low hydrogen loading sufficient to probe the H₂–framework interaction: one using the UFF force field and one using DREIDING. Equilibrate each system and run production trajectories long enough to sample the interaction energy as a function of distance (e.g., via umbrella sampling or by scanning the H₂–framework distance). Save the trajectories.
- Evidence: `/app/outputs/irmof1_ff_trajectories_manifest.json`

### Step 3: Adsorption and diffusion MD for IRMOF‑1, IRMOF‑10, IRMOF‑13
- Role: process
- Action: For each of IRMOF‑1, IRMOF‑10 and IRMOF‑13, run UFF‑based MD simulations at 77 K under four hydrogen loadings: 1 wt%, 2 wt%, 5 wt%, and the liquid‑hydrogen density equivalent (number of H₂ molecules equal to total pore volume divided by 47.48 Å³, corresponding to 0.09 g/cm³). Use the UFF force field. For each system, equilibrate and then collect a production trajectory of at least 200 ps. Save the trajectories.
- Evidence: `/app/outputs/adsorption_md_trajectories_manifest.json`

### Step 4: Analysis and compilation of scored results
- Role: scored (load-bearing)
- Action: Analyze the trajectories from the previous two steps. (1) From the IRMOF‑1 force‑field trajectories, determine the optimum H₂–framework interaction energy for UFF and for DREIDING (in kcal/mol). (2) From the IRMOF‑1 and IRMOF‑13 adsorption trajectories, identify adsorbed H₂ molecules (within 3.1 Å of the framework surface) and compute the volumetric density (1/Å³ × 10⁻²) of adsorbed H₂ in each pore type (A and B for IRMOF‑1; A′, B′, C and E for IRMOF‑13) for every loading, as well as the total overall density. (3) From the IRMOF‑10 and IRMOF‑13 trajectories, compute the self‑diffusion coefficient (Å²/ps) of H₂ for every loading using the Einstein relation. Write all results into /app/outputs/results.json exactly following the output contract schema.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: JSON object with keys: interaction_energy_UFF (number, kcal/mol), interaction_energy_DREIDING (number, kcal/mol), adsorption_density_IRMOF1 (object with keys "1wt%", "2wt%", "5wt%", "liquid", each containing {A, B, Total}), adsorption_density_IRMOF13 (object with keys "1wt%", "2wt%", "5wt%", "liquid", each containing {A′, B′, C, E, Total}), self_diffusion_IRMOF10 (object with keys "1wt%", "2wt%", "5wt%", "liquid" each a number), self_diffusion_IRMOF13 (same). All densities in 1/Å³ × 10⁻², diffusion coefficients in Å²/ps.
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
- target_policy: reference_match
- description: Single JSON file containing all scored quantities: force‑field interaction energies, pore‑resolved adsorbed hydrogen densities, and H₂ self‑diffusion coefficients.
- schema:
  - `type`: object
  - `required`:
    - `interaction_energy_UFF`: number (kcal/mol)
    - `interaction_energy_DREIDING`: number (kcal/mol)
    - `adsorption_density_IRMOF1`: object with keys "1wt%", "2wt%", "5wt%", "liquid", each containing {A: number, B: number, Total: number}
    - `adsorption_density_IRMOF13`: object with keys "1wt%", "2wt%", "5wt%", "liquid", each containing {A′: number, B′: number, C: number, E: number, Total: number}
    - `self_diffusion_IRMOF10`: object with keys "1wt%", "2wt%", "5wt%", "liquid", each a number (Å²/ps)
    - `self_diffusion_IRMOF13`: object with keys "1wt%", "2wt%", "5wt%", "liquid", each a number (Å²/ps)
  - `units`:
    - `interaction_energy_UFF`: kcal/mol
    - `interaction_energy_DREIDING`: kcal/mol
    - `adsorption_densities`: 1/Å³ × 10⁻²
    - `self_diffusion_coefficients`: Å²/ps

Notes: All adsorption densities are per available pore volume. The liquid‑density equivalent loading corresponds to filling every pore volume with 0.09 g/cm³ liquid hydrogen (1 H₂ per 47.48 Å³). D pore is excluded from analysis. Tolerances and relative ordering checks are defined in the hidden checker and are not part of the public contract.

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
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "interaction_energy_UFF": "number (kcal/mol)",
          "interaction_energy_DREIDING": "number (kcal/mol)",
          "adsorption_density_IRMOF1": "object with keys \"1wt%\", \"2wt%\", \"5wt%\", \"liquid\", each containing {A: number, B: number, Total: number}",
          "adsorption_density_IRMOF13": "object with keys \"1wt%\", \"2wt%\", \"5wt%\", \"liquid\", each containing {A′: number, B′: number, C: number, E: number, Total: number}",
          "self_diffusion_IRMOF10": "object with keys \"1wt%\", \"2wt%\", \"5wt%\", \"liquid\", each a number (Å²/ps)",
          "self_diffusion_IRMOF13": "object with keys \"1wt%\", \"2wt%\", \"5wt%\", \"liquid\", each a number (Å²/ps)"
        },
        "units": {
          "interaction_energy_UFF": "kcal/mol",
          "interaction_energy_DREIDING": "kcal/mol",
          "adsorption_densities": "1/Å³ × 10⁻²",
          "self_diffusion_coefficients": "Å²/ps"
        }
      },
      "description": "Single JSON file containing all scored quantities: force‑field interaction energies, pore‑resolved adsorbed hydrogen densities, and H₂ self‑diffusion coefficients."
    }
  ],
  "notes": "All adsorption densities are per available pore volume. The liquid‑density equivalent loading corresponds to filling every pore volume with 0.09 g/cm³ liquid hydrogen (1 H₂ per 47.48 Å³). D pore is excluded from analysis. Tolerances and relative ordering checks are defined in the hidden checker and are not part of the public contract."
}
```

## How you are scored
A hidden verifier reads your `results.json` and checks that it contains all required fields in the correct units and structure. It then compares every numeric value (interaction energies, adsorption densities, diffusion coefficients) to a hidden reference that represents the physically expected outcome for this system. The comparison accounts for legitimate run‑to‑run and toolchain‑to‑toolchain spread by using domain‑appropriate tolerances; the better your computed numbers agree with the reference, the higher your score. The verifier also examines qualitative consistency, such as the relative ordering of densities across pore types, to confirm that the reported trends are physically plausible. The final reward is a weighted average of these checks, normalized to a single number between 0 and 1. Reporting the paper’s numbers without honestly executing the simulation workflow will be detected and will not earn credit.
