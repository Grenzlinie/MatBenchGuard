
# Electronic structure and thermoelectric properties of CuRh_{1-x}Mg_{x}O_{2}

Antoine Maignan, \( ^{1} \)  Volker Eyert, \( ^{1,2} \)  Christine Martin, \( ^{1} \)  Stefan Kremer, \( ^{1,3} \)  Raymond Frésard, \( ^{1} \)  and Denis Pelloquin \( ^{1} \) 

 \( ^{1} \) Laboratoire CRISMAT, UMR CNRS-ENSICAEN(ISMRA) 6508, and IRMA, FR3095, Caen, France
 \( ^{2} \) Center for Electronic Correlations and Magnetism,
Institut für Physik, Universität Augsburg, 86135 Augsburg, Germany
 \( ^{3} \) Institut für Theorie der Kondensierten Materie,
Universität Karlsruhe, 76128 Karlsruhe, Germany
(Dated: November 13, 2018)

Electronic structure calculations using the augmented spherical wave method have been performed for  \( CuRhO_{2} \) . For this semiconductor crystallizing in the delafossite structure, it is found that the valence band maximum is mainly due to the  \( 4d\ t_{2g} \)  orbitals of  \( Rh^{3+} \) . The structural characterizations of  \( CuRh_{1-x}Mg_{x}O_{2} \)  show a broad range of  \( Mg^{2+} \)  substitution for  \( Rh^{3+} \)  in this series, up to about 12%. Measurements of the resistivity and thermopower of the doped systems show a Fermi liquid-like behavior for temperatures up to about 1000 K, resulting in a large weakly temperature dependent power factor. The thermopower is discussed both within the Boltzmann equation approach as based on the electronic structure calculations and the temperature independent correlation functions ratio approximation as based on the Kubo formalism.

PACS numbers: 71.20.-b, 72.15.Eb, 73.90.+f

Keywords: electronic structure, low-dimensional compounds

## I. INTRODUCTION

The search for new thermoelectric materials in order to convert waste-heat into electricity has motivated numerous studies on transition-metal oxides. One advantage of these materials over several others lies in their ability to be used at elevated temperatures in air. This opens the route to target systems releasing heat at temperatures as high as 1000 K. Among the studied p-type thermoelectric oxides, the layered ones such as  \( Na_{x}CoO_{2} \) , misfit cobaltites, or, more recently, the delafossites, all with structures containing  \( CdI_{2} \) -type layers, have been particularly investigated according to the richness of their physical properties. For instance, the thermoelectric performance of several  \( AMO_{2} \)  delafossites have been measured, leading to the following dimensionless figures of merit  \( ZT \)  of 0.04 at 800 K ( \( CuCr_{0.97}Mg_{0.03}O_{2} \) ), \( ^{1} \)  0.14 at 1100 K ( \( CuFe_{0.99}Ni_{0.01}O_{2} \) ), \( ^{2} \)  and 0.15 at 1000 K ( \( CuRh_{0.90}Mg_{0.10}O_{2} \) ). \( ^{3} \)  Their crystal structures can all be described as a delafossite-type, in which  \( MO_{2} \) -layers of edge sharing  \( MO_{6} \)  octahedra alternate along the c-axis with layers of monovalent  \( Cu^{+} \) cations, the latter exhibiting a dumbbell O–Cu–O coordination.

Although the thermoelectric properties of the Cu-based delafossites have been measured, their origin remains a subject of controversy. In the  \( CuCr_{1-x}Mg_{x}O_{2} \)  system, the measurements have been interpreted by considering different active layers for the electrical transport – either in the Cu or  \( CrO_{2} \)  layers – whereas in a recent report on  \( CuRhO_{2} \) , the electrical conductivities of both Cu and  \( RhO_{2} \)  layers have been proposed to be comparable at 300 K. \( ^{4} \) 

In order to shed light on the respective role of the layers on the transport properties in delafossites, electronic structure calculations have proven to be useful. \( ^{5,6,7,8,9,10,11,12,13} \)  In the  \( AcO_{2} \)  delafossite with A = Pt or Pd, these calculations have demonstrated that their low resistivities ( \( \sim 5 \mu\Omega \)  cm at room temperature \( ^{14,15} \) ) come almost exclusively from the in-plane d orbitals of the  \( A^{+} \) cations. \( ^{6,10} \)  For  \( CuMO_{2} \) , on the opposite, it is found that the  \( t_{2g} \)  states of the  \( M = Cr^{3+} \)  cations provide the most important contribution at the valence band maximum, with spin polarization supported by the experimental evidences for negative magnetoresistance and magnetothermopower. \( ^{12} \)  However, as has been recently reported for  \( CuYO_{2} \) , \( ^{9} \)  where the  \( 4d^{0} \)  stable electronic configuration of  \( Y^{3+} \)  precludes any participation of Y to the transport, there exists some cases where the copper cations are contributing to the charge delocalization. However, this delafossite belongs to those characterized by a large M cation ( \( r_{Y^{3+}} = 0.090 \)  nm versus  \( r_{Cr^{3+}} = 0.0615 \)  nm) favoring the incorporation of extra  \( O^{2-} \)  anions into the copper layer so that in that case the physics might be different. In that respect, the physics of the oxygen stoichiometric  \( CuMO_{2} \)  subclass of delafossites is of interest, especially if we consider the possibility to control the magnetism at the M-site. This is outlined by the multiferroic behavior exhibited by the  \( CuMO_{2} \)  delafossites for  \( M = Cr^{3+} \)  or  \( Fe^{3+} \) , which are both showing electric polarization induced by incommensurate antiferromagnetism according to the  \( S = \frac{3}{2} \)  and  \( S = \begin{array}{c}\frac{5}{2} \\ \hline \end{array} \)  high-spin M cations, respectively. \( ^{16,17,18} \)  For these delafossites, the complex magnetism resulting from the frustrated nature of the  \( MO_{2} \)  network is indeed thought to be responsible for the magnetic field induced electric polarization.

Such multiferroic behavior is in marked contrast to the metal-type behavior reported for the  \( Mg^{2+} \)  substituted rhodate  \( CuRh_{1-x}Mg_{x}O_{2} \) . The  \( 4d^{5}/4d^{6} \)  electronic configurations of low-spin  \( Rh^{4+}/Rh^{3+} \)  in this series provides a unique opportunity to study the electronic ground-state of a delafossite without extra contributions generated by the large magnetic moments of  \( Cr^{4+}/Cr^{3+} \)
 

 \( (S = 1/S = \frac{3}{2}) \)  or  \( Fe^{4+}/Fe^{3+} \)   \( (S = 2/S = \frac{5}{2}) \)  cations. However, literature data for  \( CuRh_{1-x}Mg_{x}O_{2} \)  show some variation. This is best illustrated by the different values reported for the room temperature Seebeck coefficient S of  \( CuRh_{0.90}Mg_{0.10}O_{2} \) , which are  \( S_{300K} = 130 \mu VK^{-1} \) , and  \( S_{300K} = 70 \mu VK^{-1} \)  as given in Refs. 3 and 4, respectively. \( ^{19} \)  Among the possible reasons explaining this discrepancy is the uncertainty of the Mg for Rh substitution controlling the concentration of  \( Rh^{4+} \)  holes in the  \( Rh^{3+} \)  matrix. In order to check for the transport mechanism and for the substitution effectiveness, electronic structure calculations have been performed. In the present paper, these results are discussed in comparison to the experimental data. The latter are obtained on polycrystalline samples, for which the delafossite structure was verified by a combined X-ray and electron diffraction study. Taken together with the cation analysis, these characterizations also demonstrate the existence of a  \( Mg^{2+} \)  solubility limit much larger than in  \( CuCr_{1-x}Mg_{x}O_{2} \) . The electrical resistivity and Seebeck coefficient measurements show that the substitution of Mg for Rh in  \( CuRhO_{2} \)  allows to progressively induce an insulator to metal transition accompanied by a gradual decrease of the thermopower.

Contrasting previous studies, these results are found to be compatible with electronic structure calculations with a lack of significant contribution of copper, the most important contribution at the Fermi level coming from the 4d orbitals of the Rh cations. The lack of significant magnetic contribution, probed by magnetic susceptibility, responsible for the low temperature increase in  \( CuCrO_{2} \)  and  \( CuFeO_{2} \) , allows for the study of the metallic state from 2.5 K to 1000 K. An unusual  \( T^{2} \)  regime is evidenced over a broad temperature range, which, when combined with the T dependence of the Seebeck coefficient, leads to remarkably T independent power factors,  \( PF \equiv \frac{S^{2}}{\rho} \) .

## II. METHODOLOGY

## A. Electronic structure calculations: theoretical method

The calculations are based on density-functional theory and the generalized gradient approximation (GGA). \( ^{20} \)  They were performed using the scalar-relativistic implementation of the augmented spherical wave (ASW) method (see Refs. 21,22,23 and references therein). In the ASW method, the wave function is expanded in atom-centered augmented spherical waves, which are Hankel functions and numerical solutions of Schrödinger's equation, respectively, outside and inside the so-called augmentation spheres. In order to optimize the basis set, additional augmented spherical waves were placed at carefully selected interstitial sites. The choice of these sites as well as the augmentation radii were automatically determined using the sphere-geometry optimization algorithm. \( ^{24} \)  Self-consistency was achieved by a highly efficient algorithm for convergence acceleration. \( ^{25} \)  The Brillouin zone integrations for the self-consistent field calculations were performed using the linear tetrahedron method with up to 1156 k-points within the irreducible wedge of the rhombohedral Brillouin zone, \( ^{23,26} \)  whereas the calculation of the density of states and the thermopower is based on 19871 k-points.

In the present work, a new full-potential version of the ASW method was employed. \( ^{[27]} \)  In this version, the electron density and related quantities are given by spherical-harmonics expansions inside the muffin-tin spheres. In the remaining interstitial region, a representation in terms of atom-centered Hankel functions is used. \( ^{[28]} \)  However, in contrast to previous related implementations, we here get away without needing a so-called multiple- \( \kappa \)  basis set, which fact allows to investigate rather large systems with a minimal effort.

## B. Ceramic samples preparation and characterization

The polycrystalline samples of the  \( CuRh_{1-x}Mg_{x}O_{2} \)  series have been prepared by solid state reaction in air. Bars of typical size  \( 2 \times 2 \times 10 \)  mm were prepared by mixing stoichiometric amounts of the  \( Cu_{2}O \) ,  \( Rh_{2}O_{3} \)  and MgO precursors, which were then pressed. The electron diffraction study was carried out with a JEOL 2010CX transmission electron microscope. The sample preparation is made by crushing in butanol some bar pieces, the corresponding microcrystals being afterwards deposited on Ni grids. The purity of the obtained black bars was checked by X-ray powder diffraction using a Panalytical X-pert Pro and a Brucker diffractometers. The data were analyzed by using the Fullprof suite. \( ^{29} \) 

As two different calcination temperatures have been used in the literature, two attempts were made at either  \( 930^{\circ} \) C or  \( 1050^{\circ} \) C for a duration of twelve hours. As shown in Fig. 1a for  \( CuRh_{0.9}Mg_{0.1}O_{2} \)  (x = 0.1), one small extra peak identified as CuO appears (see the vertical arrow in Fig. 1a). The weight of the latter depends on the synthesis temperature. Indeed, when increasing it from  \( 930^{\circ} \) C to  \( 1050^{\circ} \) C, the weight of this peak decreases. Furthermore, as these patterns were recorded in the same conditions, (amount of powder and acquisition time), this comparison shows the poor crystallinity of the  \( 930^{\circ} \) C prepared sample. This result agrees with the less dispersed cation contents of the  \( 1050^{\circ} \) C prepared sample as probed by energy dispersive X-ray spectroscopy (EDS) analysis performed within the transmission electron microscope. Such conclusions are consistent with the thermodynamics of the Cu-Rh-O ternary diagram, which showed that  \( CuRhO_{2} \)  synthesized below  \( 985^{\circ} \) C in an oxygen pressure of 0.1 MPa is unstable. \( ^{30} \)  Thus, the sample series corresponding to x = 0, 0.01, 0.04, 0.10, 0.15, and 0.30 in  \( CuRh_{1-x}Mg_{x}O_{2} \)  has been calcined in air at  \( 1050^{\circ} \) C for a duration of twelve hours.

The patterns of the  \( CuRh_{1-x}Mg_{x}O_{2} \)  samples are all
 
![](./images/867768172088918988_1.jpg)

![](./images/867768172088918988_2.jpg)

FIG. 1: (Color online) Top: X-ray patterns of two  \( CuRh_{0.90}Mg_{0.10}O_{2} \)  samples synthesized at  \( 930^{\circ}C \)  and  \( 1050^{\circ}C \) , respectively, with indexation in the  \( R\overline{3}m \)  space group. Bottom: X-ray diffraction patterns at room temperature; the vertical bars correspond to the locations of the diffraction peaks in the  \( R\overline{3}m \)  space group (with  \( a = 3.0741(1)\mathring{A} \) , and  \( c = 17.0952(3)\mathring{A} \) ). The missing data in the  \( 44-44.8^{\circ} \)  region ( \( 2\theta \) ) have been intentionally eliminated due to a small peak coming from the sample holder.

refined in the  \( R\overline{3}m \)  space group, usually reported for delafossite compounds at room temperature, as shown in Fig. 1. A small decrease of both a and c lattice parameters is observed when x increases up to 15% (corresponding to a decrease of  \( \sim 0.6\% \)  of the cell volume). From x = 0.10 on, one small extra peak appears that can be identified as CuO.

In order to test the maximum content of  \( Mg^{2+} \)  substituted for Rh cations, EDS analyses coupled to electron diffraction have been made first for the compound with the highest experimental Mg doping (x = 0.3). This analytical study demonstrates that a maximum of 12%  \( Mg^{2+} \)  can be substituted at the Rh site in  \( CuRhO_{2} \) , while the  \( Cu_{2}MgO_{3} \)  oxide is detected as a secondary phase. This is consistent with the observation from X-ray diffraction of this impurity for x > 0.10. For that reason, our measurements of transport properties are restricted to compounds corresponding to  \( x \leq 0.10 \) , the x = 0.10 composition already containing a very low amount of CuO as impurity. We emphasize that this structural study cannot be reconciled with previous data by Shibasaki et al. \( ^{4} \)  given for compounds nominally containing up to 20% of  \( Mg^{2+} \) .
The low temperature ( \( T < 320 K \) ) electrical resistivity ( \( \rho \) ) and Seebeck coefficient (S) were measured by using a Quantum Design cryostat. The four-probe and the steady-state techniques were used for the former and the latter, respectively, indium electrical contacts having been deposited with ultrasonics. For the high temperature  \( \rho \)  and S measurements ( \( T > 300 K \) ) a Ulvac-Zem 3 system was used. The magnetic susceptibility was measured by using a dc SQUID magnetometer (zero field-cooling,  \( \mu_{0}H = 0.3T \) ).

## III. RESULTS

## A. Calculations: Important role of the Rh 4d orbitals

The calculations were based on the crystal structure data by Oswald et al. \( ^{31} \)  who determined the lattice constants as  \( a = 3.08 \AA \)  and  \( c = 17.09 \AA \) . However, these authors did not measure the internal oxygen parameter. For this reason, we performed an energy minimization, leading to a value of  \( z_{O} = 0.10717 \) , which was used in all subsequent calculations.

The electronic bands along selected high-symmetry lines of the first Brillouin zone of the hexagonal lattice, Fig. 2, are displayed in Fig. 3.

![](./images/867768172088918988_3.jpg)

FIG. 2: First Brillouin zone of the hexagonal lattice.

The corresponding partial densities of states (DOS) are shown in Fig. 4. While the lower part of the spectrum is dominated by O 2p states, the transition metal d states lead to rather sharp peaks in the interval from -4 to +4 eV. In particular, the  \( t_{2g} \)  and  \( e_{g} \)  manifolds of the Rh 4d states as resulting from the octahedral coordination are recognized. This representation of the partial DOS used a local rotated coordinate system with the Cartesian axes pointing towards the oxygen atoms.  \( \sigma \) -type overlap of the O 2p states with the Rh 4d  \( e_{g} \)  orbitals leads to the contribution of the latter between -7 and -6 eV. In contrast, due to the much weaker  \( \pi \) -type overlap of the O 2p states with the  \( t_{2g} \)  orbitals, these states give rise to sharp peaks in the interval from -2.2 eV to the valence band maximum. The  \( t_{2g} \)  manifold is separated by an optical band gap of  \( \approx 0.75 \)  eV from the empty  \( e_{g} \)  states and thus leads to a Rh  \( d^{6} \)  state. The Cu 3d states are essentially
 

limited to the interval from -4 eV to the valence band maximum and thus Cu can be assigned a monovalent  \( d^{10} \)  configuration in close analogy with the experimental findings. In passing, we mention the finite dispersion of the electronic bands parallel to  \( \Gamma \) -A, which points to a considerable three-dimensionality arising from the coupling between the layers. Yet, this overall behavior of the dispersion perpendicular to the a - b plane is contrasted by the barely noticeable dispersion particularly along the line K-H. This has been also observed for other delafossite materials. \( ^{10,12} \) 

Further insight about the electronic properties of  \( CuRhO_{2} \)  can be gained by analyzing the real and imaginary parts of the dielectric function as calculated within linear-response (see Ref. 23 for more details). As is evident from Fig. 5, the asymmetry between the in-plane and out-of-plane directions is not reflected in the absorption gap following from the imaginary parts of the dielectric function. In fact the gap is very close to 0.75 eV in all three directions, which is most likely to exceed the Hund's rule coupling. Therefore, the low-spin  \( 4d^{6} \)  configuration of  \( Rh^{3+} \)  is expected to be the ground state. This is consistent with earlier findings by Singh for  \( CuCoO_{2} \) , where the Co ions adopt the low-spin  \( 3d^{6} \)  configuration. \( ^{8} \) 

Finally, we have calculated the thermopower using the framework of Boltzmann theory. \( ^{32} \)  The transport properties are expressed in terms of the Onsager transport coefficients,

 \[ L_{\lambda\lambda^{\prime}}^{(n)}=\frac{1}{T}\int_{-\infty}^{+\infty}d E\left(-\frac{\partial f(E)}{\partial E}\right)\Xi_{\lambda\lambda^{\prime}}(E)\left(E-\mu\right)^{n}, \quad (1) \] 

where  \( \left(-\frac{\partial f(E)}{\partial E}\right) \)  is the negative derivative of the Fermi function and

 \[ \Xi_{\lambda\lambda^{\prime}}(E)=\frac{1}{\Omega_{c}}\sum_{\mathbf{k}}\sum_{n}v_{\mathbf{k}n}^{\lambda}v_{\mathbf{k}n^{\prime}}^{\lambda^{\prime}}\tau_{\mathbf{k}n}\delta(E-\varepsilon_{\mathbf{k}n}) \quad (2) \] 

denotes the so-called transport distribution. \( ^{33,34} \)  Here,  \( \Omega_{c} \)  is the volume of the unit cell,  \( v_{kn}^{\lambda} \)  a Cartesian component

![](./images/867768172088918988_4.jpg)

FIG. 3: (Color online) Electronic bands of  \( CuRhO_{2} \) .

![](./images/867768172088918988_5.jpg)

FIG. 4: (Color online) Partial densities of states (DOS) of  \( CuRhO_{2} \) . Selection of the Rh 4d orbitals is relative to the local rotated reference frame, see text.

![](./images/867768172088918988_6.jpg)

FIG. 5: (Color online) Dielectric function of  \( CuRhO_{2} \) .

of the group velocity of the n'th band, and  \( \tau_{kn} \)  is the relaxation time. While the electrical conductivity and the thermal conductivity (at zero electric field) are given directly by (1) for n = 0 and n = 2, respectively, the thermopower is calculated from the matrix equation

 \[ S_{\lambda\lambda^{\prime}}=\frac{1}{e T}\left(\left[L^{(0)}\right]^{-1}L^{(1)}\right)_{\lambda\lambda^{\prime}}, \quad (3) \] 

where e is the (negative) electronic charge. Following standard practice we assume that the relaxation time does not depend on k and band index, in which case  \( \tau \)  cancels from the Seebeck coefficient. The implementation of the above formulation was done along similar lines as those previously proposed by Scheidemantel et al. as well as by Madsen and Singh. \( ^{33,34} \)  The implementation was tested against the recent results by Singh for  \( CuCoO_{2} \)  and  \( YCuO_{2} \) , and very good agreement was found. \( ^{8,9} \) 

The xx-components of the thermopower as calculated for different doping levels are displayed in Fig. 6; the
 
![](./images/867768172088918988_7.jpg)

FIG. 6: (Color online) Thermopower  \( S_{xx} \)  of  \( CuRhO_{2} \)  for different hole doping levels.

calculated zz-components are about 10-20% larger. According to these findings, the thermopower strongly decreases with increased hole doping. In addition, it shows an almost linear dependence on temperature especially in the intermediate-temperature range with the downturn at low doping and high temperatures reflecting excitations across the optical band gap. Worth mentioning are the rather high values for the lower doping levels down to  \( \approx 100 \)  K and the pronounced drop below this temperature.

In passing, we mention that apart from systematically slightly smaller values our results are in perfect agreement with the calculations of Usui et al., \( ^{13} \)  who likewise used the Boltzmann equation approach and who in turn obtained almost perfect agreement with the experimental data by Kuriyama et al. \( ^{3} \)  However, we recall from the above mentioned previous comparative tests to the results by Singh that the thermopower is remarkably sensitive to details of the crystal structure. Since Usui et al. used slightly different lattice constants in their calculations this might explain the systematic deviations in the calculated thermopower.

## B. Electrical resistivity: A metal-insulator transition

 \( \rho(T) \)  curves for the  \( CuRh_{1-x}Mg_{x}O_{2} \)  series as given in Fig. 7 reveal the modification of the electronic ground-state induced by the substitution. At 300 K, the values decrease by a factor of  \( \sim300 \)  as x increases from x = 0.00 to x = 0.10. This drop is even more pronounced at lower temperatures as the  \( \rho(T) \)  curve exhibits a localized behavior in  \( CuRhO_{2} \)  with  \( \rho_{100K} = 3 \times 10^{4} \Omega \)  cm at 100 K. In contrast, metal-like behavior is observed for  \( CuRh_{0.90}Mg_{0.10}O_{2} \)  with  \( \rho_{100K} = 1.2 \times 10^{-3} \Omega \)  cm. It must be emphasized that the change of electronic state induced by  \( Mg^{2+} \)  is progressive. The  \( CuRh_{0.99}Mg_{0.01}O_{2} \)  com-

![](./images/867768172088918988_8.jpg)

FIG. 7: (Color online) Temperature dependence of the resistivity of  \( CuRh_{1-x}Mg_{x}O_{2} \)  for x = 0, x = 0.01, x = 0, and x = 0.10.

pound still exhibits a localized behavior but with a resistivity decreased by three orders of magnitude at 100 K as compared to  \( CuRhO_{2} \) , whereas for  \( CuRh_{0.96}Mg_{0.04}O_{2} \) ,  \( \rho \)  remains almost T independent from 100 K to 1000 K ( \( \rho \)  increasing by 5% only in this temperature range). The  \( \rho(T) \)  curve shows a re-entrant behavior only below  \( \sim 100 K \) , reaching a maximum value of  \( \rho = 8 \times 10^{-1} \Omega \)  cm at 5 K. In fact, a closer inspection of the curves reveals that they all go through a minimum value at a characteristic temperature  \( T_{min} \)  separating a  \( \frac{d\rho}{dT} < 0 \)  regime below  \( T_{min} \)  from a  \( \frac{d\rho}{dT} > 0 \)  regime for  \( T > T_{min} \)  (Fig. 7). As shown in Table I, the  \( T_{min} \)  value decreases from  \( T_{min}=800 K \)  for  \( CuRhO_{2} \)  to  \( T_{min}=38 K \)  for  \( CuRh_{0.90}Mg_{0.10}O_{2} \) .

For the pristine compound, the localizing behavior observed below  \( T_{\text{min}} \)  (800 K) is consistent with the existence of a rather small gap at the Fermi level obtained in the section III A. Even though this temperature dependence of the resistivity is similar to the curve measured for  \( CuCrO_{2} \) , it is in fact closer to the one of  \( CuCr_{0.99}Mg_{0.01}O_{2} \) .¹² However, the data point to a different transport mechanism. Indeed, first, no significant magneto-resistance was observed in contrast to all  \( CuCr_{1-x}Mg_{x}O_{2} \)  samples showing a magneto-resistance as high as  \( -10\% \)  at 5 K in 7 T. Second, neither the Arrhenius law  \( \rho \propto e^{-T_{0}/T} \)  nor the polaronic model  \( \rho \propto Te^{-T_{0}/T} \) , nor the variable range hop-

<table><tr><td>x</td><td>\( T_{\text{min}}(\text{K}) \)</td><td>\( \rho(T_{\text{min}})(\text{m}\Omega \text{ cm}) \)</td></tr><tr><td>0.00</td><td>800</td><td>102</td></tr><tr><td>0,01</td><td>699</td><td>45.56</td></tr><tr><td>0.04</td><td>320</td><td>10.74</td></tr><tr><td>0,10</td><td>38</td><td>1.22</td></tr></table>

TABLE I:  \( T_{min} \)  and doping-dependence of the resistivity at  \( T_{min} \)  for several compositions of  \( CuRh_{1-x}Mg_{x}O_{2} \) .
 

ping model \(\rho \propto e^{-(T_{0}/T)^{\alpha}}\) with \(\alpha = 1/2\), \(1/3\) or \(1/4\), which are broadly used in conventional three dimensional transition metal perovskites as \(\mathrm{La}_{1-\mathrm{x}}\mathrm{Sr}_{\mathrm{x}}\mathrm{CoO}_{3}\),\(^{35}\) and which were successfully applied to the two dimensional chromium based delafossites \(\mathrm{CuCrO}_{2}\) and \(\mathrm{CuCr}_{0.98}\mathrm{Mg}_{0.02}\mathrm{O}_{2}\), respectively,\(^{12}\) can convincingly fit the \(\rho(T)\) data of \(\mathrm{CuRhO}_{2}\).

This conclusion about the transport mechanism in  \( CuRhO_{2} \)  is confirmed by the analysis of the  \( \rho(T) \)  curves found for the Mg-substituted  \( CuRhO_{2} \)  compounds. First, the attempts to fit the curves by a polaronic model fail as for  \( CuRhO_{2} \) . Second, a low temperature Fermi liquid behavior is found for  \( CuRh_{0.90}Mg_{0.10}O_{2} \) . Third, the metal-like regions of the curves can be adjusted to  \( T^{2} \)  dependences that are obeyed over a wide temperature range. As shown in Fig. 8 for  \( CuRh_{0.96}Mg_{0.04}O_{2} \) , the

![](./images/867768172088918988_9.jpg)

FIG. 8: (Color online) Fermi liquid-like behavior of  \( CuRh_{1-x}Mg_{x}O_{2} \)  for the dopings x = 0.04 and x = 0.1. For  \( CuRh_{0.96}Mg_{0.04}O_{2} \) , a constant contribution  \( \rho_{cc} = 8 m\Omega \)  cm has been subtracted for clarity. The thin full lines represent the Fermi liquid fits, while the thick full lines are guides for the eyes only.

\(\rho \propto T^{2}\) regime holds from \(\sim 300\mathrm{K}\) to \(\sim 850\mathrm{K}\). Expressing \(\rho(T)\) as \(\rho(T) = \rho_{0} + AT^{2}\) as in a Fermi liquid we

<table><tr><td>Compound</td><td>A( \( \Omega \)  m K \( ^{-2} \) )</td></tr><tr><td>CuRh_{0.96}Mg_{0.04}O_{2}</td><td>7.7 10 \( ^{-11} \)</td></tr><tr><td>CuRh_{0.90}Mg_{0.10}O_{2}</td><td>3 10 \( ^{-11} \)</td></tr><tr><td>PdCoO_{2} (from Ref. 14)</td><td>4.8 10 \( ^{-13} \)</td></tr><tr><td>Thin films of V_{2}O_{3} (from Ref. 36)</td><td>2 10 \( ^{-9} \)</td></tr><tr><td>La_{1-x}Sr_{x}TiO_{3} (from Ref. 37)</td><td>2-3 10 \( ^{-11} \)</td></tr></table>

TABLE II: Fermi liquid transport parameter for several oxides.

obtain the transport parameter A. As shown in Table II, the values of A for these rhodates are found to be located in an intermediate range, namely they are larger than in the  \( PdCoO_{2} \)  delafossites, \( ^{14} \)  but smaller than in thin films of  \( V_{2}O_{3} \) . \( ^{36} \)  In a fashion similar to the behavior observed in the titanates  \( La_{1-x}Sr_{x}TiO_{3} \) , \( ^{37} \)  A increases with decreasing concentration of charge carriers, while, in contrast to all the above systems, the  \( T^{2} \) -behavior may be observed for temperatures up to 1000 K. Remarkably, the widely observed phonon-dominated  \( \rho \propto T \)  behavior is not taking over, even at such high temperatures. Such a result enlightens the unusual transport behavior of these rhodates. The presence of the  \( Mg^{2+} \)  scattering centers, up to 12%, corresponds to concentration well below the percolation threshold, and no band purely based on Mg orbitals is expected to form. Therefore, on their own, such low Mg concentrations should not affect the transport in the T range where this  \( \rho \propto T^{2} \)  regime is observed but by hole doping the Rh-based 4d bands. Still, inhomogeneous distribution of the Mg ions on the Rh sites might be responsible for the kink observed in Fig. 8 for  \( CuRh_{0.90}Mg_{0.10}O_{2} \) .

Finally, the resistivity values for  \( CuRh_{1-x}Mg_{x}O_{2} \)  are rather comparable to those reported in Ref. 4 ( \( T \leq 300K \) ) or in Ref. 3 ( \( T \geq 400K \) ). The decrease of  \( \rho \)  induced by the  \( Mg^{2+} \)  substitution in the present samples strongly suggests that “hole” charge carriers are created according to the formula  \( CuRh_{1-x}^{3+}Rh_{x}^{4+}Mg_{x}^{2+}O_{2} \) . It must also be added that since no other  \( CuMO_{2} \)  delafossites exhibit such metal-like behavior down to very low T, the role of the Cu channel to the electronic transport can hardly be invoked as is also confirmed by the electronic structure calculations.

## C. Thermoelectric power and power factors

Although the  \( \rho \)  values of our  \( CuRh_{1-x}Mg_{x}O_{2} \)  series are comparable to those already reported, \( ^{3} \)  the Seebeck coefficients values for  \( CuRhO_{2} \)  (Table III and Fig. 9) appear to be different. When compared to the study in which the samples were calcined at lower  \( T^{4} \) , \( ^{4} \)  the present S values are found to be always much larger, as documented in Table III. Besides, our data for the substituted compounds showing an S decrease as x increases cannot be reconciled with the x-independent  \( S_{300K} \)  for all substituted compounds of Ref. 4.

For the most metallic sample, the S values are al-

<table><tr><td>x</td><td>T(K)</td><td>S( \( \mu \) V K \( ^{-1} \) )</td></tr><tr><td>0</td><td>330</td><td>280</td></tr><tr><td>0 (from Ref. 4)</td><td>300</td><td>130</td></tr><tr><td>0.10</td><td>450</td><td>120</td></tr><tr><td>0-10 (from Ref. 3)</td><td>450</td><td>165</td></tr><tr><td>0.05-0.20 (from Ref. 4)</td><td>450</td><td>65</td></tr></table>

TABLE III: Typical values of the thermopower of  \( CuRh_{1-x}Mg_{x}O_{2} \) .
 
![](./images/867768172088918988_10.jpg)

FIG. 9: (Color online) Temperature dependence of the thermopower of  \( CuRh_{1-x}Mg_{x}O_{2} \)  for x = 0, x = 0.01, x = 0,04, and x = 0.10. Lines are guide for the eyes, only.

ways increasing with T as shown for  \( CuRh_{0.90}Mg_{0.10}O_{2} \)  in Fig. 9. In contrast, the localizing behavior of  \( CuRhO_{2} \)  is reflected by the  \( S(T) \)  curves showing an upturn towards high S values as T decreases below  \( \sim 450 \)  K. For all  \( x > 0.01 \) , or for  \( T > 450 \)  K (for x = 0.00 and x = 0.01) the  \( S(T) \)  curves exhibit an almost  \( S \propto T \)  regime as shown by the lines drawn on the  \( S(T) \)  curves in Fig. 9. Such a T dependence is characteristic of a metallic behavior. As previously reported for  \( CuRh_{0.90}Mg_{0.10}O_{2} \) , this behavior leads to rather large positive values, larger than  \( 300 \mu V K^{-1} \)  at 1000 K for x = 0.00 and x = 0.01. The decrease of S as x increases together with the positive sign of S is consistent with an increase of the hole ( \( Rh^{4+} \) ) fraction induced by charge compensation created by the  \( Mg^{2+} \)  for  \( Rh^{3+} \)  substitution.

Remarkably, all these trends are in good qualitative agreement with the theoretical findings presented in Sec. III A. Yet, the experimentally obtained values at 1000 K are somewhat smaller than the theoretically predicted ones. One is therefore tempted to analyze the above experimental data within a completely different approach, namely, the temperature independent correlation functions ratio approximation (TICR). \( ^{38} \)  In this approach, the thermopower arising from the Kubo formalism

 \[ S(T)=\frac{1}{eT}\frac{\langle j_{E}j_{n}\rangle-\mu\langle j_{n}j_{n}\rceil}{\langle j_{n}j_{\bar{n}}\rangle} \quad (4) \] 

is approximated by assuming that the energy current-particle current correlation function and the particle current autocorrelation function share the same temperature dependence. Thus their ratio should result in a hyperbolic offset of strength  \( E_{0} \)  of the thermopower as

 \[ S(T)=\frac{1}{eT}(E_{0}-\mu(T)). \quad (5) \] 

At high temperatures the temperature dependence of the thermopower is governed by the one of the chemical potential which follows from

 \[ n(T)=\int\mathrm{d}\epsilon f(E-\mu)\rho(E). \quad (6) \] 

Here,  \( f(E) \)  again denotes the Fermi function and  \( \rho(E) \)  is the density of states. In the present context, the latter is taken from the electronic structure calculations (Fig. 4). Yet, within the present model there is still room for improvement especially at high temperatures. This goes mainly along two different directions. One way to improve on the TICR as covered by (5)/(6) would be to use a modified density of states resulting from the GGA result by a rigid energetical upshift of the conduction bands. However, for reasonable values of the latter, it turned out that the thermopower shows little sensitivity to the actual optical band gap. From this, we can furthermore conclude that the behavior of the thermopower is dominated by the holes in the valence bands.

Another direction is provided by the observation that, in many cases, the thermopower tends to loose its temperature dependence above room temperature, see e. g. Ref. 39. With this motivation, the TICR expression (5) was extended by adding a temperature independent contribution  \( S_{0} \)  to  \( S(T) \) . Such a contribution is often attributed to localized degenerate states. Here they may derive from the pockets on the Fermi surface centered around the H and A points that are characterized by small Fermi velocities (see Fig. 3). As a consequence, within the extended TICR the thermopower is determined by two parameters, namely,  \( E_{0} \)  and  \( S_{0} \) , which, together with the GGA DOS, can be used to fit the experimental data. The result is shown in Fig. 10 for all three doped samples. Regarding  \( E_{0} \) , the values range from 40 meV to 90 meV, thereby being quite similar to the ones reported for electron-doped manganites. In these materials a large density of states at the bottom

![](./images/867768172088918988_11.jpg)

FIG. 10: (Color online) Comparison of the different theoretical models, including the temperature independent contribution  \( S_{0} \) , (lines) with our experimental values (symbols) of the temperature dependence of the thermopower of  \( CuRh_{1-x}Mg_{x}O_{2} \)  for x = 0.01, x = 0.04, and x = 0.10
 

of the band results in low degeneracy temperatures and large negative thermopower. \( ^{38} \)  For the title compounds, the density of states at the top of the valence band is large, resulting in the large positive thermopower, together with low degeneracy temperature. The  \( S_{0} \)  values are quite large ( \( 40\mu VK^{-1} \leq S_{0} \leq 100\mu VK^{-1} \) ) and appear to be comparable to the ones reported for various layered colbatates, in which the here considered  \( RhO_{2} \)  layers are replaced by isostructural  \( CoO_{2} \)  layers. \( ^{39} \)  Additionally, the fact that the thermopower data for all three doped samples could be reproduced using the same DOS for both the extended TICR model and the GGA calculations is quite remarkable. This gives a strong support to use the rigid band model.

In order to check the thermoelectric performance, we now address the power factor PF (PF =  \( \frac{S^{2}}{\rho} \) ). Combining their T dependences,  \( S \propto T \)  and  \( \rho \propto T^{2} \)  at sufficiently high temperature, this leads to remarkable T-independent values of the PF as shown in Fig. 11. The

![](./images/867768172088918988_12.jpg)

FIG. 11: (Color online) Temperature dependence of the power factor of  \( CuRh_{1-x}Mg_{x}O_{2} \)  for x = 0, x = 0.01, x = 0  \( \cdot \)  0.04, and x = 0.10. Lines are guide for the eyes, only.

best values are observed for the most substituted samples exhibiting a value of the PF = 7 10 \( ^{-4} \) WK \( ^{-2} \) m \( ^{-1} \) . As shown in Fig. 11 and in good qualitative agreement

 \( ^{1} \)  Y. Ono, K. Satoh, T. Nozaki, and T. Kajitani, Jap. J. Appl. Phys. 46, 1071 (2007).

 \( ^{2} \)  K. Hayashi, T. Nozaki, and T. Kajitani, Jap. J. Appl. Phys. 46, 5226 (2007); T. Nozaki, K. Hayashi, T. Kajitani, J. Chem. Eng. Jap. 40, 1205 (2007).

 \( ^{3} \)  H. Kuriyama, M. Nohara, T. Sasagawa, K. Takubo, T. Mizokawa, K. Kimura, and H. Takagi, Proc. 25th Int. Conf. Thermoelectrics (IEEE, Piscataway, 2006), p. 97.

 \( ^{4} \)  S. Shibasaki, W. Kobayashi, and I. Terasaki, Phys. Rev. B 74, 235110 (2006).

with the calculations presented in Sec. III A, the values are found to increase as x increases in  \( CuRh_{1-x}Mg_{x}O_{2} \)  showing that the induced relative  \( \rho \)  decrease is more than compensating the S decrease.

## IV. CONCLUSION

In summary, Mg-doped  \( CuRhO_{2} \)  has been investigated by means of electronic structure calculations, structural characterization, and transport measurements. The electronic structure calculations clearly indicate that the transport is dominated by the Rh 4d bands. Structural data demonstrate that the solubility limit of Mg in  \( CuRhO_{2} \)  is as high as 12%, provided the samples are prepared at temperatures above  \( \sim1000^{\circ}C \) , in which case Rh is indeed substituted by Mg. This substitution results in a peculiar hole doping of the rather narrow Rh 4d bands, shown by a  \( T^{2} \)  dependence of the resistivity, a T dependence of the thermopower, and a quite large nearly T independent power factor, up to temperatures as high as 1000 K. Regarding the thermopower, good qualitative agreement between the theoretical prediction arising from the GGA+Boltzmann approach and experimental data is obtained. Yet, an additional purely entropic contribution needs to be invoked when treating the GGA results in the TICR framework for quantitative explanation, in a similar fashion as what was found in cobaltites with isostructural  \( CoO_{2} \)  layers. \( ^{39} \)  Thermal conductivity measurements performed on dense samples would be necessary to measure the figure of merit. Work along this line is in progress.

## V. ACKNOWLEDGMENTS

We gratefully acknowledge many useful discussions with T. Kopp and A. Reller. V.E. is especially grateful to D. Singh for very fruitful discussions during the implementation of the transport properties into the ASW package. This work was supported by the ANR through NEWTOM as well as by the Deutsche Forschungsgemeinschaft through SFB 484 (V.E.) and the Research Unit 960 “Quantum Phase Transitions” (S.K.).

 \( ^{5} \)  V. R. Galakhov, A. I. Poteryaev, E. Z. Kurmaev, V. I. Anisimov, S. Bartkowski, M. Neumann, Z. W. Lu, B. M. Klein, and T.-R. Zhao, Phys. Rev. B 56, 4584 (1997).

 \( ^{6} \)  R. Seshadri, C. Felser, K. Thieme, and W. Tremel, Chem. Mater. 10, 2189 (1998).

 \( ^{7} \)  K. P. Ong, K. Bai, P. Blaha, and P. Wu, Chem. Mater. 19, 634 (2007).

 \( ^{8} \)  D. J. Singh, Phys. Rev. B 76, 085110 (2007).

 \( ^{9} \)  D. J. Singh, Phys. Rev. B 77, 205126 (2008).

 \( ^{10} \)  V. Eyert, R. Frésard, and A. Maignan, Chem. Mat. 20,
 

2370 (2008).

 \( ^{11} \)  V. Eyert, R. Frésard, and A. Maignan, Phys. Rev. B 78, 052402 (2008).

 \( ^{12} \)  A. Maignan, C. Martin, R. Frésard, V. Eyert, E. Guilmeau, S. Hébert, M. Poienar, and D. Pelloquin, Solid State Commun. 149, 962 (2009).

 \( ^{13} \)  H. Usui, R. Arita, and K. Kuroki, J. Phys.: Condens. Matter 21, 064223 (2009).

 \( ^{14} \)  M. Tanaka, M. Hasegawa, and H. Takei, J. Phys. Soc. Japan 65, 3973 (1996).

 \( ^{15} \)  R. D. Shannon, D. B. Rogers, and C. T. Prewitt, Inorg. Chem. 10, 713 (1971); C. T. Prewitt, R. D. Shannon, and D. B. Rogers, ibid. 10, 719 (1971); D. B. Rogers, R. D. Shannon, C. T. Prewitt, and J. L. Gillson, ibid. 10, 723 (1971).

 \( ^{16} \)  J.-P. Doumerc, A. Wichainchai, A. Ammar, M. Pouchard, and P. Hagenmuller, Mat. Res. Bull. 21, 745 (1986).

 \( ^{17} \)  T. Kimura, J. C. Lashley, and A. P. Ramirez, Phys. Rev. B 73, 220401(R) (2006).

 \( ^{18} \)  S. Seki, Y. Onose, and Y. Tokura, Phys. Rev. Lett. 101, 067204 (2008).

 \( ^{19} \)  This value  \( (130\mu\mathrm{VK}^{-1}) \)  is extrapolated from the high-temperature measurements reported in Ref. 3.

 \( ^{20} \)  J. P. Perdew, K. Burke, and M. Ernzerhof, Phys. Rev. Lett. 77, 3865 (1996)

 \( ^{21} \)  A. R. Williams, J. Kübler, and C. D. Gelatt, Jr., Phys. Rev. B 19, 6094 (1979).

 \( ^{22} \)  V. Eyert, Int. J. Quantum Chem. 77, 1007 (2000).

 \( ^{23} \)  V. Eyert, The Augmented Spherical Wave Method – A Comprehensive Treatment, Lect. Notes Phys. 719 (Springer, Berlin Heidelberg 2007).

 \( ^{24} \)  V. Eyert and K.-H. Höck, Phys. Rev. B 57, 12727 (1998).

 \( ^{25} \)  V. Eyert, J. Comp. Phys. 124, 271 (1996).

 \( ^{26} \)  P. E. Blöchl, O. Jepsen, and O. K. Andersen, Phys. Rev. B 49, 16223 (1994).

 \( ^{27} \)  V. Eyert, unpublished

 \( ^{28} \)  M. S. Methfessel, Phys. Rev. B 38, 1537 (1988).

 \( ^{29} \)  J. Rodriguez-Carvajal, Physica B 192, 55 (1993).

 \( ^{30} \)  K. T. Jacob, T. H. Okabe, T. Uda, and Y. Waseda, Bull. Mater. Sci. 22, 741 (1999).

 \( ^{31} \)  H. R. Oswald, P. Kuhn, and A. Reller, Solid State Ionics 32/33, 528 (1989).

 \( ^{32} \)  P. B. Allen, Boltzmann theory and resistivity of metals. In: Quantum Theory of Real Materials, ed by J. R. Chelikowsky and S. G. Louie (Kluwer, Boston 1996) pp 219–250.

 \( ^{33} \)  T. J. Scheidemantel, C. Ambrosch-Draxl, T. Thonhauser, J. V. Badding, and J. O. Sofo, Phys. Rev. B 68, 125210 (2003).

 \( ^{34} \)  G. K. H. Madsen and D. J. Singh, Comput. Phys. Commun. 175, 67 (2006).

 \( ^{35} \)  R. X. Smith, M. J. R. Hoch, P. L. Kuhns, W. G. Moulton, A. P. Reyes, G. S. Boebinger, J. Mitchell, and C. Leighton, Phys. Rev. B 78, 092201 (2008).

 \( ^{36} \)  C. Grygiel, Ch. Simon, B. Mercey, W. Prellier, R. Frésard, and P. Limelette, Appl. Phys. Lett. 91, 262103 (2007).

 \( ^{37} \)  Y. Tokura, Y. Taguchi, Y. Okada, Y. Fujishima, T. Arima,

K. Kumagai, and Y. Iye, Phys. Rev. Lett. 70, 2126 (1993).

 \( ^{38} \)  R. Frésard, S. Hébert, A. Maignan, L. Pi, and J. Hejtmanek, Phys. Lett. A 303, 223 (2002).

 \( ^{39} \)  P. Limelette, S. Hébert, V. Hardy, R. Frésard, Ch. Simon, and A. Maignan, Phys. Rev. Lett. 97, 046601 (2006).
 
