# DFT study of V2O5 structural and electronic properties using PBE+U+D2 with Mn doping

## Problem background
Vanadium pentoxide (V2O5) is a promising cathode material for metal‑ion batteries because of its high theoretical capacity, but its practical performance is limited by low conductivity and stability. Accurate computational modelling of V2O5 is challenging: standard DFT‑GGA calculations fail to simultaneously reproduce the electronic band gap (they underestimate it) and the weak interlayer spacing (they overestimate it). A combined approach that adds a Hubbard U correction on vanadium 3d states together with a Grimme D2 dispersion correction has been proposed to resolve both shortcomings. Additionally, doping V2O5 with transition metals such as Mn is known to modify its structural and electronic properties. In this task you will computationally evaluate the PBE+U+D2 method for pristine V2O5 and investigate the effects of Mn doping by computing the resulting lattice parameters, band gap, volume change, and magnetization.

## Approach
The computational approach uses spin‑polarized plane‑wave density functional theory (DFT) within the generalized gradient approximation (PBE). To improve the description of electronic correlations and weak interlayer dispersion, a Hubbard U correction (U = 6 eV applied to vanadium 3d states) and the Grimme D2 semi‑empirical dispersion correction are employed together (the PBE+U+D2 scheme). Calculations are performed with the Quantum ESPRESSO package using ultrasoft pseudopotentials. First, a pristine 1×1×2 supercell of α‑V2O5 is built from the experimental crystal structure and fully relaxed (variable cell dynamics) to obtain the equilibrium lattice parameters and electronic band gap. Then, two Mn‑doped supercells are constructed: a substitutional cell (one V replaced by Mn) and an interstitial cell (one Mn inserted between layers). Both doped cells are relaxed with the same PBE+U+D2 settings, and for each the unit cell volume change relative to pristine and the total magnetization per supercell are extracted. The workflow thus evaluates whether the PBE+U+D2 method can simultaneously describe the structure and electronic gap of V2O5, and quantifies how Mn doping alters the volume and induces magnetization.

## Reproduction target
Specifically, you must produce the following three JSON result files:

1. `/app/outputs/pristine_results.json` – containing the relaxed lattice parameters a, b, c (Å), unit cell volume (Å³), and electronic band gap (eV) of pristine V2O5 obtained from the PBE+U+D2 variable‑cell relaxation.

2. `/app/outputs/mn_sub_results.json` – containing the percentage change in unit cell volume (delta_volume_pct) relative to the relaxed pristine volume, and the total magnetization per supercell (magnetization_muB, in μB) for the substitutionally Mn‑doped supercell after relaxation.

3. `/app/outputs/mn_int_results.json` – containing the same quantities for the interstitially Mn‑doped supercell after relaxation.

All quantities are to be computed using the PBE+U+D2 method with U = 6 eV on V 3d, the Grimme D2 correction, and the other computational settings described in the workflow steps. The exact numerical values are not provided; your job is to run the DFT calculations and report the outcomes.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- USPP pseudopotentials (V, O, Mn): https://pseudopotentials.quantum-espresso.org/
- Experimental crystal structure of α-V2O5: 10.1107/S010827018600984X

## Workflow steps

### Step 1: Prepare pristine V2O5 supercell
- Role: process
- Action: Construct a 1x1x2 supercell of α-V2O5 using the experimental crystal structure (lattice parameters a=11.512 Å, b=3.564 Å, c=4.368 Å and fractional coordinates from the Enjalbert & Galy reference).
- Evidence: none

### Step 2: PBE+U+D2 calculation on pristine V2O5
- Role: scored (load-bearing)
- Action: Run spin-polarized plane-wave DFT using Quantum ESPRESSO with the PBE+U+D2 scheme (U=6 eV on V 3d states, Grimme D2 dispersion correction), USPP pseudopotentials, plane-wave cutoff 35 Ry, charge density cutoff 16x larger, Γ-centred k-mesh, Gaussian smearing 0.01 eV. Perform variable-cell relaxation of the pristine supercell and extract the relaxed lattice parameters a, b, c (Å), unit cell volume (Å³), and electronic band gap (eV).
- Output file: `/app/outputs/pristine_results.json`
- Format: json
- Contract: {"a": float (angstrom), "b": float (angstrom), "c": float (angstrom), "volume": float (angstrom^3), "band_gap": float (eV)}
- Scoring: scored by hidden verifier

### Step 3: Prepare Mn substitutional doped supercell
- Role: process
- Action: From the pristine supercell, replace one vanadium atom with manganese to form a substitutionally doped supercell (Mn0.25V1.75O5 stoichiometry).
- Evidence: none

### Step 4: PBE+U+D2 calculation on Mn substitutional doped V2O5
- Role: scored (load-bearing)
- Action: Using the same PBE+U+D2 settings (U=6 eV on V 3d, D2 correction) and computational parameters, perform variable-cell relaxation of the substitutional Mn-doped supercell. Compute the relaxed unit cell volume and total magnetization per supercell (μB).
- Output file: `/app/outputs/mn_sub_results.json`
- Format: json
- Contract: {"delta_volume_pct": float (%), "magnetization_muB": float (muB)}
- Scoring: scored by hidden verifier

### Step 5: Prepare Mn interstitial doped supercell
- Role: process
- Action: From the pristine supercell, insert one Mn atom at an interstitial site between V2O5 layers (approximate Wyckoff position 2b, coordinates (0.5, 0, z≈0.5)) to form an interstitially doped supercell (Mn0.25V2O5 stoichiometry).
- Evidence: none

### Step 6: PBE+U+D2 calculation on Mn interstitial doped V2O5
- Role: scored (load-bearing)
- Action: Using the same PBE+U+D2 settings, perform variable-cell relaxation of the interstitial Mn-doped supercell. Compute the relaxed unit cell volume and total magnetization per supercell (μB).
- Output file: `/app/outputs/mn_int_results.json`
- Format: json
- Contract: {"delta_volume_pct": float (%), "magnetization_muB": float (muB)}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/pristine_results.json`
- `/app/outputs/mn_sub_results.json`
- `/app/outputs/mn_int_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### pristine_results.json
- path: `/app/outputs/pristine_results.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Pristine V2O5 relaxed structure and band gap from PBE+U+D2 calculation.
- schema:
  - `type`: object
  - `required`:
    - `a`: float (angstrom)
    - `b`: float (angstrom)
    - `c`: float (angstrom)
    - `volume`: float (angstrom^3)
    - `band_gap`: float (eV)
  - `items`: object
  - `required_columns`:
  - `units`:
    - `a`: angstrom
    - `b`: angstrom
    - `c`: angstrom
    - `volume`: angstrom^3
    - `band_gap`: eV

### mn_sub_results.json
- path: `/app/outputs/mn_sub_results.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Volume change and magnetization for substitutional Mn-doped V2O5.
- schema:
  - `type`: object
  - `required`:
    - `delta_volume_pct`: float (%)
    - `magnetization_muB`: float (muB)
  - `items`: object
  - `required_columns`:
  - `units`:
    - `delta_volume_pct`: %
    - `magnetization_muB`: muB

### mn_int_results.json
- path: `/app/outputs/mn_int_results.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Volume change and magnetization for interstitial Mn-doped V2O5.
- schema:
  - `type`: object
  - `required`:
    - `delta_volume_pct`: float (%)
    - `magnetization_muB`: float (muB)
  - `items`: object
  - `required_columns`:
  - `units`:
    - `delta_volume_pct`: %
    - `magnetization_muB`: muB

Notes: Scoring compares the agent's reported values for lattice parameters, band gap, volume changes, and magnetizations against the paper's reported or experimental reference values within pre-defined tolerances. The target policy is exact_match with tolerance because these physical quantities are deterministic for a given method and the goal is to match the published results.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "pristine_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "a": "float (angstrom)",
          "b": "float (angstrom)",
          "c": "float (angstrom)",
          "volume": "float (angstrom^3)",
          "band_gap": "float (eV)"
        },
        "items": {},
        "required_columns": [],
        "units": {
          "a": "angstrom",
          "b": "angstrom",
          "c": "angstrom",
          "volume": "angstrom^3",
          "band_gap": "eV"
        }
      },
      "description": "Pristine V2O5 relaxed structure and band gap from PBE+U+D2 calculation."
    },
    {
      "file": "mn_sub_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "delta_volume_pct": "float (%)",
          "magnetization_muB": "float (muB)"
        },
        "items": {},
        "required_columns": [],
        "units": {
          "delta_volume_pct": "%",
          "magnetization_muB": "muB"
        }
      },
      "description": "Volume change and magnetization for substitutional Mn-doped V2O5."
    },
    {
      "file": "mn_int_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "delta_volume_pct": "float (%)",
          "magnetization_muB": "float (muB)"
        },
        "items": {},
        "required_columns": [],
        "units": {
          "delta_volume_pct": "%",
          "magnetization_muB": "muB"
        }
      },
      "description": "Volume change and magnetization for interstitial Mn-doped V2O5."
    }
  ],
  "notes": "Scoring compares the agent's reported values for lattice parameters, band gap, volume changes, and magnetizations against the paper's reported or experimental reference values within pre-defined tolerances. The target policy is exact_match with tolerance because these physical quantities are deterministic for a given method and the goal is to match the published results."
}
```

## How you are scored
A hidden verifier independently checks each of the three result files. For pristine V2O5, it compares your reported lattice parameters and band gap against reference values obtained from PBE+U+D2 calculations performed with the chosen method. For the doped cells, it compares your reported volume change and magnetization against reference results for Mn substitutional and interstitial doping. The verifier uses tolerances that account for numerical noise and implementation differences while still requiring a genuine DFT relaxation to match. Each artifact is scored individually, and the scores are combined with appropriate weights to give a final reward between 0 and 1. Simply guessing or reporting arbitrary numbers will not pass the verifier; only a correct series of DFT calculations can produce outputs that fall within the tolerances.
