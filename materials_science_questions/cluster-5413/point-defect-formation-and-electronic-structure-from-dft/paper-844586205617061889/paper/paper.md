PHYSICAL REVIEW MATERIALS 7, 033603 (2023)

# Cd implantation in $\alpha$-MoO$_3$: An atomic scale study

Adeleh Mokhles Gerami $\odot,^{1,2, *}$ Juliana Heiniger-Schell $\odot,^{2,3}$ E. Lora da Silva $\odot,^{4}$ Messias S. Costa $\odot,^{5}$ Cleidilane S. Costa $\odot,^{5}$ João G. Monteiro $\odot,^{6}$ José J. Pires, $^{7}$ Daniela R. Pereira, $^{8}$ Carlos Díaz-Guerra $\odot,^{9}$ Artur W. Carbonari $\odot,^{10}$ Katharina Lorenz $\odot,^{8,11}$ and João G. Correia $\odot^{6,2}$

$^{1}$School of Particles and Accelerators, Institute for Research in Fundamental Sciences (IPM), Tehran P.O. Box 19395-5531, Iran
$^{2}$European Organization for Nuclear Research (CERN), CH-1211 Geneva, Switzerland
$^{3}$Institute for Materials Science and Center for Nanointegration Duisburg-Essen (CENIDE), University of Duisburg-Essen, 45141 Essen, Germany
$^{4}$IFIMUP, Institute of Physics for Advanced Materials, Nanotechnology and Photonics, Department of Physics and Astronomy, Faculty of Sciences, University of Porto, 687, 4169-007 Porto, Portugal
$^{5}$Universidade Federal do Pará, UFPA/Abaetetuba, 68440000 Abaetetuba, PA Brazil
$^{6}$Centro de Ciências e Tecnologias Nucleares, Departamento de Engenharia e Ciências Nucleares, Instituto Superior Técnico (IST), Universidade de Lisboa, 2695-066 Bobadela, Portugal
$^{7}$Departamento de Materiais, Instituto Superior Técnico, Universidade de Lisboa, 1049-001 Lisboa, Portugal
$^{8}$Instituto de Engenharia de Sistemas e Computadores-Microsistemas e Nanotecnologias (INESC MN), Lisbon, 1000-029 Lisboa, Portugal
$^{9}$Departamento de Física de Materiales, Facultad de Ciencias Físicas, Universidad Complutense de Madrid, E-28040 Madrid, Spain
$^{10}$Instituto de Pesquisas Energéticas e Nucleares, IPEN, São Paulo, SP, CEP 05508-000, Brazil
$^{11}$IPFN, Instituto Superior Técnico, Universidade de Lisboa, 1049-001 Lisboa, Portugal

![](./images/844586205617061889_1.jpg)
(Received 16 August 2022; accepted 25 January 2023; published 16 March 2023)

Lamellar $\alpha$-MoO$_3$ crystals were implanted with low fluence of radioactive $^{111\text{m}}$Cd ions at ISOLDE-CERN. Subsequently, we have probed the interaction of the Cd impurity in the lattice with native point defects, such as oxygen vacancies, as a function of annealing temperature using the time differential perturbed angular correlations nanoscopic technique. The experimental data were complemented and interpreted by modeling different Cd-defect configurations in $\alpha$-MoO$_3$ with first-principles density functional theory (DFT). The agreement between experiments and DFT simulations shows that only the interstitial Cd (Cd$_I$) prevails in the van der Waals gap, by inducing a polaron effect. Upon raising the annealing temperature, Cd$_I$ is able to trap hole charge carriers resultant from the oxygen vacancies $V_O$. Oxygen vacancies were found to form most commonly at two-fold coordinated (O2) atoms. According to comparison DFT results with the experimental electric field gradient values ($V_{zz}$ and $\eta$) and the calculated formation energies for different defect complexes, the configuration of Cd$_I$ with two (O2) vacancies ($V_{O2}$), located at different planes, is found to be more favorable and stable than the other defect configurations. The electron-polaron formation around the Cd impurity at an interstitial site is enhanced by inducing (O2) vacancies with the creation of hole polaron states.

DOI: 10.1103/PhysRevMaterials.7.033603

## I. INTRODUCTION

MoO$_3$ belongs to the family of two-dimensional (2D) inorganic materials with increasing attention due to the wide range of distinct properties leading to several applications, particularly in electronics, catalysis, and sensors [1,2]. The MoO$_3$ system has been found to crystallize in different structural phases including the orthorhombic phase $\alpha$-MoO$_3$; the monoclinic phase $\beta$-MoO$_3$; the high-pressure metastable phase $\beta'$-MoO$_3$; and the hexagonal phase $h$-MoO$_3$ [3]. Among these polymorphs, the $\alpha$-MoO$_3$ is the most stable crystal phase at room temperature (RT) [3,4]. This system exhibits a layered structure consisting of van der Waals (vdW) interacting sheets of distorted, edgelike Mo-O$_6$ octahedra in which Mo atoms are bonded to three different types of oxygen atoms at various distances from 1.67 to $2.33$ Å [5,6].

Figure 1 shows an artistic representation of the $\alpha$-MoO$_3$ lattice structure, from which evidence the distorted octahedra. There are three nonequivalent oxygen sites associated with the coordination to the Mo atom: single-coordinated O1, double-coordinated O2, and triple-coordinated O3. The anisotropy of the lattice is emphasized by the different types of bonds, i.e., along the [010] axis the interactions are of vdW type, while the bonds along the [100] and [001] axes are of the covalent type [6]. The vdW gap is the most important feature of this structure since it allows easy intercalation of atoms or accommodation of defects, which play an essential role, for example, in tuning the wide optical band gap of the semiconductor (2.8–3.2 eV) [5].

*adeleh.mokhles.gerami@cern.ch

Published by the American Physical Society under the terms of the Creative Commons Attribution 4.0 International license. Further distribution of this work must maintain attribution to the author(s) and the published article's title, journal citation, and DOI.

2475-9953/2023/7(3)/033603(15) 033603-1 Published by the American Physical Society

![](./images/844586205617061889_2.jpg)

FIG. 1. Artistic plot of the $\alpha$-MoO$_3$ structure identifying the relevant planes, the nonequivalent oxygen atomic sites, and the interstitial positions of interest. The green, yellow, and red spheres represent the O3, O2, and O1, respectively.

Due to the specific structural and optical properties of $\alpha$-MoO$_3$, the system performs well in a variety of electrical applications such as solar cells [7], catalysis [8], gas sensing [9,10], field emission [11], lithium-ion batteries [12], photochromic and electrochromic devices [13], and ultraviolet photodetectors [14]. So far, the literature has pointed out [15–17] that some intrinsic point defects, such as oxygen vacancies, can be form in the MoO$_3$ lattice simply by varying the synthesis conditions; these include annealing, controlling the oxygen partial pressure, etc.

Previously, it was reported that the reduction of the optical band gap is due to the incorporation of metal ions or oxygen vacancies into $\alpha$-MoO$_3$ lattice [18]. In the case of oxygen vacancies, free electrons are released from the vacancies [19]. The excess electrons may either be located as electron pairs at the anion sites or, if separated, may be located at the surrounding cations, resulting in the formation of two Mo$^{5+}$. In the other cases, these excess electrons can form delocalized states around a group of cations. It has been observed that the Mo$^{5+}$ charge state appears in the photoemission spectra at low concentrations of oxygen vacancies, and the Mo$^{4+}$ charge state appears at higher concentrations of oxygen vacancies [20,21]. On the other hand, oxygen vacancies can act as shallow donors, thereby increasing the carrier concentration that causes intervalence charge transfer between localized neighboring sites acting as self-trapping sites, similar to what is expected from polaron behavior. These charge transfers can occur either along Mo$^{5+}$-Mo$^{6+}$, or Mo$^{5+}$-O-Mo$^{6+}$, or O$^{2-}$-Mo$^{6+}$ [17]. In addition, the formation of oxygen vacancies can increase the interlayer spacing, which can potentially lead to improved electrochemical performance [16].

So far, several methods have been applied to tune the conductivity of MoO$_3$. These methods include mechanical strain, UV irradiation, or thermal treatments under low oxygen partial pressures, which influence the crystal morphology of MoO$_3$, inducing oxygen deficiency and thus leading to stoichiometry changes of MoO$_{3-x}$ [22]. Although the resistivity of intrinsic $\alpha$-MoO$_3$ is generally very high, it has been reported [23] that the hole mobility of intrinsic bulk $\alpha$-MoO$_3$ is predicted to be relatively high with the range of $2000\ \mathrm{cm^2/(V\ s)}$ for the case of nonstrain condition. This result was obtained by employing deformation potential theory based on DFT calculations. This feature is because the transition metal Mo atoms in $\alpha$-MoO$_3$ have multiple valence states, enabling these to act as a hole transport layer in polymer solar cells (PSCs) and an organic light-emitting diode (OLED) [24,25]. To overcome the high resistivity of intrinsic $\alpha$-MoO$_3$, doping with different cations, such as In ions, has been proposed to improve hole concentration and conductivity [26]. In another application, sensors based on Cd-doped $\alpha$-MoO$_3$ nanobelts have revealed a high response to H$_2$S and low cross sensitivity to other reducing gases, with the improvement in sensor properties attributed to the modification of intrinsic defects, as demonstrated by photoluminescence (PL) spectroscopy, Raman and x-ray photoelectron spectroscopy (XPS) measurements [10]. Yet, from other studies [27] it was shown that the use of Fe ions as dopants in $\alpha$-MoO$_3$ nanoribbons can create a potential for use in gas sensors with excellent hydrogen gas sensing properties at room temperature (RT). Moreover, in the literature source of Ref. [27], the presence of Fe$^{3+}$ in the sample was observed from the XPS spectra, indicating the formation of oxygen vacancies. The presence of Fe$^{3+}$ was also observed by emission Mössbauer experiments performed on the same batch of samples using $^{57}$Mn/$^{57}$Fe as probe nuclei [28]. Finally, $\alpha$-MoO$_3$ samples normally show low luminescence emission efficiency [29]; however, stable room-temperature PL has been achieved in $\alpha$-MoO$_3$ crystals by ion implantation doping with Er and Eu [30]. It has been reported that doping $\alpha$-MoO$_3$ with rare-earth ions is particularly advantageous for applications of this oxide in organic solar cells [31].

To study the nanoscopic phenomena in $\alpha$-MoO$_3$ lamellar crystals, with oxygen vacancies, and their interaction with metal impurities, we applied the time differential perturbed angular correlation (TD-PAC), nuclear hyperfine radioactive technique using the $^{111\mathrm{m}}$Cd/$^{111}$Cd probe isotope. TD-PAC allows one to measure the hyperfine interaction at probes, which are radioactive ions implanted in the structures to be analyzed. We can therefore obtain local information on an atomic scale regarding the electronic charge density [electric field gradient (EFG)] or polarization (hyperfine magnetic field $B$). The experimental data are complemented by employing density functional theory (DFT) simulations, to support the interpretation of the experimental data.

## II. METHODS

### A. TD-PAC method

The time differential PAC technique is widely used in materials science to study the local nanoscopic electronic environment of a probe element since it accurately measures the EFGs and/or magnetic fields interacting with the quadrupole and/or magnetic moments of the nuclei of the probe. TD-PAC measures nuclear hyperfine interactions as the nuclear magnetic resonance (NMR) or the emission Mössbauer spectroscopy (eMs) techniques, but the quality of the observation is temperature independent and a larger number of (radioactive) probe elements are available [32–34]. Online production

![](./images/844586205617061889_3.jpg)

FIG. 2. Artistic representation of the TD-PAC experimental con- cept (left) and of the TD-PAC data observable (right).

of radioactive isotopes at ISOLDE-CERN [35] allows to find probe element/isotopes with suitable decay cascades, nuclear moments, lifetimes $>2$ ns and spin $>\frac{1}{2}$ , which can be applied with the TD-PAC technique. Differently from NMR, the alignment of the nuclear probing state occurs via a decay cascade where the detection of the first gamma selects a set of aligned spins which is redistributed as a function of time in a characteristic way, by the nuclei external charge field distribution [36]. Thus, the generation of a set of aligned nuclei spins is an essential part of the measurement process, and differently from NMR and Mössbauer spectroscopy, this technique works over a wide temperature range from 1 to2000 K.

In this work, the $^{111 ~m} Cd /^{111} Cd(T_{1 / 2}=48 ~min)$ TD-PAC probe is used. The EFG induced by the surrounding charge distribution modulates the half-life histogram of the 245.4- keV intermediate state, which is characterized by 84.5 ns half-life and a spin $I=+\frac{5}{2}$ . Figure 2 schematically describes the $^{111 ~m} Cd$ decay cascade and the TD-PAC measurement observable. The experimental setup of the TD-PAC spectrometer consists of an array of $6-\gamma$ detectors mounted on the sides of a cube pointing to the center where the sample is fixed. Thirty $\gamma_{1}(150.8 keV)$ vs $\gamma_{2}(245.4 keV)$ coincidence exponential time histograms $\chi_{k}(\theta, t), k=1-30$ , from detector pairs with relative angles $\theta=180^{\circ}(k=6)$ and $\theta=90^{\circ}(k=24)$ are recorded [37].

In Fig. 2, the systematic errors and the half-life exponential component that is common for all spectra are eliminated by constructing the experimental ratio function R(t), which hasthe form given by Eq. (1):
$$\begin{aligned}
R(t) & =2 \frac{\sqrt[6]{\prod_{j}^{6} N_{j}\left(180^{\circ}, t\right)}-\sqrt[24]{\prod_{i}^{24} N_{i}\left(90^{\circ}, t\right)}}{\sqrt[6]{\prod_{j}^{6} N_{j}\left(180^{\circ}, t\right)}+2 \sqrt[24]{\prod_{i}^{24} N_{i}\left(90^{\circ}, t\right)}} \\
& =A_{22} G_{22}(t).
\end{aligned}\qquad(1)$$

The $N_{k=i or j}(\theta, t)$ are the $\chi_{k}(\theta, t)$ experimental spectra after removal of the time-independent chance coincidences background and after time shift synchronization to reveal the perturbation function $G_{22}(t)$ . The histogram $N_{k}(\theta, t)$ spectra are the convolution of the time resolution function of each pair of detectors with the time decay exponential, characteristic of the half-life of the probing intermediate state of the gamma- ray cascade. For each of the 30 spectra, a fit is performed to determine the experimental time resolution and the real number channel $N_{0}(k)$ corresponding to the time =0 between the detection of $\gamma_{1}$ and $\gamma_{2}$ .

No(k) is always behind the channel with the maximum of the convoluted exponential, on a zone with a stiff slope that leads to easy uncertainties of time-zero determination. Consequently, the first points of the R(t) function, close to t = 0, are of poor quality and were not considered for fitting. Once the $N_{0}(k)$ numbers are determined the $N_{k}(\theta, t)$ spectra will be time shifted to a common initial channel corresponding to t = 0 using a simple interpolation method.

R(t) emphasizes, first, the effective amplitude of the angu- lar correlation $A_{22}$ , which is determined solely by the nuclear cascade characteristics and the solid angle efficiencies of the detector. Second, $G_{22}(t)$ reveals the reorientation of the nu clear spin in the presence of the local fields of the material. For a purely magnetic interaction, $G_{22}(t)$ describes the Larmor spin precession with a frequency proportional to the product of the nuclear state magnetic moment by the magnetic local hyperfine field.

Equation (2) defines the theoretical function $R_{fit }(t)$ by which the parameters are fitted to the experimental R(t) func- tion. For each angle between detectors, $\theta=180^{\circ}, 90^{\circ}$ , the angular correlation functions $W(\theta, t)$ are calculated numer ically by taking into account the full Hamiltonian for the nuclear quadrupole hyperfine interaction [38]. Therefore,
$$R_{\mathrm{fit}}(t)=2\left(\frac{W\left(180^{\circ}, t\right)-W\left(90^{\circ}, t\right)}{W\left(180^{\circ}, t\right)+2 W\left(90^{\circ}, t\right)}\right).\qquad(2)$$

In our case of the pure nuclear quadrupole interactions, there are three observable frequencies for spin $\frac{5}{2}$ : these are $\omega_{1} \leqslant$  w2, w3 = w1 + w2 that provide the signature of the EFG interacting with the nucleus quadrupole moment, due to a specific charge distribution of the respective surroundings.From these values, the quadrupole frequency $\omega_{Q}=e Q V_{z z} /$ [4I(2I-1) $\hbar$ ] or its spin-independent version $v_{Q}=e Q V_{z z} / h$ and the asymmetry parameter $\eta=(V_{x x}-V_{y y}) / V_{z z}$ are extracted. The Vzz is defined as the "principal" component of the diagonalized EFG tensor chosen according to $|V_{z z}|>|V_{y y}|>|V_{x x}|$ and the absolute value of $V_{z z}$ can be measured by TD-PAC. When $\eta=$ 0 , the observable $\omega_{1}$ frequency becomes equal to $\omega_{0}$ defined as $\omega_{0}=6 \omega_{Q}$ for half-integer spin or $\omega_{0}=3 \omega_{Q}$ for integerspin. The observation $\omega_{1}, \omega_{2}, \omega_{3}$ frequencies depend on $\omega_{Q}$  and $\eta$ as described in Ref. [36]. We consider the quadrupole moment to be Q = 0.664(7)b, as reported in Ref. [39], for the intermediate state of $^{111} Cd$ .

In the case of interactions with randomly distributed de- fects, a distribution of frequencies is observed that broadens the frequency spectrum and attenuates R(t) as a function of time. In this work the distributions around a central $v_{Q}$ value are only assumed as Lorentzia type for fitting purposes. Their

width is characterized by $\sigma = \text{FWHM}/2$ that depends on the density and variety of the lattice defects [40].

### B. Sample preparation
$\text{MoO}_3$ lamellar crystals were grown by the evaporation solidification method described in detail in Refs. [5,30]. A disk of compacted Mo powder was placed at the center of a horizontal tube furnace at a temperature of $750\,^\circ\text{C}$ for 10 h, under 2 l/min airflow. The heating of the disk promotes the oxidation of Mo by direct contact with the oxygen from the air. Lamellar $\text{MoO}_3$ crystals then grow at the cooler ends of the tube, where the temperature is about $400\,^\circ\text{C}$–$450\,^\circ\text{C}$. From the batch of selected crystals, the majority, $\sim$70%, had 2–4 $\mu\text{m}$ of thickness [30], and the remaining were thicker and larger crystallites, up to $100\,\mu\text{m}$ of thickness, with an approximate area of $2 \times 5\,\text{mm}^2$. The reason to choose large sized crystallites was for easy handling. These lamellar crystals have a surface orientation of [010], as determined by XRD measurements [5], showing the lower growth rate along the [010] compared to the perpendicular directions, and consistent with previous studies [41,42]. The selected batch of crystals was separated into several groups, each containing one or two larger crystallites. Each group of crystallites was carefully fixed in different positions of the sample holder with clamps and mounted inside the implantation vacuum chamber. The $^{111\text{m}}\text{Cd}$/$^{111}\text{Cd}$ with half-life time around $T_{1/2}=48$ min was produced online from a molten tin target with a plasma ion source at the ISOLDE/CERN facility and implanted at RT with 30-keV energy and low fluences of $5 \times 10^{11}\,\text{at/cm}^2$. Due to the short lifetime of $^{111\text{m}}\text{Cd}$, we carried out an independent cycle of implantation for each measurement. The post-implantation annealing step was kept at a relatively short 10-min time interval and the TD-PAC measurement was performed for each group of samples and each measurement, which takes about 3 h to complete. Subsequently to the implantation, the $\text{MoO}_3$ samples were removed from the clamps to be first annealed under air. On the first cycle of experiments, dedicated to studying the recovery of implantation defects, the TD-PAC measurements were performed in a 6 $\text{BaF}_2$ detector analog spectrometer as described in Ref. [37] at RT after annealing at $300\,^\circ\text{C}$ and $320\,^\circ\text{C}$. On the second cycle of experiments, the TD-PAC measurements were performed under air, as a function of temperature between RT and $300\,^\circ\text{C}$, for samples that were previously annealed at $450\,^\circ\text{C}$.

### C. Density functional theory
The Vienna *ab initio* simulation package (VASP) code [43] was employed to perform initial structural relaxations and also to calculate formation energies of the supercells and the partial charge densities by using the lattice constants optimized with the WIEN2K code. The projector augmented wave (PAW) scheme was considered with the following configurations: $\text{Mo}[4p^64d^55s^1]$, $\text{O}[2s^22p^4]$, and $\text{Cd}[4d^{10}5s^2]$. Convergence of the total energy was achieved with a plane-wave kinetic-energy cutoff of 500 eV. The generalized-gradient approximation (GGA) functional with the Perdew-Burke-Ernzerhof parametrization [44] was used for all the calculations. The rotationally invariant DFT+$U$ approach, introduced by Liechtenstein *et al.* [45], was utilized to account for the onsite Coulomb interactions of the $d$ Mo states, by considering an effective Hubbard potential of $U_{\text{eff}}=U-J=6$ eV. The value of $U_{\text{eff}}$ is considered from the article of Ding *et al.* [46]. These authors concluded that the obtained results by resorting to the value of $U_{\text{eff}}=6$ was in good agreement with the atomic geometries obtained by the hybrid HSE06 method. The long-range vdW interactions for all systems were described in the context of dispersion corrections using the Becke and Johnson damping function DFT-D3(BJ) [47,48]. The Brillouin-zone (BZ) was sampled with a $12 \times 2 \times 8$ Monkhorst-Pack k-point mesh for the unit cell [49]. The convergence criterion was considered when the Hellmann Feynman forces where less than $0.01\,\text{eV}/\mathring{\text{A}}$ per atom. To perform the supercell calculations, a cell size of $3 \times 1 \times 2$ was used with a reduced k-point mesh of $4 \times 2 \times 4$.

<table>
<caption>TABLE I. Lattice parameters calculated with different XC functions. The quoted % refers to relative deviations from the experimental values [51].</caption>
<thead>
  <tr>
    <th>XC functional</th>
    <th>$a$ ($\mathring{\text{A}}$)</th>
    <th>%</th>
    <th>$b$ ($\mathring{\text{A}}$)</th>
    <th>%</th>
    <th>$c$ ($\mathring{\text{A}}$)</th>
    <th>%</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>PBE</td>
    <td>3.95</td>
    <td>−0.34</td>
    <td>13.81</td>
    <td>−0.33</td>
    <td>3.68</td>
    <td>−0.34</td>
  </tr>
  <tr>
    <td>LDA</td>
    <td>4.00</td>
    <td>0.99</td>
    <td>13.99</td>
    <td>0.99</td>
    <td>3.73</td>
    <td>0.99</td>
  </tr>
  <tr>
    <td>PBE-D3(BJ)</td>
    <td>3.98</td>
    <td>0.33</td>
    <td>13.90</td>
    <td>0.33</td>
    <td>3.71</td>
    <td>0.31</td>
  </tr>
  <tr>
    <td>Expt. [51]</td>
    <td>3.96</td>
    <td></td>
    <td>13.86</td>
    <td></td>
    <td>3.70</td>
    <td></td>
  </tr>
</tbody>
</table>

The full potential linearized augmented plane wave (FP-LAPW) method as implemented in the WIEN2K code [50], was employed for optimizing the structural lattice parameters of the cell and to compute the hyperfine parameters ($V_{zz}$, and the axial asymmetry $\eta$ parameters). As an all-electron method, WIEN2K has proven to be a benchmark for calculating hyperfine parameters. Therefore, we have chosen this code for a more accurate interpretation of the experimental TD-PAC data. In this calculation, the cutoff parameter $R_{\text{MT}} \times K_{\text{MAX}}$, which controls the size of the basis set, is set to 8.0. A mesh of $(6 \times 3 \times 3)\,\mathbf{k}$ points in the irreducible part of the first Brillouin zone (BZ) was applied to the self-consistent total energy calculation. The radii of the muffin-tin atomic spheres of Cd, Mo, and O are set to 1.99, 1.65, and 1.42 a.u., respectively. In addition, the energy value of $-8$ Ry is set as the boundary separating the core electron states and valence electron states.

The volume optimization on the pristine unit cell was performed by considering the dispersion corrections so that the interlayer distances could be more accurately described. Knowing that the room-temperature experimental lattice constants are $a=3.96\,\mathring{\text{A}}$, $b=13.85\,\mathring{\text{A}}$, and $c=3.69\,\mathring{\text{A}}$ for the $\alpha\text{-MoO}_3$ with $Pbnm$ space group [51], we have performed volume relaxations by employing different exchange-correlation (XC) functionals in order to confirm the best suited method to describe the system (Table I). In Table I, we note that the optimized lattice constants agree well with the experimental $\alpha\text{-MoO}_3$ lattice constants [51] when the effect of long-range dispersion forces is taken into account.

Since the framework of DFT does not take temperature effects into account, the experimental $\alpha\text{-MoO}_3$ lattice parameters at room temperature were used for the systems with different defect complexes to allow for a more comparable


![](./images/844586205617061889_4.jpg)

FIG. 3. Left: the $R(t)$ TD-PAC observable (black points) with the respective fit (red line) as a function of time. Right: the respective Fourier transforms. The blue lines in the Fourier spectra mark the triplets of observable frequencies characteristic of every EFG. The experimental points result from merging similar data obtained with two implanted samples that were annealed at $300\,^\circ\text{C}$ and $320\,^\circ\text{C}$, respectively. The measurement was performed at RT.

interpretation of the results with experimental data. The internal parameters were then relaxed by force optimization to a threshold value below $1\ \text{mRy}/\mathring{\text{A}}$. The best set of internal lattice parameters was used as a starting point for the calculations upon searching for the EFG signatures characteristic of specific nanoscopic configurations of the cell, as revealed by the TD-PAC experiments.

### III. RESULTS
#### A. TD-PAC experiments

Figures 3 and 4 present the TD-PAC results measured at RT and at RT to higher temperatures, respectively. In the mentioned figures, the $R(t)$ experimental observable and the corresponding best fit functions are plotted as a function of time (left), and the corresponding (real part) Fourier transform is shown on the right. The conditions of the measurements are indicated on each set of figures, where the fits are also described. The notation $\text{EFG}i$, $i=1$–$6$, refers to different EFGs calculated using the hyperfine parameters which are obtained from the fit. $\text{EFG}d$ characterizes a broad EFG distribution that generally characterizes a set of $^{111}\text{Cd}$ probe atoms in highly disturbed environments. In the Fourier diagrams of each $\text{EFG}i$, we highlight the triplet of characteristic frequencies with an abbreviated Ei notation for graphical simplicity. Table II and the first row of Table III show the fitting results of the TD-PAC spectra measured at RT and annealed at $310\pm10\,^\circ\text{C}$ and $450\,^\circ\text{C}$, respectively. Although visual inspection of the plot reveals that annealing at $450\,^\circ\text{C}$ produces more defined spectra, the values of the hyperfine parameters show that the broadly distributed interaction ($\text{EFG}d$) in the $450\,^\circ\text{C}$ annealed spectrum is not only better defined, but also the fit was performed with only one additional well-defined interaction (EFG4), while the spectrum for the sample annealed at $310\pm10\,^\circ\text{C}$ was fitted with three additional well-defined interactions (EFG1, EFG2, and EFG3).

Figure 3 shows the $R(t)$ data taken for the measurement at room temperature, $\text{TM}=\text{RT}$, with fitting analysis and corresponding Fourier transform of a spectrum obtained by merging data collected after implantation and subsequent annealing at the temperature of $\text{TA}=300\,^\circ\text{C}$ and $\text{TA}=320\,^\circ\text{C}$, 10 min, in air with similar characteristics. Both spectra are very similar and this procedure enables the improvement of the measurement statistics, which is low due to the short lifetime of the $^{111\text{m}}\text{Cd}$/$^{111}\text{Cd}$ probe isotope. Table II contains the corresponding fitting parameters obtained for each EFG

![](./images/844586205617061889_5.jpg)

FIG. 4. Left: the $R(t)$ TD-PAC observable (black points) with the corresponding fit (red line) as a function of time. Right: the respective Fourier transforms. The blue continuous lines at the Fourier spectra highlight the triplets of the observable frequencies characteristic of every EFG. The figure shows data of implanted samples that were subsequently annealed in air for 10 min at $450\,^\circ\text{C}$. The measurements were then performed at $24\,^\circ\text{C}$, $100\,^\circ\text{C}$, $120\,^\circ\text{C}$, $200\,^\circ\text{C}$, and $300\,^\circ\text{C}$. Similar results were obtained at $100\,^\circ\text{C}$ and $120\,^\circ\text{C}$ and the data were merged on a single spectrum.

<table>
<caption>TABLE II. The fit parameters $v_Q$, $\eta$, $|V_{zz}|$, $\sigma$ are obtained for merged $R(t)$ data obtained from implanted samples after annealing at $300\,^\circ\text{C}$ and $320\,^\circ\text{C}$, with measurements performed at RT. The sign of $V_{zz}$ is not determined by TD-PAC.</caption>
<thead>
  <tr>
    <th colspan="5">TA=$310\pm10\,^\circ\text{C}$, TM=RT</th>
  </tr>
  <tr>
    <th>
    </th>
    <th> $v_Q$ (MHz)
    </th>
    <th> $\eta$
    </th>
    <th> $|V_{zz}|$ ($\text{V}/\text{\AA}^2$ )
    </th>
    <th> $\sigma$ (MHz)
    </th>
    <th> $f$\%
    </th>
  </tr>
</thead>
<tbody>
  <tr>
    <td> EFG1
    </td>
    <td> 54.9(6)
    </td>
    <td> 0.40(4)
    </td>
    <td> 34.2(5)
    </td>
    <td> ~ 0
    </td>
    <td> 12(2)
    </td>
  </tr>
  <tr>
    <td> EFG2
    </td>
    <td> 108.6(1.0)
    </td>
    <td> 0.19(3)
    </td>
    <td> 68(1)
    </td>
    <td> 5(1)
    </td>
    <td> 26(3)
    </td>
  </tr>
  <tr>
    <td> EFG3
    </td>
    <td> 313(1)
    </td>
    <td> 0.32(1)
    </td>
    <td> 195(2)
    </td>
    <td> 2(1)
    </td>
    <td> 13(2)
    </td>
  </tr>
  <tr>
    <td> EFGd
    </td>
    <td> 234.7(9.5)
    </td>
    <td> 0.33(6)
    </td>
    <td> 146(6)
    </td>
    <td> 52(2)
    </td>
    <td> 48(5)
    </td>
  </tr>
</tbody>
</table>

component included in the fitting function. We emphasize three aspects: (a) an important fraction $f_d \sim 50\%$ of Cd probes resides in highly disturbed environments, and is characterized by a broad frequency distribution ($\sim$40%), most likely due to unrecovered implantation defects; (b) a clear EFG 2 accounting for $f_2 \sim 26\%$ of the Cd probes is found in a regular, well-defined environment; and (c) the presence of smaller fractions $f_1$, $f_3$, may suggest the Cd probe atoms interacting with different local environments. Although the inclusion of EFG1 and EFG3 improves the fit, their respective parameters cannot be uniquely defined within the present statistics since different combinations of $v_Q$ and $\eta$ could lead to similar quality fits. Figure 4 shows the $R(t)$ data with fit analysis and respective Fourier transform of spectra obtained from samples after implantation and annealing at $450\,^\circ\text{C}$, during 10 min under atmospheric condition. Respective spectra were measured at different temperatures, namely, at the temperatures of $24\,^\circ\text{C}$, $100\,^\circ\text{C}$, $120\,^\circ\text{C}$, $200\,^\circ\text{C}$, and $300\,^\circ\text{C}$. Similar results were obtained at $100\,^\circ\text{C}$ and $120\,^\circ\text{C}$ and the data were merged on a single spectrum identified as $110\,^\circ\text{C}$. Table III contains the corresponding fit parameters obtained for every EFG component, which are included in the fitting function of each spectrum. There is a relevant effect in the TD-PAC spectra, when the post-implant annealing temperature has been increased from $300\,^\circ\text{C}$ to $450\,^\circ\text{C}$. This is emphasized by the fact that a main EFG4 is now clearly revealed throughout all spectra. Increasing the temperature certainly plays an important role in annealing implantation defects and promoting Cd to a well-defined site/defect complex. Such a feature can be observed from the temperature dependence of the main EFG parameters (EFG4), $V_{zz}$ and $\eta$ in Table III. The decrease of $V_{zz}$ and the increase of the axial symmetry parameter $\eta$ as a function of temperature strongly suggests that Cd sits on a site with specific environment that is particularly sensitive to temperature; this leads to a more asymmetric local charge distribution at high temperature.

The spectra obtained at $24\,^\circ\text{C}$, $110(10)\,^\circ\text{C}$, and $300\,^\circ\text{C}$ still show, in addition to EFG4, the presence of important contributions from Cd probes in highly disturbed environments characterized by wide EFG$d$ distributions with high $\sigma$ values. This fraction $f_d$ is reduced for measurements performed at higher temperatures, suggesting that additional annealing occurs during the measurement. At the same time, the fit provides evidence of additional small fractions of probes characterized by new EFG5 and EFG6. Such behavior, occurring as a function of measurement temperature up to $300\,^\circ\text{C}$, leads us to suggest that the 10-min annealing time at $450\,^\circ\text{C}$ might be too short for complete recovery of the implantation defects and the stabilization of the Cd-defects configuration. Similar conclusions have been drawn for the optical activation of rare-earth ions in $\text{MoO}_3$ where 30-s rapid thermal annealing at $550\,^\circ\text{C}$ proved less efficient than 4-h conventional annealing at $450\,^\circ\text{C}$ [52].

Since each TD-PAC measurement takes about 3 h, the final spectrum contains a cumulative effect of two factors: (1) the first annealing step at higher temperature (TA) and (2) the lower acquisition measurement temperature (TM) (and annealing temperature) during an extended

<table>
<caption>TABLE III. The fit parameters $v_Q$, $\eta$, $|V_{zz}|$, $\sigma$ are obtained for merged $R(t)$ data obtained from implanted samples after annealing at $450\,^\circ\text{C}$, with measurements performed at $24\,^\circ\text{C}$, $100\,^\circ\text{C}$, $120\,^\circ\text{C}$, $200\,^\circ\text{C}$, and $300\,^\circ\text{C}$. The sign of $V_{zz}$ is not determined by TD-PAC.</caption>
<thead>
  <tr>
    <th colspan="6">TA=$450\,^\circ\text{C}$</th>
  </tr>
  <tr>
    <th>
    </th>
    <th> $v_Q$ (MHz)
    </th>
    <th> $\eta$
    </th>
    <th> $|V_{zz}|$ ($\text{V}/\text{\AA}^2$)
    </th>
    <th> $\sigma$ (MHz)
    </th>
    <th> $f$\%
    </th>
    <th> TM ($^\circ\text{C}$)
    </th>
  </tr>
</thead>
<tbody>
  <tr>
    <td> EFG4
    </td>
    <td> 261.6(4)
    </td>
    <td> 0.484(4)
    </td>
    <td> 163(1)
    </td>
    <td> ~ 1
    </td>
    <td> 37(3)
    </td>
    <td rowspan="2"> 24
    </td>
  </tr>
  <tr>
    <td> EFGd
    </td>
    <td> 225(2)
    </td>
    <td> $0.43(3)$
    </td>
    <td> $140(2)$
    </td>
    <td> $39(5)$
    </td>
    <td> $63(5)$
    </td>
  </tr>
  <tr>
    <td> EFG4
    </td>
    <td> 258.7(1)
    </td>
    <td> 0.505(6)
    </td>
    <td> 161(1)
    </td>
    <td> 1.4(2)
    </td>
    <td> 27(1)
    </td>
    <td rowspan="2"> 110(10)
    </td>
  </tr>
  <tr>
    <td> EFGd
    </td>
    <td> 288.6(7.0)
    </td>
    <td> $^0$
    </td>
    <td> $180(5)$
    </td>
    <td> $68(7)$
    </td>
    <td> $73(2)$
    </td>
  </tr>
  <tr>
    <td> EFG2
    </td>
    <td> 111.5(1.1)
    </td>
    <td> 0.25(3)
    </td>
    <td> 69.4(7)
    </td>
    <td> ~0
    </td>
    <td> 12(2)
    </td>
    <td rowspan="3"> 200
    </td>
  </tr>
  <tr>
    <td> EFG4
    </td>
    <td> 255.0(3)
    </td>
    <td> 0.575(2)
    </td>
    <td> 159(1)
    </td>
    <td> 2.90(4)
    </td>
    <td> 68(3)
    </td>
  </tr>
  <tr>
    <td> EFG5
    </td>
    <td> 494(1)
    </td>
    <td> 0.488(4)
    </td>
    <td> 308(2)
    </td>
    <td> 1.6(9)
    </td>
    <td> 19(2)
    </td>
  </tr>
  <tr>
    <td> EFG4
    </td>
    <td> 244.0(6)
    </td>
    <td> 0.664(9)
    </td>
    <td> 152(1)
    </td>
    <td> 5.6(6)
    </td>
    <td> 50(6)
    </td>
    <td rowspan="4"> 300
    </td>
  </tr>
  <tr>
    <td> EFG5
    </td>
    <td> 493(1)
    </td>
    <td> 0.489(5)
    </td>
    <td> 307(2)
    </td>
    <td> 0(2)
    </td>
    <td> 9(3)
    </td>
  </tr>
  <tr>
    <td> EFG6
    </td>
    <td> 158.3(5)
    </td>
    <td> 0.76(2)
    </td>
    <td> 98.6(8)
    </td>
    <td> ~0
    </td>
    <td> 11(1)
    </td>
  </tr>
  <tr>
    <td> EFGd
    </td>
    <td> $115(19)$
    </td>
    <td> $0.2(1)$
    </td>
    <td> $72(11)$
    </td>
    <td> $46(10)$
    </td>
    <td> $31(6)$
    </td>
  </tr>
</tbody>
</table>

![](./images/844586205617061889_6.jpg)

FIG. 5. Structure of Cd-doped $\alpha$-MoO₃ with a nominal concentration of 4.16% [Cd] in substitutional site (left) and interstitial site (right).

3-h time, leading to the identification of several Cd local environments in the $\alpha$-MoO₃ lattice, which are due to the formation of different Cd-defect complexes. The analysis of the experimental results, as well as the detail regarding the local crystalline environment of Cd under the influence of augmenting the annealing and measurement temperature, will be further discussed in the next section, with support from DFT simulations.

### B. DFT results and discussion
#### 1. Stability of the Cd ion in $\alpha$-MoO₃ lattice

After $^{111\text{m}}$Cd implantation and annealing of the $\alpha$-MoO₃ samples, the persistence of a multitude of different EFG signatures, resulting from the TD-PAC data, indicates that Cd interacts with point defects that are most likely oxygen vacancies. To describe and analyze the experimental results in detail, we have performed DFT simulations of $\alpha$-MoO₃ doped with Cd, for a variety Cd sites and configurations of Cd with oxygen defect complexes. For these calculations, we used the DFT+$U$ Hubbard model to handle the strongly correlated $d$ states of Mo, as well as a dispersion corrected term, DFT+D3(BJ), due to the layered nature of the structure.

Due to the concentrations of implanted $^{111\text{m}}$Cd, which are of the order of parts per million (PPM), the simulated supercells have to be created as large as possible to minimize the interaction of multiple Cd atoms at periodic supercell images and to avoid unrealistic doping effects regarding the TD-PAC experiments. However, the choice of supercells, according to the experimental concentration, is prohibitively time-consuming. Therefore, the size of the supercell is carefully chosen based on the minimum distance between the Cd ions in periodic supercell images so that their charge distributions do not overlap.

Figure 5 shows the supercell size of $3\times1\times2$ ($a\times b\times c$ crystalline axes, respectively) chosen for all calculations, which represents a good compromise between computational time and EFG convergence and corresponds to a nominal Cd concentration of about 4.16%. Different Cd-impurity sites in $\alpha$-MoO₃ were simulated by considering the substitutional Mo position (Fig. 5, left), $\text{Cd}_s$, the interstitial implantation point (Fig. 5, right), $\text{Cd}_I$, and their interaction with oxygen vacancies. The final position of Cd with or without vacancies in the lattice was mainly derived by comparing the experimental EFG values ($V_{zz}$ and $\eta$) with those obtained from a variety of DFT simulations. The calculation of the formation energies for the final configurations is another step that contributes to the understanding of the local Cd site and defect formation as well as their stability.

The formation energy of the $\text{Cd}_s$ atom at the $\alpha$-MoO₃ lattice site was calculated in the form of [53,54]

$$
\begin{aligned}
E_{F(\text{Cd}s)} &= E(\text{Mo}_{1-x}\text{Cd}s_x\text{O}_3) - E(\text{MoO}_3) \\
&\quad + (1 - x)E_{\text{Mo}} - xE_{\text{Cd}},
\end{aligned} \tag{3}
$$

where $x = N_s / T_{\text{Mo}}$, with $N_s$ being the number of substitutional impurities in the supercell and $T_{\text{Mo}}$ is the total number of Mo atoms in the supercell. $E(\text{Mo}_{1-x}\text{Cd}s_x\text{O}_3)$ is the total energy of the implanted system, $E(\text{MoO}_3)$ is the total energy of pristine $\alpha$-MoO₃; the $E_{\text{Mo}}$ and $E_{\text{Cd}}$ are the total energies of Mo in the bulk body-centered-cubic phase and Cd in the bulk hexagonal-close-packed (hcp) RT phases, normalized to the total number of atoms of the cells.

In the case of the interstitial Cd atom at $\alpha$-MoO₃, the formation energy can be calculated according to the following equation [55]:

$$
E_{F(\text{Cd}I)} = E(\text{MoCd}_I_n\text{O}_3) - E(\text{MoO}_3) - nE_{\text{Cd}}, \tag{4}
$$

where $n$ is the number of interstitial atoms in the host lattice, the $E(\text{MoCd}_I_n\text{O}_3)$ is the total energy of the $\alpha$-MoO₃ system with the $\text{Cd}_I$ impurity.

The calculated formation energies ($E_F$) for substitutional and interstitial Cd in $\alpha$-MoO₃ are presented in Table IV. With a significantly lower $E_F = 1.25$ eV, the Cd impurity, $\text{Cd}_I$, located within the vdW gap in the $\alpha$-MoO₃ structure, is shown to be the most energetically stable configuration. The coordination of the $\text{Cd}_I$ is found to be in a tetragonally distorted octahedral, surrounded by oxygen atoms. From this, we can conclude that Cd prefers to stabilize within the vdW gap rather than the substitutional or other interstitial sites. Also, this feature is in agreement with Ref. [56], as they predict that the interstitial site between two layers is the most stable, due to sufficient interlayer spacing caused by the weak

TABLE IV. DFT computed hyperfine parameters $V_{zz}$, $\eta$ and total formation energies $E_{F}$ by considering the effect of onsite Coulomb interaction $U_{\text{eff}}$, to treat the $d$ states of Mo, and dispersion corrections [DFT-D3(BJ)]. The calculated multiple defect configurations are tentatively assigned to experimental values.

<table>
  <thead>
    <tr>
      <th rowspan="2">Configuration</th>
      <th colspan="3">Method : PBE $+U=6$ eV (Mo)</th>
      <th>Experimental</th>
    </tr>
    <tr>
      <th>$V_{zz}$ (V/Å²)</th>
      <th>$\eta$</th>
      <th>$E_{F}$ (eV)</th>
      <th>EFG</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Cd$_s$</td>
      <td>45.18</td>
      <td>0.950</td>
      <td>4.750</td>
      <td></td>
    </tr>
    <tr>
      <td>Cd$_I$</td>
      <td>54.13</td>
      <td>0.240</td>
      <td>1.250</td>
      <td>EFG2</td>
    </tr>
    <tr>
      <td>Cd$_I^{VO1a}$</td>
      <td>−134.26</td>
      <td>0.086</td>
      <td>1.124</td>
      <td></td>
    </tr>
    <tr>
      <td>Cd$_I^{VO1b}$</td>
      <td>−77.74</td>
      <td>0.354</td>
      <td>1.130</td>
      <td></td>
    </tr>
    <tr>
      <td>$^{VO1a}$Cd$_I^{VO1b}$</td>
      <td>−185.17</td>
      <td>0.215</td>
      <td>1.053</td>
      <td></td>
    </tr>
    <tr>
      <td>Cd$_I^{VO2}$</td>
      <td>190.24</td>
      <td>0.373</td>
      <td>1.150</td>
      <td>EFG 3</td>
    </tr>
    <tr>
      <td>$^{VO2}$Cd$_I^{VO2}$</td>
      <td>−48.87</td>
      <td>0.255</td>
      <td>1.046</td>
      <td></td>
    </tr>
    <tr>
      <td>$^{VO2}$Cd$_I^{VO2}$</td>
      <td>173.96</td>
      <td>0.545</td>
      <td>1.041</td>
      <td>EFG 4</td>
    </tr>
  </tbody>
</table>

vdW interactions effect in the Co and Sn co-doped system of $\alpha$-MoO$_3$.

Since different EFG signatures appear in the TD-PAC data measurements, this fact may indicate that Cd interacts with point defects, which are most likely to be the oxygen vacancies. For this reason, we have considered systems with different complexes of oxygen vacancies. To calculate the formation energies of the $\alpha$-MoO$_3$ lattice with these native defects, MoCd$_n$O$_{3-y}$, we have considered the following expression [53,57]:

$$
\begin{aligned}
E_{F(\text{CdO})}=E\left(\mathrm{MoCd}_{n} \mathrm{O}_{3-y}\right)-E\left(\mathrm{MoCd}_{n} \mathrm{O}_{3}\right)+\frac{N_{\mathrm{vac}}}{2} E\left(\mathrm{O}_{2}\right). \\
(5)
\end{aligned}
$$

$E(\text{MoCd}_n O_{3-y})$ is the total energy of the Cd-doped $\alpha$-MoO$_3$ with oxygen vacancies, $N_{\text{vac}}$ is the number of oxygen vacancies per supercell, and $E(\text{O}_2)$ is the reference energy for the oxygen molecule at $T=0$ K. The final total formation energy of a specific supercell will then be obtained by adding $E_{F(\text{CdO})}$ to the formation energies of nondefective system [53]. The VASP code is used to calculate the formation energies of the vacancy and nonvacancy systems because the calculated electronic energy for the oxygen molecule is in closer agreement with experimental values (5.2 eV) [57,58], when compared with the results from the WIEN2K code.

### 2. Experimental and DFT electric field gradients
For further interpretation of the experimental results, the different defect complexes located around the Cd site, that are most compatible with the experimental EFGs value, are presented with the following nomenclature:
(1) Cd$_I$ with one oxygen vacancy of O1a, $^{VO1a}$Cd$_I$,
(2) Cd$_I$ with one oxygen vacancy of O1b, Cd$_I^{VO1b}$,
(3) Cd$_I$ with two O1 vacancies, $^{VO1a}$Cd$_I^{VO1b}$,
(4) Cd$_I$ with one O2 vacancy, Cd$_I^{VO2}$,
(5) Cd$_I$ with two O2 vacancies in the same plane, $^{VO2}$Cd$_I^{VO2}$,
(6) Cd$_I$ with two O2 vacancies in different planes $^{VO2}$Cd$_I^{VO2}$.

The positions of O1a, O1b, and O2 are shown in Fig. 5. Table IV lists the calculated values of $V_{zz}$, $\eta$, and total formation energies $E_{F}$ of these configurations as well as a tentative assignment of the EFG signatures obtained from the fit to the TD-PAC data. By analyzing the formation energies of the defect complexes, we observed that the configuration of the Cd$_I$ atom, which is surrounded by two O2 vacancies in different planes ($^{VO2}$Cd$_I^{VO2}$) is energetically the most favorable and is therefore the most stable defect complex with $E_F=1.041$ eV. Although the formation energy of other defect complexes, such as Cd$_I$ with two O2 vacancies in the same plane ($^{VO2}$Cd$_I^{VO2}$), is in the same range of energies as $^{VO2}$Cd$_I^{VO2}$, but the EFGs signatures of $^{VO2}$Cd$_I^{VO2}$ configurations were not observed in the TD-PAC experimental results. This could be due to the fact that implantation is a nonthermal equilibrium process that may favor one defect over the other. The best way to determine which defect complexes appear in the sample after implantation of the $^{111\text{m}}$Cd ion is by comparing the calculated EFGs ($|V_{zz}|$, $\eta$) with experimental results. From the combined analysis of the DFT calculations with TD-PAC measurements at RT (Table II), as shown in Fig. 6, we may conclude that after implantation and a short annealing time (10 min) at temperatures of $310(10)^\circ$C/air, the main EFG2 with the values of $V_{zz}=68(1)$ V/Å² and $\eta=0.19(3)$ can be assigned to the single interstitial Cd$_I$ site. For this impurity position, the simulated $\eta=0.24$ is obtained in reasonable agreement with the experimental value, with a $\sim 20$ % difference in the simulated $V_{zz}=54.13$ V/Å². This amount of discrepancy observed in $V_{zz}$ may result from the polaron effect [59] surrounding the Cd ion since the employed DFT calculations do not account for the phonon-electron coupling. Further discussion of the polaron effect is presented in Sec. III B 4.

Another configuration found from DFT calculations, which we consider to be consistent with the experimental EFG3 hyperfine parameters [$V_{zz}=195(2)$ V/Å² and $\eta=0.32(1)$] is the Cd$_I^{VO2}$ single-vacancy defect complex, with $E_F=1.150$ eV and with the calculated hyperfine parameters of $V_{zz}=190.24$ V/Å² and $\eta=0.373$. When the annealing temperature in the first step is raised to $450^\circ$C, a much more stable defect associated to the Cd impurity occurs, which is characterized by EFG4 (Table III). From Table IV, and again by comparing the hyperfine parameters between DFT and TD-PAC measurements, we assign the EFG4 to the Cd$_I$ stabilized with two O2 vacancies at different layered planes of $\alpha$-MoO$_3$ ($^{VO2}$Cd$_I^{VO2}$), which is the most stable configuration found from DFT. The calculated DFT $V_{zz}$ and $\eta$ values are $173.96$ V/Å² and $0.545$, respectively; whereas the measured

![](./images/844586205617061889_7.jpg)

FIG. 6. Plot of comparison data between the calculated hyper- fine parameters $(|V_{zz}|, \eta)$ and experimental results for the different configuration of Cd in $\alpha-MoO_{3}$. The dashed lines and colored lines are corresponding to the calculated DFT results and the circle points are corresponding to the experimental results for different config- urations. The calculated $|V_{zz}|$ and $\eta$ that could be matched to the experiments are plotted in color.

experimental $V_{zz}$ and $\eta$ values of EFG4 are 163(1) $V / \AA^{2}$ and0.484(4), respectively.

To estimate the changes in the hyperfine parameters $(V_{z z}$ , n) of the experimental EFG4 component as a function of temperature, the configuration of $^{VO 2} Cd_{I V O 2}$ is simulated considering the experimental lattice constant obtained for different temperatures. The values of the lattice constant at different temperatures are given in Ref. [60]. The calculated $V_{z z}$ and $\eta$ parameters are plotted in Fig. 7 (left). As we may observe, by increasing the measurement temperature, the main parameter of the EFG $(V_{z z})$ decreases and the axial symmetry parameter $(\eta)$ increases, which is consistent with the experi mental results shown in Fig. 7 (right).

![](./images/844586205617061889_8.jpg)

FIG. 7. Left: the calculated $V_{z z}$ (left axis, shown by the black circles), and $\eta$ (right axis represented by blue squares), for the $^{VO 2} Cd_{I V O 2}$ configuration calculated by considering the experimental lattice constant at different temperature values, as presented in Ref. [60]. The calculations are done by employing $PBE+U_{Mo}=6 eV$ and the dispersion corrections [DFT-D3(BJ)]. Right: the experimental temperature dependence of $V_{z z}$ and $\eta$ of the main EFG parameters (EFG4) (samples after annealing at $450^{\circ} C$ ) for temperatures ranging from $24^{\circ} C$ up to300°C.

## 3. Electronic properties: Partial density of states

The partial density of states (PDOS) and partial charge densities (PCD) around the Fermi energy for pristine $\alpha-MoO_{3}$ are presented in Fig. 8. We may observe from the PDOS[Fig. 8 (left)] that the valence band maximum (VBM) is mostly composed of O p states, with all the three inequivalent O sites, whereas the conduction band minimum (CBM) is mainly formed by Mo $d$ states, as is common for most existing oxides. Figure 8 (right) shows the corresponding isosurface of the charge densities projected around the Fermi energy.

When introducing an interstitial Cd impurity into the lat- tice, a variation of the density of states occurs. Figure 9 (left) shows the PDOS of $\alpha-MoO_{3}$ with the Cd impurity at the interstitial position. For this system, we observe a localized peak consisting mainly of the O2 states, with some mixture of Mo $4 d$ states, slightly below the Fermi energy, which we infer it to be the polaron peak. An increase in density is observed for the $O p$ states when the $Cd$ impurity is considered in the lattice. The presence of the oxygen and Mo localized states around the Fermi energy leads to a distribution of charges mainly over the surrounding Mo sites, as can be seen in Fig. 9 (right), and when compared to the pristine system. The increase in charge distribution is due to the release of electrons between $Mo^{5+}$ and $Mo^{6+}$ , which are the closest neighbors of the $Cd$ ion, as it is shown in the corresponding charge densities in Fig. 9 (right). These electrons will become trapped at the $Cd_{I}$ site, leading to the formation of a small po laron effect (see Sec. III B 4 for more details). Since polarons involve a single trapped excess electron, and the system is simulated considering spin polarization, the defect level splits into two spin states (majority and minority). Therefore, the oxygen peak located within the band gap originates entirely from the occupied majority spin states. By analyzing the defect complexes $Cd_{I V O 2}$ and $^{VO 2} Cd_{I V O 2}$ (Figs. 10 and 11, respectively), strong variations around the Fermi energy are observed, when compared to the $Cd_{I}$ system without oxygen vacancies. For the $Cd_{I V O 2}$ complex [Fig. 10 (left)], we ob serve a larger spectral weight of the minority spin channel, which is essentially formed by Mo $d$ states, when comparing

![](./images/844586205617061889_9.jpg)

FIG. 8. Left: partial density of states of the pristine $\alpha$-MoO$_3$ system. Right: corresponding isosurface of the charge densities projected around the Fermi energy (addition of partial charge densities of the VBM and CBM).

to the Cd$_I$ system. By looking at the charge densities around the Fermi energy [Fig. 10 (right)], we find that a larger fraction of charge distribution occurs, not only at the Mo ions close to the vacant oxygen site, but also at other Mo sites. The PDOS of the $^{VO2}$Cd$_I$ $_{VO2}$ complex [Fig. 11 (left)] shows two localized oxygen polaron centers very close to the CBM, with the first peak distinctly formed by O $p$ states, and the second formed by a hybridization of oxygen $p$ states with a small amount of Mo $d$ states. By looking at the isosurfaces corresponding to the charge densities around the Fermi energy [Fig. 11 (right)], these are largely distributed throughout the different Mo and O sites of the lattice. The symmetry-breaking distortion lowers the energy of the polaron state into two localized peaks inside the band gap. The deformation of the lattice structure seems to have a visible effect on the composition of the polaron peak in the density of states, indicating that rehybridization between O and Mo states is taking place.

### 4. Electron and hole polarons: Charge localization and lattice deformation
By observing the charge density differences (CDD) between the Cd$_I$ system at $\alpha$-MoO$_3$, and the pristine $\alpha$-MoO$_3$, and also with the pure crystal Cd atom, we find that most of the negative charge accumulation is localized at the Cd site (Fig. 12). In addition, some charge accumulation can be seen around oxygen and Mo, which are the nearest neighbors of the Cd impurity ion. While for the oxygen and Mo ions, the localized charges are due to both electron and hole carriers, the Cd center is surrounded by negative charges. This effect resembles the behavior of polarons (electrons) and is consistent with what is discussed in the literature sources of Refs. [19,59], regarding small polarons being highly mobile in $\alpha$-MoO$_3$. We observe in the 2D contour map [Fig. 12 (right)] that a high electron density occurs with some charge transfer between the oxygen next neighbors of the Cd impurity, which is consistent with the corresponding PDOS results. From the present calculations, we can infer that the contribution of small polarons around Cd may ultimately contribute as a factor to increase $|V_{zz}|$of the experimental result when compared to the DFT calculation: we must stress that DFT electronic structure calculations do not take into account the vibrational entropy.

By analyzing the CDD of the Cd$_I$ $_{VO2}$ and $^{VO2}$Cd$_I$ $_{VO2}$ defect complexes (Figs. 13 and 14, respectively), we can observe significant variations in the isosurface plot and contour map densities. By removing one of the O2 ions at the vicinity of the Cd site, Cd$_I$ $_{VO2}$ [Fig. 13 (left)], we observe a distribution

![](./images/844586205617061889_10.jpg)

FIG. 9. Left: partial density of states of interstitial Cd-doped $\alpha$-MoO$_3$ system. Right: corresponding isosurface of the charge densities projected around the Fermi energy.

![](./images/844586205617061889_11.jpg)

FIG. 10. Left: partial density of states of interstitial Cd-doped $\alpha$-MoO$_3$ system and with one O2 vacancy, $\text{Cd}_{I\ VO2}$. Right: corresponding isosurface of the charge densities projected around the Fermi energy.

![](./images/844586205617061889_12.jpg)

FIG. 11. Left: partial density of states of interstitial Cd-doped $\alpha$-MoO$_3$ system and with two O2 vacancies, $^{VO2}\text{Cd}_{I\ VO2}$. Right: corresponding isosurface of the charge densities projected around the Fermi energy.

![](./images/844586205617061889_13.jpg)

FIG. 12. Isosurfaces of the charge density differences of the Cd-doped $\alpha$-MoO$_3$ structure where the left plot is the unit-cell representation, and the right plot is the contour map along the (0 0 1) axis and centered at the Cd site. The silver, purple, and red spheres represent the Mo, Cd, and O ions, respectively. The colors of the isosurfaces are attributed to the different charges: blue isosurfaces represent the negative charges and the yellow are the positive charges. The color of the contour plot is assigned with absolute values, where the light blue areas with circular contour lines refer to regions with high-density electrons and the dark blue regions with circular contour lines are of high hole density.

![](./images/844586205617061889_14.jpg)

FIG. 13. Isosurfaces of the charge density differences of the Cd-doped $\alpha$-MoO$_3$ structure, and one O2 vacancy, where the left plot is the unit-cell representations, and the right plot is the contour map along the (0 0 1) axis and centered at the Cd site. The silver, purple, and red spheres represent the Mo, Cd, and O ions, respectively. The colors of the isosurfaces are attributed to the different charges: blue isosurfaces represent the negative charges and the yellow are the positive charges. The color of the contour plot is assigned with absolute values, where the light blue areas with circular contour lines refer to regions with high-density electrons and the dark blue regions with circular contour lines are of high hole density.

of the charge densities to other sites, further away from Cd. While the Cd ion shows a lower charge accumulation (positive and negative), the neighboring Mo site of the O2 vacancy (below the Cd ions) shows a significant increase of both positive and negative charge densities, although the negative charges contribute with a larger portion. This isosurface shows a dumbbell shape along the $x$ axis, indicating a bipolaron orbital originating from a trapped charge carrier at the Mo site. By observing the contour plot of the Cd$_{I VO2}$ system [Fig. 13 (right)], a very large hole density with a dumbbell shape, right below the Cd impurity site, appears. This is consistent with trapped hole charge carriers at the Mo site. The O and Mo atoms surrounding the Cd center also attract a small portion of positive and negative charges.

For the $^{VO2}$Cd$_{I VO2}$ structure, different bipolaron orbitals can be seen at four Mo sites surrounding the Cd impurity [Fig. 14 (left)]. Moreover, we may observe that the charge accumulation increases and spreads to other oxygen and Mo sites, when compared to the Cd$_{I VO2}$ system. When two or more bipolarons are close to each other, they can lower their energy by sharing the same distortions, resulting in an effective attraction between the bipolarons. If the interaction is sufficiently large, then this attraction leads to a bound bipolaron.

![](./images/844586205617061889_15.jpg)

FIG. 14. Isosurfaces of the charge density differences of the Cd-doped $\alpha$-MoO$_3$ structure, and two O2 vacancies, where the left plot is the unit-cell representations, and the right plot is the contour map along the (0 0 1) axis and centered at the Cd site. The silver, purple, and red spheres represent the Mo, Cd, and O ions, respectively. The colors of the isosurfaces are attributed to the different charges: blue isosurfaces represent the negative charges and the yellow are the positive charges. The color of the contour plot is assigned with absolute values, where the light blue areas with circular contour lines refer to regions with high-density electrons and the dark blue regions with circular contour lines are of high hole density.

Cd IMPLANTATION IN $\alpha$-MoO$_3$: AN ...
PHYSICAL REVIEW MATERIALS 7, 033603 (2023)

The isosurfaces and contour maps results correlate well with the formation of polaron effects, especially for the system with O2 vacancies, where hole polarons may emerge. By inducing an O2 vacancy, excess hole carriers tend to become trapped mainly at a next-neighbor Mo cation site. A significant distortion of the lattice occurs, not only because of the native O2 vacancies, through which the neighboring cations have to assume new positions, but also because of the polaron effect induced by the oxygen vacancies. The formation of hole polarons is caused by the presence of oxygen vacancies in the lattice. An oxygen vacancy creates two unpaired electrons near two cations (Mo) surrounding the vacancy, so that each of the two Mo ions accompanying the defect acquires an unbound extra charge. The extra electrons on the metal ion sites interacting with the lattice form a bound lattice polaron, where the charge unbalance due to the oxygen vacancy leads to the formation of a hole polaron.

## IV. CONCLUSION

We have performed a series of TD-PAC measurements and density functional calculations to investigate the effect of the Cd impurity at the MoO$_3$ system. The aim was to compare the theoretical results, mainly by looking at the EFGs, with those obtained by TD-PAC experimental measurements using $^{111m}$Cd as a probe.

Different Cd configurations were investigated to analyze and interpret the experimental results. In this study, the formation energies were calculated to aid in understanding the configuration of the local Cd sites and formation of defects in the $\alpha$-MoO$_3$ lattice. Comparing the theoretical EFG values with the experimental results, we found that the implanted Cd ions preferentially stabilize in an interstitial position within the vdW gap at RT. By accounting for native-type defects, such as oxygen vacancies at the vicinity of the interstitial Cd impurity, we obtained differences in the $V_{zz}$ and $\eta$ values for Cd. Comparing these values to the experimental data, we found that by considering other factors, which included the variation of the annealing temperature, the formation of oxygen vacancies close to the Cd site was indeed possible.

In this study, we found that the oxygen vacancies belonging to the O2 sites were energetically the most favorable and thus leading to the stabilization of the structure. This phenomenon was also theoretically predicted for $\alpha$-MoO$_3$ [61,62], as the $V_{O2}$ has the lowest formation energy compared to other defect types. Therefore, for the theoretical calculations, we considered the system with one O2 vacancy and a second system with two O2 vacancies at the vicinity of the Cd impurity. The results of $V_{zz}$ and $\eta$ for these two cases resulted in better agreement with the experimental values of the EFG3 and the EFG4 components.

Moreover, by introducing the Cd impurity at an interstitial site, we observe a strong positive charge localization around the impurity site, which is indicative of the formation of polarons. On the other hand, by inducing the O2 vacancies into the systems, we observe an increase of the polaron isosurfaces, mainly around the Mo atoms that are located in the vicinity of the O2 vacancy site(s). Moreover, in the case of the $Cd_{I VO2}$ system, we observe the formation of a dumbbell-shaped orbital at one of the Mo sites, whereas for the $^{VO2}Cd_{I VO2}$ system, several dumbbell-shaped orbitals appear at different Mo sites surrounding the Cd impurity, which indicates a bipolaron effect. These results suggest that the hopping of hole charge carriers increases due to the missing O2 atoms and they become trapped at the neighboring cation sites.

## ACKNOWLEDGMENTS

This work was funded by the FCT Grants No. PTDC/CTM-CTM/3553/2020 and No. CERN/FIS-TEC/0003/2019, and the Federal Ministry of Education and Research (BMBF) through Grants No. 05K16PGA and No. 05K22PGA and by Banco Santander-UCM through Project No. PR87/19-22613. We acknowledge the financial support received from the European Union's Horizon 2020 Framework research and innovation program under Grants No. 654002 (ENSAR2) and No. 101057511 (EURO-LABS) and from the project of "vdW4device" with the code of POCI-01-0145-FEDER-032527. E.L.d.S. acknowledges the Network of Extreme Conditions Laboratories (NECL), financed by FCT and co-financed by NORTE 2020, through the programme Portugal 2020 and FEDER; and also the High Performance Computing Chair, a R/D infrastructure (based at the University of Évora; PI: M. Avillez), endorsed by Hewlett Packard Enterprise (HPE), and involving a consortium of higher education institutions, research centers, enterprises, and public and private organizations. The authors acknowledge the cluster resources provided by CERN (HTC) and Univ. Évora-Oblivion for performing the calculations.

A.M.G. and E.L.d.S. performed the ab initio calculations. J.S., M.S.C., C.S.C., J.G.M., J.J.P., D.R.P., C.D.G., A.W.C., K.L., and J.G.C. have contributed to the PAC experiments, analysis of PAC spectra, and discussion of the obtained results. J.S., A.W.C., K.L., and J.G.C. supervised the project. A.M.G., J.S., E.L.d.S., M.S.C., C.S.C., J.G.M., J.J.P., D.R.P., C.D.G., A.W.C., K.L., and J.G.C. have contributed equally to the discussion and writing of the paper. All authors have read and agreed to the published version of the manuscript.

[1] I. A. de Castro, R. S. Datta, J. Z. Ou, A. Castellanos-Gomez, S. Sriram, T. Daeneke, and K. Kalantar-zadeh, Molybdenum oxides - from fundamentals to functionality, *Adv. Mater.* 29, 1701619 (2017).

[2] G. Hu, Q. Ou, G. Si, Y. Wu, J. Wu, Z. Dai, A. Krasnok, Y. Mazor, Q. Zhang, Q. Bao, C.-W. Qiu, and A. Alù, Topological polaritons and photonic magic angles in twisted $\alpha$-MoO$_3$ bilayers, *Nature (London)* 582, 209 (2020).

[3] L. Wang, M.-C. Li, G.-H. Zhang, and Z.-L. Xue, Morphology evolution and quantitative analysis of $\beta$-MoO$_3$ and $\alpha$-MoO$_3$, *High Temp. Mater. Process.* 39, 620 (2020).

[4] H. Sun, H. Zhang, X. Jing, J. Hu, K. Shen, Z. Liang, J. Hu, Q. Tian, M. Luo, Z. Zhu, Z. Jiang, H. Huang, and F. Song, One-step synthesis of centimeter-size $\alpha$-MoO$_3$ with single crystallinity, *Appl. Surf. Sci.* 476, 789 (2019).

033603-13

[5] D. R. Pereira, C. Díaz-Guerra, M. Peres, S. Magalhães, J. G. Correia, J. G. Marques, A. G. Silva, E. Alves, and K. Lorenz, Engineering strain and conductivity of $MoO_3$ by ion implantation, Acta Mater. 169, 15 (2019).

[6] D. O. Scanlon, G. W. Watson, D. J. Payne, G. R. Atkinson, R. G. Egdell, and D. S. L. Law, Theoretical and experimental study of the electronic structures of $MoO_3$ and $MoO_2$, J. Phys. Chem. C 114, 4636 (2010).

[7] C. Girotto, E. Voroshazi, D. Cheyns, P. Heremans, and B. P. Rand, Solution-processed $MoO_3$ thin films as a hole-injection layer for organic solar cells, ACS Appl. Mater. Interfaces 3, 3244 (2011).

[8] M. Labanowska, EPR monitoring of redox processes in transition metal oxide catalysts, ChemPhysChem 2, 712 (2001).

[9] E. Comini, L. Yubao, Y. Brando, and G. Sberveglieri, Gas sensing properties of $MoO_3$ nanorods to $CO$ and $CH_3OH$, Chem. Phys. Lett. 407, 368 (2005).

[10] S. Bai, C. Chen, D. Zhang, R. Luo, D. Li, A. Chen, and C.-C. Liu, Intrinsic characteristic and mechanism in enhancing $H_2S$ sensing of Cd-doped $\alpha$-$MoO_3$ nanobelts, Sens. Actuators B: Chem. 204, 754 (2014).

[11] J. Zhou, N.-S. Xu, S.-Z. Deng, J. Chen, J.-C. She, and Z.-L. Wang, Large-area nano wire arrays of molybdenum and molybdenum oxides: Synthesis and field emission properties, Adv. Mater. 15, 1835 (2003).

[12] X. Hu, W. Zhang, X. Liu, Y. Mei, and Y. Huang, Nanostructured Mo-based electrode materials for electrochemical energy storage, Chem. Soc. Rev. 44, 2376 (2015).

[13] J. N. Yao, K. Hashimoto, and A. Fujishima, Photochromism induced in an electrolytically pretreated $MoO_3$ thin film by visible light, Nature (London) 355, 624 (1992).

[14] Q. Zheng, J. Huang, S. Cao, and H. Gao, A flexible ultraviolet photodetector based on single crystalline $MoO_3$ nanosheets, J. Mater. Chem. C 3, 7469 (2015).

[15] E. D. Hanson, L. Lajaunie, S. Hao, B. D. Myers, F. Shi, A. A. Murthy, C. Wolverton, R. Arenal, and V. P. Dravid, Systematic study of oxygen vacancy tunable transport properties of few-layer $MoO_{3-x}$ enabled by vapor-based synthesis, Adv. Funct. Mater. 27, 1605380 (2017).

[16] M. Dieterle, G. Weinberg, and G. Mestl, Raman spectroscopy of molybdenum oxides part I. Structural characterization of oxygen defects in $MoO_{3-x}$ by DR UV/VIS, Raman spectroscopy and X-ray diffraction, Phys. Chem. Chem. Phys. 4, 812 (2002).

[17] G. Mestl, N. F. D. Verbruggen, and H. Knoezinger, Mechanically activated $MoO_3$. 2. Characterization of defect structures, Langmuir 11, 3035 (1995).

[18] M. Anwar and C. A. Hogarth, The optical absorption edge in amorphous thin films of $MoO_3$-$In_2O_3$, J. Mater. Sci. 24, 3673 (1989).

[19] H. A. Tahini, X. Tan, S. N. Lou, J. Scott, R. Amal, Y. H. Ng, and S. C. Smith, Mobile polaronic states in $\alpha$-$MoO_3$: An ab initio investigation of the role of oxygen vacancies and alkali ions, ACS Appl. Mater. Interfaces 8, 10911 (2016).

[20] M. T. Greiner, L. Chai, M. G. Helander, W.-M. Tang, and Z.-H. Lu, Transition metal oxide work functions: The influence of cation oxidation state and oxygen vacancies, Adv. Funct. Mater. 22, 4557 (2012).

[21] M. Shetty, K. Murugappan, T. Prasomsri, W. H. Green, and Y. Roman-Leshkov, Reactivity and stability investigation of supported molybdenum oxide catalysts for the hydrodeoxygenation (HDO) of m-cresol, J. Catal. 331, 86 (2015).

[22] P.-R. Huang, Y. He, C. Cao, and Z.-H. Lu, Impact of lattice distortion and electron doping on $\alpha$-$MoO_3$ electronic structure, Sci. Rep. 4, 7131 (2014).

[23] B. S. Dandogbessi, and A.-O. Omololu, First principles prediction of the electronic structure and carrier mobilities of biaxially strained molybdenum trioxide $(MoO_3)$, J. Appl. Phys. 120, 055105 (2016).

[24] N. Tokmoldin, N. Griffiths, D. D. C. Bradley, and S. A. Haque, A hybrid inorganic–organic semiconductor light-emitting diode using $ZrO_2$ as an electron-injection layer, Adv. Mater. 21, 3475 (2009).

[25] X. Hu, L. Chen, and Y. Chen, Universal and versatile $MoO_3$-based hole transport layers for efficient and stable polymer solar cells, J. Phys. Chem. C 118, 9930 (2014).

[26] H.-Y. Chen, H.-C. Su, C.-H. Chen, K.-L. Liu, C.-M. Tsai, S.-J. Yen, and T.-R. Yew, Indium-doped molybdenum oxide as a new p-type transparent conductive oxide, J. Mater. Chem. 21, 5745 (2011).

[27] S. Yang, G. Lei, L. Tan, H. Xu, J. Xiong, Z. Wang, and H. Gu, Fe-doped $MoO_3$ nanoribbons for high-performance hydrogen sensor at room temperature, J. Alloys Compd. 877, 160200 (2021).

[28] J. Schell, D. Zyabkin, K. Bharuth-Ram, J. N. Gonçalves, C. Díaz-Guerra, H. P. Gunnlaugsson, A. T. Martín-Luengo, P. Schaaf, A. Bonanni, H. Masenda, T. T. Dang, T. E. Mølholt, S. Ólafsson, I. Unzueta, R. Mantovan, K. Johnston, H. P. Gíslason, P. B. Krastev, D. Naidoo, and B. Qi, Anisotropy of the electric field gradient in two-dimensional $\alpha$-$MoO_3$ investigated by $^{57}$Mn ($^{57}$Fe) emission Mössbauer spectroscopy, Crystals 12, 942 (2022).

[29] L. X. Song, J. Xia, Z. Dang, J. Yang, L. B. Wang, and J. Chen, Formation, structure, and physical properties of a series of $\alpha$-$MoO_3$ nanocrystals: From 3D to 1D and 2D, CrystEngComm 14, 2675 (2012).

[30] M. Vila, C. Díaz-Guerra, D. Jerez, K. Lorenz, J. Piqueras, and E. Alves, Intense luminescence emission from rare-earth-doped $\alpha$-$MoO_3$ nanoplates and lamellar crystals for optoelectronic applications, J. Phys. D: Appl. Phys. 47, 355105 (2014).

[31] H.-Q. Wang, T. Stubhan, A. Osvet, I. Litzov, and C. J. Brabec, Up-conversion semiconducting $MoO_3$: Yb/Er nanocomposites as buffer layer in organic solar cells, Sol. Energy Mater. Sol. Cells 105, 196 (2012).

[32] Th. Wichert, in Hyperfine Interaction of Defects in Semiconductors, edited by G. Langouche, Hyperfine Interaction of Defects in Semiconductors (Elsevier, Amsterdam, 1992); G. Schatz, A. Weidinger:Nukleare Festkörperphysik (B. G. Teubner, Stuttgart, 1997).

[33] R. Dogra, A. P. Byrne, and M. C. Ridgway, The potential of the perturbed angular correlation technique in characterizing semiconductors, J. Electron. Mater. 38, 623 (2009).

[34] M. B. Barbosa, J. G. Correia, K. Lorenz, R. Vianden, and J. P. Araújo, Studying electronic properties in GaN without electrical contacts using $\gamma$-$\gamma$ vs e-$\gamma$ perturbed angular correlations, Sci. Rep. 9, 1 (2019).

[35] R. Catherall, W. Andreazza, M. Breitenfeldt, A. Dorsival, G. J. Focker, T. P. Gharsa, T. J. Giles, J. L. Grenard, F. Locci, P. Martins, S. Marxaril, J Schipper, A. Shornikov, and T. Stora,

The ISOLDE facility, J. Phys. G: Nucl. Part. Phys. 44, 094002 (2017).

[36] T. Butz, Analytic perturbation functions for static interactions in perturbed angular correlations of $\gamma$ rays, Hyperfine Interact. 52, 189 (1989).

[37] T. Butz, S. Saibene, Th. Fraenzke, and M. Weber, A "TDPACcamera'', Nucl. Instrum. Methods Phys. Res., Sect. A 284, 417 (1989).

[38] N. P. Barradas, M. Rots, A. A. Melo, and J. C. Soares, Magnetic anisotropy and temperature dependence of the hyperfine fields of $^{111}$Cd in single-crystalline cobalt, Phys. Rev. B 47, 8763 (1993).

[39] H. Haas, J. Röder, J. G. Correia, J. Schell, A. S. Fenta, R. Vianden, E. M. Larsen, P. A. Aggelund, R. Fromsejer, L. B. Hemmingsen, and S. P. Sauer, Free Molecule Studies by Perturbed $\gamma$- $\gamma$ Angular Correlation: A New Path to Accurate Nuclear Quadrupole Moments, Phys. Rev. Lett. 126, 103001 (2021).

[40] M. Deicher, Dynamics of defects in semiconductors, Hyperfine Interact. 79, 681 (1993).

[41] H. C. Zeng, Vapour phase growth of orthorhombic molybdenum trioxide crystals at normal pressure of purified air, J. Cryst. Growth 186, 393 (1998).

[42] B. Yan, Z. Zheng, J. Zhang, H. Gong, Z. Shen, W. Huang, and T. Yu, Orientation controllable growth of $MoO_3$ nanoflakes: Micro-Raman, field emission, and birefringence properties, J. Phys. Chem. C 113, 20259 (2009).

[43] G. Kresse and J. Furthmüller, Efficient iterative schemes for ab initio total-energy calculations using a plane-wave basis set, Phys. Rev. B 54, 11169 (1996).

[44] J. P. Perdew, K. Burke, and M. Ernzerhof, Generalized Gradient Approximation Made Simple, Phys. Rev. Lett. 77, 3865 (1996).

[45] A. I. Liechtenstein, V. I. Anisimov, and J. Zaanen, Densityfunctional theory and strong interactions: Orbital ordering in Mott-Hubbard insulators, Phys. Rev. B 52, R5467 (1995).

[46] H. Ding, H. Lin, B. Sadigh, F. Zhou, V. Ozolins, and M. Asta, Computational investigation of electron small polarons in $\alpha$-MoO$_3$, J. Phys. Chem. C 118, 15565 (2014).

[47] S. Grimme, J. Antony, S. Ehrlich, and H. Krieg, A consistent and accurate ab initio parametrization of density functional dispersion correction (DFT-D) for the 94 elements H-Pu, J. Chem. Phys. 132, 154104 (2010).

[48] S. Grimme, S. Ehrlich, and L. Goerigk, Effect of the damping function in dispersion corrected density functional theory, J. Comput. Chem. 32, 1456 (2011).

[49] H. J. Monkhorst and J. D. Pack, Special points for brillouinzone integrations, Phys. Rev. B 13, 5188 (1976).

[50] P. Blaha, K. Schwarz, F. Tran, R. Laskowski, G. K. H. Madsen, and L. D. Marks, WIEN2k: An APW+lo program for calculating the properties of solids, J. Chem. Phys. 152, 074101 (2020).

[51] H. Sitepu, B. H. O. Connor, and D. Li, Comparative evaluation of the march and generalized spherical harmonic preferred orientation models using X-ray diffraction data for molybdite and calcite powders, J. Appl. Crystallogr. 38, 158 (2005).

[52] M. Vila, C. Díaz-Guerra, K. Lorenz, J. Piqueras, I. Píš, E. Magnano, C. Munuera, E. Alves, and M. García-Hernández, Effects of thermal annealing on the structural and electronic properties of rare earth-implanted $MoO_3$ nanoplates, CrystEngComm 19, 2339 (2017).

[53] D. E. P. Vanpoucke, P. Bultinck, S. Cottenier, V. Van Speybroeck, and I. Van Driessche, Aliovalent doping of $CeO_2$: DFT study of oxidation state and vacancy effects, J. Mater. Chem. A 2, 13723 (2014).

[54] N. K. Nepal, S. Adhikari, B. Neupane, and A. Ruzsinszky, Formation energy puzzle in intermetallic alloys: Random phase approximation fails to predict accurate formation energies, Phys. Rev. B 102, 205121 (2020).

[55] V. Kulish, W. Liu, F. Benistant, and S. Manzhos, Dopantdopant interactions in beryllium doped indium gallium arsenide: An ab initio study, J. Mater. Res. 33, 401 (2018).

[56] X. Xu, H. Lai, Y. Xia, T. Luo, Y. Chen, S. Wang, K. Chen, X. Wang, T. Shi, W. Xie, and P. Liu, The electronic properties tuned by the synergy of polaron and d-orbital in a Co-Sn co-intercalated $\alpha$-MoO$_3$ system, J. Mater. Chem. C 8, 6536 (2020).

[57] H.-S. Kim, J. B. Cook, H. Lin, J. S. Ko, S. H. Tolbert, V. Ozolins, and B. Dunn, Oxygen vacancies enhance pseudocapacitive charge storage properties of $MoO_{3-x}$, Nat. Mater. 16, 454 (2017).

[58] B. S. Bokstein, M. I. Mendelev, and D. J. Srolovitz, Thermodynamics and Kinetics in Materials Science: A Short Course (Oxford University Press, Oxford, 2005).

[59] C. Franchini, M. Reticcioli, M. Setvin, and U. Diebold, Polarons in materials, Nat. Rev. Mater. 6, 560 (2021).

[60] H. Negishi, S. Negishi, Y. Kuroiwa, N. Sato, and S. Aoyagi, Anisotropic thermal expansion of layered $MoO_3$ crystals, Phys. Rev. B 69, 064111 (2004).

[61] H. Peelaers, M. L. Chabinyc, and C. G. Van de Walle, Controlling n-type doping in $MoO_3$, Chem. Mater. 29, 2563 (2017).

[62] M. Rellán-Piñeiro and N. Lopez, One oxygen vacancy, two charge states: Characterization of reduced $\alpha$-MoO$_3$ (010) through theoretical methods, J. Phys. Chem. Lett. 9, 2568 (2018).