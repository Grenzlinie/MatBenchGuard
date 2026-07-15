# Monte Carlo yield calculation for amorphous silica

## Problem background
The irradiation of amorphous silica nanoparticles by energetic electrons generates ionizations and electronic excitations. The yields of these events determine how many reducing equivalents become available at the particle surface and are central to understanding interfacial reduction processes. Monte Carlo track structure simulations can compute these yields from first principles using the material's electronic response, without the need for a particle accelerator or wet-lab experiment.

## Approach
The simulation follows a stochastic, collision-by-collision model of electron transport in amorphous silica. The core input is the differential dipole oscillator strength distribution (DDOs) for amorphous silica from Philipp (1966). Energy‑dependent inelastic collision cross sections are derived from this distribution using the methodology of Ashley and Green. The simulation tracks each electron through the material, sampling the distance between collisions from a Poisson distribution with a mean free path determined by the cross section and the material density (2.3 g/cm³). At each inelastic collision the energy transfer ΔE is sampled from the cumulative cross section. The event is classified as an ionization if ΔE exceeds the ionization potential (~9 eV) and as an electronic excitation if ΔE lies between the appearance energy (~7 eV) and the ionization potential. Primary and secondary electrons are followed until they fall below the appearance energy. Many random tracks are simulated to obtain stable average yields, reported as the number of events per 100 eV of deposited energy.

## Reproduction target
Implement a Monte Carlo track structure simulation as described. Use the Philipp (1966) differential dipole oscillator strength distribution for amorphous silica. Compute two quantities: the average ionization yield (events per 100 eV) and the average excitation yield (events per 100 eV) for electron irradiation of pure amorphous silica. Save these results to `/app/outputs/yields.json` as a JSON object with keys `ionization_yield_per_100eV` and `excitation_yield_per_100eV`.

## Assets

- Differential dipole oscillator strength distribution for amorphous silica (Philipp, 1966): https://doi.org/10.1016/0038-1098(66)90067-6

## Workflow steps

### Step 1: Monte Carlo track structure simulation
- Role: scored (load-bearing)
- Action: Implement a Monte Carlo simulation of electron transport in amorphous silica. Use the differential dipole oscillator strength distribution from Philipp (1966) and the Ashley/Green inelastic collision cross-section model. Use density 2.3 g/cm³, appearance energy ~7 eV, ionization potential ~9 eV. Simulate a sufficient number of primary electron tracks (e.g., 10^4) to achieve statistical convergence. For each energy-transfer event, classify as ionization (ΔE > 9 eV) or excitation (7 eV < ΔE ≤ 9 eV). Compute the average ionization yield per 100 eV and excitation yield per 100 eV. Write the yields to /app/outputs/yields.json.
- Output file: `/app/outputs/yields.json`
- Format: json
- Contract: {"ionization_yield_per_100eV": <float>, "excitation_yield_per_100eV": <float>}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/yields.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### yields.json
- path: `/app/outputs/yields.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Monte Carlo computed ionization and excitation yields in amorphous silica, to be compared against reference values with tolerance.
- schema:
  - `type`: object
  - `required`:
    - `ionization_yield_per_100eV`: float, units: per 100 eV
    - `excitation_yield_per_100eV`: float, units: per 100 eV

Notes: Only the Monte Carlo track structure simulation stage is included; the experimental pulse radiolysis and the kinetic simulation of e_aq- / MV+ profiles are omitted, as the scored target is the separable dry-lab MC calculation.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "yields.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "ionization_yield_per_100eV": "float, units: per 100 eV",
          "excitation_yield_per_100eV": "float, units: per 100 eV"
        }
      },
      "description": "Monte Carlo computed ionization and excitation yields in amorphous silica, to be compared against reference values with tolerance."
    }
  ],
  "notes": "Only the Monte Carlo track structure simulation stage is included; the experimental pulse radiolysis and the kinetic simulation of e_aq- / MV+ profiles are omitted, as the scored target is the separable dry-lab MC calculation."
}
```

## How you are scored
A hidden verifier reads `/app/outputs/yields.json` and compares the reported ionization and excitation yields to reference values. The comparison uses a tolerance that accounts for legitimate Monte Carlo statistical spread and implementation differences. The score reflects how close both yields are to the reference; you must submit a valid JSON file containing the two required fields.
