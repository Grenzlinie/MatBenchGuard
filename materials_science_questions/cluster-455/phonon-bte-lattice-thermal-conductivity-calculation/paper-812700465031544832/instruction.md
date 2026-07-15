# Lattice thermal conductivity of Al-doped TiNiSn from DFT and a semi-empirical model

## Problem background
Half‑Heusler compounds such as TiNiSn are promising thermoelectric materials, but their high lattice thermal conductivity limits efficiency. Doping with Al and the presence of secondary‑phase inclusions both affect phonon transport. This task replicates a theoretical model that calculates lattice thermal conductivity from ab initio DFT‑derived elastic parameters and semi‑empirical formulas, to quantify the relative contributions of Al mass‑fluctuation scattering and secondary‑phase inclusion scattering.

## Approach
The approach combines three stages: (1) DFT total‑energy calculations on a series of volumes for pure TiNiSn and for a 96‑atom supercell of (Ti₀.₉₇Al₀.₀₃)NiSn to obtain energy‑volume curves; (2) fitting those curves to the Murnaghan equation of state to extract equilibrium lattice parameter, bulk modulus, and its pressure derivative, then computing Debye temperature and Grüneisen parameter via average sound velocity; (3) applying a semi‑empirical intrinsic lattice‑thermal‑conductivity formula that depends on average atomic mass, Debye temperature, volume per atom, and Grüneisen parameter, followed by a relaxation‑time model that incorporates phonon scattering by secondary‑phase inclusions with a fixed volume fraction (x = 0.05) and radius (R = 1 nm), to obtain the effective lattice thermal conductivity with inclusions. The calculations are carried out for both compositions at 300 K and 700 K, allowing a comparison of the effects of Al mass‑fluctuation scattering and inclusion scattering on the lattice thermal conductivity.

## Reproduction target
Produce the file `/app/outputs/lattice_thermal_conductivity_results.json` containing the DFT‑derived parameters (a₀, B₀, B₀′, Θ_D, γ, v_s) for both pure TiNiSn and (Ti₀.₉₇Al₀.₀₃)NiSn, and the eight lattice thermal conductivity values: intrinsic and with‑inclusions for each composition at 300 K and 700 K. All values must be in the units specified (Å, GPa, K, m/s, W m⁻¹ K⁻¹).

## Assets

- Open-source DFT code (e.g., Quantum ESPRESSO): https://www.quantum-espresso.org
- TiNiSn half-Heusler crystal structure: https://materialsproject.org/materials/mp-1869/
- Pseudopotential library: https://www.materialscloud.org/discover/sssp/table/precision

## Workflow steps

### Step 1: DFT total energy calculations vs volume
- Role: process
- Action: Perform self‑consistent total energy calculations with an open‑source DFT code for a series of scaled lattice constants (volume scaling) for (i) the pure TiNiSn primitive cell and (ii) a 96‑atom supercell of (Ti0.97Al0.03)NiSn with one Al substituted at a Ti site. Record the total energy E for each volume V in a structured table.
- Evidence: `/app/outputs/dft_ev_data.csv`

### Step 2: Equation‑of‑state fitting and derived parameters
- Role: process
- Action: Fit the DFT E(V) data to the Murnaghan equation of state to extract equilibrium lattice parameter a₀, bulk modulus B₀, and pressure derivative B₀′ for both compositions. Compute Debye temperature Θ_D via average sound velocity (using G = 0.59 B and the average atomic mass) and Grüneisen parameter γ = (1/2)B₀′ − 1/6. Save all DFT‑derived parameters (a₀, B₀, B₀′, Θ_D, γ, average sound velocity v_s) in a JSON file.
- Evidence: `/app/outputs/dft_parameters.json`

### Step 3: Compute lattice thermal conductivities with and without inclusions
- Role: scored (load-bearing)
- Action: Read the DFT‑derived parameters. For each composition compute intrinsic lattice thermal conductivity κ_l_intrinsic(T) at T = 300 K and 700 K using the semi‑empirical Morelli‑Slack formula (average atomic mass M̄, volume per atom δ, n=3, prefactor A as defined in the literature). Then apply an inclusion scattering model with input values: inclusion volume fraction x = 0.05 and radius R = 1 nm; use heat capacity C = 3R per atom and the relaxation‑time approach to obtain κ_l_with_inclusions(T). Report all eight κ_l values together with the DFT parameters in a single JSON file.
- Output file: `/app/outputs/lattice_thermal_conductivity_results.json`
- Format: json
- Contract: A JSON object with two top‑level keys: "DFT_parameters" (object with composition names as keys, each containing a0_angstrom, B0_GPa, B0_prime, Theta_D_K, gamma, vs_m_per_s) and "kappa_l_values" (object with eight numeric fields: TiNiSn_intrinsic_300K, TiNiSn_intrinsic_700K, TiNiSn_with_inclusions_300K, TiNiSn_with_inclusions_700K, Ti0.97Al0.03NiSn_intrinsic_300K, Ti0.97Al0.03NiSn_intrinsic_700K, Ti0.97Al0.03NiSn_with_inclusions_300K, Ti0.97Al0.03NiSn_with_inclusions_700K). All numeric values are floats.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/lattice_thermal_conductivity_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### lattice_thermal_conductivity_results.json
- path: `/app/outputs/lattice_thermal_conductivity_results.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Lattice thermal conductivity results from DFT‑based semi‑empirical model. The hidden checker recomputes κ_l_values from the reported DFT_parameters to verify self‑consistency, then compares the recomputed values to hidden gold reference values and checks structural ordering (κ_l_with_inclusions < κ_l_intrinsic, and larger reduction for the Al‑doped composition).
- schema:
  - `type`: object
  - `required`:
    - `DFT_parameters`: object with sub‑objects TiNiSn and Ti0.97Al0.03NiSn
    - `kappa_l_values`: object
  - `items`:
    - `a0_angstrom`: number
    - `B0_GPa`: number
    - `B0_prime`: number
    - `Theta_D_K`: number
    - `gamma`: number
    - `vs_m_per_s`: number
    - `TiNiSn_intrinsic_300K`: number
    - `TiNiSn_intrinsic_700K`: number
    - `TiNiSn_with_inclusions_300K`: number
    - `TiNiSn_with_inclusions_700K`: number
    - `Ti0.97Al0.03NiSn_intrinsic_300K`: number
    - `Ti0.97Al0.03NiSn_intrinsic_700K`: number
    - `Ti0.97Al0.03NiSn_with_inclusions_300K`: number
    - `Ti0.97Al0.03NiSn_with_inclusions_700K`: number
  - `units`:
    - `a0_angstrom`: Å
    - `B0_GPa`: GPa
    - `Thermodynamic parameters`: K for Θ_D, dimensionless for γ, m/s for v_s
    - `kappa_l`: W m⁻¹ K⁻¹

Notes: The checker will use the same semi‑empirical formulas and the agent‑supplied DFT parameters to recompute the κ_l values. Differences due to numerical rounding are absorbed by a generous tolerance. The structural ordering (trend) carries part of the reward.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "lattice_thermal_conductivity_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": {
          "DFT_parameters": "object with sub‑objects TiNiSn and Ti0.97Al0.03NiSn",
          "kappa_l_values": "object"
        },
        "items": {
          "a0_angstrom": "number",
          "B0_GPa": "number",
          "B0_prime": "number",
          "Theta_D_K": "number",
          "gamma": "number",
          "vs_m_per_s": "number",
          "TiNiSn_intrinsic_300K": "number",
          "TiNiSn_intrinsic_700K": "number",
          "TiNiSn_with_inclusions_300K": "number",
          "TiNiSn_with_inclusions_700K": "number",
          "Ti0.97Al0.03NiSn_intrinsic_300K": "number",
          "Ti0.97Al0.03NiSn_intrinsic_700K": "number",
          "Ti0.97Al0.03NiSn_with_inclusions_300K": "number",
          "Ti0.97Al0.03NiSn_with_inclusions_700K": "number"
        },
        "units": {
          "a0_angstrom": "Å",
          "B0_GPa": "GPa",
          "Thermodynamic parameters": "K for Θ_D, dimensionless for γ, m/s for v_s",
          "kappa_l": "W m⁻¹ K⁻¹"
        }
      },
      "description": "Lattice thermal conductivity results from DFT‑based semi‑empirical model. The hidden checker recomputes κ_l_values from the reported DFT_parameters to verify self‑consistency, then compares the recomputed values to hidden gold reference values and checks structural ordering (κ_l_with_inclusions < κ_l_intrinsic, and larger reduction for the Al‑doped composition)."
    }
  ],
  "notes": "The checker will use the same semi‑empirical formulas and the agent‑supplied DFT parameters to recompute the κ_l values. Differences due to numerical rounding are absorbed by a generous tolerance. The structural ordering (trend) carries part of the reward."
}
```

## How you are scored
A hidden verifier independently evaluates each workflow stage's output artifact. The final reward is a weighted combination of the scores for each stage. The verifier reads the DFT_parameters from your submitted JSON, recomputes the eight κ_l values using the same formulas, and compares them to hidden reference values with appropriate tolerances. It also checks that the structural ordering among the reported κ_l values is correct (e.g., that inclusion scattering reduces κ_l, and that the reduction due to Al doping plus inclusions follows a specific pattern). Reporting the paper's numbers without actually executing the DFT and computation pipeline will not succeed, because the hidden verifier checks both self‑consistency and agreement with independent reference values. Each stage’s artifact must be present and correctly formatted.
