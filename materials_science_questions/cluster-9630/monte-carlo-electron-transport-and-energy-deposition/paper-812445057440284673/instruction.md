# Monte Carlo electron backscattering spectrum and energy gap in magnetic trapping configuration

## Problem background
The search for a 17 keV neutrino has been complicated by artifacts in beta‑spectrum measurements with silicon detectors. Electrons that backscatter in a magnetic trapping geometry can deposit less energy, leading to an apparent drop in the spectrum that mimics a heavy‑neutrino kink. The physical mechanism is that after a scattering event, the energy deposited in the detector is reduced, and when scattering angles are restricted, this can produce a clear energy gap below the beta endpoint. Understanding the size of this gap and the shape of the scattered spectrum is critical for interpreting heavy‑neutrino searches. This task aims to compute the energy spectrum of electrons that backscatter from one silicon detector and are subsequently detected in a second detector in the same magnetic bottle, and to determine the resulting energy gap.

## Approach
A Monte Carlo simulation is used to model electron transport in the experimental configuration. A 35S beta source with an endpoint of 167 keV is placed at the centre of a 7 T solenoid of length 30 cm and diameter 6.2 cm. Two silicon detectors are at the solenoid ends. The simulation proceeds as follows:
- Sample initial electron energies from the allowed beta spectrum (Fermi function with screening and radiative corrections).
- Propagate each electron along magnetic field lines. Only electrons that can reach one detector (the scatterer) with an incidence angle ≤ the critical angle θc ≈ 60° (set by the ratio of the magnetic field at the detector to that at the centre, sin θc = √(B/B₀)) are considered.
- For these electrons, simulate the scattering process in silicon: energy loss via Bethe–Bloch stopping power and angular redistribution through multiple elastic scattering (or a simplified model that captures the emergence of an energy gap). Track the fraction of energy deposited in the scatterer and the direction of the backscattered electron.
- Propagate the backscattered electron back toward the opposite detector, again subject to the angular acceptance constraint.
- Record the energy deposited in the second detector when the electron reaches it.
- Collect a large number of such backscattering events and histogram the detected energies (binning from 0 to 167 keV).

## Reproduction target
Produce the histogram of detected energies as a CSV file. The histogram should cover the energy range from 0 to 167 keV. The verifier will use this histogram to determine the effective endpoint of the scattered‑electron spectrum: the highest energy bin with a non‑zero count. The difference between the beta endpoint (167 keV) and this effective endpoint is the energy gap. The correctness and accuracy of the simulation will be judged primarily by whether this gap, derived from your histogram, matches a hidden reference value (with a tolerance). Additionally, the spectrum shape should show a clear cutoff (counts dropping to zero above the gap region).

## Assets

- Python scientific computing packages (numpy, scipy, matplotlib): https://pypi.org

## Workflow steps

### Step 1: Monte Carlo simulation of scattered electron spectrum
- Role: scored (load-bearing)
- Action: Implement a Monte Carlo simulation of electron transport from a 35S source (endpoint 167 keV) at the center of a 7 T solenoid (length 30 cm, diameter 6.2 cm) with two silicon detectors at the ends. Sample initial electron energies from the allowed beta spectrum (Fermi function, radiative corrections). Determine which electrons reach the first detector with incidence angle ≤ θc ≈ 60° (critical angle from magnetic field ratio). Simulate backscattering in the silicon detector, including energy loss and angular redistribution, tracking only those backscattered electrons that can reach the opposing detector under similar angular constraints. Record the energy deposited in the second detector for each such event. Bin these energies from 0 to 167 keV and write a histogram CSV.
- Output file: `/app/outputs/simulated_scattered_spectrum.csv`
- Format: csv
- Contract: CSV with header: energy_keV, counts. energy_keV is the bin center in keV (float). counts is the number of events in that bin (integer). Rows cover 0 to 167 keV.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/simulated_scattered_spectrum.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### simulated_scattered_spectrum.csv
- path: `/app/outputs/simulated_scattered_spectrum.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: The energy spectrum of electrons detected after backscattering. The hidden checker reads this file, identifies the effective endpoint (the highest energy bin with counts > 0), computes the energy gap = 167 - effective_endpoint, and compares it to a hidden reference gap with a predefined tolerance. Full credit if the gap lies within the tolerance.
- schema:
  - `type`: table
  - `required_columns`: `energy_keV`, `counts`
  - `units`:
    - `energy_keV`: keV
    - `counts`: dimensionless

Notes: The exact reference gap and tolerance are hidden.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "simulated_scattered_spectrum.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "energy_keV",
          "counts"
        ],
        "units": {
          "energy_keV": "keV",
          "counts": "dimensionless"
        }
      },
      "description": "The energy spectrum of electrons detected after backscattering. The hidden checker reads this file, identifies the effective endpoint (the highest energy bin with counts > 0), computes the energy gap = 167 - effective_endpoint, and compares it to a hidden reference gap with a predefined tolerance. Full credit if the gap lies within the tolerance."
    }
  ],
  "notes": "The exact reference gap and tolerance are hidden."
}
```

## How you are scored
After you submit, a hidden verifier reads your `simulated_scattered_spectrum.csv` and performs the following:
1. It identifies the effective endpoint: the centre of the highest energy bin that has a non‑zero count.
2. It computes the energy gap = 167 keV – effective_endpoint.
3. It compares this gap to a hidden reference gap (derived from the paper’s own simulation) with a predefined tolerance. If the gap lies within the tolerance, the bulk of the reward is awarded.
4. It also performs a structural check: the histogram should have zero counts above the gap region (i.e., there should be a visible energy gap). This carries a smaller weight.
Your final reward is a weighted combination of these two components. There is no need to produce any additional report; the histogram alone provides the needed information. Note that the reference gap and tolerance are hidden, so you must rely on a faithful implementation of the physics and geometry described in the approach.
