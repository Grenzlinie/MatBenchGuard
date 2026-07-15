PHYSICAL REVIEW B 85, 033409 (2012)

# Exciton-phonon sidebands in metallic carbon nanotubes studied using semiconductor Bloch equations

Evgeny Bobkin, $^{*}$ Andreas Knorr, and Ermin Malic

Institut für Theoretische Physik, Nichtlineare Optik und Quantenelektronik, Technische Universität Berlin, Hardenbergstr. 36, 10623 Berlin, Germany

(Received 8 April 2011; revised manuscript received 29 September 2011; published 26 January 2012)

We use semiconductor Bloch equations to describe excitonic absorption spectra of metallic carbon nanotubes. In particular, we focus on the formation of exciton-phonon induced sidebands. Our approach is based on the density matrix formalism combining zone-folded tight-binding wave functions and electron-phonon coupling, allowing a straight-forward description of temporal and spectral many-body interactions. We observe clear excitonic features in the spectra of metallic carbon nanotubes in agreement with recent experimental and theoretical studies. Furthermore, depending on the temperature, we find significant exciton-phonon sidebands on both sides of the zero-phonon excitonic line. We investigate the polaronic shift and the transfer of the spectral weight to the sidebands for a variety of metallic nanotubes with different chiral angles and diameters.

DOI: 10.1103/PhysRevB.85.033409
PACS number(s): 78.67.Ch, 71.35.Cc, 63.22.Gh

## I. INTRODUCTION

Spectroscopic methods, such as absorption, Raman scattering, and Rayleigh, as well as photoluminescence are standard techniques to successfully characterize carbon nanotubes (CNTs). $^{1-4}$ The tubes show a variety of different semiconducting and metallic structures depending on their diameter and chiral angle, $^{3,4}$ resulting in a large application potential in optoelectronics. $^{4-6}$ Earlier experimental $^{7-10}$ and theoretical studies $^{11-24}$ have demonstrated the crucial importance of excitonic effects to understand the optical properties of CNTs. In an extension of these studies, the influence of exciton-phonon coupling on the optical spectra of CNTs has been investigated experimentally, $^{25-30}$ observing an increase of the exciton-phonon interaction with a decreasing CNT diameter. Perebeinos et al. $^{31}$ have theoretically demonstrated the formation of sidebands in semiconducting nanotubes based on the ab initio evolution of the Bethe-Salpether equation combined with the Su-Schrieffer-Heeger model. The comprehensive experimental data, in particular with respect to metallic carbon nanotubes, has not yet been complemented by theoretical studies. The purpose of our work is to close this gap by studying the exciton-phonon-induced formation of sidebands in the absorption spectra of a broad variety of metallic CNTs. Our approach is based on a many-body density matrix framework $^{32}$ yielding CNT Bloch equations, $^{16,17,33}$ allowing a microscopical description of excitonic absorption spectra of semiconducting and metallic CNTs of arbitrary chiral angle and with a wide range of diameters. Note that the zone-folded tight-binding wave functions can be inappropriate for nanotubes with small diameters, where hybridization effects might play an important role. $^{34}$

We perform calculations in an excitonic basis, in which the Bloch equations no longer contain the numerically demanding Coulomb interaction and the focus lies on the inclusion of exciton-phonon interaction. The approach presented here can be extended in a straight-forward way to other low-dimensional nanostructures, such as graphene or nanoribbons. $^{35-37}$

## II. THEORETICAL MODEL

The starting point of our model is represented by the Hamilton operator in the second quantization: $^{17,32,35}$

$$
\begin{aligned}
\mathcal{H}= & \mathcal{H}_{\text {free }}+\mathcal{H}_{\text {field }}+\mathcal{H}_{\text {carrier }} \\
& +\mathcal{H}_{\text {phonon }}+\mathcal{H}_{\text {carrier-phonon }}.
\end{aligned}
\tag{1}
$$

$\mathcal{H}_{\text {free }}$ is the free electron Hamiltonian containing the single particle energy $E_{l}(\mathbf{k})$:

$$
\mathcal{H}_{\text {free }}=\sum_{l \mathbf{k}} E_{l}(\mathbf{k}) a_{l \mathbf{k}}^{+} a_{l \mathbf{k}}.
\tag{2}
$$

Here, $a_{j}^{+}(a_{j})$ creates (annihilates) an electron in a given quantum state denoted by the compound index $j \equiv l, \mathbf{k}$ including the band index $l$ and the wave vector $\mathbf{k}$. The latter consists of a continuous component $z$ along the nanotube axis and a quantized subband index $m.^{3}$ To obtain a largely analytical description of the formation of exciton-phonon-induced sidebands in the absorption spectra of CNTs, we focus in this first study on the energetically lowest transition $E_{11}$. The band structure is calculated within the nearest-neighbors tight-binding approximation combined with a zone-folding method: $^{3}$ $E_{l}(\mathbf{k})=\frac{\lambda_{l} \gamma_{0}|e(\mathbf{k})|}{1+\lambda_{l} s_{0}|e(\mathbf{k})|}$, where $\lambda_{c}=-1, \lambda_{v}=+1$ and $e(\mathbf{k})=\sum_{j=1}^{3} \exp (i \mathbf{k} \cdot \mathbf{b}_{j})$ with the connecting vectors $\mathbf{b}_{j}$ indicating the direction and the distance of the nearest neighbor atoms. The tight-binding parameters $\gamma_{0}=-2.84$ and $s_{0}=0.07$ can be obtained from ab-initio calculations. $^{3}$ The second term of the Hamilton operator describes the carrier-light interaction with an applied electromagnetic field, described by the vector potential $\mathbf{A}(t)$:

$$
\mathcal{H}_{\text {field }}=i \hbar \frac{e_{0}}{m_{e}} \sum_{\substack{l_{1} l_{2} \\ \mathbf{k}}} \mathbf{A}(t) \cdot \mathbf{M}_{l_{1} l_{2}}(\mathbf{k}) a_{l_{1} \mathbf{k}}^{+} a_{l_{2} \mathbf{k}}.
\tag{3}
$$

Here, $e_{0}$ is the elementary charge and $m_{e}$ is the vacuum electron mass. The optical matrix element $\mathbf{M}_{l_{1} l_{2}}(\mathbf{k})$ is introduced via the relationship $\langle l_{1} \mathbf{k}_{1}|\mathbf{A}(t) \cdot \mathbf{p}| l_{2} \mathbf{k}_{2}\rangle=-i \hbar \mathbf{A}(t) \cdot$

1098-0121/2012/85(3)/033409(6)
033409-1
©2012 American Physical Society

$\mathbf{M}_{l_{1} l_{2}}(\mathbf{k}_{1}) \delta_{\mathbf{k}_{1}, \mathbf{k}_{2}}$, where $|l\mathbf{k}\rangle$ is a tight-binding state. $^{38}$ For the optical matrix elements we use an analytical expression: $^{39-41}$

$$
\begin{aligned}
\mathbf{M}_{l_{1} l_{2}}(\mathbf{k})= & \frac{2 \mathcal{M}}{\left|\mathbf{b}_{1}\right|} \sum_{j=1}^{3}\left\{C_{a}^{l_{1} *}(\mathbf{k}) C_{b}^{l_{2}}(\mathbf{k}) e^{i \mathbf{k} \cdot \mathbf{b}_{j}} \mathbf{b}_{j}\right. \\
& \left.-C_{b}^{l_{1} *}(\mathbf{k}) C_{a}^{l_{2}}(\mathbf{k}) e^{-i \mathbf{k} \cdot \mathbf{b}_{j}} \mathbf{b}_{j}\right\},
\end{aligned}
\tag{4}
$$

where $C_{a}^{l}=\lambda_{l} e(\mathbf{k}) /|e(\mathbf{k})| C_{b}^{l}(\mathbf{k})$ with $C_{b}^{l}(\mathbf{k})=$ $1 / \sqrt{2(1+\lambda_{l} s_{0}|e(\mathbf{k})|)}$. The constant parameter $\mathcal{M}$, representing the optical matrix strength between two carbon atoms, described by the hydrogen-like $2 p_{z}$ orbitals $\phi(\mathbf{r})$ and separated by $\mathbf{b}_{1}$, is defined as: $\mathcal{M}=\langle\phi(\mathbf{r}+|\mathbf{b}_{1}| \mathbf{e}_{x})|\partial_{x}| \phi(\mathbf{r})\rangle$. Here, $\mathbf{e}_{x}$ is a Cartesian unit vector in the $x$ direction. The third term in the Hamilton operator describes the Coulomb-induced carrier-carrier interaction

$$
\mathcal{H}_{\text {carrier }}=\frac{1}{2} \sum_{j_{1} j_{2} j_{3} j_{4}} V_{j_{3} j_{4}}^{j_{1} j_{2}} a_{j_{1}}^{+} a_{j_{2}}^{+} a_{j_{4}} a_{j_{3}}.
\tag{5}
$$

The carrier-carrier Coulomb matrix elements are calculated using the Bloch wave functions:

$$
\begin{aligned}
V_{\substack{l_{1} l_{2} l_{3} l_{4} \\
\mathbf{k}_{1} \mathbf{k}_{2} \mathbf{k}_{3} \mathbf{k}_{4}}}= & \mathcal{A}_{\substack{l_{1} l_{3} \\
\mathbf{k}_{1} \mathbf{k}_{3}}} \mathcal{A}_{\substack{l_{2} l_{4} \\
\mathbf{k}_{2} \mathbf{k}_{4}}} V_{\left|\mathbf{k}_{1}-\mathbf{k}_{3}\right|} \\
& × \mathcal{I}_{\mathbf{k}_{1}-\mathbf{k}_{3}} \delta_{l_{1}, l_{3}} \delta_{l_{2}, l_{4}} \delta_{\mathbf{k}_{1}+\mathbf{k}_{2}, \mathbf{k}_{3}+\mathbf{k}_{4}},
\end{aligned}
\tag{6}
$$

with prefactors

$$
\mathcal{A}_{\substack{l_{1} l_{3} \\
\mathbf{k}_{1} \mathbf{k}_{3}}}=\left\{1+\lambda_{l_{1}} \lambda_{l_{3}} \frac{e^{*}\left(\mathbf{k}_{1}\right)}{\left|e\left(\mathbf{k}_{1}\right)\right|} \frac{e\left(\mathbf{k}_{3}\right)}{\left|e\left(\mathbf{k}_{3}\right)\right|}\right\} C_{b}^{l_{1}}\left(\mathbf{k}_{1}\right) C_{b}^{l_{3}}\left(\mathbf{k}_{3}\right)
\tag{7}
$$

and

$$
\mathcal{I}_{\mathbf{k}}=\left[\left(\frac{|\mathbf{k}| a_{B}}{Z_{\text {eff }}}\right)^{2}+1\right]^{-6}
\tag{8}
$$

resulting from the tight-binding coefficients, $^{17}$ the Bohr radius $a_{B}$, the effective atomic number $^{17} Z_{\text {eff }}$, and the Kroneckers describing the momentum conservation. For CNTs as quasi-one-dimensional structures, it is necessary to regularize the Coulomb potential. Within the approximation that the carrier density is concentrated on the surface of the tube of a radius $\rho_{0}$, we obtain

$$
V_{R}(z-z')=\frac{e_{0}^{2}}{2 \pi^{2} \epsilon_{0}} \frac{K\left(-\frac{4 \rho_{0}^{2}}{\left(z-z^{\prime}\right)^{2}}\right)}{\left|z-z^{\prime}\right|}
\tag{9}
$$

with the permittivity $\epsilon_{0}$. The corresponding Fourier transform reads

$$
V_{\mathbf{q}}=e_{0}^{2} /\left(2 \pi^{2} \epsilon_{0} L\right) I(\rho|\mathbf{q}|) K(\rho|\mathbf{q}|)
\tag{10}
$$

with $I(x)$ [$K(x)$] as the regular (irregular) modified cylindrical Bessel function of zeroth order. The length $L$ of the nanotube cancels after performing the sum over $\mathbf{q}$. Furthermore, the Coulomb interaction is screened by introducing the dielectric function $\epsilon(\mathbf{q})$ within the static limit of the Lindhard approximation $^{42}$

$$
\epsilon(\mathbf{q})=1-2 V_{\mathbf{q}} \sum_{l_{1} l_{2}} \frac{\rho_{\mathbf{k}-\mathbf{q}}^{l_{1}}-\rho_{\mathbf{k}}^{l_{2}}}{E_{l_{1}}(\mathbf{k}-\mathbf{q})-E_{l_{2}}(\mathbf{k})}\left|\mathcal{A}_{\mathbf{k}-\mathbf{q} \mathbf{k}}^{l_{1} l_{2}} \mathcal{I}_{\mathbf{q}}\right|^{2}. \quad(11)
$$

The screening effects play an important role, in particular for metallic nanotubes. $^{16,43}$

The last two contributions in the Hamilton operator describe the free phonon system

$$
\mathcal{H}_{\text {phonon }}=\sum_{j \mathbf{q}} \hbar \omega_{j \mathbf{q}} b_{j \mathbf{q}}^{+} b_{j \mathbf{q}},
\tag{12}
$$

and the carrier-phonon interaction $^{35,36}$

$$
\mathcal{H}_{\text {carrier-phonon }}=\sum_{j \mathbf{q} \mathbf{k} l} g_{\mathbf{q}}^{j} a_{l \mathbf{k}+\mathbf{q}}^{+} a_{l \mathbf{k}} b_{j \mathbf{q}}+\text { h.a. }
\tag{13}
$$

Here, $\hbar \omega_{j \mathbf{q}}$ is the phonon energy and $b_{j \mathbf{q}}^{+}$($b_{j \mathbf{q}}$) are operators creating (annihilating) a phonon with the wave vector $\mathbf{q}$ and the mode $j$. In our analytical study, we focus on $\Gamma$-LO and $K$ phonons assuming a constant phonon energy of $\hbar \omega_{\text {LO }} \approx 200$ meV and $\hbar \omega_{\text {LO }} \approx 150$ meV, respectively. The carrier-phonon coupling matrix elements are taken from Ref. 44, where it has been shown that Kohn anomalies can be exploited to determine the strength of the carrier-phonon coupling at high-symmetry points in the Brillouin zone of graphene. Within this approximation, the coupling does not depend on the carrier and phonon momentum. The matrix elements for CNTs can be traced back to the ones calculated for graphene $^{44}$ by taking into account the ratio of the unit cells of graphene and the investigated nanotube, i.e. $|g^{j}|^{2}=D_{j}^{2} a_{0}^{2} \sqrt{3} /(2 \mathbf{a} \cdot \mathbf{c})$ $e V^{2}$. Here, $\mathbf{a}$ is the vector along the tube axis, $\mathbf{c}$ is the circumference vector, and $j$ denotes the phonon mode with $^{43}$ $|D_{\text {LO }}|^{2}=0.0405$ eV$^{2}$ and $|D_{K}|^{2}=0.0994$ eV$^{2}$.

Having determined the Hamilton operator including the electron and phonon energies as well as the coupling elements, we can now derive the CNT-Bloch equation for the microscopic polarization $p_{\mathbf{k}}=\langle a_{c \mathbf{k}}^{+} a_{v \mathbf{k}}\rangle$. The arising hierarchy problem is resolved within the correlation expansion $^{42}$ up to second order in electron-phonon interaction and in the Hartree-Fock factorization to truncate the Coulomb contribution. The resulting Bloch equation reads:

$$
\begin{aligned}
\partial_{t} p_{\mathbf{k}}= & i \tilde{\omega}_{v c}(\mathbf{k}) p_{\mathbf{k}}-\tilde{\Omega}_{\mathbf{k}}(t)-\gamma p_{\mathbf{k}} \\
& +\sum_{j l \mathbf{q}}\left(g_{\mathbf{q}}^{j} S_{\mathbf{k}, \mathbf{q}}^{l c j}-g_{\mathbf{q}}^{j} S_{\mathbf{k}-\mathbf{q}, \mathbf{q}}^{v l j}+g_{\mathbf{q}}^{j *} S_{\mathbf{k}-\mathbf{q}, \mathbf{q}}^{c l j *}-g_{\mathbf{q}}^{j *} S_{\mathbf{k}, \mathbf{q}}^{l v j *}\right)
\end{aligned}
\tag{14}
$$

with the transition energy $\hbar \tilde{\omega}_{v c}(\mathbf{k})=\{E_{v}(\mathbf{k})-E_{c}(\mathbf{k})+$ $V_{\text {ren }}(\mathbf{k})\} / \hbar$ renormalized by the repulsive part of the electron-electron interaction: $^{17,33}$

$$
V_{\text {ren }}(\mathbf{k})=\sum_{\mathbf{k}^{\prime}}\left(V_{\mathbf{k} \mathbf{k}^{\prime} \mathbf{k}^{\prime} \mathbf{k}}^{c v v c}-V_{\mathbf{k} \mathbf{k}^{\prime} \mathbf{k}^{\prime} \mathbf{k}}^{v v v v}\right).
\tag{15}
$$

The oscillator strength is determined by the Rabi frequency $\tilde{\Omega}_{\mathbf{k}}(t)=e_{0} / m_{e} \mathbf{A}(t) \cdot \mathbf{M}_{v c}(\mathbf{k})-i / \hbar V_{\text {exc }}(\mathbf{k}, t)$ renormalized by

the attractive part of the electron-hole interaction $^{17,33}$

$$
V_{\mathrm{exc}}(\mathbf{k}, t)=\sum_{\mathbf{k}^{\prime}}\left(V_{\substack{c v c v \\
\mathbf{k} \mathbf{k}^{\prime} \mathbf{k}^{\prime} \mathbf{k}}} p_{\mathbf{k}^{\prime}}(t)+V_{\substack{c c v v \\
\mathbf{k} \mathbf{k}^{\prime} \mathbf{k}^{\prime} \mathbf{k}}} p_{\mathbf{k}^{\prime}}^{*}(t)\right). \quad(16)
$$

While $V_{\text {ren }}(\mathbf{k})$ accounts for a considerable blue-shift of the freeparticle Van Hove singularities in the absorption spectrum, $V_{\text {exc }}(\mathbf{k}, t)$ is responsible for the formation of bound electronhole pairs leading to red-shifted excitonic Lorentz peaks. For more details, see Refs. 17 and 33. The second line in Eq. (14) contains the electron-phonon contributions with the phonon-assisted quantities $S_{\mathbf{k}, \mathbf{q}}^{l_{1} l_{2} j}=\langle a_{l_{1} \mathbf{k}+\mathbf{q}}^{+} a_{l_{2} \mathbf{k}} b_{j \mathbf{q}}\rangle$ describing the transition of an electron accompanied by phonon emission and absorption, respectively. Analogous to the microscopic polarisation [Eq. (14)], we derive equations of motion for $S_{\mathbf{k}, \mathbf{q}}^{l_{1} l_{2} j}$ and obtain a closed set of coupled differential equations:

$$
\begin{aligned}
\partial_{t} S_{\mathbf{k}, \mathbf{q}}^{l_{1} l_{2} j}= & i\left\{\omega_{v c}(\mathbf{k})-\omega_{\mathbf{q}}\right\} S_{\mathbf{k}, \mathbf{q}}^{l_{1} l_{2} j}+\frac{i}{\hbar}\left(1+N_{\mathbf{q}}\right) g_{\mathbf{j}}^{*}\left\{\rho_{\mathbf{k}+\mathbf{q}}^{l_{1} l_{2}}-\rho_{\mathbf{k}}^{l_{1} l_{2}}\right\} \\
& +\frac{2 i}{\hbar} \sum_{\mathbf{k}^{\prime}}\left(V_{\substack{l_{2} l_{1} l_{2} l_{1} \\
\mathbf{k} \mathbf{k}^{\prime} \mathbf{k} \mathbf{k}^{\prime}}} S_{\mathbf{k}^{\prime}, \mathbf{q}}^{l_{1} l_{2} j}+V_{\substack{l_{2} l_{1} l_{1} l_{2} \\
\mathbf{k} \mathbf{k}^{\prime} \mathbf{k} \mathbf{k}^{\prime}}} S_{\mathbf{k}^{\prime}, \mathbf{q}}^{l_{1} l_{2} j}\right).
\end{aligned}
$$

Now, we have a closed set of coupled differential equations, which will be evaluated within the Runge-Kutta algorithm. The damping constant $\gamma=0.0125 / \hbar$ has been introduced to Eq. (14) for numerical reasons. It denotes neglected processes of higher order in the correlation expansion and has no influence on the peak position or the formation of phonon sidebands in the absorption spectrum of CNTs.

### III. EXCITONIC BASIS

To study the linear absorption of CNTs including excitonphonon interaction, we perform the transformation of the Bloch equation for the microscopic polarization [Eq. (14)] into the excitonic basis. $^{45}$ First, we introduce a basis set of excitonic wave functions $\Phi_{n \mathbf{k}}$ with $n$ denoting the exciton energies. Then, following the procedure in Ref. 45, we rewrite the microscopic polarization

$$
p_{\mathbf{k}}=\sum_{n} \Phi_{n \mathbf{k}} P_{n},
$$

with the new quantity $P_{n}$ as the $n$th excitonic transition amplitude. In the excitonic basis, we introduce the new phonon-assisted densities

$$
S_{\mathbf{k}, \mathbf{q}}^{j}=\sum_{n} \Phi_{n \mathbf{k}+\mathbf{q} / 2} T_{n,-\mathbf{q}}^{j} ; S_{\mathbf{k}, \mathbf{q}}^{j *}=\sum_{n} \Phi_{n \mathbf{k}+\mathbf{q} / 2} R_{n, \mathbf{q}}^{j}.
$$

This method allows us to focus on the description of the carrierphonon interaction, since all information about the carriercarrier coupling is already contained in the excitonic wave functions $\Phi_{n \mathbf{k}}$. Within the linear optics, i.e., assuming that the driving field is small resulting in a negligible change of occupation probabilities, $^{42}$ we take into account only terms which are linear in polarization $p_{\mathbf{k}}(t)$ and vector potential $\mathbf{A}(t)$. Now, we insert the above transformations of the microscopic polarization and the phonon-assisted densities into the Bloch equation [Eq. (14)]. Then, we multiply the left hand side with a complex conjugated excitonic wave function $\Phi_{n^{\prime} \mathbf{k}}^{*}$ and use the completeness relation. We obtain a new simplified Bloch equation:

$$
i \hbar \dot{P}_{n}=\varepsilon_{n} P_{n}-A_{n}(t)-i \hbar \gamma P_{n}+\sum_{n^{\prime} j \mathbf{q}} g_{n n^{\prime}}^{j}(\mathbf{q}) Q_{n^{\prime} \mathbf{q}}^{j}, \quad(20)
$$

with the excitonic energy $\varepsilon_{n}$ and with $Q_{n^{\prime} \mathbf{q}}^{j}=T_{n^{\prime} \mathbf{q}}^{j}+R_{n^{\prime} \mathbf{q}}^{j}$. Here, the effective carrier-light coupling is given by

$$
A_{n}(t)=i \hbar \frac{e_{0}}{m_{e}} \sum_{\mathbf{k}} \Phi_{n \mathbf{k}}^{*} \mathbf{A}(t) \cdot \mathbf{M}_{c v}(\mathbf{k}).
$$

The excitonic polarization amplitudes $P_{n}$ couple to the effective densities $R_{n \mathbf{q}}^{j}$ and $T_{n \mathbf{q}}^{j}$ driven by the coupling with phonons of the mode $j$.

$$
\begin{aligned}
i \hbar \dot{T}_{n \mathbf{q}}^{j}= & \left(\epsilon_{n \mathbf{q}}^{j}+\epsilon_{j}\right) T_{n \mathbf{q}}^{j}-i \hbar \gamma_{s} T_{n \mathbf{q}}^{j} \\
& +\left(1+N_{j \mathbf{q}}\right) \sum_{n^{\prime}} g_{n n^{\prime}}^{j}(\mathbf{q}) P_{n^{\prime}},
\end{aligned}
$$

$$
\begin{aligned}
i \hbar \dot{R}_{n \mathbf{q}}^{j}= & \left(\epsilon_{n \mathbf{q}}^{j}-\epsilon_{j}\right) R_{n \mathbf{q}}^{j}-i \hbar \gamma_{s} R_{n \mathbf{q}}^{j} \\
& +N_{j \mathbf{q}} \sum_{n^{\prime}} g_{n n^{\prime}}^{j}(\mathbf{q}) P_{n^{\prime}} .
\end{aligned}
$$

Here, $\epsilon_{n}(\epsilon_{n \mathbf{q}}^{j})$ is the excitonic transition energy (containing the phonon distortion), which is obtained via the equation:

$$
\begin{aligned}
& \left\{E_{c}(\mathbf{k})-E_{v}(\mathbf{k})+\sum_{\mathbf{k}^{\prime}}\left(V_{\substack{c v v c \\
\mathbf{k} \mathbf{k}^{\prime} \mathbf{k}^{\prime} \mathbf{k}}}-V_{\substack{v v v v \\
\mathbf{k} \mathbf{k}^{\prime} \mathbf{k}^{\prime} \mathbf{k}}}\right)\right\} \Phi_{n \mathbf{k}} \\
& \quad+\sum_{\mathbf{k}^{\prime}}\left(V_{\substack{c v c v \\
\mathbf{k} \mathbf{k}^{\prime} \mathbf{k}^{\prime} \mathbf{k}}} \Phi_{n \mathbf{k}^{\prime}}+V_{\substack{c c v v \\
\mathbf{k} \mathbf{k}^{\prime} \mathbf{k}^{\prime} \mathbf{k}}} \Phi_{n \mathbf{k}^{\prime}}^{*}\right)=\epsilon_{n} \Phi_{n \mathbf{k}} .
\end{aligned}
$$

In an analogous way, $\epsilon_{n \mathbf{q}}^{j}$ can be determined. $\epsilon_{j}$ denotes the constant dispersion relation of optical phonons in the mode $j$. In the bath approximation, the phonon occupation density $N_{j \mathbf{q}}=\langle b_{j \mathbf{q}}^{+} b_{j \mathbf{q}}\rangle$ is approximated by the Bose-Einstein distribution. The phenomenological damping corresponds to the experimentally measured phonon lifetime of $1.1 \mathrm{ps} .{ }^{46}$ Within the excitonic basis, the exciton-phonon coupling matrix elements can be expressed as

$$
g_{n n^{\prime}}^{j}(\mathbf{q})=\sum_{\mathbf{k}}\left|g_{\mathbf{q}}^{j}\right| \Phi_{n \mathbf{k}}^{*}\left(\Phi_{n^{\prime} \mathbf{k}+\mathbf{q} / 2}-\Phi_{n^{\prime} \mathbf{k}-\mathbf{q} / 2}\right) .
$$

They explicitly depend on the excitonic wave function $\Phi_{n \mathbf{k}}$, which can be determined by solving the microscopic polarization of the pure excitonic system [first line in Eq. (14)] $^{47}$. Considering the stationary distribution of the microscopic polarization in the reciprocal space and assuming the one-exciton limit, i.e. $n=n^{\prime}$, the excitonic wave function is proportional to $p_{\mathbf{k}}$ up to a constant parameter, cp. Eq. (18). As a result, applying the normalization condition we can calculate the excitonic wave functions. Then, the new exciton-phonon and carrier-light coupling elements can be determined allowing the solution of Eqs. (20)-(23) and the determination of the absorption coefficient.

### IV. EXCITONIC ABSORBTION SPECTRUM

The linear absorption spectrum of carbon nanotubes can be determined via the absorption coefficient

$$
\alpha(\omega) \propto \sum_{\mathbf{k}} \Im \mathrm{m}\left\{p_{\mathbf{k}}^{\prime \prime}(\omega) M_{v c}(\mathbf{k})\right\} /\{\omega A(\omega)\},
$$


which is given by the Fourier transform of the imaginary part of the microscopic polarization $p_{\mathbf{k}}^{\prime \prime}(\omega)$. It can be expressed within an analytic expression including the exciton-phonon coupling:

$$
\alpha(\omega) \propto \frac{\Re \mathrm{e}}{\omega}\left(\frac{-i}{\hbar\left(\omega-\omega_{n}+i \gamma\right)-\sum_{j \mathbf{q}} g_{n n}^{j 2}(\mathbf{q}) \Gamma_{n \mathbf{q}}^{j}}\right) \quad (27)
$$

with

$$
\Gamma_{n \mathbf{q}}^{j}=\frac{1+N_{j \mathbf{q}}}{\hbar\left(\omega-\omega_{n \mathbf{q}}^{j}-\omega_{j}+i \gamma_{s}\right)}+\frac{N_{j \mathbf{q}}}{\hbar\left(\omega-\omega_{n \mathbf{q}}^{j}+\omega_{j}+i \gamma_{s}\right)},
\quad (28)
$$

where $\omega_{j}$ is the phonon frequency of the mode $j$ and $\hbar \omega_{n \mathbf{q}}^{j}$ the phonon-renormalized excitonic energy. Without the exciton-phonon coupling, i.e., $(g_{n n}^{j}=0)$, Eq. (27) corresponds to a Lorentzian describing symmetric excitonic transitions. Including the exciton-phonon coupling, we observe the formation of phonon sidebands. Their position and optical strength is given by terms in $\Gamma_{n \mathbf{q}}^{j}$. The contribution proportional to $(1+N_{j \mathbf{q}})$ describes processes accompanied by an emission of phonons, while the phonon absorption is described by the $N_{j \mathbf{q}}$ term.

Figure 1 shows the absorption spectrum of an exemplary metallic (18,0) zigzag nanotube at different temperatures. The absorption with and without the exciton-phonon interaction is compared. Neglecting the influence of phonons, we observe a symmetric Lorentz peak describing the excitonic transition (dashed line). Including the exciton-phonon interaction via $\Gamma$-LO phonons, our calculations reveal the formation of one sideband at room temperature (solid line). It is located 200 meV above the zero-phonon line corresponding to the $\Gamma$-LO phonon emission process. At higher temperatures, the occupation of phonons is increased leading to efficient phonon absorption. As a result, we find a sideband also below the zero-phonon line, cp. Fig. 1(b). By increasing the temperatures, we obtain an enhanced transfer of the optical spectral weight from the zero-phonon line to the sidebands, cp. Fig. 1(c). Furthermore, we observe a small, temperature-independent shift of the zero-phonon line due to the exciton-phonon interaction, cp. Fig. 1(d). Note that this polaron shift is expected to be larger due to contributions stemming from higher excitonic transitions. $^{31}$

![](./images/813335629948518400_1.jpg)

FIG. 1. (Color online) Absorption spectrum of the exemplary metallic (18,0) CNT at (a) room temperature and (b) an elevated temperature (1000 K). Pronounced phonon-induced sidebands are observed on both sides of the zero-phonon line, depending on temperature. For comparison, the dashed line represents the excitonic spectrum without phonons. Enlargements of (c) the higher-energetic sideband and (d) the polaron shift at 300 and 1000 K.

![](./images/813335629948518400_2.jpg)

FIG. 2. (Color online) Diameter dependence of the polaron shift and the transfer of the spectral weight from the zero-phonon line to the phonon-induced sideband at room temperature. Metallic tubes [(21,0), (18,0), (15,0), (12,0), (9,0)] with varying diameter and a constant chiral angle $(\Theta=0^{\circ})$ are investigated. The dependence is shown for $\Gamma$-LO and $K$ phonons, respectively.

To obtain a better understanding of the formation of the phonon-induced sidebands, we study the diameter and the chirality dependence of (i) the polaron shift and (ii) the spectral weight transfer from the zero-phonon line to the phonon-induced ($\Gamma$-LO and $K$-phonons) sideband. We observe a decrease of both features with increasing diameter, cp. Fig. 2. This can be traced back to the weaker electron-phonon and electron-electron coupling elements $V_{\mathbf{q}},|g|^{2} \propto$ $1 / d$. Our calculations show that $K$ phonons give rise to more pronounced features in the spectra, in agreement with experimental findings. $^{27}$ For smaller nanotubes with diameters around 0.8 nm, we obtain a polaron shift of approximately

![](./images/813335629948518400_3.jpg)

FIG. 3. (Color online) Chirality dependence of the polaron shift and the transfer of the spectral weight from the zero-phonon line to the phonon sideband at room temperature. The metallic Kataura branch with $2 n_{1}+n_{2}=24$ is investigated containing nanotubes with different chiral angles and a similar diameter. The dependence is shown for $\Gamma-$ LO and $K$ phonons, respectively.

033409-4

15 meV (35 meV) and a spectral weight transfer of 35% (60%)
in the case of $\Gamma$-LO ($K$) phonons. Furthermore, our cal-
culations reveal a strong chirality dependence: The polaron
shift and the spectral weight transfer are about four to six
times larger for zigzag nanotubes (with a chiral angle of $0^\circ$)
compared to armchair tubes ($30^\circ$). This dependence can be
partially led back to the small diameter change along the
investigated Kataura branch. The tubes close to the armchair
configuration have a slightly larger diameter than the zigzag
tubes, resulting in smaller polaron shifts and smaller spectral
weight transfer, cp. Fig. 3.

## V. CONCLUSION

In conclusion, we have presented a microscopic and semi-
analytic expression for the absorption coefficient including
the formation of excitons as well as of the phonon-induced
sidebands in carbon nanotubes. Our approach is based on
excitonic wave functions, which already include the Coulomb-
induced carrier-carrier interaction and allow us to focus on
the exciton-phonon coupling. Depending on temperature, we
observe pronounced sidebands at both sides of the zero-phonon
line. Our calculations reveal that the coupling with $K$ phonons
is predominant, leading to a polaron shift of up to 40 meV.
Furthermore, we observe a reduction of both the polaron
shift and the spectral weight transfer with increasing diameter
and increasing chiral angle, i.e., the most pronounced phonon
sidebands are expected for zigzag tubes with a small diameter.
The presented approach can also be applied to investigate
optical properties of other nanostructures, such as graphene
and nanoribbons.

## ACKNOWLEDGMENTS

We acknowledge financial support by the Deutsche
Forschungsgesellschaft through SFB 658. Furthermore, we
thank E. Molinari, D. Prezzi, A. Ruini (Modena), F. Mauri,
and M. Lazzeri (Paris) for fruitful discussions.

*evgeny.bobkin@tu-berlin.de
$^1$S. M. Bachilo, M. S. Strano, C. Kittrell, R. H. Hauge, R. E. Smalley,
and R. B. Weisman, *Science* **298**, 2361 (2002).
$^2$M. Y. Sfeir, F. Wang, L. Huang, C.-C. Chuang, J. Hone,
S. P. O'Brien, T. F. Heinz, and L. E. Brus, *Science* **306**, 1540
(2004).
$^3$S. Reich, C. Thomsen, and J. Maultzsch, *Carbon Nanotubes: Basic
Concepts and Physical Properties* (Wiley-VCH Verlag, Weinheim,
2004).
$^4$A. Jorio, G. Dresselhaus, and M. S. Dresselhaus, *Carbon Nan-
otubes: Advanced Topics in the Synthesis, Structure, Properties
and Applications* (Springer, Berlin, 2007).
$^5$P. Avouris, M. Freitag, and V. Perebeinos, *Nat. Photonics* **2**, 341
(2008).
$^6$E. Malic, C. Weber, M. Richter, V. Atalla, T. Klamroth, P. Saalfrank,
S. Reich, and A. Knorr, *Phys. Rev. Lett.* **106**, 097401 (2011).
$^7$F. Wang, G. Dukovic, L. E. Brus, and T. F. Heinz, *Science* **308**, 838
(2005).
$^8$J. Maultzsch, R. Pomraenke, S. Reich, E. Chang, D. Prezzi,
A. Ruini, E. Molinari, M. S. Strano, C. Thomsen, and C. Lienau,
*Phys. Rev. B* **72**, 241402 (2005).
$^9$J. Shaver and J. Kono, *Laser & Photon. Rev.* **1**, 260 (2007).
$^{10}$F. Wang, D. J. Cho, B. Kessler, J. Deslippe, P. J. Schuck, S. G.
Louie, A. Zettl, T. F. Heinz, and Y. R. Shen, *Phys. Rev. Lett.* **99**,
227401 (2007).
$^{11}$T. Ando, J. *Phys. Soc. Jpn.* **66**, 1066 (1997).
$^{12}$C. L. Kane and E. J. Mele, *Phys. Rev. Lett.* **90**, 207401 (2003).
$^{13}$C. D. Spataru, S. Ismail-Beigi, L. X. Benedict, and S. G. Louie,
*Phys. Rev. Lett.* **92**, 077402 (2004).
$^{14}$E. Chang, G. Bussi, A. Ruini, and E. Molinari, *Phys. Rev. B* **72**,
195423 (2005).
$^{15}$J. Jiang, R. Saito, G. G. Samsonidze, A. Jorio, S. G. Chou,
G. Dresselhaus, and M. S. Dresselhaus, *Phys. Rev. B* **75**, 035407
(2007).
$^{16}$E. Malic, J. Maultzsch, S. Reich, and A. Knorr, *Phys. Rev. B* **82**,
035433 (2010).
$^{17}$M. Hirschulz, F. Milde, E. Malic, S. Butscher, C. Thomsen,
S. Reich, and A. Knorr, *Phys. Rev. B* **77**, 035403 (2008).
$^{18}$E. Malic, M. Hirschulz, S. Reich, and A. Knorr, *Phys. Status Solidi
RRL* **3**, 196 (2009).
$^{19}$T. G. and Pedersen, *Carbon* **42**, 1007 (2004).
$^{20}$S. V. Goupalov, B. C. Satishkumar, and S. K. Doorn, *Phys. Rev. B*
**73**, 115401 (2006).
$^{21}$T. Ando and S. Uryu, *Phys. Status Solidi C* **6**, 173 (2009).
$^{22}$R. M. Konik, *Phys. Rev. Lett.* **106**, 136805 (2011).
$^{23}$R. R. Hartmann, I. A. Shelykh, and M. E. Portnoi, *Phys. Rev. B* **84**,
035437 (2011).
$^{24}$S. V. Goupalov, *Phys. Rev. B* **84**, 125407 (2011).
$^{25}$F. Plentz, H. B. Ribeiro, A. Jorio, M. S. Strano, and M. A. Pimenta,
*Phys. Rev. Lett.* **95**, 247401 (2005).
$^{26}$S. Berciaud, L. Cognet, P. Poulin, R. B. Weisman, and B. Lounis,
*Nano Lett.* **7**, 1203 (2007).
$^{27}$O. N. Torrens, M. Zheng, and J. M. Kikkawa, *Phys. Rev. Lett.* **101**,
157401 (2008).
$^{28}$Y. Murakami, B. Lu, S. Kazaoui, N. Minami, T. Okubo, and
S. Maruyama, *Phys. Rev. B* **79**, 195407 (2009).
$^{29}$S. Berciaud, C. Voisin, H. Yan, B. Chandra, R. Caldwell, Y. Shan,
L. E. Brus, J. Hone, and T. F. Heinz, *Phys. Rev. B* **81**, 041414
(2010).
$^{30}$G. Yu, Q. Liang, Y. Jia, and J. Dong, *J. Appl. Phys.* **107**, 024314
(2010).
$^{31}$V. Perebeinos, J. Tersoff, and P. Avouris, *Phys. Rev. Lett.* **94**, 027402
(2005).
$^{32}$F. Rossi and T. Kuhn, *Rev. Mod. Phys.* **74**, 895 (2002).
$^{33}$E. Malic, M. Hirschulz, F. Milde, M. Richter, J. Maultzsch,
S. Reich, and A. Knorr, *Phys. Status Solidi B* **245**, 2155
(2008).
$^{34}$X. Blase, L. X. Benedict, E. L. Shirley, and S. G. Louie, *Phys. Rev.
Lett.* **72**, 1878 (1994).
$^{35}$S. Butscher, F. Milde, M. Hirschulz, E. Malic, and A. Knorr, *Appl.
Phys. Lett.* **91**, 203103 (2007).
$^{36}$T. Winzer, A. Knorr, and E. Malic, *Nano Lett.* **10**, 4839 (2010).
$^{37}$E. Malic, T. Winzer, E. Bobkin, and A. Knorr, *Phys. Rev. B* **84**,
205406 (2011).
$^{38}$R. Saito, G. Dresselhaus, and M. Dresselhaus, *Physical Properties
of Carbon Nanotubes* (World Sientific, Singapore, 2003).

033409-5

$^{39}$E. Malic, M. Hirtschulz, F. Milde, A. Knorr, and S. Reich, *Phys. Rev. B* **74**, 195431 (2006).

$^{40}$A. Grüneis, R. Saito, G. G. Samsonidze, T. Kimura, M. A. Pimenta, A. Jorio, A. G. SouzaFilho, G. Dresselhaus, and M. S. Dresselhaus, *Phys. Rev. B* **67**, 165402 (2003).

$^{41}$E. Malic, M. Hirtschulz, F. Milde, Y. Wu, J. Maultzsch, T. Heinz, A. Knorr, and S. Reich, *Physica Status Solidi (b)* **244**, 4240 (2007); *Phys. Rev. B* **77**, 045432 (2008).

$^{42}$H. Haug and S. W. Koch, *Quantum theory of the Optical and Electronic Properties of Semiconductors*, 5th ed. (World Scientific Publishing, Singapore, 2009).

$^{43}$E. Malic, J. Maultzsch, S. Reich, and A. Knorr, *Phys. Rev. B* **82**, 115439 (2010).

$^{44}$S. Piscanec, M. Lazzeri, J. Robertson, A. C. Ferrari, and F. Mauri, *Phys. Rev. B* **75**, 035427 (2007).

$^{45}$T. Östreich, N. Donlagic, C. Wöhler, and K. Schönhammer, *Phys. Status Solidi B* **206**, 205 (1998).

$^{46}$D. Song, F. Wang, G. Dukovic, M. Zheng, E. D. Semke, L. E. Brus, and T. F. Heinz, *Phys. Rev. Lett.* **100**, 225503 (2008).

$^{47}$A. Thränhardt, S. Kuckenberg, A. Knorr, T. Meier, and S. W. Koch, *Phys. Rev. B* **62**, 2706 (2000).