![](./images/811194403078012928_1.jpg)

Journal of the Mechanics and Physics of Solids
48 (2000) 2077–2114

JOURNAL OF THE
MECHANICS AND
PHYSICS OF SOLIDS

www.elsevier.com/locate/jmps

# A theory of subgrain dislocation structures

M. Ortiz *, E.A. Repetto, L. Stainier

Graduate Aeronautical Laboratories, California Institute of Technology, Pasadena, CA 91125, USA

Received 1 April 1999; received in revised form 6 December 1999

## Abstract

We develop a micromechanical theory of dislocation structures and finite deformation single crystal plasticity based on the direct generation of deformation microstructures and the computation of the attendant effective behavior. Specifically, we aim at describing the lamellar dislocation structures which develop at large strains under monotonic loading. These microstructures are regarded as instances of sequential lamination and treated accordingly. The present approach is based on the explicit construction of microstructures by recursive lamination and their subsequent equilibration in order to relax the incremental constitutive description of the material. The microstructures are permitted to evolve in complexity and fineness with increasing macroscopic deformation. The dislocation structures are deduced from the plastic deformation gradient field by recourse to Kröner's formula for the dislocation density tensor. The theory is rendered nonlocal by the consideration of the self-energy of the dislocations. Selected examples demonstrate the ability of the theory to generate complex microstructures, determine the softening effect which those microstructures have on the effective behavior of the crystal, and account for the dependence of the effective behavior on the size of the crystalline sample, or size effect. In this last regard, the theory predicts the effective behavior of the crystal to stiffen with decreasing sample size, in keeping with experiment. In contrast to strain-gradient theories of plasticity, the size effect occurs for nominally uniform macroscopic deformations. Also in contrast to strain-gradient theories, the dimensions of the microstructure depend sensitively on the loading geometry, the extent of macroscopic deformation and the size of the sample. © 2000 Elsevier Science Ltd. All rights reserved.

Keywords: A. Microstructures; A. Dislocations; B. Constitutive behavior; B. Crystal plasticity; C. Energy methods

* Corresponding author. Fax: +1-626-304-0175.
E-mail address: ortiz@madrid.caltech.edu (M. Ortiz).

0022-5096/00/$ - see front matter © 2000 Elsevier Science Ltd. All rights reserved.
PII: S0022-5096(99)00104-0

### 1. Introduction

Crystals deformed to large plastic strains are commonly observed to develop characteristic dislocation structures (Hughes and Hansen 1991, 1993; Hansen, 1992; Bay et al., 1992; Hughes et al. 1994, 1997; Hansen and Hughes, 1995; Rosen et al., 1995; Murr et al., 1997; Nesterenko et al., 1997; Doherty et al., 1997). Often these structures consist of roughly parallel arrays of dislocation walls which, as noted by Ortiz and Repetto (Ortiz and Repetto, 1999), may be regarded as instances of *sequential lamination*, a feature which we endeavor to exploit systematically in the present work. The emergence of these dislocations structures is known to have a marked influence on the hardening characteristics of fee crystals (Argon and Haasen, 1993; Zehetbauer, 1993; Zehetbauer and Seumer, 1993; Les et al., 1996). The formulation of quantitative theories of single-crystal plasticity which explicitly and directly account for the effect of dislocation structures is a long-standing goal of physical metallurgy.

A related issue which has recently been the subject of extensive theoretical and experimental work, concerns the dependence of the macroscopic behavior of single crystals and polycrystals on the size of the sample, identified with the grain size, wire diameter, film thickness, or some other limiting feature size. This dependence is sometimes referred to as *size effect*. Material models which are sensitive to the size of the sample, or to gradients in the deformation field, are necessarily nonlocal and contain intrinsic length-scale parameters. A class of *phenomenological* theories of plasticity which comply with these requirements may be obtained by allowing the hardening relations to depend on strain gradients (Fleck and Hutchinson 1993, 1997; Fleck et al., 1994; Nix, 1998; Nix and Gao, 1998). Strain-gradient theories are nonlocal, endow the material with a single and constant material length scale, and have been used to account for the role of strain-gradient hardening with considerable success.

In this paper we develop a *micromechanical* theory of dislocation structures and finite-deformation single-crystal plasticity based on the direct generation of deformation microstructures and the computation of the attendant effective behavior. Specifically, we aim at describing the *lamellar* dislocation structures which develop at large strains under monotonic loading (Hughes and Hansen 1991, 1993; Bay et al., 1992; Hughes et al. 1994, 1997; Hansen and Hughes, 1995; Rosen et al., 1995; Murr et al., 1997; Doherty et al., 1997) and their effect on the macroscopic behavior of crystals. Often, the observed microstructures exhibit more than one level of lamination, i.e., comprise laminates within laminates (see, e.g., Fig. 6 of Hughes and Hansen, 1993 for an example). Microstructures of this type have long been treated within the context of the crystallographic theory of martensite (Ball and James, 1987; Chipot and Kinderlehrer, 1988; Kohn 1991, 1991; Bhattacharya 1991, 1992; Pedregal, 1993), but, their consideration in connection with crystal plasticity appears to be new.

The cornerstone of the theory is the explicit construction — and equilibration — of evolving deformation and dislocation structures as part of the incremental constitutive description of the material. Among all possible microstructures, sequential

laminates, or 'laminates within laminates', have a recursive or 'tree' structure and can therefore be generated and treated in a particularly efficient manner. It is, there- fore, fortuitous that, as noted above, the experimentally observed microstructures of interest fall into this class. The point of departure of our construction is a conven- tional local model of crystal plasticity. Evidently, only uniform local deformations, generally involving multiple slip, are accounted for by such models. At the most basic level, the approach proposed here may be regarded simply as a means of pro- viding the material with additional local deformation degrees of freedom instead of being compelled to deform uniformly, the material is permitted to develop complex local deformation fields in the form of sequential laminates. Once these additional degrees of freedom are provided to the material, it will spontaneously chose the 'path of least resistance'; i.e., it will develop such microstructures as minimize the incremental work of deformation (Ortiz and Repetto, 1999). Ortiz and Repetto (Ortiz and Repetto, 1999) have noted that, in crystals exhibiting latent, hardening, micro- structural development may indeed offer an energetic advantage over uniform defor- mations.

The scope of the present paper is two-fold. Firstly, we endeavor to formulate a general variational framework for single-crystal plasticity in which microstructures arise naturally as a consequence of the lack of convexity of the incremental energy functional. Secondly, we discuss specific procedures for the efficient implementation of the theory as an incremental constitutive update for use in large-scale computing.

Our variational formulation builds on the approach of Ortiz and Repetto (Ortiz and Repetto, 1999), which is based on the consideration of a time-discretized bound- ary value problem in which the primary unknown is the incremental displacement field over a finite time step. In this setting, the dislocation structures are deduced indirectly from the incompatibility of the plastic deformation gradient field $F^{\mathrm{p}}$, in contrast to other theories of low energy dislocation structures (Neumann, 1986; Lub- arda et al., 1993), in which the spatial dislocation distribution and its time evolution are the primary unknowns. Ortiz and Repetto (Ortiz and Repetto, 1999) noted that this incremental or time-discretized boundary value problem obeys a minimum prin- ciple, and proceeded to formally derive the corresponding incremental energy density by recourse to work-minimizing deformation paths. More direct, formulations of the incremental energy density are also possible for a wide class of materials (Radovitzky and Ortiz, 1999; Ortiz and Stainier, 1999), and in the work presented here we follow this more direct route.

A far-reaching realization (Ortiz and Repetto, 1999) is that, in crystals exhibiting latent hardening the energy function is nonconvex, which favors the development of microstructures. Roughly speaking, the resulting microstructures consist of regions in which a small number of slip systems are activated, thereby mitigating the effects of latent hardening. Using a sequential lamination construction, Ortiz and Repetto (Ortiz and Repetto, 1999) were able to characterize analytically several dislocation structures commonly observed to occur in fatigued fcc crystals, including the coplanar slip zones which form during the stage I of hardening in Cu-lat.%Ge single crystals; the fence structures observed during the early stages of stage II of hardening in fcc crystals; and the parallel arrays of dipolar walls which develop in fcc crystals

fatigued to saturation. An instance of a possible rank-two laminate, or a laminate of laminates, was also identified and explained mathematically by Ortiz and Repetto (Ortiz and Repetto, 1999). It should be noted, however, that all these applications of the theory were concerned with configurations leading to the 'training' of the crystal and the establishment of a fixed microstructure. In the present work, by con- trast, we specifically address the issue of microstructures which evolve with defor- mation.

In order to account for the size effect, i.e., the observed dependence of the behavior of crystals on sample size, we explicitly include the self-energy of the dislocations into the total energy of the crystal. Since the self-energy of the dislocations is a function of the dislocation density, which by Kröner's formula is in turn given by the curl of $F^{\mathrm{p}}$, the resulting energy is nonlocal. The nonlocal theory effectively accords well-defined dimensions to all the features of the microstructure, including the lamellar thicknesses. These optimal microstructural sizes follow directly from the competition between the dislocation wall energies and the energy of the transition or boundary layers which inevitably form at complex lamellar interfaces. The absol- ute dimensions of the microstructure depend on two length-scale parameters: the Burgers vector length $b$, and some suitable geometrical feature size $d$ representative of the overall size of the microstructure. Depending on the application, $d$ may be variously identified with the grain size of a polycrystal, the thickness of a film, or some other appropriate feature size. For definiteness, however, in the remainder of the paper we shall refer to $d$ as the 'grain size'.

The variational formulation just outlined provides a solid mathematical foundation for the theory and a plausible mechanistic explanation for why microstructures form spontaneously in deformed single crystals. We also wish to emphasize that the theory lends itself to an efficient implementation as part of the constitutive updates which are applied, e.g., at the quadrature-point level in large-scale finite-element, simula- tions. The basis of the implementation is the recursive treatment of sequential lami- nates, which from a graph-theoretical point of view may be regarded as tree struc- tures. The deformations at all levels of the tree, i.e., in all the lamellar which form the microstruture, are obtained by the repeated application of Hadamard's compatibility conditions. The deformations then follow as a function of a collection of vectors $a_{i}$, which describe the amplitudes of the deformation jumps across each lamellar inter- face $i$. This collection of vectors may be regarded as the additional local degrees of freedom afforded by the microstructure. The microstructure is also subject to equilib- rium in the form of continuity of tractions across all lamellar interfaces. These equi- librium conditions, in conjunction with the local constitutive updates, define a system of nonlinear algebraic equations which can be solved for the vectors $a_{i}$. This in turn determines the incremental deformations at, all levels of the tree.

Dislocation structures generally evolve in complexity and fineness with defor- mation. We account for microstructural refinement by allowing the leaves of the tree, i.e., the lowest level lamellae, to branch into pairs of new leaves. By this process a new level of lamination is added to the microstructure. The geometry of the new interface and the volume fractions of the new leaves may be determined by recourse to energy minimization. When the incremental behavior is described by a linearized

Hill's comparison solid, this process of energy minimization leads simply to a con-
ventional Hill-Hadamard localization analysis (see e.g., Asaro and Rice, 1977).

The additional key element of the nonlocal theory concerns the estimation of the
dislocation wall energies and the lamellar interfacial energies, whose competition
determines the microstructural dimensions. To this end we adapt a construction of
Ball and James (Ball and James, 1987) leading to the definition of kinematically
admissible fields which effect a compatible transition between complex lamellar. The
construction yields, therefore, an upper bound to the interfacial energy which we
use as a — hopefully tight — estimate of the actual energy. Under the assumption
of separation of scales, the nonlocal contribution to the energy may be treated per-
turbatively. The nonlocal theory then yields all microstructural dimensions and the
effect of the grain size $d$ on the effective macroscopic behavior of the crystal.

We illustrate the range of behaviors predicted by the theory by way of selected
examples. Two of them are concerned with crystals deformed in simple shear and
are motivated by the recent, work of Hughes et al. (Hughes et al., 1994) on the
near-surface microstructures which develop under large sliding loads. The examples
demonstrate the ability of the theory to account for the development of complex
microstructures and the softening effect that such microstructures have on the effec-
tive macroscopic response of the crystal. It bears emphasis that these microstructures
develop under nominally uniform macroscopic deformation. The present theory is
therefore in contrast to strain-gradient theories which require the presence of macro-
scopic strain gradients for nonlocal effects to arise. We also illustrate how the theory
naturally predicts a size effect with the aid of an example concerned with the defor-
mation of a crystal under uniaxial tension along the (001) axis. As expected, small
grain sizes result in stiffer behavior of the crystal. The theory also predicts the micro-
structure to refine with increasing strain: in accordance with experiment, (Hughes et
al., 1994). This is in contrast with strain-gradient plasticity theories, in which the
microstructural lengthscale is constant and independent of deformation.

## 2. Crystal plasticity

We begin by reviewing key aspects of the constitutive theory of single crystals
which are pertinent, to subsequent developments. Locally, the deformation of the
crystal is fully described by the local deformation gradient, $F$. Ductile single crystals
are characterized by the existence of a certain class of deformations $F^{\rm p}$, or 'plastic'
deformations, which leave the crystal lattice undistorted and unrotated, and, conse-
quently, induce no long-range stresses. In addition to the plastic deformation $F^{\rm p}$,
some degree of lattice distortion $F^{\rm e}$ may also be expected in general. One therefore
has, locally,

$$F=F^{\rm e}F^{\rm p} \tag{1}$$

This multiplicative elastic-plastic kinematics was first suggested by Let (Lee, 1969)
and further developed by others (Teodosiu, 1969; Asaro and Rice, 1977; Havner,

1973; Hill and Rice, 1972; Mandel, 1972; Rice, 1971) within the context of ductile single crystals.

We adopt an internal variable formalism (Lubliner 1972, 1973; Rice, 1975) to describe the local inelastic processes and postulate the existence of a Helmholtz free energy density of the form

$$
A=A(F^{\mathrm{e}},F^{\mathrm{p}},Q)=A(FF^{\mathrm{p}-1},F^{\mathrm{p}},Q)\equiv A(F,F^{\mathrm{p}},Q) \tag{2}
$$

where $Q$ denotes some suitable collection of internal — or hardening — variables. Common choices of internal variables for crystals are the slip strains and dislocation densities on each of the slip systems of the crystal. The free energy may also depend on other variables, such as temperature, vacancy and solute concentrations, and others, whose evolution is governed by partial differential field equations. We shall tacitly assume that such variables are integrated independently, e.g., by recourse to a staggered or fractional-step procedure, and for present purposes they may be regarded as given. The local *state* of the material is described by the variables $\{F, F^{\mathrm{p}}, Q\}$. In metals, the elastic response is ostensibly independent of the internal processes aid the free energy Eq. (2) may be assumed to decompose additively as

$$
A=W^{\mathrm{e}}(FF^{\mathrm{p}-1})+W^{\mathrm{p}}(F^{\mathrm{p}},Q) \tag{3}
$$

The function $W^{\mathrm{e}}$ determines the elastic response of the metal, e.g., upon unloading, whereas the function $W^{\mathrm{p}}$ describes the hardening of the material. Physically, $W^{\mathrm{p}}$ represents the stored energy due to the plastic working of the crystal.

We shall denote by $P$ the first Piola-Kirchoff stress tensor (e.g., Marsden and Hughes, 1983), which in the absence of viscosity follows from Coleman's relations as

$$
P=A_{,F}(F,F^{\mathrm{p}},Q) \tag{4}
$$

In order to determine the evolution of the internal variables, suitable kinetic equations must be supplied. Assuming that the rate of the local internal processes described by $Q$ is determined solely by the local thermodynamic state, the general form of the kinetic equations is

$$
\dot{Q}=f(F,F^{\mathrm{p}},Q) \tag{5}
$$

In addition, the rate of plastic deformation $\dot{F}^{\mathrm{p}}$ is subject to the kinematic restrictions imposed by a flow rule. In crystals, plastic deformations are crystallographic in nature. The conventional flow rule in this cast is of the form (Rice, 1971)

$$
\dot{F}^{\mathrm{p}}=\left(\sum_{\alpha=1}^{N} \dot{\gamma}^{\alpha} s^{\alpha} \otimes m^{\alpha}\right) F^{\mathrm{p}} \tag{6}
$$

where $\gamma^{\alpha}$ is the slip strain, and $s^{\alpha}$, and $m^{\alpha}$ are orthogonal unit vectors defining the slip direction and slip-plane normal corresponding to slip system $\alpha$. The collection $\gamma$ of slip strains may be regarded as part of the internal variable set $Q$. A zero value of a slip rate $\dot{\gamma}^{\alpha}$ signifies that the corresponding slip system $\alpha$ is inactive. The flow rule Eq. (6) allows for multiple slip, i.e., for simultaneous activity on more than one system one a region of the crystal. The vectors $\{s^{\alpha}, m^{\alpha}\}$ remain consistant through-

out, the deformation and are determined by crystallography. In fcc crystals $s^{\alpha}$ is any cube face diagonal and $m^{\alpha}$ any cube diagonal, see Table 1. Note that we differentiate between pairs of slip systems of the form $(+s, m)$ and $(-s, m)$, and require that,

$$
\dot{\gamma}^{\alpha} \geq 0 \tag{7}
$$

which embodies the notion of plastic irreversibility.

The thermodynamic forces conjugate to $Q$ are

$$
Y=-A_{, Q} \tag{8}
$$

In particular, for a single crystal possessing a structure independent, elastic response, Eq. (3), the thermodynamic form conjugate to $\gamma^{\alpha}$ is given by the 'overstress'

$$
Y^{\alpha}=\tau^{\alpha}-\tau_{\mathrm{c}}^{\alpha} \tag{9}
$$

where

$$
\tau^{\alpha}=\left(F^{\mathrm{eT}} P F^{\mathrm{pT}}\right) \cdot\left(s^{\alpha} \otimes m^{\alpha}\right) \tag{10}
$$

is the resolved shear stress on the plant of normal $m^{\alpha}$ in the direction $s^{\alpha}$, and

$$
\tau_{\mathrm{c}}^{\alpha}=W_{, \gamma^{\alpha}}^{\mathrm{p}} \tag{11}
$$

is the critical resolved shear stress of system $\alpha$. In writing Eq. (9) we have accounted for the fact that, in view of the flow rule Eq. (6), a variation in $\gamma^{\alpha}$ necessarily implies a variation in $F^{\mathrm{p}}$. In addition, the dot product, between two second-rank tensors is taker1 to be: $A \cdot B=A_{i j} B_{i j}$. The hardening relations Eq. (11) may be expressed in rate form as

$$
\dot{\tau}_{\mathrm{c}}^{\alpha}=\sum_{\beta=1}^{N} h^{\alpha \beta} \dot{\gamma}^{\beta} \tag{12}
$$

where

$$
h^{\alpha \beta}=W_{, \gamma^{\alpha} \gamma^{\beta}}^{\mathrm{p}}(\gamma) \tag{13}
$$

is the hardening matrix of the crystal.

Table 1
Slip systems of an FCC crystal and Schmid and Boas' nomenclature (Schmid and Boas, 1961)

<table>
<thead>
<tr>
<th>System</th>
<th>B2</th>
<th>B4</th>
<th>B5</th>
<th>A3</th>
<th>A2</th>
<th>A6</th>
</tr>
</thead>
<tbody>
<tr>
<td>$\sqrt{2}s$</td>
<td>$\pm[011]$</td>
<td>$\pm[101]$</td>
<td>$\pm[110]$</td>
<td>$\pm[101]$</td>
<td>$\pm[011]$</td>
<td>$\pm[110]$</td>
</tr>
<tr>
<td>$\sqrt{3}m$</td>
<td>(111)</td>
<td>(111)</td>
<td>(111)</td>
<td>(111)</td>
<td>(111)</td>
<td>(111)</td>
</tr>
<tr>
<td>System</td>
<td>C1</td>
<td>C3</td>
<td>C5</td>
<td>D4</td>
<td>D1</td>
<td>D6</td>
</tr>
<tr>
<td>$\sqrt{2}s$</td>
<td>$\pm[011]$</td>
<td>$\pm[101]$</td>
<td>$\pm[110]$</td>
<td>$\pm[101]$</td>
<td>$\pm[011]$</td>
<td>$\pm[110]$</td>
</tr>
<tr>
<td>$\sqrt{2}m$</td>
<td>(111)</td>
<td>(111)</td>
<td>(111)</td>
<td>(111)</td>
<td>(111)</td>
<td>(111)</td>
</tr>
</tbody>
</table>

The kinetic relations Eq. (5) are said to derive from an inelastic potential if there exists a kinetic potential $\psi(Y)$ such that,

$$\dot{Q}=\psi_{, Y}(Y) \tag{14}$$

Additionally, we may introduce the dual potential $\psi^{*}(\dot{Q})$ by recourse to the Legendre transformation

$$\psi^{*}(\dot{Q})=\max _{Y}\{Y \cdot \dot{Q}-\psi(Y)\} \tag{15}$$

Then one has

$$Y=\psi^{*}{ }_{, \dot{Q}}(\dot{Q}) \tag{16}$$

which constitutes a restatement of the kinetic equations Eq. (14). A particular case of these potential relations follows from Schmid's rule, which states that the slip strain rate $\dot{\gamma}^{\alpha}$ is a function of the driving force $Y^{\alpha}$ acting on the same system. i.e.,

$$\dot{\gamma}^{\alpha}=f^{\alpha}\left(Y^{\alpha}\right) \tag{17}$$

Rice (Rice, 1975) noted that the kinetic relations Eq. (17) have the potential structure

$$\dot{\gamma}^{\alpha}=\psi_{, Y^{\alpha}}(Y) \tag{18}$$

where

$$\psi(Y)=\sum_{\alpha=1}^{N} \int_{0}^{Y^{\alpha}} f^{\alpha}\left(Y^{\alpha}\right) d Y^{\alpha} \tag{19}$$

is the inelastic potential.

In many crystals, it is found that activity in a slip system hardens other systems more than it hardens the system itself (Kocks 1964, 1966; Ramaswami et al., 1965; Franciosi et al., 1980; Bassani and Wu, 1991a,b), a phenomenon known as latent hardening. Many of the intricacies in the behavior of single crystals, such as the development of the dislocation structures described subsequently, may be traced to the presence of latent hardening (Cuitiño and Ortiz 1992a, 1993; Ortiz and Repetto, 1999). A simple model of latent hardening was proposed by Hutchinson (Hutchinson, 1976). In Hutchinson's model the evolution of the flow stresses is taken to be governed by the hardening law Eq. (12) with a hardening matrix of the form

$$h^{\alpha \beta}=h\left[q+(1-q) \delta^{\alpha \beta}\right] \tag{20}$$

The parameter $q$ characterizes the latent, hardening behavior. The choice $q=1$ corresponds to isotropic or Taylor hardening. For fcc metals, Kocks (Kocks, 1960) determined experimentally the range of this parameter to be $1 \leq q \leq 1.4$. A form of the self-hardening rate $h$, suitable for Al-Cu alloys is (Pierce et al., 1982; Chang and Asaro, 1981)

$$h(\gamma)=h_{0} \operatorname{sech}^{2}\left(\frac{h_{0} \gamma}{\tau_{\mathrm{s}}-\tau_{0}}\right) \tag{21}$$

where

$$
\gamma=\sum_{\alpha=1}^{N} \gamma^{\alpha}
\tag{22}
$$

is an effective slip strain, $h_{0}$ is the initial hardening rate, $\tau_{0}$ is the critical resolved shear stress and $\tau_{\mathrm{S}}$ is the saturation strength. Comparisons between Eq. (21) and experimental data are given by Asaro (Asaro, 1983).

## 3. Time-discretized constitutive relations

In anticipation of the emergence of fine microstructures, we adopt a variational perspective and endeavor to formulate the boundary value problem of finite crystal plasticity as a sequence of *incremental* energy minimization problems. The appropriate definition of the energy function to be minimized has been addressed by Radovitzky and Ortiz (Radovitzky and Ortiz, 1999), Ortiz and Repetto (Ortiz and Repetto, 1999), and Ortiz and Stainier (Ortiz and Stainier, 1999). An incremental energy density may formally be obtained by integration of the constitutive relations along 'minimizing paths', i.e., along such deformation histories as minimize the incremental work of deformation. The work of deformation itself then supplies the sought strain energy potential. This approach has been used in the past to derive deformation, or pseudo-elastic, theories of plasticity. A recent, application of minimizing paths to the study of dislocation structures in ductile single crystals may be found in (Ortiz and Repetto, 1999). However, the task of determining minimizing paths for specific models is often daunting, specially for rate-sensitive materials, which detracts from the practicality of the approach. Here, we adopt an alternative and more direct method for formulating incremental energy densities proposed by Radovitzky and Ortiz (Radovitzky and Ortiz, 1999) and Ortiz and Stainier (Ortiz and Stainier, 1999).

We envisage an incremental solution procedure and concern ourselves with a generic time interval $[t_{n}, t_{\mathrm{n}+1}]$. Let the initial state $(F_{n}, F_{n}^{P}, Q_{n})$ and the updated deformations $F_{\mathrm{n}+1}$ be given. The first step in effecting an integration of the constitutive relations is to provide an incremental rule for updating $F^{\mathrm{p}}$ in a manner compatible with the flow rule Eq. (6). One possibility is to use the exponential mapping:

$$
F_{n+1}^{\mathrm{p}}=\exp \left\{\sum_{\alpha=1}^{N} \Delta \gamma^{\alpha} s^{\alpha} \otimes m^{\alpha}\right\} F_{n}^{\mathrm{p}}
\tag{23}
$$

where

$$
\Delta \gamma^{\alpha}=\gamma_{n+1}^{\alpha}-\gamma_{n}^{\alpha}
\tag{24}
$$

A particularly appealing aspect of the exponential update Eq. (23) is that it exactly preserves volume in the absence of climb, i.e., when $s^{\alpha}$ and $m^{\alpha}$ are orthogonal. Other

alternative time-discretizations of the flow rule may be found elsewhere (Cuitiño and Ortiz, 1992b; Miehe and Stein, 1992; Miehe, 1996).

Suppose that the kinetic equations possess the potential structure Eq. (14). Then we may introduce the incremental work of deformation function:

$$
D_{n}\left(F_{n+1}, F_{n+1}^{\mathrm{p}}, Q_{n+1}\right)=A\left(F_{n+1}, F_{n+1}^{\mathrm{p}}, Q_{n+1}\right)-A_{n}+\Delta t \psi^{*}\left(\frac{Q_{n+1}-Q_{n}}{\Delta t}\right)
\tag{25}
$$

The incremental energy density may be defined as

$$
W_{n}\left(F_{n+1}\right)=W_{n-1}\left(F_{n}\right)+\min _{Q_{n+1}} D_{n}\left(F_{n+1}, F_{n+1}^{\mathrm{p}}, Q_{n+1}\right)
\tag{26}
$$

where it is tacitly understood that $F_{n+1}^{\mathrm{p}}$ is computed through Eq. (23) or some other discretization of the flow rule. The slip strains $\{\gamma_{n+1}^{\alpha}, \alpha=1,..., N\}$ are regarded as a subset of $Q_{n+1}$ and, consequently, are optimized along with the remaining of the internal variables. In appending the label $n$ to $D_{n}$, and $W_{n}$, we wish to emphasize that these functions are incremental in the sense that they depend parametrically on the local state $(F_{n}, F_{n}^{\mathrm{p}}, Q_{n})$ at time $t_{n}$. In particular, the incremental strain-energy density $W_{n}$ changes between time steps, as required by irreversibility. For simplicity, in writing Eq. (26) we have assumed that the material lacks viscosity in the Newton- ian sense. A more general constitutive framework including viscosity has been con- sidered by Radovitzky and Ortiz (Radovitzky and Ortiz, 1999) and Ortiz and Stainier (Ortiz and Stainier, 1999). It may be shown (Radovitzky and Ortiz, 1999; Ortiz and Stainier, 1999) that, the internal-variable update implied in Eq. (26) is consistent with the kinetic relations Eq. (16). In addition, one has

$$
P_{n+1}=\frac{\partial W_{n}}{\partial F_{n+1}}\left(F_{n+1}\right)
\tag{26a}
$$

i.e., $W_{n}$, furnishes a potential for the stresses $P_{n+1}$ at, time $t_{n+1}$.

Unfortunately, the models of latent, hardening proposed to date rarely derive from a potential as in Eq. (13). In order to be able to bring these models into conformity with the variational framework envisioned here, we simply treat the hardening matrix explicitly by sampling it at the beginning of the time step. Provided that the harden- ing matrix is symmetric, this is tantamount to a step-by-step quadratic approximation of the stored energy $W^{p}$, namely,

$$
W_{n}^{\mathrm{p}}\left(\gamma_{n+1}\right)=W_{n}^{\mathrm{p}}+\sum_{\alpha}\left\{\tau_{c n}^{\alpha}\left(\gamma_{n+1}^{\alpha}-\gamma_{n}^{\alpha}\right)+\frac{1}{2}\left(\gamma_{n+1}^{\alpha}-\gamma_{n}^{\alpha}\right) \sum_{\beta} h_{n}^{\alpha \beta}\left(\gamma_{n+1}^{\beta}-\gamma_{n}^{\beta}\right)\right\}
\tag{26b}
$$

where $\tau_{c n}^{\alpha}$ and $h_{n}^{\alpha \beta}$ are the critical resolved shear stress for system $\alpha$ and the hardening matrix at time $t_{n}$ respectively.

## 4. Incremental variational formulation

Next, we turn to the general incremental boundary value problem of the elastic- plastic solid. We consider a general crystal occupying a domain $B_{0}$ in its reference

configuration. The deformation of the crystal at time $t$ is described by a deformation mapping $\varphi(X, t): B_{0} \rightarrow R^{3}$. The deformation gradierit field is

$$
F=\nabla_{0} \varphi\qquad(27)
$$

where $\nabla_{0}$ is the material gradient over $B_{0}$. In the components, $F_{i, J}=\varphi_{i, J}$.

The multiplicative decomposition Eq. (1) of $F$ is now assumed to apply locally for all $X$ in $B_{0}$ and $t$. We note that neither $F^{\mathrm{e}}$ nor $F^{\mathrm{p}}$ define compatible fields. Follow- ing Nye (Nye, 1953); see also (Mura, 1987), the dislocation density tensor is defined as

$$
A=\nabla_{0} \times F^{\mathrm{p}}\qquad(28)
$$

In components, $A_{i, J}=F_{i K, L}^{\mathrm{p}} \epsilon_{\mathrm{L} \mathrm{KJ}}$, where $\epsilon_{\mathrm{L} \mathrm{KJ}}$ is the permutation tensor. It is evident, from this definition that, $A$ is a measure of the incompatibility of $F^{\mathrm{p}}$ and that, from a continuum perspective, dislocations are inextricably related to incompatibility. A direct consequence of definition Eq. (28) is that

$$
\nabla_{0} \cdot A=0\qquad(29)
$$

This identity embodies the physical requirement, that dislocation lines cannot end abruptly in the interior of the crystal. Identity Eq. (29) also embodies Frank's rule for dislocation reactions. It, should be carefully noted that, in the present theory, the dislocation density $A$ is a derived field which follows from $F^{\mathrm{p}}$.

Within a time-discretized framework, the equilibrium deformations $\varphi_{\mathrm{n}+1}$ of the crystal at time $t_{\mathrm{n}+1}$ may be identified with the minimizers of the functional

$$
\Phi_{n}\left[\varphi_{n+1}\right]=\int_{B_{0}} W_{n}\left(\nabla_{0} \varphi_{n+1}\right) d V_{0}+\text { forcing terms }\qquad(30)
$$

where $W_{n}$ is the incremental strain-energy density Eq. (26). In view of the potential relations Eq. (26a), the first term in $\Phi_{n}$ may be regarded as a measure of the work of deformation, and $\Phi_{n}$ itself as a path-dependent potential energy. It also follows from Eq. (26a) that the Euler-Lagrange equations corresponding to Eq. (30) are the equilibrium equations of the body. It should be carefully noted that the functional $\Phi_{n}$ is strictly incremental, and it, depends on the initial state $\{F_{n}, F_{n}^{\mathrm{p}}, Q_{n}\}$ of the crystal at time $t_{n}$ through the dependence of $W_{n}$ on the local initial state.

For typical crystals exhibiting latent hardening the variational problem just stated may have no solution, i.e., there may be no deformation mapping $\varphi_{\mathrm{n}+1}$ for which the infimum of Eq. (30) is attained. Mathematically, this owes to the lack of quasi-convexity of the incremental energy density $W_{n}$ (see, e.g., Dacorogna, 1989). It is generally possible, however, to construct deformation mappings $\varphi_{\mathrm{n}+1}$ which bring $\Phi_{n}[\varphi_{\mathrm{n}+1}]$ arbitrarily close to its minimum value. Inevitably, such deformation map- pings exhibit fine microstructure in the form of rapidly varying deformation patterns. To these patterns there correspond equally intricate dislocation structures through Nye's relation Eq. (28). Ortiz and Repetto (Ortiz and Repetto, 1999) have shown that certain energy minimizing microstructures closely match a number of dislocation

patterns commonly observed to occur in fatigued fee crystals, including the coplanar slip zones which form during the stage I of hardening in Cu-lat.%Ge single crystals; the fence structures observed during the early stages of stage II of hardening in fcc crystals; and the parallel arrays of dipolar walls which develop in fcc crystals fatigued to saturation.

In the case of crystal plasticity, the fineness of microstructures is evidently con- strained by the crystal lattice. This cutoff has a profound influence on the scaling properties of the crystal (Ortiz and Repetto, 1999) and warrants careful attention. The effect of the crystal lattice may be approximated simply by adding to the free energy of the crystal the self-energy of the dislocations. All other contributions of the dislocation population to the energy of the crystal are presumed to be accounted for in the free energy Eq. (2) in some effective sense. A straightforward derivation (Ortiz and Repetto, 1999) gives this self-energy in the form:

$$
E^{\mathrm{self}}=\int_{B_{0}} \frac{T}{b}|A| d V_{0}=\int_{B_{0}} \frac{T}{b}\left|\nabla_{0} \times F^{\mathrm{p}}\right| d V_{0}
\tag{31}
$$

where $T$ is the dislocation self-energy per unit length, or dislocation line tension, and $b$ is the magnitude of the Burgers vector. In writing Eq. (31), we assume, for simplicity, that, $T$ is independent of the orientation of the dislocation segment. A commonly adopted expression for $T$ is (Kuhlmann-Wilsdorff, 1989)

$$
T=C \mu b^{2}
\tag{32}
$$

where $\mu$ is an average shear modulus and $C$ is a constant, of order unity. It should be carefully noted that $C$ is a logarithmically decreasing function of the dislocation density in the walls (Kuhlmann-Wilsdorff, 1989). Since the dislocations are densely packed within the walls, a comparatively low value of $C$ is likely to be appropriate. The ratio $T / b$ has the units of a surface energy. It will prove convenient to introduce the reference surface energy

$$
\Gamma=C \mu d
\tag{33}
$$

where $d$ is the grain size, and the small parameter

$$
\epsilon=\sqrt{\frac{b}{d}}
\tag{34}
$$

With this notation, the functional to be minimized is

$$
\Phi_{n}\left[\varphi_{n+1}\right]=\int_{B_{0}}\left[W_{n}\left(\nabla_{0} \varphi_{n+1}\right)+\epsilon^{2} \Gamma\left|\nabla_{0} \times F_{n+1}^{\mathrm{p}}\right|\right] d V_{0}+\text { forcing terms }
\tag{35}
$$

which is augmented from Eq. (30) by the addition of the dislocation self energy Eq. (31). It, should be carefully noted that, by virtue of this extension, the functional Eq. (35) becomes nonlocal. In particular, it depends on the plastic deformation gradi- ent through the dislocation density tensor $A$. In writing Eq. (30), it is tacitly implied

that the local plastic deformation $F_{n+1}^{\mathrm{p}}(X)$ is obtained by the local optimisation Eq. (26). It is clear from the form of Eq. (35) that the self-energy term plays the role of a singular perturbation superposed on the local form of the energy functional. In particular, the self-energy vanishes and the local form of the incremental potential energy is recovered in the formal limit, of $\epsilon \to 0$.

## 5. The effective incremental problem

In the remainder of this paper, we turn our attention to the formulation of an effective theory of single crystals with microstructure in the regime of $\epsilon<1$. This regime corresponds to the assumption of *separation of scales*. Indeed, as we shall see, the condition $\epsilon<1$ ensures that the microstructure consists of lamellae which are fine on the scale of the grain size $d$.

We seek an effective potential energy of the form

$$
\bar{\Phi}_{n}\left[\varphi_{n+1}\right]=\int_{B_{0}} \bar{W}_{n}\left(\nabla_{0} \varphi_{n+1}\right) d V_{0}+\text { forcing terms }
$$

for some effective energy density $\bar{W}_{n}$. Here, the deformation mapping $\bar{\varphi}_{n+1}$ describes a macroscopic deformation of the crystal exhibiting slow variation on the scale of $d$. The effective energy density $\bar{W}_{n}$ may be computed as follows. Consider a crystallite occupying a domain $\Omega_{0}$ of size $d$ to which the following affine boundary conditions are applied:

$$
\varphi(X, t)=\bar{F}(t) \cdot X, \quad X \in \partial \Omega_{0}
$$

In the limit of fine microstructures, the shape of $\Omega_{0}$ is immaterial (see, e.g., Dacorogna, 1989). It follows by a straightforward application of the divergence theorem that $\bar{F}(t)$ coincides with the average deformation $\Omega_{0}$ at time $t$ and, consequently, plays the role of a macroscopic deformation gradient. In a time-discretized setting, we actually apply a sequence of macroscopic deformation gradients $\bar{F}_{0}, \bar{F}_{1}, \ldots, \bar{F}_{n}$, resulting in microscopic state fields $\left\{F_{n}, F_{n}^{\mathrm{p}}, Q_{n}\right\}$ at time $t_{n}$, and we subsequently apply a prescribed macroscopic deformation $\bar{F}_{n+1}$ at time $t_{\mathrm{n}+1}$. The effective energy density is, then,

$$
\bar{W}_{n}\left(\bar{F}_{n+1}\right)=\inf _{\varphi_{n+1}} \frac{1}{\left|\Omega_{0}\right|} \int_{\Omega_{0}}\left[W_{n}\left(\nabla_{0} \varphi_{n+1}\right)+\epsilon^{2} \Gamma\left|\nabla_{0} \times F_{n+1}^{\mathrm{p}}\right|\right] d V_{0}
$$

where the infimum is taken over all deformation fields $\varphi_{\mathrm{n}+1}$ satisfying the affine boundary conditions Eq. (37). We note that in general we shall be interested in the case of $\epsilon$ small but not necessarily zero. Under these conditions the effective energy density $\bar{W}_{n}\left(\bar{F}_{n+1}\right)$ may be expected to exhibit a dependence on the size $d$ of the domain, or size effect. In view of the structure of the functional Eq. (36), its Euler–

Lagrange equations follow in terms of the divergence of a macroscopic stress field $\bar{P}_{n+1}$ obtained through the relation

$$
\bar{P}_{n+1}=\frac{\partial \bar{W}_{n}}{\partial \bar{F}_{n+1}}
\tag{39}
$$

where $\bar{F}_{n+1}=\nabla_{0} \bar{\varphi}_{n+1}$ is the macroscopic deformation gradient field. It follows, therefore, that the effective incremental strain-energy density $\bar{W}_{n}$ furnishes a potential for the macroscopic incremental stress-strain relations.

In the presence of latent hardening, the incremental strain-energy density $W_{n}$ lacks quasiconvexity and we may expect

$$
\bar{W}_{n}(\bar{F}_{n+1})<W_{n}(\bar{F}_{n+1})
\tag{40}
$$

i.e., the uniform deformation $\bar{F}_{n+1}$ does not minimize the incremental work of deformation. Instead, such minimization requires the development of microstructures (Ortiz and Repetto, 1999). Correspondingly, a marked reduction in the hardening rate predicted by the theory may be expected to accompany the formation of dislocation structures, as observed experimentally (Zehetbauer, 1993; Zehetbauer and Seumer, 1993; Les et al., 1996). The calculation of the effective energy density, and by extension of the effective behavior of the crystal, therefore hinges on the ability to find a microstructure $\varphi_{\mathrm{n}+1}$ which minimizes the incremental work of deformation over the domain $\Omega_{0}$. It should be carefully noted that in general a microstructure may be already established within $\Omega_{0}$ at time $t_{n}$. The calculation of these evolving microstructures is, therefore, incremental in nature. This microstructural evolution represents an irreversible internal process which renders the incremental energy density $\bar{W}_{n}$ history dependent. Thus, $\bar{W}_{n}$ depends on the precise history of macroscopic deformations prior to $\bar{F}_{n}$ as befits plastic irreversibility. In particular, the crystal exhibits hysteresis under cyclic deformation.

By construction, the effective energy density $\bar{W}_{n}$ is quasiconvex, and the the infimum of the effective potential energy Eq. (36) is indeed realized for some classical deformation field $\varphi_{\mathrm{n}+1}$. The effective problem is, therefore, well-posed. The solution of the effective problem entails the determination of deformation fields $\bar{\varphi}_{n+1}$ which vary on the macroscale, and the attendant microstructures, which are effectively subsumed within $\bar{W}_{n}$, need no longer be accounted for explicitly. The efficient calculation of the effective energy density $\bar{W}_{n}$ is addressed next.

## 6. Dislocation structures — laminates

Next we turn to the problem of calculating the effective macroscopic behavior of crystals with microstructure as described by the effective incremental energy density $\bar{W}_{n}$ defined in Eq. (38). We assume that a microstructure compatible with a macroscopic deformation $\bar{F}_{n}$ is known over the domain $\Omega_{0}$ at time $t_{n}$. In addition, we are given a new macroscopic deformation $\bar{F}_{n+1}$. The problem is to find a new microstructure which minimizes the incremental energy of the crystallite $\Omega_{0}$. An approximate

yet phyically relevant-solution to this problem may be obtained by restricting the competing microstructures to the class of sequential laminates. In this section we proceed to formulate an efficient algorithm for carrying out the requisite microstructural updates. For simplicity of notation, we henceforth omit, the label $n+1$ previously used to designate the value of physical variables at time $t_{n+1}$.

Uniform deformations may conentionally be categorized as rank-zero laminates. In order to define laminates of rank one, we introduce the characteristic functions $\chi^{ \pm}(\xi):[0,l] \to R$ of the as

$$
\chi^{+}(\xi)=
\begin{cases}
0, & \text{if } \xi \in[0,l\lambda^-) \\
1, & \text{if } \xi \in[l\lambda^- l),
\end{cases} \tag{41}
$$

$$
\chi^{-}(\xi)=1-\chi^{+}(\xi) \tag{42}
$$

with $\lambda^- \epsilon(0,1)$. These functions may be extended to the entire real line by periodicity. We also set $\lambda^+=1-\lambda^-$, so that $\lambda^++\lambda^-=1$. Consider two deformations $F^{ \pm}$ satisfying Hadamard's jump condition:

$$
[F]=F^{+}-F^{-}=a \otimes N \tag{43}
$$

for some 'polarization' vector $a$ and unit vector $N$. Evidently, $a$ measures the amplitude of the jump and $N$ is the unit normal to the plant of discontinuity. Then, the corresponding laminate of layer thickness $l$ and volume fractions $\lambda^{ \pm}$ is characterized by deformation gradients of the form

$$
F(X)=\chi^{+}(X \cdot N)F^{+}+\chi^{-}(X \cdot N)F^{-} \tag{44}
$$

The average deformation in the laminate is

$$
\bar{F}=\lambda^{-}F^{-}+\lambda^{+}F^{+} \tag{45}
$$

By construction, this deformation field is weakly compatible and, consequently, there is a continuous displacement field $\varphi$ whose gradient is $F$ almost everywhere.

Following Kohn (Kohn, 1991), a laminate of rank — $r$ is a layered mixture of two rank — $(r-1)$ laminates, which affords an inductive definition of laminates of any rank. As noted by Kohn (Kohn, 1991): the construction of sequential laminates presumes a separation of scales: the length scale $l_r$ of the $r$th-rank layering satisfies $l_r < l_{r-1}$. Treatments of sequential lamination may be found in (Kohn and Strang, 1986a,b,c; Bhattacharya 1991, 1992; Kohn, 1991; Pedregal, 1993).

Sequential laminates have a binary tree structure. The nodes of the tree are occupied by deformations $F_i$, $i=1,\dots, N$, where $N$ is the number of nodes, or order, of the tree. The root deformation is the average or macroscopic deformation $\bar{F}$. Each node in the tree has either two children or none at all. Nodes with a common parent are called siblings. Nodes without children are called leaves. Nodes which are not leaves are said to be interior nodes. We shall denote by $\mathscr{I}$ and $\mathscr{L}$ the sets of internal nodes and leaves of a tree, respectively. The deformations of the children of node $i$, will be denoted $F_i^{\pm}$. Each generation is called a level. The root occupies level 0 of the tree. The number of levels is the rank $r$ of the tree. Level $l$ contains at most

$2^1$ nodes. The example in Fig. 1a represents a rank-three laminate of order eleven. The leaves of the tree are nodes 6 to 11. The children of, e.g., node 2 are nodes 4 and 5, with $F_2^-=F_4$ and $F_2^+=F_5$. The sequential laminate defined by the tree is shown in Fig. 1b. As is evident, from this example, physically the leaves of the tree correspond to simple lamellae undergoing uniform deformation, whereas interior nodes correspond to complex lamellae.

The deformation $F_i$ of an internal node $i$ is an average of the deformations $F_i^\pm$ of its children, i.e.,
$$
F_i=\lambda_i^-F_i^-+\lambda_i^+F_i^+, \quad i \in \mathscr{I} \tag{46}
$$
where $o\lambda_i^\pm<1$ are the volume fractions occupied by each of the children. The volume fractions are subject to the constraint

![](./images/811194403078012928_2.jpg)

Fig. 1. A sequential laminate with nine kinematical degrees of freedom.

$$
\lambda_{i}^{-}+\lambda_{i}^{+}=1, \quad i \in \mathscr{I}
\tag{47}
$$

It, therefore follows that the deformation $F_{i}$ of an $l$-level node is the average deformation of a $(r-l)$-rank laminate. Additionally, siblings must be rank-one compatible, i.e.,

$$
F_{i}^{+}-F_{i}^{-}=a_{i} \otimes N_{i}, \quad i \in \mathscr{I}
\tag{48}
$$

for some vectors $a_{i}$ and $N_{i},|N_{i}|=1$. The latter vector is the unit normal to the interface between the children of node $i$ in the underformed configuration. It follows from Eqs. (46)-(48) that the deformations of the children of interior node $i$ are

$$
F_{i}^{-}=F_{i}-\lambda_{i}^{+} a_{i} \otimes N_{i}
\tag{49}
$$

$$
F_{i}^{+}=F_{i}+\lambda_{i}^{-} a_{i} \otimes N_{i}
\tag{50}
$$

Applying this relation recursively, the deformation in all the nodes may be computed from the deformation $\bar{F}$ of the root, or average macroscopic deformation, and the variables $\{a_{i}, N_{i}, \lambda_{i}^{ \pm}, i \in \mathscr{I}\}$.

The dislocation structure corresponding to a laminate follows directly from Nye's formula Eq. (28). It is found from this formula that the dislocation structure consists of multipolar dislocation walls separating the lamellae in the laminate. Thus, let $F_{i}^{\mathrm{p} \pm}$ be the plastic deformations corresponding to two siblings meeting at the planar interface $X \cdot N_{i}=C$. Then, the dislocation density on the interface follows from Eq. (28) as

$$
A_{i}=\left[F_{i}^{\mathrm{p}}\right] \times N_{i} \delta\left(X \cdot N_{i}-C\right), \quad i \in \mathscr{I}
\tag{51}
$$

which shows that the interface is a dislocation wall. For instance, consider the case of two leaves deforming in single slip. Then, the corresponding interfacial dislocation structure consists of two sets of parallel straight dislocations in each of the slip systems operating within the leaves, i.e., the interface is a dipolar wall (Ortiz and Repetto, 1999).

## 7. The local theory

We begin by considering the limit $\epsilon \to 0$ of problem Eq. (38). Mathematically, the limiting effective energy corresponds to the so-called $\gamma$-limit, of $\Phi_{n}$ (de Giorgi, 1975; de Giorgi and Franzoni, 1975; Modica, 1987; Sternberg, 1988). As expected, this limiting form of the theory suffices to determine many of the salient features of the evolving dislocation structures, such as the orientation and nesting of the dislocation walls, misorientations across the walls, patterns of slip activity, and others. In subsequent sections we turn to the nonlocal extension of the theory obtained by the consideration of the self-energy of the dislocations. The nonlocal theory enables the prediction of the thickness of the lamellae, the relation of such thicknesses to the grain size, and the dependence of the effective behavior on the grain size, among other features which lie outside the scope of the local theory.

The stresses $P_{i}$ in the leaves $i \in \mathscr{S}$ follow directly from the incremental constitutive

relations Eq. (38). The effective stresses in the interior nodes then follow recursively by the relation:

$$P_{i}=\lambda_{i}^{-} P_{i}^{-}+\lambda_{i}^{+} P_{i}^{+}, \quad i \in \mathscr{T} \tag{52}$$

The stress thus obtained at the root, of tree is the macroscopic or effective stress $\bar{P}$. The incremental strain energy of the tree is

$$\bar{W}_{n}(\bar{F} ;\{a_{i}, N_{i}, \lambda_{i}^{ \pm}, i \in \mathscr{T}\}) \sum_{i \in \mathscr{S}} v_{i} \bar{W}_{i, n}(F_{i}) \tag{53}$$

where $v_{i}$ are the volume fractions of the leaves. These volume fractions satisfy the constraint

$$\sum_{i \in \mathscr{S}} v_{i}=1 \tag{54}$$

Minimization of $\bar{W}_{n}$ with respect to the polarization vectors $\{a_{i}, i \in \mathscr{T}\}$, taking constraints Eqs. (46)-(48) into account, yields the traction equilibrium equations for the interior nodes:

$$t_{i} \equiv \frac{\partial \bar{W}_{n}}{\partial a_{i}}=(P_{i}^{+}-P_{i}^{-}) \cdot N_{i}=0, \quad i \in \mathscr{T} \tag{55}$$

where $t_{i}$ is the unbalanced traction across the interface corresponding to interior node $i$. For given $\bar{F}$ and fixed values of the variables $\{N_{i}, \lambda_{i}^{ \pm} A, i \in \mathscr{T}\}$, Eq. (55) defines a system of nonlinear equations which may be solved for the amplitudes $\{a_{i}, i \in \mathscr{T}\}$, e.g., by recourse to a local Newton-Raphson iteration.

In principle, the variables $\{N_{i}, \lambda_{i}^{ \pm}, i \in \mathscr{T}\}$ which define the geometry of the laminate could also be optimized at every time step. However, the mobility of dislocation walls in crystals, once formed, appears to be small. We therefore assume that the values of the geometrical variables $\{N_{i}, \lambda_{i}^{ \pm}\}$ are set when leaf $i$ becomes unstable and branches into two new leaves, and remain unchanged thereafter. By virtue of this assumption, $\{a_{i}, i \in \mathscr{T}\}$ represents the complete collection of microstructural deformation degrees of freedom which the material has at its disposal in addition to the macroscopic deformation $\bar{F}$. At equilibrium, i.e., when the internal degrees of freedom $\{a_{i}, i \in \mathscr{T}\}$ satisfy Eq. (55) one has

$$\bar{P}=\frac{\partial \bar{W}_{n}}{\partial \bar{F}} \tag{56}$$

i.e., $\bar{W}_{n}$ furnishes a potential for the macroscopic stress-strain relations.

The geometrical variables $\{N_{i}, \lambda_{i}^{ \pm}, i \in \mathscr{T}\}$ may be determined as follows. Assume that, a leaf $i$ becomes unstable at time $t_{n}$ and branches into two children with volume fractious $\lambda_{i}^{ \pm}$ separated by a dislocation wall of normal $N_{i}$. The incremental strain energy density of the leaf is

$$\bar{W}_{i, n}(F_{i}, a_{i}, N_{i}, \lambda_{i}^{ \pm})=\lambda_{i}^{-} W_{i, n}(F_{i}^{-})+\lambda_{i}^{+} W_{i, n}(F_{i}^{+}) \tag{57}$$

It should be noted that both incipient, leaves are at the same state at time $t_{n}$. Taking

constraints Eqs. (46)-(48) into account, the optimality conditions for the geometrical variables $\{N_{i}, \lambda_{i}^{ \pm}\}$ are found to be

$$
\frac{\partial \bar{W}_{i, n}}{\partial \lambda_{i}^{-}}=\left[W_{n}\right]-P_{i} \cdot\left(a_{i} \otimes N_{i}\right)=0
\tag{58}
$$

$$
\frac{\partial \bar{W}_{i, n}}{\partial N_{i}}=\left(a_{i} \cdot\left[P_{i}\right]\right) \times N_{i}=0
\tag{59}
$$

where $P_{i}$ is computed from the stresses in the leaves in accordance with Eq. (52). Evidently, Eq. (58) is the configurational force conjugate to the position of the interfaces, which may be computed directly from Eshelby's energy-momentum tensor (Abeyaratne and Knowles, 1990). Likewise, Eq. (58) represents the configurational force conjugate to the orientation of the dislocation walls. Eqs. (58) and (59) define a system of nonlinear equations which, in conjunction with the equilibrium Eq. (55), can be solved for the unknowns $\{a_{i}, N_{i}, \lambda_{i}^{ \pm}\}$. A nontrivial solution is obtained, signaling the formation of two new leaves, when $0<\lambda_{i}^{ \pm}<1$ and

$$
\bar{W}_{i, n}<W_{i, n}\left(F_{i}\right)
\tag{60}
$$

i.e., when the process of branching reduces the incremental work of deformation.

The geometrical parameters $\{N_{i}, \lambda_{i}^{ \pm}, i \in \mathscr{I}\}$ may be estimated — and the solution procedure just described may be simplified — by recourse to linearization, leading to a conventional Hill-Hadamard stability analysis of the leaves. We begin by linearizing the incremental strain energy of the leaf $i$ under consideration, with the result

$$
W_{i, n}\left(F_{i}\right)=P_{i, n} \cdot\left(F_{i}-F_{i, n}\right)+\frac{1}{2}\left(F_{i}-F_{i, n}\right) \cdot c_{i, n} \cdot\left(F_{i}-F_{i, n}\right)+o\left(\left|F_{i}-F_{i, n}\right|^{2}\right)
\tag{61}
$$

where

$$
c_{i, n}=\left[\frac{\partial^{2} W_{i, n}}{\partial F_{i} \partial F_{i}}\right]_{F_{i}=F_{i, n}}
\tag{62}
$$

are the tangent moduli for leaf $i$ at time $t_{n}$. These moduli are also referred to as algorithmic moduli since their definition requires a time discretization of the constitutive equations. Explicit expressions of the tangent moduli for various constitutive updates and material models may be found in (Cuitiño and Ortiz, 1992a; Ortiz and Stainier, 1999). It should be noted that the definition Eq. (62) of the tangent moduli allows for general material behavior, including rate-dependency. In the rate-independent limit, the Hill-Hadamard analysis may be based on the material tangent moduli which relate the rate of deformation $\dot{F}$ to the stress rate $\dot{P}$. Here again, explicit, expressions of the material tangent, moduli for a variety of rate-independent plasticity models are available from the literature (e.g., Asaro and Rice, 1977; Asaro, 1983).

Using the quadratic approximation Eq. (61), representation Eqs. (49) and (50) and constraint, Eq. (47), the resulting incremental strain-energy density of the leaf $i$ is found to be

$$
\bar{W}_{i, n}-W_{i, n}\left(F_{i}\right)=\frac{1}{2} \lambda_{i}^{-} \lambda_{i}^{+}\left(a_{i} \otimes N_{i}\right) \cdot c_{i, n}\left(N_{i}\right) \cdot\left(a_{i} \otimes N_{i}\right)+o\left(\left|F_{i}-F_{i, n}\right|^{2}\right)
\tag{63}
$$

Introducing the acoustic tensor $D_{i, n}(N_{i})$ corresponding to the moduli $c_{i, n}$ and the normal $N_{i}$ through the identity

$$
\left(a_{i} \otimes N_{i}\right) \cdot c_{i, n}\left(N_{i}\right) \cdot\left(a_{i} \otimes N_{i}\right)=a_{i} \cdot D_{i, n}\left(N_{i}\right) \cdot a_{i}
\tag{64}
$$

Eq. (63) further simplifies to

$$
\bar{W}_{i, n}-W_{i, n}\left(F_{i}\right)=\frac{1}{2} \lambda_{i}^{-} \lambda_{i}^{+} a_{i} \cdot D_{i, n}\left(N_{i}\right) \cdot a_{i}+o\left(\left|F_{i}-F_{i, n}\right|^{2}\right)
\tag{65}
$$

It follows from this expression that, to first order in the incremental deformation, the bifurcation condition Eq. (60) requires that the acoustic tensor $D_{i, n}(N_{i})$ becomes negative semi-definite for some direction $N_{i}$. Branching thus requires that

$$
\operatorname{det}[D_{i, n}(N_{i})]=0
\tag{66}
$$

which is the classical Hill-Hadamard localization condition (Asaro and Rice, 1977). Within this approximation, a leaf branches into two new leaves when Eq. (66) is satisfied for some direction $N_{i}$, which thereafter defines the orientation of the dislocation wall separating the new leaves. As soon as the acoustic tensor becomes negative definite, Eq. (65) develops a minimum with respect to the volume fractions $\lambda_{i}^{ \pm}$ at

$$
\lambda_{i}^{-}=\lambda_{i}^{+}=\frac{1}{2}
\tag{67}
$$

i.e., the new leaves occupy identical volume fractions. Indeed, many of the observed lamellar structures are composed of ostensibly uniform lamellae (Hughes and Hansen 1991, 1993; Bay et al., 1992; Hansen and Hughes, 1995; Rosen et al., 1995), which would appear to bear out the quadratic approximation. Evidently, it, follows from Eq. (67) that microstructures composed of grossly dissimilar lamellae cannot be adequately described by the quadratic approximation Eq. (61) and consequently, are not, amenable to a Hill-Hadamard analysis. In such cases, the fully nonlinear stability analysis Eqs. (58) and (59) must be carried out instead. It bears emphasis that, in all cases, the determination of the degrees of freedom $\{a_{i}, \ i \in \mathscr{A}\}$ requires a fully nonlinear analysis. (Box 1 and 2)

We conclude this section by addressing a few matters of implementation. The solutions of the Hill-Hadamard condition Eq. (66) may be obtained by parameterizing the normal $N_{i}$, in terms of spherical angles (see e.g., Ortiz et al., 1987; Leroy and Ortiz 1989, 1990; Nacar et al., 1989). We begin by sweeping the unit sphere at, regular intervals of the spherical angles and determining the points where $\operatorname{det}[D_{i, n}(N_{i})]$ attains a local minimum relative to its neighbors on the grid. The precise minimizers of $\operatorname{det}[D_{i, n}(N_{i})]$ are then pin-pointed by a Newton-Raphson iteration. The resulting directions are deemed admissible if the corresponding value of $\operatorname{det}[D_{i, n}(N_{i})]$ is below a small positive tolerance. The absolute minimizer among all the local

Box 1. Recursive algorithm for the calculation of the deformations, stresses
and unbalanced tractions of a laminate.
```
type tree_node = record
    LChild: tree_node;
    RChild: tree_node;
    $\lambda$: real;
    $a$: real[1..$d$]; {$d$ is the spatial dimension}
    $N$: real[1..$d$];
    $F$: real[1..$d$] [1..$d$];
    $P$: real[1..$d$] [1..$d$];
    $c$: real[1..$d$] [1..$d$] [1..$d$] [1..$d$];
end

procedure update_tree (root: tree_node)
begin
    update_node (root);
end

procedure update_node (node: tree_node)
begin
    if (node. LChild=nil and node.RChild=nil) then
        constitutive_update (node.$F$,node.$P$,node.$c$);
    else
        lchild := node.LChild;
        rchild := node.RChild;
        lchild.$F$:= node.$F$+rchild.$A$*node.$a$ $\otimes$ node.$N$;
        rchild.$F$:= node.$F$-lchild.$A$*node.$a$ $\otimes$ node.$N$;
        update_node(lchild);
        update_node(rchild);
        node.$P$:= lchild.$X$*lchild.$P$+rchild.$A$*rchild.$P$;
        node.$t$:= (rchild.$P$-lchild.$P$).node.$N$;
    end if
end
```

minima is then selected as the direction $N_i$ of the new interface. If the absolute minimizer is not unique, one of the minimizers is selected at random.

As noted above, by virtue of the fact, that the geometrical parameters $\{N_i$, $\lambda_i^\pm$, $i \in \mathscr{I}\}$ are held fixed, the equilibrium equations Eq. (55) become a system of non-linear equations for the variables $\{a_i$, $i \in \mathscr{I}\}$. A flow chart for the calculation of $t_i(\{a_i$, $i \in \mathscr{I}\}$ is given in list 1. The recursive character of the calculations, which permits a particularly simple aid efficient, implementation of the theory, is noteworthy. We

Box 2. Recursive algorithm for the calculation of the Hessian matrix of
the equilibrium equations.

```
procedure tangent-tree (root: tree_node, T: real[1..d] [1..N] [1..d] [1..N])
begin
{N is the number of interior nodes}
  root.dF:= 0 ;
  for n:= 1 to N do
      node_of_index (n) .da := 0;
  end do
  for n:= 1 to N do
      node:= node_of_index (n) ;
      for j:= 1 to d do {assign node . da to unit vectors}
          node . da := e_j;
          tangent_node (root);
          for m:= 1 to N do
              for i:= 1 to d do
                  T[i] [m] [j] [n]:= node_of_index (m).dt [i];
              end do
          end do
          node.da:= 0;
      end do
  end do
end

procedure tangent_node (node: tree_node)
begin
    if (node. LChild=nil and node. RChild=nil) then
      node.dP:= node.c:node.dF;
    else
      lchild:= node.LChild;
      rchild:= node.RChild;
      lchild.dF:= node.dF + rchild.λ*node.du⊗node.N;
      rchild.dF:= node.dF - lchild.λ*node.du⊗node.N;
      tangent_node (lchild);
      tangent_node (rchild);
      node.dP:= lchild.λ*lchild.dP+rchild.λ*rchild.dP;
      node.dt:= (rchild.dP-lchild.dP). node.N;
    end if
end
```

solve system Eq. (55) by a Newton–Raphson interaction. A flow chart for the calcu- lation of the requisite tangent matrix

$$
T_{i j}=\frac{\partial t_{i}}{\partial a_{j}}
\tag{68}
$$

which follows directly from the tangent moduli $\{c_{i, n}, i \in \mathscr{I}\}$, is shown in list 2. In order to ensure the convergence of the Newton–Raphson iteration, we make use of a line search algorithm based on bisection followed by a secant iteration.

We have found that the application of the procedure just outlined may in some cases lead to a proliferation of low-angle subgrain boundaries. This proliferation occurs when the Hill–Hadamard condition Eq. (66) is enforced with some finite tolerance, i.e., a leaf branches whenever the determinant of the acoustic tensor is below some small — but positive — prescribed value. The same condition may then be satisfied by each of the children in the next time step, and so on, resulting in runaway branching. In order to ensure that branching is physical, we impose an additional threshold condition. Thus we assume that, for a leaf to be able to branch, the dislocation walls which bound the leaf must be sufficiently ‘well-developed’. A dislocation wall is presumed to be well-developed when it acts as an effective barrier to dislocations moving within the leaves, i.e., when the critical stress $\tau_{\mathrm{c}}^{\mathrm{wall}}$ for a dislocation to cross the wall is larger than the critical stress for the same dislocation to move within the abutting leaves. Since $\tau_{\mathrm{c}}^{\mathrm{wall}}$ may be expected to scale with the square root, of the dislocation density $\rho^{\text {wall }}$ within the wall, and $\rho^{\text {wall }}$, according to Eq. (51), in turn scales with $\left|\left[F^{\mathrm{p}}\right] \times N\right|$, we simply require that, for branching to occur in a leaf, the corresponding value of $\left|\left[F^{\mathrm{p}}\right] \times N\right|$ exceed a small threshold value.

## 8. Examples of application of the local theory

We proceed to illustrate the range of behaviors predicted by the local theory by way of selected examples. In order to emphasize that the proposed construction can be wrapped around any existing single-crystal plasticity model, we have based the calculations reported here on the model of Hutchinson (Hutchinson, 1976) and Pierce et al. (Pierce et al., 1982), Eqs. (20) and (21). The constitutive updates are carried out, using the implicit procedure of Cuitiño and Ortiz (Cuitiño and Ortiz, 1992a). The values of the material constants adopted in the calculations are roughly represen- tative of an Al–Cu alloy, (Asaro, 1983; Chang and Asaro, 1981). The elastic con- stants are: $c_{11}$=168.4 GPa, $c_{12}$=121.4 GPa and $c_{44}$=75.4 GPa. The initial critical resolved shear stress is $\tau_{0}$=100 MPa and the saturation value of the critical resolved shear stress is $\tau_{\mathrm{S}}$=180 MPa. The latent hardening constant is $q$=1.4. All calculations correspond to quasistatic loading.

The crystal is deformed in simple shear on a plane of normal $\bar{m}$ in the direction $\bar{s}$. Thus, the prescribed macroscopic deformation is

$$
\bar{F}=I+\bar{\gamma} \bar{s} \otimes \bar{m}
\tag{69}
$$

where $\bar{\gamma}$ is the macroscopic shear strain. The work conjugate stress measure is the resolved shear stress

$$
\bar{\tau}=\bar{P} \cdot(\bar{s} \otimes \bar{m})
$$

acting on plane $\bar{m}$ in the direction $\bar{s}$. This mode of deformation is motivated by the experiments of Hughes et al. (1994), who investigated the formation of a contact boundary layer in blocks of copper sliding over steel plates. In the grains within the contact boundary layer, the nominal mode of deformation is the form Eq. (69). Assuming that, the grains are randomly oriented initially, the directions $\bar{s}$ and $\bar{m}$ may themselves be chosen randomly relative to the crystallographic axis.

We begin by considering the simple case of shear on the (001) plane along the [110] face diagonal. In the finite deformation regime, with lattice rotations taken into account, this deformation results in the activation of the systems A6 and D6. Here and henceforth we adopt, the Schmidt-Boas nomenclature for the sip systems of fee crystals, see Table 1 stress-strain curves are shown in Fig. 2. In the absence of microstructure formation, the crystal deforms in double slip by the simultaneous activation of the systems A6 and D6. In the presence of latent, hardening, which in the model under consideration corresponds to the regime $q>1$, this process of double slip in turn results in a high rate of hardening.

![](./images/811194403078012928_3.jpg)

Fig. 2. Stress-strain curves for a fcc crystal subjected to simple shear on the (001) plane in the [110] direction, showing the softening of microstructure development. The curves are obtained using Hutchinson (Hutchinson, 1976) and Pierce et al. (Pierce et al., 1982) model of hardening, with material constants representative Al-Cu alloys (Asaro, 1983; Chang and Asaro, 1981).

When the formation of microstructure is allowed for through the sequential lami- nation construction described in the foregoing, the deformation field becomes inhomogeneous immediately after first yield. The microstructure that develops con- sists of a simple laminate, with each variant, deforming in single slip by the activation of one of the systems A6 or D6. These variants are separated by dipolar dislocation walls of normal $N=\{-1/\sqrt{2},1/\sqrt{2},0\}$. The formation of this microstructure results in a significant relaxation of the stress-strain response, Fig. 2. A marked reduction in the rate of hardening following the inception of dislocation structures such as con- sidered here is observed experimentally in many crystals (Zehetbauer and Seumer, 1993; Les et al., 1996).

A second example which leads to the development of a somewhat more complex microstructure concerns the case of a crystal such as described above subjected to simple shear on the plane $\bar{m}=(0.314485,-0.104828,0.943456)$ along direction $\bar{s}$ =[0.929270, -0.168905, -0.328524], corresponding to a randomly chosen orien- tation of the crystal. The computed $\bar{\tau}-\bar{\gamma}$ stress-strain curves and the evolution of the microstructure are shown in Fig. 3. The crystal first yields by the activation of the four systems D6, C1, B5 and A2. Soon thereafter, at a strain $\bar{\gamma}=0.7 \times 10^{-2}$, a rank

![](./images/811194403078012928_4.jpg)

Fig. 3. Stress-strain curves for a fcc crystal subjected to simple shear on the (0.314485, -0.104828,0.943456) plant in the [0.929270, -0.168905, -0.328524] direction (selected at random), showing the development of microstructure in the form of a rank-3 laminate and the attendant relaxation of the stress- strain response. The curves are obtained using Hutchinson (Hutchinson, 1976) and Pierce et al. (Pierce et al., 1982) model of hardening, with material constants representative Al-Cu alloys (Asaro, 1983; Chang and Asaro, 1981).

1 laminate forms. The microstructure consists of two lamellae separated by a dislocation wall of normal $N_1=\{-0.13595, 0.00797, 0.99068\}$. One of the two lamellae retains the full complement of active systems, D6, C1, B5 and A2, whereas only the three systems C1, B5 and A2 are active in the remaining lamella. This reduction in the number of active slip systems over part of the volume of the crystal confers the laminate an energetic advantage in the presence of strong latent, hardening.

At the strains $\bar{\gamma}=1.7 \times 10^{-2}$ and $\bar{\gamma}=3.1 \times 10^{-2}$, the right leaf of the first, rank-1 laminates goes through two successive branching events, resulting in the first stable rank-3 laminate shown in Fig. 3. The computed orientations of the three families of dislocation walls which bound the leaves of the tree are $N_1=\{-0.13595, 0.00797$, $0.99068\}, \quad N_2=\{-0.03532, \quad 0.99923, \quad 0.01697\}$ and $N_3=\{-0.71477, \quad 0.03864$, $0.69829\}$. As may be seen from Fig. 3, the leaves in the right branch of the tree exhibit the same slip activity pattern and are separated by low-angle subgrain boundaries. By contrast, the misorientation between the main two branches of the tree measured by the relative angle of rotation between their respective crystalline lattices, grows comparatively quickly and reaches 14 degrees at $\bar{\gamma}=0.5$. This angle is in the experimentally observed range of 5 to 20 degrees reported by Hughes and Hansen (Hughes and Hansen, 1993) for nickel deformed by rolling from intermediate to large strains. As is evident from Fig. 3, the net effect, of the microstructure is to significantly relax the response of the crystal. The ability of the present theory to generate physically meaningful microstructures automatically and to determine the effect of such microstructures on the effective response of the crystal is noteworthy.

## 9. The nonlocal theory

The local theory developed so far has the ability to predict salient features of subgrain microstructures such as the orientation and nesting of the dislocation walls, misorientations across the walls, patterns of slip activity, and others. However, the local theory is incapable of according well-defined sizes to microstructural features. In particular, the thickness of the lamellae and the dependence of such thicknesses and the effective behavior on grain size are outside the scope of the local theory.

In order to overcome these limitations, we turn to problem Eq. (38) with finite $\epsilon$, i.e., with the self-energy of the dislocations taken into account. The construction which we propose in order to estimate $\bar{W}_n$ is similar to that applied by Ball and James (Ball and James, 1987) to martensite. Thus, we retain the tree geometry $\{N_i$, $\lambda_i^{ \pm}, i \in \mathscr{I}\}$ of the dislocation structures predicted by the local theory. However, we now account explicitly for two additional items in the energy budget of the crystal: the energy contained within the transition or boundary layers which separate complex lamellae; and the self-energy of the dislocations contained in the dislocation walls. As pointed out, by Ball and James (Ball and James, 1987) in the context of martensite the competition between these two types of energy endows the microstructure with well-defined dimensions. It should be noted that Muller and Kohn (Kohn and Müller, 1992) found that, for some model systems, this construction may not be optimal. Indeed, interfacial energy may change the topology of the microstructure, e.g., by inducing twin branching.

The presence of transition or boundary layers between complex lamellae in the microstructure is necessitated by the fact, that the compatibility relations Eq. (48), when applied to interior nodes of the tree, enforce compatibility *on average* only. Thus, deformations $F_{i}^{\pm}$ corresponding to two adjacent interior nodes represent average deformations of all their children, and Eq. (48) merely requires the compatibility of those average deformations. Under those conditions, the actual deformation field is bound to exhibit transition or boundary layers at the interfaces between interior nodes, i.e., between lamellae of rank one or higher. These boundary layers in turn cost energy and have been argued to be a factor determinant of the arrangement and separation of the dislocation walls (Kuhlmann-Wilsdorff and van der Merwe, 1982; Bay et al., 1992).

We proceed to estimate this energy by explicitly constructing a kinematically admissible deformation field. Alternative constructions may be based on interpolation (Chipot and Kinderlehrer, 1988). Owing to the variational character of the incremen- tal problem, the energy of the kinematically admissible field on which we base our construction is a — hopefully tight — upper bound on the actual energy. We consider an interior node $i$ of size $l_{i}$ and deformation $F_{i}$. The children of the node are two leaves of deformations $F_{i}^{\pm}$ and volume fractions $\lambda_{i}^{\pm}$ separated by a dislocation wall of normal $N_{i}$, Fig. 4. The distances between such walls which equal the sizes of the children are

![](./images/811194403078012928_5.jpg)

Fig. 4. Assumed structure of the boundary layer between interior node $i$ and adjacent lamellae. Figure shows a normal cross section of the node $i$, i.e., the dislocation walls separating the children of node $i$ are perpendicular to the plane of the figure.

$$
l_{i}^{ \pm}=\lambda_{i}^{ \pm} l_{i}^{\mathrm{c}}
\tag{71}
$$

where

$$
l_{i}^{\mathrm{c}}=l_{i}^{-}+l_{i}^{+}
\tag{72}
$$

is the combined thickness of the leaves. Evidently, $l_{i}^{-}=l_{i}^{+}$if $\lambda_{i}^{-}=\lambda_{i}^{+}$, as is the cast in the quadratic approximation Eq. (61). Adjacent to the node $i$ lies the sibling node $j$. The geometry of the assumed kinematically admissible field is similar to that con- sidered by Ball and James (Ball and James, 1987). Fig. 4 shows a normal cross section of the lamella $i$ showing the assumed boundary-layer structure. Within this normal cross section, the transition between $i$ and the adjacent lamellae is effected through regions in the shape of right triangles. The deformation $F_{i}^{\mathrm{BL}}$ in such regions is of the form

$$
F_{i}^{\mathrm{BL}}=F_{i}+a_{i} \otimes N_{i}^{\mathrm{BL}}
\tag{73}
$$

where, with reference to Fig. 4,

$$
N_{i}^{\mathrm{BL}}=-\lambda_{i}^{+} \frac{N_{i} \cdot r_{i}^{-}}{\left|r_{i}^{-}\right|^{2}} r_{i}^{-}+\lambda_{i}^{-} \frac{N_{i} \cdot r_{i}^{+}}{\left|r_{i}^{+}\right|^{2}} r_{i}^{+}
\tag{74}
$$

Here, the vectors $r_{i}^{ \pm}$are aligned with the sides of the boundary-layer triangles and contained within the normal cross section of the node, Fig. 4. It should be noted that, since these triangles are chosen to be straight, $r_{i}^{ \pm}$are orthogonal. In addition, since $r_{i}^{ \pm}$are contained within the normal cross section of node $i$, one has $(r_{i}^{-} \times r_{i}^{+}) \cdot N_{i}=0$ and $(r_{i}^{-} \times r_{i}^{+}) \cdot N_{i}^{\mathrm{BL}}=0$. It follows from Eq. (73) that the deformation $F_{i}^{\mathrm{BL}}$ of the boundary layer is entirely determined by the average deformation $F_{i}$ of the node and by the vector $a_{i}$. In particular, $F_{i}^{\mathrm{BL}}=F_{i}$ if $a_{i}=0$. Therefore, consideration of boundary layers does not increase the number of microscopic degrees of freedom relative to the local theory. It, is readily verified that,

$$
F_{i}^{\mathrm{BL}} \cdot r_{i}^{ \pm}=F_{i}^{ \pm} \cdot r_{i}^{ \pm}
\tag{75}
$$

$$
F_{i}^{\mathrm{BL}} \cdot\left(r_{i}^{-}+r_{i}^{+}\right)=F_{i} \cdot\left(r_{i}^{-}+r_{i}^{+}\right)
\tag{76}
$$

and

$$
F_{i}^{\mathrm{BL}} \cdot\left(r_{i}^{-} \times r_{i}^{+}\right)=F_{i}^{ \pm} \cdot\left(r_{i}^{-} \times r_{i}^{+}\right)
\tag{77}
$$

$$
F_{i}^{\mathrm{BL}} \cdot\left(r_{i}^{-} \times r_{i}^{+}\right)=F_{i} \cdot\left(r_{i}^{-} \times r_{i}^{+}\right)
\tag{78}
$$

which establishes the kinematic admissibility of $F_{i}^{\mathrm{BL}}$. Under these conditions, an upper hound to the incremental strain-energy density of the lamella is given by:

$$
\bar{W}_{i, n}=\left(1-\lambda_{i}^{\mathrm{BL}}\right)\left[\lambda_{i}^{-} W_{i, n}^{-}\left(F_{i}^{-}\right)+\lambda_{i}^{+} W_{i, n}^{+}\left(F_{i}^{+}\right)\right]+\lambda_{i}^{\mathrm{BL}} W_{i, n}^{\mathrm{BL}}\left(F_{i}^{\mathrm{BL}}\right)
\tag{79}
$$

where

$$
\lambda_{i}^{\mathrm{BL}}=C_{i}^{\mathrm{BL}} \frac{l_{i}^{\mathrm{c}}}{l_{i}}
\tag{80}
$$

is the volume fraction of the boundary layer. The constant, $C_{i}^{\mathrm{BL}}$ is of order 1 and

depends on the the orientation and relative thicknesses of the the leaves. For instance, $C_i^{BL=1 in the case of leaves of equal thickness. As is evident from Eq. (80, $\lambda_i^{BL and, by extension, the boundary-layer contribution to the incremental strain-energy density of the the node, scale with the combined width $ l_i^^ of the leaves.

Next, we proceed to estimate the energy of the dislocation walls separating the leaves. For simplicity, we shall assume separation of scales, i.e., $ l_i^^ < l_i.. Under these conditions, the dominant, contribution to the wall energy per unit volume is:

$$
\bar{ W_{_{,,n^{walls=rac{8\ \^{2\\Gamma}{ $ l_i^^|[[ F_i^^] imes N_i|
 tag{81)
$$

 where $\Gamma and $\ are given by Eqs. (33) and ( (34, respectively. Evly, the wall energy density $\bar W_{_{,,n^{walls scales in inverse proportion to the combined thickness $ l_i^^ of the leaves.

The total energy density of the node $i in the nonlocal theory now follows as

$$
\bar W_{_{,n^((1-\ lambda_i^{BL)[[\lambda_i^-\ W_{_{,n^(F_i^-)+\lambda_i^+\ W_{_{,n^(F_i^+)]]+\\ambda_i^{BL\ W_{_{,n^{BL(F_i^{BL)+\\bar W_{_{,n^{walls
 tag{82)
$$

The optimal size of the the leaves follows by minimization of $\bar W_{_{,n^with respect to $ l_i^^. Such optimal value is is the result of the competition between the boundary layer energy, which drives $ l_i^^ down, i.e, promotes fine microstructure, and the dislocation wall energy, which drives $ l_i^^ up, thus decreasing the number of walls per unit volume. The result is

$$$
 l_i^=\left\left(rac{8\\Gamma|[[ F_i^] imes N_i| l_i}{C_i^{BL(W_{_{,n^{BL-\\bar W_{_{,n))\rightright^{1//2
 	ag(83)
$$

 where $\ $\bar W_{_{,n is given by Eq. (57). The scaling law Eq. (83 results in equdistribution of the boundary layer and dislocation wall energies, i.e,,

$$
\\bar W_{_{,n^{walls=((\bar W_{_{,n^{BL-\\bar W_{_{,n)\)\lambda_i^{BL
 tag((84)
$$

Using this relation, the total energy Eq. (82 may be written in in the form::

$$
\\bar W_{_{,n^(((1-2\\lambda_i^{BL)[[\lambda_i^-\ W_{_{,n^(F_i^-)+\\lambda_i^+\ W_{_{,n^(F_i^+)]]+2\\\ambda_i^{BL\ W_{_{,n^{BL(F_i^{BL))
 	ag(85))
$$

 which obviiates the need for computing the dislocation wall energy explicitly.

The size of the entire microstructure, i.e,, the value of $ l_i when $i is is the root of the tree, is identified with the grain size $ d, and is presumed known. The size optimization given by Eq. ( (83 applies to the leaves of the tree only, and the size of the interior nodes is kept constant and equal to their value at the moment of their becoming interior, i.e.: at the time of their branching into leaves. As the macroscopic defor- mation is increased monotonically, the interior boundary layers are expected to harden rapidly, leading to a monotonic. reduction of the size $ l_i^^ of the leaves in accordance with Eq. (83.. In view of the limited mobility of the dislocation walls, this process of refinement may be expected to occur by the addition of new walls and not by the shifting of existing ones (Hansen,  (1992.

It is interesting to note that the scaling relation Eq. (83) implies

$$
l_{i}^{\mathrm{c}} \sim \sqrt{b l_{i}}
\tag{86}
$$

i.e., the size of the children scales as the geometric mean of the Burgers vector length and the size of the parent. The prominent role played by the Burgers vector length as an intrinsic length-scale parameter of the theory is evident in Eq. (86). It follows from Eq. (86) that the first-level lamellae have sizes of order $\sqrt{b d}=\varepsilon d$. Likewise, the second-level lamellae have sizes of order $\sqrt{b d} \sqrt{b d}=\varepsilon^{3 / 2} d$. Applying these relations recursively it is found that the size of level-$\tau$ lamellae is of order $\varepsilon^{p} d$, with $p=2\left(1-2^{-\tau}\right)$. In particular, the size of the lamellae becomes commensurate with $b$ as $r \rightarrow \infty$, i.e., $b$ sets a lower bound for the fineness of the microstructure. It, also follows from these relations that the size of the lamellae vanishes - and the local theory is recovered - as $\epsilon \rightarrow 0$, which corresponds to the limit of infinitely large grain sizes.

In general, the nonlocal effective energies and stresses may be expected to bound above those obtained from the local theory. In particular, the response of the material may be expected to become increasingly harder with decreasing grain size $d$, in keeping with observation (Nix, 1998; Fleck et al., 1994). Microstructures are sup- pressed when they lead to energies in excess of that corresponding to a uniform deformation. This cross over from microstuctures to uniform deformations may be expected to occur for sufficiently small grain sizes. Examples illustrative of these general trends are shown in Section 10.

The nonlocal energy of the laminate follows by the addition of the energies Eq. (85) of the leaves, with the result:

$$
\bar{W}_{n}^{\varepsilon}\left(\bar{F} ;\left\{a_{i}, N_{i}, \lambda_{i}^{ \pm}, i \varepsilon \mathscr{S}\right\}\right)=\sum_{i \varepsilon \mathscr{S}} v_{i} \bar{W}_{i, n}^{\varepsilon}\left(F_{i}\right)
\tag{87}
$$

The equilibrium equations for the laminate follow in the form:

$$
t_{i}^{\varepsilon}=\frac{\partial \bar{W}_{n}^{\varepsilon}}{\partial a_{i}}=0
\tag{88}
$$

At equilibrium, the macroscopic stress-strain response of the crystal is given by

$$
\bar{P}^{\varepsilon}=\frac{\partial \bar{W}_{n}^{\varepsilon}}{\partial \bar{F}}
\tag{89}
$$

This expression may be evaluated by a recursive application of the averaging rule

$$
P_{i}=\left(1-2 \lambda_{i}^{\mathrm{BL}}\right)\left[\lambda_{i}^{-} P_{i}^{-}+\lambda_{i}^{+} P_{i}^{+}\right]+2 \lambda_{i}^{\mathrm{BL}} P_{i}^{\mathrm{BL}}, \quad i \epsilon \mathscr{T}
\tag{90}
$$

which generalizes Eq. (52).

The equilibration of the tree may be effected by directly solving the equilibrium Eq. (88) for the amplitudes $\left\{a_{i}, i \epsilon \mathscr{T}\right\}$ as in the local theory. However, in cases in which there is a sharp separation of scales between the various levels of the laminate, the boundary-layer volume fractions $\lambda_{i}^{\mathrm{BL}}$ are small and the nonlocal theory may be

treated perturbatively. Then, to leading order the nonlocal energy of the laminate is given by Eq. (87), with the amplitudes $\{a_{i}, i \in \mathscr{I}\}$ set equal to those obtained from the local theory. Likewise, the nonlocal macroscopic stress-strain behavior follows from Eq. (89) with $\{a_{i}, i \in \mathscr{I}\}$ set equal to their local values. This simplifies the implementation of the nonlocal theory, as the equilibrium equations of the laminate remain identical to those corresponding to the local theory, and the nonlocal correc- tions are rendered explicit. The solution proceeds by first, equilibrating the laminate, which entails solving the local equilibrium Eq. (55) for the amplitudes $\{a_{i}, i \in \mathscr{I}\}$. The optimal sizes $\{l_{i}^{c}, i \in \mathscr{L}\}$ are then computed from Eq. (83) and the boundary-layer volume fractions $\{\lambda_{i}^{BL}, i \in \mathscr{L}\}$ follow from Eq. (80). Finally, the macroscopic stresses follow from the recursive application of Eq. (90) from the leaves up to the root of the tree.

## 10. Examples of application of the nonlocal theory

A first, illustration of the nonlocal theory is provided by the example of an fcc crystal deformed in shear on the (001) plant along the [110] face diagonal discussed in Section 8. For this example, the local theory predicts a simple laminate consisting of two variants undergoing single slip on systems A6 and D6. The geometry of this example is such that the plastic deformations in each of the variants are compatible. i.e., $[F^{p}] \times N=0$. Under these conditions, the interfaces between the lamellae are dislo- cation-free and, consequently, carry no energy. The microstructure is thus free to refine indefinitely and the local limit is attained. In particular, the theory predicts the absence of a size effect. This example serves to illustrate that the extent of the size effect may vary sharply depending on the mode of deformation and the orientation of the crystal.

Our next example stands in contrast to the one just described in that the size effect is particularly pronounced. We consider a crystal subjected to uniaxial tension along the (001) axis. For simplicity, we restrict the slip activity to the systems B2, B4, C1 and C3. The crystal then develops a microstructure in the form of a simple laminate consisting of two lamellae deforming in double slip. The pair of systems (B2, B4) operate jointly in one lamella, whereas the pair of systems (C1, C3) operate in the remaining lamella. The pair of systems (B2, B4) combine to define the effective system $s=[11 \overline{2}], m=(\overline{1} 11)$, whereas the pair (C1, C3) combine to define the effective system $s=[112], m=(\overline{1} \overline{1} 1)$. The calculations are based on Hutchinson (Hutchinson, 1976) and Pierce et al. (Pierce et al., 1982) model of hardening, with material con- stants representative of Al-Cu alloys (Asaro, 1983; Chang and Asaro, 1981). In addition, for purposes of calculation of interfacial energies, we set $C=0.1$ and $\mu=c_{44}$ in Eq. (32).

For this geometry it is found that the deformation of the boundary layer, as described in Section 9, is essentially elastic. The behavior of the boundary layer is therefore very stiff, which contributes to accentuate the size effect. The true (Cauchy) stress vs true (logarithmic) strain curves obtained for grain sizes $d=1 \mu m, 10 \mu m$, $100 \mu$, and 1 mm are shown in Fig. 5. The response predicted by the local theory,

![](./images/811194403078012928_6.jpg)

Fig. 5. Uniaxial stress-strain curves for an (001) fcc crystal showing the dependence on grain size $d$ or similar limiting feature size. The curves are obtained using Hutchinson (Hutchinson, 1976) and Pierce et al. (Pierce et al., 1982) model of hardening, with material constants representative of Al-Cu alloys (Asaro, 1983; Chang and Asaro, 1981).

which corresponds to the limit, $d \to \infty$, is also shown for reference. As expected, the response of the crystal stiffens sharply with decreasing grain size. It should be care- fully noted, however, that due to the stiffness of the boundary layer, the nonlocal stress-strain curve lies above the stress-strain curve corresponding to uniform defor- mation below a certain critical value of $d$. For grain sizes smaller than this critical size, the microstructure is suppressed altogether and the grain deforms uniformly.

The evolution of the lamella thickness with macroscopic strain is depicted in Fig.
6. As is evident from the figure, the size of the microstructure is predicted to decrease with the macroscopic strain, in keeping with observation (Bassim and Klassen, 1986; Hughes et al., 1994). More precisely, the lamella thickness $l$ is found to vary in inverse proportion to the square root, of the macroscopic true strain $\varepsilon$, i.e., $l \sim \varepsilon^{-1/2}$, in accordance with the analysis of Ortiz and Repetto (Ortiz and Repetto, 1999). The ability of the nonlocal theory to supply scaling relations such as just described is particularly noteworthy. However, it should be carefully noted that the precise value of the exponent is likely to be related to the elastic behavior of the boundary layer under the conditions of the example. Other exponents may be expected to arise in casts in which the boundary layers are more compliant and deform plastically. In addition, constructions which allow for self-similar lamella branching, such as pro- posed by Kohn and Muller (Kohn and Müller, 1992) for martensite, are likely to lead to yet, a different set of exponents.

Finally, the computed dependence of the flow stress, sampled at 50% deformation,

![](./images/811194403078012928_7.jpg)

Fig. 6. Evolution of lamellar thickness during uniaxial stress-strain test of a (001) fcc crystal for four different grain sizes $d$.

on the grain size is shown in Fig. 7. As may be seen from the figure, the flow stress of the crystal is predicted to rise sharply with decreasing grain size under the con- ditions of the example. The results shown in Fig. 7 are suggestive of a Hall-Petch (Petch, 1953) scaling relation $\sigma \sim d^{-1 / 2}$ for large $d$. The ability of the theory to predict quantitatively the strength and hardness enhancement which is observed to occur in small samples (Nix, 1998; Fleck et al., 1994) is noteworthy.

### 11. Summary and conclusions

We have developed a micromechanical theory of dislocation structures aynd finite- deformation single-crystal plasticity based on the direct generation of deformation microstructures and the computation of the attendant effective behavior. Specifically, we have aimed at describing the lamellar dislocation structures which develop at large strains under monotonic loading. (Hughes and Hansen 1991, 1993; Hansen, 1992; Bay et al., 1992; Hughes et al. 1994, 1997; Hansen and Hughes, 1995; Rosen et al., 1995; Murr et al., 1997; Doherty et al., 1997) Following Ortiz and Repetto (Ortiz and Repetto, 1999), these microstructures are regarded as instances of sequen- tial lamination and treated accordingly. The present approach is based on the explicit construction of microstructures by recursive lamination and their subsequent equili-

![](./images/811194403078012928_8.jpg)

Fig. 7. Grain-size dependence of flow stress at 50% deformation in a (001) fcc crystal.

bration in order to relax the incremental constitutive description of the material. The microstructures are permitted to evolve in complexity and fineness with increasing macroscopic deformation by a process of branching of the leaves of the tree, resulting in the net creation of new leaves. The dislocation structures are deduced from the plastic deformation-gradient field by recourse to Kröner's formula for the dislocation density tensor. The theory is rendered nonlocal by the consideration of the self- energy of the dislocations. The intrinsic length parameters of the nonlocal theory which determine the absolute dimensions of the microstructure are the Burgers vector length $b$ and some suitable geometrical feature size $d$, such as the grain size or film thickness, setting an upper bound for the overall size of the microstructure.

Through selected examples, we have demonstrated the ability of the theory to generate complex microstructures, determine the softening effect which those micro- structures have on the effective behavior of the crystal, and account for the depen- dence of the effective behavior on the size of the sample, or size effect. Our first two examples are concerned with crystals deformed in simple shear and are motivated by the work of Hughes et al. (Hughes et al., 1994) on the near-surface microstructures which develop under large sliding loads. The softening effect of microstructure development on the effective macroscopic behavior of the crystal is evident in these examples. The calculations produce a wealth of additional information regarding, e.g., the misorientations which develop between the various lamellae which form the microstructure. By assigning random orientations to the crystals, the theory may be used to predict the misorientation distribution functions reported by Hughes and co-workers (Hughes et al. 1997, 1998). In a similar vein, consideration of subgrain structures should have the effect of diffusing and generally adding structure to the

textures which are computed from conventional single-crystal models, thereby bring- ing the texture predictions into closer agreement with experiment, (Hughes and Hansen, 1993).

The nonlocal theory predicts the microstructure to refine with increasing macro- scopic deformation and the effective behavior of the crystal to stiffen with decreasing sample size, in keeping with experiments (Bassim and Klassen, 1986; Hughes et al., 1994; Nix, 1998; Nix and Gao, 1998). It should be carefully noted that, while both the present theory and strain-gradient theories of plasticity are nonlocal, they differ in several notable respects. Thus, in contrast to strain-gradient theories of plasticity, the present theory predicts a size effect for nominally uniform macroscopic defor- mations. Also in contrast to strain-gradient theories, the dimensions of the micro- structure depend sensitively on the loading geometry, the extent of macroscopic deformation and the size of the sample.

# Acknowledgements

The support of the Department of Energy through Caltech's ASCI Center of Excel- lence for Simulating Dynamic Response of Materials is gratefully acknowledged. LS also wishes to gratefully acknowledge the support from the Belgian Scientific Research Fund (FNRS).

# References

Abeyaratne, R., Knowles, J.K., 1990. On the driving traction acting on a surface of strain discontinuity in a continuum. Journal of the Mechanics and Physics of Solids 38, 335-360.

Argon, A., Haasen, P., 1993. A new mechanism of work-hardening in the late stages of large-strain plastic-flow in fee and diamond cubic-crystals. Acta Metallurgica et Materialia 41 (11), 3289-3306.

Asaro, R.J., 1983. Micromechanics of crystals and polycrystals. Advances in Applied Mechanics 23, 1-115.

Asaro, R.J., Rice, J.R., 1977. Strain localization in ductile single crystals. Journal of the Mechanics and Physics of Solids 25, 309.

Ball, J.M., James, R.D., 1987. Fine phase mixtures as minimizers of energy. Archive for Rational Mech- anics and Analysis 100, 13-52.

Bhattacharya, J.L., Wu, T.Y., 1991a. Latent hardening in single crystals. 1. Theory and experiments. Proceed- ings of the Royal Society of London A435, 1-19.

Bassani, J.L., Wu, T.Y., 1991b. Latent hardening in single crystals. 2. Analytical characterization and predictions. Proceedings of the Royal Society of London A435, 21-41.

Bassim, M., Klassen, R., 1986. Variation in dislocation cell size with local strain in a low alloy steel. Materials Science and Engineering 81, 163-167.

Bay, B., Hansen, N., Hughes, D., Kuhlmann-Wilsdorf, D., 1992. Overview no-96 - evolution of fee deformation structures in polyslip. Acta Metallurgica et Materialia 40 (2), 205-219.

Bhattacharya, K., 1991. Wedge-like microstructure in martensites. Acta Metallurgica et Materialia 39, 2431-2444.

Bhattacharya, K., 1992. Self-accommodation in martensite. Archive for Rational Mechanics and Analysis 120, 201-244.

Chang, Y.W., Asaro, R.J., 1981. An experimental study of shear localization in aluminium-copper single crystals. Acta Metallurgica 29, 241.

Chipot, M., Kinderlehrer, D., 1988. Equilibrium configurations of crystals. Archive for Rational Mechanics and Analysis 103, 237-277.

Cuitiño, A.M., Ortiz, M., 1992a. Computational modelling of single crystals. Modelling and Simulation in Materials Science and Engineering 1, 255-263.

Cuitiño, A.M., Ortiz, M., 1992b. A material-independent method for extending stress update algorithms from small-strain plasticity to finite plasticity with multiplicative kinematics. Engineering Compu- tations 9, 437-451.

Cuitiño, A.M., Ortiz, M., 1993. Constitutive modeling of $H_2$ intermetallic crystals. Materials Science and Engineering A170, 111-123.

Dacorogna, B., 1989. Direct Methods in the Calculus of Variations. Springer-Verlag, New York.

De Giorgi, E., 1975. Sulla convergenza di alcune successioni di integrali del tipo dell'area. Rendicont di Matematica 8, 277-294.

De Giorgi, E., Franzoni, T., 1975. Su un tipo di convergenza variazionale. Atti Acad. Naz. Lincei, Rendiconti Cl. Sc. Mat. Fis. Nat. 56, 842-850.

Doherty, R., Hughes, D., Humphreys, F., Jonas, J., Jensen, D., Kassuer, M., King, W., McNelley, T., McQueen, H., Rollett, A., 1997. Current issues in recrystallization: a review. Materials Science and Engineering A-Structural Materials Properties Microstructure and Processing 238 (2), 219-274.

Fleck, N., Hutchinson, J., 1993. Aphemenological theory for strain gradient effects in plasticity. Journal of the Mechanics and Physics of Solids 41 (12), 1825-1857.

Fleck, N., Hutchinson, J., 1997. Strain gradient plasticity. Advances in Applied Mechanics 33, 295-361.

Fleck, N., Muller, G., Ashby, M., Hutchinson, J., 1994. Strain gradient plasticity - theory and experiment. Acta Metallurgica et Materialia 42 (2), 475-487.

Franciosi, P., Berveiller, M., Zaoui, A., 1980. Latent hardening in copper and aluminium single crystals. Acta Metallurgica 28, 273-283.

Hansen, N., 1992. Deformation microstructures. Scripta Metallurgica et Materialia 27 (11), 1447-1452.

Hansen, N., Hughes, D., 1995. Analysis of large dislocation populations in deformed metals. Physica Status Solidi A-Applied Research 149 (1), 155-172.

Havner, K.S., 1973. On the mechanics of crystalline solids. Journal of the Mechanics and Physics of Solids 21, 383.

Hill, R., Rice, J.R., 1972. Constitutive analysis of elastic-plastic crystals at arbitary strains. Journal of the Mechanics and Physics of Solids 20, 401.

Hughes, D., Chrzan, D., Liu, Q., Hansen, N., 1998. Scaling of misorientation angle distributions. Physical Review Letters 81 (21), 4664-4667.

Hughes, D., Dawson, D., Korellis, J., Weingarteu, L., 1994. Near-surface microstructures developing under large sliding loads. Journal of Materials Engineering and Performance 3 (4), 459-475.

Hughes, D., Hansen, N., 1991. Microstructural evolution in nickel during rolling and torsion. Materials Science and Technology 7 (6), 544-553.

Hughes, D., Hansen, N., 1993. Microstructural evolution in nickel during rolling from intermediate to large strains. Metallurgical Transcations A-Physical Metallurgy and Materials Science 24 (9), 2021-2037.

Hughes, D., Hansen, N., 1995. High-angle boundaries and orientation distributions at large strains. Scripta Metallurgica et Materialia 33 (2), 315-321.

Hughes, D., Hansen, N., 1997. High angle boundaries formed by grain subdivision mechanisms. Acta Materialia 45 (9), 3871-3886.

Hughes, D., Liu, Q., Chrzan, D., Hansen, N., 1997. Scaling of microstructural parameters: Misorientations of deformation induced boundaries. Acta Materialia 45 (1), 105-112.

Hutchinson, J.W., 1976. Elastic-plastic: behavior of polycrystalline metals and composites. Proceeding of the Regal Society of London A319, 247-272.

Kocks, U.F., 1960. Polyslip in single crystals. Acta Metallurgica 8, 345-352.

Kocks, U.F., 1964. Latent hardening and secondary slip in aluminum and silver. Transcations of the Metallurgical Society of the AIME 230, 1160.

Kocks, U.F., 1966. A statistical theory of flow stress and work-hardening. Philosophical Magazine 13, 541.

Kohn, R., 1991. The relaxation of a double-well energy. Continuum Mechanics and Thermodynamics 3, 193-236.

Kohn, R.V., Müller, S., 1992. Branching of twins near an austenite-twinned-martensite interface. Philo- sophical Magazine A66, 697-715.

Kohn, R.V., Strang, G., 1986a. Optimal design and relaxation of variational problems, i. Communications on Pure and Applied Mathematics 39, 113-137.

Kohn, R.V., Strang, G., 1986b. Optimal design and relaxation of variational problems, ii. Communications on Pure and Applied Mathematics 39, 139-182.

Kohn, R.V., Strang, G., 1986c. Optimal design and relaxation of variational problems, iii. Communications on Pure and Applied Mathematics 39, 353-377.

Kuhlmann-Wilsdorff, D., 1989. Theory of plastic deformation: properties of low energy dislocation struc- tures. Materials Science and Engineering A113, 1.

Kuhlmann-Wilsdorff, D., van der Merwe, J.H., 1982. Theory of dislocation cell sizes in deformed metals. Materials Science and Engineering 55, 79.

Lee, E.H., 1969. Elastic-plastic deformation at finite strains. Journal of Applied Mechanics 36, 1.

Leroy, Y., Ortiz, M., 1989. Finite element analysis of strain localization in frictional materials. Inter- national Journal of Numerical and Analytical Methods for Geomechanics 13, 53-74.

Leroy, Y., Ortiz, M., 1990. Finite element analysis of transient strain localization phenomena in frictional materials. International Journal of Numerical and Analytical Methods for Geomechanics 14, 93-124.

Les, P., Zehetbauer, M., Stuwe, H., 1996. Characteristics of work hardening in late stages of high tempera- ture deformation of aluminium single crystals. Physica Status Solidi A-Applied Research 157 (2), 265-273.

Lubarda, V.A., Blurm, J.A., Needleman, A., 1993. An analysis of equilibrium dislocation distributions. Acta Metallurgica et Materialia 41, 625-642.

Lubliner, J., 1972. On the thermodynamic foundations of non-linear solid mechanics. International Journal of Non-Linear Mechanics 7, 237-254.

Lubliner, J., 1973. On the structure of the rate equations of materials with internal variables. Acta Mech- anica 17, 109-119.

Mandel, J., 1972. Plasticité classique et viscoplasticité. Technical report, lecture notes. Int. Centre for Mech. Sci., Udiue. Springer, Berlin.

Marsden, J.E., Hughes, T.J.R., 1983. Mathematical Foundations of Elasticity. Prentice-Hall, Englewood Cliffs (NJ).

Miehe, C., 1996. Exponential map algorithm for stress updates in anisotropic multiplicative elastoplasticity for single crystals. International Journal for Numerical Methods in Engineering 39, 3367-3390.

Miehe, C., Stein, E., 1992. A canonical model of multiplicative elasto-plasticity, formulation and aspects of the numerical implementation. European Journal of Mechanics, A-Solids 11, 25-43.

Modica, L., 1987. Gradient theory of phase transitions and minimal interface criterion. Archive for Rational Mechanics and Analysis 98, 123-142.

Mura, T., 1987. Micromechanics of defects in solids. Kluwer Academic Publishers, Boston.

Murr, L.E., Meyers, M.A., Niou, C.-S., Chen, Y.J., Pappu, S., Kennedy, C., 1997. Shock-induced defor- mation twinning in tantalum. Acta Materialia 45, 157-175.

Nacar, A., Needleman, A., Ortiz, M., 1989. A finite element method for analyzing localization in rate- dependent solids at finite strains. Computer Methods in Applied Mechanics and Engineering 73 (3), 235-258.

Nesterenko, V., Meyers, M., LaSalvia, J., Bondar, M., Chen, Y., Lukyanov, Y., 1997. Shear localization and recrystallization in high-strain, high-strain-rate deformation of tantalum. Materials Science and Engineering A229, 23-41.

Neumann, P., 1986. Low energy dislocation configurations: A possible key to the understanding of fatigue. Materials Science and Engineering 81, 465-475.

Nix, W., 1998. Yielding and strain hardening of thin metal films on substrates. Scripta Materialia 39 (4/5), 545-554.

Nix, W., Gao, H., 1998. Indentation size effects in crystalline materials: A law for strain gradient plasticity. Journal of the Mechanics and Physics of Solids 46 (3), 411-425.

Nye, J.F., 1953. Some geometrical relations in dislocated crystals. Acta Metallurgica 1, 153-162.

Ortiz, M., Leroy, Y., Needleman, A., 1987. A finite element method for localized failure analysis. Com- puter Methods in Applied Mechanics and Engineering 61 (2), 189-214.

Ortiz, M., Repetto, E.A., 1999. Nonconvex energy minimization and dislocation structures in ductile single crystals. Journal of the Mechanics and Physics of Solids 47 (2), 397–462.

Ortiz, M., Stainier, L., 2000. The variational formulation of viscoplastic constitutive updates. Computer Methods in Applied Mechanics and Engineering (in press).

Pedregal, P., 1993. Laminates and microstructure. European Journal of Applied Mathematics 4, 121–149.

Petch, N.J., 1953. The cleavage strength of polycrystals. Journal of the Iron and Steel Institute 174, 25–28.

Pierce, D., Asaro, R., Needleman, A., 1982. An analysis of nonuniform and localized deformation in ductile single crystals. Acta Metallurgica 30, 1087–1119.

Radovitzky, R., Ortiz, M., 1999. Error estimation and adaptive meshing in strongly nonlinear dynamic problems. Computer Methods in Applied Mechanics and Engineering 172, 203–240.

Ramaswami, B., Kocks, U.F., Chalmers, B., 1965. Latent hardening in silver and ag-au alloy. Transactions of the Metallurgical Society of the AIME 233, 927.

Rice, J.R., 1971. Inelastic constitutive relations for solids: an internal-variable theory and its applications to metal plasticity. Journal of the Mechanics and Physics of Solids 19, 433.

Rice, J.R., 1975. Continuum mechanics and thermodynamics of plasticity in relation to microscale defor- mation mechanisms. In: Argon, A. (Ed.), Constitutive Equations in Plasticity. MIT Press, Cambridge (Mass), pp. 23–79.

Rosen, G., Jensen, D., Hughes, D., Hansen, N., 1995. Microstructure and local crystallography of cold- rolled aluminum. Acta Metallurgica et Materialia 43 (7), 2563–2579.

Schmid, E., Boas, N., 1961. Kristall Plastizität. Springer, Berlin.

Sternberg, P., 1988. The effect of a singular perturbation on nonconvex variational problems. Archive for Rational Mechanics and Analysis 101, 209–260.

Teodosiu, C., 1969, A dynamic theory of dislocations and its applications to the theory of the elastic- plastic continuum. In: Simmons, J.A., (Ed.), Conf. Fundamental Aspects of Dislocation Theory, vol. 2. Washington. Natl. Bureau of Standards Special Publication, pp. 837.

Zehetbauer, M., 1993. Cold work-hardening in stage-iv and stage-v of fcc metals 2 — model fits and physical results. Acta Metallurgica et Materialia 41 (2), 589–599.

Zehetbauer, M., Seumer, V., 1993. Cold work-hardening in stage-iv and stage-v of fee metals 1 — experi- ments and interpretation. Acta Metallurgica et Materialia 41 (2), 577–588.