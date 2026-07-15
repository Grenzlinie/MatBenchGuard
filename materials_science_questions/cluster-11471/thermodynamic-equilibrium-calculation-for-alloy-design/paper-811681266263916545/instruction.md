# Calculate specific interfacial energy between M23C6 and austenite using misfit dislocation model

## Problem background
Austenitic heat-resistant stainless steels are widely used in high-temperature structural applications, such as superheater and reheater tubes in ultra-supercritical boilers. Two alloys—25Cr-20Ni-Nb-N and 22Cr-25Ni-Mo-Nb-N—exhibit different high-temperature tensile strengths after long-term aging at 700°C, and the grain-boundary precipitates, mainly M23C6 carbides, are believed to play a key role in interfacial strength. Because M23C6 grows with a cube-on-cube orientation relationship with the austenite matrix, the specific interfacial energy between the two phases can be estimated from their lattice constants using a misfit dislocation model. The lattice constants of austenite and M23C6 in both alloys have been measured by X-ray diffraction, and the elastic modulus of austenite is known as a function of temperature. The task is to compute the specific interfacial energy for each alloy at room temperature (25°C) and at the service temperature (700°C) to determine whether the energies differ systematically between the two alloys.

## Approach
The calculation uses the misfit dislocation model for a coherent interface. The mismatch between the carbide lattice (aM23C6) and three times the austenite lattice (3 aγ) defines the misfit δ = |aM23C6 − 3 aγ|/aM23C6. The strain energy is carried by interfacial dislocations with Burgers vector b = aγ/√2. A correction factor f(δ) = δ[2/(1+1/(4δ²)) − ln(2δ)] accounts for overlap of dislocation stress fields. The specific interfacial energy is then σ = (Eγ aγ) / (4√2(1−ν²)) × f(δ), where Eγ is the Young's modulus of austenite (Eγ = 254680 − 114.76 T [MPa], with T in Kelvin), ν = 0.29 is Poisson's ratio. At 700°C, the room-temperature lattice constants must be expanded using the linear coefficient of thermal expansion α = 2.21×10⁻⁵ K⁻¹. Compute σ for each alloy at 25°C (298.15 K) and 700°C (973.15 K).

## Reproduction target
Compute the specific interfacial energy σ (in J/m²) between M23C6 and austenite for 25Cr-20Ni-Nb-N and 22Cr-25Ni-Mo-Nb-N at 25°C and 700°C. Save the four results as a CSV file with the columns: alloy, temperature_C, sigma. The values will be compared to a hidden reference to evaluate numerical accuracy and the consistency of the relative trend between the two alloys.

## Assets

- NumPy: numpy

## Workflow steps

### Step 1: Calculate specific interfacial energy
- Role: scored (load-bearing)
- Action: Using the given lattice constants (at room temperature) for 25Cr-20Ni-Nb-N: aγ = 3.59798 Å, aM23C6 = 10.65841 Å, and for 22Cr-25Ni-Mo-Nb-N: aγ = 3.59450 Å, aM23C6 = 10.68570 Å; the elastic modulus formula Eγ = 254680 - 114.76*T (T in Kelvin), Poisson ratio ν = 0.29, linear thermal expansion coefficient α = 2.21e-5 K⁻¹, compute the specific interfacial energy σ between M23C6 and austenite at 25°C (298.15 K) and 700°C (973.15 K) using the misfit dislocation model: misfit δ = |aM23C6 - 3*aγ| / aM23C6; Burgers vector b = aγ/√2; correction factor f(δ) = δ * (2/(1+1/(4δ^2)) - ln(2δ)); σ = (Eγ * aγ) / (4√2*(1-ν^2)) * f(δ). For the 700°C case, adjust the room-temperature lattice constants for thermal expansion first. Output a CSV file with the four results.
- Output file: `/app/outputs/specific_interfacial_energy.csv`
- Format: csv
- Contract: CSV with columns: alloy (string), temperature_C (int), sigma (float). Four rows.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/specific_interfacial_energy.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### specific_interfacial_energy.csv
- path: `/app/outputs/specific_interfacial_energy.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Computed specific interfacial energy σ (J/m²) for each alloy at each temperature. The hidden checker recomputes these values and verifies that σ for 25Cr-20Ni-Nb-N is higher than σ for 22Cr-25Ni-Mo-Nb-N at both temperatures.
- schema:
  - `type`: table
  - `required_columns`: `alloy`, `temperature_C`, `sigma`
  - `units`:
    - `sigma`: J/m^2

Notes: The lattice constants for austenite and M23C6 in both alloys are provided in the instruction as numeric inputs. The calculation does not require any external dataset.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "specific_interfacial_energy.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "alloy",
          "temperature_C",
          "sigma"
        ],
        "units": {
          "sigma": "J/m^2"
        }
      },
      "description": "Computed specific interfacial energy σ (J/m²) for each alloy at each temperature. The hidden checker recomputes these values and verifies that σ for 25Cr-20Ni-Nb-N is higher than σ for 22Cr-25Ni-Mo-Nb-N at both temperatures."
    }
  ],
  "notes": "The lattice constants for austenite and M23C6 in both alloys are provided in the instruction as numeric inputs. The calculation does not require any external dataset."
}
```

## How you are scored
A hidden verifier independently recomputes σ from the given inputs using the same model. It reads your CSV and checks each σ value against its own recomputed reference within an undisclosed tolerance. In addition, it verifies that the relative ordering (which alloy exhibits higher interfacial energy) matches the expected physical picture. Each correctly matched row contributes to a weighted score, and the overall reward is the weighted sum of these checks. Simply hardcoding numbers or guessing will not earn full credit because the tolerance and hidden reference are not revealed in advance.
