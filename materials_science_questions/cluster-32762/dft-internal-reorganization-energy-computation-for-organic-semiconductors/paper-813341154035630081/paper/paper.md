# Constrained Density Functional Theory of Molecular Dimers

J.-H. Franke, N.N. Nair, L. Chi, and H. Fuchs

**Abstract** For charge transport in organic semiconductors the geometrical response to the presence of the charge plays a crucial role. Often, charge transport in these materials can be considered as the hopping of a localized polaron. Unfortunately, the description of localized charge carriers within semilocal Density Functional Theory (DFT) is prevented by the self-interaction error that artificially delocalizes the charge. Here, we present a computational scheme for the description of localized charges in an organic semiconductor. Constrained DFT is used to localize the charge on one of the molecules of a molecular dimer. The availability of the forces from this constraint enables ab initio molecular dynamics calculations and gives access to the geometrical response of neighboring molecules to the presence of a charged neighbor. This is demonstrated for a pentacene dimer. The reorganization energy is found to increase from 91 meV to 108 meV when decreasing the distance between two Pentacene molecules from 7 Å to 4 Å.

## 1 Introduction

We study here the charge hopping process between two charge states of a molecular dimer. This process can be considered as the elementary charge transport step in the thermally activated hopping regime of strongly localized polarons in small molecule organic semiconductors. It is thus of tremendous interest for research into higher performance organic semiconductors.

To be able to describe the charge transfer process it is first necessary to localize a charge on one molecule. To this end we implement a constrained DFT (CDFT)

---

J.-H. Franke · L. Chi · H. Fuchs
Physikalisches Institut, WWU Münster, Wilhelm-Klemm-Str. 10, 48149 Münster, Germany,
e-mail: frankejo@uni-muenster.de

N.N. Nair
Department of Chemistry, IIT Kanpur, Uttar Pradesh 208016, India

W.E. Nagel et al. (eds.), *High Performance Computing in Science and Engineering '11*, DOI 10.1007/978-3-642-23869-7_14,
© Springer-Verlag Berlin Heidelberg 2012

approach into the CPMD code supporting ultrasoft pseudopotentials. Different defi- nitions of what constitutes a charge on a molecule are tested and found to be able to produce correct charge states. To access the geometrical response of the molecules to the charge state and sample the thermodynamic properties it is further necessary to implement the ionic forces resulting from the charge constraint. The presented methodology is finally used to calculate the reorganization energy of an isolated molecule-positive ion Pentacene dimer as a function of intermolecular distance.

In the following sections the constrained DFT approach is first outlined, then applied to Benzene and Pentacene dimers. The focus on the Benzene calculations is to establish the validity of the electronic structure optimization and to check if the method is able to prepare an isolated ion—neutral molecule electronic structure. The focus of the Pentacene calculations is on the geometry-electronic structure rela- tionship. Here, also structural relaxations of the dimer via simulated annealing and energy conservation of a Born-Oppenheimer molecular dynamics run are demon- strated.

## 2 Constrained DFT Methodology

To realistically describe systems containing strongly localized charges like small po- larons, it is a prerequisite to localize the charge. If this is achieved in a proper way, a meaningful description of electronic polarization and structural relaxation response in the surrounding medium due to the presence of a charged molecule based on ab initio methods becomes possible. Combining this with molecular dynamics, also dynamical quantities can be studied and eventually even charge hopping rates could be calculated.

The inherent self-interaction error in widely used semilocal exchange-correlation functionals artificially delocalizes the charge density of a molecular ion over many molecules [3, 10–12, 16, 24]. This stems from the convexity of the energy curve as a function of fractional electron number, making a fractional electron occupation of isolated fragments energetically more favorable than integer occupations. In exact DFT this energy curve is a linear function with its slope given by the ionization en- ergy or electron affinity [14].¹ The artificial delocalization of charges makes current semi-local exchange-correlation functionals ill suited to the description of strongly localized charges in small polarons.

Apart from constructing self-interaction-free density functionals, a straightfor- ward way to overcome this limitation is to put a constraint on the charge of the molecules [2, 4, 13, 15, 19–23]. This implies the need to define a measure for the charge residing on one molecule, which is basically a partitioning problem of the spatially delocalized charge into regions in space defined to belong to a cer-

¹ The energy of an additional charge distributed over two identical entities in exact DFT is thus invariant towards its distribution on the two units, consistent with the ensemble interpretation of fractional electron numbers. If the molecular geometries differ, the charge would become correctly localized.

tain molecule. The arbitrariness of this definition is evident from the many different partitioning schemes suggested in the framework of constrained DFT, the most prominent probably being Mulliken and Löwdin population analyses [17] as well as Hirshfeld [8] or Becke [1] real space weight-function based charges [2, 13, 21, 22].

In general, different charge partitioning schemes can be defined via a projection operator $\hat{P}_{i j}$. With the KS-states $|\Psi_{n}\rangle$ and occupation numbers $f_{n}$ this operator defines an occupation matrix $N_{i j}$

$$
N_{i j}=\sum_{n} f_{n}\left\langle\Psi_{n}\left|\hat{P}_{i j}\right| \Psi_{n}\right\rangle. \tag{1}
$$

The charges of parts of the system $A$, e.g. orbitals, atoms or molecules, can be obtained as the partial trace of the occupation matrix

$$
n^{A}=\sum_{i \in A} N_{i i}. \tag{2}
$$

The projection operator can take different forms, for example it can be a weighting function in real space like in the work of Dederichs et al. [4] or in the Hirshfeld scheme [13]

$$
\left\langle\mathbf{r}^{\prime}\left|\hat{P}_{i j}^{\mathrm{Hirsh}}\right| \mathbf{r}\right\rangle=\frac{n_{\mathrm{iso}}^{i}(\mathbf{r})}{\sum_{l} n_{\mathrm{iso}}^{l}(\mathbf{r})} \delta\left(\mathbf{r}-\mathbf{r}^{\prime}\right) \delta_{i j} \tag{3}
$$

where $n_{\text {iso }}^{i}(\mathbf{r})$ denotes the electron density of an isolated (promolecular) atom. The projection operators for Mulliken, Löwdin and dual charges are

$$
\hat{P}_{i j}^{\text {Mull }}=\left|\phi_{i}\right\rangle\left\langle\phi_{j}\right|, \tag{4}
$$

$$
\hat{P}_{i j}^{\text {Loew }}=U^{-1 / 2}\left|\phi_{i}\right\rangle\left\langle\phi_{j}\right| U^{-1 / 2}, \tag{5}
$$

$$
\hat{P}_{i j}^{\text {Dual }}=\frac{1}{2}\left(\left|\tilde{\phi}_{i}\right\rangle\left\langle\phi_{j}|+| \phi_{j}\right\rangle\left\langle\tilde{\phi}_{i}\right|\right) \tag{6}
$$

where $\left|\phi_{i}\right\rangle$ denotes the non-orthogonal local projectors and $\left|\tilde{\phi}_{i}\right\rangle=\sum_{j} U_{i j}^{-1}\left|\phi_{j}\right\rangle$ the orthogonal ones $(U_{i j}=\langle\phi_{i}|\phi_{j}\rangle)$. Here the projectors are simply taken as the pseudo wave functions of the pseudopotentials used.

In our case we have a rather well-defined situation we have to reproduce with the constrained DFT calculations. We know the ionic state and the neutral state of the isolated molecule, and the constraint DFT should naturally produce a neutral molecule and an ion. The arbitrariness in the definition of the charges is thus to be eliminated by comparing the produced molecular states to the isolated molecular states. The constraint needs to be formulated in such a way that these states are most closely reproduced. A margin of error is however introduced by the unknown magnitude of polarization effects on the neighboring molecule.

We implemented the Hirshfeld charge constraint and the Dual [7] as well as the Löwdin orbital projection schemes. The Hirshfeld scheme is complete in the sense of partial charges adding up to the total charge of the system. For the orbital projection scheme this depends on the completeness of the projector set. As we project on the atomic pseudo-orbitals, yet expand the Kohn-Sham wave functions in a plane

wave basis, the projection remains incomplete and absolute numbers of the charges should be taken with a grain of salt. The beauty of the orbital projection schemes (Mulliken, Löwdin and Dual) lies in their simplicity as all quantities can be straightforwardly evaluated in reciprocal space and are thus well parallelized in CPMD.² For the Hirshfeld charges the regions with small electron densities produce numerical instabilities in the derivative of the weighting function needed for the ionic forces that necessitate a real space cutoff. Although this problem can be solved [13], it still requires additional effort that is not needed in the projection schemes. Also, the evaluation of the forces requires additional 3-dimensional Fourier transforms which constitutes a serious bottleneck in massively parallel calculations. Also the implementation in conjunction with ultrasoft pseudopotentials is more involved then in the case of the projection schemes. Therefore, ultrasoft pseudopotentials and ionic forces are not implemented for the Hirshfeld charge constraint and the results presented here for this constraint scheme are limited to norm-conserving pseudopotentials and static electronic-self-consistency calculations. The Dual and Löwdin orbital projection schemes are implemented in CPMD including support for ultrasoft pseudopotentials. The Löwdin projection scheme implementation also comprises ionic forces.

Using ultrasoft pseudopotentials, the occupation matrix for the projection operator becomes

$$
N_{i j}=\sum_{n} f_{n}\left\langle\Psi_{n} \hat{S}\left|\hat{P}_{i j}\right| \hat{S} \Psi_{n}\right\rangle \tag{7}
$$

with $\hat{S}$ being the $\hat{S}$-operator of ultrasoft pseudopotentials.

The charge difference between the charge on the donor and acceptor molecules can now be constrained to a given value $N_{c}$ as

$$
\left(n^{A}-\sum_{I \in A} Z_{I}\right)-\left(n^{D}-\sum_{I \in D} Z_{I}\right)=N_{c} \tag{8}
$$

with the $Z_{I}$ denoting the core charges of the pseudopotentials. Under this constraint the DFT functional to minimize becomes

$$
E_{\mathrm{CDFT}}[n]=E_{\mathrm{DFT}}[n]+V_{c}\left(\left(n^{A}-\sum_{I \in A} Z_{I}\right)-\left(n^{D}-\sum_{I \in D} Z_{I}\right)-N_{c}\right) \tag{9}
$$

with the Lagrange multiplier $V_{c}$. In practice, the minimization is performed by optimizing the wave functions for a given $V_{c}$, then calculating the $N_{c}$ from these wave functions and predicting a new $V_{c}$ from the error in $N_{c}$. Thus, the optimization of the charge constraint is done in an outer loop around the electronic self-consistency loop.

---
² In fact, the additional overhead in the projection schemes scales linearly to at least 128 cores. This test was done on the NEC Nehalem cluster of HLRS that boasts 8 cores per node and Infiniband interconnect.

For the calculation of the self-consistent wave functions an additional term in the wave function forces appears due to the constraint:

$$
\begin{align}
\frac{\delta E_{\mathrm{CDFT}}}{\delta\langle\Psi_n|} &= \frac{\delta E_{\mathrm{DFT}}}{\delta\langle\Psi_n|} + V_c\left(\frac{\delta n^A}{\delta\langle\Psi_n|} - \frac{\delta n^D}{\delta\langle\Psi_n|}\right) \tag{10} \\
&= \frac{\delta E_{\mathrm{DFT}}}{\delta\langle\Psi_n|} + V_c \sum_{i\in D,A} \sigma_i \hat{S} \hat{P}_{ii} \hat{S}|\Psi_n\rangle. \tag{11}
\end{align}
$$

The function $\sigma_i$ is hereby defined as being 1 for $i \in A$ and $-1$ for $i \in D$. The additional forces on the ions due to the constraint are

$$
\frac{\partial E_{\mathrm{CDFT}}}{\partial R_I} = \frac{\partial E_{\mathrm{DFT}}}{\partial R_I} + V_c\left(\frac{\partial n^A}{\partial R_I} - \frac{\partial n^D}{\partial R_I}\right). \tag{12}
$$

The evaluation of the ionic forces is much more involved as many terms depend on the ionic positions. For the Löwdin projection scheme this becomes

$$
\begin{align}
\frac{\partial n^A}{\partial R_I} &= \sum_n \sum_{i\in A} f_n \frac{\partial}{\partial R_I} \langle \tilde{\phi}_i | \hat{S} | \Psi_n \rangle^2 \tag{13} \\
&= 2 \sum_n \sum_{i\in A} f_n \langle \tilde{\phi}_i | \hat{S} | \Psi_n \rangle \left( \langle \Psi_n | \frac{\partial \hat{S}}{\partial R_I} | \tilde{\phi}_i \rangle + \langle \Psi_n | \hat{S} \frac{\partial}{\partial R_I} | \tilde{\phi}_i \rangle \right) \tag{14}
\end{align}
$$

with

$$
\frac{\partial}{\partial R_I} | \tilde{\phi}_i \rangle = \sum_l | \phi_l \rangle \frac{\partial}{\partial R_I} U_{il}^{-1/2} + U_{il}^{-1/2} \frac{\partial}{\partial R_I} | \phi_l \rangle. \tag{15}
$$

While the evaluation of the $\partial \hat{S}/\partial R_I$ and $\partial |\phi_i\rangle/\partial R_I$ terms is straightforward, the derivative involving the matrix $U_{il}^{-1/2}$ is more complicated. Nevertheless it can be calculated by first diagonalizing the overlap matrix $U_{il} = \langle \phi_i | \phi_l \rangle$ [9]:

$$
U D_i = u_i D_i \tag{16}
$$

and then evaluating the derivative in the orthogonal basis of the eigenvectors $D_i$ (which constitute the rows of the matrix $D_{ij}$) as

$$
\left( \frac{\partial U^{-1/2}}{\partial R_I} \right)_{mn} = -\left( \frac{\partial U}{\partial R_I} \right)_{mn} \frac{u_m^{-1/2} u_n^{-1/2}}{u_m^{-1/2} + u_n^{-1/2}}. \tag{17}
$$

The derivative of the matrix in its non-orthogonal basis is then obtained through back-transformation via

$$
\left( \frac{\partial U^{-1/2}}{\partial R_I} \right)_{il} = \sum_{m,n} D_{mi} \left( \frac{\partial U^{-1/2}}{\partial R_I} \right)_{mn} D_{nl}. \tag{18}
$$

The ionic forces are only implemented for this Löwdin charge constraint.

## 3 CDFT on the Benzene Dimer

Calculations using different target values of the charge difference $N_c$ yield different Lagrange multipliers. Integrating these along the coordinate of charge difference should yield the energy difference between the different charge states. The mutual consistency of the Lagrange multiplier and the energy can be considered as a self-consistency check of the numerical implementation of the constrained DFT. The process of localizing a charge on one constituent of a dimer system can be understood as a combination of adding charge on one and removing the same amount from the other unit. In exact DFT, changing the charge amount in an isolated system, i.e. one part of the dimer, changes the total energy proportional to the ionization energy or electron affinity, depending on the overall charge of the system [15]. Since, due to the constraint, one constituent of the dimer gains the charge that is lost on the other, the net effect on the energy should vanish in exact DFT. The finite Lagrange multipliers are thus a direct consequence of the self-interaction error present in the PBE functional used here. A parabolic energy contribution as a function of fractional electron number can be expected for the Hartree contribution of the self-energy, under the additional assumption of fixed shape of all orbitals. The Lagrange multiplier of the constraint needed to change the occupation number of one orbital should be linear in the fractional electron number.

At this stage a simpler system, the Benzene dimer, is used for testing. For this system data from self-interaction corrections and restricted open-shell Hartree-Fock calculations are readily available [10]. Stacking the Benzene molecules in its neutral geometry at varying distances, the charge difference is constrained to different values $N_c$. Importantly, the two molecules considered have the same geometry and therefore only absolute charge differences between the two molecules need to be considered. The overall system contains one positive elementary charge. For these tests the Dual projection scheme and the PBE density functional were used. The resulting Lagrange multiplier $V_c$ is plotted against $N_c$ in Fig. 1a. A linear relationship is found for a molecule-molecule distance of $7\mathrm{\AA}$. The mutual consistency of the different charge projection schemes is highlighted by the almost identical Mulliken and Löwdin charges calculated for these wave functions. The corresponding energies are plotted in Fig. 1b, together with the energies predicted from the linear fit of Fig. 1a. Here, the excellent agreement gives evidence of the numerical self-consistency of the code.

To further elucidate the validity of the constraint scheme it is instructive to look at the magnetization density of the Benzene dimer. The single hole on the dimer should produce a magnetization density that corresponds to the HOMO at the ion while vanishing at the neutral molecule for the quasi isolated molecules, i.e. the $7\mathrm{\AA}$ dimer. In Fig. 2 one can see that in the unconstrained case the magnetization density is completely delocalized over the dimer. Constraining the charge difference to higher values then increasingly concentrates the charge on one molecule, with finally vanishing magnetization density at the other. The charge difference value $N_c$ at which this occurs, is larger then 1.0 for the Dual charge constraint. Nevertheless, the magnetization density at a charge difference of 1.3 resembles the sought-for

![](./images/813341154035630081_1.jpg)

Fig. 1 Constrained DFT using the Dual constraint scheme on the Benzene dimer with one positive charge. a Lagrange multiplier $V_c$ plotted against the charge difference between the two molecules $N_c$ with molecules $7$ Å apart. The relationship is linear which can be seen by the linear fit. Mulliken and Löwdin population analysis schemes are tested on the converged wave functions and give almost identical charge differences. b The energies obtained for the Benzene dimer at $7$ Å as a function of the charge difference between the two molecules. The parabolic behavior is evident from the coincidence of the energies calculated as the integral of the fit function from (a) with the actual energies obtained during the calculations. c $V_c$-$N_c$-plots obtained for different intermolecular distances. At smaller distances the initial slope of the curve is smaller then in the $7$ Å distance case, i.e. the $V_c$ values are smaller for small $N_c$. At higher $N_c$ and smaller distances aberrations from linear behavior appear. d Energies for Benzene dimers at different distances as a function of $N_c$. The total energy decreases with increasing distance. Secondly, the parabolas at smaller distances are less steep then for the isolated case. e and f Lagrange multipliers and energies at high $N_c$ of the Dual projection and Hirshfeld schemes. Nonlinearities occur for $N_c$ values of 1.3 and 1.0 in the Lagrange multiplier. The energies at the respective values are parabolic, up to the nonlinearity in the Lagrange multiplier, yet differ drastically at even higher values

magnetization density of the isolated ion and the neutral molecule closely. For comparison, the results for a Hirshfeld charge constraint are also given. Here, the charge is completely localized at a charge difference of 1.0 already for the $7$ Å dimer.

![](./images/813341154035630081_2.jpg)

Fig. 2 Spin density isosurfaces (isovalue $m=0.002$) of the Benzene dimer with different constraints at the intermolecular distance of $7\ \mathring{A}$. In this well separated limit, the spin density should be limited to one molecule only. The spin density of an isolated positive ion is given at the right of the figure. The unconstrained dimer shows the complete delocalization of the single unpaired electron into the two molecular HOMOs. Switching on the constraint leads to localization of the spin density. At a charge difference $N_c$ of 0.9, the Dual and the Hirshfeld charge constraint both yield the same spin density, which corresponds almost to the isolated ion, with some residual occupation still on the other molecule. At $N_c=1.0$ the Hirshfeld constraint yields basically the correct ion-neutral system, while the Dual constraint charge transfer is still incomplete. However, the dual constraint also generates the correct ion, albeit only at the larger $N_c$ value of 1.2. Constraining the Hirshfeld charges to this value leads to additional charge transfer, probably tending towards the negative plus double positive ionic state. The $3\ \mathring{A}$ dimer shown on the right exhibits basically the same pattern albeit the charge localization occurs at higher $N_c$ values

Comparing the total energy of the constrained dimer ($7\ \mathring{A}$ case) to the sum of energies of the neutral molecule plus that of the ion gives further insight into the validity of the scheme presented. Without constraint, the energy of the dimer at $7\ \mathring{A}$ is about 1 eV smaller then the sum of the single constituent energies. This energy difference is reduced with increasing charge difference, following the parabolic energy curves. At a charge difference $N_c=1.0$, it is still smaller by 315 meV and 47 meV for Dual and Hirshfeld charge constraints, respectively. However, it is difficult to quantify effects on the total energy of the polarization response of the neutral molecule to the presence of the charged molecule. This will lower the total energy, bringing the real, physical energy of the dimer closer to the calculated ones. The crossing point of the energy parabola with the expected energy value is very slightly larger then $N_c=1.0$ in the Hirshfeld scheme and around $N_c=1.2$ for the Dual pro-

jection scheme, corresponding quite well to the $N_c$ values where the magnetization density becomes completely localized on one molecule.

Plotting the $V_c$-$N_c$ behavior for $N_c$ values up to 1.3 for the 7 Å dimer, aberrations from linearity are observed. In the Hirshfeld constraint scheme, the aberrations take the form of a sudden jump in the Lagrange multiplier at $N_c = 1.0$, while in the Dual projection scheme this jump occurs at higher charge differences and is much smaller. In fact, for the 7 Å dimer this discontinuity in the Lagrange multiplier occurs very close to the charge differences of $N_c = 1.0$ and $N_c = 1.2$ for which the total energy and spin density indicate the preparation of an isolated ion-neutral molecule com- plex. Considering again the gradual transfer of electrons from one molecule to the other with increasing charge differences as adding infinite amounts of charge to one molecule and withdrawing the same amount from the other, one can immediately see the origin of this discontinuity. In exact DFT this jump would correspond to the sum of two derivative discontinuities of the energy with respect to fractional elec- tron numbers: one as the ion passes from the single to double positive ionic state and one from the neutral-negative ionic state transition. In the semilocal PBE functional this discontinuity is underestimated as only the discontinuity in the kinetic energy is present. However there is still a jump at crossings of integer electron numbers.

$V_c$-$N_c$ plots at different dimer distances (Fig. 1c) show that the slope of the curve is different from the 7 Å case and also the aberrations from linearity occur at smaller charge differences. Localization of spin density occurs at larger charge differences, see Fig. 2. Note that in Hartree-Fock theory the spin density of the 3 Å dimer is not fully localized on one molecule [10] and the complete charge localization might thus be unphysical here as Hartree-Fock should overlcalize fractional charges [11]. In conclusion, one can say that the calculations discussed above show that the elec- tronic structure of the ion-neutral molecule dimer can be prepared by our charge constrained DFT implementation.

## 4 CDFT on the Pentacene Dimer

The next point is to study the influence of the geometrical structure and check if our method gives the correct reorganization energy of an isolated molecular dimer. For this purpose the DFT-D method using the PBE functional is chosen in conjunction with the Löwdin charge constraint as this is the only constraint scheme with im- plementation of the ionic forces. All calculations presented below were done using ultrasoft pseudopotentials. Occasional cross-checking with norm-conserving pseu- dopotentials of the Troullier-Martins type gave identical results.

First, the inner reorganization energy of Pentacene is evaluated using the "4- point-method" [5, 18]. It is calculated as the sum of the two contributions of distort- ing the neutral molecule to its charged geometry and distorting the ion to its neutral geometry. These quantities are directly accessible through isolated molecule calcu- lations. Calculating the energies of charged or neutral isolated molecules ($E^+$ and $E^0$) in their charged or neutral geometries ($\mathbf{R}_N^+$ and $\mathbf{R}_N^0$) gives for the reorganization

energy

$$
\lambda=E^{+}(\left\{\mathbf{R}_{\mathbf{N}}^{\mathbf{0}}\right\})-E^{+}(\left\{\mathbf{R}_{\mathbf{N}}^{+}\right\})+E^{0}(\left\{\mathbf{R}_{\mathbf{N}}^{+}\right\})-E^{0}(\left\{\mathbf{R}_{\mathbf{N}}^{\mathbf{0}}\right\}). \tag{19}
$$

Since there are only energy differences involved, contributions of possible interaction energies of a neutralizing background charge in periodic calculations cancel out.

The above mentioned quantity was calculated using CPMD at the PBE-D level of theory and carefully converging the energy cutoffs of the plane wave basis set and unit cell size. Also the BLYP functional in conjunction with semiempirical dispersion corrections (BLYP-D) was tested. All values obtained are in very good agreement with each other as the CPMD calculations yield values of 62.4 meV and 65.6 meV for PBE-D and BLYP-D, respectively. Markedly, this is in contrast to the reorganization energy reported in the literature using the hybrid B3LYP functional of 98 meV [6]. The difference is here attributed to the semilocality of the functionals used as technical effects of pseudopotentials, incomplete basis set or spurious interactions due to small supercells can be excluded.

In the next step, a Pentacene dimer was constructed from the relaxed ionic and neutral geometries. $V_c$-$N_c$ and $E$-$N_c$ plots for dimer distances of $4\,\text{\AA}$, $5\,\text{\AA}$ and $7\,\text{\AA}$ are given is Fig. 3a, b. They are similar to the ones obtained for Benzene before, but here the dimer is made up of the neutral and ionic geometries. Positive charge differences hereby correspond to the positive charge being more on the Pentacene in its ionic geometry. As a consequence of the geometrical differences of the molecules, the charge is more easily accommodated by the ionic Pentacene, thus giving a charge difference of 0.04e for the unconstrained $7\,\text{\AA}$ dimer already. This translates to a y-axis intercept (point of vanishing charge difference) of the Lagrange multipliers at negative values. Since the $V_c$-$N_c$ curves are linear for all dimers, the $E$-$N_c$ curves which correspond to the integral of this function form parabolas with minima at the unconstrained charge differences. The energy differences between energies obtained for positive and negative charge differences

$$
\Delta E(N_c)=E(-N_c)-E(N_c) \tag{20}
$$

can be interpreted as the reorganization energy at a given charge difference. This quantity is plotted in Fig. 3c. As expected from the parabolic behavior of the $E$-$N_c$ plots this energy difference is linear in the charge differences. Its intercept with the reorganization energy of isolated molecules gives the charge difference at which the ionic state should be reached when interpreting the $7\,\text{\AA}$ dimer as isolated molecules. Again, this can be compared to the charge differences at which the spin density is localized on the ion (Fig. 4) and the location of the jump in the Lagrange multiplier of Fig. 3a. The result is that the ionic-neutral dimer is obtained at a Löwdin charge difference of 1.3e. The mutual consistency of the different indicators shows that the physical electronic state is obtained at this charge difference. Interestingly, the situation is very similar for the smaller dimer distances of $4\,\text{\AA}$ and $5\,\text{\AA}$.

The forces acting on the ions show that the molecules are not in their respective ground state at this charge difference. The forces are largest for the dimer with the smallest intermolecular distance. To get insight into the molecular relaxation

![](./images/813341154035630081_3.jpg)

Fig. 3 Constrained DFT using the Löwdin constraint scheme with ultrasoft pseudopotentials tested on the cofacially stacked Pentacene dimer. One molecule is in the frozen ionic geometry, the other in the neutral one with positive charge differences corresponding to more charge on the ion. a Lagrange multiplier $V_c$ plotted against the charge difference $N_c$ with molecules at different distances. The relationship is linear up to charge differences of 1.2e for the $5\mathring{A}$ and $7\mathring{A}$ dimers. It jumps for $N_c=1.3$e in these cases and shows increasing slope already for smaller $N_c$ values for the $4\mathring{A}$ dimer. b The energies obtained for the Pentacene dimers as a function of the charge difference between the two molecules. The parabolas are slightly offset along the x-axis by the finite positive charge difference observed already in the unconstrained electronic state. c The energy differences (20) as a function of $N_c$. The plots are linear and almost identical. The isolated molecule reorganization energy is reached at a charge difference of $N_c=1.3$e d NVE ensemble trajectory of the $7\mathring{A}$ Pentacene dimer at a charge difference of $N_c=1.3$e. Shown are the Kohn-Sham energy and the sum of Kohn-Sham and kinetic energy that should be conserved throughout the run. The system temperature is initialized as 300 K and the conserved energy does not exhibit any significant drift and fluctuates by about $2\times10^{-3}$ Hartree

pattern in the presence of the other molecule, the structure is relaxed by simulated annealing Born-Oppenheimer molecular dynamics. In these runs, 6 carbon atoms are constrained to move along the axis connecting the two molecules, i.e. they are constrained to fix the intermolecular distance. The fixed atoms are at both ends and in the middle of the molecule. The two middle atoms are also constrained along the other coordinates, so that slipping motion and in-plane rotations do not occur. To test the accuracy of the constraint contribution to the ionic forces and the other molecular dynamics parameters (timestep of 40 a.u., convergence of the wave function gradients to $<10^{-6}$ a.u., charge difference constraint converged to $<10^{-5}$e), a trajectory of the Pentacene dimer at a charge difference of 1.3e is generated. Figure 3d shows the fluctuations of the Kohn-Sham energy and the conserved energy. It is evident that no significant drift occurs in the conserved energy and its fluctuations are also reasonable. After extensive optimization of the molecular dynamics scheme

![](./images/813341154035630081_4.jpg)

Fig. 4 Spin density isosurfaces (isovalue m = 0.002) of the Pentacene dimer with the Löwdin and Hirshfeld constraints at varying intermolecular distances. The spin density is completely localized on the molecule in the ionic geometry (the left one) for $N_c=1.3$e and on the molecule in the neutral geometry at $N_c=-1.3$e for the Löwdin constraint. The Hirshfeld constraint localizes the spin density already at $N_c=1.0$e. All spin density isosurfaces correspond well to the spin density of the isolated molecule shown on the right

involving a second order Lagrange polynomial prediction of the Lagrange multiplier [13] at the new timestep and occasional memory resets of the preconditioned con- jugate gradient minimizer, the generation of this trajectory of 160 fs still cost one day of wallclock time on 64 cores. In conclusion, it is proved that our constrained DFT approach is able to generate trajectories of physically correct charge localized systems.

The relaxation of the three dimers showed significant additional relaxations for all distances. Relaxation was carried out by simulated annealing subject to the above mentioned constraints and the forces were converged to maximum gradients of $10^{-4}$ a.u.. The energy of the electronic state with charge on the former neutral molecule, i.e. $E(-N_c)$ was then calculated at the relaxed geometry, giving the reorganization energy via (20). The results (see Table 1) show a significant increase of the reorga- nization energy already for the dimer with $7$ Å intermolecular distance to 0.00336 Hartree (91 meV). The reorganization energy is even larger for the smaller distances

Table 1 Reorganization energies of Pentacene dimers at $N_c=1.3$e with varying distances calculated from (20). The second column contains the results for the geometry frozen in its isolated molecule—is ion configuration and the third the values obtained when relaxing the geometry self-consistently. In these relaxations the intermolecular distances are fixed by the constraints mentioned in the text

<table>
<thead>
<tr>
<th>Intermolecular distance</th>
<th colspan="2">Reorganization energy</th>
</tr>
<tr>
<th></th>
<th>isolated configuration</th>
<th>relaxed configuration</th>
</tr>
</thead>
<tbody>
<tr>
<td>7 Å</td>
<td>0.00231 a.u.</td>
<td>0.00336 a.u.</td>
</tr>
<tr>
<td>5 Å</td>
<td>0.00231 a.u.</td>
<td>0.00359 a.u.</td>
</tr>
<tr>
<td>4 Å</td>
<td>0.00227 a.u.</td>
<td>0.00398 a.u.</td>
</tr>
</tbody>
</table>

(0.00359 a.u. and 0.00398 a.u. corresponding to 98 meV and 108 meV). The fact that the reorganization energy at frozen isolated molecule—is ion configurations is similar for all distances (cf. Fig. 3c) points to the mutual cancellation of electronic polarization energies in these cases, i.e. the polarization energies of charge states $N_c$ and $-N_c$ cancel out. This leads to reorganization energies independent of molecular distance. However, the polarization becomes important for the relaxations of the molecules, increasing the reorganization energy with decreasing distance. Since the electrostatic interactions are long ranged, they are also important already for the 7 Å configuration.

This result gives evidence of the importance of the surrounding medium for the calculation of reorganization energies. The surrounding molecules contribute significantly to the overall reorganization energy. Since the reorganization energy enters the rate constant of Marcus theory in the exponential, these effects are highly significant.

## 5 Outlook

Through the CDFT based molecular dynamics not only the electronic and structural response of the surrounding medium to the presence of a charged molecule is accessible, but also the fact that the electronic structure is available on-the-fly can be used. The final quantity of interest, the charge carrier mobility, can be obtained from charge hopping rates between nearest neighbors. These, in turn, can be calculated from the electronic structure of the molecules via the Tully surface hopping probability to the electronic state where the charge resides on the formerly neutral molecule. The hopping probability follows the geometrical configurations directly and an ensemble average could be obtained from a trajectory of adequate length. Moreover, the fact that the charge states are ground states of the constrained system means that this technique is based on the solid ground of applicability of DFT, not using virtual states.

Acknowledgments. The simulations were performed on the national supercomputer NEC Ne-halem Cluster at the High Performance Computing Center Stuttgart (HLRS) under the grant num-

ber AIMDPOLH/12841. The authors especially thank Dominik Marx for instrumental discussions concerning this project.

## References

1. Becke, A.D.: A multicenter numerical integration scheme for polyatomic molecules. The Journal of Chemical Physics **88**, 2547–2553 (1988). DOI 10.1063/1.454033. http://link.aip.org/link/?JCP/88/2547/1

2. Behler, J., Delley, B., Reuter, K., Scheffler, M.: Nonadiabatic potential-energy sur- faces by constrained density-functional theory. Physical Review B **75**, 115,409 (2007). http://link.aps.org/doi/10.1103/PhysRevB.75.115409

3. Cohen, A.J., Mori-Sanchez, P., Yang, W.: Insights into current limitations of den- sity functional theory. Science **321**, 792–794 (2008). DOI 10.1126/science.1158722. http://www.sciencemag.org/cgi/content/abstract/321/5890/792

4. Dederichs, P.H., Blügel, S., Zeller, R., Akai, H.: Ground states of constrained sys- tems: Application to cerium impurities. Physical Review Letters **53**, 2512–2515 (1984). http://link.aps.org/doi/10.1103/PhysRevLett.53.2512

5. Deng, W.Q., Goddard III, W.A.: Predictions of hole mobilities in oligoacene organic semi- conductors from quantum mechanical calculations. The Journal of Physical Chemistry B **108**, 8614–8621 (2004). http://dx.doi.org/10.1021/jp0495848

6. Gruhn, N.E., da Silva Filho, D.A., Bill, T.G., Malagoli, M., Coropceanu, V., Kahn, A., Bredas, J.L.: The vibrational reorganization energy in pentacene: Molecular influences on charge transport. Journal of the American Chemical Society **124**, 7918–7919 (2002). http://dx.doi.org/10.1021/ja0175892

7. Han, M.J., Ozaki, T., Yu, J.: O (N) LDA+U electronic structure calculation method based on the nonorthogonal pseudoatomic orbital basis. Physical Review B **73**, 045110 (2006). http://link.aps.org/doi/10.1103/PhysRevB.73.045110

8. Hirshfeld, F.L.: Bonded-atom fragments for describing molecular charge densities. Theoreti- cal Chemistry Accounts: Theory, Computation, and Modeling (Theoretica Chimica Acta) **44**, 129–138 (1977). http://dx.doi.org/10.1007/BF00549096

9. Jorgensen, P., Simons, J.: Ab initio analytical molecular gradients and Hessians. The Journal of Chemical Physics **79**, 334–357 (1983). DOI 10.1063/1.445528. http://link.aip.org/link/?JCP/79/334/1

10. Mantz, Y.A., Gervasio, F.L., Laino, T., Parrinello, M.: Charge localization in stacked rad- ical cation DNA base pairs and the benzene dimer studied by self-interaction corrected density-functional theory. The Journal of Physical Chemistry A **111**, 105–112 (2007). http://dx.doi.org/10.1021/jp063080n

11. Mori-Sanchez, P., Cohen, A.J., Yang, W.: Many-electron self-interaction error in ap- proximate density functionals. The Journal of Chemical Physics **125**, 201102 (2006). DOI 10.1063/1.2403848. http://link.aip.org/link/?JCP/125/201102/1

12. Mori-Sanchez, P., Cohen, A.J., Yang, W.: Localization and delocalization errors in density functional theory and implications for band-gap prediction. Physical Review Letters **100**, 146,401 (2008). http://link.aps.org/doi/10.1103/PhysRevLett.100.146401

13. Oberhofer, H., Blumberger, J.: Charge constrained density functional molecular dynamics for simulation of condensed phase electron transfer reactions. The Journal of Chemical Physics **131**, 064101 (2009). DOI 10.1063/1.3190169. http://link.aip.org/link/?JCP/131/064101/1

14. Parr, R.G., Yang, W.: Density-Functional Theory of Atoms and Molecules. Oxford University Press (1988)

15. Perdew, J.P., Parr, R.G., Levy, M., Balduz, J.L.: Density-functional theory for fractional parti- cle number: Derivative discontinuities of the energy. Physical Review Letters **49**, 1691–1694 (1982). http://link.aps.org/doi/10.1103/PhysRevLett.49.1691

16. Perdew, J.P., Zunger, A.: Self-interaction correction to density-functional approx- imations for many-electron systems. Physical Review B **23**, 5048–5079 (1981).
http://link.aps.org/abstract/PRB/v23/p5048

17. Szabo, A., Szabo, J., Ostlund, N.S.: Modern Quantum Chemistry: Introduction to Advanced Electronic Structure Theory. Dover Publishing Inc. (1996)

18. Wang, L., Nan, G., Yang, X., Peng, Q., Li, Q., Shuai, Z.: Computational methods for design of organic materials with high charge mobility. Chemical Society Reviews **39**, 423–434 (2010).
http://dx.doi.org/10.1039/b816406c

19. Wu, Q., Cheng, C.L., Van Voorhis, T.: Configuration interaction based on constrained density functional theory: A multireference method. The Journal of Chemical Physics **127**, 164119 (2007). DOI 10.1063/1.2800022. http://link.aip.org/link/?JCP/127/164119/1

20. Wu, Q., Kaduk, B., Van Voorhis, T.: Constrained density functional theory based configura- tion interaction improves the prediction of reaction barrier heights. The Journal of Chemi- cal Physics **130**, 034109 (2009). DOI 10.1063/1.3059784. http://link.aip.org/link/?JCP/130/034109/1

21. Wu, Q., Van Voorhis, T.: Direct optimization method to study constrained sys- tems within density-functional theory. Physical Review A **72**, 024,502 (2005).
http://link.aps.org/doi/10.1103/PhysRevA.72.024502

22. Wu, Q., Van Voorhis, T.: Constrained density functional theory and its application in long- range electron transfer. Journal of Chemical Theory and Computation **2**, 765–774 (2006).
http://dx.doi.org/10.1021/ct0503163

23. Wu, Q., Van Voorhis, T.: Extracting electron transfer coupling elements from con- strained density functional theory. The Journal of Chemical Physics **125**, 164105 (2006).
DOI 10.1063/1.2360263. http://link.aip.org/link/?JCP/125/164105/1

24. Zhang, Y., Yang, W.: Comment on “generalized gradient approximation made simple”. Phys- ical Review Letters **80**, 890–890 (1998). http://link.aps.org/abstract/PRL/v80/p890