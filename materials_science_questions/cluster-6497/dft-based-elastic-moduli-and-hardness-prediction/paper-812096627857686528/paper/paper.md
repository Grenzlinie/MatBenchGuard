Atoms embedded in an electron gas: the generalized gradient approximation

This content has been downloaded from IOPscience. Please scroll down to see the full text.

1997 Phys. Scr. 55 499

(http://iopscience.iop.org/1402-4896/55/4/022)

View the table of contents for this issue, or go to the journal homepage for more

Download details:

IP Address: 129.8.242.67
This content was downloaded on 26/07/2015 at 07:00

Please note that terms and conditions apply.

# Atoms Embedded in an Electron Gas: The Generalized Gradient Approximation

U. Yxklinten*, J. Hartford and T. Holmquist

Department of Applied Physics, Chalmers University of Technology and Göteborg University, S-412 96 Göteborg, Sweden

Received May 27, 1996; accepted September 17, 1996

## Abstract
The bonding properties of atoms are studied within the atom-in-jellium model. The emphasis is on a comparison between the widely used local- density approximation (LDA) and the generalized-gradient approximation (GGA-PW91) for the electron exchange and correlation interactions. The analysis shows that the GGA is more able to account for energy differences due to changes in electron density gradients (in mainly the valence shells), as the free atom is immersed into an electron gas, than the LDA. GGA lowers the energies for free atoms and thus reduces the overbinding present in LDA. Results are presented for a large fraction of the periodic system. The present work provide GGA basic parameters for the effective-medium theory (EMT), which is a glue-scheme method versatile for large systems of interacting atoms, and additional positive tests of the usefulness of GGA in density-functional calculations, showing it to pave the way towards chemi- cal accuracy.

## 1. Introduction
The prospects for constructive contributions to Science and Technology from Materials Theory have never been so bright as now. The rapid computer development allows suc- cessively more and more complex materials to be studied. The outburst of theoretical methods and further develop- ments of them provides an arsenal of tools for the descrip- tion of materials on many different levels.

For total-energy calculations, giving bonding, structural and elastic properties, a common denominator is the foun- dation provided by the density-functional theory (DFT) [1-3] that allows the calculation of ground-state properties of a many-electron system from a one-electron Schrödinger equation [4]. The latter equation has wellknown parts; kinetic energy, electrostatic interactions etc. In addition, there is a part that takes care of the many-electron inter- actions, the so-called exchange-correlation (XC) energy, $E_{xc}$. In practice, this is done in an approximate way. In the sim- plest account, in the local-density approximation (LDA) [4-6], the XC effects are described as in a homogeneous electron gas taken at the local density $n(r)$ of the studied inhomogeneous system. Now, as the Fermi statistics of the electrons and the Coulombic repulsions among them give basically non-local effects, many attempts have been made to extend the approximation for $E_{xc}$ to non-local depen dencies on the electron density $n(r)$. In a Taylor expansion the first non-trivial term involves the gradient of the density $n(r)$. Such a direct expansion does not work, but a successful gradient-corrected XC functional has been derived by Lan- greth and Mehl [7]. This and other experiences have been developed into the so-called generalized-gradient approx- imation (GGA) [8-10].

The LDA is known to give too weak binding of the core electrons in an atom and overbind atoms in molecules and solids. This is corrected for by considering the density gra- dient, and the GGA has been shown to provide a chemically useful accuracy in a number of applications [11-16]. As there have been several GGA:s published in the literature, we stress that we use the functional published in Ref. [10], denoted with GGA-PW91.

An atom embedded in a homogeneous electron gas("jellium") is a model system for solids, which has appealed to many theorists over the years and whose simplicity makes it possible to study the differences between the XC functionals in great detail. In this approach one focuses on a single atom and examines its interaction with a host of extended states. Each atom of a solid feels and responds to an environment. The latter may be considered in some approximate way, particularly in simple metals because of efficient electronic screening. Probably this line of thinking started with Wigner's and Seitz' study of the cohesion of alkali metals [17]. It has then reappeared in such models as cellular methods [18], spherical solids [19], the renormalized-atom model [20, 21], the atom-in- jellium model [22], and the the effective-medium theory(EMT) [24,25].

To explain the difference between the LDA and GGA we note that the charge relaxation as the atom is immersed in jellium (or solid) weakens the electron density gradients compared to the free atom. The LDA does not take the changes in gradients (particularly in the valence electron region) fully into account, whereas the GGA in comparison lowers the energy for the free atom because of its larger gra- dients, and thereby reduces the bonding strength. It is con- cluded that going from LDA to GGA give general improvements, in particular for embedded atoms with too strong binding in LDA. The GGA also increases the Wigner-Seitz radii of the alkali and 3d-metals from the too small LDA values.

Another motivation for this work is to provide GGA input parameters to the EMT, a so-called glue-scheme method. The scheme is derived in a systematic way from the Hohenberg-Kohn-Sham density functional for the electrons of a many-atom system. Like the above mentioned methods, it uses the idea of atomic cells. The density, $\bar{n}$, in one cell is the average of the density tails from the surrounding cells.

* Present address: Center for Atomic-scale Materials Physics and Physics Department, Technical University of Denmark, DK-2800 Lyngby, Denmark.

Physica Scripta 55

From self-consistent calculations on this model system one derives the immersion energy as a function of $\bar{n}$, the density distribution of the immersed atom, and the atom-induced density of states. Such calculations have been performed in the LDA by Puska, Nieminen, and Manninen [22] and in other XC approximations [23].

In Section 2 we present the essence of the theory used, both for the atom-in-jellium model and for the effective- medium theory. The results and discussion are given in Section 3 and in Section 4 we write some concluding remarks.

## 2. Theory
### 2.1. Atom in an electron gas
A number of properties of inhomogeneous electronic systems can be discussed from the viewpoint of an atom embedded in an electron gas, such as cohesive energies and bond lengths. In connection with the EMT it is used to derive parameters for the inter-atomic potentials [22-24].

The basic quantity we calculate is the immersion energy of an atom embedded in a homogeneous electron gas with electron density $\bar{n}$. This energy is defined as,
$$
\begin{aligned}
\Delta E^{\mathrm{hom}}(\bar{n}) & =E^{\text {atom }+ \text { jellium }}(\bar{n})-E^{\text {jellium }}(\bar{n})-E^{\text {atom }} \\
& =E^{\mathrm{emb}}(\bar{n})-E^{\text {atom }},
\end{aligned}
\tag{1}
$$
where $E^{\mathrm{emb}}(\bar{n})$ is the binding energy of the embedded atom, i.e. the total energy of the atom plus jellium relative to the energy of the jellium and the total energy of the free atom, $E^{\text {atom }}$. For a paramagnetic jellium the total energy of an embedded atom may be calculated with the spin- compensated formalism [4, 5], because electron shells that are partially filled in free atoms either become completed or merge into the continuum of the electron-gas states. The total energy of the free atom is calculated with the spin- decomposed formalism [6, 26, 27] that gives the same approximations for the electron exchange and correlation for a spin-compensated system as that used for the embed- ded atom.

The accuracy of the results from the Kohn-Sham equa- tions depends on the approximation of the functional for the electronic exchange-correlation effects. The widely used LDA is in principle valid for slowly and weakly varying densities. For physical systems, however, it is known to underbind the core-electrons in an atom and to overbind the atoms in a molecule or solid. Although not perfect, many deficiencies of the LDA and the local-spin-density approximation (LSDA) are removed by the GGA [10, 11]. It is derived via a real-space cut-off of the long-range part of the density-gradient expansion for the XC hole of the elec- tron and satisfies a number of sum rules. Older GGA:s have a wave-vector cut-off for the correlation, dependent on a semi-empirical parameter. The improvement in this new GGA is attributed to the non-spurious part of the gradient- expansion, that is, the XC hole is better described close to its origin compared to LDA, LSDA and older GGA:s.

The XC energy functionals are expressed in terms of the exchange-energy $(\epsilon_{\mathrm{x}}^{\mathrm{LDA}})$ of LDA, correlation-energy $(\epsilon_{\mathrm{c}}^{\mathrm{L} \mathrm{SDA}})$ of LSDA and correction functions with the density gra- dients. The GGA exchange-energy expression for a spin- polarized system is,
$$E_{\mathrm{x}}^{\mathrm{GGA}}[n]=\int \mathrm{d}^{3} r n(\boldsymbol{r}) \varepsilon_{\mathrm{x}}^{\mathrm{LDA}}(n) F(s),\tag{2}$$
where $s=|\nabla n| /(2 k_{\mathrm{f}} n)$ is the inhomogeneity parameter with the local Fermi wave-vector defined by $k_{\mathrm{f}}=(3 \pi n)^{1 / 3}$. The correlation-energy expression is,
$$E_{\mathrm{c}}^{\mathrm{GGA}}\left[n_{\uparrow}, n_{\downarrow}\right]=\int \mathrm{d}^{3} r n(\boldsymbol{r})\left[\varepsilon_{\mathrm{c}}^{\mathrm{L} \mathrm{SDA}}(n, \zeta)+H(t, n, \zeta)\right],\tag{3}$$
where $t \propto|\nabla n| / k_{\mathrm{f}}^{1 / 2}$ is another scaled gradient and $\zeta=(n_{\uparrow}$ $-n_{\downarrow}) / n$ is the local spin polarization. The functions $F$ and $H$ are determined from conditions imposed on the XC hole. Detailed forms of expressions (2) and (3) are given in Ref. [10].

The new GGA should be well suited for solid systems as well as for the atom-in-jellium, where the inhomogeneity parameter [$s$ in eq. (2)] never is much greater than unity [11, 23].

#### 2.1.1. Calculations.
The calculations closely follow those of Ref. [22]. Besides the implementation the GGA the orig- inal codes have been changed just with respect to tail cor- rections, in order to increase the stability of the code [28].

Solving the Kohn-Sham equations one obtains the one- electron energy-eigenvalue parameters and corresponding wavefunctions. Squaring the latter ones and summing them for all eigenstates with energies lower than the Fermi level yields the electron density $n(r)$. Calculating this density in the atom-in-jellium model, and subtracting the constant embedding density, $\bar{n}$, the atom-induced density, $\Delta n(r)$, is obtained. From this one can calculate the atom-induced electrostatic Hartree potential, $\Delta \phi(r)$. The electrostatic attraction between the atom and the electron background [which is canceled by the positive background in the calcu- lation of the immersion energy, eq. (1)] is,
$$-\bar{n} \int_{r \leqslant s} \mathrm{~d}^{3} r \Delta \phi(\bar{n}, r)=\bar{n}, r)=\bar{n} \alpha(\bar{n}),\tag{4}$$
where the integration is carried out over the neutral sphere of the atom, with radius $s$. This is defined as the sphere, where the total charge, that is, the integral of the electron density and the nuclear charge, vanishes. To better compare the atom-in-jellium and the EMT we chose to include the interaction in eq. (4) in the atom-in-jellium model. We then have the cohesive energy of an embedded atom as the sum of the immersion energy and the electrostatic attraction,
$$E_{\mathrm{c}}[\bar{n}]=\Delta E^{\mathrm{hom}}[\bar{n}]-\alpha(\bar{n}) \bar{n}.\tag{5}$$

There is a very good approximate exponential relation between the neutral radius and the embedding density [24],
$$\bar{n}(s)=n_{0} \mathrm{e}^{-\eta\left(s-s_{0}\right)},\tag{6}$$
where $n_{0}$ is the (optimum) embedding density at the minimum of the cohesive function eq. (5) and $s_{0}$ the corre- sponding neutral sphere.

The quantities $\Delta E^{\mathrm{hom}}(\bar{n}), \alpha(\bar{n}), E_{\mathrm{c}}(\bar{n}), \eta, n_{0}$ and $s_{0}$ are to be calculated and used both for the discussion of the atom-in- jellium model and for the total-energy expression of the EMT.

An interesting feature that can be seen in the embedding calculations is the broadening of an atomic level into a reso- nance, when the level lies in the continuum of jellium levels.

---
*Physica Scripta 55*

The atom-induced density of states (DOS), $\Delta D(\varepsilon)$, can be obtained from the scattering phase shifts, $\delta_{l}(\varepsilon)$, by [22],

$$
\Delta D(\varepsilon)=\frac{2}{\pi} \sum_{l} \frac{\partial \delta_{l}(\varepsilon)}{\partial \varepsilon}(2 l+1). \tag{7}
$$

This induced DOS allows for modelling of hybridization effects, for example, the d-d electron interaction in the transition metals [24].

To study the difference between the two XC approximations it is instructive to compare the relaxation charge density,

$$
\Delta n^{\mathrm{rel}}(r)=\Delta n(r)-n^{\mathrm{atom}}(r), \tag{8}
$$

which give a measure of the change in the electron screening of the nucleus, when the atom is immersed in the jellium. The change in XC energy due to the charge relaxation is given by

$$
\Delta e_{\mathrm{xc}}(r)=n(r) \varepsilon_{\mathrm{xc}}[n(r)]-\bar{n} \varepsilon_{\mathrm{xc}}[\bar{n}]-n^{\mathrm{atom}}(r) \varepsilon_{\mathrm{xc}}\left[n^{\mathrm{atom}}(r)\right]. \tag{9}
$$

Note that $\Delta e_{\mathrm{xc}}(r)$ is an energy density that may be plotted against radial distance to reveal spatial differences in the two XC functionals.

### 2.2. The effective-medium theory
The effective-medium theory (EMT) is a glue-type calculational scheme for the total energy of a system of interacting atoms [24, 25]. The simplicity of the scheme makes it able to deal with large systems and, equally important, it provides a simple physical picture. The total-energy expression is systematically derived within the DFT to the lowest order in density deviations. It consists of an electrondensity-dependent cohesive term (the pair-functional, $E_{\mathrm{c}}$) and corrections,

$$
E=\sum_{i} E_{\mathrm{c}, i}\left[\bar{n}_{i}\right]+\Delta E_{\mathrm{AS}}+\Delta E_{-\mathrm{el}}, \tag{10}
$$

where the sum is over the atoms in the system under study.

The cohesive term,

$$
E_{\mathrm{c}, i}\left[\bar{n}_{i}\right]=\Delta E_{i}^{\mathrm{hom}}\left[\bar{n}_{i}\right]-\alpha_{i}\left(\bar{n}_{i}\right) \bar{n}_{i}, \tag{11}
$$

is calculated in a reference system, that is, the atom $i$ immersed in a homogeneous electron gas [24] of proper density [c.f. eq. (5)]. The atom $i$ is related to its reference system by viewing each atom to be immersed in the electron gas set up by the density tails from neighbouring atoms, averaging up to $\bar{n}_{i}$. In this picture the electrostatic interaction $-\alpha_{i} \bar{n}_{i}$ is the attraction between the Hartree potential, eq. (4), of atom $i$ and the density tails sticking into its neutral sphere.

The cohesive function (11), with a minimum of $E_{0}$ at some optimum embedding density, $n_{0}$, may be parameterized as [24]

$$
E_{\mathrm{c}}\left(\bar{n}_{i}\right)=E_{0}+E_{2}\left[\left(\bar{n}_{i} / n_{0}\right)-1\right]^{2}+E_{3}\left[\left(\bar{n}_{i} / n_{0}\right)-1\right]^{3}. \tag{12}
$$

One can also use a parameterization in terms of the universal binding curve of Rose and co-workers [30].

The induced average electron density at site $i$, is easily related to the neutral radius of atom $i$, eq. (6). It is calculated from the integrated superposition of the density tails from the neighbouring atoms $j$ sticking into the region occupied by atom $i$ (Fig. 1),

$$
\bar{n}_{i}=n_{0} \mathrm{e}^{-\eta\left(s_{i}-s_{0}\right)}=\sum_{j} \Delta n_{i j}\left(s_{i}, r_{i j}\right). \tag{13}
$$

![](./images/812096627857686528_1.jpg)

Fig. 1. Schematic picture showing how the electron density is built up as a superposition of the densities, $\Delta n_{j}$, from the neighbouring atoms. The density tails from neighbouring atoms, $j$, are averaged in the region $s_{i}$ belonging to atom $i$, giving the background density $\bar{n}_{i}$. The notations in the figure are the same as in Section 2.1.1.

Here $\eta$ is a parameter determined by the induced density, $\Delta n(r)$, as are $\eta_{1}$ and $\eta_{2}$ in the Ansatz for the induced density on atom $i$ by the nearest-neighbour atom $j$ [24],

$$
\Delta \bar{n}_{i j}\left(s_{i}, r_{i j}\right)=\frac{n_{0}}{12} \mathrm{e}^{\eta_{1}\left(s_{i}-s_{0}\right)-\eta_{2}\left(r_{i j}-\beta s_{0}\right)}. \tag{14}
$$

As the neutral spheres are chosen to be equal to the Wigner-Seitz radii of an fcc crystal, one obtains the relation $\eta=\eta_{1}+\beta \eta_{2}$, where $\beta \simeq 1.809$ is a geometrical factor.

The Ansatz (13) is an equation in $s_{i}$ (or $\bar{n}_{i}$), and together with eq. (10) it gives the total energy for an fcc metal.

For structures that deviate from the fcc lattice an electrostatic pair-potential ($\Delta E_{\mathrm{AS}}$, atomic-sphere correction) is included. It is parametrised by $\alpha, n_{0}, \eta_{1}$ and $\eta_{2}$.

The one-electron energy ($\Delta E_{\mathrm{el}}$) is the sum of the oneelectron energy-parameter shifts, when going from the effective medium (the homogeneous electron gas) to the real host [24]. This difference arises from covalent bonding, hybridization and wave-function orthogonalizing effects. Several ways of including the one-electron term have been reported [29, 31-35]. It is beyond the scope of our paper to present or discuss any such correction here. We will only report the basic EMT-parameters needed for the two first terms in the total-energy expression, eq. (10).

## 3. Results and discussion
### 3.1. Comparison of the atom-in-jellium results in LDA and GGA
We have performed calculations in both the LDA and GGA exchange-correlation approximations for atoms ranging from H to Zn, excluding the noble gases. Some results are presented together with experimental values; cohesive energy in Fig. 2, neutral sphere radii in Fig. 3 and bulk modulus in Fig. 4. The experimental data are not included for a direct comparison but more as an indication of the quality of the changes, as just studying the atom-in-jellium or the first term of the EMT energy expression is an oversimplification. The cohesive energy functions of the 2p-series (within the GGA) are shown in Fig. 5 as an example of trends in position and depth of the minima. The elements in the late part of the row (O) bind most strongly and C with a half-filled sub-shell prefers the highest embedding density.

![](./images/812096627857686528_2.jpg)

Fig. 2. The cohesive energies $(E_{0})$ of the $E_{c}$ functions for atoms from $H$ to Zn (excluding the inert gases). The GGA results (open circles) are compared with the LDA values (black circles) and experimental values for the cohe- sive energies (crosses) [37].

One major deficiency of LDA is the overbinding of atoms in molecules and solids. For an atom in jellium this is exhibited as too deep cohesive-energy function and high equilibrium density, especially for the middle of the second (C-F) and third (Si-Cl) rows. The GGA consequently results in an upward shift in energy and in lower equilibrium den- sities compared to LDA, see Fig. 2 and Table I.

![](./images/812096627857686528_3.jpg)

Fig. 3. Neutral-sphere radii $(s_{0})$ corresponding to the minima of the $E_{c}$ functions. The GGA results (open circles) are compared with the LDA values (black circles) and experimental Wigner-Seitz radii (crosses) [38]. The experimental values for the alkali metals are for $0 ~K$.

![](./images/812096627857686528_4.jpg)

Fig. 4. The atom-in-jellium and EMT values for the bulk modulus, eq. (15) The GGA results (open circles) are compared with the LDA values (black circles) and experimental values for the bulk modulus (crosses) [37, 39].

![](./images/812096627857686528_5.jpg)

Fig. 5. Cohesive function $E_{c}[\bar{n}]$ [eq. (11)], calculated for the 2p-series within the GGA. The elements in the late part of the row (O) bind most strongly and $C$ with a half-filled sub-shell prefers the highest embedding density.

The large changes for the simple metals found in the GGA-I [23] are not present in our GGA results. In Fig. 6 cohesive energy curves for $O, Na, Al$ and $P$ are presented. The shift in cohesive minima for the too hardly LDA-bound second and third row elements is up to $1 eV$. As a compari son, the cohesive-energy functions calculated in the Self- Interaction Corrected (SIC) approximation [23] have large shifts for the 2p-elements (e.g. $\simeq 2 eV$ for $O$ ), but much smaller for the 3p-elements $(0-0.5 eV)$.

Our values for $E_{0}$ of $Co$ and $Ni$ in LDA differ from those of Ref. [24]. The use of the frozen-core approximation in Ref. [24] is likely to cause this difference.

To further analyze the GGA results we first note that the difference between GGA and LDA total energies for free atoms are larger than for embedded atoms. Secondly we find that the XC potential in GGA has somewhat sharper gradients, but the effects on the electron densities are negli- gible (though not completely for $H$ ) in agreement with pre vious reports $[15,16]$ . Figures 7 and 8 show that the relaxation charge densities, defined by eq. (8), for $Na$ and $Al$  are smaller than for $O$ and $P$ , which are bound harder in the

![](./images/812096627857686528_6.jpg)

Fig. 6. Comparison of the cohesive function $E_{c}(\bar{n})$ , [eq. (11)] calculated within the GGA and the LDA, respectively for $O, Na, Al$ and $P$ . The shift in cohesive minima for the too hardly LDA-bound $O$ and $P$ atoms are abou. $1 eV$ , while the change for $Na$ and $Al$ is much smaller.

Physica Scripta 55

<table>
<caption>Table I. Parameters for the Effective-Medium Theory. The parameters are calculated within the generalized gradient approximation (GGA) [10] and compared with the previous values calculated within the local-density approximation (LDA). See text for definitions.</caption>
<tr>
<td>
![](./images/812096627857686528_7.jpg)
</td>
<td>
![](./images/812096627857686528_8.jpg)
</td>
</tr>
<tr>
<td>
![](./images/812096627857686528_9.jpg)
</td>
<td>
![](./images/812096627857686528_10.jpg)
</td>
</tr>
</table>

jellium. It is also seen that the difference between LDA and GGA electron densities are very small.

If we study the corresponding changes in XC energy [see eq. (9)] in Figs 9 and 10, we see that the changes are smaller for GGA (due to lower free atom energies); note especially that the lowering of the XC energy density is not localized to the core region. The results may be explained by the fact that the change in gradients in the charge relaxation is not fully taken into account by LDA, whereas GGA gives more bonding to the larger gradients of the free atom, and thus reduces the bonding strength. The larger gradients and relaxation charges for the middle 2p-, 3p-series and transition elements give the trend in cohesion difference between LDA and GGA.

Traditionally one has argued that the too small binding of core electrons in LDA causes the core orthogonalization to push the valence electrons a little too far out. This in turn gives an over-sized overlap with neighbouring atoms in a molecule or solid and thus an overestimate of the bond strength [2] Our analysis shows that the present GGA does not result in that type of correction, but rather in a difference in the energy given to gradients in low density regions (i.e., to the valence electrons).

Above is in agreement with the fact that LDA is quite well satisfied in the high density limit. Hydrogen is in the opposite extrem with its small and rapidly varying density. Examining the relaxation charge for H (Fig. 11) it is clear that GGA has a stronger core orthogonalization than LDA.

![](./images/812096627857686528_11.jpg)

Fig. 7. Relaxation charge densities (a measure of the change in the electron screening of the nucleus, when the atom is immersed in the jellium) for Na and Al atoms embedded in an jellium with density $r_{s}=4.00\,\mathrm{a}_{0}$ and $r_{s}=3.25\,\mathrm{a}_{0}$, respectively. The solid lines are for the GGA calculation and dashed for LDA. The difference between LDA and GGA densities are seen to be very small. The background density is related to the radius $r_{s}$ by $\bar{n}=4\pi r_{s}^{3}/3$.

As there is no core/valence the difference in XC energy is evenly distributed. The observable difference in core orthog- onalization decreases fast with atomic number.

The trends through the periodic system are well described in both approximations. This is exemplified by the variation

![](./images/812096627857686528_12.jpg)

Fig. 8. Same as in Fig. 7, but for O and P atoms embedded in an jellium with density $r_{s}=2.75\,\mathrm{a}_{0}$ and $r_{s}=3.25\,\mathrm{a}_{0}$, respectively.

![](./images/812096627857686528_13.jpg)

Fig. 9. Difference in XC energy between the free atoms and the embedded atoms (see the text for a definition) for Na and Al atoms embedded in an jellium with density $r_{s}=4.00\,\mathrm{a}_{0}$ and $r_{s}=3.25\,\mathrm{a}_{0}$, respectively. The solid lines are for the GGA calculation and dashed for LDA.

![](./images/812096627857686528_14.jpg)

Fig. 10. Same as in Figure 9, but for O and P atoms embedded in an jellium with density $r_{s}=2.75\,\mathrm{a}_{0}$ and $r_{s}=3.25\,\mathrm{a}_{0}$, respectively.

of the neutral-sphere radii, $s_{0}$, with atomic number. Neutral-sphere radii in GGA and LDA are compared with experimental Wigner-Seitz radii in Fig. 3. The overbinding of LDA causes both first-principles calculations and the atom-in-jellium model to underestimate the lattice constants

![](./images/812096627857686528_15.jpg)

Fig. 11. (a) Relaxation charge densities for H atom embedded in an jellium with density $r_{s}=3.25\,\mathrm{a}_{0}$ and (b) the corresponding difference in XC energy between the free atoms and the embedded atoms (see the text for definitions).

![](./images/812096627857686528_16.jpg)

Fig. 12. The GGA atom-induced density of states [eq. (7)] for V (a) and Fe (b) atoms at several embedding densities around the cohesive minima at $r_{s}=2.75 \mathrm{a}_{0}$ and $r_{s}=2.50 \mathrm{a}_{0}$, respectively. The Fermi level has been set to 0 eV.

(equilibrium volume) of metals, especially the alkali metals. The GGA gives an increase in the neutral sphere radii for Li, Na and K with 2.0%, 3.2% and 4.2% respectively, also the radii for 3d-metals are nicely increased compared to experiment.

The bulk modulus of a metal depends mostly on the kinetic energy of the interstitial electron gas as a function of the density [23]. The experimental trend is quite well obeyed in the atom-in-jellium model, as described below. The bulk modulus is related to the curvature of the cohesive energy as [25],

$$
B=v \frac{\partial}{\partial v}\left(\frac{\partial E_{\mathrm{c}}}{\partial v}\right)=\frac{1}{12 \pi s_{0}} \frac{\partial^{2} E_{\mathrm{c}}}{\partial s^{2}}=\frac{E_{2} \eta^{2}}{6 \pi s_{0}},
\tag{15}
$$

where in the last step the parametrization (12) has been used. Expression (15) is identical to the EMT bulk modulus for the case where one assumes to have space filling spheres on a close-packed lattice. Our results are compared with LDA and experimental bulk-modulus values in Fig. 4. The GGA results are systematically smaller than the LDA ones, and in fairly good agreement with experimental results for the simple metals and for the early and the last transition metals. Calculations on transition metals with full potential LMTO within GGA gives an agreement similar to the atom-in-jellium model [12]. It reflects that the discrepancy from experiment is not solely due to the simplified model, but rather to the sensitivity of absolute values of the bulk moduli to the XC approximation used. The increased value for Flourine is due to the shift in an already large $\eta$-value, which enters as the square in the bulk-modulus expression.

For an atom embedded in the jellium the energy bands of a crystalline solid are replaced by resonances in the local density of states (LDOS) in the electron gas. The resonances are most pronounced for the transition metals. The results for Vanadium and Iron, Fig. 12, serve as illustrations of the general behavior. A d-electron resonance sharpens and moves towards the Fermi level as the embedding density is lowered. Fe has an almost filled d-resonance, and V has one that is slightly more than half-filled. Small differences in the atom-induced LDOS are noted between the LDA and GGA. With a simple model using square d-bands these resonances can provide estimates of the contribution of the d-d electron interactions to the cohesive energies [24].

### 3.2. EMT Parameters in GGA
It should be stressed that we only have calculated the basic parameters to describe a simple fcc metal and, that the EMT has further approximations far beyond the approx- imative treatment of XC effects. Many features of the XC potential may vanish in the EMT approximation. It is common practice to improve the agreement with experimen- tal data by adjusting some of the input parameters to an empirical value, typically the measured shear modulus. However, the major changes in $E_{c}(\bar{n}), s_{0}$ and $B$ for the atom in-jellium are carried over directly to the EMT potential. The GGA improves the cohesive energies, lattice constants and bulk modulus, as discussed in Section IIIA.

The dependence on background density of the neutral sphere radius expressed by $\eta$ and $\eta_{1}$ show very small differ ences between LDA and GGA, except for the halogens, which tend to pull electrons more tightly in GGA. The atom-induced electrostatic potential, $\alpha$, remains practically unchanged. A complete set of parameters, calculated both within LDA and GGA, for elements with atomic number 1-30, excluding the noble gases, is presented in Table I.

## 4. Concluding remarks
The aim of this paper is to provide GGA results for the atom-in-jellium model and EMT parameters for the 30 first elements (excluding the noble gases) [40]. Bonding proper- ties of GGA compared to LDA have also been analyzed and we find that GGA reduces the overbinding of LDA mainly by giving more bonding energy to the gradients of the free atom. The effect is most pronounced for the middle 2p- and 3p-series which have large gradients in their valence electron densities.

The GGA results are found to preserve EMT cohesive properties that are well described in the LDA and improve several of the deficiencies of LDA. In this respect it differs from GGA-I, which tends to overcorrect the overbinding [23]. The GGA consequently raises the $E_{c}$ curves for the 2p and 3p-series, contrary to SIC, which leaves the 3p-serie unchanged. The increase in Wigner-Seitz radii with the

Physica Scripta 55

GGA is also favorable. A small lowering in equilibrium den- sities is found for all elements, except Cl, which has a rela- tively large reduction. The bulk-modulus values of the the simple and 3d-transition metals are improved, with the largest correction for the middle of the 3d-row. Parameters that depends on the shape of the electron charge densities are left unchanged.

The overall result of this paper can then be summarized: The atom-in-jellium is a positive test of the GGA, and GGA provides improved input parameters for the effective- medium theory, EMT.

### Acknowledgements

The authors are thankful to Professor B. I. Lundqvist for proposing the project and for discussions of the manuscript and to L. Hansen for debug- ging, discussions and proof-reading. One of the authors (U.Y.) especially thanks G. Eliasson for the introduction to the embedding codes. We would also like to thank J. Perdew for providing us with GGA computer codes.

This work has been supported by the Swedish Natural Science Research Council and the Swedish Board for Industrial and Technical Development.

### References

1. Hohenberg, P. and Kohn, W., Phys. Rev. 136, B864 (1964).
2. Jones, R. and Gunnarsson, O., Rev. Mod. Phys. 61, 689 (1989).
3. Parr, R. G. and Weitao Yang, "Density-Functional Theory of Atoms and Molecules" (Oxford University Press, 1989).
4. Kohn, W. and Sham, L., Phys. Rev. 140, A1133 (1965).
5. Hedin, L. and Lundqvist, B., J. Phys. C4, 2064 (1971).
6. Gunnarsson, O. and Lundqvist, B. I., Phys. Rev. B13, 4274 (1976).
7. Langreth, D. and Mehl, M., Phys. Rev. Lett. 47, 446 (1981).
8. Perdew, J. P. and Wang, Y., Phys. Rev. B33, 8800 (1986).
9. Perdew, J. P., Phys. Rev. B33, 8822 (1986); 34 7406(E) (1986).
10. Perdew, J., in: "Electronic Structure of Solids '91", (Edited by P. Ziesche and H. Eschrig) (Akademie-Verlag, Berlin 1991).
11. Perdew, J. P. *et al.*, Phys. Rev. B46, 6671 (1992).
12. Körling, M. and Häglund, J., Phys. Rev. B45, 13 293 (1992).
13. Becke, Axel D., J. Chem. Phys. 97, 9173 (1992).
14. Häglund, J., Phys. Rev. B47, 566 (1993).
15. Juan, Yu-Min and Kaxiras, E., Phys. Rev. B48, 14 944 (1993).
16. Hammer, B., Jacobsen, K. W. and Nøskov, J. K., Phys. Rev. Lett. 70,3971 (1993).
17. Wigner, E. P. and Seitz, F., Solid State Physics, 1, 97-123 (1955).
18. Ziman, J. M., "Principles of the Theory of Solids" (Cambridge at the University Press, 1965).
19. Almbladh, C. O., von Barth, U., Popovic, Z. D. and Stott, M. J., Phys. Rev. B14, 2250 (1976).
20. Hodges, L., Watson, R. E. and Ehrenreich, H., Phys. Rev. B5, 3953(1972).
21. Watson, R. E., Herbst, J. F., Hodges, L., Lundqvist, B. I. and Wilkins, J. W., Phys. Rev. B13, 1463 (1976).
22. Puska, M. J., Nieminen, R. M. and Manninen, M., Phys. Rev. B24,3037 (1981).
23. Puska, M. and Nieminen, R., Phys. Rev. B43, 12221 (1991).
24. Jacobsen, K. W., Nørskov, and Puska, M. J., Phys. Rev. B35, 7423(1987).
25. Jacobsen, K. W., Comments Cond. Mat. Phys. 14, 129 (1988).
26. Gunnarsson, O., Lundqvist, B. I. and Wilkins, J. W., Phys. Rev. B10,319 (1974).
27. von Barth, U. and Hedin, L., J. Phys. C5, 1629 (1972).
28. Eliasson, G. (unpublished).
29. Christensen, O. B., Jacobsen, K. W., Nørskov, J. K. and Manninen, M., Phys. Rev. Lett. 66, 2219 (1991).
30. Rose, J. H., Ferrante, J. and Smith, J. R., Phys. Rev. Lett. 47, 675(1981).
31. Nordlander, P., Holloway, S. and Nørskov, J. K., Surf. Sci. 136, 59(1984).
32. Nørskov, J. K., J. Chem. Phys. 90, 7461 (1989).
33. Stoltze, P., Physica Scripta 36, 829 (1987).
34. Hansen, L., Stoltze, P., Jacobsen, K. W. and Nørskov, J. K., Phys. Rev. B44, 6523 (1991).
35. Yxklinten, U., Andersson, Y. and Lundqvist, B. I., Phys. Rev. Lett. 72,2302 (1994).
36. Shoe, H. B. and Rose, J. H., Phys. Rev. Lett. 66, 2519 (1991).
37. Kittel, C., "Introduction to Solid State Physics" (Wiley, New York1976).
38. Compiled by P. Eckerlin and H. Kandler, in: "Landolt-Börnstein, Numerical Data and Functional Relationships in Science and Tech- nology" (Edited by K.-H. Hellwege) (Springer-Verlag, 1971).
39. Guillermet, A. F. and Grimvall, G., Phys. Rev. B40, 1521 (1989).
40. The calculational data and EMT-parameters may be aquired at http://fy.chalmers.se/~hart/