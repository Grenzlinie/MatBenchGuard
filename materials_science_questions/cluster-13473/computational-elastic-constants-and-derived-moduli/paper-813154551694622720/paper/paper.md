**THEORY AND SIMULATION**

# Analysis of Local Rearrangements in Chains during Simulation of the Plastic Deformation of Glassy Polymethylene

I. A. Strelnikovⁿ, N. K. Balabaevᵇ, M. A. Mazoᵃ,*, and E. F. Oleinikⁿ

ⁿ Semenov Institute of Chemical Physics, Russian Academy of Sciences, ul. Kosygina 4, Moscow, 119991 Russia
ᵇ Institute of Mathematical Problems of Biology, Russian Academy of Sciences, Institutskaya ul. 4, Pushchino, Moscow oblast, 142290 Russia

*e-mail: mazo@polymer.chph.ras.ru

Received April 17, 2013;
Revised Manuscript Received July 15, 2013

Abstract—A molecular-dynamics simulation of the low-temperature (~100 K below $T_g$) plastic deformation of glassy polymethylene (PM) was conducted. A model system consisting of 64 chains containing 100 CH₂ groups (the united-atoms approach) in each computational cell with periodic boundary conditions was considered. The behavior of 32 such cells was considered. Each cell was subjected to an active isothermal uniaxial compression at a constant temperature of $T_{def} = 50$ K to a strain of $\varepsilon = 30\%$. An analysis showed that the inelastic deformation of glassy PM proceeded via nonaffine displacements ("gliding") of chain fragments comprising 11–13 sites $-CH_2-$. These displacements are correlated and directed mainly along chain axes. Only a small number of conformational rearrangements occur in chains during the deformation of the material. Conformational transitions add only small additional displacements to nonaffine atomic transformations. A free-volume analysis using Voronoi–Delaunay tessellation in the deformed polymer did not show its relation to local plastic rearrangements.

DOI: 10.1134/S0965545X14010088

## INTRODUCTION

In the last decade, there has been considerable progress in understanding the mechanisms of deformation of metal glass above all owing to the application of computer-based-simulation methods [1–3]. Structural rearrangements responsible for plasticity, which are named shear transformations, were discovered and characterized for these materials [4–6].

For the first time, local rearrangements during the deformation of glassy polymer systems were considered in [7–12]. There, the features of the analysis of the inelastic deformation of chain structures were defined and the molecular simulation of the plastic deformation of atactic polypropylene (PP) and polycarbonate (PC) was conducted. It was established that plastic deformation was not the result of the conformation rearrangement of chains, but was a set of localized steplike shear cooperative displacements of lengthy chain fragments. Unit plastic rearrangements in a polymer glass have the structure of shear transformations. Repeated nucleation of such transformations defines the development of plasticity in glassy polymer materials.

The displacement of chains relative to each other is the main mechanism of deformation. Conformational changes in chains do not involve significant atomic displacements and do not lead to simple kinematic configurations known for the deformation of crystals, e.g., dislocations and disclinations, or to the specific polymer structures of rotons and strophons and similar helically formed structures [9]. In addition, the analysis of local strain in glassy chain systems has shown that the contribution of intramolecular forces to the deformation rearrangements is small.

In [13, 14], a simulation of the uniaxial compression of glassy polymethylene (PM) was performed, and it was shown that the frequency of conformational transitions increased with the growth of the deformation, although the concentrations of different conformers changed slightly during the deformation. Conformational transitions can correlate along the polymer chain. It was established that the accumulation of gauche conformers was not substantial for an increase in chain mobility, while the local density and general conformational mobility were not related to the local rotational mobility.

Earlier, the authors conducted a molecular-dynamics simulation of the low-temperature deformation of glassy PM [15]. Mechanical and thermodynamic characteristics of the deformation process, conformational compositions of the chains, and changes in the density of the glass as the deformation progressed were considered. It was shown that inelastic rearrangements in glassy PM did not begin with the conformational unfolding of coils, but with the gener-

![](./images/813154551694622720_1.jpg)

Fig. 1. Dependences averaged over 32 samples for (1) strain $\sigma$ and (2) density $\rho$ versus relative deformation $\varepsilon$ during uniaxial compression (averaging over 96 numerical experiments). Conditions of deformation: $T = 50$ K, $-d\varepsilon/dt = 2 \times 10^8\ \text{s}^{-1}$. The rms deviations are indicated by vertical lines on the plots.

ation of deformational local atomic rearrangements of the shear type.

In addition to the abovementioned investigation, a detailed analysis of torsion angles and nonaffine dis- placements of polymer chains in the process of defor- mation is presented in the present paper. This analysis is followed by a discussion of local rearrangements due to the uniaxial compression of glassy PM.

## DESCRIPTION OF THE MODEL AND THE SIMULATION PROCEDURE

Sixty-four PM chains each with a length of 100 $\text{CH}_2$ groups that were considered in the united-atoms approximation [16] were placed into a computational cubic cell with periodic boundary conditions. Valence bonds and bond angles were set according to the har- monic potentials

$$U(L) = K_L(L - L_0)^2 \quad \text{and} \quad U(\theta) = K_\theta(\theta - \theta_0)^2,$$

where $L$ is the length of the valence bond, $L_0 = 1.53\ \mathring{\text{A}}$, $K_\text{L} = 1047.5\ \text{kJ mol}^{-1}\ \mathring{\text{A}}^{-2}$, $\theta_0 = 113.0^\circ$, and $K_\theta = 167.6\ \text{kJ mol}^{-1}\ \text{rad}^{-2}$. For torsion angles, the used potential was

$$U(\varphi) = K_1(1 + \cos(3\varphi)) + K_2(1 + \cos(\varphi)),$$

where $K_1 = 6.704\ \text{kJ mol}^{-1}$ and $K_2 = 1.634\ \text{kJ mol}^{-1}$. Nonavalent interactions were set according to the Lennard-Jones potential

$$U(r) = \varepsilon_\text{LJ} \left[(R_\text{min}/r)^{12} - 2(R_\text{min}/r)^6\right],$$

where $\varepsilon_\text{LJ} = 0.503\ \text{kJ mol}^{-1}$ and $R_\text{min} = 4.2654\ \mathring{\text{A}}$.

In order to perform the numerical integration of Newton's equations of motion, the velocity Verlet algorithm [17] with a integration step of 1 fs was used. The temperature in the system was kept constant with a collision thermostat [18] with the parameters $\lambda = 5.5\ \text{ps}^{-1}$ and $m_0 = 1$ amu, which provided an insignifi- cant (~0.01 cP) increase in the viscosity of the system. The pressure was set and kept constant with a Ber- endsen barostat [19].

A detailed description of the process of preparation of amorphous polymer systems is given in [15]. In total, 32 samples with a mean density of $0.996\ \text{g/cm}^3$ were obtained at a temperature of 50 K from different initial data. Each of these samples was compressed in the thermostat, in which a temperature of 50 K was kept, to 30% along one of the axes at a velocity of $\varepsilon = -2 \times 10^{-4}\ \text{ps}^{-1}$ for 1.5 ns, while normal pressure was kept along the two remaining axes. Then, the dimen- sions of the computational cell in the direction of deformation were fixed and the system relaxed for 1 ns. In total, 96 numerical experiments were performed, that is, 3 independent calculations for each of the 32 samples. All results related to the unperturbed sys- tem were obtained via averaging over all 32 samples, while the results of the simulation of the deformation were obtained via averaging over all 96 calculations.

For the further analysis of the structural changes in the samples during calculations, the coordinates of all particles averaged over 1 ps were recorded every 10 ps ($\Delta\varepsilon = -0.2\%$). Averaging was performed in order to reduce the influence of temperature fluctuations on the results of calculations.

## RESULTS AND DISCUSSION

### The $\boldsymbol{\sigma-\varepsilon}$ Diagram and the Change in Density

Figure 1 shows the $\sigma-\varepsilon$ diagram and the depen- dence of the density on the deformation during uniax- ial compression at a temperature of 50 K averaged over three deformations along the axes of each of the 32 samples. The $\sigma-\varepsilon$ diagram has a shape featuring a sharp yield point at $\varepsilon$ approximately from $-12$ to $-13\%$ and an ultimate yield stress of $\sigma_y \sim 195$ MPa, which is typical for a polymer glass. After the sharp yield point, the deformation reaches the stationary yielding flow at a yield stress of $\sigma \sim 190$ MPa. When the deformations are small ($\varepsilon$ approximately from $-1.5$ to $-2.5\%$), an elastic response with a compres- sion modulus of $E \sim 2.6$ GPa and a Poisson ratio of $\text{v} = 0.42$ are observed. In general, the stress-strain dia- gram agrees well with both experimental data [20, 21] and the results of other numerical experiments for glassy polymers [13-15, 22]; however, the calculated strain exceeds experimental values, a result that is apparently due to the high velocity of strain in com- puter-assisted experiments.

The density of the system increases insignificantly during small deformations (~0.6%) and reaches its

---

POLYMER SCIENCE Series A Vol. 56 No. 2 2014

![](./images/813154551694622720_2.jpg)

Fig. 2. Frequency polygons for the values of orientation parameter $S$ in (1) initial samples and (2) samples deformed by 30%. The increment of $S$ is 0.05.

maximum at $\varepsilon = -7\%$, after which it starts decreasing (Fig. 1). A similar behavior of amorphous polyethylene (PE) was observed in [14, 15]. Thus, in the case of a delayed-elastic mode of deformation of $-2.5\% > \varepsilon > -12\%$, the increase in density during the deformation slows down and the density reaches the maximum and starts decreasing. The samples have already reached the initial density in the area of active yielding flow at $\varepsilon \sim -16\%$. The stationary yielding flow is accompanied by a systematic decrease in density.

It is known that PM chains crystallize in melt relatively easily [23]. No microcrystalline areas were detected in the considered samples during visual analysis. A detailed investigation into the orientational regularity of chains for each sample made it possible to calculate the degree of orientation of the separate fragments of chains for the initial and deformed samples. The segments connecting the next nearest carbon atoms along the chain were chosen as such fragments.

The degree of orientation, $S$, was calculated through the expression
$$S = 0.5(3\langle\cos^2\varphi_i\rangle - 1),$$
where $\varphi_i$ is the angle between the $i$th segment and the direction of the preferred orientation, $\mathbf{n}_s$, of the considered segments, which corresponds to the maximum value of $S$. Parameter $S$ adopts values from 0 (for a fully unoriented system) to 1 (when all segments are parallel to each other). Figure 2 shows frequency polygons for the values of $S$ in the initial samples and in the samples after 30% uniaxial compression. It is seen that the values of $S$ before the deformation are small: The average over all the samples is 0.15, a result that is evidence for the absence of noticeable anisotropy in them. A small residual anisotropy may be due to the presence of lengthy fragments of molecules formed solely by trans conformers in relatively small computational cells.

![](./images/813154551694622720_3.jpg)

Fig. 3. Distributions of $P_\varphi$ over the values of torsion angles $\varphi$ (1) before and (2) after uniaxial compression ($\varepsilon = 30\%$). The increment of $\varphi$ is $1^\circ$.

The deformation results in a slight increase in $S$; however, even when $\varepsilon = -30\%$, the degrees of orientation of deformed samples are not high, with an average value of $S \sim 0.21$. The increase in the orientational-order parameter during deformation was observed before in the amorphous phase of amorphous-crystalline PE [24]. The uniaxial compression of a sample leads to a decrease in its size in the direction of the applied force, thereby making the chains change their spatial orientation. Here, vector $\mathbf{n}_s$ tends to occupy the position perpendicular to the direction of the applied force.

### Conformational Transitions

The distributions of torsion angles in PM chains before and after deformation are shown in Fig. 3. It is seen that there are two types of conformers in the system—trans ($\varphi = 180^\circ \pm 15^\circ$) and gauche ($\varphi = 72^\circ \pm 14^\circ$ and $288^\circ \pm 14^\circ$)—and that the transitional states are practically absent.

Trans conformers dominate in all prepared samples; the concentration of trans conformers in the undeformed sample reaches approximately 92.6% on average. Such a high concentration of trans conformers in PM with united atoms was found also in [13–15, 25]. Conformational transitions are extremely rare in the stress-free state (one transition per sample over 30 ps). However, deformation results in active conformational mobility, as discovered in [13, 14]: The average numbers of trans–gauche and gauche–trans transitions per unit time increase with an increase in the degree of deformation, and this growth persists during the transition to the stationary-yielding-flow mode (Fig. 4). After the deformation ceases and the dimen-

![](./images/813154551694622720_4.jpg)

Fig. 4. (1, 2) Average numbers of (1) trans–gauche and (2) gauche–trans transitions per unit time (50 ps) and (3) corresponding compression deformation $\varepsilon$.

![](./images/813154551694622720_5.jpg)

Fig. 5. (1) Strain release in the direction of deformation, $\sigma_x$, during its fixation at $\varepsilon = -30\%$ and (2) the observed change in intensity of conformational transitions, $v_{conf}$, that is, the number of transitions in the sample over 50 ps.

sions of the cell are fixed, the conformational mobility slows sharply. In addition, Fig. 5 shows that the intensities of trans–gauche and gauche–trans transitions are similar. That is why deformation has a weak influence on the conformational composition of the polymer: The content of trans conformers decreased by just $0.6\%$.

It is interesting that, after the deformation ceases and the dimensions of the cell are fixed, the drops in the intensity of transitions and in strain proceed symmetrically (Fig. 5). It is possible that two modes of strain release are observed here: first, a fast mode with a characteristic time of 40–50 ps when the strain drops ~18% over 150 ps and, then, a relatively slow mode with a characteristic time of ~300 ps. Even longer calculations are required to reliably distinguish between these two modes.

The analysis of certain conformational transitions in the process of deformation showed that three types of these transitions can be distinguished: a steplike transition after which a new state persists (isolated transitions, Fig. 6a), a steplike conformational transition into a new state followed by a steplike relapse after a short time (relapsing transitions, Fig. 6b), and an extremely rarely occurring event when a transitional conformational state persists in a small section of the chain over time (Fig. 6c). It turns out that most conformational transitions due to deformation are isolated transitions; that is, the part of relapsing transitions, which stayed in a new state for less that 30 ps, was approximately $9\%$ of the total number of transitions.

The analysis of the dependence of conformational transitions on the distance to the end of the chain showed that transitions on the ends of the chain were less likely than those in its middle. This result is explained by the fact that terminal fragments possess a higher freedom of movement, a circumstance that assists the relaxation of the local strain leading to the conformational transition.

In order to evaluate the degree of correlation between the conformational rearrangements occurring in one chain, the probability of the occurrence of conformational transitions in each of the 20 neighboring sites was calculated as a function of the time after an isolated conformational transition (Fig. 7). The calculation was performed for all transitions that occurred in the process of deformation. Figure 7 shows that this

![](./images/813154551694622720_6.jpg)

Fig. 6. Characteristic changes in the conformational angles during deformation: (a) isolated transitions, (b) relapsing transitions, (c) “hanging up” in the transitional state.

POLYMER SCIENCE Series A Vol. 56 No. 2 2014

![](./images/813154551694622720_7.jpg)

Fig. 7. Probability of conformational transitions in 20 neighboring sites on the time after the isolated conformational transition: (1) even neighbors, (2) odd neighbors.

probability is maximum at the times below 10 ps and drops fast, becoming a background probability already for the times exceeding 30 ps. The probability depends also on the parity of the neighbor: It is higher for even neighbors than it is for odd neighbors.

In addition, Fig. 7 shows that conformational transitions do not occur within 30 ps (or 0.6% of deformation) after isolated transitions in neighboring sites in around 70% of the cases. If, however, transitions occur within 30 ps, one transition happens with a probability of 89%; two transitions, with a probability of 9%; and three transitions, with a probability of 1%.

Figure 8 presents the probability of a second conformational transition after an isolated transition during the first 10 ps (an increment of deformation of 0.2%) versus the number of sites between the conformers in one chain. The probability of such transitions is low and decreases quickly with the distance along the chain. Here, the dependence on the parity of the neighbor is clear as well.

These results are in good agreement with the data of [14], in which the same low probability of the reverse conformational transition and a slightly higher probability of the correlated transition in even neighbors along the chain than those in odd neighbors were observed.

The detailed analysis of the various types of conformational transitions during deformation that are observed within 30 ps after the isolated conformational transition showed that, in the conformers located next nearest to a chosen conformer, a transition to $t \to g^{\pm}$ is the most probable after a $g^{\pm} \to t$ transition, while after a $g^{\pm} \to t$ transition, a $t \to g^{\pm}$ transition can occur with a higher probability, although a $g^{\pm} \to t$ transition can likewise occur.

![](./images/813154551694622720_8.jpg)

Fig. 8. Probability of the correlated transition along the chain over 10 ps after the initial transition. The calculation was performed for all transitions that occurred during the process of deformation.

### Nonaffine Deformational Displacements

Various approaches are used in the literature to determine local atomic displacements during the simulation of the deformation of amorphous materials. However, the allocation of displacements without a correction for the deformation of the system on the whole makes it difficult to locate plastic rearrangements [10, 26]. Falk and Langer proposed one of the most effective methods for the analysis of structural rearrangements during the simulation of the deformation of a metal glass [27]. They suggested using rms difference $D^2$ between the actual changes in the distance between the considered particle and the surrounding particles and those distances that correspond to affine displacements $\varepsilon_{ij}$ of this area in order to quantitatively assess the values of the nonaffine displacements of the particle relative to its immediate surroundings during the transition of the system from the state at time $t - \Delta t$ to the state at time $t$:

$$
\begin{aligned}
D^{2}(t, \Delta t) &=\sum_{n=1}^{N} \sum_{i=1}^{3}\left(r_{n}^{i}(t)-r_{0}^{i}(t)\right. \\
&-\left.\sum_{j=1}^{3}\left(\delta_{i j}-\varepsilon_{i j}\right)\left[r_{n}^{j}(t-\Delta t)-r_{0}^{j}(t-\Delta t)\right]\right)^{2},
\end{aligned}
$$

where $r_{n}^{i}(t)$ is the $i$th component of the radius vector of particle $n$ at time $t$, the zero index corresponds to the particle for which the calculation is performed, $\delta_{ij}$ is the Kronecker symbol, and $\varepsilon_{ij}$ is the deformational tensor. Selecting the value of tensor $\varepsilon_{ij}$ that minimizes $D^2$, we find such a local affine transformation that

reflects the affine deformation of the surroundings of the considered particle in the best way. Further, the assessment of local structural rearrangements was performed with the use of the variable

$$
\bar{D}_{\min }(t, \Delta t)=\sqrt{\min _{\varepsilon_{i j}} D^{2}(t, \Delta t) / N}
$$

This variable characterizes the displacement of the considered particle relative to its local surroundings and correlates greatly with the modulus of the vector of the nonaffine displacement of the particle, $dr_{\text{non-aff}}$, which is calculated via the change in the sizes of the samples:

$$
\alpha_{\text{nonaff}}=\alpha_{\text{new}}-\alpha_{\text{old}} \frac{Box_{\alpha, \text{new}}}{Box_{\alpha, \text{old}}}, \quad \alpha=x, y, z,
$$

$$
d r_{\text{nonaff}}=\sqrt{x_{\text{nonaff}}^{2}+y_{\text{nonaff}}^{2}+z_{\text{nonaff}}^{2}},
$$

where $\alpha_{\text{nonaff}}-\alpha$ is the component of the vector of the nonaffine displacement of the particle; $\alpha_{\text{old}}$ and $\alpha_{\text{new}}$ are the coordinates of the considered particle along the $\alpha$ axis before and after the deformation, respectively; and $Box_{\alpha, \text{old}}$ and $Box_{\alpha, \text{new}}$ are the sizes of the cell along the $\alpha$ axis before and after the deformation, respectively.

The distribution of the values of $\bar{D}_{\min }$ for $\mathrm{CH}_{2}$ groups in all the considered systems is given in Fig. 9. It is important that, in the absence of deformation, the distribution of $\bar{D}_{\min }$ practically coincides with the distribution on the initial deformation section presented in Fig. 9 when the coordinates of the particles are compared at different times and at a temperature of $50 \mathrm{~K}$. In other words, the value of $\bar{D}_{\min }$ is solely due to thermal fluctuations. A monotonic increase in the average displacement and broadening of the distribution over displacements with deformation are observed, and relatively large displacements occur. Qualitatively, the process of the accumulation of local plastic deformations does not change during growth in the overall deformation. Let us further consider all particles that are displaced by more than $0.6 \AA$ during rearrangements.

![](./images/813154551694622720_9.jpg)

Fig. 9. Distributions of the particles of the system over $\bar{D}_{\min }$ for various degrees of deformation of the samples: changes in $\varepsilon(1)$ from 0 to $-0.2 \%$, (2) from -12 to $-12.2 \%$, and (3) from -29.9 to $-30 \%$. The increment of $\bar{D}_{\min }$ is $0.01 \AA$.

In order to examine the contribution of the conformational mobility to the local mechanisms of deformation, the values of $\bar{D}_{\min }$ for the particles that participated in the conformational transition (four particles forming a torsion angle were considered for each transition) were compared to the overall distribution of $\bar{D}_{\min }$ (Fig. 10). Conformational transitions do contribute to $\bar{D}_{\min }$; however, the proportion of particles participating in the transition is only a small part $(\sim 2 \%)$ of all the rearranged particles. According to the analysis of chains containing particles with relatively large values of $\bar{D}_{\min }$, the proportion of those chains in which conformational transitions occur reaches $30 \%$. Nevertheless, even this input is not enough for us to state that collective displacements in the PM chain are caused by (accompanied by) conformational transitions.

The analysis of the dependence of the average displacement of particles on their number in the chain showed that the ends of chains provide large displacements in general. Apparently, this is due to the additional capability of the ends of chains to turn and undergo translations.

The spatial distribution of particles with a relatively high value of $\bar{D}_{\min }(>0.6 \AA)$ to the macroscopic sharp yield point and in the area of steady yielding flow is given in Fig. 11. It is seen that correlated displacements of the lengthy sections of chains occur. In order to investigate this correlation in detail, a correlation function of the value of $\bar{D}_{\min }$ along the chain was calculated for each chain:

$$
C F(\Delta N)=\frac{\frac{1}{100-\Delta N} \sum_{i=1}^{100-\Delta N}\left(\bar{D}_{\min, i}-\left\langle\bar{D}_{\min, i}\right\rangle\right)\left(\bar{D}_{\min, i+\Delta N}-\left\langle\bar{D}_{\min, i+\Delta N}\right\rangle\right)}{\frac{1}{100} \sum_{i=1}^{100}\left(\bar{D}_{\min, i}-\left\langle\bar{D}_{\min, i}\right\rangle\right)^{2}},
$$

---

POLYMER SCIENCE Series A Vol. 56 No. 2 2014

![](./images/813154551694622720_10.jpg)

Fig. 10. Distributions of $\bar{D}_{\text{min}}$ for (1, left ordinate axis) all particles and (2, right ordinate axis) particles that participated in the conformational transition for a change in $\varepsilon$ from $-24$ to $-24.2\%$. The increment of $\bar{D}_{\text{min}}$ is $0.05$ Å.

where $i$ is the numeration of particles along the chain, $\bar{D}_{\text{min},j}$ is the value of $\bar{D}_{\text{min}}$ for the $i$th particle, and $\langle\bar{D}_{\text{min},j}\rangle$ is the average over the system displacement of the $i$th particle in the chain. The use of $\langle\bar{D}_{\text{min},j}\rangle$ is necessary because terminal sites are displaced more than central sites on average. The data were averaged over all chains and samples. The resulting dependence was close to an exponential dependence (Fig. 12): $CF(\Delta N)=CF_{0}+A\mathrm{exp}(-\Delta N/N_{\mathrm{c}})$, with $N_{\mathrm{c}}=13.3$ when $\varepsilon$ changes from 0 to $-0.2\%$ and $N_{\mathrm{c}}=11.6$ when $\varepsilon$ changes from $-28$ to $-28.2\%$. In other words, displacements during the deformation of glassy PM proceed by chain segments with lengths of $11-13-\mathrm{CH}_{2}-$ groups, and the segment lengths do not change significantly during growth in the overall deformation. Such a length is proportionate to the dimensions of the computational cell. This circumstance might cause the absence of localization and transformation of displacements into shear bands.

For the statistical analysis of the displacements of long chain sections, the orientations of segments connecting the next nearest particles of these sections, the orientations of segments corresponding to the nonaffine displacement of particles, and the angle between the directions of the preferred orientation of the above-described two types of segments were calculated. Having selected all chain sections consisting of particles with values of $\bar{D}_{\text{min}}>0.6$ Å, we considered only sections with lengths of 5–10 particles.

The distribution of the degrees of orientation of segments connecting the particles of the next nearest displacing segments showed that the majority of them were basically a sequence of trans conformers. Here, the orientation of displacements is slightly lower; however, it is a priori sufficient to estimate the collective uniaxial shear. This fact makes it possible to use a vector of the preferred orientation for the characteristics of the direction of such shear.

A similar picture was obtained for glassy PP during small deformations ($\varepsilon=\pm0.1\%$) in [10], where an orientational correlation of nonaffine displacements up to the tenth neighbor along the chain was observed. Figure 13 shows the frequency distributions of angles between the directions of the preferred orientation of chain sections and the displacements of particles. It is seen that, during small deformations, the displacements of chain sections occur mostly along the chain. This mechanism persists with an increase in deformation, but the displacements in other directions occur as well. In other words, the preferred mechanism of deformation in the model with united atoms is the "gliding" of chains relative to each other.

# Changes in the Free Volume of Glass during Deformation

In order to analyze the influence of the free volume on local plastic rearrangements, a Voronoi–Delaunay tessellation was calculated for the PM glass. The volume of a Voronoi polyhedron and the radius of a Delaunay sphere were considered the measures of free volume. The Voronoi polyhedron characterizes the free volume per atom. The Delaunay sphere is defined as a sphere passing through four particles of the system and not containing other particles. Thus, the radii of Delaunay spheres characterize the voids in a sample.

![](./images/813154551694622720_11.jpg)

Fig. 11. Spatial distribution of particles with $\bar{D}_{\text{min}} > 0.6$ Å during deformations of the samples, $\varepsilon$, (a) from $-6$ to $-6.2\%$ and (b) from $-24$ to $-24.2\%$.

It was found that the largest local deformation displacements were not related to the changes in the local free volume. This result means that stationary yielding flow can proceed without notable changes in the volume when the temperature of deformation of the polymer glass is low, a circumstance that agrees well with the work of Capaldi et al. [14], in which the steadiness of the density of the system was observed for large values of deformation.

![](./images/813154551694622720_12.jpg)

Fig. 12. (Open circles) Correlation function of the non-affine displacements along the chain and (solid line) its exponential approximation during a change in $\varepsilon$ from $-28$ to $-28.2\%$.

![](./images/813154551694622720_13.jpg)

Fig. 13. Distributions over the angle between the orientation vectors of the chain sections and their displacements in (a) the linear region ($\varepsilon = 0$ to $-2\%$) and (b) the region of yielding flow ($\varepsilon = -28$ to $-30\%$). The increment of the aforementioned angle is $1^\circ$.

POLYMER SCIENCE Series A Vol. 56 No. 2 2014

## CONCLUSIONS

The performed simulation of the low-temperature inelastic compressive deformation of glassy PM whose chains consist of united atoms has made it possible to reveal and analyze the local mechanisms of deformation. It turned out that the displacements of chain fragments consisting of 11–13 $CH_2$ groups along the chain were the main type of deformation rearrangement. Deformation begins with the gliding of such fragments, and this mechanism does not change with growth in the deformation to $\varepsilon=-30\%$. The mechanism of conformational unfolding of chains does not play a significant role in the low-temperature plasticity of PM glass.

The absence of the intermolecular correlation of the values of displacements $\bar{D}_{\text{min}}$ indicates that such displacements of segments during deformation have a weak influence on the structure of the nearest surroundings. The analysis of angles between the directions of nonaffine displacements and the vectors of the preferred orientation of such sections showed that the distribution over angles has a peak in the area of small angle values. It is possible to conclude that "gliding" of the active chain fragment along other chains is the priority mechanism of rearrangements.

The displacements of deformationally active chain fragments in other directions are almost absent in the area of linear deformations. The distribution over angles becomes more uniform with growth in the deformation; i.e., rotational displacements occur. However, the peak in the area of small angles persists.

A high content (96.2%) of trans conformers is the characteristic feature of the considered system. The conformational mobility in chains intensifies during the deformation of the sample, and the frequency of conformational transitions increases continuously with growth in $\varepsilon$. An analogous behavior was observed in other studies [13–15]. However, the ratio between trans and gauche conformers in the sample changes insignificantly before macroscopic deformations of $\varepsilon=30\%$. It turned out that conformational transitions were weakly correlated inside the chains. Their spatial correlation was not detected either.

The correlation between conformational transitions and rearrangements detected with the use of the characteristic of nonaffine displacement $\bar{D}_{\text{min}}$ was analyzed. The particles that participated in conformational transitions have enlarged values of $\bar{D}_{\text{min}}$; however, the portion of such sections is small and does not exceed 5% of all particles rearranged during deformation. The main deformational displacements of long chain sections are not caused or accompanied by conformational transitions in these chains.

## ACKNOWLEDGMENTS

This work was financially supported under a grant from the Ministry of Education and Science of the Russian Federation (state contract no. 16.523.12.3001).

## REFERENCES

1. M. L. Falk and C. E. Maloney, *Eur. Phys. J. B* **75**, 405 (2010).
2. L. Bertier, *Physics* **4**, 42 (2011).
3. R. Dasgupta, H. George, E. Hentschel, and I. Procaccia, *Phys. Rev. E: Stat. Phys., Plasmas, Fluids, Relat. Interdiscip. Top.* **87** (022810) (2013).
4. V. Bulatov and A. Argon, *Mod. Simul. Mater. Sci. Eng.* **2**, 203 (1994).
5. A. Argon, *Acta Metall. Mater.* **27**, 47 (1979).
6. A. S. Argon and M. J. Demkowicz, *Metall. Mater. Trans. A* **39**, 1762 (2008).
7. D. R. Theodorou and U. W. Suter, *Macromolecules* **18**, 1467 (1985).
8. D. R. Theodorou and U. W. Suter, *Macromolecules* **19**, 139 (1986).
9. A. S. Argon, P. H. Mott, and U. W. Suter, *Phys. Status Solidi B* **172**, 193 (1992).
10. P. H. Mott, A. S. Argon, and U. W. Suter, *Philos. Mag. A* **67**, 931 (1993).
11. M. Hutnik, A. S. Argon, and U. W. Suter, *Macromolecules* **26**, 1097 (1993).
12. D. R. Theodorou and U. W. Suter, *Macromolecules* **19**, 379 (1986).
13. F. M. Capaldi, M. C. Boyce, and G. C. Rutledge, *Phys. Rev. Lett.* **89** (175505) (2002).
14. F. M. Capaldi, M. C. Boyce, and G. C. Rutledge, *Polymer* **45**, 1391 (2004).
15. N. K. Balabaev, M. A. Mazo, A. V. Lyulin, and E. F. Oleinik, *Polym. Sci. A* **52**, 633 (2010).
16. E. A. Zubova, A. I. Musienko, N. K. Balabaev, E. B. Gusarova, M. A. Mazo, L. I. Manevich, and Al. Al. Berlin, *Dokl. Phys. Chem.* **418**, 15 (2008).
17. M. P. Allen and D. J. Tildesley, *Computer Simulation of Liquids* (Clarendon, Oxford, 1987).
18. A. S. Lemak and N. K. Balabaev, *J. Comput. Chem.* **17**, 1685 (1996).
19. H. J. C. Berendsen, J. P. M. Postma, W. F. Gunsteren, A. Di Nola, and J. R. Haak, *J. Chem. Phys.* **81**, 3684 (1984).
20. J. Perez, *Physics and Mechanics of Amorphous Polymers* (Balkema, Rotterdam, 1998).
21. E. Oleinik, in *High Performance Polymers*, Ed by E. Baer and S. Moet (Hanser, Munich, 1990), p. 60.
22. A. V. Lyulin, B. Vorselaars, M. A. Mazo, N. K. Balabaev, and M. A. J. Michels, *Europhys. Lett.* **71**, 618 (2005).
23. D. L. White, *Polyethylene, Polypropylene and Other Polyolefins* (Professiya, St. Petersburg, 2006) [in Russian].
24. S. Lee and G. C. Rutledge, *Macromolecules* **44**, 3096 (2011).
25. D. Hossain, M. A. Tschopp, D. K. Ward, J. L. Bouvard, P. Wang, and M. F. Horstemeyer, *Polymer* **51**, 6071 (2010).
26. M. L. Falk and J. S. Langer, *Annu. Rev. Condens. Matter Phys.* **2**, 353 (2011).
27. M. L. Falk and J. S. Langer, *Phys. Rev. E: Stat. Phys., Plasmas, Fluids, Relat. Interdiscip. Top.* **57**, 7192 (1998).

Translated by E. Boltukhina

---

POLYMER SCIENCE Series A Vol. 56 No. 2 2014