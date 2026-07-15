# Gruneisen parameters of bead-spring chains: MD simulation and theory

Cite as: J. Chem. Phys. 153, 244903 (2020); https://doi.org/10.1063/5.0035451
Submitted: 28 October 2020 . Accepted: 06 December 2020 . Published Online: 28 December 2020

Craig S. Stevenson, John G. Curro, and John D. McCoy

![](./images/812522251856379905_1.jpg) ![](./images/812522251856379905_2.jpg) ![](./images/812522251856379905_3.jpg)

## ARTICLES YOU MAY BE INTERESTED IN

[Efficient and realistic simulation of phase coexistence](https://doi.org/10.1063/5.0027778)
The Journal of Chemical Physics 153, 244121 (2020); https://doi.org/10.1063/5.0027778

[An energy-landscape-based crossover temperature in glass-forming liquids](https://doi.org/10.1063/5.0034719)
The Journal of Chemical Physics 153, 241101 (2020); https://doi.org/10.1063/5.0034719

[Eyring equation and fluctuation-dissipation far away from equilibrium](https://doi.org/10.1063/5.0032634)
The Journal of Chemical Physics 153, 244116 (2020); https://doi.org/10.1063/5.0032634

![](./images/812522251856379905_4.jpg)

J. Chem. Phys. 153, 244903 (2020); https://doi.org/10.1063/5.0035451
153, 244903

© 2020 Author(s).

# Gruneisen parameters of bead-spring chains: MD simulation and theory

Cite as: J. Chem. Phys. 153, 244903 (2020); doi: 10.1063/5.0035451
Submitted: 28 October 2020 • Accepted: 6 December 2020 •
Published Online: 28 December 2020

![](./images/812522251856379905_5.jpg) ![](./images/812522251856379905_6.jpg) ![](./images/812522251856379905_7.jpg)

Craig S. Stevenson, $^{1}$ John G. Curro, $^{2,a)}$ and John D. McCoy $^{2}$

## AFFILIATIONS
$^{1}$University of New Mexico, Albuquerque, New Mexico 87131, USA
$^{2}$New Mexico Institute of Mining and Technology, Socorro, New Mexico 87801, USA

a)Author to whom correspondence should be addressed: jgcurro@gmail.com

## ABSTRACT
Molecular Dynamics (MD) simulations were carried out in a microcanonical ensemble to compute the Gruneisen parameter (denoted as $\gamma$) of a liquid of bead-spring chains having 10 beads/chain. $\gamma$ was studied over a wide range of temperatures below and above the glass transition temperature. We found that the Gruneisen parameter varied in the range of 2.1–3.1 and was significantly higher than typically observed experimentally in real polymers. In the glass, a theory was developed for $\gamma$ using a cell model in which the beads are harmonically bound to their respective cell centers. The resulting Gruneisen parameter is predicted to increase slightly with temperature. Above the glass transition temperature, we employed the generalized Flory dimer equation-of-state and the polymer reference interaction model theory to calculate $\gamma$. In these calculations, we found that $\gamma$ decreased with temperature in the liquid. The theoretical predictions for $\gamma$ were found to be in good qualitative agreement with our MD simulations, without any adjustable parameters, both above and below $T_g$. In experiments on real polymers, $\gamma$ undergoes a sharp discontinuity at the glass transition. By contrast, in our MD simulations, $\gamma$ varies smoothly over a broad transition region.

Published under license by AIP Publishing. https://doi.org/10.1063/5.0035451

## I. INTRODUCTION
The Gruneisen parameter, $^{1}$ denoted as $\gamma$, is well known in solid-state physics. Qualitatively, it is a measure of how the vibrational frequencies change with volume. For a collection of harmonic oscillators of frequency $v_i$, the Gruneisen parameter is defined as

$$
\gamma = \frac{\sum_{i} \gamma_{i} c_{i}}{\sum_{i} c_{i}}, \tag{1a}
$$

where the mode Gruneisen parameters $\gamma_i$,

$$
\gamma_{i}=-\frac{\partial \ln v_{i}}{\partial \ln V}, \tag{1b}
$$

are averaged with the mode vibrational heat capacities $c_i$ as weighting factors,

$$
c_{\mathrm{i}}=\mathrm{k}_{\mathrm{B}}\left(\frac{\mathrm{h} v_{\mathrm{i}}}{\mathrm{k}_{\mathrm{B}} \mathrm{T}}\right)^{2} \frac{\exp \left(\mathrm{h} v_{\mathrm{i}} / \mathrm{k}_{\mathrm{B}} \mathrm{T}\right)}{\left[\exp \left(\mathrm{h} v_{\mathrm{i}} / \mathrm{k}_{\mathrm{B}} \mathrm{T}\right)-1\right]^{2}}, \tag{1c}
$$

where T is the temperature, $k_B$ is the Boltzmann constant, and h is Planck's constant. The sum of $c_i$'s is the total heat capacity at constant volume $C_V$. An important application of the Gruneisen parameter is in shockwave physics. The Mie-Gruneisen equation-of-state $^{1,2}$ is commonly used as the constitutive model input to shockwave hydrodynamic codes. $^{3}$ The Gruneisen parameter can be measured experimentally using Eq. (1). For example, Wada et al. $^{4}$ determined $\gamma$ of polystyrene from ultrasonic velocity measurements by measuring the frequency as a function of density. Similarly, Kruger, Bohn, and Schrieber $^{5}$ measured $\gamma$ of various materials from longitudinal acoustic frequencies as a function of density using Brillouin spectroscopy.

A thermodynamic interpretation of the Gruneisen parameter can be expressed in several ways. $^{2}$ One representation suggests that $\gamma$ acts like a coupling parameter between mechanical and heat effects,

$$
\gamma=\mathrm{V}\left(\frac{\partial \mathrm{P}}{\partial \mathrm{E}}\right)_{\mathrm{V}}. \tag{2a}
$$

Here, γ is the pressure response to an impulse of internal energy E deposited in a material. Alternatively, we can show from thermodynamic manipulations that

$$
\gamma=\frac{\mathrm{V} \alpha}{\kappa \mathrm{C}_{\mathrm{V}}}, \tag{2b}
$$

where α and κ are the thermal expansion coefficient and isothermal compressibility, respectively. Another representation of γ can be written in terms of the thermal pressure,

$$
\gamma=\frac{\mathrm{V}}{\mathrm{C}_{\mathrm{V}}}\left(\frac{\partial \mathrm{P}}{\partial \mathrm{T}}\right)_{\mathrm{V}}. \tag{2c}
$$

For quantized harmonic oscillators, the vibrational mode definition of γ in Eq. (1) is exactly equivalent $^{2,10}$ to the thermodynamic definitions in Eq. (2). For an ideal gas, Eq. (2c) can be used to show that γ = 2/3. From the van der Waals equation-of-state, we find γ = (2/3)/(1 − η), where η is the packing fraction. Note that $\mathrm{C}_{\mathrm{V}}=3 \mathrm{Nk}_{\mathrm{B}} / 2$ is the same for both the ideal gas and the van der Waals fluid. $^{6}$ Thus, for a typical liquid packing fraction of 0.5, we expect γ ~ 4/3 for a van der Waals liquid. Additionally, γ decreases with temperature since the packing fraction decreases with T.

The thermodynamic Gruneisen parameter can, of course, be obtained experimentally from measurements of the thermal expansion, compressibility, and heat capacities of a given material using Eq. (2b). Alternatively, γ can be measured from energy deposition experiments using Eq. (2a). In these experiments, $^{7,8}$ the material is exposed to a pulse of electrons from an electron accelerator and the resulting stress pulse is measured. For metals and solids with simple molecular structures, experiments $^{9}$ show that the thermodynamic Gruneisen parameter ranges approximately from 2 to 3 and is weakly dependent on temperature.

Polymers, $^{10}$ by contrast, have Gruneisen parameters that are smaller in magnitude than for simple atomic systems and are typically less than one. Furthermore, γ can depend markedly on temperature and pressure. An explanation for the difference in the Gruneisen parameters between simple atomic systems and polymers was suggested by Curro $^{10}$ to be due to density-independent internal degrees of freedom in polymers. In Eq. (1b), the mode Gruneisen parameters γᵢ are not all equal. In fact, for polymers with a complex monomeric architecture, the internal vibrational frequencies, or optical modes, are almost independent of density. This is clear from the work of Wu and Shen, $^{11}$ who used infrared spectroscopy to measure the frequency shifts with pressure of internal vibrations of polystyrene. Wu and Shen reported infrared mode Gruneisen parameters γᵢ in the range of 0.01–0.02—orders of magnitude smaller than the center-of-mass modes of the polymer repeat units. Consequently, only some of the terms in the numerator of Eq. (1a) contribute to γ. At the same time, all the terms in the denominator contribute. In other words, for polymers, there are many channels for deposited energy that are density-independent and consequently do not contribute to the pressure. In the limit of high temperature, Curro suggested $^{10}$ the approximation

$$
\gamma \sim \gamma_{1} / \mathrm{q}, \tag{3}
$$

where q is the number of atoms in the polymer repeat unit and γ₁ is the Gruneisen parameter characteristic of a simple atomic crystal or glass.

Recently, there have been molecular dynamics (MD) simulations of shockwaves in a range of polymers using explicit atom $^{12}$ and coarse-grained models. $^{13}$ Agrawal and co-workers $^{14}$ deduced the Gruneisen parameter from coarse-grained MD simulations of the shock Hugoniot of polyethylene. Godey, Bensaid, and Soldera $^{15}$ used molecular dynamics (MD) simulations, employing a detailed explicit-atom model, to determine Gruneisen parameters of polyethylene and polystyrene as a function of temperature. Godey and co-workers found that γ decreased with increasing temperature and was in the range of 0.50–1.5 in accordance with experiment.

The purpose of the present investigation is to study the Gruneisen parameter of bead-spring chains by both MD simulations and theory. Our motivation for this work is to see the effect that the monomer structure has on the magnitude of the Gruneisen parameter. For a bead-spring model of a polymer, the repeat units, by definition, have no internal structure. Hence, q = 1 in Eq. (3) for this model and we expect that γ would be of order γ₁ for the bead-spring model of polymer chains. Real polymers, having a complex monomer structure, have internal degrees of freedom that increase the heat capacity in Eq. (2b) over that of bead-spring models. Therefore, we anticipate that the magnitude of the Gruneisen parameter of bead-spring models would be significantly larger, depending on the details of the monomer structure, than observed from experiments and explicit-atom simulations of complex polymers like polystyrene.

In this paper, we will begin by discussing the MD simulation methods we used to study bead-spring chains of length N = 10 repeat units. In particular, we will show how we obtained the Gruneisen parameter from the simulations. We will then present our simulation results for γ as a function of temperature both below and above the glass transition temperature Tg. The simulation results will first be discussed and compared to theories below Tg where the harmonic oscillator approximation would be expected to be valid. We will then turn our attention to the Gruneisen parameter above Tg where we apply liquid state theoretical methods to calculate γ and compare with our simulations. Finally, we will discuss our MD results for γ in the glass transition region.

## II. MOLECULAR DYNAMICS SIMULATIONS

Our MD simulations were carried out using the LAMMPS code developed by Plimpton $^{16}$ using the standard bead-spring model $^{17}$ of Kremer and Grest. Following our earlier work, $^{18}$ we simulated systems of n = 80 chains having N = 10 beads per chain. Thus, we have a total of 800 beads in a cubic box with periodic boundary conditions to emulate bulk behavior. Between nonadjacent beads, we employed the Lennard-Jones 12-6 potential (LJ) with a cutoff,

$$
\begin{aligned}
\mathrm{v}(\mathrm{r}) & =4 \varepsilon\left[\left(\frac{\sigma}{\mathrm{r}}\right)^{12}-\left(\frac{\sigma}{\mathrm{r}}\right)^{6}\right], & & \mathrm{r} \leq 2.3 \sigma \\
& =0, & & \mathrm{r}>2.3 \sigma.
\end{aligned} \tag{4}
$$

The bond potential between adjacent beads is taken to be harmonic with a bond length of $\ell=0.90 \sigma$,

$$
\mathrm{U}_{\mathrm{bond}}(\mathrm{r})=\frac{\mathrm{k}_{\mathrm{bond}}}{2}(\mathrm{r}-\ell)^{2},
\tag{5}
$$

and a spring constant of $\mathrm{k}_{\mathrm{bond}}=1111 \varepsilon / \sigma^{2}$. The bond length was chosen to be less than $\sigma$ in order to avoid crystallization at low temperatures of the chains during the simulations.

As a starting point for the present study, we drew on the constant temperature and pressure bulk simulations from our earlier work. $^{18}$ We follow the standard practice of using a dimensionless temperature $\mathrm{T}$, defined as $\mathrm{T}=\mathrm{k}_{\mathrm{B}} \mathrm{T}_{\mathrm{K}} / \varepsilon$, where $\mathrm{T}_{\mathrm{K}}$ is the temperature in degrees K. Constant cooling runs were performed at zero pressure where $\mathrm{T}$ is varied according to

$$
\mathrm{T}=1-\Gamma_{\mathrm{T}} \mathrm{t}
\tag{6}
$$

with a cooling rate of $\Gamma_{\mathrm{T}}=2 \times 10^{-5}$ and time $\mathrm{t}$ is in units of $\sqrt{\mathrm{m} \sigma^{2} / \varepsilon}$. The average density was measured over a range of temperatures encompassing the glass transition. For this system, the glass transition temperature was observed to be $\mathrm{T}_{\mathrm{g}}=0.381$. In Fig. 1, we show a plot of density vs temperature from our previous investigation $^{18}$ along with the densities used here.

In order to obtain the Gruneisen parameter, we employed a microcanonical ensemble where the number of beads $\mathrm{nN}$, volume $\mathrm{V}$, and internal energy $\mathrm{E}$ are held fixed in the simulation. The general approach is as follows: (1) At a given temperature $\mathrm{T}$, we first determine the corresponding density or volume from a constant pressure simulation at $\mathrm{P}=0$. We use the last snapshot of this simulation as our starting configuration. The resulting density from this snapshot is close to the results shown in Fig. 1. (2) Using this density, the microcanonical integrator in LAMMPS is used to compute the pressure at a series of internal energies E. (3) The Gruneisen parameter is then found from Eq. (2a) by taking the derivative of the P vs E curve. In this study, we carried out a series of simulations over a range of densities corresponding to $\mathrm{T}=0.70-0.10$. For each density, we incrementally changed the internal energy by rescaling the velocities (and hence the kinetic energy) of the beads. For each velocity rescale, we ran microcanonical simulations for $3 \times 10^{6}$ time steps where we followed the pressure as a function of time. After the pressure equilibrates, we report the average equilibrated pressure. Some of the pressure-energy lines are shown in Fig. 2. It can be observed from Fig. 2 that the data are linear over the range of energies studied.

From the slopes of the lines in Fig. 2, we then determined the Gruneisen parameters using Eq. (2a). These results are shown in Table I and in Fig. 3. To determine the uncertainty in $\gamma$ caused by errors in the pressure, density, and other variables, several runs were repeated, as indicated in Table I. The resultant error bars are shown in Fig. 3. From Fig. 3, it can be observed that the Gruneisen parameter of bead-spring chain systems is in the range of 2.4-3.06 and is larger than measured experimentally on polymers like polystyrene. The magnitude of $\gamma$ measured here was anticipated from the earlier work of Curro $^{10}$ since $\mathrm{q}=1$ in Eq. (3) for bead-spring chains. As mentioned above, we expect that $\gamma \sim \gamma_{1}$ for bead-spring chains and would be similar in magnitude to simple atomic systems. To illustrate this point, we also performed MD simulations on an atomic liquid $(\mathrm{N}=1)$ and found that $\gamma=2.32$ at $\mathrm{T}=0.75$ and $\rho \sigma^{3}=0.723$, as reported in Table I and shown in Fig. 3. Lower temperature simulations for the atomic liquid were problematic because of the proximity of the two-phase gas-liquid regime. MD simulations $^{19}$ carried out at the National Institute for Standards

![](./images/812522251856379905_8.jpg)

FIG. 1. Density vs temperature results from our previous constant pressure simulations $^{18}$ (blue squares). Densities and temperatures used in the present investigation (red circles). The dashed line indicates the glass transition temperature.

![](./images/812522251856379905_9.jpg)

FIG. 2. Pressure vs internal energy (circles) from nVE simulations of 10 unit chains for selected temperatures: 0.10, 0.20, 0.30, 0.40, 0.50, 0.60, and 0.70 (left to right). The straight lines are a fit to the data.

<table>
<caption>TABLE I. MD simulation results at P = 0: N = 10 except for the last row where N = 1.</caption>
<tbody>
<tr>
<td>
$T$
</td>
<td>
$\rho\sigma^{3}$
</td>
<td>
$\gamma$
</td>
<td>
$T$
</td>
<td>
$\rho\sigma^{3}$
</td>
<td>
$\gamma$
</td>
</tr>
<tr>
<td>
0.10
</td>
<td>
1.0792
</td>
<td>
2.3815
</td>
<td>
0.42
</td>
<td>
1.0405
</td>
<td>
2.9889
</td>
</tr>
<tr>
<td>
0.20
</td>
<td>
1.0709
</td>
<td>
2.5003
</td>
<td>
0.44
</td>
<td>
1.0301
</td>
<td>
3.0062
</td>
</tr>
<tr>
<td>
</td>
<td>
1.0705
</td>
<td>
2.6333
</td>
<td>
0.48
</td>
<td>
1.0159
</td>
<td>
2.9516
</td>
</tr>
<tr>
<td>
</td>
<td>
1.0676
</td>
<td>
2.6159
</td>
<td>
0.50
</td>
<td>
1.0146
</td>
<td>
2.9295
</td>
</tr>
<tr>
<td>
0.30
</td>
<td>
1.0583
</td>
<td>
2.7447
</td>
<td>
</td>
<td>
1.0021
</td>
<td>
2.9020
</td>
</tr>
<tr>
<td>
</td>
<td>
1.0534
</td>
<td>
2.8386
</td>
<td>
</td>
<td>
1.0153
</td>
<td>
2.8914
</td>
</tr>
<tr>
<td>
</td>
<td>
1.0566
</td>
<td>
2.8590
</td>
<td>
0.52
</td>
<td>
1.0006
</td>
<td>
2.8547
</td>
</tr>
<tr>
<td>
0.34
</td>
<td>
1.0453
</td>
<td>
2.9495
</td>
<td>
0.60
</td>
<td>
0.9878
</td>
<td>
2.7533
</td>
</tr>
<tr>
<td>
0.36
</td>
<td>
1.0446
</td>
<td>
2.9492
</td>
</td>
<td>
</td>
<td>
0.9758
</td>
<td>
2.6843
</td>
</tr>
<tr>
<td>
0.38
</td>
<td>
1.0450
</td>
<td>
3.0604
</td>
<td>
</td>
<td>
0.9827
</td>
<td>
2.7212
</td>
</tr>
<tr>
<td>
0.40
</td>
<td>
1.0374
</td>
<td>
3.0542
</td>
<td>
0.70
</td>
<td>
0.9546
</td>
<td>
2.6654
</td>
</tr>
<tr>
<td>
</td>
<td>
1.0419
</td>
<td>
2.9796
</td>
<td>
</td>
<td>
0.9600
</td>
<td>
2.5916
</td>
</tr>
<tr>
<td>
</td>
<td>
1.0374
</td>
<td>
2.9967
</td>
<td>
</td>
<td>
0.9492
</td>
<td>
2.5365
</td>
</tr>
<tr>
<td>
$0.75^{\mathrm{a}}$
</td>
<td>
$0.7230^{\mathrm{a}}$
</td>
<td>
$2.320^{\mathrm{a}}$
</td>
<td>
</td>
<td>
</td>
<td>
</td>
</tr>
</tbody>
</table>

$^{\mathrm{a}}$N = 1.

and Technology (NIST) show that the phase boundary would occur below about $\rho\sigma^{3} = 0.70$.

In Fig. 3, we also can see that $\gamma$ increases with temperature below the glass transition temperature. This is in contrast to polymers like polystyrene for which the Gruneisen parameter decreases with increasing temperature. Interestingly, in our simulations, the Gruneisen parameter appears to go through a maximum at the glass transition temperature and then decreases with temperature in the liquid regime. More will be said about this later in this paper.

![](./images/812522251856379905_10.jpg)

FIG. 3. The Gruneisen parameter as a function of temperature for chains of N = 10 (red circles) from MD simulations. 90% error bars are shown for selected points based on three separate runs (see Table I). The blue square corresponds to a monatomic liquid N = 1. The solid line ($T < T_{\mathrm{g}}$) is the harmonic prediction from Eqs. (16) and (17). The solid curve ($T > T_{\mathrm{g}}$) is the liquid-state theory prediction for $\gamma$. The vertical dashed line marks the glass transition temperature.

### III. THE GLASSY REGIME

Let us now consider the Gruneisen parameter for a bead-spring polymer well below the glass transition temperature. In this regime, large-scale configurational changes are largely suppressed and the structure is effectively frozen in a metastable energy state. Therefore, it is reasonable to assume that the polymer repeat units undergo only harmonic vibrations within a cell²⁰ formed by neighboring atoms. Let us denote the position of a bead i from the center of a cell as $\vec{\mathrm{r}}_{\mathrm{i}}$. Following the work of Prigogine and co-workers,²⁰ we employ a cell model to represent the chain interactions. The potential energy of a bead-spring chain can be written as

$$
\mathrm{V} = \frac{1}{2}\sum_{\mathrm{ij}} \left( \vec{\mathrm{r}}_{\mathrm{i}}\alpha_{\mathrm{ij}}\vec{\mathrm{r}}_{\mathrm{j}} + \delta_{\mathrm{ij}}\mathrm{Kr}_{\mathrm{i}}^{2} \right), \tag{7}
$$

where $\alpha_{\mathrm{ij}}$ is related to the vibrational spring constants and K represents the spring constant²⁰,²¹ for the cell potential in the harmonic approximation. In this model, all the atoms except one are at their respective lattice positions. Thus, we effectively reduce the problem involving many chains to single chain problem. The quadratic form in Eq. (7) can now be diagonalized in the standard manner. The 3N eigenvalues then represent the normal modes of a chain with frequencies $v_{\mathrm{i}}$ given by²⁰

$$
v_{\mathrm{i}} = \frac{1}{2\pi}\left[ (\lambda_{\mathrm{i}} + \mathrm{K})/\mathrm{M} \right]^{1/2}, \quad \mathrm{i} = 1, \ldots, 3\mathrm{N}, \tag{8}
$$

where $\lambda_{\mathrm{i}}$'s are the eigenvalues of the $\alpha_{\mathrm{ij}}$ matrix and M is the mass of a bead.

For the completely flexible, bead-spring model used here, we expect (N − 1) of $\lambda_{\mathrm{i}}$'s to be of the form

$$
\lambda_{\mathrm{i}} = \frac{\mathrm{k}_{\mathrm{bond}}}{2}\lambda_{\mathrm{i}}^{0}, \tag{9a}
$$

where $\lambda_{\mathrm{i}}^{0}$ are eigenvalues of the NxN matrix $\mathrm{A}_{\mathrm{ij}}$. Although it is not essential for our analysis here, we can approximate $\mathrm{A}_{\mathrm{ij}}$ if we assume that the distance between lattice points is equal to the bond length $\ell$. With this approximation, $\mathrm{A}_{\mathrm{ij}}$ is tridiagonal and similar, but not identical, to the Rouse matrix,²²

$$
\begin{gathered}
\mathrm{A}_{\mathrm{ij}} = -\delta_{\mathrm{ij}-1} + 2\delta_{\mathrm{ij}} - \delta_{\mathrm{ij}+1}, \quad \mathrm{i} = 2, 3, \ldots, (\mathrm{N} - 1), \\
\mathrm{A}_{11} = \mathrm{A}_{\mathrm{NN}} = 1, \quad \mathrm{A}_{12} = \mathrm{A}_{\mathrm{N}-1\mathrm{N}} = -1,
\end{gathered} \tag{9b}
$$

where $\delta_{\mathrm{ij}}$ is the usual Kronecker delta. This matrix has N − 1 nonzero eigenvalues given by²³

$$
\lambda_{\mathrm{i}}^{0} = 4\sin^{2}\left( \frac{\mathrm{i}\pi}{2\mathrm{N}} \right), \quad \mathrm{i} = 1, 2, \ldots, (\mathrm{N} - 1), \tag{9c}
$$

with the remaining $\lambda_{\mathrm{i}}$'s equal to zero. Thus, the 3N frequencies in Eq. (8) are decomposed into (N − 1) bond vibration frequencies defined by

$$
v_{\mathrm{i}} = \frac{1}{2\pi}\sqrt{\left( \frac{\frac{\mathrm{k}_{\mathrm{bond}}}{2}\lambda_{1}^{0} + \mathrm{K}}{\mathrm{M}} \right)}, \quad \mathrm{i} = 1, \ldots, (\mathrm{N} - 1), \tag{10}
$$

and (2N + 1) Lennard-Jones frequencies from the cell potential

$$
v_{\mathrm{i}}=\frac{1}{2 \pi} \sqrt{\frac{\mathrm{K}}{\mathrm{M}}}, \quad \mathrm{i}=\mathrm{N}, \ldots, 3 \mathrm{~N}. \tag{11}
$$

From Eq. (10), we note that the bond vibration frequencies are perturbed by the LJ interactions relative to what they would be if we turned off all the nonbonded interactions by setting K = 0.

In the original Lennard-Jones and Devonshire⁴ cell theory, the potential of a test atom in a cell is calculated by summing over nearest neighbor atoms at the centers of their respective lattice sites. Prigogine and Garikian²¹ expanded the Lennard-Jones and Devonshire cell potential to terms quadratic in the distance from the cell center. This harmonic approximation results in the spring constant K given by

$$
\mathrm{K}=\frac{(\mathrm{m}-2) \varepsilon}{\mathrm{a}^{2}}\left[22\left(\frac{\mathrm{V}_{0}}{\mathrm{~V}}\right)^{4}-10\left(\frac{\mathrm{V}_{0}}{\mathrm{~V}}\right)^{2}\right], \tag{12}
$$

where m is the coordination number of the lattice, “a” is the lattice spacing, and V₀ is the volume at zero temperature. Note that in general, the lattice spacing “a” is proportional to V^(1/3) and is not equal to the bond length, as assumed above in approximating λᵢ⁰. From Eq. (9c), we find, for our simulations of N = 10 bead chains, the nonzero eigenvalues λᵢ⁰ approximately range from 0.098 to 3.98. By comparing Eqs. (9) and (12), we see that k_bondλᵢ⁰ ≫ 2K for most of the bond vibration modes.

The Prigogine cell model theory was used previously by Curro¹⁰ to study the differences in the Gruneisen parameter between complex polymers and atomic crystals and glasses. In the present study, we will apply this harmonic cell theory to calculate the Gruneisen parameter of bead-spring chains at low temperature. From Eq. (1), along with Eqs. (8)–(11), we can write the Gruneisen parameter as

$$
\gamma=\frac{\frac{1}{2} \sum_{\mathrm{i}=\mathrm{N}}^{3 \mathrm{~N}} \mathrm{c}_{\mathrm{i}}\left(-\frac{\partial \ln \mathrm{K}}{\partial \ln \mathrm{V}}\right)}{\sum_{\mathrm{i}=1}^{3 \mathrm{~N}} \mathrm{c}_{\mathrm{i}}}+\frac{\frac{1}{2} \sum_{\mathrm{i}=1}^{(\mathrm{N}-1)} \mathrm{c}_{\mathrm{i}}\left(-\frac{\partial \ln \left(\frac{1}{2} \mathrm{k}_{\mathrm{bond}} \lambda_{\mathrm{i}}^{0}+\mathrm{K}\right)}{\partial \ln \mathrm{V}}\right)}{\sum_{\mathrm{i}=1}^{3 \mathrm{~N}} \mathrm{c}_{\mathrm{i}}}. \tag{13}
$$

Since most of the vibrational frequencies are much larger than the Lennard-Jones modes, we make the approximation that the bond vibrations are decoupled from the Lennard-Jones vibrations so that the perturbing effect of K on vibration frequencies in Eq. (13) can be ignored. Since λᵢ⁰ are independent of volume, we can significantly simplify Eq. (13) to read

$$
\gamma=-\frac{1}{2}\left(\frac{\partial \ln \mathrm{K}}{\partial \ln \mathrm{V}}\right) \frac{\sum_{\mathrm{i}=\mathrm{N}}^{3 \mathrm{~N}} \mathrm{c}_{\mathrm{i}}}{\sum_{\mathrm{i}=1}^{3 \mathrm{~N}} \mathrm{c}_{\mathrm{i}}}=\left(\frac{\mathrm{C}_{\mathrm{V}}^{0}}{\mathrm{C}_{\mathrm{V}}}\right) \gamma_{1}, \tag{14}
$$

where γ₁ is the Gruneisen parameter of a monatomic glass, C_V⁰ is the heat capacity with the bond vibrations removed, and C_V is the total heat capacity of the full bead-spring glass,

$$
\gamma_{1}=-\frac{1}{2}\left(\frac{\partial \ln \mathrm{K}}{\partial \ln \mathrm{V}}\right), \quad \mathrm{C}_{\mathrm{V}}^{0}=\sum_{\mathrm{i}=\mathrm{N}}^{3 \mathrm{~N}} \mathrm{c}_{\mathrm{i}}, \quad \mathrm{C}_{\mathrm{V}}=\sum_{\mathrm{i}=1}^{3 \mathrm{~N}} \mathrm{c}_{\mathrm{i}}. \tag{15}
$$

We now make use of the classical equipartition approximation by assuming that each mode contributes k_B T to the total energy. Thus, we can approximate the Gruneisen parameter of a bead-spring glass with the simple formula

$$
\gamma=\frac{(2 \mathrm{~N}+1)}{3 \mathrm{~N}} \gamma_{1}. \tag{16}
$$

For the case of bead-spring chains with N = 10 used in our MD simulations, we have γ = 0.70γ₁. By differentiation of Eq. (12) with respect to volume, using Eq. (15), we find¹⁰ that

$$
\gamma_{1}=\frac{22\left(\mathrm{~V}_{0} / \mathrm{V}\right)^{2}-5}{11\left(\mathrm{~V}_{0} / \mathrm{V}\right)^{2}-5}+\frac{1}{3}. \tag{17}
$$

In the T = 0 limit, we find from Eq. (17) that γ₁ = 3.17, and from Eq. (16), we predict that γ = 2.21 for our bead-spring glass. This is in good agreement with our MD simulations at very low temperatures, as can be seen from the line in Fig. 3. At higher temperatures, it can be seen from Fig. 3 that the simulation points are higher than predicted by the theory. This is likely due, in part, to broadening of the transition region and is discussed later in Sec. V. Note that Eqs. (16) and (17) predict that γ increases slightly with temperature in the glass in contrast to complex polymers that display the opposite trend. From Eq. (16), we also note that there is a 1/N free-volume-like, chain-end correction to γ that disappears in the limit of long chains to give γ = $\frac{2}{3}$γ₁ = 2.11. It should also be mentioned that if our bead-spring model had bond bending or torsional potentials, we would expect from our above arguments that γ would be reduced even further relative to γ₁.

It should be pointed out that the assumption that the bond vibrations are not perturbed by the LJ interactions is not rigorously true for our chains with the bond stretching potential in Eq. (5). In fact, Eq. (13) could be evaluated numerically without assuming that the bond and LJ vibrations are decoupled. Such a numerical calculation is beyond the scope of this investigation. Nevertheless, the Gruneisen expression in Eq. (16) can be viewed as a lower bound of the more exact calculation. For systems where the bond vibration frequencies are higher, the decoupling approximation becomes progressively more accurate. On the other extreme, if the bond vibration frequency is sufficiently small, then k_bondλᵢᴿ ≪ 2K. In this case, the Gruneisen parameter can be seen from Eq. (13) to be the same as for the monomer glass γ = γ₁.

We point out here an interesting formula for the Gruneisen parameter of an ideal crystal lattice in D dimensions derived recently by Krivtsov and Kuz’kin.²⁵ Consider the case of the Mie potential¹ defined by

$$
\mathrm{v}(\mathrm{r})=\varepsilon\left(\frac{\mathrm{n}}{\mathrm{n}-\mathrm{m}}\right)\left(\frac{\mathrm{n}}{\mathrm{m}}\right)^{\mathrm{m} /(\mathrm{n}-\mathrm{m})}\left[\left(\frac{\sigma}{\mathrm{r}}\right)^{\mathrm{n}}-\left(\frac{\sigma}{\mathrm{r}}\right)^{\mathrm{m}}\right] \tag{18}
$$

as a generalization of the LJ potential. Counting nearest neighbor interactions only, Krivtsov and Kuz’kin derived a formula for the Gruneisen parameter

$$
\gamma_{1}=\frac{\mathrm{m}+\mathrm{n}+4}{2 \mathrm{D}}-\frac{1}{2} \tag{19}
$$

in the T = 0 limit. For the special case of the Lennard-Jones potential (n = 12 and m = 6) in three dimensions, Eq. (19) reduces to γ₁ = $\frac{19}{6}$ = 3.17. As to be expected, this is identical to the cell model result since both calculations make the same assumptions. Note that

Eq. (19) demonstrates that the Gruneisen parameter can be consid- ered as a measure of the steepness of the repulsive interactions. This sensitivity of the Gruneisen parameter to the repulsive exponent (n)has been discussed previously by Roland et al. $^{26}$

The simulations, and hence the theory presented here, are for classical systems. It should be mentioned that in real poly- mers, quantum effects are important. In particular, from the Debye model, $^{27}$ both the heat capacities $C_{V}^{0}$ and $C_{V}$ in Eq. (15) would be expected to approach zero as $T^{3}$ and increase with temperature. As a consequence, the ratio $C_{V}^{0} / C_{V}$ in Eq. (14) and, therefore, $\gamma$ decrease with temperature. As an example, quantum effects were included in the earlier calculations of Curro $^{10}$ describing polystyrene and poly methyl methacrylate. This was done by inserting the vibrational fre- quencies, determined from spectroscopy, directty into Eq. (1c) for the heat capacities.

## IV. THE LIQUID REGIME
Above the glass transition temperature, the harmonic approx- imation breaks down and the frequency interpretation of the Gruneisen parameter in Eq. (1) loses its meaning. Therefore, in the liquid regime, we will focus on the thermodynamic definitions of y given in Eq. (2). Our aim in this section is to apply liquid state theoretical methods to develop a theory for the Gruneisen parame-ter of bead-spring chains. More specifically, we will employ Eq. (2c) as a route to $\gamma$ . Toward that end, we will carry out the following steps: (1) The LJ interactions between the nonadjacent beads will be mapped to equivalent hard spheres using the well-known pro- cedures from Barker and Henderson $^{28}(BH)$ and Weeks, Chandler, and Andersen $^{29}$ (WCA). (2) An equation-of-state for these hard sphere chains will be employed to evaluate the thermal pressure( P/ T)y. (3) The heat capacity will then be calculated from the Polymer Reference Interaction Model (PRISM) theory and used in Eq. (2c) to find the Gruneisen parameter for the hard sphere chain system. (4) Thermodynamic perturbation theory $^{28-30}$ will then be used to correct the hard-core Gruneisen parameter for attractive interactions.

Following the work of Weeks et al., $^{29}$ we divide the LJ potential v(r) into a repulsive reference part $v_{0}(r)$ and an attractive part $v_{a}(r)$ ,
$$
\begin{gathered}
\mathrm{v}(\mathrm{r})=4 \varepsilon\left[\left(\frac{\sigma}{\mathrm{r}}\right)^{12}-\left(\frac{\sigma}{\mathrm{r}}\right)^{6}\right], \\
\mathrm{v}_{0}(\mathrm{r})=\mathrm{v}(\mathrm{r})+\varepsilon, \quad \mathrm{r}<2^{1 / 6} \sigma, \quad \mathrm{v}_{0}(\mathrm{r})=0, \quad \mathrm{r} \geq 2^{1 / 6} \sigma, \\
\mathrm{v}_{\mathrm{a}}(\mathrm{r})=-\varepsilon, \quad \mathrm{r}<2^{1 / 6} \sigma, \quad \mathrm{v}_{\mathrm{a}}(\mathrm{r})=\mathrm{v}(\mathrm{r}), \quad \mathrm{r} \geq 2^{1 / 6} \sigma.
\end{gathered}
$$

Note that the reference potential $v_{0}(r)$ consists of the LJ potential that is shifted up to zero and clipped at the minimum. The effectivehard-core diameter d is then calculated from the BH formula $^{28,30}$ 
$$\mathrm{d}=\int_{0}^{\infty}\left\{1-\exp \left[-\mathrm{v}_{0}(\mathrm{r}) / \mathrm{k}_{\mathrm{B}} \mathrm{T}\right]\right\} \mathrm{dr}.\qquad(21)$$

The hard-core diameters d were calculated from this equation at the temperatures of the MD simulations; the results are given in Table Il. The corresponding densities $\rho \sigma^{3}$ were rescaled to the equivalent hard-core densities $\rho d^{3}$ also shown in Table II.

<table>
<caption>TABLE II. Theoretical results above $T_{g}$.</caption>
<thead>
  <tr>
    <th>T</th>
    <th>$\rho\sigma^{3}$</th>
    <th>d/σ</th>
    <th>$\rho d^{3}$</th>
    <th>$V(dP/dT)_{V}$</th>
    <th>$C^{*}$</th>
    <th>$\gamma_{0}$</th>
    <th>$\gamma$</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>0.40</td>
    <td>1.0389</td>
    <td>0.9989</td>
    <td>1.0355</td>
    <td>9.858</td>
    <td>3.171</td>
    <td>3.108</td>
    <td>3.228</td>
  </tr>
  <tr>
    <td>0.44</td>
    <td>1.0301</td>
    <td>0.9985</td>
    <td>1.0255</td>
    <td>9.265</td>
    <td>3.168</td>
    <td>2.924</td>
    <td>3.100</td>
  </tr>
  <tr>
    <td>0.48</td>
    <td>1.0159</td>
    <td>0.9981</td>
    <td>1.0106</td>
    <td>8.901</td>
    <td>3.165</td>
    <td>2.813</td>
    <td>2.919</td>
  </tr>
  <tr>
    <td>0.50</td>
    <td>1.0107</td>
    <td>0.9978</td>
    <td>1.0040</td>
    <td>8.442</td>
    <td>3.162</td>
    <td>2.670</td>
    <td>2.844</td>
  </tr>
  <tr>
    <td>0.52</td>
    <td>1.0006</td>
    <td>0.9976</td>
    <td>0.9934</td>
    <td>8.118</td>
    <td>3.158</td>
    <td>2.571</td>
    <td>2.726</td>
  </tr>
  <tr>
    <td>0.60</td>
    <td>0.9821</td>
    <td>0.9965</td>
    <td>0.9718</td>
    <td>7.385</td>
    <td>3.151</td>
    <td>2.344</td>
    <td>2.504</td>
  </tr>
  <tr>
    <td>0.70</td>
    <td>0.9546</td>
    <td>0.9950</td>
    <td>0.9404</td>
    <td>6.679</td>
    <td>3.140</td>
    <td>2.127</td>
    <td>2.215</td>
  </tr>
</tbody>
</table>

In this investigation, we use the PRISM theory of Curro and Schweizer $^{31-33}$ to characterize the intermolecular structure of bead spring chain liquids with hard-core interactions between the beads. The intermolecular structure is specified by the intermolecular radial distribution function g(r) between pairs of beads on different chains. The PRISM theory relates g(r) to the single-chain structure fac- tor $\hat{\omega}(k)$ through a generalized Ornstein-Zernike equation. $^{34}$ The Ornstein-Zernike equation together with an approximation (clo- sure) for the direct correlation function C(r) allows one to calcu- late g(r) for a given model of the intramolecular structure $\hat{\omega}(k)$ . See Appendix A for a more detailed description of PRISM the- ory. In this work, we used a modified freely jointed chain model for $\hat{\omega}(k)$ where unphysical overlaps of nearby beads along a chain are removed. To solve the PRISM equations, we made use of the Python-based pyPRISM code of Martin and co-workers $^{35}$ to cal culate g(r) for our system. The results are shown in Fig. 4 for four different densities above $T_{g}$ .

![](./images/812522251856379905_11.jpg)

The equation-of-state can be computed from PRISM theory. However, the pressure is typically found to be too low when using the compressibility route, and too high via the virial route.³⁶ Instead, we employed the generalized Flory dimer (GFD) theory of Dickman, Hall, and Honnell,³⁷,³⁸ which has been demonstrated to be a more accurate equation-of-state.³⁹,⁴⁰ The GFD theory relates the compressibility factor ($Z = P/\rho T$) of a liquid of hard chains to those of a hard sphere liquid ($N = 1$) and a fluid composed of hard dimers ($N = 2$). The compressibility factor $Z(N,\eta)$ of an N-mer is then written as a weighted average,

$$Z(N,\eta) = (1 + Y_{\text{N}})Z(2,\eta) - Y_{\text{N}}Z(1,\eta),\tag{22a}$$

where $\eta$ is the packing fraction; $Z(1,\eta)$ and $Z(2,\eta)$ are compressibility factors for monomers and dimers, respectively. The weighting factor $Y_{\text{N}}$ is given by

$$Y_{\text{N}} = \frac{v_{\text{e}}(\text{N}) - v_{\text{e}}(2)}{v_{\text{e}}(2) - v_{\text{e}}(1)},\tag{22b}$$

where $v_{\text{e}}(\text{n})$ is the volume excluded by an n-mer to a monomer averaged over all conformations of the n-mer. In GFD theory, the Carnahan and Starling equation⁴¹ is used for $Z(1,\eta)$, and the Tildesley and Streett⁴² equation is used for $Z(2,\eta)$. The exclusion volumes $v_{\text{e}}$ were evaluated for our system with the hard-core diameter d of the beads and the bond length $\ell = 0.90\sigma$. The details of the expressions used in the GFD theory are given in Appendix B. The pressure of our 10-bead chain system was calculated from Eq. (22) and found to be linear with temperature. The slopes of these lines gave us the thermal pressures shown in Table II.

The internal energy of the bead-spring liquid has several contributions that we express as

$$
\begin{align*}
\text{E} &= \text{E(kinetic)} + \text{E(springs)} + \text{E}_{\text{intra}} + \text{E}_{\text{inter}} \\
&= \frac{3}{2}\text{nN}\varepsilon\text{T} + \frac{3}{2}\text{n(N} - 1)\varepsilon\text{T} + \text{E}_{\text{intra}} + \text{E}_{\text{inter}}.\tag{23a}
\end{align*}
$$

The intramolecular and intermolecular contributions to E can be written²⁹ in terms of the attractive interactions in Eq. (20),

$$\frac{\text{E}_{\text{intra}}}{\text{nN}} = 4\pi\rho\int_{0}^{\infty}\omega(\text{r})\text{v}_{\text{a}}(\text{r})\text{r}^{2}\text{dr},\tag{23b}$$

$$\frac{\text{E}_{\text{inter}}}{\text{nN}} = 2\pi\rho\int_{0}^{\infty}\text{g}_{0}(\text{r})\text{v}_{\text{a}}(\text{r})\text{r}^{2}\text{dr}.\tag{23c}$$

The intermolecular radial distribution function $\text{g}_{0}(\text{r})$ above is taken from the hard-core reference system with hard-core diameter d. We then numerically integrated Eq. (23c) to obtain the intermolecular internal energy as a function of temperature. These results are plotted in Fig. 5 for several densities. From Fig. 5, we see that $\text{E}_{\text{inter}}$ is linear in temperature at all the densities studied.

We now define a dimensionless heat capacity $\text{C}^{*}$ at constant volume by differentiating Eq. (23a) with respect to temperature,

$$\text{C}^{*} \equiv \frac{\text{C}_{\text{V}}}{\text{nN}\varepsilon} = \frac{3}{2} + \frac{3}{2}\left(1 - \frac{1}{\text{N}}\right) + 2\pi\rho\left(\frac{\partial\text{E}_{\text{inter}}/\text{nN}\varepsilon}{\partial\text{T}}\right)_{\text{V}}.\tag{24}$$

Since the intramolecular structure function $\hat{\omega}(\text{k})$ is inputted directly into PRISM theory and is not determined self-consistently, the intramolecular internal energy in Eq. (23b) does not depend on temperature and, therefore, does not contribute to $\text{C}^{*}$. However, there is a nonzero intermolecular contribution to the heat capacity. This is because the effective hard-core diameter d, and hence $\text{g}_{0}(\text{r})$, does depend on temperature, as can be seen in Table II. From the slopes of the energy vs temperature lines in Fig. 5, together with Eq. (24), we determined the reduced heat capacity $\text{C}^{*}$ as a function of density. These results are given in Table II. We are now in a position to estimate the Gruneisen parameter $\gamma_{0}$ for the hard-core reference system of bead-spring chains. From Eq. (2c), we can deduce $\gamma_{0}$ from the thermal pressure and the heat capacity. These hard-core Gruneisen parameters are given in Table II.

![](./images/812522251856379905_12.jpg)

FIG. 5. The intermolecular internal energy, calculated from Eq. (23c), as a function of temperature at the following densities $\rho\sigma^{3}$ (bottom to top): 1.0389, 1.0301, 1.0159, 1.0107, 1.0006, 0.9821, and 0.9546. The blue dashed line depicts the constant pressure ($P = 0$) path.

A further refinement in the Gruneisen parameter can be achieved using the perturbation approach of Weeks, Chandler, and Andersen.²⁹ If the attractive interactions $\text{v}_{\text{a}}(\text{r})$ in Eq. (20) are weak, we can approximate the Helmholtz free energy A to first order as

$$\frac{\text{A}}{\text{nN}} \cong \frac{\text{A}_{0}}{\text{nN}} + 2\pi\rho\int_{0}^{\infty}\text{g}_{0}(\text{r})\text{v}_{\text{a}}(\text{r})\text{r}^{2}\text{dr},\tag{25}$$

where $\text{A}_{0}$ is the Helmholtz free energy of the repulsive reference system. From Eq. (23c), we recognize that the integral on the RHS of Eq. (25) is just the intermolecular internal energy,

$$\text{A} = \text{A}_{0} + \text{E}_{\text{inter}} = \text{A}_{0} + \text{E} - \frac{3}{2}\text{nN}\varepsilon\text{T} - \frac{3\text{nN}\varepsilon}{2}\left(1 - \frac{1}{\text{N}}\right)\text{T} - \text{E}_{\text{intra}},\tag{26}$$

where in the second line we substituted for $\text{E}_{\text{inter}}$ from Eq. (23a). Starting with Eq. (26), thermodynamic arguments can be used to

![](./images/812522251856379905_13.jpg)

FIG. 6. Reciprocal heat capacity vs natural logarithm of the density. The fit to the data gives a straight line of slope −0.0370.

relate the Gruneisen parameter $\gamma$ to that of the corresponding hard-core system $\gamma_0$,

$$
\Delta \gamma = \gamma - \gamma_0 = -\frac{3}{2} \left( 2 - \frac{1}{\mathrm{N}} \right) \left( \frac{\partial (1/C^*)}{\partial \ln \rho \sigma^3} \right)_T. \tag{27}
$$

The thermodynamic arguments leading to Eq. (27) are detailed in Appendix C. From the data in Table II, we plotted the reciprocal heat capacity vs $ln\rho\sigma^3$ in Fig. 6. From the slope of the straight line, we find from Eq. (27) that we get a constant correction in the Gruneisen parameter of $\Delta \gamma = 0.105$ for chains of 10 beads. This correction is small, as anticipated from van der Waals theory, and is a necessary requirement in the perturbation approach. The attraction correction was applied to $\gamma_0$, and the results are plotted in Fig. 3. It can be seen that the theoretical curve is in good qualitative agreement with the MD simulations.

## V. TRANSITION REGIME

From Fig. 3, it can be seen that the theoretical predictions show that the Gruneisen parameter increases slightly with temperature below $T_g$ and decreases strongly with temperature above $T_g$. In between, the MD simulations appear to go through a maximum at about the glass transition temperature. In order to compare with experimental data on real polymers, in Fig. 7, we re-plotted the results from Fig. 3 as a function of $T/T_g$. Also shown are experimental data on polystyrene of Curro $^{10}$ where the squares were determined from experimental thermal expansion coefficients, compressibilites, and heat capacities via Eq. (2b). The triangles indicate the Gruneisen parameters determined via Eq. (2a) from energy deposition experiments of Gauster $^8$ on polystyrene. Note that the Gruneisen parameter for the bead-spring system is significantly larger than for polystyrene as we anticipated.

![](./images/812522251856379905_14.jpg)

FIG. 7. The Gruneisen parameter as a function of $T/T_g$ for chains of N = 10 (red circles) from MD simulations. The blue squares and triangles are experimental data on PS from Ref. 10. The solid line ($T < T_g$) is the harmonic prediction, and the solid curve ($T > T_g$) is the liquid-state theory prediction for $\gamma$. The vertical dashed line marks the glass transition temperature. The red short dashed line is an estimate of the breadth of the transition from simulations on PS in Ref. 15.

It can be seen from Fig. 7 that polystyrene undergoes a sharp, discontinuous up-jump in $\gamma$ at $T_g$. This is what we expect since $\gamma$ is a combination of three thermodynamic functions: the thermal expansion, isothermal compressibility, and heat capacity, all of which are discontinuous at $T_g$. Whether $\gamma$ experiences an up-jump or a down-jump depends on which of the three thermodynamic functions wins out in Eq. (2b),

$$
\gamma_+ \cong \gamma_- (1 + \Delta \alpha/\alpha_- - \Delta \kappa/\kappa_- - \Delta C_V/C_{V-}), \tag{28}
$$

where $\gamma_-$ and $\gamma_+$ are the Gruneisen parameters below and above $T_g$, and $\Delta \alpha$, $\Delta \kappa$, and $\Delta C_V$ refer to the jumps at $T_g$. Based on this argument, we would expect the bead-spring chain simulations to also exhibit a discontinuous change in $\gamma$ at the glass transition. In Fig. 7, we can see that this does not appear to be the case.

Recently, Godey, Bensaid, and Soldera $^{15}$ performed MD simulations on polystyrene and polyethylene above and below the glass transition. They reported Gruneisen parameters where the transition region is very broad, suggesting that the transition region for our bead-spring chain simulations should also be large. As a result, the sharp discontinuous change in $\gamma$ seen in experiments is smeared out in our MD simulations because of the breadth of the transition region. In Fig. 7, the dashed red line marks the approximate breadth of the transition region for PS from Godey et al. $^{15}$ This

seems to apply to our MD simulations as well. We speculate that the reason that the glass transition is broad in these simulations is due to finite size effects inherent in computer simulations. Finite size effects on first and second order transitions were studied by Binder.⁴⁴ Additionally, it is well known that the glass transition temperature depends on the sample thickness in both experiments and bead-spring MD simulations.¹⁸ Another contributing factor to the breadth of the transition could be that our simulations are trapped in various metastable states below the glass transition temperature. A broad distribution of these metastable energy states could lead to large variations in physical properties. The extreme cooling rates required in the simulations not only raise the glass transition temperature but could also broaden the distribution of energy states in the glass.

## VI. CONCLUSIONS

We carried out MD simulations on bead-spring liquids having 10 beads per chain over a temperature range above and below the glass transition. As seen clearly in Fig. 7, the Gruneisen parameters of the bead-spring MD simulations and theory are significantly larger (~5 times at $T_\text{g}$) than the experimental data on polystyrene. This was anticipated from the early work of Curro¹⁰ and is a result of polystyrene having many more high frequency modes of energy absorption that do not contribute to the pressure.

At low temperatures, we made a harmonic approximation based on the work of Prigogine,²⁰,²¹ which results in a theoretical Gruneisen parameter that increases slightly with temperature in the glass. For temperatures above the glass transition, we used the generalized Flory dimer theory³⁷,³⁸ for the equation-of-state and PRISM theory³¹⁻³³ to calculate the heat capacity. The resulting Gruneisen parameter decreased markedly with temperature. The theoretical predictions for the Gruneisen parameter were in good qualitative agreement with our MD simulations in both the glass and the liquid regimes. It should be mentioned that no adjustable parameters were used in either theory.

Our MD simulations exhibited a broad transition region where $\gamma$ varies smoothly with temperature and goes through an apparent maximum. Similar behavior of the Gruneisen parameter has been observed in other MD simulations by Godey *et al.*¹⁵ This is in contrast to the sharp jump in $\gamma$ at $T_\text{g}$ seen in experiments on real polymers. We speculate that the broad transition regime is due to the finite system size inherent in computer simulations.

## APPENDIX A: PRISM THEORY

In PRISM theory,³¹⁻³³ the intermolecular pair correlation function g(r) is related to the direct correlation function C(r) through the generalized Ornstein-Zernike equation³⁴ shown in Fourier space,
$$
\hat{\mathrm{h}}(\mathrm{k})=\hat{\omega}(\mathrm{k}) \hat{\mathrm{C}}(\mathrm{k}) \hat{\omega}(\mathrm{k})+\rho \hat{\omega}(\mathrm{k}) \hat{\mathrm{C}}(\mathrm{k}) \hat{\mathrm{h}}(\mathrm{k}), \tag{A1}
$$
where the caret symbol denotes Fourier transformation with wave vector k, h(r)(= g(r) − 1) is the total intermolecular correlation function, and $\hat{\omega}(\mathrm{k})$ is the single chain structure factor defined as
$$
\hat{\omega}(\mathrm{k})=\frac{1}{\mathrm{~N}} \sum_{\alpha \gamma=1}^{\mathrm{N}} \hat{\omega}_{\alpha \gamma}(\mathrm{k}). \tag{A2}
$$
$\omega_{\alpha \gamma}(\mathrm{r})$ is the probability that two beads $\alpha$ and $\gamma$ on the same chain are separated by a distance r. C(r) is the direct correlation function. The generalized Ornstein-Zernike equation can be viewed as a relationship between the intermolecular correlations g(r) and the intramolecular structure $\hat{\omega}(\mathrm{k})$. In order to solve for g(r), we need to make a closure approximation for C(r). For chains in which the beads interact with a hard sphere potential, g(r) must vanish inside the hard core. Here, we will employ the Percus-Yevick closure³¹⁻³³ that approximates the direct correlation as zero outside the hard-core diameter d,
$$
\begin{aligned}
& \mathrm{h}(\mathrm{r})=-1, \quad \mathrm{r}<\mathrm{d}, \\
& \mathrm{C}(\mathrm{r})=0, \quad \mathrm{r}>\mathrm{d}.
\end{aligned} \tag{A3}
$$

In general, the intermolecular correlations and intramolecular structure are coupled together and need to be solved in a self-consistent manner. Such calculations are possible and have been carried out on realistic models of polyolefins⁴³ with results that are in good agreement with MD simulations. Here, we avoid the self-consistent computations by making use of the Flory ideality hypothesis and approximate the chains in the liquid state as being ideal. In other words, the intermolecular and intramolecular excluded volume forces cancel each other out so the average radius of gyration $\mathrm{R}_\mathrm{g} \propto \mathrm{N}^{1 / 2}$. This allows us to compute the intramolecular structure function $\hat{\omega}(\mathrm{k})$ from Eq. (A2) in a separate single chain calculation. One of the simplest polymer models is the freely jointed chain (FJC) model for which the single chain structure factor $\hat{\omega}_0(\mathrm{k})$ can be computed in closed form,³⁶
$$
\hat{\omega}_{0}(\mathrm{k})=\frac{\left[1-\mathrm{f}^{2}-2(\mathrm{f} / \mathrm{N})+2\left(\mathrm{f}^{\mathrm{N}+1} / \mathrm{N}\right)\right]}{(1-\mathrm{f})^{2}}, \quad \mathrm{f}=\sin (\mathrm{k} \ell / \mathrm{k} \ell). \tag{A4}
$$

A problem with the FJC model is that it allows for unphysical overlaps of beads. To improve on this model, Schweizer and Curro³⁶ devised the non-overlapping freely jointed chain model (NFJC). In this approach, some of the individual $\omega_{\alpha \gamma}(\mathrm{r})$ intramolecular probabilities are set to zero for r < d and as freely jointed chains for r > d,
$$
\hat{\omega}(\mathrm{kd})=\hat{\omega}_{0}(\mathrm{kd})+\frac{2}{\mathrm{~N}} \sum_{\tau=2}^{\mathrm{N}-1}\left[\hat{\omega}_{\tau}(\mathrm{kd})-\left(\frac{\sin (\mathrm{kd})}{\mathrm{kd}}\right)^{\tau}\right]. \tag{A5}
$$

The reader is directed to Ref. 36 for the details involving the calculation of $\hat{\omega}_\tau(\mathrm{kd})$. Equations (A1), (A3), and (A5) can now be solved numerically using a Picard iteration technique. In this work, we employed the Python-based pyPRISM code of Martin and co-workers³⁵ for this purpose.

## APPENDIX B: VARIABLES IN THE CFD THEORY

The various exclusion volumes³⁷⁻⁴⁰ we used in Eq. (24) are as follows:
$$
\mathrm{v}_{\mathrm{e}}(1)=\frac{4 \pi \mathrm{d}^{3}}{3}, \tag{B1}
$$

$$
\mathrm{v}_{\mathrm{e}}(2)=\frac{4 \pi \mathrm{d}^{3}}{3}\left\{1+\frac{3}{4}\left(\frac{\ell}{\mathrm{d}}\right)-\frac{1}{2}\left(\frac{\ell}{2 \mathrm{~d}}\right)^{3}\right\}, \tag{B2}
$$

$$
\mathrm{v}_{\mathrm{e}}(3) \cong 9.826 \mathrm{d}^{3}, \tag{B3}
$$


$$\mathrm{v}_{\mathrm{e}}(\mathrm{N}) \cong \mathrm{v}_{\mathrm{e}}(3)+(\mathrm{N}-3)\left[\mathrm{v}_{\mathrm{e}}(3)-\mathrm{v}_{\mathrm{e}}(2)\right]. \tag{B4}$$

It should be mentioned that the monomer exclusion volume for a trimer in Eq. (B3) was derived by Honnell and Hall⁴⁸ for tangent hard spheres. For computational expediency, we used Eq. (B3) without correcting for overlapping of hard spheres in the fused-sphere trimer.

The Carnahan-Starling equation for monomer liquids is given by⁴¹
$$\mathrm{Z}(\eta, 1)=\frac{1+\eta+\eta^{2}-\eta^{3}}{(1-\eta)^{3}}. \tag{B5}$$

The Tildesley-Streett equation, generalized for fused-sphere dimers, is somewhat involved, and we reproduce⁴² it here,
$$\mathrm{Z}(2, \eta)=\frac{1+\mathrm{f}_{1} \eta+\mathrm{f}_{2} \eta^{2}-\mathrm{f}_{3} \eta^{3}}{(1-\eta)^{2}}, \tag{B6}$$

$$\mathrm{f}_{1}=1+\mathrm{a}_{1}\left(\frac{\ell}{\mathrm{d}}\right)+\mathrm{a}_{2}\left(\frac{\ell}{\mathrm{d}}\right)^{3},$$

$$\mathrm{f}_{2}=1+\mathrm{a}_{3}\left(\frac{\ell}{\mathrm{d}}\right)+\mathrm{a}_{4}\left(\frac{\ell}{\mathrm{d}}\right)^{3},$$

$$\mathrm{f}_{3}=1+\mathrm{a}_{5}\left(\frac{\ell}{\mathrm{d}}\right)+\mathrm{a}_{6}\left(\frac{\ell}{\mathrm{d}}\right)^{3},$$

$\mathrm{a}_{1}=0.378$ 36, $\quad \mathrm{a}_{2}=1.078$ 60, $\quad \mathrm{a}_{3}=1.303$ 76,
$\mathrm{a}_{4}=1.800$ 10, $\quad \mathrm{a}_{5}=2.398$ 03, $\quad \mathrm{a}_{6}=0.357$ 00.

Since for the bead-spring chains studied here, the bond length is less than the hard-core diameter, we need to account for overlapping of beads in the calculation of the packing fraction $\eta$. We made the approximation that only overlaps of adjacent beads need to be accounted for. This leads to the following approximate expression relating the packing fraction to the density:
$$\eta=\frac{\pi \rho \mathrm{d}^{3}}{6}\left[1-\frac{1}{2}\left(1-\frac{1}{\mathrm{~N}}\right)\left(1-\frac{\ell}{\mathrm{d}}\right)^{2}\left(2+\frac{\ell}{\mathrm{d}}\right)\right]. \tag{B7}$$

## APPENDIX C: THERMODYNAMIC RELATIONS IN PERTURBATION THEORY

We begin by differentiating Eq. (26) with respect to $\mathrm{dE}$ at constant $\mathrm{V}$,
$$
\begin{aligned}
\left(\frac{\partial \mathrm{A}}{\partial \mathrm{E}}\right)_{\mathrm{V}}-\left(\frac{\partial \mathrm{A}_{0}}{\partial \mathrm{E}}\right)_{\mathrm{V}} &=1-\frac{3 \mathrm{Nn} \varepsilon}{2}\left(2-\frac{1}{\mathrm{~N}}\right)\left(\frac{\partial \mathrm{T}}{\partial \mathrm{E}}\right)_{\mathrm{V}} \\
&=1-\frac{3 \mathrm{Nn} \varepsilon}{2}\left(2-\frac{1}{\mathrm{~N}}\right)\left(\frac{1}{\mathrm{C}_{\mathrm{V}}}\right). \tag{C1}
\end{aligned}
$$

Our next step is to differentiate the above equation with respect to volume at constant $\mathrm{T}$,
$$
\left[\frac{\partial}{\partial \mathrm{V}}\left(\frac{\partial \mathrm{A}}{\partial \mathrm{E}}\right)_{\mathrm{V}}\right]_{\mathrm{T}}-\left[\frac{\partial}{\partial \mathrm{V}}\left(\frac{\partial \mathrm{A}_{0}}{\partial \mathrm{E}}\right)_{\mathrm{V}}\right]_{\mathrm{T}}=-\frac{3 \mathrm{Nn} \varepsilon}{2}\left(2-\frac{1}{\mathrm{~N}}\right)\left[\frac{\partial\left(1 / \mathrm{C}_{\mathrm{V}}\right)}{\partial \mathrm{V}}\right]_{\mathrm{T}}. \tag{C2}
$$

We now reverse the order of differentiation to get
$$
\left[\frac{\partial}{\partial \mathrm{E}}\left(\frac{\partial \mathrm{A}}{\partial \mathrm{V}}\right)_{\mathrm{T}}\right]_{\mathrm{V}}-\left[\frac{\partial}{\partial \mathrm{E}}\left(\frac{\partial \mathrm{A}_{0}}{\partial \mathrm{V}}\right)_{\mathrm{T}}\right]_{\mathrm{V}}=-\frac{3 \mathrm{Nn} \varepsilon}{2}\left(2-\frac{1}{\mathrm{~N}}\right)\left[\frac{\partial\left(1 / \mathrm{C}_{\mathrm{V}}\right)}{\partial \mathrm{V}}\right]_{\mathrm{T}}. \tag{C3}
$$

Using the identity $\mathrm{P}=-(\partial \mathrm{A} / \partial \mathrm{V})_{\mathrm{T}}$, we can simplify Eq. (C3) to obtain
$$
\left[\frac{\partial \mathrm{P}}{\partial \mathrm{E}}\right]_{\mathrm{V}}-\left[\frac{\partial \mathrm{P}_{0}}{\partial \mathrm{E}}\right]_{\mathrm{V}}=\frac{3 \mathrm{Nn} \varepsilon}{2}\left(2-\frac{1}{\mathrm{~N}}\right)\left[\frac{\partial\left(1 / \mathrm{C}_{\mathrm{V}}\right)}{\partial \mathrm{V}}\right]_{\mathrm{T}}. \tag{C4}
$$

From the definition of the Gruneisen parameter from Eq. (2a), it can be seen that Eq. (C4) can be written as
$$\Delta \gamma \equiv \gamma-\gamma_{0}=\frac{3}{2}\left(2-\frac{1}{\mathrm{~N}}\right)\left[\frac{\partial\left(1 / \mathrm{C}^{*}\right)}{\partial \ln \mathrm{V}}\right]_{\mathrm{T}}. \tag{C5}$$

For our purposes, it is more convenient to rewrite the above volume derivative as the corresponding density derivative to finally arrive at the desired equation (27),
$$\Delta \gamma \equiv \gamma-\gamma_{0}=-\frac{3}{2}\left(2-\frac{1}{\mathrm{~N}}\right)\left[\frac{\partial\left(1 / \mathrm{C}^{*}\right)}{\partial \ln \rho \sigma^{3}}\right]_{\mathrm{T}}. \tag{C6}$$

## DATA AVAILABILITY

The data that support the findings of this study are available from the corresponding author upon reasonable request.

## REFERENCES
¹E. Grüneisen, *Ann. Phys.* **344**, 257 (1912); G. Mie, *ibid.* **316**, 657 (1903).
²J. G. Curro, *J. Macromol. Sci., Part C: Polym. Rev.* **11**, 321 (1974).
³S. D. Ramsey, E. M. Schmidl, Z. M. Boyd, J. F. Lilieholm, and R. S. Baty, *Phys. Fluids* **30**, 046101 (2018).
⁴Y. Wada, A. Itani, T. Nishi, and S. Nagai, *J. Polym. Sci., Part A-2: Polym. Phys.* **7**, 201 (1969).
⁵J. K. Kruger, K. P. Bohn, and J. Schreiber, *Phy. Rev. B* **54**, 15767 (1996).
⁶D. C. Johnston, *Advances in Thermodynamics of the van der Waals Fluid* (Morgan Claypool, San Rafael, CA, 2014); arXiv:1402.1205.
⁷R. A. Graham and R. E. Hutchison, *Appl. Phys. Lett.* **11**, 69 (1967).
⁸W. B. Gauster, *Phys. Rev. B* **4**, 1288 (1971).
⁹D. S. Sanditov, A. A. Mashanov, M. V. Darmaev, B. D. Sanditov, and V. V. Mantatov, *Russ. Phys. J.* **52**, 221 (2009).
¹⁰J. G. Curro, *J. Chem. Phys.* **58**, 374 (1973).
¹¹C. K. Wu and M. Shen, *J. Macromol. Sci. Phys. B* **7**, 559 (1973).
¹²T. L. Chantawansri, T. W. Sirk, E. F. C. Byrd, J. W. Andzelm, and B. M. Rice, *J. Chem. Phys.* **137**, 204901 (2012).
¹³B. Arman, A. Srinivas Reddy, and G. Arya, *Macromolecules* **45**, 3247 (2012).
¹⁴V. Agrawal, P. Peralta, Y. Li, and J. Oswald, *J. Chem. Phys.* **145**, 104903 (2016).
¹⁵F. Godey, M. O. Bensaid, and A. Soldera, *Polymer* **164**, 33 (2019).
¹⁶S. J. Plimpton, *Comput. Phys.* **117**, 1 (1995).
¹⁷K. Kremer and G. S. Grest, *J. Chem. Phys.* **92**, 5057 (1990).
¹⁸C. S. Stevenson, J. G. Curro, and J. D. McCoy, *J. Chem. Phys.* **146**, 203322 (2017).
¹⁹D. Siderius, https://www.nist.gov/mml/csd/informatics/lammps-md-equation-state-pressure-vs-density-linear-force-shifted-potential-25s.
²⁰I. Prigogine, N. Trappeniers, and V. Mathot, *Discuss. Faraday Soc.* **15**, 93 (1953).

$^{21}$I. Prigogine and G. Garikian, *Physica* **16**, 239 (1950).

$^{22}$P. E. Rouse, *J. Chem. Phys.* **21**, 1272 (1953).

$^{23}$J. Wuttke, "Macromolecular dynamics: An introductory lecture," in *Macromolecular Systems in Soft and Living Matter*, Lecture Notes 42nd IFF Spring School, edited by J. K. G. Donth *et al.* (Schriften des Forschungszentrums Julich, 2011).

$^{24}$J. E. Lennard-Jones and A. F. Devonshire, *Proc. R. Soc. London, Ser. A* **163**, 53 (1937).

$^{25}$A. M. Krivtsov and V. A. Kuz'kin, *Mech. Solids* **46**, 387 (2011).

$^{26}$C. M. Roland, J. L. Feldman, and R. Casalini, *J. Non-Cryst. Solids* **352**, 4895 (2006).

$^{27}$C. Kittel, *Introduction to Solid State Physics*, 8th ed. (John Wiley and Sons, New York, 2004).

$^{28}$J. A. Barker and D. Henderson, *J. Chem. Phys.* **47**, 4714 (1967).

$^{29}$J. D. Weeks, D. Chandler, and H. C. Andersen, *J. Chem. Phys.* **54**, 5237 (1971).

$^{30}$J. P. Hanson and I. R. McDonald, *Theory of Simple Liquids* (Academic, London, 1986).

$^{31}$J. G. Curro and K. S. Schweizer, *Macromolecules* **20**, 1928 (1987).

$^{32}$K. S. Schweizer and J. G. Curro, *Phys. Rev. Lett.* **58**, 246 (1987).

$^{33}$K. S. Schweizer and J. G. Curro, in *Advances in Chemical Physics*, edited by I. Prigogine and S. A. Rice (John Wiley & Sons, Inc., 1997), Vol. 1.

$^{34}$D. Chandler, in *Studies in Statistical Mechanics VIII*, edited by E. W. Montroll and J. L. Lebowitz (North Holland, Amsterdam, 1982).

$^{35}$T. B. Martin, T. E. Gartner, R. L. Jones, C. R. Snyder, and A. Jayaraman, *Macromolecules* **51**, 2906 (2018).

$^{36}$K. S. Schweizer and J. G. Curro, *J. Chem. Phys.* **89**, 3350 (1988).

$^{37}$R. Dickman and C. K. Hall, *J. Chem. Phys.* **85**, 4108 (1986).

$^{38}$K. G. Honnell and C. K. Hall, *J. Chem. Phys.* **90**, 1841 (1989).

$^{39}$A. Yethiraj, J. G. Curro, K. S. Schweizer, and J. D. McCoy, *J. Chem. Phys.* **98**, 1635 (1993).

$^{40}$J. G. Curro, A. Yethiraj, K. S. Schweizer, J. D. McCoy, and K. G. Honnell, *Macromolecules* **26**, 2655 (1993).

$^{41}$N. F. Carnahan and K. E. Starling, *J. Chem. Phys.* **51**, 635 (1969).

$^{42}$D. J. Tildesley and W. B. Streett, *Mol. Phys.* **41**, 341 (1980).

$^{43}$M. Pütz, J. G. Curro, and G. S. Grest, *J. Chem. Phys.* **114**, 2847 (2001).

$^{44}$K. Binder, *Ferroelectrics* **73**, 43 (1987).

---

J. Chem. Phys. **153**, 244903 (2020); doi: 10.1063/5.0035451
Published under license by AIP Publishing

153, 244903-11