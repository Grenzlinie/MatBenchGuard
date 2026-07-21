# Distortion of a Substrate Induced by Adsorption at Solid-Liquid Interfaces

E. V. Vakarin, $^{*}$ A. E. Filippov, $^{\dagger}$ and J. P. Badiali $^{\ddagger}$

Structure et Réactivité des Systèmes Interfaciaux, Université Pierre et Marie Curie,
4 Place Jussieu, 75230 Paris Cedex 05, France
(Received 26 May 1998)

Employing a generalized lattice gas theory and the Brownian dynamics simulation, we show that the presence of an adsorbate may induce a distortive transition in the underlying substrate. The transition takes place if we have a strong pinning of the adsorbate and the lateral interaction strong enough to compete with the cohesive energy of the substrate. The threshold for the transition is determined by an interplay of the elastic energies arising from the atomic displacements of both subsystems. The resulting lattice configuration appears as a compromise between the symmetry of the clean substrate and the symmetry of the close packed adsorbate. [S0031-9007(98)07554-1]

PACS numbers: 68.45.–v

Processes occurring at solid-liquid interfaces are traditionally described under the assumption that the solid substrate does not change under the influence of the adlayer [1–5]. Nevertheless, ordering properties of fluids in slit pores were shown [6] to be significantly affected by the thermal motion of wall atoms. For real interfaces the substrate-adsorbate bonding energy can be comparable to, or even larger than the cohesive energy of the substrate [7]. One then has to investigate modifications of the substrate induced by the adsorbate [8]. Recent experimental investigations [9] have suggested that some local distortion of $Au\{111\}$ surfaces should be assumed in order to interpret the diffraction patterns of $n$-alkyl thiols. Similar buckling and lateral shifts are detected [10] for $Ru\{001\}$ in the presence of adsorbed oxygen. For the same reason, adsorbates are shown to decrease the roughening temperature [11].

In the presence of a strong pinning and the lateral interaction, an adsorbate may induce the in-plane stress [12–14] and lead to a rearrangement of the substrate. In this letter we consider a solid-liquid interface and discuss static distortions of the substrate induced by an adsorbate with strong lateral interactions. The substrate is assumed to be stable with a given crystalline configuration. The surface is modeled as a two-dimensional square lattice (the spacing is $d$) of adsorbing sites located on the top of the substrate atoms. The sites have the displacive degrees of freedom due to the elastic properties of the substrate (phononic excitations or anharmonicity effects). This is mediated by the substrate pair potential $U_{SS}(\mathbf{R}_{i},\mathbf{R}_{j})$, where $\mathbf{R}_{i}$ is a two-dimensional vector specifying the location of the site. We assume that the motion of the substrate in the direction perpendicular to the surface is forbidden. In the absence of the adsorbate the solid atoms vibrate around the equilibrium positions $\mathbf{R}_{i}^{0}$ in such a way that $\langle\mathbf{u}_{i}\rangle=\langle\mathbf{R}_{i}-\mathbf{R}_{i}^{0}\rangle=0$. The surface is exposed to a liquid with a given pair potential. The adsorbing potential is introduced as that of the sticky site model [15,16]. This model is chosen because, in addition to its mathematical simplicity, it allows us to describe a strong pinning of the adsorbate to the substrate positions. Because of this specific potential the partition function can be reduced to that of the lattice gas with an additional integration over the substrate positions.

$$
\begin{aligned}
\Xi= & \int\left(d \mathbf{R}_{i}\right) e^{-\beta / 2 \sum_{i, j} U_{S S}\left(\mathbf{R}_{i} \mathbf{R}_{j}\right)} \\
& \times \sum_{t_{i}} e^{-\beta / 2 \sum_{i, j} W_{L L}\left(\mathbf{R}_{i} \mathbf{R}_{j}\right) t_{i} t_{j}} e^{\beta \sum_{i} \mu_{i} t_{i}}.
\end{aligned}\quad (1)
$$

The chemical potential is $\mu_{i}$, and $W_{LL}(\mathbf{R}_{i}\mathbf{R}_{j})$ is the mean force potential for the adsorbate. Each pair of the solid sites interacts through the $U_{SS}$ potential plus an extra $W_{LL}$ contribution from a pair of adsorbed particles. The presence of this additional interaction is determined by the set of occupation numbers $t_{i}=0,1$. To proceed further we extract the contribution corresponding to the reference state, i.e., the state with the sites located at the equilibrium positions
$U_{SS}(\mathbf{R}_{i},\mathbf{R}_{j})=U_{SS}(\mathbf{R}_{i}^{0},\mathbf{R}_{j}^{0})+U_{SS}(\mathbf{u}_{i},\mathbf{u}_{j})$,
$W_{LL}(\mathbf{R}_{i},\mathbf{R}_{j})=W_{LL}(\mathbf{R}_{i}^{0},\mathbf{R}_{j}^{0})+W_{LL}(\mathbf{u}_{i},\mathbf{u}_{j})$. Each displacement-dependent part contains the one-body potential (at $i=j$) and the displacement interaction potential (at $i \neq j$). Performing the summation over $t_{i}$ within the mean field approximation (MFA), we obtain

$$
\begin{aligned}
\Xi= & e^{-\beta F_{0}(\Theta)} \int\left(d \mathbf{u}_{i}\right) e^{-\beta / 2 \sum_{i, j} U_{S S}\left(\mathbf{u}_{i} \mathbf{u}_{j}\right)} \\
& \times e^{\beta / 2 \sum_{i, j} W_{L L}\left(\mathbf{u}_{i} \mathbf{u}_{j}\right) \Theta_{i} \Theta_{j}} \\
& \times \prod_{i}\left[1+\tau_{i}(\Theta)\{e^{-\beta \sum_{j} W_{L L}\left(\mathbf{u}_{i} \mathbf{u}_{j}\right) \Theta_{j}}-1\}\right],
\end{aligned}\quad (2)
$$

where $F_{0}(\Theta)$ is the free energy and $\tau_{i}(\Theta)$ is the average occupation number for the reference state [15], and $\Theta_{i}=\langle t_{i}\rangle$ is the average occupation number to be determined from the free energy. It is seen from Eq. (2) that, in addition to the usual potentials, we have an entropic term under the product (it originates from the summation over the occupation numbers).

Even within the harmonic approximation for $W_{LL}(\mathbf{u}_i \mathbf{u}_j)$, this term generates the anharmonicity and the many-body correlations. This is due to the fact that the coverage is not uniform along the lattice. Then the domain walls between the covered and uncovered parts of the substrate induce the anharmonicity due to unbalanced forces.

In the absence of anharmonic effects stabilizing the substrate at a large displacement regime, we observe the harmonic instability [17] of the substrate (at $\mathbf{u}_i=0$) when the fraction of distorted bonds increases [18]. A proper description of this distortive transition requires taking into account the nonparabolicity of the one-body displacement potential [17] [$V_1(\mathbf{u}_i)$ is the $i=j$ part of Eq. (2)]. This is done by including higher order terms in $\mathbf{u}_i^2$ to $U_{SS}(\mathbf{u}_i, \mathbf{u}_j)$. Then we observe [19] a multiple-welled potential with new equilibrium positions appearing in addition to, or even instead of the substrate one $\mathbf{u}_i=0$. For specific coverages $(\Theta \approx \frac{1}{2})$ these additional minima are not much deeper that the initial one, and the potential may be approximated by the square well:
$$
V_{1}(\mathbf{u}_{i})=\left\{\begin{array}{ll}
-U_{0}, & \left|\mathbf{u}_{i}\right|<L / 2, \\
\infty, & \text { otherwise, }
\end{array}\right.\qquad(3)
$$
where $U_0$ is the depth of the well and $L$ is its width. The cutoff distance $L$ corresponds to the flat bottom region of the real anharmonic potential. It is clear that such an approximation does not allow us to determine the coverage self-consistently.

In addition to the one-body potential we consider the bilinear correlation term. It contains the substrate contribution $\sum_{i j} D_{i j} \mathbf{u}_{i} \mathbf{u}_{j}$ and the bilinear combination $\sum_{i j} T_{i j}(\Theta) \Delta_{i j} \mathbf{u}_{i} \mathbf{u}_{j}$ from the adsorbate. Here $T_{i j}(\Theta) \propto$ $\Theta_{i} \Theta_{j}, D_{i j}$, and $\Delta_{i j}$ are the corresponding elastic matrices. For simplicity we assume the uniaxial anisotropy: $\mathbf{u}_{i} \mathbf{u}_{j}= \pm u_{i} u_{j}$ along a virtual external field $v_{i}$. Therefore each $u_{i}$ is a scalar restricted to $[-L / 2, L / 2]$. Then our problem becomes quasi-one-dimensional, with the partition function $\tilde{\Xi}=\Xi e^{\beta F_{0}(\Theta)}$ given by
$$
\tilde{\Xi}=\int_{-L / 2}^{L / 2}\left(d u_{i}\right) e^{-\beta \sum_{i, j}\left[D_{i j}+T_{i j}(\Theta) \Delta_{i j}\right] u_{i} u_{j}} e^{-\beta \sum_{i} v_{i} u_{i}}. \quad(4)
$$

Introducing the MFA for the displacements and setting after that $v_i=0$, we get the free energy excess
$$
\begin{aligned}
\beta F= & \beta F_{0}(\Theta)-\frac{1}{2} \sum_{i, j}\left[\tilde{D}_{i j}+T_{i j}(\Theta) \tilde{\Delta}_{i j}\right]\left\langle u_{i}\right\rangle\left\langle u_{j}\right\rangle \\
& -\sum_{i} \ln I\left[\left\langle u_{i}\right\rangle\right],
\end{aligned}\qquad(5)
$$
where
$$
I\left[\left\langle u_{i}\right\rangle\right]=\frac{\sinh \left\{\sum_{j}\left[\tilde{D}_{i j}+T_{i j}(\Theta) \tilde{\Delta}_{i j}\right]\left\langle u_{j}\right\rangle\right\}}{\left\{\sum_{j}\left[\tilde{D}_{i j}+T_{i j}(\Theta) \tilde{\Delta}_{i j}\right]\left\langle u_{j}\right\rangle\right\}}.\qquad(6)
$$

Here $\langle u_i\rangle$ is the average dimensionless distortion, and
$$
\tilde{D}_{i j}=\beta D_{i j}\left(\frac{L}{2}\right)^{2}, \quad \tilde{\Delta}_{i j}=\beta \Delta_{i j}\left(\frac{L}{2}\right)^{2}\qquad(7)
$$
are the dimensionless elastic energies. Minimization of the free energy with respect to $\langle u_i\rangle$ gives the following self-consistent relation
$$
\left\langle u_{i}\right\rangle=-\mathcal{L}\left[\sum_{j}\left[\tilde{D}_{i j}+T_{i j}(\Theta) \tilde{\Delta}_{i j}\right]\left\langle u_{j}\right\rangle\right],\qquad(8)
$$
where $\mathcal{L}(x)=cth(x)-1 / x$ is the Langevin function. If only $n$ nearest neighbors (nn) contribute, then the threshold for $\langle u_i\rangle \neq 0$ is given by
$$
n[\tilde{D}+T(\Theta) \tilde{\Delta}] \leq-3.\qquad(9)
$$

This equation represents an interplay between the elastic energies of the adsorbate and the substrate. For the substrate, $D$ is positively defined because of the thermodynamical stability, while $\Delta$ is negative for repulsing (nn) interactions. This indicates that the set of $\{\mathbf{R}_i^0\}$ is close to the maxima of $W_{LL}$. The adsorbate then tends to shift from $\{\mathbf{R}_i^0\}$ to minimize the energy. If the coupling is strong, the substrate is also involved in this motion. We deal with a distortive transition from the substrate-induced ordering $(\langle u_i\rangle=0)$ to that induced by the adsorbate $(\langle u_i\rangle \neq 0)$.

To recover the structure appearing due to this transition, we perform the Brownian dynamics simulation which allows us to go beyond the small distortions up to a complete rearrangement of the surface. A similar approach has been developed recently [20-25] in the framework of the generalized Frenkel-Kontorova model. We consider two interacting subsystems of $N_j \leq 1 \times 10^3$ particles (where $j=1,2$ for the substrate and for the adsorbate atoms, respectively). The case of $N_2/N_1=$ 1 is reported here. One of them is confined to the minima of the external periodic potential $V_0(\mathbf{R})$ with the amplitude $V_0$, which is used to model the square crystalline surface. In general, the substrate atoms can move from these minima being affected by the adsorbate. Another subsystem describes the adsorbate, which is attracted to the substrate (moving) atoms and does not interact directly with the potential $V_0(\mathbf{R})$. For simplicity we set both atomic masses $m_j=1$. The equation of motion for the atomic coordinates $\mathbf{R}_{j i}$ is
$$
\begin{aligned}
\ddot{\mathbf{R}}_{j i}+\eta \dot{\mathbf{R}}_{j i} & +\frac{\partial}{\partial \mathbf{R}_{j i}} V_{0}\left(\mathbf{R}_{j i}\right) \delta_{j 1}+ \\
& \frac{\partial}{\partial \mathbf{R}_{j i}} \sum_{k l} V\left(\mathbf{R}_{j i}-\mathbf{R}_{k l}\right)=\delta F\left(\mathbf{R}_{j i} ; t\right),(10)
\end{aligned}
$$
where $1 \leq i \leq N_j$. To model a thermal bath we apply the Gaussian random force $\delta F_{j i}(t)$,
$$
\begin{aligned}
\left\langle\delta F\left(\mathbf{R}_{j i} ; t\right), \delta F\left(\mathbf{R}_{j^{\prime} i^{\prime}} ; t^{\prime}\right)\right\rangle & =2 \eta T \delta_{j j^{\prime}} \delta\left(\mathbf{R}_{j i}-\mathbf{R}_{j^{\prime} i^{\prime}}\right) \\
& \times \delta\left(t-t^{\prime}\right),
\end{aligned}\qquad(11)
$$
to all atoms. The coefficient $\eta=1$ determines the temperature $T$ and corresponds to the viscous damping due to energy exchange between the adsorbate and the substrate. We calculated the average square of velocity to

![](./images/811058921627189249_1.jpg)

FIG. 1. Maxima of $G_{11}(\mathbf{q})$ for the adsorbate-induced (a) and substrate-induced (b) structures.

control the temperature fixed $T=1$. The interaction potential is chosen to be $V(|\mathbf{R}_{j j'}|)=V_{j j'} \exp (-\mathbf{R}_{j j'}^{2}/a_{j j'})$. The interaction is repulsive within a subsystem $(V_{j j}>0)$ and is attractive for different subsystems $(V_{12}<0)$. The numerical solution of (10), supplemented by the periodic boundary conditions, enables us to calculate the density distributions $\varrho_{j}(\mathbf{R})=\sum_{i} \delta(\mathbf{R}-\mathbf{R}_{i j})$ and, after the averaging, the two-body correlation functions $G_{j, j'}(\mathbf{R},\mathbf{R}')=\langle\varrho_{j}(\mathbf{R})\varrho_{j'}(\mathbf{R}')\rangle$. The two-dimensional Fourier transform of the substrate correlation function $G_{11}(\mathbf{q})=\int d(\mathbf{R}-\mathbf{R}')e^{i\mathbf{q}(\mathbf{R}-\mathbf{R}')}G_{11}(\mathbf{R},\mathbf{R}')$ represents our main focus. The distribution of its maxima is shown in Fig. 1. If $V_{0}$ dominates over $V_{12}$ and $V_{22}$, both subsystems reach the square lattice structure, determined by the substrate [Fig. 1(b)]. If $V_{11} \ll V_{22}$, the steady state has a distorted hexagonal symmetry [Fig. 1(a)]. This makes a compromise between the square (unperturbed) structure and the hexagonal structure driven by the adsorbate (two common reflection axes are indicated in Fig. 1). All intermediate distributions appear as superpositions of these two limiting cases. Namely, the $b,b'$ maxima (and complementary to them) disappear and the $a,a'$ (and complementary) peaks grow if one passes from the substrate- to the adsorbate-driven structure. According to the general approach [26], the normalized height difference of $b$ (or $b'$) peaks for two structures determines the order parameter which is depicted in Fig. 2. Keeping fixed all other parameters of the problem and the relations between them $(V_{11}=V_{12}, V_{22}=3V_{12}, a_{11}=a_{22}=0.875, a_{12}=0.5)$, we increase the $V_{22}$ from the trivial case of $V_{22}=0$ up to $V_{22}^{\text{max}}=50$ (the adsorbate-driven structure). $V_{i j}$ and $a_{i j}$ are measured in terms of $V_{0}$ and the initial lattice spacing, respectively. The characteristic time necessary to reach the steady state is estimated to be $t_{\text{max}}=1.5\times 10^{2}\times \eta^{-1}$. At each step we calculated the order parameter: $1-G_{11}(\mathbf{q}_{b};V_{22})/G_{11}(\mathbf{q}_{b};V_{22}=0)$. The relative strength of interaction is determined as $V_{22}/V_{22}^{\text{max}}$. Qualitatively, the same result is observed when $V_{12}$ changes at fixed $V_{22}$. Since the elastic matrices treated analytically are just the second derivatives of the potentials, the curvatures are proportional to the potential magnitudes. The proportionality coefficients disappear when the ratio is taken. This allows us to compare the theoretical prediction [from Eq. (8)] with the simulation result. The asymptotic regime $(\langle u\rangle \to 1)$, corresponding to the adsorbate-driven structure, is described correctly. But a deviation is seen near the threshold. This is due to the finite box size which leads to difficulties in extracting the $b$ peak from the satellite fluctuations. The rate of interaction at which the $b,b'$ peaks disappear, is quite sensitive to the noise produced by the random force $\delta F_{j i}(t)$. Therefore the threshold should be associated with the inflection point [27] appearing at $V_{22}/V_{22}^{\text{max}}\approx 0.154$ (the theory gives 0.183). On the other hand, the threshold is predicted within the MFA, which is known [26] to be only qualitatively correct near the ordering transition. The latter cannot be qualified as the conventional commensurate-incommensurate transition [1], since both subsystems form a common lattice which, however, differs from that of the clean substrate. On the other hand, this is not the conventional reconstruction, because the substrate itself is stable. The instability towards the structural change is induced by the adsorbate. This suggests that in the presence of competing interactions these two tendencies are mixed to give a qualitatively new structure. A detailed analysis of this transition, as well as its self-consistent dependence on the coverage, will be presented in a future study.

![](./images/811058921627189249_2.jpg)

FIG. 2. The order parameter as a function of the relative strength of the adsorbate-adsorbate interaction. The simulation result (dots) vs the theory [from Eq. (8)] (line).

E. V. V. gratefully acknowledges support from the French Ministry of Education, Research and Technologies. For A. E. F. this work was supported in part within the CNRS Cooperation Program Ukraine-France. The authors are greatful to Dr. Di Caprio for useful comments.

*Permanent address: Institute for Condensed Matter Physics, Svientsitsky str. 1, 290011, Lviv, Ukraine.

$^{\dagger}$Permanent address: Donetsk Physical-Technical Institute of NASU 340114, Donetsk, Ukraine.
$^{\ddagger}$Author to whom correspondence should be addressed.

[1] B.N.J. Persson, Surf. Sci. Rep. 15, 1 (1992).

[2] J. Villain and M.B. Gordon, Surf. Sci. 125, 1 (1983).

[3] L.D. Roelofs and P.J. Estrup, Surf. Sci. 125, 51 (1983).

[4] W. Selke, in Phase Transitions and Critical Phenomena, edited by C. Domb and J. Lebowitz (Academic Press, London, 1992), Vol. 15, p. 1.

[5] A.D. Novaco and J.P. McTague, Phys. Rev. Lett. 38, 1286 (1977); J.P. McTague and A.D. Novaco, Phys. Rev. B 19, 5299 (1979).

[6] D.J. Diestler and M. Schoen, J. Chem. Phys. 104, 6784 (1996).

[7] V.P. Zhdanov and B. Kasemo, J. Chem. Phys. 108, 4582 (1998).

[8] H. Ibach, Surf. Sci. Rep. 29, 193 (1997).

[9] P. Fenter, A. Eberhardt, and P. Eisenberg, Science 266, 1216 (1994); N. Camillone III, T.Y.B. Leung, and G. Scoles, Surf. Sci. 373, 333 (1997).

[10] M. Lindroos, H. Pfnür, G. Held, and D. Menzel, Surf. Sci. 222, 451 (1989).

[11] V.P. Zhdanov and B. Kasemo, Phys. Rev. B 56, R10 067 (1997).

[12] J.E. Müller, M. Wuttig, and H. Ibach, Phys. Rev. Lett. 56, 1583 (1986).

[13] W. Daum, C. Stuhlmann, and H. Ibach, Phys. Rev. Lett. 60, 2741 (1988).

[14] A. Grossmann, W. Erley, J.B. Hannon, and H. Ibach, Phys. Rev. Lett. 77, 127 (1996).

[15] J.P. Badiali, L. Blum, and M.L. Rosinberg, Chem. Phys. Lett. 129, 149 (1986).

[16] M.L. Rosinberg, J.L. Lebowitz, and L. Blum, J. Stat. Phys. 44, 153 (1986).

[17] R. Blinc and B. Zeks, Soft Modes in Ferroelectrics and Antiferrolectrics (North-Holland, Amsterdam, 1974).

[18] J.V. Andersen and L.J. Lewis, Phys. Rev. E 57, R1211 (1998).

[19] E.V. Vakarin, A.E. Filippov, J.P. Badiali, and M.F. Holovko (to be published).

[20] B.N.J. Persson, Phys. Rev. Lett. 71, 1212 (1993); Phys. Rev. B 48, 18 140 (1993).

[21] F.-J. Elmer, Phys. Rev. E 50, 4470 (1994); M. Weiss and F.-J. Elmer, Phys. Rev. B 53, 7539 (1996).

[22] M.G. Rozman, M. Urbakh, and J. Klafter, Phys. Rev. Lett. 77, 683 (1996); Phys. Rev. E 54, 6485 (1996); Europhys. Lett. 39, 183 (1997).

[23] O.M. Braun, T. Dauxois, M.V. Paliy, and M. Peyrard, Phys. Rev. Lett. 78, 1295 (1997); Phys. Rev. E 55, 3598 (1997).

[24] M. Paliy, O. Braun, T. Dauxois, and B. Hu, Phys. Rev. E 56, 4025 (1997).

[25] O.M. Braun, A.R. Bishop, and J. Röder, Phys. Rev. Lett. 79, 3692 (1997).

[26] L.D. Landau and E.M. Lifshitz, Statistical Physics (Perg- amon, London, 1958).

[27] V.P. Zhdanov, J.L. Sales, and R.O. Unac, Surf. Sci. 381, L599 (1997).