# A crack-mechanics based model for damage and plasticity of brittle materials under dynamic loading

Q.H. Zuo $^{a,*}$, D. Disilvestro $^{a}$, J.D. Richter $^{a,b}$

$^{a}$ Department of Mechanical and Aerospace Engineering, The University of Alabama in Huntsville, Huntsville, AL 35899, USA
$^{b}$ NASA/Marshall Space Flight Center, MSFC-EV91, Huntsville, AL 35812, USA

---

## A R T I C L E  I N F O

**Article history:**
Received 27 February 2010
Available online 16 June 2010

**Keywords:**
Continuum damage
Crack mechanics
Damage evolution
Brittle materials
Dynamic loading

---

## A B S T R A C T

A rate-dependent model for damage and plastic deformation of brittle materials under dynamic loading is presented. The model improves upon a recently developed micromechanical damage model (Zuo et al., 2006) by incorporating plastic deformation of the material. The distribution of the microcracks in the material is assumed to remain isotropic, and the damage evolution is through the growth of the average crack size. Plasticity is considered through an additive decomposition of the total strain rate, and a rate-independent, von Mises model is used. The model was applied to simulate the response of a model material (SiC) under uniaxial strain loading. To further examine the behavior of the model, cyclic loading and large-strain compressive loading were considered. Numerical results of the model predictions are presented, and comparisons with those from a previous model are provided.

© 2010 Elsevier Ltd. All rights reserved.

---

## 1. Introduction

Many engineering materials (e.g., ceramics, concrete, rocks, and explosives) contain brittle constituents that are subject to microcracking under loading. For example, lightweight ceramics, which have recently been used as armors against high-velocity impact (Wilkins et al., 1967; Addessio and Johnson, 1990; Rajendran and Kroupa, 1989; Rajendran, 1994; Rajendran and Grove, 1996; Meyer et al., 1999; Lundberg et al., 2000; Zuo et al., 2008), are brittle materials with very high compressive strength, but also with low tensile strength (Johnson and Holmquist, 1999; Holmquist et al., 2001; Holmquist and Johnson, 2002). Predictive modeling of the mechanical response of brittle materials under a general (three-dimensional), dynamic loading is of a practical interest to the designer of structures and systems containing brittle materials. Much research has been done in recent years on the fundamental understanding and the development of advanced constitutive models for brittle and quasi-brittle materials (e.g., Ortiz, 1985; Simo and Ju, 1987, 1989; Yazdani and Schreyer, 1988, 1990, 2003; Hansen and Schreyer, 1994, 1995; Dube et al., 1996; Zhang et al., 2003), and on experimentally measuring the material responses under dynamic loading conditions (e.g., Grady and Kipp, 1985, 1989; Kipp and Grady, 1989a,b; Feng et al., 1996, 1998; Vogler et al., 2010).

The response of a brittle material under thermal-mechanical loading is strongly affected by the behavior of microcracks in the material (either present prior to the application of loads or nucleated under low tensile/shear stresses). The microcracks may open, shear, and grow as cracks become unstable when the stress is high enough, and coalesce when the spacing between the cracks becomes small enough, resulting in a rather complex response of the material, which is observed macroscopically (Dienes, 1978, 1985; Dienes et al., 2006; Zuo et al., 2008). Consequently, predictive modeling of a structure or system that contains a brittle material should take into account the behavior of microcracks in the material. A number of micromechanics-based theories and models have been developed recently to predict the behavior of brittle materials under dynamic loading (e.g., Dienes, 1978, 1983, 1985, 1996; Costin, 1983; Taylor et al., 1986; Addessio and Johnson, 1990; Rajendran, 1994; Rajendran and Grove, 1996; Dienes et al., 2006). These models typically assume a distribution of microcracks in the material, prior to the application of the loading, and calculate the damage accumulation via the growth of microcracks under stress. In particular, Dienes has developed the theory of Statistical CRAck Mechanics (SCRAM) for modeling the damage and failure of brittle materials (Dienes et al., 2006; Zuo et al., 2008). The SCRAM theory considers an ensemble of randomly distributed microcracks in the material in the unloaded state, and evaluates the evolution of the probability distribution function (pdf) of the cracks in various orientations as a function of the loading. The damage in the material is obtained by a statistical averaging of the responses of the microcracks of various sizes and orientations. A unique feature of the SCRAM model is the modeling of anisotropic damage of the material by keeping track of the mean crack sizes along a set of pre-determined orientations. Based on the SCRAM work, Addessio and Johnson (1990) proposed a continuum damage model (ISOSCM), in which the distribution of the crack size is assumed to remain isotropic. An important aspect of the ISOSCM model is its

---

* Corresponding author.
E-mail address: zuo@eng.uah.edu (Q.H. Zuo).

0020-7683/$ - see front matter © 2010 Elsevier Ltd. All rights reserved.
doi:10.1016/j.ijsolstr.2010.06.009

numerical efficiency, as the evolution of damage is based on the average crack size over all orientations. Following the ISOSCM work, other models have been proposed for brittle materials to account for additional physical mechanisms that can affect the response of the materials (Bennett et al., 1998; Lee et al., 2004). For example, Bennett et al. proposed a damage model (Visco-SCRAM) for plastically bonded explosives (PBX), which includes the viscous effect of the plastic binder in the explosives (Bennett et al., 1998; Hackett and Bennett, 2000).

Recently, based on the ISOSCM model, Zuo et al. (2006) proposed a rate-dependent damage model, the Dominant Crack Algorithm (DCA), for the damage of brittle materials under dynamic loading. The DCA model improves the ISOSCM model in several aspects. The rate-dependent damage evolution in the DCA model is based on the strain energy release rate associated with the critical crack orientation, which is defined as the most unstable orientation for cracks that isotropically distributed in the material (Zuo and Dienes, 2005). In addition, the DCA model removes a discontinuity in the damage surface in the ISOSCM model, which, under certain limited loading paths, may not be thermodynamically consistent (Lewis and Schreyer, 1996). An extended version of the model (ViscoDCA) has been implemented in engineering analysis codes (e.g., ABAQUS, ALE3D) and is currently used for modeling damage in energetic materials under ballistic impact (Pfau et al., 2009). One important physical mechanism that is not accounted for in the DCA model, however, is the plastic deformation of the material. Neglecting the plastic deformation may be justified for applications in which there is little confinement of the material (e.g., a tensile stress state), and the deformation is thus dominated by the brittle behavior. However, for certain applications, such as problems involving high confinement of quasi-brittle materials (e.g., a uniaxial strain condition as encountered in plate impact experiments), the confining pressure in the material may be enough to produce plastic deformation. Concrete, for example, displays plastic deformation before failure (e.g., Hansen and Schreyer, 1994, 1995). Furthermore, materials such as plastic bonded explosives, for which the DCA model is intended, are known to undergo plastic deformation even under normal application conditions (Dienes et al., 2006). For such applications, as is shown in this paper, neglecting plastic deformation can lead to an over-prediction of the actual stress in the material, which in turn can cause a prediction of excessive crack growth. The main objective of this work is to incorporate plastic deformation into the DCA model. The resulting improved model, for the ease of reference, is called the Plastic-DCA.

The paper proceeds as follows. The theoretical formulation of the Plastic-DCA model is given in Section 2. The numerical algorithm for the model is presented in Section 3. Section 4 shows comparisons between the numerical predictions obtained for a silicon carbide (SiC) model material subjected to both cyclic uniaxial strain loading and large-strain compression, using the DCA and the Plastic-DCA models. The paper ends in Section 5 with a summary and some concluding remarks.

### 1.1. Notation

The following direct tensor notations (e.g., Curtin, 1981) are used in the paper:
$$
\begin{align*}
\mathbf{i} &\equiv \delta_{ij} \mathbf{e}_i \otimes \mathbf{e}_j; & \mathbf{I} &\equiv \frac{1}{2} \left( \delta_{ik}\delta_{jl} + \delta_{il}\delta_{jk} \right) \mathbf{e}_i \otimes \mathbf{e}_j \otimes \mathbf{e}_k \otimes \mathbf{e}_l, \\
\mathbf{u} \otimes \mathbf{v} &\equiv u_i v_j \mathbf{e}_i \otimes \mathbf{e}_j; & \mathbf{A} \otimes \mathbf{B} &\equiv A_{ij} B_{kl} \mathbf{e}_i \otimes \mathbf{e}_j \otimes \mathbf{e}_k \otimes \mathbf{e}_l, \\
\mathbf{u} \cdot \mathbf{v} &\equiv u_k v_k; & \mathbf{A}\mathbf{u} &\equiv A_{ik} u_k \mathbf{e}_i; & \mathbf{A}\mathbf{B} &\equiv A_{ik} B_{kj} \mathbf{e}_i \otimes \mathbf{e}_j \\
\mathbf{T}\boldsymbol{\varepsilon} &\equiv T_{ijkl} \varepsilon_{kl} \mathbf{e}_i \otimes \mathbf{e}_j; & \mathbf{C}\mathbf{D} &\equiv C_{ijkl} D_{klmn} \mathbf{e}_i \otimes \mathbf{e}_j \otimes \mathbf{e}_m \otimes \mathbf{e}_n, \\
tr\mathbf{A} &\equiv \mathbf{i} : \mathbf{A} = A_{ii}; & \mathbf{A} : \mathbf{B} &\equiv A_{ik} B_{ki},
\end{align*}
$$
where $\mathbf{i}$ is the second-order identity tensor; $\mathbf{I}$, the fourth-order (symmetric) identity tensor; $\delta_{ij}$, the Kronecker delta; $\{\mathbf{e}_i\}$ ($i=1,2,3$), an arbitrary orthonormal basis; "$\otimes$", the tensor product; $\mathbf{u}$, $\mathbf{v}$, vectors; $\mathbf{A}$, $\mathbf{B}$, $\boldsymbol{\varepsilon}$, symmetric, second-order tensors; $\mathbf{T}$, $\mathbf{C}$, $\mathbf{D}$, fourth-order tensors; ":", the scalar product of second-order tensors; and $tr$, the trace of a second-order tensor.

## 2. Model formulation

We consider the mechanical response of a quasi-brittle material under a general, three-dimensional stress state. The material is assumed to contain a large number of penny-shaped cracks with different sizes and orientations. As in previous work (Addressio and Johnson, 1990; Zuo et al., 2006), the size distribution of the cracks is assumed to remain isotropic (i.e., independent of the crack orientation) and exponential during loading. Under such assumptions, the probability density function (pdf) of the crack numbers can be written as (Addressio and Johnson, 1990)
$$
n(c,t) = \frac{N_o}{\bar{c}(t)} \exp(-c/\bar{c}(t)), \tag{1}
$$
where $\bar{c}(t)$ is the mean crack radius, and $N_o$ is the initial crack number density per solid angle. In the current model, $N_o$ is kept as a material constant, and the damage in the material is reflected through the evolution of $\bar{c}(t)$.

In the DCA model, the total strain rate $\dot{\boldsymbol{\varepsilon}}$ is decomposed into the contributions from the matrix (uncracked solid) and from the response (open, shear, and growth) of microcracks. Here, to include plastic deformation, the decomposition is modified as (Dienes et al., 2006)
$$
\dot{\boldsymbol{\varepsilon}} = \dot{\boldsymbol{\varepsilon}}_m + \dot{\boldsymbol{\varepsilon}}_c^d + \dot{\boldsymbol{\varepsilon}}_c^{gr} + \dot{\boldsymbol{\varepsilon}}^p, \tag{2}
$$
where the strain rates related to the matrix, the opening and shear of cracks (with the current sizes), and the growth of cracks are given by, respectively,
$$
\begin{align*}
\dot{\boldsymbol{\varepsilon}}_m &= \mathbf{C}_m \dot{\boldsymbol{\sigma}}, \\
\dot{\boldsymbol{\varepsilon}}_c^d &= \mathbf{D}(\bar{c}) \dot{\boldsymbol{\sigma}}, \\
\dot{\boldsymbol{\varepsilon}}_c^{gr} &= \frac{\partial \mathbf{D}(\bar{c})}{\partial \bar{c}} \dot{\bar{c}} \boldsymbol{\sigma},
\end{align*} \tag{3}
$$
where $\mathbf{C}_m$ is the compliance tensor of the matrix, $\mathbf{D}(\bar{c})$ is the damage tensor, and $\dot{\boldsymbol{\varepsilon}}^p$ is the plastic strain rate, which is to be defined later. The plastic deformation considered in the current work refers to deformation that cannot be recovered upon removal of the stress on the material. For a crystalline solid, the physical (micromechanical) origin of such deformation is the movement of dislocations (slip) on the slip planes in the material. Deformation mechanisms such as mechanical twinning and phase transformation are not considered.

If the matrix is modeled by linear isotropic elasticity, then the compliance tensor $\mathbf{C}_m$ of the matrix can be written as
$$
\mathbf{C}_m = \frac{1}{3K} \mathbf{P}^{sp} + \frac{1}{2G} \mathbf{P}^d, \tag{4}
$$
where $K$ and $G$ are, respectively, the bulk and shear moduli of the matrix, which are constants for the model. The spherical and deviatoric projection operators are (e.g., Hansen and Schreyer, 1994)
$$
\mathbf{P}^{sp} \equiv \frac{1}{3} (\mathbf{i} \otimes \mathbf{i}); \quad \mathbf{P}^d \equiv \mathbf{I} - \mathbf{P}^{sp}
$$
with $\mathbf{i}$ and $\mathbf{I}$ denoting, respectively, the 2nd- and (symmetric) 4th-order identity tensors defined in Notation.

The damage tensor developed in the DCA model is used in the current work,

$$
\mathbf{D}(\bar{c})=\beta^{e} N_{o} \bar{c}^{3}\left(\frac{3}{2-v} \mathbf{P}^{d}+\mathbf{P}^{+}\left(\mathbf{P}^{d}+\frac{5}{2} \mathbf{P}^{s p}\right) \mathbf{P}^{+}\right),
\tag{5}
$$

where $v$ is the Poisson's ratio of the matrix, and $\beta^{e} \equiv 64 \pi(1-v) /$ (15G) is a material constant depending on the elastic properties of the matrix. The quantity $N_{o} \bar{c}^{3}$ can be thought as a dimensionless scalar representation of the material damage. In Eq. (5), $\mathbf{P}^{+}$is the positive projection operator (a 4th-order tensor), defined by the stress state: $\mathbf{P}^{+}=\mathbf{I}$ if the stress state is tensile (all three principal stresses are positive); $\mathbf{P}^{+}=\mathbf{0}$ if it is compressive (the principal stresses are all negative). When the principle stresses are of mixed signs, $\mathbf{P}^{+}$ eliminates the contributions of the compressive principal stresses to the crack opening strain, making the formulation consistent with crack-mechanics (Yazdani and Schreyer, 1988, 1990, 2003; Wen and Yazdani, 2008). The details of the definition for $\mathbf{P}^{+}$are described by Zuo et al. (2006).

In Eq. (3c), $\dot{\bar{c}}$ is the crack growth rate given by (Zuo et al., 2006)

$$
\frac{\dot{\bar{c}}}{\dot{\bar{c}}_{\max }}=1-\frac{1}{1+\langle F(\boldsymbol{\sigma}, \bar{c})\rangle},
\tag{6}
$$

where $F(\boldsymbol{\sigma}, \bar{c})$ is the damage function based on the stability of the cracks along the critical orientation. The damage surface $F(\boldsymbol{\sigma}, \bar{c})=0$ divides the stress space into two regions: the elastic region corresponding to $F(\boldsymbol{\sigma}, \bar{c})<0$ in which $\dot{\bar{c}}=0$, and the damage accumulation region for $F(\boldsymbol{\sigma}, \bar{c})>0$ in which $\dot{\bar{c}}>0$. The angled bracket is the Macaulay bracket, which takes the value of the argument when positive and is zero otherwise. The expression for $F(\boldsymbol{\sigma}, \bar{c})$ is given in Zuo et al. (2006). The maximum growth rate $\dot{\bar{c}}_{\max }$ is the terminal speed for crack growth (e.g., Freund, 1990) and is either the shear wave speed of the matrix for closed cracks, or the Rayleigh wave speed $C_{R}$ for open cracks, which is only slightly less than the shear wave speed. The choice depends on whether the crack with the critical orientation is open or closed.

For simplicity, the von Mises theory with associated flow rule is used here to model the plastic response of the material. In the von Mises theory, the yield surface is given by (e.g., Lubliner, 1990; Simo and Hughes, 1998)

$$
f(\boldsymbol{\sigma})=\bar{\sigma}-\sigma_{y}=0,
\tag{7}
$$

where $\bar{\sigma} \equiv \sqrt{3\left(\boldsymbol{\sigma}^{d}: \boldsymbol{\sigma}^{d}\right) / 2}$, with $\boldsymbol{\sigma}^{d}$ being the stress deviator, is the equivalent (von Mises) stress, and $\sigma_{y}$ is the yield stress of the material, which in general is a function of the plastic strain, strain rate, and temperature. Also for simplicity, here the yield stress $\sigma_{y}$ is assumed to remain constant (i.e. perfect plasticity). Following an associated flow rule, the plastic strain rate is given by (e.g., Lubliner, 1990; Simo and Hughes, 1998)

$$
\dot{\boldsymbol{\varepsilon}}^{p}=\dot{\lambda} \frac{\partial f(\boldsymbol{\sigma})}{\partial \boldsymbol{\sigma}}=\dot{\lambda} \mathbf{N}=\dot{\lambda} \frac{3}{2} \frac{\boldsymbol{\sigma}^{d}}{\bar{\sigma}},
\tag{8}
$$

where $\mathbf{N}$ denotes the normal to the yield surface. The substitution of Eqs. (3) and (8) into Eq. (2) yields

$$
\left(\mathbf{C}_{m}+\mathbf{D}(\bar{c})\right) \dot{\boldsymbol{\sigma}}+\dot{\bar{c}} \frac{\partial \mathbf{D}(\bar{c})}{\partial \bar{c}} \boldsymbol{\sigma}+\dot{\lambda} \frac{3}{2} \frac{\boldsymbol{\sigma}^{d}}{\bar{\sigma}}=\dot{\boldsymbol{\varepsilon}}.
\tag{9}
$$

For a prescribed total strain rate $\dot{\varepsilon}$, with the damage tensor defined in Eq. (5), (9) is a tensorial equation for the stress rate $\dot{\boldsymbol{\sigma}}$, the crack growth rate $\dot{\bar{c}}$, and the plastic parameter $\dot{\lambda}$. When supplemented by the consistency equation, $\dot{f}(\boldsymbol{\sigma})=0$, where $f(\boldsymbol{\sigma})=0$ is the yield surface given by Eq. (7), and by Eq. (6) for the crack growth, Eq. (9) can be solved for $\dot{\boldsymbol{\sigma}}, \dot{\bar{c}}$, and $\dot{\lambda}$. In practice, however, solving such coupled, nonlinear equations poses a serious technical challenge. As an approximation, we have developed an alternative, simpler algorithm.

## 3. Numerical algorithm

Consider a typical time step $\Delta t \equiv t^{n+1}-t^{n}$, where $t^{n}$ and $t^{n+1}$ are, respectively, the times at the beginning and at the end of the step. The computational algorithm for the step $\Delta t$ is summarized in the following. Suppose that the material state (i.e., stress, mean crack size, and plastic strain) is known at the beginning of the step. The total strain rate $\dot{\varepsilon}_{n+1}$ for the step is prescribed, and the objective here is to update the stress, mean crack size, and plastic strain.

The integration of Eq. (2) over the time step gives the incremental form

$$
\Delta \boldsymbol{\varepsilon}=\left(\Delta \boldsymbol{\varepsilon}_{m}+\Delta \boldsymbol{\varepsilon}_{c}^{d}+\Delta \boldsymbol{\varepsilon}_{c}^{g r}\right)+\Delta \boldsymbol{\varepsilon}^{p},
\tag{10}
$$

where $\Delta \boldsymbol{\varepsilon}=\dot{\boldsymbol{\varepsilon}}_{n+1} \Delta t$, and so on. For convenience, we define

$$
\Delta \boldsymbol{\varepsilon}^{\mathrm{DCA}} \equiv \Delta \boldsymbol{\varepsilon}_{m}+\Delta \boldsymbol{\varepsilon}_{c}^{d}+\Delta \boldsymbol{\varepsilon}_{c}^{g r}=\Delta \boldsymbol{\varepsilon}-\Delta \boldsymbol{\varepsilon}^{p}.
\tag{11}
$$

Then, it follows from Eqs. (2) and (3) that

$$
\left(\mathbf{C}_{m}+\mathbf{D}(\bar{c})\right) \dot{\boldsymbol{\sigma}}=\dot{\boldsymbol{\varepsilon}}-\dot{\boldsymbol{\varepsilon}}^{p}-\dot{\boldsymbol{\varepsilon}}_{c}^{g r}.
\tag{12}
$$

Integrating Eq. (12) over the time step gives

$$
\boldsymbol{\sigma}^{n+1}=\boldsymbol{\sigma}^{n}+\left(\mathbf{C}_{m}+\mathbf{D}\left(\bar{c}^{n}\right)\right)^{-1}\left(\Delta \boldsymbol{\varepsilon}-\Delta \boldsymbol{\varepsilon}^{p}-\Delta \boldsymbol{\varepsilon}_{c}^{g r}\right).
\tag{13}
$$

As an approximation, we assume here that over a small time step the damage (crack growth) and plasticity calculations can be done separately. That is, in each step, the crack growth $\Delta \bar{c}$ and the strain increment due to crack growth $\Delta \boldsymbol{\varepsilon}_{c}^{g r}=\Delta \bar{c}(\partial \mathbf{D}(\bar{c}) / \partial \bar{c}) \boldsymbol{\sigma}$ are first calculated assuming the step does not involve plasticity. The stress at the end of this sub-step calculation can then be used to calculate the plastic strain for the step, which in turn is used to update (correct) the stress predicted by the first sub-step calculation.

Let us define the stress found by assuming that the step does not involve plasticity as the trial stress for the second sub-step, which involves plasticity only:

$$
\boldsymbol{\sigma}^{t r} \equiv \boldsymbol{\sigma}^{n}+\left(\mathbf{C}_{m}+\mathbf{D}\left(\bar{c}^{n}\right)\right)^{-1}\left(\Delta \boldsymbol{\varepsilon}-\Delta \boldsymbol{\varepsilon}_{c}^{g r}\right).
\tag{14}
$$

Then, it follows from Eqs. (13) and (14) that

$$
\boldsymbol{\sigma}^{n+1}=\boldsymbol{\sigma}^{t r}-\mathbf{E}^{n} \Delta \boldsymbol{\varepsilon}^{p},
\tag{15}
$$

where, for convenience, $\mathbf{E}^{n} \equiv\left(\mathbf{C}_{m}+\mathbf{D}\left(\bar{c}^{n}\right)\right)^{-1}$ was introduced to represent the (4th-order) elasticity tensor of the material at the beginning of the step. An implicit integration (e.g., Simo and Hughes, 1998) of Eq. (8) over the step gives

$$
\Delta \boldsymbol{\varepsilon}^{p}=\Delta \lambda \mathbf{N}^{n+1}=\Delta \lambda \frac{3}{2}\left(\frac{\boldsymbol{\sigma}^{d}}{\bar{\sigma}}\right)^{n+1}.
\tag{16}
$$

Substitution of Eq. (16) into Eq. (15) gives

$$
\boldsymbol{\sigma}^{n+1}+\mathbf{E}^{n} \Delta \lambda \frac{3}{2}\left(\frac{\boldsymbol{\sigma}^{d}}{\bar{\sigma}}\right)^{n+1}=\boldsymbol{\sigma}^{t r}.
\tag{17}
$$

Since the distribution of the cracks is assumed to remain isotropic during loading, it is reasonable to assume that the elasticity tensor of the material also remains isotropic. Let

$$
\mathbf{E}^{n}=3 K^{n} \mathbf{P}^{s p}+2 \mu^{n} \mathbf{P}^{d},
\tag{18}
$$

where $K^{n}$ and $\mu^{n}$ are the current (damaged) bulk and shear moduli of the material at the beginning of the step. It follows from Eqs. (17) and (18) that

$$
\left(1+\frac{3 \mu^{n} \Delta \lambda}{\bar{\sigma}^{n+1}}\right)\left(\boldsymbol{\sigma}^{n+1}\right)^{d}=\left(\boldsymbol{\sigma}^{t r}\right)^{d},
\tag{19a}
$$

$$
p^{n+1}=p^{t r},
\tag{19b}
$$

where $\left(\boldsymbol{\sigma}^{n+1}\right)^{d}$ and $p^{n+1}$ are respectively the stress deviator and the pressure at the end of the step, and $\left(\boldsymbol{\sigma}^{t r}\right)^{d}$ and $p^{t r}$ are the corresponding values for the trial stress:

$$
p^{tr}=-\frac{1}{3}tr(\boldsymbol{\sigma}^{tr}),
\tag{20a}
$$

$$
(\boldsymbol{\sigma}^{tr})^{d}=\boldsymbol{\sigma}^{tr}+p^{tr}\mathbf{i}.
\tag{20b}
$$

It follows from Eq. (19a) that

$$
(\boldsymbol{\sigma}^{n+1})^{d}=\frac{(\boldsymbol{\sigma}^{tr})^{d}}{\left(1+\frac{3\mu^{n}\Delta\lambda}{\bar{\sigma}^{n+1}}\right)},
\tag{21a}
$$

$$
\left(\frac{\boldsymbol{\sigma}^{d}}{\bar{\sigma}}\right)^{n+1}=\frac{(\boldsymbol{\sigma}^{n+1})^{d}}{\bar{\sigma}^{n+1}}=\frac{\boldsymbol{\sigma}^{tr}}{\bar{\sigma}^{tr}},
\tag{21b}
$$

where $\bar{\sigma}^{tr}\equiv(3/2(\boldsymbol{\sigma}^{tr}:\boldsymbol{\sigma}^{tr}))^{1/2}$ is the trial von Mises stress. It is implied by Eq. (21a) that the direction of the stress deviator at the end of the step is the same as that at the trial state, which is available once the trial state is found, and that the normal to the yield surface can be calculated solely based on the trial state. It follows from Eq. (21a) that

$$
\bar{\sigma}^{n+1}=\left(\frac{3}{2}(\boldsymbol{\sigma}^{n+1})^{d}:(\boldsymbol{\sigma}^{n+1})^{d}\right)^{1/2}=\frac{\bar{\sigma}^{tr}}{\left(1+\frac{3\mu^{n}\Delta\lambda}{\bar{\sigma}^{n+1}}\right)}.
\tag{22}
$$

Or,

$$
\bar{\sigma}^{n+1}=\bar{\sigma}^{tr}-3\mu^{n}\Delta\lambda.
\tag{23}
$$

That is, the plastic parameter $\Delta\lambda$ is proportional to the distance from the trial state to the final state.

In an implicit algorithm, the final stress state (at the end of the step) is required to be on the yield surface

$$
f(\boldsymbol{\sigma}^{n+1})=\bar{\sigma}^{n+1}-\sigma_{y}=0.
\tag{24}
$$

The substitution of Eq. (23) to (24) solves for the plastic parameter $\Delta\lambda$:

$$
\Delta\lambda=\frac{\bar{\sigma}^{tr}-\sigma_{y}}{3\mu^{n}}=\frac{f^{tr}}{3\mu^{n}}.
\tag{25}
$$

The above formulations can be summarized in the following steps:

1. Assume the step does not involve plastic deformation. The state is defined as the trial state. Since $(\Delta\boldsymbol{\varepsilon}^{p})^{tr}=0$,
$$
(\Delta\boldsymbol{\varepsilon}^{DCA})^{tr}=\Delta\boldsymbol{\varepsilon}-(\Delta\boldsymbol{\varepsilon}^{p})^{tr}=\Delta\boldsymbol{\varepsilon}.
\tag{26}
$$

2. Call the DCA routines to calculate the stress and mean crack size at the end of the step using $(\Delta\boldsymbol{\varepsilon}^{DCA})^{tr}$. The numerical algorithm for this part of the calculation is implicit and is described in detail previously (Zuo et al., 2006). The stress so calculated is defined as the trial stress for the step, $\boldsymbol{\sigma}^{tr}$.

3. Check if the trial state lies outside the yield surface $f(\boldsymbol{\sigma})=\bar{\sigma}-\sigma_{y}=0$. If $f^{tr}\equiv\bar{\sigma}^{tr}-\sigma_{y}\leqslant0$, then the current step indeed does not involve plastic deformation and the calculation for the step is complete.
On the other hand, if $f^{tr}>0$, then the step involves plasticity and corrections to the stress must be made. Go to step 4.

4. Solve for the plastic parameter $\Delta\lambda$ using Eq. (25). The plastic strain increment for the time increment is then
$$
\Delta\boldsymbol{\varepsilon}^{p}=\Delta\lambda\frac{3}{2}\left(\frac{\boldsymbol{\sigma}^{d}}{\bar{\sigma}}\right)^{n+1}=\Delta\lambda\frac{3}{2}\frac{(\boldsymbol{\sigma}^{tr})^{d}}{\bar{\sigma}^{tr}}.
\tag{27}
$$

It follows from Eq. (21b) that

$$
(\boldsymbol{\sigma}^{n+1})^{d}=\frac{(\boldsymbol{\sigma}^{tr})^{d}}{\bar{\sigma}^{tr}}\bar{\sigma}^{n+1}=\frac{\sigma_{y}}{\bar{\sigma}^{tr}}(\boldsymbol{\sigma}^{tr})^{d}.
\tag{28}
$$

That is, in the deviatoric plane, the final stress can be found be returning the trial stress back onto the yield surface along a radial direction (the direction of the trial stress). With the pressure and the deviatoric parts known, the final stress is

$$
\boldsymbol{\sigma}^{n+1}=(\boldsymbol{\sigma}^{n+1})^{d}-p^{n+1}\mathbf{i}=\frac{\sigma_{y}}{\bar{\sigma}^{tr}}(\boldsymbol{\sigma}^{tr})^{d}-p^{tr}\mathbf{i}.
\tag{29}
$$

Now, the stress has been corrected and the plastic strain calculated, hence the calculation for the step is complete.

A computer subroutine was written to numerically implement the procedure discussed above. The subroutine was combined with the original subroutines developed by Zuo et al. for the DCA model to form a complete set of subroutines, which can now be applied to model both the damage and plastic deformation of a brittle material under general, three-dimensional state of stress. The numerical results are presented next.

## 4. Results and discussion

To illustrate the main features of the model, a driver program was written that provides the strain increments to the material subroutines for updating the stress, mean crack size, and plastic strain in the material. The model material is the silicon carbide studied previously using the DCA model (Zuo et al., 2006). The average grain size of the material is $7\,\mu\text{m}$ (Kipp and Grady, 1989b). The model constants are based on those of Addessio and Johnson (1990) and of Grady (1994); and, for convenience, they are listed in Table 1. Compared to the constants used in the DCA model, the only additional constant in the new model is the yield stress of the material, $\sigma_{y}=0.125$ Mbar. For the ease of comparisons of the results given by the two models, the stress unit previously used in the DCA model, Mbar (100 GPa), is also used here.

The computed responses of the model material to high-rate $(1.0\times10^{5}\,\text{s}^{-1})$, uniaxial strain loadings (cyclic and large-strain compression) are shown next to illustrate the main features of the current model. Uniaxial strain loading was chosen because it simulates the state of stress of the materials in the early stages of high-velocity plate-impact calculations.

### 4.1. Cyclic loading: verification problem

The first example is a cyclic (tension-compression-tension) loading and the results are shown in Fig. 1. The material is subjected initially to a positive (tensile) strain rate until a tensile strain of $\varepsilon_{11}=1.0\times10^{-2}$ is reached (point C in Fig. 1). Then it is unloaded until a strain of $\varepsilon_{11}=-5.0\times10^{-4}$ (point D) is reached and reloaded again to a strain of $\varepsilon_{11}=2\times10^{-2}$ (point E). As is seen in Fig. 1, the response predicted by Plastic-DCA for this loading case is identical to that by DCA. This is expected, since, due to the large amount of damage caused by tension, the stress state remains inside the yield surface (compare the peak stress $\sigma_{11}\approx9.3\times10^{-3}$ Mbar at point B with the yield stress of $\sigma_{y}=0.125$ Mbar) during the loading history. A discussion of the various features of a response dominated by tensile crack growth shown in Fig. 1 is given later in connection with Figs. 6-8. This example serves as a verification of the formu-

<table>
<caption>Table 1 Material constants for SiC based on Addessio and Johnson (1990) and Grady (1994).</caption>
<thead>
<tr>
<th>Constant</th>
<th>Definition</th>
<th>Value</th>
<th>Unit</th>
</tr>
</thead>
<tbody>
<tr>
<td>$\rho$</td>
<td>Density</td>
<td>3.177</td>
<td>g/cm³</td>
</tr>
<tr>
<td>$G$</td>
<td>Shear modulus</td>
<td>1.869</td>
<td>Mbar</td>
</tr>
<tr>
<td>$\nu$</td>
<td>Poisson's ratio</td>
<td>0.16</td>
<td></td>
</tr>
<tr>
<td>$N_{0}$</td>
<td>Crack number density</td>
<td>$1.0\times10^{5}$</td>
<td>cm⁻³</td>
</tr>
<tr>
<td>$\bar{c}_{0}$</td>
<td>Initial crack size</td>
<td>$14.0\times10^{-4}$</td>
<td>cm</td>
</tr>
<tr>
<td>$\gamma$</td>
<td>Surface energy</td>
<td>$1.0\times10^{-8}$</td>
<td>Mbar cm</td>
</tr>
<tr>
<td>$\mu$</td>
<td>Friction coefficient</td>
<td>0.26</td>
<td></td>
</tr>
<tr>
<td>$\sigma_{y}$</td>
<td>Yield stress</td>
<td>0.125</td>
<td>Mbar</td>
</tr>
</tbody>
</table>

![](./images/811780225498087424_1.jpg)

Fig. 1. Comparison of cyclic responses predicted by the DCA model and Plastic-DCA models: verification problem.

lation and numerical algorithm of the current model for the stress states in which plastic deformation is absent.

### 4.2. Compressive loading

Next consider the computed response to large compressive strains (up to 20%). The response given by the current model (Plastic-DCA) is shown in Fig. 2 for the stresses (both the axial and longitudinal), and in Fig. 3 for the evolution of the mean crack size (damage). The results predicted by DCA are overlaid for comparison. In the figures, the legend "DCA" (also in blue) refers to the results of the DCA model, whereas "Plastic-DCA" (in green) refers to those of the Plastic-DCA model. It is seen that the two models give identical results up to the point P, when the stress state first reaches the yield surface. Following the initial yielding, the stresses calculated by the two models show an increasing difference: the stress state by Plastic-DCA remains on the yield surface ($\sigma_{11}-\sigma_{22}=-\sigma_{y}$) as deformation proceeds, whereas the stress state by DCA would be above the yield surface. Fig. 3 shows that including plastic deformation has a very modest effect on the crack growth for uniaxial (strain) compression: at $\varepsilon_{11}=-0.2$, the mean crack size has grown to $\bar{c}\approx5.9\bar{c}_{0}$ with the consideration of plastic deformation, compared to $\bar{c}\approx6.0\bar{c}_{0}$ given by the DCA model.

![](./images/811780225498087424_2.jpg)

Fig. 2. Comparison of responses to large compressive strain predicted by the DCA model and Plastic-DCA models.

![](./images/811780225498087424_3.jpg)

Fig. 3. Comparison of the evolutions of the mean crack size under large compressive strain.

The temporary strain-softening (reduction in stress) shown in Fig. 2 is caused by a fast crack growth (around point B) immediately following the initiation of the crack growth, corresponding to point $A^{*}$ in Fig. 3. Under uniaxial compressive strain, which induces a triaxial stress state ($\sigma_{11}<\sigma_{22}=\sigma_{33}<0$, where $\sigma_{22}=\sigma_{33}$ are the lateral stresses), cracks can become unstable due to the shear stress in the material, grow for a range of the applied strain, and then be stabilized by the friction from large pressures acting on the crack faces (Zuo and Dienes, 2005). As the crack growth in the material slows down, the response is essentially linear elastic with a damaged modulus (hence the lower slope for path B-P than for A-B, as shown in Fig. 2), until the stress state reaches the yield surface at point P. To further demonstrate these points, magnified views of Figs. 2 and 3 are shown in Figs. 4 and 5, respectively. It is seen that the cracks are initially stable when the stresses are low, become unstable at $A^{*}$, experience a fast growth (around B), and eventually slow down as the pressure in the material becomes large enough. This complex behavior of crack growth seems to be

![](./images/811780225498087424_4.jpg)

Fig. 4. Details of the stress response for strain up to $\varepsilon_{11}=-0.02$ showing regions of initially linear elastic, hardening, softening due to fast crack growth, and hardening again as the crack growth slows down.

![](./images/811780225498087424_5.jpg)

Fig. 5. Details of crack growth for strain up to $\varepsilon_{11}=-0.02$ showing that the cracks are initially stable, become unstable at A*, experience fast growth, and slow down as the compressive strain becomes large enough.

consistent with the hardening-softening-hardening response observed in Fig. 2.

### 4.3. Tensile behavior of a fictitious (quasi-brittle) material with lowered $\sigma_y$

As is shown in Fig. 1 and discussed earlier, for the SiC studied by Addessio and Johnson (1990) and Grady (1994), no plastic deformation is predicted under tensile loading and the response is completely controlled by crack growth under a tensile stress state. Absence of plasticity is due to the fact that the SiC considered has a high yield strength ($\sigma_y=0.125$ Mbar) and hence a low ductility, especially under a tensile stress state. Experimental data shows that certain quasi-brittle materials, such as concrete, can have some plastic deformation, even under tensile loading. To demonstrate the features of the current model when both damage and plastic deformation are present under tensile loading, we artificially lower the yield stress to $\sigma_y=0.0035$ Mbar (3.5 kbar) and keep all the other material constants unchanged.

The loading is the same as that considered in Fig. 1. Comparisons of the stress-strain responses, evolutions of the damage (in terms of the mean crack size), and the paths traversed by the stress state (pressure and shear) in the material, are shown respectively in Figs. 6-8. Fig. 9 shows the evolutions of the plastic strains with the applied (total) strain predicted by the current model.

The material is initially at the state of free stress and free strain (point A in all the plots) and is then subjected to cyclic strain rates with a constant magnitude. The results obtained using the previous model (DCA), which have been discussed by Zuo et al. (2006), will be summarized first, followed by those obtained using the current model (Plastic-DCA).

#### 4.3.1. DCA results (based on Zuo et al., 2006)

It is seen from Figs. 6-8 that during the loading part of the path (A-B-C) the material behaves first elastically (A-A*), with a slightly damaged modulus corresponding to an initial crack size of $\bar{c}_0=14$ $\mu$m. Crack growth is initiated at point A* ($\varepsilon_{11}\approx1.6\times10^{-3}$, $\sigma_{11}\approx7.1\times10^{-3}$ Mbar), when the stress state reaches the initial damage surface with $\bar{c}_0$. Immediately following point A*, the strain rate due to crack growth, $\dot{\varepsilon}^{gr}$, is still too low to cause a significant effect in the response. As a result, the stress keeps increasing until it reaches its maximum value at point B [$σ_{11}≈9.30×10^{-3}$ Mbar and $ε_{11}≈2.3×10^{-3}$].

![](./images/811780225498087424_6.jpg)

Fig. 6. Comparison of cyclic responses predicted by the DCA model and Plastic-DCA models with a lowered yield stress ($\sigma_y=3.5$ kbar).

![](./images/811780225498087424_7.jpg)

Fig. 7. Comparison of the evolutions of the mean crack size under uniaxial strain for $\sigma_y=3.5$ kbar.

![](./images/811780225498087424_8.jpg)

Fig. 8. Comparison of the evolutions of the stress state (pressure and von Mises stress) for $\sigma_y=3.5$ kbar.

![](./images/811780225498087424_9.jpg)

Fig. 9. The plastic strains as functions of the applied strain predicted by the current model for $\sigma_{y}=3.5$ kbar.

Following point B, the strain rate due to crack growth over-comes the total prescribed strain rate; consequently, the stress starts to decrease while the strain keeps on increasing ($\dot{\varepsilon}_{11}=1.0\times 10^{5}/s$), and the material strain-softens (from B to C). At point C the material starts to unload and the cracks continue to grow for a short period (crack inertia effects) until the stress meets with the damage surface at $C^{*}$, which is slightly below point C in Fig. 6 (the blue line). From point $C^{*}$ the material behaves elastically until it reaches the origin (A), where the inelastic strain due to crack growth is zero as all the cracks are now closed. As can be observed in the figure, the material stiffness along the path A–D is constant and is less than the initial stiffness (corresponding to $\bar{c}_{0}$), but significantly higher than that for the path A–C. This is because the material is now under uniaxial (strain) compression, which causes the cracks to remain closed. As a result, the damage due to crack opening is deactivated and only the damage from the crack shearing (sliding of crack faces) is active [the first term in Eq. (5) for the damage tensor].

The material is then reloaded. From D to A, the cracks remain closed and the response is identical to that for the path A–D. Be-yond point A, the reloading path follows the same previous path up to point $C^{*}$, because the cracks are now in tension and start to open again, thus, the damage accumulated at $C^{*}$ is reactivated. The importance of capturing this kind of nonlinear material behav-ior, where the path taken by the material (or the stiffness) depends on both the accumulated damage in the material and the current state of stress, has been discussed by Hansen and Schreyer (1994, 1995) in their work on damage deactivation. At point $C^{*}$ the material reaches the damage surface again, and the crack size begins to grow all the way to point E, where the final strain of $\varepsilon_{11}=2\times 10^{-2}$ is reached.

The evolution of the stress state $(p,\bar{\sigma})$ in the material is shown in Fig. 8. As the material is strained in tension, the von Mises stress $\bar{\sigma}$ increases while the pressure decreases, until the stress state reaches the damage surface at $A^{*}$, where the mean crack size starts to grow. The cracks keep growing until the stress state falls inside the damage surface at $C^{*}$, which is indistinguishable from point C in Fig. 8. Upon further unloading, the stress state $(p,\bar{\sigma})$ returns to the origin A (stress free), where the material is loaded in compression with both $p$ and $\bar{\sigma}$ increasing linearly. During the reloading ($\dot{\varepsilon}_{11}>0$), the material follows the same path as the unloading path, D–A–$C^{*}$, until point $C^{*}$ is reached, where cracks start to grow again and the material further softens from $C^{*}$ to E.

### 4.3.2. Plastic-DCA results
The numerical results predicted by the current model have some features similar to those of the DCA model, but they also con-tain some significant differences due to the consideration of plastic deformation. Starting also at a stress free state (point A), the re-sponse is the same as in the previous model for the first part of the loading where the material behaves elastically without crack growth or plasticity. Then, at $\varepsilon_{11}\approx 0.96\times 10^{-3}$ ($\sigma_{11}=4.3\times 10^{-3}$ Mbar), corresponding to point $A''$ in the figures, the stress state reaches the yield surface with $\bar{\sigma}=\sigma_{y}=3.5\times 10^{-3}$ Mbar, and the material starts to deform plastically. Upon plastic yielding, as is shown in Fig. 8, the von Mises (or equivalent) stress in the material is limited by the yield stress $\sigma_{y}$, which is constant for the perfect plasticity model considered here; but due to the effects of lateral confinement provided by the uniaxial strain condition, the mean stress (negative pressure) keeps on increasing with the applied strain. As a result, the stress component $\sigma_{11}$ continues to increase, giving an apparent “hardening” response, as seen in Fig. 6. The initial damage surface corresponding to the mean crack size $\bar{c}_{0}$ is reached when $\sigma_{11}$ obtains a critical value ($\sigma_{11}\approx 7.1\times 10^{-3}$ Mbar) at point $B^{*}$ in Figs. 6–8. It is seen in Figs. 6 and 7 that both models predict the same critical value of $\sigma_{11}$ for the initiation of the crack growth (corresponding to $A^{*}$ and $B^{*}$, respectively), while in the Plastic-DCA model the strain at which crack growth initiates is delayed by the plastic deformation. Beyond the point $B^{*}$, both crack growth and plastic deformation take place simultaneously for a given strain increment $\Delta\varepsilon_{11}$ in the material, and eventually these inelastic strain increments overcome the total strain increment, resulting in a strain-softening response. Com-pared with the DCA model results, the current model predicts a lower peak stress ($\sim$12%) that the material can reach ($8.22\times 10^{-3}$ Mbar vs. $930\times 10^{-3}$ Mbar) and a larger value of strain ($\sim$35%) corresponding to the peak stress ($3.1\times 10^{-3}$ vs. $2.3\times 10^{-3}$). From point $B'$ the stress starts deceasing while the strain is still increasing, and the material strain-softens, as predicted by the DCA model.

The plastic deformation continues as the material is further strained and the stress–strain response of the material follows the path $B'$–$B''$ until point $B''$, corresponding to $\varepsilon_{11}\approx 3.9\times 10^{-3}$, $\varepsilon_{11}^{p}\approx 1.6\times 10^{-3}$ (see Fig. 9), is reached, where there has been enough reduction in the stress due to softening so that the stress state is now inside the yield surface, as shown in Fig. 8. Conse-quently, the plastic strain rate in the material reduces to zero fol-lowing point $B''$, as shown in Fig. 9; and the material response, as controlled by damage, is qualitatively similar to that predicted by DCA, as shown in Figs. 6–8. It is noted that though the stress component $\sigma_{11}$ varies significantly between path $A''$– $B^{*}$–$B'$–$B''$, the stress state remains on the yield surface (i.e., $\bar{\sigma}=\sigma_{y}$), as shown in Fig. 8.

Unloading for the Plastic-DCA model begins at point $C'$ ($\varepsilon_{11}=1.0\times 10^{-2}$). As in DCA, even though the prescribed strain rate becomes negative at point $C'$, crack growth does not terminate until the damage surface is reached at point $C''$ (slightly different from $C'$), causing a small increase in the crack size between points C and $C''$, as shown in Fig. 7. Physically, this is due to the inertial effects of crack growth, as explained in Zuo et al. (2006). The mean crack size at point $C''$ predicted by the current model is $\bar{c}_{C''}\approx 9\bar{c}_{0}$, somewhat smaller than that by the DCA model ($\approx$$10\bar{c}_{0}$). Following point $C''$, as shown in Fig. 6, the material unloads elastically with the damaged modulus corresponding to the crack size of $\bar{c}_{C''}$. Because $\bar{c}_{C''}$ is less than that for the DCA model, the unloading slope is larger (stiffer response) than that given by the DCA model, as shown in Fig. 6. It is also seen that upon the complete removal of the stress ($\sigma_{11}=0$), the strain does not return to zero since the material has been plastically deformed, whereas in the DCA model the strain does return to zero for $\sigma_{11}=0$ (point A).

The cracks normal to the axial direction are closed when the axial stress $\sigma_{11}$ reaches zero, which now corresponds to a positive value of the total strain for Plastic-DCA. From here the compressive stress grows at a gradually higher rate until the same slope as in the DCA is reached, which corresponds to partially deactivated damage, as discussed earlier. At point $D'$, the end of the reverse loading where the strain is $\varepsilon_{11}=-5.0 \times 10^{-4}$, a value of compressive stress $\sigma_{11}=-3.0 \times 10^{-3}$ Mbar is predicted by the Plastic-DCA, compared to $\sigma_{11}=-1.0 \times 10^{-3}$ Mbar by the DCA model. When the material is then reloaded, the response follows the same path as for the unloading until point $C''$, where the stress state reaches the damage surface and the cracks start to grow again until reaching point $E'$ (the end of the cyclic loading).

The object of this work is to present a three-dimensional framework for modeling plasticity and damage in brittle or quasi-brittle materials based on statistical crack mechanics. We are not attempting to represent any specific SiC, but rather are using SiC, with its many well characterized properties, as a convenient model material. We have artificially lowered the yield stress in Section 4.3 in order to exercise the model with what is now a fictitious material, not to better represent the behavior of SiC.

## 5. Summary and conclusions

We have presented an extension to a recently developed damage model for brittle materials (DCA) by incorporating plastic deformation of the materials. The current model (Plastic-DCA) considers damage due to the growth of microcracks as well as plastic deformation in a material by decomposing the strain rate into the contributions of the matrix (uncracked solids), the opening and shear of cracks, the growth of cracks, and plasticity. As was done in previous works (Addressio and Johnson, 1990; Zuo et al., 2006) the current model assumes that the distribution of the microcracks remains isotropic and that the evolution of damage in the material is through the growth of the average crack size.

A set of material routines has been written that numerically integrates the governing evolution equations for the stress, the damage, and the plasticity under a general, three-dimensional state of stress. To illustrate the key features of the new model, a driver program has also been created that provides the material subroutines with a prescribed loading path and strain history. The new model was applied to simulate the response of a silicon carbide (SiC) model material under uniaxial strain loading. Numerical results of the model predictions were shown and comparisons with the results obtained with the previous model (DCA) were provided for both cyclic and large compressive loadings (20%).

For the purpose of comparing the current model and the DCA model, the same set of model constants for SiC and the strain history that were previously used in the DCA model calculations were used in the current work. (The only exception is the addition of the yield stress of the material in the current model, which was determined from the experiment of Grady, 1994.) We have considered the response of material under uniaxial strain conditions with a rate of $10^{5} / \mathrm{s}$. The response to tensile loading shows that the current model can indeed reproduce the results of DCA model when, due to a large amount of crack growth under tension, the stress state is inside the yield surface for SiC considered by Grady. The response to compressive loading shows that while the two models give identical results before yielding takes place, the current model predicts lower axial stress than the previous model. At the compressive strain of $\varepsilon_{11}=-0.2$ (20% compression), the current model predicts an axial stress $\sigma_{11}=-0.51$ Mbar, compared with $\sigma_{11}=-0.59$ Mbar given by the DCA model.

To further demonstrate the features of the model under both damage and plastic deformation under tensile loading, we have also studied a fictional (quasi-brittle) material with a much lower yield stress ($\sigma_{y}=3.5$ kbar) than that for SiC reported by Grady (1994). The numerical results indicate that when plastic deformation is considered, the predicted peak stress is about 12% lower than that obtained from DCA, and the value of the strain corresponding to the peak stress is $\sim 35 \%$ larger. Furthermore, the mean crack size, which is directly related to the macroscopic damage in the material, predicted by the currently model is shown to be consistently lower than that predicted by DCA. The results obtained with the current model indicate that neglecting plastic deformation could lead to over-predictions of both the peak stress of the material and the amount of damage in the material.

The current model contains only one additional material constant: the yield stress; consequently, the simplicity and numerical efficiency, which are important merits of the DCA model, have been preserved. It is believed that the current model is a useful improvement to the DCA model. With the consideration of both damage and plasticity, the model should be more applicable to quasi-brittle materials such as concrete and explosives, which can develop plastic deformation under loading.

For the sake of simplicity, the plasticity part of the model is taken to be a simple, rate-independent, von Mises model without hardening. A rate-independent plasticity model might be a reasonable assumption for the ceramic model material considered here in which there is limited ductility. But in a general material, one might expect the plasticity part to be rate dependent as well. Furthermore, nonlinear effect of the equation of state (EOS) was not considered in the current formulation. A realistic (nonlinear) equation of state is required before the model can be applied to applications involving high-velocity impact. Consideration of a more general plasticity formulation, as well inclusion of a realistic equation of state and comparisons of model prediction with experimental data are topics for future work.

## Acknowledgements

The authors are grateful for technical discussions with F.L. Addressio, J.K. Dienes, J.A. Gilbert, R.M. Hackett, R.R. Little, Jeremy R. Rice and H.A. Toutanji, and for the contributions of M. Bailey to the work. The authors are also grateful to two anonymous reviewers for many constructive comments, including suggestion of the value for the yield stress for SiC used in the paper. The work was supported in part by University Transportation Center for Alabama (UTCA#: 09301), the National Science Foundation (NSF#: DBI-0923402), and a research startup fund from the University of Alabama in Huntsville.

## References

Addressio, F.L., Johnson, J.N., 1990. A constitutive model for the dynamic response of brittle materials. Journal of Applied Physics 67, 3275-3286.

Bennett, J.G., Haberman, K.S., Johnson, J.N., Asay, B.W., Henson, B.F., 1998. A constitutive model for the non-shock ignition and mechanical response of high explosives. Journal of the Mechanics and Physics of Solids 46, 2303-2322.

Costin, L.S., 1983. A microcrack damage model for the deformation and failure of brittle rock. Journal of Geophysics Research 88, 9485-9492.

Dienes, J.K., 1978. A statistical theory of fragmentation. In: Kim, Y.S. (Ed.), Proceedings of the 19th US Symposium on Rock Mechanics, University of Nevada, pp. 51-55.

Dienes, J.K., 1983. On the stability of shear cracks and the calculation of compressive strength. Journal of Geophysics Research 88, 1173-1179.

Dienes, J.K., 1985. A statistical theory of fragmentation processes. Mechanics of Materials 4, 325-335.

Dienes, J.K., 1996. A unified theory of flow, hot spots, and fragmentation with an application to explosive sensitivity. In: Davison, L., Grady, D.E., Shahinpoor, M. (Eds.), High Pressure Shock Compression of Solids II. Springer-Verlag, New York, pp. 366-398.

Dienes, J.K., Zuo, Q.H., Kershner, J.D., 2006. Impact initiation of explosives and propellants via statistical crack mechanics. Journal of Physics and Mechanics of Solids 54, 1237-1275.

Dube, J.F., Pijaudier-Cabot, G., La Borderie, C., 1996. Rate dependent damage model for concrete in dynamics. Journal of Engineering Mechanics 122, 939-947.

Feng, R., Raiser, G.F., Gupta, Y.M., 1996. Shock response of polycrystalline silicon carbide undergoing inelastic deformation. Journal of Applied Physics 79, 1378-1387.

Feng, R., Raiser, G.F., Gupta, Y.M., 1998. Material strength and inelastic deformation of silicon carbide under shock wave compression. Journal of Applied Physics 83,79-86.

Freund, L.B., 1990. Dynamic Fracture Mechanics. Cambridge University Press, New York.

Grady, D.E., Kipp, M.E., 1985. Geometric statistics and dynamic fragmentation. Journal of Applied Physics 58, 1210-1222.

Grady, D.E., 1994. Shock-wave strength properties of baron carbide and silicon carbide. Journal de Physique 4, 385-391.

Gurtin, M.E., 1981. An Introduction to Continuum Mechanics. Academic Press, New York.

Hackett, R.M., Bennett, J.G., 2000. An implicit finite element material model for energetic particulate composite materials. International Journal for Numerical Methods in Engineering 49, 1191-1209.

Hansen, N.R., Schreyer, H.L., 1994. A thermodynamically consistent framework for theories of elastoplasticity coupled with damage. International Journal of Solids and Structures 31, 359-389.

Hansen, N.R., Schreyer, H.L., 1995. Damage deactivation. Journal of Applied Mechanics 62, 450-458.

Holmquist, T.J., Templeton, D.W., Bishnoi, K.D., 2001. Constitutive modeling of aluminum nitride for large strain, high-strain rate, and high-pressure applications. International Journal of Impact Engineering 25, 211-231.

Holmquist, T.J., Johnson, G.R., 2002. Response of silicon carbide to high velocity impact. Journal of Applied Physics 91, 5858-5866.

Johnson, G.R., Holmquist, T.J., 1999. Response of boron carbide subjected to large strains, high strain rates, and high pressures. Physics of Solids 85,8060-8073.

Kipp, M.E., Grady, D.E., 1989a. Shock compression and release in high-strength ceramics. In: Schmidt, S.C., Johnson, J.N., Davison, L.W. (Eds.), Shock Compression of Condensed Matter, Proceedings of the American Physical Society Topical Conference, Albuquerque, New Mexico, August 14-17, 1989, pp.377-380.

Kipp, M.E., Grady, D.E., 1989b. Shock compression and release in high-strength ceramics. Sandia National Laboratories Technical Report SAND89-1461.

Lee, H.K., Simunovic, S., Shin, D.K., 2004. A computational approach for prediction of the damage evolution and crushing behavior of chopped random fiber composites. Computational Materials Science 29, 459-474.

Lewis, M.W., Schreyer, H.L., 1996. A thermodynamically consistent description of dynamic continuum damage. In: Davison, L., Grady, D.E., Shahinpoor, M. (Eds.), High Pressure Shock Compression of Solids II. Springer-Verlag, New York, pp.452-471.

Lubliner, J., 1990. Plasticity Theory. Macmillan Publishing Company, New York.

Lundberg, P., Renstrom, R., Lundberg, B., 2000. Impact of metallic projectiles on ceramic targets: transition between interface defeat and penetration. International Journal of Impact Engineering 24, 259-275.

Meyer Jr., H.W., Abeln, T., Bingert, S., Bruchey, W.J., Brannon, R.M., Chhabildas, L.C., Dienes, J.K., Middleditch, J., 1999. Crack behavior of ballistically impacted ceramic. In: Furnish, M.D., Chhabildas, L.C., Hixson, R.S. (Eds.), Shock Compression of Condensed Matter, AIP Conference Proceedings, vol. 505. Springer-Verlag, New York, pp. 1109-1112.

Ortiz, M., 1985. A constitutive theory for the inelastic behaviour of concrete. Mechanics of Materials 4, 67-93.

Pfau, D.G., DeFisher, S.E., Suarez, D.A., Scheper, E.P., Baker, E.L., 2009. Design for insensitive munitions compliance of XM1069 120 mm multipurpose tank round. In: NDIA IMEM Symposium, Tucson, AZ, May 11-14, 2009, pp. 1-18.

Rajendran, A.M., Kroupa, J.L., 1989. Impact damage model for ceramic materials. Journal of Applied Physics 66, 3560-3565.

Rajendran, A.M., 1994. Modeling the impact behavior of AD85 ceramic under multiaxial loading. International Journal of Impact Engineering 15, 749-768.

Rajendran, A.M., Grove, D.J., 1996. Modeling the shock response of silicon carbide, baron carbide and titanium diboride. International Journal of Impact Engineering 18, 611-631.

Simo, J.C., Ju, J.W., 1987. Stress and strain based continuum damage models, part I and II. International Journal of Solids and Structures 23, 821-869.

Simo, J.C., Ju, J.W., 1989. On continuum damage-elastoplasticity at finite strains: a computational framework. Computational Mechanics 5, 375-400.

Simo, J.C., Hughes, T.J.R., 1998. Computational Inelasticity. Springer-Verlag, New York.

Taylor, L.M., Chen, E.P., Kuszmaul, J.S., 1986. Microcrack-induced damage accumulation in brittle rock under dynamic loading. Computer Methods in Applied Mechanics and Engineering 55, 301-320.

Vogler, T.J., Alexander, C.S., Wise, J.L., Montgomery, S.T., 2010. Dynamic behavior of tungsten carbide and alumina filled epoxy composites. Journal of Applied Physics 107, 043520, 1-13.

Wen, C., Yazdani, S., 2008. Anisotropic damage model for woven fabric composites during tension-tension fatigue. Composite Structures 82, 127-131.

Wilkins, M., Honodel, C., Sawle, D., 1967. An approach to the study of light armor. Report No. UCRL-50284, Lawrence Radiation Laboratory.

Yazdani, S., Schreyer, H.L., 1988. An anisotropic damage model with dilatation for concrete. Mechanics of Materials 7, 231-244.

Yazdani, S., Schreyer, H.L., 1990. Combined plasticity and damage mechanics model for plain concrete. Journal of Engineering Mechanics 116, 1435-1450.

Yazdani, S., Schreyer, H.L., 2003. Nonlinear response of plain concrete shear walls with damage. International Journal of IT in Architecture, Engineering and Construction 1, 251-258.

Zhang, Y.Q., Hao, H., Lu, Y., 2003. Anisotropic dynamic damage and fragmentation of rock materials under explosive loading. International Journal of Engineering Science 41, 917-929.

Zuo, Q.H., Dienes, J.K., 2005. On the stability of penny-shaped cracks with friction: the five types of brittle behavior. International Journal of Solids and Structures 42, 1309-1326.

Zuo, Q.H., Addessio, F.L., Dienes, J.K., Lewis, M.W., 2006. A rate-dependent damage model for brittle materials based on the dominant crack. International Journal of Solids and Structures 43, 3350-3380.

Zuo, Q.H., Dienes, J.K., Middleditch, J., Meyer, H.W., 2008. Modeling anisotropic damage in an encapsulated ceramic under ballistic impact. Journal of Applied Physics 104, 023508, 1-10.