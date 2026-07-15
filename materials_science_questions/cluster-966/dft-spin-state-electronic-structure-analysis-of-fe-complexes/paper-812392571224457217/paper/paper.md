# Modelling spin-forbidden reactions: recombination of carbon monoxide with iron tetracarbonyl

Jeremy N. Harvey*$^{a}$ and Massimiliano Aschi$^{b}$

$^{a}$ School of Chemistry, University of Bristol, Cantock's Close, Bristol, UK BS8 1TS.
E-mail: jeremy.harvey@bris.ac.uk
$^{b}$ Dipartimento di Chimica, Ingegneria Chimica e Materiali, Universita' di l'Aquila, Via Vetoio (Coppito 1), I-67010 l'Aquila, Italy

Received 28th November 2002, Accepted 29th November 2002
First published as an Advance Article on the web 25th April 2003

New density functional theory and *ab initio* computations on the $[Fe(CO)_5]$ system are reported. Careful exploration of basis set and correlation effects leads to "best" values for the difference in energy $\Delta E(1,3)$ between ground state $^3[Fe(CO)_4]$ and the singlet excited state of *ca.* 8 kcal mol$^{-1}$, and for the bond dissociation energy BDE(3) of $[Fe(CO)_5]$ with respect to ground state fragments $^3[Fe(CO)_4] + CO$ of *ca.* 40 kcal mol$^{-1}$. A modified form of the B3PW91 functional is used to explore the potential energy surface for the spin-forbidden recombination reaction of CO with $^3[Fe(CO)_4]$. A $C_s$-symmetric minimum energy crossing point (MECP) between the reactant (triplet) and product (singlet) potential energy surfaces is found, lying 0.43 kcal mol$^{-1}$ above the reactants. The rate coefficient for recombination is computed using a non-adiabatic form of transition state theory, in which the MECP is treated as the critical point in the reaction. Semi-quantitative agreement with experiment is obtained: the predicted rate coefficient, $8.8 \times 10^{-15}$ cm$^3$ molecule$^{-1}$ s$^{-1}$, is only six times smaller than the experimental rate. This is the first computation from first principles of a rate coefficient for a spin-forbidden reaction of a transition metal compound.

## Introduction

As well as the many synthetic applications of $[Fe(CO)_5]$ as a (very) fundamental building block for organometallic compounds of iron, it has been the subject of a great many investigations using the methods of physical chemistry and of physical organometallic chemistry, aimed at understanding the fundamental aspects of its chemistry.$^{1,2}$ This is no doubt in part due to its modest size, ready availability and significant vapour pressure. Another factor is surely that for such a small molecule, its chemistry encompasses a surprisingly broad range of principles and reaction types. For example, the reaction which forms the topic of the present paper, *i.e.* gas-phase recombination of CO with the $[Fe(CO)_4]$ fragment to regenerate iron pentacarbonyl, is in many respects an archetypal ligand addition reaction to an unsaturated species. Therefore, the theoretical study in this paper should be of broader interest to computational and experimental transition metal chemists.

Our particular focus of interest here is a set of experiments carried out in the Weitz group.$^{3,4}$ In this work, $[Fe(CO)_5]$ or some other stable organometallic is photodissociated in a flow tube using UV light, and the time-evolution of the fragments is monitored by transient infrared spectroscopy. In the presence of ligands such as CO, N$_2$ or C$_2$H$_4$ in the backing gas, these can then react with fragments such as $[Fe(CO)_4]$ to generate the corresponding saturated species. Many recombination

DOI: 10.1039/b211871h
Faraday Discuss., 2003, 124, 129-143

This journal is © The Royal Society of Chemistry 2003

View Online

reactions of simple ligands with unsaturated metal fragments involve purely attractive potential energy surfaces and thereby proceed essentially at the gas-collision rate. Reaction (1) is an example of such a very fast recombination process whose rate has been measured by Weitz et al.³ The homologous reaction (2) is very different, as it occurs roughly 400 times slower than (1). The authors explained this observation based on the spin-conserving nature of these two reactions. It is well established, both from computation (see below) and experiment that the unsaturated [Fe(CO)₃] and [Fe(CO)₄] species have spin triplet ground states. Reaction (1) is thereby spin-allowed. [Fe(CO)₅], which has 18 electrons, is of course a singlet. Therefore, reaction (2) is spin-forbidden, and this may account for its slow rate. Similar slow rates have been observed for related spin-forbidden reactions.⁴

$$[\mathrm{Fe(CO)_3}] + \mathrm{CO} \rightarrow [\mathrm{Fe(CO)_4}] \quad k = 2.2 \times 10^{-11} \ \mathrm{cm^3 \ s^{-1} \ molecule^{-1}} \tag{1}$$

$$[\mathrm{Fe(CO)_4}] + \mathrm{CO} \rightarrow [\mathrm{Fe(CO)_5}] \quad k = 5.2 \times 10^{-14} \ \mathrm{cm^3 \ s^{-1} \ molecule^{-1}} \tag{2}$$

There have been a large number of computational and theoretical papers concerning the chemistry of [Fe(CO)₅]. The bond energies have been addressed by various groups, using ab initio⁵ and density functional methods.⁶ Potential energy curves relevant to the photodissociation of [Fe(CO)₅] have also been computed,⁷ and several studies have attempted to account for some of the reactivity issues discussed here.²ᶜ,⁶ᶜ,ᵈ However, these have not been able to provide quantitative insight into reaction rates, which is the aim of the present study. Also, some of the computed properties vary considerably from one level of theory to another, and the lack of accurate experimental data means that there are still considerable uncertainties about the correct value of these observables, in particular the singlet/triplet energy splitting and the bond energy.

The spin-forbidden character of recombination reaction (2) makes its computational study highly challenging. In the limit of very strong spin-orbit coupling, spin-forbidden reactions are in principle no more complex than other reactions: As the system evolves from reactant to product, coupling between the different spin states will lead to the overall wavefunction smoothly changing its spin character, from being *e.g.* mainly "triplet" in nature to mainly "singlet". However, even in such cases, the computational challenge is severe, as most electronic structure codes do not include the spin-orbit coupling part of the Hamiltonian, so that only pure spin states can be addressed, and the correct *adiabatic* potential energy surfaces can therefore not be readily obtained.

In fact, as we shall see below, the [Fe(CO)₄,CO] system is not at the strong coupling limit, so that this system is inherently *non-adiabatic*. This means that dynamics will tend to evolve mainly on zeroth-order potential energy surfaces, of defined spin, with transfer between surfaces occurring, with a probability dependent on the strength of spin-orbit coupling, in the regions where these *diabatic* surfaces cross or at least lie very close in energy. Although this makes the treatment of the dynamics more complex, it does mean that traditional computational methods can be used to compute the energy of the different electronic states. It is however necessary to locate the important regions of the potential energy surfaces where the relevant spin states lie close in energy. In most cases, these surfaces actually cross, and the problem is reduced to finding the crossing points. One approach for finding such points treats the system in a pseudo-one-dimensional way, in which each surface is mapped out for several values of a given reaction coordinate, usually a bond length or angle. The crossing point between the resulting one-dimensional curves is a rough approximation to the lowest energy crossing point between the surfaces. However, it is usually more accurate, and faster, to use a gradient-based method to explicitly locate the exact minimum energy crossing point (MECP) between the surfaces. Several algorithms to do this have been proposed in the literature.⁸,⁹ We¹⁰ and others¹¹ have shown how the energy and geometry of MECPs (or more generally of crossing points) can be used to provide a qualitative estimate of the rate of spin-forbidden reactions. Most relevant to the present work, we have carried out a number of studies of spin-forbidden processes in transition metal chemistry, including both organometallic¹² and bioinorganic¹³ reactions.¹⁴,¹⁵

For more precise estimates of rate coefficients, one must either resort to non-adiabatic dynamical studies, or to non-adiabatic statistical rate theories. The latter basically involve using a multi-plicative "transmission factor", related to the spin-orbit coupling strength, to correct the rate computed using standard transition state theory, treating, where appropriate, the MECP like the

130
Faraday Discuss., 2003, 124, 129–143

View Online
transition state of adiabatic statistical methods. Such methods have already been applied to a number of small gas-phase reactions, $^{16-18}$ but not, at least as far as we are aware, to transition metal chemistry.

In the present study, we aim to calculate the rate coefficient for addition of CO to triplet $[Fe(CO)_{4}]$ using non-adiabatic transition state theory (NA-TST). We will start by presenting the NA-TST method used here, which is based on the unimolecular method of ref. 16, as already used by us in conjunction with MECPs. $^{18}$ We will also explain how the different pieces of input needed for this study, in particular the properties of the MECP, can be derived from computation. Then, we will present the technical computational details relating to our calculations. As usual when applying statistical rate theories, it is extremely important to obtain accurate estimates of the barrier height, here the energy of the MECP. As mentioned above, the correct splitting between singlet and triplet states and the bond energy are not very well known. Accordingly, we have carried out a large number of computations aimed at elucidating these questions, as well as characterising the reactants and MECP, and we will next present these results. Finally, we shall present our computed rates for the title reaction, compare these to experiment, and discuss the implications for other spin-forbidden reactions.

## Non-adiabatic transition state theory (NA-TST)
The reaction of interest in the present study is in some respects of the most simple type possible for a spin-forbidden bimolecular reaction, as illustrated by the schematic potential energy surfaces of Fig. 1. There is only one step, corresponding to the spin-crossing or MECP. The addition is suf- ficiently exothermic, the size of the molecule large enough, and the pressure of the experiments to be modelled $^{3}$ high enough that only the forward reaction needs to be taken into account, with collisional cooling certain to occur faster than reverse dissociation. Also, there are no intermediate species involved. Singlet $[Fe(CO)_{4}]$ lies too high in energy to play a significant role in the kinetics at room temperature. Finally, the seam of crossing around the MECP, even though the latter is low- lying (see below), is certain to represent a clear dividing surface between reactant and product configurations so that variational effects are not expected to be important.

For all these reasons, the rate coefficient can be written in the following relatively simple way:

$$
k(T)=\frac{1}{h Q_{\mathrm{R}}(T)} \int_{0}^{\infty} N_{\mathrm{MECP}}(E) \mathrm{e}^{-E / k_{\mathrm{B}} T} \mathrm{~d} E
$$

In this equation, $h$ is Planck's constant, $Q_{\mathrm{R}}(T)$ is the reactant partition function, including electronic, vibrational and rotational degrees of freedom for both reactants $^{3}[Fe(CO)_{4}]$ and $CO$ , as well as the relative translational motion. $N_{MECP}(E)$ is an effective number of states (or integrated

![](./images/812392571224457217_1.jpg)

Fig. 1 Schematic potential energy surfaces for the $[Fe(CO)_{5}]$ system.

Faraday Discuss., 2003, 124, 129-143

View Online

density of states) at the MECP for a given energy $E$ relative to the zero-point level of the reactants, and $k_{\mathrm{B}}$ is Boltzmann's constant. This equation is identical to that used in normal transition state theory, except concerning the expression used for the number of states, which is given here as:

$$
N_{\mathrm{MECP}}(E)=\int_{0}^{E} \rho^{\mathrm{MECP}}\left(E-E_{\mathrm{H}}\right) p_{\mathrm{SH}}\left(E_{\mathrm{H}}\right) \mathrm{d} E_{\mathrm{H}}
$$

As can be seen, this equation involves a second integration, over $E_{\mathrm{H}}$, which is the part of the total energy $E$ which is in the coordinate orthogonal to the seam of crossing between the two surfaces. For each value of this energy, the contribution to the integrated sum of states $N_{\mathrm{MECP}}(E)$ is obtained as a product of the density of states within the crossing seam $\rho^{\mathrm{MECP}}(E-E_{\mathrm{H}})$, and a probability for hopping from one surface to the other, $p_{\mathrm{SH}}(E_{\mathrm{H}})$. The first of these terms is similar to the traditional density of states term used within the dividing surface around a saddle-point: the crossing seam defines a sub-space within which the available energy $E-E_{\mathrm{H}}$ may be distributed in many different ways amongst the rotational and vibrational degrees of freedom. The term $p_{\mathrm{SH}}$ corresponds in fact to the sum of the probabilities for hopping from one surface to another upon approaching the seam from below, and of that for hopping upon recrossing the seam in the other direction. To a first approximation, this term depends only on $E_{\mathrm{H}}$, and can be calculated in a pseudo-one-dimensional way using either Landau-Zener theory or from WKB theory (using an expression given by Delos and Thorson).$^{16,19}$

The general Landau-Zener surface-hopping probability is given by:

$$
p_{\mathrm{SH}}^{\mathrm{Landau-Zener}}\left(E_{\mathrm{H}}\right)=(1+P)(1-P)
$$

$$
P=\exp\left(\frac{-2 \pi V_{12}^{2}}{h \Delta F} \sqrt{\frac{\mu_{\mathrm{H}}}{2\left(E-E_{\mathrm{MECP}}\right)}}\right)
$$

where $(1-P)$ is the probability of hopping on the first passage, and $P(1-P)$ the probability for (a) not hopping on first crossing the seam, then (b) hopping upon crossing it again in the reverse direction, and their sum gives $p_{\mathrm{SH}}$. In this expression, $V_{12}$ is the electronic matrix element for coupling between the two surfaces (which is due to spin-orbit coupling in our case), $\mu_{\mathrm{H}}$ is the reduced mass for movement along the direction orthogonal to the crossing seam, and $\Delta F$ is the norm of the difference of the gradients on the two surfaces. Note that in the common case of small spin-orbit coupling, this expression reduces to:

$$
p_{\mathrm{SH}}^{\mathrm{Landau-Zener}}\left(E_{\mathrm{H}}\right) \approx \frac{4 \pi V_{12}^{2}}{h \Delta F} \sqrt{\frac{\mu_{\mathrm{H}}}{2\left(E-E_{\mathrm{MECP}}\right)}}
$$

which is essentially the equation given in ref. 18. Note that for energies below or exactly equal to that of the crossing point, this expression is not defined, and the probability is instead zero.

The alternative expression for the hopping probability, based on WKB theory, is:

$$
p_{\mathrm{SH}}^{\mathrm{Delos}}\left(E-E_{\mathrm{MECP}}\right)=4 \pi^{2} V_{12}^{2}\left(\frac{2 \mu_{\mathrm{H}}}{\hbar^{2} F \Delta F}\right)^{2 / 3} A i^{2}\left[\left(E-E_{\mathrm{MECP}}\right)\left(\frac{2 \mu_{\mathrm{H}} \Delta F^{2}}{\hbar^{2} F^{4}}\right)^{1 / 3}\right]
$$

In this equation, $\hbar$ is Planck's constant divided by $2 \pi$, and $F$ is the geometric mean of the norms of the gradients on the two surfaces at the crossing point. $Ai$ denotes the Airy function. The advantage of this second expression is that it is not equal to zero for $E$ below the crossing point, although it does decrease rapidly in this regime. This allows for tunnelling from one surface to the other below the crossing point.

The data needed to apply this theory are a set of properties of the two reactants and of the MECP. For the reactants, all that is needed is the geometry (and hence the rotational constants) and vibrational frequencies of $\mathrm{CO}$ and ${ }^{3}\left[\mathrm{Fe}(\mathrm{CO})_{4}\right]$. For the MECP, one needs its energy relative to the reactants, its geometry, the vibrational frequencies within the seam of crossing needed to compute $\rho^{\mathrm{MECP}}(E)$, the reduced mass along the reaction coordinate, the norm of the difference in gradients on the two surfaces, and their geometric mean, as well as the root mean square spin-orbit coupling matrix element $V_{12}$ between the singlet and triplet wavefunctions. These properties will be

132
Faraday Discuss., 2003, 124, 129-143

View Online

calculated at the levels of theory described below. The methods needed to locate and characterize the MECP have been described before. $^{9,18,20}$ Briefly, a script program has been developed which: (a) generates suitable input files for an electronic structure code; (b) calls the code; (c) extracts from the output the energies and gradients on the two surfaces; (d) combines these to yield an effective gradient which is directed towards the MECP; (e) uses this to update the geometry until con- vergence to the MECP is reached.

## Computational details

The bulk of the density functional theory computations have been carried out using the Gaussian program, $^{21}$ with a flexible, triple-zeta basis set. Specifically, the all-electron basis sets of Ahlrichs et $a l.^{22}$ are used, as implemented in Gaussian. These are segmented contractions of the form (17s9p6d)/[6s3p3d] for Fe and (11s6p)/[5s3p] for C and O. A set of two diffuse, uncontracted 4p- like functions $^{23}$ was added to the Fe basis $(\alpha=0.134915$ and 0.041843), as well as one f polar isation function $(\alpha=1.0)$ on iron, and one d function each on C and O $(\alpha=0.8$ and 1.2, respectively). Test calculations using larger basis sets (e.g. "VQZ-VTZ" below) led to very similar results, so we assume the present basis to be more or less converged in size for DFT computations. Where required, this basis is simply referred to as "TZV". Full geometry optimisation was carried out for all species. Some DFT computations were also carried out using the MOLPRO 2002.3 code, $^{24}$ with the same TZV basis.

All ab initio computations were carried out using MOLPRO 2002.3 using a variety of methods and basis sets. MCSCF and internally-contracted multi-reference perturbation theory $^{25}$ (CASPT2 for short) calculations were carried out using a variety of active spaces, as discussed in the text. The MCSCF calculations included all configurations for the chosen active space and wavefunction symmetry (CASSCF computations). For the CASPT2 calculations, typically only the configura- tions with a weight in the CASSCF wavefunction exceeding a certain threshold (0.001 to 0.01) wereincluded in the reference wavefunction. In all cases, these configurations made up more than $99.9 \%$  of the CASSCF wavefunction by weight, and convergence tests were carried out to make sure the threshold was small enough. To compute bond energies, single-reference MP2 energies for CO were used in conjunction with CASPT2 energies for $[Fe(CO)_{4}]$ and $[Fe(CO)_{5}]$ (see discussion below). Also in the CASPT2 calculations, a level shift, typically of 0.3 au, was applied to the virtual orbitals so as to avoid "intruder" state problems. $^{26}$ In the absence of the level shift, catastrophic con vergence problems were sometimes observed. Single-reference CCSD and CCSD(T) computations were also carried out. $^{27}$ As discussed in the text, it was found that using density functional theory "orbitals" to expand the CCSD wavefunction led to improved performance in some cases. In all correlated calculations, the core Fe (1s2s2p3s3p) and C and O (1s) orbitals were held frozen.

The basis sets used for these ab initio computations covered a broad range of sizes. We will refer to these basis sets using labels such as "double-zeta" (DZ) which loosely describe their size. In detail, the "DZ" basis used the same basis from ref. 22 on the Fe atom, without additional p or f functions, and the cc-pVDZ basis of Dunning $^{28}$ on C and O, but without the d polarisation functions. The "VDZ" basis adds the two diffuse p functions and the f function mentioned above on Fe, and uses the full cc-pVDZ basis on C and O. The "VTZ-VDZ" basis adds an extra d function $(\alpha=0.134915)$ on Fe, and replaces the single f function with a [2f1g] set $(\alpha_{f}=3.265953$ ,0.786787, ag = 2.248) taken from the VTZ correlation-consistent iron basis sets of Ricca and Bauschlicher. $^{29}$ The "VQZ-VDZ" basis expands this basis set by uncontracting the most diffuse primitive d function in the contraction scheme, replacing the diffuse $\alpha=0.134915 d$ function by a set of two $(\alpha=0.12,0.05)$ , and using a larger [3f2g1h] polarisation set $(\alpha_{f}=5.138777,1.51900$ ,0.44901, ag = 3.705809, 1.011411, an = 2.48) also taken from ref. 29. This leads to a final basis of(17s12p8d3f2g1h)/[6s5p6d3f2g1h] size. Finally, the "VTZ" and "VQZ-VTZ" bases use the same Fe bases as the VTZ-VDZ and VQZ-VDZ sets, but with the larger cc-pVTZ basis $^{28}$ on C and O. To test for possible relativistic effects, some CCSD(T) calculations were repeated using relativistic(Douglas-Kroll) one-electron integrals, $^{30}$ as implemented in MOLPRO. Negligible changes in relative energetics were obtained.

For the NA-TST computations, MECPs were optimised using the code developed by one ofus, $^{9,18,20}$ and the frequencies within the seam of crossing were also computed as described. $^{9,18}$

Faraday Discuss., 2003, 124, 129-143

View Online

Vibrational densities of state within the harmonic approximation were computed using the steepest descent method.³¹ The spin–orbit coupling between singlet and triplet states was computed at the geometry of the ³[Fe(CO)₄] minimum, and at the geometry of the MECP determined at the B3PW91/TZV level, using the full Breit–Pauli Hamiltonian, as implemented in MOLPRO,³² using state-averaged CASSCF wavefunctions, and the large, 12 electrons in 12 orbitals active space described below. The basis set used was a variation on the VDZ basis described above: The Fe basis was the same, but the cc-pVDZ basis, whose general contraction pattern cannot be treated by the spin–orbit integral routine, was replaced by the double-zeta basis of ref. 22 for C and O, with one d function in each case ($\alpha_{\rm C}=0.55$, $\alpha_{\rm O}=1.185$).

## Results: DFT and *ab initio* calculations

In previous studies of spin-forbidden reactions of transition metal compounds, we have used standard density functional theory,³³ *e.g.* using the well established hybrid B3LYP functional, to compute the necessary points on the potential energy surfaces.¹²⁻¹⁴ Based on this and other previous experience, this functional should yield reasonable, qualitatively accurate potential energy surfaces. It is well known, however, that rate calculations require very accurate potential energy surfaces, as properties such as the barrier height have a very large influence on computed rate coefficients. In the present case, we are attempting to reproduce a difference between rate coefficients of roughly 500: this corresponds to an approximate difference in barrier heights of less than 4 kcal mol⁻¹, so our results need to be significantly more accurate than this, at least for the barrier height. As can be seen from Fig. 1, this also requires the computed singlet–triplet energy separation $\Delta E(1,3)$ to be well reproduced.

To test whether DFT was capable of providing this level of accuracy for the present system, we first of all computed the key energetics using a variety of different functionals. This often provides a useful informal check as to the overall accuracy of DFT approaches:³³ when large differences are observed between functionals, great care should be taken to ascertain which is most reliable. Our DFT results for the [Fe,(CO)₅] system are summarised in Table 1.

It is to be noted first of all that the computed *geometries* for the different species are found to be very similar with all the functionals. [Fe(CO)₅] has a $D_{3\text{h}}$ trigonal bipyramid structure with two axial and three equatorial ligands. Both singlet and triplet [Fe(CO)₄] have $C_{2\text{v}}$ minima, which are best described as truncated forms of the parent pentacarbonyl species, in which one of the equatorial ligands has been removed, and some relaxation of the axial ligands towards the vacant site

<table>
<caption>Table 1 Computed energetics of the [Fe(CO)₅] system (in kcal mol⁻¹) using a variety of different functionals, and the TZV basis. $\Delta E(1,3)$, BDE(3) and BDE(1) are defined in the text. All results include a correction for zero-point energy computed at the B3PW91* level. For each functional, the corresponding percentage of “exact” exchange is indicated in brackets</caption>
<thead>
<tr>
<th>Functional</th>
<th>$\Delta E(1,3)$</th>
<th>BDE(3)</th>
<th>BDE(1)</th>
<th>$E_{\rm rel}$ MECP</th>
</tr>
</thead>
<tbody>
<tr>
<td>LDA (0%)</td>
<td>−5.91</td>
<td>68.26</td>
<td>62.35</td>
<td>—</td>
</tr>
<tr>
<td>BP86 (0%)</td>
<td>0.92</td>
<td>42.94</td>
<td>43.86</td>
<td>—</td>
</tr>
<tr>
<td>BLYP (0%)</td>
<td>1.43</td>
<td>34.23</td>
<td>35.66</td>
<td>1.30</td>
</tr>
<tr>
<td>G96LYP (0%)</td>
<td>1.61</td>
<td>33.48</td>
<td>35.08</td>
<td></td>
</tr>
<tr>
<td>HCTH147 (0%)</td>
<td>0.43</td>
<td>37.32</td>
<td>37.75</td>
<td></td>
</tr>
<tr>
<td>BPW91 (0%)</td>
<td>1.64</td>
<td>41.03</td>
<td>42.67</td>
<td>—</td>
</tr>
<tr>
<td>B3LYP (20%)</td>
<td>9.78</td>
<td>25.91</td>
<td>35.70</td>
<td>3.69</td>
</tr>
<tr>
<td>B1LYP (25%)</td>
<td>12.92</td>
<td>21.03</td>
<td>33.95</td>
<td>—</td>
</tr>
<tr>
<td>mPW1PW91 (25%)</td>
<td>12.11</td>
<td>30.42</td>
<td>42.53</td>
<td>1.64</td>
</tr>
<tr>
<td>PBE0 (25%)</td>
<td>9.15</td>
<td>34.12</td>
<td>43.26</td>
<td>—</td>
</tr>
<tr>
<td>KMLYP (55%)</td>
<td>21.61</td>
<td>21.11</td>
<td>42.72</td>
<td>—</td>
</tr>
<tr>
<td>MPW1K (42%)</td>
<td>20.21</td>
<td>20.67</td>
<td>40.88</td>
<td>—</td>
</tr>
<tr>
<td>B3PW91 (20%)</td>
<td>9.65</td>
<td>31.64</td>
<td>41.30</td>
<td>2.17</td>
</tr>
<tr>
<td>B3PW91* (15%)</td>
<td>6.88</td>
<td>36.47</td>
<td>43.35</td>
<td>0.49</td>
</tr>
<tr>
<td>B3′′PW91** (10%)</td>
<td>4.09</td>
<td>41.53</td>
<td>45.62</td>
<td>—</td>
</tr>
</tbody>
</table>

Faraday Discuss., 2003, 124, 129–143

View Online

has occurred. The details of these geometries have been discussed exhaustively in previous studies. $^{5,6}$

Turning to the energies, the agreement between functionals is much less good. Thus, the pre- dicted $\Delta E(1,3)$ ranges from slightly negative values to as large as $20 kcal mol^{-1}$ . This too is in line with previous observations. $^{6}$ By and large, the results do all follow one general trend, whereby the splitting increases upon inclusion of gradient corrections and especially of "exact", Hartree-Fock exchange. Thus, the LDA gives a singlet ground state, whereas gradient-corrected "pure" density functionals such as the standard BP86 and BLYP, as well as the newer G96LYP $^{34}$ and HCTH147 $^{35}$ give very small state splittings. Standard hybrid functionals such as B3LYP and B3PW91, which are based on Becke's 3-parameter fit to the G2 set of compounds $^{36}$ (and include $20 \%$ exact exchange), or the newer, B1LYP, $^{37}$ mPW1PW91, $^{38}$ and PBE0 $^{39}$ functionals, where the proportion is slightly larger, at $25 \%$ , all give values of the order of $10 kcal mol^{-1}$ . Functionals such as KMLYP $^{40}$ or MPW1K, $^{41}$ which have been developed mainly so as to reproduce more accurately certain activation barriers for simple hydrogen abstraction reactions, include a very large amount of exact exchange, and yield very large $\Delta E(1,3)$ values. As will be discussed below, these are cer tainly incorrect, which confirms that functionals of this type, whilst valuable in the context for which they have been developed, are certainly not of general applicability.

The above observations are in fact not really new: previous calculations with the B3LYP functional give values very close to that in Table 1, and "pure" functionals have been found to give the same sort of small splitting obtained here. $^{6}$ The dependence on the amount of exact exchange has also been observed more generally for the splitting between high- and low-spin states of metal compounds. $^{42}$ In fact, Reiher et al. have found energy splittings to depend almost linearly on the proportion of exact exchange for a set of Fe(u) and other complexes, and they have found that a modified form of the B3LYP functional, with $15 \%$ exchange (instead of $20 \%$ ), often gives the best agreement with experiment for these and other compounds. $^{43}$ We have reproduced a similar result for the energy splitting between singlet and triplet $[Fe(CO)_{4}]$ , computed at the B3LYP optimised geometries, with modified forms of B3LYP with different values of the $c_{3}$ coefficient for admixture of "exact exchange". This splitting (uncorrected for ZPE, and with the version of B3LYP as installed in MOLPRO, which differs slightly from that installed in Gaussian) varies almost linearly from $-2.20 kcal mol^{-1}$ for $c_{3}=0.0$ to $7.44 kcal mol^{-1}$ for $c_{3}=0.20$ (i.e. the "normal" B3LYP functional) to $21.03 kcal mol^{-1}$ with $c_{3}=0.50$ . As explained further below, we believe that the modified B3PW91 functional, with $c_{3}=0.15$ as suggested by Reiher et al., $^{43}$ gives the "best" result, and this is also shown in Table 1. Following their notation, we refer to this as B3PW91*. Results for $c_{3}=0.10$ (B3PW91**) are also shown.

It is to be noted that the bond energies also vary significantly from one functional to another. We include in Table 1 dissociation energies referenced not only to the triplet ground state (which we call BDE(3)), but also those (BDE(1)) referenced to the excited singlet fragment, which has an electronic structure more similar to that of the $[Fe(CO)_{5}]$ molecule. The latter "intrinsic" bond energies vary less strongly than the former, as these in effect also depend indirectly on $\Delta E(1,3)$ . Nevertheless, the choice of the correlation functional, especially, does affect the computed BDE(1), with the LYP functional giving noticeably smaller values.

Clearly, a reliable set of calibration data is necessary. Unfortunately, there is not much experimental data for this system, and it is not very accurate. $\Delta E(1,3)$ is known to be positive, so that $[Fe(CO)_{4}]$ has a triplet ground state. $^{1}$ However, the fact that even rather weak ligands, such as methane and xenon, form singlet adducts which are stable at low temperature in matrices, suggests that the energy splitting between the two states cannot be very large. Concerning the bond energy, the most reliable determination $^{44}$ is fairly accurate, at $41 \pm 2 kcal mol^{-1}$ , but there is some uncertainty as to whether it refers to BDE(1) or to BDE(3). This point is discussed lower down.

Instead, then, we sought to calibrate our computations using traditional ab initio computations, using both single- and multi-reference methods. These results are summarised in Tables 2 and 3. In principle, multi-reference methods should be the most accurate, given the known tendency of transition metal compounds to display multi-configurational character, and so we therefore started with these methods. As always in such cases, the most difficult choice to make is that of the reference, multi-configurational, wavefunction, which most often means selection of an active space (AS). At first sight, the partly occupied d-orbital manifold might appear to be the most appropriate choice, which would lead to an eight electron, five orbital (8,5) AS. However, this neglects the most

Faraday Discuss., 2003, 124, 129-143

<table>
<caption>Table 2 CASPT2 computed energetics (in kcal mol⁻¹) for the [Fe(CO)₅] system. All computations were carried out at the B3LYP/TZV optimised geometries, and do not include a correction for ZPE</caption>
<thead>
<tr>
<th></th>
<th></th>
<th>DZ</th>
<th>VTZ</th>
<th>VTZ-VDZ</th>
<th>VTZ</th>
<th>VQZ-VDZ</th>
<th>VQZ-VTZ</th>
</tr>
</thead>
<tbody>
<tr>
<td>AS I</td>
<td>ΔE(1,3)</td>
<td>18.9</td>
<td>16.4</td>
<td>15.4</td>
<td>14.3</td>
<td>—</td>
<td>13.9</td>
</tr>
<tr>
<td></td>
<td>BDE (3)</td>
<td>31.0</td>
<td>37.7</td>
<td>39.4</td>
<td>39.5</td>
<td>—</td>
<td>—</td>
</tr>
<tr>
<td></td>
<td>BDE (1)</td>
<td>49.9</td>
<td>54.1</td>
<td>54.8</td>
<td>53.8</td>
<td>—</td>
<td></td>
</tr>
<tr>
<td>AS II</td>
<td>ΔE(1,3)</td>
<td>12.4</td>
<td>10.3</td>
<td>9.2</td>
<td>8.4</td>
<td>8.0</td>
<td>7.9</td>
</tr>
<tr>
<td></td>
<td>BDE (3)</td>
<td>36.2</td>
<td>43.3</td>
<td>45.1</td>
<td>45.0</td>
<td>47.6</td>
<td>45.5</td>
</tr>
<tr>
<td></td>
<td>BDE (1)</td>
<td>48.6</td>
<td>53.6</td>
<td>54.3</td>
<td>53.3</td>
<td>55.6</td>
<td>53.4</td>
</tr>
<tr>
<td>AS III</td>
<td>ΔE(1,3)</td>
<td>10.6</td>
<td>10.2</td>
<td>7.9</td>
<td>7.8</td>
<td>6.3</td>
<td>6.8</td>
</tr>
<tr>
<td></td>
<td>BDE (3)</td>
<td>25.2</td>
<td>33.6</td>
<td>50.6</td>
<td>36.1</td>
<td>59.8</td>
<td>43.2</td>
</tr>
<tr>
<td></td>
<td>BDE (1)</td>
<td>35.8</td>
<td>43.8</td>
<td>58.5</td>
<td>43.9</td>
<td>66.1</td>
<td>50.0</td>
</tr>
</tbody>
</table>

important source of static correlation in transition metal compounds: correlation of d-orbital electron pairs. This effect is due to the fact that in the absence of correlation the resulting overestimate of interelectronic repulsion leads to doubly occupied d orbitals having the "wrong" shape, which makes them inappropriate as reference orbitals for the ensuing PT2 treatment. Within a multi-reference framework, this effect can be largely treated by using a "double-shell" of d orbitals⁵ᵇ within the AS: the eight d electrons are now allowed to occupy 10 orbitals (8,10). The second set of orbitals, which are significantly if weakly occupied, are not "4d" orbitals (their radius is rather similar to that of the first set of d orbitals, but with an extra radial node), but serve to describe the radial correlation of the electron pair. This choice of AS, referred to as AS I in Table 2, leads to a large predicted singlet-triplet energy difference $\Delta E(1,3)$, rather similar to that obtained in previous ab initio studies.⁵ The value obtained is fairly stable from one basis to another, suggesting that basis set effects are not enormous in this system. The bond energies also are consistent. It is notable that the predicted $\Delta E(1,3)$ is larger than that obtained with almost all the DFTs, except those with the most exact exchange. This is unlike what has been found by Reiher et al.,⁴³ where the best agreement with experiment came from including less exact exchange than in functionals such as B3LYP.

<table>
<caption>Table 3 CCSD and CCSD(T) computed energetics (kcal mol⁻¹) for the [Fe(CO)₅] system, using various basis sets. All computations were carried out at the B3LYP/TZV optimised geometries, and do not include a correction for ZPE</caption>
<thead>
<tr>
<th></th>
<th></th>
<th>DZ</th>
<th>VDZ</th>
<th>VTZ-VDZ</th>
<th>VQZ-VDZ</th>
</tr>
</thead>
<tbody>
<tr>
<td>CCSD</td>
<td>ΔE(1,3)</td>
<td>12.9</td>
<td>13.1</td>
<td>12.1</td>
<td>10.9</td>
</tr>
<tr>
<td></td>
<td>BDE (3)</td>
<td>30.1</td>
<td>30.7</td>
<td>31.5</td>
<td>33.7</td>
</tr>
<tr>
<td></td>
<td>BDE (1)</td>
<td>43.0</td>
<td>43.8</td>
<td>43.6</td>
<td>44.6</td>
</tr>
<tr>
<td>CCSD(T)</td>
<td>ΔE(1,3)</td>
<td>8.0</td>
<td>7.6</td>
<td>5.7</td>
<td>4.1</td>
</tr>
<tr>
<td></td>
<td>BDE (3)</td>
<td>36.4</td>
<td>38.8</td>
<td>40.7</td>
<td>43.5</td>
</tr>
<tr>
<td></td>
<td>BDE (1)</td>
<td>44.4</td>
<td>46.5</td>
<td>46.4</td>
<td>47.6</td>
</tr>
<tr>
<td>CCSDᵃ</td>
<td>ΔE(1,3)</td>
<td>14.8</td>
<td>14.8</td>
<td>13.7</td>
<td>12.5</td>
</tr>
<tr>
<td></td>
<td>BDE (3)</td>
<td>27.7</td>
<td>28.4</td>
<td>29.2</td>
<td>31.4</td>
</tr>
<tr>
<td></td>
<td>BDE (1)</td>
<td>42.5</td>
<td>43.1</td>
<td>42.9</td>
<td>44.0</td>
</tr>
<tr>
<td>CCSD(T)ᵃ</td>
<td>ΔE(1,3)</td>
<td>13.4</td>
<td>11.6</td>
<td>10.0</td>
<td>8.1</td>
</tr>
<tr>
<td></td>
<td>BDE (3)</td>
<td>31.4</td>
<td>34.9</td>
<td>36.6</td>
<td>39.6</td>
</tr>
<tr>
<td></td>
<td>BDE (1)</td>
<td>44.8</td>
<td>46.6</td>
<td>46.6</td>
<td>47.7</td>
</tr>
<tr>
<td colspan="6">ᵃ These coupled-cluster computations used "orbitals" optimised with the BP86 DFT method instead of the more usual Hartree–Fock method.</td>
</tr>
</tbody>
</table>

View Online

However, further calculations showed that AS I does not lead to a balanced reference function. The problem is that, like doubly occupied d orbitals, L–M dative bonding is poorly described by a single-reference ansatz such as Hartree–Fock theory, or indeed with CASSCF methods in which the bonding pair is not included in the active space, such as with AS I here. This problem is especially severe where doubly occupied ligand orbitals donate into empty metal d orbitals.⁵ᵇ Thus, in ¹[Fe(CO)₄] and ¹[Fe(CO)₅], there is formally one empty d orbital on the metal (of a₁ symmetry for the tetracarbonyl), which leads to dative bonding with a linear combination of carbon lone pair orbitals of same symmetry. To describe multi-configurational character in this M–C bonding, it is desirable to have both of these orbitals in the active space, leading to a (10,11) active space. This can be somewhat reduced in size by removing one of the second-shell d orbitals of a₁ symmetry, as there is no corresponding d-electron pair. This gives AS II, which is (10,10) for the two singlet species. The corresponding choice for ³[Fe(CO)₄] is to use a double set of d orbitals only for the three doubly-occupied d orbitals (of a₁, a₂, and b₁ symmetry), and to use just the single d orbital for the singly-occupied a₁ and b₂ orbitals, where multi-configurational effects are less important. AS II is therefore of (8,8) size for the triplet state. Although the "same" active space is therefore not used for all the species involved for AS II, the inclusion of all near-degeneracy effects in the reference function should lead to good results for CASPT2 energies.⁴⁵

As can be seen in the Table, the ΔE(1,3) calculated with AS II is much smaller, intermediate in value between that obtained with hybrid and pure functionals. The BDEs are not necessarily reliable in this case (as with AS III, below), because it is not immediately clear how the AS should be treated upon dissociation: At the ¹[Fe(CO)₅] minimum, the AS includes, at least to a certain extent, the CO lone pair, whereas this has to be treated in a single-reference ansatz in the dis- sociated moiety.

Finally, we also used the larger AS III, which is designed using the same general principles, but is chosen to be larger and more consistent: occupied ligand orbitals of a₁ and b₂ symmetry were included for all species (12 electrons), and a second shell of d orbitals was added for all d orbitals. This leads to a (12,12) AS for all species. As can be seen in the Table, the predicted ΔE(1,3) is rather close to that obtained with AS II, which agreement, together with the fact that both of these ASs have been explicitly designed to reproduce all the near-degeneracy effects (in contrast to AS I where metal–ligand bonding effects were not included) suggests that these values are close to the correct value.⁴⁶

Further evidence for this comes from the single-reference coupled-cluster calculations. These were not possible using the large VTZ and VQZ-VTZ bases, however, as can be seen in Table 2, the results with VQZ-VDZ and even VTZ-VDZ are by and large similar to those with the larger basis sets. At first sight, coupled-cluster methods may seem inappropriate for cases where the wave- function is deemed to be multi-configurational. However, as discussed above, this is only partly so for this system, where the need for multiple references is more due to the poor quality of the Hartree–Fock reference than to the contribution of any other significant, chemically relevant, configurations. There are some indications that the single-reference method is only of borderline applicability from the value of the τ₁ diagnostic, which measures the weight of single excitations and thus of the importance of other configurations.⁴⁷ This is between 0.04 and 0.06 for all the iron species, depending mainly on the basis set, as against a desirable value of 0.02 or smaller. This casts some doubt on the coupled-cluster energetics. However, the use of DFT (BP86) "orbitals", which have been optimised using a functional which includes correlation, and can thus be expected to give a better n-electron basis for the description of the correlated wavefunction, leads to much smaller τ₁ values, of 0.02–0.025. The total energies obtained are by and large similar to those with the normal, Hartree–Fock orbital basis, except for ³[Fe(CO)₄] where the energies are a bit lower.

The relative energetics at the coupled-cluster level are by and large similar to those obtained with CASPT2 with AS II and III. The bond energies are more reliable, as there is no question about the effect of splitting the active space. Also, it is to be noted that the use of BP86 orbitals leads to a lower relative energy of ³[Fe(CO)₄], and thus to larger ΔE(1,3). Our feeling is that the CCSD(T)/ VQZ-VDZ results, using BP86 orbitals, are the most reliable, giving ΔE(1,3) of 8.1 kcal mol⁻¹, and BDE(3) of 39.6 kcal mol⁻¹. After adding the zero-point energy correction from the B3PW91* calculations, this gives respectively ΔE(1,3) = 8.8 kcal mol⁻¹ and BDE(3) = 36.0 kcal mol⁻¹. However, these results are still not fully converged: BDE(3) is probably somewhat too small, and ΔE(1,3) still somewhat too large.

Faraday Discuss., 2003, 124, 129–143

View Online

Returning to the DFT results, we observe that the modified B3PW91* functional, with the amount of exact exchange reduced to 15%, gives the results closest to those we believe would emerge from CCSD(T) calculations with larger basis sets. We have therefore mainly used this functional in exploring the surface-crossing behaviour, and in our rate computations.

MECP calculations and NA-TST results

Following the calibration studies described in the previous section, we also located the MECP for intersection of the reactant triplet surface with the singlet surface using several different DFT functionals, and the results are shown in Table 1. The *geometry* of the MECP was found to be more or less the same using the different methods. However, these structures are remarkable in one way which is important to discuss. Thus, based on the $D_{3\text{h}}$ structure of $[\text{Fe(CO)}_5]$, and the $C_{2\text{v}}$, truncated trigonal bipyramid, structures of both singlet and triplet $[\text{Fe(CO)}_4]$, it would perhaps be natural to assume that the lowest crossing occurs at $C_{2\text{v}}$ geometries corresponding to an extended Fe–C bond for one of the equatorial carbonyl ligands. In fact, we made this very assumption in our previous, unpublished, study of the MECP in this system, cited in the review, ref. 14a. Another study aimed at understanding the surface crossing behaviour in this system, $^{6d}$ in which the partial optimisation method was used to study the crossing point, also made this assumption. In fact, this is in some ways inevitable in the latter case, as this method involves carrying out a set of geometry optimisations at fixed values of a given geometric coordinate, chosen here to be the equatorial Fe–C distance. On the singlet surface, the minimum energy path for dissociation is presumably of $C_{2\text{v}}$ symmetry so the set of partially optimised structures on that surface will be $C_{2\text{v}}$ symmetric.

We have located MECPs under the constraint of $C_{2\text{v}}$ symmetry, at the B3LYP, B3PW91 and B3PW91* levels, with the TZV basis. These lie 6.9, 6.5 and 5.4 kcal mol$^{-1}$, respectively, above the separated reactants (without correction for ZPE). The first of these values is in good agreement with the value of 5.2 kcal mol$^{-1}$, derived at the B3LYP/SVP level reported in ref. 14a. However, upon calculating the vibrational frequencies within the seam of crossing at the $C_{2\text{v}}$ MECP, $^{9,18}$ it becomes apparent that these points are not minima within the seam of crossing: in each case, three imaginary frequencies are obtained, corresponding to various symmetry-breaking bending motions of the incoming carbonyl.

Accordingly, we searched for a less symmetric MECP, and found one at the geometry shown in Fig. 2. This structure can be described as involving "sideways" approach of the CO to $^3[\text{Fe(CO)}_4]$, both in terms of the incoming CO ($\angle\text{Fe–C–O}=135^\circ$) itself, and of the $[\text{Fe(CO)}_4]$ moiety and its $C_{2\text{v}}$ axis ($C_{\text{eq}}$–Fe–$C_{\text{incoming}}$ angles: $99^\circ$ and $163^\circ$, *vs.* $129^\circ$ for both angles in the $C_{2\text{v}}$ MECP). The reason for this approach seems to be that the triplet potential energy surface is much less repulsive along this coordinate: along the $C_{2\text{v}}$ axis, there is a repulsive three-electron two-centre interaction between the CO lone pair and the singly occupied $d$ orbital of $\text{a}_1$ symmetry. With the side-on approach, the CO lone pair is less oriented towards the metal, thus less repulsive, and the $\text{b}_2$ singly-occupied $d$ orbital on the metal can form a back-bonding interaction with the $\pi^*$ orbital on the CO.

![](./images/812392571224457217_2.jpg)

Fig. 2 Two views of the B3PW91*/TZV structure of the MECP between singlet and triplet states of $[\text{Fe(CO)}_5]$. On the left, "side-on"; on the right, looking down the approximate $C_{2\text{v}}$ symmetry axis of the $[\text{Fe(CO)}_4]$ moiety.

138
Faraday Discuss., 2003, 124, 129–143

View Online

Indeed, at the crossing point, the triplet gradient is only very weakly repulsive, and geometry optimisation on the triplet surface, although it does lead to dissociation of the Fe–C bond, involves a very flat potential energy curve. We have not found any weakly bound triplet complex: although such a van der Waals complex certainly exists, the interaction will be very weak, and will be poorly described by DFT methods. Along the $C_\text{s}$ approach pathway, the incoming CO ligand can approach much closer on the triplet surface before significant repulsion sets in, and thereby, the intersection with the attractive, singlet, curve, occurs at lower energies. In agreement with this discussion, the triplet wavefunction at the $C_\text{s}$ MECP involves significant spin density on the incoming CO ligand (0.23 unpaired electrons), as predicted from the donation into the $\pi^*$ orbital. Also, $r(\text{Fe–C})$ is much smaller for the $C_\text{s}$ MECP (2.24 Å) than for the $C_{2\text{v}}$ one (2.65 Å). All the frequencies at the $C_\text{s}$ MECP are real.

The energetics of the $C_\text{s}$ MECP are given, for the different DFTs where it has been located, in Table 1. It can be seen that the barrier is very low, especially at our preferred B3PW91* level. One interesting aspect is that the height of the MECP does not vary in any immediately obvious way with the energy splitting $\Delta E(1,3)$, as would be suggested by considering Fig. 1. Thus, the BLYP and mPW1PW91 MECPs have very similar relative energies, even though the state splitting is extremely small in the first case, and large in the second. This is because, as we have discussed before, $^{12–14}$ the one-dimensional picture is only qualitatively correct for understanding surface crossings: $^1[\text{Fe(CO)}_4]$ and $^3[\text{Fe(CO)}_4]$ have significantly (if not radically) different geometries, $^{5,6}$ and some energy needs to be provided to bring them both to the same geometry: this factor may be as important as the differing behaviour along the "reaction coordinate" in establishing the height of the MECP.

We have also computed the other properties needed for the NA-TST computations at the MECP. Most of these, such as the slopes on the two surfaces, or the reduced mass in the direction orthogonal to the seam of crossing (9.2 u), are obtained directly from the MECP computation. We have also calculated the rms spin–orbit coupling, at the CASSCF level, using AS III as described above, and get a value of 66 cm$^{-1}$. At the optimum geometry of $^3[\text{Fe(CO)}_4]$, the rms spin–orbit coupling is somewhat smaller, at 29 cm$^{-1}$.

Putting all these elements together leads to the predicted NA-TST results, shown in Fig. 3. As can be seen, the quantitative agreement with experiment is not perfect – the computed rate

![](./images/812392571224457217_3.jpg)

Fig. 3 Arrhenius plot of the computed rate coefficients for addition of CO to $^3[\text{Fe(CO)}_4]$. The heavy line uses the WKB-derived expression for $p_\text{SH}$ in computing $k$, the light line uses the Landau–Zener expression, and the dot–dashed line, provided for comparison (see text) assumes adiabatic behaviour ($p_\text{SH}=1$). The dot is the experimental rate at room temperature from ref. 3.

Faraday Discuss., 2003, 124, 129–143

View Online

coefficient at room temperature, $8.8 \times 10^{-15}\ \text{cm}^3\ \text{molecule}^{-1}\ \text{s}^{-1}$, is too low, by a factor of six. Given the approximate nature of the NA-TST theory, and the remaining uncertainties concerning the potential energy surfaces, agreement to within better than one order of magnitude cannot in any case be expected. $^{18}$ For example, increasing or decreasing the energy of the MECP by a small amount, $0.5\ \text{kcal}\ \text{mol}^{-1}$, (which is a conservative estimate for the error on this quantity) roughly halves or doubles, respectively, the computed 300 K rate coefficient. Doubling or halving the rms spin-orbit coupling, $V_{12}$, again provides a conservative uncertainty for the inaccuracy of the non-adiabatic treatment, and leads to rate coefficients roughly four times larger or smaller, respectively. Finally, it is to be noted that for both the $^3[\text{Fe(CO)}_4]$ reactant and the MECP, there are several very low frequencies (5 and 7, respectively, below $100\ \text{cm}^{-1}$), whose contribution to the partition function and density of states may be poorly described by the standard approximations for the harmonic oscillator.

Taking into account these inevitable uncertainties, $^{18}$ we believe that the computed 300 K rate coefficient is in fact in excellent semi-quantitative agreement with the experimental value. This lends support to the NA-TST approach, and to the accuracy of our computed potential energy surfaces. Computed rates using potential energy surfaces obtained with different methods are in less good agreement. For example, using the B3PW91/TZV MECP, which lies $2.17\ \text{kcal}\ \text{mol}^{-1}$ above the reactants, the computed rate coefficient is $8.5 \times 10^{-16}\ \text{cm}^3\ \text{molecule}^{-1}\ \text{s}^{-1}$, one order of magnitude smaller than that obtained using B3PW91*, which is already somewhat too small.

Overall, our computations are in agreement with many other experimental observations, and also provide much additional insight. First, the computed rate is confirmed to be significantly slower than the gas-collision rate, as was found experimentally. This emphatically confirms that the difference in rate with the analogous spin-allowed $\text{CO} + ^3[\text{Fe(CO)}_3]$ reaction is due to the spin-forbidden nature of the reaction. The need to change spin leads to two differences compared to spin-allowed reactions: instead of only having a variational barrier, $^{48}$ there is a true, albeit small, energy barrier to surmount, and the system must undergo a somewhat improbable hop from one surface to the other at the MECP. It is possible to quantify the contribution of both of these effects to the rate reduction by considering the ratio of the computed rates with and without non-adiabatic behaviour. The "adiabatic" rate coefficient plotted in Fig. 3 is obtained using traditional transition state theory, using all the properties of the MECP but treating it instead as an adiabatic TS (equivalently, $p_{\text{SH}}$ is set to 1). As can be seen, this rate coefficient is about 20 times higher than the non-adiabatic one at all temperatures. Since the overall rate coefficient is *ca.* 500 times lower than for the analogous spin-allowed reaction, it appears that this reduction in rate is due in roughly equal parts to the presence of the barrier, and to the need for surface-hopping.

Another interesting observation is that the temperature dependence is weak: between 250 and 400 K, the computed WKB-derived rate can be fitted to the Arrhenius equation with an apparent $E_{\text{a}}$ of $1.2\ \text{kcal}\ \text{mol}^{-1}$. In the experiments, a very limited temperature range only was accessible and accordingly no change in rate was observable within experimental error. Smirnov$^{49}$ has measured the kinetics of shock-tube thermal dissociation of $[\text{Fe(CO)}_5]$, and modelled them using a complex kinetic scheme of dissociation and recombination reactions. The best agreement with experiments involved a barrier to reverse addition of $\text{CO}$ to $[\text{Fe(CO)}_4]$ of $2.5 \pm 1.5\ \text{kcal}\ \text{mol}^{-1}$, but this result was obtained under the assumption that $p_{\text{SH}} = 1$, which can be expected to lead to an overestimate of the barrier. It is to be noted that the temperature dependence is close to that of the "adiabatic" rate, showing that the spin-hopping constraint does not lead to an increase in the activation energy (enthalpic effect), but only to a decrease of the rate at all temperatures (entropic effect). This is explained by the fact that the integration to give $N(E)$ is dominated at all energies by the terms with a small amount of energy $E_{\text{H}}$ in the direction orthogonal to the crossing seam. This is because the hopping probability $p_{\text{SH}}$ is largest for small $E_{\text{H}}$, and so is the density of states in the orthogonal modes. Since the latter increases with energy in the same way for non-adiabatic and adiabatic reactions, the energy and temperature dependence of the rate coefficients are also similar in both cases. It can also be noted that the WKB-derived expression for the hopping probability and the Landau-Zener one give very similar results, suggesting that tunnelling does not play an important role in the present reaction.

The observation that the activation barrier is small is important: it means that the activation barrier of the reverse reaction, unimolecular dissociation of $[\text{Fe(CO)}_5]$, should not exceed by much the endothermicity of the reaction. This means that the experimental determination of the BDE, $^{44}$

140
Faraday Discuss., 2003, 124, 129-143

based on measuring this activation energy, and hitherto assumed to refer to BDE(1), is much more likely to pertain to BDE(3), and it can be seen from Tables 1 and 3 that our computed values for BDE(3) are in good agreement with the experimental value (41±2 kcal mol⁻¹), whereas those for BDE(1) agree less well.

## Conclusions
In this contribution, we have tried to show how accurate DFT and *ab initio* computations, combined with an appropriate form of non-adiabatic transition-state theory, can be used to predict the rate coefficient for a spin-forbidden ligand recombination reaction. Whilst the size of the system involved is relatively small, accurate calculations for metal complexes of this type are highly challenging. We have shown how the CASPT2 level, and especially the CCSD(T) level, can be used to derive fairly accurate energetics, provided great care is taken in the choice of active space, of basis set, of reference orbitals, *etc*. It is apparent from Tables 2 and 3 that very different values can be obtained from different calculations: Reliable calibration can only be obtained from a hierarchy of calculations! Despite having carried out a broad range of computations, our best estimates for the energy difference between singlet and triplet [Fe(CO)₄], 8 kcal mol⁻¹, and of the first bond energy of [Fe(CO)₅], BDE(3), 39.6 kcal mol⁻¹, do not seem to be fully converged with basis set size, and must therefore still be treated with some caution.

We have also shown how the MECP for the title reaction can be located and used to characterise reactivity. *Full* characterisation of the MECP is essential: it is only through the computation of frequencies that we realised that the true MECP is not of $C_{2v}$ symmetry, as had been previously assumed. Finally, application of the NA-TST method gives useful insight into the origin of the slow rate of this reaction, gives semi-quantitative agreement with the experimental rate, and allows us to reinterpret the experiment which was used to derive the bond energy of [Fe(CO)₅], thereby giving a value in good agreement with our computations.

Finally, the experience gained in this study should be transferable to many other spin-forbidden reactions, *e.g*. the other reactions studied by Weitz *et al.*,³⁴ and the recombination of CO with haem compounds.¹³

## Acknowledgements
JNH thanks the EPSRC for support of this research, and MA thanks the University of l'Aquila for the grant "Ricerche di Rilevante Interesse di Ateneo anno 2001".

## References
1  For reviews, see (a) M. Poliakoff and E. Weitz, *Acc. Chem. Res.*, 1987, **20**, 408; (b) N. Leadbeater, *Coord. Chem. Rev.*, 1999, **188**, 35; (c) M. Poliakoff and J. J. Turner, *Angew. Chem., Int. Ed. Engl.*, 2001, **40**, 2809.
2  For recent highlights, see (a) L. Bañares, T. Baumert, M. Bergt, B. Kiefer and G. Gerber, *J. Chem. Phys.*, 1998, **108**, 5799–5810; (b) H. Ihee, J. Cao and A. H. Zewail, *Angew. Chem., Int. Ed. Engl.*, 2001, **40**, 1532–1536; (c) P. T. Snee, C. K. Payne, S. D. Mebane, K. T. Kotz and C. B. Harris, *J. Am. Chem. Soc.*, 2001, **123**, 6909–6915.
3  T. A. Seder, A. J. Ouderkirk and E. Weitz, *J. Chem. Phys.*, 1986, **85**, 1977–1986; R. J. Ryther and E. Weitz, *J. Phys. Chem.*, 1991, **95**, 9841–9852.
4  See also E. Weitz, *J. Phys. Chem.*, 1994, **98**, 11 256–11 264; Ref. *1a*; J. Wang, G. T. Long and E. Weitz, *J. Phys. Chem. A*, 2001, **105**, 3765–3772.
5  (a) L. A. Barnes, M. Rosi and C. W. Bauschlicher, Jr., *J. Chem. Phys.*, 1991, **94**, 2031–2039; (b) B. J. Persson, B. O. Roos and K. Pierloot, *J. Chem. Phys.*, 1994, **101**, 6810–6821; (c) A. W. Ehlers and G. Frenking, *Organometallics*, 1995, **14**, 423–426; (d) O. Rubner, V. Engel, M. R. Hachey and C. Daniel, *Chem. Phys. Lett.*, 1999, **302**, 489–494; (e) A. Ricca, *Chem. Phys. Lett.*, 2001, **350**, 313–317.
6  (a) B. Delly, M. Wrinn and H. P. Lüthi, *J. Chem. Phys.*, 1994, **100**, 5785–5791; (b) J. Li, G. Schreckenbach and T. Ziegler, *J. Am. Chem. Soc.*, 1995, **117**, 486–494; (c) W. Wang and E. Weitz, *J. Phys. Chem. A*, 1997, **101**, 2358–2363; (d) S. A. Decker and M. Klobukowski, *J. Am. Chem. Soc.*, 1998, **120**, 9342–9355; (e) O. González-Blanco and V. Branchadell, *J. Chem. Phys.*, 1999, **110**, 778–783.
7  C. Daniel, M. Bénard, A. Dedieu, R. Wiest and A. Veillard, *J. Phys. Chem.*, 1984, **88**, 4805–4811; M. C. Heitz and C. Daniel, *J. Am. Chem. Soc.*, 1997, **119**, 8269–8275; M. C. Heitz, K. Finger and C. Daniel, *Coord. Chem Rev.*, 1997, **159**, 171–193.

*Faraday Discuss.*, 2003, **124**, 129–143

8 (a) N. Koga and K. Morokuma, *Chem. Phys. Lett.*, 1985, **119**, 371; (b) A. Farazdel and M. Dupuis,
*J. Comput. Chem.*, 1991, **12**, 276; (c) F. Jensen, *J. Am. Chem. Soc.*, 1992, **114**, 1596; (d) D. R. Yarkony,
*J. Phys. Chem.*, 1993, **97**, 4407; (e) M. J. Bearpark, M. A. Robb and H. B. Schlegel, *Chem. Phys. Lett.*,
1994, **223**, 269; (f) K. M. Dunn and K. Morokuma, *J. Phys. Chem.*, 1996, **100**, 123; (g) J. M. Anglada and
J. M. Bofill, *J. Comput. Chem.*, 1997, **18**, 992.

9 J. N. Harvey, M. Aschi, H. Schwarz and W. Koch, *Theor. Chem. Acc.*, 1998, **99**, 95.

10 M. Aschi, J. N. Harvey, C. A. Schalley, D. Schröder and H. Schwarz, *Chem. Commun.*, 1998, 531;
D. Schröder, C. Heinemann, H. Schwarz, J. N. Harvey, S. Dua, S. Blanksby and J. H. Bowie, *Chem. Eur.
J.*, 1998, **4**, 2550; C. A. Schalley, J. N. Harvey, D. Schröder and H. Schwarz, *J. Phys. Chem. A*, 1998, **102**,
1021; M. Aschi and J. N. Harvey, *J. Chem. Soc. Perkin Trans. 2*, 1999, 1059; M. Aschi and F. Grandinetti,
*Int. J. Mass Spec.*, 2000, **201**, 151; E. L. Øiestad, J. N. Harvey and E. Uggerud, *J. Phys. Chem. A*, 2000,
**104**, 8382.

11 See *e.g.* M. R. Manaa and D. R. Yarkony, *J. Chem. Phys.*, 1991, **95**, 1808; K. A. Nguyen, M. S. Gordon, J.
A. Montgomery, Jr., H. H. Michels and D. R. Yarkony, *J. Chem. Phys.*, 1993, **98**, 3845; A. H. H. Chang
and D. R. Yarkony, *J. Chem. Phys.*, 1993, **99**, 6824; J. M. Anglada, J. M. Bofill, S. Olivella and A. Solé, *J.
Am. Chem. Soc.*, 1996, **118**, 4636; Q. Cui and K. Morokuma, *J. Chem. Phys.*, 1997, **107**, 4951; R. G.
Sadygov and D. R. Yarkony, *J. Chem. Phys.*, 1997, **107**, 4994; J. E. Stevens, Q. Cui and K. Morokuma, *J.
Chem. Phys.*, 1998, **108**, 1544; A. L. Kaledin, Q. Cui, M. C. Heaven and K. Morokuma, *J. Chem. Phys.*,
1999, **111**, 5004; S. Wilsey, F. Bernardi, M. Olivucci, M. A. Robb, S. Murphy and W. Adam, *J. Phys.
Chem. A*, 1999, **103**, 1669; D.-Y. Hwang and A. M. Mebel, *Chem. Phys.*, 2000, **256**, 169; E. García-
Expósito, M. J. Bearpark, R. M. Ortuño, V. Branchadell, M. A. Robb and S. Wilsey, *J. Org. Chem.*, 2001,
**66**, 8811; F. Ijjaali, M. El-Mouhtadi, M. Esseffar, M. Alcamí, O. Mó and M. Yáñez, *Phys. Chem. Chem.
Phys.*, 2001, **3**, 179.

12 (a) K. M. Smith, R. Poli and J. N. Harvey, *New J. Chem.*, 2000, **24**, 77–80; (b) K. M. Smith, R. Poli and
J. N. Harvey, *Chem. Eur. J.*, 2001, **7**, 1679; (c) J. C. Green, J. N. Harvey and R. Poli, *J. Chem. Soc., Dalton
Trans.*, 2002, 1861.

13 J. N. Harvey, *J. Am. Chem. Soc.*, 2000, **122**, 12 401.

14 For reviews of this work, see(a) J. N. Harvey, in *Computational Organometallic Chemistry*, ed. T. R.
Cundari, Marcel Dekker, New York, Basel, 2001; (b) J. N. Harvey, R. Poli and K. M. Smith, *Coord. Chem.
Rev.* in press; (c) R. Poli and J. N. Harvey, *Chem. Soc. Rev.*, 2003, **32**, 1.

15 For work by other groups on spin-forbidden reactions of transition metal compounds especially those
relating to the location of MECPs see *e.g.* (a) D. G. Musaev and K. Morokuma, *J. Phys. Chem.*, 1996, **100**,
11 600; (b) D. Danovich and S. Shaik, *J. Am. Chem. Soc.*, 1997, **119**, 1773; (c) D. Schröder, S. Shaik and
H. Schwarz, *Acc. Chem. Res.*, 2000, **33**, 139–145; (d) E. Le Grognec and R. Poli, *Chem. Eur. J.*, 2001, **7**,
4572–4583; (e) J. S. Hess, S. Leelasubcharoen, A. L. Rheingold, D. J. Doren and K. H. Theopold, *J. Am.
Chem. Soc.*, 2002, **124**, 2454–2455.

16 J. C. Lorquet and B. Leyh-Nihant, *J. Phys. Chem.*, 1988, **92**, 4778.

17 (a) Q. Cui, K. Morokuma and J. M. Bowman, *J. Chem. Phys.*, 1999, **110**, 9469; (b) M. Aschi and F.
Grandinetti, *J. Chem. Phys.*, 1999, **111**, 6759; (c) J. N. Harvey, S. Grimme, M. Woeller, S. D. Peyerimhoff,
D. Danovich and S. Shaik, *Chem. Phys. Lett.*, 2000, **322**, 358–362; (d) P. R. P. de Moraes, H. V. Linnert,
M. Aschi and J. M. Riveros, *J. Am. Chem. Soc.*, 2000, **122**, 10 133–10 142; (e) M. Aschi and A. Largo,
*Chem. Phys.*, 2001, **265**, 251–261; (f) A. J. Marks, *J. Chem. Phys.*, 2001, **114**, 1700.

18 J. N. Harvey and M. Aschi, *Phys. Chem. Chem. Phys.*, 1999, **1**, 5555–5563.

19 J. B. Delos, *J. Chem. Phys.*, 1973, **59**, 2365.

20 Many of the necessary programs can be obtained upon request from JNH.

21 M. J. Frisch, G. W. Trucks, H. B. Schlegel, G. E. Scuseria, M. A. Robb, J. R. Cheeseman, V. G.
Zakrzewski, J. A. Montgomery, Jr., R. E. Stratmann, J. C. Burant, S. Dapprich, J. M. Millam, A. D.
Daniels, K. N. Kudin, M. C. Strain, O. Farkas, J. Tomasi, V. Barone, M. Cossi, R. Cammi, B. Mennucci,
C. Pomelli, C. Adamo, S. Clifford, J. Ochterski, G. A. Petersson, P. Y. Ayala, Q. Cui, K. Morokuma,
D. K. Malick, A. D. Rabuck, K. Raghavachari, J. B. Foresman, J. Cioslowski, J. V. Ortiz, B. B. Stefanov,
G. Liu, A. Liashenko, P. Piskorz, I. Komaromi, R. Gomperts, R. L. Martin, D. J. Fox, T. Keith, M. A.
Al-Laham, C. Y. Peng, A. Nanayakkara, C. Gonzalez, M. Challacombe, P. M. W. Gill, B. G. Johnson,
W. Chen, M. W. Wong, J. L. Andres, M. Head-Gordon, E. S. Replogle and J. A. Pople, *GAUSSIAN 98*
(Revision A.7), Gaussian, Inc., Pittsburgh, PA, 1998.

22 A. Schäfer, H. Horn and R. Ahlrichs, *J. Chem. Phys.*, 1992, **97**, 2571–2577.

23 A. J. H. Wachters, *J. Chem. Phys.*, 1970, **52**, 1033.

24 R. D. Amos, A. Bernhardsson, A. Berning, P. Celani, D. L. Cooper, M. J. O. Deegan, A. J. Dobbyn, F.
Eckert, C. Hampel, G. Hetzer, P. J. Knowles, T. Korona, R. Lindh, A. W. Lloyd, S. J. McNicholas, F. R.
Manby, W. Meyer, M. E. Mura, A. Nicklass, P. Palmieri, R. Pitzer, G. Rauhut, M. Schütz, U. Schumann,
H. Stoll, A. J. Stone, R. Tarroni, T. Thorsteinsson, and H.-J. Werner, *MOLPRO, a package of ab initio
programs designed by H.-J. Werner and P. J. Knowles, version 2002.1*, University of Birmingham, UK, 2002.

25 P. Celani and H.-J. Werner, *J. Chem. Phys.*, 2000, **112**, 5546.

26 B. O. Roos and K. Andersson, *Chem. Phys. Lett.*, 1995, **245**, 215–223.

27 P. J. Knowles, C. Hampel and H.-J. Werner, *J. Chem. Phys.*, 1993, **99**, 5219; P. J. Knowles, C. Hampel and
H.-J. Werner, *J. Chem. Phys.*, 2000, **112**, 3106, erratum.

142
Faraday Discuss., 2003, **124**, 129–143

View Online

28 T. H. Dunning, Jr., *J. Chem. Phys.*, 1989, **90**, 1007.
29 A. Ricca and C. W. Bauschlicher, *Theor. Chem. Acc.*, 2001, **106**, 314.
30 B. A. Hess, *Phys. Rev. A*, 1986, **33**, 3742, and references therein.
31 W. Forst, *Theory of Unimolecular Reactions*, Academic Press, New York, 1973; T. Baer and W. L. Hase, *Unimolecular Reaction Dynamics*, Oxford University Press, Oxford, UK, 1996.
32 A. Berning, M. Schweizer, H.-J. Werner, P. J. Knowles and P. Palmieri, *Mol. Phys.*, 2000, **98**, 1823.
33 W. Koch and M. C. Holthausen, *A Chemist's Guide to Density Functional Theory*, Wiley-VCH, Weinheim, 2000.
34 P. M. W. Gill, *Mol. Phys.*, 1996, **89**, 433.
35 A. D. Boese, N. L. Doltsinis, N. C. Handy and M. Sprik, *J. Chem. Phys.*, 2000, **112**, 1670.
36 A. D. Becke, *J. Chem. Phys.*, 1993, **98**, 5648.
37 C. Adamo and V. Barone, *Chem. Phys. Lett.*, 1997, **274**, 242; A. D. Becke, *J. Chem. Phys.*, 1996, **104**, 1040.
38 C. Adamo and V. Barone, *J. Chem. Phys.*, 1998, **108**, 664–675.
39 C. Adamo and V. Barone, *J. Chem. Phys.*, 1999, **110**, 6158–6170.
40 J. K. Kang and C. B. Musgrave, *J. Chem. Phys.*, 2001, **115**, 11040.
41 B. J. Lynch, P. L. Fast, M. Harris and D. G. Truhlar, *J. Phys. Chem. A*, 2000, **104**, 4811–4815.
42 See *e.g.* D. M. Ball, C. Budha, A. M. Gillespie, D. P. White and T. R. Cundari, *Inorg. Chem.*, 2002, **41**, 152–156; For a discussion see ref. 14*c*.
43 (*a*) M. Reiher, O. Salomon and B. A. Hess, *Theor. Chem. Acc.*, 2001, **107**, 48; (*b*) O. Salomon, M. Reiher and B. A. Hess, *J. Chem. Phys.*, 2002, **117**, 4729.
44 K. E. Lewis, D. M. Golden and G. P. Smith, *J. Am. Chem. Soc.*, 1984, **106**, 3905.
45 For a discussion of the use of different active space for different species on the same potential energy surface, see ref. 5*b*.
46 However one factor we have not systematically explored is the effect of the level shift on the computed energetics. In one case, we found non-negligible changes in $\Delta E(1,3)$ from varying the shift from $0.5E_{\text{h}}$ to 0.3 (the value used in all the other computations) or 0.1. This dependence needs to be explored in more detail before using CASPT2 calculations as accurate calibrations.
47 See discussion in F. Jensen, *An Introduction to Computational Chemistry*, John Wiley, 1998.
48 We have confirmed that the spin-allowed reaction of CO with $^{3}[\text{Fe}(\text{CO})_{3}]$ proceeds on a purely attractive potential energy surface, by carrying out a set of constrained optimizations on $^{3}[\text{Fe}(\text{CO})_{4}]$ at progressively larger values of one Fe–C bond length. The energy increases smoothly to the dissociation asymptote.
49 V. N. Smirnow, *Kinet. Catal.*, 1993, **34**, 591.

Faraday Discuss., 2003, **124**, 129–143
143