
# Strain-Induced Activation of Symmetry-Forbidden Exciton-Phonon Couplings for Enhanced Phonon-Assisted Photoluminescence in MoS₂ Monolayers

Rishabh Saraswat, \( ^{1} \)  Rekha Verma, \( ^{1} \text{ and Sitangshu Bhattacharya}^{2} \) 

 \( ^{1} \) Department of Electronics and Communication Engineering,

Indian Institute of Information Technology-Allahabad, Uttar Pradesh 211015, India

 \( ^{2} \) Electronic Structure Theory Group, Department of Electronics and Communication Engineering, Indian Institute of Information Technology-Allahabad, Uttar Pradesh 211015, India

Phonon-assisted photoluminescence (PL) in molybdenum-based two-dimensional dichalcogenides is typically weak due to the dormant phonon coupling with optically inactive momentum-dark (intervalley) excitons, unlike in tungsten-based dichalcogenides where such processes are more prominent. Despite this inefficiency, we revisit excitons in  \( MoS_{2} \)  using rigorous finite-momentum Bethe-Salpeter equation calculations to identify ways to enhance phonon-assisted recombination channels. Our ab-initio results, complemented by group-theoretic analyses, reveal that while unstrained  \( MoS_{2} \)  exhibits no phonon-assisted PL emissions at cryogenic temperatures due to forbidden  \( A^{\prime\prime} \)  phonon modes, biaxial strain opens a pathway to significantly intensify this emission by activating hole-phonon  \( A^{\prime} \) -mediated scattering channels. By calculating allowed exciton-phonon matrix elements and scattering rates, we demonstrate how strain redistributes oscillator strengths toward radiative recombination. These findings provide a promising route to improving PL emission efficiency in various metal dichalcogenide monolayers through strain engineering and offer valuable insights for further exploration of exciton-phonon dynamics, including time-resolved spectroscopic studies.

Light emission in pristine semiconductors arises from the radiative recombination of bound electron-hole pairs, or excitons. The nature of this emission, whether direct or indirect, depends on the relative positions of the energy valleys in the exciton dispersion [1], similar to electronic band dispersion, especially with respect to the valley center,  \( \Gamma \) , in the excitonic transferred Brillouin zone (BZ). At  \( \Gamma \) , the excitonic center-of-mass momentum is zero (Q = 0, is the optical dipole limit condition) and therefore represent intravalley excitons. A direct optical gap arises when the lowest energy valley is at  \( \Gamma \) , allowing efficient radiative recombination without additional momentum transfer, resulting in intense direct photoluminescence (PL) emission [2]. Conversely, an indirect optical gap occurs when the lowest exciton energy lies at a finite momentum state ( \( Q \neq 0 \) ), producing intervalley excitons, where recombination requires additional momentum from phonons. This indirect process is less efficient due to multiparticle interactions and selection rules [3], leading to weaker PL emission, such as in bulk honeycomb (h)-boron nitride (BN) [4].

Intrinsic high-quality two-dimensional (2D) molybdenum (Mo) and tungsten (W)-based h-transition metal dichalcogenide (TMD) samples are ideal for studying intense ground-state exciton-light interactions. These noncentrosymmetric crystals with time-reversal symmetry can enable spin-momentum coupling between band-edge electron and hole states across two distinct time-reversed valleys K and  \( K' \)  in the electronic BZ [5, 6] (see Fig. 1(a)). Circularly polarized light with left or right handedness can selectively excite excitons in these valleys, leading to valley polarization [7–16]. The parallel (antiparallel) alignment of these electron and hole spins at K or  \( K' \)  further imposes the selection criterion on exciton formation, resulting in spin-allowed optically active (spin-forbidden inactive) intravalley excitons. Only these active or “bright” excitons undergo strong radiative recombination [15, 17–21] and therefore emit intense direct PL. In case of intervalley excitons (see Fig. 1(b)), momentum conservation requires a zero dipole oscillator strength, rendering them optically inactive or “dark” across the excitonic BZ.

Excitons those are dark, whether they are intra- or intervalley, do not contribute to the PL directly, unless they are activated intentionally. This has been shown for the energetically lowest lying dark intravalley spin-forbidden excitons. These excitons were observed to undergo dark to bright transition in  \( MoS_{2} \)  and  \( MoSe_{2} \)  [22, 23] by spin-flipping process in an external in-plane magnetic field, or due to exchange interaction [24], or by phonon assistance such as in  \( WS_{2} \)  [25], leading to valley depolarization. The recombination of intervalley dark excitons at cryogenic temperatures in  \( MoSe_{2} \)  has been observed with varied outcomes. In one instance, no phonon-assisted PL is reported, though there is an asymmetry in the brightest direct PL signal toward higher energies [26]. In other observations, strong exciton-phonon (exc-ph) coupling appears, assisted by longitudinal acoustic (LA) phonons at the M point (in the phonon BZ) [27] and  \( A' \)  optical phonons at room temperature [28]. In contrast,  \( WSe_{2} \)  consistently shows valley depolarization effects due to intense exc-ph scattering [26, 29–34].

Although phonon-assisted PL emission has garnered significant attention in 2D h-MoSe \( _{2} \) , WS \( _{2} \)  and WSe \( _{2} \) , however, such a detailed mechanism in 2D h-MoS \( _{2} \)  remains largely unexplored. Therefore in this work, we revisit 2D h-MoS \( _{2} \)  for a comprehensive understanding of phonon-assisted indirect excitonic recombination. While MoS \( _{2} \)  direct emission about room temperatures dominates at  \( \Gamma \)  in the excitonic BZ due to thermalization, we rather show using group-theoretic analyses that the cryogenic PL emission due to the low-energy dark excitons are forbidden by symmetry conditions. However, by harnessing strain engineering, these dark excitons can be activated to couple with intervalley phonon mode (A') within the M-K BZ route, unlocking a pathway to enhanced indirect PL emission. We demonstrate these emissions using biaxial strain in the range of -0.5% to +3%, achievable under laboratory conditions [35]. We illustrate that indirect PL emission at higher tensile strains in 2D MoS \( _{2} \)  is dominated by hole-
 
![](./images/1083017860978049077_1.jpg)

![](./images/1083017860978049077_2.jpg)

![](./images/1083017860978049077_3.jpg)

![](./images/1083017860978049077_4.jpg)

![](./images/1083017860978049077_5.jpg)

![](./images/1083017860978049077_6.jpg)

![](./images/1083017860978049077_7.jpg)

FIG. 1. Top panel: (a) Spin-resolved  \( G_{0}W_{0} \)  corrected electron energy dispersion in 1% biaxially tensile strained 2D h- \( MoS_{2} \) . The intravalley excitons (labeled as  \( e_{1} \) ) are at K and  \( K' \) . The intervalley excitons ( \( e_{2} \) ,  \( e_{3} \)  and  \( e_{4} \) ) are however momentum-forbidden. Only the top valence band is considered for holes signifying ground state exciton. The electron-phonon and hole-phonon scattering process responsible for PL emissions are shown by fancy-arrows. (b) Corresponding excitonic energy dispersion showing lowest five excitons along the BZ. The  \( \Gamma \)  point (Q=0) corresponds to the K or  \( K' \)  in the electronic dispersion. The inset magnifies splitting of exciton energies at K. (c) Phonon dispersion exhibiting phonon energies modes along BZ. The individual atomic contribution is superimposed and is shown by the color-map. The dashed-lines ( \( e_{2} \)  and  \( e_{3} \) ) in the shaded area represent the two different phonon-assisted channels for exciton recombination in (a). Bottom panel (left to right): Excitonic probability distribution function and symmetry of the lowest exciton (shown by red circles in (b)) at momenta M ( \( e_{3} \) ),  \( \Gamma \)  ( \( e_{1} \) ),  \( Q_{\Gamma-K} \)  ( \( e_{4} \) ) and at K ( \( e_{2} \) ).

phonon processes (see Fig. 1(a)), where the hole is scattered by a phonon from K to K', resulting in a recombination at K'. The PL intensity peaks sharply at +1% strain, with a pronounced decline above and below this range due to a reduction in exc-ph coupling across different modes. These systematic findings can be useful as a textbook example to reveal the symmetry-driven indirect PL in 2D TMDs. The following discussions can also explain the non-monotonic PL response to biaxial strain recently observed in 2D WSe₂ [36].

To investigate 2D  \( MoS_{2} \) , we employ fully relativistic, norm-conserving pseudopotentials [37] with core corrections for Mo (core: [Ca]; valence: 3d, 4p, 5s, and 4d) and S (core: [Ne]; valence: 3s and 3p). Ground-state and excited-state computations were performed using Quantum Espresso [38] and Yambo [39], respectively. A total of 200 electronic states (26 occupied, 174 unoccupied) were sufficient to converge quasiparticle (QP) gaps, with a screening matrix cut-off of 20 Ry for both QP energies and the Bethe-Salpeter (BS) equation. Convergence tests (see Supplemental Material [40]) indicate that an 18×18×1 grid with Coulomb cut-off techniques [41] accurately reproduces excitonic energies within experimental ranges. Electron-phonon self-energies [42], including Debye-Waller corrections [43], were computed on a 60×60×1 fine grid. In the following discussion, we focus on results at +1% biaxial strain and compare them to other strain conditions as necessary.

The indirect emission process is a two-step mechanism governed by Fermi’s golden rule. An exciton transitions from its initial state,  \( |\varphi_{I}\rangle \) , to a final state,  \( |\varphi_{f}\rangle \) , via an intermediate state,  \( |\varphi_{I}\rangle \) . This involves a light coupling ( \( \hat{\xi} \) ) and phonon coupling ( \( \hat{g}_{q} \) ), which may occur in either order. The entire process can then be described by  \( \left\langle\varphi_{f}\left|\hat{g}_{q}^{\dagger}\hat{\varphi}\right|\varphi_{I}\right\rangle = \left\langle\varphi_{f}\left|\hat{g}_{q}^{\dagger}\right|\varphi_{I}\right\rangle \left\langle\varphi_{I}\left|\hat{\xi}\right|\varphi_{I}\right\rangle \) . The light-field polarization direction also imposes condition on the coupling of phonon modes with excitons via the symmetry of states that are excited, aligning with the selection rules dictated by the crystal’s point group symmetry. Such cases are reported for bulk h-BN, where in-plane and out-of-plane light-field polarization selectively allows LA/TA and Z phonon modes coupling with excitons [44, 45] and is found effective in overcoming limitations of indirect emission in WS \( _{2} \) .
 

(a)

![](./images/1083017860978049077_8.jpg)

(b)

![](./images/1083017860978049077_9.jpg)

(c)

![](./images/1083017860978049077_10.jpg)

(d)

![](./images/1083017860978049077_11.jpg)

![](./images/1083017860978049077_12.jpg)

0%

![](./images/1083017860978049077_13.jpg)

+0.75%

![](./images/1083017860978049077_14.jpg)

+1%

![](./images/1083017860978049077_15.jpg)

+3%

FIG. 2. (a)-(c): Phonon mode  \( A' \)  resolved exc-ph coupling  \( |\mathcal{G}(\mathbf{Q},\mathbf{q})| \)  across the exciton BZ at various strains. All values are normalized to  \( 10^{-4} \)  meV. Only the most prominent mode interaction contributing to the indirect and direct PL emission (Fig. 6 below) are shown. The x and y axes are in transferred exciton momenta. The intensity of the color-map shows the coupling strength.

[46, 47] and WSe_{2} [48] by strain engineering.

For a 2D MoS₂, the D₃h point group symmetry includes a fully symmetric (even) irreducible representation, A₁'. The in-plane (two-dimensional) components, x and y, transform as the E' representation, enabling mixing and transitions allowed by symmetry. The out-of-plane z component transforms as A₁', allowing additional transitions. Consequently, the overall transformation of the dipole operator can be expressed as E' [x, y] + A₁' [z]. This implies that when an incoming plane-polarized light field (used commonly in pump-probe experiment), represented by E' [x, y], interacts with a ground state of symmetry A₁', the resulting tensor product becomes A₁' ⊗ E' = E'. This corresponds to the symmetry of the energetically lowest doubly degenerate dark excitons (e₁) at the Γ point.

To analyze the symmetry of the intervalley excitons, we performed a rigorous finite-momentum BS equation calculation for the lowest five excitonic energies and states across the entire BZ. Momentum conservation indicates that the intervalley exciton  \( e_{2} \)  in Fig. 1(a) corresponds to the exciton at the K point in the exciton dispersion shown in Fig. 1(b). Similarly, exciton  \( e_{3} \)  and  \( e_{4} \)  are located at the M and about  \( \frac{1}{2} |\Gamma - K| \)  point respectively. The degeneracy at  \( \Gamma \)  is lifted due to spin-orbit coupling along the  \( \Gamma \) -K direction. At the K point, the point group symmetry reduces to  \( C_{3h} \) . The two-dimensional irreducible representation,  \( E' \) , transforms as the one-dimensional  \( E' \)  in  \( C_{3h} \) , which is even with respect to the mirror symmetry  \( \sigma_{h} \)  and highlights that the charge densities are predominantly localized at the hole sites. This corresponds to the symmetry of the lowest two excitons  \( e_{2} \)  at K. Similarly, the point group symmetry at the M towards  \( \Gamma \)  reduces to  \( C_{2v} \) , resulting in the double-point group irreducible representation  \( \Gamma_{5} \) , describing the degenerate excitons  \( e_{3} \)  at M. Additionally, the exciton  \( e_{4} \)  is odd with respect to both  \( \sigma_{v} \)  and  \( \sigma_{vv} \)  rotations within the  \( C_{2v} \)  group and as the degeneracy is lifted at this point, the split excitons have either  \( A_{2} \)  or  \( B_{2} \)  symmetry. We emphasize that biaxial strain in the 2D system does not alter the crystalline point group symmetry; thus, the symmetry representations remain invariant under applied strain. These symmetries are illustrated in the bottom panel of Fig. 1.

Similar to the electron-phonon matrix elements [42],

 \[ g_{m n,\nu}(\mathbf{k},\mathbf{q})=\langle m\mathbf{k}+\mathbf{q}|\Delta V_{v\mathbf{q}}|n\mathbf{k}\rangle, \quad (1) \] 

where  \( g_{mn,\nu}(\mathbf{k}, \mathbf{q}) \)  denotes the electronic scattering probability amplitude for a transition from an initial Bloch state  \( |n\mathbf{k}\rangle \)  to a final state  \( |m\mathbf{k} + \mathbf{q}\rangle \)  via phonon absorption or emission and  \( \Delta V_{v\mathbf{q}} \)  represents the Kohn-Sham potential perturbed by phonons, the exc-ph matrix elements can be expressed as [49]

 \[ \mathcal{G}_{n m v}(\mathbf{Q},\mathbf{q})=\sum_{\mathbf{k}}\left|\sum_{v c c^{\prime}}A_{v\mathbf{k},c(\mathbf{Q}+\mathbf{q})}^{m}(\mathbf{Q}+\mathbf{q})_{v\mathbf{k},c^{\prime}(\mathbf{k}+\mathbf{q})}^{A_{v,n}(\mathbf{Q})}A_{v\mathbf{k},c^{\prime}(\mathbf{k}+\mathbf{q})}^{n,\mathbf{Q}}g_{c^{\prime}c v}(\mathbf{k}+\mathbf{Q},\mathbf{q})\right. \quad (2) \] 

 \[ -\sum_{c v v^{\prime}}A_{v(\mathbf{k}-\mathbf{q}),c(\mathbf{k}+\mathbf{q})}^{S_{m}(\mathbf{Q}+\mathbf{q})*}A_{v^{\prime}\mathbf{k},c(\mathbf{k}+\mathbf{q})S_{v^{\prime}}v c}^{S_{n}(\mathbf{Q})}(\mathbf{k}-\mathbf{Q},\mathbf{q})\Bigg] \quad (2) \] 

where  \( \mathcal{G}_{n m v}(\mathbf{Q},\mathbf{q}) \)  now denotes the probability amplitude for an exciton scattering from an initial state  \( |n\mathbf{Q}\rangle \)  to a final state  \( |m\mathbf{Q}+\mathbf{q}\rangle \) , mediated by absorption or emission of a phonon characterized by state  \( |v\mathbf{q}\rangle \) . The coupling strength is defined as  \( |\mathcal{G}_{n m v}(\mathbf{Q},\mathbf{q})|^{2} \) .  \( A_{v(\mathbf{k})}^{S_{m}(\mathbf{Q}+\mathbf{q})*} \)  is the coefficient representing the exciton envelope function, describing the probability amplitude for a hole with momentum k and an electron with momentum  \( k+Q \) . The exc-ph interaction in Eqn. (2) can be interpreted as a quantum superposition of electron and hole scattering events with phonons, with each event weighted by the exciton wavefunction represented in the transition basis. After incorporating the long-range Coulomb Hartree potential (with reciprocal
 

lattice vectors G=0) in the finite-BS equation calculation and obtaining the phonon energies from density functional perturbation theory, we computed the exc-ph coupling strength for the lowest exciton.

We highlight here the prominent phonon modes that strongly interact with the lowest indirect exciton. By analyzing the transferred momentum between the larger and reduced point group symmetries (Fig. 1(c)), we identify intervalley modes between M and K with  \( C_{s}(m) \)  symmetry as key contributors. These modes belong to branches characterized by  \( A' \)  (even under  \( \sigma_{h} \) ) or  \( A'' \)  (odd under  \( \sigma_{h} \) ), which drive both indirect and direct scattering processes. Using the compatibility table [3], we find that the  \( E' \)  exciton at K reduces to  \( A' \)  in  \( C_{s}(m) \) , allowing symmetric coupling. In contrast, when reducing to  \( A'' \) , the antisymmetric representation results in forbidden interactions. Consequently, modes 1, 4, 5, and 9, which are  \( A'' \) , do not contribute to indirect emission at any strain. This contrasts with excitons at  \( \Gamma \) , where all modes are symmetry-allowed to couple. Figure 2 illustrates these interactions under

![](./images/1083017860978049077_16.jpg)

![](./images/1083017860978049077_17.jpg)

FIG. 3. (a) Relaxation time at +1% strain for the lowest five excitons (1-5) at  \( \Gamma \)  as function of temperature. Phonon mode resolved normalized scattering rates of excitons 1 and 5 at (b) 10 K and (c) 300 K.

various strain levels. For instance, the subplot (a) shows for the unstrained case, where only significant allowed modes are 3 and 7 that would exhibit noticeable interaction with the lowest exciton between  \( \Gamma \) -M and around  \( \Gamma \)  respectively. While other modes are less significant, the subplot demonstrates that coupling between the  \( \Gamma \)  and M points is primarily driven by mode 3. However, mode 7 exhibits stronger coupling, predominantly interacting with excitons localized near  \( \Gamma \) . Subplot (b) shows the exc-ph coupling strength at +0.75% strain for the lowest exciton interacting with phonon mode 3 and 8 with mode 3 having similar strength compared to the previous case.

At higher strain levels (+1% and +3%), as shown in sub-

<table><tr><td>Reduction to</td><td>Mode:  \( A&#x27; \)  ( \( C_{s}(m) \) )</td><td>Mode:  \( A&#x27;&#x27; \)  ( \( C_{s}(m) \) )</td></tr><tr><td>Excision:  \( E&#x27; \)  at  \( \mathbf{K} \)  ( \( C_{3h} \) )</td><td>\( A&#x27; \)</td><td>0</td></tr><tr><td>Excision:  \( \Gamma_{5} \)  at  \( \mathbf{M} \)  ( \( C_{2v} \) )</td><td>\( A&#x27; \oplus A&#x27;&#x27; \)</td><td>\( A&#x27; \oplus A&#x27;&#x27; \)</td></tr></table>

TABLE I. Allowed exciton (lowest) and phonon mode interactions in various point groups. The SI [40] contains detailed discussion on our group-theoretic results.

plots (c) and (d), the coupling strength increases significantly compared to the respective modes (see Figs. S17-S23 in the SI [40] for plots of intermediate strain values). At +1%, modes 3 and 8 strongly interact with the lowest exciton near M and around  \( \Gamma \) , respectively. This observation aligns with the exciton dispersion in Fig. 1(b), which suggests phonon-assisted exciton scattering in these states. Additionally, mode 8 shows substantial interaction with the exciton near the K and  \( K' \)  points, indicating strong scattering in these regions. At +3%, the interaction distribution for mode 3 becomes more widespread across all high-symmetry points. However for mode 8, the interaction strength significantly drop-out but becomes increasingly localized around  \( \Gamma \) , K, and  \( K' \)  points, reflecting a shift in the coupling dynamics.

Using the coupling strengths, we find the scattering rates for each of the five excitons at  \( \Gamma \)  in Fig. 3. The exc-ph scattering rate can be computed from [49]

 \[ \begin{aligned}&\Gamma_{\mathrm{nq}}^{\mathrm{ex-ph}}(T)=\frac{2\pi}{\hbar}\frac{1}{N_{\mathbf{q}}}\sum_{\mathbf{n}\mathbf{m}\mathbf{v}}|\mathcal{G}_{\mathbf{n}\mathbf{m} \mathbf{v}}(\mathbf{Q},\mathbf{q})|^{2}\times\\&\left[(N_{\mathbf{v}\mathbf{q}}\pm1/2\pm F_{m\mathbf{Q}+\mathbf{q}}+1/2)\times\delta(E_{n\mathbf{Q}}-E_{m\mathbf{Q}+\mathbf{q}}^{\prime}\pm\hbar\omega_{\mathbf{v}\mathbf{q}})\right]\\ \end{aligned} \quad (3) \] 

where  \( N_{vq} \)  and  \( F_{mQ+q} \)  represent the phonon and excitonic occupation factors, respectively, and  \( N_{q} \)  is the total number of discrete phonon points. The relaxation time is then given as the inverse of the scattering rate,  \( \tau_{\mathrm{ex-ph}}^{\mathrm{exp}}(T) = 1/\Gamma_{\mathrm{nq}}^{\mathrm{ex-ph}}(T) \) , which is plotted in Fig. 3(a)-(c). From these plots, we see the general trend of increment of the scattering rate with temperature for all excitons [34], albeit with varying slopes. This indicates that higher temperatures lead to stronger exciton-phonon interactions across the spectrum. To gain further insight, we analyzed the contributions of individual phonon modes to the scattering rate at cryogenic (10 K) and room temperature (300 K) for the two excitons: exciton 1 and exciton 5 at  \( \Gamma \) . The contributions are normalized to the total scattering rate at their respective temperatures. The impact of modes 3 and 8 on the scattering of the exciton 1 is evident and is attributed to the exc-ph interaction at both 10 K and 300 K. In contrast, for the exciton 5, modes 3 and 7 are the primary contributors at these temperatures.

Figure 4 illustrates the linewidth ( \( \Delta \) ) as a function of temperature for the above two excitons 1 and 5 at  \( \Gamma \) . For exciton 1, the  \( \Delta \)  is interpreted to fall under the strong-coupling regime following Toyozawa's equation [50, 51]:

 \[ \Delta=\sqrt{\Delta_{\mathrm{A}}^{2}+\Delta_{\mathrm{O}}^{2}} \quad (4) \] 

where  \( \Delta_{\mathrm{A}}^{2}=S_{\mathrm{A}}E_{\mathrm{A}}\coth\left(\frac{E_{\mathrm{A}}}{2k_{B}T}\right) \)  represents the broadening due to acoustic phonons, and  \( \Delta_{\mathrm{O}}^{2}=S_{\mathrm{O}}E_{\mathrm{O}}\left[\exp\left(\frac{E_{\mathrm{O}}}{2k_{B}T}\right)-1\right]^{-1} \)  accounts for the broadening caused by optical phonons. Here,
 
![](./images/1083017860978049077_18.jpg)

FIG. 4. Linewidth for exciton 1 and 5 at  \( \Gamma \)  as a function of temperature at +1% strain. Symbols are the ab-initio result where as broken lines are fitted from the appropriate linewidth models.

 \( S_{A} \)  and  \( S_{O} \)  are the fitted exc-ph coupling strengths for acoustic and optical phonons, respectively, and  \( E_{A} \)  and  \( E_{O} \)  are their mean phonon energies. For exciton 1 under +1% strain, we fit the data using the parameters  \( S_{A} = 2.27 \)  meV,  \( S_{O} = 0.1 \)  meV,  \( E_{A} = 25 \)  meV, and  \( E_{O} = 48.1 \)  meV. In contrast, exciton 5 ex-

![](./images/1083017860978049077_19.jpg)

FIG. 5. Lowest energy phonon replicas at 10 K for various strains. "The  \( \times \) " symbol denotes a forbidden indirect PL due to symmetry. The intensity scale is absolute. The inset shows the experimental cryogenic direct PL (symbols) from [23] for unstrained 2D  \( MoS_{2} \) . The solid line is our ab-initio result.

hibits weak coupling at lower temperatures, which is modeled using

 \[ \gamma=\gamma_{0}+a T+b\left[\exp\left(\frac{E_{O}}{k_{B}T}\right)-1\right]^{-1} \quad (5) \] 

where \(a (= 2 \text{ meV/K})\) and \(b (= 10 \text{ meV})\) represent the contributions from acoustic and optical phonon coupling, respectively, and \(\gamma_{0} (= 29.3 \text{ meV})\) is a temperature-independent offset. For exciton 5, weak coupling dominates up to approximately 225 K. Beyond this temperature, the broadening transitions to being governed by strong coupling. However, it is noted that the linewidth roll-off rates remain relatively modest. We resolved that the modes 3 and 8 for exciton 1 while 3 and 7 (\(A'\) for exciton 5, are responsible to account such coupling in \(\Delta\).

To compute the PL intensity, we employ Eqn. (2) within the ab-initio framework implemented in the Yambo code. A damping factor of 2 meV is applied to account for the exc-ph self-energy, and five virtual exciton states are included in the

![](./images/1083017860978049077_20.jpg)

![](./images/1083017860978049077_21.jpg)

![](./images/1083017860978049077_22.jpg)

![](./images/1083017860978049077_23.jpg)

FIG. 6. PL intensities with increasing temperatures at +1% strain demonstrating phonon replicas for the modes 3 and 8. The energies are measured as shift from the first bright exciton at  \( \Gamma \) . The inset in (b) and (c) shows the atomic vibrations for the modes 3 and 8. The dotted symbols in (d) represent the hole-phonon process in the PL intensity.

exc-ph scattering process. To ensure our analyses are on right track, we confirmed our excitonic dispersion to be in excellent agreement with Wu et. al. [52] at unstrained condition. Figure 5 illustrates the lowest-energy PL intensity peaks under various strain conditions. Our ab-initio results for direct PL from unstrained  \( MoS_{2} \)  monolayer show excellent agreement with experimental findings (inset in Fig. 5) [23]. We observe the emergence of a doublet structure, reaching its maximum at +1% strain driven by intense exc-ph interactions. This is in contrast to +0.75%, where the PL is only due to the dominant mode 8. To highlight this non-monotonic behavior, we present the exciton thermalization process in Fig. 6(a)-(d). The emission energies are referenced relative to the first bright exciton at  \( \Gamma \)  in the excitonic BZ. Consequently, all emissions to the left of the zero-energy line correspond to indirect processes. Our results can provide an insight to the recently reported PL emission by López et. al. [36] for  \( WSe_{2} \) . While López et. al. attribute their similar non-monotonic PL variation (see Fig. 3 in their work) to the energetic resonance of indirect excitons with defect-related states, we believe that contributions from intense symmetry-allowed exc-ph interactions, such as highlighted in this work, cannot be overlooked.

At cryogenic temperatures, as shown in Fig. 6(d), the emission lines exhibit two prominent phonon replicas. These Gaussian-type replicas, located approximately 50 and 70 meV
 
![](./images/1083017860978049077_24.jpg)

![](./images/1083017860978049077_25.jpg)

FIG. 7. Normalized PL intensities with varying temperatures at unstrained and +1% strain. The vertical dashed line in all cases shows the direct bright recombination.

below the bright line, are attributed to the intervalley acoustic and optical modes 3 and 8, respectively, along the M-K direction (see the dashed line in Fig. 1(c) corresponding to the  \( \varepsilon_{2} \)  exciton). Mode 3 originates from in-plane vibrations of Mo atoms (shear mode), while mode 8 corresponds to out-of-plane vibrations. As a general trend, the PL associated with the optical mode appears at lower energy than that associated with the acoustic mode. To discern whether the observed peaks arise from electron-phonon or hole-phonon scattering processes (see Eqn. (2)), we evaluated the PL intensity separately for their contributions. Our analysis reveals that the lower-energy PL peak is primarily driven by the hole-phonon process. Specifically, this peak arises from optical phonons facilitating hole scattering from K to K', leading to recombination at K'. The strong exc-ph interaction responsible for such recombination is further illustrated by the coupling matrix  \( |\mathcal{G}(\mathbf{Q}, \mathbf{q})| \)  in Fig. 2(c) and schematically depicted in Fig. 1(a). Interestingly, this behavior remains same at all higher strains. This feature serves as a textbook example of how exciton scattering at K and K' transitions from a no-phonon to a hole-phonon process.

The next higher-energy peak, around 50 meV, corresponds to excitons close to  \( \Gamma \)  along the  \( \Gamma \) -M direction, which require small acoustic phonon energies for scattering. However, we note that excitons  \( e_{3} \)  and  \( e_{4} \)  are confined to scatter within themselves using intervalley optical phonon mode 8 ( \( \sim \) 42 meV) but lack any available recombination path. Below 50 K, there is no significant exciton thermalization that would result in a  \( \Gamma \) -centered recombination channel. At 100 K,  \( \Gamma \) -centered recombination begins to appear, predominantly driven by optical modes 7 and 9 (see Fig. 15-21 in the SI [40] for the corresponding exc-ph plots). As the temperature increases, the lower-energy curves do not appear to red or blue shift, however broadens with satellites emerging in the energy range 20–40 meV above and below the bright line. The emergence of the  \( \Gamma \) -centered emission with temperature in Fig. 6(a)-(c) is a clear indication of the sharing of the oscillator strengths between the indirect and direct excitons.

To understand how the emission energy shifts and the PL intensity is maximized with temperature, we present results under unstrained and +1% strain conditions in Fig. 7(a)-(b) respectively. A clear redshift of the bright emission is observed as the strain transitions. Under unstrained conditions, faint indirect emission is visible near 1.73 eV, while the direct bright emission is the strongest among all strain conditions. At lower strains (see Fig. S25 in the SI [40]), the intensities around the direct path become most prominent due to satellite weights that thermalize at higher temperatures. The maximum intensity of the indirect excitons at cryogenic temperatures is observed at +1% strain. At higher strain levels, the indirect emissions become more distributed, but their intensities drop significantly due to weaker exciton-phonon couplings. We also note that the appearance of the doublet peaks at higher strains (such as beyond +1%) reverse their intensity magnitude, as shown in Fig. 5. These are due to the additive contribution from other modes at the low-energy side peak. A few additional tasks remain, such as identifying the symmetries of the indirect spin-split excitons  \( e_{2} \)  with respect to  \( C_{3} \)  rotation, which will be addressed in future work.

In summary, we investigate ab-initio exciton-phonon couplings in 2D  \( MoS_{2} \)  using a quantum superposition approach for electron and hole scattering events with phonons. Through rigorous ab-initio calculations and group-theoretic analyses, we demonstrate that indirect emission in 2D  \( MoS_{2} \)  under in-plane light polarization is symmetry-allowed for both acoustic and optical phonon modes with  \( A' \)  character. This systematic study serves as a textbook example of how indirect exciton recombination, absent in the compressive and unstrained cases, becomes dominated by hole-phonon scattering processes ( \( K \)  to  \( K' \)  transitions) under tensile strain. We find that this transition maximizes the indirect emission around +1% strain at cryogenic temperatures, driven by enhanced exciton-phonon scatterings assisted by intervalley  \( A' \)  phonon modes with reduced point group  \( C_{S}(m) \) . These results provide an alternative explanation for the non-monotonic PL variations with strain reported in recent experiments [36].

This work was carried out with financial support from SERB, India with grant number CRG/2023/000476. We acknowledge the National Super Computing Mission (NSM) for providing computing resources of “Paramshivay” at IIT BHU, India.
 

bridge University Press, 1992).

[3] M. S. Dresselhaus, G. Dresselhaus, and A. Jorio, Group theory: Application to the Physics of Condensed Matter, 1st ed. (Springer-Verlag Berlin Heidelberg, Germany, 2008).

[4] P. V. G. Cassabois and B. Gil, Nat. Photonics 10, 262–266 (2016).

[5] W. Yao, D. Xiao, and Q. Niu, Phys. Rev. B 77, 235406 (2008).

[6] D. Xiao, G.-B. Liu, W. Feng, X. Xu, and W. Yao, Phys. Rev. Lett. 108, 196802 (2012).

[7] T. Cao, G. Wang, W. Han, H. Ye, C. Zhu, J. Shi, Q. Niu, P. Tan, E. Wang, B. Liu, and J. Feng, Nat. Commun. 3, 887 (2012).

[8] H. Zeng, J. Dai, W. Yao, D. Xiao, and X. Cui, Nat. Nanotechnol. 7, 490–493 (2012).

[9] K. F. Mak, K. He, J. Shan, and T. F. Heinz, Nat. Nanotechnol. 7, 494–498 (2012).

[10] A. M. Jones, H. Yu, N. J. Ghimire, S. Wu, G. Aivazian, J. S. Ross, B. Zhao, J. Yan, D. G. Mandrus, D. Xiao, W. Yao, and X. Xu, Nat. Nanotechnol. 8, 634–638 (2013).

[11] A. Srivastava, M. Sidler, A. V. Allain, D. S. Lembke, A. Kis, and A. Imamoglu, Nat. Phys. 11, 141–147 (2015).

[12] J. P. Echeverry, B. Urbaszek, T. Amand, X. Marie, and I. C. Gerber, Phys. Rev. B 93, 121107(R) (2016).

[13] T. Deilmann and K. S. Thygesen, Phys. Rev. B 96, 201113(R) (2017).

[14] E. Malic, M. Selig, M. Feierabend, S. Brem, D. Christiansen, F. Wendler, A. Knorr, and G. Berghäuser, Phys. Rev. Lett. 2, 014002 (2018).

[15] G. Wang, A. Chernikov, M. M. Glazov, T. F. Heinz, X. Marie, T. Amand, and B. Urbaszek, Phys. Rev. B 90, 021001 (2018).

[16] T. Mueller and E. Malic, NPJ 2D Mater. Appl. 2, 29 (2018).

[17] A. Splendiani, L. Sun, Y. Zhang, T. Li, J. Kim, C.-Y. Chim, G. Galli, and F. Wang, Nano Lett. 10, 1271–1275 (2010).

[18] H. R. Gutiérrez, N. Perea-López, A. L. Elías, A. Berkdemir, B. Wang, R. Lv, F. López-Urias, V. H. Crespi, H. Terrones, and M. Terrones, Nano Lett. 13, 3447–3454 (2013).

[19] Y. Zhang, T.-R. Chang, B. Zhou, Y.-T. Cui, H. Yan, Z. Liu, F. Schmitt, J. Lee, R. Moore, and Y. C. et al., Nat. Nanotechnol. 9, 111 (2014).

[20] M. Palummo, M. Bernardi, and J. C. Grossman, Nano Lett. 5, 2794 (2015).

[21] K. He, N. Kumar, L. Zhao, Z. Wang, K. F. Mak, H. Zhao, and J. Shan, Phys. Rev. Lett. 113, 026803 (2014).

[22] X.-X. Zhang, T. Cao, Z. Lu, Y.-C. Lin, F. Zhang, Y. Wang, Z. Li, J. C. Hone, J. A. Robinson, D. Smirnov, S. G. Louie, and T. F. Heinz, Nat. Nanotechnol. 12, 883–888 (2017).

[23] C. Robert, B. Han, P. Kapuscinski, A. Delhomme, C. Faugeras, T. Amand, M. R. Molas, M. Bartos, K. Watanabe, T. Taniguchi, B. Urbaszek, M. Potemski, and X. Marie, Nat. Commun. 11, 4037 (2020).

[24] T. Yu and M. W. Wu, Phys. Rev. B 89, 205303 (2014).

[25] Z. Wang, A. Molina-Sánchez, P. Altmann, D. Sangalli, D. D. Fazio, G. Soavi, U. Sassi, F. Bottegoni, F. Ciccacci, M. Finazzi, L. Wirtz, A. C. Ferrari, A. Marini, G. Cerullo, and S. D. Conte, Nano Lett. 18, 6882 (2018).

[26] S. Brem, A. Ekman, D. Christiansen, F. Katsch, M. Selig, C. Robert, X. Marie, B. Urbaszek, A. Knorr, and E. Malic, Nano Lett. 20, 2849 (2020).

[27] C. M. Chow, H. Yu, A. M. Jones, J. R. Schaibley, M. Koehler, D. G. Mandrus, R. Merlin, W. Yao, and X. Xu, NPJ 2D Mater.

Appl. 1, 33 (2017).

[28] D. Li, C. Trovatello, S. D. Conte, M. Nuß, G. Soavi, G. Wang, A. C. Ferrari, G. Cerullo, and T. Brixner, Nat. Commun. 12, 954 (2021).

[29] S. Zheng, J.-K. So, F. Liu, Z. Liu, N. Zheludev, and H. J. Fan, Nano Lett. 17, 6475–6480 (2017).

[30] V. Chellappan, A. L. C. Pang, S. Sarkar, Z. E. Ooi, and K. E. J. Goh, Electron. Mater. Lett. 14, 766 (2018).

[31] Y. Miyauchi, S. Konabe, F. Wang, W. Zhang, A. Hwang, Y. Hasegawa, L. Zhou, S. Mouri, M. Toh, G. Eda, and K. Matsuda, Nat. Commun. 9, 2598 (2018).

[32] T.-Y. Jeong, S. Bae, S.-Y. Lee, S. Jung, Y.-H. Kim, and K.-J. Yee, Nanoscale 12, 22487–22494 (2020).

[33] V. Funk, K. Wagner, E. Wietek, J. D. Ziegler, J. Förste, J. Lindlau, M. Förg, K. Watanabe, T. Taniguchi, A. Chernikov, and A. Högele, Phys. Rev. Res. 3, L042019 (2021).

[34] H.-Y. Chen, D. Sangalli, and M. Bernardi, Phys. Rev. Res. 4, 043203 (2022).

[35] H. Li, A. W. Contryman, X. Qian, S. M. Ardakani, Y. Gong, X. Wang, J. M. Weiss, C. H. Lee, J. Zhao, P. M. Ajayan, J. Li, H. C. Manoharan, and X. Zheng, Nat. Commun. 6, 7381 (2015).

[36] P. H. López, S. Heeg, C. Schattauer, S. Kovalchuk, A. Kumar, D. J. Bock, J. N. Kirchhof, B. Höfer, K. Greben, D. Yagodkin, L. Linhart, F. Libisch, and K. I. Bolotin, Nat. Commun. 13, 7691 (2022).

[37] D. R. Hamann, Phys. Rev. B 88, 085117 (2013).

[38] P. Giannozzi, O. Andreussi, T. Brumme, O. Bunau, M. B. Nardelli, M. Calandra, R. Car, C. Cavazzoni, D. Ceresoli, and M. C. et al., J. Phys.: Condens. Matter 29, 465901 (2017).

[39] D. Sangalli, A. Ferretti, H. Miranda, C. Attaccalite, I. Marri, E. Cannuccia, P. Melo, M. Marsili, F. Paleari, A. Marrazzo, et al., J. Condens. Matter Phys. 31, 325902 (2019).

[40] See Supplemental section at http://supplemental/ for necessary convergence and supporting figures.

[41] A. Guandalini, P. D'Amico, A. Ferretti, and D. Varsano, NPJ Comput. Mater. 9, 44 (2023).

[42] H. Y. Fan, Phys. Rev. 6, 808 (1950).

[43] E. Cannuccia and A. Marini, Phys. Rev. lett. 107, 255501 (2011).

[44] F. Paleari, H. P. Miranda, A. Molina-Sánchez, and L. Wirtz, Phys. Rev. Lett. 122, 187401 (2019).

[45] T. Q. P. Vuong, G. Cassabois, P. Valvin, V. Jacques, A. V. D. Lee, A. Zobelli, K. Watanabe, T. Taniguchi, and B. Gil, 2D Mater. 4, 011004 (2016).

[46] Y. Pan and F. Caruso, NPJ 2D Mater. Appl. 8, 42 (2024).

[47] T. Chowdhury, S. Chatterjee, D. Das, T. Iimokhin, P. D. Núñez, G. M. A., S. Chatterjee, K. Majumdar, P. Ghosh, A. Mishchenko, and A. Rahman, Phys. Rev. B 110, L081405 (2024).

[48] O. B. Aslan, M. Deng, and T. F. Heinz, Phys. Rev. B 98, 115308 (2018).

[49] H.-Y. Chen, D. Sangalli, and M. Bernardi, Phys. Rev. Lett. 125, 107401 (2020).

[50] Y. Toyozawa, Prog. Theor. Phys. 20, 53 (1958).

[51] T. Q. P. Vuong, G. Cassabois, P. Valvin, S. Liu, J. H. Edgar, and B. Gil, Phys. Rev. B 95, 201202(R) (2017).

[52] F. Wu, F. Qu, and A. H. MacDonald, Phys. Rev. B 9, 075310 (2015).
 
