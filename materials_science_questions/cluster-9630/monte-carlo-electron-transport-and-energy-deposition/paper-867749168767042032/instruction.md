# Simulating Escaping Reaction-Product Energy from Proton-Irradiated Boron Particles

## Problem background
In proton radiation therapy, introducing boron particles can enhance the local dose through two mechanisms: the nuclear reaction ¹¹B(p,α)²α produces energetic alpha particles, and proton-induced Auger cascades emit low-energy electrons. For both channels, the energy deposited in the surrounding tissue depends on the particle radius because self-absorption within the particle reduces the escaping energy. An optimal particle size exists that balances reaction probability against escape probability. This task involves simulating a spherical boron particle under proton irradiation to compute the total escaping energy of alpha particles and Auger electrons as functions of particle radius, and to determine the radii that maximize each energy product.

## Approach
The simulation proceeds in two independent tracks. For alpha particles, the reaction cross section (¹¹B(p,α)⁸Be) and differential angular distributions are taken from published data (Sikora, 2016) and fitted. SRIM tables provide proton stopping power and alpha projected range in boron. The particle is divided into concentric spherical shells; for each shell, the reaction fraction is computed via an integral of the cross-section-to-stopping-power ratio over the proton energy window that optimizes the reaction rate. Alpha emission is sampled at several angles in the center-of-mass frame, transformed to the lab frame, and each alpha’s energy loss to the particle surface is subtracted. The escaping alpha energy is summed and normalized to a percentage of the maximum value over the radius grid (0.001 to 45 µm). For Auger electrons, the K‑shell ionization cross section for protons on boron is taken from the ECPSSR theory and fitted. All electrons are assumed to originate at 155 eV. Their range in boron is approximated by the Wilson–Dennison mid‑energy formula. Using the same shell integration, the reaction fraction for electron production is computed, and the average escape path length is used to estimate the fraction of electrons that leave the particle with residual energy. The escaping electron energy is summed and normalized to a percentage of the maximum over the radius grid (0.1 to 100 nm). The two output curves (alpha energy product vs. radius and electron energy product vs. radius) are the primary artifacts to be reproduced.

## Reproduction target
Produce two CSV files under `/app/outputs`: (1) `alpha_energy_product.csv` – columns `radius_um` (particle radius in µm) and `alpha_energy_product_percent` (normalized escaping alpha energy, 0–100). The radii should cover from 0.001 µm to 45 µm with sufficient resolution to capture the local maxima of the curve. (2) `electron_energy_product.csv` – columns `radius_nm` (particle radius in nm) and `electron_energy_product_percent` (normalized escaping electron energy, 0–100). The radii should cover from 0.1 nm to 100 nm with sufficient resolution around the peak region. The curves must be smooth and correctly reflect the physics described in the workflow. A hidden verifier will extract the peak radii and compare them to reference values; accurate peak positions and the overall shape of each curve determine the score.

## Assets

- SRIM (Stopping and Range of Ions in Matter): http://www.srim.org/
- Sikora 11B(p,α)8Be cross sections: 10.1007/s10894-016-0069-y
- ECPSSR K‑shell ionization cross sections: 10.1103/PhysRevA.20.465
- Wilson–Dennison electron range approximation: 10.1109/TPS.2011.2176515
- Reference Mathematica implementation: https://github.com/JacobBaxley/PBFT_Particle_Size_Simulation

## Workflow steps

### Step 1: Fit material property functions
- Role: process
- Action: Fit proton stopping power, alpha projected range, total and differential cross sections for the 11B(p,α)8Be reaction, and K‑shell ionization cross sections for protons on boron using data from SRIM, Sikora, and ECPSSR theory. Produce smooth analytic functions suitable for integration and energy‑loss calculations.
- Evidence: `/app/outputs/fits.log`

### Step 2: Alpha energy product curve
- Role: scored (load-bearing)
- Action: Compute the normalized alpha energy product (escaping alpha energy per incident proton) as a function of spherical boron particle radius (0.001–45 µm). Use the fitted cross sections and stopping powers, discretize each particle into 20 concentric cells, evaluate the reaction‑fraction integral, apply angular differential cross‑section weights from 8 emission angles (30°–160°), account for proton and alpha energy loss, and normalize to percentage of the maximum. Output the curve as a CSV file.
- Output file: `/app/outputs/alpha_energy_product.csv`
- Format: csv
- Contract: radius_um: float; alpha_energy_product_percent: float
- Scoring: scored by hidden verifier

### Step 3: Electron energy product curve
- Role: scored
- Action: Compute the normalized electron energy product (escaping Auger electron energy per incident proton) as a function of spherical boron particle radius (0.1–100 nm). Use the fitted K‑shell ionization cross section, proton stopping power, and the Wilson‑Dennison electron range approximation (initial electron energy 155 eV) to estimate the average escape path length and energy loss. Normalize to percentage of the maximum and output as a CSV file.
- Output file: `/app/outputs/electron_energy_product.csv`
- Format: csv
- Contract: radius_nm: float; electron_energy_product_percent: float
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/alpha_energy_product.csv`
- `/app/outputs/electron_energy_product.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### alpha_energy_product.csv
- path: `/app/outputs/alpha_energy_product.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Normalized alpha energy product vs. particle radius. The hidden checker will locate the two main peaks and compare the peak radii to reference values.
- schema:
  - `type`: table
  - `required_columns`: `radius_um`, `alpha_energy_product_percent`
  - `units`:
    - `radius_um`: µm
    - `alpha_energy_product_percent`: %

### electron_energy_product.csv
- path: `/app/outputs/electron_energy_product.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Normalized electron energy product vs. particle radius. The hidden checker will locate the maximum peak and compare its radius to a reference value.
- schema:
  - `type`: table
  - `required_columns`: `radius_nm`, `electron_energy_product_percent`
  - `units`:
    - `radius_nm`: nm
    - `electron_energy_product_percent`: %

Notes: The checker recomputes the peak radii from these curves and compares them to hidden gold values with tolerances appropriate for numerical implementation differences.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "alpha_energy_product.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "radius_um",
          "alpha_energy_product_percent"
        ],
        "units": {
          "radius_um": "µm",
          "alpha_energy_product_percent": "%"
        }
      },
      "description": "Normalized alpha energy product vs. particle radius. The hidden checker will locate the two main peaks and compare the peak radii to reference values."
    },
    {
      "file": "electron_energy_product.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "radius_nm",
          "electron_energy_product_percent"
        ],
        "units": {
          "radius_nm": "nm",
          "electron_energy_product_percent": "%"
        }
      },
      "description": "Normalized electron energy product vs. particle radius. The hidden checker will locate the maximum peak and compare its radius to a reference value."
    }
  ],
  "notes": "The checker recomputes the peak radii from these curves and compares them to hidden gold values with tolerances appropriate for numerical implementation differences."
}
```

## How you are scored
The final reward is a weighted combination of scores from the two scored artifacts. The alpha energy product curve carries a higher weight (approximately 0.6). The verifier reads `alpha_energy_product.csv`, locates the two dominant local maxima, and compares their radii to hidden reference values using a tolerance that accounts for expected numerical implementation differences. Additional low‑weight checks may assess curve smoothness and monotonic segments. The electron energy product curve carries the remaining weight (approximately 0.4). The verifier reads `electron_energy_product.csv`, locates the global maximum, and compares its radius to a hidden reference value with a suitable tolerance. Additional low‑weight structural checks may be applied. Reporting numeric values without producing the correct curves does not satisfy the task; the verifier independently recomputes the peak positions from the submitted CSV files.
