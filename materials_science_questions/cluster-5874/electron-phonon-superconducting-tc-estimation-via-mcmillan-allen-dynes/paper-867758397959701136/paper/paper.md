# Fully anisotropic superconductivity with few Helmholtz Fermi-surface harmonics

Jon Lafuente-Bartolome, $^{1,2}$ Idoia G. Gurtubay, $^{1,2}$ and Asier Eiguren $^{1,2}$

$^{1}$ Materia Kondentsatuaren Fisika Saila, University of the Basque Country UPV/EHU, 48080 Bilbao, Basque Country, Spain.
$^{2}$ Donostia International Physics Center (DIPC),
Paseo Manuel de Lardizabal 4, 20018 Donostia-Sebastián, Spain

(Dated: October 15, 2020)

We present an alternative representation for the anisotropic Eliashberg equations of superconductivity, whose numerical solution yields an efficiency gain of several orders of magnitude with respect to the conventional representation in momentum space. Our method is a practical realization of a long-sought approach, whose essence is a linear transformation from regular $\mathbf{k}$ space to a set of orthonormal functions defined as the solutions of the Helmholtz equation on the Fermi surface. In this way, all the anisotropy of the problem can be described by a handful of coefficients with built-in symmetry. We perform benchmark calculations on the gap anisotropy of MgB₂, and reproduce previous results at a remarkably reduced computational cost. Furthermore, we apply our methodology to efficiently determine the transition temperature of the compressed YH₆ hydride, obtaining very good agreement with recent experimental measurements. The simplification introduced by our method enables the high-throughput exploration of superconducting materials without having to resort to the isotropic approximation, and opens up possibilities towards first principles calculations of more advanced theories of superconductivity.

The microscopic theory of superconductivity put forward by Bardeen, Cooper and Schrieffer [1] stands for one of the greatest achievements of condensed matter theory, as it provided the first quantitative explanation of the different experimental signatures of superconductivity available at the time. The frequency-dependence of the superconducting gap found soon after in strong-coupling superconductors [2], was successfully rationalized by the extension of the theory developed by Eliashberg [3, 4], which accounted for retardation effects in the electron-phonon interaction. The discovery of superconductivity in MgB₂ at 39 K [5] and its multiple-gap structure [6–9] challenged the theory once again, as it added another crucial aspect to consider: the anisotropy of the electron-phonon interaction [10]. The development of numerical methods to compute electron-phonon interactions from first principles has witnessed an enormous progress thereafter [11], and a detailed theoretical account of experimentally measured anisotropic superconducting properties is possible nowadays [12–15].

The advent of high-temperature superconductivity in hydrides at high pressures has resulted in a change of paradigm in superconductivity research, in which experimental efforts are guided by prior theoretical predictions [16, 17]. This synergy has led to the discovery of the superconductors with the highest critical temperature up to date [18–20]. Advanced structure searching algorithms are constantly expanding the range of possible candidates [21], but due to the exceedingly high computational burden associated with a full account of the anisotropy, predictions on the critical temperature almost invariably assume an isotropic electron-phonon interaction, and in most cases are based on the semi-empirical McMillan-Allen-Dynes formula [22]. The urgency to include full anisotropic resolution in the systematic predictions of superconducting properties in the vast range of possible interesting candidates asks for further methodological developments.

A particularly elegant and promising scheme in this direction was proposed by Allen [23]. By rewriting the electron self-energy in terms of an orthonormal set of functions, the so-called Fermi-surface harmonics (FSH), he showed that the anisotropic Eliashberg equations of superconductivity could take a particularly simple form [24]. The key advantage comes from replacing the continuous integrals in $\mathbf{k}$ space by discrete sums in FSH coefficients, where one can apply a cutoff and reduce the size of the problem dramatically without losing accuracy, provided that those sums converge rapidly. However, the technical difficulties to implement the specific basis set proposed in Ref. [23] has turned the practical realization of the original idea unattainable.

In this work, we present a reformulation of the Eliashberg equations in terms of an alternative basis set, composed of the solutions of the Helmholtz equation defined on the Fermi surface, namely, the Helmholtz Fermi-surface harmonics (HFSH) [25]. We explicitly show that this representation turns out to be strikingly beneficial in the problem of superconductivity, reducing the computational workload in several orders of magnitude. The robustness of the numerical procedure to obtain the HFSH functions allows for a systematic application of the method in diverse materials with different crystal structures or Fermi surface topologies. Additional improvements in the method [26] provide a proper account of the gap symmetry, and at the same time reduce the size in the expansions even further. We perform benchmark calculations in the paradigmatic anisotropic superconductor MgB₂, and determine the critical temperature of the recently synthesized YH₆ under pressure within

full anisotropic accuracy with a handful of coefficients.

We start by briefly reviewing the anisotropic Eliash- berg theory of phonon-mediated superconductivity. More detailed derivations and discussions can be found, for example, in Ref. [24].

For most metals, the characteristic phonon energies $(\omega_D)$ are much smaller than the electronic energies $(\varepsilon_F)$, that is $\omega_D/\varepsilon_F \ll 1$. In this regime, the Migdal approximation [27] in which the Eliashberg theory relies, remains valid. This very same fact restricts the phonon-mediated superconducting pairing to a very narrow window around the Fermi surface. As a result, the problem of superconductivity is reduced to the solution of two coupled nonlinear integral equations defined on the Fermi surface [24]:

$$
\begin{aligned}
Z_{\mathbf{k}}\left(i \omega_{j}\right)=1 & +\frac{\pi T}{\omega_{j} N_{F} \Omega_{\mathrm{BZ}}} \sum_{j^{\prime}} \int_{S_{F}} \frac{d s_{\mathbf{k}^{\prime}}}{v_{\mathbf{k}^{\prime}}} R_{\mathbf{k}^{\prime}}^{Z}\left(i \omega_{j^{\prime}}\right) \\
& \times \lambda_{\mathbf{k}, \mathbf{k}^{\prime}}\left(i \omega_{j}-i \omega_{j^{\prime}}\right),
\end{aligned}
\tag{1}
$$

$$
\begin{aligned}
\phi_{\mathbf{k}}\left(i \omega_{j}\right)= & \frac{\pi T}{N_{F} \Omega_{\mathrm{BZ}}} \sum_{j^{\prime}} \int_{S_{F}} \frac{d s_{\mathbf{k}^{\prime}}}{v_{\mathbf{k}^{\prime}}} R_{\mathbf{k}^{\prime}}^{\phi}\left(i \omega_{j^{\prime}}\right) \\
& \times\left[\lambda_{\mathbf{k}, \mathbf{k}^{\prime}}\left(i \omega_{j}-i \omega_{j^{\prime}}\right)-\mu^{*}\left(\omega_{c}\right)\right],
\end{aligned}
\tag{2}
$$

where band indices have been omitted for simplicity, and the following auxiliary definitions have been used:

$$
R_{\mathbf{k}}^{Z}\left(i \omega_{j}\right)=\frac{\omega_{j} Z_{\mathbf{k}}\left(i \omega_{j}\right)}{\sqrt{\left[\omega_{j} Z_{\mathbf{k}}\left(i \omega_{j}\right)\right]^{2}+\phi_{\mathbf{k}}\left(i \omega_{j}\right)^{2}}},
\tag{3a}
$$

$$
R_{\mathbf{k}}^{\phi}\left(i \omega_{j}\right)=\frac{\phi_{\mathbf{k}}\left(i \omega_{j}\right)}{\sqrt{\left[\omega_{j} Z_{\mathbf{k}}\left(i \omega_{j}\right)\right]^{2}+\phi_{\mathbf{k}}\left(i \omega_{j}\right)^{2}}}.
\tag{3b}
$$

In these expressions, $N_F$ is the density of states at the Fermi surface, $v_{\mathbf{k}}$ is the electron velocity and $\Omega_{\text{BZ}}$ is the volume of the Brillouin zone. The self-consistent solution of these coupled equations yields the renormalization factor $Z_{\mathbf{k}}(i\omega_j)$ and the pair field $\phi_{\mathbf{k}}(i\omega_j)$ at a given temperature $T$, where $\omega_j=(2j+1)\pi T$ are the Matsubara frequencies, $j$ being integer numbers. Only for temperatures below the superconducting transition temperature $(T \leq T_c)$ will the resulting pair-field $\phi$ be finite. Following the most typical practice, the Coulomb repulsion has been approximated by the Morel-Anderson pseudopotential $\mu^*(\omega_c)$ [28] with a cutoff frequency of the order of $\omega_c \sim 10\omega_D$. All the anisotropy and retardation effects of the electron-phonon interaction are contained in $\lambda_{\mathbf{k},\mathbf{k}'}(i\omega)$,

which is defined as [11],

$$
\lambda_{\mathbf{k}, \mathbf{k}^{\prime}}(i \omega)=N_{F} \sum_{\nu} \frac{2 \omega_{\mathbf{k}^{\prime}-\mathbf{k}, \nu}}{\omega_{\mathbf{k}^{\prime}-\mathbf{k}, \nu}^{2}+\omega^{2}}\left|g_{\mathbf{k}, \mathbf{k}^{\prime}}^{\nu}\right|^{2},
\tag{4}
$$

where $\omega_{\mathbf{k}'-\mathbf{k},\nu}$ is the frequency of a phonon mode $\nu$ with momentum $\mathbf{q} \equiv \mathbf{k}'-\mathbf{k}$, and $g_{\mathbf{k},\mathbf{k}'}^{\nu}$ is the electron-phonon matrix elements for the scattering between states $\mathbf{k}'$ and $\mathbf{k}$ through a phonon $\mathbf{q} \nu$. All the elements entering Eq. (4) can be computed entirely from first principles at a reasonable cost nowadays.

Nevertheless, for cases in which $\lambda_{\mathbf{k},\mathbf{k}'}$ varies considerably within the Fermi surface, an extremely fine sampling of $\mathbf{k}$ points is needed for a converged numerical integration of Eqs. (1) and (2), making their direct self-consistent solution a challenging task.

An alternative reformulation of Eqs. (1)-(3) can be obtained by expanding all the scalar quantities — denoted in general by $f_{\mathbf{k}}$ — in terms of the complete and orthonormal basis set fulfilling the Helmholtz equation on the Fermi surface $\{\Phi_L(\mathbf{k})\}$ [25],

$$
f_{\mathbf{k}}=\sum_{L} f_{L} \Phi_{L}(\mathbf{k}),
\tag{5}
$$

so that Eqs. (1) and (2) take the form

$$
\begin{aligned}
Z_{L}\left(i \omega_{j}\right)= & \delta_{L 0}+\frac{\pi T}{\omega_{j}} \sum_{j^{\prime} L^{\prime}} R_{L^{\prime}}^{Z}\left(i \omega_{j^{\prime}}\right) \\
& \times \lambda_{L, L^{\prime}}\left(i \omega_{j}-i \omega_{j^{\prime}}\right),
\end{aligned}
\tag{6}
$$

$$
\begin{aligned}
\phi_{L}\left(i \omega_{j}\right)= & \pi T \sum_{j^{\prime} L^{\prime}} R_{L^{\prime}}^{\phi}\left(i \omega_{j^{\prime}}\right) \\
& \times\left[\lambda_{L, L^{\prime}}\left(i \omega_{j}-i \omega_{j^{\prime}}\right)-\mu^{*}\left(\omega_{c}\right) \delta_{L 0, L^{\prime} 0}\right].
\end{aligned}
\tag{7}
$$

In this HFSH representation, all the anisotropy of the electron-phonon interaction is encoded in the coefficients,

$$
\lambda_{L, L^{\prime}}(i \omega)=\frac{\int_{S_{F}} \frac{d s_{\mathbf{k}}}{v_{\mathbf{k}}} \int_{S_{F}} \frac{d s_{\mathbf{k}^{\prime}}}{v_{\mathbf{k}^{\prime}}} \lambda_{\mathbf{k}, \mathbf{k}^{\prime}}(i \omega) \Phi_{L}(\mathbf{k}) \Phi_{L^{\prime}}\left(\mathbf{k}^{\prime}\right)}{\int_{S_{F}} \frac{d s_{\mathbf{k}}}{v_{\mathbf{k}}} \int_{S_{F}} \frac{d s_{\mathbf{k}^{\prime}}}{v_{\mathbf{k}^{\prime}}}}.
\tag{8}
$$

If the coefficients $\lambda_{L,L'}$ are shown to decay rapidly for increasing indices, a cutoff can be applied in the sums of Eqs. (6) and (7) without any loss accuracy. Moreover, in the case of conventional $s$-wave superconductors, both $Z_{\mathbf{k}}$ and $\phi_{\mathbf{k}}$ must be invariant under all the symmetry operations of the crystal. As a result, only the fully symmetric HFSH functions, which we denote by the indices $\tilde{L}$ and fulfill $\Phi_{\tilde{L}}(S_n \mathbf{k}_i)=\Phi_{\tilde{L}}(\mathbf{k}_i)$ for all the $S_n$ symmetry operations of the point group, will contribute to their expansions — see Eq. (5). In this way, Eqs. (6),(7) can be effectively reduced to this fully symmetric subset. The sparse character of $\lambda_{L,L'}$ reflects the selection rules imposed by symmetry, which are exactly accounted for in this method. This translates into an important reduction of the dimension of the problem, and most importantly, allows for a proper account of the symmetry of the computed quantities by construction. All the details about our numerical implementation to incorporate the crystal symmetries in the HFSH basis set are described in Ref. [26].

We now demonstrate the benefit of the transformation by performing benchmark calculations in the paradigmatic anisotropic superconductor $\text{MgB}_2$, for which a detailed account of the gap anisotropy has been already

![](./images/867758397959701136_1.jpg)

FIG. 1. (a) Two-index electron-phonon mass enhancement parameter $\lambda_{\mathbf{k},\mathbf{k}'} \equiv \lambda_{\mathbf{k},\mathbf{k}'}(i\omega=0)$ computed from first principles on a discretized mesh of triangular vertices on the outer $\sigma$ Fermi surface sheet of MgB₂, unfolded into a matrix representation. In this example, the isosurface is formed by $\sim3\times10^3$ vertices. (b) First four fully symmetric Helmholtz Fermi-surface harmonics (HFSH) basis functions on this Fermi surface sheet. (c) Magnitude, in logarithmic scale, of the first $10\times10$ fully symmetric HFSH coefficients of the two-index mass enhancement parameter $\lambda_{\tilde{L},\tilde{L}'}$ on this Fermi surface sheet. Coefficients for larger values of $\tilde{L}$ are smaller than $10^{-3}$ in magnitude.

reported on multiple occasions [10, 12]. As an illustrative example, in Fig. 1(a), we represent the anisotropic $\lambda_{\mathbf{k},\mathbf{k}'} \equiv \lambda_{\mathbf{k},\mathbf{k}'}(i\omega=0)$ parameter on the outer $\sigma$ Fermi surface sheet of MgB₂ in a matrix form, computed from first principles on a discrete mesh of $\mathbf{k},\mathbf{k}'$ points forming a triangularly tessellated Fermi surface (see Ref. [26] for computational details). This example represents a typical scenario where a dense sampling of $n_k\times n_{k'}\sim10^4\times10^4$ points is needed to obtain a converged solution of Eqs. (1)-(3), as $\lambda_{\mathbf{k},\mathbf{k}'}$ varies considerably from point to point on the Fermi surface. In contrast, by transforming this quantity to the HFSH representation, all of its anisotropic details can be described by a handful of coefficients. We show the first four $\Phi_{\tilde{L}}(\mathbf{k})$ functions of this sheet in Fig. 1(b) for illustrative purposes, and the magnitude of the first $\lambda_{\tilde{L},\tilde{L}'}$ coefficients, as obtained by Eq. (8), are given in Fig. 1(c) in logarithmic scale. All the elements beyond this $10\times10$ matrix are lower than $10^{-3}$ in magnitude, and therefore give a negligible contribution to the sums in Eqs. (6) and (7). This implies that these equations can be solved in such a notably reduced subspace with virtually no loss of accuracy.

In order to verify this assertion, we solve Eqs. (6) and (7) for MgB₂ at $T=10$ K, using different cutoff values in the sums, which we denote by $n_{\tilde{L}}$. We show in Fig. 2 our results for the calculated superconducting gap on the Fermi surface,

$$
\Delta_{\mathbf{k}}^{n_{\tilde{L}}}=\frac{\phi_{\mathbf{k}}^{n_{\tilde{L}}}}{Z_{\mathbf{k}}^{n_{\tilde{L}}}}=\frac{\sum_{\tilde{L}}^{n_{\tilde{L}}}\phi_{\tilde{L}}\Phi_{\tilde{L}}(\mathbf{k})}{\sum_{\tilde{L}}^{n_{\tilde{L}}}Z_{\tilde{L}}\Phi_{\tilde{L}}(\mathbf{k})},
\tag{9}
$$

using $n_{\tilde{L}}=16$, four per Fermi surface sheet. The Matsubara frequency cutoff has been set to ten times the maximum phonon energy, and $\mu^*=0.16$ has been used. In very good agreement with previous results [12], we see that $\Delta_{\mathbf{k}}$ clusters into two ranges of values of $(1.4,2.2)$ and $(8.0,9.3)$ meV for the $\sigma$ and $\pi$ Fermi surface sheets, respectively, varying considerably within each sheet.

Figure 2(b) shows the average of the absolute error of $\Delta_{\mathbf{k}}^{n_{\tilde{L}}}$ for different values of $n_{\tilde{L}}$, with respect to the fully converged calulation in which all the symmetric HFSHs are considered in the sums,

$$
\langle\delta\epsilon(\Delta_{\mathbf{k}}^{n_{\tilde{L}}})\rangle=\frac{\int_{S_F}ds_{\mathbf{k}}|\Delta_{\mathbf{k}}^{n_{\tilde{L}}}-\Delta_{\mathbf{k}}^{n_{\tilde{L}}_{\text{max}}}|}{\int_{S_F}ds_{\mathbf{k}}}.
\tag{10}
$$

We see that the error drops rapidly with the size of the subspace. For a basis size as small as $n_{\tilde{L}}=16$, the error is $\sim0.025$ meV, well below the current experimental resolution [29]. Besides the negligible loss of accuracy, the efficiency gain with respect to state of the art approaches is immense. Taking Ref. [12] as an example, in order to obtain fully converged calculations for the very same system, a Brillouin zone sampling of $n_{\mathbf{k}}=50^3=1.25\times10^5$ k-points was needed in momentum space. Our method, in comparison, brings an efficiency gain factor of $n_{\mathbf{k}}/n_{\tilde{L}}\sim10^4$. Another important advantage of the HFSH representation is that all the information about the superconducting state is encoded effectively in the few resulting $Z_{\tilde{L}}$ and $\Phi_{\tilde{L}}$ coefficients. This facilitates the comparison between calculations using different meshes and the interpretation of experimental measurements, in a similar spirit as it is done when comparing Fermi surface averaged values — simply given by the $\tilde{L}=0$ coefficients in the HFSH representation —, but generalized to full anisotropic detail.

Besides the superconducting gap, one of the most important quantities characterizing a superconductor is its transition temperature $T_c$, which in principle can be determined by the Eliashberg equations discussed above. Equations (1)-(3), or equivalently Eqs. (6) and (7), can be self-consistently solved in a range of temperatures, and the highest $T$ resulting in a non-vanishing pair amplitude $\phi$ can be identified as $T_c$. However, this procedure in-

![](./images/867758397959701136_2.jpg)

![](./images/867758397959701136_3.jpg)

FIG. 2. (a) Magnitude of the superconducting gap $\Delta_{\mathbf{k}}^{n_{\tilde{L}}}$ on the Fermi surface of MgB₂ at 10 K, obtained after solving the anisotropic Eliashberg equations in the HFSH representation, with a cutoff of $n_{\tilde{L}}=16$. (b) Average of the absolute error of $\Delta_{\mathbf{k}}^{n_{\tilde{L}}}$ for different values $n_{\tilde{L}}$, with respect to the result obtained by considering all the symmetric HFSHs in the sums.

volves several practical shortcomings. On the one hand, in order to obtain a meaningful accuracy for the value of $T_{c}$, the self-consistent equations have to be solved in a dense-enough range of values for $T$. On the other hand, the nonlinear character of the equations introduces numerical difficulties to achieve self-consistency for $T \approx T_{c}$, where the magnitude of $\phi$ becomes vanishingly small. We have already demonstrated that the HFSH basis set remedies the first problem, as the cost of achieving self-consistency for $T \ll T_{c}$ is minimal in this representation. In the following, we show that this basis set also provides an elegant solution to the second issue.

We start by noting that as $\phi \ll Z$ at $T \approx T_{c}$, we can drop the $\phi^{2}$ terms in the denominators of Eq. (3). After this simplification, Eq. (1) can be inserted into Eq. (2), so that we are left with a single linear equation for $\Delta_{\mathbf{k}}$. This equation can be cast into an eigenvalue problem, which after performing the transformation to the HFSH representation reads [24],

$$
\varepsilon \Delta_{L}\left(i \omega_{j}\right)=\sum_{j^{\prime} L^{\prime}} \frac{1}{\left|2 j^{\prime}+1\right|} K_{L, L^{\prime}}\left(j, j^{\prime}\right) \Delta_{L^{\prime}}\left(i \omega_{j^{\prime}}\right), \quad(11)
$$

where,

$$
\begin{aligned}
& K_{L, L^{\prime}}\left(j, j^{\prime}\right)=\lambda_{L, L^{\prime}}\left(i \omega_{j}-i \omega_{j^{\prime}}\right)-\mu_{L, L^{\prime}}^{*}\left(\omega_{c}\right) \\
& -\delta_{j j^{\prime}} \sum_{j^{\prime \prime} L^{\prime \prime}} \Xi_{L, L^{\prime} L^{\prime \prime}} \lambda_{L^{\prime \prime}, 0}\left(i \omega_{j}-i \omega_{j^{\prime}}\right) \operatorname{sgn}(j) \operatorname{sgn}\left(j^{\prime \prime}\right),
\end{aligned}
$$

being $\Xi_{L, L^{\prime} L^{\prime \prime}}$ the generalization of the Clebsch-Gordan coefficients for the HFSH basis set [23, 25]. Similar to the nonlinear equations, the rapidly decaying values of the $\lambda_{L, L^{\prime}}$ coefficients in the HFSH basis set enable one to reduce drastically the size of the kernel $K$, and hence the dimension of the eigenvalue problem, while maintaining full account of the anisotropy. The temperature at which the maximum eigenvalue $\varepsilon$ equals unity gives $T_{c}$, since in that case the linearized Eliashberg equation is fulfilled. The big advantage over the nonlinear equations (6) and (7) is that no self-consistency is needed in this case, and that the evaluation of the auxiliary $R_{L}$ functions is not needed anymore.

We illustrate this approach using the compressed $\mathrm{YH}_{6}$ hydride in its bcc structure at 300GPa as a case study (all the details of the computational setup are described in Ref. [26]). Interestingly, the recent experimental confirmation of superconductivity in this system [30, 31] has revealed a sizable deviation in the measured critical temperature with respect to the current theoretical estimates [32-34]. For the sake of comparison, we first solved the full nonlinear Eqs. (6),(7) for a set of temperatures, where we used $\mu^{*}=0.11$ as in Ref. [34]. A reduced subspace of $n_{\tilde{L}}=48$ has been sufficient to obtain converged results.

We show our results for the superconducting gap on the six Fermi surface sheets at 40 K in Fig. 3(a). We obtain a continuous range of values in (25,47) meV for $\Delta_{\mathbf{k}}$, being its anisotropy particularly large on the biggest sheets. Our results are in qualitative agreement with those reported in Ref. [34], while quantitatively we obtain smaller gap values. We trace back this discrepancy to the finer Fermi surface integrations provided by our triangulated mesh, which also reflects in a smaller magnitude of the electron-phonon mass-enhancement parameter [26]. The distribution of the gap, $\rho(\Delta)$, obtained for different temperatures is represented by the light blue shaded areas in Fig. 3(b). The magnitude of the gap decreases with temperature, and we do not find superconductivity $(\phi \neq 0)$ beyond $\sim 230 \mathrm{~K}$.

The maximum eigenvalue obtained after diagonalizing Eq. (11) for the same range of temperatures and subspace size is represented by the blue dots in Fig. 3(b), displaced by -1 for ease of visualization. Its change with temperature is very smooth, allowing for an efficient use of root finding algorithms to detect the exact point where $\varepsilon=1$ is fulfilled. We find $T_{c}=230.98 \mathrm{~K}$, in really good agreement with very recent experimental results [30, 31]. With the aim of reducing the size of the problem as much as possible, we analyze in Fig. 3(c) the sensitivity of the

![](./images/867758397959701136_4.jpg)

![](./images/867758397959701136_5.jpg)

FIG. 3. (a) Magnitude of the superconducting gap on the Fermi surface of YH₆ at 300 GPa and 40 K. (b) The light blue shaded areas represent the distribution of the gap for different temperatures. The dark-blue dots represent the maximum eigenvalue of Eq. (11) in the same range of temperatures, displaced by −1, and the dashed line is a guide to the eye. The temperature at which $\text{Max}[\varepsilon]-1=0$ is fulfilled corresponds to $T_c$, and is represented by the blue diamond. (c) Convergence of $T_c$ with respect to the cutoff applied on the HFSH expansion for solving Eq. (11). The gray shaded area represents the values within a 1% accuracy with respect to the converged value, taken to be the $T_c$ obtained with $n_{\tilde{L}}=54$.

predicted $T_c$ with respect to the HFSH expansion cutoff $n_{\tilde{L}}$. Interestingly, we verify that convergence is reached very rapidly, obtaining results within 1% of accuracy with as few as 30 HFSHs. This result demonstrates that the HFSH basis set appears extremely beneficial for a precise determination of $T_c$ with a full inclusion of the anisotropy, as the problem is reduced to a small matrix diagonalization for the finite range of temperatures involved in the root finding procedure.

In conclusion, we have presented an efficient numerical scheme to predict superconducting properties from first principles with full account of the electron-phonon anisotropy. We have shown that our method introduces a reduction of several orders of magnitude in the computational workload as compared to the conventional approach, while carrying practically no loss of accuracy. Furthermore, we have demonstrated that our procedure is robust and generally valid for diverse systems, making it readily applicable to the high-throughput exploration of novel superconductors. More generally, the remarkable simplification introduced by our scheme opens the way towards new ab initio and model theoretical treatments since only a few coefficients are sufficient to describe the complexity of the Fermi surface, and even the selection rules are naturally incorporated by construction.

The authors acknowledge the Department of Education, Universities and Research of the Basque Government and the University of the Basque Country UPV/EHU (Grant No. IT756-13), the Spanish Ministry of Economy and Competitiveness MINECO (Grants No. FIS2016-75862-P and No. PID2019-103910GB-I00) and the University of the Basque Country UPV/EHU (Grant No. GIU18/138) for financial support. J.L.-B. acknowledges the University of the Basque Country UPV/EHU (Grant No. PIF/UPV/16/240) and the Donostia International Physics Center (DIPC) for financial support. Computer facilities were provided by the DIPC.

[1] J. Bardeen, L. N. Cooper, and J. R. Schrieffer, *Phys. Rev.* **108**, 1175 (1957).
[2] I. Giaever, H. R. Hart, and K. Megerle, *Phys. Rev.* **126**, 941 (1962).
[3] G. Eliashberg, *Sov. Phys. JETP* **11**, 696 (1960).
[4] D. J. Scalapino, J. R. Schrieffer, and J. W. Wilkins, *Phys. Rev.* **148**, 263 (1966).
[5] J. Nagamatsu, N. Nakagawa, T. Muranaka, Y. Zenitani, and J. Akimitsu, *Nature (London)* **410**, 63 (2001).
[6] F. Bouquet, R. A. Fisher, N. E. Phillips, D. G. Hinks, and J. D. Jorgensen, *Phys. Rev. Lett.* **87**, 047001 (2001).
[7] P. Szabó, P. Samuely, J. Kačmarčík, T. Klein, J. Marcus, D. Fruchart, S. Miraglia, C. Marcenat, and A. G. M. Jansen, *Phys. Rev. Lett.* **87**, 137005 (2001).
[8] S. Tsuda, T. Yokoya, T. Kiss, Y. Takano, K. Togano, H. Kito, H. Ihara, and S. Shin, *Phys. Rev. Lett.* **87**, 177006 (2001).
[9] F. Giubileo, D. Roditchev, W. Sacks, R. Lamy, D. X. Thanh, J. Klein, S. Miraglia, D. Fruchart, J. Marcus, and P. Monod, *Phys. Rev. Lett.* **87**, 177008 (2001).
[10] H. J. Choi, D. Roundy, H. Sun, M. L. Cohen, and S. G. Louie, *Nature (London)* **418**, 758 (2002).
[11] F. Giustino, *Rev. Mod. Phys.* **89**, 015003 (2017).
[12] E. R. Margine and F. Giustino, *Phys. Rev. B* **87**, 024505 (2013).
[13] C. Heil, S. Poncé, H. Lambert, M. Schlipf, E. R. Margine, and F. Giustino, *Phys. Rev. Lett.* **119**, 087003 (2017).

[14] M. Kawamura, R. Akashi, and S. Tsuneyuki, *Phys. Rev. B* **95**, 054506 (2017).

[15] L. Boeri, Understanding novel superconductors with ab initio calculations, in *Handbook of Materials Modeling: Applications: Current and Emerging Materials*, edited by W. Andreoni and S. Yip (Springer International Publishing, Cham, 2020) pp. 73–112.

[16] J. A. Flores-Livas, L. Boeri, A. Sanna, G. Profeta, R. Arita, and M. Eremets, *Physics Reports* **856**, 1 (2020).

[17] C. J. Pickard, I. Errea, and M. I. Eremets, *Annual Review of Condensed Matter Physics* **11**, 57 (2020).

[18] A. P. Drozdov, M. I. Eremets, I. A. Troyan, V. Ksenofontov, and S. I. Shylin, *Nature (London)* **525**, 73 (2015).

[19] A. P. Drozdov, P. P. Kong, V. S. Minkov, S. P. Besedin, M. A. Kuzovnikov, S. Mozaffari, L. Balicas, F. F. Balakirev, D. E. Graf, V. B. Prakapenka, E. Greenberg, D. A. Knyazev, M. Tkacz, and M. I. Eremets, *Nature (London)* **569**, 528 (2019).

[20] M. Somayazulu, M. Ahart, A. K. Mishra, Z. M. Geballe, M. Baldini, Y. Meng, V. V. Struzhkin, and R. J. Hemley, *Phys. Rev. Lett.* **122**, 027001 (2019).

[21] Y. Sun, J. Lv, Y. Xie, H. Liu, and Y. Ma, *Phys. Rev. Lett.* **123**, 097001 (2019).

[22] W. L. McMillan, *Phys. Rev.* **167**, 331 (1968); P. B. Allen and R. C. Dynes, *Phys. Rev. B* **12**, 905 (1975).

[23] P. B. Allen, *Phys. Rev. B* **13**, 1416 (1976).

[24] P. B. Allen and B. Mitrovic, *Theory of Superconducting Tc*, edited by F. Seitz, D. Turnbull, and H. Ehrenreich, Solid State Physics, Vol. 37 (Academic, New York, 1983) pp. 1–92.

[25] A. Eiguren and I. G. Gurtubay, *New Journal of Physics* **16**, 063014 (2014).

[26] J. Lafuente-Bartolome, I. G. Gurtubay, and A. Eiguren, *Phys. Rev. B* **102**, 165113 (2020).

[27] A. B. Migdal, *Sov. Phys. JETP* **16**, 996 (1958).

[28] P. Morel and P. W. Anderson, *Phys. Rev.* **125**, 1263 (1962).

[29] D. Mou, R. Jiang, V. Taufour, S. L. Bud’ko, P. C. Canfield, and A. Kaminski, *Phys. Rev. B* **91**, 214519 (2015).

[30] I. A. Troyan, D. V. Semenok, A. G. Kvashnin, A. V. Sadakov, O. A. Sobolevskiy, V. M. Pudalov, A. G. Ivanova, V. B. Prakapenka, E. Greenberg, A. G. Gavriliuk, V. V. Struzhkin, A. Bergara, I. Errea, R. Bianco, M. Calandra, F. Mauri, L. Monacelli, R. Akashi, and A. R. Oganov, Anomalous high-temperature superconductivity in YH₆ (2020), arXiv:1908.01534 [cond-mat.supr-con].

[31] P. P. Kong, V. S. Minkov, M. A. Kuzovnikov, S. P. Besedin, A. P. Drozdov, S. Mozaffari, L. Balicas, F. F. Balakirev, V. B. Prakapenka, E. Greenberg, D. A. Knyazev, and M. I. Eremets, Superconductivity up to 243 K in yttrium hydrides under high pressure (2019), arXiv:1909.10482 [cond-mat.supr-con].

[32] Y. Li, J. Hao, H. Liu, J. S. Tse, Y. Wang, and Y. Ma, *Scientific Reports* **5**, 9948 (2015).

[33] F. Peng, Y. Sun, C. J. Pickard, R. J. Needs, Q. Wu, and Y. Ma, *Phys. Rev. Lett.* **119**, 107001 (2017).

[34] C. Heil, S. di Cataldo, G. B. Bachelet, and L. Boeri, *Phys. Rev. B* **99**, 220502(R) (2019).