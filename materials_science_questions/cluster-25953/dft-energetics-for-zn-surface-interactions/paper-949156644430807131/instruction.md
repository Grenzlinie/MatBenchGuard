# DFT Binding and Surface Energies for Zn/Sn Crystal Facets

## Problem background
In aqueous Zn-metal batteries, Zn metal anodes suffer from non-uniform deposition (dendrite growth) and parasitic side reactions that degrade cycling stability. Surface coatings formed by chemical replacement reactions can mitigate these issues, but the role of the Zn crystal facets in these reactions is poorly understood and depends on the relative stabilities and reactivities of different surface orientations. Key thermodynamic quantities that govern facet-dependent behaviour are the binding energies of adatoms (Sn, Zn) on various Zn and Sn crystal facets, as well as the intrinsic surface energies of those facets. Computing these energies from first principles provides a fundamental reference for comparing and engineering facet-specific surface coatings.

## Approach
Use plane‑wave density functional theory (DFT) with the Perdew–Burke–Ernzerhof (PBE) exchange‑correlation functional and an open‑source code (e.g., Quantum ESPRESSO or GPAW). Construct slab models for five crystal facets: Zn(002), Zn(100), Zn(101), Sn(200), and Sn(101), starting from the bulk structures of Zn (hcp) and Sn (body‑centred tetragonal) with their standard lattice constants. For each facet build a slab thicker than four atomic layers, add a vacuum layer of at least 15 Å, and fully relax the slab geometry. Then compute:
- Binding energy of a single Sn adatom on each Zn facet: E_b = E(slab+Sn) – E(slab) – E(Sn_atom).
- Binding energy of a single Zn adatom on each of the five facets (Zn and Sn facets), defined analogously.
- Surface energy of each clean facet, obtained from the relaxed‑slab total energy and the bulk energy per atom, σ = (E_slab – N·E_bulk)/(2A), using a converged number of layers.
No experimental data or external inputs other than the crystal structures and the DFT code are required.

## Reproduction target
Produce a single table named `dft_results.csv` with one row per facet and four columns:
- facet (e.g., Zn(002))
- binding_energy_Sn_on_Zn (eV, computed only for the three Zn facets; leave empty for Sn facets)
- binding_energy_Zn_on_facet (eV, computed for all five facets)
- surface_energy (eV/nm², computed for all five facets)
All energies must come from plane‑wave DFT with the PBE functional, standard bulk lattice constants, slab thickness > 4 layers, and vacuum ≥ 15 Å. Choose appropriate numerical parameters (k‑points, pseudopotentials, convergence criteria) to achieve physically accurate results.

## Assets

- Quantum ESPRESSO (or GPAW): https://www.quantum-espresso.org/
- Zinc crystal structure
- Tin crystal structure

## Workflow steps

### Step 1: Compute DFT binding and surface energies
- Role: scored (load-bearing)
- Action: Run plane-wave DFT calculations with the PBE functional to compute: (1) binding energies of a Sn adatom on Zn(002), Zn(100), and Zn(101) facets; (2) binding energies of a Zn adatom on Zn(002), Zn(100), Zn(101), Sn(200), and Sn(101) facets; (3) surface energies of all five facets (Zn(002), Zn(100), Zn(101), Sn(200), Sn(101)). For each facet construct a slab model from the bulk crystal structure, use a slab thickness >4 atomic layers and at least 15 Å vacuum, and fully relax the slab. For binding energies, place a single adatom on the relaxed surface and compute E_b = E(slab+adatom) - E(slab) - E(atom). For surface energies, compute σ = (E(slab) - N·E_bulk)/(2A) using an appropriate number of layers. Gather all results into dft_results.csv.
- Output file: `/app/outputs/dft_results.csv`
- Format: csv
- Contract: Columns: facet (string), binding_energy_Sn_on_Zn (float eV, empty for Sn facets), binding_energy_Zn_on_facet (float eV), surface_energy (float eV/nm²). Rows correspond to facets: Zn(002), Zn(100), Zn(101), Sn(200), Sn(101).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/dft_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### dft_results.csv
- path: `/app/outputs/dft_results.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Table of DFT‑computed binding and surface energies for the five facets. The checker reads each row and compares the reported energies to reference values within per‑quantity tolerances appropriate for PBE plane‑wave DFT.
- schema:
  - `type`: table
  - `required_columns`: `facet`, `binding_energy_Sn_on_Zn`, `binding_energy_Zn_on_facet`, `surface_energy`
  - `units`:
    - `binding_energy_Sn_on_Zn`: eV
    - `binding_energy_Zn_on_facet`: eV
    - `surface_energy`: eV/nm^2

Notes: The agent must use the standard bulk lattice constants for Zn (hcp, a=2.665 Å, c=4.947 Å) and Sn (tetragonal, a=5.832 Å, c=3.181 Å). The binding_energy_Sn_on_Zn column should be left empty for Sn facets. All energies must be reported in the units specified above.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "dft_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "facet",
          "binding_energy_Sn_on_Zn",
          "binding_energy_Zn_on_facet",
          "surface_energy"
        ],
        "units": {
          "binding_energy_Sn_on_Zn": "eV",
          "binding_energy_Zn_on_facet": "eV",
          "surface_energy": "eV/nm^2"
        }
      },
      "description": "Table of DFT‑computed binding and surface energies for the five facets. The checker reads each row and compares the reported energies to reference values within per‑quantity tolerances appropriate for PBE plane‑wave DFT."
    }
  ],
  "notes": "The agent must use the standard bulk lattice constants for Zn (hcp, a=2.665 Å, c=4.947 Å) and Sn (tetragonal, a=5.832 Å, c=3.181 Å). The binding_energy_Sn_on_Zn column should be left empty for Sn facets. All energies must be reported in the units specified above."
}
```

## How you are scored
After you submit, a hidden verifier reads your `dft_results.csv` and compares each reported binding energy and surface energy to independently determined reference values (not disclosed to you). Each quantity is checked with a tolerance that accounts for legitimate spread due to different DFT implementations, pseudopotentials, and numerical settings. Your overall score is the fraction of the required 13 energy values that lie within tolerance – a real number between 0 and 1. The verifier does not inspect your raw DFT outputs; it only examines the final CSV table. Therefore, correctly executing the full DFT workflow is essential; reporting plausible numbers without running the calculations will not yield a high score.
