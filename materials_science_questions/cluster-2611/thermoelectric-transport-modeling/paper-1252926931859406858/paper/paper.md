# Flat-band energy filtering in interacting systems:
conditions for improving thermoelectric performances

F. Cosco, $^{1}$ R. Tuovinen, $^{2}$ F. Plastina, $^{3,4}$ and N. Lo Gullo $^{3,4,*}$

$^{1}$Quantum algorithms and software, VTT Technical Research Centre of Finland Ltd, Tietotie 3, 02150 Espoo, Finland
$^{2}$Department of Physics, Nanoscience Center P.O. Box 35, 40014 University of Jyväskylä, Finland
$^{3}$Dipartimento di Fisica, Università della Calabria, 87036 Arcavacata di Rende (CS), Italy
$^{4}$INFN, Sezione LNF, gruppo collegato di Cosenza

Motivated by recent theoretical and experimental studies on the role of flatbands in the thermoelectric properties of $\text{Ni}_3\text{In}_{1-x}\text{Sn}_x$ compounds, we investigate electron transport in two minimal one-dimensional flatband models, the sawtooth and diamond chains, which differ in a crucial aspect: the flatband is separated from the dispersive band by a finite gap in the former, while the two bands touch in the latter. Using a non-equilibrium Green function framework with interactions treated at the Hartree-Fock and GW levels, we compute the full set of thermoelectric coefficients and the figure of merit $zT$ as functions of gate voltage and temperature. We show that, contrary to naive expectation, a perfectly isolated flat-band is a physically ill-founded thermoelectric: the electrical conductivity vanishes as the chemical potential enters the flat-band, rendering the large Seebeck coefficient and the apparent violation of the Wiedemann-Franz law physically meaningless. Optimal thermoelectric performance is instead achieved just below the flat-band edge, where the transmission function varies most rapidly with energy, consistent with the Mahan-Sofo picture, and requires a finite broadening of the flat-band through hybridization with dispersive states. We further show that electron-electron interactions renormalize the flat-band structure itself, inducing an interaction-driven narrowing of the bandwidth and, in the diamond chain, a correlation-induced opening of a gap between the flat-band and the dispersive band near half-filling. Mean-field treatments are found to systematically overestimate $zT$, highlighting the importance of beyond-mean-field correlations for quantitatively reliable predictions in flat-band thermoelectrics.

## I. INTRODUCTION

Achieving high thermoelectric performances is currently becoming a very active research topic, especially in low dimensional materials [1, 12, 21, 22, 34, 45, 61] . In particular understanding how electronic structure controls thermoelectric transport remains a central challenge in condensed-matter physics and materials design. In a seminal work, Mahan and Sofo [36] demonstrated that a delta-like transmission function optimizes the thermoelectric figure of merit $zT$, thereby establishing energy filtering as a fundamental design principle for thermoelectric materials. This insight has motivated extensive efforts to engineer band structures and scattering mechanisms that generate narrow transport resonances. Flat-band systems [33] offer a particularly promising route toward realizing this principle. The dispersionless character of a flat band concentrates a macroscopic density of states within a narrow energy window, providing intrinsic spectral selectivity. However, the vanishing group velocity of perfectly flat bands suppresses direct charge transport, so that an isolated flat band contributes little to conductance [3]. Recent theoretical work has shown that this limitation can be overcome when flat-band states are coupled to nearby dispersive bands: scattering and hybridization convert the large density of states into sharp resonant features in the transmission, effectively implementing the optimal energy-filter mechanism and enhancing thermoelectric response [18, 19]. These results highlight the importance of the relative band alignment and interband coupling in determining the transport properties of flat-band lattices.

At the same time, rapid progress in band-structure engineering has enabled the controlled realization of flat bands in low-dimensional systems. In particular, synthetic and nanoscale one-dimensional lattices have been shown to host tunable flat or nearly flat bands whose energetic position can be brought close to the Fermi level [17, 52]. Such geometries provide highly controllable minimal platforms in which the interplay between lattice topology, band flatness, and quantum transport can be studied microscopically. One-dimensional models are therefore especially well suited for identifying generic mechanisms that may extend to more complex materials.

In this work, we investigate the transport and thermoelectric properties of two paradigmatic one-dimensional models with flat bands: the sawtooth chain and the diamond chain [4, 11], where the names refer to the shape of the crystal are shown in Fig. 1. These systems realize complementary regimes of flat-band physics. The sawtooth chain hosts an isolated flat band that is well separated from dispersive states, providing a reference limit in which flat-band modes remain largely decoupled from conducting channels. In contrast, the diamond chain features a flat-band in close proximity to dispersive bands, naturally enabling hybridization and interband scattering. This distinction allows us to directly assess how band isolation versus band mixing controls the emergence of energy-selective transmission and the resulting thermo-

* nicolino.logullo@unical.it

![](./images/1252926931859406858_1.jpg)

Figure 1. (Color online). Schematic illustration of the two models used in this work to study the thermoelectric properties of interacting electrons in flat-band systems. Panel a) shows the sawtooth chain, which hosts an isolated flat-band separated from a dispersive band by a finite energy gap. Panel b) shows the diamond chain, whose flat-band touches the dispersive band at a single point in momentum space, with no gap. In both cases, the system is connected to a hot and a cold reservoir and electrons are subject to a local Hubbard repulsion $U$. The Fermi-Dirac distributions of the two leads are shifted relative to one another by the temperature bias, driving a thermoelectric current through the flat-band system.

electric response.

Microscopically, thermoelectric transport can be addressed via density functional theory (DFT)-based approaches [16], where charge and heat currents are treated on similar footing as the electronic ground-state problem. Within steady-state DFT, the Landauer-Büttiker transmission can be constructed from Kohn-Sham spectra, enabling efficient evaluation of quantities such as the Seebeck coefficient and figure of merit [47]. Extensions to multiterminal setups [46] and analytically tractable model systems such as double quantum dots [48] have further broadened its applicability, while thermal density functional theory provides a route to include temperature effects and fluctuations [39]. Despite this progress, DFT faces intrinsic challenges in non-equilibrium transport settings. In particular, its practical accuracy relies on approximate exchange-correlation functionals, which can be inadequate for strongly correlated systems [5]. Moreover, standard DFT is not naturally formulated for open quantum systems driven out of equilibrium, where the treatment of leads and bias voltages becomes non-trivial [29, 49, 56]. While time-dependent formulations provide a formally exact route via a partition-free setup, their practical implementation remains demanding and not straightforward for general transport scenarios [15, 50]. Related issues can arise when propagating scattering states [26] or, e.g., in density-matrix renormalization group approaches [14] requiring a full microscopic description of both the conducting device and the leads.

These limitations motivate us to use of the non-equilibrium Green function (NEGF) formalism, which provides a natural framework for open, biased quantum systems [44, 51]. Within NEGF, many-body correlations are incorporated systematically through the self-energy, enabling controlled approximations beyond mean-field. This makes it particularly suitable for studying steady-state transport as well as time-dependent phenomena, including temperature-driven dynamics [40, 41, 55]. Here, we employ NEGF to compute charge and heat currents while retaining the full energy dependence of the transmission. Electronic interactions are treated at the level of Hartree-Fock and GW approximations, allowing us to disentangle mean-field renormalization from dynamical correlation effects. Such interactions are expected to play a central role in flat-band systems, where the enhanced density of states amplifies correlation effects and strongly reshapes spectral and transport properties [8].

By combining band-structure engineering with interacting quantum transport calculations, we demonstrate that proximity-induced coupling between flat and dispersive bands generates sharp transmission resonances that closely approach the ideal energy-filter condition and strongly enhance the Seebeck coefficient and thermoelectric power factor. Conversely, when the flat band is spectrally isolated, interaction effects predominantly renormalize localized states without producing significant transport enhancement. Our results elucidate how geometry, hybridization, and many-body effects cooperate to control thermoelectric performance in flat-band systems and provide design principles for low-dimensional platforms where such band structures could be engineered experimentally.

## II. NEGFS APPROACH TO THERMOELECTRICS

In Ref. [36] the authors derived the form of the transport distribution yielding the optimal thermoelectric material. The approach relied on the analysis of the transport distribution function, $\Sigma(\omega)$, which embodies the essential physics of both the electronic band structure and the energy-dependent scattering processes (via the electron lifetime). The key result is that the optimal thermoelectric performance is achieved when the energy trans-

port distribution is narrowly confined, ideally approximating a delta function. Two recent studies [18, 19] have applied this principle to engineer the density of states in binary compounds, thereby demonstrating an enhancement in their thermoelectric power. In this section, we reframe the original derivation using the Non-Equilibrium Green Function (NEGF) formalism. This approach proves to be a powerful and natural framework for understanding the microscopic mechanisms underlying the physical conditions—specifically, a very low Lorenz ratio and a high Seebeck coefficient—that result in a high figure of merit, $zT$.

### A. NEGFs approach
Transport in quantum systems is commonly described within the Landauer-Büttiker framework [6, 30, 31], in which currents are expressed in terms of transmission coefficients through the scattering region. While this picture is exact for non-interacting systems, a realistic description of thermoelectric performance requires careful treatment of the energy dependence of the transmission function, including broadening effects arising from hybridization with the leads and electron-electron scattering. A natural generalization that incorporates these effects is the Meir-Wingreen formalism [38], in which charge and heat currents are expressed as energy integrals over a transmission function that retains the full spectral structure of the interacting system. This framework provides the foundation for the transport calculations carried out in the present work.

The NEGF formalism, particularly within the linear-response regime, offers a first-principles approach to calculating energy dependent transmission functions. For a nano-scale or microscopic conductor coupled to two electrodes (reservoirs) at slightly different temperatures and electrochemical potentials, the charge current $(I_{\alpha})$ and the energy current $(J_{\alpha})$ can be derived from the Meir-Wingreen formula. The expressions are derived in Appendix A. In the steady state, the expression for these currents simplify significantly and are expressed as integrals over energy (or frequency $\omega = E/\hbar$) of the transmission function $\mathcal{T}(\omega)$. The latter is expressed as $\mathcal{T}(\omega) = \text{Tr}[\Gamma_L(\omega)G^R(\omega)\Gamma_R(\omega)G^A(\omega)]$ and it is the central quantity in NEGF approach of transport. It incorporates the electronic structure through the retarded $(G^R)$ and advanced $(G^A)$ Green functions of the scattering region and its coupling to the leads via the broadening matrices $(\Gamma_{L/R})$. This inherently includes the effect of the electronic band structure and, through the inclusion of many-body self-energies, can also account for inelastic scattering processes.

The starting point for thermoelectric analysis is the expression for the electrical current $(I_{\alpha})$ and the heat current $(\dot{Q}_{\alpha} = J_{\alpha} - \mu I_{\alpha}/e)$ flowing from the lead. Here, the chemical potential is $\mu = -eV_g$ and $V_g$ is the gate voltage which we set to be zero at the energy of the flat band of the noninteracting system. In the linear-response regime, where the applied voltage difference $\Delta V$ and temperature difference $\Delta T$ are small, these currents can be expanded as:

$$
\begin{pmatrix}
I_{\alpha} \\
\dot{Q}_{\alpha}
\end{pmatrix}
=
\begin{pmatrix}
L_{11} & L_{12} \\
L_{21} & L_{22}
\end{pmatrix}
\begin{pmatrix}
\Delta V \\
\Delta T
\end{pmatrix}
\tag{1}
$$

The above are also called the Onsager reciprocal relations. The Onsager coefficients $L^{ij}$ can be directly derived from the NEGF expression for the current A. By comparing these derived coefficients with those used in Ref. [36], we find a direct correspondence. The kinetic coefficients defined in Eqs. (2)-(4) of Ref. [36] are:

$$
L_{11} = e^2\mathcal{I}_0, \quad L_{22} = \frac{1}{T}\mathcal{I}_2
\tag{2}
$$

$$
L_{12} = \frac{e}{T}\mathcal{I}_1, \quad L_{21} = L_{12}T
\tag{3}
$$

where the integrals $\mathcal{I}_n$ are defined as:

$$
\mathcal{I}_n = \frac{1}{\hbar} \int_{-\infty}^{\infty} \frac{d\omega}{2\pi} \left(-\frac{\partial f}{\partial \omega}\right) \mathcal{T}(\omega)(\omega - \mu)^n
\tag{4}
$$

with $f(\omega) = [e^{\beta(\omega-\mu)} + 1]^{-1}$ being the Fermi-Dirac distribution function with $\beta \equiv (k_BT)^{-1}$. The electrical conductivity $\sigma$, the Seebeck coefficient $S$, and the electronic thermal conductivity $\kappa_e$ are then given by (see Appendix A):

$$
\sigma = e^2\mathcal{I}_0
\tag{5}
$$

$$
S = \frac{1}{eT} \frac{\mathcal{I}_1}{\mathcal{I}_0} = e \frac{\mathcal{I}_1}{\sigma T}
\tag{6}
$$

$$
\kappa_e = \frac{1}{T} \left(\mathcal{I}_2 - \frac{\mathcal{I}_1^2}{\mathcal{I}_0}\right)
\tag{7}
$$

These expressions [Eqs. (5)-(7)] are identical in form to those derived in Ref. [36]. The key equivalence is that the transport distribution function $\Sigma(\omega)$ in their work is replaced by $\mathcal{T}(\omega)/(2\pi\hbar)$.

### B. The Condition for Optimal Performance
The thermoelectric figure of merit, $zT$, which quantifies the thermoelectric performances can be rewritten as:

$$
zT = \frac{\sigma S^2T}{\kappa_e + \kappa_{ph}} = \frac{S^2}{L + L_{ph}}
\tag{8}
$$

where $\kappa_{ph}$ is the phonon thermal conductivity, $L = \kappa_e/(\sigma T)$ is the electronic Lorenz ratio, and $L_{ph} = \kappa_{ph}/(\sigma T)$. The search for the optimal shape of $\Sigma(\omega)$ yielding the highest possible $zT$ can be reformulated as a mathematical problem of finding the distribution function $P(\omega) = -\partial f/\partial\omega\Sigma(\omega)$ whose moments are the $I_n$ and such that the $zT$ in Eq. (8) is maximal. The solution to this variational problem is a Dirac delta function,

$\Sigma(\omega) \propto \delta(\omega - \mu - \epsilon_0)$, centered at an optimal energy $\epsilon_0$ away from the chemical potential $\mu$.

Our analysis, grounded in the NEGF expressions above, allows us to understand the physical rationale behind this mathematical result. The conditions derived in Ref. [36] for a high $zT$ correspond to a very low Lorenz ratio $L$ and a large Seebeck coefficient $S$ (respectively ($\xi \to 1$ and $A \to 0$ in Ref. [36]). Let us analyze the two main players which need to be tuned in order to achieve the highest possible $zT$.

Lorenz Ratio ($L$): The Lorenz ratio $L = \kappa_e/(\sigma T)$ is a measure of the electronic thermal conductivity relative to the electrical conductivity. Using the definitions above, we can write:

$$
L = \frac{1}{e^2 T^2} \left( \frac{\mathcal{I}_2}{\mathcal{I}_0} - \left( \frac{\mathcal{I}_1}{\mathcal{I}_0} \right)^2 \right) . \tag{9}
$$

By noticing that $\mathcal{I}_0$ is the normalization of the distribution $P(\omega)$, this expression is essentially the variance of the energy of the transmitted electrons. There are two distributions which satisfy this condition: i) the rectangular distribution; ii) the delta-function. The derivative of the Fermi-Dirac distribution is peaked around the chemical potential $\mu$ and has a width $\approx k_B T$. Therefore a delta-function distribution $P(\omega)$ is possible for a sharply peaked transmission function $\mathcal{T}(\omega) \propto \delta(\omega - \omega_0)$. In this case all transmitted electrons have exactly the same energy $\omega_0$. Consequently, the variance is zero, and we get $\mathcal{I}_2/\mathcal{I}_0 = (\mathcal{I}_1/\mathcal{I}_0)^2$, leading to $\kappa_e = 0$ and thus $L = 0$. This is the "best" possible scenario, as it completely decouples charge and heat transport electronically. In reality, a delta function is nonphysical, but a very sharp, narrow-band transmission function approximates this behavior, resulting in a very small $L$. At high temperatures where the Fermi window broadens significantly, a rectangular distribution would also lead to a low Lorenz factor.

Seebeck Coefficient ($S$): From Eq. (6), the Seebeck coefficient is proportional to the ratio between the average energy (relative to the chemical potential) of the transported electrons and the energy due to electrons with thermal energy $k_B T$. In the case of a rectangular distribution, centered around the chemical potential $\mu$, the integral $\mathcal{I}_1 \approx 0$, leading to a vanishing $S$. This is in general true for any distribution which is symmetric around $\mu$. Instead, $S$ is maximized when the transport is asymmetric around $\mu$. Being the Fermi window $(-\partial f/\partial \omega)$ symmetric around $\mu$, this occurs when $\mathcal{T}(\omega)$ is significant only on one side of $\mu$. A delta-function transmission located at an energy $\epsilon_0$ away from $\mu$ achieves this purpose. It ensures that all charge carriers have exactly the same energy, maximizing the $\mathcal{I}_1/\mathcal{I}_0$ ratio and, consequently, $S$.

Therefore, the condition for an exceptionally high $zT$ is to have a transport distribution (or transmission function) that is both extremely narrow (for a low $L$) and asymmetric (for a high $S$). The $zT$ then becomes $zT = S^2/L_{ph}$, where the denominator is now dominated by the unavoidable phonon thermal conductivity and which bounds it from above. A large $S$ can then compensate for a finite phononic contributions $L_{ph}$ and significantly enhance $zT$.

Our subsequent analysis of specific models, such as the sawtooth lattice and the diamond chain, directly applies this principle. While both models may exhibit a delta-like density of states from a flat band, it is the transmission function $\mathcal{T}(\omega)$ that dictates transport. In the diamond chain, the topology allows for a non-zero transmission at the flat-band energy, whereas in the sawtooth model, it may vanish. This highlights the crucial role of the quantum-mechanical transmission probability, accessible via NEGF, over the simple density of states in the quest for high-performance thermoelectrics. The transmission function, and not merely the density of states, is the true design parameter.

Motivated by the recent realization of one-dimensional (1D) [17] and quasi-1D [2, 59] flat-band we consider two well known 1D models. The simplest one is the sawtooth model, a one-dimensional lattice with a unit cell hosting two different sites (or orbitals) $a$ and $b$ coupled as shown in Fig.1 a). The second model we will consider is the so-called diamond model which in addition to a flat-band can host topological non-trivial phases. Its unit cell hosts three different sites (or orbitals) $a$, $b$ and $c$ which are coupled as in Fig.1 b). We notice that in both models the interaction is up to the "nearest-neighbor cell". We can write a general expression for the Hamiltonian which holds for both models as:

$$
\hat{H}_0 = \sum_{i=1,\sigma}^{N} \hat{\mathbf{c}}_{i\sigma}^{\dagger} \mathbf{h} \, \hat{\mathbf{c}}_{i\sigma} + \sum_{i=1,\sigma}^{N-1} \hat{\mathbf{c}}_{i+1\sigma}^{\dagger} \mathbf{T}\hat{\mathbf{c}}_{i\sigma} +\hat{\mathbf{c}}_{i\sigma}^{\dagger} \mathbf{T}^{\dagger}\hat{\mathbf{c}}_{i+1\sigma}, \tag{10}
$$

where $N$ is the number of cells. The two models are then obtained by properly choosing the intra-cell $\mathbf{h}$ and inter-cell $\mathbf{T}$ matrices and the vector operators $\hat{\mathbf{c}}_{i\sigma} \equiv \{\hat{c}_{i\alpha\sigma}\}$ and $\hat{\mathbf{c}}_{i\sigma}^{\dagger} \equiv \{\hat{c}_{i\alpha\sigma}^{\dagger}\}^{\mathrm{T}}$ with $\alpha$ running over the orbitals in the unit cell.

In what follows we work with periodic boundary conditions in order to avoid spurious effects coming from localized edge states which are in gap. To get rid of such effects in a recent work [42, 43] the authors introduced a local potential on one of the edge sites to push the localized state within the band of states. Since we do not look at topological properties, these states do not play any crucial role in the forthcoming discussion. Moreover in a realistic setup the contacts with the leads would destroy the boundary states because of the hybridization with the atoms of the lead itself. With this working assumption, it is possible to diagonalize [51] the Hamiltonian in Eq. (10) introducing the lattice momentum obtaining:

$$
\hat{H}_0 = \sum_{k=-N/2+1,\sigma}^{N/2} \tilde{\mathbf{c}}_{k\sigma}^{\dagger} \, \tilde{\mathbf{h}}(k) \, \tilde{\mathbf{c}}_{k\sigma}. \tag{11}
$$

where $\tilde{\mathbf{h}}(k) = \mathbf{h} + \exp(ik)\mathbf{T} + \exp(-ik)\mathbf{T}^{\dagger}$ and $\tilde{\mathbf{c}}_{k\sigma} =$

$$N^{-1/2} \sum_{j=1}^{N} \hat{\mathbf{c}}_{j \sigma} e^{-i k j}.$$

In the following we briefly discuss the salient features of the two models, highlighting those which will be used in the forthcoming discussions.

### C. The sawtooth model

The sawtooth model is the simplest one-dimensional model featuring a flat-band. It is defined by the matrices:

$$
\mathbf{h} = \begin{pmatrix}
\epsilon_a & t_{ab} \\
t_{ab} & \epsilon_b
\end{pmatrix}, \quad
\mathbf{T} = \begin{pmatrix}
t_{aa} & t_{ab} \\
0 & 0
\end{pmatrix}. \tag{12}
$$

The operators are $\hat{\mathbf{c}}_{i \sigma} \equiv \{\hat{c}_{i \alpha \sigma}\} \ \hat{\mathbf{c}}_{i \sigma}^{\dagger} \equiv \{\hat{c}_{i \alpha \sigma}^{\dagger}\}^{\mathrm{T}}$ with $\alpha = a, b$ being two orbitals per unit-cell.

A real system described by an Hamiltonian similar to the sawtooth, the zig-zag model, has recently been realized using Cu and Te atoms on Cu(111) as reported in Ref. [17]. There it has been shown that the chain of CuTe atoms induces a flat-band at about 1.5 eV below the Fermi energy. It has been shown that its presence induces a temperature dependent phase transition and induces a Luttinger liquid behavior.

For such a simple system it is possible to obtain analytic expressions for the dispersion relations of the two bands:

$$
\epsilon_{\pm}(k) = \frac{\epsilon_a + \epsilon_b}{2} + t_{aa} \cos(k) \pm \frac{1}{2} \sqrt{\Delta(k)}, \tag{13}
$$

where $\Delta(k) = (\epsilon_a - \epsilon_b + 2t_{aa} \cos(k))^2 + 8t_{ab}^2(1 + \cos(k))$ and $k = 2m\pi/N$ with $m \in (-N/2, N/2]$.

As shown in Fig. 1 a), the spectrum has a gap $E_g = \epsilon_+(\pi) - \epsilon_-(\pi) = |\epsilon_a - \epsilon_b - 2t_{aa}|$ which closes for $\epsilon_a - \epsilon_b = 2t_{aa}$. To guarantee the existence of a flat-band, it is sufficient to impose $\Delta(k) = 4(C + t_{aa} \cos(k))^2$, with $C$ a constant to be determined. After some simple algebra, the condition for the existence of the flat-band reads

$$
t_{ab} = \pm \sqrt{2t_{aa}^2 + (\epsilon_a - \epsilon_b)t_{aa}}. \tag{14}
$$

In the case of homogeneous on-site potentials $\epsilon_a = \epsilon_b$ this condition simplifies to $t_{ab} = \sqrt{2}t_{aa}$. For our purposes it is important to notice that when a perfect flat band is present the system has always a gap. In other words in the sawtooth model the flat-band, when present, is always isolated from the dispersive band. Moreover Eq. (13) shows that the appearance of a flat-band is rather fragile with respect to the variation of the parameters of the Hamiltonian. The flat-band becomes dispersive as soon as Eq. (14) is not satisfied. What is more important is that the number of states in the flat-band is an extensive quantity, and grows with the number of unit cells, namely the flat-band is a highly degenerate manifold of the system.

![](./images/1252926931859406858_2.jpg)

Figure 2. (Color online). Interaction-induced renormalization of the narrow-band bandwidth $\Delta W_n$ as a function of the gate potential $V_g$, computed at the Hartree-Fock level for an interaction strength $U = 0.15$ eV, for panel a) the sawtooth chain and panel b) the diamond chain. Each curve corresponds to a different value of the bare lead bandwidth $W_0$ (in meV), ranging from the wider bands (blue) to the narrower bands (dark red), as indicated in the legend. The insets show the corresponding GW results for two representative values of $W_0$.

### D. The diamond chain

The second model we consider is the diamond chain characterized by the matrices:

$$
\mathbf{h} = \begin{pmatrix}
\epsilon_a & t & 0 \\
t & \epsilon_b & t \\
0 & t & \epsilon_c
\end{pmatrix}, \quad
\mathbf{T} = \begin{pmatrix}
t' & t & 0 \\
0 & 0 & t \\
0 & 0 & t'
\end{pmatrix}. \tag{15}
$$

The operators are $\hat{\mathbf{c}}_{i \sigma} \equiv \{\hat{c}_{i \alpha \sigma}\}$ and $\hat{\mathbf{c}}_{i \sigma}^{\dagger} \equiv \{\hat{c}_{i \alpha \sigma}\}^{\dagger}$ with $\alpha = a, b, c$ being the site (orbital) labels.

When the local energies $\epsilon_\alpha$ are all the same, the diamond chain features a flat-band either for $t' = 0$ or for $t' = t$ [27]. As illustrated in Fig. 1 b) , the two cases differ in two main aspects, both important for our purposes. The flat-band at $t' = 0$ is at zero energy and three bands touch at the edge of the Brillouin zone: the system is gapless. At $t = t'$ the flat-band is the lowest (or highest depending on the sign of $t$) energy band with the other two bands having a semi-metallic character. Most importantly there is no energy gap separating the flat-band and the middle energy band in the case $\epsilon_a = \epsilon_b = \epsilon_c$ and $t = t'$. This is the ideal scenario to study how transport properties of the system are modified by the coupling of the flat-band to other bands. In the following we will consider the approach to the flat-band by tuning the local energies of orbitals $a$ and $c$, namely $\epsilon_a = -\epsilon_c = \epsilon \to 0$

![](./images/1252926931859406858_3.jpg)

Figure 3. (Color online). Interaction-induced renormalization of the energy gap $\Delta E_g$ between the narrow-band and the dispersive band in the diamond chain, as a function of the gate potential $V_g$, computed at the Hartree-Fock level for $\Gamma=50$ meV, as illustrated in the inset. Each curve corresponds to a different bandwidth $W_0$, ranging from wider (blue) to narrower (dark red) as in Fig. 2. The renormalization is largest near half-filling of the narrow-band ($V_g\approx0.0$ eV).

## E. Interaction and contacts

States in the flat-band do not contribute to transport directly; yet when they are coupled to dispersive states of the spectrum the system conduction is restored [18, 19]. This coupling can be provided by external fields (photoexcitation), electron-electron or electron-phonon scattering or by the contact with metallic leads in the case of transport setups. Here we examine the role of electron-electron scattering and the contact to external leads. The latter ones are modeled as non-interacting electrons with a given dispersion relation at equilibrium and characterized by a chemical potential and a temperature. For the many-body interaction we consider a Hubbard like interaction. This is partly motivated by the original works which introduced the Hubbard model itself [23, 24] to describe localized electrons in $d-$ and $f-$ orbitals. Nevertheless here we are considering the case in which the many-body interaction is not the leading term in the total energy as in the case of the Hubbard model. In this situation, the flatbands emerge due to geometrical arrangements of the Hamiltonian rather than from strong interactions favoring the occupation of a degenerate manifold of atomic like orbitals.

The total Hamiltonian reads:

$$
\hat{H}=\hat{H}_{M}+\hat{H}_{ee}+\sum_{l=L,R}\hat{H}_{l}+\hat{V}_{l} \tag{16}
$$

$$
\hat{H}_{ee}=U\sum_{\substack{i=1\\\alpha}}^{N}\hat{c}_{i\alpha\uparrow}^{\dagger}\hat{c}_{i\alpha\downarrow}^{\dagger}\hat{c}_{i\alpha\downarrow}\hat{c}_{i\alpha\uparrow} \tag{17}
$$

$$
\hat{H}_{l}=\sum_{k,\sigma=\uparrow\downarrow}\epsilon_{l,k}\hat{d}_{l,k\sigma}^{\dagger}\hat{d}_{l,k\sigma} \tag{18}
$$

$$
\hat{V}_{l}=\sum_{\substack{i=1,k\\\sigma=\uparrow\downarrow}}\left[T_{i\alpha k}^{(l)}\hat{c}_{i\alpha\sigma}^{\dagger}\hat{d}_{l,k\sigma}+T_{i\alpha k}^{(l)*}\hat{d}_{l,k\sigma}^{\dagger}\hat{c}_{i\alpha\sigma}\right], \tag{19}
$$

where $\hat{d}_{l,k\sigma},\hat{d}_{l,k\sigma}^{\dagger}$ are the annihilation and creation operators for the $k-$state of an electron in the lead $l$. Here the coefficients $T_{i\alpha k}^{(l)}$ are the overlap integrals between the $k-$state of the lead $l$ and the site (orbital) $\alpha$ in the unit cell $i$.

We resort to the non-equilibrium Green functions approach to compute the physical quantity of interest. We give a brief overview of the formalism in Appendix A with particular emphasis on the calculation of the quantities useful for the our purposes. We mention here that in the NEGFs formalism the coupling to the leads is accounted for in non-perturbative manner, provided one knows the density of states of the leads and the overlap integrals $T_{i\alpha k}^{(l)}$. This is done via the lead-induced hybridization self-energies, which we evaluate in the wide-band limit, where the electrode density of states is assumed to be featureless around the Fermi energy. This approximation is commonly justified for metallic contacts such as gold, whose electronic structure varies only weakly on the energy scales relevant for transport [9, 57, 58].

On the other hand electron-electron interactions are described via a chosen approximation scheme. In this work we consider two different cases: the mean-field (Hartree) approximation and the self-consistent GW approximation, which accounts for dynamical screening of the interaction through polarization processes beyond the single-insertion level. The GW approximation captures important correlation effects in both molecular and extended systems, while providing a reasonable description of spectral properties in many cases [20]. In the case of a short range many-body interaction, such as the one considered in this work, the GW approximation results in an effective long range correlation built up on the single particle coherences.

## F. Band flattening

In Refs. [7, 10, 32, 60] it has been shown that interactions can favor band flattening, a mechanism ascribed to the Hartree potential generated by electrons added to the system upon changing its filling. To reproduce this scenario we couple our system to an additional lead acting as a gate, which controls the total number of particles

### F Band flattening

by fixing the chemical potential at $\mu_G = e\ V_g$. At stationarity, no electrical or energy current flows through the system; instead, the system reaches equilibrium at a filling determined by the gate voltage. This corresponds to the system being in contact with a metallic Fermi sea.

We focus on the evolution of the lowest energy band as the system is progressively filled, and in particular on its bandwidth. In the non-interacting case we denote by $W_n^0$ the bandwidth of the narrowest band, where the subscript $n$ stands for "narrow". In the interacting case the problem is in general not reducible to a single-particle one; nevertheless, a single-particle spectrum can still be defined through the mean-field Hamiltonian. The latter contains only the Hartree term, and has the same structure as Eq. (11) with the replacement $\epsilon_\alpha \to \epsilon_\alpha + U n_{i\alpha}$ in the diagonal elements of $\mathbf{h}$, where $n_{i\alpha} = \int d\omega/(2\pi)\ G_{(i,\alpha,\uparrow)(i,\alpha,\uparrow)}^{<}(\omega)$ is the occupation at site $i$ and orbital $\alpha$, independent of spin due to spin symmetry (see Appendix A). To quantify the interaction-induced flattening we study the bandwidth change $\Delta W_n$, with $\Delta W_n = W_n - W_n^0$, as a function of the gate chemical potential and for different values of the bare non-interacting bandwidth $W_n^0$. The latter in the case of the sawtooth model is given by $W_n^0 = \epsilon_+(\pi) - \epsilon_-(\pi)$ and it is defined similarly for the mean-field Hamiltonian. The bandwidth $W_n$ of the interacting system is computed from the mean-field Hamiltonian of the contacted system. The results are shown in Fig. 2 for both models with $N=24$ and for $U=0.15$ eV, $T\approx 80$ K, lead coupling $\Gamma=50$ meV, and gate coupling $\Gamma_g=1$ meV.

For both the sawtooth and diamond chains, the narrowband of the interacting system becomes flatter than its non-interacting counterpart over a wide range of gate voltages, indicating that the flattening mechanism does not depend on whether the narrowband is isolated from the rest of the spectrum. The effect is most pronounced for intermediate values of $W_n^0$, as shown by the curves ranging from wide-band (blue) to narrow-band (dark red) limits in Fig. 2. A closer inspection reveals an important exception: when the non-interacting bandwidth is already very small, the band instead becomes more dispersive upon interaction. In this limit the system's occupation changes abruptly as the gate voltage is swept across the narrow-band, and the Hartree potential acts to broaden rather than flatten the band.

This behavior can be traced back to the structure of the non-interacting eigenstates. In the sawtooth model, the lowest-energy eigenstates have higher amplitude on the sites with lower local chemical potential $\epsilon_b$, and are therefore filled first as the gate voltage is increased. The resulting increase in local occupation raises the on-site energy via the Hartree potential, effectively softening the condition for flatband formation in Eq. (14). Upon further filling, eigenstates with higher amplitude on the "A" orbitals begin to be populated, leading, again through the repulsive interaction, to a violation of the flatband condition and a subsequent increase in dispersion. An analogous picture holds for the diamond chain, although in that case a simple argument based on on-site energies alone does not apply, since $\epsilon_c > \epsilon_b > \epsilon_a$ and yet the lowest-energy states have higher amplitude on orbitals "A" and "C".

The band flattening is a predominantly mean-field effect. As shown in the insets of Fig. 2 for two representative values of $W_n^0$, going beyond mean field to the GW level does not qualitatively alter the picture but leads to quantitative corrections, particularly near half-filling where correlation effects are strongest. It is also worth noting that any observed flattening remains small compared to the non-interacting bandwidth $W_n^0$, while the transition to a more dispersive regime can produce bandwidth increases that significantly exceed the non-interacting value. Finally, regarding the gap between the narrow-band and the dispersive band in the diamond chain we computed the difference $\Delta E_g = E_g - E_g^0$ between the gap of the interacting system $E_g$ and the gap of the non-interacting one $E_g^0$. Fig. 3 shows that interactions drive a purely correlation-induced closing of a gap between the two bands, which is largest near half-filling and is suppressed as $W_n^0$ increases, consistent with the picture that the effect weakens as the flat-band becomes less isolated from the dispersive background.

---

### III. HIGH THERMOELECTRIC POWER IN NARROW-BAND SYSTEMS

#### A. Electric and thermal conductivities

Before discussing the thermoelectric properties, we examine the electrical and thermal conductivities and compare them with the expectations from the non-interacting case. Within linear response theory, the electrical conductivity is expected to vanish in the flatband limit. This behavior results from the complete suppression of kinetic energy despite the presence of a formally divergent density of states: although infinitely many states are available, none of them contribute to transport. This conclusion, however, holds strictly only when the flatband is isolated from other energy bands.

Fig. 4 shows the electrical conductivity in units of $G_0\Gamma^{-1}$, where $G_0=2e^2/h$ is the conductance quantum, as a function of the gate potential $V_g$, computed at the Hartree-Fock level for $U=0.15$ eV and $T=80$ K, for two values of the lead broadening $\Gamma=5$ meV and $\Gamma=50$ meV and for both the sawtooth (panels a, b) and diamond (panels c, d) chains. Each curve corresponds to a different value of the bare non-interacting bandwidth $W_n^0$, ranging from the wide-band (blue) to the narrow-band (dark red) limit. In all panels the conductivity is suppressed as $W_n^0$ is reduced, reflecting the progressive localization of carriers as the flatband becomes more isolated. The sawtooth chain displays a single broad peak associated with transport through the dispersive band, which narrows and shifts toward lower gate voltages with decreasing $W_n^0$. The diamond chain shows a richer two-

![](./images/1252926931859406858_4.jpg)

Figure 4. (Color online). Electrical conductivity $\sigma$ in units of $G_0\Gamma^{-1}$ as a function of the gate potential $V_g$, computed at the Hartree-Fock level for interaction strength $U=0.15$ eV, temperature $T=80$ K, and two values of the lead broadening $\Gamma=5$ meV (left panels) and $\Gamma=50$ meV (right panels), for the sawtooth chain (panels a), b)) and the diamond chain (panels c), d)). Each curve corresponds to a different value of the bare non-interacting bandwidth $W_n^0$, ranging from the wide-band limit (blue) to the narrow-band limit (dark red), with the same values as in Fig. 2. The insets show the corresponding GW results for two representative values of$W_n^0$, demonstrating that correlations beyond mean field primarily renormalize the flatband-associated feature while leaving the dispersive contribution qualitatively unchanged.

peak structure, with a broad feature from the dispersive band and a sharp, narrower peak associated with transport through the flatband, whose weight and position depend sensitively on both $W_n^0$ and $\Gamma$.

The behavior in the flatband limit depends critically on both the coupling strength and the band topology, as made explicit in Fig. 5, which shows the peak conductivity $\sigma_M$ as a function of $W_0$ for both models. At small coupling ($\Gamma=5$ meV), both models recover the non-interacting expectation: $\sigma_M$ increases monotonically with $W_0$ and vanishes as $W_0\rightarrow0$, consistent with the progressive suppression of transport as the flatband becomes more isolated. At larger coupling ($\Gamma=50$ meV) the two models diverge qualitatively. In the sawtooth chain $\sigma_M$ continues to vanish in the flatband limit, a direct consequence of the large gap $\Delta E_g\approx2$ eV separating the narrowband from the dispersive band, which prevents any hybridization-driven restoration of transport regardless of the coupling strength. In the diamond chain, by contrast, $\sigma_M$ saturates to a finite value as $W_0\rightarrow0$, demonstrating that the gapless touching between the flatband and the dispersive band enables a residual transport channel that persists even when the bandwidth is fully quenched.

![](./images/1252926931859406858_5.jpg)

Figure 5. (Color online). Maximum electrical conductivity $\sigma_M$ in units of $G_0\Gamma^{-1}$ as a function of the bare non-interacting bandwidth $W_0$, computed at the Hartree-Fock level for $U=0.15$ eV and $T=80$ K, for the sawtooth (gray triangles) and diamond (cyan diamonds) chains, and for two values of the lead broadening $\Gamma=5$ meV (panel a) and $\Gamma=50$ meV (panel b)).

This observation leads to an important conclusion: transport through a flatband is restored when the latter is energetically adjacent to a dispersive band and a coupling mechanism between the two exists. This is precisely the energy filtering mechanism invoked in Refs. [18, 19] to enhance thermoelectric performance through the energy selectivity of a narrowband embedded in a dispersive background. In the present case the coupling is provided by hybridization with the leads, but an entirely analogous role can be played by electron-electron interactions. When correlation effects are incorporated at the GW level, shown in the insets of Fig. 4 for two representative values of $W_n^0$, the conductance peak associated with the narrow-band persists in the diamond chain while it is suppressed in the sawtooth model, confirming that the restoration of transport is governed by the band topology rather than by the details of the interaction, and is controlled by the presence or absence of a gap between the flat-band and the dispersive background.

The thermal conductivity displays an analogous behavior to the electrical one, as shown in panels a) and c) of Fig. 6 where we report $\kappa_e$ in units of the quantum of thermal conductance $g_0=\pi^2k_B^2T(3h)^{-1}$. In the sawtooth chain, $\kappa_e$ is progressively suppressed as $W_n^0$ is reduced and vanishes in the flatband limit, mirroring the behavior of electrical conductivity $\sigma$. In the diamond chain, by contrast, $\kappa_e$ retains a finite value even as $W_n^0\rightarrow0$,

![](./images/1252926931859406858_6.jpg)

Figure 6. (Color online). Electronic thermal conductivity $\kappa_e$ in units of $g_0$ (panels a), c)) and Lorenz ratio $L/L_0$ normalized to the Sommerfeld value $L_0$ (panels b), d)) for the sawtooth (top panels) and diamond (bottom panels) chains, computed at the Hartree-Fock level for $\Gamma = 50$ meV, $U = 0.15$ eV and $T = 80$ K. Each curve corresponds to a different value of the bare non-interacting bandwidth $W_n^0$, ranging from the wide-band (blue) to the narrow-band (dark red) limit, with the same values as in Fig. 2.

consistent with the restoration of transport through the gapless touching between the flatband and the dispersive band. In both models the thermal conductivity develops a two-peak structure in the diamond chain that directly reflects the two transport channels identified in the electrical conductivity, while the sawtooth chain shows a single broad peak that narrows and is suppressed with decreasing $W_n^0$.

### B. Violation of the WF law

Of particular interest is the violation of the Wiedemann-Franz (WF) law when the chemical potential falls within the narrow-band region. The WF law states that the ratio of the electronic thermal conductivity to the electrical conductivity is proportional to temperature, $\kappa/\sigma = L_0 T$, through a proportionality constant that is largely universal across materials. This constant, the Lorenz number, takes the value $L_0 = \pi^2/3 (k_B/e)^2$, which in natural units ($k_B = 1$, $e = 1$) gives $L_0 \approx 3.29$. Physically, the WF law quantifies the heat carried by charge carriers, and deviations from it have been reported in a variety of systems [13, 28, 37]. Although the microscopic origin of such violations is system-dependent, a breakdown of the WF law generically signals a decoupling between heat and charge currents.

A common extension of the WF law takes the form $\kappa/\sigma = L T$, where $L$ is the more general Lorenz number discussed in Sec. II. The ratio $\eta = L/L_0$ then provides a quantitative measure of the WF law violation. Since the WF law is typically derived within the free-electron model for metals, values of $\eta < 1$ (or $\eta > 1$) indicate that the conducting electrons carry less (or more) energy than their kinetic energy alone would predict.

In quantum systems where discrete energy levels can be individually resolved, such as quantum dots, violations of the WF law are ubiquitous [13, 25, 28, 37]. Consistently, WF law violations are found even in the non-interacting limit at low temperatures, an effect that weakens progressively as temperature rises. This can be understood intuitively: at very low temperatures, transport is dominated by electrons drawn from the leads at a well-defined energy, which disrupts the conventional relationship between electrical current and the energy transported by those electrons.

Panels b) and d) of Fig. 6 display $L/L_0$, as a function of the gate potential $V_g$, with the dashed horizontal line marking $L/L_0 = 1$. Here, the calculations are done at the Hartree-Fock level. In the sawtooth chain, panel b), $L/L_0$ remains systematically below 1 across the entire gate voltage range, with the suppression becoming more pronounced as $W_n^0$ is reduced. This plateau-like behavior over a finite gate voltage window is a direct consequence of the energy-filtering mechanism associated with the isolated flat-band, which suppresses energy fluctuations of the transmitted electrons. In the diamond chain, panel d), the behavior is richer and non-monotonic: $L/L_0$ exceeds 1 in the vicinity of the flat-band, where the dispersive and flat-band transport channels contribute differently to heat and charge transport, before dropping sharply as the gate voltage crosses the flat-band. This resembles the filling dependence observed in a single-level quantum dot, with the minimum satisfying $L < L_0$ near half-filling [13], but the proximity of the dispersive band quickly restores transport and amplifies energy fluctuations, driving $L/L_0$ back above unity.

However, neither of these signatures constitutes a physically meaningful departure from the Wiedemann-Franz law in the strict flatband limit. In the sawtooth chain, the suppression of $L/L_0$ simply reflects the fact that both $\kappa_e$ and $\sigma$ vanish simultaneously as $W_n^0 \to 0$, with $\kappa_e$ vanishing faster, a ratio of two quantities both going to zero carries no useful thermodynamic information. In the diamond chain, the non-monotonic behavior of $L/L_0$ is a consequence of the interplay between the two transport channels rather than a sign of genuine heat-charge decoupling. We have checked (not shown) that including many-body interactions at the GW level does not alter this picture qualitatively, though it does introduce quantitative corrections. Taken together, these observations suggest that while an isolated flatband appears to yield a more favorable Lorenz ratio, this advantage is fictitious: it does not translate into enhanced thermoelectric performance, as we now demonstrate through the analysis of the figure of merit $zT$ in the following

![](./images/1252926931859406858_7.jpg)

Figure 7. (Color online). Seebeck coefficient $S$ in units of mV/K as a function of the gate potential $V_g$, computed at the Hartree-Fock level for $U = 0.15$ eV in the region below half-filling of the narrowband, for the sawtooth chain (top panels, $W_n^0 = 6.67$ meV) and the diamond chain (bottom panels, $W_n^0 = 5.0$ meV), and for lead broadenings $\Gamma = 5$ meV (left column) and $\Gamma = 50$ meV (right column). Each curve corresponds to a different temperature ranging from $T = 35$ K (dark purple) to $T = 290$ K (dark red), as indicated in the legend.

section.

## C. Seebeck coefficient

The ability to convert temperature gradients into electric potential differences is quantified by the Seebeck coefficient. According to Eq. (6), a highly asymmetric transmission function around the chemical potential of the leads is sufficient to ensure a large Seebeck coefficient. This asymmetry typically arises from particle-hole asymmetry in the density of states, but can also be engineered through the coupling to the leads. In the case of flat-bands, the asymmetry originates from the sharpness of the density of states, which selects electrons from the leads at specific energies. A useful interpretation of Eq. (6) is that the Seebeck coefficient measures the ratio between the average energy transported by electrons through the system $\mathcal{I}_1$ and the thermal energy of the electrons in the leads $T\sigma$. For a broad transmission function, as in metals, electrons transport on average exactly the thermal energy of the hottest lead, resulting in a small Seebeck coefficient. The sharpness of the flatband-induced transmission peak breaks this averaging and is the key mechanism behind the large values of $S$ reported below.

Fig. 7 shows the Seebeck coefficient for the sawtooth chain, panels a) and b), and the diamond chain, panels c) and d), as a function of the gate potential $V_g$, for lead-system couplings $\Gamma = 5$ meV (left column) and $\Gamma = 50$ meV (right column), and for temperatures ranging from $T = 35$ K to $T = 290$ K. In all panels $S$ is negative throughout the explored gate range, consistent with electron-dominated transport below half-filling of the narrow-band. The overall magnitude of $S$ reaches values of order 1–2 mV/K, which are exceptionally large compared to both conventional metallic systems and the best known thermoelectric materials [18, 19], and directly reflect the sharpness of the narrow-band-induced peak in the transmission function.

In the weak-coupling regime ($\Gamma = 5$ meV), panels a) and c), $S$ develops a pronounced negative peak whose position shifts toward more negative gate voltages and whose magnitude grows with decreasing temperature, reflecting the increasingly sharp energy filtering provided by the flat-band edge at low $T$. The sharp vertical drop visible in each curve marks the gate voltage at which the chemical potential enters the flat-band, where the electrical conductivity is suppressed and $S$ diverges before becoming ill-defined. As temperature increases, the sharp feature is thermally smeared: the peak broadens and its magnitude is reduced, as the wider thermal window averages over a larger energy range of the transmission function, partially canceling the asymmetric contributions from either side of the narrowband peak. This temperature dependence is a direct manifestation of the competition between the energy selectivity of the narrow-band and the thermal broadening of the Fermi distribution.

In the strong-coupling regime ($\Gamma = 50$ meV), panels b) and d), the flatband peak in the transmission function is broadened by hybridization with the leads. As a consequence, the sharp dip in $S$ is significantly reduced in depth and the overall gate-voltage dependence becomes smoother. Nevertheless, sizable absolute values of $S$ persist even at large coupling, indicating that the narrowband still provides a substantial asymmetry in the transmission function even when hybridization is non-negligible. Comparing the two models, the sawtooth and diamond chains show qualitatively similar behavior, though the diamond chain displays a more symmetric gate-voltage profile around the narrowband energy, reflecting differences in the underlying band structure and the particle-hole symmetry properties of the two lattices.

We have demonstrated that flatbands are a powerful resource for thermoelectric energy conversion: the sharply peaked density of states associated with the flat-band generates a strongly asymmetric transmission function, which is the key ingredient for a large Seebeck coefficient. The enhancement is most pronounced at low temperatures and weak coupling, where the energy selectivity of the flatband is least spoiled by thermal or hybridization broadening. Again, we have checked that

![](./images/1252926931859406858_8.jpg)

Figure 8. (Color online). Thermoelectric figure of merit $zT$ as a function of the gate potential $V_g$ in the region below half-filling of the narrowband, computed for the diamond chain ($W_n^0 = 5.0$ meV) for temperatures ranging from $T = 35$ K (blue) to $T = 290$ K (dark red), at the Hartree-Fock level (panels a) and b)) and at the GW level (panels c) and d)), for lead broadenings $\Gamma = 5$ meV (left column) and $\Gamma = 50$ meV (right column). The phonon thermal conductivity has been set to $\kappa_{ph} = 10^{-3}g_0T$ W/K, where $g_0T = \pi^2k_B^2T/3h$ is the quantum of thermal conductance. As discussed in the text, this value is negligible compared to the electronic thermal conductivity in the wide-bandwidth regime, but becomes comparable to $\kappa_e$ as the flatband limit is approached, so that the values of $zT$ shown here represent an upper bound only for the largest bandwidths.

treating many-body interactions at the GW level does not alter this picture qualitatively, but introduces moderate quantitative corrections to the values of $S$. We present a comparative simulation of HF and GW in the case of the thermoelectric figure of merit analyzed next.

### D. Thermoelectric figure of merit $zT$

Both the Lorenz ratio and the Seebeck coefficient suggest that an isolated flatband outperforms a flatband embedded in a dispersive background. This stands in apparent tension with the picture put forward in [18, 19], where thermoelectric enhancement is attributed to the restoration of flatband transport via scattering into a dispersive band. However, a full restoration of transport would necessarily suppress the Seebeck coefficient, driving the material toward conventional metallic behavior — which is precisely the opposite of what is desired.

A crucial caveat must be kept in mind here. Although the sawtooth model yields a large thermovoltage, its electrical conductivity vanishes, as shown in Fig. 5. A large Seebeck coefficient under these conditions does not translate into useful thermoelectric performance. The same reasoning applies to the Lorenz ratio: its anomalously low value does not reflect a genuinely favorable departure from the Wiedemann-Franz law, but rather the fact that the thermal conductivity vanishes even faster than the electrical conductivity. The apparent violation of the Wiedemann-Franz law is therefore physically meaningless in this limit. To make this concrete, we now turn to the thermoelectric figure of merit, $zT$, as defined in Eq. (8), which simultaneously accounts for all three transport coefficients and provides an unambiguous measure of thermoelectric performance.

Fig. 8 shows $zT$ as a function of the gate potential $V_g$ in the region below half-filling of the narrowband, for temperatures ranging from 35 K (blue) to 290 K (dark red), computed with $\kappa_{ph} = 10^{-3}g_0$ W/K, where $g_0 = \pi^2k_B^2T/3h$ is the quantum of thermal conductance. As can be seen from Fig. 6, this is not universally negligible: while $\kappa_{ph}$ is small compared to the electronic thermal conductivity at large $W_n^0$, it becomes comparable to or larger than $\kappa_e$ as the flatband limit is approached and the electronic conductivity is suppressed. The values of $zT$ shown in Fig. 8 therefore represent a true upper bound only in the wide-bandwidth regime, while in the narrow-bandwidth limit the phonon contribution already plays a non-trivial role in limiting thermoelectric performance. This is the case for the chosen $W_n^0$ for both models. A more systematic treatment of the phononic thermal conductivity goes beyond the scope of our work and requires a proper definition of the physical system; the values we consider here illustrate the role of $\kappa_{ph}$ in determining the upper bound for $zT$. All four panels display a pronounced peak near $V_g \approx -0.15$ eV, which corresponds to the chemical potential being tuned to the vicinity of the flatband edge where the Seebeck coefficient is largest. It is important to note that the narrowband itself is located in the energy window $-0.08$ eV $\lesssim V_g \lesssim -0.02$ eV within the gate range explored here. The peak in $zT$ therefore does not occur when the chemical potential sits inside the narrowband, but rather just below it, in the energy region where the density of states varies most rapidly with energy. This is fully consistent with the Mahan-Sofo picture [36]: the optimal thermoelectric response is achieved not at the center of a sharp spectral feature, but at its lower edge, where the energy derivative of the transmission function is maximized and the Seebeck coefficient consequently peaks. As the gate potential is swept through the narrowband region, $zT$ drops sharply: once the chemical potential enters the flatband, conductivity is suppressed and the system enters the paradoxical regime discussed above, where a large thermovoltage coexists with vanishing carrier mobility.

At the Hartree-Fock level, panels a) and b), the peak values of $zT$ are remarkably large for both values of the lead broadening, with the larger $\Gamma = 50$ meV yielding superior performance consistent with our earlier conclu-

sion that a finite hybridization with the dispersive back-
ground is necessary to restore carrier mobility without
fully suppressing the Seebeck coefficient. The $zT$ peak
grows and sharpens with increasing temperature, reflect-
ing the growing importance of thermally activated trans-
port across the flatband edge. At the GW level, pan-
els c) and d), correlation effects beyond mean field sub-
stantially reduce the peak values of $zT$, indicating a sig-
nificant renormalization of the thermoelectric response
through a redistribution of spectral weight and an en-
hancement of effective scattering rates. Notably, the
secondary sharp feature visible near $V_g \approx -0.05$ eV in
panels a) and c) at low temperatures and small broad-
ening can be directly associated with transport through
the narrowband itself: its suppression at larger $\Gamma$ and
higher $T$ confirms that it originates from fine structure in
the transmission function tied to the flatband density of
states, which is progressively smeared out by interaction-
induced, hybridization and thermal broadening.

## IV. CONCLUSIONS

In this work we have investigated the thermoelectric
properties of interacting electrons in flatband systems,
using two paradigmatic one-dimensional models, the saw-
tooth chain and the diamond chain, as representative
cases of an isolated flatband and a gapless flatband touch-
ing a dispersive band, respectively. The two models were
treated within a non-equilibrium Green function frame-
work in which electron-electron interactions are included
diagrammatically at the Hartree-Fock and GW levels of
approximation, allowing us to access interaction-driven
renormalizations of both the spectral function and the
transport coefficients self-consistently and beyond the
mean-field description.

A central result of this work is that the naive expec-
tation, that a perfectly flat band should be an optimal
thermoelectric, is physically flawed. Although the See-
beck coefficient is large and the Lorenz ratio anomalously
suppressed in the strict flat-band limit, these signatures
alone are meaningless: the electrical conductivity van-
ishes as the chemical potential enters the flat-band, so
that a large thermovoltage is generated but no current
can flow, and the apparent violation of the Wiedemann-
Franz law simply reflects the fact that thermal conduc-
tivity vanishes faster than electrical conductivity. This
connects directly to the result of Mahan and Sofo [36]:
a delta-function transmission is mathematically optimal
but physically unreachable, since a perfectly flat-band
implies fully quenched kinetic energy and a vanishing
transmission function. Some finite broadening, whether
from hybridization with dispersive bands introduced by
the leads or from scattering into nearby dispersive states,
is not a perturbation to be minimized but a necessary
condition for useful thermoelectric performance. This
clarifies the apparent disagreement with the scenario pro-
posed in [18, 19]: a partial restoration of flat-band trans-
port is beneficial, but a full restoration suppresses the
Seebeck coefficient and drives the system toward conven-
tional metallic behavior.

The thermoelectric figure of merit, $zT$, confirms this
picture: its peak occurs just below the flat-band edge,
where the transmission function varies most rapidly with
energy, rather than inside the flat-band itself. The sys-
tematic comparison between HF and GW results reveals
that mean-field treatments generally overestimate ther-
moelectric performance, and that a proper account of
electronic correlations is necessary for reliable predic-
tions. These findings provide a coherent and physi-
cally transparent set of design principles for flatband-
based thermoelectric devices, and a powerful framework
for their theoretical description using the NEGFs ap-
proach. Natural extensions include two-dimensional flat-
band materials such as twisted moiré systems, kagome
metals, and other strongly correlated platforms where
both interaction effects and thermoelectric functionality
are of active experimental interest.

## ACKNOWLEDGMENTS

Numerical simulations were performed exploiting the
Finnish CSC facilities under the Project no. 2009128
("Transport in flatband materials"). R.T. acknowledges
the financial support of the Jane and Aatos Erkko Foun-
dation (Project EffQSim) and the Research Council of
Finland through the Finnish Quantum Flagship (Project
No. 359240).

## Appendix A: Physical quantities within the NEGFs approach

To compute the physical quantities of interest we
use the non-equilibrium Green functions (NEGFs) [44]
approach, which allows us to treat the leads non-
perturbatively and the many-body interaction through
perturbation theory. For this reason, NEGFs are partic-
ularly suitable for studying transport [44, 53, 54] in cor-
related systems. Moreover in the case of non-interacting
systems the quantities of interests such as currents and
conductivities are exact unlike in other approaches which
use linear response which is basically a perturbation ap-
proach in the coupling strengths to the leads.

We study the non-equilibrium steady state and specif-
ically the electric current and the conductivity. We solve
the Dyson equation in the frequency domain which reads:

$$
G^{R}(\omega)=g^{R}(\omega)+g^{R}(\omega) \Sigma^{R}(\omega) G^{R}(\omega) \tag{A1}
$$

$$
G^{<}(\omega)=G^{R}(\omega) \Sigma^{<}(\omega) G^{A}(\omega) \tag{A2}
$$

$$
\Sigma^{\mathrm{X}}(\omega)=\Sigma_{\mathrm{HY}}^{\mathrm{X}}(\omega)+\Sigma_{\mathrm{MB}}^{\mathrm{X}}(\omega) \tag{A3}
$$

where $g$ is the reference Green function, which we take
as the Hartree-Fock one. Above, $\mathrm{X}=<, R, A$ and the

$G^{\mathrm{X}}(\omega)$ are the Fourier transforms of the corresponding single particle Green functions:

$$
g_{\mathbf{x} \mathbf{x}^{\prime}}^{R}\left(t-t^{\prime}\right)=-\mathrm{i} \theta\left(t-t^{\prime}\right)\left\langle\left[\hat{c}_{\mathbf{x}}(t), \hat{c}_{\mathbf{x}^{\prime}}\left(t^{\prime}\right)^{\dagger}\right]_{+}\right\rangle_{0} \quad (\mathrm{~A} 4)
$$

$$
g_{\mathbf{x} \mathbf{x}^{\prime}}^{<}\left(t-t^{\prime}\right)=\mathrm{i}\left\langle\hat{c}_{\mathbf{x}^{\prime}}^{\dagger}\left(t^{\prime}\right) \hat{c}_{\mathbf{x}}(t)\right\rangle_{0}, \quad (\mathrm{~A} 5)
$$

where we introduced a multi-index $\mathbf{x}=(i, \alpha, \sigma)$. Here the average is taken over the initial equilibrium states of the uncoupled non-interacting systems. An important assumption is that stationarity is reached and therefore the single particle Green function depend only on the relative time $\tau=t-t'$, e.g., $G^{<}(\omega)=\int d \tau e^{i \omega \tau} G^{<}(\tau)$. The total self-energy is the sum of the lead induced hybridization self-energies $\Sigma_{\mathrm{HY}}^{\mathrm{X}}(\omega)=\sum_{\alpha} \Sigma_{\mathrm{HY}, \alpha}^{\mathrm{X}}(\omega)$ accounting for the coupling with the leads $\alpha=L, R$ and the many-body self-energy $\Sigma_{\mathrm{MB}}^{\mathrm{X}}(\omega)$ accounting for the electron-electron scattering. The components of the hybridization self-energies are given by:

$$
\Sigma_{\mathrm{HY}, \alpha}^{R}(\omega)=-\mathrm{i} \frac{\boldsymbol{\Gamma}_{\alpha}}{2} \quad (\mathrm{~A} 6)
$$

$$
\Sigma_{\mathrm{HY}, \alpha}^{<}(\omega)=\mathrm{i} \boldsymbol{\Gamma}_{\alpha} f_{\alpha}\left(\beta_{\alpha}\left(\omega-\mu_{\alpha}\right)\right) \quad (\mathrm{A} 7)
$$

with $f(x)=\left(e^{x}+1\right)^{-1}$ the Fermi-Dirac distribution. These self-energies are obtained in the wide-band limit, namely the density of states of the leads is constant over the range of the density of states of the system we are interested in. The matrices $\boldsymbol{\Gamma}_{\alpha}$ carry the information about the coupling strength between the lead $\alpha$ and the system as well as information on the geometry of the coupling. We take the following form for the coupling matrices

$$
\left(\boldsymbol{\Gamma}_{G}\right)_{\mathbf{x} \mathbf{x}^{\prime}}=\Gamma_{G} \delta_{\sigma \sigma^{\prime}} \delta_{i, j} \delta_{\alpha, \alpha^{\prime}} \quad (\mathrm{A} 8)
$$

$$
\left(\boldsymbol{\Gamma}_{L}\right)_{\mathbf{x} \mathbf{x}^{\prime}}=\Gamma_{L} \delta_{\sigma \sigma^{\prime}} \delta_{i, 1} \delta_{i^{\prime}, 1} \gamma_{\alpha, \alpha^{\prime}}
$$

$$
\left(\boldsymbol{\Gamma}_{R}\right)_{\mathbf{x} \mathbf{x}^{\prime}}=\Gamma_{R} \delta_{\sigma \sigma^{\prime}} \delta_{i, N} \delta_{i^{\prime}, N} \gamma_{\alpha, \alpha^{\prime}},
$$

where the matrices $\gamma_{\alpha, \alpha'}$ are given by:

$$
\gamma_{\alpha, \alpha^{\prime}}=\sum_{s, s^{\prime}} \delta_{\alpha, s} \delta_{\alpha^{\prime}, s^{\prime}}, \quad (\mathrm{A} 9)
$$

with the sums running over $a, b$ for the sawtooth and $a,b,c$ for the diamond. With this geometry the driving leads $L, R$ are coupled to the first and last cell of the system respectively.

We refer the reader to the Refs [35, 44, 53, 54] for the details of the derivation of the equations above. For the many-body self-energies we consider the GW approximations as discussed in the main text. Through the singleparticle Green functions in Eqs. (A1) and (A2) it is possible to extract information about physical quantities of interests. In particular, the total current through the system is defined as $I=I_{L}-I_{R}$ with $I_{\alpha} \equiv-e d\left\langle\hat{N}_{\alpha}\right\rangle / d t$, where $\hat{N}_{\alpha}$ is the total particle number operator of the lead $\alpha$. The current in the left lead is given by:

$$
I_{L}=\frac{e}{\hbar} \int_{-\infty}^{\infty} \frac{d \omega}{2 \pi} \mathcal{T}(\omega)\left(f\left(\beta_{L}\left(\omega-\mu_{L}\right)\right)-f\left(\beta_{R}\left(\omega-\mu_{R}\right)\right)\right), \quad (\mathrm{A} 10)
$$

where the transmission function is $\mathcal{T}(\omega)=$ $\operatorname{Tr}\left(\Gamma_{L} G^{R}(\omega) \Gamma_{R} G^{A}(\omega)\right)$. A similar equation holds for the current flowing to the right lead.

Analogously, the energy current is defined as the variation of energy of the lead $J_{\alpha} \equiv d\left\langle\hat{H}_{\alpha}\right\rangle / d t$ and which can be easily shown to be:

$$
J_{L}=\frac{1}{\hbar} \int_{-\infty}^{\infty} \frac{d \omega}{2 \pi} \omega \mathcal{T}(\omega)\left(f\left(\beta_{L}\left(\omega-\mu_{L}\right)\right)-f_{R}\left(\beta_{R}\left(\omega-\mu_{R}\right)\right)\right). \quad (\mathrm{A} 11)
$$

It is worth mentioning that at stationarity we have, by definition, that the number of particles in the system does not change and therefore $I_{L}=-I_{R}$ which follows from the conservation of the total number of particles. Therefore we have $I=2 I_{L}$, and for this reason we consider only $I_{L}$. The full expression $I=I_{L}-I_{R}$ is useful in the transient when the two currents need not to be equal in value and opposite in sign. The same hold for the energy currents, and therefore for the heat currents defined as $\dot{Q}_{\alpha}=J_{\alpha}-\mu_{\alpha} I_{\alpha} / e$.

From the current we compute the electrical and thermal conductivities of the system by expanding to first order in both $\Delta V$ and $\Delta T$:

$$
\begin{aligned}
& \left(f\left(\beta_{L}\left(\omega-\mu_{L}\right)\right)-f_{R}\left(\beta_{R}\left(\omega-\mu_{R}\right)\right)\right) \quad (\mathrm{A} 12) \\
& \quad \approx \frac{\partial f}{\partial \omega}\left(-e \Delta V-\frac{(\omega-\mu)}{T} \Delta T\right),
\end{aligned}
$$

where $T$ is the temperature. This gives

$$
\sigma=\frac{e^{2}}{\hbar} \int_{-\infty}^{\infty} \frac{d \omega}{2 \pi} \mathcal{T}(\omega)\left(-\frac{\partial f}{\partial \omega}\right), \quad (\mathrm{A} 13)
$$

$$
\kappa_{0}=\frac{1}{T \hbar} \int_{-\infty}^{\infty} \frac{d \omega}{2 \pi} \mathcal{T}(\omega)\left(-\frac{\partial f}{\partial \omega}\right)(\omega-\mu)^{2}. \quad (\mathrm{A} 14)
$$

Inserting Eq. (A12) in Eq. (A10) it is possible to derive an expression for the thermovoltage $\Delta V_{t h}$ such that $I_{L}\left(\Delta V_{t h}, \Delta T\right)=0$ and for the Seebeck coefficient:

$$
\Delta V_{t h}=-\frac{e}{\sigma T} \Delta T S=-\frac{\Delta V_{t h}}{\Delta T}=\frac{e}{\sigma T}. \quad (\mathrm{A} 15)
$$

[1] Zahra Aslani, Fabio Taddei, Fabrizio Dolcini, and Alessandro Braggio. Enhanced thermoelectricity in nanowires with inhomogeneous helical states. Physical

Review Research, 8(1), February 2026.

[2] Meryem Bouaziz, Aymen Mahmoudi, Davide Romanin, Jean-Christophe Girard, Yannick J Dappe, François Bertran, Marco Pala, Julien Chaste, Fabrice Oehler, and Abdelkarim Ouerghi. Anisotropic flat band and charge density wave in quasi-one-dimensional indium telluride. Phys. Rev. B., 110(4), July 2024.

[3] G. Bouzerar. Quantum transport in flat bands and su- permetallicity. Physical Review B, 103(7):075415, 2021.

[4] G. Bouzerar. Giant boost of the quantum metric in dis- ordered one-dimensional flat-band systems. Physical Re- view B, 106(12):125125, 2022.

[5] Kieron Burke. Perspective on density functional the- ory. The Journal of Chemical Physics, 136(15):150901, 04 2012.

[6] M. Büttiker. Four-terminal phase-coherent conductance. Phys. Rev. Lett., 57(14):1761-1764, 1986.

[7] Youngjoon Choi, Hyunjin Kim, Cyprian Lewandowski, Yang Peng, Alex Thomson, Robert Polski, Yiran Zhang, Kenji Watanabe, Takashi Taniguchi, Jason Alicea, and Stevan Nadj-Perge. Interaction-driven band flattening and correlated phases in twisted bilayer graphene. Nat. Phys., 17(12):1375-1381, December 2021.

[8] Francesco Cosco, Riku Tuovinen, and Nicolino Lo Gullo. Interacting electrons in a flat-band system within the generalized kadanoff-baym ansatz. physica status solidi (b), March 2024.

[9] F. Covito, F. G. Eich, R. Tuovinen, M. A. Sentef, and A. Rubio. Transient charge and energy flow in the wide- band limit. Journal of Chemical Theory and Computa- tion, 14(5):2495-2504, May 2018.

[10] Nicholas Dale, M. Iqbal Bakti Utama, Dongkyu Lee, Nicolas Leconte, Sihan Zhao, Kyunghoon Lee, Takashi Taniguchi, Kenji Watanabe, Chris Jozwiak, Aaron Bost- wick, Eli Rotenberg, Roland J. Koch, Jeil Jung, Feng Wang, and Alessandra Lanzara. Layer-dependent inter- action effects in the electronic structure of twisted bilayer graphene devices. Nano Letters, 23(15):6799-6806, 2023.

[11] Oleg Derzhko, Johannes Richter, and Mykola Maksy- menko. Strongly correlated flat-band systems: The route from Heisenberg spins to Hubbard electrons. Interna- tional Journal of Modern Physics B, 29(12):1530007, 2015.

[12] M. S. Dresselhaus, G. Chen, M. Y. Tang, R. G. Yang, H. Lee, D. Z. Wang, Z. F. Ren, J.-P. Fleurial, and P. Gogna. New directions for low-dimensional thermo- electric materials. Advanced Materials, 19(8):1043-1053, 2007.

[13] Bivas Dutta, Joonas T. Peltonen, Dmitry S. Antonenko, Matthias Meschke, Mikhail A. Skvortsov, Björn Kubala, Jürgen König, Clemens B. Winkelmann, Hervé Cour- tois, and Jukka P. Pekola. Thermal conductance of a single-electron transistor. Physical Review Letters, 119(7):077701, 2017.

[14] J Eckel, F Heidrich-Meisner, S G Jakobs, M Thorwart, M Pletyukhov, and R Egger. Comparative study of theo- retical methods for non-equilibrium quantum transport. New Journal of Physics, 12(4):043042, apr 2010.

[15] F. G. Eich, M. Di Ventra, and G. Vignale. Density- functional theory of thermoelectric phenomena. Phys. Rev. Lett., 112:196401, May 2014.

[16] F G Eich, M Di Ventra, and G Vignale. Functional the-ories of thermoelectric phenomena. Journal of Physics: Condensed Matter, 29(6):063001, dec 2016.

[17] Jisong Gao, Haijun Cao, Xuegao Hu, Hui Zhou, Zhi- hao Cai, Qiaoxiao Zhao, Dong Li, Zhicheng Gao, Shin- ichiro Ideta, Kenya Shimada, Peng Cheng, Lan Chen, Kehui Wu, Sheng Meng, and Baojie Feng. Flat bands and temperature-driven phase transition in quasi-one- dimensional zigzag chains. Physical Review Letters,134(8), February 2025.

[18] Fabian Garmroudi, Jennifer Coulter, Illia Serhiienko, Simone Di Cataldo, Michael Parzer, Alexander Riss, Matthias Grasser, Simon Stockinger, Sergii Khmelevskyi, Kacper Pryga, Bartlomiej Wiendlocha, Karsten Held, Takao Mori, Ernst Bauer, Antoine Georges, and Andrej Pustogow. Topological flat-band-driven metallic thermo- electricity. Physical Review X, 15(2), May 2025.

[19] Fabian Garmroudi, Simone Di Cataldo, Michael Parzer, Jennifer Coulter, Yutaka Iwasaki, Matthias Grasser, Si- mon Stockinger, Stephan Pázmán, Sandra Witzmann, Alexander Riss, Herwig Michor, Raimund Podloucky, Sergii Khmelevskyi, Antoine Georges, Karsten Held, Takao Mori, Ernst Bauer, and Andrej Pustogow. Energy filtering-induced ultrahigh thermoelectric power factors in ni 3 ge. Science Advances, 11(31), August 2025.

[20] Dorothea Golze, Marc Dvorak, and Patrick Rinke. The gw compendium: A practical guide to theoretical photoe-mission spectroscopy. Frontiers in Chemistry, Volume 7 - 2019, 2019.

[21] L. D. Hicks and M. S. Dresselhaus. Effect of quantum- well structures on the thermoelectric figure of merit. Physical Review B, 47(19):12727-12731, 1993.

[22] L. D. Hicks and M. S. Dresselhaus. Thermoelectric figure of merit of a one-dimensional conductor. Physical Review B, 47(24):16631-16634, 1993.

[23] J. Hubbard. Electron correlations in narrow energy bands. Proceedings of the Royal Society of London. Series A. Mathematical and Physical Sciences, 276:238-257, 11 1963.

[24] J. Hubbard. Electron correlations in narrow energy bands. ii. the degenerate band case. Proceedings of the Royal Society of London. Series A. Mathematical and Physical Sciences, 277:237-259, 1 1964.

[25] Deep Bahadur Karki. Wiedemann-Franz law in scatter- ing theory revisited. Physical Review B, 102(11):115423, 2020.

[26] Thomas Kloss, Joseph Weston, Benoit Gaury, Benoit Rossignol, Christoph Groth, and Xavier Waintal. Tk- want: a software package for time-dependent quantum transport. New Journal of Physics, 23(2):023025, feb 2021.

[27] Keita Kobayashi, Masahiko Okumura, Susumu Yamada, Masahiko Machida, and Hideo Aoki. Superconductivity in repulsively interacting fermions on a diamond chain: Flat-band-induced pairing. Phys. Rev. B, 94:214501, Dec 2016.

[28] Björn Kubala, Jürgen König, and Jukka P. Pekola. Vi- olation of the Wiedemann-Franz law in a single-electron transistor. Physical Review Letters, 100(6):066801, 2008.

[29] S. Kurth, G. Stefanucci, C.-O. Almbladh, A. Rubio, and E. K. U. Gross. Time-dependent quantum transport: A practical scheme using density functional theory. Phys. Rev. B, 72:035308, Jul 2005.

[30] Rolf Landauer. Spatial variation of currents and fields due to localized scatterers in metallic conduction. IBM J. Res. Dev., 1(3):223-231, 1957.

[31] Rolf Landauer. Electrical resistance of disordered one-

dimensional lattices. Philos. Mag., 21(172):863–867,
1970.

[32] Cyprian Lewandowski, Stevan Nadj-Perge, and Debanjan
Chowdhury. Does filling-dependent band renormalization
aid pairing in twisted bilayer graphene? npj Quantum
Materials, 6:82, 2021.

[33] Daniel Leykam, Alexei Andreanov, and Sergej Flach. Ar-
tificial flat band systems: from lattice models to experi-
ments. Advances in Physics: X, 3(1):1473052, 2018.

[34] Delong Li, Youning Gong, Yuexing Chen, Jiamei Lin,
Qasim Khan, Yupeng Zhang, Yu Li, Han Zhang, and
Heping Xie. Recent progress of two-dimensional thermo-
electric materials. Nanomicro Lett., 12(1):36, January
2020.

[35] N. Lo Gullo and L. Dell'Anna. Self-consistent keldysh
approach to quenches in the weakly interacting bose-
hubbard model. Phys. Rev. B, 94:184308, Nov 2016.

[36] G. D. Mahan and J. O. Sofo. The best thermoelectric.
Proceedings of the National Academy of Sciences of the
United States of America, 93(15):7436–7439, 1996.

[37] Danial Majidi, Martin Josefsson, Mukesh Kumar, Mar-
tin Leijnse, Lars Samuelson, Hervé Courtois, Clemens B.
Winkelmann, and Ville F. Maisi. Quantum confinement
suppressing electronic heat flow below the Wiedemann–
Franz law. Nano Letters, 22(2):630–635, 2022.

[38] Yigal Meir and Ned S. Wingreen. Landauer formula for
the current through an interacting electron region. Phys.
Rev. Lett., 68:2512–2515, Apr 1992.

[39] Antonio Palamara, Francesco Plastina, Antonello Sin-
dona, and Irene D'Amico. Thermal-density-functional-
theory approach to quantum thermodynamics. Phys.
Rev. A, 110:062203, Dec 2024.

[40] Y. Pavlyukh and R. Tuovinen. Open system dynamics
in linear time beyond the wide-band limit. Phys. Rev. B,
111:L241101, Jun 2025.

[41] Pedro Portugal, Christian Flindt, and Nicola Lo Gullo.
Heat transport in a two-level system driven by a time-
dependent temperature. Phys. Rev. B, 104:205420, Nov
2021.

[42] Ville A. J. Pyykkönen, Sebastiano Peotta, Philipp Fabri-
tius, Jeffrey Mohan, Tilman Esslinger, and Päivi Törmä.
Flat-band transport and josephson effect through a finite-
size sawtooth lattice. Phys. Rev. B, 103:144519, Apr
2021.

[43] Ville A. J. Pyykkönen, Sebastiano Peotta, and Päivi
Törmä. Suppression of nonequilibrium quasiparticle
transport in flat-band superconductors. Phys. Rev. Lett.,
130:216003, May 2023.

[44] M Ridley, N W Talarico, D Karlsson, N Lo Gullo, and
R Tuovinen. A many-body approach to transport in
quantum systems: from the transient regime to the sta-
tionary state. Journal of Physics A: Mathematical and
Theoretical, 55(27):273001, jun 2022.

[45] G. Jeffrey Snyder and Eric S. Toberer. Complex thermo-
electric materials. Nature Materials, 7(2):105–114, 2008.

[46] Nahual Sobrino, Roberto D'Agosta, and Stefan Kurth.
Thermoelectric efficiency in multiterminal quantum ther-
mal machines from steady-state density functional the-
ory. Phys. Rev. B, 107:195116, 2023.

[47] Nahual Sobrino, Florian G. Eich, Gianluca Stefanucci,
Roberto D'Agosta, and Stefan Kurth. Thermoelectric
transport within density functional theory. Phys. Rev.
B, 104:125115, 2021.

[48] Nahual Sobrino, David Jacob, and Stefan Kurth. An-
alytic approach to thermoelectric transport in double
quantum dots. Phys. Rev. B, 111:115108, 2025.

[49] G. Stefanucci and C.-O. Almbladh. Time-dependent
quantum transport: An exact formulation based on
tddft. Europhysics Letters, 67(1):14, jul 2004.

[50] Gianluca Stefanucci. Bound states in ab initio approaches
to quantum transport: A time-dependent formulation.
Phys. Rev. B, 75:195115, May 2007.

[51] Gianluca Stefanucci and Robert van Leeuwen. Nonequi-
librium Many-Body Theory of Quantum Systems: A
Modern Introduction. Cambridge University Press, 2013.

[52] S. Tacchi, J. Flores-Farías, D. Petti, F. Brevis, A. Cat-
toni, G. Scaramuzzi, D. Girardi, D. Cortés-Ortuño, R. A.
Gallardo, E. Albisetti, G. Carlotti, and P. Landeros. Ex-
perimental observation of flat bands in one-dimensional
chiral magnonic crystals. Nano Letters, 23(14):6776–
6783, 2023.

[53] N. W. Talarico, S. Maniscalco, and N. Lo Gullo. Study
of the energy variation in many-body open quantum sys-
tems: Role of interactions in the weak and strong cou-
pling regimes. Phys. Rev. B, 101:045103, Jan 2020.

[54] Natale Walter Talarico, Sabrina Maniscalco, and Nicol-
ino Lo Gullo. A scalable numerical approach to the
solution of the dyson equation for the non-equilibrium
single-particle green's function. physica status solidi (b),
256(7):1800501, 2019.

[55] R. Tuovinen and Y. Pavlyukh. Thermoelectric energy
conversion in molecular junctions out of equilibrium.
PRX Energy, 4:043003, Oct 2025.

[56] M Di Ventra and T N Todorov. Transport in
nanoscale systems: the microcanonical versus grand-
canonical picture. Journal of Physics: Condensed Mat-
ter, 16(45):8025, oct 2004.

[57] C. J. O. Verzijl, J. S. Seldenthuis, and J. M. Thijssen. Ap-
plicability of the wide-band limit in dft-based molecular
transport calculations. The Journal of Chemical Physics,
138(9):094102, 03 2013.

[58] J. K. Viljas, J. C. Cuevas, F. Pauly, and M. Häfner.
Electron-vibration interaction in transport through
atomic gold wires. Phys. Rev. B, 72:245415, Dec 2005.

[59] Glenn Wagner, Souvik Das, Johannes Jung, Artem
Odobesko, Felix Küster, Florian Keller, Jedrzej Korczak,
Andrzej Szczerbakow, Tomasz Story, Stuart S P Parkin,
Ronny Thomale, Titus Neupert, Matthias Bode, and
Paolo Sessi. Interaction effects in a 1D flat band at a
topological crystalline step edge. Nano Lett., 23(7):2476–
2482, April 2023.

[60] Ming Xie and Allan H. MacDonald. Nature of the corre-
lated insulator states in twisted bilayer graphene. Phys-
ical Review Letters, 124:097601, 2020.

[61] Lihua Zhao, Biao Xu, and Minhua Hu. Size effect in ther-
moelectric materials. npj Quantum Materials, 1:16028,
2016.