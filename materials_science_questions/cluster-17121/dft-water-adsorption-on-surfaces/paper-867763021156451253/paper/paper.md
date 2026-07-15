# Global Potential Energy Minima of $({\rm H_2O})_n$ Clusters on Graphite

B. S. González, J. Hernández-Rojas, J. Bretón, and J. M. Gomez Llorente*

Departamento de Física Fundamental II
Universidad de La Laguna, 38205 Tenerife, Spain

September 5, 2021

## Abstract
Likely candidates for the global potential energy minima of $({\rm H_2O})_n$ clusters with $n \leq 21$ on the (0001)-surface of graphite are found using basin-hopping global optimization. The potential energy surfaces are constructed using the TIP4P intermolecular potentials for the water molecules (the TIP3P is also explored as a secondary choice), a Lennard-Jones water-graphite potential, and a water-graphite polarization potential that is built from classical electrostatic image methods and takes into account both the perpendicular and parallel electric polarizations of graphite. This potential energy surface produces a rather hydrophobic water-graphite interaction. As a consequence, the water component of the lowest graphite-$({\rm H_2O})_n$ minima is quite closely related to low-lying minima of the corresponding TIP4P $({\rm H_2O})_n$ clusters. In about half of the cases the geometrical substructure of the water molecules in the graphite-$({\rm H_2O})_n$ global minimum coincides with that of the corresponding free water cluster. Exceptions occur when the interaction with graphite induces a change in geometry. A comparison of our results with available theoretical and experimental data is performed.

*Correponding author. E-mail address: jmgomez@ull.es

# 1 Introduction

The interaction of carbonaceous materials such as fullerenes, carbon nanotubes and graphite with atoms and molecules share many properties. In particular, in this work we will be concerned with the interaction between water and graphite. A deep understanding of the features and properties of this interaction is of particular interest in technological applications, such as those related with the use of water as a lubricant for graphite [1, 2], and, more indirectly, in the behavior of water at the nanometer scales when material related to graphite, such as carbon nanotubes, are present. Water-graphite interaction is also relevant in the design of corrosion-free combustion chambers and rocket nozzles, since water is a universal combustion product and graphite is an important surface material because of its chemical inertness under extreme conditions [3]. Other fields benefiting from this knowledge include the environmental sciences [4] and astrophysics [5], since graphite is a good candidate for the composition of nano particles and dust grains.

Despite the natural abundance of water and graphite, relatively few experimental data are available for their interaction. Studies at low temperature ($T = 85$ K) and low coverage using temperature programed desorption and vibrational high resolution electron energy loss spectroscopy have shown that water is adsorbed non dissociatively on the graphite surface forming hydrogen bonded aggregates with a two dimensional structure that changes into a three dimensional one upon warming [6]. The water arrangement for the

two-dimensional structure is unknown, as is also unknown the role played by small water clusters in the growth of these structures.

Experimental information about the water-graphite binding energies and structural aspects is currently lacking even for the water-monomer adsorp- tion. To our knowledge, there are only the early water-graphite binding energy by Kieslev *et al.* (15.0 kJ/mol) [7] and the more recent association energy reported by Kasemo *et al.* [6].

In the last few years some results from theoretical calculations have been made available. Some of these studies are concerned with macroscopic fea- tures of the water-graphite interaction. In this group we can include the work by Werder *et al.* [8], who fit an interaction potential form to experimental data for the contact angle of water nanodroplets on graphite surfaces. A similar scheme is used by Pertsin *et al.* to simulate lubricant properties from a water-graphite interaction that was previously fitted to ab-initio [9] and empirical data [10]. Finally Gatica *et al.* have used empirical water-graphite potentials to look for a wetting transition [11].

*Ab initio* calculations have been recently reported. By using second-order Möller-Plesset perturbation theory, Feller *et al.* [12] have provided the inter- action energy between a water molecule and acenes as large as $\mathrm{C_{96}H_{24}}$; the value of 24 kJ/mol that was obtained for this energy seems to be unphysically high [13]. This conclusion is confirmed by the recent theoretical calculations by Sudiarta and Geldart [14]. Using the same Möller-Plesset scheme for a water molecule on both hydrogen and fluorine terminated acenes, these

3

authors demonstrated the important contribution of this boundary to the water-acene binding energy. After removing this effect and extrapolating to an infinite graphene they reported a value of 10.2 kJ/mol. Density func- tional theory (DFT) total energy calculations were performed by Cabrera Sanfélix *et al.* [15] to study structural aspects of water layers on graphite. Absolute binding energies were not provided and no global energy minimiza- tion was done. These tasks are performed in later calculations using DFT tight-binding methods complemented with empirical van der Waals force corrections (DFTB-D) [3, 16]. In these works, clusters with up to 6 water molecules on graphite are studied and the optimal structures and the bind- ing and association energies were provided. Besides, these results are com- pared with those obtained with integrated ONIOM (ab-intio B3LYP:DFTB- D+semiempirical PM3) methods [3]. In these studies graphite is represented by up to three-layer acenes. In all these DFT studies the acene boundary effects are not removed.

A full empirical approach has been followed by Karapetian *et al.* [13] by using the Dang-Chang model for the water-water interaction and a po- larizable potential model for the water-graphene interaction that includes dispersion-repulsion contributions by means of Lennard-Jones pairwise in- teractions. In this potential the polarization term is built by associating an isotropic polarizable center with each carbon atom. The interaction between these centers, when polarized, is neglected. Again, only clusters with up to 6 water molecules are considered.

A similar empirical approach shall be followed in our present work. Because of its ability to reproduce the structure of water clusters, we will use the TIP4P model for the water-water interaction [17]. In order to analyze dependence of our results on this choice, we shall also consider the TIP3P water-water interaction model [17]. The water-graphite interaction analytic model shall include a dispersion-repulsion term, built from the sum of infinite Lennard-Jones pairwise interactions using the Steele method, and a polarization contribution which shall be built using electrostatic image methods that take into account the anisotropic response of graphite. We shall provide likely candidates for the global potential energy minima of graphite-$({\rm H_2O})_n$ clusters with $n \leq 21$. We shall employ basin-hopping global optimization to identify these global minima. From the structure and energetics of these minima we shall elucidate about the hydrophobic nature of the water-graphite interaction at the lowest temperatures, and the dependence of the results on the potential model.

This paper is organized as follows. In Section 2 we discuss our expression for the potential energy surface as a sum of Coulomb, dispersion-repulsion, and polarization contributions. In Section 3 we present likely candidates for the cluster global potential energy minima together with their association and binding energies. Here we shall compare our values with the available data. Finally, Section 4 summarizes our conclusions.

## 2 The Potential Energy Function

The closed-shell electronic structure of both graphite and water makes an empirical approach to the potential energy surface (PES) for the water-graphite and water-water interactions particularly attractive. We write the potential energy of a graphite-$({\rm H_2O})_n$ cluster as a sum of two contributions

$$
V = V_{\rm ww} + V_{\rm wg}, \tag{1}
$$

where $V_{\rm ww}$ is the sum of pairwise water-water interactions, and $V_{\rm wg}$ is the water-graphite term. For the water-water interaction we have chosen the TIP4P form as a primary choice, but we will also consider the TIP3P model. These models describe each water molecule as a rigid body with two positive charges on the hydrogen atoms and a balancing negative charge either close to the oxygen atom (TIP4P) or just at the oxygen atom (TIP3P), together with a dispersion-repulsion center on the oxygen atom. Hence, $V_{\rm ww}$ is a sum of pairwise additive Coulomb and Lennard-Jones terms. These models have been used in the study of homogeneous water clusters [18, 19, 20], water clusters containing metallic cations [21, 22], and water-${\rm C_{60}}$ clusters [23].

The water-graphite interaction is written as

$$
V_{\rm wg} = V_{\rm dr} + V_{\rm pol}, \tag{2}
$$

where $V_{\rm dr}$ is a sum of pairwise dispersion-repulsion terms between the oxy-

gen and the carbon atoms. Each of these terms is expressed as a Lennard-
Jones potential, whose parameters were obtained using the standard Lorentz-
Berthelot combination rules from the corresponding parameters for the oxygen-
oxygen and carbon-carbon interactions in TIP4P and TIP3P water and Steele
[24] graphene-graphene potentials, respectively. Specifically, we used the val-
ues $\varepsilon_{\text{CO}} = 0.389$ kJ/mol and $\sigma_{\text{CO}} = 3.28$ Å for the TIP4P, and $\varepsilon_{\text{CO}} = 0.385$
kJ/mol and $\sigma_{\text{CO}} = 3.28$ Å for the TIP3P, which are similar to those derived
by Werder *et al.* [8] to fit the contact angle for a water droplet on a graphene
surface. An analytic form for $V_{\text{dr}}$ can be obtained using Steele summation
method [24, 25] over the graphite periodic structure by writing the interac-
tion, $U_{\text{dr}}$, of a dispersion center at the point $(x,y,z)$ with a graphite layer
located at the surface $z = 0$ (the origin of the reference frame is chosen at
the center of a carbon hexagon), as a Fourier series, i.e.

$$
U_{\mathrm{dr}}(x, y, z)=U_{0}(z)+\sum_{l>0} U_{l}(z) f_{l}(x, y) \tag{3}
$$

We have checked that the contribution to this expansion from terms with
$l>1$ is negligible. Up to $l=1$, we have

$$
U_{0}(z)=\frac{8 \pi \varepsilon_{\mathrm{CO}} \sigma_{\mathrm{CO}}^{2}}{\sqrt{3} a_{0}^{2}}\left[\frac{2}{5}\left(\frac{\sigma_{\mathrm{CO}}}{z}\right)^{10}-\left(\frac{\sigma_{\mathrm{CO}}}{z}\right)^{4}\right], \tag{4}
$$

$$
U_{1}(z)=\frac{8 \pi \varepsilon_{\mathrm{CO}} \sigma_{\mathrm{CO}}^{2}}{\sqrt{3} a_{0}^{2}}\left[\frac{1}{60}\left(\frac{2 \pi \sigma_{\mathrm{CO}}^{2}}{\sqrt{3} a_{0} z}\right)^{5} K_{5}(\frac{4 \pi z}{\sqrt{3} a_{0}})-\left(\frac{2 \pi \sigma_{\mathrm{CO}}^{2}}{\sqrt{3} a_{0} z}\right)^{2} K_{2}(\frac{4 \pi z}{\sqrt{3} a_{0}})\right], \tag{5}
$$


and

$$
f_{1}(x, y)=-2\left\{\cos \left[\frac{2 \pi}{a_{0}}\left(x+\frac{y}{\sqrt{3}}\right)\right]+\cos \left[\frac{2 \pi}{a_{0}}\left(x-\frac{y}{\sqrt{3}}\right)\right]+\cos \left[\frac{4 \pi y}{\sqrt{3} a_{0}}\right]\right\},
\tag{6}
$$

where $a_0 = 1.42$ Å is the C-C distance in the graphite layer, $K_m(z)$ are the modified Bessel function of $m^\text{th}$ order, and $f_1(x,y)$ is the first corrugation function. The total dispersion-repulsion interaction is obtained as a sum of $U_\text{dr}$ terms over each graphite layer. We have obtained well converged values by including the $U_0$ contribution from the two upper layers and the first corrugation of the first layer.

In Eq. (2), $V_\text{pol}$ includes the energy associated with the polarization of graphite due to the electric field of all the water point charges. This many-body interaction, which will turn out to be smaller than $V_\text{dr}$, was evaluated using a continuum representation of graphite. We will evaluate two contributions to $V_\text{pol}$,

$$
V_\text{pol} = V_\parallel + V_\perp,
\tag{7}
$$

each one associated, respectively, with the response of graphite to the electric field component parallel and perpendicular to the graphite surface. For the first one, $V_\parallel$, we will assume that graphite behaves as a classical conductor, which allows us to make use of the image charge method to obtain (in Gaussian units)

$$
V_\parallel = -\sum_{i} \frac{q_{i}^{2}}{4 z_{i}}-\frac{1}{2} \sum_{i \neq j} \frac{q_{i} q_{j}}{r_{i j}^{\prime}},
\tag{8}
$$

8

where $q_i$ is each of the water electric point charges and $r'_{ij}$ is the distance between the charge $q_i$ and the image of the charge $q_j$, i.e., $r'_{ij} = [(x_i - x_j)^2 + (y_i - y_j)^2 + (z_i + z_j)^2]^{1/2}$.

In order to evaluate $V_\perp$, we will assume that a graphite layer (at $z=0$) has, in reciprocal space, a surface polarizability density $\alpha_\perp(k_x k_y)$ such that when an electric field depending on the surface point and perpendicular to the layer, $E_\perp(x,y) = \frac{1}{2\pi}\int \mathrm{d}k_x\mathrm{d}k_y e^{-\mathrm{i}(k_x x + k_y y)} \mathcal{E}_\perp(k_x, k_y)$, is applied, an electric dipole density, $I_\perp(x,y) = \frac{1}{2\pi}\int \mathrm{d}k_x\mathrm{d}k_y e^{-\mathrm{i}(k_x x + k_y y)} \mathcal{I}_\perp(k_x, k_y)$, is induced on that layer, with $\mathcal{I}_\perp(k_x k_y) = \alpha_\perp(k_x k_y)\mathcal{E}_\perp(k_x, k_y)$. If we now neglect the dependence of $\alpha_\perp$ on $k_x$ and $k_y$ (which is a valid approximation if $E_\perp(x,y)$ depends smoothly enough on the surface point), then we would have $I_\perp(x,y) = \alpha_\perp E_\perp(x,y)$, with $\alpha_\perp = \alpha_\perp(0,0)$ being the electric polarizability in a uniform electric field perpendicular to the layer. In this way we can calculate the dipole density induced in the graphite layer by an electric charge $q_i$ at the point $(x_i, y_i, z_i)$, and from this dipole density we can evaluate its electric field and the electric force between the polarized layer and that charge. One readily shows that the electric field due to the polarized surface in the half-space of the charge ($z>0$) is equal to the electric field induced by an image dipole $p_i = -2\pi\alpha_\perp q_i$ at the point $(x_i, y_i, -z_i)$ and direction parallel to the $z$ axis. This result can be generalized additively to the case of several electric point charges, all of them located in the space region $z>0$. From the corresponding image dipoles we can obtain their electric force on each

charge, and from here the interaction potential $V_\perp$, namely

$$
V_{\perp}=-\sum_{i} \frac{2 \pi \alpha_{\perp} q_{i}^{2}}{8 z_{i}^{2}}-\frac{1}{2} \sum_{i \neq j} \frac{2 \pi \alpha_{\perp} q_{i} q_{j}\left(z_{i}+z_{j}\right)}{r_{i j}^{\prime 3}}.
\tag{9}
$$

The use of expression (9) requires the knowledge of $\alpha_\perp$. The value of this polarizability density may be estimated from $\varepsilon_\perp$, the relative electric permittivity of graphite for applied electric fields perpendicular to the (0001) surface, whose value is $\varepsilon_\perp = 5.75$. Following Hannay's alternative derivation of the Clausius-Mossotti equation [26], we shall require the form of the diverging term in the expression of the electric field induced by a uniform surface dipole density of magnitude $I_\perp$ and direction perpendicular to the surface. The magnitude of this term is readily found to be $-4\pi I_\perp \delta(z)$. By space averaging it, we obtain the local electric field on each graphite layer $E_{\rm local} = E + 4\pi I_\perp/d$, where $d = 3.35$ Å is the layer-to-layer distance and $E$ is the magnitude of the macroscopic electric field in the medium. Then from the relation $I_\perp = \alpha_\perp E_{\rm local}$, and the expression $P = \frac{(\varepsilon_\perp -1)}{4\pi}E$ relating the volume polarization density $P = I_\perp/d$ and $E$, we arrive at the desired result

$$
\alpha_{\perp}=\frac{d\left(\varepsilon_{\perp}-1\right)}{4 \pi \varepsilon_{\perp}}.
\tag{10}
$$

We obtain by this procedure the value $\alpha_\perp = 0.220$ Å.

Being consistent with our metallic assumption for $V_\parallel$, in the evaluation of the polarization contribution to the water-graphite interaction potential we shall assume total screening of the electric field by the external graphite

surface. Therefore, only the most external graphite layer shall be considered in this evaluation.

We have also checked the relevance of the McLachlan substrate mediated interaction [27] between the water molecules in the presence of the conducting graphite layer and found it to be negligible ($\sim 0.03\%$ of the total interaction energy for the water dimer on graphite); therefore, we shall not include this term in our potential energy.

As mentioned in the Introduction, Karapetian *et al.* [13] have proposed a different model potential for the polarization contribution to the water-graphite interaction energy. These authors locate an isotropic polarizable center at each carbon atom and calculate the polarization energy as a sum of the contributions from each center. This model does not take into account the collective properties of the delocalized $\pi$ electrons and neglects completely all screening effects among the induced dipole moments. We have estimated that these defects of this model lead to an overestimation of the polarization energy by a factor of two for the water monomer.

## 3 Global Potential Energy Minima

Likely candidates for the global potential energy minima of graphite-($\text{H}_2\text{O}$)$_n$ clusters with $n \leq 21$ were located using the basin-hopping scheme [28], which corresponds to the 'Monte Carlo plus energy minimization' approach of Li and Scheraga [29]. This method has been used successfully for both neutral

[28] and charged atomic and molecular clusters [23, 30, 31, 32, 33], along with many other applications [34]. In the size range considered here the global optimization problem is relatively straightforward, but somewhat more costly than in the water-C₆₀ clusters [23]. The global minimum is generally found in fewer than $7 \times 10^4$ basin-hopping steps, independent of the random starting geometry. In some cases, starting out from the $(\mathrm{H}_2\mathrm{O})_n$ global potential minimum, the corresponding global minimum for graphite-$(\mathrm{H}_2\mathrm{O})_n$ is found even faster.

For graphite-$(\mathrm{H}_2\mathrm{O})_n$ clusters, association energies, $\Delta E_\mathrm{a}$, are defined for the process

$$
\text{graphite} + n\mathrm{H}_2\mathrm{O} = \text{graphite-}(\mathrm{H}_2\mathrm{O})_n; \quad -\Delta E_\mathrm{a}. \tag{11}
$$

We also define the water binding energy, $\Delta E_\mathrm{b}$, as the difference between the association energies of graphite-$(\mathrm{H}_2\mathrm{O})_n$ and $(\mathrm{H}_2\mathrm{O})_n$, i.e.

$$
\text{graphite} + (\mathrm{H}_2\mathrm{O})_n = \text{graphite-}(\mathrm{H}_2\mathrm{O})_n; \quad -\Delta E_\mathrm{b}. \tag{12}
$$

The clusters in these expressions are assumed to be in their global minimum. The structures and association energies employed here for the global minima of $(\mathrm{H}_2\mathrm{O})_n$ coincide precisely with those obtained by Wales and Hodges [18] and Kabrede and Hentschke [19].

For comparison with the available data, we plot in Fig. 1 the association and binding energies defined in (11) and (12) as a function of the number of

![](./images/867763021156451253_1.jpg)

Figure 1: Association, $\Delta E_{\mathrm{a}}/n$ (a), and binding, $\Delta E_{\mathrm{b}}$ (b), energies per water molecule, for the global minima of water-graphene clusters. Our results: circles for TIP4P and diamonds for TIP3P. Other calculations: DFTB-D [16] (crosses); DFTB-D [3] (asterisks); empirical [13] (up triangles); ONIOM [3] (down triangles); Möller-Plesset [14] (square, only for $n=1$).

water molecules, $n \leq 6$, for water on graphene. Our energies for the TIP3P model are somewhat higher than those for the TIP4P. With the exception of the ONIOM data, our binding and association energies are systematically lower and higher, respectively, than the *ab initio* and other empirical potential values. However, it is well known that DFT methods tend to overestimate the binding energies. Furthermore, the acene-boundary effects discussed in the Introduction have not been removed in the *ab initio* calculations, except in Sidarta and Geldart's binding energy for the water monomer. It is also relevant to remind here the overestimation of the polarization energy that takes place in the empirical potential model by Karapetian *et al.*, as mentioned at the end of Section 2. Taking all these facts into account, we can conclude that the binding energies provided by our interaction model are quite reliable.

Associations energies for $n \geq 2$ are dominated by the water-water interaction. As far as the empirical potential data are concerned, differences in these association energies are a consequence of the different water-water model interaction used in each case. The lower *ab initio* values reported by Xu *et al.* can be attributed to the poor description of the water-water interaction in their DFTB-D scheme.

The structures of the lowest minima obtained for graphene-$({\rm H_2O})_n$ with $1 < n \leq 6$ coincide with those provided by the other available calculations and with the structures that we will obtain later for the graphite-$({\rm H_2O})_n$ clusters. For $n=1$, our calculation, as the one done by Karapetian *et al.*,

provides an $\text{H}_2\text{O}$ molecule with an OH bond pointing towards the graphene and the oxygen atom just over the center of a carbon hexagon ring. On the other hand, the *ab initio* data provide a two-legged conformation with the two OH bonds pointing towards graphene in a symmetric way. This might be understood as the result of quantum zero-point-energy effects, since the difference in energy between the two geometries may be of the order of the zero point energy.

The association $(\Delta E_\text{a}/n)$ and binding energies $(\Delta E_\text{b})$ for the full graphite- $(\text{H}_2\text{O})_n$ clusters, which have been calculated as described in Section 2 with the TIP4P water-water interaction, are plotted in Fig. 2. We also in- clude in Fig. 2(a) the values of the polarization energy $V_\text{pol}$ and water- graphite dispersion-repulsion energy $V_\text{dr}$, as defined in Section 2, for the clus- ter global minima. The term $V_\text{pol}$ oscillates with $n$ around an average value of $\overline{V}_\text{pol}=3.33\,\text{kJ/mol}$; the two contributions to $V_\text{pol}$, $V_\parallel$ and $V_\perp$, are similar in magnitude with $V_\parallel$ somewhat larger than $V_\perp$. The term $V_\text{dr}$ fluctuates also around a slowly growing average as the number of water molecules close to the graphite surface increases. On average, each of these water molecules contributes about $7.26\,\text{kJ/mol}$ to $V_\text{dr}$. The water-graphite binding energies correspond quite closely to the sum of $V_\text{pol}$ and $V_\text{dr}$, while the association energies are dominated by the water-water interaction. The average value of the association energy per molecule in homogeneous TIP4P $(\text{H}_2\text{O})_n$ clusters with $6\leq n\leq21$ is $\sim42\,\text{kJ/mol}$ [18, 19]. For water cluster on graphite the corresponding value turns out to be $44.6\,\text{kJ/mol}$, which is comparable with

![](./images/867763021156451253_2.jpg)

Figure 2: (a) Polarization $V_{\rm pol}$ (dashed line) and dispersion-repulsion $V_{\rm dr}$ (full line) contributions to the potential energy of global minimum graphite-$({\rm H_2O})_n$ clusters. (b) The corresponding association energies per water molecule, $\Delta E_{\rm a}/n$ (full line), and binding energies, $\Delta E_{\rm b}$ (dashed line). Global minima in which the structure of the $({\rm H_2O})_n$ moiety differs from the global minimum of the corresponding TIP4P $({\rm H_2O})_n$ cluster are marked according to the discussion in the text.

the experimental value of $43.4 \pm 2.9\,\text{kJ}/\text{mol}$ [6]. Any of these values corresponds to the binding energy of a water molecule in a water cluster, and it is much larger than the energy for binding a water molecule onto the graphite surface. This energy balance would support an hydrophobic nature of the water-graphite interaction.

For $n=1$ we obtain a binding energy $\Delta E_{\text{a}} = \Delta E_{\text{b}} = 8.81\,\text{kJ}/\text{mol}$. This value is somewhat larger than our TIP4P binding energy for a water molecule on graphene ($\Delta E_{\text{b}} = 7.6\,\text{kJ}/\text{mol}$), and for the corresponding $\text{C}_{60}$-($\text{H}_2\text{O}$) cluster ($\Delta E_{\text{b}} = 6.31\,\text{kJ}/\text{mol}$) [23]. Thus, the numbers provided above for the binding energies of these three compounds are, at least, physically consistent. In the present case, the contribution of the polarization energy to the graphite-$\text{H}_2\text{O}$ binding energy is $2.08\,\text{kJ}/\text{mol}$; the corresponding value in the $\text{C}_{60}$-($\text{H}_2\text{O}$) cluster was $2.32\,\text{kJ}/\text{mol}$ [23]. This larger value is a consequence of the important small-size quantum effects that make the polarizability of the $\text{C}_{60}$ molecule significantly larger than that of a conducting sphere with the geometrical $\text{C}_{60}$ radius [35]. The polarization energy is responsible for orienting the $\text{H}_2\text{O}$ molecule with an OH bond pointing towards the graphite surface and the oxygen atom just over the center of a hexagonal carbon ring (Fig. 3).

The angle between the water $\text{C}_2$ symmetry axis and our $z$-axis in the $n=1$ global minimum is 39.8 degrees, practically identical to the corresponding value in the $\text{C}_{60}$-($\text{H}_2\text{O}$) cluster (40.4 degrees) [23] and close to the experimental value in benzene (37 degrees) [36]. A different water orientation

![](./images/867763021156451253_3.jpg)

Figure 3: Two views of the global minimum obtained for graphite-($\text{H}_2\text{O}$).
This figure, and those that follow, were prepared using the program XCrys-
Den [38].

with the two OH bonds pointing towards the graphite surface is also a local
minimum, but it has a slightly lower binding energy ($\Delta E_{\rm b}=8.67\,\text{kJ/mol}$).
The energy difference between this minimum and the global minimum ($\sim$
$0.14\,\text{kJ/mol}$) is so small that zero point energy effects might as well favor
the two-legged structure as the vibrationally averaged quantum global min-
imum [14]. The equilibrium distance in the global minimum between the
oxygen and the graphite surface is $3.12\,\text{\AA}$, which is very close to the *ab initio*
value ($3.04\,\text{\AA}$) [16] and the corresponding values in water-$\text{C}_{60}$ ($3.19\,\text{\AA}$) [23]
and water-benzene (experimental, $3.33\,\text{\AA}$) [36].

The structures of the TIP4P lowest minima obtained for graphite-($\text{H}_2\text{O})_n$
are presented in Fig. 4.

Due to the hydrophobic nature of the water-graphite interaction, the wa-
ter substructure is often very similar to that in the corresponding global
minimum of TIP4P ($\text{H}_2\text{O})_n$ [18, 19]. In some cases the structures are ac-
tually identical (aside from minor differences in angles and distances). The

![](./images/867763021156451253_4.jpg)

Figure 4: Likely global minima obtained for graphite-$(H_2O)_n$ clusters.

exceptions are labeled in Fig. 2: for those indicated by an asterisk ($n = 6, 7, 11, 15, 17, 19, 21$) the water substructure corresponds to a low-lying local minimum of TIP4P $(\mathrm{H}_2\mathrm{O})_n$, rather than the global minimum. The energy penalty for this choice is mainly compensated by a more favorable dispersion-repulsion contribution to the interaction energy with graphite, which arises from a larger water-graphite contact area. For example, in the graphite-$(\mathrm{H}_2\mathrm{O})_6$ global minimum the geometry of the water moiety corresponds to the "book" structure, which has also been identified as the lowest minimum in the corresponding water-$\mathrm{C}_{60}$ cluster [23]. For the sizes in question, there also exists a higher energy local minimum in which the water substructure corresponds to the global minimum for TIP4P $(\mathrm{H}_2\mathrm{O})_n$. The difference between the association energies of the global and local minimum structures of each of these graphite-$(\mathrm{H}_2\mathrm{O})_n$ clusters is 6.36, 4.11, 1.62, 1.66, 13.04, 16.39 and 9.41 kJ/mol for $n = 6, 7, 11, 15, 17, 19$, and 21, respectively.

For the clusters labeled with a circle in Fig. 2 ($n = 9, 12, 13$) the water substructure corresponds to a perturbation of the TIP4P $(\mathrm{H}_2\mathrm{O})_n$ global minimum. In other words, relaxing the water moiety in the absence of graphite does not lead to a nearby local minimum, in contrast to the cases above. These graphite-$(\mathrm{H}_2\mathrm{O})_n$ structures appear to be favored by polarization contribution in the case $n = 12$ (only the hydrogen-bond pattern is modified), and both dispersion and polarization contributions for the other two cases.

Notice that the structure of the water moiety up to $n = 6$ are basically planar with an average oxygen-graphite distance $\overline{z}_{\mathrm{O}} = 3.22$ Å; the $n = 7$

cluster corresponds to a transition to two-layer water clusters ($\overline{z}_{\rm O}=4.0$
$\text{\AA}$), and in the range $8\leq n\leq21$, we have always two-layer water structures
($\overline{z}_{\rm O}=4.53\ \text{\AA}$) in which the clusters with odd $n$ have one more water molecule
in the layer closer to the graphite surface.

The complete two-layer water structures for even $n$ are precisely the struc-
tures of the global TIP4P free water clusters. Therefore, these structures
interact with graphite in an optimal way and they keep their structure in
the corresponding water-graphite clusters. On the other hand, for odd $n$,
the free water global minima do not show optimal surfaces for its interaction
with graphite, thus explaining why these clusters change their structure to
minimize that interaction energy. The chosen new structures are sensibly
determined by those of either the $n-1$ or $n+1$ clusters. Other water-water
potential models do not produce this alternating behavior in the structure
of the free water global minima and, therefore, we can expect also different
behavior in the water-graphite global minima for $n\geq8$, as some preliminary
results with the TIP3P model seem to confirm.

The alternating behavior found in the structures of the water-graphite
global minima determines the behavior of the second energy differences.
These account for the relative cluster stability and their values for associ-
ation and binding energies, per water molecule, are plotted in Fig. 5. For
$n>7$, we observe an oscillation of period $\Delta n=2$, which corresponds to the
discussed even-odd alternating structures. The data for the association ener-
gies indicate that clusters with even $n$ are more stable than their neighbors.

![](./images/867763021156451253_5.jpg)

Figure 5: Second energy differences per water molecule for the association energies (full line) and binding energies (dashed line) of water-graphite clus- ters.

This pattern is in complete correlation with the corresponding behavior of the TIP4P free water global minima. Fig. 5 shows that, in general, second differences for binding and association energies are anticorrelated. The in- creased stability seen in the binding energies of odd $n$ clusters relative to their neighbors is due to their extra water molecule in close contact with the graphite surface. From these features we conclude that the water-water interaction certainly dominates the observed relative cluster stability. Par- ticularly stable clusters occur for $n=4,8,12,16,20$.

In the light of the preceding results, one could ask a couple of questions that are relevant to assert the hydrophobic nature of the water-graphite in- teraction: Are there for $n \geq 7$ water-graphite local minima structures, close in energy to the global minima, in which the water molecules grow into a sin- gle layer (wetting structures)? How much larger should the water-graphite

interaction be for the previous wetting structures to become the most sta- ble ones? Answering to the second question, we have found that we had to multiply the value of the Lennard-Jones parameter $\varepsilon_{\mathrm{CO}}$ by almost a factor of two for a wetting structure to become the global minimum. This is con- sistent with the analysis performed by Werder *et al.* [8] for the monomer binding energy required to produce a wetting behavior. By relaxing the wet- ting structures found by this procedure to the closest local minimum of our original potential we have found that these wetting local minima lie $\sim 2.2$ kJ/mol per water molecule above the global minimum. Although these val- ues are smaller than those found in $\mathrm{C}_{60}(\mathrm{H}_{2}\mathrm{O})_{n}$ clusters [23], the hydrophobic nature of the water-graphite interaction is also a quite robust property that would require unphysical changes in our model potential to modify it.

We have already shown by making use of the TIP3P potential that the structures of the global minima of the first six water-graphite clusters are going to depend weakly on the model chosen for the water-water interaction. However the dependence found in the structure of the water-graphite global minima on the structure of the corresponding free water clusters and the known dependence of the latter on the water-water interaction model for $n>6$, would imply changes in the structure of these larger water-graphite clusters when a different water model is chosen. Preliminary results confirm this prediction, with changes that are more significant than those found for $\mathrm{C}_{60}(\mathrm{H}_{2}\mathrm{O})_{n}$ clusters.

## 4 Conclusions

Using a theoretically guided empirical potential energy surface and basin-hopping global optimization we have characterized the geometrical structures and energetics of likely candidates for the global potential energy minima of graphite-$({\rm H_2O})_n$ clusters up to $n=21$. The structures of these minima for $1<n\leq6$ coincide with those provided by other available calculations. For $n>2$, association energies are dominated by the water-water interaction while the main contribution to the binding energies comes from the dispersion energy. Our potential energy surface provides a rather hydrophobic water-graphite interaction at the nanoscopic level. As a consequence of this property the water substructure in the lowest energy clusters often corresponds closely to a low-lying minimum of the appropriate $({\rm H_2O})_n$ cluster. In most cases the structure is simply a slightly relaxed version of the global minimum for $({\rm H_2O})_n$. However, the presence of graphite can induce changes in geometry of the water moiety.

For $n=6,7,11,15,17,19,21$ the water substructure is based on a local minimum of $({\rm H_2O})_n$, which is close in energy to the global minimum. The energy penalty for this choice is mainly compensated by the dispersion-repulsion contribution to the interaction energy, because the change in structure gives rise to a larger water-graphite contact surface. For $n=12$ the water substructure is based on a deformation of the free $({\rm H_2O})_{12}$ with the same oxygen framework as the global minimum, but a different hydrogen-bonding pattern.


The different orientation of some of the OH bonds close to the graphite surface increases the polarization energy, which stabilizes the structure. Finally, for $n=9$ and 13 the water substructure involves a more significant deformation of the global minimum, the energy penalty being compensated by both the polarization and dispersion terms. A clear alternating behavior in which the water moiety of the clusters with even $n$ keep the structure of the corresponding free water clusters, while their odd $n$ neighbors change it, has been observed; this behavior has been shown to be completely correlated with that of the free water clusters, namely $(\mathrm{H}_{2}\mathrm{O})_{n}$ clusters with even $n>6$ present faces that interact with graphite in an optimal way, while those with odd $n$ do not show this feature.

Our potential energy surface also supports, for $n>6$, wetting local minima in which the water molecules grow into a single layer. The potential energies of these structures lie at least $2.2\mathrm{kJ/mol}$ per water molecule above the global minima. The presence of the graphite surface is necessary to stabilize the monolayer which otherwise collapses in the cases we have considered. In this respect, we have also found that in order to make the wetting local minima to become the cluster global minima we should increase the magnitude of the graphite-water interaction to unphysically high values. This implies that the hydrophobic nature of the water-graphite interaction at very low temperature is a quite robust property that would require unphysical changes in our model potential to modify it.

In order to study the dependence of our qualitative picture on the model

chosen for the water-water interaction (the TIP4P potential was our primary choice), we have repeated our calculations for the TIP3P potential for $n \leq$ 6. The global minimum structures found for these clusters coincide with those of the TIP4P model. However the dependence found in the structure of the water-graphite global minima on the structure of the corresponding free water clusters and the known dependence of the latter on the water-water interaction model for $n > 6$, would imply changes in the structure of these larger water-graphite clusters when a different water model is chosen. Preliminary results the TIP3P model potential confirm this prediction.

The lowest energy structures obtained in the present work will be made available for download from the Cambridge Cluster Database [37].

## Acknowledgments
This work was supported by 'Ministerio de Educación y Ciencia (Spain)' and 'FEDER fund (EU)' under contract No. FIS2005-02886. One of us (BSG) also aknowledges 'Ministerio de Educación y Ciencia (Spain)' for an FPU fellowship, Dr. González de Sande for his help with code parallelization, and Cambridge University Chemical Laboratories for the use of their com- putational facilitites. We thank Dr. D. J. Wales for his comments on the manuscript.

## References

[1] Lancaster, J. K.; *Tribology Int.* **1990**, 23, 371.

[2] Zaidi, H.; Paulmier D.; Lapage, J.; *Appl. Surf. Sci.* **1990**, 44, 221.

[3] Xu, S.; Irle, S.; Musaev, A. G.; Lin, M. C. *J. Phys. Chem. A* **2005**, *109*, 9563.

[4] Popovicheva, O. P.; Persiantseva, N. M.; Trukhin M. E.; Rulev, G. B.; Shonija, N. K.; Buriko, I. I.; Starik, A. M.; Demirdjian, B.; Ferry, D.; Suzane, *J. Phys. Chem. Chem. Phys.* **2000**, 2, 4421.

[5] Draine, B. T. *Annu. Rev. Astron. Astrophys.* **2003**, 41, 241.

[6] Chakarov, D.; Österlund, L.; Kasemo, B. *Vacuum* **1995**, 46, 1109. *Ibid. Langmuir* **1995**, 11, 1201.

[7] Avgul, N. N.; Kieslev, A. V. *Chemistry and Physics of Carbon, Vol. 6*, Walker, P. L. Ed., Dekker, New York, 1970.

[8] Werder, T.; Walther, J. H.; Jaffe, R. L.; Halicioglu, T.; Koumoutsakos, P. *J. Phys. Chem. B* **2003**, *107*, 1345.

[9] Pertsin, A.; Grunze, M. *J. Phys. Chem. B* **2004**, *108*, 1357.

[10] Pertsin, A.; Grunze, M. *J. Chem. Phys.* **2006**, *125*, 114707.

[11] Gatica, S.M.; Johnson, J.K.; Zhao, X. C.; Cole, M. W. *J. Phys. Chem. B* **2004**, *108*, 11704.


[12] Feller, D.; Jordan, K. D. *J. Phys. Chem. A* **2000**, *104*, 9971.

[13] Karapetian, K.; Jordan, K. D. *Water in Confined Environements*, De-
vling, J. P.; Buch, V. Eds., Springer, New York, 2003, p.139.

[14] Sudiarta, I. W.; Geldart, D. J. W. *J. Phys. Chem. A* **2006**, *110*, 10501.

[15] Cabrera-San Felix, P.; Hollowy, S.; Kolanski, K. W.; Darling, G. R. *Surf.
Sci.* **2003**, *532*, 166.

[16] Lin, C. S.; Zhang, R. Q.; Lee, S. T.; Elstner, M.; Frauenheim, Th.; Wan,
L. J. *J. Phys. Chem. B* **2005**, *109*, 14183.

[17] Jorgensen, W. L. *J. Chem. Phys.* **1982**, *77*, 4156.

[18] Wales, D. J.; Hodges, M. P. *Chem. Phys. Lett.* **1998**, *286*, 65.

[19] Kabrede, H.; Hentschke, R. *J. Phys. Chem. B* **2003**, *107*, 3914.

[20] Hartke, B. *Z. Phys. Chem. B* **2000**, *214*, 1251.

[21] González, B. S.; Hernández-Rojas, J.; Wales, D. J. *Chem. Phys. Lett.*
**2005**, *412*, 23.

[22] Schulz, F.; Hartke, B. *Chem. Phys. Chem.* **2002**, *3*, 98.

[23] Hernández-Rojas, J.; Bretón, J.; Gomez Llorente, J. M.; Wales, D. J. *J.
Phys. Chem. B* **2006**, *110*, 13357.

[24] Steele, W. A. *The Interaction of Gases with Solid Surfaces*, Pergamon
Press, Oxford, 1974.

28

[25] Ocasio, M.; López, G. E. *J. Chem. Phys.* **2000**, 112, 3339.

[26] Hannay, J. H. *Eur. J. Phy.* **1983**, 4, 141.

[27] Bruch, L. W.; Cole, M. W.; Zaremba, E. *Physical Adsorption: Forces and Phenomena*, Clarendon Press, Oxford, 1997.

[28] Wales, D. J.; Doye, J. P. K. *J. Phys. Chem. A* **1997**, 101, 5111.

[29] Li, Z. Q.; Scheraga, H. A. *Proc. Natl. Acad. Sci. USA* **1987**, 84, 6611.

[30] Doye, J. P. K.; Wales, D. J. *Phys. Rev. B* **1999**, 59, 2292.

[31] Hernández-Rojas, J.; Wales, D. J. *J. Chem. Phys.* **2003**, 119, 7800.

[32] Hernández-Rojas, J.; Bretón, J.; Gomez Llorente, J. M.; Wales, D. J. *J. Chem. Phys.* **2004**, 121, 12315.

[33] Hernández-Rojas, J.; Bretón, J.; Gomez Llorente, J. M.; Wales, D. J. *Chem. Phys. Lett.* **2005**, 410, 404.

[34] Wales, D. J. *Energy Landscapes*, Cambridge University Press, Cambridge, 2003.

[35] Georgiev, G. K.; Pacheco, J. M.; Tománek, D. *Phys. Rev. Lett.* **2004**, 92, 215501.

[36] Gutowsky, H.S.; Emilsson, T.; Arunan, E. *J. Chem. Phys.* **1993**, 94, 4883.

[37] Wales, D. J.; Doye, J. P. K.; Dullweber, A.; Hodges, M. P.; Naumkin,
F. Y.; Calvo, F.; Hernández-Rojas, J.; Middleton, T. F. The Cambridge
Cluster Database, http://www-wales.ch.cam.ac.uk/CCD.html.

[38] Kokalj, A. *J. Mol. Graph. Model.* **1999**, *17*, 176.