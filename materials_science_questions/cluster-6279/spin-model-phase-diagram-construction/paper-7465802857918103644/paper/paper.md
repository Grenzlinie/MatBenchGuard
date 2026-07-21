# Weak first-order phase transition out of the classical kagome spin liquid

Cecilie Glittum$^1$ and Olav F. Syljuåsen$^1$

$^1$Department of Physics, University of Oslo, P. O. Box 1048 Blindern, N-0316 Oslo, Norway
(Dated: May 27, 2026)

The low-temperature fate of the spin-liquid regime in the classical kagome Heisenberg antiferromagnet has been debated for over three decades. Using an expansion in the number of spin components, we show that, contrary to earlier Monte Carlo simulations, the spin liquid terminates at a weak first-order phase transition into the $\sqrt{3} \times \sqrt{3}$ phase which ordered moment saturates at zero temperature. Adding second-neighbor interactions, this transition belongs to a line of first-order phase transitions that ends at a critical point. For comparison, the pyrochlore antiferromagnet remains disordered at all temperatures.

Magnetic frustration arises when the geometry of a crystal lattice prevents spins from simultaneously minimizing all their pairwise interactions. Rather than freezing into a conventional ordered state, frustrated magnets can remain in a highly correlated yet disordered cooperative regime, a classical spin liquid, down to temperatures far below the energy scale set by the exchange interactions. A central question is whether such a spin liquid is ultimately stable all the way down to zero temperature, or whether thermal fluctuations eventually conspire to select an ordered state at anomalously low temperatures [1].

The classical Heisenberg antiferromagnet on the kagome lattice, see Fig. 1, is the sharpest two-dimensional realization of this problem. Its corner-sharing triangle geometry forces every triangle to have zero total spin, leaving a ground-state manifold that is extensively degenerate. The resulting spin liquid, characterized by a diffuse neutron-scattering intensity, persists over a broad temperature range well below the exchange interaction scale. Yet both analytical arguments and numerical Monte Carlo (MC) simulations find that, at sufficiently low temperatures, thermal fluctuations select coplanar states and ultimately favor $\sqrt{3} \times \sqrt{3}$ correlations [2–9], see Fig. 1, through an order-by-disorder mechanism [10].

Despite three decades of sustained efforts, two fundamental questions about the low-temperature behavior have remained delicate to settle: First, does the spin liquid evolve into the $\sqrt{3} \times \sqrt{3}$ phase through a thermal crossover, or is there a thermodynamic phase transition separating two distinct phases? Second, does the $\sqrt{3} \times \sqrt{3}$ ordered moment truly saturate as the temperature goes to zero, or does it remain permanently suppressed by proliferating domain walls [6] and/or vortices [7]? Extensive MC efforts have led to the prevailing picture for both questions: the system appears to undergo a sharp crossover into a coplanar phase with a saturating octupolar order parameter [7, 11] and $\sqrt{3} \times \sqrt{3}$ correlations with a substantially reduced ordered moment [6, 7, 9]. However, as noted in Refs. 6 and 7, such MC simulations are challenging, as the MC algorithms experience severe slowing down at low temperatures. This motivates the use of complementary methods that do not rely on direct configuration sampling.

![](./images/7465802857918103644_0.png)

FIG. 1. Kagome lattice with spins showing the coplanar fully ordered $\sqrt{3} \times \sqrt{3}$ state. Solid lines show $J_1$ couplings. The dashed line shows one of the $J_2$ couplings.

In this Letter, we address these long-standing problems using Nematic Bond Theory (NBT), a self-consistent approach based on the large-$N_s$ expansion where $N_s = 3$ is the number of spin components. It extends the usual self-consistent Gaussian approximation (SCGA) [12] by including momentum-dependent self-energies and enforcing the local unit-length spin constraint more accurately [13–16]. NBT is particularly well suited to the kagome problem because it compares free energies of competing phases directly for large system sizes, thus bypassing sampling problems that can impair low-temperature MC studies. Our main result is that the classical kagome spin liquid and the $\sqrt{3} \times \sqrt{3}$ phase are genuine thermodynamic phases separated by a first-order transition with very small latent heat. Furthermore, the ordered moment of the $\sqrt{3} \times \sqrt{3}$ phase saturates as the temperature goes to zero.

We consider the classical Heisenberg model

$$
H = \frac{1}{2} \sum_{\vec{R},i} \sum_{\vec{R}',j} J_{\vec{R}'-\vec{R},ij} \vec{S}_{\vec{R},i} \cdot \vec{S}_{\vec{R}',j}, \tag{1}
$$

on the kagome lattice with unit-length spins $\vec{S}_{\vec{R},i}$, where $\vec{R}$ denotes the unit cell and $i$ the position within the unit cell (sublattice index). The lattice has $N = 3L^2$ spins and periodic boundary conditions. We focus on nearest-neighbor antiferromagnetic coupling $J_1 = 1$, with a second-neighbor coupling $J_2$ introduced later to map the nearby phase diagram. While SCGA takes the unit-length constraint of the spins into account approximately by enforcing unit length on average, NBT goes one step further by also suppressing spatial fluctuations of the spin lengths. To do this, the local spin-length constraint is represented by a fluctuating constraint field; its uniform component $\Delta$ is treated self-consistently as in SCGA, while nonuniform components are incorporated diagrammatically. This yields dressed spin and constraint propagators linked by self-consistent Dyson equations with a momentum-dependent self-energy (see Supplemental Material Sec. A [17]). Solving these NBT equations amounts to finding a saddle-point solution by means of iterations, starting from a chosen value of the self-consistent field $\Delta$ and an initial self-energy. The converged solution in turn gives the temperature, spin static structure factor and crucially the free energy. Operationally, we iterate the NBT equations from different initial self-energies and track the converged branches as $\Delta$ is varied. Because the iterations are not guaranteed to flow to the globally stable state, a key step is to compare the resulting free energies, and identify the physical branch as the one with the lowest value.

For large $\Delta$, which corresponds to high temperatures $T$, the NBT equations converge to a unique solution regardless of the initial self-energy. The corresponding free energy is shown as the black curve in Fig. 2. For points on this curve, our NBT results are approximately equal to SCGA and describe a disordered paramagnet at high temperatures that evolves smoothly into a highly fluctuating, noncoplanar spin liquid with a diffuse structure factor and clear pinch points at lower temperatures, see Fig. 3 lower inset [5, 7, 18]. This spin-liquid branch persists down to the lowest temperatures in our calculation; however, its free energy is minimal only at temperatures $T > T_c \approx 1.59 \cdot 10^{-3}$. At lower temperatures, the coplanar single-$\vec{q}$ $\sqrt{3} \times \sqrt{3}$ phase becomes thermodynamically stable, see the pink curve in Fig. 2. This curve is obtained by starting from a low value of $\Delta$ and an initial self-energy that biases the iterations toward the $\sqrt{3} \times \sqrt{3}$ state. To find this initial self-energy, we performed a simulation with $J_2$ slightly ferromagnetic, and used the converged self-energy at low temperature as input. States in the $\sqrt{3} \times \sqrt{3}$ phase have structure factors with sharp peaks at the $\sqrt{3} \times \sqrt{3}$ ordering wave vectors and corresponding satellite peaks, see Fig. 3 upper inset. The associated correlation length in the $\sqrt{3} \times \sqrt{3}$ phase at the phase transition is very large, exceeding 3000 kagome lattice spacings. In contrast, the correlation length in the spin liquid at the phase transition is approximately twenty kagome lattice spacings and follows a $1/\sqrt{T}$ behavior [18] (see Supplemental Material Sec. B [17]).

![](./images/7465802857918103644_1.png)

FIG. 2. Main panel: Free energy per spin vs. $T$ for the different phases indicated by the legends. The black points start from a random initial self-energy at large values of $\Delta$, and constitute the free energy of the spin liquid. The colored points are obtained starting from low $\Delta$-values with initial self-energies that bias the iterations toward their respective phases. A linear term $aT$ with $a = 3$ is subtracted for better visualization of the crossing point between the spin-liquid and $\sqrt{3} \times \sqrt{3}$ branches. The inset shows the difference of the biased curves from the spin liquid divided by $T$. $L = 300$. The spin configurations show the coplanar $\vec{q} = 0$ state (left) and the noncoplanar cuboc1 state (right).

The fact that the free energies of the spin liquid and $\sqrt{3} \times \sqrt{3}$ phase cross at a very low, but finite, temperature, implies that they are distinct thermodynamic phases. The discontinuity of slopes at the crossing point further indicates a first-order phase transition. We have carried out a finite-size analysis of the crossing point (see Supplemental Material Sec. C [17]), and find that the first-order transition has a very small latent heat per spin $\ell_h = 1.04 \cdot 10^{-4}$, thus classifying the transition as weakly first order.

Figure 2 shows also two other free-energy branches: the purple and orange curves where the initial self-energy biases the iterations toward the $\vec{q} = 0$ state and the cuboc1 state [19, 20], respectively (for illustrations, see top of Fig. 2). Their free energies are always larger than the $\sqrt{3} \times \sqrt{3}$ phase, which is even more apparent in the lower inset of Fig. 2 showing a semilog-plot of the difference in free energy from the spin liquid divided by temperature.

To further characterize the low-temperature $\sqrt{3} \times \sqrt{3}$ phase, we calculate the (same sublattice) $\sqrt{3} \times \sqrt{3}$ (dipo-

![](./images/7465802857918103644_2.png)

FIG. 3. Main panel: The (squared) ordered moment for the $\sqrt{3}$×$\sqrt{3}$ phase (pink) and spin liquid (black) vs. $T$ for different linear system sizes $L$ indicated by the numbers. The vertical line marks $T_c$ for $L=300$. Faint colors correspond to metastable states. Insets: Spin structure factors $S(\vec{q})$ for the $\sqrt{3}$×$\sqrt{3}$ phase at $T=1.58\cdot 10^{-3}$ (top, $\log_{10}(S(\vec{q})+1)$), and for the spin liquid at $T=1.78\cdot 10^{-3}$ (bottom, $S(\vec{q})$). $L=300$.

lar) ordered moment squared [7]

$$
m_{\mathrm{AF}}^{2} \equiv \frac{6}{N^{2}} \sum_{l, \vec{R}, \vec{R}^{\prime}}\left\langle\vec{S}_{\vec{R}, l} \cdot \vec{S}_{\vec{R}^{\prime}, l}\right\rangle e^{i \vec{Q} \cdot\left(\vec{R}-\vec{R}^{\prime}\right)}, \tag{2}
$$

where $\vec{Q}=(4\pi/3,0)$ corresponds to antiferromagnetic $\sqrt{3}$×$\sqrt{3}$ order. Fig. 3 shows $m_{\mathrm{AF}}^{2}$ as function of temperature for three different system sizes. As the system is two-dimensional with continuous symmetry, the ordered moment must vanish at finite temperatures as $N\rightarrow\infty$ [21]. However as is also apparent from the figure, it saturates at $T=0$ for all system sizes, i.e. the $\sqrt{3}$×$\sqrt{3}$ phase orders completely at $T=0$. In contrast, $m_{\mathrm{AF}}^{2}$ calculated in the spin lquid is almost zero.

Next we obtain the specific heat $c_{\mathrm{v}}$ as a function of temperature from the free energy, focusing on the thermodynamically stable branches, see Fig. 4. When lowering the temperature, the specific heat of the spin liquid increases and extrapolates to $1$ at $T=0$. At $T_c$ the first-order phase transition manifests itself in $c_{\mathrm{v}}(T)$ as a Dirac delta-function $\ell_h\delta(T-T_c)$ (not shown) and a discontinuity (vertical dashed line). Below $T_c$ the specific heat follows the $\sqrt{3}$×$\sqrt{3}$ branch and decreases steadily. For temperatures close to zero, the specific heat follows a $\sqrt{T}$ behavior (see Supplemental Material Sec. D [17]). The zero-temperature values for different system sizes are shown in the upper inset and a straight line fit to them gives $0.9167-1.2495/N$. This agrees well with the predicted behavior $11/12+5/4N$ for coplanar states [3]. The apparent divergence of the metastable $\sqrt{3}$×$\sqrt{3}$ specific heat indicates a possible pseudo-critical point. No such divergence in $c_{\mathrm{v}}$ is present for the metastable spin liquid.

![](./images/7465802857918103644_3.png)

FIG. 4. Main panel: The specific heat vs. $T$ for a system with linear size $L=300$. Black points are derived from the spin-liquid branch in Fig. 2 while pink points come from the corresponding $\sqrt{3}$×$\sqrt{3}$ branch. Fainter colors mark when a given branch becomes metastable. Upper inset: Specific heat at $T=0$ for different inverse system sizes. Lower inset: Specific heat vs. $T$ for the pyrochlore lattice antiferromagnet with $4\times 36^3$ sites.

A comparison between NBT and MC reveals two central differences: First, the low-temperature state found by NBT is quantitatively different from the one inferred from earlier MC simulations. Despite both approaches showing $\sqrt{3}$×$\sqrt{3}$ correlations, the ordered moment saturates within NBT, whereas in MC simulations it remains strongly suppressed at about $10\%$ of the NBT values [7, 9]. Second, instead of showing a clear signature of a weak phase transition, MC simulations of $c_{\mathrm{v}}$ show a broad plateau that ends around $T\approx 4\cdot 10^{-3}$, followed by a steep decrease [7, 22].

In MC simulations, a latent heat delta-function would appear as a peak at $T_c$ with height $(\ell_h/2T_c)^2N\approx 10^{-3}N$ and width $(2T_c)^2/(\ell_h N)\approx 0.1/N$ [23, 24]. Such a peak is hard to capture in finite-size MC simulations as it will be very narrow and sit on top of a discontinuity. Furthermore, MC equilibration across different domain-wall sectors is presumably slow at low temperatures. We therefore consider it plausible that, in the vicinity of the phase transition, conventional MC simulations may not be fully

![](./images/7465802857918103644_4.png)

FIG. 5. Main panel: $J_2$-$T$ phase diagram. Solid lines indicate weak first-order phase transitions and dashed lines indicate crossovers. Critical points are marked by stars. Lower right inset: Blow-up of the region around the triple point. Upper left inset: Latent heat per spin of the phase transitions from the spin liquid to the ordered phases as a function of $J_2$.

equilibrated and that the resulting configurations contain domains of both phases. This picture of phase coexis- tence near a weak first-order transition is consistent with the structure factor observed in MC simulations, which is reminiscent of a mixture of the $\sqrt{3} \times \sqrt{3}$ structure factor and the intermediate-temperature spin-liquid structure factor [7]. It should nevertheless be mentioned that the onset of coplanar ordering in MC simulations has been suggested to correspond to a topological (phase) transi- tion [7].

The permanently reduced ordered moment in MC sim- ulations is also consistent with phase coexistence, but has been attributed instead to the proliferation of copla- nar domain walls between $\sqrt{3} \times \sqrt{3}$ domains with opposite chirality, while keeping the system within the ground- state manifold [6], consistent with a saturating octupolar order parameter as $T \to 0$. However, it is not clear that domain-walls will proliferate at low temperatures in equi- librium. Even though domain-wall states have a large configurational multiplicity and therefore substantial en- tropic weight, domain walls stiffen the spin configuration and thereby reduce the entropic advantage compared to the $\sqrt{3} \times \sqrt{3}$ state [8]. This subtle competition between the configurational entropy of domain-wall states and the entropic gain of soft modes in the $\sqrt{3} \times \sqrt{3}$ state is difficult to settle.

To test the robustness of the weak first-order phase transition, we extend our analysis to finite second- neighbor coupling $J_2$. The resulting $J_2$-$T$ phase diagram in Fig. 5 contains two finite lines of first-order transitions that separate the disordered spin-liquid regime from two distinct low-temperature ordered phases: the $\sqrt{3} \times \sqrt{3}$ phase for ferromagnetic $J_2 < 0$ and the $\vec{q}=0$ phase for antiferromagnetic $J_2 > 0$. A blow-up of the small $J_2$-region, see right inset of Fig. 5, further reveals that the $\sqrt{3} \times \sqrt{3}$ phase extends slightly into the antiferromag- netic $J_2$ side at finite temperatures, consistent with the $\sqrt{3} \times \sqrt{3}$ state having higher spin-wave entropy than the $\vec{q}=0$ state [8]. The fact that the $\sqrt{3} \times \sqrt{3}$ phase pro trudes slightly into the region $J_2 > 0$ naturally explains the existence of the first-order transition in the nearest- neighbor model ($J_2=0$). The two first-order lines meet in a triple point at $(J_2,T_c)=(2.8 \cdot 10^{-5},1.11 \cdot 10^{-3})$ where the spin liquid, $\sqrt{3} \times \sqrt{3}$ and $\vec{q}=0$ phases coexist with a finite, but small $\sim 10^{-4}$, latent heat. The $\sqrt{3} \times \sqrt{3}$ and $\vec{q}=0$ phases are separated by a third line of first-order transitions.

The upper inset of Fig. 5 shows the latent heat per spin associated with the spin liquid to (local) order tran- sitions. They are all weakly first order ($\ell_h < 6 \cdot 10^{-3}$), and exist only over a limited range of $J_2$ before they ter- minate at critical points, marked by stars at $(J_2,T_c)=$ $(-2.139 \cdot 10^{-3},1.27 \cdot 10^{-2})$ and $(1.239 \cdot 10^{-2},4.94 \cdot 10^{-2})$, where the latent heat vanishes. Outside of the critical points we do not detect phase transitions, but instead crossovers associated with a finite peak in the specific heat that diverges at the critical points.

This extension partly agrees with earlier MC work on the $J_1$-$J_2$ kagome model [25]. For antiferromagnetic cou- plings $J_2 < 7.5 \cdot 10^{-3}$, MC simulations and NBT both find first-order phase transitions into the $\vec{q}=0$ phase, with comparable latent heats and transition tempera- tures. In particular, at $J_2=5 \cdot 10^{-3}$, the NBT values of $\ell_h=5.02 \cdot 10^{-3}$ and $T_c=2.61 \cdot 10^{-2}$ are close to the MC values. However, for large $J_2$, both ferromagnetic and antiferromagnetic, NBT indicates only crossovers, whereas MC simulations have been interpreted in terms of 2D Ising-type continuous phase transitions. Our re- sults suggest that the apparent scaling indicative of such behavior is instead a finite-size effect that disappears for sufficiently large system sizes (see Supplemental Material Sec. E [17]). For small ferromagnetic $J_2$, the MC simula- tions report a double-peak structure in the specific heat as a function of temperature. The high-temperature peak has been associated with a crossover into a $\sqrt{3} \times \sqrt{3}$ phase of reduced ordered moment, while there is an additional unclassified transition at lower temperature into the fully ordered $\sqrt{3} \times \sqrt{3}$ phase. NBT, by contrast, finds a single first-order phase transition into the $\sqrt{3} \times \sqrt{3}$ phase.

For comparison, we have applied NBT also to the nearest-neighbor pyrochlore Heisenberg antiferromagnet, the canonical three-dimensional classical spin liquid [26–29]. In that case we find no analogous ordered branch that overtakes the spin liquid at low temperatures (see Supplemental Material Sec. F [17]). Within NBT, the

pyrochlore antiferromagnet remains disordered down to
the lowest temperatures studied, with a specific heat ap-
proaching the value $0.7500 - 1.5001/N$, see lower inset
of Fig. 4. The infinite-size value agrees well with $3/4$ re-
ported in Ref. 29. This contrast emphasizes that the
kagome result is not an artifact of the NBT method
generically producing spurious order in highly frustrated
systems; instead, it reflects a genuine distinction between
two archetypal classical spin liquids.

It is appropriate to mention that the NBT method is
approximate, as the diagrammatic treatment of the con-
straint field excludes vertex corrections (see Supplemen-
tal Material Sec. A [17]). Nevertheless, NBT has previ-
ously produced the correct phases and phase transitions
for other frustrated models [16, 30], but typically overes-
timates critical temperatures by 10-20% [14]. Thus, all
temperatures presented in this Letter should be under-
stood as estimates. As NBT relies on convergence from
an initial self-energy, and different initial self-energies
could realize different converged phases, there is always
a possibility that we have not found the correct thermo-
dynamically stable state due to bad initialization. We
have therefore also performed NBT simulations with ini-
tial self-energies obtained from MC simulations. How-
ever, instead of stabilizing an alternative phase, they all
converge to either the spin liquid or to the $\sqrt{3} \times \sqrt{3}$ phase
(see Supplemental Material Sec. G [17]).

In conclusion, we have used NBT to shine new light on
a critical problem in classical frustrated magnetism: the
nearest-neighbor kagome Heisenberg antiferromagnet
does not merely drift into a coplanar regime through
crossover physics, but exits its spin-liquid regime through
a genuine, though weak, first-order phase transition.
The low-temperature phase is the $\sqrt{3} \times \sqrt{3}$ phase which
ordered moment saturates as $T \to 0$.

C.G. acknowledges funding from the European Union's
Horizon Europe research and innovation programme un-
der the Marie Skłodowska-Curie Grant Agreement No.
101126636. The computations were performed on re-
sources provided by Sigma2 - the National Infrastruc-
ture for High Performance Computing and Data Storage
in Norway, and on the Fox supercomputer at the Univer-
sity of Oslo.

[1] C. Lacroix, P. Mendels, and F. Mila, eds., *Introduction
to Frustrated Magnetism: Materials, Experiments, The-
ory*, Springer Series in Solid-State Sciences, Vol. 164
(Springer, Berlin, Heidelberg, 2011).

[2] A. B. Harris, C. Kallin, and A. J. Berlinsky, Phys. Rev.
B **45**, 2899 (1992).

[3] J. T. Chalker, P. C. W. Holdsworth, and E. F. Shender,
Phys. Rev. Lett. **68**, 855 (1992).

[4] D. A. Huse and A. D. Rutenberg, Phys. Rev. B **45**, 7536
(1992).

[5] S. Sachdev, Phys. Rev. B **45**, 12377 (1992).

[6] J. N. Reimers and A. J. Berlinsky, Phys. Rev. B **48**, 9539
(1993).

[7] M. E. Zhitomirsky, Phys. Rev. B **78**, 094423 (2008).

[8] C. L. Henley, Phys. Rev. B **80**, 180401 (2009).

[9] G.-W. Chern and R. Moessner, Phys. Rev. Lett. **110**,
077201 (2013).

[10] Villain, J., Bidaux, R., Carton, J.-P., and Conte, R., J.
Phys. France **41**, 1263 (1980).

[11] I. Ritchey, P. Chandra, and P. Coleman, Phys. Rev. B
**47**, 15342 (1993).

[12] J. T. Chalker, in *Topological Aspects of Condensed
Matter Physics: Lecture Notes of the Les Houches
Summer School: Volume 103, August 2014*, edited
by C. Chamon, M. O. Goerbig, R. Moessner, and
L. F. Cugliandolo (Oxford University Press, 2017)
https://academic.oup.com/book/0/chapter/203968137/chapter-
pdf/45121870/acprof-9780198785781-chapter-3.pdf.

[13] Michael Schecter and Olav F. Syljuåsen and Jens Paaske,
Physical Review Letters **119**, 157202 (2017).

[14] O. F. Syljuåsen, J. Paaske, and M. Schecter, Phys. Rev.
B **99**, 174404 (2019).

[15] C. Glittum and O. F. Syljuåsen, Phys. Rev. B **104**,
184427 (2021).

[16] C. Glittum and O. F. Syljuåsen, Phys. Rev. B **108**,
014413 (2023).

[17] See Supplemental Material at [URL will be inserted by
publisher] for details.

[18] D. A. Garanin and B. Canals, Phys. Rev. B **59**, 443
(1999).

[19] O. Janson, J. Richter, and H. Rosner, Phys. Rev. Lett.
**101**, 106403 (2008).

[20] L. Messio, C. Lhuillier, and G. Misguich, Phys. Rev. B
**83**, 184401 (2011).

[21] N. D. Mermin and H. Wagner, Phys. Rev. Lett. **17**, 1133
(1966).

[22] S. Schnabel and D. P. Landau, Phys. Rev. B **86**, 014413
(2012).

[23] Y. Imry, Phys. Rev. B **21**, 2042 (1980).

[24] W. Janke, First-order phase transitions, in *Com-
puter Simulations of Surfaces and Interfaces*, edited by
B. Dünweg, D. P. Landau, and A. I. Milchev (Springer
Netherlands, Dordrecht, 2003) pp. 111–135.

[25] M. Spenke and S. Guertler, Phys. Rev. B **86**, 054440
(2012).

[26] J. Villain, Zeitschrift für Physik B Condensed Matter **33**,
31 (1979).

[27] J. N. Reimers, A. J. Berlinsky, and A.-C. Shi, Phys. Rev.
B **43**, 865 (1991).

[28] J. N. Reimers, Phys. Rev. B **45**, 7287 (1992).

[29] R. Moessner and J. T. Chalker, Phys. Rev. Lett. **80**, 2929
(1998).

[30] C. Glittum and O. F. Syljuåsen, Journal of Physics: Con-
densed Matter **38**, 135801 (2026).

## SUPPLEMENTAL MATERIAL

### A. Nematic Bond Theory

The Nematic Bond Theory (NBT) [1–4] is an extension of the self-consistent Gaussian approximation (SCGA) [5] that goes beyond it by suppressing fluctuations in the lengths of the spins. To explain how it is used in this paper we begin by formulating it on the kagome lattice.

The kagome lattice can be treated as a triangular Bravais lattice with a three-site unit cell. The coordinate of the unit cell will be denoted $\vec{R}$ and can be expressed in terms of the triangular Bravais lattice vectors $\vec{a}_1=(1,0)$ and $\vec{a}_2=(-1/2,\sqrt{3}/2)$. For convenience, we also define $\vec{a}_3=-\vec{a}_1-\vec{a}_2=(-1/2,-\sqrt{3}/2)$. We have chosen the lattice spacing on the Bravais lattice to be unity, which means that the lattice spacing on the kagome lattice itself is one half. A site within a unit cell will be indexed by its sublattice index $i\in\{1,2,3\}$ so that its position within the unit cell $\vec{\alpha}_i$ takes one of the three values $\{(0,0),(1/2,0),(1/4,\sqrt{3}/4)\}$. A site on the kagome lattice can then be uniquely defined by its sublattice index $i$ and unit cell $\vec{R}$, so that for the spin at $\vec{r}=\vec{R}+\vec{\alpha}_i$, we write $\vec{S}_{\vec{r}=\vec{R}+\alpha_i}\equiv\vec{S}_{\vec{R},i}$.

The Hamiltonian of the Heisenberg model is
$$
H = \frac{1}{2}\sum_{\vec{R},i}\sum_{\vec{R}',j} J_{\vec{R}'-\vec{R},ij} \vec{S}_{\vec{R},i} \cdot \vec{S}_{\vec{R}',j}, \tag{3}
$$
where $J_{\vec{R}'-\vec{R},ij}$ denotes the exchange coupling between the spin at sublattice $i$ in unit cell $\vec{R}$ and the spin at sublattice $j$ in unit cell $\vec{R}'$. The factor $1/2$ is inserted to avoid double counting. We then introduce Fourier transforms
$$
\vec{S}_{\vec{R},i} = \frac{1}{\sqrt{N_c}} \sum_{\vec{q}} \vec{S}_{\vec{q},i} e^{i\vec{q}\cdot\vec{R}}, \tag{4}
$$

$$
J_{\vec{R},ij} = \frac{2}{N_c} \sum_{\vec{q}} J_{\vec{q},ij} e^{-i\vec{q}\cdot\vec{R}}, \tag{5}
$$
where the $\vec{q}$-sums go over the first Brillouin zone of the triangular Bravais lattice, and $N_c$ is the total number of unit cells so that the total number of spins is $N=3N_c$. The Fourier conventions have been chosen differently for $\vec{S}$ and $J$ for notational convenience. The Hamiltonian can then be written compactly
$$
H = \sum_{\vec{q}} \sum_{ij} J_{\vec{q},ij} \vec{S}_{\vec{q},i}^* \cdot \vec{S}_{\vec{q},j}, \tag{6}
$$
where $J_{\vec{q},ij}$ can be interpreted as the components of a three-by-three matrix with $\vec{q}$-dependent entries, and we have used $\vec{S}_{-\vec{q},i}=\vec{S}_{\vec{q},i}^*$. For the kagome lattice the matrix $2J_{\vec{q}}$ is
$$
\begin{pmatrix}
0 & J_1(1+e^{-iq_1})+J_2(e^{iq_2}+e^{iq_3}) & J_1(1+e^{iq_3})+J_2(e^{-iq_1}+e^{-iq_2}) \\
J_1(1+e^{iq_1})+J_2(e^{-iq_2}+e^{-iq_3}) & 0 & J_1(1+e^{-iq_2})+J_2(e^{iq_3}+e^{iq_1}) \\
J_1(1+e^{-iq_3})+J_2(e^{iq_1}+e^{iq_2}) & J_1(1+e^{iq_2})+J_2(e^{-iq_3}+e^{-iq_1}) & 0
\end{pmatrix}, \tag{7}
$$
where $q_i=\vec{q}\cdot\vec{a}_i$. In order to ensure that the matrix $J_{\vec{q}}$ is positive definite we will redefine it by subtracting its minimum eigenvalue. This corresponds to subtracting a constant in the Hamiltonian, and has no consequence for the physical properties of the model.

To obtain the free energy we will compute the partition function for the canonical ensemble $Z$ by integrating over all spins
$$
Z = \int \prod_{\vec{R},i} d\vec{S}_{\vec{R},i} e^{-\beta H}. \tag{8}
$$

The unit-length constraint on the spins will be taken into account by delta-functions written as an integral over a constraint field $\lambda_{\vec{R},i}$ at each site:
$$
\prod_{\vec{R},i} \delta(|\vec{S}_{\vec{R},i}|-1) = \int \prod_{\vec{R},i} \frac{\beta d\lambda_{\vec{R},i}}{\pi} e^{-i\beta\lambda_{\vec{R},i}(\vec{S}_{\vec{R},i}\cdot\vec{S}_{\vec{R},i}-1)}, \tag{9}
$$

where we for convenience have scaled the integration variables by the inverse temperature $\beta$. Then defining the Fourier-transformed constraint field $\lambda_{\vec{q},i}$ so that

$$
\lambda_{\vec{R},i} = \sum_{\vec{q}} \lambda_{\vec{q},i} e^{i \vec{q} \cdot \vec{R}}. \tag{10}
$$

The sum in the exponent of the integrand can then be written in terms of Fourier transformed quantities

$$
\sum_{\vec{R},i} \lambda_{\vec{R},i} \left( \vec{S}_{\vec{R},i} \cdot \vec{S}_{\vec{R},i} - 1 \right) = \sum_{\vec{q} \neq 0,i} \lambda_{\vec{q},i} \left( \sum_{\vec{q}'} \vec{S}_{\vec{q}+\vec{q}',i}^{*} \cdot \vec{S}_{\vec{q}',i} \right) + \sum_{i} \lambda_{\vec{q}=0,i} \left( \sum_{\vec{q}'} \vec{S}_{\vec{q}',i}^{*} \cdot \vec{S}_{\vec{q}',i} - N_c \right), \tag{11}
$$

where the $\vec{q}=0$ components have been written separately. The quantity $\sum_{\vec{q}'} \vec{S}_{\vec{q}+\vec{q}',i}^{*} \cdot \vec{S}_{\vec{q}',i}$ can be interpreted as the spatial modulation of the squared spin length on sublattice $i$ with wave vector $\vec{q}$. Thus the integrations over $\lambda_{\vec{q} \neq 0,i}$ force these modulations to be zero, i.e. no spatial variations of the (squared) spin lengths. In contrast the $\lambda_{\vec{q}=0,i}$ integration forces the sum of the squared spin lengths on sublattice $i$ to add up to $N_c$. Together they thus enforce the local constraint that each spin has unit length. We will treat the integrations over $\lambda_{\vec{q} \neq 0,i}$ in an approximate way using diagrams, and the integrations over $\lambda_{\vec{q}=0,i}$ using the saddle-point method. To emphasize this distinction, we will use another symbol for the $\vec{q}=0$ components: $\lambda_{\vec{q}=0,i} \equiv -i \Delta_i$, and from now on interpret $\lambda_{\vec{q},i}$ as having zero $\vec{q}=0$ components. Putting everything together, the partition function becomes

$$
Z = \int D \Delta D \lambda D S \ e^{-S} \tag{12}
$$

with

$$
S = \sum_{\vec{q},\vec{q}',\alpha,i,j} S_{\vec{q},i}^{\alpha *} \left[ (J_{\vec{q},ij} + \Delta_i \delta_{ij}) \delta_{\vec{q},\vec{q}'} - (-i) \lambda_{\vec{q}-\vec{q}',i} \delta_{ij} \right] S_{\vec{q}',j}^{\alpha} - \beta N_c \sum_{i} \Delta_i, \tag{13}
$$

where the spins have been rescaled by a factor $\sqrt{\beta}$.

In order to construct a diagrammatic theory, we introduce the bare inverse spin propagator $\mathcal{K}$, which is a matrix in the combined $\vec{q}$ and sublattice space with matrix elements $\mathcal{K}_{(\vec{q}i)(\vec{q}'j)} = \mathcal{K}_{\vec{q},ij} \delta_{\vec{q},\vec{q}'}$, where

$$
\mathcal{K}_{\vec{q},ij} \equiv J_{\vec{q},ij} + \Delta_i \delta_{ij}. \tag{14}
$$

We also define the constraint field $\boldsymbol{\Lambda}$ as a matrix containing the constraint field components, with matrix elements

$$
\Lambda_{(\vec{q}i)(\vec{q}'j)} = -i \lambda_{\vec{q}-\vec{q}',i} \delta_{ij}. \tag{15}
$$

Generalizing the number of spin components to $N_s$ and integrating over the spins, we arrive at the following expression for the partition function

$$
Z = \int D \Delta D \lambda \ e^{-(S_0+S_2+S_r)}, \tag{16}
$$

where we have omitted field-independent constants, and divided the remainder into terms according to their powers of $\boldsymbol{\Lambda}$ so that

$$
S_0 = -\beta N_c \sum_{i} \Delta_i + \frac{N_s}{2} \text{Tr} \ln \mathcal{K}, \tag{17}
$$

$$
S_2 = -\frac{N_s}{2 \cdot 2} \text{Tr} \left( \mathcal{K}^{-1} \boldsymbol{\Lambda} \mathcal{K}^{-1} \boldsymbol{\Lambda} \right), \tag{18}
$$

$$
S_r = -\sum_{l=3}^{\infty} \frac{N_s}{2 \cdot l} \text{Tr} \left( \mathcal{K}^{-1} \boldsymbol{\Lambda} \right)^l. \tag{19}
$$

The Tr-symbol indicates the trace over the combined $\vec{q}$ and sublattice space. There is no $S_1$-term as the constraint field has no $\vec{q}=0$ components. The term $S_2$ can be written

$$
S_2 = \frac{N_s}{2 \cdot 2} \sum_{\vec{q},i} \sum_{\vec{q}',j} \mathcal{K}_{\vec{q},ij}^{-1} \lambda_{\vec{q}-\vec{q}',j} \mathcal{K}_{\vec{q}',ji}^{-1} \lambda_{\vec{q}'-\vec{q},i} = \frac{N_s}{2 \cdot 2} \sum_{\vec{q},i} \sum_{\vec{q}',j} \lambda_{\vec{q}'-\vec{q},i} \mathcal{K}_{\vec{q},ij}^{-1} \mathcal{K}_{\vec{q}',ji}^{-1} \lambda_{\vec{q}-\vec{q}',j}. \tag{20}
$$

![](./images/7465802857918103644_5.png)

FIG. 6. Dyson equations for the renormalized spin propagator $K_{\vec{q}, i j}^{-1}$ (bold solid line), and the renormalized constraint-field propagator $D_{\vec{q}, i j}$ (bold wavy line).

![](./images/7465802857918103644_6.png)

FIG. 7. Self-consistent equations for the self-energy $\Sigma_{\vec{q}, i j}$ and polarization $\Pi_{\vec{q}, i j}$.

Changing summation variables $\vec{q} \to \vec{q}+\vec{q}'$ and $\vec{q}' \to \vec{p}$, one gets
$$
S_{2}=\frac{N_{s}}{2 \cdot 2} \sum_{\vec{q}, i} \sum_{\vec{p}, j} \lambda_{-\vec{q}, i} \mathcal{K}_{\vec{q}+\vec{p}, i j}^{-1} \mathcal{K}_{\vec{p}, j i}^{-1} \lambda_{\vec{q}, j},
\tag{21}
$$
and $S_{2}$ defines therefore the bare inverse constraint-field propagator $\mathcal{D}^{-1}$ with components $\mathcal{D}_{(\vec{q} i)\left(\vec{q}^{\prime} j\right)}^{-1}=D_{\vec{q} i j}^{-1} \delta_{\vec{q}, \vec{q}^{\prime}}$, where
$$
D_{\vec{q} i j}^{-1}=\frac{N_{s}}{2} \sum_{\vec{p}} \mathcal{K}_{\vec{p}+\vec{q}, i j}^{-1} \mathcal{K}_{\vec{p}, j i}^{-1}.
\tag{22}
$$

Diagrammatically we will represent the bare constraint-field propagator $\mathcal{D}_{\vec{q}, i j}$ as a thin wavy line, and the spin propagator $\mathcal{K}_{\vec{q}, i j}^{-1}$ as a thin solid line with an arrow, carrying momentum $\vec{q}$ (in the arrow direction) from $i$ to $j$. Diagramatically the term $S_{r}$ for $r \geq 3$ is a ring of thin solid line segments having $r$ hooks to attach wavy lines to. Such a ring carries a factor $N_{s}$ and a wavy line carries a factor $1/N_{s}$.

In order to capture symmetry-breaking phenomena going beyond simple perturbation theory, we construct a diagrammatic theory with renormalized propagators. In particular, $K_{\vec{q}, i j}^{-1}$ refers to the renormalized spin propagator with a self-energy addition $\Sigma_{\vec{q}, i j}$ in its denominator
$$
K_{\vec{q}, i j}=J_{\vec{q}, i j}+\Delta_{i} \delta_{i j}+\Sigma_{\vec{q}, i j}.
\tag{23}
$$

Note that in comparison to Ref. 4 we have changed the sign on the definition of the self-energy. The renormalized constraint-field propagator is written in terms of the renormalized spin propagators as
$$
D_{\vec{q}, i j}^{-1}=\frac{N_{s}}{2} \sum_{\vec{p}} K_{\vec{q}+\vec{p}, i j}^{-1} K_{\vec{p}, j i}^{-1},
\tag{24}
$$
and the self-energy is taken to be the dressed Fock diagram
$$
\Sigma_{\vec{q}, i j}=\sum_{\vec{p} \neq 0} K_{\vec{q}-\vec{p}, i j}^{-1} D_{\vec{p}, i j},
\tag{25}
$$
calculated with fully dressed propagators, but leaving out vertex corrections. Diagramatically these renormalizations correspond to the resummations shown in Fig. 6, with the self-energy and polarization shown in Fig. 7.

The constraint field can then be formally integrated out, which gives
$$
Z=\int D \Delta e^{-S^{\prime}},
\tag{26}
$$

![](./images/7465802857918103644_7.png)

FIG. 8. Leading-order omitted diagrams. Wavy lines indicate the constraint-field propagator $\mathcal{D}$ which contains a factor $1/N_s$. Solid lines indicate the spin propagator $\mathcal{K}^{-1}$. A closed solid loop carries a factor $N_s$.

where
$$
S^{\prime}=-\beta N_{c} \sum_{i} \Delta_{i}+\frac{N_{s}}{2} \sum_{\vec{q}} \ln \operatorname{det} K_{\vec{q}}+\frac{1}{2} \sum_{\vec{q} \neq 0} \ln \operatorname{det} D_{\vec{q}}^{-1}-\frac{N_{s}}{2} \sum_{\vec{q}} \operatorname{tr}\left(K_{\vec{q}}^{-1} \Sigma_{\vec{q}}\right).
\tag{27}
$$

We have here employed the notation where $K_{\vec{q}}$ means a three-by-three sublattice matrix with matrix elements $K_{\vec{q}, i j}$ (similar for $D_{\vec{q}}^{-1}$ and $\Sigma_{\vec{q}}$), and the $\operatorname{det}(\operatorname{tr})$-symbol indicates taking the determinant(trace) in this sublattice space. To arrive at this expression, we have neglected diagrams in a systematic large-$N_s$ expansion as described in appendix A of Ref. 3. The leading-order diagrams being omitted (shown in Fig. 8), and hence the error in the free energy, are of order $1/N_s$.

The final integrals over the $\Delta_i$s are calculated using the saddle-point method. Differentiating $S'$ w.r.t. $\Delta_i$ we arrive at the three saddle-point equations giving the inverse temperature
$$
\beta=\frac{N_{s}}{2 N_{c}} \sum_{\vec{q}} K_{\vec{q}, i i}^{-1},
\tag{28}
$$
where no sum over $i$ is implied. This simple form is a consequence of the fact that the contributions from the two last terms in Eq. (27) cancel each other (cf. Ref. 3). The three equations Eq. (28) enforce the average spin length on each sublattice $i$ to be unity, and they must all give the same temperature for the solution to be physical. It should be noted that since $\Sigma_{\vec{q}}$ is not fixed, it is possible to have several sets $\{(\Sigma_{\vec{q}}^{(1)}, \Delta^{(1)}), (\Sigma_{\vec{q}}^{(2)}, \Delta^{(2)}), \ldots\}$ which give the same value for the sum in Eq. (28), i.e. the same (inverse) temperature. Given this possible multivaluedness, we view Eq. (28) as equations that give the temperature for a given value of the $\Delta_i$s and $\Sigma_{\vec{q}}$.

The self-consistent equations (23), (24) and (25) are solved by iteration, starting typically from a random self-energy and equal values of the $\Delta_i$s. Each iteration gives an overall positive contribution to the self-energy. To avoid the general increase in temperature associated with this, the $\Delta_i$s are renormalized in every iteration by subtracting from them the minimum eigenvalue among all $\Sigma_{\vec{q}}$ matrices. In addition, each $\Delta_i$ is adjusted very slightly so that Eq. (28) give the same value of the temperature for all sublattices. We iterate until the temperature in subsequent iterations has converged, and then employ the converged $K_{\vec{q}}^{-1}$, $\Sigma_{\vec{q}}$ and $D_{\vec{q}}$ to calculate the free energy. Specifically we use the convergence criterion that three subsequent iterations are required to have temperatures that differ by at most by $10^{-13}$. Typically, $10-200$ iterations are needed for convergence.

After reaching convergence, we calculate the free energy per spin at the converged temperature $T$ as follows
$$
f=-\frac{N_{s} T}{2 N} \sum_{\vec{q}} \ln \operatorname{det}\left(\pi T K_{\vec{q}}^{-1}\right)+\frac{T}{2 N} \sum_{\vec{q}} \ln \operatorname{det}\left(\frac{\pi T^{2}}{2 N_{c}} D_{\vec{q}}^{-1}\right)-\frac{N_{c}}{N} \sum_{i} \Delta_{i}-\frac{N_{s} T}{2 N} \operatorname{tr}\left(K_{\vec{q}}^{-1} \Sigma_{\vec{q}}\right),
\tag{29}
$$
where the renormalized values of the $\Delta_i$s should be used. We have also reinstated factors from the integration measures.

To get information about the spin correlations we calculate the quantity
$$
A_{\vec{q}} \equiv \sum_{i j} K_{\vec{q}, i j}^{-1} e^{-i \vec{q} \cdot\left(\vec{\alpha}_{i}-\vec{\alpha}_{j}\right)},
\tag{30}
$$
which is closely related to the spin structure factor $S(\vec{q}) \equiv \sum_{i j}\langle\vec{S}_{-\vec{q}, i} \cdot \vec{S}_{\vec{q}, j}\rangle e^{i \vec{q}(\alpha_{i}-\alpha_{j})}=N_s T(A_{\vec{q}}+A_{-\vec{q}})/4$.

### B. Spin-liquid real-space correlations

We compute the real-space correlations in the spin liquid as
$$
\left\langle\vec{S}_{0, i} \cdot \vec{S}_{\vec{R}, j}\right\rangle=\frac{1}{N_{c}} \sum_{\vec{q}}\langle\vec{S}_{-\vec{q}, i} \cdot \vec{S}_{\vec{q}, j}\rangle e^{i \vec{q} \cdot \vec{R}}=\frac{N_{s} T}{4 N_{c}} \sum_{\vec{q}}\left(K_{-\vec{q}, i j}^{-1}+K_{\vec{q}, j i}^{-1}\right) e^{i \vec{q} \cdot \vec{R}},
\tag{31}
$$

![](./images/7465802857918103644_8.png)

FIG. 9. Left: Real-space correlations in the spin liquid at sublattice 1 as function of distance $R$ between the spins for two different temperatures. Values smaller than $10^{-17}$ are not shown. Right: Extracted values for the power-law exponent $a$ and correlation length $\xi$ as function of temperature. $L=600$.

and fit them to the functional form

$$
\langle \vec{S}_{0,i} \cdot \vec{S}_{\vec{R},j} \rangle \propto \frac{1}{R^a} e^{-R/\xi}, \tag{32}
$$

where $R \equiv |\vec{R}|$, and $a$ is an exponent characterizing a power-law decay at distances smaller than the correlation length $\xi$.

For low temperatures, the correlation length is expected to be long, and consequently $\langle \vec{S}_{0,i} \cdot \vec{S}_{\vec{R},j} \rangle \propto 1/R^a$. $a$ can thus be extracted as the slope in a log-log plot, see Fig. 9 left upper panel. We find that the straight-line fits work well for $T < 10^{-3}$. The resulting exponents are shown in the right upper panel, giving $a=1.94 \approx 2$, in accordance with Ref. 6. For higher temperatures, the correlation length is small, and the exponential decay dominates. For these temperatures, we can find the correlation length by extracting the negative inverse of the slope in a semi-log plot, see left lower panel. These fits work well for $T > 10^{-5}$. The resulting correlation lengths for different temperatures are shown in the right lower panel as a log-log plot. We find a slope of $-0.48 \approx -1/2$. Thus, the correlation length is estimated to go as $\xi \propto 1/\sqrt{T}$, also in accordance with Ref. 6.

## C. Finite-size behavior of the critical temperature and latent heat

The critical temperature $T_c$ and latent heat per spin $\ell_h$ are extracted from the crossing of the spin liquid and the $\sqrt{3} \times \sqrt{3}$ free-energy branches. $T_c$ is determined as the crossing temperature, and the difference in slopes of the two branches at the crossing is multiplied by $T_c$ to give the latent heat per spin. The results for different system sizes are plotted vs. the inverse system size $1/N$ in Fig. 10. The points are fitted to a quadratic polynomial in $1/N$ (shown as the lines in the plots) and the infinite-size behavior is extracted, see figure caption.

## D. Low-temperature behavior of the specific heat

In Fig. 11, we show the specific heat $c_v$ in the $\sqrt{3} \times \sqrt{3}$ phase at very low temperatures ($T < 10^{-6}$) for several system sizes indicated by the legends. We have plotted $c_v$ vs. $\sqrt{T}$ and fitted the points to straight lines which works very well at these low temperatures. The $y$-axis intercepts of the fitted lines are plotted in the inset vs. inverse system size and fitted to a straight line $c_v(T=0)=0.9167-1.2495/N$.

![](./images/7465802857918103644_9.png)

FIG. 10. Upper panel: The latent heat per spin of the phase transition vs. inverse system size. Lower panel: $T_c$ vs. inverse system size. The quadratic fits extrapolate to a latent heat of $1.0449\cdot 10^{-4}$ and a critical temperature $T_c=1.59294\cdot 10^{-3}$ for infinite system size.

![](./images/7465802857918103644_10.png)

FIG. 11. Specific heat vs. square root of temperature at low temperatures for different linear system sizes $L$ indicated by the legends. The dashed lines show fits to the functions $c_\mathrm{v}(T)=a+b\sqrt{T}$. The inset (also shown in the main text in Fig. 4 upper inset) shows the $y$-intercepts $a$ vs $1/N$ ($N=3L^2$), and the dashed line is a linear fit to these points giving $c_\mathrm{v}(T=0)=0.9167-1.2495/N$.

### E. Crossover peak for $J_2=-0.02$

For $J_2$ values lying outside the critical points, the specific heat exhibits a broad peak at the dashed lines in Fig. 5 in the main text. For $J_2=-0.02$ this peak was studied in Ref. 7 for linear system sizes $L\leq 24$. They concluded that the peak indicates a phase transition in the 2D Ising universality class. We show in Fig. 12 that NBT on the

![](./images/7465802857918103644_11.png)

FIG. 12. Left: Specific heat peaks at $J_2=-0.02$ for different linear system sizes $L$ indicated by the numbers and gray scale (darker curves correspond to larger system sizes). Right: Temperature and height of the corresponding peak maxima vs. inverse system size.

contrary reveals substantial finite-size effects in this system which should not be interpreted as indications of a phase transition. Fig. 12 (left) shows the specific heat peak obtained in NBT vs. temperature at $J_2=-0.02$ for different linear system sizes. As in Ref. 7, for small $L\leq15$, the peak grows and moves down in temperature as $L$ increases. However, when increasing $L$ further, we find that the peak shrinks, and for $L\simeq36-45$ its shape reveals two features; a low-temperature peak that shrinks and becomes a shoulder before it eventually disappears for larger system sizes, and a robust feature at a slightly higher temperature that develops into a stable broad peak that do not evolve further with system size. We take this latter broad peak to indicate a crossover rather than a phase transition. In the right panel of Fig. 12 we summarize how the temperature and height of the peak maximum behave with inverse system size. The marked change around $L=42$ is a consequence of the development of the stable broad peak.

### F. Pyrochlore antiferromagnet

We have also used NBT for the pyrochlore nearest-neighbor antiferromagnet and compared free energies of the spin liquid with the Néel [8-10] and SLP-X [4, 11] states, which are colinear ground states in the vicinity of the pure antiferromagnetic point, see left panel of Fig. 13. For temperatures $T>10^{-10}$, it is clear that the free energies of the competing states is higher than for the spin liquid. In the inset, we show $\Delta f/T$, the free-energy difference between the competing states and the spin liquid divided by temperature, which stays almost constant at a positive value as $T\rightarrow0$. We cannot rule out that these lines will eventually cross zero, but based on the flatness of the curves, it can only happen at extremely low temperatures.

We have also repeated the specific heat calculation for the pyrochlore lattice, see right panel of Fig. 13, which shows the specific heat for the spin liquid at very low temperatures for different system sizes. In contrast to the kagome lattice, $c_{\text{v}}$ behaves linearly on $T$ at low temperatures. The extrapolated $T=0$ values of the specific heat are plotted in the inset vs. inverse system size and fitted to a straight line, $c_{\text{v}}(T=0)=0.7500-1.5001/N$.

### G. Search for alternative stable states

NBT relies on convergence from an initial self-energy. This has the advantage that free energies of different states can be obtained - also those that are metastable. However, a disadvantage is that one cannot know that all states with low free energy have been found. As described in the main text, we have searched for low free-energy states by

![](./images/7465802857918103644_12.png)

FIG. 13. Left: Free energy per spin for the pyrochlore antiferromagnet for the different phases indicated by the legends. The inset shows the free-energy difference of the biased curves from the spin liquid and is divided by temperature. A term $aT$ with $a=13$ has been subtracted in the main plot to better visualize the difference between the free energies. $L=12$. Right: Pyrochlore specific heat vs. temperature at low temperatures for different linear system sizes $L$ indicated by the legends. The dashed lines show fits to the functions $c_\text{v}(T)=a+bT$. Although difficult to see, the values of $b$ are approximately 1. The inset shows the $y$-intercepts $a$ vs $1/N$ ($N=4L^3$), and the dashed line is a linear fit to these points giving $c_\text{v}(T=0)=0.7500-1.5001/N$.

![](./images/7465802857918103644_13.png)

FIG. 14. Free energy per spin for NBT simulations initiated with self-energies gotten from MC simulations at temperatures indicated by the legends (colored circles). Here the average MC correlation function is used. The solid and dashed lines are the free energies obtained by NBT of the spin liquid and $\sqrt{3} \times \sqrt{3}$ phase, respectively. $L=12$. $a=3$. The inset shows a blow-up of the phase-transition region.

running NBT for slightly perturbed systems, and picked the converged self-energy of those as initial self-energies for the nearest-neighbor model at low values of $\Delta$. This gives the free energies shown in Fig. 2 in the main text.

We have also biased NBT with initial self-energies obtained from Monte Carlo (MC) simulations. The MC sim- ulations were carried out starting from a random spin state at high temperature, and then gradually lowering the temperature to the desired one. We used four different temperatures $T = \{0.001, 0.005, 0.01, 0.02\}$, and a linear system size $L = 12$. We used the Metropolis algorithm with updates in which the proposed spin is selected in a cone around the old spin [12, 13]. The cone is adjusted during equilibration to get acceptance probability one-half [14]. After equilibrating for $10^8$ MC steps, the spin correlation function was calculated and converted to a self-energy. We used correlation functions based on both single-configuration snapshots, and on MC averages (for another $10^8$ MC steps). In all, three initial self-energies (two based on independent MC snapshots, and one based on MC averages) were investigated for each temperature.

For each of the twelve different MC initial self-energies, we ran 800 NBT simulations with different $\Delta$-values equally spaced on a log-scale in the interval $[10^{-9}, 1]$, all starting with the same initial self-energy. The converged free energies and temperatures were recorded. They are shown as colored circles in Fig. 14 for the case where the initial self-energies are based on the average over $10^8$ MC configurations. The runs initiated with MC snapshots are similar. We find that *all* these runs either converge to the spin-liquid branch or to the $\sqrt{3} \times \sqrt{3}$ branch. For the runs initiated by MC snapshots, there is a trend that the NBT initiated by low-temperature configurations has a tendency of converging to the $\sqrt{3} \times \sqrt{3}$ branch. However, and perhaps somewhat surprisingly, the temperature of the MC configurations do not seem to play any significant role in which state the NBT converges to when the inital self-energy is based on MC *averages*, at least not for the four temperatures we have investigated.

[1] Michael Schecter and Olav F. Syljuåsen and Jens Paaske, *Physical Review Letters* **119**, 157202 (2017).
[2] O. F. Syljuåsen, J. Paaske, and M. Schecter, *Phys. Rev. B* **99**, 174404 (2019).
[3] C. Glittum and O. F. Syljuåsen, *Phys. Rev. B* **104**, 184427 (2021).
[4] C. Glittum and O. F. Syljuåsen, *Phys. Rev. B* **108**, 014413 (2023).
[5] J. T. Chalker, in *Topological Aspects of Condensed Matter Physics: Lecture Notes of the Les Houches Summer School: Volume 103, August 2014*, edited by C. Chamon, M. O. Goerbig, R. Moessner, and L. F. Cugliandolo (Oxford University Press, 2017) https://academic.oup.com/book/0/chapter/203968137/chapter-pdf/45121870/acprof-9780198785781-chapter-3.pdf.
[6] D. A. Garanin and B. Canals, *Phys. Rev. B* **59**, 443 (1999).
[7] M. Spenke and S. Guertler, *Phys. Rev. B* **86**, 054440 (2012).
[8] G.-W. Chern, R. Moessner, and O. Tchernyshyov, *Phys. Rev. B* **78**, 144418 (2008).
[9] M. F. Lapa and C. L. Henley, *Ground States of the Classical Antiferromagnet on the Pyrochlore Lattice* (2012), arXiv:1210.6810 [cond-mat.str-el].
[10] Iqbal, Yasir and Müller, Tobias and Ghosh, Pratyay and Gingras, Michel J. P. and Jeschke, Harald O. and Rachel, Stephan and Reuther, Johannes and Thomale, Ronny, *Phys. Rev. X* **9**, 011005 (2019).
[11] P. Ghosh, Y. Iqbal, T. Müller, R. T. Ponnaganti, R. Thomale, R. Narayanan, J. Reuther, M. J. P. Gingras, and H. O. Jeschke, *npj Quantum Materials* **4**, 63 (2019).
[12] D. Hinzke and U. Nowak, *Computer Physics Communications* **121-122**, 334 (1999), proceedings of the Europhysics Conference on Computational Physics CCP 1998.
[13] D. P. Landau and K. Binder, *A Guide to Monte Carlo Simulations in Statistical Physics*, 3rd ed. (Cambridge University Press, 2009).
[14] J D Alzate-Cardona and D Sabogal-Suárez and R F L Evans and E Restrepo-Parra, *Journal of Physics: Condensed Matter* **31**, 095802 (2019).