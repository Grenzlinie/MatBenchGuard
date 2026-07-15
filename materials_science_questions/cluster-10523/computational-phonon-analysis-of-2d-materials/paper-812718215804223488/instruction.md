# Phonon Properties of Type-I Si and Ge Clathrates via DFT and Lattice Dynamics

## Problem background
Type-I silicon and germanium clathrates are cage-like crystals consisting of a host framework with large voids that can encapsulate guest atoms. These materials are attractive for thermoelectric applications because filling the cages often drastically reduces lattice thermal conductivity while retaining good electrical transport — the “phonon glass electron crystal” concept. The key to understanding this reduction lies in the phonon dynamics: guest atoms introduce low-frequency “rattling” modes that interact with the host phonons, causing avoided crossings, flat bands, and modifications to the overall phonon spectrum. Quantifying how these changes affect phonon group velocities, Grüneisen parameters, Debye temperatures, and ultimately lattice thermal conductivity is crucial for engineering improved thermoelectrics. This task computes those phonon properties from first principles for empty and guest-filled Si and Ge clathrates.

## Approach
The work employs density functional theory (DFT) with the PBEsol exchange-correlation functional to relax the crystal structures and then compute harmonic and quasi-harmonic phonon properties using the phonopy package. For five clathrate compositions (empty Si46, Na-filled Na8Si46, K-filled K8Si46, empty Ge46, and K-filled K8Ge44 with two framework vacancies), the procedure first performs full geometry optimization. From the relaxed structures, harmonic phonon eigenfrequencies and eigenvectors are obtained on a dense q‑point mesh. To capture anharmonic effects, phonon frequencies are also calculated at isotropically strained volumes (+5% and –5%). The harmonic phonon dispersions are extracted along a standard high‑symmetry path in the cubic Brillouin zone. From these data we compute: the spectral width of the phonon band structure; mode‑resolved group velocities (v_TA, v_LA) and Debye temperatures (θ_TA, θ_LA); mode Grüneisen parameters (γ_TA, γ_LA); the average Grüneisen parameter at 300 K; and the lattice thermal conductivity κ_l at 300 K, using the Debye‑Callaway formalism with the Asen‑Palmer modification. The analysis compares empty host frameworks with guest‑filled ones to reveal how the guests alter the phonon dynamics and thermal transport.

## Reproduction target
Produce two output files for the five clathrate compositions (Si46, Na8Si46, K8Si46, Ge46, K8Ge44□2):

1. **computed_properties.json** – an array of objects, each containing the composition name and the following computed quantities: gamma_300, gamma_TA, gamma_LA, v_TA (km/s), v_LA (km/s), v_s (km/s, average sound velocity), theta_TA (K), theta_LA (K), theta_D (K), spectral_width (cm⁻¹), rattler_freq (cm⁻¹, set to null for empty compositions), and kappa_l_300 (W/m·K).

2. **phonon_dispersions.json** – for each composition, the phonon dispersion along a high‑symmetry path (e.g., Γ–X–M–Γ–R–X), with q‑point fractional coordinates, frequencies for every phonon branch (list of arrays), and a mapping of high‑symmetry point labels to their indices in the q‑point list.

The verifier will compare your computed properties against reference values and will recompute the spectral width from the band structure data to verify consistency.

## Assets

- All-electron or pseudopotential DFT code (FHI-aims or Quantum ESPRESSO): https://aimsclub.fhi-berlin.mpg.de/ (FHI-aims) or https://www.quantum-espresso.org/
- Phonopy: phonopy
- Crystal structures of type-I Si and Ge clathrates (empty and filled)

## Workflow steps

### Step 1: DFT geometry relaxation
- Role: process
- Action: For each clathrate composition (Si46, Na8Si46, K8Si46, Ge46, K8Ge44□2), perform DFT geometry optimization using the PBEsol exchange-correlation functional. Relax atomic positions and lattice vectors until forces are below 0.001 eV/Å. Output the relaxed structures (lattice vectors and atomic coordinates) for later phonon calculations.
- Evidence: `/app/outputs/relaxed_structures.json`

### Step 2: Harmonic phonon calculation
- Role: process
- Action: For each relaxed structure, compute harmonic phonon eigenfrequencies and eigenvectors using phonopy (finite displacement or DFPT). Save the raw phonon data (force constants or band.yaml) for later dispersion extraction and property calculations.
- Evidence: `/app/outputs/phonon_data.zip`

### Step 3: Quasi-harmonic phonon at strained volumes
- Role: process
- Action: For each composition, create unit cells with +5% and -5% isotropic volume strain, then compute phonon frequencies at each strained volume using the same harmonic method as step 2. Output the strained‑volume phonon data needed to compute Grüneisen parameters.
- Evidence: `/app/outputs/strained_phonon_data.zip`

### Step 4: Compute phonon properties and lattice thermal conductivity
- Role: scored (load-bearing)
- Action: From the harmonic and quasi-harmonic phonon data, compute for each composition: spectral width (max − min frequency on the high‑symmetry path), rattler frequency (for filled systems), average group velocities v_TA, v_LA, v_s (km/s), Debye temperatures θ_TA, θ_LA, θ_D (K), mode‑resolved Grüneisen parameters γ_TA, γ_LA, the average Grüneisen parameter at 300 K (γ̄|₃₀₀), and the lattice thermal conductivity κ_l at 300 K (W/m·K) using the Debye‑Callaway formalism with the Asen‑Palmer modification. Write all values into computed_properties.json.
- Output file: `/app/outputs/computed_properties.json`
- Format: json
- Contract: Array of objects. Each object has keys: 'name' (str), 'gamma_300' (float), 'gamma_TA' (float), 'gamma_LA' (float), 'v_TA' (float, km/s), 'v_LA' (float, km/s), 'v_s' (float, km/s), 'theta_TA' (float, K), 'theta_LA' (float, K), 'theta_D' (float, K), 'kappa_l_300' (float, W/m·K), 'spectral_width' (float, cm⁻¹), 'rattler_freq' (float or null, cm⁻¹). For empty compositions, 'rattler_freq' is null.
- Scoring: scored by hidden verifier

### Step 5: Phonon band structure data
- Role: scored
- Action: Using the harmonic phonon eigenfrequencies from step 2, extract the phonon dispersion along a standard high‑symmetry k‑path for the cubic Pm-3n space group (e.g., Γ–X–M–Γ–R–X). For each composition, output a JSON object containing: the list of q‑point fractional coordinates, the frequencies for every phonon branch (list of arrays), and a mapping of high‑symmetry labels to q‑point indices.
- Output file: `/app/outputs/phonon_dispersions.json`
- Format: json
- Contract: Object mapping composition name (str) to an object with keys: 'qpoints' (list of lists of three floats [kx,ky,kz]), 'frequencies' (list of list of floats, each inner list is one phonon branch’s frequencies in cm⁻¹ along the q‑path), 'high_symmetry_labels' (object mapping label string like 'Gamma','X','M','R' to the index in the qpoints list).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/computed_properties.json`
- `/app/outputs/phonon_dispersions.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### computed_properties.json
- path: `/app/outputs/computed_properties.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Computed phonon properties and lattice thermal conductivity for all clathrate compositions, compared against hidden reference values from the paper’s Table 1.
- schema:
  - `type`: array
  - `required`: `name`, `gamma_300`, `gamma_TA`, `gamma_LA`, `v_TA`, `v_LA`, `v_s`, `theta_TA`, `theta_LA`, `theta_D`, `kappa_l_300`, `spectral_width`, `rattler_freq`
  - `items`:
    - `name`: string
    - `gamma_300`: number
    - `gamma_TA`: number
    - `gamma_LA`: number
    - `v_TA`: number (km/s)
    - `v_LA`: number (km/s)
    - `v_s`: number (km/s)
    - `theta_TA`: number (K)
    - `theta_LA`: number (K)
    - `theta_D`: number (K)
    - `kappa_l_300`: number (W/m·K)
    - `spectral_width`: number (cm⁻¹)
    - `rattler_freq`: number or null (cm⁻¹)

### phonon_dispersions.json
- path: `/app/outputs/phonon_dispersions.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Raw phonon band structure data used by the checker to recompute spectral width and verify the existence of localized flat bands.
- schema:
  - `type`: object
  - `required`:
  - `items`:
    - `<composition_name>`:
      - `qpoints`: list of [kx,ky,kz]
      - `frequencies`: list of list of floats (cm⁻¹)
      - `high_symmetry_labels`: object { label: index }

Notes: Only the compositions Si46, Na8Si46, K8Si46, Ge46, and K8Ge44□2 are required. Ba8Ge43□3 is excluded because its Grüneisen parameter diverges and κ_l was not computed in the paper.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "computed_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "array",
        "required": [
          "name",
          "gamma_300",
          "gamma_TA",
          "gamma_LA",
          "v_TA",
          "v_LA",
          "v_s",
          "theta_TA",
          "theta_LA",
          "theta_D",
          "kappa_l_300",
          "spectral_width",
          "rattler_freq"
        ],
        "items": {
          "name": "string",
          "gamma_300": "number",
          "gamma_TA": "number",
          "gamma_LA": "number",
          "v_TA": "number (km/s)",
          "v_LA": "number (km/s)",
          "v_s": "number (km/s)",
          "theta_TA": "number (K)",
          "theta_LA": "number (K)",
          "theta_D": "number (K)",
          "kappa_l_300": "number (W/m·K)",
          "spectral_width": "number (cm⁻¹)",
          "rattler_freq": "number or null (cm⁻¹)"
        }
      },
      "description": "Computed phonon properties and lattice thermal conductivity for all clathrate compositions, compared against hidden reference values from the paper’s Table 1."
    },
    {
      "file": "phonon_dispersions.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": [],
        "items": {
          "<composition_name>": {
            "qpoints": "list of [kx,ky,kz]",
            "frequencies": "list of list of floats (cm⁻¹)",
            "high_symmetry_labels": "object { label: index }"
          }
        }
      },
      "description": "Raw phonon band structure data used by the checker to recompute spectral width and verify the existence of localized flat bands."
    }
  ],
  "notes": "Only the compositions Si46, Na8Si46, K8Si46, Ge46, and K8Ge44□2 are required. Ba8Ge43□3 is excluded because its Grüneisen parameter diverges and κ_l was not computed in the paper."
}
```

## How you are scored
A hidden verifier evaluates your submission by examining both output artifacts.

For **computed_properties.json**, the checker compares your reported values against reference targets (with tolerances that absorb legitimate differences between DFT implementations) and checks the ordering of rattler frequencies. For **phonon_dispersions.json**, the checker recomputes the maximum minus minimum frequency (spectral width) from your band structure and cross‑checks it with your reported value; it also scans for flat‑band regions indicative of localized modes. The final reward is a weighted combination across these checks, with the properties table carrying the majority of the score.

Simply reporting plausible numbers without actually executing the DFT and phonon calculations will not suffice: the checker demands self‑consistency between the two artifacts and may recompute derived quantities that cannot be fabricated without genuine raw data.
