![](./images/812341924705861632_1.jpg)

Lattice-gas modeling of CO adlayers on Pd(100)
Da-Jiang Liu

Citation: *The Journal of Chemical Physics* **121**, 4352 (2004); doi: 10.1063/1.1778134
View online: http://dx.doi.org/10.1063/1.1778134
View Table of Contents: http://scitation.aip.org/content/aip/journal/jcp/121/9?ver=pdfcov
Published by the AIP Publishing

Articles you may be interested in
[Lattice-gas model of nonadditive interacting particles on nanotube bundles](http://)
J. Chem. Phys. **134**, 064702 (2011); 10.1063/1.3530788

[Simulation of the effect of surface-oxide formation on bistability in CO oxidation on Pt-group metals](http://)
J. Chem. Phys. **126**, 074706 (2007); 10.1063/1.2483966

[Atomistic lattice-gas modeling of CO oxidation on Pd(100): Temperature-programed spectroscopy and steady-state behavior](http://)
J. Chem. Phys. **124**, 154705 (2006); 10.1063/1.2186314

[Lattice-gas study of the kinetics of catalytic conversion of NO–CO mixtures on rhodium surfaces](http://)
J. Chem. Phys. **114**, 10927 (2001); 10.1063/1.1349180

[Ab initio diffusional potential energy surface for CO chemisorption on Pd{110} at high coverage: Coupled translation and rotation](http://)
J. Chem. Phys. **107**, 8103 (1997); 10.1063/1.475073

![](./images/812341924705861632_2.jpg)

# Lattice-gas modeling of CO adlayers on Pd(100)
Da-Jiang Liu
Ames Laboratory, U.S. Department of Energy, Iowa State University, Ames, Iowa 50011

(Received 21 November 2003; accepted 8 June 2004)

Using a lattice-gas model with pairwise interactions, we study the ordered structures, coverage dependence of the heat of adsorption, and other experimentally observable behavior of adsorbed CO overlayers on Pd(100) single crystal surfaces. Transfer matrix and Monte Carlo methods give accurate information regarding the lattice-gas model that often contradicts simple mean-field-like analysis. We demonstrate the usefulness of the model by reproducing experimental results over a large range of pressures and temperatures. © 2004 American Institute of Physics.
[DOI: 10.1063/1.1778134]

## I. INTRODUCTION

CO adsorption on metal surfaces has been studied extensively as a benchmark system for chemisorption. In particular, great deal of information has been accumulated during the last 30 years about CO adsorption on Pd(100) surfaces using several different experimental techniques, and under a range of pressures and temperatures. $^{1-4}$ There are also detailed theoretical studies of CO adsorption on Pd(100) using first-principles approaches. $^{5,6}$ However, surprisingly, no previous statistical mechanics studies have been performed to precisely determine adlayer ordering and phase transitions for this system. This is a significant omission since such analysis provides strong constraints on the type and magnitude of adspecies interactions. It also provides a reliable determination of thermodynamic quantities, which is not possible with simplified analyses. Such information is invaluable in interpreting other experiments, e.g., related to CO adsorption energies.

A long-standing motivation for such detailed studies of simple chemisorption systems is to provide insight into catalytic surface reactions. It is also well recognized that ordering and islanding of reactants will limit the utility or validity of mean-field-type rate equation treatments of the reaction kinetics. $^{7}$ Hence, accurate and robust atomistic modeling of adlayer structure for individual reactants is a crucial first step in building realistic atomistic model of related surface reactions, e.g., for CO oxidation on Pd(100). $^{8}$

In this paper, we develop and analyze a lattice-gas (LG) model for CO adlayers on Pd(100). Our focus is on equilibrium aspects of this system, since molecularly adsorbed CO can diffuse quite rapidly on this surface under normal situations facilitating adlayer equilibration. The main techniques used to analyze behavior of the lattice-gas model are the transfer matrix method and Monte Carlo simulation. We aim to reproduce as many experimental observations as possible using a relatively simple model described in Sec. II. We present the first detailed and precise analysis of complex surface ordering below 0.5 ML (monolayer) for this model in Sec. III. Specifically, we provide a phase diagram which can be compared with experiments to extract values of lateral interactions. Our results show that some previous estimates from comparison with experiments $^{9}$ and density-functional theory (DFT) (Ref. 6) are not viable. The structure of dense CO adlayers is studied in Sec. IV. The heat of adsorption is studied in Sec. V. Our results show that with only short-ranged lateral repulsive interactions, the heat of adsorption decreases significantly only after coverage of CO exceeds 0.5 ML, contradicting some recent analyses. $^{9}$ Finally, some adsorption isobars are presented in Sec. VI which show good agreement with experiments over a large range of temperatures and pressures.

## II. LATTICE-GAS MODEL FOR CO/PD(100) AND ITS ANALYSIS

Various experiments $^{1,4,10}$ show that (at least below 0.5 ML) adsorbed CO resides only at bridge sites on Pd(100). Thus, our modeling of equilibrated adlayer configurations allows population of bridges sites only. We note, however, that it was suggested $^{5}$ that during adsorption, CO is first steered towards the less favorable top sites. Thus, in more general modeling of nonequilibrium configurations under reaction conditions with coadsorbates, it is appropriate to allow population of other sites. $^{8}$ Below, $a=2.75$ Å denotes the surface lattice constant of Pd(100) surface.

Our LG modeling also assumes only pairwise interactions between CO adsorbates. Figure 1 illustrates the specific interactions used: we incorporate nearest-neighbor (NN) interactions $\omega_{1}$ for CO pairs separated by distance $a/\sqrt{2}$, second NN (2NN) interactions $\omega_{2}$ for separation $a$, third NN (3NN) interactions $\omega_{3}$ for separation $\sqrt{2}a$, and sometimes fourth NN (4NN) interactions $\omega_{4}$ for separation $\sqrt{5/2}a$. Also illustrated in the figure is the experimentally observed $c(2\sqrt{2}×\sqrt{2})R45^{\circ}$ ordered structure, and the (so far not observed) $(\sqrt{5/2}×\sqrt{5/2})R18.4^{\circ}$ structure which will be discussed later.

In applying our model to analyze the heat of adsorption and the adsorption isobars for CO/Pd(100), we need also information of the heat of adsorption at low coverage, which corresponds to the absorption energy of an isolated CO molecule at a bridge site. This quantity was measured to be 1.55 eV in an early experiment by Tracy and Palmberg, $^{1}$ and to be 1.67 eV in more recent experiments. $^{3,4}$ Using DFT incorpo-


![](./images/812341924705861632_3.jpg)

FIG. 1. Schematic of the ordered structure and of the pairwise interactions used in this paper. Large open circles represent Pd atoms and small solid circles represent CO molecules adsorbed on the bridge site of the Pd(100) surface. The unit cell for the $c(2\sqrt{2}\times\sqrt{2})R45^{\circ}$ structure is drawn on the left and the unit cell of the $(\sqrt{5/2}\times\sqrt{5/2})R18.4^{\circ}$ structure is drawn on the right.

rating the generalized gradient approximation (GGA), the value 1.92–1.98 eV is obtained for the binding energy with the PW91 functional. $^{5,11}$ Using the RPBE functional, the binding energy is reduced to $1.50\ \text{eV}.^{11}$

To analyze the above two-dimensional LG model, in this paper we use two standard yet powerful statistical mechanical techniques: the transfer matrix (TM) and the Monte Carlo (MC) methods. These two methods are often complementary. Using TM, one can always obtain the equilibrium free energy and other thermodynamic properties of the system. However, it is difficult to include long-range interactions using TM. For example, performing analysis on a system or strip of size $M\times\infty$, in order to include 3NN interaction $\omega_3$, it is necessary to consider all configurations of two columns spanning the strip. Thus, one must consider a total of $2^{2M}$ configurations, if one does not reduce this number by exclusion and symmetry properties. In some situations, as approximations, one can reduce the size of the transfer matrix by considering only interactions along or nearly along the finite direction. $^{12}$ On the other hand, it is relatively straightforward to include long-range interactions using the MC method. However, standard MC algorithms can become inefficient and very slow to relax near phase boundaries so that true equilibrium properties are hard to obtain from simulations.

### III. $c(2\sqrt{2}\times\sqrt{2})R45^{\circ}$ ORDERING BELOW 0.5 ML

From the observation of $c(2\sqrt{2}\times\sqrt{2})R45^{\circ}$ ordered structure, it has been deduced that lateral interactions between CO(ads) consist of strong NN and 2NN repulsions, and a weak 3NN repulsion. It has also been pointed out by Behm et al. $^{3}$ that the 3NN repulsion $\omega_3$ should not be too strong, otherwise it would instead produce a $(\sqrt{5/2}\times\sqrt{5/2})R18.4^{\circ}$ structure, which is not observed experimentally for temperatures above 200 K.

In order to quantify the effect of the 3NN interaction on the ordering of CO adsorbates, we conduct a study of the phase diagram of the lattice-gas model with very strong NN and 2NN repulsions (i.e., exclusion), and a finite 3NN repulsion ($\omega_3>0$). (Note that the 2NN exclusion only applies in this section, while later we shall use finite 2NN repulsion.)

Different aspects of this model have been studied previously. The case of no 3NN interactions ($\omega_3=0$) represents pure hard core particles with nearest- and second-nearest-neighbor exclusion on a square lattice. At the maximum coverage $\theta_{\text{CO}}=0.5$, the ground state is highly degenerate, with alternating half-filled diagonal rows or columns sliding freely with each other without energy penalty. The transition to this semordered state is subject to many debates. From transfer matrix calculation, Ree and Chestnut claim that it is a third-order transition with a cusp point in compressibility. $^{13}$ See Ref. 14 and references therein for alternative methods and interpretations. At the other limit with $\omega_3=\infty$, it was found $^{15}$ that there is a first-order liquid-solid-like transition with increasing CO coverage. The ordered phase has a $(\sqrt{5/2}\times\sqrt{5/2})R18.4^{\circ}$ structure.

Surprisingly, we found no systematic study of the phase diagram of the model with finite 3NN repulsion, though a transfer matrix study of the model with an anisotropic finite 3NN repulsion along only one axial direction has been performed. $^{16}$

![](./images/812341924705861632_4.jpg)

FIG. 2. $\mu$-$\omega_3$ phase diagram of the lattice-gas model with NN and 2NN exclusion and 3NN repulsion. Phase boundaries between the disordered phase and the two ordered phases are obtained from locating maxima in $d\theta/d\mu$. The dashed lines dashed lines are from TM (with strip of size 10) calculations, and the symbols are from Monte Carlo simulations with histogram reweighting. The dotted line is the conjectured transition line using fermion approximation. See text and the Appendix for more details.

Figure 2 is the chemical potential versus the third NN repulsion $\omega_3$ (both normalized by $k_BT$) phase diagram obtained from analysis of transfer matrix and Monte Carlo data. The symbols are data points obtained from Monte Carlo simulations by locating the maxima of either the compressibility, or the heat capacity for finite systems of size $L\times L$ with periodic boundary conditions, with $L$ ranges from 40 to 128. The dashed lines are obtained from transfer matrix calculations using strip size of 10. Figure 2 show that the model exhibits following distinct phases: the disordered phase, the $c(2\sqrt{2}\times\sqrt{2})R45^{\circ}$ phase, the $(\sqrt{5/2}\times\sqrt{5/2})R18.4^{\circ}$ phase, and a semordered phase. The semordered phase is the extension of the above mentioned degenerate phase with $\omega_3=0$ and has long-ranged ordering in one direction only. The transitions between the disordered phase and the two fully ordered phases are first order, while the transition between the disordered phase and the semordered phase, and between the semordered and the $c(2\sqrt{2}\times\sqrt{2})R45^{\circ}$ are continuous. Numerical evidences suggests that there is a multi-critical point near $\beta\mu=5.1$ and $\beta\omega_3=0.2$. See the Appendix for more results and discussions of this model.

Within the framework of the lattice gas model with only repulsive interactions between neighboring pairs up to 3NN, one can conclude from Fig. 2 that $0.005\ \text{eV}<\omega_3<0.05\ \text{eV}$

in order to match experimental observation that no $(\sqrt{5/2} \times \sqrt{5/2})R18.4^\circ$ or semiordered phase is observed at room temperature. A caveat is that introducing further neighboring interactions can change the phase diagram significantly and the above constraint on the magnitude of $\omega_3$ is no longer valid if longer-ranged or nonpairwise interactions should be considered. A complete experimental phase diagram can help us determine the magnitude of the interactions more precisely. Unfortunately, such information is not currently available. However, we do note that the onset coverage (0.4 ML) of the $c(2\sqrt{2} \times \sqrt{2})R45^\circ$ (cf. Fig. 11 in Ref. 3) is quite consistent with the model (see Fig. 7 in the Appendix).

Based on the above analysis (and also our investigations in subsequent sections), we assign a value of $\omega_3=0.03$ eV for the strength of the 3NN repulsive interactions. In the following analyses which include consideration of behavior for CO coverages above 0.5 ML, it is necessary to relax the constraint of second NN exclusions. The value of $\omega_2$ of around 0.17 eV is determined from our analysis of the heat of adsorption in Sec. V, and adsorption isobars in Sec. VI. However, before presenting these analyses, in Sec. IV, we provide a more complete picture of adlayer ordering by describing behavior at coverages above 0.5 ML (using the parameter choice $\omega_1=\infty$, $\omega_2=0.17$ eV, and $\omega_3=0.03$ eV).

## IV. STRUCTURE OF DENSE CO ADLAYERS

Because of the difficulties of experimental techniques (e.g., work function and infrared analysis) in dealing with high CO coverages ($\theta_{\text{CO}}>0.5$), structures of dense CO adlayers on Pd(100) are a matter of some debate. $^{17-19}$ As $\theta_{\text{CO}}$ increases above 0.5 ML, it is concluded from diffraction studies that the adlayers structure undergoes a commensurate-incommensurate transition (CIT). The study by Schuster $et$ $al.^{19}$ suggests it is in the Pokrovsky-Talapov universality class, consistent with expectation from symmetry arguments.

Lattice-gas models are not ideal for study of CIT's, since they put too many constraints on the structure of domain walls. Nonetheless, we perform a Monte Carlo study to investigate CO adlayer structure above 1/2 ML. We simulate the system at a fixed pressure while lowering the temperature. We use Glauber dynamics (corresponding to adsorption/desorption in the LG model) with the Metropolis algorithm. Occasionally, we also mix in Kawasaki dynamics (corresponding to diffusion in the LG model) with Glauber dynamics. Here, our focus is in the equilibrium structure of CO overlayer, thus we do not need to mimic the physical kinetics accurately. The primary challenge is that due to CO adspecies repulsions, adlayers can become nearly "frozen" using normal dynamics at high CO coverages and low substrate temperatures. In fact, the LG model with NN and 2NN exclusion has been used to study the glass transition. $^{20}$

Although our simulations are not faithful to the physical adlayer dynamics, they provide at least some qualitative insights into adlayer structure. For a fixed system size with periodic boundary conditions, if we lower the temperature very slowly, eventually a single domain occupies the whole system. Upon further lowering the temperature, defects are formed. However, we are unable to observe any well-defined domain wall structure as suggested by Berndt and Bradshaw. $^{18}$ On the other hand, if we lower the temperature more quickly, then different domains still occupy the system near the transition point. Further decreasing the temperature is accompanied by the enlargement of those original domains, and emergence of defects inside different domains. We show in Fig. 3 a snapshot of such a configuration generated by Monte Carlo simulations.

![](./images/812341924705861632_5.jpg)

FIG. 3. Snapshot of Monte Carlo simulations using the Glauber dynamics and the Metropolis algorithm for the LG model at a fixed pressure while lowering the temperature. The annealing rate is $10^4$ MCS/K (each site in the system is sampled once on average for each MCS). Other parameters are $p_{\text{CO}}=10^{-7}$ Torr, $\omega_1=\infty$, $\omega_2=0.17$ eV, $\omega_3=0.03$ eV. The snapshot is taken at $T=400$ K. For illustration, we denote CO with exactly two 2NN and four 3NN by a circle, and all other CO ("defects") by a black dot. Also note that the Pd(100) substrate (not shown) is rotated $45^\circ$. Shown in the figure is a $L=128$ subsystem in a simulation with $L=256$ using periodic boundary conditions. $\theta_{\text{CO}}=0.511$ ML.

## V. HEAT OF ADSORPTION

Assuming equilibrium between CO in the gas phase and the chemisorbed phase, the Clausius-Clapeyron equation relates the gas phase pressure $P$ to an isosteric heat of adsorption, $E_{\text{st}}$, via
$$
E_{\text{st}}=-\left[d \ln P / d\left(1 /\left(k_{B} T\right)\right)\right]_{\theta}. \tag{1}
$$

Various experimental techniques $^{1,3,9,21}$ give similar results for the value of $E_{\text{st}}$ as $\theta_{\text{CO}} \to 0$, while conflicting results have been obtained for the coverage dependence of $E_{\text{st}}$. Most studies $^{1,9,21}$ show a decrease in $E_{\text{st}}$ with increasing $\theta_{\text{CO}}$, while the study by Behm $et$ $al.^{3}$ shows a roughly constant $E_{\text{st}}$ for $\theta_{\text{CO}}<0.5$. Contamination by carbon is suggested $^{3}$ as the reason for this discrepancy, a claim disputed by others. $^{9}$

The presence of lateral interactions between CO adspecies is often invoked $^{1,9}$ to explain the coverage dependence of $E_{\text{st}}$. Using the transfer matrix technique, it is rather straightforward to calculate the heat of adsorption from a lattice-gas Hamiltonian. Such a study has been performed for the O/Ru(0001) system $^{22}$ with interactions based on DFT calculations, yet to our knowledge, has not been performed for the CO/Pd(100) system.

In lattice-gas modeling, it is appropriate to use the grand canonical ensemble. We assume simply that the gas phase pressure $P$ is related to the chemical potential through

![](./images/812341924705861632_6.jpg)

FIG. 4. Transfer matrix calculation of the isosteric heat of adsorption versus CO coverage on Pd(100). The lines are obtained using strips of size 8, and the symbols are obtained using strips of size 10. Nearest-neighbor interaction $\omega_{1}$ is assumed to be infinite and other neighboring interactions are shown in the figure. $T=300$ K.

$\mu=k_{B}T\ln(P/P_{0})$ where $P_{0}$ is a reference pressure at which the gas phase chemical potential is zero. More accurate forms of the relationship between the pressure and the chemical potential will introduce corrections to the heat of adsorption on the order of $k_{B}T$, which is negligible for present purposes. Unlike the isobar experiments treated later in Sec. VI, for our analysis here, we do not need information regarding prefactors for desorption, or the sticking coefficient for adsorption.

Using the transfer matrix method, we examine the coverage dependence of $E_{\text{st}}$ for the lattice-gas model with various choices of interactions. Any coverage dependence would reflect the influence of adspecies interactions which can cause $E_{\text{st}}$ to deviate from its limiting value $\epsilon_{b}$, the binding energy of an isolated adsorbate. Some of the results are shown in Fig. 4.

For the lattice gas model with only a finite 2NN repulsive interaction, the heat of adsorption is effectively a step function, with the form

$$
E_{\text{st}} \approx
\begin{cases}
\epsilon_{b} & \text{if } \theta<0.5 \\
\epsilon_{b}-4\omega_{2} & \text{if } 0.5<\theta<1.
\end{cases} \tag{2}
$$

The result can be explained as follows: for $\theta<0.5$, adsorbed CO molecules can rearrange themselves to avoid any 2NN pairs. Around $\theta=0.5$, they form a near-perfect $c(2\sqrt{2}$ $\times\sqrt{2})R45^{\circ}$ adlayer. To adsorb more CO molecules beyond this near-perfect overlayer, for each additional molecule adsorbed, it is necessary to move two molecules away from their original superlattice position and create four second NN pairs. See Fig. 5 for an illustration.

With longer-ranged repulsive interactions, $E_{\text{st}}$ decreases as $\theta_{\text{CO}}$ increases even for $\theta_{\text{CO}}<0.5$. However, the coverage dependence is quite nonlinear. For example, with 3NN interactions only the dotted line, $E_{\text{st}}$ only decreases slightly for $\theta_{\text{CO}}<0.25$. This is again due to the fact that below this coverage, CO(ads) can easily arrange themselves in a way to avoid any 3NN pairs.

With the present set of parameters for lateral interactions, the lattice-gas model produces a coverage dependence of the heat of adsorption somewhere between the experimental results of Behm *et al.* and other groups. Most of the decrease in the heat of adsorption occurs when $\theta_{\text{CO}}>0.5$, while only a slight decrease occurs when $\theta_{\text{CO}}<0.5$.

![](./images/812341924705861632_7.jpg)

FIG. 5. Schematic showing the accommodation of an extra CO molecule in an otherwise perfect $c(2\sqrt{2}\times\sqrt{2})R45^{\circ}$ structure.

The near parabolic decrease in $E_{\text{st}}$ starting from $\theta_{\text{CO}}$ $=0$, as well as the transient increase after the ordering transition, shown by Fig. 4, are quite reminiscent to the experimental results of Guo and Yates$^{23}$ for CO adsorption on Pd(111). However, they reported a plateau at an ordering transition, while we see first a sharp drop and then a plateau at the ordering transition point.

The controversy regarding the heat of adsorption is unresolved. On one hand, the work by King and co-workers$^{9}$ using single crystal adsorption calorimetry is the most direct and reliable. On the other hand, their analysis of the data produces estimates for interactions $\omega_{3}=0.26$ eV and $\omega_{4}$ $=0.026$ eV using our notation which are certainly far too large. It is both inconsistent with the observed $c(2\sqrt{2}$ $\times\sqrt{2})R45^{\circ}$ structure see Sec. III, and also create too big a decrease in the heat of adsorption as $\theta_{\text{CO}}$ exceed 0.5 ML.

## VI. ADSORPTION ISOBARS

For a CO adlayer in equilibrium with gas phase CO, it is clear that as the surface temperature increases at fixed pressure, the CO coverage will decrease. For higher fixed pressures, this decrease will be delayed until a higher temperature range. To quantify this behavior using our LG model, one needs a more quantitative determination of the relationship between pressure and chemical potential than that presented in the preceding section. To this end additional assumptions are needed. We assume that the impingement rate is given by $P/\sqrt{2\pi mk_{B}T}$ and the attempt frequency for desorption is $\nu_{0}$, then we assume that

$$
\mu=\epsilon_{b}+k_{B}T\ln\frac{P}{\nu_{0}\sqrt{2\pi mk_{B}T}}. \tag{3}
$$

The initial sticking coefficient when $\theta_{\text{CO}}=0$ is taken to be unity. Thus by assuming equilibrium of CO between gas phase and the chemisorption phase, one can calculate the adsorption isobar of the lattice gas model using either the transfer matrix or the Monte Carlo method.

The results are shown in Fig. 6. For low pressures, as $T$ decreases, $\theta_{\text{CO}}$ first increases, then reach a plateau at $\theta_{\text{CO}}$ $=0.5$. For $p_{\text{CO}}=10^{-7}$ Torr, the plateau occurs near $T$ $=420$ K. This result is in very good agreement with experiments.$^{3,21}$ Specifically, the inflection point around 420 K in the work function measurement by Behm *et al.* Fig. 13 of Ref. 3 for pressure around $10^{-7}$ Torr is reproduced, with-

![](./images/812341924705861632_8.jpg)

FIG. 6. Adsorption isobars calculated from the lattice-gas model.

out assuming any particular work function-coverage dependence near $\theta_{\mathrm{CO}} \approx 0.5$. Upon a further decrease in temperature, $\theta_{\mathrm{CO}}$ again increases above 0.5 ML. Experimentally, this corresponds to the adlayer moving into the regime of the commensurate-incommensurate transition discussed in Sec. IV. Here, we simply note that the temperature where this occurs depends sensitively on the value of the 2NN interactions $\omega_{2}$. By choosing $\omega_{2}=0.17 \mathrm{eV}$, the transition occurs between $340 \mathrm{~K}$ to $400 \mathrm{~K}$ for $p_{\mathrm{CO}}$ between $10^{-9}$ to $10^{-7}$ Torr, in agreement with experiments. $^{19,21}$ It is also significant that at high pressures, the LG model predicts disappearance of the plateau near $\theta_{\mathrm{CO}}=0.5$, as observed experimentally. $^{21}$

Note that we "naively" choose $\nu_{0}=10^{13} \mathrm{~s}^{-1}$ for the desorption prefactor, while Behm et al. obtain a value on the order of $10^{16} \mathrm{~s}^{-1}$ from their adsorption isobars. Consequently there is some discrepancy between the lattice-gas model prediction and experiments at low coverages. Specifically for $\theta_{\mathrm{CO}}<0.5 \mathrm{ML}$, desorption occurs at a higher temperature than experiments. The discrepancy is not likely to be resolved by modification of interactions, since at low coverages repulsive lateral interactions are not significantly strong enough to affect desorption.

### VII. SUMMARY

We have performed a combined transfer matrix and Monte Carlo study of a lattice-gas model for CO adlayers on Pd(100). Model predictions are compared against a variety of experimental observations. Of particular significance is our determination of repulsive adspecies interactions: $\omega_{1}=\infty$, $\omega_{2}=0.17 \mathrm{eV}$, and $\omega_{3}=0.03 \mathrm{eV}$. Our assignment of a weak 3NN interaction is consistent with early qualitative arguments by Behm et al. $^{3}$ We use a binding energy of $\epsilon_{b}$ $=1.60 \mathrm{eV}$ in analysis of the heat of adsorption and the desorption isobars to be consistent with experimental estimates. These values deviate significantly from DFT-GGA calculations with the PW91 functional. Both the binding energy ${ }^{5,11}$ $(\epsilon_{b}=1.92-1.98 \mathrm{eV})$ and the values of lateral interactions $^{6}$ $(\omega_{2}=0.305 \mathrm{eV}$ and $\omega_{3}=0.155 \mathrm{eV})$ are far too large to be consistent with experimental observation. Using the more recently available RPBE functional $^{11}$ seems to give more accurate results for chemisorption on transition metals, including the binding energy of $\mathrm{CO} / \mathrm{Pd}(100)$ ( $\epsilon_{b}=1.50 \mathrm{eV}$ ). However, to obtain energetics accurate enough to describe adlayer ordering is still very demanding of DFT calculations.

![](./images/812341924705861632_9.jpg)

FIG. 7. Coverage-temperature phase diagram of the lattice-gas model with NN and second NN exclusion and third NN repulsion. Symbols are obtained from Monte Carlo simulations. "D," "[5]," "[2]," and "S" represent the disordered, $(\sqrt{5} \times \sqrt{5}) R 26.6^{\circ}, c(4 \times 2)$, and the semiordered phases, respectively. Note that the coverage is in term of the bridge sites lattice, which is half of the value using the substrate lattice.

### ACKNOWLEDGMENTS

The author thanks Professor T. L. Einstein and Professor P. A. Thiel for helpful discussions, and Professor J. W. Evans for extensive discussion and suggestions. This work was supported by the Division of Chemical Sciences, U.S. Department of Energy (USDOE). It was performed at Ames Laboratory which is operated for the USDOE by Iowa State University under Contract No. W-7405-Eng-82.

### APPENDIX: PHASE DIAGRAMS OF THE LATTICE-GAS MODEL WITH NN AND SECOND NN EXCLUSION AND THIRD NN REPULSION ON A SQUARE LATTICE

In Sec. III we study the phase diagram of a two-dimensional lattice gas model with nearest- and second-nearest exclusion, and a finite third-nearest-neighbor repulsion. There we focus on the transitions between the disordered and fully-ordered phases that are most relevant to CO adsorbed on Pd(100) surfaces. However, more complex structures and transitions exists for this simple LG model.

As mentioned in Sec. III, there are two fully-ordered phases, $c(2 \sqrt{2} \times \sqrt{2}) R 45^{\circ}$ and $(\sqrt{5 / 2} \times \sqrt{5 / 2}) R 18.4^{\circ}$, and a semiordered phase. For statistical studies, it is more common to use the lattice of bridge sites, and rotate it by $45^{\circ}$, so that it becomes a square lattice with twice the density of lattice sites as the underlying Pd(100) surface atoms. Then the two ordered phases become $c(4 \times 2)$ and $(\sqrt{5} \times \sqrt{5}) R 26.6^{\circ}$. This simpler notation is used exclusively below. The semiordered phase is sometimes referred to as a $(2 \times 1)$ phase $^{24}$ or the degenerate phase. $^{16}$

The two transition lines between the disordered phase and the two fully ordered phases must be first-order according to Landau and Lifshitz's theory of phase transitions adapted to two-dimensional systems. $^{25}$ Figure 7 is the coverage-temperature phase diagram of the model. Note that the coexistence of the disordered and the $c(4 \times 2)$ phases does not extend to $\omega_{3}=0$. For $\beta \omega_{3}<0.2$, as $\mu$ increases, the system changes from the disordered phase first to the semiorder phase, then to the $c(4 \times 2)$ phase. The transfer matrix finite-size-scaling study of Kinzel and Schick $^{24}$ for the model with NN exclusion and 2NN repulsion can be of relevance

here. They argue that the transition from the disordered phase to the semiordered [the $(2\times1)$ phase in their terminology] is continuous and nonuniversal. The semiordered phase as an intermediate phase between the disordered and the $c(4\times2)$ phases is also reported for an anisotropic model. $^{16}$

The transition from the semiordered to the $c(4\times2)$ phase should also be continuous. Near the transition, MC simulations show domain walls separating different $c(4$ $\times2)$ ordered regions. With large $\mu$, where domain walls are more well-defined, we observe that the domain wall energy is simply $\omega_{3}$, while the energy cost for wanderings of domain walls is $\mu/2$ per kink, representing loss of half an allowed site by having a kink. The fermion approximation for domain walls $^{26}$ predicts that the transition line is given by $\beta\omega_{3}=2\exp[-\beta\mu/2]$. MC simulations lend some supports for this conjecture, although uncertainties are quite large.

Note that the meeting point of the postulated transition line to the disordered-ordered transition line $(\beta\mu,\beta\omega_{3})$ $=(5.1,\ 0.2)$ is very close to the point where the first-order nature of the order-disorder transition becomes apparent from MC simulations. Using systems of size up to 128 $\times128$, double-well distributions in particle density in grand canonical ensemble simulations emerges with $\beta\omega_{3}\gtrsim0.2$. It seems reasonable to identify this point as a tricritical point where the order-disorder transition changes from second order to first order. It is also perhaps a Lifshitz point, where the disordered, fully ordered, and modulated-ordered phases are indistinguishable. $^{27}$ However, without a systematic finite-size analysis, which is beyond the scope of this paper, one can not be certain of the above classification.

The $(\sqrt{5}\times\sqrt{5})R26.6^{\circ}$ phase exists for $\omega_{3}>0.19k_{B}T$. For $\omega_{3}$ larger than this value, as $\mu$ and $\rho$ increases, the system first changes from the disordered phase to the $(\sqrt{5}$ $\times\sqrt{5})R26.6^{\circ}$ phase, then to the $c(4\times2)$ phase at higher $\mu$ or $\rho$. There is a narrow region of disordered phase between these two ordered phase. The region gets narrower as $\omega_{3}$ increases, though it is not clear whether it vanishes at a finite $\omega_{3}$ or persists as $\omega_{3}\rightarrow\infty$. Note that the two transitions lines in Fig. 2 are obtained from transfer matrix calculation by finding maxima in $d\rho/d\mu$ using strip size $N=10$. The size is perhaps too small for reliable estimate of phase transitions between such complex phases. Monte Carlo simulations using either Glauber or Kawasaki dynamics are also too inefficient in this regime (high density and strong repulsion) to give reliable estimates. An interesting feature found from Monte Carlo simulations is that as $\rho$ increases above 0.2, domains walls with $c(4\times2)$ characteristic emerges and gradually take over as $\rho$ approaches 0.25.

$^{1}$J. C. Tracy and P. W. Palmberg, J. Chem. Phys. 51, 4852 (1969).
$^{2}$A. M. Bradshaw and F. M. Hoffmann, Surf. Sci. 72, 513 (1978).
$^{3}$R. J. Behm, K. Christmann, G. Ertl, and M. A. Van Hove, J. Chem. Phys. 73, 2984 (1980).
$^{4}$J. Szanyi, W. K. Kuhn, and D. W. Goodman, J. Vac. Sci. Technol. A 11, 1969 (1993).
$^{5}$A. Eichler and J. Hafner, Phys. Rev. B 57, 10110 (1998).
$^{6}$M. W. Wu and H. Metiu, J. Chem. Phys. 113, 1177 (2000).
$^{7}$J. Wintterlin, S. Völkening, T. V. W. Janssens, T. Zambelli, and G. Ertl, Science 278, 1931 (1997).
$^{8}$D.-J. Liu and J. W. Evans (unpublished).
$^{9}$Y. Y. Yeo, L. Vattuone, and D. A. King, J. Chem. Phys. 106, 1990 (1997).
$^{10}$A. Ortega, F. M. Hoffmann, and A. M. Bradshaw, Surf. Sci. 119, 79 (1982).
$^{11}$B. Hammer, L. B. Hansen, and J. K. Nørskov, Phys. Rev. B 59, 7413 (1999).
$^{12}$C. C. A. Günther, P. A. Rikvold, and M. A. Novotny, Phys. Rev. B 42, 10738 (1990).
$^{13}$F. H. Ree and D. A. Chestnut, Phys. Rev. Lett. 18, 5 (1967).
$^{14}$L. Lafuente and J. A. Cuesta, J. Chem. Phys. 119, 10832 (2003).
$^{15}$A. Bellemans and R. K. Nigam, Phys. Rev. Lett. 16, 1038 (1966).
$^{16}$F. Buda, G. M. Florio, and P. V. Giaquinta, Phys. Rev. B 35, 2021 (1987).
$^{17}$P. Uvdal, P.-A. Karlsson, C. Nyberg, S. Andersson, and N. V. Richardson, Surf. Sci. 202, 167 (1988).
$^{18}$W. Berndt and A. M. Bradshaw, Surf. Sci. Lett. 279, L165 (1992).
$^{19}$R. Schuster, I. K. Robinson, K. Kuhnke, S. Ferrer, J. Alvarez, and K. Kern, Phys. Rev. B 54, 17097 (1996).
$^{20}$S. S. Rao and S. M. Bhattacharjee, Phys. A 45, 670 (1992).
$^{21}$J. Szanyi and D. Goodman, J. Phys. Chem. 98, 2972 (1994).
$^{22}$C. Stampfl, H. J. Kreuzer, S. H. Payne, H. Pfnür, and M. Scheffler, Phys. Rev. Lett. 83, 2993 (1999).
$^{23}$X. Guo and J. T. Yates, Jr., J. Chem. Phys. 90, 6761 (1989).
$^{24}$W. Kinzel and M. Schick, Phys. Rev. B 24, 324 (1981).
$^{25}$E. Domany, M. Schick, J. S. Walker, and Griffiths, Phys. Rev. B 18, 2209 (1978).
$^{26}$J. Villain, in *Ordering in Strongly Fluctuating Condensed Matter System*, edited by T. Riste (Plenum, New York, 1980), pp. 221–260.
$^{27}$R. M. Hornreich, M. Luban, and S. Shtrikman, Phys. Rev. Lett. 35, 1678 (1975).