# Relative Stability of f.c.c. and b.c.c. Structures for Model Systems at High Temperatures $(^{**})(^{**})$.

A. RAHMAN

Materials Science and Technology Division, Argonne National Laboratory Argonne, Ill. 60439, U.S.A.

G. JACUCCI

Dipartimento di Fisica dell'Università di Trento - 38050 Povo, Italia

(ricevuto il 20 Marzo 1984)

Summary. - Free-energy, entropy and volume differences between face-centered and body-centered cubic structures have been evaluated for model rare gas and alkali metal crystals by using the method of over- lapping distributions. Stable phases are predicted in agreement with the behaviour of real materials in the regions of validity of classical mechanics and in agreement with the results of previous dynamical-simulation studies of crystal nucleation from the melt and of polymorphic trans- formations. The existence of a stable b.c.c. phase at high pressure and temperatures is predicted in this way for Lennard-Jones solids, while no high-pressure f.c.c. phase is expected for model Rb and Cs systems. We also show the possibility of making calculations of free-energy bar- riers to displacive crystalline transformations along a prescribed tra- jectory in configuration space.

PACS. 64.70. - Phase equilibria, phase transitions, and critical points of specific substances.

(*) To speed up publication, the authors of this paper have agreed to not receive the proofs for correction.
(**) Work supported by the U.S. Department of Energy, Istituto per la Ricerca Scientifica e Tecnologica, Trento, and Gruppo Nazionale di Struttura della Materia del C.N.R., Italy.

### 1. - Introduction.

To understand how different lattice structures arise in nature, one needs to postulate the interaction potential between various particles and then to use it to evaluate the relevant thermodynamic potential which ensures the stability of one structure relative to another. For complex materials the first already is a formidable problem. For certain classes of monatomic materials (rare-gas solids, alkali metals) the problem of the interaction potential is under- stood well enough so as to warrant a serious attack on the problem of evaluating thermodynamic-potential differences.

However, attempts have been made in the literature to solve the problem of the relative stability of lattice structures without detailed knowledge of the interactions. ZENER $(^{1})$, in particular, suggested that failure of certain shear modes could be responsible for low-temperature structural transformations in the light alkali metals, whereas FRIEDEL attempted to show $(^{2})$ that the b.c.c. phase has favorable higher entropy than the close-packed phase, this arising from first-neighbor interactions and the topology of the BCC structure. ALEXANDER and MCTAGUE went even further $(^{3})$ and used the Landau theory of melting transitions $(^{4})$ to show the « universal » preference of b.c.c. structures in all systems.

In recent years molecular dynamics and Monte Carlo calculations $(^{5})$ have made it possible to go beyond the realm of conjecture and unrealistic general arguments. In a study of homogeneous nucleation in monatomic supercooled fluids it has been found that the structure of the nucleated phase is sensitive to the pair potential $(^{6})$. Specifically, a potential $V_{1}$ (say, a Lennard-Jones pair interaction) gave rise to structure $S_{1}$ (a close packed structure) by homo geneous nucleation, while $V_{2}$ (an alkali metal) gave $S_{2}$ (a b.c.c. structure).Already in these studies it was shown that a system with potential function $V_{1}$ nucleating into structure $S_{1}$ would spontaneously change its structure to $S_{2}$ when the potential function was switched to $V_{2}$.

(1) C. ZENER: in Phase Stability in Metals and Alloys, edited by P.S. RUDMAN, J. STRINGER and R.I. JAFFEE (McGraw-Hill, New York, N.Y., 1967), p. 25.
(2) J. FRIEDEL: J. Phys. (Paris) Lett., 35, 159 (1974).
(3) S. ALEXANDER and J. MCTAGUE: Phys. Rev. Lett., 41, 702 (1978).
(4) L.D. LANDAU: Phys. Z. Sowjetunion, 11, 26, 545 (1937).
(5) See, for example, a) Modern Theoretical Chemistry, Vol. 5, edited by B.J. BERNE(Plenum Press, New York, N.Y., 1977) and b) W.W. WooD and J.J. ERPENBECK: Annu. Rev. Phys. Chem., 27, 319 (1976).
(6) C.S .Hsu and A. RAHMAN: a) J. Chem. Phys., 70, 5234 (1979); b) 71, 4974 (1979).

Even more recently $(^{7})$ it has become possible to study, by molecular-dynamics techniques, the behavior of perfect crystalline solids at constant external stress in such a way as to allow the solid the freedom to adopt a dif- ferent structure if the ambient temperature and pressure conditions make a change favorable.

This new method of studying polymorphic transitions has also been applied successfully to the study of such transitions in the relatively more complicated case of binary ionic systems (KCl, AgI) $(^{8})$.

Thus it has now become necessary to attempt to calculate, by fundamental statistical mechanics, the free-energy differences between various crystalline structures, given the potential of interaction. The methodology for pursuing such a program now exists and various facets of this methodology will be dealt with in an appropriate section below.

The purpose of the present paper is to report the results of some initial calculations on two potential functions and two structures. For a Lennard- Jones system we have evaluated $F_{F}-F_{B}$, where $F$ is the Helmholtz free energy and subscripts F and B stand for f.c.c. and b.c.c., respectively.

Another class of systems for which a quantitatively accurate theoretical Hamiltonian is available in the literature is that of alkali metals. The pertur- bation theory provides an effective ionic-pair interaction between the alkali ions embedded in a sea of conduction electrons. Because of the quantitative reliability of these predictions, we have considered it profitable to undertake a study of crystalline alkali metals from the point of view of structural and free-energy differences.

Lennard-Jones systems and alkali metals have an added attraction for a study of f.c.c., b.c.c. structures and of free-energy differences between the structures because in the laboratory rare-gas solids (for which LJ is a good model system) crystallize as a close-packed structure and alkali metals as a b.c.c. structure.

From the point of view of fundamental theory, recent developments $(^{9})$ have shown how to calculate the change in thermodynamic potentials as systems freeze from liquid to solid; the same theory also shows how to calculate the free-energy difference between various structures in terms of correlation func- tions in the liquid state out of which the structures are nucleated. This is another reason why a serious attempt at calculating free-energy differences between various structures and for various model systems is called for.

(7) M. PARRINELLO and A. RAHMAN: Phys. Rev. Lett., 45, 1196 (1980); J. Appl. Phys.,52, 7182 (1981).
( $^{8})$ a) M. PARRINELLO and A. RAHMAN: J. Phys. (Paris), 42, C6-511 (1981); b) M. PARRI NELLO, A. RAHMAN and P. VASHISHTA: Phys. Rev. Lett., 50, 1073 (1983).
(9) T.V. RAMAKRISHNAN and M. YUsSOUFF: Phys. Rev. B, 19, 2775 (1979).

## 2. - Free-energy calculation.

In classical statistical mechanics the central problem is the evaluation of the configurational integral $Q$ that appears in the partition function $Z$:

$$
Q \equiv \int_{\Omega} \exp \left[-\beta V\left(\left\{\boldsymbol{r}_{i}\right\}\right)\right] \mathrm{d} \boldsymbol{r}_{1} \ldots \mathrm{d} \boldsymbol{r}_{i} \ldots \mathrm{d} \boldsymbol{r}_{N},
$$

$$
Z=\exp [-\beta F] \equiv\left(2 \pi m / \beta h^{2}\right)^{3 N / 2} Q.
$$

$F$ is the Helmholtz free energy, $\beta$ the inverse temperature, $h$ Planck's constant and $\Omega$ the volume of the $N$-particle system. The problem we wish to solve is that of the free-energy difference of two systems with potential functions $V_{1}$ and $V_{2}$ spanning the same configuration space $\left\{\boldsymbol{r}_{i}\right\} \equiv R$. In order to calculate this free-energy difference, we need

$$
Q_{1} / Q_{2}=\exp \left[-\beta\left(F_{1}-F_{2}\right)\right]=\int_{\Omega} \exp \left[-\beta V_{1}(R)\right] \mathrm{d} \tau / \int_{\Omega} \exp \left[-\beta V_{2}(R)\right] \mathrm{d} \tau.
$$

The integration extends over the same volume in the configuration space $R$. Simple algebraic manipulation gives

$$
\text { (1) } \quad\left\{\begin{array}{l}
Q_{1}=\int \exp \left[-\beta\left(V_{1}-V_{2}\right)\right] \exp \left[-\beta V_{2}\right] \mathrm{d} \tau, \\
Q_{1} / Q_{2}=\left\langle\exp \left[-\beta\left(V_{1}-V_{2}\right)\right]\right\rangle_{2},
\end{array}\right.
$$

where the symbol \langle\rangle$_{2}$ has an obvious meaning. This «one-sided» expression for $Q_{1} / Q_{2}$ and similarly a mirror image expression with 1,2 interchanged is a practical way of evaluating $\Delta F=F_{1}-F_{2}$ by sampling configurations from one of the two canonical ensembles.

A «two-sided», more symmetric, formulation is obtained as follows by constructing normalized distribution functions $h_{1}(\Delta)$ and $h_{2}(\Delta)$ in the canonical ensembles generated by $V_{1}$ and $V_{2}$, respectively. Thus, by definition,

$$
\begin{aligned}
& h_{1}(\Delta)=\int \delta\left(V_{1}-V_{2}-\Delta\right) \exp \left[-\beta V_{1}\right] \mathrm{d} \tau / Q_{1} \equiv\left\langle\delta\left(V_{1}-V_{2}-\Delta\right)\right\rangle_{1} \\
& h_{2}(\Delta)=\int \delta\left(V_{1}-V_{2}-\Delta\right) \exp \left[-\beta V_{2}\right] \mathrm{d} \tau / Q_{2} \equiv\left\langle\delta\left(V_{1}-V_{2}-\Delta\right)\right\rangle_{2}.
\end{aligned}
$$

But, by the same manipulation as before,

$$
\begin{aligned}
h_{1}(\Delta) & =\int \delta\left(V_{1}-V_{2}-\Delta\right) \exp \left[-\beta\left(V_{1}-V_{2}\right)\right] \exp \left[-B V_{2}\right] \mathrm{d} \tau / Q_{1}= \\
& =\exp [-\beta \Delta] \int \delta\left(V_{1}-V_{2}-\Delta\right) \exp \left[-\beta V_{2}\right] \mathrm{d} \tau / Q_{1}=\exp [-\beta \Delta] h_{2}(\Delta) Q_{2} / Q_{1}.
\end{aligned}
$$

Hence we have

$$
(2)\qquad Q_{1} / Q_{2}=\exp [-\beta \Delta] h_{2}(\Delta) / h_{1}(\Delta).
$$

The left-hand side being independent of $\Delta$, the right side gives a practical method of evaluating the fraction $Q_{1} / Q_{2}$. The functions $h_{i}(\Delta)$ can be estimated in a Monte Carlo sampling by compiling a histogram $h_{i}^{*}(\Delta)$ of the frequency of occurrence of configurations with $V_{1}-V_{2}$ between $\Delta-\delta / 2$ and $\Delta+\delta / 2$.

The introduction of these energy distribution overlap methods for the cal- culation of free-energy differences is due to VALLEAU and collaborators $(^{10})$ and to BENNETT $(^{11})$ , building upon earlier work of McDonald and Singer $(^{12})$ . An alternative equation for the two-sided evaluation was proposed by BEN- NETT $(^{11})$ ; this was denoted by him as the acceptance ratio method. This and other methods, including eq. (2), are discussed and compared in an illuminating paper $(^{11})$ by BENNETT, in which a complete treatment of the relative statistical error can also be found. Bennett's equation can be derived from the following identity:

$$
\int_{\Omega} w(R) \exp \left[-\beta\left(V_{1}+V_{2}\right] \mathrm{d} \tau=\left\langle w(R) \exp \left[-\beta V_{2}\right]\right\rangle_{1} Q_{1}=\left\langle w(R) \exp \left[-\beta V_{1}\right]\right\rangle_{2} Q_{2},\right.
$$

or

$$
(3)\qquad \frac{Q_{2}}{Q_{1}}=\frac{\left\langle w(R) \exp \left[-\beta V_{2}\right]\right\rangle_{1}}{\left\langle w(R) \exp \left[-\beta V_{1}\right]\right\rangle_{2}},
$$

where $w(R)$ is an arbitrary function of the configuration; the function $w$ was introduced by BENNETT in order to optimize the estimation of the free-energy difference $(1 / \beta) \ln (Q_{1} / Q_{2})$ . According to him $(^{11})$ statistical arguments can be used to show that the choice

$$
(4)\qquad w(R)=\text { const } x\left(\frac{Q_{2}}{n_{2}} \exp \left[-\beta V_{1}\right]+\frac{Q_{1}}{n_{1}} \exp \left[-\beta V_{2}\right]\right)^{-1},
$$

where $n_{1}, n_{2}$ are the numbers of statistically independent configurations from each Monte Carlo sample, minimizes the expectation value of $(\Delta F_{\text {est }}-\Delta F)^{2}$. Substituting eq. (4) in eq. (3) gives

$$
(5)\qquad \frac{Q_{2}}{Q_{1}}=\frac{\left\langle f\left(\beta\left(V_{1}-V_{2}\right)+c\right)\right\rangle_{1}}{\left\langle f\left(\beta\left(V_{1}-V_{2}\right)-c\right)\right\rangle_{2}} \exp [+c],
$$

(10) J.P. VALLEAU and G.M. TORRIE: Modern Theoretical Chemistry, Vol. 5, edited by B.J. BERNE (Plenum Press, New York, N.Y., 1977) and references therein.
(11) C.H. BENNETT: J. Comput. Phys., 22, 245 (1976).
(12) I. R. MCDONALD and K. SINGER: Discuss. Faraday Soc., 43, 40 (1967); J. Chem. Phys., 47, 4766 (1967); 50, 2308 (1969).

where $c=\ln (Q_{2}n_{1}/Q_{1}n_{2})$ and $f(x)=1/(1+\exp[x])$ is the Fermi function.
Equation (5) is true for any value of the shift constant $c$, but the particular value specified minimizes the expected square error $(^{11})$. The magnitude $\sigma^{2}$ of this minimum square error can be conveniently expressed in terms of $n_{1}$, $n_{2}$ and of the normalized variances of $f$ in ensembles 1 and $2(^{11})$:

$$
(6)\qquad \sigma^{2}=\frac{1}{n_{1}} \frac{\left\langle f^{2}\right\rangle_{1}-\langle f\rangle_{1}^{2}}{\langle f\rangle_{1}^{2}}+\frac{1}{n_{2}} \frac{\left\langle f^{2}\right\rangle_{2}-\langle f\rangle_{2}^{2}}{\langle f\rangle_{2}^{2}}.
$$

The use of Monte Carlo sampling to evaluate free-energy differences with eq. (2) or eq. (5) rests on, there being sufficient overlap between $h_{1}^{*}$ and $h_{2}^{*}$. This is clearly seen in eq. (2), since, if there is no overlap, the ratio $h_{1}^{*}/h_{2}^{*}$ cannot be estimated. The use of eq. (1) is even more critical, in that it requires es-sentially complete overlap of one of the two histograms by the other. We first note that, from eq. (1) and the definition of $h_{1}(\Delta)$ and $h_{2}(\Delta)$,

$$
\int h_{1}(\Delta) \mathrm{d} \Delta=1=\frac{Q_{2}}{Q_{1}}\left\langle\exp \left[-\beta\left(V_{1}-V_{2}\right)\right]\right\rangle_{2}=\frac{Q_{2}}{Q_{1}} \int_{-\infty}^{+\infty} h_{2}(\Delta) \exp [-\beta \Delta] \mathrm{d} \Delta.
$$

In regions of $\Delta$ where $h_{2}(\Delta)$ is small, the histogram $h_{2}^{*}(\Delta)$ will be zero. If $h_{1}=$ $=(Q_{2}/Q_{1})h_{2}\exp[-\beta\Delta]$ is significant in these regions, the use of $h_{2}^{*}$ will lead to very large errors since $Q_{1}/Q_{2}$ will be determined from the area in those re-gions. No such problem exists for the two-sided methods eqs. (2) and (5) if partial overlap of $h_{1}^{*}$ and $h_{2}^{*}$ exists. The statistical error, however, will depend strongly on the extent of the overlap $(^{11})$.

Where no overlap occurs, bridging distributions may be employed. These correspond to potential-energy functions intermediate between $V_{1}$ and $V_{2}$. When necessary, several such intermediate ensembles may be employed. This technique called «multistage sampling» rests on repeated applications of eqs. (2) or (5). Alternatively, if the gap between the two histograms $h_{i}^{*}$ is not much larger than their widths, a graphical method, proposed by BENNETT $(^{11})$, may be employed to extract the value of $Q_{2}/Q_{1}$. One gets from eq. (2)

$$
(7)\qquad \beta(F_{2}-F_{1})+\frac{1}{2}\beta\Delta+\log h_{1}(\Delta)=\log h_{2}(\Delta)-\frac{1}{2}\beta\Delta.
$$

We assumed that no values of $\Delta$ exist for which $h_{1}^{*}$ and $h_{2}^{*}$ are both non-zero. Hence eq. (7) is not directly useful. However, a plot of the quantities $\frac{1}{2}\beta\Delta+\log h_{1}(\Delta)$ and $\log h_{2}(\Delta)-\frac{1}{2}\beta\Delta$ against $\Delta$ produces two curves whose extrapolations into the gap are separated by the constant vertical displace-ment $\beta(F_{2}-F_{1})$. The free-energy difference can then be read easily from the graph (see fig. 1).

![](./images/812067928185765889_1.jpg)

Fig. 1. - Use of the graphical method (ref. (¹)) for the evaluation of free-energy differences in the case of little or no overlap between $h_{1}^{*}(\Delta)$ and $h_{2}^{*}(\Delta)$ (see the text). Data are taken from the comparison of an LJ crystal of f.c.c. structure to the correspond- ing quasi-harmonic model. From the above graph we get $\beta \Delta F$ per particle $=0.143 \pm$ \pm 0.002 at $T=0.5$ and $\varrho=1.0$.

## 3. - Strategy and methodology of the present work.

This section is divided in three subsections on the following topics:

a) crystal free energy and the f.c.c.-b.c.c. transformation,

b) alternative thermodynamical paths for multistage sampling,

c) choice of sampling algorithm.

The reader interested in technical procedures for the evaluation of $\Delta F$ and of its statistical error should refer to the preceding paper in this review (called I henceforth) and to ref. (¹¹) for material not included in sect. 2. Here we only note that the results presented in sect. 5 to 7 below are obtained with Bennett's method (¹¹), eq. (5) of sect. 2. The error quoted will be the expected error or square root of the variance given by eq. (6) of sect. 2. The numbers $n_{1}$ and $n_{2}$ representing the number of statistically independent configurations

from each Monte Carlo sample are obtained by making use of the correlation length $\tau$ in the way described in I. Results have also been obtained by using the simple two-sided overlap method in the form used by VALLEAU and and collaborators $^{(10)}$. In that case the quoted error is the root mean square deviation of the r.h.s. of eq. (2) of sect. 2 in the domain of values of the variable $\Delta$ where overlap of the histograms $h_{1}^{*}(\Delta)$ and $h_{2}^{*}(\Delta)$ occurs.

a) Crystal free energy and the f.c.c.-b.c.c. transformation. The standard way of evaluationg the free energy of crystals is from a normal-mode expansion of the potential energy $^{(13)}$. In the quasi-harmonic approximation knowledge of the normal-mode frequencies $v_{j}$ as functions of the density is all the information needed, besides the value of the potential energy of the geometrically perfect lattice. At high temperatures the partition function $Z$ of a three-dimensional harmonic crystal containing $N$ particles has the limiting form

$$
Z_{N}=\exp \left[-\beta V_{0}\right] \prod_{j=1}^{3 N-3}\left(k_{\mathrm{B}} T / h v_{j}\right) Z_{\mathrm{c}. \mathrm{m}.},
$$

where $V_{0}$ is the potential energy of the static lattice and $Z_{\text {c.m. }}$ is the center-ofmass contribution. Quite a bit is known about harmonic crystals, particularly with nearest-neighbor $(n-n)$ interaction. For example, the entropy for small crystals has been investigated $(^{14,15})$, and the excess (with respect to the Einstein model) Born-von Kármán harmonic entropies for the two close-packed three-dimensional periodic $(n-n)$ crystals have been obtained as functions of $N$ by HoOVER $^{(15)}$:

$$
\left(S^{e} / N k_{\mathrm{B}}\right)_{\text {f.c.c. }}=0.24680-(\ln N) / N, \quad\left(S^{e} / N k_{\mathrm{B}}\right)_{\mathrm{HCP}}=0.24541-(\ln N) / N.
$$

Furthermore, for f.c.c. solids, thermodynamic properties including pressure, Gruneisen $\gamma$ and elastic constants have been calculated with lattice dynamicsfor both the Lennard-Jones 6-12 and the exponential six pair potentials $(^{16})$; the interaction potential is extended to convergence, but the harmonic approximation is made for the forces. The application of this general «lattice dynamics » method to the f.c.c.-b.c.c. polymorphic transformation has been carried out by Hoover et al. $(^{17})$ for inverse power potentials $\varphi(r)=\varepsilon(\sigma / r)^{n}$.

(13) G. JACUCCI and N. QUIRKE: *Free energy calculations for crystals*, in *Computer Simulation in the Physics and Chemistry of Solids*, in *Lect. Notes in Phys*. (Springer Verlag, Berlin, 1982).
(14) A. BEYERLEIN and Z.W. SALSBURG: *J. Chem. Phys.*, 47, 3763 (1967).
(15) W.G. HooVER: *J. Chem. Phys.*, 49, 1981 (1968).
(16) A.C. HOLT, W.G. HOOVER, S.G. GRAY and D.R. SHORTLE: *Physica*, 49, 61 (1970).
(17) W.G. HOOVER, D.A. YOUNG and R. GROVER: *J. Chem. Phys.*, 56, 2207 (1972).

Lattice dynamics can be applied only to stable structures, having real $\nu_j$.
The close-packed f.c.c. structure satisfies the mechanical-stability requirement in the quasi-harmonic approximation for many systems: $n$-$n$ interaction, the inverse-power and the Lennard-Jones potentials and for hard spheres. The b.c.c. crystal is unstable to shear for $n$-$n$, hard spheres, and for the inverse power potential for $n>7$ $(^{17})$. We have verified that it is also unstable for the Lennard-Jones (12-6) potential summed to convergence, in the quasi-harmonic approximation presently discussed.

The result of the inverse-power potential investigation has been that, for $n<7$, the system undergoes a polymorphic transformation from the close-packed structure at low temperature to the body-centered structure before melting $(^{17})$. It has been concluded that the looser packing of the body-centered arrangement induces more low-frequency shear modes. Their effect can be seen in the larger values of the excess entropy:

$$
\Delta S / N k_{\mathrm{B}}=1 /(N-1) \sum_{j=1}^{3 N-3} \ln \left(\nu_{\mathrm{E}} / \nu_{j}\right)
$$

and of the mean square displacement relative to the Einstein model: $\langle r^2 \rangle / \langle r_{\mathrm{E}}^2 \rangle =$
$=1/(3N-3)\sum_{j=1}^{3N-3}(\nu_{\mathrm{E}}/\nu_j)^2$. Taking into account the different Helmholtz free energy of the Einstein model for the two structures, the polymorphic trans-
ition can be located in thermodynamic space. The interest of this investigation partly resides in the fact that some metallic crystals show this type of poly-
morphic transformation and that the repulsive interaction in these systems is certainly much softer than that in the (12-6) LJ.

Analysis of experimental data, for example on alkali halides $(^{18})$ and on argon $(^{19})$ crystals, has shown, however, that the anharmonic contributions to the free energy of the lattice cannot be neglected. More frequently these days the study of disorder and of anharmonicity in condensed systems is made by using computational rather than analytical tools. For the f.c.c. Lennard-
Jones solid, for example, the comparison of lattice dynamics approximations with Monte Carlo calculations $(^{16})$ has clearly demonstrated the contribution to thermodynamic properties of terms in the energy beyond quadratic in the particle displacements. Methods described in sect. 2, in particular, have been used in a «direct Monte Carlo calculation of anharmonic free energies» by PoLLock $(^{20})$; this is an application of the one-sided method of eq. (1) above; the system studied is a periodically repeating LJ, nearest-neighbor, f.c.c. crystal containing 32 particles. The values of the free energy obtained by this method

(18) M.P. Tosı and F. Fumi: Phys. Rev., 131, 1485 (1963).
(19) J. Kuebler and M. Tosı: Phys. Rev. A, 137, 1617 (1965).
(20) E.L. Pollock: J. Phys. C, 9, 1129 (1976).

are in better argeement with experimental rare-gas crystal data than the pre- vious estimates from conventional anharmonic theory. We note in passing that from fig. 1 of Pollock $(^{20})$ we read $\Delta F / N k T=0.12$ at $T=0.5$ and $\varrho=1.0$ . From our figure 1 we can see that two-sided overlap evaluation of $\Delta F / N k T$ gives $0.143 \pm 0.002$ .

More recently, KRATKY $(^{21})$ has investigated the relative stability of f.c.c. and HCP hard-sphere crystals using a method for the direct evaluation of the partition function by an importance sampling technique and taking ac- count of the special features of the hard-sphere potential. He finds the f.e.e. structures favored by an entropy difference of $0.02 k_{B}$ .

To our knowledge no machine calculations exist for the free-energy dif- ference between various polymorphs of a crystal with continuous pair inter- action.

b) Possible thermodynamic paths in multistage of the f.c.c.-b.c.c. transfor- mation. A simple geometrical transformation relates the f.c.c. and b.c.c. lat- tices. By using the cubic directions in a b.c.e. lattice for reference, a defor- mation which stretches one cubic direction by a factor $2^{\frac{2}{3}}$ and contracts the other two, each by a factor $2^{-\frac{1}{3}}$ , produces a body-centered tetragonal lattice where the body center is at the center of a square of side $2^{\frac{1}{3}}$ . It is easy to see that the resulting structure is f.c.c. and that the density is unchanged in this transformation. This rather special feature of the transformation will be used in devising various paths for the multistage sampling method.

The methodology described in sect. 2 requires the use of two Hamiltonians defined in the same configuration space. In the f.c.c.-b.c.e. transformation we shall choose two identical Hamiltonians which contain the same number of particles interacting with the same pair potential; but the two configurations upon which the Hamiltonians act will be related by a one-to-one correspondence via the space transformation mentioned above. In other words we wish to evaluate $\Delta F$ between two regions in configuration space using the same Hamil tonian. The geometric deformation is used to relate the configurations in the two regions in a one-to-one correspondence. An alternative, but operationally equivalent description would be to interpret the calculation as one for two different Hamiltonians $H_{1}, H_{2}$ having the same configuration space; for example, with the usual b.c.c. structure the pair interaction will be $\varphi(r^{2} \equiv x^{2}+$  $+y^{2}+z^{2})$ for $H_{1}$ , and for $H_{2}$ it will be anisotropic and given by $\varphi(s)$ with $s^{2}=2^{-\frac{1}{3}}(x^{2}+y^{2})+2^{\frac{2}{3}} z^{2} .$

The free energy $F_{0}$ of a subdomain of volume $\Omega_{0}$ of configuration space is determined by the configurational integral $Q_{0}$ , the integration being restricted to $\Omega_{0}$ . If the domain $\Omega_{0}$ corresponds to a well-defined pocket of the potential energy surface V and is well separated from other such pockets by a ridge of

(21) K.W. KRATKY: Chem. Phys., 57, 167 (1981).

high values of $V$, then $\Omega_{\mathrm{c}}$ is a metastable region. Trajectories given by the solution of the equations of motion will be trapped in the pocket for a long time. While the value of $F$ pertaining to the unrestricted domain $\Omega$ is the relevant quantity in the thermodynamic limit and will be dominated by the truly stable configurations, the values of $F_{0}$ obtained from different regions of metastability will describe the relative stability of such metastable regions. The escape time from the metastable regions will depend on certain properties of $V$: the height of the ridges, the existence of low-lying saddle points along paths joining neighboring metastable regions, and of course of the temper- ature.

In the case of a LJ crystal a low-energy barrier path is available $(^{7})$ for a b.c.c. to f.c.c. transformation to take place. A way of constraining the system to remain in the b.c.c. structure is to use fixed periodic boundary conditions to inhibit the model crystallite from taking the path of the transformation irrespective of the existence of a potential-energy barrier. Similarly, imposing the value of the ratio between the sides of the rectangular parallelepiped through (periodic) boundary conditions is a way of constraining the system in order to construct intermediate ensembles for multistage sampling. The values of the constrained free energy $F_{\xi}$ for different values of the « reaction co-ordinate » $\xi$ locating the position of the system along the transformation path will show whether a barrier exists and will yield an estimate of its numerical value. These matters will be discussed further in sect. 7.

Let us describe three possible « routings » for the multistage sampling:

i) A simple linear combination of the two Hamiltonians, namely $H(\lambda)=\lambda H_{1}+(1-\lambda) H_{2}$; varying $\lambda$ gradually switches on one Hamiltonian and switches off the other.

ii) Whenever the harmonic model $H_{\mathrm{h}}$ in both structures is stable, a good choice is to evaluate $F$ (f.c.c.)-$F_{\mathrm{h}}$(f.c.c.) and $F$ (b.c.c.)-$F_{\mathrm{h}}$(b.c.c.) separately. The advantage is that anharmonicity usually gives a relatively small correc- tion; hence the harmonic Hamiltonian $H_{\mathrm{h}}$ may be expected to retain much of the many-body correlation effects. As a consequence the overlap of energy distributions can be expected to be larger than with other routings.

iii) Whenever a « physical » path exists between the two structures as, for example, the one found by PARRINELLO and RAHMAN $(^{8 a})$ in KCl which goes from rock-salt to the «CsCl » polymorph, it can be employed in the way alluded to above.

In the present work method i) has been mainly used. We anticipated that iii) will be discussed in more detail in sect. 7.

c) About sampling algorithms. The distributions $h(\Delta)$ introduced in sect. 2 can be evaluated by using various algorithms to sample configuration

space. In principle, $h(\Delta)$ is defined in the canonical ensemble. Not all algorithms apply to the canonical ensemble: the usual MD, for instance, samples the micro- canonical ensemble. It can be argued, however, that the different distributions of say the fluctuations of the potential energy per particle in the two ensembles will not reflect itself in the distribution $h(\Delta)$ of $\Delta$. We have investigated this point looking for differences in the estimation of $h(\Delta)$ in the two ensembles without finding any within statistical error. In the following we shall present data obtained in the canonical as well as microcanonical ensembles. No dif- ference is found in the evaluation of $F_{f.c.c. }-F_{b.c.c. }$ .

A canonical version of MD is, of course, presently available $(^{22})$ . In paper I we have compared the efficiency of MC and two MD algorithms for configuration space sampling and for gathering quantitative information on $h(\Delta)$ in par ticular. While this efficiency was found to be not too different for the two al- gorithms, one particular feature stood out in favor of MD and MDM (by using the terminology in I) in particular, namely the variance of the mean of the potential energy in MDM runs for crystals was shown to be much smaller than in MDM or MC. This was interpreted to be a consequence of the oscillatory behavior of the energy fluctuations of the system in the microcanonical en- semble. It was shown further that MDC calculations can be treated in a way as to correct for the uncertainty in the reading of the mean potential energy associated with the slow random fluctuations of the internal energy of the system resulting from the time integral of the heat flux to and from the tem- perature bath.

In view of the role played by the internal energy in determining entropies from free-energy estimates and given the fact that the magnitude of the ex- pected error of potential-energy averages in standard MC or MD simulations is quite substantial and will be found to be one order of magnitude larger thanthat of free-energy differences, it is essential to make the optimal choice (MDM) for the algorithm to be used in the estimation of potential-energy averages.

The insight presented in paper I is largely a result of the present study rather than pre-existing wisdom; hence the choice of algorithms we have made for this work is not necessarily one we would repeat. However, although the data have been gathered with various algorithms, later larger $N$ runs were MD calculations.

## 4. - Model systems and procedures.
We have used the methods of sect. 2 and 3 to investigate the Lennard- Jones 6-12 potential and also the pair potentials suitable for rubidium and cesium metals. The alkali metal effective pair interactions were constructed
(22) H.C. ANDERSEN: J. Chem. Phys., 72, 2384 (1980).

by PRICE et al. $(^{23})$ using the theory of electron screening of the bare ion-ion Coulomb potential.

We note that there are other effective pair interactions available in the literature. The DRT (Dagens, Rasolt, Taylor $(^{24})$ ) potential using the Geldart- Taylor $(^{25})$ dielectric function has been used successfully for studying a variety of properties $(^{26})$.

Eventually, for $\Delta F$ calculations of the kind reported here, it would be very satisfactory to compare the results based on different assumptions in the theory of metals. Our present work was based on effective alkali pair potentials of Price et al. $(^{23})$ which have already been used in the investigation of homogeneous liquid-to-solid nucleation $(^{6})$, on the one hand, and of poly morphic structural transformations $(^{7})$, on the other.

At this point we digress somewhat towards the thermodynamics of density, volume and free-energy changes in the vicinity of equilibrium conditions. The motivation of this digression is easily seen in the fact that the pseudo- potential approach to the cohesion in metals, up to second order in the per- turbation caused by the pseudopotential, gives the energy $V$ of the metal system as

$$
V=V_{1}(\Omega)=\sum_{l}^{N} \sum_{j>l}^{N} V_{\mathrm{EPP}}\left(\left|\boldsymbol{r}_{l}-\boldsymbol{r}_{j}\right| ; \Omega\right),
$$

$N$ being the number of ions in volume $\Omega$. EPP stands for effective pair potential. The ionic positions are at $\boldsymbol{r}_{l}, l=1, \ldots, N$. Note that $V_{\mathrm{EPP}}$ depends on $\Omega$ as well as on the interparticle distance $\left|\boldsymbol{r}_{l j}\right|$. The least satisfactory part of the theory of $V$ given above is $V_{1}(\Omega)$. Hence, in a polymorphic transition between two structures, if there is a density change, then the potential difference has to be evaluated by using the change in $V_{1}(\Omega)$.

To deal with this problem one can take advantage of the common practice in the calculations of defect properties which is to work at constant volume $(^{26})$. The desired constant-pressure transformation characteristics are then deduced with the use of the thermodynamic-equilibrium condition.

It is easily shown $(^{26,27})$ that the Gibbs free-energy difference for variations at constant pressure are equal to the Helmholtz free-energy differences at constant volume. Similarly volume changes $\Delta \Omega$ occurring when a polymorphic transition takes place at constant pressure are related to $\Delta p$ when they occur

$(^{23})$ D.L. PRICE: Phys. Rev. A, 4, 358 (1971); D.L. PRICE, K.S. SINGWI and M.P. Tosi: Phys. Rev. B, 2, 2983 (1970).
$(^{24})$ M. RASOLT and R. TAYLOR: Phys. Rev. B, 11, 2717 (1975); L. DAGENS, M. RASOLT and R. TAYLOR: Phys. Rev. B, 11, 2726 (1975).
$(^{25})$ D.J.W. GELDART and R. TAYLOR: Can. J. Phys., 48, 169 (1970).
$(^{26})$ G. JACUCCI and R. TAYLOR: J. Phys. F, 9, 1489 (1979) and references therein.
$(^{27})$ C.P. FLYNN: Point Defects and Diffusion (Clarendon, Oxford, 1972).

at constant volume. The above-mentioned relations are derived from first-
order truncations of suitable Taylor expansions and hence are valid to first
order in relative changes like $\Delta\Omega/\Omega$ etc.

Let us derive the $\Delta\Omega$, $\Delta p$ relation with the f.c.c.-b.c.c. transformation in
mind. $\Delta\Omega=\Omega_{\mathrm{F}}-\Omega_{\mathrm{B}}$ and $\Delta p=p_{\mathrm{F}}-p_{\mathrm{B}}$ are changes in volume and pressure
accompanying the f.c.c.-b.c.c. transformation at constant $p$ and $\Omega$, respectively.
If we set up the system F (i.e. f.c.c.) in such a way that on transformation
to B (i.e. b.c.c.) the latter attains the same state point $p_{\mathrm{B}},\Omega_{\mathrm{B}}$ in both constant-
volume and constant-pressure transformations, F would have started at $p_{\mathrm{F}},\Omega_{\mathrm{B}}$
in one case and $p_{\mathrm{B}},\Omega_{\mathrm{F}}$ in the other. Thus, for F, the volume change $\Delta\Omega=$
$=\Omega_{\mathrm{F}}-\Omega_{\mathrm{B}}$ is attained by a pressure change $-\Delta p=p_{\mathrm{B}}-p_{\mathrm{F}}$. Hence $\Delta\Omega=$
$=\Omega\chi_{T}^{\mathrm{F}}\Delta p$ where $\chi_{T}^{\mathrm{F}}$ is the compressibility of F, by using a symmetric argument
$\Delta\Omega=\Omega\chi_{T}^{\mathrm{B}}\Delta p$, all to first order in small quantities. Neglecting $(\chi_{T}^{\mathrm{F}}-\chi_{T}^{\mathrm{B}})/\chi_{T}$,
we write $\Delta\Omega=\Omega\chi_{T}\Delta p$. Since the compressibility cannot be evaluated without
knowning $V_{1}(\Omega)$, we shall use the experimental values for the alkali metal in
question. All the above transformations are at constant temperature $T$.

In the case of volume-independent interaction, LJ systems for instance,
constant-pressure calculations can now be made without special difficulty $(^{7})$.
In the calculations reported in this paper, however, the LJ system has been
treated in the same way as the alkalis, namely at constant volume.

We note here, as a small digression, that, at constant volume $\Omega$, calculations
for an alkali require but one table of values of $V_{\mathrm{EPP}}(r;\Omega)$ as a function of $r$;
at constant pressure, however, one needs several such tables to cover the range
of $\Omega$ values that the system fluctuates through at the ambient pressure and
temperature, in addition to the functions $V_{1}(\Omega)$. Such a numerical scheme is
actually being used for constant-pressure quench studies of crystal nucleation
from the melt $(^{28})$.

The next item to mention in this section of procedures is that of the trun-
cation of the potential. The usual procedure is to truncate the potential and
to introduce corrections for the error thus committed. The larger the system
and the longer the cut-off, lesser is the error. However, a central feature of
the $\Delta F$ calculational methods is the width of the energy distributions and va-
rious overlaps between such distributions. The larger the system, the narrower
are the distributions and greater is the difficulty of obtaining practically reas-
onable overlapping histograms. Thus a compromise has to be made to allow
for a balance between conflicting requirements.

Liquid-state calculations are not encumbered by this question of balance.
Firstly, the pair correlations approach their asumptotic value of unity at
rather short distances allowing accurate evaluation of the interactions beyond
the cut-off; secondly, the entropy per particle of the liquid-state system has been
found to be insensitive to system size; in fact, 32-particle systems yielded the

(28) Y. LIMOGE and A. RAHMAN: private communication.

same free energies as 108-particle systems after correcting for cut-off effects; this was found to be so for monatonic LJ systems (¹⁰) as well as for diatomic systems (²⁹), a molecule being two LJ centers rigidly fused together.

In the work being reported here, on LJ and alkali crystal systems, we have found that below a certain size the usual procedure to correct for neighbors beyond the cut-off led to poor results; extensive calculations with 54- and 128-particle systems brought us to this conclusion. However, for 144 and 320 particle systems (the latter requiring heavy multistage calculation) we obtained systematically consistent results. Our conclusion is that for the reliability of free-energy difference data a rule of thumb is $N \geqslant 144$. We consistently chose a cut-off such that for the f.c.c. and b.c.c. structure the number of interacting neighbors came as close as possible. This number was 54 for f.c.c., 58 for b.c.c. in a 144-particle system and 140, 136, respectively, for the 320 system. Note specially (in fig. 1 of (⁶ᵃ)) that the alkali metal potential we are using can, in practice, be truncated in the usual way because of the rapid decrease in the amplitude of Friedel oscillations.

Some of the results for the 128-particle system will also be discussed below to display the small difference with the results for a 144-particle system.

As is commonly done in setting up dynamical matrices for small unit cell crystal vibrations, one can use a small-sized system and the neighbors in the adjoining cells to take all particles into account which fall within the cut-off radius around a given particle; this may be a way of dealing with the conflicting requirements of the long cut-off and broad energy distributions. This is still to be systematically tested. Our observation that the entropy per particle is not insensitive to the cut-off for $N < 144$ leads us to doubt the possibility of getting accurate results from systems much smaller than this.

In concluding this section on procedures we shall state a variety of details which need to be put down. Let $\varepsilon$ and $\sigma$ denote units of energy and length. For LJ systems these parameters appear in their usual way in the analytical form of the potential. For alkali metals we have chosen for all our calculation $\varepsilon = 555.86 \cdot 10^{-16}$ erg and $\sigma = 4.4048 \mathring{A}$; all quantities will be expressed in their dimensionless reduced form by using the above $\varepsilon$, $\sigma$, besides $k_{\text{B}}$. Extensive quantitites will be given per particle, throughout.

As for the state parameters, we studied the LJ system most thoroughly at number density $\varrho = 1.0054$ and temperature $T = 0.500$, *i.e.* some $\frac{2}{3}$ of the way to the triple point. We also studied this system at $\varrho = 0.8378$, $T = 0.500$ and at $\varrho = 1.0054$, $T = 1.02$.

Two alkali metals, Rb, Cs were studied at STP and under pressure at room temperature. Rb was also investigated at $\varrho = 1.564$ and at low $T$, namely 0.1.

These data made it possible to assess the variation of $\Delta F$ with $\varrho$ and $T$ for these model systems.

(²⁹) N. Quirke and G. Jacucci: *Mol. Phys.*, **45**, 823 (1982).

## 5. - Results for the Lennard-Jones potential.

a) Evaluation of $\Delta F$ and $\Delta S$. In this subsection we present numerical estimates for $\Delta F$ between b.c.c.-f.c.c. structures of the Lennard-Jones crystal. All data refer to the thermodynamic state defined by $T=0.500$ and $\varrho=1.0054$ (in the usual LJ units).

The procedure used was the multistage overlapping distribution method applied to the linear combination Hamiltonian $H(\lambda)=\lambda H_{\mathrm{B}}+(1-\lambda) H_{\mathrm{F}}$ described in sect. 3.

A 320-particle system interacting up to a distance $R_{\mathrm{c}}=3.20$ was studied by using MDC and 11 intermediate stages for evaluating $\Delta F$. After equilibration each ensemble was sampled by using a 2000 step run. The results are given in table I, together with analogous results corresponding to a cut-off distance $R_{\mathrm{c}}^{\prime}=2.35$.

As seen from the last line in table I, the result for $F_{\mathrm{F}}-F_{\mathrm{B}}$ was $-0.1757 \pm$ $\pm 0.0015$ and $-0.1044 \pm 0.0011$ for the cut-off distances $R_{\mathrm{c}}$ and $R_{\mathrm{c}}^{\prime}$, respectively. We can check whether this discrepancy can be accounted for by the difference in cut-off by making use of the values of the potential energy at $T=0$; by using a superscript to denote zero temperature, $V_{\mathrm{F}}^{0}-V_{\mathrm{B}}^{0}$ is found to be $-8.1629+$ $+7.8810=-0.2819$ and $-7.7793+7.5680=-0.2113$ for $R_{\mathrm{c}}$ and $R_{\mathrm{c}}^{\prime}$, respectively. Thus $-0.2819+0.2113=-0.0706$ satisfactorily accounts for the discrepancy $-0.1757+0.1044=-0.0713$ in $\Delta F$ values. This suggests that the change in cut-off does not affect the calculated value of $\Delta S$.

In fact, the potential-energy difference $V_{\mathrm{F}}-V_{\mathrm{B}}$ at temperature $T=0.500$

<table>
<caption>TABLE I. - Values of $\Delta F=F_{\text{f.c.c.}}-F_{\text{b.c.c.}}$. $U_{\lambda}$ is $\lambda U_{\text{f.c.c.}}+(1-\lambda)U_{\text{b.c.c.}}$. The system is an LJ comprising 320 particles. $R_{\mathrm{c}}$ is the potential cut-off distance.</caption>
<thead>
<tr>
<th colspan="2">$\lambda$</th>
<th colspan="2">$R_{\mathrm{c}}=2.35$</th>
<th colspan="2">$R_{\mathrm{c}}=3.20$</th>
</tr>
<tr>
<th colspan="2"></th>
<th>eq. (2)</th>
<th>eq. (5)</th>
<th>eq. (2)</th>
<th>eq. (5)</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2">b.c.c.</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>0</td>
<td>0.03</td>
<td>0.0177 $\pm$ 0.0010</td>
<td>0.0176 $\pm$ 0.0003</td>
<td>0.0165 $\pm$ 0.0015</td>
<td>0.0165 $\pm$ 0.0005</td>
</tr>
<tr>
<td>0.03</td>
<td>0.07</td>
<td>0.0160 $\pm$ 0.0011</td>
<td>0.0160 $\pm$ 0.0003</td>
<td>0.0140 $\pm$ 0.0012</td>
<td>0.0140 $\pm$ 0.0004</td>
</tr>
<tr>
<td>0.07</td>
<td>0.125</td>
<td>0.0132 $\pm$ 0.0009</td>
<td>0.0135 $\pm$ 0.0003</td>
<td>0.0095 $\pm$ 0.0010</td>
<td>0.0096 $\pm$ 0.0004</td>
</tr>
<tr>
<td>0.125</td>
<td>0.1875</td>
<td>0.0085 $\pm$ 0.0008</td>
<td>0.0084 $\pm$ 0.0003</td>
<td>0.0037 $\pm$ 0.0010</td>
<td>0.0035 $\pm$ 0.0003</td>
</tr>
<tr>
<td>0.1875</td>
<td>0.25</td>
<td>0.0025 $\pm$ 0.0015</td>
<td>0.0032 $\pm$ 0.0002</td>
<td>0.0018 $\pm$ 0.0008</td>
<td>--0.0022 $\pm$ 0.0003</td>
</tr>
<tr>
<td>0.25</td>
<td>0.375</td>
<td>--0.0044 $\pm$ 0.0009</td>
<td>--0.0043 $\pm$ 0.0004</td>
<td>--0.0144 $\pm$ 0.0015</td>
<td>--0.0156 $\pm$ 0.0006</td>
</tr>
<tr>
<td>0.376</td>
<td>0.5</td>
<td>--0.0142 $\pm$ 0.0013</td>
<td>--0.0146 $\pm$ 0.0004</td>
<td>--0.0233 $\pm$ 0.0015</td>
<td>--0.0242 $\pm$ 0.0005</td>
</tr>
<tr>
<td>0.5</td>
<td>0.625</td>
<td>--0.0238 $\pm$ 0.0006</td>
<td>--0.0237 $\pm$ 0.0003</td>
<td>--0.0317 $\pm$ 0.0009</td>
<td>--0.0323 $\pm$ 0.0005</td>
</tr>
<tr>
<td>0.625</td>
<td>0.75</td>
<td>--0.0311 $\pm$ 0.0012</td>
<td>--0.0311 $\pm$ 0.0003</td>
<td>--0.0386 $\pm$ 0.0015</td>
<td>--0.0399 $\pm$ 0.0004</td>
</tr>
<tr>
<td>0.75</td>
<td>0.875</td>
<td>--0.0392 $\pm$ 0.0010</td>
<td>--0.0393 $\pm$ 0.0004</td>
<td>--0.0486 $\pm$ 0.0006</td>
<td>--0.0476 $\pm$ 0.0005</td>
</tr>
<tr>
<td>0.875</td>
<td>1.0</td>
<td>--0.0503 $\pm$ 0.0011</td>
<td>--0.0501 $\pm$ 0.0004</td>
<td>--0.0575 $\pm$ 0.0007</td>
<td>--0.0575 $\pm$ 0.0006</td>
</tr>
<tr>
<td colspan="2">f.c.c.</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td colspan="2">$\Delta F$:</td>
<td>--0.1051 $\pm$ 0.0035</td>
<td>--0.1044 $\pm$ 0.0011</td>
<td>--0.1704 $\pm$ 0.0041</td>
<td>--0.1757 $\pm$ 0.0015</td>
</tr>
</tbody>
</table>

is found to be $-0.2429 \pm 0.0036$ and $-0.1703 \pm 0.0032$ for $R_{\mathrm{c}}$ and $R_{\mathrm{c}}^{\prime}$, respectively, and the difference between these is $-0.0726 \pm 0.0048$.

It is thus apparent that the calculated $\Delta F$ can be corrected for the finite cut-off by making appropriate lattice sums from the cut-off to infinity and also that the entropy difference $S_{\mathrm{F}}-S_{\mathrm{B}}=-0.1344 \pm 0.0078$ (for $R_{\mathrm{c}}$) and $-0.1318 \pm$ $\pm 0.0068$ (for $R_{\mathrm{c}}^{\prime}$) should be in satisfactory agreement with each other.

In addition to the 320-particle system, a 144-particle system also has been studied but by MC using the cut-off $R_{\mathrm{c}}^{\prime}=2.35$ and 5 stages. Several runs of 5000 macrosteps have been carried out, thus obtaining the following results, uncorrected for contributions beyond cut-off: $\Delta F=-0.0940 \pm 0.0036$ and $\Delta V=-0.1640 \pm 0.0060$, yielding $\Delta S=-0.140 \pm 0.014$, again in satisfactory agreement with the corresponding MDC results with the same cut-off $R_{\mathrm{c}}^{\prime}$.

In summary, the entropy difference is found to be insensitive to the cut-off and to the number of particles in the system for the reported values of $R_{\mathrm{c}}$ and $N$. The best estimate is obtained by averaging the above MDC results:
$S_{\mathrm{F}}-S_{\mathrm{B}}=-0.1331 \pm 0.0049$.

The free-energy difference, corrected for the long-range contribution in the way anticipated above, is $F_{\mathrm{F}}-F_{\mathrm{B}}=-0.1566 \pm 0.0015$ and $-0.1559 \pm$ $\pm 0.0011$ from calculations employing $R_{\mathrm{c}}$ and $R_{\mathrm{c}}^{\prime}$, respectively.

b) $\Delta F$ at neighboring state points. The value of $\Delta F \equiv F_{\mathrm{F}}-F_{\mathrm{B}}$ decides the relative stability of the two structures. Additional information as well as a check of the thermodynamic consistency of the results can be obtained by evaluations of $\Delta F$ at different state points. We have carried out investigations along these lines with a 128-particle system. The size of this system (and the cut-off used) has turned out to be somewhat smaller than needed to provided values of $\Delta S$ independent of $N$ and $R_{\mathrm{c}}$, within statistical error. The results to be discussed below, although internally consistent, deserve, therefore, a word of caution, if extrapolated to predict the behavior of infinite systems.

i) The derivative of $\Delta F$ with respect to the volume $\Omega$ is related to the pressure change $\Delta p$ observed in a structural transformation at constant $\Omega$. To first order in small quantities, this $\Delta p$ in turn is related to the volume change $\Delta \Omega$ the system would undergo if the transformation happens at constant pressure $p$. Now $p=-(\partial F / \partial \Omega)_{T}$ gives $\Delta p=-(\partial \Delta F / \partial \Omega)_{T}$ and, as already shown, $\Delta \Omega=\Omega \chi_{T} \Delta p$. We hence get the following value for the volume change connected with the transformation at $T=0.5$, by measuring the pressure (using the virial theorem), and hence $\Delta p$:

$$
\Delta \Omega / \Omega=\left(\Omega_{\mathrm{F}}-\Omega_{\mathrm{B}}\right) / \Omega=(-0.43 \pm 0.08) \%,
$$

i.e. the relative volume change is smaller than one percent and is negative.

ii) Taking into account the eventual curvature $c$ of $\Delta F$ as a function of $T$, one can expect the following relation to hold between quantities relative

25 - Il Nuovo Cimento D.

to temperatures $T_{1}$ and $T_{2}$:

$$\Delta F_{2}=\Delta F_{1}-\Delta S_{1}(T_{2}-T_{1})+c(T_{2}-T_{1})^{2},$$

$$\Delta F_{1}=\Delta F_{2}-\Delta S_{2}(T_{1}-T_{2})+c(T_{1}-T_{2})^{2},$$

i.e.

$$(8)\qquad \Delta F_{2}=\Delta F_{1}-\frac{1}{2}(\Delta S_{1}+\Delta S_{2})(T_{2}-T_{1}).$$

To check whether the calculated values of $\Delta F$ obey eq. (8), runs were carried out at $T_{1}=0.50$ and $T_{2}=0.85$, at a density $\varrho=1.00$. The value of $\Delta F_{2}=$ $=-0.030 \pm 0.006$ is in good accord with the right-hand side of eq. (8), which is found to be $-0.027$.

In summary, this additional investigation has provided a check that $\Delta F$ increases with increasing temperature, in accord with the negative sign, and the value, of $\Delta S$; and it also increases with increasing volume, in accord with the negative sign, and the value, of $\Delta \Omega$.

It would have been more satisfactory to obtain data on the variation of $\Delta F$ with $\Omega$ and $T$ by using the large system. This was not done in view of the heavy computation that would have been required. However, we believe that the thermodynamic consistency of the results has been satisfactorily demonstrated.

The signs of $\Delta S$ and $\Delta \Omega$ show that the relative stability of the f.c.c. structure (i.e. the value of $(\Delta G) p$) increases upon increasing the pressure, but decreases upon increasing the temperature. However, a linear extrapolation from $T=0.5$, where $\Delta F=-0.156 \pm 0.001$ and $\Delta S=-0.133 \pm 0.005$, by using $\partial \Delta F / \partial T=-\Delta S$, shows that there will be no f.c.c. $\to$ b.c.c. transition in this system before melting the crystal at normal pressure.

The location of the f.c.c. $\leftrightarrow$ b.c.c. transition line in the $p$-$T$ diagram can be derived approximately from the values of $\Delta S$ and $\Delta \Omega$ by expanding $(^{26,27})$

$$(\Delta G(p, T))_{p} \equiv G_{\mathrm{F}}(p, T)-G_{\mathrm{B}}(p, T) \simeq(\Delta F(p, T))_{V}$$

about $(p_{0}, T_{0})$ to first order in $\delta p=p-p_{0}$ and $\delta T=T-T_{0}$:

$$(\Delta G(p, T))_{p}=\left(\Delta G\left(p_{0}, T_{0}\right)\right)_{p}-(\Delta S)_{p} \delta T+(\Delta \Omega)_{p} \delta p.$$

Approximating $(\Delta S)_{p} \simeq(\Delta S)_{V}+(\alpha / \chi_{T})(\Delta \Omega)_{p}$, where $\alpha$ is the coefficient of thermal expansion and $\alpha / \chi_{T} \sim 9$ for argon $(^{30})$, we get

$$(\Delta G(p, T))_{p}=\Delta F-1.3 \Delta S \delta T+\Delta \Omega \delta p,$$

$(^{30})$ Argon, Helium and the Rare Gas, edited by G. A. Cook (Interscience, New York, N.Y., 1961).

in terms of our quantitites $\Delta F$, $\Delta S$ and $\Delta \Omega$ estimated at $(p_0, T_0)$. The polymorphic transition line is identified by $(\Delta G(\tilde{p}, \tilde{T}))_p = 0$:

$$
\tilde{T}-T_{0}=\frac{\Delta F}{1.3 \Delta S}+\frac{\Delta \Omega}{1.3 \Delta S}\left(\tilde{p}-p_{0}\right).
$$

Inserting numerical values in this relation we estimate that the f.c.c.-b.c.c. transition line should cross the experimental melting line of argon under pressure $(^{30})$ at about 230 K and 0.8 GPa, the stable b.c.c. phase region being located above this point towards higher pressures and temperatures. As a consequence, we expect that at pressures of ten to hundred (in reduced units $\varepsilon/\sigma^3$) and up there should exist a temperature region where the Lennard-Jones solid prefers to take up the BCC structure.

## 6. - Results for alkali metals.

a) *Rubidium at STP.* The model system consisted of 144 particles interacting with the pair potential described in sect. 4. With a cut-off $R_c = 2.435$ each particle has $\sim 54$ neighbors in the f.c.c. structure and $\sim 58$ in the b.c.c. one, *i.e.* it includes the first six shells in both structures, as in the MC calculation performed with 144 LJ particles. Two independently equilibrated MC runs 5000 macrosteps long have been carried out at $\varrho = 0.92237$ and $T = 0.728$, corresponding to standard temperature and pressure (STP), thus obtaining the following results:

$$
\left.
\begin{array}{ll}
F_{\mathrm{F}}-F_{\mathrm{B}} &
\begin{array}{l}
\text{1)} \quad 0.1050 \pm 0.0028 \\
\text{2)} \quad 0.1076 \pm 0.0025
\end{array}
\end{array}
\right\} = 0.1063 \pm 0.0019,
$$

$$
\left.
\begin{array}{ll}
V_{\mathrm{F}}-V_{\mathrm{B}} &
\begin{array}{l}
\text{1)} \ -4.552 + 4.639 = 0.087 \ \pm 0.016 \\
\text{2)} \ -4.553 + 4.662 = 0.109 \ \pm 0.015
\end{array}
\end{array}
\right\} = 0.098 \ \pm 0.011,
$$

$$
T(S_{\mathrm{F}}-S_{\mathrm{B}}) = 0.008 \ \pm 0.011.
$$

The values of the correlation length were about 50 macrosteps for the Fermi function and 100 for $V$. The multistage calculations consisted of 5 ensembles, corresponding to $\lambda \equiv (0.0, 0.25, 0.50, 0.75, 1.0)$. The free-energy difference $\Delta F$ is very precisely determined and it is positive as expected. The potential-energy difference $\Delta V$ coincides with this value within statistical error, indicating that the entropy difference $\Delta S$ for the two lattices is very small: $\Delta V$ is only about $2\%$ of the energy per particle.

b) $\Delta \Omega$ and thermodynamic checks for Rb. Two analogous MC runs were carried out at $T = 0.728$ and $\varrho = 1.564$. The density dependence of the ef-

fective pair interaction in alkali metals mentioned in sect. 4 makes it imperative to use the potential relevant to this higher density. The results of the MC runs are

$$
F_{\mathrm{F}}-F_{\mathrm{B}} \left. \begin{array}{ll}
\text { 1) } & 0.1861 \pm 0.0028 \\
\text { 2) } & 0.1918 \pm 0.0025
\end{array} \right\} = 0.1890 \pm 0.0019,
$$

$$
V_{\mathrm{F}}-V_{\mathrm{B}} \left. \begin{array}{l}
\text { 1) } 3.3779-3.1570=0.2209 \pm 0.0058 \\
\text { 2) } 3.3599-3.1523=0.2076 \pm 0.0141
\end{array} \right\} = 0.2143 \pm 0.0076,
$$

$$
T(S_{\mathrm{F}}-S_{\mathrm{B}}) = 0.0253 \pm 0.0078.
$$

Number of particle, cut-off and length of the MC runs were as mentioned above. Values of the correlation lengths were very similar. The result shows that increasing the density favors still more the b.c.c. structure in terms of both potential and free energy, although now we have $S_{\mathrm{F}}>S_{\mathrm{B}}$ rather unexpectedly.

This result can be combined with the previous one to estimate the value of the volume change connected with the transformation. From the observations made above we can already predict that $\Omega_{\mathrm{F}}-\Omega_{\mathrm{B}}$ will be positive. We shall make use of the atomic volume $\Omega$ at melting $92.60 \cdot 10^{-24} \mathrm{~cm}^{3}$ and we shall approximate the isothermal bulk modulus $B_{T}$ by the value of the adiabatic one $B_{s}=2.14 \cdot 10^{10} \mathrm{dyn} / \mathrm{cm}^{3}$ at a density $\varrho=1.530$, i.e. close to melting. Again we have
$$
\Delta \Omega / \Omega=-\left(B_{\mathrm{T}}\right)^{-1}\left(\frac{\partial \Delta F}{\partial \Omega}\right)_{\mathrm{T}}=(0.56 \pm 0.02) \%.
$$

One other temperature was investigated at $\varrho=1.564$, namely $T=0.100$. Nine ensembles were used in the multistage sampling scheme to get sufficient overlap. The values of $\tau$ were about half of the previous ones. The other con ditions were the same. Here are the results:

$$
F_{\mathrm{F}}-F_{\mathrm{B}} \left. \begin{array}{ll}
\text { 1) } & 0.2020 \pm 0.0006 \\
\text { 2) } & 0.2008 \pm 0.0007
\end{array} \right\} = 0.2014 \pm 0.0005,
$$

$$
V_{\mathrm{F}}-V_{\mathrm{B}} \left. \begin{array}{l}
\text { 1) } 2.3814-2.1803=0.2011 \pm 0.0021 \\
\text { 2) } 2.3836-2.1798=0.2038 \pm 0.0019
\end{array} \right\} = 0.2025 \pm 0.0014,
$$

$$
T(S_{\mathrm{F}}-S_{\mathrm{B}}) = 0.0011 \pm 0.0015.
$$

The entropy difference is again very small. We can perform a thermodynamic check to verify that the value of $T \Delta S$ larger than the statistical error found at $T=0.728$ is indeed meaningful. $T_{1}=0.1, T_{2}=0.728$:
$$
\Delta F_{2}=\Delta F_{1}-\frac{1}{2}\left(\Delta S_{1}+\Delta S_{2}\right)\left(T_{2}-T_{1}\right)=0.1840 \pm 0.0056,
$$

which compares favorably with the value found at $T_{2}: \Delta F_{2}=0.1890 \pm 0.0019$.
The problem of locating the f.c.c.-b.c.c. transition line in the $p$-$T$ diagram has been dealt with in the previous section. In the scheme presented there, which uses linear extrapolation as the central approximation, the value of $\Delta S$ appears in the denominator in determining the value of the transition tem- perature. The small value of $\Delta S$ in rubidium leads us to the conclusion that the transition cannot occur before melting.

c) Comparison Rb-Cs. Using a somewhat smaller system, containing128 particles with an interaction potential cut-off $R_{c}=2.304$ , we have carried out a parallel calculation of $\Delta F$ for Rb and Cs. All runs were MC calculations2000 macrosteps long. Each comprised 5 overlaps, corresponding to $\lambda \equiv(0.0$ ,0.25, 0.50, 0.75, 0.90, 1.00). The results are shown in table II.

TABLE II. - Calculations of $\Delta F$ for Rb and Cs at standard temperature and pressure(STP) and under compression. The asterisks * denote mean values over the three runs. The energy unit $\varepsilon=555.86 \cdot 10^{-16} erg$ is the well depth of the Rb pair potential at STP.

<table>
<thead>
<tr>
<th>Metal</th>
<th>$\varrho$</th>
<th>$(F_{F}-F_{B})/\varepsilon$</th>
<th>$(U_{F}-U_{B})/\varepsilon$</th>
<th>$T(S_{F}-S_{B})/\varepsilon$</th>
</tr>
</thead>
<tbody>
<tr>
<td>Rb</td>
<td>$\varrho_{STP}$</td>
<td>$0.103\pm 0.003$ *</td>
<td>$0.126\pm 0.008$ *</td>
<td>$0.023\pm 0.009$ *</td>
</tr>
<tr>
<td>Cs</td>
<td>$\varrho_{STP}$</td>
<td>$0.101\pm 0.005$</td>
<td>$0.111\pm 0.018$</td>
<td>$0.010\pm 0.019$</td>
</tr>
<tr>
<td>Rb</td>
<td>$1.25×\varrho_{STP}$</td>
<td>$0.158\pm 0.006$</td>
<td>$0.204\pm 0.017$</td>
<td>$0.046\pm 0.108$</td>
</tr>
<tr>
<td>Rb</td>
<td>$1.70×\varrho_{STP}$</td>
<td>$0.216\pm 0.008$</td>
<td>$0.310\pm 0.010$</td>
<td>$0.094\pm 0.013$</td>
</tr>
<tr>
<td>Cs</td>
<td>$1.72×\varrho_{STP}$</td>
<td>$0.212\pm 0.005$</td>
<td>$0.306\pm 0.019$</td>
<td>$0.094\pm 0.020$</td>
</tr>
</tbody>
</table>

The results for Rb are somewhat different from the ones obtained with144 particles and a longer cut-off. The more extensive study performed with the Lennard-Jones system showed that convergence of the entropy difference was only reached with the 144-particle system, where the cut-off used con- sistently included 54 particles, up to the fourth shell of neighbors, in the f.c.c. structure and 58 particles, up to the fifth shell of neighbors, in the b.c.c. one. Accordingly, we shall consider the results obtained with the 128-particle systems precise but inaccurate for the deseription of the given potential model and we report them primarily for pointing out the similarity for the alkalimetals. Nonetheless, it should be noted that the new results for Rb are in semi-quantitative accord with the one given in subsections a) and b). $\Delta F$  and $\Delta V$ are about equal at STP, their value being about 0.1 , indicating stability of the b.c.c. structure dictated by potential energy. $T \Delta S$ is essentially zero at STP, but becomes positive under pressure. On the other hand, compressing the crystal increases $\Delta V$ so much that $\Delta F$ increases as well, indicating a positive value for the volume change $\Delta \Omega$ for the transformation: the valueobtained for $\Delta \Omega / \Omega$ is $(+0.77 \pm 0.06) \%$ for Rb, not too different from the 144particle value, and $+0.74 \pm 0.05$ for Cs, by using a value of $1.63 \cdot 10^{11} dyn / cm^{2}$  for $B_{T}$ of Cs.

The striking feature exhibited by this data is the coincidence of the values of the various energies expressed in the same units for the two metals at STP or under pressure (while the values of the density $\varrho_{\text{STP}}$ differ by $26 \%$). With the potential model used, the properties of the heavier alkali metals, for what concerns the stability of crystal lattices, may be the same. In particular, we see no evidence of the experimentally observed transition to f.c.c. in Cs at high compression.

## 7. - Free-energy barriers.

The method of overlapping distributions for the calculation of free-energy differences relies, in principle, on just one requirement, namely that the po- tential functions to be investigated, $V_{1}, V_{2}$ say, span the same configuration space. $V_{\lambda}=\lambda V_{1}+(1-\lambda) V_{2}$ obviously satisfies this criterion if $V_{1}$ and $V_{2}$ do and, therefore, is a suitable potential function for a multistage determination of $\Delta F$. The weight parameter $\lambda$ has no obvious physical meaning.

There is a clear gain in using $V_{\lambda}$ as written above, i.e. as a linear combina- tion of $V_{1}$ and $V_{2}$. The gain is that, as intermediate stages are introduced, the histogram already calculated can be systematically re-used. Suppose we start with $V_{1}$ and $V_{2}$ and get the histograms for $h_{1}(\Delta)$ and $h_{2}(\Delta)$ finding that there is no overlap. We would then decide to use $V_{\lambda}$ with $\lambda=\frac{1}{2}$. One of the two distributions between $V_{1}, V_{2}$ would be $h_{1}[(1-\lambda) \Delta]$. Obviously the histogram for this $h_{1}$ is obtained from the previous histogram for $h_{1}(\Delta)$ by relabelling the axis with factor $(1-\lambda)$; similarly for the stage $V_{\lambda}, V_{2}$. Hence the gain men- tioned above.

However, in physical terms the function $V_{\lambda}$ has no particular significance. We know from laboratory and from computational experience that crystalline structures do «travel» in their configuration space from one point to another along paths which have a particularly simple description. For such displacive transformations, it would be particularly desirable to be able to calculate the free-energy barrier.

We have developed a method of calculating $\Delta F$ between the end points of such paths with the aim not only of evaluating $\Delta F$ by the method of overlap- ping distributions, but also of evaluating the free-energy barrier that needs to be overcome in a crystalline-structure transformation.

The example we present below is only partially satisfactory from the above point of view. It is simply an application of the methodology to a b.c.c.-f.c.c. transformation in an LJ crystal and not an example of a free-energy barrier along the chosen path because along this path there is no barrier.

Let $l_{1}=l_{2}=l_{3}=a$ denote the cubic-cell edges of a b.c.c. lattice. The tetragonal body-centered lattice with $l_{1}=a \xi, \quad l_{2}=l_{3}=a / \sqrt{\xi}, \quad 1 \leqslant \xi \leqslant 2^{\frac{1}{3}}$ is b.c.c. at $\xi=1$ and f.c.c. at $\xi=2^{\frac{1}{3}}$ for which $l_{1} / l_{2}=2^{\frac{1}{3}}$. The volume per particle is $2 / a^{3}$ irrespective of the value of $\xi$.

From the point of view of the determination of the reaction path and the reaction co-ordinate, a much more complicated case is that of rock-salt $\leftrightarrow$ CsCl structural change for many alkali halides $(^{8 a})$ . We shall not go into details here except to say that perhaps a barrier does exist in this case.

It is clear that the tetragonal structures whose potentials can be symbolized by $V_{\xi}$ span a specific f.c.c. $\leftrightarrow$ b.c.c. path. The multistage overlapping method can obviously be used with $V_{\xi}$ instead of $V_{\lambda}$ except that the "gain" mentioned above for $V_{\lambda}$ is not available while using $V_{\xi}$ , simply because $V_{\xi}-V_{\xi'} \neq(\xi-$ $\xi')(V_{1}-V_{2})$ .

Using a LJ system of 320 particles, we calculated the $\Delta F$ with seven equally spaced intermediate values of $\xi$ with the following results:
$$
T=0.7, \quad \varrho=1.0054 \mathrm{~LJ} \text { system },
$$

$$
F_{\mathrm{F}}-F_{\mathrm{B}}=\Delta F=-0.088 \pm 0.003,
$$

$$
\Delta V=-0.184 \pm 0.007, \quad \Delta S=-0.137 \pm 0.008.
$$

Let us check these results with those of subsect. 5a).

Using the identity $(\partial / \partial \beta) \beta F=V$ , we can construct finite differences arising out of the two temperatures 0.5 and 0.7 . This gives, respectively,
$$
\frac{-0.088 \pm 0.003}{0.7}+\frac{0.104 \pm 0.001}{0.5}
$$
and
$$
\frac{1}{2}(-0.184 \pm 0.007-0.170 \pm 0.003) \cdot(1 / 0.7-1 / 0.5),
$$
i.e. 0.082 and 0.101 with an expected error of about 0.01.

### 8. - Comments and conclusions.

Free-energy, entropy and volume differences between face-centered and body-centered cubic structures have been evaluated for model crystals. Because these differences only amount to about one percent of the respective quantities per particle in the two phases, high-precision difference methods based on ensemble sampling are employed. Statistical errors of one percent or less are obtained in most cases.

The relative stability of phases of model rare gas and alkali metal crystal is assumed within classical mechanics, but without approximations like harmonicity or the like. Results are found to be in agreement with the behaviour of real materials as well as of model systems studied in dynamical simulations of crystal nucleation $(^{6})$ and of polymorphic transformations $(^{7})$ . A linear extrapolation to high temperature and pressure (which neglects differences in second-order derivatives of the Gibbs free energy $G$ with respect to $p$ and $T$ for the two structures) of the dependence of $\Delta G$ on $p$ and $T$ estimated

locally permits one to draw the line of the polymorphic transformation in the $p$-$T$ diagram for the f.c.c.-b.c.c. transition. The existence of a stable b.c.c. phase at high pressure and temperature is predicted in this way for Lennard- Jones solids. In contrast, no high-pressure f.c.c. phase is found for model systems of Rb and Cs.

In sect. 5 we showed that for the LJ system at $T=0.5$ and $\varrho=1.0$, $S_{\text{f.c.c.}} << S_{\text{b.c.c.}}$. Thus the relative stability of the f.c.c. lattice is due to the potential energy making the dominant contribution to the stability of f.c.c. But no general statement can be made about the sign of the difference $S_{\text{f.c.c.}} - S_{\text{b.c.c.}}$. We see from sect. 6 that for an alkali metal at high density $S_{\text{f.c.c.}} > S_{\text{b.c.c.}}$ but this fails to make f.c.c. relatively more stable. Thus arguments based on the « looseness » of the b.c.c. structure as being the cause of stability are not quite valid.

Moreover, in the cases considered here, $\Delta V$ and $\Delta F$ are of the same sign, i.e. the stability is dictated by the potential energy and not by entropy.

The alkali potential functions used here fail to predict the experimentally observed transition to f.c.c. in Cs at high compression. This is presumably due to a failure of the pseudopotential second-order perturbation theory to take the changes of electronic structure properly into account. Recently MD calculations have been reported by showing the existence of such a transfor- mation for a model system describing $Li(^{31})$ akin to the ones employed in the present study of the heavier alkali metals. Therefore, we conclude that our calculations would have given a different result if applied to the model for Li.

The methods outlined and used in this paper on a few model systems show the possibility of making precise calculations of free-energy barriers to dis- placive crystalline transformations along a prescribed trajectory in configuration space. Therefore, relevant information on transition probabilities can also be obtained in addition to assessing the magnitude of the relative stability (i.e. $\Delta G$) of different crystal structures. When the barrier is absent or low enough, dynamical-simulation studies are very useful in detecting the sign of $\Delta C$, in locating the transition line (i.e. $\Delta G=0$) and in showing the route spontaneously taken by the system in undergoing the transformation. If the barrier is too high, however, dynamical simulation studies may observe the system being trapped in a metastable state during the whole time of the simulation. As an extreme example of this circumstance, we note that spon- taneous polymorphic transformations of the crystalline structures have been observed in molecular dynamic studies in which nontraditional periodic boundary conditions were used; these allow the system the additional freedom to change the shape of the elementary box. This should be contrasted to the use of the usual rigid boundary conditions made in this work. Free-energy

(31) R.G. MuNRo and R.D. MouNTAIN: Phys. Rev. B, to be published.

difference calculations here have been performed in such a way that the system is constrained to remain in a well-defined region in configuration space.

An interesting result arising from the nature of the method of overlapping distributions is that it is fallacious to think of the future simply in terms of studying «bigger» systems even if bigger computers are available. Increase in system size makes the calculations difficult, in principle, by making the distributions narrow and thus preventing their overlap.

* * *

We have profited from many useful discussions with M. PARRINELLO in the early stages of this work. GJ is grateful for the repeated warm hospitality received in the Materials Science and Technology Division at Argonne National Laboratory.

### RIASSUNTO

La differenza di energia libera, entropia e volume tra strutture cubiche a facce centrate e a corpo centrato sono valutate, per cristalli modello di gas rari e metalli alcalini, con il metodo delle distribuzioni sovrapposte. Nella regione di validità della meccanica classica si predice la stabilità delle fasi osservate per le sostanze reali anche in accordo con i risultati di precedenti studi di simulazione della nucleazione del cristallo dalla fase liquida e di trasformazioni polimorfe. Inoltre si predice in questo modo l'esistenza di una fase stabile di struttura cubica a corpo centrato per i solidi di Lennard-Jones, mentre non ci si aspetta una fase di struttura cubica a facce centrate per i metalli alcalini sotto pressione. Si mostra inoltre la possibilità di effettuare il calcolo della barriera di energia libera che impedisce le trasformazioni cristalline con spostamento lungo una traiettoria prefissata nello spazio delle configurazioni.

Относительная устойчивость FCC и ВСС структур для модельных
систем при высоких температурах.

Резюме (*). — Оцениваются различия свободных энергий, энтропий и объемов между гранецентрированными и объемоцентрированными кубическми структурами для модельных редких газов и щелочно-галоидных кристаллов, используя метод пере-крывающихся распределений. Предсказываются устойчивые фазы в соответствии с поведением реальных материалов в областях справедливости классической механики и в согласии с результатами предыдущих динамических рассмотрений зарождения кристаллов из расплава и полиморфных образований. Предсказывается существо-вание устойчивой ВСС фазы при высоких давлениях и температурах для твердых тел Леннарда-Джонса, тогда как не ожидается устойчивой FCC фазы при высоком давлении для модельных Rb и Cs систем. Мы также показываем возможность проведения вычислений барьеров свободной энергии для кристаллических превра-щений вдоль предсказанной траектории в конфигурационном пространстве.

(*) Переведено редакцией.