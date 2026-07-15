# Deuterium Quadrupole Coupling Constant Calculation for Benzene-d1

## Problem background
The deuterium quadrupole coupling constant (DQCC) in deuterated benzenes is a fundamental molecular property that governs the splitting of NMR lines for quadrupolar nuclei in anisotropic environments. Accurate knowledge of the DQCC and its asymmetry parameter is essential for interpreting NMR spectra of molecules dissolved in liquid crystals, for molecular dynamics studies, and for benchmarking quantum-chemical methods. This work addresses the theoretical determination of the DQCC in benzene-d1 (C6H5D) by combining high-level electron-structure calculations with harmonic rovibrational corrections. The goal is to compute a value that can be compared with experimental liquid-crystal NMR results, thereby assessing the reliability of modern ab initio methods for nuclear quadrupole coupling tensors.

## Approach
The theoretical approach consists of two main components:

1. **Equilibrium electronic structure calculation** – The electric field gradient (EFG) at the deuterium nucleus is computed at the SCF and MP2 levels of theory using a locally dense (LD) basis set. This basis set is constructed from IGLO basis sets: for the deuterium atom, the IGLO‑IV hydrogen basis is augmented with tight p and d primitives (exponents scaled by a factor of 3) and one f function from cc‑pVQZ; the other hydrogens use IGLO‑II without d functions; carbons use IGLO‑III but with polarization exponents taken from IGLO‑IV. The EFG is converted to a DQCC (in kHz) using a fixed nuclear quadrupole moment Q(²H) = 0.2860 fm², and the asymmetry parameter η is extracted.

2. **Harmonic rovibrational correction** – Using a published harmonic force field and the same equilibrium geometry, a normal‑mode perturbation‑theory calculation is performed at the SCF/HIII level (IGLO‑III basis on all atoms) to obtain the vibrational contributions ΔDQCC and Δη. These corrections are added to the equilibrium SCF and MP2 results to yield the final, rovibrationally averaged DQCC and asymmetry parameter for C6H5D at 300 K.

The method assumes that anharmonic effects can be adequately accounted for by using an effective rα geometry approximation, and solvent effects are negligible for the final comparison.

## Reproduction target
Starting from the equilibrium geometry of benzene (r_CC = 1.3914 Å, r_CH = 1.0802 Å) and the harmonic force field extracted from the literature, perform the quantum‑chemical workflow described in the steps below to obtain the final corrected SCF and MP2 deuterium quadrupole coupling constants (in kHz) and the associated asymmetry parameters for benzene‑d1 (C6H5D). Report these four numbers in the scored output file `/app/outputs/theoretical_DQCC.json`.

## Assets

- DALTON quantum chemistry package: https://daltonprogram.org/
- IGLO basis sets (HII, HIII, HIV): https://www.basissetexchange.org
- Equilibrium geometry of benzene (Gauss and Stanton 2000): 10.1021/jp9932893
- Harmonic force field of benzene (Goodman et al. 1991): 10.1021/j100180a033

## Workflow steps

### Step 1: Prepare geometry and force field
- Role: process
- Action: Obtain the equilibrium geometry of benzene (r_CC=1.3914 Å, r_CH=1.0802 Å) from Gauss and Stanton (2000) and the harmonic force field from Goodman et al. (1991). Construct Cartesian coordinates for C6H5D by replacing one hydrogen with deuterium at the same bond length; keep the ring geometry unchanged. Extract the force constants in internal coordinates. Set up the input files needed for the quantum chemistry calculations.
- Evidence: `/app/outputs/geometry.xyz`

### Step 2: Compute raw SCF and MP2 DQCC with LD basis
- Role: process
- Action: Perform single-point energy and electric-field-gradient calculations for C6H5D at the equilibrium geometry using SCF and MP2 methods with the locally dense (LD) basis set. The basis is: for deuterium, a [6s6p4d1f] set formed by augmenting the IGLO-IV hydrogen basis with three successive tight p and d primitives (exponent factor 3) and adding one f from cc-pVQZ; for the other hydrogens, use IGLO-II without d functions; for carbon, use IGLO-III with the polarization exponents from IGLO-IV. Convert the EFG to DQCC (kHz) using the nuclear quadrupole moment Q(2H)=0.2860 fm^2. Record the raw DQCC and eta for both levels.
- Evidence: `/app/outputs/raw_dqcc_ld.json`

### Step 3: Compute harmonic rovibrational corrections
- Role: process
- Action: Using the harmonic force field from step 1, perform a normal-mode perturbation-theory calculation at the SCF/HIII level (IGLO-III basis for all atoms) on the same equilibrium geometry of C6H5D. Compute the harmonic vibrational contribution to the DQCC and eta. Record the total rovibrational corrections delta_DQCC and delta_eta.
- Evidence: `/app/outputs/rovib_correction.json`

### Step 4: Assemble final corrected DQCC and eta
- Role: scored (load-bearing)
- Action: Add the rovibrational corrections from step 3 to the raw SCF and MP2 DQCC and eta from step 2. For each method, final_value = raw_value + correction. Write the resulting four numbers to /app/outputs/theoretical_DQCC.json.
- Output file: `/app/outputs/theoretical_DQCC.json`
- Format: json
- Contract: {"SCF_DQCC_kHz": <float>, "MP2_DQCC_kHz": <float>, "SCF_eta": <float>, "MP2_eta": <float>}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/theoretical_DQCC.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### theoretical_DQCC.json
- path: `/app/outputs/theoretical_DQCC.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Final corrected SCF and MP2 deuterium quadrupole coupling constant (kHz) and asymmetry parameter for C6H5D.
- schema:
  - `type`: object
  - `required`:
    - `SCF_DQCC_kHz`: number
    - `MP2_DQCC_kHz`: number
    - `SCF_eta`: number
    - `MP2_eta`: number
  - `units`:
    - `SCF_DQCC_kHz`: kHz
    - `MP2_DQCC_kHz`: kHz
    - `SCF_eta`: unitless
    - `MP2_eta`: unitless

Notes: The scoring tolerance for DQCC values is ±2 kHz; eta values are checked for range compliance.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "theoretical_DQCC.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "SCF_DQCC_kHz": "number",
          "MP2_DQCC_kHz": "number",
          "SCF_eta": "number",
          "MP2_eta": "number"
        },
        "units": {
          "SCF_DQCC_kHz": "kHz",
          "MP2_DQCC_kHz": "kHz",
          "SCF_eta": "unitless",
          "MP2_eta": "unitless"
        }
      },
      "description": "Final corrected SCF and MP2 deuterium quadrupole coupling constant (kHz) and asymmetry parameter for C6H5D."
    }
  ],
  "notes": "The scoring tolerance for DQCC values is ±2 kHz; eta values are checked for range compliance."
}
```

## How you are scored
A hidden verifier independently assesses each workflow stage's artifact and combines the per‑stage scores (weighted) into a final reward. The main scored artifact is `/app/outputs/theoretical_DQCC.json`. The verifier will compare the DQCC values you compute to hidden gold reference values within a tolerance, and will check that the asymmetry parameters fall within an expected range. Simply reporting numbers found in the original publication is not sufficient; you must execute the pipeline and produce the artifacts from your own calculations to receive credit.
