# DFT reproduction of electronic, magnetic, and phonon properties of TlFeSe₂

## Problem background
The cuprate high-temperature superconductors are derived from parent compounds that are layered Néel antiferromagnetic Mott insulators with strong in-plane superexchange. Finding compounds with similar crystal and electronic structures, but without copper, could help unify the understanding of unconventional superconductivity. Ternary iron selenides AFeSe₂ (A=Tl,K,Rb,Cs) with the I4̅m2 structure contain FeSe₂ layers resembling the CuO₂ planes of cuprates and have been proposed as potential cuprate analogs. This task focuses on TlFeSe₂ and aims to determine computationally whether it exhibits a Néel antiferromagnetic insulating ground state, a robust nearest-neighbor superexchange coupling, and dynamical lattice stability – key properties for a parent compound of high-temperature superconductivity.

## Approach
The approach uses first-principles density functional theory (DFT) with the plane-wave code Quantum ESPRESSO. The electronic interactions are described at the generalized gradient approximation level (GGA-PBE) using ultrasoft pseudopotentials. A magnetic supercell is constructed by doubling the crystallographic unit cell along the a′ and b′ axes to accommodate the Néel antiferromagnetic order. After relaxing the structure in this magnetic state, total energies are computed for four collinear spin configurations: ferromagnetic, Néel antiferromagnetic, collinear antiferromagnetic, and bicollinear antiferromagnetic. These energies are mapped onto a Heisenberg model with first-, second-, and third-neighbor interactions to extract the nearest-neighbor exchange constant J₁. A dense k-point electronic structure calculation in the Néel ground state yields the indirect band gap. Independently, the phonon dispersion of nonmagnetic TlFeSe₂ is calculated using density functional perturbation theory (DFPT) to assess the presence of any imaginary modes, which would indicate dynamical instability.

## Reproduction target
Produce the following outputs for TlFeSe₂, all written to `/app/outputs`:
- `j1_value_tl_fese2.txt`: a single floating-point number – the nearest-neighbor Heisenberg exchange constant J₁, in units of meV/S², extracted from the total energy differences of the four magnetic configurations.
- `band_gap_tl_fese2.txt`: a single floating-point number – the indirect band gap of the Néel antiferromagnetic state, in meV.
- `phonon_stability_tl_fese2.txt`: a single line containing either 'stable' or 'unstable', reflecting whether the nonmagnetic phonon dispersion shows no imaginary modes (or none below -5 cm⁻¹).

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- Ultrasoft pseudopotentials (GGA‑PBE) for Fe, Se, Tl: https://www.materialscloud.org/discover/sssp/table/efficiency
- Crystal structure of TlFeSe₂ (space group I4̅m2)

## Workflow steps

### Step 1: Structural relaxation of TlFeSe₂ in Néel AFM state
- Role: process
- Action: Using the experimental crystal structure (I4̅m2), perform DFT structure optimization in the Néel antiferromagnetic state with Quantum ESPRESSO, GGA-PBE. The magnetic unit cell is doubled along a′ and b′ axes.
- Evidence: `/app/outputs/relax.log`

### Step 2: Total energy calculations for magnetic configurations
- Role: process
- Action: On the relaxed structure, compute total energies for ferromagnetic, Néel AFM, collinear AFM, and bicollinear AFM spin arrangements using the same DFT settings. Record the total energy of each configuration.
- Evidence: `/app/outputs/magnetic_energies.txt`

### Step 3: Extract J₁ exchange coupling constant
- Role: scored (load-bearing)
- Action: From the total energies of the four magnetic configurations, solve the linear equations of the Heisenberg model to obtain the nearest-neighbor exchange constant J₁ (in meV/S²). Write the result as a single number to j1_value_tl_fese2.txt.
- Output file: `/app/outputs/j1_value_tl_fese2.txt`
- Format: txt
- Contract: A single line containing a floating-point value in meV/S².
- Scoring: scored by hidden verifier

### Step 4: DFT electronic structure in AFM ground state
- Role: process
- Action: Perform a self-consistent DFT calculation on the Néel AFM structure using a dense k-mesh to obtain the band structure and density of states, allowing identification of the indirect gap.
- Evidence: `/app/outputs/bands.dat`

### Step 5: Report indirect band gap
- Role: scored (load-bearing)
- Action: From the band structure of step4, determine the indirect band gap (in meV) between the highest valence band and lowest conduction band. Write the value to band_gap_tl_fese2.txt.
- Output file: `/app/outputs/band_gap_tl_fese2.txt`
- Format: txt
- Contract: A single line containing the band gap in meV.
- Scoring: scored by hidden verifier

### Step 6: Phonon dispersion calculation for nonmagnetic TlFeSe₂
- Role: process
- Action: Perform a nonmagnetic DFT relaxation of TlFeSe₂, then compute the phonon dispersion and density of states using density functional perturbation theory (DFPT) in Quantum ESPRESSO. Ensure the computation covers high-symmetry directions to capture any imaginary modes.
- Evidence: `/app/outputs/phonon_dispersion.dat`

### Step 7: Assess phonon stability
- Role: scored
- Action: Inspect the phonon dispersion from step6: if all phonon frequencies are real (no imaginary modes, or none below -5 cm⁻¹), write 'stable' to phonon_stability_tl_fese2.txt; otherwise write 'unstable'.
- Output file: `/app/outputs/phonon_stability_tl_fese2.txt`
- Format: txt
- Contract: A single line: either 'stable' or 'unstable'.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/j1_value_tl_fese2.txt`
- `/app/outputs/band_gap_tl_fese2.txt`
- `/app/outputs/phonon_stability_tl_fese2.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### j1_value_tl_fese2.txt
- path: `/app/outputs/j1_value_tl_fese2.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: Nearest-neighbor exchange coupling constant J₁ extracted from DFT total energies of magnetic configurations.
- schema:
  - `type`: text
  - `description`: A single line containing a floating-point value in meV/S².

### band_gap_tl_fese2.txt
- path: `/app/outputs/band_gap_tl_fese2.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: Indirect charge excitation gap of TlFeSe₂ in the Néel AFM ground state.
- schema:
  - `type`: text
  - `description`: A single line containing the band gap in meV.

### phonon_stability_tl_fese2.txt
- path: `/app/outputs/phonon_stability_tl_fese2.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: Phonon stability verdict based on absence of imaginary frequencies in nonmagnetic TlFeSe₂.
- schema:
  - `type`: text
  - `description`: A single line: 'stable' or 'unstable'.

Notes: Only TlFeSe₂ is targeted; other alkali variants are omitted. The SCAN meta‑GGA cross‑check and charge/spin density visualisation are omitted as they are not essential to the main quantified claim. The agent must obtain the initial crystal structure from public databases (ICSD or published CIFs).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "j1_value_tl_fese2.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "description": "A single line containing a floating-point value in meV/S²."
      },
      "description": "Nearest-neighbor exchange coupling constant J₁ extracted from DFT total energies of magnetic configurations."
    },
    {
      "file": "band_gap_tl_fese2.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "description": "A single line containing the band gap in meV."
      },
      "description": "Indirect charge excitation gap of TlFeSe₂ in the Néel AFM ground state."
    },
    {
      "file": "phonon_stability_tl_fese2.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "description": "A single line: 'stable' or 'unstable'."
      },
      "description": "Phonon stability verdict based on absence of imaginary frequencies in nonmagnetic TlFeSe₂."
    }
  ],
  "notes": "Only TlFeSe₂ is targeted; other alkali variants are omitted. The SCAN meta‑GGA cross‑check and charge/spin density visualisation are omitted as they are not essential to the main quantified claim. The agent must obtain the initial crystal structure from public databases (ICSD or published CIFs)."
}
```

## How you are scored
A hidden verifier checks each output independently against a hidden reference. The band gap and J₁ are compared to reference values with appropriate tolerances that account for legitimate computational spread (different pseudopotential versions, numerical settings). The phonon stability string is compared to the expected outcome derived from a reference DFPT calculation. Each output contributes a partial score, and the final reward is the weighted sum: band gap 40%, J₁ 40%, phonon stability 20%. Simply reporting literature numbers without running the calculations is insufficient because the verifier's reference is designed to accept correct results obtained under real, potentially variable, computation conditions.
