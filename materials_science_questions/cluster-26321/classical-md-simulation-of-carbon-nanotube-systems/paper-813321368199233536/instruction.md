# Classical MD Simulation of Water Permeation through CNT Membranes

## Problem background
Understanding water transport through carbon nanotube (CNT) pores is important for the design of nanofluidic devices and biomimetic membrane channels. This study investigates the self-diffusion of water through (6,6) single-walled carbon nanotubes (SWCNTs) embedded in a lipid bilayer, and how it is affected by static electric fields and by inter-pore interactions in arrays of CNTs. The system comprises water reservoirs separated by a POPC lipid membrane that contains either a single CNT or an array of four CNTs. The quantities of interest include the steady‑state water permeation rate, the intra‑pore diffusion coefficient, the dipole orientation distribution of water molecules inside the pore, and the effective viscosity of water in a close‑packed array. Molecular dynamics (MD) simulations in conjunction with continuum‑level modeling are used to compute these properties from atomic trajectories.

## Approach
The approach relies on classical all-atom MD simulations using the CHARMM27 force field and the TIP3P water model. Three simulation systems are built: a single (6,6) SWCNT in a POPC membrane with water layers on each side, and two periodic arrays of four such CNTs with center‑to‑center separations of 15 Å and 25 Å. After equilibration in the NPT ensemble, production runs are carried out in the NVT ensemble at 300 K using Langevin dynamics. For the single tube, two separate production runs are performed: one with no external field and one with a static electric field of 0.0065 V/Å applied along the CNT axis. For each array separation, only a zero‑field production run is performed. The trajectories are analyzed to extract transport properties. Tracer permeation rates are obtained by monitoring the net number of water molecules crossing the CNT (color‑diffusion counting). Intra‑pore diffusion coefficients are computed from the axial mean squared displacement of water molecules inside the tube. Osmotic permeability is evaluated from the collective velocity autocorrelation function of all water molecules in the pores. The hopping rate is derived via the continuous‑time random walk model relation k = 2 D_p / a² with a characteristic length scale a = 0.26 nm. Dipole orientation distributions are obtained by binning the cosine of the angle between the water dipole and the tube axis. The effective viscosity of the 15‑Å array is determined from the Einstein relation applied to the off‑diagonal stress component, tracking chains of six water molecules initially near the center of each CNT.

## Reproduction target
Produce three CSV files under `/app/outputs/` that report the required quantities for the specified conditions:

1. `/app/outputs/permeation_rates.csv` — for each zero-field condition (single tube, array 15 Å, array 25 Å), list the system identifier, field condition (always 'none'), steady‑state tracer permeation rate j_d (ns⁻¹), diffusive permeability p_d (nm³ ns⁻¹), intra‑pore diffusion coefficient D_p (nm² ns⁻¹), hopping rate k (ns⁻¹), and osmotic permeability p_f (nm³ ns⁻¹).

2. `/app/outputs/dipole_distribution.csv` — for the single‑tube system under zero and static fields, provide a normalized histogram of the cosine of the water dipole angle α relative to the +z axis, with bin edges and probabilities.

3. `/app/outputs/effective_viscosity.csv` — for the 15 Å array under zero field, report the effective viscosity η (N·s·m⁻²) computed from the stress autocorrelation.

The numerical results should reflect the underlying physics of water transport and inter‑pore friction as modeled by the force field and simulation protocol.

## Assets

- MD simulation engine (NAMD, GROMACS, or LAMMPS): https://www.ks.uiuc.edu/Research/namd/ (NAMD); https://www.gromacs.org/ (GROMACS); https://www.lammps.org/ (LAMMPS)
- CHARMM27 force field parameters
- TIP3P water model

## Workflow steps

### Step 1: Build molecular systems
- Role: process
- Action: Construct the following simulation systems using the CHARMM27 force field and TIP3P water: (1) a single (6,6) SWCNT (length ~36.9 Å, diameter 8.20 Å) embedded in a POPC lipid bilayer, solvated with ~1337 water molecules forming two ~10 Å reservoirs on each side, periodic box ~34.84×34×66.29 Å³; (2) a periodic array of four (6,6) SWCNTs with 15 Å center-to-center separation in a POPC membrane (~3045 water molecules, box ~45.75×60.32×66.68 Å³); (3) the same array with 25 Å separation (~4327 water molecules, box ~63.10×59.99×66.27 Å³). CNT atoms are neutral sp² carbon (CHARMM type CA); CNT axis aligned with z-direction. Generate topology and coordinate files suitable for the chosen MD engine.
- Evidence: `/app/outputs/system_build.log`

### Step 2: Equilibration and production MD simulations
- Role: process
- Action: For each constructed system, perform NPT equilibration (1 ns at 300 K, 1 atm with fixed CNT, then gradually release harmonic constraints on lipids and CNT over 0.4 ns). Then run 50-ns NVT production at 300 K using Langevin dynamics (damping 1 ps⁻¹). For the single tube, run one simulation with zero electric field and one with a static electric field of 0.0065 V/Å along +z. For each array separation (15 Å, 25 Å), run only zero-field simulations. Use Particle Mesh Ewald (12 Å real-space cutoff), 12 Å van der Waals cutoff with switching from 10 Å, 2 fs time step with SHAKE on bonds to hydrogen. Save atomic trajectories at sufficient frequency for subsequent analysis (e.g., every 1 ps).
- Evidence: `/app/outputs/md_simulation.log`

### Step 3: Calculate steady-state permeation rates and transport coefficients
- Role: scored (load-bearing)
- Action: From the production trajectories, compute the net water permeation rate j_d (molecules/ns) through the CNT(s) using a colour-diffusion counting method, the axial intra-pore diffusion coefficient D_p from the Einstein relation on the axial mean squared displacement of water molecules inside the CNT, the hopping rate k using k = 2 D_p / a² with a = 0.26 nm, the osmotic permeability p_f by integrating the axial collective-velocity total correlation function, and the diffusive permeability p_d = j_d / c_H2O with c_H2O = 33.5 nm⁻³. Report results for the three zero-field conditions: single tube, array 15 Å, array 25 Å.
- Output file: `/app/outputs/permeation_rates.csv`
- Format: csv
- Contract: Columns: system (string, one of 'single', 'array15', 'array25'), field (string, 'none'), j_d (float, ns⁻¹), p_d (float, nm³ ns⁻¹), D_p (float, nm² ns⁻¹), k (float, ns⁻¹), p_f (float, nm³ ns⁻¹).
- Scoring: scored by hidden verifier

### Step 4: Calculate dipole orientation distribution
- Role: scored
- Action: For the single-tube trajectories (zero field and static field), compute the probability distribution of cos(α), where α is the angle between the water dipole vector and the +z axis (CNT axis). Bin cos(α) into equal-width intervals between -1 and 1 (approximately 0.1 width) and normalise to unit area.
- Output file: `/app/outputs/dipole_distribution.csv`
- Format: csv
- Contract: Columns: system (string, 'single'), field (string, 'none' or 'static'), cos_alpha_low (float, lower bin edge), cos_alpha_high (float, upper bin edge), probability (float, normalised count).
- Scoring: scored by hidden verifier

### Step 5: Calculate effective viscosity for 15 Å array
- Role: scored
- Action: From the 15 Å array zero-field trajectory, track hexamer groups of six water molecules initially nearest the center of each CNT. Compute the effective viscosity η from the Einstein relation using the long-time slope of the mean square displacement of the off-diagonal stress component P_zz, as defined in the protocol. Report the result.
- Output file: `/app/outputs/effective_viscosity.csv`
- Format: csv
- Contract: Columns: array_separation (string, '15'), eta (float, N·s·m⁻²).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/permeation_rates.csv`
- `/app/outputs/dipole_distribution.csv`
- `/app/outputs/effective_viscosity.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### permeation_rates.csv
- path: `/app/outputs/permeation_rates.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Steady-state tracer permeation rates and transport coefficients for single CNT and array systems under zero and static electric fields.
- schema:
  - `type`: table
  - `required_columns`: `system`, `field`, `j_d`, `p_d`, `D_p`, `k`, `p_f`
  - `units`:
    - `j_d`: ns^-1
    - `p_d`: nm^3 ns^-1
    - `D_p`: nm^2 ns^-1
    - `k`: ns^-1
    - `p_f`: nm^3 ns^-1

### dipole_distribution.csv
- path: `/app/outputs/dipole_distribution.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Normalised probability distribution of the cosine of the water dipole angle for single-tube system.
- schema:
  - `type`: table
  - `required_columns`: `system`, `field`, `cos_alpha_low`, `cos_alpha_high`, `probability`

### effective_viscosity.csv
- path: `/app/outputs/effective_viscosity.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Effective viscosity of water confined in the 15 Å CNT array.
- schema:
  - `type`: table
  - `required_columns`: `array_separation`, `eta`
  - `units`:
    - `eta`: N s m^-2

Notes: Scoring compares agent-reported values to hidden reference values from the paper using tolerance-based comparison. J_d, D_p, k, p_f use relative tolerance; dipole histogram uses mean absolute difference; effective viscosity uses relative tolerance.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "permeation_rates.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "system",
          "field",
          "j_d",
          "p_d",
          "D_p",
          "k",
          "p_f"
        ],
        "units": {
          "j_d": "ns^-1",
          "p_d": "nm^3 ns^-1",
          "D_p": "nm^2 ns^-1",
          "k": "ns^-1",
          "p_f": "nm^3 ns^-1"
        }
      },
      "description": "Steady-state tracer permeation rates and transport coefficients for single CNT and array systems under zero and static electric fields."
    },
    {
      "file": "dipole_distribution.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "system",
          "field",
          "cos_alpha_low",
          "cos_alpha_high",
          "probability"
        ]
      },
      "description": "Normalised probability distribution of the cosine of the water dipole angle for single-tube system."
    },
    {
      "file": "effective_viscosity.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "array_separation",
          "eta"
        ],
        "units": {
          "eta": "N s m^-2"
        }
      },
      "description": "Effective viscosity of water confined in the 15 Å CNT array."
    }
  ],
  "notes": "Scoring compares agent-reported values to hidden reference values from the paper using tolerance-based comparison. J_d, D_p, k, p_f use relative tolerance; dipole histogram uses mean absolute difference; effective viscosity uses relative tolerance."
}
```

## How you are scored
Your submission will be evaluated by an automated hidden verifier. The verifier compares the values in the output CSV files to hidden reference values using appropriate comparison metrics for each output. For the permeation rates and transport coefficients, a performance‑oriented metric is used that rewards accuracy and penalizes large deviations. For the dipole distribution, the histogram probabilities are compared. For the effective viscosity, the reported value is compared. Each output's score is weighted according to its importance, and the weighted sum produces a final reward between 0.0 (no match) and 1.0 (excellent agreement). Good reproduction requires faithfully executing the MD simulation and analysis steps as described, not guessing or fabricating numbers.
