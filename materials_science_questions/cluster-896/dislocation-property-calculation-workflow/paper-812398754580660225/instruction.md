# Dislocation Network Line Length Calculation for (111) f.c.c. Interface

## Problem background
Interfaces between f.c.c. and b.c.c. crystals are often described by dislocation arrays. Bollmann's O-lattice theory predicts the structure of these interfaces by analyzing the transformation relating the two crystal lattices. For a given orientation relationship and lattice parameter ratio, the theory yields candidate habit planes and the geometry (spacings, directions, Burgers vectors) of the interfacial dislocations. For the (111) f.c.c. habit plane close to the Nishiyama-Wasserman orientation relationship, a two-dislocation description can be replaced by a three-dislocation network. This task investigates whether the network reduces the total dislocation line length per unit area compared to the simpler two-dislocation description, by re-implementing the O-lattice calculation and performing the network minimization described in the literature. The specific system is a Cu/Cr interface with known lattice parameters and the Nishiyama-Wasserman orientation. The quantity of interest is the dislocation line length per unit area for both descriptions, together with the geometric parameters that define the interface.

## Approach
The approach follows the O-lattice method for f.c.c./b.c.c. interfaces. The computation proceeds in two main stages.

First, set up the transformation matrix A using the f.c.c. and b.c.c. lattice parameters (a_fcc = 0.36249 nm, a_bcc = 0.2878 nm) and the Nishiyama-Wasserman orientation relationship (close-packed planes parallel, [0-11]_fcc parallel to [00-1]_bcc). Using the six Burgers vectors of type 1/2<110> in the f.c.c. lattice, compute the corresponding O-lattice vectors X_i^0 from the relation X_i^0 = T^{-1} b_i, where T = I - A^{-1}.

Next, identify the pair of O-lattice vectors (X_i^0, X_j^0) whose Burgers vectors satisfy b_i + b_j = b_k for some k and that together define the (111) habit plane. From this pair, compute the dislocation spacings d1, d2, the angle theta' between the dislocation line directions, and the total dislocation line length per unit area for the two-dislocation description. Then, using the geometric construction for a three-dislocation network (where a node connects dislocations of the three Burgers vectors), determine the node coordinates (x, y) that minimize the total length of the three dislocation segments meeting at the node. Compute the resulting network line length per unit area. Report all computed quantities in the specified output file.

## Reproduction target
Produce a JSON file, results.json, containing the following computed quantities for the Cu/Cr interface with the lattice parameters and orientation relationship specified above, evaluated on the (111) f.c.c. habit plane:
- two_dislocation_line_length (nm^-1): total dislocation line length per unit area for the two-dislocation description.
- network_line_length (nm^-1): total line length per unit area for the three-dislocation network.
- theta_prime (degrees): angle between the dislocation line directions.
- d1 (nm) and d2 (nm): spacings of the two dislocation arrays.
- node_coordinates: optimal (x, y) coordinates of the network node, in nm.

## Assets

- numpy: https://pypi.org/project/numpy/

## Workflow steps

### Step 1: Compute O-lattice vectors
- Role: process
- Action: Set up transformation matrices using the given f.c.c. and b.c.c. lattice parameters (a_fcc=0.36249 nm, a_bcc=0.2878 nm) and the Nishiyama-Wasserman orientation relationship. Compute the O-lattice vectors X_i^0 for all six 1/2<110> f.c.c. Burgers vectors using the relation X_i^0 = T^{-1} b_i.
- Evidence: `/app/outputs/o_lattice_vectors.json`

### Step 2: Determine (111) habit plane and dislocation network parameters
- Role: scored (load-bearing)
- Action: From the O-lattice vectors, identify the pair of Burgers vectors (b_i, b_j) that define the (111) f.c.c. habit plane and satisfy b_i + b_j = b_k for some k. Compute the dislocation spacings d1, d2, the angle theta' between dislocation line directions, and the line length per unit area for the two-dislocation description. Determine the node coordinates (x,y) that minimize the total segment lengths for the three-dislocation network using the geometry from Appendix I. Compute the network line length per unit area. Report all quantities.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: {"two_dislocation_line_length": "float (nm^-1)", "network_line_length": "float (nm^-1)", "theta_prime": "float (degrees)", "d1": "float (nm)", "d2": "float (nm)", "node_coordinates": "[float x (nm), float y (nm)]"}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results.json
- path: `/app/outputs/results.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Dislocation line length per unit area for two-dislocation description and three-dislocation network, plus geometric parameters. The hidden checker compares these values to the paper's reported results with an absolute tolerance and verifies theta_prime > 60°.
- schema:
  - `type`: object
  - `required`:
    - `two_dislocation_line_length`: float (nm^-1)
    - `network_line_length`: float (nm^-1)
    - `theta_prime`: float (degrees)
    - `d1`: float (nm)
    - `d2`: float (nm)
    - `node_coordinates`: [float, float] (nm)
  - `units`:
    - `two_dislocation_line_length`: nm^-1
    - `network_line_length`: nm^-1
    - `theta_prime`: degrees
    - `d1`: nm
    - `d2`: nm
    - `node_coordinates`: nm

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "two_dislocation_line_length": "float (nm^-1)",
          "network_line_length": "float (nm^-1)",
          "theta_prime": "float (degrees)",
          "d1": "float (nm)",
          "d2": "float (nm)",
          "node_coordinates": "[float, float] (nm)"
        },
        "units": {
          "two_dislocation_line_length": "nm^-1",
          "network_line_length": "nm^-1",
          "theta_prime": "degrees",
          "d1": "nm",
          "d2": "nm",
          "node_coordinates": "nm"
        }
      },
      "description": "Dislocation line length per unit area for two-dislocation description and three-dislocation network, plus geometric parameters. The hidden checker compares these values to the paper's reported results with an absolute tolerance and verifies theta_prime > 60°."
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden verifier reads your submitted results.json. It checks that theta_prime exceeds 60 degrees (a geometric requirement for a favorable network) and that d1, d2, and node_coordinates are positive and numerically consistent. The verifier then compares your computed two_dislocation_line_length and network_line_length to the paper's reported reference values using an appropriate hidden tolerance. The reward is assigned based on how closely your computed results match the expected values. Simply reporting the expected numbers without performing the computation will not satisfy the verifier because the tolerance is tight enough to require an accurate implementation of the method.
