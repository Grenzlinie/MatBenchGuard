OPEN
# Novel Janus gamma-Pb₂XY monolayers with high thermoelectric performance X=S, Se and Y=Se, Te X≠Y

Efracio Mamani Flores $^{1,5\bowtie}$, Victor José Ramirez Rivera $^{1,5}$, Fredy Mamani Gonzalo $^{1}$, Jose Ordonez-Miranda $^{3}$, Julio R. Sambrano $^{4}$, Mario Lucio Moreira $^{2}$ & Maurício Jeomar Piotrowski²

The quest for efficient thermoelectric materials has intensified with the advent of novel Janus monolayers exhibiting exceptional thermoelectric parameters. In this work, we comprehensively investigate the structural, electronic, transport, phonon, and thermoelectric properties of novel Janus $\gamma$-Pb₂XY (X=S, Se; Y=Se, Te; X≠Y) monolayers using density functional theory combined with the Boltzmann transport equation. Our findings unveil the energetic, dynamic, thermal, and mechanical stability of these monolayers, along with their remarkable thermoelectric performance. Remarkably, the $p$-type $\gamma$-Pb₂SeTe monolayer exhibits an outstanding figure of merit (ZT) of 6.88 at 800 K, attributed to its intrinsically low lattice thermal conductivity of 0.162 Wm⁻¹K⁻¹ arising from strong phonon scattering, low group velocity, low phonon relaxation time, and a high Grüneisen parameter. Furthermore, these monolayers demonstrate high Seebeck coefficients and electrical conductivities, making them promising for efficient charge transport and thermoelectric energy conversion. Our results highlight the immense potential of Janus $\gamma$-Pb₂XY monolayers as promising candidates for high-temperature thermoelectric applications and open up exciting avenues for further exploration of these novel two-dimensional materials in energy-related technologies.

In recent years, two-dimensional (2D) materials have attracted significant attention due to their enhanced physical properties compared to the corresponding bulk counterparts $^{1,2}$. These promising materials have a wide range of applications, including electronics³, optoelectronics⁴, photovoltaics⁵, gas detection⁶, and thermoelectricity⁷.

For instance, the recent synthesis of bulk $\gamma$-GeSe via chemical vapor deposition (CVD)⁸ has prompted further investigation exploring its thermoelectric properties under monolayers form⁹. The $\gamma$ phase of group IV monochalcogenide is characterized by a buckled honeycomb lattice with a four-atomic-thick layer, presenting intriguing possibilities for its layered structure and corresponding Van der Waals (vdW) interlayer interactions involved. Notably, Jia et al.¹⁰ reported that $\gamma$-PbX monolayers exhibit a low lattice thermal conductivity and a high thermoelectric figure of merit $ZT$ ranging from 1.97 to 2.45, under a 4% of strain. Further, the recent synthesis of Janus monolayers by sulfurization¹¹ and remote hydrogen plasma¹², through the replacement of a top layer with another chemical compound, typically from the same family, enables to break the symmetry and tailor the properties of non-Janus base monolayers. In particular, this symmetry break via Janus monolayers has the potential to enhance the thermoelectric response of materials, however it is not explored yet.

The thermoelectric performance of materials is determined by the following well-known figure of merit

$$
ZT = \frac{\sigma S^{2}}{\kappa_{e} + \kappa_{l}} T = \frac{PF}{\kappa_{e} + \kappa_{l}} T, \tag{1}
$$

where $\sigma$ is the electrical conductivity, $S$ is the Seebeck coefficient, $PF = \sigma S^{2}$ is the power factor, $T$ is the temperature, and $\kappa_{e}$ and $\kappa_{l}$ are the electron and phonon thermal conductivities, respectively. A thermoelectric material

¹Department of Physics, Jorge Basadre Grohmann National University, Tacna, Perú. ²Department of Physics, Federal University of Pelotas, Pelotas, Rio Grande do Sul, Brazil. ³LIMMS, CNRS-IIS IRL 2820, The University of Tokyo, Tokyo 153-8505, Japan. ⁴Modeling and Molecular Simulation Group, São Paulo State University, Bauru, São Paulo 17033-360, Brazil. ⁵These authors contributed equally: Efracio Mamani Flores and Victor José Ramirez Rivera. ✉email: emamanif@unjbg.edu.pe

with high rate of heat-to-electricity conversion therefore should exhibit high Seebeck coefficient, high electrical conductivity, and low thermal conductivity. As there is a strong correlation among these three physical properties, the maximization of $ZT$ is challenging. For instance, materials with a wide bandgap tend to have a high Seebeck coefficient, but a low electrical conductivity, which reduces $PF$ and hence $ZT$. Another approach to maximize $ZT$ involves searching for materials with low lattice thermal conductivity, which can be achieved through strain engineering$^{13-15}$, phonon manipulation$^{16-18}$, including four-phonon processes$^{19}$ or doping$^{20,21}$. Considering that $\kappa_e$ is proportional to $\sigma$, the reduction of $\kappa_l$ represents a key strategy to enhance $ZT^{22}$.

In this study, we systematically investigate the thermoelectric properties of Janus $\gamma$-Pb₂XY (X=S, Se; Y=Se, Te; X≠Y) monolayers using density functional theory (DFT) combined with the Boltzmann transport equation (BTE). We find a notable reduction in the cross-plane lattice thermal conductivity of all Janus monolayers and explain the physical mechanisms driving its values. A maximum figure of merit $ZT = 6.88$ was obtained for $p$-type carriers at 800 K for Janus $\gamma$-Pb₂SeTe monolayer. These findings highlight the exceptional thermoelectric response of Janus $\gamma$-Pb₂XY monolayers and lay the foundation for their applications in thermoelectricity.

## Computational details
Theoretical calculations were conducted using the open-access software Quantum Espresso$^{23}$ employing the projector-augmented wave (PAW) method$^{24}$ with the Perdew-Burke-Ernzerhof (PBE) formulation$^{25}$ for the structural, mechanical, electronic and thermoelectric properties of this research. To mitigate overestimations of electronic properties, we employed the Heyd-Scuseria-Ernzerhof (HSE06) hybrid functional$^{26}$. van der Waals interactions within each Janus monolayer were accounted for using the DFT-D3 approach by Grimme$^{27}$. Brillouin zone integration was performed using an 18x18x1 k-point grid, with a cut-off energy of 800 eV for the expansion of the plane wave basis. Convergence criteria for structural optimization were set to a force threshold of $1 \times 10^{-3}$ Ry/Bohr, with an energy convergence criterion of $10^{-12}$ Ry for self-consistent electronic iterations. Convergence tests, including those for the energy cutoff and $\mathbf{k}$-mesh, are detailed in the Supplementary Material (SM) (Fig. S1).

We assessed dynamic stability using Phonopy$^{28}$ with 6x6x1 supercells and a 2x2x1 $\mathbf{k}$-points grid based on the finite displacement method, incorporating rotational symmetry of free space using the HiPhive package$^{29}$. We ensured that the out-of-plane acoustic mode (ZA) strictly followed Born-Huang constraints$^{30}$. Mechanical properties were obtained using the Strain-Energy methodology$^{31}$, considering ion relaxation coefficients through the rectangular unit cell, as shown in Fig. 1a. Carrier mobility and relaxation time were derived from the deformation potential theory proposed by Bardeen and Shockley$^{32}$. Ab initio molecular dynamics simulations utilized a 4x4x1 supercell and a $\Gamma$-centered $\mathbf{k}$-point mesh sampling, with an energy cutoff of 400 eV within the canonical ensemble NVT, implemented using the VASP computational code$^{33}$.

Electronic transport properties were investigated using the Boltzmann transport equations under the constant relaxation time approximation (CRTA) in BoltzTraP2$^{34}$ with a finer 54x54x1 $\mathbf{k}$-point mesh using PBE functional. Lattice thermal conductivity was determined using second-order (harmonic, 6x6x1) and third-order (anharmonic, 3x3x1) interatomic force constants (IFCs) through Phonopy+HiPhive and Phono3py$^{35}$ with 2x2x1 and 4x4x1 $\mathbf{k}$-points grids, respectively, under the solution of the linearized Boltzmann transport equation (LBTE)$^{36}$ with a Q-grid of 80x80x1. To account for the influence of lattice conductivity along the $z$ axis in 2D materials, a scaling factor was applied by multiplying $L_z/h$, where $L_z$ is the length of the unit cell along the $z$ axis and $h$ is the thickness of the monolayer, considering only the $x$ and $y$ directions. All thermoelectric properties were evaluated in the temperature range from 300K to 800K.

![](./images/1021633078444949576_1.jpg)

Figure 1. (a) Top and (b) side views of Janus $\gamma$-Pb₂XY (X=S, Se; Y=Se, Te; X≠Y) monolayers. In (a), the solid black line represents the unit cell, while the red dashed line denotes the orthogonal cell used for calculating the elastic constants. Figure (b) presents a schematic diagram illustrating the distances, angles, and heights for each Janus monolayer.

## Results and discussion
### Structural properties
The optimized structures for each Janus $\gamma$-Pb₂XY (X=S, Se; Y=Se, Te; X≠Y) monolayer are depicted in Fig. 1a, conforming to the space group $P3m1$ (No. 156). Two unit cells are observed: the unit cell denoted by a solid black line is used for the general calculations of this research, whereas the rectangular dashed unit cell denoted in red is employed for the mechanical properties of the material. Additionally, in Fig. 1b, a vacuum implementation along the $c$ direction of $30$ Å is shown to eliminate any other periodic interactions and work directly with the $xy$ plane.

We also provide the heights, distances, and angles between atoms of each monolayer, as observed in Table 1. Notably, Janus monolayers can be formed by replacing the top part of the $\gamma$-PbX monolayers, substituting the top layer with another chemical element. The obtained lattice parameters fall within the range of 4.10–4.31 Å, as shown in Table 1. These values are consistent with the average values of their base monolayers ($\gamma$-PbX), which are 4.04, 4.18, and 4.43 Å for $\gamma$-PbS, $\gamma$-PbSe, and $\gamma$-PbTe, respectively, as demonstrated in the theoretical work by Jia et al.¹⁰. This behavior of the lattice parameter for Janus monolayers, being essentially the average of their respective base monolayers, has been observed in other experimental and theoretical results¹²˙³⁷. The bond lengths of $d_{\text{Pb-X}}$ and $d_{\text{Pb-Y}}$ increase with the atomic radius of the chalcogenides, similarly to the height $h$, as seen in Table 1.

When predicting new materials through theoretical studies, it is crucial to assess their stability, demonstrated here through cohesion energy, phonon dispersion plots, molecular dynamics, and mechanical stability (section of Mechanical properties). First, we evaluate the strength of the chemical bond (cohesive energy) via

$$
E_{coh} = \frac{E_{\text{Total}} - \left(N_{\text{Pb}}E_{\text{Pb}} + N_{\text{X}}E_{\text{X}} + N_{\text{Y}}E_{\text{Y}}\right)}{N_{\text{Pb}} + N_{\text{X}} + N_{\text{Y}}}, \tag{2}
$$

where $E_{\text{Total}}$ represents the total energy of the system for each monolayer, $N_{\text{Pb}}$, $N_{\text{X}}$, and $N_{\text{Y}}$ denote the number of atoms in the unit cell for each element, and $E_{\text{Pb}}$, $E_{\text{X}}$, and $E_{\text{Y}}$ represent the individual energy of each atom for Pb, X, and Y. The results are presented in Table 1, showing negative values, indicating greater attraction between the atoms than the energy required to separate them, suggesting energetic stability, similar with other Janus monolayers³⁸⁻⁴⁰.

Additionally, we present the phonon dispersion plot in Fig. 2a, revealing the absence of imaginary frequencies, indicating dynamic stability for each Janus monolayer. Notably, there is no gap between the acoustic and optical phonons, with high-frequency acoustic branches overlapping with low-frequency optical branches. This behavior, observed in other theoretical studies, leads to low thermal conductivity due to strong scattering between acoustic and optical phonons¹⁰˙⁴¹. Acoustic phonons are mainly dominated by Pb, while optical phonons are primarily dominated by the top X layer.

We observe that as the atomic mass of the chalcogenides increases, the maximum frequency decreases, with maximum values of 7.31, 6.80, and 4.76 THz for Janus $\gamma$-Pb₂SSe, $\gamma$-Pb₂STe, and $\gamma$-Pb₂SeTe monolayers,

<table>
  <thead>
    <tr>
      <th>Monolayer</th>
      <th>$a$</th>
      <th>$d_{\text{Pb-X}}$</th>
      <th>$d_{\text{Pb-Y}}$</th>
      <th>$\phi_{\angle\text{X-Pb-X}}$</th>
      <th>$\phi_{\angle\text{Y-Pb-Y}}$</th>
      <th>$\phi_{\angle\text{Pb-Pb-Pb}}$</th>
      <th>$h$</th>
      <th>$E_{coh}$</th>
      <th>$C_{11}$</th>
      <th>$C_{12}$</th>
      <th>$C_{66}$</th>
      <th>$Y_{2\text{D}}$</th>
      <th>$\nu$</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>$\gamma$-Pb₂SSe</td>
      <td>4.10</td>
      <td>2.72</td>
      <td>2.82</td>
      <td>97.95</td>
      <td>93.40</td>
      <td>65.79</td>
      <td>5.80</td>
      <td>− 4.10</td>
      <td>37.54</td>
      <td>9.45</td>
      <td>14.05</td>
      <td>35.16</td>
      <td>0.252</td>
    </tr>
    <tr>
      <td>$\gamma$-Pb₂STe</td>
      <td>4.25</td>
      <td>2.75</td>
      <td>3.00</td>
      <td>101.54</td>
      <td>90.45</td>
      <td>67.39</td>
      <td>5.89</td>
      <td>− 3.95</td>
      <td>36.61</td>
      <td>7.51</td>
      <td>14.55</td>
      <td>35.07</td>
      <td>0.205</td>
    </tr>
    <tr>
      <td>$\gamma$-Pb₂SeTe</td>
      <td>4.31</td>
      <td>2.86</td>
      <td>3.01</td>
      <td>97.92</td>
      <td>91.51</td>
      <td>68.60</td>
      <td>6.00</td>
      <td>− 3.84</td>
      <td>35.71</td>
      <td>12.02</td>
      <td>11.85</td>
      <td>31.66</td>
      <td>0.337</td>
    </tr>
  </tbody>
</table>

Table 1. The calculated values for various properties of Janus $\gamma$-Pb₂XY (X=S, Se; Y=Se, Te; X≠Y) monolayers: lattice constant $a$ (Å), bond lengths $d$ (Å), bond angles $\phi$ (°), thickness $h$ (Å), cohesive energy $E_{coh}$ (eV/atom), relaxed ion stiffness constants $C_{ij}$, Young's modulus $Y_{2\text{D}}$ (Nm⁻¹), Poisson's ratio $\nu$. In the notation, the atoms of the top and bottom layers are denoted by X and Y, respectively.

![](./images/1021633078444949576_2.jpg)

Figure 2. (a) The calculated phonon dispersions with their respective atomic projected phonon density of states and (b) the results of Ab initio molecular dynamic simulations at 300 K, both for Janus $\gamma$-Pb₂XY (X=S, Se; Y=Se, Te; X≠Y) monolayers.

respectively. This trend can be attributed to the heavier atoms vibrating at lower frequencies due to their greater inertia, contrasting with lighter atoms that vibrate at higher frequencies. Furthermore, ab-initio molecular dynamics simulations were conducted at room temperature under the canonical NVT ensemble to observe energy fluctuations over a range of 0-10 picoseconds in each Janus monolayer. The energy fluctuation was found to be insignificant, with no observed structural phase changes or chemical bond ruptures during the simulation (Fig. S3 in SM). This result confirms the thermal stability of all Janus monolayers at room temperature, as depicted in Fig. 2b. In addition, according to Bader's charge analysis (Table S1 in SM), it is evident that Pb₁ atoms share 0.712 electrons to X (X=S, Se), being higher compared to the 0.481 electrons shared by Pb₂ atoms to Y (Y=Se, Te), so there is a strong bond between Pb₁-X and Pb₂-Y bonds, gaining more electrons to X and Y atoms in each Janus monolayer due to electronegativity, also forming part of metavalent bonds. This appearance of metavalent bonds in each Janus monolayer corroborates a possible low thermal conductivity at first instance. This same behavior has been seen in the Janus $\gamma$-Ge₂SSe⁴² monolayer where its metavalent bond was corroborated by Bader charges.

## Mechanical properties
To confirm the mechanical stability of the Janus monolayers studied here, we assessed the elastic stiffness coefficients $C_{ij}$ (using Voigt notation) utilizing the rectangular unit cell depicted in Fig. 1. We applied uniaxial ($\varepsilon_{x/y}$) and biaxial ($\varepsilon_{xy}$) strains ranging from -1% to 1% with increments of 0.5%, and at each strain level, we performed a relaxation of the atomic positions. The elastic stiffness coefficients were evaluated using the following expressions

$$
\frac{\Delta E(S, \varepsilon_{i})}{S_{0}}=\frac{1}{2}\left(C_{11} \varepsilon_{11}^{2}+C_{22} \varepsilon_{22}^{2}+2 C_{12} \varepsilon_{11} \varepsilon_{22}+4 C_{66} \varepsilon_{12}^{2}\right),
\tag{3}
$$

$$
C_{11}=\frac{1}{S_{0}} \frac{\partial U}{\partial \varepsilon_{11}^{2}}, C_{22}=\frac{1}{S_{0}} \frac{\partial U}{\partial \varepsilon_{22}^{2}}, \quad C_{12}=\frac{1}{S_{0}} \frac{\partial U}{\partial \varepsilon_{11} \varepsilon_{22}},
\tag{4}
$$

where $S_{0}$ is the area of the rectangular cell, $\Delta E$ is the energy variation with respect to the equilibrium energy, $U$ represents the total energy of the system, $\varepsilon_{11}$ is the deformation in the $x$ direction, $\varepsilon_{22}$ is the deformation in the $y$ direction and $\varepsilon_{12}$ is the simultaneous deformation in the $x$ and $y$ directions.

To analyze the mechanical properties of the Janus monolayers, we need to obtain the elastic stiffness constants $C_{ij}$ using Voigt notation. Since it is a hexagonal structure, we obtain two elastic stiffness constants, $C_{11}$ and $C_{22}$, along with $C_{12}$, where $C_{66}$ can be derived as $(C_{11}-C_{12})/2$. We organize these constants into a matrix as

$$
C_{ij}=\left(\begin{array}{ccc}
C_{11} & C_{12} & 0 \\
C_{21} & C_{22} & 0 \\
0 & 0 & \left(C_{11}-C_{22}\right) / 2
\end{array}\right).
\tag{5}
$$

The mechanical stability of these monolayers is determined by Born's mechanical stability criterion⁴³, which requires that $C_{11}>0$ and $C_{11}^{2}>C_{12}^{2}$. As demonstrated in Table 1, all Janus monolayers in this study meet these criteria, indicating their mechanical stability.

To examine the angular dependence of Young's modulus and Poisson's ratio, we utilize the elastic stiffness coefficients defined in Equation (4). We establish the following relationships

$$
Y_{2 \mathrm{D}}(\theta)=\frac{C_{11} C_{22}-C_{12}^{2}}{C_{11} \sin ^{4} \theta+C_{22} \cos ^{4} \theta-\Pi \sin ^{2} \theta \cos ^{2} \theta},
\tag{6}
$$

$$
\nu(\theta)=\frac{C_{11} C_{22}-\Pi \sin ^{2} \theta \cos ^{2} \theta-C_{12}\left(\sin ^{4} \theta+\cos ^{4} \theta\right)}{C_{11} \sin ^{4} \theta+C_{22} \cos ^{4} \theta+\Pi \sin ^{2} \theta \cos ^{2} \theta},
\tag{7}
$$

where $\Pi=\left[\left(C_{11} C_{22}-C_{12}^{2}\right) / C_{66}-2 C_{12}\right]$ and $\theta$ represents the angular dependence for Young's modulus and Poisson's coefficient, respectively. As illustrated in Fig. 3 and detailed in Table 1, directional mechanical isotropy is observed for each Janus monolayer, with low Young's modulus indicating flexibility. Deformation is applied in a given direction to determine the ideal strength and critical strain. This is expressed as $\varepsilon_{x / y, x y}=\left(a-a_{0}\right) / a_{0}$, where $a_{0}$ represents the optimized lattice parameter and $a$ is the material's deformed value based on the rectangular unit cell. As seen in Fig. 3d-f, uniaxial deformation is applied in the $x$ direction (Zig Zag) and $y$ direction (Armchair), meanwhile biaxial deformation along $xy$ direction is at Figure S2 in SM. The vacuum through $c$ rescaled the stress. It was demonstrated that the stress along the ZigZag direction can handle more stress compared to the Armchair direction, reaching a critical point of 2.01 (1.87) N/m, 1.92 (1.87) N/m, and 2.03 (1.91) N/m at a critical strain of 18 (18) %, 16 (18) %, and 17 (16) % along the ZigZag (Armchair) direction for Janus $\gamma$-Pb₂SSe, $\gamma$-Pb₂STe, and $\gamma$-Pb₂SeTe monolayers, respectively. As observed in Figure S2, the stress resistance is higher compared to the uniaxial ones, reaching a critical point almost twice as high compared to the uniaxial strains, with values of 3.78, 4.87, and 3.70 at a critical strain of 17, 17, and 24 % for Janus $\gamma$-Pb₂SSe, $\gamma$-Pb₂STe, and $\gamma$-Pb₂SeTe monolayers, respectively. Among the studied Janus monolayers, $\gamma$-Pb₂STe withstands the highest stress and highest biaxial strain. It is crucial to understand the maximum stress that Janus $\gamma$-Pb₂XY (X=S, Se; Y= Se, Te; X≠Y) monolayers can withstand, as the material can break once it reaches its maximum strength.

## Electronic properties
Afterwards, we delved into the electronic characteristics of the Janus $\gamma$-Pb₂XY (X=S, Se; Y= Se, Te; X≠Y) monolayers, considering both the PBE and HSE06 functionals. The band structure outcomes are illustrated in Fig. 4.

![](./images/1021633078444949576_3.jpg)

Figure 3. (a) Top view of Janus $\gamma$-Pb$_2$XY (X=S, Se; Y= Se, Te; X≠Y) monolayers, illustrating the Zigzag and Armchair directions based on the rectangular unit cell. (b) Young's modulus $Y_{2D}(\theta)$, (c) Poisson's ratio $\nu(\theta)$ as functions of the angle $\theta$ and (d-f) Stress-strain curve along Zig Zag (x) and Armchair (y) direction.

![](./images/1021633078444949576_4.jpg)

Figure 4. The band structures of Janus $\gamma$-Pb$_2$XY (X=S, Se; Y= Se, Te; X≠Y) monolayers, calculated using the PBE and HSE06 functionals. The results are represented by solid and dashed lines, respectively, showcasing the electronic behavior of these materials under different theoretical frameworks, (a) Represent the band structure for $\gamma$-Pb$_2$SSe (b) Represent the band structure for $\gamma$-Pb$_2$STe (c) Represent the band structure for $\gamma$-Pb$_2$SeTe.

revealing that all monolayers possess an indirect bandgap. Specifically, using the PBE functional, the bandgap measures 0.87 eV, 1.01 eV, and 0.78 eV for $\gamma$-Pb$_2$SSe, $\gamma$-Pb$_2$STe, and $\gamma$-Pb$_2$SeTe, respectively. With the HSE06 functional, these values increase to 1.39 eV, 1.53 eV, and 1.23 eV for the same monolayers. These bandgaps exceed those reported for their base monolayers by Nair et al. $^{41}$.

In all Janus monolayers, the conduction band minimum (CBM) is located at the $\Gamma$ point, and the valence band maximum (VBM) is at the K-$\Gamma$ point. Around the VBM, the presence of the Mexican hat is noted, which was also observed in other $\gamma$-monolayers$^{44-47}$. Both peaks are located at K-$\Gamma$ and $\Gamma$-M along with a small energy level difference, which can be influenced by external factors, primarily deformation, resulting in an energy level shift, causing carrier mobility and corresponding bandgaps to be affected$^{48-51}$. In the case of these Janus monolayers in the $\gamma$ phase, due to the new valley at $\Gamma$-M.

Next, we evaluated the projected band structure to determine which orbitals of each element play a significant role in CBM and VBM, as shown in Fig. 5. Primarily, it is observed that CBM is mainly dominated by the Pb-$p$ orbitals in each Janus monolayer, while VBM is primarily dominated by the X-$p$ orbital (the compound of the top layer) with a slight contribution from the Y-$p$ orbitals (the compound of the bottom part). This representation provides insights into the electronic properties of the materials, illustrating the contributions of different atomic orbitals to the band structure.

Another important parameter to consider in electronic properties is the Work Function, which is basically the energy required for an electron to leave the material surface and can be determined by average planar electrostatic potentials. As can be seen in Fig. 6, where the Work Function is given by $\Phi = E_{\text{vac}} - E_{\text{F}}$, where $E_{\text{vac}}$ is the vacuum energy and $E_{\text{F}}$ is the Fermi level.

![](./images/1021633078444949576_5.jpg)

**Figure 5.** The projected band structure of Janus $\gamma$-Pb$_2$XY (X=S, Se; Y= Se, Te; X≠Y) monolayers using the PBE functional. (a) Shows the projected band structure for $\gamma$-Pb$_2$SSe. (b) Shows the projected band structure for $\gamma$-Pb$_2$STe. (c) Shows the projected band structure for $\gamma$-Pb$_2$SeTe.

![](./images/1021633078444949576_6.jpg)

Figure 6. The average plane electrostatic potentials of Janus $\gamma$-Pb₂XY (X=S, Se; Y= Se, Te; X≠Y) monolayers, along with the work functions on the bottom side Y and top X. This visualization provides insights into the charge distribution and electrostatic properties of the monolayers. Additionally, the work functions $\Phi_1$ and $\Phi_2$ on the bottom and top sides, respectively, are indicated, with $\Delta\Phi$ representing the difference in the vacuum level between the two sides. (a) Shows the electrostatic potential and work functions for $\gamma$-Pb₂SSe. (b) Shows the electrostatic potential and work functions for $\gamma$-Pb₂STe. (c) Shows the electrostatic potential and work functions for $\gamma$-Pb₂SeTe.

Due to the structural asymmetry resulting from the difference in atoms both at the top and bottom of the monolayer, a difference in electronegativity is proposed, necessitating the correction of dipoles on each Janus monolayers. It was confirmed that there is a difference in vacuum energy on both sides of the Janus monolayers (which consequently causes a difference in work functions), with a dependence on atomic radius; the greater the difference in atomic radius between X and Y, the greater their $\Delta\Phi$. The results are observed in Table 2, obtaining $\Delta\Phi$ of 0.47, 1.02, and 0.69 eV for Janus $\gamma$-Pb₂SSe, $\gamma$-Pb₂STe, and $\gamma$-Pb₂SeTe monolayers, respectively. Based on $\Phi_1$ and $\Phi_2$, we can conclude that $\Phi_1$, corresponding to the bottom part of the monolayer, is greater than $\Phi_2$, corresponding to the top part of the monolayer, suggesting that electrons from the top layer are relatively easier to remove compared to $\Phi_1$, consequently requiring less energy to escape from the surface.

### Carrier mobility
Carrier mobility is a crucial parameter in determining the potential applications of materials in electronic devices. In this study, we employed the deformation potential theory proposed by Bardeen and Shockley³², which has been widely utilized in theoretical investigations and has been adapted for 2D materials⁵². The carrier mobility ($\mu_{2D}$) can be expressed as

$$
\mu_{2D} = \frac{e\hbar^3 C_{2D}}{k_B T m^* \overline{m} E_d^2}, \tag{8}
$$

where, $e$ and $\hbar$ represent the elementary charge and reduced Planck's constant, respectively. $C_{2D}$ denotes the 2D elastic stiffness, obtained by fitting the strain-energy curve along the $x$/$y$ directions:

$$
C_{2D} = \frac{1}{A_0} \frac{\partial E_s}{\varepsilon_{\text{uni}}^2}, \tag{9}
$$

where $A_0$ is the equilibrium unit cell area, and $E_s$ is the strain-energy difference between the deformed and undeformed unit cell. Additionally, $k_B$ is Boltzmann constant, $T$ is the temperature (room temperature), $m^*$ and $\overline{m}$ represent the effective mass and its average, respectively, determined by fitting a parabolic function to the energy dispersion curve for both electrons (CBM) and holes (VBM) along the $x$/$y$ transport direction. The effective mass ($m^*$) is given by

<table>
  <thead>
    <tr>
      <th>Monolayer</th>
      <th>$E_{\text{g}}^{\text{PBE}}$</th>
      <th>$E_{\text{g}}^{\text{HSE06}}$</th>
      <th>$\overline{E}_{\text{Vac}}$</th>
      <th>$E_{\text{F}}$</th>
      <th>$\Delta\Phi$</th>
      <th>$\Phi_1$</th>
      <th>$\Phi_2$</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>$\gamma$-Pb₂SSe</td>
      <td>0.87</td>
      <td>1.39</td>
      <td>3.51</td>
      <td>−1.92</td>
      <td>0.47</td>
      <td>5.19</td>
      <td>5.66</td>
    </tr>
    <tr>
      <td>$\gamma$-Pb₂STe</td>
      <td>1.01</td>
      <td>1.53</td>
      <td>3.41</td>
      <td>−1.64</td>
      <td>1.02</td>
      <td>4.54</td>
      <td>5.56</td>
    </tr>
    <tr>
      <td>$\gamma$-Pb₂SeTe</td>
      <td>0.78</td>
      <td>1.23</td>
      <td>3.36</td>
      <td>−1.72</td>
      <td>0.69</td>
      <td>4.73</td>
      <td>5.42</td>
    </tr>
  </tbody>
</table>

Table 2. The bandgaps ($E_{\text{g}}$) calculated using both PBE and HSE06 functionals, along with the vacuum energy ($\overline{E}_{\text{Vac}}$), the Fermi level ($E_{\text{F}}$), the work functions ($\Phi_1$ and $\Phi_2$) with respect to the bottom and top layers, respectively, and their corresponding work function difference ($\Delta\Phi$) are summarized for Janus $\gamma$-Pb₂XY (X=S, Se; Y= Se, Te; X≠Y) monolayers. All values shown are in eV.

<table><thead><tr><th></th><th>Monolayer</th><th>$m_x^*/m_0$</th><th>$m_y^*/m_0$</th><th>$C_{2D}^x$</th><th>$C_{2D}^y$</th><th>$E_d^x$</th><th>$E_d^y$</th><th>$\mu_{2D}^x$</th><th>$\mu_{2D}^y$</th><th>$\tau_x$</th><th>$\tau_y$</th></tr></thead><tbody><tr><td rowspan="3">Electron</td><td>$\gamma$-Pb₂SSe</td><td>0.17</td><td>0.17</td><td>24.83</td><td>24.81</td><td>− 8.486</td><td>− 8.486</td><td>264.39</td><td>264.18</td><td>25.05</td><td>25.03</td></tr><tr><td>$\gamma$-Pb₂STe</td><td>0.14</td><td>0.14</td><td>26.76</td><td>26.84</td><td>− 8.346</td><td>− 8.362</td><td>393.56</td><td>393.17</td><td>32.26</td><td>32.23</td></tr><tr><td>$\gamma$-Pb₂SeTe</td><td>0.13</td><td>0.13</td><td>29.41</td><td>29.41</td><td>− 8.962</td><td>− 8.962</td><td>461.28</td><td>461.42</td><td>34.10</td><td>34.11</td></tr><tr><td rowspan="3">Hole</td><td>$\gamma$-Pb₂SSe</td><td>0.55</td><td>0.55</td><td>24.83</td><td>24.81</td><td>− 4.174</td><td>− 4.170</td><td>101.28</td><td>101.40</td><td>31.52</td><td>31.56</td></tr><tr><td>$\gamma$-Pb₂STe</td><td>0.56</td><td>0.56</td><td>26.76</td><td>26.84</td><td>− 4.760</td><td>− 4.760</td><td>78.85</td><td>79.07</td><td>25.32</td><td>25.39</td></tr><tr><td>$\gamma$-Pb₂SeTe</td><td>0.47</td><td>0.47</td><td>29.41</td><td>29.41</td><td>− 4.906</td><td>− 4.906</td><td>118.26</td><td>119.29</td><td>31.54</td><td>31.55</td></tr></tbody></table>

Table 3. The carrier effective mass, $m^{*}$, 2D elastic modulus, $C_{2D}$ (Nm⁻¹), deformation potential constant, $E_{d}$ (eV), carrier mobility, $\mu_{2D}$ (cm²V⁻¹s⁻¹), and relaxation time, $\tau$ (fs), at room temperature, along the transport directions $x$ and $y$ for Janus $\gamma$-Pb₂XY (X=S, Se; Y= Se, Te; X≠Y) monolayers. Here, $m_0$ denotes the mass of a free electron.

$$
m^{*}=\hbar^{2}\left[\frac{\partial^{2} E(k)}{\partial k^{2}}\right]^{-1}, \tag{10}
$$

while the average effective mass $(\overline{m})$ is calculated as the geometric mean of the masses along the $x$ and $y$ directions $(\overline{m}=\sqrt{m_{x} m_{y}})$. Furthermore, $E_{d}$ represents the deformation potential constant for CBM and VBM along the $x/y$ directions, as defined below

$$
E_{d}=\frac{\Delta E_{\text {edge }}}{\varepsilon_{\text {uni }}}, \tag{11}
$$

where $\Delta E_{\text {edge }}$ is the energy displacement for CBM and VBM concerning the vacuum level when a uniaxial strain $\varepsilon_{x/y}$ is applied.

The results obtained from applying this theory to determine $C_{2D}$ and $E_{d}$ are depicted in Fig. 7, with solid lines representing the fitting performed to obtain these values. Table 3 presents the obtained values, showcasing isotropic behavior for all monolayers in this study. Moreover, it is notable that the carrier mobility for electrons exceeds that of holes, which can be attributed to factors such as effective mass and potential deformation constant. Across all monolayers, the effective mass of electrons is lower than that of holes, a significant factor in electronic devices as it implies greater curvature in CBM/VBM, facilitating a better response to charge carriers. Additionally, the potential deformation constant is relatively lower in VBM compared to CBM due to a low slope, contributing to a carrier mobility that is not excessively low. For instance, the carrier mobility for electrons (holes) was observed to be 264.39 (101.28), 393.56 (78.85), and 461.42 (118.26) cm²V⁻¹s⁻¹ along the X-direction, with a similar trend observed along the Y-direction, for Janus $\gamma$-Pb₂SSe, $\gamma$-Pb₂STe, and $\gamma$-Pb₂SeTe monolayers, respectively (as shown in Table 3).

It is worth noting that all Janus monolayers in this study exhibit high carrier mobility, surpassing that of single-layer $MoS_2$ with a value of 200 cm²V⁻¹s⁻¹ reported by Radisavljevic et al.⁵³. However, with increasing

![](./images/1021633078444949576_7.jpg)

Figure 7. (a) Strain-energy and (b) CBM/VBM of Janus $\gamma$-Pb₂XY (X=S, Se; Y= Se, Te; X≠Y) monolayers plotted against the uniaxial strains along the $x/y$ direction $(\epsilon_{uni}^{x/y})$. Data fitting is represented by solid lines in each plot.

temperature, the carrier mobility performance tends to decrease (see Fig. S4), attributed to the rise in phonon contributions. Nevertheless, it is important to emphasize that using the DP theory overestimates the carrier mobility because it does not include different mechanisms of carrier scattering given mainly by electron-phonon couplings.

Phonon transport properties and lattice thermal conductivity
The lattice thermal conductivity, determined via the LBTE, is expressed using Cartesian coordinates $\alpha\beta$ as follows

$$
\kappa^{\alpha \beta}=\sum_{b} \frac{1}{k_{\mathrm{B}} T^{2} V} \times\left\langle f_{0}\left(\omega_{\mathbf{q}, b} ; T\right)\left[1+f_{0}\left(\omega_{\mathbf{q}, b} ; T\right)\right]\left(\hbar \omega_{\mathbf{q}, b}\right)^{2} v_{\mathbf{q}, b}^{\alpha} F_{\mathbf{q}, b}^{\beta}\right\rangle_{\mathbf{q}}.
$$

Here, $b$ represents a phonon mode, $\omega_{\mathbf{q}, b}$ is the angular frequency, $v_{\mathbf{q}, b}$ is the group velocity for each phonon mode at the $\mathbf{q}$-point in reciprocal space, $f_{0}(\omega_{\mathbf{q}, b};T)$ is the equilibrium occupation for a respective phonon mode at temperature $T$, $F_{\mathbf{q}, b}$ is the Cartesian vector of coefficients, $\langle\cdots\rangle_{\mathbf{q}}$ denotes averaging over the first Brillouin zone. $F_{\mathbf{q}, b}$ is obtained from the solution of the LBTE and is directly related to the phonon lifetime $^{54}$. The group velocity $v_{\mathbf{q}, b}$ and phonon lifetime $\tau_b$ are given by the following relations

$$
v_{\mathbf{q}, b}=\frac{\partial \omega_{b}}{\partial \mathbf{q}}, \tau_{b}=\frac{1}{2 \Gamma_{b}\left(\omega_{b}\right)}, \tag{12}
$$

respectively, where the properties of harmonic phonons for each phonon mode $b$ are distributed, and $\Gamma_{b}(\omega_b)$ takes the form analogous to the Fermi golden rule.

Another parameter indicating strong anharmonicity is the Grüneisen parameter $\gamma$, expressed in terms of the reciprocal wave vector $\mathbf{q}$ and the phonon mode $b$ through

$$
\gamma_{b}(\mathbf{q})=-\frac{a}{\omega_{b}} \frac{\partial b}{\partial a}, \tag{13}
$$

Here, $a$ is the lattice parameter. The Grüneisen parameter $\gamma$ describes the anharmonicity of a system; the larger $\overline{|\gamma|}$, the stronger the phonon-phonon anharmonic dispersion, leading to low lattice thermal conductivity due to its inverse relationship with the lattice conductivity $^{55}$.

To gain deeper insights into the phonon thermal transport mechanisms within each Janus monolayer, we conducted calculations for the group velocity, phonon lifetime, and Grüneisen parameter. Analyzing the group velocity depicted in Fig. 8a, we observe consistently low average values across all Janus monolayers: 0.59, 0.53, and 0.44 km/s for Janus $\gamma$-Pb₂SSe, $\gamma$-Pb₂STe, and $\gamma$-Pb₂SeTe monolayers, respectively. These values are notably lower compared to their primary phases, such as $\gamma$-PbSe$^{56}$, which boasted an average of 1.35 km/s.

The Janus $\gamma$-Pb₂SSe monolayer exhibits a distinctive trend, showing higher group velocities in acoustic modes at low frequencies and optical modes at higher frequencies, consistent with the phonon dispersion plot depicted in Fig. 2a. Additionally, we note that the group velocity of acoustic modes surpasses that of optical modes (refer to Fig. S5 in the SM), suggesting a slightly greater contribution from acoustic modes to the overall group velocity.

Understanding the role of group velocity in lattice thermal conductivity ($\kappa_l$) is crucial, given its direct correlation. Lower group velocities are imperative for achieving relatively low $\kappa_l$. However, relying solely on group velocity to understand the behavior of $\kappa_l$ across each Janus monolayer is insufficient. Hence, we further explore other parameters to gain a comprehensive understanding of the observed strong anharmonicity evident in the phonon dispersion plot shown in Fig. 2a.

In Fig. 8b, we visualize the phonon lifetime for each Janus monolayer, where optical modes at higher frequencies demonstrate longer lifetimes, contributing significantly to lattice conductivity. Generally, a low phonon lifetime indicates lower lattice thermal conductivity ($\kappa_l$), as it is inversely related to the anharmonic scattering rate ($\tau_{anh}^{-1}$). Therefore, observing an overall low phonon lifetime across all modes suggests relatively low $\kappa_l$.

Moving on to the Grüneisen parameter depicted in Fig. 8c, we note that ZA acoustic modes exhibit higher anharmonicity at lower frequencies compared to higher-frequency optical modes. This anharmonicity restricts the passage of phonons, resulting in reduced lattice thermal conductivity. Specifically, we obtained Grüneisen parameter values of 0.97, 1.40, and 1.09 for Janus $\gamma$-Pb₂SSe, $\gamma$-Pb₂STe, and $\gamma$-Pb₂SeTe monolayers, respectively. Notably, $\gamma$-Pb₂STe displays strong anharmonicity, comparable to well-known thermoelectric materials like PbTe$^{57}$ and CoSb₃$^{58}$, which possess Grüneisen parameters around $\sim1.4$ and $\sim0.95$, respectively.

All the prerequisites for achieving low lattice conductivity are evident across these factors. However, before calculating lattice thermal conductivity, we must ensure the implementation of rotational invariance conditions to obtain the out-of-plane mode (ZA) strictly quadratic near the gamma point. This requirement is addressed by applying the rotational sum methodology proposed by Born-Huang$^{30}$. Failure to implement this methodology could lead to significant alterations in the results of lattice thermal conductivity, given the sensitivity of phonon modes to even minor changes$^{59,60}$.

The computed values for $\kappa_l$ at room temperature are 0.623, 0.156, and 0.163 Wm⁻¹K⁻¹ for Janus $\gamma$-Pb₂SSe, $\gamma$-Pb₂STe, and $\gamma$-Pb₂SeTe monolayers, respectively (Fig. 8d with solid fill). These values are notably low compared to other gamma phase monolayers such as $\gamma$-GeSe$^{41,61}$ or $\gamma$-PbSe$^{10,56}$ from previous theoretical studies. The achievement of such low $\kappa_l$ values is a significant milestone in realizing high thermoelectric performance. Although we consider the quadratic ZA mode for the monolayers in this study, it is also feasible to mention that we have only considered the 3 phonon process involved because we work with the third order anharmonic interatomic forces, being influential also the fourth order anharmonic process when there is a gap between the modes of the phonons and in consequence, a more exact knowledge of phonon transports compared to three-phonon process.

![](./images/1021633078444949576_8.jpg)

Figure 8. (a) Group velocity, (b) phonon lifetime, (c) Grüneisen parameter, and (d) lattice thermal conductivity at 300 K (800 K) with solid filled (dashed) lines for Janus $\gamma$-Pb₂XY (X=S, Se; Y= Se, Te; X≠Y) monolayers.

## Thermoelectric properties
To delve into the thermoelectric properties of Janus $\gamma$-Pb₂XY (X=S, Se; Y= Se, Te; X≠Y) monolayers, we need to consider crucial parameters that indicate a material's suitability for thermoelectric applications. The figure of merit ZT, often used for this purpose, is decomposed into the power factor and the total lattice contribution (comprising electronic $\kappa_{e}$ and lattice $\kappa_{l}$ contributions), as shown in Eq. (1). In the results discussed below, we consider both $n$-type ($n<0$) and $p$-type ($n>0$) behaviors, corresponding to electrons and holes, respectively, across temperatures ranging from 300 K to 800 K, with increments of 100 K. Since BoltzTraP2 determines the electrical conductivity and electronic contribution assuming a constant relaxation time, it is essential to obtain $\tau$ as it varies for each material. In this study, we utilized the deformation potential theory to determine $\tau$, as shown in Equation 14,

$$
\tau=\frac{\mu_{2 \mathrm{D}} m^{*}}{e}, \quad(14)
$$

where the values of $\tau$ at room temperature are listed in Table 3. Moreover, the absolute values of the Seebeck coefficient for $n$-type and $p$-type carrier concentrations are shown in Fig. 9a. Notably, the Seebeck coefficient for $p$-type carriers is higher compared to $n$-type, accompanied by a reduction in the Seebeck coefficient with increasing carrier concentration. This behavior can be described by considering Mott's relationship⁶²,

$$
S=\frac{8 \pi^{2} k_{B}^{2} T}{3 e h^{2}} m^{*}\left(\frac{\pi}{3 n}\right)^{\frac{2}{3}}, \quad(15)
$$

the $m^{*}$ and $n$ values significantly influence the Seebeck coefficient, as illustrated in Table 3. For holes, the effective mass is higher compared to electrons, resulting in a higher Seebeck coefficient that decreases with increasing carrier concentrations. However, for $n$-type carriers, a slight increase in the Seebeck coefficient is observed at higher carrier concentration levels. This behavior arises from the BoltzTraP2 methodology, which operates on the rigid band approximation (RBA) and derives transport coefficients based on the band structure, including contributions from bands away from the Fermi level.

The corresponding values of $|S|$ concerning the optimal $ZT$ value at room temperature are presented in Table 4, with 247.1 (196.9), 289.9 (240.1), and 301.6 (242.1) $\mu \mathrm{VK}^{-1}$ for Janus $\gamma$-Pb₂SSe, $\gamma$-Pb₂STe, and $\gamma$-Pb₂SeTe monolayers of $p$ ($n$)-type, respectively. Particularly, the $p$-type Seebeck coefficients stand out as indicators of good thermoelectric materials, consistent with other excellent thermoelectric materials⁵⁸,⁶³.

On the other hand, the electrical conductivity exhibits a linear behavior with increasing carrier concentration, as depicted in Fig. 9b. The variation between charge carriers can be attributed to the following relationship

![](./images/1021633078444949576_9.jpg)

Figure 9. The thermoelectric properties of Janus $\gamma$-Pb₂XY (X=S, Se; Y= Se, Te; X≠Y) monolayers, focusing on three key parameters: (a) Seebeck coefficients, (b) electronic conductivity, and (c) power factor. These properties are analyzed across different temperatures and carrier concentrations ($n$) to understand the thermoelectric performance of the material comprehensively.

<table>
  <thead>
    <tr>
      <th>T</th>
      <th>Type</th>
      <th>Monolayer</th>
      <th>|S|</th>
      <th>σ</th>
      <th>PF</th>
      <th>κₑ</th>
      <th>ZT</th>
      <th>n</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="6">300</td>
      <td rowspan="3">n-type</td>
      <td>γ-Pb₂SSe</td>
      <td>196.9</td>
      <td>17612</td>
      <td>0.683</td>
      <td>0.083</td>
      <td>0.29</td>
      <td>2.6 × 10¹¹</td>
    </tr>
    <tr>
      <td>γ-Pb₂STe</td>
      <td>240.1</td>
      <td>13015</td>
      <td>0.750</td>
      <td>0.060</td>
      <td>1.04</td>
      <td>1.4 × 10¹¹</td>
    </tr>
    <tr>
      <td>γ-Pb₂SeTe</td>
      <td>242.1</td>
      <td>13351</td>
      <td>0.782</td>
      <td>0.061</td>
      <td>1.05</td>
      <td>1.2 × 10¹¹</td>
    </tr>
    <tr>
      <td rowspan="3">p-type</td>
      <td>γ-Pb₂SSe</td>
      <td>247.1</td>
      <td>63276</td>
      <td>3.863</td>
      <td>0.232</td>
      <td>1.36</td>
      <td>3.6 × 10¹²</td>
    </tr>
    <tr>
      <td>γ-Pb₂STe</td>
      <td>289.9</td>
      <td>31618</td>
      <td>2.657</td>
      <td>0.114</td>
      <td>2.96</td>
      <td>1.8 × 10¹²</td>
    </tr>
    <tr>
      <td>γ-Pb₂SeTe</td>
      <td>301.6</td>
      <td>32865</td>
      <td>2.989</td>
      <td>0.116</td>
      <td>3.22</td>
      <td>1.5 × 10¹²</td>
    </tr>
    <tr>
      <td rowspan="6">800</td>
      <td rowspan="3">n-type</td>
      <td>γ-Pb₂SSe</td>
      <td>253.8</td>
      <td>8322</td>
      <td>0.536</td>
      <td>0.107</td>
      <td>1.24</td>
      <td>3.8 × 10¹¹</td>
    </tr>
    <tr>
      <td>γ-Pb₂STe</td>
      <td>369.6</td>
      <td>5446</td>
      <td>0.744</td>
      <td>0.119</td>
      <td>2.76</td>
      <td>2.3 × 10¹¹</td>
    </tr>
    <tr>
      <td>γ-Pb₂SeTe</td>
      <td>325.8</td>
      <td>5399</td>
      <td>0.573</td>
      <td>0.099</td>
      <td>2.85</td>
      <td>1.7 × 10¹¹</td>
    </tr>
    <tr>
      <td rowspan="3">p-type</td>
      <td>γ-Pb₂SSe</td>
      <td>297.2</td>
      <td>19693</td>
      <td>1.739</td>
      <td>0.157</td>
      <td>3.52</td>
      <td>3.4 × 10¹²</td>
    </tr>
    <tr>
      <td>γ-Pb₂STe</td>
      <td>339.9</td>
      <td>10543</td>
      <td>1.218</td>
      <td>0.086</td>
      <td>5.33</td>
      <td>2.7 × 10¹²</td>
    </tr>
    <tr>
      <td>γ-Pb₂SeTe</td>
      <td>357.3</td>
      <td>9828</td>
      <td>1.255</td>
      <td>0.084</td>
      <td>6.88</td>
      <td>1.4 × 10¹²</td>
    </tr>
  </tbody>
</table>

Table 4. The calculated optimal dimensionless figure-of-merit ($ZT$) and the corresponding Seebeck coefficient $|S|$ ($\mu$VK⁻¹), electronic conductivity $\sigma$ ($\Omega$⁻¹m⁻¹), power factor $PF$ (Wm⁻¹K⁻² × 10⁻³), electronic thermal conductivity $\kappa_{e}$ (Wm⁻¹K⁻¹), and carrier concentration $n$ (cm⁻²) of $n$-type and $p$-type for Janus $\gamma$-Pb₂XY (X=S, Se; Y= Se, Te; X≠Y) monolayers at 300 and 800 K.

$$
\sigma=\frac{n e^{2} \tau}{m^{*}},\qquad(16)
$$

where a high charge carrier mobility depends on a low effective mass and higher carrier concentration. This dependency benefits $n$-type electron carriers more compared to $p$-type carriers.

Concerning the optimal $ZT$ value, the electrical conductivity at room temperature was determined for $p$ ($n$)-type, resulting in values of 63276 (17612), 31618 (13015), and 32865 (13351) $\Omega^{-1} \mathrm{m}^{-1}$ for Janus $\gamma-\mathrm{Pb}_{2} \mathrm{SSe}, \gamma-\mathrm{Pb}_{2}$ $\mathrm{STe}$, and $\gamma-\mathrm{Pb}_{2} \mathrm{SeTe}$ monolayers, respectively (see Table 4). These values indicate good electrical conductivities for both charge carriers, further supporting the thermoelectric potential of these Janus monolayers.

Furthermore, Fig. 9c depicts the power factor as a function of carrier concentration at different temperatures, providing insight into the thermoelectric performance. The power factor balances the opposing trends of the Seebeck coefficient and electrical conductivity, offering an indication of thermoelectric efficiency. It is notable that the power factor initially increases with rising carrier concentration and then decreases, a trend observed across all Janus monolayers for $p$-type carrier concentrations. However, for $n$-type carriers, two peaks are observed, corresponding to the slight increase in the Seebeck coefficient at high charge carrier concentrations. This behavior is reflected in the $n$-type power factor. Remarkably, the power factor values concerning the optimum $ZT$ value for $p(n)$ type are 3.863 (0.683), 2.657 (0.750), and 2.989 (0.782) $\mathrm{Wm}^{-1} \mathrm{K}^{-2} \times 10^{-3}$ for Janus $\gamma-\mathrm{Pb}_{2} \mathrm{SSe}, \gamma-\mathrm{Pb}_{2} \mathrm{STe}$, and $\gamma-\mathrm{Pb}_{2} \mathrm{SeTe}$ monolayers, respectively (see Table 4). These values exceed those of $\mathrm{PbTe}^{64}$, a material recognized for its excellent thermoelectric properties.

The electronic thermal contribution $(\kappa_{e})$, as shown in Fig. S6, exhibits a linear increase with increasing carrier concentration, similar to the behavior observed for electrical conductivity. This correlation can be attributed to the Wiedemann-Franz law $^{65}$, indicating that $p$-type carriers are favored due to their lower electronic contribution compared to $n$-type carriers.

The optimal values of the figure of merit $ZT$ were obtained at room temperature, with electronic contributions for $p$ ($n$)-type of 0.232 (0.083), 0.114 (0.060), and 0.116 (0.061) $\mathrm{Wm}^{-1} \mathrm{K}^{-1}$ for Janus $\gamma-\mathrm{Pb}_{2} \mathrm{SSe}, \gamma-\mathrm{Pb}_{2} \mathrm{STe}$, and $\gamma-\mathrm{Pb}_{2} \mathrm{SeTe}$ monolayers, respectively. This relatively low electronic contribution is crucial for thermoelectric applications as it influences $\kappa_{\text{Tot}}$, where $\kappa_{\text{Tot}}=\kappa_{e}+\kappa_{l}$.

Based on the high power factor and low lattice conductivity, superior thermoelectric performance is expected, which can be quantified by the figure of merit $ZT$. Figure 10 illustrates the $ZT$ values as a function of carrier concentration for $n$-type and $p$-type Janus monolayers at different temperatures. Additionally, Table 4 lists the calculated optimal $ZT$ values and their corresponding transport properties at room temperature. Clearly, the $ZT$ values for each Janus monolayer first increase and then decrease with increasing carrier concentration. For $n$-type Janus monolayers, the optimal carrier concentration ranges between $10^{10}-10^{12} \mathrm{cm}^{-2}$, while for $p$-type, it ranges between $10^{11}-10^{13} \mathrm{cm}^{-2}$, as shown in Fig. 10. At room temperature, the optimum $ZT$ values of $n$-type Janus $\gamma-\mathrm{Pb}_{2} \mathrm{SSe}, \gamma-\mathrm{Pb}_{2} \mathrm{STe}$, and $\gamma-\mathrm{Pb}_{2} \mathrm{SeTe}$ monolayers reach maximum values of 0.29, 1.04, and 1.05, respectively, with corresponding carrier concentrations of $\sim 2.6 \times 10^{11}, \sim 1.4 \times 10^{11}$, and $\sim 1.2 \times 10^{11} \mathrm{cm}^{-2}$. Similarly, the optimal $ZT$ values of $p$-type Janus monolayers are 1.36, 2.96, and 3.22, with carrier concentrations of $\sim 3.6 \times$ $10^{12}, \sim 1.8 \times 10^{12}$, and $\sim 1.5 \times 10^{12} \mathrm{cm}^{-2}$, respectively. Upon reaching 800 K, the optimum $ZT$ values for Janus $\gamma$ -$\mathrm{Pb}_{2} \mathrm{SSe}, \gamma-\mathrm{Pb}_{2} \mathrm{STe}$, and $\gamma-\mathrm{Pb}_{2} \mathrm{SeTe}$ monolayers for $p$ ($n$)-type are 3.52 (1.24), 5.33 (2.76), and 6.88 (2.85) at carrier concentrations of $3.4 \times 10^{12}$ ($3.8 \times 10^{11}$), $2.7 \times 10^{12}$ ($2.3 \times 10^{11}$), and $1.4 \times 10^{12}$ ($1.7 \times 10^{11}$) $\mathrm{cm}^{-2}$, respectively.

![](./images/1021633078444949576_10.jpg)

Figure 10. The figure of merit (ZT) as a function of carrier concentration for Janus $\gamma-\mathrm{Pb}_{2} \mathrm{XY}$ (X=S, Se; Y= Se, Te; X≠Y) monolayers.

showcasing excellent $p$-type thermoelectric performance across all Janus monolayers. These results are higher than those obtained by Ji et al.¹⁰ without Janus, where they obtained a maximum ZT of 2.45 and higher than other gamma-phase monolayers⁹⁴²56,66,67. Nevertheless, it is necessary to note that the thermoelectric properties have been obtained using the PBE functionals without consideration of SOC (BoltzTraP2 does not support SOC in QE), which may alter the thermoelectric properties of some monolayers⁶⁸⁻⁷⁰.

## Conclusions
Based on the density functional and deformation potential theories, as well as the Boltzmann transport equation, we have theoretically studied the structural, electronic, transport, phonon, and thermoelectric properties of Janus $\gamma$-Pb₂XY (X=S, Se; Y= Se, Te; X≠Y) monolayers. We have confirmed the energetic, dynamic, thermal, and mechanical stability of Janus monolayer by applying the Born stability criterion to analyze the cohesion energy, phonon dispersion, and molecular dynamics. We have found that: (i) The electron mobility of these Janus monolayers is isotropic and ranges from 264.18 to 461.42 cm²V⁻¹s⁻¹, which makes them suitable for the development of nanoelectronic devices. (ii) The high phonon dispersion rates of Janus $\gamma$-Pb₂SSe, $\gamma$-Pb₂STe, and $\gamma$-Pb₂SeTe monolayers at room temperature lead to low lattice thermal conductivities of 0.623, 0.156, and 0.163 Wm⁻¹K⁻¹, respectively. (iii) A figure of merit ZT as high as 3.52, 5.33, and 6.88 were determined for p-type carriers. The obtained results thus show the great potential of Janus $\gamma$-Pb₂XY (X=S, Se; Y= Se, Te; X≠Y) monolayers for thermoelectric applications.

## Data availability
All data relevant to this study are presented in the manuscript, and its supplementary information files. Any remaining questions or requests for additional details regarding the datasets should be directed to the corresponding author.

Received: 9 May 2024; Accepted: 8 July 2024
Published online: 19 July 2024

## References
1. Zhang, X., Chen, A., Chen, L. & Zhou, Z. 2D materials bridging experiments and computations for electro/photocatalysis. *Adv. Energy Mater.* 12, 2003841 (2022).
2. Zha, J. *et al.* Infrared photodetectors based on 2D materials and nanophotonics. *Adv. Funct. Mater.* 32, 2111970 (2022).
3. Zhang, X. *et al.* Ultrasensitive field-effect biosensors enabled by the unique electronic properties of graphene. *Small* 16, 1902820 (2020).
4. Wang, Y., Xu, Y., Hu, M., Ling, H. & Zhu, X. MXenes: Focus on optical and electronic properties and corresponding applications. *Nanophotonics* 9, 1601–1620 (2020).
5. Wang, L. *et al.* 2D photovoltaic devices: Progress and prospects. *Small Methods* 2, 1700294 (2018).
6. Yang, W., Gan, L., Li, H. & Zhai, T. Two-dimensional layered nanomaterials for gas-sensing applications. *Inorg. Chem. Front.* 3, 433–451 (2016).
7. Pu, J. *et al.* Enhanced thermoelectric power in two-dimensional transition metal dichalcogenide monolayers. *Phys. Rev. B* 94, 014312 (2016).
8. Lee, S. *et al.* $\gamma$-GeSe: A new hexagonal polymorph from group IV-VI monochalcogenides. *Nano Lett.* 21, 4305–4313 (2021).
9. Dong, B. *et al.* New two-dimensional phase of tin chalcogenides: Candidates for high-performance thermoelectric materials. *Phys. Rev. Mater.* 3, 013405 (2019).
10. Jia, P.-Z. *et al.* High thermoelectric performance induced by strong anharmonic effects in monolayer (PbX)₂ (X= S, Se, Te). *Appl. Phys. Lett.*121 (2022).
11. Zhang, J. *et al.* Janus monolayer transition-metal dichalcogenides. *ACS Nano* 11, 8192–8198 (2017).
12. Lu, A.-Y. *et al.* Janus monolayers of transition metal dichalcogenides. *Nat. Nanotechnol.* 12, 744–749 (2017).
13. Wu, C.-W. *et al.* Significant regulation of stress on the contribution of optical phonons to thermal conductivity in layered Li₂ZrCl₆: First-principles calculations combined with the machine-learning potential approach. *Appl. Phys. Lett.*121 (2022).
14. Tang, S. *et al.* Improving thermoelectric performance of asymmetrical Janus 1T-SnSSe monolayer by the synergistic effect of band convergence and crystal lattice softening under strain engineering. *Mater. Today Phys.* 29, 100923 (2022).
15. Bai, S. *et al.* Unravelling the thermoelectric properties and suppression of bipolar effect under strain engineering for the asymmetric Janus SnSSe and PbSSe monolayers. *Appl. Surf. Sci.* 599, 153962 (2022).
16. Zhou, W.-X. *et al.* Thermal conductivity of amorphous materials. *Adv. Funct. Mater.* 30, 1903829 (2020).
17. Lin, S. & Buehler, M. J. Thermal transport in monolayer graphene oxide: Atomistic insights into phonon engineering through surface chemistry. *Carbon* 77, 351–359 (2014).
18. Ding, Z., Pei, Q.-X., Jiang, J.-W. & Zhang, Y.-W. Manipulating the thermal conductivity of monolayer MoS₂ via lattice defect and strain engineering. *J. Phys. Chem. C* 119, 16358–16365 (2015).
19. Chen, X.-K., Zhang, E.-M., Wu, D. & Chen, K.-Q. Strain-induced medium-temperature thermoelectric performance of Cu₄TiSe₄: The role of four-phonon scattering. *Phys. Rev. Appl.* 19, 044052 (2023).
20. Nishino, Y., Deguchi, S. & Mizutani, U. Thermal and transport properties of the Heusler-type Fe₂VAl₁₋ₓGeₓ (0≤x≤0.20) alloys: Effect of doping on lattice thermal conductivity, electrical resistivity, and seebeck coefficient. *Phys. Rev. B* 74, 115115 (2006).
21. Xing, T. *et al.* Ultralow lattice thermal conductivity and superhigh thermoelectric figure-of-merit in (Mg, Bi) co-doped GeTe. *Adv. Mater.* 33, 2008773 (2021).
22. Yin, Y., Baskaran, K. & Tiwari, A. A review of strategies for developing promising thermoelectric materials by controlling thermal conduction. *Physica Status Solidi (a)* 216, 1800904 (2019).
23. Giannozzi, P. *et al.* QUANTUM ESPRESSO: A modular and open-source software project for quantum simulations of materials. *J. Phys. Condens. Matter* 21, 395502 (2009).
24. Blöchl, P. E. Projector augmented-wave method. *Phys. Rev. B* 50, 17953 (1994).
25. Ernzerhof, M. & Scuseria, G. E. Assessment of the Perdew-Burke-Ernzerhof exchange-correlation functional. *J. Chem. Phys.* 110, 5029–5036 (1999).
26. Heyd, J., Scuseria, G. E. & Ernzerhof, M. Hybrid functionals based on a screened Coulomb potential. *J. Chem. Phys.* 118, 8207–8215 (2003).
27. Moellmann, J. & Grimme, S. DFT-D3 study of some molecular crystals. *J. Phys. Chem. C* 118, 7615–7621 (2014).
28. Togo, A. & Tanaka, I. First principles phonon calculations in materials science. *Scripta Mater.* 108, 1–5 (2015).

29. Eriksson, E., Fransson, E. & Erhart, P. The Hiphive Package for the extraction of high-order force constants by machine learning. Adv. Theory Simul. 2, 1800184 (2019).
30. Born, M. & Huang, K. Dynamical Theory of Crystal Lattices (Oxford University Press, 1996).
31. Thomas, S., Ajith, K. & Valsakumar, M. Directional anisotropy, finite size effect and elastic properties of hexagonal boron nitride. J. Phys. Condens. Matter 28, 295302 (2016).
32. Bardeen, J. & Shockley, W. Deformation potentials and mobilities in non-polar crystals. Phys. Rev. 80, 72 (1950).
33. Hafner, J. Ab-initio simulations of materials using VASP: Density-functional theory and beyond. J. Comput. Chem. 29, 2044–2078 (2008).
34. Madsen, G. K., Carrete, J. & Verstraete, M. J. BoltzTraP2, a program for interpolating band structures and calculating semi-classical transport coefficients. Comput. Phys. Commun. 231, 140–145 (2018).
35. Togo, A., Chaput, L., Tadano, T. & Tanaka, I. Implementation strategies in Phonopy and Phono3py. J. Phys. Condensed Matter 35, 353001 (2023).
36. Chaput, L. Direct solution to the linearized phonon Boltzmann equation. Phys. Rev. Lett. 110, 265506 (2013).
37. Seixas, L. Janus two-dimensional materials based on group IV monochalcogenides. J. Appl. Phys.128 (2020).
38. Hiep, N. T., Nguyen, C. Q. & Hieu, N. N. Negative Poisson's ratio and anisotropic carrier mobility in ternary Janus Si₂XY (X/Y= S, Se, Te): First-principles prediction. Appl. Phys. Lett.123 (2023).
39. Wang, Z., Yan, X., Liu, Y. & Yang, G. Piezoelectric response and ferromagnetic order in 2D Janus FeGeN₃. Appl. Phys. Lett.124 (2024).
40. Vu, T. V., Phuc, H. V., Kartamyshev, A. & Hieu, N. N. Enhanced out-of-plane piezoelectricity and carrier mobility in Janus γ-Sn₂XY (X/Y= S, Se, Te) monolayers: A first-principles prediction. Applied Physics Letters122 (2023).
41. Nair, S. S., Sajjad, M., Biswas, K. & Singh, N. Metavalent bonding induced phonon transport anomaly in 2D γ-MX (M= Ge, Sn, Pb; X= S, Se, Te) Monolayers. ACS Appl. Energy Mater. 6, 8787–8793 (2023).
42. Thanh, V. V., Truong, D. V. & Tuan Hung, N. Janus γ-Ge₂SSe monolayer as a high-performance material for photocatalysis and thermoelectricity. ACS Appl. Energy Mater. 6, 910–919 (2023).
43. Mażdziarz, M. Comment on ‘The Computational 2D Materials Database: High-throughput modeling and discovery of atomically thin crystals'. 2D Mater. 6, 048001 (2019).
44. Tuan, V. V. et al. Mexican-hat dispersions and high carrier mobility of γ-SnX (X= O, S, Se, Te) single-layers: A first-principles investigation. Phys. Chem. Chem. Phys. 24, 29064–29073 (2022).
45. Vu, T. V., Phuc, H. V., Nhan, L. C., Kartamyshev, A. & Hieu, N. N. Predicted novel Janus γ-Ge₂XY (S, Se, Te) monolayers with Mexican-hat dispersions and high carrier mobilities. J. Phys. D Appl. Phys. 56, 135302 (2023).
46. Vu, T. V., Anh, N. P., Phuc, H. V., Kartamyshev, A. & Hieu, N. N. Strong out-of-plane piezoelectricity and Rashba-type spin split- ting in asymmetric structures: first-principles study for Janus γ-Sn₂OX (X= S, Se, Te) monolayers. New J. Chem. 47, 11660–11668 (2023).
47. Luo, N., Duan, W., Yakobson, B. I. & Zou, X. Excitons and Electron-Hole Liquid State in 2D γ-Phase Group-IV Monochalcogenides. Adv. Func. Mater. 30, 2000533 (2020).
48. Xue, X.-X. et al. Strain tuning of electronic properties of various dimension elemental tellurium with broken screw symmetry. J. Phys. Condens. Matter 30, 125001 (2018).
49. Van Thanh, V. et al. Effects of strain and electric field on electronic and optical properties of monolayer γ-GeX (X= S, Se and Te). Appl. Surf. Sci. 582, 152321 (2022).
50. Chovvadiya, D., Pillai, S. B., Chakraborty, B. & Jha, P. K. Strain effect on Mexican-hat dispersion and electronic band gap of 2D α -CN. AIP Conf. Proc.2265 (2020).
51. Alavi-Rad, H. Strain engineering in optoelectronic properties of MoSi₂N₂ monolayer: ultrahigh tunability. Semicond. Sci. Technol. 37, 065018 (2022).
52. Lang, H., Zhang, S. & Liu, Z. Mobility anisotropy of two-dimensional semiconductors. Phys. Rev. B 94, 235306 (2016).
53. Radisavljevic, B., Radenovic, A., Brivio, J., Giacometti, V. & Kis, A. Single-layer MoS₂ transistors. Nat. Nanotechnol. 6, 147–150 (2011).
54. Chaput, L., Togo, A., Tanaka, I. & Hug, G. Phonon-phonon interactions in transition metals. Phys. Rev. B 84, 094302 (2011).
55. Lee, C. H. & Gan, C. K. Anharmonic interatomic force constants and thermal conductivity from Grüneisen parameters: An application to graphene. Phys. Rev. B 96, 035105 (2017).
56. Zhu, X.-L. et al. High thermoelectric performance of new two-dimensional IV-VI compounds: A first-principles study. J. Phys. Chem. C 124, 1812–1819 (2019).
57. Morelli, D., Jovovic, V. & Heremans, J. Intrinsically minimal thermal conductivity in cubic I-V-VI₂ semiconductors. Phys. Rev. Lett. 101, 035901 (2008).
58. Caillat, T., Borshchevsky, A. & Fleurial, J.-P. Properties of single crystalline semiconducting CoSb₃. J. Appl. Phys. 80, 4442–4449 (1996).
59. Carrete, J. et al. Physically founded phonon dispersions of few-layer materials and the case of borophene. Mater. Res. Lett. 4, 204–211 (2016).
60. Taheri, A., Pisana, S. & Singh, C. V. Importance of quadratic dispersion in acoustic flexural phonons for thermal transport of two-dimensional materials. Phys. Rev. B 103, 235426 (2021).
61. Fan, Q. et al. Understanding intrinsic phonon thermal transport in two-dimensional γ-GeX (X= S, Se, Te) from first principles. Results Phys. 49, 106528 (2023).
62. Wang, N., Li, M., Xiao, H., Zu, X. & Qiao, L. Layered LaCuOSe: A promising anisotropic thermoelectric material. Phys. Rev. Appl. 13, 024038 (2020).
63. Martin, J., Wang, L., Chen, L. & Nolas, G. Enhanced seebeck coefficient through energy-barrier scattering in PbTe nanocomposites. Phys. Rev. B 79, 115311 (2009).
64. Sootsman, J. R. et al. Large enhancements in the thermoelectric power factor of bulk PbTe at high temperature by synergistic nanostructuring. Angewandte Chemie-Int. Edn. 47, 8618–8622 (2008).
65. Jonson, M. & Mahan, G. Mott's formula for the thermopower and the Wiedemann-Franz law. Phys. Rev. B 21, 4223 (1980).
66. Shu, Z. et al. High-performance thermoelectric monolayer γ-GeSe and its group-IV monochalcogenide isostructural family. Chem. Eng. J. 454, 140242 (2023).
67. Ding, C. et al. High thermoelectric performance of a novel γ-PbSnX₂ (X= S, Se, Te) Monolayer: Predicted using first principles. Nanomaterials 13, 1519 (2023).
68. Li, G., Ding, G. & Gao, G. Thermoelectric properties of SnSe₂ monolayer. J. Phys. Condens. Matter 29, 015001 (2016).
69. Guo, S.-D. & Wang, J.-L. Spin-orbital coupling effect on the power factor in semiconducting transition-metal dichalcogenide monolayers. Semicond. Sci. Technol. 31, 095011 (2016).
70. Guo, S.-D. Spin-orbit and strain effect on power factor in monolayer MoS₂. Comput. Mater. Sci. 123, 8–13 (2016).

## Acknowledgements
We extend our heartfelt gratitude to the Universidad Nacional Jorge Basadre Grohmann for its unwavering support to the project *"Development of new thermoelectric materials for energy conversion: A theoretical and

experimental approach", approved by Rectoral Resolution No 11174-2023-UNJBG. We would also acknowledge the support received from the Brazilian agencies Rio Grande do Sul Research Foundation (FAPERGS) and Sao Paulo Research Foundation (FAPESP) under grants no 2013/07296-2, 2019/08928-9, 2020/01144-0, and 2022/03959-6, as well as the National Council for Scientific and Technological Development (CNPq), under grants no 307213/2021-8 and 307345/2021-1. Their invaluable support played a crucial role in facilitating the successful execution of this research.

## Author contributions
E.M.F. and V.J.R.R. conceived the computational study and performed the DFT calculations. J.O.M. and F.M.G. analyzed the results and interpreted the data. M.J.P., M.L.M and J.R.S. provided guidance and supervision. E.M.F. coordinated the research project. All authors contributed to writing and reviewing the manuscript.

## Funding
This research was financially supported by the Universidad Nacional Jorge Basadre Grohmann, through the program "Fondos del canon, sobrecanon y regalías mineras" approved by Rectoral Resolution NÂ° 11174-2023-UNJBG.

## Competing interests
The authors declare no competing interests.

## Additional information
Supplementary Information The online version contains supplementary material available at https://doi.org/10.1038/s41598-024-67039-0.

Correspondence and requests for materials should be addressed to E.M.F.

Reprints and permissions information is available at www.nature.com/reprints.

Publisher's note Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

![](./images/1021633078444949576_11.jpg)
Open Access This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if changes were made. The images or other third party material in this article are included in the article's Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article's Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit http://creativecommons.org/licenses/by/4.0/.

© The Author(s) 2024