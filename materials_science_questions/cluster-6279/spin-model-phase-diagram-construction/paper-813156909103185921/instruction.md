# Dynamic Phase Diagram of a Cylindrical Ising Nanowire via Effective-Field Theory

## Problem background
Low-dimensional magnetic nanostructures, such as nanowires and nanotubes, exhibit rich phase behavior that is crucial for applications in high-density recording, sensing, and biomedical technologies. Understanding the dynamic response of such systems under time-varying magnetic fields is essential, yet the dynamic phase diagrams of cylindrical Ising nanowires have not been systematically explored. This task addresses that gap by computing the dynamic phase diagram of a cylindrical spin‑1/2 Ising nanowire driven by an oscillating magnetic field. The system comprises a ferromagnetic core and a surface shell, with exchange couplings within and between these components. The interplay of temperature, field amplitude, and coupling ratios leads to a variety of phases and transitions, including paramagnetic, ferromagnetic, antiferromagnetic, and non-magnetic phases as well as mixed states. The goal is to determine the phase boundaries and critical points in the temperature–field plane for a representative set of material parameters.

## Approach
The theoretical framework combines effective‑field theory (EFT) with correlations and Glauber‑type stochastic dynamics, often referred to as dynamic effective‑field theory (DEFT). The nanowire is modeled with four sublattice magnetizations corresponding to two surface and two core sites that are distinguished by their local environment. The EFT differential‑operator technique is employed to express the quasi‑static magnetizations as products of hyperbolic operators acting on a function of the total effective field. By incorporating Glauber single‑spin-flip transition rates, one obtains a coupled set of first‑order ordinary differential equations (ODEs) for the time evolution of the four sublattice magnetizations. The physical behavior is fully determined by the temperature, the amplitude of the sinusoidal driving field, and the dimensionless coupling ratios r = J_Int / J_C and Δ_S, where J_C, J_S, and J_Int are the core, surface, and interface exchange constants. A numerical integration of the ODEs is performed at each point of a (T, h0) grid until a periodic steady state is reached. The resulting time‑averaged magnetizations serve as dynamic order parameters, and the steady‑state symmetry properties classify the phase (paramagnetic, ferromagnetic, antiferromagnetic, non‑magnetic, or a mixed phase). The phase boundaries and their order (second or first) are then identified, yielding the complete dynamic phase diagram.

## Reproduction target
For the specific set of coupling parameters r = 1.0 and Δ_S = 0.0, with energy units fixed by J_C = 1.0, k_B = 1.0, τ = 1.0, and ω = 1.0, implement the DEFT procedure to construct the dynamic phase diagram in the (T, h0) plane. From this diagram, extract two quantities:
- The tricritical point, defined as the point (T_t, h_t) where the second‑order phase boundary changes over to a first‑order boundary.
- The zero‑field critical temperature T_c, i.e., the second‑order transition temperature at h0 = 0.
Report these numbers in the specified JSON files.

## Assets

- Python 3
- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Simulate dynamic phase diagram
- Role: process
- Action: Derive the explicit ODE system for the four sublattice magnetisations by expanding the effective-field theory (EFT) differential-operator expressions for spin‑1/2 with the Glauber dynamics prescription. For the fixed parameter set r=1.0, ΔS=0.0, JC=1.0, kB=1.0, τ=1.0, ω=1.0, construct a grid of temperatures T and field amplitudes h0. For each (T,h0) point, numerically integrate the ODEs until a periodic steady state is reached; classify the resulting magnetisation time series into phases (p, f, af, nm, mixed) using symmetry criteria on the time series; compute time‑averaged magnetisations as dynamic order parameters; and locate the phase boundaries and their order (second‑/first‑order). Store the full phase‑space information in an evidence log to document the pipeline execution.
- Evidence: `/app/outputs/phase_scan.log`

### Step 2: Extract tricritical point
- Role: scored (load-bearing)
- Action: From the completed (T,h) phase diagram, identify the tricritical point where the second‑order phase boundary meets the first‑order line. Write the coordinates (T_t, h_t) as a JSON file.
- Output file: `/app/outputs/tricritical_point.json`
- Format: json
- Contract: JSON object with keys 'T_t' (float) and 'h_t' (float).
- Scoring: scored by hidden verifier

### Step 3: Extract zero‑field critical temperature
- Role: scored (load-bearing)
- Action: From the phase diagram at h=0, determine the second‑order transition temperature T_c between the paramagnetic and the ordered phase. Write the value as a JSON file.
- Output file: `/app/outputs/critical_temperature_h0.json`
- Format: json
- Contract: JSON object with key 'T_c' (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/tricritical_point.json`
- `/app/outputs/critical_temperature_h0.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### tricritical_point.json
- path: `/app/outputs/tricritical_point.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: The dynamic tricritical point coordinates (T_t, h_t) where the phase boundary changes from second-order to first-order.
- schema:
  - `type`: object
  - `required`:
    - `T_t`: float, tricritical temperature (reduced units, JC=1.0, kB=1.0)
    - `h_t`: float, tricritical field amplitude (same reduced units)

### critical_temperature_h0.json
- path: `/app/outputs/critical_temperature_h0.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: The zero‑field second‑order critical temperature T_c separating the paramagnetic phase from the ordered phase.
- schema:
  - `type`: object
  - `required`:
    - `T_c`: float, second-order transition temperature at h=0 (same reduced units)

Notes: Both quantities are fixed deterministic outputs of the simulation for the given Hamiltonian and are scored by absolute‑tolerance comparison against hidden gold values digitised from Fig. 3(a). No directional improvement is defined; exact_match is the appropriate policy.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "tricritical_point.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "T_t": "float, tricritical temperature (reduced units, JC=1.0, kB=1.0)",
          "h_t": "float, tricritical field amplitude (same reduced units)"
        }
      },
      "description": "The dynamic tricritical point coordinates (T_t, h_t) where the phase boundary changes from second-order to first-order."
    },
    {
      "file": "critical_temperature_h0.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "T_c": "float, second-order transition temperature at h=0 (same reduced units)"
        }
      },
      "description": "The zero‑field second‑order critical temperature T_c separating the paramagnetic phase from the ordered phase."
    }
  ],
  "notes": "Both quantities are fixed deterministic outputs of the simulation for the given Hamiltonian and are scored by absolute‑tolerance comparison against hidden gold values digitised from Fig. 3(a). No directional improvement is defined; exact_match is the appropriate policy."
}
```

## How you are scored
Your submission will be evaluated by an automated verifier that inspects the required output files. The verifier compares your reported tricritical point coordinates and the zero‑field critical temperature to hidden reference values derived from the published work, using a tolerance that accounts for legitimate numerical differences between independent implementations. The final reward is a weighted combination of the scores for each quantity: you receive full credit for a quantity if the reported value agrees with the reference within the tolerance, and partial credit proportional to the deviation otherwise, with the total reward ranging from 0 to 1. The verifier does not access any external resources; only the files you write under `/app/outputs` are considered.
