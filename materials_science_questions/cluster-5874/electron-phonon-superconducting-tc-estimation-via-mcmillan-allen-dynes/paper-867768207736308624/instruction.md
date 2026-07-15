# Computation of Fluorine Hopfield Parameter in H3F via Gaspari-Gyorffy Method

## Problem background
Hydrogen-rich compounds under extreme pressure have emerged as promising candidates for high-temperature superconductivity. Following the discovery of superconductivity near 200 K in compressed H₃S, attention has turned to the H₃F system to explore whether strong electron-phonon coupling can be achieved at moderate pressures. A central quantity in assessing the electron-phonon coupling is the Hopfield parameter η, which captures the electronic contribution to the coupling strength. In this task you will compute the fluorine component of the Hopfield parameter (η_F) for cubic H₃F, and its dominant pd-channel contribution, using first-principles electronic-structure methods. A large η_F on the fluorine site would signal a strong pairing interaction and the potential for high superconducting transition temperatures.

## Approach
The reproduction follows an all-electron LAPW (linearized augmented plane wave) method, which provides the band structure, densities of states, and scattering phase shifts required by the Gaspari-Gyorffy (GG) theory. You will set up the Im-3m crystal structure of H₃F at two lattice constants (5.4 Bohr and 5.6 Bohr) and perform self-consistent LAPW calculations using the Hedin-Lundqvist exchange-correlation functional. From the converged potentials, you will extract the total and angular-momentum-decomposed densities of states at the Fermi level, the scattering phase shifts δ_l for each atom, and the free-scatterer density of states N_l^(1). These ingredients are then inserted into the GG formula, which expresses the Hopfield parameter η for each atomic species as a sum over angular-momentum channels:

η_j = (1 / N(E_f)) ∑_{l=0}^{2} 2(l+1) sin²(δ_l^j − δ_{l+1}^j) v_l^j v_{l+1}^j

where v_l^j = N_l^j(E_f) / N_l^{j(1)}. The fluorine η_F is decomposed into pd (l=1→l=2) and other contributions. You will compute η_F and its pd-channel contribution for both lattice constants and output the results as a structured JSON file.

## Reproduction target
Your goal is to produce a single scored artifact: the file hopfield_parameters.json containing the computed fluorine Hopfield parameter η_F (in eV/Å²) and its pd-channel contribution for H₃F in the Im-3m structure at lattice constants 5.4 Bohr and 5.6 Bohr. The calculations must be performed from scratch using the LAPW workflow (Elk is the recommended open-source code). The output file must follow the contract described below, with keys “5.4” and “5.6”. You are not required to compute superconducting T_c, elastic constants, or compare to H₃S; these aspects are outside the scope of this reproduction.

## Assets

- Elk LAPW code: https://elk.sourceforge.io/

## Workflow steps

### Step 1: LAPW electronic structure calculations
- Role: process
- Action: Set up the Im-3m crystal structure of H3F and perform self-consistent all-electron LAPW calculations using the Elk code at lattice constants 5.4 Bohr and 5.6 Bohr, with the Hedin-Lundqvist exchange-correlation functional and a dense k-point grid.
- Evidence: `/app/outputs/lapw_output.log`

### Step 2: Extract DOS, phase shifts, and free-scatterer DOS
- Role: process
- Action: Post-process the LAPW results to compute the total density of states N(Ef), angular-momentum-decomposed partial DOS, scattering phase shifts δ_l for each atomic species, and the free-scatterer DOS N_l^(1).
- Evidence: `/app/outputs/dos_phase_data.json`

### Step 3: Compute Hopfield parameters
- Role: scored (load-bearing)
- Action: Apply the Gaspari-Gyorffy formula to compute the fluorine Hopfield parameter η_F and its pd-channel contribution for both lattice constants. Output the results as a JSON file.
- Output file: `/app/outputs/hopfield_parameters.json`
- Format: json
- Contract: JSON object with keys "5.4" and "5.6". Each value: {"lattice_constant_bohr": float, "pressure_gpa": float or null, "eta_F_ev_per_ang2": float, "eta_pd_contribution_ev_per_ang2": float}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/hopfield_parameters.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### hopfield_parameters.json
- path: `/app/outputs/hopfield_parameters.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Computed fluorine Hopfield parameter and pd-channel contribution for H3F at lattice constants 5.4 Bohr and 5.6 Bohr. The values will be compared to paper-reported results within a tolerance; structural consistency (pd dominance and pressure trend) is also verified.
- schema:
  - `type`: object
  - `top_level_keys`:
    - `5.4`:
      - `type`: object
      - `required`: `lattice_constant_bohr`, `eta_F_ev_per_ang2`, `eta_pd_contribution_ev_per_ang2`
      - `fields`:
        - `lattice_constant_bohr`: float
        - `pressure_gpa`: float or null
        - `eta_F_ev_per_ang2`: float
        - `eta_pd_contribution_ev_per_ang2`: float
    - `5.6`:
      - `type`: object
      - `required`: `lattice_constant_bohr`, `eta_F_ev_per_ang2`, `eta_pd_contribution_ev_per_ang2`
      - `fields`:
        - `lattice_constant_bohr`: float
        - `pressure_gpa`: float or null
        - `eta_F_ev_per_ang2`: float
        - `eta_pd_contribution_ev_per_ang2`: float

Notes: The Hydrogen Hopfield parameter is computed but not scored; only the fluorine component is the primary target. Only the two LAPW runs and the GG formula post-processing are required; EOS fitting is skipped (pressure may be reported as null or deduced).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "hopfield_parameters.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "top_level_keys": {
          "5.4": {
            "type": "object",
            "required": [
              "lattice_constant_bohr",
              "eta_F_ev_per_ang2",
              "eta_pd_contribution_ev_per_ang2"
            ],
            "fields": {
              "lattice_constant_bohr": "float",
              "pressure_gpa": "float or null",
              "eta_F_ev_per_ang2": "float",
              "eta_pd_contribution_ev_per_ang2": "float"
            }
          },
          "5.6": {
            "type": "object",
            "required": [
              "lattice_constant_bohr",
              "eta_F_ev_per_ang2",
              "eta_pd_contribution_ev_per_ang2"
            ],
            "fields": {
              "lattice_constant_bohr": "float",
              "pressure_gpa": "float or null",
              "eta_F_ev_per_ang2": "float",
              "eta_pd_contribution_ev_per_ang2": "float"
            }
          }
        }
      },
      "description": "Computed fluorine Hopfield parameter and pd-channel contribution for H3F at lattice constants 5.4 Bohr and 5.6 Bohr. The values will be compared to paper-reported results within a tolerance; structural consistency (pd dominance and pressure trend) is also verified."
    }
  ],
  "notes": "The Hydrogen Hopfield parameter is computed but not scored; only the fluorine component is the primary target. Only the two LAPW runs and the GG formula post-processing are required; EOS fitting is skipped (pressure may be reported as null or deduced)."
}
```

## How you are scored
A hidden verifier will inspect hopfield_parameters.json after your run. It compares the reported η_F and pd-channel contribution at each lattice constant to hidden reference values with appropriate tolerances, checks that the pd channel is the dominant contribution (≥60% of total η), and verifies that η_F at the smaller lattice constant (higher pressure) is larger than at the larger lattice constant. The final reward is a weighted combination of these checks. Merely quoting the paper’s numbers will not pass; the verifier expects results that are consistent with a genuine execution of the prescribed LAPW + GG post-processing pipeline.
