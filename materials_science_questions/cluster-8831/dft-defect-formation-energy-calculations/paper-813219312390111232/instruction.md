# DFT Formation Energy of S2 Substitution at MoS2 Grain Boundary

## Problem background
Understanding the stability and atomic-scale structure of grain boundaries in two-dimensional transition metal dichalcogenides such as MoS2 is essential for predicting and optimizing their electronic and mechanical behavior. A key quantity that determines whether certain atomic configurations are favored at grain boundary cores is the formation energy of sulfur substitution (S2 replacing a Mo atom) at dislocation sites. In this task we compute, using first-principles density functional theory (DFT), the formation energy for an S2 substitution at a Mo-oriented 5|7 dislocation core with ~21° tilt angle in monolayer MoS2. The energy is evaluated under S-rich conditions and provides insight into the boundary's thermodynamic stability.

## Approach
The computational approach employs DFT within the local density approximation (LDA) and the projector-augmented wave (PAW) method, as available in several open-source DFT codes. A periodic atomic model of the grain boundary is constructed with the specified tilt angle and supercell dimensions; a vacuum layer separates periodic images perpendicular to the plane. Two total energy calculations are performed: one for the pristine Mo-oriented 5|7 grain boundary and one for the same boundary in which a S2 dimer replaces a Mo atom at the dislocation core. The formation energy is obtained from the difference of these total energies, corrected for the change in atomic species using chemical potentials. The chemical potential of sulfur is taken as that of bulk sulfur (S-rich limit). The calculations use a plane-wave basis with an energy cutoff of 280 eV and a Γ-centered 1×3×1 Monkhorst-Pack k-point mesh, relaxing until atomic forces fall below a convergence threshold. The outcome is a single floating-point formation energy (in eV) that characterizes the substitution.

## Reproduction target
Compute the formation energy (in eV) for S2 substitution at the Mo-oriented 5|7 grain boundary in monolayer MoS2 with ~21° tilt angle under S-rich conditions, following the protocol described in the workflow steps. Report the resulting energy as a single float (up to three decimal places) on the first line of `/app/outputs/substitution_formation_energy.txt`.

## Assets

- Open-source DFT software (e.g., Quantum ESPRESSO, ABINIT, GPAW) with LDA pseudopotentials: https://www.quantum-espresso.org/

## Workflow steps

### Step 1: Generate atomic model of MoS2 grain boundary
- Role: process
- Action: Construct the atomic structure of a monolayer MoS2 grain boundary with a Mo-oriented 5|7 dislocation core, tilt angle ~21°, in-plane supercell dimensions approximately 34 Å (perpendicular to GB) × 11 Å (along GB), and a vacuum layer of 12 Å. Write the atomic coordinates to a file in a format suitable for the chosen DFT software.
- Evidence: `/app/outputs/gb_structure.dat`

### Step 2: Compute formation energy of S2 substitution
- Role: scored (load-bearing)
- Action: Using the grain boundary structure from the previous step, perform DFT total energy calculations with the local density approximation (LDA) and the projector-augmented wave (PAW) method (or an open-source equivalent). Calculate the total energy for the unsubstituted Mo-oriented 5|7 grain boundary (E_Mo-5|7) and for the configuration where a S2 replaces a Mo at the dislocation core (E_S2-sub). Compute the formation energy E_f = E_S2-sub - E_Mo-5|7 - Δn_Mo μ_Mo - Δn_S μ_S under S-rich conditions (μ_S = chemical potential of bulk sulfur). Write the resulting formation energy, in electron volts, to the output file.
- Output file: `/app/outputs/substitution_formation_energy.txt`
- Format: txt
- Contract: A single float on the first line, representing the formation energy in eV.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/substitution_formation_energy.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### substitution_formation_energy.txt
- path: `/app/outputs/substitution_formation_energy.txt`
- format: txt
- purpose: scored
- target_policy: reference_match
- description: Computed formation energy for S2 substitution at the grain boundary.
- schema:
  - `type`: text
  - `content_type`: float
  - `units`: eV
  - `description`: The file contains a single float on the first line, representing the formation energy for S2 substitution at the Mo-oriented 5|7 grain boundary in eV.

Notes: The hidden checker compares the reported formation energy to the paper's reported DFT value using an appropriate absolute tolerance to account for legitimate differences between DFT implementations.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "substitution_formation_energy.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "text",
        "content_type": "float",
        "units": "eV",
        "description": "The file contains a single float on the first line, representing the formation energy for S2 substitution at the Mo-oriented 5|7 grain boundary in eV."
      },
      "description": "Computed formation energy for S2 substitution at the grain boundary."
    }
  ],
  "notes": "The hidden checker compares the reported formation energy to the paper's reported DFT value using an appropriate absolute tolerance to account for legitimate differences between DFT implementations."
}
```

## How you are scored
A hidden verifier reads your reported formation energy from `substitution_formation_energy.txt` and compares it to a reference value derived from the published DFT result. The comparison uses an absolute tolerance that accounts for legitimate numerical spread arising from different DFT implementations (e.g., pseudopotential choice, k-point integration). If your computed energy is within tolerance of the reference, you receive full credit for this stage. Process‑step evidence files are not individually scored but are expected to be present. The final reward is a float between 0 and 1 reflecting the overall reproduction quality.
