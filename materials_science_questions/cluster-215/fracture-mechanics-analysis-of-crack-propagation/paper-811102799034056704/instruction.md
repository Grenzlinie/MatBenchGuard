# Temperature-Dependent Fracture Toughness of Brittle Coating on Ductile Substrate under Indentation

## Problem background
This task addresses the temperature‑dependent fracture toughness of a brittle coating deposited on a ductile substrate when subjected to Vickers indentation. The model is based on microcrack formation theory: during unloading, numerous microcracks nucleate from each corner of the indentation impression and coalesce into radial cracks under tensile residual stresses. The fracture toughness of the coating/substrate system is derived by linking the crack‑tip opening displacement (CTOD) to the dislocation movement of atoms, and the temperature effect is incorporated through an Arrhenius‑type rate‑controlling equation. The model requires indentation geometry (load, indentation diagonal, radial crack length, coating thickness) and material properties of the coating and substrate to compute the macroscopic strain energy release rate, the CTOD, the microcrack areal density, and finally the temperature‑dependent fracture toughness \(K_s\). Two indentation‑pressure approaches (basic pressure and composite hardness) are used to estimate the residual stress in the plastic zone, leading to two sets of predictions that can be compared.

## Approach
The temperature-dependent fracture toughness model relies on the following equations and input data. Implement these steps in Python using numpy and scipy (for root-finding if needed).

### Input data

**Indentation mark (the single mark to use for final output):**
- Indentation load \(P = 196\) N
- Diagonal \(2a_c = 616.6\) µm → half-diagonal \(a_c = 308.3\) µm
- Radial crack length \(c = 433.0\) µm
- Coating thickness \(t = 45\) µm

**Indenter geometry:**
- Half-angle of Vickers indenter \(\psi = 68^\circ\) (used in Eq. 25 and 28)

**Material properties (WC-10Co4Cr coating / 1018 steel substrate):**
- Coating Young's modulus \(E_c = 310\) GPa
- Substrate Young's modulus \(E_s = 250\) GPa → \(\Sigma = E_c/E_s = 1.24\)
- Function \(F(\Sigma) = 0.64\) (from the paper’s graph for \(\Sigma = 1.24\))
- Coating Vickers hardness \(H_c = 10.4\) GPa
- Substrate Vickers hardness \(H_s = 1.05\) GPa
- Poisson’s ratio \(\nu = 0.3\) (not directly used in the provided equations but may be needed if implementing \(F(\Sigma)\) integral; use the given \(F(\Sigma)\) value directly)
- Yield stress of coating \(\sigma_c = 210\) MPa → shear yield stress \(\tau_c = \sigma_c/\sqrt{3} = 121\) MPa
- Yield stress of substrate \(Y = 380\) MPa → shear stress \(\tau = Y/\sqrt{3} \approx 220\) MPa
- Tensile strength of coating (used as extreme case stress in Eq. 13): \(\sigma = 223\) MPa
- Volume fraction of brittle δ-WC phase \(V_f = 0.7642\) (from the coating composition: 76.42 vol% WC)
- Burgers vector of δ-WC phase: \(b_b = 0.2906\) nm
- Burgers vector of α-Co phase: \(b_d = 0.2519\) nm
- Composite Burgers vector magnitude (computed via Eq. 29): \(b = 0.2701\) nm (you can compute it yourself to verify, but the value from the paper is 0.2701 nm)
- Boltzmann constant \(k = 1.380649 \times 10^{-23} \, \mathrm{J/K}\) (or use \(8.617333262 \times 10^{-5} \, \mathrm{eV/K}\) if converting units, but the model works with SI units in J; use SI consistently)
- Temperatures to evaluate: \(T \in \{298, 400, 600, 800, 1000\}\) K

### Computational steps

1. **Compute macroscopic strain energy release rate \(G_\varepsilon\) and CTOD \(\delta\)**

   Use the through-thickness cracking model with interface sliding:

   \[
   G_\varepsilon = \frac{\sigma^2 t}{E_c}\left(\frac{\sigma}{3\tau} + \pi F(\Sigma)\right)
   \]

   where \(\sigma = 223\) MPa (tensile strength), \(t = 45\times10^{-6}\) m, \(E_c = 310\times10^9\) Pa, \(\tau = 220\times10^6\) Pa, \(F(\Sigma)=0.64\). Compute \(G_\varepsilon\) in J/m².

   Then obtain CTOD:

   \[
   \delta = \frac{G_\varepsilon}{2 \tau_c}
   \]

   with \(\tau_c = 121\times10^6\) Pa.

2. **Composite Burgers vector \(b\) and scale factor \(m\)**

   The composite Burgers vector magnitude is:

   \[
   b = b_b \left[1 + \frac{2}{\sqrt{\pi}} \sqrt{1-V_f} \left( \left(\frac{b_d}{b_b}\right)^2 - 1 \right) \right]^{1/2}
   \]

   With the values above, \(b = 0.2701\) nm (you may recalculate). Then scale factor:

   \[
   m = \frac{\delta}{b}
   \]

   (ensure consistent units: \(\delta\) in m, \(b\) in m → \(m\) dimensionless).

3. **Microcrack areal density \(\rho_c\)** (for each pressure approach)

   First compute the residual stress \(\sigma_r\) from the indentation pressure. The plastic zone radius factor \(f\) is:

   \[
   f = \frac{h}{a_c} = \sqrt{\frac{E_c}{H_c}} \, (\cos\psi)^{1/3}
   \]

   with \(E_c\) and \(H_c\) in Pa, \(\psi=68^\circ\) (in radians). Then the residual stress for a fully developed plastic zone is:

   \[
   \sigma_r = p \left\{ \frac{3\left[\ln f + \frac{1}{2}\right]}{1+3\ln f} - 1 - \frac{1}{2 f^3} \right\}
   \]

   where the indentation pressure \(p\) is either:
   - **Approach 1 (basic pressure):** \(p = \frac{P}{2 a_c^2}\)
   - **Approach 2 (composite hardness):** \(p = H_m\) with \(H_m\):

     \[
     H_m = 3 \left(\frac{t}{2 a_c}\right) \left(\frac{H_c}{E_c}\right)^{1/2} \left(H_c - H_s\right) (\tan\psi)^{1/3} + H_s
     \]

   (Use \(t=45\times10^{-6}\) m, \(a_c=308.3\times10^{-6}\) m, and the hardness values in Pa. Note that hardness and Young's modulus must be in consistent units.)

   With \(\sigma_r\) known, compute the crack spacing \(D\):

   \[
   D = \frac{2 t \sigma_r}{\tau}
   \]

   (using the substrate shear stress \(\tau\) above). Then the microcrack areal density:

   \[
   \rho_c = \frac{1}{t D}
   \]

   Units: \(\rho_c\) in m⁻².

4. **Determine scale-linking parameter \(n\)** (for each approach separately)

   At room temperature \(T_0 = 298\) K, the temperature-dependent strain energy release rate must equal the macroscopic \(G_\varepsilon\) computed in step 1. The expression for \(G_d\) is:

   \[
   G_d(T) = G_0 \exp\!\left( -\frac{ \frac{G_\varepsilon}{n} \left(\frac{\delta}{m}\right)^2 }{k T} \right)
   \]

   with

   \[
   G_0 = m A \rho_c \frac{k T}{\left(\frac{\delta}{m}\right)^2}
   \]

   where the radial crack area \(A = 2 c t\) (crack length \(c\) times coating thickness, but the paper states \(A = 2 c t\) for a median crack; use that).  
   Set \(G_d(T_0) = G_\varepsilon\) and solve numerically for \(n\) (e.g., using `scipy.optimize.fsolve` or a simple bracketing method). Note that the factor \(\frac{\delta}{m}\) is just \(b\); you may use \(b\) directly. The equation becomes:

   \[
   G_\varepsilon = m A \rho_c \frac{k T_0}{b^2} \exp\!\left( -\frac{G_\varepsilon \, b^2}{n \, k T_0} \right)
   \]

   Solve for \(n\).

5. **Compute temperature-dependent fracture toughness \(K_s\)**

   For each approach (with its own \(n\) computed using that approach’s \(\rho_c\)), evaluate \(G_d(T)\) using the formula for each temperature \(T\) in {298, 400, 600, 800, 1000} K:

   \[
   G_d(T) = G_0(T) \exp\!\left( -\frac{G_\varepsilon \, b^2}{n \, k T} \right)
   \]

   where \(G_0(T) = m A \rho_c \frac{k T}{b^2}\). Then the fracture toughness of the coating/substrate system is:

   \[
   K_s = \sqrt{G_d(T) \, E_c}
   \]

   Convert to MPa·m^{1/2}: \(K_s\) (in Pa·m^{1/2}) divided by \(10^6\) gives MPa·m^{1/2}.

   Collect the results in a dictionary for approach 1 and approach 2.

All computations use the specific indentation mark listed above; do not average over multiple marks.

## Reproduction target
Compute the fracture toughness \(K_s\) of the WC‑10Co4Cr coating on AISI 1018 low‑carbon steel substrate for a specific Vickers indentation mark: load \(P = 196\) N, average diagonal \(2a_c = 616.6\) µm, and radial crack length \(c = 433.0\) µm, with a coating thickness \(t = 45\) µm. Use the material properties (elastic moduli, hardness, Poisson’s ratio, yield stresses, Burgers vectors, etc.) as given in the task description. Perform the computation for both the basic indentation pressure approach (approach 1) and the composite hardness approach (approach 2) at the five temperatures: 298 K, 400 K, 600 K, 800 K, and 1000 K. Write the results to a single structured JSON file with the schema described in the output contract, mapping each temperature (as a string) to the computed \(K_s\) value in MPa·m\(^{1/2}\).

## Assets

- Python numerical computing environment (numpy, scipy): pip install numpy scipy

## Workflow steps

### Step 1: Compute temperature-dependent fracture toughness and write final JSON
- Role: scored (load-bearing)
- Action: Implement the temperature-dependent fracture toughness model for brittle coating/ductile substrate systems under indentation. Compute the macroscopic strain energy release rate, crack tip opening displacement, composite Burgers vector, scale factor, microcrack areal density, and residual plastic stress for the specified indentation mark (load 196 N, half diagonal 308.3 µm, radial crack length 433.0 µm, coating thickness 45 µm) using both the basic indentation pressure approach and the composite hardness approach. Numerically solve for the scale-linking parameter n by equating room-temperature energy release rates. Then compute the fracture toughness K_s at temperatures 298 K, 400 K, 600 K, 800 K, and 1000 K for both approaches. Write the results to fracture_toughness_results.json.
- Output file: `/app/outputs/fracture_toughness_results.json`
- Format: json
- Contract: Top-level JSON object with keys 'approach1' and 'approach2'. Each key maps to an object whose keys are the temperature strings '298','400','600','800','1000' and values are the computed K_s as numeric floats (unit MPa·m^1/2).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/fracture_toughness_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### fracture_toughness_results.json
- path: `/app/outputs/fracture_toughness_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Fracture toughness of WC-10Co4Cr coating/1018 steel substrate at five temperatures computed with basic indentation pressure (approach1) and composite hardness (approach2). Values are in MPa·m^1/2.
- schema:
  - `type`: object
  - `required`:
    - `approach1`: object
    - `approach2`: object
  - `items`:
    - `approach1`:
      - `type`: object
      - `required_keys`: `298`, `400`, `600`, `800`, `1000`
      - `value_type`: number
    - `approach2`:
      - `type`: object
      - `required_keys`: `298`, `400`, `600`, `800`, `1000`
      - `value_type`: number

Notes: K_s values are compared to paper-reported reference values using per-temperature tolerance; monotonic increasing trend with temperature is also verified.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "fracture_toughness_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "approach1": "object",
          "approach2": "object"
        },
        "items": {
          "approach1": {
            "type": "object",
            "required_keys": [
              "298",
              "400",
              "600",
              "800",
              "1000"
            ],
            "value_type": "number"
          },
          "approach2": {
            "type": "object",
            "required_keys": [
              "298",
              "400",
              "600",
              "800",
              "1000"
            ],
            "value_type": "number"
          }
        }
      },
      "description": "Fracture toughness of WC-10Co4Cr coating/1018 steel substrate at five temperatures computed with basic indentation pressure (approach1) and composite hardness (approach2). Values are in MPa·m^1/2."
    }
  ],
  "notes": "K_s values are compared to paper-reported reference values using per-temperature tolerance; monotonic increasing trend with temperature is also verified."
}
```

## How you are scored
Your submitted `fracture_toughness_results.json` will be evaluated by an automated hidden verifier. The verifier compares your reported \(K_s\) values for each approach and temperature to reference values using a tolerance. In addition, it examines the temperature dependence of \(K_s\) for physical consistency. Your final score is a weighted combination of accuracy (how many values fall within the tolerance) and consistency, ranging from 0 to 1. The verifier is independent; simply reporting a number without correctly executing the computational pipeline will not suffice.
