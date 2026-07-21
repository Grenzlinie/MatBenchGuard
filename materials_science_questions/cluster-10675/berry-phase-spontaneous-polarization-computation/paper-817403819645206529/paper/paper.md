# Dipole-dipole interactions and incommensurate order in perovskite structures

R. G. Burkovsky*

Peter the Great St. Petersburg Polytechnic University, 29 Politekhnicheskaya, 195251 Saint Petersburg, Russia

![](./images/817403819645206529_1.jpg)
(Received 3 January 2018; revised manuscript received 21 April 2018; published 31 May 2018)

Dipole-dipole (DD) interactions are known to play an important role in conditioning ferroelectricity in $ABO_3$ perovskite crystals. Their possible role in conditioning nonferroelectric (inhomogeneous) cation ordering is presently unexplored. I analyze the energy of DD interactions in perovskite structure for different inhomogeneous spatial patterns of electric dipoles localized at the lattice sites. I show that DD interactions can favor inhomogeneous ordering when other terms of the Hamiltonian allow large total polarizability of $A$ sites, comparably large total polarizability of oxygen sites in $A$-O planes, and relatively weak total polarizability of oxygen sites in the $B$-O direction. These conditions are naturally expected in $PbZrO_3$ crystals, for which the reason behind antiferroelectric and incommensurate inhomogeneous ordering is currently being debated.

DOI: 10.1103/PhysRevB.97.184109

## I. INTRODUCTION

Perovskite crystals and thin films have many technological applications in electromechanical sensors and actuators, pyro-electric sensors, and electrocaloric, energy storage, and memory devices [1–5]. The physics of these materials has proven to be challenging, and many questions remain unresolved.

In particular, the reason for antiferroelectric (AFE) and incommensurate (IC) instabilities in $PbZrO_3$-like perovskites is currently being debated. Historically it was assumed that there should be an AFE soft mode that triggers an AFE phase transition [6]. This assumption implies a temperature-dependent minimum in phonon dispersion at the nonzero wave vector in the cubic phase. For $PbZrO_3$, this minimum should be located at the wave vector that describes AFE modulations: $\mathbf{q}_{AFE}=(\frac{1}{4},\frac{1}{4},0)$. Experimentally, it was discovered that there is no such minimum, but there is a strongly flattened transverse acoustic (TA) phonon branch, which is temperature-dependent not only at $\mathbf{q}_{AFE}$ but in a much broader range of the $\Gamma$-$M$ direction $[\mathbf{q}=(\xi,\xi,0)]$ of the Brillouin zone, which might be compatible with the critical dynamics associated with the IC phase transition [7]. The AFE transition is being considered to occur when the energy of the TA branch becomes sufficiently small that the anharmonic terms of the Hamiltonian (umklapp interaction [7] or trilinear coupling [8,9]) can trigger the formation of the commensurate AFE phase instead of the IC phase. Under hydrostatic pressure, the temperature-driven phase-transition scenario is more complex [10]. A new low-symmetry (presumably orthorhombic [10]) phase, which is free from modulations in the Pb sublattice, appears below the cubic phase. Prior to the transition from this phase to the IC modulated phase $[\mathbf{q}_{IC} \approx (0.2,0.2,0)]$, there is a critical increase of diffuse scattering at that wave vector, indicating the presence of an IC soft mode.

The AFE and IC transitions seem to occur as a result of critical increase of generalized susceptibility at finite wave vectors belonging to the $\Gamma$-$M$ direction. In other directions, the generalized susceptibility is much lower and largely temperature-independent. In other terms, the generalized stiffness (inverse of susceptibility) is strongly anisotropic in the Brillouin zone and pronouncedly small along the $\Gamma$-$M$ direction in contrast to other directions. The physical reason for this particular stiffness distribution in $PbZrO_3$-like crystals is studied intensively.

With regard to phenomenological analysis, the anisotropic dispersion of the TA branch has been modeled within the framework of Landau theory by inclusion of gradient terms of the form $(\frac{dP}{dx}u-P\frac{du}{dx})$, where $P$ denotes macroscopic polarization and $u$ denotes elastic strain. These terms reflect the flexoelectric interaction, which is the interaction between polarization and inhomogeneous strain and vice versa [7]. With regard to atomistic models, the possibility of a flattened stiffness branch with a finite-wave-vector minimum was considered in Ref. [11]. The authors have considered two order parameters — Pb displacements and oxygen octahedral tilts — and the simplest coupling between them, in the sense that it involves relatively close neighbors. It is shown that this coupling can contribute to the lowering of stiffness at finite wave vectors along the $\Gamma$-$M$ direction. However, this coupling is of short-range character; the coupling due to the dipole-dipole (DD) interactions has not been considered.

Presently there are no results indicating that the DD interactions can contribute to flattening of the stiffness dispersion along the $\Gamma$-$M$ direction. In contrast, they are known to contribute strongly to the lowering of stiffness at the zone center [12,13], which is referred to as the Lorentz correction [14]. In addition, it is known that at particular combinations of ionic polarizabilities, they can also contribute to the lowering of stiffness for wave vectors in $\{hk0\}$ reciprocal space planes [15], which is reminiscent of the observed phonon spectra in $KNbO_3$ and similar crystals.

In this paper, I show that at particular conditions for polarizabilities, the DD interactions do contribute toward reduced stiffness selectively in the $\Gamma$-$M$ direction, particularly toward dispersion with a minimum at the finite wave vector. These

*roman.burkovsky@gmail.com

conditions are readily expected in PbZrO₃-like crystals, in contrast to other perovskites, for which this type of stiffness dispersion is not observed. The results suggest that the DD interactions can be important in conditioning IC and AFE phases.

In Sec. II, I specify the DD energy in a perovskite structure and the dipole patterns that are relevant for transverse modes in the $\Gamma$-$M$ direction, and I outline the simple dynamical model suitable for demonstrating the effect of DD interactions on the stiffness dispersion. In Sec. III, I compute the Coulomb coefficients and localize those of them that contribute toward flattened and even negative stiffness dispersion along the $\Gamma$-$M$ direction. Further, I explore the effect of DD interactions on the stiffness dispersion by modeling. In Sec. IV, I examine the possibility of explaining the observed behavior of real crystals using the results obtained. Section V contains a concise summary.

## II. METHOD

### A. Dipole patterns characteristic of the transverse modes in the $\Gamma$-$M$ direction

The specifics of the problem makes it more convenient to consider the lattice energy not in terms of ionic displacements $\mathbf{u}$, which is more common, but in terms of electric dipoles associated with them: $\mathbf{d} = \mathbf{Z}\mathbf{u}$, where $\mathbf{Z}$ is the appropriately defined charge.

I consider the DD interactions in the approximation where each site of the cubic $ABO_3$ lattice is characterized by the local electric dipole $d_{l,k,\gamma}$, where $l$ enumerates unit cells, $k$ denotes sites in the cell, and $\gamma$ denotes Cartesian coordinate $(x,y,z)$. In the Fourier representation, $d_{l,k,\gamma} = \sum_{\mathbf{q}} p_{k,\gamma}(\mathbf{q})\exp(i\mathbf{q} \cdot \mathbf{r}_{l,k})$, where $\mathbf{q}$ denotes the wave vector in the first Brillouin zone, $\mathbf{r}_{l,k}$ is the site position, and $p_{k,\gamma}(\mathbf{q})$ is the Fourier component of the spatial distribution of dipoles in the sublattice.

An arbitrary dipole pattern is described by 15 independent components $p_{k,\gamma}(\mathbf{q})$ (five atoms by three Cartesian coordinates) for each wave vector. However, only a small subset of all possible dipole patterns is relevant to the problem. For explaining the possible influence of DD interactions on the stiffness along the $\Gamma$-$M$ direction, only those patterns are relevant that correspond to the $\Sigma_3$ irreducible representation (IR) (in the notation of Cowley [16]). This IR describes anomalously low-energy transverse modes associated with the phase transition in PbZrO₃. The IR is five-dimensional, meaning that the allowed dipole pattern is a superposition of five components, each described by an independent amplitude. These components are shown schematically in Fig. 1. I label them $p_A$, $p_B$, $p_{O1}$, $p_{ORot}$, and $p_{ODist}$. They are defined as [16]¹

$$
\begin{aligned}
p_{\text{Pb},x} &= -p_{\text{Pb},y} = p_A/\sqrt{2}, \\
p_{\text{Zr},x} &= -p_{\text{Zr},y} = p_B/\sqrt{2}, \\
p_{\text{O1},x} &= -p_{\text{O1},y} = p_{\text{O1}}/\sqrt{2}, \\
p_{\text{O2},x} &= -p_{\text{O3},y} = p_{\text{ORot}}/\sqrt{2}, \\
p_{\text{O3},x} &= -p_{\text{O2},y} = p_{\text{ODist}}/\sqrt{2}.
\end{aligned}
\tag{1}
$$

![](./images/817403819645206529_2.jpg)

FIG. 1. Dipole patterns corresponding to the four independent amplitudes of the $\Sigma_3$ irreducible representation. The fifth pattern, corresponding to the dipole waves in the $B$ sublattice, is omitted for clarity. Each pattern is shown for the two ends of the $\Gamma$-$M$ direction.

The $A$, $B$, and O1 sublattices are allowed to possess only transverse dipole waves in this representation. The dipole waves in the O2 and O3 sublattices are entangled and described by independent amplitudes $p_{\text{ORot}}$ and $p_{\text{ODist}}$. These patterns correspond to the dipoles at oxygen sites directed along $A$-O planes and along $B$-O chains, respectively. At the zone boundary $[\mathbf{q} = (\frac{1}{2},\frac{1}{2},0)]$, the $p_{\text{ORot}}$ dipole pattern corresponds to the antiphase rotations of oxygen octahedra. The $p_{\text{ODist}}$ amplitude corresponds to the antiphase distortions of the octahedra. When

---
¹The unit cell is chosen as $A$: (0,0,0); $B$: $(\frac{1}{2},\frac{1}{2},\frac{1}{2})$; O1: $(\frac{1}{2},\frac{1}{2},0)$; O2: $(\frac{1}{2},0,\frac{1}{2})$; O3: $(0,\frac{1}{2},\frac{1}{2})$.

$q$ is decreased, the dipole patterns corresponding to $p_{\text{ORot}}$ and $p_{\text{ODist}}$ transform gradually to the components of homogeneous polarization at $q \to 0$. To illustrate how these patterns change with changing wave vector, Fig. 1 shows each pattern for the zone center and the zone boundary.

### B. DD energy
For each wave vector, the DD energy is given by the quadratic form in terms of $\{p_{k,\gamma}(\mathbf{q})\}$ as
$$
W^{\text{DD}}(\mathbf{q}) = \frac{1}{2} \sum_{k,k',\gamma,\gamma'} C_{k,k',\gamma,\gamma'}(\mathbf{q}) p_{k,\gamma}(\mathbf{q}) p_{k',\gamma'}^*(\mathbf{q}), \tag{2}
$$
where * stands for complex conjugate. The kernel of the quadratic form is given by Coulomb coefficients $C_{k,k',\gamma,\gamma'}(\mathbf{q})$, which are computed using Ewald's method, as described in Refs. [17,18] and in the Appendix of this paper. After transforming the coordinates from $\{p_{k,\gamma}\}$ to $p_A \cdots p_{\text{ODist}}$, the DD energy takes the form
$$
\begin{aligned}
W^{\text{DD}} &= \frac{1}{2} \big(p_A^* \cdots p_{\text{ODist}}^*\big) \begin{pmatrix}
C_{\text{A-A}} & \cdots & C_{\text{A-ODist}} \\
\vdots & \ddots & \vdots \\
C_{\text{A-ODist}} & \cdots & C_{\text{ODist-ODist}}
\end{pmatrix} \\
&\quad \times \begin{pmatrix}
p_A \\
\vdots \\
p_{\text{ODist}}
\end{pmatrix}.
\end{aligned} \tag{3}
$$

The dipole patterns $p_A \cdots p_{\text{ODist}}$ do not interact with the macroscopic electric field, and the coefficients $\{C\}$ in (3) describe only that part of the DD interaction that is analytic at $q \to 0$ and is referred to, sometimes, as the short-range part of DD interactions [19].

### C. Stabilizing terms of the Hamiltonian
In modeling the stiffness dispersion, I use a Hamiltonian of the form
$$
W^{\text{Total}} = W^{\text{DD}} + W^S, \tag{4}
$$
where $W^S$ is the part that describes the energy cost of creating dipole waves in the absence of DD interactions. In the calculations, I use the following form (in the coordinate system of $\Sigma_3$ IR):
$$
\begin{aligned}
2W^S &= \alpha_A^{-1}|p_A|^2 + \alpha_B^{-1}|p_B|^2 + \alpha_{\text{O-A}}^{-1}|p_{\text{O1}}|^2 \\
&\quad + \alpha_{\text{O-A}}^{-1}|p_{\text{ORot}}|^2 + \alpha_{\text{O-B}}^{-1}|p_{\text{ODist}}|^2.
\end{aligned} \tag{5}
$$

The values $\alpha$ describe polarizabilities of individual lattice sites. Oxygen sites have tetragonal symmetry and are characterized by two polarizability constants: $\alpha_{\text{O-A}}$ (in A-O planes) and $\alpha_{\text{O-B}}$ (along O-B chains). The rationale behind this approach can be understood by noting that Eq. (3) becomes exact when the positions of all ions are fixed and their dipolar response to the field is determined by single-ion electronic polarizabilities (approximation of a purely ionic crystal). For real perovskite crystals this approximation is generally incorrect, but for $\text{PbZrO}_3$ it is expected to be largely adequate. The single-ion electronic polarizabilities of $\text{Pb}^{2+}$ and $\text{O}^{2-}$ are large [20] and the short-range force constants linking those ions to each other are relatively small [21]. This allows the assumption that the approximation of independently polarizable sites should be adequate, at least on a qualitative level, for describing $p_A$, $p_{\text{O1}}$, and $p_{\text{ORot}}$ degrees of freedom, which are the degrees of freedom of primary interest.

### D. Calculation of dipolar stiffness
The model Hamiltonian [Eq. (4)] is linked to the elements of the total stiffness matrix $S_{k,k',\gamma,\gamma'}$ as
$$
W^{\text{Total}} = \frac{1}{2} \sum_{k,k',\gamma,\gamma'} S_{k,k',\gamma,\gamma'} p_{k,\gamma} p_{k',\gamma'}^*. \tag{6}
$$

In the following section, I use the compact term "stiffness" to refer to the lowest eigenvalue of the total stiffness matrix.

## III. RESULTS

### A. Analysis of Coulomb coefficients
To identify the combinations of dipole patterns $p_A \cdots p_{\text{ODist}}$ that can be energetically preferred at finite wave vectors over the zone center, I compute and analyze the wave-vector dependence of the relevant Coulomb coefficients along the $\Gamma$-$M$ direction. This type of analysis has not been published before for perovskite structure. Figure 2 shows the coefficients linking $A$ and the oxygen subsystem in Eq. (3). The coefficients related to the $B$ ion are omitted for clarity, since $\text{Zr}^{4+}$ is not

![](./images/817403819645206529_3.jpg)

FIG. 2. Coefficients describing the energy of dipole-dipole interactions between $A$ and oxygen sublattices of cubic perovskite structure for wave vectors along the $\Gamma$-$M$ direction, and for dipole patterns corresponding to the $\Sigma_3$ irreducible representation.

involved in the unstable modes of PbZrO₃ and is very weakly polarizable [20].

The key dipole patterns of interest are $p_A$ and $p_{\text{ORot}}$ (see Fig. 1), which are linked to the unstable phonon modes in PbZrO₃ crystal [7-9,21]. For obtaining initial insight, it is instructive to first consider the reduced system, where only those two patterns are allowed. The DD energy of this reduced system is

$$
\begin{aligned}
W^{\mathrm{DD}}= & \frac{1}{2}\left(p_{A}^{*}, p_{\mathrm{ORot}}^{*}\right)\left(\begin{array}{cc}
C_{A-A} & C_{A-\mathrm{ORot}} \\
C_{A-\mathrm{ORot}} & C_{\mathrm{ORot-ORot}}
\end{array}\right) \\
& \times\left(\begin{array}{c}
p_{A} \\
p_{\mathrm{ORot}}
\end{array}\right),
\end{aligned}
\tag{7}
$$

where all terms are $\mathbf{q}$-dependent.

The first main observation is that DD interactions do favor the simultaneous presence of the same phase $p_A$ and $p_{\text{ORot}}$ patterns along the broad range of wave vectors. The energy cost of the simultaneous presence of $p_A$ and $p_{\text{ORot}}$ patterns is affected by the cross terms in Eq. (7). The corresponding contribution to the energy is $C_{A-\text{ORot}}\text{Re}(p_A^* p_{\text{ORot}})$. The $C_{A-\text{ORot}}(\mathbf{q})$ dependence shows that when $p_A$ and $p_{\text{ORot}}$ have the same phase (for $q \to 0$ this means the same direction of sublattice polarization), the resulting contribution is negative for the whole $\Gamma$-$M$ direction, except the $M$ point.

It is important that the coupling amplitude does not diminish upon approaching the $\Gamma$ point. This is in contrast to the picture of short-range coupling between $A$ ion shifts and oxygen octahedra tilts, as considered in Ref. [11], where the coupling at the $\Gamma$ point is forbidden.

The second main observation is that $C_{A-A}(\mathbf{q})$ and $C_{\text{ORot-ORot}}(\mathbf{q})$ dependences do favor competing trends in the stiffness dispersion of the coupled $p_A$-$p_{\text{ORot}}$ system. The energy cost of the $p_A$ pattern, as determined by the DD interaction with itself (coefficient $C_{A-A}$), increases upon going from zone center to zone boundary. The energy cost of the $p_{\text{ORot}}$ pattern, in contrast, decreases. One should expect that these conflicting trends can result in either positive, flat, or negative total stiffness dispersion at small wave vectors, depending on the other (stabilizing) terms of the Hamiltonian. If stabilizing terms result in a large energy cost for the $p_A$ pattern, the total stiffness dispersion is expected to follow the negative $C_{\text{ORot-ORot}}$ dispersion. If the stabilizing terms result in a large energy cost for the $p_{\text{ORot}}$ pattern, the positive $C_{A-A}$ dispersion is expected to dominate. In the case of comparable energy costs of $p_A$ and $p_{\text{ORot}}$ patterns due to the stabilizing terms, one can expect flattened dispersion.

In the following, I explore the available scenarios by modeling.

### B. Modeling results

I model the total energy of the lattice using Eq. (4). The only model parameters are site polarizabilities $\alpha_A, \alpha_B, \alpha_{\text{O}-A}$ (oxygen polarizability in $A$-O planes), and $\alpha_{\text{O}-B}$ (oxygen polarizability along $O$-$B$ chains). I explore the following three trends:

(i) The shift of stiffness minimum from zone center to finite wave vectors upon increasing $\alpha_{\text{O}-A}$, while keeping $\alpha_{\text{O}-B}=0$.

(ii) The shift of stiffness minimum from finite wave vectors to zone center upon decreasing the oxygen polarizability anisotropy $\delta=\alpha_{\text{O}-A}/\alpha_{\text{O}-B}$.

(iii) The increase of the stiffness anisotropy in the $hk0$ plane upon increasing the oxygen polarizability anisotropy.

### 1. Trend 1: the shift of stiffness minimum from zone center to finite wave vectors upon increasing $\alpha_{\text{O}-A}$

The first calculation shows that the system reduced to only $p_A$, $p_{\text{ORot}}$, and $p_{\text{O1}}$ degrees of freedom demonstrates a crossover from positive to negative stiffness dispersion at small wave vectors, and that the latter case allows an IC minimum of stiffness. The reduction is achieved by assuming $\alpha_B=\alpha_{\text{O}-B}=0$. Oxygen sites are not allowed to polarize in the direction toward the $B$ ion, but they are allowed to polarize in $A$-O planes. The stabilizing part of the Hamiltonian is controlled by polarizabilities $\alpha_A$ and $\alpha_{\text{O}-A}$.

To show the trend, I have selected a series of different pairs $(\alpha_A,\alpha_{\text{O}-A})$ that all result in the minimum of stiffness dispersion touching the zero stiffness level (the condition of instability of a modeled system). Figure 3 shows a series of stiffness profiles corresponding to those $(\alpha_A,\alpha_{\text{O}-A})$ pairs. The result confirms that the competition between positive and negative dispersions of Coulomb coefficients $C_{A-A}(\mathbf{q})$ and $C_{\text{ORot-ORot}}(\mathbf{q})$ can result in negative stiffness dispersion when the polarizability of oxygen in $A$-O planes is sufficiently large.

The finite-wave-vector minimum does appear in this case, because of gradual decoupling of $p_A$ and $p_{\text{ORot}}$ degrees of freedom upon approaching the zone boundary, resulting in the stiffness increase at large wave vectors. This is conditioned by the decline in magnitude of the $C_{A-\text{ORot}}$ coupling coefficient.

![](./images/817403819645206529_4.jpg)

FIG. 3. Profiles of the lowest eigenvalue of the total stiffness matrix along the $\Gamma$-$M$ direction for the case of only $p_A$ and $p_{\text{ORot}}$ degrees of freedom enabled by nonzero polarizabilities $\alpha_A$ and $\alpha_{\text{O}-A}$. An incommensurate minimum appears for sufficiently large $p_{\text{ORot}}$. The inset shows the combinations of $\alpha_A$ and $\alpha_{\text{O}-A}$ that correspond to the profiles.

![](./images/817403819645206529_5.jpg)

FIG. 4. (a) Profiles of the lowest total stiffness eigenvalue along the $\Gamma$-$M$ direction for a set of the values of oxygen polarizability anisotropy ($\delta = 1$, 1.2, 1.4, 1.7, 2, and 3). (b) Dependence of the position of the profile minimum on the oxygen polarizability anisotropy.

## 2. Trend 2: the shift of stiffness minimum from finite wave vectors to zone center upon decreasing the oxygen polarizability anisotropy

Next I show that the tendency toward negative small-wave-vector stiffness dispersion is suppressed when the oxygen the sites become highly polarizable not only in $A$-O planes but also along $B$-O chains.

To make the modeling possibly more realistic, the $A$- and $B$-site polarizabilities are made equal to the electronic polarizabilities of $\text{Pb}^{2+}$ and $\text{Zr}^{4+}$ [20]: $\alpha_A = \alpha_{\text{Pb2+}}^{\text{electronic}} = 4.9$ $\text{\AA}^3$, $\alpha_B = \alpha_{\text{Zr4+}}^{\text{electronic}} = 0.37$ $\text{\AA}^3$. It is known that oxygen electronic polarizability should be relatively large [20], but the corresponding effective value is not unique and varies from crystal to crystal depending, in particular, on the size of "free space" available to the $\text{O}^{2-}$ ion [22]. In modeling, I have used oxygen polarizability components $\alpha_{\text{O-}A}$ and $\alpha_{\text{O-}B}$ as variable parameters.

Figure 4 shows the stiffness profiles corresponding to the different pairs ($\alpha_{\text{O-}A}$,$\alpha_{\text{O-}B}$). The pairs are chosen to provide a stiffness minimum touching the zero stiffness level. The figure traces the evolution of the profile as a function of oxygen polarizability anisotropy $\delta = \alpha_{\text{O-}A}/\alpha_{\text{O-}B}$. At high polarizability anisotropy levels, the stiffness minimum is at finite wave vectors, in agreement with the results of the previous section.

However, the decrease of the anisotropy level results in a shift of stiffness minimum back to smaller wave vectors and eventual arrival to the zone center.

The reason for this trend is that when the $p_{\text{ORot}}$ pattern is complemented by the $p_{\text{ODist}}$ pattern of similar magnitude, the oxygen subsystem stops favoring negative dispersion. Let us consider the specific composite dipole pattern composed from the equal-in-magnitude $p_{\text{ORot}}$ and $p_{\text{ODist}}$ patterns: $p_{\text{ORot}} = p_{\text{ODist}} = p$. The energy of this pattern will be ($C_{\text{ORot-ORot}} + C_{\text{ORot-ODist}})|p|^2$. But, as one may see from Fig. 2, the positive dispersion of $C_{\text{ORot-ODist}}$ nearly cancels the negative dispersion of $C_{\text{ORot-ORot}}$ when they are summed up. As a result, the energy of the pattern composed from equal-in-magnitude $p_{\text{ORot}}$ and $p_{\text{ODist}}$ is nearly wave-vector-independent, in contrast to the pattern composed of the $p_{\text{ORot}}$ component alone. The situation with $p_{\text{ORot}} \approx p_{\text{ODist}}$ becomes achievable when sufficiently large polarizability $\alpha_{\text{O-}B}$ makes the $p_{\text{ODist}}$ pattern allowed.

## 3. Trend 3: the increase of the stiffness anisotropy in the $hk0$ plane upon increasing oxygen polarizability anisotropy

Finally I show that the flattened and negative dispersion, explored in Figs. 3 and 4, is specific solely to the $\Gamma$-$M$ direction. For this purpose, I compute a set of two-dimensional distributions of stiffness in the $hk0$ plane, corresponding to the several curves in Fig. 4. Figure 5 shows the three-dimensional plots of the lowest total stiffness eigenvalue in the $hk0$ plane of the Brillouin zone. For the cases of large and anisotropic oxygen polarizability ($b$ and $c$), the pronouncedly small eigenvalue is solely at the $\Gamma$-$M$ direction. For the dipolar waves in other directions, the DD interactions create large additional energy cost. The increase of oxygen polarizability anisotropy results in an increase of stiffness dispersion anisotropy.

---

## IV. DISCUSSION

### A. Summary of the trends and the relation to phonon soft modes

The results of modeling show how the polarizabilities affect the stiffness landscape. When oxygen polarizability is isotropic, the stiffness minimum is at the zone center and the stiffness dispersion is also largely isotropic. This is expected for a normal ferroelectric crystal, which is unstable with respect to homogeneous polarization and whose critical dynamics is represented by a largely isotropic ferroelectric soft mode. When oxygen polarizability is highly anisotropic and not too small compared to $A$-site polarizability, the stiffness dispersion becomes "unbent" along the $\Gamma$-$M$ direction while retaining large positive dispersion along the other directions. The gradual unbending of the stiffness dispersion first results in its flattening, and then in the appearance of a minimum at finite wave vectors. When the dispersion is largely flat, the preferred ordering type is nondetermined on the level of considering stiffness dispersion: the energy of the homogeneous dipole pattern is the same as the energy of the IC or AFE patterns. In the language of soft phonon modes, this picture is rather complex since the flat polarization branch corresponding to the flat stiffness dispersion is subject to avoided crossing with the transverse acoustic branch, which has linear dispersion reflecting the crystal elasticity. The resulting picture should correspond to the simultaneous presence of the low-energy

![](./images/817403819645206529_6.jpg)

FIG. 5. Distributions of the lowest total stiffness eigenvalue in the hk0 plane of the Brillouin zone for the three different degrees of oxygen polarizability anisotropy. Anisotropy parameter $\delta = \alpha_{O-A}/\alpha_{O-B}$ is 1.0 (a), 1.51 (b), and 1.83 (c).

zone-center TO mode and the strongly flattened low-energy TA branch along the $\Gamma$-$M$ direction. This seems to be consistent with the experimentally observed phonon spectra in $PbZrO_3$ [7] and $PbHfO_3$ [23].

### B. The difference between DD and short-range couplings between $A$ and oxygen sublattices

With the present results taken into account, there are two different coupling types identified that can contribute toward IC instability in a perovskite structure. The first coupling type is considered in Ref. [11]. It corresponds to the energy of short-range interactions between transverse Pb-ion displacement waves and the waves related to oxygen octahedral tilts. The second coupling type has been analyzed in this paper. It is due to the DD interactions between $A$ and oxygen sublattices. Despite being related to the same sublattices, the two coupling types have different effects. Due to symmetry restrictions, short-range coupling is forbidden at the zone center. The Pb and oxygen displacements become mixed only at finite wave vectors. This makes the short-range coupling unlikely to be the sole coupling responsible for the flatness of stiffness, because it is known that these displacements are strongly mixed at the zone center, too [21]. The DD coupling, in contrast, allows that.

### C. Appropriateness of the present model for describing $PbZrO_3$

The DD coupling can be important in shaping the characteristic stiffness dispersion in $PbZrO_3$. This crystal is likely to fulfill the conditions established in this paper. The total polarizability of oxygen sites is expected to be strongly anisotropic, because of weak binding of oxygen in $A$-O planes, as compared to the strong binding in the $B$-O direction [21]. To flatten the stiffness dispersion strongly, the oxygen polarizability should not be too small compared to that of $Pb^{2+}$ sites, which can be estimated from below by the exceptionally large $Pb^{2+}$ electronic polarizability $\alpha_{Pb2+} = 4.9$ $\mathring{A}^3$. The calculations give flattened dispersion for $\alpha_{O-A} \approx 4.4$-$4.5$ $\mathring{A}^3$ and $\alpha_{O-B} \approx 2.5$-$2.9$ $\mathring{A}^3$. $^{2}$ The value of $\alpha_{O-B}$ is within the range of effective $O^{2-}$ electronic polarizabilities reported in Ref. [20] for simple oxides ($0.5$-$3.2$ $\mathring{A}^3$). This value is therefore reasonable: one should expect $\alpha_{O-B}$ to be limited to the electronic polarizability, because oxygen ions are largely forbidden to shift toward $Zr^{4+}$ ions due to tight binding in this direction [21]. The $\alpha_{O-A}$ value is larger than that, which can be logical because of the polarizability enhancement due to weak binding of oxygen in $A$-O planes in $PbZrO_3$. The DD interaction can influence the IC instability to a considerable degree.

### D. The difference between the effects of DD interactions on the stiffness landscapes of $PbZrO_3$ and $PbTiO_3$

The results seem to help rationalize the difference in stiffness dispersions in chemically similar $PbZrO_3$ and $PbTiO_3$ in the cubic phase. In $PbZrO_3$ the stiffness dispersion is more anisotropic, as it is seen in phonon dispersions and diffuse scattering distributions in these crystals [7,24]. These two crystals should differ in the level of anisotropy of the oxygen sites polarizability. $PbZrO_3$ is expected to have larger $\alpha_{O-A}$ and smaller $\alpha_{O-B}$ because of the difference in the ability of oxygen to displace in $A$-O planes and along $B$-O chains. This is supported by first-principles-predicted anisotropy of the relevant self-term force constants of Ghosez *et al.* [21].

$^{2}$The flattened dispersion is obtained with $\alpha_{O-A} = 4.38$ $\mathring{A}^3$, $\alpha_{O-B} = 2.9$ $\mathring{A}^3$ for Fig. 5(b), and $\alpha_{O-A} = 4.52$ $\mathring{A}^3$, $\alpha_{O-B} = 2.47$ $\mathring{A}^3$ for Fig. 5(c).

The effect of DD interactions toward flattening of stiffness along the $\Gamma$-$M$ direction is expected to be weaker in $\text{PbTiO}_3$ than in $\text{PbZrO}_3$.

## V. CONCLUSION

I have shown the condition, in terms of total polarizabilities of perovskite sites, under which the dipole-dipole interactions do favor an anisotropic stiffness dispersion landscape with strongly flattened dispersion along the $\Gamma$-$M$ direction. The condition is that the polarizability of oxygen sites is highly anisotropic, with the component along the $A$-O planes being larger than that along the $B$-O chains, and that the polarizability component in the $A$-O planes is sufficiently large in comparison with the $A$-site polarizability.

By analysis of the wave-vector dispersion of Coulomb coefficients, I have shown the physical reasons behind this condition. The flattened stiffness dispersion can be achieved as the result of a cancellation between the trends toward positive dispersion in the $A$ sublattice and negative dispersion in the oxygen sublattice, when its dipolar response is restricted largely to the $A$-O planes. This restriction is important because when it is removed, the DD energy of the oxygen subsystem stops having strongly negative wave-vector dispersion. These aspects of DD interactions are determined solely by perovskite geometry, and they should be relevant as long as the dipolar state of the crystal can be approximated by a system of point dipoles localized at the high-symmetry positions. This approximation is widely used in atomistic models.

The mechanism of flattening of stiffness dispersion in the $\Gamma$-$M$ direction is likely to be important in $\text{PbZrO}_3$ and similar crystals. On the other hand, the influence of this mechanism on the energetics of $\text{PbTiO}_3$ should be weaker, which can be part of the explanation for the absence of IC ordering in this crystal, in contrast to $\text{PbZrO}_3$.

## ACKNOWLEDGMENTS

The work was supported by the Russian Science Foundation (Grant No. 17-72-20083). The author thanks Alexander Tagantsev for his help in localizing the problem, and Oleg Kvyatkovskii, Sergey Vakhrushev, Alexei Bosak, and Alexei Filimonov for useful discussions.

[1] G. H. Haertling, J. Am. Ceram. Soc. **82**, 797 (1999).
[2] J. Scott, *Science (NY)* **315**, 954 (2007).
[3] X.-K. Wei, A. K. Tagantsev, A. Kvasov, K. Roleder, C.-L. Jia, and N. Setter, *Nat. Commun.* **5**, 3031 (2014).
[4] W. Geng, Y. Liu, X. Meng, L. Bellaiche, J. F. Scott, B. Dkhil, and A. Jiang, *Adv. Mater.* **27**, 3165 (2015).
[5] B. Xu, J. Íñiguez, and L. Bellaiche, *Nat. Commun.* **8**, 15682 (2017).
[6] G. Samara, *Phys. Rev. B* **1**, 3777 (1970).
[7] A. Tagantsev *et al.*, *Nat. Commun.* **4**, 2229 (2013).

## APPENDIX: COULOMB COEFFICIENTS

The Coulomb coefficients are given by [17,18]
$$
C_{k,k',\gamma,\gamma'}(\mathbf{q}) = \frac{4\pi}{v_a} \frac{q_\gamma q_{\gamma'}}{q^2} - Q_{k,k',\gamma,\gamma'}(\mathbf{q}), \tag{A1}
$$
where $q_\gamma$ is the $(\gamma)$ Cartesian component of the reduced wave vector $\mathbf{q}$.

The values $Q_{k,k',\gamma,\gamma'}$ can be evaluated using Ewald's transformation as [18]
$$
\begin{aligned}
&Q_{k,k',\gamma,\gamma'}(\mathbf{q}) \\
&= -\frac{4\pi}{v_a} \frac{q_\gamma q_{\gamma'}}{q^2} \left[ \exp\left(-\frac{q^2}{4Y}\right) - 1 \right] \\
&\quad - \frac{4\pi}{v_a} \sum_{\boldsymbol{\tau} \neq 0} \frac{(\boldsymbol{\tau} + \mathbf{q})_\gamma (\boldsymbol{\tau} + \mathbf{q})_{\gamma'}}{(\boldsymbol{\tau} + \mathbf{q})^2} \\
&\quad \times \exp\left(-\frac{|\boldsymbol{\tau} + \mathbf{q}|^2}{4Y}\right) e^{i\boldsymbol{\tau}[\mathbf{x}(k)-\mathbf{x}(k')]} + Y^{3/2} \\
&\quad \times \sum_{l'} H_{\gamma\gamma'}\left[\sqrt{Y}|\mathbf{x}(lk) - \mathbf{x}(l'k')|\right] e^{-i\mathbf{q}[\mathbf{x}(lk)-\mathbf{x}(l'k')]}, \tag{A2}
\end{aligned}
$$
where $\mathbf{x}(lk)$ is the position of atom $k$ in unit cell $l$, and $\boldsymbol{\tau}$ is the reciprocal space vector. The function $H_{\gamma\gamma'}$ is defined by
$$
\begin{aligned}
H_{\gamma\gamma'}(\mathbf{x}) &= \frac{\partial^2}{\partial x_\gamma \partial x_{\gamma'}} \frac{2}{\sqrt{\pi}} \frac{1}{x} \int_x^\infty \exp(-s^2)ds \\
&= \frac{x_\gamma x_{\gamma'}}{x^2} \left[ \frac{3}{x^3}\text{erfc}(x) + \frac{2}{\sqrt{\pi}} \left( \frac{3}{x^2} + 2 \right) \exp(-x^2) \right] \\
&\quad - \delta_{\gamma\gamma'} \left[ \frac{1}{x^3}\text{erfc}(x) + \frac{2}{\sqrt{\pi}} \frac{1}{x^2}\exp(-x^2) \right], \tag{A3}
\end{aligned}
$$
where $\text{erfc}(x)$ is a complementary error function
$$
\text{erfc}(x) = \frac{2}{\sqrt{\pi}} \int_x^\infty \exp(-s^2)ds \equiv xH(x). \tag{A4}
$$

In Eq. (A2), in the case of $l = l'$ and $k = k'$ the function $H_{\gamma\gamma'}$ is replaced by
$$
H_{\gamma\gamma'}^0(0) = \frac{4}{3\sqrt{\pi}} \delta_{\gamma\gamma'}. \tag{A5}
$$

It has been verified that the summations over the range of $-5$ to $5$ real and reciprocal unit cells in Eq. (A2) with the value of $Y = 1.25 \times 10^{19}\ \text{m}^{-2}$ produce accurate results.

[8] J. Hlinka, T. Ostapchuk, E. Buixaderas, C. Kadlec, P. Kuzel, I. Gregora, J. Kroupa, M. Savinov, A. Klic, J. Drahokoupil *et al.*, *Phys. Rev. Lett.* **112**, 197601 (2014).
[9] J. Íñiguez, M. Stengel, S. Prosandeev, and L. Bellaiche, *Phys. Rev. B* **90**, 220103 (2014).
[10] R. Burkovsky, I. Bronwald, D. Andronikova, B. Wehinger, M. Krisch, J. Jacobs, D. Gambetti, K. Roleder, A. Majchrowski, A. Filimonov *et al.*, *Sci. Rep.* **7**, 41512 (2017).
[11] K. Patel, S. Prosandeev, Y. Yang, B. Xu, J. Íñiguez, and L. Bellaiche, *Phys. Rev. B* **94**, 054107 (2016).

184109-7

[12] P. W. Anderson, in *Conference Proceedings of the Lebedev Physics Institute, Academy of Sciences of the USSR, Nov. 1958* (Fizika Dielektrikov, Moscow, 1960), p. 290.

[13] W. Zhong, R. D. King-Smith, and D. Vanderbilt, *Phys. Rev. Lett.* **72**, 3618 (1994).

[14] J. Slater, *Phys. Rev.* **78**, 748 (1950).

[15] A. Hüller, *Z. Phys.* **220**, 145 (1969).

[16] R. Cowley, *Phys. Rev.* **134**, A981 (1964).

[17] M. Born and K. Huang, *Dynamical Theory of Crystal Lattices* (Clarendon, Oxford, 1988).

[18] A. A. Maradudin, E. W. Montroll, G. H. Weiss, and I. Ipatova, *Theory of Lattice Dynamics in the Harmonic Approximation* (Academic, New York, 1963), Vol. 12.

[19] E. Farhi, A. K. Tagantsev, R. Currat, B. Hehlen, E. Courtens, and L. A. Boatner, *Eur. Phys. J. B* **15**, 615 (2000).

[20] J. R. Tessman, A. Kahn, and W. Shockley, *Phys. Rev.* **92**, 890 (1953).

[21] P. Ghosez, E. Cockayne, U. V. Waghmare, and K. M. Rabe, *Phys. Rev. B* **60**, 836 (1999).

[22] A. Bussmann, H. Bilz, R. Roenspiess, and K. Schwarz, *Ferroelectrics* **25**, 343 (1980).

[23] R. G. Burkovsky, D. Andronikova, Y. Bronwald, M. Krisch, K. Roleder, A. Majchrowski, A. V. Filimonov, A. I. Rudskoy, and S. B. Vakhrushev, *J. Phys.: Condens. Matter* **27**, 335901 (2015).

[24] B. D. Chapman, E. A. Stern, S.-W. Han, J. O. Cross, G. T. Seidler, V. Gavrilyatchenko, R. V. Vedrinskii, and V. L. Kraizman, *Phys. Rev. B* **71**, 020102(R) (2005).