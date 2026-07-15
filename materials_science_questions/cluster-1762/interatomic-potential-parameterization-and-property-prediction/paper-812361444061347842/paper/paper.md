# Transition State Theory of Zeolitic Diffusion
Diffusion of $CH_4$ and $CF_4$ in 5A Zeolite

By D. M. RUTHVEN AND R. I. DERRAH

Dept. of Chemical Engineering, University of New Brunswick, Fredericton,
New Brunswick, Canada

Received 1st June, 1972

A simple theory of zeolitic diffusion is developed from the principles of transition state theory. General expressions for the diffusivity are derived in terms of the lattice parameter and the partition function for the transition state which, for the type A zeolites, is identified as a molecule in passage through the 8-membered oxygen window. Theoretical diffusivities calculated for $CH_4$ and $CF_4$ in 5A zeolite agree well with experimental data and it is shown that, in the transition state, the $CF_4$ molecule has a high degree of rotational freedom whereas the rotation of the $CH_4$ molecule is severely restricted. This difference is attributed to the difference in the moments of inertia.

The phenomenon of zeolitic sorption has been widely studied but progress in the theoretical understanding of zeolitic transport has been limited. The subject has been reviewed by Walker, Austin and Nandi $^1$ and more recently by Rieckert $^2$ and by Barrer. $^3$ Extensive experimental diffusivity data are available for several gas-zeolite systems and it is pertinent to consider the extent to which such data may be interpreted, on the molecular scale, in terms of established physical principles. In the present paper a simple theory of zeolitic transport is developed from transition state theory and used to interpret experimental data for the diffusion of methane and tetrafluoromethane in 5A zeolite.

## TRANSITION STATE THEORY OF ZEOLITIC TRANSPORT

Consideration is restricted to those zeolite lattices which consist of relatively large cavities inter-connected by windows of molecular dimensions. Molecules occluded within a cavity are in a region of low potential energy and have considerable freedom of movement within the cavity. In passing through a window the freedom of movement of the sorbate molecule is severely constrained and, as a result of repul- sion forces, there may be an appreciable energy barrier. For such systems, the passage of a molecule through the window between adjacent cavities may be considered as a rate process involving an activated transition state. At any instant, only relatively few of the occluded molecules will be in the activated state in a window and statistical equilibrium with molecules in the cavities may be assumed. This model is appropriate for molecules such as hydrocarbons in type A zeolites but may not be directly applic- able to the more open lattices of the faujasite zeolites and even to the diffusion of the small permanent gas molecules in the A type of zeolite. For such systems, calcula- tions suggest that the windows may be regions of minimum rather than maximum potential energy, so that the assumption of an activated transition state may be inappropriate. $^1$

The concentration ratio of molecules in the windows to molecules in the cavities $(c_z^*/c_z)$ may be expressed as the ratio of the relevant partition functions $(f_z^*/f_z)$:

$$
\frac{c_{z}^{*}}{c_{z}}=\frac{f_{z}^{*}}{f_{z}} \exp \left[\frac{\left(u_{z}-u_{z}^{*}\right)}{k T}\right] \tag{1}
$$

where $u_{z}-u_{z}^{*}$ is the difference in potential energy. In terms of transition state theory the rate of passage of molecules through the windows is given by :

$$
j=\frac{k T}{h} c_{z}^{*}=\frac{k T}{h} c_{z} \frac{f_{z}^{*}}{f_{z}} \exp \left[\frac{\left(u_{z}-u_{z}^{*}\right)}{k T}\right]
\tag{2}
$$

where $k$ is Boltzmann's constant, $h$ is Planck's constant and $T$ is the absolute temperature. If we consider a cubic array of cavities (lattice parameter $\delta$) such as exists in the type A zeolites (for which $\delta=12.3 \AA$), the flux in a given direction across any plane through the crystal will be :

$$
J^{\prime}=\frac{k T \delta}{6 h} c_{z} \frac{f_{z}^{*}}{f_{z}} \exp \left[\frac{\left(u_{z}-u_{z}^{*}\right)}{k T}\right].
\tag{3}
$$

(The factor $\frac{1}{6}$ arises because, for cubic cells with one window in each face, only one sixth of the activated molecules will be passing through a window in the direction considered at any instant.) As the cavities are small ($\delta$ small) the net flux in the $x$ direction, in the presence of a concentration gradient, is given by :

$$
J_{x}=-\left(\frac{k T \delta^{2}}{6 h}\right) f_{z}^{*} \exp \left[\frac{\left(u_{z}-u_{z}^{*}\right)}{k T}\right] \frac{\partial}{\partial x}\left(\frac{c_{z}}{f_{z}}\right).
\tag{4}
$$

For an ideal vapour phase (pressure $p$, molecular partition function $f_{g}$) in equilibrium with a sorbate concentration $c_{z}$, the activity $(a)$, which is proportional to the absolute activity, may be defined by the relationship :

$$
a=p / k T f_{g}=c_{z} / f_{z}
\tag{5}
$$

whence :

$$
\frac{\partial}{\partial x}\left(\frac{c_{z}}{f_{z}}\right)=\frac{\partial a}{\partial x}=\frac{1}{f_{z}}\left(1-\frac{c_{z}}{f_{z}} \frac{\partial f_{z}}{\partial c_{z}}\right) \frac{\partial c_{z}}{\partial x}=\frac{1}{f_{z}} \frac{\partial \ln a}{\partial \ln c_{z}} \frac{\partial c_{z}}{\partial x}.
\tag{6}
$$

The Fickian diffusivity $D$ (defined by $J_{x}=-D\left[\partial c_{z} / \partial x\right]$) is therefore given by :

$$
D=\left(\frac{k T \delta^{2}}{6 h}\right) \frac{f_{z}^{*}}{f_{z}} \exp \left[\frac{\left(u_{z}-u_{z}^{*}\right)}{k T}\right] \frac{\partial \ln a}{\partial \ln c}.
\tag{7}
$$

We may also define a drag coefficient $\kappa$ (reciprocal mobility) which is related to the diffusivity by the expression

$$
D=\frac{k T}{\kappa} \frac{\partial \ln a}{\partial \ln c}
$$

where

$$
\kappa=\left(\frac{6 h}{\delta^{2}}\right) \frac{f_{z}}{f_{z}^{*}} \exp \left[\frac{\left(u_{z}^{*}-u_{z}\right)}{k T}\right]\left(\text { dyn } \mathrm{cm}^{-1} \text { molecule}^{-1}\right). \quad(8)
$$

The derivative $\partial \ln a / \partial \ln c_{z}$ is determined by the shape of the equilibrium isotherm (for an ideal vapour phase $\partial \ln a / \partial \ln c_{z}=\partial \ln p / \partial \ln c_{z}$). At low sorbate concentrations (the Henry's Law region) the isotherm is linear and the limiting diffusivity $D_{0}$ is

$$
D_{0}=\frac{k T}{\kappa}=\left(\frac{k T \delta^{2}}{6 h}\right) \frac{f_{z}^{*}}{f_{z}} \exp \left[\frac{\left(u_{z}-u_{z}^{*}\right)}{k T}\right].
\tag{9}
$$

This expression may be obtained directly from eqn (4) since, at sufficiently low concentrations, $f_{z}$ is independent of $c_{z}$.

At higher concentrations, $f_{z}$ is a function of $c_{z}$ and the isotherm becomes non-linear, leading to a concentration dependent diffusivity. By contrast, the drag coefficient,

which depends only on the ratio of partition functions $(f_{z}^{*} / f_{z}) \exp [(u_{z}-u_{z}^{*}) / k T]$, may be expected to be essentially independent of concentration since, to a first approximation, the concentration dependent factors cancel.

This type of behaviour has been observed experimentally for the sorption of light paraffins $^{4,5}$ and olefins $^{6}$ in type A zeolites. The diffusivities were found to be strongly concentration dependent but this effect could be quantitatively accounted for by considering the non-linearity of the isotherms; the drag coefficients were found to be essentially independent of concentration. From the theory outlined above we may expect such behaviour to be common, although not necessarily universal.

Within the Henry's law region $(c_{z}=K p)$ we may write :

$$
f_{z}=K f_{g}^{\prime} k T \exp \left[\left(u_{z}-u_{g}\right) / k T\right] \tag{10}
$$

where $K$ is the Henry constant (molecule $cm^{2} dyn^{-1} cavity^{-1}$ ), $f_{g}^{\prime}$ is the partition function per unit volume for the gaseous sorbate and $u_{g}$ is the corresponding potential energy (usually $u_{g}=0$ ). This allows the limiting diffusivity $D_{0}$ to be expressed in terms of more accessible quantities :

$$
D_{0}=\left(\frac{\delta^{2}}{6 \boldsymbol{h}}\right) \frac{f_{z}^{*}}{K f_{g}^{\prime}} \exp \left[\frac{\left(u_{g}-u_{z}^{*}\right)}{k T}\right]. \tag{11}
$$

Writing $u^{\prime}=u_{z}^{*}-u_{g}$ and, for the temperature dependence of the Henry constant, $K=K_{0} \exp q / k T$ we obtain

$$
D_{0}=\left(\frac{\delta^{2}}{6 \boldsymbol{h}}\right) \frac{1}{K_{0}}\left(\frac{f_{z}^{*}}{f_{g}^{\prime}}\right) \exp \left[-\frac{\left(u^{\prime}+q\right)}{k T}\right]. \tag{12}
$$

If the temperature dependence of the factor $f_{z}^{*} / f_{g}^{\prime}$ is small, this equation has the form of an Eyring expression $(D_{0}=D_{*} \exp (-E / R T))$ with :

$$
D_{*}=\left(\frac{\delta^{2}}{6 \boldsymbol{h}}\right) \frac{1}{K_{0}} \frac{f_{z}^{*}}{f_{g}^{\prime}} ; \quad \frac{E}{R}=\frac{u^{\prime}+q}{k}. \tag{13}
$$

These expressions provide a convenient basis for comparison with experimental diffusivity data, since $K_{0}$ and $q$ may be found from equilibrium data, $u^{\prime}$ may be calculated from potential theory and the ratio $f_{z}^{*} / f_{g}^{\prime}$ may be estimated from theoretical considerations.

The partition function $f_{g}^{\prime}$ may be expressed as a product of the translational, rotational and internal vibrational partition functions $(f_{trans }^{\prime}, f_{rot }, f_{int })$ :

$$
f_{g}^{\prime}=f_{\text {trans }}^{\prime} f_{\text {rot }} f_{\text {int }}=\left(2 \pi m k T / \boldsymbol{h}^{2}\right)^{\frac{3}{2}} \mathrm{e} f_{\text {rot }} f_{\text {int }} \tag{14}
$$

where $m$ is the mass of a sorbate molecule. The partition function for the transition state $f_{z}^{*}$ includes all degrees of freedom other than translation through the window, which is accounted for by the factor $k T / \boldsymbol{h}$ in eqn (2)-(7). The molecule in the transition state may be assumed to have the same internal degrees of freedom (partition function $f_{int }$ ) as a molecule in the gas phase but the motion of the molecule as a whole will be severely restricted. We may represent the degrees of freedom corresponding to motion of the centre of gravity of the molecule in the plane of the window as a two dimensional oscillation characterized by a partition function $f^{+}$. For the two limiting cases of freely rotating and non-rotating transition states we have :

$$
\text { free rotation: } \quad f_{z}^{*}=f_{\text {int }} f^{+} f_{\text {rot }} ; \quad \frac{f_{z}^{*}}{f_{g}^{\prime}}=\frac{f^{+}}{f_{\text {trans }}^{\prime}} \tag{15}
$$

$$
\text { no rotation: } \quad f_{z}^{*}=f_{\text {int }} f^{+} ; \quad \frac{f_{z}^{*}}{f_{g}^{\prime}}=\frac{f^{+}}{f_{\text {trans }}^{\prime} f_{\text {rot }}}. \tag{16}
$$

D. M. RUTHVEN AND R. I. DERRAH

For simple symmetrical molecules, the extreme cases of free rotation and no significant rotation may be approximately realized depending inter-alia on the moment of inertia of the sorbate molecule and its size relative to the window. For linear and other non-symmetric molecules, the situation will be more complex since the rotational freedom of the molecule will be replaced, in the transition state, by a rocking vibration from which an appreciable contribution to the partition function may be expected. The excitation of such degrees of freedom with increasing temperature may lead to a significant temperature dependence of the ratio $f_{z}^{*} / f_{g}'$ with consequent departure from the simple Eyring equation for the temperature dependence of the diffusivity. For such systems, however, the extremes of freely rotating and non-rotating transition states may still serve to provide useful upper and lower estimates of the diffusivity although to obtain quantitative predictions one will require more detailed analysis of the vibra- tional degrees of freedom for the transition state.

# THEORETICAL CALCULATION OF $u_{z}^{*}$ AND $f^{+}$FROM POTENTIAL THEORY

In principle, the potential energy of a non-polar molecule at any point within a zeolite lattice may be calculated by summing the contributions of the dispersion, repulsion, polarization and quadrupole energies arising from the interaction of the sorbate molecule with each ion of the lattice. $^{7-11}$ The 5A zeolite is particularly suitable for such calculations since the positions of both the oxygen ions and the exchangeable cations are well established. For the analysis of diffusivity data we require only the potential energy for a sorbate molecule close to the centre of the8-membered oxygen window $(u')$ since the average potential energy for a molecule within a cavity $(u_{z})$ has been expressed in terms of the experimental heat of sorption. This simplifies the problem since symmetry considerations show that, at the centre of a window, the gradient of electric field is very small so that polarization and quadrupole energies may be neglected.

The dispersion energy is given by:
$$\phi_{\mathbf{D}}=-\sum_{i j} \frac{A_{i}}{r_{i j}^{6}}\quad(17)$$
where $r_{i j}$ is the distance of the sorbate molecule from the j th ion of type i and $A_{i}$ is a constant which may be estimated from either the Kirkwood-Müller $^{12,13}$ or SlaterKirkwood formula $^{14}$ :
$$A_{1, i}=\frac{6 m_{e} c^{2} \alpha_{1} \alpha_{i}}{\left(\alpha_{1} / \chi\right)+\left(\alpha_{i} / \chi_{i}\right)}\quad(18)$$

$$A_{1, i}=\frac{3 e h \alpha_{1} \alpha_{i}}{4 \pi \sqrt{ } m_{e}\left[\left(\alpha_{1} / n_{1}\right)^{\frac{1}{2}}+\left(\alpha_{i} / n_{i}\right)^{\frac{1}{2}}\right]}.\quad(19)$$

In these expressions $\alpha_{1}, \alpha_{i}$ are the polarizabilities and $\chi_{1}, \chi_{i}$ the magnetic susceptibilities of the sorbate molecule and ion respectively, $m_{e}$ is the mass and e the charge of an electron, c is the velocity of light and $n_{1}, n_{i}$ are the numbers of electrons in the outer shells of the molecule and ion respectively.

The repulsion energy $(\phi_{R})$ may be estimated assuming the usual inverse twelfthpower law:
$$\phi_{\mathbf{R}}=\sum_{i, j} \frac{B_{i}}{r_{i j}^{12}}.\quad(20)$$

The value of the repulsion constant $B_{i}$ is calculated by setting the distance correspond ing to the minimum of the potential well for the interaction of a sorbate molecule

I-74

with an isolated ion $(\rho_{ei})$ equal to the sum of the van der Waals radii $(\rho_{01}+\rho_{0i})$. In considering the interaction between a sorbate molecule and an isolated ion it is necessary to take account of the polarization energy which is given by:

$$
\phi_{\mathrm{P}}=-\frac{1}{2} \alpha_{1}\left(q_{i} / r^{2}\right)^{2} \tag{21}
$$

where $\alpha_{1}$ is the polarizability of the sorbate molecule and $q_{i}$ is the change on the particular ion. Thus, for the isolated molecule-ion interaction :

$$
\phi=\phi_{\mathrm{D}}+\phi_{\mathrm{R}}+\phi_{\mathrm{P}}=-\frac{A_{i}}{r^{6}}+\frac{B_{i}}{r^{12}}-\frac{1}{2} \alpha_{1}\left(\frac{q_{i}}{r^{2}}\right)^{2} \tag{22}
$$

from which, by setting $(\partial \phi / \partial r)_{r=\rho_{e i}}=0$ we obtain :

$$
B_{i}=\frac{A_{i} \rho_{e i}^{6}}{2}\left(1+\frac{\alpha_{1} q_{i}^{2} \rho_{e i}^{2}}{3 A_{i}}\right). \tag{23}
$$

Calculations were carried out for methane and tetrafluoromethane molecules in an idealized 5A zeolite lattice. Each cavity was assumed to contain $4 \mathrm{Ca}^{++}$and $4 \mathrm{Na}^{+}$ions placed at the centres of the six-membered oxygen rings in a tetrahedral arrangement. The small effect of the silicon and aluminium ions was neglected in the calculations. The positions of the oxygen ions were taken from Broussard and Shoemaker $^{15}$ and the parameters employed in the calculations are summarized in table 1. A charge of $-e / 4$ was assigned to each oxygen ion and values of polarizability and susceptibility estimated by Kiselev et al. $^{10,11}$ were selected. For $\mathrm{O}^{-\frac{1}{4}}$ the values are rather smaller than those given by Barrer and Stuart $^{7}$ as a result of a correction for the ionic charge. For methane, consistent values of the dispersion constants were obtained from both Slater-Kirkwood and Kirkwood-Müller formulae and the mean of these values was used. Magnetic susceptibility data are not available for tetrafluoromethane; the dispersion constants were therefore calculated from the Slater-Kirkwood expression. The van der Waals radii of the sorbate molecules were estimated from the known bond lengths $^{16}(\mathrm{C}-\mathrm{H}=1.09 \AA ; \mathrm{C}-\mathrm{F}=1.32 \AA)$ and the atomic radii of hydrogen and fluorine as estimated by Pauling $^{17}(\rho_{\mathrm{H}}=1.2-$ $1.29 \AA ; \rho_{\mathrm{F}}=1.35 \AA$ ). These values are similar to those given by Barrer $^{18}$ but are subject to uncertainties of at least $\pm 0.05 \AA$.

<table>
<caption>TABLE 1.—MOLECULAR PARAMETERS USED IN POTENTIAL CALCULATIONS</caption>
<thead>
<tr>
<th>sorbate/ion</th>
<th>$\mathrm{CH}_{4}$</th>
<th>$\mathrm{CF}_{4}$</th>
<th>$\mathrm{O}^{-\frac{1}{4}}$</th>
<th>$\mathrm{Ca}^{++}$</th>
<th>$\mathrm{Na}^{+}$</th>
</tr>
</thead>
<tbody>
<tr>
<td>$\alpha / 10^{-25} \mathrm{~cm}^{3}$ molecule$^{-1}$</td>
<td>26</td>
<td>36.7</td>
<td>14.7</td>
<td>4.71</td>
<td>1.8</td>
</tr>
<tr>
<td>$\chi / 10^{-30} \mathrm{~cm}^{3}$ molecule$^{-1}$</td>
<td>20.2</td>
<td>—</td>
<td>17.7</td>
<td>22.1</td>
<td>6.95</td>
</tr>
<tr>
<td>$\rho_{0} / 10^{-8} \mathrm{~cm}$</td>
<td>2.34</td>
<td>2.67</td>
<td>1.4</td>
<td>0.99</td>
<td>0.98</td>
</tr>
<tr>
<td></td>
<td>(2.2-2.3)*</td>
<td>(2.66-2.72)*</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>$A_{\mathrm{CH}_{4}} / 10^{-45} \mathrm{kcal} \mathrm{cm}^{6} \mathrm{~mol}^{-1}$</td>
<td>—</td>
<td>—</td>
<td>1.33</td>
<td>0.561</td>
<td>0.225</td>
</tr>
<tr>
<td>$B_{\mathrm{CH}_{4}} / 10^{-90} \mathrm{kcal} \mathrm{cm}^{12} \mathrm{~mol}^{-1}$</td>
<td>—</td>
<td>—</td>
<td>2.28</td>
<td>9.75</td>
<td>2.44</td>
</tr>
<tr>
<td>$A_{\mathrm{CF}_{4}} / 10^{-45} \mathrm{kcal} \mathrm{cm}^{6} \mathrm{~mol}^{-1}$</td>
<td>—</td>
<td>—</td>
<td>1.76</td>
<td>0.681</td>
<td>0.289</td>
</tr>
<tr>
<td>$B_{\mathrm{CF}_{4}} / 10^{-90} \mathrm{kcal} \mathrm{cm}^{12} \mathrm{~mol}^{-1}$</td>
<td>—</td>
<td>—</td>
<td>5.14</td>
<td>28.8</td>
<td>7.19</td>
</tr>
</tbody>
</table>

* values estimated by Barrer $^{18}$

The results of the theoretical potential calculations are given in fig. 1 and 2, which show the profiles along the principal axis of a zeolite crystal, from the centre of the cavity to the centre of the 8-membered oxygen window and the profiles across the plane of the window. The principal contribution to the potential arises from the oxygen framework and, near the centre of the window, the contribution of the cations

D. M. RUTHVEN AND R. I. DERRAH

is very small. The potential at the centre of the window is very sensitive to small changes in the van der Waals radii since both dispersion and repulsion terms are large. This effect is illustrated in table 2.

In order to estimate the partition function $f^{+}$, the potential profile across the window was fitted to a parabolic expression : $\Delta u'=\frac{1}{2}\mu(\Delta x)^2$, where $\Delta u'$ is the change

![](./images/812361444061347842_1.jpg)

FIG. 1.—Potential profiles along the fourth order axis of a 5A zeolite cavity from the cavity centre to the centre of the 8-membered oxygen window. (a) $CH_4$, $(r_{CH_4}+r_{O-0.25})=3.75\ Å$; (b) $CF_4$, $(r_{CF_4}+r_{O-0.25})=4.06\ Å$.

![](./images/812361444061347842_2.jpg)

FIG. 2.—Potential profiles across the plane of the 8-membered oxygen window : upper, $CF_4$; lower, $CH_4$.

**TABLE 2.—THE EFFECT OF VAN DER WAALS RADIUS ON THE POTENTIAL OF A METHANE MOLECULE AT THE CENTRE OF THE 8-MEMBERED OXYGEN WINDOW**

| van der Waals radius $\rho_0$/Å | potential $Nu'$/ kcal mol⁻¹ |
|----------------------------------|------------------------------|
| 2.26                             | $-2.30$                      |
| 2.29                             | $-2.10$                      |
| 2.31                             | $-1.90$                      |
| 2.33                             | $-1.71$                      |
| 2.35                             | $-1.51$                      |
| 2.37                             | $-1.31$                      |

(van der Waals radius for O⁻⁴ taken as 1.4 Å)

in potential energy for a displacement $\Delta x$ from the centre of the ring and $\mu$ is a constant. The vibration frequency $(v)$ may then be obtained from the usual relationship for a harmonic oscillator:
$$
v=(1 / 2 \pi)(\mu / m)^{\frac{1}{2}} \tag{25}
$$
and the corresponding partition function for the 2 dimensional oscillation is given by :
$$
f^{+}=\frac{\exp (-\boldsymbol{h} v / \boldsymbol{k} T)}{(1-\exp (-\boldsymbol{h} v / \boldsymbol{k} T))^{2}}. \tag{26}
$$

Values of $u'$, $v$ and $f^{+}$are summarized in table 3 together with the values of $f_{\text {rot }}$ and $f_{\text {trans }}^{\prime}$ calculated from the usual expressions :
$$
f_{\text {trans }}^{\prime}=\left(\frac{2 \pi m \boldsymbol{k} T}{\boldsymbol{h}^{2}}\right)^{\frac{3}{2}} e \tag{27}
$$
$$
f_{\text {rot }}=\left(\frac{8 \pi^{2} I \boldsymbol{k} T}{\boldsymbol{h}^{2}}\right)^{\frac{3}{2}} \frac{\sqrt{ } \pi}{12}. \tag{28}
$$

(Tetrahedral molecule with moment of inertia $I$.)

**TABLE 3.—POTENTIAL ENERGIES AND PARTITION FUNCTIONS FOR $\text{CH}_4$ AND $\text{CF}_4$**

| | $\text{CH}_4$ | $\text{CF}_4$ |
|-------------------------------|---------------|---------------|
| $Nu'$/kcal mol⁻¹              | $-1.68$       | $+3.30$       |
| $v/10^{12}\ \text{s}^{-1}$    | $3.39$        | $2.29$        |
| $T/\text{K}$ (mean of experimental data) | $250$ | $400$ |
| $\boldsymbol{k}T/\boldsymbol{h}v$ | $1.53$ | $3.63$ |
| $f^{+}$                       | $2.21$        | $13.0$        |
| $f_{\text{rot}}$              | $27.6$        | $5720$        |
| $f_{\text{trans}}'$           | $1.3\times 10^{26}$ | $34.0\times 10^{26}$ |
| $f_{\text{rot}} \exp(-\Delta u'/\boldsymbol{k}T)$ | $0.32$ | $70$ |

$N =$ Avogadro's number

The effective radius of a freely rotating tetrahedral molecule will be somewhat larger than the corresponding radius for the non-rotating molecule and this will lead to a difference in the potential energy of the transition state. It is not possible to make a reliable calculation of this effect owing to the uncertainty in the van der Waals radii. However, as an approximate estimate of the difference in effective radii for rotating and non-rotating molecules, one may take the difference between half the corner-to-corner distance of the tetrahedron and the radius of the circumscribing

sphere. This gives, for both methane and tetrafluoromethane, a difference in effective radius of about $0.2 \AA$. The corresponding estimate of the difference in potential energy for rotating and non-rotating transition states is about 2.2 and 3.5 kcal/mol for methane and tetrafluoromethane respectively. The ratio of the numbers of freely rotating to non-rotating molecules in the transition state will be determined by the ratio of partition functions, duly corrected for the difference in potential energy. For methane this ratio (given by $f_{\text {rot }} \exp \left(-\Delta u^{\prime} / k T\right)$ ) is appreciably less than unity suggesting that, in the transition state, rotation will be largely inhibited whereas for tetrafluoromethane this ratio is much greater than unity indicating essentially free rotation

# COMPARISON OF THEORETICAL AND EXPERIMENTAL DIFFUSIVITIES

Kinetic and equilibrium measurements for the sorption of methane and tetra- fluoromethane in Linde 5A zeolite crystals were made gravimetrically using a vacuum microbalance system. $^{5,6}$ Diffusional time constants were calculated by matching the experimental sorption curves to the appropriate transient solution of the diffusionequation, duly corrected to allow for the size distribution of the zeolite crystals. $^{19,20}$  To obtain the diffusivities, the mean crystal half-side $(=1.8 \mu m)$ , as determined by photomicrography, $^{20}$ was used.

The experiments were carried out over a range of pressures from about 3 to300 Torr. The isotherms for tetrafluoromethane were essentially linear (Henry's Law region) and the diffusivities were found to be independent of concentration, although subject to random experimental errors of about $\pm 20 \%$ . For methane, the departure from Henry's Law was significant at the lower temperatures and higher pressures and the Henry constants were calculated using the theoretical model isotherm, as

![](./images/812361444061347842_3.jpg)

FIG. 3.-Experimental diffusivity data for $CH_{4}$ and $CF_{4}$ in $5 ~A$ zeolite crystals: (a) $CF_{4}$ ; (b) $CH_{4}$ .

![](./images/812361444061347842_4.jpg)

FIG. 4.—Temperature dependence of Henry's Law constants (CH₄—5A, ○ ; CF₄—5A, × ; CH₄—4A,²³ △). (a) CH₄, $K=1.9×10^{-6}\mathrm{e}^{4540/\boldsymbol{R}T}$ ; (b) CF₄, $K=3.8×10^{-7}\mathrm{e}^{5890/\boldsymbol{R}T}$.

![](./images/812361444061347842_5.jpg)

FIG. 5.—Temperature dependence of diffusivity for CH₄ and CF₄ in 5A zeolite (experimental points, theoretical lines). (a) CH₄, no rotation ; (b) CF₄, free rotation.

previously described. $^{21}$ Departures from linearity were not sufficiently pronounced to cause any significant concentration dependence of the diffusivity, within the accuracy of the experimental measurements. The diffusivity data, for those temperatures at which the measurements extended over a sufficiently wide range of concentrations, are shown in fig. 3 and the average diffusivities are given in table 4. For methane at 273 K, the diffusional time constant is about $10^{-2} \mathrm{~s}^{-1}$; this represents the practical upper limit of the experimental method.

TABLE 4.-EXPERIMENTAL DIFFUSIVITIES AND HENRY'S LAW CONSTANTS

<table>
  <thead>
    <tr>
      <th>sorbate</th>
      <th>temp./K</th>
      <th>$K \times 10^{3}/$<br>molecule (cavity Torr)$^{-1}$</th>
      <th>$D_{0} \times 10^{11}/$<br>$\mathrm{cm}^{2} \mathrm{~s}^{-1}$</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="5">$\mathrm{CF}_{4}$</td>
      <td>348</td>
      <td>2.3</td>
      <td>0.62</td>
    </tr>
    <tr>
      <td>358</td>
      <td>1.5</td>
      <td>0.64</td>
    </tr>
    <tr>
      <td>393</td>
      <td>0.84</td>
      <td>1.73</td>
    </tr>
    <tr>
      <td>424</td>
      <td>0.44</td>
      <td>10.1</td>
    </tr>
    <tr>
      <td>450</td>
      <td>0.26</td>
      <td>7.75</td>
    </tr>
    <tr>
      <td rowspan="8">$\mathrm{CH}_{4}$</td>
      <td>$185^{*}$</td>
      <td>702.0</td>
      <td>2.12</td>
    </tr>
    <tr>
      <td>212</td>
      <td>96.0</td>
      <td>8.9</td>
    </tr>
    <tr>
      <td>228</td>
      <td>42.0</td>
      <td>13.2</td>
    </tr>
    <tr>
      <td>$230^{*}$</td>
      <td>31.7</td>
      <td>12.6</td>
    </tr>
    <tr>
      <td>232</td>
      <td>30.0</td>
      <td>16.6</td>
    </tr>
    <tr>
      <td>$273^{*}$</td>
      <td>7.8</td>
      <td>28.6</td>
    </tr>
    <tr>
      <td>273</td>
      <td>7.0</td>
      <td>22.5</td>
    </tr>
    <tr>
      <td>323</td>
      <td>1.7</td>
      <td>---</td>
    </tr>
  </tbody>
</table>

* data of Dr. K. F. Loughlin. $^{5}$

The temperature dependence of the Henry constants and diffusivities is shown in fig. 4 and 5 and the parameters of the empirical equations $D_{0}=D_{*} \exp (-E / R T)$ and $K=K_{0} \exp (q / R T)$ are listed in table 5. The values of $K_{0}$ and $q$ for methane differ somewhat from those previously reported $^{21}$ as a result of the inclusion of additional experimental data. The heat of sorption of tetrafluoromethane (5.89 kcal/mol) is somewhat greater than the value obtained by Barrer and Reucroft $^{22}$ for sorption in faujasite (5.3 kcal/mol). Also included in table 5 are the experimental diffusivity data reported by Habgood $^{23}$ for the diffusion of methane in 4A zeolite at low concentrations. The Henry constants for the $\mathrm{CH}_{4}-4 \mathrm{~A}$ system,

TABLE 5.-COMPARISON OF EXPERIMENTAL AND THEORETICAL DIFFUSIVITY DATA

<table>
  <thead>
    <tr>
      <th rowspan="2">system</th>
      <th rowspan="2">$K_{0}/$<br>molecule<br>(cavity Torr)$^{-1}$</th>
      <th colspan="3">experimental values</th>
      <th colspan="3">theoretical values</th>
    </tr>
    <tr>
      <td>$Nq/$<br>kcal<br>mol$^{-1}$</td>
      <td>$D^{*}/$<br>$\mathrm{cm}^{2} \mathrm{~s}^{-1}$</td>
      <td>$E/$<br>kcal mol$^{-1}$</td>
      <td>$E/$<br>kcal<br>mol$^{-1}$</td>
      <td>rotating<br>$D_{*\text{rot}}/$<br>$\mathrm{cm}^{2} \mathrm{~s}^{-1}$</td>
      <td>not rotating<br>$D_{*\text{n.r.}}/$<br>$\mathrm{cm}^{2} \mathrm{~s}^{-1}$</td>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>$\mathrm{CH}_{4}-5 \mathrm{~A}$</td>
      <td>$1.9 \times 10^{-6}$</td>
      <td>4.54</td>
      <td>$7.2 \times 10^{-8}$</td>
      <td>2.98</td>
      <td>2.86</td>
      <td>$1.72 \times 10^{-6}$</td>
      <td>$6.22 \times 10^{-8}$</td>
    </tr>
    <tr>
      <td>$\mathrm{CH}_{4}-4 \mathrm{~A}^{23}$</td>
      <td></td>
      <td>5.2</td>
      <td>$5.8 \times 10^{-8}$</td>
      <td>7.42</td>
      <td>---</td>
      <td>---</td>
      <td>---</td>
    </tr>
    <tr>
      <td>$\mathrm{CF}_{4}-5 \mathrm{~A}$</td>
      <td>$3.8 \times 10^{-7}$</td>
      <td>5.89</td>
      <td>$2.5 \times 10^{-6}$</td>
      <td>9.15</td>
      <td>9.19</td>
      <td>$1.92 \times 10^{-6}$</td>
      <td>$3.36 \times 10^{-10}$</td>
    </tr>
  </tbody>
</table>

calculated from Habgood's data, are shown in fig. 4. These values are not very different from the values for the $\mathrm{CH}_{4}-5 \mathrm{~A}$ system so that, according to the theory developed above, the difference in diffusivities between 4A and 5A zeolites should be due mainly to the difference in activation energy resulting from the difference in the effective window diameter, while the pre-exponential factors $(D_{*})$ should be similar. The experimental diffusivity data for methane are in accordance with this conclusion.

2342
ZEOLITIC DIFFUSION

Theoretical activation energies for diffusion were calculated from the theoretical values of $u'$, given in table 3, and the experimental values of $q(E = Nu' + Nq)$ which are listed in table 5. The theoretical values of $D_{*}$ were calculated according to eqn (13), (15) and (16), for both freely rotating and non-rotating transition states, using the values of $f^{+}, f_{rot}'$ and $f_{trans}'$ given in table 3. The theoretical lines corresponding to these cases are shown in fig. 5. It is evident that the theory, with the assumption of a freely rotating transition state, provides a very satisfactory fit of the experimental diffusivity data for tetrafluoromethane, while an equally good fit of the data for methane may be obtained by assuming a non-rotating transition state. This difference is understandable in terms of the large difference in the moments of inertia $(5.33 \times$ $10^{-40}$ and $117 \times 10^{-40} \mathrm{~g} \mathrm{~cm}^{2}$ ) and the corresponding difference in the rotational partition functions of these otherwise similar molecules. For methane, the gain in entropy arising from rotational freedom (in the transition state) is not sufficient to make up for the increase in potential energy, whereas for tetrafluoromethane the increased rotational freedom is more than sufficient to compensate for the increase in energy.

CONCLUSION

In view of the inevitable uncertainties in the theoretical calculation of potential energies, the agreement between the experimental and theoretical diffusivities is remarkable. The calculated values of $u'$ are, however, very sensitive to the values used for the van der Waals radii and, since these values are subject to some uncertainty, the agreement between experimental and theoretical activation energies is, to some extent, fortuitous. The theoretical calculation of $D_{*}$ is very much less dependent on the accuracy of the potential calculations since the partition function $f^{+}$does not depend on the absolute potential and is therefore insensitive to small errors in the assumed van der Waals radii. The conclusions concerning the rotational states of the two molecules in the transition states are therefore not dependent on the accuracy of the potential calculations. The method of calculation requires no assumptions concerning the state of the adsorbed molecules within the zeolite cavities; the results therefore give no direct evidence concerning the rotational states within the cavities. However, since tetrafluoromethane is freely rotating in the transition state, free rotation within the cavity seems highly probable. For methane, however, no such conclusion can be drawn since a non-rotating transition state does not necessarily imply any restriction of rotation within the cavities.

The experimental data for methane and tetrafluoromethane provide strong evidence in support of the transition state theory of zeolitic diffusion. For simple molecules it appears that the theory may give useful quantitative predictions of the diffusivity but the main value of the theory will probably be as a basis for the interpretation of experimental data.

The financial support of the National Research Council of Canada is gratefully acknowledged.

$^{1}$ P. L. Walker, L. G. Austin and S. P. Nandi, Chem. Phys. Carbon 1966, 2, 257.
$^{2}$ L. Rieckert, Adv. Catalysis, 1970, 21, 281.
$^{3}$ R. M. Barrer, Adv. in Chem., 1971, 102, 1.
$^{4}$ D. M. Ruthven and K. F. Loughlin, Trans. Faraday Soc., 1971, 67, 1661.
$^{5}$ K. F. Loughlin, Ph.D. Thesis (University of New Brunswick 1970).
$^{6}$ R. I. Derrah, M.Sc. Thesis (University of New Brunswick 1971).
$^{7}$ R. M. Barrer and W. I. Stuart, Proc. Roy. Soc. A, 1959, 249, 464.
$^{8}$ R. M. Barrer and D. J. Ruzicka, Trans. Faraday Soc., 1962, 58, 2253.

$^{9}$ K. Fiedler, H. J. Spangenberg and W. Schirmer, *Monats. Deut. Akad. Wiss. Berlin*, 1967, **9**, 516.

$^{10}$ A. V. Kiselev, *Adv. Chem.*, 1971, **102**, 37.

$^{11}$ P. Brauer, A. V. Kiselev, E. A. Lesnik and A. A. Lopatkin, *Russ. J. Phys. Chem.*, 1968, **42** 1350; 1969, **43**, 844.

$^{12}$ J. G. Kirkwood, *Phys. Z.*, 1932, **33**, 57.

$^{13}$ A. Müller, *Proc. Roy. Soc. A*, 1936, **154**, 624.

$^{14}$ J. C. Slater and J. G. Kirkwood, *Phys. Rev.*, 1931, **37**, 682.

$^{15}$ L. Broussard and D. P. Shoemaker, *J. Amer. Chem. Soc.*, 1960, **82**, 1041.

$^{16}$ *Tables of Interatomic Distances and Configuration*, ed. L. E. Sutton (Chem. Soc., London, 1958).

$^{17}$ L. Pauling, *The Nature of the Chemical Bond* (Cornell Univ. Press, Ithaca, New York, 1960), p. 257.

$^{18}$ R. M. Barrer in *Non-Stoichiometric Compounds*, ed. L. Mandelcorn (Academic Press, New York, 1964).

$^{19}$ D. M. Ruthven and K. F. Loughlin, *Chem. Eng. Sci.*, 1971, **26**, 577.

$^{20}$ K. F. Loughlin, R. I. Derrah and D. M. Ruthven, *Canad. J. Chem. Eng.*, 1971, **49**, 66.

$^{21}$ D. M. Ruthven and K. F. Loughlin, *J.C.S. Faraday I*, 1972, **68**, 696.

$^{22}$ R. M. Barrer and P. J. Reucroft, *Proc. Roy. Soc. A*, 1960, **258**, 449.

$^{23}$ H. W. Habgood, *Canad. J. Chem.*, 1958, **36**, 1384.