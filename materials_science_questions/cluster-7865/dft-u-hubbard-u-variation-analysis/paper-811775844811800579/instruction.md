# DFT+U Energy Differences and Orbital Order in STO/SVO Heterostructures

## Problem background
In perovskite oxide heterostructures composed of alternating SrTiO3 (STO) and SrVO3 (SVO) layers, the interplay of electron correlation, tetragonal strain, and spin-orbit coupling (SOC) can drive a competition between different orbital and magnetic orders. As the thickness of the SVO layers increases, the system is predicted to undergo an insulator-to-metal transition. First-principles density functional theory calculations with a Hubbard U correction and SOC can be used to evaluate the relative stability of competing states—such as an alternating-orbital-order ferromagnetic state (AOO FM) versus a d_xy orbital-ordered antiferromagnetic state (Néel AF)—and to characterize the resulting electronic structure (band gaps, orbital moments). The goal is to compute these energetic and electronic properties for (001)-oriented SrTiO3(4 layers)/SrVO3(n layers) superlattices with n=1..5.

## Approach
The computational workflow proceeds in two stages. First, structural relaxations are performed for each superlattice (n=1 to 5) using the GGA-PBE exchange-correlation functional. The in-plane lattice constant is fixed to the experimental STO value of 3.905 Å, a c(2×2) in-plane supercell is used to allow for antiferromagnetic and orbital orderings, and the c lattice parameter and all internal atomic coordinates are relaxed. Second, the relaxed structures are used as input for static DFT+U calculations including SOC. The Hubbard U and Hund’s J parameters on the V 3d states are set to U=4.5 eV and J=0.7 eV. For each n, total energy calculations are carried out for the following magnetic/orbital configurations:
- n=1: AOO FM and d_xy Néel AF.
- n=2: AOO FM and d_xy Néel AF.
- n=3: AOO FM with two types of interlayer alignment (AAA and ABA).
- n=4 and n=5: AOO FM (to obtain band gaps).
From these calculations, the total energies, band structures, and the orbital moment on the d_- sublattice (for n=1 AOO FM) are extracted. The energy differences per V atom are then computed and recorded.

## Reproduction target
This task aims to reproduce six specific numerical quantities from the DFT+U+SOC calculations, and to store each as a plain text file under /app/outputs:
1. The total energy difference per V atom between the AOO FM and d_xy Néel AF states for n=1 (in meV/V) → n1_energy_diff.txt.
2. The analogous energy difference for n=2 → n2_energy_diff.txt.
3. The total energy difference per V atom between the AAA and ABA interlayer alignments of the AOO FM state for n=3 (in meV/V) → n3_energy_diff.txt.
4. The minimum direct band gap at Γ for the n=4 AOO FM state (in eV) → n4_band_gap.txt.
5. The minimum direct band gap at Γ for the n=5 AOO FM state (in eV) → n5_band_gap.txt.
6. The orbital moment on the d_- sublattice for the n=1 AOO FM state (in µB) → n1_orbital_moment.txt.
The verifier will judge whether the reproduced numbers are consistent with the expected physical behavior (e.g., insulating vs metallic for the band gaps) by comparing against hidden reference values.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP efficiency pseudopotentials (Sr, Ti, V, O): https://www.materialscloud.org/discover/sssp/package/efficiency

## Workflow steps

### Step 1: Structural relaxation of superlattices
- Role: process
- Action: Use GGA-PBE to relax the c lattice parameter and internal coordinates of (SrTiO3)4/(SrVO3)n (001) superlattices for n=1..5, fixing the in-plane lattice constant to 3.905 Å and employing a c(2×2) in-plane supercell. Produce the relaxed structures.
- Evidence: `/app/outputs/relaxation.log`

### Step 2: DFT+U+SOC total energy and band structure calculations
- Role: process
- Action: For each relaxed structure, perform static LDA+U (U_V=4.5 eV, J_V=0.7 eV) calculations with spin-orbit coupling for the following configurations: (i) n=1 AOO FM and n=1 d_xy Néel AF, (ii) n=2 AOO FM and n=2 d_xy AF, (iii) n=3 AOO FM with AAA and ABA interlayer order, (iv) n=4 AOO FM, (v) n=5 AOO FM. Obtain total energies, band structures, and for n=1 AOO FM, the orbital moment on the d_- sublattice. Save all raw outputs.
- Evidence: none

### Step 3: Energy difference for n=1
- Role: scored
- Action: Compute the total energy difference ΔE = E(AOO FM) - E(d_xy Néel AF) per V atom for n=1 (in meV/V) from the DFT outputs and write the number to n1_energy_diff.txt.
- Output file: `/app/outputs/n1_energy_diff.txt`
- Format: txt
- Contract: A single floating-point number (meV/V).
- Scoring: scored by hidden verifier

### Step 4: Energy difference for n=2
- Role: scored
- Action: Compute the total energy difference ΔE = E(FM AOO) - E(d_xy AF) per V atom for n=2 (in meV/V) from the DFT outputs and write the number to n2_energy_diff.txt.
- Output file: `/app/outputs/n2_energy_diff.txt`
- Format: txt
- Contract: A single floating-point number (meV/V).
- Scoring: scored by hidden verifier

### Step 5: Energy difference for n=3 (interlayer alignment)
- Role: scored
- Action: Compute the total energy difference ΔE = E(AAA) - E(ABA) per V atom for n=3 (in meV/V) from the DFT outputs and write the number to n3_energy_diff.txt.
- Output file: `/app/outputs/n3_energy_diff.txt`
- Format: txt
- Contract: A single floating-point number (meV/V).
- Scoring: scored by hidden verifier

### Step 6: Band gap for n=4
- Role: scored
- Action: Determine the minimum direct band gap at Γ for the n=4 AOO FM state (in eV) and write the number to n4_band_gap.txt. If the state is metallic, write 0.0.
- Output file: `/app/outputs/n4_band_gap.txt`
- Format: txt
- Contract: A single floating-point number (eV).
- Scoring: scored by hidden verifier

### Step 7: Band gap for n=5
- Role: scored
- Action: Determine the minimum direct band gap at Γ for the n=5 AOO FM state (in eV) and write the number to n5_band_gap.txt. If the state is metallic (gap ≤ 0.1 eV), write 0.0.
- Output file: `/app/outputs/n5_band_gap.txt`
- Format: txt
- Contract: A single floating-point number (eV).
- Scoring: scored by hidden verifier

### Step 8: Orbital moment on d_- sublattice for n=1
- Role: scored (load-bearing)
- Action: Extract the orbital moment (in μB) on the d_- sublattice from the SOC calculation of the n=1 AOO FM state and write it to n1_orbital_moment.txt.
- Output file: `/app/outputs/n1_orbital_moment.txt`
- Format: txt
- Contract: A single floating-point number (μB).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/n1_energy_diff.txt`
- `/app/outputs/n2_energy_diff.txt`
- `/app/outputs/n3_energy_diff.txt`
- `/app/outputs/n4_band_gap.txt`
- `/app/outputs/n5_band_gap.txt`
- `/app/outputs/n1_orbital_moment.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### n1_energy_diff.txt
- path: `/app/outputs/n1_energy_diff.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: Energy difference for n=1 between AOO FM and d_xy AF states.
- schema:
  - `type`: text
  - `description`: A single floating-point number (meV/V).

### n2_energy_diff.txt
- path: `/app/outputs/n2_energy_diff.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: Energy difference for n=2 between FM AOO and d_xy AF states.
- schema:
  - `type`: text
  - `description`: A single floating-point number (meV/V).

### n3_energy_diff.txt
- path: `/app/outputs/n3_energy_diff.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: Energy difference for n=3 between AAA and ABA interlayer alignments.
- schema:
  - `type`: text
  - `description`: A single floating-point number (meV/V).

### n4_band_gap.txt
- path: `/app/outputs/n4_band_gap.txt`
- format: txt
- purpose: scored
- target_policy: threshold_or_better
- description: Band gap for n=4 AOO FM state; expected to be insulating (>0.1 eV).
- schema:
  - `type`: text
  - `description`: A single floating-point number (eV).

### n5_band_gap.txt
- path: `/app/outputs/n5_band_gap.txt`
- format: txt
- purpose: scored
- target_policy: threshold_or_better
- description: Band gap for n=5 AOO FM state; expected to be metallic (≤0.1 eV).
- schema:
  - `type`: text
  - `description`: A single floating-point number (eV).

### n1_orbital_moment.txt
- path: `/app/outputs/n1_orbital_moment.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: Orbital moment on the d_- sublattice for the n=1 AOO FM state.
- schema:
  - `type`: text
  - `description`: A single floating-point number (μB).

Notes: The scoring checks the six numerical values against hidden reference values from the original work. Energy differences and the orbital moment are compared within a tolerance (exact_match with tolerance). Band gaps are evaluated as threshold_or_better: n4 must be >0.1 eV (insulating) and n5 must be ≤0.1 eV (metallic).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "n1_energy_diff.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "description": "A single floating-point number (meV/V)."
      },
      "description": "Energy difference for n=1 between AOO FM and d_xy AF states."
    },
    {
      "file": "n2_energy_diff.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "description": "A single floating-point number (meV/V)."
      },
      "description": "Energy difference for n=2 between FM AOO and d_xy AF states."
    },
    {
      "file": "n3_energy_diff.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "description": "A single floating-point number (meV/V)."
      },
      "description": "Energy difference for n=3 between AAA and ABA interlayer alignments."
    },
    {
      "file": "n4_band_gap.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "text",
        "description": "A single floating-point number (eV)."
      },
      "description": "Band gap for n=4 AOO FM state; expected to be insulating (>0.1 eV)."
    },
    {
      "file": "n5_band_gap.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "text",
        "description": "A single floating-point number (eV)."
      },
      "description": "Band gap for n=5 AOO FM state; expected to be metallic (≤0.1 eV)."
    },
    {
      "file": "n1_orbital_moment.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "description": "A single floating-point number (μB)."
      },
      "description": "Orbital moment on the d_- sublattice for the n=1 AOO FM state."
    }
  ],
  "notes": "The scoring checks the six numerical values against hidden reference values from the original work. Energy differences and the orbital moment are compared within a tolerance (exact_match with tolerance). Band gaps are evaluated as threshold_or_better: n4 must be >0.1 eV (insulating) and n5 must be ≤0.1 eV (metallic)."
}
```

## How you are scored
A hidden verifier reads each of the six output files, parses the numerical value, and compares it against a hidden reference derived from the original study. Each quantity is evaluated according to its nature:
- Energy differences (n1, n2, n3) are compared to a reference value within a tolerance.
- The orbital moment (n1_orbital_moment) is compared to a reference within a tolerance.
- Band gaps (n4, n5) are checked against a threshold: the verifier determines whether the gap correctly indicates an insulator or a metal according to the hidden criterion.

The six scored artifacts carry equal weight, each contributing 1/6 of the total reward. Meeting or exceeding the required accuracy/threshold earns full credit for that artifact; otherwise partial credit may be assigned. The final reward is the weighted sum. Simply reporting a number without actually running the DFT calculations is likely to produce an incorrect value and will not pass the verification. The verifier does not inspect intermediate files or the raw DFT outputs; it only checks the contents of the six specified text files.
