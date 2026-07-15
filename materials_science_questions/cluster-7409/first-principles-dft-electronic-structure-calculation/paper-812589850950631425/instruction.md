# First-principles OER overpotential on faceted In2O3 with oxygen vacancies

## Problem background
Indium oxide (In2O3) nanostructures with exposed {001} crystal facets are promising photoelectrodes for solar water splitting because the {001} facets can dissociate water and accumulate photogenerated holes, but their large band gap (~3 eV) severely limits visible-light absorption. Introducing oxygen vacancies into these faceted structures has been proposed as a way to enhance optical absorption, carrier transport, and catalytic activity. Understanding how oxygen vacancies modify the electronic structure and the oxygen evolution reaction (OER) energetics on the {001} surface is essential for optimising the material. This task focuses on first-principles evaluation of the OER Gibbs free energy landscape on In2O3 {001} surfaces with and without oxygen vacancies, revealing the impact of vacancies on the thermodynamic overpotential.

## Approach
The computational approach uses spin-polarised density functional theory (DFT) within the generalized gradient approximation (GGA-PBE). A {001}-oriented slab of body-centred cubic In2O3 is built with vacuum to avoid spurious interactions. The perfect slab is relaxed, then an oxygen vacancy is created by removing one surface oxygen atom and the defective slab relaxed. For each surface, the adsorption geometries and total energies of the three OER intermediates — OH*, O*, and OOH* — are computed, along with energies of isolated H2O and H2 molecules. Vibrational frequency calculations on the adsorbed species yield zero-point energy and entropy corrections. Applying the computational hydrogen electrode model, the Gibbs free energy changes ΔG₁ through ΔG₄ for the four proton-coupled electron transfer steps are assembled into a free energy diagram. The theoretical overpotential η = max(ΔG₁,ΔG₂,ΔG₃,ΔG₄) − 1.23 V is computed for each surface. The two surfaces are compared to evaluate the role of the vacancy.

## Reproduction target
You must produce the file `/app/outputs/free_energy_diagram.json` containing the four ΔG values (in eV) and the derived overpotential (in eV) for both the perfect and the oxygen-vacancy In2O3 {001} surfaces. The overpotential is defined as η = max(ΔG₁,ΔG₂,ΔG₃,ΔG₄) − 1.23 V. All ΔG values must be referenced to the same energy conventions used in the computational hydrogen electrode model.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP pseudopotential library (PBE): https://www.materialscloud.org/discover/sssp/table/efficiency
- bcc In2O3 crystal structure (mp-22557): https://materialsproject.org/materials/mp-22557

## Workflow steps

### Step 1: Relax clean In2O3 {001} slab
- Role: process
- Action: Construct a {001}-oriented slab of bcc In2O3 with ~10 Å vacuum from the publicly available bulk structure. Perform DFT relaxation of atomic positions using GGA-PBE, spin-polarized, with well-converged energy and force criteria. Save the relaxed geometry.
- Evidence: `/app/outputs/relaxed_slab.cif`

### Step 2: Relax oxygen-vacancy slab
- Role: process
- Action: Create an oxygen vacancy by removing one surface oxygen atom from the relaxed perfect slab; relax the geometry of the defective slab under the same DFT settings as the clean slab. Save the relaxed defective geometry.
- Evidence: `/app/outputs/relaxed_vacancy.cif`

### Step 3: Compute electronic density of states and defect state analysis
- Role: process
- Action: For both the perfect and oxygen‑vacancy In2O3 {001} surfaces, compute the electronic density of states (DOS) and band structure using DFT with the same GGA-PBE settings. From the DOS, verify the presence of a new defect state in the band gap of the vacancy surface and quantify the increase in the density of states at the valence band maximum (VBM) relative to the perfect surface. Save the DOS data and defect analysis to a JSON file.
- Evidence: `/app/outputs/dos_analysis.json`

### Step 4: Compute DFT energies of OER intermediates
- Role: process
- Action: For both surfaces (perfect and vacancy), place the OER intermediates OH*, O*, OOH* on the surface, relax the adsorbates, and compute their total energies. Also compute the total energy of an isolated H2O molecule and H2 molecule in the gas phase. Perform vibrational frequency calculations to obtain zero-point energy and entropy corrections for each adsorbed species. Save all raw energies and corrections to a JSON file.
- Evidence: `/app/outputs/intermediate_energies.json`

### Step 5: Assemble Gibbs free‑energy diagram and compute OER overpotential
- Role: scored (load-bearing)
- Action: Using the total energies, zero-point energy and entropy corrections from Step 04, apply the computational hydrogen electrode model to calculate the Gibbs free‑energy change for each of the four OER steps (OH* → O* → OOH* → O2 release) on both the perfect and oxygen‑vacancy In2O3 {001} surfaces. Compute the theoretical overpotential η = max(ΔG₁,ΔG₂,ΔG₃,ΔG₄) − 1.23 V for each surface and write the complete results to free_energy_diagram.json.
- Output file: `/app/outputs/free_energy_diagram.json`
- Format: json
- Contract: {"perfect_surface":{"ΔG1":"number (eV)","ΔG2":"number (eV)","ΔG3":"number (eV)","ΔG4":"number (eV)"},"vacancy_surface":{"ΔG1":"number (eV)","ΔG2":"number (eV)","ΔG3":"number (eV)","ΔG4":"number (eV)"},"overpotential":{"perfect":"number (eV)","vacancy":"number (eV)"}}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/free_energy_diagram.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### free_energy_diagram.json
- path: `/app/outputs/free_energy_diagram.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Gibbs free‑energy diagram for the OER on perfect and oxygen‑vacancy In2O3 {001} facets, including the derived overpotentials.
- schema:
  - `type`: object
  - `required`:
    - `perfect_surface`: object containing ΔG1–ΔG4 in eV
    - `vacancy_surface`: object containing ΔG1–ΔG4 in eV
    - `overpotential`: object containing 'perfect' and 'vacancy' overpotentials in eV
  - `items`: object
  - `required_columns`:
  - `units`:
    - `ΔG1`: eV
    - `ΔG2`: eV
    - `ΔG3`: eV
    - `ΔG4`: eV
    - `overpotential.perfect`: eV
    - `overpotential.vacancy`: eV

Notes: All ΔG values must be given in eV, referenced to the same energy conventions. The overpotential is defined as max(ΔG₁,ΔG₂,ΔG₃,ΔG₄) − 1.23 V. The checker will verify the overpotential values against the paper's reported hidden threshold; a lower (better) overpotential meets the threshold and earns full credit.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "free_energy_diagram.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": {
          "perfect_surface": "object containing ΔG1–ΔG4 in eV",
          "vacancy_surface": "object containing ΔG1–ΔG4 in eV",
          "overpotential": "object containing 'perfect' and 'vacancy' overpotentials in eV"
        },
        "items": {},
        "required_columns": [],
        "units": {
          "ΔG1": "eV",
          "ΔG2": "eV",
          "ΔG3": "eV",
          "ΔG4": "eV",
          "overpotential.perfect": "eV",
          "overpotential.vacancy": "eV"
        }
      },
      "description": "Gibbs free‑energy diagram for the OER on perfect and oxygen‑vacancy In2O3 {001} facets, including the derived overpotentials."
    }
  ],
  "notes": "All ΔG values must be given in eV, referenced to the same energy conventions. The overpotential is defined as max(ΔG₁,ΔG₂,ΔG₃,ΔG₄) − 1.23 V. The checker will verify the overpotential values against the paper's reported hidden threshold; a lower (better) overpotential meets the threshold and earns full credit."
}
```

## How you are scored
A hidden verifier checks your file for structure (presence and shape of required keys) and re-computes the overpotential from the submitted ΔG values to ensure self-consistency. The overpotential for each surface is compared against a hidden reference threshold derived from the original publication. Scoring follows a threshold-or-better policy: an overpotential that is equal to or lower (better) than the reference earns full credit for that surface; reward decreases only as the overpotential becomes worse. The final reward is the weighted combination of the checks across the scored stage.
