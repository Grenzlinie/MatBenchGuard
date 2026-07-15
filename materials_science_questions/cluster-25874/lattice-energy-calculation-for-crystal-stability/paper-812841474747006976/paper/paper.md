Condensed Matter, Interfaces, and Materials

# Phase-Transferable Force Field for Alkali Halides
Marie-Madeleine Walz, Mohammad Mehdi Ghahremnapour, Paul J. van Maaren, and David van der Spoel

*J. Chem. Theory Comput.*, **Just Accepted Manuscript** • DOI: 10.1021/acs.jctc.8b00507 • Publication Date (Web): 09 Oct 2018
Downloaded from http://pubs.acs.org on October 10, 2018

Just Accepted

"Just Accepted" manuscripts have been peer-reviewed and accepted for publication. They are posted online prior to technical editing, formatting for publication and author proofing. The American Chemical Society provides "Just Accepted" as a service to the research community to expedite the dissemination of scientific material as soon as possible after acceptance. "Just Accepted" manuscripts appear in full in PDF format accompanied by an HTML abstract. "Just Accepted" manuscripts have been fully peer reviewed, but should not be considered the official version of record. They are citable by the Digital Object Identifier (DOI®). "Just Accepted" is an optional service offered to authors. Therefore, the "Just Accepted" Web site may not include all articles that will be published in the journal. After a manuscript is technically edited and formatted, it will be removed from the "Just Accepted" Web site and published as an ASAP article. Note that technical editing may introduce minor changes to the manuscript text and/or graphics which could affect content, and all legal disclaimers and ethical guidelines that apply to the journal pertain. ACS cannot be held responsible for errors or consequences arising from the use of information contained in these "Just Accepted" manuscripts.

![](./images/812841474747006976_1.jpg)

is published by the American Chemical Society. 1155 Sixteenth Street N.W., Washington, DC 20036
Published by American Chemical Society. Copyright © American Chemical Society.
However, no copyright claim is made to original U.S. Government works, or works produced by employees of any Commonwealth realm Crown government in the course of their duties.

# Phase-Transferable Force Field for Alkali Halides

Marie-Madeleine Walz, Mohammad M. Ghahremanpour, Paul J. Van Maaren,
and David Van der Spoel*

Department of Cell and Molecular Biology, Uppsala University, Husargatan 3, Box 596,
SE-75124 Uppsala, Sweden

E-mail: david.vanderspoel@icm.uu.se

### Abstract

A longstanding goal of computational chemistry is to predict the state of materials in all phases with a single model. This is particularly relevant for materials that are difficult or dangerous to handle or compounds that have not yet been created. Progress towards this goal has been limited as most work has concentrated on just one phase, often determined by particular applications. In the framework of the development of the *Alexandria* force field we present here new polarizable force fields for alkali halides with Gaussian charge distributions for molecular dynamics simulations. We explore different descriptions of the Van der Waals interaction, like the commonly applied 12-6 Lennard-Jones (LJ), and compare it to “softer” ones, such as 8-6 LJ, Buckingham and a modified Buckingham potential. Our results for physico-chemical properties of the gas, liquid and solid phase of alkali halides, are compared to experimental data and calculations with reference polarizable and non-polarizable force fields. The new polarizable force field that employs a modified Buckingham potential predicts the tested properties for gas, liquid and solid phases with a very good accuracy. In contrast to reference force fields, this model reproduces the correct crystal structures for all alkali halides at low and high temperature. Seeing that experiments with molten salts may be tedious due to high temperatures and their corrosive nature, the models presented here can contribute significantly to our understanding of alkali halides in general and melts in particular.

### Introduction

Alkali halides play a fundamental role in nature from biology¹ to atmospheric science,² but also in technological and industrial applications, such as the field of thermal energy storage³ or processing of aluminum.⁴ The broad spectrum of applications highlights the need for a detailed understanding of such salts from a theoretical point of view. Computer simulations of molecular dynamics (MD) are nowadays often used to support experimental findings, providing insight on a molecular level and allowing for a more reliable and

trustworthy interpretation of observed phenomena. The predictive power of a computer simulation for calculating physico-chemical properties relies, however, sensitively on an accurate description of interatomic and -molecular interactions. Such non-bonded interactions can be represented by a set of functions accounting for Van der Waals and Coulomb interactions. The mathematical description for electrostatic interactions with different charge distributions and optionally polarizability has been researched at length⁵⁻⁸ and a multitude of different functional forms exist for the Van der Waals term. Historically, often a simple 12-6 Lennard-Jones potential⁹ is employed, in particular in biomolecular force fields,¹⁰ even though a variety of more accurate potentials have been proposed. It is somewhat puzzling indeed that neither the Buckingham potential¹¹ nor, for instance, the Lennard-Jones 9-6 potential,¹² has been adopted more widely. However, a number of recent papers¹³⁻¹⁷ have investigated potentials with a softened repulsive interaction.

There is an extensive body of literature regarding force fields developed to describe alkali halides in computer simulations. A common approach is to parameterise alkali halides in connection to established water models, using for example ion-water distances or hydration free energies in the parameterisation procedure.¹⁶,¹⁸⁻³³ Other research focuses the parameterisation on physico-chemical properties from alkali halides only, or even just uses parameters that are extracted from density functional theory calculations.¹⁷,³⁴⁻⁴⁰ Furthermore, there are force fields that are parameterised for describing both the physico-chemical properties of ions in a crystal lattice and ions solvated by water.¹⁶,¹⁹ Besides these differences in parameterisation approach, another distinction is that some force fields have individual sets of parameters for alkali halide salts,³⁴,³⁵ while more recent force fields use individual ion parameters.¹⁶,¹⁸⁻²⁰,³⁰,³¹ The latter has the promise of transferability regarding mixing of different salts in solution, melts or solid phases. With individual ion parameters there is just one potential describing e.g. a chloride-chloride interaction, while for parameters for the individual salts the chloride-chloride interaction in NaCl could be different from that in KCl. Still, such potentials have been successfully used for mixtures by using an interpolation

method. $^{41-43}$

Even if one is interested in the properties of ions in water only, it is reasonable to include the interaction between the alkali and halide ions in the parameterisation: beyond the pure alkali halides, such interactions are relevant for all ions in solution, for example in the process of crystallisation or dissolution of salts in aqueous solution or when contact ion pairs are formed in water. For instance, Cavallari *et al.*$^{44}$ investigated ion-ion interactions in aqueous solution by comparing the accuracy of the microscopic structure of concentrated salt solutions (NaCl, KCl) with their thermodynamic properties that were predicted by MD simulations and concluded that there is no direct correlation between these. The authors$^{44}$ suggest that the lack of correlation might be explained by a too steep repulsion term of the employed 12-6 Lennard-Jones potential and the lack of polarization in the investigated force field models. Auffinger *et al.*$^{45}$ explored the effect of different Van der Waals parameter sets (Åqvist$^{24}$ and Dang$^{46}$) and water models (TIP3P$^{47}$ and SPC/E$^{48}$) on ion contact pair formation and ion aggregation (NaCl, KCl) in biomolecular simulations using the AMBER force field.$^{49}$ They report that, when using Åqvist ion-parameters,$^{24}$ unphysical crystal formation in water can occur at concentrations that are still well below the solubility limit, that is associated with an increased occurrence of ion contact pairs at lower concentrations where no crystal formation is observed. The authors$^{45}$ point out that this is even relevant for the interaction of charged biomolecular systems, as the cation - oxygen/nitrogen interactions are affected to an unknown degree by the use of misbalanced ionic parameters. These examples demonstrate that it is crucial to develop a physically accurate description of the interionic potentials of the alkali halides and to optimise parameters in one force field consistently together in order to avoid artefacts in MD simulations. We note that this artefact has been corrected in more recent AMBER versions (later than AMBER ff9X) $^{19}$ and this has been verified in, for instance, simulations of RNA in different salts.$^{50}$

In this paper we focus on systematic force field parameterisation of alkali halides based on gas and solid phase properties. The parameters will be part of the *Alexandria* force field, that

will rely on both experimental and quantum chemical data. A database of quantum-chemical properties that lies at the foundation of the force field has recently been published⁵¹,⁵² based on quantum chemistry calculations reported previously⁵³ and distributed charge parameters for general organic compounds have been derived.⁵⁴ Other input to the force field develop- ment is an extensive set of benchmarks of classical force fields used in simulations of liquids and model systems⁵⁵⁻⁶⁴ which can be found at the http://virtualchemistry.org reposi- tory.⁶⁵ We strive for a phase transferable force field (g, l, s) such as demonstrated for example by Jordan *et al.* for molecular nitrogen⁶⁶ or NaCl.⁶⁷ However, as pointed out by Aragones *et al.*, there is still room for improvement regarding such force fields for alkali halides in order to accurately predict e.g. melting points.⁶⁸ These authors conclude that polarizability, charge distribution and combination rules might hold the key for developing a phase transferable force field. Here, we explore various types of Van der Waals potentials, such as different types of Lennard-Jones potentials (12-6 and 8-6 LJ), and compare them to more elaborate ones, such as Buckingham (BK) ¹¹ and a modified Buckingham potential (WBK) ¹³ in order to implement an improved description of Van der Waals interactions in combination with a polarizable Gaussian charge distribution. Compared to point charges, Gaussian charge distributions provide a more physical model that is able to describe e.g. charge transfer, in particular in combination with polarizability. In addition, such a model contributes to a higher numerical stability during simulations due to smaller forces between atoms. The force field was derived systematically using Bayesian Monte Carlo (BMC) simulations⁶⁹,⁷⁰ with the parameters for the individual ions being the variables and a target function was minimised based on properties of all alkali halides at the same time.

In order to present our findings on alkali halides in a larger context, we compare them to simulation results obtained with other force fields such as the non-polarizable OPLS/AA, ¹⁸ the one published by Joung and Cheatham (JC), ¹⁹ the CHARMM Drude Force Field, based on a classical Drude oscillator (polarizable CHARMM), ²⁰ as well as to a more recently devel- oped polarizable force field employing Gaussian charge distributions (Kiss) ¹⁶ (see Table 1).

All force fields are tested by simulating ion pairs (gas phase) and solid crystals at room temperature. The best force fields are then examined at elevated temperature $(\geq T_m)$.

Table 1: The investigated force fields. The following abbreviations are used in the table: VdW: Van der Waals, pol: polarizability, LJ: Lennard-Jones, BK: Buckingham, WBK: Wang-Buckingham, PC: point charge, GC: Gaussian charge, LB: Lorentz-Berthelot. The combining rules refer to the combination of the individual ion parameters for the VdW interaction.

<table>
<thead>
<tr>
<th>force field</th>
<th>abbr. in this paper</th>
<th>VdW potential</th>
<th>charge</th>
<th>pol</th>
<th>combining rules</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="6">Reference force fields</td>
</tr>
<tr>
<td>OPLS/AA¹⁸</td>
<td>OPLS/AA</td>
<td>12-6 LJ</td>
<td>PC</td>
<td>no</td>
<td>geometric average</td>
</tr>
<tr>
<td>Joung and Cheatham¹⁹</td>
<td>JC</td>
<td>12-6 LJ</td>
<td>PC</td>
<td>no</td>
<td>LB</td>
</tr>
<tr>
<td>CHARMM Drude FF²⁰</td>
<td>pol-CHARMM</td>
<td>12-6 LJ</td>
<td>PC</td>
<td>yes</td>
<td>LB</td>
</tr>
<tr>
<td>Kiss and Baranyai¹⁶</td>
<td>Kiss</td>
<td>BK</td>
<td>GC</td>
<td>yes</td>
<td>Kong</td>
</tr>
<tr>
<td colspan="6">This work</td>
</tr>
<tr>
<td>Alexandria</td>
<td>WBK</td>
<td>WBK</td>
<td>GC</td>
<td>yes</td>
<td>Hogervorst</td>
</tr>
<tr>
<td>Alexandria</td>
<td>BK</td>
<td>BK</td>
<td>GC</td>
<td>yes</td>
<td>Kong</td>
</tr>
<tr>
<td>Alexandria</td>
<td>8-6 LJ</td>
<td>8-6 LJ</td>
<td>GC</td>
<td>yes</td>
<td>LB</td>
</tr>
<tr>
<td>Alexandria</td>
<td>12-6 LJ</td>
<td>12-6 LJ</td>
<td>GC</td>
<td>yes</td>
<td>LB</td>
</tr>
</tbody>
</table>

## Theory

### Force field model

In our polarizable force field the potential energy surface is represented by a set of predefined analytical functions accounting for the non-bonded interactions. The Coulomb potential features Gaussian charge distributions in combination with a core-shell model that allows for polarizability of the ions. The total charge of the ions (+/-1) is split up over a core and a shell with the core being positive and the shell being negative, following chemical intuition.

The Coulomb potential has the following functional form:⁷¹,⁷²

$$
V_{coul,GC}(r_{ij}) \ = \ \frac{1}{4\pi\epsilon_0} \frac{q_i q_j \mathrm{erf}\left(\beta_{ij} r_{ij}\right)}{r_{ij}} \tag{1}
$$

with the Coulomb constant $\frac{1}{4\pi\epsilon_0}$, the charge of the interacting sites $q_i$ and $q_j$, the error function $\text{erf}(x)$, the $\beta_{ij} = \frac{\beta_i\beta_j}{\sqrt{\beta_i^2+\beta_j^2}}$ characterising the Gaussian charge distribution, and the distance $r_{ij}$ between $q_i$ and $q_j$. The polarization energy between core and shell is described by a harmonic function$^{73}$

$$
V_{pol}(r_{cs}) \ = \ \frac{1}{4\pi\epsilon_0} \frac{q_s^2}{2\alpha}r_{cs}^2 \tag{2}
$$

with $q_s$ being the charge of the shell, $\alpha$ being the polarizability and $r_{cs}$ being the distance between core and shell.

The Van der Waals interactions are characterised by an attractive long-range $r^{-6}$ term, while for the description of the short-range Pauli repulsion different functional forms were tested. We applied 8-6 and 12-6 Lennard-Jones, as well as the Buckingham potential (for mathematical description see $SI$). All of these have the disadvantage of a singularity to either plus or minus infinity at very short distances. Wang et al.$^{13}$ have recently introduced a modified Buckingham potential that fixes this shortcoming:

$$
V_{WBK}(r) \ = \ \frac{2\epsilon}{1 - \frac{3}{\gamma+3}} \left(\frac{\sigma^6}{\sigma^6 + r^6}\right) \left[\frac{3}{\gamma + 3}e^{\gamma(1-\frac{r}{\sigma})} - 1\right] \tag{3}
$$

Here, $\sigma$ is the minimum energy distance, $\epsilon$ is the well depth and $\gamma$ is a dimensionless constant describing the steepness of the repulsion. The Wang-Buckingham potential has no singularity, tends to an attractive $r^{-6}$ term for long distances and a repulsive exponential term at short distances. To calculate the cross-coefficients for the Van der Waals pair interactions from the individual ion parameters, many different combining rules exist and these may have a significant impact on the short-range repulsive part (for the applied combining rules see $SI$, or Table 1).

## Optimisation of the parameters
We start from available experimental data for 20 alkali halide (AH) salts (solid phase) and ion pairs (gas phase). For each of the AHs the lattice constant $r_o$ is known with great

accuracy, $^{16,17,19,74}$ whereas other data such as the lattice energies may have considerable error bars (between different sources the difference can be as large as around $50\ kJ/mol$ for certain salts). $^{74-78}$ In the optimisation process we aim to reproduce interionic distances, vibrational frequencies, dipole moments and dissociation energies for the ion pairs with reasonable root-mean-square deviations (RMSDs), while still obtaining correct crystal densities. Due to the large error bars of the experimental lattice energies they have not been used in the force field parameterisation.

## Coulomb parameters

In the first step, the charge of core and shell, as well as the $\beta$ value characterising the Gaussian charge distribution, were optimised to reproduce experimental dipole moment values for AH ion pairs at experimental equilibrium distances $r_e$. The dipole moment $\vec{\mu}$ for the polarizable core-shell model can be calculated by $\vec{\mu} = \sum_{i=1}^{N} q_i \vec{r}_i$, with $q_i$ being the charge of the respective site and $\vec{r}_i$ being the position. The width of the Gaussian charge distribution was set equal on both core and shell. The Coulomb parameters, nine $\beta$ and nine $q_i$, were determined using a Bayesian Monte Carlo (BMC) algorithm by minimising

$$
\chi_{dipole}^2 = \frac{1}{N} \sum_{a \in A} \sum_{h \in H} \left[\vec{\mu}_{calc} - \vec{\mu}_{exp}\right]_{r_e}^2 \tag{4}
$$

using a home-built Python script, with N being the number of AHs. During the optimisation process, the Coulomb energy, force and force constant were monitored to give reasonable trends with the lowest possible $\chi_{dipole}^2$. The core positions were fixed at experimental equilibrium distances, while the positions of the shells were determined in each optimisation step by minimising the sum of Coulomb and polarization energy using the L-BFGS-B algorithm (from the Python SciPy library) for a given set of charge and $\beta$ values. Different available sets of polarizability values were tested, $^{16,20,39,79,80}$ showing that the polarizability has a significant impact on the result. The lowest $\chi_{dipole}^2$ was obtained with the quantum chemically

calculated polarizability values from Molina et al.⁷⁹ which was then selected for the rest of the parameterisation. In addition to the polarizability, the results are also very sensitive towards the $\beta$ values, while the charge values have a smaller influence, as was observed by Kiss et al.¹⁶

Van der Waals parameters

In the second step, the Van der Waals parameters were determined by optimising towards the ion pair dissociation energies $D_e$, interionic equilibrium distances $r_e$ and vibrational frequencies $\tilde{\nu}$, while maintaining accurate crystal densities. Considering the ion pairs, the force on each of the ions at equilibrium distance should be zero due to combination of the Coulomb, polarization and the Van der Waals interactions. The sum of those energies is equal to the dissociation energy $D_e$, i.e. the experimentally available dissociation energy $D_0$ that is corrected for the vibrational zero-point energy ($ZPE$). For the AHs, the $ZPE$ can be approximated with good accuracy with $ZPE = \frac{1}{2}h\tilde{\nu}.^{81,82}$ The elastic mode can be used as a proxy for the vibrational frequencies. As a first ansatz, the frequencies $\tilde{\nu}$ are considered to correspond to harmonic motions, which means they can be converted to force constants $k_{AH}$ using $\tilde{\nu} = \frac{1}{2\pi c}\sqrt{\frac{k_{AH}}{\mu_{AH}}}$ with $\mu_{AH}$ being the reduced mass of the AH ion pair. If we simultaneously approximate the energy function $V_{tot}$ as a harmonic function we can compute the following residual for the ion pairs:

$$
\begin{aligned}
\chi_{IP}^{2}= & \frac{1}{N} \sum_{a \in A} \sum_{h \in H} \omega_{D_{e}}\left[V_{t o t}(a, h, r_{e})-\left.D_{e}\right|_{r_{e}}]^{2}+\right. \\
& \omega_{r_{e}}\left[\frac{-\partial V_{t o t}(a, h, r_{e})}{\partial r_{e}}\right]_{r_{e}}^{2}+ \\
& \omega_{f c}\left[\frac{\partial^{2} V_{t o t}(a, h, r_{e})}{\partial r_{e}^{2}}-k_{a h}\right]_{r_{e}}^{2}
\end{aligned} \tag{5}
$$

with $\omega_x$ being optional weighting factors.

A further condition is that the interionic spacings $r_{AH}$ in all AH lattices correspond to free energy minima (the interionic spacing for the NaCl-like crystals is $r_{AH} = \frac{1}{2}r_o$ and

for the CsCl-like crystals it is $r_{AH} = \frac{1}{2}\sqrt{3}r_o$ with $r_o$ being the lattice constant). This condition is equivalent to requiring that the pressure in the model crystal is in equilibrium with the environment. In order to use this in parameter optimisation the pressure $p$ has to be computed from

$$
p = \frac{2}{3v} \left(E_{kin} - \Xi\right) \tag{6}
$$

where $v$ is the volume, $E_{kin} = \frac{3}{2}Nk_BT$ is the kinetic energy, $T$ the absolute temperature and $\Xi$ the virial, determined by

$$
\Xi = -\frac{1}{2}\sum_{i<j} r_{ij}F_{ij}. \tag{7}
$$

The total virial $\Xi_{tot}$ has contributions due to Van der Waals interactions $\Xi_{VdW}$ and Coulomb interactions $\Xi_{Coulomb}$, with $\Xi_{tot} = \Xi_{VdW} + \Xi_{Coulomb}$. The latter term is constant in the optimisation of Van der Waals parameters and was evaluated using a single point calculation in GROMACS$^{83}$ based on the particle-mesh Ewald algorithm.$^{84}$ The pressure $p$ is split into short-range and (analytical) long-range $p_{lr}$ contributions:

$$
p = \frac{2}{3v} \left(E_{kin} - \Xi_{tot}\right) + p_{lr} \tag{8}
$$

$$
p_{lr} = -\frac{4}{3}\pi \langle C_6 \rangle \rho^2 r_c^{-3} \tag{9}
$$

with $\langle C_6 \rangle$ the average dispersion constant, $\rho$ the particle density and $r_c$ the cut-off value for Van der Waals interactions. Note that the long range virial due to Coulomb interactions is included in $\Xi_{Coulomb}$ already.

The cohesive energy of a crystal, with $V_{tot} = V_{vdw} + V_{coul} + V_{pol}$, can be calculated by summing over all individual interactions of one ion with all surrounding neighbours following the principle of calculating the Madelung constant (see $SI$).$^{85,86}$ The forces $F_{ij}$ needed to compute the virial due to the Van der Waals interactions, Eqn. 7, can be computed in the same manner. Due to symmetry, the polarization energy is close to zero in a perfect crystal (at low temperature) and it is therefore neglected in the optimisation of the Van der Waals


parameters. There is, however, another contribution to the pressure due to vibrations of the ions in a NVT simulation, referred to as $p_{offset}$. This contribution is impossible to evaluate analytically due to the non-linear dependence of vibrations on the Van der Waals parameters, but it can be determined in an iterative fashion in cycles of parameter optimisation and NVT simulations. Given a reference pressure $p_{ref}$ to optimise the parameters against a further $\chi^{2}$ term can be formulated:

$$
\chi_{cryst}^{2} \ = \ \frac{\omega_{r_o}}{N} \sum_{a \in A} \sum_{h \in H} [p_{ref} - p - p_{offset}]_{r_{AH}}^{2} \. \tag{10}
$$

With this, the sum of $\chi_{IP}^{2}$ and $\chi_{cryst}^{2}$ can be minimised numerically. For all alkali halide ions ($Li^{+}$, $Na^{+}$, $K^{+}$, $Cs^{+}$, $F^{-}$, $Cl^{-}$, $Br^{-}$, $I^{-}$ ), there are 18 parameters ($\sigma_{ij}$, $\epsilon_{ij}$) using a Lennard-Jones $n-6$ potential and 27 parameters ($A_{ij}$, $B_{ij}$ and $C_{ij}$ or $\sigma_{ij}$, $\epsilon_{ij}$ and $\gamma_{ij}$) using a (modified) Buckingham potential. Those parameters together with 80 observables (20 salts with $D_e$, $r_e$, $\tilde{\nu}$ and $r_{AH}$) yield a well-behaved optimisation using a BMC algorithm implemented in a home-built Python script.

# Results and Discussion

## Force field parameters
For this work, parameters for two different Lennard-Jones potentials (12-6 and 8-6 LJ), a Buckingham (BK) and a modified Buckingham (Wang-Buckingham, WBK) potential were optimised. Simulation results using these potentials are compared to the reference force fields OPLS/AA, JC, pol-CHARMM and Kiss (Table 1). In Fig. 1, all Van der Waals parameters from this work, together with the parameters from the reference force fields are visualised. All optimised values and the applied polarizability values are tabulated in the *SI* Table S1. The different Van der Waals parameters from various force fields work in combination with different descriptions of Coulomb interactions (e.g. point charge *vs.* Gaussian charge) and

![](./images/812841474747006976_2.jpg)

Figure 1: Van der Waals parameters of all force fields. a) the sigma and b) epsilon values for the force fields that employ a LJ potential, together with the ones from the WBK potential. c) gamma for WBK only. d), e) and f) respectively show the A, B and C values from the force fields using a BK potential.

are employed in force fields that are either polarizable or non-polarizable. The force fields use different combining rules to calculate the cross-coefficients for the pair interactions from the ion parameters. It is therefore difficult to compare the parameters from the force fields directly.

Several tests were run using random starting values for the Van der Waals parameters to assess the reproducibility of the optimised parameters. Due to correlation between parameters, different combinations of e.g. epsilon and sigma for a LJ potential can give similar results. To obtain reproducible parameters we constrained e.g. the sigma values ( e.g. $\sigma_{Li^{+}} < \sigma_{Na^{+}}$ or $\sigma_{Li^{+}} < \sigma_{F^{-}}$). When doing so, one ends up with reproducible trends in the numerical values, although they can still vary due to direct and indirect correlation, that is, through the different salts that are modelled by the parameters. Each cation is involved

in four different salts, and the properties of each salt depend beyond other things on the combination of the cation and the anion values. This means that if one cation or anion value changes, this affects other salts that contain the same ion as well and thus the other counterion in that salt. Interestingly, we did not constrain the order of sigma values for the WBK potential, but obtained this order from the parameterisation process automatically.

# Different phases of alkali halides

At ambient conditions, alkali halides (AHs) are solid crystalline salts with a NaCl (LiF to CsF) or a CsCl (CsCl to CsI) crystal structure. At higher temperature and/or pressure other phases exist, such as molten salts, alkali halide vapours or the high pressure CsCl phase.⁷⁵ The goal of our force field is to be applicable to different phases, correctly predicting physical properties and phase transitions. For this purpose the force field was parameterised using experimental values from the gas and solid phase, as described in detail above. The parameters for the different salts are calculated from the individual optimised ion parameters using combining rules. The change in bond character between crystal and ion-pair of the alkali halides is therefore an extra challenge. The ionic bond character in the gas phase is calculated by the ratio of the experimental dipole moment over the theoretical dipole moment assuming point charges (Table S2). The ionicity varies between 65% and 85% (strongest for Lithium salts). In contrast, the bond character in the solid phase is in general more ionic and does not change as much as in the gas phase due to the additional electrostatic interaction in the crystal. The Van der Waals parameters of the individual ions will therefore reflect a compromise between the bond characters that vary with the alkali halides as well as with the different phases.

In the following sections the simulation results from alkali halide vapours (monomer) and crystalline salts at room temperature are discussed and compared to results from other reference force fields and experimental data. To investigate the phase transferability, we determine the density and potential energy of the alkali halides at the melting point temper-

ature for both the solid and the melt, the heat of fusion, the surface tension, the electrical conductivity as well as self-diffusion constants at temperatures above the melting point for the best force fields. All MD simulations were performed using the GROMACS simulation software (for further details on the simulations see $SI$).

As a measure for the predictive power of the force fields, RMSD values are given. For better comparison of the various physical properties, we also report normalised RMSDs (NRMSDs) in percent; the RMSD values are normalised towards the arithmetic mean of the experimental data $\bar{y}$ with $\text{NRMSD} = 100\ (\text{RMSD}\ /\ \bar{y})$. Table 2 summarises all RMSD and NRMSD values. Note that the gas and solid phase properties have been calculated for all tested force fields, while the properties at elevated temperature were just determined for the best reference force fields, JC and Kiss, and our new force field WBK.

**Table 2:** RMSD (R) and NRMSD (%) values for gas and solid phase properties for all tested force fields, and high temperature properties calculated for JC, Kiss and WBK. For the gas phase: the interionic distance $r_e$, dissociation energy $D_e$, the frequency $\tilde{\nu}$ and dipole moment $\mu$; for the solid phase: the density $\rho$ and lattice energy $V_{lattice}$ at RT and $T_m$; for the liquid phase: the density $\rho$, the potential energy $V$, surface tension $\sigma$, electrical conductivity $\kappa_{NE}$ and the self-diffusion coefficient $D$. Also heat of fusion $\Delta H_{fus}$ is listed. * Evaluated for 9 salts (LiF, LiCl, NaCl, KF, KCl, KBr, RbCl, RbBr and CsF). ** Evaluated for 4 salts (NaCl, NaI, RbCl and CsCl).

<table>
  <thead>
    <tr>
      <th rowspan="2">property</th>
      <th colspan="8">Reference force fields</th>
      <th colspan="4">Force fields from this research</th>
    </tr>
    <tr>
      <th colspan="2">OPLS/AA</th>
      <th colspan="2">JC</th>
      <th colspan="2">pol-CHARMM</th>
      <th colspan="2">Kiss</th>
      <th colspan="2">BK</th>
      <th colspan="2">LJ 8-6</th>
      <th colspan="2">LJ 12-6</th>
      <th colspan="2">WBK</th>
    </tr>
    <tr>
      <th></th>
      <th>R</th>
      <th>%</th>
      <th>R</th>
      <th>%</th>
      <th>R</th>
      <th>%</th>
      <th>R</th>
      <th>%</th>
      <th>R</th>
      <th>%</th>
      <th>R</th>
      <th>%</th>
      <th>R</th>
      <th>%</th>
      <th>R</th>
      <th>%</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>$r_e$ [pm]</td>
      <td>14</td>
      <td>5.6</td>
      <td>17</td>
      <td>6.6</td>
      <td>10</td>
      <td>4.0</td>
      <td>22</td>
      <td>8.4</td>
      <td>6</td>
      <td>2.3</td>
      <td>5</td>
      <td>2.1</td>
      <td>9</td>
      <td>3.5</td>
      <td>3</td>
      <td>1.2</td>
    </tr>
    <tr>
      <td>$D_e$ [kJ/mol]</td>
      <td>32.8</td>
      <td>6.3</td>
      <td>36.3</td>
      <td>7.0</td>
      <td>65.4</td>
      <td>12.5</td>
      <td>27.2</td>
      <td>5.2</td>
      <td>20.5</td>
      <td>3.9</td>
      <td>15.3</td>
      <td>2.9</td>
      <td>15.1</td>
      <td>2.9</td>
      <td>20.6</td>
      <td>3.9</td>
    </tr>
    <tr>
      <td>$\tilde{\nu}$ [cm⁻¹]</td>
      <td>132</td>
      <td>38.5</td>
      <td>121</td>
      <td>35.4</td>
      <td>316</td>
      <td>91.9</td>
      <td>166</td>
      <td>48.3</td>
      <td>35</td>
      <td>10.2</td>
      <td>70</td>
      <td>20.3</td>
      <td>129</td>
      <td>37.6</td>
      <td>36</td>
      <td>10.6</td>
    </tr>
    <tr>
      <td>$\mu$ [D]</td>
      <td>3.62</td>
      <td>38.9</td>
      <td>3.79</td>
      <td>40.7</td>
      <td>1.80</td>
      <td>19.3</td>
      <td>1.43</td>
      <td>15.4</td>
      <td>0.49</td>
      <td>5.2</td>
      <td>0.37</td>
      <td>4.0</td>
      <td>0.59</td>
      <td>6.4</td>
      <td>0.38</td>
      <td>4.0</td>
    </tr>
    <tr>
      <td>average NRMSD</td>
      <td colspan="2">22.3 %</td>
      <td colspan="2">22.4 %</td>
      <td colspan="2">31.9 %</td>
      <td colspan="2">19.3 %</td>
      <td colspan="2">5.4 %</td>
      <td colspan="2">7.3 %</td>
      <td colspan="2">12.6 %</td>
      <td colspan="2">5.0 %</td>
    </tr>
    <tr>
      <td>gas phase</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>$\rho_{solid,RT}$ [kg/m³]</td>
      <td>397</td>
      <td>12.1</td>
      <td>75</td>
      <td>2.3</td>
      <td>941</td>
      <td>28.7</td>
      <td>340</td>
      <td>10.4</td>
      <td>24</td>
      <td>0.7</td>
      <td>32</td>
      <td>1.0</td>
      <td>32</td>
      <td>1.0</td>
      <td>2</td>
      <td>0.1</td>
    </tr>
    <tr>
      <td>$V_{lattice,RT}$ [kJ/mol]</td>
      <td>35.1</td>
      <td>4.7</td>
      <td>13.3</td>
      <td>1.8</td>
      <td>34.2</td>
      <td>4.5</td>
      <td>13.6</td>
      <td>1.8</td>
      <td>13.4</td>
      <td>1.8</td>
      <td>15.3</td>
      <td>2.0</td>
      <td>19.7</td>
      <td>2.6</td>
      <td>15.5</td>
      <td>2.1</td>
    </tr>
    <tr>
      <td>average NRMSD</td>
      <td colspan="2">8.4 %</td>
      <td colspan="2">2.0 %</td>
      <td colspan="2">16.6 %</td>
      <td colspan="2">6.1 %</td>
      <td colspan="2">1.3 %</td>
      <td colspan="2">1.5 %</td>
      <td colspan="2">1.8 %</td>
      <td colspan="2">1.1%</td>
    </tr>
    <tr>
      <td>solid ph. at RT</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>$\rho_{s,T_m}$ [kg/m³]</td>
      <td>171</td>
      <td>5.8</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>362</td>
      <td>12.3</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>105</td>
      <td>3.6</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>$V_{s,T_m}$ [kJ/mol]*</td>
      <td>19.9</td>
      <td>2.6</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>12.5</td>
      <td>1.6</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>7.6</td>
      <td>1.0</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>$\rho_{liq,T_m}$ [kg/m³]</td>
      <td>152</td>
      <td>6.2</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>330</td>
      <td>13.5</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>176</td>
      <td>7.2</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>$V_{liq,T_m}$ [kJ/mol]*</td>
      <td>16.1</td>
      <td>2.2</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>10.7</td>
      <td>1.5</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>12.3</td>
      <td>1.7</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>$\Delta H_{fus}$ [kJ/mol]</td>
      <td>7.5</td>
      <td>31.3</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>12.6</td>
      <td>52.7</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>4.4</td>
      <td>18.3</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>$\sigma$ [dyn/cm]</td>
      <td>18.5</td>
      <td>17.1</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>65.3</td>
      <td>60.2</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>34.5</td>
      <td>31.8</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>$\kappa_{NE}$ [S/cm]</td>
      <td>2.0</td>
      <td>62.5</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>2.3</td>
      <td>73.7</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>1.3</td>
      <td>40.9</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>$D$ [$10^{-5}\ cm^2/s$]**</td>
      <td>2.9</td>
      <td>42.5</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>2.0</td>
      <td>29.8</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>1.1</td>
      <td>16.6</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>average NRMSD</td>
      <td colspan="2">21.3 %</td>
      <td colspan="2"></td>
      <td colspan="2"></td>
      <td colspan="2">30.7 %</td>
      <td colspan="2"></td>
      <td colspan="2"></td>
      <td colspan="2">15.1 %</td>
      <td colspan="2"></td>
    </tr>
    <tr>
      <td>liq. & s. ph. at $T_m$</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>average NRMSD</td>
      <td colspan="2">15.4 %</td>
      <td colspan="2">12.2 %</td>
      <td colspan="2">24.3 %</td>
      <td colspan="2">12.7 %</td>
      <td colspan="2">3.4 %</td>
      <td colspan="2">4.4 %</td>
      <td colspan="2">7.2 %</td>
      <td colspan="2">3.1 %</td>
    </tr>
    <tr>
      <td>all ph. w/o and w high temp. data</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td colspan="2"></td>
      <td colspan="2">15.2 %</td>
      <td colspan="2"></td>
      <td colspan="2">18.7 %</td>
      <td colspan="2"></td>
      <td colspan="2"></td>
      <td colspan="2"></td>
      <td colspan="2">7.1 %</td>
    </tr>
  </tbody>
</table>

### Gas phase

The molecular composition of alkali halide vapours is mainly comprised of monomers $AH$, also referred to as diatomic molecule or ion pair. Depending on temperature and pressure, a significant fraction of the vaporised salt can exist as dimers $(AH)_2$, and for NaF, LiCl and LiBr even trimers $(AH)_3$ have been observed. $^{87,88}$ In the parameterisation, physical properties from monomers were used, and here we report simulation results for this species.

Interionic distance In Fig. 2 (a & b) the interionic distances of the AH ion pairs are plotted *vs.* the respective salt that are ordered by the alkali ions. The experimental cation-anion distances (black solid line) scale with the respective alkali and halide ion, and increase from lithium to cesium as well as from fluoride to iodide. Our new force fields closely reproduce the experimental interionic distances with RMSD between 3 and 6 pm (WBK and BK, Table 2). The 12-6 LJ shows a larger deviation (RMSD of 9 pm) and the same goes for the reference force fields (RMSDs from 10 to 22 pm, Table 2). In particular the Kiss force field shows a systematic overestimation of the interionic distances, suggesting that the repulsive part of the potential energy curves is too steep.

The dissociation energy, vibrational frequency and dipole moment, that were evaluated from the simulations are dependent on the interionic distance. The reported values correspond to the interionic distances determined by the force field.

Dissociation energy Fig. 2 (c & d) shows the potential energy of the AH ion pairs that equals the experimental dissociation energy corrected for the $ZPE$, *i.e.* $D_e$. The dissociation energy, which is the sum of the Coulomb, Van der Waals and polarization energy, follow the same ion-dependency as the interionic distances: with increasing size of the alkali and halide ion, the dissociation energy gets less negative. The tested force fields predict this trend correctly but differ in their accuracy. The lowest RMSD values are observed for our new force fields between 15.1 $kJ/mol$ (12-6 LJ) to 20.6 $kJ/mol$ (WBK), while for the reference force

![](./images/812841474747006976_3.jpg)

Figure 2: Distances, dissociation energies, vibrational frequencies and dipole moments for ion pairs (a, c, e and g: reference force fields and b, d, f and h: this research). For plots that show the differences relative to experimental data see SI Figure S2 and for the tabulated values Table S3-6. Experimental data is from the following references: interionic distances, $^{89}$ dissociation energies, $^{90}$ vibrational frequencies, $^{90-92}$ dipole moments. $^{89}$

fields RMSDs between 27.2 $kJ/mol$ (Kiss) and 65.4 $kJ/mol$ (pol-CHARMM) are observed (Table 2). The $D_e$ are systematically overestimated (too strong bonds) by pol-CHARMM, and underestimated (too weak bonds) by OPLS/AA and JC. The Kiss force field lies in between, however it should be kept in mind that the values correspond to interionic distances that overestimates the experimental values in general. Our new force fields reproduce the dissociation energies $D_e$ closely for the Li-, Na- and Cs-salts, but overestimate the bond strengths slightly for K- and Rb-salts.

It is worth noticing that the dissociation energy is better described by the more repulsive LJ potentials than by the softer BK or WBK. This is related to the fact that the dissociation energy was optimised simultaneously with other properties such as e.g. the vibrational frequencies. According to Werhahn et al.$^{14,31}$ all of the here investigated VdW potentials have difficulties to accurately capture both the short and long range part of the corresponding potential energy surface: a more accurate description of the repulsive wall can lead to an inaccurate description of the long range and even the area around the minimum. As the LJ potential has an intrinsic deficiency in describing the repulsive part accurately, they are able to capture the potential's minimum better. In contrast, the softer potentials are much better in describing properties that are related to the repulsive part of the potential (e.g. vibrational frequency, see below), but have a slightly worse description of the potential's minimum (i.e. the dissociation energy). Xantheas and Werhahn$^{14,15}$ showed that by introducing an additional parameter in these VdW potentials it is possible to improve this issue.

Vibrational frequency In Fig. 2 (e & f) the simulated vibrational frequencies of the AH ion pairs are compared to experimental data. The experimental frequencies are highest for lithium salts and decrease towards caesium salts, and in each alkali series from fluoride to iodide. This trend is predicted by all force fields, except for Kiss that has difficulties in particular for lithium and sodium salts. All force fields tend to overestimate the experimental frequencies, especially for lithium salts. The new force fields perform well with RMSD values

between $35\ cm^{-1}$ (BK) to $129\ cm^{-1}$ (12-6 LJ) compared to the reference force fields with RMSDs from $121\ cm^{-1}$ (JC) to $316\ cm^{-1}$ (pol-CHARMM). As mentioned earlier, in alkali halide vapours an appreciable amount of dimers and trimers exists in addition to monomers. The fraction of such dimers and trimers is largest for lithium and fluoride salts and decreases towards caesium and iodide salts,⁸⁷ and complicates the measurements for the lighter alkali halides, leading to larger experimental errors.⁹² One possible explanation for the systematic overestimation of the vibrational frequencies of the lighter alkali halides with all force fields could be partially due to this larger experimental error. On the other hand, an intrinsic deficiency of the force fields to capture the true curvature of the potential energy surface at short interionic distances could be responsible as well.

All reference force fields have quite large RMSD values for the vibrational frequencies, which is partially due to the fact that most of them employ a 12-6 LJ potential. Both polarizable reference force fields, pol-CHARMM and Kiss, have a higher RMSD value for the frequencies than the simpler non-polarizable force fields OPLS/AA and JC. This suggests that both Kiss and pol-CHARMM have inaccurate curvatures of the potential energy surface at those interionic distances. The higher RMSD cannot be attributed to the fact that they are polarizable, as shown by the results from our force fields.

Dipole moment Fig. 2 (g & h) displays the dipole moments that were determined from simulation in comparison to experimental values. The dipole moment increases from lithium to caesium salts, and in each alkali halide series from fluoride to iodide, and is directly proportional to the interionic distance. As the correct prediction of the dipole moment is closely related to considering the ion's polarizability, it is not surprising that non-polarizable force fields perform poorest with a RMSD of 3.62 D (OPLS/AA) and 3.79 D (JC), since these potentials model the theoretical 100% ionicity (Table S2). However, the other reference force fields that do implement polarizability show a high RMSD of 1.43 D (Kiss) and 1.80 D (pol-CHARMM) as well. In comparison, the dipole moments that are predicted using our new

polarizable force fields, follow the experimental data with RMSD values between 0.37 D (8-6 LJ) to 0.59 D (12-6 LJ). In fairness, it has to be pointed out that none of the reference force fields were optimised for reproducing gas-phase properties, but rather to give correct results for properties of one ion in combination with water (like hydration free energies and intermolecular-ion distances).

Our force fields give an accurate description of the physico-chemical properties of the ion pairs. The investigated gas phase properties are predicted with an average NRMSD of 5% (WBK), 5.4% (BK), 7.3% (8-6 LJ) and 12.6% (12-6 LJ) in comparison to the investigated reference force fields (average NRMSD of 19.3% (Kiss), 22.3% (OPLS/AA), 22.4% (JC) and 31.9% (pol-CHARMM)). Without the vibrational frequencies, the average NRMSD for our force fields is between 3% (WBK and 8-6 LJ) and 4.3% (12-6 LJ), indicating that this is the physico-chemical property that is most affected by the choice of the Van der Waals potential. Comparing vibrational frequencies calculated with the two tested LJ potentials, it is clear that the softer 8-6 LJ potential performs better than the commonly applied more repulsive 12-6 LJ potential. The even softer BK and WBK potential perform almost equally well and have a significantly improved RMSD value (approx. factor of 4 compared to the 12-6 LJ).

For the other properties (interionic distance, dissociation energy and dipole moment), the choice of the Van der Waals potential does not seem to have such a significant influence. However, the resulting dipole moment depends not only on the included polarizability but also on properly balanced Coulomb and Van der Waals forces that determine the distance between the two ions. This becomes evident if one compares the resulting dipole moments from the reference force fields to our own results (Fig. 2 g & h) and to theory (Table S2). It can be concluded that it is difficult to completely disentangle the contributions and effects from the Van der Waals and Coulomb interaction and from polarization to a certain physico-chemical property.

### Solid phase

At ambient conditions, most alkali halides crystallise with a NaCl structure (face-centred cubic), while caesium chloride, bromide and iodide assume the CsCl crystal structure (body-centred cubic). At higher pressure or temperature, phase transitions can occur. For example, CsCl transforms to the NaCl structure at higher temperatures, while NaCl, K-halides, and Rb-halides transform to the CsCl structure at higher pressures.⁷⁵,⁹³ In the following section the simulation results at ambient conditions on density, stability of the crystal structure and lattice energy of the alkali halides are reported and compared to experimental data.

Density The simple trends that were observed for the gas phase properties do get more complex in condensed phase: the experimental solid densities (Fig. 3 a & b) increase in each alkali series, except for the alkali fluorides that show a higher density than expected from this trend. In all cases the difference from the trend is around $1000\ kg/m^3$. In conjunction with this, the lattice energy is about $150\ kJ/mol$ lower than suggested by the trend. The different force fields capture this behaviour with different accuracy. For some of the tested reference force fields the salts get amorphous, liquid or change the crystal structure during the NPT simulation (Kiss: LiI; OPLS/AA: LiCl, LiBr and CsI; pol-CHARMM: LiCl, LiBr, LiI, NaBr and NaI) as can be evaluated by determining, for example, radial distribution functions. From the reference force field both Kiss and JC were optimised to give satisfying crystal densities, while pol-CHARMM and OPLS/AA were only optimised for the interaction with water. That special care has to be taken to retain the crystal structure was discussed and investigated by Joung and Cheatham who showed that certain combinations of sigma and epsilon values using a 12-6 LJ potential can result in unstable crystals.¹⁹ With our new force fields all salts retain the correct crystal structure during simulation. While the reference force fields have RMSDs for the densities between $75\ kg/m^3$ (JC) and $941\ kg/m^3$ (pol-CHARMM), that are partially that high due to the loss of the crystal structure, our new force fields have unprecedented RMSD values of $2\ kg/m^3$ (WBK) to $32\ kg/m^3$ (LJ, both

![](./images/812841474747006976_4.jpg)

Figure 3: Room temperature solid phase densities and lattice energies of alkali halides at ambient conditions (a and c: reference force fields and b and d: this research). For plots that show the differences relative to experimental data see $SI$ Figure S3 and for the tabulated values Table S7 and S8. Experimental data is from the following references: densities (calculated from the lattice constants) $^{75}$ and lattice energies at room temperature. $^{76}$

8-6 and 12-6). The force fields from this research were optimised towards the pressure at constant volume which is the reason why such low density RMSD values are obtained (see SI).

Lattice energy In Fig. 3 (c & d) the lattice energies from NPT simulations are shown for the different force fields and compared to experimental data.⁷⁶ Within each alkali halide series, the lattice energies get less negative from fluoride to iodide, indicating the highest bond strength for LiF and the weakest for CsI. Most of the force fields follow the experimental data reasonably well; it is interesting to notice that the potential energy seems to be relatively insensitive towards the loss of the crystal structure (see e.g. LiI from Kiss). The reference force fields have RMSDs between 13.3 $kJ/mol$ (JC) and 35.1 $kJ/mol$ (OPLS/AA). We would like to point out that the lattice energies were not included in the optimisation process of our parameters for the alkali halides. The RMSD values for the lattice energy using our new force fields is between 13.4 $kJ/mol$ (BK) and 19.7 $kJ/mol$ (12-6 LJ).

While the reference force fields from Kiss and JC were optimised towards one set of lattice energies, we chose not to do so, because there is a rather large spread in the available experimental data. Still, the RMSDs of the lattice energies from this research are satisfying, even more so if compared to several sets of experimental lattice energies. While the lattice energies of the WBK force field lie in the middle of all experimental data,⁷⁴⁻⁷⁸ the lattice energies of Kiss and JC reproduce the data set they were optimised for, however compared to other data sets they show larger deviations than our WBK force field.

Our simulation results for the reference force fields JC and Kiss can be compared to the respective author's own simulations of AH crystals at RT. In general we have very good agreement, with two exceptions. For Kiss we observed that the density value for LiI given in their paper is not equilibrated, which is why our value shows a larger deviation. For JC we could perfectly reproduce the density (calculated from their interionic distances), but we obtained a lower RMSD for the lattice energies (13.3 vs. 17.6 $kJ/mol$). While

we determined the lattice energy from NPT simulations, they chose to calculate the lattice energy from perfect cubic crystals. The lattice constant was increased from zero, thereby the potential energies decreased and passed through a minimum. The authors set this minimum in the potential energy curve equal to the lattice energy.

Overall, our new force fields perform very well, predicting the tested solid state properties (density and lattice energy) at ambient conditions with an average NRMSD of 1.1% (WBK), 1.3% (BK), 1.5% (8-6 LJ) and 1.8% (12-6 LJ) with the additional benefit that all AH crystal structures are stable during simulation. In comparison the reference force fields have average NRMSD values of 2.0% (JC), 6.1% (Kiss), 8.4% OPLS/AA and 16.6% (pol-CHARMM).

Regarding the influence of the Van der Waals description, it can be stated that the WBK potential gives a very low RMSD for the density at ambient conditions, while good results were also obtained with the other tested Van der Waals potentials, with the LJ potentials giving the poorest results. It should be mentioned that the BK potential is rather tricky in the optimisation, and care has to be taken to obtain physically reasonable potential energy surfaces for all pair interactions that otherwise can lead to crashing MD simulations.

Combining the average NRMSD values from gas and solid phase, JC (12.2%) and Kiss (12.7%) perform best among the investigated reference force fields (OPLS/AA: 15.4%, pol-CHARMM: 24.3%). The combined average NRMSD values from this research result in 3.1% (WBK), 3.4% (BK), 4.4% (8-6 LJ) and 7.2% (12-6 LJ). Based on this we decided to further evaluate just the force fields JC, Kiss and WBK at elevated temperatures ($\geq T_m$).

# High temperature solid phase and molten salts

In order to test the transferability of the best force fields for the solids at higher temperatures, we performed simulations at the melting point temperature of the respective AH, and inspected the resulting density (see Fig. 4, a & b), lattice energy and the crystal structure. None of the tested force fields was optimised for reproducing properties at elevated temperatures.

![](./images/812841474747006976_5.jpg)

![](./images/812841474747006976_6.jpg)

![](./images/812841474747006976_7.jpg)

![](./images/812841474747006976_8.jpg)

![](./images/812841474747006976_9.jpg)

![](./images/812841474747006976_10.jpg)

Figure 4: High temperature solid (a) and liquid (c) phase densities of alkali halides at the melting point at ambient pressure and the differences to the experimental values (b & d) for the force field of Kiss, JC and our new force field WBK. Liquid phase radial distribution function $g(r)$ for (e) $Li^+-I^-$ (for WBK, JC and Kiss) after 1ns, and (f) NaCl (for WBK); the dotted vertical lines at the first peak(s) in e & f indicate experimental values. The data is tabulated in the $SI$ in Table S9 and S10. Experimental data is from the following reference: densities of the crystals and melts at $T_m.^{94}$

Density and lattice energy of the crystal The simulations were carried out starting from the correct experimental densities and crystal structures for the given temperature, i.e. the AHs from LiF to CsCl have the NaCl crystal structure, while CsBr and CsI have the CsCl structure. The WBK force field reproduces the experimental density of the AHs at such high temperatures quite well, with an RMSD of 105 $kg/m^3$. Larger deviations are observed for the salts CsBr and CsI that reside in the CsCl crystal structure; this observation also holds for the reference force fields. It should be mentioned that the reference density values for CsBr and CsI are calculated estimates,⁹⁴ as no experimental data was available. The RMSD value excluding the salts in CsCl structure results in 40 $kg/m^3$. In addition to the density, the lattice energy at $T_m$ was evaluated for 9 salts (LiF, LiCl, NaCl, KF, KCl, KBr, RbCl, RbBr and CsF) with a RMSD from experiment⁹⁵ of 7.6 $kJ/mol$ (see SI, Table S11). All salts are stable and retain the experimentally observed crystal structure.

In comparison, simulations using the reference force fields from Kiss and JC do not maintain the original crystal structure for certain salts. For Kiss, both, LiF and NaF melt, and in addition LiI, which gets amorphous at ambient conditions, forms some kind of irregular CsCl crystal structure in simulations at $T_m$. The fact that LiF and NaF melt at the melting point while performing a bulk simulation (i.e. applying three-dimensional boundary conditions) proves that the melting point temperature of this force field underestimates the experimental melting point temperature by at least 20 - 30%. This conclusion is derived from the fact that the physical break-down temperature, i.e. the temperature at which a material melts without any nucleation site for melting, lies approximately 20 - 30% above the melting point.⁹⁶ Besides those salts (LiF, LiI and NaF), the reference force field Kiss is in agreement with the experimental data with a RMSD of 362 $kg/m^3$. The RMSD of the lattice energy for the 9 salts that are listed above is 12.5 $kJ/mol$. The non-polarizable JC force field also shows a good agreement with the experimental data, however LiI undergoes structural changes during the NPT simulation that finally leads to a different crystal structure. For JC, the RMSD value of the density is 171 $kg/m^3$ and the RMSD of the lattice energy for those 9

salts is 19.9 $kJ/mol$.

Density and potential energy of the melt Simulations of the liquid phase at $T_m$ were performed as well for the WBK, JC and Kiss force fields. The trend in the density of the melted salts is captured by all force fields (Fig. 4, c & d). The RMSD of the densities is 176 $kg/m^3$ for WBK, 152 $kg/m^3$ for JC and 330 $kg/m^3$ for Kiss. Note that LiI simulated with Kiss actually solidifies again at the experimental melting point temperature, after being a melt for approximately 1 ns. The potential energy of the melt was evaluated for the 9 salts listed above, and the RMSD values are 12.3 $kJ/mol$ for WBK, 16.1 $kJ/mol$ for JC, and 10.7 $kJ/mol$ for Kiss (see SI, Table S12). Regarding the densities of the salt at $T_m$, both JC and our WBK give a better description than Kiss. The potential energies of the lattice and the melt at $T_m$ from Kiss and our WBK force field give very satisfying results for the 9 salts that were evaluated, while a slightly worse description is obtained with JC.

Radial distribution function of the melt An analysis of radial distribution functions (RDF) of the melts revealed that there is a structural difference in the simulated melts depending on the applied force field: for the salts LiCl, LiBr and LiI (Fig. 4), the second peak in the cation-anion RDF shows an apparent substructure for Kiss that is associated with a short-range local order; for JC the second peak is broadened in the NPT simulation for those salts, and the substructure is more evident in the constant volume simulation; with WBK no substructure is observed (see inset in Fig. 4e). There does not seem to be any evidence of such a substructure in the second peak of the g(r)_{+-} in the experimental data.⁹⁷ Other simulations of lithium melts using e.g. Tosi-Fumi or Michielsen's parameters do not provide this feature either.⁹⁸,⁹⁹ A prolonged simulation (up to 4 ns) of LiI using Kiss reveals that the observed structure is indeed a precursor state to a layered structure that is still observed at 100 K above the experimental melting point, with diffusion coefficients close to zero. In Fig. 4f all RDFs for NaCl are plotted for WBK, showing good agreement with experimental data.¹⁰⁰,¹⁰¹

![](./images/812841474747006976_11.jpg)

![](./images/812841474747006976_12.jpg)

![](./images/812841474747006976_13.jpg)

![](./images/812841474747006976_14.jpg)

![](./images/812841474747006976_15.jpg)

![](./images/812841474747006976_16.jpg)

Figure 5: Heat of fusion values of the alkali halides at $T_{m,exp}$, as well as surface tension and electrical conductivity of the melts at $100\ K$ above the experimental melting point (a, c & e) and the differences to the experimental values (b, d & f) for the force field of Kiss, JC and our new force field WBK. Note that the melted LiI simulated with Kiss solidified again. The data is tabulated in the $SI$ in Table S13-S15. Experimental data is from the following references: heat of fusion, $^{102}$ surface tension, $^{103}$ electrical conductivity. $^{104}$

To further investigate the high temperature physico-chemical properties, also the heat of fusion at $T_{m,exp}$, as well as the surface tension and electrical conductivity of the melts at 100 K above the experimental melting point were determined (see Fig. 5).

Heat of fusion The heat of fusion is the amount of energy (enthalpy) added to melt a substance without a change in temperature. Here, we calculate the $\Delta H_{fus}$ from the respective simulations of the crystals and melts at the experimental melting point and compare it to the experimental heat of fusion values (Fig. 5, a & b). The $\Delta H_{fus}$ values follow the zig-zag trend, *i.e.* in general the values are higher for the fluoride-salt and drop towards the iodide-salt for a certain cation; the values of CsBr and CsI are higher than expected from this trend. All force fields have difficulties to predict this trend for all of the salts: Kiss deviates in particular for the salts where the crystal melts (even though they should be stable), *i.e.* LiF and NaF (see above for more details) and shows in general the opposite trend. Both, JC and WBK have an increased accuracy, but show an opposite trend for the Cs-salts, *i.e.* CsBr and CsI are lower than CsF and CsCl even though they should be higher. The RMSD is 12.6 $kJ/mol$ for Kiss (8.6 $kJ/mol$ without LiF, LiI, and NaF), 7.5 $kJ/mol$ for JC and 4.4 $kJ/mol$ for WBK.

Surface tension The surface tension is an important interfacial property that reflects beyond other things the surface composition that can differ from the one in the bulk, in particular if polarizable ions are involved. The surface tension $\sigma$ can be evaluated from MD simulations through the following equation

$$
\sigma = \frac{L_z}{2} \left( \langle \Pi_{zz} \rangle - \frac{\langle \Pi_{xx} \rangle + \langle \Pi_{yy} \rangle}{2} \right) \tag{11}
$$

where $L_z$ is the length of the simulation box in z-direction and $\langle \Pi_{xx,yy,zz} \rangle$ are the diagonal elements of the average pressure tensor. The surface tension of alkali halides is highest for the fluoride-salts and drops towards the iodide-salts for a certain cation, with experimental

values between 69 to 240 $dyn/cm$ (Fig. 5, c & d). This overall trend is captured for most of the salts by all tested force fields, with the exception of Kiss that has difficulties for the lithium-salts. Here, the surface tension of LiF, LiCl and LiBr is significantly underestimated, and for LiI that has solidified a negative surface tension is observed. $^{105}$ The RMSD values are 65.3 $dyn/cm$ (54.5 $dyn/cm$ without LiI) for Kiss, 34.5 $dyn/cm$ for WBK and 18.5 $dyn/cm$ for JC. In general the polarizable models give lower surface tension values in comparison to non-polarizable models, which is in line with what was observed before. $^{106}$ As discussed in literature, there are simulation parameters that can affect the surface tension value, as e.g. the system's interface area $^{107}$ or the truncation of the dispersion. $^{58,106,108}$ Finite size effects can be investigated by simulating different interface areas, and the bulk value can be extrapolated by fitting the data. $^{107}$ The bulk value is lower in comparison to surface tension values that are measured in systems that are affected by finite size effects; for the studied system's interface area we estimate that the bulk value should lie approximately 5% lower than the reported value. In contrast, the truncation of the dispersion can change the surface tension more severely, and in general it is recommended to use full Ewald summation also for dispersion. $^{58,106}$ Aguado and Madden reported that with truncation of the dispersion that corresponds to half of the box-size, the surface tension value is 14% lower than the value calculated with full Ewald summation of the dispersion. $^{106}$ Here, instead of full Ewald summation, we employ long-range dispersion correction after the cut-off. Fischer *et al.* report that the difference in surface tension between full Ewald summation of the dispersion interactions *vs.* applying a cut-off of 1.1 nm can be significant; the surface tension is approx. 30% higher using Ewald summation. $^{55,58}$ Zubilliaga *et al.* investigated the influence of the cut-off length of the dispersion interactions on surface tension, and found that the surface tension converges at a cut-off length of 2.3 nm. $^{108}$ Fisher *et al.* showed that the values of Zubilliaga *et al.* are virtually identical to the ones calculated using PME for the dispersion. For our surface tension data a cut-off between 1.0 nm and 1.8 nm was applied, depending on the respective salt. This implies that the true values lie most likely approx. 15 - 25% higher

than what is shown in Fig. 5 c and listed in Table S14. An increase in the surface tension data by 15 - 25% would lead to hypothetical RMSD values of 61.3 - 59.6 dyn/cm for Kiss, 29.0 - 39.1 dyn/cm for JC and 25.9 - 22.7 dyn/cm for WBK.

Electrical conductivity The electrical conductivity $\kappa$ of the salt melts is a physico- chemical property that reflects the dynamics of the ions in the bulk. There are different methods to estimate the conductivity from MD simulations employing e.g. the Nernst- Einstein (NE) equation using diffusion coefficients, the Green-Kubo (GK) time integral of the electric-current autocorrelation function, or the Einstein-Helfand (EH) formula that is based on the translational dipole moment. $^{33,109-111}$ The latter two are in general more ac curate as they account for ionic correlation effects, while the NE-approach gives an upper bound value of the conductivity. The NE-approach calculates the electrical conductivityfrom the summation of the cationic and anionic self-diffusion coefficients $D_{+/-}$ (in $m^{2} / s$ )

$$
\kappa_{N E}=\frac{N_{p a i r} e^{2}}{V k_{B} T}\left(q_{+}^{2} D_{+}+q_{-}^{2} D_{-}\right) \tag{12}
$$

with

$$
D_{i}=\frac{1}{6 t} \lim _{t \rightarrow \infty}\left\langle\left|r_{i}(t)-r_{i}(0)\right|^{2}\right\rangle. \tag{13}
$$

Here $q_{+/-}^{2}$ is qual to 1 , e is the electric charge $1.60 * 10^{-19} C, V$ is the volume of the simulation box, $N_{pair }$ is the number of ion pairs, and $k_{B}$ is the Boltzmann constant 1.38 * $10^{-23} ~J / K$ . In cases with neglectable ion correlation effects, there can be an agreementbetween the conductivity determined using the NE-approach and e.g. the EH-method. $^{111,112}$  From molten $LiCl,^{113} NaCl,^{114} KF^{43}$ and $KCl^{43,113}$ simulations it was concluded that the degree of correlation between the ion motions is small. Ribeiro observed that the ion cross- correlation depends on the specific salt; while no cross-correlation was observed for KF, the degree of cross-correlation got more pronounced going from KCl, to LiCl and finally to LiF. $^{43}$ Borucka et al. tested the applicability of the NE-approach using experimental

self-diffusion data from molten NaCl and came to the conclusion that the experimental conductivity was overestimated by $40\% .^{115}$ Using more recent diffusion data for NaCl, NaI, RbI and $CsCl,^{116}$ we observe that the conductivity calculated from experimental self-diffusion coefficients is maximal $25\%$ higher than the experimental conductivity $^{104}$ (see SI, Table S15). We anticipate that there can be a difference in the degree of cross-correlation between reality and different force fields (e.g. polarizable vs. non-polarizable).

The experimental electrical conductivity values show the highest values for LiF and drop in each cation series towards the iodide salt with the values ranging from 9.0 to 0.9 S/cm (see Fig. 5, e & f). The general trend is predicted correctly by all force fields for most of the salts; the exception being LiI simulated with Kiss that forms a layered structure with diffusion coefficients close to zero, which in turn leads to an electrical conductivity close to zero. The RMSD values are 2.3 S/cm (2.2 S/cm without LiI) for Kiss, 2.0 S/cm for JC and 1.3 S/cm for WBK, indicating the the dynamic nature of the salts is best captured with our new force field. The corresponding diffusion coefficients are listed in the SI in Table S16. Evaluating the differences between the calculated and experimental data, WBK tends to overestimate the experimental data for most of the salts, while JC systematically underestimates the experimental values; Kiss is overestimating or underestimating depending on the salt. As $\kappa_{NE}$ are upper bound values, this implies that JC definitely underestimates the experimental values. It was shown earlier that the inclusion of polarization in a force field leads to an increase in conductivity, which is in line with an increased mobility of the ions. $^{113}$ Our results support this observation for WBK and JC, as all of the conductivity values of WBK are higher than the ones from JC. The polarizable force field Kiss does not follow this trend as pronounced.

Self-diffusion Finally, the temperature dependence of the self-diffusion coefficients was evaluated for the respective cation and anion in the salts NaCl, NaI, RbCl and CsCl using three temperatures above the melting point temperature (see SI Figure S4 and Table S17).

The average RMSD values for the self-diffusion coefficients of the ions in all salts and at different temperatures are 1.1 x $10^{-5}~cm^2/s$ for WBK, 2.0 x $10^{-5}~cm^2/s$ for Kiss and 2.9 x $10^{-5}~cm^2/s$ for JC. In general, the WBK force field seems to have a tendency to overestimate the experimental data, while the two reference force fields rather underestimate the self-diffusion coefficients. It has to be stated that the experimental diffusion coefficients may have large error bars, due to the challenging measurements at high temperatures.⁹⁸ The evaluation of the electrical conductivity, that also reflects the dynamics in the melts, is completely in line with this result if one solely considers the 4 investigated salts. For NaCl, NaI, RbCl and CsCl, the RMSD of the conductivity would result in 0.6 $S/cm$ for WBK, 0.7 $S/cm$ for Kiss and 0.9 $S/cm$ for JC. This implies that, considering all salts together, the force field JC most likely has more realistic diffusion coefficients than Kiss, as it has a lower RMSD for the electrical conductivity than the one evaluated for Kiss (see above).

Overall, it can be concluded that our new WBK force field gives the best description of the high temperature experimental data, looking at densities and potential energies from the solid and liquid phase in combination with structure, heat of fusion, surface tension, electrical conductivity and temperature-dependent diffusion coefficients, resulting in an average NRMSD value of 15.1% for WBK, 21.3% for JC, and 30.7% for Kiss (see Table 2). Considering all investigated phases together the average NRMSD is 7.1% for WBK, 15.2% for JC and 18.7% for Kiss.

## Conclusion
Considering all investigated properties from the gas, liquid and solid phases, the WBK force field performs very well in comparison to the reference force fields. From the investigation of different Van der Waals potentials and their ability to model the different phases, we can conclude that the energy function are improved systematically going from 12-6 LJ to 8-6 LJ to BK and finally WBK as is apparent from properties such as the vibrational frequencies.

It shows that systematic errors in LJ potentials¹¹⁷ can be remedied by introducing softer potentials such as BK and, in particular, WBK.

Our new WBK force field can certainly be improved further to capture more properties with higher accuracy. Instead of Gaussian charge distributions one could e.g. use Slater charge distributions that are known to describe the Coulomb interactions more realisti-cally.⁷,⁸,¹¹⁸ Regarding the Van der Waals interactions, it has been pointed out earlier that the combining rules have a severe effect on the pair-potentials and the properties that are calculated with them.¹⁶,¹¹⁹,¹²⁰ Here we explored a modified Buckingham potential,¹³ however it should be mentioned that there are other efforts in this field.¹⁴,¹⁵ In addition to the dipole-dipole interaction, some models³⁴,³⁷ calculate the dipole-quadrupole interaction through an extra term in the long-range attractive Van der Waals interaction explicitly; this adds an ex-tra parameter in the optimisation process but might increase the accuracy of the dispersion description. Along these lines, it is known that many-body-interactions play a crucial role in many materials¹²¹ and it was pointed out already in 1987¹²² that the inclusion of them in alkali halides are important to properly describe both elastic and dielectric properties at the same time. Several groups work in this direction and try to account for many-body-interactions.²⁶,²⁷,³⁷,¹²¹,¹²³ Nevertheless, inclusion of polarizability in the force field as used here and by Kiss et al.¹⁶ yields a good approximation of many body interactions.

The results and conclusions of this paper are dependent on the physico-chemical prop-erties selected for parameterisation, however the model gives very accurate predictions for properties that were not used for parameterisation as well. The applicability of a force field outside the range of properties used to parameterise it, is indeed one of the most important problems in the field. Our new WBK force field supports the correct crystal structure for all alkali halides at low and high temperature in contrast to the other tested force fields, but it will be interesting to see, for example, how the model will fare with different water models as it has solely been optimised towards interactions within alkali halides.

In summary, by combining polarizability, distributed charges and a soft Van der Waals

potential, we have come one step closer to a truly phase-transferable force field for alkali halides.

## Acknowledgments

The Swedish research council is acknowledged for financial support to DvdS (grant 2013-5947), and for a grant of computer time (SNIC2016/34-44) through the High Performance Computing Center North in Umeå, Sweden. NMF is supported through eSSENCE - The e-Science Collaboration (Uppsala-Lund-Umeå, Sweden).

## TOC

![](./images/812841474747006976_17.jpg)

# Supporting information

Additional information is available on the other Van der Waals potentials, the applied combining rules, the cohesive energy of the lattice, the pressure offsets and averages (Figure S1), and details on the molecular dynamics simulations. The numerical values of the optimised Van der Waals parameters are given in Table S1. Gas phase properties (experimental ion-pair distance, experimental and "theoretical point-charge" dipole moment, and ionicity) are listed in Table S2. In Figure S2 and S3 the difference between the calculated and the experimental values for gas and solid phase properties are plotted. In Table S3 to S16, all calculated values are listed: Table S3: Interionic distances for ion pairs; Table S4: Dissociation energies for ion pairs; Table S5: Vibrational frequencies for ion pairs; Table S6: Dipole moments for ion pairs; Table S7: Densities of the crystals at RT; Table S8: Lattice energies of the crystals at RT; Table S9: Densities of the crystals at $T_m$; Table S10: Densities of the melts at $T_m$; Table 11: Lattice energies of the crystal at $T_m$; Table 12: Potential energies of the melts at $T_m$; Table S13: Heat of fusion at $T_{m,exp}$; Table S14: Surface tension, Table S15: Electrical conductivity, and Table S16: Self-diffusion coefficients of the melts at 100 K above the $T_m$. Finally, the temperature dependence of the self-diffusion coefficients is presented in Figure S4 and the values are listed in Table S17. This information is available free of charge via the Internet at http://pubs.acs.org

# References

(1) Bindels, R. J. M. A molecular switch controlling renal sodium and potassium excretion. *Nature Genetics* **2003**, *35*, 302-303.

(2) Finlayson-Pitts, B. J.; Ezell, M. J.; Pitts Jr, J. N. Formation of chemically active chlorine compounds by reactions of atmospheric NaCl particles with gaseous $\mathrm{N_2O_5}$ and $\mathrm{ClONO_2}$. *Nature* **1989**, *337*, 241-244.

(3) Kenisarin, M. M. High-temperature phase change materials for thermal energy storage. Renew. Sust. Energ. Rev. 2010, 14, 955–970.

(4) Utigard, T. The properties and uses of fluxes in molten aluminum processing. JOM 1998, 50, 38–43.

(5) Hall, G. G.; Tsujinaga, K. The molecular electrostatic potential of some simple molecules. Theor. Chim. Acta. 1986, 69, 425–436.

(6) Hall, G. G.; Smith, C. M. The electron density of the water molecule. Theor. Chim. Acta. 1986, 69, 71–81.

(7) Wang, B.; Truhlar, D. G. Screened Electrostatic Interactions in Molecular Mechanics. J. Chem. Theory Comput. 2014, 10, 4480–4487.

(8) Wang, B.; Truhlar, D. G. Partial Atomic Charges and Screened Charge Models of the Electrostatic Potential. J. Chem. Theory Comput. 2012, 8, 1989–1998.

(9) Lennard-Jones, J. E. On the Determination of Molecular Fields. Proc. Royal Soc. Lond. Ser. A 1924, 106, 463–477.

(10) Riniker, S. Fixed-Charge Atomistic Force Fields for Molecular Dynamics Simulations in the Condensed Phase: An Overview. J. Chem. Inf. Model. 2018, 58, 565–578.

(11) Buckingham, R. A. The Classical Equation of State of Gaseous Helium, Neon and Argon. Proc. R. Soc. London Ser. A 1938, 168, 264–283.

(12) Hagler, A. T.; Lifson, S.; Dauber, P. Consistent force-field studies of inter-molecular forces in hydrogen-bonded crystals .2. Benchmark for the objective comparison of alternative force-fields. J. Amer. Chem. Soc. 1979, 101, 5122–5130.

(13) Wang, L.-P.; Chen, J.; Voorhis, T. V. Systematic Parametrization of Polarizable Force Fields from Quantum Chemistry Data. J. Chem. Theory Comput. 2013, 9, 452–460.

(14) Werhahn, J. C.; Miliordos, E.; Xantheas, S. S. A new variation of the Buckingham exponential-6 potential with a tunable, singularity-free short-range repulsion and an adjustable long-range attraction. *Chem. Phys. Lett.* **2015**, *619*, 133–138.

(15) Xantheas, S. S.; Werhahn, J. C. Universal scaling of potential energy functions describing intermolecular interactions. I. Foundations and scalable forms of new generalized Mie, Lennard-Jones, Morse, and Buckingham exponential-6 potentials. *J. Chem. Phys.* **2014**, *141*, 064117.

(16) Kiss, P. T.; Baranyai, A. A new polarizable force field for alkali halide ions. *J. Chem. Phys.* **2014**, *141*, 114501.

(17) Peng, Z.; Ewig, C. S.; Hwang, M. J.; Waldman, M.; Hagler, A. T. Derivation of Class II Force Fields. 4. van der Waals Parameters of Alkali Metal Cations and Halide Anions. *J. Phys. Chem. A* **1997**, *101*, 7243–7252.

(18) Jorgensen, W. L.; Maxwell, D. S.; Tirado-Rives, J. Development and testing of the OPLS all-atom force field on conformational energetics and properties of organic liquids. *J. Amer. Chem. Soc.* **1996**, *118*, 11225–11236.

(19) Joung, I. S.; Cheatham III, T. E. Determination of Alkali Halide Monovalent Ion Parameters for Use in Explicitly Solvated Biomolecular Simulations. *J. Phys. Chem. B* **2008**, *112*, 9020–9041.

(20) Yu, H.; Whitfield, T. W.; Harder, E.; Lamoureux, G.; Vorobyov, I.; Anisimov, V. M.; MacKerell, Jr., A. D.; Roux, B. Simulating Monovalent and Divalent Ions in Aqueous Solution Using a Drude Polarizable Force Field. *J. Chem. Theory Comput.* **2010**, *6*, 774–786.

(21) Dang, L. X.; Smith, D. E. Molecular dynamics simulations of aqueous ionic clusters using polarizable water. *J. Chem. Phys.* **1993**, *99*, 6950–6956.

(22) Dang, L. X. Development of nonadditive intermolecular potentials using molecular dynamics: Solvation of $Li^+$ and $F^-$ ions in polarizable water. *J. Chem. Phys.* **1992**, 96, 6970–6977.

(23) Jensen, K. P.; Jorgensen, W. L. Halide, Ammonium, and Alkali Metal Ion Parameters for Modeling Aqueous Solutions. *J. Chem. Theory Comput.* **2006**, 2, 1499–1509.

(24) Åqvist, J. Ion-water interaction potentials derived from free energy perturbation simulations. *J. Phys. Chem.* **1990**, 94, 8021–8024.

(25) Lamoureux, G.; Roux, B. Absolute Hydration Free Energy Scale for Alkali and Halide Ions Established from Simulations with a Polarizable Force Field. *J. Phys. Chem. B.* **2006**, 110, 3308–3322.

(26) Bajaj, P.; Götz, A. W.; Paesani, F. Toward Chemical Accuracy in the Description of Ion - Water Interactions through Many-Body Representations. I. Halide - Water Dimer Potential Energy Surfaces. *J. Chem. Theory Comput.* **2016**, 12, 2698–2705.

(27) Riera, M.; Mardirossian, N.; Bajaj, P.; Götz, A. W.; Paesani, F. Toward chemical accuracy in the description of ion-water interactions through many-body representations. Alkali-water dimer potential energy surfaces. *J. Chem. Phys.* **2017**, 147, 161715.

(28) Riera, M.; Götz, A. W.; Paesani, F. The i-TTM model for ab initio-based ion-water interaction potentials. II. Alkali metal ion-water potential energy functions. *Phys. Chem. Chem. Phys.* **2016**, 18, 30334–30343.

(29) Arismendi-Arrieta, D. J.; Riera, M.; Bajaj, P.; Prosmiti, R.; Paesani, F. i-TTM Model for Ab Initio-Based Ion-Water Interaction Potentials. 1. Halide-Water Potential Energy Functions. *J. Phys. Chem. B.* **2016**, 120, 1822–1832.

(30) Fuentes-Azcatl, R.; Barbosa, M. C. Potassium bromide, $KBr/\epsilon$: New Force Field. *Physica A* **2018**, 491, 480 – 489.

(31) Werhahn, J. C.; Akase, D.; Xantheas, S. S. Universal scaling of potential energy functions describing intermolecular interactions. II. The halide-water and alkali metal-water interactions. *J. Chem. Phys.* **2014**, 141, 064118.

(32) Benavides, A.; Portillo, M.; Chamorro, V.; Espinosa, J.; Abascal, J.; Vega, C. A potential model for sodium chloride solutions based on the TIP4P/2005 water model. *J. Chem. Phys.* **2017**, 147, 104501.

(33) Michalowsky, J.; Zeman, J.; Holm, C.; Smiatek, J. A polarizable MARTINI model for monovalent ions in aqueous solution. *J. Chem. Phys.* **2018**, 149, 163319.

(34) Fumi, F.; Tosi, M. Ionic sizes and born repulsive parameters in the NaCl-type alkali halides-I. *J. Phys. Chem. Solids* **1964**, 25, 31 – 43.

(35) Sangster, M.; Dixon, M. Interionic potentials for alkali halides: I Crystal independent shell parameters and fitted Born-Mayer potentials. *J. Phys. C: Solid State* **1978**, 11, 1523–1540.

(36) Madden, P. A.; Heaton, R.; Aguado, A.; Jahn, S. From first-principles to material properties. *J. Mol. Structure: THEOCHEM* **2006**, 771, 9–18.

(37) Salanne, M.; Rotenberg, B.; Jahn, S.; Vuilleumier, R.; Simon, C.; Madden, P. A. Including many-body effects in models for ionic liquids. *Theor. Chem. Acc.* **2012**, 131, 1143.

(38) Catlow, C. R. A.; Diller, K. M.; Norgett, M. J. Interionic potentials for alkali halides. *J. Phys. C: Solid State* **1977**, 10, 1395.

(39) Gowda, B. T.; Benson, S. W. Empirical potential parameters for alkali [metal] halide molecules and crystals, hydrogen halide molecules, alkali metal dimers, and hydrogen and halogen molecules. *J. Phys. Chem.* **1982**, 86, 847–857.

(40) Mao, A. H.; Pappu, R. V. Crystal lattice properties fully determine short-range interaction parameters for alkali and halide ions. *J. Chem. Phys.* **2012**, *137*, 064104.

(41) Lantelme, F.; Turq, P. Ionic dynamics in the LiCl-KCl system at liquid state. *J. Chem. Phys.* **1982**, *77*, 3177–3187.

(42) Wang, J.; Wu, J.; Sun, Z.; Lu, G.; Yu, J. Molecular dynamics study of the transport properties and local structures of molten binary systems (Li, NaCl, (Li, K)Cl and (Na, K)Cl. *J. Mol. Liq.* **2015**, *209*, 498 – 507.

(43) Ribeiro, M. C. Chemla effect in molten LiCl/KCl and LiF/KF mixtures. *J. Phys. Chem. B* **2003**, *107*, 4392–4402.

(44) Cavallari, M.; Cavazzoni, C.; Ferrario, M. Structure of NaCl and KCl concentrated aqueous solutions by ab initio molecular dynamics. *Mol. Phys.* **2004**, *102*, 959–966.

(45) Auffinger, P.; Cheatham, T. E.; Vaiana, A. C. Spontaneous formation of KCl aggregates in biomolecular simulations: a force field issue? *J. Chem. Theory Comp.* **2007**, *3*, 1851–1859.

(46) Dang, L. X.; Kollman, P. A. Free energy of association of the $K^+$: 18-crown-6 complex in water: a new molecular dynamics study. *J. Phys. Chem.* **1995**, *99*, 55–58.

(47) Jorgensen, W. L.; Chandrasekhar, J.; Madura, J. D.; Impey, R. W.; Klein, M. L. Comparison of Simple Potential Functions for Simulating Liquid Water. *J. Chem. Phys.* **1983**, *79*, 926–935.

(48) Berendsen, H. J. C.; Grigera, J. R.; Straatsma, T. P. The missing term in effective pair potentials. *J. Phys. Chem.* **1987**, *91*, 6269–6271.

(49) Weiner, S. J.; Kollman, P. A.; Nguyen, D. T.; Case, D. A. An All Atom Force Field for Simulation of Proteins and Nucleic Acids. *J. Comput. Chem.* **1986**, *7*, 230–252.

(50) Fischer, N. M.; Poleto, M. D.; Steuer, J.; van der Spoel, D. Influence of ${\rm Na}^+$ and ${\rm Mg}^{2+}$ ions on RNA structures studied with molecular dynamics simulations. *Nucleic Acids Res.* **2018**, 46, 4872–4882.

(51) Ghahremanpour, M. M.; van Maaren, P. J.; van der Spoel, D. The Alexandria Library: A Quantum Chemical Database of Molecular Properties for Force Field Development. *Sci. Data* **2018**, 5, 180062.

(52) Ghahremanpour, M. M.; van Maaren, P.; van der Spoel, D. Alexandria Library [Data set]. Zenodo. 2017; http://doi.org/10.5281/zenodo.1004711.

(53) Ghahremanpour, M. M.; van Maaren, P. J.; Ditz, J.; Lindh, R.; van der Spoel, D. Large-Scale Calculations of Gas Phase Thermochemistry: Enthalpy of Formation, Standard Entropy and Heat Capacity. *J. Chem. Phys.* **2016**, 145, 114305.

(54) Ghahremanpour, M. M.; van Maaren, P. J.; Caleman, C.; Hutchison, G. R.; van der Spoel, D. Polarizable s-type Atomic Orbitals for General Molecular Mechanics Force Fields. **2018**, https://doi.org/10.26434/chemrxiv.7035881.

(55) Caleman, C.; van Maaren, P. J.; Hong, M.; Hub, J. S.; Costa, L. T.; van der Spoel, D. Force Field Benchmark of Organic Liquids: Density, Enthalpy of Vaporization, Heat Capacities, Surface Tension, Compressibility, Expansion Coefficient and Dielectric Constant. *J. Chem. Theory Comput.* **2012**, 8, 61–74.

(56) Zhang, H.; Tan, T.; Feng, W.; van der Spoel, D. Molecular recognition in different environments: $\beta$-cyclodextrin dimer formation in organic solvents. *J. Phys. Chem. B* **2012**, 116, 12684–93.

(57) Zhang, H.; Tan, T.; Hetenyi, C.; van der Spoel, D. Quantification of Solvent Contribution to the Stability of Noncovalent Complexes. *J. Chem. Theory Comput.* **2013**, 9, 4542–4551.

(58) Fischer, N. M.; van Maaren, P. J.; Ditz, J. C.; Yildirim, A.; van der Spoel, D. Properties of liquids in Molecular Dynamics Simulations with explicit long-range Lennard Jones interactions. *J. Chem. Theory Comput.* **2015**, *11*, 2938–2944.

(59) Zhang, J.; Tuguldur, B.; van der Spoel, D. Force field benchmark II: Gibbs energy of solvation of organic molecules in organic liquids. *J. Chem. Inf. Model.* **2015**, *55*, 1192–1201.

(60) Zhang, J.; Tuguldur, B.; van der Spoel, D. Correction to Force field benchmark II: Gibbs energy of solvation of organic molecules in organic liquids. *J. Chem. Inf. Model.* **2016**, *56*, 819–820.

(61) Zhang, H.; Tan, T.; van der Spoel, D. Generalized Born and Explicit Solvent Models for Free Energy Calculations in Organic Solvents: Cyclodextrin Dimerization. *J. Chem. Theory Comput.* **2015**, *11*, 5103–5113.

(62) Zhang, H.; Yin, C.; Yan, H.; van der Spoel, D. Evaluation of Generalized Born Models for Large Scale Affinity Prediction of Cyclodextrin Host-Guest Complexes. *J. Chem. Inf. Model.* **2016**, *56*, 2080–2092.

(63) Zhang, H.; Jiang, Y.; Yan, H.; Yin, C.; Tan, T.; van der Spoel, D. Free Energy Calculations of Ionic Hydration Consistent with the Experimental Hydration Free Energy of the Proton. *J. Phys. Chem. Lett.* **2017**, *8*, 2705–2712.

(64) Zhang, H.; Yin, C.; Jiang, Y.; van der Spoel, D. Force Field Benchmark of Amino acids: I. Hydration and Diffusion in Different Water Models. *J. Chem. Inf. Model.* **2018**, *58*, 1037–1052.

(65) van der Spoel, D.; van Maaren, P. J.; Caleman, C. GROMACS Molecule & Liquid Database. *Bioinformatics* **2012**, *28*, 752–753.

(66) Jordan, P. C.; van Maaren, P. J.; Mavri, J.; van der Spoel, D.; Berendsen, H. J. C. Towards Phase Transferable Potential Functions: Methodology and Application to Nitrogen. J. Chem. Phys. 1995, 103, 2272–2285.

(67) Laaksonen, A.; Clementi, E. Theoretical study of some gas, liquid and crystal properties of sodium chloride using ab initio potentials. Mol. Phys. 1985, 56, 495–524.

(68) Aragones, J. L.; Sanz, E.; Valeriani, C.; Vega, C. Calculation of the melting point of alkali halides by means of computer simulations. J. Chem. Phys. 2012, 137, 104507.

(69) Frederiksen, S. L.; Jacobsen, K. W.; Brown, K. S.; Sethna, J. P. Bayesian Ensemble Approach to Error Estimation of Interatomic Potentials. Phys. Rev. Lett. 2004, 93, 165501.

(70) Mortensen, J. J.; Kaasbjerg, K.; Frederiksen, S. L.; Nørskov, J. K.; Sethna, J. P.; Jacobsen, K. W. Bayesian Error Estimation in Density-Functional Theory. Phys. Rev. Lett. 2005, 95, 216401.

(71) Elking, D.; Darden, T.; Woods, R. J. Gaussian induced dipole polarization model. J. Comput. Chem. 2007, 28, 1261–1274.

(72) Kiss, P. T.; Sega, M.; Baranyai, A. Efficient Handling of Gaussian Charge Distributions: An Application to Polarizable Molecular Models. J. Chem. Theory Comput. 2014, 10, 5513–5519.

(73) van Maaren, P. J.; van der Spoel, D. Molecular dynamics simulations of water with a novel shell-model potential. J. Phys. Chem. B. 2001, 105, 2618–2626.

(74) C R, G.; Jose, D.; Datta, A. Electronic structure, lattice energies and Born exponents for alkali halides from first principles. AIP Advances 2012, 2, 012131.

(75) Sirdeshmukh, D. B.; Sirdeshmukh, L.; Subhadra, K. G. Alkali Halides, 1st ed.; Springer: Berlin, Heidelberg, New York, 2001.

(76) Rumble, J. R. CRC Handbook of Chemistry and Physics, 98th Ed. (Internet Version 2018); CRC Press Taylor Francis: Boca Raton, FL, 2018.

(77) Morris, D. The lattice energies of the alkali halides. Acta Crystallogr. 1956, 9, 197−198.

(78) Cubicciotti, D. Erratum: Lattice Energies of the Alkali Halides and the Electron Affinities of the Halogens. J. Chem. Phys. 1961, 34, 2189−2189.

(79) Molina, J. J.; Lectez, S.; Tazi, S.; Salanne, M.; Dufreche, J. F.; Roques, J.; Simoni, E.; Madden, P.; Turq, P. Ions in solutions: Determining their polarizabilities from first-principles. J. Chem. Phys. 2011, 134, 014511.

(80) Hättig, C.; Heß, B. A. TDMP2 calculation of dynamic multipole polarizabilities and dispersion coefficients for the halogen anions $F^-$, $Cl^-$, $Br^-$ and $I^-$. J. Chem. Phys. 1998, 108, 3863−3870.

(81) McQuarrie, D. A. Quantum Chemistry, 2nd ed.; University Science Books: Sausalito, California, 2008.

(82) Irikura, K. K. Experimental Vibrational Zero-Point Energies: Diatomic Molecules. J. Phys. Chem. Ref. Data 2007, 36, 389−397.

(83) Hess, B.; Kutzner, C.; Van er Spoel, D.; Lindahl, E. GROMACS 4: Algorithms for Highly Efficient, Load-Balanced, and Scalable Molecular Simulation. J. Chem. Theory Comput. 2008, 4, 435−447.

(84) Essmann, U.; Perera, L.; Berkowitz, M. L.; Darden, T.; Lee, H.; Pedersen, L. G. A Smooth Particle Mesh Ewald Method. J. Chem. Phys. 1995, 103, 8577−8592.

(85) Baker, A. D.; Baker, M. D. Rapid calculation of individual ion Madelung constants and their convergence to bulk values. Am. J. Phys. 2010, 78, 102−105.

(86) Baker, M. D.; Baker, A. D. Teaching nanochemistry: Madelung constants of nanocrystals. J. Chem. Educ. 2010, 87, 280−284.

(87) Datz, S.; Smith Jr., W. T.; Taylor, E. H. Molecular Association in Alkali Halide Vapors. J. Chem. Phys. 1961, 34, 558–563.

(88) Miller, R. C.; Kusch, P. Molecular Composition of Alkali Halide Vapors. J. Chem. Phys. 1956, 25, 860–876.

(89) National Institute of Standards and Technology, Diatomic Spectral Database Holdings. http://physics.nist.gov/cgi-bin/MolSpec/diperiodic.pl, 2018.

(90) Brewer, L.; Brackett, E. The Dissociation Energies of Gaseous Alkali Halides. Chem. Rev. 1961, 61, 425–432.

(91) National Institute of Standards and Technology, Experimental Vibrational Frequencies. https://cccbdb.nist.gov/expvibs1.asp, 2018.

(92) Veazey, S. E.; Gordy, W. Millimeter-Wave Molecular-Beam Spectroscopy: Alkali Fluorides. Phys. Rev. 1965, 138, 1303–1311.

(93) Darnell, A.; McCollum, W. Thermodynamics of the Fm3m/ Pm3m transition in the potassium and rubidium halides. J. Phys. Chem. Solids 1970, 31, 805–815.

(94) Galwey, A. A view and a review of melting of alkali metal halide crystals. J. Therm. Anal. Calorim. 2005, 82, 23–40.

(95) Adams, D.; McDonald, I. Rigid-ion models of the interionic potential in the alkali halides. J. Phys. C: Solid State 1974, 7, 2761.

(96) Belonoshko, A. B.; Skorodumova, N.; Rosengren, A.; Johansson, B. Melting and critical superheating. Phys. Rev. B 2006, 73, 012201.

(97) Levy, H. A.; Agron, P. A.; Bredig, M. A.; Danford, M. D. X-ray and Neutron Diffraction Studies of Molten Alkali Halides. Ann. NY Acad. Sci. 1960, 79, 762–780.

(98) Wang, J.; Sun, Z.; Lu, G.; Yu, J. Molecular Dynamics Simulations of the Local Structures and Transport Coefficients of Molten Alkali Chlorides. *J. Phys. Chem. B* **2014**, 118, 10196 – 10206.

(99) Michielsen, J.; Woerlee, P.; vd Graaf, F.; Ketelaar, J. Pair potential for alkali metal halides with rock salt crystal structure. Molecular Dynamics Calculations on NaCl and LiI. *J. Chem. Soc. Far. Trans.* **1975**, 71, 1730–1741.

(100) Edwards, F. G.; Enderby, J. E.; Howe, R. A.; Page, D. I. The structure of molten sodium chloride. *J. Phys. C: Solid State* **1975**, 8, 3483.

(101) Biggin, S.; Enderby, J. E. Comments on the structure of molten salts. *J. Phys. C: Solid State* **1982**, 15, L305.

(102) Janz, G. J. *Molten Salts Handbook*; Academic Press: New York, London, 1967.

(103) Yaws, C. L.; Richmond, P. C. *Thermophysical Properties of Chemicals and Hydrocarbons*; Elsevier, 2009; pp 782–789.

(104) Janz, G. J.; Dampier, F.; Lakshminarayanan, G.; Lorenz, P.; Tomkins, R. *Molten Salts. Volume I. Electrical Conductance, Density, and Viscosity Data*; 1968.

(105) Orowan, E. Surface energy and surface tension in solids and liquids. *Proc. R. Soc. Lond. A* **1970**, 316, 473–491.

(106) Aguado, A.; Wilson, M.; Madden, P. A. Molecular dynamics simulations of the liquid–vapor interface of a molten salt. I. Influence of the interaction potential. *Can. J. Phys.* **2001**, 115, 8603–8611.

(107) Aguado, A.; Scott, W.; Madden, P. A. Molecular dynamics simulations of the liquid–vapor interface of a molten salt. II. Finite size effects and comparison to experiment. *J. Chem. Phys.* **2001**, 115, 8612–8619.

(108) Zubillaga, R. A.; Labastida, A.; Cruz, B.; Martínez, J. C.; Sánchez, E.; Alejandre, J. Surface Tension of Organic Liquids Using the OPLS/AA Force Field. *J. Chem. Theory Comput.* **2013**, *9*, 1611–1615.

(109) Schröder, C.; Haberler, M.; Steinhauser, O. On the computation and contribution of conductivity in molecular ionic liquids. *J. Chem. Phys.* **2008**, *128*, 134501.

(110) Kowsari, M. H.; Fakhraee, M. Influence of butyl side chain elimination, tail amine functional addition, and C2 methylation on the dynamics and transport properties of imidazolium-based [Tf2N⁻] ionic liquids from molecular dynamics simulations. *J. Chem. Eng. Data* **2015**, *60*, 551–560.

(111) Docampo-Álvarez, B.; Gómez-González, V.; Méndez-Morales, T.; Rodríguez, J. R.; López-Lago, E.; Cabeza, O.; Gallego, L. J.; Varela, L. M. Molecular dynamics simulations of mixtures of protic and aprotic ionic liquids. *Phys. Chem. Chem. Phys.* **2016**, *18*, 23932–23943.

(112) Dommert, F.; Schmidt, J.; Qiao, B.; Zhao, Y.; Krekeler, C.; Delle Site, L.; Berger, R.; Holm, C. A comparative study of two classical force fields on statics and dynamics of [EMIM][BF₄] investigated via molecular dynamics simulations. *J. Chem. Phys.* **2008**, *129*, 224501.

(113) Morgan, B.; Madden, P. A. Ion mobilities and microscopic dynamics in liquid (Li, K) Cl. *J. Chem. Phys.* **2004**, *120*, 1402–1413.

(114) Lee, Y.-C.; Kolafa, J.; Curtiss, L. A.; Ratner, M. A.; Shriver, D. F. Molten salt electrolytes. I. Experimental and theoretical studies of LiI/AlCl₃. *J. Chem. Phys.* **2001**, *114*, 9998–10009.

(115) Borucka, A. Z.; Bockris, J.; Kitchener, J. Self-diffusion in molten sodium chloride: a test of the applicability of the Nernst?Einstein equation. *Proc. R. Soc. Lond. A* **1957**, *241*, 554–567.

(116) Bockris, J.; Hooper, G. Self-diffusion in molten alkali halides. *Discuss. Faraday Soc.* **1961**, *32*, 218–236.

(117) Wensink, E. J. W.; Hoffmann, A. C.; van Maaren, P. J.; van der Spoel, D. Dynamic Properties of Water/Alcohol Mixtures Studied by Computer Simulation. *J. Chem. Phys.* **2003**, *119*, 7308–7317.

(118) Rappé, A. K.; Goddard III, W. A. Charge Equillibration for Molecular Dynamics Simulations. *J. Phys. Chem.* **1991**, *95*, 3358–3363.

(119) Kong, C. L.; Chakrabarty, M. R. Combining rules for intermolecular potential param- eters. III. Application to the exp 6 potential. *J. Phys. Chem.* **1973**, *77*, 2668–2670.

(120) Hogervorst, W. Transport and equilibrium properties of simple gases and forces be- tween like and unlike atoms. *Physica* **1971**, *51*, 77–89.

(121) Hermann, J.; DiStasio Jr, R. A.; Tkatchenko, A. First-principles models for van der Waals interactions in molecules and materials: concepts, theory, and applications. *Chem. Rev.* **2017**, *117*, 4714–4758.

(122) Shanker, J.; Sinha, R.; Hans, D. On the interionic potentials and polarization models in alkali halide crystals. *Solid State Commun.* **1987**, *62*, 769–772.

(123) Cisneros, G. A.; Wikfeldt, K. T.; Ojamae, L.; Lu, J.; Xu, Y.; Torabifard, H.; Bartók, A. P.; Csányi, G.; Molinero, V.; Paesani, F. Modeling molecular interactions in water: From pairwise to many-body potential energy functions. *Chem. Rev.* **2016**, *116*, 7501–7528.