# DFT computation of Mössbauer isomer shifts for Fe(III) complex 1

## Problem background
Iron(III) complexes with cyclin-dependent kinase (CDK) inhibitors are of interest for their magnetic and electronic properties. In the solid state, such complexes can exhibit a mixture of coordination geometries and spin states. Mössbauer spectroscopy is sensitive to the local environment of the iron nucleus, and density functional theory (DFT) calculations can model possible structures, compute relative stabilities, and predict ⁵⁷Fe Mössbauer isomer shifts. The target here is to compute the Mössbauer isomer shifts for a model complex, [Fe(L₁)Cl₃], in several plausible coordination arrangements, and thereby help rationalise the experimental spectroscopic signatures.

## Approach
We consider four variants of the [Fe(L₁)Cl₃] complex, differing in coordination mode and spin state (1a–1d). For each, a molecular model is built, then the geometry is optimised using DFT at the B3LYP/6-311G(d) level with Wachter's all-electron basis for iron. A harmonic vibrational frequency check ensures the optimised structures are local minima. From the converged electron density, the non-relativistic electron density at the ⁵⁷Fe nucleus, ρ₀ᴬ⁡(0), is extracted. The Mössbauer isomer shift δ (mm/s) is calculated using δ = α [ρ₀ᴬ⁡(0) − ρ₀ˢ⁡(0)], where the calibration constants α = −0.395 mm s⁻¹ au³ and ρ₀ˢ = 11614.10 au⁻³ are adopted from the literature. The shifts are reported at 0 K (no Doppler correction).

## Reproduction target
Compute the ⁵⁷Fe Mössbauer isomer shift (δ, in mm/s) at 0 K for each of the four model structures of [Fe(L₁)Cl₃] labelled 1a, 1b, 1c, and 1d, using the DFT protocol described above. Report the four values as a JSON object with keys "1a", "1b", "1c", "1d" and floating-point values.

## Assets

- Open-source DFT package (e.g., ORCA, NWChem, PySCF): ORCA
- Wachter's all-electron basis set for Fe: 10.1063/1.1676429
- Mössbauer calibration constants

## Workflow steps

### Step 1: Build initial structures
- Role: process
- Action: Construct molecular models for the four variants of [Fe(L₁)Cl₃]: 1a (tetrahedral, Fe coordinated to N7 of L₁ and three Cl⁻, spin state S=5/2); 1b (N6 monodentate coordination with a proton shifted to N3); 1c (bidentate coordination via N6 and N7 with proton at N1); 1d (trigonal-bipyramidal, Fe coordinated to N7, three Cl⁻, and one water molecule, spin state S=3/2). Use the ligand's chemical structure (2-chloro-6-benzylamino-9-isopropylpurine) and the descriptions provided.
- Evidence: none

### Step 2: DFT geometry optimization and frequency check
- Role: scored
- Action: Optimize the geometry of each structure (1a-1d) using density functional theory at the B3LYP/6-311G(d)+Wachter's level. Perform harmonic vibrational frequency calculations to verify that the optimized structures are minima. Save the final optimized coordinates of all four structures in a single XYZ file.
- Output file: `/app/outputs/step_01_optimized_structures.xyz`
- Format: txt
- Contract: XYZ file with multiple structures. Each molecule begins with the number of atoms on a line, followed by a comment line specifying '1a (S=5/2)', '1b', '1c', '1d (S=3/2)' etc., then lines with element symbol and x,y,z coordinates in Angstrom.
- Scoring: scored by hidden verifier

### Step 3: Mössbauer isomer shift calculation
- Role: scored (load-bearing)
- Action: From the optimized wavefunction/electron density of each structure, compute the non-relativistic electron density at the ⁵⁷Fe nucleus, ρ₀^A(0). Calculate the Mössbauer isomer shift δ (mm/s) using δ = α [ρ₀^A(0) - ρ₀^S(0)], where α = -0.395 mm s⁻¹ au³ and ρ₀^S = 11614.10 au⁻³. Report the shifts at 0 K (no Doppler correction). Output a JSON file with the computed shifts.
- Output file: `/app/outputs/step_02_isomer_shifts.json`
- Format: json
- Contract: JSON object with keys '1a', '1b', '1c', '1d' (all strings) and values being floats representing the isomer shift δ in mm/s (unitless in JSON).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_optimized_structures.xyz`
- `/app/outputs/step_02_isomer_shifts.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_optimized_structures.xyz
- path: `/app/outputs/step_01_optimized_structures.xyz`
- format: txt
- purpose: scored
- target_policy: structural_audit
- description: Optimized geometries of the four Fe(III) complex models, used to verify that the DFT geometry optimization was performed correctly and produced minima.
- schema:
  - `type`: text
  - `description`: XYZ file with four optimized structures (1a, 1b, 1c, 1d). Each structure begins with a line containing the number of atoms, followed by a comment line identifying the model and spin state, then lines with element symbol and Cartesian coordinates (Å). The file must be parseable and contain chemically reasonable Fe–ligand bond lengths and coordination numbers.

### step_02_isomer_shifts.json
- path: `/app/outputs/step_02_isomer_shifts.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: The agent's computed Mössbauer isomer shifts. The checker compares each value to the hidden gold (paper-reported theoretical shifts) with a tight tolerance.
- schema:
  - `type`: object
  - `required`:
    - `1a`: float (mm/s)
    - `1b`: float (mm/s)
    - `1c`: float (mm/s)
    - `1d`: float (mm/s)
  - `description`: JSON object containing the computed ⁵⁷Fe Mössbauer isomer shifts at 0 K for the four structures. Values are unitless floats representing δ in mm/s.

Notes: The agent must use the specified DFT method, basis sets, and calibration constants. The kinetic isotope effect (temperature Doppler shift) must not be applied; report 0 K values. The vibrational frequency check is required to ensure the optimized structures are minima but its output is not submitted.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_optimized_structures.xyz",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "text",
        "description": "XYZ file with four optimized structures (1a, 1b, 1c, 1d). Each structure begins with a line containing the number of atoms, followed by a comment line identifying the model and spin state, then lines with element symbol and Cartesian coordinates (Å). The file must be parseable and contain chemically reasonable Fe–ligand bond lengths and coordination numbers."
      },
      "description": "Optimized geometries of the four Fe(III) complex models, used to verify that the DFT geometry optimization was performed correctly and produced minima."
    },
    {
      "file": "step_02_isomer_shifts.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "1a": "float (mm/s)",
          "1b": "float (mm/s)",
          "1c": "float (mm/s)",
          "1d": "float (mm/s)"
        },
        "description": "JSON object containing the computed ⁵⁷Fe Mössbauer isomer shifts at 0 K for the four structures. Values are unitless floats representing δ in mm/s."
      },
      "description": "The agent's computed Mössbauer isomer shifts. The checker compares each value to the hidden gold (paper-reported theoretical shifts) with a tight tolerance."
    }
  ],
  "notes": "The agent must use the specified DFT method, basis sets, and calibration constants. The kinetic isotope effect (temperature Doppler shift) must not be applied; report 0 K values. The vibrational frequency check is required to ensure the optimized structures are minima but its output is not submitted."
}
```

## How you are scored
A hidden verifier will inspect your submitted artifacts after your run finishes. The optimised geometry file (step 1) is checked for parseability, correct atom counts, and chemically sensible Fe–ligand bond distances. The isomer shift file (step 2) is compared to a hidden reference; each structure's shift is evaluated with a tolerance that accounts for legitimate code-to-code variation. The final reward is a weighted combination of these two checks, with the isomer shifts carrying most of the weight.
