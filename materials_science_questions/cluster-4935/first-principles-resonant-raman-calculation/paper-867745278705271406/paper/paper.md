
# Strong exciton regulation of Raman scattering in monolayer dichalcogenides

Yuanxi Wang \( ^{*} \) 

Department of Physics, Pennsylvania State University, University Park, Pennsylvania 16802, USA
2-Dimensional Crystal Consortium, Pennsylvania State University, University Park, Pennsylvania 16802 and Material Research Institute, Pennsylvania State University, University Park, Pennsylvania 16802

Bruno R. Carvalho

Departamento de Física, Universidade Federal do Rio Grande do Norte, Natal, Rio Grande do Norte 59078-970, Brazil

Vincent H. Crespi \( ^{1} \) 

Department of Physics, Pennsylvania State University, University Park, Pennsylvania 16802, USA
Department of Materials Science and Engineering, Pennsylvania State University, University Park, Pennsylvania 16802, USA
Department of Chemistry, Pennsylvania State University, University Park, Pennsylvania 16802, USA and
2-Dimensional Crystal Consortium, Pennsylvania State University, University Park, Pennsylvania 16802

The weakly screened electron-hole interactions in an atomically thin semiconductor not only downshift its excitation spectrum from a quasiparticle one, but also redistribute excitation energies and wavefunction characters with profound effects on diverse modes of material response, including the exciton-phonon scattering processes accessible to resonant Raman measurements. Here we develop a first-principles framework to calculate frequency-dependent resonant Raman intensities that includes excitonic effects and goes beyond the Placke approximation. We show how excitonic effects in  \( MoS_{2} \)  strongly regulate Raman scattering amplitudes and thereby explain the puzzling near-absence of resonant Raman response around the A and B excitons (which produce very strong signals in optical absorption), and also the pronounced strength of the resonant Raman response from the C exciton. Furthermore, this efficient perturbative approach reduces the number of GW-BSE calculations from two per Raman mode (in finite displacement) to one for all modes and affords natural extension to higher-order resonant Raman processes.

Low-energy excitations of two-dimensional semiconductors such as  \( MoS_{2} \)  are dominated by very strong excitonic effects [1, 2]. While excitonic resonances are evident from absorption spectroscopy [3], resonant Raman spectroscopy offers a more multifaceted perspective: the Raman intensity of a phonon mode plotted against laser energies (Raman excitation profile) not only reveals excitonic resonances with resolutions on par with absorption, but also reflects exciton-phonon coupling strengths [4, 5]. Raman features emerging upon reaching resonance furthermore capture finite-momentum processes such as higher-order Raman scattering and defect scattering [6–10], both key processes in valleys [5, 11, 12]. The appeal of these rich outputs, combined with the procedural simplicity of Raman measurements (perhaps best attested by Raman's original discovery using sunlight, distilled liquids, and a human eye [13]) contributes to its wide usage. Spectral features in Raman excitation profiles are generally aligned in energy with absorption features for molecules [14–16] and 3D bulk solids [17], with intensities of similar orders of magnitude, as modulated by electron-phonon interactions. This expectation is confounded by the puzzling near-absence of Raman intensity measured at the A/B exciton energies and the disproportionately higher Raman intensity measured at the C exciton in  \( MoS_{2} \)  [6, 18]. This anomaly in 2D semiconductors suggests an unidentified regulating effect by excitons.

Despite the rich experimental data on Raman measurements of 2D solids, the role of excitons on Raman spectra is rarely modeled at a first-principles level beyond calculating shifted resonance energies, because of the high computational cost of many-body perturbation theory calculations and the sparsity of implementations that consolidate electron-phonon and many-body phenomena. One recent important theoretical advance  \( [19] \)  (implemented in  \( [20, 21] \) ) used finite differences through solution of the Bethe-Salpeter equation (BSE) on the quasiparticle (GW) band structure, but employed a quasi-static Placzek approximation that is only valid in the non-resonant regime. Here we follow the generalized approach of Ref.  \( [22] \) , valid for solids in the resonant regime, to develop a perturbation framework that goes beyond the Placzek approximation and includes electron-hole interactions. Both ingredients are crucial to capturing exciton-regulated Raman scattering in  \( MoS_{2} \) , including dramatic differences in the strength of the resonant response in the vicinity of the A/B and C excitons that agree with experiments. We show that band-extrema electron-hole pairs such as the A/B excitons suppress Raman response due to their energies being well separated from the rest of the exciton spectrum, and that parallel-band electron-hole pairs such as the C exciton amplify Raman response due to their bunching of energies causing strong rehybridization during atomic vibration.

We first explain the detailed theoretical and computational basis of the calculations; readers interested primarily in the results and physical interpretation of excitonic effects in resonant Raman spectra may ad-
 

vance to Fig. 1 and the associated discussion. First-principles Raman spectra calculations are most straightforward for Raman shifts, routinely achieving excellent agreement with experiments  \( [23–25] \) . Raman intensities are usually computed within the non-resonant Placzek approximation: since the scattered light intensity is proportional to the electronic susceptibility  \( \chi(\omega) \)  periodically modified by atomic vibrations ( \( \omega \)  is the incident light frequency), a product-to-sum identity converts the scattered  \( \cos(\omega_{\mathrm{phonot}}t)\cos(\omega t) \)  wave into Stokes and anti-Stokes components. The scattering amplitude depends on how strongly  \( \chi \)  is changed by vibrations  \( \xi \) , i.e.  \( |d\chi/d\xi|^{2} \propto |d\epsilon/d\xi|^{2} \) , where  \( \epsilon(\omega) \)  is the dielectric function  \( \epsilon(\boldsymbol{\omega}) = 1 + \sum_{S} |\langle0|\mathbf{r}|S\rangle|^{2}/(\omega_{S} - \omega - i\gamma) \)  and S runs over all excitations (the "negative frequency" contribution is suppressed for clarity but is included in all calculations). This derivative has been calculated using the second derivative of the electronic density matrix  \( [26, 27] \) , the "2n+1" theorem  \( [28] \) , or finite differences of the static dielectric tensor  \( [24, 29] \)  (calculated from density functional perturbation theory  \( [30] \) ). The derivative can also be expanded using perturbation theory, i.e. by treating  \( \omega_{S} \)  and the matrix elements separately,

 \[ \begin{aligned}\frac{d\epsilon(\omega)}{d\xi}=&\sum_{S}\left(\frac{\partial\epsilon}{\partial\omega_{S}}\frac{d\omega_{S}}{d\xi}+\frac{1}{\omega_{S}-\omega-i\gamma}\frac{d\left|\langle0|\mathbf{r}\left|S\right\rangle|^{2}\right|}{d\xi}\right)\\\equiv&d_{2}+d_{3}.\end{aligned} \quad (1) \] 

The former group of “two-band terms”

 \[ d_{2}=-\sum_{S}\frac{\langle0|\mathbf{r}\left|S\right\rangle\langle S|\partial H\left|S\right\rangle\langle\dot{S}|\mathbf{r}\left|0\right\rangle}{(\omega_{S}-\omega-i\gamma)^{2}} \quad (2) \] 

involves only transitions between pairs of bands. The latter group of “three-band terms” (see Supplemental Materials)

 \[ \begin{aligned}d_{3}=&\sum_{S^{\prime}\neq S}\frac{-1}{\omega_{S}-\omega-i\gamma}\left(\frac{\langle0|\mathbf{r}\left|S^{\prime}\right\rangle\langle S^{\prime}|\partial H\left|S\right\rangle\langle S|\mathbf{r}\left|0\right\rangle}{\omega_{S^{\prime}}-\omega_{S}}\right)\\&+\sum_{S\neq S^{\prime}}\frac{1}{\omega_{S^{\prime}}-\omega-i\gamma}\left(\frac{\langle0|\mathbf{r}\left|S^{\prime}\right\rangle\langle S^{\prime}|\partial H\left|S\right\rangle\langle S|\mathbf{r}\left|0\right\rangle}{\omega_{S^{\prime}}-\omega_{S}}\right)\\\equiv&\sum_{S\neq S^{\prime}}-\frac{\langle0|\mathbf{r}\left|S^{\prime}\right\rangle\langle S^{\prime}|\partial H\left|S\right\rangle\langle S|\mathbf{r}\left|0\right\rangle}{(\omega_{S^{\prime}}-\omega-i\gamma)(\omega_{S}-\omega-i\gamma)}\end{aligned} \quad (3) \] 

contains transitions between three states. So far the expressions are general: if all quantities are calculated at the DFT level, the Hamiltonian  \( H = H^{DFT} \)  and  \( |S\rangle \)  are free electron-hole transitions separated by  \( \omega_{S} \) ; if calculated at the BSE level,  \( H = H^{BSE} \)  and  \( |S\rangle \)  are excitonic wavefunctions with eigenvalues  \( \omega_{S} \) . Physically, two- and three-band terms respectively represent contributions from the oscillating excitation eigenvalues (Kohn-Sham eigenvalues or BSE eigenvalues) and the oscillatory rehybridization of wavefunctions (Kohn-Sham orbitals or BSE eigenvectors) [31]. By combining the  \( d_{2} \)  and  \( d_{3} \)  terms we recover the usual perturbation expression for Raman susceptibility  \( \alpha \) , ignoring small phonon energies,

 \[ \alpha_{\mathrm{p e r t r u b.}}\propto\sum_{S,S^{\prime}}\frac{\langle0|\mathbf{r}|S^{\prime}\rangle\langle S^{\prime}|\partial H|S\rangle\langle S|\mathbf{r}|0\rangle}{(\omega_{S^{\prime}}-\omega-i\gamma)(\omega_{S}-\omega-i\gamma)}. \quad (4) \] 

Three-band terms are often neglected due to the apparent squared denominator of the two-band terms (see Eqns. 1 and 2) [20]; the final expanded expression shows that three-band terms become important when the intervals between excitation energies are small.

So long as laser energies  \( \omega \)  are away from excitation levels so that  \( \omega_{phonon} \ll |\omega - \omega_{S} + i\gamma| \) , the Placzek approximation holds [22] and finite-displacement calculations using static dielectric tensors [24, 32] agree qualitatively with Raman intensities measured at finite (but sub-bandgap)  \( \omega \) , due to the near-constant dielectric function in this regime. The use of Placzek approximation in the resonant regime [19, 33] was argued to be problematic in Ref. [22], where a more rigorous expression is derived that is equivalent to keeping only the three-band terms  \( d_{3} \) . These  \( d_{3}^{2} \)  terms correspond to the so-called “Albrecht B/C terms” (or Herzberg-Teller terms) in the vibronic theory for resonant Raman intensities in molecules accounting for nuclear wavefunctions [34–36]. The seemingly missing “Albrecht A terms” (or Condon terms) [36] only arise for excitations with finite Frank-Condon shifts and is negligible for delocalized vibrations in solids [37, 38] (and even for localized vibrations near certain common defects in  \( MoS_{2} \)  [39]).

Since  \( d_{3} \)  readily separates from  \( d_{2} \)  in the perturbation approach, we derive the single-particle expansion for both at the BSE level and numerically verify that their sum matches the spectra obtained from finite displacements within the Placzek approximation and that, for  \( \omega \rightarrow 0 \) ,  \( d_{3} \)  (general) and  \( d_{2} + d_{3} \)  (Placzek) converge to the same value, i.e.  \( d_{2} \)  goes to zero. With the optical matrix elements in Eqn. 4 readily available in existing GW-BSE codes, we focus on evaluating the exciton-phonon coupling matrix elements. For the derivative of the exciton Hamiltonian  \( \partial H^{BSE} \)  within the Tamm-Dancoff approximation, we neglect the contribution from the derivative of the BSE kernel  \( \partial K \)  [40], neglect the derivative of the quasiparticle correction by using  \( \partial H^{QP} \approx \partial H^{DFT} \)  (as validated in Refs. [40, 41]) so that

 \[ \begin{align*}d_{2}=&\sum_{S,vck}\frac{|\langle0|\mathbf{r}\left|S\right\rangle|^{2}\ |\langle S|vck\rangle|^{2}}{(\omega_{S}-\omega-i\gamma)^{2}}\\&\times\left[\langle ck|\partial H^{\mathrm{DFT}}|ck\rangle-\langle vk|\partial H^{\mathrm{DFT}}|vk\rangle\right]\end{align*} \quad (5) \] 

Here we neglect  \( c \neq c' \)  and  \( v \neq v' \)  terms in Ref. [40] (DFT-level “three-band” terms) since they only contribute significantly when the energy separation between bands is similar to phonon energies; for the low-energy electronic structure of  \( MoS_{2} \) , most band-pairs of small
 

separation are up-down spin copies forbidding interband scattering, with the exception of the valence band top being split by spin-orbit interaction. Although in general bands split by spin-orbit coupling allow interband scattering (yielding significant DFT-level “three-band” terms  \( [31, 42] \) ), the spin-orbit Hamiltonian near the valleys in  \( MoS_{2} \)  only involves  \( \sigma_{z} \)  so that spins components are decoupled  \( [1, 43] \) . This approximation is numerically justified later. The  \( d_{3} \)  terms involve

 \[ \begin{align*}\langle S^{\prime}|\partial H^{\mathrm{BSE}}|S\rangle&\approx\sum_{vv^{\prime}cc^{\prime}k}\langle S^{\prime}|vck\rangle\langle v^{\prime}c^{\prime}k|S\rangle\\\times\left[\langle ck|\partial H^{\mathrm{DFT}}|c^{\prime}k\rangle\delta_{vv^{\prime}}-\langle v^{\prime}k|\partial H^{\mathrm{DFT}}|vk\rangle\delta_{cc^{\prime}}\right].\end{align*} \quad (6) \] 

Again neglecting  \( c \neq c' \)  and  \( v \neq v' \)  terms and substituting into Eqn. 3 gives

 \[ \begin{align*}d_{3}=&\sum_{S\neq S^{\prime},vck}\frac{\langle0|\mathbf{r}|S^{\prime}\rangle\langle S|\mathbf{r}|0\rangle S_{vck}S_{vck}^{\prime*}}{\left(\omega_{S}-\omega-i\gamma\right)\left(\omega_{S^{\prime}}-\omega-i\gamma\right)}\\&\times\left[\langle ck|\partial H^{\mathrm{DFT}}|ck\rangle-\langle vk|\partial H^{\mathrm{DFT}}|vk\rangle\right].\end{align*} \quad (7) \] 

All calculations will follow Eqns. 5 and 7.

All GW-BSE calculations are performed using the BerkeleyGW package  \( [44, 45] \)  based on Kohn-Sham eigenvalues and orbitals obtained within the local density approximation, using Quantum ESPRESSO  \( [46] \) . An energy cutoff of 24 Ry, 500 empty bands, and a  \( 12 \times 12 \times 1 \)  k-point grid was used for the dielectric matrix and quasiparticle self-energy, where the Coulomb interaction is truncated in the out-of-plane direction  \( [47] \) . The static remainder technique  \( [48] \)  accelerates convergence of the quasiparticle gap. BSE matrix elements are assembled using 3 valence bands and 4 conduction bands on the same grid and interpolated onto a  \( 40 \times 40 \times 1 \)  grid for diagonalization (Haydock iteration is not used because BSE eigenvectors are needed). The Supplemental Material contains details on convergence tests for the above parameters and all calculations involving phonons. Finally, summation over  \( S \neq S' \)  terms are limited to eigenvalue pairs no further apart than 0.3 eV; exciton pairs separated further contribute negligibly due to large denominators in Eqn. 7 and their constituent single-particle transitions being from different bands. Increasing this convergence parameter to 0.4 eV changes Raman intensities by at most 2% (for any laser frequency). We include 800 excitonic states to converge Raman intensities within the 0–3.5 eV spectral range.

The calculated Raman intensities  \( |\alpha(\omega)|^{2} \)  for the out-of-plane  \( A_{1}^{\prime} \)  mode in Fig. 1 shows that combining  \( |d_{2}|^{2} \)  (blue dashed) and  \( |d_{3}|^{2} \)  terms (red solid) from the perturbation approach into  \( |d_{2} + d_{3}|^{2} \)  (green solid) yields good agreement with the finite displacement spectrum (filled green) from pre-resonance (<1.5 eV) well into the resonant regime, and that two-band terms correctly converge

![](./images/867745278705271406_1.jpg)

FIG. 1. Resonant Raman intensities of the out-of-plane  \( A_{1}^{\prime} \)  mode in  \( MoS_{2} \)  calculated as a function of the laser energy. Combining two-band  \( |d_{2}|^{2} \)  (blue dashed) and three-band  \( |d_{3}|^{2} \)  terms (red solid) calculated from perturbation theory into  \( |d_{2} + d_{3}|^{2} \)  (green solid) correctly matches the result from finite displacements (filled light green). Only the three-band plot is to be compared with experiments: Raman intensity is suppressed at the A/B excitons and amplified at the C exciton. The lower panel shows A/B exciton eigenvalues far below all others and eigenvalues near the C exciton bunched together.

to zero for vanishing laser energies. These agreements are absolute, i.e. with no adjustable rescaling parameter. While the exclusion of  \( c \neq c' \)  and  \( v \neq v' \)  terms (DFT-level three-band terms) proved valid,  \( S \neq S' \)  terms (BSE level three-band terms) contribute significantly near the C exciton energy  \( \sim 2.4 \)  eV. Optical transitions within the near-parallel valence and conduction bands along  \( \Gamma - K \)  (see band structure in the Supplemental Material) yield a peak in the joint density of states and hence also in the absorbance spectra, ignoring excitonic effects, near 4 eV (blue hollow in inset of Fig. 2). Including excitonic effects, these transitions are constituents of the C excitons with BSE eigenvalues bunched near 2.4 eV [1] (red hollow in Fig. 2, truncated within its range of convergence). This bunching does not cause an order-of-magnitude change in the absorbance spectral features (whose integral is constrained by the f-sum rule [49]), apart from an overall redshift due to the exciton binding energy and a redistribution of spectral weight rendering exciton resonances sharper than single-particle features. However, as in standard perturbation theory where smaller eigenvalue intervals lead to wavefunctions being more strongly perturbed, bunched BSE eigenvalues cause strong rehybridization of excitonic states during atomic vibration (i.e. decreased denominators  \( \omega_{S'} - \omega_{S} \)  in the first line of Eqn. 3) and regroups what used to be independent transitions at different k-points (which cannot scatter into each other by a  \( \Gamma \)  phonon) into excitonic states.
 

all with zero momenta (which allows inter-scattering i.e. increased numerator in Eqn. 7). Therefore, three-band terms contribute an order-of-magnitude amplification in Raman intensities around the C exciton resonance. This can be seen even in the results from finite displacements in Fig. 2, where Raman intensities without electron-hole interaction near 4 eV (blue filled) are amplified to form the highest Raman peak with electron-hole interaction near 2.4 eV (red filled); comparing the more rigorous three-band spectra would yield the same conclusion. In stark contrast, the A and B excitons – each doubly degenerate (two valleys) – are well separated from other excitations, so they only contribute to two-band terms (dashed blue in Fig. 1). Since only three-band terms are valid for on-resonance frequencies, the orphaned A and B states should not appear in an experimental measurement. Thus the final frequency-dependent Raman intensity  \( |d_{3}|^{2} \)  (red in Fig. 1) is suppressed at the A/B excitons and amplified at the C exciton. In this way, our perturbation method reveals how spectral features in resonant Raman characterise not only the exciton spectrum and wavefunction character, but also how exciton-phonon coupling enables inter-state scattering.

![](./images/867745278705271406_2.jpg)

FIG. 2. Raman intensities with (red) and without (blue) excitonic effects, showing the amplified Raman response at the C exciton compared with the Raman intensities calculated without excitonic effects. The inset compares the absorbance spectra with (red, truncated within its range of convergence) and without (blue) electron-hole interaction, where excitonic effects redistribute spectral weights without enhancement. Both Raman intensities shown are from finite displacements; the visible A/B resonances here should be suppressed in the more rigorous three-band spectra  \( \left(\left|d_{3}\right|^{2}\right. \)  in Fig. 1).

We now compare with experiments in Fig. 3 and demonstrate that agreement is only achieved for the beyond-Placzek treatment of Raman intensity including excitonic effects. Two sets of experimental data on the frequency-dependent  \( A_{1}^{\prime} \)  mode intensity from Refs. [6, 18] are aligned at the 2.8 eV data point and normalized in intensity by the Raman peak of silicon at  \( 520 \, cm^{-1} \)  (which has its own known frequency dependence) to yield the modulus-squared of the Raman susceptibility  \( |\alpha(\omega)|^{2} \)  (to be distinguished from Raman cross-section, which has an additional  \( \omega^{4} \)  frequency dependence [31, 42]), which can be directly compared with the calculated results. The calculated three-band intensity from Fig. 1 is broadened by 0.2 eV to reflect more realistic C exciton lifetimes estimated from those of free carriers in  \( MoS_{2} \)  [50]. Good agreement is achieved for the Raman intensity suppression around the A and B excitons, as clearly resolved by the red points (not missing potential resonances) and for the Raman intensity amplification near the C exciton. The two very small resonances measured at the A/B exciton energies and a scissors shift applied are discussed in the Supplemental Materials. In all prior comparisons between finite displacement BSE calculations (Placzek) and experiments known to us, satisfactory agreements were achieved for few laser frequencies [21] or for limited spectral region (e.g. the lowest excitonic peak in [19],  \( WS_{2} \)  A/B excitons in [20], and the  \( WSe_{2} \)  C exciton in [20]). Going beyond Placzek allows us to achieve agreement over the energy range of all three excitons.

![](./images/867745278705271406_3.jpg)

FIG. 3. Experimental Raman excitation profile for the out-of-plane  \( A_{1}^{\prime} \)  mode from Ref. [18] (red) and Ref. [6] (black), compared with the calculated three-band terms in Fig. 1 with broadening increased to 0.2 eV to reflect more realistic exciton lifetimes as estimated from free electron lifetimes.

This analysis has broader implications. For the band structure of a generic solid, every exciton bound state from the solution of the BSE consists of electron-hole pairs with matching group velocities, either at band extrema (zero velocity, spanning a direct gap) or along parallel bands (finite velocity, more common in indirect band gap materials). We expect band-extrema excitons in general to suppress Raman response: by construction these excitons have energies well below parallel-band excitons, giving large denominators in Eqn. 7. Even when there are multiple degenerate valleys as in the case of  \( MoS_{2} \) , the localized (in k-space) nature of band-extrema excitons allows us to approximate the electron-phonon coupling matrix elements to be constants in Eqn. 7, so (focusing on one vc pair) the sum  \( \sum_{k}\langle S^{\prime}|k\rangle\langle k|S\rangle \)  can be
 

contracted to zero due to the orthogonality of S and  \( S' \) , giving a vanishing numerator. By contrast, we expect parallel-band excitons in general to amplify Raman response: by construction, parallel pairs of conduction and valence bands span larger Brillouin zone areas (often emanating from high symmetry points, which gives them a further multiplicative degeneracy factor) and therefore allow abundant ways of assembling into excitons with similar energies bunching in a narrow energy window (as many as there are sampled k-points in the parallel-band areas). The resonant Raman intensity of silicon amplified by excitonic effects (compared with the independent quasiparticle case) in Ref. [19] is presumably attributed to this mechanism, given the abundance of parallel bands in silicon [51]. As a consequence of the general validity of the three-band dominance demonstrated here, resonant Raman measurements can directly probe how excitons undergo inter-state scattering by phonons, which affects exciton population dynamics and lifetimes [52].

The perturbation framework developed here not only allows us to go beyond the classical Placzek approximation and include excitonic effects, but also to achieve better scaling behavior: the GW-BSE routine is only performed once statically (at the slight expense of calculating electron-phonon coupling matrix elements for all Raman active modes), compared with finite differences methods where at least two GW-BSE runs are needed for each Raman active mode. This advantage can be exploited to accelerate Raman intensity calculations for low-symmetry materials such as  \( ReS_{2} \)  [53], with 18 Raman modes. For second-order Raman intensities, the computational demand for finite differences is even higher, requiring evaluating the BSE dielectric function  \( N^{2} \)  times, N being the number of Raman modes. In addition, finite-momentum phonon displacements need to be performed on supercells compatible with phonon wavevectors. Despite the computational challenge, second-order Raman intensities were successfully calculated from first-principles recently [54]. Our perturbation treatment can be naturally extended to calculate second-order Raman, where the electron-phonon coupling matrix elements would also be calculated for finite-momenta phonons, but without employing supercells thanks to density functional perturbation theory. The key challenge would be in efficiently calculating finite momentum excitons [55, 56] (exciton dispersions), which may be overcome using accurate tight-binding based models (fitted to GW band structures) [57].

This work is supported by computational time on the LSU-superMIC through the XSEDE allocation TG-DMR170050 and by the National Science Foundation Materials Innovation Platform under DMR-1539916. B.R.C. acknowledges the financial support from the Brazilian agencies CNPq and CAPES.

 \( ^{*} \)  yow5110@psu.edu
 \( ^{\dagger} \)  vhc2@psu.edu

[1] D. Y. Qiu, F. H. Da Jornada, and S. G. Louie, Phys. Rev. Lett. 111, 216805 (2013).

[2] R. Soklaski, Y. Liang, and L. Yang, Appl. Phys. Lett. 104, 193110 (2014).

[3] K. F. Mak, C. Lee, J. Hone, J. Shan, and T. F. Heinz, Phys. Rev. Lett. 105, 136805 (2010), arXiv:1004.0546.

[4] B. R. Carvalho, L. M. Malard, J. M. Alves, C. Fantini, and M. A. Pimenta, Phys. Rev. Lett. 114, 136403 (2015).

[5] B. R. Carvalho, Y. Wang, S. Mignuzzi, D. Roy, M. Terrones, C. Fantini, V. H. Crespi, L. M. Malard, and M. A. Pimenta, Nat. Commun. 8, 14670 (2017).

[6] J.-U. Lee, J. Park, Y.-W. Son, and H. Cheong, Nanoscale 7, 3229 (2015), arXiv:1501.02525.

[7] K. Golasa, M. Grzeszczyk, P. Leszczyński, C. Faugeras, A. A. L. Nicolet, A. Wysmolek, M. Potemski, and A. Babinski, Appl. Phys. Lett. 104, 092106 (2014).

[8] S. Mignuzzi, A. J. Pollard, N. Bonini, B. Brennan, I. S. Gilmore, M. A. Pimenta, D. Richards, and D. Roy, Phys. Rev. B 91, 195411 (2015).

[9] A. C. Ferrari, J. C. Meyer, V. Scardaci, C. Casiraghi, M. Lazzeri, F. Mauri, S. Piscanec, D. Jiang, K. S. Novoselov, S. Roth, and A. K. Geim, Phys. Rev. Lett. 97, 187401 (2006).

[10] P. Venezuela, M. Lazzeri, and F. Mauri, Phys. Rev. B 84, 035433 (2011).

[11] H. Zeng, J. Dai, W. Yao, D. Xiao, and X. Cui, Nat. Nanotechnol. 7, 490 (2012), arXiv:1202.1592 [cond-mat.mes-hall].

[12] K. F. Mak, K. He, J. Shan, and T. F. Heinz, Nat. Nanotechnol. 7, 494 (2012), arXiv:1205.1822.

[13] C. V. Raman and K. S. Krishnan, Nature 121, 501 (1928).

[14] S. A. Asher, M. Ludwig, and C. R. Johnson, J. Am. Chem. Soc. 108, 3186 (1986).

[15] J. A. Shelnutt, J. Chem. Phys. 72, 3948 (1980).

[16] J. B. Page, in Top. Appl. Phys., Vol. 68 (1991) pp. 17–72.

[17] R. M. Martin and L. M. Falicov, in Light Scatt. Solids I Introd. Concepts (1983) pp. 79–145.

[18] B. R. Carvalho, L. M. Malard, J. M. Alves, C. Fantini, and M. A. Pimenta, Phys. Rev. Lett. 116, 089904 (2016).

[19] Y. Gillet, M. Giantomassi, and X. Gonze, Phys. Rev. B 88, 094305 (2013), arXiv:arXiv:1309.1850v1.

[20] E. del Corro, A. Botello-Méndez, Y. Gillet, A. L. Elias, H. Terrones, S. Feng, C. Fantini, D. Rhodes, N. Pradhan, L. Balicas, X. Gonze, J.-C. Charlier, M. Terrones, and M. A. Pimenta, Nano Lett. 16, 2363 (2016).

[21] H. P. C. Miranda, S. Reichardt, G. Froehlicher, A. Molina-Sánchez, S. Berciaud, and L. Wirtz, Nano Lett. 17, 2381 (2017), arXiv:1702.05461.

[22] M. Profeta and F. Mauri, Phys. Rev. B 63, 245415 (2001).

[23] C. Rice, R. J. Young, R. Zan, U. Bangert, D. Wolverson, T. Georgiou, R. Jalil, and K. S. Novoselov, Phys. Rev. B 87, 081307 (2013).

[24] L. Liang and V. Meunier, Nanoscale 6, 5394 (2014).

[25] A. Molina-Sánchez and L. Wirtz,
 

Phys. Rev. B 84, 155413 (2011), arXiv:1109.5499.

[26] M. Lazzeri and F. Mauri, Phys. Rev. Lett. 90, 036401 (2003).

[27] L. Wirtz, M. Lazzeri, F. Mauri, and A. Rubio, Phys. Rev. B 71, 241402 (2005).

[28] M. Veithen, X. Gonze, and P. Ghosez, Phys. Rev. B 71, 125107 (2005).

[29] P. Umari, A. Pasquarello, and A. Dal Corso, Phys. Rev. B 63, 094305 (2001).

[30] S. Baroni, S. De Gironcoli, A. Dal Corso, and P. Giannozzi, Rev. Mod. Phys. 73, 515 (2001).

[31] A. Compaan and H. J. Trodahl, Phys. Rev. B 29, 793 (1984).

[32] A. A. Puretzky, L. Liang, X. Li, K. Xiao, K. Wang, M. Mahjouri-Samani, L. Basile, J. C. Idrobo, B. G. Sumpter, V. Meunier, and D. B. Geohegan, ACS Nano 9, 6333 (2015).

[33] C. Ambrosch-Draxl, H. Auer, R. Kouba, E. Y. Sherman, P. Knoll, and M. Mayer, Phys. Rev. B 65, 064501 (2002).

[34] A. C. Albrecht, J. Chem. Phys. 34, 1476 (1961).

[35] R. Bozio, A. Feis, I. Zanon, and C. Pecile, J. Chem. Phys. 91, 13 (1989).

[36] M. Walter and M. Moseler, (2018), arXiv:1806.03840.

[37] M. Cardona and G. Güntherodt, eds., Light Scattering in Solids II, Topics in Applied Physics, Vol. 50 (Springer Berlin Heidelberg, Berlin, Heidelberg, 1982).

[38] J. Kürti and H. Kuzmany, Phys. Rev. B 44, 597 (1991).

[39] S. Gupta, S. N. Shirodkar, D. Kaplan, V. Swaminathan, and B. I. Yakobson, J. Phys. Condens. Matter 30, 095501 (2018).

[40] D. A. Strubbe, Optical and transport properties of organic molecules: methods and applications, Ph.D. thesis, University of California Berkeley, USA (2012).

[41] S. Ismail-Beigi and S. G. Louie, Phys. Rev. Lett. 90, 076401 (2003).

[42] J. B. Renucci, R. N. Tyte, and M. Cardona, Phys. Rev. B 11, 3885 (1975).

[43] D. Xiao, G. B. Liu, W. Feng, X. Xu, and W. Yao, Phys. Rev. Lett. 108, 196802 (2012), arXiv:1112.3144.

[44] J. Deslippe, G. Samsonidze, D. A. Strubbe, M. Jain, M. L. Cohen, and S. G. Louie, Comput. Phys. Commun. 183, 1269 (2012), arXiv:1111.4429.

[45] M. Rohlfing and S. G. Louie, Phys. Rev. B 62, 4927 (2000).

[46] P. Giannozzi, S. Baroni, N. Bonini, M. Calandra, R. Car, C. Cavazzoni, D. Ceresoli, G. L. Chiarotti, M. Cococcioni, I. Dabo, A. D. Corso, S. Fabris, G. Fratesi, S. de Gironcoli, R. Gebauer, U. Gerstmann, C. Gougoussis, A. Kokalj, M. Lazzeri, L. Martin-Samos, N. Marzari, F. Mauri, R. Mazzarello, S. Paolini, A. Pasquarello, L. Paulatto, C. Sbraccia, S. Scandolo, G. Sclauzero, A. P. Seitsonen, A. Smogunov, P. Umari, and R. M. Wentzcovitch, J. Phys. Condens. Matter 21, 395502 (2009), arXiv:0906.2569.

[47] S. Ismail-Beigi, Phys. Rev. B 73, 233103 (2006).

[48] J. Deslippe, G. Samsonidze, M. Jain, M. L. Cohen, and S. G. Louie, Phys. Rev. B 87, 165124 (2013), arXiv:1208.0266.

[49] M. S. Hybertsen and S. G. Louie, Phys. Rev. B 34, 5390 (1986).

[50] X. Li, J. T. Mullen, Z. Jin, K. M. Borysenko, M. Buongiorno Nardelli, and K. W. Kim, Phys. Rev. B 87, 115418 (2013).

[51] J. R. Chelikowsky and M. L. Cohen, Phys. Rev. B 10, 5095 (1974).

[52] G. Antonius and S. G. Louie, (2017), arXiv:1705.04245.

[53] A. McCreary, J. R. Simpson, Y. Wang, D. Rhodes, K. Fujisawa, L. Balicas, M. Dubey, V. H. Crespi, M. Terrones, and A. R. Hight Walker, Nano Lett. 17, 5897 (2017).

[54] Y. Gillet, S. Kontur, M. Giantomassi, C. Draxl, and X. Gonze, Sci. Rep. 7, 7344 (2017).

[55] P. Cudazzo, L. Sponza, C. Giorgetti, L. Reining, F. Sottile, and M. Gatti, Phys. Rev. Lett. 116, 066803 (2016).

[56] D. Y. Qiu, T. Cao, and S. G. Louie, Phys. Rev. Lett. 115, 176801 (2015).

[57] F. Wu, F. Qu, and A. H. Macdonald, Phys. Rev. B 91, 075310 (2015), arXiv:1501.02273.
 
