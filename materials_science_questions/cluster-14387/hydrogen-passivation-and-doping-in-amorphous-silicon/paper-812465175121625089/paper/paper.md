# Bond-centred hydrogen and muonium in silicon; a Feynman path-integral simulation

This content has been downloaded from IOPscience. Please scroll down to see the full text.

1996 J. Phys.: Condens. Matter 8 8309

(http://iopscience.iop.org/0953-8984/8/43/023)

View the table of contents for this issue, or go to the journal homepage for more

Download details:

IP Address: 139.184.14.159
This content was downloaded on 20/08/2015 at 05:18

Please note that terms and conditions apply.

# Bond-centred hydrogen and muonium in silicon;
## a Feynman path-integral simulation

Carlos P Herrero and Rafael Ramírez

Instituto de Ciencia de Materiales, Consejo Superior de Investigaciones Científicas (CSIC),
Campus de Cantoblanco, 28049 Madrid, Spain

Received 14 May 1996, in final form 4 August 1996

**Abstract.** Isolated hydrogen and muonium in crystalline silicon have been studied by the path-integral Monte Carlo method, using a parametrized Si–H interaction derived from earlier *ab initio* calculations. Hydrogen and deuterium are found to be stable at the bond-centre (BC) site, but this position is metastable for muonium. Average values of the kinetic and potential energy of the defects are compared with those expected for the hydrogen-like impurities within a harmonic approximation. The backwards relaxation of the Si-atom nearest neighbours of the impurity is found to be dependent on the impurity mass (higher host-atom relaxation for higher impurity mass).

## 1. Introduction

Isolated hydrogen and muonium in crystalline semiconductors have been widely studied in the last decade, by both experimental and theoretical methods. The interactions involving hydrogen are diverse and can affect the macroscopic properties of semiconductors. As an example, it is well known that almost 100% of boron acceptors can be passivated in Si at room temperature, with the consequent increase in the resistivity of the material by several orders of magnitude. Different reviews on this subject have been published in past years [1–4].

It is now generally accepted that the lowest-energy site for isolated hydrogen-like impurities in crystalline silicon is the bond-centre (BC) site, midway between two adjacent Si atoms. Electron paramagnetic resonance experiments have shown the presence of hydrogen in the so-called AA9 defect [5, 6], with axial symmetry around the [111] crystal axis, as expected for a BC site. Several theoretical studies [7–10] have found that this position is the equilibrium site for hydrogen in silicon, with a backwards relaxation of the nearest Si atoms of about $0.4\ \mathring{\text{A}}$.

Muonium may be considered as a light pseudoisotope of hydrogen, since the mass of the muon $\mu^+$ is about 1/9 that of the proton. In fact, this property has been used to extrapolate various characteristics of muonium in semiconductors to the case of hydrogen, which is difficult to observe as an isolated impurity in these materials [11–13]. However, the difference in mass between a proton and muon can be enough to make the BC site (the lowest-energy position for hydrogen) a metastable site for muonium, as a consequence of the high zero-point energy of this impurity at a BC site (about three times larger than that of hydrogen). In this line, it has been shown that muonium can display a behaviour distinct from that of hydrogen in silicon due to such quantum effects [14].

0953-8984/96/438309+12$19.50 © 1996 IOP Publishing Ltd

Hydrogen diffusion in silicon has been studied by molecular dynamics simulations [15–17], which have given diffusion coefficients that compare well with experiment. However, in these methods the atomic nuclei are treated as classical particles and typical quantum effects like zero-point vibrations are not directly accessible. These effects can be important for light impurities like hydrogen, and even more so for muonium, especially at low temperatures.

In this paper, we study mass-dependent properties of hydrogen-like impurities (H, deuterium (D), and muonium (the so-called anomalous muonium or Mu* centre)) at the BC site of crystalline silicon by the Feynman path-integral Monte Carlo (PIMC) method. This procedure provides a powerful approach for studying finite-temperature properties of quantum systems [18–20]. In this work, we calculate the average kinetic and potential energy of a supercell Si₆₄I (I = impurity, H, D or Mu*), as well as the isotope effect on the host-atom relaxation. Finally, the density distribution for the impurities at the BC site is also analysed.

## 2. The method of calculation

The path-integral approach in statistical physics is based on the formal equivalence between the canonical density matrix and the time evolution operator for a quantum system [18]. In particular, if our system of $P+1$ quantum particles ($P$ silicon nuclei and one impurity) is described by the hamiltonian $H$, the partition function $Z$ at temperature $T$ is given by
$$
Z = \operatorname{Tr}[\exp(-\beta H)] \tag{1}
$$
where $\beta=1/(k_B T)$ and $k_B$ is Boltzmann's constant. $Z$ can be expressed as a path integral in the following way [18]:
$$
Z = \int \exp\left[ -\frac{1}{\hbar} \int_0^{\beta \hbar} \Phi[\boldsymbol{R}(u)] \mathrm{d}u \right] \mathcal{D}\boldsymbol{R}(u) \tag{2}
$$
where $u$ is a parameter with dimensions of time, and $\boldsymbol{R}$ is a vector in a $3(P+1)$-dimensional space, the components of which are the Cartesian coordinates of the nuclei, $\boldsymbol{R}=(\boldsymbol{r}_1, \dots, \boldsymbol{r}_{P+1})$. The paths $\boldsymbol{R}(u)$ satisfy the cyclic condition $\boldsymbol{R}(0)=\boldsymbol{R}(\beta \hbar)$, and the functional $\Phi[\boldsymbol{R}(u)]$ is given by
$$
\Phi[\boldsymbol{R}(u)] = \frac{1}{2} \sum_{p=1}^{P+1} m_p \dot{\boldsymbol{r}}_p^2(u) + V[\boldsymbol{R}(u)] \tag{3}
$$
where $m_p$ is the mass of nucleus $p$, and $\dot{\boldsymbol{r}}_p$ the derivative of $\boldsymbol{r}_p$ with respect to the 'time' coordinate $u$. Since our calculations are performed within the Born–Oppenheimer approximation, we employ a potential energy surface $V(\boldsymbol{R})$ for the nuclei coordinates, as described below.

The path integral in equation (2) can be evaluated by a discretization of the cyclic paths $\boldsymbol{R}(u)$ into $N$ points $(\boldsymbol{R}_1, \boldsymbol{R}_2, \dots, \boldsymbol{R}_N)$. For sufficiently large $N$, $Z$ can be approximated within the high-temperature approximation by a free-particle propagator, leading to the expression
$$
Z_N = C \int \mathrm{d}\boldsymbol{R}_1 \dots \mathrm{d}\boldsymbol{R}_N \exp(-\beta V_{\text{eff}}) \tag{4}
$$
where the integral is extended to the whole coordinate space of $3(P+1)$ dimensions, and the constant $C$ is given by
$$
C = \left( \frac{m_{\text{I}}}{m_{\text{Si}}} \right)^{3N/2} \left( \frac{N m_{\text{Si}}}{2\pi \beta \hbar^2} \right)^{3(P+1)N/2}. \tag{5}
$$

$Z_N$ is formally identical to the partition function for a classical system of $P+1$ cyclic 'chains', interacting via an effective potential

$$
V_{\mathrm{eff}}(\boldsymbol{R}_{1}, \ldots, \boldsymbol{R}_{N}) = \sum_{j=1}^{N} \left[ A(\boldsymbol{R}_{j}, \boldsymbol{R}_{j+1}) + \frac{1}{N} V(\boldsymbol{R}_{j}) \right] \tag{6}
$$

where

$$
A(\boldsymbol{R}_{j}, \boldsymbol{R}_{j+1}) = \frac{N}{2\beta^2\hbar^2} \left[ m_{\mathrm{I}}(\boldsymbol{r}_{P+1,j+1} - \boldsymbol{r}_{P+1,j})^2 + \sum_{p=1}^{P} m_{\mathrm{Si}}(\boldsymbol{r}_{p,j+1} - \boldsymbol{r}_{pj})^2 \right]. \tag{7}
$$

The index $p$ refers to the particle, and goes from 1 to $P$ for the silicon atoms, and values $P+1$ for the impurity. The index $j$ indicates the 'time' coordinate along the path; $m_{\mathrm{Si}}$ and $m_{\mathrm{I}}$ are the mass of the host atoms and the impurity, respectively, and $V$ represents the potential energy part of the Hamiltonian. In equation (6) one has $\boldsymbol{R}_{N+1} = \boldsymbol{R}_{1}$, as a consequence of the cyclic character of the paths in equation (2). Thus, in this discretization of the path integral, the quantum paths of a nucleus are described by cyclic chains divided into $N$ 'time-slices', and within a given path, the nucleus $p$ at time-slice $j$ is harmonically coupled to its $j+1$ and $j-1$ images with spring constant $N m_p/(\beta\hbar)^2$ (see equation (7)). On the other hand, the interaction potential $V(\boldsymbol{R}_{j})$ in equation (6) is 'instantaneous', in the sense that it is restricted to particle images sharing the same 'time' coordinate $j$. This approximation for the partition function $Z$ becomes exact in the limit of large $N$:

$$
Z = \lim_{N \to \infty} Z_N. \tag{8}
$$

It will be interesting in the discussion below to compare the behaviour of the quantum impurities studied with that of a 'classical' impurity suffering the same interaction potential, and following classical statistical mechanics. This classical limit with the potential $V(\boldsymbol{R})$ is obtained by putting $N=1$ in the partition function of equation (4). In this case, $A(\boldsymbol{R}_{j}, \boldsymbol{R}_{j+1})=0$, and each quantum path collapses into a single point in the configuration space.

In this context, the average kinetic energy of particle $p$ at temperature $T$ is given by [20]

$$
\langle K_p \rangle = \frac{3}{2} N k_B T - \frac{N m_p}{2\beta^2\hbar^2} \sum_{j=1}^{N} \langle (\boldsymbol{r}_{p,j+1} - \boldsymbol{r}_{pj})^2 \rangle. \tag{9}
$$

The single-particle density $n_p(\boldsymbol{r})$, defined as the probability density for finding the nucleus $p$ at position $\boldsymbol{r}$ is obtained as $N^{-1}$ times the probability density for finding any of the $N$ images of nucleus $p$ at $\boldsymbol{r}$ [20]. More details on the PIMC method can be found elsewhere [18, 20, 21].

The Si–Si interaction has been modelled by the Stillinger–Weber potential [22], that gives results for crystalline silicon (total energy, quantum delocalization of the Si atoms) in good agreement with those derived from experiment [23–25]. The Si–H interaction has been described by a three-body potential developed to reproduce the energy surface obtained by Van de Walle *et al* [7] for $\mathrm{H}^+$, which is thought to be the stable state of H in undoped and p-type silicon [7, 26, 27]. The actual form of our parametrized potential is given elsewhere [28].

The partition function $Z_N$ in equation (4) has been sampled by the Metropolis method [29, 30]. We employ a $2 \times 2 \times 2$ supercell of the Si face-centred cubic cell with periodic boundary conditions. It contains 64 Si atoms and one impurity, and the simulation cell parameter amounts to 10.86 Å. A simulation run proceeds via successive MC steps (MCS).

In each MCS, the path coordinates of the nuclei are updated according to two different kinds of sampling scheme. In the first one, attempts to move are carried out sequentially for each nucleus at every time-slice. The second one is a random move of the centre of gravity (CG) of the cyclic path associated with each particle, leaving unaltered the shape of each individual path (translation of the path). At each temperature studied, the maximum distance allowed for random moves was fixed to obtain an acceptance ratio of about 50% for each kind of sampling. At 50 K, the maximum allowed impurity displacements in a MCS amount to 0.10 Å, 0.14 Å, and 0.24 Å for moves of individual path coordinates of deuterium, hydrogen and muonium, respectively. For moves of the CG, we obtain nearly the same value for the three impurities (~0.06 Å at 50 K). At each temperature, we generated $2 \times 10^5$ paths per atom for the calculation of ensemble average properties, and $6 \times 10^4$ paths per atom for system equilibration. To keep the numerical error caused by the discretization of the integrals lower than 1 meV per atom, we have taken for the product $NT$ the values 2000 K for Si, 10 000 K for H and D, and 30 000 K for muonium. Thus, at $T = 50$ K, the cyclic paths include 40 time-slices for Si, 200 for H and D, and 600 for muonium. The number of time-slices $N$ employed in the MC simulations decreases as $1/T$ as temperature increases, to keep the same precision in the energy $\langle E \rangle$. Since in equation (4) the same number $N$ appears for Si and impurity nuclei, in the actual MC simulations every consecutive $n$ $(=N_\text{I}/N_\text{Si})$ time-slices for the impurity correspond to $n$ time-slices of Si, that collapse into a single one.

## 3. Results of the simulations

With our parametrized Si–H potential, the BC site is the absolute energy minimum with a backwards relaxation of the nearest-neighbour Si atoms of 0.3 Å. In this minimum-energy configuration, we find a potential energy of –1.39 eV with respect to the pure host supercell. This energy can be separated into Si–Si and Si–H interactions, and we obtain a Si–H energy $V(\text{Si--H}) = -2.83$ eV, along with a relaxation energy of the lattice $\Delta V(\text{Si--Si}) = 1.44$ eV. The energy surface for hydrogen in silicon so obtained reproduces closely the main features of that found by Van de Walle and co-workers from pseudopotential density functional calculations [7]. By keeping the Si atoms fixed at their fully relaxed positions (for the impurity at BC), we find at the energy minimum a force constant $k_\parallel = 18.42$ eV Å$^{-2}$ for impurity motion along the axis, and $k_\perp = 3.50$ eV Å$^{-2}$ for vibrations perpendicular to the [111] direction. These values translate for hydrogen into $\omega_\parallel = 2230$ cm$^{-1}$ and $\omega_\perp = 972$ cm$^{-1}$. For the potential employed here, we do not find any difference between displacements along different directions perpendicular to [111], e.g., $[1\bar{1}0]$ and $[11\bar{2}]$. The energy curve along the bond is highly anharmonic, as a consequence of the constraints suffered by the impurity at the BC site [28].

We define the average defect energy $\langle E_\text{I} \rangle$ at a given temperature $T$ as the difference between the total energy of the supercell, $\langle E(\text{Si}_{64}\text{I}) \rangle$ (I = H, D or muonium), and that of the silicon supercell without the impurity at the same temperature, $\langle E(\text{Si}_{64}) \rangle$. In the following, we will take as zero defect energy the classical limit at $T = 0$, i.e.

$$
\langle E_\text{I} \rangle = \langle E(\text{Si}_{64}\text{I}) \rangle - \langle E(\text{Si}_{64}) \rangle - E_\text{I}^\text{Cl}(T=0)
\tag{10}
$$

where $E_\text{I}^\text{Cl}(T=0) = E_\text{I}^\text{Cl}(\text{Si}_{64}\text{I}) - E_\text{I}^\text{Cl}(\text{Si}_{64}) = -1.39$ eV is obtained when one considers the atomic nuclei (both of the impurity and silicon) as classical particles at $T = 0$. In figure 1 we present the defect energy versus the temperature from 0 to 400 K. Open symbols indicate results of our PIMC simulations for deuterium (circles), hydrogen (squares), and muonium (triangles). For the latter impurity, we show only results up to 100 K, since muonium is not

![](./images/812465175121625089_1.jpg)

Figure 1. The temperature dependence of the defect energy for bond-centred impurities, as obtained from path-integral Monte Carlo simulations for deuterium (open circles), hydrogen (squares) and anomalous muonium (triangles). The dotted lines correspond to three-dimensional harmonic oscillators with force constants $k_{\parallel}=18.42$ eV $\text{\AA}^{-2}$ and $k_{\perp}=3.50$ eV $\text{\AA}^{-2}$. The dashed line represents the average thermal energy of a 3D classical harmonic oscillator: $\langle E\rangle=3k_{B}T$.

confined by our potential at the BC site for higher temperatures [14]. As expected, zero-point effects due to the finite mass of the impurities cause an increase in the defect energy, which is higher for lower impurity mass. Up to 400 K, hydrogen and deuterium are found to be located around the BC site, which is the equilibrium position for a classical particle. The dotted lines in figure 1 were obtained in a one-particle harmonic approximation (HA) with masses corresponding to the different impurities. In this approximation, one has

$$
E_{\mathrm{I}}^{\mathrm{HA}}=\frac{1}{2}\hbar\sum_{i=1}^{3}\omega_{i}\coth\left(\frac{\hbar\omega_{i}}{2k_{B}T}\right)
\tag{11}
$$

where the $\omega_{i}$ correspond to the vibrational frequencies ($\omega_{\parallel}$ and $\omega_{\perp}$) obtained for each impurity at the BC site. In this approximation at $T=0$, the defect energies corresponding to deuterium, hydrogen, and muonium scale roughly as $1:\sqrt{2}:3\sqrt{2}$. The dashed line in figure 1 corresponds to the average energy of a classical three-dimensional (3D) harmonic oscillator, which increases linearly with temperature, and does not depend on the oscillator mass: $\langle E\rangle=3k_{B}T$. For hydrogen and deuterium we find a tendency of the defect energy (squares and circles) to be slightly higher than that corresponding to the HA (dotted lines). For muonium, however, this tendency is much clearer, since this impurity is lighter (more delocalized) and feels stronger the anharmonicity of the interaction potential. In fact, we obtain in this case from the PIMC simulations a defect energy about 85 meV higher than that found in the HA. This increase is mainly due to the change in the kinetic energy of the impurity, which increases as a consequence of the constraints suffered by the particle in the [111] axis (bond direction). This is clearly seen in figure 2, where we plot the kinetic energy of the impurity at 50 K versus $1/\sqrt{m_{\mathrm{I}}}$. Open squares represent the kinetic energy obtained from the MC simulations, which are compared with the results found for the one-particle

HA with the frequencies $\omega_i$ ($i=1,2,3$) derived from the force constants $k_\parallel$ and $k_\perp$ given above (continuous line). The classical limit corresponds to infinite impurity mass, and gives $\langle K_{\text{I}} \rangle = 6.5$ meV.

![](./images/812465175121625089_2.jpg)

Figure 2. The kinetic energy of hydrogen-like impurities at 50 K, as a function of the inverse square root of the impurity mass. Open squares represent data obtained from PIMC simulations. The full line corresponds to a one-particle harmonic approximation with the force constants $k_\parallel$ and $k_\perp$ given in the text. The dashed line is a guide to the eye.

An important consequence of the impurity delocalization is that the average interaction energy between the host atoms and the impurity will change as a function of the impurity mass. One expects that muonium will be more delocalized than hydrogen and deuterium, and thus it will explore points of the configuration space with energy $V(\text{Si-I})$ higher (impurity less bound) than that corresponding to a classical particle at the BC site. This is in fact obtained from our PIMC simulations, as shown in figure 3. We find a linear dependence of this binding energy versus $1/\sqrt{m_{\text{I}}}$. For H, the potential energy of the Si-I-Si three-centre bond is about 0.2 eV higher than for a classical particle, and about 0.4 eV lower than for the Mu* centre.

Taking into account that the presence of the impurity at the BC site is associated with a strong backwards relaxation of the nearest Si atoms, one expects that the more confined the impurity around the bond-centre site, the higher will be the lattice relaxation energy. This means that for increasing impurity delocalization (lower mass), the lattice relaxation energy will decrease. This is shown in figure 4, where we plot the energy $\Delta V(\text{Si-Si})$ obtained from our Monte Carlo simulations, versus $m_{\text{I}}^{-1/2}$. We find again a linear correlation between these variables. Changes of $\Delta V(\text{Si-Si})$ as a function of the impurity mass are not negligible. For hydrogen, we find that this energy is 55 meV lower than that corresponding to a classical particle, and 108 meV higher than for anomalous muonium. Note that due to the quantum delocalization of $\mu^+$ around the BC site, the lattice relaxation energy decreases from 1.42 eV (classical particle at 50 K) to 1.26 eV, i.e., this energy changes by about 11%. The change in lattice relaxation around the impurity can be also quantified by the distance $d(\text{Si-Si})$ between average positions of the nearest host atoms. In figure 5, we display this distance

![](./images/812465175121625089_3.jpg)

Figure 3. The interaction energy $V$(Si-I) versus $m_{\mathrm{I}}^{-1/2}$. Open squares are data points derived from PIMC simulations at 50 K.

![](./images/812465175121625089_4.jpg)

Figure 4. The lattice relaxation energy versus $m_{\mathrm{I}}^{-1/2}$ at $T=50$ K. Open squares indicate the results of the PIMC simulations.

![](./images/812465175121625089_5.jpg)

Figure 5. The average distance between Si-atom nearest neighbours of the impurity, as a function of the inverse square root of the impurity mass, as obtained from the PIMC simulations. The dashed line is a least-squares fit to the data points.

at $T=50$ K as a function of the inverse square root of the mass impurity. As a result, the distance $d$(Si-Si) decreases by about 0.05 Å when going from a classical particle (limit of infinite mass) to bond-centred muonium.

It is interesting to compare the delocalization of the different hydrogen-like impurities at low temperatures (almost ground state). Since our Si-H potential displays axial symmetry around the [111] crystal axis, the probability density function for the impurity will show the same cylindrical symmetry around the Si-Si axis. In figure 6 we plot the integrated

![](./images/812465175121625089_6.jpg)

Figure 6. The probability density for the distance of the impurity to the Si-Si axis at 50 K. The continuous line is for Mu*, the dashed line for H, and the dotted line for D.

![](./images/812465175121625089_7.jpg)

Figure 7. The probability density for the Si-I-Si angle (I = impurity) at 50 K. The continuous line is for Mu*, the dashed line for H, and the dotted line for D.

impurity density versus the distance $\rho$ to the Si-Si axis at $T = 50$ K. The maximum of these distribution functions moves towards higher distances as the impurity mass decreases. We find these maxima at $\rho_m = 0.120$, $0.145$ and $0.314$ Å, for H, D and muonium, respectively. These values are in a ratio 1:1.21:2.62, to be compared with the ratio expected for a harmonic approximation, i.e., 1:1.19:1.73 ($\rho_m$ proportional to $m_{\mathrm{I}}^{-1/4}$, since for a harmonic oscillator the ground-state delocalization $(\Delta r)^2$ scales as $1/\sqrt{m_{\mathrm{I}}}$). Hydrogen and deuterium follow closely the harmonic ratio, but the ratio between muonium and hydrogen (or deuterium) departs considerably from the value expected for the HA. This result agrees with the observation made above that muonium feels the anharmonicity of the interatomic potential more strongly than hydrogen and deuterium. Note that the most probable site for the impurities is the bond centre, exactly between the nearest Si atoms, which corresponds to $\rho = 0$ in figure 6. The curves shown is this figure show off-BC maxima because they correspond to an integration of the volume density weighted by $2\pi\rho$, as obtained from the PIMC simulations.

A complementary picture of the actual defect configuration can be obtained by looking at the distribution of the instantaneous Si-I-Si angle for the different impurities. This angle distribution is shown in figure 7 at a temperature of 50 K, for which the most probable angles are $171^\circ$, $169^\circ$ and $155^\circ$ for D, H and muonium, respectively. It is interesting to see the influence of the potential anharmonicity and the coupling between host-atom and impurity vibrations on the density distribution for the impurity, in particular for the case of Mu*, where the differences with respect to the one-particle HA will be greater. Thus, in figure 8 we present the Si-I-Si angle distribution corresponding to the Mu* centre in the HA (dashed line), with the Si atoms fixed at their relaxed positions for the absolute energy minimum $(d(\mathrm{Si-Si}) = 2.948$ Å). This distribution is plotted as a dashed line, and is to be compared with that obtained in the PIMC simulations for this centre (continuous line). It is clear that the one-particle HA predicts a density distribution narrower than that found in the MC simulations. At this point, one can argue that the actual Mu* centre could be better described by a kind of quasiharmonic approximation (QHA), in which the Si-Si distance

![](./images/812465175121625089_8.jpg)

Figure 8. The probability density for the Si–I–Si angle (I = impurity) for anomalous muonium at $T=50$ K. Continuous line: PIMC simulation: dashed line: one-particle harmonic approximation with $k_\parallel$ and $k_\perp$ given in the text; dotted line: quasiharmonic approximation for a distance $d(\text{Si--Si})=2.899$ Å.

should be that obtained in the PIMC simulation of this centre (namely, $d(\text{Si--Si})=2.899$ Å at 50 K), with the frequencies $\omega_\parallel$ and $\omega_\perp$ calculated for this host-atom configuration. In fact, such a QHA gives a Si–I–Si angle distribution (the dotted line in figure 8) closer to the MC results, but is still far from giving a good agreement with the path-integral simulations.

## 4. Discussion

An important consequence of the anharmonicity of the interatomic potential is the dependence on the impurity mass of several quantities that are constant in a harmonic approximation. That is, in a HA the average positions of the atomic nuclei (host and guest) remain constant, irrespective of the temperature and impurity mass. From the results of our PIMC simulations, one can quantify the influence of the anharmonicities upon the average atom positions. Thus, in a HA one expects that the distance $d(\text{Si--Si})$ between host-atom nearest neighbours of the impurity will be independent of the impurity mass. The results shown in figure 5 indicate that this distance decreases appreciably when one goes from deuterium to muonium. If one compares the values of this distance corresponding to the different hydrogen-like impurities with that obtained for the minimum-energy configuration (classical particle at $T=0$, $d=2.948$ Å), one finds changes of $-0.015$, $-0.019$, and $-0.049$ Å, for D, H and muonium, respectively. For comparison, we note that for a 'classical' hydrogen-like particle, we obtain at 50 K a change of $-4 \times 10^{-3}$ Å, indicating that it feels the potential anharmonicity much less than the actual quantum impurities. Taking into account that the backwards relaxation of the nearest silicon atoms obtained here for the minimum-energy configuration is $\Delta d=0.298$ Å per Si atom, we find a reduction of the nearest-neighbour relaxation of about 8% for the case of $\text{Mu}^*$. The change in the relaxation of nearest neighbours is especially important for muonium, and indicates that the large delocalization of this light impurity, with the concomitant feeling of the potential

surface anharmonicity, cannot be neglected if one is to give a precise characterization of these point defects. It is worth comparing these distances with the spatial delocalization of Si nuclei in their ground state, with values $(\Delta r)^2 \sim 7 \times 10^{-3}$ $\mathring{\text{A}}^2$, as derived from the vibrational density of states obtained from neutron diffraction experiments [23, 25]. This translates into $\Delta x \sim 0.05$ $\mathring{\text{A}}$, and thus changes in the average position of the nearest silicon atoms, due to the anharmonicity of the Si–I interaction potential, are of the order of their zero-point delocalization.

As shown in figure 1, the defect energy for anomalous muonium Mu* departs appreciably from that expected for a pure HA. The increase in the total defect energy with respect to the one-particle HA is found to be 85 meV, from which 51 meV are associated with an increase in the kinetic energy of the impurity (see figure 2). The remaining difference comes from the change of the potential energy of the defect, which results from the competition between an increase in $V(\text{Si–I})$ (see figure 3) and a decrease in the lattice relaxation energy (figure 4). As a result, the potential energy is 34 meV higher than that corresponding to the one-particle HA.

![](./images/812465175121625089_9.jpg)

Figure 9. The mean distance from the impurity to the Si–Si axis, as a function of the distance between nearest Si atoms. Open squares: PIMC simulations at 50 K; dotted line, the quasiharmonic approximation, as described in the text. An arrow indicates the Si–Si distance corresponding to the absolute energy minimum with the impurity at the BC site.

At this point, it is interesting to compare the correlation between $d(\text{Si–Si})$ and the average distance from the impurity to the bond axis. This is shown in figure 9, where one sees that the mean distance $\langle\rho\rangle$ to the axis goes up as the Si–Si distance decreases (impurity mass, $m_{\text{I}}$, decreases). The open squares are results of our PIMC simulations for the different hydrogen-like impurities studied here. In order to compare these results with those corresponding to a QHA, we proceed as follows. The mean distance $\langle\rho\rangle$ is given by

$$
\langle\rho\rangle^{2}=\frac{\pi \hbar}{4 m \omega_{\perp}} \operatorname{coth}\left(\frac{\hbar \omega_{\perp}}{2 k_{B} T}\right) \tag{12}
$$

with $\omega_{\perp}=(k_{\perp}/m_{\text{I}})^{1/2}$, and $k_{\perp}$ is obtained as a function of the Si–Si distance via the equation $k_{\perp}=13.84\ d(\text{Si–Si})-37.30$ ($k_{\perp}$ in eV $\mathring{\text{A}}^{-2}$, $d(\text{Si–Si})$ in $\mathring{\text{A}}$, as found in a linear

fit to the force-constant change as a function of $d$(Si-Si), for our parametrized potential). Finally, the relationship between $m_{\mathrm{I}}$ and $d$(Si-Si) is given by the dashed line in figure 5. As a result, we obtain for this QHA the continuous line shown in figure 9. As expected from the comments above, the PIMC simulations give for the quantum impurities values of $\langle\rho\rangle$ larger than the QHA values, in particular for $\mathrm{Mu}^{*}$.

For muonium, at temperatures higher than 100 K, our potential does not confine the impurity around a BC site. Instead, we find a different configuration for the defect, which is comparable to that of normal muonium (the so-called Mu centre) [11, 12]. In this case, muonium is highly delocalized around the interstitial tetrahedral T site, and this delocalization makes the kinetic energy of the impurity at 50 K decrease from 0.44 eV for $\mathrm{Mu}^{*}$ to 0.11 eV for $\mathrm{Mu}$ [14].

Note that our analysis is restricted to impurities confined around the BC site. At temperatures higher than 400 K, impurity diffusion will be important, and the hydrogen-like species will have a non-negligible probability of occupying other interstitial sites, as shown in previous molecular dynamics simulations [15, 16, 17]. Also, at low temperatures, it is possible that hydrogen hops from BC site to BC site due to thermally assisted tunnelling, as shown by Cheng and Stavola for the boron-hydrogen complex in silicon [31]. Although PIMC simulations such as those employed here do not allow us to analyse directly the possibility of impurity tunnelling between adjacent BC sites, Monte Carlo simulations based on the quantum transition-state theory [19, 32, 33] are a promising technique to obtain insight into this interesting point in the near future.

## 5. Conclusions

Path-integral Monte Carlo simulations give valuable information on point defects in semiconductors. In particular, for light impurities, one can study the effect of anharmon- icities in the interaction potential on the kinetic and potential energy of the defect. These effects are especially important for muonium, for which the defect energy changes by more than 10% with respect to a one-particle harmonic approximation. The energy of lattice relaxation also changes appreciably with the impurity mass, and is more than 0.1 eV higher for bond-centred H than for the $\mathrm{Mu}^{*}$ centre.

## Acknowledgments

We thank E Artacho for helpful discussions and J C Noya for critical comments on the manuscript. This work was supported by CICYT (Spain) under contract PB93-1254.

## References

[1] Pankove J I and Johnson N M (ed) 1991 *Hydrogen in Semiconductors* (New York: Academic)
[2] Pearton S J, Corbett J W and Stavola M 1992 *Hydrogen in Crystalline Semiconductors* (Berlin: Springer)
[3] Pearton S J 1994 *Int. J. Mod. Phys.* **B 8** 1093
[4] Estreicher S K 1995 *Mater. Sci. Eng. Rep.* **14** 1
[5] Gorelkinskii Yu V and Nevinnyi N N 1987 *Pis. Zh. Tekh. Fiz.* **13** 105 (Engl. Transl. 1987 *Sov. Tech. Phys. Lett.* **13** 45)
[6] Gorelkinskii Yu V and Nevinnyi N N 1991 *Physica* **B 170** 155
[7] Van de Walle C G, Denteneer P J H, Bar-Yam Y and Pantelides S T 1989 *Phys. Rev.* **B 39** 10791
Van de Walle C G, Bar-Yam Y and Pantelides S T 1988 *Phys. Rev. Lett.* **60** 2761
[8] Estreicher S K 1987 *Phys. Rev.* **B 36** 9122
[9] Vogel S, Celio M, Maric D M and Meier P F 1989 *J. Phys.: Condens. Matter* **1** 4729

[10] Bonapasta A A, Lapiccirella A, Tomassini N and Capizzi M 1988 *Europhys. Lett.* **7** 145

[11] Patterson B D 1988 *Rev. Mod. Phys.* **60** 69

[12] Kiefl R F and Estle T L 1991 *Hydrogen in Semiconductors* ed J I Pankove and N M Johnson (New York: Academic) ch 15

[13] Kreitzman S R, Hitti B, Lichti R L, Estle T L and Chow K H 1995 *Phys. Rev. B* **51** 13 117

[14] Ramírez R and Herrero C P 1994 *Phys. Rev. Lett.* **73** 126

[15] Buda F, Chiarotti G L, Car R and Parrinello M 1989 *Phys. Rev. Lett.* **63** 294; 1991 *Physica B* **170** 98

[16] Boucher D E and DeLeo G G 1994 *Phys. Rev. B* **50** 5247

[17] Panzarini G and Colombo L 1994 *Phys. Rev. Lett.* **73** 1636

[18] Feynman R P 1972 *Statistical Mechanics* (New York: Addison-Wesley)

[19] Gillan M J 1987 *Phys. Rev. Lett.* **58** 563; 1988 *Phil. Mag. A* **58** 257

[20] Gillan M J 1990 *Computer Modelling of Fluids, Polymers and Solids* ed C R A Catlow, S C Parker and M P Allen (Dordrecht: Kluwer)

[21] Ceperley D M 1995 *Rev. Mod. Phys.* **62** 279

[22] Stillinger F H and Weber T A 1985 *Phys. Rev. B* **31** 5262

[23] Dolling G and Cowley R A 1966 *Proc. R. Soc.* **88** 463

[24] Kluge M D and Ray J R 1988 *Phys. Rev. B* **37** 4132

[25] Ramírez R and Herrero C P 1993 *Phys. Rev. B* **48** 14 659

[26] Deák P, Snyder L C and Corbett J W 1991 *Phys. Rev. B* **43** 4545

[27] Chang K J and Chadi D J 1989 *Phys. Rev. B* **40** 11 644

[28] Herrero C P and Ramírez R 1995 *Phys. Rev. B* **51** 16 761

[29] Metropolis N, Rosenbluth A W, Rosenbluth M N, Teller A H and Teller E 1953 *J. Chem. Phys.* **21** 20

[30] Binder K and Heermann D W 1988 *Monte Carlo Simulation in Statistical Physics* (Berlin: Springer)

[31] Cheng Y M and Stavola M 1994 *Phys. Rev. Lett.* **73** 3419

[32] Voth G A, Chandler D and Miller W H 1989 *J. Chem. Phys.* **91** 7749

[33] Cao J and Voth G A 1994 *J. Chem. Phys.* **100** 5106