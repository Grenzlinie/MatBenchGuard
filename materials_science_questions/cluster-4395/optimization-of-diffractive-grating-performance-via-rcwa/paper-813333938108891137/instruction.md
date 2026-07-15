# Optimized Two- and Three-Channel Spectral Beam Combining Efficiency via Reflecting Volume Bragg Gratings

## Problem background
Spectral beam combining (SBC) is a technique to scale the output power of high-power fiber lasers by combining multiple laser beams with slightly offset wavelengths into a single near-diffraction-limited beam, using dispersive optical elements such as reflecting volume Bragg gratings (VBGs). This approach helps overcome the thermal and nonlinear limitations that cap the power of single fiber lasers. The combining efficiency depends on the grating's spectral selectivity, the finite spectral width and divergence of the input beams, and unavoidable losses such as absorption and surface reflections. In this task, we numerically investigate the SBC combining efficiency for two-channel and three-channel configurations using optimized reflecting VBGs, accounting for realistic beam divergence (0.6 mrad) and Gaussian spectral profiles. The objective is to compute the overall combining efficiency and the intermediate per-beam diffraction and transmission efficiencies under these conditions.

## Approach
The core computation relies on Kogelnik's coupled-wave theory for an unslanted reflecting volume Bragg grating with sinusoidal refractive index modulation. This theory provides the diffraction efficiency as a function of the wavelength offset Δλ from the Bragg condition. Given a set of fixed grating parameters (average refractive index, thickness, period, index modulation, and centre wavelength), one can generate the spectral selectivity curve (diffraction efficiency versus Δλ) around the Bragg wavelength.

Each laser source's spectral distribution is approximated by a Gaussian profile. The effective efficiency a beam experiences is obtained by convolving the grating's monochromatic selectivity curve with the Gaussian spectrum. For a two‑channel system, one beam is aligned to the Bragg wavelength (λ₁ = 1064 nm) and is predominantly diffracted, while the second beam is at the fourth minimum wavelength (λ₂ = 1063.36 nm) and is primarily transmitted. The total combining efficiency is calculated as the average of the diffraction efficiency of the first beam and the transmission efficiency of the second, reduced by a fixed loss factor ηα that accounts for absorption and reflection losses.

For the three‑channel configuration, two identical gratings are cascaded. The first grating operates identically to the two‑channel case. The second grating, with its Bragg condition centred at 1064.64 nm and an incident angle of 4.4°, combines a third laser beam. The cascaded combining efficiency is computed using a multi‑channel formula that assumes equal input powers and the same loss factor for each grating. All per‑beam diffraction and transmission efficiencies are computed by convolving the appropriate grating selectivity curves with the same Gaussian spectra.

The goal is to implement this numerical model and compute the per‑beam and total efficiencies for two spectral widths (w = 0.1 nm and w = 0.3 nm), with the beam divergence taken into account implicitly through the grating design (the given parameters are already optimized for 0.6 mrad).

## Reproduction target
Produce a structured JSON file named `sbc_efficiencies.json` under `/app/outputs/`. For each of the two spectral widths (0.1 nm and 0.3 nm), report:
- For the two‑channel system: the transmission efficiency η_T at 1063.36 nm, the diffraction efficiency η_D at 1064 nm, and the total combining efficiency η.
- For the three‑channel system: the diffraction efficiency η₁D of VBG1 at 1064 nm, the transmission efficiency η₂T′ of VBG2 at 1064 nm, the transmission efficiency η₁T of VBG1 at 1063.36 nm, the transmission efficiency η₁T′ of VBG2 at 1063.36 nm, the diffraction efficiency η₂D of VBG2 at 1064.64 nm, and the total three-channel combining efficiency η.
 The exact schema is defined in the Output Contract. The calculated efficiencies will be compared against a reference to assess correctness.

## Assets

- numpy: numpy
- scipy: scipy

## Workflow steps

### Step 1: Compute SBC combining efficiencies
- Role: scored (load-bearing)
- Action: Implement the diffraction efficiency formula (Kogelnik’s coupled-wave theory) for an unslanted reflecting volume Bragg grating with sinusoidal refractive index modulation. Compute the spectral selectivity curve (diffraction efficiency versus wavelength offset Δλ) for the optimized grating parameters: average refractive index nav = 1.485, thickness t = 2.5 mm, period Λ = 0.36 μm, refractive index modulation δn = 550 ppm, centre wavelength λ0 = 1064 nm, incident angle ∼5°. Approximate the spectral distribution of each laser by a Gaussian. For spectral widths w = 0.1 nm and w = 0.3 nm, compute by convolution the effective diffraction efficiency ηD at the Bragg wavelength λ1 = 1064 nm and the effective transmission efficiency ηT at the 4th minimum wavelength λ2 = 1063.36 nm. Calculate the two‑channel combining efficiency using η = (ηT·(1−ηα) + ηD)/2 with absorption/reflection losses ηα = 1.5%. For three‑channel SBC, use a second identical grating (centre wavelength 1064.64 nm, incident angle 4.4°). Compute the cascaded combining efficiency via the appropriate multi‑channel formula, assuming equal laser powers and the same loss factor for each grating. Output all per‑beam efficiencies and the total combining efficiencies in a structured JSON file.
- Output file: `/app/outputs/sbc_efficiencies.json`
- Format: json
- Contract: object with top‑level keys "two_channel" and "three_channel". "two_channel" is an array of objects with keys: "w" (float, nm), "eta_T" (float, %), "eta_D" (float, %), "eta" (float, %). "three_channel" is an array of objects with keys: "w" (float, nm), "eta_1D" (float, %), "eta_2T_prime" (float, %), "eta_1T" (float, %), "eta_1T_prime" (float, %), "eta_2D" (float, %), "eta" (float, %). Each array must contain entries for w = 0.1 and w = 0.3.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/sbc_efficiencies.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### sbc_efficiencies.json
- path: `/app/outputs/sbc_efficiencies.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Two‑channel and three‑channel SBC combining efficiencies and their intermediate per‑beam diffraction/transmission efficiencies for spectral widths 0.1 nm and 0.3 nm. The hidden checker compares the reported values against paper‑derived gold thresholds (threshold_or_better).
- schema:
  - `type`: object
  - `required`:
    - `two_channel`: array of objects with fields w (number, nm), eta_T (number, %), eta_D (number, %), eta (number, %)
    - `three_channel`: array of objects with fields w (number, nm), eta_1D (number, %), eta_2T_prime (number, %), eta_1T (number, %), eta_1T_prime (number, %), eta_2D (number, %), eta (number, %)
  - `items`: None
  - `required_columns`: None
  - `units`:
    - `w`: nm
    - `eta_T`: %
    - `eta_D`: %
    - `eta`: %
    - `eta_1D`: %
    - `eta_2T_prime`: %
    - `eta_1T`: %
    - `eta_1T_prime`: %
    - `eta_2D`: %

Notes: The agent must implement the diffraction efficiency model from Kogelnik’s coupled‑wave theory using the given grating parameters. No external dataset is required.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "sbc_efficiencies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": {
          "two_channel": "array of objects with fields w (number, nm), eta_T (number, %), eta_D (number, %), eta (number, %)",
          "three_channel": "array of objects with fields w (number, nm), eta_1D (number, %), eta_2T_prime (number, %), eta_1T (number, %), eta_1T_prime (number, %), eta_2D (number, %), eta (number, %)"
        },
        "items": null,
        "required_columns": null,
        "units": {
          "w": "nm",
          "eta_T": "%",
          "eta_D": "%",
          "eta": "%",
          "eta_1D": "%",
          "eta_2T_prime": "%",
          "eta_1T": "%",
          "eta_1T_prime": "%",
          "eta_2D": "%"
        }
      },
      "description": "Two‑channel and three‑channel SBC combining efficiencies and their intermediate per‑beam diffraction/transmission efficiencies for spectral widths 0.1 nm and 0.3 nm. The hidden checker compares the reported values against paper‑derived gold thresholds (threshold_or_better)."
    }
  ],
  "notes": "The agent must implement the diffraction efficiency model from Kogelnik’s coupled‑wave theory using the given grating parameters. No external dataset is required."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier that reads the files you wrote under `/app/outputs/`. The verifier independently checks the content of each scored output artifact against a hidden reference (gold). For `sbc_efficiencies.json`:
- The reported per‑beam efficiencies and total combining efficiencies are compared to reference values with appropriate tolerances.
- Internal consistency is verified: the verifier may recompute the total combining efficiency from the per‑beam numbers using the provided formulas to ensure the relationship holds.
- The artifact must adhere to the declared format and contain the required fields.

The verifier combines the results of all checks into a single reward score between 0.0 and 1.0. No additional information (e.g., paper identity, expected values, or tolerance thresholds) is provided; you must compute the answer from the problem description and the specified model.
