# Thermoelectric Transport Modeling and Figure of Merit Enhancement via Minority Carrier Blocking

## Problem background
Thermoelectric materials convert heat to electricity, but their efficiency is limited by bipolar transport — when both electrons and holes conduct, the Seebeck coefficient is reduced and the thermal conductivity increased. This task investigates a strategy to suppress bipolar conduction by embedding heterostructure barriers that selectively block minority carriers while leaving majority carriers largely unaffected. The goal is to compute the resulting figure of merit zT for several narrow-band-gap semiconductors and compare it with the bulk, barrier-free case.

## Approach
The model is a near-equilibrium multiband Boltzmann transport calculation under the relaxation-time approximation, using a modified‑Kane nonparabolic dispersion. Energy‑dependent scattering is treated via Matthiessen’s rule, including acoustic deformation potential, screened polar optical phonon, ionized‑impurity, and short‑range defect scattering. Heterostructure barriers are introduced through a single‑barrier Wentzel-Kramers-Brillouin (WKB) transmission coefficient applied in the minority‑carrier band only (zero barrier in the majority‑carrier band). The full two‑carrier transport equations yield partial electron and hole properties, from which the total electrical conductivity, Seebeck coefficient, and electronic thermal conductivity (including the bipolar term) are obtained. Combined with a constant lattice thermal conductivity, the dimensionless figure of merit zT is computed. This is done for six material/type/temperature conditions, both with and without minority‑carrier blocking, over a wide carrier concentration range. The required band-structure parameters and scattering coefficients for each material are supplied in the instruction.

## Reproduction target
Implement the transport model described above and compute, for the following six conditions: n‑type Bi2Te2.7Se0.3 at 500 K, p‑type Bi0.5Sb1.5Te3 at 500 K, n‑type Mg2Si0.4Sn0.6 at 900 K, p‑type Mg2Si0.4Sn0.6 at 900 K, n‑type Si0.8Ge0.2 at 1200 K, and p‑type Si0.8Ge0.2 at 1200 K — (i) the electrical conductivity, Seebeck coefficient, electronic (including bipolar) thermal conductivity, and zT as a function of carrier concentration over a log‑spaced grid from 1e17 to 1e21 cm⁻³; (ii) the same quantities when a 20‑nm‑wide barrier of height 10*kB*T is present in the minority‑carrier band (majority‑carrier barrier height zero); (iii) the maximum zT for each of the bulk and barrier cases. Use the band, scattering, and defect parameters provided for each material, and constant lattice thermal conductivities: 0.5 W m⁻¹ K⁻¹ for Bi2Te3‑based alloys, 0.8 W m⁻¹ K⁻¹ for Mg2Si0.4Sn0.6 and Si0.8Ge0.2. The final output is a single JSON file containing the full zT curves and the scalar maximum zT values for all configurations.

## Material parameters

The following tables provide the band structure, scattering, and defect parameters needed for the six material conditions. Use these values directly in the transport model. The effective masses are single-valley values; the final density-of-states effective mass must be multiplied by $N_{\text{val}}^{2/3}$, where $N_{\text{val}}$ is the valley degeneracy (6 for all bands in Bi₂Te₃-based alloys, as listed in the paper). For Si₁₋ₓGeₓ and Mg₂Si₁₋ₓSnₓ, the valley degeneracy is given in the table captions.

### Bi₂Te₃-based alloys

| Parameter | n-type Bi₂Te₂.₇Se₀.₃ (x=0.3) at 500 K | p-type Bi₀.₅Sb₁.₅Te₃ at 500 K |
|-----------|-----------------------------------------|--------------------------------|
| Band gap (eV) | 0.183 | 0.211 |
| Band offset between 1st and 2nd conduction bands (eV) | 0.23 | 0.23 |
| Band offset between 1st and 2nd valence bands (eV) | 0.27 | 0.27 |
| Electron effective mass of 1st conduction band (m₀) | 0.2147 | 0.17 |
| Electron effective mass of 2nd conduction band (m₀) | 0.2247 | 0.18 |
| Hole effective mass of 1st valence band (m₀) | 0.3936 | 0.36 |
| Hole effective mass of 2nd valence band (m₀) | 0.3936 | 0.36 |
| Nonparabolicity α of 1st conduction band (eV⁻¹) | 0 | 0 |
| Nonparabolicity α of 2nd conduction band (eV⁻¹) | 1.0 | 1.0 |
| Nonparabolicity α of 1st valence band (eV⁻¹) | 0.6 | 0.6 |
| Nonparabolicity α of 2nd valence band (eV⁻¹) | 2.0 | 2.0 |
| Acoustic phonon deformation potential Dₐ for electrons (eV) | 19.0 | 20.0 |
| Acoustic phonon deformation potential Dₐ for holes (eV) | 23.7 | 20.0 |
| Elastic constant Cₗ (N m⁻²) | 7.1 × 10¹⁰ | 7.1 × 10¹⁰ |
| Compensation ratio r_c | 1 | 1 |
| Nonionized defect density N_V (cm⁻³) | 1 × 10¹⁹ | 3 × 10¹⁹ |
| Short-range potential of defects U_V (J m⁻³) | 1 × 10⁻⁴⁶ | 1 × 10⁻⁴⁶ |

### Si₀.₈Ge₀.₂ (x=0.2) at 1200 K

The conduction band valley degeneracy is 6, the valence band degeneracy is 1.

| Parameter | n-type Si₀.₈Ge₀.₂ | p-type Si₀.₈Ge₀.₂ |
|-----------|-------------------|-------------------|
| Band gap (eV) | 0.667 | 0.667 |
| Band offset between 1st and 2nd conduction bands (eV) | 0.162 | 0.162 |
| Band offset between 1st and 2nd valence bands (eV) | 0.0932 | 0.0932 |
| Electron effective mass of 1st conduction band (m₀) | 0.32 | 0.32 |
| Electron effective mass of 2nd conduction band (m₀) | 0.32 | 0.32 |
| Hole effective mass of 1st valence band (m₀) | 0.59 | 0.59 |
| Hole effective mass of 2nd valence band (m₀) | 0.203 | 0.203 |
| Nonparabolicity α (all bands) | 0 | 0 |
| Acoustic phonon deformation potential Dₐ for electrons (eV) | 20 | 20 |
| Acoustic phonon deformation potential Dₐ for holes (eV) | 15 | 15 |
| Elastic constant Cₗ (N m⁻²) | 9.8 × 10¹⁰ | 9.8 × 10¹⁰ |
| Compensation ratio r_c | 4 | 1.4 |
| Nonionized defect density N_V (cm⁻³) | 5 × 10¹⁸ | not used |
| Short-range potential of defects U_V (J m⁻³) | 1 × 10⁻⁴⁶ | not used |

### Mg₂Si₀.₄Sn₀.₆ at 900 K

The conduction band valley degeneracy is 3, the valence band degeneracy is 1. Parameters are taken from Bahk et al., Phys. Rev. B 89, 075204 (2014).

| Parameter | n-type Mg₂Si₀.₄Sn₀.₆ | p-type Mg₂Si₀.₄Sn₀.₆ |
|-----------|------------------------|------------------------|
| Band gap (eV) | 0.25 | 0.25 |
| Band offset between 1st and 2nd conduction bands (eV) | 0.0 | 0.0 |
| Band offset between 1st and 2nd valence bands (eV) | 0.05 | 0.05 |
| Electron effective mass of 1st conduction band (m₀) | 0.5 | 0.5 |
| Electron effective mass of 2nd conduction band (m₀) | 0.5 | 0.5 |
| Hole effective mass of 1st valence band (m₀) | 0.8 | 0.8 |
| Hole effective mass of 2nd valence band (m₀) | 0.1 | 0.1 |
| Nonparabolicity α (all bands) | 0 | 0 |
| Acoustic phonon deformation potential Dₐ for electrons (eV) | 14 | 14 |
| Acoustic phonon deformation potential Dₐ for holes (eV) | 14 | 14 |
| Elastic constant Cₗ (N m⁻²) | 1.0 × 10¹¹ | 1.0 × 10¹¹ |
| Compensation ratio r_c | 1 | 1 |
| Nonionized defect density N_V (cm⁻³) | 1 × 10¹⁹ | 1 × 10¹⁹ |
| Short-range potential of defects U_V (J m⁻³) | 1 × 10⁻⁴⁶ | 1 × 10⁻⁴⁶ |

## Assets

- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Implement transport model
- Role: process
- Action: Write Python code that implements the nonparabolic multiband Boltzmann transport model with energy‑dependent scattering and WKB barrier transmission. Include calculation of: density‑of‑states and directional‑averaged squared velocity for a nonparabolic band; differential conductivity; energy‑dependent scattering time via Matthiessen’s rule (acoustic deformation potential, screened polar optical phonon, ionized impurity, short‑range defect scattering); single‑barrier WKB transmission coefficient; integrals for electrical conductivity, Seebeck coefficient, and electronic thermal conductivity (including the bipolar term) for a given carrier concentration and temperature. The code should be modular and callable by the subsequent scored step.
- Evidence: `/app/outputs/implementation_check.log`

### Step 2: Compute thermoelectric figure of merit for all conditions
- Role: scored (load-bearing)
- Action: Using the transport code from step 1 and the band/scattering parameters provided in the instruction for the six conditions (n‑type Bi2Te2.7Se0.3 at 500 K, p‑type Bi0.5Sb1.5Te3 at 500 K, n‑type and p‑type Mg2Si0.4Sn0.6 at 900 K, n‑type and p‑type Si0.8Ge0.2 at 1200 K), compute the electrical conductivity, Seebeck coefficient, electronic thermal conductivity (including bipolar), and dimensionless figure of merit zT as a function of carrier concentration for both the bulk (no barriers, transmission=1) and the minority‑carrier blocking scenario (20‑nm‑wide barriers with barrier height 10*kB*T in the minority‑carrier band, zero barrier height in the majority‑carrier band). Assume constant lattice thermal conductivities: 0.5 W m⁻¹ K⁻¹ for Bi2Te3‑based alloys, 0.8 W m⁻¹ K⁻¹ for Mg2Si0.4Sn0.6, and 0.8 W m⁻¹ K⁻¹ for Si0.8Ge0.2. Vary carrier concentration over a wide log‑spaced range (e.g., 200 points from 1e17 to 1e21 cm⁻³). Output all results in a single JSON file thermoelectric_results.json.
- Output file: `/app/outputs/thermoelectric_results.json`
- Format: json
- Contract: A JSON object with top‑level keys identifying each condition (e.g., "n_Bi2Te2.7Se0.3_500K_kappa_lat_0.5"). Each value is an object containing: temperature_K (number), kappa_lat_W_mK (number), carrier_concentration_cm3 (array of numbers), sigma_bulk_S_m (array), S_bulk_microV_K (array), kappa_elec_bulk_W_mK (array), kappa_bi_bulk_W_mK (array), sigma_barrier_S_m (array), S_barrier_microV_K (array), kappa_elec_barrier_W_mK (array), kappa_bi_barrier_W_mK (array), zT_bulk (array), zT_barrier (array), max_zT_bulk (number), max_zT_barrier (number). All arrays share the same length and correspond to the carrier concentrations.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/thermoelectric_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### thermoelectric_results.json
- path: `/app/outputs/thermoelectric_results.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Thermoelectric properties and zT vs. carrier concentration for the six material/type/temperature conditions under bulk and minority‑carrier blocking scenarios. The checker recomputes zT from the provided transport coefficients and compares max_zT values to hidden paper‑reported gold.
- schema:
  - `type`: object
  - `description`: Top-level keys identify each condition (e.g., n_Bi2Te2.7Se0.3_500K_kappa_lat_0.5). Each value is an object with required fields: temperature_K (number), kappa_lat_W_mK (number), carrier_concentration_cm3 (array of numbers), sigma_bulk_S_m (array), S_bulk_microV_K (array), kappa_elec_bulk_W_mK (array), kappa_bi_bulk_W_mK (array), sigma_barrier_S_m (array), S_barrier_microV_K (array), kappa_elec_barrier_W_mK (array), kappa_bi_barrier_W_mK (array), zT_bulk (array), zT_barrier (array), max_zT_bulk (number), max_zT_barrier (number). All arrays are of equal length and correspond to the carrier concentrations.

Notes: The checker will internally recompute zT = S²σT/(κ_elec + κ_lat) from each set of coefficients, verify self‑consistency with the stored zT arrays, then extract max_zT and compare the bulk and barrier maximums to gold. The score is monotonic: meeting or exceeding the paper‑reported zT earns full credit, and only worse results are penalized.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "thermoelectric_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "description": "Top-level keys identify each condition (e.g., n_Bi2Te2.7Se0.3_500K_kappa_lat_0.5). Each value is an object with required fields: temperature_K (number), kappa_lat_W_mK (number), carrier_concentration_cm3 (array of numbers), sigma_bulk_S_m (array), S_bulk_microV_K (array), kappa_elec_bulk_W_mK (array), kappa_bi_bulk_W_mK (array), sigma_barrier_S_m (array), S_barrier_microV_K (array), kappa_elec_barrier_W_mK (array), kappa_bi_barrier_W_mK (array), zT_bulk (array), zT_barrier (array), max_zT_bulk (number), max_zT_barrier (number). All arrays are of equal length and correspond to the carrier concentrations."
      },
      "description": "Thermoelectric properties and zT vs. carrier concentration for the six material/type/temperature conditions under bulk and minority‑carrier blocking scenarios. The checker recomputes zT from the provided transport coefficients and compares max_zT values to hidden paper‑reported gold."
    }
  ],
  "notes": "The checker will internally recompute zT = S²σT/(κ_elec + κ_lat) from each set of coefficients, verify self‑consistency with the stored zT arrays, then extract max_zT and compare the bulk and barrier maximums to gold. The score is monotonic: meeting or exceeding the paper‑reported zT earns full credit, and only worse results are penalized."
}
```

## How you are scored
A hidden verifier independently scores each stage of the workflow and combines them by weight into a final reward. It reads your JSON output, recomputes zT from the provided transport coefficients to check self‑consistency, and extracts the maximum bulk and barrier zT values. Those maxima are compared against hidden paper‑reported reference values using a tolerance, and the verifier also checks that the barrier case yields a higher maximum zT than the corresponding bulk case. Merely reporting the paper’s numbers is not enough; the verifier uses your raw data to recompute the quantities of interest. No gold values or tolerances are revealed in the instruction.
