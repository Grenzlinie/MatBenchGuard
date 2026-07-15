# DFT calculation of electronic structure and ferroelectric properties of a polar oxide semiconductor

## Problem background
The compound SrNb₂V₂O₁₁ is a polar oxide that has drawn attention as a potential visible‑light‑absorbing piezoelectric semiconductor. Understanding its electronic structure, dielectric response, and spontaneous polarization is crucial for assessing its suitability for ferroelectric and photoferroelectric applications. In this task, you will determine these properties from first‑principles density functional theory (DFT) using the published crystal structure.

## Approach
The crystal structure of SrNb₂V₂O₁₁ adopts the monoclinic polar space group Cc (No. 9). The experimentally determined lattice parameters and fractional coordinates are:

  - a = 18.15415 Å, b = 5.52811 Å, c = 9.52728 Å, β = 99.8033°

Atomic positions (fractional coordinates, all sites fully occupied):

  Nb1  0.42347  0.25051  0.60796
  Nb2  0.31243  0.25033  0.23605
  V1   0.02557  0.23534  0.45970
  V2   0.71160  0.26242  0.35404
  Sr1  0.11792  0.29700  0.13150
  O1  –0.00283  0.04554  0.02040
  O2   0.35442  0.2570   0.42677
  O3   0.36437  0.0253   0.69120
  O4   0.11551  0.25691  0.51576
  O5   0.48693  0.0200   0.0392
  O6   0.22517  0.03366  0.27542
  O7   0.38121  0.4663   0.17303
  O8   0.25330  0.2454   0.02836
  O9   0.01044  0.2483   0.27445
  O10  0.24153  0.5273   0.261
  O11  0.62489  0.23024  0.35765

You will use an open‑source plane‑wave DFT code (e.g., Quantum ESPRESSO) with the PBEsol exchange‑correlation functional and norm‑conserving pseudopotentials. The workflow is:
  1. Fully relax the cell parameters and ionic positions until forces are converged.
  2. Compute the electronic band structure and extract the direct band gap at the Γ point.
  3. Perform a DFPT calculation at Γ to obtain the phonon frequencies.
  4. From the same DFPT run, obtain the Born effective charges and, together with the phonon frequencies, compute the static dielectric tensor; report its isotropic average ε_iso.
  5. Calculate the spontaneous polarization using the Berry‑phase formalism, referencing a centrosymmetric C2/c structure that can be derived from the given Cc coordinates by removing the polar distortion.

Note that a suitable norm‑conserving pseudopotential library (e.g., SSSP efficiency) is publicly available, and the agent is responsible for choosing sensible convergence parameters (k‑mesh, plane‑wave cutoff, force thresholds) that are typical for such oxide systems.

## Reproduction target
The goal is to produce four output files for the relaxed SrNb₂V₂O₁₁ Cc structure:
  - The direct electronic band gap at the Γ point, in eV (floating‑point number).
  - A list of Γ‑point phonon frequencies, one per line in cm⁻¹; any imaginary frequency is reported as a negative number.
  - The isotropic static dielectric constant ε_iso (dimensionless floating‑point number).
  - The magnitude of the spontaneous polarization, in μC cm⁻² (floating‑point number).
These quantities must be obtained from the DFT workflow described above and written to the specified output files exactly as described in the workflow steps.

## Assets

- Quantum ESPRESSO (or any open‑source plane‑wave DFT code supporting PBEsol and DFPT): https://www.quantum-espresso.org/
- Norm‑conserving pseudopotentials for Sr, Nb, V, O (e.g., SSSP efficiency library, PseudoDojo): https://www.materialscloud.org/discover/sssp/table/efficiency

## Workflow steps

### Step 1: DFT geometry optimization
- Role: process
- Action: Using the atomic coordinates and lattice parameters of the polar Cc structure provided in the instructions, perform a full DFT geometry relaxation (cell parameters and ionic positions) with the PBEsol functional and norm‑conserving pseudopotentials. Convergence criterion: forces below a reasonable threshold.
- Evidence: `/app/outputs/geom_opt.log`

### Step 2: Electronic band gap at Γ
- Role: scored
- Action: From the relaxed structure, compute the electronic band structure along high‑symmetry lines and extract the direct band gap at the Γ point. Write the band gap value in eV as a single floating‑point number.
- Output file: `/app/outputs/step_01_bandgap.txt`
- Format: txt
- Contract: A single floating‑point number (eV).
- Scoring: scored by hidden verifier

### Step 3: Γ‑point phonon frequencies
- Role: scored
- Action: Perform a density‑functional perturbation theory (DFPT) calculation at the Γ point on the relaxed structure to obtain the phonon frequencies. Write one frequency per line (in cm⁻¹), representing any imaginary frequencies as negative numbers.
- Output file: `/app/outputs/phonon_frequencies.txt`
- Format: txt
- Contract: One frequency per line (floating‑point numbers); imaginary frequencies as negative numbers.
- Scoring: scored by hidden verifier

### Step 4: Static dielectric constant
- Role: scored (load-bearing)
- Action: Using the Born effective charges and phonon frequencies from the DFPT results, compute the static dielectric tensor and its isotropic average ε_iso. Write ε_iso as a dimensionless floating‑point number.
- Output file: `/app/outputs/step_02_dielectric.txt`
- Format: txt
- Contract: A single floating‑point number (dimensionless).
- Scoring: scored by hidden verifier

### Step 5: Spontaneous polarization
- Role: scored
- Action: Calculate the spontaneous polarization of the relaxed polar Cc structure using the Berry phase formalism (or via Born effective charges and atomic displacements referenced to a centrosymmetric C2/c structure). Write the polarization magnitude in μC cm⁻² as a single floating‑point number.
- Output file: `/app/outputs/step_03_polarization.txt`
- Format: txt
- Contract: A single floating‑point number (μC cm⁻²).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_bandgap.txt`
- `/app/outputs/phonon_frequencies.txt`
- `/app/outputs/step_02_dielectric.txt`
- `/app/outputs/step_03_polarization.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_bandgap.txt
- path: `/app/outputs/step_01_bandgap.txt`
- format: txt
- purpose: scored
- target_policy: reference_match
- description: DFT direct band gap at Γ, eV.
- schema:
  - `type`: text
  - `units`: eV

### phonon_frequencies.txt
- path: `/app/outputs/phonon_frequencies.txt`
- format: txt
- purpose: scored
- target_policy: structural_audit
- description: Phonon frequencies at Γ, one per line, imaginary frequencies as negative numbers.
- schema:
  - `type`: text
  - `units`: cm⁻¹

### step_02_dielectric.txt
- path: `/app/outputs/step_02_dielectric.txt`
- format: txt
- purpose: scored
- target_policy: reference_match
- description: Isotropic static dielectric constant ε_iso.
- schema:
  - `type`: text
  - `units`: dimensionless

### step_03_polarization.txt
- path: `/app/outputs/step_03_polarization.txt`
- format: txt
- purpose: scored
- target_policy: reference_match
- description: Spontaneous polarization magnitude.
- schema:
  - `type`: text
  - `units`: μC cm⁻²

Notes: All scored outputs are compared against the paper's reported values within tolerances that account for DFT code and pseudopotential differences. The phonon frequency file is audited for the absence of imaginary modes.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_bandgap.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "text",
        "units": "eV"
      },
      "description": "DFT direct band gap at Γ, eV."
    },
    {
      "file": "phonon_frequencies.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "text",
        "units": "cm⁻¹"
      },
      "description": "Phonon frequencies at Γ, one per line, imaginary frequencies as negative numbers."
    },
    {
      "file": "step_02_dielectric.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "text",
        "units": "dimensionless"
      },
      "description": "Isotropic static dielectric constant ε_iso."
    },
    {
      "file": "step_03_polarization.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "text",
        "units": "μC cm⁻²"
      },
      "description": "Spontaneous polarization magnitude."
    }
  ],
  "notes": "All scored outputs are compared against the paper's reported values within tolerances that account for DFT code and pseudopotential differences. The phonon frequency file is audited for the absence of imaginary modes."
}
```

## How you are scored
A hidden verifier will independently score each of the four output files. The scalar outputs (bandgap, ε_iso, polarization) will be compared against a hidden reference that represents the expected physical result from a correct DFT calculation at the same level of theory. Agreement within a tolerance that accounts for typical differences between DFT codes, pseudopotentials, and numerical choices is required to earn full credit. The phonon frequency list will be checked for the absence of negative (imaginary) frequencies, which confirms dynamical stability. The overall reward is a weighted combination of the scores from these individual checks. Merely reporting a numeric value without having performed the required DFT computation will not yield a high score, because the verifier's reference is based on the actual physical output of a properly conducted run.
