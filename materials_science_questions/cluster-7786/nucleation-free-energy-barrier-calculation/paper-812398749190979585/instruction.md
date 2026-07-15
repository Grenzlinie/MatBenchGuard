# Nucleation Free-Energy Barrier Calculation

## Problem background
Heterogeneous nucleation of martensite in iron-nickel alloys is studied through elasticity theory. The model considers an embryo (a thin oblate ellipsoid containing a mixture of two twin-related Bain variants) attached to a screw dislocation, which may represent the stress field of a dislocation pile-up. Combining chemical free energy, elastic self-energy, and dislocation–embryo interaction energy yields a total free energy whose barrier determines whether nucleation can occur by thermal fluctuations. The focus is on quantifying the nucleation barrier at low temperature and estimating how many dislocations are needed to make the barrier surmountable for realistic interfacial energies.

## Approach
The thermodynamic model expresses the total free energy of an embryo containing n atoms as F_T = A n + B n^{2/3}, where A includes the chemical driving force and the elastic self-energy coefficient of the oblate embryo, and B incorporates the interfacial energy and the effective negative surface energy from the dislocation–embryo interaction. The elastic energies are computed using a Fourier-defect formalism: the embryo is filled with transformation defects having the averaged Bain strain of two variants, and the dislocation is represented by a half-plane of dislocation defects. For a range of embryo shapes (axial ratio t), variant fraction f, and orientation angles, the elastic self-energy coefficient E0_BB is minimized numerically. The interaction energy with a screw dislocation is then computed for each shape, yielding an effective interfacial energy γ_I(t). The chemical free energy of the Fe–29Ni system is given by a temperature-dependent expression. With γ = 23 erg/cm² and a single dislocation (N_B=1), the total free energy is assembled and the critical nucleus (size n*, axial ratio t*) that maximizes the barrier is found. The barrier height ΔF* is extracted in units of k_B T. Finally, using the critical axial ratio t*, the effective negative surface energy γ_I(t*) is used to estimate the number of dislocations N_B needed when the true interfacial energy is raised to 200 erg/cm².

## Reproduction target
Compute the free energy barrier for heterogeneous nucleation in Fe–29Ni at 250 K, using the elastic constants from Suezawa and Cook (1978) and the chemical free energy expression provided in the paper’s method. Under the condition of a single dislocation (N_B=1) and interfacial energy γ = 23 erg/cm², determine the critical embryo shape and size, and report the barrier ΔF* in units of k_B T. Then, from the same critical shape, compute the effective negative surface energy γ_I and estimate the number of dislocations N_B required when the interfacial energy is set to a realistic value of 200 erg/cm². The output must include the barrier height, the N_B estimate, and the critical axial ratio.

## Assets

- Elastic constants and Bain strains for Fe-29Ni from Suezawa and Cook (1978) Acta Metall. 26, 1205: 10.1016/0001-6160(78)90066-6

## Workflow steps

### Step 1: Compute elastic self-energy coefficient E0_BB
- Role: process
- Action: Using the published elastic constants and Bain strains for Fe-29Ni, implement the Fourier-defect formalism for the elastic self-energy of an oblate ellipsoidal transformation defect. For each axial ratio t and variant fraction f, minimize the orientation-dependent coefficient E0_BB(t, f, θ, φ) over θ and φ, obtaining E0_BB_min(t, f).
- Evidence: `/app/outputs/self_energy_minima.csv`

### Step 2: Compute dislocation-embryo interaction and effective interfacial energy γ_I
- Role: process
- Action: Implement the Fourier-defect formalism for the interaction between a screw dislocation (half-plane defect representation) and the embryo. Compute the interaction coefficient E0_BD and the effective interfacial energy γ_I(t) = f E0_BD / (s(t) ā²) for a range of axial ratios, using the same parameters and Debye cut-off as in step 1.
- Evidence: `/app/outputs/effective_gamma_I.csv`

### Step 3: Compute nucleation barrier and required dislocation count
- Role: scored (load-bearing)
- Action: Assemble the total free energy F_T = A n + B n^(2/3) with A = g + E0_BB_min(t) and B = s(t) ā² (γ + N_B γ_I(t)). Use the chemical free energy expression for Fe-29Ni at 250 K, set γ = 23 erg cm⁻² and N_B=1. Find the critical axial ratio (t*) and critical size (n*) that maximize F_T beyond the metastable minimum, obtaining the free-energy barrier ΔF*. Convert ΔF* to units of k_B T. Then, using t* and γ_I(t*), compute the number of dislocations required for nucleation (N_B) for γ=200 erg cm⁻² via N_B = –γ / γ_I(t*). Write the results to nucleation_results.json.
- Output file: `/app/outputs/nucleation_results.json`
- Format: json
- Contract: Object with keys: barrier_at_250K (float, in units of k_B T), NB_estimate (float, dimensionless), critical_axial_ratio (float, dimensionless).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/nucleation_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### nucleation_results.json
- path: `/app/outputs/nucleation_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Contains the computed free-energy barrier for heterogeneous nucleation at 250 K (should exceed 50 k_B T), the estimated number of dislocations required for realistic interfacial energy (should be ≈10), and the critical axial ratio of the embryo. The checker verifies barrier > 50 k_B T, NB within 20% of 10, and critical axial ratio in [15, 25].
- schema:
  - `type`: object
  - `required`:
    - `barrier_at_250K`: number (k_B T)
    - `NB_estimate`: number
    - `critical_axial_ratio`: number

Notes: The only scored artifact is nucleation_results.json. The checker compares the barrier and NB estimate to the paper's reported thresholds and tolerance. The critical axial ratio is used as a consistency check. No hidden holdout dataset is needed; the gold values are paper-reported thresholds.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "nucleation_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "barrier_at_250K": "number (k_B T)",
          "NB_estimate": "number",
          "critical_axial_ratio": "number"
        }
      },
      "description": "Contains the computed free-energy barrier for heterogeneous nucleation at 250 K (should exceed 50 k_B T), the estimated number of dislocations required for realistic interfacial energy (should be ≈10), and the critical axial ratio of the embryo. The checker verifies barrier > 50 k_B T, NB within 20% of 10, and critical axial ratio in [15, 25]."
    }
  ],
  "notes": "The only scored artifact is nucleation_results.json. The checker compares the barrier and NB estimate to the paper's reported thresholds and tolerance. The critical axial ratio is used as a consistency check. No hidden holdout dataset is needed; the gold values are paper-reported thresholds."
}
```

## How you are scored
A hidden verifier reads the output file `nucleation_results.json`. It checks the reported free energy barrier against a threshold derived from the paper’s criterion (the barrier must be large enough to preclude thermal activation at low temperature). It compares the estimated number of dislocations N_B to a reference value with a tolerance that accounts for differences in numerical implementation. The critical axial ratio is also checked for consistency with the expected shape regime. Each check contributes a weighted fraction to the final reward; the barrier and N_B estimate carry the largest weight. The reported numbers are compared directly to hidden reference values, so honest computation is required — the verifier does not merely validate the format.
