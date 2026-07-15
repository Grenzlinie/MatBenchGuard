Raman Scattering by Coupled LO Phonon-Plasmon Mode
in $n$-GaAs

Shin'ichi KATAYAMA and Kazuo MURASE

Department of Physics, Osaka University, Toyonaka 560

(Received July 19, 1976)

Recent experimental results of Raman spectra in gallium arsenide are analyzed on the basis of a non-local theory of the coupling between plasmons and longitudinal optical (LO) phonons. A formula is derived which gives the efficiency for the Raman scattering by a coupled LO phonon-plasmon (LO-PL) mode in an absorptive medium. The finiteness of the wave number of the scattering mode and the attenuation of light in the medium are explicitly taken into account. An analysis of the GaAs Raman spectra obtained recently by Murase et al. shows that the theory reproduces the experimental results fairly well. It also explains the characteristic features of the spectra. The integrated efficiency from the LO-PL mode in GaAs is estimated to be of the order of $10^{-11}$.

§1. Introduction

The elementary excitation of the coupled mode of the longitudinal optical (LO) phonons and the plasmons (PL) has been studied by many authors in polar semiconductors. Such a mode was predicted to exist when the free carrier plasma frequency $\omega_{\mathrm{p}}$ is close to the LO phonon frequency $\omega_{\ell}{ }^{1-3)}$ The coupling gives rise to an upper $(\mathrm{L}_{+})$and a lower $(\mathrm{L}_{-})$branch in the dispersion relation of the coupled LO phonon-plasmon (LO-PL) mode (See Fig. 2). The first observation of the coupled mode was made by Mooradian and Wright $^{4)}$ at a wave number $q \sim 0$ by Raman scattering with the $1.06 \mu \mathrm{m}$ YAG laser line. The result was analyzed in terms of the phenomenological theory of light scattering by phonons with the dielectric constant modified by the presence of free carriers. ${ }^{5,6)}$

Recently Murase et al. ${ }^{7,8)}$ have made a Raman scattering measurement of the LO-PL mode in $n$-GaAs at several lines from an Ar-ion laser in a back scattering configuration. The variation of the peak position with incident laser wavelength and carrier concentration has led them to conjecture that the observed peak corresponds to the $\mathrm{L}_{-}$coupled LO-PL mode in the single particle excitation region. They also found from a careful study on the change of line shape that the peak is quite broad and strongly asymmetric. Raman spectra similar to those observed by Murase et al. have been recently obtained in InAs, ${ }^{9,10)} n$-InP and $n$-GaAs. ${ }^{11)}$ The most important feature of these experiments is that the momentum transfered from the light to the crystal can no longer be regarded as vanishingly small, so that local theories (assuming $q \sim 0$) for the coupled modes are not justified. Another important feature of the experiments is that the laser lights they are using are in the absorption region of crystal. This certainly invalidates the scattering theory on the assumption of a transparent medium.

The purpose of this paper is to develop and apply a non-local theory of Raman scattering from a coupled LO-PL mode in an absorptive medium. A particular attention is focused on the case of $n$-GaAs, where detailed experimental data by Murase et al. are available. The analysis shows that non-local effects are evident in the spectra. Our formalism provides a satisfactory picture on the response of the coupled carrier-LO phonon system as deduced from the spectral positions, line widths and line shape. A part of this work has been reported in a short note. ${ }^{12)}$ In $\S 2$ the Raman scattering theory in metals will be developed to obtain a formula for the Raman efficiency in an opaque semiconductor. This is expressed in terms of the correlation of the electronic susceptibility modulation through the atomic displacement and the induced electric field. In $\S 3$, the required correlation functions are calculated by the method of Green functions, starting from a Hamiltonian which contains the carrier-LO phonon interaction, the Coulomb interaction among the carriers and an anharmonic phonon

interaction. Section 4 will be devoted to an analysis of the GaAs spectra obtained by Murase et al. In §5, the results are summarized.

## §2. Raman Scattering from an Opaque Semiconductor
We adopt here the theory of Raman scattering developed for metals by Mills et al. $^{13)}$ and Inoue and Moriya. $^{14)}$ Suppose a semiconductor occupies a half space defined by $z<0$. For simplicity we neglect here all complexities associated with the surface layer region. Let an electromagnetic (EM) radiation of frequency $\omega_{0}$ be propagating in the $x$-$z$ plane and reflected in a back scattering geometry as shown in Fig. 1. In general, the quantity describing the electromagnetic response is the space- and time-dependent dielectric constant $\varepsilon(r, t)$. Here it is equal to unity for $z>0$ and to the dielectric constant of bulk medium for $z<0$. The latter consists of a background dielectric constant $\varepsilon=\varepsilon_{1}+i \varepsilon_{2}$ and a fluctuating part $4 \pi \alpha(r ; t)$ which generates the scattered light and gives rise to Raman effects.

![](./images/812268931921215492_1.jpg)

Fig. 1. Scattering geometry in which a semiconductor occupies the space $z<0$ with its surface on the $x$-$y$ plane. $\theta_{0}$ is the incident angle in the $x$-$z$ plane. $\theta_{\mathrm{s}}$ and $\varphi_{\mathrm{s}}$ define the scattering direction.

The differential scattering efficiency is defined as the fraction of photons scattered per solid angle per unit frequency interval. Its expression is $^{14)}$

$$
\begin{aligned}
\frac{1}{\Phi_{0}} \frac{\mathrm{d}^{2} \Phi}{\mathrm{d} \omega_{\mathrm{s}} \mathrm{d} \Omega_{\mathrm{s}}}= & 4 S \frac{\omega_{0}^{3} \omega_{\mathrm{s}}}{c^{4}} \frac{\cos \theta_{\mathrm{s}}}{\cos \theta_{0}} \int_{-\infty}^{\infty} \mathrm{d} \tau \mathrm{e}^{-i\left(\omega_{0}-\omega_{\mathrm{s}}\right) \tau}\left\langle\hat{\boldsymbol{e}}_{0} \cdot \tilde{\boldsymbol{C}}^{*} \cdot \tilde{\boldsymbol{\alpha}}^{*}\left(\boldsymbol{k}_{/ /}-\boldsymbol{k}_{0 / /}, k_{z}^{i}+k_{z}^{s} ; t\right)\right. \\
& \left.\times \tilde{\boldsymbol{G}}^{*}\left(\boldsymbol{k}_{/ /}, \omega_{\mathrm{s}}\right) \cdot \boldsymbol{G}\left(\boldsymbol{k}_{/ /}, \omega_{\mathrm{s}}\right) \cdot \boldsymbol{\alpha}\left(\boldsymbol{k}_{/ /}-\boldsymbol{k}_{0 / /}, k_{z}^{i}+k_{z}^{s} ; t+\tau\right) \cdot \boldsymbol{C} \cdot \hat{\boldsymbol{e}}_{0}\right\rangle,
\end{aligned}
\tag{2.1}
$$

where $S, \theta_{0}, \theta_{\mathrm{s}}, \omega_{0}$ and $\omega_{\mathrm{s}}$ are the area of the surface, the angles of incidence and scattered light and its frequencies, respectively; $\langle\rangle$ is the statistical average; $C, \hat{\boldsymbol{e}}_{0}$ and $\boldsymbol{G}\left(\boldsymbol{k}_{/ /}, \omega_{\mathrm{s}}\right)$ are the transfer function connecting the fields inside and outside of specimen, the polarization unit vector, and the two dimensional Fourier transform of the EM Green function $\boldsymbol{G}(\boldsymbol{r}, \boldsymbol{r}^{\prime}$, $\left.\omega_{\mathrm{s}}\right),{ }^{13,14)}$ respectively;

$$
\boldsymbol{\alpha}\left(\boldsymbol{q}_{/ /}, q_{z} ; t\right)=\frac{1}{S} \int_{z<0} \mathrm{~d} \boldsymbol{r} \mathrm{e}^{i q_{z} z-i \boldsymbol{q}_{/ /} \cdot \boldsymbol{r}} \boldsymbol{\alpha}(\boldsymbol{r} ; t),
\tag{2.2}
$$

$\boldsymbol{k}_{/ /}, \boldsymbol{k}_{0 / /}, k_{z}^{i}$ and $k_{z}^{s}$ are the components of wave vector parallel and normal to the surface.

Let us assume that the electronic susceptibility of semiconductor is modulated by atomic displacement as well as the induced electric field. Then we expand $\boldsymbol{\alpha}(\boldsymbol{r} ; t)$ in the vicinity of the lattice point $\chi^{0}(\ell)$ using normal coordinate of LO phonon $Q_{\boldsymbol{q}}$ and the induced electric field component $E_{\boldsymbol{q}}$. We retain the term corresponding to first order Raman process;

$$
\alpha_{\mu \nu}^{1}(\boldsymbol{r} ; t)=\sum_{\ell} \delta(\boldsymbol{r}-\boldsymbol{x}(\ell)) \alpha_{\mu \nu}^{1}(\boldsymbol{x}(\ell) ; t), \tag{2.3}
$$

$$
\begin{aligned}
\alpha_{\mu \nu}^{1}(\boldsymbol{x}(\ell) ; t)= & \sum_{\boldsymbol{q}}\left\{(\bar{M})^{-1 / 2} \sum_{\sigma} a_{\mu \nu}^{\sigma} \xi_{\boldsymbol{q}}^{\sigma} Q_{\boldsymbol{q}}\right. \\
& \left.+\sum_{\sigma} b_{\mu \nu}^{\sigma} \xi_{\boldsymbol{q}}^{\sigma} E_{\boldsymbol{q}}\right\} \mathrm{e}^{i \boldsymbol{q} \cdot \boldsymbol{x}^{0}(\ell)}, \quad(2.4)
\end{aligned}
$$

where $\mu, v, \sigma$ and $\ell$ denote the Cartesian components, the unit cell, respectively. The quantities $a_{\mu \nu}^{\sigma}$ and $b_{\mu \nu}^{\sigma}$ are the atomic displacement susceptibility tensor and the electrooptic tensor, $^{6)}$ respectively, $\bar{M}$ is the reduced mass density and $\xi_{\boldsymbol{q}}$ is the polarization vector of LO phonon. The Fourier component of the electric field is determined by the Poisson equation

$$
E_{\boldsymbol{q}}=-\frac{4 \pi e}{\varepsilon_{\infty}} \frac{1}{i q} \rho_{\boldsymbol{q}}-\left\{4 \pi\left(\varepsilon_{0}-\varepsilon_{\infty}\right)\right\}^{1 / 2} \frac{\omega_{t}}{\varepsilon_{\infty}} Q_{\boldsymbol{q}}, \quad(2.5)
$$

$\omega_{t}, \rho_{\boldsymbol{q}}, \varepsilon_{0}$ and $\varepsilon_{\infty}$ being the transverse optical (TO) phonon frequency, the density fluctuation of carriers, static and optical dielectric constants, respectively. Inserting eq. (2.3) into eq. (2.1) we find the expression of the differential Raman efficiency with the use of correlation functions;

$$
\frac{1}{\Phi_{0}} \frac{\mathrm{d}^{2} \Phi}{\mathrm{d} \omega_{\mathrm{s}} \mathrm{d} \Omega_{\mathrm{s}}}=\frac{\omega_{0}^{3} \omega_{\mathrm{s}}}{c^{4}} \frac{\cos \theta_{\mathrm{s}}}{\cos \theta_{0}} \frac{4}{\bar{M}} A\left(\omega_{0}-\omega_{\mathrm{s}}\right), \quad(2.6)
$$

where the function $A(\omega)$ is given by
$$
\begin{aligned}
A(\omega)= & \frac{1}{2 \pi} \int_{0}^{\infty} \frac{\mathrm{d} q}{\left|q-\left(k_{z}^{i}+k_{z}^{s}\right)\right|^{2}} \sum_{\alpha} \sum_{\beta \gamma \delta} \sum_{\beta^{\prime} \gamma^{\prime} \delta^{\prime}}\left(C_{\gamma^{\prime}} \hat{e}_{0 \gamma^{\prime}}\right)^{*} G_{\beta^{\prime} \alpha}^{*}\left(\boldsymbol{k}_{/ /}, \omega_{\mathrm{s}}\right) G_{\alpha \beta}\left(\boldsymbol{k}_{/ /}, \omega_{\mathrm{s}}\right)\left(C_{\gamma} \hat{e}_{0 \gamma}\right) \xi_{q}^{\delta^{\prime} *} \xi_{q}^{\delta} \\
& \times \int_{-\infty}^{\infty} \mathrm{d} \tau \mathrm{e}^{-i \omega \tau}\left[L_{\gamma^{\prime} \beta^{\prime}}^{\delta^{\prime} *} L_{\beta \gamma}^{\delta}\left\langle Q_{q}^{+}(t) Q_{q}(t+\tau)\right\rangle+\frac{4 \pi \bar{M}}{\varepsilon_{\infty}} \frac{4 \pi e^{2}}{q^{2} \varepsilon_{\infty}} b_{\gamma^{\prime} \beta^{\prime}}^{\delta^{\prime} *} b_{\beta \gamma}^{\delta}\left\langle\rho_{q}^{+}(t) \rho_{q}(t+\tau)\right\rangle\right. \\
& \left.+i \frac{4 \pi e}{q \varepsilon_{\infty}} \bar{M}^{1 / 2}\left\{L_{\gamma^{\prime} \beta^{\prime}}^{\delta^{\prime} *} b_{\beta \gamma}^{\delta}\left\langle Q_{q}^{+}(t) \rho_{q}(t+\tau)\right\rangle-b_{\gamma^{\prime} \beta^{\prime}}^{\delta^{\prime} *} L_{\beta \gamma}^{\delta}\left\langle\rho_{q}^{+}(t) Q_{q}(t+\tau)\right\rangle\right\}\right],
\end{aligned}
\tag{2.7}
$$
with
$$
L_{\beta \gamma}^{\delta}=a_{\beta \gamma}^{\delta}-b_{\beta \gamma}^{\delta}\left(\frac{4 \pi \bar{M}}{\varepsilon_{\infty}}\right)^{1 / 2}\left(\omega_{\ell}^{2}-\omega_{\tau}^{2}\right)^{1 / 2}.
$$

In the above equation we assumed that the coupled mode is excited along the direction (z-axis) normal to the surface. The wave number dependence of the correlation functions repre- sents the non-local character of the scattering excitation.

§3. Coupled System of Carriers, LO Phonons and Plasmons in Polar Semiconductor

In order to calculate the correlation functions appearing in eq. (2.7) we investigate the following Green functions;
$$
\left\langle\left\langle Q_{\boldsymbol{q}}^{+}(t) ; Q_{\boldsymbol{q}}(0)\right\rangle\right\rangle=D_{Q Q}(\boldsymbol{q}, t), \quad(3.1 \mathrm{a})
$$

$$
\left\langle\left\langle c_{\boldsymbol{k} \sigma}^{+} c_{\boldsymbol{k}-\boldsymbol{q} \sigma}(t) ; Q_{\boldsymbol{q}}(0)\right\rangle\right\rangle=G_{\rho Q}(\boldsymbol{q}, t), \quad(3.1 \mathrm{~b})
$$

$$
\left\langle\left\langle c_{\boldsymbol{k} \sigma}^{+} c_{\boldsymbol{k}-\boldsymbol{q} \sigma}(t) ; \rho_{\boldsymbol{q}}(0)\right\rangle\right\rangle=G_{\rho \rho}(\boldsymbol{q}, t), \quad(3.1 \mathrm{c})
$$

$$
\left\langle\left\langle Q_{\boldsymbol{q}}^{+}(t) ; \rho_{\boldsymbol{q}}(0)\right\rangle\right\rangle=D_{Q \rho}(\boldsymbol{q}, t), \quad(3.1 \mathrm{~d})
$$
with
$$
\rho_{\boldsymbol{q}}=\sum_{\boldsymbol{k}, \sigma} c_{\boldsymbol{k} \sigma}^{+} c_{\boldsymbol{k}+\boldsymbol{q} \sigma}.
$$

Here we have used the notation:
$$
\begin{aligned}
F_{A B}(\boldsymbol{q}, t) & =\left\langle\left\langle A_{\boldsymbol{q}}(t) ; B_{\boldsymbol{q}}(0)\right\rangle\right\rangle \\
& =-i \frac{\theta(t)}{\hbar}\left\langle\left[A_{\boldsymbol{q}}(t), B_{\boldsymbol{q}}(0)\right]\right\rangle, \quad(3.2)
\end{aligned}
$$
where $A(t)=e^{i H t / \hbar} A e^{-i H t / \hbar}, \theta(t)$ denotes the Heviside step function. By the fluctuation-dissipation theorem the correlation function is connected with the two time Green function. $^{15)}$

To evaluate the above Green functions we use the following Hamiltonian;
$$
\begin{aligned}
H= & \sum_{\boldsymbol{k}, \sigma} E_{\boldsymbol{k}} c_{\boldsymbol{k} \sigma}^{+} c_{\boldsymbol{k} \sigma}+\frac{1}{2} \sum_{\boldsymbol{q}}\left(P_{\boldsymbol{q}}^{+} P_{\boldsymbol{q}}+\omega_{\ell}^{2} Q_{\boldsymbol{q}}^{+} Q_{\boldsymbol{q}}\right) \\
& +\sum_{\boldsymbol{q}, \boldsymbol{k}, \sigma} V(q) c_{\boldsymbol{k}+\boldsymbol{q} \sigma}^{+} c_{\boldsymbol{k} \sigma} Q_{\boldsymbol{q}}+\frac{1}{2} \sum_{\boldsymbol{q}, \boldsymbol{k}, \boldsymbol{k}^{\prime} \sigma, \sigma^{\prime}} \frac{4 \pi e^{2}}{q^{2} \varepsilon_{\infty}} \\
& × c_{\boldsymbol{k}+\boldsymbol{q} \sigma}^{+} c_{\boldsymbol{k}^{\prime}-\boldsymbol{q} \sigma^{\prime}}^{+} c_{\boldsymbol{k}^{\prime} \sigma^{\prime}} c_{\boldsymbol{k} \sigma}+H_{A}, \quad(3.3)
\end{aligned}
$$
with
$$
E_{\boldsymbol{k}}=\frac{\hbar^{2} k^{2}}{2 m^{*}},
$$
and
$$
V(q)=i \omega_{\ell} \frac{\sqrt{4 \pi} e}{q^{2}}\left(\frac{1}{\varepsilon_{\infty}}-\frac{1}{\varepsilon_{0}}\right)^{1 / 2}(\boldsymbol{q} \cdot \boldsymbol{\xi}).
$$

Here, $c_{\boldsymbol{k} \sigma}^{+}, c_{\boldsymbol{k} \sigma}$ and $P_{\boldsymbol{q}}$ are the creation and an nihilation operators of electrons and the canonical conjugate momentum to $Q_{q}$, respec- tively. The Coulomb and Fröhlich interactions have been assumed for the electron-electron and electron-LO phonon interactions, respectively. The last term $H_{A}$ in eq. (3.3) describes an harmonic interaction of phonons. Using eqs. (3.1) and (3.3) with the Fourier transform of the Green function
$$
F_{A B}(\boldsymbol{q}, \omega)=\int_{-\infty}^{\infty} \frac{\mathrm{d} t}{2 \pi} F_{A B}(\boldsymbol{q}, t) \mathrm{e}^{i \omega t}, \quad(3.4)
$$
one finds the equation of motion for $D_{Q Q}(q, \omega)$ :
$$
\left(\omega^{2}-\omega_{\ell}^{2}\right) D_{Q Q}(\boldsymbol{q}, \omega)-V(\boldsymbol{q}) \sum_{\boldsymbol{k}, \sigma} G_{\rho Q}(\boldsymbol{k}, \boldsymbol{k}-\boldsymbol{q}, \omega)-\frac{i}{\hbar} \mathscr{G}_{A}(\boldsymbol{q}, \omega)=\frac{1}{2 \pi}, \tag{3.5}
$$
where we introduced
$$
\mathscr{G}_{A}(\boldsymbol{q}, \omega)=\int_{-\infty}^{\infty} \frac{\mathrm{d} t}{2 \pi}\left\langle\left\langle\left[P_{\boldsymbol{q}}, H_{A}\right](t) ; Q_{\boldsymbol{q}}(0)\right\rangle\right\rangle \mathrm{e}^{i \omega t}. \tag{3.6}
$$

$\mathscr{G}_{A}(q, \omega)$ is the contribution of the lattice anharmonicity. In a similar way, the equation of motion for $G_{\rho Q}(k, k-q, \omega)$ is obtained as

$$
\begin{aligned}
\left(E_{\boldsymbol{k}}-E_{\boldsymbol{k}-\boldsymbol{q}}-\hbar \omega\right) G_{\rho Q}(\boldsymbol{k}, \boldsymbol{k}-\boldsymbol{q}, \omega)-\frac{4 \pi e^{2}}{q^{2} \varepsilon_{\infty}} & \left(n_{\boldsymbol{k} \sigma}-n_{\boldsymbol{k}-\boldsymbol{q} \sigma}\right) \sum_{\boldsymbol{k}, \sigma} G_{\rho Q}(\boldsymbol{k}, \boldsymbol{k}-\boldsymbol{q}, \omega) \\
& =V(-\boldsymbol{q})\left(n_{\boldsymbol{k} \sigma}-n_{\boldsymbol{k}-\boldsymbol{q} \sigma}\right) D_{Q Q}(\boldsymbol{q}, \omega),
\end{aligned}
$$

where $n_{\boldsymbol{k} \sigma}=\left\langle c_{\boldsymbol{k} \sigma}^{+} c_{\boldsymbol{k} \sigma}\right\rangle$. In deriving eqs. (3.5) and (3.7), we used the decoupling corresponding to random phase approximation (RPA). If we approximate $\mathscr{G}_{A}(\boldsymbol{q}, \omega)$ as

$$
\mathscr{G}_{A}(\boldsymbol{q}, \omega)=i \hbar \omega \Sigma(\boldsymbol{q}, \omega) D_{Q Q}(\boldsymbol{q}, \omega),
$$

with $\Sigma(\boldsymbol{q}, \omega)=\Pi(\boldsymbol{q}, \omega)+i \Gamma_{A}$, the above coupled equations can be solved in a closed form as

$$
D_{Q Q}(\boldsymbol{q}, \omega)=\frac{1}{2 \pi} \frac{1}{\omega^{2}-\tilde{\omega}_{\ell}^{2}+i \omega \Gamma_{A}-|V(\boldsymbol{q})|^{2} \chi(\boldsymbol{q}, \omega)},
$$

with

$$
\tilde{\omega}_{\ell}^{2}=\omega_{\ell}^{2}-\omega \Pi(\boldsymbol{q}, \omega),\quad (3.10a)
$$

$$
\chi(\boldsymbol{q}, \omega)=\frac{q^{2} \varepsilon_{\infty}}{4 \pi e^{2}}\left\{\frac{1}{\varepsilon(\boldsymbol{q}, \omega)}-1\right\}.\quad (3.10b)
$$

In eq. (3.10b) $\varepsilon(\boldsymbol{q}, \omega)$ is the electronic dielectric function in RPA, given by

$$
\varepsilon(\boldsymbol{q}, \omega)=1-\frac{4 \pi e^{2}}{q^{2} \varepsilon_{\infty}} \sum_{\boldsymbol{k}, \sigma} Q(\boldsymbol{k}, \boldsymbol{k}-\boldsymbol{q}, \omega),
$$

with

$$
Q(\boldsymbol{k}, \boldsymbol{k}-\boldsymbol{q}, \omega)=\frac{n_{\boldsymbol{k} \sigma}-n_{\boldsymbol{k}-\boldsymbol{q} \sigma}}{E_{\boldsymbol{k}}-E_{\boldsymbol{k}-\boldsymbol{q}}-\hbar \omega}.
$$

The solution for $G_{\rho Q}(\boldsymbol{k}, \boldsymbol{k}-\boldsymbol{q}, \omega)$ is given by

$$
G_{\rho Q}(\boldsymbol{k}, \boldsymbol{k}-\boldsymbol{q}, \omega)=\frac{Q(\boldsymbol{k}, \boldsymbol{k}-\boldsymbol{q}, \omega)}{\varepsilon(\boldsymbol{q}, \omega)} V(-\boldsymbol{q}) D_{Q Q}(\boldsymbol{q}, \omega).
$$

Proceeding in a similar way, we obtain the other set of the Green functions; $G_{\rho \rho}(\boldsymbol{k}, \boldsymbol{k}-\boldsymbol{q}, \omega)$ and $D_{Q \rho}(\boldsymbol{q}, \omega)$ as

$$
G_{\rho \rho}(\boldsymbol{k}, \boldsymbol{k}-\boldsymbol{q}, \omega)=\frac{Q(\boldsymbol{k}, \boldsymbol{k}-\boldsymbol{q}, \omega)}{1-\frac{4 \pi e^{2}}{q^{2} \varepsilon_{\infty}} \frac{\omega^{2}-\tilde{\omega}_{\mathrm{t}}^{2}+i \omega \Gamma_{A}}{\omega^{2}-\tilde{\omega}_{\ell}^{2}+i \omega \Gamma_{A}} \sum_{\boldsymbol{k}, \sigma} Q(\boldsymbol{k}, \boldsymbol{k}-\boldsymbol{q}, \omega)},\quad (3.14)
$$

$$
D_{Q \rho}(\boldsymbol{q}, \omega)=V(q) \sum_{\boldsymbol{k}, \sigma} \frac{G_{\rho \rho}(\boldsymbol{k}, \boldsymbol{k}-\boldsymbol{q}, \omega)}{\omega^{2}-\tilde{\omega}_{\ell}^{2}+i \omega \Gamma_{A}}.\quad (3.15)
$$

## §4. Analysis of Experimental Results of $n$-GaAs

Let us analyze the experimental results of $n$-GaAs $^{7,8)}$ on the basis of the theory developed in previous sections. Using eqs. (3.9), (3.13), (3.14) and (3.15) with the fluctuation-dissipation theorem, we have the function $A(\omega)$ in eq. (2.7) as

$$
\begin{aligned}
A(\omega)= & \frac{\hbar}{\omega_{\ell}} \int_{0}^{\infty} \mathrm{d} q \frac{n_{q}(\omega)+1}{(q-\langle q\rangle)^{2}+(\Delta q)^{2}} \sum_{\alpha}\left|G_{\alpha y}\left(k_{/ /}, \omega_{s}\right)\right| \varepsilon_{y x z} | \\
& \times \underbrace{\left(a+b\left(\omega_{\mathrm{t}}^{2}-\omega^{2}\right)\left(\frac{4 \pi \bar{M}}{\varepsilon_{\infty}\left(\omega_{\ell}^{2}-\omega_{\mathrm{t}}^{2}\right)}\right)^{1 / 2}\right)} \hat{\varepsilon}_{q}^{z} C_{x} \hat{e}_{0 x} \mid{ }^{2} J(q, \omega).
\end{aligned}
$$

Here we took $\langle q\rangle=\operatorname{Re}\left(k_{z}^{s}+k_{z}^{i}\right)$ and $\Delta q=\operatorname{Im}\left(k_{z}^{s}+k_{z}^{i}\right)$. The momentum transferred to excitation will be $\left(k_{z}^{s}+k_{z}^{i}\right) \simeq 2(2 \pi / \lambda)(N+i K)$ where $\lambda$ is the wavelength in vacuum; $N$ and $K$ are the real and imaginary parts of refractive index, respectively. The quantities $a_{y x}^{z}, b_{y x}^{z}$ can be written as $a\left|\varepsilon_{y x z}\right|$ and $b\left|\varepsilon_{y x z}\right|$ in ZnS structure, where we have chosen the coordinate axis as $x / /\langle 100\rangle, y / /\langle 010\rangle$ and $z / /\langle 001\rangle$ crystalline directions; $\varepsilon_{y x z}$ is the Levi-Civita symbol. The

function $J(q, \omega)$ in the integrand of eq. (4.1) is the phonon spectral density function defined as
$$J(q, \omega)=-2 \omega_{\ell} \operatorname{Im} D_{Q Q}(q, \omega), \quad (4.2)$$
which was shown as functions of $q$ and $\omega$ in Landau damping region for $n$-GaAs in ref. 12. In Fig. 2 the peak positions estimated from $J(q, \omega)$ are plotted as functions of wave number for carrier density $n=8.4 \times 10^{17} \mathrm{~cm}^{-3}$. These curves represent the dispersion of the LO-PL modes. The effective mean wave number $\langle q\rangle$ and its spreading $\Delta q$ for each laser line $(5145 \mathring{A}$, $4880 \mathring{A}$ and $4765 \mathring{A}$) are estimated with the complex refractive index. $^{16)}$ The values are listed in Table I. As seen in Fig. 2 the frequencies of $L_{-}$ mode at $\langle q\rangle$ agree with the observed peak positions of Raman spectra. This strongly suggests that the observed lines are due to the LO-PL mode. Further, the peak positions show that the observed modes extend into the single particle excitation region. In this region a single particle excitation could be resonantly emitted or absorbed by the LO-PL mode through the carrier-LO phonon coupling. This gives rise to broad spectral lines as was observed.

![](./images/812268931921215492_2.jpg)

Fig. 2. The dispersion relations of the coupled LO-PL modes. The hached lines correspond to $\omega_{s}$ $=\pm q v_{\mathrm{F}}+(\hbar q^{2} / 2 m^{*})$. The full circles $\bigcirc$ show the observed peak positions of Raman spectra at mean wave number $\langle q\rangle$.

<table>
<caption>Table I. Numerical values of $\langle q\rangle$, $\Delta q$ and $\delta(\equiv(\Delta q)^{-1})$.</caption>
<thead>
<tr>
<th>Wave length</th>
<th>$\langle q\rangle$ $10^{6}(\mathrm{cm}^{-1})$</th>
<th>$\Delta q$ $10^{5}(\mathrm{cm}^{-1})$</th>
<th>$\delta(\mathring{A})$</th>
</tr>
</thead>
<tbody>
<tr>
<td>$5145 \mathring{A}$</td>
<td>1.050</td>
<td>0.833</td>
<td>1200</td>
</tr>
<tr>
<td>$4880 \mathring{A}$</td>
<td>1.156</td>
<td>1.015</td>
<td>985</td>
</tr>
<tr>
<td>$4765 \mathring{A}$</td>
<td>1.205</td>
<td>1.108</td>
<td>903</td>
</tr>
</tbody>
</table>

### 4.1 Comparison of calculated and experimental line shape

A line shape function $g(\omega)$ is defined from eq. (4.1) as
$$
\begin{aligned}
g(\omega)= & \left(1+D \frac{\omega_{\mathrm{t}}^{2}-\omega^{2}}{\omega_{\mathrm{t}}^{2}}\right)^{2} \frac{\pi \omega_{\ell}^{2}}{2 v_{\mathrm{F}}} \\
& × \int_{0}^{\infty} \mathrm{d} q \frac{n_{q}(\omega)+1}{(q-\langle q\rangle)^{2}+(\Delta q)^{2}} J(q, \omega), \quad (4.3)
\end{aligned}
$$
where $v_{\mathrm{F}}$ is the Fermi velocity,
$$
D=\frac{b}{a}\left[\frac{4 \pi \bar{M}}{\varepsilon_{\infty}\left(\omega_{\ell}^{2}-\omega_{\mathrm{t}}^{2}\right)}\right]^{1 / 2} \omega_{\mathrm{t}}^{2}.
$$

In Fig. 3(a), (b) and (c), the line shape functions $g(\omega)$ calculated under the assumption of $T=0$ K are plotted as functions of Raman shift

![](./images/812268931921215492_3.jpg)

Fig. 3. Calculated and observed line shape functions vs Raman shift for three different wavelengths at three different carrier densities.

$\omega=\omega_{0}-\omega_{\mathrm{s}}$ in full lines. The values of $\langle q\rangle$ and $\Delta q$ for computations are taken from Table I, and the value $D=-2.795$ is assumed. The effective mass $m^{*}=0.0775 \mathrm{~m}, 0.080 \mathrm{~m}$ and $0.083 \mathrm{~m}$ are taken for $n=8.4 \times 10^{17} \mathrm{~cm}^{-3}$, $2 \times 10^{18} \mathrm{~cm}^{-3}$ and $4.5 \times 10^{18} \mathrm{~cm}^{-3}$, respectively. The band nonparabolicity effect is contained in the effective mass. $^{17)}$ The observed spectra obtained at $100 \mathrm{~K}$ are also plotted in broken lines, whose heights are adjusted so that the calculated and observed peak heights agree with each other. The increment of the electron temperature by the laser light was suppressed less than $50 \mathrm{~K}$.

In Fig. 3(a), (b) and (c) we observe that:
(a) The agreement of peak positions with experiment is fairly good. The shift of the peak position with wavelengths is consistent with the dispersion relation of the $\mathrm{L}_{-}$mode as is seen in Fig. 2.
(b) The tendency of the narrowing of spectral linewidths with the increase of concentration is consistent with experiment. However, the calculated line is narrower than the observed one.
(c) The features of the asymmetry of the spectral line agree with the experiment. In particular, the agreement is very good for $n=8.4 \times 10^{17} \mathrm{~cm}^{-3}$.
(d) The $\mathrm{S}$ band which is observed at high frequency edge is reproduced in the calculation, though the intensity is only half of the observed one.

Now we examine in detail the contribution of individual effects to the resultant overall line shape shown in Fig. 3.
(A) Width due to the carrier-LO phonon interaction.

Let us first discuss the phonon spectral density function $J(q, \omega)$ in the integrand of eq. (4.3). Neglecting lattice anharmonicity, the phonon spectral density becomes
$$
J(q, \omega)=\frac{\omega_{\ell}}{\pi} \frac{\omega \Gamma(q, \omega)}{\left(\omega^{2}-\omega_{\ell}^{2}-|V(q)|^{2} \operatorname{Re} \chi(q, \omega)\right)^{2}+\omega^{2} \Gamma^{2}(q, \omega)},
$$
where $\chi(q, \omega)$ is defined in eq. (3.10b). The width of the phonon spectral line is found from $\chi(q, \omega)$ to be
$$
\Gamma(q, \omega)=\frac{\pi}{\omega}\left|\frac{V(q)}{\varepsilon(q, \omega)}\right|^{2} \sum_{\boldsymbol{k} \sigma}\left(n_{\boldsymbol{k} \sigma}-n_{\boldsymbol{k}-q \sigma}\right) \delta\left(E_{\boldsymbol{k}}-E_{\boldsymbol{k}-\boldsymbol{q}}-\hbar \omega\right).
$$

In Fig. 4, we plot the phonon spectral density function for the wave number corresponding to $5145 \AA$. The full, broken and broken-dotted lines show the curves for $n=4.5 \times 10^{18} \mathrm{~cm}^{-3}$, $2 \times 10^{18} \mathrm{~cm}^{-3}$ and $8.4 \times 10^{17} \mathrm{~cm}^{-3}$, respectively. The horizontal bars and full circles represent the experimental widths and peak positions, respectively. The above calculation indicates that the observed broad linewidth is mainly due to the damping of the LO-PL mode through the resonant electron-LO phonon coupling. However, the predicted asymmetry is in the opposite direction to that of the experiment.

![](./images/812268931921215492_4.jpg)

Fig. 4. Phonon spectral densities as functions of frequencies for three different carrier densities. The open circles $\bigcirc$ and horizontal error bars represent the observed peak positions and the full line widths at half maxima, respectively.

(B) Interference effect between two scattering mechanisms.

Next we consider the origin of the asymmetry of line shape. The proportionality factor before the integral in eq. (4.3)
$$
\left(1+D \frac{\omega_{\mathrm{t}}^{2}-\omega^{2}}{\omega_{\mathrm{t}}^{2}}\right)^{2}
$$
arises from the contribution from the scatterings due to atomic displacement and electro-

optic process. Recent theoretical $^{18)}$ and experi mental studies $^{19)}$ suggest that $a>0$ and $b<0$ for GaAs at the frequency of our interest. We use in the following analysis the numerical values obtained by Mooradian and Mc-Whorter $^{5)}$

$$|a|=6.4 \times 10^{7} \mathrm{~cm}^{-1} \text { and }|b|=8.4 \times 10^{-7} \text { esu. }$$

From the product of eq. (4.6) and $J(q, \omega)$, we define the functions
$$J_{\mathrm{T}}(q, \omega)=J(q, \omega)+J_{2}(q, \omega)+J_{3}(q, \omega), \quad(4.7)$$
where
$$J_{2}(q, \omega)=2 D \frac{\omega_{\mathrm{t}}^{2}-\omega^{2}}{\omega_{\mathrm{t}}^{2}} J(q, \omega),$$
and
$$J_{3}(q, \omega)=D^{2}\left(\frac{\omega_{\mathrm{t}}^{2}-\omega^{2}}{\omega_{\mathrm{t}}^{2}}\right)^{2} J(q, \omega).\qquad(4.8)$$

The function $J_{2}(q, \omega)$ represents the inter ference effect between the two scattering mechanisms. Figure 5 shows the functions $J_{T}(q, \omega), J_{2}(q, \omega)$ and $J_{3}(q, \omega)$ for wave number $q=1.05 ×10^{6} ~cm^{-1}$ . The term $J_{3}(q, \omega)$  is very small compared with the phonon response term $J(q, \omega)$ . It is seen from the varia tion of $J_{2}(q, \omega)$ that the two scattering mecha nisms interfere destructively at frequencies below $\omega_{t}$ and constructively at frequencies above $\omega_{t}$ . The solid lines represent the total spectral density function. This exhibits precisely the behavior of the observed Raman spectra whose peak position and width are indicated by a horizontal bar and a full circle, respectively.

![](./images/812268931921215492_5.jpg)

Fig. 5. Interference effect in the phonon spectral density. The function $J_{2}(q, \omega)$ and $J_{3}(q, \omega)$ are calculated from eq. (4.8).

![](./images/812268931921215492_6.jpg)

Fig. 6. Phonon spectral density $J(q, \omega)$ (a) and line shape function $g(\omega)$ (b). Full and broken lines represent curves with and without the interference effect.

### (C) Distribution of transferred momentum.
Finally, we show the effect of the distribution of transferred momentum on the line shape by comparing $J(q, \omega)$ with $g(\omega)$ which includes the effect of the distribution of momentum. In Fig. 6 these functions are plotted for carrier density $8.4 ×10^{17} ~cm^{-3}$ . The broken lines represent the curves without interference. The peak shift due to the distribution of transferred momentum is small. The width of $g(\omega)$ is about twice that of the phonon spectral density J(q, w). Another important effect due to the distribution of momentum is the appearence of a small $S$ -band. As was predicted by Murase et al. $^{8)}$ the $S$ -band comes from the LO-PL mode at large wave numbers where density of state of phonon is high, and is enhanced by the inter- ference effect.

### 4.2 Evaluation of the integrated Raman effi- ciency
The integrated scattering efficiency of the LO-PL mode ( $B$ band and $S$ band) is estimated as
$$S=\frac{\omega_{0}^{3} \omega_{\mathrm{s}}}{c^{4}} \frac{4 \hbar a^{2}}{\bar{M} \omega_{\ell}} I\left(\theta_{0}\right) \frac{2 v_{\mathrm{F}}}{\pi \omega_{\ell}^{2}} \int_{S+B} g(\omega) \mathrm{d} \omega. \quad(4.9)$$

Here the reduction factor $I(\theta_{0})$ is obtained by using the EM Green function components andthe transfer function components $^{14)}$ as follows;

$$
I\left(\theta_{0}\right)=\frac{4\left|\varepsilon-\sin ^{2} \theta_{0}\right||\varepsilon|(\omega / c)^{2} \cos \theta_{\mathrm{s}} \cos \theta_{0}}{\left|\left(\varepsilon-\sin ^{2} \theta_{0}\right)^{1 / 2}+\varepsilon \cos \theta_{0}\right|^{2}\left|\varepsilon-\sin ^{2} \theta_{\mathrm{s}}\right||i(\omega / c)(1-\sqrt{\bar{\varepsilon}})|^{2}}.
\tag{4.10}
$$

The maximum of $I(\theta_{0})$ is realized at the Brewster angle. The values of $I(\theta_{0})$ are given in Table II for the experimental incident angle $\theta_{0}=80^{\circ}$. Using these values we estimate the integrated Raman efficiency from eq. (4.9). The numerical integrations give an integrated efficiency of the order of $\sim 10^{-11}$. Detail numerical values are summarized in Table II.

It was reported by Murase et al. $^{7)}$ that the $B$-band for the samples with low concentration $n \leq 5.5 \times 10^{17} \mathrm{~cm}^{-3}$ was not observed near the TO phonon frequency. To explore the origin for the disappearence of the $B$-band we briefly discuss the dependence of the efficiency on the carrier density. In Fig. 7 we plotted the calculated relative integrated efficiencies normalized at $2 \times 10^{18} \mathrm{~cm}^{-3}$ as functions of carrier density. The open circles show the experimental values for each concentrations corrected by taking into account the change of the thickness of the depletion layer. It is noteworthy that the calculated efficiency shows the marked decrease below $n \sim 10^{18} \mathrm{~cm}^{-3}$. This is due to the strong interference effect of two scattering mechanisms discussed in (B) as well as due to the interchange of the excitation strengths of $L_{-}$ mode and of upper $\mathrm{L}_{+}$mode. On the other hand, the large discrepancy between calculation and experiment is seen at $n=4.5 \times 10^{18} \mathrm{~cm}^{-3}$. These have not been explained from the effects considered in this work. In this analysis the electro-optic tensor $a_{\beta \gamma}^{\delta}$ is regarded as a constant. The discrepancy would be improved if the values of $a_{\beta \gamma}^{\delta}$ was assumed to be reduced with the increase of carrier density. The possibility of the reduction of $a_{\beta \gamma}^{\delta}$ due to high doping will come from the Burstein shift $^{20)}$ or the increase of the band gap energy due to the electron-electron interaction. $^{21)}$

Table II. Integrated Raman efficiencies $S_{1}, S_{2}$ and $S_{3}$; the reduction factor $I(\theta_{0})$. $S_{1}, S_{2}$ and $S_{3}$ correspond to $n=8.4 \times 10^{17} \mathrm{~cm}^{-3}, 2 \times 10^{18} \mathrm{~cm}^{-3}$ and $4.5 \times 10^{18} \mathrm{~cm}^{-3}$, respectively.

<table>
<thead>
<tr>
<th></th>
<th>$I(\theta_{0})$
$(\times 10^{-2})$</th>
<th>$S_{1}$
$(\times 10^{-11})$</th>
<th>$S_{2}$
$(\times 10^{-11})$</th>
<th>$S_{3}$
$(\times 10^{-11})$</th>
</tr>
</thead>
<tbody>
<tr>
<td>$5145\mathring{A}$</td>
<td>1.10</td>
<td>1.945</td>
<td>3.205</td>
<td>3.810</td>
</tr>
<tr>
<td>$4880\mathring{A}$</td>
<td>0.98</td>
<td>2.067</td>
<td>2.942</td>
<td>3.418</td>
</tr>
<tr>
<td>$4765\mathring{A}$</td>
<td>0.92</td>
<td>2.129</td>
<td>2.867</td>
<td>3.238</td>
</tr>
</tbody>
</table>

![](./images/812268931921215492_7.jpg)

Fig. 7. Integrated scattering efficiencies normalized at $2 \times 10^{18} \mathrm{~cm}^{-3}$ as functions of carrier densities. The open circles $\bigcirc$ indicate the integrated relative intensities by the experiment.

## §5. Conclusions
We have developed a non-local theory of light scattering from a coupled LO-PL mode in highly doped polar semiconductors. We regard the carriers in doped semiconductors to form an interacting electron gas embedded in a polarizable medium consisting of the lattice and valence electrons. The theory takes account of the strong carrier-LO phonon interaction, the Coulomb interactions between the carriers, and the attenuation of light in the crystal. Theory is then applied to an analysis of the Raman spectra in GaAs. From this analysis, we have seen;

(1) The theory reproduces most of the important aspects of the observed spectra including the line position, the linewidth and the line shape. It is demonstrated that the asymmetry of the lines result from an interference between the atomic displacement and electro-optic processes.
(2) At carrier density $\sim 10^{18} \mathrm{~cm}^{-3}$ the lower branch of the LO-PL mode $(L_{-})$ persists as a fairly well defined excitation even in the Landau damping region.
(3) The theory predicts an integrated scattering efficiency of the order of $10^{-11}$ for the LO-PL mode in GaAs. The predicted dependence on the carrier densities is in good

agreement with experimental results.

The above observations lead us to conclude that our theoretical model of LO-PL mode coupling provides a satisfactory understanding of the Raman spectra obtained in the absorp- tion region of the crystal. All the numerical computations in this paper have been confined to zero temperature. We have discussed in detail the finite temperature effects on Raman spectra by comparing the room temperature experiment with the calculation assuming $T=300 \mathrm{~K}.^{22)}$ The results show both an addi tional broadening and peak shift for $B$-band compared with that obtained assuming $T=0 \mathrm{~K}$. The calculated lines are narrower than the observed one as shown in Fig. 3. To get more excellent agreement, the actual temperature effect have to be included in the computations. It should be emphasized, however, that the essential parts of the contributions for the line shape are taken into account in this paper.

## Acknowledgements

We would like to express thanks to Profes- sors H. Kawamura, J. Kanamori and K. Suzuki for their enlighting discussions and suggestions. We are also grateful to Professor I. Yokota for helpful discussions and sugges- tions. We thank Y. Ando for his participation in the experiment. The present work was sup- ported by the research bounty in memory of Yoshio Nishina.

## References

1) I. Yokota: J. Phys. Soc. Japan 16 (1961) 2075.
2) B. B. Varga: Phys. Rev. A137 (1965) 1896.
3) K. S. Singwi and M. P. Tosi: Phys. Rev. 147 (1966)658.
4) A. Mooradian and G. B. Wright: Phys. Rev. Letters 16 (1966) 999.
5) A. Mooradian and A. L. McWhorter: Phys. Rev. Letters 19 (1967) 849.
6) E. Burstein, A. Pinczuk and S. Iwasa: Phys. Rev.157 (1967) 611.
7) K. Murase, Y. Ando, H. Kawamura and S. Katayama: Proc. 12th Int. Conf. Phys. Semicond., ed. M. H. Pilkuhn (1974) p. 458.
8) K. Murase, S. Katayama, Y. Ando and H. Kawamura: Phys. Rev. Letters 33 (1974) 1481.
9) S. Buchner and E. Burstein: Phys. Rev. Letters 33(1974) 908.
10) E. L. Ivchenko, D. N. Mirlin and I. I. Reshina: Soviet Physics-Solid State 17 (1976) 1510.
11) V. I. Zemski, E. L. Ivchenko, D. N. Mirlin and I. I. Reshina: Solid State Commun. 16 (1975) 221.
12) S. Katayama, K. Murase and H. Kawamura: Solid State Commun. 16 (1975) 945.
13) D. L. Mills, A. A. Maradudin and E. Burstein: Phys. Rev. Letters 21 (1968) 1178.
14) M. Inoue and T. Moriya: J. Phys. Soc. Japan 29(1970) 117.
15) D. N. Zubarev: Soviet Physics-Uspekhi 3 (1960)320.
16) H. R. Philipp and H. Ehrenreich: Phys. Rev. 129(1963) 1550.
17) M. Cardona: Phys. Rev. 121 (1961) 752.
18) M. Cardona, F. Cerderia and T. A. Fjeldly: Phys. Rev. B10 (1974) 3433.
19) A. Mooradian and A. L. McWhorter: Proc. Int. Cof. on Light Scattering Spectra in Solids, ed. G. B. Wright (1969) p. 297.
20) E. Burstein: Phys. Rev. 93 (1953) 632.
21) J. C. Inkson: J. Phys. C9 (1976) 1177.
22) K. Murase, S. Katayama, H. Kawamura and Y. Ando: Progr. theor. Phys. 57 (1975) Suppl. p. 115.