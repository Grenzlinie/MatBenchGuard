# Electronic structure of the zinc-blende and rocksalt phases of InSb
Eugene J. Mele
Xerox Webster Research Center, Webster, New York 14580

J. D. Joannopoulos
Department of Physics, Massachusetts Institute of Technology, Cambridge, Massachusetts 02139
(Received 19 December 1980)

The electronic structure of InSb in the common zinc-blende-crystal phase and in a rocksalt-crystal phase (which is metastable at standard temperature and pressure) are inves- tigated using a self-consistent pseudopotential formalism including relativistic effects. For the zinc-blende structure we find that a local $s$-$p$ potential for the valence electrons yields, in a self-consistent calculation for the solid, a charge density in excellent agreement with previous calculations employing empirical nonlocal potentials. Relativistic effects are found to be very important in order to obtain a good description of the band gap and overall bandwidth. For the rocksalt phase we obtain a metallic solid, in agreement with ex- periment, and observe (in comparison with the zinc-blende results) substantial changes in the valence-band density of states. These results are in very good agreement with the ex- perimental x-ray-photoemission-spectroscopy studies of these two phases. Unlike the situa- tion for the covalently bonded zinc-blende crystal, we obtain very large charge transfer from the cations to the anions (estimated to be $0.9e^-$) in the metallic rocksalt phase, which we speculate helps to stabilize the solid. Band-structure, densities-of-states, charge-density, and Fermi-surface results are presented.

## I. INTRODUCTION
InSb is a rather unusual material. It has recently been discovered that InSb can be grown in a metal- lic rocksalt structure at normal pressures and tem- peratures. $^{1}$ It is the only III-V compound found, to date, that has this property. The growth procedure involves sputtering on a cold substrate with the sub- sequent formation of microcrystals aligned along the [100] crystal axis.
The possibility of having a III-V compound grow at STP into a rocksalt phase is a very surprising result. The usual situation is that the covalent III-V compounds (as well as the group IV's and more ionic II-VI's) exist in a tetrahedrally bonded zinc- blende structure. As the bonding in the $(A^{n} B^{8-n})$ semiconductors becomes more ionic, the zinc-blende structure becomes unstable to an increase in coordi- nation number. One then finds most of the I-VII's existing in a rocksalt phase. This transition from covalent bonding and zinc blende to ionic bonding and rocksalt is delineated in Phillips's ionicitytheory. $^{2}$
Under high pressures the zinc-blende materials undergo various reversible structural transitions to metallic phases. $^{3,4}$ It is interesting that again the more ionic II-VI's revert to a rocksalt phase while the III-V's transform into a $\beta$-Sn-like phase. In both cases the coordination number increases since the bonding is becoming more metallic under pres- sure. $^{5}$ Thus the rocksalt structure supports both metallic and ionic bonding. It is interesting to note at this point that InSb can also revert to the rocksalt phase with only 13 kbar of pressure. In this case, however, the transition occurs from an amorphousfilm, and is irreversible and metastable at STP. $^{6,7}$
In order to attempt a first step in understanding the electronic structure and nature of bonding in InSb we have performed a comparative study of the zinc-blende and rocksalt phases using a state-of-the- art self-consistent pseudopotential approach. These two materials present several computational compli- cations for studies of their electronic structures.
First, both In and Sb are large-$Z$ elements, hence relativistic effects can be very important. In fact, both spin-orbit splitting and Darwin mass correc- tions are known to induce sizable shifts in the valence electronic levels. $^{8}$ These effects have only been included in previous non-self-consistent calcu- lations. $^{9,10}$ In this work we incorporate spin-orbit splitting in our self-consistent calculations following a similar scheme. $^{9,11}$ and adopt a new scheme for including relativistic $s$-wave corrections as well. The latter are found to provide a very important correc-

tion to the overall valence bandwidth in these compounds.

Second, since the rocksalt phase is metallic, we require an efficient scheme for calculating Brillouin-zone summations of the valence charge density in the construction of self-consistently screened pseudopotentials. Special point sampling schemes $^{12}$ which are conventionally employed for this purpose are only rigorously justified in the limit of completely filled bands. They are, however, expected to be very adequate in situations where the Fermi energy falls in a rather narrow band. The rocksalt band structures satisfies neither of these criteria, possessing a quite complicated Fermi surface with the Fermi energy passing through both very narrow and very dispersive bands. To obtain an accurate valence charge density we make extensive use of a $\vec{k} \cdot \vec{p}$ representation for the mixing of valence eigenstates throughout the Brillouin zone. In this way we tractably sample a mesh of $k$ points in the Brillouin zone during each iteration of the calculation.

In this paper we will proceed as follows. In Sec. II we briefly review our scheme for construction of effective local valence pseudopotentials. In Sec. III we briefly outline the procedure followed in the self-consistent calculations in the solid and discuss methods adopted to incorporate spin-orbit and mass-velocity corrections. We also outline a scheme which makes the $\vec{k} \cdot \vec{p}$ approach very efficient for such calculations on metallic systems. In Sec. IV we present results for the zinc-blende and rocksalt phases of InSb, comparing band structures, densities of states, and charge densities. Finally, in Sec. V we conclude with a further discussion of these results and their relation to previous work.

## II. POTENTIALS

As discussed extensively elsewhere, $^{13-17}$ the pseudopotential approach is founded on the assumption that one may construct an effective one-electron valence potential which retains the shape of an allelectron potential away from the core region, but replaces the singular all-electron potential near the core with a smoother weaker potential. This "pseudopotential" does not bind core states and relieves the valence wave functions of the constraint of being orthogonal to a rapidly spatially varying core wave function. As a consequence this allows for a rapidly convergent Fourier expansion of the valence eigenstates. Following this prescription one expects the pseudopotential to be $l$ dependent since, in principle, a different set of core wave functions are being deleted for each angular momentum component under consideration. In practice, however, Starkloff and Joannopoulos (SJ) (Ref. 15) have observed that for a wide variety of heavy elements (Si typically marks the transition from light to heavy in this context) a single effective ionic potential suffices to describe valence $s$ - and $p$-valence eigenfunctions.
The SJ ionic potential is parametrized in the form
$$
V_{\text {ion }}^{p s}(r)=\left(-Z e^{2} / r\right)\left[\left(1-e^{-\lambda r}\right) /\left(1+e^{-\lambda\left(r-r_{c}\right)}\right)\right],
$$
which describes a rapid truncation of an ionic $(-Z e^{2} / r)$ potential to zero near $r=r_{c}$. $\lambda$ and $r_{c}$ are then chosen such that a self-consistent atomic calculation employing this effective potential will reproduce as closely as possible some predesignated properties of a self-consistent all-electron calculation on the atom. Typically, close attention is paid to obtaining the correct valence $s$-state and $p$-state valence eigenvalues in the neutral atom while obtaining the correct magnitude and location of peaks in the radial charge density for these states.
Although the problem is clearly severely underdetermined, in practice the two parameters in the model potential of Eq. (1) satisfy all of these conditions reasonably well. The local nature of this potential then makes it computationally convenient for the self-consistent calculations to be described. In particular, the $\vec{k} \cdot \vec{p}$ scheme we introduce becomes especially efficient if the valence potential is $l$ independent.

We note further, that considerable attention has recently been paid to the norm-conserving character of the pseudopotential, $^{17}$ i.e., whether in addition to achieving the correct shape of the valence wave function away from the core, the effective potential also yields the exact magnitude of the wave function in this region. This is related to the energy range over which the pseudopotential will correctly mimic the all electron potential and hence characterizes the validity of transfer of the effective potential from the neutral atom (where it is fit) to the solid state.
Without following the explicit guidelines recently described for the construction of norm-conserving nonlocal pseudopotentials, we find that the ionic local potentials described by Eq. (1) are typically norm-conserving to $1-2 \%$.

In all the calculations discussed below we choose a local exchange-correlation potential of the form
$$
V_{\mathrm{xc}}(r)=-\left(\frac{3}{8} \pi\right)^{1 / 3} 3 \alpha \rho^{1 / 3}(r) \quad (2)
$$


<table><caption>TABLE I. $\alpha = 1$ self-consistent atomic electronic structure data.</caption>
<tbody>
<tr>
<td>
</td>
<td colspan="3">
All Electron
</td>
<td colspan="3">
Pseudopotential
</td>
</tr>
<tr>
<td>
</td>
<td>
$E$ (eV)
</td>
<td>
$r_{\text{max}}$ (a.u.)
</td>
<td>
$|rR(r)|_{\text{max}}$
</td>
<td>
$E$ (eV)
</td>
<td>
$r_{\text{max}}$ (a.u.)
</td>
<td>
$|rR(r)|_{\text{max}}$
</td>
</tr>
<tr>
<td>
Sb 5$s$
</td>
<td>
$-$14.81
</td>
<td>
1.89
</td>
<td>
0.774
</td>
<td>
$-$14.47
</td>
<td>
1.85
</td>
<td>
0.753
</td>
</tr>
<tr>
<td>
Sb 5$p$
</td>
<td>
$-$7.25
</td>
<td>
2.23
</td>
<td>
0.662
</td>
<td>
$-$7.22
</td>
<td>
2.19
</td>
<td>
0.657
</td>
</tr>
<tr>
<td>
In 5$s$
</td>
<td>
$-$10.13
</td>
<td>
2.14
</td>
<td>
0.700
</td>
<td>
$-$9.98
</td>
<td>
2.03
</td>
<td>
0.684
</td>
</tr>
<tr>
<td>
In 5$p$
</td>
<td>
$-$4.69
</td>
<td>
2.72
</td>
<td>
0.549
</td>
<td>
$-$4.65
</td>
<td>
2.65
</td>
<td>
0.539
</td>
</tr>
<tr>
<td colspan="7">
$^{\dagger}$Potential parameters
</td>
</tr>
<tr>
<td>
</td>
<td>
</td>
<td>
$z$
</td>
<td>
$r_{c}$ (a.u.)
</td>
<td>
$\lambda$ (a.u.$.^{-1}$)
</td>
<td>
</td>
<td>
</td>
</tr>
<tr>
<td>
</td>
<td>
In
</td>
<td>
3
</td>
<td>
1.206
</td>
<td>
9.8420
</td>
<td>
</td>
<td>
</td>
</tr>
<tr>
<td>
</td>
<td>
Sb
</td>
<td>
5
</td>
<td>
1.083
</td>
<td>
5.2090
</td>
<td>
</td>
<td>
</td>
</tr>
</tbody>
</table>

with $\alpha = 1$. The coefficient $\alpha = 1$ is arbitrarily chosen since it has been our experience that $\alpha = 1$ provides a better description of transition energies near the gap than smaller values of $\alpha$ which are fit to reproduce atomic total energies.

In Table I we list the results of all electron $\alpha = 1$ calculations of valence $s$ and $p$ eigenstates of In and Sb and the positions and magnitudes of the associated radial-wave-function maxima. The results of self-consistent calculations for these elements using the ionic potentials of Eq. (1) are also given for the fitted values of $\lambda$ and $r_{c}$ listed.

### III. METHOD OF CALCULATION

#### A. General consideration

In these calculations the valence wave functions are expanded in a set of plane waves, with the eigenvalues of the Hamiltonian $\{ E(k) \}$ satisfying the secular equation

$$
\begin{aligned}
\operatorname{det} \mid\left[\hbar^{2} / 2 m(K+G)^{2}-E(k)\right] & \delta_{G G^{\prime}}+V\left(G-G^{\prime}\right) \mid \\
& =0, \quad(3)
\end{aligned}
$$

where $V(q)$ is the Fourier transform of the fully screened crystal potential and the $\{ G \}$ are the reciprocal-lattice vectors. The computational mechanics required to self-consistently solve (3) have been discussed extensively elsewhere. $^{9,18}$ Here we merely note that a reasonably large set of plane waves (typically 60–70) are directly "included" in (3), augmented by an additional (typically $>150$) plane wave introduced through second-order perturbation theory. After each iteration the eigenfunctions with eigenvalues below the Fermi energy are used to construct a valence charge density which in turn is used to construct a screening potential. This potential consists of an electrostatic part due to the valence charge density

$$
V_{H}(G)=\left(4 \pi e^{2} /|G|^{2}\right) \rho(G), \quad(4)
$$

and a local exchange-correlation part of the form given in Eq. (2). The charge density and screening potential are expanded in the lowest 10 shells of reciprocal-lattice vectors. These terms are added to the bare ion pseudopotential to define the crystal potential used in the next iteration. Following an initial guess in which the self-consistent potential is approximated by an empirical potential, 5 to 6 iterations are generally required to achieve self-consistency.

#### B. $\overrightarrow{\mathbf{k}} \cdot \overrightarrow{\mathbf{p}}$ expansion

The time-limiting step in the procedure outlined above is the diagonalization of a large matrix on a mesh of $k$ values in the Brillouin zone which is sufficiently fine to provide a good description of the valence charge density. In the semiconducting zinc-blende structure this is not a serious problem since a special points scheme$^{12,19}$ yields a well converged integral over reciprocal space, requiring diagonalization of a large matrix at as few as two points in the irreducible Brillouin zone. This

scheme, however, breaks down for partially filled bands and hence we desire a more efficient procedure with which to study the metallic rocksalt structure.

We proceed with a relatively straightforward development of $\vec{k} \cdot \vec{p}$ representation for the periodic part of the band Bloch functions satisfy the effective Schrödinger equation
$$
\begin{aligned}
{\left[\left(\hbar^{2} / 2 m\right)\left(k^{2}-2 i \vec{k} \cdot \vec{\nabla}-\nabla^{2}\right)+V(r)\right] u_{n, k}(r) } & \\
& =E_{n}(k) u_{n, k}(r). \quad(5)
\end{aligned}
$$

Clearly the set $\left\{u_{n, k}\right\}$ labeled by band index $n$ are a complete orthonormal set of basis functions which may be used to expand the periodic $\left\{u_{n, k^{\prime}}\right\}$ at any other $k^{\prime}$ point in the Brillouin zone. For definiteness we will assume we have determined the $\left\{u_{n, \Gamma}\right\}$ at the zone center and wish to study the $\left\{u_{n, k}\right\}$ at some other point in the Brillouin zone. Using the $\left\{u_{n, \Gamma}\right\}$ as a basis we obtain
$$
\begin{aligned}
\sum_{n^{\prime}}\left[\frac{\hbar^{2}}{2 m}\left(k^{2} \delta_{n n^{\prime}}-2 i \vec{k} \cdot \vec{\nabla}_{n n^{\prime}}\right)+E_{n}(\Gamma) \delta_{n n^{\prime}}\right] C_{n^{\prime}}(k) & \\
& =E_{n}(k) C_{n}(k), \quad(6 a)
\end{aligned}
$$
where
$$
\vec{\nabla}_{n n^{\prime}}=\left\langle u_{n, \Gamma}|\vec{\nabla}| u_{n^{\prime}, \Gamma}\right\rangle\qquad(6b)
$$
and
$$
C_{n}(k)=\left\langle u_{n, k} | u_{n, \Gamma}\right\rangle.\qquad(6c)
$$

If the number of $\left\{u_{n, \Gamma}\right\}$ retained in the expansion of Eq. (6a) were equal to the number of reciprocal-lattice vectors included in the evaluation of $u_{n, \Gamma}$ then (6) is essentially exact. The utility of expression (6a), however, is that the expansion set can be accurately truncated for reasonably small $n$. Physically, the $\left\{u_{n, \Gamma}\right\}$ provide a local basis set of $s$, $p, d, \ldots$, etc., symmetry which is well suited for expansion of $\left\{u_{n, k}\right\}$ at any other point in the Brillouin zone. For eigenanalysis at arbitrary $k$ which would typically require direct expansion in $60-70$ plane waves, we have been able to accurately obtain the lowest six eigenvalues and eigenfunctions, limiting the expansion to the lowest $26\left\{u_{n, \Gamma}\right\}$ and treating the remainder in Lowdin perturbation theory. $^{19}$ The construction and solution of Eq. (6a) proceeds as follows.

At the zone center we expand the Hamiltonian in a finite set of $M$ plane waves (treating an additional set through Lowdin perturbation theory), saving (1) the resultant eigenvalues $\left\{E_{n}(\Gamma), n=1,2, \ldots, M\right\}$, (2) a subset of the lowest $N$ eigenfunctions $\left\{u_{n, \Gamma}\right.$, $n=1,2, \ldots, N\}$, (3) a set of effective-dipole-transition matrix elements coupling these $N$ states to each other,
$$
(B)_{n n^{\prime}}=\left\langle n\left|\vec{\nabla}(\mathrm{eff})\right| n^{\prime}\right\rangle \quad\left(n, n^{\prime}=1,2, \ldots N\right),
$$
and (4) a set of second-order coefficients,
$$
(T)_{n n^{\prime}}=\sum_{n^{\prime \prime}} \frac{\left\langle n\left|\vec{\nabla}(\mathrm{eff})\right| n^{\prime \prime}\right\rangle\left\langle n^{\prime \prime}\left|\vec{\nabla}(\mathrm{eff})\right| n^{\prime}\right\rangle}{\bar{E}-E_{n^{\prime \prime}}(\Gamma)},
$$
where $\bar{E}$ is an average band energy of the system.
The operator $\vec{\nabla}$ (eff) differs slightly from the true dipole operator due to the $k$ dependence of the second-order perturbation-theory corrections introduced by plane waves outside the direct expansion set for the $u_{n, \Gamma}$. Expanding these corrections to lowest in $k$ we obtain
$$
G(\mathrm{eff})=G+\frac{2 m}{\hbar^{2}} \sum_{G^{\prime}} \frac{\left|V_{G, G^{\prime}}\right|^{2}}{\left[G^{2}-\left(G^{\prime}\right)^{2}\right]^{2}}\left(G-G^{\prime}\right),
$$
where $G$ is inside the direct Lowdin sphere and $G^{\prime}$ is outside. Thus the effective dipole operator includes the lowest-order gradient corrections from plane waves outside the original expansion set.(This is found to be important for calculations involving the lowest-lying conduction bands.)

Having determined these matrices at a single point in the Brillouin zone, (our choice of the zone center is an optimum one since we avoid the task of having to symmetrize these various coefficients), the reduced Hamiltonian at any $k$ is then
$$
\begin{aligned}
H_{n n^{\prime}}(k)= & E_{n}(\Gamma) \delta_{n n^{\prime}} \\
& +\hbar^{2} / 2 m\left(k^{2} \delta_{n n^{\prime}}\right. \\
& \left.\quad-2 i \vec{k} \cdot \underline{B}_{n n^{\prime}}+\vec{k} \cdot \underline{T}_{n n^{\prime}} \cdot \vec{k}\right). \quad(10)
\end{aligned}
$$

All of the information about the crystal potential is contained in the $E_{n}(\Gamma)$ and the matrices $\underline{B}$ and $\underline{T}$ which are specified at a single point in the Brillouin zone. This reduced Hamiltonian can now be quickly diagonalized, and the resulting eigenvectors back-transformed to a plane-wave basis from which a charge density can be calculated. As the evaluation of the charge density can itself be a time-consuming proposition we have followed a procedure whereby the integral of the charge density over a partially filled band is initially approximated by a special point summation. Subsequently the sum is modified in only those regions of the Brillouin zone where a mostly filled (empty) band is found to move above (below) the Fermi energy. In all, no more than 16

points in the irreducible Brillouin zone are em-
ployed for this improved integration.

### C. Spin-orbit coupling

As noted in the Introduction, since both In and
Sb are heavy elements we must be concerned with
relativistic corrections to the one-electron Hamil-
tonian of the system. The most serious such correc-
tions are spin-orbit terms which in general lower the
symmetry of the spin-free one-electron solutions.
For zinc-blende InSb, they introduce level splittings
near the band gap which typically exceed the band
gap by a factor of 3. In the solid, the spin-orbit
Hamiltonian may be written
$$
H_{\mathrm{so}}=\left(\hbar / 4 m^{2} c^{2}\right) \underline{\sigma} \cdot(\vec{\nabla} V × \overrightarrow{\mathrm{p}}), \quad(11)
$$
where the $\underline{\sigma}$ are the Pauli spin matrices. This
operator is dominated by the crystal volume close to
the atomic cores, i.e., where $\vec{\nabla} V$ is large. This, un
fortunately, is where the smooth pseudo-wave-
function is a poor approximation to the rapidly os-
cillating all-electron wave function for the solid. In
empirical pseudopotential theory, the usual response
to this problem has been to project the valence
pseudo-wave-function onto the core states. Follow-
ing the work of Chelikowsky and Cohen $^{9}$ we obtain
a spin-orbit Hamiltonian
$$
\begin{aligned}
H_{\mathrm{so}}\left(\overrightarrow{\mathrm{k}} ; \overrightarrow{\mathrm{G}}, \overrightarrow{\mathrm{G}}^{\prime}\right)= & i(\overrightarrow{\mathrm{k}}+\overrightarrow{\mathrm{G}}) \\
& ×\left(\overrightarrow{\mathrm{k}}+\overrightarrow{\mathrm{G}}^{\prime}\right) \cdot \underline{\sigma} \mu P\left(\overrightarrow{\mathrm{G}}-\overrightarrow{\mathrm{G}}^{\prime}\right), \quad(12)
\end{aligned}
$$
where $P(\overrightarrow{\mathrm{G}})$ is a Fourier transform of a linear su-
perposition of site-centered core states with relative
weights fixed to the ratio of free-atom spin-orbit
splitting for valence states. For the case of InSb the
sum is accurately obtained by including only the
outermost $p$ core level. The coupling strength $\mu$ is
then taken as an adjustable parameter and is chosen
to fit the spin-orbit gap at the valence-band max-
imum in the zinc-blende phase. In calculations on
the rocksalt structure $\mu$ is adjusted only for the
change in unit-cell volume. To include the spin-
orbit contribution in the calculation, we isolate the
ten lowest-lying spin-free states (obtained as
described in the preceding section), expand the basis
set to include spin degrees of freedom, transform
(12) to the band representation and solve for the
eigenspectrum of the resulting $20 ×20$ problem.

### D. Mass velocity and Darwin corrections

Aside from the spin-orbit corrections described in
the previous section, the relativistic Hamiltonian in-
troduces two non-symmetry-breaking terms into the
one-electron Schrödinger equation,
$$
H=-p^{4} / 8 m^{3} c^{2}+\left(\hbar^{2} / 8 m^{2} c^{2}\right) \vec{\nabla}^{2} V. \quad(13)
$$

While these terms are implicitly included in an em-
pirical pseudopotential for the crystal, the ionic
pseudopotentials of Sec. II are fit to nonrelativistic
all-electron atomic calculations and hence do not in-
clude these corrections. As with the spin-orbit
terms, these additions to the Hamiltonian are dom-
inated by the crystal volume near the atomic cores.
From atomic calculations one expects these correc-
tions to be strong $(\sim 1 \mathrm{eV})$ for $s$ states of row-5 ele-
ments and negligible for the $p$ states, and higher-
lying excited states.

The importance of these corrections for the
valence electron states can be seen by noting that a
self-consistent calculation ignoring these relativistic
effects (but including spin-orbit coupling) typically
yields a valence-band width of $9.2 \mathrm{eV}$ (instead of
$10.8 \mathrm{eV}$ ) and a band gap of $\sim 0.7 \mathrm{eV}$ (instead of
$0.23 \mathrm{eV}$ ); i.e., the lowest two $s$-like bands lie sys-
tematically too high in energy. Some of this
discrepancy could in principle be attributed to the
general difficulties characterizing one-electron calcu-
lations using approximate exchange-correlation po-
tentials for the excited states of the system. It is
more probable, however, that the error is largely as-
sociated with the absence of $s$-wave corrections in
the Hamiltonian. To eliminate this difficulty we
construct an empirical scheme with parameters
chosen consistent with the magnitude of these
corrections in both the isolated atom limit and the
crystalline zinc-blende phase. In this way the calcu-
lation on the rocksalt structure will be free from ad-
ditional parameters.

We proceed by writing a nonlocal operator which
induces specified shifts of $\Delta_{1}=1 \mathrm{eV}$ at the valence-
band minimum and $\Delta_{2}=-0.33 \mathrm{eV}$ at the conduc-
tion band minimum.
$$
H=\Delta_{1}\left|\Gamma_{6}^{v}\right\rangle\left\langle\Gamma_{6}^{v}\right|+\Delta_{2}\left|\Gamma_{6}^{c}\right\rangle\left\langle\Gamma_{6}^{c}\right|. \quad(14)
$$

Assuming that the levels are spanned by a basis of
valence $s$-like orbitals, and taking the relative admix-
tures $\alpha$ of these functions from the calculated wave
functions for $\Gamma_{6}^{v}$, we construct the $2 ×2$ unitary
operator which will transform $H$ to the localized $s$ -
orbital basis
$$
U=\left[1 /\left(1+\alpha^{2}\right)^{1 / 2}\right]\left[\begin{array}{rr}
1 & \alpha \\
-\alpha & 1
\end{array}\right], \quad(15)
$$
so that

$$
U^{+} H U=\left[\begin{array}{ll}
V_{a a} & V_{a a} \\
V_{a c}^{*} & V_{c c}
\end{array}\right]
$$

The diagonal terms in (16) describe a correction that is independent of the size of the crystal. The off-diagonal terms denote a relativistic "interaction" between anions and cations and should vanish exponentially as the crystal becomes infinite. We find the choices

$$
\begin{aligned}
& V_{a a}=-0.93 \mathrm{eV}, \\
& V_{c c}=-0.47 \mathrm{eV}, \\
& V_{a c}=0.27 e^{-\beta\left(b-b_{0}\right)} \mathrm{eV},
\end{aligned}
\tag{17}
$$

correctly describe these relativistic effects in the limit $b \to b_{0}$ (the zinc-blende bond length) and $b \to \infty$ (isolated atoms). The constant $\beta^{-1}$ is not fixed by these considerations and assumes the value of the Bohr radius.

It will be recalled that the crystal potential enters the calculation at any arbitrary point in the Brillouin zone through the eigenvalues and eigenvectors at $\Gamma$. Hence, the correct specification of these relativistic adjustments at the zone center uniquely specifies them throughout the full Brillouin zone.

## IV. RESULTS
The valence bands and low-lying conduction bands obtained in these calculations are plotted along principle symmetry axes in the Brillouin zone in Fig. 1. The results for the zinc-blende phase show the familiar structure common to all III-V's: a bonding $s$-like band, localized primarily on the anions, splits away from the rest of the valence band near $-10 \mathrm{eV}$, and a cation $s$ and $p$ hybridized band extends from $-5.5 \mathrm{eV}$ to the valence-band maximum where it is spin-orbit split from two unhybridized less dispersive $p$-like bands. In this calculation we obtain a band gap of $0.26 \mathrm{eV}$.

![](./images/814705614268661760_1.jpg)

FIG. 1. Band structure along principal symmetry axes to zinc-blende InSb ($a = 6.47$ Å, left) and rocksalt InSb ($a = 6.12$ Å, right).

The lattice constant for the rocksalt crystal structure at STP is $6.12 \AA$. $^{1,6,7}$ The overall valence band structure of this phase is similar to that obtained in the zinc-blende structure, with some notable differences. Again an $s$-like bonding band localized primarily on the Sb sites splits away from the main valence band. The calculated width of this band is $30\%$ larger than the zinc-blende $s$ band. Though the InSb nearest-neighbor distance actually increases in the more dense rocksalt phase, the increased coordination more than compensates for this dilation of nearest-neighbor distance, yielding a more dispersive $s$ band. The $s$-$p$ hybridized band which extends from $-6 \mathrm{eV}$ to just below the Fermi energy is also found to be slightly more dispersive than the corresponding band in the zinc-blende phase. The most profound differences between the two structures clearly occur within several eV of the Fermi energy. In agreement with experiment, the rocksalt structure is found to be metallic. Moreover, we find

that the Fermi energy crosses two relatively un- dispersive $p$-like bands and a strongly dispersive "conduction" band. The latter dips slightly below the Fermi energy at $\Gamma$ and then plunges 3 eV below the Fermi energy at $X$. This band may be crudely identified with the lowest conduction band calculat- ed in the zinc-blende structure. $^{20}$ In this case $X$ is an antibonding state locating virtual charge "be-hind" the bonds oriented along the equivalent [111] directions. $^{21}$ The rocksalt structure which does not possess such directed bonds will have the equivalent "antibonding" level filled as valence electrons at- tempt to spread out and become more free- electron-like. This qualitative argument also ex- plains the upward shift of the bonding counterpart of this level which is found at -4 eV in the rocksalt structure. To compensate for the extra charge donated into this additional dispersive band which crosses the Fermi energy, the two higher-lying $p$ bands are slightly depleted, moving above the Fermi energy at $L$.

The densities of state calculated in these two structures are shown in Fig. 2 where they are com- pared with the x-ray photoelectron spectroscopy(XPS) spectra obtained by Minomura et al. $^{6,7}$ The results for the zinc-blende phase are in generally good agreement with the experimental spectra. We obtain an overall bandwidth of 10.7 eV which, though in good agreement with relativistic orthogo- nalized plane-wave (OPW) calculations (10.5 eV) is smaller than the 11.7 eV obtained using nonlocalempirical pseudopotentials. $^{9}$

![](./images/814705614268661760_2.jpg)

FIG. 2. Densities of states and x-ray photoemission spectra from zinc-blende InSb (top) and rocksalt InSb(bottom).

The valence-band spectrum changes quite signifi- cantly as we proceed to the rocksalt phase. The in- creased dispersion of the lowest $s$-like band which we noted previously seems to be also observed ex- perimentally. This effect and the increased disper- sion of the next-higher-lying $sp$-like band cause aneffective narrowing of the heteropolar gap near -7 eV which is also evident by comparing the two ex- perimental traces. Van Hove singularities attribut- able to the minima in two bands at the $X$ point near -4 eV contribute to the filling in of this region in the density of states. Finally, the shapes of the upper $p$ bands are strongly modified; a sharp edge emerges at -2 eV and the Fermi energy which fills in a re- gion of high state density produces a sharp cutoff in the XPS spectrum. We also note that the bending over of the dispersive conduction band obtained in the rocksalt structure contributes some rather in- teresting structure in the density of states above the Fermi energy. This could be observable, possibly, in a high-resolution x-ray-absorption study.

In Fig. 3 we compare the self-consistent valence charge density obtained for the two structures. Both maps are given in the nonpolar planes of their respective crytals, i.e., (110) for zinc blende and(100) for rocksalt. The normalization is in units of $e^{-} / \Omega_{c}$ where $\Omega_{c}$ is the unit-cell volume. For the zinc-blende structure a well-defined bond charge is obtained, displaced slightly towards the anion. The results are quite reminiscent of the charge profiles obtained by Chelikowsky and Cohen for InSb using an empirical nonlocal pseudopotential. $^{9}$ These au thors found that a local empirical pseudopotential for InSb gave a valence charge density which over- estimated the magnitudes of the bond charge and charge transfer from In to Sb (in comparison with estimates obtained from analyses of x-ray reflection intensities $^{23}$ ). The success of the present results us ing a local potential indicate that the discrepancy should be attributed to the approximate form factors employed in the local empirical potential and not specifically to its local character. It is also worth noting that the charge density is not affected appre- ciably by the relativistic effects discussed in Sec. III.

As expected, there are very significant qualitative changes in the self-consistent charge density calcu- lated for the metallic rocksalt phase. As shown in

![](./images/814705614268661760_3.jpg)
![](./images/814705614268661760_4.jpg)

FIG. 3. Top: valence charge density in units of $e^{-}/\Omega_{c}$ for zinc blende InSb in the (110) plane. Bottom: valence charge density in units of $e^{-}/\Omega_{c}$ for rocksalt shown in (100) plane.

Fig. 3(b) we find the valence charge much more strongly localized on the anions, with a slight rem- nant of a bond charge persisting along the [100] directions. There is, in fact, a minimum in the valence charge density on the cations in this struc- ture. It is difficult to construct a reliable quantita- tive estimate of the charge transfer in such a calcu- lation. On may proceed, nevertheless, by partition- ing the charge by the ratio of charges enclosed within touching spheres of equal radii centered on the anions and cations. In the zinc-blende structure we find a charge transfer of $0.24e^{-}$ from In to Sb whereas in the rocksalt phase the transfer is $0.87e^{-}$.

It would appear difficult, at first, to reconcile the persistence of this large charge transfer with the me- tallic character of the rocksalt phase. This apparent contradiction is settled by an examination of the charge densities of the various bands that cross the Fermi energy (and are hence responsible for the screening properties of the system). The charge density for the very dispersive band is given in Fig.4(a) near the $X$ point of the Brillouin zone. The change is nearly uniformly dispersived throughout the unit cell explaining the large dispersion of this band. This band is primarily responsible for the metallic nature of this structure. By contrast in Fig.4(b) the charge density of the band crossing the Fer- mi energy near $L$ is given. The electrons are found to be $p$-like and strongly localized on the anions. Moreover the density of states at the Fermi energy is dominated by these carriers. These very heavy electrons contribute less efficiently to the metallic character of the crystal and are certainly incapable of screening the positive ions left on the cation sites. We thus conclude that states near the Fermi energy are of two types: (1) very heavy carriers get local- ized on the anion sites explaining the large charge transfer from In to Sb in this structure and (2) a smaller number of light electrons are nearly uni- formly spread throughout the unit cell forming a strongly dispersive band explaining the metallic na- ture of the phase.

![](./images/814705614268661760_5.jpg)
![](./images/814705614268661760_6.jpg)

FIG. 4. Top: charge density for conduction band at $X$ in (100) plane of rocksalt InSb. Normalization is $(1e^{-}/\Omega_{c})$. Bottom: charge density for conduction band at $L$ in (100) plane of rocksalt InSb. Normalization is $(1e^{-}/\Omega_{c})$.

Finally, in Fig. 5, we show the intersections of the Fermi surfaces for these various bands with the $\Gamma XK$ plane and the $\Gamma XL$ plane. The Fermi surface is clearly a complex multisheeted structure. We note briefly that the light dispersive electrons, previ-

![](./images/814705614268661760_7.jpg)

FIG. 5. Fermi surfaces for rocksalt InSb in $\Gamma XL$ plane (top) and $\Gamma XK$ plane (bottom). The numbers identify bands in order of increasing energy at the $L$ point of the Brillouin zone.

ously alluded to, are located in sizable pockets centered at the $X$ points of the Brillouin zone and a tiny pocket at the zone center. The "heavy" bands are characterized by pockets of holes at the $L$ point and zone center, and an open orbit nearly parallel to the $\Gamma-L$ axis.

### V. SUMMARY AND DISCUSSION
The present results complement a previous empirical study of the band structures of zinc-blende and rocksalt InSb using extended Hückel theory. $^{24}$ Several features obtained in this very simple theory are consistent with the present more realistic calculations. In particular the transition from the semiconducting to the metallic state and the location of the dispersive band near the $X$ point of the Brillouin zone are also obtained in the Hückel calculations. The present results, however, provide a generally more satisfying description of the XPS spectrum for the metallic phase. In addition, these self-consistent calculations identify an interesting transition in character of the valence charge in these structures. In the zinc-blende crystal we obtain, as expected, a partially ionic yet well defined covalent bond connecting the In and Sb sites. On the other hand, the rocksalt structure, though metallic, is characterized by charge transfer near unity from the cation to anion sites. This charge transfer is attributable to the presence of $p$-like bands near the Fermi level which are primarily localized on the anion sites. It has previously been suggested, $^{6}$ however, that the charge transfers in the zinc-blende and rocksalt structures are nearly equivalent. This was based on core-level spectroscopy of the In and Sb $4d$ levels. Our results are clearly inconsistent with this conclusion. The discrepancy may be attributable to the inability of core-level spectroscopy to distinguish between and separate the on-site Coulomb contribution from the lattice Madelung contribution to the chemical shifts.

The large charge transfer predicted from these calculations presumably helps to stabilize the ionic rocksalt crystal structure. It is curious that InSb, which is considered to be as covalent as the prototypical covalent heteropolar semiconductor GaAs, can be prepared in a rocksalt structure at all. As noted in the Introduction a $\beta$-Sn-like metallic phase is generally obtained by pressurizing compounds in the zinc-blende crystal structure (including InSb). This leads one to speculate that the sputtered and amorphous InSb films that yields the rocksalt structure may be systematically more ionic than their zinc-blende counterparts. This may reflect an increase in charge transfer that would be expected in internal surfaces, voids, or defects.

In any case the metastability of the rocksalt structure at STP is consistent with the fact that InSb is the most metallic tetrahedrally coordinated semiconductor (other than Sn). Following this argument GaSb and AlSb may be expected to exhibit similar anomalous behavior.

### ACKNOWLEDGMENTS
We should like to thank Dr. B. Weinstein and Dr. F. Herman for some helpful discussions. One of us (J.D.J.) should also like to thank the Alfred P. Sloan Foundation for a fellowship and acknowledge partial support of this work from ONR No. N00014-77-C-0132.

$^1$H. Oyanagi and S. Minomura, unpublished.

$^2$J. C. Phillips, *Bonds and Bands in Semiconductors* (Academic, New York, 1973).

$^3$A. Jayaraman, R. C. Newton, and G. C. Kennedy, *Nature* (London) 191, 1288 (1961).

$^4$R. E. Hanneman, M. D. Banus, and G. C. Gatos, J. Phys. Chem. Solids. 25, 293 (1964).

$^5$A theoretical framework for the interpretation of these transitions has been given by J. A. VanVechton, Phys. Rev. B 7, 1479 (1973).

$^6$H. Oyanagi and S. Minomura, unpublished.

$^7$S. Minomura, O. Shimomura, K. Asaumi, H. Oyanagi, and K. Takemura, *Proceedings of the Seventh International Conference on Amorphous and Liquid Semiconductors*, edited by W. E. Spear (Edinburgh University, Edinburgh, 1977); O. Shimomura, K. Asaumi, N. Sakai, and S. Minomura, Philos. Mag. 34, 839 (1976).

$^8$F. Herman and S. Skillman, *Atomic Structure Calculations* (Prentice Hall, Englewood Cliffs, New Jersey, 1963).

$^9$J. R. Chelikoswky, and M. L. Cohen, Phys. Rev. B 14, 556 (1976).

$^{10}$I. B. Ortenburger and W. E. Rudge, IBM Research Laboratory Reports RJ-1041 (unpublished).

$^{11}$L. R. Savaria and D. Brust, Phys. Rev. 176, 915 (1968).

$^{12}$P. J. Chadi and M. L. Cohen, Phys. Rev. B 8, 5747 (1973); A. Baldareschi, ibid. 7, 5212 (1973).

$^{13}$J. C. Phillips and L. Kleinman, Phys. Rev. 116, 880 (1959).

$^{14}$M. L. Cohen, and V. Heine, in *Solid State Physics*, edited by H. Ehrenreich, F. Seitz, and D. Turnbull (Academic, New York, 1970), Vol. 24, p. 37f.

$^{15}$J. D. Joannopoulos, T. Starkloff, and M. Kastner, Phys. Rev. Lett. 38, 660 (1977); T Starkloff and J. D. Joannopoulos, Phys. Rev. B 16, 5212 (1977).

$^{16}$A. Zunger and M. L. Cohen, Phys. Rev. B 18, 5449 (1978).

$^{17}$D. R. Hamann, M. Schluter, and C. Chiang, Phys. Rev. Lett. 43, 1494 (1979).

$^{18}$M. Schluter, J. Chelikowsky, S. G. Louie, and M. L. Cohen, Phys. Rev. B 12, 4200 (1975).

$^{19}$P. O. Lowdin, J. Chem. Phys. 19, 1396 (1951).

$^{20}$Y. W. Tsang and M. L. Cohen, Phys. Rev. B 9, 3541 (1974).

$^{21}$J. P. Walter and M. L. Cohen, Phys. Rev. B 4, 1977 (1971).

$^{22}$J. R. Chelikowsky and M. L. Cohen, Phys. Rev. Lett. 36, 229 (1976).

$^{23}$D. H. Bilderback and R. Collela, Phys. Rev. Lett. 35, 858 (1975).

$^{24}$T. Shimizu and N. Ishii, Phys. Lett. 62A, 122 (1977).