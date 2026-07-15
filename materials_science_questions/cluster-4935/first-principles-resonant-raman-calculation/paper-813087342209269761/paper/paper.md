![](./images/813087342209269761_1.jpg)

14 March 1997

Chemical Physics Letters 267 (1997) 31-36

![](./images/813087342209269761_2.jpg)

# Resonance de-enhancement in the continuum Raman spectrum of HI

N. Chakrabarti, C. Kalyanaraman $^{1}$, N. Sathyamurthy $^{2}$

Department of Chemistry, Indian Institute of Technology, Kanpur 208 016, India

Received 9 September 1996; in final form 6 January 1997

## Abstract

A time-dependent quantum mechanical wave packet approach has been used to predict the continuum Raman spectrum of HI. The possibility of observing resonance de-enhancement arising from interference between wavefunctions evolving on different excited states is pointed out. © 1997 Published by Elsevier Science B.V.

## 1. Introduction

With the availability of tunable lasers, there have been a number of resonance Raman [1-4] and continuum Raman studies [5-10] carried out on diatomic and polyatomic systems. The results are usually reported in the form of Raman excitation profiles (REPs), which are scattering cross sections plotted as a function of excitation wavelength, for the fundamental as well as overtone transitions of the vibrational mode. In the case of a polyatomic molecule, understandably, different vibrational modes would have different REPs. REPs carry information on the short time (fs) dynamics of the excited state(s).

Traditionally, Raman cross sections used to be computed using the Kramers-Heisenberg-Dirac (KHD)[11,12] sum-over-states formula, but in recent years the time-dependent quantum mechanical (TDQM) approach [13-18] has become the method of choice. The latter bypasses the need to compute the bound states for the excited electronic state and it is easy to follow conceptually and implement computationally.

Since there is only one vibrational coordinate in diatomic molecules, an investigation of the REPs can be elaborate and can provide a wealth of information on the excited state(s). REPs of some halogens $(Cl_{2}$ [19], $Br_{2}$ [20,21], $I_{2}$ [22]) and interhalogens [23] have been studied experimentally as well as theoretically. When there is one or more excited state(s) present in the vicinity of the excited state to which the Raman excitation is being considered, there is the possibility of interference effects being observed.

We find that HI is an excellent candidate for a resonance Raman investigation. Photodissociation of HI has received considerable attention in recent years. When light of longest wavelength is used for photodissociation, it involves a total of four excited state potential energy curves. They all lie close to each other, although they all have different transition dipole moments with the ground state. As a result, one can expect substantial interference between the wavefunctions evolving on these four states. Levy and Shapiro [24] have proposed reasonable potential

$^{1}$ Present address: Department of Chemistry, University College London, 20 Gordon Street, London WC1H 0AJ, UK.
$^{2}$ Honorary Professor, S.N. Bose National Center for Basic Sciences, Calcutta, India.

0009-2614/97/$17.00 © 1997 Published by Elsevier Science B.V. All rights reserved.
PII S0009-2614(97)00057-2

energy curves for the ground and excited states of HI and also transition dipole moments which yield photodissociation cross section values in agreement with experimental results. Kalyanaraman and Sathya- murthy [25] pointed out that channel control could be accomplished through vibrational excitation, using HI photodissociation as an example. Zhu et al. [26] have demonstrated the feasibility of the coherent con- trol of HI⁺/I⁺ formation by exploiting the quantum mechanical interference between two competing ex- citation pathways. More recently, Gross et al. [27] have pointed out the possibility of channel control in HI photodissociation by an appropriate choice of initial superposition states. Therefore, we have under- taken a study of the continuum Raman spectrum of HI and point out the possibility of observing resonance de-enhancement [28] effects in it. If observed, they would vindicate the validity of the proposed potential energy curves and transition dipole moments.

## 2. Methodology

We make use of the potential energy curves and transition moments proposed by Levy and Shapiro [24]. For the sake of convenience, the potential en- ergy curves for the ground and first four excited states of HI are reproduced in Fig. 1a. To start with, we con- sider excitation from the ground vibrational state ($v =$ 0) of the ground electronic state ($X^{1}\Sigma_{0}$) of HI. The initial condition of the promoted state wavefunction is represented as
$$
\left|\phi^{l}(0)\right\rangle=\mu^{l}\left|\chi_{0}\right\rangle, \quad l=1-4, \tag{1}
$$
where $\chi_{0}$ represents the wavefunction of the ground vibronic state and $\mu$ the transition dipole moment; $l$ is a channel index denoting the different excited states ($1 = {}^{3}\Pi_{1}$, $2 = {}^{1}\Pi_{1}$, $3 = {}^{3}\Sigma_{1}$ and $4 = {}^{3}\Pi_{0}$). The time- evolution of the excited state wavefunction is governed by the coupled differential equation [25]:
$$
i\hbar\frac{\partial}{\partial t}\begin{pmatrix}
\phi^{1} \\
\phi^{2} \\
\phi^{3} \\
\phi^{4}
\end{pmatrix}
=
\begin{pmatrix}
H_{11} & V_{12} & V_{13} & 0 \\
V_{21} & H_{22} & V_{23} & 0 \\
V_{31} & V_{32} & H_{33} & 0 \\
0 & 0 & 0 & H_{44}
\end{pmatrix}
\begin{pmatrix}
\phi^{1} \\
\phi^{2} \\
\phi^{3} \\
\phi^{4}
\end{pmatrix}. \tag{2}
$$

The symbols $H_{ij}$ and $V_{ij}$ have their usual meaning. The Laplacian of the wavefunction is evaluated using the fast Fourier transform (FFT) algorithm and the time-evolution is followed using the second-order dif-ference (SOD) scheme [29]:
$$
\phi^{l}(t+\Delta t)=\phi^{l}(t-\Delta t)-\frac{2iH\Delta t}{\hbar}\phi^{l}(t), \tag{3}
$$
for a total of 16384 timesteps with each timestep $\Delta t =$ 0.00218 fs. We used a grid of 256 points along $r$, the HI bond distance coordinate. The minimum value of $r$ was set at $0.1\ a_{0}$, and the mesh spacing ($\Delta r$) was also set at $0.1\ a_{0}$.

![](./images/813087342209269761_3.jpg)

Fig. 1. (a) Potential energy curves for HI [24]. In the text ${}^{3}\Pi_{1}$, ${}^{1}\Pi_{1}$, ${}^{3}\Sigma_{1}$ and ${}^{3}\Pi_{0}$ excited state curves have been referred to as 1, 2, 3 and 4 respectively. Excited states 1 and 2 correspond to the H + I channel and 3 and 4 to the H + I* channel. (b) Time correlation functions for $v_{\text{i}}=0$ and $v_{\text{f}}=0$-$7$.

The autocorrelation function $C_{00}^{l}(t)=\langle\phi^{l}(0)|\phi^{l}(t)\rangle$ for each excited state $l$ was evaluated at each timestep and the total ($C_{00}(t)=\sum_{l=1}^{4}C_{00}^{l}(t)$) is plotted in Fig. 1b. The Fourier transform of $C_{00}^{l}(t)$ yields the photodissociation cross section [30]:
$$
\sigma_{l}(\omega)=\frac{2\pi\omega}{3\hbar c}\int_{-\infty}^{\infty}\mathrm{e}^{i(\omega+\omega_{0})t}\langle\phi^{l}(0)|\phi^{l}(t)\rangle\mathrm{d}t, \tag{4}
$$

where $\omega_0$ is the wavenumber corresponding to the $v =$ 0 state and $\omega$ to the incident light. The Raman amplitude ($\alpha_{10}^l(\omega)$) for the fundamental vibrational excitation via each electronic channel is obtained from the cross correlation function $C_{10}^l(t) = \langle \phi_1 | \phi^l(t) \rangle$, where $\phi_1$ is the promoted state corresponding to the wavefunction ($\chi_1$) for the first excited vibrational state ($v=1$) of the ground electronic state:

$$
\alpha_{10}^{l}(\omega)=\frac{i}{\hbar} \int_{0}^{\infty} C_{10}^{l}(t) \mathrm{e}^{i\left(\omega+\omega_{0}\right) t} \mathrm{~d} t. \tag{5}
$$

Similar expressions hold for the Raman amplitude of the overtones:

$$
\alpha_{v 0}^{l}(\omega)=\frac{i}{\hbar} \int_{0}^{\infty} C_{v 0}^{l}(t) \mathrm{e}^{i\left(\omega+\omega_{0}\right) t} \mathrm{~d} t, \quad v=2,3, \ldots(6)
$$

The Raman intensity or Raman excitation profile for each channel is obtained from the corresponding Raman amplitude:

$$
I_{v 0}^{l}(\omega)=\omega \omega_{\mathrm{s}}^{3}\left|\alpha_{v 0}^{l}(\omega)\right|^{2}, \quad v=1,2,3, \ldots, \tag{7}
$$

where $\omega_{\mathrm{s}}$ is the frequency of the scattered radiation. In reality, the observable is the overall Raman excitation profile:

$$
I_{v 0}(\omega)=\omega \omega_{\mathrm{s}}^{3}\left|\alpha_{v 0}(\omega)\right|^{2}, \quad v=1,2,3, \ldots, \tag{8}
$$

where $\alpha_{v 0}(\omega)=\sum \alpha_{v 0}^{l}(\omega)$. It is clear from the above that there will be constructive and destructive interference between the Raman amplitudes for the different channels and the observed REP for the fundamental (as well as the overtone) excitation would reveal enhancement and de-enhancement effects.

## 3. Results and discussion

The autocorrelation function $C_{00}(t)$ and the cross correlation functions $C_{v 0}(t)(v=1-7)$ for HI in its ground vibronic state are shown in Fig. 1b. The magnitude of $C_{00}$ at initial time $(t=0)$ reflects the value of $\mu^{2}=\sum_{l=1}^{4}\left(\mu^{l}\right)^{2}$ [31]. $C_{00}(t)$ decreases dramatically in about 3 fs and then it dies off relatively slowly in the following 3 fs. $C_{v 0}$ values, understandably, start from zero, rise to a maximum, fall off and then rise to a second maximum before dying off to zero. The first and predominant hump in $C_{10}$ is over in less than 3 fs, implying that the continuum Raman scattering resulting in the fundamental $(v=0 \rightarrow 1)$ vibrational excitation is over in about 3 fs. The successively higher overtones also have a double humped $C_{v 0}$ and take successively longer times.

The REPs resulting from each electronic excited state for the $v=0 \rightarrow 1$ transition are shown in Figs. 2a-d and they all show only a single maximum each. The overall REP for the fundamental transition, shown in Fig. 2e, on the other hand, has a characteristic "dip" (between the two maxima) which is close to the maximum of the absorption cross section (not shown). This is clearly a de-enhancement and it can be traced to the interference between the Raman amplitudes for the four different excited states. REPs for the overtone excitations $(v=2-5)$ show an even stronger de-enhancement effect as shown in Figs. 3a-d.

The interference effect seen in REP is to be contrasted with the relatively smooth photodissociation cross section curve obtained for HI [24,25]. This is because the latter is a sum over partial cross sections while the former is related to the square of the sum over channel-specific Raman amplitudes. It is worth adding that the nonadiabatic coupling between the excited states, which plays an important role in the photodissociation of HI into $\mathrm{H}+\mathrm{I}$ and $\mathrm{H}+\mathrm{I}^{*}$ channels, has been found to be of little significance in deciding the REPs.

TDQM approaches to photo-excitation processes have been generally ignoring angular momentum couplings. A study by Offer and Balint-Kurti on HOCl [32] is an exception. There are four different excited electronic states involved in the present study: $^{1} \Pi_{1}$, $^{3} \Sigma_{1},^{3} \Pi_{0}$ and $^{3} \Pi_{1}$. Of these, $^{3} \Pi_{0}$ is optically coupled only with the ground electronic state $\left({ }^{1} \Sigma_{0}\right)$. The $^{1} \Sigma_{0}-$ $^{3} \Pi_{0}$ transition requires [33] that the total angular momentum $(J=S+\Lambda$, where $S$ and $\Lambda$ are the spin and orbital angular momentum vectors respectively) changes by unity during excitation (and de-excitation) and this would be provided by the spin angular momentum of the photon. For a rotationless HI absorbing (or emitting) a single photon, $J+J_{h \nu}=J^{\prime} . J_{h \nu}$ represents the spin of the photon. All the other three excited states are coupled to each other and to the ground electronic state. They all correspond to $J=1$ ( $J=0$ is not allowed [33]) and therefore automatically involve $\Delta J=1$ transition. Once again the spin angular

![](./images/813087342209269761_4.jpg)

Fig. 2. The channel specific REPs and the overall REP for HI: (a) $l=1$; (b) $l=2$; (c) $l=3$; (d) $l=4$ and (e) overall.

momentum of the photon provides for the change in $J$. The normal selection rule of singlet-singlet is not being obeyed in the present case because of spin-orbit coupling, which is taken care of through proper choice of transition dipole matrix elements.

## 4. Summary and conclusion

We have demonstrated in this Letter the utility of time-dependent quantum mechanical approach to predicting continuum Raman spectra of diatomic molecules like HI involving several dissociative elec- tronic excited states. Since they all lie close to each other in energy and three of them are strongly cou- pled, the interference between the time-evolving wavefunctions on these states and hence their Raman amplitudes is large enough that the overall Raman excitation profile for HI reveals a substantial de- enhancement. The effect is predicted to be stronger for the overtones. If these predictions are verified in the laboratory, it would vindicate the reliability of the

![](./images/813087342209269761_5.jpg)

Fig. 3. REPs for the overtones of HI: (a) $v=0\rightarrow2$; (b) $v=0\rightarrow3$; (c) $v=0\rightarrow4$ and (d) $v=0\rightarrow5$.

potentials and the transition moments proposed [24]
for the excited states of HI.

Finally, we would like to add that the TDQM frame-
work provides a natural means of computing transients
[3] that might be observed in the laboratory in the near
future. This will form the subject of a future study.

## Acknowledgements

This study was supported in part by a grant from
the INDO-US subcommission. NC is grateful to Nis-
hant Sinha for valuable discussions. We are grateful
to Dr. S. Umapathy for introducing us to resonance
Raman and de-enhancement effects and to the anony-
mous referee for his critical comments on the earlier
version of the manuscript.

## References

[1] G.H. Atkinson, in: Advances in laser spectroscopy, Vol. 1,
eds. B.A. Garetz and J.R. Lombardi (Heyden, London, 1982)
ch. 8;
B.S. Hudson, P.B. Kelly, L.D. Ziegler, R.A. Desiderio,
D.P. Gerrity, W. Hess and R. Bates, in: Advances in laser
spectroscopy, Vol. 3, eds. B.A. Garetz and J.R. Lombardi
(Wiley, Singapore, 1986) ch. 1.

[2] A.B. Myers and R.A. Mathies, in: Biological applications
of Raman spectroscopy, Vol. 2, ed. T.G. Spiro (Wiley, New
York, 1987) ch. 1.

[3] M. Shapiro, J. Phys. Chem. 97 (1993) 7396;
M. Shapiro, in: Femtosecond chemistry, Vol. 1, eds. J. Manz
and L. Wöste (VCH, Weinheim, 1995) ch. 9.

[4] N. Biswas and S. Umapathy, Chem. Phys. Lett. 236 (1995)
24.

[5] W. Kiefer and H.J. Bernstein, J. Raman Spectrosc. 1 (1973)
417.

[6] D.G. Imre, J.L. Kinsey, A. Sinha and J. Krenos, J. Phys.
Chem. 88 (1984) 3956.

[7] R.J. Sension, R.J. Brudzynski and B.S. Hudson, Phys. Rev.
Lett. 61 (1988) 694;
R.J. Sension, R.J. Brudzynski, B.S. Hudson, J. Zhang and
D.G. Imre, Chem. Phys. 141 (1990) 393;
M. von Dirke, B. Heumann, R. Schinke, R.J. Sension and
B.S. Hudson, J. Chem. Phys. 99 (1993) 1050.

[8] K.Q. Lao, M.D. Person, P. Xayariboun and L.J. Butler, J.
Chem. Phys. 92 (1990) 823;
M.D. Person, P.W. Kash and L.J. Butler, J. Chem. Phys. 94
(1991) 2557.

[9] L.D. Ziegler, J. Chem. Phys. 84 (1986) 103;
L.D. Ziegler, Y.C. Chung, P.G. Wang and Y.P. Zhang, J.
Chem. Phys. 90 (1989) 4125.

[10] A.B. Myers, J. Opt. Soc. Am. B. 7 (1990) 1665;
F. Markel and A.B. Myers, Chem. Phys. Lett. 167 (1990)
175;
D.L. Phillips and A.B. Myers, J. Phys. Chem. 95 (1991)
7164.

[11] H.A. Kramers and W. Heisenberg, Z. Phys. 31 (1925) 681.

[12] P.A.M. Dirac, Proc. R. Soc. A 114 (1927) 710.

[13] S.-Y. Lee and E.J. Heller, J. Chem. Phys. 71 (1979) 4777.

[14] E.J. Heller, Acc. Chem. Res. 14 (1981) 368.

[15] E.J. Heller, R.L. Sundberg and D.J. Tannor, J. Phys. Chem.
86 (1982) 1822;
R.L. Sundberg and E.J. Heller, Chem. Phys. Lett. 93 (1982)
586;
D.J. Tannor and E.J. Heller, J. Chem. Phys. 77 (1982) 202.

[16] S.O. Williams and D.G. Imre, J. Phys. Chem. 92 (1988)
3363.

[17] M.V. Ramakrishna and R.D. Coalson, Chem. Phys. 120
(1988) 327.

[18] N. Biswas, S. Umapathy, C. Kalyanaraman and N.
Sathyamurthy, Proc. Indian Acad. Sci. (Chem. Sci.) 107
(1995) 233.

[19] J. Strempel and W. Kiefer, J. Chem. Phys. 95 (1991) 2391.

[20] J. Strempel and W. Kiefer, J. Raman Spectrosc. 22 (1991)
583.

[21] B. Hartke, Chem. Phys. Lett. 160 (1989) 538; J. Raman
Spectrosc. 22 (1991) 131.

[22] J. Strempel and W. Kiefer, Can. J. Chem. 69 (1991) 1732.

[23] I. Levy, M. Shapiro and A. Yogev, J. Chem. Phys. 96 (1992)
1858;
M. Ganz, W. Kiefer, E. Kolba, J. Manz and J. Strempel,
Vibr. Spectrosc. 1 (1990) 119;
M. Ganz, W. Kiefer, E. Kolba, J. Manz and P. Vogt, Chem.
Phys. 164 (1992) 99;
M. Ganz, W. Kiefer, A. Materny and P. Vogt, J. Mol. Struct.
226 (1992) 115;
H. Guo, J. Chem. Phys. 99 (1993) 1685.

[24] I. Levy and M. Shapiro, J. Chem. Phys. 89 (1988) 2900.

[25] C. Kalyanaraman and N. Sathyamurthy, Chem. Phys. Lett.
290 (1993) 52;
C. Kalyanaraman and N. Sathyamurthy, Curr. Sci. 65 (1993)
19.

[26] L. Zhu, V. Kleiman, X. Li, S.P. Lu, K. Trentelman and R.J.
Gordon, Science 270 (1995) 77.

[27] P. Gross, A.P. Gupta, D.B. Bairagi and M.K. Mishra, J.
Chem. Phys. 104 (1996) 7045.

[28] P. Stein, V. Miskowski, W.H. Woodruff, J.P. Griffin, K.G.
Werner, B.P. Gaber and T.G. Spiro, J. Chem. Phys. 64 (1976)
2159;
K.S.-K. Shin and J.I. Zink, J. Am. Chem. Soc. 112 (1990)
7148;
J.I. Zink and K.-S. K. Shin, in: Advances in photochemistry,
Vol. 16 (Wiley, New York, 1991) p. 119;
C. Reber and J.I. Zink, J. Phys. Chem. 96 (1992) 1991.

[29] M.D. Feit, J.A. Fleck, Jr. and A. Steiger, J. Comput. Phys.
47 (1982) 412;
D. Kosloff and R. Kosloff, J. Comput. Phys. 52 (1983) 35;
R. Kosloff and D. Kosloff, J. Chem. Phys. 79 (1983) 1823;
R. Kosloff, J. Phys. Chem. 92 (1988) 2087;
V. Mohan and N. Sathyamurthy, Comput. Phys. Rep. 7
(1988) 412;
N. Balakrishnan, C. Kalyanaraman and N. Sathyamurthy,
Phys. Rep., in press.

[30] E.J. Heller, J. Chem. Phys. 68 (1978) 3891;
K.C. Kulander and E.J. Heller, J. Chem. Phys. 69 (1978)
2439.

[31] B.R. Johnson and J.L. Kinsey, J. Chem. Phys. 99 (1993)
7267.

[32] A.R. Offer and G.G. Balint-Kurti, J. Chem. Phys. 104 (1996)
563;
A.R. Offer and G.G. Balint-Kurti, J. Chem. Phys., in press.

[33] G. Herzberg, Molecular spectra and molecular structure.
(I). Spectra of diatomic molecules (Van Nostrand Reinhold,
Toronto, 1950).