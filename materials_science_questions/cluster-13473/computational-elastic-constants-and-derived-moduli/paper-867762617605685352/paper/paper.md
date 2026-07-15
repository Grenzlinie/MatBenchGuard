# THE ANOMALOUS YIELD BEHAVIOR OF FUSED SILICA GLASS

W. SCHILL¹, S. HEYDEN¹, S. CONTI² AND M. ORTIZ¹

ABSTRACT. We develop a critical-state model of fused silica plasticity on the basis of data mined from molecular dynamics (MD) calculations. The MD data is suggestive of an irreversible densification transition in volumetric compression resulting in permanent, or plastic, densification upon unloading. The MD data also reveals an evolution towards a critical state of constant volume under pressure-shear deformation. The trend towards constant volume is from above, when the glass is over-consolidated, or from below, when it is underconsolidated. We show that these characteristic behaviors are well-captured by a critical state model of plasticity, where the densification law for glass takes the place of the classical consolidation law of granular media and the locus of constant-volume states defines the critical-state line. A salient feature of the critical-state line of fused silica, as identified from the MD data, that renders its yield behavior anomalous is that it is strongly non-convex, owing to the existence of two well-differentiated phases at low and high pressures. We argue that this strong non-convexity of yield explains the patterning that is observed in molecular dynamics calculations of amorphous solids deforming in shear. We employ an explicit and exact rank-2 envelope construction to upscale the microscopic critical-state model to the macroscale. Remarkably, owing to the equilibrium constraint the resulting effective macroscopic behavior is still characterized by a non-convex critical-state line. Despite this lack of convexity, the effective macroscopic model is stable against microstructure formation and defines well-posed boundary-value problems.

## 1. INTRODUCTION

The anomalous shear modulus behavior of silica glass has been a long-standing topic of investigation. For instance, Kondo *et al.* [1] and references therein examined the non-monotonic dependence of the elastic moduli on pressure for fused quartz, cf. Fig. 1a. Notably, between 0 and 2.5 GPa, the shear modulus and bulk modulus decreases. Likewise, the anomalous pressure dependence of the strength of amorphous silica has also received considerable attention. For instance, Meade and Jeanloz [2] made measurements of the yield strength at pressures up to 81 GPa at room temperature and showed that the strength of amorphous silica decreases significantly as it is compressed to denser structures with higher coordination, Fig. 1b. Clifton *et al.* [3, 4, 5] and Simha and Gupta [6] investigated the effect of pressure on failure waves in silica and soda-lime glass through angled flyer

1

plate impact experiments and observed a loss of shear strength as the failure wave traversed the glass at pressures of 4-6 GPa.

![](./images/867762617605685352_1.jpg)

FIGURE 1. a) Elastic moduli vs. pressure as measured by Kondo et al. (1981) [1]; b) Measurements of the yield strength of SiO₂ glass at pressures as high as 81 GPa at room temperature showing the variation of the strength of amorphous silica as it is compressed to denser structures with higher coordination [2].

These phenomena appear to be intimately linked to structural rearrange- ments occurring at the atomic level. Sato and Funamori [7, 8] performed structural measurements of SiO₂ glass Si-O bond length and coordination number at pressures from 20 to 100 GPa using a diamond anvil cell and x-ray diffraction. They observed a transition from four-fold to six-fold coor- dinated structure that comes to completion at around 45 GPa. Wakabayashi et al. [9] studied the densification behavior again using a diamond anvil cell experimental setup and concluded that permanent densification occurs for pressures between 9 and 13 GPa. Vandembroucq [10] observed pressure- induced reorganizations of the amorphous network allowing a more efficient packing of tetrahedra that remain linked at their vertices only. Inamura et al. [11] studied transformations at pressures of up to about 20 GPa and temperatures of up to about 700 C. Their results are indicative of the ex- istence of a high pressure variant of silica glass. However, a sharp phase transformation was not observed, which is suggestive of a volumetric plastic hardening mechanism. Luo et al. [12] reported a novel dense silica poly- morph retrieved from shock-wave and diamond-anvil cell experiments. The polymorph is composed of face-sharing polyhedra and it has a density simi- lar to stishovite. Sterical constraints on the bond angles induce an intrinsic disorder in the Si positions and the resulting Si-coordination is transitional between four and sixfold.

Beyond the specific instance of fused silica, there exists an extensive liter- ature on the microstructural mechanisms that mediate plastic deformation in amorphous solids. Demkowicz and Argon [13] observed that in amorphous silicon plastic deformation is mediated by autocatalytic avalanches of unit inelastic shearing events. They performed a bond-angle analysis in order to

correlate changes in the average bond angle to discrete relaxation events.
Langer [14, 15] formulated a theory of *shear transformation zones* (STZ)
to describe viscoplastic deformation in amorphous solids. Langer's theory
accounts for the formation of deformation patterns such as shear banding in
metallic glasses. An alternative theory of structural rearrangement in bulk
metallic solids is based on *free-volume* kinetics. Chen and Goldstein [16]
observed that the flow in metallic glasses is strongly inhomogeneous at high
stresses and low temperatures, and attributed the patterning to local reduc-
tions in flow strength. Spaepen [17] later argued that these reductions are
due to the formation of free volume, and that the attendant inhomogeneous
flow is controlled by the competition between the stress-driven creation and
diffusional annihilation of free volume [18]. This hypothesis was later verified
experimentally by Argon [19].

![](./images/867762617605685352_2.jpg)

FIGURE 2. Molecular dynamics calculation of an idealized amor-
phous solid showing distinctive patterns in the deformation field
(the darker color indicates larger non-affine displacements) [20].

There have also been extensive molecular dynamics studies of the den-
sification behavior and plastic deformations of amorphous silica. Pilla *et
al.* [21], Lacks [22], Wu *et al.* [23], and Huang *et al.*, [24, 25] computed
pressure-density relationships over a broad range of pressures and temper-
atures. The attendant mechanisms of deformation entail transitions from
four-fold to six-fold coordination. In particular, Wu *et al.* [23] argued that
the four-fold to six-fold transition is not direct but involves the formation
of an intermediate five-fold coordinated structures at $\sim 12$ GPa and is only
complete at $\sim 60$ GPa. Liang and co-workers [26] noted anomalous be-
havior in the form of a minimum shear strength occurring at $\sim 10$ GPa

and proposed a mechanism involving unquenchable 5-fold defects. Mantisi *et al.* [27] utilized an NVE ensemble along with monoclinic change in the simulation box orientation to study combined pressure-shear loading. They observed steps, or *jerking*, in the shear stress vs. shear strain response, which they attribute to either finite size effects or localized dissipative re-arrangements. Several authors [20, 28] have performed molecular dynamics calculations on amorphous solids deforming under shear and found that the resulting deformation field forms distinctive patterns to accommodate permanent deformations, Fig. 2.

This past work strongly suggests that the plastic deformation of amorphous solids and, in particular, fused silica glass, is mediated by localized atomic-level instabilities that promote deformation patterning, Fig. 2. Such fine-scale pattern formation is reminiscent of the microstructure attendant to the relaxation of non-convex energy functionals [29]. We argue that a critical state plasticity model [30, 31] characterized by a strongly non-convex critical-state line in pressure-shear space explains the observed patterning. In order to formulate the theory, we perform Molecular Dynamics (MD) calculations designed to mine data on the volume-pressure relation and the pressure-shear response of fused silica, Section 2. In Section 3, we formulate a critical state constitutive model that closely reproduces the phenomenology revealed by the MD data. The data suggest that the critical-state line in the pressure-shear plane is indeed strongly non-convex. The handling of non-convexity necessitates a fundamental extension of classical plasticity, which is based on the principle of maximum dissipation and is predicated on the assumption of convexity of the elastic domain. In Section 4, we consider the implications of this extension and utilize notions from the Direct Methods in the Calculus of Variations to characterize explicitly and exactly the effective, or *relaxed*, behavior of fused silica at the macroscale. Remarkably, owing to the equilibrium constraint the effective macroscopic behavior of fused silica is still strongly non-convex, despite being stable with respect to microstructure formation. In particular, it defines well-posed boundary-value problems.

## 2. SUPPORTING MOLECULAR DYNAMICS CALCULATIONS

We use MD calculations for purposes of data mining, as well as to gain insight into the molecular basis of the inelasticity of glass.

**NB** (Pressure sign convention): *In keeping with the standard sign convention in experimental work and in MD, we take compressive pressure to be positive and tensile pressure to be negative.*

### 2.1. Methodology.
All calculations are performed using Sandia National Laboratories (SNL) Large-scale Atomic/Molecular Massively Parallel Simulator (LAMMPS) [32]. Calculations are carried out by explicit velocity-Verlet dynamics [33] with a time step of 0.5 fs for a total of $10^6$ time steps up to maximum deformations of the order of 20%, corresponding to strain

![](./images/867762617605685352_3.jpg)

Figure 3. Two views of the crystal structure of $\beta$-cristobalite (By Solid State (Own work) [Public domain], via Wikimedia Commons). Si: red atoms; O: grey atoms.

![](./images/867762617605685352_4.jpg)

Figure 4. Rapid cooling of a $\beta$-cristobalite melt and generation of an amorphous structure. Sample is cooled from $\beta$-cristobalite structure at $T=5000$K to $T=300$K in $t=470$ ps.

rates of approximately $4 \times 10^8$ 1/s. The representative volume element (RVE) contains 1,536 atoms and is subjected to periodic boundary conditions. We utilize $4^3$ primitive lattice cells of $\beta$-cristobalite to construct RVEs $4 \times 7.16 = 28.64$ Å wide. We have verified that unit cells comprising $8^3$ lattice cells do not significantly alter the results of the calculations.

All calculations are performed at a temperature of 300K. Long-range Coulombic interactions are evaluated by Ewald summation [34]. Short-range

interactions are assumed to obey the modified BKS potential

$$
E(r_{ij}) = A \exp(-r_{ij}/\rho) - C/r_{ij}^6 + D/r_{ij}^{12},
$$

proposed by [35], where $r_{ij}$ represents the interatomic distance. This po-
tential modifies the BKS potential proposed in [36] by the insertion of an
additional repulsive short-range interaction term in order to increase cal-
culation stability. The additional repulsive term additionally prevents the
unphysical divergence of the potential at small interatomic distances. The
parameters $A$, $C$, $D$, and $\rho$ used in calculations may be found in Table 4 of
[35].

In order to obtain an initial amorphous state of $\text{SiO}_2$, we utilize the melt
quench procedure No. 2 of Malavasi [35]. This quench procedure is per-
formed on an NVT ensemble (cf., e. g., [34]) and consists of cooling a $\beta$-
cristobalite melt, Fig. 3, from 5000K to 300K over 470 fs with a time step
of 2 fs, Fig. 4.

![](./images/867762617605685352_5.jpg)

FIGURE 5. Pressure-compression response showing densification
transition at $\sim 8$ GPa and unloading from several pressures show-
ing permanent densification upon full unloading.

2.2. Volumetric behavior. We begin by querying the behavior of amor-
phous silica under compressive volumetric loading and unloading. Fig. 5
shows the computed dependence of pressure on volume, including unload-
ing from a range of maximum pressures. At low maximum pressures, the
material unloads ostensibly elastically and returns to its initial undeformed

configuration upon unloading. By contrast, at pressures above $\sim 8$ GPa the material undergoes a distinctive permanent densification transition and the unloading curve exhibits permanent volumetric deformation.

Past studies [21, 24, 25] have reported similar pressure-density relationships, but calculations to date have been limited to significantly smaller sample sizes and monotonic loading. We note that without unloading it is not possible to ascertain whether the material response is nonlinear elastic, and therefore governed by a simple equation of state, or elastic-plastic. The results collected in Fig. 5 clearly reveal that the latter is indeed the case and that the volumetric response of glass exhibits inelasticity in the form of loading-unloading irreversibility, path-dependency and hysteresis at sufficiently high pressures.

![](./images/867762617605685352_6.jpg)

FIGURE 6. Computed and experimentally measured [8] radial distribution function at pressure $p=50$ GPa.

Radial distribution functions are commonly used as a validation and interpretation metric in MD simulations, e. g., Jin *et al.* [37, 38]. Fig. 6 shows the computed radial distribution function at 50 GPa. By way of comparison, Fig. 6 also shows corresponding experimental measurements performed by Sato and Funamori [8]. As can be seen from the figure, the MD calculations accurately capture the location and amplitude of the first peak in the radial distribution, which determines the radius of the first shell of atoms, and, to a fair degree of approximation, the location and amplitude of the second peak. The tails of the computed and measured radial distributions differ in fine detail but exhibit a similar rate of decay.

![](./images/867762617605685352_7.jpg)

FIGURE 7. Evolution of the distribution of coordination numbers
of the atoms in a sample during volumetric-compression loading
and unloading up to a pressure of 50 GPa. Si atom coordination
numbers are illustrated by the color bar and the oxygen atoms are
represented as black spheres. (a) and (b) Initial state; (c) and (d)
Peak pressure. (e) and (f) Unloaded state.

In order to elucidate the atomic-level mechanisms underlying permanent
volumetric deformation, we examine the evolution of the coordination num-
ber (cf., e. g., [38, 39])

$$
(1)\qquad CN = \int_{0}^{r_m} \rho g(r) 4\pi r^2 dr,
$$

where $\rho$ is the particle density, or number of atoms per unit volume, $g(r)$ is the radial distribution function and $r_m$ is the location of the first minimum of $g(r)$. The coordination number measures the number of nearest-neighbors of an atom. A simple way to approximate equation (1) given a set of atomic positions, is to perform a Voronoi tessellation of the atoms and then count the number of faces of individual Voronoi cells. In order to mitigate the effect of noise, a face is not counted if its area is below $1.3$ $\mathring{\text{A}}^2$, if it has more than 10 edges, or if one of its edges is shorter that $0.5$ $\mathring{\text{A}}$. Fig. 7 shows the evolution of the distribution of coordination numbers in a sample during compressive volumetric loading and unloading up to a pressure of 50 GPa. Initially, the entire sample consists of 4-fold coordinated atoms, Figs. 7a and 7b. At peak pressure, the coordination of most atoms changes from 4-fold to 6-fold, but a significant fraction of atoms exhibits an intermediate coordina- tion. Remarkably, upon unloading, only a small fraction of atoms recovers a 4-fold coordination, with the second largest fraction retaining 6-fold coor- dination and the majority of the sample remaining in an intermediate 5-fold coordination. These results evince the irreversible nature of the structural transitions attendant to permanent densification of glass, in agreement with experimental observations [7, 8, 9, 10, 11, 12]. The prevalence of transitional structures with a preponderance of 5-fold atoms upon unloading is also in agreement with the calculations of Wu et al. [23] and the experimental observations of Luo et al. [12].

2.3. Pressure-shear coupling. Using the same initial amorphous configu- ration of atoms, we now subject the RVE to pressure followed by monotonic shear deformation. To impart the shear deformation, affine boundary con- ditions are applied to the boundary of the RVE while simultaneously con- trolling the pressure by means of a barostat. We generate shear stress-strain curves over a range of pressure and we average the curves over a sample of initial conditions.

![](./images/867762617605685352_8.jpg)

FIGURE 8. a) Shear stress vs. shear strain under compressive pressure. b) Shear stress vs. shear strain under tensile pressure.

![](./images/867762617605685352_9.jpg)

FIGURE 9. Computed and experimentally measured [1] depen-
dence of the shear modulus on pressure. a) Overall view showing
initial anomalous dependence. b) Detail of the pressure range of
1-3 GPa.

The resulting average shear stress-strain curves are shown in Fig. 8. The
shear stress-strain curves exhibit an initial pressure-dependent elastic stage
followed by yielding. The computed dependence of the shear modulus on
pressure is shown in Fig. 9, which also includes measurements by Kondo
et al. [1] by way of comparison. As may be seen from the figure, the MD
results capture the anomalous initial decrease of the shear modulus with
pressure, cf. [3]. Furthermore, the MD results closely match the experimen-
tal measurements, which provides a measure of model validation.

A salient feature of the shear stress-strain curves is the serrated nature
of the yield plateau, also known as jerky flow, Fig. 8. These serrations have
been associated with localized bursts of atomic movements, or avalanches
[13]. In order to detect and quantify these avalanches, Falk and Langer [14]
proposed the parameter

$$
(2)\qquad D(i) \equiv \min _{\boldsymbol{\beta} \in \mathbb{R}^{3 × 3}}\left(\sum_{j}\left|\left(\boldsymbol{u}_{j}-\boldsymbol{u}_{i}\right)-\boldsymbol{\beta}\left(\boldsymbol{r}_{j}-\boldsymbol{r}_{i}\right)\right|^{2}\right)^{1 / 2},
$$

which represents the deviation of the incremental displacements $\boldsymbol{u}_{j}$ of the
atoms in a neighborhood of a reference atom $i$ from an incremental affine
deformation. Spikes in the distribution of $D(i)$ may therefore be identified
with the occurrence of avalanches around atom $i$. Fig. 10 shows the distri-
bution of $D(i)$ at points of a shear stress-strain curve when such avalanches
occur. In this case, no averaging with respect to initial conditions is per-
formed in order to preserve fluctuations. As may be seen from the figure,
the occurrence of avalanches correlates closely with drops in the stress-strain
curve, which identifies avalanches as the agents of plastic deformation and
the mechanism underlying the observed jerky plastic flow.

![](./images/867762617605685352_10.jpg)

FIGURE 10. Shear stress vs. shear strain curve and shear tran-
sitions at serrations. Blue indicates affine deformation whereas
yellow and red indicate medium and large non-affine deformations,
respectively.

2.4. Volume evolution and critical state behavior. A fundamental
characteristic of the pressure-shear response of glass, especially as regards
the categorization of its plastic response, concerns the evolution of volume
during shearing deformation. In order to ascertain this behavior, we deform
samples volumetrically up to a maximum pressure $p_{\text{max}}$, or preconsolidation
pressure, and subsequently unload to a lower pressure $p \leq p_{\text{max}}$, or confining
pressure. The samples are then deformed in shear at constant confining
pressure $p$.

Fig. 11, shows the evolution of the volume of the sample with shear defor-
mation at four values of confining pressure $p$ and a range of preconsolidation
pressures $p_{\text{max}} \geq p$. The striking feature in these plots is that, in all cases,
the volume of the sample attains a limiting volume, or critical state, at suf-
ficiently large shear deformation. The critical state is attained both under
compressive (positive) and tensile (negative) confining pressures. The lim-
iting volume depends on the confining pressure but is independent of the
preconsolidation pressure, Fig. 13. The calculations also show that, at the
critical state, the sample deforms at a constant shear stress that depends on
the confining pressure but is independent of the preconsolidation pressure.
Remarkably, the volume initially decreases in under-consolidated samples,
$p_{\text{max}} \lesssim 2p$, and increases in over-consolidated samples, $p_{\text{max}} \gtrsim 2p$. Similar
trends are observed in the evolution of the volumetric strain, Fig. 12.

![](./images/867762617605685352_11.jpg)

FIGURE 11. Evolution of volume during pressure-shear response
for different values of preconsolidation pressure $p_{\text{max}}$ (shown inset
in the figures) and confining pressure $p$. a) $p = -1$ GPa. b) $p = 3$
GPa. c) $p = 6$ GPa. d) $p = 9$ GPa.

![](./images/867762617605685352_12.jpg)

Figure 12. Evolution of volumetric strain during pressure-shear
response for different values of preconsolidation pressure $p_{\text{max}}$
(shown inset in the figures) and confining pressure $p$. a) $p = -1$
GPa. b) $p = 3$ GPa. c) $p = 6$ GPa. d) $p = 9$ GPa.

![](./images/867762617605685352_13.jpg)

FIGURE 13. Shear stress vs. shear strain for different values of preconsolidation pressure $p_{\text{max}}$ (shown inset in the figures) and confining pressure $p$. a) $p = -1$ GPa. b) $p = 3$ GPa. c) $p = 6$ GPa. d) $p = 9$ GPa.

## 3. MESOSCOPIC CRITICAL-STATE MODEL

The preceding MD data provides a basis for the formulation of a meso- scopic continuum model of the inelasticity of fused silica glass. In partic- ular, the attainment of a critical state in the evolution of volume under pressure-shear loading, Section 2.4, strongly suggests a representation based on critical-state theory of plasticity [30, 31]. A central tenet of critical- state theory is that a solid confined at fixed pressure attains a critical state after sufficient shear deformation beyond which subsequent plastic defor- mation occurs at constant volume and without further consolidation. In this section, we investigate the ability of critical-state theory to describe the behavior of glass gleaned from molecular dynamics.

### 3.1. Finite kinematics.
In view of the large deformations that occur over the pressure range of interest, we formulate the theory in finite kinemat- ics. We assume a standard multiplicative decomposition of the deformation gradient $\boldsymbol{F}$ of the form [40]
$$(3)\qquad \boldsymbol{F}=\boldsymbol{F}^{e} \boldsymbol{F}^{p}$$
into an elastic part $\boldsymbol{F}^{e}$ and a plastic part $\boldsymbol{F}^{p}$. We denote by $J=\operatorname{det}(\boldsymbol{F})$, $J^{e}=\operatorname{det}\left(\boldsymbol{F}^{e}\right)$ and $J^{p}=\operatorname{det}\left(\boldsymbol{F}^{p}\right)$ the corresponding Jacobians.

### 3.2. Equilibrium relations.
We further adopt a thermodynamic formal- ism [41, 42] to describe the local inelastic processes and postulate the exis- tence of a Helmholtz free energy density per unit undeformed volume of the general form
$$(4)\qquad A=W^{e}\left(\boldsymbol{C}^{e}, T\right)+W^{p}\left(. J^{p}, T\right),$$
where
$$(5)\qquad \boldsymbol{C}^{e}=\boldsymbol{F}^{e T} \boldsymbol{F}^{e}$$
is the elastic right Cauchy-Green deformation tensor, $W^{e}$ is the thermoelas tic strain energy density per unit undeformed volume and $W^{p}$ is the stored energy density per unit undeformed volume. The corresponding equilibrium relations are
$$(6a)\qquad \boldsymbol{P}=\frac{\partial W}{\partial \boldsymbol{F}}=2 \boldsymbol{F}^{e} \frac{\partial W^{e}}{\partial \boldsymbol{C}^{e}} \boldsymbol{F}^{p-T},$$

$$(6b)\qquad \boldsymbol{Y}=-\frac{\partial W}{\partial \boldsymbol{F}^{p}}=\left(\boldsymbol{C}^{e} \frac{\partial W^{e}}{\partial \boldsymbol{C}^{e}}+\frac{\partial W^{e}}{\partial \boldsymbol{C}^{e}} \boldsymbol{C}^{e}\right) \boldsymbol{F}^{p-T}-\frac{\partial W^{p}}{\partial J^{p}} J^{p} \boldsymbol{F}^{p-T},$$
where $\boldsymbol{P}$ is the first Piola-Kirchhoff stress tensor and $\boldsymbol{Y}$ is the thermody namic driving force conjugate to $\boldsymbol{F}^{p}$. We additionally assume that the elastic behavior of glass is isotropic. In particular,
$$(7)\qquad \boldsymbol{C}^{e} \frac{\partial W^{e}}{\partial \boldsymbol{C}^{e}}=\frac{\partial W^{e}}{\partial \boldsymbol{C}^{e}} \boldsymbol{C}^{e}.$$

Using this identity, the rate of dissipation evaluates to
$$(8)\qquad \boldsymbol{Y} \cdot \dot{\boldsymbol{F}}^{p}=J \boldsymbol{y} \cdot \boldsymbol{d}^{p},$$

where

$$
\boldsymbol{y}=\boldsymbol{\sigma}-p_{c} \boldsymbol{I}
$$

is a spatial driving force,

$$
\boldsymbol{d}^{p}=\frac{1}{2}\left(\boldsymbol{l}^{p}+\boldsymbol{l}^{p T}\right)=\frac{1}{2}\left(\dot{\boldsymbol{F}}^{p} \boldsymbol{F}^{p-1}+\left(\dot{\boldsymbol{F}}^{p} \boldsymbol{F}^{p-1}\right)^{T}\right)
$$

is the plastic rate of deformation tensor,

$$
J \boldsymbol{\sigma}=2 \boldsymbol{F}^{e} \frac{\partial W^{e}}{\partial \boldsymbol{C}^{e}}\left(\boldsymbol{C}^{e}, T\right) \boldsymbol{F}^{e T}
$$

is the Cauchy stress and

$$
J p_{c}=J^{p} \frac{\partial W^{p}}{\partial J^{p}}\left(J^{p}, T\right)
$$

is a critical pressure.

3.3. Flow rule. In view of the structure of the rate-of-dissipation identity (8), and following the classical kinetic theory of Onsager, we assume the existence of a dual kinetic potential $\psi^{*}(\boldsymbol{y}, J^{p})$ such that

$$
\boldsymbol{d}^{p}=\frac{\partial \psi^{*}}{\partial \boldsymbol{y}}\left(\boldsymbol{y}, J^{p}\right).
$$

We allow for a dependence of $\psi^{*}$ on $J^{p}$ in order to account for the effect of densification of the glass on its flow characteristics. We also note that objectivity, or invariance under rotations superposed on the spatial configuration, follows from the assumed isotropy of $\psi^{*}(\cdot, J^{p})$. If, in addition, we idealize the kinetics of plastic deformation as rate-independent, then $\psi^{*}(\boldsymbol{y}, J^{p})$ is the indicator function of an elastic domain $E(J^{p}) \subset \mathbb{R}_{\text {sym }}^{3 \times 3}$, i. e.,

$$
\psi^{*}\left(\boldsymbol{y}, J^{p}\right)=I_{E\left(J^{p}\right)}(\boldsymbol{y})= \begin{cases}0, & \text { if } \boldsymbol{y} \in E\left(J^{p}\right), \\ +\infty, & \text { otherwise. }\end{cases}
$$

Because of the extended character and lack of differentiability of $I_{E\left(J^{p}\right)}(\boldsymbol{y})$, the potential relation (13) needs to be understood in the sense of some appropriate notion of generalized derivative, or flow rule. If $E(J^{p})$ is convex, the appropriate generalized derivative is supplied by the set-valued subdifferential [43]

$$
\boldsymbol{d}^{p} \in\left\{\boldsymbol{r} \in \mathbb{R}_{\mathrm{sym}}^{3 \times 3} \text { s. t. }\left(\boldsymbol{y}-\boldsymbol{y}^{*}\right) \cdot \boldsymbol{r} \geq 0, \forall \boldsymbol{y}^{*} \in E\left(J^{p}\right)\right\},
$$

which embodies Drucker's principle of maximum dissipation, which underlies the classical theory plasticity [44].

3.4. Calibration from MD data. We proceed to use the data mined from MD, Section 2, to specialize the general framework just outlined to fused silica glass and calibrate the resulting model.

3.4.1. Elasticity. For definiteness, we consider elastic strain-energy densities
of the neo-Hookean form

$$
(16)\qquad W^{e}\left(\boldsymbol{C}^{e}\right)=\frac{\mu\left(J^{e}\right)}{2}\left(J^{e-2 / 3} \operatorname{tr}\left(\boldsymbol{C}^{e}\right)-3\right)+f\left(J^{e}\right),
$$

where $\mu(J^{e})$ is a volume-dependent shear modulus and $f(J^{e})$ defines the
volumetric equation of state. The Cauchy stress follows from (16) as

$$
(17)\qquad \begin{aligned}
J \boldsymbol{\sigma}=2 \boldsymbol{F}^{e} \frac{\partial W^{e}}{\partial \boldsymbol{C}^{e}} \boldsymbol{F}^{e T} & =\left(\frac{1}{2} \mu^{\prime}\left(J^{e}\right)\left(J^{e-2 / 3} \operatorname{tr}\left(\boldsymbol{B}^{e}\right)-3\right)+f^{\prime}\left(J^{e}\right)\right) J^{e} \boldsymbol{I} \\
& +\mu\left(J^{e}\right)\left(J^{e-2 / 3} \boldsymbol{B}^{e}-\frac{1}{3} J^{e-2 / 3} \operatorname{tr}\left(\boldsymbol{B}^{e}\right) \boldsymbol{I}\right),
\end{aligned}
$$

where

$$
(18)\qquad \boldsymbol{B}^{e}=\boldsymbol{F}^{e} \boldsymbol{F}^{e T}
$$

is the elastic left Cauchy-Green deformation tensor.

![](./images/867762617605685352_14.jpg)

FIGURE 14. Volumetric MD data during monotonic compressive
loading. a) Total volumetric Jacobian $J$ vs. elastic Jacobian $J^{e}$
as deduced from unloading, showing two phases (dense and loose)
separated by a densification phase transition. b) Shear modulus $\mu$
vs. $J^{e}$ and fit of each of the phases.

The molecular dynamics data suggests a densification phase transition
when the plastic volumetric deformation attains a critical value of $J^{p} = J_c^p \approx 0.9$, Fig. 14a. We therefore regard glass as a two-phase material and
describe the elasticity of each phase by means of an elastic strain-energy
density of the form (16). Specializing (17) to simple elastic shear following
a volumetric plastic deformation gives

$$
(19)\qquad J \sigma_{12}=\mu\left(J^{e}\right) \gamma,
$$

in axes aligned with the shearing directions and with $\gamma$ denoting the shear
strain. Using this relation in combination with the MD data in Fig. 9a gives

the $\mu$ vs. $J^e$ data shown in Fig. 14b. For definiteness, we fit these data by functions of the form

$$
(20) \quad \mu\left(J^{e}\right)= \begin{cases}a_{0}+a_{1} J^{e}+a_{2} J^{e^{2}}, & J^{e} \geq J_{c}^{p}, \\ b_{1} \exp \left(b_{2}\left(J^{e}-1\right)\right)+b_{3}, & \text { otherwise },\end{cases}
$$

and obtain the coefficients tabulated in Table 1. The goodness of the fit is shown in Fig. 14b. The two-phase structure of the equation of state is also clear from the figure.

TABLE 1. Pressure-dependent shear-modulus parameters

<table>
<thead>
<tr>
<th>$a_0$</th>
<th>$a_1$</th>
<th>$a_2$</th>
<th>$b_1$</th>
<th>$b_2$</th>
<th>$b_3$</th>
</tr>
</thead>
<tbody>
<tr>
<td>347.15 GPa</td>
<td>-745.82 GPa</td>
<td>426.46 GPa</td>
<td>0.20773 GPa</td>
<td>-19.498</td>
<td>34.6439 GPa</td>
</tr>
</tbody>
</table>

![](./images/867762617605685352_15.jpg)

FIGURE 15. Consolidation MD data during monotonic compressive loading. a) Pressure $p$ vs. elastic Jacobian $J^e$ and fits for dense and loose phases. b) Preconsolidation pressure $p_c$ on permanent densification $1-J^p$ and fit.

Next, we determine the equation-of-state function $f(J^e)$ in eq. (16) by examining the case of pure elastic compression. Specializing (17) to this case, we obtain the relation

$$
(21) \quad-J p=f^{\prime}\left(J^{e}\right) J^{e}.
$$

In this particular case, the MD data of Fig. 5 reduces to Fig. 15a. We fit these data by functions of the form

$$
(22) \quad f\left(J^{e}\right)= \begin{cases}\frac{c}{2}\left(J^{e}-1\right)^{2}, & J^{p} \geq J_{c}^{p}, \\ \frac{d_{1}}{2}\left(J^{e}-1\right)^{2}+\frac{d_{2}}{4}\left(J^{e}-1\right)^{4}, & \text { otherwise },\end{cases}
$$

and obtain the coefficients tabulated in Table 2. The goodness of the fit is also shown in Fig. 14b.

TABLE 2. Volumetric elastic-energy dependence

<table>
<thead>
<tr>
<th>c</th>
<th>$d_1$</th>
<th>$d_2$</th>
</tr>
</thead>
<tbody>
<tr>
<td>-33.75 GPa</td>
<td>-25.167 GPa</td>
<td>-1879.69 GPa</td>
</tr>
</tbody>
</table>

![](./images/867762617605685352_16.jpg)

FIGURE 16. a) Schematic of elastic domain in the $(p,q)$-plane,
where $p$ denotes the pressure, $q$ the Mises effective shear stress,
$p_t$ the tensile failure pressure, $p_c$ the compressive yield pressure
and $q_c$ the shear yield strength. The dash-dot line represents the
critical-state line. b) Stress path for pressure-shear test (vertical
line at $p$) and directions of plastic deformation rate (arrows) in the
over-consolidated case, labeled OC, and under-consolidated case,
labeled UC.

3.4.2. Elastic domain and yield surface. Under the assumption of rate in-
dependence, we model the yield-behavior of glass by means of the elliptic
elastic domain

$$
(23)\quad E(J^p)=\left\{\boldsymbol{y}\in\mathbb{R}_{\mathrm{sym}}^{3\times3},\ \left(\frac{q}{q_c(J^p)}\right)^2+\left(\frac{p-(p_c(J^p)+p_t)/2}{(p_c(J^p)+p_t)/2}\right)^2\leq1\right\},
$$

where

$$
(24)\quad q=\sqrt{\frac{1}{2}\boldsymbol{s}\cdot\boldsymbol{s}}
$$

is the Mises effective shear stress,

$$
(25)\quad \boldsymbol{s}=\boldsymbol{\sigma}-\frac{1}{3}\mathrm{tr}(\boldsymbol{\sigma})\boldsymbol{I}=\boldsymbol{y}-\frac{1}{3}\mathrm{tr}(\boldsymbol{y})\boldsymbol{I}
$$

is the stress deviator, $p_t$ is the tensile failure pressure, $p_c$ is the compressive
yield pressure, $q_c$ is the shear yield strength and $J^p$ plays the role of an
internal variable, cf. Fig. 16a. Elastic domains of the type (23) have been
used in connection to Cam-Clay models of granular media (cf., e. g., [45]) and
glasses [46, 47, 27]. The function $p_c(J^p)$ defines the consolidation relation.
The curve in the $(p,q)$-plane

$$
(26)\quad q_c=g(p_m),
$$


with

$$
(27) \qquad p_{m}=\frac{p_{t}+p_{c}}{2}
$$

may be obtained by eliminating $J^{p}$ between $q_{c}(J^{p})$ and $p_{c}(J^{p})$. Evidently, $p_{m}$ is the pressure at which $q$ attains its maximum value $q_{c}$ on the yield surface $\partial E(J^{p})$, cf. eq. (23), and at which, by the flow rule (15), the plastic strain rate is volume preserving. Thus, the relation (26) represents the critical state line in the $(p,q)$-plane.

3.4.3. Consolidation curve. We proceed to identify the consolidation curve $p_{c}(J^{p})$ for fused silica from the MD data shown in Fig. 5. To this end, we identify $J^{p}$ as the volumetric deformation upon unloading and the corresponding $p_{c}(J^{p})$ as the maximum pressure attained during loading. The resulting data are shown in Fig. 14b. We fit these data by means of a power-law relation of the form

$$
(28) \qquad p_{c}=p_{0}+\frac{A}{\alpha}(1-J^{p-\alpha}),
$$

previously used by Becker [48] as a volumetric equation of state. In addition, we identify the tensile failure stress $p_{t}$ from MD calculations as the maximum tensile pressure at which the glass sample is stable. The resulting values of the constants are tabulated in Table 3. The goodness of the fit is shown in Fig. 14b.

<p><b>Table 3.</b> Hardening parameters</p>

<table>
<thead>
<tr>
<th>$A$</th>
<th>$\alpha$</th>
<th>$p_{0}$</th>
<th>$p_{t}$</th>
</tr>
</thead>
<tbody>
<tr>
<td>$8.48613$ GPa</td>
<td>$9.2689$</td>
<td>$3.02934$ GPa</td>
<td>$-10$ GPa</td>
</tr>
</tbody>
</table>

3.4.4. Evolution towards the critical state. We verify that a simple elastic domain of the form (23) and the consolidation curve (28) are indeed capable of representing the complex yield and flow behavior revealed by the pressure-shear MD data collected in Section 2.3. Thus, consider a pressure-shear test at confining pressure $p$ and effective shear stress $q$ increasing monotonically from zero. The corresponding loading path is shown as a vertical line at $p$ in Fig. 16b. The intermediate ellipse in the figure corresponds to the critical state that is eventually attained along the loading path. The figure also depicts two cases, labeled 'under-consolidated' (UC) and 'over-consolidated' (OC). In the under-consolidated case, $p$ lies to right of the initial value of $p_{m}$, resulting in a plastic strain rate $\boldsymbol{d}^{p}$ (shown as an arrow in the figure) with a negative, or compressive, volumetric component, $\text{tr}(\boldsymbol{d}^{p})<0$. $^{1}$ By contrast, in the over-consolidated case, $p$ lies to left of the initial value of

$^{1}$We recall that, under the pressure sign convention $p=-\text{tr}(\boldsymbol{\sigma})$, a positive (negative) component of the normal to the yield surface in the $(p,q)$-plane corresponds to a negative (positive), or compressive (tensile), volumetric plastic strain, $\text{tr}(\boldsymbol{d}^{p})<0$ ($\text{tr}(\boldsymbol{d}^{p})>0$).

$p_m$, resulting in a plastic strain rate $\boldsymbol{d}^p$ (also shown as an arrow in the figure) with a positive, or tensile, volumetric component, $\operatorname{tr}(\boldsymbol{d}^p) > 0$. It thus follows that under-consolidated samples are predicted to decrease their volume, whereas over-consolidated samples are predicted to increase their volume, in accord with the MD data in Fig. 12. From relation (10), it follows that

$$(29) \qquad \dot{J}^p = J^p \operatorname{tr}(\boldsymbol{d}^p),$$

and from the monotonicity of the consolidation curve, Fig. 14b, it follows that $p_c$ increases in the under-consolidated case and decreases in the over-consolidated case. Thus, in both cases the yield surface converges towards the critical-state yield surface, as required. We also note that, following the attainment of the critical state, represented by the intermediate ellipse in Fig. 17b, both the sample volume and the shear stress remain constant, in agreement with the MD data collected in Fig. 12 and Fig. 13. We therefore conclude that the MD data for fused silica presented in Section 2 is indicative of—and well-represented by—critical state theory of plasticity.

![](./images/867762617605685352_17.jpg)

FIGURE 17. a) Critical state line MD data (dots) and fits. The dash line is the fit in the compressive regime and the dash-dot line is the fit in the tensile regime. b) Critical state line (solid curve) obtained by intersecting the compressive and tensile critical state lines. The dash line represents a typical elastic domain.

3.4.5. The anomalous critical-state line of fused silica. In order to close the model, the critical state line (26) remains to be identified. We determine the critical state line, eq. (26), from the MD simulations described in Section 2.3, by identifying $p_m$ with the confining pressure applied to the sample and the corresponding $q_c$ with the shear stress upon the attainment of the critical state of constant volume.

The data thus obtained is shown in Fig. 17a. The critical-state line thus determined exhibits two clear regimes, one under predominantly compressive

pressures and another under predominantly tensile pressures. Remarkably,
in the tensile regime the critical-state line increases with increasing tensile
pressure, which represents anomalous behavior. By contrast, in the com-
pressive regime the critical-state line increases with increasing compressive
pressure, or confinement, as expected.

The tensile regime of the critical-state line is well-represented by a linear
relation of the form

$$
(30) \quad q=\frac{p_{1}-p}{p_{1}-p_{t}} q_{t},
$$

capped vertically at $p=p_{t}$. The compressive regime of the critical-state line
is in turn well-presented by a power law of the form

$$
(31) \quad q=B p^{\beta}.
$$

The resulting values of the constants are tabulated in Table 4. The goodness
of the fit is shown in Fig. 17a.

TABLE 4. Critical state line constants

<table>
<thead>
<tr>
<th>$p_{1}$</th>
<th>$q_{t}$</th>
<th>$p_{t}$</th>
<th>$B$</th>
<th>$\beta$</th>
</tr>
</thead>
<tbody>
<tr>
<td>12.337 GPa</td>
<td>7.402 GPa</td>
<td>$-8.5$ GPa</td>
<td>$1.168\sqrt{\text{GPa}}$</td>
<td>0.5</td>
</tr>
</tbody>
</table>

The anomalous yield behavior of fused silica under predominantly tensile
pressures uncovered by the MD data is indeed consistent with the experi-
mental data of Meade and Jeanloz [2] noted in the introduction, Fig. 1b, who
attributed the anomaly to changes in coordination at the atomic level. In-
terestingly, Meade and Jeanloz [2] observe an additional region of anomalous
shear yield strength behavior at pressures above 30 GPa, not captured by
the present MD calculations. Likely causes of this discrepancy are the large
disparity in strain rates between the work of Meade and Jeanloz [2], which
was performed at quasi-static loading rates, and the present calculations,
which entail large rates of deformation, and possible inadequacies of the
interatomic potentials at extremely large pressures and volume reductions.

The intersection of the tensile and compressive critical state lines, eq. (30)
and (31), respectively, results in a non-convex combined critical-state line,
Fig. 17b. The figure reveals that fused silica is doubly anomalous, on ac-
count of the anomalous dependence of the its shear modulus of volumetric
deformation, and of the strong non-convexity of its critical-state line.

## 4. MICROSTRUCTURE, RELAXATION AND DIV-QUASICONVEXIFICATION

We now proceed to show that the strongly non-convex critical-state line
in Fig. 17b is, in fact, unstable with respect to microstructure formation and
that consideration of microstructure results in a stable, or relaxed, critical-
state line that captures the fine structure of the MD data at the tensile-to-
compressive transition. We recall that, as noted in the introduction, several

authors [20, 28] have performed molecular dynamics calculations on amor-
phous solids deforming under shear and found that the resulting deforma-
tion field develops fine microstructure in order to accommodate permanent
macroscopic deformations, Fig. 2. In this section, we appeal to notions from
the Direct Methods in the Calculus of Variations in order establish a con-
nection between the strong non-convexity of the critical-state line and the
development of fine microstructure, and to characterize explicitly and ex-
actly the effective or relaxed behavior at the macroscale. For completeness,
a summary of the main mathematical concepts and arguments is consigned
to the Appendix. A full mathematical account may be found in the article
of Conti et al. [49].

We carry out the analysis within the framework of limit analysis [44].
Thus, we assume that the solid is at collapse, i. e., it deforms plastically at
constant applied load. Under these conditions, the instantaneous behavior
of the solid is rigid and ideally plastic, i. e., no instantaneous hardening
takes place (ideal plasticity) and (rigid-plastic behavior)

$$
(32) \quad \boldsymbol{d}^{p}=\frac{1}{2}\left(\nabla \boldsymbol{v}+\nabla \boldsymbol{v}^{T}\right) \equiv \boldsymbol{e}(\boldsymbol{v}),
$$

where $\boldsymbol{v}: \Omega \to \mathbb{R}^{3}$ is the velocity field at collapse, or collapse mode, and
$\Omega$ is the domain of the solid at collapse. The corresponding kinematic and
static problems of limit analysis [44] can then be jointly expressed as the
saddle-point problem

$$
(33) \quad \inf _{\boldsymbol{v}} \sup _{\boldsymbol{\sigma}}\left\{\int_{\Omega} \boldsymbol{\sigma} \cdot \nabla \boldsymbol{v} d x: \boldsymbol{\sigma}(x) \in E\left(J^{p}(x)\right), \boldsymbol{v}=\boldsymbol{g} \text { on } \partial \Omega\right\},
$$

where the minimization and maximization take place over suitable spaces of
velocities and stresses, respectively, $J^{p}$ accounts for the state of consolida-
tion of the solid, $\boldsymbol{g}$ is a prescribed velocity field over the boundary and we
assume that the solid is free of body forces. We recall that the inner maxi-
mum problem in (33) embodies Drucker's principle of maximum dissipation
and the static principle of classical plasticity, whereas the outer minimum
problem embodies the kinematic principle of classical plasticity.

We further note that, for a solid obeying critical-state theory of plasticity,
instantaneous rigid-ideally plastic behavior implies, in particular, instanta-
neous constancy of volume, which in turn requires that the solid be either
locally rigid or at critical state. This condition sets the requirement that
$\boldsymbol{\sigma}(x) \in K$ a. e. in $\Omega$, where $K$ is the domain bounded by the critical-state
line. Since the critical-state line is the locus of points in stress space at which
material behavior is ideally plastic, $K$ may be regarded as a limit domain
in the sense of hardening plasticity (cf., e. g., [50] for a lucid introduction to
limit surfaces in hardening plasticity). Thus, at collapse (33) specializes to

$$
(34) \quad \inf _{\boldsymbol{v}} \sup _{\boldsymbol{\sigma}}\left\{\int_{\Omega} \boldsymbol{\sigma} \cdot \nabla \boldsymbol{v} d x: \boldsymbol{\sigma}(x) \in K, \boldsymbol{v}=\boldsymbol{g} \text { on } \partial \Omega\right\},
$$

The maximization with respect $\boldsymbol{\sigma}$ may be effected pointwise, whereupon the problem (34) reduces to the kinematic problem
$$
(35) \quad \inf _{\boldsymbol{v}}\left\{\int_{\Omega} \phi(\boldsymbol{e}(\boldsymbol{v})) d x: \quad \boldsymbol{v}=\boldsymbol{g} \text { on } \partial \Omega\right\},
$$
where
$$
(36) \quad \phi\left(\boldsymbol{d}^{p}\right)=\sup _{\boldsymbol{\sigma} \in K} \boldsymbol{\sigma} \cdot \boldsymbol{d}^{p}
$$
is the limit plastic dissipation potential.

This classical theory of limit analysis is mathematically well-developed provided that the limit domain $K$ is convex, in which case no microstructure occurs. In order extend the theory to non-convex domains and microstruc- ture formation, we reformulate the saddle-point problem (34) as
$$
(37) \quad \sup _{\boldsymbol{\sigma}} \inf _{\boldsymbol{v}}\left\{\int_{\Omega} \boldsymbol{\sigma} \cdot \nabla \boldsymbol{v} d x: \boldsymbol{\sigma} \in K, \boldsymbol{v}=\boldsymbol{g} \text { on } \partial \Omega\right\},
$$
where we have simply inverted the order of the maximum and minimum problems. We recall that, in the convex case, problems (37) and (34) are equivalent by the inf-sup theorem [51], but not so in the non-convex case. An integration by parts gives (37) in the equivalent form
$$
(38) \quad \sup _{\boldsymbol{\sigma}} \inf _{\boldsymbol{v}}\left\{\int_{\partial \Omega} \boldsymbol{\sigma} \boldsymbol{\nu} \cdot \boldsymbol{g} d \mathcal{H}^{2}-\int_{\Omega} \operatorname{div} \boldsymbol{\sigma} \cdot \boldsymbol{v} d x: \boldsymbol{\sigma} \in K, \boldsymbol{v}=\boldsymbol{g} \text { on } \partial \Omega\right\},
$$
where $d \mathcal{H}^{2}$ denotes the element of area on the boundary $\partial \Omega$. Evidently, for the supremum to be non-trivial we must have $\operatorname{div} \boldsymbol{\sigma}=\mathbf{0}$, i. e., the stress field must be in equilibrium, whereupon (38) reduces to the static problem
$$
(39) \quad \sup _{\boldsymbol{\sigma}}\left\{\int_{\partial \Omega} \boldsymbol{\sigma} \boldsymbol{\nu} \cdot \boldsymbol{g} d \mathcal{H}^{2}: \boldsymbol{\sigma} \in K, \operatorname{div} \boldsymbol{\sigma}=\mathbf{0}\right\}.
$$

The question of existence of solutions of problem (39) may be ascertained by recourse to the direct method of the Calculus of Variations [29]. Exis- tence of solutions is indicative of stability of the material with respect to microstructure. Stability in turn necessitates some appropriate notion of convexity to be satisfied by the limit domain $K$. In the present setting, the appropriate notion is symmetric div-quasiconvexity [52, 49], cf. Appendix A, a notion of convexity in symmetric stress space that accounts for the equilibrium constraint $\operatorname{div} \boldsymbol{\sigma}=\mathbf{0}$.

Equally as important as establishing existence is the treatment of cases that depart from the preceding program, specifically, solids for which $K$ fails to be symmetric div-quasiconvex. In such cases, the supremum in (39) may be attained arbitrarily closely by weakly-convergent sequences of stress fields, but the supremum itself may not be attained by any one stress field. The weakly-convergent maximizing sequences are typically characterized by increasingly fine microstructure, a situation reminiscent of the fine patterns computed by [20]. The weak limits of the maximizing sequences can then be identified as the macroscopically observable, or average, stress fields.

The problem is, then, to characterize all macroscopic stress fields that are attainable as weak limits of sequences of maximizing microscopic stress-field sequences. This characterization determines the effective yield behavior of the solid at the macroscale.

Based on standard theory [29] we expect that the macroscopic states thus defined satisfy the relaxed problem

$$
(40) \quad \sup _{\boldsymbol{\sigma}}\left\{\int_{\partial \Omega} \boldsymbol{\sigma} \boldsymbol{\nu} \cdot \boldsymbol{g} d \mathcal{H}^{2}: \boldsymbol{\sigma} \in \bar{K}, \operatorname{div} \boldsymbol{\sigma}=0\right\},
$$

for some effective limit domain $\bar{K}$. Evidently, $\bar{K}$ must contain $K$ and be symmetric div-quasiconvex in order for the supremum of the effective problem (40) to be attained. In addition, $\bar{K}$ must be as small as possible in order for the solutions of the effective problem (40) to be weak limits of maximizing sequences of the unrelaxed problem (39). These constraints identify $\bar{K}$ as the symmetric div-quasiconvex envelope of $K$, and can be visualized as the smallest symmetric div-quasiconvex set containing $K$.

The remaining problem of interest is to determine the symmetric div-quasiconvex envelope $\bar{K}$ of the limit surface of fused silica, eqs. (30) and (31), Fig. 17. An explicit and exact construction of $\bar{K}$ has been derived by Conti et al. [49]. They show that the curves

$$
(41) \quad q=\left(s+\frac{3}{4}(p-r)^{2}\right)^{1 / 2}
$$

in $(p, q)$-plane represent rank-2 connections between states of constant stress in traction equilibrium, and that the curves bound symmetric div-quasiconvex sets in the $(p, q)$-plane. Evidently, the smallest such set containing $K$, or rank-2 envelope of $K$, contains $\bar{K}$. The mathematical challenge is to show that the rank-2 envelope of $K$ is in fact $\bar{K}$. This equivalence has been proven by Conti et al. [49].

Specifically, the rank-2 envelope of the limit domain $K$ for fused silica is obtained by fitting a curve of the form (41) so as to smooth out the transition between the tensile and compressive regimes of the critical-state line. The conditions that determine the extreme rank-2 connection are

$$
(42a) \quad q_{t}^{2}=s+\frac{3}{4}\left(p_{t}-r\right)^{2},
$$

$$
(42b) \quad q^{2}=s+\frac{3}{4}(p-r)^{2},
$$

$$
(42c) \quad q=B p^{\beta},
$$

$$
(42d) \quad \beta B p^{\beta-1}=\frac{1}{q} \frac{3}{4}(p-r),
$$

to be solved for $r, s, p$ and $q$. The values of these variables computed from Tables 3 and 4 are shown in Table 5.

The resulting envelope is shown in Fig. 18a. It bears emphasis that the relaxed limit domain $\bar{K}$ is not convex, which illustrates the fact that symmetric div-quasiconvex sets are a strictly larger class than convex sets. We

<table>
<caption>Table 5. The rank-2 envelope of fused silica glass.</caption>
<thead>
<tr>
<th>$r$</th>
<th>$s$</th>
<th>$p_{\text{min}}$</th>
<th>$p_{\text{max}}$</th>
</tr>
</thead>
<tbody>
<tr>
<td>5.176 GPa</td>
<td>7.674 GPa²</td>
<td>4.141 GPa</td>
<td>6.084 GPa</td>
</tr>
</tbody>
</table>

![](./images/867762617605685352_18.jpg)

FIGURE 18. a) Relaxed critical-state line showing rank-2 connection envelope (dash line). b) Rank-2 connection captures the fine structure of the MD data at the tension-to-compression transition point.

also note that $\bar{K} \neq K$, which shows that, indeed, $K$ is not symmetric div-quasiconvex, or stable against microstructure, as surmised. Fig. 18b shows the rank-2 connection curve in isolation together with the MD data. The comparison suggests that the rank-2 envelope construction indeed captures the fine structure of the MD data at the tension-to-compression transition point, which, in hindsight, the unrelaxed model in Fig. 17 fails to do. Conversely, we conclude that the fine structure of the MD data at the tension-to-compression transition point is the result of accommodation at the microstructural level.

## 5. SUMMARY AND CONCLUDING REMARKS

We have developed a critical-state model of fused silica plasticity on the basis of data mined from Molecular Dynamics (MD) calculations. The MD data is suggestive of an irreversible densification transition in volumetric compression resulting in permanent, or plastic, densification upon unloading. The MD data also reveals an evolution towards a critical state of constant volume under pressure-shear deformation. The trend towards constant volume is from above, when the glass is overconsolidated, or from below, when it is underconsolidated. We have shown that these characteristic behaviors are well-captured by a critical-state model of plasticity, where the densification law for glass takes the place of the classical consolidation

law of granular media and the locus of constant-volume states defines the critical-state line.

A salient feature of the critical-state line of fused silica, as identified from MD data, that renders its yield behavior anomalous—and raises it from the commonplace—is that it is strongly non-convex, owing to the existence of two well-differentiated phases, at low and high pressures. This anomalous yield strength of fused silica is indeed consistent with—and born out by—the measurements of [2]. The strong non-convexity of yield in turn explains the patterning observed by [20] in molecular dynamics calculations of amorphous solids deforming in shear.

The proclivity of fused silica for patterning at the microscale raises the question of its effective behavior at the macroscale, i. e., the average stress and deformation conditions that are attainable when microstructure is ac- counted for. Remarkably, this question can be rigorously and exactly as- certained for fused silica within the framework of limit analysis and the calculus of variations [49]. We recall that stress solutions of the static prob- lem of limit analysis are subject to an equilibrium, or divergence, constraint. The problem is, therefore, to determine all macroscopic states of stress at- tainable as averages of microscopic stress fields that are within yield and at equilibrium. Conti et al. [49] have shown that the effective or macro- scopic critical-state line thus defined can be computed explicitly and exactly through a rank-2 envelope construction in the $(p,q)$-plane. This remarkable result effectively upscales the microscopic critical state model delineated by the MD data to the macroscale. The rank-2 envelope indeed captures the fine structure of the critical-state line, as gleaned from MD data, at the tension-to-compression transition, which further underscores the impor- tance of microstructure in shaping the macroscopic, or effective, behavior of fused silica. The effective or macroscopic model of fused silica is stable with respect to microstructure, defines well-posed boundary-value problems and is, therefore, suitable for use in large-scale continuum calculations.

## ACKNOWLEDGEMENTS

WS, SH and MO gratefully acknowledge support from the US Office of Naval Research through grant N000141512453. SC is grateful for the support of the Deutsche Forschungsgemeinschaft through the Sonderforschungsbere- ich 1060 "The mathematics of emergent effects".

## APPENDIX A. RELAXATION OF THE LIMIT-ANALYSIS PROBLEM

For completeness, we summarize the main concepts and arguments lead- ing to the computation of the relaxed critical-state line and limit domain $\bar{K}$. Further mathematical details may be found in the article of [49].

We begin by introducing the dissipation functional $F: L^\infty(\Omega, \mathbb{R}_{\mathrm{sym}}^{3 \times 3}, \mathrm{div})$ $\to \overline{\mathbb{R}}$ defined as

$$
(43) \quad F(\boldsymbol{\sigma})= \begin{cases}\int_{\partial \Omega} \boldsymbol{\sigma} \boldsymbol{\nu} \cdot \boldsymbol{g} d \mathcal{H}^{2}, & \text { if } \boldsymbol{\sigma} \in K \text { almost everywhere in } \Omega, \\ -\infty, & \text { otherwise },\end{cases}
$$

where $L^\infty(\Omega, \mathbb{R}_{\mathrm{sym}}^{3 \times 3}, \mathrm{div})$ is the space of essentially bounded stress fields over $\Omega$ with zero distributional divergence endowed with its weak* topology and we assume $\Omega$ to be Lipschitz and bounded. Then, problem (39) is equivalent to

$$
(44) \quad \sup _{\boldsymbol{\sigma} \in L^{\infty}\left(\Omega, \mathbb{R}_{\mathrm{sym}}^{3 \times 3}, \mathrm{div}\right)} F(\boldsymbol{\sigma}).
$$

The question of existence of solutions of problem (44) may be ascertained by recourse to the direct method of the Calculus of Variations [29]. Thus, if $K$ is bounded the functional $F$ is clearly weakly coercive in $L^\infty(\Omega, \mathbb{R}_{\mathrm{sym}}^{3 \times 3}, \mathrm{div})$. In addition, if $\boldsymbol{g} \in L^{1}(\partial \Omega, \mathbb{R}^{3})$, the space of integrable velocity fields over $\partial \Omega$, then the dissipation function

$$
(45) \quad D(\boldsymbol{\sigma})=\int_{\partial \Omega} \boldsymbol{\sigma} \boldsymbol{\nu} \cdot \boldsymbol{g} d \mathcal{H}^{2}
$$

is weakly continuous in $L^\infty(\Omega, \mathbb{R}_{\mathrm{sym}}^{3 \times 3}, \mathrm{div})$ by the trace theorem for $W^{1,1}(\Omega, \mathbb{R}^{3})$ (cf., e. g., [53], p. 168).

In order to apply Tonelli's theorem [54], there remains to identify conditions under which $F$ is upper-semicontinuous on $L^\infty(\Omega, \mathbb{R}_{\mathrm{sym}}^{3 \times 3}, \mathrm{div})$. We recall that $F$ is upper-semicontinuous if $\limsup _{h \to \infty} F(\boldsymbol{\sigma}_{h}) \leq F(\boldsymbol{\sigma})$ for every $\boldsymbol{\sigma} \in L^\infty(\Omega, \mathbb{R}_{\mathrm{sym}}^{3 \times 3}, \mathrm{div})$ and every sequence $(\boldsymbol{\sigma}_{h})$ converging weak* to $\boldsymbol{\sigma}$ in $L^\infty(\Omega, \mathbb{R}_{\mathrm{sym}}^{3 \times 3}, \mathrm{div})$. We expect upper-semicontinuity to necessitate some appropriate notion of convexity of $K$. The appropriate notion is symmetric div-quasiconvexity, which is a special case of $\mathcal{A}$-quasiconvexity, see [52] and [49] for the mathematical treatment.

Definition A.1 (Symmetric div-quasiconvex function). A function $f: \mathbb{R}_{\mathrm{sym}}^{3 \times 3} \to$ $\overline{\mathbb{R}}$ is symmetric div-quasiconvex if

$$
(46) \quad f(\boldsymbol{\sigma}) \leq \int_{(0,1)^{3}} f(\boldsymbol{\sigma}+\boldsymbol{\xi}) d x,
$$

for all $\boldsymbol{\sigma} \in \mathbb{R}_{\mathrm{sym}}^{3 \times 3}$ and all $\boldsymbol{\xi} \in C_{\mathrm{per}}^{\infty}\left([0,1]^{3}, \mathbb{R}_{\mathrm{sym}}^{3 \times 3}\right)$ such that $\operatorname{div} \boldsymbol{\xi}=\mathbf{0}$ and $\int_{(0,1)^{3}} \boldsymbol{\xi} d x=\mathbf{0}$.

This notion of convexity may be transferred to sets.

Definition A.2 (Symmetric div-quasiconvex set). A compact set $K \subset \mathbb{R}_{\mathrm{sym}}^{3 \times 3}$ is symmetric div-quasiconvex if there is a symmetric div-quasiconvex function $g \in C^{0}\left(\mathbb{R}_{\mathrm{sym}}^{3 \times 3} ;[0, \infty)\right)$ such that $K=\{\boldsymbol{\sigma}: g(\boldsymbol{\sigma})=0\}$.

Evidently, every convex function, respectively convex set, is a symmetric div-quasiconvex function, respectively symmetric div-quasiconvex set, but

the converse, as we shall see, is not true. The relevance of symmetric div- quasi-convexity to problem (44) stems from the following connection.

Theorem A.3 (div-quasiconvexity and upper-semicontinuity). Suppose that the compact set $K \subset \mathbb{R}_{\text {sym }}^{3 × 3}$ is symmetric div-quasiconvex. Then, the func tional (43) is weak* upper semicontinuous in $L^{\infty}(\Omega, \mathbb{R}_{sym}^{3 × 3}, div)$ .

This theorem is in the spirit of the classical theorems of Morrey [55], which put forth a equivalence between quasiconvexity and lower-semicontinuity of energy functionals. The proof of the theorem is based on the results of Fonseca and Müller [52] and may be found in [49]. Existence then follows from an application of Tonelli's theorem [54].

Theorem A.4 (Existence). Let $\Omega \subset \mathbb{R}^{3}$ be bounded and Lipschitz. Sup pose that $K \subset \mathbb{R}_{sym}^{3 × 3}$ is a nonempty compact symmetric div-quasiconvex set. Let $g \in L^{1}(\partial \Omega, \mathbb{R}^{3})$ . Then, the static problem (44) of limit analysis has solutions.

Suppose now that $K$ fails to be symmetric div-quasiconvex. Based on standard theory [29] we expect that the weak limits of maximizing se quences, representing the macroscopic states of solids with increasingly fine microstructure, satisfy the relaxed problem

$$
\text { (47) } \sup _{\boldsymbol{\sigma} \in L^{\infty}\left(\Omega, \mathbb{R}_{\text {sym }}^{3 × 3}, \operatorname{div}\right)} \overline{F}(\boldsymbol{\sigma}),
$$

where the relaxed functional $\bar{F}: L^{\infty}(\Omega, \mathbb{R}_{sym}^{3 × 3}$ , div $) \to \overline{\mathbb{R}}$ has the form

$$
\text { (48) } \quad \overline{F}(\boldsymbol{\sigma})= \begin{cases}\int_{\partial \Omega} \boldsymbol{\sigma} \boldsymbol{\nu} \cdot \boldsymbol{g} d \mathcal{H}^{2}, & \text { if } \boldsymbol{\sigma} \in \overline{K} \text { almost everywhere in } \Omega, \\ -\infty, & \text { otherwise },\end{cases}
$$

for some effective limit domain $\bar{K}$ . Evidently, $\bar{K}$ must contain $K$ and be symmetric div-quasiconvex in order for $\bar{F}$ to be upper-semicontinuous and the supremum in the effective problem (47) to be attained. In addition, $\bar{K}$ must be as small as possible in order for the solutions of the effective problem (47) to be weak limits of maximizing sequences of the unrelaxed problem (44). These constraints lead to the following notion of envelope.

Definition A.5 (Symmetric div-quasiconvex envelope). The symmetric div quasiconvex envelope of a compact set $K \subset \mathbb{R}_{sym}^{3 × 3}$ is the set

$$
\begin{aligned}
& \text { (49) } \quad \overline{K}=\left\{\boldsymbol{\sigma} \in \mathbb{R}_{\text {sym }}^{3 × 3}: g(\boldsymbol{\sigma}) \leq \max g(K)\right. \\
& \text { for all symmetric div-quasiconvex } \left.g \in C^{0}\left(\mathbb{R}_{\text {sym }}^{3 × 3} ;[0, \infty)\right)\right\} \text {. }
\end{aligned}
$$

The remaining problem of interest is to determine the symmetric div quasiconvex envelope $\bar{K}$ of sets $K$ in the $(p, q)$ -plane. For sets of a specific form, a construction of $\bar{K}$ has been put forth by [49]. Here we limit ourselves to summarizing the main arguments and refer the interested reader to [49] for mathematical details.

A main building block of the explicit construction of $\bar{K}$ is the following classical result of [56].

Theorem A.6 (Tartar'85). The function $f(\boldsymbol{\sigma})=2|\boldsymbol{\sigma}|^{2}-\operatorname{tr}(\boldsymbol{\sigma})^{2}$ is symmetric div-quasiconvex.

We recall that the critical-state surface of fused silica is isotropic and is defined by its trace, or critical-state line, on the $(p, q)$-plane. From Tartar's theorem A.6, [49] show the following.

Theorem A.7. The set $\left\{\boldsymbol{\sigma} \in \mathbb{R}_{\mathrm{sym}}^{3 \times 3}: q^{2} \leq s+\frac{3}{4}(p-r)^{2}\right\}$, with $r, s \in \mathbb{R}$, is symmetric div-quasiconvex.

The curves $q=\left(s+\frac{3}{4}(p-r)^{2}\right)^{1 / 2}$ in $(p, q)$-plane represent rank-2 connections, or connections between stress states in equilibrium. By theorem A.7, the curves bound symmetric div-quasiconvex sets in the $(p, q)$-plane. Therefore, the smallest such set containing $K$, or rank-2 envelope of $K$, contains $\bar{K}$. [49] show that the rank-2 envelope of $K$ and $\bar{K}$ in fact coincide, which effectively replaces the computation of $\bar{K}$ by the much easier task of constructing the rank-2 envelope of $K$.

For fused silica with $K$ determined from MD data, the rank-2 envelope construction of $\bar{K}$ is given in Section 4, Table 5.

## REFERENCES

[1] Kenichi Kondo, Satoshi Iio, and Akira Sawaoka. Nonlinear pressure dependence of the elastic moduli of fused quartz up to 3 gpa. *Journal of Applied Physics*, 52(4):2826–2831, 1981.

[2] C. Meade and R. Jeanloz. Effect of a coordination change on the strength of amorphous sio2. *Science*, 241(4869):1072–1074, 1988.

[3] R. J. Clifton, M. Mello, and N. S. Brar. Effect of shear on failure waves in soda lime glass. *AIP Conference Proceedings*, 429(1):521–524, 1998.

[4] A. S. AbouSayed and R. J. Clifton. Pressure shear waves in fused silica. *Journal of Applied Physics*, 47(5):1762–1770, 1976.

[5] S. Sundaram and R. J. Clifton. Flow behavior of soda-lime glass at high pressures and high shear rates. In *American Institute of Physics Conference Series*, volume 429 of *American Institute of Physics Conference Series*, pages 517–520, July 1998.

[6] C. Hari Manoj Simha and Y. M. Gupta. Time-dependent inelastic deformation of shocked soda-lime glass. *Journal of Applied Physics*, 96(4):1880–1890, 2004.

[7] Tomoko Sato and Nobumasa Funamori. High-pressure structural transformation of sio₂ glass up to 100 gpa. *Phys. Rev. B*, 82:184102, Nov 2010.

[8] Tomoko Sato and Nobumasa Funamori. Sixfold-coordinated amorphous polymorph of sio₂ under high pressure. *Phys. Rev. Lett.*, 101:255502, Dec 2008.

[9] Daisuke Wakabayashi, Nobumasa Funamori, Tomoko Sato, and Takashi Taniguchi. Compression behavior of densified sio₂ glass. *Phys. Rev. B*, 84:144103, Oct 2011.

[10] Damien Vandembroucq, Thierry Deschamps, Camille Coussa, Antoine Perriot, Etienne Barthel, Bernard Champagnon, and Christine Martinet. Density hardening plasticity and mechanical ageing of silica glass under pressure: a raman spectroscopic study. *Journal of Physics: Condensed Matter*, 20(48):485221, 2008.

[11] Y. Inamura, Y. Katayama, W. Utsumi, and K.-I. Funakoshi. Transformations in the Intermediate-Range Structure of $\mathrm{SiO}_{2}$ Glass under High Pressure and Temperature. *Physical Review Letters*, 93(1):015501, June 2004.

[12] S. N. Luo, O. Tschaune, P. D. Asimow, and T. J. Ahrens. A new dense silica polymorph: A possible link between tetrahedrally and octahedrally coordinated silica. *American Mineralogist*, 89:455461, 2004.

[13] Michael J. Demkowicz and Ali S. Argon. Autocatalytic avalanches of unit inelastic shearing events are the mechanism of plastic deformation in amorphous silicon. *Phys. Rev. B*, 72:245206, Dec 2005.

[14] M. L. Falk and J. S. Langer. Dynamics of viscoplastic deformation in amorphous solids. *Phys. Rev. E*, 57:7192–7205, Jun 1998.

[15] J. S. Langer. Microstructural shear localization in plastic deformation of amorphous solids. *Phys. Rev. E*, 64:011504, Jun 2001.

[16] M. H. Chen and M. Goldstein. Anomalous viscoelastic behavior of metallic glasses of Pd-Si-based alloys. *Journal of Applied Physics*, 43(4):1642–1648, 1972.

[17] F. Spaepen. A microscopic mechanism for steady state inhomogeneous flow in metallic glasses. *Acta Metallurgica*, 25(4):407–415, 1977.

[18] D. E. Polk and D. Turnbull. Flow of melt and glass forms of metallic alloys. *Acta Metallurgica*, 20(4):493–498, 1972.

[19] A. S. Argon. Plastic deformation in metallic glasses. *Acta Metallurgica*, 27(1):47–58, 1979.

[20] Craig E Maloney and Mark O Robbins. Evolution of displacements and strains in sheared amorphous solids. *Journal of Physics: Condensed Matter*, 20(24):244128, 2008.

[21] O Pilla, L Angelani, A Fontana, J R Gonalves, and G Ruocco. Structural and dynami- cal consequences of density variation in vitreous silica. *Journal of Physics: Condensed Matter*, 15(11):S995, 2003.

[22] Daniel J. Lacks. Localized mechanical instabilities and structural transformations in silica glass under high pressure. *Phys. Rev. Lett.*, 80:5385–5388, Jun 1998.

[23] Min Wu, Yunfeng Liang, Jian-Zhong Jiang, and S Tse John. Structure and properties of dense silica glass. *Scientific reports*, 2:398, 2012.

[24] Liping Huang and John Kieffer. Amorphous-amorphous transitions in silica glass. i. reversible transitions and thermomechanical anomalies. *Phys. Rev. B*, 69:224203, Jun 2004.

[25] Liping Huang and John Kieffer. Amorphous-amorphous transitions in silica glass. ii. irreversible transitions and densification limit. *Phys. Rev. B*, 69:224204, Jun 2004.

[26] Yunfeng Liang, Caetano R. Miranda, and Sandro Scandolo. Mechanical strength and coordination defects in compressed silica glass: Molecular dynamics simulations. *Phys. Rev. B*, 75:024205, Jan 2007.

[27] B. Mantisi, A. Tanguy, G. Kermouche, and E. Barthel. Atomistic response of a model silica glass under shear and pressure. *The European Physical Journal B*, 85(9):304, 2012.

[28] Anaël Lemaître and Christiane Caroli. Rate-dependent avalanche size in athermally sheared amorphous solids. *Phys. Rev. Lett.*, 103:065501, Aug 2009.

[29] B. Dacorogna. *Direct Methods in the Calculus of Variations*. Springer-Verlag New York, Inc., New York, NY, USA, 1989.

[30] K. H. Roscoe, A. N. Schofield, and C. P. Wroth. On the yielding of soils. *Geotechnique*, 8(1):2253, 1958.

[31] A. N. Schofield and P. Wroth. *Critical state soil mechanics*. European civil engineering series. McGraw-Hill, London, New York, 1968.

[32] Steve Plimpton. Fast parallel algorithms for short-range molecular dynamics. *Journal of Computational Physics*, 117(1):1 – 19, 1995.

[33] MBBJM Tuckerman, Bruce J Berne, and Glenn J Martyna. Reversible multiple time scale molecular dynamics. *The Journal of chemical physics*, 97(3):1990–2001, 1992.

[34] Mark Tuckerman. *Statistical mechanics: theory and molecular simulation*. Oxford University Press, 2010.

[35] Gianluca Malavasi, M. Cristina Menziani, Alfonso Pedone, and Ulderico Segre. Void size distribution in md-modelled silica glass structures. *Journal of Non-Crystalline Solids*, 352(3):285 – 296, 2006.

[36] B. W. H. van Beest, G. J. Kramer, and R. A. van Santen. Force fields for silicas and aluminophosphates based on ab initio calculations. *Phys. Rev. Lett.*, 64:1955–1958, Apr 1990.

[37] Wei Jin, Rajiv K Kalia, Priya Vashishta, and José P Rino. Structural transformation, intermediate-range order, and dynamical behavior of sio 2 glass at high pressures. *Physical review letters*, 71(19):3146, 1993.

[38] Wei Jin, Rajiv K. Kalia, Priya Vashishta, and José P. Rino. Structural transformation in densified silica glass: A molecular-dynamics study. *Phys. Rev. B*, 50:118–131, Jul 1994.

[39] Renée M Van Ginhoven, Hannes Jónsson, and L René Corrales. Silica glass structure generation for ab initio calculations using small samples of amorphous silica. *Physical Review B*, 71(2):024208, 2005.

[40] E. D. Lee. Elastic-plastic deformation at finite strains. *Journal of Applied Mechanics*, 13(3):167–178, 1969.

[41] J. Lubliner. On the thermodynamic foundations of non-linear solid mechanics. *Inter- national Journal of Non-Linear Mechanics*, 7(3):237 – 254, 1972.

[42] J Lubliner. On the structure of the rate equations of materials with internal variables. *Acta Mechanica*, 17(1-2):109–119, 1973.

[43] R. T. Rockafellar. *Convex analysis*. Princeton Mathematical Series. Princeton Uni- versity Press, Princeton, N. J., 1970.

[44] J. Lubliner. *Plasticity theory*. Macmillan ; Collier Macmillan, New York, London, 1990.

[45] M. Ortiz and A. Pandolfi. A variational cam-clay theory of plasticity. *Computer Meth- ods in Applied Mechanics and Engineering*, 193:26452666, 2004.

[46] G. Kermouche, E. Barthel, D. Vandembroucq, and Ph. Dubujet. Mechanical mod- elling of indentation-induced densification in amorphous silica. *Acta Materialia*, 56(13):3222 – 3228, 2008.

[47] G. A. Gazonas, J. W. McCauley, I. G. Batyrev, R. C. Becker, P. Patel, B. M. Rice, and N. S. Weingarten. Multiscale modeling of non-crystalline ceramics (glass). Technical Report ARL-MR-0765, U.S. Army Research Laboratory, Aberdeen Proving Ground, MD, 2011.

[48] R. C. Becker. A glass model capturing high-rate fracture observations. Technical Report ARL-TR-6086, U.S. Army Research Laboratory, Aberdeen Proving Ground, MD, 2012.

[49] S. Conti, S. Müller, and M. Ortiz. Non-convex limit analysis. (in preparation), 2017.

[50] J. B. Martin. *Plasticity : fundamentals and general results*. MIT Press, Cambridge, MA, 1975.

[51] I. Ekeland and R. Temam. *Convex analysis and variational problems*. Classics in applied mathematics. Society for Industrial and Applied Mathematics, Philadelphia, 1999.

[52] Irene Fonseca and Stefan Müller. $\mathcal{A}$-quasiconvexity, lower semicontinuity, and Young measures. *SIAM Journal on Mathematical Analysis*, 30(6):1355–1390, 1999.

[53] L. Ambrosio, N. Fusco, and D. Pallara. *Functions of bounded variation and free dis- continuity problems*. Oxford mathematical monographs. Clarendon Press, Oxford ; New York, 2000.

[54] L. Tonelli. *Fondamenti di Calcolo delle Variazioni*. Zanichelli, Bologna, 1921.

[55] C. B. Morrey. Quasi-convexity and the lower semicontinuity of multiple integrals. *Pacific Journal of Mathematics*, 2(1):25–53, 1952.

[56] L. Tartar. Estimations fines des coefficients homogénéisés. In *Ennio De Giorgi collo- quium (Paris, 1983)*, volume 125 of *Research Notes in Mathematics*, pages 168–187. Pitman, Boston, MA, 1985.

THE ANOMALOUS YIELD BEHAVIOR OF FUSED SILICA GLASS
33

$^{1}$Division of Engineering and Applied Science, California Institute of Tech-
nology, 1200 E. California Blvd., Pasadena, CA 91125.
E-mail address: ortiz@caltech.edu

$^{2}$Institut für Angewandte Mathematik, Universität Bonn, Endenicher Allee
60, 53115 Bonn, Germany.