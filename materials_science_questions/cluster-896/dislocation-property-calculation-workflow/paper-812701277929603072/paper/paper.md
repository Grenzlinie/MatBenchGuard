Modelling and Simulation in Materials Science and Engineering

ACCEPTED MANUSCRIPT

# Solute-strengthening in elastically anisotropic fcc alloys

To cite this article before publication: Shankha Nag *et al* 2019 *Modelling Simul. Mater. Sci. Eng.* in press https://doi.org/10.1088/1361-651X/ab60e0

Manuscript version: Accepted Manuscript

Accepted Manuscript is "the version of the article accepted for publication including all changes made as a result of the peer review process, and which may also include the addition to the article by IOP Publishing of a header, an article ID, a cover sheet and/or an 'Accepted Manuscript' watermark, but excluding any other editing, typesetting or other changes made by IOP Publishing and/or its licensors"

This Accepted Manuscript is © 2019 IOP Publishing Ltd.

During the embargo period (the 12 month period from the publication of the Version of Record of this article), the Accepted Manuscript is fully protected by copyright and cannot be reused or reposted elsewhere.
As the Version of Record of this article is going to be / has been published on a subscription basis, this Accepted Manuscript is available for reuse under a CC BY-NC-ND 3.0 licence after the 12 month embargo period.

After the embargo period, everyone is permitted to use copy and redistribute this article for non-commercial purposes only, provided that they adhere to all the terms of the licence https://creativecommons.org/licences/by-nc-nd/3.0

Although reasonable endeavours have been taken to obtain all necessary permissions from third parties to include their copyrighted content within this article, their full citation and copyright line may not be present in this Accepted Manuscript version. Before using any content from this article, please refer to the Version of Record on IOPscience once published for full citation and copyright details, as permissions will likely be required. All third party content is fully copyright protected, unless specifically stated otherwise in the figure caption in the Version of Record.

View the article online for updates and enhancements.

This content was downloaded from IP address 130.89.3.19 on 23/12/2019 at 11:50

# Solute-strengthening in elastically anisotropic fcc alloys

Shankha Nag$^{a}$, Céline Varvenne$^{b}$, William A. Curtin$^{a}$

$^{a}$École polytechnique fédérale de Lausanne, Switzerland
$^{b}$Aix-Marseille University, CNRS, CINaM, Marseille, France

## Abstract

Dislocation motion through a random alloy is impeded by its interactions with the compositional fluctuations intrinsic to the alloy, leading to strengthening. A recent theory predicts the strengthening as a function of the solute-dislocation interaction energies and composition. First-principles calculations of solute/dislocation interaction energies are computationally expensive, motivating simplified models. An elasticity model for the interaction reduces to the pressure field of the dislocation multiplied by the solute misfit volume. Here, the elasticity model is formulated and evaluated for cubic anisotropy in fcc metals, and compared to a previous isotropic model. The prediction using the isotropic model with Voigt-averaged elastic constants is shown to represent the full anisotropic results within a few percent, and so is the recommended approach for studying anisotropic alloys. Application of the elasticity model using accessible experimentally-measured properties and/or first-principles-computed properties is then discussed so as to guide use of the model for estimating strengths of existing and newly proposed alloys.

Keywords:
solute-strengthening, interaction energy, linear elasticity approximation, elastic moduli averaging, Voigt averaging scheme

## 1. Introduction

The strengthening of elemental metals by alloying has a long history. The underlying mechanism of strengthening [1, 10, 2] is the interaction of dislocations with either (i) the alloying elements as solutes in the lattice or (ii) the stable and/or metastable precipitates formed by the host elements and the alloying elements. Solute strengthening due to the glide of dislocations through a field of substitutional solute atoms, whether the solutes are randomly distributed on the lattice sites or having preferential interactions leading to short-range-order, has seen a resurgence of interest in recent years due to the discovery of so-called High Entropy Alloys

Preprint submitted to Modelling and Simulation in Materials Science and EngineeringOctober 11, 2019

(HEAs) [26]. HEAs are multicomponent alloys (N=5 or more elements) in near-equal compositions but generally forming single fcc or bcc phases with no precipitation. While other systems may consist of multiple phases, and some HEAs may be unstable to eventual precipitate formation, the existence of stable or metastable random phases with high atomic complexity is intriguing. Moreover, some of these HEA materials have impressive mechanical properties (strength, ductility, and/or fracture toughness) [11, 46].

Scientific and technological interest in both dilute solute-strengthened alloys (Al-Mg, Mg-Y, Ni-Al, and many others) and the HEAs, which are essentially high-concentration solute-strengthened materials, has led to the development of a general theoretical model to predict solute strengthening in random alloys [21, 22, 43, 41]. This theory is based on the motion of edge dislocations, which typically control strength — this has been demostrated by application of the same theoretical framework to fcc screw dislocations in [24] where they have shown the critical stress to move an edge dislocation at 0K to be comparable but typically slightly lower than the stress to move a screw dislocation. The full theory shows that the temperature- and strain-rate dependent flow strength stems from the intrinsic solute/dislocation interaction energies and the dislocation line tension [15, 16]. The solute/dislocation interaction energies are challenging to determine in real alloys, especially HEAs, due to the need for computational study of the dislocation core via first principles methods [32]. Experiments cannot provide this information directly either.

To enable the use of experimental inputs and/or first-principles inputs, the full theory has been reduced to a simpler form through the use of linear elasticity theory to compute the solute/dislocation interaction energies [43]. The elasticity model for solute strengthening then relies on fundamental material and solute quantities: elastic constants $C_{ij}$, dislocation Burgers vector $\mathbf{b}$, stable and unstable stacking fault energies $\gamma_{\text{ssf}}$ and $\gamma_{\text{usf}}$, dislocation line tension $\Gamma$, and the solute misfit strain tensors $\varepsilon_{ij}^{\text{misfit}}$ in the alloy. First-principles methods can compute all of these quantities, even in the highly-complex HEAs [48]. On the other-hand, mechanical tests are often carried out on polycrystals, and supplemented by TEM analyses, to obtain experimental values of properties like the average isotropic elastic constants, Burgers vector (and lattice constant $a$), and stacking fault width of the dissociated partials that arise in fcc crystals, from which $\gamma_{\text{ssf}}$ can be deduced. The solute misfit volumes $\Delta V = \varepsilon_{ii}^{\text{misfit}}a^3/4$ for fcc alloys can be determined in principle from lattice constant measurements on alloys of varying composition. Thus, if the elasticity approximation is accurate then the theory can be used to rationalize existing experimental measurements and to predict properties of new alloys via the use of first-principles computations on candidate alloys [38, 48].

The elasticity theory of solute strengthening has only been examined within isotropic elasticity. Yet the elemental fcc metals exhibit a range of anisotropies, as characterized by the Zener anisotropy $A=2C_{44}/(C_{11}-C_{12})$ where $C_{11}$, $C_{12}$, and $C_{44}$ are the three independent elastic constants in a cubic crystal, with $A\sim1.22$ for Al, $\sim2.57$ for Ni, $\sim3.21$ for Cu, and $\sim2.85$ for Au [5]. Dilute alloys based on Ni, Cu, and Au should thus be treated within anisotropic elasticity, and many fcc HEA families (e.g. Co-Cr-Fe-Mn-Ni-Al, Rh-Ir-Pt-Pd-Au-Ag-Ni-Cu) are at least moderately anisotropic. The aim of this paper is therefore to provide general results for solute-strengthening in the anisotropic elastic model for fcc random alloys.

The isotropic theory has a simple analytic form and experimental measurements may only provide averaged isotropic elastic constants. Therefore, we present results in terms of the difference in predictions between anisotropic and isotropic models. We show that both elasticity assumptions lead to qualitatively identical results, which enables the use of the isotropic model with a correction factor to account for estimated or anticipated anisotropy. Our results also allow for an understanding of whether the isotropic estimate is an underestimate or an overestimate, and to what approximate degree. Overall, predictions using the full anisotropic theory and isotropic theory using the Voigt averaged isotropic moduli are in very good agreement (within a few $\%$) over a wide range of anisotropy, $0.5<A<4$.

The remainder of the paper is organized as follows. Section 2 briefly reviews the current theory of solute-strengthening. Section 3 simplifies the theory using linear elasticity, for both anisotropic and isotropic models. In Section 4, predictions of isotropic and anisotropic models over a wide range of parametric dislocation core structures are compared. Section 5 discusses how to apply the theory with limited experimental or first-principles properties. Section 6 summarizes the paper.

## 2. Theory of solute strengthening

We consider random alloys, *i.e.* for an alloy containing $n$ elements at concentrations $c_n$, the probability that a type-$n$ solute occupies a particular lattice site is exactly $c_n$, irrespective of surrounding atom-types. When an initially straight edge dislocation is introduced into such a random alloy, it spontaneously becomes wavy as it moves into regions where the local solute environment reduces the energy of the local dislocation segment. However, the wavy structure has an increased line length, and so there is an energy cost to becoming wavy. The dislocation thus takes on a wavy structure that minimizes its total energy, *i.e.* lowering of potential energy due to interactions with favorable solute environments and increase in elastic energy due to line tension. Each local segment of the dislocation is then in a local energy minimum, and motion of that segment (plastic flow) then requires stress-assisted thermal

activation out of the local minimum and over the adjacent local maximum into the subsequent local minimum along the glide plane. The overall dislocation moves as the local segments advance via the thermally-activated process. This general framework was first postulated by Labusch [15, 16].

Leyson *et al.* [21, 22] formalized the above description in a more quantitative way, in particular (i) by making connection with the atomistically-computed solute / dislocation interaction energies, and (ii) by considering a dislocation of total length $L$ to become wavy with a wavelength $4\zeta$ and amplitude $w$, constructing the total energy as a function of $(\zeta, w)$, and minimizing the total energy to obtain the characteristic length scales $(\zeta_c, w_c)$. The elastic energy due to increased dislocation length can be expressed as

$$
\Delta E_{\text{el}} \approx \Gamma \left(\frac{w^2}{2\zeta}\right) \left(\frac{L}{2\zeta}\right),
\tag{1}
$$

when $w \ll \zeta$, which is typically the case. The potential energy due to solute interactions with the dislocation starts from the fundamental interaction energy $U(x_i, y_j)$ between a solute at in-plane position $(x_i, y_j)$, and a straight dislocation aligned along $z$ at the origin. For fcc metals, $x$ and $y$ are the $<110>$ and $<111>$ crystallographic directions. In a specific solute environment, the change in potential energy of a segment as the dislocation glides a distance $w$ from an initial starting point is

$$
\Delta U_{\text{tot}}(\zeta, w) = \sum_{ij} n_{ij} \left[U(x_i - w, y_j) - U(x_i, y_j)\right]
\tag{2}
$$

where $n_{ij}$ is the number of solute atoms along the dislocation length $\zeta$. In a random alloy, the average energy change is zero, and the dislocation segments seek favorable (energy-lowering) fluctuations that scale with the standard deviation of the potential energy change. The total potential energy of the wavy dislocation in the random alloy can be derived as [22],

$$
\Delta E_p = -\left(\frac{\zeta}{\sqrt{3}b}\right)^\frac{1}{2} \Delta \tilde{E}_p(w) \cdot \frac{L}{2\zeta},
\tag{3}
$$

$$
\text{where } \Delta \tilde{E}_p(w) = \left[c \sum_{ij} (U(x_i - w, y_j) - U(x_i, y_j))^2\right]^\frac{1}{2},
\tag{4}
$$

is the characteristic energy fluctuation per unit length of dislocation and $c$ is the concentration of the solute.

Minimization of the total energy, $\Delta E_{\text{tot}} = \Delta E_p + \Delta E_{\text{el}}$, with respect to $\zeta$ is analytic. The subsequent minimization with respect to $w$ reduces to the solution

of $d\Delta \tilde{E}_p(w)/dw = \Delta \tilde{E}_p(w)/2w$. Each individual segment at length $\zeta_c$ then lies in a minimum local energy well of depth $-(\zeta_c/\sqrt{3}b))^{1/2}\Delta \tilde{E}_p(w_c)$ with a nearby energy maximum at distance $w_c$ along the glide plane. The net barrier height, including the reduction in elastic energy, leads to an energy barrier of

$$
\Delta E_b = 1.22 \left(\frac{w_c^2 \Gamma \Delta \tilde{E}_p^2(w_c)}{b}\right)^{\frac{1}{3}} . \tag{5}
$$

The energy barrier is reduced by an applied stress, which does work of $-\tau b \zeta_c x$ on the dislocation as it glides over distance $x$. The zero-temperature yield stress $\tau_{y0}$ is the stress needed to reduce the barrier to zero so that the dislocation moves with no thermal activation. This flow stress is given by

$$
\tau_{y0} = \frac{\pi}{2} \frac{\Delta E_b}{b \zeta_c(w_c) w_c} = 1.01 \left(\frac{\Delta \tilde{E}_p^4(w_c)}{\Gamma b^5 w_c^5}\right)^{\frac{1}{3}} . \tag{6}
$$

For stresses $\tau < \tau_{y0}$, the energy barrier is finite and the dislocation segments overcome the barrier by thermal activation. The time required to overcome the barrier is then related to the plastic strain rate. The finite-temperature and finite strain-rate flow stress $\tau_y(T,\dot{\varepsilon})$ is then derived as

$$
\tau_y(T,\dot{\varepsilon}) = \tau_{y0} \left[ 1 - \left( \frac{kT}{\Delta E_b} \ln \frac{\dot{\varepsilon}_0}{\dot{\varepsilon}} \right)^{\frac{2}{3}} \right] ; \quad \text{at low temperatures}, \tag{7}
$$

where $\dot{\varepsilon}_0 = 10^4 s^{-1}$, consistent with previous works [21, 43]. At stresses below $\approx 0.5\tau_{y0}$ waviness on multiple scales becomes important [17, 20] but this is not crucial for the present paper.

From the skeleton review of the theory above, it is evident that the key parameters for solute strengthening are the energy barrier $\Delta E_b$ and zero-temperature flow stress $\tau_{y0}$. These quantities are directly derived from the underlying solute/dislocation interaction energies $U(x_i,y_j)$ for the dissociated edge dislocation and the dislocation line tension $\Gamma$, and so the theory has no fitting parameters. The theory above has been outlined for the case of a dilute binary alloy (one type of solute in a host matrix) but the analysis can be generalized to arbitrary compositions and thus encompasses High Entropy Alloys and other non-dilute solid solution alloys [43, 41].

### 3. Linear elasticity model

The solute/dislocation interaction energies $U(x_i, y_j)$ can be computed using intensive first-principles methods [21, 22, 41, 47] for dilute alloys. Atomistic simulations using semi-empirical potentials can be employed, but are rarely quantitative for real materials and so such simulations are best used to test the theory and any approximations to it. It is thus valuable to gain broad insight through the introduction of reasonable approximations that enable great simplification of the theory.

#### 3.1. Anisotropic elasticity for solute/dislocation interactions

In linear elasticity, the solute/dislocation interaction energy is
$$
U(x_i, y_j) = p(x_i, y_j)\Delta V, \tag{8}
$$
where $p(x_i, y_j)$ is the pressure field created at position $(x_i, y_j)$ by the dislocation centered at the origin. The above expression is specific to substitutional solutes in cubic materials; the general form involves the contraction of the stress tensor and the solute misfit strain tensor [7, 8, 37, 38] and is straightforward. Note that solute interactions with the stacking fault of the dissociated fcc dislocation are neglected here — see Varvenne et al. [41] for their inclusion and, when considering plastic flow at moderate temperatures, there is no solute diffusion to the stacking faults (and so no Suzuki effect). The pressure field of the dislocation depends on the dislocation core structure. The dislocation structure is characterized generally by the distribution of Burgers vector $\partial \mathbf{b}/\partial x$ along the glide plane; we discuss analytical descriptions of the core structure later. The pressure field generated by the dislocation structure is then a function of the Burgers vector distribution and the alloy elastic constants, and can be written in the form
$$
p(x_i, y_j) = C_{44} f\left(x_i, y_j, \frac{C_{11}}{C_{44}}, A, \frac{\partial \mathbf{b}}{\partial x}\right), \tag{9}
$$
where $f$ is a dimensionless pressure field. $f$ is obtained from the fundamental Stroh solution $\sigma_{ij}^{\text{Stroh}}$ for the components of the stress field created by an incremental Burgers vector $d\mathbf{b}(x')$ in an anisotropic material [34], followed by superposition of the fields due to all the increments of Burgers vector. Specifically, we can write
$$
f(x_i, y_j) = \frac{1}{C_{44}} \int_{-\infty}^{\infty} \frac{\partial \sigma_{kk}^{\text{Stroh}}}{\partial \mathbf{b}}(x_i - x', y_j)\frac{\partial \mathbf{b}}{\partial x}(x')dx'. \tag{10}
$$


Substituting the above approximation for $U(x_i, y_j)$ into all of the prior results leads to a decoupling of the solute misfit volume and the dislocation fields. The key energy quantity in Equation 4 becomes

$$
\begin{aligned}
\Delta \tilde{E}_{p}(w) &= C_{44} \Delta V c^{\frac{1}{2}}\left[\sum_{i j}\left(f\left(x_{i}-w, y_{j}\right)-f\left(x_{i}, y_{j}\right)\right)^{2}\right]^{\frac{1}{2}}, \\
&= C_{44} \Delta V c^{\frac{1}{2}} g\left(w, \frac{C_{11}}{C_{44}}, A, \frac{\partial \mathbf{b}}{\partial x}\right).
\end{aligned}
\tag{11}
$$

The minimization with respect to $w$ to obtain $w_c$ involves only the dislocation-core-structure-dependent quantity $g$ via the solution of $dg/dw = g/2w$. The final quantities controlling the flow stress versus temperature and strain rate reduce to the forms

$$
\Delta E_{b}=1.22\left(w_{c} g\left(w_{c}\right)\right)^{\frac{2}{3}}\left(\frac{c C_{44}^{2} \Delta V^{2} \Gamma}{b}\right)^{\frac{1}{3}},
\tag{12}
$$

$$
\tau_{y 0}=1.01\left(\frac{g^{4}\left(w_{c}\right)}{w_{c}^{5}}\right)^{\frac{1}{3}}\left(\frac{c^{2} C_{44}^{4} \Delta V^{4}}{\Gamma b^{5}}\right)^{\frac{1}{3}}.
\tag{13}
$$

In a dilute alloy, for a given matrix the analysis is independent of the solute(s) added to create the alloy. In a concentrated alloy, the material properties (elastic constants, line tension, Burgers vector, stacking fault energy, and core structure) are those of a hypothetical average-alloy matrix. The solute misfit volume and concentration only enter through multiplication after all minimizations have been carried out. In the elasticity theory, we can thus address the key features of solute strengthening as a function of the elastic properties of the material, the line tension, and the dislocation structure as represented through $\partial \mathbf{b}/\partial x$.

For non-dilute alloys or HEAs with more than one type of solute, $c\Delta V^2$ is replaced with $\sum_n c_n(\Delta \bar{V}_n^2 + \sigma_{\Delta V_n}^2)$ [43], where $\Delta \bar{V}_n$ is the average misfit volume of solute $n$ and $\sigma_{\Delta V_n}$ is its standard deviation due to local fluctuations in chemical occupation. Also, the elastic moduli and dislocation structure entering the theory are those for the concentrated alloy at the given composition.

### 3.2. Solute/dislocation interactions estimated with average isotropic elastic constants

The theory can be reduced further under the assumption of isotropy, in line with Ref. [43]. Introducing the average isotropic elastic constants $\mu_{\text{avg}}$ and $\nu_{\text{avg}}$, the quantity $g$ can be written as

$$
g\left(w, \frac{C_{11}}{C_{44}}, A, \frac{\partial \mathbf{b}}{\partial x}\right)=\left(\frac{\mu_{\text{avg}}}{C_{44}}\right) \frac{1+\nu_{\text{avg}}}{1-\nu_{\text{avg}}} g^{\text{iso}}\left(w, \frac{\partial \mathbf{b}}{\partial x}\right).
\tag{14}
$$

In this form, the contribution to solute-dislocation interaction energy from dislocation structure ($g^{\text{iso}}$) and elasticity are fully decoupled. Note that the quantity $g^{\text{iso}}$ is equal to the quantity $\frac{1}{3\pi}\left[\sum_{ij} \Delta f_{ij}^2(w)\right]^{\frac{1}{2}}$ in Ref. [43]. All predictions scale with $\mu_{\text{avg}}$ and $\nu_{\text{avg}}$. Here, we examine the three standard averaging schemes of Voigt, Reuss, and Hill [44, 31, 13]. For all three, the bulk modulus is

$$
K_{\text{avg}} = \frac{C_{11} + 2C_{12}}{3}, \tag{15}
$$

while the shear moduli are given by

$$
\mu_{\text{avg}}^{\text{Voigt}} = \frac{C_{11} - C_{12} + 3C_{44}}{5}, \tag{16}
$$

$$
\mu_{\text{avg}}^{\text{Reuss}} = \frac{5C_{44}\left(C_{11} - C_{12}\right)}{3C_{11} - 3C_{12} + 4C_{44}}, \tag{17}
$$

$$
\mu_{\text{avg}}^{\text{Hill}} = \frac{\mu_{\text{avg}}^{\text{Voigt}} + \mu_{\text{avg}}^{\text{Reuss}}}{2}. \tag{18}
$$

The average Poisson's ratio $\nu_{\text{avg}}$ is then computed from $\mu_{\text{avg}}$ and $K_{\text{avg}}$ as

$$
\nu_{\text{avg}} = \frac{3K_{\text{avg}} - 2\mu_{\text{avg}}}{2\left(3K_{\text{avg}} + \mu_{\text{avg}}\right)}. \tag{19}
$$

The Voigt and Reuss results are polycrystalline upper and lower bounds, respectively. The intermediate Hill average was proposed because it tends to be closer to many experimental measurements of elastic constants in polycrystals than either of the bounds. Lastly, $\mu_{\text{avg}}/C_{44}$ and $\nu_{\text{avg}}$ are dimensionless functions of only $C_{11}/C_{44}$ and the anisotropy ratio $A$. Therefore, comparisons between isotropic and anisotropic elasticity depend only $C_{11}/C_{44}$, $A$, the slip density $\partial \mathbf{b}/\partial x$, and the chosen isotropic averaging scheme.

### 3.3. Dislocation core structure parameterization
The strengthening parameters depend on the dislocation structure as characterized by $\partial \mathbf{b}/\partial x$. In fcc systems, the relevant $a/2\langle 110 \rangle$ dislocations dissociate into two Shockley partial dislocations, $\mathbf{b}_{\mathbf{p},1}$ and $\mathbf{b}_{\mathbf{p},2}$, of $a/6\langle 112 \rangle$ type. Following Varvenne *et al.* [43], we parameterize the dislocation core structure in terms of two Gaussian functions of width $\sigma$ separated by the Shockley partial separation $d$. The classical analytical Peierls-Nabarro model yields a Lorentzian distribution [6], and atomistic

simulations of the shear displacement across the glide plane show a slow decay sim- ilar to the Lorentzian function. However, the atomistic simulations give the total shear displacement, not solely the "plastic" displacement associated with the dis- tribution $\partial \mathbf{b} / \partial x$. The slow decay in atomistics is well-represented as arising from the elastic strain due to a Gaussian distribution of Burgers vector $\partial \mathbf{b} / \partial x$, as shown explicitly for atomistic models of Al, Cu, and Ni in Appendix A. The Burgers vector distribution is thus parameterized as

$$
\frac{\partial \mathbf{b}}{\partial x}(x)=\frac{1}{\sqrt{2 \pi \sigma^{2}}}\left(\mathbf{b}_{\mathbf{p}, \mathbf{1}} \mathrm{e}^{-\frac{(x+d / 2)^{2}}{2 \sigma^{2}}}+\mathbf{b}_{\mathbf{p}, \mathbf{2}} \mathrm{e}^{-\frac{(x-d / 2)^{2}}{2 \sigma^{2}}}\right).\qquad(20)
$$

When carrying out the minimization with respect to $w$, the solution can yield oneor two local minima depending on the core structure [41]. Two local minima, $w_{c, 1}$  and $w_{c, 2}$ , emerge when $d$ is sufficiently larger than $\sigma$ . In such situations, the Burgers vector distribution has two very distinct peaks, one for each partial, and the first minimum occurs at small $w_{c}$ typically smaller than the partial separation $d$ . Also, as evident from Figure 1, the "second" larger $w_{c, 2}$ solution exists for all parameter values, with $w_{c, 2}$ decreasing with decreasing $d / b$ . The "first solution" $w_{c, 1}$ exists for larger $d / b$ but is subsumed by the "second solution" below $d / b \approx 6$ . Unfortunately, the literature seems to suggest that it is the larger- $w_{c}$ solution that emerges with increasing $d / b$ whereas it is really the smaller $w_{c}$ that emerges as a new solution. Later on we discuss results for both solutions when they arise.

![](./images/812701277929603072_1.jpg)

Figure 1: Non-dimensional total energy of a wavy dislocation in a random alloy as a function of the amplitude, for various Shockley partial separation distances $d$ at fixed partial peak width $\sigma/b=1.5$ as computed assuming isotropic elasticity. For partial separations $>6b$, there are two minima at $w_{c,1}$ and $w_{c,2}$ while for small partial separations the first minimum is subsumed by the second minimum, resulting in a single minimum label as $w_{c,1}$.

## 4. Results

We now assess the accuracy of the easily-used isotropic model relative to the more-complex anisotropic model. Anisotropy enters in the theory through (i) the dislocation line tension, and (ii) the dislocation core structure quantity $g$. Both aspects are examined in the following.

### 4.1. Line tension

The line tension $\Gamma$ enters the theory as $\Gamma^{1/3}$ in $\Delta E_b$ and as $\Gamma^{-1/3}$ in $\tau_{y0}$ (Equations 12 and 13), and hence results are weakly dependent on the precise value of $\Gamma$. However, the line tension scales with the elastic moduli, and so is in principle a function of the anisotropy. For fcc alloys, the line tension is best related to the shear modulus in the $<111>$ plane along the $<110>$ direction, $\mu_{111/110}=(C_{11}-C_{12}+C_{44})/3$ via the scaling relation $\Gamma=\alpha\mu_{111/110}b^2$. Values of $\alpha\sim1/16-1/8$ have been used, with the larger value found in several atomistic studies of bowed-out dislocations [36]. In the absence of the crystal anisotropic elastic constants,

$\mu_{111/110}$ must be appropriately estimated. Figures 2(a)-(c) thus displays the ratios $\mu_{\text{avg}}/\mu_{111/110}$ for the Voigt, Reuss and Hill averaging schemes, and for an important range of $A$ and $C_{11}/C_{44}$. The ratio $(\mu_{\text{avg}}^{\text{Hill}}/\mu_{111/110})^{1/3}$ is nearly unity over a wide range of $A$ and $C_{11}/C_{44}$, deviating by at most 5%. Thus, $\mu_{\text{avg}}^{\text{Hill}}$, which is close to the experimental polycrystalline shear modulus, should be used in estimating the line tension. The Voigt averaged moduli should *not* be used for estimating the line tension [4].

Thus, to minimize the differences between isotropic and anisotropic results, the line tension must be calculated either directly from $\mu_{111/110}$, or from the isotropic polycrystal data.

![](./images/812701277929603072_2.jpg)

Figure 2: Comparison of $\mu_{\text{avg}}$ with $\mu_{111/110}$ for the different isotropic averaging schemes as a function of $C_{11}/C_{44}$ and $A$.

### 4.2. Error of the isotropic approximation

In no case does the isotropic approximation for $g$ yield a different number of solutions for $w_c$ than the anisotropic case. Choosing the line tension as described

above, we thus compute the relative error of the isotropic solution as

$$
\frac{\Delta E_{b}^{\mathrm{iso}}-\Delta E_{b}}{\Delta E_{b}}=\left[\left(\frac{\mu_{\mathrm{avg}}}{C_{44}}\right) \frac{1+\nu_{\mathrm{avg}}}{1-\nu_{\mathrm{avg}}}\right]^{\frac{2}{3}}\left(\frac{w_{c}^{\mathrm{iso}}}{w_{c}} \cdot \frac{g^{\mathrm{iso}}\left(w_{c}^{\mathrm{iso}}\right)}{g\left(w_{c}\right)}\right)^{\frac{2}{3}}-1 ; \quad \text { and } \tag{21}
$$

$$
\frac{\tau_{y 0}^{\mathrm{iso}}-\tau_{y 0}}{\tau_{y 0}}=\left[\left(\frac{\mu_{\mathrm{avg}}}{C_{44}}\right) \frac{1+\nu_{\mathrm{avg}}}{1-\nu_{\mathrm{avg}}}\right]^{\frac{4}{3}}\left(\frac{w_{c}}{w_{c}^{\mathrm{iso}}}\right)^{\frac{5}{3}}\left(\frac{g^{\mathrm{iso}}\left(w_{c}^{\mathrm{iso}}\right)}{g\left(w_{c}\right)}\right)^{\frac{4}{3}}-1. \tag{22}
$$

The relative error is independent of (i) any absolute values of the elastic constants, (ii) the solute misfit volumes, (iii) dislocation line tension, (iv) total Burgers vector magnitude, and (v) any numerical prefactors. Thus, the results depend only on the ratios of anisotropic elastic constants, the isotropic averaging scheme (see equations 15–19) and the dislocation core structure. Note that the characteristic amplitude $w_{c}^{\text{iso}}$ is independent of the isotropic averaging scheme.

These dependencies are fully described through the non-dimensional elastic parameters $A=2 C_{44} /(C_{11}-C_{12}), C_{11}/C_{44}$, and core structure parameters $d/b$ and $\sigma/b$. We study a wide range $0.5 < A < 5$, the full physical range of $C_{11}/C_{44}$ for this range of $A$, and values $d/b=3,7,11,15$ and $\sigma/b=1.0,1.5,2.0,2.5$ that cover expected core structures (See Appendix A). We thus examine the range of possible errors defined in Equations 21 and 22 induced by the use of the isotropic approximation for these values.

### 4.3. Errors in energy barrier and zero-T strength

Overall, we find that the Voigt average provides the best agreement with the full anisotropic result. Indeed, figure 3 presents the differences in energy barrier and strength versus $A$ for the Voigt, Reuss, and Hill average, for a typical case $(C_{11}/C_{44}=$ $2.7; d/b=7; \sigma/b=1.5)$. The error in the Hill result is typically twice that of the Voigt result, and of the opposite sign (negative rather than positive). Recall that the various isotropic models only differ via ratios of the dislocation pressure pre-factor $\mu_{\text{avg}}(1+\nu_{\text{avg}})/(1-\nu_{\text{avg}})$ (see Equation 14) and so results can be easily related analytically. We thus focus on the Voigt results below, which are generally the most accurate.

![](./images/812701277929603072_3.jpg)

Figure 3: Relative differences in $\Delta E_b$ and $\tau_{y0}$ estimated with average isotropic elastic constants versus those predicted with full stiffness tensor as a function of anisotropy ratio $A$ (for $C_{11}/C_{44}=2.7$ and dislocation core parameters being $d=7b$ and $\sigma=1.5b$). Results are reported for Voigt, Reuss and Hill isotropic averages. Filled circle markers: first minimum solution. Filled star markers: second minimum solution.

The differences in energy barrier and strength are very weakly dependent on $C_{11}/C_{44}$. Figure 4 presents the differences in energy barrier and strength versus $A$ using the Voigt model for various values of $C_{11}/C_{44}$, again for a typical core structure $(d/b=7; \sigma/b=1.5)$. The variations around the middle value of $C_{11}/C_{44}=2.7$ are typically less than $1\%$. This is well below the accuracy of the elasticity theory itself and so can be neglected. All further results below thus correspond to $C_{11}/C_{44}=2.7$.

![](./images/812701277929603072_4.jpg)

Figure 4: Relative differences in $\Delta E_b$ and $\tau_{y0}$ as estimated with Voigt isotropic elastic constants versus full anisotropy as a function of $C_{11}/C_{44}$ and anisotropy ratio (for dislocation core parameters $d=7b$ and $\sigma=1.5b$). Marker colors indicate different $C_{11}/C_{44}$ values. Filled circles: first minimum solution; filled stars: second minimum solution.

Figure 5 shows the relative differences in $w_c$, $\Delta E_b$ and $\tau_{y0}$ between the Voigt isotropic model and the full anisotropic elasticity as a function of anisotropy $A$, for the first minimum $w_{c,1}$ for various dislocation core structure parameters $(d/b, \sigma/b)$. Figure 6 shows the same quantities for the second minimum $w_{c,2}$. The differences in the value of $w_c$ are zero for most cases, and differ by $\pm b/2$ in only a few cases. The difference is not systematic with $\sigma/b$, and may arise due to the discrete increments of $b/2$ used in determining the minimum energy and thus the appropriate discrete value for $w_c$. Specifically, a very small energy change due to the isotropic approximation can shift the discrete minimum by $b/2$; this has consequences for the energy barrier and strength. Overall, however, the amplitude of the dislocation waviness is generally well-preserved (within $b/2$) using the isotropic model.

The differences in energy barrier $\Delta E_b$ for both minima (Figures 5(b), 6(b)) are typically positive and less than $5\%$ over a wide range of parameters. Larger differences correlate with the changes in the $w_c$ value by $b/2$. For the first solution $(w_{c,1})$, which controls the low-temperature behavior, the errors can be negative and reach $\approx 10\%$ but only for very high anisotropy, the narrowest core structures, and widest core separations. Overall, however, corrections to the energy barrier due to anisotropy are not significant except when the $w_c$ is shifted by $b/2$, which occurs mainly for $\sigma/b=1.0, 2.0$ and high levels of anisotropy.

The differences in zero-temperature strength $\tau_{y0}$ for both minima (Figures 5(c), 6(c)) are typically positive and slightly larger than the energy barrier. For the second minimum $(w_{c,2})$ the errors are consistent across all core structures and generally remain below $+5\%$ for $A<5$. For the first minimum $(w_{c,1})$, the error for core widths $\sigma/b=1.0,2.0$ and wide partial spacings $d/b=15$ is over $10\%$ error even at moderate anisotropy of $A=2-3$. These errors correlate with the small shifts in $w_{c,1}$ by $b/2$ because the strength scales as $w_{c}^{-5/3}$ and $w_{c,1}$ is typically small $(\approx 5b)$ so that shifts by $\pm b/2$ are not negligible. This suggests the use of a continuous $w$ in the minimization rather than the use of a physical discrete set of $w$ spaced by $b/2$; this would lead to continuous variation in behavior and more-precise agreement between the isotropic and anisotropic theories.

Overall, the errors when using the Voigt isotropic elastic constants are within $5\%$ of the true anisotropic results, and typically overestimating. Deviations do increase with increasing $A$, but are almost always small for $A<3$ and remain moderate for $A<4$. We discuss the practical application of these results below.

![](./images/812701277929603072_5.jpg)

Figure 5: Relative differences in (a) $w_c$, (b) $\Delta E_b$ and (c) $\tau_{y0}$ computed with the Voigt-averaged isotropic elastic constants versus full anisotropic results as a function of the anisotropy ratio $A$, for the first minimum solution.

![](./images/812701277929603072_6.jpg)

Figure 6: Relative differences in (a) $w_c$, (b) $\Delta E_b$ and (c) $\tau_{y0}$ computed with the Voigt-averaged isotropic elastic constants versus full anisotropic results as a function of the anisotropy ratio $A$, for the second minimum solution. Note that there is no second minimum solution for the wider partial spreads $\sigma/b=2,2.5$ when the partial separation is $7b$ since it is effectively one full dislocation undissociated.

### 5. Practical application of the theory

We have shown that the difference between the Voigt isotropic model and the full anisotropic model are usually relatively small. The largest deviations arise when the isotropic model predicts a shift of $b/2$ in $w_c$ relative to the full anisotropic model, which occurs almost exclusively for $\sigma/b=1.0,2.0$ and can thus be identified. Otherwise, we consider the errors of $5\%$ to be well within the uncertainty of the elasticity model, relative to the full theory, and the full theory itself involves approximations. Thus, the isotropic theory can be used and then corrected to approach the anisotropic result based on available understanding. Experiments do not usually yield the Voigt moduli nor the core structure (especially $\sigma$), and application of the model also requires the line tension $\Gamma$. In this section, we therefore first present a parametric study of the predictions of the isotropic theory and then address how we envision the use of the anisotropic elasticity theory in combination with experimental or first-principles inputs.

### 5.1. Normalized results for $w_c$, $\Delta E_b$ and $\tau_{y0}$ using isotropic elasticity

We first present the isotropic results over the range of core structures. From Eqs. 12, 13 and 14, it is evident that the energy barrier and strength are functions of $w_c^\text{iso}(d/b,\sigma/b)$ and $g^\text{iso}(w_c,d/b,\sigma/b)$, with

$$
\Delta E_{b} \propto\left(w_{e}^{\text {iso }} g^{\text {iso }}\right)^{2 / 3},
\tag{23}
$$

$$
\tau_{y 0} \propto\left(g^{\text {iso }} / w_{c}^{\text {iso } 5 / 4}\right)^{4 / 3}.
\tag{24}
$$

Figures 7(b) and 7(c) show these normalized quantities over a wide range of $(d/b,\sigma/b)$ with the two solutions for $w_c$ (where applicable). Figure 7(a) presents the $w_{c,1}$ and $w_{c,2}$, although these are not directly needed in practical application of the model.

Figure 7(c) shows that the strength quantity is quite sensitive to the partial core width $\sigma$, especially for small $\sigma$. The quantity $\sigma$, while correlated through the Peierls-Nabarro model to the unstable stacking fault energy and elastic constants of the alloy [6], is not well established. The atomistic simulations in Appendix A, and previous analyses in Ref. [43], indicate that a range $1.5<\sigma/b<2.5$ prevails across most materials. Subsequent applications of the model used the value $\sigma/b=1.5$ across a wide range of materials with good success and we have seen above that the $w_c$ for this value of $\sigma/b$ agrees with that obtained in the full anisotropic model; this is further discussed below.

![](./images/812701277929603072_7.jpg)

Figure 7: (a) Dislocation roughening amplitude $w_c$, (b) dimensionless $\Delta E_b$, and (c) dimensionless $\tau_{y0}$ versus partial separation distance $d/b$, for different partial core spreading $\sigma/b$, as computed assuming isotropic elasticity.

### 5.2. Application using experimental or computational inputs

Here we provide a simple method for experimentalists and computational material scientists to investigate alloy strengthening in existing or new materials, reasonably accounting for elastic anisotropy. This is further illustrated on a specific HEA case.

In section 4 we have established that the dislocation line tension is well estimated as $\Gamma = \alpha\mu b^2$ using the Hill-average moduli. We have also compared the energy barrier for dislocation motion ($\Delta E_b$) and the zero-temperature yield stress ($\tau_{y0}$) using Voigt-averaged elastic constants versus full anisotropic stiffness tensor, and found a deviation of mostly 5% (occasionally $\sim 10\%$ for $\Delta E_b$ and $\geq 10\%$ for $\tau_{y0}$, but only for very high anisotropy). So, for a first estimation of the strengthening, we can avoid the cumbersome anisotropic formalism and instead make isotropic predictions $\Delta E_b^{\text{Voigt}}$ and $\tau_{y0}^{\text{Voigt}}$, using the Voigt-averaged elastic constants. The dimensionless coefficients of Equations 23 and 24 for $\Delta E_b$ and $\tau_{y0}$ are shown in Figure 7. Full results are then obtained by multiplying the dimensionless results by the appropriate prefactors using Voigt-averaged elastic constants

$$
\Delta E_b \text{ prefactor: } \quad 1.22 \left( \mu_{\text{avg}}^{\text{Voigt}} \frac{1 + \nu_{\text{avg}}^{\text{Voigt}}}{1 - \nu_{\text{avg}}^{\text{Voigt}}} \right)^{\frac{2}{3}} \left( \left( \sum_n c_n \Delta \bar{V}_n^2 \right) \Gamma b \right)^{\frac{1}{3}}, \tag{25}
$$

$$
\tau_{y0} \text{ prefactor: } \quad 1.01 \left( \mu_{\text{avg}}^{\text{Voigt}} \frac{1 + \nu_{\text{avg}}^{\text{Voigt}}}{1 - \nu_{\text{avg}}^{\text{Voigt}}} \right)^{\frac{4}{3}} \left( \frac{\left( \sum_n c_n \Delta \bar{V}_n^2 \right)^2}{\Gamma b^{10}} \right)^{\frac{1}{3}}, \tag{26}
$$

according to Equations 12 and 13. Finally, for a more-accurate prediction accounting for the elastic anisotropy, the above isotropic estimations for $\Delta E_b$ and $\tau_{y0}$ can be corrected by the additional factors shown in Figures 5 and 6.

The above procedure requires ingredients from either experiments or atomistic simulations: $\mu_{\text{avg}}^{\text{Voigt}}$ and $\nu_{\text{avg}}^{\text{Voigt}}$, the norm of the Burgers vector $b$, the solute misfit volumes $\Delta V_n$, the line tension of the dislocation $\Gamma$ and the Shockley partial separation $(d)$ and partial spreading $(\sigma)$. The Zener factor $A$ is required for choosing the appropriate anisotropy correction factors. We detail in the following how to get all these quantities.

Elastic constants enable the determination of $\mu_{\text{avg}}^{\text{Voigt}}$, $\nu_{\text{avg}}^{\text{Voigt}}$, $A$, and $\Gamma \propto \mu_{111/110} \approx \mu_{\text{avg}}^{\text{Hill}}$. The $C_{ij}$ can be obtained in several different ways, each with a different level of accuracy. The elastic constants can be computed using first-principles density-functional theory (DFT) calculations, which is reasonably accurate. They can also be estimated using the elemental values and a rule-of-mixtures law, $C_{ij}^{\text{rom}} = \sum_n c_n C_{ij}^n$. The full stiffness tensor of an existing alloy sample can be measured using standard methods for single crystals and advanced techniques for polycrystals [23, 14, 9]. It is

more conventional, however, to measure only the average elastic moduli of untextured polycrystals, which are typically close to the Hill approximation [13]. $\Gamma$ can thus be computed using the experimental isotropic shear modulus. The Voigt-averaged values can then be estimated by using the anisotropy $A$ of the rule-of-mixtures $C_{ij}^{\text{rom}}$ and the measured isotropic elastic constants with equations 15–19 as

$$
\mu_{\text{avg}}^{\text{Voigt}} \approx \mu_{\text{avg}}^{\text{expt}} \frac{(2A+3)(3A+2)}{3A^2+19A+3}, \tag{27}
$$

$$
\nu_{\text{avg}}^{\text{Voigt}} \approx \frac{\mu_{\text{avg}}^{\text{expt}} \left(1+\nu_{\text{avg}}^{\text{expt}}\right)-\mu_{\text{avg}}^{\text{Voigt}} \left(1-2\nu_{\text{avg}}^{\text{expt}}\right)}{2\mu_{\text{avg}}^{\text{expt}} \left(1+\nu_{\text{avg}}^{\text{expt}}\right)+\mu_{\text{avg}}^{\text{Voigt}} \left(1-2\nu_{\text{avg}}^{\text{expt}}\right)}. \tag{28}
$$

The lattice constant can be computed using first-principles methods or atomistic simulations with suitable interatomic potentials, or measured by diffraction. The solute misfit volumes can be computed with some additional effort [42, 48]. The misfit volumes can be determined in principle from experiments on alloys at different compositions followed by interpolation, but this requires fabrication of the alloys [3]. Lattice constants and misfit volumes can also be estimated using Vegard's law, which has been shown to be fairly accurate over a range of alloys [25, 43, 40, 48].

The dislocation core parameters $d/b$ and $\sigma/b$ are more challenging to assess. Fortunately, most results are insensitive to $d/b$ for $d/b \geq 7$. The partial separation $d/b$ can be estimated from knowledge of the stable stacking fault energy $\gamma_{\text{ssf}}$ and analytic and/or Peierls-Nabarro models. It can also be measured, on average, via TEM [29, 19]. The partial core spreading $\sigma/b$ is the least accessible quantity, yet the results are rather sensitive to this value. The uncertainty in $\sigma/b$ likely dominates the overall uncertainty of the elasticity model, whether isotropic or anisotropic. Successful past applications have used a single value of $\sigma/b=1.5$ with the Leyson *et al.* model, which is on the low end of physical values seen in several fcc atomistic core structures (Appendix A). This value may partially compensate for (i) additional "chemical" contributions in the core that are not included in the elasticity model and (ii) a larger $\sigma/b$ combined with a larger numerical prefactor (see Ref. [25] and discussion below). For example, for Al-X binary alloys, the full DFT-computed X-solute interactions energies were computed [22] but the final results could be well represented by the Leyson *et al.* elasticity model with $\sigma/b=1.5$.

As an illustrative example, here we compute the strength of the CoCrFeMnNi Cantor alloy using available experimental and computational inputs. The uniaxial tensile yield strength has been measured experimentally as 125 MPa at T=293K and strain rate $10^{-3}\text{s}^{-1}$ [30], after extrapolating the Hall-Petch grain-size effect to infinite grain size. Our prediction here is a refinement of the prediction of Varvenne *et al.* of

125 MPa based on isotropic elasticity [43] with the experimental polycrystal elastic constants, which was in very good agreement with the experimental value.

The single crystal elastic constants of the Cantor alloy have recently been measured by Teramoto et al. to be $C_{11}=195.9\,\mathrm{GPa}$, $C_{12}=117.7\,\mathrm{GPa}$, and $C_{44}=129.3\,\mathrm{GPa}$ [39]. The experimentally measured partial dislocation spacing of the edge dislocations $d$ is $\sim5-8\,\mathrm{nm}$ [29]. The lattice constant obtained from X-ray diffraction is $3.6\,\mathrm{\mathring{A}}$ [18] and therefore the Burgers vector $b$ is $2.5456\,\mathrm{\mathring{A}}$; so $d/b\gg7$. The average misfit volumes $\Delta\bar{V}_{n}$ were estimated in Ref. [43], based on experimental lattice constant data on Ni-Co, Ni-Cr, and Ni-Fe binaries and a range of Mn-containing HEAs and the application of Vegard's law, leading to the values $(-0.864,\,-0.684,\,0.286,\,0.466,\,0.796\,\mathring{\mathrm{A}}^{3})$ for (Ni, Co, Fe, Cr and Mn), respectively.

With the above inputs, we predict the yield strength using the isotropic theory with Voigt elastic constants and the additional corrections accounting for anisotropy obtained from Figures 5 and 6. The anisotropy is characterized by $A=3.3$ and $C_{11}/C_{44}=1.52$. The Voigt-averaged elastic constants are then computed to be $\mu_{\mathrm{avg}}^{\mathrm{Voigt}}=93.22\,\mathrm{GPa}$ and $\nu_{\mathrm{avg}}^{\mathrm{Voigt}}=0.233$ (from Equations 16, 19). The line tension is computed as $\Gamma=(1/8)\mu_{111/110}b^{2}=0.3497\,\mathrm{eV/\mathring{A}}$. The prefactors for computing $\Delta E_{b}$ and $\tau_{y0}$ using the Voigt moduli can be then computed from Equations 25 and 26 as $0.847\,\mathrm{eV}$ and $5.314\,\mathrm{GPa}$, respectively. The additional correction factors for anisotropy obtained from Figures 5(b) and 5(c) are 0.976 for $\Delta E_{b}$ and 0.95 for $\tau_{y0}$ (first minimum $w_{c,1}$ relevant here).

The remaining quantities needed in the theory that are not directly connected with the anisotropy are the misfit quantity $\sum_{n}c_{n}\Delta\bar{V}_{n}^{2}=0.43\,\mathring{\mathrm{A}}^{6}$, $d/b$ already established to be $\gg6$, and $\sigma/b$. We use the value $\sigma/b=1.5$ to be consistent with Varvenne et al. . With these values, we obtain the dimensionless quantities for $\tau_{y0}$ $(0.01758)$ and $\Delta E_{b}$ $(1.277)$ from Figure 7.

Multiplying all of the components discussed above yields $\tau_{y0}=88.75\,\mathrm{MPa}$ and $\Delta E_{b}=1.056\,\mathrm{eV}$. The uniaxial tensile yield strength at temperature and strain rate $\sigma_{y}=3.06\tau_{y}$ is then computed from Equation 7 as $128.7\,\mathrm{MPa}$, where the Taylor factor 3.06 for untextured fcc polycrystals is used. This prediction is in very good agreement with the experimental value of 125 MPa. The additional anisotropy factors do not lead to any significant change in the prediction in this particular case. This level of agreement is well within the uncertainty of the model and is not expected to be achieved for all alloys.

In the absence of the single-crystal elastic moduli, we would estimate the strength using the reported isotropic polycrystalline moduli $\mu=80-81\,\mathrm{GPa}$ and $\nu=0.25-0.265$ [18, 12, 45] as follows. The Voigt-average elastic moduli require $A$. This is estimated using the rule-of-mixtures $C_{ij}^{\mathrm{rom}}$ obtained from the elemental moduli. For

the Cantor alloy, where not all elements crystallize in fcc at low temperature, we use the first-principles DFT values for these elements in the fcc structure [33]. The resulting $C_{ij}^{\text{rom}}$ yields the estimate $A=2.35$, somewhat lower than the experimental value but still indicating a non-negligible level of anisotropy. The Voigt-averaged elastic constants are then computed to be $\mu_{\text{avg}}^{\text{Voigt}}=87.061$ GPa, $\sim6.5\%$ lower than the single-crystal value, and $\nu_{\text{avg}}^{\text{Voigt}}=0.248$ using Equations 27 and 28 respectively. The line tension uses the experimental shear modulus, $\Gamma=(1/8)\mu b^2=0.406$ eV/Å. The anisotropic correction factors for $\Delta E_b$ and $\tau_{y0}$ are 0.98 and 0.97 respectively (See Figure 5). The remaining inputs to the theory are unchanged. Using the components computed above yields the new predictions of $\tau_{y0}=82.15$ MPa and $\Delta E_b=1.089$ eV with a tensile yield strength at temperature and strain rate of 121.82 MPa. The difference with the more-complete prediction is small, and within the uncertainty of the theory.

The example above is intended mainly to show how the anisotropic results can be applied in practice, depending on the availability of experimental data. The objective is not to show that the anisotropic model gives better agreement with experiment in this particular case. In general, the anisotropic model gives higher strengths than the isotropic model because the Voigt-averaged elastic constants that best-capture the anisotropy are always larger than the isotropic elastic constants.

## 6. Discussion and Summary

The illustration in the previous section shows how experimental measurements provide some guidance on the relevant material properties needed in the theory. As noted, in the absence of experiments, many of these quantities can be estimated or computed using first-principles [48]. Thus, there are different avenues for evaluating the parameters needed in the model. Alloy design and discovery will follow the route of computation. The use of experimental inputs on materials that have been fabricated and tested can further validate the theory or help identify if other factors (solute-solute interactions; chemical short-range order; microstructure) are important in determining strength.

There are uncertainties associated with each material quantity, and the errors associated with these uncertainties can accumulate. The elasticity theory itself is an approximation to a more-complete theory, and even the full theory is not perfect. Nonetheless, the theory provides general guidance for understanding what material variables determine the strength, and their relative importance. This allows for the rationalization of experimental trends across families of alloys and provides a framework for searching higher-performance alloys.

The underlying theory of this complex process of a dislocation moving through a random alloy continues to evolve. In application to edge dislocations in bcc alloys, a new general stochastic analysis of the wavy dislocation configuration has been presented [25]. This analysis involves a more-detailed statistical analysis of the wavy dislocation structure via stochastic modeling of the structure segment-by-segment and including the full statistical distribution of possible segment energy changes due to the solute fluctuations. This analysis leads to additional numerical coefficients $\kappa = 0.56$ and $\beta = 0.833$ multiplying the line energy and potential energy terms appearing in Equation 5, respectively, and a change in the energy barrier by a factor $\sqrt{2}/(\sqrt{2}-0.25)=1.214$. The same analysis applies to fcc alloys, and the net effects are a factor of $\sqrt{\kappa/\beta}=0.82$ multiplying the line tension and the factor of 1.214 for the energy barrier, which then also enters the zero-temperature strength. These effects change the numerical coefficients in Equations 5 and 6 from (1.22, 1.01) to (1.39, 1.31), respectively. Thus, the successful use of $\sigma/b=1.5$, which is smaller than values seen in simulations (see Appendix A), together with the original Leyson model may reflect some cancellation of effects. For instance, using $\sigma/b=2.0$ and the corresponding dimensionless coefficient for $\tau_{y0}$ of $\sim0.012$ (see Figure 7(c)) with the revised prefactor of 1.31 gives a net factor of $\sim0.016$ which is nearly equal to that obtained using the present Leyson model with $\sigma/b=1.5$ (dimensionless coefficient $\sim0.017$) and with the Leyson coefficient 1.01, giving a net factor $\sim0.017$. However, for overall consistency with the previous literature and successful quantitative application of the Leyson model, we advocate continued use of the original Leyson model coefficients. We also note that these coefficients do not enter into any *difference* between isotropic and anisotropic theories, and so do not affect the primary analyses of this paper.

The theory is also currently being extended to include the effects of solute-solute interactions, while remaining in the random alloy limit. The anisotropic elasticity theory here will remain valuable because the solute-solute interactions can be incorporated along with the elasticity contributions to solute/dislocation interactions. Thus, the theory will continue to improve by incorporating increasing, but realistic, complexity.

In summary, we have shown that the predictions of a fully anisotropic elastic model for solute strengthening can be obtained using an isotropic elasticity model with the Voigt-averaged elastic constants for the dislocation field and the Hill-averaged elastic constants for the line tension. Additional small correction factors to match the anisotropic result precisely are also provided. The effects of anisotropy are not negligible — the use of the standard Hill estimate for the isotropic moduli in equations 21 and 22 leads to rather lower strength predictions for high anisotropy

$(A=3-4)$. Since many HEAs to date have anisotropy in the range of $A=2-4$, these corrections are valuable for making refined predictions. We have provided some guidelines on obtaining the data needed to make predictions. Results then follow using the coefficients presented graphically here, which we hope assists with application of the theory. The elastic theory provides an approximate but firm and analytical foundation for understanding trends in solute strengthening. Since the composition space in multi-component random alloys is immense, and experimental searching through that entire space is not feasible, the present theory provides a framework for rapid probing of the entire space in the search for attractive compositions for desired performance.

### 7. Acknowledgement

We thank the European Research Council for funding this work through the project ERC/FP Project 339081 entitled "PreCoMet Predictive Computational Metallurgy".

### Appendix A. Slip density in fcc elements

In elements having an fcc crystal structure of lattice parameter $a$, the prevailing $a/2<110>$ dislocations gliding on the $\{111\}$ planes dissociate into two mixed $a/6<112>$-type Shockley partial dislocations $\mathbf{b_{p,1}}$ and $\mathbf{b_{p,2}}$. The partials are separated by an intrinsic stable stacking fault of energy $\gamma_{\text{ssf}}$. The separation distance is determined by a balance between the repulsive elastic force between the partials and the attractive configurational force due to the stacking fault.

The cores of the Shockley partials are not delta-functions; the Burgers vector is spread along the glide plane over some range of atoms. The most widely-used model for describing the Burgers vector density of dislocation cores is the Peierls-Nabarro (P-N) model [6]. Under certain simplifications of the generalized stacking fault energy curve, the P-N model predicts a Lorentzian form of Burgers vector density as $\frac{\mathbf{b}}{\pi}\frac{\zeta}{x^{2}+\zeta^{2}}$ where $\zeta$ characterizes the width. Analysis shows that $\zeta \sim 1/\gamma_{\text{usf}}$ where $\gamma_{\text{usf}}$ is the unstable stacking fault energy. However, the computed values of $\zeta$ for partial cores are typically about $1/2$ those observed in simulations of atomistic dislocation cores [35]. Here, we show that a Gaussian function provides a better description of the plastic displacements associated with the atomistic dislocation core structure.

The Burgers vector distribution is the plastic slip distribution along the glide plane. The plastic slip is not the same as the total shear strain, due to the additional elastic shearing. In the centers of the partial cores of the dislocation, the elastic shearing is indeed small and the use of elasticity questionable. Away from the centers

515 of the partial cores, the shear distribution is composed of both plastic and elastic
516 contributions, and the elastic contributions stem from the elastic fields of the plastic
517 slip distribution along the entire slip plane.

518 We have examined the slip distribution of fully-relaxed atomistic edge dislocation
519 cores for Al, Ni, and Cu as predicted by widely-used interatomic potentials [27, 28].
520 Specifically, the core structure is created in the standard manner. In an initial
521 cylindrical sample of fcc crystal of radius $100b$ with orientation $x=$ (Burgers vector
522 and glide direction $\{110\}$), $y =$ (normal to the slip plane $\{111\}$), $z =$ (dislocation
523 line direction $\{112\}$), we impose the anisotropic displacement field corresponding to a
524 Volterra edge dislocation lying along the $z$ axis of the cylinder with the cut-plane for
525 slip lying along the $(x-y)$ slip plane in the region $(x < 0, y = 0)$. The displacements
526 of a thin annular region of atoms on the outer boundary of the cylinder are held fixed
527 at the Volterra solution and all interior atoms are then relaxed to their equilibrium
528 positions to create the dissociated dislocation. The displacement $\mathbf{u}(x)$ of every atom
529 away from its initial fcc position is then measured. We focus on the atoms in the
530 planes just above and just below the slip plane, and denote their positions by the
531 coordinate $x_i$ along the glide plane direction. The difference in shear displacements
532 across the slip plane is computed by finite differences in the discrete system as

$$
\left.rac{D\Delta\mathbf{u}}{Dx}ight|_{(x_i+x_{i+1})/2} = rac{\Delta\mathbf{u}(x_{i+1}) - \Delta\mathbf{u}(x_i)}{b/2}. \tag{A.1}
$$

533 Figure A.8 shows the computed $D\Delta u_x/Dx$ and $D\Delta u_z/Dx$ from the atomistic cal-
534 culations for the edge and screw components respectively of a edge full dislocation
535 in Al, Ni and Cu.

536 We are interested only in the plastic displacements, which are the discrete atom-
537 istic counterparts of the slip density $\partial\mathbf{b}/\partial x$. We consider the measured shear strains
538 $D\Delta u_x/(b/\sqrt{1.5}) > 0.01$ (corresponding to $D\Delta u_x/Dx > 0.016$) to be dominated by
539 the plastic displacements. We thus fit the measured $D\Delta\mathbf{u}/Dx$ in this region to a
540 sum of two Gaussians (Equation 20) as

$$
rac{D\Delta\mathbf{u}}{Dx} \approx rac{1}{\sqrt{2\pi\sigma^2}} \left( \mathbf{b}_{\mathbf{p},\mathbf{1}}\mathrm{e}^{-rac{(x+d/2-x_c)^2}{2\sigma^2}} + \mathbf{b}_{\mathbf{p},\mathbf{2}}\mathrm{e}^{-rac{(x-d/2-x_c)^2}{2\sigma^2}} ight). \tag{A.2}
$$

541 $d/b$ is taken as the distance between the peaks in $D\Delta u_x/Dx$ and the average or
542 center position $x_c$ of the full dislocation is taken as the middle of the peaks. $\sigma/b$ is
543 then the only fitting parameter, computed by a least-squares method, considering
544 both components $\frac{\partial b_x}{\partial x}$ and $\frac{\partial b_z}{\partial x}$. Figure A.8 shows the best-fit results using dislocations
545 symbols $\perp$ and the fitted value of $\sigma/b$ is shown in each figure. The fits are gener-
546 ally good, with root-mean-square error below $\sim 0.01$. We note that fits to other

547 types of functions, viz. logistic, Lorentzian, Gaussian-Lorentzian mixture, are not
548 significantly better or worse in this region.

![](./images/812701277929603072_8.jpg)

![](./images/812701277929603072_9.jpg)

![](./images/812701277929603072_10.jpg)

Figure A.8: Analysis of the dislocation core: atomistics, Gaussian fit and relative displacement gradient due to the fitted Gaussian core. The blue stars $\bigstar$ are the $D\Delta \mathbf{u}/Dx$ computed from atomistic displacements near the dislocation core, the dislocations $\perp$ are from bimodal Gaussian fit to the atomistic $D\Delta \mathbf{u}/Dx$ (explained in the text) and the red filled circles $\bullet$ are the $D\Delta \mathbf{u}^{\mathbf{tot}}/Dx$ computed from the anisotropic displacement field due to the dislocations $\perp$ (also explained in the text).

In the small shear strain region $<1\%$, Figure A.8 shows that the best-fit Gaussian plastic slip is significantly smaller than the total atomistic slip. This discrepancy may have tended to movitate the use of the Lorentzian function of the original PN model. However, in this regime, the total shear strains are dominated by the elastic shear strains caused by the Gaussian distribution of plastic slip. To demonstrate this, we compute the total anisotropic displacements $\mathbf{u}^{\text{tot}}(x)$ at every atomic site generated by the best-fit bimodal Gaussian Burgers vector distribution, using the Stroh formalism and the superposition principle to obtain the elastic contribution, similar to Equation 10. The quantity $D\Delta\mathbf{u}^{\text{tot}}/Dx$ is then computed from $\mathbf{u}^{\text{tot}}$ using finite differences as above. Figure A.8 shows the total slip distribution (elastic plus plastic) in the region outside the cores, and the results closely match the full atomistic results. The two-Gaussian model thus captures both the underlying plastic slip distribution and the surrounding elastic shearing for dissociated fcc dislocations.

Atomistically-computed dislocation core structures require either DFT or atom- istic interatomic potentials. DFT can be performed on elemental metals but alloy studies automatically include the response of the atoms to the random environment, preventing extraction of the underlying structure of the average alloy. In this case, computation of GPFE curves together with a double-Gaussian modeling of the dislo- cation core structure could be useful. Atomistic potentials are available for a number of elements, and some alloy systems, but with the usual caveats about accuracy rela- tive to the real materials. For alloys, the average-atom potential [42] can be created and used to examine the average core structure, but again relies on accuracy of the underlying potentials for the elemental constituents and their interactions. Typical values of $\sigma$ are thus valuable. In Figure A.8, we find values $1.75 < \sigma/b < 2.25$ for Al, Cu, and Ni. This range is consistent with the range $1.5 < \sigma/b < 2.5$ obtained by Varvenne *et al.* [43] for Fe-Ni-Cr alloys. They then showed that $\sigma/b=1.5$ provided good predictions for strength across a range of alloys, and this value was then used in subsequent work. While the solute strengthening does depend on $\sigma/b$, we thus remain consistent with previous work in suggesting the use of $1.5b$ in all fcc materials unless there is compelling evidence that a significantly different value should apply (see section 6).

[1] Ali Argon. *Strengthening Mechanisms in Crystal Plasticity*. Oxford University Press, August 2007.

[2] T. Balakrishna Bhat and V. S. Arunachalam. Strengthening mechanisms in alloys. *Proceedings of the Indian Academy of Sciences Section C: Engineering Sciences*, 3(4):275-296, December 1980.

[3] J. Bandyopadhyaya and K. P. Gupta. Low temperature lattice parameter of nickel and some nickel-cobalt alloys and grüneisen parameter of nickel. *Cryogenics*, 17(6):345–347, 1977.

[4] D. M. Barnett, R. J. Asaro, S. D. Gavazza, D. J. Bacon, and R. O. Scattergood. The effects of elastic anisotropy on dislocation line tension in metals. *J. Phys. F: Met. Phys.*, 2:854–864, 1972.

[5] Allan Bower. *Applied Mechanics of Solids*. CRC Press, October 2009.

[6] Vasily V. Bulatov and Wei Cai. *Computer Simulations of Dislocations*. Oxford series on materials modelling. Oxford University Press, 2006.

[7] E. Clouet. The vacancy - edge dislocation interaction in FCC metals: a comparison between atomic simulations and elasticity theory. *Acta Mater.*, 54:3543–3552, 2006.

[8] Emmanuel Clouet, Sbastien Garruchet, Hoang Nguyen, Michel Perez, and Charlotte S. Becquart. Dislocation interaction with C in $\alpha$-Fe: A comparison between atomic simulations and elasticity theory. *Acta Mater.*, 56:3450–3460, 2008.

[9] X. Du and Ji-Cheng Zhao. Facile measurement of single-crystal elastic constants from polycrystalline samples. *npj Computational Materials*, 3(17), 2017.

[10] H. Gleiter. Fundamentals of Strengthening Mechanisms. In *Strength of Metals and Alloys (ICSMA 6)*, pages 1009–1024. Elsevier, 1982.

[11] Bernd Gludovatz, Anton Hohenwarter, Dhiraj Catoor, Edwin H. Chang, Easo P. George, and Robert O. Ritchie. A fracture-resistant high-entropy alloy for cryogenic applications. *Science*, 345(6201):1153–1158, 2014.

[12] A. Haglund, M. Koehler, D. Catoor, E. P. George, and V. Keppens. Polycrystalline elastic moduli of a high-entropy alloy at cryogenic temperatures. *Intermetallics*, 58:62–64, 2015.

[13] R. Hill. The Elastic Behaviour of a Crystalline Aggregate. *Proceedings of the Physical Society. Section A*, 65(5):349–354, May 1952.

[14] C. J. Howard and E. H. Kisi. Measurement of single-crystal elastic constants by neutron diffraction from polycrystals. *Journal of Applied Crystallography*, 32(4):624–633, 1999.

[15] R. Labusch. A Statistical Theory of Solid Solution Hardening. physica status solidi (b), 41(2):659–669, 1970.

[16] R. Labusch. Statistische theorien der mischkristallhrtung. Acta Metall., 20(7):917 – 927, 1972.

[17] R. Labusch. Cooperative effects in alloy hardening. Czech. J. Phys., 38(5):474–481, 1988.

[18] G. Laplanche, P. Gadaud, O. Horst, F. Otto, G. Eggeler, and E. P. George. Temperature dependencies of the elastic moduli and thermal expansion coeffi- cient of an equiatomic, single-phase cocrfemnni high-entropy alloy. Journal of Alloys and Compounds, 623:348–353, 2015.

[19] G. Laplanche, A. Kostka, C. Reinhart, J. Hunfeld, G. Eggeler, and E.P. George. Reasons for the superior mechanical properties of medium-entropy CrCoNi com- pared to high-entropy CrMnFeCoNi. Acta Materialia, 128:292–303, April 2017.

[20] G. P. M. Leyson and W. A. Curtin. Solute strengthening at high temperatures. Modelling and Simulation in Materials Science and Engineering, 24(6):065005, August 2016.

[21] Gerard Paul M. Leyson, William A. Curtin, Louis G. Hector, and Christopher F. Woodward. Quantitative prediction of solute strengthening in aluminium alloys. Nature Materials, 9(9):750–755, September 2010.

[22] G.P.M. Leyson, L.G. Hector, and W.A. Curtin. Solute strengthening from first principles and application to aluminum alloys. Acta Materialia, 60(9):3873–3884, May 2012.

[23] D. Y. Li and J. A. Szpunar. Determination of single crystals' elastic constants from the measurement of ultrasonic velocity in the polycrystalline material. Acta Metallurgica et Materialia, 40(12):3277–3283, 1992.

[24] D. Ma, M. Friák, J. Pezold, D. Raabe, and J. Neugebauer. Computation- ally efficient and quantitatively accurate multiscale simulation of solid-solution strengthening by ab initio calculation. Acta Materialia, 85:53 – 66, 2015.

[25] F. Maresca and W. A. Curtin. Mechanistic origin of high retained strength in refractory bcc high entropy alloys up to 1900K. submitted.

[26] D.B. Miracle and O.N. Senkov. A critical review of high entropy alloys and related concepts. Acta Materialia, 122:448-511, January 2017.

[27] Y. Mishin, D. Farkas, M. J. Mehl, and D. A. Papaconstantopoulos. Interatomic potentials for monoatomic metals from experimental data and ab initio calcu- lations. Physical Review B, 59(5):3393-3407, February 1999.

[28] Y. Mishin, M. J. Mehl, D. A. Papaconstantopoulos, A. F. Voter, and J. D. Kress. Structural stability and lattice defects in copper: Ab initio, tight-binding, and embedded-atom calculations. Physical Review B, 63(22), May 2001.

[29] Norihiko L. Okamoto, Shu Fujimoto, Yuki Kambara, Marino Kawamura, Zheng- hao M. T. Chen, Hirotaka Matsunoshita, Katsushi Tanaka, Haruyuki Inui, and Easo P. George. Size effect, critical resolved shear stress, stacking fault en- ergy, and solid solution strengthening in the CrMnFeCoNi high-entropy alloy. Scientific Reports, 6:35863, October 2016.

[30] F. Otto, A. Dlouhý, Ch. Somsen, H. Bei, G. Eggeler, and E. P. George. The influences of temperature and microstructure on the tensile properties of a CoCr- FeMnNi high-entropy alloy. Acta Materialia, 61(15):5743-5755, 2013.

[31] A. Reuss. Berechnung der Fliegrenze von Mischkristallen auf Grund der Plas- tizittsbedingung fr Einkristalle . ZAMM - Zeitschrift fr Angewandte Mathematik und Mechanik, 9(1):49-58, 1929.

[32] D. Rodney, L. Ventelon, E. Clouet, L. Pizzagalli, and F. Willaime. Ab initio modeling of dislocation core properties in metals and semiconductors. Acta Mater., 124:633 - 659, 2017.

[33] S. L. Shang, A. Saengdeejing, Z. G. Mei, D. E. Kim, H. Zhang, S. Ganeshan, Y. Wang, and Z. K. Liu. First-principles calculations of pure elements: Equa- tions of state and elastic stiffness constants. Computational Materials Science, 48:813-826, 2010.

[34] A. N. Stroh. Dislocations and Cracks in Anisotropic Elasticity. Philosophical Magazine, 3(30):625-646, June 1958.

[35] B. A. Szajewski, A. Hunter, D. J. Luscher, and I. J. Beyerlein. The influ- ence of anisotropy on the core structure of Shockley partial dislocations within FCC materials. Modelling and Simulation in Materials Science and Engineering, 26(1):015010, 2018.

[36] B. A. Szajewski, F. Pavia, and W. A. Curtin. Robust atomistic calculation of dislocation linetension. *Modelling and Simulation in Materials Science and Engineering*, 23, 2015.

[37] A. Tehranchi, B. Yin, and W. A. Curtin. Softening and hardening of yield stress by hydrogen-solute interactions. *Philosophical Magazine*, 97(6):400-418, February 2017.

[38] A. Tehranchi, B. Yin, and W. A. Curtin. Solute strengthening of basal slip in Mg alloys. *Acta Materialia*, 151:56-66, 2018.

[39] Takeshi Teramoto, Kazuki Yamada, Ryo Ito, and Katsushi Tanaka. Monocrys- talline elastic constants and their temperature dependences for equiatomic CrM- nFeCoNi high-entropy alloy with the face-centered cubic structure. *Journal of Alloys and Compounds*, 777:1313-1318, 2019.

[40] C. Varvenne and William A. Curtin. Predicting yield strengths of noble metal high entropy alloys. *Scr. Mater.*, 142:92 - 95, 2018.

[41] C. Varvenne, G.P.M. Leyson, M. Ghazisaeidi, and W.A. Curtin. Solute strength- ening in random alloys. *Acta Materialia*, 124:660-683, February 2017.

[42] C. Varvenne, A. Luque, W. Nohring, and W. A. Curtin. Average-atom inter- atomic potential for random alloys. *Physical Review B*, 93(104201), 2016.

[43] C. Varvenne, Aitor Luque, and William A. Curtin. Theory of strengthening in fcc high entropy alloys. *Acta Materialia*, 118:164-176, October 2016.

[44] W. Voigt. *Lehrbuch der Kristallphysik*, (Leipzig Teubner) p 962. 1928.

[45] Z. Wu, H. Bei, G. M. Pharr, and E. P. George. Temperature dependence of the mechanical properties of equiatomic solid solution alloys with face-centered cubic crystal structures. *Acta Materialia*, 81:428-441, 2014.

[46] X. Yang, Y. Zhang, and P.K. Liaw. Microstructure and compressive properties of nbtivtaalx high entropy alloys. *Procedia Engineering*, 36:292 - 298, 2012.

[47] J. A. Yasi, L. G. Jr. Hector, and D. R. Trinkle. First-principles data for solid- solution strengthening of magnesium: From geometry and chemistry to proper- ties. *Acta Materialia*, 58(17):5704-5713, 2010.

[48] B. Yin and W. A. Curtin. First-principles-based prediction of yield strength in the RhIrPdPtNiCu high-entropy alloy. npj Computational Materials, 5(14), 2019.