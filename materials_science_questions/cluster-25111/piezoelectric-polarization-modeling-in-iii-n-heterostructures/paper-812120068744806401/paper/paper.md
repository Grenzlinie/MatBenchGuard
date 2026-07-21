![](./images/812120068744806401_1.jpg)

# Microscopic analysis of optical gain in InGaN/GaN quantum wells

B. Witzigmann, V. Laino, M. Luisier, U. T. Schwarz, G. Feicht et al.

Citation: *Appl. Phys. Lett.* 88, 021104 (2006); doi: 10.1063/1.2164907
View online: http://dx.doi.org/10.1063/1.2164907
View Table of Contents: http://apl.aip.org/resource/1/APPLAB/v88/i2
Published by the American Institute of Physics.

---

## Additional information on Appl. Phys. Lett.
Journal Homepage: http://apl.aip.org/
Journal Information: http://apl.aip.org/about/about_the_journal
Top downloads: http://apl.aip.org/features/most_downloaded
Information for Authors: http://apl.aip.org/authors

---

## ADVERTISEMENT

![](./images/812120068744806401_2.jpg)

# Microscopic analysis of optical gain in InGaN/GaN quantum wells
B. Witzigmann, $^{\text{a)}}$ V. Laino, and M. Luisier
Integrated Systems Laboratory, ETH Zürich, CH-8092 Zürich

U. T. Schwarz, G. Feicht, and W. Wegscheider
Angewandte und experimentelle Physik, Universität Regensburg, 93040 Regensburg, Germany

K. Engl, M. Furitsch, A. Leber, A. Lell, and V. Härle
Osram Opto Semiconductors GmbH, Leibnizstr. 4, D-93055 Regensburg, Germany

(Received 11 July 2005; accepted 17 November 2005; published online 11 January 2006)

A microscopic theory is used to analyze optical gain in InGaN/GaN quantum wells (QW). Experimental data are obtained from Hakki-Paoli measurements on edge-emitting lasers for different carrier densities. The simulations are based on the solution of the quantum kinetic Maxwell-Bloch equations, including many-body effects and a self-consistent treatment of piezoelectric fields. The results confirm the validity of a QW gain description for this material system with a substantial inhomogeneous broadening due to structural variation. They also give an estimate of the nonradiative recombination rate. © 2006 American Institute of Physics.
[DOI: 10.1063/1.2164907]

The optical properties of group-III nitride-based quantum wells (QW) have been subject to active research due to their application in short-wavelength emitters on the one hand, and their complex material properties on the other hand. In the wurtzite structure, these materials show strong internal spontaneous and piezoelectric fields. Moreover, Coulomb interaction effects of the electron-hole plasma play an important role. With increasing carrier density in the well, the piezoelectric fields are screened partially, which results in a reduction of the quantum-confined Stark shift of the subband levels and an increase of the optical matrix element due to the overlap of the electron and hole wave functions. As a consequence, the physics of the carrier density dependent gain spectrum are ideally governed by a combination of partially screened internal piezoelectric fields, bandfilling, Coulomb induced band-gap renormalization, and homogeneous broadening due to carrier-carrier and carrier-phonon scattering. These mechanisms have been the subject of theoretical investigations, and qualitative trends have been explained. $^{1}$

Experimental gain spectra in group-III nitride-based QWs have been reported in literature $^{2}$ from Hakki-Paoli measurements. $^{3}$ In QW structures grown by metalorganic chemical vapor deposition (MOCVD), the large lattice mismatch of GaN and InGaN causes indium fluctuations which have been observed in structural analyses. $^{4}$ For the modeling, these fluctuations can be treated as nonideality, and they translate into inhomogeneous broadening in the optical gain spectrum due to the resulting compositional or thickness variations. Various theoretical representations of inhomogeneous broadening have been suggested in literature, including the formation of quantum-dot-type structures, $^{5}$ and it has not been clear whether QW-based models are suitable to describe optical gain for this material system.

In this letter, we give a quantitative analysis of measured gain spectra from a Fabry-Perot laser diode at different carrier densities with the aid of a microscopic gain model. An active region of multiple quantum wells (MQWs) is treated as superposition of single identical QWs. The QW bandstructure is computed using a six-band ${\mathbf{k}}×{\mathbf{p}}$ method, which includes coupling effects for the heavy-hole, light-hole, and the crystal-field split hole dispersion. Spectral optical gain is obtained from the following semiclassical relation: $^{6}$

$$
G_{\text{calc}}=-\frac{2\omega}{\epsilon_{0}ncE_{o}V}\text{Im}\left(e^{i\omega t}\sum_{ji}\sum_{\mathbf{k}}\left(\mu_{\mathbf{k}}^{ji}\right)^{*}p_{\mathbf{k}}^{ji}\right),\tag{1}
$$

where $\omega$ is the laser frequency, $\epsilon_{0}$ is the vacuum permittivity, $n$ is the optical refractive index, $c$ is the speed of light in a vacuum, $E_{o}$ is the slowly varying electric-field amplitude, $V$ is the active region volume, ${\mathbf{k}}=({\mathbf{k}}_{\mathbf{x}},{\mathbf{k}}_{\mathbf{y}})$ the QW two-dimensional wave vector, $\mu_{\mathbf{k}}^{ji}$ is the matrix element between conduction subband $i$ and valence subband $j$, and $p_{\mathbf{k}}^{ji}=\langle b_{-\mathbf{k}}^{j}a_{\mathbf{k}}^{i}\rangle$ is the microscopic polarization induced between subbands $i$ and $j$. The microscopic polarization is computed by solving the semiconductor Bloch equations with an inclusion of the carrier correlations on a quantum kinetic level in the Hamiltonian. The polarization dephasing rates are calculated within the second Born approximation in the Markovian limit. $^{7,6,8}$ In contrast to Ref. 6, the equation of motion is solved in steady state, which is numerically efficient and allows for an extensive use as analysis tool. The microscopic theory ensures a correct treatment of plasma and excitonic effects, which leads to a natural derivation of homogeneous broadening and band-gap renormalization without any phenomenological parameters for these effects. Inhomogeneous broadening results from local well width or composition fluctuations depending on the material growth kinetics. In the simulation, a convolution of the homogeneously broadened gain spectrum with a Gaussian distribution $\sigma(\omega,\Delta E)$ of given spectral width is applied. $^{9}$

$$
G_{inh}(\omega)=\int d\omega'G_{\text{calc}}(\omega-\omega')\sigma(\omega',\Delta E),\tag{2}
$$

and $\Delta E$ is obtained by a comparison of experimental and simulated spectra. Under the assumption that $\Delta E$ results from a shift of the fundamental band gap induced by local indium fluctuations, the compositional fluctuations can be estimated from the band gap versus indium fraction relation.

$^{\text{a)}}$Electronic mail: bernd@iis.ee.ethz.ch

![](./images/812120068744806401_3.jpg)

FIG. 1. (Color online) Top: 2D indium distribution obtained from digital analysis of lattice images (DALI). Bottom: Average of In distribution for the vertical MQW structure.

In general, $\Delta E$ can be combination of thickness, concentration, and strain field fluctuation, therefore, the data for indium fluctuation derived here should be viewed as upper limit.

For the simulations in this letter, standard parameters from literature are used. The crystal potentials and effective masses for the bandstructure calculation are taken from Ref. 10 for GaN and InN, using Vegard's law for the ternary alloy. The band-gap relation is taken from Ref. 11, and the spontaneous and piezo induced polarization constants can be found in Ref. 12.

The gain measurements are performed with separate confinement heterostructure laser diodes which are grown by MOCVD on silicon carbide (SiC) substrates. The active region consists of three 2 nm $\text{In}_{0.1}\text{Ga}_{0.9}\text{N}$ MQWs with 6 nm GaN barrier layers.

A digital analysis of lattice images technique (DALI) (Ref. 13) from cross-section high-resolution transmission electron microscopy is performed in order to verify the QW thickness, indium composition, and well-to-well homogeneity. To avoid specimen degradation during electron-beam irradiation, $^{14,15}$ the exposure time before image recording was kept smaller than 1 min.

Figure 1 shows a color-coded map of the active region. The image indicates the presence of In-rich areas with lateral extensions of 2-5 nm on a homogeneous In matrix. The bottom of the figure depicts an average of the [11-20] direction, the measured average thickness of the QWs is 1.9 nm-2.2 nm, and the average In concentration in the wells is 10%-12%. Within the accuracy of this measurement, the well thickness and average In concentration of the three wells justify treating the wells as identical in the simulation, and no additional deformation of the gain spectrum is expected due to vertical inhomogeneities of the MQW stack.

![](./images/812120068744806401_4.jpg)

FIG. 2. Comparison between measured (solid) and calculated (dashed) gain curves for the InGaN/GaN MQW structure as function of the carrier densities $N$ and currents $I$. The carrier densities and drive currents are $N{=}[2.50\ 2.60\ 2.82\ 2.95\ 3.04\ 3.15\ 3.25]{[}10^{19}\ \text{cm}^{-3}{]}$, and $I$ $=[30\ 45\ 60\ 75\ 90\ 105\ 120]$ mA, respectively.

Gain is measured with the Hakki-Paoli method $^{3}$ using the procedure as outlined in Ref. 2. The optical waveguide is formed by a ridge structure with a width of $3\ \mu\text{m}$. The optical confinement factor is determined via simulation by solving the vectorial Helmholtz equation with a finite-element method $^{16}$ in two dimensions for the full structure that is derived from scanning-electron microscopy pictures. The resulting confinement factor is $\Gamma{=}0.017$. Figure 2 shows the comparison of measured and simulated spectral optical gain at different drive currents. The temperature is held constant at $T{=}300$ K.

The simulation matches both the measured peak gain shift with increasing carrier density and the shape of the spectral gain curve within the uncertainty of the measurement. The oscillations at the low-energy side of the measured spectra are caused by optical coupling to the SiC substrate, $^{2}$ and are not included in the simulation. The curves are obtained using the standard material parameters from literature, except that the strain- induced piezoelectric fields have been reduced by 50% in comparison to the data in Ref. 12. This could be due to local potential fluctuations in the QW with changing indium concentration which change the microscopic effective piezo-strength. Additionally, local strain relaxation effects due to the large mismatch of the lattice constants might contribute as well. The inhomogeneous broadening is found to be $\Delta E{=}31$ meV, which corresponds to an indium fluctuation of $\Delta x{=}0.012$. The bowing factor which is used for this calculation is $-1.4$ eV. $^{11}$

As comparison, AlGaAs/GaAs-based QWs typically show inhomogeneous broadening energy of $\Delta E{=}6$-$8$ meV, which indicates much smaller fluctuations for this material system. It should be emphasized that within this theory the homogeneous broadening is calculated rigorously, and is not a fitting parameter in the simulation, which allows a quantitative estimate of the inhomogeneous broadening.

Figure 3 shows the spectral gain curve for a carrier density of $N{=}3.15{\times}10^{19}\ \text{cm}^{-3}$, and different broadening values in steps of 10 meV between 0 meV and 40 meV. The dashed line is the measurement at a current of 105 mA. Due to the

![](./images/812120068744806401_5.jpg)

FIG. 3. Optical gain for an InGaN/GaN QW with inhomogeneous broadening between 0 and 40 meV in 10 meV steps. The carrier density is $N$ $=3.15×10^{19}\ \text{cm}^{-3}$, and the dashed line is measured gain at $I$=105 mA.

gain asymmetry, the gain peak redshifts with increasing inhomogeneous broadening, which is in agreement with previous investigations. $^{9}$ At a broadening value of around 30 meV, the curve matches the measured data across the entire spectral range. With the optical confinement factor being fixed, the combination of active carrier density and inhomogeneous broadening is unique, as both the peak gain and the gain width need to match the experiment for multiple drive currents. This technique allows one to match an estimated active carrier density from the simulation to the actual current of the measurement, and the resulting current/carrier density pairs are given in the caption of Fig. 2. The inhomogeneous broadening of $\Delta E$=31 meV extracted from the measured gain spectra reduces the peak gain by more than 50% at a gain level typical for device operation and increases its spectral width (see Fig. 3). It quantifies the role of indium fluctuations on the gain characteristics, and therefore typical laser characteristics such as laser threshold or differential gain, can be estimated with better accuracy in the design process.

Matching measured to simulated gain curves gives the possibility to extract the nonradiative recombination coefficients of the device. This is accomplished by relating the respective measured current and simulated carrier density values via
$$
\frac{\eta_{i} I}{q V}=A \cdot N+B \cdot N^{2}, \tag{3}
$$
where $A$ is the Shockley–Read–Hall (SRH) monomolecular recombination and $B$ is the spontaneous emission recombination. We assume that Auger processes are negligible at this wavelength. The effective active volume $V$ is estimated to be $V$=$1.2×10^{-11}\ \text{cm}^{3}$, and $I$ is the drive current. The spontaneous emission coefficient $B$ can be obtained from simulation. Integrating the simulated spontaneous emission spectrum times the spectral density, the spontaneous emission coefficient is $B_{\text{sim}}$=$0.3×10^{-10}\ \text{cm}^{3}\text{s}^{-1}$. A fit to the current versus density relation is shown in Fig. 4. Only $A$ is used as free parameter, and $B$ is taken from the simulation. Assuming an internal efficiency $\eta_{i}$=1, the resulting SRH carrier lifetime is $\tau$=$1/A$=0.9 ns, which is in the range of previously reported numbers. $^{17}$ Decreasing the internal efficiency will result in a slightly higher SRH lifetime, therefore, the extracted number for $\tau$ can be interpreted as the lower limit. The fitted curve does not cross the origin, with an offset of $-28$ mA. This could be due to carrier localization processes at low drive currents, which reduce the slope of the current versus carrier density curve, and needs further investigations.

![](./images/812120068744806401_6.jpg)

FIG. 4. Current versus carrier density for the InGaN/GaN MQW structure.

In conclusion, we demonstrated that a physics-based QW model can explain the main features of measured optical gain spectra for a $\text{In}_{0.1}\text{Ga}_{0.9}\text{N/GaN}$ MQW structure. The analysis showed an inhomogeneous broadening of $\Delta E$=31 meV, which corresponds to indium fluctuations of $\Delta x$=0.012. Moreover, a monomolecular carrier lifetime of 0.9 ns has been extracted.

$^{1}$W. W. Chow, A. F. Wright, A. Girndt, F. Jahnke, and S. W. Koch, Appl. Phys. Lett. 71, 2608 (1997).
$^{2}$U. T. Schwarz, E. Sturm, W. Wegscheider, V. Kuemmler, A. Lell, and V. Haerle, Appl. Phys. Lett. 83, 4095 (2003).
$^{3}$B. W. Hakki and T. L. Paoli, J. Appl. Phys. 46, 1299 (1975).
$^{4}$D. Gerthsen, E. Hahn, B. Neubauer, V. Potin, A. Rosenauer, and M. Schowalter, Phys. Status Solidi C 0, 1668 (2003).
$^{5}$W. W. Chow and H. C. Schneider, Appl. Phys. Lett. 81, 2566 (2002).
$^{6}$W. W. Chow and S. W. Koch, *Semiconductor-Laser Fundamentals* (Springer, Berlin, 1999).
$^{7}$O. Hess and T. Kuhn, Phys. Rev. A 54, 3347 (1996).
$^{8}$W. Schaefer and M. Wegener, *Semiconductor Optics and Transport Phenomena* (Springer, Berlin, 2002).
$^{9}$W. W. Chow, A. Girndt, and S. W. Koch, Opt. Express 2, 119 (1998).
$^{10}$J. Piprek, *Semiconductor Optoelectronic Devices* (Academic, Boston, 2003).
$^{11}$I. Vurgaftman and J. Mayer, J. Appl. Phys. 94, 3675 (2003).
$^{12}$F. Bernardini, V. Fiorentini, and D. Vanderbilt, Phys. Rev. B 64, 085207 (2001).
$^{13}$A. Rosenauer, S. Kaiser, T. Reisinger, J. Zweck, W. Gebhardt, and D. Gerthsen, Optik (Stuttgart) 102, 63 (1996).
$^{14}$T. M. Smeeton, M. J. Kappers, J. S. Barnard, M. E. Vickers, and C. J. Humphreys, Appl. Phys. Lett. 83, 5419 (2003).
$^{15}$T. Li, E. Hahn, D. Gerthsen, A. S. A. Rosenau, L. Reimann, and D. Bimberg, Appl. Phys. Lett. 86, 241911 (2005).
$^{16}$M. Streiff, A. Witzig, and W. Fichtner, IEE Proc.-J: Optoelectron. 149, 166 (2002).
$^{17}$M. Kuramoto, Y. Hisanaga, A. Kimura, N. Futagawa, A. Yamaguchi, M. Nido, and M. Mizuta, Semicond. Sci. Technol. 16, 770 (2001).