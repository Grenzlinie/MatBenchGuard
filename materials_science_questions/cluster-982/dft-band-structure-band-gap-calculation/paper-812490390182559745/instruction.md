# First-principles Calculation of Band Gap and SHG Coefficients for Sulfate Iodate Crystals

## Problem background
Noncentrosymmetric crystals are essential for second harmonic generation (SHG), a nonlinear optical process used in frequency conversion for solid-state lasers. Designing new noncentrosymmetric materials with strong SHG response is an active challenge. A strategy to tailor structural dimensionality and optical properties is aliovalent substitution, where an anionic group is replaced by another of different charge. This task concerns a mixed-metal sulfate iodate, AgBi(SO₄)(IO₃)₂ (ABSI), synthesized via aliovalent substitution from the parent iodate AgBi(IO₃)₄ (ABI). The structural transformation is accompanied by changes in the crystal packing and potentially enhanced nonlinear optical performance. First-principles density functional theory (DFT) calculations are employed to compute the electronic band gap, the full second-order nonlinear susceptibility tensor, and powder-averaged SHG coefficients for both compounds, aiming to quantify the SHG response and understand its microscopic origin.

## Approach
We use plane-wave pseudopotential DFT within the generalized gradient approximation (GGA-PBE) to perform self-consistent field (SCF) calculations and band structure computations on both ABSI and ABI. The Kohn-Sham band gap is extracted from the band structure. The second-order nonlinear optical susceptibility tensor (SHG) is then computed using the length-gauge formalism from the SCF wavefunctions. From the tensor, the powder SHG coefficient is obtained by the Kurtz-Perry powder averaging method, and the dominant d22 tensor component is identified. The same computational protocol is applied to the parent ABI compound to enable a direct comparison. All calculations use publicly available crystal structure data and standard pseudopotential libraries.

## Reproduction target
Compute the following quantities and write each as a single floating-point number in a plain text file:
- Kohn-Sham band gap of ABSI (eV)
- Powder SHG coefficient of ABSI (pm/V)
- d22 component of the SHG tensor of ABSI (pm/V)
- Powder SHG coefficient of ABI (pm/V)
Additionally, compare the powder SHG coefficients of the two compounds and determine whether ABSI exhibits a larger SHG response than ABI. The comparison is performed by the hidden verifier based on the submitted values; no separate output is required.

## Assets

- CIF file for ABSI crystal structure: 10.1039/d0cc07862j
- CIF file for ABI crystal structure: 10.1039/C4TC00032K
- Open-source DFT code with SHG functionality: https://www.abinit.org
- Standard pseudopotential library (e.g., SSSP, PseudoDojo): https://www.materialscloud.org/discover/sssp/

## Workflow steps

### Step 1: Obtain and prepare crystal structures
- Role: process
- Action: Retrieve the CIF files for ABSI and ABI from public crystallographic repositories. Convert them into input files suitable for the chosen DFT code (e.g., generate atomic positions and lattice vectors).
- Evidence: `/app/outputs/absi_struct.pickle`

### Step 2: DFT band structure calculation for ABSI
- Role: process
- Action: Perform a self-consistent field (SCF) calculation followed by a non-self-consistent band structure calculation on the ABSI crystal structure using a GGA exchange-correlation functional and the chosen pseudopotentials. Save the band structure data and SCF wavefunctions.
- Evidence: `/app/outputs/absi_scf_wavefunctions.npy`

### Step 3: Extract Kohn-Sham band gap for ABSI
- Role: scored (load-bearing)
- Action: From the band structure of ABSI, locate the valence band maximum and conduction band minimum and compute their energy difference in eV. Write this single float to the output file.
- Output file: `/app/outputs/band_gap_absi.txt`
- Format: txt
- Contract: Single float (eV)
- Scoring: scored by hidden verifier

### Step 4: SHG tensor calculation for ABSI
- Role: process
- Action: Using the SCF wavefunctions from step 2, compute the full second-order nonlinear optical susceptibility tensor (SHG) for ABSI within the length-gauge formalism. Save all independent tensor components in pm/V.
- Evidence: `/app/outputs/shg_absi_tensor.json`

### Step 5: Extract powder SHG coefficient for ABSI
- Role: scored
- Action: From the computed SHG tensor, compute the powder-averaged second harmonic intensity (Kurtz-Perry method) and write the resulting powder SHG coefficient in pm/V to the output file.
- Output file: `/app/outputs/shg_powder_absi.txt`
- Format: txt
- Contract: Single float (pm/V)
- Scoring: scored by hidden verifier

### Step 6: Extract largest SHG tensor component d22 for ABSI
- Role: scored
- Action: From the SHG tensor, identify the component conventionally labeled d22 and write its value in pm/V to the output file.
- Output file: `/app/outputs/shg_d22_absi.txt`
- Format: txt
- Contract: Single float (pm/V)
- Scoring: scored by hidden verifier

### Step 7: DFT SCF and band structure calculation for ABI
- Role: process
- Action: Perform the same sequence of SCF and band structure calculation on the ABI crystal structure as in step 2. Save the SCF wavefunctions.
- Evidence: `/app/outputs/abi_scf_wavefunctions.npy`

### Step 8: SHG tensor calculation for ABI
- Role: process
- Action: Compute the full SHG tensor for ABI using the wavefunctions from step 7, following the same protocol as step 4.
- Evidence: `/app/outputs/shg_abi_tensor.json`

### Step 9: Extract powder SHG coefficient for ABI
- Role: scored
- Action: Compute the powder SHG coefficient from the ABI SHG tensor (same powder-averaging method as step 5) and write the result in pm/V to the output file.
- Output file: `/app/outputs/shg_powder_abi.txt`
- Format: txt
- Contract: Single float (pm/V)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/band_gap_absi.txt`
- `/app/outputs/shg_powder_absi.txt`
- `/app/outputs/shg_d22_absi.txt`
- `/app/outputs/shg_powder_abi.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### band_gap_absi.txt
- path: `/app/outputs/band_gap_absi.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: Kohn-Sham band gap of ABSI computed from DFT band structure.
- schema:
  - `type`: text
  - `format`: single_float
  - `unit`: eV

### shg_powder_absi.txt
- path: `/app/outputs/shg_powder_absi.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: Powder-averaged second harmonic generation coefficient for ABSI.
- schema:
  - `type`: text
  - `format`: single_float
  - `unit`: pm/V

### shg_d22_absi.txt
- path: `/app/outputs/shg_d22_absi.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: The d22 component of the SHG tensor for ABSI.
- schema:
  - `type`: text
  - `format`: single_float
  - `unit`: pm/V

### shg_powder_abi.txt
- path: `/app/outputs/shg_powder_abi.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: Powder-averaged second harmonic generation coefficient for the parent compound ABI.
- schema:
  - `type`: text
  - `format`: single_float
  - `unit`: pm/V

Notes: All four outputs are single floating-point numbers in plain text. The hidden checker compares each to the paper-reported value within a tolerance, and additionally verifies that the ABSI powder SHG is greater than the ABI powder SHG. The verifier does not need to recompute the values; it reads the submitted text files directly.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "band_gap_absi.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "format": "single_float",
        "unit": "eV"
      },
      "description": "Kohn-Sham band gap of ABSI computed from DFT band structure."
    },
    {
      "file": "shg_powder_absi.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "format": "single_float",
        "unit": "pm/V"
      },
      "description": "Powder-averaged second harmonic generation coefficient for ABSI."
    },
    {
      "file": "shg_d22_absi.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "format": "single_float",
        "unit": "pm/V"
      },
      "description": "The d22 component of the SHG tensor for ABSI."
    },
    {
      "file": "shg_powder_abi.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "format": "single_float",
        "unit": "pm/V"
      },
      "description": "Powder-averaged second harmonic generation coefficient for the parent compound ABI."
    }
  ],
  "notes": "All four outputs are single floating-point numbers in plain text. The hidden checker compares each to the paper-reported value within a tolerance, and additionally verifies that the ABSI powder SHG is greater than the ABI powder SHG. The verifier does not need to recompute the values; it reads the submitted text files directly."
}
```

## How you are scored
Your submission will be evaluated by a hidden verifier that reads the four output text files and compares each value to the correct result with an appropriate tolerance. The verifier also checks that the ordering of the powder SHG coefficients (ABSI vs ABI) matches expectation. Each of these checks contributes a weight to the final reward, which is a number between 0 and 1. You must produce these numbers through a correct execution of the DFT and SHG calculation pipeline; simply writing plausible numbers without performing the calculations will generally not pass the verifier, as the tolerances are set based on legitimate computational reproducibility. The band gap step is load-bearing, meaning that downstream steps rely on its correct execution.
