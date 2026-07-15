# Vibrational Mode Energy Analysis of Macromolecules Using a Debye-like Model

## Problem background
Phonons — quantized vibrational modes — contribute to the effective forces between macromolecules and to their folding thermodynamics. This task explores a phenomenological model that treats a macromolecule as an isotropic elastic continuum and uses a Debye‑like description of the vibrational density of states. You will compute the zero‑point energy, finite‑temperature internal energy, and Helmholtz free energy for a spherical molecule and for a dimer formed by two such molecules, as well as the zero‑point energy of a one‑dimensional atomic chain. The results illuminate the magnitude and temperature dependence of phonon‑mediated forces and how they depend on molecular size, shape, and vibrational stiffness.

## Approach
A macromolecule containing N atoms is modeled as a uniform elastic sphere. Its volume V is derived from N and a typical interatomic spacing a: V = (4π/3) [ (3N/(4π))^{1/3} − 1/2 ]³ a³. The vibrational density of states (modes per unit frequency) is taken to be

g(ω) = 3V ω² / (2π² v³),

where v is the speed of sound. Finite‑size effects are captured by a lower cutoff ω_L and an upper cutoff ω_U, determined from the molecular volume and the total number of vibrational modes:

ω_L = (π/2) v (4π/(3V))^{1/3},
ω_U = v [ 2π² (3N − 6 + π²/12) / V ]^{1/3}.

Using this density of states, the zero‑point energy is computed as

U_Z = ∫_{ω_L}^{ω_U} (ℏω/2) g(ω) dω.

The temperature‑dependent Debye internal energy U(T) is obtained by integrating

U(T) = 3 ∫_{ω_L}^{ω_U} (V ω²)/(2π² v³) · (ℏω)/(e^{ℏω/k_B T} − 1) dω.

The Helmholtz free energy F(T) follows from

F(T) = −k_B T ln Z,
ln Z = − ∫_{ω_L}^{ω_U} g(ω) { (ℏω)/(2 k_B T) + ln[ 1 − exp(−ℏω/(k_B T)) ] } dω.

You will apply this model to:

- A **monomer sphere** with N = 500, a = 1.5×10⁻¹⁰ m, v = 2500 m/s.
- A **dimer sphere** of the same material but with **twice the volume (2V)** and the same v, to compute the dimerization zero‑point energy difference ΔU_zero = U_zero(dimer) − 2·U_zero(monomer).
- **Temperature sweeps** at T = 0, 100, 200, 300 K: compute U(T) and F(T) for monomer and dimer, then ΔU(T) = U_dimer(T) − 2·U_monomer(T) + ΔU_zero and ΔF(T) = F_dimer(T) − 2·F_monomer(T). Repeat the whole set of temperature‑dependent calculations with a **5% higher speed of sound in the dimer** (v_dimer = 1.05·v = 2625 m/s).
- A **one‑dimensional chain** of the same N = 500 atoms, using the 1D density of states g_1D = 3V/(π a² v), with cutoffs
  ω_L,1D = π v / (N a),
  ω_U,1D = π (3N − 6) v / (3 N a),
  to obtain the zero‑point energy.

All integrations are to be performed numerically (e.g., with scipy.integrate) in electron‑volt (eV) energy units. Use physical constants from scipy.constants (ℏ, k_B). No external datasets are required; the parameters above fully specify the computations.

## Reproduction target
You must produce a single JSON file at `/app/outputs/reproduction_results.json` with exactly the structure shown in the output contract. The file must contain:

- `spherical_monomer`: volume V, cutoffs ω_L, ω_U, and zero‑point energy U_zero.
- `spherical_dimer`: the same quantities for the dimer (volume 2V).
- `dimerization`: the dimerization zero‑point energy difference ΔU_zero, and an array `Delta_U_temperature_dependent` with entries for T = 0, 100, 200, 300 K, each giving U_mono, U_dimer, ΔU, and ΔF for the baseline v.
- `dimerization_5pct_higher_v`: analogous entries for the case where the dimer's speed of sound is 5% higher (v = 2625 m/s).
- `oneD_chain`: cutoffs ω_L, ω_U and zero‑point energy U_zero for the 500‑atom linear chain.

All energies in eV, frequencies in rad/s, volume in m³. Use `scipy.constants` for ℏ, k_B and `scipy.integrate` for the integrals. Your task is to implement the model correctly; the exact numbers will emerge from the computation.

## Assets

- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Compute all phonon force quantities
- Role: scored (load-bearing)
- Action: Implement the Debye-like continuum model for a spherical macromolecule with N=500 atoms, interatomic distance a=1.5e-10 m, and baseline speed of sound v=2500 m/s. Compute molecular volume V, lower and upper cutoff frequencies ω_L, ω_U, and zero-point energy U_Zero for monomer and dimer (dimer volume is twice the monomer volume). Compute the dimerization zero-point energy difference ΔU_Zero. Numerically integrate the Debye internal energy and Helmholtz free energy to obtain U(T) and F(T) for monomer and dimer at temperatures T = 0, 100, 200, 300 K, and compute the temperature-dependent ΔU(T) = U_dimer − 2·U_monomer + ΔU_Zero and ΔF(T) = F_dimer − 2·F_monomer. Repeat the temperature-dependent calculations for the case where the dimer's speed of sound is 5% higher (2625 m/s). Additionally, compute the zero-point energy of a 500-atom linear chain using the 1D density of states given in the model. Write all computed quantities into /app/outputs/reproduction_results.json.
- Output file: `/app/outputs/reproduction_results.json`
- Format: json
- Contract: {
  "spherical_monomer": {
    "omega_L": float,
    "omega_U": float,
    "V": float,
    "U_zero": float
  },
  "spherical_dimer": {
    "omega_L": float,
    "omega_U": float,
    "V": float,
    "U_zero": float
  },
  "dimerization": {
    "Delta_U_zero": float,
    "Delta_U_temperature_dependent": [
      {
        "T": float,
        "U_mono": float,
        "U_dimer": float,
        "Delta_U": float,
        "Delta_F": float
      }
    ]
  },
  "dimerization_5pct_higher_v": {
    "Delta_U_zero": float,
    "Delta_U_temperature_dependent": [
      {
        "T": float,
        "U_mono": float,
        "U_dimer": float,
        "Delta_U": float,
        "Delta_F": float
      }
    ]
  },
  "oneD_chain": {
    "omega_L": float,
    "omega_U": float,
    "U_zero": float
  }
}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/reproduction_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### reproduction_results.json
- path: `/app/outputs/reproduction_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Aggregated results from the continuum phonon model: monomer and dimer cutoffs and zero-point energies, temperature-dependent energy and free energy differences for dimerization (baseline and 5% higher speed of sound), and 1D chain zero-point energy.
- schema:
  - `type`: object
  - `required`: `spherical_monomer`, `spherical_dimer`, `dimerization`, `dimerization_5pct_higher_v`, `oneD_chain`
  - `properties`:
    - `spherical_monomer`:
      - `type`: object
      - `properties`:
        - `omega_L`:
          - `type`: number
        - `omega_U`:
          - `type`: number
        - `V`:
          - `type`: number
        - `U_zero`:
          - `type`: number
    - `spherical_dimer`:
      - `type`: object
      - `properties`:
        - `omega_L`:
          - `type`: number
        - `omega_U`:
          - `type`: number
        - `V`:
          - `type`: number
        - `U_zero`:
          - `type`: number
    - `dimerization`:
      - `type`: object
      - `properties`:
        - `Delta_U_zero`:
          - `type`: number
        - `Delta_U_temperature_dependent`:
          - `type`: array
          - `items`:
            - `type`: object
            - `properties`:
              - `T`:
                - `type`: number
              - `U_mono`:
                - `type`: number
              - `U_dimer`:
                - `type`: number
              - `Delta_U`:
                - `type`: number
              - `Delta_F`:
                - `type`: number
    - `dimerization_5pct_higher_v`:
      - `type`: object
      - `properties`:
        - `Delta_U_zero`:
          - `type`: number
        - `Delta_U_temperature_dependent`:
          - `type`: array
          - `items`:
            - `type`: object
            - `properties`:
              - `T`:
                - `type`: number
              - `U_mono`:
                - `type`: number
              - `U_dimer`:
                - `type`: number
              - `Delta_U`:
                - `type`: number
              - `Delta_F`:
                - `type`: number
    - `oneD_chain`:
      - `type`: object
      - `properties`:
        - `omega_L`:
          - `type`: number
        - `omega_U`:
          - `type`: number
        - `U_zero`:
          - `type`: number

Notes: All output values are computed from the given parameters (N=500, a=1.5e-10 m, v_base=2500 m/s) using the Debye-like continuum model. The hidden checker compares each value to paper-reported references with domain-appropriate tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "reproduction_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "spherical_monomer",
          "spherical_dimer",
          "dimerization",
          "dimerization_5pct_higher_v",
          "oneD_chain"
        ],
        "properties": {
          "spherical_monomer": {
            "type": "object",
            "properties": {
              "omega_L": {
                "type": "number"
              },
              "omega_U": {
                "type": "number"
              },
              "V": {
                "type": "number"
              },
              "U_zero": {
                "type": "number"
              }
            }
          },
          "spherical_dimer": {
            "type": "object",
            "properties": {
              "omega_L": {
                "type": "number"
              },
              "omega_U": {
                "type": "number"
              },
              "V": {
                "type": "number"
              },
              "U_zero": {
                "type": "number"
              }
            }
          },
          "dimerization": {
            "type": "object",
            "properties": {
              "Delta_U_zero": {
                "type": "number"
              },
              "Delta_U_temperature_dependent": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "T": {
                      "type": "number"
                    },
                    "U_mono": {
                      "type": "number"
                    },
                    "U_dimer": {
                      "type": "number"
                    },
                    "Delta_U": {
                      "type": "number"
                    },
                    "Delta_F": {
                      "type": "number"
                    }
                  }
                }
              }
            }
          },
          "dimerization_5pct_higher_v": {
            "type": "object",
            "properties": {
              "Delta_U_zero": {
                "type": "number"
              },
              "Delta_U_temperature_dependent": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "T": {
                      "type": "number"
                    },
                    "U_mono": {
                      "type": "number"
                    },
                    "U_dimer": {
                      "type": "number"
                    },
                    "Delta_U": {
                      "type": "number"
                    },
                    "Delta_F": {
                      "type": "number"
                    }
                  }
                }
              }
            }
          },
          "oneD_chain": {
            "type": "object",
            "properties": {
              "omega_L": {
                "type": "number"
              },
              "omega_U": {
                "type": "number"
              },
              "U_zero": {
                "type": "number"
              }
            }
          }
        }
      },
      "description": "Aggregated results from the continuum phonon model: monomer and dimer cutoffs and zero-point energies, temperature-dependent energy and free energy differences for dimerization (baseline and 5% higher speed of sound), and 1D chain zero-point energy."
    }
  ],
  "notes": "All output values are computed from the given parameters (N=500, a=1.5e-10 m, v_base=2500 m/s) using the Debye-like continuum model. The hidden checker compares each value to paper-reported references with domain-appropriate tolerances."
}
```

## How you are scored
A hidden verifier will read your `reproduction_results.json` and compare each required numeric field to independently computed reference values. The comparison uses tolerances appropriate for the model and its numerical integration. Some fields are checked for relative accuracy, others for absolute deviation, and the temperature‑dependent trends are verified for correct sign and shape. The verifier combines the outcomes of all checks into a final score between 0 and 1, with the primary weight on the spherical monomer/dimer energies and the temperature‑dependent differences. Partial credit is possible. Simply printing known literature values is not sufficient; the verifier performs an independent assessment of your computed results. You do not need to know the reference values — only to implement the model faithfully.
