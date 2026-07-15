PHYSICAL REVIEW RESEARCH 1, 033138 (2019)

# Predicting charge transport in the presence of polarons:
## The beyond-quasiparticle regime in $SrTiO_3$

Jin-Jian Zhou and Marco Bernardi*
Department of Applied Physics and Materials Science, California Institute of Technology, Pasadena, California 91125, USA

![](./images/812706277489639425_1.jpg)
(Received 26 August 2019; revised manuscript received 17 October 2019; published 2 December 2019)

In materials with strong electron-phonon ($e$-ph) interactions, the electrons carry a phonon cloud during their motion, forming quasiparticles known as polarons. Predicting charge transport and its temperature dependence in the polaron regime remains an open challenge. Here, we present first-principles calculations of charge transport in a prototypical material with large polarons, $SrTiO_3$. Using a cumulant diagram-resummation technique that can capture the strong $e$-ph interactions, our calculations can accurately predict the experimental electron mobility in $SrTiO_3$ between 150–300 K. They further reveal that for increasing temperature the charge transport mechanism transitions from bandlike conduction, in which the scattering of renormalized quasiparticles is dominant, to a beyond-quasiparticle transport regime governed by incoherent contributions due to the interactions between the electrons and their phonon cloud. Our work reveals long-sought microscopic details of charge transport in $SrTiO_3$, and provides a broadly applicable method for predicting charge transport in materials with strong $e$-ph interactions and polarons.

DOI: 10.1103/PhysRevResearch.1.033138

## I. INTRODUCTION

Understanding charge transport in complex materials is a grand challenge of fundamental and technological relevance. The interactions between electrons and phonons (the quanta of lattice vibrations) set an intrinsic limit for the conductivity and typically control charge transport near room temperature. When electron-phonon ($e$-ph) interactions are weak, charge transport is well described by the scattering of quasiparticles (QPs) [1], leading to the well-known bandlike conduction regime. As the $e$-ph interactions become stronger, the electrons are dressed by a cloud of phonons, forming composite charge carriers known as polarons [2–4]. In the limit of strong $e$-ph coupling, the electrons are self-trapped by the lattice distortions, and the conduction mechanism becomes the thermally activated hopping of localized polarons [5].

Many oxides and organic crystals exhibit $e$-ph coupling strengths intermediate between the bandlike and polaron hopping limits [6,7]. In this so-called “large polaron” regime, the charge transport mechanisms and their temperature dependence are not well understood. The transition from bandlike to hopping conduction for increasing $e$-ph coupling strength is also unclear, and recent work on the Holstein model uncovered an incoherent transport regime at intermediate coupling [8]. Yet, predictive calculations and microscopic understanding of charge transport in the intermediate $e$-ph coupling regime remain an open challenge.

Strontium titanate ($SrTiO_3$), which is stable in the cubic phase above 105 K, is a prototypical material with intermediate $e$-ph coupling in which large-polaron effects are clearly seen in experiments [9–12]. Charge transport in $SrTiO_3$ is a decades-old problem [13–18], yet its underlying microscopic mechanisms are still debated [19]. The electron mobility in cubic $SrTiO_3$ exhibits a roughly $T^{-3}$ temperature dependence above 150 K [17,18], which is commonly attributed to the scattering of electron QPs with phonons [13–16]. Different phenomenological models based on QP scattering have been proposed that can fit the experimental transport data [15,20]. However, the carrier mean free paths extracted from experiment in $SrTiO_3$ fall below the interatomic distance [18], violating the Mott-Ioffe-Regel (MIR) criterion for the applicability of the QP scattering picture [21]. While there is consensus that large polarons are present in $SrTiO_3$ [9–12,22], charge transport in this regime cannot yet be predicted, and detailed microscopic understanding has remained elusive [19].

First-principles calculations based on lowest-order $e$-ph scattering plus the Boltzmann transport equation (BTE) [23] can accurately predict the conductivity in simple metals and semiconductors [24–28]. We have recently shown [29] that when this approach is applied to $SrTiO_3$, one can obtain an accurate temperature dependence for the electron mobility if all the phonons (including the soft modes) are taken into account. However, the absolute value of the computed electron mobility is an order of magnitude greater than experiment [29]. It is clear that QP scattering alone cannot explain charge transport in $SrTiO_3$, consistent with the MIR limit violation; a fully quantum mechanical framework is needed to predict charge transport in this beyond-QP regime.

Here we show first-principles calculations of charge transport in cubic $SrTiO_3$ using a finite-temperature retarded cumulant approach that includes higher-order $e$-ph interactions and goes beyond the QP scattering picture. Our calculations can accurately predict the experimental electron mobility in

*Corresponding author: bmarco@caltech.edu

Published by the American Physical Society under the terms of the Creative Commons Attribution 4.0 International license. Further distribution of this work must maintain attribution to the author(s) and the published article’s title, journal citation, and DOI.

2643-1564/2019/1(3)/033138(10)
033138-1
Published by the American Physical Society

JIN-JIAN ZHOU AND MARCO BERNARDI
PHYSICAL REVIEW RESEARCH 1, 033138 (2019)

SrTiO₃ between 150–300 K, and further shed light on its microscopic origin. We show that the weight of the QP peak in the electron spectral function is strongly renormalized, with significant weight transfer to the incoherent phonon satellites. While the renormalized QPs control transport at low temperature, the incoherent contributions from the phonon satellites and large momentum states are significant at room temperature, indicating a transport regime beyond the QP scattering paradigm. Consistent with these trends, our analysis shows that near room temperature the scattering rate (extracted from the optical conductivity) breaks the Planckian limit of $k_{\text{B}}T$ for semiclassical transport [30], clearly indicating a beyond-QP charge transport regime. Our work opens new avenues for computing charge transport in complex materials with large polarons and beyond the QP scattering regime.

## II. ELECTRON SPECTRAL FUNCTION

Central to our approach for computing charge transport is the electron spectral function, $A(\omega)$, which can be seen as the density of states at energy $\omega$ of a single electron. Due to the interactions with the phonons, the spectral function consists of a QP peak representing a single-electron-like excitation and an incoherent part including both phonon satellite peaks and a background contribution [31,32]. While the spectral weights of the QP peak and incoherent part may vary, they always add up to one due to the sum rule $\int d\omega A(\omega)=1$, which amounts to a conservation of the electron. To investigate the dynamics of the electrons and their interactions with the phonons, we compute the spectral function with a finite-temperature retarded cumulant approach that can account for higher-order $e$-ph interactions (see Appendix A), and use it directly to predict transport, without relying on QP scattering approaches.

We focus on the electron spectral function in cubic SrTiO₃ above 110 K. Leveraging our recently developed approach [29], which combines density functional theory (DFT), its linear response extension [33] and the temperature dependent effective potential (TDEP) method [34], we compute the band structure, lattice vibrations and $e$-ph interactions for all phonon modes, including the soft modes due to the lattice anharmonicity (see Appendix B). Using these quantities, we calculate the spectral function using a retarded cumulant formalism [35,36]. The retarded cumulant approach is based on an exponential ansatz for the retarded Green's function of an electronic state $|nk\rangle$ (with band index $n$ and momentum $\boldsymbol{k}$) in the time domain:
$$
G_{nk}^R(t)=-i\theta(t)e^{-i\varepsilon_{nk}t}e^{C_{nk}(t)}, \tag{1}
$$
where $t$ is time, $\theta(t)$ is the Heaviside step function, and $\varepsilon_{nk}$ is the noninteracting electron energy from DFT. The $e$-ph interactions are included in the cumulant $C_{nk}(t)$; an approximate expression derived in Ref. [35] computes $C_{nk}(t)$ using the off-shell lowest-order $e$-ph self-energy, $\Sigma_{nk}(\omega)$ [23] as input:
$$
C_{nk}(t)=\int_{-\infty}^{\infty}d\omega\frac{\beta_{nk}(\omega)}{\omega^2}(e^{-i\omega t}+i\omega t-1), \tag{2}
$$
where $\beta_{nk}(\omega)\equiv|\text{Im}\Sigma_{nk}(\omega+\varepsilon_{nk})|/\pi$. The spectral function can be obtained for each state from the retarded Green's function in the frequency domain, using $A_{nk}(\omega)=-\text{Im}G_{nk}^R(\omega)/\pi$.

![](./images/812706277489639425_2.jpg)

FIG. 1. (a) Combined spectral functions $A_{nk}(\omega)$ for the three lowest conduction bands in cubic SrTiO₃, for $\boldsymbol{k}$ along the $\Gamma$-$X$ and $\Gamma$-$M$ Brillouin zone directions at 110 K. (b) The energy-momentum dispersion of the QP peaks of the spectral function, shown at 110 and 300 K, compared with the electronic band structure from DFT. The zero of the energy axis is set to the conduction band minimum.

Our scheme to compute the retarded Green's function at finite-temperature (see Appendix A) further allows us to compute the spectral function as a function of temperature. The retarded cumulant approach includes higher-order $e$-ph Feynman diagrams beyond the Migdal approximation [37], and it produces accurate spectral functions (see below) that can capture the strong $e$-ph interactions. On the other hand, we have verified that the lowest-order Dyson-Migdal approximation generates spectral functions with large errors in the QP spectral weight and satellites energies, consistent with recent results at zero temperature [38].

The computed electron spectral functions for the three lowest conduction bands in cubic SrTiO₃ at 110 K are combined in a color map and shown in Fig. 1(a). Each state exhibits a rather sharp QP peak at low energy and broader phonon satellite peaks at higher energies (~60 meV or more above the QP peak). By tracking the low-energy QP peaks, we map the energy-momentum dispersion of the QPs. Figure 1(b) shows that the interacting QPs exhibit a heavier effective mass than in the DFT band structure calculations, in which the $e$-ph interactions are not included. The mass enhancement is a factor of 1.8–2.6 for different bands and directions, and it increases only slightly with temperature. Taking the lowest bands along $\Gamma$-M as an example, the DFT effective mass is roughly $0.75m_e$ ($m_e$ is the electron mass), compared to a QP effective mass of $1.4m_e$ at 110 K and a slightly heavier mass of $1.6m_e$ at 300 K. The mass enhancement is thus roughly a factor of 2, in excellent agreement with experimental results at low doping [9,12].

The interactions with the surrounding phonons not only make the electron QPs heavier, they also significantly reduce the QP spectral weight to a value well below one, transferring weight to the higher-energy incoherent phonon satellites. The QP peak even disappears at large electron momenta,

033138-2

![](./images/812706277489639425_3.jpg)

FIG. 2. Computed electron spectral functions $A_{k}(\omega)$ for the lowest conduction band in cubic $SrTiO_{3}$. In each panel, the zero of the $\omega$ energy axis is set to the energy of the QP peak at the $\Gamma$ point. (a) The spectral function $A_{k}(\omega)$ at three temperatures between 110-300 K, for $k=\Gamma$. The energies of the two LO phonons that couple strongly with the electrons are labeled $\omega_{\text{LO-1}}$ and $\omega_{\text{LO-2}}$, and the arrows point to the second set of satellites at $2\omega_{\text{LO-1}}$ and $\omega_{\text{LO-1}}+\omega_{\text{LO-2}}$. (b) The spectral weight $N(\omega)$ obtained by integrating the spectral function up to an energy $\omega$. (c) The spectral function $A_{k}(\omega)$ at 110 K for different values of $\boldsymbol{k}$ along the $\Gamma$-$M$ Brillouin zone line, and (d) The corresponding integrated spectral weight $N(\omega)$.

leaving a spectral function made up entirely by the incoherent background. These trends are analyzed in detail below and in Fig. 2, focusing on how the spectral function of the lowest conduction band changes as a function of temperature and momentum.

The spectral function at the conduction band minimum at $\Gamma$ exhibits a QP peak, two main satellites (also known as phonon sidebands or replicas), and weaker additional satellites at higher energy [see Fig. 2(a)]. The two main satellite peaks are at an energy $\omega_{\text{LO-1}}=98$ meV and $\omega_{\text{LO-2}}=57$ meV above the main QP peak; these values correspond, respectively, to the energies of the two longitudinal optical (LO) modes with long-range $e$-ph interactions that exhibit the strongest coupling with electrons [29]. Note also the presence in Fig. 2(a) of weak phonon sideband peaks at energies of $2\omega_{\text{LO-1}}$ and $\omega_{\text{LO-1}}+\omega_{\text{LO-2}}$. These higher-order replicas, which are known to occur in the strong coupling limit of the Holstein model [39], are akin to the higher harmonics observed in phonon Floquet states [40] and are a signature of strong coupling with the LO modes.

The main phonon sidebands are associated with the polaron plus one-phonon continuum, and are a hallmark of the large polaron regime [41]. Note that our calculations are performed on lightly $n$-doped $\text{SrTiO}_{3}$, with the chemical potential lying below the lowest QP peak; therefore, as expected, the phonon satellites appear at energy *higher* than the QP peak as they correspond to the excitation of an "electronlike" QP plus one LO phonon [31,38]. On the other hand, recent angle-resolved photoemission measurements on heavily $n$-doped samples, in which the chemical potential is above the QP peak, revealed a phonon sideband roughly $\sim$100 meV *below* the QP peak, which corresponds to the excitation of a "holelike" QP plus one LO phonon [11,12,31]. The energy difference between the QP peak and phonon sideband observed in experiments is in very good agreement with the $\omega_{\text{LO-1}}=98$ meV energy difference between the QP peak and the most intense satellite peak found in our computed spectral function. We have verified that at high doping our approach also gives satellites with energies lower than the QP peak, consistent with experiment. The fact that the satellite position can be higher or lower than the QP peak depending on doping is well known [31,42], but since inverse photoemission measurements are challenging, the low doping regime we compute here is rarely probed experimentally.

To compute the spectral weights of the QP peak and incoherent part, we integrate the spectral function up to an energy $\omega$, obtaining the spectral weight $N(\omega)=\int_{-\infty}^{\omega}A(\omega')d\omega'$ given in Fig. 2(b). We find that the spectral weight of the QP peak is $\sim$0.4 at 110 K, and thus much less than the unit value of the weak $e$-ph interaction limit. As the temperature increases from 110 to 300 K, both the QP peak and the phonon satellites are broadened and smeared out [see Fig. 2(a)], but the QP spectral weight changes only slightly, primarily due to an overlap between the QP peak and the phonon satellites near 300 K. At all temperatures between 110-300 K, the QP weight is strongly renormalized to a value of $\sim$0.4, implying that (pictorially) only half of the electron resides in the QP state, while the other half contributes to the incoherent dynamical interactions with the phonons.

Figure 2(c) reveals the disappearance of the QP peak at large enough momentum $\boldsymbol{k}$ by showing how the spectral function changes as we increase $\boldsymbol{k}$ along the $\Gamma$-$M$ Brillouin zone line. We find that the QP spectral weight decreases with increasing momentum [see Fig. 2(d)] and that the QP peak ultimately disappears at $\boldsymbol{k}=0.12M$, leading to a fully incoherent spectral function at larger momenta. These so-called end points of the QP peak, which have been predicted in both the Fröhlich [43] and Holstein models [44], are yet another signature of the strong $e$-ph interactions. The decrease of the QP spectral weight and the disappearance of the QP peak at large momentum have a significant impact on transport, as we discuss below.

![](./images/812706277489639425_4.jpg)

FIG. 3. (a) Electron mobility as a function of temperature, computed using the retarded cumulant approach plus the Kubo formula (red circles) and compared with experimental values taken from Refs. [17,18]. The mobility computed in Ref. [29] using lowest-order $e$-ph scattering plus the BTE is also shown (blue pentagons). (b) The combined conduction-band spectral functions at $T=150$ K are shown together with the TDF defined in Eq. (5), which quantifies the contribution to the dc conductivity as a function of electron energy $\omega$. (c) The same quantities as in (b) shown at $T=300$ K. The zero of the energy axis is set to the energy of the lowest QP peak.

### III. ELECTRON MOBILITY

Large polaron transport is commonly believed to be the bandlike conduction of QPs with enhanced effective mass. However, this simplified picture neglects the fact that the QP weight can drop to values much smaller than one (here, to roughly 0.4, as discussed above), and that the contribution to transport from the incoherent part of the spectral function can be significant. Temperature also plays a primary role. At low temperature, the electrons occupy the low-energy QP states, and there are only few LO phonons due to their relatively high energy. As the temperature increases, thermal fluctuations push the electrons to higher energies, exciting the electrons outside of the QP peak into the incoherent regime. In addition, the number of LO phonons grows rapidly with temperature, leading to strong dynamical interactions between the electron and its phonon cloud. The incoherent contributions are thus expected to significantly influence transport at higher temperatures.

To investigate these points quantitatively in ${\text{SrTiO}}_{3}$, we compute the conductivity directly from the spectral functions—therefore including both the QP and incoherent contributions—using the Kubo formula [41]. In the absence of current-vertex corrections, the conductivity can be expressed as [45,46]
$$
\begin{aligned}
\sigma_{\alpha \beta}(\omega)=& \frac{\pi \hbar e^{2}}{V_{\mathrm{uc}}} \int d \omega^{\prime} \frac{f\left(\omega^{\prime}\right)-f\left(\omega^{\prime}+\omega\right)}{\omega} \\
& × \sum_{n \boldsymbol{k}} v_{n \boldsymbol{k}}^{\alpha} v_{n \boldsymbol{k}}^{\beta} A_{n \boldsymbol{k}}\left(\omega^{\prime}\right) A_{n \boldsymbol{k}}\left(\omega^{\prime}+\omega\right),
\end{aligned} \quad (3)
$$
where $\boldsymbol{v}_{n \boldsymbol{k}}$ is the band velocity of the electronic state $|n \boldsymbol{k}\rangle$, $f(\omega)$ is the Fermi-Dirac distribution, $V_{\text{uc}}$ is the unit cell volume, and $\alpha$ and $\beta$ are Cartesian directions. We also compute the dc conductivity, using $\sigma^{\mathrm{dc}}=\sigma(\omega \to 0)$, and the electron mobility as $\mu=\sigma^{\mathrm{dc}} / n_{c} e$, where the carrier concentration $n_{c}$ is computed as
$$
n_{c}=\sum_{n \boldsymbol{k}} \int_{-\infty}^{\infty} d \omega f(\omega) A_{n \boldsymbol{k}}(\omega). \tag{4}
$$

We perform mobility calculations in the lightly $n$-doped regime, with electron concentrations ranging between $10^{17}$–$10^{18}\ \text{cm}^{-3}$, and find that the computed mobility is nearly independent of the chosen concentration above 150 K, consistent with experimental data [17,18].

Our computed electron mobility in ${\text{SrTiO}}_{3}$ as a function of temperature is shown in Fig. 3(a) and compared with experimental data taken from Refs. [17,18]. Both the absolute value and the temperature dependence of the computed mobility are in excellent agreement with experiments. Our computed mobility at 300 K is about $8\ \text{cm}^{2}\ \text{V}^{-1}\text{s}^{-1}$ versus an experimental value of $\sim 5\ \text{cm}^{2}\ \text{V}^{-1}\text{s}^{-1}$ [17,18]. For comparison, the mobility obtained using lowest-order $e$-ph scattering plus the BTE is an order of magnitude higher than experiments [29], as also shown in Fig. 3(a).

The order-of-magnitude mobility drop from the BTE to the cumulant approach in ${\text{SrTiO}}_{3}$ is due to both the QP renormalization and the incoherent contributions. The cumulant approach clearly shows that the QP peak is strongly renormalized with significant weight transfer to higher energy incoherent satellites, and the QP peak even disappears as momentum $\boldsymbol{k}$ goes beyond the end points [see Figs. 2, 3(b), and 3(c)]. However, the BTE inherently assumes that the QP states are well defined for all bands and momentum values, so it fails to capture the contributions from the incoherent part of the spectral function, thus placing all the weight in the QP peak and significantly overestimating the mobility. Our results show unambiguously that the established lowest-order $e$-ph plus BTE approach [23–28] is accurate only in the case of weak $e$-ph interactions. Including higher-order $e$-ph processes and incoherent polaron effects via the cumulant approach

greatly improves the computed mobility in materials with strong $e$-ph coupling.

Correctly taking into account the contributions from all the phonon modes, including the soft modes [29], is also essential for predicting the electron mobility and its temperature dependence in ${\text{SrTiO}}_{3}$. Neglecting the soft mode in the calculations leads to significant errors in the computed mobility and its temperature dependence (see Fig. 5 in Appendix C), both in the BTE and in the cumulant approach. These results show that the soft modes, and not just the LO phonons as is widely believed, also contribute to charge transport in the large polaron regime.

Lastly, note also that in the weak $e$-ph coupling limit, in which the spectral function consists only of a sharp QP peak and no incoherent contributions, the expression we use for ${\sigma}^{\text{dc}}$ reduces to the conductivity obtained from the relaxation time approximation (RTA) of the BTE [45,47]. For a material with weak $e$-ph interactions and negligible polaron effects, one thus expects that the cumulant and BTE approaches predict the same transport results. We perform this sanity check for GaAs, showing that its mobility curves computed with the cumulant and BTE-RTA are in close agreement (see Fig. 6 in Appendix D). In the case of ${\text{SrTiO}}_{3}$, on the other hand, it is apparent that the BTE cannot predict the mobility correctly.

## IV. COHERENT AND INCOHERENT CONTRIBUTIONS

Our approach for computing the conductivity in the presence of polarons further allows us to resolve the coherent and incoherent contributions to transport and to uncover different transport regimes as a function of temperature. We write the dc conductivity as ${\sigma}^{\text{dc}}=\int \Phi (\omega )d\omega$, where the integrand
$$
\Phi(\omega)=\frac{\pi \hbar e^{2}}{V_{\mathrm{uc}}} \sum_{n \boldsymbol{k}} v_{n \boldsymbol{k}}^{\alpha} v_{n \boldsymbol{k}}^{\beta}|A(n \boldsymbol{k}, \omega)|^{2}\left(-\frac{\partial f(\omega)}{\partial \omega}\right), \quad(5)
$$
is referred to as the transport distribution function (TDF), and is employed here to quantify the contributions to the dc conductivity as a function of electron energy $\omega$. We analyze the TDF between 150–300 K in Figs. 3(b) and 3(c), and find that both the coherent QP peak and the incoherent part contribute to transport. At temperatures below $\sim$200 K, the TDF spans primarily the QP peaks [see Fig. 3(b)], implying that transport is dominated by the scattering of QPs with a strongly renormalized spectral weight. As the temperature increases, the high-energy tail of the TDF extends into the incoherent contributions [see Fig. 3(c)], which become important and contribute by as much as 40% to the conductivity at 300 K, as discussed below. Therefore, transport near room temperature is governed not only by the weight-renormalized QPs, but also by the incoherent phonon satellites above the QP peaks and by the polaron states at large momenta beyond the end points, where the QP peaks disappear. The picture of QP scattering is inadequate to describe transport at room temperature in ${\text{SrTiO}}_{3}$, and a more complex picture emerges in which transport is an interplay between the QP renormalization and the contributions from the incoherent phonon sidebands and from the polaron states beyond the end points, all of which are consequences of the dynamical interactions between the electrons and the phonon cloud.

![](./images/812706277489639425_5.jpg)

FIG. 4. (a) Comparison between the computed optical conductivities at 150 and 300 K. The curves were normalized to possess the same integral. (b) Computed optical conductivity divided by the dc conductivity at each temperature. (c) The inverse of the effective transport relaxation time, $\tau_{\mathrm{tr}}^{*-1}$, extracted from $\sigma(\omega)$ and shown as a function of temperature. The Planckian limit $k_{\mathrm{B}} T$ is shown with a dashed line. (d) The incoherent contribution to charge transport, quantified by the dc conductivity ratio $\sigma_{\text {inc }}^{\text {dc }} / \sigma^{\text {dc }}$ defined in the text.

These conclusions are supported by experiments on the optical conductivity. Recent experiments in ${\text{SrTiO}}_{3}$ show that the Drude peak at low frequency in the optical conductivity, which is associated with the coherent bandlike transport of QPs, loses weight for increasing temperatures up to 300 K [9,10]. Figure 4(a) compares the low-energy optical conductivities at 150 and 300 K, both computed with Eq. (3) and normalized to possess the same integral, consistent with the optical sum rule. The optical conductivities exhibit a Drude-like peak centered at zero frequency, and an incoherent shoulder structure consisting of phonon sidebands plus a broad background. We find a significant weight transfer from the Drude peak to the incoherent shoulder as the temperature increases from 150 to 300 K, in agreement with experiments [9]. The Drude peak is sharp at 150 K, but it broadens rapidly as the temperature increases [see Fig. 4(b)]. These trends confirm the transition seen in our transport results from a renormalized QP regime at low temperature to an incoherent, beyond-QP regime near room temperature.

We also extract an effective transport relaxation time, $\tau_{\mathrm{tr}}^{*}$, from the optical conductivity through the extended Drude analysis of Ref. [48]:
$$
\tau_{\mathrm{tr}}^{*}=-\frac{2}{\pi \sigma^{\mathrm{dc}}} \int_{0}^{\infty} \frac{1}{\omega^{\prime}} \frac{\partial \sigma\left(\omega^{\prime}\right)}{\partial \omega^{\prime}} d \omega^{\prime}.\qquad(6)
$$

Figure 4(c) shows the inverse of $\tau_{\text{tr}}^{*}$, namely, the effective scattering rate characterizing the width of the Drude peak. We find that this effective scattering rate increases rapidly with temperature, reaching values much greater than the QP scattering rate extracted from the QP peak of the spectral function in Fig. 2(a). Due to the uncertainty principle, in a semiclassical transport regime the scattering rate cannot exceed the so-called Planckian limit of $k_{\text{B}}T$ [30]. We find that the effective scattering rate in $\text{SrTiO}_3$ exceeds the Planckian limit $k_{\text{B}}T$ above 250 K, highlighting the beyond-quasiparticle nature of charge transport in $\text{SrTiO}_3$ near room temperature. The breaking of the Planckian limit in $\text{SrTiO}_3$ at room temperature is consistent with very recent results obtained by Mishchenko *et al.* using a model Hamiltonian [49].

Finally, one expects the incoherent contributions to transport to be significant at temperatures where the scattering rate exceeds the Planckian limit, namely above $\sim$250 K in our calculations. We quantify the incoherent contribution to transport by defining the conductivity ratio $\sigma_{\text{inc}}^{\text{dc}}/\sigma^{\text{dc}}$, where the incoherent contribution to the conductivity $\sigma_{\text{inc}}^{\text{dc}}$ is obtained by integrating the TDF at energies greater than all QP peaks ($\omega > 32$ meV in our calculations). Figure 2(d) shows that above 250 K the beyond-QP incoherent contributions amount to up to $\sim$40% of the total dc conductivity, confirming that the Planckian limit breaking is associated with a fully quantum mechanical transport regime beyond the QP scattering paradigm. While the Planckian limit breaking has been typically associated with strange metals and other strongly correlated phases of matter [50-52], our results highlight that strong $e$-ph interactions can also lead to this quantum mechanical transport regime.

### V. CONCLUSION

In summary, we developed a broadly applicable approach for computing charge transport in the large polaron regime in materials with intermediate $e$-ph coupling strength. Our calculations on $\text{SrTiO}_3$ unveil a transition from bandlike transport of strongly weight-renormalized QPs at low temperature to an incoherent transport regime beyond the QP picture near room temperature. Our approach can shed new light on broad classes of materials with polaron effects, ranging from perovskites [53] and transition metal oxides [54,55] to high-$T_c$ superconductors [56,57].

### ACKNOWLEDGMENTS

J.-J.Z. has benefited from discussion with N.-E. Lee. This work was supported by the Joint Center for Artificial Photosynthesis, a DOE Energy Innovation Hub, supported through the Office of Science of the U.S. Department of Energy under Award No. DE-SC0004993. M.B. acknowledges support by the National Science Foundation under Grant No. ACI-1642443, which provided for code development, and Grant No. CAREER-1750613, which provided for theory and method development. This work was partially supported by the Air Force Office of Scientific Research through the Young Investigator Program, Grant FA9550-18-1-0280. This research used resources of the National Energy Research Scientific Computing Center, a DOE Office of Science User Facility supported by the Office of Science of the U.S. Department of Energy under Contract No. DE-AC02-05CH11231.

### APPENDIX A: FINITE TEMPERATURE RETARDED CUMULANT APPROACH

We implement and employ a retarded cumulant approach [35,36] to compute the electron spectral function at finite temperature. The retarded cumulant approach [see Eqs. (1) and (2)] was recently employed to study the electron spectral function near the band edge in insulators at zero temperature [38]. However, the separation scheme used in Ref. [38] to compute the cumulant and the spectral function is not well behaved at finite temperature [35], where $\beta_{nk}(0) > 0$. Here, we develop a new scheme to compute the retarded Green's function at finite temperature. We rewrite Eq. (2) as

$$
C_{nk}(t)=P \int_{-\infty}^{\infty} d \omega \frac{\tilde{\beta}_{nk}(\omega)}{\omega^{2}}\left(e^{-i \omega t}-1\right)-i t \Sigma_{nk}\left(\varepsilon_{nk}\right), \quad \text{(A1)}
$$

where $\tilde{\beta}_{nk}(\omega) \equiv \beta_{nk}(\omega)-\beta_{nk}(0)$ and $P$ denotes the Cauchy principal value of the integral. The following two relations are used to derive Eq. (A1):

$$
\int_{-\infty}^{\infty} \frac{\left(e^{-i \omega t}+i \omega t-1\right)}{\omega^{2}} d \omega=-\pi t,
$$

$$
P \int_{-\infty}^{\infty} \frac{\tilde{\beta}_{nk}(\omega)}{\omega} d \omega=-\operatorname{Re} \Sigma_{nk}\left(\varepsilon_{nk}\right).
$$

We evaluate $\tilde{\beta}_{nk}(\omega)$ on a discrete frequency grid, $\omega_{l}=l \Delta \omega$ with $l$ an integer. We label the first term in Eq. (A1) as $C_{nk}^{s}(t)$ and compute it from $\tilde{\beta}_{nk}(\omega_{l})$,

$$
C_{nk}^{s}(t)=\sum_{\omega_{l} \neq 0} \frac{\tilde{\beta}_{nk}\left(\omega_{l}\right)}{\omega_{l}^{2}}\left(e^{-i \omega_{l} t}-1\right) \Delta \omega. \quad \text{(A2)}
$$

Substituting Eqs. (A1) and (A2) into Eq. (1), the retarded Green's function becomes

$$
G_{nk}^{R}(t)=-i \theta(t) e^{-i t\left(\varepsilon_{nk}+\Sigma_{nk}\left(\varepsilon_{nk}\right)\right)} e^{C_{nk}^{s}(t)}. \quad \text{(A3)}
$$

We then evaluate the spectral function by Fourier transforming to the frequency domain, and obtain

$$
A_{nk}(\omega)=A_{nk}^{0}(\omega) * A_{nk}^{s}(\omega) / 2 \pi, \quad \text{(A4)}
$$

where $*$ denotes a convolution operation; the two quantities entering this formula are

$$
A_{nk}^{0}(\omega)=\frac{-\operatorname{Im} \Sigma\left(\varepsilon_{nk}\right) / \pi}{\left(\omega-\varepsilon_{nk}-\operatorname{Re} \Sigma\left(\varepsilon_{nk}\right)\right)^{2}+\operatorname{Im} \Sigma\left(\varepsilon_{nk}\right)^{2}} \quad \text{(A5)}
$$

and $A_{nk}^{s}(\omega)$, which is the Fourier transform of $e^{C_{nk}^{s}(t)}$.

Note that $C_{nk}^{s}(t)$ defined in Eq. (A2) is periodic with a period of $\mathcal{T}=2 \pi / \Delta \omega$; we compute $e^{C_{nk}^{s}(t)}$ on a discrete time grid $t_{j}=j \Delta t$ with $j \in[-N, N]$ and $\Delta t=\mathcal{T}/(2N+1)$. It is seen from Eq. (A2) that $C_{nk}^{s}(-t_{j})=C_{nk}^{s}(t_{j})^{*}$ and $C_{nk}^{s}(0)=0$, which allows us to compute $C_{nk}^{s}(t_{j})$ only for $j \in[1, N]$ and obtain $e^{C_{nk}^{s}(t_{j})}$ on the full time grid. We then obtain $A_{nk}^{s}(\omega)$ on a frequency grid with the same step $\Delta \omega$ as $\tilde{\beta}_{nk}(\omega)$ via a discrete Fourier transform of $e^{C_{nk}^{s}(t_{j})}$. The value of $A_{nk}^{s}(\omega)$ is guaranteed to be real. We have carefully checked the convergence of $A_{nk}^{s}(\omega)$ with respect to the range and step

size of both the time and frequency grids. Specifically, we employed $\omega$ values ranging from $-0.8$ to $0.8$ eV with a small step $\Delta\omega$ of 0.05 meV and $N=32\,000$ for the time grid in our calculations.

## APPENDIX B: COMPUTATIONAL DETAILS

We carry out $ab$ initio calculations on cubic $\text{SrTiO}_3$ with a lattice parameter of $3.9$ Å. The ground-state electronic structure is computed within the Perdew-Burke-Ernzerhof generalized gradient approximation [58] of density functional theory (DFT) using the QUANTUM ESPRESSO code [59]. We employ fully-relativistic norm-conserving pseudopotentials, which include spin-orbit coupling (SOC) [60,61], together with a plane-wave basis set with a kinetic energy cutoff of 85 Ry. The anharmonic lattice-dynamical properties of cubic $\text{SrTiO}_3$ are computed using the temperature-dependent effective potential (TDEP) method [34] with $4\times4\times4$ supercells, together with a scheme we recently developed [29] to accurately include the long-range dipole-dipole contributions in the interatomic force constants.

We use our in-house developed PERTURBO code [62] to compute the lowest-order $e$-ph self-energy at temperature $T$ for the Bloch state $|nk\rangle$ with band $n$ and crystal momentum $\boldsymbol{k}$,
$$
\begin{aligned}
&\Sigma_{nk}(\omega,T)=\sum_{m,\nu\boldsymbol{q}}|g_{mn,\nu}(\boldsymbol{k},\boldsymbol{q})|^{2}\\
&\times\left[\frac{N_{\nu\boldsymbol{q}}+f_{m\boldsymbol{k}+\boldsymbol{q}}}{\omega-\varepsilon_{m\boldsymbol{k}+\boldsymbol{q}}+\omega_{\nu\boldsymbol{q}}+i\eta}+\frac{N_{\nu\boldsymbol{q}}+1-f_{m\boldsymbol{k}+\boldsymbol{q}}}{\omega-\varepsilon_{m\boldsymbol{k}+\boldsymbol{q}}-\omega_{\nu\boldsymbol{q}}+i\eta}\right],
\tag{B1}
\end{aligned}
$$
where $\varepsilon_{nk}$ is the DFT band electron energy, $\omega_{\nu\boldsymbol{q}}$ is the energy of a phonon with branch index $\nu$ and wave vector $\boldsymbol{q}$, $f_{nk}$ and $N_{\nu\boldsymbol{q}}$ are, respectively, the Fermi and Bose occupation numbers evaluated at temperature $T$, and $\eta$ is a small broadening. The key quantities are the $e$-ph coupling matrix elements, $g_{mn,\nu}(\boldsymbol{k},\boldsymbol{q})$, defined as
$$
g_{mn,\nu}(\boldsymbol{k},\boldsymbol{q})=\sqrt{\frac{\hbar}{2\omega_{\nu\boldsymbol{q}}}}\sum_{\kappa\alpha}\frac{\boldsymbol{e}_{\nu\boldsymbol{q}}^{\kappa\alpha}}{\sqrt{M_{\kappa}}}\langle m\boldsymbol{k}+\boldsymbol{q}|\partial_{q\kappa\alpha}V|nk\rangle,\quad(\text{B2})
$$
where $\partial_{q\kappa\alpha}V\equiv\sum_{p}e^{i\boldsymbol{q}\boldsymbol{R}_{p}}\partial_{p\kappa\alpha}V$, with $\partial_{p\kappa\alpha}V$ the variation of the Kohn-Sham potential for a unit displacement of the atom $\kappa$ (with mass $M_{\kappa}$ and in the unit cell at $\boldsymbol{R}_{p}$) in the $\alpha$ direction, and $\boldsymbol{e}_{\nu\boldsymbol{q}}$ is the phonon displacement eigenvector. We obtain the $e$-ph matrix elements with the method described in our recent work [29]. Briefly, we first compute the electronic wave functions $|nk\rangle$ on an $8\times8\times8$ $\boldsymbol{k}$-point grid using DFT, construct Wannier functions for the Ti-$t_{2g}$ orbitals from the three lowest conduction bands using the WANNIER90 code [63], compute $\partial_{q\kappa\alpha}V$ on an $8\times8\times8$ $\boldsymbol{q}$-point grid with density functional perturbation theory [33], and compute renormalized phonon energies $\omega_{\nu\boldsymbol{q}}(T)$ and eigenvectors $\boldsymbol{e}_{\nu\boldsymbol{q}}(T)$ with TDEP. Using these ingredients, we first evaluate the $e$-ph matrix elements in Eq. (B2) on coarse grids. Wannier interpolation together with a long-range $e$-ph correction for the polar modes [64–66] is then employed to interpolate $g_{mn,\nu}(\boldsymbol{k}\boldsymbol{q})$ for $\boldsymbol{k}$ and $\boldsymbol{q}$ points on very fine Brillouin zone grids, which are needed to converge the $e$-ph self-energy in Eq. (B1). An approach we recently developed [25] is employed to converge the imaginary part of the self-energy, $\text{Im}\Sigma_{nk}(\omega)$, which is computed off-shell on a fine energy $\omega$ grid, and the real part of the self-energy, $\text{Re}\Sigma_{nk}$, which is evaluated on-shell at the electron energy $\varepsilon_{nk}$. The spectral functions $A_{nk}(\omega)$ are then obtained using the finite temperature retarded cumulant approach described in Appendix A, using $\text{Im}\Sigma_{nk}(\omega)$ and $\text{Re}\Sigma_{nk}(\varepsilon_{nk})$ as input.

We compute spectral functions $A_{nk}(\omega)$ on fine $\boldsymbol{k}$-point grids with up to $100^{3}$ points in the Brillouin zone, which are then employed in the conductivity and mobility calculations using Eqs. (3) and (4). Note that the spectral functions depend on both the temperature $T$ and chemical potential $\mu$. For each temperature and carrier concentration $n_c$ considered in our calculations, we determine self-consistently the chemical potential $\mu(T,n_c)$ using Eq. (4); this means that the spectral functions computed using the chemical potential $\mu(T,n_c)$ give a consistent carrier concentration $n_c$.

## APPENDIX C: SOFT MODE CONTRIBUTION TO TRANSPORT

To highlight the contribution from the soft modes to charge transport in $\text{SrTiO}_3$, we compare the electron mobility computed with and without the soft mode contribution, as shown in Fig. 5. Our recent calculations using the BTE show that the ferroelectric soft mode plays an important role in transport, especially at low temperatures below 250 K, and that including the soft mode contribution is critical to obtaining an accurate temperature dependence of the electron mobility [29]. The results from the cumulant approach exhibit the same trend—neglecting the soft mode contribution leads to a significant overestimate of the mobility below 250 K and to an inaccurate temperature dependence. Although the phonon satellites in the spectral function is primarily due to the strong coupling

![](./images/812706277489639425_6.jpg)

FIG. 5. Electron mobility in $\text{SrTiO}_3$ computed using the BTE within the RTA and the cumulant approach plus the Kubo formula, compared with experimental data [17]. For both the BTE-RTA and the cumulant approach, the electron mobility obtained by excluding the contribution from the ferroelectric soft phonon mode is also shown.

between the electron and LO phonons, the ferroelectric soft mode can impact the width of the QP peak, thus contributing to charge transport.

## APPENDIX D: COMPUTED ELECTRON MOBILITY IN GaAs: BTE VERSUS CUMULANT APPROACH

The method we developed in this work, which uses the retarded cumulant approach plus the Kubo formula to compute charge transport, is general and can be applied broadly in materials with $e$-ph interactions ranging from weak to strong. To illustrate this point, we apply our approach to GaAs, a high-mobility semiconductor in which large-polaron effects are very weak. We have recently computed the temperature dependent electron mobility in GaAs using the BTE approach within the RTA [25]. With the same computational settings for the DFT and DFPT calculations as in Ref. [25], we compute the electron mobility at temperatures between 250–400 K using the cumulant approach. Figure 6(a) compares the electron mobility from the cumulant and BTE-RTA calculations with experimental data. Due to the weak $e$-ph coupling, the spectral function in GaAs consists of a sharp QP peak with near-unit spectral weight [see Fig. 6(b)], plus a weak phonon sideband at energy $\omega_{\text{LO}} = 36$ meV above the QP peak, where $\omega_{\text{LO}}$ is the LO phonon energy in GaAs. The cumulant approach and the BTE-RTA give mobility results in close agreement with each other, as is expected in materials with weak $e$-ph coupling. We have thus shown that our implementation of the cumulant plus Kubo approach without current-vertex corrections reduces to the RTA solution of the BTE in the weak $e$-ph coupling limit [45,47].

For linear-response theory to be consistent with the BTE, the Kubo formula with current-vertex corrections should reduce in the weak $e$-ph coupling limit to the full solution of the BTE, e.g., the solution obtained in practice with an iterative method [27]. Our calculation on GaAs in the absence of current-vertex corrections shows good agreement with the BTE-RTA, and similarly we expect that including the current-vertex corrections would give results consistent with the iterative BTE solution for GaAs. In the case of ${\text{SrTiO}}_{3}$, the BTE-RTA and the iterative solution of the BTE produce very similar results as we have shown previously [29]. Therefore the current-vertex corrections are not essential for ${\text{SrTiO}}_{3}$ and are neglected in our calculations.

![](./images/812706277489639425_7.jpg)

FIG. 6. (a) Electron mobility in GaAs as a function of temperature, computed using the cumulant approach plus the Kubo formula (red circles), the BTE approach within the RTA (blue pentagons), and compared with experimental values taken from Refs. [67,68]. (b) Spectral function for the electronic state at the conduction band minimum in GaAs, computed at 300 K using the cumulant approach. Note the small phonon sidebands at energy $\omega_{\text{LO}} = 36$ meV above the QP peak.

[1] J. M. Ziman, *Electrons and Phonons: The Theory of Transport Phenomena in Solids* (Oxford University Press, New York, 2007).

[2] H. Fröhlich, Electrons in lattice fields, *Adv. Phys.* **3**, 325 (1954).

[3] T. Holstein, Studies of polaron motion, *Ann. Phys.* **8**, 343 (1959).

[4] J. T. Devreese and A. S. Alexandrov, Fröhlich polaron and bipolaron: recent developments, *Rep. Prog. Phys.* **72**, 066501 (2009).

[5] D. Emin, *Polarons* (Cambridge University Press, Cambridge, UK, 2012).

[6] G. Iadonisi, J. Ranninger, and G. De Filippis, *Polarons in Bulk Materials and Systems with Reduced Dimensionality*, Proceedings of The International School of Physics “Enrico Fermi”, Vol. 161 (IOS, Amsterdam, 2006).

[7] S. Fratini, D. Mayou, and S. Ciuchi, The transient localization scenario for charge transport in crystalline organic materials, *Adv. Funct. Mater.* **26**, 2292 (2016).

[8] A. S. Mishchenko, N. Nagaosa, G. De Filippis, A. de Candia, and V. Cataudella, Mobility of Holstein Polaron at Finite Temperature: An Unbiased Approach, *Phys. Rev. Lett.* **114**, 146401 (2015).

[9] J. L. M. van Mechelen, D. van der Marel, C. Grimaldi, A. B. Kuzmenko, N. P. Armitage, N. Reyren, H. Hagemann, and I. I. Mazin, Electron-Phonon Interaction and Charge Carrier Mass Enhancement in ${\text{SrTiO}}_{3}$, *Phys. Rev. Lett.* **100**, 226403 (2008).

[10] J. T. Devreese, S. N. Klimin, J. L. M. van Mechelen, and D. van der Marel, Many-body large polaron optical conductivity in ${\text{SrTi}}_{1-x}{\text{Nb}}_{x}{\text{O}}_{3}$, *Phys. Rev. B* **81**, 125119 (2010).

[11] C. Chen, J. Avila, E. Frantzeskakis, A. Levy, and M. C. Asensio, Observation of a two-dimensional liquid of Fröhlich polarons at the bare ${\text{SrTiO}}_{3}$ surface, *Nat. Commun.* **6**, 9585 (2015).

[12] Z. Wang, S. McKeown Walker, A. Tamai, Y. Wang, Z. Ristic, F. Y. Bruno, A. de la Torre, S. Riccò, N. C. Plumb, M. Shi *et al.*, Tailoring the nature and strength of electron-phonon interactions in the ${\text{SrTiO}}_{3}(001)$ 2D electron liquid, *Nat. Mater.* **15**, 835 (2016).

[13] H. P. R. Frederikse and W. R. Hosler, Hall mobility in ${\text{SrTiO}}_{3}$, *Phys. Rev.* **161**, 822 (1967).

[14] S. H. Wemple, M. DiDomenico, and A. Jayaraman, Electron scattering in perovskite-oxide ferroelectric semiconductors, *Phys. Rev.* **180**, 547 (1969).

[15] A. Verma, A. P. Kajdos, T. A. Cain, S. Stemmer, and D. Jena, Intrinsic Mobility Limiting Mechanisms in Lanthanum-Doped Strontium Titanate, Phys. Rev. Lett. 112, 216601 (2014).

[16] W. X. Zhou, J. Zhou, C. J. Li, S. W. Zeng, Z. Huang et al., Electron-soft phonon scattering in $n$-type $\text{SrTiO}_3$, Phys. Rev. B 94, 195122 (2016).

[17] T. A. Cain, A. P. Kajdos, and S. Stemmer, La-doped $\text{SrTiO}_3$ films with large cryogenic thermoelectric power factors, Appl. Phys. Lett. 102, 182101 (2013).

[18] X. Lin, C. W. Rischau, L. Buchauer, A. Jaoui, B. Fauqué, and K. Behnia, Metallicity without quasi-particles in room-temperature strontium titanate, npj Quantum Mater. 2, 41 (2017).

[19] C. Collignon, X. Lin, C. W. Rischau, B. Fauqué, and K. Behnia, Metallicity and superconductivity in doped strontium titanate, Annu. Rev. Condens. Matter Phys. 10, 25 (2019).

[20] E. Mikheev, B. Himmetoglu, A. P. Kajdos, P. Moetakef, T. A. Cain, C. G. V. d. Walle, and S. Stemmer, Limitations to the room temperature mobility of two- and three-dimensional electron liquids in $\text{SrTiO}_3$, Appl. Phys. Lett. 106, 062102 (2015).

[21] N. E. Hussey, K. Takenaka, and H. Takagi, Universality of the Mott-Ioffe-Regel limit in metals, Philos. Mag. 84, 2847 (2004).

[22] J. J. Devreese, Fröhlich Polarons. Lecture course including detailed theoretical derivations, arXiv:1611.06122.

[23] M. Bernardi, First-principles dynamics of electrons and phonons, Eur. Phys. J. B 89, 239 (2016).

[24] J. I. Mustafa, M. Bernardi, J. B. Neaton, and S. G. Louie, Ab initio electronic relaxation times and transport in noble metals, Phys. Rev. B 94, 155105 (2016).

[25] J.-J. Zhou and M. Bernardi, Ab initio electron mobility and polar phonon scattering in GaAs, Phys. Rev. B 94, 201201(R) (2016).

[26] T.-H. Liu, J. Zhou, B. Liao, D. J. Singh, and G. Chen, First-principles mode-by-mode analysis for electron-phonon scattering channels and mean free path spectra in GaAs, Phys. Rev. B 95, 075206 (2017).

[27] J. Ma, A. S. Nissimagoudar, and W. Li, First-principles study of electron and hole mobilities of Si and GaAs, Phys. Rev. B 97, 045201 (2018).

[28] N.-E. Lee, J.-J. Zhou, L. A. Agapito, and M. Bernardi, Charge transport in organic molecular semiconductors from first principles: The bandlike hole mobility in a naphthalene crystal, Phys. Rev. B 97, 115203 (2018).

[29] J.-J. Zhou, O. Hellman, and M. Bernardi, Electron-Phonon Scattering in the Presence of Soft Modes and Electron Mobility in $\text{SrTiO}_3$ Perovskite from First Principles, Phys. Rev. Lett. 121, 226603 (2018).

[30] S. A. Hartnoll, Theory of universal incoherent metallic transport, Nat. Phys. 11, 54 (2015).

[31] A. Damascelli, Z. Hussain, and Z.-X. Shen, Angle-resolved photoemission studies of the cuprate superconductors, Rev. Mod. Phys. 75, 473 (2003).

[32] R. M. Martin, L. Reining, and D. M. Ceperley, Interacting Electrons: Theory and Computational Approaches (Cambridge University Press, Cambridge, UK, 2016).

[33] S. Baroni, S. de Gironcoli, A. Dal Corso, and P. Giannozzi, Phonons and related crystal properties from density-functional perturbation theory, Rev. Mod. Phys. 73, 515 (2001).

[34] O. Hellman, I. A. Abrikosov, and S. I. Simak, Lattice dynamics of anharmonic solids from first principles, Phys. Rev. B 84, 180301(R) (2011).

[35] J. J. Kas, J. J. Rehr, and L. Reining, Cumulant expansion of the retarded one-electron Green function, Phys. Rev. B 90, 085112 (2014).

[36] J. J. Kas and J. J. Rehr, Finite Temperature Green's Function Approach for Excited State and Thermodynamic Properties of Cool to Warm Dense Matter, Phys. Rev. Lett. 119, 176403 (2017).

[37] L. Hedin, On correlation effects in electron spectroscopies and the GW approximation, J. Phys.: Condens. Matter 11, R489 (1999).

[38] J. P. Nery, P. B. Allen, G. Antonius, L. Reining, A. Miglio, and X. Gonze, Quasiparticles and phonon satellites in spectral functions of semiconductors and insulators: Cumulants applied to the full first-principles theory and the Fröhlich polaron, Phys. Rev. B 97, 115145 (2018).

[39] M. Berciu, Green's Function of a Dressed Particle, Phys. Rev. Lett. 97, 036402 (2006).

[40] H. Hübener, U. De Giovannini, and A. Rubio, Phonon driven Floquet matter, Nano Lett. 18, 1535 (2018).

[41] G. D. Mahan, Many-Particle Physics, 3rd ed. (Springer US, New York, 2000).

[42] J. S. Zhou, M. Gatti, J. J. Kas, J. J. Rehr, and L. Reining, Cumulant Green's function calculations of plasmon satellites in bulk sodium: Influence of screening and the crystal environment, Phys. Rev. B 97, 035137 (2018).

[43] A. S. Mishchenko, N. V. Prokof'ev, A. Sakamoto, and B. V. Svistunov, Diagrammatic quantum Monte Carlo study of the Fröhlich polaron, Phys. Rev. B 62, 6317 (2000).

[44] G. L. Goodvin and M. Berciu, The end points in the dispersion of Holstein polarons, Europhys. Lett. 92, 37006 (2010).

[45] E. N. Economou, Electrical conductivity and Green's functions, in Green's Functions in Quantum Physics (Springer, Berlin, Heidelberg, 2006), Chap. 8, pp. 173-198.

[46] D. N. Basov, R. D. Averitt, D. van der Marel, M. Dressel, and K. Haule, Electrodynamics of correlated electron materials, Rev. Mod. Phys. 83, 471 (2011).

[47] P. B. Allen, Electron self-energy and generalized Drude formula for infrared conductivity of metals, Phys. Rev. B 92, 054305 (2015).

[48] X. Deng, A. Sternbach, K. Haule, D. N. Basov, and G. Kotliar, Shining Light on Transition-Metal Oxides: Unveiling the Hidden Fermi Liquid, Phys. Rev. Lett. 113, 246404 (2014).

[49] A. S. Mishchenko, L. Pollet, N. V. Prokof'ev, A. Kumar, D. L. Maslov, and N. Nagaosa, Polaron Mobility in the "Beyond Quasiparticles" Regime, Phys. Rev. Lett. 123, 076601 (2019).

[50] V. J. Emery and S. A. Kivelson, Superconductivity in Bad Metals, Phys. Rev. Lett. 74, 3253 (1995).

[51] O. Gunnarsson, M. Calandra, and J. E. Han, Colloquium: Saturation of electrical resistivity, Rev. Mod. Phys. 75, 1085 (2003).

[52] J. A. N. Bruin, H. Sakai, R. S. Perry, and A. P. Mackenzie, Similarity of scattering rates in metals showing T-linear resistivity, Science 339, 804 (2013).

[53] K. Miyata, T. L. Atallah, and X.-Y. Zhu, Lead halide perovskites: Crystal-liquid duality, phonon glass electron

crystals, and large polaron formation, Sci. **Adv. 3**, e1701469 (2017).

[54] S. Moser, L. Moreschini, J. Jaćimović, O. S. Barišić, H. Berger, A. Magrez *et al.*, Tunable Polaronic Conduction in Anatase TiO₂, **Phys. Rev. Lett. 110**, 196403 (2013).

[55] C. Cancellieri, A. S. Mishchenko, U. Aschauer, A. Filippetti, C. Faber, O. S. Barišić, V. A. Rogalev, T. Schmitt, N. Nagaosa, and V. N. Strocov, Polaronic metal state at the LaAlO₃/SrTiO₃ interface, **Nat. Commun. 7**, 10386 (2016).

[56] A. Lanzara, P. Bogdanov, X. Zhou, S. Kellar, D. Feng, E. Lu, T. Yoshida, H. Eisaki, A. Fujimori, K. Kishio *et al.*, Evidence for ubiquitous strong electron–phonon coupling in high-temperature superconductors, **Nature (London) 412**, 510 (2001).

[57] A. Legros, S. Benhabib, W. Tabis, F. Laliberté, M. Dion, M. Lizaire, B. Vignolle, D. Vignolles, H. Raffy, Z. Li *et al.*, Univer-sal *T*-linear resistivity and planckian dissipation in overdoped cuprates, **Nat. Phys. 15**, 142 (2019).

[58] J. P. Perdew, A. Ruzsinszky, G. I. Csonka, O. A. Vydrov, G. E. Scuseria, L. A. Constantin, X. Zhou, and K. Burke, Restoring the Density-Gradient Expansion for Exchange in Solids and Surfaces, **Phys. Rev. Lett. 100**, 136406 (2008).

[59] P. Giannozzi, S. Baroni, N. Bonini, M. Calandra, R. Car *et al.*, QUANTUM ESPRESSO: A modular and open-source software project for quantum simulations of materials, **J. Phys.: Condens. Matter 21**, 395502 (2009).

[60] D. R. Hamann, Optimized norm-conserving Vanderbilt pseudopotentials, **Phys. Rev. B 88**, 085117 (2013).

[61] M. J. van Setten, M. Giantomassi, E. Bousquet, M. J. Verstraete, D. R. Hamann *et al.*, The PseudoDojo: Training and grading a 85 element optimized norm-conserving pseudopotential table, **Comput. Phys. Commun. 226**, 39 (2018).

[62] The code employed in this work will be released in the future at http://perturbo.caltech.edu.

[63] A. A. Mostofi, J. R. Yates, G. Pizzi, Y.-S. Lee, I. Souza, D. Vanderbilt, and N. Marzari, An updated version of wannier90: A tool for obtaining maximally-localised Wannier functions, **Comput. Phys. Commun. 185**, 2309 (2014).

[64] F. Giustino, M. L. Cohen, and S. G. Louie, Electron-phonon interaction using Wannier functions, **Phys. Rev. B 76**, 165108 (2007).

[65] J. Sjakste, N. Vast, M. Calandra, and F. Mauri, Wannier interpolation of the electron-phonon matrix elements in polar semiconductors: Polar-optical coupling in GaAs, **Phys. Rev. B 92**, 054307 (2015).

[66] C. Verdi and F. Giustino, Fröhlich Electron-Phonon Vertex from First Principles, **Phys. Rev. Lett. 115**, 176401 (2015).

[67] P. Blood, Electrical properties of *n*-type epitaxial GaAs at high temperatures, **Phys. Rev. B 6**, 2257 (1972).

[68] K. H. Nichols, C. M. L. Yee, and C. M. Wolfe, High-temperature carrier transport in *n*-type epitaxial GaAs, **Solid-State Electron. 23**, 109 (1980).