![](./images/812435664816570370_1.jpg)

# Filling and emptying kinetics of carbon nanotubes in water

Aparna Waghe, Jayendran C. Rasaiah, and Gerhard Hummer

Citation: *The Journal of Chemical Physics* **117**, 10789 (2002); doi: 10.1063/1.1519861

View online: http://dx.doi.org/10.1063/1.1519861

View Table of Contents: http://scitation.aip.org/content/aip/journal/jcp/117/23?ver=pdfcov

Published by the AIP Publishing

---

## Articles you may be interested in

[Capillary filling with giant liquid/solid slip: Dynamics of water uptake by carbon nanotubes](https://aip.scitation.org/doi/10.1063/1.3664622)
J. Chem. Phys. **135**, 214705 (2011); 10.1063/1.3664622

[Kinetics of water filling the hydrophobic channels of narrow carbon nanotubes studied by molecular dynamics simulations](https://aip.scitation.org/doi/10.1063/1.3509396)
J. Chem. Phys. **133**, 204702 (2010); 10.1063/1.3509396

[Effects of size constraint on water filling process in nanotube](https://aip.scitation.org/doi/10.1063/1.2883655)
J. Chem. Phys. **128**, 134703 (2008); 10.1063/1.2883655

[Molecular-dynamics studies of bending mechanical properties of empty and C 60 -filled carbon nanotubes under nanoindentation](https://aip.scitation.org/doi/10.1063/1.1924694)
J. Chem. Phys. **122**, 224713 (2005); 10.1063/1.1924694

[Equilibrium and kinetics: Water confined in carbon nanotubes as one-dimensional lattice gas](https://aip.scitation.org/doi/10.1063/1.1799971)
J. Chem. Phys. **121**, 7996 (2004); 10.1063/1.1799971

---

![](./images/812435664816570370_2.jpg)

This article is copyrighted as indicated in the article. Reuse of AIP content is subject to the terms at: http://scitation.aip.org/termsconditions. Downloaded to IP:
129.137.5.42 On: Fri, 14 Nov 2014 10:25:08

# Filling and emptying kinetics of carbon nanotubes in water
Aparna Waghe and Jayendran C. Rasaiah$^{\rm a)}$
Department of Chemistry, University of Maine, Orono, Maine 04469

Gerhard Hummer$^{\rm b)}$
Laboratory of Chemical Physics, National Institute of Diabetes and Digestive and Kidney Diseases,
National Institutes of Health, Bethesda, Maryland 20892-0520

(Received 9 August 2002; accepted 17 September 2002)

The kinetics of water filling and emptying the interior channel of carbon nanotubes is studied by molecular dynamics simulations. Filling and emptying occur predominantly by sequential addition of water to or removal from a single-file chain inside the nanotube. Advancing and receding water chains are orientationally ordered. This precludes simultaneous filling from both tube ends, and forces chain rupturing to occur at the tube end where a water molecule donates a hydrogen bond to the bulk fluid. We use transition path concepts and a Bayesian approach to identify a transition state ensemble that we characterize by its commitment probability distribution. At the transition state, the tube is filled with all but one water molecule. Filling thermodynamics and kinetics depend sensitively on the strength of the attractive nanotube–water interactions. This sensitivity increases with the length of the tubes. © 2002 American Institute of Physics. [DOI: 10.1063/1.1519861]

## I. INTRODUCTION
The interaction of water with carbon nanotubes$^{1,2}$ has been probed by experiment$^{3-5}$ and simulation.$^{6-12}$ In recent molecular dynamics (MD) simulations,$^{12}$ we observed that water penetrated into the narrow interior channel of a carbon nanotube. A small perturbation of the interactions between water and the nanotube wall had a large effect on the filling behavior. Reducing the well-depth of the carbon–water Lennard-Jones interactions from about 0.11 kcal/mol to 0.065 kcal/mol resulted in a tube that fluctuated between empty and filled states, in which an ordered chain of hydrogen-bonded water molecules spans the nanotube channel. A free energy barrier of about $4\,k_{\rm B}T$ separates the filled from the empty state. The lifetimes of filled and empty states are exponentially distributed, and equilibrium and kinetic free energy differences agree. This two-state like behavior is remarkable, considering the small volume of the nanotube channel, filled by only five water molecules. Transient filling and emptying has been observed similarly in simulations of nonpolar pores in membranes.$^{13}$

Here, we study in detail the mechanism of the emptying and filling transition. In particular, we identify a transition state ensemble for this reaction, and test it by determining its commitment probability distribution.$^{14-16}$ For a tube favoring the empty state, the location of the transition state is close to the fully filled state, which has implications on the length dependence of both the kinetics and equilibrium of filling and emptying. We explore this by comparing simulation results for nanotubes of different length. In a series of nonequilibrium simulations, we show that filling and emptying occur rapidly for both short and long tubes, on subnanosecond time scales, following small perturbations of the carbon–water interactions. This result has implications on the role of nonpolar channels in biological systems, and on using polarity changes to drive filling and emptying transitions in nanotube devices.$^{12,13,17}$

## II. TRANSITION STATE ENSEMBLE
In the MD simulation of the carbon nanotube with modified carbon–water interactions, i.e., reduced attraction$^{12}$ (see Table I), a (6,6) “armchair”-type tube of about $L=13.5$ Å length and 8.1 Å diam (carbon-to-carbon) was surrounded by a bath of about 1000 water molecules. The system was periodically replicated. Electrostatics was treated with particle-mesh Ewald summation,$^{18}$ as implemented in the AMBER 6.0 program (University of California at San Francisco). The simulation of Ref. 12 was extended to a total production time of 42 ns. During that time, we observed a total of 14 filling and 15 emptying transitions. To characterize the mechanism of filling and emptying, we first identify the relevant states sampled during the simulation. We partition the length of the nanotube into five water sites, with each site either empty (0) or occupied (1). From the 42 ns MD simulation, we find that the two most populated states correspond to the tube either empty (00000) or completely filled (11111). The most populated partially filled states have water molecules in a contiguous arrangement [(10000), (11000), etc.], connected with the bulk fluid at only one opening. Fragmented water chains, such as (01100), are rare.

We find in addition that water molecules entering into an initially empty nanotube have a strong preference for having their dipoles oriented inward (hydrogens entering first). Figure 1 shows the normalized water dipole moments projected onto the tube axis as a function of their position along the tube axis. Results are separated for $N=1,2,\dots,5$ water molecules inside the tube. We find that for a single molecule in a tube, the water dipole moments point inward preferen-

$^{\rm a)}$Electronic mail: rasaiah@maine.edu
$^{\rm b)}$Electronic mail: gerhard.hummer@nih.gov

<table>
<caption>TABLE I. Lennard-Jones parameters of the unmodified (Refs. 12, 22) and modified (Ref. 12) carbon–water interactions.</caption>
<thead>
<tr>
<th>
</th>
<th>
$\epsilon_{\text{CO}}$ (kcal/mol)
</th>
<th>
$\sigma_{\text{CO}}$ (Å)
</th>
</tr>
</thead>
<tbody>
<tr>
<td>
unmodified
</td>
<td>
0.114 33
</td>
<td>
3.275 2
</td>
</tr>
<tr>
<td>
modified
</td>
<td>
0.064 61
</td>
<td>
3.413 8
</td>
</tr>
</tbody>
</table>

tially. With subsequent molecules entering into the tube, this orientational preference is maintained, such that the chain grows with all dipoles pointing inward. As a consequence, the dipolar orientations of water chains entering from the two ends simultaneously are not compatible, thus disfavoring simultaneous filling from both sides. Moreover, rupturing of an intact water chain occurs predominantly at the end with the hydrogen bond pointing outward. In addition, the emptying and filling kinetics from the two sides should differ if the tube is oriented in an external electric field.

Put together, these observations imply that (1) filling can be initiated from either side of the tube, and then progresses from the same side, with the possible exception of the last water molecule completing the single-file chain; (2) emptying of a completely filled tube starts from the side with the hydrogen bond pointing outward; and (3) filling/emptying proceed by adding/subtracting water molecules to/from the chain. The number of water molecules in the contiguous chain should thus be a good reaction coordinate for the filling/emptying process.

From the probabilities $p_N$ of the states (00000), (10000) and (00001), (11000), and (00011), etc., with $N=0$, 1, 2, $\dots$, water molecules in a contiguous chain, we obtain a free energy profile, $G_N=-k_BT \ln p_N$, along the presumed reaction coordinate (Fig. 2). This free energy profile is peaked between the states with $N=3$ [(11100) and (00111)] and $N$ $=4$ [(11110) and (01111)] contiguous water molecules at one side and a gap of a single water molecule at the other side of the tube. These states are thus candidates for a transition state ensemble.

![](./images/812435664816570370_3.jpg)

FIG. 1. Normalized dipole of water molecules inside the tube projected onto the tube axis as a function of the position $z$ of the water oxygen atom along the tube axis. Each point corresponds to one water molecule in a saved configuration. The results are separated for $N=1$–5 water molecules inside the tube (top to bottom).

![](./images/812435664816570370_4.jpg)

FIG. 2. Free energies $G_N/k_BT=-\ln p_N$ of states with $N$ contiguous water molecules filling the short tube with modified carbon–water interactions. The probabilities $p_N$ were calculated from a 42-ns equilibrium MD simulation of a nanotube with modified carbon–water interactions in water. Probabilities $p_N$ for symmetric states (e.g., 10000 and 00001) are added together. The cartoon insets indicate the empty state (left), the “transition state” with three molecules completely inside the tube and the fourth one just entering (center), and the filled state with five molecules inside (right).

To explore this hypothesis, we first analyze the equilibrium MD simulation of filling and emptying. $^{12}$ We monitor the filling states visited along the MD trajectory, and determine the probability that a given state subsequently first reaches the completely filled state (11111), or the completely empty state (00000). The probability of reaching the completely filled state first, starting from (11110) or (01111), is found to be 88%. Starting from a state $N=3$, i.e., (11100) and (00111), the probability of reaching the completely filled state first is 33%. This suggests that the transition state ensemble, defined as the configurations with 50% probability to become filled first when propagated with initial velocities from a Maxwell–Boltzmann distribution, is contained within the union of the states with $N=3$ and $N=4$. We thus introduce a continuous coordinate that connects these two states. This coordinate is chosen as the axial position of the water molecule within the tube and closest to the opening. More precisely, we determine the one-dimensional distance $z$ of that water molecule from the center of the nanotube, measured along the nanotube axis.

To select candidate transition states, we use a Bayesian analysis. $^{19}$ Consider a system with a phase or configuration space in which two nonoverlapping regions $A$ and $B$ have been defined. Trajectories for this system occasionally connect the two regions $A$ and $B$. In the framework of transition path sampling, $^{20}$ the segment of such a trajectory connecting the two regions is called a transition path (TP). At equilibrium, points $\mathbf{x}$ in phase or configuration space have a probability density $p_{\text{eq}}(\mathbf{x})$; in the ensemble of transition paths, that probability density is $p(\mathbf{x}|\text{TP})$ which is different from $p_{\text{eq}}(\mathbf{x})$. For a member $\mathbf{x}$ of the transition state ensemble, we expect that the probability of being in a transition path, given

![](./images/812435664816570370_5.jpg)

FIG. 3. Bayesian analysis to determine a transition state ensemble for filling/emptying of the tube with modified carbon-water parameters. Shown is $p(z|\text{TP})/p_{\text{eq}}(z)\equiv p(\text{TP}|z)$, where $z$ is the axial coordinate (measured with respect to the center of the nanotube) of the water molecule closest to the exit in a tube filled with four water molecules.

that the system is in $\mathbf{x}$, assumes a maximum. From the relation between conditional probabilities, we obtain the unnormalized probability of being in a transition path, given that the system is in $\mathbf{x}$,
$$
p(\text{TP}|\mathbf{x})\equiv\frac{p(\mathbf{x}|\text{TP})}{p_{\text{eq}}(\mathbf{x})}.\tag{1}
$$

This expression allows us to estimate a transition state ensemble from an equilibrium simulation, as long as we have sufficiently frequent crossings between $A$ and $B$, by finding the maxima of $p(\text{TP}|\mathbf{x})$ with respect to $\mathbf{x}$. If equilibrium sampling is inadequate, one could combine umbrella sampling (for the denominator) with transition path sampling$^{20}$ (for the numerator). Here, we use 29 crossing events between the empty and filled states to estimate the location of the "transition state" for filling and emptying. We first select all states (11110) and (01111) that are located along a transition path between the empty and filled state, (00000) and (11111). We also construct the ensemble of (11110) and (01111) states from the complete equilibrium trajectory. For both the equilibrium and transition path ensembles, we determine the distributions of positions $z$ of the outermost water molecule, $p_{\text{eq}}(z)$ and $p(z|\text{TP})$, with $4.3< z<6.7$ Å $=L/2$. The ratio of the two distributions, $p(\text{TP}|z)$ in Eq. (1), is shown in Fig. 3. We find a maximum near $z=6$ Å, with $z$ measured from the center of the nanotube of length 13.5 Å. Instead of placing the transition state at exactly that value, we assume in the following that all states with $N=4$ and $z\geqslant6$ Å form a transition state ensemble. We note that any filling or emptying transition necessarily crosses through this transition state ensemble.

Transition states can be defined through commitment probabilities.$^{14-16}$ The transition state ensemble consists of structures that have a 50% probability of reaching the filled state first when starting from that configuration with velocities randomly chosen from a Maxwell-Boltzmann distribution. To test our "transition state ensemble," we randomly picked ten structures from the 42-ns equilibrium trajectory that satisfied the criteria $N=4$ and $z\geqslant6$ Å. For each of those ten structures, we then prepared 50 initial phase points by randomly assigning velocities according to a Maxwell-Boltzmann distribution at 300 K. The resulting 500 phase points were propagated in time by MD until the tube either filled up completely, or emptied completely. For each of the ten structures, the fraction $p$ of times it reached the filled state first was determined. The smallest $p$ was 0.38, the largest 0.62. The mean and variance of the $p$ values were 0.49 and 0.0084, respectively. This is close to the ideal mean of 0.5. The variance is only somewhat larger than expected from a binomial distribution, $p(1-p)/n=0.005$, for $n=50$ repetitions and $p=0.5$. We thus conclude that the simple conformational criteria of filling by $N=4$ water molecules, with the outermost water molecule at least $z=6$ Å away from the center of the tube, leads to a transition state ensemble with a narrow commitment probability distribution centered at 50% (Fig. 4).

![](./images/812435664816570370_6.jpg)

FIG. 4. Distribution of commitment probabilities $p_{\text{fill}}$ for the transition state ensemble. The shaded histogram shows the commitment probability distribution from MD simulations of the tube with modified carbon-water interactions. As a reference, the solid line shows the expected binomial variation for an ideal commitment distribution, with all conformations assumed to have exactly $p_{\text{fill}}=0.5$.

Instead of the combination of number and position of water molecules, we could have used the position $z$ of the water molecule at the tip of the water chain as a single con-

![](./images/812435664816570370_7.jpg)

FIG. 5. Free energy $G(z)$ (solid line; left scale) and conditional probability $p(\text{TP}|z)$ (dashed line; right scale) for the position $z$ of the water molecule at the tip of the water chain (relative to the opening at which the water chain is connected to the bulk fluid). The bottom panel shows the distributions of $z$ for $N=1-5$ water molecules filling the tube.

tinuous reaction coordinate. Here, we prefer the "chemi- cally" more intuitive occupancy number over z. Figure 5 shows the free energy surface and $p(TP|z)$ for the tube with modified carbon-water parameters. We find that $G(z)$ in creases approximately linearly to a barrier of about $3\ k_{B}T$ before dropping sharply into a minimum corresponding to the fully formed chain.

$$
00000\underset{k_{10}}{\stackrel{k_{01}}{\rightleftharpoons}}\left\{\begin{array}{ccccc}
10000 & \underset{k_{21}}{\stackrel{k_{12}}{\rightleftharpoons}} & 11000 & \underset{k_{32}}{\stackrel{k_{23}}{\rightleftharpoons}} & 11100 & \underset{k_{43}}{\stackrel{k_{34}}{\rightleftharpoons}} & 11110 \\
00001 & \underset{k_{21}}{\stackrel{k_{12}}{\rightleftharpoons}} & 00011 & \underset{k_{32}}{\stackrel{k_{23}}{\rightleftharpoons}} & 00111 & \underset{k_{43}}{\stackrel{k_{34}}{\rightleftharpoons}} & 01111
\end{array}\right\}\underset{k_{54}}{\stackrel{k_{45}}{\rightleftharpoons}}11111.
\tag{2}
$$

From the lifetimes of states 00000 to 11111 and the free energy profile shown in Fig. (2) from the 42-ns equilibrium simulation with modified carbon parameters (Table I), we can estimate the rate coefficients in Eq. (2) as listed in Table II. We find that the rate coefficients for adding water mol- ecules are similar $(\sim 0.1\ \text{ps}^{-1})$, and so are the rate coeffi cients for removing water $(\sim 0.2\ \text{ps}^{-1})$, except for the first and last molecules in both cases. This can be explained en- ergetically. The first molecule to enter an empty tube gives up one more hydrogen bond than subsequently entering mol- ecules; a molecule leaving a filled tube results in dangling hydrogen bonds inside the tube. The kinetic scheme Eq. (2) allows us to calculate mean first passage times from the filled to the empty state and vice versa of 190 ps and 1.8 ns, re- spectively. These values compare well with the correspond- ing estimates from 15 emptying and 14 filling transitions in the equilibrium MD simulation, which are $230\pm 70$ ps and $2.4\pm 0.7$ ns, respectively.

For the tube with modified (i.e., unfavorable) carbon- water interactions, the transition state for filling and empty- ing is located very close to the filled state. Even with the tube already filled with all but one water molecule, there remains a $50\%$ chance of it being completely emptied instead of filled. For the modified tube that exhibits emptying and fill- ing in the MD simulations, $^{12}$ the free energy along $N$ in creases close to linearly with the number of molecules be- tween $N=1$ and $N=3$. Thus, adding the second or third water molecule to a pre-existing chain costs roughly the same free energy, which drops significantly only once the chain is completed with the fifth water molecule.

TABLE II. Reciprocals of rate coefficients (in units of ps) in the kinetic scheme Eq. (2), as determined from a 42-ns equilibrium MD simulation by using lifetimes and free energy differences.

<table>
 <thead>
  <tr>
   <th>
   </th>
   <th colspan="5">
    $i$
   </th>
  </tr>
  <tr>
   <th>
   </th>
   <th>
    0
   </th>
   <th>
    1
   </th>
   <th>
    2
   </th>
   <th>
    3
   </th>
   <th>
    4
   </th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td>
    $1/k_{{i,{i + 1}}}$
   </td>
   <td>
    57
   </td>
   <td>
    11
   </td>
   <td>
    17
   </td>
   <td>
    5
   </td>
   <td>
    7.5
   </td>
  </tr>
  <tr>
   <td>
    $1/k_{{i + 1,i}}$
   </td>
   <td>
    3.8
   </td>
   <td>
    4.5
   </td>
   <td>
    9.7
   </td>
   <td>
    5
   </td>
   <td>
    42.6
   </td>
  </tr>
 </tbody>
</table>

### III. KINETICS OF FILLING AND EMPTYING

The number $N$ of water molecules inside the tube pro- vides a reasonable reaction coordinate. We can represent the filling and emptying process in a simple kinetic scheme in which filling occurs sequentially on two alternative path- ways, starting from either end of the tube,

### IV. NANOTUBE LENGTH DEPENDENCE OF FILLING AND EMPTYING

Under conditions where filling is unfavorable, we expect that the filling kinetics slows down as the length increases, while the emptying kinetics should not be affected signifi- cantly. To explore the length dependence, we perform MD simulations at constant pressure (1 bar) and temperature (300 K) for a tube with the modified carbon parameters (Table I) and twice the length. A (6,6)-type tube of about $27\ \mathring{\text{A}}$ length is solvated by 4145 water molecules, resulting in a box size of about $51\ \mathring{\text{A}}$. Details of the simulations are as in Ref. 12. We find that for the long tube, lifetimes of the filled state are indeed comparable to those of the short tube. This is shown in Fig. 6, where we compare the cumulative distributions of the lifetimes of the filled state from equilibrium simulations of the short tube, $^{12}$ and nonequilibrium simulations of both the short and the long tube. In the nonequilibrium simula- tions, the carbon-water potential is switched between the unmodified and modified parameters. With the unmodified parameters favoring the filled state, the simulations are con- tinued until the tube is filled. After the tube has been filled for a few tens of picoseconds, the potential is switched to the modified form that favors the empty state. The simulations are continued until emptying occurs, and after a few tens of picoseconds, the original carbon-water parameters are used again (see Fig. 7). The lifetime is defined as the time from switching parameters to the last filled (modified parameters) or empty state (unmodified parameters) before a transition, and does not include the time of the transition itself. The average lifetimes of the filled state are $230\pm 70$ ps (short tube; 14 lifetimes from equilibrium MD), $190\pm 40$ ps (short tube; 20 lifetimes from nonequilibrium MD); and $240\pm 80$ ps (long tube; 15 lifetimes from nonequilibrium MD), in agree- ment within the combined statistical errors of one estimated standard deviation. We also calculated the mean time of the transitions between the last filled and first completely empty states as $27\pm 4$ ps (15 transitions from equilibrium MD); $28\pm 5$ ps (short tube; 20 transitions from nonequilibrium MD); $91\pm 10$ ps (long tube; 15 transitions from nonequilib-

![](./images/812435664816570370_8.jpg)

FIG. 6. Cumulative distributions of the lifetimes of the filled state for the nanotube with modified carbon-water interactions. Results are shown for equilibrium solid line and nonequilibrium simulations of the short tube long-dashed line, and for nonequilibrium simulations of the long tube short-dashed line. In the nonequilibrium simulations, the carbon-water potential is switched from unmodified to modified parameters Table I at time zero, with the tube filled. The dotted line shows an exponential distribution with a mean time of 0.2 ns.

rium MD. As expected, the transition time i.e., the time to empty the tube after the transition was initiated is significantly longer for the long tube.

## V. SENSITIVITY TO WATER-NANOTUBE INTERACTION PARAMETERS

To explore the remarkable sensitivity of filling with respect to the water-nanotube attractive interactions, we use a carbon-water Lennard-Jones potential $u(r;\lambda)=4\epsilon[(\sigma/r)^{12}-\lambda(\sigma/r)^6]$, tunable by varying a control parameter $\lambda$. This potential is conformal$^{21}$ with another Lennard-Jones potential with new parameters, $\epsilon'=\epsilon\lambda^2$ and $\sigma'=\sigma/\lambda^{1/6}$. The Lennard-Jones parameters of the unmodified $sp^2$ carbon-water interactions$^{22}$ are $\epsilon=0.114\ 333$ kcal/mol and $\sigma=3.275\ 21$ Å. Then, $\lambda=0.752$ corresponds approximately to the modified interactions,$^{12}$ for which the short nanotube was found to fluctuate between empty and filled states. Results of equilibrium simulations of the long nanotube in water are shown in Fig. 8 for different $\lambda$ values, starting from a filled state Table III. An 11-ns equilibrium MD trajectory for $\lambda$

![](./images/812435664816570370_9.jpg)

FIG. 7. Number of water molecules inside the long tube $L\approx27$ Å in nonequilibrium simulations. At times marked by arrows, the carbon-water potential is switched between parameters favoring the filled and empty states, respectively Ref. 12.

![](./images/812435664816570370_10.jpg)

FIG. 8. Number of water molecules inside the long tube $L\approx27$ Å in equilibrium simulations for $\lambda=1$ top, 0.785 middle, and 0.75 bottom scaling the attractive carbon-water van der Waals interactions.

$=0.75$ shows a mostly empty tube that is briefly filled by $N=9$ water molecules, without ever reaching a completely filled state $N=10$. For a slightly more attractive potential with $\lambda=0.785$, emptying and filling occur at equilibrium, with seven emptying and six filling events during a 13-ns MD simulation. For $\lambda=1$ i.e., unmodified carbon-water interactions, the tube remains filled continuously for over 4 ns.

Figure 9 shows the free energy profiles for filling of the long nanotube. Free energies $G_N/k_BT=-\ln P_N$ are shown as a function of $N$ for $\lambda=0.75$ mostly empty tube, $\lambda=0.785$ half-filled/half-empty, and $\lambda=1$ mostly filled, where $P_N$ is the probability of observing exactly $N$ water molecules inside the tube. We find that for $\lambda=0.75$ and 0.785, the free energies depend linearly on $N$ between the empty and filled state $1\leqslant N\leqslant8$, but with different slope. For $\lambda=1$, the tube remains filled and the occupancy fluctuations are small, with $9\leqslant N\leqslant12$. However, the 66-ns simulation for the unmodified short tube also showed a linear dependence of $G_N$ on $N$ Fig. 2a of Ref. 12 for $2\leqslant N\leqslant5$. The slope of $G_N$ versus $N$ depends linearly on $\lambda$, as shown in the inset of Fig. 9, and expected from first-order perturbation theory.

We can now address the mechanism and thermodynamics of filling of long and narrow tubes. In a simplified model, filling occurs from either one or the other end through a contiguous chain of water molecules connected with the bulk fluid, and the free energy is linear with respect to the number $N$ of water molecules inside the tube for $1\leqslant N<M$ where $M$ is the number of water sites inside the filled tube. Only the first and last water molecule to enter have different free en-

<table>
<caption>TABLE III. Lennard-Jones parameters of the $\lambda$-dependent carbon-water interactions.</caption>
<thead>
<tr>
<th>$\lambda$</th>
<th>$\epsilon'_{\text{CO}}$ kcal/mol</th>
<th>$\sigma'_{\text{CO}}$ Å</th>
</tr>
</thead>
<tbody>
<tr>
<td>1.000</td>
<td>0.114 33</td>
<td>3.275 2</td>
</tr>
<tr>
<td>0.785</td>
<td>0.070 45</td>
<td>3.410 1</td>
</tr>
<tr>
<td>0.752</td>
<td>0.064 66</td>
<td>3.434 5</td>
</tr>
<tr>
<td>0.750</td>
<td>0.064 31</td>
<td>3.436 1</td>
</tr>
</tbody>
</table>

![](./images/812435664816570370_11.jpg)

FIG. 9. Free energy profiles for filling of the long nanotube. Free energies $G_N/k_BT=-\ln P_N$ are shown as a function of $N$ for $\lambda=0.75$, 0.785, and 1. $P_N$ is the probability of observing exactly $N$ water molecules inside the tube. The inset shows the slope of the free energy profiles for filling of the long nanotube with respect to $N$ as a function of $\lambda$. For $\lambda=1$, the slope was determined for the short tube [Fig. 2(a) of Ref. 12], consistent with the difference in free energies for $N=9$ and 10 for the long tube.

ergies. The resulting free energy profile of states $N=0$ $(000\cdots0)$, $N=1$ $[(100\cdots0)$ and $(000\cdots01)]$, etc., is given approximately by
$$
G_N\approx
\begin{cases}
0 & \text{for } N=0 \\
\Delta G_0+(N-1)\Delta G & \text{for } 1\leqslant N<M \\
G_{M-1}+\Delta G_1 & \text{for } N=M.
\end{cases}
\tag{3}
$$

A free energy change $\Delta G_0$ is associated with the first water molecule entering into an initially empty tube. Subsequently entering water molecules form hydrogen bonds with those already inside, resulting in a free energy change of $\Delta G$. The last water molecule to enter $(N=M)$ completes the water wire, resulting in a free energy change of $\Delta G_1$. Each of the three parameters, $\Delta G$, $\Delta G_0$, and $\Delta G_1$ will depend on the strength of nanotube-water interactions (measured, e.g., by the parameter $\lambda$) and solvent conditions (such as temperature, pressure, and osmolality). With $\Delta G_0\approx-\Delta G_1$, we find that $G_M\approx(M-2)\Delta G$. The fraction of filled tubes is then given approximately by $1/\{1+\exp[(M-2)\Delta G/k_BT)]\}$. Therefore, if $\Delta G<0$ (as for $\lambda=1$ with $\Delta G\approx-3.6\ k_BT$), long tubes will be mostly filled; if $\Delta G>0$ (as for $\lambda=0.75$ with $\Delta G\approx0.6\ k_BT$), long tubes will be mostly empty even though shorter tubes may be filled. $\Delta G$ is proportional to $\lambda$, as shown in Fig. 9, and $\Delta G\approx0$ for $\lambda=0.758$. For longer tubes $[M\approx L/(2.55\ \text{\AA})]$, the transition between empty and filled tubes becomes increasingly sharp with respect to the parameter $\lambda$ controlling the strength of the attractive water-nanotube interactions (Fig. 10). However, chain fragmentation not considered in the model Eq. (3) also becomes more likely as the tube length increases.

With modified carbon-water parameters $(\lambda=0.752)$ favoring the empty state, we found that the lifetimes of the filled state are approximately the same for long and short tubes. The kinetics of filling, however, differs substantially between the short and long tubes if the empty state is favored. From the above analysis, we expect the lifetime of the empty state to be substantially longer for the long tube with modified carbon parameters because the free energy barrier between the empty and filled states grows linearly with the length of the tube. Indeed, once emptied the long tube does not fill completely within 10 ns of equilibrium simulation [bottom panel in Fig. 8]. This is consistent with the model of the length dependence of filling, with $\Delta G\approx0.6\ k_BT>0$ resulting in a high barrier for filling of the long tube (Fig. 9).

![](./images/812435664816570370_12.jpg)

FIG. 10. Probability of having a tube filled completely as a function of the parameter $\lambda$ tuning the attractive $(r^{-6})$ van der Waals interactions between water and nanotube carbons. Results are shown for the simplified model Eq. (3) with $\Delta G_M\approx(M-2)\Delta G$ and $\Delta G$ linear in $\lambda$ for tubes with $M=5$, 10, and 100 water sites $(L\approx13$, 26, and 260 Å).

The model Eq. (3) suggests that efficient filling and emptying of the long nanotube at equilibrium requires favorable carbon-water interactions. Indeed, by cycling between the modified and unmodified carbon-water interactions (Fig. 7), we find that both the short and the long nanotube with unmodified interactions $(\Delta G\approx-3.6\ k_BT<0)$ fill rapidly with water. The mean lifetimes of the empty state agree within statistical uncertainties: $13\pm4$ ps for the short tube and 13 $\pm4$ ps for the long nanotube. The cumulative distributions of lifetimes of the empty state are shown in Fig. 11. As found before for emptying, the transition times for filling are longer in the long tube: $36\pm5$ ps versus $11.5\pm1$ ps.

These results and the free-energy model, Eq. (3), suggest that the "transition state" for filling and emptying is close to the empty state for tubes that are preferentially filled $(\Delta G$ $<0)$, as with an unmodified interaction, and close to the filled state for tubes that are preferentially empty $(\Delta G$ $>0)$, as with modified interactions.

## VI. CONCLUSIONS

In summary, the filling and emptying transitions of carbon nanotubes in water follow a remarkably simple kinetics. Because of the one-dimensional arrangement of water molecules, filling and emptying occur by sequentially adding (removing) water molecules to (from) a hydrogen-bonded chain. For a preferentially empty tube $(\Delta G>0)$, a transition state ensemble between the empty and completely filled tube could be defined with a simple geometric criterion, with the tube filled by all but one water molecule and the outermost water molecule close to the entrance (Fig. 2). The resulting ensemble of transition states was tested by determining that its commitment distribution was sharply peaked at $p=0.5$

![](./images/812435664816570370_13.jpg)

FIG. 11. Cumulative distributions of the lifetimes of the empty state for the nanotube with unmodified carbon-water interactions. Results are shown for nonequilibrium simulations of the short (solid line) and long tube (long-dashed line). In the nonequilibrium simulations, the carbon-water potential is switched from modified to unmodified parameters at time zero, with the tube empty. The dotted line shows an exponential distribution with a mean time of 15 ps.

(i.e., with velocities drawn randomly from a Maxwell-Boltzmann distribution, each conformation of the ensemble has equal probabilities of $\sim 50\%$ to fill or empty first). The time dependence of filling and emptying follows a simple kinetic scheme, Eq. (2). The rate coefficients for adding water molecules are similar, and so are the rate coefficients for removing water except for the first and last molecules in both cases, corresponding to an almost linear free energy profile between the empty and filled state. This and the location of the transition states close to the filled state for a preferentially empty tube have implications on the length dependence of filling. Under conditions in which adding a water molecule to a preexisting but incomplete chain is unfavorable (i.e., the free energy increases as molecules enter into the tube), we expect the rate of filling to decrease with tube length, while the rate of emptying depends only weakly on length. This is supported by equilibrium and nonequilibrium MD simulations. The thermodynamics and kinetics of filling and emptying, and of the water transport through nanotubes, has also been analyzed by Maibaum and Chandler$^{23}$ using a coarse-grained Ising-type, highlighting the role of density fluctuations.

Normally, single-file dynamics is complicated by the many-body correlations between particles confined to motion along a line. Here, however, those correlations, due to the tight hydrogen-bond interactions, are strong enough to greatly simplify the theoretical description. As in an earlier analysis of the transport of water through nanotubes, $^{24}$ we only need to consider a linear sequence of states, and the dynamics can be described accurately by a kinetic model.

## ACKNOWLEDGMENTS

G.H. thanks Dr. A. Szabo and Dr. A. Berezhkovskii for insightful discussions, and Professor D. Chandler for sending a preprint of Ref. 23 before publication. A.W. and J.C.R. acknowledge support from the National Science Foundation, Grant No. CHE 9961336.

$^{1}$S. Iijima, Nature (London) 354, 56 (1991).
$^{2}$P. M. Ajayan, Chem. Rev. 99, 1787 (1999).
$^{3}$A. Zahab, L. Spina, P. Poncharal, and C. Marlière, Phys. Rev. B 62, 10000 (2000).
$^{4}$Y. Gogotsi, J. A. Libera, A. Guvenc-Yazicioglu, and C. M. Megaridis, Appl. Phys. Lett. 79, 1021 (2001).
$^{5}$C. M. Megaridis, A. G. Yazicioglu, J. A. Libera, and Y. Gogotsi, Phys. Fluids 14, L5 (2002).
$^{6}$K. Koga, G. T. Gao, H. Tanaka, and X. C. Zeng, Nature (London) 412, 802 (2001).
$^{7}$M. C. Gordillo and J. Martí, Chem. Phys. Lett. 329, 341 (2000).
$^{8}$J. Martí and M. C. Gordillo, Phys. Rev. E 64, 021504 (2001).
$^{9}$W. H. Noon, K. D. Ausman, R. E. Smalley, and J. P. Ma, Chem. Phys. Lett. 355, 445 (2002).
$^{10}$J. H. Walther, R. Jaffe, T. Halicioglu, and P. Koumoutsakos, J. Phys. Chem. B 105, 9980 (2001).
$^{11}$T. Werder, J. H. Walther, R. L. Jaffe, T. Halicioglu, F. Noca, and P. Koumoutsakos, Nano Lett. 1, 697 (2001).
$^{12}$G. Hummer, J. C. Rasaiah, and J. P. Noworyta, Nature (London) 414, 188 (2001).
$^{13}$O. Beckstein, P. C. Biggin, and M. S. P. Sansom, J. Phys. Chem. B 105, 12902 (2001).
$^{14}$M. M. Klosek, B. J. Matkowsky, and Z. Schuss, Ber. Bunsenges. Phys. Chem. 95, 331 (1991).
$^{15}$R. Du, V. S. Pande, A. Y. Grosberg, T. Tanaka, and E. S. Shakhnovich, J. Chem. Phys. 108, 334 (1998).
$^{16}$P. G. Bolhuis, C. Dellago, and D. Chandler, Proc. Natl. Acad. Sci. U.S.A. 97, 5877 (2000).
$^{17}$G. Hummer, J. C. Rasaiah, and J. P. Noworyta, in *Technical Proceedings of the Second International Conference on Computational Nanoscience and Nanotechnology*, edited by M. Laudon and B. Romanowicz Computational Publications, Cambridge, 2002, pp. 124–127.
$^{18}$T. Darden, D. York, and L. Pedersen, J. Chem. Phys. 98, 10089 (1993).
$^{19}$G. Hummer unpublished.
$^{20}$C. Dellago, P. G. Bolhuis, F. S. Csajka, and D. Chandler, J. Chem. Phys. 108, 1964 (1998).
$^{21}$S. F. O'Shea, G. S. Dubey, and J. C. Rasaiah, J. Chem. Phys. 107, 237 (1997).
$^{22}$W. D. Cornell, P. Cieplak, C. I. Bayley, I. R. Gould, K. M. Merz, Jr., D. M. Ferguson, D. C. Spellmeyer, T. Fox, J. W. Caldwell, and P. A. Kollman, J. Am. Chem. Soc. 117, 5179 (1995).
$^{23}$L. Maibaum and D. Chandler unpublished.
$^{24}$A. Berezhkovskii and G. Hummer, Phys. Rev. Lett. 89, 064503 (2002).