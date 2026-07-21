# Quantum critical dynamics of the random transverse-field Ising spin chain

This content has been downloaded from IOPscience. Please scroll down to see the full text.

1997 Europhys. Lett. 39 135

(http://iopscience.iop.org/0295-5075/39/2/135)

View [the table of contents for this issue], or go to the [journal homepage] for more

Download details:

IP Address: 136.186.1.81
This content was downloaded on 06/09/2015 at 08:18

Please note that [terms and conditions apply].

EUROPHYSICS LETTERS
15 July 1997

Europhys. Lett., 39 (2), pp. 135-140 (1997)

# Quantum critical dynamics of the random transverse-field
Ising spin chain

H. RIEGER¹ and F. IGLÓI²(*)

¹ HLRZ, Forschungszentrum Jülich - 52425 Jülich, Germany
² Research Institute for Solid State Physics - H-1525 Budapest, P.O.Box 49, Hungary,
Institut für Theoretische Physik, Universität zu Köln - 50937 Köln, Germany

(received 22 April 1997; accepted 10 June 1997)

PACS. 05.50+q - Lattice theory and statistics; Ising problems.
PACS. 64.60Ak - Renormalization-group, fractal, and percolation studies of phase transitions.
PACS. 68.35Rh - Phase transitions and critical phenomena.

Abstract. - Dynamical correlations of the spin and the energy density are investigated in the critical region of the random transverse-field Ising chain by numerically exact calculations in large finite systems ($L \leq 128$). The spin-spin autocorrelation function is found to decay proportionally to $(\log t)^{-2x_{\text{m}}}$ and $(\log t)^{-2x_{\text{m}}^{\text{s}}}$ in the bulk and on the surface, respectively, with $x_{\text{m}}$ and $x_{\text{m}}^{\text{s}}$ the bulk and surface magnetization exponents, respectively. On the other hand, the critical energy-energy autocorrelation functions have a power law decay, which are characterized by novel critical exponents $\eta_{\text{e}} \approx 2.2$ in the bulk and $\eta_{\text{e}}^{\text{s}} \approx 2.5$ at the surface, respectively. The numerical results are compared with the predictions of a scaling theory.

The asymptotic behavior of the time-dependent correlation functions for interacting many- body systems turned out to be a very difficult subject of theoretical research. Exact results in this field are scarce, one can mention the one-dimensional spin-1/2 XY-model [1] and the Ising chain in a transverse field [2]. Both models can be mapped onto a system of non-interacting fermions, where the equal-position correlation functions are calculated by the Pfaffian method utilizing the theory of Töplitz determinants.

In this letter we consider —for the first time— the critical dynamical correlations of an interacting quantum system in the presence of quenched (i.e. time-dependent) disorder. It has recently become clear that quenched disorder has rather different effects on phase transitions in quantum systems [3] than on thermally driven phase transitions. For example, in the Griffiths phase, which is situated at the disordered side of the critical point, the susceptibility has an essential singularity in classical systems, whereas in a quantum system the corresponding singularity is stronger, it is in a power law form.

(*) Permanent address: Institute for Theoretical Physics, Szeged University, H-6720 Szeged, Hungary.

© Les Editions de Physique

Here we consider the prototype of random quantum systems, the one-dimensional random transverse-field Ising model defined by the Hamiltonian

$$
H = -\sum_{l} J_{l} \sigma_{l}^{x} \sigma_{l+1}^{x} - \sum_{l} h_{l} \sigma_{l}^{z} , \tag{1}
$$

where the $\sigma_{l}^{x}$, $\sigma_{l}^{z}$ are Pauli matrices at site $l$ and the $J_{l}$ exchange couplings and the $h_{l}$ transverse fields are random variables with distributions $\pi(J)$ and $\rho(h)$, respectively. The Hamiltonian in (1) is closely related to the transfer matrix of a classical two-dimensional layered Ising model, which was first introduced and studied by McCoy and Wu [4].

The static critical behavior of the random transverse-field Ising model in (1) has been studied analytically and numerically by several authors [5]-[8]. The system possesses a critical point at $\delta = [\ln J]_{\text{av}} - [\ln h]_{\text{av}} = 0$, and has a spontaneous ferromagnetic order if the average couplings are stronger than the average fields. (We use the bracket $[\dots]_{\text{av}}$ to denote disorder averages.) The critical properties of the model, which are known through exact and conjectured results to a large extent, are in many respects different from that of pure systems. One important difference is that in the random system —due to a broad distribution of various physical quantities— the typical and average quantities are usually different and the rare events dominate the critical properties. For instance, the static average spin-spin correlation function is expected to behave as

$$
G_{l}^{\text{m}}(r) = \left[\left\langle\sigma_{l}^{x} \sigma_{l+r}^{x}\right\rangle\right]_{\text{av}} = \frac{1}{r^{2x_{\text{m}}}} \exp[-r/\xi] , \tag{2}
$$

where $\langle\dots\rangle$ means the (zero-temperature) expectation value. For the random transverse-field Ising model the average correlation length $\xi \sim \delta^{-\nu}$ diverges with the true exponent $\nu = 2$ and the decay exponent $x_{\text{m}} = 1 - \omega/2 \approx 0.191$ is expressed in terms of the golden mean $\omega = (1 + \sqrt{5})/2$. The decay of the average end-to-end distance critical correlations involves the surface magnetization exponent $x_{\text{m}}^{\text{s}} = 1/2$. On the other hand, the *typical* correlation length diverges with $\nu_{\text{typ}} = 1$ and the *typical* critical correlations are of a stretched exponential form: $-\log G_{\text{typ}}^{\text{m}}(r) \sim r^{1/2}$. In contrast, the critical energy-density correlation function $G_{l}^{\text{e}}(r) = \left[\left\langle\sigma_{l}^{z} \sigma_{l+r}^{z}\right\rangle\right]_{\text{av}}$ is a self-averaging quantity and at the critical point it behaves as $-\log G^{\text{e}}(r) \sim r^{1/2}$, like its typical value.

In this letter we consider the time-dependent correlation functions

$$
G_{l}^{\text{m}}(r,t) = \left[\left\langle\sigma_{l}^{x}(t) \sigma_{l+r}^{x}\right\rangle\right]_{\text{av}} \quad \text{and} \quad G_{l}^{\text{e}}(r,t) = \left[\left\langle\sigma_{l}^{z}(t) \sigma_{l+r}^{z}\right\rangle\right]_{\text{av}} \tag{3}
$$

at the critical point, both in the bulk and at the surface of the system. In a quantum system statics and dynamics are inherently related and the time evaluation is given via the Heisenberg picture by $\sigma_{l}^{x}(t) = \exp[tH] \sigma_{l}^{x} \exp[-tH]$. For simplicity here we confine ourselves to the *auto*correlations, *i.e.* $r = 0$; dynamical two-site correlations will be discussed elsewhere [9].

To start our study, we present a scaling framework for the quantum critical dynamics of the model (1). Consider the general time- and position-dependent correlation function $\left\langle\sigma_{l}^{x}(t) \sigma_{l+r}^{x}\right\rangle$, which can be written as

$$
\left\langle\sigma_{l}^{x}(t) \sigma_{l+r}^{x}\right\rangle = \sum_{n} \langle 0|\sigma_{l}^{x}|n\rangle \langle n|\sigma_{l+r}^{x}|0\rangle \exp\left[-t(E_{n} - E_{0})\right] . \tag{4}
$$

Here $|n\rangle$ denotes the $n$-th excited state of $H$ in eq. (1) with energy $E_{n}$. Before performing the disorder average, we note that this correlation function is not self-averaging at the critical point. To see its scaling behavior at the critical point we present the following simple argument. The random samples can be divided into two groups. In the *typical* samples (*i.e.* which appear with probability one) the critical correlations decay faster than any power law. On the other

hand, a vanishing fraction of the samples (the so-called *rare events*) is ordered at the critical point and the correlation function measured on these samples is of order O(1). The disorder average of the correlation function is then determined by the rare events and the corresponding scaling behavior is governed by the scaling properties of the probability distribution of these rare realizations.

For example the probability $P(l)$, which measures the occurrence of samples with a finite local magnetization $m(l) = \text{O}(1)$ at site $l$ (take, for instance, fixed boundary conditions, or consider an off-diagonal matrix element in the case of free b.c., see [8]), scales as the average critical magnetization $P(l/b) = b^{-x_{\text{m}}}P(l)$, when lengths are rescaled by a factor $b > 1$. For equal time correlations in the rare realizations the local magnetization is of order O(1) at both spatial coordinates. The corresponding joint probability distribution $P_2(l, l + r)$ factorizes for large spatial separations $\lim_{r \to \infty} P_2(l, l + r) = P(l)P(l + r)$, since the disorder is uncorrelated. Consequently, the spatial correlations follow the scaling rule

$$
G^{\text{m}}(r, t = 0) = b^{-2x_{\text{m}}}G^{\text{m}}(r/b, t = 0) , \tag{5}
$$

whereas for end-to-end distance correlations we have the surface magnetization scaling dimension $x_{\text{m}}^{\text{s}}$. Now taking $r = b$ we recover the known critical decay as given in eq. (2).

For critical time-dependent spin-spin autocorrelations, however, the scaling behavior is dif- ferent from that in eq. (5). This is due to the fact that the disorder is strictly correlated along the time axis and the probability for the occurrence of a rare sample with $m(l) = \text{O}(1)$ at different times is simply $P_2((l, t), (l, 0)) \sim P(l)$. Thus, the scaling behavior of the critical magnetization autocorrelation function satisfies the scaling rule

$$
G^{\text{m}}(r = 0, \ln t) = b^{-x_{\text{m}}}G^{\text{m}}(r = 0, \ln t/b^{1/2}) , \tag{6}
$$

where we have made use of the relation between the relevant time $t_{\text{r}}$ and length $\xi$ scales, $\sqrt{\xi} \sim \ln t_{\text{r}}$ [5], [6]. Note that the usual scaling combination is $t/b^{z}$, however, the critical dynamical exponent $z$ is $\infty$ here. Taking now the length scale as $b = (\ln t)^2$, we obtain

$$
G_{\text{m}}(r = 0, t) \sim (\ln t)^{-2x_{\text{m}}} . \tag{7}
$$

For the surface autocorrelation function the scaling relation in eqs. (6), (7) and consequently the decay exponent involve the surface magnetization exponent $x_{\text{m}}^{\text{s}}$.

For energy density autocorrelations the typical realizations govern the scaling properties at the critical point. The relevant quantity is now the matrix element $[|\langle 0|\sigma_{l}^{z}|n\rangle|^{2}]_{\text{av}}$ on the r.h.s. of eq. (4), which scales in an exponential form: $\log[|\langle 0|\sigma_{l}^{z}|n\rangle|^{2}]_{\text{av}} = b^{-1/2}\log[|\langle 0|\sigma_{l/b}^{z}|n\rangle|^{2}]_{\text{av}}$ [8]. Consequently the critical energy density autocorrelations satisfy the scaling relation

$$
\log G^{\text{e}}(r = 0, \ln t) = b^{-1/2}\log G^{\text{e}}(r = 0, \ln t/b^{1/2}) , \tag{8}
$$

and with $b = (\ln t)^2$ one obtains a power law dependence of $G^{\text{e}}(r = 0, t)$ with novel, non-trivial exponents

$$
G^{\text{e}}(r = 0, t) \sim t^{-\eta_{\text{e}}} . \tag{9}
$$

In the actual calculations we transformed the model in eq. (1) into a free fermion model [10], where the correlation functions are expressed by averages of fermion operators, which are then calculated by Wick's theorem and by the Pfaffian method [11]. We use free boundary conditions, in which case the most convenient representation is given in [12], which necessi- tates only the diagonalization of a $2L \times 2L$ matrix. From the corresponding eigenvalues and eigenvectors, one obtains the elements of the Pfaffian, which is then evaluated by calculating

![](./images/812372993685585922_1.jpg)

Fig. 1. – a) Bulk spin-spin autocorrelation function $G_{L/2}^{\rm m}(\tau)=[\langle\sigma_{L/2}^x(t)\sigma_{L/2}^x\rangle]_{\rm av}$ in imaginary time for various system sizes (and the uniform distribution). Note that we have chosen $L$ to be odd, so that $L/2$ denotes the central spin. In this plot with $[G_{L/2}^{\rm m}(\tau)]^{-1/2x_{\rm m}}$ on linear scale vs. $\tau$ on a logarithmic scale the infinite system size limit is expected to lay on a straight line as indicated. b) Same as a) for the surface spin-spin autocorrelation function $G_{1}^{\rm m}(\tau)=[\langle\sigma_{1}^x(\tau)\sigma_{1}^x\rangle]_{\rm av}$ in imaginary time.

the determinant of the corresponding antisymmetric matrix. Details of the calculations will be presented elsewhere [9].

The critical properties of the random quantum spin chains are expected to be independent of the details of the distributions of the couplings and the fields. In this letter we consider the binary distribution $\pi(J)=\frac{1}{2}\delta(J-\lambda)+\frac{1}{2}\delta(J-\lambda^{-1})$ and $h=h_0$, and the uniform distribution $\pi(J)=\Theta(1-J)\Theta(J)$ and $\rho(h)=h_0^{-1}\Theta(h_0-h)\Theta(h)$. In both cases the critical point is at $h_0=1$. All numerical data which we present below are averaged over 50000 samples.

First we study the critical spin-spin autocorrelation function for imaginary time $t=-i\tau$ in the bulk (i.e. at the site $l=L/2$) and at the surface (i.e. at site $l=1$). As shown in fig. $1a$, the finite lattice results fall into the same curve for $\log\tau\leq\sqrt{L}$ and the critical temporal decay takes place on a logarithmic scale $G_{L/2}^{\rm m}(\tau)\sim(\log\tau)^{-2x_{\rm m}}$, in agreement with the scaling prediction (7). For surface correlations the numerical calculation is less demanding and one can go up to finite systems of size $L=128$. As can be seen in fig. $1b)$, in this case the logarithmic decay depends on the surface magnetization exponent: $G_{1}^{\rm m}(\tau)\sim(\log\tau)^{-2x_{\rm m}^s}$.

The autocorrelation functions in real time generally have an oscillatory character. In the random system the average over different oscillating functions results in a complicated looking behaviour, as we demonstrate for the surface autocorrelation function in fig. $2a)$. Its Fourier transform, however, has a nice scaling character. We actually consider
$$
\chi_{1}^{\rm m}(\omega)=\frac{1}{2\pi}\int_{-\infty}^{\infty}{\rm d}t\,e^{i\omega t}\int_{-\infty}^{\infty}{\rm d}\tau\,G_{1}^{m}(t+i\tau)=\frac{2}{\omega}|\langle\omega|\sigma_{1}^x|0\rangle|^{2},
\tag{10}
$$
where $\langle\omega|$ is a state with an excitation energy $E_{\rm exc}-E_0=\omega$. For small frequencies $\omega$ we expect the finite-size scaling form of $\chi_{1}^{\rm m}(\omega)$ to be given by
$$
\chi_{1}^{\rm m}(\omega,L)\sim\omega^{-1}L^{-1}\tilde{\chi}(\log(\omega)/L^{1/2})
\tag{11}
$$
with the scaling combination $\log(\omega)/L^{1/2}$ replacing $\log(t)/L^{1/2}$ from (6). In fig. $2b)$ we show a corresponding scaling plot that yields a good data collapse.

Next we turn to analyze the energy density autocorrelation function at the critical point. As seen in fig. $3a)$, the energy density autocorrelation function is described by a power law

![](./images/812372993685585922_2.jpg)

Fig. 2. – a) Surface spin-spin autocorrelation function $G_{1}^{\mathrm{m}}(t)$ in real time for the binary distribution with $\lambda=4$. The data for $L=64$ and those shown for $L=32$ are exactly identical, although both data sets have different disorder realization. The expected $1/\log(t)$ behavior for the envelope indicated by the broken line is only a guide to the eye. b) Scaling plot of the Fourier-transformed surface spin-spin autocorrelation function $\chi_{1}^{\mathrm{m}}(\omega)$ (10) for the binary distribution and $\lambda=4$.

dependence in imaginary time $\tau$ as $G_{L/2}^{\mathrm{e}}(\tau) \sim \tau^{-\eta_{\mathrm{e}}}$, in agreement with the scaling prediction (8) and (9). The decay exponent $\eta_{\mathrm{e}} \simeq 2.2$ is universal, i.e. it does not depend on the type of randomness. A similar power law decay is found for the surface energy autocorrelations in fig. $3b)$, with a surface critical exponent $\eta_{\mathrm{e}}^{\mathrm{s}} \simeq 2.5$. These novel critical exponents complete our knowledge about the critical behavior of the random transverse-field Ising spin chain.

To summarize, we have studied dynamical correlations at the critical point of the random transverse-field Ising spin chain. We showed that the magnetization autocorrelation function has anomalous logarithmic decay, whereas the energy-density autocorrelations decay as a power law with novel critical exponents. There are still many interesting aspects of the dynamical behavior of random quantum systems. Here we mention the dynamical properties in the Griffiths phase,

![](./images/812372993685585922_3.jpg)

Fig. 3. – a) Bulk energy-energy autocorrelation function $G_{L/2}^{\mathrm{e}}(\tau)=[\langle\sigma_{L/2}^{z}(\tau)\sigma_{L/2}^{z}\rangle]_{\mathrm{av}}$ in imaginary time for various system sizes (and the binary distribution, $\lambda=4$) in a log-log plot. The straight line has slope $-2.2$, which yields our estimate for the exponent $\eta_{\mathrm{e}}$. b) Same as $a)$ for the surface energy-energy autocorrelation function $G_{1}^{\mathrm{e}}(\tau)=[\langle\sigma_{1}^{z}(\tau)\sigma_{1}^{z}\rangle]_{\mathrm{av}}$ in imaginary time. The straight line has slope $-2.5$, which yields our estimate for the exponent $\eta_{\mathrm{e}}^{\mathrm{s}}$.

the temperature-dependent autocorrelations and the dynamical two-site correlations. The study of these and other related problems is in progress [9].

***

This study was partially performed during FI's visit in Köln. This work has been supported by the Hungarian National Research Fund under grants No OTKA TO12830, TO23642 and TO15786 and the Sonderforschungsbereich (SFB) 341 (Köln-Aachen-Jülich). HR's work was supported by the Deutsche Forschungsgemeinschaft (DFG).

REFERENCES

[1] MCCOY B. M., BAROUCH E. and ABRAHAM D. B., *Phys. Rev. A*, 4 (1971) 2331.
[2] PERK J. H. H., CAPEL H. W., QUISPEL G. R. W. and NIJHOFF F. W., *Physica A*, 123 (1984) 1.
[3] See, for instance, RIEGER H. and YOUNG A. P., *Quantum Spin Glasses, Lect. Notes Phys.*, Vol. 492, *Complex behaviour of Glassy Systems*, edited by J. M. RUBI and C. PEREZ-VICENTE (Springer, Berlin-Heidelberg-New York) 1997, p. 254; J. KISKER and H. RIEGER, *Phys. Rev. B*, 55 (1997) 11981R and references therein.
[4] MCCOY B. M. and WU T. T., *Phys. Rev.*, 176 (1968) 631; 188 (1969) 982; MCCOY B. M., *Phys. Rev.*, 188 (1969) 1014.
[5] FISHER D. S., *Phys. Rev. Lett.*, 69 (1992) 534; *Phys. Rev. B*, 51 (1995) 6411.
[6] YOUNG A. P. and RIEGER H., *Phys. Rev. B*, 53 (1996) 8486.
[7] MCKENZIE R. H., *Phys. Rev. Lett.*, 77 (1996) 4804.
[8] IGLÓI F. and RIEGER H., *Phys. Rev. Lett.*, 78 (1997) 2473.
[9] IGLÓI F. and RIEGER H., to be published.
[10] LIEB E., SCHULTZ T. and MATTIS D., *Ann. Phys. (N.Y.)*, 16 (1961) 407; PFEUTY P., *Ann. Phys. (Paris)*, 57 (1970) 79.
[11] STOLZE J., NÖPPERT A. and MÜLLER G., *Phys. Rev. B*, 52 (1995) 4319; SACHDEV S. and YOUNG A. P., *Phys. Rev. Lett.*, 78 (1997) 2220.
[12] IGLÓI F. and TURBAN L., *Phys. Rev. Lett.*, 77 (1996) 1206.