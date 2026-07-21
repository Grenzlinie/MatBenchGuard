![](./images/812404109796704256_1.jpg)

Applied Surface Science 85 (1995) 33-38

![](./images/812404109796704256_2.jpg)

# Surface barrier sensitivity of positronium formation at surfaces

A. Ishii *, T. Aisaka

Faculty of General Education, Tottori University, Koyama, Tottori 680, Japan

Received 18 May 1994

## Abstract

Smooth surface barriers are introduced to calculate wave functions for positrons and electrons at metal surfaces. The calculated positronium formation probability is very sensitive to the shape of the surface barrier potential. According to our calculations, the calculated positronium energy spectrum is sensitive not only to the positronic surface barrier but also to the electronic surface barrier potential. Thus, positronium formation may be one of the most powerful spectroscopies to measure the electronic surface barrier potential shape.

## 1. Introduction

The surface barrier potential is an important in- gredient in surface electronic states. The surface electronic density depends on the surface barrier potential. For example, to analyze a surface image state peak in an inverse photoemission spectrum, the electronic surface barrier potential plays a dominant role in calculating the spectrum. Furthermore, to determine the surface atomic structure by using scan- ning tunneling spectroscopy (STS), inclusion of a surface barrier is very important to avoid the ghost images in the STS image.

However, experimental measurement of the sur- face barrier potential is very difficult because very few spectroscopies which are sensitive to the barrier potential exist. One candidate would be angular-re- solved ultraviolet photoemission spectroscopy (ARUPS), but the sensitivity is not sufficient enough to determine the profile of the barrier potential. Though a lot of the first-principles calculation schemes are presented to obtain electronic wave function and self-consistent potential, reproduction of the surface barrier is still very hard work.

In this paper, we would like to present a new tool wherein we use positronium (Ps) formation at sur- faces. Since Ps states do not exist in metals or semiconductors because of the strong screening ef- fect in these materials [1], Ps formation occurs only at the surface via the Coulomb interaction between incident positrons and surface electrons of the first atomic layer of the surface. Thus, in contrast to ARUPS where at least ten layers contribute to the spectrum [2], Ps formation is very sensitive to the topmost atomic layer of the surface.

In recent years, the idea of Ps formation spec- troscopy has been proposed by many authors [3-9] based on the analogy between the Ps formation and ARUPS. In photoemission theory the photocurrent

* Corresponding author. Fax: + 81 857 28 6343.

0169-4332/95/$09.50 © 1995 Elsevier Science B.V. All rights reserved
SSDI 0169-4332(94)00304-1

spectrum is, in principle, calculated by the following formula:

$$
I(\boldsymbol{k}) = \sum_{i} \left| \left\langle i \left| \frac{e}{c} \boldsymbol{A} \cdot \nabla \right| f \right\rangle \right|^2 \delta(E_f - E_i - \hbar \omega), \quad (1)
$$

where $|f\rangle$ is the final state, $\langle i|$ is the initial state, and $\boldsymbol{k}$ is the wave number of the measured photoelectron.

In Ps formation theory, the formation probability is given by the following formula:

$$
\begin{aligned}
P(\boldsymbol{p}) =& \sum_{i} \left| \left\langle i \left| \frac{-e^2}{|\boldsymbol{r}_+ - \boldsymbol{r}_-|} \right| f \right\rangle \right|^2 \\
& \times \delta(E_{\text{Ps}} - E_+ - E_- - E_{\text{binding}}). \quad (2)
\end{aligned}
$$

where $|f\rangle$ is the final Ps state and $\langle i|$ is the initial state. Comparing Eqs. (1) and (2), we can see that the two formulae are very similar except for the interaction ingredient. Thus, we can consider that Ps formation would work just like ARUPS.

The Ps formation probability has been calculated by many authors using Eq. (2) or equivalent formulae. However, theoretical calculations on Ps formation have not yet included the surface barrier effect. In all previous work, a step function was assumed for the surface barrier. For example, Walker and Nieminen [5] assumed that the electronic barrier potential was the infinite step potential. Other theoretical work [7,9] assumed a finite step barrier for both electrons and positrons.

The purpose of the present work is to calculate Ps formation including smooth surface barriers for both electrons and positrons.

## 2. Surface barrier model

For the electronic surface barrier, we use the well-known formulae presented by Jones, Jennings and Jepsen [10]:

$$
V(z) = \begin{cases}
-\dfrac{1}{4(z-z_0)} \left(1 - e^{\lambda(z-z_0)}\right), & z < z_0, \\
\dfrac{-U_0}{Ae^{-\beta(z-z_0)} + 1}, & z > z_0,
\end{cases} \quad (3)
$$

where we use atomic units. This formula was originally used for thin films of tungsten and nowadays it is used for a lot of metal surfaces. Using this formula to calculate inverse photoemission spectra, we can reproduce the electronic surface state very well. In Fig. 1, we show examples of inverse photoemission spectra for a range of barrier potential shapes ($\lambda$). In Fig. 2, we show the variation of the calculated smooth surface barrier of Eq. (3) for three different $\lambda$ values.

![](./images/812404109796704256_3.jpg)

Fig. 1. Calculated angle-resolved inverse photoemission spectra for $Al(111)(\sqrt{3} \times \sqrt{3})R30^\circ$-Na surface for various surface barrier potentials.

![](./images/812404109796704256_4.jpg)

Fig. 2. Electronic surface barrier potential of Eq. (3) for $\lambda^{-1} = 1.1$, 2.0, 2.5. The energy is measured from the band bottom.

![](./images/812404109796704256_5.jpg)

Fig. 3. Positronic surface potential of Eq. (4) for $\lambda^{-1}=1.3,1.4$,
1.6. The energy is measured from the vacuum level.

For the positronic surface potential, we use the
empirical formulae presented by Jennings [11]:

$$
\begin{aligned}
& V(z) \\
& \quad= \begin{cases}-\frac{1}{4\left(z-z_{0}\right)\left[1-\mathrm{e}^{\lambda\left(z-z_{0}\right)}\right]}+\frac{\mathrm{e}^{\gamma z}}{z}, & z<z_{\mathrm{c}}, \\
U_{+}, & z>z_{\mathrm{c}}.\end{cases}
\end{aligned}
$$

The only problem in using this empirical potential is
the sharp edge at $z=z_{\mathrm{c}}$. For Ps formation, however,
this problem is not so serious, because Ps formation
occurs mainly outside the surface. In Fig. 3, we
show the variation of the calculated positronic bar-
rier potential for three different $\lambda$ values.

## 3. Wave functions

The wave functions of electrons and positrons for
the above barrier potentials are calculated from the
Schrödinger equation by the Runge-Kutta scheme.
To solve for the wave functions, we should start the
calculation from outside the solid to account, for the
stability of the solution. Far outside the surface
potentials (3) and (4) both have the same asymptotic
form

$$
V(z)=-\frac{1}{4 z}. \tag{5}
$$

![](./images/812404109796704256_6.jpg)

Fig. 4. Calculated electronic wave function (real part). The corre-
sponding surface barrier potential is imposed.

The exact solution for the potential is the Whittaker
function,
$W_{k\frac{1}{2}}(z)$

$$
\begin{aligned}
& =\mathrm{e}^{-\frac{1}{2} z} z^{k}\left(1\right. \\
& \left.+\sum_{n=1}^{\infty} \frac{\left[\frac{1}{4}-\left(k-\frac{1}{2}\right)^{2}\right] \cdots\left[\frac{1}{4}-\left(k-n+\frac{1}{2}\right)^{2}\right]}{n! z^{n}}\right),
\end{aligned}
$$

![](./images/812404109796704256_7.jpg)

Fig. 5. Calculated positron wave function (real part). The corre-
sponding surface potential is imposed. The incident positron ki-
netic energy is 0.1 hartree.

![](./images/812404109796704256_8.jpg)

Fig. 6. Calculated positron wave function (real part). The corresponding surface potential is imposed. The incident positron kinetic energy is 2.0 hartree.

where the summation will be taken up to $n=8$ in the actual calculation.

In Fig. 4 we show the real part of the calculated electronic wave function for the surface barrier potential of Eq. (3). The parameters that were used are very typical, so we can guess from Fig. 4 the width of the tail of the surface electronic density toward the vacuum side. This type of electronic wave function is well-established and widely used in ARUPS and LEED calculations.

In Figs. 5 and 6 we show the real part of the calculated positronic wave function for the barrier potential of Eq. (4). In Fig. 5 the incident positron energy is only 2.72 eV so that the wavefield is modified by the potential trough. In Fig. 6, because of its kinetic energy (54.4 eV), the positron wave field looks almost the same as that of a flat potential. However, when we look at the figure very carefully, we find that the wavelength of the wave is modified gradually through the potential trough region. Thus, we suppose that this effect would cause some interference with the electronic and Ps waves.

### 4. Ps formation probability

The matrix element of the Ps formation is calculated by the following formula:
$$
\begin{aligned}
M= & \int \mathrm{d} \boldsymbol{r}_{-} \psi_{\boldsymbol{k}}\left(\boldsymbol{r}_{-}\right) \int \mathrm{d} \boldsymbol{r}_{+} \Psi_{p}\left(\boldsymbol{r}_{-}, \boldsymbol{r}_{+}\right) V\left(\boldsymbol{r}_{-}, \boldsymbol{r}_{+}\right) \\
& \times \varphi_{\boldsymbol{q}}\left(\boldsymbol{r}_{+}\right),
\end{aligned}\qquad(7)
$$
where the suffix ' + ' means positron and ' - ' means electron. The interaction $V$ is assumed to be the Coulomb interaction [5-7,9]. We reform the above formula, for convenience, to the LEED-type calculation:
$$
\begin{aligned}
M= & \frac{1}{L^{3} \sqrt{\pi a_{0}^{3}}} \sum_{g} \sum_{\sigma= \pm 1} 4 \pi \exp \left[-\mathrm{i}\left(\boldsymbol{k}_{g \|}-\boldsymbol{q}_{g \|}\right) \cdot \boldsymbol{c}\right] \\
& \times \iint \mathrm{d} x_{-} \mathrm{d} y_{-} \exp \left[-\mathrm{i}\left(\frac{1}{2} p_{\|}-\boldsymbol{q}_{\|}-\boldsymbol{k}_{\|}\right) \cdot \boldsymbol{r}_{\|}\right] \\
& \times \int_{-\infty}^{0} \mathrm{~d} z_{-} \exp \left(-\frac{1}{2} \mathrm{i} p_{z} z_{-}\right) \\
& \times\left[\psi_{\boldsymbol{k}_{g}}(z) B_{g}^{+}+\psi_{\boldsymbol{k}_{g}}^{*}(z)\right] F\left(z_{-}\right),
\end{aligned}\qquad(8)
$$

$$
\begin{aligned}
F\left(z_{-}\right)= & \int_{-\infty}^{z_{-}} \mathrm{d} z_{+} \frac{\exp \left[-b_{g}\left(z_{-}-z_{+}\right)\right]}{2 b_{g}} \\
& \times \exp \left(-\frac{1}{2} \mathrm{i} p_{z}^{\sigma} z_{+}\right) \\
& \times\left[\varphi_{\boldsymbol{q}_{g}\left(z_{+}\right) A_{g}^{-}+\varphi^{*} \boldsymbol{q}_{g}}\left(z_{+}\right) A_{g}^{+}\right] \\
= & \int_{z_{-}}^{0} \mathrm{~d} z_{+} \frac{\exp \left[b_{g}\left(z_{-}-z_{+}\right)\right]}{-2 b_{g}} \\
& \times \exp \left(-\frac{1}{2} \mathrm{i} p_{z}^{\sigma} z_{+}\right) \\
& \times\left[\varphi_{\boldsymbol{q}_{g}}\left(z_{+}\right) A_{g}^{-}+\varphi_{\boldsymbol{q}_{g}}^{*}\left(z_{+}\right) A_{g}^{+}\right],
\end{aligned}\qquad(9)
$$
where $\boldsymbol{g}$ is the reciprocal lattice vector and $\boldsymbol{c}$ is the position of the origin of the surface atomic layer. The suffix $\sigma$ means
$$
p_{z}^{\sigma}= \begin{cases}p_{z}, & \sigma=+1, \\ p_{z}, & \sigma=-1.\end{cases}\qquad(10)
$$

Formulae (8) and (9) are very general and can be applied to any crystal having periodicity towards the surface parallel. However, hereafter, we do not include the reciprocal lattice vector, because we just want to see the typical dependence of Ps formation on the surface barrier.

### 5. Results

In Fig. 7 we show the variation of Ps formation intensity for various positron energies. The parameter $\lambda^{-1}$ indicates the profile of the positronic surface potential (see Fig. 3) where, in the present calculation, the inner potential for the positron $(U_{+})$ is fixed

![](./images/812404109796704256_9.jpg)

Fig. 7. Calculated Ps formation intensity $(|M|^{2})$ as a function of incident positron kinetic energy. The electron energy level is fixed to be -0.15 hartree measured from the vacuum level.

to be zero. From the figure, we first find that there are a lot of peaks and valleys in the Ps intensity-energy curve. However, since we fixed the electron energy level to be 0.12 hartree from the band bottom, the Ps intensity which can be measured in the actual experiment would be mixed with other Ps contributions from electrons in other energy levels.

The second important point in Fig. 7 is that the variation of the intensity curves becomes mild for the smaller parameter, i.e., closer to a step-like potential. This is quite natural, because we have found no variation using a step potential.

In Fig. 8 we show the dependence of Ps formation intensity on the electron surface barrier for an incident positron energy of 87.9 eV with normal incidence. These curves correspond to the Ps formation energy spectrum if we multiply them by the electronic density of states for each energy. We find a high sensitivity of Ps formation to the surface barrier profile.

In Fig. 9 we show the dependence of Ps formation intensity on surface potential shape for both electrons and positrons. In the figure, 'electron' means $\lambda^{-1}$ is electronic, and 'positron' means $\lambda^{-1}$ is positronic. 'e,p' means we change both $\lambda^{-1}$ values coincidentally. From this graph, we can see that the sensitivity of Ps formation on the electronic surface barrier is far stronger.

![](./images/812404109796704256_10.jpg)

Fig. 8. Calculated Ps formation intensity as a function of electronic energy. The incident positron energy is 3.23 hartree.

From Figs. 8 and 9 we see that Ps formation is very sensitive to the electronic surface barrier. Next we show the surface barrier dependence of ARUPS spectra. In Fig. 10, we show ARUPS spectra for the H/Ni(111) surface for various $\lambda^{-1}$. As can be seen in the figure, the dependence is much weaker for ARUPS spectra.

Therefore, we have found that Ps formation is one of the most powerful tools to observe the electronic surface barrier shape. The new spectroscopy we propose proceeds as follows. First, we measure the surface atomic configuration by LEED or RHEED. Second, we check the theoretical electronic states by

![](./images/812404109796704256_11.jpg)

Fig. 9. Calculated Ps formation intensity as a function of the surface potential shape parameter, $\lambda^{-1}$. The electronic energy level is fixed to be -0.375 hartree. The incident positron kinetic energy is 1.5 hartree.

![](./images/812404109796704256_12.jpg)

Fig. 10. Calculated ARUPS spectra using the smooth surface barrier potential of Eq. (3). The target surface is H/Ni(111).

ARUPS where electronic states are calculated by a first-principles self-consistent molecular dynamics calculation like FLAPW, FP-LMTO or Car-Par- rinello. Third, we check the positronic potential by low energy positron diffraction (LEPD) using the atomic configuration data of the LEED and the theoretically obtained electronic density. Finally, we fit the measured Ps spectrum to the theoretical calcu- lation by adjusting the electronic surface barrier pro- file. Though this project seems to be a very heavy one, it should be pointed out that this is currently the only way to measure the electronic surface barrier potential.

## 6. Conclusion

We presented theoretical calculations on Ps for- mation including realistic surface potential profiles for both electrons and positrons. The calculated re- sults show that the Ps formation probability is very sensitive to the shape of the electronic surface barrier potential. Thus, based on this work, we propose a new technique - Ps formation spectroscopy - to determine the electronic surface barrier potential.

## Acknowledgements

This work is supported by the Computer Center of the Insititute of Molecular Science. The authors are also grateful to M. Uesugi for his help with the computational calculation.

## References

[1] W. Brandt and A. Dupasquier, Positron Solid-State Physics (Elsevier, New York, 1983);
P.J. Schultz and K.G. Lynn, Rev. Mod. Phys. 60 (1988) 701;
A. Ishii, Ed., Positrons at Metallic Surfaces (Trans Tech Publications, Aedermannsdorf, 1992/93).

[2] A. Ishii and T. Aisaka, Surf. Sci. 242 (1991) 250.

[3] A.P. Mills, Jr., Phys. Rev. Lett. 50 (1983) 671.

[4] A. Ishii, Doctoral Thesis (Waseda University, Tokyo, 1985).

[5] A.B. Walker and R.M. Nieminen, J. Phys. F 16 (1986) L295.

[6] A. Ishii and S. Shindo, Phys. Rev. B 35 (1987) 6521.

[7] A. Ishii, Phys. Rev. B 36 (1987) 1853.

[8] A. Ishii, Surf. Sci. 209 (1989) 1.

[9] A. Ishii and J.B. Pendry, Surf. Sci. 209 (1989) 23.

[10] R.O. Jones, P.J. Jennings and O. Jepsen, Phys. Rev. B 29 (1984) 6474.

[11] P.J. Jennings, Surf. Sci. 198 (1988) 180.