# Local-density functional and on-site correlations:
## The electronic structure of $La_2CuO_4$ and $LaCuO_3$

M. T. Czyżyk and G. A. Sawatzky

Department of Solid State and Applied Physics, University of Groningen,
Nijenborgh 4, NL-9747 AG Groningen, The Netherlands
(Received 20 December 1993)

State-of-the-art electronic-structure calculations based on the local-density approximation (LDA) to the density functional fail to reproduce the insulating antiferromagnetic ground state in the parent compounds of the high-temperature oxide superconductors. Similar problems have been observed earlier in *classical* transition-metal oxides such as FeO, CoO, and NiO. In this work we present the method which delivers the correct insulating antiferromagnetic ground state in the *correlated oxides* preserving other properties as well as the efficiency of the *standard* LDA. The method embeds the relevant (for a given system of electrons) part of the Hubbard Hamiltonian into the Kohn-Sham LDA equation. The resulting Hamiltonian attempts to fix two *intrinsic* problems of the LDA: the deficiency in forming localized (atomiclike) moments and the lack of discontinuity of the effective one-particle potential when going from occupied to unoccupied states. We present the detailed study of $La_2CuO_4$ and $LaCuO_3$. In the case of $La_2CuO_4$ the energy gap and the value of the localized magnetic moment in the stable insulating antiferromagnetic solution are in good agreement with experiment. We compare our results with the *standard* local spin density approximation calculation and multiband Hubbard model calculations, as well as with results of spectroscopy: inverse photoemission, valence photoemission, and x-ray absorption at the $K$ edge of oxygen. In the case of $LaCuO_3$ such an extensive comparison is limited due to the limited data available for this compound. We discuss, however, the electric and magnetic properties and the insulator-metal-insulator transitions upon increase of oxygen deficiency.

## I. INTRODUCTION

The density-functional (DF) theory has been a most successful theoretical method for describing ground-state properties in solid-state physics since the beginning of the 1970s. $^{1,2}$ An enormous amount of applications of the local-density approximation (LDA) to the DF can be found in the literature for the description of a wide range of phenomena in a wide range of materials (see, e.g., references within Refs. 1 and 2 and reviews 3 and 4). Unfortunately the class of materials where the LDA does not work properly is also growing rapidly including those with the most startling physical properties.

In particular, although some of the properties of the high-temperature oxide superconductors such as, e.g., the lattice dynamics and crystal stability, are still well described by the LDA, the state-of-the-art electronic-structure calculations performed within this approximation fail to reproduce the insulating, antiferromagnetic (AF) ground state of parent (undoped) materials. Similar problems have already been observed much earlier in *classical* transition-metal oxides such as FeO, CoO, and NiO.

It is well established that the approach which treats the many-body (Coulomb) interaction within the LDA is not adequate for materials which exhibit a strong electron-electron interaction. A crucial question, namely, whether it is possible to solve this problem within the DF by more elaborate approximations than the LDA $^{5}$ or whether it is necessary to resort to configuration-interaction techniques, has attracted a lot of attention during recent years. Within the DF, the self-interaction corrected (SIC) LDA is perhaps the most promising approach. $^{6,7}$ The SIC LDA is, however, very difficult numerically, which strongly inhibits wider applications.

In this work we present the method which delivers the correct insulating AF ground state in the *correlated oxides* preserving other properties as well as the numerical efficiency of the *standard* LDA. The method embeds the relevant (for a given system of electrons) part of the Hubbard-like Hamiltonian into the Kohn-Sham LDA equation. Care is taken to avoid double counting of electron-electron interactions during this procedure. In this way we attack two *intrinsic* problems of the LDA.

The first problem is that the LDA attempts to treat the second-Hund-rule correlation together with spin polarization (Stoner-like). This is obviously incorrect, but it seems to be the only possibility within a formalism based on the electron-gas model. The correlation effects which are behind the second Hund rule are responsible for orbital polarization (ordering) and the formation of local (atomiclike) moments. Stoner-like effects alone are treated rather accurately within the LDA. The simple example of this intrinsic deficiency of the LDA is a transition from a spin-split ferromagnetic to a paramagnetic state. In the so-called *nonmagnetic* solution within the LDA the magnetic moments vanish. This leads to a huge difference in the energy between the magnetic and the nonmagnetic solution, and the critical temperature is related to the moment formation rather than the order-

©1994 The American Physical Society

disorder transition. The inability of developing local mo- ments leads also to a failure in the description of Mott insulators within the LDA, which is a very serious limi- tation. The method, which was introduced by Anisimov et al. $^{8}$ and which is further developed here, includes the leading terms for on-site Coulomb and exchange interac-tion $U$ and $J$ allowing for orbital ordering (polarization) to develop around the mean-field (MF) solution in sys- tems containing localized orbitals.

The second intrinsic problem in the LDA is that the occupied and unoccupied states are solutions to the same N-electron potential instead of being the solutions to the $(N-1)$ - and $(N+1)$ -electron potentials, respectively.In this paper, we worked out the procedure (the model) solving the problem where it is mostly needed: for lo- calized $d$ and $f$ electrons embedded into the reservoir of other (delocalized) electrons. Following the spirit and conclusions of work by Perdew et al. $^{9}$ we further mod ified our Hamiltonian in such a way that the potential jumps discontinuously by a constant $I-A$ when going from occupied to unoccupied states (where $I$ and $A$ are the first ionization potential and electron affinity, respec- tively). For the localized level this constant is just equal to $U$ (or to $U-J$ , depending on the change of spin of the system under concern).

We have performed a series of calculations using two forms of the modified Hamiltonian and the standard LDA (as reference) for a number of transition-metal ox- ides. The stable localized magnetic moment, the energy gap, and other features are in good agreement with ex- periments. We also performed calculations in the same manner for transition metals themselves as a test of lim- itations of our method. Although the approach was not meant to be well founded for systems where orbitals under concern are not localized enough (i.e., $d$ orbitals in pure transition metals in particular) the results are rather interesting and worth some attention. We in- tend to present those results elsewhere. Here we report the results of calculations for $La_{2} CuO_{4}$ and $LaCuO_{3}$ in detail. The former compound does not need any in- troduction; its quasi-two-dimensional (2D) structure is commonly known. The latter compound possesses a per- ovskite structure (among other phases) with small tetrag- onal elongation; its $Cu-O-Cu$ segments form a nearly cu bic three-dimensional (3D) network.

In Sec. II we describe the formalism of our approach. Section II A gives an intermediate step, which consists of an improved version of the method introduced in Ref.8 and which we call the local spin density approxima- tion plus around mean field corrections (LSDA+AMF).Section II B describes a new version of the LSDA $+U$  method. In Sec. III A we present and compare re- sults of calculations performed for $La_{2} CuO_{4}$ with the standard LSDA and with model Hamiltonian versions of the LSDA provided in Secs. II A and II B. Compari- son with experiment and other theoretical work is also given. Section III B is devoted to a similar study of LaCuO3. In addition, we discussed the insulator-metal- insulator transitions upon the increase of oxygen defi- ciency in $LaCuO_{3-\delta}$ . Finally, Sec. IV assembles our conclusions.

## II. METHOD OF CALCULATION
The self-consistent calculations within the LDA wereperformed by the localized spherical wave method (LSW) which is a version of the well-known augmented spheri- cal waves method (ASW) of Wiliams et al. $^{10}$ The LSW has already been successfully applied in many differ- ent cases. $^{11-14}$ The difference between the LSW and the ASW which is of importance here is the linear transfor- mation of the basis set. This transformation producesthe most localized set (hence the name of the method) by screening every spherical wave centered on every site by spherical waves centered on the neighboring sites. $^{12}$ As far as the ASW is a sister method of the linear muffin-tin orbital method (LMTO), $^{15}$ the LSW is a sister methodof the tight-binding LMTO. $^{16}$ 

The reason why the most localized basis set is so im- portant is because it also forms a nearly orthogonal set. The orthonormality of the basis set is implicitly assumed below when we write down the electron-electron interac- tion terms for $d$ - and/or $f$ -atomiclike orbitals in modi fied total energy functionals. For this reason the LSW, in addition to its numerical efficiency, proves to be a very convenient method.

### A. LDA and the orbital/spin polarization around the the MF solution
In order to cure (at least partially) the deficiencies of the LDA mentioned in the preceding section one can at- tempt to treat the correlation of the localized $d$ and/or f electrons explicitly by adding to the total energy func- tional the relevant electron-electron interaction terms ex- tracted from the general many-body Hamiltonian. Dur- ing this procedure one should avoid double counting of the interaction. The simplest expression which includes on-site Coulomb and exchange interaction is written in the form
$$
\begin{aligned}
E^{\mathrm{LDA}+\mathrm{AMF}}= & E^{\mathrm{LDA}}+\frac{1}{2} \sum_{m, m^{\prime}, \sigma} U\left(n_{m \sigma}-n^{0}\right)\left(n_{m^{\prime}-\sigma}-n^{0}\right) \\
& +\frac{1}{2} \sum_{m, m^{\prime}, m \neq m^{\prime}, \sigma}(U-J)\left(n_{m \sigma}-n^{0}\right)\left(n_{m^{\prime} \sigma}-n^{0}\right), \\
& (1)
\end{aligned}
$$
where $n_{m \sigma}$ are occupation numbers of the localized level orbitals and $n^{0}=\frac{1}{2(2 l+1)} \sum_{m \sigma} n_{m \sigma}$ ; it was proposed by Anisimov et al. $^{8}$ Showing that LDA corresponds to a MF solution of the many-body problem, an extensive justifi- cation of this formula was presented in Ref. 8. There is no need to reproduce those considerations here beyond the summarizing point that the functional in Eq. (1) and the effective one-particle potential emerging from it (by the functional derivation procedure) allow us to develop spin and/or orbital polarization (ordering) around and beyond the MF LDA solution. [The acronym AMF in Eq. (1) and in expressions below means around mean field.] From a formal point of view, we just mention that if one writes the identity
$$
\begin{aligned}
n_{m \uparrow} n_{m^{\prime} \downarrow}= & n_{m \uparrow}\left\langle n_{\downarrow}\right\rangle+n_{m^{\prime} \downarrow}\left\langle n_{\uparrow}\right\rangle-\left\langle n_{\uparrow}\right\rangle\left\langle n_{\downarrow}\right\rangle \\
& +\left(n_{m \uparrow}-\left\langle n_{\uparrow}\right\rangle\right)\left(n_{m^{\prime} \downarrow}-\left\langle n_{\downarrow}\right\rangle\right)
\end{aligned}\qquad(2)
$$

and observes that the first three terms consist of the MF approximation, one may directly conclude that the natural extension should have a form similar to Eq. (1).

The first version of the total energy functional we use in this work differs from that in Eq. (1) in two aspects.

First, we suggest that $n^0$ should be replaced by $n_{\sigma}^0 = \frac{1}{2l+1} \sum_m n_{m\sigma}$. In that way the average is taken for each spin independently [as in Eq.(2)]. To be consistent, we use then $E^{\text{LSDA}}$ instead of $E^{\text{LDA}}$ as the starting point. This small formal change has important consequences. It opens degrees of freedom for spin-split solutions for all other electrons in the system. The two different categories of correlation mentioned in the Introduction are treated by different parts of the Hamiltonian in a complementary way.

The second improvement is that we use matrices $U_{mm'}$ and $J_{mm'}$ instead of scalar values $U$ and $J$. Allowing for such anisotropy makes the model more realistic and partially accounts for the multiplet splitting.

Our first energy functional then reads
$$
\begin{aligned}
E^{\mathrm{LSDA}+\mathrm{AMF}}= & E^{\mathrm{LSDA}}+\frac{1}{2} \sum_{m, m^{\prime}, \sigma} U_{m m^{\prime}}\left(n_{m \sigma}-n_{\sigma}^{0}\right) \\
& \times\left(n_{m^{\prime}-\sigma}-n_{-\sigma}^{0}\right) \\
& +\frac{1}{2} \sum_{m, m^{\prime}, m \neq m^{\prime}, \sigma}\left(U_{m m^{\prime}}-J_{m m^{\prime}}\right)\left(n_{m \sigma}-n_{\sigma}^{0}\right) \\
& \times\left(n_{m^{\prime} \sigma}-n_{\sigma}^{0}\right).
\end{aligned}\tag{3}
$$

The structure of $U_{mm'}$ and $J_{mm'}$ matrices is known since the classical work of Condon and Shortley$^{17}$ and Griffith. $^{18}$ Their specific forms in cubic symmetry for $d$ electrons were already used in the context of correlation effects in transition metals, e.g., by Oleś and Stollhoff$^{19}$ and recently in the model Hartree-Fock calculations for $\mathrm{La}_{2} \mathrm{CuO}_{4}$ by Grant and McMahan. $^{20}$

We want our approach (the implementation) to be general, equally valid for different $l$ values (in particular for $d$ and $f$ electrons) and not limited to some specific symmetry. Therefore, we opt for the general expressions for $U_{mm'}$ and $J_{mm'}$ in terms of Slater integrals and Gaunt's numbers (or equivalently in terms of the Clebsch-Gordan coefficients). $^{18}$ For completeness we reproduce those expressions in the Appendix.

In order to obtain the effective potential in DF one takes the functional derivative of the total energy over the charge density $\delta / \delta n(\mathbf{r})$. This procedure has to be extended here to the variation of the charge density of particular orbital $n_{m \sigma}(\mathbf{r})$ when applied to terms added to energy functional. One then obtains
$$
\begin{aligned}
V_{m \sigma}^{\mathrm{LSDA}+\mathrm{AMF}}(\mathbf{r})= & V_{\sigma}^{\mathrm{LSDA}}(\mathbf{r})+\sum_{m^{\prime}} U_{m m^{\prime}}\left(n_{m^{\prime}-\sigma}-n_{-\sigma}^{0}\right) \\
& +\sum_{m^{\prime}, m^{\prime} \neq m}\left(U_{m m^{\prime}}-J_{m m^{\prime}}\right)\left(n_{m^{\prime} \sigma}-n_{\sigma}^{0}\right).
\end{aligned}\tag{4}
$$

Two important comments are in order here. First, we have dropped site indices in $U, J, n_{m \sigma}$, and $n_{\sigma}^{0}$, as well as the summation over all sites in case of expressions for the total energy. We have also dropped the index $l$, which should distinguish between different possible localized levels ( $d, f$, and so on). Second, the effective potential given by Eq. (4) is orbital dependent only when acting in the nearly orthogonal subspace of the localized level selected for such treatment (see the comment about the basis set above). This feature eliminates the difficulty of using a non-Hermitian Hamiltonian as encountered in SIC LDA calculations. $^{7}$

Recently, Steiner et al. $^{21}$ have presented calculations of the one-particle Green's function and quasiparticle band structure for $\mathrm{Fe}, \mathrm{Co}$, and $\mathrm{Ni}$. The self-energy operator which they constructed includes on-site $3 d-3 d$ interactions up to the second order in parameters $U$ and $J$. Up to first order the self-energy operator is energy independent, so there is no need to solve the Dyson equation. Straightforward diagonalization delivers the same information and usually it is more accurate and much more efficient numerically. Our approach, as described so far, is therefore equivalent to that in Ref. 21 up to the first order in on-site Coulomb and exchange interaction. Moreover, we treat the first order terms more accurately using $U_{mm'}$ and $J_{mm'}$ matrices instead of scalar values $U$ and $J$. It is instructive, however, to see the diagrammatic representation of the Dyson equation and the structure of the self-energy operator. $^{21}$ One should notice that the MF part of interactions were explicitly subtracted from the self-energy. In our approach this is done by construction from the very beginning [see Eq. (1) and Ref. 8].

### B. LDA and the atomic limit

First, we transform the total energy functional given in Eq. (3) to a different form:
$$
E^{\mathrm{LSDA}+\mathrm{AMF}}=E^{\mathrm{LSDA}}+H_{\mathrm{int}}-\left\langle H_{\mathrm{int}}\right\rangle,\tag{5}
$$
with
$$
\begin{aligned}
H_{\mathrm{int}}= & \frac{1}{2} \sum_{m, m^{\prime}, \sigma} U_{m m^{\prime}} n_{m \sigma} n_{m^{\prime}-\sigma} \\
& +\frac{1}{2} \sum_{m, m^{\prime}, m \neq m^{\prime}, \sigma}\left(U_{m m^{\prime}}-J_{m m^{\prime}}\right) n_{m \sigma} n_{m^{\prime} \sigma}.
\end{aligned}\tag{6}
$$

It is easy to show using the summation relations given in the Appendix that the averaging over occupation numbers $(\left\langle n_{m \sigma}\right\rangle=n_{\sigma}^{0})$ leads to the expression
$$
\left\langle H_{\mathrm{int}}\right\rangle=U N_{\uparrow} N_{\downarrow}+\frac{1}{2}\left(N_{\uparrow}^{2}+N_{\downarrow}^{2}\right) \frac{2 l}{2 l+1}(U-J),\tag{7}
$$
where $N_{\sigma}=(2 l+1) n_{\sigma}^{0}=\sum_{m} n_{m \sigma}$. Equation (5) is just another form of the result obtained under the assumption that the LDA corresponds to the MF solution.

In the next step, one may verify the total energy of the $N$-degenerate level $(N=N_{\sigma}+N_{-\sigma})$ with Coulomb repulsion and exchange parameters $U$ and $J$. We call such a case an atomic limit, which may be written as
$$
\begin{aligned}
E^{\text {at lim }}= & \frac{1}{2} U N(N-1)-\frac{1}{2} J N_{\uparrow}\left(N_{\uparrow}-1\right) \\
& -\frac{1}{2} J N_{\downarrow}\left(N_{\downarrow}-1\right).
\end{aligned}\tag{8}
$$

Now we suggest that because we want to correct the LDA in the description of localized $d$ or/and $f$ electrons

embedded into the reservoir of delocalized electrons, one should subtract the term $E^{\text{at lim}}$ [Eq. (8)] obtained in the atomic limit from the total energy functional instead of a term corresponding to the mean field [Eq. (7)] while adding an explicit electron-electron interaction term [Eq. (6)].$^{22}$ In this way we obtain the new version of the LSDA+$U$ total energy functional:

$$
E^{\mathrm{LSDA}+U}=E^{\mathrm{LSDA}}+H_{\mathrm{int}}-E^{\text {at lim }}. \tag{9}
$$

To obtain the effective potential one should take the functional derivative in the same manner as in the preceding subsection. We can show, after some algebra, that the new effective potential, which we call $V_{m \sigma}^{\mathrm{LSDA}+U}$, assumes the following form:

$$
V_{m \sigma}^{\mathrm{LSDA}+U}(\mathbf{r})=V_{m \sigma}^{\mathrm{LSDA}+\mathrm{AMF}}(\mathbf{r})-(U-J)\left(n_{\sigma}^{0}-\frac{1}{2}\right)
\tag{10}
$$

[compare with Eq. (4)].

The important feature of this new potential is that on the top of the orbital and/or spin polarization *around* the LSDA solution, the last term adds the shift of the center of the level depending on its average occupation. In an extreme case of empty states this term moves the level upward by $\frac{1}{2}(U-J)$ and in a case of occupied states it moves the level downward by $\frac{1}{2}(U-J)$. One should note (as mentioned already above) that for the localized level $U-J=I-A$, where $I$ and $A$ are the first ionization potential and electron affinity, respectively. In this way the new potential (both terms together) mimics the discontinuity when going from occupied to unoccupied states. For years one used to interpret the LDA eigenenergies of unoccupied (occupied) states as the electron addition (removal) energies knowing and/or ignoring the fact that there is no strict justification for such an interpretation. Although our method is not solving this problem in principle (we tend to say that there is no such solution within one-particle theory), the eigenvalues of unoccupied (occupied) states of the new effective potential will be closer to the true addition (removal) energy also for the correlated $d$- and/or $f$-electron systems.

## III. RESULTS OF CALCULATIONS
### A. $\text{La}_2\text{CuO}_4$

We have assumed that $\text{La}_2\text{CuO}_4$ has spatial symmetry of a single-face-centered orthorhombic $D_{2h}^{18}$ space group described as $Abma$. The orthorhombic $c$ axis is parallel then to the conventional one (see comment about conventions in Ref. 4). We have ignored, however, the orthorhombic distortion and tilting of the $\text{CuO}_6$ octahedra. The extensive attempts to obtain an insulating AF solution within the LSDA have shown that inclusion of this distortion, though producing some narrowing of the topmost valence bands, does not open the gap and does not provide a stable magnetic moment (see, e.g., the review by Pickett$^4$). The on-site Coulomb correlation which we introduce in our calculations is by far much stronger and practically independent of such a distortion. This justifies our simplification. It is relevant, however, to observe that the AF ordering makes two Cu atoms in the elemental cell inequivalent. Also eight La and four apex oxygen atoms which were respectively equivalent in $D_{2h}^{18}$ space group are split in two classes (of four and two atoms). Such a structure can be described, formally, by the $D_{2h}^{19}$ ($Ammm$) space group and the symmetry lowering is obtained by removing a screw axis from $D_{2h}^{18}$. La and apex O atoms may then gain some spin polarization, but all the planar oxygen atoms still remain equivalent (in accordance with an elemental analysis of the planar AF structure).

The atomic-sphere radii we have used are (in angstroms) 0.92 for Cu, 1.53 for La, and 1.42 and 1.36 for planar and apex oxygen, respectively. This selection, which differs from the ones most used in LDA before, reflects the realistic size of ions (small Cu and large O) and it allows for a direct O-O overlap. It was stressed by Pickett$^4$ that this is important for a realistic description of the electronic structure of cuprates. In order to improve the space filling we have allocated four empty atomic spheres with radii $1.24$ Å at all positions equivalent to $(1/4,1/4,1/4)$.

All electrons were included during the self-consistent calculations. The basis set of augmented spherical waves for the valence electrons consisted of $4s$-, $4p$-, and $3d$-like functions for Cu; $2s$, $2p$, and $3d$ functions for O; $6s$, $5p$, $5d$, and $4f$ functions for La, and additionally $s$- and $p$-like functions for the empty spheres. In all $\text{La}_2\text{CuO}_4$ calculations the self-consistency was obtained with the use of $512\ \mathbf{k}$ points in the Brillouin zone (BZ). The density of states (DOS) and partial DOS were calculated by linear tetrahedral technique.

We will compare results of three calculations: (i) using the standard LSDA; (ii) using the modified potential according to Eq. (4), which we call LSDA+AMF; and (iii) using the modified potential according to Eq. (10), which we call LSDA+$U$. In both cases (ii) and (iii) we included an on-site correlation for Cu $3d$ and La $4f$ orbitals.

To complete this description we have to comment on how we treated the on-site Coulomb and exchange parameters. There have been many efforts in the literature to calculate effective (screened) $U$ in atoms and solids by various approaches and in particular within the LDA (see, e.g., Refs. 23–26 and the references therein). Though it is established that constrained LDA calculations can deliver reasonable values of the on-site Coulomb repulsion parameter $U$, those values may still differ by up to 30% between different calculations.$^{27}$ In previous implementations of the LDA+$U$ approach,$^{8,28}$ which are closer to our LSDA+AMF version, the value of $U$ and also the on-site exchange $J$ parameter were calculated within the LDA by the method introduced by Gunnarsson $et\ al.^{24}$ showing that it is possible to work in a parameter-free framework. In this work, only values of $U\equiv F_{\text{eff}}^0$ for Cu $3d$ and La $4f$ states were used as the results of constrained LDA calculations. Having in mind a large spread of $U$ values for Cu $d$ states reported in the literature, we have decided, in order to facilitate a comparison of our results with those of Grant and McMahan,$^{20}$ to use the same value of $U=7.42$ eV. For La $4f$ we used the value of $U=11$ eV.$^{29}$ For Cu $3d$ $F^2$ and $F^4$ Slater integrals we chose the free-ion optical values obtained

from Ref. 30, as already used in Refs. 31 and 32. In order to get the La $4f$ $F^{2},F^{4}$, and $F^{6}$ values, we used the fact that empirical Slater integrals compare very favorably with the results of atomic Hartree-Fock calculations when the latter ones are scaled down to $80\% .^{33}$ We took Hartree-Fock values of $F^{2},F^{4}$, and $F^{6}$ for La $4f$ (extrapolated from ones for Ce) from Mann's table $^{34}$ and then reduced them accordingly. The relations between $F^{2},F^{4}$, etc. and $J,U,J_{mm'}$, and $U_{mm'}$ are given in the Appendix. Selected values of the parameters we used are listed in Table I. We want to stress that none of the parameters was treated as adjustable. (N.B. One may always try to do so to tune some important characteristics of the final results to experimental data. Indeed, as we point out below, comparing results with experiments, Grant and McMahan's $U=7.42$ eV seems to be to small. A value larger by about 1.2 - 1.6 eV, still being in the range of values reported in the literature, would improve the agreement.)

The LSDA band structure of $La_{2}CuO_{4}$ was presented in the literature in many occasions (see, e.g., Ref. 4), and though different calculations always show some small differences, it is essentially well established. Our results compare well with previous calculations and in this sense they do not bring any new information, except perhaps a wider energy range and very detailed DOS and partial DOS projected on irreducible representations (see below). We need this calculation as a reference in our systematic comparison.

In Figs. 1(a), 1(b), and 1(c) we compare the overall structure of $La_{2}CuO_{4}$ obtained by the three calculations, respectively. The total DOS in unit cell (two $La_{2}CuO_{4}$ molecules) is shown in the lower panel. In the upper panels we present local DOS projected on different atomic sites. The energy range includes the semicore $2s$ states of oxygen at about -19 eV and -17 eV for planar and apex sites and semicore $5p$ states of La at about -15 eV. Then through valence Cu $3d$ and O $2p$ states (from -8 eV) we go to unoccupied states up to 15 eV. Unoccupied states (and actually all states in the total DOS) are strongly dominated by $4f$ states of La and then, next to them, $5d$ states of La (note the different scale of some panels). While the O $2s$ and La $5p$ remain virtually unchanged when going from (a) to (b) and (c) in Fig. 1, Cu $3d$ and O $2p$ valence states are strongly modified. Energy gaps of 2.10 eV and 1.65 eV are opened in cases (b) and (c), respectively. As we will discuss in more detail below, this is due to the Hubbard splitting of the Cu $d_{x^{2}-y^{2}}$ orbital. The experimental value of this gap is reported to be $1.8\ eV.^{35}$ The gap in $La_{2}CuO_{4}$ is reduced by many-body effects such as the formation of Zhang-Rice singlets. Our gap of 1.65 eV is too small. This could be due to a too small $U$ value used for Cu $d$ states, and also perhaps an incorrect treatment of the configuration hybridization as discussed below. In Fig. 1 one can also observe an essential enhancement of the oxygen contribution to the top of the valence band which is the manifestation of the charge-transfer character of the gapin late transition-metal oxides. $^{36}$

TABLE I. Selected parameters of on-site Coulomb interaction (in eV). Effective $U$ were calculated by the constrained LDA. Slater integrals are either empirical or HF values (see the main text). The last column gives the resulting on-site exchange $J$ parameter.

<table>
<thead>
  <tr>
    <th></th>
    <th>$U$</th>
    <th>$F^{2}$</th>
    <th>$F^{4}$</th>
    <th>$F^{6}$</th>
    <th>$J$</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>Cu $3d$</td>
    <td>$7.42^{\mathrm{a}}$</td>
    <td>11.5</td>
    <td>7.4</td>
    <td></td>
    <td>1.35</td>
  </tr>
  <tr>
    <td>La $4f$</td>
    <td>$11.0^{\mathrm{b}}$</td>
    <td>8.4</td>
    <td>5.3</td>
    <td>3.7</td>
    <td>0.68</td>
  </tr>
</tbody>
</table>

$^{\mathrm{a}}$ Reference 20.
$^{\mathrm{b}}$ Reference 29.

Figure 1 and all other figures in the paper are plotted in a such way that zero corresponds to the Fermi energy for the metallic solution and to the top of valence band for insulating solutions.

In both cases (ii) and (iii) [Figs. 1(b) and 1(c)] we have obtained a stable AF solution with local $\mu_{\mathrm{Cu}}=$ $0.67\mu_{B}$ and $0.62\mu_{B}$, respectively. These values are in good agreement with the experimental one, which is around $0.55\mu_{B}.^{37}$ The experimentally measured value is always reduced by quantum fluctuations in the AF state. The result of our calculation of $\mu_{\mathrm{Cu}}$, which does not take this effect into account, should be reduced (for a two-dimensional system) to about $66\%$ of its value. $^{38}$ The values of charge transfer gaps and Cu local magnetic moments for both $La_{2}CuO_{4}$ and $LaCuO_{3}$ are collected in Table II.

The difference between cases (ii) and (iii) as far as gap and magnetic moment are concerned is not sufficient to claim that approach (iii) is superior to (ii). There is, however, another important, clearly visible difference between results (ii) and (iii), which is the position of a very sharp peak (about 1 eV wide and also very large) of La $4f$ states. In case (ii) and in the standard LSDA these states are placed about 1 eV below La $5d$ states at about 4 eV and 3 eV, respectively. [In this aspect cases (i) and (ii) are almost the same.] In case (iii), however, La $4f$ states are shifted nearly 5 eV upward and they are placed at 8.5 eV coinciding with the top of $5d$ states. This is the relative position of lanthanum $5d$ and $4f$ states which was very clearly observed by an inverse photoemission experiment. $^{39}$ Moreover, the absolute position on the energy scale is also correctly reproduced. Standard LSDA calculations were always placing these states much too low (which was usually silently ignored). This dramatic difference is very pronounced in Fig. 2, where we present the band structure of $La_{2}CuO_{4}$ obtained in cases (i) and (iii). The group of very flat La $4f$ bands is shifted from about 3 eV in the case of standard LSDA calculation [given in Fig. 2(a)] to 8.5 eV in the case of LSDA+$U$ [given in Fig. 2(b)].

We have shown that our new scheme (iii) offers important improvements over scheme (ii) and only results of this scheme will be discussed and compared to standard LSDA from now on.

The one-face-centered orthorhombic BZ and the definition of the cross section through it are shown in Fig. 3. Note that the section $\Gamma-Z$ corresponds to the (110) direction. Sections $\Gamma-Y$ and $Z-L$ are parallel to the conventional $k_{z}$ axis (see comments about conventions in Ref. 4) and therefore show very little dispersion in both

![](./images/812738279832027136_1.jpg)

FIG. 1. Total DOS (two molecules in the unit cell) and local DOS on different atomic sites of $La_2CuO_4$: (a) metallic nonmagnetic solution by standard LSDA; (b) insulating AF solution by modified Hamiltonian LSDA+AMF [Eq. (4)]; (c) insulating AF solution by modified Hamiltonian LSDA+$U$ [Eq. (10)]. The zero of energy is set to the Fermi energy in (a) and to the top of the valence band in (b) and (c). While the semicore O $2s$ and La $5p$ states remain unchanged there is a strong modification of the valence Cu $3d$ and O $2p$ states when going from (a) to (b) and (c). Note also the shift of unoccupied La $4f$ states in (c). See the main text for more discussion.

cases (with the exception, perhaps, of dispersive unoccupied La $5d$ states).

In order to discuss the nature of differences between the metallic nonmagnetic solution [Fig. 2(a)] and the insulating AF solution [Fig. 2(b)] we have to analyze simultaneously the projections of the local partial DOS of

![](./images/812738279832027136_2.jpg)

FIG. 2. Electronic band structure of $La_2CuO_4$: (a) metallic nonmagnetic solution by standard LSDA; (b) insulating AF solution by the modified Hamiltonian (LSDA+$U$) Eq. (10). The zero of energy is the same as in Fig. 1. The semicore O $2s$ and La $5p$ bands are not shown. The upper Hubbard band (UHB) splits up from the O $2p$ and Cu $3d$ valence bands and opens the gap of 1.65 eV in the AF solution. Its LHB partner is located at $-7$ eV. (See Fig. 4 and its discussion in the main text.) Note also the 5 eV upward shift of very flat La $4f$ states. For more comments see the main text.

<table>
<caption>TABLE II. Charge-transfer gaps and Cu local magnetic moments in $La_2CuO_4$ and $LaCuO_3$.</caption>
<thead>
  <tr>
    <th rowspan="2"></th>
    <th colspan="3">$La_2CuO_4$</th>
    <th colspan="3">$LaCuO_3$</th>
  </tr>
  <tr>
    <th>LSDA</th>
    <th>LSDA+$U$</th>
    <th>Expt.</th>
    <th>LSDA</th>
    <th>LSDA+$U$</th>
    <th>Expt.</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>$E_g$</td>
    <td>0</td>
    <td>1.65</td>
    <td>$1.80^{\text{a}}$</td>
    <td>0</td>
    <td>0.95</td>
    <td>0 ?</td>
  </tr>
  <tr>
    <td>$\mu_{Cu}$</td>
    <td>0</td>
    <td>0.62</td>
    <td>$0.55^{\text{b}}$</td>
    <td>0</td>
    <td>0.98</td>
    <td>0 ?</td>
  </tr>
</tbody>
<tfoot>
  <tr>
    <td colspan="7">${}^{\text{a}}$Reference 35.</td>
  </tr>
  <tr>
    <td colspan="7">${}^{\text{b}}$Reference 37.</td>
  </tr>
</tfoot>
</table>

Cu $3d$ and planar and apex O $2p$ states on the symmetry components. These partial DOS are given in Figs. 4 - 6. All these figures are organized in the same way as in Fig. 2: (a) gives the results of standard LSDA; and (b) gives the results of the LSDA+$U$ [Eq. (10)]. First of all, we show in Fig. 4 the projection of Cu $3d$ states on irreducible representations of the point group of the Cu site (which is $D_{4h}$ because, as we mentioned above, we ignored the orthorhombic distortion). The atomic origin of these states is also indicated in terms of cubic harmonics. For the metallic solution, states at the Fermi energy are dominated by $d_{x^2-y^2}$ component (as expected). They hybridize with planar O $2p$ states which are given in Fig. 5. Analyzing the shape of partial states, one can locate bonding ($-7$ to $-5$ eV) and antibonding ($-1$ to $1.5$ eV) parts of the $d_{x^2-y^2}-p\sigma$ hybrid. It is also possible to do the same with $d_{xy}-p\pi_{\parallel}$ and $d_{yz}-p\pi_{\perp}$ components; however, bonding-antibonding separation is not so evident.

In the case of the AF solution $d_{x^2-y^2}$ states are strongly modified by an on-site correlation. The formation of a lower Hubbard band (LHB) at $-7$ eV and an upper Hubbard band (UHB) of opposite spin at 2 eV is very clear. Their separation (9 eV) is larger than the value of the Coulomb $U$ (7.4 eV) due to hybridization (which is a well known behavior). The overall shift of all other Cu $d$ states downward (Fig. 4) and O $2p$ states upward is the next thing to observe. The latter is true,

![](./images/812738279832027136_3.jpg)

FIG. 3. The one-face-centered orthorhombic Brillouin zone. The bold solid line shows the cross section which we used for plotting the band structure in Fig. 2.

<table>
<caption>TABLE III. Partition of the first added hole and the first added electron in La₂CuO₄ (in %). See the main text for more comments.</caption>
<thead>
<tr>
<th rowspan="2"></th>
<th colspan="3">First hole at the top of the valence band</th>
<th colspan="3">First electron in the conduction band (UHB)</th>
</tr>
<tr>
<th>LSDA</th>
<th>LSDA+$U$</th>
<th>$8B$ HMª</th>
<th>LSDA</th>
<th>LSDA+$U$</th>
<th>$8B$ HMª</th>
</tr>
</thead>
<tbody>
<tr>
<td>Cu $d_{x^2-y^2}$</td>
<td>28</td>
<td>4</td>
<td>8</td>
<td>48</td>
<td>60</td>
<td>65</td>
</tr>
<tr>
<td>Cu $d_{z^2}$</td>
<td>17</td>
<td>14</td>
<td>14</td>
<td>5</td>
<td>0.3</td>
<td>~0</td>
</tr>
<tr>
<td>planar O</td>
<td>16</td>
<td>15</td>
<td>25</td>
<td>36</td>
<td>35</td>
<td>33</td>
</tr>
<tr>
<td>apex O</td>
<td>27</td>
<td>61</td>
<td>52</td>
<td>10</td>
<td>3.8</td>
<td>~0</td>
</tr>
</tbody>
<tfoot>
<tr>
<td colspan="7">ªEight-band Hubbard model. Reference 20.</td>
</tr>
</tfoot>
</table>

in particular, for the apex oxygen states which are given in Fig. 6. Due to this effect the overall contents of oxygen at the top of the valence band increases significantly, changing from 46% (19% planar and 27% apex) in the standard LSDA to 76% (15% planar and 61% apex) in our AF solution. The latter values compare favorably with 77% (25% planar and 52% apex) obtained for the highest occupied valence state in the AF solution of the eight-band Hubbard model by Grant and McMahan.²⁰ Their values, however, were given for one specific k point in the BZ while ours are obtained by integrating over the energy interval at the top of the valence band containing one hole per La₂CuO₄ molecule. This procedure seems to be more representative. [In our calculation, we include all other valence orbitals (e.g., La), which also makes the results of our distribution analysis more realistic.] This high content of oxygen at the top of valence band is in accordance with the classification of cuprates as charge-transfer gap materials.³⁶ The same estimation of Cu contribution shows a change from 45% (28% $d_{x^2-y^2}$ and 17% $d_{z^2}$) in the standard LSDA to 17% (4% $d_{x^2-y^2}$ and 14% $d_{z^2}$) in the AF solution. The latter values are again very close to those (8% and 14%) obtained in Ref. 20 by the eight-band Hubbard model in the AF solution. The results of the partition analysis of the first added hole are collected in Table III (together with the results of a similar analysis for the first added electron which is discussed below). We also included there the correspond-

![](./images/812738279832027136_4.jpg)

FIG. 4. Cu d partial DOS in La₂CuO₄ projected on irreducible representations of site symmetry: (a) and (b) and the zero of energy are the same as in Fig. 2. The atomic origin of states is also indicated. Solid and dashed line shows DOS for opposite spin directions. In the nonmagnetic case (a) these two lines are degenerate. Cu d contribution to the LHB and UHB (which are separated by about 9 eV) is entirely dominated by $x^2 - y^2$ component with opposite spins. Note also the overall downwards shift of all other d states when going from (a) to (b).

ing values from Ref. 20.

In spite of the essential progress in the description of various properties of $La_2CuO_4$ as we pointed out so far and as we will also show below when discussing unoccupied states of the LSDA+$U$ solution, the nature of the first ionization state (the top of the valence band) is still not described properly. We want to stress that this is a serious problem in our approach and we discuss it in some detail. It is established (experimentally and by many-body theory) that the first added hole in $La_2CuO_4$ goes to the Cu-O planes. This means that it should have predominantly planar O $2p\sigma$ and Cu $d_{x^2-y^2}$ character, which is not the case in our calculation (see Table III). Hole doping populates the Zhang-Rice (ZR) singlets$^{40}$ which bind the holes in the Cu-O planes. A description of ZR singlets seems to be impossible within a one-particle picture. (No methods with a single-determinant many-body function can do this.) We argue, however, that the essential part of the energetics of ZR singletlike states can be obtained. There are two mechanisms which should be taken into account. First, it was shown$^{28,20}$ that in the solution in which the spin of one Cu is flipped relatively to the AF background an extra hole goes to four surrounding (planar) oxygens (in ac-

![](./images/812738279832027136_5.jpg)

FIG. 5. Planar O $2p$ partial DOS in $La_2CuO_4$: (a) and (b) and the zero of energy are the same as in Fig. 2. Unoccupied states are shown as multiplied by a factor of 10, which in the case of metallic solution (a) produces the discontinuity at zero energy. The opening of the gap of 1.65 eV [in (b)] is strongly pronounced for the $p\sigma$ component. Note a large contribution of this state to the UHB. For more discussion, in particular when the shape of unoccupied states is concerned, see the main text.

![](./images/812738279832027136_6.jpg)

FIG. 6. Apex O $2p$ partial DOS in $La_2CuO_4$. The figure is organized as Fig. 5, except that the solid and dashed lines indicating DOS of opposite spin directions in (b) are not fully degenerate. Spin splitting of the occupied $\sigma$ component corresponds exactly to the spin-splitting Cu $d_{z^2}$ component in the topmost panel of Fig. 4(b). Note also the small spin-polarized contribution to the UHB of $\sigma$ component in (b). All states are shifted significantly towards the top of valence band when going from (a) to (b). See the main text for more discussion.

cordance with elementary symmetry analysis). The lim- ited configuration-interaction calculations mixing such a Cu-spin-flipped solution with the AF solution with a model Hamiltonian gave the ratio of planar to apex oxy- gen contributions which is much closer to the experimen- tal value (see Ref. 20 and references therein). We also can obtain the one-Cu-spin-flipped solution using a suit- able supercell with our LSDA+$U$ method (as was demon strated with the simpler scheme in Ref. 28). Though the subsequent configuration-interaction between these two solution seems to be beyond our method, we ex- pect that the energetics will be dominated by one-Cu- spin-flipped solution. The second mechanism, which is, as a matter of fact, more general (the first mecha- nism was related to specific 2D square geometry of Cu- O bonds), is the renormalization of transfer integrals to mimic the configuration-configuration hybridization of many-body theory rather than to use the molecular orbital-molecular orbital hybridization as in one-particle theories. This mechanism selectively enhances the hy- bridization of some orbitals by factors related to the de- generacy (by symmetry) of configuration-configuration hybridization. $^{22}$ It is expected (for further discussion seethe paragraph below about the valence photoemission) that a part of $Cu d_{x^{2}-y^{2}}$ and planar O $2 p \sigma$ states will be further stabilized and perhaps pushed out of the top of the valence band.

To complete the discussion of the partial DOS of the valence bands in the AF solution, we mention that the hybridization between $Cu d$ and $O 2 p$ states is more pro nounced than in the standard LSDA solution insofar as $Cu d_{x y}-O p \pi_{\|}, Cu d_{y z}-O p \pi_{\perp}$ , and $Cu d_{z^{2}}$ - apex O $p \sigma$ orbitals are concerned. Bonding-antibonding sep aration is also more evident, as one may see comparingthe respective panels in Fig. 4(b) with those in Fig. 5(b) for planar and those in Fig. 6(b) for apex oxygen. In particular, $p \sigma$ states of apex oxygen show spin splitting,which exactly corresponds to the opposite (as it should) spin splitting of $Cu d_{z^{2}}$ states. The bonding part is lo cated at $-4 eV$ and antibonding at the top of the valence band. There are, however, features in the $p \pi_{\|}$ component of the planar oxygen DOS that cannot be traced to Cu- O hybridization (also called nonbonding when this hy-bridization is concerned). As shown already by others, $^{23}$  a direct $p-p$ interaction plays an important role here.

Turning to unoccupied states, we make two points. The first concerns the composition of the UHB. This sin- gle band (doubly degenerate, as all the others, due to AF order) is separated by a gap of $1.65 eV$ from the top of valence bands [see Fig. 2(c)]. From case (b) of Figs. 4,5, and 6 one can see that the UHB is entirely built from the spin polarized $Cu d_{x^{2}-y^{2}}$ component, which amounts to $60 \%$ , and from the planar $O p_{y}$ component, which amounts to $35 \%$ (values reported in Ref. 20 were $65 \%$ and $33 \%$ , respectively). While the contribution from $Cu d_{z^{2}}$  is negligibly small (about $0.3 \%$ ), there is also a contribu tion from the apex $O p_{z}$ component of about $3.8 \%$ . The latter contribution is relevant for a proper description of polarized x-ray absorption spectra of oxygen, which we discuss below. All values obtained in this analysis are collected in Table III.

Our second comment about unoccupied states con- cerns the overall shape of $O p$ states in the energy range up to $11 eV$ . The dramatic change of these states [com pare (a) with (b) in Figs. 5 and 6], besides the formation of gap, is due to very sharp peaks which are located at3 eV in the standard LSDA calculation (a) and which disappear in the LSDA+$U$ calculation (b). These peaks are identified as the tails of La $4 f$ states entering the oxygen atomic spheres. They are stronger for apex O because it is a nearest neighbor of La. Actually, these peaks do not disappear, but they shift upward by about5 eV where they superimpose on the sharp structures already present in that energy range. This behavior is directly related to the shift of La $4 f$ states which we dis cussed in detail when describing Figs. 1 and 2. Above, referring to the inverse photoemission experiment, $^{39}$ we used this shift to discriminate between the calculation(ii) performed with LSDA+AMF [Eq. (4)] and the cal- culation (iii) performed with LSDA+$U$ [Eq. (10)]. Here we again confront all three calculations with another ex- periment, namely, with polarized x-ray absorption at the $K$ edge of oxygen. $^{41}$

In Figs. 7(a)-7(c) we show the results of the calcu- lation of absorption spectra. The experimental result is also included. The curve marked $E \| c(E \perp c)$ reflects the shape of $z$ ( $x$ and $y$ ) component(s) of both apex and planar $O p$ states. Contributions from apex and

![](./images/812738279832027136_7.jpg)

FIG. 7. Polarized x-ray absorption at the $K$ edge of oxy gen in $La_{2} CuO_{4}$ : (a)-(c) are the same as in Fig. 1. Dashedline, $E \perp c$ ; dotted line, $E \| c$ . Experimental results (Ref. 41) are added in the case (c) and $E \perp c$ and $E \| c$ spectra are sepa rated for clarity. The experimental spectra were aligned with the calculated ones to match the peak at $5.5 eV$ for $E \| c$ . See the main text for discussion.

planar oxygen have to be offset due to a difference in the binding energy of the $1s$ level. This offset certainly depends on the difference in screening of core hole created during the excitation process. It is also sensitive to the values of atomic-sphere radii used in the calculation (which are never selected in a unique way). It seems that the offset values 2.22, 2.10, and 2.21 eV, which we obtained in our calculations in cases (i), (ii), and (iii), respectively, are too large. We used, therefore, the experimentally estimated offset$^{42,41}$ of 0.3 eV in all three calculations. Partial DOS were convoluted with a Lorentzian distribution using the energy-dependent parameter $\Gamma_{\text{FWHM}} = 0.4 + 0.08(E - E_{\text{threshold}})$ (in eV) to account for lifetime effects and with a Gaussian distribution with parameter $\Gamma_{\text{FWHM}} = 0.3$ eV to simulate instrumental broadening. $^{43}$ (FWHM denotes full width at half maximum.) Comparing calculated spectra with the experiment in Fig. 7, one can easily see a drastic disagreement in cases (a) and (b). (Using the offset of apex and planar oxygen contributions as the adjustable parameter does not lead to an improvement in these cases.) In Fig. 7(c), however, we obtained an essential improvement in the description of absorption spectra. A strong leading peak in the $\mathbf{E}\perp\mathbf{c}$ spectrum corresponds to planar oxygen $p\sigma$ states in the UHB, while a small leading peak in the $\mathbf{E}\parallel\mathbf{c}$ spectrum corresponds to 3.8% of the $p\sigma$ apex oxygen contribution to this band. [Compare the middle panel of Fig. 5(b) and the lowest panel of Fig. 6(b).] The remaining discrepancy can be explained in the following way. First of all, note that we align the experimental curves with calculated ones to match the wide structure and the peak at 5.5 eV in particular. This is to stress that the positions of the leading peaks are not reproduced exactly. Had we obtained the UHB at energy higher by 0.6 eV (i.e., the gap of 2.25 eV instead of 1.65 eV), we would have had perfect agreement here. We estimated that this would require us to use a value of $U$ for Cu $d$ states larger by about 1.2 - 1.6 eV than the one taken from Ref. 20. Second, it is expected that the effect of the core hole in the O $1s$ orbital, when included in the calculation, should shift the intensity within the broad structures located between 3 and 8 eV towards lower energy. $^{44}$ This will further fill in the space between the leading peaks and these structures. It will also enhance the details of these structures at the lower energy shoulders (for both $\mathbf{E}\perp\mathbf{c}$ and $\mathbf{E}\parallel\mathbf{c}$, however, possibly in a slightly different way). Finally, we mention that the $\parallel$ to $\perp$ intensity ratio of the leading peaks estimated from experimental data of Ref. 42 is 13 - 14% and 10% is given in Ref. 41 as the ratio of $\parallel$ to both $\parallel$ + $\perp$ intensity. Our value is 11% for the $\parallel$ to $\perp$ ratio [or 10% for the $\parallel$ to ($\parallel$ + $\perp$) ratio]. (See the analysis of the UHB composition above.) Having these three points in mind we conclude that the agreement with experiment in Fig. 7(c) is very good.

After enumerating a number of features of our LSDA+$U$ results, which gave the essential progress over the standard LSDA calculation when comparing with the variety of experimental data, we again point out serious difficulties now in a context of valence photoemission of $\text{La}_2\text{CuO}_4$. Results of our calculation are given in Fig. 8.

![](./images/812738279832027136_8.jpg)

FIG. 8. Valence photoemission of $\text{La}_2\text{CuO}_4$. The calculations included different photoionization cross sections for different contributing electrons. Background is not included. For more discussion see the main text.

We have taken into account different energy-dependent photoemission cross sections for different types of electrons Cu $3d$, O $2s$, and $2p$, and La $5p$ and $5d$. The realistic lifetime (Lorentzian) and instrumental (Gaussian) broadening were applied. (The procedure is the same as that in Ref. 14, but without background simulation.) Though one possibly can improve the one-particle simulation of the spectrum by taking into account also a coherent process (k-dependent matrix elements, i.e., amplitudes rather than cross sections), a comparison with the experimental curves in Figs. 1 and 2 in Ref. 45 clearly shows serious discrepancies. In our result the main photoemission "line" is much too wide (about 2.5 eV) and we cannot reproduce the satellite at about $-12$ eV.

This deficiency is directly related to characteristic multiconfigurational behavior of strongly correlated systems as (late) transition-metal oxides. On the base of the many-body model Hamiltonian cluster calculations$^{46,47}$ (which can explain the shape of spectrum) it is known that the satellite and the main line narrowing are caused by the "additional" hybridization of the $d^8$ configuration with the dominating $d^9\underline{L}$ one and due to the multiplet splitting of $d^8$. We described above the origin of this "additional" hybridization when we discussed the nature of the top of the valence band. Then the final shape of the spectrum is affected by quantum interference between different configurations, which is known as the spectral weight transfer problem. In our LSDA+$U$ calculation states from the $d^8$ configuration are located at about $-7$ eV. The additional hybridization will push these states out of the valence band (like in the case of impurity states embedded in the wide band). Part of them will be pushed down to about $-12$ eV (satellite line) and part up to (perhaps out of) the top of valence band giving valence band narrowing and the "Zhang-Rice singlet states" if the hybridization is large enough. $^{48}$

We tackled this problem in a previous work$^{22}$ in the test case of photoemission of NiO. Though we manage to obtain the correct satellite position and the main band narrowing, we did not obtain progress when the problem of spectral weight transfer is concerned. This is beyond a one-particle picture since in the real many-body situation the one-electron removal spectral weights are determined by the overlap integrals of type $\langle\Psi_i^{N-1}|d_i\Psi_G^N\rangle$. These integrals are related to the fractional parentage coefficients

in atomic spectroscopy (and should not be confused with, say, dipole transition matrix elements).

All these difficulties are left out here and our valence photoemission spectrum remains in rather poor agreement with the experiment.

### B. LaCuO₃

The LaCuO₃ compound is not as well known and widely studied as La₂CuO₄. It has attracted researchers' attention only recently (see Refs. 49-51 and references therein). In some early studies⁵² LaCuO₃ was seen as a "good model for the cuprate superconductors" because its basic building block (CuO₆ octahedron) is the same as that in La₂CuO₄. Since then, however, there is no evidence of superconductivity found in the extensive search over many La₁₋ₓMₓCuO₃ compounds.⁵⁰ It seems that the essential factor here is that LaCuO₃ has a 3D network of O-Cu-O bonds contrary to the 2D (planar) structure of (all) high-Tc superconductors. Large uncertainty remains in the literature when electric and magnetic properties of LaCuO₃ are concerned. This is probably due to the difficult sample preparation and uncertainty about oxygen deficiency.⁵⁰,⁵¹ There are reports in the literature that LaCuO₃ has poor metallic conductivity,⁵³,⁵¹ but there are also reports of insulating behavior⁴⁹ and semiconducting behavior for a fully stochiometric tetragonal phase (see Ref. 51 and references therein). Where magnetic properties are concerned suggestions were presented that LaCuO₃ is an antiferromagnet, a Pauli paramagnet, an antiferromagnet with ferromagnetic canting, as well as a Cu³⁺ low spin nonmagnetic compound (see Refs. 50 and 51 and references therein).

In our systematic study we have performed a series of band structure calculations. First, we used the smallest possible, tetragonal perovskite cell (symmetry P4/mmm) with lattice parameters $a = 3.81875$ Å and $c = 3.97271$ Å (Ref. 49) and carried out the calculation by the standard LSDA. Then in order to allow for possible AF ordering in Cu-O planes similar to that in La₂CuO₄ we constructed a $\sqrt{2} \times \sqrt{2} \times 2$ supercell. The resulting structure (also tetragonal) belongs to the $D_{4h}^{17}$ (I4/mmm) space group with atoms in the following Wyckoff positions: Cu in 2a and 2b, La in 4d, apex O in 4e with $z = 0.25$ and planar O in 8h with $x = 0.25$. Using this supercell we first repeated the standard LSDA calculations but now introducing initial AF spin polarization. We observed that magnetic polarization is quickly vanishing and the system converges to exactly the same nonmagnetic solution as that obtained in a smaller tetragonal cell. Then we carried out the calculation using our LSDA+$U$ method obtaining a stable AF insulating solution with an energy gap of 0.95 eV and a local moment $\mu_{\text{Cu}} = 0.98\mu_{B}$.

Before we give a full report of our results we will add some more details about the calculations. Applying the same criterion as in the case of La₂CuO₄ we selected atomic-sphere radii to be (in angstroms) 0.83 for Cu, 1.63 for La, and 1.40 for both planar and apex oxygen. Note that the Cu sphere is smaller than the one used in La₂CuO₄ since the Cu³⁺ ion is smaller than the Cu²⁺ one. This reflects a difference of nominal valency of Cu in these compounds. The space filling was improved by allocating empty atomic spheres at Wyckoff positions 4c and 8f with radii 0.70 and 0.61, respectively. The basis set we used for LaCuO₃ included the same augmented-spherical waves as for La₂CuO₄. In general all technical steps of the calculations for LaCuO₃ followed closely those for La₂CuO₄ and we maintained the same level of accuracy. Finally, we used the same values of on-site Coulomb and exchange parameters for Cu $d$ and La $f$ states as in La₂CuO₄. Obviously some of these values may differ slightly in these two cases, but we are convinced that the influence on the physical content of the solution will be very small.

Results for LaCuO₃ are presented below in a way similar to those for La₂CuO₄ in Sec. III A. Much less experimental data is available, however, for LaCuO₃, so our results should be seen rather as predictions and explanation of the electronic structure of this material. (We also will not show and/or discuss results of the intermediate version of the Hamiltonian.) We will stress similarities and differences relative to La₂CuO₄.

In Fig. 9 we show the overall DOS of LaCuO₃. The figure is organized as Fig. 1 for La₂CuO₄. The assignment of semicore O 2s and La 5p states remains the same. A large shift of La 4f states is also clearly visible. In this case, however, there are no experimental data (e.g., inverse photoemission) available to confirm the position of La 4f states. The important difference with respect to La₂CuO₄ is that the shapes of the local DOS for apex and planar oxygen are nearly the same in the whole energy range. This reflects the simple fact that the tetragonal deviation from the cubic perovskite is rather small and all oxygen atoms are almost equivalent. It means that (contrary to La₂CuO₄) both types of oxygen will nearly equally contribute to the UHB that is separated [Fig. 9(b)] from the top of the mostly oxygen valence band by a charge transfer gap of 0.05 eV. Although it is not explicitly visible in Fig. 9 (but it will be explicit below) it further means that, contrary to La₂CuO₄, both Cu $d_{x^2-y^2}$ and $d_{z^2}$ orbitals undergo Hubbard splitting. We point out here that our solution is essentially different from the model proposed recently by Bringley et al.⁵¹ In their model the $d_{z^2}$ band is completely filled and does not undergo Hubbard splitting. We will return to this problem.

Since there are no published detailed results of the band structure calculation for LaCuO₃,⁵⁴ before we continue with our main presentation, we include a small paragraph reporting the standard LSDA calculation for this compound. In Fig. 10 we show the band structure obtained with the smallest tetragonal perovskite unit cell. LaCuO₃ appears here as a nonmagnetic metallic system. Bands crossing the Fermi energy are formed by antibonding Cu $d_{x^2-y^2}$ - planar O $2p\sigma$ and Cu $d_{z^2}$ - apex O $2p\sigma$ orbitals. The Fermi surface is presented in Fig. 11. It consists of two sheets. One resembles a shape of octahedrons centered at $\Gamma$ points and connected by necks in the $z$ directions, but only touching other octahedrons at $X$ points in the $xy$ plane. The second sheet forms closed pockets of holes around $A$ points. In Table IV we listed the local partial charges within atomic

![](./images/812738279832027136_9.jpg)

FIG. 9. Total DOS (two molecules in unit cell) and lo- cal DOS on different atomic sites for $LaCuO_3$: (a) metallic nonmagnetic solution by standard LSDA; (b) insulating AF solution by modified LSDA+$U$ Hamiltonian [Eq. (10)]. The zero of energy is set to the Fermi energy in (a) and to the top of valence band in (b). Note the strong modification of the valence Cu $3d$ and O $2p$ states and the shift of unoccupied La $4f$ states when going from (a) to (b).

![](./images/812738279832027136_10.jpg)

FIG. 10. Electronic band structure of $LaCuO_3$ as ob- tained by the standard LSDA plotted within the simple tetragonal BZ corresponding to the smallest tetragonal per- ovskite unit cell. The zero of energy is set to the Fermi energy. The semicore O $2s$ and La $5p$ bands are not shown.

spheres which with some caution can be interpreted as occupation numbers. The total DOS at $E_f$ is equal to 2.4 states/eV.

Returning to our primary presentation, in Fig. 12 we compare the band structure of $LaCuO_3$ obtained with our LSDA+$U$ method (b) with the standard one, but now plotted within a $\sqrt{2} \times \sqrt{2} \times 2$ supercell for consis tency (a). (Of course, the latter one represents the same electronic structure as that in Fig. 10 and all the DOS and partial DOS obtained from these two band structures are exactly the same.) Figure 12 is organized in the same way as Fig. 2 for $La_2CuO_4$. Comments about the shift of La $4f$ states remain equally valid. An important dif- ference is that we have now [in (b)] two split up Hubbard bands and that they are well separated from each other.(In cubic perovskite they would be degenerate at the $\Gamma$ point.) This separation becomes important in the discus- sion of transport properties of $n$-doped $LaCuO_{3-\delta}$ given below. The indirect gap is equal to 0.95 eV, but a direct one is about 2 eV everywhere in the BZ. As in the case of $La_2CuO_4$ one should look simultaneously at the projec- tions of the local partial DOS of Cu $3d$ and planar and apex O $2p$ states on the symmetry components. These

![](./images/812738279832027136_11.jpg)

FIG. 11. Two sheets of the Fermi surface of $LaCuO_3$ as obtained by the standard LSDA. Shadowed regions are occu- pied by electrons.

<table>
<caption>TABLE IV. Partial charges in atomic spheres for LaCuO₃ as obtained by the standard LSDA calculation.</caption>
<tbody><tr>
<td colspan="2">Cu</td>
<td colspan="2">Planar O</td>
<td colspan="2">Apex O</td>
<td colspan="2">La</td>
</tr>
<tr>
<td>4s</td>
<td>0.07</td>
<td>2s</td>
<td>1.97</td>
<td>2s</td>
<td>1.97</td>
<td>6s</td>
<td>0.12</td>
</tr>
<tr>
<td>4p</td>
<td>0.08</td>
<td>2p σ</td>
<td>1.601</td>
<td>2p σ</td>
<td>1.615</td>
<td>5p</td>
<td>5.88</td>
</tr>
<tr>
<td>3d xy</td>
<td>1.789</td>
<td>π∥</td>
<td>1.805</td>
<td>πₓ</td>
<td>1.790</td>
<td>5d</td>
<td>0.63</td>
</tr>
<tr>
<td>yz</td>
<td>1.787</td>
<td>π⊥</td>
<td>1.794</td>
<td>πᵧ</td>
<td>1.790</td>
<td>4f</td>
<td>0.25</td>
</tr>
<tr>
<td>zx</td>
<td>1.787</td>
<td>3d</td>
<td>0.25</td>
<td>3d</td>
<td>0.21</td>
<td>
</td>
<td>
</td>
</tr>
<tr>
<td>z²</td>
<td>1.430</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
</tr>
<tr>
<td>x²−y²</td>
<td>1.331</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
</tr>
</tbody>
</table>

![](./images/812738279832027136_12.jpg)

FIG. 12. Electronic band structure of LaCuO₃. The figure is organized as Fig. 2. Note the upward shift of La 4f bands when going from (a) to (b) and the two split up Hubbard bands in (b). The lower UHB is separated from the valence bands by an indirect gap of 0.95 eV. Points in the BZ are labeled as in Ref. 55.

![](./images/812738279832027136_13.jpg)

FIG. 13. Cu d partial DOS in LaCuO₃. The figure is organized as Fig. 4. Deviation from cubic symmetry is very small in both cases (a) and (b). Although $d_{x²−y²}$ and $d_{z²}$ states show equal Hubbard splitting (about 8 eV), they contribute differently to two UHB's (compare Fig. 12). See the main text for a simultaneous discussion of Figs. 13-15.

are given in Figs. 13-15.

First, we observe that the deviation from cubic symmetry is very small. The degeneracy of $xy, yz, zx$ and $x^2-y^2, z^2$ states in Fig. 13 is barely lifted and shapes of planar and apex O $2p\sigma$ and $2p\pi$ states are the same in the whole energy range in Figs. 14 and 15, respectively. As a consequence, contrary to $La_2CuO_4$, both $d_{x^2-y^2}$ and $d_{z^2}$ states equally contribute to the Fermi energy region [Fig. 13(a)] and they show nearly the same Hubbard splitting [Fig. 13(b)]. In the latter case local moment $\mu_{Cu}=0.98\mu_B$ comes equally from $d_{x^2-y^2}$ ($0.48\mu_B$) and from $d_{z^2}$ ($0.5\mu_B$) orbitals. The small though important difference one should observe is that the $d_{z^2}$ orbital is contributing much more to the lower band from two split up upper Hubbard bands. This will be relevant for the discussion of transport properties of $n$-doped $LaCuO_{3-\delta}$.

Next, the overall upward shift of occupied O $2p$ states and downward shift of occupied Cu $d$ states when going from case (a) to case (b) is much less pronounced than in $La_2CuO_4$. Nevertheless, the formation of the charge transfer gap is apparent. Further analysis shows hybridization between Cu $d_{xy}$ and planar O $2p\pi_{\parallel}$ orbitals and between Cu $d_{yz,zx}$ and both apex O $2p\pi_{x,y}$ and planar $\pi_{\perp}$ orbitals. This effect is stronger in the LSDA+$U$ solution and the resulting states are located in energy range $-7$ to $-3.5$ eV. Moreover, there is significant direct oxygen $\pi$-$\pi$ hybridization of states located between $-3.5$ eV and the top of the valence band in the LSDA+$U$ solution and between $-4$ eV and about $-1.5$ eV in the standard LSDA solution. This effect is equally pronounced in both cases.

Finally, when unoccupied oxygen states are concerned we would like to make two points. First, we again point out that the upward shift of La $4f$ states (by about 5 eV) is reflected in the oxygen local DOS by a shift of sharp peaks located at 3.5 eV in the standard LSDA solution to about 9 eV in the LSDA+$U$ solution. Second, states in the wide structure ranging from 4 eV up to 9 eV in all O $2p\pi$ partial DOS are nearly equally hybridized with empty La $5d$ states located in that energy range.

![](./images/812738279832027136_14.jpg)

FIG. 14. Planar O $2p$ partial DOS in $LaCuO_3$. The figure is organized as Fig. 5. See the main text for simultaneous discussion of Figs. 13-15.

![](./images/812738279832027136_15.jpg)

FIG. 15. Apex O $2p$ partial DOS in $LaCuO_3$. The figure is organized as Fig. 14. See the main text for simultaneous discussion of Figs. 13-15.

We close this section by discussing transport properties of $LaCuO_{3-\delta}$ for $0 \leq \delta \leq 0.5$. We refer here to the experimental evidence reported in Ref. 51 and we will compare our interpretation with the model depicted in Fig. 8 therein. Describing results of our LSDA+$U$ calculation we pointed out energetic separation of two UHB's and the fact that the lower from them is dominated by apex O $\sigma$-Cu $d_{z^2}$ contribution. Since oxygen vacancies are acting as double donors, this Hubbard subband will become quickly populated when $\delta$ increases. The system will appear as metallic, though with poor conductivity due to the small mobility of carriers in the narrow band. Moreover, doping of a Hubbard subband is not at all a rigid filling process. During the electron doping, states are transferred from the upper (empty) Hubbard band to the lower one and the UHB just disappears. Such a process, which is beyond a standard band picture, could possibly be described by a combination of the LSDA+$U$ and the coherent potential approximation (CPA), which is widely used in the theory of alloys. (We would like to recall here that the approach, which in the theory of alloys is called CPA, was introduced by Hubbard$^{56}$ for the description of motion of an extra electron or hole through a half-filled narrow band in a strongly correlated system.) $LaCuO_{3-\delta}$ should behave as a poor metal (semiconductor) with decreasing numbers of carriers as $\delta$ increases. When $\delta$ reaches 0.5 all the bands, except the planar $\sigma$-Cu $d_{x^2-y^2}$ (second) UHB, are completely filled and the system again becomes insulating. Our model is clearly presented in Fig. 16. (Compare with Fig. 8 in Ref. 51.) Summarizing, our model predicts $LaCuO_{3-\delta}$ to be an insulator for the ideal stochiometric tetragonal phase ($\delta=0$) (contrary to the model in Ref. 51), a poor metal (doped semiconductor) for $0 \leq \delta \leq 0.5$, and again an insulator for $\delta=0.5$. This seems to be in full agreement with experimental evidence collected by Bringley et al. in Ref. 51. (It is extremely difficult to prepare a stochiometric tetragonal phase without oxygen vacancies. This probably explains why $LaCuO_3$ was mostly reported to be metallic.)

![](./images/812738279832027136_16.jpg)

FIG. 16. Model proposed of the electronic structure of $LaCuO_{3-\delta}$ upon an increase in oxygen deficiency $\delta$. (pl = planar, ax = apex, LH, UH = lower, upper Hubbard subbands.) The transfer of states from the UHB to the LHB upon doping (as indicated by the arrow) results in the disappearance of the upper band and "growth" of the lower one. This is depicted by the change of the horizontal size of relevant boxes (apex O $2p\sigma$ - Cu $d_{z^2}$).

When magnetic properties are concerned, $LaCuO_3$ is antiferromagnetic in the LSDA+$U$ solution. It remains antiferromagnetic in all ranges of $\delta$ according to our interpretation of the $n$-doping process, in particular for $\delta=0.5$, as was observed experimentally. For intermediate $\delta$ values it is very likely that some ferromagnetic component will develop due to disorder and moments canting. We stress strongly, however, that neither our calculations nor our model of the doping process say anything about the ratio of long-range order for the finite temperatures.

## IV. SUMMARY
In Sec. II we presented, modified in its physical meaning and also technically extended, a version of the so-called LDA+$U$ method of including an on-site Coulomb correlation (the essential part) to the effective Hamiltonian of the local-density approximation to the density functional. We distinguished our method by the label LSDA+$U$ because the original formulation intrinsically does not allow for spin polarization in the DF part of the Hamiltonian.

In Sec. III we reported extensively and discussed carefully results of the electronic-structure calculation for $La_2CuO_4$ and $LaCuO_3$ carried out by the LSDA+$U$ method. The most important features of our solution for $La_2CuO_4$ are (i) a stable AF insulating solution with the correct value of the Cu local moment, (ii) the moment carried entirely by the $d_{x^2-y^2}$ orbital, (iii) a charge transfer gap with the correct value, (iv) a correct position of La $4f$ states and a correct description of inverse photoemission, (v) a correct description of polarization-dependent x-ray absorption at the oxygen $K$ edge including details of $\mathbf{E} \parallel c$ and $\mathbf{E} \perp c$ anisotropy, and also the following serious difficulties: (vi) the incorrect nature of the first ionization states (the ratio of in-plane and out-of-plane contributions), and (vii) a poor reproduction of valence photoemission. Both of these difficulties [(vi) and (vii)] are directly related to the problem of an incorrect treatment of the configuration hybridization and (vii) also to the "lack" of treatment of the spectral weight transfer. We discussed some possibilities (and attempts) to improve upon points (vi) and (vii). We consider these problems as important because they show the essence of (many-body) strong electron-electron correlation and also as difficult ones because any successful treatment (if ever possible) will certainly spoil the simplicity and wide applicability of the effective one-particle approach.

Where $LaCuO_3$ is concerned few experimental data are available, so results of our calculations should be considered rather as predictions. Inspired by our LSDA+$U$ solution, we constructed a model which gives a full explanation of insulator-metal-insulator transitions upon $n$ doping.

On the basis on our results and on those obtained with the simpler form of the modified Hamiltonian$^8$ we claim that the method using the effective potential in the form of Eq. (10) offers a significant improvement over the standard LSDA calculations when dealing with the electron-electron correlations of localized orbitals embedded in delocalized electron systems. The LSDA+$U$ method deliv-

ers an essentially better approximation to the electron-removal and electron-addition spectra, which is crucial for the interpretation of the majority of (spectroscopy) experiments. Finally, it requires only a minor increase of computational effort over the standard LSDA, which is very important for the materials science where we need efficient tools to handle more and more complex systems.

## ACKNOWLEDGMENTS

We would like to thank M.A. Oleś and F. Barriquand for useful discussion. This work was supported by the Netherlands Foundation for Fundamental Research on Matter (FOM), the Netherlands Foundation for Chemical Research (SON), the Netherlands Organization for the Advancement of Pure Research (NWO), and the Committee for the European Development of Science and Technology (CODEST) program.

## APPENDIX

The general expressions for Coulomb and exchange electron-electron interaction matrices in the case of equivalent $nl$ electrons assume a relatively simple form. We reproduce them here after Ref. 18. They read

$$
U_{m m^{\prime}}^{l}=\sum_{k=0}^{2 l} a_{m m^{\prime}}^{l k} F^{k}, \tag{A1}
$$

$$
J_{m m^{\prime}}^{l}=\sum_{k=0}^{2 l} b_{m m^{\prime}}^{l k} F^{k}, \tag{A2}
$$

where $F^{k}$ are Slater integrals for a given $nl$ and

$$
a_{m m^{\prime}}^{l k}=c^{k}(l m, l m) c^{k}\left(l m^{\prime}, l m^{\prime}\right), \tag{A3}
$$

$$
b_{m m^{\prime}}^{l k}=\left[c^{k}\left(l m, l m^{\prime}\right)\right]^{2}, \tag{A4}
$$

where

$$
c^{k}\left(l m, l^{\prime} m^{\prime}\right)=\left(\frac{4 \pi}{2 l+1}\right)^{\frac{1}{2}} \int d \Omega Y_{l m}^{*} Y_{k m-m^{\prime}} Y_{l^{\prime} m} \quad (\mathrm{~A} 5)
$$

are known as Gaunt's numbers. $^{57}$ Equation (A5) provides also a relation to the much more common Clebsch-Gordan coefficients. $^{58}$

It is rather cumbersome to verify the following two summation relations. The first of them is

$$
\sum_{m m^{\prime}} U_{m m^{\prime}}^{l}=(2 l+1)^{2} F^{0}=(2 l+1)^{2} U. \tag{A6}
$$

Here and everywhere in this work we identify the atomic Slater integral $F^{0}$ with the screened (in solid), effective Coulomb interaction parameter $U$ for a given $nl$ (i.e., $F_{\text {eff }}^{0} \equiv U$ ). Note that we use here the index $l$ explicitly for $U$ and $J$ matrices to stress this dependence, but we still drop this index in the case of $U$ and $J$ parameters and Slater integrals. Next, we recall the relation

$$
\begin{aligned}
& J=\frac{1}{14}\left(F^{2}+F^{4}\right) \text { for } l=2, \\
& J=\frac{1}{6435}\left(286 F^{2}+195 F^{4}+250 F^{6}\right) \text { for } l=3,
\end{aligned} \quad (\mathrm{~A} 7)
$$

known in the field of atomic spectroscopy. The second useful summation relation can be written as

$$
\sum_{m m^{\prime}}\left(U_{m m^{\prime}}^{l}-J_{m m^{\prime}}^{l}\right)=2 l(2 l+1)(U-J). \tag{A8}
$$

These summation relations were used in Sec. II B.

$^{1}$ Theory of the Inhomogeneous Electron Gas, edited by S. Lundqvist and N.H. March (Plenum, New York, 1983).
$^{2}$ G.D. Mahan and K.R. Subbaswamy, Local Density Theory of Polarizability (Plenum, New York, 1990).
$^{3}$ R.O. Jones and O. Gunnarsson, Rev. Mod. Phys. 61, 689 (1989).
$^{4}$ W.E. Pickett, Rev. Mod. Phys. 62, 433 (1989).
$^{5}$ D.C. Langreth and J.P. Perdew, Phys. Rev. B 21, 5469 (1980); D.C. Langreth and M. J. Mehl, ibid. 28, 1809 (1983); J.P. Perdew and Y. Wang, ibid. 33, 8800 (1986).
$^{6}$ J.P. Perdew and A. Zunger, Phys. Rev. B 23, 5048 (1981).
$^{7}$ J.P. Perdew, in Advances in Quantum Chemistry, edited by S.B. Trickey (Academic, New York, 1990), Vol. 21, p. 113, and references therein.
$^{8}$ V.I. Anisimov, J. Zaanen, and O.K. Andersen, Phys. Rev. B 44, 943 (1991).
$^{9}$ J.P. Perdew, R.G. Parr, M. Levy, and J.L. Balduz, Jr., Phys. Rev. Lett. 49, 1691 (1982).
$^{10}$ A.R. Williams, J. Kübler, and C.D. Gelatt, Jr., Phys. Rev. B 19, 6094 (1979).
$^{11}$ M.T. Czyżyk, R.A. de Groot, G. Dalba, P. Fornasini, A. Kisiel, F. Rocca, and E. Burattini, Phys. Rev. B 39, 9831 (1989); J. Ghijsen, L.H. Tjeng, J. van Elp, H. Eskes, J. Westerink, G.A. Sawatzky, and M.T. Czyżyk, ibid. 38, 11322 (1988); M. Grioni, M.T. Czyżyk, F.M.F. de Groot, J.C. Fuggle, and B.E. Watts, ibid. 39, 4886 (1989); M.T. Czyżyk and R.A. de Groot, in Proceedings of the Second European Conference on Progress in X-Ray Synchrotron Radiation Research Research, Rome, Italy, 1989, edited by A. Balerna, E. Bernieri, and S. Mobilio (Italian Physical Society, Bolonia, 1990), p. 47; P.J.W. Weijs, M.T. Czyżyk, J.F. van Acker, W. Speier, J.B. Goedkoop, H. van Leuken, H.J.M.Hendrix, R.A. de Groot, G. van der Laan, K.H.J. Buschow, G. Wiech, and J.C. Fuggle, Phys. Rev. B 41, 11899 (1990).
$^{12}$ H. van Leuken, A. Lodder, M.T. Czyżyk, F. Springelkamp, and R.A. de Groot, Phys. Rev. B 41, 5613 (1990).
$^{13}$ M.T. Czyżyk, K. Lawniczak-Jabłońska, and S. Mobilio, Phys. Rev. B 45, 1581 (1992).
$^{14}$ M.T. Czyżyk, R. Potze, and G.A. Sawatzky, Phys. Rev. B 46, 3729 (1992).
$^{15}$ O.K. Andersen, Phys. Rev. B 12, 3060 (1975); H.K. Skriver, The LMTO Method (Springer-Verlag, Berlin, 1984).
$^{16}$ O.K. Andersen and O. Jepsen, Phys. Rev. Lett. 53, 2571 (1984).
$^{17}$ E.U. Condon and G.H. Shortley, The Theory of Atomic Spectra (Cambridge University Press, Cambridge, 1953).
$^{18}$ J.S. Griffith, The Theory of Transition-Metal Ions (Cam-

bridge University Press, Cambridge, 1961).

19A.M. Oles and G. Stollhoff, Phys. Rev. B 29, 314 (1984).

20J.B. Grant and A.K. McMahan, Phys. Rev. B 46, 8440 (1992).

21M.M. Steiner, R.C. Albers, and L.J. Sham, Phys. Rev. B 45, 13272 (1992).

22V.I. Anisimov, I.V. Solovyev, M.A. Korotin, M.T. Czyżyk, and G.A. Sawatzky, Phys. Rev. B 48, 16929 (1993).

23A.K. McMahan, R.M. Martin, and S. Satpathy, Phys. Rev. B 38, 6650 (1988).

24O. Gunnarsson, O.K. Andersen, O. Jepsen, and J. Zaanen, Phys. Rev. B 39, 1708 (1989).

25M.S. Hybertsen, and M. Schlüter, Phys. Rev. B 39, 9028 (1989).

26A.K. McMahan, J.F. Annett, and R.M. Martin, Phys. Rev. B 42, 6268 (1990).

27One should be a bit careful when comparing the values of $U$ reported in the literature, because of the different, often only implicitly assumed, conventions which are used. All values obtained by constrained-LDA calculations involving the atomic-sphere (muffin-tin) approximation should be identified with the screened Slater monopole integral $F_{\text{eff}}^{0}$. We do so; see the Appendix. The diagonal values of the Coulomb interaction $U_{mm}$, $m=x^{2}-y^{2},3z^{2}-r^{2},xy$, etc., are, however, different. In terms of Racah $A,B$, and $C$ parameters they read $U_{d}\equiv F_{\text{eff}}^{0}=A+7/5C$ and $U_{mm}=A+4B+3C$. As an example, $U_{d}=7.42$ eV in Ref. 26 and $U(d_{x^{2}-y^{2}})=8.96$ eV in Ref. 20 are in fact the same. Of course, values of $B$ and $C$ have to be known. The authors of references used in this example did not confuse that matter, but it seems that ambiguity about these values exists in the literature.

28V.I. Anisimov, M.A. Korotin, J. Zaanen, and O.K. Andersen, Phys. Rev. Lett. 68, 345 (1992).

29V.I. Anisimov (private communication).

30C.E. Moore, Atomic Energy Levels, Natl. Bur. Stand. (U.S.), Circ. No. 467 (U.S. GPO, Washington, D.C., 1958), Vols. 1-3.

31H. Eskes, L.H. Tjeng, and G.A. Sawatzky, Phys. Rev. B 41, 288 (1990).

32H. Eskes and G.A. Sawatzky, Phys. Rev. B 44, 9656 (1991).

33F.M.F. de Groot, J.C. Fuggle, B.T. Thole, and G.A. Sawatzky, Phys. Rev. B 42, 5459 (1990).

34J.B. Mann, Atomic Structure Calculations, Los Alamos Scientific Laboratory Reports No. LASL-3690 (1967) (unpublished).

35S.L. Cooper, G.A. Thomas, A.J. Millis, P.E. Sulewski, J. Orenstein, D.H. Rapkine, S.-W. Cheong, and P.L. Trevor, Phys. Rev. B 42, 10785 (1990).

36J. Zaanen, G.A. Sawatzky, and J.W. Allen, Phys. Rev. Lett. 55, 418 (1985).

37F. Barriquand and G.A. Sawatzky (unpublished).

38E. Manousakis, Rev. Mod. Phys. 63, 1 (1991).

39Y. Gao, T.J. Wagener, J.H. Weaver, A.J. Arko, B. Flandermeyer, and D.W. Capone II, Phys. Rev. B 36, 3971 (1987).

40F.C. Zhang, and T.M. Rice, Phys. Rev. B 37, 3759 (1988).

41E. Pellegrin, N. Nücker, J. Fink, S.L. Molodtsov, A. Gutiérrez, E. Navas, O. Strebel, Z. Hu, M. Domke, G. Kaindl, S. Uchida, Y. Nakamura, J. Markl, M. Klauda, G. Saemann-Ischenko, A. Krol, J.L. Peng, Z.Y. Li, and R.L. Greene, Phys. Rev. B 47, 3354 (1993). The experimental spectra presented in Fig. 7 differ slightly from those published by Pellegrin et al. We used spectra which were corrected for the self-absorption effect and which were kindly provided to us by E. Pellegrin after publication.

42C.T. Chen, L.H. Tjeng, J. Kwo, H.L. Kao, P. Rudolf, F. Sette, and R.M. Fleming, Phys. Rev. Lett. 68, 2543 (1992).

43We used such a broadening procedure successfully on many occasions. See, e.g., Refs. 11, 13, and 14.

44Such an expectation is based on our previous experience with self-consistent calculations of the core-hole effects on the XAS spectra in semiconductors and metals. See M.T. Czyżyk and R.A. de Groot, in Proceedings of the Second European Conference on Progress in X-Ray Synchrotron Radiation Research, Rome, Italy, 1989, p. 47; P.J.W. Weijs, M.T. Czyżyk, J.F. van Acker, W. Speier, J.B. Goedkoop, H. van Leuken, H.J.M. Hendrix, R.A. de Groot, G. van der Laan, H.J. Buschow, G. Wiech, and J.C. Fuggle, Phys. Rev. B 41, 11899 (1990).

45Z.-X. Shen, J.W. Allen, J.J. Yeh, J.-S. Kang, W. Ellis, W. Spicer, I. Lindau, M.B. Maple, Y.D. Dalichaouch, M.S. Torikachvili, J.Z. Sun, and T.H. Geballe, Phys. Rev. B 36, 8414 (1987).

46A. Fujimori, E. Takayama-Muromachi, Y. Uchida, and B. Okai, Phys. Rev. B 35, 8814 (1987).

47J. Ghijsen, L.H. Tjeng, J. van Elp, H. Eskes, J. Westerink, G.A. Sawatzky, and M.T. Czyżyk, Phys. Rev. B 38, 11322 (1988).

48H. Eskes and G.A. Sawatzky, Phys. Rev. Lett. 61, 1415 (1988).

49J.F. Bringley, B.A. Scott, S.J. La Placa, R.F.Boehme, T.M. Show, M.W. McElfresh, S.S. Trail, and D.E. Cox, Nature (London) 347, 263 (1990).

50A.W. Webb, E.F. Skelton, S.B. Qadri, V. Browning, and E.R. Carpenter, Jr., Phys. Rev. B 45, 2480 (1992).

51J.F. Bringley, B.A. Scott, S.J. La Placa, T.R. McGuire, F. Mehran, M.W. McElfresh, and D.E. Cox, Phys. Rev. B 47, 15269 (1993).

52K. Allan, A. Campion, J. Zhou, and J.B. Goodenough, Phys. Rev. B 41, 11572 (1990).

53G. Demazeau, C. Parent, M. Pouchard, and P. Hagenmuller, Mater. Res. Bull. 7, 913 (1972).

54The only band structure calculation of $LaCuO_{3}$ known to us is that reported without details by W.E. Pickett and H. Krakauer, Phys. Rev. B 35, 7252 (1987).

55Jaejun Yu, A.J. Freeman, and J.-H. Xu, Phys. Rev. Lett. 58, 1035 (1987).

56J. Hubbard, Proc. R. Soc. London Ser. A 281, 401 (1964).

57J.A. Gaunt, Philos. Trans. R. Soc. London Ser. A 228, 151 (1929).

58D.A. Varshslovich, A.N. Moskalev, and V.K. Khersonskii, Quantum Theory of Angular Momentum (World Scientific, Singapore, 1989).

![](./images/812738279832027136_17.jpg)

FIG. 11. Two sheets of the Fermi surface of $LaCuO_3$ as obtained by the standard LSDA. Shadowed regions are occupied by electrons.

![](./images/812738279832027136_18.jpg)

FIG. 16. Model proposed of the electronic structure of $LaCuO_{3-\delta}$ upon an increase in oxygen deficiency $\delta$. (pl = planar, ax = apex, LH, UH = lower, upper Hubbard subbands.)
The transfer of states from the UHB to the LHB upon doping (as indicated by the arrow) results in the disappearance of the upper band and "growth" of the lower one. This is depicted by the change of the horizontal size of relevant boxes (apex O $2p\sigma$ - Cu $d_{z^2}$).