# Interaction energy between Gd substitution and oxygen vacancy in monoclinic HfO2 from DFT

## Problem background
Monoclinic HfO₂ (m-HfO₂) is a high-κ dielectric material widely studied for gate oxides in CMOS devices and for resistive switching memories. Its electrical properties are strongly influenced by oxygen vacancies (V_O), which introduce defect states inside the band gap. Incorporating trivalent dopants such as gadolinium (Gd) is a common strategy to tailor defect behavior, but the effect of Gd on oxygen vacancies remains debated: some studies suggest Gd suppresses vacancy formation, while others find it lower formation energies and increases vacancy concentration.

A key quantity that quantifies the interplay between a substitutional Gd at a Hf site (Gd_Hf) and an oxygen vacancy is the *interaction energy* E_int. A negative value indicates attractive interaction (the defects prefer to bind), whereas a positive value indicates repulsion. Determining this interaction energy is essential for understanding whether Gd passivates defect states and how it modifies the formation of oxygen vacancies.

## Approach
We use spin-polarized density functional theory (DFT) at the generalized gradient approximation level with a Hubbard U correction on the Gd 4f orbitals (GGA+U) to evaluate the total energies of several supercell configurations. The approach follows a supercell defect calculation strategy:

1. Build a 2×2×2 supercell of monoclinic HfO₂ (96 atoms) with the experimental lattice parameters.
2. Relax the defect-free (perfect) supercell to obtain its total energy.
3. Introduce single point defects: one Gd atom substituting a Hf atom (Gd_Hf), and one oxygen vacancy at a four-coordinated oxygen site (V_O₄). Relax each defect structure separately and record the total energies.
4. Create a complex defect by removing the three-coordinated oxygen atom closest to the Gd atom in the relaxed Gd_Hf supercell; relax this Gd_Hf + V_O complex and record its total energy.
5. From the four total energies, compute the interaction energy E_int = E(complex) + E(perfect) – E(Gd_Hf) – E(V_O₄).

All calculations use the PBE exchange-correlation functional with a plane-wave cutoff of 500 eV, a 2×2×2 k‑point mesh, and a force convergence of <0.01 eV/Å. The open‑source code Quantum ESPRESSO and the SSSP efficiency pseudopotentials (version 1.3) serve as the computational engine.

## Reproduction target
Your goal is to carry out the five DFT calculations described above and to output a single file `/app/outputs/results.json` containing the four total energies (perfect, Gd_Hf, V_O₄, complex) and the interaction energy E_int computed from them. The energies must derive from the structural relaxations you perform; do not look up pre‑existing numbers. The file must be a JSON object with the following keys, all in units of eV:

- `total_energy_perfect`
- `total_energy_Gd_Hf`
- `total_energy_V_O4`
- `total_energy_complex`
- `interaction_energy_E_int`

You may use any workflow orchestration you prefer, but the final output must be exactly this file at this path.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP efficiency pseudopotentials v1.3 (PBE, Hf, O, Gd): https://www.materialscloud.org/discover/sssp/table/efficiency

## Workflow steps

### Step 1: Perfect supercell relaxation
- Role: process
- Action: Construct a 96-atom supercell (2x2x2) of monoclinic HfO2 from the published lattice parameters. Perform structural relaxation (atomic positions only) with spin-polarized GGA (PBE) using a plane-wave cutoff of 500 eV and a 2x2x2 k-point mesh. Record the total energy in a JSON file.
- Evidence: `/app/outputs/perfect_energy.json`

### Step 2: Gd_Hf defect relaxation
- Role: process
- Action: In the relaxed perfect supercell, replace one Hf atom with a Gd atom to create a substitutional Gd_Hf defect. Relax the structure with spin-polarized GGA+U (U=7.5 eV, J=0.6 eV on Gd 4f), same cutoff and k-points. Record the total energy in a JSON file.
- Evidence: `/app/outputs/gd_hf_energy.json`

### Step 3: V_O4 defect relaxation
- Role: process
- Action: In the relaxed perfect supercell, remove one four-coordinated oxygen (O4) atom to create an oxygen vacancy V_O4. Relax the structure with spin-polarized GGA (no Gd, so GGA), same cutoff and k-points. Record the total energy in a JSON file.
- Evidence: `/app/outputs/v_o4_energy.json`

### Step 4: Complex defect relaxation
- Role: process
- Action: Starting from the relaxed Gd_Hf supercell, identify the nearest three-coordinated oxygen (O3) to the Gd atom and remove it to form the Gd_Hf+V_O complex. Relax the structure with spin-polarized GGA+U (same settings). Record the total energy in a JSON file.
- Evidence: `/app/outputs/complex_energy.json`

### Step 5: Interaction energy calculation
- Role: scored (load-bearing)
- Action: Using the total energies obtained in steps 1–4, compute the interaction energy E_int = E(complex) + E(perfect) - E(Gd_Hf) - E(V_O4). Write all four total energies and the computed E_int to results.json.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: JSON object with keys: total_energy_perfect (float, eV), total_energy_Gd_Hf (float, eV), total_energy_V_O4 (float, eV), total_energy_complex (float, eV), interaction_energy_E_int (float, eV)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results.json
- path: `/app/outputs/results.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Agent's computed total energies and the interaction energy between Gd_Hf and V_O. The hidden checker recomputes E_int from the four total energies, verifies that it is negative, and compares it to an expected range consistent with the paper's result.
- schema:
  - `type`: object
  - `required`:
    - `total_energy_perfect`: float (eV)
    - `total_energy_Gd_Hf`: float (eV)
    - `total_energy_V_O4`: float (eV)
    - `total_energy_complex`: float (eV)
    - `interaction_energy_E_int`: float (eV)
  - `units`:
    - `total_energy_perfect`: eV
    - `total_energy_Gd_Hf`: eV
    - `total_energy_V_O4`: eV
    - `total_energy_complex`: eV
    - `interaction_energy_E_int`: eV

Notes: The checker performs a recompute: it reads the total energies, recomputes E_int = total_energy_complex + total_energy_perfect - total_energy_Gd_Hf - total_energy_V_O4, and scores the sign and magnitude against a hidden gold value. An E_int more negative than the paper's (stronger attraction) is accepted as equal or better.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": {
          "total_energy_perfect": "float (eV)",
          "total_energy_Gd_Hf": "float (eV)",
          "total_energy_V_O4": "float (eV)",
          "total_energy_complex": "float (eV)",
          "interaction_energy_E_int": "float (eV)"
        },
        "units": {
          "total_energy_perfect": "eV",
          "total_energy_Gd_Hf": "eV",
          "total_energy_V_O4": "eV",
          "total_energy_complex": "eV",
          "interaction_energy_E_int": "eV"
        }
      },
      "description": "Agent's computed total energies and the interaction energy between Gd_Hf and V_O. The hidden checker recomputes E_int from the four total energies, verifies that it is negative, and compares it to an expected range consistent with the paper's result."
    }
  ],
  "notes": "The checker performs a recompute: it reads the total energies, recomputes E_int = total_energy_complex + total_energy_perfect - total_energy_Gd_Hf - total_energy_V_O4, and scores the sign and magnitude against a hidden gold value. An E_int more negative than the paper's (stronger attraction) is accepted as equal or better."
}
```

## How you are scored
A hidden verifier will examine your `/app/outputs/results.json`. It will confirm that all five keys are present and contain numeric values. It will independently recompute E_int from the four total energies you submit (to guard against transcription errors). It will then compare this recomputed (or your reported) interaction energy to a reference value obtained from the original study, applying a hidden tolerance that accounts for differences in DFT implementations. The scoring rewards a result that is physically consistent with the paper’s findings: a correct sign and a magnitude close to the expected range earn full credit, while deviations degrade the score gradually. Note that simply reporting a plausible number without actually performing the calculations will not pass the hidden verification steps that check the internal consistency of your submitted total energies.
