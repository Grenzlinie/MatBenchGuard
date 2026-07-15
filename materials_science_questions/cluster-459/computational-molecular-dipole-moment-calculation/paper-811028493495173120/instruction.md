# Halogen Chemisorption on Mercury Cluster Model

## Problem background
The chemisorption of halogen atoms (Cl, Br, I) on a mercury surface is an important model system for understanding the nature of adsorbate–metal bonding. This task investigates whether the bond is ionic or covalent by performing ab initio quantum-chemical calculations on a finite cluster model of the mercury surface. A central mercury atom plus its six nearest neighbours form an Hg₇ cluster, onto which a halogen atom is adsorbed at the atop site. The interaction is studied in two distinct electronic states: one formally neutral (²A₁) and one formally ionic (²A₂). The goal is to compute structural parameters, dipole moment curves, and the response to an external electric field — quantities that together characterize the ionicity of the chemisorption bond.

## Approach
The reproduction uses restricted open‑shell Hartree–Fock (ROHF) calculations with non‑empirical Hay–Wadt pseudopotentials to replace core electrons. The basis sets are contracted as (3s3p3d/2s1p2d) for Hg and (4s4p1d/3s3p1d) for the halogens. First, the Hg₇ cluster is built at the experimental Hg–Hg distance and the electronic ground state of the bare cluster is identified by comparing different closed‑shell configurations. Reference energies for the isolated halogen atoms are computed at the same level. Then, for each halogen and each electronic state, total energies E(z) and dipole moments μ(z) are calculated as functions of the adsorbate–surface distance z. The potential energy curves are fitted to extract the equilibrium distance (rₑ), perpendicular vibrational frequency (νₑ), and binding energy (BE). The dipole moment is expanded around equilibrium as μ = M₀ + M₁(z−rₑ) + M₂(z−rₑ)² to obtain the coefficients M₀, M₁, M₂. Finally, uniform external electric fields of +0.01 a.u. and −0.01 a.u. are added to the Hamiltonian and the equilibrium distance is re‑optimized, yielding field‑induced shifts. All raw simulation data are saved in a single JSON file from which the final parameters are derived.

## Reproduction target
For each of the three halogens (Cl, Br, I) and each of the two electronic states (²A₁, ²A₂), compute and report the following quantities: (1) equilibrium distance rₑ (Å), perpendicular vibrational frequency νₑ (cm⁻¹), and binding energy BE (kJ mol⁻¹); (2) dipole moment expansion coefficients M₀ (a.u.), M₁ (a.u.), M₂ (a.u.) at the equilibrium distance; (3) the change in rₑ (Å) when a uniform external electric field of +0.01 a.u. or −0.01 a.u. is applied. The raw potential energy curves, dipole moments, and field‑optimised distances must be stored in simulation_raw_results.json as specified in the workflow; the final structural parameters, dipole coefficients, and field shifts are recomputed from that file by the verifier.

## Assets

- PySCF (or equivalent quantum chemistry code with ROHF): https://pyscf.org
- Hay–Wadt pseudopotential parameters and basis sets: 10.1063/1.448800
- Experimental mercury lattice geometry

## Workflow steps

### Step 1: Build the Hg7 cluster model and define basis sets
- Role: process
- Action: Construct the finite cluster model consisting of a central Hg atom with its six nearest neighbours in the first layer, using the experimental Hg–Hg distance. Set up the Hay–Wadt pseudopotentials and basis sets for Hg and each halogen (Cl, Br, I) according to the paper’s specification.
- Evidence: `/app/outputs/cluster_setup_log.txt`

### Step 2: Reference calculations for isolated fragments
- Role: process
- Action: Perform ROHF calculations for the bare Hg7 cluster in different closed-shell electronic configurations to determine the correct ground state (lowest total energy). Compute the total energy of the isolated halogen atoms (Cl, Br, I) at the same level.
- Evidence: `/app/outputs/reference_energies.csv`

### Step 3: Supersystem potential energy curves and response to electric fields
- Role: scored (load-bearing)
- Action: For each combination of halogen (Cl, Br, I) and electronic state (²A₁, ²A₂): compute the ROHF total energy E(z) and dipole moment μ(z) for a series of adsorbate–surface distances z, and re-optimize the equilibrium distance after adding uniform external electric fields of +0.01 and −0.01 a.u. Save all raw data—E(z), μ(z) arrays, and field-optimized distances—to simulation_raw_results.json.
- Output file: `/app/outputs/simulation_raw_results.json`
- Format: json
- Contract: Top-level keys: halogen (string), state (string); each contains arrays: z (float[]), E (float[]), mu (float[]), and field_optimized_re for F=+0.01 and F=-0.01 (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/simulation_raw_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### simulation_raw_results.json
- path: `/app/outputs/simulation_raw_results.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Raw potential energy curves, dipole moments, and field-optimised distances for all six adsorbate–cluster systems.
- schema:
  - `type`: object
  - `description`: Top-level keys are halogen (Cl, Br, I) and electronic state (2A1, 2A2); each value is an object with keys: z (float array), E (float array), mu (float array), field_optimized_re (object with keys F_plus_0.01 and F_minus_0.01 as floats).

Notes: The checker recomputes the structural parameters (re, nu_e, BE), dipole coefficients (M0, M1, M2), and field shifts from this raw file and compares them to hidden paper gold using tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "simulation_raw_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "description": "Top-level keys are halogen (Cl, Br, I) and electronic state (2A1, 2A2); each value is an object with keys: z (float array), E (float array), mu (float array), field_optimized_re (object with keys F_plus_0.01 and F_minus_0.01 as floats)."
      },
      "description": "Raw potential energy curves, dipole moments, and field-optimised distances for all six adsorbate–cluster systems."
    }
  ],
  "notes": "The checker recomputes the structural parameters (re, nu_e, BE), dipole coefficients (M0, M1, M2), and field shifts from this raw file and compares them to hidden paper gold using tolerances."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier. It reads your simulation_raw_results.json, recomputes the equilibrium distances, vibrational frequencies, binding energies, dipole moment coefficients, and field‑induced shifts, and compares each value to a hidden reference. The verifier also checks that key structural relationships (such as the ordering of rₑ and νₑ between the two electronic states and the sign of the field‑induced shifts) are satisfied. Each workflow stage contributes to the total reward; the load‑bearing scored stage (Step 3, the supersystem calculations) carries the largest weight. You must produce the required raw simulation data — simply reporting numbers is not sufficient.
