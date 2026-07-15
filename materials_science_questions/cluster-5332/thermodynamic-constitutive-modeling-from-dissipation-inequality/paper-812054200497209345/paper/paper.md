![](./images/812054200497209345_1.jpg)

Available online at www.sciencedirect.com

![](./images/812054200497209345_2.jpg)

European Journal of Mechanics A/Solids 26 (2007) 189-211

![](./images/812054200497209345_3.jpg)

# Strain-gradient elastic-plastic material models and assessment of the higher order boundary conditions

## Castrenze Polizzotto *

Department of Structural Engineering and Geotechnics, University of Palermo, Viale delle Scienze, 90128 Palermo, Italy

Received 11 July 2005; accepted 27 July 2006

Available online 2 October 2006

## Abstract

A gradient elastic material model exhibiting gradient kinematic and isotropic hardening is addressed within a thermodynamic framework suitable to cope with nonlocal-type continua. The Clausius-Duhem inequality is used, in conjunction with the concepts of energy residual, insulation condition and locality recovery condition, to derive all the pertinent restrictions upon the constitutive equations, including the PDEs and the related higher order (HO) boundary conditions that govern the gradient material behaviour. Through a suitable limiting procedure, the HO boundary conditions are shown to interpret the action, upon the body's boundary surface, of idealized extra HO constraints capable to impede the onset of strain as a nonlocality source and to react with a double traction (of dimension moment/area), work-conjugate of the impeded strain. The HO boundary conditions for the internal moving elastic/plastic boundary are also provided. A number of variational principles are proved. A few simple illustrative numerical examples are worked out.

© 2006 Elsevier Masson SAS. All rights reserved.

Keywords: Nonlocal thermodynamics; Gradient elasticity; Gradient plasticity; Higher order boundary conditions

## 1. Introduction

Strain gradients are usually introduced into the constitutive models either as a remedy to some shortcomings (e.g. strain localization, wave dispersion) that show up within classical local-type continuum theories and to the consequent mesh dependence in standard finite element analyses, or in the purpose to render the models capable to capture some phenomena (e.g. size effects, microstructural defect accumulation and dislocation patterning) that remain unnoticed within classical continuum theories.

The introduction of strain gradients into the gradient theory formulations leads to initial/boundary value problems governed by partial differential equations (PDEs) of higher order (HO) with extra HO boundary conditions (that is, conditions involving tensors of order two or more). There exists a variety of ways in which the strain gradients are incorporated into these formulations by different authors, but essentially two strategies can be identified: one consists in heuristically introducing the gradient dependence directly into the constitutive equations of the local-type material, in the other the pertinent gradient dependent constitutive equations are derived by means of suitable energy arguments.

* Fax: +39 0916568407.
E-mail address: cpoli@diseg.unipa.it (C. Polizzotto).

0997-7538/$ - see front matter © 2006 Elsevier Masson SAS. All rights reserved.
doi:10.1016/j.euromechsol.2006.07.005

Examples of the former strategy are: the gradient plasticity theory by Acharya and Bassani (2000) and Bassani et al. (2001), where the gradient dependence is incorporated directly into the tangent moduli (with the appealing feature of leaving unaltered the classical plasticity theory framework with no need for extra boundary conditions); the gradient plasticity and gradient elasticity theories by Aifantis and co-workers (see review papers by Aifantis, 1999a, 1999b, 2003), in which the gradient dependence is introduced directly into the yield stress and, respectively, into the elasticity stress-strain laws (leading to governing PDEs that can be easily addressed numerically, but no clear indication is there given about the extra boundary conditions). Another example is the gradient plasticity theory by Voyiadjis and Abu Al-Rab (2005) which is a generalization of the Aifantis' one just mentioned.

A classical example of the second strategy mentioned above is the second strain gradient elasticity theory by Mindlin (1965), in which the virtual work principle and a strain energy potential incorporating the strain gradients are employed for deriving the pertinent constitutive equations and the extra boundary conditions. However, Mindlin's theory is to be considered a constitutively local-type one in which the gradient features are enforced at the global level through the compatibility equations, i.e. the strain- and strain gradient-displacement relations (Polizzotto, 2003a, 2003b). Other examples of this second strategy are the gradient plasticity theories advanced by Fleck and Hutchinson (1997, 2001), Gurtin (2000, 2002, 2003), Gudmundson (2004), Fredriksson and Gudmundson (2005), in which the pertinent constitutive equations and related extra HO boundary conditions are derived by the use of a special kind of virtual work principle in conjunction with arguments of classical (local) thermodynamics. Further examples of this strategy are the gradient plasticity theory by Polizzotto and Borino (1998), Liebe and Steinmann (2001), Polizzotto (2003b), and the gradient elasticity theory by Polizzotto (2003a, 2003b), where arguments of nonlocal irreversible thermodynamics are employed. In this last line of research, the gradient damage theories by Liebe and Steinmann (2001), Liebe et al. (2001), Peerlings et al. (2004) are also to be quoted, whereas the theory advanced by Stumpf et al. (2004) can be related to Mindlin's approach.

Gradient elasticity and gradient plasticity have been generally addressed as two distinct research topics, one for gradient elasticity (Mindlin, 1965; Mindlin and Eshel, 1968; Wu, 1992; Triantafyllidis and Aifantis, 1986; Altan and Aifantis, 1997; Lam et al., 2003; Polizzotto, 2003a), another for gradient plasticity, either in its flow version coupled with local elasticity (Aifantis, 1984; Zbib and Aifantis, 1992; Lasry and Belytscko, 1988; Mühlhaus and Aifantis, 1991; de Borst et al., 1993; de Borst et al., 1995; Fleck and Hutchinson, 2001; Liebe and Steinmann, 2001; Polizzotto and Borino, 1998; Gudmundson, 2004), or in its deformation-theory version (Fleck and Hutchinson, 2001; Gao et al., 1999). It is not the purpose of the present paper to review the rich literature on this subject, of which the references quoted above are representative.

In the present paper, a theory of gradient elasticity coupled with gradient plasticity is addressed within the framework of infinitesimal displacements, for the purpose of producing a phenomenological constitutive model with a richer set of nonlocality features. The main issue is the formulation of the constitutive equations and the accompanying extra (HO) boundary conditions in the presence of several coupling gradient features (although in practice there is seldom a need for such a multigradient constitutive model). For this purpose, a thermodynamic approach similar to the one established in previous papers by the author (Polizzotto and Borino, 1998; Polizzotto, 2003a, 2003b) will be adopted with the Clausius-Duhem inequality enriched by an additional term called *energy residual* and constituting a paramount ingredient of nonlocal thermodynamics (Edelen and Laws, 1971; Eringen and Edelen, 1972; Eringen, 1972).

The outline of the paper is as follows. Section 2 is devoted to preliminary arguments of thermodynamics, and in particular to the Clausius-Duhem inequality, the insulation condition and the locality recovery condition. In Section 3, the thermodynamic restrictions upon the constitutive equations are derived, including the PDEs and HO boundary conditions for elasticity, kinematic hardening and isotropic hardening, as well as the constitutive forms of the energy residual and of the plastic dissipation density. Restrictions on the free energy potential are also derived. In Section 4 the meaning of the double tractions is pointed out. In Section 5 the evolutive laws of plasticity obeying the normality rule are provided together with the related local-type maximum dissipation principle. A minimum principle is also provided for the evaluation of the plastic strain state of the particle system which finds itself in a given total strain state and is subjected to a specified plastic deformation mechanism. In Section 6 the total potential energy principle is addressed in two versions, in rate form with flow-theory plasticity and time-finite form with deformation-theory plasticity. In Section 7 a limiting procedure is envisioned to justify the introduction of idealized HO constraints. Section 8 contains a few numerical examples. Section 9 is devoted to the conclusions. The notation system is presented in Appendix A.

## 2. Thermodynamic framework

Let a continuous set of material particles occupy an (open) domain, $V$, of the three-dimensional Euclidean space, which is referred to a Cartesian orthogonal coordinate system, say $\mathbf{x}=(x_1,x_2,x_3)$, in its undeformed configuration. The material is elastic-plastic rate-independent and undergoes small deformations; it is endowed with a Helmholtz free energy potential, $\psi$, of the form:

$$
\psi = \psi_e(\boldsymbol{\varepsilon}^e, \nabla\boldsymbol{\varepsilon}^e) + \psi_{\text{in}}(\boldsymbol{\varepsilon}^p, \kappa, \nabla\boldsymbol{\varepsilon}^p, \nabla\kappa),
\tag{1}
$$

where $\psi_e$ is the elastic strain energy density, $\psi_{\text{in}}$ is the internal stored energy density and both are at least twice differentiable with respect to their own arguments. Also, $\boldsymbol{\varepsilon}^e$ and $\boldsymbol{\varepsilon}^p$ are the elastic and plastic strain tensors, $\kappa$ is a scalar internal variable. Isothermal conditions are assumed throughout for simplicity. Although not shown in (1), $\psi$ may depend explicitly on point $\mathbf{x}$. The gradients $\nabla\boldsymbol{\varepsilon}^e$, $\nabla\boldsymbol{\varepsilon}^p$, $\nabla\kappa$ in (1) represent macroscopic variables by which the microstructure nonlocality sources (as inhomogeneities, defects, dislocations) manifest themselves as gradient effects; (in particular, the gradient $\nabla\boldsymbol{\varepsilon}^p$ can be related to the geometrically necessary dislocations, Fleck et al. (1994), Fleck and Hutchinson (1997, 2001), Gurtin (2002)). As usual, plastic strain affects elasticity only through the difference $\boldsymbol{\varepsilon}^e = \boldsymbol{\varepsilon} - \boldsymbol{\varepsilon}^p$, $\boldsymbol{\varepsilon}$ being the total strain. By assumption, the field $\boldsymbol{\varepsilon}^e$ is $C^3$-continuous and the fields $\boldsymbol{\varepsilon}^p$ and $\kappa$ are $C^1$-continuous; (reasons for this choice will be evident next). Hence, $\psi$ is finite at all points in $V$. At this stage, no relationship is postulated between $\boldsymbol{\varepsilon}^p$ and $\kappa$, except the generic notion that both variables are related to the plastic deformation process and that $\dot{\boldsymbol{\varepsilon}}^p = \mathbf{0}$ everywhere $\dot{\kappa}=0$.

The thermodynamic arguments presented in this section are in many aspects coincident with analogous ones in Polizzotto (2003a, 2003b), from where they in fact are replaced and in part repeated for more clarity, but also with some basic differences.

In the present context, in which the thermodynamics principle of the local action does not hold, the Clausius-Duhem inequality in point-wise form reads (Edelen and Laws, 1971; Eringen and Edelen, 1972; Eringen, 1972; Polizzotto and Borino, 1998; Polizzotto, 2003a, 2003b):

$$
\boldsymbol{\sigma} : \dot{\boldsymbol{\varepsilon}} + P - \dot{\psi} \geqslant 0 \quad \text{in } V,
\tag{2}
$$

where $P$ denotes the *energy residual* (localization residual after Edelen and Laws, 1971). $P$ interprets the long distance interactions between the material particles promoted by the nonlocality sources in $V$; it equals the energy density transmitted to the generic point in $V$ from all other points in it through the latter interactions and collects the cumulative effects of the three types of nonlocality associated with elasticity, kinematic hardening and isotropic hardening.

The energy residual $P$ has to satisfy the following two conditions:

### (i) Insulation condition

$$
\int_V P \mathrm{d}V = 0 \quad \text{for all deformation mechanism in } \mathcal{M},
\tag{3}
$$

where $\mathcal{M}$ denotes the set of all deformation mechanisms;

### (ii) Locality recovery condition

$$
P = 0 \quad \text{in } V \text{ for all deformation mechanism in } \mathcal{M}_0,
\tag{4}
$$

where $\mathcal{M}_0 \subset \mathcal{M}$ denotes the subset of all gradient-free deformation mechanisms, that is, characterized by uniform strain fields (all nonlocality sources are inactive). Note that if $P=0$ everywhere in $V$ for all deformation mechanism in $\mathcal{M}$, the material would be a local-type, or simple, material.

The global condition (3) was advanced by Edelen and Laws (1971) in the general framework of nonlocal continuum theories. It is motivated by the nonlocal nature of the material constitutive behaviour, whereby long distance particle interactions are allowed in the inside of the domain $V$, but not between the material particles in $V$ and the exterior world. Only recently has the merit of condition (3) been recognized (see e.g. Polizzotto and Borino, 1998; Liebe and Steinmann, 2001; Liebe et al., 2001; Benvenuti et al., 2002; Polizzotto, 2003a, 2003b).

The point-wise condition (4) constitutes a thermodynamic characterization of a requisite that every phenomenological constitutive model has to possess, that is, the requisite by which, whenever the nonlocality sources are all inactive,

hence the gradients $\nabla \dot{\boldsymbol{\varepsilon}}^{e}$, $\nabla \dot{\boldsymbol{\varepsilon}}^{p}$, $\nabla \dot{\kappa}$ are identically vanishing, then the gradient model behaves as a local one both in stress and in energy. Condition (4) was first introduced by Polizzotto et al. (2006) within the framework of nonlocal (integral) elasticity; heuristic rules were in use before for the purpose.

Inequality (2) together with conditions (3) and (4) are used (in next section) for deriving the pertinent restrictions upon the constitutive equations. In view of this, let the boundary surface $S=\partial V$ be decomposed in two portions, say $S=S_{c} \cup S_{f}$, such that the body is clamped with ordinary constraints at points of $S_{c}$ (where the displacement is specified), free at points of $S_{f}$ (where the traction is specified). Let $S$ be also decomposed as $S=S_{c}^{(1)} \cup S_{f}^{(1)}$, such that the body is clamped with some (idealized) elasticity HO constraints at points of $S_{c}^{(1)}$ (where elastic strain is prescribed), free at points of $S_{f}^{(1)}$ (where the work-conjugate force, called elastic double traction, is prescribed). Additionally, let $V_{p} \subset V$ be the subdomain in which a plastic deformation mechanism is taking place at the generic time, and let the boundary surface $S_{p}:=\partial V_{p}$ be decomposed as $S_{p}=S_{p(\mathrm{ext})} \cup S_{p(\mathrm{int})} . S_{p(\mathrm{int})}$ is the (moving) internal elastic/plastic boundary, $S_{p(\mathrm{ext})}=S_{p} \cap S$. Also, let $S_{p(\mathrm{ext})}$ be decomposed as $S_{p(\mathrm{ext})}=S_{p c}^{(1)} \cup S_{p f}^{(1)}$, such that $V$ is clamped with some plasticity HO constraints at points of $S_{p c}^{(1)}$ (where the plastic strain rate is prescribed), free at points of $S_{p f}^{(1)}$ (where the plastic double traction rate is prescribed). Both the plastic strain rate and plastic double traction rate are prescribed on $S_{p(\mathrm{int})}$. Obviously, $S_{p(\mathrm{int})}=\emptyset$ whenever $V_{p}=V$. The sense in which the term prescribed is to be intended will be clarified in next section. A further discussion on these HO constraints is presented in Section 7.

### 3. Restrictions on the constitutive equations

Following a known procedure of constitutive equation theory (Colemann and Gurtin, 1967; Germain et al., 1983; Lemaitre and Chaboche, 1990) and leaving for the moment unspecified the evolutive laws governing the irreversible material behaviour, the state equations and all other restrictions on the constitutive equations are derived in this section. For this purpose, let us introduce the definitions:

$$
\boldsymbol{\sigma}^{(0)}:=\frac{\partial \psi_{e}}{\partial \boldsymbol{\varepsilon}^{e}}, \quad \boldsymbol{\sigma}^{(1)}:=\frac{\partial \psi_{e}}{\partial \nabla \boldsymbol{\varepsilon}^{e}},
\tag{5}
$$

$$
\mathbf{s}^{(0)}:=\frac{\partial \psi_{\text {in }}}{\partial \boldsymbol{\varepsilon}^{p}}, \quad \mathbf{s}^{(1)}:=\frac{\partial \psi_{\text {in }}}{\partial \nabla \boldsymbol{\varepsilon}^{p}},
\tag{6}
$$

$$
\chi^{(0)}:=\frac{\partial \psi_{\text {in }}}{\partial \kappa}, \quad \chi^{(1)}:=\frac{\partial \psi_{\text {in }}}{\partial \nabla \kappa}.
\tag{7}
$$

In this paper, the stresses denoted with symbols as $(\cdot)^{(0)}$ are referred to as simple stresses, those denoted with symbols as $(\cdot)^{(1)}$ are referred to as double stresses (but the name HO-stresses may also be used). Note that $\boldsymbol{\sigma}^{(0)}=$ $\left\{\sigma_{i j}^{(0)}\right\}$ and $\mathbf{s}^{(0)}=\left\{s_{i j}^{(0)}\right\}$ are second-order symmetric tensors, $\boldsymbol{\sigma}^{(1)}=\left\{\sigma_{r i j}^{(1)}\right\}$ and $\mathbf{s}^{(1)}=\left\{s_{r i j}^{(1)}\right\}$ are third-order tensors symmetric in the last two indices, whereas $\chi^{(0)}$ is a scalar and $\chi^{(1)}=\left\{\chi_{r}^{(1)}\right\}$ is a vector. Then, expanding the time derivative of $\psi$, inequality (2) becomes:

$$
\left(\boldsymbol{\sigma}-\boldsymbol{\sigma}^{(0)}\right): \dot{\boldsymbol{\varepsilon}}^{e}-\boldsymbol{\sigma}^{(1)^{\mathrm{T}}}: \nabla \dot{\boldsymbol{\varepsilon}}^{e}+\left(\boldsymbol{\sigma}-\mathbf{s}^{(0)}\right): \dot{\boldsymbol{\varepsilon}}^{p}-\mathbf{s}^{(1)^{\mathrm{T}}}: \nabla \dot{\boldsymbol{\varepsilon}}^{p}-\chi^{(0)} \dot{\kappa}-\boldsymbol{\chi}^{(1)} \cdot \nabla \dot{\kappa}+P \geqslant 0 \quad \text { in } V .
\tag{8}
$$

### 3.1. Elastic deformation mechanisms

Assuming (isothermal) elastic transformations, such that $\dot{\boldsymbol{\varepsilon}}^{p}$ and $\dot{\kappa}$ are identically vanishing and $\dot{\boldsymbol{\varepsilon}}^{e}=\dot{\boldsymbol{\varepsilon}}$, Eq. (8) simplifies as

$$
\left(\boldsymbol{\sigma}-\boldsymbol{\sigma}^{(0)}\right): \dot{\boldsymbol{\varepsilon}}^{e}-\boldsymbol{\sigma}^{(1)^{\mathrm{T}}}: \nabla \dot{\boldsymbol{\varepsilon}}^{e}+P \geqslant 0 \quad \text { in } V .
\tag{9}
$$

For more generality, the material characteristics are assumed discontinuous across some internal surface, say $\Gamma$. Under this hypothesis, by integration of (9) over $V$, applying the divergence theorem and observing that $\dot{\boldsymbol{\varepsilon}}^{e}$ is continuous across $\Gamma$, we can write:

$$
\int_{V}\left[\boldsymbol{\sigma}-\boldsymbol{\sigma}^{(0)}+\nabla \cdot \boldsymbol{\sigma}^{(1)}\right]: \dot{\boldsymbol{\varepsilon}}^{e} \mathrm{~d} V-\int_{S} \mathbf{n} \cdot \boldsymbol{\sigma}^{(1)}: \dot{\boldsymbol{\varepsilon}}^{e} \mathrm{~d} S+\int_{\Gamma} \mathbf{n} \cdot\left[\left[\boldsymbol{\sigma}^{(1)}\right]\right]_{\Gamma}: \dot{\boldsymbol{\varepsilon}}^{e} \mathrm{~d} S \geqslant 0
\tag{10}
$$

where $\mathbf{n}$ denotes the unit external normal to $S$, and also the unit normal to $\Gamma$ oriented in some prefixed direction. The symbol $[\![\cdot ]\!]_{\Gamma}$ denotes jump across $\Gamma$.

Considering that inequality (10) holds for any admissible elastic deformation mechanism $\dot{\boldsymbol{\varepsilon}}^{e}$, hence for arbitrary $\dot{\boldsymbol{\varepsilon}}^{e}$ fields in $V \cup S$ and that all integrals in (10) are linear with respect to $\dot{\boldsymbol{\varepsilon}}^{e}$, the necessary and sufficient conditions for (10) are the following state equations, that is:
$$
\boldsymbol{\sigma}=\boldsymbol{\sigma}^{(0)}-\nabla \cdot \boldsymbol{\sigma}^{(1)} \quad \text { in } V \setminus \Gamma,
\tag{11}
$$
and the related HO boundary conditions
$$
\dot{\boldsymbol{\varepsilon}}^{e}=\mathbf{0} \quad \text { on } S_{c}^{(1)},
\tag{12a}
$$
$$
\mathbf{t}_{(n)}^{(1)}:=\mathbf{n} \cdot \boldsymbol{\sigma}^{(1)}=\mathbf{0} \quad \text { on } S_{f}^{(1)},
\tag{12b}
$$
$$
\left[\left[\mathbf{t}_{(n)}^{(1)}\right]\right]_{\Gamma}:=\mathbf{n} \cdot\left[\left[\boldsymbol{\sigma}^{(1)}\right]\right]_{\Gamma}=\mathbf{0} \quad \text { on } \Gamma,
\tag{12c}
$$
where obviously (12b) and (12c) hold also in rate form. The stress $\boldsymbol{\sigma}$ of (11), referred to as the *total Cauchy stress* in this paper, proves to be $C^{1}$-continuous in $V$ (what is necessary for $\boldsymbol{\sigma}$ to satisfy the field equilibrium equations), except on $\Gamma$, where the continuity requirement for $\boldsymbol{\varepsilon}^{e}$ is relaxed to $C^{0}$-continuity. The HO traction $\mathbf{t}_{(n)}^{(1)}$ in (12b,c) is work-conjugate of the impeded elastic strain; it is referred to as *elastic double traction* (with dimension moment/area). The (homogeneous) HO boundary conditions (12a–c) assign vanishing prescribed values to $\boldsymbol{\varepsilon}^{e}$ and $\mathbf{t}_{(n)}^{(1)}$.

Eqs. (11) and (12a–c) imply that (10) is satisfied as an equality, and thus (9) is also satisfied as an equality; hence we can write:
$$
P=P^{(e l)}:=\boldsymbol{\sigma}^{(1)^{\mathrm{T}}}: \nabla \dot{\boldsymbol{\varepsilon}}^{e}-\left(\boldsymbol{\sigma}-\boldsymbol{\sigma}^{(0)}\right): \dot{\boldsymbol{\varepsilon}}^{e},
\tag{13}
$$
which, substituting from (11) for $\boldsymbol{\sigma}$, gives:
$$
P=P^{(e l)}=\boldsymbol{\sigma}^{(1)^{\mathrm{T}}}: \nabla \dot{\boldsymbol{\varepsilon}}^{e}+\nabla \cdot \boldsymbol{\sigma}^{(1)}: \dot{\boldsymbol{\varepsilon}}^{e} \quad \text { in } V.
\tag{14}
$$

This is the constitutive equation for $P$ in the hypothesis of purely elastic deformation.

Eq. (11) with $\boldsymbol{\sigma}^{(0)}$ and $\boldsymbol{\sigma}^{(1)}$ given by (5) is a PDE system of the second order. This, together with the boundary conditions (12a–c) (one tensor-valued boundary condition, either static, or kinematic, at every point of $S \cup \Gamma$), constitute the gradient elasticity constitutive equations.

**Remark 1.** The elasticity model presented in this subsection differs from the one given by Polizzotto (2003a) for many aspects. In the latter paper, in fact, a second gradient model is addressed, which admits only displacement-driven strain modes and complies with HO boundary conditions formally similar to the Mindlin (1965) model (the HO constraints impede the displacement first and second normal derivatives over the clamped surface). Instead, in the present (first gradient) model arbitrary elastic strains are admitted and the HO constraints impede just the strain.

### 3.2. Elastic-plastic deformation mechanisms

General elastic-plastic deformation mechanisms are here considered, while assuming that the state equations previously obtained, that is (11) and (12a–c), continue to be valid. The Clausius–Duhem inequality (8), substituting $\boldsymbol{\sigma}$ from (11) in the first addend, can be rewritten as:
$$
D:=\boldsymbol{\sigma}: \dot{\boldsymbol{\varepsilon}}^{p}-\boldsymbol{\sigma}^{(0)}: \dot{\boldsymbol{\varepsilon}}^{p}-\mathbf{s}^{(1)^{\mathrm{T}}}: \nabla \dot{\boldsymbol{\varepsilon}}^{p}-\chi^{(0)} \dot{\kappa}-\boldsymbol{\chi}^{(1)} \cdot \nabla \dot{\kappa}+P^{(p l)} \geqslant 0,
\tag{15}
$$
where $P^{(p l)}:=P-P^{(e l)}$ and $D$ denotes the plastic dissipation density.

The energy residual $P^{(p l)}$, associated with the plasticity nonlocality sources, is at the present stage the last state variable to be determined. For this purpose, the Onsager reciprocity principle is assumed valid, hence the plastic dissipation can be represented as a bilinear form in terms of fluxes $\dot{\boldsymbol{\varepsilon}}^{p}, \dot{\kappa}$ (independent variables driving the plastic deformation mechanism) and of related affinities, say $\boldsymbol{\rho}$ and $\chi$, that is:
$$
D=\boldsymbol{\rho}: \dot{\boldsymbol{\varepsilon}}^{p}-\chi \dot{\kappa}.
\tag{16}
$$

Next, on comparing (15) with (16), we can write:

$$
P^{(p l)}=\boldsymbol{\rho}: \dot{\boldsymbol{\varepsilon}}^{p}-\chi \dot{\kappa}-\left(\boldsymbol{\sigma}-\mathbf{s}^{(0)}\right): \dot{\boldsymbol{\varepsilon}}^{p}+\mathbf{s}^{(1)^{\mathrm{T}}}: \nabla \dot{\boldsymbol{\varepsilon}}^{p}+\chi^{(0)} \dot{\kappa}+\boldsymbol{\chi}^{(1)} \cdot \nabla \dot{\kappa}.
\tag{17}
$$

With an integration of (17) over $V_p$ (where $\dot{\boldsymbol{\varepsilon}}^p$ and $\dot{\kappa}$ are nonvanishing), applying the divergence theorem and enforcing the insulation condition (3), we have the equality:

$$
\begin{aligned}
\int_{V_{p}} P^{(p l)} \mathrm{d} V= & \int_{V_{p}}\left[\boldsymbol{\rho}-\left(\boldsymbol{\sigma}-\mathbf{s}^{(0)}+\nabla \cdot \mathbf{s}^{(1)}\right)\right]: \dot{\boldsymbol{\varepsilon}}^{p} \mathrm{~d} V-\int_{V_{p}}\left[\chi-\chi^{(0)}+\nabla \cdot \boldsymbol{\chi}^{(1)}\right] \dot{\kappa} \mathrm{d} V \\
& +\int_{S_{p}} \mathbf{n} \cdot \mathbf{s}^{(1)}: \dot{\boldsymbol{\varepsilon}}^{p} \mathrm{~d} S+\int_{S_{p}} \mathbf{n} \cdot \boldsymbol{\chi}^{(1)} \dot{\kappa} \mathrm{d} S=0.
\end{aligned}
\tag{18}
$$

Eq. (18) has to be satisfied for arbitrary plastic deformation mechanisms $(\dot{\boldsymbol{\varepsilon}}^p, \dot{\kappa})$ and for any possible evolutive law governing the material plastic behaviour, hence for arbitrary choices of the $\dot{\boldsymbol{\varepsilon}}^p, \dot{\kappa}$ fields; it thus implies the following field equations:

$$
\boldsymbol{\rho}=\boldsymbol{\sigma}-\mathbf{s} \quad \text { in } V_{p},
\tag{19}
$$

$$
\mathbf{s}:=\mathbf{s}^{(0)}-\nabla \cdot \mathbf{s}^{(1)} \quad \text { in } V_{p},
\tag{20}
$$

$$
\chi=\chi^{(0)}-\nabla \cdot \boldsymbol{\chi}^{(1)} \quad \text { in } V_{p}
\tag{21}
$$

which respectively define the net total Cauchy stress, the total back-stress and the total drag stress. Additionally, Eq. (18) gives the HO boundary conditions accompanying (19)-(21) as:

$$
\dot{\boldsymbol{\varepsilon}}^{p}=\mathbf{0} \quad \text { and } \quad \dot{\kappa}=0 \quad \text { on } S_{p c}^{(1)},
\tag{22a}
$$

$$
\mathbf{p}_{(n)}^{(1)}:=\mathbf{n} \cdot \mathbf{s}^{(1)}=\mathbf{0} \quad \text { and } \quad q_{(n)}^{(1)}:=\mathbf{n} \cdot \boldsymbol{\chi}^{(1)}=0 \quad \text { on } S_{p f}^{(1)},
\tag{22b}
$$

$$
\dot{\mathbf{p}}_{(n)}^{(1)}=\dot{\boldsymbol{\varepsilon}}^{p}=\mathbf{0} \quad \text { and } \quad \dot{q}_{(n)}^{(1)}=\dot{\kappa}=0 \quad \text { on } S_{p(\text { int })},
\tag{22c}
$$

where $\mathbf{p}_{(n)}^{(1)}$ and $q_{(n)}^{(1)}$ are the plastic double tractions, work-conjugate of $\dot{\boldsymbol{\varepsilon}}^p$ and $\dot{\kappa}$, respectively. The (homogeneous) HO boundary conditions (22a-c) specify zero prescribed values for $\dot{\boldsymbol{\varepsilon}}^p, \dot{\kappa}, \mathbf{p}_{(n)}^{(1)}$ and $q_{(n)}^{(1)}$. The static-type conditions in (22c) have been added to signify that the plasticity HO constraints placed upon $S_{p(\text { int })}$ are to be interpreted as nonreacting HO constraints, as well as in consequence of the $C^0$-continuity of the plastic double traction rates across $S_{p(\text { int })}$ (adjacent to $V_e=V \setminus V_p$, where $\dot{\boldsymbol{\varepsilon}}^p \equiv \mathbf{0}$ and $\dot{\kappa} \equiv 0$). The boundary conditions (22a,b) are substantially coincident, respectively, with the hard and free boundary conditions advanced by Gurtin (2004) and Gurtin and Needleman (2005).

It is worth noting that, whereas conditions (22a,b) hold in either time-finite and rate forms because the related boundary surfaces are fixed (they lie on the body's boundary surface $S$), on the contrary conditions (22c) hold as a rule in rate form because the boundary $S_{p(\text { int })}$ is in general moving with the progressing deformation process; an exception to this rule occurs in the deformation-theory plasticity.

Finally, substituting from (19)-(21) for $\boldsymbol{\rho}$ and $\chi$, Eq. (17) gives:

$$
P^{(p l)}=\nabla \cdot \mathbf{s}^{(1)}: \dot{\boldsymbol{\varepsilon}}^{p}+\mathbf{s}^{(1)^{\mathrm{T}}}: \nabla \dot{\boldsymbol{\varepsilon}}^{p}+\nabla \cdot \boldsymbol{\chi}^{(1)} \dot{\kappa}+\boldsymbol{\chi}^{(1)} \cdot \nabla \dot{\kappa}
\tag{23}
$$

which is the constitutive equation for $P^{(p l)}$. The total residual $P$ proves to be:

$$
P=P^{(e l)}+P^{(p l)}=P^{(e l)}+P^{(k h)}+P^{(i h)} \quad \text { in } V,
\tag{24}
$$

where, by (14) and (23), we have set:

$$
P^{(e l)}:=\nabla \cdot \boldsymbol{\sigma}^{(1)}: \dot{\boldsymbol{\varepsilon}}^{e}+\boldsymbol{\sigma}^{(1)^{\mathrm{T}}}: \nabla \dot{\boldsymbol{\varepsilon}}^{e}=\nabla \cdot\left(\boldsymbol{\sigma}^{(1)}: \dot{\boldsymbol{\varepsilon}}^{e}\right),
\tag{25a}
$$

$$
P^{(k h)}:=\nabla \cdot \mathbf{s}^{(1)}: \dot{\boldsymbol{\varepsilon}}^{p}+\mathbf{s}^{(1)^{\mathrm{T}}}: \nabla \dot{\boldsymbol{\varepsilon}}^{p}=\nabla \cdot\left(\mathbf{s}^{(1)}: \dot{\boldsymbol{\varepsilon}}^{p}\right),
\tag{25b}
$$

$$
P^{(i h)}:=\nabla \cdot \boldsymbol{\chi}^{(1)} \dot{\kappa}+\boldsymbol{\chi}^{(1)} \cdot \nabla \dot{\kappa}=\nabla \cdot\left(\boldsymbol{\chi}^{(1)} \dot{\kappa}\right).
\tag{25c}
$$

That is, at every point $\mathbf{x} \subset V$, the residual $P$ can be decomposed in as many parts as there are nonlocality types (i.e. elasticity, kinematic and isotropic hardening in the present case). Every individual component of $P$ represents the long distance energy density transmitted to the generic particle from all other particles in $V$ as a consequence of the related nonlocality sources. Obviously, in $V_{e}:=V \backslash V_{p}$ it is $P^{(k h)}=P^{(i h)}=0$ and $P=P^{(e l)}$.

In writing Eqs. (18)-(21) it has been tacitly assumed that $\Gamma \notin V_{p}$. In the opposite case, (20) and (21) do not holdon $\Gamma$; moreover the following conditions have to be appended to (22a-c):
$$
\left[\left[\mathbf{p}_{(n)}^{(1)}\right]\right]_{\Gamma}=\mathbf{0} \quad \text { and } \quad\left[\left[q_{(n)}^{(1)}\right]\right]_{\Gamma}=0 \quad \text { on } \Gamma \cap V_{p},
$$
which hold also in rate form. Satisfaction of (26) requires that $\mathbf{s}^{(1)}$ and $\chi^{(1)}$ be discontinuous across $\Gamma$ (hence the continuity requirements on $\boldsymbol{\varepsilon}^{p}$ and $\kappa$ are there to be relaxed to $C^{0}$-continuity).

Eq. (20) with $\mathbf{s}^{(0)}$ and $\mathbf{s}^{(1)}$ given by (6) constitutes a second-order PDE system which, completed with the pertinent HO boundary conditions $(22 a)_{1},(22 b)_{1}$ and $(22 c)_{1}$, describes the kinematic-type hardening of the material behaviour. Analogously, Eq. (21) with $\chi^{(0)}$ and $\chi^{(1)}$ given by (7) is a second-order scalar PDE which, together with the HO boundary conditions $(22 a)_{2},(22 b)_{2}$ and $(22 c)_{2}$, describes the isotropic-type hardening of the material behaviour.

The residual $P$ given by $(24)_{2}$ and $(25 a-c)$ obviously complies with the insulation condition (3). The locality recovery condition (4), by $(25 a-c)$ and (5)-(7), gives:
$$
\nabla \cdot \boldsymbol{\sigma}^{(1)}=\nabla \cdot\left(\frac{\partial \psi_{e}}{\partial \nabla \boldsymbol{\varepsilon}^{e}}\right)=\mathbf{0} \quad \text { in } V,
$$

$$
\nabla \cdot \mathbf{s}^{(1)}=\nabla \cdot\left(\frac{\partial \psi_{\text {in }}}{\partial \nabla \boldsymbol{\varepsilon}^{p}}\right)=\mathbf{0}, \quad \nabla \cdot \chi^{(1)}=\nabla \cdot\left(\frac{\partial \psi_{\text {in }}}{\partial \nabla \kappa}\right)=0 \quad \text { in } V,
$$
to be satisfied for any deformation mechanism in $\mathcal{M}_{0}$.

A first consequence of Eqs. (27) and (28) is that the double stresses $\boldsymbol{\sigma}^{(1)}, \mathbf{s}^{(1)}$ and $\chi^{(1)}$ have to vanish identically for any gradient-free deformation mechanism. In fact, Eqs. (27) and (28) can be satisfied in $\mathcal{M}_{0}$ if, and only if, the partial derivatives there appearing, hence the double stresses, are spatially constant for any gradient-free deformation mechanism, and thus, by the homogeneous boundary conditions (12b) and (22b), identically vanishing correspond- ingly.

A second consequence of Eqs. (27) and (28) is the necessity of a restriction on $\psi$, whereby $\psi$ has to depend on the strain gradients homogeneously with a degree larger than one. In fact, under this condition, the partial derivatives in(27) and (28), hence the double stresses, vanish identically for any gradient-free deformation mechanism.

It can be shown that, under the above restriction, all the response functions coincide with those of the local consti- tutive model in the case of gradient-free deformation mechanism, but this point is not further pursued here for brevity(for a discussion in the context of nonlocal elasticity see Polizzotto et al., 2006).

Remark 2. The gradient plasticity model presented in this section is similar, but not equal, to the one previously advanced by the author (Polizzotto, 2003b). The main differences regard the HO boundary conditions. These are here specified more precisely for both the fixed and moving boundaries of the plastified zone.

### 4. Meaning of the energy residual and double tractions

The double tractions $\mathbf{t}_{(n)}^{(1)}, \mathbf{p}_{(n)}^{(1)}$ and $q_{(n)}^{(1)}$, which play a crucial role in the HO boundary conditions (12a-c) and(22a-c), are strictly related to the residual components (25a-c) in a way to be explained hereafter. For this purpose, let $V_{0}$ denote an arbitrary subdomain of $V$ and let the total energy residual in $V_{0}$, say $P(V_{0})$ , be computed, namely
$$
\mathcal{P}\left(V_{0}\right)=\int_{V_{0}} P \mathrm{~d} V.
$$

In general, $P(V_{0}) \not \equiv 0 \forall V_{0} \subset V$ because long distance interactions are allowed to occur between particles in $V_{0}$ and in $V \backslash V_{0}$ , respectively. Eq. (29), by $(24)_{2}$ and $(25 a-c)$ and applying the divergence theorem, can be written (using thenotation $S_{0}:=\partial V_{0}$ and assuming $\Gamma=\emptyset$ for simplicity):
$$
\mathcal{P}\left(V_{0}\right)=\int_{S_{0}}\left[\mathbf{t}_{(n)}^{(1)}: \dot{\boldsymbol{\varepsilon}}^{e}+\mathbf{p}_{(n)}^{(1)}: \dot{\boldsymbol{\varepsilon}}^{p}+q_{(n)}^{(1)} \dot{\kappa}\right] \mathrm{d} S.
$$

Eq. (30) shows that the double tractions $\mathbf{t}_{(n)}^{(1)}$, $\mathbf{p}_{(n)}^{(1)}$ and $q_{(n)}^{(1)}$ represent the long distance energy (per unit strain rate) flowing through the oriented unit area on $S_{0}$ as a consequence of, respectively, gradient elasticity, gradient kinematic hardening and gradient isotropic hardening. Therefore, these double tractions have the meaning of *nonlocality influx forces* (dimensionally, moment/area) promoting the long distance energy interactions between particles located in the opposite sides of $S_{0}$.

It is worth noting that, in the case of gradient-free deformation mechanisms, by the locality recovery condition it is $P=0$ everywhere in $V$ and thus $\mathcal{P}(V_{0})=0\ \forall V_{0}\subseteq V$. Correspondingly, in the right-hand side of (30) the double tractions are all vanishing identically.

If $V_{0}=V_{p}$, by the HO boundary conditions (22a,b), Eq. (30) simplifies as:

$$
\mathcal{P}\left(V_{p}\right)=\int_{S_{p(\mathrm{int})}} \mathbf{t}_{(n)}^{(1)}: \dot{\boldsymbol{\varepsilon}}^{e} \mathrm{d} S
\tag{31}
$$

which only depends on the elastic double traction $\mathbf{t}_{(n)}^{(1)}$ acting on the moving internal elastic/plastic boundary $S_{p(\mathrm{int})}$. This implies that, under any deformation mechanism, the total long distance energy transmitted to the subdomain $V_{p}$ flows in through the surface $S_{p(\mathrm{int})}$ and is supplied at the expenses of the elastic deformation only.

Finally, if $V_{0}=V$, Eq. (30) becomes:

$$
\mathcal{P}(V)=\int_{S} \mathbf{t}_{(n)}^{(1)}: \dot{\boldsymbol{\varepsilon}}^{e} \mathrm{d} S+\int_{S_{p(\mathrm{ext})}}\left(\mathbf{p}_{(n)}^{(1)}: \dot{\boldsymbol{\varepsilon}}^{p}+q_{(n)}^{(1)} \dot{\kappa}\right) \mathrm{d} S+\int_{S_{p(\mathrm{int})}}\left(\mathbf{p}_{(n)}^{(1)}: \dot{\boldsymbol{\varepsilon}}^{p}+q_{(n)}^{(1)} \dot{\kappa}\right) \mathrm{d} S=0.
\tag{32}
$$

The HO boundary conditions (12a,b) and (22a–c) guarantee that all the integrals in (32) vanish identically, as required by the insulation condition (3). In fact, at points of $S$, either $\dot{\boldsymbol{\varepsilon}}^{e}=\mathbf{0}$, or $\mathbf{t}_{(n)}^{(1)}=\mathbf{0}$, whereas at points of $S_{p(\mathrm{ext})}$, either $\dot{\boldsymbol{\varepsilon}}^{p}=\mathbf{0}$ and $\dot{\kappa}=0$, or $\mathbf{p}_{(n)}^{(1)}=\mathbf{0}$ and $q_{(n)}^{(1)}=0$. At points of $S_{p(\mathrm{int})}$ (where nonreacting HO constraints are located), both the kinematic and static *rate-form* conditions are to be satisfied.

### 5. Evolutive laws

The form (16) of the dissipation $D$ suggests one to formulate the plasticity evolutive laws in a classical way in terms of the dissipative stresses $\boldsymbol{\rho}$ and $\chi$; for instance, with the normality rule and denoting by $F$ the yield function:

$$
F:=\phi(\boldsymbol{\rho})-\chi-\sigma_{y} \leqslant 0, \quad \dot{\lambda} \geqslant 0, \quad \dot{\lambda} F(\boldsymbol{\rho}, \chi)=0,
\tag{33a}
$$

$$
\dot{\boldsymbol{\varepsilon}}^{p}=\dot{\lambda} \frac{\partial \phi}{\partial \boldsymbol{\rho}}, \quad \dot{\kappa}=\dot{\lambda},
\tag{33b}
$$

where $\sigma_{y}$ denotes the yield stress. Then, by (33b), the relation between $\kappa$ and $\boldsymbol{\varepsilon}^{p}$ proves to be given by

$$
\dot{\kappa}=\left(\dot{\boldsymbol{\varepsilon}}^{p}: \dot{\boldsymbol{\varepsilon}}^{p}\right)^{1 / 2} /(\mathbf{g}: \mathbf{g})^{1 / 2},
\tag{34}
$$

where $\mathbf{g}:=\partial \phi / \partial \boldsymbol{\rho}$. The plasticity laws (33a,b) are equivalent to a local-type maximum dissipation principle cast in the form:

$$
D\left(\dot{\boldsymbol{\varepsilon}}^{p}, \dot{\kappa}\right)=\max _{\boldsymbol{\rho}, \chi}\left(\boldsymbol{\rho}: \dot{\boldsymbol{\varepsilon}}^{p}-\chi \dot{\kappa}\right) \quad \text { s.t. } \quad F(\boldsymbol{\rho}, \chi) \leqslant 0
\tag{35}
$$

where ‘s.t.’ stands for ‘subject to’ and the optimal objective function represents the dissipation density as a function of the (locally) fixed plastic deformation mechanism $(\dot{\boldsymbol{\varepsilon}}^{p}, \dot{\kappa})$.

The nonlocal gradient nature of the material plastic behaviour comes up when the material state in terms of the plastic strain variables $(\boldsymbol{\varepsilon}^{p}, \kappa)$ is to be evaluated for a given plastic deformation mechanism distributed in $V_{p}$ and satisfying (22a,c). This task can be achieved by solving the PDE systems and HO boundary conditions previously established, i.e. Eqs. (19)–(21) and (22a–c), with $\boldsymbol{\sigma}$ given by (11), but (22a,c) written in time-finite form, that is:

$$
\boldsymbol{\varepsilon}^{p}=\mathbf{0} \quad \text { and } \quad \kappa=0 \quad \text { on } S_{p c}^{(1)} \cup S_{p(\mathrm{int})},
\tag{36a}
$$

$$
\mathbf{n} \cdot \mathbf{s}^{(1)}=\mathbf{0} \quad \text { and } \quad \mathbf{n} \cdot \boldsymbol{\chi}^{(1)}=0 \quad \text { on } S_{p f}^{(1)}.
\tag{36b}
$$

Alternatively, the same task can be addressed by a variational formulation. This consists in the minimization of the functional $Y = Y[\boldsymbol{\varepsilon}^p, \kappa]$ defined as follows:

$$
Y := \int_{V_p} \left[\psi_e(\boldsymbol{\varepsilon} - \boldsymbol{\varepsilon}^p, \nabla \boldsymbol{\varepsilon} - \nabla \boldsymbol{\varepsilon}^p) + \psi_{\text{in}}(\boldsymbol{\varepsilon}^p, \kappa, \nabla \boldsymbol{\varepsilon}^p, \nabla \kappa) + \boldsymbol{\rho} : \boldsymbol{\varepsilon}^p - \chi \kappa\right] \mathrm{d}V
\tag{37}
$$

subject to the constraints (36a).

In (37), $\boldsymbol{\rho}$ and $\chi$ are to be considered known fields in $V_p$, obtained from the application of (35) at every point of $V_p$. Also, $\boldsymbol{\varepsilon}$ is any fixed total strain field in $V$, but complying with the regularity requirements and boundary conditions (12a,b). It can be proved that the solution (if any) of the PDE system coincides with the (unique) solution to the above constrained minimum problem and conversely.

Proof. The first variation of $Y$, after application of the divergence theorem, can be written, remembering Eqs. (5)–(7):

$$
\begin{aligned}
\delta Y &= \int_{V_p} \left[\boldsymbol{\rho} - \boldsymbol{\sigma}^{(0)} + \mathbf{s}^{(0)} + \nabla \cdot \left(\boldsymbol{\sigma}^{(1)} - \mathbf{s}^{(1)}\right)\right] : \delta \boldsymbol{\varepsilon}^p \mathrm{d}V - \int_{V_p} \left[\chi - \chi^{(0)} + \nabla \cdot \boldsymbol{\chi}^{(1)}\right] \delta \kappa \mathrm{d}V \\
&- \int_{S_p} \mathbf{n} \cdot \boldsymbol{\sigma}^{(1)} : \delta \boldsymbol{\varepsilon}^p \mathrm{d}S + \int_{S_p} \mathbf{n} \cdot \mathbf{s}^{(1)} : \delta \boldsymbol{\varepsilon}^p \mathrm{d}S + \int_{S_p} \mathbf{n} \cdot \boldsymbol{\chi}^{(1)} \delta \kappa \mathrm{d}S.
\end{aligned}
\tag{38}
$$

Here the variations are arbitrary, but $\delta \boldsymbol{\varepsilon}^p = \mathbf{0}$ and $\delta \kappa = 0$ on $S_{pc}^{(1)} \cup S_{p(\text{int})}$, according to (36a).

If $(\boldsymbol{\varepsilon}^p, \kappa)$ is a solution of the differential problem, then all the integrals of (38) vanish identically by (19)–(21) and (36a,b), hence $\delta Y = 0$ for arbitrary variations $\delta \boldsymbol{\varepsilon}^p, \delta \kappa$ complying with (36a); namely, $Y$ is stationary correspondingly. Conversely, if $(\boldsymbol{\varepsilon}^p, \kappa)$ is a solution of the constrained minimum problem, $Y$ has there a stationarity point and thus the field equations (19)–(21) and the boundary conditions (36a,b) are all satisfied, that is, $\boldsymbol{\varepsilon}^p$ and $\kappa$ solve the differential problem. On the other hand, due to the assumed convexity of $\psi$, the second variation of $Y$ is positive definite and consequently the minimum problem for the functional $Y$ admits a (unique) solution. The proof is so complete. $\square$

## 6. The structural boundary-value problem

In this section, the elastic plastic solid considered in the previous sections is subjected to external actions consisting of body forces $\mathbf{b}$ in $V$, surface tractions $\mathbf{T}$ on $S_f$, imposed displacements $\mathbf{U}$ on $S_c$. Thermal-like strains are disregarded for simplicity. These actions vary in time quasi-statically and produce infinitesimal strains and displacements. The evolutive response of the body to the loads can be obtained in principle by a step-by-step analysis.

The rate problem is first considered here, that is, the body's response to load rates assigned at some known intermediate stage of the loading program, in which the flow-theory plasticity is of concern. The time-finite problem, that is, the body's response to the load at the generic time in the hypothesis of deformation-theory plasticity, will be addressed subsequently in this section.

### 6.1. Rate problem

Let us consider the functional

$$
\mathcal{L}[\dot{\mathbf{u}}, \dot{\lambda}] := \int_V \ddot{\psi} \mathrm{d}V - \int_V \dot{\mathbf{b}} \cdot \dot{\mathbf{u}} \mathrm{d}V - \int_{S_f} \dot{\mathbf{T}} \cdot \dot{\mathbf{u}} \mathrm{d}S,
\tag{39}
$$

where $\ddot{\psi}$ denotes the second time variation of $\psi$ computed in the reference state; moreover, it is:

$$
\dot{\boldsymbol{\varepsilon}} = \nabla^s \dot{\mathbf{u}}, \quad \dot{\boldsymbol{\varepsilon}}^e = \dot{\boldsymbol{\varepsilon}} - \mathbf{g} \dot{\lambda}, \quad \dot{\kappa} = \dot{\lambda} \quad \text{in } V,
\tag{40}
$$

with $\mathbf{g} = \partial \phi / \partial \boldsymbol{\rho}$ and $\dot{\boldsymbol{\varepsilon}}^p = \mathbf{g} \dot{\lambda}$. The constraints to comply with in the minimization operation are:

$$
\dot{\mathbf{u}} = \dot{\mathbf{U}} \quad \text{on } S_c, \quad \dot{\boldsymbol{\varepsilon}} = \mathbf{0} \quad \text{on } S_c^{(1)},
\tag{41a}
$$

$$
\dot{\lambda} = 0 \quad \text{in } V_y^* \cup S_{y(\text{int})} \cup S_{pc}^{(1)}, \quad \dot{\lambda} \geqslant 0 \quad \text{in } V_y,
\tag{41b}
$$

where $V_y := \{\mathbf{x} \in V: F(\boldsymbol{\rho}, \chi) = 0\}$, $V_y^* := V \setminus V_y$, $S_y := \partial V_y$, $S_{y(\text{int})} := S_y \cap V$.

$\ddot{\psi}$ is a quadratic form in the rate variables, which for simplicity sake is here assumed in the following form:

$$
\begin{aligned}
\ddot{\psi}= & \frac{1}{2} \mathbf{E}:: \dot{\boldsymbol{\varepsilon}}^{e} \dot{\boldsymbol{\varepsilon}}^{e}+\frac{1}{2} \mathbf{M}::\left(\left(\nabla \dot{\boldsymbol{\varepsilon}}^{e}\right)^{\mathrm{T}} \cdot \nabla \dot{\boldsymbol{\varepsilon}}^{e}\right)+\frac{1}{2} \mathbf{C}:: \dot{\boldsymbol{\varepsilon}}^{p} \dot{\boldsymbol{\varepsilon}}^{p}+\frac{1}{2} \mathbf{N}::\left(\left(\nabla \dot{\boldsymbol{\varepsilon}}^{p}\right)^{\mathrm{T}} \cdot \nabla \dot{\boldsymbol{\varepsilon}}^{p}\right) \\
& +\frac{1}{2} H_{0} \dot{\kappa}^{2}+\mathbf{H}_{1} \cdot \nabla \dot{\kappa} \dot{\kappa}+\frac{1}{2} \mathbf{H}_{2}: \nabla \dot{\kappa} \nabla \dot{\kappa},
\end{aligned}
\tag{42}
$$

where the moduli tensors $\mathbf{E}, \mathbf{M}, \ldots, \mathbf{H}_{2}$ are the only nontrivial tensor-valued elements of the Hessian matrix of $\psi$. $\mathbf{E}$ is the standard elasticity fourth-order moduli tensor; $\mathbf{M}, \mathbf{C}$ and $\mathbf{N}$ are fourth-order tensors with the same symmetry features as $\mathbf{E}$; $\mathbf{H}_{2}$ is second-order and symmetric. (Other restrictions that may be required by objectivity are out of concern for the present purposes.)

It can be proved that the solution to the rate boundary-value problem, if any, minimizes the functional (39) with the constraints (41a,b), and that conversely the solution to the constrained minimum problem solves the rate boundary-value problem.

**Proof.** Let the augmented functional

$$
\mathcal{L}_{a}=\mathcal{L}-\int_{S_{c}} \dot{\mathbf{r}} \cdot(\dot{\mathbf{u}}-\dot{\mathbf{U}}) \mathrm{d} S
\tag{43}
$$

be considered, where $\dot{\mathbf{r}}$ is a Lagrangian-multiplier traction rate. The first variation of $\mathcal{L}_{a}$ can be written, after application of the divergence theorem:

$$
\begin{aligned}
\delta \mathcal{L}_{a}= & \int_{V}\left\{\mathbf{E}: \dot{\boldsymbol{\varepsilon}}^{e}-\nabla \cdot\left(\nabla \dot{\boldsymbol{\varepsilon}}^{e}: \mathbf{M}\right)\right\}:\left(\nabla^{s} \delta \dot{\mathbf{u}}-\mathbf{q} \delta \dot{\lambda}\right) \mathrm{d} V+\int_{V}\left\{\mathbf{C}: \delta \dot{\boldsymbol{\varepsilon}}^{p}-\nabla \cdot\left(\nabla \dot{\boldsymbol{\varepsilon}}^{p}: \mathbf{N}\right)\right\}: \mathbf{q} \delta \dot{\lambda} \mathrm{d} V \\
& +\int_{V}\left\{H_{0} \dot{\lambda}+\mathbf{H}_{1} \cdot \nabla \dot{\lambda}-\nabla \cdot\left(\mathbf{H}_{1} \dot{\lambda}+\mathbf{H}_{2} \cdot \nabla \dot{\lambda}\right)\right\} \delta \dot{\lambda} \mathrm{d} V+\int_{S} \mathbf{n} \cdot \nabla \dot{\boldsymbol{\varepsilon}}^{e}: \mathbf{M}: \delta \dot{\boldsymbol{\varepsilon}}^{e} \mathrm{~d} S-\int_{S_{y}} \mathbf{n} \cdot \nabla \dot{\boldsymbol{\varepsilon}}^{p}: \mathbf{N}: \delta \dot{\boldsymbol{\varepsilon}}^{p} \mathrm{~d} S \\
& -\int_{S_{y}} \mathbf{n} \cdot\left(\mathbf{H}_{1} \dot{\lambda}+\mathbf{H}_{2} \cdot \nabla \dot{\lambda}\right) \delta \dot{\lambda} \mathrm{d} S-\int_{V} \dot{\mathbf{b}} \cdot \delta \dot{\mathbf{u}} \mathrm{d} V-\int_{S_{f}} \dot{\mathbf{T}} \cdot \delta \dot{\mathbf{u}}-\int_{S_{c}} \dot{\mathbf{r}} \cdot \delta \dot{\mathbf{u}} \mathrm{d} S-\int_{S_{c}}(\dot{\mathbf{u}}-\dot{\mathbf{U}}) \cdot \delta \dot{\mathbf{r}} \mathrm{d} S,
\end{aligned}
\tag{44}
$$

where the variation fields $\delta \dot{\mathbf{u}}, \delta \dot{\lambda}$ must comply with the constraints (41a,b), but in homogeneous form for $\delta \dot{\mathbf{u}}$, hence $\delta \dot{\lambda}=0$ on $S_{y}$.

Let us recognize that the stress rate tensors corresponding to (42) take on the expressions:

$$
\dot{\boldsymbol{\sigma}}=\mathbf{E}: \dot{\boldsymbol{\varepsilon}}^{e}-\nabla \cdot\left(\nabla \dot{\boldsymbol{\varepsilon}}^{e}: \mathbf{M}\right),
\tag{45a}
$$

$$
\dot{\mathbf{s}}=\mathbf{C}: \dot{\boldsymbol{\varepsilon}}^{p}-\nabla \cdot\left(\nabla \dot{\boldsymbol{\varepsilon}}^{p}: \mathbf{N}\right),
\tag{45b}
$$

$$
\dot{\chi}=H_{0} \dot{\kappa}+\mathbf{H}_{1} \cdot \nabla \dot{\kappa}-\nabla \cdot\left(\mathbf{H}_{1} \dot{\kappa}+\mathbf{H}_{2} \cdot \nabla \dot{\kappa}\right),
\tag{45c}
$$

$$
\dot{\boldsymbol{\rho}}=\dot{\boldsymbol{\rho}}_{\varepsilon}-(\mathbf{E}+\mathbf{C}): \dot{\boldsymbol{\varepsilon}}^{p}+\nabla \cdot\left[\nabla \dot{\boldsymbol{\varepsilon}}^{p}:(\mathbf{M}+\mathbf{N})\right],
\tag{45d}
$$

$$
\dot{\boldsymbol{\rho}}^{(1)}=\dot{\boldsymbol{\rho}}_{\varepsilon}^{(1)}-\nabla \dot{\boldsymbol{\varepsilon}}^{p}:(\mathbf{M}+\mathbf{N}),
\tag{45e}
$$

$$
\dot{\boldsymbol{\rho}}_{\varepsilon}=\mathbf{E}: \dot{\boldsymbol{\varepsilon}}-\nabla \cdot \dot{\boldsymbol{\rho}}_{\varepsilon}^{(1)}, \quad \dot{\boldsymbol{\rho}}_{\varepsilon}^{(1)}=\nabla \dot{\boldsymbol{\varepsilon}}: \mathbf{M}.
\tag{45f}
$$

Hence, applying the divergence theorem, Eq. (44) can be rewritten as follows:

$$
\begin{aligned}
\delta \mathcal{L}_{a}= & -\int_{V}(\nabla \cdot \dot{\boldsymbol{\sigma}}+\dot{\mathbf{b}}) \cdot \delta \dot{\mathbf{u}} \mathrm{d} V+\int_{S_{f}}(\mathbf{n} \cdot \dot{\boldsymbol{\sigma}}-\dot{\mathbf{T}}) \cdot \delta \dot{\mathbf{u}} \mathrm{d} S+\int_{S_{c}}(\mathbf{n} \cdot \dot{\boldsymbol{\sigma}}-\dot{\mathbf{r}}) \cdot \delta \dot{\mathbf{u}} \mathrm{d} S \\
& +\int_{V_{y}}[\dot{\chi}-\mathbf{g}:(\dot{\boldsymbol{\sigma}}-\dot{\mathbf{s}})] \delta \dot{\lambda} \mathrm{d} V-\int_{S_{u}}(\dot{\mathbf{u}}-\dot{\mathbf{U}}) \cdot \delta \dot{\mathbf{r}} \mathrm{d} S+\int_{S} \mathbf{n} \cdot \dot{\boldsymbol{\sigma}}^{(1)}: \delta \dot{\boldsymbol{\varepsilon}} \mathrm{d} S+\int_{S_{y}} \mathbf{n} \cdot \dot{\boldsymbol{\sigma}}^{(1)}: \mathbf{g} \delta \dot{\lambda} \mathrm{d} S \\
& -\int_{S_{y}} \mathbf{n} \cdot \dot{\mathbf{s}}^{(1)}: \mathbf{g} \delta \dot{\lambda} \mathrm{d} S-\int_{S_{y}} \mathbf{n} \cdot \dot{\chi}^{(1)} \delta \dot{\lambda} \mathrm{d} S,
\end{aligned}
\tag{46}
$$

where $\dot{\chi}-\mathbf{g}:(\dot{\boldsymbol{\sigma}}-\dot{\mathbf{s}})=-\dot{F}$.

If the set $(\dot{\mathbf{u}}, \dot{\lambda})$ solves the rate boundary-value problem, then $\dot{F} \delta \dot{\lambda} \leqslant 0$ in $V_{y}$ and thus $\delta \mathcal{L}_{a}=\delta \mathcal{L} \geqslant 0$ for arbitrary admissible variations $\delta \dot{\mathbf{u}}, \delta \dot{\lambda}$; that is, $\mathcal{L}$ has correspondingly a stationarity, or minimum, condition. Conversely, if $\delta \mathcal{L}_{a} \geqslant 0$ for arbitrary constrained variations, then necessarily the equilibrium equations are satisfied, namely

$$
\nabla \cdot \dot{\boldsymbol{\sigma}}+\dot{\mathbf{b}}=\mathbf{0} \quad \text { in } V, \quad \mathbf{n} \cdot \dot{\boldsymbol{\sigma}}=\dot{\mathbf{T}} \quad \text { on } S_{f},
$$

together with the yield conditions (33a), the boundary conditions (41a,b) and moreover the following boundary conditions:

$$
\mathbf{n} \cdot \dot{\boldsymbol{\sigma}}^{(1)}=\mathbf{0} \quad \text { on } S_{f}^{(1)}, \quad \dot{\mathbf{r}}=\mathbf{n} \cdot \dot{\boldsymbol{\sigma}} \quad \text { on } S_{c}.
$$

On the other hand, the second variation of $\mathcal{L}$ reads:

$$
\delta^{2} \mathcal{L}=\int_{V}\left[\ddot{\psi}_{e}\left(\delta \dot{\boldsymbol{\varepsilon}}^{e}, \nabla \delta \dot{\boldsymbol{\varepsilon}}^{e}\right)+\ddot{\psi}_{\mathrm{in}}\left(\delta \dot{\boldsymbol{\varepsilon}}^{e}, \delta \dot{\kappa}, \nabla \delta \dot{\boldsymbol{\varepsilon}}^{e}, \nabla \delta \dot{\kappa}\right)\right] \mathrm{d} V
$$

which is positive definite by the assumed convexity of $\ddot{\psi}$. Therefore, denoting by $\dot{\mathbf{u}}^{\prime}, \dot{\lambda}^{\prime}$ any fields complying with (41a,b), one can write:

$$
\mathcal{L}\left[\dot{\mathbf{u}}^{\prime}, \dot{\lambda}^{\prime}\right]=\mathcal{L}[\dot{\mathbf{u}}, \dot{\lambda}]+\delta \mathcal{L}+\frac{1}{2} \delta^{2} \mathcal{L} \geqslant \mathcal{L}[\dot{\mathbf{u}}, \dot{\lambda}]
$$

where the equality sign holds if, and only if, $\dot{\mathbf{u}}^{\prime} \equiv \dot{\mathbf{u}}, \dot{\lambda}^{\prime} \equiv \dot{\lambda}$. In conclusion, the solution of the rate boundary-value problem is the (unique) solution of the minimization problem. The theorem is so proved. $\square$

The theorem just presented is an extension of analogous theorems given by Mühlhaus and Aifantis (1991), Fleck and Hutchinson (2001) within a simpler context (local elasticity, gradient isotropic hardening).

### 6.2. Time-finite problem

Fleck and Hutchinson (1993, 2001) showed that deformation-theory plasticity may be useful in many instances of practice and for this reason they provided a time-finite version of the total potential energy principle for gradient plasticity (Fleck and Hutchinson, 2001). In doing that these authors adopted an Osgood-type law for plastic strain and considered the elastic strain negligible in comparison to the plastic one. Here instead both elastic and plastic strains are considered, with the plastic strain obeying time-finite plasticity laws, that is:

$$
F=\phi(\boldsymbol{\rho})-\chi-\sigma_{y} \leqslant 0, \quad \lambda \leqslant 0, \quad \lambda F=0,
$$

$$
\boldsymbol{\varepsilon}^{p}=\lambda \frac{\partial \phi}{\partial \boldsymbol{\rho}}, \quad \kappa=\lambda.
$$

These admit a dissipation function $D=D\left(\boldsymbol{\varepsilon}^{p}, \kappa\right)$ such that the dissipation stresses $\boldsymbol{\rho}, \chi$ related to a given time-finite plastic deformation mechanism $\left(\boldsymbol{\varepsilon}^{p}, \kappa\right)$ are given by

$$
\boldsymbol{\rho}=\frac{\partial D}{\partial \boldsymbol{\varepsilon}^{p}}, \quad \chi=-\frac{\partial D}{\partial \kappa}.
$$

Additionally, the related HO boundary conditions read:

$$
\boldsymbol{\varepsilon}^{e}=\mathbf{0} \quad \text { on } S_{c}^{(1)} ; \quad \varepsilon^{p}=\mathbf{0} \quad \text { and } \quad \kappa=0 \quad \text { on } S_{p c}^{(1)},
$$

$$
\mathbf{n} \cdot \boldsymbol{\sigma}^{(1)}=\mathbf{0} \quad \text { on } S_{f}^{(1)} ; \quad \mathbf{n} \cdot \mathbf{s}^{(1)}=\mathbf{0} \quad \text { and } \quad \mathbf{n} \cdot \chi^{(1)}=0 \quad \text { on } S_{p f}^{(1)},
$$

where $S=S_{c}^{(1)} \cup S_{f}^{(1)}=S_{p c}^{(1)} \cup S_{p f}^{(1)}$ (no internal elastic-plastic boundary is to be considered in the present context).

Correspondingly, the functional to be minimized is:

$$
\tilde{\mathcal{L}}\left[\mathbf{u}, \boldsymbol{\varepsilon}^{p}, \kappa\right]:=\int_{V} \psi \mathrm{d} V+\int_{V} D\left(\boldsymbol{\varepsilon}^{p}, \kappa\right) \mathrm{d} V-\int_{V} \mathbf{b} \cdot \mathbf{u} \mathrm{d} V-\int_{S_{f}} \mathbf{T} \cdot \mathbf{u} \mathrm{d} V,
$$

where $\psi$ is the free energy (1) with $\boldsymbol{e}^e = \nabla^s \mathbf{u} - \boldsymbol{\varepsilon}^p$, whereas the relevant constraints are (53a) and
$$\mathbf{u} = \mathbf{U} \quad \text{on } S_c. \tag{55}$$

It can be proved that the solution (if any) to the time-finite boundary-value problem minimizes (54) under the constraints (53a) and (55), and that conversely the (unique) minimum solution solves the time-finite boundary-value problem.

**Proof.** Proceeding as in Section 6.1, the augmented functional
$$\tilde{\mathcal{L}}_a := \tilde{\mathcal{L}} + \mathbf{r} \cdot (\mathbf{u} - \mathbf{U}) \tag{56}$$
is considered and its first variation, after application of the divergence theorem, is written as:
$$
\begin{aligned}
\delta \tilde{\mathcal{L}}_a &= \int_V \left[ \frac{\partial \psi_e}{\partial \boldsymbol{\varepsilon}^e} - \nabla \cdot \left( \frac{\partial \psi_e}{\partial \nabla \boldsymbol{\varepsilon}^e} \right) \right] : \delta (\nabla^s \mathbf{u} - \boldsymbol{\varepsilon}^p) \mathrm{d}V - \int_V \mathbf{b} \cdot \delta \mathbf{u} \mathrm{d}V \\
&+ \int_V \left[ \frac{\partial \psi_{\text{in}}}{\partial \boldsymbol{\varepsilon}^p} - \nabla \cdot \left( \frac{\partial \psi_{\text{in}}}{\partial \nabla \boldsymbol{\varepsilon}^p} \right) + \frac{\partial D}{\partial \boldsymbol{\varepsilon}^p} \right] : \delta \boldsymbol{\varepsilon}^p \mathrm{d}V + \int_V \left[ \frac{\partial \psi_{\text{in}}}{\partial \kappa} - \nabla \cdot \left( \frac{\partial \psi_{\text{in}}}{\partial \nabla \kappa} \right) + \frac{\partial D}{\partial \kappa} \right] \delta \kappa \mathrm{d}V \\
&+ \int_S \left[ \mathbf{n} \cdot \left( \frac{\partial \psi_e}{\partial \nabla \boldsymbol{\varepsilon}^e} \right) : \delta \boldsymbol{\varepsilon}^e + \mathbf{n} \cdot \left( \frac{\partial \psi_{\text{in}}}{\partial \nabla \boldsymbol{\varepsilon}^p} \right) : \delta \boldsymbol{\varepsilon}^p + \mathbf{n} \cdot \left( \frac{\partial \psi_{\text{in}}}{\partial \nabla \kappa} \right) \delta \kappa \right] \mathrm{d}S \\
&- \int_{S_f} \mathbf{T} \cdot \delta \mathbf{u} \mathrm{d}S - \int_{S_c} (\mathbf{u} - \mathbf{U}) \cdot \delta \mathbf{r} \mathrm{d}S - \int_{S_c} \mathbf{r} \cdot \delta \mathbf{u} \mathrm{d}S. \tag{57}
\end{aligned}
$$

This, again applying the divergence theorem and after recognition of the stress tensors (5)-(7), (11) and (19)-(21), takes on the form:
$$
\begin{aligned}
\delta \tilde{\mathcal{L}}_a &= - \int_V (\nabla \cdot \boldsymbol{\sigma} + \mathbf{b}) \cdot \delta \mathbf{u} \mathrm{d}V + \int_{S_f} (\mathbf{n} \cdot \boldsymbol{\sigma} - \mathbf{T}) \cdot \delta \mathbf{u} \mathrm{d}S + \int_{S_c} (\mathbf{n} \cdot \boldsymbol{\sigma} - \mathbf{r}) \cdot \delta \mathbf{u} \mathrm{d}S \\
&- \int_{S_c} (\mathbf{u} - \mathbf{U}) \cdot \delta \mathbf{r} \mathrm{d}S + \int_V \left( \frac{\partial D}{\partial \boldsymbol{\varepsilon}^p} - \boldsymbol{\rho} \right) : \delta \boldsymbol{\varepsilon}^p \mathrm{d}V + \int_V \left( \frac{\partial D}{\partial \kappa} + \chi \right) \delta \kappa \mathrm{d}V \\
&+ \int_S \mathbf{n} \cdot \boldsymbol{\sigma}^{(1)} : \delta \boldsymbol{\varepsilon}^e \mathrm{d}S + \int_S \mathbf{n} \cdot \mathbf{s}^{(1)} : \delta \boldsymbol{\varepsilon}^p \mathrm{d}S + \int_S \mathbf{n} \cdot \boldsymbol{\chi}^{(1)} \delta \kappa \mathrm{d}S. \tag{58}
\end{aligned}
$$

If the set $(\mathbf{u}, \varepsilon^p, \kappa)$ solves the time-finite boundary-value problem, then obviously it is $\delta \tilde{\mathcal{L}}_a = 0$ for arbitrary variation fields $\delta \mathbf{u}, \delta \boldsymbol{\varepsilon}^p, \delta \kappa$ complying with (53a) and (55), but the latter in homogeneous form, hence $\tilde{\mathcal{L}}_a$ is stationary correspondingly. Conversely, if the set $(\mathbf{u}, \varepsilon^p, \kappa)$ minimizes the functional $\tilde{\mathcal{L}}$ under the constraints (53a) and (55), then $\delta \tilde{\mathcal{L}}$ has to vanish identically for arbitrary variations $\delta \mathbf{u}, \delta \varepsilon^p, \delta \kappa$ complying with (53a) and (55), and therefore all integrals of (58) must vanish in their respective domains of definition. This means that the time-finite equilibrium conditions are satisfied, i.e.
$$\nabla \cdot \boldsymbol{\sigma} + \mathbf{b} = \mathbf{0} \quad \text{in } V, \quad \mathbf{n} \cdot \boldsymbol{\sigma} = \mathbf{T} \quad \text{on } S_f \tag{59}$$
and that the stresses $\boldsymbol{\rho} = \boldsymbol{\sigma} - \mathbf{s}$ and $\chi$ turn out to be the dissipative stresses related to $\boldsymbol{\varepsilon}^p$ and $\kappa$ everywhere the latter variables are not trivially vanishing. Moreover, the HO boundary conditions (53b) are satisfied, whereas $\mathbf{r} = \mathbf{n} \cdot \boldsymbol{\sigma}$ on $S_c$. The proof is so complete. $\square$

### 7. An assessment of the HO constraints by a limiting procedure

The aim of this section is to provide a motivation for the HO constraints while resting at the macrostructural scale. This goal is pursued by a simple paradigmatic infinite-length bar model subjected to the stress $\bar{\sigma} > 0$ at the remote ends – but a pure shear model might also have been chosen as in Fleck and Hutchinson (1993).

The free energy $\psi = \psi_e + \psi_{\text{in}}$ is specified for simplicity as follows:

$$
\psi_{e}=\frac{1}{2} E \varepsilon^{e 2}+\frac{1}{2} M \varepsilon^{e^{\prime} 2}, \quad \psi_{\mathrm{in}}=\frac{1}{2} H \kappa^{2}+\frac{1}{2} J \kappa^{\prime 2}
\tag{60}
$$

where $E, M, H, J$ are material constants and the prime denotes derivative with respect the abscissa $x$. The material exhibits gradient elasticity and gradient isotropic hardening. According to the results of Section 3, Eqs. (11) and (21), the differential equations governing the gradient material behaviour are:

$$
\sigma=E \varepsilon^{e}-M \varepsilon^{e^{\prime \prime}}, \quad \chi=H \kappa-J \kappa^{\prime \prime}
\tag{61}
$$

respectively for elasticity and isotropic hardening, whereas the double Cauchy stress and the double drag stress by Eqs. (5) and (7) are, respectively:

$$
\sigma^{(1)}=M \varepsilon^{e^{\prime}}, \quad \chi^{(1)}=J \kappa^{\prime}.
\tag{62}
$$

The yield condition is taken as

$$
\sigma-\chi=\sigma_{y},
\tag{63}
$$

where $\sigma = \text{const}\ (=\bar{\sigma})$ everywhere in the bar for equilibrium, $\sigma_y$ is the yield stress, and $\kappa = |\varepsilon^p|$. By hypothesis, no unloadings occur, hence the deformation-theory plasticity can be applied and $\varepsilon^p > 0$.

Let the bar be piecewise homogeneous with discontinuities at a single location, say $x=0$. Denoting $E_1, M_1, H_1, J_1$ the moduli values in the half bar $x>0$, and $E_2, M_2, H_2, J_2$ those for $x<0$, the differential equations in (61) can be solved separately for the two half bars and (assuming $\sigma_y = \text{const}$ and $\sigma > \sigma_y$) we can write:

$$
\varepsilon^{e}=\frac{\sigma}{E_{1}}\left[a_{11} \mathrm{e}^{-x / \ell_{1}}+a_{12} \mathrm{e}^{x / \ell_{1}}+1\right] \quad orall x>0,
\tag{64a}
$$

$$
\varepsilon^{e}=\frac{\sigma}{E_{2}}\left[a_{21} \mathrm{e}^{-x / \ell_{2}}+a_{22} \mathrm{e}^{x / \ell_{2}}+1\right] \quad orall x<0,
\tag{64b}
$$

$$
\varepsilon^{p}=\frac{\sigma-\sigma_{y}}{H_{1}}\left[b_{11} \mathrm{e}^{-x / \ell_{1}^{p}}+b_{12} \mathrm{e}^{x / \ell_{1}^{p}}+1\right] \quad orall x>0,
\tag{65a}
$$

$$
\varepsilon^{p}=\frac{\sigma-\sigma_{y}}{H_{2}}\left[b_{21} \mathrm{e}^{-x / \ell_{2}^{p}}+b_{22} \mathrm{e}^{x / \ell_{2}^{p}}+1\right] \quad orall x<0,
\tag{65b}
$$

where $\ell_1, \ell_2, \ell_1^p, \ell_2^p$ are internal lengths given by

$$
\ell_{\alpha}:=\sqrt{M_{\alpha} / E_{\alpha}}, \quad \ell_{\alpha}^{p}:=\sqrt{J_{\alpha} / H_{\alpha}} \quad (\alpha=1,2).
\tag{66}
$$

The integration constants can be obtained by enforcing the HO boundary conditions, which here read, Eqs. (12b,c), (22c) and (26)₂:

$$
\sigma^{(1)} \rightarrow 0, \quad \text{hence } \varepsilon^{e^{\prime}} \rightarrow 0, \quad \text{at } x \rightarrow \pm \infty,
\tag{67a}
$$

$$
\left[\left[\sigma^{(1)}\right]\right]_{x=0}=M_{1} \varepsilon^{e^{\prime}}(+0)-M_{2} \varepsilon^{e^{\prime}}(-0)=0 \quad \text{at } x=0,
\tag{67b}
$$

$$
\chi^{(1)} \rightarrow 0, \quad \text{hence } \varepsilon^{p^{\prime}} \rightarrow 0, \quad \text{at } x \rightarrow \pm \infty,
\tag{68a}
$$

$$
\left[\left[\chi^{(1)}\right]\right]_{x=0}=J_{1} \varepsilon^{p^{\prime}}(+0)-J_{2} \varepsilon^{p^{\prime}}(-0)=0 \quad \text{at } x=0
\tag{68b}
$$

besides the continuity conditions

$$
\left[\left[\varepsilon^{e}\right]\right]_{x=0}=0, \quad \left[\left[\varepsilon^{p}\right]\right]_{x=0}=0.
\tag{69}
$$

There are as many unknown constants as boundary conditions and the constants can be determined (details are skipped for brevity) to obtain

$$
\varepsilon^{e}=\frac{\sigma}{E_{1}}\left[1-\Omega_{e} \ell_{2} \mathrm{e}^{-x / \ell_{1}}\right] \quad orall x \geqslant 0,
\tag{70a}
$$

$$
\varepsilon^{e}=\frac{\sigma}{E_{2}}\left[1+\Omega_{e} \ell_{1} \mathrm{e}^{x / \ell_{2}}\right] \quad orall x \leqslant 0,
\tag{70b}
$$

![](./images/812054200497209345_4.jpg)

Fig. 1. Infinite bar with moduli jumps at $x=0$ and subjected to a traction $\sigma$ at the remote ends. Typical elastic (a) and plastic (b) strain responses.

$$
\varepsilon^{p}=\frac{\sigma-\sigma_{y}}{H_{1}}\left[1-\Omega_{p} \ell_{2}^{p} \mathrm{e}^{-x / \ell_{1}^{p}}\right] \quad \forall x \geqslant 0,
\tag{71a}
$$

$$
\varepsilon^{p}=\frac{\sigma-\sigma_{y}}{H_{2}}\left[1+\Omega_{p} \ell_{1}^{p} \mathrm{e}^{x / \ell_{2}^{p}}\right] \quad \forall x \leqslant 0,
\tag{71b}
$$

where

$$
\Omega_{e}=\frac{E_{2}-E_{1}}{\sqrt{E_{1} M_{1}}+\sqrt{E_{2} M_{2}}}=\frac{E_{2}-E_{1}}{E_{1} \ell_{1}+E_{2} \ell_{2}},
\tag{72}
$$

$$
\Omega_{p}=\frac{H_{2}-H_{1}}{\sqrt{H_{1} J_{1}}+\sqrt{H_{2} J_{2}}}=\frac{H_{2}-H_{1}}{H_{1} \ell_{1}^{p}+H_{2} \ell_{2}^{p}}.
\tag{73}
$$

Eq. $(73)_{2}$ coincides with a result given by Fleck and Hutchinson (1993) for a pure shear model.

In Figs. 1(a) and 1(b) the plots of the elastic and plastic strain profiles are reported with a few details of the gradient response. As a consequence of the double traction continuity at $x=0$, where the moduli jumps are located, the strain curves there exhibit discontinuous slopes as far as the related internal lengths are different from each other.

Suitable limit conditions for the half bar $x<0$ are worth being discussed at this point.

### 7.1. First limit case: $E_{2} \rightarrow \infty, H_{2} \rightarrow \infty$

Let the material of the half bar $x<0$ be a gradient material $(M_{2} \neq 0, J_{2} \neq 0)$, but *elastically and plastically rigid* $(E_{2} \rightarrow \infty, H_{2} \rightarrow \infty)$. Correspondingly, it can be found that the general solution (70a,b) and (71a,b) takes on the limit form:

$$
\varepsilon^{e}=\frac{\sigma}{E_{1}}\left(1-\mathrm{e}^{-x / \ell_{1}}\right) \quad \forall x \geqslant 0,
\tag{74a}
$$

$$
\varepsilon^{p}=\frac{\sigma-\sigma_{y}}{H_{1}}\left(1-\mathrm{e}^{-x / \ell_{1}^{p}}\right) \quad \forall x \geqslant 0,
\tag{74b}
$$

$$
\varepsilon^{e}=\varepsilon^{p}=0 \quad \forall x \leqslant 0.
\tag{75}
$$

This limit response is plotted in Figs. 2(a) and 2(b).

Let the rigid half bar be removed and substituted with suitable constraints applied upon the deformable half bar $x>0$ at the end $x=0$. These constraints consist in an ordinary constraint impeding the displacement $u$, and two HO constraints impeding, respectively, the onset of the elastic and plastic strains $\varepsilon^{e}, \varepsilon^{p}$ as macroscopic nonlocality-source strains for the half bar $x>0$. A limit gradient bar model is so obtained, with ordinary and HO constraints at $x=0$ and subjected to the traction $\sigma$ at the other (remote) end. The response of this idealized bar model is governed by the differential equations:

$$
\sigma=E_{1} \varepsilon^{e}-M_{1} \varepsilon^{e^{\prime \prime}}, \quad \chi=H_{1} \kappa-J_{1} \kappa^{\prime \prime}
\tag{76}
$$

![](./images/812054200497209345_5.jpg)

Fig. 2. Infinite bar with the half part $x<0$ elastically and plastically rigid, subjected to a traction $\sigma$ at the remote ends. Typical elastic (a) and plastic (b) strain responses.

with the accompanying HO boundary conditions

$$
\varepsilon^{e}=\varepsilon^{p}=0 \quad \text { at } x=0,\qquad(77a)
$$

$$
\sigma^{(1)}=M_{1} \varepsilon^{e^{\prime}}=0 \quad \text { and } \quad \chi^{(1)}=J_{1} \varepsilon^{p^{\prime}}=0 \quad \text { at } x \rightarrow+\infty.\qquad(77b)
$$

It is an easy task to verify that the solution to (76)-(77a,b) coincides with (74a,b).

### 7.2. Second limit case: $M_{2}=J_{2}=0, E_{2} \rightarrow \infty, H_{2} \rightarrow \infty$

Let the material of the half bar $x<0$ be a local-type one $(M_{2}=J_{2}=0)$ and elastically and plastically rigid $(E_{2} \rightarrow \infty, H_{2} \rightarrow \infty)$. Correspondingly, it is found that the general solution (70a,b) and (71a,b) takes on the limit form:

$$
\varepsilon^{e}=\frac{\sigma}{E_{1}}, \quad \varepsilon^{p}=\frac{\sigma-\sigma_{y}}{H_{1}} \quad \forall x>0,\qquad(78a)
$$

$$
\varepsilon^{e}=\varepsilon^{p}=0 \quad \forall x<0.\qquad(78b)
$$

This, for $x>0$, coincides with the local-type solution, although the material is there a gradient material.

Again, let the rigid half bar $x<0$ be removed and substituted by only an ordinary constraint applied at $x=0$. The limit bar model so obtained consists in the deformable half bar $x>0$, ordinarily constrained at $x=0$ and subjected to the traction $\sigma$ at the remote end. The response of this limit bar model is governed by (76) with the accompanying HO boundary conditions:

$$
\sigma^{(1)}=M_{1} \varepsilon^{e^{\prime}}=0, \quad \text { hence } \varepsilon^{e^{\prime}}=0, \quad \text { at } x=0 \text { and } x \rightarrow+\infty,\qquad(79a)
$$

$$
\chi^{(1)}=J_{1} \varepsilon^{p^{\prime}}=0, \quad \text { hence } \varepsilon^{p^{\prime}}=0, \quad \text { at } x=0 \text { and } x \rightarrow+\infty.\qquad(79b)
$$

The solution to (76) and (79a,b) can be easily shown to coincide with (78a).

### 7.3. Third limit case: $M_{2}=0, E_{2} \rightarrow \infty, H_{2} \rightarrow \infty$

Let the material of the half bar $x<0$ be local elastic $(M_{2}=0)$, but exhibit gradient isotropic hardening $(J_{2} \neq 0)$; also let it be elastically and plastically rigid $(E_{2} \rightarrow \infty, H_{2} \rightarrow \infty)$. The general solution (70a,b) and (71a,b) is correspondingly found to take on the form:

$$
\varepsilon^{e}=\frac{\sigma}{E_{1}} \quad \forall x>0,\qquad(80a)
$$

$$
\varepsilon^{p}=\frac{\sigma-\sigma_{y}}{H_{1}}\left(1-\mathrm{e}^{-x / \ell_{1}^{p}}\right) \quad \forall x>0,\qquad(80b)
$$

$$
\varepsilon^{e}=\varepsilon^{p}=0 \quad \forall x<0\qquad(80c)
$$

showing that, for $x > 0$, the elastic response coincides with the local one, in spite of the fact that the material is there gradient elastic.

Like in the first limit case previously discussed, the rigid half bar $x < 0$ is removed and substituted with an ordinary and a plasticity HO constraint applied at $x = 0$. Again, the limit bar model consists in the deformable half bar $x > 0$, clamped with an ordinary constraint and a plasticity HO constraint in $x = 0$, impeding the onset of the plastic strain $\varepsilon^p$ as nonlocality-source strain for the half bar $x > 0$. The response of the limit bar model is therefore governed by the field equations (89) accompanied by the HO boundary conditions:

$$
\sigma^{(1)}=M_{1} \varepsilon^{e^{\prime}}=0, \quad \text { hence } \varepsilon^{e^{\prime}}=0, \quad \text { at } x=0 \text { and } x \rightarrow+\infty,\qquad(81a)
$$

$$
\varepsilon^{p}(0)=0 ; \quad \chi^{(1)}=J_{1} \varepsilon^{p^{\prime}}=0, \quad \text { hence } \varepsilon^{p^{\prime}}=0, \quad \text { at } x \rightarrow+\infty.\qquad(81b)
$$

The solution of (76) and (81a,b) is found to coincide with (70a,b).

In conclusion of this subsection, we observe that the above results, although obtained within a restricted context (one-dimensional problem, deformation-theory plasticity), can be extrapolated by conceiving the existence, in a gradient elastic/plastic body, of distinct idealized HO constraints for elasticity and plasticity. These constraints are kinematically characterized by their ability to impede, respectively, the onset of elastic strain and the plastic strain, and statically characterized by their ability to react with double tractions, work-conjugate of the impeded strains.

These HO constraints, which add to the ordinary constraints, can be conceived as idealized devises applied upon the boundary surface, whose action is like that of a substrate composed of either gradient, or local-type, material which at the limit becomes elastically and/or plastically rigid.

The above limiting procedure – previously adopted by Fleck and Hutchinson (1993), although not systematically – does not provide any microstructural motivation or interpretation for the HO constraints. In the framework of gradient plasticity, Fleck and Hutchinson (1993, 2001), Shu et al. (2001) and others interpreted the related HO constraints as barriers against which the moving dislocations are arrested. In an analogous way, the elasticity HO constraints may be macroscopically interpreted as devices blocking the formation, coalescence and growth of microstructure defects and inhomogeneities in the vicinity of the clamped surface, but this point obviously needs further study.

Remark 3. Like the HO boundary conditions, the HO constraints can in principle be of order $n = 1,2,\dots$ in relation to the order of the displacement gradient they are able to impede ($n = 0$ corresponds to standard boundary conditions and ordinary constraints). However, in this paper the order $n = 1$ is always of interest, thus the simple indication "HO" cannot produce misconfusion.

## 8. Applications

### 8.1. Homogeneous hardening bar in tension

Let a homogeneous bar of length $L$ be clamped at both ends with ordinary, as well as with HO constraints capable to impede the onset of the elastic and plastic strains, and let it be subjected to the displacements $u = U/2$ at the end $x = L/2$, $u = -U/2$ at the other end $x = -L/2$. The material is gradient elastic and exhibits gradient isotropic hardening, and thus obeys the differential equations (61). In the hypothesis of no unloadings, hence of applicability of the deformation-theory plasticity, these field equations can be written as

$$
\varepsilon^{e}-\ell^{2} \varepsilon^{e^{\prime \prime}}=\sigma / E, \quad \varepsilon^{p}-\ell_{p}^{2} \varepsilon^{p^{\prime \prime}}=\left(\sigma-\sigma_{y}\right) / H,\qquad(82)
$$

where $\ell:=\sqrt{M / E}$, $\ell_{p}:=\sqrt{J / H}$. Taking into account the symmetry with respect to the middle section $x = 0$, as well as of the HO boundary conditions $\varepsilon^e = \varepsilon^p = 0$ at $x = \pm L/2$, we easily find:

$$
\varepsilon^{e}=\frac{\sigma}{E}\left(1-\frac{\cosh (x / \ell)}{\cosh z}\right), \quad \varepsilon^{p}=\frac{\sigma-\sigma_{y}}{H}\left(1-\frac{\cosh \left(x / \ell_{p}\right)}{\cosh z_{p}}\right),\qquad(83)
$$

where $z$ and $z_p$ denote the size coefficients defined as

$$
z:=L / 2 \ell, \quad z_{p}:=L / 2 \ell_{p}.\qquad(84)
$$

![](./images/812054200497209345_6.jpg)

Fig. 3. Plot of the size factor $\varphi=\varphi(z)$ relating to the homogeneous gradient bar in extension of Fig. 4.

Since $u'=\varepsilon^{e}$ for $\sigma<\sigma_{y}$ and $u'=\varepsilon^{e}+\varepsilon^{p}$ for $\sigma>\sigma_{y}$, integration with respect to $x$ and with the standard boundary conditions on $u$ at $x=\pm L/2$, we can easily obtain the stress/displacement relations in the elastic and plastic regimes. For this purpose, let the following size factor $\varphi(z)$ be introduced, that is:

$$
\varphi(z):=z /(z-\tanh z)
\tag{85}
$$

(see Fig. 3). Also, let $\widehat{E}$, $\widehat{H}$ denote the size-effect-amplified elastic and hardening moduli defined as

$$
\widehat{E}:=E \varphi(z), \quad \widehat{H}:=H \varphi\left(z_{p}\right)
\tag{86}
$$

and $\widehat{E}_{t}$ the related tangent modulus, that is

$$
\widehat{E}_{t}=\widehat{E} \widehat{H} /(\widehat{E}+\widehat{H}).
\tag{87}
$$

Then, the stress-displacement relations prove to be as follows:

$$
\sigma=\widehat{E} U / L \quad \text { for } U \leqslant U^{e},
\tag{88a}
$$

$$
\sigma=\sigma_{y}+\widehat{E}_{t}\left(U-U^{e}\right) / L \quad \text { for } U \geqslant U^{e},
\tag{88b}
$$

where $U^{e}$ is the ends displacement at the elastic limit, i.e.

$$
U^{e}=\sigma_{y} L / \widehat{E}.
\tag{89}
$$

In Fig. 4(a) the stress-displacement relations (88a,b) are plotted assuming $\sigma_{y}=\sigma_{y}^{0}=$ constant, in Fig. 4(b) the same relations are plotted assuming $\sigma_{y}$ size dependent, for instance in the form $\sigma_{y}=\sigma_{y}^{0} \sqrt{\varphi(z)}$, but other forms of size dependence for the yield stress can be envisioned (Fredriksson and Gudmundson, 2005).

Fleck et al. (1994) reported the results of experiments on thin wires of diameter $a$ in the range from 12 to $170 \mu \mathrm{m}$, showing that the stress-displacement plots vary quite moderately on varying $a$. The analytical solution (88a,b) is unable to capture these (modest) experimental cross section size effects because it is independent of $a$ (the strain is uniform in the cross section). The size effects shown by the analytical solution (88a,b) arise from the HO constraints located at the bar ends, by which the elastic and plastic strain responses are forced to exhibit a continuous pattern with zero end values. In order that (in accord with the mentioned experimental results) the gradient bar response exhibits no size effects of any kind, no HO constraint are to be located at the bar ends, in which case the HO boundary conditions are to be expressed by equating to zero the double tractions, that is, $M \varepsilon^{e^{\prime}}=J \varepsilon^{p^{\prime}}=0$, hence $\varepsilon^{e^{\prime}}=\varepsilon^{p^{\prime}}=0$, at $x=\pm L / 2$. Under these conditions, the gradient solution (105a,b) is replaced by the local solution, that is:

$$
\sigma=E U / L \quad \text { for } U \leqslant U^{e},
\tag{90}
$$

$$
\sigma=\sigma_{y}+E_{t}\left(U-U^{e}\right) / L \quad \text { for } U \geqslant U^{e},
\tag{91}
$$

where $U^{e}=\sigma_{y} L / E$ and $E_{t}=E H /(E+H)$.

![](./images/812054200497209345_7.jpg)

Fig. 4. Homogeneous gradient elastic-plastic bar clamped with ordinary and HO constraints at the ends $x=0$, $x=L$ and subjected to ends relative displacement $U$, with $\ell_p=\ell$. Stress-displacement diagrams for different values of the internal length $\ell$: (a) yield stress $\sigma_y=\sigma_y^0=$ const.; (b) yield stress $\sigma_y=\sigma_y^0(\varphi(z))^{1/2}$ (size dependent).

### 8.2. Semi-infinite hardening bar with nonhomogeneous yield stress

A semi-infinite bar $x\geqslant0$ is considered, clamped with ordinary and HO constraints at $x=0$ and subjected to the traction $\sigma>0$ at the remote end. The material is gradient elastic with gradient isotropic hardening ($H>0$) and possesses a yield stress $\sigma_y$ varying linearly as
$$
\sigma_y=\sigma_y^0+Cx, \tag{92}
$$
where $C>0$ is a given constant. The governing field equations are as in Eq. (61). The elastic strain is easily found as (see Eq. (64a)):
$$
\varepsilon^e=\frac{\sigma}{E}\left(1-\mathrm{e}^{-x/\ell}\right), \tag{93}
$$
where $\ell:=\sqrt{M/E}$. Eq. $(61)_2$, combined with the yield condition $\sigma-\chi=\sigma_y$, gives the differential equation:
$$
\varepsilon^p-\ell_p^2\varepsilon^{p''}=\frac{\sigma-\sigma_y^0}{H}-\frac{Cx}{H}, \tag{94}
$$
where $\ell_p:=\sqrt{J/H}$. The general solution of (107) is
$$
\varepsilon^p=\frac{\sigma-\sigma_y^0}{H}\left(b_1\mathrm{e}^{x/\ell_p}+b_2\mathrm{e}^{-x/\ell_p}+1\right)-\frac{Cx}{H} \tag{95}
$$
which holds for $0\leqslant x\leqslant x_p$, whereas $\varepsilon^p=0\ \forall x>x_p$. The unknown quantities $b_1$, $b_2$ and $x_p$ are to be determined by the HO boundary conditions, which read:
$$
\varepsilon^p(0)=\varepsilon^p(x_p)=0,\quad \varepsilon^{p'}(x_p)=0. \tag{96}
$$
(Note: $x_p$ is the current location of the moving internal elastic/plastic boundary, hence both the plastic strain $\varepsilon^p$ and the related double traction $J\varepsilon^{p'}$ have there to vanish.) Skipping the analytical details for brevity, we can write the solution as:
$$
\varepsilon^p(x)=\frac{\sigma-\sigma_y^0}{H}\left[1-\mathrm{e}^{-x/\ell_p}-\left(1-\mathrm{e}^{-\xi}\right)\frac{\mathrm{e}^{x/\ell_p}-\mathrm{e}^{-x/\ell_p}}{\mathrm{e}^{\xi}-\mathrm{e}^{-\xi}}\right]+\frac{C\ell_p}{H}\left[\xi\frac{\mathrm{e}^{x/\ell_p}-\mathrm{e}^{-x/\ell_p}}{\mathrm{e}^{\xi}-\mathrm{e}^{-\xi}}-\frac{x}{\ell_p}\right] \tag{97}
$$
which holds for $0\leqslant x\leqslant x_p$ and $\xi:=x_p/\ell_p$. The unknown $\xi$ is the root of the transcendental equation:
$$
\frac{1-\mathrm{e}^{-\xi}(1+\tanh\xi)}{\xi-\tanh\xi}=\frac{C\ell_p}{\sigma-\sigma_y^0}. \tag{98}
$$

The strains $\varepsilon^e$ and $\varepsilon^p$ are plotted in Figs. 5(a) and 5(b) as functions of $x$. The total drag stress proves to be: $\chi=\sigma-\sigma_y^0-Cx$ for $0\leqslant x<x_p$, but $\chi=0$ for $x>x_p$: it thus is discontinuous at $x=x_p$, as geometrically sketched in Fig. 5(c).

![](./images/812054200497209345_8.jpg)

Fig. 5. Semi-infinite gradient elastic-plastic bar with linearly varying yield stress, clamped at $x=0$ with ordinary and OH constraints and subjected to a traction $\sigma$ at the remote end: (a) elastic strain response; (b) plastic strain response; (c) total hardening stress $\chi$; ($\sigma/E=0.02$; $C\ell_p/(\sigma_y-\sigma_y^0)=0.066$; $\ell_p=\ell=10$ cm).

### 8.3. Beam cross section in bending

A beam cross section in bending is considered, which is rectangular with dimensions $b\times 2h$, Fig. 6(a). The material exhibits a local elasticity law, $\sigma=E(\varepsilon-\varepsilon^p)$, and a gradient isotropic hardening governed by the differential equation $\chi=H(\varepsilon^p-\ell_p^2\varepsilon^{p''})$, where $E$ and $H>0$ are the elastic and hardening moduli. The total strain is given by the linear law $\varepsilon=Kx$, where $K>0$ is the imposed bending curvature. The yield function is taken as $|\sigma-\chi|=\sigma_y$. No unloadings occur, hence the deformation-theory plasticity is applicable. The problem being antisymmetric with respect to the middle cord $x=0$, the half section $x>0$, where $\sigma-\chi>0$, is considered for the computation.

In analogy with the previous examples, the differential equation for the plastic strain $\varepsilon^p(x)$ is easily found to be:

$$
\varepsilon^{p}-\left(\frac{\ell_{p}}{\mu}\right)^{2} \varepsilon^{p \prime \prime}=\frac{\mu^{2}-1}{\mu^{2}}\left(K x-\varepsilon_{y}\right) \quad\left(x_{p} \leqslant x \leqslant h\right),
\tag{99}
$$

where
$$
\mu:=\sqrt{1+\frac{E}{H}}, \quad \varepsilon_{y}:=\frac{\sigma_{y}}{E}.
\tag{100}
$$

The general solution of (99) is, with the notation $X=x/h$:

$$
\varepsilon^{p}(X)=A \cosh \frac{X}{\beta}+B \sinh \frac{X}{\beta}+\frac{\mu^{2}-1}{\mu^{2}}\left(\bar{\varepsilon} X-\varepsilon_{y}\right)
\tag{101}
$$

which holds for $X_p\leqslant X\leqslant 1$ and
$$
\beta:=\frac{\ell_{p}}{\mu h}, \quad \bar{\varepsilon}:=K h.
\tag{102}
$$

![](./images/812054200497209345_9.jpg)

![](./images/812054200497209345_10.jpg)

![](./images/812054200497209345_11.jpg)

![](./images/812054200497209345_12.jpg)

![](./images/812054200497209345_13.jpg)

![](./images/812054200497209345_14.jpg)

Fig. 6. Cross section of an elastic-plastic beam in bending: (a) geometry and total strain profile; (b) location $X_p=x_p/h$ of the moving elastic/plastic boundary plotted as a function of the adimensional curvature $\bar{\varepsilon}=Kh$ for different values of $\ell_p$; (c) plastic strain $(\varepsilon_p)$, stress $(\sigma)$ and total hardening stress $(\chi)$ profiles for $X_p>0$ (partially plastified cross section); (d) analogous profiles for $X_p=0$ (fully plastified cross section).

For $X_p>0$ (cross section partially plastified), there are three HO boundary conditions for the plastified zone, that is:
$$
\varepsilon^{p}\left(X_{p}\right)=\varepsilon^{p \prime}\left(X_{p}\right)=\varepsilon^{p \prime}(1)=0,\qquad(103)
$$
whereas for $X_p=0$ (cross section fully plastified, the cord $X=X_p$ ceases being a moving boundary, so the second condition of (103) drops), the HO boundary conditions reduce to only two, that is:
$$
\varepsilon^{p}(0)=\varepsilon^{p \prime}(1)=0.\qquad(104)
$$

By (101) together with the first and third of (103), we obtain the coefficients $A$ and $B$ as in the following:
$$
A=\frac{\mu^{2}-1}{\mu^{2} \cosh \left(\left(1-X_{p}\right) / \beta\right)}\left[\beta \bar{\varepsilon} \sinh \frac{X_{p}}{\beta}-\left(\bar{\varepsilon} X_{p}-\varepsilon_{y}\right) \cosh \frac{1}{\beta}\right],\qquad(105a)
$$

$$
B=-\frac{\mu^{2}-1}{\mu^{2} \cosh \left(\left(1-X_{p}\right) / \beta\right)}\left[\beta \bar{\varepsilon} \cosh \frac{X_{p}}{\beta}-\left(\bar{\varepsilon} X_{p}-\varepsilon_{y}\right) \sinh \frac{1}{\beta}\right]\qquad(105b)
$$

![](./images/812054200497209345_15.jpg)

Fig. 7. Adimensionalized bending moment $M/M_e$ plotted as a function of the ratio $\bar{\varepsilon}/\varepsilon_y$, related to the beam cross section of Fig. 6, for different values of $\ell_p$ and size independent yield stress.

which hold also in the limit case $X_p=0$. Using the second condition of (103), we obtain the equation

$$
\Phi\left(X_{p}\right):=\frac{\sinh \left(\left(1-X_{p}\right) / \beta\right)}{X_{p} \sinh \left(\left(1-X_{p}\right) / \beta\right)+\beta\left(\cosh \left(\left(1-X_{p}\right) / \beta\right)-1\right)}=\frac{\bar{\varepsilon}}{\varepsilon_{y}}
\tag{106}
$$

which is to be used to evaluate the abscissa $X_p$ as a function of $\bar{\varepsilon}$. The quantity

$$
\bar{\varepsilon}^{*}=\varepsilon_{y} \Phi(0)
\tag{107}
$$

specifies the value of the increasing curvature, $K^{*}=\bar{\varepsilon}^{*} / h$, for which the cross section starts being fully plastified. For $\bar{\varepsilon}>\bar{\varepsilon}^{*}$, the coefficients (105a,b) take on the values

$$
A=A^{*}:=\frac{\mu^{2}-1}{\mu^{2}} \varepsilon_{y}, \quad B=B^{*}:=-\frac{\mu^{2}-1}{\mu^{2}}\left(\frac{\beta \bar{\varepsilon}}{\cosh (1 / \beta)}+\varepsilon_{y} \tanh \frac{1}{\beta}\right).
\tag{108}
$$

In Fig. 6(b) the abscissa $X_p$ is plotted as a function of the ratio $\bar{\varepsilon}/\varepsilon_y$ for different values of $\ell_p$. In Figs. 6(c₁), 6(c₂), the plastic strain, the stress and the (total) hardening force profiles are reported for the cross section partially plastified $(X_p>0, \bar{\varepsilon}<\bar{\varepsilon}^{*})$ and for a particular value of $\ell_p$; the peculiar discontinuity of $\chi$ at $X=X_p$ is again encountered. Similar profiles are shown in Figs. 6(d₁), 6(d₂) for the fully plastified cross section $(X_p=0, \bar{\varepsilon}>\bar{\varepsilon}^{*})$, where $\chi$ exhibits a jump at $X=X_p=0$. In Fig. 7, the adimensional bending moment $M/M_e$ is plotted as a function of the ratio $\bar{\varepsilon}/\varepsilon_y$ for different values of $\ell_p$, where $M_e:=2bh^2\sigma_y$ (elastic limit bending moment).

## 9. Comments and conclusion

A thermodynamic framework, useful for a consistent formulation of gradient dependent material models, has been presented, in which: (i) the free energy includes the strain gradients as internal variables, (ii) the Clausius-Duhem inequality contains the energy residual as an additional state variable, (iii) the insulation condition and the locality recovery condition are to be satisfied, and (iv) the Onsager reciprocity principle is applicable. This framework substantially coincides with analogous ones previously proposed by the author (Polizzotto, 2003a, 2003b), but it is here enriched by the locality recovery condition (so far used only in the context of nonlocal integral elasticity, Polizzotto et al. (2006)).

In the formulations inspired to the above thermodynamic framework, the energy residual is the only new state variable to introduce ab initio, whereas all other state variables, required by the gradient nature of the material behaviour, are obtained as a by-product of the procedure, each endowed with a state equation. This procedural scheme is theoretically well motivated and leads without uncertainties to the pertinent restrictions on the constitutive equations, including the HO boundary conditions. It seems to be somewhat advantageous with respect to other procedures based on an extended form of the virtual work principle (see e.g. Gurtin, 2003, 2004; Gurtin and Needleman, 2005; Gudmundson, 2004), in which in fact several new state variables, more than the strictly necessary amount, are to be introduced into the formulation.

The presented gradient elastic/gradient plastic constitutive model conforms to the above thermodynamic framework. The multigradient feature of the model has been useful for the assessment of the relevant HO boundary conditions. These in fact are conceptually different and possess different physical bases in elasticity and in plasticity (although these differences are not fully clear at present). The proposed constitutive model is an improvement of previous models by the author (Polizzotto, 2003a, 2003b) for many aspects and in particular for the HO boundary conditions.

These HO boundary conditions prove to be all homogeneous. This fact may be viewed as a weak point of the present theory. However, there is a consistency in this homogeneity feature of the HO boundary conditions. These in fact, as part of the material constitutive equations directly derived from the second thermodynamics principle, cannot contain any boundary data and thus must exhibit a homogeneous form. Anyway, this point remains open to future investigations.

The main original contributions of the present paper can be summarized as follows:

I. A clear assessment of the HO boundary conditions for gradient elasticity and gradient plasticity, respectively, and of their basic role in the deformation process of a gradient continuum: indeed, they guarantee that no long distance energy is allowed to flow through the boundary surface, such that the body remains constitutively insulated during deformation. These HO boundary conditions – obtained as part of the relevant constitutive equations via the Clausius–Duhem inequality – improve analogous conditions of the literature (Fleck and Hutchinson, 2001; Gurtin, 2003; Gudmundson, 2004; Fredriksson and Gudmundson, 2005; Gurtin and Needleman, 2005) and fill a gap in relation to the moving internal elastic/plastic boundary, for which no clear boundary condition had been advanced previously.

II. The ascertainment, via the locality recovery condition, of the necessity of a restriction upon the free energy potential (this has to depend on the strain gradients homogeneously with a degree larger than one) in order to guarantee that the gradient material model behaves as a local model in the case of gradient-free deformation mechanism.

The rather academic numerical examples reported in this work were chosen with the intent to explain the correct way to enforce, in the author’s opinion, the HO boundary conditions, especially those related to the moving internal elastic/plastic boundary. Further research work is needed, in particular to envisage satisfactory micromechanics-based motivations for the HO constraints, as well as macroscopic rules to specify the right boundary locations for these constraints.

### Acknowledgement

This paper is part of a research project sponsored by the Italian Government, MIUR.

### Appendix A. Notation

As a rule, a compact notation is used, with boldface letters to denote vectors and tensors. The scalar product between vectors and tensors is denoted by suitably shaped dot marks, each with as many dots as the number of couples of contracted indices. In the case of more than one couple of contracted indices, the contraction proceeds from the couple of indices in the closest position to each other, and then continues with another couple analogously. For instance, if $\mathbf{a} = \{a_i\}$, $\mathbf{B} = \{B_{ij}\}$, $\mathbf{C} = \{C_{ijk}\}$ and $\mathbf{D} = \{D_{ijkh}\}$ are a vector and tensors, their scalar products can be written as follows: $\mathbf{a} \cdot \mathbf{B} = \{a_i B_{ij}\}$, $\mathbf{B} \cdot \mathbf{a} = \{B_{ij} a_j\} = \mathbf{a} \cdot \mathbf{B}^\mathrm{T}$, $\mathbf{B} : \mathbf{C} = \{B_{ij} C_{jik}\}$, $\mathbf{D} \vdots \mathbf{C} = \{D_{ijkh} C_{h kj}\}$, $\mathbf{D} :: \mathbf{aC} = D_{ijkh} a_h C_{kji}$, where the notation $\mathbf{aC} = \{a_i C_{jkh}\}$ is the tensor product of $\mathbf{a}$ by $\mathbf{C}$ and the index summation rule for repeated indices is applied. Also, $\mathbf{a} \cdot \mathbf{D} \vdots \mathbf{C} = (\mathbf{a} \cdot \mathbf{D}) \vdots \mathbf{C}$, that is, contractions proceed from the felt to the right. Orthogonal Cartesian coordinates $\mathbf{x} = (x_1, x_2, x_3)$ are used throughout. The spatial gradient $\nabla = \{\partial_i\}$ obeys the rule: $\nabla AB = (\nabla A) B$, but $\nabla(AB) = (\nabla A) B + A(\nabla B)$; also, $\nabla^s$ denotes the symmetric part of $\nabla$. An upper dot indicates time rate. The symbol $:=$ means equality by definition; $(\cdot)^\mathrm{T}$ denotes the transpose of $(\cdot)$. Other symbols are defined in the text at their first appearance.

### References

Acharya, A., Bassani, J.L., 2000. Incompatibility and crystal plasticity. J. Mech. Phys. Solids 48, 299–314.

Aifantis, E.C., 1984. On the microstructural origins of certain inelastic models. Trans. ASME J. Eng. Mater. Technol. 106, 326–330.

Aifantis, E.C., 1999a. Gradient deformation models at nano-, micro- and macro-scales. ASME J. Eng. Mater. 121, 189–202.

Aifantis, E.C., 1999b. Strain gradient interpretation of size effects. Int. J. Fracture 95, 299–314.

Aifantis, E.C., 2003. Update on a class of gradient theories. Mech. Mater. 35, 259–280.

Altan, B.S., Aifantis, E.C., 1997. On some aspects in the special theory of gradient elasticity. J. Mech. Behavior Mater. 8, 231–282.

Bassani, J.L., Needleman, A., Van Der Giessen, E., 2001. Plastic flow in a composite: a comparison of nonlocal continuum and discrete dislocation predictions. Int. J. Solids Struct. 38, 833–853.

Benvenuti, E., Borino, G., Tralli, A., 2002. A thermodynamically consistent nonlocal formulation of damaging materials. Eur. J. Mech. A Solids 21, 535–553.

Colemann, B.D., Gurtin, M.E., 1967. Thermodynamics with internal variables. J. Chem. Phys. 47, 597–613.

de Borst, R., Sluys, L.J., Mühlhaus, H.-B., 1993. Fundamental issues in finite element analysis of localization of deformation. Eng. Comput. 10, 99–121.

de Borst, R., Pamin, J., Sluys, L.J., 1995. Gradient plasticity for localization problems in quasi-brittle and frictional materials. In: Owen, D.R.J., Oñate, E., Hinton, E. (Eds.), Computational Plasticity, Fundamentals and Applications. Pineridge Press, Swansea, UK, pp. 509–533.

Edelen, D.G.B., Laws, N., 1971. Thermodynamics with internal variables. J. Chem. Phys. 47, 597–613.

Eringen, A.C., 1972. Nonlocal polar elastic continua. Int. J. Eng. Sci. 10, 1–6.

Eringen, A.C., Edelen, D.G.B., 1972. Nonlocal elasticity. Int. J. Eng. Sci. 10, 233–248.

Fleck, N.A., Hutchinson, J.W., 1993. A phenomenological theory for strain gradient effects in plasticity. J. Mech. Phys. Solids 41, 1825–1857.

Fleck, N.A., Hutchinson, J.W., 1997. Strain gradient plasticity. Adv. Appl. Mech. 33, 261–295.

Fleck, N.A., Hutchinson, J.W., 2001. A reformulation of strain gradient plasticity. J. Mech. Phys. Solids 49, 2245–2271.

Fleck, N.A., Muller, G.M., Ashby, M.F., Hutchinson, J.W., 1994. Strain gradient plasticity: theory and experiments. Acta Metall. Mater. 42, 475–487.

Fredriksson, P., Gudmundson, P., 2005. Size-dependent yield strength of thin films. Int. J. Plasticity 21, 1834–1854.

Gao, H., Huang, Y., Nix, W.D., Hutchinson, J.W., 1999. Mechanism-based strain gradient plasticity—I. Theory. J. Mech. Phys. Solids 47, 1239–1263.

Germain, P., Nguyen, Q.S., Suquet, P., 1983. Continuum thermodynamics. ASME J. Appl. Mech. 50, 731–742.

Gudmundson, P., 2004. A unified treatment of strain gradient plasticity. J. Mech. Phys. Solids 52, 1379–1406.

Gurtin, M.E., 2000. On the plasticity of single crystals: free energy, microforces, plastic-strain gradients. J. Mech. Phys. Solids 48, 989–1036.

Gurtin, M.E., 2002. A gradient theory of single-crystal viscoplasticity that accounts for geometrically necessary dislocations. J. Mech. Phys. Solids 50, 5–32.

Gurtin, M.E., 2003. On a framework for small-deformation viscoplasticity: free energy, microforces, plastic-strain gradients. J. Plasticity 19, 47–90.

Gurtin, M.E., 2004. A gradient theory of small-deformation isotropic plasticity that accounts for Burgers vector and for dissipation due to plastic spin. J. Mech. Phys. Solids 52, 2545–2568.

Gurtin, M.E., Needleman, A., 2005. Boundary conditions in small-deformation single-crystal plasticity that account for the Burger vector. J. Mech. Phys. Solids 53, 1–31.

Lam, D.C.C., Yang, F., Chong, A.C.M., Wang, J., Tong, P., 2003. Experiments and theory in strain gradient elasticity. J. Mech. Phys. Solids 51, 1477–1508.

Lasry, D., Belytscko, J.L., 1988. Localization limiters in transient problems. Int. J. Solids Struct. 24, 581–597.

Lemaitre, J., Chaboche, J.-L., 1990. Mechanics of Solid Materials. Cambridge University Press, Cambridge.

Liebe, T., Steinmann, P., 2001. Theory and numerics of a thermodynamically consistent framework for geometrically linear gradient plasticity. Int. J. Numer. Methods Engrg. 51, 1437–1467.

Liebe, T., Steinmann, P., Benallal, A., 2001. Theoretical and computational aspects of a thermodynamically consistent framework for geometrically linear damage. Comput. Methods Appl. Mech. Engrg. 190, 6555–6576.

Mindlin, R.D., 1965. Second gradient of strain and surface-tension in elasticity. Int. J. Solids Struct. 1, 417–438.

Mindlin, R.D., Eshel, N.N., 1968. On first strain-gradient theories in linear elasticity. Int. J. Solids Struct. 28, 845–858.

Mühlhaus, H.-B., Aifantis, E.C., 1991. A variational principle for gradient plasticity. Int. J. Solids Struct. 28, 845–858.

Peerlings, R.H.J., Massart, T.J., Geers, M.G.D., 2004. A thermodynamically motivated implicit gradient damage framework and its application to brick masonry cracking. Comput. Methods Appl. Mech. Engrg. 193, 3403–3417.

Polizzotto, C., 2003a. Gradient elasticity and nonstandard boundary conditions. Int. J. Solids Struct. 40, 7399–7423.

Polizzotto, C., 2003b. Unified thermodynamic framework for nonlocal/gradient continuum theories. Eur. J. Mech. A Solids 22, 651–668.

Polizzotto, C., Borino, G., 1998. A thermodynamics-based formulation of gradient-dependent plasticity. Eur. J. Mech. A Solids 17, 741–761.

Polizzotto, C., Fischi, P., Pisano, A.A., 2006. A nonhomogeneous nonlocal elasticity model. Eur. J. Mech. A Solids 25, 308–333.

Shu, J.Y., Fleck, N.A., Van der Giessen, E., Needleman, A., 2001. Boundary layers in constrained plastic flow: comparison of nonlocal and discrete dislocation plasticity. J. Mech. Phys. Solids 49, 1361–1395.

Stumpf, H., Makowski, J., Gorski, J., Hackl, K., 2004. Thermodynamically consistent nonlocal theory of ductile damage. Mech. Res. Commun. 31, 355–363.

Triantafyllidis, N., Aifantis, E.C., 1986. A gradient approach to localization of deformation: Hyperelastic materials. J. Elasticity 16, 225–237.

Voyiadjis, G.Z., Abu Al-Rab, R.K., 2005. Gradient plasticity theory with a variable length scale parameter. Int. J. Solids Struct. 42, 3998–4029.

Wu, C.H., 1992. Cohesive elasticity and surface phenomena. Quart. Appl. Math. L (1), 73–103.

Zbib, H.M., Aifantis, E.C., 1992. On the gradient-dependent theory of plasticity and shear bending. Acta Mech. 92, 209–225.