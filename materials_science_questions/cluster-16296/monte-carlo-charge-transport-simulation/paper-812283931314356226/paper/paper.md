# Quantum corrected full-band Cellular Monte Carlo simulation of AlGaN/GaN HEMTs

Shinya Yamakawa, Stephen M. Goodnick, Shela Aboud¹ and Marco Saraniti¹

Department of Electrical Engineering, Arizona State University,
Tempe, AZ, 85287-5706, USA
¹ Department of Electrical and Computer Engineering, Illinois Institute of Technology,
Chicago, IL, 60616-3793, USA
email: shinya.yamakawa@asu.edu

A full-band Cellular Monte Carlo (CMC) approach [1] is applied to simulation of electron transport in AlGaN/GaN HEMTs with quantum corrections included via the effective potential method. The full-band CMC transport model is based on a detailed model of the electron-phonon interactions in the wurtzite crystal structure using the rigid pseudo-ion model, where the anisotropic deformation potentials are derived from the electronic band structure, the atomic pseudopotential, and the phonon dispersion. Realistic polar-optical phonon, impurity, piezoelectric and dislocation scatterings are also included in the full-band CMC simulator, which shows good agreement with measured velocity-field data from pulsed I-V measurements at Arizona State University [2].

AlGaN/GaN HEMTs have several advantages over GaAs based technology due to their potential for high-voltage and high-power operation. An important issue of AlGaN/GaN HEMTs is the high sheet charge density $N_s$, which is obtained even without modulation doping in the AlGaN layer due to the piezoelectric and spontaneous polarization. In order to include quantum effects into the transport simulation, one needs to solve the two-dimensional Schrödinger-Poisson problem with an appropriate transport kernel. An alternative way is the use of effective potentials [3] with a particle-based Monte Carlo simulator. The effective potential, $V_{eff}(x)$, is obtained by the integral transformation from the classical potential $V(x)$ as

$$
V_{eff}(x)=\frac{1}{\sqrt{2 \pi} a_{0}} \int_{-\infty}^{+\infty} V(x+\xi) \exp \left(-\frac{\xi^{2}}{2 a_{0}^{2}}\right) d \xi. \tag{1}
$$

The calculated HEMT structure consists of a 15 nm doped $Al_{0.2}Ga_{0.8}N$ layer, 5 nm unintentionally doped $Al_{0.2}Ga_{0.8}N$ layer, and 100 nm unintentionally doped GaN layer, shown in Fig. 2. The background, unintentional doping is taken as $10^{17}\ \text{cm}^{-3}$ for both the GaN and AlGaN layers. The electron densities with various Gaussian smoothing parameters, $a_0$, are shown in Fig. 3. The Schrödinger-Poisson result is also shown in the figure. This figure shows that the use of $a_0$=3Å can quite accurately describe the electron density reduction and charge setback from the interface.

This effective potential approach has been combined with the full-band CMC code for device simulation. Figure 4 shows the electron distribution along the channel. The electron displacement due to the effective potential can be clearly seen in the figure. The Calculated $I_d$-$V_{ds}$ characteristics, with and without the effective potential, are shown in Fig. 5. An approximately 20 % reduction due to quantum-mechanical size-quantization effects is found in the current.

[1] M. Saraniti and S.M. Goodnick, *IEEE Trans. Elec. Dev.* 47, 1909 (2000)
[2] J.M. Barker *et al.*, *Physica* B314, 39 (2002)
[3] D.K. Ferry, *Superlattices and Microstructures* 28, 419 (2000)

A full journal publication of this work will be published in the Journal of Computational Electronics.

![](./images/812283931314356226_1.jpg)

Fig. 1 : Velocity vs field relationship for bulk GaN.

![](./images/812283931314356226_2.jpg)

Fig. 2 : Structure of the calculated HEMT device.

![](./images/812283931314356226_3.jpg)

Fig. 3 : Electron density by the classical and effective potential method. The electron density by the Schrödinger-Poisson calculation is also shown.

![](./images/812283931314356226_4.jpg)

Fig. 4 : Electron distribution along the channel using the effective potential with $a_0$=3Å. Note the displacement of electrons by the effective potential.

![](./images/812283931314356226_5.jpg)

Fig. 5 : Output device characteristics with and without the effective potential. The gate voltage is -1V. Notice that there is about 20 % current reduction due to the quantization effect.

A full journal publication of this work will be published in the Journal of Computational Electronics.