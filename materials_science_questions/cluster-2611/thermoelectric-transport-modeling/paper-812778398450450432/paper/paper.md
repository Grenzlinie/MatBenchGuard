# Thermoelectric and vibrational properties of $Be_2C$, $BeMgC$ and $Mg_2C$ using first-principles method

V. Maurya, $^{a}$ U. Paliwal, $^{b}$ G. Sharma $^{c}$ and K. B. Joshi $^{*a}$

Transport coefficients are calculated combining first-principles calculations with the Boltzmann transport theory. Electronic states obtained in terms of the $k$-space eigen-energies from the crystalline orbital program, based on density functional theory, are Fourier transformed and interfaced with the transport equations modeled in the BoltzTraP. The calculations are performed for $Be_2C$, $Mg_2C$, and the BeMgC mixed crystal. The Seebeck coefficient, electronic thermal conductivity and the power factor are calculated. Further, the transport coefficients are linked to find the electronic fitness function to compare the performance with other thermoelectric materials. The procedure can also be applied to study the thermoelectric properties of other materials. The vibrational frequencies at the Brillouin zone centre are calculated generating a Hessian matrix from the analytical gradients of the energy with respect to atomic coordinates in the three antifluorite crystals. Moreover, the static, high frequency dielectric constants and Born effective charges are calculated to find splitting in the longitudinal optic and transverse optic modes. Results are compared with the data wherever available in the literature and a very good agreement is found in most cases.

## 1. Introduction
Clean energy is one of the central issues from scientific, economic and environmental points of view. Efforts have begun to look into sustainable and efficient sources of clean energy. $^{1-7}$ Thermoelectric (TE) and photo-voltaic devices in conjunction with renewable energy sources play a vital role in this strategic area such as thermoelectric generators and space exploration. $^{7,8}$ Like solar-energy conversion, the TE generators require enhanced energy efficiency and waste heat recovery from the exhaust. Reliable, silent or sustainable operations and small device size are the additional required features. $^{7,9}$ The challenges are to find materials having specific and tailored thermoelectric properties. $^{1-9}$ Combining quantum mechanical principles with computational power, it is possible to simulate and predict properties of materials. $^{4,7,10}$ Density functional theory (DFT) has been the backbone of such techniques over the last several decades. $^{11}$ Now it is also possible to calculate thermoelectric coefficients by coupling $k$-space eigen-energies from first-principles DFT methods with the Boltzmann transport equations (BTEs). $^{12,13}$ No such provision lies for each computational method used in general by the community of computational materials scientists. $^{14}$ These are highly needed because the performance of a TE material is quantified in terms of the figure of merit ($zT$), and the power factor (PF) which can be obtained theoretically vis-a-vis experimentally. Such an interface was published for the Linearized Augmented Plane Wave (LAPW) method recently. $^{15}$

In this endeavor we couple the $k$-space eigen-vectors and eigen-energies calculated from the first-principles periodic Linear Combination of Atomic Orbitals (LCAO) with the second principle model based on the BTE embodied in the BoltzTraP. $^{16-18}$ The periodic LCAO method is implemented in the CRYSTAL package. $^{16,17}$ A series of this crystalline orbital program in several versions has appeared in literature. In these, the non-cellular periodic LCAO method enables to use the Hartree-Fock or the DF theory to find the $E$-$k$ curve and several other properties of a crystal. The Hartree-Fock method treats the exchange part exactly and correlation part very poorly. The DFT treats both parts reasonably well but approximately. $^{16}$ The multi-valley structures of $E$-$k$ curves and the band gap of periodic solids largely depend on the theory applied and consequently the electronic and thermoelectric properties vary. $^{18}$ Recent trends are to use hybrid functionals to get accurate values of the band gap and bands dispersion which works well in some solids. $^{19-22}$ The hybrid functionals club merit of both approaches. Many methods use a number of hybrid functionals from the library of exchange and correlation (XC) functionals. On the contrary, one can devise a hybrid XC functional tuning percentage of mixing in the CRYSTAL98 and higher versions. $^{16,17}$ Effect on the band gap and bands dispersion can also be examined. Therefore an interface of the periodic LCAO method with the BoltzTraP will be highly useful to predict the transport coefficients from the $E$-$k$ dispersion

---
$^{a}$Department of Physics, Mohan Lal Sukhadia University, Udaipur-313001, India.
E-mail: cmsmlsu@gmail.com
$^{b}$Department of Physics, Jai Narain Vyas University, Jodhpur-342011, India
$^{c}$Department of Pure & Applied Physics, University of Kota, Kota-324005, India

spectra provided by the periodic LCAO method.¹⁶⁻¹⁸ This is the major objective of this paper.

Hitherto, oxides cover major section (~70%) of the explored TE materials. Half or full-Heusler compounds which owe spin-polarized band structure, skutterudites, clathrates and chalcogenides share major part of the residual section.²,⁴,⁷,²³⁻²⁵ Alkaline-earth metal methanides are technologically important carbides. The complex chemical synthetic process leads to either very low yield or very less stability.⁷,²⁶ The Be₂C, Mg₂C and Al₄C₃ are among a few known alkaline-earth methanides.²⁶⁻²⁹ Interestingly, Mg₂C is only recently synthesized²⁸,²⁹ whereas no ternary methanide is studied to our knowledge. The Be₂C, used in the ceramic and nuclear technology, has attracted quite a few theoretical as well as experimental studies.³⁰⁻³⁸ On Mg₂C, the band gap and the pressure coefficients are calculated employing local density approximation (LDA) in FP-LAPW method.³⁹,⁴⁰ Later it is synthesized and characterized by X-ray diffraction method.²⁸,²⁹ In our earlier work we have studied structural and bonding properties of Be₂C, Mg₂C and the hypothetical BeMgC deploying the periodic LCAO method.⁴¹,⁴² The thermal conductivity and band gap are proposed without specifying the carrier density or the chemical potential which is mandatory for practical purpose.⁴³,⁴⁴ Thus there are minimal efforts on the TE studies of carbides. So the second objective is to deploy the interface between periodic LCAO method and the BoltzTraP to find the thermoelectric coefficients of the Be₂C, Mg₂C and the BeMgC. Further, we compare the TE performance with other materials by means of the newly introduced electronic fitness function (EFF).⁴⁵

While modeling the properties of particularly the ceramics, nuclear and refractory materials, some limitations remain for practical applications due to change in properties at high temperatures. Vibrational properties and nature of bonding are elemental to the thermal behavior of crystals. Moreover, the vibration frequencies carry information regarding symmetry driven structural stability under different conditions.¹,⁴⁴,⁴⁷ The frequencies can be compared with the Infrared (IR) and Raman spectra. Essentially, the visible and infrared radiation used in conventional IR and Raman spectroscopies interact strongly with the phonon modes close to the Brillouin Zone (BZ) centre.¹,⁴⁶⁻⁴⁸ Therefore, meaningful information can also be obtained from frequencies at the $\Gamma$ point of the BZ in a crystal. Further, the Born effective charges (BEC) and the splitting in longitudinal optical (LO) and transverse optical (TO) modes provide additional features of the vibration spectra and dynamical behavior of crystals.¹⁶,¹⁷,⁴⁹ Thus it is imperative to improve upon the current understanding on the vibrational behavior of the three methanides. Therefore, the third objective of this work is to present the vibrational frequencies at the BZ centre, the BEC, static and high frequency dielectric constants and the LO-TO splitting of vibrational frequencies in Be₂C, Mg₂C and BeMgC.

Following is the plan of the remaining part of the paper: calculations procedures are described in the second section. Three parts of this section contains computational details, a brief description to compute the TE properties followed by the description on zone centre frequencies along with the LO-TO splitting. Results are presented in the third section. The four sub-sections cover discussion of results on electronic, thermoelectric, vibrational and the dielectric properties. Results are summarized in the last section.

## 2. Methods and computational details

### 2.1 Periodic LCAO method

The first-principles periodic LCAO method is applied.¹⁶,¹⁷,⁴⁹,⁵⁰ The salient features can be found in our earlier work.⁴¹ The Perdew-Burke-Ernzerhof (PBE) ansatz based on the generalized gradient approximation (GGA) is applied to treat the XC part of the Kohn-Sham Hamiltonian.⁵¹ The structure is optimized with an iterative method based on the total energy gradients calculated analytically with respect to the nuclear coordinates and numerically with respect to the lattice constants. The convergence is checked from the root-mean-square and absolute value of the largest component of the gradients and displacements. The thresholds (in a.u.) for the maximum and the root-mean-square forces were set to $4.5\times10^{-4}$, $3.0\times10^{-4}$ and those for displacements the thresholds were $1.8\times10^{-3}$, $1.2\times10^{-3}$ respectively. The complete optimization was ensured when the four conditions are simultaneously satisfied for the fractional coordinates and cell parameters. For exact treatment of the Coulomb and exchange terms of the total energy operator, computation of integrals over an infinite series is mandatory.¹⁶,¹⁷,⁴⁹,⁵⁰ To achieve it in practice, each infinite series needs to be truncated by setting threshold values of controlling parameters. These tolerance ($T$) parameters ensure that beyond cutoff limits the contribution to the total sum is smaller than $10^{-T}$ that can be neglected. In current calculations, five tolerances of the order of $10^{-7}$, $10^{-7}$, $10^{-7}$, $10^{-7}$ and $10^{-12}$ were undertaken to truncate Coulomb and exchange sum.¹⁷,⁴⁹,⁵⁰ The SCF process is stopped when two successive cycles differ in energy by less than $10^{-8}$ Hartree in geometry optimization and $10^{-12}$ Hartree in force calculations. The antifluorite structure belonging to the space group $Fm\overline{3}m$ (#225) is taken for the three carbides. The lattice parameters and bulk modulii deduced from the equation of state $E(V)$ are the same as described in our earlier work for this crystal structure of the three carbides.⁴¹

### 2.2 Transport properties

The figure of merit $zT$, expressed above, depends on the thermal conductivity ($\kappa$) which contains both electronic ($\kappa_{\text{e}}$) and lattice ($\kappa_{\text{l}}$) contributions. The electronic part ($\kappa_{\text{e}}$) is usually low in semiconductors. However, band gaps and bandwidth in the vicinity of Fermi level affect the electronic part associated with TE properties. It is well known that many XC functionals are being used by the community which show variation in the band gap of semiconductors. Usage of hybrid functional brings the band gap values close to the many body GW calculations which are believed to give accurate band gap in semiconductors.¹⁹⁻²¹ Better agreement of band gap from quasi particle or GW calculations with the hybrid functional and also with experiments, in some cases, is ascribed to the fact that hybrid functionals essentially augment LDA or GGA by non-local

exchange. $^{19-21}$ The underestimation of band gap by DFT has commonly been attributed to the inappropriate treatment of the XC functional $^{20-22,52}$ and the incomplete cancellation of the artificial self-interaction $^{20,52}$ within the LDA (local) or GGA (semi-local) descriptions. The hybrid functional, generally, combines the $\frac{1}{4}$ non-local exchange, $\frac{3}{4}$ of the semi-local exchange with the correlation functional. $^{16,17,20-22,50}$ The Kohn-Sham eigenvalues generated using such XC functionals are closer to those generated from many body perturbation theory. Here, therefore, we have also deduced band energies using a PBE0 hybrid functional. $^{20-22,52}$

Now it has become possible to unravel thermoelectric properties by combining first-principles methods with the BTE. $^{15,18,53}$ The requisite formulation to find tensors of transport coefficients from band energies, $\varepsilon_{i k}$ of the $i^{th}$ band at a $k$ point can be found elsewhere. $^{12,13,15,18}$ Two approximations are made to simplify the calculation procedure. Firstly, in the constant relaxation time approximation $\tau_{i, k}=\tau$ for all $i, k$ and secondly, in the rigid-band approximation we assume that the band structure does not vary with temperature or doping. The formulation gives the electrical conductivity tensor $\sigma$, thermal conductivity tensor $\kappa_{\mathrm{e}}$ and the Seebeck coefficient $S$. The temperature and chemical potential $(\mu)$ dependent tensors determine the number of charge carriers. $^{15,18,53}$ The thermoelectric quantities are obtained from the average of the diagonal components of the Seebeck and electrical conductivity tensors.

To compute these tensors, the band energies calculated from the converged electronic charge density using periodic LCAO method over a dense grid of $k$-points need to be linked with the BoltzTraP. To achieve this an interface is created. The interface arranges the $E$-$k$ spectrum from the LCAO method and writes into the case.energy file required for processing by the BoltzTraP to compute the transport coefficients. The interface also takes care of the units conversion of the energy and the $k$-vectors. Lattice vectors and symmetry related information of the crystal under investigation are given in the case.struct file. Thereafter another required file namely case.intrans is generated to completely fill the basket of files BoltzTraP.def. A flowchart of the entire process can be found in our recent work where a similar interface is created to link the energy spectrum from the LAPW method with the BoltzTraP. $^{15}$ In the current study the band energies are calculated over a dense grid size leading to $\sim 10$ 000 $k$-points in the irreducible BZ of the three crystals. The $k$-points were adequate to ensure convergence in Fourier expansion coefficients.

Performance of a TE material is quantified in terms of figure of merit $(z T)$ defined as $z T=(S \sigma T) / \kappa$ where $S$ is the Seebeck coefficient, $\sigma$ is electrical conductivity, $\kappa$ is thermal conductivity, and $T$ is absolute temperature. The quantity $S^{2} \sigma$, known as the power factor (PF) is of profound interest to characterize TE materials theoretically as well as experimentally. An ideal TE should follow an electron-crystal phonon-glass model because high $z T$ requires a large $S$, high $\sigma$ and low $\kappa$. First two transport coefficients also ensure high PF. For metals and semiconductors, the Seebeck coefficient is given by: $^{54}$

$$
S=\frac{2 k_{\beta}{ }^{2}}{3 e \hbar^{2}} m_{\mathrm{DOS}}^{*} T\left(\frac{\pi}{3 n}\right)^{2 / 3}. \tag{1}
$$

So for high power at certain temperature, a material should have high effective mass and low carrier density, which in turn reduces $\sigma$. The effective mass comes from the complexity of the electronic band structure. The degree to which the band structure can be decoupled with the electrical conductivity and $S$ is quantified by means of the EFF. Otherwise these have counterpoising role in determining the figure of merit and the PF. The EFF (or the $t$ function) is defined as $^{45} t=(\sigma / \tau) S^{2}(N / V)^{2 / 3}$, where $\tau$ is the relaxation time, $\sigma / \tau$ and $S$ are directly obtained from band structure and the BTE, $(N / V)$ is the volumetric density of states directly proportional to the density of states effective mass $\left(m_{\mathrm{DOS}}^{*}\right)$ and the Fermi energy $\left(E_{\mathrm{F}}\right)$ as: $\left(\frac{N}{V}\right) \propto\left(m_{\mathrm{DOS}}^{*}\right)^{3 / 2} E_{\mathrm{F}}{ }^{1 / 2}$. The function captures the behaviour that quantifies the favourable thermoelectric performance that is useful to scrutinize on a scale. The unit of the $t$-function turns out to be $\frac{W^{5 / 3}}{K^{2}} \frac{m}{\sqrt[3]{S}}$.

### 2.3 Zone centre frequencies and dielectric tensors

In periodic systems the phonon frequencies at the $\Gamma$ point are calculated by diagonalizing the mass weighted Hessian matrix $(W_{ij})$ within the harmonic approximation as: $^{16,17,49,50,55-57}$

$$
W_{ij}^{k=0}=\sum_{G} \frac{H_{ij}^{0 G}}{\sqrt{M_{i} M_{j}}}, \tag{2}
$$

where $M_{i}$ and $M_{j}$ are the masses of the atoms associated with the $i^{th}$ and $j^{th}$ coordinates, respectively. Hessian $H_{ij}^{0 G}$ is the second derivative of the electronic and nuclear repulsive energy $E$ at $u=0$ with respect to displacement $u_{i}=x_{i}-x_{i}^{\prime}$ of atom $\mathrm{A}$ in the $0^{\text{th}}$ cell, and displacement $u_{j}=x_{j}-x_{j}^{\prime}$ of atom $\mathrm{B}$ in the $G^{\text{th}}$ cell from the equilibrium positions $x_{i}^{\prime}, x_{j}^{\prime}$:

$$
\sum_{G} H_{ij}^{0 G}=\sum_{G}\left[\frac{\partial^{2} E}{\partial u_{i}^{0} \partial u_{j}^{G}}\right]_{0}, i=1,....3N;j=1,....3N. \tag{3}
$$

The Hessian at $\mathbf{u}=0$ is calculated by the analytical evaluation of the first derivative $\Phi_{j}$ of $E$ with respect to the atomic displacements:

$$
\Phi_{j}=\sum_{G} v_{j}^{G}=\sum_{G}\left[\frac{\partial E}{\partial u_{j}^{G}}\right],\ j=1,.......,3N, \tag{4}
$$

and the numerical evaluation of the derivative $\left[\frac{\partial \Phi_{j}}{\partial u_{i}^{0}}\right]_{0}$. Since the displacement step considered here is $u_{i}=0.001$ Å, the corresponding change in energy is very small and therefore tight tolerance in the self-consistent-field cycles is taken.

The effect of dynamical charge due to macroscopic electric field associated with the coherent displacement of crystal nuclei can be included in the Hessian as a correction. $^{55-58}$ It takes care of the long range Coulomb interaction and results into LO-TO

splitting. The LO frequencies are obtained by the additional non-analytic term to the dynamical matrix (eqn (2)):

$$
W_{i j}^{k \rightarrow 0}=\frac{1}{\sqrt{M_{\alpha} M_{\beta}}} \frac{4 \pi}{\Omega} \frac{\left(\sum_{k} q_{k} Z_{\alpha, k i}^{*}\right)\left(\sum_{k^{\prime}} q_{k^{\prime}} Z_{\beta, k^{\prime} j}^{*}\right)}{\sum_{k k^{\prime}} q_{k} \varepsilon_{k k^{\prime}} q_{k^{\prime}}}, \quad(5)
$$

where $\Omega$ is the cell volume and $Z_{\alpha}^{*}$ is the BEC tensor of atom $\alpha$. The electronic dielectric tensor is evaluated using a finite field saw-tooth model $^{50}$ and the BEC tensor is obtained from the localised Wannier functions. $^{50,58}$ The ionic contribution deduced from frequency eigenvalues $\omega_{\mathrm{m}}$, eigenvector $V$ and Born tensor $Z$ are added in $\varepsilon^{\infty}$ to find the static dielectric tensor:

$$
\varepsilon_{i j}^{0}(\omega)=\varepsilon_{i j}{ }^{\infty}+\frac{4 \pi}{\Omega} \sum_{m} \frac{\overline{Z}_{m, i} \overline{Z}_{m, j}}{\omega_{m}{ }^{2}-\omega^{2}}, \quad(6)
$$

where $\bar{Z}_{m, i}=\sum_{\alpha, j} Z_{\alpha, i j}^{*} V_{(\alpha, i) j}, \omega$ is the electric field frequency, $\alpha$ labels the $\mathrm{N}$ atoms of the unit cell, and $i$ and $j$ indicate the three Cartesian components.

## 3. Results and discussion
### 3.1 Electronic states
The lattice constant and bulk modulus reported in our earlier publication are well reproduced from the total energy curves of the three crystals. $^{41}$ The bands dispersion curves delineating microscopic picture of electronic bands are described in Fig. 1. The bands structures show that each carbide has indirect band gap with the valence band maximum (VBM) at $\Gamma$ and the conduction band minimum (CBM) at $X$. The $\Gamma-X$ gaps, for $\mathrm{Be}_{2} \mathrm{C}$, BeMgC and $\mathrm{Mg}_{2} \mathrm{C}$, in order, are 2.90, 1.86 and 2.05 eV. Likewise $\Gamma-\Gamma$ direct gaps are 4.24, 4.21 and 3.53 eV. Similar calculations using PBE0 hybrid functional $^{21}$ suggest that $\Gamma-X$ gaps, sequentially for $\mathrm{Be}_{2} \mathrm{C}, \mathrm{BeMgC}$ and $\mathrm{Mg}_{2} \mathrm{C}$ are 4.37, 3.24 and 3.46 eV whereas the $\Gamma-\Gamma$ direct gaps are 5.77, 5.59 and 5.19 eV. Thus PBE0 gives larger band energies and band gaps than the PBE. Band gap measurement is attempted only for the $\mathrm{Be}_{2} \mathrm{C}$ and $\Gamma-X$ indirect band gap is reported. $^{38,40}$ The authors did not propose definite value but concluded that the band gap may be more than at least $1.3 \mathrm{eV} .^{37,38}$ Moreover, $\mathrm{X}_{1 \mathrm{v}}$ and $\mathrm{X}_{4 \mathrm{v}}^{\prime}$ bands observed at -11.5 and -6.7 eV from VBM in LEED, ARPES and NEXAFS experiments are found at -11.46 and -6.79 eV by PBE calculations. The PBE0 functional locates these bands at-12.87 eV and-7.71 eV. Thus energies of these states are very well produced by PBE-GGA in case of $\mathrm{Be}_{2} \mathrm{C}$. In case of $\mathrm{Mg}_{2} \mathrm{C}$ only a few calculations are available for comparison. The published calculations reveal that indirect (direct) band gap lies in the $0.67-0.97 \mathrm{eV}(1.34-1.9 \mathrm{eV})$ range. $^{28,40,43}$ So both PBE and PBE0 predict band gaps beyond the limits proposed by earlier workers. The LDA used by earlier workers may be the reason for this discrepancy. $^{52}$ In BeMgC, interestingly PBE0 calculation gives a value of $5.6( \pm 0.1) \mathrm{eV}$ for both $\Gamma-K$ and $\Gamma-\Gamma$ gaps. These two gaps are separated by 0.25 eV in the PBE bands structure. Current results follow the trends of compounds with identical crystal structure wherein the band gap is found more in the compound with lighter elements. $^{59}$

It is known that DOS gives the number of electronic states integrated over $k$-space in a finite energy interval. The curves showing electronic DOS are displayed on the right hand panels of Fig. 1. The occupied DOS can be divided into two parts. In first part, the occupied valence band below -10 eV is largely constituted by the C-2s state present in the three carbides. In the second part, the upper valence bands extend from -9.5 to

![](./images/812778398450450432_1.jpg)

Fig. 1 Band structures and the DOS of three carbides using the PBE functional.

0 eV approaching to the Fermi level. The interacting cationic (Be and or Mg) 2s2p and C-2p states constitute states in this region. Additionally, the cationic 2p states interact in bonding and anti- bonding modes with C-2p state to form remaining valence bands as well as a few conduction bands in the vicinity of Fermi energy. There is a minor contribution of outer cation s states also. Difference in the DOS of three carbides can be marked by appearance of peaks. The peaks like structures are absent in Be₂C and clearly visible in the other two compounds. These bands have typical character of C-2p states and play major role in the thermoelectric properties. Both DOS and dispersion curves reveal that the lowest valence band of Be₂C is very deep having the largest width and least number of states. On the contrary, in Mg₂C corresponding band has the shortest width and maximum number of states. This is a manifestation of flat bands in Mg₂C. The flat bands are normally seen in materials with ionic character. So, the DOS of BeMgC indicate mixed ionic and covalent character.

### 3.2 Thermoelectric properties
As discussed before, experimental studies of band energies and gaps are reported only for Be₂C and the characteristic energies from PBE are in very good agreement compared to the PBE0 hybrid functional. Also, in a study on SrRuO₃ several XC func- tionals were applied to compute the TE properties and PBE was found to be the most suitable.⁶⁰ Therefore, we use the PBE eigen-energies at k points to compute the TE properties. Also these properties are studied under the constant relaxation time approximation wherein $\tau$ is a constant, and the band structure is independent of both temperature and doping. The relaxation time can be estimated from the experimental electrical conductivity $\sigma$ at given carrier density and temperature. In case of Be₂C, such a specified value of electrical conductivity is not available. So we have compared the optimum value of $\sigma/\tau$ deduced directly from the BTE with the reciprocal of the experimental resistivity $\rho=10^{3}\ \mu\Omega$ cm (ref. 61) at 300 K which gives $\tau = 4\times10^{-14}$ s. In absence of such a data for three carbides, we take this as a representative value of relaxation time. On the availability of exact value of $\tau$ the transport coef- ficients can be readily calculated. Dependence of S and PF with chemical potential $(\mu)$ is displayed in Fig. 2-4. At four temper- atures such a dependence for Be₂C is shown in Fig. 2(a). Specific structures appear in S. It shows that by appropriate doping the Seebeck coefficient of the order of $\sim 2.74-1.54\times10^{-3}\ \text{V}\ \text{K}^{-1}$ can be achieved. As the range of chemical potential over which this structure is visible expands with increase in temperature, the attainable doping level to achieve calculated S increases. One can see in Fig. 2(b) that optimum PF is $\cong 1.36\times10^{-3}\ \text{W}\ \text{mK}^{-2}$ at 100 K and rises to $26.42\times10^{-3}\ \text{W}\ \text{mK}^{-2}$ at 800 K where $S\cong 2.73\times10^{-3}\ \text{V}\ \text{K}^{-1}$.

For Mg₂C, variation of S and PF with chemical potential is shown in Fig. 3. It depicts that optimum values of S and PF are $2.94\times10^{-3}\ \text{V}\ \text{K}^{-1}$ and $17.10\times10^{-3}\ \text{W}\ \text{mK}^{-2}$ at 300 K. Corre- sponding values at 800 K are $1.344\times10^{-3}\ \text{V}\ \text{K}^{-1}$ and $58.20\times10^{-3}\ \text{W}\ \text{mK}^{-2}$. Similarly, at 300 K the S and PF of BeMgC are $2.91\times10^{-3}\ \text{V}\ \text{K}^{-1}$ and $9.88\times10^{-3}\ \text{W}\ \text{mK}^{-2}$. The S and PF lie in between the corresponding values of Be₂C and Mg₂C. It is well expected as bands dispersion and DOS in BeMgC is interme- diate to those in Be₂C and Mg₂C. The microscopic variation in the curvature of bands determines the velocity and effective mass tensor and consequently trend with respect to chemical potential is somewhat different in BeMgC than in Mg₂C visible in Fig. 3(b) and 4(b). In mixed compounds mass and concen- tration dependence affect thermal properties and the effect of mutual interaction of the sub lattices (Be and Mg in this case) on thermal properties is not well understood.⁶

Effect of the electronic states exhibited through DOS can be clearly seen in the $S^{2}\sigma$ plotted in Fig. 2-4. Widths of the valence bands in the vicinity of Fermi level are 8.75, 4.844 and 6 eV respectively for the Be₂C, Mg₂C and BeMgC from the PBE calculations. Likewise width of the first conduction band is 4.36, 3.87 and 4.949 eV. The PF is more in Mg₂C wherein bands are relatively flat that is normally found in compounds with prevalent ionic character. The Mulliken population analysis also pointed such ionic behaviour in Mg₂C.²⁰,³⁵ Carriers in heavy

![](./images/812778398450450432_2.jpg)

Fig. 2 Variation of (a) Seebeck coefficient and (b) power factor of Be₂C with chemical potential at $\tau=4\times10^{-14}$ s.

![](./images/812778398450450432_3.jpg)

Fig. 3 Variation of (a) Seebeck coefficient and (b) power factor of $Mg_2C$ with chemical potential at $\tau = 4 \times 10^{-14}$ s.

![](./images/812778398450450432_4.jpg)

Fig. 4 Variation of (a) Seebeck coefficient and (b) power factor of BeMgC with chemical potential at $\tau = 4 \times 10^{-14}$ s.

band (flat band structure) have low velocity and large effective mass so Seebeck coefficient is somewhat higher in $Mg_2C$. The overall effect is the maximum PF of $Mg_2C$ among the three carbides. The dependence of PF on $\mu$ is shown in Fig. 2(b)-4(b) reveal that PF depends strongly on the sign of chemical potential. The curves signify better performance of three carbides with p-type doping. The asymmetry with respect to sign is lowest in the $Be_2C$ and maximum in $Mg_2C$. The asymmetry is sufficiently large in $Mg_2C$ and BeMgC to propose p-type majority carriers. So both $Mg_2C$ and the BeMgC could, in principle, make a good TE unlike $Be_2C$.

In Fig. 5-7, we plot temperature and concentration dependence of $S$ and PF. The optimum values of the $S$ and PF are maximum for $Mg_2C$ followed by BeMgC and the $Be_2C$. In the figures both coefficients increase with temperature. The value of $S$ is comparable to the experimental values $147\ \mu V\ K^{-1}$ in $SrTiO_3$ which has band gap $3.25$ eV.⁶² The difference in the relaxation time and band gap may cause the residual deviation.⁶⁰,⁶²

In the three cases the maximum PF is well around the experimentally realizable high doping (up to $10^{20}\ cm^{-3}$).⁴,⁷,⁵⁴ The values of PF at three temperatures are listed in Table 1. We see that at a given temperature PF is maximum in $Mg_2C$ that increases with temperature. Though hole concentration corresponding to the maximum PF is higher in $Mg_2C$ ($\sim 7 \times 10^{20}\ cm^{-3}$) it is well within the achievable experimental limits. To predict the values of TE quantities, we need to consider the variation resulting from the relaxation time. We have taken $\tau = 4 \times 10^{-14}$ s in all calculations reported above. However, in the case of $Mg_2C$ thermal conductivity $\sim 34\ W\ mK^{-1}$ is reported at 300 K using plane wave pseudopotential (PP) method.⁴³,⁴⁴ The comparison with the optimum value obtained in the current calculations give $\tau = 4.4 \times 10^{-15}$ s.⁴³ It alters the relaxation time by a factor of $\sim 10^{-1}$. Therefore we calculated optimum values of PF and $\kappa_e$ also at $\tau = 4.4 \times 10^{-15}$ s, and give in Table 1. It furnishes the range of transport coefficients. Reviews on the basis of high-throughput calculations suggest that PF more than $3 \times 10^{-3}\ W\ mK^{-2}$ at experimentally realizable doping are

![](./images/812778398450450432_5.jpg)

Fig. 5 Variation of (a) S and (b) PF of $Be_2C$ with p-type doping when $\tau = 4 \times 10^{-14}$ s.

![](./images/812778398450450432_6.jpg)

Fig. 6 Variation of (a) S and (b) PF of $Mg_2C$ with p-type doping when $\tau = 4 \times 10^{-14}$ s.

promising for the next generation thermoelectrics and less than $1 \times 10^{-3}$ W mK$^{-2}$ are of little use. $^{4,7}$ In a few theoretical vis-a-vis experimental studies it is observed that calculations usually underestimate the PF. $^{60,62}$ In view of these, we may infer that the values of PF will be more than those listed in Table 1. The predicted PF of $Mg_2C$ is better than the values suggested for TE materials on the basis of data mining techniques covering many thousand compounds. $^{4,5,7,45}$ BeMgC may also be tried at higher temperatures once it is synthesized in the laboratory.

In Table 1, optimum values of the electrical and thermal conductivity of the three carbides are also listed. At the three temperatures $\sigma$ is almost same for the three carbides. It is maximum for $Be_2C$ and $\sim$2.6 times the conductivity of $Mg_2C$. Note that these optimum values occur at different levels of carrier concentration. The electronic thermal conductivity also follow nearly the similar trend. In the three compounds $\kappa_e$ is negligibly small below $10^{21}$ cm$^{-3}$ and rises thereafter. Therefore the reported values are found at $\sim$$10^{23}$ cm$^{-3}$. In case of BeMgC both coefficients are in between the $Be_2C$ and $Mg_2C$.

In a recent work on a quaternary mixed compound, the figure of merit $(zT)$ is interpreted in terms of generalized material parameter which connects the thermal conductivity, band gap and the newly defined weighted mobility. $^{6}$ It is proposed that for a good thermoelectric the weighted mobility and the band gap should be high and the $zT$ is proportional to the band gap. It is also mentioned that the materials with wide band gap have modest theoretical PF. $^{6}$ Though the carbides containing magnesium have band gap $\sim$2 eV, the PF is good as discussed before. It may be a consequence of the larger effective mass resulting from the non parabolic bands in eqn (1) which facilitate enhanced thermoelectric performance. $^{63}$ To examine it further, measurement of transport coefficients shall be fruitful.

As discussed earlier, the transport function EFF i.e. $t$ measures the extent to which a complex band structure decouples $\sigma$ and $S$. It is proposed to find and screen materials that overcome reciprocal behaviour of $\sigma$ and $S$ in achieving a good thermoelectric behaviour. In order to compare the performance of the three carbides with the promising TE materials we have calculated the EFF i.e. $t$-function introduced

![](./images/812778398450450432_7.jpg)

Fig. 7 Variation of (a) S and (b) PF of BeMgC with p-type doping when $\tau = 4 \times 10^{-14}$ s.

<table>
<caption>Table 1 Calculated PF, $\sigma$ and $\kappa_{\mathrm{e}}$ at the optimum carrier density and two relaxation times ($\tau$)</caption>
<thead>
<tr>
<th rowspan="2">Temp (K)</th>
<th rowspan="2">Transport coefficients</th>
<th colspan="2">$\mathrm{Be_{2}C}$</th>
<th colspan="2">$\mathrm{BeMgC}$</th>
<th colspan="2">$\mathrm{Mg_{2}C}$</th>
</tr>
<tr>
<th>$4 \times 10^{-14}$ s</th>
<th>$4.4 \times 10^{-15}$ s</th>
<th>$4 \times 10^{-14}$ s</th>
<th>$4.4 \times 10^{-15}$ s</th>
<th>$4 \times 10^{-14}$ s</th>
<th>$4.4 \times 10^{-15}$ s</th>
</tr>
</thead>
<tbody>
<tr>
<td>300</td>
<td>$\mathrm{PF(10^{-3}\ W\ mK^{-2})}$</td>
<td>6.78</td>
<td>0.75</td>
<td>9.88</td>
<td>1.09</td>
<td>17.10</td>
<td>1.93</td>
</tr>
<tr>
<td></td>
<td>$\kappa_{\mathrm{e}}\ (\mathrm{W\ mK^{-1}})$</td>
<td>628</td>
<td>68</td>
<td>334</td>
<td>38.4</td>
<td>244</td>
<td>27.00</td>
</tr>
<tr>
<td></td>
<td>$\sigma\ (10^{6}\ \mathrm{S\ m^{-1}})$</td>
<td>86.7</td>
<td>9.5</td>
<td>47</td>
<td>5.2</td>
<td>33</td>
<td>3.7</td>
</tr>
<tr>
<td>500</td>
<td>$\mathrm{PF(10^{-3}\ W\ mK^{-2})}$</td>
<td>13.93</td>
<td>1.52</td>
<td>19.40</td>
<td>2.13</td>
<td>31.00</td>
<td>3.43</td>
</tr>
<tr>
<td></td>
<td>$\kappa_{\mathrm{e}}\ (\mathrm{W\ mK^{-1}})$</td>
<td>1043</td>
<td>116</td>
<td>578.9</td>
<td>63.94</td>
<td>409</td>
<td>45.00</td>
</tr>
<tr>
<td></td>
<td>$\sigma\ (10^{6}\ \mathrm{S\ m^{-1}})$</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>800</td>
<td>$\mathrm{PF(10^{-3}\ W\ mK^{-2})}$</td>
<td>26.33</td>
<td>2.88</td>
<td>35.94</td>
<td>3.96</td>
<td>58.20</td>
<td>6.47</td>
</tr>
<tr>
<td></td>
<td>$\kappa_{\mathrm{e}}\ (\mathrm{W\ mK^{-1}})$</td>
<td>1678</td>
<td>186</td>
<td>922.2</td>
<td>101.18</td>
<td>655</td>
<td>71</td>
</tr>
</tbody>
</table>

recently.⁴⁵ The EFF for three crystals are plotted in Fig. 8. The function gradually decreases and becomes negligible beyond $10^{22}\ \mathrm{cm}^{-3}$. At higher temperature the EFF is more. According to the screening criteria, the p-type materials having EFF more than that of FeNbSb ($0.75 \times 10^{12}\ \mathrm{W}^{5/2}\ \mathrm{ms}^{-1/3}\ \mathrm{K}^{-2}$ at 300 K and $2.10 \times 10^{12}\ \mathrm{W}^{5/2}\ \mathrm{ms}^{-1/3}\ \mathrm{K}^{-2}$ at 800 K, shown by horizontal lines in Fig. 8) are useful in TE applications.⁴⁵ The optimum value of PF for this reference compound lies in the 4.3 to $5.5 \times 10^{-3}\ \mathrm{W}\ \mathrm{mK}^{-2}$ range at 800 K. The $\mathrm{Mg_{2}C}$ has the PF in this range and the EFF is more than FeNbSb up to a certain carrier concentration. Thus $\mathrm{Mg_{2}C}$ fits into this criterion. Moreover, it turns out to be a better TE compared to the similar p-type compound $\mathrm{Mg_{2}Ge}$ ($t = 0.85$). The $\mathrm{Mg_{2}Si}$ ($t = 1.18$) is albeit better than the $\mathrm{Mg_{2}C}$.⁴⁵ The EFF of $\mathrm{Be_{2}C}$ also satisfies the screening criterion but the PF is somewhat lower and other type of carriers will also have some contribution which does not help to make it a good thermoelectric.

### 3.3 Vibrational frequencies and LO-TO splitting

The IR and Raman frequencies are calculated at the zone centre i.e. at $\Gamma$-point of the BZ. The classified active modes and corresponding frequencies are listed in Table 2. For the antifluorite crystals the group theory suggests either g or u type modes. The $\mathrm{Be_{2}C}$ and $\mathrm{Mg_{2}C}$ contain six optical modes at the $\Gamma$ point. The irreducible presentation for the two crystals is:

$$
\Gamma = 3\mathrm{F_{2g}} \oplus 6\mathrm{F_{1u}}. \tag{7}
$$

The g and u indicate symmetric and anti symmetric normal modes. $\mathrm{F_{1u}}$ arises from the Cation-C(apical) whereas $\mathrm{F_{1g}}$ arises from the C(central)-C(apical) vibrations. In $\mathrm{Be_{2}C}$, excluding the three translational acoustic modes belonging to the $\mathrm{F_{1u}}$ representation, there are 3 Raman active ($3\mathrm{F_{2g}}$) and 3 IR active ($3\mathrm{F_{1u}}$) optic modes. The Raman active modes vibrate at $722.41\ \mathrm{cm}^{-1}$ and IR active modes at $632.48\ \mathrm{cm}^{-1}$. In the long wavelength limit, optical phonons couple to the macroscopic electric fields in ionic crystals. It manifests in the difference in the frequency of LO and TO at the $\Gamma$-point and shows the LO-TO split. In $\mathrm{Be_{2}C}$, the LO, TO modes do not overlap and the anti-symmetric IR optical mode exhibits an LO-TO split of $333.34\ \mathrm{cm}^{-1}$.

In $\mathrm{Mg_{2}C}$, the three Raman active modes vibrate at $389.18\ \mathrm{cm}^{-1}$ while IR active modes vibrate at $421.78\ \mathrm{cm}^{-1}$. These are in very good agreement with $387.76\ \mathrm{cm}^{-1}$, $437.79\ \mathrm{cm}^{-1}$ reported by PP method²⁸ and $387\ \mathrm{cm}^{-1}$, $428\ \mathrm{cm}^{-1}$ reported by Quantum Espresso using norm-conserving PP method.⁶⁴ Calculations using LDA in the PAW method found these modes at 406.26 and $559.44\ \mathrm{cm}^{-1}$.⁴³ So each calculation,

![](./images/812778398450450432_8.jpg)

Fig. 8 Concentration and temperature dependence of the EFF (the t-function) for (a) $Be_2C$, (b) $Mg_2C$ and (c) BeMgC. The horizontal lines mark that materials having EFF above these lines at 300 and 800 K are very good thermoelectric.

except the one using PAW, gives nearly similar frequencies. It is observed that $Mg_2C$ is synthesized at 15 GPa and fully recoverable under ambient conditions. In view of this it is remarkable to see absence of negative zone centre frequencies in $Mg_2C$ calculations. The BeMgC mixed crystal shows the $\Gamma=9F$ irreducible representation with reduced symmetry and 9 modes. The first three IR and Raman active acoustic modes have zero frequencies. There are two sets of optic modes. In each set, the three TO modes have 519.83 $cm^{-1}$ and 565.59 $cm^{-1}$ frequencies. Both these sets are IR and Raman active and show mixing of the TO and LO modes. Although absence of imaginary frequencies alone does not ascertain stability of crystals, the non-appearance in BeMgC increases the chances of BeMgC synthesis in laboratory.

The vibrational frequencies and the active modes change with atoms and symmetry. The optical modes are sensitive to the inter-cellular interaction and therefore generalized trend $\langle(\omega_L)^2\rangle\rangle(\omega_T)^2$ is usually seen in the vibration spectra of the three materials. Unlike pure methanides, BeMgC shows mixing of the LO-TO modes. The replacement of Be by Mg reduces symmetry and the interaction between Be-Mg cations leads to the lowering of the LO frequency by 17.7 $cm^{-1}$ from the TO mode of 565.59 $cm^{-1}$ frequency. In fact, one of active Raman mode arises from the vibration of cations. The Be-Be bond length ($d_{Be-Be}$ $\cong a/2$) and mass is lower than the Mg-Mg so the frequency is larger in $Be_2C$. In BeMgC, both inter-cellular environment and appearance of Be-Mg bonds alter the frequencies of vibration. Further, electro-negativity of Be and Mg leads to asymmetry in polarization which causes mixing of the LO, TO modes in BeMgC.

### 3.4 Born effective charges and dielectric properties

Now we present the calculated BEC, high frequency $(\varepsilon^{\infty})$ and the static dielectric tensors $(\varepsilon^{0})$. BEC is the derivative of polarization with respect to atomic position at zero macroscopic electric field. Hence this and related quantities exhibit dynamical properties of crystals and categorized mathematically as tensor. The BEC captures change in polarization with respect to atomic displacement. The three crystals show isotropic behaviour and the values are given in Table 3. Calculated BEC on two cations and carbon is about 20% lower than the formal charge $(+2|e|;-4|e|)$ in the two methanides. In BeMgC, the dynamical charges on the three atoms are less in comparison to the formal charge. We found the maximum reduction ($\sim$30%) on the beryllium. Further, we note that $Z_C^*=2Z_{Cation}^*$ and the sum rule $\sum_{\alpha}Z_{\alpha,ij}^*=0$ is very well followed. The BEC, dielectric constants and susceptibility reveal that the tendency of polarization under electric field is more in $Be_2C$ and less in the $Mg_2C$. It leads to a larger contribution of vibrational part (Column-VII) in the $\varepsilon^{0}$ (Column-V). The total contribution $(\varepsilon^{0})$ decreases in the $Be_2C >$ BeMgC $> Mg_2C$ order. The available values of $Mg_2C$ taking LDA in the PP method⁶⁴ are also given in Table 3. We note that our results well reconcile. A difference of $\sim$39% in the $\varepsilon^{\infty}$ is found. To check if this is due to the lattice constant, we calculated the dynamical tensors at the experimental lattice constant of $Mg_2C$. These numbers, within parenthesis, are given in a row of Table 3. Only a marginal reduction in difference ($\sim$38.5%) is observed. To check if this is due to the band gap we also calculated the dielectric constants and the refractive index using the empirical relations among band gap, high frequency dielectric constants and the refractive index proposed by Moss.⁶⁵ The deviations in the dielectric constant and refractive index $(n)$ from Moss formulation are about 13% and 7%. In case of the PP results deviation rises to 20% and 29%.

The Born effective charges and the LO-TO splitting are closely related. The more is the BEC the more is the LO-TO split. In Table 3, the isotropic BEC are listed. The non-zero value in each case signifies the LO-TO splitting. We note that the BEC is maximum on the constituent atoms in $Be_2C$ and the LO-TO split 333.34 $cm^{-1}$ is the largest. This and the acquiescence of the BEC sum rule exhibited by the three carbides ensure reliability of our calculations. In $Mg_2C$, the anti-symmetric mode

Table 2 Frequencies (in ${\rm cm}^{-1}$) calculated at the BZ centre together with the LO-TO split. In BeMgC the TO modes are both IR and Raman active and have $F$ symmetry. The values given in parenthesis are calculated at the experimental lattice constant

<table>
<thead>
<tr>
<th colspan="3"></th>
<th colspan="2">Mg₂C</th>
<th colspan="3"></th>
<th></th>
</tr>
<tr>
<th></th>
<th></th>
<th></th>
<th rowspan="2">Be₂C</th>
<th rowspan="2">This work</th>
<th colspan="3">Others work</th>
<th rowspan="2">BeMgC</th>
</tr>
<tr>
<th></th>
<th></th>
<th></th>
<th>PPᵃ</th>
<th>PAWᵇ</th>
<th>PPᶜ</th>
</tr>
</thead>
<tbody>
<tr>
<td>TO</td>
<td>IR</td>
<td>F₁ᵤ</td>
<td>632.52</td>
<td>421.78 (394.21)</td>
<td>437.79</td>
<td>406.26</td>
<td>428</td>
<td>519.83</td>
</tr>
<tr>
<td></td>
<td>Raman</td>
<td>F₂ᵍ</td>
<td>722.41</td>
<td>389.18 (374.12)</td>
<td>387.76</td>
<td>—</td>
<td>387</td>
<td>565.59</td>
</tr>
<tr>
<td>LO</td>
<td></td>
<td>F₁ᵤ</td>
<td>965.85</td>
<td>635.99 (613.41)</td>
<td>—</td>
<td>559.44</td>
<td>588</td>
<td>754.57</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>547.91</td>
</tr>
<tr>
<td>LO-TO</td>
<td></td>
<td>F₁ᵤ</td>
<td>333.33</td>
<td>214.21 (219.20)</td>
<td>—</td>
<td>153.18</td>
<td>160</td>
<td>234.74</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>−17.68</td>
</tr>
</tbody>
</table>

ᵃ Calibrated from the graphical data of ref. 28. ᵇ Ref. 43. ᶜ Ref. 64.

Table 3 Dynamical BEC ($Z_{\alpha}^{*}$), high frequency ($\varepsilon^{\infty}$) and static ($\varepsilon^{0}$) dielectric constants together with the contribution of the vibrational part ($\varepsilon^{\omega}$). The refractive index and susceptibility are also given. The values given in parenthesis for Mg₂C are calculated at the experimental lattice constant

<table>
<thead>
<tr>
<th rowspan="2"></th>
<th rowspan="2"></th>
<th rowspan="2"></th>
<th rowspan="2">Dynamical charge<br>$Z_{\alpha({\rm electrons})}^{*}$</th>
<th colspan="3">Isotropic dielectric tensor</th>
<th rowspan="2">$\chi$</th>
<th rowspan="2">$n$</th>
</tr>
<tr>
<th>$\varepsilon^{0}$</th>
<th>$\varepsilon^{\infty}$</th>
<th>$\varepsilon^{\omega}$</th>
</tr>
</thead>
<tbody>
<tr>
<td>Be₂C</td>
<td>This work</td>
<td>Be</td>
<td>1.605</td>
<td>15.124</td>
<td>6.486</td>
<td>8.638</td>
<td>5.4856</td>
<td>2.547</td>
</tr>
<tr>
<td></td>
<td></td>
<td>C</td>
<td>−3.210</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td>Mossᵇ</td>
<td>—</td>
<td>—</td>
<td>—</td>
<td>5.723</td>
<td>—</td>
<td>—</td>
<td>2.392</td>
</tr>
<tr>
<td>Mg₂C</td>
<td>This work</td>
<td>Mg</td>
<td>1.588 (1.599)</td>
<td>13.280 (14.211)</td>
<td>5.839 (5.869)</td>
<td>7.441 (8.342)</td>
<td>4.839 (4.869)</td>
<td>2.416 (2.423)</td>
</tr>
<tr>
<td></td>
<td></td>
<td>C</td>
<td>−3.175 (−3.197)</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td>PPᵃ</td>
<td>Mg</td>
<td>1.57</td>
<td>15.4</td>
<td>8.15</td>
<td>7.25</td>
<td>—</td>
<td>—</td>
</tr>
<tr>
<td></td>
<td></td>
<td>C</td>
<td>−3.14</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td>Mossᵇ</td>
<td>—</td>
<td>—</td>
<td>—</td>
<td>6.807</td>
<td>—</td>
<td>—</td>
<td>2.609</td>
</tr>
<tr>
<td>BeMgC</td>
<td>This work</td>
<td>Be</td>
<td>1.409</td>
<td>12.278</td>
<td>6.209</td>
<td>6.069</td>
<td>5.209</td>
<td>2.492</td>
</tr>
<tr>
<td></td>
<td></td>
<td>Mg</td>
<td>1.569</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td>C</td>
<td>−2.978</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td>Mossᵇ</td>
<td>—</td>
<td>—</td>
<td>—</td>
<td>7.147</td>
<td>—</td>
<td>—</td>
<td>2.673</td>
</tr>
</tbody>
</table>

ᵃ Ref. 64. ᵇ Ref. 65.

shows LO-TO splitting of $214.28\ {\rm cm}^{-1}$. This is more than the $153\ {\rm cm}^{-1}$ obtained from the PAW method using LDA⁴³ and $160\ {\rm cm}^{-1}$ obtained from the LDA-PP method.⁶⁴ It may be noticed that absolute TO frequencies from LDA-PP method are in very good agreement while LO frequencies differ by $48\ {\rm cm}^{-1}$ leading to a less LO-TO split. The effect of LDA and GGA reflects in the lattice constant, volume and bulk modulus determination. Due to the over-binding tendency, the LDA underestimates the lattice constant, volume and overestimates the bulk modulus. This is one of the reason for the differences with the LDA-PP results. So, at the first place, we can see the effect of volume by computing the LO-TO split and the BEC in Mg₂C at the experimental lattice constant. The LO-TO split and the dielectric constants are given in Tables 2 and 3 respectively. A difference of $5\ {\rm cm}^{-1}$ is found which is negligible in view of the fact that numerical inaccuracy in current calculations is $2\ {\rm cm}^{-1}$.⁵⁷ The values of BEC, listed in Table 3, at experimental lattice constant are close to those at the equilibrium lattice constant. Thus role of LDA or GGA appearing in terms of volume estimation is not the only reason for the residual discrepancy. The Raman and the IR spectroscopic measurements are required for a fair comparison.

## 4. Conclusions
The Seebeck coefficient, power factor and thermal conductivity are calculated for the antifluorite crystals of Be₂C, Mg₂C and BeMgC using the first-principles calculations. Modelling of TE properties predict PF of Mg₂C in the $5.17$-$58.20\times10^{-3}\ {\rm W\ mK^{-2}}$ range within 100 to 800 K. The better performance can be achieved at $\sim2\times10^{21}\ {\rm cm}^{-3}$ p-type doping level. The PF is well above the $3\times10^{-3}\ {\rm W\ mK^{-2}}$ required at experimentally realizable doping level for the next generation thermoelectrics. The hypothetical BeMgC mixed compound also exhibits such properties above 300 K. The value of EFF for Mg₂C is well above the threshold on the scale of a good thermoelectric. Moreover, major contribution of p-type carriers is observed in the energy transport. So Mg₂C is a good candidate for the thermoelectric measurements and usage. It is found above Mg₂Ge and below Mg₂Si on the EFF scale. The BeMgC may probably be a good thermoelectric unlike Be₂C. For a rigorous analysis

measurements of transport coefficients shall be fruitful.
Nevertheless, the current study demonstrates that the interface used in this study can be well applied to explore TE properties of other materials using the periodic LCAO method.

For the three methanides, the zone centre vibration frequencies are in very good agreement with other calculations. The BEC, static as well as high frequency dielectric tensors, susceptibility and refractive index are isotropic in nature for the three crystals. A consistent trend and a good accord with available results is observed. Calculated BEC charges and susceptibility show that $Be_2C$ has the maximum tendency of polarization and hence exhibits largest LO-TO splitting. The band gap measurement and spectroscopic investigations of the vibrational properties of the methanides shall be helpful to examine our findings rigorously.

## Conflicts of interest
Authors declare no conflicts of interest.

## Acknowledgements
VM is thankful to the UGC, New Delhi for the BSR fellowship. Partial support is also received from the grants of RUSA-Phase I. Authors gratefully acknowledge the assistance provided by S. Lemal and P. Ghosez, Université de Liège, Belgium at various stages of the thermoelectric calculations.

## References
1 J. M. Skelton, L. A. Burton, A. J. Jackson, F. Oba, S. C. Parker and A. Walsh, *Phys. Chem. Chem. Phys.*, 2017, **19**, 12452.
2 A. J. Hong, L. Li, R. He, J. J. Gong, Z. B. Yan, K. F. Wang, J.-M Liu and Z. F. Ren, *Sci. Rep.*, 2016, **6**, 22778.
3 T. D. Sparks, M. W. Gaultois, A. Oliynyk, J. Brgoch and B. Meredig, *Scr. Mater.*, 2016, **111**, 10.
4 W. Chen, *et al.*, *J. Mater. Chem. C*, 2016, **4**, 4414.
5 C. G. Fu, T. J. Zhu, Y. T. Liu, H. H. Xie and X. B. Zhao, *Energy Environ. Sci.*, 2015, **8**, 216.
6 W. Liu, J. Zhou, Q. Jie, Y. Li, H. S. Kim, J. Bao, G. Chen and Z. Ren, *Energy Environ. Sci.*, 2016, **9**, 530.
7 A. Zevalkink, *et al.*, *Appl. Phys. Rev.*, 2018, **5**, 021303.
8 J. Yang and T. Caillat, *MRS Bull.*, 2006, **31**, 224.
9 J.-P. Fleurial, M. A. Ryan, A. Borshchevsky, W. Phillips, E. A. Kolawa, G. J. Snyder, T. Caillat, T. Kascich and P. Mueller, *US Pat.* number 6787691, 2004.
10 W. Setyawen and S. Curtarolo, *Comput. Mater. Sci.*, 2010, **49**, 299.
11 D. S. Sholl and J. A. Steckel, *Density Functional Theory*, John Wiley & Sons, Hoboken, New Jersey, 2009.
12 S. Bhattacharya and G. K. H. Madsen, *Phys. Rev. B: Condens. Matter Mater. Phys.*, 2015, **92**, 85205.
13 K. P. Ong, D. J. Singh and P. Wu, *Phys. Rev. B: Condens. Matter Mater. Phys.*, 2011, **83**, 115110.
14 J. Neugebauer and H. Tilmann, *Wiley Interdiscip. Rev.: Comput. Mol. Sci.*, 2013, **3**, 438.
15 V. Maurya and K. B. Joshi, *J. Alloys Compd.*, 2019, **779**, 971.
16 R. A. Evarestov, *Quantum Chemistry of Solids: The LCAO First Principles Treatment of Crystals*, Springer-Verlag, Berlin, vol. 153, 2007.
17 R. Dovesi, *et al.*, *Int. J. Quantum Chem.*, 2014, **114**, 1287.
18 G. K. H. Madsen, J. Carrete and M. J. Verstraete, *Comput. Phys. Commun.*, 2018, **231**, 140.
19 K. B. Joshi, U. Paliwal and B. K. Sharma, *Phys. Status Solidi B*, 2011, **248**, 1248.
20 F. Fuchs, J. Furthmuller and F. Bechsted, *Phys. Status Solidi B*, 2009, **246**, 1877.
21 A. D. Becke, *J. Chem. Phys.*, 2014, **140**, 18A301.
22 F. Fuchs, J. Furthmüller, F. Bechstedt, M. Shishkin and G. Kresse, *Phys. Rev. B*, 2007, **76**, 115109.
23 B. Chen, J.-H. Xu, C. Uher, D. T. Morelli, G. P. Meisner, J.-P. Fleurial, T. Caillat and A. Borshchevsky, *Phys. Rev. B: Condens. Matter Mater. Phys.*, 1997, **55**, 1476.
24 J. Martin, G. S. Nolas, H. Wang and J. Yang, *J. Appl. Phys.*, 2007, **102**, 103719.
25 M. W. Gaultois, T. D. Sparks, C. K. H. Borg, R. Seshadri, W. D. Bonificio and D. R. Clarke, *Chem. Mater.*, 2013, **25**, 2911.
26 U. Ruschewitz, *Coord. Chem. Rev.*, 2003, **244**, 115.
27 R. O. G. Blachnik, P. Gross and C. Hyaman, *Trans. Faraday Soc.*, 1970, **66**, 1058.
28 O. O. Kurakevych, Y. Le Godec, T. A. Strobel and D. Y. Kim, *J. Mater. Chem. C*, 2014, **118**, 8128.
29 O. O. Kurakevych, T. A. Strobel, D. Y. Kim and G. D. Cody, *Angew. Chem.*, 2013, **52**, 8930.
30 L. H. Rovner and G. R. Hopkins, *Nucl. Technol.*, 1976, **29**, 274.
31 H. Migge, *J. Nucl. Mater.*, 1981, **103**, 687.
32 W.-S. Shish, R. B. Stephens and W. J. James, *Fusion Sci. Technol.*, 2000, **37**, 24.
33 H. Kleykamp, *J. Nucl. Mater.*, 2001, **294**, 88.
34 A. Anghel, C. Porosnicu, C. P. Lungu, K. Sugiyama, C. Kriger and J. Roth, *J. Nucl. Mater.*, 2011, **416**, 9.
35 M. M. Disko, J. C. H. Spence, O. F. Sankey and D. Saldin, *Phys. Rev. B: Condens. Matter Mater. Phys.*, 1986, **33**, 5642.
36 J. L. Corkill and M. L. Cohen, *Phys. Rev. B*, 1993, **48**, 17138.
37 C. H. Lee, W. R. L. Lambrecht and B. Segall, *Phys. Rev. B: Condens. Matter Mater. Phys.*, 1995, **51**, 10392.
38 C.-T. Tzeng, K.-D. Tsuei and W.-S. Lo, *Phys. Rev. B: Condens. Matter Mater. Phys.*, 1998, **58**, 6837.
39 F. Kalarasse and B. Bennecer, *J. Phys. Chem. Solids*, 2008, **69**, 1775.
40 S. Laref and A. Laref, *Comput. Mater. Sci.*, 2008, **44**, 664.
41 K. B. Joshi, D. K. Trivedi, U. Paliwal and K. L. Galav, *Mater. Res. Express*, 2016, **3**, 55601.
42 U. Paliwal, D. K. Trivedi, K. L. Galav and K. B. Joshi, *AIP Conf. Proc.*, 2013, **1536**, 395.
43 A. Chernatynskiy and S. R. Phillpot, *Phys. Rev. B: Condens. Matter Mater. Phys.*, 2015, **92**, 64303.
44 K. Kaur and R. Kumar, *Chin. Phys. B*, 2016, **25**, 26402.
45 G. Xing, J. Sun, Y. Li, X. Fan, W. Zheng and D. J. Singh, *Phys. Rev. Mater.*, 2017, **1**, 65405.
46 J. M. Skelton, S. C. Parker, A. Togo, I. Tanaka and A. Walsh, *Phys. Rev. B: Condens. Matter Mater. Phys.*, 2014, **89**, 205203.

47 L. Valenzano, F. J. Torres, K. Doll, F. Pascale, C. M. Zicovich- Wilson and R. Dovesi, *Z. Phys. Chem.*, 2006, **220**, 893.

48 U. Paliwal, G. Sharma and K. B. Joshi, *J. Mat. Sci.*, 2019, **54**, 1382.

49 F. Pascle, C. M. Zicovich-Wilson, G. Lopez, B. Civalleri, R. Orlando and R. Dovesi, *J. Comp. Chem.*, 2004, **25**, 888.

50 R. Dovesi, V. R. Saunders, C. Roetti, R. Orlando, C. M. Zicovich-Wilson, F. Pascale, B. Civalerri, K. Doll, N. M. Harrison, I. J. Bush, Ph. D'Arco and M. Llunell, *CRYSTAL14 User's Manual*, Turin:University of Torino, 2014.

51 J. P. Perdew, K. Burke and M. Ernzerhof, *Phys. Rev. Lett.*, 1996, **77**, 3865.

52 J. P. Perdew and A. Zunger, *Phys. Rev. B: Condens. Matter Mater. Phys.*, 1981, **23**, 5048.

53 K. Seeger, *Semiconductor Physics*, Springer-Verlag, Heidelberg, 2004.

54 Y. Pei, H. Wang and G. J. Snyder, *Adv. Mater.*, 2012, **24**, 6125.

55 K. Doll, N. M. Harrison and V. C. Saunders, *Int. J. Quantum Chem.*, 2001, **82**, 1.

56 K. Doll, *Comput. Phys. Commun.*, 2001, **137**, 74.

57 C. M. Zicovich-Wilson, F. Pascale, E. Roetti, V. R. Saunders, R. Orlando and R. Dovesi, *J. Comp. Chem.*, 2004, **25**, 1874.

58 C. M. Zicovich-Wilson, A. Bert, C. Roetti, R. Dovesi and V. R. Saunders, *J. Chem. Phys.*, 2002, **116**, 1120.

59 D. M. Rowe and C. M. Bhandari, *Modern Thermoelectrics*, Reston Publishing Company, Reston Virginia, 1983.

60 N. Miao, B. Xu, N. C. Bristowe, D. I. Bilc, M. J. Verstraete and P. Ghosez, *J. Phys. Chem. C*, 2016, **120**, 9112.

61 S. T. Oyama and R. Kieffer, *Carbides, Kirk-Othmer Encycl. Chem. Technol.*, 2000, **4**, 647.

62 D. I. Bilc, C. G. Floare, L. P. Zarbo, S. Garabagiu, S. Lemal and P. Ghosez, *J. Phys. Chem. C*, 2016, **120**, 25678.

63 H. Shi, D. Parker, M.-H. Du and D. J. Singh, *Phys. Rev. Appl.*, 2015, 014004.

64 T. Li, W. Ju, H. Liu, H. Cui, X. Zhao, Y. Yong and Z. Feng, *Comput. Mater. Sci.*, 2014, **93**, 234.

65 T. S. Moss, *Proc. Phys. Soc., London, Sect. B*, 1950, **63**, 167.