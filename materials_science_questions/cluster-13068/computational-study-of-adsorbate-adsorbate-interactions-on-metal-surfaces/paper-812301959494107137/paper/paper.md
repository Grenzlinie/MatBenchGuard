### Stiffening Transition in Vicinal Surfaces with Adsorption

Noriko AKUTSU*,\*) Yasuhiro AKUTSU**,\**) and Takao YAMAMOTO***,\***)

* Faculty of Engineering, Osaka Electro-Communication University
Neyagawa 572-8530, Japan
** Department of Physics, Graduate School of Science, Osaka University
Toyonaka 560-0011, Japan
*** Department of Physics, Faculty of Engineering, Gunma University
Kiryu 376-0052, Japan

(Received September 7, 2000)

We study the vicinal surface with adsorption below the roughening temperature, using a solid-on-solid model coupled with the Ising model. We calculate the step tension $\gamma$ and the step-interaction coefficient $B$ using the density matrix algorithm. We find a temperature $T_{\mathrm{s}}$ where $B$ vanishes and that the surface free energy has the form $f(p)-f(0)=\gamma p+(\mathrm{const}) p^{5}+\cdots$, where $p$ is the surface gradient.

Below the roughening temperature $T_{\mathrm{R}}$, a vicinal surface, which is a surface that is slightly tilted relative to one of the facet planes of a crystal, is described well in terms of terraces, steps and kinks (the "TSK picture"). Since systems whose "elementary excitation" is an extended linear object (like the step), belong to the Gruber-MullinsPokrovsky-Talapov (GMPT) universality class, $^{1)-7)}$ we have the following form of the vicinal surface free energy (per projected area):

$$
f(p)=f(0)+\gamma p+B p^{3}+O\left(p^{4}\right), \tag{1}
$$

where $p$ ($\propto$ step density $\rho$) is the surface gradient. This $p$-$p^{3}$ form of expansion is characteristic of the GMPT universality class. Physically, $\gamma$ is the step tension, and $B$ represents the effect of step-step interactions. To be precise, $\gamma$ and $B$ depend on the mean running direction angle (relative to one of the crystal axes on the facet plane) of the steps, which we denote by $\theta$; we should then write $\gamma=\gamma(\theta, T)$ and $B=B(\theta, T)$ (where $T$ is the temperature). If we set up the $x$-$y$ coordinates on the facet plane so that the $y$-axis corresponds to $\theta=0$ (i.e., steps are along the $y$ direction), the angle $\theta$ is related to the surface gradients $p_{x}$ (along the $x$ direction) and $p_{y}$ (along the $y$ direction) as $^{8)}$

$$
p_{x}=-a_{h} \rho \cos \theta, \quad p_{y}=-a_{h} \rho \sin \theta, \tag{2}
$$

where $a_{h}$ is the height of a single step. (For convenience, we adopt units in which $a_{h}=1$ in the following.) With (2), we can regard the free energy $f$ as a function of the gradient vector $\boldsymbol{p}=(p_{x}, p_{y})$, allowing us to write $f=f(\boldsymbol{p})$. For systems in which

*) E-mail: nori@phys.osakac.ac.jp
**) E-mail: acts@phys.sci.osaka-u.ac.jp
***) E-mail: yamamoto@phys.eg.gunma-u.ac.jp

the step-step interaction is short ranged, there exists the following universal relation between $\gamma(\theta, T)$ and $B(\theta, T)^{8), 9)}$ (which leads to the universal Gaussian curvature jump at the facet edge $^{8)-11)}$ ):

$$
B(\theta, T)=\frac{\pi^{2}}{6} \frac{\left(k_{\mathrm{B}} T\right)^{2}}{\tilde{\gamma}(\theta, T)}. \tag{3}
$$

Here $k_{\mathrm{B}}$ is the Boltzmann constant and $\tilde{\gamma}(\theta, T)$, defined by

$$
\tilde{\gamma}(\theta, T)=\gamma(\theta, T)+\partial^{2} \gamma(\theta, T) / \partial \theta^{2}, \tag{4}
$$

is the step stiffness. The manner in which the long-range (inverse-square) step- step interaction modifies the relation (3) is also known. $^{10), 12)}$ Since the essential mechanism of the GMPT form (1) is the non-penetrability of steps, the universality of this form and also of the relation (3) are fairly "robust". However, for adsorbed vicinal surfaces, there may occur breakdown of the GMPT form at a temperature $T_{\mathrm{s}}$ where $B(\theta, T)$ vanishes. We demonstrate this in the present paper. Since the smallness of $B$ is characteristic of a low-temperature stiff surface, the anomalous behavior at $T_{\mathrm{s}}$ may be called a stiffening transition.

It is known that adsorbed atoms often change properties of a surface. $^{7), 13)-22)}$ Recently, the adsorption effect on the behavior of a step has been studied experimen- tally. $^{17)-22)}$ In this paper, to study the adsorption effect on the vicinal surface, we consider the restricted solid-on-solid (RSOS) model $^{23)}$ on a square lattice, coupled with an Ising spin system representing an adsorbed gas. In the RSOS model, we restrict each nearest-neighbor (nn) height difference $\Delta h$ to be $\Delta h=0, \pm 1$, which is a reasonable simplification, because configurations with large $|\Delta h|$ are energetically unfavorable.

We assume that the gas atoms are likely to adsorb at step edge positions and that the adsorbed atom modifies the ledge energy locally. The Ising spins are, then, located on the bonds of the square lattice where the RSOS model is defined; the Ising spins form a $45^{\circ}$-rotated square lattice. We further assume ferromagnetic interactions (attractive interactions in the lattice-gas picture) with coupling constant $J$ between nearest-neighbor spins on the rotated square lattice. We assume a simple linear modification of the ledge energy as $\epsilon \rightarrow \epsilon(1-\alpha \sigma)$ (where $\sigma$ is an Ising spin). This modification leads to the interaction between the RSOS system and the Ising system. The Hamiltonian of the RSOS-Ising coupled model is, therefore, written as

$$
\mathcal{H}=\sum_{\langle i, j\rangle} \epsilon\left(1-\alpha \sigma_{b(i, j)}\right)\left|h_{i}-h_{j}\right|-J \sum_{\left\langle b, b^{\prime}\right\rangle} \sigma_{b} \sigma_{b^{\prime}}, \tag{5}
$$

where $h_{i}$ is the integer surface height at site $i, \epsilon$ is the "bare" ledge energy and $\sigma_{b(i, j)}=\pm 1$ is the Ising spin variable on the bond $b(i, j)$ connecting the nn site pair $\langle i, j\rangle$. We should note that the RSOS condition $(|\Delta h| \leq 1$ for each nn site pair) is implicit in (5).

We analyze the model with the transfer-matrix method. For this purpose, we extend the well-known mapping between the RSOS model and the vertex model on the dual lattice, $^{23), 24)}$ to obtain a "decorated" vertex model (Fig. 1). The decorated

vertex model can again be regarded as
a 6-state vertex model with $19 \times 16 =$
304 non-zero vertex weights (304-vertex
model). For approximate diagonaliza-
tion of the transfer matrix, we employ
the product-wavefunction renormaliza-
tion group (PWFRG) method, $^{25),26)}$
which is a variant of White's density
matrix renormalization group (DMRG)
method $^{27)}$ (the "infinite-system" algo-
rithm, to be precise). The PWFRG is
specially designed to obtain the fixed
point (i.e. thermodynamic limit of the
system $^{28)}$ ) of the DMRG efficiently. For the vicinal surface problem, we have veri-
fied the reliability of the PWFRG method $^{29)}$ ; even with a small number of "retained
bases" (in the DMRG/PWFRG terminology), the method gives close-to-exact re-
sults.

![](./images/812301959494107137_1.jpg)

Fig. 1. (a)RSOS heights $(h_{1},\cdots,h_{4})$ and
edge variables in the mapped vertex model.
(b) Decorated-vertex-model representation
of the RSOS-Ising coupled system. Ising
spins are represented by circles.

For calculation of $\gamma(\theta,T)$ and $B(\theta,T)$ in (1), we use an approach similar to that
used in Ref. 29), where we obtained $\gamma$ and $\tilde{\gamma}$ for $2 \times 1$-reconstructed $Si(001).^{30),31)}$ We
introduce the Andreev field $\eta^{32)}$ along the $x$ direction to tilt the surface by adding the
term $-\eta \sum_{m,n}(h_{(m+1,n)}-h_{(m,n)})$ to the Hamiltonian (5). (Here $(m,n)$ is the position
vector of the lattice site.) In the vertex-model representation, the surface gradient
$p$ along the $x$ direction is just the thermal average of the vertical edge variable of
the vertex model, which can easily be calculated from the fixed-point wavefunction
obtained by the PWFRG. By sweeping the field $\eta$, we obtain a $p$ - $\eta$ curve. [The actual
calculation is very similar to that of the magnetization curve for spin chains. $^{26),33)}$
(See also, Ref. 34).).] From the standard argument $^{32)}$ using Andreev's Legendre
transformation, $p \to \eta, f(p) \to \tilde{f}(\eta)=f(p)-p \eta \ (\eta=\partial f(p)/\partial p)$, we have from (1)
(with $\rho=p$)
$$
\eta=\gamma+3 B p^{2}+\text { (higher order). } \tag{6}
$$

Hence, from the PWFRG calculation, we obtain the $p$ - $\eta$ curve and perform the
least-square fitting to obtain $\gamma$ and $B$. For the actual fitting, we adopt the fitting
form
$$
\eta=A_{0}+A_{2} p^{2}+A_{3} p^{3}+A_{4} p^{4}, \tag{7}
$$
since the coefficients $A_{3}$ and $A_{4}$ may not be small. If the relation (3) holds, we obtain
the step stiffness $\tilde{\gamma}(0)$ as
$$
\tilde{\gamma}(0)=\frac{\pi^{2}\left(k_{\mathrm{B}} T\right)^{2}}{2 A_{2}}. \tag{8}
$$

In Fig. 2, we plot $p$ - $\beta \eta$ curves $[\beta=1/(k_{\mathrm{B}} T)]$ for $\alpha=0.5$ and $J=0.15$ calculated
with the PWFRG at certain temperatures. In Fig. 3, we display the temperature
dependence of $\tilde{\gamma}(0)$ obtained from (8). In contrast to the "normal" cases, where
$\tilde{\gamma}$ is a monotonically decreasing function of temperature, our $\tilde{\gamma}$ clearly exhibits a
diverging anomaly at $T_{\mathrm{s}}\ (k_{\mathrm{B}} T_{\mathrm{s}}/\epsilon \approx 0.4)$. The step tension $\gamma(0)$, on the other hand,
behaves smoothly near $T_{\mathrm{s}}$, with only weak "reentrance".

![](./images/812301959494107137_2.jpg)

Fig. 2. PWFRG results for the $p$-$\beta\eta$ curves
($\alpha = 0.5$ and $J = 0.15$). Temperature of
each curve is $k_{\rm B}T/\epsilon = 0.3, 0.35, 0.4, 0.45$,
and 0.5, from right to left.

![](./images/812301959494107137_3.jpg)

Fig. 3. Temperature dependence of step stiff-
ness $\tilde{\gamma}(0)$ (triangles) and step tension $\gamma(0)$
(circles) (semi-log plot). The solid and bro-
ken lines are guides to the eye.

At $T_{\rm s}$, both $A_2$ and $A_3$ in (7) become very small. The $\eta$-$p$ curve is then well
fitted by
$$
\eta = A_0 + A_4 p^4 + A_5 p^5 + \cdots, \tag{9}
$$
which is equivalent to the non-GMPT form of expansion
$$
f(p) = f(0) + \gamma p + C_5 p^5 + (\text{higher order}). \tag{10}
$$

We have thus found a vanishing of $B$ at a temperature $T_{\rm s}$ in theRSOS-Ising coupled
system, which we call a “stiffening transition”. As for the $p$-$\eta$ curve, we should have a
change in the critical behavior, from the ordinary square-root type $^{35)}$ $p \sim (\eta - \eta_c)^{1/2}$
($\eta > \eta_c$, $\eta_c = \gamma$) to a new one, $p \sim (\eta - \eta_c)^{1/4}$. We should stress that the stiffening
transition has nothing to do with the roughening transition, which takes place well
above $T_{\rm s}$. (We estimate $k_{\rm B}T_{\rm R}/\epsilon \sim 1.35$ in the present case.)

We propose two possible mechanisms of the stiffening transition: (1) a “single-
particle” mechanism, and (2) an intrinsically many-body mechanism. The first one
is based on the “universal free-fermion picture” of the vicinal surface $^8)$ in a direct
way. In the transfer-matrix treatment for the coarse-grained vicinal surface, the
statistical-mechanical problem of a many-step system is equivalent to finding the
ground state of a free-fermion system in one dimension. From this point of view,
the ordinary parabolic dispersion of the single-particle energy $\omega(k) \sim \sigma k^2$ (near
$k \sim 0$) is the source of the $\rho^3$-term in (1) with $B = \sigma \pi^2/3$. Hence, the vanishing
of $B$ and appearance of the non-GMPT form (10) can be simply interpreted as the
change of $\omega(k)$ from $k^2$-type to $k^4$-type. Since $\tilde{\gamma}$ is inversely proportional to the
(scaled) squared fluctuation width characterizing the step roughness, $^{36)}$ we should
have step-smoothening behavior at $T_{\rm s}$.

The second mechanism is based on the formation of “bound states” of steps. If
we “integrate out” the Ising-degrees of freedom, we have an effectiveRSOS model
with effective interactions. If this interaction amounts to attraction between the
steps, the formation of a “bound state” (or, “bound steps”, “step bunch”) may
become possible. Suppose that steps form $n$-body bound states. We regard each

bunch of steps as a "composite particle" and assume that the free-fermion picture itself is valid for the system of composite particles. By $\rho_n$, $\gamma_n$ and $\tilde{\gamma}_n$, we denote the density, formation free energy, and stiffness of the $n$-body step bunch. Note that we have $p = n\rho_n$, and roughly $\gamma_n \sim n\gamma_1$ and $\tilde{\gamma}_n \sim n\tilde{\gamma}_1$. $^{37)}$ From a simple dimensional analysis, we see that in the expansion (1) of the vicinal-surface free energy $f(p)$, the coefficient $B$ scales as $B \sim 1/n^4$. Hence, if $n$ diverges then $B$ vanishes, and $T_{\mathrm{s}}$ is the condensation temperature of the steps.

To summarize, we have discussed the adsorption effect on the vicinal surface below the roughening temperature in terms of the restricted solid-on-solid model coupled with the Ising model. By employing the product-wavefunction renormaliza- tion group method, we have obtained the temperature dependence of the step tension and step stiffness. We have found a stiffening transition at which the step interaction coefficient vanishes, and at the same time, we have found that the vicinal surface free energy takes a form that differs form that of the Gruber-Mullins-Pokrovsky- Talapov-type.

We should note that anomalous increase of step stiffness has been observed $^{19)}$ for boron (B)-doped Si(001). A similar phenomenon has also been observed $^{20)}$ for high temperature $Si(111)$ , where a Si adatom layer is known to exist. $^{38)-41)}$ The stiffening transition we have found may have relevance to these anomalous types of behavior. In this Letter, we have restricted our analysis to a special (but typical, in our view) set of parameter values of the model. To explore a full parameter space is an important problem, which may lead to the discovery of other interesting phenomena and may also lead to clarification of the mechanism of the stiffening transition.

This work was partially supported by the "Research for the Future" Program of the Japan Society for the Promotion of Science (JSPS-RFTF97P00201) and by a Grant-in-Aid for Scientific Research from the Ministry of Education, Science, Sports and Culture (No. 09640462 and No. 12640393).

1) E. E. Gruber and W. W. Mullins, J. Phys. Chem. Solids 28 (1967), 6549.
V. L. Pokrovsky and A. L. Talapov, Phys. Rev. Lett. 42 (1979), 65 [Sov. Phys. -JETP 51(1980), 134].
2) F. D. M. Haldane and J. Villain, J. de Phys. 42 (1981), 1673.
3) T. Izuyama and Y. Akutsu, J. Phys. Soc. Jpn. 51 (1982), 50.
T. Yamamoto and T. Izuyama, J. Phys. Soc. Jpn. 56 (1987), 632.
4) C. Jayaprakash, W. F. Saam and S. Teitel, Phys. Rev. Lett. 50 (1983), 2017.
5) H. J. Schultz, J. de Phys. 46 (1985), 257.
G. F. Gallet, P. Noziéres, S. Balibar and E. Rolley, Europhys. Lett. 2 (1986), 701.
6) H. van Beijeren and I. Nolden, in Structure and Dynamics of Surfaces, ed. W. Schommers and P. von Blancken-hagen (Springer-Verlag, Berlin, Heidelberg, 1987), vol. 2, p. 259.
7) A. Pimpinelli and J. Villain, Physics of Crystal Growth (Cambridge University Press,1998).
8) Y. Akutsu, N. Akutsu and T. Yamamoto, Phys. Rev. Lett. 61 (1988), 424.
9) T. Yamamoto, Y. Akutsu and N. Akutsu, J. Phys. Soc. Jpn. 57 (1988), 453.
10) W. F. Saam, Phys. Rev. Lett. 62 (1989), 2636.
11) L. V. Mikheev and V. L. Pokrovsky, J. de Phys. I 1 (1991), 373.
R. Sato and Y. Akutsu, J. Phys. Soc. Jpn. 64 (1995), 3593.

J. D. Noh and D. Kim, Phys. Rev. **E53** (1996), 3225.

12) N. C. Bartelt, T. L. Einstein and E. D. Williams, Surf. Sci. **276** (1992), 308.
T. Yamamoto, Y. Akutsu and N. Akutsu, J. Phys. Soc. Jpn. **63** (1994), 915.

13) D. J. Eaglesham, F. C. Unterwald and D. C. Jacobson, Phys. Rev. Lett. **70** (1993), 966.

14) M. C. Desjonquéres and D. Spanjaard, *Concepts in Surface Physics*, Second Edition (Springer-Verlag, Berlin, Heidelberg, 1993, 1996).

15) M. Copel, M. C. Reuter, Efthimios Kaxiras and R. M. Tromp, Phys. Rev. Lett. **63** (1989), 632.

16) D. E. Jones, J. P. Pelz, Y. Hong, E. Bauer and I. S. T. Tsong, Phys. Rev. Lett. **77** (1996), 330.

17) K. Fujita, Y. Kusumi and M. Ichikawa, Surf. Sci. **357-358** (1995), 490; Phys. Rev. **B58** (1998), 1126.

18) X.-s. Wang and E. D. Williams, Surf. Sci. **400** (1998), 220.

19) J. B. Hannon, N. C. Bartelt, B. S. Swartzentruber, J. C. Hamilton and G. L. Kellogg, Phys. Rev. Lett. **79** (1997), 4226.

20) A. V. Latyshev, H. Minoda, Y. Tanishiro and K. Yagi, Phys. Rev. Lett. **76** (1996), 94.

21) J. S. Ozcomert, W. W. Pai, N. C. Bartelt and J. E. Reutt-Robey, Phys. Rev. Lett. **72** (1994), 258.

22) M. Horn-von Hoegen, H. Minoda, K. Yagi, F. Meyer zu Heringdorf and D. Kähler, Surf. Sci. **402-404** (1998), 464.
H. Minoda, K. Yagi, F.-J. Meyer zu Heringdorf, A. Meier, D. Kähler and M. Horn-von Hoegen, Phys. Rev. **B59** (1999), 2363.

23) K. Sogo, Y. Akutsu and T. Abe, Prog. Theor. Phys. **70** (1983), 739.
T. T. Truong and M. den Nijs, J. of Phys. **A19** (1986), L645.

24) H. van Beijeren, Phys. Rev. Lett. **38** (1977), 993.

25) T. Nishino and K. Okunishi, J. Phys. Soc. Jpn. **64** (1995), 4084.

26) Y. Hieida, K. Okunishi and Y. Akutsu, Phys. Lett. **A233** (1997), 464.

27) S. R. White, Phys. Rev. Lett. **69** (1992), 2863.
T. Nishino, J. Phys. Soc. Jpn. **64** (1995), 3598.

28) S. Östlund and S. Rommer, Phys. Rev. Lett **75** (1995), 3537; Phys. Rev. **B55** (1997), 2164.

29) N. Akutsu and Y. Akutsu, Phys. Rev. **B57** (1998), R4233; Surf. Sci. **376** (1997), 92.

30) B. S. Swartzentruber, Y.-W. Mo, R. Kariotis, M. G. Lagally and M. B. Webb, Phys. Rev. Lett. **65** (1990), 1913.
B. S. Swartzentruber and M. Schacht, Surf. Sci. **322** (1995), 83.

31) N. C. Bartelt, R. M. Tromp and E. D. Williams, Phys. Rev. Lett. **73** (1994), 1656.

32) A. F. Andreev, Zh. Eksp. Theor. Fiz. **80** (1981), 2042 [Sov. Phys. -JETP **53** (1982), 1063].

33) K. Okunishi, Y. Hieida and Y. Akutsu, Phys. Rev. **B59** (1999), 6806.

34) Y. Honda and T. Horiguchi, Phys. Rev. **E56** (1997), 3920.

35) C. Rottman, M. Wortis, J. C. Heyraud and J. J. Métois, Phys. Rev. Lett. **52** (1984), 1009.
Y. Carmi, S. G. Lipson and E. Polturak, Phys. Rev. **B36** (1987), 1894.
E. Rolley, E. Chevalier, C. Guthmann and S. Balibar, Phys. Rev. Lett. **72** (1994), 872.

36) M. P. A. Fisher, D. S. Fisher and J. D. Weeks, Phys. Rev. Lett. **48** (1982), 368.
Y. Akutsu and N. Akutsu, J. of Phys. **A19** (1986), 2813.
J. de Coninck and J. Ruiz, J. of Phys. **A21** (1988), L147.
D. B. Abraham and P. J. Upton, Phys. Rev. **B37** (1988), 3835.

37) K. Sudoh, T. Yoshinobu, H. Iwasaki and E. D. Williams, Phys. Rev. Lett. **80** (1998), 5152.

38) S. Ino, Jpn. J. Appl. Phys. **16** (1977), 891.
H. Iwasaki, S. Hasegawa, M. Akizumi, S.-Te Li, S, Nakamura and J. Kanamori, J. Phys. Soc. Jpn. **56** (1987), 3425.

39) S. Kohmoto and A. Ichimiya, Surf. Sci. **223** (1989), 400.

40) A. V. Latyshev, A. B. Krasilnikov, A. L. Aseev, L. V. Sokolov and S. I. Stenin, Surf. Sci. **254** (1991), 90.

41) Y.-N. Yang and E. D. Williams, Phys. Rev. Lett. **72** (1994), 1862.