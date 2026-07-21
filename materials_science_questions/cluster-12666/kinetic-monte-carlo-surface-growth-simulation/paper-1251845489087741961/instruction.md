# Vicinal Cellular Automaton Meander-to-Mound Transition

## Problem background
The growth of epitaxial crystal surfaces on miscut (vicinal) substrates can produce either regular step meanders or three-dimensional pyramidal mounds, depending on the competition between the Ehrlich–Schwoebel (ES) step-edge barrier and adatom terrace diffusion. Understanding this morphological transition is important for controlling surface nanostructures. This task uses a Vicinal Cellular Automaton (VicCA) model that decouples terrace diffusion and step incorporation to study the transition. The key quantifiable outputs are the time-scaling exponents of the surface correlation length and the classification of surface morphologies across the parameter space of the ES barrier height and diffusion rate.

## Approach
The VicCA model is a (2+1)D cellular automaton on a square lattice with helical boundary conditions along the y‑direction (across steps) and periodic boundary conditions along the x‑direction (along steps). Adatoms diffuse on terraces according to an energy landscape that includes a potential well at step bottoms and an ES barrier at step tops, with independent diffusion attempts per time step. Crystal growth proceeds via CA attachment rules: kink and void sites are filled unconditionally, while terrace nucleation requires a critical nucleus. After running simulations to a specified time, height‑height correlation functions are computed separately along and across the step direction. The first minimum (wavelength λ) and first maximum (amplitude A) are extracted. For a set of diffusion rates, the time series of λ and A are fitted to scaling laws λ ∼ t^{1/z} and A ∼ t^β to obtain dynamic and growth exponents. For a grid of (diffusion rate, ES barrier) values, the final‑time wavelength and amplitude anisotropy is used to classify the surface morphology as meander, mound, or mixed.

## Model parameters and rules (all energies in units of k_B T)
- **Temperature and energy scale** – The thermal energy k_B T is set to 1 (all energies expressed in units of k_B T).  
- **Diffusion barrier** – The terrace diffusion barrier is \(E_0 = 1\;k_B T\). Consequently, on a flat terrace the probability for a single jump attempt to succeed is  
  \[
  P_0 = e^{-\beta E_0} = e^{-1}\approx 0.3679,
  \]
  where \(\beta = 1/(k_B T)=1\).  
- **Ehrlich–Schwoebel barrier** – At a descending step (an adatom on the upper terrace attempting to hop down to a lower terrace) the jump must overcome an *additional* barrier \(E_{ES}\) (given in k_B T).  The jump probability becomes  
  \[
  P_{\text{down}} = P_0\;e^{-E_{ES}} = e^{-(1+E_{ES})}.
  \]
  Jumps on the same terrace or from a lower to an upper step edge occur with probability \(P_0\).  
- **Diffusion attempts** – Every adatom makes \(n_{DS}\) independent jump attempts per time step. Each attempt chooses one of the four nearest-neighbour sites with equal probability.  
- **CA incorporation rules**  
  - A surface site that has three in‑plane neighbours (a “void” at a step) or two neighbours (a “kink”) is filled unconditionally.  
  - On a straight step, an adatom is incorporated only if at least one other adatom occupies an adjacent site (effective critical nucleus size 2 at the step).  
  - Nucleation on a terrace requires a critical nucleus of size 4 (i.e. an isolated adatom is incorporated only when it has three neighbours that are also adatoms).  
- **Potential well at step bottom** – There is a potential well of depth \(E_V = 1\,k_B T\) located at the bottom of each monoatomic step. For an adatom sitting at a step‑bottom well site, any jump attempt *out of the well* (to a terrace site of higher energy) requires overcoming the additional well depth; its success probability is  
  \[
  P_{\text{well\_out}} = P_0\; e^{-E_V} = e^{-(1+E_V)} = e^{-2}.
  \]
  A jump *into* a well site from a terrace (energy‑lowering) has the standard probability \(P_0 = e^{-1}\). Jumps that do not cross the well boundary (entirely within the same terrace or along the step edge) also occur with probability \(P_0\).  
  **Well-site identification:** A lattice site is considered a well site if it has a neighbouring site in the positive y‑direction (the ascending step direction) whose crystal height is exactly one unit higher. On the vicinal surface this corresponds to the terrace sites immediately below each monoatomic step edge.

## System geometry and simulation protocol
- **Lattice** – Square lattice of size \(N_x = 400\) (along steps, x‑direction) by \(N_y = 300\) (across steps, y‑direction). Periodic boundary conditions in x, helical boundary conditions in y (the height offset between the top and bottom edges is preserved).  
- **Initial surface** – *Flat surface*: all heights zero. *Vicinal surface*: monoatomic steps descending from left to right, with initial terrace width \(l_0 = 10\) lattice units. The vicinal surface is built so that after every 10 rows the height increases by 1.  
- **Adatom concentration** – A constant adatom coverage \(c_0 = 0.01\) is maintained; after each time step the number of adatoms is reset to \(\lfloor c_0\,N_x N_y\rfloor\).  
- **Simulation time** – \(T_{\max} = 10^{6}\) time steps.  

## Output files and their scoring

Write all artifacts under `/app/outputs`:
- `/app/outputs/scaling_exponents.csv`
- `/app/outputs/morphology_diagram_es.csv`

### Detailed workflow

### Step 1: VicCA Simulation and Correlation Function Computation (process, not directly scored)
- Implement the VicCA model following the rules above.  
- **For scaling exponents:** Run the model with \(E_{ES}=3\;k_B T\) for each \(n_{DS}\in\{1,2,5,10,15,20\}\) on both flat and vicinal surfaces. Record the full height map \(h(x,y)\) at time points \(t = 5\times 10^4, \; 1\times 10^5, \; 2\times 10^5, \; 3\times 10^5, \;4\times 10^5, \;5\times 10^5, \;6\times 10^5, \;7\times 10^5, \;8\times 10^5, \;9\times 10^5, \; 1\times 10^6\) (11 snapshots).  
- **For the morphology diagram:** Run simulations on the parameter grid \(n_{DS}\in\{1,2,5,10,15,20\}\) × \(E_{ES}\in\{0.0,\,1.0,\,2.0,\,2.2,\,2.4,\,2.5,\,2.6,\,2.8,\,3.0,\,4.0,\,5.0,\,6.0,\,7.0,\,8.0\}\;k_B T\) with fixed \(c_0=0.01\), \(E_V=1\;k_B T\), initial terrace width \(l_0=10\), system size \(400\times300\), and simulation time \(10^6\) steps. Save only the final height map \(h(x,y)\) at \(t=10^6\).  
- **Height–height correlation functions** – For each saved height map compute the directional correlation functions:
  \[
  C_x(\delta) = \big\langle \left[h(x+\delta,y) - h(x,y)\right]^2 \big\rangle_{x,y},\qquad
  C_y(\delta) = \big\langle \left[h(x,y+\delta) - h(x,y)\right]^2 \big\rangle_{x,y},
  \]
  where the averages run over all valid pairs.  
- **Extract wavelength and amplitude** – Find the first non‑zero minimum of \(C_x(\delta)\) (the location \(\delta\) gives the wavelength \(\lambda_x\)) and the first maximum of \(C_x(\delta)\) (its value is the amplitude \(A_x\)). Do the same for \(C_y(\delta)\) to obtain \(\lambda_y, A_y\).  

### Step 2: Extract Time‑Scaling Exponents (scored)
- Using the time series of \(\lambda_x,\lambda_y\) and \(A_x,A_y\) computed in Step 1 from the \(E_{ES}=3\,k_B T\) simulations, fit a power law over the monotonic growth regime (use the full set of 11 snapshots). Perform a linear least‑squares fit on \(\log(\lambda)\) vs \(\log(t)\) to obtain the dynamic exponent \(1/z\) (slope), and similarly on \(\log(A)\) vs \(\log(t)\) for the growth exponent \(\beta\).  
- Do this separately for the x (across steps) and y (along steps) directions.  
- Write results to `scaling_exponents.csv` with one row per \((n_{DS}, \text{surface\_type})\). For flat surfaces the x and y values are identical; duplicate the exponent values in the corresponding columns.
- **Output file:** `/app/outputs/scaling_exponents.csv`
- **Format:** CSV, columns: `n_DS` (int), `surface_type` (str, `'flat'` or `'vicinal'`), `exponent_1z_x` (float), `exponent_1z_y` (float), `exponent_beta_x` (float), `exponent_beta_y` (float).  
- **Scoring:** compared to hidden reference values with a tolerance of 0.10.

### Step 3: Classify Morphologies and Produce ES Barrier Diagram (scored)
- For each \((n_{DS}, E_{ES})\) combination listed in Step 1, use the final‑time wavelength and amplitude data to classify the surface morphology as **`'meander'`**, **`'mound'`** or **`'mixed'`**.  
  The verifier will check that your diagram satisfies three heuristic constraints:
  1. **Monotonicity** – For a fixed \(n_{DS}\), the sequence of morphology labels with increasing \(E_{ES}\) must be non‑decreasing in the order  
     ```
     'meander' → 'mixed' → 'mound'
     ```
     (i.e. the morphology can only change from meander to mixed to mound; it never goes backward).  
  2. **Endpoints** – At \(E_{ES}=0.0\) the morphology must be `'meander'`; at \(E_{ES}=8.0\) it must be `'mound'`.  
  3. **Consistency with the overall transition trend** – As diffusion rate increases (larger \(n_{DS}\)), the transition from meander to mound moves to higher \(E_{ES}\) values, which is a physically expected trend.  
  Use the computed anisotropy (ratio of wavelengths, ratio of amplitudes, etc.) to decide the label, ensuring the above rules hold. Do not attempt to guess the hidden reference classification; the heuristic verifier will evaluate your diagram using the constraints above and a hidden reference.
- **Output file:** `/app/outputs/morphology_diagram_es.csv`
- **Format:** CSV, columns: `n_DS` (int), `E_ES` (float, k_BT), `morphology` (str, one of `'meander'`,`'mixed'`,`'mound'`).  
- **Scoring:** heuristic verification based on the rules above; exact string comparison against a hidden reference is used internally, but you are only required to meet the stated constraints.

## Output contract (for informational consistency)
The hidden verifier expects the two CSV files exactly as described above.

| output file | columns | purpose | target policy |
|------------|---------|---------|---------------|
| scaling_exponents.csv | n_DS, surface_type, exponent_1z_x, exponent_1z_y, exponent_beta_x, exponent_beta_y | scored | reference\_match (tolerance 0.10) |
| morphology_diagram_es.csv | n_DS, E_ES, morphology | scored | heuristic (see Step 3) |