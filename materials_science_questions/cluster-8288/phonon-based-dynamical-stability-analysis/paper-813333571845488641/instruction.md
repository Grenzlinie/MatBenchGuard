# Structure, stability and properties of a predicted carbon allotrope

## Problem background
Carbon can form many allotropes with diverse properties. Under cold compression, graphite transforms into a new phase whose crystal structure has been debated. Several computational studies have proposed candidate structures with sp3 bonding, but the lowest-enthalpy polymorph and its physical properties remain uncertain. This task involves reproducing a computational prediction of a novel carbon allotrope and its key properties, using first-principles calculations.

## Approach
The reproduction is compute-driven. The agent constructs the candidate crystal structure from lattice parameters and atomic coordinates provided in the paper, performs density functional theory (DFT) geometry optimization at 15 GPa using the local density approximation (LDA), and then computes a set of physical properties. The central comparison is the enthalpy per atom of the candidate phase versus several known carbon allotropes (graphite, diamond, M carbon, W carbon, bct-C4, oC16-II, and Cco-C8) over a range of pressures from 0 to 50 GPa, to identify the thermodynamically most stable phase at high pressures. Additionally, phonon dispersion is calculated to assess dynamical stability, and electronic band gap, bulk modulus, Vickers hardness, XRD pattern, and Raman spectrum are computed to characterize the material. All calculations use the LDA functional and open-source tools (Quantum ESPRESSO, Phonopy, pymatgen). The original paper used VASP and other software; the task rescopes to these open-source equivalents.

## Reproduction target
Construct a specific orthorhombic carbon phase with space group Cmcm, lattice constants a=2.469 Å, b=11.170 Å, c=4.802 Å, and atomic fractional coordinates (0.0,0.868,-0.482), (0.0,0.442,-0.421), (0.0,0.778,-0.25), (0.0,0.2,-0.25). Using open-source DFT and phonon codes, relax the structure at 15 GPa, compute enthalpies of this phase and the reference carbon phases (graphite, diamond, M carbon, W carbon, bct-C4, oC16-II, Cco-C8) at a range of pressures spanning 0 to 50 GPa, including the transition region, calculate phonon dispersion, electronic band gap at 0 GPa, bulk modulus, Vickers hardness, XRD pattern (λ=0.3329 Å at 18.4 GPa), and Raman spectrum (at 15 GPa). The objective is to determine whether this phase becomes the most stable candidate among those considered at high pressures, whether it is dynamically stable (no imaginary phonon modes), and to obtain its characteristic property values.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- Phonopy: https://phonopy.github.io/phonopy/
- pymatgen: pymatgen
- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Build initial C carbon structure
- Role: process
- Action: Create the primitive cell of C carbon from lattice constants a=2.469 Å, b=11.170 Å, c=4.802 Å and fractional coordinates of four inequivalent atoms: (0.0, 0.868, -0.482), (0.0, 0.442, -0.421), (0.0, 0.778, -0.25), (0.0, 0.2, -0.25). Save as an input file for DFT.
- Evidence: `/app/outputs/initial_C_carbon.cif`

### Step 2: Relax C carbon structure at 15 GPa
- Role: scored
- Action: Perform DFT geometry optimization (variable cell relaxation) at 15 GPa using the LDA functional. Output the final optimized structure.
- Output file: `/app/outputs/relaxed_structure.cif`
- Format: other
- Contract: CIF format containing lattice constants a, b, c and fractional coordinates of all atoms.
- Scoring: scored by hidden verifier

### Step 3: Obtain reference carbon phase structures
- Role: process
- Action: Gather input structures for the known carbon phases: graphite, diamond, M carbon, W carbon, bct-C4, oC16-II, Cco-C8 from public databases or literature. The agent must locate correct crystal structure data for each phase.
- Evidence: `/app/outputs/reference_structures_collected.txt`

### Step 4: Compute enthalpies of carbon phases
- Role: scored (load-bearing)
- Action: For each carbon phase (C carbon, graphite, diamond, M carbon, W carbon, bct-C4, oC16-II, Cco-C8), perform DFT relaxations at a range of pressures spanning 0 to 50 GPa, including the transition region, and compute the enthalpy per atom. Compile results into a table.
- Output file: `/app/outputs/enthalpy_vs_pressure.csv`
- Format: csv
- Contract: CSV with columns: pressure_GPa, H_graphite, H_diamond, H_M_carbon, H_W_carbon, H_bctC4, H_oC16II, H_CcoC8, H_C_carbon. All enthalpies in eV/atom.
- Scoring: scored by hidden verifier

### Step 5: Calculate phonon dispersion
- Role: scored
- Action: Using the relaxed C carbon structure at 15 GPa, compute phonon frequencies via the finite-displacement method (Quantum ESPRESSO + Phonopy). Output dispersion data and a flag indicating the maximum imaginary frequency.
- Output file: `/app/outputs/phonon_dispersion.yaml`
- Format: txt
- Contract: YAML object with keys: 'q_path' (list of labels), 'frequencies' (list of frequency lists, cm⁻¹), 'max_imaginary_frequency' (float, cm⁻¹).
- Scoring: scored by hidden verifier

### Step 6: Calculate electronic band gap
- Role: scored
- Action: Perform a band structure calculation for C carbon at 0 GPa using the relaxed geometry. Extract the direct band gap at the Gamma point.
- Output file: `/app/outputs/band_gap.txt`
- Format: txt
- Contract: Single floating-point number (eV).
- Scoring: scored by hidden verifier

### Step 7: Compute bulk modulus
- Role: scored
- Action: Perform fixed-volume DFT calculations on C carbon around the equilibrium volume. Fit the energy-volume data to the third-order Birch-Murnaghan equation of state to obtain the bulk modulus B0.
- Output file: `/app/outputs/bulk_modulus.txt`
- Format: txt
- Contract: Single floating-point number (GPa).
- Scoring: scored by hidden verifier

### Step 8: Estimate Vickers hardness
- Role: scored
- Action: Using the equilibrium bond lengths and unit cell volume of C carbon, calculate the Vickers hardness via the empirical formula of Šimůnek and Vackář (PRL 96, 085501).
- Output file: `/app/outputs/hardness.txt`
- Format: txt
- Contract: Single floating-point number (GPa).
- Scoring: scored by hidden verifier

### Step 9: Simulate XRD pattern
- Role: scored
- Action: Using the relaxed C carbon structure at 18.4 GPa, generate the X-ray diffraction pattern for Cu Kα wavelength (0.3329 Å), outputting two-theta angles and intensities.
- Output file: `/app/outputs/xrd_pattern.csv`
- Format: csv
- Contract: CSV with columns: two_theta_deg (float), intensity_arb (float).
- Scoring: scored by hidden verifier

### Step 10: Calculate Raman spectrum
- Role: scored
- Action: Compute the Raman spectrum of C carbon at 15 GPa using density-functional perturbation theory (e.g., Quantum ESPRESSO with Raman post-processing). Output Raman shifts and intensities.
- Output file: `/app/outputs/raman_spectrum.csv`
- Format: csv
- Contract: CSV with columns: raman_shift_cm^{-1} (float), intensity_arb (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/relaxed_structure.cif`
- `/app/outputs/enthalpy_vs_pressure.csv`
- `/app/outputs/phonon_dispersion.yaml`
- `/app/outputs/band_gap.txt`
- `/app/outputs/bulk_modulus.txt`
- `/app/outputs/hardness.txt`
- `/app/outputs/xrd_pattern.csv`
- `/app/outputs/raman_spectrum.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### relaxed_structure.cif
- path: `/app/outputs/relaxed_structure.cif`
- format: other
- purpose: scored
- target_policy: reference_match
- description: Optimized C carbon unit cell at 15 GPa; lattice parameters and atomic positions are checked against paper's reported values.
- schema:
  - `type`: other
  - `description`: CIF file containing lattice parameters a, b, c (Å) and atomic fractional coordinates; compared to paper's reference values within tolerances.

### enthalpy_vs_pressure.csv
- path: `/app/outputs/enthalpy_vs_pressure.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Enthalpy per atom for all carbon phases at multiple pressures; the checker verifies that C carbon is the most stable phase at pressures above a threshold consistent with the paper's claim.
- schema:
  - `type`: table
  - `required_columns`: `pressure_GPa`, `H_graphite`, `H_diamond`, `H_M_carbon`, `H_W_carbon`, `H_bctC4`, `H_oC16II`, `H_CcoC8`, `H_C_carbon`
  - `units`:
    - `pressure_GPa`: GPa
    - `H_graphite`: eV/atom
    - `H_diamond`: eV/atom
    - `H_M_carbon`: eV/atom
    - `H_W_carbon`: eV/atom
    - `H_bctC4`: eV/atom
    - `H_oC16II`: eV/atom
    - `H_CcoC8`: eV/atom
    - `H_C_carbon`: eV/atom

### phonon_dispersion.yaml
- path: `/app/outputs/phonon_dispersion.yaml`
- format: txt
- purpose: scored
- target_policy: threshold_or_better
- description: Phonon dispersion data and max_imaginary_frequency; stability is validated if the maximum imaginary frequency is within a small tolerance.
- schema:
  - `type`: object
  - `required`: `q_path`, `frequencies`, `max_imaginary_frequency`
  - `items`:
    - `q_path`: list of string labels
    - `frequencies`: list of lists of floats (cm⁻¹)
    - `max_imaginary_frequency`: float (cm⁻¹)

### band_gap.txt
- path: `/app/outputs/band_gap.txt`
- format: txt
- purpose: scored
- target_policy: reference_match
- description: Direct band gap; compared to paper's reference value within tolerance.
- schema:
  - `type`: text
  - `description`: Single floating-point number giving the direct band gap at Γ point in eV.

### bulk_modulus.txt
- path: `/app/outputs/bulk_modulus.txt`
- format: txt
- purpose: scored
- target_policy: reference_match
- description: Bulk modulus B0 from EOS fit; compared to paper's reference value within tolerance.
- schema:
  - `type`: text
  - `description`: Single floating-point number giving the bulk modulus in GPa.

### hardness.txt
- path: `/app/outputs/hardness.txt`
- format: txt
- purpose: scored
- target_policy: reference_match
- description: Vickers hardness; compared to paper's reference value within tolerance.
- schema:
  - `type`: text
  - `description`: Single floating-point number giving the Vickers hardness in GPa.

### xrd_pattern.csv
- path: `/app/outputs/xrd_pattern.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Simulated XRD pattern; peak positions are compared to reference values within tolerance.
- schema:
  - `type`: table
  - `required_columns`: `two_theta_deg`, `intensity_arb`
  - `units`:
    - `two_theta_deg`: degrees
    - `intensity_arb`: arbitrary units

### raman_spectrum.csv
- path: `/app/outputs/raman_spectrum.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Raman spectrum; peak positions are compared to reference values within tolerance.
- schema:
  - `type`: table
  - `required_columns`: `raman_shift_cm^{-1}`, `intensity_arb`
  - `units`:
    - `raman_shift_cm^{-1}`: cm⁻¹
    - `intensity_arb`: arbitrary units

Notes: All scored quantities are compared to paper-reported values with appropriate tolerances. The enthalpy check uses a threshold_or_better policy to ensure C carbon is the lowest-enthalpy phase. The phonon stability check is based on max_imaginary_frequency. The remaining quantities are checked via reference_match with tolerances derived from expected DFT spread.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "relaxed_structure.cif",
      "format": "other",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "other",
        "description": "CIF file containing lattice parameters a, b, c (Å) and atomic fractional coordinates; compared to paper's reference values within tolerances."
      },
      "description": "Optimized C carbon unit cell at 15 GPa; lattice parameters and atomic positions are checked against paper's reported values."
    },
    {
      "file": "enthalpy_vs_pressure.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "pressure_GPa",
          "H_graphite",
          "H_diamond",
          "H_M_carbon",
          "H_W_carbon",
          "H_bctC4",
          "H_oC16II",
          "H_CcoC8",
          "H_C_carbon"
        ],
        "units": {
          "pressure_GPa": "GPa",
          "H_graphite": "eV/atom",
          "H_diamond": "eV/atom",
          "H_M_carbon": "eV/atom",
          "H_W_carbon": "eV/atom",
          "H_bctC4": "eV/atom",
          "H_oC16II": "eV/atom",
          "H_CcoC8": "eV/atom",
          "H_C_carbon": "eV/atom"
        }
      },
      "description": "Enthalpy per atom for all carbon phases at multiple pressures; the checker verifies that C carbon is the most stable phase at pressures above a threshold consistent with the paper's claim."
    },
    {
      "file": "phonon_dispersion.yaml",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": [
          "q_path",
          "frequencies",
          "max_imaginary_frequency"
        ],
        "items": {
          "q_path": "list of string labels",
          "frequencies": "list of lists of floats (cm⁻¹)",
          "max_imaginary_frequency": "float (cm⁻¹)"
        }
      },
      "description": "Phonon dispersion data and max_imaginary_frequency; stability is validated if the maximum imaginary frequency is within a small tolerance."
    },
    {
      "file": "band_gap.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "text",
        "description": "Single floating-point number giving the direct band gap at Γ point in eV."
      },
      "description": "Direct band gap; compared to paper's reference value within tolerance."
    },
    {
      "file": "bulk_modulus.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "text",
        "description": "Single floating-point number giving the bulk modulus in GPa."
      },
      "description": "Bulk modulus B0 from EOS fit; compared to paper's reference value within tolerance."
    },
    {
      "file": "hardness.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "text",
        "description": "Single floating-point number giving the Vickers hardness in GPa."
      },
      "description": "Vickers hardness; compared to paper's reference value within tolerance."
    },
    {
      "file": "xrd_pattern.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "two_theta_deg",
          "intensity_arb"
        ],
        "units": {
          "two_theta_deg": "degrees",
          "intensity_arb": "arbitrary units"
        }
      },
      "description": "Simulated XRD pattern; peak positions are compared to reference values within tolerance."
    },
    {
      "file": "raman_spectrum.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "raman_shift_cm^{-1}",
          "intensity_arb"
        ],
        "units": {
          "raman_shift_cm^{-1}": "cm⁻¹",
          "intensity_arb": "arbitrary units"
        }
      },
      "description": "Raman spectrum; peak positions are compared to reference values within tolerance."
    }
  ],
  "notes": "All scored quantities are compared to paper-reported values with appropriate tolerances. The enthalpy check uses a threshold_or_better policy to ensure C carbon is the lowest-enthalpy phase. The phonon stability check is based on max_imaginary_frequency. The remaining quantities are checked via reference_match with tolerances derived from expected DFT spread."
}
```

## How you are scored
Each workflow step produces a scored artifact. A hidden verifier independently checks each artifact against a reference gold derived from the original study. The verifier compares the relaxed structure, enthalpy ranking, phonon stability, band gap, bulk modulus, hardness, XRD peaks, and Raman peaks using appropriate tolerances and scoring policies (reference match, threshold or better). The final reward is a weighted sum of the stage scores; reporting correct numbers is required but not enough — the artifacts must be the direct outputs of the specified computation pipeline.
