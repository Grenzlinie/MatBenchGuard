PHYSICAL REVIEW B 94, 184508 (2016)

# Understanding and enhancing superconductivity in $FeSe/SrTiO_3$ by quantum size effects

Bruno Murta and Antonio M. García-García*

Cavendish Laboratory, University of Cambridge, JJ Thomson Av., Cambridge, CB3 0HE, United Kingdom
(Received 6 August 2016; revised manuscript received 28 October 2016; published 21 November 2016)

Superconductivity in one-atom-layer iron selenide (FeSe) on a strontium titanate (STO) substrate is enhanced by almost an order of magnitude with respect to bulk FeSe. There is recent experimental evidence suggesting that this enhancement persists in FeSe/STO nanoislands. More specifically, for sizes $L \sim 10$ nm, the superconducting gap is a highly nonmonotonic function of $L$ with peaks well above the bulk gap value. This is the expected behavior only for weakly-coupled metallic superconductors such as Al or Sn. Here we develop a theoretical formalism to describe these experiments based on three ingredients: Eliashberg theory of superconductivity in the weak coupling limit, pairing dominated by forward scattering, and periodic orbit theory to model spectral fluctuations. We obtain an explicit analytical expression for the size dependence of the gap that describes quantitatively the experimental results with no free parameters. This is a strong suggestion that superconductivity in FeSe/STO is mediated by STO phonons. We propose that, since FeSe/STO is still a weakly coupled superconductor, quantum size effects can be used to further enhance the bulk critical temperature in this interface.

DOI: 10.1103/PhysRevB.94.184508

## I. INTRODUCTION

Bulk iron selenide (FeSe) has a relatively low critical temperature $T_c \sim 8$ K with respect to other iron-based superconductors. Surprisingly, a much higher critical temperature $T_c > 40$ K was reported [1,2] in a single atomic layer of FeSe (with a capping layer) on a strontium titanate (STO) substrate. Additional scanning tunneling microscopy (STM) measurements [3], in situ transport results [4] using a four-probe STM technique, and ARPES [5] experiments have not only confirmed this enhancement but also pointed to an even higher critical temperature $T_c \sim 100$ K in the absence of a capping layer.

Interestingly, in multilayer FeSe heterostructures [6] $T_c$ decreases sharply as the number of FeSe layers increases. However, the energy gap, as measured by STM techniques, is nonzero only for a single FeSe layer. This is a clear indication that the substrate plays a key role in the enhancement of $T_c$. Indeed, it is well established by now that the Fermi surface of bulk FeSe and the one in FeSe/STO are qualitatively different: Only the latter is particle doped. Charge transfer from the substrate to the FeSe layer is expected to enhance superconductivity as it increases the number of carriers available. Nevertheless, this additional charge is not enough to justify such a dramatic enhancement of $T_c$ [5,7,8].

A recent ARPES experiment [5] has revealed the existence of strongly peaked replica bands approximately 100 meV away from the original electronlike holelike bands in FeSe/STO. Given that STO has a very flat optical phonon band precisely centered around 100 meV [9,10], and since these oxygen vibrational modes are widely separated from other phonon modes, the occurrence of these replica bands is likely due to the coupling between 3d FeSe electrons and the optical oxygen phonon branch in the STO substrate. This novel forward scattering mechanism [11,12], which had previously been found to be relevant in other superconductors [13–16], has in principle the potential to explain the high critical temperature observed in experiments.

Indeed, although different theoretical models [8,11] have already been employed to model FeSe/STO, the approach of Ref. [11] is perhaps the most promising one as values close to the experimental critical temperature were obtained by considering forward scattering [12–16] as the sole superconductivity mechanism. Unlike the usual BCS prediction, the critical temperature is approximately proportional to both the Debye energy and the electron-phonon coupling constant. We note that this approach employs the conventional Eliashberg formalism that assumes that Migdal's theorem holds. For this to happen the Fermi energy must be larger than the Debye energy. In FeSe/STO the Debye energy is of the order of the Fermi energy, but corrections to the Eliashberg formalism [17] due to deviations from Migdal's theorem are still small in the limit of weak coupling $\lambda \leqslant 0.25$ that seems to describe the FeSe/STO experimental results. Indeed, the results of a recent calculation [18] of vertex corrections in FeSe/STO provide further support to the applicability of the Eliashberg formalism.

Recent STM measurements [6] in one-layer FeSe/STO nanoislands of typical size $L \sim 10$ nm have shown that the superconducting gap is a highly nonmonotonic function of the grain size. Even small changes in the grain size induce large variations of the gap with peaks and valleys that deviate substantially (~40–50%) from the bulk limit. This is hardly an exception as there are already a plethora of theoretical and experimental studies [19–31] that have shown the importance of size effects in superconductivity when one or more dimensions is reduced to the nanoscale (see Ref. [32] for an excellent review focused on superconductivity nanograins). Of special importance in our analysis is the experimental observation of strikingly similar effects [33] in nanograins of conventional metallic superconductors such as Al and Sn. Its origin is well understood [20,34–43]: fluctuations of the spectral density around the Fermi energy, enhanced by spectral degeneracies (shell effects), make the gap sensitive to the grain size. Bardeen-Schieffer-Cooper (BCS) theory is enough to model quantitatively these quantum-size deviations from the bulk limit. In standard BCS theory these effects

*amg73@cam.ac.uk

2469-9950/2016/94(18)/184508(9)
184508-1
©2016 American Physical Society

are especially pronounced for sizes much smaller than the superconducting coherence length of the material. However, its observation in FeSe/STO comes as a total surprise. The coherence length in FeSe/STO is of the order of the grain size, and forward scattering suppresses quantum size effects as it restricts the phase space available for pairing. The only possible explanation is that superconductivity in FeSe/STO is not BCS-like, namely the gap or $T_c$ do not depend exponentially on the electron-phonon coupling constant, and that deviations from perfect forward scattering are sufficiently strong.

Here we propose a theoretical model that describes quantitatively these quantum size effects, thus shedding light on the bulk FeSe/STO superconductivity mechanism. More specifically, we combine semiclassical techniques with the Eliashberg theory of superconductivity in the weak-coupling limit in order to describe theoretically quantum size effects in superconductors with strong forward scattering. We then show that our model describes quantitatively size effects in FeSe/STO nanoislands without the need of any fitting parameter. This is a strong indication that high $T_c$ superconductivity in FeSe/STO is mostly caused by pairing of FeSe electrons mediated by STO phonons. Finally, we also argue that, as in granular metallic superconductors [44] and thin films [19,27], further enhancement of superconductivity is possible by nanoengineering of FeSe/STO nanograins to form a bulk material.

## II. RESULTS
We study quantum size effects in FeSe/STO by combining Eliashberg theory [45,46] and forward scattering [13-16] with a semiclassical analysis of size effects [40] based on periodic orbit theory. In the bulk limit this problem has already been investigated in detail [11,12,18], where it was proposed that forward scattering could be the main mechanism for the enhancement of superconductivity. Here we study specifically how forward scattering modifies quantum size effects in FeSe/STO.

Within the Eliashberg theory [45,46] of superconductivity, the electron self-energy due to the electron-phonon interaction in the weak-coupling limit [11] is given by:

$$
\begin{aligned}
\Delta\left(\mathbf{k}, i \omega_{n}\right)= & \frac{-1}{N \beta} \sum_{\mathbf{q}, m}\left|g(\mathbf{k}, \mathbf{q})\right|^{2} D^{(0)}\left(\mathbf{q}, i \omega_{n}-i \omega_{m}\right) \\
& \times \frac{\Delta\left(\mathbf{k}+\mathbf{q}, i \omega_{m}\right)}{\omega_{m}^{2}+\epsilon_{\mathbf{k}+\mathbf{q}}^{2}+\Delta^{2}\left(\mathbf{k}+\mathbf{q}, i \omega_{m}\right)},
\end{aligned}
\tag{1}
$$

where $\Delta(\mathbf{k},i\omega_n)$ is the gap function, $\text{D}^{(0)}(\mathbf{q},i\omega_m)=-2\omega_D/(\omega_D^2+\omega_m^2)$ is the bare phonon propagator (assuming a flat phonon mode of Debye energy $\omega_D,\hbar=1$), and $|g(\mathbf{k},\mathbf{q})|$ is the matrix element that describes the electron-phonon interaction. $\epsilon_k$ is the dispersion of the electron (relative to the chemical potential $\mu$), $N$ is the number of momentum grid points, $\beta=1/k_B T$ is the inverse temperature, and $\omega_n=(2n+1)\pi/\beta$ is a Matsubara frequency.

The assumption that the superconducting properties of FeSe/STO can be described by considering only the phonon-mediated pairing channel in the weak-coupling limit $\lambda\leqslant0.3$ [11] requires forward scattering [13-16] to be included in the model. Replacing $\lambda=0.3$ and $\omega_D=100$ meV in the usual BCS expression $\Delta_0=2\omega_D\exp(-1/\lambda)$ gives a bulk gap of only 7 meV, which is far from the experimentally measured 16.5 meV [47]. However, solving the Eliashberg momentum-dependent equations for low-momentum transfer gives a gap linear in both the Debye energy and the coupling constant, which would allow the bulk gap to be obtained for a Debye energy of the expected order of magnitude for a small $\lambda$.

Under the assumption of strong forward scattering, only electrons close to the Fermi level are involved in the pairing. Therefore we assume that pairing occurs only at the Fermi level. Another argument in favor of this approximation is that we aim to model experiments [47] where theoretical results are compared to the experimental value of the spectroscopic gap measured in different positions of the grain which is closely related to fixing the momentum $k$ to be the Fermi momentum. Other calculations [37,44] in conventional superconducting nanograins have shown that the magnitude of mesoscopic effects is not substantially altered by including the $k$ dependence provided that the effective number of states subjected to pairing is not substantially altered. Based on similar arguments we also neglect any angular dependence of $k$ at $k_F$. We note that recent theoretical [18] and experimental results [48] suggest that, in contrast with previous claims in the literature, the angular dependence must be taken into account for a quantitative description of the gap in FeSe/STO. However, we believe that by averaging over $k$ we would get qualitatively similar results for the mesoscopic fluctuations we are interested in. A more detailed analysis would obscure our main goal, which is making an analytical and parameter-free estimation of the strength of mesoscopic fluctuations in this material. In summary, we assume $|\mathbf{k}|\approx k_F$ in (1):

$$
\begin{aligned}
\Delta\left(i \omega_{n}\right)= & \frac{-1}{N \beta} \sum_{\mathbf{q}, m}|g(\mathbf{q})|^{2} D^{(0)}\left(\mathbf{q}, i \omega_{n}-i \omega_{m}\right) \\
& \times \frac{\Delta\left(i \omega_{m}\right)}{\omega_{m}^{2}+\epsilon_{\mathbf{k}_{F}+\mathbf{q}}^{2}+\Delta^{2}\left(i \omega_{m}\right)}.
\end{aligned}
\tag{2}
$$

The extreme case of low-momentum transfer corresponds to perfect forward scattering, for which no momentum transfer is allowed and hence the matrix element can be written as a Kronecker Delta function. In this limit the bulk gap is found to be $\Delta_0\approx\frac{2\lambda}{2+3\lambda}\omega_D$ [18]. As expected, the expression for the bulk gap is linear in $\lambda$ and $\omega_D$. For $\lambda=0.22$ and $\omega_D=100$ meV we get a bulk gap of $\sim$16 meV.

However, it is clear that within this perfect forward scattering limit no corrections due to quantum size effects can be expected. Indeed, the fluctuations arising from the quantization of the energy levels are due to the variation of the number of states that contribute to the interaction as the area of the grain is changed; such change cannot be observed in this case because the Kronecker delta picks a single momentum state for the interaction. As a result, we must consider a finite cutoff in order to observe fluctuations.

In order to mimic the experimental situation, we must therefore consider the case of forward scattering with a finite width [14]. The matrix element may be written as $|g(\mathbf{q})|^2=N g_0^2 h(\mathbf{q})=N\lambda\omega_D^2 h(\mathbf{q})$, where $h(\mathbf{q})$ gives the functional

form of the cutoff. For example, Rademaker *et al.* [11] considered an exponentially decaying cutoff $h(\mathbf{q}) = e^{-|\mathbf{q}|/q_0}$. Keeping a general form of the cutoff function, equation (2) becomes:
$$
\begin{aligned}
\Delta(i \omega_{n})= & \frac{2 \omega_{D}^{3} \lambda}{\beta} \sum_{\mathbf{q}, m} \frac{h(\mathbf{q})}{\omega_{D}^{2}+\left(\omega_{n}-\omega_{m}\right)^{2}} \\
& \times \frac{\Delta(i \omega_{m})}{\omega_{m}^{2}+\epsilon_{\mathbf{k}_{F}+\mathbf{q}}^{2}+\Delta^{2}(i \omega_{m})}.
\end{aligned}\qquad(3)
$$

Using the ansatz $\Delta(i \omega_{n}) = \Delta/(1+(\omega_n/\omega_D)^2)$ [11] and setting $n=0$ so that $\omega_n \ll \omega_D$ and therefore $\omega_D^2 + (\omega_n - \omega_m)^2 \approx \omega_D^2 + \omega_m^2$, equation (3) becomes:
$$
1=\frac{2 \lambda \omega_{D}^{5}}{\beta} \sum_{\mathbf{q}, m} \frac{h(\mathbf{q})}{\left(\omega_{m}^{2}+\epsilon_{\mathbf{k}_{F}+\mathbf{q}}^{2}\right)\left[\omega_{D}^{2}+\omega_{m}^{2}\right]^{2}+\omega_{D}^{4} \Delta^{2}}.
\qquad(4)
$$

The Matsubara frequency summation in equation (4),
$$
\frac{1}{\beta} \sum_{m} \frac{1}{\left(\omega_{m}^{2}+\epsilon_{\mathbf{k}_{F}+\mathbf{q}}^{2}\right)\left[\omega_{D}^{2}+\omega_{m}^{2}\right]^{2}+\omega_{D}^{4} \Delta^{2}},\qquad(5)
$$
can be solved by contour integration before considering the sum over momentum. Assuming $\epsilon_{\mathbf{k}_{F}+\mathbf{q}} \ll \Delta_0 \ll \omega_D$ for the range of $\mathbf{q}$ considered [49], the approximate poles of the integrand are $\omega_m = \pm i\sqrt{\Delta^2 + \epsilon^2}, \pm i(\omega_D - \Delta/2), \pm i(\omega_D + \Delta/2)$. After summing over Matsubara frequencies, equation (3) becomes:
$$
1=\lambda \omega_{D} \sum_{\mathbf{q}} h(\mathbf{q})\left(\frac{1}{\sqrt{\epsilon_{\mathbf{k}_{F}+\mathbf{q}}^{2}+\Delta^{2}}}-\frac{3}{2 \omega_{D}}\right).\qquad(6)
$$

For an arbitrary cutoff $h(\mathbf{q})$, equation (6) can only be solved numerically. However, in order to study the deviations from the perfect forward scattering limit analytically, and for the sake of simplicity as well, we assume a sharp cutoff so that $h(\mathbf{q})=0$ everywhere except for $\mathbf{q}$'s within the interval $\epsilon_F - \epsilon_0 < \epsilon_{\mathbf{k}_F+\mathbf{q}} < \epsilon_F + \epsilon_0$ where $h(\mathbf{q}) = \frac{2\pi}{Aq_0^2}$ with $\epsilon_0 = \hbar^2 q_0^2/2m^*$, $m^*$ is the effective electron mass, $q_0 \sim C/a$, $a$ is the lattice constant of FeSe, and $C \sim \mathcal{O}(1)$. The chosen value of the cutoff $h(\mathbf{q}) = \frac{2\pi}{Aq_0^2}$ ensures that the perfect forward scattering limit is recovered for $q_0 \to 0$.

By converting the sum over momentum states into an integral over energy about the chemical potential, Eq. (6) may be rewritten as:
$$
\begin{aligned}
1 & =\lambda \omega_{D} \frac{2 \pi}{A q_{0}^{2}} \sum_{|\mathbf{q}|<q_{0}}\left(\frac{1}{\sqrt{\epsilon_{\mathbf{k}_{F}+\mathbf{q}}^{2}+\Delta^{2}}}-\frac{3}{2 \omega_{D}}\right) \\
& =\frac{\lambda \omega_{D}}{2 \epsilon_{0} v_{T F}(0)} \int_{\epsilon_{F}-\epsilon_{0}}^{\epsilon_{F}+\epsilon_{0}} d \epsilon \nu(\epsilon)\left(\frac{1}{\sqrt{\left(\epsilon-\epsilon_{F}\right)^{2}+\Delta^{2}}}-\frac{3}{2 \omega_{D}}\right),
\end{aligned}
\qquad(7)
$$
where $\nu(\epsilon)$ is the density of states at energy $\epsilon$ and $v_{TF}(0) = \frac{A k_F^2}{4\pi \epsilon_F}$ is the bulk density of states at the Fermi energy.

We note that the overlap integrals between the single-particle wave functions, which arise from the matrix element, were ignored, since their contribution to the finite size fluctuations of the gap is small [41]. Therefore, the only correction due to quantum size effects that we consider is the quantization of the energy levels through the semiclassical expansion [50,51] of the spectral density,
$$
\nu(\epsilon)=\nu_{T F}(0)(1+\overline{g}(0)+\tilde{g}(\epsilon)),\qquad(8)
$$
where
$$
\overline{g}(0)= \pm \frac{\mathcal{L}}{2 k_{F} L^{2}}\qquad(9)
$$
$$
\begin{aligned}
\tilde{g}(\epsilon) & =\tilde{g}_{1,2}^{(2)}(\epsilon)-\frac{1}{2} \sum_{i} \tilde{g}_{i}^{(1)}(\epsilon) \\
& =\sum_{L_{n} \neq 0}^{\infty} J_{0}\left(k(\epsilon) L_{n}^{1,2}\right)-\sum_{i=x, y} \frac{2 L_{i}}{k_{F} L^{2}} \sum_{L_{n} \neq 0}^{\infty} \cos \left(k(\epsilon) L_{n}^{i}\right),
\end{aligned}
\qquad(10)
$$
where the plus and minus signs in $\overline{g}(0)$, the Weyl term, correspond to Neumann and Dirichlet boundary conditions, respectively, $L_x = \alpha L$ and $L_y = L/\alpha$ are the sides of the rectangle $(\alpha > 1)$, $L^2 = L_x L_y$ is the area, $\mathcal{L}=2(L_x + L_y)$ is the perimeter, and $k_F = \sqrt{2 m^* \epsilon_F}/\hbar$ is the Fermi wave vector. $J_0$ is the zeroth-order Bessel function of the first kind, $L_n^{1,2} = 2\sqrt{L_x^2 n^2 + L_y^2 m^2}$ is the length of the periodic orbit $(n,m)$, and $L_n^i = 2n L_i$ is the length of a single-integer periodic orbit. $\tilde{g}_{1,2}^{(2)}(\epsilon)$ is of $\mathcal{O}(1/\sqrt{k_F L})$, whereas $\overline{g}(0)$ and $\tilde{g}_i^{(1)}$ are both of $\mathcal{O}(1/k_F L)$.

Replacing the spectral density by the expression above in (7) and expanding the gap as
$$
\Delta(L)=\Delta_{0}\left(1+f_{1 / 2}+f_{1}\right),\qquad(11)
$$
where $f_i$ stand for corrections to the gap of order $(k_F L)^{-i}$, the gap equation is solved order by order in $(k_F L)^{-i}$. A detailed derivation of the finite size corrections is presented in Appendix. Here we only present the highlights of the calculation and state the final results.

The zeroth-order term in $(k_F L)^{-i}$ equality gives the bulk gap for a finite width $\epsilon_0$ of the phonon spectrum:
$$
1=\frac{\lambda \omega_{D}}{2 \epsilon_{0}} \int_{-\epsilon_{0}}^{\epsilon_{0}} d \epsilon\left(\frac{1}{\sqrt{\epsilon^{2}+\Delta_{0}^{2}}}-\frac{3}{2 \omega_{D}}\right).\qquad(12)
$$

This integral is evaluated exactly to give:
$$
\Delta_{0}=\frac{\epsilon_{0}}{\sinh \left((1 / \lambda+3 / 2) \frac{\epsilon_{0}}{\omega_{D}}\right)}.\qquad(13)
$$

As expected, the zeroth-order term (i.e., the bulk gap) in this expansion in the small parameter $1/k_F L$ coincides with the result in the perfect $(\epsilon_0 \to 0)$ forward scattering limit [18], since for FeSe/STO $\epsilon_0 \ll \Delta_0 \ll \omega_D$ corrections to this limit are expected to be rather small.

![](./images/811110458240008194_1.jpg)
![](./images/811110458240008194_2.jpg)

FIG. 1. Size dependence of the low-temperature superconducting gap: (Blue line) analytical result from Eqs. (11), (13), (17), and (18) with $\lambda = 0.22$, $\epsilon_0 = 4$ meV, $k_F = 2.06$ nm, $\omega_D = 100$ meV, and $\epsilon_F = 60$ meV; (red line) numerical evaluation of the gap from the second line of (7) for the same parameters. Left: nanoisland of rectangular shape of aspect ratio $\alpha = 1.2$, for all areas. Right: the same for an aspect ratio $\alpha = 1.4$. In both cases we find excellent agreement between numerical and analytical results. We have found a similar agreement for other aspect ratios. The small difference between the analytical and numerical results is likely due to the fact that we are considering only the leading contribution in $\propto \Delta_0/\omega_D \ll 1$. Higher-order corrections will bring an even better agreement with the numerical results.

A straightforward calculation (see Appendix for details) results in the following expression for the leading finite size correction:
$$
f_{1 / 2}=\frac{\int_{-\epsilon_{0}}^{\epsilon_{0}} d \epsilon \tilde{g}_{1,2}^{(2)}(\epsilon)\left(\frac{1}{\sqrt{\epsilon^{2}+\Delta_{0}^{2}}}-\frac{3}{2 \omega_{D}}\right)}{\Delta_{0}^{2} \int_{-\epsilon_{0}}^{\epsilon_{0}} d \epsilon \frac{1}{\left(\Delta_{0}^{2}+\epsilon^{2}\right)^{3 / 2}}}.\qquad(14)
$$

Considering the numerator first, using the asymptotic limit of the Bessel function $J_{0}(x)=\sqrt{2 / \pi x} \cos (x-\pi / 4)$, expanding the wave vector $k(\epsilon)=k_{F}(1+\epsilon /(2 \epsilon_{F}))$ (where $\epsilon_F = \hbar^2 k_F^2/2m$ is the Fermi energy) and solving the energy integral within the limit $\epsilon_0 \ll \Delta_0$, the numerator in (14) becomes:
$$
\begin{aligned}
& \int_{-\epsilon_{0}}^{\epsilon_{0}} d \epsilon \tilde{g}_{1,2}^{(2)}(\epsilon)\left(\frac{1}{\sqrt{\epsilon^{2}+\Delta_{0}^{2}}}-\frac{3}{2 \omega_{D}}\right) \\
& \quad=2 \epsilon_{0}\left(\frac{1}{\Delta_{0}}-\frac{3}{2 \omega_{D}}\right) \sum_{L_{n} \neq 0}^{\infty} J_{0}\left(k_{F} L_{n}\right) \operatorname{sinc}\left(L_{n} / \xi\right), \quad(15)
\end{aligned}
$$
where $\operatorname{sinc}(x) \equiv \sin (x) / x$ and $\xi=\frac{2 \epsilon_{F}}{k_{F} \epsilon_{0}}$ plays the role of coherence length. Therefore contributions from periodic orbits much greater than $\xi$ are strongly suppressed.

The integral over energy in the denominator can be solved exactly to give:
$$
\Delta_{0}^{2} \int_{-\epsilon_{0}}^{\epsilon_{0}} d \epsilon \frac{1}{\left(\Delta_{0}^{2}+\epsilon^{2}\right)^{3 / 2}}=\frac{2 \epsilon_{0}}{\sqrt{\Delta_{0}^{2}+\epsilon_{0}^{2}}} \approx \frac{2 \epsilon_{0}}{\Delta_{0}},\qquad(16)
$$
where in the last step we considered the limit $\epsilon_0 \ll \Delta_0$, which was used to derive a closed-form expression for the numerator. Dividing (15) by (16) gives $f_{1/2}$:
$$
f_{1 / 2}=\left(1-\frac{3 \Delta_{0}}{2 \omega_{D}}\right) \sum_{L_{n} \neq 0}^{\infty} J_{0}\left(k_{F} L_{n}\right) \operatorname{sinc}\left(L_{n} / \xi\right).\qquad(17)
$$

The calculation of the next-to-leading-order term $\propto (k_F L)^{-1}$, highlighted in Appendix, is more convoluted. Here we only state the final result to leading order in $\frac{\Delta_0}{\omega_D}$:
$$
\begin{aligned}
f_{1}= & -\left(1-\frac{3 \Delta_{0}}{2 \omega_{D}}\right)\left[\frac{L_{x}+L_{y}}{k_{F} L^{2}}+\sum_{i=x, y} \frac{2 L_{i}}{k_{F} L^{2}} \sum_{L_{n} \neq 0}^{\infty} \cos \left(k_{F} L_{n}^{i}\right)\right. \\
& \left.\times \operatorname{sinc}\left(\frac{L_{n}^{i}}{\xi}\right)\right]-\frac{3 \Delta_{0}}{2 \omega_{D}} f_{1 / 2}^{2},
\end{aligned}\qquad(18)
$$
where $L_x = \alpha L$ and $L_y = L/\alpha$ are the sides of the nanoisland, with $\alpha > 1$, $L_n^i = 2n L_i$ is the length of the periodic orbit and $L = \sqrt{L_x L_y}$. Since the STO substrate is a dielectric, Dirichlet boundary conditions were used, hence the minus sign in the Weyl term.

The final expression for the size dependence of the gap (11) in the semiclassical limit is obtained from (13), (17), and (18). At least for FeSe/STO nanoislands [47] $k_F \sim 2$ nm and $L \sim$ 10 nm, so it is safe to neglect higher orders in the semiclassical expansion. We also stress that these analytical results are only valid in the limits $\epsilon_0 \ll \Delta_0 \ll \omega_D$ and $\lambda \ll 1$.

We test explicitly the validity of the semiclassical expression (11) by comparing it with the numerical calculation of the gap from (12) using the exact spectral density. Results, depicted in Fig. 1, clearly show that the analytical expression is an excellent quantitative approximation for the numerical gap including the complex pattern of oscillations induced by fluctuations of the spectral density. We have focused on the range of parameters describing FeSe/STO, as this is the main goal of the paper. However, with the appropriate modifications, our results are applicable to any weakly coupled superconductor where electron pairing, mediated by phonons or another mechanism, is dominated by forward scattering.


### III. COMPARISON WITH FeSe/STO EXPERIMENTAL RESULTS

For the sake of clarity, we start by summarizing the range of parameters that are supposed to describe superconductivity in FeSe/STO nanoislands [47]. To a good extent the nanoislands are rectangular with area $\sim$50-100 nm². The aspect ratio varies from island to island and is not known experimentally, but it is expected to belong to the interval (0,1.5]. ARPES measurements [5] strongly suggest a Debye energy of $\omega_D \sim$ 100 meV. The Fermi energy is of the same order but slightly smaller, $\epsilon_F \sim$ 60 meV [8]. Taking into account that the effective mass of FeSe electrons is $\text{m}_{\text{eff}} \approx 2.7$ mₑ [52], the effective Fermi wave vector $k_F \approx 2$ nm. Assuming forward scattering as the main source of pairing and $\omega_D \sim$ 100 meV, an electron-phonon coupling constant of $\lambda \approx 0.2$ is required in order for (13) to reproduce the experimental bulk gap $\Delta_0 \approx$ 16 meV. The phonon spectrum must be strongly peaked around $\omega_D \sim$ 100 meV but must still have some finite width, though much smaller than $\omega_D$. Indeed, an exponentially decaying form $|g(\mathbf{q})|^2 \propto \exp(-|\mathbf{q}|/q_0)$ has been proposed [12], where $q_0 \sim C/a$ [with $C = \mathcal{O}(1)$ and $a$ is the lattice spacing] is related to the dielectric properties of the FeSe/STO interface. This matrix element arises from the induced dipole layer generated by the relative displacements of the Ti cations and the oxygen anions in the STO substrate as the phonon modes corresponding to these oscillations are excited. Qualitatively, the cutoff in energy $\epsilon_0$ introduced in the previous section is related to the typical decay on momentum $\epsilon_0 = \hbar^2 q_0^2/2m^* \sim$ 3 meV $\ll \Delta_0 \sim$ 16 meV.

Setting $\lambda = 0.22$, $k_F = 2.06$ nm, $\epsilon_0 = 4$ meV, $\omega_D = 100$ meV, and $\epsilon_F = 60$ meV, we now compare the analytical expression of the gap size dependence (11), together with Eqs. (13), (17), and (18), with the experimental results for FeSe nanoislands on a STO substrate [47]. The agreement (see Fig. 2) is reasonably good, especially taking into account that there are no free fitting parameters. Since the aspect ratio varies from nanoisland to nanoisland, and is not known experimentally (though is expected to be less than 3/2), we have decided to compare the experimental data with the results for two aspect ratios 1.2 and 1.4. Similar results are obtained for other aspect ratios provided that it is not very close to a square shape. More specifically, as is observed in the figures, the oscillating pattern is sensitive to the aspect ratio but its average deviations from the bulk limit are not. For that reason, and for the sake of clarity, we did not include in Fig. 2 more analytical results of more aspect ratios. We stress there is no fine tuning of any parameter and the agreement between theory and experiment is in general not very sensitive to small changes of the parameters.

Our results provide strong evidence that FeSe/STO is mostly a phonon-mediated superconductor where forward scattering is induced by STO phonons with a strongly peaked spectrum around 100 meV. Although not shown, we have checked that numerical results obtained with more realistic cutoff functions, such as exponential [12], lead to very similar results by an appropriate rescaling of $\epsilon_0$ still within the allowed range $\epsilon_0 \ll \Delta_0$. We stick to analytical results in order to emphasize the uniqueness of FeSe/STO: a high $T_c$ superconductor that, for the first time, allows a full analytical quantitative treatment not only of the bulk limit but also of finite size effects.

![](./images/811110458240008194_3.jpg)

FIG. 2. Size dependence of the low-temperature superconducting gap of FeSe nanoislands on a STO substrate: (Black and green lines) analytical result from (11), (13), (17), and (18) with $\lambda = 0.22$, $\epsilon_0 = 4$ meV, $k_F = 2.06$ nm, $\omega_D = 100$ meV, and $\epsilon_F = 60$ meV; (red circles): experimental results from Ref. [47]. The aspect ratio of the nanoisland, which varies from island to island, is not known experimentally, but it is expected to be less than 1.5. We compare the experimental data with the analytical results for two aspect ratios 1.2 (black) and 1.4 (green). Similar qualitative agreement is observed for other aspect ratios (not shown). The overall oscillating pattern, including the enhancement of the gap (which can be as large as 40%, for some sizes), is well captured by the analytical expression. For a more quantitative comparison it would be necessary to know experimentally the nanoisland aspect ratio.

In summary, we find very good agreement between a parameter-free theory and experiments. We stress that, al- though there is some flexibility, the value of the parameters we use is fixed by experiments or first-principle calcula- tions [5,12]. Additional experiments where the shape of the grains is known with more precision would obviously be helpful to fix other parameters of the model more accurately, including the form of the cutoff function and the value of the electron-phonon coupling constant.

### IV. FURTHER ENHANCEMENT OF SUPERCONDUCTIVITY IN FESE/STO

The experimental results for FeSe/STO nanoislands show an enhancement of the superconducting gap of about 50% for some grain sizes. Evidently, a single nanograin $\sim$10 nm is effectively zero dimensional so it cannot sustain global long-range order, a distinct feature of a state with zero resistance. However, a natural question to ask is whether the global critical temperature of a nanoengineered bulk material, composed of an array of these nanoislands connected by Josephson junctions, is enhanced by quantum size effects. This question has been answered affirmatively [44,53] in the context of quasi-two-dimensional weakly-coupled superconductors. For Al, it was predicted a maximum enhancement of 300% that has recently been confirmed experimentally [28]. The reason for the enhancement is simply that, although many

grains have a low $T_c$, in order for a supercurrent to exist it is only necessary that a relatively small number (given by the percolation threshold) of grains are still superconducting at the global critical temperature.

The enhancement that could be achieved in FeSe/STO would likely be much smaller for a number of reasons: (1) the typical length that controls size effects is much smaller than in Al; (2) shell effects are weaker because a rectangular grain has less level degeneracy than spherical Al grains; (3) FeSe/STO is strictly two dimensional, so quantum and thermal fluctuations, which are detrimental to superconductivity, are stronger. Nevertheless, it is likely that an enhancement of up to 50% [54] could be observed, provided that it is possible to nanoengineer an array of square (instead of rectangular, as shell effects are stronger in the former) grains of sizes $\sim 6$ nm. Finally, it would be necessary to suppress thermal fluctuations by coupling the interface to a metal or by making the FeSe/STO interface more metallic.

## V. CONCLUSION
We have developed a theory of quantum size effects in Eliashberg superconductivity in the limit of weak coupling and peaked phonon spectrum. Our model describes the highly nonmonotonic size dependence of the superconducting gap of FeSe/STO nanoislands quantitatively. Our results provide further support that FeSe/STO is a weakly-coupled phonon- mediated superconductor with pairing coming from interface phonons with a strongly peaked, but finite, frequency spec- trum. Further enhancement of superconductivity is possible by nanoengineering of FeSe/STO superconducting grains.

## ACKNOWLEDGMENTS
A.M.G. warmly thanks Lili Wang, Canli Song, and Zhi Li for providing the experimental data of Ref. [47] and illumination discussions. A.M.G. acknowledges support from EPSRC, Grant No. EP/I004637/1.

## APPENDIX: FINITE SIZE EFFECTS FOR FORWARD SCATTERING WITH A FINITE CUTOFF
Starting from equation (7),
$$
1=\frac{\lambda \omega_{D}}{2 \epsilon_{0} \nu_{T F}(0)} \int_{-\epsilon_{0}}^{\epsilon_{0}} d \epsilon \nu(\epsilon)\left(\frac{1}{\sqrt{\epsilon^{2}+\Delta^{2}}}-\frac{3}{2 \omega_{D}}\right), \quad \text { (A1) }
$$
and expanding the superconducting gap and the density of states, respectively, as $\Delta(L)=\Delta_{0}(1+f_{1 / 2}+f_{1})$ and $\nu(\epsilon)=$ $\nu_{T F}(0)(1+g_{1 / 2}+g_{1})$, where $f_{i}$ and $g_{i}$ are of $\mathcal{O}(k_{F} L)^{-i}$, including only terms up to $\mathcal{O}(1 / k_{F} L)$:

$$
\begin{aligned}
1= & \frac{\lambda \omega_{D}}{2 \epsilon_{0}} \int_{-\epsilon_{0}}^{\epsilon_{0}} d \epsilon\left(1+g_{1 / 2}+g_{1}\right)\left[\frac{1}{\sqrt{\epsilon^{2}+\Delta_{0}^{2}\left(1+2 f_{1 / 2}+2 f_{1}+f_{1 / 2}^{2}\right)}}-\frac{3}{2 \omega_{D}}\right] \\
= & \frac{\lambda \omega_{D}}{2 \epsilon_{0}} \int_{-\epsilon_{0}}^{\epsilon_{0}} d \epsilon\left(1+g_{1 / 2}+g_{1}\right)\left[\frac{1}{\sqrt{\epsilon^{2}+\Delta_{0}^{2}}} \frac{1}{\sqrt{1+\frac{\Delta_{0}^{2}}{\Delta_{0}^{2}+\epsilon^{2}}\left(2 f_{1 / 2}+2 f_{1}+f_{1 / 2}^{2}\right)}}-\frac{3}{2 \omega_{D}}\right] \\
\approx & \frac{\lambda \omega_{D}}{2 \epsilon_{0}} \int_{-\epsilon_{0}}^{\epsilon_{0}} d \epsilon\left(1+g_{1 / 2}+g_{1}\right)\left[\frac{1-\frac{\Delta_{0}^{2}}{\Delta_{0}^{2}+\epsilon^{2}}\left(f_{1 / 2}+f_{1}+\frac{f_{1 / 2}^{2}}{2}\right)+\frac{3}{2}\left(\frac{\Delta_{0}^{2}}{\Delta_{0}^{2}+\epsilon_{0}^{2}}\right)^{2} f_{1 / 2}^{2}}{\sqrt{\epsilon^{2}+\Delta_{0}^{2}}}-\frac{3}{2 \omega_{D}}\right] \\
= & \frac{\lambda \omega_{D}}{2 \epsilon_{0}} \int_{-\epsilon_{0}}^{\epsilon_{0}} d \epsilon\left[\left(\frac{1}{\sqrt{\epsilon^{2}+\Delta_{0}^{2}}}-\frac{3}{2 \omega_{D}}\right)+\left(g_{1 / 2}\left(\frac{1}{\sqrt{\epsilon^{2}+\Delta_{0}^{2}}}-\frac{3}{2 \omega_{D}}\right)-\frac{\Delta_{0}^{2}}{\left(\epsilon^{2}+\Delta_{0}^{2}\right)^{3 / 2}} f_{1 / 2}\right)\right. \\
& \left.+\left(g_{1}\left(\frac{1}{\sqrt{\epsilon^{2}+\Delta_{0}^{2}}}-\frac{3}{2 \omega_{D}}\right)-\frac{\Delta_{0}^{2}}{\left(\epsilon^{2}+\Delta_{0}^{2}\right)^{3 / 2}}\left(f_{1}+\frac{f_{1 / 2}^{2}}{2}+f_{1 / 2} g_{1 / 2}\right)+\frac{3}{2} \frac{\Delta_{0}^{4}}{\left(\epsilon^{2}+\Delta_{0}^{2}\right)^{5 / 2}} f_{1 / 2}^{2}\right)\right]
\end{aligned}
$$

where after the last equality the terms between the first, second, and third pairs of large curly brackets are of $\mathcal{O}(1), \mathcal{O}(1/\sqrt{k_F L})$, and $\mathcal{O}(1/k_F L)$, respectively. In the transition from the second to the third line the binomial expansion $1/\sqrt{1+x}=1-\frac{1}{2}x+\frac{3}{8}x^2+\mathcal{O}(x^3)$ was carried out, since the corrections $f_i$ and $g_i$ are much smaller than unity.

Equating terms of $\mathcal{O}(1)$ we get:
$$
1=\frac{\lambda \omega_{D}}{2 \epsilon_{0}} \int_{-\epsilon_{0}}^{\epsilon_{0}} d \epsilon\left(\frac{1}{\sqrt{\epsilon^{2}+\Delta_{0}^{2}}}-\frac{3}{2 \omega_{D}}\right), \quad \text { (A3) }
$$
which can be easily integrated to lead to obtain an explicit expression for the bulk gap:
$$
\Delta_{0}=\frac{\epsilon_{0}}{\sinh \left((1 / \lambda+3 / 2) \frac{\epsilon_{0}}{\omega_{D}}\right)}. \quad \text { (A4) }
$$

Equating terms of $\mathcal{O}(1/\sqrt{k_F L})$ gives:
$$
f_{1 / 2}=\frac{\int_{-\epsilon_{0}}^{\epsilon_{0}} d \epsilon \tilde{g}_{1,2}^{(2)}(\epsilon)\left(\frac{1}{\sqrt{\epsilon^{2}+\Delta_{0}^{2}}}-\frac{3}{2 \omega_{D}}\right)}{\Delta_{0}^{2} \int_{-\epsilon_{0}}^{\epsilon_{0}} d \epsilon \frac{1}{\left(\Delta_{0}^{2}+\epsilon^{2}\right)^{3 / 2}}}. \quad \text { (A5) }
$$


The numerator can be simplified the following way:

$$
\begin{aligned}
\int_{-\epsilon_{0}}^{\epsilon_{0}} d \epsilon \tilde{g}_{1,2}^{(2)}(\epsilon)\left(\frac{1}{\sqrt{\epsilon^{2}+\Delta_{0}^{2}}}-\frac{3}{2 \omega_{D}}\right) &=\int_{-\epsilon_{0}}^{\epsilon_{0}} d \epsilon \sum_{L_{n} \neq 0}^{\infty} J_{0}\left(k(\epsilon) L_{n}^{1,2}\right)\left(\frac{1}{\sqrt{\epsilon^{2}+\Delta_{0}^{2}}}-\frac{3}{2 \omega_{D}}\right) \\
& \approx \int_{-\epsilon_{0}}^{\epsilon_{0}} d \epsilon \sum_{L_{n} \neq 0}^{\infty} \sqrt{\frac{2}{\pi k_{F} L_{n}^{1,2}}} \cos \left(k_{F}\left(1+\frac{\epsilon}{2 \epsilon_{F}}\right) L_{n}^{1,2}-\frac{\pi}{4}\right)\left(\frac{1}{\sqrt{\epsilon^{2}+\Delta_{0}^{2}}}-\frac{3}{2 \omega_{D}}\right) \\
& \approx \sum_{L_{n} \neq 0}^{\infty} J_{0}\left(k_{F} L_{n}^{1,2}\right) \int_{-\epsilon_{0}}^{\epsilon_{0}} d \epsilon \cos \left(\frac{k_{F} \epsilon}{2 \epsilon_{F}} L_{n}^{1,2}\right)\left(\frac{1}{\sqrt{\epsilon^{2}+\Delta_{0}^{2}}}-\frac{3}{2 \omega_{D}}\right) \\
& \approx \sum_{L_{n} \neq 0}^{\infty} J_{0}\left(k_{F} L_{n}^{1,2}\right)\left(\frac{1}{\Delta_{0}}-\frac{3}{2 \omega_{D}}\right) \int_{-\epsilon_{0}}^{\epsilon_{0}} d \epsilon \cos \left(\frac{k_{F} \epsilon}{2 \epsilon_{F}} L_{n}^{1,2}\right) \\
&=\sum_{L_{n} \neq 0}^{\infty} J_{0}\left(k_{F} L_{n}^{1,2}\right)\left(\frac{1}{\Delta_{0}}-\frac{3}{2 \omega_{D}}\right) 2 \frac{2 \epsilon_{F}}{k_{F} L_{n}^{1,2}} \sin \left(\frac{k_{F} \epsilon_{0}}{2 \epsilon_{F}} L_{n}^{1,2}\right) \\
& \equiv \sum_{L_{n} \neq 0}^{\infty} J_{0}\left(k_{F} L_{n}^{1,2}\right) 2 \epsilon_{0}\left(\frac{1}{\Delta_{0}}-\frac{3}{2 \omega_{D}}\right) \operatorname{sinc}\left(\frac{L_{n}^{1,2}}{\xi}\right),
\end{aligned}
\tag{A6}
$$

where $\operatorname{sinc}(x) \equiv \sin (x) / x$ and $\xi \equiv \frac{2 \epsilon_{F}}{k_{F} \epsilon_{0}}$ is the relevant coherence length. In the transition from the second to the third line, the asymptotic limit $J_{0}(x)=\sqrt{\frac{2}{\pi x}} \cos (x-\frac{\pi}{4})$ was used and $k(\epsilon)$ was expanded about the Fermi wave vector $k_{F}$. In the following line, the double-angle formula $\cos (a+b)=$ $\cos (a) \cos (b)-\sin (a) \sin (b)$ was used, and the term involving the sines was neglected since $\sin (\frac{k_{F} \epsilon}{2 \epsilon_{F}} L_{n}^{1,2}) \ll 1$. Given that $\epsilon_{0} \ll \Delta_{0} \ll \omega_{D}$, the term between curly brackets in the integrand was assumed constant. However, since the periodic orbits $L_{n}^{1,2}$ can be arbitrarily large, the change of the phase of the cosine over the range of integration cannot be neglected.

The denominator can also be evaluated explicitly,

$$
\Delta_{0}^{2} \int_{-\epsilon_{0}}^{\epsilon_{0}} d \epsilon \frac{1}{\left(\Delta_{0}^{2}+\epsilon^{2}\right)^{3 / 2}}=\frac{2 \epsilon_{0}}{\sqrt{\epsilon_{0}^{2}+\Delta_{0}^{2}}} \approx \frac{2 \epsilon_{0}}{\Delta_{0}}, \tag{A7}
$$

where in the last step we considered the limit $\epsilon_{0} \ll \Delta_{0}$, which was used to derive a closed-form expression for the numerator. Dividing (A6) by (A7) gives the leading-order correction:

$$
f_{1 / 2}=\left(1-\frac{3 \Delta_{0}}{2 \omega_{D}}\right) \sum_{L_{n} \neq 0}^{\infty} J_{0}\left(k_{F} L_{n}\right) \operatorname{sinc}\left(L_{n} / \xi\right). \tag{A8}
$$

Equating terms of $\mathcal{O}(1 / k_{F} L)$:

$$
\begin{aligned}
& {\left[\int_{-\epsilon_{0}}^{\epsilon_{0}} d \epsilon \frac{\Delta_{0}^{2}}{\left(\epsilon^{2}+\Delta_{0}^{2}\right)^{3 / 2}}\right] f_{1}} \\
&= \int_{-\epsilon_{0}}^{\epsilon_{0}} d \epsilon\left(g_{1}\left(\frac{1}{\sqrt{\epsilon^{2}+\Delta_{0}^{2}}}-\frac{3}{2 \omega_{D}}\right)-\frac{\Delta_{0}^{2}}{\left(\epsilon^{2}+\Delta_{0}^{2}\right)^{3 / 2}}\right. \\
&\left.\times\left(\frac{f_{1 / 2}^{2}}{2}+f_{1 / 2} g_{1 / 2}\right)+\frac{3}{2} \frac{\Delta_{0}^{4}}{\left(\epsilon^{2}+\Delta_{0}^{2}\right)^{5 / 2}} f_{1 / 2}^{2}\right), \quad \text { (A9) }
\end{aligned}
$$

where $\quad g_{1}=\bar{g}(0)-\frac{1}{2} \sum_{i} \tilde{g}_{i}^{(1)}(\epsilon)=-\frac{L_{x}+L_{y}}{k_{F} L^{2}}-\sum_{i=x, y} \frac{2 L_{i}}{k_{F} L^{2}}$ $\sum_{L_{n} \neq 0}^{\infty} \cos (k(\epsilon) L_{n}^{i})$ is the $\mathcal{O}(1 / k_{F} L)$ correction to the density of states and, as before, $g_{1 / 2}=\sum_{L_{n} \neq 0}^{\infty} J_{0}(k(\epsilon) L_{n}^{1,2})$. The term on the left-hand side (LHS) and the two terms involving $f_{1 / 2}^{2}$ on the right-hand side (RHS) can be simplified by solving the integrals assuming $\epsilon_{0} \ll \Delta_{0}$:

$$
\begin{aligned}
\frac{2 \epsilon_{0}}{\Delta_{0}} f_{1}= & \int_{-\epsilon_{0}}^{\epsilon_{0}} d \epsilon\left(g_{1}\left(\frac{1}{\sqrt{\epsilon^{2}+\Delta_{0}^{2}}}-\frac{3}{2 \omega_{D}}\right)\right. \\
& \left.-\frac{\Delta_{0}^{2}}{\left(\epsilon^{2}+\Delta_{0}^{2}\right)^{3 / 2}} f_{1 / 2} g_{1 / 2}\right)+\frac{2 \epsilon_{0}}{\Delta_{0}} f_{1 / 2}^{2}\left(\frac{3}{2}-\frac{1}{2}\right).
\end{aligned}
\tag{A10}
$$

The first term on the RHS can be written in closed form as:

$$
\begin{aligned}
- & \int_{-\epsilon_{0}}^{\epsilon_{0}} d \epsilon\left(\frac{L_{x}+L_{y}}{k_{F} L^{2}}+\sum_{i=x, y} \frac{2 L_{i}}{k_{F} L^{2}} \sum_{L_{n} \neq 0}^{\infty} \cos \left(k(\epsilon) L_{n}^{i}\right)\right) \\
& \times\left(\frac{1}{\sqrt{\epsilon^{2}+\Delta_{0}^{2}}}-\frac{3}{2 \omega_{D}}\right) \\
\approx & -2 \epsilon_{0}\left(\frac{1}{\Delta_{0}}-\frac{3}{2 \omega_{D}}\right)\left[\frac{L_{x}+L_{y}}{k_{F} L^{2}}+\sum_{i=x, y} \frac{2 L_{i}}{k_{F} L^{2}}\right. \\
& \left.\times \sum_{L_{n} \neq 0}^{\infty} \cos \left(k_{F} L_{n}^{i}\right) \operatorname{sinc}\left(L_{n}^{i} / \xi\right)\right],
\end{aligned}
\tag{A11}
$$

where in the transition from the first to the second line the approximations described in (A6) were used. The term $\sim f_{1 / 2} g_{1 / 2}$ can also be simplified:

$$
\begin{aligned}
& -\int_{-\epsilon_{0}}^{\epsilon_{0}} d \epsilon \frac{\Delta_{0}^{2}}{\left(\epsilon^{2}+\Delta_{0}^{2}\right)^{3 / 2}} f_{1 / 2} g_{1 / 2} \\
& =-f_{1 / 2} \int_{-\epsilon_{0}}^{\epsilon_{0}} d \epsilon \frac{\Delta_{0}^{2}}{\left(\epsilon^{2}+\Delta_{0}^{2}\right)^{3 / 2}} \sum_{L_{n} \neq 0}^{\infty} J_{0}\left(k(\epsilon) L_{n}^{1,2}\right) \\
& \approx-f_{1 / 2} \sum_{L_{n} \neq 0}^{\infty} J_{0}\left(k_{F} L_{n}^{1,2}\right) \int_{-\epsilon_{0}}^{\epsilon_{0}} d \epsilon \frac{\Delta_{0}^{2}}{\left(\epsilon^{2}+\Delta_{0}^{2}\right)^{3 / 2}} \\
& \quad \times \cos \left(\frac{k_{F} \epsilon}{2 \epsilon_{F}} L_{n}^{1,2}\right) \\
& \approx-f_{1 / 2} \frac{1}{\Delta_{0}} \sum_{L_{n} \neq 0}^{\infty} J_{0}\left(k_{F} L_{n}^{1,2}\right) \frac{\int_{-\epsilon_{0}}^{\epsilon_{0}} d \epsilon \cos \left(\frac{k_{F} \epsilon}{2 \epsilon_{F}} L_{n}^{1,2}\right)}{}
\end{aligned}
$$

$$
\begin{aligned}
& =-f_{1 / 2} \frac{2 \epsilon_{0}}{\Delta_{0}} \sum_{L_{n} \neq 0}^{\infty} J_{0}\left(k_{F} L_{n}^{1,2}\right) \operatorname{sinc}\left(L_{n}^{1,2} / \xi\right) \\
& =-\frac{\frac{2 \epsilon_{0}}{\Delta_{0}}}{\left(1-\frac{3 \Delta_{0}}{2 \omega_{D}}\right)} f_{1 / 2}^{2}, \quad \text { (A12) }
\end{aligned}
$$

where again all steps were previously described in (A6). Combining Eqs. (A10), (A11), and (A12) gives the next-to-leading-order correction:

$$
\begin{aligned}
f_{1}= & -\left(1-\frac{3 \Delta_{0}}{2 \omega_{D}}\right)\left[\frac{L_{x}+L_{y}}{k_{F} L^{2}}+\sum_{i=x, y} \frac{2 L_{i}}{k_{F} L^{2}} \sum_{L_{n} \neq 0}^{\infty} \cos \left(k_{F} L_{n}^{i}\right)\right. \\
& \left.\times \operatorname{sinc}\left(\frac{L_{n}^{i}}{\xi}\right)\right]+f_{1 / 2}^{2}\left(1-\frac{1}{1-\frac{3 \Delta_{0}}{2 \omega_{D}}}\right).
\end{aligned}
$$

[1] W. Qing-Yan, L. Zhi, Z. Wen-Hao, Z. Zuo-Cheng, Z. Jin-Song, L. Wei, D. Hao, O. Yun-Bo, D. Peng, C. Kai *et al.*, *Chin. Phys. Lett.* **29**, 037402 (2012).

[2] W.-H. Zhang, Y. Sun, J.-S. Zhang, F.-S. Li, M.-H. Guo, Y.-F. Zhao, H.-M. Zhang, J.-P. Peng, Y. Xing, H.-C. Wang, T. Fujita, A. Hirata, L. Zhi, H. Ding, C.-J. Tang, M. Wang, Q.-Y. Wang, K. He, S.-H. Ji, X. Chen, J.-F. Wang, Z.-C. Xia, L. Li, Y.-Y. Wang, J. Wang, L.-L. Wang, M.-W. Chen, Q.-K. Xue, and X.-C. Ma, *Chin. Phys. Lett.* **31**, 017401 (2014).

[3] W. Zhang, Z. Li, F. Li, H. Zhang, J. Peng, C. Tang, Q. Wang, K. He, X. Chen, L. Wang, X. Ma, and Q.-K. Xue, *Phys. Rev. B* **89**, 060506 (2014).

[4] J.-F. Ge, Z.-L. Liu, C. Liu, C.-L. Gao, D. Qian, Q.-K. Xue, Y. Liu, and J.-F. Jia, *Nat. Mater.* **14**, 285 (2015).

[5] J. Lee, F. Schmitt, R. Moore, S. Johnston, Y.-T. Cui, W. Li, M. Yi, Z. Liu, M. Hashimoto, Y. Zhang *et al.*, *Nature (London)* **515**, 245 (2014).

[6] Q. Wang, W. Zhang, Z. Zhang, Y. Sun, Y. Xing, Y. Wang, L. Wang, X. Ma, Q.-K. Xue, and J. Wang, *2D Materials* **2**, 044012 (2015).

[7] S. Coh, M. L. Cohen, and S. G. Louie, *New J. Phys.* **17**, 073027 (2015).

[8] L. P. Gor'kov, *Phys. Rev. B* **93**, 060507 (2016).

[9] B. Li, Z. W. Xing, G. Q. Huang, and D. Y. Xing, *J. Appl. Phys.* **115**, 193907 (2014).

[10] N. Choudhury, E. J. Walter, A. I. Kolesnikov, and C.-K. Loong, *Phys. Rev. B* **77**, 134111 (2008).

[11] L. Rademaker, Y. Wang, T. Berlijn, and S. Johnston, *New J. Phys.* **18**, 022001 (2016).

[12] D.-H. Lee, *Chin. Phys. B* **24**, 117405 (2015).

[13] M. L. Kulić and R. Zeyher, *Phys. Rev. B* **49**, 4395 (1994).

[14] G. Varelogiannis, A. Perali, E. Cappelluti, and L. Pietronero, *Phys. Rev. B* **54**, R6877 (1996).

[15] G. Santi, T. Jarlborg, M. Peter, and M. Weger, *Physica C: Superconductivity* **259**, 253 (1996).

[16] A. Perali, C. Grimaldi, and L. Pietronero, *Phys. Rev. B* **58**, 5736 (1998).

[17] C. Grimaldi, L. Pietronero, and S. Strässler, *Phys. Rev. Lett.* **75**, 1158 (1995).

[18] Y. Wang, K. Nakatsukasa, L. Rademaker, T. Berlijn, and S. Johnston, *Supercond. Sci. Technol.* **29**, 054009 (2016).

[19] J. M. Blatt and C. J. Thompson, *Phys. Rev. Lett.* **10**, 332 (1963).

[20] S. Bose, P. Raychaudhuri, L. Banerjee, P. Vasa, and P. Ayyub, *Phys. Rev. Lett.* **95**, 147003 (2005).

[21] C. Brun, I.-Po. Hong, F. Patthey, I. Y. Sklyadneva, R. Heid, P. M. Echenique, K. P. Bohnen, E. V. Chulkov, and W.-D. Leder, *Phys. Rev. Lett.* **102**, 207002 (2009).

[22] C. Carbillet, S. Caprara, M. Grilli, C. Brun, T. Cren, F. Debontridder, B. Vignolle, W. Tabis, D. Demaille, L. Largeau, K. Ilin, M. Siegel, D. Roditchev, and B. Leridon, *Phys. Rev. B* **93**, 144509 (2016).

[23] R. W. Cohen and B. Abeles, *Phys. Rev.* **168**, 444 (1968).

[24] G. Deutscher, H. Fenichel, M. Gershenson, E. Grünbaum, and Z. Ovadyahu, *J. Low Temp. Phys.* **10**, 231 (1973).

[25] I. Giaever and H. R. Zeller, *Phys. Rev. Lett.* **20**, 1504 (1968).

[26] Y. Guo, Y.-F. Zhang, X.-Y. Bao, T.-Z. Han, Z. Tang, L.-X. Zhang, W.-G. Zhu, E. Wang, Q. Niu, Z. Qiu *et al.*, *Science* **306**, 1915 (2004).

[27] A. Perali, A. Bianconi, A. Lanzara, and N. L. Saini, *Solid State Commun.* **100**, 181 (1996).

[28] U. S. Pracht, N. Bachar, L. Benfatto, G. Deutscher, E. Farber, M. Dressel, and M. Scheffler, *Phys. Rev. B* **93**, 100503 (2016).

[29] M. Zgirski, K.-P. Riikonen, V. Touboltsev, and K. Arutyunov, *Nano Lett.* **5**, 1029 (2005).

[30] M. Strongin, R. S. Thompson, O. F. Kammerer, and J. E. Crow, *Phys. Rev. B* **1**, 1078 (1970).

[31] N. A. H. K. Rao, J. C. Garland, and D. B. Tanner, *Phys. Rev. B* **29**, 1214 (1984).

[32] S. Bose and P. Ayyub, *Rep. Prog. Phys.* **77**, 116503 (2014).

[33] S. Bose, A. M. García-García, M. M. Ugeda, J. D. Urbina, C. H. Michaelis, I. Brihuega, and K. Kern, *Nat. Mater.* **9**, 550 (2010).

[34] R. H. Parmenter, *Phys. Rev.* **166**, 392 (1968).

[35] V. Gladilin, V. Fomin, and J. Devreese, *Solid State Commun.* **121**, 519 (2002).

[36] H. Heiselberg, *Phys. Rev. A* **68**, 053616 (2003).


[37] A. A. Shanenko, M. D. Croitoru, M. Zgirski, F. M. Peeters, and K. Arutyunov, *Phys. Rev. B* **74**, 052502 (2006).

[38] V. Z. Kresin and Y. N. Ovchinnikov, *Phys. Rev. B* **74**, 024514 (2006).

[39] M. D. Croitoru, A. A. Shanenko, and F. M. Peeters, *Phys. Rev. B* **76**, 024511 (2007).

[40] A. M. García-García, J. D. Urbina, E. A. Yuzbashyan, K. Richter, and B. L. Altshuler, *Phys. Rev. Lett.* **100**, 187001 (2008).

[41] A. M. García-García, J. D. Urbina, E. A. Yuzbashyan, K. Richter, and B. L. Altshuler, *Phys. Rev. B* **83**, 014510 (2011).

[42] I. Brihuega, A. M. García-García, P. Ribeiro, M. M. Ugeda, C. H. Michaelis, S. Bose, and K. Kern, *Phys. Rev. B* **84**, 104525 (2011).

[43] M. A. N. Araújo, A. M. García-García, and P. D. Sacramento, *Phys. Rev. B* **84**, 172502 (2011).

[44] J. Mayoh and A. M. García-García, *Phys. Rev. B* **90**, 014509 (2014).

[45] F. Marsiglio and J. P. Carbotte, *Superconductivity: Conventional and Unconventional Superconductors* (Springer, Berlin, Heidelberg, 2008), Chap. 3, pp. 73–162.

[46] A. Abrikosov, L. Gor’kov, and I. Dzyaloshinskii, *Methods of Quantum Field Theory in Statistical Physics*, Dover Books on Physics Series (Dover Publications, New York, 1975).

[47] Z. Li, J.-P. Peng, H.-M. Zhang, C.-L. Song, S.-H. Ji, L. Wang, K. He, X. Chen, Q.-K. Xue, and X.-C. Ma, *Phys. Rev. B* **91**, 060509 (2015).

[48] Y. Zhang, J. J. Lee, R. G. Moore, W. Li, M. Yi, M. Hashimoto, D. H. Lu, T. P. Devereaux, D.-H. Lee, and Z.-X. Shen, *Phys. Rev. Lett.* **117**, 117001 (2016).

[49] As noted in the description of the terms involved in equation (1), the electron dispersion $\epsilon_k$ is measured relative to the Fermi level, so $\epsilon_{k_F} = 0$. Hence, for $\epsilon_{\mathbf{k}_F+\mathbf{q}} \ll \Delta_0$, we require $|\mathbf{q}|$ to be small, which is indeed the case if we impose a sharp cutoff in $\mathbf{q}$.

[50] M. Brack and R. Bhaduri, *Semiclassical Physics*, Frontiers in Physics (Addison-Wesley, Reading, MA, 1997).

[51] M. Gutzwiller, *Chaos in Classical and Quantum Mechanics*, Interdisciplinary Applied Mathematics (Springer, New York, 1991).

[52] L. Zhao, A. Liang, D. Yuan, Y. Hu, D. Liu, J. Huang, S. He, B. Shen, Y. Xu, X. Liu, L. Yu, G. Liu, H. Zhou, Y. Huang, X. Dong, F. Zhou, K. Liu, Z. Lu, Z. Zhao, C. Chen, Z. Xu, and X. J. Zhou, *Nat. Commun.* **7**, 10608 (2016).

[53] J. Mayoh and A. M. García-García, *Phys. Rev. B* **92**, 174526 (2015).

[54] A. Garcia-Garcia (unpublished).