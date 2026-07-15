# Squeezed Thermal Phonons Precurse Nonthermal Melting of Silicon as a Function of Fluence

Eeuwe S. Zijlstra, $^{1,2,*}$ Alan Kalitsov, $^{1,3}$ Tobias Zier, $^{1,2}$ and Martin E. Garcia $^{1,2}$

$^{1}$Theoretical Physics, University of Kassel, Heinrich-Plett-Strasse 40, 34132 Kassel, Germany
$^{2}$Center for Interdisciplinary Nanostructure Science and Technology (CINSaT), Heinrich-Plett-Strasse 40, 34132 Kassel, Germany
$^{3}$Department of Physics, University of Puerto Rico, San Juan, Puerto Rico 00931, USA

(Received 14 June 2012; revised manuscript received 18 October 2012; published 29 January 2013)

A femtosecond-laser pulse can induce ultrafast nonthermal melting of various materials along pathways that are inaccessible under thermodynamic conditions, but it is not known whether there is any structural modification at fluences just below the melting threshold. Here, we show for silicon that in this regime the room-temperature phonons become thermally squeezed, which is a process that has not been reported before in this material. We find that the origin of this effect is the sudden femtosecond-laser-induced softening of interatomic bonds, which can also be described in terms of a modification of the potential energy surface. We further find in *ab initio* molecular-dynamics simulations on laser-excited potential energy surfaces that the atoms move in the same directions during the first stages of nonthermal melting and thermal phonon squeezing. Our results demonstrate how femtosecond-laser-induced coherent fluctuations precurse complete atomic disordering as a function of fluence. The common underlying bond-softening mechanism indicates that this relation between thermal squeezing and nonthermal melting is not material specific.

DOI: 10.1103/PhysRevX.3.011005

Subject Areas: Computational Physics, Materials Science, Semiconductor Physics

## I. INTRODUCTION

The interaction of an intense femtosecond-laser pulse with a solid typically leads to a nonthermal state that usually exists for approximately 1-10 ps, where the electrons acquire a temperature of several 1000-10000 K and the atoms move on the potential energy surface created by the hot electrons [1,2]. Ultrashort laser pulses thus provide a direct means to transiently manipulate the electrons that are responsible for many material properties, including structural stability. As a result, depending on the laser fluence, the atoms may start to move along unconventional trajectories within ultrashort times. One of the possible ensuing effects is the melting of a crystal within a few hundred femtoseconds, which was discovered three decades ago and has since been observed in many semiconductors and semimetals, both experimentally [3-8] and in simulations [9]. In particular, in silicon, gallium arsenide, and indium antimonide, theoretical studies have demonstrated that nonthermal melting, i.e., melting out of thermodynamic equilibrium due to laser-induced changes in the potential energy surface, is initiated through a laser-induced lattice instability of transverse acoustic phonons at the Brillouin-zone boundary [10,11].

In this article, we direct our attention to excitations that are not sufficiently intense to melt a material and we investigate which laser-induced structural modifications can be used to predict the melting transition by looking for collective atomic motions below the melting threshold. Besides being of fundamental interest, we expect that knowledge of this process should also have implications in the field of femtosecond-laser materials processing. In previous attempts to find a precursor to ultrafast melting, it has been proposed that, for fluences below the melting threshold, the softening of coherent optical $\Gamma$-point phonons provides a relevant monitoring parameter [12]. However, their different locations in the Brillouin zone indicate that the atoms follow different pathways during ultrafast melting and $\Gamma$-point phonon softening, which are therefore not directly related. So, roughly 30 years after its discovery, it remains unclear which physical process precurses nonthermal melting.

## II. ATOMIC PATHWAYS

In order to address this open question, we have performed *ab initio* molecular-dynamics simulations of silicon, in which we explicitly take into account the hot-electron plasma created by femtosecond-laser excitation for different fluences (see the Appendix for details about the method). We study supercells containing $(n+1)\times n\times n$ conventional unit cells with $N=96,288,640$ and 1200 atoms in total. Atomic velocities and displacements are initialized so as to reproduce a Maxwell-Boltzmann distribution with a temperature of 1 mhartree (316 K). In Fig. 1(a), we show the time dependence of the root-mean-square atomic displacements from their equilibrium positions during the first 210 fs after femtosecond-laser excitation for absorbed fluences of

---
*zijlstra@uni-kassel.de*

Published by the American Physical Society under the terms of the *Creative Commons Attribution 3.0 License*. Further distribution of this work must maintain attribution to the author(s) and the published article's title, journal citation, and DOI.

---
2160-3308/13/3(1)/011005(8)
011005-1
Published by the American Physical Society

![](./images/813250579617808386_1.jpg)

FIG. 1. Atomic pathways induced by a femtosecond-laser pulse for four different fluences. (a) Averaged root-mean-square displacements from equilibrium as a function of time. The vertical linewidths are twice the standard deviations of the averages shown. The dashed line indicates the Lindemann stability limit. (b) Snapshot after 146 fs of a particular run for each excitation strength. The atomic coordinates are projected in the $z$ direction. The lines indicate $(1,-1,0)$ lattice planes.

7, 12, 17, and $22\ \text{mJ/cm}^2$, where we assume that near-ultraviolet light with a penetration depth of 10 nm heats the electrons to 40, 50, 60, and 70 mhartree, respectively. Each curve shows the average over 60 runs for a 96-atom supercell. We see that, for the two highest electronic temperatures, the atoms move away rapidly from their lattice sites without bound, which is an indication that the silicon melts (see Video 1). Noticeably, both curves already exceed the Lindemann stability limit (equaling approximately 15% of the Si-Si nearest-neighbor distance, i.e., $0.35\ \mathring{\text{A}}$) within 150 fs. In contrast, the atomic motions for the two lowest curves stay bound and we observe an oscillatory behavior that has not been noticed before in silicon: At the electronic temperature of 50 (40) mhartree, the root-mean-square atomic displacement reaches a maximum after 146 (98) fs and decreases afterwards. As we will elaborate below, this oscillatory behavior is a direct manifestation of the thermal squeezing of the classical ensemble of acoustic phonons in silicon, where the mean-square atomic displacements and momenta rotatively dip below their thermal averages in the laser-excited potential. In Fig. 1(b), snapshots after 146 fs of a particular run for each of the four selected electronic temperatures are superimposed. Strikingly, the atoms move in essentially the same directions for all electronic excitation densities, demonstrating that the same atomic pathways are followed during the first stages of nonthermal melting at high fluences and of phonon squeezing at lesser fluences.

![](./images/813250579617808386_2.jpg)

VIDEO 1. Animated version of Fig. 1. (a) Averaged root-mean-square displacements from equilibrium as a function of time. (b) Temporal evolution of the atomic coordinates from 0 to 210 fs of a particular run for each excitation strength. The atomic coordinates are projected in the $z$ direction. The lines indicate $(1,-1,0)$ lattice planes. The atoms move in the same directions during the first stages of nonthermal melting (60 and 70 mhartree) and thermal phonon squeezing (40 and 50 mhartree).

### III. MICROSCOPIC MECHANISM
A squeezed state of a classical oscillator is characterized by a variable that deviates less from its average value than at thermal equilibrium, while its conjugated variable has a larger variance. This so-called thermal squeezing has first been experimentally observed in a pumped microcanti- lever, where the cosine component of the time-averaged

shot noise could be deamplified while the sine component was simultaneously amplified [13], and has been exploited for subthermal noise measurements [14,15]. Whereas in Refs. [13–15] the squeezing of an oscillator has been achieved by means of a modulation of the macroscopic spring constant, in solids, it is possible to manipulate microscopic bonds by a femtosecond-laser pulse [16,17] that leads to squeezing [18]. The microscopic mechanism of femtosecond-laser-induced thermal squeezing is schematically illustrated in Figs. 2(a)–2(e) for an ensemble of nearly degenerate phonon modes. Before laser excitation, the thermal distribution of the atomic displacements is in equilibrium with the harmonic potential [Fig. 2(a)]. Through a femtosecond-laser pulse, the potential softens almost instantaneously, rendering the initial distribution function too narrow (squeezed) for the actual potential, so that, on average, the atoms start to move outward [Fig. 2(b)]. After a quarter of a phonon period, the distribution reaches its maximum width, which is wider than the equilibrium distribution of the laser-excited potential [Fig. 2(c)]. Thereupon, the distribution narrows again and, after half a period, when all oscillators have approximately finished a 180° phase shift, the displacements are back near their initial absolute values, albeit with opposite signs. The narrowness of the initial distribution is, however, not fully regained due to anharmonicities, phonon-phonon interactions, and a temporally diminishing constructive interference between phonon modes with different frequencies [Fig. 2(d)]. Depending on the strengths of these effects, further oscillations may be observed [Fig. 2(e)]. From the general nature of this mechanism, it follows that phonon squeezing is a common phenomenon that must emerge after intense femtosecond-laser excitation below the melting fluence in materials that exhibit laser-induced bond softening, which is a prerequisite for nonthermal melting. In agreement with our theory, we note that thermal phonon squeezing in bismuth [18] has been observed in the same general direction, where at higher fluences a lattice instability induces nonthermal melting [8].

![](./images/813250579617808386_3.jpg)

FIG. 2. Time-dependent variance of the atomic displacements at the electronic temperature of 50 mhartree. (a)–(e) Schematic illustration of thermal phonon squeezing. The black curves represent laser-induced changes in the potential. The blue curves represent the distribution of atomic displacements. (f) Ab initio results in the harmonic approximation. The blue curve is for $N = 640$. The red curves are for $N = 1200$. The solid curves represent classical results. The dashed curve represents the quantum-mechanical result. The hatched region represents the zero-point motion in the laser-excited state. (g) Ab initio molecular-dynamics results: total and spectrally decomposed variances averaged over nine runs ($N = 640$). The light shaded areas represent standard deviations of the averages. (h) Phonon density of states before (purple curve) and after (black curve and shaded areas) femtosecond-laser excitation in the range from 0 to 17.5 THz.

### IV. THERMAL SQUEEZING IN REAL SPACE

Further insight into the nature of the atomic motions can be obtained from the time-dependent variance $\langle \mathbf{u}^2 \rangle - \langle \mathbf{u} \rangle^2$ of the atomic displacements $\mathbf{u}$ in the harmonic approximation (see the Appendix), from which we notice that $N = 640$ already gives a sufficient sampling of all phonon modes in the first Brillouin zone [Fig. 2(f)]. By comparing the classical and quantum-mechanical time-resolved variances [Fig. 2(f)], we conclude that, even though the mean-square atomic displacements vary between only 1.5 and 4.4 times the zero-point variance, quantum effects are not important for thermal phonon squeezing in silicon.

Figure 2(g) shows the results of our molecular-dynamics simulation with 640 atoms per supercell. Comparison with Fig. 2(f) demonstrates that anharmonicities and phonon-phonon interactions, which are fully included in the molecular-dynamics simulations and totally absent in the harmonic approximation, lead to an approximately $30\%$ lengthening of the oscillation period and an equally large relative increase of the height of the first variance maximum. In Fig. 2(h), we draw phonon densities of states before and after laser excitation (see the Appendix). Three peaks, $\nu_1 = 2.3$, $\nu_2 = 7.9$, and $\nu_3 = 12.6$ THz, are discernible. Using the orthonormal eigenvectors $\{e_i\}$ of the $3N \times 3N$ dynamical matrix, we define the projection operators as

$$
P_1 = \sum_{i, \nu_i \le 4.8\ \text{THz}} e_i \otimes e_i^T \quad \text{and} \quad P_{2,3} = 1 - P_1. \tag{1}
$$

The sum runs over all eigenpairs up to the first minimum in the phonon density of states, so that $\langle (P_1 \mathbf{u})^2 \rangle$ gives the


![](./images/813250579617808386_4.jpg)

FIG. 3. Total and spectrally projected instantaneous atomic temperatures as a function of time after femtosecond-laser excitation. The data used and the decomposition are the same as in Fig. 2(g).

mean-square atomic displacements projected onto the directions of the phonon modes with frequencies that approximately equal $\nu_1$ and so that $\langle (P_{2,3}{\bf u})^2 \rangle$ gives the contributions from all other lattice vibrations. In Fig. 2(g), we plot these spectrally projected variances along with the total $\langle {\bf u}^2 \rangle$, showing that acoustic phonon modes, which already swing with the largest amplitudes before laser excitation, dominate squeezing in real space.

## V. THERMAL SQUEEZING IN MOMENTUM SPACE

A more even spectral weighting is obtained by consid- ering the conjugated variables, i.e., the atomic momenta, whose distribution has a variance proportional to the in- stantaneous atomic temperature $k_B T_{\rm atomic} = m\langle {\bf v}^2 \rangle/3$ that we plot together with properly normalized spectral projec- tions in Fig. 3. Although initially the phonons share a common temperature, the laser excitation is seen to lead to an average cooling of the atoms that is most pronounced for the phonon modes with frequencies around $\nu_1$. We further note that acoustic and optical phonons have not reached a common temperature after 600 fs, which is a new finding that suggests a line along which semiempirical theories, like the two-temperature model, can be extended. On top of these time-averaged effects, we notice at least two oscillations with periods that approximately equal $1/2\nu_1$ and $1/2\nu_3$, demonstrating that phonon squeezing is not limited to the acoustic lattice vibrations that are responsible for nonthermal melting but that it also occurs in the optical part of the spectrum. In analogy, we infer that thermal squeezing is likely to occur in almost any material after femtosecond-laser excitation, as long as there is some modification of the interatomic force constants.

## VI. FURTHER CONSIDERATIONS

In addition to the atomic forces that arise from laser- excited potential energy surfaces, which are fully incor- porated into the present simulations, incoherent electron- phonon interactions will eventually lead to a thermaliza- tion of the electrons and the atoms. The essential step in this equilibration process is the emission of high-frequency phonons when hot carriers, i.e., electrons and holes, cool down [19]. At very low excitation densities, emission of phonons happens on a time scale of $\tau_0 = 200$–260 fs (see [20]), but due to screening by the hot carriers this process has theoretically been predicted to slow down quadrati- cally with the excitation density according to $\tau = \tau_0(1 + \rho^2/\rho_c^2)$, where $\rho$ is the excitation density, i.e., the number of electron-hole pairs per unit volume, and $\rho_c$ is the so-called critical density [21]. A recent experiment on silicon performed at $\rho = 2.2 \times 10^{-21}$ cm$^{-3}$ has shown exponential atomic heating with a time constant $\tau = 2$ ps and has been explained by the above theory using $\tau_0 =$ 230 fs and $\rho_c = 8 \times 10^{20}$ cm$^{-3}$ [20]. In our simulations performed at the electronic temperature of 50 mhartree, $\rho = 1.5 \times 10^{22}$ cm$^{-3}$, so that we can expect the screening to become considerably more effective, but the estimate of 81 ps from the above theory is probably too large. A second interaction that is important for the electron-atom thermal- ization process is Auger recombination, where an electron- hole pair recombines, transferring its energy to a third carrier and thereby keeping the electrons and holes hot [21]. Competing with the above heat-exchange processes is the diffusion of hot carriers away from the excited surface region. In a thin-film geometry, where diffusion into the bulk is irrelevant, a complete thermalization of the excited carriers initially at 50 mhartree with the lattice initially at 316 K would lead to a phonon temperature that equals approximately 5700 K, assuming the high-temperature heat capacity of the lattice, which is well above the melting point of 1687 K. The estimated increase of the atomic temperature during the first 600 fs after the laser pulse depends on the exponential time constant $\tau$, which is currently unknown for our excitation density but should, according to [20,21], lie between 40 K ($\tau = 81$ ps) and 1408 K ($\tau = 2$ ps). As mentioned above, in a bulk geome- try, these values can be considerably lower due to carrier diffusion, which is an important process because of the very short penetration depth of near-ultraviolet light that equals approximately 10 nm. Additionally, by tuning the laser wavelength, it might be possible to excite electrons just above the band gap, likewise reducing the energy transfer from electrons to atoms. In any case, a rapid loss of coherence in the electronic subsystem in Si causes the electron-phonon thermalization to occur through incoher- ent scattering events. In bismuth, this has been shown to lead to a roughly linear increase of the variance of the atomic displacements with time, which is superimposed on the phonon-squeezing effect [18]. In silicon, we expect a similar additional linear increase of the variance in Fig. 2(g) and of the ionic temperature in Fig. 3. However, in view of the above discussion, the slopes are hard to

determine and will definitely depend on experimental parameters, such as the sample thickness and the wavelength of the ultrashort laser pulse.

## VII. RELATION TO EXPERIMENTS
To complete our story, we now briefly discuss previous occurrences of phonon squeezing in crystals in the literature in the context of our new findings. First, quantum or vacuum squeezing has been induced by Garrett and co-workers in a transparent medium, $KTaO_3$, using second-order Raman scattering, which does not induce bond softening [22]. The goal of this study is to squeeze the phonon wave packet below its zero-point width, which requires very low temperatures. Thermal squeezing of phonons, i.e., squeezing at elevated temperatures, has been observed in an opaque material, namely, bismuth [18]. This study [18] has been limited to the low-fluence regime, well below the threshold for nonthermal melting, but in Sec. III we have linked thermal squeezing in Bi at low fluences and the direction in which it has been observed to nonthermal melting at higher fluences, in agreement with our theory. It is, however, important to point out that the precise role of the atomic displacements perpendicular to the eigenvector of the coherently excited $A_{1g}$ mode during nonthermal melting has not yet been confirmed. In another study that is worth mentioning, harmonic models that are used to compare with experimental data for InSb that is excited at fluences both above and just below the melting threshold show oscillations of the root-mean-square atomic displacements [Eq. (2) and Fig. 2 in Ref. [23] and Eq. (5) and Fig. 7 in Ref. [24] ], which are a direct manifestation of phonon squeezing comparable to our results in Fig. 2(g). Unfortunately, this effect could not be observed experimentally in the time-dependent Debye-Waller factors [23,24]. This discrepancy between harmonic theory and experiment has been attributed to the models, in particular, to the absence of anharmonicities therein [23,24], which are indeed far from negligible, as can, for example, be seen either by comparing Figs. 2(f) and 2(g) or from Refs. [10,11]. It is, however, important to note that harmonic models cannot describe melting. Only a computation of the full pathways, such as the one performed here, can establish a connection between complex confined and unbound atomic motions. We therefore believe that the absence of squeezing in the experimental study of InSb [23,24] should not be explained as an artifact of the models but that it is probably due to other, experimental reasons, such as insufficient time resolution or large statistical errors.

## VIII. PRECURSOR TO NONTHERMAL MELTING
In summary, we have found that phonons in silicon become thermally squeezed after relatively low-fluence femtosecond-laser excitation and we have shown that the atoms follow the same pathways in this process and during the first stages of nonthermal melting at higher fluences, demonstrating a close relationship at the microscopic level between these two seemingly independent phenomena. We have attributed these two processes to a common origin, namely, the laser-induced softening of the interatomic force constants, where, however, anharmonicities and phonon-phonon interactions enhance the squeezing effect by 30%. Based on a comparison of the atomic pathways, we have established that phonon squeezing is *the* precursor to nonthermal melting as a function of fluence. In this capacity, it has some predictive powers. First, if we expect no squeezing after femtosecond-laser excitation because the phonons neither soften nor harden considerably, laser-induced melting is a thermal process. This is, for example, the case in aluminum [16]. The time scale of thermal melting is governed by incoherent electron-lattice equilibration, which lies typically in the range of picoseconds [25,26] but might also be faster, leading possibly to ultrafast thermal melting. Second, systems exhibiting nonthermal melting will definitively show thermal phonon squeezing at fluences below the melting threshold. Thermal squeezing may thus be used to experimentally obtain information about the nonthermal or thermal microscopic nature of ultrafast melting. It is also interesting to point out that, if there is laser-induced bond hardening, e.g., in gold [16], from our physical picture [Figs. 2(a)–2(e)] we expect the squeezing oscillations to have the opposite sign compared to silicon, meaning that the distribution of displacements initially becomes narrower. For gold, delayed thermal melting has been reported [27]. In the case of laser-induced bond softening, the squeezing is in the reported direction [cf. Figs. 2(b) and 2(c)] and its amplitude increases with fluence up to the melting fluence. Thermal phonon squeezing can thus be used to follow and characterize the nature of ultrafast melting up to the melting transition as a function of fluence and could also provide a control parameter for femtosecond-laser-induced materials processing, which can relatively easily be measured as oscillations in the Bragg intensities.

## ACKNOWLEDGMENTS
We thank BMBF (Project No. 05K10SJA) and DFG (Project No. GA 465/15-1) for funding. Computations were performed at the ITS, University of Kassel.

## APPENDIX: METHODS
### 1. *Ab initio* molecular-dynamics simulations after femtosecond-laser excitation
To describe the effect of a hot-electron plasma, we used electronic-temperature-dependent density-functional theory [28], where the occupancies of the Kohn-Sham orbitals [29] are described by a Fermi function. This model, which is usually used to describe silicon after intense
011005-5

femtosecond-laser excitation, implicitly assumes very fast electron-hole equilibration. An interesting alternative model completely neglects electron-hole recombination [30]. However, in the current work, we have restricted ourselves to the first more usual model. In order to be able to treat sufficiently large supercells, we have devel- oped our own code for highly excited valence electron systems (CHIVES) [31], which uses norm-conserving pseu- dopotentials [32]; a primitive Gaussian basis set with exponents $a_{1}=1.17769 a_{0}^{-2}$ ( $s$ and $p$ orbitals), $a_{2}=$  $0.40348 a_{0}^{-2}$ ( $s, p$ , and $d$ orbitals), and $a_{3}=0.12989 a_{0}^{-2}$ ( $s$ and $p$ orbitals); and a regular three-dimensional grid with a cutoff energy of 1330 eV to describe the Hartree and the exchange and correlation potentials in the local density approximation [33]. For our 96-atom supercell, we use a $1 \times 2 \times 2 k$ grid. All other cells are treated without no ticeable loss of accuracy in the $\Gamma$ -point approximation. With these choices, we reproduce the laser-induced soft- ening of the Brillouin-zone-boundary phonons responsible for nonthermal melting [10]. In particular, for the trans- verse acoustic phonons at the $X$ point, we find a ground state frequency of 4.30 THz that decreases to 0 THz at an electronic temperature that equals approximately65 mhartree, in excellent agreement with previous density-functional-theory calculations [34]. Using the computed forces and the velocity Verlet scheme, we per- form molecular-dynamics simulations with a time step of2 fs, which is approximately $1 / 40 \nu_{3}$ [Fig. 2(h)]. We initi alize the atomic velocities and displacements before laser excitation using inverse transform sampling and 6N true random numbers [35] $r_{i}$ lying uniformly on [0,1] as

$$
v_{i}^{(i)}=\sqrt{\frac{2 k_{B} T_{\text {atomic }}^{(i)}}{m}} \mathcal{F}\left(2 r_{i}-1\right), \quad i=1, \ldots, 3 N \quad \text { (A1) }
$$

and

$$
u_{i}^{(i)}=\sqrt{\frac{2 k_{B} T_{\text {atomic }}^{(i)}}{m \omega_{i}^{(i) 2}}} \mathcal{F}\left(2 r_{i+3 N}-1\right), \quad i=1, \ldots, 3 N, \quad \text { (A2) }
$$

where $F$ is the inverse error function, reproducing the Maxwell-Boltzmann velocity distribution [Eq. (A5)] and the distribution of Eq. (A6). The quantities appearing in these equations are defined below. It is worth noting that we fully take into account all laser-induced changes in the potential energy surface but neglect the energy transfer from the electrons to the atoms due to incoherent electron-phonon scattering that is expected to occur on a time scale of 2-81 ps (Sec. VI), which is much longer than the approximately 150 fs needed to reach the maximum squeezing effect in our simulations [Fig. 2(g)].

## 2. Phonons
We calculate all phonon modes that are compatible with a supercell by displacing an arbitrary atom from its equi- librium position by $0.001 a_{0}$ , first in the $x$ direction and then in the $y$ direction. Using the computed forces on all the atoms and the symmetry of the lattice, we construct the3N x 3N dynamical matrix, whose orthonormal eigenvec- tors $e_{i}$ are phonon directions that are related to the usual phonon vectors by $\varepsilon_{i}=e_{i} / \sqrt{m}$ , where $m$ is the atomic mass of silicon. We obtain phonon frequencies $\nu_{i}$ from the eigenvalues $\lambda_{i}=m \omega_{i}^{2}$ with $\omega_{i}=2 \pi \nu_{i}$ . For the initial eigenvectors and eigenfrequencies at low electronic tem- perature before laser excitation, we use the notation $e_{i}^{(i)}$ and v. We denote the phonon directions and frequencies after laser excitation (electronic temperature of 50 mhartree) by $e_{i}$ and $\nu_{i}$ . We compute phonon densities of states before and after laser excitation by, respectively, convolving the frequencies $\nu_{i}^{(i)}$ and $\nu_{i}$ , obtained for the $N=1200$ super cell, with Gaussians with full widths at half maximum of1 THz [Fig. 2(h)].

## 3. Harmonic theory of thermal phonon squeezing
In order to derive an expression for the time-dependent variance of the atomic displacements after laser excitation[Fig. 2(f)], we first consider the stationary distributions of the atomic velocities and displacements in thermodynamic equilibrium at a temperature $k_{B} T_{atomic }^{(i)}=1$ mhartree, where $k_{B}$ is the Boltzmann constant, which applies to the situation before laser excitation. We call the vectors of length 3N with the velocities and displacements of all atoms $v$ and $u$ , respectively, and define the displacements and velocities in the phonon directions before laser excitation as

$$
u_{i}^{(i)}=\boldsymbol{e}_{i}^{(i)^{T}} \cdot \mathbf{u} \quad \text { (A3) }
$$

and

$$
v_{i}^{(i)}=\boldsymbol{e}_{i}^{(i)^{T}} \cdot \mathbf{v}, \quad \text { (A4) }
$$

where $T$ stands for transpose. The probability for $v_{i}^{(i)}$ to be between $v_{i}^{(i)}$ and $v_{i}^{(i)}+d v_{i}^{(i)}$ is given by the Maxwell Boltzmann velocity distribution

$$
P_{v_{i}^{(i)}} d v_{i}^{(i)}=\sqrt{\frac{m}{2 \pi k_{B} T_{\text {atomic }}^{(i)}}} \exp \left(-m v_{i}^{(i)^{2}} / 2 k_{B} T_{\text {atomic }}^{(i)}\right) d v_{i}^{(i)}.
$$

In the harmonic approximation, the probability for $u_{i}^{(i)}$ to be between $u_{i}^{(i)}$ and $u_{i}^{(i)}+d u_{i}^{(i)}$ equals

$$
P_{u_{i}^{(i)}} d u_{i}^{(i)}=\sqrt{\frac{m \omega_{i}^{(i)^{2}}}{2 \pi k_{B} T_{\text {atomic }}^{(i)}}} \exp \left(-m \omega_{i}^{(i)^{2}} u_{i}^{(i)^{2}} / 2 k_{B} T_{\text {atomic }}^{(i)}\right) d u_{i}^{(i)}.
$$

After the laser excitation, we obtain new phonon directions e, that are related to the initial directions by

$$
\boldsymbol{e}_{i}^{T}=\sum_{j} C_{i j} \boldsymbol{e}_{j}^{(i)^{T}}, \quad \text { (A7) }
$$

with coefficients $C_{ij} = \boldsymbol{e}_i^T \cdot \boldsymbol{e}_j^{(i)}$ that follow immediately from our computed phonon directions. The atomic displacement in the direction $e_i$ at time $t=0$ after laser excitation is given by
$$
\begin{aligned}
u_{i}(t=0) \equiv \boldsymbol{e}_{i}^{T} \cdot \mathbf{u} &=\sum_{j} C_{i j} \boldsymbol{e}_{j}^{(i) T} \cdot \mathbf{u}=\sum_{j} C_{i j} u_{j}^{(i)}(t=0) \\
&(\mathrm{A} 8)
\end{aligned}
$$
and analogously
$$
v_{i}(t=0)=\sum_{j} C_{i j} v_{j}^{(i)}(t=0). \tag{A9}
$$

Using these initial conditions, in the harmonic approximation,
$$
\begin{aligned}
u_{i}(t)=& \sum_{j} C_{i j} u_{j}^{(i)}(t=0) \cos \left(\omega_{i} t\right) \\
&+\frac{1}{\omega_{i}} \sum_{j} C_{i j} v_{j}^{(i)}(t=0) \sin \left(\omega_{i} t\right). \quad \text { (A10) }
\end{aligned}
$$

Integrating over all possible initial displacements and velocities, we get
$$
\begin{aligned}
\left\langle u_{i}^{2}(t)\right\rangle= & \int d u_{1}^{(i)} \cdots \int d u_{3 N}^{(i)} \int d v_{1}^{(i)} \cdots \\
& \times \int d v_{3 N}^{(i)} P_{u_{1}^{(i)}} \cdots P_{u_{3 N}^{(i)}} P_{v_{1}^{(i)}} \cdots P_{v_{3 N}^{(i)}}\left[u_{i}(t)\right]^{2} \\
= & \cos ^{2}\left(\omega_{i} t\right) \sum_{j} C_{i j}^{2} \frac{k_{B} T_{\text {atomic }}^{(i)}}{m \omega_{j}^{(i)^{2}}} \\
&+\frac{\sin ^{2}\left(\omega_{i} t\right)}{\omega_{i}^{2}} \sum_{j} C_{i j}^{2} \frac{k_{B} T_{\text {atomic }}^{(i)}}{m}. \quad \text { (A11) }
\end{aligned}
$$

Averaging over all phonon modes gives
$$
\begin{aligned}
\left\langle\mathbf{u}^{2}\right\rangle= & \frac{1}{N m} \sum_{i=1}^{3 N}\left[\cos ^{2}\left(\omega_{i} t\right) \sum_{j} C_{i j}^{2} \frac{k_{B} T_{\text {atomic }}^{(i)}}{\omega_{j}^{(i)^{2}}}\right. \\
& \left.+\sin ^{2}\left(\omega_{i} t\right) \sum_{j} C_{i j}^{2} \frac{k_{B} T_{\text {atomic }}^{(i)}}{\omega_{i}^{2}}\right], \quad \text { (A12) }
\end{aligned}
$$
which is our final result per atom for the classical time-dependent variance of the atomic displacements in the harmonic approximation. A comparison with quantum-mechanical theory [18] shows that quantum effects modify the above equation by the substitution
$$
k_{B} T_{\text {atomic }}^{(i)} \rightarrow \frac{\hbar \omega_{j}^{(i)}}{2} \operatorname{coth}\left(\frac{\hbar \omega_{j}^{(i)}}{2 k_{B} T_{\text {atomic }}^{(i)}}\right). \tag{A13}
$$

The quantum-mechanical zero-point variance in the laser-excited potential equals
$$
\left\langle\mathbf{u}^{2}\right\rangle_{0 \mathrm{~K}}=\frac{1}{N m} \sum_{i} \frac{\hbar}{2 \omega_{i}}. \tag{A14}
$$

[1] K. H. Bennemann, Photoinduced Phase Transitions, J. Phys. Condens. Matter 23, 073202 (2011).

[2] E. S. Zijlstra and M. E. Garcia, in Dynamics at Solid State Surfaces and Interfaces. Volume 1: Current Developments, edited by U. Bovensiepen, H. Petek, and M. Wolf (Wiley, Weinheim, 2010), p. 447-474.

[3] C. V. Shank, R. Yen, and C. Hirlimann, Time-Resolved Reflectivity Measurements of Femtosecond-Optical-Pulse- Induced Phase Transitions in Silicon, Phys. Rev. Lett. 50,454 (1983).

[4] M. Harb, R. Ernstorfer, C. T. Hebeisen, G. Sciaini, W. Peng, T. Dartigalongue, M. A. Eriksson, M. G. Lagally, S. G. Kruglik, and R. J. D. Miller, Electronically Driven Structure Changes of Si Captured by Femtosecond Electron Diffraction, Phys. Rev. Lett. 100, 155504 (2008).

[5] K. Sokolowski-Tinten, C. Blome, C. Dietrich, A. Tarasevitch, M. Horn von Hoegen, D. von der Linde, A. Cavalleri, J. Squier, and M. Kammler, Femtosecond X-Ray Measurement of Ultrafast Melting and Large Acoustic Transients, Phys. Rev. Lett. 87, 225701 (2001).

[6] P. Saeta, J.-K. Wang, Y. Siegal, N. Bloembergen, and E. Mazur, Ultrafast Electronic Disordering During Femtosecond Laser Melting of GaAs, Phys. Rev. Lett.67, 1023 (1991).

[7] A. M. Lindenberg et al., Atomic-Scale Visualization of Inertial Dynamics, Science 308, 392 (2005).

[8] G. Sciaini, M. Harb, S.G. Kruglik, T. Payer, C.T. Hebeisen, F.-J. Meyer zu Heringdorf, M. Yamaguchi, M. Horn-von Hoegen, R. Ernstorfer, and R.J.D. Miller, Electronic Acceleration of Atomic Motions and Disordering in Bismuth, Nature (London) 458, 56 (2009).

[9] P. L. Silvestrelli, A. Alavi, M. Parrinello, and D. Frenkel, Ab Initio Molecular Dynamics Simulation of Laser Melting of Silicon, Phys. Rev. Lett. 77, 3149 (1996).

[10] P. Stampfli and K. H. Bennemann, Time Dependence of the Laser-Induced Femtosecond Lattice Instability of Si and GaAs: Role of Longitudinal Optical Distortions, Phys. Rev. B 49, 7299 (1994).

[11] E.S. Zijlstra, J. Walkenhorst, and M.E. Garcia, Anharmonic Noninertial Lattice Dynamics During Ultrafast Nonthermal Melting of InSb, Phys. Rev. Lett.101, 135701 (2008).

[12] S. Hunsche, K. Wienecke, T. Dekorsy, and H. Kurz, Impulsive Softening of Coherent Phonons in Tellurium, Phys. Rev. Lett. 75, 1815 (1995).

[13] D. Rugar and P. Grütter, Mechanical Parametric Amplification and Thermomechanical Noise Squeezing, Phys. Rev. Lett. 67, 699 (1991).

[14] V. Natarajan, F. DiFilippo, and D. E. Pritchard, Classical Squeezing of an Oscillator for Subthermal Noise Operation, Phys. Rev. Lett. 74, 2855 (1995).

[15] I. Mahboob, E. Flurin, K. Nishiguchi, A. Fujiwara, and H. Yamaguchi, Enhanced Force Sensitivity and Noise Squeezing in an Electromechanical Resonator Coupled to a Nanotransistor, Appl. Phys. Lett. 97, 253105 (2010).

[16] V. Recoules, J. Clérouin, G. Zérah, P. M. Anglade, and S. Mazevet, Effect of Intense Laser Irradiation on the Lattice Stability of Semiconductors and Metals, Phys. Rev. Lett.96, 055503 (2006).

[17] D.M. Fritz *et al.*, *Ultrafast Bond Softening in Bismuth: Mapping a Solid's Interatomic Potential with X-Rays*, Science **315**, 633 (2007).

[18] S.L. Johnson, P. Beaud, E. Vorobeva, C.J. Milne, É.D. Murray, S. Fahy, and G. Ingold, *Directly Observing Squeezed Phonon States with Femtosecond X-Ray Diffraction*, Phys. Rev. Lett. **102**, 175503 (2009).

[19] A.J. Nozik, *Spectroscopy and Hot Electron Relaxation Dynamics in Semiconductor Quantum Wells and Quantum Dots*, Annu. Rev. Phys. Chem. **52**, 193 (2001).

[20] M. Harb, R. Ernstorfer, T. Dartigalongue, C.T. Hebeisen, R.E. Jordan, and R.J.D. Miller, *Carrier Relaxation and Lattice Heating Dynamics in Silicon Revealed by Femtosecond Electron Diffraction*, J. Phys. Chem. B **110**, 25308 (2006).

[21] E.J. Yoffa, *Screening of Hot-Carrier Relaxation in Highly Photoexcited Semiconductors*, Phys. Rev. B **23**, 1909 (1981).

[22] G.A. Garrett, A.G. Rojo, A.K. Sood, J.F. Whitaker, and R. Merlin, *Vacuum Squeezing of Solids: Macroscopic Quantum States Driven by Light Pulses*, Science **275**, 1638 (1997).

[23] P.B. Hillyard *et al.*, *Carrier-Density-Dependent Lattice Stability in InSb*, Phys. Rev. Lett. **98**, 125501 (2007).

[24] P.B. Hillyard, D.A. Reis, and K.J. Gaffney, *Carrier-Induced Disordering Dynamics in InSb Studied with Density Functional Perturbation Theory*, Phys. Rev. B **77**, 195213 (2008).

[25] B.J. Siwick, J.R. Dwyer, R.E. Jordan, and R.J.D. Miller, *An Atomic-Level View of Melting Using Femtosecond Electron Diffraction*, Science **302**, 1382 (2003).

[26] B. Rethfeld, K. Sokolowski-Tinten, D. von der Linde, and S.I. Anisimov, *Ultrafast Thermal Melting of Laser-Excited Solids by Homogeneous Nucleation*, Phys. Rev. B **65**, 092103 (2002).

[27] R. Ernstorfer, M. Harb, C.T. Hebeisen, G. Sciaini, T. Dartigalongue, and R.J.D. Miller, *The Formation of Warm Dense Matter: Experimental Evidence for Electronic Bond Hardening in Gold*, Science **323**, 1033 (2009).

[28] N.D. Mermin, *Thermal Properties of the Inhomogeneous Electron Gas*, Phys. Rev. **137**, A1441 (1965).

[29] W. Kohn and L.J. Sham, *Self-Consistent Equations Including Exchange and Correlation Effects*, Phys. Rev. **140**, A1133 (1965).

[30] P. Tangney and S. Fahy, *Calculations of the $A_1$ Phonon Frequency in Photoexcited Tellurium*, Phys. Rev. Lett. **82**, 4340 (1999).

[31] E.S. Zijlstra, N. Huntemann, A. Kalitsov, M.E. Garcia, and U. von Barth, *Optimized Gaussian Basis Sets for Goedecker-Teter-Hutter Pseudopotentials*, Model. Simul. Mater. Sci. Eng. **17**, 015009 (2009).

[32] S. Goedecker, M. Teter, and J. Hutter, *Separable Dual-Space Gaussian Pseudopotentials*, Phys. Rev. B **54**, 1703 (1996).

[33] J.P. Perdew and Y. Wang, *Accurate and Simple Analytic Representation of the Electron-Gas Correlation Energy*, Phys. Rev. B **45**, 13244 (1992).

[34] L. Shokeen and P.K. Schelling, *Thermodynamics and Kinetics of Silicon under Conditions of Strong Electronic Excitation*, J. Appl. Phys. **109**, 073503 (2011).

[35] M. Haahr, *True Random Number Service*, http://www .random.org.