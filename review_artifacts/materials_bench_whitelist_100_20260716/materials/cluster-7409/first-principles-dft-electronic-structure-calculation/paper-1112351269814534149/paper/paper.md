# THz carrier dynamics in $SrTiO_3$/$LaTiO_3$ interface two-dimensional electron gases

Ahana Bhattacharya¹, Andri Darmawan¹², Jeong Woo Han¹, Frederik Steinkamp¹, Nicholas S. Bingham³⁴⁵, Ryan J. Suess¹, Stephan Winnerl⁶, Markus E.Gruner¹², Eric N. Jin⁵⁷, Frederick J. Walker⁵, Charles H. Ahn⁵, Rossitza Pentcheva¹², and Martin Mittendorff¹*

¹Universität Duisburg-Essen, Fakultät für Physik, 47057 Duisburg, Germany
²Universität Duisburg-Essen, Center for Nanointegration (CENIDE), 47057 Duisburg, Germany
³University of Maine, Department of Physics and Astronomy, Orono, ME 04469, USA
⁴University of Maine, Frontier Institute for Research in Sensor Technologies, Orono, ME 04469 USA
⁵Yale University, Department of Applied Physics, New Haven, CT 06511 USA
⁶Helmholtz-Zentrum Dresden-Rossendorf, Bautzner Landstraße 400, 01328 Dresden, Germany
⁷U.S. Naval Research Laboratory, 4555 Overlook Ave, SW Washington, D.C. 20375, USA

* email: martin.mittendorff@uni-due.de

A 2DEG forms at the interface of complex oxides like $SrTiO_3$ (STO) and $LaTiO_3$ (LTO), despite each material having a low native conductivity, as a band and a Mott insulator, respectively. The interface 2DEG hosts charge carriers with moderate charge carrier density and mobility that raised interest as a material system for applications like field-effect transistors or detectors. Of particular interest is the integration of these oxide systems in silicon technology. To this end we study the carrier dynamics in a STO/LTO/STO heterostructure epitaxially grown on Si(001) both experimentally and theoretically. Linear THz spectroscopy was performed to analyze the temperature dependent charge carrier density and mobility, which was found to be in the range of $10^{12}\ \text{cm}^{-2}$ and $1000\ \text{cm}^2\text{V}^{-1}\text{s}^{-1}$, respectively. Pump-probe measurements revealed a very minor optical nonlinearity caused by hot carriers with a relaxation time of several 10ps, even at low temperature. Density functional theory calculations with a Hubbard $U$ term on ultrathin STO-capped LTO films on STO(001) show an effective mass of 0.64-0.68 $m_e$.

### I Introduction

Heterostructures of complex transition metal oxides feature interface phenomena that are distinct from the bulk ranging from the formation of two-dimensional electron gases (2DEGs) to superconductivity or magnetism¹,²,³,⁴,⁵. The 2DEGs originate from a discontinuity in the polarity of the crystal structure at the atomically sharp interfaces⁶. Depending on the composition of the oxide heterostructures, the 2DEG can host charge carriers with high mobility and high carrier density⁷. Electrostatic gating enables control over the charge carrier density, thus making it a feasible option for devices like field-effect transistors or detectors⁸,⁹,¹⁰,¹¹. As it was recently shown, the 2DEG in heterostructures of the band insulator STO and the Mott insulator LTO epitaxially grown on Si(001) features a high carrier density of about $10^{12}\ \mathrm{cm}^{-2}$, with a mobility in the range of $100\ \mathrm{cm^2V^{-1}s^{-1}}$ at room temperature, making it particularly interesting for devices¹². While the dc conductivity has been studied extensively for such structures, there are relatively few studies investigating the THz conductivity¹³,¹⁴. Here we study the non-equilibrium carrier dynamics of the 2DEG at the STO/LTO interface in the vicinity of the Si(001) substrate. Linear THz time-domain spectroscopy reveals the carrier density and mobility as a function of the temperature without the need of electrical contacts, while pump-probe experiments performed in the THz spectral range give insights into the relaxation dynamics of optically excited charge carriers. For the samples investigated in this study, we found a charge carrier density on the order of $10^{12}\ \mathrm{cm}^{-2}$ and mobility in the range of $1000\ \mathrm{cm^2V^{-1}s^{-1}}$, the THz conductivity is well described by the Drude model. Intraband excitation with a fluence of about $200\ \mathrm{nJ\ cm^{-2}}$ leads to a rather small pump-induced increase in transmission of about 0.04%. The experimental results are complemented by density functional theory (DFT) calculations with an on-site Hubbard term to explore the electronic properties of the 2DEG. Our results show an effective mass of 0.64-$0.68\ m_e$, with $m_e$ being the electron rest mass. The calculated effective mass is used as input for simulations of the experimental results via a two-temperature model, which agrees qualitatively with the experimental findings.

## II Experimental Methods and Results

The samples are grown by molecular beam epitaxy (MBE) on a low-doped and high resisitive Si substrate. The heterostructures are comprised of 4.5 unit cells (uc) STO on Si, 2 uc LTO and capped by 5 uc STO. Details of the sample growth can be found in Ref. 12, a sketch of the sample is shown in Fig. 1(a). A second sample of STO on Si, but without the intermediate 2 uc LTO layer, serves as reference for spectroscopic measurements. This way, we can exclude any contribution stemming from a 2DEG forming at the STO/Si interface or the STO/vacuum interface.

![](./images/1112351269814534149_1.jpg)

Figure 1: (a) Sketch of the sample structure. Experimental (b) and fitted (c) THz field transmission ($t$) as a function of the frequency ($f$) and temperature ($\theta$).

To characterize the charge carrier density and mobility as a function of the temperature, we performed THz time-domain spectroscopy (THz TDS). The measurements were performed in a closed-cycle cryostat equipped with z-cut quartz windows, enabling temperature dependent measurements in the temperature range from 5 K to room temperature.

The experimental transmission as a function of the frequency and the temperature is shown in Fig. 1(b), the oscillations of the transmission, appearing as ripples along the temperature axis, are caused by multiple reflections within the sample. Even though 2DEGs in STO are characterized by a rather complex interplay of electron-electron and electron-phonon scattering¹⁵, the THz transmission can be well described with a simple Drude model. To extract the carrier density and mobility from the experimental results, we fit a Drude conductivity in combination with a thin film model to the experimental results via¹⁶

$$
t(\omega)=\left|\frac{E_{\text{sample}}(\omega)}{E_{\text{reference}}(\omega)}\right|=\left|\frac{n_{Si}+1}{n_{Si}+1+Z_{0}\sigma(\omega)}\right|, \qquad \text{Eq. 1}
$$

where $t(\omega)$ is the THz field transmission obtained from the sample and reference spectra $E_{\text{sample}}(\omega)$ and $E_{\text{reference}}(\omega)$, respectively. The refractive index of the substrate is represented by $n_{Si}$, $Z_0$ is the free-space impedance and $\sigma(\omega)$ the sheet conductivity of the 2DEG. The latter is derived from the Drude model via

$$
\sigma(\omega)=\frac{ne^{2}\tau}{m^{*}(1-i\omega\tau)}, \qquad \text{Eq. 2}
$$

where $m^{*}$ represents the effective mass, $\tau$ the momentum scattering time, $n$ is the sheet carrier density and $e$ the electric charge of an electron. The effective mass $m^{*}$ is derived from the DFT simulations as described below. It is obtained by averaging over the calculated values of effective masses of the 2DEG along $\Gamma$-M and $\Gamma$-X directions (the band structure is depicted in Fig. 4c). As a result, we get the charge carrier density and mobility as a function of the temperature as shown in Fig. 2(a) and (b), respectively.

![](./images/1112351269814534149_2.jpg)

Figure 2: Extracted (a) charge carrier density ($n$) and (b) mobility ($\mu$) as a function of the temperature ($\theta$).

The mobility is observed to increase moderately with temperature and reaches significantly above 1000 cm²V⁻¹s⁻¹ before decreasing to about 1160 cm²V⁻¹s⁻¹ at room temperature. The charge carrier density decreases slightly with temperature on heating the sample from 5K to 20K. On heating beyond 20K, charge carrier density increases with temperature, reaching a value of approximately $7.7{\cdot}10^{12}\ \text{cm}^{-2}$ at room temperature, which is consistent with earlier findings¹². The magnitude of the mobility and carrier density lies between those found for the two-carrier model (mobility of 10000 in the silicon and 100 in the oxide layers) used in Ref. 12.

To measure the non-equilibrium carrier dynamics in the 2DEG, we performed

pump-probe experiments at the free-electron laser (FEL) facility FELBE at Helmholtz-Zentrum Dresden-Rossendorf. To efficiently excite the 2DEG via free-carrier absorption and avoid heating via phonon absorption¹⁷, we tuned the FEL to 1.35 THz, corresponding to a photon energy of about 5.6 meV. The FEL provides a continuous pulse train with a repetition rate of 13 MHz¹⁸, a small fraction of about 2% of the FEL power is split off to serve as probe, the polarization is rotated by $90^\circ$ after passing a delay stage. The majority of the FEL power is guided to a parabolic mirror, focusing both, pump and probe beam, on the sample. While the pump beam is blocked behind the sample, the probe beam is guided through an additional polarizer in order to minimize scattered pump radiation, before detection with a bolometer. The sample is mounted in a flow cryostat to maintain a sample temperature of 10 K. In order to avoid spurious pump-probe signals stemming from a potential 2DEG at the STO/ Si(001) interface and/or at the STO/vacuum interface, we performed measurements on the reference sample, observing no measurable change in transmission.

The experiments are performed at four different pump fluences of $16\ \text{nJ}\ \text{cm}^{-2}$, $53\ \text{nJ}\ \text{cm}^{-2}$, $106\ \text{nJ}\ \text{cm}^{-2}$, and $185\ \text{nJ}\ \text{cm}^{-2}$, the corresponding pump-probe signals are shown in Fig. 3(a). As can be seen, only a minor pump-induced change in transmission of about 0.04% is observed at the highest pump fluence. To measure these very small pump-induced changes in transmission, we averaged over 40 measurements at each fluence. After the peak of the pump-probe signal is reached, the signal decays on a time scale of about 50 ps, indicating a fast cooling of the hot carriers. The lines in Fig. 3(a) serve as guide to the eye, indicating standard pump-probe signals that can be described by an error function for the rising edge and an exponential decay for the carrier relaxation. Due to the poor signal-to-noise ratio, the carrier relaxation time cannot be determined precisely. The maximum of the pump-probe signal scales with the square-root of the pump fluence, which is represented by a phenomenological fit as red solid line in Fig. 3(b).

![](./images/1112351269814534149_3.jpg)

Figure 3: Pump-induced change in transmission ($\Delta T/T$) as a function of the delay time ($\Delta t$) for various pump fluences. The solid lines serve as guides to the eye. (b) Maximum pump-induced change in transmission as a function of the applied pump fluence, the red line represents a phenomenological square root fit.

## III Theoretical Results and Discussion

Density functional theory calculations were performed on STO/LTO/STO/Si(001) as well as STO/Si(001) using the Vienna ab-initio package (VASP)$^{19,20,21}$ which implements the projector augmented wave (PAW)$^{22,23}$ method and pseudopotentials. The PBE$^{24}$ exchange-correlation functional within the generalized gradient approximation was used with an on-site Hubbard $U$ term in the rotationally invariant formulation of Dudarev et al. $^{25}$ . Effective corrections $U_{eff}=$ 5 eV and 8 eV are applied on the Ti $3d$ and La

$4f$ states, respectively, consistent with previous work²⁶,²⁷. We employed a $p(2×2)$ lateral unit cell consisting of four inequivalent Ti sites per layer in order to allow octahedral tilts and rotations, as well as an antiferromagnetic G-type ordering for the bulk LTO phase. The lateral lattice constant is fixed to the experimental lattice constant of Si (5.43Å) exposing the STO and LTO films to -1.70% and - 4.04% compressive strain, respectively. Asymmetric slabs were utilized with a 1ML STO capping layer, followed by 2MLs of LTO and 3MLs of STO on 9 MLs reconstructed Si(001) substrate, whose bottom side is passivated by H. A vacuum region of 30Å is added to avoid interactions between the slab and its periodic images. Additionally, we have considered 3ML STO/Si(001) as a reference system. We model the interface between STO and Si(001)²⁸ by a SrO-termination at the reconstructed Si(001) interface, as previously reported by Chen et al²⁹. Overall, the studied systems contain 164 and 104 atoms for STO/LTO/STO/Si(001) and STO/Si(001), respectively. We used an energy cut-off of 500 eV and sampled the Brillouin zone using a $5×5×1$ $\Gamma$-centered $k$-mesh. The ionic positions were fully relaxed.

![](./images/1112351269814534149_4.jpg)

Figure 4: Spin density of (a) STO/LTO/STO on reconstructed Si(001) and (b) STO on reconstructed Si(001), (integrated between -0.6 eV and the Fermi energy at $E_F$=0 with isosurface value of 0.0006 e/Å³). The lower panels show the site-resolved band structure along the $\Gamma$-M and $\Gamma$-X directions in (c) STO/LTO/STO/Si(001) and (d) STO/Si(001).

Figs. 4a and b displays side views of the relaxed systems. For STO/LTO/STO/Si(001) the spin-density, integrated from -0.6 eV to $E_F$, displays a significant contribution at the LTO/STO interface with $d_{xy}$ orbital polarization at the Ti sites as well as at the topmost Si layers. The band structure shown in Fig.4c indicates that several conduction bands cross the Fermi level and thus contribute to the metallicity of the system and the formation of a 2DEG. The main contribution arises from Ti $3d$ states at the LTO/STO interface with some participation of Si at the STO/Si(001) interface (IF-3). The carriers at the LTO/STO interface have mainly $d_{xy}$ character, wheereas the $d_{xz}$ and $d_{yz}$ orbitals

are lying above the Fermi level, while for LTO/STO(001) without a Si substrate, the carriers involved in the formation of the 2DEG are predominantly $d_{xy}$ and $d_{xz+yz}$ orbitals$^{30}$.

Furthermore we have calculated the effective mass of the bands at the LTO/STO interface contributing to the 2DEG along the $\Gamma$-M and $\Gamma$-X directions- from the band stucture depicted in Fig. 4c. The calculated effective mass along $\Gamma$-M direction is $0.64m_e$ while along $\Gamma$-X direction is $0.68m_e$. Those bands are stemming from the $3d_{xy}$ orbitals of Ti at the LTO/STO interface. In contrast, the reference system shows only two bands crossing at $E_F$, a hole band contributed by O at the surface (IF+3) as well as an electron band of Si at the interface (IF-3) as seen in Fig. 4d. Our results show that the 2DEG at the LTO/STO interface has predominantly Ti $d_{xy}$ character.

To simulate the dynamics of the 2DEG, we perform calculations based on a two-temperature model via $\alpha_e \theta \frac{d\theta}{dt}+\beta(\theta-\theta_l)=A(\theta)I(t),$
Eq. 3

where $\alpha_e$ represents the specific heat of the 2DEG, which can be derived from the effective mass, assuming a parabolic dispersion relation. The temperature of the 2DEG and the lattice are represented by $\theta$ and $\theta_l$, respectively. $\beta$=$1.4 \cdot 10^4 W m^{-2} K^{-1}$ is a fit parameter for the carrier relaxation time, $A(\theta)$ is the absorption of the 2DEG derived from the thin film model at the photon frequency applied in the experiment (1.35 THz), and $I(t)$ describes the temporal evolution of the pump pulse. The temperature dependent parameters for the absorption, i.e. the carrier density and mobility, are interpolated from the THz TDS results shown in Fig. 2. From the temporal evolution of the electron temperature, we calculated the pump-induced change in transmission via the thin-film model shown in Fig. 5(a), Fig. 5(b) shows the maximum change in transmission as a function of the pump fluence. While the theoretical results qualitatively reproduce the experimental results including the fluence dependence, the absolute values are about five times higher than experimentally observed. From the specific heat mentioned above, we estimate a maximum increase of the electron temperature of about 18 K. We note that the quantitative deviation between the two-temperature model and the experimental results is likely related to the fundamental difference between the

pump-probe experiments and the THz TDS measurements: while the THz TDS measurements were taken at equilibrium, i.e. both, electrons and lattice have the same temperature, the pump-probe measurements probe a hot carrier distribution in a cold lattice.

![](./images/1112351269814534149_5.jpg)

Figure 5: (a) Simulated pump-induced change in transmission ($\Delta T/T$) derived from a two-temperature model. (b) Simulated maximum of the pump-induced change in transmission as a function of the applied pump fluence.

The pump-induced change in transmission is rather small compared to other 2DEGs based on conventional heterostructures$^{31,32}$. We attribute the remarkably small pump-probe signals to the temperature dependence of the oxide-interface 2DEG in our STO/LTO heterostructure. In the interfacial 2DEGs studied here, we see the carrier density initially decreases with increasing temperature at first and reaches a minimum value at 20 K. Only for temperatures above this minimum value is an increase in carrier density

observed (cf. Fig. 2(a)). The mobility in the STO/LTO 2DEG increases until a temperature of about 80 K beyond which it shows a small drop, indicating weak electron-phonon scattering. The decrease in mobility below 80K as well as the initial decrease of carrier density with temperature point towards the presence of ionized impurities at the interface. The trends observed in the carrier density and mobility in the STO/LTO 2DEG are counteracting on the transmission/absorption of THz radiation, resulting in the very small pump-induced change in transmission observed in our pump-probe experiments.

### IV. Summary
In conclusion, we investigated the physical properties of the 2DEG formed at the STO/LTO interface via THz TDS and high intensity THz pump-probe measurements. The experiments are complemented by DFT+U calculations of the 2DEG that find an effective mass of 0.64-0.68 $m_e$. The optical properties and the dynamical evolution of the 2DEG are modelled via thin-film model and two-temperature model, respectively. We found a surprisingly low impact of the intraband excitation on the sample conductivity, that resulted in small pump-induced changes of the transmission that were less than 0.05%.

Acknowledgment

This study was funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation)—Project-ID 278162697—SFB1242. We thank J. Michael Klopf and the ELBE team for their assistance. Work at Yale supported by the Office of Naval Research Multidisciplinary University Research Initiative to support the EXtreme Electron DEvices (EXEDE) program (synthesis and characterization) and by NSF DMR-2412358 (analysis).


$^{1}$ J. Mannhart and D. G. Schlom, "Oxide Interfaces – An Opportunity for Electronics," Science **327**, 1607 (2010), DOI: 10.1126/science.1181862.

$^{2}$ H. Y. Hwang, Y. Iwasa, M. Kawasaki, B. Keimer, N. Nagaosa, and Y. Tokura, "Emergent phenomena at oxide interfaces," Nat. Mater. **11**, 103 (2012), DOI: 10.1038/NMAT3223.

$^{3}$ S. Stemmer and S. J. Allen, "Two-Dimensional Electron Gases at Complex Oxide Interfaces," Annu. Rev. Mater. Res. **44**, 151 (2014), DOI: 10.1146/annurev-matsci-070813-113552.

$^{4}$ Y.-Y. Pai, A. Tylan-Tyler, P. Irvin, and J. Levy, "Physics of SrTiO₃-based heterostrcutures and nanostructures: a review," Rep. Prog. Phys. **81**, 036503 (2018), DOI: 10.1088/1361-6633/aa892d.

$^{5}$ M. Yang, Ariando, J. Zhou, T. C. Asmara, P. Krüger, X. J. Yu, X. Wang, C. Sanchez-Hanke, Y. P. Feng, T. Venkatesan, and A. Rusydi, "Direct Observation of Room-Temperature Stable Magnetism in LaAlO₃/SrTiO₃ Heterostructures," ACS Appl. Mater. Interfaces **10**, 9774 (2018), DOI: 10.1021/acsami.7b12945.

$^{6}$ A. Ohtomo and H. Y. Hwang, "A high-mobility electron gas at the LaAlO₃/SrTiO₃ heterointerface," Nature **428**, 423 (2004), DOI: 10.1038/nature02308.

$^{7}$ K. Yang, S. Nazir, M. Behtash, and J. Cheng, "High-Throughput Design of Two-Dimensional Electron Gas Systems Based on Polar/Nonpolar Perovskite Oxide Heterostructures," Scientific Reports **6**, 34667 (2016), DOI: 10.1038/srep34667.

$^{8}$ C. W. Schneider, S. Thiel, G. Hammerl, C. Richter, and J. Mannhart, "Microlithography of electron gases formed at interfaces in oxide heterostructures," Appl. Phys. Lett. **89**, 122101 (2006), DOI: 10.1063/1.2354422.

$^{9}$ C. Cen, S. Thiel, J. Mannhart, and J. Levy, "Oxide Nanoelectronics on Demand," Science **323**, 1026 (2009), DOI: 10.1126/science.1168294.

$^{10}$ D. F. Bogorin, C. W. Bark, H. W. Jang, C. Cen, C. M. Folkman, C.-B. Eom, and J. Levy, "Nanoscale rectification at the LaAlO₃/SrTiO₃ interface," Appl. Phys. Lett. **97**, 013102 (2010), DOI: 10.1063/1.3459138.

$^{11}$ P. D. Eerkes, W. G. van der Wiel, and H. Hilgenkamp, "Modulation of conductance and superconductivity by top-gating in LaAlO₃/SrTiO₃ 2-dimensional electron system," Appl. Phys. Lett. **103**, 201603 (2013), DOI: 10.1063/1.4829555.

$^{12}$ E. N. Jin, A. Kakekhani, S. Ismail-Beigi, C. H. Ahn, and F. J. Walker, "Two-dimensional electron gas oxide remote doping of Si(001)," Phys. Rev. Mater. **2**, 115001 (2018), DOI: 10.1103/PhysRevMaterials.2.115001.

$^{13}$ A. Dubroka, M. Rössle, K. W. Kim, V. K. Malik, L. Schlutz, S. Thiel, C. W. Schneider, J. Mannhart, G. Herranz, O. Copie, M. Bibes, A. Barthelemy, and C. Bernhard, "Dynamical Response and Confinement of the Electrons at the LaAlO₃/SrTiO₃ Interface," Phys. Rev. Lett. **104**, 156807 (2010), DOI: 10.1103/PhysRevLett.104.156807.

$^{14}$ X. Liu, J. Zhang, Z. Zhang, X. Lin, Y. Yu, X. Xing, Z. Jin, Z. Cheng, and G. Ma, "Thermodynamics of quasi-2D electron gas at BFO/Si interface probed with THz time-domain spectroscopy," Appl. Phys. Lett. **111**, 152906 (2017), DOI: 10.1063/1.4989667.

$^{15}$ P. D. C. King, S. McKeown Walker, A. Tamai, A. ke la Torre, T. Eknapakul, P. Buaphet, S.-K. Mo, W. Meevasana, M. S. Bahramy, and F. Baumberger, "Quasiparticle dynamics and spin-orbital texture of the SrTiO₃ two-dimensional electron gas," Nat. Commun. **5**, 3414 (2014), DOI: 10.1038/ncomms4414.

$^{16}$ J. Lloyd-Hughes and T.-I. Jeon, "A Review of the Terahertz Conductivity of Bulk and Nano-Materials," J. Infrared Milli. Terahz. Waves **33**, 871 (2012), DOI: 10.1007/s10762-012-9905-y.

$^{17}$ D. Nuzhnyy, J. Petzelt, S. Kamba, T. Yamada, M. Tyunina, A. K. Tagantsev, J. Levoska, and N. Setter, "Polar phonons in some compressively stressed epitaxial and polycrystalline SrTiO₃ thin films," J. Electroceram. **22**, 297 (2009), DOI: 10.1007/s10832-008-9494-2.

$^{18}$ M. Helm, S. Winnerl, A. Pashkin, J. M. Klopf, J.-C. Deinert, S. Kovalev, P. Evtushenko, U. Lehnert, R. Xiang, A. Arnold, A. Wagner, S. M. Schmidt, U. Schramm, T. Cowan, and P. Michel, "The ELBE infrared and THz facility at Helmholtz-Zentrum Dresden-Rossendorf," Eur. Phys. J. Plus **138**, 158 (2023), DOI: 10.1140/epjp/s13360-023-03720-z.

$^{19}$ G. Kresse and J. Hafner, "Ab initio molecular dynamics for liquid metals," Phys. Rev. B **47**, 558 (1993), DOI: 10.1103/PhysRevB.47.558

$^{20}$ G. Kresse and J. Furthmueller, "Efficiency of ab-initio total energy calculations for metas and semiconductors using a plane-wave basis set," Comput. Mater. Sci. 6, 15 (1996), DOI: 10.1016/0927-0256(96)00008-0.

$^{21}$ G. Kresse and J. Furthmueller, "Efficient iterative schemes for ab initio total-energy calculations using a plane wave basis set," Phys. Rev. B 54, 11169 (1996), DOI: 10.1103/PhysRevB.54.11169

$^{22}$ P. E. Blochl, Projector augmented-wave method, Phys. Rev. B 50, 17953 (1994), DOI: 10.1103/PhysRevB.50.17953

$^{23}$ G. Kresse and D. Joubert, "From ultrasoft pseudopotentials to the projector augmented-wave method," Phys. Rev. B 59, 1758 (1999), DOI: 10.1103/PhysRevB.59.1758

$^{24}$ P. Perdew, K. Burke, and M. Ernzerhof, "Generalized gradient approximation made simple," Phys. Rev. Lett. 77, 3865 (1996), DOI: 10.1103/PhysRevLett.77.3865

$^{25}$ S. L. Dudarev, G. A. Botton, S. Y. Savrasov, C. J. Humphreys, and A. P. Sutton, "Electron-energy-loss spectra and the structural stability of nickel oxide: An LADA+ U study," Phys. Rev. B 57, 1505 (1998), DOI: 10.1103/PhysRevB.57.1505

$^{26}$ S. Okamoto, A. J. Millis, and N. A. Spaldin, "Lattice Relaxation in Oxide Heterostructures: LaTiO₃/SrTiO₃ Superlattices," Phys. Rev. Lett. 97, 056802 (2006), DOI: 10.1103/PhysRevLett.97.056802

$^{27}$ D. Doennig, W. E. Pickett, and R. Pentcheva, "Massive Symmetry Breaking in LaAlO₃/SrTiO₃(111) Quantum Wells: A Three-Orbital Strongly Correlated Generalization of Graphene," Phys. Rev. Lett. 111, 126804 (2013), DOI: 10.1103/PhysRevLett.111.126804

$^{28}$ A.M. Kolpak, F. J. Walker, J.W. Reiner, Y. Segal, D. Su, M. S. Sawicki, C. C. Braodbridge, Z. Zhang, Y. Zhu, C. H. Ahn, and S. Ismail-Beigi, "Interface-Induced Polarization and Inhibition of Ferroelectricity in Epitaxial SrTiO₃/Si," Phys. Rev. Lett. 105, 217601 (2010), DOI: 10.1103/PhysRevLett.105.217601.

$^{29}$ T. Chen, K. Ahmadi-Majlan, Z. H. Lim, Z. Zhang, J. H. Ngai, and D. P. Kumah, "Effect of buffer termination on intermixing and conductivity in LaTiO₃/SrTiO₃ heterostructures integrated on Si(110)," J. Vac. Sci. Technol. A 1 40, 013206 (2022), DOI: 10.1116/6.0001464

$^{30}$ M. J. Veit, R. Arras, B. J. Ramshaw, R. Pentcheva, and Y. Suzuki, "Nonzero Berry phase in quantum oscillations from giant Rashba-type spin splitting in LaTiO₃/SrTiO₃ heterostructures," Nat. Commun. 9, 1458 (2018), DOI: 10.1038/s41467-018-04014-0.

$^{31}$ J. R. Danielson, Y.-S. Lee, J. P. Prineas, J. T. Steiner, M. Kira, and S. W. Koch, "Interaction of Strong Single-Cycle Terahertz Pulses with Semiconductor Quantum Wells," Phys. Rev. Lett. 99, 237401 (2007), DOI: 10.1103/PhysRevLett.99.237401.

$^{32}$ D. Sabbagh, J. Schmidt, S. Winnerl, M. Helm, L. Di Gaspare, M. De Seta, M. Virgilio, and M. Ortolani, "Electron Dynamics in Silicon-Germanium Terahertz Quantum Fountain Structures," ACS Photonics 3, 403 (2016), DOI: 10.1021/acsphotonics.5b00561.