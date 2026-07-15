# Thermoelectric Transport Properties of Hybrid Perovskites and Bi2Te3 via DFT and BoltzTraP

## Problem background
Organic–inorganic hybrid perovskite iodides ABI3 (A = CH3NH3 (MA), NH2CHNH2 (FA); B = Sn, Pb) have been widely studied as solar-cell absorbers, but their thermoelectric potential is less explored. Efficient thermoelectric materials require a high figure of merit ZT = (S²σ/κ)T, which depends on the Seebeck coefficient S, electrical conductivity σ, and thermal conductivity κ. This task computationally evaluates the thermoelectric transport properties of these perovskites and compares them with the well‑known thermoelectric material Bi2Te3, which is optimized near room temperature. By computing S, σ, and the electronic thermal conductivity κe as functions of chemical potential μ at 400 K, one can assess whether suitably doped perovskites could approach the performance of Bi2Te3.

## Approach
The workflow uses density functional theory (DFT) with the GGA‑PBE exchange‑correlation functional to obtain the electronic band structures. Geometry optimizations (atomic positions) are performed for the perovskite structures while keeping the experimental lattice parameters fixed. The Kohn‑Sham eigenvalues are then computed on dense k‑meshes for the perovskites and for Bi2Te3. Using these electronic structures, the semi‑classical Boltzmann transport equations are solved with the BoltzTraP2 code under the constant relaxation time approximation. A fixed lattice thermal conductivity is used for all compounds so that the electron‑doped perovskites and hole‑doped Bi2Te3 can be compared on an equal footing. The code outputs the Seebeck coefficient S, electrical conductivity σ, electron thermal conductivity κe, power factor S²σ, and figure of merit ZT as functions of the chemical potential μ.

## Reproduction target
Produce a complete dataset of transport coefficients for (MA)PbI3, (MA)SnI3, (FA)PbI3, (FA)SnI3, and Bi2Te3 as a function of chemical potential μ in the range –1.0 to +1.0 eV (at least 100 points) at 400 K, and write it to transport_properties.json. From this dataset, extract for each compound the chemical potential that maximizes ZT: for perovskites consider only the electron‑doped region (μ > 0); for Bi2Te3 consider only the hole‑doped region (μ < 0). Report the corresponding maximum ZT and carrier concentration (in units of 10¹⁹ cm⁻³) in max_ZT_summary.json.

## Assets

- Quantum ESPRESSO (v7.0 or later): https://www.quantum-espresso.org/
- BoltzTraP2: https://github.com/sousaw/BoltzTraP2
- GGA-PBE pseudopotentials for Pb, Sn, I, Bi, Te (from SSSP efficiency set): https://www.materialscloud.org/discover/sssp/table/efficiency
- Experimental crystal structures of (MA)PbI3, (MA)SnI3, (FA)PbI3, (FA)SnI3 from Stoumpos et al., Inorg. Chem. 2013, 52, 9019-9038: 10.1021/ic401215x
- Bi2Te3 crystal structure (e.g., from Materials Project, mp-3429): https://materialsproject.org/materials/mp-3429

## Workflow steps

### Step 1: Structure Optimization of Perovskites
- Role: process
- Action: Using Quantum ESPRESSO GGA-PBE, add missing hydrogen atoms to the organic cations (MA, FA) and fully relax the atomic positions of (MA)PbI3, (MA)SnI3, (FA)PbI3, (FA)SnI3 while keeping the experimental lattice parameters fixed. The lattice parameters are: (MA)PbI3: a=b=6.3115, c=6.3161 Å, space group P4mm; (MA)SnI3: a=b=6.2302, c=6.2316 Å, P4mm; (FA)PbI3: a=b=8.9817, c=11.006 Å, P3m1; (FA)SnI3: a=6.3286, b=8.9554, c=8.9463 Å, Amm2. Converge forces below 0.005 eV/Å.
- Evidence: `/app/outputs/optimized_structures.json`

### Step 2: DFT Electronic Structure of Perovskites
- Role: process
- Action: From the optimized structures, perform a non-self-consistent field (nscf) GGA-PBE calculation with Quantum ESPRESSO on a dense k-mesh to obtain the Kohn-Sham eigenvalues needed for transport. Use the same pseudopotentials and plane-wave cut-off as in step01.
- Evidence: `/app/outputs/perovskite_eigenvalues.npy`

### Step 3: DFT Electronic Structure of Bi2Te3
- Role: process
- Action: Obtain a Bi2Te3 unit cell from a public database (e.g., hexagonal Bi2Te3, space group R-3m). Relax the structure if needed and compute the Kohn-Sham eigenvalues on a dense k-mesh using the same GGA-PBE parameters as for the perovskites.
- Evidence: `/app/outputs/bi2te3_eigenvalues.npy`

### Step 4: Raw Transport Coefficients Calculation
- Role: scored (load-bearing)
- Action: Using BoltzTraP2 with a constant relaxation time τ = 2×10⁻¹⁴ s and lattice thermal conductivity κL = 1.2 W m⁻¹ K⁻¹, compute the Seebeck coefficient S, electrical conductivity σ, electron thermal conductivity κe, power factor S²σ, and figure of merit ZT as a function of chemical potential μ (range −1.0 to +1.0 eV, at least 100 points) at 400 K for (MA)PbI3, (MA)SnI3, (FA)PbI3, (FA)SnI3, and Bi2Te3. Save the complete dataset to transport_properties.json.
- Output file: `/app/outputs/transport_properties.json`
- Format: json
- Contract: JSON object with a top-level key for each compound: "(MA)PbI3", "(MA)SnI3", "(FA)PbI3", "(FA)SnI3", "Bi2Te3". Each key maps to a list of data points, where each point is an object with fields: mu (chemical potential in eV), S (Seebeck coefficient in μV/K), sigma (electrical conductivity in (Ω·m)⁻¹), kappa_e (electron thermal conductivity in W m⁻¹ K⁻¹), PF (power factor in W m⁻¹ K⁻²), ZT (dimensionless).
- Scoring: scored by hidden verifier

### Step 5: Maximum ZT and Carrier Concentration Summary
- Role: scored
- Action: From the raw transport data, extract for each compound the chemical potential, the maximum ZT, and the corresponding carrier concentration (in units of 10¹⁹ cm⁻³). For perovskites consider only the electron-doped region (μ > 0); for Bi2Te3 consider only the hole-doped region (μ < 0). Write the summary to max_ZT_summary.json.
- Output file: `/app/outputs/max_ZT_summary.json`
- Format: json
- Contract: JSON object with a key for each compound (same as above). Each value is an object with fields: max_ZT (float), carrier_concentration (float, in 10¹⁹ cm⁻³), doping_region (string, either "electron" or "hole").
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/transport_properties.json`
- `/app/outputs/max_ZT_summary.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### transport_properties.json
- path: `/app/outputs/transport_properties.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Complete raw transport coefficients for all five compounds. The checker recomputes ZT from S, sigma, kappa_e and verifies internal consistency before scoring the max ZT summary.
- schema:
  - `type`: object
  - `required`:
    - `(MA)PbI3`: array of data points
    - `(MA)SnI3`: array of data points
    - `(FA)PbI3`: array of data points
    - `(FA)SnI3`: array of data points
    - `Bi2Te3`: array of data points
  - `items`:
    - `mu`: number (eV)
    - `S`: number (μV/K)
    - `sigma`: number ((Ω·m)⁻¹)
    - `kappa_e`: number (W m⁻¹ K⁻¹)
    - `PF`: number (W m⁻¹ K⁻²)
    - `ZT`: number (dimensionless)
  - `required_columns`:
  - `units`:
    - `mu`: eV
    - `S`: μV/K
    - `sigma`: (Ω·m)⁻¹
    - `kappa_e`: W m⁻¹ K⁻¹
    - `PF`: W m⁻¹ K⁻²
    - `ZT`: dimensionless

### max_ZT_summary.json
- path: `/app/outputs/max_ZT_summary.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Extracted maximum ZT and corresponding carrier concentration in the relevant doping region for each compound. Compared against hidden gold values derived from the paper with tolerances.
- schema:
  - `type`: object
  - `required`:
    - `(MA)PbI3`: object with max_ZT, carrier_concentration, doping_region
    - `(MA)SnI3`: object with max_ZT, carrier_concentration, doping_region
    - `(FA)PbI3`: object with max_ZT, carrier_concentration, doping_region
    - `(FA)SnI3`: object with max_ZT, carrier_concentration, doping_region
    - `Bi2Te3`: object with max_ZT, carrier_concentration, doping_region
  - `items`:
    - `max_ZT`: float
    - `carrier_concentration`: float (10¹⁹ cm⁻³)
    - `doping_region`: string ("electron" or "hole")
  - `required_columns`:
  - `units`:
    - `carrier_concentration`: 10¹⁹ cm⁻³

Notes: All values are in SI units unless specified otherwise. The lattice thermal conductivity κL is fixed at 1.2 W m⁻¹ K⁻¹ for all compounds. The relaxation time τ is taken as 2×10⁻¹⁴ s.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "transport_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": {
          "(MA)PbI3": "array of data points",
          "(MA)SnI3": "array of data points",
          "(FA)PbI3": "array of data points",
          "(FA)SnI3": "array of data points",
          "Bi2Te3": "array of data points"
        },
        "items": {
          "mu": "number (eV)",
          "S": "number (μV/K)",
          "sigma": "number ((Ω·m)⁻¹)",
          "kappa_e": "number (W m⁻¹ K⁻¹)",
          "PF": "number (W m⁻¹ K⁻²)",
          "ZT": "number (dimensionless)"
        },
        "required_columns": [],
        "units": {
          "mu": "eV",
          "S": "μV/K",
          "sigma": "(Ω·m)⁻¹",
          "kappa_e": "W m⁻¹ K⁻¹",
          "PF": "W m⁻¹ K⁻²",
          "ZT": "dimensionless"
        }
      },
      "description": "Complete raw transport coefficients for all five compounds. The checker recomputes ZT from S, sigma, kappa_e and verifies internal consistency before scoring the max ZT summary."
    },
    {
      "file": "max_ZT_summary.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "(MA)PbI3": "object with max_ZT, carrier_concentration, doping_region",
          "(MA)SnI3": "object with max_ZT, carrier_concentration, doping_region",
          "(FA)PbI3": "object with max_ZT, carrier_concentration, doping_region",
          "(FA)SnI3": "object with max_ZT, carrier_concentration, doping_region",
          "Bi2Te3": "object with max_ZT, carrier_concentration, doping_region"
        },
        "items": {
          "max_ZT": "float",
          "carrier_concentration": "float (10¹⁹ cm⁻³)",
          "doping_region": "string (\"electron\" or \"hole\")"
        },
        "required_columns": [],
        "units": {
          "carrier_concentration": "10¹⁹ cm⁻³"
        }
      },
      "description": "Extracted maximum ZT and corresponding carrier concentration in the relevant doping region for each compound. Compared against hidden gold values derived from the paper with tolerances."
    }
  ],
  "notes": "All values are in SI units unless specified otherwise. The lattice thermal conductivity κL is fixed at 1.2 W m⁻¹ K⁻¹ for all compounds. The relaxation time τ is taken as 2×10⁻¹⁴ s."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier that independently inspects the output artifacts. First, the verifier recomputes the ZT values from the raw data in transport_properties.json using the same physical constants to check internal consistency. Then it compares the maximum ZT and carrier concentration reported in max_ZT_summary.json against reference values derived from the literature, with appropriate tolerances that account for implementation differences. The final reward is a weighted combination of these checks: raw-data consistency and agreement of the extracted summary values. A submission that runs the complete DFT+BoltzTraP2 pipeline and produces physically reasonable, self‑consistent results will earn the highest reward. Simply reporting numbers without a correct underlying computation will not pass.
