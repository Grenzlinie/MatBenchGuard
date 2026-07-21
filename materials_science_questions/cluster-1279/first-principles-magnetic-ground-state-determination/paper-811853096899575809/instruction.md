# DFT reproduction of FM stabilization energies and Fe moments in Fe/Cu codoped In2O3 with oxygen vacancy

## Problem background
In₂O₃ is a transparent semiconducting oxide that, when doped with Fe, can exhibit magnetic ordering. Understanding the factors that stabilize ferromagnetism (FM) over antiferromagnetism (AFM) is crucial for spintronic applications. Both Cu codoping and the presence of oxygen vacancies (VO) have been proposed to affect the magnetic coupling between Fe ions. In this task, you will use first‑principles density‑functional theory (DFT) to compute the FM stabilization energy and Fe magnetic moments for four specific supercell configurations of Fe‑doped In₂O₃, with and without Cu and VO, in order to assess how these additives influence the magnetic ground state.

## Approach
You will construct an 80‑atom cubic bixbyite In₂O₃ supercell and substitute two In atoms with Fe at the second‑nearest‑neighbour (b) configuration. From this base, you will create four systems: Fe‑only (b‑IFO), with a bridging oxygen vacancy between the Fe ions (b‑IFO‑VO), with an additional Cu atom at the Cu1 site adjacent to both Fe ions (b‑IFCO‑i), and with both Cu and vacancy (b‑IFCO‑VO‑i). For each system, perform spin‑polarized DFT geometry optimization using the GGA‑PBE exchange‑correlation functional, then compute total energies for FM and AFM alignment of the Fe spins. Finally, calculate ΔE_FM = E_FM − E_AFM and extract the total and Fe‑projected magnetic moments. The workflow is purely computational; all required structural data and pseudopotentials are publicly available.

## Reproduction target
Produce a CSV file magnetic_results.csv containing the FM stabilization energy (ΔE_FM, in meV) and the total and Fe‑projected magnetic moments (in μB) for each of the four systems in both FM and AFM orderings. The columns are system, delta_EFM_meV, M_total_FM, M_total_AFM, M_Fe1_FM, M_Fe2_FM, M_Fe1_AFM, M_Fe2_AFM. The hidden verifier will compare your values against a reference and also check that the relative ordering of ΔE_FM across the four systems follows the expected physical trend. You do not need to produce any plots or density‑of‑states analysis.

## Assets

- Spin‑polarized DFT package (e.g., Quantum ESPRESSO, CP2K): https://www.quantum-espresso.org/
- Cubic bixbyite In2O3 crystal structure (conventional cell, 80 atoms): mp‑22526, from the Materials Project (structure accessible via pymatgen or direct CIF download)
- GGA-PBE pseudopotentials for In, O, Fe, Cu: https://www.materialscloud.org/discover/sssp/

## Workflow steps

### Step 1: Build supercell and doping configurations
- Role: process
- Action: Construct an 80‑atom conventional cubic bixbyite In2O3 supercell. Substitute two In atoms with Fe at the b configuration (second‑nearest‑neighbour Fe pair, e.g., two In(1) sites separated by [½,½,0]). For b‑IFO‑VO, remove the bridging oxygen atom between the two Fe ions. For b‑IFCO‑i, replace an additional In atom with Cu at the Cu1 position adjacent to both Fe ions. For b‑IFCO‑VO‑i, apply both Cu substitution and bridging‑oxygen removal. Generate initial atomic coordinate files for each of the four systems.
- Evidence: none

### Step 2: DFT geometry optimization
- Role: process
- Action: Perform spin‑polarized DFT structural relaxations for each of the four systems using GGA‑PBE exchange‑correlation. Use a plane‑wave cutoff of at least 500 eV and k‑point sampling no coarser than 3×3×3. Relax atomic positions until forces are below 0.02 eV/Å. Save the relaxed atomic coordinates for each system.
- Evidence: none

### Step 3: Static total‑energy calculations for FM and AFM orderings
- Role: process
- Action: For each relaxed structure, run spin‑polarized static calculations with ferromagnetic (FM) and antiferromagnetic (AFM) alignment of the Fe moments. Use a finer k‑point mesh (e.g., 4×4×4) and tight SCF convergence (10⁻⁶ eV). Save the total energy and projected magnetic moments for each spin configuration.
- Evidence: none

### Step 4: Compute ΔE_FM and magnetic moments, output CSV
- Role: scored (load-bearing)
- Action: From the static total energies, compute ΔE_FM = E_FM − E_AFM for each system. Extract the total magnetic moment and projected magnetic moments on Fe1 and Fe2 in both FM and AFM orderings. Write the results to magnetic_results.csv with columns: system, delta_EFM_meV, M_total_FM, M_total_AFM, M_Fe1_FM, M_Fe2_FM, M_Fe1_AFM, M_Fe2_AFM.
- Output file: `/app/outputs/magnetic_results.csv`
- Format: csv
- Contract: CSV with columns: system (str, one of 'b-IFO','b-IFO-VO','b-IFCO-i','b-IFCO-VO-i'), delta_EFM_meV (float, meV), M_total_FM (float, μB), M_total_AFM (float, μB), M_Fe1_FM (float, μB), M_Fe2_FM (float, μB), M_Fe1_AFM (float, μB), M_Fe2_AFM (float, μB).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/magnetic_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### magnetic_results.csv
- path: `/app/outputs/magnetic_results.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Table of FM stabilisation energies and Fe projected magnetic moments for the four b‑configuration systems.
- schema:
  - `type`: table
  - `required_columns`: `system`, `delta_EFM_meV`, `M_total_FM`, `M_total_AFM`, `M_Fe1_FM`, `M_Fe2_FM`, `M_Fe1_AFM`, `M_Fe2_AFM`
  - `units`:
    - `delta_EFM_meV`: meV
    - `M_total_FM`: μB
    - `M_total_AFM`: μB
    - `M_Fe1_FM`: μB
    - `M_Fe2_FM`: μB
    - `M_Fe1_AFM`: μB
    - `M_Fe2_AFM`: μB

Notes: The checker will compare the ΔE_FM and magnetic moment values in this file against a hidden reference derived from the published data, using appropriate tolerances that account for differences in DFT codes and pseudopotentials. It will also verify that the relative ordering of ΔE_FM across systems is consistent with the expected physical trend.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "magnetic_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "system",
          "delta_EFM_meV",
          "M_total_FM",
          "M_total_AFM",
          "M_Fe1_FM",
          "M_Fe2_FM",
          "M_Fe1_AFM",
          "M_Fe2_AFM"
        ],
        "units": {
          "delta_EFM_meV": "meV",
          "M_total_FM": "μB",
          "M_total_AFM": "μB",
          "M_Fe1_FM": "μB",
          "M_Fe2_FM": "μB",
          "M_Fe1_AFM": "μB",
          "M_Fe2_AFM": "μB"
        }
      },
      "description": "Table of FM stabilisation energies and Fe projected magnetic moments for the four b‑configuration systems."
    }
  ],
  "notes": "The checker will compare the ΔE_FM and magnetic moment values in this file against a hidden reference derived from the published data, using appropriate tolerances that account for differences in DFT codes and pseudopotentials. It will also verify that the relative ordering of ΔE_FM across systems follows the expected physical trend."
}
```

## How you are scored
Your submission will be evaluated by a hidden verifier that independently checks your magnetic_results.csv. The verifier compares your reported ΔE_FM and magnetic moments to reference values derived from the original study, using appropriate tolerances that account for differences in DFT codes and pseudopotentials. It also verifies that the ordering of ΔE_FM across the four systems conforms to the physically correct pattern. The score is a weighted combination: 60% from the ΔE_FM values (correct sign, magnitude within tolerance, and correct ordering) and 40% from the Fe magnetic moments. You must actually run the DFT calculations; the verifier’s internal reference is hidden, and fabricating numbers that happen to match the reference is not a viable strategy.