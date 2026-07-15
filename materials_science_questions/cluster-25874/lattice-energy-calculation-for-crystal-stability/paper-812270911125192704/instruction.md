# Lattice dynamics of solid CS2: phonon frequencies, density of states, and heat capacity from Kihara core potential

## Problem background
Solid carbon disulphide (CS₂) is a molecular crystal composed of linear triatomic molecules. At low temperature it adopts an orthorhombic Cmca structure with two molecules per primitive unit cell. Understanding the lattice vibrations (phonons) and low-temperature thermodynamic properties of such a crystal requires a reliable intermolecular potential. The Kihara core potential models each molecule as a hard convex core (here a rod representing the carbon‑sulphur molecular axis) surrounded by a soft repulsive‑dispersive envelope. Combined with a quadrupole‑quadrupole electrostatic term, it offers a physically transparent description of intermolecular forces. This task reconstructs the harmonic, rigid‑molecule lattice dynamics of solid CS₂ based on that potential. From the dynamical matrix one obtains phonon frequencies, the vibrational density of states, the constant‑volume heat capacity Cᵥ, and the lattice energy at the experimental crystal geometry.

## Approach
The central assumption is the rigid‑molecule harmonic approximation, where each CS₂ molecule has three translational and two rotational (librational) degrees of freedom. The intermolecular potential is the Kihara 12‑6 core potential added to a quadrupole‑quadrupole interaction. The key geometric quantity is the shortest distance between the finite rod cores of two molecules. A published geometric algorithm computes this distance for arbitrary orientations, with special handling when the molecular axes become nearly parallel; a smooth interpolation is required to obtain well‑defined first derivatives for the dynamical matrix. Using the experimental crystal structure at 5.3 K (space group Cmca, lattice parameters a, b, c and molecular tilt angle) together with pre‑adjusted potential scaling multipliers (U₀ × 0.85, ρ₀ × 1.06, L × 0.88), the 10 × 10 dynamical matrix is constructed for any wave‑vector q. Diagonalising it yields ten phonon frequencies. Zone‑centre modes are assigned to the irreducible representations Ag, B1g, B2g, B3g, Au, B1u, B2u. To obtain the vibrational density of states, the dynamical matrix is diagonalised at a large number (1000) of random q‑points uniformly distributed in the irreducible wedge of the Brillouin zone; the resulting 10 000 eigenfrequencies are histogrammed with 1 cm⁻¹ resolution. The constant‑volume heat capacity Cᵥ is then computed from this DOS via the standard harmonic‑oscillator formula. Finally, the lattice energy is obtained by summing the intermolecular potential over all relevant neighbours and extrapolating to infinite cut‑off distance.

## Reproduction target
Produce a self‑consistent set of computed quantities from the Kihara‑potential lattice dynamics, all evaluated at the experimental 5.3 K crystal geometry:
- The seven optically‑active zone‑centre phonon frequencies (Ag, B1g, B2g, B3g, Au, B1u, B2u).
- A histogram of the vibrational density of states built from 1000 uniformly distributed random wave‑vectors (irreducible wedge) with 1 cm⁻¹ bin width.
- The constant‑volume heat capacity Cᵥ (cal mol⁻¹ K⁻¹) for temperatures from 0 K to 100 K, derived from that DOS.
- The lattice energy (kcal mol⁻¹) at the experimental geometry, extrapolated to infinite neighbour‑cutoff.

The results must be internally consistent (for example, the heat capacity must follow from the submitted DOS via the harmonic formula) and written to the specified output files. The computed numbers will be compared to independent reference values by a hidden verifier; the reference values are not provided.

## Assets

- CS2 crystal structure at 5.3 K: 10.1107/S0567740882000428
- Python scientific stack (numpy, scipy, matplotlib): numpy scipy matplotlib

## Workflow steps

### Step 1: Zone-centre phonon frequencies
- Role: scored
- Action: Implement the Kihara core potential (Kihara 12‑6 plus quadrupole‑quadrupole) and the minimum rod‑core distance algorithm from the paper's Appendix (including parallel‑axes interpolation). Use the experimental crystal structure at 5.3 K and the fitted potential scaling multipliers (U₀×0.85, ρ₀×1.06, L×0.88). Construct the 10×10 rigid‑molecule harmonic dynamical matrix at q = (0,0,0) and diagonalise it to obtain the ten normal‑mode frequencies. Extract the seven optically active modes (Ag, B1g, B2g, B3g, Au, B1u, B2u).
- Output file: `/app/outputs/zone_center_frequencies.json`
- Format: json
- Contract: Array of objects with keys "mode" (string, one of "Ag","B1g","B2g","B3g","Au","B1u","B2u") and "frequency" (float, cm⁻¹).
- Scoring: scored by hidden verifier

### Step 2: Random wavevector sampling and phonon frequencies
- Role: process
- Action: Generate 1000 uniformly distributed random wavevectors in the irreducible wedge of the Brillouin zone (qx,qy,qz ≥ 0). For each wavevector, construct and diagonalise the 10×10 dynamical matrix using the same potential and structure. Collect all 10000 eigenfrequencies and store the raw array for later density‑of‑states binning.
- Evidence: `/app/outputs/random_frequencies.npy`

### Step 3: Vibrational density of states
- Role: scored (load-bearing)
- Action: From the 10000 phonon frequencies obtained in the previous step, construct a histogram with bin width 1 cm⁻¹. Output the bin centres and the corresponding density values (arbitrary units, normalised to the total number of modes).
- Output file: `/app/outputs/density_of_states.json`
- Format: json
- Contract: Object with keys "bin_centers" (array of floats, cm⁻¹) and "density" (array of floats, same length).
- Scoring: scored by hidden verifier

### Step 4: Heat capacity Cv
- Role: scored (load-bearing)
- Action: Using the density‑of‑states histogram, compute the constant‑volume heat capacity Cv via the standard harmonic formula over the temperature range 0–100 K at a resolution appropriate for comparison (e.g., 1 K steps). Report Cv in cal·mol⁻¹·K⁻¹.
- Output file: `/app/outputs/heat_capacity.json`
- Format: json
- Contract: Array of objects with keys "temperature" (float, K) and "Cv" (float, cal·mol⁻¹·K⁻¹).
- Scoring: scored by hidden verifier

### Step 5: Lattice energy at experimental geometry
- Role: scored
- Action: Evaluate the total intermolecular potential energy per mole, summing over all relevant neighbours and extrapolating to infinite distance as in the paper's Table II footnote. Report the lattice energy in kcal/mol.
- Output file: `/app/outputs/lattice_energy.txt`
- Format: txt
- Contract: Plain text containing one number (float, kcal/mol).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/zone_center_frequencies.json`
- `/app/outputs/density_of_states.json`
- `/app/outputs/heat_capacity.json`
- `/app/outputs/lattice_energy.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### zone_center_frequencies.json
- path: `/app/outputs/zone_center_frequencies.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Seven optically‑active zone‑centre mode frequencies. Each mode must match the hidden reference within ±5 cm⁻¹.
- schema:
  - `type`: array
  - `items`:
    - `mode`: string (one of Ag, B1g, B2g, B3g, Au, B1u, B2u)
    - `frequency`: float (cm⁻¹)

### density_of_states.json
- path: `/app/outputs/density_of_states.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Histogram of the vibrational density of states with 1 cm⁻¹ resolution. Checked for bin count, reasonable peak positions, and shape consistency.
- schema:
  - `type`: object
  - `required`: `bin_centers`, `density`
  - `bin_centers`: array of float (cm⁻¹)
  - `density`: array of float (arbitrary units)

### heat_capacity.json
- path: `/app/outputs/heat_capacity.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Constant‑volume heat capacity curve from 0 to 100 K. The checker recomputes Cv from the submitted DOS for self‑consistency, then compares Cv at selected temperatures to the hidden paper curve within ±2 cal·mol⁻¹·K⁻¹.
- schema:
  - `type`: array
  - `items`:
    - `temperature`: float (K)
    - `Cv`: float (cal·mol⁻¹·K⁻¹)

### lattice_energy.txt
- path: `/app/outputs/lattice_energy.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: Lattice energy at the experimental 5.3 K geometry, extrapolated to infinite cutoff. Scored against the hidden gold (−9.06 kcal/mol) with tolerance ±0.5 kcal/mol.
- schema:
  - `type`: text
  - `description`: Single float (kcal/mol)

Notes: The potential‑parameter fitting stage is omitted because the paper explicitly reports the fitted scaling multipliers (U₀×0.85, ρ₀×1.06, L×0.88) and these are used directly. Lattice‑parameter optimisation is excluded per taskability scope.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "zone_center_frequencies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "array",
        "items": {
          "mode": "string (one of Ag, B1g, B2g, B3g, Au, B1u, B2u)",
          "frequency": "float (cm⁻¹)"
        }
      },
      "description": "Seven optically‑active zone‑centre mode frequencies. Each mode must match the hidden reference within ±5 cm⁻¹."
    },
    {
      "file": "density_of_states.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": [
          "bin_centers",
          "density"
        ],
        "bin_centers": "array of float (cm⁻¹)",
        "density": "array of float (arbitrary units)"
      },
      "description": "Histogram of the vibrational density of states with 1 cm⁻¹ resolution. Checked for bin count, reasonable peak positions, and shape consistency."
    },
    {
      "file": "heat_capacity.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "array",
        "items": {
          "temperature": "float (K)",
          "Cv": "float (cal·mol⁻¹·K⁻¹)"
        }
      },
      "description": "Constant‑volume heat capacity curve from 0 to 100 K. The checker recomputes Cv from the submitted DOS for self‑consistency, then compares Cv at selected temperatures to the hidden paper curve within ±2 cal·mol⁻¹·K⁻¹."
    },
    {
      "file": "lattice_energy.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "description": "Single float (kcal/mol)"
      },
      "description": "Lattice energy at the experimental 5.3 K geometry, extrapolated to infinite cutoff. Scored against the hidden gold (−9.06 kcal/mol) with tolerance ±0.5 kcal/mol."
    }
  ],
  "notes": "The potential‑parameter fitting stage is omitted because the paper explicitly reports the fitted scaling multipliers (U₀×0.85, ρ₀×1.06, L×0.88) and these are used directly. Lattice‑parameter optimisation is excluded per taskability scope."
}
```

## How you are scored
A hidden verifier reads your output artifacts and independently scores each stage:
- Zone‑centre frequencies: each of the seven mode frequencies is compared to a hidden reference; credit is proportional to the fraction of modes that fall within an acceptable tolerance.
- Density of states: the submitted histogram is checked for bin count, shape consistency, and that major peak positions are plausible.
- Heat capacity: the verifier recomputes Cᵥ from your submitted DOS to verify self‑consistency; then the Cᵥ values at selected temperatures are compared against a hidden reference curve, again awarding credit based on agreement within a tolerance.
- Lattice energy: the submitted value is compared directly to a hidden reference; full credit if the difference is within a tolerance, partial otherwise.

The final reward is a weighted sum of the scores from each stage; the zone‑centre frequencies and heat capacity carry the largest weight. Providing numbers that are merely copied from the literature without running the dynamics will not satisfy the internal consistency checks.
