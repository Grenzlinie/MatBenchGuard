Accepted Manuscript

Investigation of the Thermal Conductivity in Nanographene $C_{80}H_{30}$ by Molecular Dynamics Simulation

Flávio Silva Dias, Horácio Wagner Leite Alves, Wagner Souza Machado

![](./images/812751976302379008_1.jpg)

PII: S2352-2143(19)30267-9

DOI: https://doi.org/10.1016/j.cocom.2019.e00421

Article Number: e00421

Reference: COCOM 421

To appear in: Computational Condensed Matter

Received Date: 14 May 2019

Revised Date: 24 June 2019

Accepted Date: 16 July 2019

Please cite this article as: F.S. Dias, H.W. Leite Alves, W.S. Machado, Investigation of the Thermal Conductivity in Nanographene $C_{80}H_{30}$ by Molecular Dynamics Simulation, Computational Condensed Matter, https://doi.org/10.1016/j.cocom.2019.e00421.

This is a PDF file of an unedited manuscript that has been accepted for publication. As a service to our customers we are providing this early version of the manuscript. The manuscript will undergo copyediting, typesetting, and review of the resulting proof before it is published in its final form. Please note that during the production process errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

# Investigation of the Thermal Conductivity in Nanographene $\boldsymbol{C_{80}H_{30}}$ by Molecular Dynamics Simulation

Flávio Silva Dias$^{a,b}$, Horácio Wagner Leite Alves$^b$, Wagner Souza Machado$^{b*}$

$^{a}$Instituto Federal da Bahia, Campus de Vitória da Conquista, 45075-265, Vitória da Conquista, BA, Brazil

$^{b}$Departamento de Ciências Naturais, Universidade Federal de São João Del Rei, Praça Dom Helvécio, 74, 36301-160, São João Del Rei, MG, Brazil

*Corresponding author. Tel: +55-32-3379-2483; E-mail: wagner@ufsj.edu.br

## Abstract

In this work the thermal conductivity $\lambda$ of warped nanographene ($C_{80}H_{30}$) was investigated through the Equilibrium Molecular Dynamics (EMD) simulations using the Green-Kubo's equation. Based on the proposed methodology, the $C_{80}H_{30}$ thermal conductivity was simulated for directions x, y and z, and for different temperatures. The obtained average thermal conductivity value, $233W\cdot m^{-1}\cdot K^{-1}$ were compared with the simulated thermal conductivity of graphene and carbon nanotube reported in the literature. The distorted molecular structure of $C_{80}H_{30}$ is responsible for its good thermal conductivity in all directions. It has been found that the $C_{80}H_{30}$ has a greater number of acoustic modes in the range from 0 to 15 THz, when compared with graphene, which must be related to a high thermal conductivity.

**Keywords:** Thermal conductivity, Nanographene $\ce{C_{80}H_{30}}$, Molecular dynamics simulations

## Introduction

Since the discovery of graphene in 2004 by Novoselov *et al.* [1], it has been investigated extensively by the scientific community, leading to the demonstration of several intriguing properties [2-4]. In particular, the thermal properties of carbon nanostructures depend on the way how the carbon atoms are bond together, resulting in different allotropic forms, such as: graphene (or '2D graphite')[5, 6], 0D fullerenes [7, 8] or 1D carbon nanotubes [9, 10]. These different carbon nanostructures give rise to different thermal properties [11].

In 2013, the nanographene ($\ce{C_{80}H_{30}}$) was synthesized by Kawasumi *et al.* [12]. This grossly warped nanostructure contains exactly 80 carbon atoms joined together in a network of 26 rings, with 30 hydrogen atoms decorating them, being confirmed by X-ray crystallography, as shown in Figure 1. Graphene tends to remain in planar geometry as a consequence of its two-dimensional hexagonal lattice. In the $\ce{C_{80}H_{30}}$ nanographene lattice, the non-hexagonal rings defects cause planarity distortions, and unique structural and physical properties appears, such as improved solubility in common organic solvents and a relatively large HOMO-LUMO gap [12].

![](./images/812751976302379008_2.jpg)

Figure 1. Molecular structure of the nanographene $C_{80}H_{30}$.

As an interesting asymmetric material, its electronic and optical properties, as well as the possible applications of these warped nanographenes, have been investigated recently [13-17], and some results show the potential use in CO chemical sensors [18] and the possibility to tune the HOMO-LUMO gap controlling the $O_2$ adsorption, demonstrating the possibility of using $C_{80}H_{30}$ in optoelectronics [13].

In addition to its electronic and optical properties, the thermal properties of $C_{80}H_{30}$ are also of fundamental and practical importance. Experiments have demonstrated that graphene [19], carbon nanotubes [20] and graphite [21] have high thermal conductivities. This opens possibilities of using graphene nanostructures for nanoscale thermal management.

In this work, we have used molecular dynamics simulation, through the EMD method, to study the thermal conductivity in nanographene $C_{80}H_{30}$. To our knowledge, the thermal conductivity of this $C_{80}H_{30}$ has not been studied yet. We have observed that the thermal conductivity of $C_{80}H_{30}$ was relatively high compared with others carbon nanostructures with similar dimensions. We have also noted that the direction with slightly higher

thermal conductivity is the one in which the atomic structure is curved. The increased thermal conductivity was related to a higher number of phonon frequencies in the range of 0 to 15 THz of its density of states when compared to the graphene. The results from the thermal conductivity analysis in carbon based nanostructures can be important for the development of nanoelectronics devices based on nanographenes.

## 2. Theoretical Framework

The calculations were done by using the classical molecular dynamics techniques, supercell approach and the Large-scale Atomic/Molecular Massively Parallel Simulation (LAMMPS) molecular dynamics program [22]. To describe the atomic interactions involved, we have used Adaptive Intermolecular Reactive Empirical Bond-order potential (AIREBO) [23]. To control the simulations, we have used the *Nanolab* virtual as graphical user interface (GUI) [24], and the thermal conductivity were obtained through the Equilibrium Molecular Dynamics simulations (EMD), based on the Green-Kubo relations [25, 26].

In the calculations, the supercell used to obtain the nanographene ($\text{C}_{80}\text{H}_{30}$) thermal conductivity was a tetragonal unit cell with lattice parameters $a = b = 1.7$ nm and $c = 1.6$ nm, resulting a volume equal to $4.624$ nm$^3$, as shown in Figure 2. These values were obtained by a systematic study of the minimum supercell dimension which keeps the integrity of the $\text{C}_{80}\text{H}_{30}$ nanostructure throughout the simulations, and it has been described as a macromolecule in a big box. It is interesting to remark that with this supercell size, the interactions between neighboring nanographenes is reduced in similar way that was observed in silicon nanowires *ab initio* calculations [27].

All simulations were performed within the canonical ensemble (*NVT* ensemble) and the step time $t_{\text{step}}$, was investigated from 0.2 to 1 fs. The system equilibrium time ($t_{\text{equil}}$) was

around 2 ns, which was used as the simulation time ($t_{simul}$) for the thermal conductivity evaluation in all cases. The thermal conductivity $\lambda$ was then obtained by evaluating the following expression

$$
\lambda_{n}=\frac{1}{k_{B} T^{2} V} \int_{0}^{\infty}\left\langle J_{n}(t) \cdot J_{n}(0)\right\rangle d t \quad (1),
$$

Where $n$ is the coordinate in each direction $x$, $y$ or $z$, $k_{\rm B}$ is the Boltzmann constant and $V$ and $T$ are the supercell volume and absolute temperature, respectively.

![](./images/812751976302379008_3.jpg)

Figure 2. Supercell used to describe the ${\rm C_{80}H_{30}}$ molecule: (a) face of upper side, and (b) side face.

The heat flux $J_{\rm n}(t)$ in each direction can be obtained by

$$
J_{n}(t)=\sum_{i} v_{n, i} E_{i}+\sum_{i} z_{i} \frac{d E_{i}}{d t} \quad (2)
$$

where $n$ and $v_{\rm n}$ are the atomic coordinate and velocity in each direction, respectively, and $E$ is the total energy.

The energy for the potential AIREBO, consists of three terms:

$$
E=\frac{1}{2} \sum_{I} \sum_{j \neq i}\left[E_{i j}^{R E B O}+E_{i j}^{L J}+\sum_{k \neq i, j} \sum_{l \neq i, j . k} E_{k i j l}^{T O R S I O N}\right] \quad (3)
$$

where $E_{i j}^{R E B O}$ is the Reactive Empirical Bond-order potential function (REBO), $E_{i j}^{L J}$ is the long-range interactions terms and $E_{k i j l}^{T O R S I O N}$ represents the torsional interaction terms dependent on dihedral angles.

To clarify the mechanism of the thermal behavior of $C_{80} H_{30}$, their phonon spectra were analyzed along each direction. For this purpose, we have calculated the phonon density of states (PHDOS) by taking the discrete Fourier transform of the velocity autocorrelation functions components (VACF), as described by Eq. 4:

$$
PHDOS(\omega)=\int_{-\infty}^{+\infty} VACF(t) e^{-i \omega t} d t \quad (4)
$$

Here $\omega$ is the phonon frequency, $i$ is the imaginary unit, and the VACF can be calculated as

$$
VACF(t)=\frac{\left\langle\sum_{i=1}^{N} \vec{v}_{i}\left(t_{0}\right) \cdot \vec{v}_{i}\left(t+t_{0}\right)\right\rangle}{\left\langle\sum_{i=1}^{N} \vec{v}_{i}\left(t_{0}\right) \cdot \vec{v}_{i}\left(t_{0}\right)\right\rangle} \quad (5)
$$

where $N$ is the number of atoms and $\vec{v}_{i}$ is the atom velocity.

The PHDOS and the thermal conductivity was also calculated for graphene, formed by 112 carbon atoms within a box with dimensions of 1 nm, 2.56 nm and 1.97 nm respectively for the $x$, $y$ and $z$ directions. These dimensions were chosen to facilitate the graphene PHDOS data comparison with the obtained $C_{80} H_{30}$ data. The PHDOS was obtained by post-processing 10 trajectories which the atomic velocities were recorded every 0.6 fs. The thermal conductivity was simulated at 300 K and the initial parameters and conditions used for the simulations of the graphene were the same as those used for $C_{80} H_{30}$.

## Results and discussions

In the first step, a study was carried out to determine the appropriated $t_{\text {step }}$ for the $C_{80} H_{30}$ thermal conductivity simulations. The energy simulation was performed as a function of

the $t_{\text{step}}$, and according to Figure 3, the minimum energy was obtained for $t_{\text{step}}$= 0.6 fs. The kinetic energy was practically constant for the interval between 0.6 and 1.0 fs, as presented in the insert graph of the Fig. 3. This may be an indication that a $t_{\text{step}}$= 0.6 fs is a reasonable value for use in the $\text{C}_{80}\text{H}_{30}$ thermal conductivity simulations.

![](./images/812751976302379008_4.jpg)

Figure 3. Total and potential energies for different $t_{\text{step}}$. Insert: kinetic energy variation for different $t_{\text{step}}$.

For stability and precision in energy conservation, it is necessary to choose a time step interval that is at least an order of magnitude lower than the system's fastest time scale [28]. This time scale can be related to the molecular vibration period $T_v$, which can have its estimated value considering a harmonic system by:

$$
T_{v}=2 \pi\left(m / k_{r}\right)^{1 / 2} \quad(6)
$$

where $m$ is the mass and $k_{r}$ is the force constant of the system.

For graphene $k_{r}$ is considered to be 740 N/m [29], the mass of the carbon atom equal to $1.99 \times 10^{-26}$ kg, and the estimated vibration period value is equal to 32.7 fs. Thus, a $t_{\text{step}}<$ 3.2 fs would be a reasonable value for the intrinsic graphene. In the literature a typical time step of 1.0 fs is used [30,31]. In the case of $\text{C}_{80}\text{H}_{30}$ there is still no report in the literature of the $k_{r}$ value to estimate the time step, so it is possible that it presents a period

close to pure graphene. On the other hand, once it is a nanostructure with intrinsic defects and composed also by hydrogen atoms, a shorter time should to be used to avoid rupture of the structure during the simulation. For these reasons, simulation of the thermal conductivity for this material using $t_{step}$= 0.6 fs should be reasonable.

In Figure 4, the results obtained for $C_{80}H_{30}$ thermal conductivity simulated, $\lambda$, are presented. The thermal conductivity was calculated in the three directions of $C_{80}H_{30}$ ($\lambda_x$, $\lambda_y$, $\lambda_z$), at temperature of 300 K. The obtained values were of $211\ \mathrm{W{\cdot}m^{-1}{\cdot}K^{-1}}$ for $\lambda_x$, $260\ \mathrm{W{\cdot}m^{-1}{\cdot}K^{-1}}$ for $\lambda_y$ and $229\ \mathrm{W{\cdot}m^{-1}{\cdot}K^{-1}}$ for $\lambda_z$. A good stability of the thermal conductivity values was obtained after a simulation time of 1000 ps and should be related to the appropriate choice of the system equilibrium time ($t_{equil}=2$ ns). It is believed that there is a rapid convergence of the thermal conductivity values and, therefore, less fluctuation after 1000 ps. This stability should also be related to the stability of the simulated molecular structure over time at the tested temperature.

![](./images/812751976302379008_5.jpg)

Figure 4. Values of the thermal conductivity in function of simulation time. $T=300$ K, $t_{step}=0.6$ fs, $t_{equil}=2$ ns.

As there is a dependence of the thermal conductivity with the size and curvature of the carbon nanostructures, it is presented in Table 1 some results from literature for simulated thermal conductivity of different carbon nanostructures at $T=300$ K. It was selected only

the direction of higher thermal conductivity and results for systems with dimensions of the same order as those used in this work for reference. From Table 1, it can be concluded that the value found for the $C_{80}H_{30}$ is in the same range of values reported in literature for different carbon nanostructure. The thermal conductivity values for the $C_{80}H_{30}$ nanostructure may be related both to the molecular size and to the structural defects as well, when compared with the graphene and carbon nanotube data.

Table 1 – Simulated thermal conductivity of carbon nanostructures at 300 K.

<table>
  <thead>
    <tr>
      <th rowspan="2">Potential</th>
      <th rowspan="2">Method</th>
      <th>Nanostructure</th>
      <th>System</th>
      <th>$\lambda máx.$</th>
      <th rowspan="2">Reference</th>
    </tr>
    <tr>
      <th></th>
      <th>legth (nm)</th>
      <th>($\text{Wm}^{-1}\text{K}^{-1}$)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>AIREBO</td>
      <td>EMD</td>
      <td>$C_{80}H_{30}$</td>
      <td>1.5</td>
      <td>260.0</td>
      <td>This work</td>
    </tr>
    <tr>
      <td rowspan="2">AIREBO</td>
      <td rowspan="2">EMD</td>
      <td>Graphene zigzag</td>
      <td>1.97</td>
      <td>141</td>
      <td rowspan="2">This work</td>
    </tr>
    <tr>
      <td>Graphene armchair</td>
      <td>2.56</td>
      <td>49</td>
    </tr>
    <tr>
      <td rowspan="2">AIREBO</td>
      <td rowspan="2">RNEMD*</td>
      <td>Graphene zigzag</td>
      <td>10.0</td>
      <td>78.0</td>
      <td rowspan="2">Ng at. al. 28</td>
    </tr>
    <tr>
      <td>Graphene armchair</td>
      <td>10.0</td>
      <td>53.6</td>
    </tr>
    <tr>
      <td>AIREBO</td>
      <td>EMD</td>
      <td>Nanotubo (10,10)</td>
      <td>2.5</td>
      <td>~173</td>
      <td>Grujicicet. $al.^{29}$</td>
    </tr>
    <tr>
      <td>REBO</td>
      <td>EMD</td>
      <td>Nanotubo (10, 10)</td>
      <td>2.5</td>
      <td>240</td>
      <td>Che at. $al.^{30}$</td>
    </tr>
    <tr>
      <td>AIREBO</td>
      <td>EMD</td>
      <td>Nanotubo (10, 10)</td>
      <td>2.5</td>
      <td>137</td>
      <td>Dias at. $Al.^{31}$</td>
    </tr>
    <tr>
      <td>-</td>
      <td>Experimental</td>
      <td>Fullerene</td>
      <td>~0.7</td>
      <td>0.4</td>
      <td>Tea at. $Al.^{8}$</td>
    </tr>
  </tbody>
  <tfoot>
    <tr>
      <td colspan="6">*Reverse Non-Equilibrium Molecular Dynamics (RNEMD).</td>
    </tr>
  </tfoot>
</table>

The curvature in the $C_{80}H_{30}$ nanostructure are responsible for the defects and for the phonons scattering in all directions, justifying the finding of relatively high values for $\lambda$ in all directions. Carbon nanotubes show a thermal conductivity increasing when its diameter is reduced, due to the smaller number of optical phonons that participate in the

scattering process in this case, and greater number of acoustic phonons that participate in the same process. For a better understanding, in the CNTs, the thermal conductivity is higher in small diameter nanotubes and decrease when the diameter increases. This can be interpreted that the thermal conductivity is related to the material curvature [36]. This phenomenon is observed in $C_{80}H_{30}$, in which its atomic structure is a bended plane of atoms in one direction, the direction with slightly higher thermal conductivity.

In the Figure 5, is presented a comparison between the evaluated PHDOS for the $C_{80}H_{30}$ with PHDOS for graphene. The nanographene $C_{80}H_{30}$ has more optical vibrational modes with frequencies greater than 83 THz than graphene. This shift in the frequency of the $C_{80}H_{30}$ in relation to the intrinsic graphene happens due of the amount of defects present in its structure in relation to the intrinsic graphene [37].

For the single wall carbon nanotube (6,6), 90% of the phonons modes that contribute to thermal conductivity are concentrated in the range of 1 to 11 THz; for the single wall carbon nanotube (2,1), the greatest contribution of the phonons to thermal conductivity comes from vibrational modes with frequencies smaller than 18 THz; and in the case of graphene, 90% of the thermal conductivity comes from vibrational modes with frequencies smaller than 13 THz [36, 38]. Based on these results it is expected that most of the phonons that contribute to the $C_{80}H_{30}$ thermal conductivity comes from vibrational modes with frequencies smaller than 15 THz. Moreover, the $C_{80}H_{30}$ also has a great number of acoustic modes in the range from 0 to 15 THz, when compared with graphene (Figure 5 (b)). This last feature could justifies why $C_{80}H_{30}$ has higher thermal conductivity than graphene. In addition, the thermal conductivity along the y-direction is higher than in the other directions, with a greater number of acoustic phonons in the range of 0 to 15 THz. This should be related to the fact that the plane of atoms is bended at this direction.

![](./images/812751976302379008_6.jpg)

Figure 5. Calculated vibrational density of states for $C_{80}H_{30}$ in the x, y and z directions compared with those of pristine grapheme: (a) from 0 to 83 THz range (b) zoom from 0 to 16 THz range.

The simulated thermal conductivity of three dimensions $C_{80}H_{30}$ was investigated in the 50-900 K temperature range. As shown in Figure 6, the $C_{80}H_{30}$ thermal conductivity values decrease with the temperature increasing. Furthermore, the results show that thermal conductivities of all directions present close values for temperatures higher than 200 K (Figure 6).

In Figure 7(a), the result of the PHDOS evaluated for different temperatures in direction y is shown. It can be concluded that the intensity of the PHDOS in the acoustic region from 0 to 15 THz, increases with increasing temperature, and this must be related to a reduction of the phonon mean free path. However, with increasing temperature, the phonon-phonon

interactions, known as the Umklapp process, start to take part leading to the reduction of the phonon time life and consequently decreasing the thermal conductivity as well [36, 39, 40].

In Figure 7(b), when the temperature increases, it occurs a reduction of the PHDOS in direction y in intensity at high frequencies related to the phonon scattering increasing. This occurs due to the increasing of the structure disorder with the temperature, a behavior also observed in amorphous graphene [41].

![](./images/812751976302379008_7.jpg)

Figure 6. Simulation of thermal conductivity for the $C_{80}H_{30}$ as a function of temperature, for the x, y and z directions.

![](./images/812751976302379008_8.jpg)

Figure 7. Calculated vibrational density of states for $C_{80}H_{30}$ in the $y$-direction for different temperature (a) from 0 to 16 THz and (b) from 70 to 83 THz.

## Conclusions

In summary, we present our results for the $C_{80}H_{30}$ simulated thermal conductivity in the three directions of the nanostructure, which was obtained by using the equilibrium molecular dynamics simulations based on Green-Kubo relationships. By comparing the obtained results for the $C_{80}H_{30}$ nanostructure with both graphene and carbon nanotube ones, we have detected that the high thermal conductivity of the $C_{80}H_{30}$ in the three directions is related to the curvature, or distorted plane that this nanostructure presents. It has been found that the $C_{80}H_{30}$ has a greater number of acoustic modes in the range from 0 to 15 THz, when compared with graphene, which must be related to a high thermal

conductivity. In addition, the thermal conductivity along the $y$-direction is higher than in the other directions, with a higher number of acoustic phonons in the range of 0 to 15 THz being identified for this direction.

# AUTHOR INFORMATION

Flávio Silva Dias is currently a Phd candidate of Graduate Program in Physics and Chemistry of Materials at Federal University of São João del Rei, MG Brazil. His interests cover construction and characterization of carbon xerogel sensors and molecular dynamics simulation of carbon based materials.

Horácio Wagner Leite Alves is currently an Associate Professor of Federal University of São João del Rei, MG Brazil. He obtained a PhD in Science at the Federal University of Paraná in 2011. His research focuses on Study of Structural Properties, Electronic Structure, Optical Excitations, Network and Surfaces Dynamics of new materials especially in the following subjects: characterization of semiconductors III-V, IV-IV and IV-VI, surfaces, alloys and nanostructures, calculation of fossils and dielectric properties, development of high-K oxides, thermoelectric materials, 2D materials, topological insulation and biological macromolecules.

Wagner Souza Machado is currently a Professor of Federal University of São João del Rei, MG Brazil. He obtained a PhD in Solid State Physics at the University of São Paulo in 1989. His research focuses on electrical characterization of organic electronic devices such as transistors, electronic memories and sensors based on carbon nanostructures and molecular dynamics simulation of carbon based materials.

### Corresponding Author

*E-mail: wagner@ufsj.edu.br

### Acknowledgments

The authors thank the support from both the Instituto Federal da Bahia and the Universidade Federal de São João del-Rei.

### References

[1] K. S. Novoselov, A. K. Geim, S. V. Morozov, D. Jiang, Y. Zhang, S. V. Dubonos, I. V. Grigorieva, A. A. Firsov, Electric field effect in atomically thin carbon films, Science 306 (2004), pp. 666–669.

[2] K. S. Novoselov, E. McCann, S. V. Morozov, V. I. Falko, M. I. Katsnelson, U. Zeitler, F. Schedin, A. K. Geim, D. Jiang, Unconventional quantum Hall effect and Berry's phase of $2\pi$ in bilayer graphene, Nat. Phys. 2 (2006), pp. 177-180.

[3] K. S. Novoselov, A. K. Geim, S. V. Morozov, D. Jiang, M. I. Katsnelson, I. V. Grigorieva, S. V. Dubonos, A. A. Firso, Two-dimensional gas of massless Dirac fermions in graphene, Nature 438 (2005), pp. 197-200.

[4] F. Schedin, A. K. Geim, S. V. Morozov, E. W. Hill, P. Blake, M .I. Katsnelson, K. S. Novoselov, Detection of individual gas molecules adsorbed on graphene, Nat. Mater. 6 (2007), 652-655.

[5] A. A. Balandin, S. Ghosh, W. Bao, L. Calizo, D. Teweldebrhan, F. Miao, C N. Lau, Superior Thermal Conductivity of Single-Layer Graphene, Nano Letters 8 (2008), pp. 902-907.

[6] M. Park, S. -C. Lee, Y. -S. Kim Length-dependent lattice thermal conductivity of graphene and its macroscopic limit. J. Appl. Phys. 114 (2013), 053506.

[7] B. W. Kroto, J. R. Heath, S. C. O'Brien, R. F. Curl, R. E. Smalley C60: buckminsterfullerene, Nature 318 (1985), pp. 162–163.

[8] N. H. Tea, R. -C. Yu, M. B. Salamon, D. C. Lorents, R. Malhotra, R. S. Ruoff, Thermal Conductivity of C60 and C70 Crystals, Applied Physics A 56 (1993), pp. 219-225.

[9] M. Fujii, X. Zhang, H. Xie, H. Ago, K. Takahashi, T. Ikuta, H. Abe, T. Shimizu, Measuring the thermal conductivity of a single carbon nanotube, Phys. Rev. Lett. 95 (2005), 065502.

[10] Q. Li, C. Liu, X. Wang, S. Fan, Measuring the thermal conductivity of individual carbon nanotubes by the raman shift method, Nanotechnology 20 (2009), 145702.

[11] A. A. A. Balandina, Thermal properties of graphene and nanostructured carbon materials, Nature Materials, 10 (2011), pp. 569-581.

[12] K. Kawasumi, Q. Zhang, Y. Segawa, L. T. Scott, K. Itami, A grossly warped nanographene and the consequences of multiple odd-membered-ring defects, Nature Chemistry 5 (2013), pp.739–744.

[13] Y. Dai, Z. Li, J. Yang, Distinct molecule adsorption behaviors on warped nanographene $\mathrm{C}_{80}\mathrm{H}_{30}$: A theoretical study, Carbon 100 (2016) 428-434.

[14] H. Dong, K. Gilmore, B. Lin, T. Hou, S. T. Lee, Z. Guo, Y. Li, Adsorption of metal adatom on nanographene: computational investigations, Carbon 89 (2015), 249-259.

[15] Y. Noguchi, O. Sugino, Symmetry breaking and excitonic effects on optical properties of defective nanographenes, J. Chem. Phys. 142 (2015) 064313.

[16] Y. Dai, Z. Li, J. Yang, Density functional study of nonlinear optical properties of grossly warped nanographene $\mathrm{C}_{80}\mathrm{H}_{30}$, J. Phys. Chem. C 118 (2014) 3313-3318.

[17] Y. Dai, Z. Li, J. Yang, A density functional study of the nonlinear optical properties of edge-functionalized nonplanar nanographenes, Chem. Phys. Chem. 16 (2015), pp. 2783-2788.

[18] S. Jameh-Bozorghi, H. Soleymanabadi, Warped $\mathrm{C}_{80}\mathrm{H}_{30}$ nanographene as a chemical sensor for CO gas: DFT studies, Physics Letters A 381 (2017), pp. 646-651

[19] A. A. Balandin, S. Ghosh, W. Bao, I. Calizo, D. Teweldebrhan, F. Miao, C. Ning Lau, Superior thermal conductivity of single-layer graphene, NANO LETTERS 8 (2008), pp. 902-907.

[20] P. Kim, L. Shi, A. Majumar, P. L. McEuen, Thermal transport measurements of individual multiwalled nanotubes, PHYSICAL REVIEW LETTERS 87 (2001), 215502.

[21] H. O. Pierson, Handbook of Carbon, Graphite, Diamonds and Fullerenes: Processing, Properties and Applications; Noyes Publications: Park Ridge, NJ, 1995.

[22] S. Plimpton, Fast parallel algorithms for short-range molecular dynamics. Journal of Computational Physics, 117 (1995), 1–19.

[23] S. J. Stuart, A. B. Tutein, J. A. Harrison, A reactive potential for hydrocarbons with intermolecular interactions, J. Chem. Phys., 112 (2000), pp. 6472–6486.

[24] Virtual NanoLab version 2016.4, QuantumWise A/S (www.quantumwise.com).

[25] L. Cui, Y. Feng, X. Zang, Dependence of Thermal Conductivity of Carbon Nanopeapods on Filling Ratios of Fullerene Molecules, J. Phys. Chem. A. 119 (2015), pp.11226-11232

[26] J. R. Lukes, H. Zhong, Thermal conductivity of individual single-wall carbon nanotubes, J. Heat Transfer 129 (2007), pp. 705–716.

[27] F. L. Almeida Cruz, A. C. M, Carvalho and H. W. Leite Alves, Solid State Communications 290 (2019), pp. 1-6.

[28] K. Sangrak, Issues on the Choice of a Proper Time Step in Molecular Dynamics, Physics Procedia 53 (2014), pp. 60-62.

[29] J. Medina, F. Avilés, A. Tapia, The bond force constants of graphene and benzene calculated by density functional theory, Molecular Physics 113 (2014), pp. 1297-1305.

[30] U. Ray, G. Balasubramanian, Reduced thermal conductivity of isotepe substituted carbon nanomaterials: Nanotube versus graphene nanoribbon. Chemical Physics Letters 599 (2014), pp. 154-158.

[31] B. Mortazavi, M. Pötschket and G. Cuniberti, Multiscale modeling of thermal conductivity of poly crystalline graphene sheets. Nanoescale 6 (2014), pp. 3344–3352.

[32] T. Y. Ng, J. J. Yeo, Z. S. Liu, A molecular dynamics study of the thermal conductivity of graphene nanoribbons containing dispersed Stone–Thrower–Wales defects, Carbon 50 (2012), pp. 4887-4893.

[33] M. Grujicic, G. Cao, B. Gersten, Atomic-scale computations of the lattice contribution to thermal conductivity of single-walled carbon nanotubes, Mater. Sci. Eng. B 107(2004), pp. 204–216.

[34] J. Che, T. Cagin, W. A. Goddard III, Thermal conductivity of carbon nanotubes, Nanotechnology 11 (2000), pp. 65–69.

[35] F. S. Dias, W. S. Machado, The effects of computational time parameter in the thermal conductivity of single-walled carbon nanotubes by molecular dynamics simulation, Computational Condensed Matter 15, (2018), p.21-24.

[36] S. –Y. Yue, T. Ouyang, M. Hu, Diameter Dependence of Lattice Thermal Conductivity of Single Walled Carbon Nanotubes: Study from Ab Initio, Nature 5 (2015), pp. 1-8.

[37] Y. Hong, J. Zhang, X. C. Zeng, Interlayer thermal conductance within a phosphorene and graphene bilayer, Nanoescala 8 (2016), pp 1921-19218.

[38] L. Zhu, B. Li, Low thermal conductivity in ultrathin carbon nanotube (2, 1), Nature 4 (2014), pp.1-6.

[39] S. Berber, Y. –K. Kwon, D. Tománek, Unusually High Thermal Conductivity of Carbon Nanotubes, Physical Review Letters 84 (2000), pp. 4613-4616.

[40] K. Tang, F. Zhu, Y. Chen, Y. Li, H. Liao, S. Liu, Molecular Dynamics Simulation on Thermal Conductivity of Single-Walled Carbon Nanotubes, $14^{th}$ International Conference on Electronic Packaging Technologyv (2013), pp. 583-586

[41] D. Liesegang, C. Oligschleger, Spectral Modifications of Graphene Using Molecular Dynamics Simulations, Journal of Modern Physics 5 (2014), pp.149-156