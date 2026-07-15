# Dielectric Response of $\text{Ta}_2\text{O}_5$, $\text{NbTaO}_5$ and $\text{Nb}_2\text{O}_5$ from First-Principles Investigations

S. Clima$^{\text{a}}$, G. Pourtois$^{\text{a}}$, S. Van Elshocht$^{\text{a}}$, S. De Gendt$^{\text{a,b}}$, M. Heyns$^{\text{a,c}}$, D.J. Wouters$^{\text{a}}$ and J.A. Kittl$^{\text{a}}$

$^{\text{a}}$ IMEC vzw , Kapeldreef 75, B-3001 Leuven, Belgium
$^{\text{b}}$ Department of Chemistry, Katholieke Universiteit Leuven, Celestijnenlaan 200F, B-3001 Leuven, Belgium
$^{\text{c}}$ Department of Metallurgy and Materials Engineering, Katholieke Universiteit Leuven, B-3001 Leuven, Belgium

High-$\kappa$ dielectrics are intensively investigated as a replacement for $\text{SiO}_2$ in integrated nanoelectronics. Ta and Nb based oxides are among the list of interesting candidates that display a relatively large dielectric constant with a band gap larger than 3 eV. In this paper, we show that it is possible to modulate the dielectric response of the $\text{Ta}_2\text{O}_5$ by admixing it with $\text{Nb}_2\text{O}_5$. The dynamical charges and dielectric constants of $\text{Ta}_2\text{O}_5$ and of $\text{Nb}_2\text{O}_5$ were calculated at the Density Functional Theory (DFT) level for different crystal phases. The averaged dielectric constants range between 27(38) and 42(77) for $\text{Ta}_2\text{O}_5$ ($\text{Nb}_2\text{O}_5$) in the hexagonal and orthorhombic varieties. Interestingly, a mixed $\text{NbTaO}_5$ composition exhibits a directionally averaged dielectric constant of 54 and a relatively large band gap, close to the arithmetic mean value of the binary species. The origins of the dielectric permeability are discussed and confronted to experimental measurements.

## Introduction

The aggressive scaling drives for faster, more power-efficient, lower-cost integrated circuits (IC), which requires the introduction of a new generation of high-$\kappa$ materials in integrated capacitors or gate insulator [1]. The need for a tight composition control at an industrial scale limits the chemical complexity of the materials that can be considered [2]. From that point of view, simple binary oxides, such as $\text{HfO}_2$, $\text{ZrO}_2$, $\text{Al}_2\text{O}_3$ and $\text{Ta}_2\text{O}_5$ have emerged as being the most promising candidates in terms of integration. Among them, $\text{Ta}_2\text{O}_5$ and $\text{Nb}_2\text{O}_5$ with their relatively high dielectric constant and moderate band gaps, are interesting oxides for IC capacitor; tantalum oxide being already integrated in some DRAM applications [3-5]. The challenge for $\text{Ta}_2\text{O}_5$ is to grow high performance dielectric films at low thermal budgets, while the highest dielectric permittivities are obtained for highly ordered crystalline defect-free $\text{Ta}_2\text{O}_5$ films, that typically requires high temperature treatments [5, 6]. The chemical and structural similarities of Nb- and Ta-based oxides favor the idea of mixing them together to enhance either the dielectric permittivity of tantalum pentoxide host or the band-gap of niobium pentoxide [6]. In the present work, we investigate the dielectric response of these oxides. It is generally accepted that low permittivities (about 19-26 (30) for Ta (Nb) oxides) are obtained for a poorly ordered and oxygen vacancies-rich orthorhombic phase [6]. On the contrary, the

hexagonal conformation of tantalum pentoxide is believed to be the high permittivity phase (values of up to 90-110 have been reported [5]). The latter can be deposited at temperatures similar to the orthorhombic polymorph, although in this case a lattice compatible substrate is required [5, 7]. To the best of our knowledge, no detailed study of the factors driving the dielectric constants of these oxides has been made before. We used a first-principles approach to calculate the dielectric permittivities for the orthorhombic and two hexagonal crystal structures of Nb and Ta oxides. The main drawback of using $Nb_2O_5$ as an insulator material is its relatively small band gap with respect to $Ta_2O_5$, which consequently leads to high leakage currents. Still, a solid solution of $Ta_2O_5$ and $Nb_2O_5$ might offer a good compromise between the conservation of a band gap large enough for a proper device operation and an enhanced dielectric permittivity, as in the case of $HfSiO_x$ [8] with respect to $HfO_2$. We therefore also investigated the dielectric response and the electronic properties of a $NbTaO_5$ homogeneous solid solution.

## Computational Details

The total energy and the band structure calculations were performed using Density Functional Theory with the Quantum-ESPRESSO package [9] and Local Density Approximation (LDA) combined with Vanderbilt ultrasoft pseudopotentials [10]. The $2s^2, 2p^4$ electrons of O, $4s^2,4p^6,4d^4,5s^1$ of Nb and $5s^2,5p^6,5d^3,6s^2$ electrons of Ta were treated as valence states. A kinetic-energy cut off of 40 Ry has been chosen for the plane wave expansion of the wavefunction, whereas the integration of the Brillouin zone was replaced by a sum on a Monkhorst-Pack grid of special k-points: 4x4x4, 4x4x8 and 9x9x4 for the orthorhombic, hexagonal A and B crystalline structures, respectively. The ionic position and cell volume optimizations were performed with the following convergence criteria: $10^{-4}$ Ry/bohr for the Hellman-Feynman forces and $10^{-5}$ Ry/bohr³ for the stress tensor. The dielectric permittivity tensors, phonon modes and Born effective charge tensors were evaluated using a linear response approach [11, 12]. Vacancy type defects were computed on large supercells, in which case a finite-difference approach was used to calculated the dielectric response. Small differences of 5-10% for the dielectric constant evaluated with the two approaches were observed. The electronic properties were computed at the LDA level, which suffers from a systematic underestimation of the band gap [13]. The provided values must therefore be regarded as qualitative.

## Results and Discussions

In what follows, we consider a set of representative crystal structures (Figure 1) that are consistent with the XRD experimental patterns found by Hardy et al. [14] (Figure 2): orthorhombic (β-$Ta_2O_5$ and T-$Nb_2O_5$ Figure 1a) and hexagonal phases (δ-$Ta_2O_5$ and isostructural TT-$Nb_2O_5$ Figure 1b and 1c) [15, 16]. The orthorhombic β-$Ta_2O_5$ that is reported to be the dominant phase below 1630K, displays different oxygen content/vacancies that fluctuate with the level of impurities, substrates and processing conditions [4,17,18]. The well-characterized β-$Ta_2O_5$ phase corresponds to a $Ta_{22}O_{55}$ stoichiometric crystal, whose unit cell size is unfortunately too large to be handled by modern first-principles calculations. Therefore, we followed the approach proposed by Ramprasad et al. [19] and considered a smaller crystal unit that neglects

the presence of oxygen vacancies. This ideal crystal model meets the requirements of an insulating phase and is expected to be representative of the orthorhombic structure [19]. Indeed, the simulated powder XRD pattern (Figure 2 d,e,f) of our simplified orthorhombic structure shows only minor differences compared to the experimental signature (Figures 2 a,b,c). The optimized cell parameters are: a=7.21(7.23) Å, b=6.13(6.13) Å and c= 3.72(3.70) Å for the $Ta_2O_5$ ($Nb_2O_5$) orthorhombic phase. The hexagonal form of the oxides has been modeled based on two possible candidate structures (denoted as $\delta_A$ and $\delta_B$, see Fig 1b and 1c). Fukumoto et al. [16] found that the hexagonal $\delta_A$ phase of $Ta_2O_5$ is more stable than the $\delta_B$ one. In contrast with their results, we found that the $\delta_A$ phase converges to a slightly unsymmetrical distribution of the atoms in the hexagonal unit cell (a= 7.48(7.49) Å, b=7.37(7.38) Å and c= 3.70(3.68) Å for $Ta_2O_5$ ($Nb_2O_5$)). This conformation is more stable than the $\delta_B$ phase (a= 3.35(3.36) Å and c= 8.80(8.89) Å for $Ta_2O_5$ ($Nb_2O_5$)) by 1.48 eV (1.41 eV) per $Ta_2O_5$ ($Nb_2O_5$) formula unit. Furthermore, we found that the $\delta_A$ phase is 1.22 eV/$Ta_2O_5$ (1.02 eV/$Nb_2O_5$) energetically less stable than the β orthorhombic one. The computed $\delta_A$ structure is somewhat distorted from the ideal symmetric hexagonal one for the Ta (Nb) atoms, as illustrated in Figure 1b. The high-symmetry model is found to be unstable within the local density approximation. This analysis confirms that the orthorhombic phase is the most stable one and is expected to be predominant for the Ta and Nb oxides in thermodynamic equilibrium conditions. Hexagonal phases are unlikely to be representative of the crystalline phase obtained upon the application of a low thermal budget (<700ºC) and in the absence of a suitable substrate.

![](./images/811853546449272833_1.jpg)

Figure 1. Crystal structure of the LDA optimized β orthorhombic (a), hexagonal $\delta_A$ (b) xy topview), and $\delta_B$ (c) phases of $M_1M_2O_5$, $M_{1,2}$=Ta, Nb. In the mixed $NbTaO_5$ orthorhombic oxide (a) the 1-4 and 5-8 sites were randomly occupied by either a Nb or a Ta site.

![](./images/811853546449272833_2.jpg)

Figure 2. XRD patterns of $(Nb_xTa_{1-x})_2O_5$ for (a,b,c, x=0,1,0.5) sol-gel films [14], powder diffraction simulated for (d,e,f, x=0,1,0.5) β, (g,h, x=0,1) $δ_A$ and (i,j,x=0,1) $δ_B$ phases.

Table I summarizes the computed dielectric permittivity of the orthorhombic and hexagonal phases (sum of the ionic and electronic contributions), together with the effective polarization charges (corresponding to the main diagonal of the tensor) and the computed band gaps. The directionally averaged dielectric permittivity of

$Ta_2O_5$ ($Nb_2O_5$) are 42 (77) for the $\beta$ phase, 34 (58) for the $\delta_A$ and 27 (38) for the hexagonal $\delta_B$ one. The experimental values of the dielectric constants of the two materials vary significantly (19-90 [5, 6] for Ta and 30-90 [15, 20] for Nb) depending on the deposition techniques used, the crystalline phase obtained and its purity. We found that the computed dielectric constants fall within the reported experimental values and are consistent with the higher dielectric polarizability reported for Nb based oxides.

TABLE I. Calculated dielectric permittivity (main tensor components), average effective charges (main diagonal of the transition metal tensor, for oxygen are shown in brackets) and band gaps, computed for $Ta_2O_5$, $Nb_2O_5$ and $TaNbO_5$ in the hexagonal (A and B) and orthorhombic phases. * indicates some small deviations of the actual values with respect to the arithmetic averages.

<table>
  <thead>
    <tr>
      <th rowspan="2"></th>
      <th rowspan="2"></th>
      <th colspan="3">ε</th>
      <th colspan="3">Born Effective Charges</th>
      <th colspan="2">$E_g$</th>
    </tr>
    <tr>
      <th>XX</th>
      <th>YY</th>
      <th>ZZ</th>
      <th>XX</th>
      <th>YY</th>
      <th>ZZ</th>
      <th>DFT</th>
      <th>Exp.</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>$δ_A$</th>
      <th>$Ta_2O_5$</th>
      <td>45</td>
      <td>23</td>
      <td>35</td>
      <td>7.20(-2.93)</td>
      <td>5.92(-2.42)</td>
      <td>8.40(-3.41)</td>
      <td>2.33</td>
      <td>3.9-4.5 [4]</td>
    </tr>
    <tr>
      <th></th>
      <th>$Nb_2O_5$</th>
      <td>77</td>
      <td>31</td>
      <td>65</td>
      <td>8.23(-3.34)</td>
      <td>8.23(-3.34)</td>
      <td>11.45(-4.64)</td>
      <td>1.77</td>
      <td>3.4 [25]</td>
    </tr>
    <tr>
      <th>$δ_B$</th>
      <th>$Ta_2O_5$</th>
      <td>37</td>
      <td>37</td>
      <td>9</td>
      <td>7.50(-3.05)</td>
      <td>7.50(-3.05)</td>
      <td>3.25(-1.35)</td>
      <td>2.35</td>
      <td>3.9-4.5 [4]</td>
    </tr>
    <tr>
      <th></th>
      <th>$Nb_2O_5$</th>
      <td>52</td>
      <td>52</td>
      <td>9</td>
      <td>8.02(-3.26)</td>
      <td>8.02(-3.26)</td>
      <td>3.00(-1.25)</td>
      <td>1.90</td>
      <td>3.4 [25]</td>
    </tr>
    <tr>
      <th>$\beta$</th>
      <th>$Ta_2O_5$</th>
      <td>32</td>
      <td>47</td>
      <td>47</td>
      <td>6.71(-2.73)</td>
      <td>7.45(-3.03)</td>
      <td>8.87(-3.64)</td>
      <td>2.07</td>
      <td>3.9-4.5 [4]</td>
    </tr>
    <tr>
      <th></th>
      <th>$Nb_2O_5$</th>
      <td>50</td>
      <td>81</td>
      <td>100</td>
      <td>7.08(-2.88)</td>
      <td>7.87(-3.20)</td>
      <td>9.58(-3.89)</td>
      <td>1.60</td>
      <td>3.4 [25]</td>
    </tr>
    <tr>
      <th></th>
      <th>$NbTaO_5$</th>
      <td>44</td>
      <td>54</td>
      <td>64</td>
      <td>$6.89^{*}(-2.81)$</td>
      <td>$7.65^{*}(-3.11)$</td>
      <td>$9.44^{*}(-3.83)$</td>
      <td>1.82</td>
      <td>-</td>
    </tr>
  </tbody>
</table>

A close inspection of the permittivity tensors reveals that the dielectric constants are anisotropic, especially for the $\delta_B$ phase. This latter is a good example to illustrate the impacts of the crystal structure and of the topology of different metal centers on the anisotropy of the dielectric response. The $\delta_B$ phase displays a slab-like structure without any metal-oxygen bonds to bridge the adjacent layers (Figure 1c). This peculiar structure results in a lower polarizability and in higher vibrational frequencies along the normal direction to the layers (z). The definition of the lattice-vibrational component of the dielectric permittivity [21],

$$
\varepsilon_{i o n}^{\alpha \beta}=\frac{4 \pi e^{2}}{\Omega} \sum_{\lambda} \frac{Z_{\lambda \alpha} Z_{\lambda \beta}}{\omega_{\lambda}^{2}} \tag{1}
$$

$$
Z_{\lambda \alpha}=\sum_{i \alpha} \frac{Z_{i, \alpha \beta}^{*} \xi_{i, \lambda \alpha}}{\sqrt{M_{i}}} \tag{2}
$$

($Z_{\alpha \beta}^{*}$ is the effective charge tensor, in other words the dynamical polarizability of the vibrating ions, $M_i$ – mass of the atom i, $\Omega$ – volume of the unit cell and $\xi_{i,\lambda\alpha}$ , $\omega$ are the eigenvector and eigenfrequency of the mode $\lambda$ ) clearly points up that a low

polarizability, combined with a high vibrational frequency in a given direction, leads to low permittivity component in that direction.

Interestingly, $\mathrm{Nb_2O_5}$ exhibits effective dynamical charges higher than $\mathrm{Ta_2O_5}$ (see Table I), while the frequency modes of vibration active for the dielectric response remain relatively unchanged. Therefore, the Nb based oxides display an increased ionic dielectric polarizability with respect to their Ta based counterparts. The analysis of the electronic structure reveals that the 4d orbitals of Nb are more strongly hybridized with the O 2p ones (hence forming bonds with a higher degree of covalency) compared to the 5d orbitals of the Ta atoms. As a consequence, the change in polarizability induced upon the vibrational motion is more important for the Nb centers than for the Ta ones, which leads to larger effective charges. Note that the well-known underestimation of the LDA band-gap has a direct influence on the hybridization of metal 4d (5d) with the oxygen 2p orbitals, which leads to a weak artificial enhancement of the Ta and Nb polarization charge values [22]. However, we believe that the description of the polarizability of the two metal oxides remain qualitatively correct since Nb is reported to have a higher polarizability than Ta [23, 24]. The impact on the absolute values of the computed dielectric constant is expected to be relatively small.

![](./images/811853546449272833_3.jpg)

Figure 3. Distribution of the dielectric intensity for the Ta (left panel) and Nb oxides (right panel) in $\beta$ phase with respect to the frequencies of vibration. Atomic contributions are calculated with dynamical charges of the corresponding species. The spectral range limited to the lowest energy modes.

Figure 3 illustrates the frequency-dependent dielectric intensities. These correspond to the individual terms of the summation of Eq. (1) [25]. The comparison

of the distribution of frequencies of the $Ta_2O_5$ vibrational modes to the $Nb_2O_5$ reveals that there is almost no difference between the oxides. Therefore, at a given crystal structure, the higher permittivity of $Nb_2O_5$ compared to its Ta counterpart is due to the larger dynamic polarizability of the Nb centers, rather than to a shift of the low infra- red frequency modes. The nature of the vibrations active in the dielectric constant is such that they mainly arise from the movement/distortion of the oxygen coordination cage around the metal ion, which explains the relative similitude of the frequency of vibrations in the Nb and Ta oxides. There is only a noticeable movement of the metallic ions inside the oxygen shells for the low-energy modes (i.e., below $200\ cm^{-1}$). Therefore, the contribution of the metal centers to the dielectric intensities is larger at the low-energy end of the spectrum. Note that since Nb has a lower atomic mass than Ta, it also displays larger vibrational amplitudes and its contributions to the dielectric constant are correspondingly more important (see Figure 3).

Since the orthorhombic phase of $Ta_2O_5$ is known to present site vacancies, we quantified the role of these latter on the dielectric response by introducing either one O ($V_O$) or one Ta vacancy ($V_{Ta}$) in a $1x2x2\ \beta$ orthorhombic supercell. Compared to the perfect crystal case, the dynamical charges are decreasing upon the introduction of the Ta or O vacancy (Table II). These latters result in a local distortion of the chemical environment around the defective center. As a result, the adjacent atoms have smaller dynamical charges due to the tighter metal-oxygen bonds around the vacancy, which results to a local symmetry lowering and to a shift of the frequencies of vibration towards higher values. The combination of these factors leads to a reduction of the dielectric constant. For the 1x2x2 supercell, the averaged dielectric constant of $Ta_2O_5$ is decreased from 46 (for the perfect crystal, as calculated in finite- difference approach) to 34 and 31 for a O and a Ta vacancy, respectively. Note the reduction of the dielectric constant upon the introduction of a concentration of vacancy defects that is close to the experimental value. Lessening of the $V_O$ concentration (by doubling the model cell size) boosts the dielectric constant from 34 to 41.

<table>
<caption>TABLE II. Effective dynamical charges of Ta (and O in brackets) computed for 1x2x2 $Ta_2O_5$ orthorhombic supercell with $V_O$ and $V_{Ta}$.</caption>
<thead>
<tr>
<th rowspan="2"></th>
<th rowspan="2">&lt;ε&gt;</th>
<th colspan="3">Effective Dynamical Charges</th>
</tr>
<tr>
<th>XX</th>
<th>YY</th>
<th>ZZ</th>
</tr>
</thead>
<tbody>
<tr>
<td>$Ta_2O_5$</td>
<td>46</td>
<td>6.71 (-2.73)</td>
<td>7.45 (-3.03)</td>
<td>8.87 (-3.64)</td>
</tr>
<tr>
<td>$V_O$</td>
<td>34</td>
<td>6.47 (-2.58)</td>
<td>7.15 (-2.86)</td>
<td>8.21 (-3.30)</td>
</tr>
<tr>
<td>$V_{Ta}$</td>
<td>31</td>
<td>6.49 (-2.53)</td>
<td>6.70 (-2.64)</td>
<td>8.34 (-3.18)</td>
</tr>
</tbody>
</table>

We finally explore the dielectric response of a $(Nb_{0.5}Ta_{0.5})_2O_5$ solid solution. Since the $\beta$ orthorhombic structure presents the closest match to the experimental XRD pattern (Figure 2), it has been used to illustrate the impact of the admixture on the dielectric response. In the employed orthorhombic model unit cell, the positions of the Nb and Ta atoms were chosen such that the atoms intermix homogenously along the x, y and z directions. The averaged permittivity constant is computed to be 54, i.e., approximately the arithmetic mean of the pure oxides, which is consistent with the trend reported experimentally for a set of different $NbTaO_x$ compositions and for other oxide alloys [14,26]. Similarly, the computed band gap of the mixed oxide is

calculated to be close to the arithmetic average (1.82 eV) of the LDA $Ta_2O_5$ (2.07 eV) and $Nb_2O_5$ (1.60 eV) gaps.

## Concluding remarks

To summarize, first-principles calculations predicted the hexagonal crystal structures to be less stable than the orthorhombic one. The latter would, therefore be representative for the low thermal budget (<700ºC) films. We computed anisotropic dielectric permittivities with directional components that range between 32-47, 50-100 and 44-64 for the orthorhombic $Ta_2O_5$, $Nb_2O_5$, and $NbTaO_5$ phases, respectively, that show a good agreement with experimental findings. Crystal imperfections of vacancy type were found to decrease the dielectric response. We found that Nb atoms have a higher polarizability compared to Ta ones in different crystal phases, which suggests that introducing a low concentration of Nb in a $Ta_2O_5$ matrix can be used to enhance the dielectric constant of the system while paying a minimal penalty for the reduction of the band gap.

## Acknowledgments

This work is part of the IMEC Industrial Affiliation Program on DRAM MIMCAP devices.

## References

1.  ITRS, http://www.itrs.net/.
2.  S. B. Reddy, K. P. Rao, and M. S. R. Rao, *Applied Physics a-Materials Science & Processing*, **89**, 1011 (2007).
3.  E. Atanassova and A. Paskaleva, *Microelectronics Reliability*, **47**, 913 (2007).
4.  C. Chaneliere, J. L. Autran, R. A. B. Devine, et al., *Materials Science & Engineering R*, **22**, 269 (1998).
5.  J. Lin, N. Masaaki, A. Tsukune, et al., *Applied Physics Letters*, **74**, 2370 (1999).
6.  K. Kukli, M. Ritala, and M. Leskela, *Journal of Applied Physics*, **86**, 5656 (1999).
7.  K. Kishiro, N. Inoue, S. C. Chen, et al., *Japanese Journal of Applied Physics*, **37**, 1336 (1998).
8.  K. Chang, K. Shanmugasundaram, J. Shallenberger, et al., *Thin Solid Films*, **515**, 3802 (2007).
9.  P. Giannozzi et al., www.quantum-espresso.org, (2008).
10. D. Vanderbilt, *Physical Review B*, **41**, 7892 (1990).
11. S. Baroni, S. de Gironcoli, A. Dal Corso, et al., *Reviews of Modern Physics*, **73**, 515 (2001).
12. P. Giannozzi, S. Degironcoli, P. Pavone, et al., *Physical Review B*, **43**, 7231 (1991).
13. Å. Seidl, A. Gorling, P. Vogl, et al., *Physical Review B*, **53**, 3764 (1996).
14. A. Hardy, D. Dewulf, and S. Van Elshocht, *private communications*.
15. A. Pignolet, G. M. Rao, and S. B. Krupanidhi, *Thin Solid Films*, **261**, 18 (1995).
16. A. Fukumoto and K. Miwa, *Physical Review B*, **55**, 11155 (1997).

17. L. A. Aleshina and S. V. Loginova, *Crystallography Reports*, **47**, 415 (2002).

18. B. R. Sahu and L. Kleinman, *Physical Review B*, **69**, 165202 (2004).

19. R. Ramprasad, M. Sadd, D. Roberts, et al., *Microelectronic Engineering*, **69**, 190 (2003).

20. S. J. Kim, B. J. Cho, M. Bin Yu, et al., *IEEE Electron Device Letters*, **26**, 625 (2005).

21. X. Y. Zhao and D. Vanderbilt, *Physical Review B*, **65**, 233106 (2002).

22. A. Filippetti and N. A. Spaldin, *Physical Review B*, **68**, 9 (2003).

23. M. Stromme, G. A. Niklasson, M. Ritala, et al., *Journal of Applied Physics*, **90**, 4532 (2001).

24. R. J. Cava, W. F. Peck, J. J. Krajewski, et al., *Materials Research Bulletin*, **31**, 295 (1996).

25. P. Delugas, V. Fiorentini, and A. Filippetti, *Applied Physics Letters*, **92**, 172903 (2008).

26. W. F. A. Besling, E. Young, T. Conard, et al., *Journal of Non-Crystalline Solids*, **303**, 123 (2002).