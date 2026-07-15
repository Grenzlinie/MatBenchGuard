# The $\alpha-\gamma$ transition of Cerium is entropy-driven

B. Amadon, $^{1}$ S. Biermann, $^{2}$ A. Georges, $^{2}$ and F. Aryasetiawan $^{3,4}$

$^{1}$CEA, Département de Physique Théorique et Appliquée, BP 12, 91680 Bruyères-le-Châtel, France
$^{2}$Ecole Polytechnique, Centre de Physique Théorique, 91128 Palaiseau Cedex, France
$^{3}$Research Institute for Computational Sciences, AIST,
1-1-1 Umezono, Tsukuba Central 2, Ibaraki 305-8568, Japan
$^{4}$CREST, Japan Science and Technology Agency

We emphasize, on the basis of experimental data and theoretical calculations, that the entropic stabilization of the $\gamma$-phase is the main driving force of the $\alpha$-$\gamma$ transition of cerium in a wide temperature range below the critical point. Using a formulation of the total energy as a functional of the local density and of the f-orbital local Green's functions, we perform dynamical mean-field theory calculations within a new implementation based on the multiple LMTO method, which allows to include semi-core states. Our results are consistent with the experimental energy differences and with the qualitative picture of an entropy-driven transition, while also confirming the appearance of a stabilization energy of the $\alpha$ phase as the quasiparticle Kondo resonance develops.

PACS numbers: 71.27.+a, 71.30.+h, 71.15.Nc

The $\alpha-\gamma$ phase transition of cerium [1, 2] is a first-order isostructural transition, ending at a second-order critical point at $T_c \simeq 600$K. When temperature decreases below $T_c$, the volume change between the two phases increases [3, 4], reaching $15\%$ at room temperature. The magnetic susceptibility follows Curie-Weiss behaviour in the (larger volume) $\gamma$- phase, and is Pauli-like in the (smaller-volume) $\alpha$- phase. This is interpreted as 4f electrons being localized in the $\gamma$- phase, giving rise to local moments and contributing weakly to the electronic bonding (hence the larger volume). In contrast, in the $\alpha$- phase, the 4f electrons participate in both the bonding and the formation of quasiparticles.

The detailed mechanism underlying the transition has been the subject of debate. In the Mott transition picture [5], the focus is put on the 4f orbitals only, while the Kondo volume collapse (KVC) picture [6] emphasizes the key role of the hybridisation between the 4f electrons and (spd-) conduction electron states which form broader bands. In this picture, the stronger hybridisation of the low-volume $\alpha$-phase leads to a high Kondo temperature and in turn to a screening of the 4f local moment, while the high-volume $\gamma$-phase has a low Kondo temperature, leading in practice to unscreened moments for $T > T_K^\gamma$. Photoemission experiments [7] demonstrate that both phases display Hubbard bands and hence are strongly correlated. In addition, a quasiparticle peak is seen in the $\alpha$ phase only. These observations are compatible with both pictures. However, a recent theoretical calculation [8] of the optical spectrum, in connection with the experimental results of Ref. [9], has emphasized the importance of hybridisation effects, in qualitative agreement with the KVC picture. In both the Mott and KVC pictures, the $\alpha$- phase is stabilized by energetic effects (the f-electron kinetic energy in the Mott picture, or the Kondo screening energy in the KVC picture), while the $\gamma$ phase is stabilized by its large spin-fluctuation entropy.

In this letter, we argue that entropic effects actually play the dominant role in the transition, at least in the temperature range $300\mathrm{K} < T < T_c$. Using available experimental data, we estimate the jump in entropy and internal energy ($\Delta S = S_\gamma - S_\alpha, \Delta E = E_\gamma - E_\alpha$) and find that $T\Delta S$ is always significantly larger than $\Delta E$ in this temperature range. The second purpose of this article is to examine whether this conclusion is consistent with total energy calculations within the LDA+DMFT scheme, a combination of density-functional theory (DFT) within the local density approximation (LDA) with dynamical mean-field theory (DMFT). Recently, cerium has been the focus of pioneering theoretical work [8, 10-12] using the LDA+DMFT approach. In Refs. [11], the total energy was studied and it was concluded that a negative curvature effect is apparent already at elevated temperatures ($T \sim 1600$K), corresponding to the energetic stabilization of the $\alpha$-phase which was viewed as ultimately driving the transition. Here, we reconsider this issue within a new implementation of LDA+DMFT using the multiple LMTO scheme, and basing our total energy calculations on a functional of the local density and f-orbital Green's function. Using extensive Quantum Monte-Carlo calculations, we are able to reach temperatures lower than the experimental $T_c$. Our results are consistent with the qualitative picture of an entropy-driven transition, and with the experimentally measured energy differences.

The Clausius-Clapeyron relation $dp/dT = \Delta S/\Delta V$ relates the slope of the transition line to the jump of the entropy and unit-cell volume $\Delta V = V_\gamma - V_\alpha$ at the transition. Furthermore, the continuity of the Gibbs free-energy yields the relation: $\Delta E - T\Delta S + p\Delta V = 0$. Using available experimental data [3, 4] on $dp/dT$ and $\Delta V$, one can thus determine the three quantities $\Delta E$, $T\Delta S$ and $p\Delta V$, which are plotted on Fig. 1 as a function of temperature. As clear from this graph, the entropic term $T\Delta S$

![](./images/867770163070501650_1.jpg)

FIG. 1: Experimental variation of the entropy term $T\Delta S$, energy $\Delta E$ and $p\Delta V$ (obtained as described in the text from the data of [4] -circles- and [3] -squares-), between the $\gamma$ and the $\alpha$ phase across the transition line in the P-T phase diagram. Dotted lines are extrapolations based on exact limits (at $T_c$ all three terms vanish, and $T\Delta S = \Delta E$ at $p=0$).

above room-temperature is of order $30-40$meV, more than twice as large as the energy difference $\Delta E$ between the two phases (of order $10-20$meV). The energetic stabilization of the $\alpha$-phase results in $\Delta E = E_\gamma - E_\alpha > 0$, but the difference in free-energy has the opposite sign: $\Delta F = F_\gamma - F_a = \Delta E - T\Delta S = -p\Delta V < 0$ precisely because the difference of entropy dominates over the energy difference. We conclude from this analysis that entropic effects are essential to the physics of the $\alpha$-$\gamma$ transition, at least at room temperature and above. We note that the relative importance of spin and lattice contributions to the entropic stabilization of the $\gamma$-phase is currently under debate, with very different conclusions reached from experimental studies of pure cerium [13] and of the $\text{Ce}_{0.9}\text{Th}_{0.1}$ alloy [14].

An accurate calculation of the electronic and lattice free-energy of cerium, from first principles, is a major challenge. While the calculation of the entropy is beyond the scope of this article, we focus in the following on the calculation of the total energy, at temperatures below the experimental $T_c$, within the LDA+DMFT framework. This raises two important methodological questions. The first one is the proper choice of the valence states to be included in the starting LDA- hamiltonian. Indeed, it is mandatory to include semicore states (in particular $5p$ states) in the valence when computing the energy, because these states contribute significantly to the variation of the energy upon compression. On the other hand, we have found that, within an LMTO-ASA framework, it is crucial to include the $6p$ orbitals in the valence in order to obtain a proper band-structure. Since in standard implementations of the LMTO-ASA method, the simultaneous inclusion of $5p$ and $6p$ orbitals in the valence states is not possible, previous works using DMFT for Ce were either restricted to spectral properties only [10] or have treated the different terms in the expression of the total energy within different implementation of DFT [11]. Secondly, in view of the small energy differences between the two phases (on the scale of 10 to 20meV), a precise formulation of the total energy functional must be used.

The starting Hamiltonian is constructed from an LDA calculation within the orthogonalized localized basis set of the multiple LMTO-ASA scheme [16], retaining $5s,5p,6s,6p,5d$ and $4f$ states in the valence band. We neglect spin-orbit coupling which has little effect on LDA energies in Cerium. Many body terms acting on the f-orbitals are added to this hamiltonian, as well as a double-counting correction term (as in LDA+U schemes [17]), so that the many-body hamiltonian reads $H = H_{\text{KS}} + H_{\text{U}} - H_{\text{DC}}$ with:

$$
\begin{aligned}
H_{\text{KS}} &= \sum_{\mathbf{k}LL'} h_{LL'}^{\text{KS}}(\mathbf{k})c_{\mathbf{k}L}^{\dagger}c_{\mathbf{k}L'} \tag{1} \\
H_{U} &= \frac{1}{2}U \sum_{\mathbf{R}} \sum_{ab\sigma} \hat{n}_{\mathbf{R}a}\hat{n}_{\mathbf{R}b}
\end{aligned}
$$

In this expression, $h_{LL'}^{\text{KS}}(\mathbf{k})$ denotes the Kohn-Sham (LDA) hamiltonian at a given $\mathbf{k}$-point, expressed in an (orthogonalized) LMTO basis set $\chi_L^{\mathbf{k}}$, with $L = \{lm\sigma\}$ and $L'$ running over the full valence set. The Hubbard term is written in real space, with $\mathbf{R}$ denoting atomic positions and $a,b$ running only over the f-orbitals. We use the value of the Coulomb interaction U=6 eV, computed by constrained LDA calculations in [2, 10].

In order to derive an expression for the total energy, we start from the ("spectral density") free-energy functional introduced by Kotliar and Savrasov [19], which depends on the total local electron density $\rho(\mathbf{r})$ and the on-site Green's function in the correlated subset of orbitals: $G_{ab}^{\mathbf{RR}}$ (denoted below $G_{ab}$ for simplicity). The functional is constructed by introducing source terms, $v_{KS}(\mathbf{r}) - v_c(\mathbf{r})$ (the difference of the Kohn Sham potential $v_{KS}$ and the crystal potential $v_c$), and $\Delta\Sigma_{ab}(i\omega_n)$, coupling to the density operators $\psi^{\dagger}(\mathbf{r})\psi(\mathbf{r})$ and to $\sum_{\mathbf{R}} \chi_a^*(\mathbf{r}-\mathbf{R})\psi(\mathbf{r},\tau)\psi^{\dagger}(\mathbf{r}',\tau')\chi_b(\mathbf{r}'-\mathbf{R}) = c_{a\mathbf{R}}(\tau)c_{b\mathbf{R}}^{\dagger}(\tau')$, respectively. The Luttinger-Ward [18] part of the functional is approximated by that of the on-site local many-body hamiltonian $H_U - H_{\text{DC}}$. This yields:

$$
\begin{aligned}
&\Omega[\rho(\mathbf{r}), G_{ab}; v_{KS}(\mathbf{r}), \Delta\Sigma_{ab}]_{\text{LDA+DMFT}} \\
&= -\frac{1}{\beta}\text{tr}\ln[i\omega_n + \mu + \frac{1}{2}\nabla^2 - v_{KS}(\mathbf{r}) - \chi^*. \Delta\Sigma . \chi] \\
&- \int d\mathbf{r}\left(v_{KS}-v_c\right)\rho(\mathbf{r}) - \text{tr}\left[G.\Delta\Sigma\right] \\
&+ \frac{1}{2}\int d\mathbf{r}d\mathbf{r}'\rho(\mathbf{r})U(\mathbf{r}-\mathbf{r}')\rho(\mathbf{r}') + E_{xc}[\rho(\mathbf{r})] \\
&+ \sum_{\mathbf{R}} \left(\Phi_{\text{imp}}[G_{ab}^{\mathbf{RR}}] - \Phi_{\text{DC}}[G_{ab}^{\mathbf{RR}}]\right) \tag{2}
\end{aligned}
$$

Minimization with respect to the sources gives a functional of the local Green function and the density only. Stationarity of this functional with respect to $\rho(\mathbf{r})$ and $G_{ab}$ yields the basic equations of LDA+DMFT [20], and

in particular, the self-consistency condition for the local Green's function: $G_{ab}(i\omega_n) = \sum_{\mathbf{k}} G(\mathbf{k}, i\omega_n)_{ab}$. The full Green's function reads: $\hat{G}^{-1}(\mathbf{k}, i\omega_n) = (i\omega_n+\mu)\cdot\mathbb{1}-\hat{h}^{\text{KS}}+\hat{V}_{DC}-\hat{\Sigma}_{\text{imp}}(i\omega_n)$, with $\Sigma_{\text{imp}}^{ab} = \delta\Phi_{\text{imp}}/\delta G_{ab}$ the local impurity self-energy and $V_{\text{DC}}^{ab} = \delta\Phi_{\text{DC}}/\delta G_{ab}$. From (2), an expression of the total energy within LDA+DMFT can finally be obtained as:

$$
E = E_{\text{DFT}} - \sum_{\lambda} \varepsilon_{\lambda}^{\text{KS}} + \langle H_{\text{KS}} \rangle + \langle H_U \rangle - E_{\text{DC}} \tag{3}
$$

Note that, importantly, the total energy does not simply reduce to the expectation value $\langle H \rangle$ of the many-body hamiltonian (1). In (3), $E_{\text{DFT}}$ is the expression of the energy within density-functional theory, $\sum_{\lambda} \varepsilon_{\lambda}^{\text{KS}}$ is the sum of the occupied Kohn-Sham eigenvalues and $\langle H_{\text{KS}} \rangle = \text{tr}\left[H_{KS}\hat{G}\right]$. Note that these last two terms do not cancel each other, since $\text{tr}\left[H_{KS}\hat{G}\right]$ is evaluated with the full Green's function including the self-energy, while $\sum_{\lambda} \epsilon_{\lambda}^{KS} = \text{tr}\left[H_{KS}\hat{G}_{KS}\right]$. Eq. (3) expresses that the latter term has to be removed from $E_{DFT}$, in order to correctly take into account the change of occupation of the Kohn Sham orbitals. The LDA+DMFT scheme should in principle be performed by imposing self-consistency not only on the DMFT quantities but also on the local density [15] (or equivalently on the LDA Hamiltonian), in such a way that $\rho(\mathbf{r}) = \langle \mathbf{r} | \hat{G} | \mathbf{r} \rangle$, i.e including the correlation-induced changes to the local density. However, for simplicity and in order to compare to previous works [11], we present as a first step in this paper calculations without full self-consistency on $\rho(\mathbf{r})$. The double-counting correction term is written in terms of the LDA occupancy of the f-orbital, as: $E_{DC} = U N_{\text{lda}}^f (N_{\text{lda}}^f -1)/2$. In order to solve the DMFT equations, we have used the Hirsch-Fye Quantum Monte Carlo algorithm, and studied the temperature range from 400K to 1600K. The number of sweeps was adjusted in order to obtain a precision on the energy of order 20meV, a rather demanding requirement at the lowest temperature. The kinetic energy $\langle H_{KS} \rangle = \sum_{n,\mathbf{k}} H_{KS}(\mathbf{k}) G(\mathbf{k}, i\omega_n)$ is computed in a direct manner, while the correlation energy $\langle H_U \rangle$ is computed from the double occupancy.

![](./images/867770163070501650_2.jpg)

FIG. 2: Experimental [7] and LDA+DMFT theoretical results for the PES and BIS spectra of $\alpha$ and $\gamma$ cerium

First, we display on Fig. 2 the spectral functions (obtained by maximum-entropy continuation of our QMC data) for the $\alpha$ and the $\gamma$ phase, in comparison to experimental spectra. As in previous LDA+DMFT studies [10, 11], the quasiparticle peak is correctly described in the $\alpha$ phase, while Hubbard bands are present both in the $\alpha$ and the $\gamma$ phases. Their intensities are correct (although their positions are not very accurately reproduced). These results give us confidence that the main physical features of both phases are correctly captured by our calculations.

![](./images/867770163070501650_3.jpg)

FIG. 3: Symbols: internal energy (E) vs. volume curves for cerium, computed within LDA+DMFT for different temperatures. Also shown is the free energy (F), calculated from the experimental pressure vs. volume curves (a:[13], b:[3]). The position of these experimental curves with respect to each other is arbitrary. Short vertical lines on these curves show the experimental volumes at each temperature. Arrows indicate the volume of each phase at room temperature, at the transition pressure.

On Fig. 3, we display our results for the energy as a function of volume for three different temperatures (1600K, 800K and 400K). Statistical error bars of the QMC calculation are indicated on these plots. At 1600K we observe a smooth curve with a minimum located at $31.0\pm0.5$ $\AA^3$. At 800K, the minimum is located at a somewhat lower volume and we note that the curvature decreases near the minimum of the curve and in particular for lower volumes. For 400K, this effect is strong enough to shift the minimum to $29\pm1$ $\AA^3$. According to experimental results [3, 4], the volume of the $\alpha$ and $\gamma$ phases at 400K are $28.5\pm0.1$ and $32.0\pm0.1$ $\AA^3$, and the difference of energy between these two phases is $13.5\pm4$meV (see Fig. 1). This value is quite consistent with our calculations, even though a precise theoretical value would require to reduce the statistical error bars even more. Overall, we do not find evidence for a region of negative curvature in the energy versus volume curve. However, because 400K is below the critical point, a double tangent should be present in the free-

energy vs. volume $F(V)$. We have plotted in Fig. 3 the experimental free-energy vs. volume curves deduced from recent pressure versus volume measurements at 413 K [3] and 300K [3, 13], by integrating the equation of state: $F(V)-F(V_{0})=-\int_{V_{0}}^{V} p(V') d V'$. For volumes be tween the equilibrium volumes of the $\alpha$ and $\gamma$ phases,(indicated by short vertical lines for each temperature), $F(V)$ is taken to be the common tangent. Comparison of the theoretical energy to the experimental free-energy suggests that the entropic stabilization of the $\gamma$ -phase is mainly responsible for the appearance of a region of neg- ative curvature in the free-energy $F(V)$. Moreover the entropic stabilization $T \Delta S$ is of order 40 meV at 400 K, as seen from Figs. 1 and 3, much larger than $\Delta E$.

Although we do not find a double tangent in the en- ergy versus volume curve, we do observe a decrease of the curvature and the flattening of the volume depen- dance of the energy, as temperature is reduced. In or- der to understand its physical origin, we have plotted in Fig. 4, as a function of volume, the two contributions $A=\langle H_{KS}\rangle-\sum_{\lambda} \epsilon_{\lambda}^{LDA}$ (ie the correlation induced changes to the kinetic and hybridization energies) and $B=\langle H_{U}\rangle$ (the interaction energy among f orbitals). A negative curvature is clearly seen to develop in A as T is reduced, consistent with the observed development of the Kondo resonance (Fig. 2) and with the stabilization energy of the $\alpha$ phase as previously emphasized in reference [11].

Finally, the number of f electrons computed in DMFT is plotted in Fig. 5 as a function of volume. As expected, this number is very close to 1 in the localized $\gamma$ phase while it increases at lower volume due to hybridization ef- fects. In contrast to reference [11], we find a monotonous decrease of $n_{f}$ as volume is increased. One should keep in mind however that $n_{f}$ depends on the basis set and the functional.

![](./images/867770163070501650_4.jpg)

FIG. 4: Evolution of $A=\operatorname{tr}[H_{KS} G]-\Sigma \epsilon_{\lambda}^{LDA}$ and $B=\langle H_{U}\rangle$(note that, in this case, the scale is four time larger) as a function of volume, computed in DMFT for different temper- atures.

In conclusion, we have revisited the problem of the volume-collapse transition of cerium, emphasizing that it is mainly entropy-driven. We have presented LDA+DMFT calculations of the total energy, obtained from a functional of the local density and local Green's function, within a new implementation based on the mul- tiple LMTO formalism. This allows us to include semi- core states and to calculate the Hamiltonian, the energy, as well as spectra within the same formalism. We confirm the development of a contribution to the kinetic and hy- bridisation energy stabilizing the $\alpha$ phase, as temperature is lowered and the Kondo quasiparticle resonance devel- ops, in qualitative agreement with the results of Ref. [11]. However, we find that the magnitude of this stabilization energy is too small to induce a pronounced negative cur- vature in the total energy curve, and that the transition is actually driven by entropy effects at least above room temperature. This is consistent with the experimental measurements of Drymiotis et al [21].

![](./images/867770163070501650_5.jpg)

FIG. 5: Evolution of the number of f electrons in LDA and DMFT for different temperatures as a function of volume.

We acknowledge useful discussions with A. I. Lichten- stein (who also shared with us his QMC code), as well as with K. Haule, K. Held, G. Kotliar and A. K McMa- han. This work has been supported by CEA, CNRS, Ecole Polytechnique and by an RTN contract of the E.U (HPRN-CT-2002000295). F. A. thanks NAREGI Nanoscience Project, MEXT, Japan, for financial sup- port. Note added: as this paper was being writ- ten, we learned of the preprint cond-mat/0504380 by A.K.McMahan, in which LDA+DMFT calculations are performed for several rare-earths, including also spin- orbit coupling. The conclusions of this recent work regarding cerium are qualitatively similar to those of Ref. [11].

[1] For a review, see: D. G. Koskimaki and K. A. Gschnei- dner Jr., in Handbook on the Physics and Chemistry of Rare Earths, ed. by K. A. Gschneidner Jr. and L. R. Eyring (North-Holland, Amsterdam, 1978)

[2] For a review, see: A. K. McMahan et al., J.Comput.-

Aided Mater. Des., **5**, 131 (1998), cond-mat/9805064.

[3] A. Schiwek, F. Porsch, and W. B. Hopzapfel, High Pres- sure Research **22**, 407 (2002); A. Schiwek, PhD, Univer- sität Paderborn, (2003)

[4] R. I. Beecroft and C. A. Swenson, J. Phys. Chem. Solids **15**, 234 (1960)

[5] B. Johansson, Phil. Mag., **30**, 469 (1974).

[6] J. W. Allen and R. M. Martin, Phys. Rev. Lett. **49**, 1106 (1982); J. W. Allen and L. Z. Liu, Phys. Rev. B **46**, 5047 (1992). M. Lavagna, C. Lacroix, and M. Cyrot, Phys. Lett. **90A**, 210 (1982).

[7] E. Wuilloud *et al.*, Phys. Rev. B **28**, R7354 (1983); D. M. Wieliczka, C. G. Olson, and D. W. Lynch, Phys Rev B **29**, 3028 (1984)

[8] K. Haule *et al.*, Phys. Rev. Lett **94**, 036401 (2005).

[9] J.W. van der Eb, A. B. Kuz'menko, and D. van der Marel, Phys. Rev. Lett. **86**, 3407 (2001).

[10] M. B. Zölfl *et al.*, Phys. Rev. Lett. **87**, 276403 (2001)

[11] K. Held, A.K. McMahan and R.T. Scalettar, Phys. Rev. Lett. **87**, 276404 (2001). A. K. McMahan, K. Held and R. T. Scalettar, Phys. Rev. B **67**, 075108 (2003)

[12] O. Sakai, Y. Shimizu and Y. Kaneta, (2005) cond- mat/0503675

[13] I.-K. Jeong *et al.*, Phys. Rev. Lett. **92**, 105702 (2004)

[14] M.E. Manley *et al.*, Phys. Rev. B **67**, 014103 (2003).

[15] S. Savrasov, G. Kotliar, and E. Abrahams, Nature **410**, 793 (2001).

[16] F. Aryasetiawan and O. Gunnarsson, Phys. Rev. B **49**, 7219 (1994)

[17] V. I. Anisimov *et al.*, Phys. Rev. B **48** 16929 (1993)

[18] J. M. Luttinger and J. C. Ward, Phys. Rev. **118**, 1417 (1960)

[19] S. Y. Savrasov and G. Kotliar, Phys. Rev. B **69**, 245101 (2004)

[20] A. Georges (2004) cond-mat/0403123

[21] F. Drymiotis *et al*, J. Phys. Cond. Matter **17**, L77 (2005)