# Predicting resonant trajectories in the PCR3BP with a Conv1d-FC neural network

## Problem background
The planar circular restricted three-body problem (PCR3BP) models the motion of a massless particle under the gravitational influence of the Sun and Neptune, both moving on circular orbits. Particles in the Kuiper belt can be trapped in the 2:3 mean motion resonance with Neptune, characterized by a librating resonant angle σ = 3λ − 2λ_N − ϖ. Understanding their resonant behaviour normally requires lengthy numerical integrations. This work explores whether an artificial neural network (ANN) can learn to predict the future orbital evolution and resonant amplitudes of such particles from a short initial integration, thereby providing a fast method to identify stable resonant objects. The problem is to train an ANN to map the first 25 time points of a 100-point trajectory to the remaining 75 points and to evaluate its ability to recover the resonant amplitude A_σ and the prediction loss for a validation set of particles with eccentricity e=0.1.

## Approach
The procedure combines numerical simulations and supervised learning. First, generate a large set of particle trajectories by numerically integrating the PCR3BP equations of motion in the synodic frame using an eighth‑order Runge–Kutta integrator with a fixed time step over 25 000 yr. Each trajectory is output at 100 equally spaced time points, recording the orbital elements (semimajor axis a, eccentricity e, longitude of perihelion ϖ, mean longitude λ) in the heliocentric inertial frame. Two datasets are created: a training set of 10 000 trajectories with initial resonant angles σ₀ sampled such that the number density is proportional to the square of the resonant amplitude A_σ (Train III distribution), and a validation set of 1000 trajectories with σ₀ spaced uniformly. All particles have e=0.1, semimajor axis at the nominal 2:3 resonance (a=1.31), and longitude of perihelion ϖ=60°.

A feed‑forward ANN is constructed with an input layer, a one‑dimensional convolutional layer (Conv1d) with kernel size 1, two fully connected hidden layers (256 and 300 neurons, ReLU activations), and an output layer. The network receives the first 25 time points (6250 yr) of the orbital elements and must predict the subsequent 75 points (18750 yr). Training minimises the mean absolute error over the four predicted orbital elements using the Adam optimizer. After training, the model is applied to the validation set. For each trajectory, the validation loss ℒ_valid is computed from the predicted vs. true orbital elements, and the resonant angle σ(t) is reconstructed from the predicted ϖ and λ (using Neptune’s known mean longitude). A sinusoidal fit to σ(t) over the full 25 000 yr window yields the resonant amplitude A_σ. The final output is a CSV file containing, for every validation trajectory, its initial resonant angle σ₀, the validation loss, and the predicted A_σ.

## Reproduction target
Produce the validation loss profile and predicted resonant amplitudes for the best‑trained neural network on the e=0.1 case. Specifically: (1) generate the training set (10 000 trajectories, σ₀ distribution ∝ A_σ²) and validation set (1000 trajectories, σ₀ uniformly spaced) by numerical integration of the PCR3BP; (2) implement and train the described Conv1d‑FC network; (3) evaluate on the validation set to obtain per‑trajectory validation loss and predicted A_σ from a sinusoidal fit, and compile the results into a CSV with columns sigma_0 (degrees), validation_loss, predicted_A_sigma (degrees). The goal is to achieve predicted resonant amplitudes below 120° for all stable resonators, consistent with the known stability criterion, and to produce a validation loss curve that captures the resonant behavior across the σ₀ range.

## Assets

- PyTorch: torch
- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Generate training and validation trajectories
- Role: process
- Action: Numerically integrate the PCR3BP equations for 10000 training trajectories and 1000 validation trajectories (e=0.1, initial resonant angles sampled as described) to create the supervised learning dataset. The integration spans 25000 yr with 100 equally‑spaced output points per trajectory, recording orbital elements (a, e, ϖ, λ).
- Evidence: none

### Step 2: Train the Conv1d‑FC neural network
- Role: process
- Action: Construct and train a feed‑forward neural network (Conv1d input layer, two fully‑connected hidden layers, ReLU activations, Adam optimizer) on the generated training trajectories. The network learns to map the first 25 time points to the remaining 75 points of the orbital elements.
- Evidence: `/app/outputs/trained_model.pt`

### Step 3: Evaluate on validation set and compile results
- Role: scored (load-bearing)
- Action: Apply the trained model to each validation trajectory (first 25 points) to predict the remaining 75 points. For each trajectory compute the validation loss (mean absolute error over the four orbital elements) and a sinusoidal fit to the predicted resonant angle to obtain the resonant amplitude A_σ. Assemble a CSV containing the initial resonant angle σ₀, validation loss, and predicted A_σ for all 1000 validation particles.
- Output file: `/app/outputs/best_ann_results.csv`
- Format: csv
- Contract: CSV with columns: sigma_0 (float, degrees), validation_loss (float), predicted_A_sigma (float, degrees). Exactly 1000 rows, one per validation trajectory.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/best_ann_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### best_ann_results.csv
- path: `/app/outputs/best_ann_results.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Per‑trajectory validation loss and predicted resonant amplitude A_sigma for 1000 validation trajectories. The hidden checker compares these values to gold reference values (with tolerances for stochastic training) and also verifies that all predicted_A_sigma are below 120°.
- schema:
  - `type`: table
  - `required_columns`: `sigma_0`, `validation_loss`, `predicted_A_sigma`
  - `units`:
    - `sigma_0`: degrees
    - `predicted_A_sigma`: degrees

Notes: The agent must implement the numerical integration, model construction, training, and evaluation entirely from the method description. No pre‑generated data, pre‑trained model, or external data downloads are provided; the workflow is compute‑heavy but fully public.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "best_ann_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "sigma_0",
          "validation_loss",
          "predicted_A_sigma"
        ],
        "units": {
          "sigma_0": "degrees",
          "predicted_A_sigma": "degrees"
        }
      },
      "description": "Per‑trajectory validation loss and predicted resonant amplitude A_sigma for 1000 validation trajectories. The hidden checker compares these values to gold reference values (with tolerances for stochastic training) and also verifies that all predicted_A_sigma are below 120°."
    }
  ],
  "notes": "The agent must implement the numerical integration, model construction, training, and evaluation entirely from the method description. No pre‑generated data, pre‑trained model, or external data downloads are provided; the workflow is compute‑heavy but fully public."
}
```

## How you are scored
A hidden verifier independently assesses your CSV output from the evaluation step. It compares each trajectory’s validation_loss and predicted_A_sigma against reference values obtained from a correct implementation of the pipeline. Because training is stochastic, the comparison uses tolerances that absorb legitimate run‑to‑run variation. The verifier also checks that all predicted A_σ are less than 120°, as expected for stable 2:3 resonators. The per‑trajectory scores are aggregated into a final reward in the range [0,1]; higher reward is given for smaller discrepancies in validation loss and closer resonant amplitudes, and for satisfying the stability threshold. The verification is performed entirely on your submitted CSV; no further computation is required by the verifier.
