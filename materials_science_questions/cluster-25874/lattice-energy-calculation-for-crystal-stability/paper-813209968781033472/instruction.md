# Heats of Formation and Energetic Properties of Substituted RDX and HMX Derivatives via DFT

## Problem background
High energy density materials (HEDMs) such as RDX (hexahydro-1,3,5-trinitro-1,3,5-triazine) and β-HMX (1,3,5,7-tetranitro-1,3,5,7-tetraazacyclooctane) are widely used explosives with well‑established structures and performance. To develop derivatives with potentially superior energetic properties, one strategy is to replace the nitro groups (–NO₂) on the parent ring by bulkier polynitro‑alkyl substituents: trinitromethyl (–C(NO₂)₃) or dinitromethyl (–CH(NO₂)₂). The effect of such substitutions on heats of formation, detonation performance, thermal stability, and impact sensitivity is not yet fully established for these ring systems. This raises the quantitative question: how do these substituents alter the gas‑phase and solid‑phase heats of formation, detonation velocity and pressure, ring strain, bond energies, and free volume, and do the trinitromethyl and dinitromethyl groups produce systematically different trends? The present task aims to answer these questions by a reproducible computational pipeline that delivers numerical predictions for all considered compounds.

## Approach
The approach combines density functional theory (DFT) calculations with established empirical corrections to obtain the required properties without relying on any pre‑computed results. All molecular geometries – the parent compounds RDX and β‑HMX, their trinitromethyl‑ and dinitromethyl‑substituted derivatives (20 in total), as well as the small reference molecules needed for isodesmic and homodesmotic reactions and the radical fragments for bond dissociation energies – are optimized at the B3LYP/6‑31G(d,p) level. Frequency calculations confirm that each structure is a minimum and provide zero‑point energies and thermal corrections. Gas‑phase heats of formation are obtained via isodesmic reactions that conserve bond types, using experimental reference heats of formation for CH₄, NH₃, CH₃NH₂, CH(NO₂)₃ and CH₂(NO₂)₂ (taken from public thermochemical sources) together with G2‑theory values for the ring parent molecules (chair‑1,3,5‑triazacyclohexane, chair‑1,3,5,7‑tetraazacyclooctane) and NH₂NO₂. Solid‑phase heats of formation are then derived by subtracting an empirically estimated sublimation enthalpy, calculated from the molecular surface area and electrostatic potential descriptors (A, v, σ²_tot) evaluated at the 0.001 e/bohr³ isosurface. Crystal density is predicted from the molecular volume inside the same isosurface, corrected by an electrostatic interaction term. Using the solid‑phase heat of formation and the predicted density, detonation properties (heat of detonation Q, detonation velocity D, detonation pressure P, and oxygen balance OB) are computed with the Kamlet‑Jacobs equations. Strain energies of the central 1,3,5‑triazinane or 1,3,5,7‑tetrazocane ring are obtained through homodesmotic reactions that isolate the ring strain from substituent effects. Bond dissociation energies for key bonds (C–N in the ring, N–NO₂, N–R where R is the substituent, and C–NO₂ within the substituent) are determined from the total energies of the optimised parent molecule and the corresponding radical fragments, including zero‑point corrections. Finally, the free space per molecule in the crystal, a proxy for impact sensitivity, is computed as ΔV = V_eff − V_int, where V_eff = M/ρ and V_int is the volume inside the 0.003 e/bohr³ isosurface.

## Reproduction target
Produce a CSV file, `/app/outputs/computed_properties.csv`, containing one row for each of the 22 compounds: RDX (A0), β‑HMX (B0), the dinitromethyl‑substituted series A11–A13 and B11–B15, and the trinitromethyl‑substituted series A21–A23 and B21–B25. For every compound report the following quantities (in the specified units): total electronic energy E0 (a.u.), zero‑point energy ZPE (a.u.), thermal correction H_T (kJ/mol), gas‑phase heat of formation ΔHf,gas (kJ/mol), molecular surface area A (Å²), electrostatic balance v (dimensionless), surface electrostatic variability σ²_tot (kcal/mol), sublimation enthalpy ΔHsub (kJ/mol), solid‑phase heat of formation ΔHf,solid (kJ/mol), crystal density ρ (g/cm³), heat of detonation Q (cal/g), detonation velocity D (km/s), detonation pressure P (GPa), oxygen balance OB (%), strain energy SE (kJ/mol), bond dissociation energies BDE_ring_CN, BDE_N_NO₂, BDE_N_R, BDE_C_NO₂ (all in kJ/mol), effective molecular volume V_eff (Å³), intrinsic molecular volume V_int (Å³), and free space per molecule ΔV (Å³). For bonds that do not exist in a particular compound (e.g., parent compounds lack a substituent), the corresponding BDE columns may be left blank or filled with NaN. The exact column order and naming must match the output contract; no additional rows or columns may appear.

## Assets

- Quantum chemistry software supporting B3LYP/6-31G(d,p) and G2 theory
- NIST Chemistry WebBook: experimental gas-phase heats of formation for CH4, NH3, CH3NH2: https://webbook.nist.gov/chemistry/
- Experimental heats of formation of trinitromethane and dinitromethane from literature: 10.1007/BF00926190
- Rice et al. (2006) sublimation enthalpy correlation coefficients: 10.1021/jp0536192
- Politzer et al. (2009) crystal density electrostatic correction coefficients: 10.1080/00268970903007073
- Kamlet-Jacobs detonation equations: 10.1063/1.1666768
- Pospíšil et al. free space per molecule method: 10.1007/s00894-010-0817-3

## Workflow steps

### Step 1: DFT geometry optimization and frequency calculation
- Role: process
- Action: Optimize geometries and compute total energies E0, zero-point energies ZPE, and thermal corrections H_T for all target molecules (RDX, β-HMX, and all their trinitromethyl- and dinitromethyl-substituted derivatives) and all required reference and small molecules used in isodesmic, homodesmotic, and bond-dissociation reactions, using B3LYP/6-31G(d,p). Confirm all optimized structures are minima (no imaginary frequencies).
- Evidence: `/app/outputs/optimization_output.log`

### Step 2: Obtain reference heats of formation
- Role: process
- Action: Collect experimental gas-phase heats of formation at 298 K from public sources for CH4, NH3, CH3NH2, CH(NO2)3, and CH2(NO2)2. For chair-1,3,5-triazacyclohexane, chair-1,3,5,7-tetraazacyclooctane, and NH2NO2, compute HOFs via G2 theory atomization reactions using the geometries from step_01.
- Evidence: `/app/outputs/reference_hofs.json`

### Step 3: Calculate gas-phase heats of formation via isodesmic reactions
- Role: process
- Action: For each target molecule, set up the appropriate isodesmic reaction (one scheme for RDX-derived six-membered ring, one for β-HMX-derived eight-membered ring) that conserves bond counts. Use the total energies, ZPEs, and thermal corrections from step_01 and the reference HOFs from step_02 to compute the gas-phase heat of formation ΔHf,gas at 298 K.
- Evidence: none

### Step 4: Calculate molecular electrostatic surface descriptors
- Role: process
- Action: For each target molecule, extract the molecular surface area A, electrostatic balance v, and surface electrostatic variability σ²tot from the electron density at the 0.001 e/bohr³ isosurface using the optimized geometry from step_01.
- Evidence: none

### Step 5: Calculate sublimation enthalpies
- Role: process
- Action: Compute ΔHsub for each target molecule using the empirical correlation ΔHsub = aA² + b(vσ²tot)^0.5 + c with coefficients from the literature (a=2.670e-4 kcal/mol/Å⁴, b=1.650 kcal/mol, c=2.966 kcal/mol) and the descriptors from step_04. Convert to kJ/mol.
- Evidence: none

### Step 6: Calculate solid-phase heats of formation
- Role: process
- Action: Compute ΔHf,solid = ΔHf,gas − ΔHsub for each target molecule using the gas-phase HOFs from step_03 and sublimation enthalpies from step_05.
- Evidence: none

### Step 7: Predict crystal density
- Role: process
- Action: For each target molecule, determine the molecular volume V(0.001) by Monte Carlo integration inside the 0.001 e/bohr³ isosurface. Compute the crystal density ρ using the electrostatic correction: ρ = β1(M/V(0.001)) + β2(vσ²tot) + β3, with coefficients from the literature (β1=0.9183, β2=0.00278, β3=0.0), where M is molecular mass and v, σ²tot from step_04.
- Evidence: none

### Step 8: Calculate detonation properties
- Role: process
- Action: Calculate the heat of detonation Q from the solid-phase HOF and the molecular composition (products CO2, H2O, N2, with priority rules for oxygen). Compute detonation velocity D and pressure P using the Kamlet-Jacobs equations, and oxygen balance OB. Use density ρ from step_07.
- Evidence: none

### Step 9: Calculate strain energies via homodesmotic reactions
- Role: process
- Action: Use the optimized geometries and energies from step_01 for each target molecule and the required small reference molecules in the homodesmotic reaction schemes (for RDX and β-HMX series) to compute strain energy SE = (sum of product energies + ZPE correction) − (sum of reactant energies).
- Evidence: none

### Step 10: DFT calculations on radical fragments for bond dissociation energies
- Role: process
- Action: For each target molecule, generate radical fragments by homolytically cleaving the selected bonds (C-N ring, N-NO2, N-R, C-NO2 in substituent). Optimize geometries and compute total energies and ZPEs for these radical species at B3LYP/6-31G(d,p) using unrestricted calculations.
- Evidence: `/app/outputs/radical_energies.json`

### Step 11: Calculate bond dissociation energies
- Role: process
- Action: For each target molecule, compute the bond dissociation energies for the selected bonds using BDE = [E0(radical A) + E0(radical B) − E0(parent)] + ΔZPE correction, where energies are from step_01 (parent) and step_10 (radicals).
- Evidence: none

### Step 12: Calculate free space per molecule
- Role: process
- Action: For each target molecule, compute the intrinsic molecular volume Vint inside the 0.003 e/bohr³ isosurface. Obtain effective volume Veff = M/ρ using molecular mass M and density ρ from step_07. Compute ΔV = Veff − Vint.
- Evidence: none

### Step 13: Compile final properties CSV
- Role: scored
- Action: Assemble all computed properties for the 22 molecules (RDX, β-HMX, and all derivatives) into a single CSV file.
- Output file: `/app/outputs/computed_properties.csv`
- Format: csv
- Contract: CSV with columns: compound (string), E0 (float, a.u.), ZPE (float, a.u.), H_T (float, kJ/mol), DeltaH_f_gas (float, kJ/mol), A (float, Angstrom^2), v (float, dimensionless), sigma2_tot (float, kcal/mol), DeltaH_sub (float, kJ/mol), DeltaH_f_solid (float, kJ/mol), rho (float, g/cm^3), Q (float, cal/g), D (float, km/s), P (float, GPa), OB (float, %), SE (float, kJ/mol), BDE_ring_CN (float, kJ/mol), BDE_N_NO2 (float, kJ/mol), BDE_N_R (float, kJ/mol), BDE_C_NO2 (float, kJ/mol), V_eff (float, Angstrom^3), V_int (float, Angstrom^3), Delta_V (float, Angstrom^3). Missing BDE values for bonds not present may be left blank or NaN.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/computed_properties.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### computed_properties.csv
- path: `/app/outputs/computed_properties.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Compiled results table with computed gas-phase and solid-phase heats of formation, detonation properties, strain energies, bond dissociation energies, and free space per molecule for all title compounds. The checker compares these values against paper-reported gold values with tolerances.
- schema:
  - `type`: table
  - `required_columns`: `compound`, `E0`, `ZPE`, `H_T`, `DeltaH_f_gas`, `A`, `v`, `sigma2_tot`, `DeltaH_sub`, `DeltaH_f_solid`, `rho`, `Q`, `D`, `P`, `OB`, `SE`, `BDE_ring_CN`, `BDE_N_NO2`, `BDE_N_R`, `BDE_C_NO2`, `V_eff`, `V_int`, `Delta_V`

Notes: The tolerances and gold values are hidden. Scoring uses threshold-or-better with tolerances appropriate for DFT-level property reproduction. The trend of HOF differences between substituent types is also verified.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "computed_properties.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "compound",
          "E0",
          "ZPE",
          "H_T",
          "DeltaH_f_gas",
          "A",
          "v",
          "sigma2_tot",
          "DeltaH_sub",
          "DeltaH_f_solid",
          "rho",
          "Q",
          "D",
          "P",
          "OB",
          "SE",
          "BDE_ring_CN",
          "BDE_N_NO2",
          "BDE_N_R",
          "BDE_C_NO2",
          "V_eff",
          "V_int",
          "Delta_V"
        ]
      },
      "description": "Compiled results table with computed gas-phase and solid-phase heats of formation, detonation properties, strain energies, bond dissociation energies, and free space per molecule for all title compounds. The checker compares these values against paper-reported gold values with tolerances."
    }
  ],
  "notes": "The tolerances and gold values are hidden. Scoring uses threshold-or-better with tolerances appropriate for DFT-level property reproduction. The trend of HOF differences between substituent types is also verified."
}
```

## How you are scored
A hidden verifier inspects the submitted `/app/outputs/computed_properties.csv`. It compares each reported numeric value (heats of formation, detonation properties, strain energies, bond dissociation energies, free space) against reference values derived from the original study. Scoring follows a threshold‑or‑better policy: you receive full credit when your computed value is at least as good as the threshold, and partial credit when it is worse. The verifier additionally evaluates the qualitative trend of the heats of formation: it checks that the computed values reflect the systematic differences between trinitromethyl‑substituted, dinitromethyl‑substituted, and parent compounds. The overall reward is a weighted sum over all evaluated quantities. Merely writing down numbers without executing the described pipeline will not yield a correct submission because the verifier tests for internal consistency and expects genuine computational artefacts.
