Nanoscale

Accepted Manuscript

This article can be cited before page numbers have been issued, to do this please use: X. Wang, J. Zhang, Y. Chen and P. K. L. Chan, Nanoscale, 2017, DOI: 10.1039/C6NR08682A.

![](./images/811088260200660993_1.jpg)

This is an Accepted Manuscript, which has been through the Royal Society of Chemistry peer review process and has been accepted for publication.

Accepted Manuscripts are published online shortly after acceptance, before technical editing, formatting and proof reading. Using this free service, authors can make their results available to the community, in citable form, before we publish the edited article. We will replace this Accepted Manuscript with the edited and formatted Advance Article as soon as it is available.

You can find more information about Accepted Manuscripts in the author guidelines.

Please note that technical editing may introduce minor changes to the text and/or graphics, which may alter content. The journal's standard Terms & Conditions and the ethical guidelines, outlined in our author and reviewer resource centre, still apply. In no event shall the Royal Society of Chemistry be held responsible for any errors or omissions in this Accepted Manuscript or any consequences arising from the use of any information it contains.

![](./images/811088260200660993_2.jpg)

rsc.li/nanoscale

# Nanoscale

PAPER

Received 00th January 20xx,
Accepted 00th January 20xx

DOI: 10.1039/x0xx00000x

www.rsc.org/

## Molecular dynamics study of thermal transport in dinaphtho[2,3-b:2',3'-f]thieno[3,2-b]thiophene (DNTT) organic semiconductor

Xinyu Wang, $^{a}$ Jingchao Zhang, $^{b}$ Yue Chen $^{* a}$ and Paddy K. L. Chan $^{* a}$

The thermal transport in a high-mobility and air-stable small molecule organic semiconductor, dinaphtho[2,3-b:2',3'-f]thieno[3,2-b]thiophene (DNTT), is simulated by using non-equilibrium molecular dynamics. We find that the thermal conductivity of DNTT has a strong dependence on crystal size and orientation directions $(a^{\star}, b^{\star}$ and $c^{\star})$. The bulk thermal conductivities of DNTT along the $a^{\star}, b^{\star}$ and $c^{\star}$ directions are 0.73, 0.33 and 0.95 W/m-K, respectively. The polycrystalline nature of the DNTT thin film in the experiment means that it is essential to consider effects of thermal boundary resistance (TBR) and vacancy on the thermal conductivity. The TBR across different interfaces are calculated as 7.00±0.26, 6.15±0.13 and 3.20±0.09 ×10⁹ m²-K/W for the $a^{\star}-b^{\star}$, $a^{\star}-c^{\star}$ and $b^{\star}-c^{\star}$ interfaces, respectively. On the other hand, the thermal conductivities of DNTT with a vacancy concentration of 6% can be reduced 44%, 33% and 35% in the $a^{\star}, b^{\star}$ and $c^{\star}$ directions. Our findings indicate that the boundary and defect scatterings of phonons have significant effects on the thermal conductivity of organic semiconductors. This work contributes with fundamental knowledge to control the thermal property of organic semiconductors in organic electronic devices.

## Introduction

The rapid development of organic electronic devices has very much attracted the attention of the research community and electronic industry. The active layer of organic electronic devices is mainly constructed from polymer or small molecules. The polymer materials are usually deposited by using a solution method, while the small molecules have greater flexibility in terms of processing methods, so that different approaches, such as vapor phase deposition, solution shearing or thermal evaporation, can be used for device fabrication. In these small molecule devices, the molecular alignment, grain boundary density and crystallinity of the organic semiconductors can be moderated by carefully controlling the deposition parameters. $^{1-5}$ For example, Niazi *et al.* demonstrated that the morphology of organic crystal and the carrier mobility can be controlled with the polystyrene content in the solution blend or the solvents used for the deposition in organic field effect transistors (OFETs) based on 2,8-difluoro-5,11-bis(triethylsilylethynyl) anthradithiophene (diF-TES-ADT). $^{4}$ Similarly, Yang *et al.* demonstrated that different substrate deposition temperatures can be utilized to modify the grain size of pentacene, which has significant effects on the carrier mobility. $^{5}$

Recently, a promising small molecule organic semiconductor, dinaphtho[2,3-b:2',3'-f]thieno[3,2-b]thiophene (DNTT), has not only demonstrated high field effect mobility (larger than 1 cm²/V-s), but also shows excellent ambient air stability and more importantly, extremely good thermal stability up to 120 °C in air.⁶ Since thin films with good mobility are developed by using thermal evaporation where the effects from the grain boundary, impurities and defects are still present,⁷ ⁸ the carrier mobility can be further improved to 9.9 cm²/V-s in DNTT single crystals fabricated by vapor phase deposition.⁹ Compared with the electrical properties, the characterization of the thermal properties of high performance organic semiconductors has been very limited.¹⁰ Although temperature dependence on carrier mobility is generally adapted to deviate the band-like or hopping transport of carriers, the main heat transport parameter, that is, the thermal conductivity ($k$) of these organic materials, has been rarely reported. As opposed to laboratory scale devices, when a large number of DNTT OFETs are integrated together for practical applications, such as computational chips or logic circuits, there is generation of wasted heat and the corresponding thermal management would have a critical role in the overall performance and durability of the device, but these are generally ignored. Chung *et al.* reported that highly thermally conductive substrates would provide efficient heat dissipation in organic light-emitting diodes (OLEDs) which could reduce the device temperature increase and improve OLED lifetime.¹¹ To overcome this potential bottleneck in practical applications, a model that can evaluate the thermal conductivity of small molecule materials and quantify the effects of the interface boundaries or defects is essential. Actually, similar to the charge carrier transport, phonon transport is also significantly affected by the crystal boundaries and defects. Previously, Wang *et al.* investigated the effects of isotopic substitutions and vacancies on the thermal conductivity of pentacene by using molecular dynamics (MD) simulations.¹² They observed that the isotopic substitution of C only has a slight effect on the thermal conductivity while the vacancy in

---
$^{a}$ Department of Mechanical Engineering, The University of Hong Kong, Hong Kong.
$^{b}$ Holland Computing Center, University of Nebraska-Lincoln, Lincoln, NE 68588, USA.
$^{*}$ Corresponding authors. E-mail: pklc@hku.hk (Paddy K. L. Chan) and yuechen@hku.hk (Yue Chen).
† Electronic Supplementary Information (ESI) available. See DOI: 10.1039/x0xx00000x

---

This journal is © The Royal Society of Chemistry 2016
Nanoscale, 2016, **00**, 1-9 | 1

Paper

the structure could cause a significant reduction in the thermal conductivity.

In the current work, we apply non-equilibrium molecular dynamics (NEMD) to simulate the thermal transport of DNTT crystals. We first investigate the dependence of the thermal conductivity of DNTT on the crystal size and orientation, and extract the bulk thermal conductivity and average phonon mean free path (MFP) along different directions. After that, the temperature dependence of the thermal conductivity is examined from 100 K to 600 K. We have also developed different crystal boundaries in the orientation of the DNTT crystals to determine the thermal boundary resistance (TBR) under different directions. The phonon density of state (DOS) is evaluated to gain a better understanding of the MD simulation results on the TBR. Finally, the effect of crystal defects on thermal conductivity is investigated with a vacancy concentration ranging from 0% to 6%. The vacancy effect on the thermal conductivity of the DNTT crystals is also compared with the experimental value which is measured by using the differential 3-ω method.

## Simulation models
MD simulation is a key technique used to predict the properties of materials and obtain insight into the underlying physics of materials. Many investigations on thermal transport have been conducted by using MD simulation. $^{12-16}$ Therefore, MD simulation is used in this study, of which all are performed with the Large-scale Atomic/Molecular Massively Parallel Simulator (LAMMPS) package. $^{17}$ The thermal conductivities of DNTT along the different crystal directions were calculated by using the NEMD approach. $^{12,18,}$ $^{19}$ The model is shown in Fig. 1(a), and it can be observed that kinetic energy is added and subtracted in the heat source and heat sink regions of the simulation system, so that the heat flux and temperature gradient along the simulation direction are created. After the system arrives at the steady state, the constant heat flux and temperature gradient can be used to fit the thermal conductivity by using Fourier's law:

$$
J=-k\nabla T \tag{1}
$$

where $J$ is the heat flux, $k$ is the thermal conductivity, and $T$ is the temperature.

Many types of force fields, including assisted model building with energy refinement (AMBER), $^{20-22}$ consistent-valence forcefield (CVFF), $^{23}$ condensed-phase optimized molecular potentials for atomistic simulation studies (COMPASS), $^{14,24,25}$ and general AMBER force field (GAFF), $^{26}$ have been developed to model the atomic interactions for predicting the structure and properties of organic materials. In previous MD studies of small molecule organic semiconductors, $^{12,27,28}$ GAFF has been adopted to account for the intermolecular and intramolecular interactions of organic molecules. $^{26}$ Here, we use GAFF to describe the bond, angle, dihedral, van der Waals and electrostatic interactions in the DNTT molecules. The details of the GAFF parameters used in the simulation are shown in the ESI†. The development of the DNTT simulation box was based on the DNTT structure reported by Yamamoto and Takimiya, $^{29}$ in which the unit cell of DNTT is monoclinic (see Fig. 1(b)) and the corresponding parameters of the unit cell are as follows: $a$: 6.187 Å, $b$: 7.662 Å, $c$: 16.208 Å, $\alpha$: 90°, $\beta$: 92.49°, and $\gamma$: 90°. The simulation box was divided into 20-30 slabs parallel to the box face along the heat transport direction. Due to the monoclinic property of DNTT crystals, the simulation box is also monoclinic, so that the heat flux is along the normal direction of the box face rather than the real crystal direction, $a$, $b$, or $c$. We denoted the three actual heat transport directions of the simulation box as $a^{*}$, $b^{*}$ and $c^{*}$ (see Fig. S1 in the ESI†).

As shown in Fig. 1(a), the periodic boundary condition along all

![](./images/811088260200660993_3.jpg)

Fig. 1 (a) Schematic illustration of typical NEMD process. Rectangular boxes represent heat source and sink regions. (b) Crystal structure of DNTT used in simulation. (c) Typical temperature distribution along the heat flux direction. Red solid lines denote linear regions for fitting thermal conductivity.

of the crystal directions is developed by locating the heat source slab at the middle of the simulation box and two heat sink slabs at the two ends of the simulation box. The time step is chosen to be 0.5 fs in all of our MD simulations. The following is a summary of the simulation process. The initial DNTT system was first thermalized in a NVT ensemble (i.e., constant mass, volume, and temperature) for 0.5 ns at the specified temperature. Subsequently, a NVE (i.e., constant mass, volume, and energy) ensemble was performed on the system for another 0.5 ns until equilibrium. When the system arrived at the NVE equilibrium, thermal energy was inputted into the heat source slab for every two-time steps by scaling the velocities of the atoms and consequently the same amount of energy was outputted at the two heat sink slabs for 6 ns to perform NEMD simulation where the total energy of the system was conserved. By exporting the temperature variations of each system slab during the NEMD, it could be confirmed that the system had reached the steady state after the 6 ns of the NEMD and a steady temperature difference (around 100-200 K) between the heat source and sink was obtained. The data were collected during the following 2.5 ns which was divided into five time blocks (0.5 ns) after the steady state was reached. The temperature profile of the system, obtained by averaging the temperature of each slab during each time block, is shown in Fig. 1(c) and the linear region of the temperature profile is used to fit the $k$ values. The final values were calculated by averaging the five time blocks with the error bar as the standard deviation. It is worth noting that the classical MD simulation does not take quantum effects into consideration. Thus quantum correction is needed to modify the simulation temperature when it is lower than the Debye temperature. Previous work has indicated that the Debye temperature of many organic materials is below $100\ \text{K}$, $^{30,31}$ such as, 68.3 K for acridinium ditetracyanoquinodimethanide, $^{30}$ whereas the simulation temperature in our work is varied from 100 K to 600 K. Hence no quantum correction is needed to rectify the thermal conductivity calculation. Additionally, the electron contribution to the thermal conductivity is also neglected due to the small carrier concentration in this organic material.

The phonon DOS is a quantitative value that indicates the phonon modes of the system which reveal the thermal energy transport physics of materials. To interpret the TBR results of DNTT, we further calculated the phonon DOS by taking the Fourier transform of the velocity autocorrelation function (VACF): $^{32}$

$$
F(\omega)=\frac{1}{\sqrt{2 \pi}} \int_{-\infty}^{\infty} e^{i \omega t} \frac{\langle\boldsymbol{v}(t) \cdot \boldsymbol{v}(0)\rangle}{\langle\boldsymbol{v}(0) \cdot \boldsymbol{v}(0)\rangle} d t \tag{2}
$$

where $F(\omega)$ denotes the phonon DOS at frequency $\omega$, and $\boldsymbol{v}(t)$ and $\boldsymbol{v}(0)$ are atom velocity vectors at $t$ time and zero time, respectively. The value of $F(\omega)$ denotes the number of phonon modes at frequency $\omega$. Since phonon DOS is material and structure dependent, the extent of the overlap in the phonon DOS between two different materials indicates the capacity of the interfacial thermal transport between them. To quantify the extent of the overlap in the phonon DOS, the overlapping factor of phonon DOS $(S)$ is calculated by: $^{33,34}$

$$
S=\frac{\int_{0}^{\infty} F_{1}(\omega) F_{2}(\omega) d \omega}{\int_{0}^{\infty} F_{1}(\omega) d \omega \cdot \int_{0}^{\infty} F_{2}(\omega) d \omega} \tag{3}
$$

where subscripts "1" and "2" represent different materials.

# Results and discussion
## Effects of crystal size and orientation
To understand the dependence of crystal size and orientation of the thermal conductivity of DNTT along different principle axes, we built the DNTT crystal box with different lengths along the $a^{*}, b^{*}$ and $c^{*}$ directions. Generally, when the system size is larger than the phonon MFP, the phonon propagation in the system can be considered as diffusive. On the other hand, for systems with dimensions smaller than or close to the phonon MFP, the phonon transports ballistically through the system with scattering at the boundaries. $^{18}$ The cross-section of the simulation boxes normal to the heat transport direction was configured with $4 \times 4$ unit cells. Along the heat transport direction, the super cells of DNTT contained 10-100 unit cells for the $a^{*}$ and $b^{*}$ directions and 10-64 unit cells for the $c^{*}$ direction. As shown in Fig. 1(a), since our simulation structure is symmetric, the crystal length $(L)$ is equal to half of that of the simulation box $(L_{box})$. The equilibrium temperature of NVT during the simulation is 300 K.

Fig. 2(a) shows the thermal conductivity dependence on crystal size and orientation of the DNTT crystals at 300 K. Our simulation results indicate that the thermal conductivity of DNTT is strongly dependent on the crystal size and direction. When the crystal length increases, the thermal conductivity shows an increasing trend, which is attributed to the weaker phonon boundary scattering and more phonons with a long MFP that are involved in the thermal transport. To evaluate the bulk thermal conductivity and phonon MFP of DNTT, we applied the thermal conductivity solution of the Boltzmann transport equation with Fourier's law and combined Matthiessen's rule to extrapolate the MD results. Based on gray approximation, the thermal conductivity of the bulk crystals in the $i$ direction can be formulated $(k_{bulk,i})$ as follows: $^{19,35-37}$

$$
k_{b u l k, i}=C v_{i} l_{b u l k, i} \tag{4}
$$

where subscript $i$ is the phonon transport direction ($i=a^{*}, b^{*}$ or $c^{*}$). $C$ is the volumetric specific heat capacity, $v_{i}$ is the average phonon velocity in the $i$ direction over all phonon modes, and $l_{bulk,i}$ is the average bulk phonon MFP in the $i$ direction over all phonon modes. As mentioned earlier, when the material size is reduced to the nanoscale, the phonon MFP will suffer from the effects of phonon boundary scattering and the effective phonon MFPs of the nanostructure material $(l_{nano,i})$ can be obtained from using Matthiessen's rule with the assumption that the different phonon scatterings are independent:

$$
\frac{1}{l_{\text {nano }, i}}=\frac{1}{l_{\text {bulk }, i}}+\frac{1}{L} \tag{5}
$$

By combining Eqs. (4) and (5), the thermal conductivity of the nanostructure material $(k_{nano,i})$ in the $i$ direction can be expressed as:

$$
\frac{1}{k_{\text {nano }, i}}=\frac{1}{C v_{i}}\left(\frac{1}{l_{\text {bulk }, i}}+\frac{1}{L}\right)=\frac{1}{k_{\text {bulk }, i}}+\frac{1}{C v_{i}} \cdot \frac{1}{L} \tag{6}
$$

We re-plot the dependence of the thermal conductivity on crystal size and orientation in the form $(1/k$ vs $1/L)$ as shown in Fig. 2(b). By performing the extrapolation, the bulk thermal conductivities of DNTT along the $a^{*}, b^{*}$ and $c^{*}$ directions are obtained: 0.73, 0.33 and 0.95 W/m-K, respectively. The corresponding thermal anisotropy factors of $a^{*}/b^{*}, a^{*}/c^{*}$ and $c^{*}/b^{*}$ are 2.21, 0.77 and 2.88. At the same

![](./images/811088260200660993_4.jpg)

Fig. 2 (a) Thermal conductivities (k) of DNTT at different lengths (L) along $a^{*}$, $b^{*}$ and $c^{*}$ directions at 300 K. Black square, red dot and blue triangle represent MD simulation results along $a^{*}$, $b^{*}$ and $c^{*}$ directions, respectively. Green reverted triangle represents previous experimental result measured by using differential 3-ω method. (b) Relations between $1/k$ and $1/L$ along $a^{*}$, $b^{*}$ and $c^{*}$ directions. Solid lines denote linear fittings between $1/k$ and $1/L$ along $a^{*}$, $b^{*}$ and $c^{*}$ directions.

time, the average phonon MFP of the $a^{*}$, $b^{*}$ and $c^{*}$ directions can also be extracted as 13.8, 9.5 and 8.4 nm. From Fig. 2(b), it can be observed that the slope of the extrapolation lines of the $a^{*}$, $b^{*}$ and $c^{*}$ directions ($1/Cv$ in Eq. (6)) is $b^{*} > a^{*} > c^{*}$. Assuming that the volumetric specific heat capacity (C) is independent of the crystal orientation direction, the relation of the average phonon velocity is $c^{*} > a^{*} > b^{*}$. The primary reason for $k_{bulk,a^{*}} > k_{bulk,b^{*}}$ is attributed to the fact that phonon MFP and the velocity along $a^{*}$ are larger than those along $b^{*}$. However, even though the phonon MFP of the $c^{*}$ direction is slightly smaller than that of the $b^{*}$ direction, as the phonon velocity along the $c^{*}$ direction is approximately 3 times that along the $b^{*}$ direction, the thermal conductivity along the $c^{*}$ direction is 2.88 times the value of that along the $b^{*}$ direction.

In our previous experimental work on DNTT thin films by using the differential 3-ω method, $^{38}$ the measured cross-plane ($c^{*}$ direction) thermal conductivity of DNTT thin film with a thickness of 50 nm is 0.45±0.06 W/m-K at room temperature. When the MD simulation result was compared with the experimental value, it was found that the MD simulation result along the $c^{*}$ direction is 1.9 times larger than the experimental result. This is expected because the experiments were performed on thermally evaporated DNTT thin films with grain boundaries or other defects while the simulation is based on a perfect crystalline DNTT. The transmission electron microscope (TEM, Tecnai G2 20 S-TWIN) and atomic force microscope (AFM, Bruker MultiMode 8) images in Figs. 3(a) and 3(c), show that the DNTT thin films used in the experiment are composed of many small DNTT grains. Furthermore, a ring pattern with bright spots in the selected area electron diffraction (SAED) image (Fig. 3(b)) also confirms the polycrystalline structure and thus grain boundaries are present in the thin films. In essence, the thermal conductivity of the semiconductor is determined by different phonon-phonon scatterings, including Umklapp, normal, boundary, and impurity scatterings. $^{39-41}$ Recently, Epstein et al. used different self-assembly monolayers (SAMs) to modify the surface energy of the substrate to obtain pentacene thin films with different grain sizes. $^{42}$ By using frequency domain thermoreflectance (FDTR), they found that the thermal conductivity of pentacene can be enhanced from approximately 0.25 W/m-K to approximately 1 W/m-K when the pentacene grain size is increased from 144 nm to 293 nm at room temperature. Similarly, their experimental results were also different from the MD simulation results reported by Wang et al. which were based on single crystal pentacene. $^{12}$ These findings suggest the decreases in thermal conductivity induced by the crystal boundary and other defects are worthy of more detailed investigation.

Effect of temperature

The second factor that we examined was the temperature effect on the thermal conductivity of the DNTT organic semiconductor. The temperature range was 100 K to 600 K because the differential scanning calorimetry (DSC) results showed there is no thermal transition for DNTT up to 390 °C. $^{29}$ We changed the equilibrium temperature of NVT to control the simulation temperature. For each

![](./images/811088260200660993_5.jpg)

Fig. 3 (a) TEM image of 50 nm DNTT thin film at 300 K. (b) SAED pattern of 50 nm DNTT thin film at 300 K. (c) AFM image of 50 nm DNTT thin film at 300 K.


![](./images/811088260200660993_6.jpg)

Fig. 4 Temperature (T) dependence of thermal conductivity (k) for DNTT along $a^{*}$, $b^{*}$ and $c^{*}$ directions. Solid lines represent fitting curves between k and T based on the relation: $k \propto 1/T$.

heat flux direction, the cross-sectional size of the simulation boxes was the same as that of the previous simulation ($4 \times 4$ unit cells) and sample lengths are as follows: $a^{*}$-100 unit cells; $b^{*}$-100 unit cells; and $c^{*}$-64 unit cells. Fig. 4 shows the thermal conductivity of DNTT along the $a^{*}$, $b^{*}$ and $c^{*}$ directions at different simulation temperatures. It can be observed that the thermal conductivities of the $a^{*}$ and $c^{*}$ directions are reduced as the temperature increases. On the other hand, the thermal conductivity of the $b^{*}$ direction shows only a slight decrease in the same temperature range. In general, when the crystal temperature increases, phonon Umklapp scattering becomes stronger and the effective phonon MFP is reduced, thus resulting in a decrease of the thermal conductivities as shown in the $a^{*}$ and $c^{*}$ directions. However, since the intrinsic phonon MFP is much shorter and average phonon velocity is much smaller along the $b^{*}$ direction, temperature does not have an obvious effect on the thermal conductivity along the $b^{*}$ direction. The increase of temperature makes the phonon Umklapp scattering dominate the phonon scattering, so the thermal conductivity follows the relation: $k \propto 1/T.^{39}$ Fig. 4 shows that the fitting curves agree with the MD simulation results well, thus validating our analysis about the temperature dependence of thermal conductivity.

Effect of crystal boundary

When heat transports across the interface of different crystals or grain boundaries, temperature discontinuity will occur at the interface, which gives rise to TBR. TBR, which is also known as Kapitza resistance $(R_{K})$, is described by the following equation:

$$
R_{K}=\frac{\Delta T}{q} \tag{7}
$$

where $\Delta T$ is the temperature drop at the interface and $q$ is the heat flux across the interface. To study the effect of the crystal boundary on the thermal transport of DNTT, we calculated the TBR across DNTT crystal boundary by using NEMD. In practice, the DNTT crystal boundary is randomly distributed in the thin films as shown in Fig. 3 and it is difficult to simulate all these random crystal boundaries. Hence we choose three representative crystal boundary interfaces, i.e. $a^{*}-b^{*}$, $a^{*}-c^{*}$ and $c^{*}-b^{*}$ interfaces. Since the DNTT structure is monoclinic, a simulation system with crystals of two orientations cannot be periodically repeated in three dimensions, and thus the free boundary condition was applied. The configurations $(x \times y \times z)$ of the crystals with hybrid orientations are: $b^{*} \times c^{*} \times a^{*}-c^{*} \times a^{*} \times b^{*}(a^{*}-b^{*})$, $b^{*} \times c^{*} \times a^{*}-a^{*} \times b^{*} \times c^{*}(a^{*}-c^{*})$ and $c^{*} \times a^{*} \times b^{*}-a^{*}$

![](./images/811088260200660993_7.jpg)

Fig. 5 (a-c) Structure of $a^{*}-b^{*}$, $a^{*}-c^{*}$ and $b^{*}-c^{*}$ interfaces at initial condition. (d-f) Structure of $a^{*}-b^{*}$, $a^{*}-c^{*}$ and $b^{*}-c^{*}$ interfaces after thermal equilibrium in NVT ensemble.

$\times b^{*} \times c^{*}\ (b^{*}-c^{*})$. Figs. 5(a) to 5(c) show the structure of the $a^{*}-b^{*}$, $a^{*}-c^{*}$ and $b^{*}-c^{*}$ interfaces in the initial condition. The structure of the $a^{*}-b^{*}$, $a^{*}-c^{*}$ and $b^{*}-c^{*}$ interfaces is presented in Figs. 5(d) to 5(f) after thermal equilibrium is reached in the NVT ensemble. Five different system lengths were applied along the heat flux direction (z direction) for each configuration and the details are provided in Table 1. We also changed the interface cross-sectional areas to verify the effect of the cross-sectional areas on TBR. We found that there was no variation in the TBR with changes in the cross-sectional areas. During the simulation, molecule layers at the edges of the simulation box were fixed. The heat source and sink were placed at the molecule layers close to the two ends of the z direction and the simulation temperature was set as 300 K. By changing the location of the heat source and sink, no thermal rectification phenomenon was observed (see Fig. S3 in the ESI†).

### Table 1 Detailed configurations of various interfaces

<table>
  <thead>
    <tr>
      <th>Crystal orientation</th>
      <th colspan="5">Configuration (Unit cells)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>$b^* \times c^* \times a^*$ - $c^* \times a^* \times b^*$</td>
      <td>10×5×11-5×10×11</td>
      <td>10×5×15-5×10×15</td>
      <td>10×5×21-5×10×21</td>
      <td>10×5×31-5×10×31</td>
      <td>10×5×41-5×10×41</td>
    </tr>
    <tr>
      <td>$b^* \times c^* \times a^*$ - $a^* \times b^* \times c^*$</td>
      <td>10×5×11-10×8×6</td>
      <td>10×5×15-10×8×8</td>
      <td>10×5×21-10×8×11</td>
      <td>10×5×31-10×8×16</td>
      <td>10×5×41-10×8×21</td>
    </tr>
    <tr>
      <td>$c^* \times a^* \times b^*$ - $a^* \times b^* \times c^*$</td>
      <td>5×10×11-10×8×6</td>
      <td>5×10×15-10×8×8</td>
      <td>5×10×21-10×8×11</td>
      <td>5×10×31-10×8×16</td>
      <td>5×10×41-10×8×21</td>
    </tr>
  </tbody>
</table>

![](./images/811088260200660993_8.jpg)

Fig. 6 (a) Typical temperature distribution along the heat flux direction (z direction) for $a^*$ - $b^*$ interface. Black square represents $b^* \times c^* \times a^*$ crystal orientation. Red dot represents $c^* \times a^* \times b^*$ crystal orientation. Solid lines denote linear fittings near interface to obtain temperature drop ($\Delta T$) at interface. (b) TBR of $a^*$ - $b^*$, $a^*$ - $c^*$ and $b^*$ - $c^*$ interfaces for different simulation box lengths ($L$) at 300 K. Dashed lines denote average TBR values for different interfaces. (c) Phonon DOS of DNTT for $a^*$ - $b^*$, $a^*$ - $c^*$ and $b^*$ - $c^*$ interfaces. Slanted line areas denote overlap of phonon DOS.

The temperature distribution along the heat flux direction for the $a^*$ - $b^*$ interface in Fig. 6(a) shows a temperature drop at the interface. Fig. 6(b) shows the variation of the TBR with different system lengths. For all of the interfaces, the TBR remains almost constant with increasing system length. This differs from the reported length dependence of TBR of a silicon-germanium (Si-Ge) interface reported by Balasubramanian and Puri.⁴³ As the phonon MFP values are much longer for Si and Ge,⁴⁴ an increase in the system length allows for more phonons with the long MFP to contribute to the energy transport, thus leading to a reduction in the predicted TBR of the Si-Ge interface. However, in our DNTT material, the average phonon MFP values are 13.8, 9.5 and 8.4 nm along the $a^*$, $b^*$ and $c^*$ directions, respectively, which are close to or shorter than our system length in our simulation work. As a result, most of the DNTT phonons have been excited to transport energy within the system length in the simulation. As shown in Fig. 6(b), the average TBR across the $a^*$ - $b^*$, $a^*$ - $c^*$ and $b^*$ - $c^*$ interfaces is 7.00±0.26, 6.15±0.13 and 3.20±0.09 ×10⁹ m²-K/W, respectively. These TBR values are comparable to those of organic-organic interfaces that consist of two different types of materials, such as copper phthalocyanine (CuPc)-fullerene (C₆₀) interfaces.⁴⁵ It is also much lower than the TBR of the silver (Ag)-DNTT interface

![](./images/811088260200660993_9.jpg)

Fig. 7 Thermal conductivity ($k$) of DNTT thin film with different interface numbers at 300 K. Total thickness of DNTT thin film is 50 nm. Assumption that thin film is composed of two types of crystal orientations ("A" and "B"). "A" and "B" represent $a^{*}$, $b^{*}$ or $c^{*}$ crystal orientation. Green dashed line is the experimental thermal conductivity value (0.45 W/K-m).

evaluated in our previous work $(1.14 \times 10^{-7}\ \text{m}^2\text{-K/W}).^{38}$ To gain deeper insight into these TBR values, we further evaluated the phonon DOS of the DNTT molecules near to the interface. From Fig. 6(c), the phonon DOS of two DNTT orientations across the interface show a large overlapping region while the overlap of the phonon DOS of organic semiconductors and metal is small. $^{45}$ The large overlap of phonon DOS indicates that the phonons have a wide transport channel, so that the TBR of the DNTT crystal interface is small. It should also be noted that the overlapping factors for $a^{*}-b^{*}$, $a^{*}-c^{*}$ and $b^{*}-c^{*}$ interfaces calculated by Eq. (3) are 0.0387, 0.0379 and 0.0393, which demonstrates that extent of overlap in the phonon DOS for all three interfaces is similar. As shown in Figs. 5(d) to 5(f), after thermal equilibrium is reached, the molecules close to the interface restructure. In comparison to the initial condition, disorder of the molecules (around two or three layers) in the $a^{*}$ orientation occurs in both the $a^{*}-b^{*}$ and $a^{*}-c^{*}$ interfaces while the molecules in the $b^{*}-c^{*}$ interface are identical with the original structure. The disorder of the molecules close to the interface induces the phonon scattering and hinders phonon transport in the $a^{*}$ orientation side. Although the overlapping factors for three interfaces are similar, the TBR across the $a^{*}-b^{*}$ and $a^{*}-c^{*}$ interfaces outweighs that of the $b^{*}-c^{*}$ interface due to molecular restructuring near the interface. To further understand the phonon scattering across the interfaces, we calculated the spatial distribution of heat flux across $a^{*}-b^{*}$, $a^{*}-c^{*}$ and $b^{*}-c^{*}$ interfaces (see Fig. S4 in the ESI$\dagger$). Strong scattering can be observed around the interface regions.

If we assume that the differences between the experimental and the MD simulation results for thermal conductivity for perfect single crystals are only resultant of crystal misalignment based on the TBR values, then we can quantify the number of boundary interfaces in the DNTT thin films used in the experimental study. We assume that the DNTT thin films (50 nm in thickness) in the experiment is composed of two types of crystal orientations ("A" and "B") as shown in Fig. 7. "A" and "B" represent the $a^{*}$, $b^{*}$ or $c^{*}$ crystal orientation. The effective thermal conductivity of the DNTT thin film, $k_{film}$, can be calculated from:

$$
\frac{1}{k_{film}}=m \cdot\left(\frac{L_{A}}{k_{A}}+\frac{L_{B}}{k_{B}}\right)+(2 m-1) \cdot R_{K} \tag{8}
$$

where $m$ denotes the period number of "A-B", $k_{A}$ and $k_{B}$ are the predicted thermal conductivity calculated from the MD simulation results with Eq. (6), $R_{K}$ is the TBR across the interface, and $L_{A}$ and $L_{B}$ are the thickness of the "A" and "B" layer. To reduce the degree of freedom of the variables in Eq. (8), it is assumed that $L_{A}=L_{B}$ and $m(L_{A}+L_{B})=50$ nm. Fig. 7 shows the effective thermal conductivity calculated from Eq. (8) as a function of the interface number. When the interface number increases, the effective thermal conductivity of the mixed orientation structures ($a^{*}-b^{*}$, $a^{*}-c^{*}$ and $b^{*}-c^{*}$) is monotonically reduced. To match the MD simulation results to the experimental values, one can estimate that there are around one to two crystal interfaces in the DNTT thin films of the experimental sample. It is important to point out that the estimated number of crystal interfaces in the DNTT thin films of the experimental sample represents the upper limit value, because the effects of other types of defects on the thermal conductivity are neglected, which we will discuss later.

![](./images/811088260200660993_10.jpg)

Fig. 8 Thermal conductivity ($k$) of DNTT long $a^{*}$, $b^{*}$ and $c^{*}$ directions with different vacancy concentrations ($n$) that range from 0% to 6% at 300 K. Solid lines represent fitting curves between $k$ and $n$ based on Eq. (9). Green dashed line is experimental thermal conductivity value (0.45 W/K-m).

### Effect of crystal defect

Defects in semiconductor crystals not only block the charge transport, but also result in phonon scattering which reduces the phonon MFP for thermal transport. Crystal defects have different forms including impurity and vacancy. Given that vacancy defects can be easily generated during the fabrication process of organic semiconductor thin films, $^{46-48}$ in this section, our primary focus is on the vacancy effect on the thermal conductivity of DNTT. In the simulation, the sample dimensions were: $a^{*}$-4×4×100 unit cells; $b^{*}$-4×4×100 unit cells; and $c^{*}$-4×4×64 unit cells. The boundary condition was periodic and simulation temperature was 300 K. In the simulation system, the DNTT molecules were randomly removed for vacancy concentration which ranged from 0% to 6%. Fig. 8 shows the thermal conductivity variations with respect to different vacancy concentrations. It can be observed that the thermal conductivities of the three directions monotonically decrease with vacancy concentration. When the vacancy concentration is 6%, the MD

simulations predict that the thermal conductivities of DNTT are reduced 44%, 33% and 35% in the $a^{*}$, $b^{*}$ and $c^{*}$ directions, respectively, which demonstrate that vacancies have a significant effect on the thermal transport of organic thin films. We also calculated the heat flux distribution for different DNTT crystal orientations with 6% vacancy concentration as shown in Fig. S5 of the ESI†. It can be observed that there are scattering of heat propagation around the vacancy regions which further verify that phonon scattering induced by vacancy hinders the thermal transport.

Che *et al.* proposed that the thermal conductivity and vacancy concentration of diamonds follow the relation:⁴⁹

$$
k_{vac}(n)=\frac{k_{per}}{1+\varphi n^{\alpha}} \tag{9}
$$

where $k_{vac}$ and $k_{per}$ are the thermal conductivities of material with vacancy and perfect crystals, respectively; $n$ is the vacancy concentration; $\varphi$ is the fitting parameter; and $\alpha$ is the scaling factor to evaluate the material sensitivity to vacancy. By fitting Eq. (9) to the MD simulation results, the scaling factors along the $a^{*}$, $b^{*}$ and $c^{*}$ directions are 1.004, 1.048 and 1.215, respectively. The obtained scaling factors are very close to the value of silicon⁵⁰ and pentacene¹². Based on the investigation on the effects of crystal boundary and vacancy, we conclude that both crystal boundary and vacancy can play an important role in the thermal transport of organic semiconductors. Owing to the polycrystalline nature of DNTT, many boundaries and defects form during thin film fabrication, which explains why the experimental value of the thermal conductivity of $c^{*}$ direction is much lower than the MD predicted value. Since the structure of polycrystalline DNTT thin film is complex, it is challenging to separate the effects of these two aspects through experiments.

## Conclusions
We have investigated thermal transport in a small molecule organic semiconductor, dinaphtho[2,3-b:2',3'-f]thieno[3,2-b]thiophene (DNTT), by using NEMD. The predicted bulk thermal conductivities of DNTT along $a^{*}$, $b^{*}$ and $c^{*}$ directions are 0.73, 0.33 and 0.95 W/m-K, respectively, which indicates an obvious anisotropy of the thermal transport. The MD predicted thermal conductivity in the $c^{*}$ direction of the DNTT thin film with a thickness of 50 nm is around 0.85 W/m-K, which is 1.9 times larger than that of a previous experimental result (0.45 W/m-K). The SAED pattern, TEM and AFM images prove that the DNTT thin film used in the experiment is polycrystalline, thus indicating that grain boundary and vacancy play an important role in the experimental result which is not considered in the MD simulation which considers perfect single crystals. We also study the temperature dependence of thermal conductivity and find that thermal conductivity monotonically decreases with increasing temperatures. In addition, the TBR across different interfaces is investigated. The simulated TBR values are $7.00\pm0.26$, $6.15\pm0.13$ and $3.20\pm0.09 \times 10^{-9}$ m²-K/W for the $a^{*}$-$b^{*}$, $a^{*}$-$c^{*}$ and $b^{*}$-$c^{*}$ interfaces, respectively. In comparing the MD simulation results with the experimental values, it is estimated there are around one to two interfaces in the DNTT thin films. Furthermore, we also investigate the vacancy effect on the thermal conductivity of the DNTT thin films. The predicted thermal conductivities of DNTT are reduced 44%, 33% and 35% in the $a^{*}$, $b^{*}$ and $c^{*}$ directions, respectively, with a vacancy concentration of 6%. Hence, due to the phonon boundary and phonon defect scatterings, the crystal boundaries and vacancies have significant influences on the thermal properties of organic semiconductors. Our findings thus provide valuable information on ways to modulate the thermal conductivity of organic semiconductors to obtain the desired thermoelectric properties and improve the thermal management capability of organic electronics.

## Acknowledgements
We gratefully acknowledge the support from General Research Fund (GRF) under Grant No. HKU 710313E and 17200314, Collaborative Research Fund (CRF) under Grant No. C7045-14E, The National Natural Science Foundation of China (NSFC) and the Research Grants Council (RGC) of Hong Kong Joint Research Scheme under Grant No. HKU 715/14. This research is conducted in part by using the research computing facilities and advisory services offered by Information Technology Services at The University of Hong Kong. The authors appreciate the comments from Prof. Alan J. H. McGaughey of Carnegie Mellon University.

## References
1. D. T. James, B. K. C. Kjellander, W. T. T. Smaal, G. H. Gelinck, C. Combe, I. McCulloch, R. Wilson, J. H. Burroughes, D. D. C. Bradley and J.-S. Kim, *ACS Nano*, 2011, **5**, 9824-9835.
2. Y. Diao, B. C. K. Tee, G. Giri, J. Xu, D. H. Kim, H. A. Becerril, R. M. Stoltenberg, T. H. Lee, G. Xue, S. C. B. Mannsfeld and Z. Bao, *Nat. Mater.*, 2013, **12**, 665-671.
3. M. Shtein, H. F. Gossenberger, J. B. Benziger and S. R. Forrest, *J. Appl. Phys.*, 2001, **89**, 1470-1476.
4. M. R. Niazi, R. Li, E. Qiang Li, A. R. Kirmani, M. Abdelsamie, Q. Wang, W. Pan, M. M. Payne, J. E. Anthony, D.-M. Smilgies, S. T. Thoroddsen, E. P. Giannelis and A. Amassian, *Nat. Commun.*, 2015, **6**, 8598.
5. H. Yang, M.-M. Ling and L. Yang, *J. Phys. Chem. C*, 2007, **111**, 12508-12511.
6. K. Kuribara, H. Wang, N. Uchiyama, K. Fukuda, T. Yokota, U. Zschieschang, C. Jaye, D. Fischer, H. Klauk, T. Yamamoto, K. Takimiya, M. Ikeda, H. Kuwabara, T. Sekitani, Y.-L. Loo and T. Someya, *Nat. Commun.*, 2012, **3**, 723.
7. H. Chang, Y. Deng, Y. Geng, T. Wang and D. Yan, *Org. Electron.*, 2015, **22**, 86-91.
8. M.-C. Jung, M. R. Leyden, G. O. Nikiforov, M. V. Lee, H.-K. Lee, T. J. Shin, K. Takimiya and Y. Qi, *ACS Appl. Mater. Interfaces*, 2015, **7**, 1833-1840.
9. W. Xie, K. Willa, Y. Wu, R. Häusermann, K. Takimiya, B. Batlogg and C. D. Frisbie, *Adv. Mater.*, 2013, **25**, 3478-3484.
10. E. Vitoratos, S. Sakkopoulos, E. Dalas, N. Paliatsas, D. Karageorgopoulos, F. Petraki, S. Kennou and S. A. Choulis, *Org. Electron.*, 2009, **10**, 61-66.
11. S. Chung, J.-H. Lee, J. Jeong, J.-J. Kim and Y. Hong, *Appl. Phys. Lett.*, **94**, 253302.

This journal is © The Royal Society of Chemistry 2016

*Nanoscale*, 2016, **00**, 1-9 | 9

12. D. Wang, L. Tang, M. Long and Z. Shuai, *J. Phys. Chem. C*, 2011, **115**, 5940-5946.

13. Y. Liu, J. Huang, B. Yang, B. G. Sumpter and R. Qiao, *Carbon*, 2014, **75**, 169-177.

14. C. Shao, Y. Jin, K. Pipe, M. Shtein and J. Kieffer, *J. Phys. Chem. C*, 2014, **118**, 9861-9870.

15. Y. Jin, C. Shao, J. Kieffer, M. L. Falk and M. Shtein, *Phys. Rev. B*, 2014, **90**, 054306.

16. W.-L. Ong, S. Majumdar, J. A. Malen and A. J. H. McGaughey, *J. Phys. Chem. C*, 2014, **118**, 7288-7295.

17. S. Plimpton, *J. Comput. Phys.*, 1995, **117**, 1-19.

18. Y. Hong, J. Zhang, X. Huang and X. C. Zeng, *Nanoscale*, 2015, **7**, 18716-18724.

19. D. P. Sellan, E. S. Landry, J. E. Turney, A. J. H. McGaughey and C. H. Amon, *Phys. Rev. B*, 2010, **81**, 214305.

20. W. D. Cornell, P. Cieplak, C. I. Bayly, I. R. Gould, K. M. Merz, D. M. Ferguson, D. C. Spellmeyer, T. Fox, J. W. Caldwell and P. A. Kollman, *J. Am. Chem. Soc.*, 1995, **117**, 5179-5197.

21. S. J. Weiner, P. A. Kollman, D. A. Case, U. C. Singh, C. Ghio, G. Alagona, S. Profeta and P. Weiner, *J. Am. Chem. Soc.*, 1984, **106**, 765-784.

22. S. J. Weiner, P. A. Kollman, D. T. Nguyen and D. A. Case, *J. Comput. Chem.*, 1986, **7**, 230-252.

23. P. Dauber-Osguthorpe, V. A. Roberts, D. J. Osguthorpe, J. Wolff, M. Genest and A. T. Hagler, *Proteins.*, 1988, **4**, 31-47.

24. H. Sun, *J. Phys. Chem. B*, 1998, **102**, 7338-7364.

25. H. Sun, P. Ren and J. R. Fried, *Comput. Theor. Polym. Sci.*, 1998, **8**, 229-246.

26. J. Wang, R. M. Wolf, J. W. Caldwell, P. A. Kollman and D. A. Case, *J. Comput. Chem.*, 2004, **25**, 1157-1174.

27. W. Shi, J. Chen, J. Xi, D. Wang and Z. Shuai, *Chem. Mater.*, 2014, **26**, 2669-2677.

28. M. Yoneya, M. Kawasaki and M. Ando, *J. Mater. Chem.*, 2010, **20**, 10397-10402.

29. T. Yamamoto and K. Takimiya, *J. Am. Chem. Soc.*, 2007, **129**, 2224-2225.

30. W. Duffy, F. M. Weinhaus, D. L. Strandburg and J. F. Deck, *Phys. Rev. B*, 1979, **20**, 1164-1172.

31. P. Ramadoss and N. Buvaneswari, *J. Chem.*, 2011, **8**, 1246-1249.

32. J. M. Dickey and A. Paskin, *Phys. Rev.*, 1969, **188**, 1407-1418.

33. B. Li, J. Lan and L. Wang, *Phys. Rev. Lett.*, 2005, **95**, 104302.

34. D. Alexeev, J. Chen, J. H. Walther, K. P. Giapis, P. Angelikopoulos and P. Koumoutsakos, *Nano Lett.*, 2015, **15**, 5744-5749.

35. J. A. Thomas, J. E. Turney, R. M. Iutzi, C. H. Amon and A. J. H. McGaughey, *Phys. Rev. B*, 2010, **81**, 081411.

36. J. E. Turney, E. S. Landry, A. J. H. McGaughey and C. H. Amon, *Phys. Rev. B*, 2009, **79**, 064301.

37. D. P. Sellan, J. E. Turney, A. J. H. McGaughey and C. H. Amon, *J. Appl. Phys.*, 2010, **108**, 113524.

38. X. Wang, K. D. Parrish, J. A. Malen and P. K. L. Chan, *Sci. Rep.*, 2015, **5**, 16095.

39. M. G. Holland, *Phys. Rev.*, 1963, **132**, 2461-2471.

40. J. Callaway, *Phys. Rev.*, 1959, **113**, 1046-1051.

41. J. D. Chung, A. J. H. McGaughey and M. Kaviany, *J. Heat Transfer*, 2004, **126**, 376-380.

42. J. Epstein, W.-L. Ong, C. J. Bettinger and J. A. Malen, *ACS Appl. Mater. Interfaces*, 2016, **8**, 19168-19174.

43. G. Balasubramanian and I. K. Puri, *Appl. Phys. Lett.*, 2011, **99**, 013116.

44. A. Minnich and G. Chen, *Appl. Phys. Lett.*, 2007, **91**, 073105.

45. Y. Jin, C. Shao, J. Kieffer, K. P. Pipe and M. Shtein, *J. Appl. Phys.*, 2012, **112**, 093503.

46. A. Poschlad, V. Meded, R. Maul and W. Wenzel, *Nanoscale Res. Lett.*, 2012, **7**, 248.

47. R. Ruiz, D. Choudhary, B. Nickel, T. Toccoli, K.-C. Chang, A. C. Mayer, P. Clancy, J. M. Blakely, R. L. Headrick, S. Iannotta and G. Malliaras, *Chem. Mater.*, 2004, **16**, 4497-4508.

48. S. Seo, L. C. Grabow, M. Mavrikakis, R. J. Hamers, N. J. Thompson and P. G. Evans, *Appl. Phys. Lett.*, 2008, **92**, 153313.

49. J. Che, T. Çağın, W. Deng and W. A. Goddard, *J. Chem. Phys.*, 2000, **113**, 6888-6900.

50. Y. Lee, S. Lee and G. S. Hwang, *Phys. Rev. B*, 2011, **83**, 125202.