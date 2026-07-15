# Relaxation energies and vibrational frequencies of clean and hydroxylated alkaline-earth oxide surfaces

## Problem background
Understanding how water interacts with alkaline-earth oxide surfaces is important for heterogeneous catalysis, corrosion, and geochemical processes. This work investigates the surface relaxation and the energetics of water dissociation on the (001), (110), and (210) surfaces of MgO, CaO, and SrO using first-principles periodic calculations. The goal is to compute the small relaxation energies experienced by the clean and hydroxylated surfaces, the water/solid interaction (hydroxylation) energies, and the harmonic vibrational frequencies of the resulting OH groups. The results are used to characterize the surface morphology and the strength of water–oxide bonding.

## Approach
The surfaces are modeled as periodic five-layer slabs with a vacuum region. For each oxide and surface orientation, calculations are performed at the density-functional theory (DFT) level using an open‑source periodic code (e.g., Quantum ESPRESSO or CP2K) and standard pseudopotentials. The workflow consists of: (1) optimizing an isolated water molecule to obtain a reference energy and geometry; (2) building unrelaxed slab models using the experimental bulk lattice constants and the rocksalt structure; (3) relaxing the clean slabs (ions only, fixed cell) to get relaxed and unrelaxed total energies; (4) placing a dissociated water molecule on each side of the slab (OH on the surface cation, H on a surface oxygen) and performing a constrained vertical relaxation to obtain the hydroxylated geometry and energy; (5) computing harmonic OH stretching frequencies by scanning the H···Os and H···Ow bond lengths, fitting a sixth‑degree polynomial to the potential energy curve, and numerically solving the one‑dimensional nuclear Schrödinger equation. From the collected total energies the clean and hydroxylated relaxation energies and the hydroxylation energy per water molecule are calculated, and all results are compiled into a single CSV file.

## Reproduction target
Using a periodic DFT code, construct five‑layer slab models for the (001), (110), and (210) surfaces of MgO, CaO, and SrO. For each surface, compute the clean‑surface relaxation energy (ΔE = E_relaxed − E_unrelaxed), the hydroxylated‑surface relaxation energy after adding water, and the hydroxylation energy per water molecule. Compute the harmonic vibrational frequencies (in cm⁻¹) of the H···Os (hydrogen on surface oxygen) and H···Ow (hydroxyl) stretching modes. Report all values in the scored CSV file `/app/outputs/relaxation_and_frequencies.csv` with one row per oxide–surface combination and the columns: oxide, plane, clean_ΔE_relax, hyd_ΔE_relax, E_hyd, freq_HOs, freq_HOw. Energies are in hartree, frequencies in cm⁻¹.

## Assets

- Periodic DFT code: https://www.quantum-espresso.org
- Pseudopotential library (SSSP): https://www.materialscloud.org/discover/sssp/table

## Workflow steps

### Step 1: Optimize isolated water molecule
- Role: process
- Action: Optimize geometry of an isolated water molecule using the selected DFT code and basis set. Record the equilibrium total energy and geometry; this provides the water reference energy needed for hydroxylation energy calculations.
- Evidence: `/app/outputs/water_energy.txt`

### Step 2: Build slab models
- Role: process
- Action: Construct five-layer periodic slab models for the (001), (110), and (210) surfaces of MgO, CaO, and SrO using the experimental lattice constants (4.21, 4.86, 5.22 Å) and rocksalt structure. Ensure symmetric slabs with vacuum spacing.
- Evidence: `/app/outputs/slab_structures.log`

### Step 3: Clean surface relaxations
- Role: process
- Action: For each slab, perform geometry optimization (ion positions only, fixed cell) to obtain the relaxed total energy and the unrelaxed total energy of the clean slab. Record both energies for later use.
- Evidence: `/app/outputs/clean_relaxation_energies.log`

### Step 4: Hydroxylated surface relaxations
- Role: process
- Action: Place one dissociated water molecule per side of each slab (OH on surface cation, H on surface oxygen) and perform a constrained vertical relaxation along the z-axis, allowing the top surface atoms to move. Obtain the equilibrium hydroxylated geometry and total energy.
- Evidence: `/app/outputs/hydroxylated_geometries.log`

### Step 5: Compute vibrational frequencies
- Role: process
- Action: For each hydroxylated slab, scan the H···Os and H···Ow bond lengths around their equilibrium values, compute total energies at each displacement, fit a sixth-degree polynomial to the potential energy curve, and numerically solve the 1D nuclear Schrödinger equation to obtain the harmonic vibrational frequencies ωe for both OH stretching modes.
- Evidence: `/app/outputs/frequency_scans.log`

### Step 6: Compile results and write CSV
- Role: scored (load-bearing)
- Action: Calculate the clean relaxation energy ΔE = E(relaxed) − E(unrelaxed) from step 03; the hydroxylated relaxation energy from step 04; the hydroxylation/interaction energy E_hyd = [E(slab+2H2O) − E(clean slab) − 2E(H2O)]/2 using water energy from step 01, clean slab energy from step 03, and hydroxylated energy from step 04; and retrieve the harmonic frequencies from step 05. Write all values into a single CSV file with one row per oxide–surface combination.
- Output file: `/app/outputs/relaxation_and_frequencies.csv`
- Format: csv
- Contract: oxide (string), plane (string), clean_ΔE_relax (float in hartree), hyd_ΔE_relax (float in hartree), E_hyd (float in hartree), freq_HOs (float in cm⁻¹), freq_HOw (float in cm⁻¹)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/relaxation_and_frequencies.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### relaxation_and_frequencies.csv
- path: `/app/outputs/relaxation_and_frequencies.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Summary table of computed relaxation energies, hydroxylation energies, and harmonic vibrational frequencies for all oxide/surface combinations.
- schema:
  - `type`: table
  - `required_columns`: `oxide`, `plane`, `clean_ΔE_relax`, `hyd_ΔE_relax`, `E_hyd`, `freq_HOs`, `freq_HOw`
  - `units`:
    - `clean_ΔE_relax`: hartree
    - `hyd_ΔE_relax`: hartree
    - `E_hyd`: hartree
    - `freq_HOs`: cm^-1
    - `freq_HOw`: cm^-1

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "relaxation_and_frequencies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "oxide",
          "plane",
          "clean_ΔE_relax",
          "hyd_ΔE_relax",
          "E_hyd",
          "freq_HOs",
          "freq_HOw"
        ],
        "units": {
          "clean_ΔE_relax": "hartree",
          "hyd_ΔE_relax": "hartree",
          "E_hyd": "hartree",
          "freq_HOs": "cm^-1",
          "freq_HOw": "cm^-1"
        }
      },
      "description": "Summary table of computed relaxation energies, hydroxylation energies, and harmonic vibrational frequencies for all oxide/surface combinations."
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden verifier independently checks each stage of the workflow for correctness and completeness. The main scored artifact is the CSV file, which is judged against a set of physical plausibility criteria derived from the reference study: the relaxation energies must be small in magnitude, the hydroxylation energies must follow a specific ordering across the different surfaces, and the vibrational frequencies must lie within physically reasonable ranges and satisfy a relative comparison between H···Os and H···Ow modes. Reporting the reference paper's numbers without performing the actual calculations will not satisfy these checks. The final reward is a weighted combination of several checks, with the majority of the weight on the CSV content.
