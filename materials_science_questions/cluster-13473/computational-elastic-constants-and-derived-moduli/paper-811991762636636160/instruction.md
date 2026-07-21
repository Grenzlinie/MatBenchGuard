# Phage Capsid Breaking Force Prediction from DNA Hydration Osmotic Pressure Model

## Problem background
Bacteriophages package double-stranded DNA inside protein capsids under high internal pressure due to DNA bending and electrostatic repulsion. Atomic force microscopy (AFM) indentation experiments have measured the spring constant and breaking force of individual phage capsids with different amounts of packaged DNA (empty, partially filled, and wild-type). An analytical thermodynamic model was developed to explain how the internal DNA pressure contributes to the capsid’s resistance to external deformation. The model treats the total force as the sum of the empty-capsid elasticity and an osmotic term from DNA hydration forces, which depends on the DNA density inside the capsid. This task asks you to implement that model and compute the predicted breaking force for a set of genome lengths.

## Approach
The deformation force on a capsid under an AFM tip is modelled as the sum of the force to deform an empty capsid (linear spring with constant $k_{\text{empty}}$) and an additional osmotic force arising from the DNA inside. The osmotic pressure is described by an exponential hydration force law, $\Pi = F_0 \exp(-d/c)$, where $d$ is the interaxial spacing between DNA strands and $F_0$, $c$ are empirical constants. The interaxial spacing depends on the capsid volume and the total contour length of the packaged DNA; as the DNA length increases, the strands are packed more closely, and the osmotic pressure rises. During indentation, the capsid volume decreases slightly, which increases the DNA density and hence the osmotic pressure. For the small indentations at break (around 6.5 nm), the volume change is small, so the osmotic contribution is approximately linear in indentation depth. The total breaking force is evaluated at the average indentation depth at failure. You will compute the predicted breaking force for four conditions: empty capsid (zero osmotic term), and DNA lengths of 37.7 kb, 45.7 kb, and 48.5 kb, using the given capsid parameters.

## Reproduction target
Implement the osmotic indentation model described in Step 1 to compute the predicted capsid breaking force (in nanonewtons) for the four DNA packaging conditions (0%, 78%, 94%, and 100% of wild-type DNA). Write the results to a CSV file with the specified columns and rows. Your implementation will be checked by a hidden verifier that recomputes the predicted forces from the model, verifying correct implementation within a numerical tolerance.

## Assets

- Python and standard scientific libraries

## Workflow steps

### Step 1: Compute predicted capsid breaking forces
- Role: scored
- Action: Implement the analytical osmotic indentation model to compute the predicted breaking force for capsids with different DNA packaging lengths. Use the formulas: interaxial spacing $d = \sqrt{2V/\sqrt{3}} / \sqrt{L_{\text{contour}}}$, osmotic pressure $\Pi = F_0 \exp(-d/c)$, volume change ratio $V_0/V \approx 1 + \frac{3}{16 r_0^2} D^2$, and total force $F(D) = k_{\text{empty}} D + \Pi \cdot \frac{\pi r_0}{2} D$. For the empty capsid (genome length 0), set the osmotic term to zero. Use the given numerical parameters: capsid radius $r_0 = 29.5$ nm, undeformed capsid volume $V_0 = 87114$ nm³, empty capsid spring constant $k_{\text{empty}} = 0.13$ N/m, indentation at break $D = 6.5$ nm, hydration force parameters $F_0 = 1.2 \times 10^4$ pN/nm² and $c = 0.30$ nm, and DNA contour length conversion $0.34$ nm per base pair. Compute for genome lengths of 0, 37.7, 45.7, and 48.5 kb and output the predicted forces in nanonewtons (nN).
- Output file: `/app/outputs/model_predictions.csv`
- Format: csv
- Contract: Columns: `genome_length_percent` (float), `genome_length_kb` (float), `predicted_breaking_force_nN` (float). Four rows corresponding to the four conditions (0% empty, 78% fill, 94% fill, 100% fill).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/model_predictions.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### model_predictions.csv
- path: `/app/outputs/model_predictions.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Predicted capsid breaking force for four DNA packaging conditions (empty, 78%, 94%, 100% WT) computed from the osmotic indentation model.
- schema:
  - `type`: table
  - `required_columns`: `genome_length_percent`, `genome_length_kb`, `predicted_breaking_force_nN`
  - `units`:
    - `genome_length_percent`: percent
    - `genome_length_kb`: kb
    - `predicted_breaking_force_nN`: nN

## Self-check before finishing (optional, not scored)

Before you finish, you may run a quick script to confirm that:
- `/app/outputs/model_predictions.csv` exists
- The CSV contains a header with exactly the columns `genome_length_percent`, `genome_length_kb`, and `predicted_breaking_force_nN`
- The file has four data rows

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness.

## How you are scored
A hidden verifier will recompute the predicted forces from the formulas and parameters given in Step 1. It will read your `model_predictions.csv` and compare your predicted breaking forces to the independently recomputed values within a tolerance. Full credit is awarded if all four predictions match the recomputed values within the tolerance. The single scored artifact, `model_predictions.csv`, carries the entire task weight.