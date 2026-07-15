# Thermochemical Ionization Potential of CF4

## Problem background
The ionization potential of carbon tetrafluoride (CF4) is not well established; early electron‑impact measurements gave a value near 17.8 eV, while vacuum ultraviolet absorption spectroscopy reveals a continuous absorption limit at about 120900 cm⁻¹ (14.99 eV). This limit can be interpreted as the onset of the dissociation CF4 → CF3⁺ + F⁻, suggesting that the true ionization potential is lower and can be estimated through a thermochemical cycle. In this task we compute the ionization potential of CF4 by combining the observed absorption limit with known thermochemical data.

## Approach
The ionization potential (IP) of CF4 can be estimated from a thermochemical cycle that uses the observed continuous absorption limit, interpreted as dissociation into CF3⁺ + F⁻. The cycle proceeds as follows:

1. The experimental limit of continuous absorption (14.99 eV) is attributed to the process:
   CF4 → CF3⁺ + F⁻.
   Adding the electron affinity of fluorine (EA_F) yields the energy for:
   CF4 → CF3⁺ + F + e⁻, plus the term (14.99 + EA_F).

2. The atomization energy of CF4 is known as 14.65 eV + 2·D_F₂, where D_F₂ is the dissociation energy of F₂. It is assumed that breaking a single C–F bond costs one quarter of the total atomization energy.

3. By combining the two processes under the assumption that the bond energy in CF4⁺ is the same as in CF4, one obtains an expression for the ionization potential in terms of the given quantities. The necessary numeric constants are:
   - Dissociation limit: 14.99 eV
   - Atomization energy expression: 14.65 eV + 2·D_F₂
   - The combination (EA_F − D_F₂/2) = 2.88 eV (determined from independent crystal‑energy cycles)
   - Bond energy partition: ¼ of the atomization energy.

The task is to derive the IP from these raw numbers, performing the required arithmetic *without* relying on any pre‑evaluated intermediate constant. The result must be reported as a single floating‑point number.

## Reproduction target
Compute the ionization potential of CF4 (in eV) from the given thermochemical constants. Write the result as a single floating‑point number to the file `/app/outputs/ionization_potential.txt`.

## Assets

- Thermochemical Constants for CF4

## Workflow steps

### Step 1: Compute CF4 Ionization Potential
- Role: scored
- Action: Using the provided constants—dissociation limit of CF4 at 14.99 eV, atomization energy expression 14.65 eV + 2·D_F2, the one‑quarter bond energy assumption, and (EA_F − D_F₂/2) = 2.88 eV—derive the ionization potential (IP) of CF4 via the thermochemical cycle described in the Approach. Do not rely on any pre‑computed intermediate constant; compute the IP directly from the raw numbers. Report the result in electron volts.
- Output file: `/app/outputs/ionization_potential.txt`
- Format: txt
- Contract: A single line with a floating-point number (e.g., 14.21).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/ionization_potential.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### ionization_potential.txt
- path: `/app/outputs/ionization_potential.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: Computed ionization potential of CF4 from the thermochemical cycle.
- schema:
  - `type`: text
  - `description`: A single line containing a floating-point number representing the ionization potential in eV.

Notes: The calculation uses the given constants and the described cycle. The result is deterministic and is compared to the paper's published value within a tolerance on the hidden checker side.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "ionization_potential.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "description": "A single line containing a floating-point number representing the ionization potential in eV."
      },
      "description": "Computed ionization potential of CF4 from the thermochemical cycle."
    }
  ],
  "notes": "The calculation uses the given constants and the described cycle. The result is deterministic and is compared to the paper's published value within a tolerance on the hidden checker side."
}
```

## How you are scored
A hidden verifier reads the number from your `ionization_potential.txt` and compares it to the correct ionization potential (determined from the same thermochemical cycle and the provided constants). Your score is based solely on how close your reported value is to that reference; reporting a value within a predefined tolerance earns full credit, and greater deviations yield lower scores. The verifier does not inspect your calculation method, only the output file.
