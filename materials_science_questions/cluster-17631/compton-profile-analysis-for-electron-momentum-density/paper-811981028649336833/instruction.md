# Monte Carlo Simulation of Geometrical Broadening in Compton Scattering

## Problem background
Compton profile measurements probe the electron momentum distribution in materials by analysing the spectrum of photons scattered inelastically from a sample. However, practical spectrometers use finite apertures and extended photon sources, resulting in a distribution of scattering angles instead of a single well-defined angle. This geometrical broadening distorts the measured Compton profile, spreading it beyond the intrinsic electron momentum contribution. Accurately quantifying this geometrical contribution is essential for correcting experimental data. The broadening depends on the experimental geometry – collimator sizes, source and detector distances, and the nominal scattering angle. A Monte Carlo simulation can model the photon trajectories through the apparatus, account for interactions in the sample, and build a histogram of the scattered photon energies, thereby capturing the geometrical energy spread for a given setup.

## Approach
The geometric response of the spectrometer is obtained by a Monte Carlo simulation of photon transport. The simulation models a flat circular radioactive source (diameter 0.72 cm) emitting 60 keV photons uniformly from its surface, a source collimator (length 3 cm, diameter 0.5 cm), a water sample, and a detector collimator (length 8.5 cm, diameter 0.5 cm). The axis of the source collimator and the axis of the detector collimator intersect at the sample position, forming a nominal angle of 135°. The distances from source to sample and from sample to detector are 7 cm and 12 cm, respectively. Photon trajectories are sampled from the source emission points, and photons that strike the collimator walls are discarded. Photons reaching the water sample penetrate and scatter at a random depth, with depth probability governed by the linear attenuation coefficient for water at 60 keV. The scattering angle is calculated from the incident and scattered directions. A Compton-scattered photon that passes back through the sample and successfully traverses the detector collimator is recorded as a successful event. The energy of each successfully scattered photon is computed from the scattering angle using the Compton formula, and events are accumulated into a histogram with a bin width of approximately 35 eV. After collecting a sufficient number of events, the standard deviation of the scattered photon energy distribution is computed from the histogram. This standard deviation quantifies the geometrical broadening for the chosen geometry.

## Reproduction target
Implement a Monte Carlo simulation for the 135° scattering geometry with the exact dimensions and parameters listed above (source diameter 0.72 cm, source collimator 0.5 cm diameter × 3 cm long, detector collimator 0.5 cm diameter × 8.5 cm long, source-to-sample 7 cm, sample-to-detector 12 cm, incident photon energy 60 keV). Simulate photon emission, collimation, attenuation in water, and detection, recording the scattered photon energy for many successful events. Bin these energies into a histogram with a bin width of approximately 35 eV. From the resulting histogram compute the standard deviation of the energy distribution. Write the computed standard deviation (in eV) together with the histogram counts and bin edges (in eV) to a JSON file named `geometrical_contribution.json` in the `/app/outputs` directory. The file must follow the required output schema.

## Assets

- Linear attenuation coefficient of water at 60 keV: https://physics.nist.gov/PhysRefData/Xcom/html/xcom1.html

## Workflow steps

### Step 1: Run Monte Carlo simulation for 135° geometry
- Role: scored
- Action: Implement a Monte Carlo simulation of Compton scattering using the described experimental geometry: source collimator diameter 0.5 cm, length 3 cm; detector collimator diameter 0.5 cm, length 8.5 cm; source-to-sample 7 cm; sample-to-detector 12 cm; angle between collimator axes 135°; source diameter 0.72 cm; incident photon energy 60 keV. Sample emission points from a flat source, propagate photons through collimators, account for exponential attenuation in the water sample, and determine the scattering angle. Record successful events and bin the scattered photon energy into a histogram with bin width ~35 eV. Compute the standard deviation of the energy distribution. Write the result to /app/outputs/geometrical_contribution.json.
- Output file: `/app/outputs/geometrical_contribution.json`
- Format: json
- Contract: JSON object with keys: "standard_deviation" (float, in eV), "histogram_counts" (list of int), "histogram_bin_edges" (list of float, in eV).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/geometrical_contribution.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### geometrical_contribution.json
- path: `/app/outputs/geometrical_contribution.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Monte Carlo simulation result for 135° geometry: standard deviation of the scattered photon energy distribution (eV), histogram counts (integers), and histogram bin edges (eV).
- schema:
  - `type`: object
  - `required`: `standard_deviation`, `histogram_counts`, `histogram_bin_edges`
  - `properties`:
    - `standard_deviation`:
      - `type`: number
    - `histogram_counts`:
      - `type`: array
      - `items`:
        - `type`: integer
    - `histogram_bin_edges`:
      - `type`: array
      - `items`:
        - `type`: number

Notes: The checker recomputes the standard deviation from the histogram, checks internal consistency, compares to the paper's 340 eV with tolerance, and may perform a shape test on the histogram.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "geometrical_contribution.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": [
          "standard_deviation",
          "histogram_counts",
          "histogram_bin_edges"
        ],
        "properties": {
          "standard_deviation": {
            "type": "number"
          },
          "histogram_counts": {
            "type": "array",
            "items": {
              "type": "integer"
            }
          },
          "histogram_bin_edges": {
            "type": "array",
            "items": {
              "type": "number"
            }
          }
        }
      },
      "description": "Monte Carlo simulation result for 135° geometry: standard deviation of the scattered photon energy distribution (eV), histogram counts (integers), and histogram bin edges (eV)."
    }
  ],
  "notes": "The checker recomputes the standard deviation from the histogram, checks internal consistency, compares to the paper's 340 eV with tolerance, and may perform a shape test on the histogram."
}
```

## How you are scored
A hidden verifier will assess your output automatically. It will read the JSON file and perform the following checks:
1. **Internal consistency**: the verifier recomputes the standard deviation from the histogram counts and bin edges you supply and compares it to your reported `standard_deviation`; a small tolerance (on the order of a few eV) allows for rounding differences.
2. **Accuracy against reference**: the verifier compares your standard deviation against a reference value derived from the original experimental study. A tolerance is applied that accounts for expected variation between independent implementations and finite simulation statistics.
3. **Shape verification**: the verifier checks that the histogram is non-empty, the bin edges are monotonically increasing, and the peak energy (bin with maximum count) falls between 49.8 keV and 50.2 keV.
The final reward is a weighted combination of these checks. You do not need to know the hidden reference value – the verifier handles the comparison. Ensure that your JSON file follows the exact schema described in the output contract.
