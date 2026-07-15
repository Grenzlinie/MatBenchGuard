# DFT Simulation of Pentanoic Acid Adsorption on α‑Al₂O₃ Surfaces

## Problem background
The dispersion of ceramic powders in a liquid medium is often hampered by attractive interparticle forces that cause agglomeration. A common strategy to overcome this problem is to add surfactant molecules, such as carboxylic acids, that adsorb on the particle surfaces and provide steric repulsion. Understanding the detailed adsorption mechanism at the atomic level is essential for rationally tailoring surface chemistry. This task investigates the adsorption of a single pentanoic acid (C₅H₁₀O₂) molecule on two distinct terminations of the (0001) surface of α‑Al₂O₃ (corundum): a clean, Al/O‑terminated surface and a surface saturated with isolated hydroxyl groups. The goal is to determine, through first-principles simulations, the resulting adsorbed structures and their characteristic infrared (IR) spectroscopic signatures, which can serve as fingerprints to identify the adsorption mode in experiments.

## Approach
The study employs plane-wave density functional theory (DFT) within the generalized gradient approximation using the PBESOL functional, augmented with Grimme's D2 dispersion correction. Scalar-relativistic ultrasoft pseudopotentials are used for all elements. Two slab models are constructed from the bulk corundum structure: (i) a clean (0001) surface terminated by Al and O atoms, and (ii) a hydroxylated (0001) surface prepared by replacing the uppermost Al atoms with H, forming isolated Al₂O–H groups. For each surface, Born-Oppenheimer molecular dynamics (BOMD) simulations of a single pentanoic acid molecule initially placed near the surface are performed to observe the adsorption dynamics and bond formation. After a chemical bond is established, the geometry of the full system is relaxed to a minimum using the BFGS algorithm. Finally, density functional perturbation theory (DFPT) is applied to the relaxed structures to compute the vibrational frequencies and infrared intensities. The key structural distances and the wavenumbers of the most informative IR peaks are then extracted to characterise each adsorption configuration.

## Reproduction target
Reproduce the adsorption structures and infrared spectra for both surface terminations by following the complete computational protocol (slab relaxation, BOMD, BFGS optimization, DFPT). From the final relaxed geometries and IR results, populate a single CSV file named `adsorption_structures_ir.csv` that contains the quantities listed below.

**For the clean Al/O‑terminated surface:**
- The C–O bond length in the newly formed C–O–Al bridge.
- The carbonyl C=O bond length of the adsorbed molecule.
- The O(carbonyl)–H(surface hydroxyl) interatomic distance.
- The O–H stretching wavenumber of the isolated surface hydroxyl.
- The C=O stretching wavenumber of the adsorbate carbonyl.

**For the hydroxylated surface:**
- The O(adsorbate)–H and O(surface)–H distances in the hydrogen bond that links the acid to the surface.
- The carbonyl C=O bond length.
- The wavenumber of the characteristic O–H···O bridge vibrational mode.
- The wavenumbers of prominent O–H stretching vibrations of the surface hydroxyls.

All quantities must be reported in rows with columns `surface_type`, `distance_label`, `distance_angstrom`, `IR_peak_mode`, `wavenumber_cm`, and `intensity` (intensity may be left empty).

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/download
- Ultrasoft pseudopotentials (Al, O, C, H): https://www.quantum-espresso.org/pseudopotentials
- α‑Al₂O₃ (corundum) crystal structure: http://www.crystallography.net/cod/1000022.html

## Workflow steps

### Step 1: Construct and relax clean and hydroxylated (0001) α‑Al₂O₃ slabs
- Role: process
- Action: Build a 3×3 supercell slab of the (0001) corundum surface with at least 25 Å vacuum. Prepare two terminations: (i) clean Al/O‑terminated surface, and (ii) hydroxylated surface by replacing top Al with H to create isolated Al₂O‑H groups. Using DFT (PBESOL GGA, ultrasoft pseudopotentials, Γ‑point sampling, Grimme D2 dispersion correction), relax the top atomic layers of each slab with the BFGS algorithm until forces converge, while keeping the bottom two layers fixed at bulk positions.
- Evidence: `/app/outputs/slab_relaxation.log`

### Step 2: BOMD and BFGS relaxation of pentanoic acid on clean Al/O‑terminated surface
- Role: process
- Action: Place a single pentanoic acid molecule (C₅H₁₀O₂) with its acidic group ~3 Å above the relaxed clean slab. Run Born‑Oppenheimer molecular dynamics on the electronic ground state with a time step of ~0.96756 fs (20 a.u.) until a chemical bond forms. Then fully relax the geometry using BFGS (energy tolerance 0.01 mRy, force tolerance 0.1 mRy/bohr), keeping the bottom two slab layers fixed.
- Evidence: `/app/outputs/bomd_clean.log`

### Step 3: BOMD and BFGS relaxation of pentanoic acid on hydroxylated surface
- Role: process
- Action: Place a pentanoic acid molecule ~3 Å above the relaxed hydroxylated slab. Run Born‑Oppenheimer molecular dynamics and BFGS optimization using the same computational parameters as for the clean surface.
- Evidence: `/app/outputs/bomd_hydrox.log`

### Step 4: DFPT infrared spectrum calculation for both adsorbed configurations
- Role: process
- Action: For each relaxed adsorption structure (clean and hydroxylated), perform a density functional perturbation theory calculation (ph.x) to obtain vibrational frequencies, infrared intensities, and normal‑mode eigenvectors. Fix the atoms of the lower slab layers during the dynamical matrix calculation. Identify the O–H and C=O stretching modes that correspond to the surface hydroxyl and the adsorbate carbonyl.
- Evidence: `/app/outputs/ir_calc.log`

### Step 5: Compile key structural distances and IR peak data into a CSV
- Role: scored (load-bearing)
- Action: From the optimized geometries and IR results, extract the requested interatomic distances and IR peak wavenumbers. For the clean Al/O‑terminated surface: the C–O bond length in the C–O–Al bridge, the carbonyl C=O bond length, the O(carbonyl)–H(surface OH) distance, the O–H stretch wavenumber of the isolated surface hydroxyl, and the C=O stretch wavenumber of the adsorbate carbonyl. For the hydroxylated surface: the O(adsorbate)–H and O(surface)–H distances in the strong hydrogen bond, the carbonyl C=O bond length, the O–H stretching wavenumbers of surface hydroxyls, and the complex O–H···O bridge mode wavenumber. Write one row per measured quantity to a CSV file named 'adsorption_structures_ir.csv'.
- Output file: `/app/outputs/adsorption_structures_ir.csv`
- Format: csv
- Contract: CSV with columns: surface_type (AlO_terminated or hydroxylated), distance_label (string, e.g., C_O_Al, C_O_carbonyl, OH_surface, OH_ads_H, OH_surf_H), distance_angstrom (float), IR_peak_mode (string, e.g., OH_stretch_surface, CO_stretch, bridge_mode), wavenumber_cm (float), intensity (float, optional).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/adsorption_structures_ir.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### adsorption_structures_ir.csv
- path: `/app/outputs/adsorption_structures_ir.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: A CSV file containing the key interatomic distances and infrared peak wavenumbers for pentanoic acid adsorbed on the Al/O‑terminated and hydroxylated (0001) α‑Al₂O₃ surfaces. Each row reports one measured quantity with its surface type, distance or mode label, and the numeric value. The checker compares the reported numbers to hidden paper‑reported reference values.
- schema:
  - `type`: table
  - `required_columns`: `surface_type`, `distance_label`, `distance_angstrom`, `IR_peak_mode`, `wavenumber_cm`, `intensity`
  - `units`:
    - `distance_angstrom`: Angstrom
    - `wavenumber_cm`: cm^-1

Notes: The agent must run all four process stages (slab relaxation, BOMD+BFGS on both surfaces, and DFPT IR calculations) to obtain the geometries and spectra needed to populate this CSV. The scored step is load‑bearing because the quantities (specific bond lengths and wavenumbers) cannot be guessed; they arise only from the full computational pipeline.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "adsorption_structures_ir.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "surface_type",
          "distance_label",
          "distance_angstrom",
          "IR_peak_mode",
          "wavenumber_cm",
          "intensity"
        ],
        "units": {
          "distance_angstrom": "Angstrom",
          "wavenumber_cm": "cm^-1"
        }
      },
      "description": "A CSV file containing the key interatomic distances and infrared peak wavenumbers for pentanoic acid adsorbed on the Al/O‑terminated and hydroxylated (0001) α‑Al₂O₃ surfaces. Each row reports one measured quantity with its surface type, distance or mode label, and the numeric value. The checker compares the reported numbers to hidden paper‑reported reference values."
    }
  ],
  "notes": "The agent must run all four process stages (slab relaxation, BOMD+BFGS on both surfaces, and DFPT IR calculations) to obtain the geometries and spectra needed to populate this CSV. The scored step is load‑bearing because the quantities (specific bond lengths and wavenumbers) cannot be guessed; they arise only from the full computational pipeline."
}
```

## How you are scored
A hidden, automated verifier compares each reported distance and wavenumber in your `adsorption_structures_ir.csv` to reference values derived from the original publication. The verifier checks structural quantities with a tolerance appropriate for DFT‑level reproducibility (e.g., bond lengths within a few hundredths of an angstrom) and checks vibrational frequencies within a tolerance of a few tens of cm⁻¹. It also verifies that the CSV contains the required rows for both surface types and that the bond lengths are physically consistent with the respective adsorption mechanisms. Your total reward is the fraction of reported quantities that fall within the acceptable tolerance windows. Simply listing numbers without running the full workflow will produce incorrect values that fail these comparisons.
