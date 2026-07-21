# Breakdown of a Magnetization Plateau due to Anisotropy in Heisenberg Mixed-Spin Chains
Shoji Yamamoto
Department of Physics, Okayama University, Tsushima, Okayama 700-8530, Japan

Tôru Sakai
Faculty of Science, Himeji Institute of Technology, Ako, Hyogo 678-1297, Japan
(18 March 1999)

We discuss the critical behavior of the spin-$(1, \frac{1}{2})$ Heisenberg ferrimagnetic chain in a magnetic field, whose magnetization curve exhibits a plateau at a third of the full magnetization. A bond alternation stabilizes the massive state, whereas an exchange anisotropy causes the breakdown of the plateau and the onset of a gapless spin-fluid state, where the transition, lying in the $XY$ but ferromagnetic region, is of Kosterlitz-Thouless type. In order to elucidate significant quantum effects, we investigate the model of classical version as well.

PACS numbers: 75.10.Jm, 75.40Mg, 75.30.Kz

## I. INTRODUCTION

Ground-state magnetization curves of quantum spin chains have been attracting much current interest due to their quantized plateaux as functions of a magnetic field. Several years ago Hida [1] revealed that a spin-$\frac{1}{2}$ ferromagnetic-antiferromagnetic-antiferromagnetic trimerized chain exhibits a plateau in its magnetization curve at a third of the full magnetization. Although it was already familiar that, in the presence of a field, integer-spin Heisenberg antiferromagnetic chains remain massive from zero field up to a critical field [2], yet the magnetization plateau at a fractional value of the full magnetization was still met with a surprise. Since then various low-dimensional quantum spin systems in a field have been investigated, including polymerized spin chains [3-8], spin chains with anisotropy [9] or four-spin exchange coupling [10], and decorated spin ladders [11-13]. Experimental observations [14,15] of quantized magnetization plateaux have also been reported. In such circumstances, generalizing the Lieb-Schultz-Mattis theorem [16,17], Oshikawa, Yamanaka, and Affleck (OYA) [18] found a criterion for the fractional quantization. They pointed out that quantized plateaux in magnetization curves may appear under the condition
$$
S_{\text{unit}} - m = \text{integer}, \tag{1.1}
$$
where $S_{\text{unit}}$ is the sum of spins over all sites in the unit period and $m$ is the magnetization $M$ divided by the number of the unit cells.

Mixed-spin chains are the system of all others that stimulates us in this context. There exists a large amount of chemical knowledge [19] on quantum ferrimagnets. In an attempt to realize a quasi-one-dimensional ferrimagnetic system, Gleizes and Verdaguer [20] synthesized a few bimetallic compounds such as $\text{AMn(S}_2\text{C}_2\text{O}_2\text{)}_2(\text{H}_2\text{O})_3\text{·4.5H}_2\text{O}$ (A = Cu, Ni, Pd, Pt). Then numerous chemical explorations [21,22] followed and various examples of a ferrimagnetic one-dimensional compound were systematically obtained. The vigorous experimental research motivated theoretical investigations into Heisenberg ferrimagnets. Drillon et al. [23] pioneeringly carried out numerical diagonalizations of spin-$(S, \frac{1}{2})$ Heisenberg Hamiltonians for $S = 1$ to $\frac{5}{2}$ and revealed typical thermodynamic properties of ferrimagnetic mixed-spin chains. In recent years, quantum ferrimagnets have met with further theoretical understanding [24-34] owing to various tools such as field [24,34] and spin-wave [25,26,32,33] theories, matrix-product formalism [27,28], and quantum Monte Carlo [26,29,32] and density-matrix renormalization-group [25,30,32] techniques. In particular, their mixed nature, showing both ferromagnetic and antiferromagnetic aspects [32], has lately attracted considerable attention.

However, little is known about quantum ferrimagnetic behavior in a magnetic field [27], especially about magnetization curves [31]. Although anisotropy is an interesting and important factor from an experimental point of view, there exist few arguments on anisotropic models in a field. Now, considering the OYA argument and the accumulated chemical knowledge on ferrimagnetic compounds, the magnetization process of realistic mixed-spin-chain models arouses our interest all the more and indeed deserves urgent communication. In an attempt to serve as guides for further experimental study, we here consider an alignment of alternating spins $S$ and $s$ in a field, as described by the Hamiltonian
$$
\mathcal{H} = \sum_{j=1}^N \left[(\boldsymbol{S}_j \cdot \boldsymbol{s}_j)_\alpha + \delta(\boldsymbol{s}_j \cdot \boldsymbol{S}_{j+1})_\alpha - H(S_j^z + s_j^z)\right],
\tag{1.2}
$$
where $(\boldsymbol{S} \cdot \boldsymbol{s})_\alpha = S^x s^x + S^y s^y + \alpha S^z s^z$. We note that even the bond alternation $\delta$ is now experimentally adjustable [22]. According to the OYA criterion (1.1), as $H$ increases from zero to the saturation field

$$
\begin{aligned}
H_{\mathrm{sat}}=\frac{1}{2}(1+\delta)\left[\alpha(S+s)+\sqrt{\alpha^{2}(S-s)^{2}+4 S s}\right], \\
(1.3)
\end{aligned}
$$

the model (1.2) may exhibit quantized plateaux at $m=\frac{1}{2}$ (1), $\frac{3}{2}(2), \cdots, S+s-1$. Though a multi-plateau problem is a fascinating subject, we restrict our argument to the simplest case of $(S, s)=\left(1, \frac{1}{2}\right)$ in the following. This is, on the one hand, because we at first aim at understanding the typical and essential behavior of quantum ferrimagnets in a field, and, on the other hand, because the low-energy structure of the model (1.2) remains qualitatively the same [24,32] as long as $S \neq s$. Then, a plateau is expected at $m=\frac{1}{2}$. At the Heisenberg point, the ground state of the Hamiltonian (1.2) without field is a multiplet of spin $N / 2$ [35]. The ferromagnetic excitations, reducing the ground-state magnetization, exhibit a gapless dispersion relation, whereas the antiferromagnetic ones, enhancing the ground-state magnetization, are gapped from the ground state [29]. Therefore, at the isotropic point, $m$ jumps up to $\frac{1}{2}$ just as a field is applied and forms a plateau for $H_{\mathrm{c} 1} \leq H \leq H_{\mathrm{c} 2}$ [31], where $H_{\mathrm{c} 1}$ and $H_{\mathrm{c} 2}$ are the lower and upper critical fields, equal to 0 and the antiferromagnetic gap, respectively.

![](./images/867753078202302621_1.jpg)

FIG. 1. Schematic view of the low-energy structure of the spin- $(1, \frac{1}{2})$ quantum ferrimagnetic chain with anisotropic exchange coupling near the Heisenberg point $\alpha=1$ : (a) the Ising region $\alpha>1$ and (b) the $X Y$ region $\alpha<1$.

In the presence of exchange anisotropy, the above argument should be modified, where the $(N+1)$-fold degenerate ground-state multiplet splits [24,30], as illustrated in Fig. 1. In the Ising region, the ground state is a doublet of $M= \pm N / 2$ and therefore $H_{\mathrm{c} 1}$ remains 0 . As $\alpha$ increases, $H_{\mathrm{c} 2}$ comes to be given as $(1+\delta) \alpha$ and the magnetization curve ends up with a trivial step. Thus we take little interest in this region. In the $X Y$ region, on the other hand, the ground state is a singlet of $M=0$. Now $H_{\mathrm{c} 1}$ moves away from 0 and the plateau shrinks as $\alpha$ decreases (see Fig. 2 below). Here arises a stimulative problem: how stable the plateau is against the anisotropy and what comes over the plateau phase? In this article, we demonstrate that the plateau survives the $X Y$ anisotropy in the entire antiferromagnetic region and vanishes in the ferromagnetic region. The transition is of Kosterlitz-Thouless (KT) type [36] and a gapless spin-fluid phase [37] appears instead.

![](./images/867753078202302621_2.jpg)

FIG. 2. The ground-state magnetization curves for the quantum Hamiltonian (1.2) at various values of $\alpha$ : (a) $\delta=1$ and (b) $\delta=0.6$.

![](./images/867753078202302621_3.jpg)

FIG. 3. (a) Scaled quantity $N \Delta_{N}$ versus $\alpha$ at $\delta=1$ and $\delta=0.6$. (b) The central charge $c$ and the critical exponent $\eta$ versus $\alpha$ in the vicinity of the phase boundary at $\delta=1$ and $\delta=0.6$.

## II. SCALING ANALYSIS

We numerically diagonalize finite clusters up to $N=12$ and analyze the data obtained employing a scaling technique [9,38]. Suppose a field is applied to the cluster of $N$ unit cells, a magnetization, let us say, $M$, is induced in the ground state. In this sense we represent a field as a function of $N$ and $M$: $H(N,M)$. Even though $M$, as well as $N$, is given, $H(N,M)$ is not in general unique. The upper and lower bounds of $H(N,M)$ are, respectively, given by

$$
H_{+}(N, M)=E(N, M+1)-E(N, M), \tag{2.1}
$$

$$
H_{-}(N, M)=E(N, M)-E(N, M-1), \tag{2.2}
$$

where $E(N,M)$ is the lowest energy in the subspace labeled $M$ of the Hamiltonian (1.2) without the Zeeman term. If the system is massive at the sector labeled $M$, $H_{\pm}(N,M)$ should approach different values $H_{\pm}(m)$, respectively, as $N \to \infty$, which can be estimated by the Shanks' extrapolation [39]. In the critical system, on the other hand, $H_{\pm}(N,M)$ should converge to the same value as [40,41]

$$
H_{\pm}(N, M) \sim H(m) \pm \frac{\pi v_{\mathrm{s}} \eta}{N} \quad(N \rightarrow \infty), \tag{2.3}
$$

where $v_{\mathrm{s}}$ is the sound velocity and $\eta$ is the critical index defined as $\langle\sigma_{0}^{+} \sigma_{r}^{-}\rangle \sim(-1)^{r} r^{-\eta}$ with a relevant spin operator $\sigma$, which may here be a certain linear combination of $\boldsymbol{S}$ and $\boldsymbol{s}$.

In Fig. 2 we show thus-obtained thermodynamic-limit magnetization-versus-field curves, where we smoothly interpolate the raw data $H(m)$ for the sake of guiding eyes. We might expect that the bond alternation simply makes the plateau grow because the magnetization curve becomes stepwise as $\delta \to 0$. However, this naive idea is not true in general. In the vicinity of the Ising limit $\alpha \to \infty$, the plateau length behaves as $(1+\delta)\alpha$ and thus the bond alternation makes the plateau shrink. Around the Heisenberg point $\alpha=1$, this picture seems to be still valid in part but the precise scenario is not so simple. At the Heisenberg point, for example, the antiferromagnetic excitation gap, that is, the gap between the ground state and the lowest level in the subspace with $M=N/2+1$, is not a monotonic function of $\delta$ (Table I). On the other hand, near the $XY$ point $\alpha=0$, the plateau seems to grow monotonically with the bond alternation.

Once $\delta$ is given, the plateau length is monotonically reduced with the decrease of $\alpha$. The system is gapless at every sector of the Hilbert space in the ferromagnetically ordered region $\alpha \leq -1$ and is thus supposed to encounter a phase transition going through the $XY$ region $-1 < \alpha < 1$. It is surprising that the plateau still exists at the $XY$ point. We will show later that such a stable plateau is peculiar to quantum spins, while, for classical spins, only a slight anisotropy of $XY$ type breaks the plateau.

![](./images/867753078202302621_4.jpg)

FIG. 4. Phase diagram of the spin-$(1,\frac{1}{2})$ quantum ferri- magnetic chain (1.2) at the absolute zero temperature. The phase boundary determined by the critical index $\eta$ is shown by a solid line, whereas the PRG estimate by a dotted line. The dominant error for the PRG result occurs in extrapolating $\alpha_{\mathrm{c}}(N,N+2)$ to the $N \to \infty$ limit rather than originates from the numerical diagonalization.

The plateau length $\Delta_{N}=H_{+}(N,M)-H_{-}(N,M)$ is a relevant order parameter to detect the phase boundary. The scaling relation (2.3) suggests that $\Delta_{N}$ should be proportional to $1/N$ in the critical system. We plot in Fig. 3(a) the scaled quantity $N\Delta_{N}$ as a function of $\alpha$. $N\Delta_{N}$ looks independent of $N$ beyond a certain value of $\alpha$, showing an aspect of the KT transition. The central charge $c$ of the critical phase can be extracted from the scaling relation of the ground-state energy:

$$
\frac{E(N, M)}{N} \sim \varepsilon(m)-\frac{\pi c v_{\mathrm{s}}}{N^{2}} \quad(N \rightarrow \infty). \tag{2.4}
$$

Due to the small correlation length [25,26] of the present system, we can directly and precisely estimate $v_{\mathrm{s}}$ from the dispersion curves. In Fig. 3(b) we plot $c$ versus $\alpha$ and find that $c$ approaches unity as the system goes toward the critical region. Assuming the asymptotic formula $\Delta_{N} \sim 2\pi v_{\mathrm{s}}\eta/N$, we can further evaluate the critical exponent $\eta$, which is also shown in Fig. 3(b). Figure 3 fully convinces us of the KT universality of this phase transition. The phase boundary is obtained by tracing the points of $\eta=\frac{1}{4}$ [42] and is shown in Fig. 4 by a solid line. On the other hand, we have another numerical tool, the phenomenological renormalization-group (PRG) technique [43], to determine the phase boundary. At each $\delta$, the PRG equation

$$
(N+2)\Delta_{N+2}(\alpha, \delta)=N\Delta_{N}(\alpha, \delta), \tag{2.5}
$$

gives size-dependent fixed points $\alpha_{\mathrm{c}}(N,N+2)$. $\alpha_{\mathrm{c}}(N,N+2)$ is well fitted to a linear function of $1/(N+1)$ in the vicinity of $\delta=1$, whereas, as $\delta \to 0$, the linearity becomes worse and thus the uncertainty in the $N \to \infty$ extrapolation increases. Just for reference, the thus-obtained

phase boundary is also shown in Fig. 4 by a dotted line, which is somewhat discrepant from the highly accurate estimate based on $\eta$. The PRG equation applied to gapful-to-gapful phase transitions yields an accurate solution, to be sure, but, for transitions to a gapless phase, including those of KT type, the PRG analysis is likely to miss the correct solution due to essential corrections to the scaling law (2.3), overestimating the gapful-phase region [44,45]. The present PRG solution may still be recognized as the lower boundary of $\alpha_c$.

![](./images/867753078202302621_5.jpg)

FIG. 5. The ground-state magnetization curves for the classical Hamiltonian (1.2) with $\delta = 1$ at various values of $\alpha$.

## III. SUBLATTICE MAGNETIZATIONS

In an attempt to elucidate how much effect quantum fluctuations have on the stability of the plateau, we investigate the Hamiltonian (1.2) of classical version as well, where $\boldsymbol{S}_j$ and $\boldsymbol{s}_j$ are classical vectors of magnitude 1 and $\frac{1}{2}$, respectively. We show in Fig. 5 the classical magnetization curves. We note that the classical model also exhibits a plateau at $m = \frac{1}{2}$. The magnetization curves in the Ising region are not so far from the quantum behavior, though we have not shown them explicitly. However, the classical plateau can hardly stand the anisotropy of $XY$ type. In this context, it is interesting to observe sublattice magnetizations separately. We show in Fig. 6 the configuration of each classical spin as a function of a field. The classical plateau is nothing but a Néel-ordered state. In other words, without the fully ordered staggered magnetization, classical spins could not form a magnetization plateau. On the other hand, Fig. 7 shows that quantum spins can form a magnetization plateau with any combination of sublattice magnetizations. It is the case with the quantum model as well that sublattice magnetizations themselves freeze while going through the plateau. However, as long as the $XY$ exchange interaction exists, they are in general reduced from the full values 1 and $-\frac{1}{2}$, respectively. It is quantum fluctuations that stabilize the plateau with unsaturated sublattice magnetizations.

![](./images/867753078202302621_6.jpg)

FIG. 6. The ground-state sublattice magnetizations per unit cell as functions of a field for the classical Hamiltonian (1.2) with $\delta = 1$ at various values of $\alpha$: (a) the larger spin $S = 1$ and (b) the smaller spin $\frac{1}{2}$.

![](./images/867753078202302621_7.jpg)

FIG. 7. The ground-state sublattice magnetizations per unit cell as functions of a field for the quantum Hamiltonian (1.2) with $\delta = 1$ at various values of $\alpha$: (a) the larger spin $S = 1$ and (b) the smaller spin $\frac{1}{2}$.

One more interesting observation on the quantum spin configuration is that the collapse of the staggered order


in $z$ direction neither coincides with the $XY$ point nor results in the disappearance of the plateau. The $z$-direction spin correlations between the two sublattices turn ferromagnetic before the model reaches the $XY$ point. Here let us be reminded of the mixed nature [32] of quantum ferrimagnets. Because of the coexistent elementary excitations of different types, the specific heat exhibits a Schottky-like peak in spite of the initial ferromagnetic behavior at low temperatures, whereas the susceptibility-temperature product shows both increasing and decreasing behaviors as functions of temperature. The present phenomenon, a massive state in the ferromagnetic background, might also be recognized as a combination of ferromagnetic and antiferromagnetic features.

## IV. SUMMARY AND DISCUSSION

We have investigated the critical behavior of anisotropic Heisenberg mixed-spin chains in a field. The model shows an anisotropy-induced transition of KT type between the plateau and spin-fluid phases, whose phase boundary lies in the ferromagnetic-coupling region. Though we have restricted our argument to the case of $(S, s)=(1, \frac{1}{2})$, qualitatively the same scenario may be expected in higher-spin cases, where multi-plateau phases are possible with the assistance of bond alternation [46].

While our scaling analysis is highly accurate, it is subtle whether or not the plateau still exists at the $XY$ point. Therefore, any other argument would be helpful in understanding further the numerical findings obtained. Let us consider a spin-$\frac{1}{2}$ ferromagnetic-antiferromagnetic antiferromagnetic trimerized chain

$$
\begin{aligned}
\mathcal{H}=\sum_{j=1}^{N}\left[-\gamma\left(\boldsymbol{\sigma}_{j}^{a} \cdot \boldsymbol{\sigma}_{j}^{b}\right)_{\alpha}+\left(\boldsymbol{\sigma}_{j}^{b} \cdot \boldsymbol{\sigma}_{j}^{c}\right)_{\alpha}+\left(\boldsymbol{\sigma}_{j}^{c} \cdot \boldsymbol{\sigma}_{j+1}^{a}\right)_{\alpha}\right], & \\
& (4.1)
\end{aligned}
$$

which can be regarded as the Heisenberg ferrimagnet of our interest in the $\gamma \to \infty$ limit. Such a replica-model approach is quite useful [47] in studying low-dimensional quantum magnetism. Introducing the Jordan-Wigner spinless fermions via

$$
\lambda_{j}^{\dagger}=\sigma_{j}^{\lambda+} \exp \left[-\mathrm{i} \pi \sum_{l=1}^{j-1} \sigma_{l}^{\lambda+} \sigma_{l}^{\lambda-}\right] \quad(\lambda=a, b, c), \quad(4.2)
$$

we replace the Hamiltonian (4.1) by

$$
\mathcal{H}=\sum_{j=1}^{N}\left[\left(a_{j}, b_{j}\right)_{-\gamma, \alpha}+\left(b_{j}, c_{j}\right)_{1, \alpha}+\left(c_{j}, a_{j+1}\right)_{1, \alpha}\right], \quad(4.3)
$$

where $4(a, b)_{\gamma, \alpha}=2 \gamma\left(a^{\dagger} b+b^{\dagger} a\right)+\alpha\left(2 a^{\dagger} a-1\right)\left(2 b^{\dagger} b-1\right)$.

![](./images/867753078202302621_8.jpg)

FIG. 8. Dispersion relations of the spin-$\frac{1}{2}$ trimerized chain (4.1) at the $XY$ point $\alpha=0$. (a) $\gamma=1$. There is no gap in the excitation spectrum. (b) $\gamma>1$. There open up gaps at the sectors of $\frac{1}{3}$ and $\frac{2}{3}$ band filling, where $2 \Delta=3 \gamma-\left(\gamma^{2}+8\right)^{1 / 2}$.

![](./images/867753078202302621_9.jpg)

FIG. 9. The ground-state sublattice magnetizations per unit cell as functions of a field of the trimerized spin-$\frac{1}{2}$ chain (4.1) at the $XY$ point $\alpha=0$ for $\gamma=1.25$ and $\gamma=2$.

Now we focus our interest on the $XY$ point $\alpha=0$. After the Fourier transformation, we obtain the equation to determine the single-particle excitation spectrum as

$$
\varepsilon_{k}^{3}-\left(\gamma^{2}+2\right) \varepsilon_{k}-2 \gamma \cos k=0. \quad(4.4)
$$

The resultant dispersion relation is qualitatively different according as $\gamma=1$ or not, as illustrated in Fig. 8. At $\gamma=1$, which is not large enough to let ferromagnetically coupled neighboring spins construct spin 1's, there is no gap in the excitation spectrum. However, as $\gamma$ increases, gaps open up at the sectors of $\frac{1}{3}$ and $\frac{2}{3}$ band filling and this scenario remains qualitatively unchanged in the whole region $\gamma>1$. Noting the relation between the magnetization and the band filling,

$$
M=N_{\text {occ }}-\frac{3 N}{2}, \quad(4.5)
$$

where $N_{\rm occ}$ is the number of occupied states, we are al- lowed to expect magnetization plateaux at $m=\pm\frac{1}{2}$. The inclusion of the bond alternation $\delta$ results in the enhance- ment of the gap, which is consistent with Fig. 2. Qualita- tively the same scenario is available for a ferromagnetic- ferromagnetic-antiferromagnetic trimerized chain, as was pointed out by two pioneering authors [48,49]. The present analysis is not strictly comparable to the orig- inal argument unless $\alpha=1$. However, the nonvanishing gap in the $\gamma\rightarrow\infty$ limit may be a qualitative evidence for the existence of the plateau at the $XY$ point in the original model (1.2). We further show in Fig. 9 the sub- lattice magnetizations in the ground state of the replica model with $\alpha=0$ as functions of a field at a few values of $\gamma>1$. We are convinced all the more that the Néel order has already disappeared and both the spins 1 and $\frac{1}{2}$ have the same-sign $z$ components at the $XY$ point.

In recent years, a massive-to-spin-fluid phase transi- tion of KT type has been given a great deal of attention [50–56] in the context of Haldane’s conjecture [2]. In such cases the critical point never goes beyond the $XY$ point. The magnetization plateau in our argument should be distinguished from the gap immediately above the ground state, to be sure, but, compared with Haldane’s scenario [42], the present observation looks novel and is fascinat- ing to be further studied. There may be a new mass- generation mechanism peculiar to quantum mixed-spin chains, other than the valence-bond picture [57]. Quite recently Okamoto and Kitazawa [58] have reported that the magnetization plateau of the spin-$\frac{1}{2}$ trimerized chain which is closely related with the present model also disap- pears in the $XY$ ferromagnetic region. We hope that our investigation, combined with such an argument from a different viewpoint, will contribute toward revealing the possibly novel scenario for the breakdown of quantized plateaux.

## ACKNOWLEDGMENTS

It is a pleasure to thank H.-J. Mikeska and U. Schollwöck for helpful discussions. This work was sup- ported by the Japanese Ministry of Education, Science, and Culture through Grant-in-Aid No. 09740286 and by the Okayama Foundation for Science and Technology. The numerical computation was done in part using the facility of the Supercomputer Center, Institute for Solid State Physics, University of Tokyo.

[1] K. Hida, J. Phys. Soc. Jpn. 63, 2359 (1994).
[2] F. D. M. Haldane, Phys. Lett. 93A, 464 (1983); Phys. Rev. Lett. 50, 1153 (1983).
[3] K. Okamoto, Solid State Commun. 98, 245 (1995).
[4] T. Tonegawa, T. Nakao, and M. Kaburagi, J. Phys. Soc. Jpn. 65, 3317 (1996).
[5] K. Totsuka, Phys. Lett. A 228, 103 (1997); Phys. Rev. B 57, 3454 (1998).
[6] H. Nakano and M. Takahashi, J. Phys. Soc. Jpn. 67, 1126 (1998).
[7] D. C. Cabra and M. D. Grynberg, Phys. Rev. B 59, 119 (1999);
[8] A. Honecker, Phys. Rev. B 59, 6790 (1999).
[9] T. Sakai and M. Takahashi, Phys. Rev. B 57, 3201 (1998).
[10] T. Sakai and Y. Hasegawa, preprint (cond-mat/9809291).
[11] D. C. Cabra, A. Honecker, and P. Pujol, Phys. Rev. Lett. 79, 5126 (1997); Phys. Rev. B 58, 6241 (1998).
[12] K. Tandon, S. Lal, S. K. Pati, S. Ramasesha, and D. Sen, Phys. Rev. B 59, 396 (1999).
[13] A. K. Kolezhuk, Phys. Rev. B 59, February 1 (1999).
[14] Y. Narumi, M. Hagiwara, R. Sato, K. Kindo, H. Nakano, and M. Takahashi, Physica B 246-247, 509 (1998).
[15] W. Shiramura, K. Takatsu, B. Kurniwan, H. Tanaka, H. Uekusa, Y. Ohashi, K. Takizawa, H. Mitamura, and T. Goto, J. Phys. Soc. Jpn. 67, 1548 (1998).
[16] E. Lieb, T. Schultz, D. Mattis, Ann. Phys. 16, 407 (1961).
[17] I. Affleck, Phys. Rev. 37, 5186 (1988).
[18] M. Oshikawa, M. Yamanaka, and I. Affleck, Phys. Rev. Lett. 78, 1984 (1997).
[19] O. Kahn, Magnetism of the heteropolymetallic systems, Structure and Bonding 68, 91 (Springer-Verlag, 1987); O. Kahn, Y. Pei, and Y. Journaux, in Inorganic Materi- als, edited by D. W. Bruce and D. O’Hare (Wiley, New York, 1995), p. 95.
[20] A. Gleizes and M. Verdaguer, J. Am. Chem. Soc. 103, 7373 (1981); ibid. 106, 3727 (1984).
[21] Y. Pei, M. Verdaguer, O. Kahn, J. Sletten, and J.-P. Re- nard, Inorg. Chem. 26, 138 (1987); O. Kahn, Y. Pei, M. Verdaguer, J.-P. Renard, and J. Sletten, J. Am. Chem. Soc. 110, 782 (1988); P. J. van Koningsbruggen, O. Kahn, K. Nakatani, Y. Pei, J.-P. Renard, M. Drillon, and P. Legoll, Inorg. Chem. 29, 3325 (1990).
[22] Y. Pei, O. Kahn, J. Sletten, J.-P.Renard, R. Georges, J.- C. Gianduzzo, J. Curely, and Q. Xu, Inorg. Chem. 27, 47 (1988).
[23] M. Drillon, J. C. Gianduzzo, and R. Georges, Phys. Lett. 96A, 413 (1983); M. Drillon, E. Coronado, R. Georges, J. C. Gianduzzo, and J. Curely, Phys. Rev. B 40, 10992 (1989).
[24] F. C. Alcaraz and A. L. Malvezzi, J. Phys. A 30, 767 (1997).
[25] S. K. Pati, S. Ramasesha, and D. Sen, Phys. Rev. B 55, 8894 (1997); J. Phys.: Condens. Matter 9, 8707 (1997).
[26] S. Brehmer, H.-J. Mikeska, and S. Yamamoto, J. Phys.: Condens. Matter 9, 3921 (1997).
[27] A. K. Kolezhuk, H.-J. Mikeska, and S. Yamamoto, Phys. Rev. B 55, 3336 (1997); K. Maisinger, U. Schollwöck, S. Brehmer, H.-J. Mikeska, and S. Ya- mamoto, Phys. Rev. B 58, 5908 (1998); A. K. Kolezhuk, H.-J. Mikeska, K. Maisinger, and U. Schollwöck, preprint (cond-mat/9812326).


[28] H. Niggemann, G. Uimin, and J. Zittartz, J. Phys.: Con- dens. Matter **9**, 9031 (1997); *ibid.* **10**, 5217 (1998).

[29] S. Yamamoto, Int. J. Mod. Phys. C **8**, 609 (1997); S. Ya- mamoto, S. Brehmer, and H.-J. Mikeska, Phys. Rev. B **57**, 13610 (1998); S. Yamamoto and T. Sakai, J. Phys. Soc. Jpn. **67**, 3711 (1998).

[30] T. Ono, T. Nishimura, M. Katsumura, T. Morita, and M. Sugimoto, J. Phys. Soc. Jpn. **66**, 2576 (1997).

[31] T. Kuramoto, J. Phys. Soc. Jpn. **67**, 1762 (1998).

[32] S. Yamamoto and T. Fukui, Phys. Rev. B **57**, 14008 (1998); S. Yamamoto, T. Fukui, K. Maisinger, and U. Schollwöck, J. Phys.: Condens. Matter **10**, 11033 (1998); S. Yamamoto, Phys. Rev. B **59**, 1024 (1999).

[33] N. B. Ivanov, Phys. Rev. B **57**, 14024 (1998).

[34] M. Abolfath, H. Hamidian, and A. Langari, preprint (cond-mat/9901063).

[35] E. Lieb and D. Mattis, J. Math. Phys. **3**, 749 (1962).

[36] J. M. Kosterlitz and D. J. Thouless, J. Phys. C **6**, 1181 (1973).

[37] F. D. M. Haldane, Phys. Rev. B **25**, 4925 (1982).

[38] T. Sakai and M. Takahashi, Phys. Rev. B **43**, 13383 (1991);

[39] D. Shanks, J. Math. Phys. **34**, 1 (1955).

[40] J. L. Cardy, J. Phys. A **17**, L385 (1984); H. W. Blöte, J. L. Cardy and M. P. Nightingale, Phys. Rev. Lett. **56**, 742 (1986).

[41] I. Affleck, Phys. Rev. Lett. **56**, 746 (1986).

[42] H. J. Schulz, Phys. Rev. B **34**, 6372 (1986).

[43] M. P. Nightingale, Physica **83A**, 561 (1976).

[44] K. Nomura and K. Okamaoto, J. Phys. Soc. Jpn. **62**, 1123 (1993).

[45] K. Okamoto and K. Nomura, J. Phys. A: Math. Gen. **29**, 2279 (1996).

[46] S. Yamamoto and T. Sakai, unpublished.

[47] See for example, K. Hida, Phys. Rev. B **45**, 2207 (1992); *ibid.* **46**, 8268 (1992).

[48] C. E. Zaspel, J. Chem. Phys. **86**, 4713 (1987).

[49] K. Okamoto, Solid State Commun. **83**, 1039 (1992).

[50] R. Botet, R. Jullien, and M. Kolb, Phys. Rev. B **28**, 3914 (1983).

[51] J. Solyom and T. Ziman, Phys. Rev. B **30**, 3980; H. J. Schulz and T. Ziman, *ibid.* **33**, 6545 (1986).

[52] F. C. Alcaraz and A. Moreo, Phys. Rev. B **46**, 2896 (1992).

[53] U. Schollwöck and Th. Jolicœur, Europhys. Lett. **30**, 493 (1995).

[54] M. Yajima and M. Takahashi, J. Phys. Soc. Jpn. **63**, 3634 (1994).

[55] A. L. Malvezzi and F. C. Alcaraz, J. Phys. Soc. Jpn. **64**, 4485 (1995).

[56] J. P. Neirotti and M. J. de Oliveira, Phys. Rev. B **59**, 3303 (1999).

[57] I. Affleck, T. Kennedy, E. H. Lieb, and H. Tasaki, Phys. Rev. Lett. **59**, 799 (1987); Commun. Math. Phys. **115**, 477 (1988).

[58] K. Okamoto and A. Kitazawa, preprint (cond- mat/9809138).

TABLE I. The antiferromagnetic excitation gap $\Delta$ as a function of $\delta$ at the Heisenberg point $\alpha=1$.

<table>
  <thead>
    <tr>
      <th>$\delta$</th>
      <th>1</th>
      <th>0.8</th>
      <th>0.6</th>
      <th>0.4</th>
      <th>0.2</th>
      <th>0</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>$\Delta$</td>
      <td>1.7591</td>
      <td>1.6042</td>
      <td>1.4986</td>
      <td>1.4500</td>
      <td>1.4558</td>
      <td>$\frac{3}{2}$</td>
    </tr>
  </tbody>
</table>