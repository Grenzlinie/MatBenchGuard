# Titanium $3d$ ferromagnetism with perpendicular anisotropy in defective anatase

Markus Stiller, $^{1,{*}}$ Alpha T. N'Diaye, $^{2}$ Hendrik Ohldag, $^{2,3}$ José Barzola-Quiquia, $^{1}$ Pablo D. Esquinazi, $^{1}$ Thomas Amelal, $^{4,\dagger}$ Carsten Bundesmann, $^{4}$ Daniel Spemann, $^{4}$ Martin Trautmann, $^{5}$ Angelika Chassé, $^{5}$ Hichem Ben Hamed, $^{5}$ Waheed A. Adeagbo, $^{5}$ and Wolfram Hergert $^{5}$

$^{1}$Division of Superconductivity and Magnetism, Felix-Bloch-Institute for Solid-state Physics, University of Leipzig, 04103 Leipzig, Germany
$^{2}$Advanced Light Source, Lawrence Berkeley National Laboratory, Berkeley, California 94720, USA
$^{3}$Stanford Synchrotron Radiation Lightsource, SLAC National Accelerator Laboratory, Menlo Park, California 94025, USA
$^{4}$Leibniz Institute of Surface Engineering (IOM), Ion Source Development and Application Group, 04318 Leipzig, Germany
$^{5}$Institute of Physics, Martin-Luther-Universität Halle-Wittenberg, 06120 Halle, Germany

![](./images/812691455427477504_1.jpg)
(Received 27 September 2019; revised manuscript received 12 November 2019; published 9 January 2020)

This work focuses on the generation of ferromagnetism at the surface of anatase TiO$_2$ films by low-energy ion irradiation. Controlled Ar$^+$-ion irradiation resulted in a thin ($\sim$10) nm ferromagnetic surface layer. The intrinsic origin and robustness of the magnetic order has been characterized by x-ray magnetic circular dichroism at room temperature revealing that a Ti band is spin-polarized. These results, together with density functional theory calculations, indicate that Ti vacancy-interstitial pairs are responsible for the magnetic order. Superconducting quantum interference device measurements show the existence of a perpendicular magnetic anisotropy and a low remanent magnetization. Magnetic force microscopy reveals that this low remanence is due to oppositely aligned magnetic domains with magnetization vectors normal to the main surface. The weak domain-wall pinning, the magnetic anisotropy, together with the simplicity of the preparation method, open up interesting possibilities for future applications. As an example, single domain patterns of $\sim$1 $\mu$m width and several $\mu$m length can be easily prepared.

DOI: 10.1103/PhysRevB.101.014412

## I. INTRODUCTION

Since ferromagnetism at higher temperature in semiconductors, such as ZnO or GaAs, was theoretically predicted, many groups have investigated this topic [1]. For example, codoped TiO$_2$ has drawn interest as dielectric material exhibiting colossal permittivity [2] as well as magnetism [3], thus turning it into a multiferroic system. Over the years, ferromagnetism has been observed also in many undoped oxides, such as HfO$_2$ [4–7], CeO$_2$ [8], TiO$_2$ [7,9,10], In$_2$O$_3$ [7,8], ZnO [8,11–13], Al$_2$O$_3$ [8], or SnO$_2$ [5,8,14]. It became evident that doping was not necessary because the magnetism is related to crystal defects, and consequently it can be accompanied by a magnetocrystalline anisotropy. Magnetic oxides are not only interesting from a physics point of view, but they are also important for applications in many fields, such as magnetic storage [15], hybrid complementary metal oxide semiconductor or magnetic logic [16,17], high-frequency components [18–21], magnetic field sensors [22], biomedical applications [23], or giant magnetoresistance sensors [24,25]. Perpendicular magnetic anisotropy (PMA) is a desired condition for magnetic thin films because of its importance for high-density energy storage as magnetic random access memory devices [26–32], the enhanced magneto-optical Kerr rotation [33–35], spin-transfer torque [36,37], and spin-orbit torque [38]. The requirements for new magnetic storage devices demand miniaturization, i.e., magnetic bits of the order of 10 nm or less. To extend the superparamagnetic limit and obtain higher bit densities [39], materials showing PMA with large anisotropy are of special interest [40].

Magnetic anisotropy can have bulk and/or interfacial contributions originating from spin-orbit interactions [41], which induces a coupling between the magnetization and the crystallographic lattice [42–44]. Large anisotropies are usually found in materials that have large spin-orbit coupling, such as heavy elements (Pt, Au,...) or rare earths with nonzero orbital momentum. In multilayers, magnetic anisotropy has been found in the case of a broken symmetry at interfaces [45,46], a crystallographic mismatch between the layers leading to magnetostriction effects [47], or electron hybridization across the interface [48]. This occurs especially at the metal/oxide interfaces, due to hybridization of the metal $3d_{xz}$, $3d_{yz}$, or $3d_{z^2}$ orbitals and the oxide $2p$ orbitals [49,50]. Studies also showed that the interfacial effects are sensitive to their quality, [51] and interfacial anisotropy energies of the order of $\approx$1.5 mJ/m$^2$ for, e.g., Co(Fe)(B) [27,52], are typical. Such interfacial PMA is mainly known to occur in bi(tri)layers made of an oxide and a magnetic layer (and a heavy metal film) [28,46,50,53–58].

In contrast to Co/Pt-based multilayers, films based on ferromagnet/oxide interfaces [54] exhibit a much lower coercivity, despite the PMA. This is favorable for studies of domain wall propagation as record domain wall speeds were obtained [59,60] and are, therefore, good candidates for racetrack memories [61]. Voltage control of magnetism in such systems [59,62–64] could be used for low-power nonvolatile

$^*$markus.stiller@uni-leipzig.de
$^\dagger$Present address: Empa, Swiss Federal Laboratories for Materials Science and Technology, Dübendorf CH-8600, Switzerland.

---
2469-9950/2020/101(1)/014412(10) 014412-1 ©2020 American Physical Society

memories and logic devices, in contrast to current controlled devices.

This work presents a way to produce a magnetic layer at the surface of $TiO_2$ anatase by low-energy $Ar^{+}$-ion irradiation [65]. Defect-induced magnetism in $TiO_2$ has been studied in the past [7,66–70], achieving Curie temperatures of up to 880 K [10,69]. The main difference between our approach and those published is related to the low ion energy and fluences we use, which allow us to produce a robust magnetic layer close to the surface of the films. In general, magnetism could arise from cation and anion defects. Several mechanisms have been proposed for both cases in $TiO_2$ [7,10,66–75]. To clarify the nature of the ferromagnetism, we used element-specific techniques, i.e., x-ray absorption spectroscopy (XAS) and x-ray magnetic circular dichroism (XMCD). The spectra were obtained by recording the total electron yield (TEY) and the luminescence yield (LY). Detailed theoretical investigations of structural and magnetic properties of defects by means of density functional theory (DFT) serve to calculate the XMCD spectra and indicate that the origin of the magnetism is di-Frenkel pairs (di-FPs), that the Ti band is spin-polarized, and, to an extent, also the hybridized O $2p$ band. Magnetic force microscopy (MFM) shows the presence of magnetic domain structures with opposite magnetization directions aligned normal to the film surface.

## II. METHODS
### A. Sample preparation and irradiation

The samples were prepared in three steps: (i) growth of amorphous $TiO_2$ films by ion beam sputter deposition (IBSD), (ii) crystallization by postgrowth annealing, and (iii) defect generation by low-energy ion irradiation.

IBSD uses a low-energy ion beam for sputtering a target [76]. The sputtered particles condense on a substrate and a film begins to grow. In the case of compound materials, for instance oxides and nitrides, additional $O_2$ or nitrogen background gas is provided in order to generate stoichiometric thin films. The amorphous $TiO_2$ thin films were grown using a Ti target, Xe ions with an energy of 1000 eV, and $O_2$ background gas with a partial pressure of about $1.5 \times 10^5$ mbar on $LaAlO_3$ (100) substrates (size $5 \times 5$ $mm^2$). The sputtering geometry with a scattering angle of $110^\circ$ was chosen in order to get a low fraction of Xe particles inside the $TiO_2$ film (less than 0.1%). The film thickness was about 40 nm. More details are given in Ref. [77].

Postgrowth annealing was performed at $T = 1000$ K for 1 h at ambient conditions. As a result, polycrystalline and epitaxial samples were obtained. Thereafter, the anatase films were irradiated with $Ar^+$ ions with an energy of 200 eV, a fluence of $1 \times 10^{15}$ $cm^{-2}$ $s^{-1}$, and at normal incidence. The penetration depth is about 10 nm.

### B. Magnetic force microscopy

Magnetic force microscopy (MFM) measures the magnetic stray fields of a sample, making it possible to detect magnetic domain structures. The film for MFM measurements was patterned using standard lithography processes, i.e., a thin film was covered with a resist, and electron beam lithography was used to prepare a mask. The resulting irradiated lines have a width of $\approx$750 nm. After irradiation with $Ar^+$ ions, the whole mask was completely removed. The MFM measurements were performed using a conventional MFM device (Veeco) with standard MFM tips (Bruker, $k = 3$ N m$^{-1}$, $Q = 220$, $r = 35$ nm). During the measurement of the magnetic lines, the lift scan height was kept at 50 nm and the tip velocity was 5 $\mu$m/s.

The MFM measurements of the film, which has also been characterized using the SQUID, were done using different parameters. To enhance the sensitivity, a negative lift height of $-$10 nm was chosen and the drive amplitude was reduced during interleave scan, such that the tip did not strike the surface. Yet, surface artifacts cannot be avoided completely and are visible in all pictures as bright dots.

### C. Density functional theory

The density functional theory (DFT) calculations were carried out using the projector augmented-wave method [78,79] as implemented in the Vienna ab initio simulation package (VASP) [80,81]. The exchange correlation functional of Perdew-Burke-Ernzerhof [82] is used with an isotropic screened on-site Coulomb interaction [83] of $U = 4$ eV, applied on Ti $3d$ orbitals. The literature propose a large variety of $U$ values from $U = 2.5$ to 10 eV. We refer, for example, to the work of Hu [84], where an intensive discussion of the different $U$ values for $TiO_2$ is given. Our choice of $U = 4$ eV is based on the best compromise between the reported values for both defect and defect-free systems [84]. The kinetic energy cutoff for the plane waves was set to 600 eV. Brillouin zone integrations were made using a $\Gamma$-centered $k$-point mesh sampling of $2 \times 2 \times 3$ $k$-points for the structural relaxation and a $6 \times 6 \times 8$ $k$-point mesh for the density of states calculation. The atomic coordinates in the supercells were relaxed with the conjugate gradient method and within a force convergence threshold of 10 meV/Å to minimize the internal forces. The cell volume is fixed to its experimental value [85] throughout the whole work.

The defects are simulated using a supercell repeating the tetragonal cell $3 \times 3 \times 1$ times, resulting in a total of 108 sites and a defect concentration of about 5.5%. The di-FP defect is formed by two Ti vacancies and two Ti interstitials simultaneously, thus the total number of atoms is conserved. The extent of each Frenkel pair (distance vacancy to its corresponding interstitial) is varied from 3 Å [first nearest neighbor (NN)] to 10 Å (twelfth NN). The interstitial atoms were inserted at the empty spheres positions, which were determined using the STUTTGART TB-LMTO program [86]. This latter takes into account the space group symmetry operations to fill in the voids between atoms with empty spheres. In addition, the distance separating two vacancies in the di-FP is varied from first NN to ninth NN. This leads in total to 108 different defect configurations. The structural data found in the DFT calculations will serve as input for the XMCD calculations.

### D. X-ray absorption spectra and magnetic circular dichroism

The XAS Ti $L$ edge calculations were performed with MULTIX [87]. Within this program, the energy levels of an

![](./images/812691455427477504_2.jpg)

FIG. 1. Scheme of the experimental setup for the x-ray magnetic dichroism measurements. The anatase film is covered with 2 nm Au.

emitting atom in a crystal field are calculated depending only on the charges and positions of its neighbors. Thus, one is not limited to certain crystal symmetries since the position of each individual atom is included. A multiplet Hamiltonian is used to calculate eigenvectors and eigenvalues of a ground state and a core-hole state while the XAS spectra are then determined by Fermi's golden rule. As a result, the spectra are obtained by sticks whose intensities arise out of the transition probabilities between ground and final states. Afterward, these sticks are broadened by Gaussian (experimental resolution) and Lorentzian functions (finite lifetime of a core-hole state) to obtain a spectrum comparable to the experimental ones [88].

The XAS and XMCD measurements were performed at beamline 6.3.1 at the Advanced Light Source at the Lawrence Berkeley National Laboratory. All experiments were done at room temperature, positive circular polarized x rays were used (with normal incidence), and the applied magnetic field was switched between $\mu_0 H = \pm 1$ T for the XMCD measurements. Total electron yield (TEY) as well as luminescence yield (LY) were used to measure the Ti $L_{2/3}$ and O $K$ edges. To measure TEY, the insulating films were covered with a 2-nm-thick Au film using magnetron sputtering; for a scheme, see Fig. 1. The preedge signal has been subtracted from the XAS data.

## III. RESULTS AND DISCUSSION

### A. X-ray diffraction

The sample was investigated with x-ray diffraction (XRD) measurements (Philips X-Pert Diffractometer with Bragg-Brentano goniometer). The results can be seen in Fig. 2.

The substrate is oriented in the (100) direction and the last $k_\beta$ Bragg peak corresponds to (400) $LaAlO_3$ (LAO). The as-prepared amorphous thin films show no $TiO_2$ peaks within the experimental resolution. After annealing at 1000 K for 1 h in an ambient atmosphere, the anatase (004) peak can be clearly recognized (see the inset in Fig. 2). No other peaks are present, confirming that the thin films are anatase in the (001) direction. From the (004) peak we find a lattice constant of $c = 9.49$ Å, which is slightly smaller compared to the literature value of 9.51 Å [89].

![](./images/812691455427477504_3.jpg)

FIG. 2. X-ray diffraction results of the amorphous and crystallized $TiO_2$ thin film. The inset is an enlargement around $2\Theta = 38^\circ$.

### B. Defect structure

The existence of di-Frenkel pairs (di-FPs) produced by low-energy ion irradiation, as found by Robinson *et al.* [90] by MD simulations using a Buckingham pair potential [91], was the starting point for a detailed investigation of different configurations of such defects on the DFT level. The theory in this work suggests that two neighboring Ti vacancy-interstitial defects (di-Frenkel pairs) are metastable in anatase and are likely to be produced using low-energy ion irradiation consistent with previous studies [71,90]. Anatase is a crystalline phase of $TiO_2$ and crystallizes in a tetragonal system, i.e., each Ti is surrounded by six O atoms. The unit cell of anatase can be seen in Fig. 3(a). By means of DFT calculations, as described in Sec. II C, Ti vacancies ($\text{Ti}_V$) and interstitials ($\text{Ti}_I$) were introduced into the material. After introducing the $\text{Ti}_V$-$\text{Ti}_I$ defects (Frenkel pair), the interstitials migrate back to the vacancy positions, recovering the pristine structure. However, when two Frenkel pairs exist as nearest neighbors, they can be metastable at room temperature [90]. Among the 108 different di-Frenkel pairs (di-FPs) configurations, only five of them relax to a spin-polarized ground state with a total magnetic moment of

![](./images/812691455427477504_4.jpg)

FIG. 3. In (a) the unit cell of anatase is shown, with Ti and O atoms in blue and red, respectively. In (b), two unit cells of anatase with di-FP1 are shown, where the Ti interstitials are black and the Ti vacancies are circles. The magnetic moment density is colored yellow (transparent). Image (c) is similar to (b) but for anatase with di-FP2.

$2\mu_{\rm B}$ per supercell. The total energies of these five magnetic structures are close to each other but almost 400 meV/f.u. higher in energy than the nonmagnetic TiO$_2$ pristine system, implying the metastability of these structures. In the following, we will solely discuss the two metastable configurations that give spin-polarized ground states and have the lowest energies among all studied structures. We mention here that the total energies of these two configurations differ only by 7 meV/f.u.

In the first configuration, di-FP1, there is a distance of 3.03 Å between vacancies ($d_{V1-V2}$) and a distance of 5.97 Å between each vacancy and its corresponding interstitial atom ($d_{V1-I1}$ and $d_{V2-I2}$); see Fig. 3(b). The distance between the two interstitials ($d_{I1-I2}$) is 6.52 Å. Each of them is fivefold coordinated [Fig. 3(b)] and has a magnetic moment of $0.7\mu_{\rm B}$. The transformation of the TiO$_6$ octahedra to TiO$_5$ caused by the di-FP was also predicted by Robinson *et al.* [90] by means of molecular-dynamics simulations. In Ref. [90], distances of 3 Å for $d_{V1-V2}$ and 2.9 Å for $d_{V1-I1}$ and $d_{V2-I2}$ are reported, indicating that they considered only the nearest interstitial coordinates (see Sec. II C).

On the other hand, di-FP2 is obtained with $d_{V1-V2}=4.96$ Å, $d_{V1-I1}=5.75$Å shorter than $d_{V2-I2}$, which is equal to 5.95 Å. However, $d_{I1-I2}$ is 3.81 Å, which is about half the distance in di-FP1 [see Fig. 3(c)]. Only interstitial $I1$ in di-FP2 is fivefold-coordinated; the second Ti forms again a TiO$_6$ octahedron.

## C. Electronic structure

The density of states (DOS) of defect-free anatase is shown in Fig. 4(a); no spin polarization is visible. The DOS of anatase with di-FP1 [Fig. 4(b)] shows a strong hybridization between Ti $d_{xz}$ orbitals and O $2p$ orbitals close to the (arbitrary) zero energy. The conduction-band minimum is mainly formed from the $d_{xz}$ orbital contribution. Each interstitial is fivefold-coordinated [see Fig. 3(b)] and has a magnetic moment of $0.7\mu_{\rm B}$. We have also calculated the magnetocrystalline anisotropy of di-FP1 and found that the easy axis is along the $z$-direction with an energy difference of 0.08 meV to the $x$-axis and 0.04 meV to the $y$-axis.

On the other hand, for di-FP2, the shrinking of the distance between the interstitials $d_{I1-I2}$ and the stretching of $d_{V1-V2}$ compared to di-FP1 induces a magnetic moment of $0.62\mu_{\rm B}$ on the O atom close to one Ti vacancy [see Fig. 3(c)]. Only one Ti interstitial ($I1$) is polarized ($0.7\mu_{\rm B}$) in di-FP2, and it is fivefold-coordinated as in di-FP1. However, the second Ti forms a TiO$_6$ octahedron. The density of states of di-FP2 [Fig. 4(c)] at the zero energy is formed by the Ti $d_{xz}$ hybridized with O $2p$ orbitals. A shallow peak from the O $2p$ orbitals develops in the conduction-band minimum, which is related to the polarization of an O atom in di-FP2.

![](./images/812691455427477504_5.jpg)

FIG. 4. The density of states (a) of TiO$_2$; (b) of TiO$_2$ with 5.5% di-FP1; and (c) of TiO$_2$ with 5.5% di-FP2. The total density of states is shaded in gray. The partial density of states (PDOS) of O $2p$ is shown by the filled orange areas. The decomposed PDOS of Ti $3d$ is presented by the colored solid lines, green for $d_{xy}$, red for $d_{xz}$, light blue for $d_{yz}$, dark blue for $d_{z^2}$, and brown for $d_{x^2}$. The black dashed lines indicate the zero energy levels of the considered systems. The spin-up and -down directions are indicated by arrows in (a).

## D. Magnetic moment measurements

In Fig. 5, the magnetic moment $m$ and magnetization $M$ versus applied field $B$ are shown. The open symbol curves show $m(B)$ of the nonirradiated anatase thin film. A small initial magnetic moment of $\approx1$ nA m$^2$ is present. This can be due to strain-induced magnetism at the substrate-film interface and/or due to impurities in the substrate or film. For example, interfacial magnetism at LAO and (TiO$_2$ terminated) SrTiO$_3$ interfaces was previously reported [92,93]. This initial moment of similar samples grown on SrTiO$_3$ was already discussed in Ref. [65].

The full symbols in Fig. 5 represent $m(B)$ data after irradiation with Ar$^+$ ions with the field applied parallel and perpendicular to the thin-film surface. Besides an increase of the saturation magnetic moment by a factor of $\approx20$, a PMA with the easy axis pointing out of the film is measured. To estimate the PMA constant $K$, the area difference of the two hysteresis curves in Fig. 5 is used and yields $K$$\approx$$0.26$ mJ/m$^2$. This result is similar to previously reported results for oxide thin films and multilayers [27,40,94] or for metallic multilayers [51]. The five $d$ orbitals (in-plane: $d_{xy}$, $d_{x^2-y^2}$; out-of-plane: $d_{xz}$, $d_{yz}$, $d_{3z^2}$) play a crucial role regarding the magnetic anisotropy. For thin films or surfaces, the structural anisotropy results in different contributions of the orbitals to the density of states. For example, when considering a monolayer, the in-plane orbitals have a larger overlap than the out-of-plane orbitals. This leads to narrower out-of-plane bands and decreased population in bands with lower

![](./images/812691455427477504_6.jpg)

FIG. 5. Magnetic moment $m$ (left axis) and magnetization $M$ (right axis) of the anatase film at $T=300$ K, before (open symbols) and after (full symbols) ${\rm Ar}^+$ irradiation. Results are shown for the two applied magnetic field directions-parallel and perpendicular to the film surface.

energy (spin down). Thus, the difference between spin-up and spin-down population is larger compared to the in-plane orbitals [95]. Such asymmetries resulting in out-of-plane magnetic anisotropies can also be induced through defects in TiO$_2$ [96].

The remanent magnetization is rather temperature-independent [65], which rules out superparamagnetism. There is small hysteresis with a coercive field of $B_c{\approx}10$ mT. The magnetization $M$ in Fig. 5 was calculated assuming a layer thickness of $\approx$10 nm (see also Sec. III G). Furthermore, the thermal stability factor $E/k_{\rm B}T$ has to be bigger than 40 [97] to ensure that the magnetic information is retained for at least 10 years. With $E=M_S{\mu_0}H_K A/2$ being the energy barrier that separates the two magnetization directions, and $K=m_s{\mu_0}H_K/2A$, one gets $E/k_{\rm B}T=KA/k_{\rm B}T$. With the PMA constant of $K=0.26$ mJ/m$^2$, we find that the thermal stability factor is large enough for an area $A\gtrsim(25$ nm$)^2$.

The temperature dependence of the magnetic moment can be seen in Fig. 6. The measurements were done in the following way: At zero field the temperature was swept from $T=300$ to 5 K, a magnetic field of ${\mu_0}H=0.05$ T was applied, and the heat-up [zero-field-cooled (ZFC)] and cool-down [field-cooled (FC)] curves were monitored. A clear irreversibility is visible, as expected for ferromagnetism. Furthermore, the field was turned off and the remanence was measured. The remanent magnetic moment $m(T)$ remains finite at $T\leqslant300$ K, and, in addition to the irreversibility in the ZFC-FC measurements, this implies a Curie temperature well above room temperature.

![](./images/812691455427477504_7.jpg)

FIG. 6. The zero-field-cooled (ZFC) and field-cooled (FC) curves together with the remanence of the irradiated anatase thin film. The magnetic field was applied perpendicular to the surface; the arrows indicate the temperature sweep direction.

## E. Magnetic force microscopy

The results of the magnetic force microscopy (MFM) measurements on a patterned anatase surface are shown in Fig. 7 for the sample magnetized either antiparallel (a) or

![](./images/812691455427477504_8.jpg)

FIG. 7. Magnetic force microscopy measurements with the sample $(M^S)$ and tip $(M^T)$ magnetization (a) antiparallel and (b) parallel to each other; (c) shows the corresponding line scans. In (d) a measurement is shown in three dimensions, where the magnetization direction of the sample was changed using a permanent magnet. The arrows indicate the $z$-component of $M^T$.

![](./images/812691455427477504_9.jpg)

FIG. 8. Magnetic force microscopy measurements at three different positions (a)–(c) of a fully irradiated thin film. In (a) and (b) the domains have been segmented with a barrier of 40% and a Gaussian smoothing of 8 px. The topography of region (c) is shown in (d); artifacts due to the negative lift height of $-10$ nm cannot be avoided completely, despite the reduced excitation voltage.

parallel (b) to the MFM tip magnetization direction. The film and the tip have been magnetized accordingly, prior to the MFM measurement, and no external field was applied during the measurement. The phase shift of the MFM signal clearly depends on the magnetization direction, as expected for a pinned ferromagnetic signal. Changing the relative magnetization direction, there is a sign change in the phase shift; see Fig. 7(c) for the line scans indicated in (a) and (b). In Fig. 7(d), the phase shift of the same magnetic pattern is shown in three dimensions. Using a permanent magnet, during the scan an external magnetic field was applied perpendicular to the thin film surface such that the magnetization direction of the sample was reversed, as can be seen in Fig. 7(d), where the phase shift changes its sign. This, along with the previous results, rules out electrostatic influences. There is no correlation between phase shift and topography. The surface roughness is unchanged by the irradiation and remains below 1 nm. The magnetic signal remains homogeneous over tens of micrometers, indicating a continuous and smooth distribution of magnetic defects (within a maximum scan size of $20\ \mu\text{m}$); this is a clear advantage for applications. Furthermore, the low ion-irradiation energy allows other masking techniques, e.g., with macromolecules [98], to prepare a magnetic pattern on the anatase surface.

The low remanence of the unpatterned and irradiated thin film (see Fig. 6) indicates the existence of randomly ordered domains on larger areas. Thus, MFM measurements were also conducted on the thin film; see Figs. 8(a)–8(d). Three different positions were measured and all show a magnetic domain structure. Figure 8(d) shows the topography of the MFM measurement shown in Fig. 8(c). Surface artifacts due to the extremely low lift height are obvious, yet the oppositely aligned domains as well as the domain boundaries are not related to topography effects. The magnetic domains explain the low remanence in the SQUID measurements and show that the magnetization of the film is directed out-of-plane. An in-plane domain structure would only be seen at the domain walls as the out-of-plane field vanishes within the domains. These results provide an explanation of the magnetic moment measurements and prove the existence of ferromagnetic domains at the surface. These results contradict the theory of paramagnetism due to vacuum fluctuations [99], at least in its current state [100], where a hysteresis/remanence and a magnetic domain structure cannot be explained.

![](./images/812691455427477504_10.jpg)

FIG. 9. Room-temperature x-ray absorption spectra (top) and magnetic circular dichroism around the Ti $L_{2,3}$ edges (blue line) for applied fields of $\pm1$ T of an irradiated TiO$_2$ sample, measured using total electron yield (TEY). Below, the results of the MultiX XMCD calculations are shown for the two di-Frenkel pairs and $d^0/d^1$ ground states.

### F. X-ray absorption spectra and x-ray magnetic circular dichroism

In Fig. 9, the XAS of the irradiated sample are shown for the Ti $L_{2,3}$ edges using TEY. The spectra consist of two edges: The $L_3$ edge originates from electron transitions from the inner $2p_{3/2}$ orbitals to empty $3d$ states, and the $L_2$ edge comes from $2p_{1/2}$ to $3d$ transitions. The two edges are split further, where the number of additional peaks depends on the valence state as well as the coordination and site symmetry [101–104]. The four standard peaks—$A$, $B$, $C$, and $D$—are common to all tetravalent Ti compounds with TiO$_6$ coordination [105] and

![](./images/812691455427477504_11.jpg)

FIG. 10. X-ray absorption spectra and magnetic circular dichro-
ism around the Ti $L_{2,3}$ edges for applied fields of $\pm 1$ T and at room
temperature of an untreated sample. The XAS spectra have been
recorded using total electron yield.

are a result of the spin-orbit splitting of $2p$ states $(L_{2,3})$ and
the $3d$ splitting to $t_{2g}$ and $e_{g}$ states. In the case of rutile and
anatase, there are additional peaks $a$ and $b$. The two prepeaks
$a$ can be understood using multiplet calculations [88,106];
a transition from $2p^{6}3d^{0}$ to $2p^{5}d^{1}$ yields a prepeak $a$,
which splits into two peaks within an octahedral crystal
field [88,105]. The origin of the $b$ peak remains an open ques-
tion. A possible explanation could be a noncubic ligand field
due to distortion of the $TiO_{6}$ octahedra [88], but this remains
doubtful [107]. Another explanation has been found taking
into account particle-hole coupling, which gives good results
for both anatase and rutile [105]. Regardless, the splitting into
the $B$-$b$ peaks is a fingerprint of anatase and rutile and does not
occur in other octahedra with similar Ti-O bond lengths, such
as $SrTiO_{3}$.

In Fig. 10, the room-temperature XAS of an untreated
anatase film are shown for the Ti $L_{2,3}$ edges measured using
TEY. The peak energies are shown in Table I, and agree well
with literature results [68,92,101-103,105,108-111]. The four
main peaks $(A-D)$ as well as the $b$-peak are visible, in
agreement with the anatase structure. The difference in the
$B/b$ intensity ratio confirms the anatase phase, where $I_{B/b}>1$
($I_{B/b}<1$) for anatase (rutile). In the XAS of the irradiated
sample (Fig. 9), the $b$ peak is present, yet the intensity is
reduced compared to the untreated anatase. The decrease in
intensity of the $b$ peak already shows that the crystal structure
has been modified during irradiation.

Further, a XMCD can be seen in the case of the irradiated
sample [blue line (i) in Fig. 9], which shows that the Ti atoms
have a magnetic moment after irradiation. There is no XMCD
signal for the untreated sample, confirming that there is no
magnetic contribution of Ti at the surface in the nonirradiated
anatase films.

<table>
<caption>TABLE I. XAS peak positions for anatase TiO₂.</caption>
<tbody>
<tr>
<th>
</th>
<td colspan="5">Peak position (eV)
</td>
</tr>
<tr>
<th>
</th>
<td>A
</td>
<td>B
</td>
<td>C
</td>
<td>D
</td>
<td>b
</td>
</tr>
<tr>
<th>TiO₂ TEY
</th>
<td>457.5
</td>
<td>459.2
</td>
<td>462.9
</td>
<td>464.7
</td>
<td>460
</td>
</tr>
<tr>
<th>TiO₂ LY
</th>
<td>457.6
</td>
<td>459.2
</td>
<td>462.9
</td>
<td>464.9
</td>
<td>460.2
</td>
</tr>
</tbody>
</table>

![](./images/812691455427477504_12.jpg)

FIG. 11. Room-temperature x-ray absorption spectra and mag-
netic circular dichroism around the Ti $L_{2,3}$ edges for applied fields
of $\pm 1$ T of an irradiated sample. The XAS spectra have been
recorded using luminescence yield. Below, the result of MultiX
XMCD calculation for TiO₂ anatase with $d^{1}$ ground state is shown.

The XAS measured with LY of the Ti $L_{2,3}$ edges are shown
in Fig. 11. The LY of the Ti $L_{2,3}$ edges also shows a small
XMCD feature that could explain the initial magnetic moment
measured in the SQUID. This signal might be due to charge-
transfer at the TiO₂/LAO interface, similar to what has been
observed for TiO₂/SrTiO₃ interfaces [92,112]. The bottom
line in Fig. 11 is the calculated XMCD signal for anatase
with $d^{1}$ ground state and agrees very well with the measured
signal. It must be kept mind that LY probes a larger part of
the sample and that the contribution of the anatase surface
is reduced (larger mean free path of photons compared to
electrons). Also, the presence of the $b$ peak in the XAS shows
a larger contribution of defect-free anatase compared to the
TEY spectra. This confirms that the structural changes, and
thus the increase of magnetism upon irradiation, are located
close to the surface of the thin film.

The O $K$ edge of an irradiated sample can be seen in
Fig. 12. The XAS show several peaks, which give information
about the environment of the O atoms. The sample was
measured using TEY to avoid the influence of the O in the
LAO substrate. There are two main peaks, $A$ and $B$, located at
530.1 and 532.6 eV. They are of $3d$ character, i.e., the O $2p$
orbital is hybridized with Ti $3d$ orbitals. The Ti $3d$ molecular
orbitals (MO) are $t_{2g}$-$e_{g}$ split, i.e., the $e_{g}$ orbitals ($d_{z^{2}}$ and
$d_{x^{2}-y^{2}}$) are directed at the Ti and the $t_{2g}$ orbitals ($d_{xy}$, $d_{yz}$, and
$d_{xz}$) are directed between O. The corresponding transitions
for the $A$ and $B$ peaks are $(\text{O}1s)\rightarrow[(\text{O}2p)-(\text{Ti}3d\{t_{2g}\})]$ ($\pi^{*}$
bond) and $(\text{O}1s)\rightarrow[(\text{O}2p)-(\text{Ti}3d\{e_{g}\})]$ ($\sigma^{*}$ bond), respec-
tively [101,108,113]. The second set of peaks—$C$, $D$, and
$E$—can be attributed to O $2p$ orbital hybridized with Ti $4s$
and $4p$ MOs [113,114]. This feature is related to the Ti-O
octahedra configuration and is absent in nonoctahedral struc-
tures [101,108,113]. An alternative explanation was found in
terms of resonance scattering within shells of neighboring

![](./images/812691455427477504_13.jpg)

FIG. 12. X-ray absorption spectra and magnetic circular dichro- ism around the O $K$ edge for applied fields of $\pm 1$ T and at room temperature of an irradiated sample. The XAS spectra have been recorded using total electron yield.

anionic backscatterers [115]. A small XMCD signal can be seen around 530 eV at the onset of the first O peak; see Fig. 12. This small signal is due to hybridized O $2p$ and Ti $3d$ orbitals [116]; see also Sec. III G.

### G. Origin of the magnetic moment

The computed structures were used to calculate the XAS and XMCD spectra of the Ti di-FPs in an anatase crystal; the results are shown in Fig. 9, curves (ii)-(v). The four possible combinations (di-FP1/2 and ground states $d^{0}$, $d^{1}$) have been shifted for clarity. The best agreement was found for di-FP2 with the $d^{1}$ ground state. $Ti^{3+}$ as the origin of the magnetic moment agrees also with the loss of the $TiO_{6}$ octahedra and the formation of $TiO_{5}$, where a Ti dangling bond acts as an O defect, thus explaining the $d^{1}$ magnetism. Note that none of the calculated XMCD curves agrees completely with the experimental data, which leads to the conclusion that also other structural changes might be involved in the formation of a magnetic moment within the $TiO_{2}$ samples. Assuming a defect concentration of one di-FP per two unit cells, and a magnetic moment of $2\mu_{B}$ per di-FP, one finds a defect depth of $\approx$10 nm and a magnetic defect concentration of $\approx$8 at. %.

There is a small XMCD signal at the onset of the O $K$ edge ($\approx$530 eV) (see Fig. 12) which is due to hybridized O $2p$ and Ti $3d_{xz}$ orbitals [116]. The origin of XMCD is different for the $L_{2,3}$ and $K$ edges. The spin-orbit interaction (SOI) connects the spin and angular momenta of the core electron and incident circularly polarized x rays. In the case of $L_{2,3}$ edges, the $2p$ states have orbital angular momenta and strong SOI due to their large binding energies, which yields the large $L_{2,3}$ XMCD and also the splitting into the $2p_{1/2}$ and $2p_{3/2}$ levels. The orbital magnetic moment, i.e., the SOI in the valence bands, is not essential to provide large XMCD. The core $s$ states, however, have no SOI due to the absence of orbital angular momentum. But, the SOI on unoccupied $p$ states at the absorbing atom is essential to yield the $K$-edge. In general, the SOI at light elements is weak compared with that of heavier elements, due to weaker gradients of Coulomb potentials. Thus, the SOI at light elements is weak compared with that of heavier elements, due to weaker gradients of Coulomb potentials. Thus, the SOI is important at the core $2p$ states in the absorbing atom, and the XMCD is a projection from the Ti $3d$ orbitals hybridized with the O $2p$ level [92,117]. Therefore, we can conclude that the main contribution to the magnetic moment is located at the $Ti^{3+}$ in di-FP defects.

### IV. CONCLUSION

In conclusion, ferromagnetism at room temperature with perpendicular magnetic anisotropy has been induced in (001) anatase after irradiating the sample with low-energy $Ar^{+}$ ions. XAS and XMCD experiments of the O $K$ and Ti $L_{3,2}$ absorption edges have shown that the magnetic moment arises at the Ti $3d$ shell. XAS and XMCD calculations of Ti di-FPs are in agreement with the results and the assumption that di-Frenkel pairs are responsible for the observed magnetism and anisotropy. SQUID measurements were used to estimate the magnetic anisotropy. Magnetic force microscopy proves the existence of oppositely aligned magnetic domains with out-of-plane magnetization directions, thus explaining the low remanence of the samples. The efficiency of the production method can be easily combined with other techniques allowing the production of arbitrary magnetic patterns with perpendicular magnetic anisotropy at the, in other respects unaltered, anatase surface.

### ACKNOWLEDGMENTS

This work was funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation)-Projektnummer 31047526-SFB 762, projects B1 and B5 and the German Academic Research Council (Project No. 57348127). Synchrotron studies were carried out at the Advanced Light Source at the Lawrence Berkeley National Laboratory. The computer resources of the Finnish IT Centre for Science (CSC), Project No. 2000643, are acknowledged.

[1] T. Dietl, H. Ohno, F. Matsukura, J. Cibert, and D. Ferrand, Science 287, 1019 (2000).
[2] W. Hu, Y. Liu, R. L. Withers, T. J. Frankcombe, L. Norén, A. Snashall, M. Kitchin, P. Smith, B. Gong, H. Chen, J. Schiemer, F. Brink, and J. Wong-Leung, Nat. Mater. 12, 821 (2013).
[3] A. Berlie, I. Terry, S. P. Cottrell, W. Hu, and Y. Liu, Mater. Horiz. 7, 188 (2020).
[4] M. Venkatesan, C. Fitzgerald, and J. Coey, Nature (London) 430, 630 (2004).
[5] J. Coey, J. Appl. Phys. 97, 10D313 (2005).
[6] J. M. D. Coey, M. Venkatesan, P. Stamenov, C. B. Fitzgerald, and L. S. Dorneles, Phys. Rev. B 72, 024450 (2005).
[7] N. H. Hong, J. Sakai, N. Poirot, and V. Brizé, Phys. Rev. B 73, 132404 (2006).
[8] A. Sundaresan, R. Bhargavi, N. Rangarajan, U. Siddesh, and C. N. R. Rao, Phys. Rev. B 74, 161306(R) (2006).
[9] N. Hoa Hong, J. Sakai, W. Prellier, A. Hassini, A. Ruyter, and F. Gervais, Phys. Rev. B 70, 195204 (2004).

014412-8

[10] S. D. Yoon, Y. Chen, A. Yang, T. L. Goodrich, X. Zuo, D. A. Arena, K. Ziemer, C. Vittoria, and V. G. Harris, J. Phys.: Condens. Matter 18, L355 (2006).

[11] M. Venkatesan, C. B. Fitzgerald, J. G. Lunney, and J. M. D. Coey, Phys. Rev. Lett. 93, 177206 (2004).

[12] M. Khalid, M. Ziese, A. Setzer, P. Esquinazi, M. Lorenz, H. Hochmuth, M. Grundmann, D. Spemann, T. Butz, G. Brauer, W. Anwand, G. Fischer, W. A. Adeagbo, W. Hergert, and A. Ernst, Phys. Rev. B 80, 035331 (2009).

[13] N. H. Hong, J. Sakai, and V. Brizé, J. Phys.: Condens. Matter 19, 036219 (2007).

[14] N. H. Hong, N. Poirot, and J. Sakai, Phys. Rev. B 77, 033205 (2008).

[15] C. Chappert, A. Fert, and F. N. V. Dau, Nat. Mater. 6, 813 (2007).

[16] T. Kawahara, IEEE Design Test Comput. 28, 52 (2011).

[17] B. Dieny, R. Sousa, J. Herault, C. Papusoi, G. Prenat, U. Ebels, D. Houssameddine, B. Rodmacq, S. Auffret, L. B. Prejbeanu, M. Cyrille, B. Delaet, O. Redon, C. Ducruet, J. P. Nozieres, and I. Prejbeanu, Int. J. Nanotechnol. 7, 591 (2010).

[18] W. H. Rippard, M. R. Pufall, S. Kaka, T. J. Silva, S. E. Russek, and J. A. Katine, Phys. Rev. Lett. 95, 067203 (2005).

[19] H. S. Choi, S. Y. Yang, S. J. Cho, I.-Y. Oh, M. Shin, H. Park, C. Jang, B.-C. Min, S.-I. Kim, S.-Y. Park, and C. S. Park, Sci. Rep. 4, 5486 (2014).

[20] S. Miwa, S. Ishibashi, H. Tomita, T. Nozaki, E. Tamura, K. Ando, N. Mizuochi, T. Saruya, H. Kubota, K. Yakushiji, T. Taniguchi, H. Imamura, A. Fukushima, S. Yuasa, and Y. Suzuki, Nat. Mater. 13, 50 (2014).

[21] A. Dussaux, B. Georges, J. Grollier, V. Cros, A. V. Khvalkovskiy, A. Fukushima, M. Konoto, H. Kubota, K. Yakushiji, S. Yuasa, K. A. Zvezdin, K. Ando, and A. Fert, Nat. Commun. 1, 8 (2010).

[22] C. Reig, S. Cardoso, and S. C. Mukhopadhyay, Giant Mag- netoresistance (GMR) Sensors: From Basis to State-of-the-Art Applications (Springer, New York, 2014).

[23] P. Tartaj, M. P. Morales, T. González-Carreño, S. Veintemillas- Verdaguer, and C. J. Serna, J. Magn. Magn. Mater. 290-291, 28 (2005).

[24] G. Binasch, P. Grünberg, F. Saurenbach, and W. Zinn, Phys. Rev. B 39, 4828 (1989).

[25] M. N. Baibich, J. M. Broto, A. Fert, F. Nguyen Van Dau, F. Petroff, P. Etienne, G. Creuzet, A. Friederich, and J. Chazelas, Phys. Rev. Lett. 61, 2472 (1988).

[26] S. Mangin, D. Ravelosona, J. A. Katine, M. J. Carey, B. D. Terris, and E. E. Fullerton, Nat. Mater. 5, 210 (2006).

[27] S. Ikeda, K. Miura, H. Yamamoto, K. Mizunuma, H. D. Gan, M. Endo, S. Kanai, J. Hayakawa, F. Matsukura, and H. Ohno, Nat. Mater. 9, 721 (2010).

[28] D. Yi, C. L. Flint, P. P. Balakrishnan, K. Mahalingam, B. Urwin, A. Vailionis, A. T. N'Diaye, P. Shafer, E. Arenholz, Y. Choi, K. H. Stone, J.-H. Chu, B. M. Howe, J. Liu, I. R. Fisher, and Y. Suzuki, Phys. Rev. Lett. 119, 077201 (2017).

[29] L. Liu, C.-F. Pai, Y. Li, H. W. Tseng, D. C. Ralph, and R. A. Buhrman, Science 336, 555 (2012).

[30] S. Emori, U. Bauer, S.-M. Ahn, E. Martinez, and G. S. D. Beach, Nat. Mater. 12, 611 (2013).

[31] L. Yin, X. Wang, and W. Mi, J. Appl. Phys. 123, 033905 (2018).

[32] S. Yuasa, A. Fukushima, K. Yakushiji, T. Nozaki, M. Konoto, H. Maehara, H. Kubota, T. Taniguchi, H. Arai, H. Imamura, K. Ando, Y. Shiota, F. Bonell, Y. Suzuki, N. Shimomura, E. Kitagawa, J. Ito, S. Fujita, K. Abe, K. Nomura, H. Noguchi, and H. Yoda, in 2013 IEEE International Electron Devices Meeting (IEEE, Piscataway, NJ, 2013), pp. 3.1.1-3.1.4.

[33] F. J. A. den Broeder, W. Hoving, and P. J. H. Bloemen, J. Magn. Magn. Mater. 93, 562 (1991).

[34] F. J. A. den Broeder, H. C. Donkersloot, H. J. G. Draaisma, and W. J. M. de Jonge, J. Appl. Phys. 61, 4317 (1987).

[35] P. F. Carcia, A. D. Meinhaldt, and A. Suna, Appl. Phys. Lett. 47, 178 (1985).

[36] L. Berger, Phys. Rev. B 54, 9353 (1996).

[37] J. C. Slonczewski, J. Magn. Magn. Mater. 159, L1 (1996).

[38] A. Manchon and S. Zhang, Phys. Rev. B 79, 094422 (2009).

[39] C. T. Rettner, S. Anders, J. E. E. Baglin, T. Thomson, and B. D. Terris, Appl. Phys. Lett. 80, 279 (2002).

[40] B. Dieny and M. Chshiev, Rev. Mod. Phys. 89, 025008 (2017).

[41] P. Bruno, Phys. Rev. B 39, 865 (1989).

[42] L. F. Mattheiss, Phys. Rev. B 6, 4718 (1972).

[43] F. Bloch and G. Gentile, Z. Phys. 70, 395 (1931).

[44] H. Bethe, Ann. Phys. 395, 133 (1929).

[45] L. Néel, J. Phys. Radium 15, 225 (1954).

[46] J. Zhang, Z. Zhong, X. Guan, X. Shen, J. Zhang, F. Han, H. Zhang, H. Zhang, X. Yan, Q. Zhang, L. Gu, F. Hu, R. Yu, B. Shen, and J. Sun, Nat. Commun. 9, 1923 (2018).

[47] M. T. Johnson, R. Jungblut, P. J. Kelly, and F. J. A. den Broeder, J. Magn. Magn. Mater. 148, 118 (1995).

[48] G. H. O. Daalderop, P. J. Kelly, and M. F. H. Schuurmans, Phys. Rev. B 50, 9989 (1994).

[49] H. X. Yang, M. Chshiev, B. Dieny, J. H. Lee, A. Manchon, and K. H. Shin, Phys. Rev. B 84, 054401 (2011).

[50] B. Rodmacq, S. Auffret, B. Dieny, S. Monso, and P. Boyer, J. Appl. Phys. 93, 7513 (2003).

[51] M. T. Johnson, P. J. H. Bloemen, F. J. A. d. Broeder, and J. J. d. Vries, Rep. Prog. Phys. 59, 1409 (1996).

[52] T. Liu, J. W. Cai, and L. Sun, AIP Adv. 2, 032151 (2012).

[53] B. F. Vermeulen, J. Wu, J. Swerts, S. Couet, I. P. Radu, G. Groeseneken, C. Detavernier, J. K. Jochum, M. Van Bael, K. Temst, A. Shukla, S. Miwa, Y. Suzuki, and K. Martens, AIP Adv. 7, 055933 (2017).

[54] H. K. Gweon, S. J. Yun, and S. H. Lim, Sci. Rep. 8, 1266 (2018).

[55] B. Rodmacq, A. Manchon, C. Ducruet, S. Auffret, and B. Dieny, Phys. Rev. B 79, 024423 (2009).

[56] A. Manchon, S. Pizzini, J. Vogel, V. Uhlíř, L. Lombard, C. Ducruet, S. Auffret, B. Rodmacq, B. Dieny, M. Hochstrasser, and G. Panaccione, J. Magn. Magn. Mater. 320, 1889 (2008).

[57] A. Manchon, C. Ducruet, L. Lombard, S. Auffret, B. Rodmacq, B. Dieny, S. Pizzini, J. Vogel, V. Uhlíř, M. Hochstrasser, and G. Panaccione, J. Appl. Phys. 104, 043914 (2008).

[58] A. Manchon, S. Pizzini, J. Vogel, V. Uhlíř, L. Lombard, C. Ducruet, S. Auffret, B. Rodmacq, B. Dieny, M. Hochstrasser, and G. Panaccione, J. Appl. Phys. 103, 07A912 (2008).

[59] A. J. Schellekens, A. van den Brink, J. H. Franken, H. J. M. Swagten, and B. Koopmans, Nat. Commun. 3, 847 (2012)

[60] I. M. Miron, T. Moore, H. Szambolics, L. D. Buda-Prejbeanu, S. Auffret, B. Rodmacq, S. Pizzini, J. Vogel, M. Bonfim, A. Schuhl, and G. Gaudin, *Nat. Mater.* **10**, 419 (2011).

[61] S. S. P. Parkin, M. Hayashi, and L. Thomas, *Science* **320**, 190 (2008).

[62] Y. Shiota, T. Maruyama, T. Nozaki, T. Shinjo, M. Shiraishi, and Y. Suzuki, *Phys. Express* **2**, 063001 (2009).

[63] Y. Shiota, T. Nozaki, F. Bonell, S. Murakami, T. Shinjo, and Y. Suzuki, *Nat. Mater.* **11**, 39 (2012).

[64] M. Weisheit, S. Fähler, A. Marty, Y. Souche, C. Poinsignon, and D. Givord, *Science* **315**, 349 (2007).

[65] M. Stiller, J. Barzola-Quiquia, P. Esquinazi, D. Spemann, J. Meijer, M. Lorenz, and M. Grundmann, *AIP Adv.* **6**, 125009 (2016).

[66] S. Zhou, E. Čižmár, K. Potzger, M. Krause, G. Talut, M. Helm, J. Fassbender, S. A. Zvyagin, J. Wosnitza, and H. Schmidt, *Phys. Rev. B* **79**, 113201 (2009).

[67] M. M. Cruz, R. C. d. Silva, N. Franco, and M. Godinho, *J. Phys.: Condens. Matter* **21**, 206002 (2009).

[68] H. Thakur, P. Thakur, R. Kumar, N. B. Brookes, K. K. Sharma, A. P. Singh, Y. Kumar, S. Gautam, and K. H. Chae, *Appl. Phys. Lett.* **98**, 192512 (2011).

[69] S. D. Yoon, Y. Chen, A. Yang, T. L. Goodrich, X. Zuo, K. Ziemer, C. Vittoria, and V. G. Harris, *J. Magn. Magn. Mater.* **309**, 171 (2007).

[70] D.-X. Li, X.-B. Qin, L.-R. Zheng, Y.-X. Li, X.-Z. Cao, Z.-X. Li, J. Yang, and B.-Y. Wang, *Chin. Phys. B* **22**, 037504 (2013).

[71] H. Peng, J. Li, S.-S. Li, and J.-B. Xia, *Phys. Rev. B* **79**, 092411 (2009).

[72] D. Sanyal, M. Chakrabarti, P. Nath, A. Sarkar, D. Bhowmick, and A. Chakrabarti, *J. Phys. D* **47**, 025001 (2013).

[73] S. Wang, L. Pan, J.-J. Song, W. Mi, J.-J. Zou, L. Wang, and X. Zhang, *J. Am. Chem. Soc.* **137**, 2975 (2015).

[74] Q. Zhao, P. Wu, B. L. Li, Z. M. Lu, and E. Y. Jiang, *J. Appl. Phys.* **104**, 073911 (2008).

[75] A. K. Rumaiz, B. Ali, A. Ceylan, M. Boggs, T. Beebe, and S. Ismat Shah, *Solid State Commun.* **144**, 334 (2007).

[76] C. Bundesmann and H. Neumann, *J. Appl. Phys.* **124**, 231102 (2018).

[77] C. Bundesmann, T. Lautenschläger, D. Spemann, A. Finzel, E. Thelander, M. Mensing, and F. Frost, *Appl. Surf. Sci.* **421**, 331 (2017).

[78] P. E. Blöchl, *Phys. Rev. B* **50**, 17953 (1994).

[79] G. Kresse and D. Joubert, *Phys. Rev. B* **59**, 1758 (1999).

[80] G. Kresse and J. Furthmüller, *Comput. Mater. Sci.* **6**, 15 (1996).

[81] G. Kresse and J. Furthmüller, *Phys. Rev. B* **54**, 11169 (1996).

[82] J. P. Perdew, K. Burke, and M. Ernzerhof, *Phys. Rev. Lett.* **77**, 3865 (1996).

[83] S. L. Dudarev, G. A. Botton, S. Y. Savrasov, C. J. Humphreys, and A. P. Sutton, *Phys. Rev. B* **57**, 1505 (1998).

[84] Z. Hu and H. Metiu, *J. Phys. Chem. C* **115**, 5841 (2011).

[85] C. J. Howard, T. M. Sabine, and F. Dickson, *Acta Crystallogr., Sect. B* **47**, 462 (1991).

[86] R. Tank, O. Jepsen, A. Burkhardt, and O. Andersen, *Max- Planck-Institut für Festkörperforschung*, Stuttgart, Germany (1994).

[87] A. Uldry, F. Vernay, and B. Delley, *Phys. Rev. B* **85**, 125133 (2012).

[88] F. M. F. de Groot, J. C. Fuggle, B. T. Thole, and G. A. Sawatzky, *Phys. Rev. B* **41**, 928 (1990).

[89] Rruff anatase mineral data (unpublished).

[90] M. Robinson, N. A. Marks, and G. R. Lumpkin, *Mater. Chem. Phys.* **147**, 311 (2014).

[91] M. Matsui and M. Akaogi, *Mol. Simul.* **6**, 239 (1991).

[92] J.-S. Lee, Y. W. Xie, H. K. Sato, C. Bell, Y. Hikita, H. Y. Hwang, and C.-C. Kao, *Nat. Mater.* **12**, 703 (2013).

[93] H. Y. Hwang, Y. Iwasa, M. Kawasaki, B. Keimer, N. Nagaosa, and Y. Tokura, *Nat. Mater.* **11**, 103 (2012).

[94] L. E. Nistor, B. Rodmacq, S. Auffret, and B. Dieny, *Appl. Phys. Lett.* **94**, 012512 (2009).

[95] J. Stöhr, *J. Electron Spectrosc. Relat. Phenom.* **75**, 253 (1995).

[96] B. Shao, Y. fang He, M. Feng, Y. Lu, and X. Zuo, *J. Appl. Phys.* **115**, 17A915 (2014).

[97] S. Ikeda, J. Hayakawa, Y. M. Lee, F. Matsukura, Y. Ohno, T. Hanyu, and H. Ohno, *IEEE Trans. Electron Dev.* **54**, 991 (2007).

[98] P. Murugan, M. Krishnamurthy, S. N. Jaisankar, D. Samanta, and A. B. Mandal, *Chem. Soc. Rev.* **44**, 3212 (2015).

[99] S. Sen, K. S. Gupta, and J. M. D. Coey, *Phys. Rev. B* **92**, 155115 (2015).

[100] J. M. D. Coey, *Nat. Mater.* **18** 652 (2019).

[101] E. Stoyanov, F. Langenhorst, and G. Steinle-Neumann, *Am. Mineral.* **92**, 577 (2007).

[102] R. D. Leapman, L. A. Grunes, and P. L. Fejes, *Phys. Rev. B* **26**, 614 (1982).

[103] R. Brydson, H. Sauer, W. Engel, J. M. Thomass, E. Zeitler, N. Kosugi, and H. Kuroda, *J. Phys.: Condens. Matter* **1**, 797 (1989).

[104] L. Garvie, A. J. Craven, and R. Brydson, *Am. Mineral.* **79**, 411 (1994).

[105] P. Krüger, *Phys. Rev. B* **81**, 125121 (2010).

[106] J. Zaanen, G. A. Sawatzky, J. Fink, W. Speier, and J. C. Fuggle, *Phys. Rev. B* **32**, 4905 (1985).

[107] J. P. Crocombette and F. Jollet, *J. Phys.: Condens. Matter* **6**, 10811 (1994).

[108] R. Brydson, H. Sauer, W. Engel, and F. Hofer, *J. Phys.: Condens. Matter* **4**, 3429 (1992).

[109] R. Brydson, B. G. Williams, W. Engel, H. Sauer, E. Zeitler, and J. M. Thomas, *Solid State Commun.* **64**, 609 (1987).

[110] D. W. Fischer and W. L. Baun, *J. Appl. Phys.* **39**, 4757 (1968).

[111] D. W. Fischer, *J. Appl. Phys.* **41**, 3561 (1970).

[112] L. Yu and A. Zunger, *Nat. Commun.* **5**, 5118 (2014).

[113] F. M. F. de Groot, M. Grioni, J. C. Fuggle, J. Ghijsen, G. A. Sawatzky, and H. Petersen, *Phys. Rev. B* **40**, 5715 (1989).

[114] M. Yoshiya, I. Tanaka, K. Kaneko, and H. Adachi, *J. Phys.: Condens. Matter* **11**, 3217 (1999).

[115] H. Kurata, E. Lefèvre, C. Colliex, and R. Brydson, *Phys. Rev. B* **47**, 13763 (1993).

[116] W. Siemons, G. Koster, H. Yamamoto, W. A. Harrison, G. Lucovsky, T. H. Geballe, D. H. A. Blank, and M. R. Beasley, *Phys. Rev. Lett.* **98**, 196802 (2007).

[117] A. Koide and T. Yokoyama, *Phys. Rev. B* **96**, 144419 (2017).

014412-10