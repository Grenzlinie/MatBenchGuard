# Computational modelling of spin-forbidden CO recombination with iron tetracarbonyl

## Problem background
The gas-phase recombination of carbon monoxide with the unsaturated iron tetracarbonyl fragment, [Fe(CO)₄], to form [Fe(CO)₅] is a fundamental ligand addition reaction. Unlike the analogous spin-allowed recombination with [Fe(CO)₃], this reaction is spin-forbidden because the ground state of the [Fe(CO)₄] reactant is a triplet while the product [Fe(CO)₅] is a singlet. The measured rate is much slower than the gas-collision limit, suggesting both a barrier in the potential energy surfaces and a need for non-adiabatic transitions (surface hopping) between spin states. Accurately predicting the rate from first principles therefore requires reliable electronic structure calculations to calibrate the key energetic quantities and a proper treatment of the spin crossing. In this task you will compute the singlet–triplet energy splitting and bond dissociation energy, locate and characterize the minimum energy crossing point (MECP) between the singlet and triplet surfaces, and apply non-adiabatic transition state theory (NA-TST) to obtain the bimolecular rate coefficient at room temperature – all using open-source quantum chemistry software.

## Approach
The overall workflow uses a hierarchy of electronic structure methods, progressing from density functional theory (DFT) to coupled-cluster singles, doubles, and perturbative triples (CCSD(T)). First, geometry optimizations and harmonic vibrational frequency calculations are performed for all species (Fe(CO)₅, singlet and triplet Fe(CO)₄, and CO) at the DFT level with a modified B3PW91 functional containing 15% exact exchange and a triple-zeta basis set (Ahlrichs TZV, augmented with diffuse p and f functions on Fe and d polarization on C and O). These provide equilibrium structures and zero-point energy (ZPE) corrections. Next, single-point CCSD(T) energies are computed at the optimized geometries using a large VQZ-VDZ basis, starting from molecular orbitals obtained by a BP86 DFT calculation. The electronic energies and ZPE corrections are combined to yield the singlet–triplet energy splitting ΔE(1,3) and the bond dissociation energy referenced to the triplet fragments (BDE(3)).

Separately, the minimum energy crossing point (MECP) between the singlet and triplet surfaces of the Fe(CO)₄ + CO system is located using a gradient-based MECP optimization algorithm at the same DFT level. The search targets a Cₛ-symmetric structure with a side-on approach of the incoming CO. At the converged MECP, the vibrational frequencies within the crossing seam are computed, and the dynamical parameters needed for NA-TST are extracted: the effective reduced mass μ_H for motion orthogonal to the seam, the norms of the gradient difference ΔF and the geometric mean gradient F on the two surfaces, and the root-mean-square spin–orbit coupling matrix element V₁₂ between the singlet and triplet states, obtained from a CASSCF(12,12)/VDZ calculation.

Finally, the reactant partition functions (rotational constants, vibrational frequencies, electronic degeneracies) and the full set of MECP properties are used to compute the bimolecular rate coefficient k(T) at T = 300 K within the framework of non-adiabatic transition state theory. Two expressions for the surface-hopping probability are evaluated: the Landau–Zener formula and the WKB-based (Delos) formula.

## Reproduction target
You must produce three scored artifacts that together capture the main quantitative findings of the study:

1. **Energetics** (`step_01_energetics.json`): the singlet–triplet electronic energy splitting ΔE(1,3) and the bond dissociation energy BDE(3) of [Fe(CO)₅] with respect to the ground-state triplet fragments, both without and with zero-point energy correction. All values must be in kcal mol⁻¹ and correspond to the CCSD(T)/VQZ‑VDZ//B3PW91* level.

2. **MECP properties** (`step_02_MECP.json`): the Cartesian coordinates (geometry) of the Cₛ MECP optimized at the B3PW91*/TZV level, its energy relative to the separated triplet Fe(CO)₄ and CO (without ZPE, in kcal mol⁻¹), the spin–orbit coupling V₁₂ (cm⁻¹), and the dynamical parameters ΔF, F, and μ_H required for the rate calculation.

3. **Rate coefficient** (`step_03_rate_coefficient.json`): the bimolecular rate coefficient k(T) at T = 300 K, in units of cm³ molecule⁻¹ s⁻¹, computed via NA-TST using both the Landau–Zener and the WKB (Delos) surface-hopping probabilities.

## Assets

- PySCF: https://github.com/pyscf/pyscf
- Basis Set Exchange: https://www.basissetexchange.org/

## Workflow steps

### Step 1: Geometry optimization and frequency analysis at B3PW91*/TZV
- Role: process
- Action: Construct initial structures for Fe(CO)₅ (D₃h), singlet Fe(CO)₄ (C₂v), triplet Fe(CO)₄ (C₂v), and CO. Perform geometry optimization and harmonic vibrational frequency calculation using the B3PW91* functional (modified B3PW91 with 15% exact exchange) and the Ahlrichs TZV basis set (augmented with diffuse p and f functions on Fe and d polarization on C and O). Extract optimized geometries, harmonic vibrational frequencies, and zero‑point energy (ZPE) corrections.
- Evidence: `/app/outputs/geom_freq_log.txt`

### Step 2: CCSD(T) single-point energies with BP86 orbitals
- Role: process
- Action: For each species (Fe(CO)₅ singlet, Fe(CO)₄ singlet, Fe(CO)₄ triplet, CO) using the B3PW91*/TZV optimized geometry, first perform a DFT calculation with the BP86 functional to obtain molecular orbitals, then carry out single‑point CCSD(T) calculations with the VQZ‑VDZ basis set (large Fe [6s5p6d3f2g1h] basis, cc‑pVDZ on C and O with additional polarization). Record the total electronic energies.
- Evidence: `/app/outputs/ccsdt_raw_energies.json`

### Step 3: Compute ZPE-corrected ΔE(1,3) and BDE(3)
- Role: scored
- Action: From the CCSD(T) electronic energies and the B3PW91* ZPE corrections, calculate the singlet–triplet electronic energy splitting ΔE(1,3) = E(singlet Fe(CO)₄) – E(triplet Fe(CO)₄), the bond dissociation energy referenced to triplet fragments BDE(3) = E(triplet Fe(CO)₄) + E(CO) – E(Fe(CO)₅), and the corresponding values after adding ZPE corrections. Write all four numbers to the output file.
- Output file: `/app/outputs/step_01_energetics.json`
- Format: json
- Contract: {"deltaE13_electronic_kcalmol": float, "deltaE13_withZPE_kcalmol": float, "BDE3_electronic_kcalmol": float, "BDE3_withZPE_kcalmol": float}
- Scoring: scored by hidden verifier

### Step 4: Locate and characterize the Cₛ MECP
- Role: process
- Action: Using the B3PW91*/TZV method, employ a gradient‑based algorithm to locate the minimum energy crossing point (MECP) between the singlet and triplet surfaces of the Fe(CO)₄ + CO system, starting from a geometry near the expected Cₛ side‑on approach. At the converged MECP, compute the vibrational frequencies within the crossing seam, the effective reduced mass μ_H for the direction orthogonal to the seam, the norms of the gradients ΔF and F on the two surfaces, and run a CASSCF(12,12)/VDZ calculation to obtain the root‑mean‑square spin‑orbit coupling V₁₂ between singlet and triplet states. Store all raw data.
- Evidence: `/app/outputs/mecp_full_properties.json`

### Step 5: Produce MECP summary and spin‑orbit coupling
- Role: scored (load-bearing)
- Action: Extract from the MECP optimization the atomic coordinates (geometry), the MECP relative energy (with respect to the separated triplet Fe(CO)₄ and CO, without ZPE), and the spin‑orbit coupling matrix element V₁₂. Also include the gradient differences ΔF, geometric mean F, and reduced mass μ_H needed for rate recomputation. Write all data to the output file.
- Output file: `/app/outputs/step_02_MECP.json`
- Format: json
- Contract: {"geometry": {"Fe": [x,y,z], "C1": [x,y,z], "O1": [x,y,z], ...}, "relative_energy_kcalmol": float, "V12_cm1": float, "deltaF": float, "F": float, "mu_H_reduced_mass": float}
- Scoring: scored by hidden verifier

### Step 6: Compute NA‑TST rate coefficient at 300 K
- Role: scored
- Action: Using the reactant partition function data (rotational constants, vibrational frequencies, electronic degeneracies from the geometry/frequency step) and the MECP properties (energy, frequencies, ΔF, F, μ_H, V₁₂) from the MECP summary, compute the bimolecular rate coefficient k(T) at T = 300 K using both the Landau–Zener and the WKB (Delos) surface‑hopping probabilities as described in the paper. Output the two rate values.
- Output file: `/app/outputs/step_03_rate_coefficient.json`
- Format: json
- Contract: {"T": 300, "k_LZ_cm3_molecule-1_s-1": float, "k_WKB_cm3_molecule-1_s-1": float}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_energetics.json`
- `/app/outputs/step_02_MECP.json`
- `/app/outputs/step_03_rate_coefficient.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_energetics.json
- path: `/app/outputs/step_01_energetics.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Computed singlet–triplet splitting and bond dissociation energy (electronic and with ZPE correction) at the CCSD(T)/VQZ‑VDZ//B3PW91* level, compared to the paper’s best‑estimate values.
- schema:
  - `type`: object
  - `required`:
    - `deltaE13_electronic_kcalmol`: number
    - `deltaE13_withZPE_kcalmol`: number
    - `BDE3_electronic_kcalmol`: number
    - `BDE3_withZPE_kcalmol`: number
  - `units`:
    - `deltaE13_electronic_kcalmol`: kcal/mol
    - `deltaE13_withZPE_kcalmol`: kcal/mol
    - `BDE3_electronic_kcalmol`: kcal/mol
    - `BDE3_withZPE_kcalmol`: kcal/mol

### step_02_MECP.json
- path: `/app/outputs/step_02_MECP.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: MECP structure, relative energy, spin‑orbit coupling V₁₂, and the dynamical parameters (ΔF, F, μ_H) required to recompute the non‑adiabatic rate. Compared to the paper’s reported B3PW91*/TZV MECP energy and V₁₂ within tolerances.
- schema:
  - `type`: object
  - `required`:
    - `geometry`: object (atom labels to Cartesian coordinates)
    - `relative_energy_kcalmol`: number
    - `V12_cm1`: number
    - `deltaF`: number
    - `F`: number
    - `mu_H_reduced_mass`: number
  - `units`:
    - `relative_energy_kcalmol`: kcal/mol
    - `V12_cm1`: cm⁻¹
    - `deltaF`: Hartree/bohr or consistent au
    - `F`: Hartree/bohr or consistent au
    - `mu_H_reduced_mass`: atomic mass units (u)

### step_03_rate_coefficient.json
- path: `/app/outputs/step_03_rate_coefficient.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: NA‑TST rate coefficient at 300 K computed using Landau–Zener and WKB hopping probabilities. The checker recomputes the rate from the submitted step_02_MECP.json parameters and compares it to the agent’s value, then checks the recomputed rate against the paper’s reported value.
- schema:
  - `type`: object
  - `required`:
    - `T`: number (temperature in K)
    - `k_LZ_cm3_molecule-1_s-1`: number
    - `k_WKB_cm3_molecule-1_s-1`: number
  - `units`:
    - `T`: K
    - `k_LZ_cm3_molecule-1_s-1`: cm³ molecule⁻¹ s⁻¹
    - `k_WKB_cm3_molecule-1_s-1`: cm³ molecule⁻¹ s⁻¹

Notes: The checker will recompute the NA‑TST rate from the MECP parameters in step_02_MECP.json to verify consistency, and will also compare the recomputed rate to the paper’s experimental‑level reference value. Energetics and MECP properties are compared directly to the paper’s reported values with appropriate tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_energetics.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "deltaE13_electronic_kcalmol": "number",
          "deltaE13_withZPE_kcalmol": "number",
          "BDE3_electronic_kcalmol": "number",
          "BDE3_withZPE_kcalmol": "number"
        },
        "units": {
          "deltaE13_electronic_kcalmol": "kcal/mol",
          "deltaE13_withZPE_kcalmol": "kcal/mol",
          "BDE3_electronic_kcalmol": "kcal/mol",
          "BDE3_withZPE_kcalmol": "kcal/mol"
        }
      },
      "description": "Computed singlet–triplet splitting and bond dissociation energy (electronic and with ZPE correction) at the CCSD(T)/VQZ‑VDZ//B3PW91* level, compared to the paper’s best‑estimate values."
    },
    {
      "file": "step_02_MECP.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "geometry": "object (atom labels to Cartesian coordinates)",
          "relative_energy_kcalmol": "number",
          "V12_cm1": "number",
          "deltaF": "number",
          "F": "number",
          "mu_H_reduced_mass": "number"
        },
        "units": {
          "relative_energy_kcalmol": "kcal/mol",
          "V12_cm1": "cm⁻¹",
          "deltaF": "Hartree/bohr or consistent au",
          "F": "Hartree/bohr or consistent au",
          "mu_H_reduced_mass": "atomic mass units (u)"
        }
      },
      "description": "MECP structure, relative energy, spin‑orbit coupling V₁₂, and the dynamical parameters (ΔF, F, μ_H) required to recompute the non‑adiabatic rate. Compared to the paper’s reported B3PW91*/TZV MECP energy and V₁₂ within tolerances."
    },
    {
      "file": "step_03_rate_coefficient.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": {
          "T": "number (temperature in K)",
          "k_LZ_cm3_molecule-1_s-1": "number",
          "k_WKB_cm3_molecule-1_s-1": "number"
        },
        "units": {
          "T": "K",
          "k_LZ_cm3_molecule-1_s-1": "cm³ molecule⁻¹ s⁻¹",
          "k_WKB_cm3_molecule-1_s-1": "cm³ molecule⁻¹ s⁻¹"
        }
      },
      "description": "NA‑TST rate coefficient at 300 K computed using Landau–Zener and WKB hopping probabilities. The checker recomputes the rate from the submitted step_02_MECP.json parameters and compares it to the agent’s value, then checks the recomputed rate against the paper’s reported value."
    }
  ],
  "notes": "The checker will recompute the NA‑TST rate from the MECP parameters in step_02_MECP.json to verify consistency, and will also compare the recomputed rate to the paper’s experimental‑level reference value. Energetics and MECP properties are compared directly to the paper’s reported values with appropriate tolerances."
}
```

## How you are scored
A hidden verifier evaluates your three output files independently. For the energetics and MECP summary, the verifier compares your reported values to reference values (with appropriate physical tolerances). For the rate coefficient, the verifier recomputes the NA-TST rate from the MECP parameters you supplied in `step_02_MECP.json` (ΔF, F, μ_H, V₁₂) and checks that your submitted rate is consistent with the recomputed value; it then compares the recomputed rate to an experimental‑level reference. The three artifacts contribute to the final reward with separate weights (energetics ~30%, MECP ~30%, rate coefficient ~40%), giving a total score between 0 and 1. You must faithfully execute the full computational pipeline; simply reporting hardcoded numbers is not sufficient to obtain a high score.
