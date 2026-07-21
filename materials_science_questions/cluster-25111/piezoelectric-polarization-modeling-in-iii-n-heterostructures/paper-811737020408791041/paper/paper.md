# Quantum-Confined Stark Effects in a Single GaN Quantum Dot

This content has been downloaded from IOPscience. Please scroll down to see the full text.

2008 Chinese Phys. Lett. 25 2628

(http://iopscience.iop.org/0256-307X/25/7/081)

View [the table of contents for this issue](), or go to the [journal homepage]() for more

Download details:

IP Address: 134.129.120.3
This content was downloaded on 22/05/2015 at 03:29

Please note that [terms and conditions apply]().

# Quantum-Confined Stark Effects in a Single GaN Quantum Dot

LIU Yong-Hui(刘永辉)**, WANG Xue-Feng(王雪峰), LI Shu-Shen(李树深)

State Key Laboratory for Superlattices and Microstructures, Institute of Semiconductors, Chinese Academy of Sciences, Beijing 100083

(Received 14 April 2008)

Using analytical expressions for the polarization field in GaN quantum dot, and an approximation by separating the potential into a radial and an axial, we investigate theoretically the quantum-confined Stark effects. The electron and hole energy levels and optical transition energies are calculated in the presence of an electric field in different directions. The results show that the electron and hole energy levels and the optical transition energies can cause redshifts for the lateral electric field and blueshifts for the vertical field. The rotational direction of electric field can also change the energy shift.

PACS: 73.21.La, 73.40.Kp, 71.23.An

In the past decades, the quantum-confined Stark effect (QCSE) has received much attention in semiconductor low-dimensional quantum structures.[¹] Many important and interesting phenomena have been observed for the Stark effects. For example, the quantum controlled logic gate may be realized by quantum dot (QD) under an external static electric field.[²]

Recently, Jarjour *et al.*[³] reported direct evidence for the control of the oscillator strength of the exciton state in a single GaN quantum dot by the application of a vertical electric field. In addition, they also studied the effect of externally applied vertical electric field on the optical properties of single InGaN/GaN quantum dots via microphotoluminescence spectroscopy.[⁴] Robinson *et al.*[⁵] studied the effect of an externally applied lateral electric field upon an exciton confined in a single InGaN quantum dot using microphotoluminescence spectroscopy. In these works, the redshift have also been observed. Some theoretical studies have been carried out for the effects of an electric field. In Ref. [6], the single band effective mass Hamiltonian is used to calculate the ground states of single-particle states. In Ref. [3], the method based on atomistic semi-empirical tight-binding simulations is used to study the exciton state. In Ref. [7], the effective-mass envelope function theory is used to calculate the electron and hole energy levels and optical transition energies.

A simple calculation for GaN QD was completed by the authors of Ref. [8] based on Ref. [9]. The analytical expressions for the polarization field are derived and the dependence of exciton energy on dot size is studied.

In this work, we begin the approximation[⁸] by separating the potential into a radial part and an axial (z direction) part and calculate the electron and hole energy level structures and optical transition energy of GaN QD in an electric field, taking into account the cylindrical structures of QDs.

The built-in polarization fields in nitride QDs has the most significant effect on the confinement potential in the z direction with the in-plane field providing additional lateral confinement.[⁸] Therefore, the radial polarization potential is a harmonic oscillator potential $ekr^2/2$, with the value of $k$ given by the second derivative with respect to $x$ of the potential evaluated at $r=0$, $\partial_x^2\varphi(z)$. After considering the lateral field $F_1$ the lateral confinement energy is given as $E_r=\hbar\sqrt{ek/m^*}-\frac{eF_1^2}{2k}$, where $m^*$ is the effective mass of the carrier.

For the axial part, the potential of a cylindrical QD with radius $R$ and height $h$ is given by[⁸]

$$
\begin{aligned}
\varphi(z) &= JI_1+\left(K+\frac{P_{QD}-P_M}{4\pi\varepsilon_r\varepsilon_0}\right)I_2, \\
I_1 &\approx 4\pi\left(z-\frac{h}{2}\right)\left(-1+\frac{2f}{\sqrt{4+f^2}}-\frac{f^3}{\sqrt{(4+f^2)^{3/2}}}\right), \\
I_2 &\approx 4\pi\left(z-\frac{h}{2}\right)\left(1-\frac{2f}{\sqrt{4+f^2}}\right),
\end{aligned}\tag{1}
$$

where $f=h/R$ is the ratio of the dot height to radius, $P_{QD}$ and $P_M$ are the spontaneous polarization constants of the QD and Matrix materials, respectively, $\varepsilon_r$ is the relative permittivity of the QD material, and $J$ and $K$ are constants given by

$$
J=\frac{-\varepsilon_0(1+\nu)(2e_{15}+e_{31}+e_{33})}{8\pi\varepsilon_r\varepsilon_0(1-\nu)},
$$

$$
K=\frac{\varepsilon_0}{8\pi\varepsilon_r\varepsilon_0}\left(4e_{31}+2e_{33}-\frac{1+\nu}{1-\nu}(2e_{15}+e_{31}+e_{33})\right),
$$

where $\varepsilon_0$ is the isotropic misfit strain, $\nu$ is Poisson's ratio, and $e_{ij}$ are the piezoelectric constants.

Using the above expressions the variation of the conduction and valence band energy along the z axis can be calculated, and a triangular well potential is

*Email: liuyh@semi.ac.cn
© 2008 Chinese Physical Society and IOP Publishing Ltd

approximated. By using Eq. (1), $I_1$, and $I_2$ the slop $F$ of the potential can then be obtained.

In the presence of external vertical electric field $F_2$, the Hamiltonians for the triangular well read $H_z = H_z^0 + H_z'$, where

$$
H_z^0 = \begin{cases}
\dfrac{p^2}{2m^*} + V_0, & \text{for } z < 0, \\
\dfrac{p^2}{2m^*} - e(F_2 - F)z, & \text{for } 0 < z < h, \\
\dfrac{p^2}{2m^*} + V_0 - eF_2h, & \text{for } z > h,
\end{cases} \tag{2}
$$

$$
H_z' = \begin{cases}
-eF_2z, & \text{for } z < 0, \\
0, & \text{for } 0 < z < h, \\
-eF_2(z - h), & \text{for } z > 0.
\end{cases} \tag{3}
$$

The Schrödinger equation of $H_z^0$ can be solved exactly in terms of the Airy function $\text{Ai}(\chi)$, giving

$$
\psi(z) = \begin{cases}
A\exp(\sqrt{\beta(V_0 - E_z^0)}z), & z < 0 \\
B\text{Ai}\left[\left(\dfrac{\beta}{e^2(F - F_2)^2}\right)^{1/3}\left(e(F - F_2)z - E_z^0\right)\right], & 0 < z < h, \\
C\exp(-\sqrt{\beta(V_0 - eF_2h - E_z^0)}z), & z > h
\end{cases} \tag{4}
$$

where $\beta = 2m^*/\hbar^2$, $V_0$ is the band offset, $E_z^0$ is the axial confinement energy which can be obtained from the boundary conditions, and $A$, $B$, $C$ are the normalization constants.

Using the perturbation theory the energy $E_z'$ can be calculated, and the energy $E_z = E_z^0 + E_z'$ can be obtained. According to Ref. [8], the value of $k$ for the radial potential can be determined by taking $\partial_x^2\varphi(z)$ at the position at which the wave function solution attains its maximum value.

The transition energy is

$$
E_T = E_r^e + E_r^h + E_z^e + E_z^h + E_G, \tag{5}
$$

where $E_G$ is the band gap of the QD material. Taking the material parameters from Refs. [9,10], we can obtain the structure parameters of the QD to be $R = 10.5\,\text{nm}$, $h = 4\,\text{nm}$, and $f = 0.38$.

Figure 1 shows the energy of transition from the electron energy level to the hole energy level for the lateral electric field. From this figure, we find that the transition energies have redshifts for the electric field which is vertical to the $z$ direction. When the lateral electric field is about $150\,\text{kV/cm}$, the transition energy $E_T$ is about $3.69\,\text{eV}$, and the energy shift of transition energy is about $20\,\text{meV}$. However, with the increase of electric field, the energy shift will increase rapidly. The reason is that the external electric field is large enough to make the carrier to get across the polarization potential which is approximated by a harmonic oscillator potential. The inset in Fig. 1 shows the field dependence of the energy shift of electron $(\Delta E_c)$ and the hole $(\Delta E_v)$. With the increasing field, $\Delta E_c$ and $\Delta E_v$ all increases. These are caused by the tilting of their band edges.

![](./images/811737020408791041_1.jpg)

Fig. 1. Energy of transition from the electron energy level to the hole energy level for the lateral electric field. The inset shows the energy shift of electron $(\Delta E_c)$ and the hole $(\Delta E_v)$ as a function of the lateral electric field.

![](./images/811737020408791041_2.jpg)

Fig. 2. Energy of transition as a function of the vertical electric field. The inset shows theoretical dependence of the energy shift on the vertical electric field. The continuous line is the fit of the theoretical values (square symbols) with a second order polynomial (see text).

Figure 2 shows the energy of transition from the electron energy level to the hole energy level for the vertical electric field parallel to the $z$ direction (this means that the internal field should be in the $-z$ direction). From this figure, we find that the transition energies have blueshifts for the electric field along the $z$ direction. With the increasing field, the energy shift of transition energy increases, and can be about $30\,\text{meV}$ at about $300\,\text{kV/cm}$. The inset shows the calculated dependence of the ground state energy shift on the field. The values are fitted by

$$
\Delta E(F_2) = \mu F_2 + \alpha F_2, \tag{6}
$$

where $\mu$ is the vertical component of the permanent dipole and $\alpha$ is the polarizability along the vertical direction. Such a dependence has been observed for both lateral$^{[11,12]}$ and vertical$^{[3,4]}$ applied fields for different systems of QDs. A least-square fit to the calculated value results in a value of $1.26\pm0.11$eÅ for the permanent dipole and of $95.28\pm3.56$meV/(MV/cm)$^2$ for the polarizability. An estimate of the internal piezoelectric field can be obtained by extrapolating the energy shift to its maximum value. In the case of the presented QD this value is about 0.7MV/cm.

![](./images/811737020408791041_3.jpg)

Fig.3. Energies of transition as functions of the angle between the electric Field $F_3$ and $z$ direction. The electric field is 100kV/cm and 200kV/cm, respectively.

Figure 3 shows the energies of transition as functions of the angle $\theta$ which is the angle between the electric field and the $z$ direction. The whole electric field are $F_{12}=F_1+F_2=F_3\sin\theta+F_3\cos\theta$. In our calculations, the electric field $F_3$ is taken to be 100kV/cm and 200kV/cm, respectively. When $0<\theta<0.5$ the lateral and vertical electric field all exist. From the figure we know that when the angle changes form 0 to 0.5, the energy has redshifts, contrarily the energy has blueshifts. The reason is that the lateral electric field makes the energy redshift and the vertical electric field makes the energy blueshift, therefore the whole effect of field will be decided by the angle between the field and $z$ direction, i.e. by the direction of field $F_{12}$. In addition, we also know that the magnitude of $F_3$ can affect that of the energy shift. With the decrease of electric field the energy shift decreases.

In summary, we have studied the quantum Stark effects of GaN quantum dot in the presence of an electric field using the approximation by separating the potential into a radial part and an axial part. The calculated results indicate that blueshifts are obtained under vertical field and redshifts are obtained under lateral field, and the rotational direction of electric field can decided the change of blueshifts or redshifts.

## References

[1] Yoffe A D 2001 *Adv. Phys.* **51** 1
[2] Berman G P and Doolen G D 2000 *Superlattices and Microstructures* **27** 89
[3] Jarjour F et al 2007 *Phys. Rev. Lett.* **99** 197403
[4] Jarjoura F et al 2007 *Superlattices and Microstructures* **6** 21
[5] Robinson W et al 2005 *Appl. Phys. Lett.* **86** 213103
[6] Nakaoka T, Kako S and Arakawa Y 2006 *Phys. Rev. B* **73** 121305
[7] Li S S and Xia J B 2005 *Appl. Phys. Lett.* **87** 043102
[8] Williams D P, Andreev A D and O'Reilly E P 2006 *Phys. Rev. B* **73** 241301
[9] Williams D P et al 2005 *Phys. Rev. B* **72** 235318
[10] Pearton S J 2000 *Optoelectronic Properties of Semiconductors and Superlattices: GaN and Related Materials?* (Netherlands: Breach Science) chap 3 p 103
[11] Robinson J et al 2005 *Appl. Phys. Lett.* **86** 213103
[12] Seufert J et al 2002 *Physica E* **13** 147