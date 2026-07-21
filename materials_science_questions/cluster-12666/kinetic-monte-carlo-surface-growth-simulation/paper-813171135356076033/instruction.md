# Kinetic Monte Carlo N2 Desorption TPD Simulation on Co and Ni Adlayer Clusters

## Problem background
Submonolayer bimetallic catalysts often exhibit properties that are not simple averages of the parent metals. N₂ desorption is a crucial step in ammonia decomposition, but the relationship between nitrogen binding energy and the temperature of the desorption peak is non‑trivial when multiple adsorption sites and lateral interactions are present. This task requires implementing kinetic Monte Carlo (KMC) simulations of N₂ temperature‑programmed desorption (TPD) on hexagonal Co and Ni adlayer clusters on Pt(111). The goal is to produce simulated TPD spectra and site‑resolved kinetic fingerprints, and to determine the desorption peak temperatures and which sites dominate the rate for each surface.

## Approach
Build a lattice KMC simulation for each catalytic surface using a variable‑rate continuous‑time Monte Carlo algorithm. The surface is a hexagonal admetal cluster (Co or Ni) on a Pt(111) substrate. The model tracks N atoms on a set of site types: fcc hollow, hcp hollow, step (110), step (100), and edge sites. Allowed events are N diffusion between neighbouring sites, and N+N association to form N₂ (which then desorbs immediately). The activation energies, binding energies, pre‑exponential factors, and pairwise lateral interaction parameters for each site and event are taken from the provided file `/resources/kmc_inputs.json` (DFT‑derived parameters, see description below). Run TPD from an initial N coverage of 0.3 ML, with a heating rate of 3 K/s. Average the results over 20 independent random seeds. (You may store intermediate trajectories in memory or temporary files; the only required outputs are the scored artifacts listed at the end of this instruction.) Post‑process the KMC histories to obtain temperature‑binned desorption rates and time‑averaged site‑specific occupation probabilities and association rates, separately for the Co/Pt and Ni/Pt cases.

## KMC input parameters file (`kmc_inputs.json`)

The file `/resources/kmc_inputs.json` provides all energetic and kinetic parameters needed to define the KMC model. It is structured as follows:

- Top‑level keys: `"Co_Pt"` and `"Ni_Pt"` (one object for each bimetallic surface).
- Each surface object contains:
  - `"lattice"`: description of the simulation cell (e.g. number of sites, site coordinates, neighbour lists).
  - `"site_energies"`: a dictionary mapping each site type (string) to its nitrogen binding energy `"E_bind"` (in eV). The binding energy is defined as the energy of one N atom on that site relative to gas‑phase N₂ (with zero‑point energy corrections already applied).
  - `"diffusion_events"`: a list of diffusion pathways. Each entry has:
    - `"site_from"`, `"site_to"`: site type strings.
    - `"E_diff"` (eV): intrinsic diffusion barrier at zero coverage.
    - `"prefactor_diff"` (s⁻¹): pre‑exponential factor for this hop.
  - `"association_events"`: a list of N+N association processes. Each entry specifies:
    - `"site_1"`, `"site_2"`: site types that can form an N₂ pair (must be occupied by N and be within the required distance).
    - `"E_assoc"` (eV): association barrier (energy of the transition state relative to the two‑atom initial state, at zero coverage).
    - `"prefactor_assoc"` (s⁻¹): pre‑exponential factor for this reaction.
  - `"lateral_interactions"`: an object describing N–N pairwise interactions. It contains:
    - `"type"`: `"pairwise"` (first‑nearest‑neighbour additive).
    - `"V_NN"` (eV): the N–N nearest‑neighbour interaction energy (positive for repulsive, negative for attractive).
    - `"cutoff_distance"` (Å): distance threshold to consider two sites as neighbours.
- Notes: all energies are in eV; pre‑factors are in s⁻¹. The Boltzmann constant is `k_B = 8.617333262145e-5 eV/K`.

### Event rate calculation and handling of lateral interactions

Rates are computed according to transition state theory using the Arrhenius form:

```
k = prefactor * exp(-E_barrier / (k_B T))
```

where `prefactor` is the event‑specific pre‑exponential factor taken directly from the JSON, and `E_barrier` is the effective activation energy that includes the influence of N–N lateral interactions. The model employs a lattice‑gas with first‑nearest‑neighbour pairwise additive interactions. The total energy of an N atom occupying site `s` is

```
E_total(s) = E_bind(site_type(s)) + Σ_{occupied neighbour sites n} V_NN
```

where `V_NN` is the pairwise interaction energy from `kmc_inputs.json` (the same value is used regardless of the site types).

The effective barrier for a **diffusion event** (hop from site `i` to site `j`) is obtained by symmetrically splitting the energy difference between final and initial states:

```
E_barrier = E_diff + 0.5 * (E_final - E_initial)
E_initial = E_total(i)   (with the N atom present on i)
E_final   = E_total(j)   (with the N atom moved to j; site j must be empty)
```

If site `j` is occupied, the hop is forbidden.

For an **association event** (two N atoms on nearby sites `i` and `j` reacting to form N₂, which then desorbs), the barrier is referenced to the initial two‑atom state. The lateral interactions affect the initial energy but the association barrier itself (`E_assoc` from the JSON) is already defined relative to the two‑atom initial state at zero coverage. Therefore the effective barrier is

```
E_barrier = E_assoc + (E_initial_pair - E_zero_coverage_pair)
```

where
```
E_initial_pair = E_total(i) + E_total(j)   (both sites occupied, interactions counted once)
```

and `E_zero_coverage_pair = E_bind(site_type(i)) + E_bind(site_type(j))` (the energy of the two isolated N atoms). Note that `E_initial_pair - E_zero_coverage_pair` is simply the sum of the interaction energies from all occupied neighbours of `i` (excluding `j`) and of `j` (excluding `i`). In practice this is equivalent to adding the lateral interaction correction to the zero‑coverage barrier.

### Physical constants
During the simulation use `k_B = 8.617333262145e-5 eV/K`. All times and rates should be in seconds.

## Reproduction target
From the KMC outputs, produce the following scored artifacts under `/app/outputs`:
- `tpd_co.csv`: desorption rate vs. temperature for the Co/Pt surface (columns `temperature` [K] and `desorption_rate` [s⁻¹], at least 100 rows covering 400–1000 K).
- `tpd_ni.csv`: analogous desorption curve for the Ni/Pt surface (covering 400–800 K).
- `site_analysis_co.json`: mapping each site type (`fcc`, `hcp`, `step_110`, `step_100`, `edge`) to an object with `average_occupation` (float, 0–1) and `average_association_rate` (float, ≥0), computed in the 600–800 K temperature window.
- `site_analysis_ni.json`: same structure for the Ni/Pt surface, computed over 500–700 K.
- `peak_temperatures.json`: object with keys `co_peak_T` and `ni_peak_T` giving the temperature of maximum desorption rate for each surface. The performance will be assessed by evaluating the peak values, the relative ordering of the two peaks, and the self‑consistency of the site statistics.

## Assets

- NumPy: numpy
- SciPy: scipy
- Matplotlib: matplotlib
- KMC input parameters (`/resources/kmc_inputs.json`)

## Workflow steps

### Step 1: Run KMC TPD simulation for Co/Pt cluster
- Role: process
- Action: Implement a lattice KMC solver for N₂ desorption on a hexagonal Co cluster on Pt(111) using the energetics from the provided `/resources/kmc_inputs.json`. Use the formulas described above to compute event rates. Run TPD with heating rate 3 K/s, initial N coverage 0.3, averaging over 20 random seeds. Record full trajectories (timestamps, temperatures, site occupations, association events) in memory or temporary storage—no external trajectory file is required as output.
- Evidence: (no permanent output file – the results feed the next steps)

### Step 2: Run KMC TPD simulation for Ni/Pt cluster
- Role: process
- Action: As in Step 1 but for the Ni/Pt surface.
- Evidence: (no permanent output file)

### Step 3: Compute Co/Pt desorption curve
- Role: scored (load‑bearing)
- Action: From the Co/Pt simulation results, compute the temperature‑binned desorption rate averaged over seeds. Write `tpd_co.csv` with columns `temperature` (K) and `desorption_rate` (s⁻¹).
- Output file: `/app/outputs/tpd_co.csv`
- Format: csv
- Contract: Columns: `temperature` (float, K), `desorption_rate` (float, s⁻¹). At least 100 rows covering 400‑1000 K.
- Scoring: scored by hidden verifier

### Step 4: Compute Co/Pt site‑resolved kinetics
- Role: scored
- Action: Using the Co/Pt simulation results, compute time‑averaged site‑specific occupation probabilities and association rates in the temperature window 600‑800 K. Write `site_analysis_co.json` as a mapping from site type (`fcc`, `hcp`, `step_110`, `step_100`, `edge`) to an object with `average_occupation` (float) and `average_association_rate` (float).
- Output file: `/app/outputs/site_analysis_co.json`
- Format: json
- Contract: `{"site_type": {"average_occupation": float (0‑1), "average_association_rate": float (≥0)}}` for each of `fcc`, `hcp`, `step_110`, `step_100`, `edge`.
- Scoring: scored by hidden verifier

### Step 5: Compute Ni/Pt desorption curve
- Role: scored (load‑bearing)
- Action: From the Ni/Pt simulation results, compute the temperature‑binned desorption rate and write `tpd_ni.csv` (columns `temperature` [K], `desorption_rate` [s⁻¹]). At least 100 rows covering 400‑800 K.
- Output file: `/app/outputs/tpd_ni.csv`
- Format: csv
- Scoring: scored by hidden verifier

### Step 6: Compute Ni/Pt site‑resolved kinetics
- Role: scored
- Action: Using the Ni/Pt results, compute time‑averaged site‑specific occupation probabilities and association rates in the temperature window 500‑700 K. Write `site_analysis_ni.json` with the same structure as the Co/Pt file.
- Output file: `/app/outputs/site_analysis_ni.json`
- Format: json
- Scoring: scored by hidden verifier

### Step 7: Compute peak temperatures
- Role: scored
- Action: Read `tpd_co.csv` and `tpd_ni.csv`. Locate the temperature at which `desorption_rate` is maximum in each. Write `peak_temperatures.json` with keys `co_peak_T` and `ni_peak_T` (values in Kelvin).
- Output file: `/app/outputs/peak_temperatures.json`
- Format: json
- Contract: `{"co_peak_T": float (K), "ni_peak_T": float (K)}`
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/tpd_co.csv`
- `/app/outputs/site_analysis_co.json`
- `/app/outputs/tpd_ni.csv`
- `/app/outputs/site_analysis_ni.json`
- `/app/outputs/peak_temperatures.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### tpd_co.csv
- path: `/app/outputs/tpd_co.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Co/Pt TPD spectrum. The checker recomputes the peak temperature from this data and compares to an expected reference value (within tolerance), and also verifies that the Co peak is higher than the Ni peak.
- schema:
  - `type`: table
  - `required_columns`: `temperature`, `desorption_rate`
  - `units`:
    - `temperature`: K
    - `desorption_rate`: s^{-1}

### site_analysis_co.json
- path: `/app/outputs/site_analysis_co.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Site‑resolved kinetics for Co/Pt. Checked for expected site types, occupation in [0,1], and non‑negative association rates.
- schema:
  - `type`: object
  - `required`:
    - `fcc`:
      - `average_occupation`: float
      - `average_association_rate`: float
    - `hcp`:
      - `average_occupation`: float
      - `average_association_rate`: float
    - `step_110`:
      - `average_occupation`: float
      - `average_association_rate`: float
    - `step_100`:
      - `average_occupation`: float
      - `average_association_rate`: float
    - `edge`:
      - `average_occupation`: float
      - `average_association_rate`: float

### tpd_ni.csv
- path: `/app/outputs/tpd_ni.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Ni/Pt TPD spectrum. The checker recomputes the peak temperature and compares to an expected reference value.
- schema:
  - `type`: table
  - `required_columns`: `temperature`, `desorption_rate`
  - `units`:
    - `temperature`: K
    - `desorption_rate`: s^{-1}

### site_analysis_ni.json
- path: `/app/outputs/site_analysis_ni.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Site‑resolved kinetics for Ni/Pt.
- schema:
  - `type`: object
  - `required`:
    - `fcc`:
      - `average_occupation`: float
      - `average_association_rate`: float
    - `hcp`:
      - `average_occupation`: float
      - `average_association_rate`: float
    - `step_110`:
      - `average_occupation`: float
      - `average_association_rate`: float
    - `step_100`:
      - `average_occupation`: float
      - `average_association_rate`: float
    - `edge`:
      - `average_occupation`: float
      - `average_association_rate`: float

### peak_temperatures.json
- path: `/app/outputs/peak_temperatures.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Self‑reported peak temperatures. The checker will cross‑validate them against peaks recomputed from the CSV files.
- schema:
  - `type`: object
  - `required`:
    - `co_peak_T`: float
    - `ni_peak_T`: float

Notes: The agent must implement a standard lattice KMC algorithm with variable‑rate continuous‑time Monte Carlo. All necessary parameters are provided in `/resources/kmc_inputs.json`; use the formulas and physical constants described in this instruction. The checker does not require any npz trajectory files; only the listed scored artifacts are validated.