
# Thermoelectric properties of cement composite analogues from first principles calculations

Esther Orisakwe, \( ^{1,*} \)  Conrad Johnston, \( ^{2} \)  Ruchita Jani, \( ^{3} \)  Xiaoli

Liu, \( ^{4,5} \)  Lorenzo Stella, \( ^{1,6} \)  Jorge Kohanoff, \( ^{7,1} \)  Niall Holmes, \( ^{3} \)  Brian

Norton, \( ^{3,8,9} \)  Ming Qu, \( ^{4} \)  Hongxi Yin, \( ^{10} \)  and Kazuaki Yazawa \( ^{11} \) 

 \( ^{1} \) School of Mathematics and Physics, Queen's University Belfast, UK

 \( ^{2} \) Pacific Northwest National Laboratory, Richland, WA, USA

 \( ^{3} \) School of Civil and Structural Engineering,

Technological University Dublin, Ireland

 \( ^{4} \) Lyles School of Civil Engineering, Purdue University, West Lafayette, IN, USA

 \( ^{5} \) Multifunctional Equipment Integration Group,

Oak Ridge National Laboratory, Oak Ridge, TN, USA

 \( ^{6} \) School of Chemistry and Chemical Engineering, Queen's University Belfast, UK

 \( ^{7} \) Instituto de Fusion Nuclear “Guillermo Velarde”,

Universidad Politecnica de Madrid, Spain

 \( ^{8} \) University College Cork, Ireland

 \( ^{9} \) Tyndall National Institute, Cork, Ireland

 \( ^{10} \) Center for Energy, Environment & Sustainability,

Washington University in St Louis (WUST), St Louis, MO, USA

 \( ^{11} \) Birck Nanotechnology Center, Purdue University, West Lafayette, IN, USA

(Dated: December 1, 2022)
 

## Abstract

Buildings are responsible for a considerable fraction of the energy wasted globally every year, and as a result, excess carbon emissions. While heat is lost directly in colder months and climates, resulting in increased heating loads, in hot climates cooling and ventilation is required. One avenue towards improving the energy efficiency of buildings is to integrate thermoelectric devices and materials within the fabric of the building to exploit the temperature gradient between the inside and outside to do useful work. Cement-based materials are ubiquitous in modern buildings and present an interesting opportunity to be functionalised. We present a systematic investigation of the electronic transport coefficients relevant to the thermoelectric materials of the calcium silicate hydrate (C-S-H) gel analogue, tobermorite, using Density Functional Theory calculations with the Boltzmann transport method. The calculated values of the Seebeck coefficient are within the typical magnitude (200 - 600  \( \mu V/K \) ) indicative of a good thermoelectric material [1]. The tobermorite models are predicted to be intrinsically p-type thermoelectric material because of the presence of large concentration of the Si-O tetrahedra sites. The calculated electronic ZT for the tobermorite models have their optimal values of 0.983 at (400 K and  \( 10^{17} \)  cm \( ^{-3} \) ) for tobermorite 9 Å, 0.985 at (400 K and  \( 10^{17} \)  cm \( ^{-3} \) ) for tobermorite 11 Å and 1.20 at (225 K and  \( 10^{19} \)  cm \( ^{-3} \) ) for tobermorite 14 Å, respectively.

## I. INTRODUCTION

On a global basis, more than 60% of the energy consumed is ultimately lost via heat to the environment \( ^{[2]} \) . It was reported that buildings contribute somewhere between 20 to 40% of the globally generated energy and energy related environmental emissions, with a sizeable amount of this energy going towards heating and cooling requirements of buildings  \( [3] \) . The overwhelming influence of climate change as well as the increasing energy demand in urban areas calls for more buildings to maximise their potential energy harvesting, distribution, storage and efficient usage  \( [4, 5] \) . Thermoelectric (TE) units can make use of the unavoidable losses to generate free electric power, because of their ability to partially recover heat by converting it into electricity  \( [6, 7] \) .

In thermoelectric materials, a temperature gradient leads to a movement of charge carriers,  \( ^{*} \)  e.orisakwe@qub.ac.uk; estherorisakwe@gmail.com
 

which results into a difference of potential at the two ends of an open circuit. In this way, thermal energy can be partially converted into electrical energy with a finite efficiency ultimately bounded by the second low of the thermodynamics. A quick estimate of the energy conversion efficiency of a thermoelectric material is given by the dimensionless figure of merit,  \( ZT^{[8]} \) :

 \[ Z T=\frac{S^{2}\sigma}{\kappa}T, \quad (1) \] 

where S is the Seebeck coefficient,  \( \sigma \)  is the electrical conductivity, T is the absolute temperature, and the total thermal conductivity  \( \kappa = \kappa_{e} + \kappa_{l} \)  is made up of contributions from charge carriers  \( \kappa_{e} \)  and lattice vibrations  \( \kappa_{l} \) . To maximise the figure of merit, the Seebeck coefficient and electrical conductivity must be maximised, while at the same time, the thermal conductivity must be minimised \( ^{[9, 10]} \) . In the limit of  \( ZT \rightarrow \infty \) , the efficiency of a Carnot engine is retrieved. For practical applications, a figure of merit  \( ZT \gg 1 \)  is typically required \( ^{[11]} \) .

Cementitious materials are complex heterogeneous composites formed by the admixture of calcareous (mostly calcium carbonate) material such as limestone with silica-, alumina- and iron-based material, which are calcinated until they fuse together. Cement-based materials like concrete are not only used as structural materials for buildings, but also for other applications like nuclear waste disposal and massive structures like water reservoirs and dams  \( [12, 13] \) .

In recent years, attention has turned to composite cement-based materials. One such composite, carbon fiber reinforced cement (CFRC), has ignited great interest in the scientific community as a promising thermoelectric material \( ^{[14]} \) . While standard cement formulations show only a mild thermoelectric effect  \( [15–20] \) , the inclusion of additives such as carbon and steel fibers, inorganic compounds like graphite and/or metallic oxides such as ZnO,  \( Bi_{2}O_{3} \)  or  \( Fe_{2}O_{5} \) , or standard thermoelectric materials like  \( Bi_{2}Te_{3} \) , can enhance the thermometric performance considerably. The challenges and opportunities presented by these composite materials have been discussed extensively in the literature  \( [21–28] \) , and in a recent review \( ^{[29]} \) . While rapid progress has been made in improving the Seebeck coefficient within CFRCs, the overall figure of merit has not been improved due, understandably, to reportedly small values of electrical conductivity.

The most important hydration product of cementitious materials is Calcium-Silicate-Hydrate gel, denoted C-S-H within the cement chemistry community, where C=CaO, S=SiO \( _{2} \)  and
 

H=H_{2}O [30]. C-S-H gel has an average calcium to silicon (Ca/Si) ratio of 1.7 [30], with local Ca/Si ratio fluctuations of 0.67 to 2.0 [31]. The description of the microscopic structure of cement is particularly complex due to the disordered and inhomogeneous nature of the material, which comprises several coexisting phases like alite, belite, etc [32]. After the work of Taylor [13], the consensus is that C-S-H based materials have a layered atomic structure akin to those of tobermorite, T14Å [Ca_{5}Si_{6}O_{16}(OH)_{2}.7H_{2}O] and jennite [Ca_{9}Si_{6}O_{18}(OH)_{6}.8H_{2}O], with a calcium to silicon ratio of 0.83 and 1.5, respectively[33]. Tobermorite minerals are generally characterized by their interlayer spacing and are named accordingly as tobermorite, T9Å, tobermorite, Tl1Å and tobermorite, T14Å [34]. Extensive structural characterization via XRD experiments of C-S-H based materials has been carried out by the group of Merlin and Bonaccorsi [35–38]. So far the first principles density functional theory calculations carried out on the C-S-H based materials such as jennite structure and tobermorite minerals has been centered around the understanding of their structural properties [33, 39], elastic constants [33, 39, 40] and anisotropic effect[33], average mechanical properties [33, 39], vibrational properties and infrared spectra [40] and/or NMR shift investigations [34]. Recently, some properties of C-S-H within the context of the civil nuclear industry have been assessed, like its ability to trap and hold radioactive fission products like Sr and its daughters [41, 42], and hydrogen gas production as a consequence of irradiation [43]. Since the C-S-H gel is responsible for the cohesive strength and durability of cementitious materials [44, 45], our drive is to optimize the thermoelectric transport coefficient of some C-S-H based tobermorite materials with the aim of improving their energy efficiency.

Motivated by the experimental results on cement-based materials, we present here first-principles calculations of the structural and electronic transport properties of the C-S-H analogs tobermorite, T9Å  \( [Ca_{5}Si_{6}O_{16}(OH)_{2}] \) , tobermorite, T11Å  \( [Ca_{4}Si_{6}O_{15}(OH)_{2}.5H_{2}O] \) , and tobermorite, T14Å  \( [Ca_{5}Si_{6}O_{16}(OH)_{2}.7H_{2}O] \)  as shown in Fig. 1. We are mainly interested in the thermoelectric properties in the low temperature regime since most of the experiments have been carried out at temperatures below 100 °C. In particular, we focus on the effects of temperature and doping on electrical and thermal conductivity, Seebeck coefficient, power factor, and figure of merit. In this work, doping is modelled in terms of an intrinsic carrier concentration determined by the electronic chemical potential via the rigid band model. To the best of our knowledge, until now no calculations have been performed to understand the thermoelectric behavior of calcium silicate hydrate (C-S-H)-based materials.
 

Our initial first-principles study can guide further investigations of the electronic transport properties of this class of materials.

## II. COMPUTATIONAL METHODS

## A. Details of electronic structure calculations

All our calculations were carried out within the framework of density functional theory (DFT) [46, 47] using a plane wave basis set as implemented in the open-source package Quantum ESPRESSO [48]. All structural optimizations and electronic property calculations were carried out using the Perdew-Burke-Ernzerhof (PBE) [49] exchange-correlation functional belonging to the generalized gradient approximation (GGA) family [50]. Ultra-soft pseudopotentials [51] were used and along with a plane wave basis with an energy cutoff of 70 Ry and density cutoff of 560 Ry for T9Å  \( [Ca_{5}Si_{6}O_{16}(OH)_{2}] \)  while energy cutoff of 80 Ry and density cutoff 640 Ry was used for T11Å  \( [Ca_{4}Si_{6}O_{15}(OH)_{2}.5H_{2}O] \)  and T14Å  \( [Ca_{5}Si_{6}O_{16}(OH)_{2}.7H_{2}O] \) , respectively. The Brillouin zone was sampled using the Monkhorst-Pack scheme [52], with a regular mesh of  \( 3\times3\times3 \)  for T9Å and T11Å, and  \( 3\times3\times1 \)  for T14Å. Electronic occupations were smeared using the Marzari-Vanderbilt scheme with broadening of 0.03 Ry [53] and the SCF convergence threshold for the electronic wavefunctions was set to  \( 10^{-10} \)  Ry for both the variable-cell and ionic relaxation. Both jennite and tobermorite models have layered structures, with layers bound by non-bonded interactions [33]. To include the effect of these interactions and obtain realistic interlayer distances during lattice constant optimization, the semiempirical dispersion correction of Grimme et al. [54] for the PBE functional (DFT-D3) was used. Atomic positions and cell parameters were fully optimized at 0 K using the Broyden-Fletcher-Goldfarb-Shanno method [55–58]. We optimized all stress and force components to less than 0.5 kbar and  \( 10^{-6} \)  Ry/Bohr, respectively.

Finally we performed a single point energy calculation in order to ensure the robustness of our results with much denser k-point grid of  \( 5 \times 5 \times 3 \)  for all the tobermorite models. Since the electronic transport coefficients are strongly dependent on the band structure energies in the Brillouin zone, we performed non-self consistent calculations for all the tobermorite models using  \( 9 \times 9 \times 3 \)  Monkhorst-Pack k-points grid (365 k-points in the irreducible Brillouin zone), while maintaining the energy criterion above. These non-SCF calculations were used
 

to obtain the band structures and transport coefficients of the tobermorite models.

## B. Transport Calculations

Electronic transport coefficients were computed from the solution of the linearized Boltzmann transport equation in conjunction with the rigid-band approximation (RBA) and constant relaxation time approximations (CRTA) [59, 60] as implemented in the BoltzTraP code.[61] In the rigid band approximation, it is assumed that only the chemical potential, not the band shape of the host compound, is changed according to the nominal doping and/or temperature. Hence, only the band energies are extrapolated for each calculation [62]. The electronic band energies of all the tobermorite models were calculated on a  \( 9 \times 9 \times 90 \)  Monkhorst-Pack k-point grid and Fourier interpolated over a denser grid containing 15 times as many k-points for better numerical evaluation of the integrals, to obtain the thermoelectric transport coefficients. In the semi-classical Boltzmann approach, the energy-dependent transport distribution function - the kernel of all transport coefficients [61, 63–66] is expressed as:

 \[ \Sigma_{\alpha\beta}(\epsilon)=\frac{q^{2}}{V}\sum_{i k}\tau_{i k}v_{\alpha}(i,k)v_{\beta}(i,k)\delta(\epsilon-\epsilon(i,k)), \quad (2) \] 

where  \( \alpha \)  and  \( \beta \)  are Cartesian components and the subscripts i and k are the band and wave vector indices, respectively. V is the unit cell volume,  \( \epsilon(i,k) \)  represents the k-dependent band energies, q is the electron charge,  \( \tau_{ik} \)  is the relaxation time and  \( v_{\alpha}(i,k) \)  is the  \( \alpha \)  component of the electron group velocity written as:

 \[ v_{\alpha}(k)=\frac{1}{\bar{\mu}}\frac{\partial\epsilon(i,k)}{\partial k_{\alpha}}. \quad (3) \] 

The advantage of the RBA in conjunction with the CTRA, is that the transport distribution function  \( \Sigma_{\alpha\beta}(\epsilon) \)  does not depend on either temperature T or electron chemical potential (doping)  \( \mu \) . Therefore, by integrating over a fixed transport distribution function,  \( \Sigma_{\alpha\beta}(\epsilon) \) , the doping and/or temperature-dependent generalised transport coefficient of the p-th order, which is solely due to the Fermi-Dirac distribution function  \( f_{0} \)  is obtained as:

 \[ L^{p}(\mu,T)=\int\Sigma_{\alpha\beta}(\mu,T)(\epsilon(i,k)-\mu)^{p}\left(-\frac{\delta f_{0}(\epsilon,\mu,T)}{\delta\epsilon}\right)\delta\epsilon, \quad (4) \] 

From where the electrical conductivity  \( \sigma \) , Seebeck coefficient S, and electronic thermal conductivity  \( \kappa_{e} \)  are extracted as a function of temperature, T, and electronic chemical
 

potential,  \( \mu \) . These transport coefficients are written as:

 \[ \sigma(\mu,T)=\frac{1}{V}\int\Sigma_{\alpha\beta}(\mu,T)\left(-\frac{\partial f_{0}(\epsilon,\mu,T)}{\partial\epsilon}\right)d\epsilon, \quad (5) \] 

 \[ S(\mu,T)=\frac{1}{VqT\sigma(\mu,T)}\int\Sigma_{\alpha\beta}(\mu,T)(\epsilon-\mu)\left(-\frac{\partial f_{0}(\epsilon,\mu,T)}{\partial\epsilon}\right)d\epsilon, \quad (6) \] 

and

 \[ \kappa_{e}(\mu,T)=\frac{1}{VT}\int\Sigma_{\alpha\beta}(\mu,T)(\epsilon-\mu)^{2}\left(-\frac{\partial f_{0}(\epsilon,\mu,T)}{\partial\epsilon}\right)d\epsilon-T S^{2}\sigma \quad (7) \] 

At zero temperature,  \( \mu \)  is equal to the Fermi energy,  \( E_{F} \) . At fixed doping, the chemical potential steadily deviates from  \( E_{F} \)  with increasing temperature as a result of the energy dependence of the density of states [65]. The electrical conductivity is related to the electronic thermal conductivity  \( \kappa_{e} \)  through the Wiedemann-Franz law,  \( \kappa_{e} = L\sigma T \) , where L is the Lorenz number [8]. The electrical conductivity is given as a function of  \( \tau(i,k) \)  (Eq. 2) and, therefore, the relaxation time  \( \tau \)  must be included as a parameter.

To obtain  \( \tau \) , one needs to calculate the scattering of electrons by ionized impurities, piezoelectric scattering, and/or acoustic phonon scattering by deformation [67]. From Eq. 2, it follows that  \( \tau \propto (\epsilon - \epsilon(i,k))^{r-1/2} \) , which sometimes has been used to understand the electron transport processes but has not been established in many materials [65]. For a simple parabolic band model,  \( \tau \)  is expressed as a power-law in a reduced carrier energy  \( \eta = E_{F}/k_{B}T \) ,  \( \tau \propto \epsilon^{r-1/2} \) , where r is the scattering parameter [65, 68]. Within the rigid-band approximation,  \( \tau \)  is typically assumed to be energy-independent and constant for simplicity [61, 69]. In this case,  \( \tau \)  cancels out in the expression for the Seebeck coefficient, which is one of the key quantities for the thermoelectric figure of merit, ZT. The calculated transport coefficients form the essential part of the figure of merit ZT, which can be rearranged as:

 \[ Z T=\frac{S^{2}\sigma}{}\frac{T}{\kappa_{e}}\left(\frac{\kappa_{e}}{\kappa_{e}+\kappa_{l}}\right) \quad (8) \] 

Two contributions to ZT can be identified in Eq. (8): (i) the electronic figure of merit  \( (Z_{e}T = S^{2}\sigma T/\kappa_{e}) \) , which is independent of the relaxation time and obtained when the heat transferred to the material through lattice vibrations  \( (\kappa_{l}) \)  is completely neglected; and (ii) a scaling factor determined by the ratio of  \( \kappa_{e}/(\kappa_{e} + \kappa_{l}) \) . The electronic figure of merit  \( Z_{e}T \)  approaches ZT when  \( \kappa_{l} \)  becomes much smaller than  \( \kappa_{e} \) . Note that the final thermoelectric transport coefficients were evaluated from their averaged trace components.
 

## III. RESULTS AND DISCUSSION

## A. Structural details of Tobermorite models

A representation of the different tobermorite crystal structures (T9Å, T11Å and T14Å) is shown in Fig. 1. These layered tobermorite minerals share similar structural arrangements, but are distinguished by the interlayer spacing distance. The notation 9Å, 11Å and 14Å indicates the characteristic interlayer spacings of 0.93 nm, 1.13 nm and 1.4 nm. This spacing is affected by the degree of hydration, a property that changes through heating. Each layer consists of continuous seven-fold edge-sharing Ca-O polyhedra stretched along the b-direction. All the oxygen atoms of the polyhedra are shared with silicon atoms to form corner-sharing  \( [SiO_{4}]^{4-} \)  tetrahedra chains. These chains are either dreierketten or wollastonite-like type [70, 71] with repeating units of three-fold tetrahedra. Two of the tetrahedra chains share edges with the Ca-polyhedron in a paired form while the third tetrahedra chain is linked to the calcium polyhedra through their apical oxygen atoms in a bridging form. Interlayer calcium polyhedra are present in all three tobermorite models. In T11Å and T14Å the interlayer spacing is filled with water molecules and additional calcium atoms. T11Å and T14Å are both different from T9Å because of the formation of double (condensed) dreierketten bridging silicate chains [35–37]. Single tetrahedra silicate chains were also reported by Hamid [72] for tobermorite 11 Å with differing calcium to silicon (Ca/Si) ratios of 0.67, 0.83 and 1.0.

Experimental lattice parameters and atomic positions for T9Å (riverside), T11Å (tobermorite) and T14Å (plombierite) were obtained from the American Mineralogist Crystal Structure Database [73]. These materials crystallize in triclinic (space group C \( \overline{1} \) ), monoclinic (space group of B11m) and monoclinic (space groups B11b) Bravais lattices containing 62, 88, and 104 atoms per unit cell, respectively.

The parent compound of tobermorite T11 Å and T14 Å shows partial occupancy for water/oxygen (WO) sites in its experimentally determined unit cell structure (i.e., the Crystallographic Information File just has WO, as it from XRD), which hinders a direct description via simulation. Refining atomic positions of the parent compound of T11Å and T14Å, leads to a breakdown in the nominal monoclinic symmetry to P1 trinclinic Bravais lattice. The angles and lattice vectors were fixed to that of the parent compound, which were used as
 
![](./images/867748054407577723_1.jpg)

FIG. 1. Layered crystal structure of tobermorite mineral: (a) T9Å (Ca_{5}Si_{6}O_{16}(OH)_{2}), (b) T11Å (Ca_{4}Si_{6}O_{15}(OH)_{2}.5H_{2}O) and (c) T14Å (Ca_{5}Si_{6}O_{16}(OH)_{2}.7H_{2}O). The large grey spheres represent calcium atoms, red spheres represent oxygen atoms, and white spheres represent the hydrogen atoms, respectively. The silicate tetrahedra are represented in blue, with the silicon atoms located in the center of the tetrahedra.
 

inputs for structural optimization. The calculated structural parameters are explicitly listed in Table I. All parameters were determined using the DFT-D3 method to correct for dispersion interactions, and are compared with the available experimental data and previous DFT calculations in Table I. The good agreement in the calculated lattice parameters rela-

TABLE I. Calculated (in italics) cell parameters of the tobermorite models. Experimentally measured values, GGA+vdW (in bold italics) and DFT-GGA values are shown for comparison. The calculated band gaps and those obtained from DFT-LDA are also listed.

<table><tr><td></td><td>Tobermorite 9 Å (Ca5Si6O16(OH)2) Expt. Calc.</td><td>Tobermorite 11 Å (Ca4Si6O15(OH)2.5H2O) Expt. Calc.</td><td>Tobermorite 14 Å (Ca5Si6O16(OH)2.7H2O) Expt. Calc.</td></tr><tr><td rowspan="3">a(Å)</td><td>11.16 a 11.19</td><td>6.74 b 6.83</td><td>6.74 c 6.80</td></tr><tr><td>11.21 d</td><td>6.80 d</td><td>6.87 d</td></tr><tr><td>11.27(11.22) f</td><td>6.82 e</td><td>6.64 e</td></tr><tr><td rowspan="4">b(Å)</td><td>7.30 a 7.32</td><td>7.39 b 7.48</td><td>7.43 c 7.43</td></tr><tr><td>7.39 d</td><td>7.51 d</td><td>7.43 d</td></tr><tr><td>7.38(7.35) f</td><td>7.47 e</td><td>7.41 e</td></tr><tr><td>7.38(7.35) f</td><td>7.48(7.44) f</td><td></td></tr><tr><td rowspan="4">c(Å)</td><td>9.57 a 9.53</td><td>22.49 b 22.72</td><td>27.99 c 28.00</td></tr><tr><td>9.71 d</td><td>22.57 d</td><td>28.49 d</td></tr><tr><td>9.71(9.61) f</td><td>22.70 e</td><td>28.18 e</td></tr><tr><td>9.71(9.61) f</td><td>22.72(22.60) f</td><td></td></tr><tr><td rowspan="4">α(°)</td><td>101.08 a 99.47</td><td>90 b 90.45</td><td>90 c 89.94</td></tr><tr><td>102.65 d</td><td>89.83 d</td><td>89.96 d</td></tr><tr><td>102.58(101.63) f</td><td>90 e</td><td>90 e</td></tr><tr><td>102.58(101.63) f</td><td>90(90) f</td><td></td></tr><tr><td rowspan="4">β(°)</td><td>92.83 a 92.27</td><td>90 b 90.01</td><td>90 c 90.03</td></tr><tr><td>92.54 d</td><td>89.05 d</td><td>90.05 d</td></tr><tr><td>92.01(92.23) f</td><td>90 e</td><td>89.99 e</td></tr><tr><td>92.01(92.23) f</td><td>90(90) f</td><td></td></tr><tr><td rowspan="4">γ(°)</td><td>89.98 a 90.60</td><td>123.25 b 123.13</td><td>123.25 c 123.93</td></tr><tr><td>89.75 d</td><td>123.43 d</td><td>123.47 d</td></tr><tr><td>89.75(90.34) f</td><td>123.22 e</td><td>121.66 e</td></tr><tr><td>89.75(90.34) f</td><td>123.57(123.63) f</td><td></td></tr><tr><td>Egap(eV)</td><td>4.52(4.6) g</td><td>4.10(4.2) g</td><td>4 04(4.0) g</td></tr></table>

 \( ^{a} \) Ref. [35],  \( ^{b} \) Ref. [36],  \( ^{c} \) Ref. [37],  \( ^{d} \) Ref. [39],  \( ^{e} \) Ref. [40],  \( ^{f} \) Ref.[33],  \( ^{g} \) Ref.[74]

tive to the available experimental values and the results cited in previous DFT calculations
 

(deviation  \( \pm1\% \)  overall) gives confidence in the relaxed tobermorite structures. In T11Å and T14Å, there is a small deviation in the angles  \( \alpha \)  and  \( \beta \)  from the experimental measured values because of the symmetry breakdown mentioned above.

## B. Electronic structure calculations

Accurate electronic structure calculations were carried out to obtain the transport properties. These calculations were performed using the relaxed cell parameters listed in Table I. The calculated band structures of the tobermorite models along some high symmetry paths for triclinic lattices  \( [75] \)  are presented in Fig. 2.

The tobermorite models are insulators and generally expected to have wide energy band gaps. The band structures of all the tobermorite models showed a direct energy band gap at the  \( \Gamma \) -point. The resulting gaps ( \( E_{gap} \) ) listed in the last row of Table I, i.e. 4.6 eV, 4.2 eV and 4.0 eV for T9Å, T11Å and T14Å, respectively, were found to be in very good agreement with previous DFT-LDA results [74].

Our band structure calculations showed that as the water content increases in T11Å and T14Å structures, their band gaps decrease as compared to T9Å, which contains no water molecules. Most of the bands near the valence band maximum (VBM) are flatter (heavy bands) than the bands near the conduction band minimum (CBM), which indicate larger effective mass for the holes than for the electrons. The resulting heavy bands near the VBM should lead to a large Seebeck coefficient in p-type thermoelectric materials. It is interesting to note that the conduction bands (Fig. 2) of the tobermorite models exhibit obvious parabolic character, which suggests that their transport properties can also be modeled using the simple parabolic band approach.

To gain a better understanding of the nature of the states in the VBM and CBM, we have plotted the element-resolved partial density of states (pDOS) of the unit cells of T9Å, T11Å and T14Å, respectively, as shown in Fig. 2. The sharp peaks in the electronic density of states below the Fermi level for all three compounds originate almost entirely from the non-water O states, with small contributions from the water O-H bonds, Si, Ca and H₂O states, respectively. From Fig. 2, it can be seen that non-water oxygen O-p states contribute significantly to the pDOS between -8.5 eV to -2.0 eV, hybridizing with the Si-p states and forming strong covalent bonds that lead to the formation of SiO₄ tetrahedra. The Ca-p
 

states exhibit a relatively small contribution to the density of states (from -7 eV to -3 eV), which indicates a negligible contribution of the alkaline-earth metal to the covalent bond but stresses the ionic bonding within the interlayer calcium polyhedra. This ionic bond character is greater in  \( T9\mathring{A} \)  than in  \( T11\mathring{A} and T14\mathring{A} \)  models due to the absence of  \( H_{2}O \)  molecules. The hybridized pDOS is expected to be beneficial to the electronic transport properties. In the tobermorite models, the water molecules are confined to the interlayer region and interact in the sense of hybridising with all other elements within the crystal. The peak in the lower valence band composed mainly of the Ca-s states was observed to make significant contributions from -24 eV to -20 eV and their interaction with the non-water O contributes to the ionic bonding within the interlayers of Ca-O polyhedra. Turning to the conduction bands, the Ca and Si states dominate the conduction band minimum. These bands were observed to be generally more dispersive than those found in the valence bands. Dispersive bands are considered to contribute to high electron mobility because of the small effective mass of the carriers.

## C. Electronic transport properties

## Seebeck Coefficient

Within the constant relaxation time approximation (CRTA), the Seebeck coefficient S is independent of  \( \tau \) . Without any adjustable parameters, S results exclusively from a first principles electronic structure calculation [8]. For a parabolic band model of a wide band-gap or non-degenerate semiconductor, the Seebeck coefficient is given by [76, 77]:

 \[ S=\pm\frac{k_{B}}{q}\left[\eta-\left(r+\frac{5}{2}\right)\right], \quad (9) \] 

where  \( \eta \)  is the reduced carrier energy, r is the scattering parameter, q is the electron charge and  \( k_{B} \)  is the Boltzmann constant. Fig. 3 shows the temperature dependence of the averaged Seebeck coefficient of all tobermorite models for different values of carrier concentrations ranging from  \( 10^{17} \)  to  \( 10^{21} \)  cm \( ^{-3} \) . These calculations were performed for both the p-type and n-type doping. The averaged Seebeck coefficient is a conductivity-weighted average of its directional components [78]:

 \[ S_{a v g}=\frac{S_{a}\sigma_{a}+S_{b}\sigma_{b}+S_{c}\sigma_{c}}{\sigma_{a}+\sigma_{b}+\sigma_{c}}, \quad (10) \]
 
![](./images/867748054407577723_2.jpg)

(a)

![](./images/867748054407577723_3.jpg)

(b)

![](./images/867748054407577723_4.jpg)

(c)

![](./images/867748054407577723_5.jpg)

(d)

![](./images/867748054407577723_6.jpg)

(e)

![](./images/867748054407577723_7.jpg)

FIG. 2. Calculated electronic band structures and partial density of states per element in the unit cells of T9Å (a and b), T11Å (c,d) and T14Å(e,f). The Fermi energy level  \( E_{f} \)  is set at the zero mark and lies in the middle of the band gap. The high symmetry lines for triclinic lattice were obtained from the literature [75].
 

which stem from the definition of S in terms of the Onsager coefficients:  \( S = L_{1}/L_{0}T \) . Here, a, b, and c are the Cartesian axes. This equation is the direct expression of the directional average of the transport coefficient in Eq. (6), provided that the relaxation time is independent of the direction. It is important to note that the negative sign of the Seebeck coefficient indicates electron carriers while the positive sign is for hole carriers. For the sake of simplicity, our discussion will be focused on the values rather than the signs. The calculated values of Seebeck coefficient are almost invariant in both p-type and n-type doping and grow monotonically with temperature as the carrier concentration increases from  \( 10^{17} \)  to  \( 10^{21} \)  cm \( ^{-3} \)  for T9Å, T11Å and T14Å, respectively. In all the tobermorite models, the calculated Seebeck coefficients show a linear decrease in their absolute values with increasing carrier concentrations as required by Eq. (9). The optimal doping for thermoelectric performance for these models expected at  \( 10^{17} \)  cm \( ^{-3} \)  for both p-type and n-type materials. Furthermore, from Fig. 3 the calculated absolute Seebeck coefficients for p-type doping in the tobermorite models were observed to be larger than those of the n-type doping. This is the direct consequence of the heavy valence bands present in the band structure of the tobermorite models in which the effective mass of the hole carriers keeps increasing. T14Å (Fig. 3(c)) shows higher S values at lower carrier concentration for p-type doping than those of T9Å (Fig. 3(a)) and T11Å (Fig. 2(b)), because of its smaller energy band gap compared to the other two models. These values of S for tobermorite models are considered the first results, since there are no available experimental or theoretical data to compare them with.

## Relaxation Time

The BoltzTraP code \( ^{[61]} \)  returns the electric conductivity divided by the constant relaxation time  \( \sigma/\tau \) . To obtain a quantitative estimate of the electrical conductivity  \( \sigma \) , we need to calculate the relaxation time  \( \tau \)  independently. Considering the high computational cost and the size of the unit cells of the tobermorite models, only the energy-dependent relaxation time for the T9Å model —i.e., the model with the fewest atoms in the unit cell — was calculated using the simple parabolic band (SPB) approach  \( [59, 79] \) , as a function of temperature, and for carrier concentrations ranging from  \( 10^{17} \)  to  \( 10^{21} \)  cm \( ^{-3} \)  for both electrons and holes.

In the SPB approximation, the relaxation time is assumed to follow a power-law expres-
 
![](./images/867748054407577723_8.jpg)

![](./images/867748054407577723_9.jpg)

![](./images/867748054407577723_10.jpg)

![](./images/867748054407577723_11.jpg)

![](./images/867748054407577723_12.jpg)

![](./images/867748054407577723_13.jpg)

FIG. 3. Calculated averaged Seebeck coefficient with respect to temperature at fixed carrier concentrations in p-type and n-type, for T9Å(a), T11Å(b) and T14Å(c).
 

sion:  \( \tau = \tau_{0}(T)(\epsilon - \epsilon_{0})^{r-1/2} \) , where  \( \epsilon_{0} \)  is a reference energy, e.g. the valence band maximum (VBM) or the conduction band minimum (CBM). The value r = 0 is appropriate for scattering from acoustic phonons at a temperature larger than the Debye temperature. Note that the prefactor  \( \tau_{0} \)  is temperature dependent (see below). The SPB approach has been successfully applied to study the thermoelectric properties of materials as reported in the literature [1, 76, 80–82].

In the case of (implicit) n-type doping, the Fermi energy  \( E_{F} \)  was first determined from the carrier concentration given by

 \[ n\left(T\right)=\frac{1}{2\pi^{2}}\left(\frac{2m_{d}^{*}k_{B}T}{\hbar^{2}}\right)^{\frac{3}{2}}F_{\frac{1}{2}}(\eta), \quad (11) \] 

and the Fermi integral  \( F_{j}(\eta) \)  is defined as

 \[ F_{j}(\eta)=\int_{0}^{\infty}\frac{e^{j}}{1+\exp\left(\frac{\epsilon}{k_{B}T}-\eta\right)}d\epsilon, \quad (12) \] 

where  \( \eta = (E_{F} - \epsilon_{0})/k_{B}T \) . For electrons,  \( \epsilon_{0} \)  is the energy of the CBM. The density of states effective mass is defined as  \( m_{d}^{*} = N_{v}^{\frac{2}{3}}(m_{a}^{*}m_{b}^{*}m_{c}^{*})^{\frac{1}{3}} \) , where  \( N_{v} \)  is the degeneracy of the band valley and  \( m_{a}^{*} \) ,  \( m_{b}^{*} \) ,  $ m_{c}^{*} are the principal effective masses with respect to the Cartesian directions at the band valley. The principal effective masses were evaluated from the Hessian matrix of band energies at the band edges using:

 \[ \frac{1}{m_{ij}^{*}}=\frac{1}{\hbar^{2}}\frac{\partial^{2}\epsilon}{\partial k_{i}\partial k_{j}} \quad (13) \] 

where i, j are Cartesian components. The elements of the Hessian matrix were calculated using the finite difference method with a 5-point central difference stencil [83]. The calculated effective masses at the conduction band minimum are  \( m_{ka}^{*} = 0.149m_{0} \) ,  \( m_{kb}^{*} = 133m_{0} \)  and  \( m_{kc}^{*} = 0.155m_{0} \) , where  \( m_{0} = 9.11 \cdot 10^{-31} \)  kg is the free electron mass. Similar calculations were done in the case of (implicit) p-type doping. In this case the calculated effective masses at the valence band maximum are  \( m_{ka}^{*} = 0.309m_{0} \) ,  \( m_{kb}^{*} = 1.161m_{0} \)  and  \( m_{kc}^{*} = 0.989m_{0} \) .

According to the SPB approach, the energy dependent relaxation time for phonon scattering is expressed as: \( ^{[1]} \) 

 \[ \tau=\frac{\sqrt{2}\pi\hbar^{4}v_{s}^{2}\rho}{3E_{d}^{2}\left(m^{*}k_{B}T\right)^{\frac{3}{2}}}\frac{F_{0}(\eta)}{F_{\frac{1}{2}}(\eta)}, \quad (14) \] 

where we consider acoustic phonons because their scattering is dominant at temperatures larger than the Debye temperature and moderate doping \( ^{[79]} \) . Eq. (14) is consistent with
 

the SPB approximation if we take  \( 1/\tau_{0} \propto k_{B}T \) , i.e., the scattering rate proportional to the number of phonons. Here,  \( \rho \)  is the mass density and the longitudinal sound velocity  \( v_{s} \)  is calculated from the elastic constants values of  \( (C_{11}/\rho)^{\frac{1}{2}} \) ,  \( (C_{22}/\rho)^{\frac{1}{2}} \)  and  \( (C_{33}/\rho)^{\frac{1}{2}} \)  in the direction of the wave vector [84]. The elastic constants  \( (C_{11}=158\ \text{GPa}, C_{22}=154\ \text{GPa} \)  and  \( C_{33}=74\ \text{GPa}) \)  were obtained from a DFT calculation at the gamma point.  \( E_{d} \)  is the acoustic deformation energy defined by  \( E_{d}^{i} = \Delta\epsilon_{i}/(\Delta V/V_{0}) \)  and calculated from the energy change  \( (\Delta\epsilon_{i}) \)  of the i-th band with volume dilation  \( (\Delta V/V_{0}) \)  along the Cartesian directions. We calculated the band structure by varying the volume from  \( 0.98V_{0} \)  to  \( 1.01V_{0} \) , with  \( \pm5.0\% \)  increase of the cell volume. To calculate the deformation energy, we adopted the method proposed by Xi et al. [81] by taking the energy change of the conduction band minimum (CBM) and the valence band maximum (VBM) for electrons and holes, respectively. The evaluated deformation energy for  \( T9\mathring{A} \)  is 10.428 eV for the VBM and 5.381 eV for the CBM.

In Figs. 4(i) to 4(v), we plot the relaxation time  \( \tau \)  as a function of temperature and carrier concentration obtained from the SPB model for  \( T9\mathring{A} \) , along the three Cartesian axes. A glance at Fig. 4 shows that at low temperatures  \( \tau \)  is large and decreases with increasing temperature. As we move from  \( 10^{17} \)  cm \( ^{-3} \)  to higher carrier concentrations, the relaxation time  \( \tau \)  decreases linearly with temperature for both p-type and n-type doping. The  \( \tau \)  values along the x and y directions are comparable because the longitudinal sound velocity is nearly the same. Over the entire carrier concentration range, the n-type relaxation time  \( \tau \)  exhibits higher values compared to those of the p-type. This is because the electrons have a much smaller effective mass than the holes, which results in a lower density of states and hence a longer relaxation time  \( \tau \) .

## Electrical Conductivity

The trace of the electrical conductivity  \( \sigma_{avg}=(\sigma_{a}+\sigma_{b}+\sigma_{c})/3 \)  was obtained from Boltzmann-TraP for  \( T9\mathring{A} \)  using the calculated relaxation time computed in Sec. III C. The resulting electrical conductivity  \( \sigma \)  for p-type and n-type doping as a function of temperature and fixed carrier concentrations ( \( 10^{17} \)  to  \( 10^{21} \)  cm \( ^{-3} \) ) is presented in Fig. 5. Both p-type and n-type  \( T9\mathring{A} \)  exhibit an increase in electrical conductivity with increasing carrier concentration, which is consistent with the dependence of electrical conductivity on the carrier concentration. At 300 K, we found p-type electrical conductivity values of 22.49, 224.43,
 
![](./images/867748054407577723_14.jpg)

(i)

(ii)

![](./images/867748054407577723_15.jpg)

![](./images/867748054407577723_16.jpg)

(iii)

![](./images/867748054407577723_17.jpg)

(iv)

![](./images/867748054407577723_18.jpg)

FIG. 4. Calculated electronic relaxation time  \( \tau \)  versus temperature for T9 \( \AA \) .
 

2190.98, 18534.20 and 93440.60  \( \Omega^{-1}m^{-1} \)  for carrier concentrations increasing from  \( 10^{17} \)  cm \( ^{-3} \)  to  \( 10^{21} \)  cm \( ^{-3} \) . For n-type doping, electrical conductivity values of 367.62, 3666.00, 30631.10, 289992.00 and  \( 1.044 \times 10^{6} \)   \( \Omega^{-1}m^{-1} \)  were obtained for the same concentration range at 300 K. A further glance at Fig. 5 shows that at low temperature  \( \sigma \)  is higher and then decreases as temperature increases, a behaviour attributed to the temperature dependence of the electron-phonon scattering described by a T \( ^{-3/2} \)  power-law. However, the electrical conductivity increases overall with increasing carrier concentration from  \( 10^{17} \)  to  \( 10^{21} \)  cm \( ^{-3} \)  in both the p-type and n-type, respectively. This is typical of a lightly doped semiconductor where the electrical conductivity decreases with temperature when most of the carriers are ionised, as a result of the thermal scattering of carriers by the vibrating lattice [85]. The overall n-type electrical conductivity  \( \sigma \)  values are significantly higher than those of the p-type doping at the same carrier concentration and temperature. This is due to the smaller effective mass at the conduction band maximum of the n-type doping.

Fig. 6 shows the temperature-dependent electrical conductivity  \( \sigma/\tau \)  versus carrier concentration obtained from BoltzTraP, in both p-type and n-type doping for T11Å and T14Å models. The general observation from Figs. 6(i) and 6(ii), is that  \( \sigma/\tau \)  decreases at a negligible rate with temperature over the entire carrier concentrations range, reaching a maximum value of  \( <0.1\times10^{6}\left(10^{14}(\Omega m s)^{-1}\right) \)  for p-type and  \( >0.2\times10^{6}\left(10^{14}(\Omega m s)^{-1}\right) \)  for n-type at carrier concentrations of  \( 10^{21} \)  cm \( ^{-3} \) , for T11Å and T14Å models, respectively. In the whole carrier concentration range, the n-type values are higher than those of p-type doping in both T11Å and T14Å. This difference can be attributed to the heavy valence band maximum in their band structures (see Fig. 2(b) and 2(c)), which causes a reduction in the mobility of the hole carriers. However, as shown in Fig. 6 the electrical conductivity of T14Å is slightly higher than that of T11Å for the same temperature and carrier concentrations in both the p-type and n-type doping.

## Electronic Thermal Conductivity

The electronic component of the total thermal conductivity is given by the Wiedemann-Franz relation:

 \[ \kappa_{e}=L\sigma T, \quad (15) \]
 
![](./images/867748054407577723_19.jpg)

![](./images/867748054407577723_20.jpg)

(i)

![](./images/867748054407577723_21.jpg)

![](./images/867748054407577723_22.jpg)

FIG. 5. Calculated averaged electrical conductivity and electronic thermal conductivity as a function of temperature and carrier concentrations for T9Å.

where L is the Lorenz number \( ^{[8]} \)  and takes the value  \( L = 2(k_{B}/q)^{2} \)  for the non-degenerate case [86]. We evaluated the averaged electronic thermal conductivity  \( \kappa_{e} \)  as a function of temperature and carrier concentration for T9Å for both p-type and n-type doping using the values of  \( \tau \)  computed from Sec. III.C. The results are presented in Fig. 5(ii). For p-type doping  \( \kappa_{e} \)  decreases slowly with temperature as the carrier concentration increases, except at carrier concentration  \( 10^{20} \)  cm \( ^{-3} \) , where the magnitude of  \( \kappa_{e} \)  initially increases up to 325 K and then slightly decreases. In contrast, for the n-type  \( \kappa_{e} \)  slightly increases (1%) with temperature at carrier concentrations of  \( 10^{18} \) ,  \( 10^{19} \)  and  \( 10^{21} \)  cm \( ^{-3} \) , and decreases with temperature at carrier concentrations of  \( 10^{17} \)  and  \( 10^{20} \)  cm \( ^{-3} \) . The average electronic thermal
 
![](./images/867748054407577723_23.jpg)

![](./images/867748054407577723_24.jpg)

(i)

![](./images/867748054407577723_25.jpg)

![](./images/867748054407577723_26.jpg)

(ii)

FIG. 6. Averaged electrical conductivity  \( \sigma/\tau \) , as a function of temperature and carrier concentrations for T11Å(i) and T14Å(ii) models.

conductivity for the tobermorite 11Å and 14Å models was also evaluated and the plots are presented in Fig. 7.

It exhibits a monotonic increase with carrier concentration in the entire temperature range when the former increases from  \( 10^{17} \)  to  \( 10^{21} \)  cm \( ^{-3} \) , for both p-type and n-type doping and for both T11Å and T14Å. This linear increase in  \( \kappa_{e}/\tau \)  can easily be explained through the Wiedemann-Franz law, Eq. (15), i.e. multiplying the decreasing values of  \( \sigma/\tau \)  by the operating temperature, raises the values of  \( \kappa_{e}/\tau \) . The electronic thermal conductivity ex-
 
![](./images/867748054407577723_27.jpg)

![](./images/867748054407577723_28.jpg)

(i)

![](./images/867748054407577723_29.jpg)

![](./images/867748054407577723_30.jpg)

(ii)

FIG. 7. Averaged electronic thermal conductivity  \( \kappa_{e}/\tau \) , as a function of temperature and carrier concentrations for T11Å(i) and T14Å(ii) models.

hibits a monotonic increase with temperature, the n-type values being an order of magnitude higher than those of the p-type doping over the entire carrier concentration range, for both T11Å and T14Å.

## Power Factor

The power factor,  \( S^{2}\sigma/\tau \)  was evaluated as a function of temperature and carrier concentration for the T11Å and T14Å models using the values of S and  \( \sigma/\tau \)  obtained from
 

BoltzTraP. Results are presented in Fig. 8. Both p-type and n-type power factors for T11Å and T14Å increase monotonically with temperature over the considered carrier concentration range. This is due to  \( S^{2} \)  increasing faster than  \( \sigma/\tau \)  decreases. However, at carrier concentrations of  \( 10^{17} \)  and  \( 10^{21} \)  cm \( ^{-3} \)  in T11Å, the power factor is increasing with temperature at a very negligible rate as compared to that of n-type doping, due to the almost zero S and very low  \( \sigma/\tau \)  values. A similar behaviour was observed in T14Å at  \( 10^{17} \)  cm \( ^{-3} \) . In p-type T11Å (T14Å) at  \( 10^{20} \)  cm \( ^{-3} \)  concentration, the power factor rises to a maximum of  \( \approx 0.36 \times 10^{14} \)  mW/mK \( ^{2} \) s ( \( \approx 0.45 \times 10^{14} \)  mW/mK \( ^{2} \) s) at about 400 K. In n-type doping, the optimal power factors are slightly lower, hence suggesting that p-type doping holds the promise for a slightly better thermoelectric performance in tobermorite models. The temperature-dependent power factor  \( S^{2}\sigma \)  versus carrier concentrations plot for T9Å is also shown in Fig. 8(iii). In both n-type and p-type power factor is seen to decrease as temperature increases except in higher carrier concentration values of  \( 10^{20} \)  and  \( 10^{21} \)  cm \( ^{-3} \) . However, the power factor generally improved when the values of scattering time was added.

## Figure of merit ZT

Using the calculated Seebeck coefficient and the values of  \( \sigma \)  and  \( \kappa_{e} \) , we calculated  \( Z_{e}T = S^{2}\sigma T/\kappa_{e} \) , which is the figure of merit that ignores the lattice thermal conductivity  \( \kappa_{l} \) , for p-type and n-type T9Å. This is reported in Fig. 9(i). The calculated  \( Z_{e}T \)  values of p-type T9Å are larger than those of n-type doping, because of the higher Seebeck coefficient (see Fig. 3(a)). The calculated  \( Z_{e}T \)  decreases for increasing carrier concentration, with the optimal values at  \( 10^{17} \)  cm \( ^{-3} \)  in both p-type and n-type T9Å. The maximum  \( Z_{e}T \)  value at  \( 10^{17} \)  cm \( ^{-3} \)  for p-type doping is 0.983, which is constant from 275-400 K, while for n-type doping the value is 0.956 from 375-400 K. At 300 K,  \( Z_{e}T \)  takes the value 0.951 for n-type doping at  \( 10^{17} \)  cm \( ^{-3} \) . In Fig. 9 we report the carrier concentration and temperature dependence of  \( Z_{e}T \)  for p-type and n-type T11Å and T14Å. These were calculated using the Seebeck coefficient, electrical conductivity,  \( \sigma/\tau \)  and electronic thermal conductivity,  \( \kappa_{e}/\tau \)  obtained from BoltzTraP. Notice that the relaxation time  \( \tau \)  is not needed to compute  \( Z_{e}T \) , as it cancels out in the ratio  \( \sigma/\kappa_{e} = (\sigma/\tau)/(\kappa_{e}/\tau) \) . From Fig. 9(ii) (T11Å) and 9(iii) (T14Å), it is clear that p-type exhibits larger  \( Z_{e}T \)  compared to n-type over the whole range of carrier concentrations. The optimal values of  \( Z_{e}T \)  slightly decrease with carrier concentration, but
 
![](./images/867748054407577723_31.jpg)

(i)

![](./images/867748054407577723_32.jpg)

![](./images/867748054407577723_33.jpg)

(ii)

![](./images/867748054407577723_34.jpg)

![](./images/867748054407577723_35.jpg)

![](./images/867748054407577723_36.jpg)

FIG. 8. Calculated averaged Power factor  \( S^{2}\sigma/\tau \) , as a function of temperature and carrier concentrations for T11Å(i) and T14Å(ii) models and power factor  \( S^{2}\sigma \)  versus carrier concentration and temperature for T9Å(iii) model.
 

overall they remain close to 1, being optimal at 400 K for p-type T11Å. For p-type T14Å the optimal  \( Z_{e}T \)  values of 1.14, 1.17 and 1.20 correspond to a temperature of 225 K and carrier concentrations from  \( 10^{17} \)  to  \( 10^{19} \)  cm \( ^{-3} \) . For n-type doping, the highest values of  \( Z_{e}T \)  are again slightly below 1 and decreasing mildly with concentration for both T11Å and T14Å. These results suggest that these tobermorite cement-based material would perform better as a p-type thermoelectric material in the low temperature regime.

To illustrate the potential thermoelectric performance of cement-based composites, their overall figure of merit, ZT, we use in Eq. (8) the following representative values for the total thermal conductivity,  \( \kappa = \kappa_{e} + \kappa_{l} = 1.15 \, W/mK \)  [87] and doping,  \( n = 10^{19} \, cm^{-3} \) . Carrier densities as high as  \( 1.626 \cdot 10^{18} \, cm^{-3} \)  have been reported in the literature.[88] Values of the total thermal conductivity in the interval 0.53-1.15 W/mK have been reported for plain (i.e., with no additives) hydrated cement paste.[27, 87]. We also fix the scattering rate,  \( \tau = 10^{-14} \)  s for tobermorite cement models T11Å and T14Å.

In Fig. 10, based on our assumptions, our calculated results (ZT) for a typical plain hydrated cement paste show that the contribution of the lattice thermal conductivity,  \( \kappa_{l} \)  is very significant and that the figure of merit is of the order < 0.1 for lower carrier density  \( 10^{17} \)  to  \( 10^{19} \)  cm \( ^{-3} \)  and a scaling factor > 0.1 for higher carrier density. This means that the actual values of ZT may be one tenth or slightly more of what we reported in the figures for the electronic figure of merit,  \( Z_{e}T \) . From Fig. 10 (i), it can also be seen that the inclusion of the scattering rate obtained via the simple parabolic band method, play a significant role as well in the determination of the figure of merit. Overall, our calculations indicate that p-type cement materials are the promising thermoelectric material.

## IV. CONCLUSIONS

We have, for the first time, employed first principles methods and the semi-classical Boltzmann theory to systematically investigate the electronic and transport properties of tobermorite minerals as an analog for cement for use in cement-based thermoelectrics. The calculated structural parameters obtained were seen to be comparable with the available experimental and DFT data. The electronic structure of these materials showed that they are direct band gap insulators, whose band gap (already mentioned in Table I) decreases as the concentration of chemically bound water molecules increases. The calculated elec-
 
![](./images/867748054407577723_37.jpg)

![](./images/867748054407577723_38.jpg)

(i)

![](./images/867748054407577723_39.jpg)

![](./images/867748054407577723_40.jpg)

(ii)

![](./images/867748054407577723_41.jpg)

![](./images/867748054407577723_42.jpg)

FIG. 9. Calculated electronic  \( Z_{e}T \) , as a function of temperature and carrier concentrations for T9Å(i), T11Å(ii), and T14Å(iii) models.
 
![](./images/867748054407577723_43.jpg)

![](./images/867748054407577723_44.jpg)

(i)

![](./images/867748054407577723_45.jpg)

![](./images/867748054407577723_46.jpg)

(ii)

![](./images/867748054407577723_47.jpg)

![](./images/867748054407577723_48.jpg)

FIG. 10. Calculated electronic ZT, as a function of temperature and carrier concentrations for T9Å(i), T11Å(ii), and T14Å(iii) models.
 

tronic relaxation time using a simple parabolic band approach showed a decreasing trend with increasing temperature, over the entire range of carrier concentrations. The electronic relaxation time  \( \tau \)  along the a and b crystallographic directions changes quite slowly as carrier concentration increases from  \( 10^{17} \)  to  \( 10^{21} \)  cm \( ^{-3} \) , because of the small difference in their longitudinal sound velocities. To the best of our knowledge there are no experimental data reported on transport properties of tobermories, hence the results presented here are to be taken as predictions. However these results can also be affected by uncertainties especially the figure of merit ZT, which is based on the total thermal conductivity. As we tried to clarify these uncertainties based on the assumptions we made in Fig. 10, it can be seen that the contribution from lattice vibrations of these cement materials is essential and can not be neglected. We further saw from Fig. 10 (i) that the contribution from the scattering time  \( \tau \)  is appropriate from carrier concentration of  \( 10^{19} \)  to  \( 10^{21} \)  for both p-type and n-type materials but not much effective at carrier concentration of  \( 10^{21} \)  cm \( ^{-3} \) . We found that the electronic transport properties of T9Å, T11Å and T14Å favor the p-type thermoelectric behaviour. This is because of the presence of heavy, and thus flat, valence bands, which lead to a higher effective mass and hence a larger Seebeck coefficient. In contrast, the effective mass for electrons in the conduction band is an order of magnitude smaller, hence leading to smaller Seebeck coefficients in n-doped tobermories. The small value of the electronic thermal conductivity suggests that the total thermal conductivity is mainly dominated by the intrinsic lattice thermal conductivity.

Our study provides a blueprint for further computational studies of emerging cement composite materials of interest for thermoelectric applications, in particular those combined with carbon fibre. We have demonstrated from first principles how the Seebeck coefficient of a candidate material can be predicted in silico, allowing for theoretical modifications to the material to be proposed and evaluated rapidly, in order to maximise the thermoelectric figure of merit.

## ACKNOWLEDGEMENTS

This research was supported through a US-Ireland grant funded by the Department for the Economy of Northern Ireland (DfE, USI 127). We are grateful for computational support from the UK Materials and Molecular Modelling Hub, which is partially funded by EPSRC
 

(EP/P020194 and EP/T022213), for which access was obtained via the UKCP consortium and funded by EPSRC grant ref EP/P022561/1. JK was also supported by the Beatriz Galindo Program (BEAGAL18/00130) from the Ministerio de Educación y Formación Profesional of Spain, and by the Comunidad de Madrid through the Convenio Plurianual with Universidad Politécnica de Madrid in its line of action Apoyo a la realización de proyectos de I+D para investigadores Beatriz Galindo, within the framework of V PRICIT (V Plan Regional de Investigación Científica e Innovación Tecnológica)

[1] R. Guo, X. Wang, Y. Kuang, and B. Huang, Physical Review B - Condensed Matter and Materials Physics 92, 1 (2015), arXiv:1505.02601.

[2] C. Yu and K. T. Chau, Energy Conversion and Management 50, 1506 (2009).

[3] L. Pérez-Lombard, J. Ortiz, and C. Pout, Energy and Buildings 40, 394 (2008).

[4] B. Zhang, Y. Tian, X. Jin, T. Y. Lo, and H. Cui, Materials 11, 2205 (2018).

[5] G. Serale, M. Fiorentini, A. Capozzoli, D. Bernardini, and A. Bemporad, Energies 11, 631 (2018).

[6] Y. W. Kim, J. Ramousse, G. Fraisse, P. Dalicieux, and P. Baranek, Energy and Buildings 70, 106 (2014).

[7] Z. Liu, L. Zhang, G. Gong, H. Li, and G. Tang, Energy and Buildings 102, 207 (2015).

[8] G. J. Snyder and E. S. Toberer, Nature Materials 7, 105 (2008).

[9] J. P. Heremans, B. Wiendlocha, and A. M. Chamoire, Energy and Environmental Science 5, 5510 (2012).

[10] C. Han, Z. Li, and S. Dou, Chinese Science Bulletin 59, 2073 (2014).

[11] G. Mahan, B. Sales, and J. Sharp, Physics Today 50, 42 (1997).

[12] P. K. Mehta and P. J. M. Monteiro, CONCRETE-Microstructure, Properties and Materials (BooksInBytes, California, 2001) arXiv:1011.1669.

[13] H. F. W. Taylor, Cement chemistry (Thomas Telford Publishing, London, 1997).

[14] P. W. Chen and D. D. Chung, Smart Materials and Structures 2, 22 (1993).

[15] M. Sun, Z. Li, Q. Mao, and D. Shen, Cement and Concrete Research 28, 549 (1998).

[16] M. Sun, Z. Li, Q. Mao, and D. Shen, Cement and Concrete Research 28, 1707 (1998).

[17] S. Wen and D. D. Chung, Cement and Concrete Research 29, 1989 (1999).
 

[18] S. Wen and D. D. Chung, Cement and Concrete Research 30, 1295 (2000).

[19] S. Wen and D. D. Chung, Cement and Concrete Research 31, 507 (2001).

[20] B. Demirel and S. Yazicioglu, Xinxing Tan Cailiao/ New Carbon Materials 23, 21 (2008).

[21] J. Zuo, W. Yao, J. Qin, and H. Cao, Key Engineering Materials 492, 242 (2012).

[22] J. Wei, L. Hao, G. He, and C. Yang, Ceramics International 40, 8261 (2014).

[23] J. Wei, Z. Nie, G. He, L. Hao, L. Zhao, and Q. Zhang, RSC Advances 4, 48128 (2014).

[24] T. Ji, X. Zhang, and W. Li, Construction and Building Materials 115, 576 (2016).

[25] J. Wei, Q. Zhang, L. Zhao, L. Hao, and C. Yang, Ceramics International 42, 11568 (2016).

[26] J. Wei, Q. Zhang, L. Zhao, L. Hao, and Z. Nie, Ceramics International 43, 10763 (2017).

[27] J. Wei, L. Zhao, Q. Zhang, Z. Nie, and L. Hao, Energy and Buildings 159, 66 (2018).

[28] X. Liu, G. Liao, and J. Zuo, Fullerenes, Nanotubes and Carbon Nanostructures 0, 1 (2020).

[29] X. Liu, R. Jani, E. Orisakwe, C. Johnston, P. Chudzinski, M. Qu, B. Norton, N. Holmes, J. Kohanoff, L. Stella, H. Yin, and K. Yazawa, Renewable and Sustainable Energy Reviews 137, 110361 (2021).

[30] A. J. Allen, J. J. Thomas, and H. M. Jennings, Nature Materials 6, 311 (2007).

[31] X. Zhang, W. Chang, T. Zhang, and C. K. Ong, Journal of the American Ceramic Society 83, 2600 (2000).

[32] E. Gartner, I. Maruyama, and J. Chen, Cement and Concrete Research 97, 95 (2017).

[33] J. Jiang, Y. Yan, D. Hou, and J. Yu, Physical Chemistry Chemical Physics 20, 13920 (2018).

[34] A. Kumar, B. J. Walder, A. Kunhi Mohamed, A. Hofstetter, B. Srinivasan, A. J. Rossini, K. Scrivener, L. Emsley, and P. Bowen, Journal of Physical Chemistry C 121, 17188 (2017).

[35] S. Merlino, E. Bonaccorsi, and T. Armbruster, American Mineralogist 84, 1613 (1999).

[36] S. Merlino, E. Bonaccorsi, and T. Armbruster, European Journal of Mineralogy 13, 577 (2001).

[37] E. Bonaccorsi, S. Merlino, and A. R. Kampf, Journal of the American Ceramic Society 88, 505 (2005).

[38] E. Bonaccorsi, S. Merlino, and H. F. Taylor, Cement and Concrete Research 34, 1481 (2004).

[39] R. Shahsavari, M. J. Buehler, R. J. Pellenq, and F. J. Ulm, Journal of the American Ceramic Society 92, 2323 (2009).

[40] A. Vidmer, G. Sclauzero, and A. Pasquarello, Cement and Concrete Research 60, 11 (2014).

[41] L. Dezerald, J. J. Kohanoff, A. A. Correa, A. Caro, R. J. Pellenq, F. J. Ulm, and A. Saúl, Environmental Science and Technology 49, 13676 (2015).
 

[42] J. Kohanoff, A. A. Correa, G. Gribakin, C. Johnston, and A. Saúl, European Physical Journal D 75, 10.1140/epjd/s10053-021-00202-8 (2021).

[43] S. Le Caër, L. Dezerald, K. Boukari, M. Lainé, S. Taupin, R. M. Kavanagh, C. S. Johnston, E. Foy, T. Charpentier, K. J. Krakowiak, R. J. Pellenq, F. J. Ulm, G. A. Tribello, J. Kohanoff, and A. Saúl, Cement and Concrete Research 100, 110 (2017).

[44] B. Lothenbach, K. Scrivener, and R. D. Hooton, Cement and Concrete Research 41, 1244 (2011).

[45] B. Lothenbach and A. Nonat, Cement and Concrete Research 78, 57 (2015).

[46] P. Hohenberg and W. Kohn, Phys. Rev. 136, B864 (1964).

[47] W. Kohn and L. J. Sham, Phys. Rev. 140, A1133 (1965).

[48] P. Giannozzi, S. Baroni, N. Bonini, M. Calandra, R. Car, C. Cavazzoni, D. Ceresoli, G. L. Chiarotti, M. Cococcioni, I. Dabo, A. Dal Corso, S. De Gironcoli, S. Fabris, G. Fratesi, R. Gebauer, U. Gerstmann, C. Gougoussis, A. Kokalj, M. Lazzeri, L. Martin-Samos, N. Marzari, F. Mauri, R. Mazzarello, S. Paolini, A. Pasquarello, L. Paulatto, C. Sbraccia, S. Scandolo, G. Sclauzero, A. P. Seitsonen, A. Smogunov, P. Umari, and R. M. Wentzcovitch, Journal of Physics Condensed Matter 21, 395502 (2009), arXiv:0906.2569.

[49] J. P. Perdew, K. Burke, and M. Ernzerhof, Physical Review Letters 77, 3865 (1996).

[50] A. Dal Corso, A. Pasquarello, A. Baldereschi, and R. Car, Physical Review B - Condensed Matter and Materials Physics 53, 1180 (1996).

[51] D. Vanderbilt, Phys. Rev. B 41, 7892 (1990).

[52] J. D. Pack and H. J. Monkhorst, Physical Review B 16, 1748 (1977).

[53] N. Marzari, D. Vanderbilt, A. De Vita, and M. C. Payne, Physical Review Letters 82, 3296 (1999), arXiv:9903147 [cond-mat].

[54] S. Grimme, J. Antony, S. Ehrlich, and H. Krieg, Journal of Chemical Physics 132, 154104 (2010).

[55] C. G. Broyden, IMA Journal of Applied Mathematics (Institute of Mathematics and Its Applications) 6, 76 (1970).

[56] R. Fletcher, The Compter Journal 13, 317 (1970).

[57] D. Goldfarb, Mathematics of Computation 24, 23 (1970).

[58] D. F. Shanno, Mathematics of Computation 24, 647 (1970).
 

[59] B. R. Nag, Electron Transport in Compound Semiconductors, edited by H.-J. Queisser, M. Cardona, and P. Fulde (Springer-Verlag Berlin Heidelberg, New York, 1980) pp. 171–229.

[60] N. W. Ashcroft and N. D. Mermin, Solid State Physics (Forth Worth, Saunders College Publishing, 1976).

[61] G. K. Madsen and D. J. Singh, Computer Physics Communications 175, 67 (2006), arXiv:0602203 [cond-mat].

[62] J. Scheidemantel, C. Ambrosch-Draxl, T. Thonhauser, V. Badding, and O. Sofo, Physical Review B - Condensed Matter and Materials Physics 68, 1 (2003).

[63] J.M.Ziman, Principles of the theory of solids-Cambridge, University Press (1972) (1972).

[64] G. D. Mahan and J. O. Sofo, Proceedings of the National Academy of Sciences of the United States of America 93, 7436 (1996).

[65] T. Takeuchi, Materials, Preparation, and Characterization in Thermoelectrics, edited by D. M. Rowe (CRC Press, New York, Chp. 7, p138, 2012) pp. Chp. 7. 138.

[66] G. K. Madsen, J. Carrete, and M. J. Verstraete, Computer Physics Communications 231, 140 (2018), arXiv:1712.07946.

[67] K. Scheer, Semiconductor Physics: An Introduction (Springer Verlag, Berlin, Chaps. 4 and 6, 2002).

[68] A. Anselm, Introduction to Semiconductor Theory, edited by M. M. Samokhvalov (English translation, Mir Publishers, MOSCOW, 1981) pp. 532–535.

[69] W. W. Schulz, P. B. Allen, and N. Trivedi, Physical Review B 45, 10886 (1992).

[70] C. Biagioni, PLINIUS n. 37 (2011).

[71] C. Biagioni, S. Merlino, and E. Bonaccorsi, Mineralogical Magazine 79, 485 (2015).

[72] S. A. Hamid, Zeitschrift für Kristallographie - New Crystal Structures 154, 189 (1981).

[73] R. T. Downs and M. Hall-Wallace, American Mineralogist 88, 247 (2003).

[74] C. C. Dharmawardhana, A. Misra, S. Aryal, P. Rulis, and W. Y. Ching, Cement and Concrete Research 52, 123 (2013).

[75] W. Setyawan and S. Curtarolo, Computational Materials Science 49, 299 (2010), arXiv:1004.2974.

[76] A. F. May, E. S. Toberer, A. Saramat, and G. J. Snyder, Physical Review B - Condensed Matter and Materials Physics 80, 1 (2009).

[77] S. Bhattacharya and R. C. Mallik, Journal of Electronic Materials 40, 1221 (2011).
 

[78] D. Parker and D. J. Singh, Science and Technology of Advanced Materials 14, 10.1088/1468-6996/14/5/055003 (2013).

[79] H. Lee, THERMOELECTRICS DESIGN AND MATERIALS (John Wiley & Sons Ltd, Chp. 12, West Sussex, UK, 2016).

[80] P. H. Böttger, G. S. Pomrehn, G. J. Snyder, and T. G. Finstad, Physica Status Solidi (A) Applications and Materials Science 208, 2753 (2011).

[81] J. Xi, M. Long, L. Tang, D. Wang, and Z. Shuai, Nanoscale 4, 4348 (2012).

[82] W. Liu, H. Chi, H. Sun, Q. Zhang, K. Yin, X. Tang, Q. Zhang, and C. Uher, Physical Chemistry Chemical Physics 16, 6893 (2014).

[83] A. Fonari and C. Sutton, Effective Mass Calculator for Semiconductors, (https://github.com/afonari/emc) (2012).

[84] O. L. Anderson, J. Phys. Chem. Solids 24, 909 (1963).

[85] S. O. Kasap, Principles of Electronic Materials and Devices (McGraw-Hill companies, New York, Ch. 5., 2005).

[86] G. S. Nolas and H. J. Goldsmid, Thermal Conductivity of Semiconductors, edited by T. M. Tritt (in Physics of Solids and Liquids: Thermal Conductivity Theory, Properties, and Applications, Plenum, Publishers New York., 2004) p. 290.

[87] R. Jani, N. Holmes, R. West, K. Gaughan, X. Liu, M. Qu, E. Orisakwe, L. Stella, J. Kohanoff, H. Yin, and B. Wojciechowski, Polymers 14, 1 (2022).

[88] J. Wei, Y. Wang, X. Li, Z. Jia, S. Qiao, Y. Jiang, Y. Zhou, Z. Miao, D. Gao, and H. Zhang, ACS Applied Materials and Interfaces 13, 3919 (2021).
 
