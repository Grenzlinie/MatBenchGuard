# Enhanced Charge Separation in Single Atom Cobalt Based Graphitic Carbon Nitride: Time Domain *Ab Initio* Analysis

Sraddha Agrawal, David Casanova, Dhara J. Trivedi,* and Oleg V. Prezhdo

Cite This: *J. Phys. Chem. Lett.* 2024, 15, 2202−2208

Read Online

ACCESS | Metrics & More | Article Recommendations | Supporting Information

**ABSTRACT:** In recent years, single atom catalysts have been at the forefront of energy conversion research, particularly in the field of catalysis. Carbon nitrides offer great potential as hosts for stabilizing metal atoms due to their unique electronic structure. We use *ab initio* nonadiabatic molecular dynamics to study photoexcitation dynamics in single atom cobalt based graphitic carbon nitride. The results elucidate the positive effect of the doped cobalt atom on the electronic structure of GCN. Cobalt doping produces filled midgap states that serve as oxidation centers, advantageous for various redox reactions. The presence of midgap states enables the harvesting of longer wavelength photons, thereby extending the absorption range of solar light. Although doping accelerates charge relaxation overall, charge recombination is significantly slower than charge separation, creating beneficial conditions for catalysis applications. The simulations reveal the detailed microscopic mechanism underlying the improved performance of the doped system due to atomic defects and demonstrate an effective charge separation strategy to construct highly efficient and stable photocatalytic two-dimensional materials.

![](./images/966876699536916489_1.jpg)

The use of carbon based materials for catalytic applications has garnered significant interest in recent years, owing to their tunable properties and low toxicity.¹ Among these materials, graphitic carbon nitride (GCN) has emerged as a promising catalyst due to its stable, metal-free nature and ability to absorb visible light.²⁻⁴ However, the low surface area and poor charge transferability of GCN have hindered its widespread application in catalytic reactions.⁵,⁶ Various approaches have been explored to improve the catalytic properties of GCN, including doping with heteroatoms, creating defects, and incorporating metal nanoparticles.⁷⁻¹⁰ However, these methods often suffer from issues such as low stability, agglomeration of nanoparticles, and difficulty in controlling the size and dispersion of metal particles.

Single atom catalysts (SACs) have emerged as a new class of catalysts that can overcome some of the limitations of traditional metal nanoparticles.¹¹⁻¹³ SACs consist of individual metal atoms dispersed on a support material, and their high catalytic activity and selectivity arise from the unique properties of isolated metal atoms. SACs exhibit excellent performance in many situations, including electrochemical, gas-phase, and liquid-phase reactions.¹⁴ The integration of SACs with GCN can improve the catalytic performance of GCN.¹⁵⁻¹⁸ The synthesis and characterization of SAC based GCN catalysts have been studied in recent years, with various metals being investigated for their suitability in this hybrid material.¹⁹ The successful integration of SACs with GCN has been demonstrated using metals such as Co, Pt, and Fe, among others.²⁰⁻²³ In these systems, the isolated metal atoms act as active sites for catalysis, improving the efficiency and selectivity of the GCN catalyst.

The catalytic activity of SAC based GCN catalysts has been evaluated for a wide range of reactions, including photodegradation of organic pollutants and electrocatalytic oxygen reduction reactions, such as CO₂ reduction and selective oxidation of alcohols.¹⁵,²³⁻²⁵ In each of these applications, the SAC based catalysts exhibited superior performance compared with GCN without the inclusion of SACs. This is attributed to the enhanced charge transfer and catalytic activity of the isolated metal atoms in the hybrid material. The combination of SACs with GCN can potentially boost the catalytic properties of both materials by exploiting the synergistic effect between the isolated metal atoms and the GCN support.¹⁶,¹⁸

Herein, we report an excited state quantum dynamics study of nonradiative processes in cobalt single atom catalyst based GCN (Co-GCN) to gain insights into the nonequilibrium processes observed experimentally for photocatalysis. For this purpose, we employ a combination of *ab initio* time-dependent density functional theory (TDDFT) and nonadiabatic (NA) molecular dynamics (MD). The calculations demonstrate that Co-SACs can be stabilized on the surface of GCN through strong coordination bonds with the nitrogen atoms. We examine the effect of Co-SACs on the electronic properties of

Received: December 28, 2023
Revised: February 7, 2024
Accepted: February 14, 2024

![](./images/966876699536916489_2.jpg)

© XXXX The Authors. Published by
American Chemical Society
2202
https://doi.org/10.1021/acs.jpclett.3c03621
*J. Phys. Chem. Lett.* 2024, 15, 2202−2208

![](./images/966876699536916489_3.jpg)

Figure 1. (a) Top and (b) side views of the optimized structure of cobalt-(OH)₂ graphitic carbon nitride (Co-GCN). Atoms: C, brown; N, gray; Co, blue; O, red; H, pink. Cobalt with two OH groups on opposite sides of Co is introduced at the center of the GCN cavity (most stable site) to model a single atom catalyst based GCN. The cobalt atom is coordinated to two nitrogen atoms of the tri-s-triazine unit of GCN and as well as to the two hydroxy groups. The geometry is optimized after heating and is overall nonplanar.

GCN and the efficiency of the resulting composite material for photocatalytic applications. The Co-SACs induce charge redistribution in the GCN framework, leading to the creation of new electronic states that enhance the catalytic activity of GCN. Our results indicate that Co centers can serve as oxidation centers and are beneficial for photoinduced charge separation. The calculations show that Co doping accelerates charge relaxation and recombination relative to that of pristine GCN. However, charge separation driven by the doping is fast, and charge recombination in Co-GCN is sufficiently slow to allow for the desired photocatalytic activity. The simulations provide a detailed mechanistic understanding of the atomistic origin of the improved performance of Co-GCN in various photocatalytic applications and offer guidance for the design of efficient materials for photocatalysis.

The simulations are performed using the mixed quantum−classical approach implementing NAMD within real-time TDDFT²⁶ in the Kohn−Sham (KS) framework.²⁷,²⁸ The NAMD simulations are performed using the decoherence induced surface hopping (DISH) algorithm²⁹ as implemented in the PYXAID software, under the classical path approximation.³⁰,³¹ DISH incorporates the loss of coherence within the electronic subsystem induced by coupling to quantum vibrations.³² Decoherence effects become important in slow charge trapping and recombination processes taking place across large energy gaps.³³⁻³⁶ The decoherence time is estimated by computing the pure-dephasing time using the optical response theory formalism.³²,³⁷,³⁸ A detailed mathematical description of the method can be found in previous papers.³⁰,³¹,³⁹ The method has been extensively applied to study excited state dynamics in a broad range of nanomaterials.⁴⁰⁻⁵²

Ground state geometry optimization, adiabatic MD, and NA coupling calculations are performed using the Vienna Ab initio Simulation Package (VASP),⁵³⁻⁵⁵ which uses a converged plane-wave basis. The Perdew−Burke−Ernzerhof (PBE) functional⁵⁶ is used to calculate the exchange-correlation effects. To describe a strongly correlated system, a Hubbard $U$ correction is applied with a value of $U_{\text{eff}} = 3.0$ eV for the Co 3d states.⁵⁷,⁵⁸ In general, although hybrid functionals, such as HSE06,⁵⁹,⁶⁰ are considered to be more reliable than PBE and PBE+$U$, DFT+$U$ is still a popular method to treat strongly correlated systems at a lower computational cost. Because the $+U$ correction is applied only to the Co atom and PBE tends to underestimate energy gaps, we employ the HSE06 functional as a reference to scale the PBE+$U$ energy gaps. Specifically, we compute the electronic structure of the system in the optimized geometry using both the HSE06 and PBE+$U$ functional and use the HSE06/PBE+$U$ energy gap ratios to scale the PBE+$U$ energy gaps obtained during MD simulations. Because the NA coupling is inversely proportional to the corresponding energy gap,³³ we scale the NA couplings obtained by PBE+$U$ by the inverse HSE06/PBE+$U$ energy gap ratios as well.

The van der Waals interactions are described via the optB86b-vdW functional employed in the vdW-DF method.⁶¹ The plane-wave basis energy cutoff and the convergence criteria for energy and force are set to 750 eV, $10^{-6}$ eV/atom, and 0.01 eV/Å, respectively. A vacuum layer of 20 Å is added onto the Co-GCN surface to avoid the interaction between the layers in the $z$-direction. A $3 \times 3 \times 1$ $\Gamma$-centered $k$-point mesh is used for the geometry optimization and adiabatic MD. A denser $9 \times 9 \times 1$ $k$-mesh is further employed to obtain an accurate electronic structure with the PBE+$U$ functional. VESTA software is used as a visualization tool.⁶² The NA coupling are calculated using the CA-NAC package.⁶³,⁶⁴ The NA couplings are obtained at the $\Gamma$-point because the system has a direct bandgap at the $\Gamma$-point.

The doped system is modeled using a $2 \times 2$ supercell with unit cell lattice parameters as given in ref 65. The system consists of 61 atoms which include 24 C, 32 N, 1 Co, 2 O, and 2 H atoms. After relaxing the geometry at 0 K, the system is heated to 300 K through repeated velocity rescaling for 2 ps. Then, 5 ps adiabatic MD trajectories are obtained in the microcanonical ensemble (NVE) with a 1 fs atomic time step. To specify the initial magnetic moment for each atom and the spin multiplet, MAGMOM and NUPDOWN = 3 parameters are used, improving the electronic structure convergence. The ab initio MD simulation demonstrates rapid fluctuations of electronic energy levels, well sampled by the 5 ps trajectory (Figure S1 of the Supporting Information). Therefore, 1 ns long NAMD simulations are performed by iterating the 5 ps NA Hamiltonian multiple times. The simulations are performed with the PYXAID software.³⁰,³¹ To simulate the quantum dynamics of charge separation, trapping, and recombination, 100 initial configurations are selected randomly from the adiabatic MD trajectory, and 100 stochastic DISH sequences are sampled for each initial condition.

The optimized structure of Co-GCN is shown in Figure 1. A single Co atom is embedded in the center of a void of the GCN framework. The structure has been identified as the most stable for most transition-metal atoms including cobalt.⁶⁶

![](./images/966876699536916489_4.jpg)

Figure 2. Spin-resolved atom projected density of states (PDOS) of Co-GCN obtained using (a) PBE+U and (b) HSE functionals. The positions of the band edge states are labeled as VBM and CBM, and the states between are trap states. The Fermi energy level is set to 0 in both cases. Energy gaps between the states obtained using HSE are used in the dynamics calculations because the bandgap obtained using the HSE functional is closer to the experimental bandgap of GCN.

![](./images/966876699536916489_5.jpg)

Figure 3. Charge densities (yellow) of the orbitals involved in the active space for (a) spin-up and (b) spin-down channels of Co-GCN obtained using the HSE functional. The charge densities for the band edge orbitals (CBM and VBM) are delocalized over the entire system, mostly excluding the defect region, while the charge densities for the defect trap states (d1−d4) are strongly localized near the doped Co atom.

Further, within this structure, Co is connected to two adjacent pyridinic N atoms of two distinct heptazine units and to two hydroxy (−OH) groups in order to mimic a stable four-coordinate complex.⁶⁷

Figure 2 shows the projected density of states (PDOS) of the system under investigation obtained by using two different functionals: PBE+U and HSE06. The PDOS is separated into contributions from C, N, Co, O, and H components. Here, we have shown the spin-polarized PDOS for the system because it has an odd number of electrons. Compared to the PBE+U, HSE06 opens up the bandgap between the valence band maximum (VBM) and conduction band minimum (CBM) and is closer to the experimental bandgap value of 2.7 eV.² The Co doping introduces multiple localized electronic midgap states, exhibiting contributions from the hydroxy ligands. Based on the orbital occupancy, all of the defect states are completely filled and hence act as hole traps. This implies that the introduction of cobalt is beneficial for oxidation reactions, such as water oxidation, as one can utilize the trapped photoexcited hole on cobalt as an oxidation center. At the same time, the cobalt midgap states can promote charge recombination, generating additional relaxation pathways. Moreover, because the NA coupling is inversely proportional to the energy gap between states,³⁰,³³ the new relaxation pathways will be faster than the electron−hole recombination in undoped GCN. Thus, on the one hand, cobalt doping facilitates charge separation and creates a catalytic site, while on the other hand, it accelerates charge recombination. Therefore, it is important to evaluate the two effects in order to establish whether the benefits of charge separation outweigh the drawbacks of accelerated charge recombination.

Figure 3 shows spin-resolved charge densities of the band edge orbitals and trap states obtained using the HSE functional. The VBM and CBM charge densities are delocalized over large parts of the GCN framework and partly on the doped atoms. On the other hand, the charge densities of the midgap states are strongly localized on cobalt. Charge densities, obtained as squares of the corresponding wave functions, provide a visual representation that can be used to analyze the NA coupling strength. The NA coupling magnitude is closely related to the overlap between the charge densities of the two states. Localization of charge densities in different parts of the system leads to a decreased overlap and a smaller NA coupling.

Electron−vibrational interactions create inelastic and elastic electron−phonon scattering, and both types of scattering have a strong influence on charge trapping and recombination. Inelastic scattering, quantified by the NA coupling strength, leads directly to energy exchange between electrons and phonons during nonradiative relaxation. On the other hand, elastic scattering, characterized by the pure dephasing time,³²,³⁷,³⁸ affects quantum coherence between initial and final states during a quantum transition and influences the transition indirectly.³³⁻³⁶ The charge trapping and recombination time scales are determined by NA coupling, energy gap, and pure dephasing time. In general, a larger energy gap, weaker NA coupling, and faster pure dephasing lead to slower dynamics.

<table>
<caption>Table 1. Canonically Averaged Energy Gaps and Absolute Nonadiabatic Couplings (NAC) between Pairs of States Involved in the Active Space for the Spin-Down Channel in Co-GCN¹</caption>
<thead>
  <tr>
    <th>orbitals</th>
    <th>energy (eV)</th>
    <th>scaled energy (eV)</th>
    <th>NAC (meV)</th>
    <th>scaled NAC (meV)</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>VBM−d1</td>
    <td>0.09</td>
    <td>0.11</td>
    <td>42.08</td>
    <td>34.93</td>
  </tr>
  <tr>
    <td>d1−d2</td>
    <td>0.42</td>
    <td>0.76</td>
    <td>24.31</td>
    <td>13.37</td>
  </tr>
  <tr>
    <td>d2−d3</td>
    <td>0.69</td>
    <td>0.60</td>
    <td>14.44</td>
    <td>16.61</td>
  </tr>
  <tr>
    <td>d3−CBM</td>
    <td>0.86</td>
    <td>1.00</td>
    <td>8.41</td>
    <td>7.23</td>
  </tr>
  <tr>
    <td>VBM−CBM</td>
    <td>2.08</td>
    <td>2.48</td>
    <td>2.10</td>
    <td>1.66</td>
  </tr>
</tbody>
</table>

¹The energy gaps and NAC are obtained using the PBE+U functional and are also scaled based on the HSE bandgap, as explained in the text.

The solar spectrum covers a broad range of energies, and in general, absorption of a photon places electrons and holes inside the bands away from the bandgap. However, relaxation of electrons and holes inside the bands through dense manifolds of states is fast (subpicoseconds) and is considerably faster than the charge trapping and recombination that take place across substantial energy gaps. Therefore, it is assumed in the simulations that the charges have already relaxed to the respective band edges. NAMD is then performed considering all possible electronic configurations in the active space constructed from the band edges and hole trap states, illustrated in Figure S2. In the current model, the nonradiative dynamics are simulated separately for the spin-up and spin-down channels. Evolution of populations of the multielectron states in each spin component is illustrated in Figure 4. The populations of all trap states are summed up together. More detailed data, including populations of each state separately, are presented in Figure S3. The corresponding time scales are reported in Tables 2 and S1. Analysis of the combined population of all trap states characterizes the time scales of charge separation and recombination, while the detailed information regarding population of each trap state provides data on the distribution of holes at different energies. Such information is important because the redox potential and

<table>
<caption>Table 2. Time Scales (ps) of Decay of Excited State (ES) Population, Rise of Trapped Hole Population, and Rise of Ground State (GS) Population, Corresponding to Figure 4¹</caption>
<thead>
  <tr>
    <th> </th>
    <th>ES decay</th>
    <th>trapped hole rise</th>
    <th>GS rise</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>spin up</td>
    <td>1.40 ± 0.22</td>
    <td>1.43 ± 0.56</td>
    <td>23.52 ± 2.90</td>
  </tr>
  <tr>
    <td>spin down</td>
    <td>0.32 ± 0.06</td>
    <td>0.34 ± 0.08</td>
    <td>12.18 ± 1.89</td>
  </tr>
</tbody>
</table>

¹Populations of all trap states are added to obtain the trapped hole population. Populations of individual trap states and corresponding time scales are shown in Figure S3 and Table S1.

efficiency of redox reactions are different for charges occupying different energy levels. The time scales reported in Tables 2 and S1 are obtained by fitting the relevant parts of the curve to exponential functions. Population decay is fitted to $P(t) = A\exp(-t/\tau)$, and population rise is fitted to $P(t) = B[1 - \exp(-t/\tau)]$. The constants $A$ and $B$ are set to 1 for fitting the decay and rise of the populations of the excited and ground states, while these constants are treated as fitting parameters in the analysis of the trap states. To estimate the uncertainties in the reported time scales, we divided the entire 5 ps trajectory into five 1 ps parts and obtained individual time scales for each trajectory and then computed the standard deviations, as reported in Table 2. The time scales in the spin-up channel are relatively slower than those in the spin-down channel, and therefore the faster spin-down channel is considered for further analysis, as shorter time scales dominate the relaxation processes.

Compared to pristine GCN,³⁹ the Co-GCN system has multiple midgap trap states that provide additional pathways for nonradiative charge recombination, and as a result, the charge carrier lifetime is shorter in the doped system. This theoretical conclusion is in agreement with the experimental reports on shorter lifetimes of charge carriers in the single atom Co-doped GCN compared to the pristine GCN.²³,⁶⁷,⁶⁸ The nonradiative relaxation becomes faster upon the doping due to the appearance of new relaxation channels with smaller energy gaps and stronger NA couplings. Although in the majority of applications one aims to achieve long-lived charge carriers, in the present case the drawback of the shortened

![](./images/966876699536916489_6.jpg)

Figure 4. Nonradiative charge carrier trapping and recombination dynamics in (a) spin-up and (b) spin-down channels in Co-GCN. Insets show the fast rise of the trapped hole population of the respective spin channels. The corresponding time scales are given in Table 2. The trapped hole population is obtained by combining all of the individual trap state populations shown in Figure S3. The charge trapping time is significantly faster than the recombination time, which is beneficial for photocatalytic applications.

carrier lifetime is outweighed by the benefit of the rapid charge separation and creation of the active catalytic sites by the cobalt doping. Further, the presence of midgap states extends the range of the absorbed light due to smaller energy gaps between occupied and empty states. In particular, the charge separation in the current system requires 0.3 ps in the faster spin-down channel, while the corresponding charge recombi- nation takes 12 ps, more than a factor of 40 slower. The large energy gap and small NAC between d3 (hole) and CBM (electron) (Table 1) lead to slow electron-hole recombina- tion, indicated by the rise of the GS population (Table 2 and Figure 4).

The ~10 ps lifetime of the charge separated state is sufficient to initiate chemical reactions involving bond breaking and rearrangements. For example, the oscillation period of a typical chemical bond, such as C-O for $CO_2$ reduction or O-H for $H_2O$ splitting, is shorter than 100 fs; i.e., the photocatalytic system has over 100 bond oscillation periods available to break a bond. Importantly, the current simulation cell is small due to computational limitations, restricting the charge carriers to be close to each other and making the recombination faster than in a real system. In large extended systems, charges can travel far from each other, and their recombination will be significantly slower.⁶⁹ Both charge separation and recombina- tion involve transitions between delocalized band states and localized trap states. As band states become more delocalized with increasing system size, both charge separation and recombination time scales will grow, but the separation will remain faster than the recombination. The experiments indicate that introduction of the dopant improves charge separation, while at the same time also shortens the carrier lifetime.²³⁶⁷⁶⁸ The results reported here are in agreement with the experimental works, which demonstrate better efficiency of separation of photogenerated charge carriers and improved photocatalytic performance of single cobalt atom based GCN.⁶⁸⁷⁰

In summary, we have studied the nonradiative charge separation and recombination dynamics in single atom cobalt- doped GCN by performing ab initio quantum dynamics simulations. The simulations demonstrate that introduction of cobalt produces occupied midgap states that serve as oxidation centers for redox reactions, in agreement with experimental results. The presence of midgap states increases the range of optical absorption in the solar spectrum by decreasing the energy gaps. Compared to the charge separation stemming from hole trapping, charge recombination is relatively slow due to larger energy gap and weaker NA coupling. Although the presence of trap states accelerates charge relaxation and recombination compared to the pristine system, as a result of additional recombination pathways, the overall photocatalytic performance of the doped system is better due to the enhanced charge separation rates. The performed simulations provide an atomistic understanding of the photoexcitation dynamics in a single atom catalyst based GCN and highlight its advantages in solar energy driven applications. The fundamental insights reported in this study assist in design of novel efficient materials for better photocatalytic applications.

## ASSOCIATED CONTENT

### Supporting Information
The Supporting Information is available free of charge at https://pubs.acs.org/doi/10.1021/acs.jpclett.3c03621.

Evolution of electronic energy levels, schematic of the electronic configurations in the active space, and detailed nonradiative relaxation dynamics data and correspond- ing time scales (PDF)

## AUTHOR INFORMATION

### Corresponding Author
Dhara J. Trivedi − Department of Physics, Clarkson University, Potsdam, New York 13699, United States; orcid.org/0000-0002-8151-3929; Email: dtrivedi@ clarkson.edu

### Authors
Sraddha Agrawal − Department of Chemistry, University of Southern California, Los Angeles, California 90007, United States

David Casanova − Donostia International Physics Center (DIPC), 20018 Donostia, Euskadi, Spain; IKERBASQUE, Basque Foundation for Science, 48009 Bilbao, Euskadi, Spain; orcid.org/0000-0002-8893-7089

Oleg V. Prezhdo − Department of Chemistry and Department of Physics and Astronomy, University of Southern California, Los Angeles, California 90007, United States; orcid.org/ 0000-0002-5140-7500

Complete contact information is available at:
https://pubs.acs.org/10.1021/acs.jpclett.3c03621

### Notes
The authors declare no competing financial interest.

## ACKNOWLEDGMENTS
S.A. and O.V.P. acknowledge support from the US Department of Energy (DE-SC0014429). D.J.T. acknowledges support from the U.S. National Science Foundation (ECCS-2138728). D.C. thanks the Spanish Ministry of Science and Innovation (projects MICIN/FEDER PID2022-136231NB-I00 and RED2022-134939-T).

## REFERENCES
(1) Mauter, M. S.; Elimelech, M. Environmental Applications of Carbon-Based Nanomaterials. Environ. Sci. Technol. 2008, 42, 5843−5859.
(2) Wang, X.; Maeda, K.; Thomas, A.; Takanabe, K.; Xin, G.; Carlsson, J. M.; Domen, K.; Antonietti, M. A Metal-Free Polymeric Photocatalyst for Hydrogen Production from Water under Visible light. Nat. Mater. 2009, 8, 76−80.
(3) Zhao, Z.; Sun, Y.; Dong, F. Graphitic Carbon Nitride Based Nanocomposites: A Review. Nanoscale 2015, 7, 15−37.
(4) Zhu, J.; Xiao, P.; Li, H.; Carabineiro, S. A. C. Graphitic Carbon Nitride: Synthesis, Properties, and Applications in Catalysis. ACS Appl. Mater. Interfaces 2014, 6, 16449−16465.
(5) Cao, S.; Low, J.; Yu, J.; Jaroniec, M. Polymeric Photocatalysts Based on Graphitic Carbon Nitride. Adv. Mater. 2015, 27, 2150−2176.
(6) Kessler, F. K.; Zheng, Y.; Schwarz, D.; Merschjann, C.; Schnick, W.; Wang, X.; Bojdys, M. J. Functional Carbon Nitride Materials − Design Strategies for Electrochemical Devices. Nat. Rev. Mater. 2017, 2, 17030.
(7) Jiang, L.; Yuan, X.; Pan, Y.; Liang, J.; Zeng, G.; Wu, Z.; Wang, H. Doping of Graphitic Carbon Nitride for Photocatalysis: A Reveiw. Appl. Catal. B: Environ. 2017, 217, 388−406.
(8) Tay, Q.; Kanhere, P.; Ng, C. F.; Chen, S.; Chakraborty, S.; Huan, A. C. H.; Sum, T. C.; Ahuja, R.; Chen, Z. Defect Engineered G-C3n4 for Efficient Visible Light Photocatalytic Hydrogen Production. Chem. Mater. 2015, 27, 4930−4933.

(9) Makaremi, M.; Grixti, S.; Butler, K. T.; Ozin, G. A.; Singh, C. V. Band Engineering of Carbon Nitride Monolayers by N-Type, P-Type, and Isoelectronic Doping for Photocatalytic Applications. *ACS Appl. Mater. Interfaces* **2018**, *10*, 11143–11151.

(10) Zhou, L.; Zhang, H.; Sun, H.; Liu, S.; Tade, M. O.; Wang, S.; Jin, W. Recent Advances in Non-Metal Modification of Graphitic Carbon Nitride for Photocatalysis: A Historic Review. *Catal. Sci. Technol.* **2016**, *6*, 7002–7023.

(11) Yang, X.-F.; Wang, A.; Qiao, B.; Li, J.; Liu, J.; Zhang, T. Single-Atom Catalysts: A New Frontier in Heterogeneous Catalysis. *Acc. Chem. Res.* **2013**, *46*, 1740–1748.

(12) Mitchell, S.; Vorobyeva, E.; Pérez-Ramírez, J. The Multifaceted Reactivity of Single-Atom Heterogeneous Catalysts. *Angew. Chem., Int. Ed.* **2018**, *57*, 15316–15329.

(13) Kaiser, S. K.; Chen, Z.; Faust Akl, D.; Mitchell, S.; Pérez-Ramírez, J. Single-Atom Catalysts across the Periodic Table. *Chem. Rev.* **2020**, *120*, 11703–11809.

(14) Cheng, N.; Zhang, L.; Doyle-Davis, K.; Sun, X. Single-Atom Catalysts: From Design to Application. *Electrochem. Energy Rev.* **2019**, *2*, 539–573.

(15) Meng, F.; Tian, Z.; Tian, W.; Zhang, H. Advances in Carbon Nitride Supported Single-Atom Photocatalysts for Hydrogen Evolution. *Curr. Opin. Chem. Eng.* **2023**, *41*, No. 100941.

(16) Fu, J.; Wang, S.; Wang, Z.; Liu, K.; Li, H.; Liu, H.; Hu, J.; Xu, X.; Li, H.; Liu, M. Graphitic Carbon Nitride Based Single-Atom Photocatalysts. *Front. Phys.* **2020**, *15*, 33201.

(17) Akinaga, Y.; Kawawaki, T.; Kameko, H.; Yamazaki, Y.; Yamazaki, K.; Nakayasu, Y.; Kato, K.; Tanaka, Y.; Hanindriyo, A. T.; Takagi, M.; Shimazaki, T.; Tachikawa, M.; Yamakata, A.; Negishi, Y. Metal Single-Atom Cocatalyst on Carbon Nitride for the Photocatalytic Hydrogen Evolution Reaction: Effects of Metal Species. *Adv. Funct. Mater.* **2023**, *33*, No. 2303321.

(18) Colombari, F. M.; da Silva, M. A. R.; Homsi, M. S.; de Souza, B. R. L.; Araujo, M.; Francisco, J. L.; da Silva, G. T. S. T.; Silva, I. F.; de Moura, A. F.; Teixeira, I. F. Graphitic Carbon Nitrides as Platforms for Single-Atom Photocatalysis. *Faraday Discuss.* **2021**, *227*, 306–320.

(19) P, S.; John, J.; Rajan, T. P. D.; Anilkumar, G. M.; Yamaguchi, T.; Pillai, S. C.; Hareesh, U. S. Graphitic Carbon Nitride (G-C3n4) Based Heterogeneous Single Atom Catalysts: Synthesis, Character- isation and Catalytic Applications. *J. Mater. Chem. A* **2023**, *11*, 8599–8646.

(20) Gao, G.; Jiao, Y.; Waclawik, E. R.; Du, A. Single Atom (Pd/Pt) Supported on Graphitic Carbon Nitride as an Efficient Photocatalyst for Visible-Light Reduction of Carbon Dioxide. *J. Am. Chem. Soc.* **2016**, *138*, 6292–6297.

(21) Cometto, C.; Ugolotti, A.; Grazietti, E.; Moretto, A.; Bottaro, G.; Armelao, L.; Di Valentin, C.; Calvillo, L.; Granozzi, G. Copper Single-Atoms Embedded in 2d Graphitic Carbon Nitride for the Co2 Reduction. *npj 2D Mater. Appl.* **2021**, *5*, 63.

(22) Liu, X.; Deng, Y.; Zheng, L.; Kesama, M. R.; Tang, C.; Zhu, Y. Engineering Low-Coordination Single-Atom Cobalt on Graphitic Carbon Nitride Catalyst for Hydrogen Evolution. *ACS Catal.* **2022**, *12*, 5517–5526.

(23) Fu, J.; Zhu, L.; Jiang, K.; Liu, K.; Wang, Z.; Qiu, X.; Li, H.; Hu, J.; Pan, H.; Lu, Y.-R.; Chan, T.-S.; Liu, M. Activation of Co2 on Graphitic Carbon Nitride Supported Single-Atom Cobalt Sites. *J. Chem. Eng.* **2021**, *41S*, No. 128982.

(24) Li, J.; Zhao, S.; Yang, S.-Z.; Wang, S.; Sun, H.; Jiang, S. P.; Johannessen, B.; Liu, S. Atomically Dispersed Cobalt on Graphitic Carbon Nitride as a Robust Catalyst for Selective Oxidation of Ethylbenzene by Peroxymonosulfate. *J. Mater. Chem. A* **2021**, *9*, 3029–3035.

(25) Zheng, Y.; Jiao, Y.; Zhu, Y.; Cai, Q.; Vasileff, A.; Li, L. H.; Han, Y.; Chen, Y.; Qiao, S.-Z. Molecule-Level G-C3n4 Coordinated Transition Metals as a New Class of Electrocatalysts for Oxygen Electrode Reactions. *J. Am. Chem. Soc.* **2017**, *139*, 3336–3339.

(26) Runge, E.; Gross, E. K. U. Density-Functional Theory for Time-Dependent Systems. *Phys. Rev. Lett.* **1984**, *52*, 997–1000.

(27) Craig, C. F.; Duncan, W. R.; Prezhdo, O. V. Trajectory Surface Hopping in the Time-Dependent Kohn-Sham Approach for Electron- Nuclear Dynamics. *Phys. Rev. Lett.* **2005**, *95*, No. 163001.

(28) Fischer, S. A.; Habenicht, B. F.; Madrid, A. B.; Duncan, W. R.; Prezhdo, O. V. Regarding the Validity of the Time-Dependent Kohn– Sham Approach for Electron-Nuclear Dynamics Via Trajectory Surface Hopping. *J. Chem. Phys.* **2011**, *134*, No. 024102.

(29) Jaeger, H. M.; Fischer, S.; Prezhdo, O. V. Decoherence-Induced Surface Hopping. *J. Chem. Phys.* **2012**, *137*, No. 22A545.

(30) Akimov, A. V.; Prezhdo, O. V. Pyxaid Program for Non- Adiabatic Molecular Dynamics in Condensed Matter Systems. *J. Chem. Theory Comput.* **2013**, *9*, 4959–4972.

(31) Akimov, A. V.; Prezhdo, O. V. Advanced Capabilities of the Pyxaid Program: Integration Schemes, Decoherence Effects, Multi- excitonic States, and Field-Matter Interaction. *J. Chem. Theory Comput.* **2014**, *10*, 789–804.

(32) Akimov, A. V.; Prezhdo, O. V. Persistent Electronic Coherence Despite Rapid Loss of Electron−Nuclear Correlation. *J. Phys. Chem. Lett.* **2013**, *4*, 3857–3864.

(33) Prezhdo, O. V.; Rossky, P. J. Evaluation of Quantum Transition Rates from Quantum-Classical Molecular Dynamics Simulations. *J. Chem. Phys.* **1997**, *107*, 5863–5878.

(34) Kilina, S. V.; Neukirch, A. J.; Habenicht, B. F.; Kilin, D. S.; Prezhdo, O. V. Quantum Zeno Effect Rationalizes the Phonon Bottleneck in Semiconductor Quantum Dots. *Phys. Rev. Lett.* **2013**, *110*, No. 180404.

(35) Trivedi, D. J.; Prezhdo, O. V. Decoherence Allows Model Reduction in Nonadiabatic Dynamics Simulations. *J. Phys. Chem. A* **2015**, *119*, 8846–8853.

(36) Gumber, S.; Prezhdo, O. V. Zeno and Anti-Zeno Effects in Nonadiabatic Molecular Dynamics. *J. Phys. Chem. Lett.* **2023**, *14*, 7274–7282.

(37) Mukamel, S. *Principles of Nonlinear Optical Spectroscopy*; Oxford University Press: 1999.

(38) Kamisaka, H.; Kilina, S. V.; Yamashita, K.; Prezhdo, O. V. Ultrafast Vibrationally-Induced Dephasing of Electronic Excitations in Pbse Quantum Dot. *Nano Lett.* **2006**, *6*, 2295–2300.

(39) Agrawal, S.; Lin, W.; Prezhdo, O. V.; Trivedi, D. J. Ab Initio Quantum Dynamics of Charge Carriers in Graphitic Carbon Nitride Nanosheets. *J. Chem. Phys.* **2020**, *153*, No. 054701.

(40) Gumber, S.; Agrawal, S.; Prezhdo, O. V. Excited State Dynamics in Dual-Defects Modified Graphitic Carbon Nitride. *J. Phys. Chem. Lett.* **2022**, *13*, 1033–1041.

(41) Agrawal, S.; Vasenko, A. S.; Trivedi, D. J.; Prezhdo, O. V. Charge Carrier Nonadiabatic Dynamics in Non-Metal Doped Graphitic Carbon Nitride. *J. Chem. Phys.* **2022**, *156*, No. 094702.

(42) Trivedi, D. J.; Wang, L.; Prezhdo, O. V. Auger-Mediated Electron Relaxation Is Robust to Deep Hole Traps: Time-Domain Ab Initio Study of Cdse Quantum Dots. *Nano Lett.* **2015**, *15*, 2086–2091.

(43) Wang, L.; Long, R.; Trivedi, D.; Prezhdo, O. V. Time-Domain Ab Initio Modeling of Charge and Exciton Dynamics in Nanoma- terials. In *Green Processes for Nanotechnology: From Inorganic to Bioinspired Nanomaterials*; Basiuk, V. A., Basiuk, E. V., Eds.; Springer International Publishing: Cham, 2015; pp 353–392.

(44) Liu, D. Y.; Perez, C. M.; Vasenko, A. S.; Prezhdo, O. V. Ag-Bi Charge Redistribution Creates Deep Traps in Defective Cs2Agbibr6: Machine Learning Analysis of Density Functional Theory. *J. Phys. Chem. Lett.* **2022**, *13*, 3645–3651.

(45) Ran, J. Y.; Wang, B. P.; Wu, Y. F.; Liu, D. Y.; Perez, C. M.; Vasenko, A. S.; Prezhdo, O. V. Halide Vacancies Create No Charge Traps on Lead Halide Perovskite Surfaces but Can Generate Deep Traps in the Bulk. *J. Phys. Chem. Lett.* **2023**, *14*, 6028–6036.

(46) Giri, A.; Walton, S. G.; Tomko, J.; Bhatt, N.; Johnson, M. J.; Boris, D. R.; Lu, G. Y.; Caldwell, J. D.; Prezhdo, O. V.; Hopkins, P. E. Ultrafast and Nanoscale Energy Transduction Mechanisms and Coupled Thermal Transport across Interfaces. *ACS Nano* **2023**, *17*, 14253–14282.

(47) Li, W.; Xue, T.; Mora-Perez, C.; Prezhdo, O. V. Ab Initio Quantum Dynamics of Plasmonic Charge Carriers. *Trends Chem.* 2023, **5**, 634−645.

(48) Xu, C.; Zhou, G. Q.; Alexeev, E. M.; Cadore, A. R.; Paradisanos, I.; Ott, A. K.; Soavi, G.; Tongay, S.; Cerullo, G.; Ferrari, A. C.; Prezhdo, O. V.; Loh, Z. H. Ultrafast Electronic Relaxation Dynamics of Atomically Thin Mos2 Is Accelerated by Wrinkling. *ACS Nano* 2023, **17**, 16682−16694.

(49) Zhou, Z. B.; Zheng, Z. F.; He, J. J.; Wang, J. L.; Prezhdo, O. V.; Frauenheim, T. Ultrafast Laser Control of Antiferromagnetic- Ferrimagnetic Switching in Two-Dimensional Ferromagnetic Semi- conductor Heterostructures. *Nano Lett.* 2023, **23**, 5688−5695.

(50) Li, L. Q.; Long, R.; Prezhdo, O. V. Why Chemical Vapor Deposition Mos < Sub < Sub > 2</Sub > Samples Outperform Physical Vapor Deposition Samples: Time-Domain Ab Initio Analysis. *Nano Lett.* 2018, **18**, 4008−4014.

(51) Prezhdo, O. V. Multiple Excitons and the Electron-Phonon Bottleneck in Semiconductor Quantum Dots:: An Ab Initio Perspective. *Chem. Phys. Lett.* 2008, **460**, 1−9.

(52) Wang, L. J.; Prezhdo, O. V.; Beljonne, D. Mixed Quantum- Classical Dynamics for Charge Transport in Organics. *Phys. Chem. Chem. Phys.* 2015, **17**, 12395−12406.

(53) Kresse, G.; Hafner, J. Ab Initio Molecular Dynamics for Liquid Metals. *Phys. Rev. B* 1993, **47**, 558−561.

(54) Kresse, G.; Hafner, J. Ab Initio Molecular-Dynamics Simulation of the Liquid-Metal-Amorphous-Semiconductor Transition in Germanium. *Phys. Rev. B* 1994, **49**, 14251−14269.

(55) Kresse, G.; Furthmüller, J. Efficient Iterative Schemes for Ab Initio Total-Energy Calculations Using a Plane-Wave Basis Set. *Phys. Rev. B* 1996, **54**, 11169−11186.

(56) Perdew, J. P.; Burke, K.; Ernzerhof, M. Generalized Gradient Approximation Made Simple. *Phys. Rev. Lett.* 1996, **77**, 3865−3868.

(57) Haase, F. T.; Bergmann, A.; Jones, T. E.; Timoshenko, J.; Herzog, A.; Jeon, H. S.; Rettenmaier, C.; Cuenya, B. R. Size Effects and Active State Formation of Cobalt Oxide Nanoparticles During the Oxygen Evolution Reaction. *Nat. Energy* 2022, **7**, 765−773.

(58) Farkaš, B.; Santos-Carballal, D.; Cadi-Essadek, A.; de Leeuw, N. H. A Dft+U Study of the Oxidation of Cobalt Nanoparticles: Implications for Biomedical Applications. *Materialia* 2019, **7**, No. 100381.

(59) Perdew, J. P. Density Functional Theory and the Band Gap Problem. *Int. J. Quantum Chem.* 1985, **28**, 497−523.

(60) Krukau, A. V.; Vydrov, O. A.; Izmaylov, A. F.; Scuseria, G. E. Influence of the Exchange Screening Parameter on the Performance of Screened Hybrid Functionals. *J. Chem. Phys.* 2006, **125**, No. 224106.

(61) Klimeš, J.; Bowler, D. R.; Michaelides, A. Van Der Waals Density Functionals Applied to Solids. *Phys. Rev. B* 2011, **83**, No. 195131.

(62) Momma, K.; Izumi, F. Vesta 3 for Three-Dimensional Visualization of Crystal, Volumetric and Morphology Data. *J. Appl. Crystallogr.* 2011, **44**, 1272−1276.

(63) Chu, W.; Prezhdo, O. V. Concentric Approximation for Fast and Accurate Numerical Evaluation of Nonadiabatic Coupling with Projector Augmented-Wave Pseudopotentials. *J. Phys. Chem. Lett.* 2021, **12**, 3082−3089.

(64) Chu, W. B.; Zheng, Q. J.; Akimov, A. V.; Zhao, J.; Saidi, W. A.; Prezhdo, O. V. Accurate Computation of Nonadiabatic Coupling with Projector Augmented-Wave Pseudopotentials. *J. Phys. Chem. Lett.* 2020, **11**, 10073−10080.

(65) Gao, Q.; Zhuang, X.; Hu, S.; Hu, Z. Corrugation Matters: Structure Models of Single Layer Heptazine-Based Graphitic Carbon Nitride from First-Principles Studies. *J. Phys. Chem. C* 2020, **124**, 4644−4651.

(66) Chen, Z.; Zhao, J.; Cabrera, C. R.; Chen, Z. Computational Screening of Efficient Single-Atom Catalysts Based on Graphitic Carbon Nitride (G-C3n4) for Nitrogen Electroreduction. *Small Methods* 2019, **3**, No. 1800368.

(67) Liu, W.; Cao, L.; Cheng, W.; Cao, Y.; Liu, X.; Zhang, W.; Mou, X.; Jin, L.; Zheng, X.; Che, W.; Liu, Q.; Yao, T.; Wei, S. Single-Site Active Cobalt-Based Photocatalyst with a Long Carrier Lifetime for Spontaneous Overall Water Splitting. *Angew. Chem., Int. Ed.* 2017, **56**, 9312−9317.

(68) Chu, C.; Zhu, Q.; Pan, Z.; Gupta, S.; Huang, D.; Du, Y.; Weon, S.; Wu, Y.; Muhich, C.; Stavitski, E.; Domen, K.; Kim, J.-H. Spatially Separating Redox Centers on 2d Carbon Nitride with Cobalt Single Atom for Photocatalytic H2O2 Production. *Proc. Natl. Acad. Sci. U. S. A.* 2020, **117**, 6376−6382.

(69) Wang, S. S.; Huang, M. L.; Wu, Y. N.; Chu, W. B.; Zhao, J.; Walsh, A.; Gong, X. G.; Wei, S. H.; Chen, S. Y. Effective Lifetime of Non-Equilibrium Carriers in Semiconductors from Non-Adiabatic Molecular Dynamics Simulations. *Nat. Comput. Sci.* 2022, **2**, 486.

(70) Zhang, L.; Luo, Q.; Hu, S.; Hu, Z.; Zhang, W.; Yang, J. Enhanced Electron−Hole Separation in Phosphorus-Coordinated Co Atom on G-C3n4 toward Photocatalytic Overall Water Splitting. *J. Phys. Chem. Lett.* 2022, **13**, 11961−11967.