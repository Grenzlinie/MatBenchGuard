# Group-theoretical classification and photoirradiation simulation of a cyano-bridged Cu-Mo assembly

## Problem background
The cyano-bridged bimetallic assembly Cu₂[Mo(CN)₈]·xH₂O, with tetragonal I4/m symmetry and octacyanomolybdate ions in a square antiprism configuration, exhibits phototunable magnetism. Its paramagnetic ground state can be magnetized by blue-light irradiation and demagnetized by red/near-infrared light, but the underlying microscopic mechanism remains unclear. A fundamental question is which static density-wave phases can appear in this lattice and how photoexcitation can induce a macroscopic magnetization. In particular, does the polarization of the incident photons control whether the system magnetizes, and what is the dynamics of the photon energy absorption? Addressing these questions requires a group-theoretical analysis of possible ordered states and a time-dependent simulation of the electronic response to a laser pulse.

## Approach
We describe the electronic structure with a three-band extended Hubbard model on the I4/m lattice at 2/3 filling, featuring Cu 3d and Mo 4d orbitals. The Hamiltonian includes on-site Coulomb repulsions on copper and molybdenum sites, intersite Coulomb and exchange interactions between neighbouring Cu–Mo pairs, and pair-hopping terms. The symmetry group of the electronic system is the direct product of space, spin, and time-reversal groups (P×S×T). For the Γ point (Q=0) the relevant point group is C4h. To enumerate static density-wave states, we combine real irreducible representations of the point group with spin singlet/triplet (S⁰ and S¹) and time-reversal symmetric/antisymmetric (T⁰ and T¹) representations, and keep only one-dimensional representations that possess an axial isotropy subgroup. We then perform a self-consistent Hartree-Fock calculation to locate a paramagnetic (PM) ground state for a specific choice of on-site Coulomb repulsions, using the fixed intersite and exchange coupling values that define the Hamiltonian. With the PM ground-state wavefunction as initial state, we simulate photoirradiation by applying a pulsed laser field described by a Gaussian-enveloped vector potential with a given photon energy and polarization direction (either in the ab plane or along the c axis). The time evolution follows from a time-dependent Hartree-Fock scheme that incorporates Peierls phase factors on all hopping terms, Dzyaloshinskii-Moriya interactions of a specified magnitude lying in the ab plane, and a small external magnetic field. By solving the time-dependent Schrödinger equation via Trotter decomposition, we obtain the time-dependent wavefunction and compute the magnetization per unit cell (normalized by saturated magnetization) and the absorbed photon energy ΔE(t) for both polarization directions. Comparing the two polarization cases reveals whether a macroscopic magnetization appears and whether the energy absorption exhibits a characteristic double-stepped profile.

## Reproduction target
1) Perform the group-theoretical classification and produce a JSON array of the one-dimensional static density-wave states at the Γ point. Each entry must contain the irreducible representation (e.g., “ΓA_g⊗S⁰⊗T⁰”), the axial isotropy subgroup, and a descriptive abbreviation. The set should include both nonmagnetic and magnetic states; two-dimensional representations are excluded. 2) Using a time-dependent Hartree-Fock simulation of the PM ground state under a pulsed laser field, compute the magnetization dynamics and absorbed energy as functions of time for both ab-plane and c-axis polarizations. Output a CSV with columns: time (in units of ħ/t_CuMo), magnetization for a-axis polarization, magnetization for c-axis polarization, absorbed energy ΔE for a-axis polarization, and absorbed energy ΔE for c-axis polarization. The results should allow one to assess whether ab-plane polarization yields significant magnetization and a double-step energy absorption, while c-axis polarization does not.

## Assets

- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Group-theoretical classification of static density-wave states
- Role: scored
- Action: Perform group-theoretical analysis for the I4/m lattice. Determine irreducible representations of the direct product group P × S × T at the Γ point (Q=0), combine real spatial irreps with spin singlet/triplet and time-reversal representations to form static density-wave sectors. List all one-dimensional representations from ΓD(0)⊗S⁰⊗T⁰ and ΓD(0)⊗S¹⊗T¹, identify their axial isotropy subgroups and abbreviations. Discard two-dimensional irreps.
- Output file: `/app/outputs/symmetry_classification.json`
- Format: json
- Contract: Array of objects, each with keys: "irreducible_representation" (string), "axial_isotropy_subgroup" (string), "abbreviation" (string).
- Scoring: scored by hidden verifier

### Step 2: Hartree-Fock ground-state calculation for paramagnetic point
- Role: process
- Action: Implement the three-band extended Hubbard Hamiltonian for I4/m lattice at 2/3 filling. Fix parameters: ε_Cu−ε_Mo = 0.5 t_CuMo, V_CuMo = 0.8 t_CuMo, J_CuMo = J'_CuMo = 0.4 t_CuMo. Choose U_Cu and U_Mo that yield a paramagnetic (PM) ground state. Perform self-consistent Hartree-Fock iterations to obtain ground-state wavefunction, charge/spin densities, and band structure, confirming PM character. Save evidence of ground-state parameters and band energies at symmetry points.
- Evidence: `/app/outputs/ground_state_info.json`

### Step 3: Time-dependent Hartree-Fock simulation of photoirradiation
- Role: scored (load-bearing)
- Action: Starting from the PM ground-state wavefunction from Step 2, apply a pulsed laser field described by A(t)=e^{-γ²(t−t₀)²} A cos(ω t) with photon energy of 3.8 t_CuMo, γ=0.025 t_CuMo/ħ, t₀=100 ħ/t_CuMo, and amplitude A appropriate for a or c polarization. Include Peierls phase factors on hopping terms and Dzyaloshinskii-Moriya interactions of magnitude 0.05 t_CuMo in the ab plane. Add a small external field gμ_B H = 0.0002 t_CuMo. Evolve the wavefunction using a Trotter decomposition for a total duration covering the pulse and subsequent relaxation (≈400–600 ħ/t_CuMo). Record the magnetization per unit cell normalized by saturated magnetization and the absorbed energy ΔE(t) for both a-axis and c-axis polarizations.
- Output file: `/app/outputs/photomagnetism_dynamics.csv`
- Format: csv
- Contract: CSV with columns: t (simulation time in units of ħ/t_CuMo), M_ab (magnetization for a-axis polarization), M_c (magnetization for c-axis polarization), E_ab (absorbed energy ΔE for a-axis), E_c (absorbed energy for c-axis). All values are floats.
- Scoring: scored by hidden verifier

### Step 4: Instantaneous spectral function analysis
- Role: process
- Action: Using the time-evolved wavefunctions from Step 3, compute the one-particle spectral functions G_p(t;k,ω) and G_h(t;k,ω) for a few selected time slices and k-points to illustrate the hole creation dynamics and double-stepped absorption. Save results as evidence.
- Evidence: `/app/outputs/spectral_functions.npz`

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/symmetry_classification.json`
- `/app/outputs/photomagnetism_dynamics.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### symmetry_classification.json
- path: `/app/outputs/symmetry_classification.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: JSON array of the eight static density-wave states, each with irreducible representation, axial isotropy subgroup, and descriptive abbreviation as in Table 1 of the source.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `properties`:
      - `irreducible_representation`: string
      - `axial_isotropy_subgroup`: string
      - `abbreviation`: string
    - `required`: `irreducible_representation`, `axial_isotropy_subgroup`, `abbreviation`
  - `required`: `irreducible_representation`, `axial_isotropy_subgroup`, `abbreviation`

### photomagnetism_dynamics.csv
- path: `/app/outputs/photomagnetism_dynamics.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Time series of magnetization (normalized by saturated magnetization) and absorbed photon energy for a-axis and c-axis laser polarizations, demonstrating polarization-dependent photomagnetism and double-stepped absorption.
- schema:
  - `type`: table
  - `required_columns`: `t`, `M_ab`, `M_c`, `E_ab`, `E_c`
  - `units`:
    - `t`: ħ/t_CuMo
    - `M_ab`: normalized magnetization
    - `M_c`: normalized magnetization
    - `E_ab`: t_CuMo
    - `E_c`: t_CuMo

Notes: The PM ground-state evidence and spectral function file are not scored; only the classification list and the magnetization/absorption dynamics carry reward. Tolerances accommodate legitimate toolchain spread.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "symmetry_classification.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "irreducible_representation": "string",
            "axial_isotropy_subgroup": "string",
            "abbreviation": "string"
          },
          "required": [
            "irreducible_representation",
            "axial_isotropy_subgroup",
            "abbreviation"
          ]
        },
        "required": [
          "irreducible_representation",
          "axial_isotropy_subgroup",
          "abbreviation"
        ]
      },
      "description": "JSON array of the eight static density-wave states, each with irreducible representation, axial isotropy subgroup, and descriptive abbreviation as in Table 1 of the source."
    },
    {
      "file": "photomagnetism_dynamics.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "t",
          "M_ab",
          "M_c",
          "E_ab",
          "E_c"
        ],
        "units": {
          "t": "ħ/t_CuMo",
          "M_ab": "normalized magnetization",
          "M_c": "normalized magnetization",
          "E_ab": "t_CuMo",
          "E_c": "t_CuMo"
        }
      },
      "description": "Time series of magnetization (normalized by saturated magnetization) and absorbed photon energy for a-axis and c-axis laser polarizations, demonstrating polarization-dependent photomagnetism and double-stepped absorption."
    }
  ],
  "notes": "The PM ground-state evidence and spectral function file are not scored; only the classification list and the magnetization/absorption dynamics carry reward. Tolerances accommodate legitimate toolchain spread."
}
```

## How you are scored
A hidden verifier independently scores each of the scored output artifacts and combines the scores with predetermined weights to produce a final reward between 0 and 1. For the classification JSON, the verifier compares each entry's irreducible representation and abbreviation against a hidden reference derived from the source literature. For the dynamics CSV, the verifier recomputes several derived quantities: the maximum magnetization for each polarization and the presence/absence of a double-stepped absorption feature in the a-axis polarization (detected via numerical differentiation of the absorbed energy). It checks that the ab-plane polarization leads to a magnetization exceeding a hidden threshold while the c-axis polarization remains much smaller, and that the a-axis absorption rate shows two distinct peaks separated by a valley. Tolerances accommodate reasonable implementation differences. Reporting the paper's numbers is not enough; the workflow must produce the artifacts by genuine computation.
