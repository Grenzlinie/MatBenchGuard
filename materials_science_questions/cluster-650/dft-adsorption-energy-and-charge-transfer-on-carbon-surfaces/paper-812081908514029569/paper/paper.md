This article was downloaded by: [Florida State University]
On: 06 May 2013, At: 11:47
Publisher: Taylor & Francis
Informa Ltd Registered in England and Wales Registered Number: 1072954
Registered office: Mortimer House, 37-41 Mortimer Street, London W1T 3JH, UK

![](./images/812081908514029569_1.jpg)

Molecular Physics: An International
Journal at the Interface Between
Chemistry and Physics

Publication details, including instructions for authors and
subscription information:
http://www.tandfonline.com/loi/tmph20

Computational studies of the
structure of carbon dioxide
monolayers physisorbed on the
basal plane of graphite

Kenton D. Hammonds $^{a}$ , Ian R. McDonald $^{a}$ \& Dominic J.
Tildesley $^{b}$

$^{a}$ Department of Chemistry, University of Cambridge,
Lensfield Road, Cambridge, CB2 1EW, U.K.
$^{b}$ Department of Chemistry, University of Southampton,
Southampton, SO9 5NH, U.K.
Published online: 22 Aug 2006.

To cite this article: Kenton D. Hammonds, Ian R. McDonald & Dominic J. Tildesley (1990):
Computational studies of the structure of carbon dioxide monolayers physisorbed on the
basal plane of graphite, Molecular Physics: An International Journal at the Interface Between
Chemistry and Physics, 70:2, 175-195

To link to this article: http://dx.doi.org/10.1080/00268979000100931

PLEASE SCROLL DOWN FOR ARTICLE

Full terms and conditions of use: http://www.tandfonline.com/page/terms-and-
conditions

This article may be used for research, teaching, and private study purposes. Any
substantial or systematic reproduction, redistribution, reselling, loan, sub-licensing,
systematic supply, or distribution in any form to anyone is expressly forbidden.

The publisher does not give any warranty express or implied or make any
representation that the contents will be complete or accurate or up to date. The
accuracy of any instructions, formulae, and drug doses should be independently
verified with primary sources. The publisher shall not be liable for any loss, actions,
claims, proceedings, demand, or costs or damages whatsoever or howsoever

caused arising directly or indirectly in connection with or arising out of the use of this material.

MOLECULAR PHYSICS, 1990, VOL. 70, No. 2, 175-195

# Computational studies of the structure of carbon dioxide monolayers physisorbed on the basal plane of graphite

by KENTON D. HAMMONDS and IAN R. McDONALD

Department of Chemistry, University of Cambridge, Lensfield Road, Cambridge CB2 1EW, U.K.

and DOMINIC J. TILDESLEY

Department of Chemistry, University of Southampton, Southampton SO9 5NH, U.K.

(Received 2 January 1990; accepted 26 January 1990)

The molecular-dynamics method has been used to study carbon dioxide physisorbed on the basal plane of graphite at temperatures between 100 and 130 K at monolayer and submonolayer coverages. Additionally, energy- minimization calculations have been used to explore the relative stability of a number of solid structures of the adsorbate. Three models of carbon dioxide, which have been successful in describing the properties of the bulk phase, where tested in these simulations of the adsorbate. The results at submonolayer cover- age suggest that the adsorbate forms a two-sublattice incommensurate herring- bone structure. These solid patches have approximately the correct melting point. At monolayer coverage the existence of a four-sublattice pinwheel struc- ture was only observed for a model with an artificially enhanced quadrupole moment. Further refinement of the potential model will require additional calorimetric or diffraction experiments.

## 1. Introduction

Monolayers of linear molecules physisorbed on the basal plane of graphite exhibit a range of solid-state structures. The two-sublattice herringbone structure illustrated in figure 1 has been observed experimentally for a number of symmetric molecules with moderate quadrupole moments, including $N_2$ [1], CO [2], $CS_2$ [3] and $C_2N_2$ [4]; the herringbone structure is characterized by the presence of a glide line (AB in figure 1), i.e. an axis of translation-reflection symmetry. Mean-field calculations for pure quadrupoles on a triangular lattice [5] show that the herring- bone structure is the equilibrium configuration whenever the external field due to the surface is sufficiently strong: the field causes the molecules to lie in a plane parallel to the surface, and the herringbone arrangement minimizes the energy within the plane. When the quadrupole moment is small and dispersion forces are correspondingly more important, as is the case for $O_2$ [6], the molecules again lie parallel to the surface, but now form centred-rectangular structures in which all molecules are mutually parallel. As the quadrupolar interaction increases in strength relative to the molecule-surface potential, the predicted [5] stable structure becomes the four-sublattice pinwheel arrangement pictured in figure 2, in which one molecule in four stands perpendicular to the surface at the centre of an hexagonal pinwheel. So far as we are aware, the pinwheel structure has not been observed experimentally for linear molecules adsorbed on graphite at monolayer coverages, but it has been

0026-8976/90 $3.00 © 1990 Taylor & Francis Ltd

![](./images/812081908514029569_2.jpg)

Figure 1. The two-sublattice herringbone structure. The dots represent carbon atoms in the first layer of graphite and the short solid lines are the projections of the molecular axes onto the surface. The glide line AB is an axis of translation-reflection symmetry. In the commensurate $\sqrt{3} \times \sqrt{3}$ structure adopted by $N_{2}$, the centres of mass of the molecules lie at the centres of every third hexagon. The angle $\psi$ has the same value for each sublattice; for $N_{2}, \psi \approx 45^{\circ}$.

![](./images/812081908514029569_3.jpg)

Figure 2. The four-sublattice pinwheel structure. The open circle represents a molecule perpendicular to the plane of the surface.

postulated [7] as the structure of CO on graphite at a coverage $\theta=1 \cdot 13$, where a coverage of unity is defined as that corresponding to the $\sqrt{3} \times \sqrt{3}$ commensurate solid (see figure 1). Carbon dioxide is a possible candidate for formation of a commensurate pinwheel monolayer, since the molecule has a quadrupole moment $(\Theta=-13.4 \pm 0.4 \times 10^{-40} C m^{2})$ significantly larger in magnitude than that of CO $(\Theta=-8.6 \times 10^{-40} C m^{2})$ [8], and one of the original aims of the present work was to test whether this conjecture is supported by detailed calculations.

The phase diagram of $CO_{2}$ on graphite has been deduced from the measured adsorption isotherms by Terlain and Larher [9]. There is a region of solid-gas coexistence that terminates in a triple-point line at 122 K, while liquid and gas coexist below a critical temperature of 127.5 K. Comparison of the vapour pressures of adsorbed and bulk $CO_{2}$ shows that adsorption does not occur at temperatures below 104K. Terlain and Larher estimate that the average area per molecule is $15.7 \AA^{2}$, which is the value expected for a $\sqrt{3} \times \sqrt{3}$ commensurate solid, and argue that geometric factors should favour herringbone packing. Neutron or X-ray diffrac-

tion measurements would help in clarifying the situation, but there are considerable practical difficulties involved. The structure of $CO_2$ monolayers on graphite has therefore not been definitively established.

In this paper we report the results of molecular-dynamics simulations and energy minimisations for models of the $CO_2$-graphite system. The work complements earlier computational studies of adsorbed layers of small molecules such as $N_2$ [10], $O_2$ [11], CO [12], $CS_2$ [3], $C_2H_4$ [13] and $C_2H_6$ [14]. The input to the molecular-dynamics calculations consists of the surface coverage, the total energy of the monolayer (which implicitly determines the average temperature), the interaction potentials and the initial configuration. In our choice of potential models we have been guided by previous calculations on the condensed phases of bulk $CO_2$, and three models [15-17] have been chosen for detailed investigation. The choice of initial configuration is also important. High-density monolayer solids can be artificially stabilized by the periodic boundary conditions used in simulations, and a metastable solid phase may persist for many thousands of time steps. A similar problem arises in energy minimisations, where use of an unsuitable starting configuration may lead to a local rather than a global minimum. Where such difficulties have been suspected in our own work, the calculations have been repeated with other choices of initial conditions. Note that we work throughout in a system of units in which Boltzmann's constant is taken as unity and energies are measured in kelvin.

## 2. The models

The potentials used in the calculations contain two ingredients: one is the interaction between two adsorbed molecules and the other is the interaction between an adsorbed molecule and the surface. We consider each in turn.

### 2.1. The intermolecular potential

Experience has shown (see e.g. [3, 10-14]) that the simulation of adsorbed phases can be successfully based on pairwise-additive potentials fitted to properties of the corresponding bulk systems. In the present work we have adopted three such models, which we label respectively 2CLJ, MOM and PRC1. Model 2CLJ is a two-centre Lennard-Jones potential used successfully by *Singer et al.* [15] in molecular-dynamics calculations on liquid $CO_2$. The inadequacies of this class of model in the simulation of ordered phases are well known, but it is useful to include an example here in order to provide a standard against which the role played by quadrupolar forces may be judged. The two interaction sites are centred on the oxygen atoms, and the model is therefore fully specified by the two Lennard-Jones parameters $\varepsilon_{OO}$, $\sigma_{OO}$ and the separation $R_{OO}$, of the oxygen sites. Models MOM [16] and PRC1 [17] are substantially more realistic in so far as allowance is made for the permanent electrostatic interactions between molecules. When these models were originally parametrized, the total electrostatic contribution was expressed as the sum of the interactions between five fractional point charges on each molecule; in the case of model MOM, the charge distribution was designed to reproduce the then available experimental value of $\Theta$ and the fourth, sixth and eighth electrostatic moments calculated by *ab initio* methods. For the sake of computational efficiency, we have reduced the number of charges to three $(q_O, q_C, q_O)$, chosen such as to preserve the quadrupole moments of the original models. This simplification is

<table>
<caption>Table 1. Parameters in the potential models.</caption>
<thead>
<tr>
<th></th>
<th>2CLJ [15]</th>
<th>MOM [16]</th>
<th>PRC1 [17]</th>
</tr>
</thead>
<tbody>
<tr>
<td>$\sigma_{OO}/Å$</td>
<td>2·900</td>
<td>3·027</td>
<td></td>
</tr>
<tr>
<td>$\sigma_{CO}/Å$</td>
<td></td>
<td>2·922</td>
<td></td>
</tr>
<tr>
<td>$\sigma_{CC}/Å$</td>
<td></td>
<td>2·824</td>
<td></td>
</tr>
<tr>
<td>$r_{OO}^{0}/Å$</td>
<td></td>
<td></td>
<td>3·783</td>
</tr>
<tr>
<td>$r_{CO}^{0}/Å$</td>
<td></td>
<td></td>
<td>3·660</td>
</tr>
<tr>
<td>$\varepsilon_{OO}/K$</td>
<td>192·5</td>
<td>74·8</td>
<td>54·83</td>
</tr>
<tr>
<td>$\varepsilon_{CO}/K$</td>
<td></td>
<td>44·8</td>
<td>29·45</td>
</tr>
<tr>
<td>$\varepsilon_{CC}/K$</td>
<td></td>
<td>26·2</td>
<td>0</td>
</tr>
<tr>
<td>$\lambda_{OO}$</td>
<td></td>
<td></td>
<td>12·04</td>
</tr>
<tr>
<td>$\lambda_{CC}$</td>
<td></td>
<td></td>
<td>12·46</td>
</tr>
<tr>
<td>$q_{O}/e$</td>
<td></td>
<td>$-0·332\dagger$</td>
<td>$-0·605\dagger$</td>
</tr>
<tr>
<td>$\varTheta/10^{-40}\,{\rm Cm}^{2}$</td>
<td></td>
<td>$-14·4$</td>
<td>$-17·5$</td>
</tr>
<tr>
<td>$R_{OO}/Å$</td>
<td>2·300</td>
<td>2·324</td>
<td>1·900</td>
</tr>
</tbody>
<tfoot>
<tr>
<td colspan="4">$\dagger\,q_{\rm C}=-2q_{O}$.</td>
</tr>
</tfoot>
</table>

justified physically to the extent that the higher-order moments of ${\rm CO}_{2}$ are much less important than the quadrupole [16]. The non-electrostatic van der Waals con- tributions are also represented by three interaction sites, taken to be coincident with the fractional charges.

Depending on the model, the site-site potentials are of either Lennard-Jones (in MOM) or exp-6 (in PRC1) form. The MOM interaction sites are located on the three atoms, but in model PRC1 the oxygen sites are shifted inwards, a change that is partly offset by the use of a larger quadrupole moment. The Lennard-Jones parameters in the MOM potential were fitted to the phonon frequencies and lattice energy of the solid, thermodynamic properties of the liquid and the second virial coefficient of the gas. The exp-6 interactions used in the PRC1 potential have the form

$$
v(r)=\frac{\varepsilon_{\alpha \beta}}{\lambda_{\alpha \beta}-6}\left\{6 \exp \left[\lambda_{\alpha \beta}\left(1-\frac{r}{r_{\alpha \beta}^{0}}\right)\right]-\lambda_{\alpha \beta}\left(\frac{r_{\alpha \beta}^{0}}{r}\right)^{6}\right\},
$$

where $\alpha$ and $\beta$ label the interaction sites and $r$ is the site-site separation. The parameters of the model were fitted to the frequencies and bandwidths of the optical lattice phonons of the bulk solid in a way that improved on the results obtained from the MOM potential. The parameter values for all three models are listed in table 1.

The minimum-energy dimer configuration for model 2CLJ is a staggered-parallel arrangement of the type shown in figure 3(a), while for model PRC1 it is the T-shaped structure of figure 3(b); for both the PRC1 and MOM models, the two dimer structures are of comparable energies. The results for the three models are

![](./images/812081908514029569_4.jpg)

Figure 3. Two dimer configurations: (a) staggered-parallel; (b) T-shaped.

**Table 2. Dimer potential energies for the structure of figure 3.**

### (a) $V_{\text{min}}$/K
| Structure          | 2CLJ  | MOM   | PRC1  |
|--------------------|-------|-------|-------|
| Staggered-parallel | $-625$| $-574$| $-576$|
| T-shaped           | $-419$| $-548$| $-590$|

### (b) Breakdown of $V_{\text{min}}$
| Structure          | **MOM**       |       | **PRC1**      |       |
|--------------------|---------------|-------|---------------|-------|
|                    | $V_{\text{vdW}}$/K | $V_{\text{elec}}$/K | $V_{\text{vdW}}$/K | $V_{\text{elec}}$/K |
| Staggered-parallel | $-272$        | $-302$| $-138$        | $-438$|
| T-shaped           | $-214$        | $-334$| $-112$        | $-478$|

given in table 2(a) under the heading $V_{\text{min}}$. With the large quadrupole moments in these models, the electrostatic interactions dominate over the van der Waals interactions. This is confirmed by the breakdown into electrostatic (elec) and van der Waals (vdW) contributions in table 2(b), which also shows that the balance between these two contributions is appreciably different in the MOM and PRC1 potentials.

### 2.2. The molecule-surface potential
In all the calculations described below, the interactions between the adsorbed molecules and the graphite were treated by the method of Steele [18], in which the molecule-surface potential is expanded in a two-dimensional Fourier series. Only the two leading terms in the expansion were retained, giving a maximum error of approximately $2\%$ in the potential energy. Solid graphite is well suited to this expansion, since the graphite atoms within a layer are closely spaced and the corrugation energies are relatively small. The expressions appropriate to a Lennard-Jones adsorbate-surface interaction are given by Steele [18], and those for an exp-6 interaction can be found in [7]. The adsorbate-surface (A-S) potential parameters were calculated from the combing rules

$$
\sigma_{\mathrm{AS}}=\frac{1}{2}(\sigma_{\mathrm{AA}}+\sigma_{\mathrm{SS}}),\quad r_{\mathrm{AS}}^{0}=\frac{1}{2}(r_{\mathrm{AA}}^{0}+r_{\mathrm{SS}}^{0}),\quad \lambda_{\mathrm{AS}}=\frac{1}{2}(\lambda_{\mathrm{AA}}+\lambda_{\mathrm{SS}}),\quad \varepsilon_{\mathrm{AS}}=(\varepsilon_{\mathrm{AA}}\varepsilon_{\mathrm{SS}})^{1/2},
$$

where $\text{A}=\text{C}$ or $\text{O}$. The Lennard-Jones S-S parameters ($\varepsilon_{\text{SS}}=28\ \text{K}$, $\sigma_{\text{SS}}=3.4\ \text{Å}$) were taken from [18], and the parameters in the exp-6 potential were chosen in such a way as to make the well depth and collision diameter the same as in the Lennard-Jones case, i.e. $\varepsilon_{\text{SS}}=28\ \text{K}$, $r_{\text{SS}}^{0}=2^{1/6}\sigma_{\text{SS}}$ and $\lambda_{\text{SS}}=14.34$. Since the PRC1 model ignores the van der Waals interactions between carbon atoms, the corresponding C-S potential has to be determined indirectly. A set of parameters were first obtained that were consistent with the combining rules given above, but here applied to PRC1 site-site interactions, and these were combined with the S-S parameters to yield the required PRC1 C-S parameters.

All three models have their minimum molecule-surface potential energy when the molecule is parallel to the surface. The carbon atom of $\text{CO}_{2}$ lies in each case above a bridge point on the surface, i.e. a point midway between two nearest-neighbour graphite atoms, and the molecular axis points towards the centres of

<table>
<caption>Table 3. Molecule-surface potential energies.</caption>
<thead>
<tr>
<th></th>
<th>2CLJ</th>
<th>MOM</th>
<th>PRC1</th>
</tr>
</thead>
<tbody>
<tr>
<td>$V_{\text{min}}$/K</td>
<td>$-2446$</td>
<td>$-2003$</td>
<td>$-1774$</td>
</tr>
<tr>
<td>$z_{\text{min}}$/Å</td>
<td>$3 \cdot 075$</td>
<td>$3 \cdot 136$</td>
<td>$3 \cdot 307$</td>
</tr>
<tr>
<td>$\Delta V_{\text{trans}}$/K</td>
<td>$139$</td>
<td>$83$</td>
<td>$40$</td>
</tr>
<tr>
<td>$\Delta V_{\text{rot}}(1)$/K</td>
<td>$7$</td>
<td>$5$</td>
<td>$1$</td>
</tr>
<tr>
<td>$\Delta V_{\text{rot}}(2)$/K</td>
<td>$119$</td>
<td>$73$</td>
<td>$40$</td>
</tr>
<tr>
<td>$V_{\text{perp}}$/K</td>
<td>$-1474$</td>
<td>$-1154$</td>
<td>$-1122$</td>
</tr>
</tbody>
</table>

$V_{\text{min}} \equiv$ global energy minimum; $z_{\text{min}} \equiv$ height of centre of mass at energy minimum; $\Delta V_{\text{trans}} \equiv$ maximum translational barrier across surface; $\Delta V_{\text{rot}}(1) \equiv$ in-plane rotational barrier at hexagon centre; $\Delta V_{\text{rot}}(2) \equiv$ in-plane rotational barrier at bridge point; $V_{\text{perp}} \equiv$ energy minimum for molecule perpendicular to surface.

adjacent graphite hexagons. When the molecule is perpendicular to the surface, the minimum energy occurs when the molecule stands above the centre of a hexagon. The results for the minimum-energy configurations are summarized in table 3.

A useful test of an assumed molecule-surface potential is the value it predicts for the isosteric enthalpy at zero coverage, defined as

$$
q_{\text{st}}^{0}=T-\left\langle V_{\text{MS}}\right\rangle,
$$

where $V_{\text{MS}}$ is the energy of interaction between a molecule and the surface. The Metropolis Monte Carlo method [19] was used to calculate $\left\langle V_{\text{MS}}\right\rangle$ as a function of temperature for models MOM and PRC1. The experimental value of $q_{\text{st}}^{0}$ at $T=195 \mathrm{~K}$ is $2160 \mathrm{~K}$ [20], while the predicted values at the same temperature are $q_{\text{st}}^{0}=1874 \pm 2 \mathrm{~K}$ (MOM) and $q_{\text{st}}^{0}=1690 \pm 2 \mathrm{~K}$ (PRC1). The discrepancies between theory and experiment may arise in part from the fact that the calculations ignore the interactions between the molecular multipole moments and image multipoles in the surface. If image interactions are included in the manner described by Bruch [21], values of $q_{\text{st}}^{0}$ of about $3000 \mathrm{~K}$ are obtained, but the numerical results are highly sensitive to the assumed position of the image plane. In view of this uncertainty, no attempt has been made to include image interactions in either the energy mini- mizations or the simulations.

### 3. Energy minimisations

The energy minimisations were performed with the help of the NAG routine E04JBF, which is designed to minimise an arbitrary function of $n$ variables. The user merely has to provide a subroutine that calculates the function of interest from variables passed to it by E04JBF. For the problem in hand, the function involved is the total potential energy of the monolayer, calculated with the intermolecular potential truncated at a centre-of-mass separation of $50 \AA$, and the variables are the quantities that define the size and shape of the unit cell, i.e. the cell lengths $a \equiv|\mathbf{a}|$, $b \equiv|\mathbf{b}|$ and cell angle $\alpha_{\text {cell }}$ of figure 4, together with the number $q$, positions and orientations of the $\mathrm{CO}_{2}$ molecules within the unit cell. Minimizations were carried out for one, two and four molecules per unit cell, and an incommensurate ground- state structure was obtained for each model; the results were essentially independent of whether or not the corrugation term in the Steele potential was included. The minimum-energy structure for the 2CLJ potential has only one molecule per unit

![](./images/812081908514029569_5.jpg)

Figure 4. The unit cell of the monolayer structures discussed in the text.

cell, lying in a plane parallel to the surface. The minimum energies for models MOM and PRC1 are achieved with the two-sublattice herringbone structures shown in figure 5(a). If the origin of the unit cell is taken as the carbon atom of molecule 1 then the centre of molecule 2 lies at the midpoint of the lattice vector $\mathbf{a}$, as pictured in figure 4; the angle $\psi$ in figure 5(a) is approximately $34^{\circ}$ for model MOM and $45^{\circ}$ for model PRC1. The three minimum-energy structures are completely specified by the number $q$, the unit-cell dimensions, the angle or angles of the molecular axes (labelled $\beta_{1}, \beta_{2}$ in figure 4), and the height $z$ of the molecules above the surface. This information is given in table 4, together with the potential energy per molecule, $V / N$. Note that the structure obtained for model PRC1 is of higher (square) symmetry than that of model MOM. Although the PRC1 structure is of herringbone type, it could be more accurately described as a T-bone structure; nearest-neighbour molecules are in the T-configuration of figure 3(b), an arrangement that reflects the dominance of the quadrupolar term in this potential.

A variety of other calculations have been carried out for the two quadrupolar models. When the density is reduced to a sufficiently small value, energy minimization leads to a T-bone structure even for the MOM potential. This happens at coverages $\theta$ less than about 0.9 (here a coverage $\theta=1$ corresponds to the $\sqrt{ } 3 \times \sqrt{ } 3$ commensurate/solid at a density of $0.064 \AA^{-2}$ ). The reduction in density has the effect of shifting the balance towards the more slowly decaying $(r^{-5})$, quadrupolar component of the intermolecular potential. Of the possible four-sublattice structures, the most stable is an incommensurate form of the pin wheel arrangement of figure 2, for which the energy per molecule without corrugation is $-3132 \mathrm{~K}$ (MOM) or $-3110 \mathrm{~K}$ (PRC1). The corresponding figures for the commensurate $\sqrt{ } 3 \times \sqrt{ } 3$ pinwheel solid are $-3024 \mathrm{~K}$ (MOM) and $-3029 \mathrm{~K}$ (PRC1), while for the commensurate $\mathrm{N}_{2}$-like structure they are $-2955 \mathrm{~K}$ (MOM) and $-2880 \mathrm{~K}$ (PRC1). The

Table 4. Minimum-energy monolayer structures.
<table>
<thead>
<tr>
<th>Model</th>
<th>$q$</th>
<th>$a/\mathring{A}$</th>
<th>$b/\mathring{A}$</th>
<th>$\alpha_{cell}$</th>
<th>$\beta_{1},\beta_{2}$</th>
<th>$z/\mathring{A}$</th>
<th>$\theta$</th>
<th>$(V/N)/\text{K}$</th>
</tr>
</thead>
<tbody>
<tr>
<td>2CLJ</td>
<td>1</td>
<td>5·481</td>
<td>3·210</td>
<td>$64\cdot 1^{\circ}$</td>
<td>$-5\cdot 8^{\circ}$</td>
<td>3·134</td>
<td>0·995</td>
<td>−3546</td>
</tr>
<tr>
<td>MOM</td>
<td>2</td>
<td>8·119</td>
<td>5·151</td>
<td>$50\cdot 6^{\circ}$</td>
<td>$84\cdot 3^{\circ},17\cdot 0^{\circ}$</td>
<td>3·178</td>
<td>0·974</td>
<td>−3264</td>
</tr>
<tr>
<td>PRC1</td>
<td>2</td>
<td>8·240</td>
<td>5·826</td>
<td>$45\cdot 0^{\circ}$</td>
<td>$90\cdot 0^{\circ},0\cdot 0^{\circ}$</td>
<td>3·327</td>
<td>0·927</td>
<td>−3170</td>
</tr>
</tbody>
</table>

![](./images/812081908514029569_6.jpg)

![](./images/812081908514029569_7.jpg)

Figure 5. Monolayer structures at the global-energy minima: (a) model MOM; (b) model PRC1. The line AB is the glide line of the herringbone structure.

high energies associated with the $N_2$-type herringbone ordering of the molecules is a consequence of the increased molecular overlap at monolayer coverage ($\theta = 1$).

The corrugation energy as calculated by the Steele method is of little importance in the energy minimizations, since it accounts, typically, for only abou $0.5\%$ of the total potential energy of the monolayer. Some recent studies [22] of $N_2$ on graphite suggest, however, that the true in-plane potential-energy barriers may be consider- ably larger than in Steele's treatment. One argument put forward is that the poten- tial barriers are increased by the anisotropy in the polarizability of graphite [23]. Such an enhancement of the barriers could be important here, given the small energy differences between the commensurate and incommensurate pinwheel struc- tures, particularly for the PRC1 potential. We have therefore tested this suggestion in an ad hoc way by repeating the energy minimisations with the Steele corrugation energy arbitrarily multiplied by factors of up to $2.5$. No significant change was observed in the relative stabilities of the structures already discussed. If multiplica- tive factors greater than $2.5$ are used, it becomes physically unrealistic to truncate the Steele expansion after two terms. We have therefore not pursued the matter further.

## 4. Molecular-Dynamics simulations

Energy minimizations are limited in scope to the extent that they take no account of entropic effects. This is particularly relevant to the present problem because $CO_2$ is adsorbed on graphite only at temperatures greater than about 104K. At such temperatures, energy minimizations may no longer be a reliable guide to structure. Simulations by molecular-dynamics methods have therefore been undertaken in order to study the behaviour of the model systems under conditions appropriate to the experimental observations. All simulations were carried out in the $NVE$ ensemble, with periodic boundary conditions imposed in the plane of the surface, i.e. the $xy$ plane. A leapfrog algorithm was used to integrate the trans- lational equations of motion, and the rotational degrees of freedom were treated by a modified leapfrog algorithm in combination with the method of quaternions [19]. Time steps of between $4.4$ and $13.2$ fs were used, and the intermolecular potentials were truncated at distances of $9.9\mathring{A}$ for the $\sqrt{3} \times \sqrt{3}$ monolayers and $13.8\mathring{A}$ in all other cases. A typical simulation consisted of an equilibration stage of between 2000 and 6000 time steps, followed by a production run of 3000-6000 time steps.

### 4.1. Translational and orientational order

It is important to be able to extract from the molecular-dynamics data informa- tion on the way in which translational and orientational order in the adsorbed layer changes either in the course of a single calculation or from run to run as the temperature or other variables are changed. If the molecules initially form a com- mensurate $\sqrt{3} \times \sqrt{3}$ solid, the persistence of translational order can be monitored using the order parameters

$$
\mathrm{OP}_{1}=\left\langle\frac{1}{2 N} \sum_{i}\left[\cos \left(\mathbf{k}_{1} \cdot \mathbf{r}_{i}\right)+\cos \left(\mathbf{k}_{2} \cdot \mathbf{r}_{i}\right)\right]\right\rangle,
$$

$$
\mathrm{OP}_{2}=\left\langle\frac{1}{N^{2}} \sum_{i>j} \sum\left[\cos \left(\mathbf{k}_{1} \cdot \mathbf{r}_{i j}\right)+\cos \left(\mathbf{k}_{2} \cdot \mathbf{r}_{i j}\right)\right]\right\rangle,
$$

where the sums run over molecules in the monolayer, $N$ is the total number of molecules, $\mathbf{r}_{i}$ represents the centre-of-mass coordinates of molecule $i$ in the plane of the surface and relative to an origin at the centre of a graphite hexagon, $\mathbf{r}_{i j}$ is the surface projection of the vector linking the centres of mass of molecules $i$ and $j$, and $\mathbf{k}_{1}$ and $\mathbf{k}_{2}$ are reciprocal-lattice vectors of the $\sqrt{3} \times \sqrt{3}$ solid, with

$$
\mathbf{k}_{1}=\frac{2 \pi}{a}\left(-\frac{1}{3}, \frac{1}{\sqrt{3}}\right), \quad \mathbf{k}_{2}=\frac{2 \pi}{a}\left(\frac{2}{3}, 0\right),
$$

where $a(=2.461 \AA)$ is the lattice parameter for graphite. The quantity $\mathrm{OP}_{1}$ is unity if the molecular centres of mass form a $\sqrt{3} \times \sqrt{3}$ solid in perfect register with the graphite, and zero in a fluid phase; $\mathrm{OP}_{2}$ will normally be the square of $\mathrm{OP}_{1}$, within a term of order $1 / N$, but if an adsorbed solid floats across the surface while retaining a $\sqrt{3} \times \sqrt{3}$ structure, $\mathrm{OP}_{2}$ will remain close to unity even though $\mathrm{OP}_{1}$ falls to zero. An additional measure of the commensurability of the surface layer is provided by the quantity $\mathrm{OP}_{\text {comm }}$, defined as the probability that the centre of mass of a molecule lies in a circle centred on a graphite hexagon and of area equal to half that of the hexagon. When the structure is commensurate with the centres of the hexagons, $\mathrm{OP}_{\text {comm }}$ will be unity, whereas for an incommensurate solid or a fluid, $\mathrm{OP}_{\text {comm }} \approx 0.5$. The monitoring of long-range translational order in incommensurate solids requires other order parameters, but useful information can aways be obtained from a study of the in-plane centre-of-mass radial distribution function $g(r)$. Similarly, the choice of appropriate orientational order parameters depends on what type of order will probably develop, and no general recipe can be given. However, the results of section 3 suggest that the dominant orientational order in a simulation based on one of the two quadrupolar potential models is likely to be of either herringbone or pinwheel form. Herringbone order can be monitored via the quantity $\mathrm{OP}_{\text {herr }}$, defined as

$$
\mathrm{OP}_{\text {herr }}=\left\langle\frac{2}{N} \sum_{i}^{\prime} \cos 2 \varphi_{i}\right\rangle,
$$

where $\varphi_{i}$ is the angle between the projection of the molecular axis onto the surface and the $x$ axis of the simulation cell, and the prime indicates that the sum on $i$ is limited to molecules in a single sublattice. Different geometries lead to different results. For example, in a perfect herringbone structure with the $x$ axis taken perpendicular to the glide line, $\mathrm{OP}_{\text {herr }}$ is the same for both sublattices and equal to $-\cos 2 \psi$; for $\mathrm{N}_{2}$-type order and the $x$ axis chosen as in figure 1, the values for the two sublattices are $\mathrm{OP}_{\text {herr }}= \pm \sqrt{ } 3 / 2$. The four-sublattice pinwheel structure can be monitored via the order parameters $\mathrm{OP}_{\text {pin }}$ and $\mathrm{OP}_{\text {wheel }}$, where

$$
\mathrm{OP}_{\text {pin }}=\left\langle\frac{4}{N} \sum_{i}^{\prime} \frac{1}{2}\left(3 \cos ^{2} \alpha_{i}-1\right)\right\rangle,
$$

where $\alpha_{i}$ is the angle between the molecular axis and an axis normal to the surface (the $z$ axis), and

$$
\mathrm{OP}_{\text {wheel }}=\left\langle\frac{4}{N} \sum_{i}^{\prime}\left(\sin ^{2} \alpha_{i} \cos 2 \varphi_{i} \cos 2 \varphi_{\mathrm{ref}}+\sin ^{2} \alpha_{i} \sin 2 \varphi_{i} \sin 2 \varphi_{\mathrm{ref}}\right)\right\rangle,
$$

where $\varphi_{\text {ref }}$ is the average value of $\varphi_{i}$ calculated for molecules in a given sublattice. In a perfect pinwheel structure, $\mathrm{OP}_{\text {pin }}=1$ for molecules in the pin sublattice, i.e. for

those molecules that stand perpendicular to the surface, and $\text{OP}_{\text{pin}} = -0.5$, $\text{OP}_{\text{wheel}} = 1$ for molecules in the three wheel sublattices, i.e. for those molecules that lie flat. Unfortunately, the interpretation of these order parameters is not always straightforward, particularly when the orientational order is of mixed herringbone- pinwheel type. More direct information on the nature and extent of any in-plane orientational order is provided by the in-plane angular distribution function $n(\varphi)$. For herringbone structures, this function will have two sharp peaks separated by $2\psi$, where $\psi$ is defined in figure 5(a), and for pinwheels it will have three peaks separated by $60^\circ$. In a fluid phase, $\text{OP}_{\text{herr}}$ and $\text{OP}_{\text{wheel}}$ will be close to zero and $n(\varphi)$ will be structureless.

### 4.2. Monolayer and near-monolayer coverages
Simulations were carried out for the three potential models at the commensurate density $(\theta = 1)$ and temperatures close to the lower limit at which adsorption occurs experimentally (104 K). Two series of calculations were made. In the first series, the system contained 96 molecules in a periodic cell of dimensions $44.3\,\text{\AA}$ by $34.1\,\text{\AA}$ and arranged initially with $\text{N}_2$-type herringbone order and axes such that $\text{OP}_{\text{her}} = \pm\sqrt{3}/2$. When the 2CLJ potential was used, the solid rapidly melted: the final values of the calculated order parameters $\text{OP}_1$ and $\text{OP}_2$ were close to zero, and the function $n(\varphi)$ showed no evidence of any in-plane orientational order. The results for the quadrupolar models are summarized in table 5 and compared with those obtained in a previous simulation of $\text{N}_2$ on graphite [10]. Models MOM and PRC1 both show a trend towards pinwheel order, as evidenced, in particular, by the development of a three-peak structure in $n(\varphi)$. The evolution from herringbone to pinwheel structure is more clearly developed for model PRC1, behaviour that is consistent with the energy minimization discussed earlier. We recall from section 3 that in both models the commensurate herringbone structure is higher in energy than the commensurate pinwheel, and the energy difference is larger for model PRC1 than for MOM. The values obtained for $\text{OP}_{\text{herr}}$ in the calculations for model PRC1 are not indicative of residual herringbone order, but instead reflect the sys- tematic way in which the four sublattices of the pinwheel structure evolve from the herringbone sublattices. In the second series of calculations, 224 molecules were arranged initially in commensurate pinwheel fashion in a cell $59.1\,\text{\AA}$ by $59.7\,\text{\AA}$. Use of the 2CLJ potential again led to a complete loss of solid-state order; the results for models MOM and PRC1 are given in table 6. Some disorder also occurs for the MOM potential, though inspection of instantaneous configurations, such as that

**Table 5. Results of molecular-dynamics simulations initiated from commensurate, herring- bone structures.**

<table>
  <thead>
    <tr>
      <th>Model</th>
      <th>MOM</th>
      <th>PRC1</th>
      <th>$\text{NO}_2$ [10]</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>$T/\text{K}$</td>
      <td>110</td>
      <td>107</td>
      <td>25</td>
    </tr>
    <tr>
      <td>$\langle V/N\rangle/\text{K}$</td>
      <td>$-$2806</td>
      <td>$-$2794</td>
      <td>$-$1426</td>
    </tr>
    <tr>
      <td>$\text{OP}_1$</td>
      <td>0·68</td>
      <td>0·86</td>
      <td>0·93</td>
    </tr>
    <tr>
      <td>$\text{OP}_2$</td>
      <td>0·57</td>
      <td>0·75</td>
      <td>0·86</td>
    </tr>
    <tr>
      <td>$\langle z\rangle/\text{\AA}$</td>
      <td>3·32</td>
      <td>3·51</td>
      <td>3·40</td>
    </tr>
    <tr>
      <td>$\text{OP}_{\text{herr}}$</td>
      <td>0·39, $-$0·40</td>
      <td>0·42, $-$0·42</td>
      <td>0·72, $-$0·72</td>
    </tr>
    <tr>
      <td>Peaks in $n(\varphi)$</td>
      <td>$0^\circ$, $57^\circ$, $116^\circ$</td>
      <td>$-1^\circ$, $61^\circ$, $117^\circ$</td>
      <td>$15^\circ$, $105^\circ$</td>
    </tr>
  </tbody>
</table>

Table 6. Results of molecular-dynamics simulations initiated from commensurate, pinwheel and incommensurate, T-bone structures.

<table>
<thead>
<tr>
<th rowspan="2">Model</th>
<th colspan="2">Pinwheel</th>
<th colspan="2">T-bone</th>
</tr>
<tr>
<th>MOM</th>
<th>PRC1</th>
<th>MOM</th>
<th>PRC1</th>
</tr>
</thead>
<tbody>
<tr>
<td>$\theta$</td>
<td>1·000</td>
<td>1·000</td>
<td>0·875</td>
<td>0·875</td>
</tr>
<tr>
<td>$T$/K</td>
<td>106</td>
<td>104</td>
<td>104</td>
<td>105</td>
</tr>
<tr>
<td>$\langle V/N \rangle$/K</td>
<td>$-2826$</td>
<td>$-2783$</td>
<td>$-2907$</td>
<td>$-2850$</td>
</tr>
<tr>
<td>$\text{OP}_1$</td>
<td>0·46</td>
<td>0·89</td>
<td>$\approx 0$</td>
<td>$\approx 0$</td>
</tr>
<tr>
<td>$\text{OP}_{\text{comm}}$</td>
<td>0·59</td>
<td>0·99</td>
<td>0·52</td>
<td>0·51</td>
</tr>
<tr>
<td>$\langle z \rangle$/Å</td>
<td>3·31</td>
<td>3·50</td>
<td>3·23</td>
<td>3·37</td>
</tr>
<tr>
<td>$\text{OP}_{\text{pin}} \dagger$</td>
<td>0·24</td>
<td>0·75</td>
<td></td>
<td></td>
</tr>
<tr>
<td>$\text{OP}_{\text{pin}} \ddagger$</td>
<td>$-0·43$</td>
<td>$-0·46$</td>
<td>$-0·47$</td>
<td>$-0·46$</td>
</tr>
<tr>
<td>$\text{OP}_{\text{wheel}} \ddagger$</td>
<td>0·79</td>
<td>0·93</td>
<td>0·92</td>
<td>0·93</td>
</tr>
<tr>
<td>$\text{OP}_{\text{herr}}$</td>
<td></td>
<td></td>
<td>$0·93,\ -0·93$</td>
<td>$0·95,\ -0·95$</td>
</tr>
<tr>
<td>Peaks in $n(\varphi)$</td>
<td>$54^\circ,\ 113^\circ,\ 174^\circ$</td>
<td>$50^\circ,\ 110^\circ,\ 171^\circ$</td>
<td>$0^\circ,\ 89^\circ$</td>
<td>$0^\circ,\ 89^\circ$</td>
</tr>
</tbody>
</table>

$\dagger$ Pin sublattice.
$\ddagger$ Wheel sublattices.

pictured in figure 6(a), suggests that this is associated with the growth of regions of herringbone order rather than with any solid-fluid transition. The herringbone regions are almost certainly incommensurate, which accounts for the low values obtained for $\text{OP}_1$, $\text{OP}_2$ and $\text{OP}_{\text{comm}}$. The function $n(\varphi)$ has the expected three-peak structure, but there is a substantial background and the peak heights are not all equal. The results for model PRC1, by contrast show that the initial commensurate pinwheel structure persists throughout the simulation; a typical configuration is shown in figure 6(b).

Low-temperature runs were also carried out for models MOM and PRC1 for systems of 196 molecules at a coverage $\theta = 0.875$. The molecules were arranged initially in T-bone order, which at this coverage is the structure of minimum energy for both models (see section 3); the $x$ axis was chosen such that $\text{OP}_{\text{herr}} = \pm 1$ in the ideal structure. The solid is commensurate with the graphite only to the extent that the spacing of molecules must be consistent with the periodic boundary conditions. The initial structure povered to be highly stable, as shown by the order parameters $\text{OP}_{\text{herr}}$ given in table 6. The distribution function $n(\varphi)$ retains a two-peak structure throughout, with the peaks separated by approximately $90^\circ$. A configuration from the MOM simulation is shown in figure 7.

The quantities $\langle V/N \rangle$ recorded in tables 5 and 6 are the mean potential energies per molecule. These results are to be compared with an experimental value, estimated from the heat of adsorption at 120 K, of 2915 K [21]. Given the discrepancies in the molecule-surface potential energies (see section 2.2), the agreement with experiment is fair, and it would not be possible to discriminate between the two models on this basis alone. The potential energies of the bulk MOM and PRC1 crystals at 120 K are respectively $-2992$ K and $-2996$ K [22]. Thus the bulk phase is in both cases energetically favoured with respect to the adsorbed solid. This is consistent with the expected desorption of $\text{CO}_2$ below 104 K and implies that at higher temperatures the monolayers are entropically stabilized.

![](./images/812081908514029569_8.jpg)

![](./images/812081908514029569_9.jpg)

Figure 6. Instantaneous configurations from simulations started in commensurate $\sqrt{3} \times \sqrt{3}$ pinwheel structures: (a) the MOM model at 105 K; (b) the PRC1 model at 108 K.

![](./images/812081908514029569_10.jpg)

Figure 7. Instantaneous configuration from the MOM simulation of the T-bone solid at $\theta=0.875$, $T=101$ K.

The stable solid structures obtained with the MOM and PRC1 potentials all disorder and eventually melt when heated to sufficiently high temperatures. The results plotted in figure 8 show how the potential energy per molecule and the order parameter $\text{OP}_{\text{herr}}$ change with temperature in the case of the T-bone solids at $\theta=0.875$. The behaviour close to melting is suggestive of a first-order transition; the estimated melting temperatures are $135\pm3$ K (MOM) and $146\pm3$ K (PRC1). Qualitatively similar changes with temperature are observed for the PRC1 model when set up in the commesurate pinwheel structure ($\theta=1$); the melting temperature in this case is $155\pm3$ K. All the monolayers studied melt by promotion of molecules to a second layer. This is evident from the form of the density distribution normal to the surface and the fact that the average molecule-surface potential energy per molecule (not shown) increases abruptly by about 100 K in the region of the transition. As an example, in the PRC1 simulation at 155 K, approximately 3% of molecules are to be found in the second layer.

The experiments of Terlain and Larher [9] suggest that solid-liquid transitions occur only below 124 K. The melting temperatures obtained here are all higher than the experimental upper limit. In the models we have used, the reduction of the dispersion interaction by substrate mediation [24] has been ignored. Such a reduction could well lead to a lowering of the predicted melting temperatures, but trial calculations that we have carried out suggest that the effect is small. However, experiments on other systems have shown that the experimental solid-liquid boundary can shift to much higher temperatures as the coverage increases towards monolayer completion [25]. The increase in melting temperature under such conditions is associated with a change in mechanism from lateral melting at submonolayer densities to second-layer promotion close to full coverage. With these points in mind,

![](./images/812081908514029569_11.jpg)

Figure 8. Results from simulations of the T-bone monolayers at $\theta=0.875$: potential energy(a) and herringbone order parameter (b) against temperature: +-+, model MOM;■----■, model PRC1 (the lines are drawn as guides to the eye).

we have carried out a number of other calculations for models MOM and PRC1 at coverage of half a commensurate monolayer $(\theta=0.5)$.

### 4.3. Submonolayer coverages
A number of different calculations have been made at a coverage $\theta=0.5$. In most cases the simulations were carried out for systems of 128 molecules in a cell $59 \cdot 1 \AA$ by $68 \cdot 2 \AA$. The molecules were organized in a rectangular strip that spanned the cell in the $x$ direction and was bordered on two sides, along the $y$ axis, by empty surface; the value $\theta=0.5$ refers to the surface as a whole, and the density of the molecules within the strip is of course approximately twice what that figure would suggest. The onset of melting was monitored by calculation of the density profile $p(y)$ in the $y$ direction, and figure 9 shows some of the results obtained for the PRC1 potential when the starting configuration was a commensurate pinwheel. At $104 \mathrm{~K}$, the pinwheel structure was stable throughout the run. Some expansion of the strip is evident in figure $9(a)$; molecules at the edges have moved away from the centres of the graphite hexagons, but there are no gas-like molecules. On heating to $110 \mathrm{~K}$, there was a loss of translational order at the edges of the strip, and study of the configurations showed that certain of the pin molecules had fallen down towards

![](./images/812081908514029569_12.jpg)

![](./images/812081908514029569_13.jpg)

![](./images/812081908514029569_14.jpg)

![](./images/812081908514029569_15.jpg)

Figure 9. Density profiles for the PRC1 pinwheel monolayer: (a) 104 K; (b) 110 K; (c) 120 K;
(d) 118 K.

the surface. The structure seen in figure 9(b) suggests that the system is now incom- mensurate but remains solid-like. When heated to 120 K, however, the strip appeared to melt; in figure 9(c), the sharp features characteristic of the solid have vanished, although the molecule-surface potential continues to modulate the density profile. Attempts to heat the system further led to the growth of solid-like clusters of herringbone order, the average temperature fell back to 118 K, after equilibrium and sharp peaks reappeared in p(y) (see figure 9(d)). Thus the apparent melting tran- sition has more the character of a transition between two solid phases. The change in orientational order can also be seen in the behaviour of the radial distribution function g(r). Figure 10 shows the results obtained at 120 K and 118 K. At 120 K there is a well-defined double peak, centred around $r=8 \AA$, that can be associated with a triangular pinwheel structure, while at 118 K the appearance of a weak peak close to $r=6 \AA$, together with the peak at $8.4 \AA$, is suggestive of a degree of T-bone ordering. The corresponding angular distribution functions are plotted in figure 11. At temperatures below the transition, the distribution has the three-peak structure characteristic of pinwheel order, with peaks separated by $60^{\circ}$; at 118 K, however, there is a loss of intensity in one of the peaks, and the two stronger peaks have moved apart to a separation closer to that expected for a T-bone structure. The growth of T-bone order can also be seen in the configuration pictured in figure 12. We conclude that the commensurate pinwheel structure is unstable at this coverage, and that herringbone order spontaneously develops. As a check, we have carried out a further simulation for a square patch of 96 PRC1 molecules arranged with pin- wheel ordering at the centre of a much larger cell. Such a patch should be less stable than the strip, since the ratio of boundary length to surface area is larger. In this

![](./images/812081908514029569_16.jpg)

Figure 10. Radial distribution function of molecular centres in the plane of the surface for the PRC1 pinwheel monolayer: ——, $T=120$ K; - - - -, 118 K.

![](./images/812081908514029569_17.jpg)

Figure 11. In-plane angular distribution function for the PRC1 pinwheel monolayer: ——, $T=120$ K; - - - -, 118 K.

case, pinwheel order begins to disappear at 106 K, with herringbone structure grad- ually replacing it. On the other hand, a square patch of 196 molecules arranged initially with T-bone order remained solid-like up to at least 125 K.

Calculations in the strip geometry and with initial pinwheel ordering were also made for the MOM potential. This system proved to be even less stable than when the PRC1 potential was used, with clusters of herringbone-ordered molecules

![](./images/812081908514029569_18.jpg)

Figure 12. Instantaneous configuration from the simulation of the PRC1 strip ($\theta=0.5$) at $T=118$ K. Note the clusters of herringbone-ordered molecules.

![](./images/812081908514029569_19.jpg)

Figure 13. Herringbone order parameters for the strips at $\theta=0.5$: $+ - +$, model MOM;
$\boldsymbol{\blacksquare}----\boldsymbol{\blacksquare}$, model PRC1. Results are expressed relative to the values for the ideal
structures and averaged over the two sublattices.

already appearing at a temperature of 100 K. That such a difference in behaviour
between the two models would be found at low coverage could have been antici-
pated from the results previously obtained at $\theta=1$.

Finally, the strip geometry was used to study the effect of temperature on the
stability of the minimum-energy incommensurate herringbone structures discussed
in section 3. In practice, small changes in the ideal, minimum-energy structures had
to be made in order to accommodate an integral number of $CO_{2}$ unit cells along the
$x$ axis of the simulation cell. The distribution function $n(\varphi)$ in the ideal structures
consists of two delta-function peaks separated by $2\psi=67^{\circ}$ (MOM) or $90^{\circ}$ (PRC1).
Increase in temperature led to a growth in the background, but no systematic shift
in the peak positions was observed. The behaviour with temperature is therefore
best described as a progressive loss of herringbone order, which leads eventually to
a liquid state in which all orientational order with respect to the surface is lost. The
temperature dependence of the herringbone order parameters is shown in figure 13.

From these results, we estimate that melting occurs at $116\pm3$ K (MOM) and
$122\pm3$ K (PRC1), results that are more in line with the experimental values than
those obtained at full coverage.

## 5. Discussion

If the results obtained with the 2CLJ potential are disregarded, all the evidence
from our calculations is that $CO_{2}$ physisorbed on graphite at less than monolayer
coverages adopts a two-sublattice incommensurate herringbone structure. Since there
are few grounds for discriminating between the two quadrupolar models we have
used, it is not useful to speculate as to whether the likely herringbone packing is the
T-bone order predicted for model PRC1 or the less-symmetric arrangement
favoured by model MOM. When set up in these structures, the low-coverage solids
are stable throughout the experimentally relevant range of temperature and have
approximately the correct melting points. The situation at densities close to mono-
layer completion is less clear. The existence of a stable four-sublattice pinwheel
structure is a possibility, but this conclusion rests heavily on results obtained with a
model (PRC1) that has an artificially enhanced quadrupole moment, a feature of the

potential for which no real justification has yet been offered and one that does not fit easily with current ideas on intermolecular forces [26]. We have also adopted a particularly simple representation of the molecule-surface interaction that neglects a number of possibly important physical effects. Refinement of the potentials could certainly be attempted, but perhaps the more pressing need is for a wider range of experimental data: the existing measurements of adsorption isotherms should if possible be supplemented by calorimetric studies and diffraction experiments.

We are grateful to the SERC for support under Special Grant GR/E 68716. We wish also to thank Dr R. M. Lynden-Bell for many helpful discussions.

## References

[1] DIEHL, R. D., and FAIN, S. C., 1983, *Surf. Sci.*, **125**, 116.
[2] MORISHIGE, K., MOWFORTH, C., and THOMAS, R. K., 1985, *Surf. Sci.*, **151**, 289.
[3] JosHI, Y. P., TILDESLEY, D. J., AYRES, J. S., and THOMAS, R. K., 1988, *Molec. Phys.*, **65**, 991.
[4] TERLAIN, A., LARHER, Y., ANGERAND, F., PARETTE, G., LAUTER, H., and BASSIGNANA, I. C., 1986, *Molec. Phys.*, **58**, 799.
[5] HARRIS, A. B., and BERLINSKY, A. J., 1979, *Can. J. Phys.*, **57**, 1852.
[6] TONEY, M. F., DIEHL, R. D., and FAIN, S. C., 1983, *Phys. Rev. B*, **27**, 6413.
[7] BELAK, J., KOBASHI, K., and ETTERS, R. D., 1985, *Surf. Sci.*, **161**, 390.
[8] GRAHAM, C., PIERRUS, J., and RAAB, R. E., 1989, *Molec. Phys.*, **67**, 939.
[9] TERLAIN, A., and LARHER, Y., 1983, *Surf. Sci.*, **125**, 304.
[10] TALBOT, J., TILDESLEY, D. J., and STEELE, W. A., 1984, *Molec. Phys.*, **51**, 1331.
[11] BHETHANABOTLA, V. R., and STEELE, W. A., 1987, *Langmuir*, **3**, 581.
[12] PETERS, C., and KLEIN, M. L., 1985, *Molec. Phys.*, **54**, 895.
[13] MOLLER, M. A., and KLEIN, M. L., 1989, *Chem. Phys.*, **129**, 235.
[14] MOLLER, M. A., and KLEIN, M. L., 1989, *J. chem. Phys.*, **90**, 1960.
[15] SINGER, K., TAYLOR, A., and SINGER, J. V. L., 1977, *Molec. Phys.*, **33**, 1757.
[16] MURTHY, C. S., O'SHEA, S. F., and MCDONALD, I. R., 1983, *Molec. Phys.*, **50**, 531.
[17] PROCACCI, P., RIGHINI, R., and CALIFANO, S., 1987, *Chem. Phys.*, **116**, 171.
[18] STEELE, W. A., 1973, *Surf. Sci.*, **36**, 317.
[19] ALLEN, M. P., and TILDESLEY, D. J., 1987, *Computer Simulation of Liquids* (Clarendon).
[20] BEEBE, R. A., KISELEV, A. V., KOVALEVA, N. V., HOLMES, J. M., and CHAMPLIN, M. E. R., 1964, *Russian J. phys. Chem.*, **38**, 506.
[21] BRUCH, L. W., 1983, *J. chem. Phys.*, **79**, 3148.
[22] JosHI, Y. P., and TILDESLEY, D. J., 1985, *Molec. Phys.*, **55**, 999.
[23] CARLOS, W. E., and COLE, M. W., 1980, *Surf. Sci.*, **91**, 339.
[24] MCLACHLAN, A. D., 1963, *Molec. Phys.*, **7**, 381.
[25] CHAN, M. H. W., MIGONE, A. D., MINER, K. D., and LI, Z. R., 1984, *Phys. Rev. B*, **30**, 2681.
[26] STONE, A. J., and PRICE, S. L., 1988, *J. phys. Chem.*, **92**, 3325.