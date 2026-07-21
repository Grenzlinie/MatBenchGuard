# Anisotropy effects in frustrated Heisenberg antiferromagnets on a square lattice

J. Roberto Viana and J. Ricardo de Sousa

Departamento de Física, Universidade Federal do Amazonas, 3000, Japiim, 69077-000, Manaus-AM, Brazil

(Received 22 June 2006; published 6 February 2007)

The anisotropic quantum spin-1/2 Heisenberg antiferromagnet (AF) on the square lattice with nearest ($J_1$) and next-nearest ($J_2$) neighbor couplings ($J_1^{xxz}-J_2$ model or anisotropic $J_1$-$J_2$ model) is studied by using the framework of an effective field theory and effective-field renormalization group approach. In the ground state, two quantum phase transitions are obtained: The second order transition from the Néel state to the spin liquid state (SL) at $\alpha_2(\Delta)$ and the first-order transition from the spin liquid state to the collinear state $(C)$ at $\alpha_1(\Delta)$ (where $\alpha=J_2/J_1$ and $\Delta$ is the spin anisotropy parameter). The two AF-SL and SL-$C$ phase boundaries meet at a critical end point ($\alpha=1/2,\Delta=1$). At finite temperature, the phase diagram in $(T,\alpha)$ plane is obtained for several values of $\Delta$. Between the paramagnetic and collinear phases we have first (low temperature) and second (high temperature) order phase transitions. In the vicinity of the quantum critical point between the AF and SL phases the critical temperature exhibits a reentrant behavior.

DOI: 10.1103/PhysRevB.75.052403
PACS number(s): 75.10.Jm, 05.30.—d, 75.40.Cx

Recently, the study of quantum phase transition has been one of the most interesting topics in the area of strongly correlated systems. Stimulated by the discovery of the cuprate superconductors,¹ the critical properties of the twodimensional quantum spin-1/2 Heisenberg antiferromagnetic model have been exhaustively analyzed.² Experimental evidences, including neutron scattering,³ muon-spin rotation,⁴ and nuclear-quadrupole-resonance technique,⁵ support the fact that magnetism is an important ingredient to the understanding of the behavior of copper-based metallic oxide superconductors (HTS). The possible coexistence of antiferromagnetism and superconductivity is one of the most attracting research fields in the study of HTS. Anderson⁶ originally suggests that quantum spin fluctuations in the $\text{CuO}_2$ planes, common in all these doped cuprates, may be responsible for the superconductivity at high temperatures,¹⁷ where the motion of holes gives rise to effective frustrating couplings in the undoped Heisenberg model and eventually leads to the breakdown of Néel order.

The study of the thermodynamical properties and phase transition of the two-dimensional (2D) Heisenberg model with competing nearest-neighbor (NN) and next-nearestneighbor (NNN) antiferromagnet exchange interactions (i.e., frustration) on a square lattice (the $J_1$-$J_2$ model) have received considerable attention recently,⁸⁻²⁰ where long-range magnetic order is suppressed by enhancing quantum fluctuations. In this work, we study the anisotropic $J_1$-$J_2$ model that is described by the following Hamiltonian:

$$
\begin{aligned}
\mathcal{H}=J_{1} \sum_{n n}\left[(1-\Delta)\left(\sigma_{i}^{x} \sigma_{j}^{x}+\sigma_{i}^{y} \sigma_{j}^{y}\right)+\sigma_{i}^{z} \sigma_{j}^{z}\right]+J_{2} \sum_{n n n} \boldsymbol{\sigma}_{i} \cdot \boldsymbol{\sigma}_{j}, \\
(1)
\end{aligned}
$$

where $\sigma_{i}^{\mu}$ is the $\mu$ ($=x,y,z$) component of the spin-1/2 Pauli operators at site $i$ on the square lattice. The first and second sum run over the nearest-neighbor (NN) and next-nearestneighbor (NNN) spin pairs, respectively, $\Delta \in [0,1]$ represents the anisotropy parameter only for the NN interactions, and the subscript $i$ ($j$) denotes sites on the $A$ ($B$) sublattice.

In the absence of anisotropy ($\Delta=0$), the quantum spin1/2 $J_1$-$J_2$ model on a square lattice is a theoretical realistic prototype to analyze the spin-liquid ground state. For $J_2$=0, the two sublattice are disconnected and the ground state is believed to have an antiferromagnetic (AF) order. The NNN exchange interactions are expected to induce strong frustration to break the AF order and to form a disordered ground state around $\alpha \simeq 0.38$ ($\alpha=J_2/J_1$). It is suggested that for $0.38 \leq \alpha \leq 0.60$ there is a nonmagnetic gapped phase.⁸²¹ The exact nature of this ground state turns out to be one of the most challenging problems for physics of frustrated spin systems. There have been a number of different proposals, for example, the spin-Peierls state,²² the plaquette state,²³ a chiral-spin state, ²⁴ etc., but the proposal of the spin-liquid state appears to be the most promising candidate.¹⁵ For $\alpha < \alpha_{2c} \simeq 0.38$ an AF state should develop, whereas for $\alpha > \alpha_{1c} \simeq 0.60$ the ordering by the disorder mechanism¹⁵ˡ¹⁶ is expected to stabilize a twofold degenerate collinear order, with spins aligned ferromagnetically along the $x$ axis and antiferromagnetically along the $y$ axis, or vice versa.

From a theoretical point of view it is known that in the two-dimensional model with continuous spin-rotational symmetry, the symmetry cannot be broken at any finite temperature,²⁵ and only models with a discrete symmetry can show a finite-temperature phase transition. The motivation of studying spin anisotropies in quantum models is because of its presence in real materials, and also show a rich phase diagram. The anisotropy in model (1) eventually leads to three-dimensional (3D) long-range order and a finitetemperature transition. For the model (1) only with NN interactions ($J_2$=0), we have a finite temperature phase transition when the anisotropy parameter is not zero ($\Delta \neq 0$). Moreover, quantum Monte Carlo simulation²⁶ indicates that the critical temperature presents the following asymptotic behavior $T_c \simeq A/\ln(1/\Delta)$ when $\Delta \to 0^+$, and reproduce the exact value $T_c$=0 in the isotropic limit ($\Delta=0$) in complete agreement with the Mermin-Wagner theorem.²⁵ It has been argued by Chandra *et al.*,¹⁰ and recently observed in numerical simulations,¹¹ that the presence of frustrating interactions can induce nontrivial discrete degrees of freedom that may un-

![](./images/812020638515462144_1.jpg)

FIG. 1. Schematic representation of the two spin cluster used in effective field theory (EFT-2).

dergo a phase transition at low temperatures. In particular, the isotropic $J_{1}$-$J_{2}$ model, i.e., Eq. (1) with $\Delta=0$, the critical temperature$T_{c}$ increases for $\alpha>\alpha_{1c}$ and when $\alpha \to \alpha_{1c}$ we have $T_{c} \to 0$ with an infinite slope. There is also a strong numerical evidence for the classical system $(S \to \infty)$ (Ref. 12) that this transition is in the same as the two-dimensional (2D) Ising universality class.

The ground-state phase diagram of the classical $(S \to \infty)$ isotropic $J_{1}$-$J_{2}$ model on a square lattice separates into two regions: For $\alpha<1 / 2$ the ground state is a Néel state (AF), while for $\alpha>1 / 2$ we have the collinear state $(C)$. For $\alpha$ $=1 / 2$ (strongly frustrated limit), the degeneracy of the ground state is large, and there is a consensus of the nonex-istence of the spin-liquid state. According to spin wave theory, $^{8}$ the classical critical point $\alpha_{c}=1 / 2$ marks the first transition between the collinear and Néel phases. Quantum fluctuations can modify drastically the critical behavior, in-ducing, for example, the existence of the spin-liquid state inthe isotropic quantum spin-1/2 $J_{1}$-$J_{2}$ model. $^{15}$

For small $J_{2}$ values, the isotropic quantum spin-1/2 $J_{1}$-$J_{2}$ model has been used to describe magnetic properties of the cuprates materials $^{2}$ and, more recently, the materials $Li_{2}VOSiO_{4}$ and $Li_{2}VOGeO_{4}$ can also be described by the model for the case of large $J_{2}$ (i.e., $J_{2} \simeq J_{1}$ ). $^{14}$ These two isostructural compounds are characterized by a layered structure containing $V^{4+}(S=1 / 2)$ ions. $^{27}$ The structures of $V^{4+}$ layer suggest that the superexchange is similar. At $T_{c}$ $\simeq 2.8 ~K$ a phase transition to a low-temperature collinear or der is observed.

Some years ago, a simple and versatile scheme, denoted by differential operator technique, $^{28}$ was proposed and ap plied exhaustively to study a large variety of problems. In particular, this technique was used to treat the criticality of quantum models $^{29}$ obtaining satisfactory qualitative results in comparison with more sophisticated methods (for example, Monte Carlo simulation). This method is used in conjugation with a decoupling procedure which ignores all high-order spin correlations [effective field theory-(EFT)].

In order to study the quantum phase transition of the Hamiltonian (1) we use the effective-field theory in cluster with two spins (denoted by EFT-2), as indicated in Fig. 1, that was previously developed in Ref. 27 for the case $J_{2}=0$. In this scheme, the magnetization $m_{A}$ in sublattice $A$ is given by
$$m_{A}=\hat{\Lambda}_{1 x} \cdot \hat{\Lambda}_{2 y} \cdot \hat{\Lambda}_{2} \cdot \hat{\Lambda}_{3} g(x, y)\big|_{x, y=0},\qquad(2)$$
with
$$\hat{\Lambda}_{r \nu}=\left(\alpha_{1 x}-m_{\nu B} \beta_{1 x}\right)^{r}\left(\alpha_{1 y}-m_{\nu A} \beta_{1 y}\right)^{r},\qquad(3)$$

$$\hat{\Lambda}_{2}=\left(\alpha_{2 x}-m_{y A} \beta_{2 x}\right)^{2}\left(\alpha_{2 y}-m_{y B} \beta_{2 y}\right)^{2},\qquad(4)$$

$$\hat{\Lambda}_{3}=\left(\alpha_{x y}-m_{y A} \beta_{x y}\right)^{2}\left(\alpha_{y x}-m_{y B} \beta_{y x}\right)^{2},\qquad(5)$$
and
$$g(x, y)=\frac{\sinh (x+y)+\frac{(x-y) e^{2 K_{1}}}{W(x, y)} \sinh W(x, y)}{\cosh (x+y)+e^{2 K_{1}} \cosh W(x, y)},\qquad(6)$$
where $W(x, y)=\sqrt{(x-y)^{2}+4 K_{1}^{2}(1-\Delta)^{2}}, \alpha_{r \nu}=cosh(K_{r} D_{\nu}), \beta_{r \nu}$ $=\sinh (K_{r} D_{\nu}), \alpha_{x y}=\alpha_{1 x} \alpha_{2 y}+\beta_{1 x} \beta_{2 y}, \beta_{x y}=\alpha_{1 x} \beta_{2 y}+\beta_{1 x} \alpha_{2 y}$ , and $m_{x \mu}(m_{y \mu})$ is the magnetization in sublattice $\mu=A, B$ in the x(y) direction.

In this work we have used the effective-field renormaliza-tion group (EFRG) approach with clusters with one and two spins, preliminarily developed in the Ising model, $^{30}$ to obtain the second-order phase transition boundaries between the F(AF) and SL phase (or disordered) of the anisotropic $J_{1}$-$J_{2}$ model. Between the collinear $(C)$ and SL phases the effective-field theory with cluster with two spins (EFT-2) is used. We observe the same qualitative results for the ground state phase diagram as that of the AF case. However, the critical parameter is higher [i.e., $\alpha_{rF}(\Delta)<\alpha_{rAF}(\Delta)$ , for r=1,2], and this difference rapidly decreases as $S$ increased.For $J_{2}=0$ , the EFRG method has been previously applied $^{31,32}$ to study the anisotropic Heisenberg model in two- and three dimensional lattices, where the results for the critical prop erties are in accordance with the values obtained by Monte Carlo simulations.

The ground state phase diagram of the anisotropic $J_{1}$-$J_{2}$ model is shown in Fig. 2. We found three phases character ized by different order parameters $m_{\nu \mu}(\nu=x, y ; \mu=A, B)$ ,namely: (i) Néel phase $(N)$ with $m_{\nu B}=-m_{\nu A}=-m_{A}$ for all $\nu$  $=x, y$ , (ii) collinear phase $(C)$ with $m_{x A}=m_{x B}=m_{A}$ and $m_{y A}$  $=m_{y B}=-m_{A}$ , and (iii) quantum spin-liquid phase (SL) with $m_{\nu A}=m_{\nu B}=m_{A}=0$ . The $N$ and SL phases are separated by a second-order transition line $\alpha_{2 AF}(\Delta)$ , while the SL and $C$ phases by a first-order transition line $\alpha_{1 AF}(\Delta)$ . The presence of the exchange anisotropy $(\Delta)$ has the general effect of de stroying the SL phase. The disordered (SL) region decreases with the increase of the anisotropy parameter, and disappear with gapless spin excitations in the Ising limit $(\Delta=1)$ . The boundaries between these phases merge at the critical end point $(\Delta=1, \alpha=1 / 2)$ . Presence of first-order quantum phase transitions has been observed in various systems; see, for example Ferreira et al. $^{33}$ The study of the first-order transi tion line has been performed by making use of an order parameter analysis. We obtain a qualitative estimate of the phase boundaries from the infinity of the first derivatives $d m_{A} / d T$ [i.e., at $T=T_{c}^{*}(\Delta, \alpha)$ we have $d m_{A} / d T \to \infty$ , there fore, $\alpha_{1 ~F, AF}(\Delta)$ is estimated with the limit of $T_{c}^{*}=0]$ . In this way we have obtained the ground state phase diagram in Fig.2. In the isotropic limit $(\Delta=0)$ , we found $\alpha_{1 AF}(0)=0.67$ for the antiferromagnetic $J_{1}$-$J_{2}$ model that can be compared with other methods, as, for example, $\alpha_{1 AF}(0) \simeq 0.60$ obtained in

![](./images/812020638515462144_2.jpg)

FIG. 2. Ground state phase diagram in $(\alpha,\Delta)$ plane for the anisotropic $J_1$-$J_2$ model with ferromagnetic (antiferromagnetic) nearest-neighbor exchange interaction. The solid and dashed lines are continuous and first-order phase boundaries, respectively. The coordinates of the critical end point are $(1/2,1)$. The critical line between the F(AF) and SL phases is indicated by $\alpha_{2\mathrm{F}}(\Delta)$ [$\alpha_{2\mathrm{AF}}(\Delta)$] and the first-order line by $\alpha_{1\mathrm{F}}(\Delta)$ [$\alpha_{1\mathrm{AF}}(\Delta)$], respectively.

Ref. 21. On the other hand, the case of the ferromagnetic $J_1$-$J_2$ model has not been analyzed in the literature, as far as we know.

For the classical spin $(S\to\infty)$ we have no quantum fluctuations and for the anisotropic $J_1$-$J_2$ model only two phases ($N$ and $C$) are present, where the first-order transition line $\alpha_{1c}(\Delta)=1/2$ is independent of $\Delta$. More recently, perturbative numerical renormalization group analysis has shown no evidence of the spin-liquid phase and it has been proposed that a direct and unexpected second-order phase transition may occur at the classical critical point. $^{33}$

In classical spin models such as the Ising and Heisenberg own, the critical properties are the same for the ferromagnetic $(J_1<0)$ and antiferromagnetic $(J_1>0)$ exchange interactions between the nearest neighbors. $^{33}$ In the absence of longitudinal magnetic field parallel to the easy axis magnetization, some quantum systems such as the quantum spin-1/2 transverse Ising and $XY$ models demonstrate isomorphism of the critical properties of the ferromagnetic and antiferromagnetic systems. Therefore, the $J_1$-$J_2$ model with classical spin or Ising limit ($\Delta=1$) are equivalent to the F and AF systems (same phase diagram) in the absence of magnetic field. The F phase is characterized at $T=0$ by $m_{\nu\mu}=m$ for all $\nu=A,B$ and $\mu=x,y$. We also study the anisotropic $J_1$-$J_2$ model with ferromagnetic (i.e., $J_1<0$) interaction between the nearest neighbors and the results are presented in Fig. 2.

At finite temperature, by using the equation of state (2), we calculate numerically the behavior of the order parameter as a function of temperature for different values of $\Delta$ and $\alpha$. The critical temperature or second-order phase transition temperatures are obtained when $m_A\to0$, i.e., we obtain $T_c(\Delta,\alpha)$. When increasing the temperature, the line separating the paramagnetic and the collinear phase is a first-order line (dashed line) for $\alpha$ between $\alpha_{1c}(\Delta)\geq1/2$ and $\alpha_t(\Delta)$, where $\alpha_t(\Delta)$ correspond to the tricritical frustration parameter and $T_t(\Delta)$ the tricritical temperature. The first-order transition temperature $T_c^*(\Delta,\alpha)$ is located (approximate) by the analysis of the first derivatives $dm_A/dT\to\infty$. For $\alpha>\alpha_t(\Delta)$ we have a second-order line, with a linear behavior for the critical temperature [i.e., $T_c\simeq a(\alpha-\alpha_t)$]. In the antiferromagnetic phase, the critical temperature $T_c(\alpha)$ [second-order phase transition for all values of $\alpha<\alpha_{2c}(\Delta)$] increases when the frustration parameter decreases. For the Ising limit ($\Delta=1$), in the classical point $\alpha=\alpha_{1c}(1)=\alpha_{2c}(1)=1/2$ the critical temperature $T_c$ vanishes, and only the $P$, AF, and $C$ phases are present.

![](./images/812020638515462144_3.jpg)

FIG. 3. Phase diagram of the anisotropic $J_1$-$J_2$ antiferromagnetic model in $(T,\alpha)$ plane for the $\Delta=1$ (Ising model), $\Delta=0.5$, and $\Delta=0$ (isotropic Heisenberg) limits. The solid and dashed lines are continuous and first-order phase boundaries, respectively. The tricritical points are shown for the $\Delta=1$, $\Delta=0.5$, and $\Delta=0$ cases. The antiferromagnetic, paramagnetic, and collinear phases are indicated in the phase diagram by AF, $P$, and $C$, respectively.

On the other hand, our analysis for $0<\Delta<1$ suggests that in the vicinity of the quantum critical point $\alpha\simeq\alpha_{2c}(\Delta)$, the second-order transition line shows a reentrant behavior at finite temperature, and for the isotropic limit ($\Delta=0$) only the Néel order is observed at $T=0$ (ground state). The results of $T_c$ versus $\alpha$ for different values of anisotropy parameter (we chose the values $\Delta=0$, 0.5, and 1.0) are reported in Fig. 3. In particular, for a sufficiently small value of $\alpha$ [i.e., around quantum critical point $\alpha_{1c}(\Delta)$] we observe first-order phase transition. At the quantum critical points $\alpha_{1c}(\Delta)$ and $\alpha_{2c}(\Delta)$ we have $T_c\to0$ with an infinite slope and a reentrant second-order transition line (between the AF and $P$ phases). We notice that reentrant behavior in quantum phase transition have recently been observed in magnetic $^{18}$ and bosonic $^{34}$ systems. Finally, we mention that our results differ from those obtained by Roscilde et al., $^{18}$ where the case of the $J_1$-$J_2$ model with NNN anisotropic interaction has been analyzed and the reentrant behavior was observed in the $C$ phase. In this work the reentrant behavior is predicted only in the $N$ phase.

In summary, we have studied the phase diagram of the

frustrated quantum spin-1/2 Heisenberg antiferromagnetic model on the square lattice with anisotropic next-neighbor interaction by using effective-field theory. The ground state phase diagram in $(\alpha,\Delta)$ plane shows three phases, namely AF, $C$, and SL. The spin-liquid phase is present in the interval of $0\leq\Delta<1$, and for the classical limit (Ising and classical Heisenberg models) only the AF $(\alpha<1/2)$ and $C$ $(\alpha>1/2)$ phases appear with the presence of a first-order phase transition at the phase transition point $\alpha=1/2$. We have proposed an alternative scheme to obtain the first-order transition line using the present EFT approach, that is based in the analysis of the temperature dependence order parameter in the collinear phase. This approach (EFT) to obtain the first-order transition lines is equivalent (error of $2\%$) to the study of the free energy stability (Maxwell construction method). Tricritical points was observed in the phase diagram $T$ versus $\alpha$ for all values of $\Delta\in[0,1]$ between the $C$ and $P$ phases. For the quantum regime $(\Delta\neq1)$, we observe a possible spin-liquid state (or disordered) at zero temperature, with existence of two quantum critical points $\alpha_{1c}(\Delta)$ and $\alpha_{2c}(\Delta)$ separating the collinear-SL (first-order) and AF-SL (second-order) phases, respectively. This EFT solution has reproduced the correct asymptotic behavior in the high frustration limits $[\alpha\geq\alpha_{1c}(\Delta)]$, exhibiting a nontrivial (no usual) reentrant behavior at low temperature in the AF phase. The critical behavior for the Ising model is in agreement with rigorous results of Monte Carlo simulation. Therefore, we expect that our results for the quantum system are qualitatively correct. A thorough Monte Carlo study for the quantum spin-1/2 anisotropic $J_1$-$J_2$ model would also appear very worthwhile. To our knowledge, no such studies have been attempted.

The authors acknowledge valuable discussions with Dr. J. A. Plascak of the Universidade Federal Minas Gerais and Dr. Angsula Ghosh of the Universidade Federal do Amazonas. This work was partially supported by CNPq, FAPEAM, and CAPES (Brazilian agencies).

---

$^{1}$J. G. Bednorz and K. A. Müller, Z. Phys. B: Condens. Matter 64, 189 (1986).

$^{2}$E. Manousakis, Rev. Mod. Phys. 63, 1 (1991).

$^{3}$D. Vaknin, S. K. Sinha, D. E. Moncton, D. C. Johnston, J. M. Newsam, C. R. Safinya, and H. E. King, Jr., Phys. Rev. Lett. 58, 2802 (1987).

$^{4}$G. Shirane, Y. Endoh, R. J. Birgeneau, M. A. Kastner, Y. Hidaka, M. Oda, M. Suzuki, and T. Murakami, Phys. Rev. Lett. 59, 1613 (1987); N. Nishida *et al.*, Jpn. J. Appl. Phys., Part 2 26, L1856 (1987).

$^{5}$Y. Kitaoka, K. Ishida, S. Hiramatsu, and K. Asayama, J. Phys. Soc. Jpn. 57, 734 (1988).

$^{6}$P. W. Anderson, Science 235, 1196 (1987).

$^{7}$C. W. Chu, P. H. Hor, R. L. Meng, L. Gao, Z. J. Huang, and Y. Q. Wang, Phys. Rev. Lett. 58, 405 (1987).

$^{8}$P. Chandra and B. Doucot, Phys. Rev. B 38, 9335 (1988); L. B. Ioffe and A. I. Larkin, Mod. Phys. Lett. B 2, 203 (1998).

$^{9}$N. B. Ivanov and J. Richter, J. Phys.: Condens. Matter 6, 3785 (1994).

$^{10}$P. Chandra, P. Coleman, and A. I. Larkin, Phys. Rev. Lett. 64, 88 (1990).

$^{11}$L. Capriotti, A. Fubini, T. Roscilde, and V. Tognetti, Phys. Rev. Lett. 92, 157202 (2004).

$^{12}$C. Weber, F. Becca, and F. Mila, Phys. Rev. B 72, 024449 (2005), and references therein.

$^{13}$L. Spanu and A. Parola, Phys. Rev. B 72, 174418 (2005); V. Lante and A. Parola, ibid. 73, 094427 (2006).

$^{14}$H. Rosner, R. R. P. Singh, W. H. Zheng, J. Oitmaa, and W. E. Pickett, Phys. Rev. B 67, 014416 (2003); J. Sirker, Zheng Weihong, O. P. Sushkov, and J. Oitmaa, ibid. 73, 184420 (2006).

$^{15}$Guang-Ming Zhang, Hui Hu, and Lu Yu, Phys. Rev. Lett. 91, 067201 (2003).

$^{16}$F. Becca and F. Mila, Phys. Rev. Lett. 89, 037204 (2002).

$^{17}$P. Sindzingre, Phys. Rev. B 69, 094418 (2004).

$^{18}$T. Roscilde, P. Verrucchi, A. Fubmi, S. Haas, and V. Tognetti, Phys. Rev. Lett. 93, 167203 (2004).

$^{19}$R. R. P. Singh, W. Zheng, J. Oitmaa, O. P. Sushkov, and C. J. Hamer, Phys. Rev. Lett. 91, 017201 (2003); J. Sirker, Zheng Weihong, O. P. Sushkov, and J. Oitmaa, Phys. Rev. B 73, 184420 (2006).

$^{20}$R. Darradi, J. Richter, and D. J. J. Farnell, Phys. Rev. B 72, 104425 (2005).

$^{21}$O. P. Sushkov, J. Oitmaa, and Z. Weihong, Phys. Rev. B 63, 104420 (2001); L. Capriotti, Int. J. Mod. Phys. B 15, 1799 (2001); X. G. Wen, Phys. Rev. B 44, 2664 (1991).

$^{22}$E. Dagotto and A. Moreo, Phys. Rev. Lett. 63, 2148 (1989).

$^{23}$M. E. Zhitomirsky and K. Ueda, Phys. Rev. B 54, 9007 (1996).

$^{24}$V. Kalmeyer and R. B. Laughlin, Phys. Rev. Lett. 59, 2095 (1987).

$^{25}$N. D. Mermin and H. Wagner, Phys. Rev. Lett. 17, 1133 (1966).

$^{26}$A. Cuccoli, T. Roscilde, V. Tognetti, R. Vaia, and P. Verrucchi, Phys. Rev. B 67, 104414 (2003).

$^{27}$P. Carretta, R. Melzi, N. Papinutto, and P. Millet, Phys. Rev. Lett. 88, 047601 (2002); H. Rosner, R. R. P. Singh, W. H. Zheng, J. Oitmaa, S. -L. Drechsler, and W. E. Pickett, ibid. 88, 186405 (2002), R. Melzi, P. Carretta, A. Lascialfari, M. Mambrini, M. Troyer, P. Millet, and F. Mila, ibid. 85, 1318 (2000).

$^{28}$R. Honmura and T. Kaneyoshi, J. Phys. C 12, 3979 (1979).

$^{29}$J. Cabral Neto and J. Ricardo de Sousa, Phys. Lett. A 336, 274 (2005); Minos A. Neto and J. Ricardo de Sousa, ibid. 330, 322 (2004); Edgar Bublitz Filho and J. Ricardo de Sousa, ibid. 323, 9 (2004).

$^{30}$I. P. Fittipaldi, J. Magn. Magn. Mater. 131, 43 (1994).

$^{31}$J. Ricardo de Sousa and I. P. Fittipaldi, J. Appl. Phys. 75, 5835 (1994); J. Ricardo de Sousa and Ijanílio G. de Araújo, J. Magn. Magn. Mater. 16, 8653 (1999).

$^{32}$A. S. Ferreira, M. A. Continentino, and E. C. Marino, Phys. Rev. B 70, 174507 (2004).

$^{33}$S. Moukouri, cond-mat/0504306 (unpublished). See also S. Moukouri, Phys. Lett. A 352, 256 (2006).

$^{34}$G. Schmid, S. Todo, M. Troyer, and A. Dorneich, Phys. Rev. Lett. 88, 167208 (2002).

052403-4