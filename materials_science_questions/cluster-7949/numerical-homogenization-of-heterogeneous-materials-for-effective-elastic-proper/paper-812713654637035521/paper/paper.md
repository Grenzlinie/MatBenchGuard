![](./images/812713654637035521_1.jpg)

# Multi-scale modeling of the chloride diffusivity and the elasticity of Portland cement paste

Mohamad Achour $^{a,b}$, François Bignonnet $^{b}$, Jean-François Barthélémy $^{c}$, Emmanuel Rozière $^{a}$, Ouali Amiri $^{b,*}$

$^{a}$GeM, Research Institute of Civil Engineering and Mechanics, UMR CNRS 6183, Ecole Centrale de Nantes, France
$^{b}$GeM, Research Institute of Civil Engineering and Mechanics, UMR CNRS 6183, Université de Nantes, France
$^{c}$Cerema, Project-team DIMA, 110 rue de Paris, BP 214, 77487 Provins Cedex, France

![](./images/812713654637035521_2.jpg)

## HIGHLIGHTS

- A multiscale, Eshelby-based model of ordinary Portland cement paste is proposed.
- Stiffness and diffusion are upscaled from a unique microstructure description.
- Chloride diffusivity and elastic moduli are well reproduced throughout hydration.

---

## ARTICLE INFO

**Article history:**
Received 28 April 2019
Received in revised form 14 September 2019
Accepted 30 September 2019

**Keywords:**
Cement paste
Micromechanics
Microstructure
Diffusion
Elastic Moduli

---

## ABSTRACT

The multi-scale modeling of Portland cement paste is addressed to predict simultaneously its stiffness and its effective diffusion coefficient of chloride ions. The heterogeneity of cement paste is handled thanks to a hierarchy of Eshelby-based homogenization schemes within the framework of micromechanics. The same microstructure description is used for both mechanical and transport properties. In a first model, the porosity is partitioned at three scales into gel pores, small and large capillary pores. Two layers of hydration products around clinker grains are considered: an inner layer comprising high density C-S-H gel and nano-sized crystal hydrates; and an outer C-S-H layer containing low density C-S-H gel and small capillary pores. In a second model, only three phases are considered: clinker grains, hydrates and capillary pores. A comparison of models with experimental results shows that both transport and mechanical properties of cement paste, throughout hydration, are accurately reproduced.

© 2019 Elsevier Ltd. All rights reserved.

---

## 1. Introduction

The durability of concrete and cement-based materials results from their ability to resist to aggressive environments. Studying chloride-induced corrosion is essential to better understand the durability of reinforced concrete (RC) structures. The initiation time of corrosion is governed by transport mechanisms in concrete, such as ingress of chloride ions. Additionally, the service life of RC structures is characterized not only by the transport properties, but also by the mechanical behavior. The serviceability of concrete structures decreases when exposed to aggressive environments and when mechanical deterioration processes occur [1].

One primary factor which affects the durability is the concrete composition. As it is the main changing component of concrete, cement paste is the most critical phase which governs the mechanical and transport properties of concrete both at early age and at long term. The physical properties of concrete thus depend strongly on the complex microstructure and pore network of hardened cement paste (HCP), which is inherited from hydration reactions [2,3]. During hydration, the microstructure evolves due to the formation of hydration products such as calcium silicate hydrate (C-S-H) or portlandite crystals and the development of the pore network. On the one hand, the hydrates form after setting an increasingly percolating solid phase which builds up the strength and the stiffness of the HCP. On the other hand, the connectivity of the pore space strongly decreases during hydration, which affects the rate of chloride ions penetration.

Several models have been developed to link the diffusion and elastic properties of HCP to its microstructure parameters, such as porosity. These models are either empirical, or based on numerical or analytical multi-scale methods. Empirical models provide

---

* Corresponding author at: 58 rue Michel Ange, 44600 Saint-Nazaire, France.
E-mail addresses: mohamad.achour@univ-nantes.fr (M. Achour), francois.bignonnet@univ-nantes.fr (F. Bignonnet), jean-francois.barthelemy@cerema.fr (J.-F. Barthélémy), emmanuel.roziere@ec-nantes.fr (E. Rozière), ouali.amiri@univ-nantes.fr (O. Amiri).

https://doi.org/10.1016/j.conbuildmat.2019.117124
0950-0618/© 2019 Elsevier Ltd. All rights reserved.

relations between the diffusivity and the relative humidity, power law relations between diffusivity and porosity, temperature and many other factors (see e.g. [4]) or between the elastic moduli and the capillary porosity [5]. However the validity of empirical models is guaranteed only for the type of cement paste which corresponds to the experiments on which they are based.

Multi-scale models aim at estimating the effective behavior of heterogeneous materials from the description of their microstructure and phase properties [6]. However the description of the microstructure of HCP is not a simple task. HCP is a complex multi-scale porous composite, where the pore network needs to be carefully considered because pore sizes vary by several orders of magnitude (from a few nanometres to more than $10\ \mu$m) [3].

Numerical models are based on microstructure simulations by computer models. The development of the 3D digitized model of cement hydration CEMHYD3D by Bentz and Garboczi [7] led to the pioneering work of voxel-based simulations of the diffusion through cement paste [8] and its elastic moduli [9]. Similarly, using the HYMOSTRUC3D hydration simulation model [10], Liu et al. [11] assessed the ionic diffusivity of cement paste by a random walk algorithm (RWA). Ma et al. [12] modeled the transport properties of cement paste using a RWA applied to a refined model in which the capillary porosity is split into two scales. Walther et al. [13] performed Lattice Boltzmann Method simulations on 2D representative volume elements of cement paste generated by bithresholded random gaussian fields in combinaison with Powers' hydration model [14].

An alternative multi-scale modeling strategy is to resort to the analytical homogenization schemes of continuum micromechanics [6,15]. These methods do not involve time consuming computer simulations, and rely on simplified descriptions of the microstructure. In the past fifteen years, the derivation of the effective behavior of cement paste from continuum micromechanics has been an active research field, following the pioneering work of Acker [16], Bernard et al. [2]. A short review of the successful application of micromechanics to the modeling of the mechanical and diffusive properties of cement paste is presented in Section 2.3.

These micromechanics based models developed in the literature are generally focusing either on the mechanical properties or, separately, on the transport properties. Micromechanical models in which the same representation of the microstructure is adopted for both transport and mechanical properties are scarce. To the best of our knowledge, only the model of Bary and Béjaoui [17] theoretically applies to both diffusion and poro-mechanical properties of cement paste. Unfortunately it has only been validated against experimental data on the coefficient of diffusion of tritiated water in mature CEM I pastes, but not on the mechanical properties.

The aim of the present work is to derive consistently using homogenization tools both transport and mechanical properties of HCP from a unified description of its evolving microstructure during hydration. The originality of the present work is to consider the same representation of the cement paste microstructure using micromechanics, with an appropriate description of the pore structure and the solid skeleton, in order to model both the effective elastic and diffusive properties. Two possible models are presented, with different levels of detail on the microstructure description. The strategy adopted to build the models is as follows:

- development of a morphological model of cement paste, which describes the different solid and pore phases at suitable scales;
- selection of appropriate homogenization schemes at each scale, with a specific focus on solid and pore connectivity;
- determination of the physical and geometrical properties of each phase at the microscopic scales;
- assessment of the models against experimental data from the literature on Portland cement paste, for both diffusive and elastic properties, for different hydration degrees and water-to-cement ratios.

The article is organized as follows. Section 2 provides background on continuum micromechanics and reviews existing micro-mechanical models of cement paste for either mechanical or transport properties in order to build in Section 3 two new models – a detailed one and an engineering one – each potentially suitable for both mechanical and transport properties. Section 4 details the assumptions used for the determination of the input data of the models such as the volume fraction, the shape as well as the elastic and diffusive properties of the constituents of cement paste. The performances of the models are then assessed against experimental data from the literature and discussed in Section 5, in terms of elastic moduli and diffusion coefficient during hydration and at the end of the hydration. Finally conclusions are drawn in Section 6.

## 2. Review of homogenization schemes for elasticity and diffusion and applications to cement paste

Within the framework of continuum micromechanics [15] briefly recalled in Section 2.1, Eshelby based homogenization schemes constitute well established tools to estimate the effective behavior of a composite material. In Section 2.2 together with Appendix B, the differences between the most commonly used homogenization schemes are briefly highlighted (see [6,15,18] for more detailed descriptions), with a specific focus on the underlying assumptions regarding the connectivity of the different phases which constitute the heterogeneous material (see also [19]). The purpose is to provide a firm basis for the discussion in Section 2.3 (review of existing models) and Section 3 (construction of new models) on the representation of cement paste morphology across the scales using these homogenization schemes to estimate simultaneously its chloride coefficient of diffusion and elastic moduli.

### 2.1. Principles of homogenization for linear composites

In the case of elasticity of composite media exhibiting a random microstructure under the scale separation hypothesis, the fundamental expression providing the homogenized stiffness tensor of a representative volume element (RVE) composed of different phases is recalled by Zaoui [15]:

$$
\mathbb{C}_{\mathrm{hom}}=\langle\mathbb{C}(\boldsymbol{z}): \mathbb{A}(\boldsymbol{z})\rangle=\sum_{i} f_{i} \mathbb{C}_{i}:\langle\mathbb{A}(\boldsymbol{z})\rangle_{i} \tag{1}
$$

where $f_{i}$ and $\mathbb{C}_{i}$ are the volume fraction and stiffness tensor of phase $i$, $\mathbb{A}(\boldsymbol{z})$ is the strain concentration tensor field relating the local strain tensor $\boldsymbol{\epsilon}$ at point $\boldsymbol{z}$ to the macroscopic one $\boldsymbol{E}$ and $\langle\bullet\rangle$ (resp. $\langle\bullet\rangle_{i}$) denotes the volume averaging operators of a field $\bullet$ over the whole RVE (resp. over the domain occupied by phase $i$). Classical homogenization schemes, as presented in Section 2.2, rely on the Eshelby inhomogeneity problem [20] to estimate the average concentration tensors $\langle\mathbb{A}(\boldsymbol{z})\rangle_{i}$ of each phase $i$ in the material.

The framework of micromechanics may readily be transposed to the homogenization of the diffusion tensor, using the following analogy: the stiffness tensor is replaced by the diffusion tensor $\boldsymbol{D}$, the strain by the concentration gradient $\nabla c$ and the stress by the molar flux.

### 2.2. Eshelby-based homogenization schemes

#### 2.2.1. Eshelby problem

In the Eshelby inhomogeneity problem, a remote stress $\boldsymbol{E}_{\infty}$ is applied to an infinite medium of homogeneous stiffness $\mathbb{C}_{0}$ in which a single inclusion of stiffness $\mathbb{C}_{i}$ is embedded. In the case

where the inclusion has an ellipsoidal shape, the strain field $\boldsymbol{\epsilon}_{i}$ within the inclusion is uniform and given by:

$$
\boldsymbol{\epsilon}_{i}=\mathbb{A}_{0}^{i}: \boldsymbol{E}_{\infty} \quad \text { with } \quad \mathbb{A}_{0}^{i}=\left[\mathbb{I}+\mathbb{P}_{0}^{i}:\left(\mathbb{C}_{i}-\mathbb{C}_{0}\right)\right]^{-1} \tag{2}
$$

where $\mathbb{P}_{0}^{i}$ is the Hill tensor associated to the ellipsoidal shape of the inclusion $i$ embedded in a medium of stiffness $\mathbb{C}_{0}$ and $\mathbb{I}$ is the symmetric identity fourth order tensor. The expressions of the Hill tensor $\mathbb{P}_{0}^{i}$, which is related to the Eshelby tensor $\mathbb{S}_{0}^{i}$ by $\mathbb{S}_{0}^{i}=\mathbb{P}_{0}^{i}: \mathbb{C}_{0}$, may be found in [6,18,21] for elasticity and in [22] for diffusion problems. The Hill tensor depends on the shape of the inclusion but not on its size.

### 2.2.2. Matrix-inclusion materials
In the case where a phase $m$ of the material is a matrix within which separate inclusions of all the other phases $i$ are embedded, the concentration rule (2) of the Eshelby problem can be used to estimate the actual concentration tensors $\langle\mathbb{A}(\boldsymbol{z})\rangle_{i}$ of each inclusion phase $i$. For example, the Mori-Tanaka estimate [23] relies on a specific case of (2) in which the matrix $m$ of stiffness $\mathbb{C}_{m}$ is the embedding media and the remote strain $\boldsymbol{E}_{\infty}$ is equal to the average strain in the matrix [24], which is determined from the strain averaging rule $\langle\boldsymbol{\epsilon}\rangle=\boldsymbol{E}$. The Mori-Tanaka estimate of the homogenized stiffness is:

$$
\mathbb{C}_{\mathrm{hom}} \approx \mathbb{C}_{\mathrm{mt}}=\left\langle\mathbb{C}_{i}: \mathbb{A}_{m}^{i}\right\rangle:\left\langle\mathbb{A}_{m}^{i}\right\rangle^{-1} \tag{3}
$$

where $\mathbb{A}_{m}^{i}$ as been defined in (2) and $\mathbb{A}_{m}^{m}=\mathbb{I}$. In (3), the shape of each inclusion $i$ has to be estimated by an ellipsoid (but not for the matrix).

Alternative homogenization schemes suitable for matrix- inclusion materials are the differential scheme [25], the PCW bound [26], or the interaction direct derivative (IDD) scheme [27]. For all these schemes, a crucial point is that the inclusion phases are never percolating while the matrix phase is always con- nected and is the main contributor to the effective property.

### 2.2.3. Disordered or poly-crystalline materials
When no phase plays the specific role of a matrix, the microstructure is called "disordered" or "poly-crystalline". The above schemes are no longer suitable and instead the self- consistent scheme [28,29] is more appropriate. The construction of the self-consistent estimate is similar to that of the Mori- Tanaka scheme, except that the matrix embedding the particles is replaced by the sought homogenized material. Rearrangement of (3) yields the definition of the self-consistent estimate $\mathbb{C}_{\mathrm{sc}}$ of the effective stiffness as the solution to the non-linear tensor equation:

$$
\mathbb{C}_{\mathrm{hom}} \approx \mathbb{C}_{\mathrm{sc}} \text { solution to }\left\langle\left(\mathbb{C}_{i}-\mathbb{C}_{\mathrm{sc}}\right): \mathbb{A}_{\mathrm{sc}}^{i}\right\rangle=0 \tag{4}
$$

An important feature of the self-consistent scheme is its ability to account for the percolation of the phases depending on their vol- ume fraction and shape. The self-consistent estimates of the elastic and diffusive percolation thresholds of a porous medium are pre- sented in Appendix B. In particular the strong dependence of these thresholds on the solid and poral phase aspect ratios are highlighted.

Statistical physical studies confirm that the connectivity of the phases, characterized by their percolation thresholds, strongly depends on the shape of the particles [30-33] but also indicate that it depends on the particles size distribution (PSD) [34,35], which is not accounted for by the self-consistent scheme. Indeed, while sta- tistical physical studies provide accurate values of the percolation thresholds on explicit morphological models, the self-consistent scheme in which the morphology is implicitly accounted for pro- vides only "poor man's percolation" [33]. Values of the percolation porosities predicted by the self-consistent scheme have been crit- icized, so one should be careful when relying on them [21].

However, an appropriate trend in term of phase aspect ratio has been observed against numerical simulations (see e.g. [36]). Fur- ther, the percolating behavior of the self consistent scheme is a valuable tool to model phenomena such as setting processes or sharp variations in the effective properties w.r.t. the phases volume fraction, such as the diffusion coefficient of cement paste w.r.t. cap- illary porosity. In the subsequent modeling developments, the per- colating behavior is described by the self-consistent scheme. It should be kept in mind that the percolation values and particles aspect ratios used in the modeling are only to be considered as indicative, and may not exactly pertain to the actual microstruc- ture features.

Finally, the self-consistent and the Mori-Tanaka schemes can be generalized to morphological patterns made of concentric spheri- cal layers [37] or confocal ellipsoids [38]. This generalization will be useful to model the inner and outer layers of hydration products around a hydrating clinker grain in cement paste.

### 2.3. Review of some existing morphological models of cement paste
A number of Eshelby-based homogenization models have already been proposed for the description of the mechanical or transport properties of cement paste. As these models perform generally well for the property (resp. mechanical or transport) for which they have been designed, the following comments mainly focus on the portability of these models to the other prop- erty (resp. transport or mechanical) for which they have not been designed. The purpose of this short review is to provide some guidelines for the developments of multi-scale models suitable simultaneously for transport and mechanical properties.

#### 2.3.1. Mechanics oriented models
In the early mechanical models of Constantinides and Ulm [39], Ulm et al. [40], Stora et al. [41], the capillary pores are embedded in a matrix of aging C-S-H. The morphological models employed by Pichler et al. [42], Honorio et al. [43], although more sophisticated, are also based on a similar assumption. Stora et al. [19] pointed out that for diffusion problem such morphology does not allow to reproduce the changes of diffusion coefficients from low to high $w/c$ ratios by several order of magnitudes, which are experimen- tally observed in cement pastes (see e.g. [44]). Further, these mod- els implicitly assume that the solid phase is always connected and forms a rigid skeleton that plays a mechanical role, even at the onset of the hydration reaction.

Alternative representations of the cement paste by Bernard et al. [2], Grondin et al. [45], Venkovic et al. [46] feature a self- consistent assemblage of aging C-S-H, other hydrates, unhydrated clinker and capillary pores at the cement scale. As mentioned above, a self-consistent scheme at this scale is a desirable feature to account for various order of magnitudes in HCP diffusivities. Another advantage of this morphological representation is to cap- ture cement setting through the percolation threshold of the self- consistent scheme. However, although the setting of the paste is appropriately modeled by the percolation of the solid phase for $w/c>0.32$, non-zero elastic moduli are predicted for a zero hydra- tion degree at low $w/c$. This results from an initial volume fraction of the clinker phase at this scale above $1/2$ for $w/c<0.32$, where $1/2$ is the lowest solid phase percolation threshold among the set of self-consistent assemblages of spheroidal solid particles and spherical (or even prolate) pores (see Fig. B.14b).

A sound way to solve the issue of a non-zero stiffness at zero hydration and low $w/c$ is to consider that anhydrous clinker grains are surrounded by densifying inner/outer layers containing some or all of the capillary porosity and hydrates. The model of Sanahuja

et al. [36] is based on this assumption and provides a good agreement with experimental results on the evolution of elastic moduli throughout hydration for a wide range w/c. Unfortunately, its direct transposition to diffusion leads to a zero diffusion coefficient in the inner and outer hydrate layers, since these are modeled as a self-consistent assemblage of flat solid particles and spherical pores.

In order to keep the number of microstructural model parameters to a minimum, so-called multi-scale engineering models have been proposed by Pichler et al. [47], Pichler and Hellmich [48], Pichler et al. [49]. The model of Pichler et al. [47] involves only one scale transition, in which the self-consistent scheme is used to describe cement paste as a disordered assemblage of three phases: hydration products, anhydrous clinker and capillary pores, whose volume fractions are directly estimated from Powers' hydration model [14]. A subsequent improvement has been proposed in Pichler and Hellmich [48], Pichler et al. [49] with two scale transitions. The first level consists in a hydrate foam comprising a self-consistent assemblage of spherical capillary pores and acicular hydration products, while the second level treats cement paste as a matrix-inclusion composite using Mori-Tanaka scheme with spherical anhydrous clinker inclusions in a matrix of hydrate foam. In this way, the effective stiffness is always zero at the onset of hydration and the gel/space ratio (density of the hydrate foam) is found to be a key parameter governing the mechanical properties. Based on this model, Termkhajornkit et al. [50] suggested further improvements to assess the role of the different hydrate phases (C-S-H, CH, AFm). A conclusion of their multi-scale study was that C-S-H is the first-order parameter explaining the compressive strength and that other hydrates simply act as reinforcing inclusions.

### 2.3.2. Diffusion oriented models
Eshelby-based multi-scale models of the diffusion properties of cement paste are scarcer in the literature than mechanics oriented ones. In a pioneering work, Pivonka et al. [51] modeled HCP as a two-phase composite using the differential scheme with capillary pores as a matrix and non-diffusive solid inclusions. As stated in Section 2.2, a direct transposition of this morphology to elasticity is not appropriate as it yields a zero effective stiffness. An improved model by Damrongwiriyanupap et al. [52] is based on the self-consistent scheme, but its direct transposition to elasticity would exhibit a non-zero stiffness at a zero hydration degree for very low w/c. Both models predict zero diffusivity for HCP with a w/c ratio below which Powers' hydration model predicts zero capillary porosity, whereas experimental measurements rather indicate a change in the order of magnitude of the diffusion coefficient.

Stora et al. [19] proposed that the gel pores may constitute privileged percolating paths for diffusion. They suggested to consider the capillary pores, together with part of the mineral phases (CH, AF), as inclusions embedded in an outer C-S-H gel matrix using a Mori-Tanaka scheme at an intermediate scale. At a finest scale, to capture the pronounced variations of the transport properties of C-S-H gels, the diffusivity of the inner and outer C-S-H phases was modeled using a so-called Mixed Composite Spheres Assemblage estimate (see [53]), which can be interpreted as a generalized self-consistent scheme with two types of composite inclusions: a pore in a solid shell and a solid particle in a pore shell. Note that the direct transposition of this scheme to mechanical properties is unfortunately not appropriate as a morphological pattern made of a solid grain in a pore shell has no mechanical meaning. At the largest scale, the anhydrous clinker is assumed surrounded by the inner and outer layers as in the model of Sanahuja et al. [36]. A good agreement with experimental data on the diffusion coefficient of tritiated water has been obtained by assuming a low diffusivity in the nano-sized C-S-H gel pores, but a bulk diffusion coefficient in the capillary pores instead of a low diffusivity as in Pivonka et al. [51], Damrongwiriyanupap et al. [52].

To sum up, although a large number of morphological models have already successfully been proposed for either fluid transport or mechanical properties, the above discussion underlines that devising a morphological model of cement paste suitable for both fluid transport and mechanical properties is not as straightforward as it might be thought at first sight. In what follows, we present two different multi-scale models of cement paste, each designed to estimate the elastic moduli and diffusion coefficient of the cement paste as a function of the original water to cement ratio and hydration degree based on a consistent description of the microstructure:

- a detailed model which distinguishes small and large capillary pores as well as inner, high density and outer, low density hydration products.
- a simplified, engineering model which relies on a much more restricted set of microstructure parameters.

The performance of these models will be assessed and discussed in Section 5.

## 3. Construction of new multi-scale models of cement paste for both elastic and diffusive properties

### 3.1. Detailed model of cement paste

#### 3.1.1. Overview of the microstructure model
As seen from the diversity of existing micro-mechanical models of cement paste reviewed in Section 2.3, there is no unique choice to model the complex morphology of cement paste. Cement paste indeed involves a continuum of length scales, whose separation is somewhat arbitrary. Yet, from a pragmatic point of view, micromechanics based models have demonstrated their ability to model various properties of cement paste.

Based on the above review of existing models, we present a first, rather detailed morphological representation of cement paste across the scales (see Fig. 1 and Table 1). This model is mostly inspired from Ma et al. [3] but also incorporates several features of the models described in Section 2.3:

- **Level II**: At the largest scale, the Portland cement paste is modeled as a disordered assemblage of large capillary pores (LCPs >100 nm), micro-sized crystal hydrates (portlandite, ettringite, monocarbonate [54]) and composite inclusions representing the clinker surrounded by two hydrate layers called respectively inner layer (high density) and outer C-S-H layer (low density).
- **Level I**: At an intermediate scale, the inner layer is considered as a disordered mix of high density C-S-H gel and nano-sized crystal hydrates. In turn, the outer C-S-H layer is considered as a mixture of small capillary pores (SCPs ≈3-100 nm) and low density C-S-H gel.
- **Level 0**: At the finest scale, the high and low density C-S-H gels are described as disordered assemblages of solid C-S-H bricks and gel pores.

The particularity of this model is to classify the capillary pore network into small and large capillary pores (SCPs and LCPs respectively) to be consistent with the several orders of magnitude encountered in capillary pore sizes, as proposed by [3,55]. The large size range 3-100 nm for the SCPs is selected since it corresponds to the pore sizes investigated by nitrogen adsorption measurements [56], which will be used in Section 4.1.3 to

![](./images/812713654637035521_3.jpg)

Fig. 1. Schematic representation of the detailed model of cement paste.

<table>
<caption>Table 1<br>Summary of model microscale parameters: elasticity properties ($E, v$), diffusion coefficients ($D$) and aspect ratios ($\omega$). Size ranges are only indicative.</caption>
<thead>
<tr>
<th>phase</th>
<th>size range</th>
<th>$E$ (GPa)</th>
<th>$v$ (-)</th>
<th>source</th>
<th>$D$ (m²/s)</th>
<th>$\omega$ (-)</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="7">Detailed model</td>
</tr>
<tr>
<td colspan="7">Level II: cement paste</td>
</tr>
<tr>
<td>anhydrous clinker</td>
<td>1–50 μm</td>
<td>135</td>
<td>0.3</td>
<td>[16]</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td>micro crystal hydrates</td>
<td>1–10 μm</td>
<td>42.3</td>
<td>0.324</td>
<td>[9] (Portlandite)</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td>large capillary pores</td>
<td>0.1–10 μm</td>
<td>0</td>
<td>–</td>
<td></td>
<td>$D_{bulk}$</td>
<td>1</td>
</tr>
<tr>
<td colspan="7">level I: hydrate layers</td>
</tr>
<tr>
<td>nano crystal hydrates</td>
<td>&lt;1 μm</td>
<td>42.3</td>
<td>0.324</td>
<td>[9] (Portlandite)</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td>LD- and HD-C-S-H particles</td>
<td>0.1–1 μm</td>
<td></td>
<td></td>
<td>upscaled from model</td>
<td></td>
<td>0.14</td>
</tr>
<tr>
<td>small capillary pores</td>
<td>3–100 nm</td>
<td>0</td>
<td>–</td>
<td></td>
<td>$D_{bulk}$</td>
<td>1</td>
</tr>
<tr>
<td colspan="7">level 0: C-S-H gels</td>
</tr>
<tr>
<td>C-S-H brick</td>
<td>5–60 nm</td>
<td>63</td>
<td>0.27</td>
<td>see text</td>
<td>0</td>
<td>0.12</td>
</tr>
<tr>
<td>gel pores</td>
<td>&lt; 3nm</td>
<td>0</td>
<td>–</td>
<td></td>
<td>$2.46×10^{-2}D_{bulk}$</td>
<td>1/0.12</td>
</tr>
<tr>
<td colspan="7">Engineering model</td>
</tr>
<tr>
<td colspan="7">Level II: cement paste</td>
</tr>
<tr>
<td>anhydrous clinker</td>
<td>1–50 μm</td>
<td>135</td>
<td>0.3</td>
<td>[16]</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td colspan="7">level I: hydrate foam</td>
</tr>
<tr>
<td>hydration products</td>
<td>&lt;10 μm</td>
<td>25.3</td>
<td>0.29</td>
<td>[65] (see text)</td>
<td>$5.04×10^{-4}D_{bulk}$</td>
<td>0.013</td>
</tr>
<tr>
<td>capillary pores</td>
<td>&lt;10 μm</td>
<td>0</td>
<td>–</td>
<td></td>
<td>$D_{bulk}$</td>
<td>6</td>
</tr>
</tbody>
</table>

quantitatively partition pore volumes between scales I and II. In this model, the diffusion may occur through the LCPs, the SCPs of the outer C-S-H layer and the gel pores of the high and low density C-S-H gels. The variation of the connectivity of these different pore types as a function of the water to cement ratio and the hydration degree is a key point in the modeling of the transport properties of the cement paste [57], which is detailed below.

### 3.1.2. Level 0: C-S-H gels
At the lowest scale, the C-S-H gels are modeled as an assemblage of bricks of solid C-S-H and of gel pores as shown in Fig. 1. Two types of C-S-H gels are considered, a low density (LD-C-S-H) gel in the outer C-S-H layer and a high density (HD-C-S-H) gel in the inner layer. Following Ulm et al. [40], Constantinides and Ulm [58], the gel porosities $\phi_{hdcsh}$ and $\phi_{ldcsh}$ of the HD- and LD-C-S-H are assumed to be equal to:

$$
\phi_{hdcsh} = \frac{f_{hdcsh}^{p}}{f_{hdcsh}} = 0.24 \quad ; \quad \phi_{ldcsh} = \frac{f_{ldcsh}^{p}}{f_{ldcsh}} = 0.37 \tag{5}
$$

where $f_{hdcsh}^{p}$ is the HD-C-S-H gel pore volume and $f_{hdcsh}$ the volume of HD-C-S-H per unit volume of cement paste. These values are here assumed intrinsic to all ordinary Portland cement pastes [40].

The gel morphology is accounted for by the self-consistent scheme as in the illustrative example of Appendix B. Given the great variability of C-S-H morphology [59], the representation of C-S-H bricks and gel pores by mono-shaped spheroids such as in [58,36] is a strong modelling assumption which lead to a controversy on the choice of the aspect ratio [60,61]. Yet for the sake of simplicity and based on observations of the C-S-H solid particles as elementary bricks of dimensions $60×30×5$ nm [62], we consider the elementary C-S-H bricks as oblate-shaped solid particles, whose aspect ratio would be $\omega_{csh}^{s} = 5/\sqrt{30×60} = 0.12$ [36]. The elementary C-S-H bricks are assumed non-diffusive. Two fundamental requirements are that the HD- and LD-C-S-H gel diffusion coefficients have to be non-zero so that water can access the anhydrous clinker throughout hydration, and that the gel stiffness is non-zero.

The effect of the shape used to model the gel pores has not been previously addressed in the literature. Under the above assumption of non-diffusive oblate solid particles, Figs. B.14 and 9 indicate that considering the pores as spherical as done by previous investigators leads to zero diffusion coefficients for HD- and LD-C-S-H, and is therefore not appropriate. This is also true for HD-C-S-H if the solid particles are assumed spherical,

since the diffusion percolation threshold is for a porosity of $1/3$ when both solid and pores are modeled by spheres. Thus, the gel pores need to be modeled as either flat or elongated spheroids in the present framework. However, an oblate shape is to be excluded, since fulfilling both non-zero diffusion and non-zero stiffness requirements for the gel porosities retained in (5) and $\omega_{csh}^s=0.12$ is not possible for oblate pores (see Fig. B.14). The gel pores have thus to be modeled as prolate spheroids, and an aspect ratio $\omega_{gp}$ greater than 5.8 is required to ensure the percolation of the pore phase for both gel porosities in (5). Due to the lack of definitive observations at this scale, we assume that $\omega_{gp}=1/\omega_{csh}^s\approx8.3$.

We here wish to clarify that the aspect ratios considered herein are only modeling assumptions for which no definitive proof has been exhibited. These retained aspect ratio values are chosen since, as summarized in Fig. 9: (1) they allow to meet non-zero diffusion in both HD- and LD-C-S-H gels and (2) they are as consistent as previous models proposed by Constantinides and Ulm [58], Sanahuja et al. [36] with experimental results on the nano-indentation modulus $M=E/(1-v^2)$ reported by Acker [16], Constantinides and Ulm [39,58].

### 3.1.3. Level I: Inner layer and outer C-S-H layer
At an intermediate scale, the hydration products are considered as two layers which coat the clinker grains. These layers consists in C-S-H gels, other nano crystalline hydration products (portlandite, sulfo-aluminates) and small capillary pores [3].

Inner layer. The inner layer comprises high density C-S-H gel (HD-C-S-H) and nano-sized crystal hydrates [3]. The HD-C-S-H gel and the nano-crystal hydrates will be referred to as the *inner hydration products*. A self-consistent homogenization scheme is used to model the inner layer, in which the nano-crystals are assumed non diffusive.

Both nano-crystals and HD-C-S-H are assumed spherical in the inner layer in order to limit the number of model parameters.

Outer C-S-H layer scale. The outer C-S-H layer comprises low density C-S-H gel (LD-C-S-H) and small capillary pores (SCPs). The size of the SCPs ranges from 3 to 100 nm according to the definition proposed by Ma et al. [3], so that it corresponds to the porosity accessible by nitrogen adsorption. The self-consistent scheme is used to handle the disorganized morphology of the outer C-S-H layer.

On the contrary to the case of the inner layer, the shapes of the particles used to represent the LD-C-S-H and the SCPs in the outer C-S-H layer are of prime importance since they control both the percolation of the solid phase – and hence the setting of cement paste – and the connectivity of the pore space. The capillary porosity is not always connected [44,57,19] and gel pores may constitute privileged paths for diffusion in dense pastes. To model this behaviour using the self-consistent scheme, the SCPs are considered as spheres (which is the least percolating shape) and the LD-C-S-H as oblate spheroids (which hinders the most SCP connectivity). Considering a non spherical shape for the LD-C-S-H adds a degree of freedom to the model, which is identified as follows: (1) a unique value of the LD-C-S-H aspect ratio will be used for all cement pastes, (2) this value will be determined from an inverse analysis of experimental measurements of early age cement paste Young's modulus, as detailed in Section 4.2.

Since the size of the micro-crystal hydrates – typically of a few tens of $\mu$m – is much larger than that of the SCPs, the former have to be introduced at the cement paste scale [3]. Although the LD-C-S-H gel and micro-crystal hydrates are not introduced at the same scale, they are referred to as *outer hydration products* according to the terminology of Ma et al. [3].

### 3.1.4. Level II: Cement paste
At the largest scale, the cement paste is modeled using a generalized self-consistent scheme which involves composite spherical particles made of an anhydrous clinker core surrounded by the two layers of level I as well as spherical large capillary pores (LCPs) and spherical micro-sized crystal hydrates.

Under these assumptions, the connectivity of the solid phase of the cement is hence governed at two distinct scales:
1.  the volume fraction of LCPs has to be lower than $1/2$ to ensure the percolation of the composite particles at level II,
2.  the volume fraction of SCPs among the outer C-S-H layer ($\phi_{scp}^{ocshl}=f_{scp}/(f_{scp}+f_{ldcsh})$) has to be below the elastic percolation porosity $\phi_e$ whose value depends on the LD-C-S-H aspect ratio (see Fig. B.14).

A non presented sensitivity analysis shows that most of the results of the present model are weakly dependent on the aspect ratio of the micro-crystals in the range 0.1 to 100. Within this range, the most significant influence of the micro-crystal shape is on the elastic moduli at very early age, because extreme values of their aspect ratio may change the percolation threshold of the solid phase. This effect is not further investigated in the present work, and the micro-crystals are kept spherical to limit the number of model parameters.

A flowchart of calculations for the detailed model is sketched in Fig. 2.

### 3.2. Engineering model of cement paste
In this section, we consider an alternative modeling strategy which is based on a simplified description of the cement paste inspired from the so-called multi-scale engineering models by [47-49,51,52]. The advantages of the engineering model are that the microstructure model parameters are kept to a minimum. Further, closed form or at least semi-analytical expressions of the effective properties are obtained as a function of the water to cement ratio and the hydration degree.

#### 3.2.1. Morphological model
The proposed engineering model is designed to benefit from the hydration model of Powers and Brownyard [14], which distinguishes mainly three phases: anhydrous clinker, hydration products and capillary pores. Since we aim at modeling the mechanical and diffusion properties from a unified description of the microstructure, the model should ensure a suitable percolation of both solid and pore phases throughout hydration; letting aside some details. Following Pichler and Hellmich [48], Pichler et al. [49], we adopt a two scale description of cement paste (see Fig. 3):
- **Level I: a hydrate foam** is described as an aging disordered assemblage of hydration products and capillary pores. A self-consistent scheme is used, with both the hydrates and capillary pores modeled with spheroidal shapes.
- **Level II: cement paste** is described as a composite with a matrix of hydrate foam from level I in which spherical anhydrous clinker inclusions are embedded, using the Mori-Tanaka scheme.

Following the same arguments than for the C-S-H gels of the detailed model (see Section 3.1.2), the hydrates will here be modeled by oblate spheroids and the capillary pores by prolate spheroids with finite aspect ratio, so that the connectivity of these phases will depend on the porosity of the hydrate foam. Further, as a refinement of the models of [51,52], the hydration products will be considered diffusive – albeit weakly – to account for the

![](./images/812713654637035521_4.jpg)

Fig. 2. Flowchart of calculations for the detailed model.

![](./images/812713654637035521_5.jpg)

Fig. 3. Schematic representation of the engineering model of cement paste.

percolation of the gel porosity they comprise. In that way, a non-zero diffusion coefficient will be retrieved for mature pastes with low w/c, as observed experimentally and not accounted for by these previous models.

Since the hydrate foam is considered as a matrix at the cement scale, its percolation behaviour will govern that of the cement paste. Akin to the strategy developed by Sanahuja et al. [36] for the outer layer, the aspect ratio of hydrates will be calibrated from experimental data on cement setting in Section 4.2.

### 3.2.2. Closed-form expression of the diffusion coefficient for the engineering model
Level I The closed-form expression of the diffusion coefficient $D_f$ of the hydrate foam is obtained following the details given in Appendix A.1 as a function of the foam porosity $\varphi$, the diffusion coefficients $D_h$ and $D_{cp}$ of the hydrates and the capillary pores and the aspect ratios $\omega_h$ and $\omega_{cp}$ of the particles used to represent them.Level II At the cement scale, the clinker particles are modeled as non-diffusive spherical inclusions in the matrix of hydrate foam using the Mori-Tanaka scheme (3). This yields the following estimate of the cement paste diffusion coefficient:

$$
D_{\text{cement}}^{\text{eng.}} = \frac{1-f_a}{1+f_a/2} D_f \tag{6}
$$

where $f_a$ is the volume fraction of anhydrous clinker in the cement paste.

### 3.2.3. Elastic moduli for the engineering model
Level I. The stiffness tensor of the hydrate phase is assumed isotropic, with bulk and shear moduli $k_h$ and $\mu_h$ respectively. The self-consistent estimate of the hydrate foam stiffness is solution to (4), which results in two coupled equations (see Appendix A.2) on the bulk and shear moduli $k_f$ and $\mu_f$ of the foam. The latter depend on the foam porosity $\varphi$, the hydrate moduli and the aspect ratios $\omega_h$ and $\omega_{cp}$ of the particles used to represent the hydrates and the capillary pores. In the general case, the system (A.14) reduces to two high-order polynomial equations, which can be readily solved using classical numerical solvers.Level II. The elastic moduli of the cement paste are determined using the Mori-Tanaka scheme with the anhydrous clinker modeled by spherical inclusions of bulk and shear moduli $k_a$ and $\mu_a$ in the matrix of hydrate foam obtained from the previous homogenization step. Projection of (3) on the

spherical and deviatoric isotropic fourth order tensors $\mathbb{J}$ and $\mathbb{K}$ directly yields the bulk and shear moduli for this engineering model as:

$$
\begin{aligned}
k_{\text{cement}}^{\text{eng.}} &= k_{f}\left[1+f_{a} \frac{k_{a}-k_{f}}{k_{f}+\left(1-f_{a}\right) \alpha_{f}\left(k_{a}-k_{f}\right)}\right] \\
\mu_{\text{cement}}^{\text{eng.}} &= \mu_{f}\left[1+f_{a} \frac{\mu_{a}-\mu_{f}}{\mu_{f}+\left(1-f_{a}\right) \beta_{f}\left(\mu_{a}-\mu_{f}\right)}\right]
\end{aligned} \tag{7}
$$

where $\alpha_{f}, \beta_{f}$ are the components of the Eshelby tensor of a sphere in an isotropic elastic medium of bulk and shear moduli $k_{f}$ and $\mu_{f}$:

$$
\alpha_{f}=\frac{3 k_{f}}{3 k_{f}+4 \mu_{f}} \quad ; \quad \beta_{f}=\frac{6}{5} \frac{k_{f}+2 \mu_{f}}{3 k_{f}+4 \mu_{f}} \tag{8}
$$

A flowchart of calculations for the engineering model is sketched in Fig. 4.

## 4. Determination of the model inputs

The multi-scale models proposed in the above section require as input data the diffusion and the elastic characteristics of all the phases as well as their volume fractions. This section details the retained hypothesis for this purpose.

### 4.1. Volume fractions

In the detailed paste model of Section 3.1, the homogenization workflow requires the volume fractions $f_{i}$ in cement paste of all the following phases $i$: anhydrous clinker $(f_{a})$, LCPs $(f_{lcp})$, SCPs $(f_{scp})$, nano-crystal hydrates $(f_{nc})$, micro-crystal hydrates $(f_{mc})$, HD-C-S-H $(f_{hdcsh})$, LD-C-S-H $(f_{ldcsh})$. Following the terminology of Ma et al. [3], we will refer also to inner hydration products $(f_{ihp}=f_{hdcsh}+f_{nc})$, outer hydration products $(f_{ohp}=f_{ldcsh}+f_{mc})$, hydration products $(f_{h}=f_{ihp}+f_{ohp})$ and outer domain $(f_{od}=f_{ohp}+f_{scp})$.

![](./images/812713654637035521_6.jpg)

Fig. 4. Flowchart of calculations for the engineering model.

### 4.1.1. Powers' hydration model

Powers' hydration model is usedto estimate the main phases of the cement paste during hydration [14,63]. The required information are the density of anhydrous clinker $\rho_{a}=3.13$ as well as the volumes of consumed water $\kappa_{w}=1.31$ and produced hydrates $\kappa_{h}=2.13$ when one unit volume of anhydrous clinker is consumed by the hydration reaction. Note that these values are for Portland cement and may vary depending on the cement composition. Further, these values include the gel pores in the volume of produced hydrates but not the capillary pores, and the volume of consumed water comprises a part reacting with hydrates i.e. chemically bound water and a part filling gel pores [64].

During hydration, the volume fractions of clinker, water, and hydration products evolve. This evolution depends on the initial water to cement ratio $w/c$ and on the degree of hydration $\alpha$ defined as the ratio of hydrated clinker to initial anhydrous clinker, as well as on the curing conditions. Referring to the capillary pores as the complementary domain to the anhydrous cement and hydration products in cement paste, the volume fractions of anhydrous clinker, hydration products and capillary pores are expressed during hydration by [14,63]:

$$
\begin{aligned}
f_{a} &=\frac{1-\alpha}{1+\rho_{a} w / c} \quad ; \quad f_{h}=\frac{\kappa_{h} \alpha}{1+\rho_{a} w / c} \quad ; \\
f_{c p} &=\frac{\rho_{a} w / c+\left(1-\kappa_{h}\right) \alpha}{1+\rho_{a} w / c}
\end{aligned} \tag{9}
$$

The hydration products are classically assumed to comprise a volume fraction of 28% of gel porosity, so that the total porosity of the cement paste is $0.28 f_{h}+f_{cp}$.

During hydration, $\alpha$ increases from zero up to a maximum hydration degree $\alpha_{\text{max}}$. Several cases may be distinguished for the maximum hydration degree, depending on the curing conditions [63]:

1. When water is not available to the entire bulk of paste from external sources, hydration stops when one of the reactant - water or clinker - is depleted. The maximum hydration degree is then:

$$
\alpha_{\max }= \begin{cases}\frac{w / c}{\kappa_{w} / \rho_{a}} & \text { if } w / c \leqslant \kappa_{w} / \rho_{a} \\ 1 & \text { otherwise }\end{cases} \tag{10}
$$

where $\kappa_{w}/\rho_{a} \approx 0.42$ for the above given values.

2. When water is available to the entire bulk of paste from external sources, hydration stops either when the clinker is depleted or when all the available space is filled by the hydration products and residual clinker (no residual capillary porosity). The maximum degree of hydration is then:

$$
\alpha_{\max }= \begin{cases}\frac{\rho_{a} w / c}{\kappa_{h}-1} & \text { if } w / c \leqslant \frac{\kappa_{h}-1}{\rho_{a}} \\ 1 & \text { otherwise }\end{cases} \tag{11}
$$

where $(\kappa_{h}-1)/\rho_{a} \approx 0.36$ for the above given values.

In that case, excess water $w_{\text{excess}}$ must be available for the chemical process, so that the final water to cement ratio is equal to the initial $w/c$ ratio plus $w_{\text{excess}}/c$. In particular, in the experimental study of Helmuth and Turk [65] to which we will refer later on, the initial water to cement ratios $w/c$ at casting time are not reported. Instead, the total water content to ignited weight ratio $w_{t}/c_{i}$ has been measured on very mature pastes cured with extra water. This $w_{t}/c_{i}$ ratio should hence correspond to the final water to cement at the maximum hydration (given by (11)), from which the original $w/c$ ratio may be deduced by resolution of:

$$
w_{t} / c_{i}= \begin{cases}w / c \frac{\kappa_{w}}{\kappa_{h}-1} & \text { if } w / c \leqslant \frac{\kappa_{h}-1}{\rho_{a}} \\ w / c+\frac{1+\kappa_{w}-\kappa_{h}}{\rho_{a}} & \text { if } w / c \geqslant \frac{\kappa_{h}-1}{\rho_{a}}\end{cases} \tag{12}
$$

where hydration stops either due to total capillary space filling or due to total anhydrous clinker consumption (see Fig. 5). Using (12), the total porosities reported in Helmuth and Turk [65] comply precisely with the predicted ones by Powers' model, assuming the usual value of 28% of gel porosity among hydrates.

The input volume fractions ($f_a$ and $\varphi$) for the engineering model presented in Section 3.2 are directly drawn from (9), with the hydrate foam capillary porosity $\varphi = f_{cp}/(f_{cp}+f_h)$. The detailed model presented in Section 3.1 requires further distinction of the different types of hydrates and capillary porosities, as presented below.

### 4.1.2. Distinction of the different types of hydrates
The revised model of the microstructure of Portland cement paste proposed by Tennis and Jennings [66] provides an estimate of the mass ratio $M_r$ of LD-C-S-H to the total C-S-H in dried conditions by:
$$
M_r=0.538+\alpha(3.017w/c-1.347) \tag{13}
$$

This expression has been established by fitting experimental results on cement pastes with $w/c\in[0.25;0.50]$. As it leads to $M_r > 1$ at high values of $\alpha$ for $w/c > 0.60$, the values of $M_r$ obtained from (13) are thresholded to 1 when necessary. Assuming that the solid phases of the two types of C-S-H (i.e. excluding gel pores) have the same density, the mass ratio (13) and the C-S-H gel porosities (5) provide a relationship on the volume fractions of LD- and HD-C-S-H:
$$
M_r=\frac{\left(1-\phi_{ldcsh}\right)f_{ldcsh}}{\left(1-\phi_{ldcsh}\right)f_{ldcsh}+\left(1-\phi_{hdcsh}\right)f_{hdcsh}} \tag{14}
$$

Next, following Ma et al. [3], it is assumed for simplicity that the volume fraction $f_{nc}$ (resp. $f_{mc}$) of the nano-crystal hydrates (resp. micro-crystal) is a constant percentage $\eta$ of the volume fraction $f_{ihp}$ (resp. $f_{ohp}$) of the inner (resp. outer) hydration products:
$$
\begin{aligned}
& f_{nc}=\eta f_{ihp} \quad \text{with} \quad f_{ihp}=f_{nc}+f_{hdcsh} \\
& f_{mc}=\eta f_{ohp} \quad \text{with} \quad f_{ohp}=f_{mc}+f_{ldcsh}
\end{aligned} \tag{15}
$$

![](./images/812713654637035521_7.jpg)

Fig. 5. Relation between final $w_t/c_i$ and initial $w/c$ ratio according to Powers' model when excess water is available to the entire bulk of paste from external sources.

where all these volume fractions are per unit volume of cement paste. The combination of eqs. (15), (9) and (14) allows to derive the volume fractions of the inner and outer hydration products, HD- and LD-C-S-H gels as well as nano- and micro-crystal hydrates:
$$
\begin{array}{ll}
f_{ohp}=f_{h}\left(1+\frac{1-M_{r}}{M_{r}} \frac{1-\phi_{ldcsh}}{1-\phi_{hdcsh}}\right)^{-1} & f_{ihp}=f_{h}-f_{ohp} \\
f_{mc}=\eta f_{ohp} & f_{nc}=\eta f_{ihp} \\
f_{ldcsh}=(1-\eta)f_{ohp} & f_{hdcsh}=(1-\eta)f_{ihp}
\end{array} \tag{16}
$$

In what follows, we consider a proportion $\eta=20\%$ of crystalline hydrates among hydration products in order to obtain total porosities (gel + capillary) in agreement with the predictions of Powers' model.

### 4.1.3. Capillary porosity partition
As mentioned earlier, the large and small capillary pores consist in the complementary domain to hydrates and anhydrous cement, and their total volume fraction $f_{cp}$ is given by Powers' hydration model (9). To partition $f_{cp}$ into the volume fractions $f_{scp}$ and $f_{lcp}$ of SCPs and LCPs, we resort to the assumption suggested by Ma et al. [3]: the porosity of SCPs in the outer domain $\phi_{od}=f_{scp}/(f_{ohp}+f_{scp})$ is assumed negatively proportional to the filling ratio of the capillary network by outer hydrates defined as $\psi_f=f_{ohp}/(f_{ohp}+f_{cp})$. Hence it is assumed that:
$$
\phi_{od}=\phi_{od}^{\text{init}}\left(1-\psi_f\right) \tag{17}
$$
where $\phi_{od}^{\text{init}}$ is the initial porosity of the SCPs in the outer domain when the hydration reaction starts. As shown in Fig. 7, experimental data from nitrogen adsorption by Ma and Li [56] in the range $w/c\in[0.3,0.5]$ can be fitted with a good agreement by (17) with $\phi_{od}^{\text{init}}=0.63$ regardless of $w/c$.

Finally, the volume fractions $f_{scp}$ and $f_{lcp}$ of SCPs and LCPs can be derived from (9), (16) and (17) as:
$$
f_{scp}=\frac{\phi_{od}}{1-\phi_{od}}f_{ohp} \quad ; \quad f_{lcp}=f_{cp}-f_{scp} \tag{18}
$$

Our capillary porosity partition, while taking advantage of (17), slightly differs from that provided in Ma et al. [3]. Indeed the latter is based on the assumption that the inner hydrates occupy exactly the same volume as the dissolved fraction of the anhydrous particle. In addition, the volume of the outer products is obtained by consistency with the total amount of hydrate products (9). This hypothesis implies that the ratio between LD-C-S-H and total C-S-H remains constant over the hydration process, which contradicts (13). Therefore we preferred to comply with (13), which is supported by experimental results, instead of keeping as a constant the current volume occupied by the composite formed by the anhydrous core surrounded by the inner products.

The volume fractions of hydrates (16) and capillary pores (18) required by the detailed multi-scale model are plotted on Fig. 6 as a function of the hydration degree $\alpha$ for $w/c=0.3$ and $w/c=0.5$, up to the maximum hydration degree given by (11).

### 4.2. Calibration of the aspect ratios of the hydrates
The hydrates aspect ratio is calibrated so as to retrieve experimental values of the hydration degree of setting $\alpha_0$ from the model in which setting is controlled by the percolation threshold of the self-consistent scheme, as in [36].

Experimental data on hydration degree of setting As reference values for the hydration degree of setting for $w/c$ in the range 0.25 to 0.60, we adopt the early age data on elastic moduli reported by Boumiz et al. [67] from ultrasonic measurements and by Zhang et al. [68] from Vicat setting tests combined with ultrasonic

![](./images/812713654637035521_8.jpg)

Fig. 6. Volume fractions for w/c = 0.3 and 0.5 for the detailed model assumptions.

![](./images/812713654637035521_9.jpg)

Fig. 7. Fitting of the relation (17) to the experimental data from [56].

measurements. Akin to the strategy adopted by [69] from the compressive strength measures of [70], the values of $\alpha_0$ are obtained from the data of [67] by assuming an affine relationship between the Young's modulus and the degree of hydration, see Fig. 8a. Due to the difficulty to accurately determine the hydration degree in the very first hours of hydration, the earliest data points are disregarded in the fitting procedure. The inferred values are reported in Fig. 8b and are in good agreement with those reported by Zhang et al. [68]. Note that values of $\alpha_0$ here determined from elastic moduli are lower than those extrapolated from compressive strength by [2,69-71].

Detailed model. The setting of the cement paste in the detailed model requires the percolation at two scales: the outer C-S-H layer (level I) and the cement paste (level II). The aspect ratio $\omega_{ldcsh}$ of the LD-C-S-H gel particles of the outer C-S-H layer is calibrated in order to retrieve the experimental values determined in Fig. 8a and those reported by [68]. Assuming that the SCPs can be described by spherical particles, the best fit is obtained for $\omega_{ldcsh}=0.138$ for the LD-C-S-H gel particles. The degree of hydration at set obtained for the detailed model is thus a composite curve w.r.t. the water to cement ratio w/c. For $w/c<0.41$, the percolation of level I occurs later than that of level II and the calibrated model is able to reproduce experimental hydration degrees at set. Hence, as opposed to the earlier models of [2,45-47] based on a self-consistent scheme with all phases at the same scale, no immediate set at $\alpha=0^+$ is simulated by the detailed model even for $w/c<0.32$ since the outer layer is initially not able to transmit mechanical loads. However, for water to cement ratio above 0.41, the percolation of level II occurs later than that of level I, so that the detailed model

![](./images/812713654637035521_10.jpg)

(a) experiments by Boumiz et al. [70]

![](./images/812713654637035521_11.jpg)

(b) calibrated models

Fig. 8. Experimental measurement of the hydration degree of setting and calibrated solid aspect ratios for the detailed model (outer C-S-H layer, level I and cement paste, level II) and the engineering model (hydrate foam, level I).

overestimates the hydration degree of setting in that case ($\alpha_0 \approx 0.15$ predicted for $w/c=0.6$ instead of $\alpha_0 \approx 0.06$). This drawback could be addressed by calibration of the aspect ratio of the micro-crystals.

Engineering model. The setting of the cement paste in the engineering model is ensured by the percolation of the hydrate foam (level I). Assuming that the capillary pores can be described by spherical particles, the best fit is obtained for $\omega_h \approx 0.014$. However, since this aspect ratio is very low, the connectivity of the capillary pores is too strongly hindered if the capillary pores are assumed spherical. To retrieve an appropriate tortuosity of the capillary porosity, the capillary pores have to be considered elongated ($\omega_{cp} > 1$). After calibration to experimental diffusion data (see Section 5.2), the final optimum is found to be $\omega_h=0.013$ and $\omega_{cp}=6$.

The low value of hydrate aspect ratio required to reproduce the setting arises as a consequence of not considering a partition of the capillary porosity across scales as in the engineering model. Indeed, the porosity of the hydrate foam is significantly higher than that of the outer C-S-H layer of the detailed model throughout hydration. From Fig. B.14, this implies that much flatter hydrate particles have to be assumed to retrieve the appropriate percolation porosity. The physical meaning of such a low aspect ratio for the hydrates is arguably questionable. Note that in the initial model of Pichler and Hellmich [48], an infinite aspect ratio has been used to describe the hydrates.

### 4.3. Elastic moduli of the different phases

The elastic moduli of the constituents of the models are summarized in Table 1. All these mechanical properties are considered to be independent of the hydration degree.

Detailed model. Nano-indentation results on LD- and HD-C-S-H by Acker [16], Constantinides and Ulm [39,58] are reported in Fig. 9. Under the assumption of Section 3.1.2 that the aspect ratio of the elementary C-S-H bricks and gels pores are $\omega_{csh}^s=1/\omega_{gp}=0.12$, the properties of the elementary C-S-H bricks are inferred by inverse analysis as in Sanahuja et al. [36] from the measured indentation moduli $M=E/(1-v^2)$ and the commonly assumed value of $v=0.24$ for both LD- and HD-C-S-H gels. The inverse analysis leads to a Young modulus $E_{csh}^s=63$GPa and a Poisson ratio $v_{csh}^s=0.27$ for the elementary C-S-H bricks, which are close to the values obtained by Constantinides and Ulm [58], Sanahuja et al. [36] by inverse analysis. The resulting modeled C-S-H gel indentation moduli are displayed in Fig. 9.

![](./images/812713654637035521_12.jpg)

Fig. 9. Self-consistent estimates of the LD- and HD-C-S-H gel indentation moduli (thick line) and diffusion coefficients (thin line) for several solid and pore aspect ratios $\omega_s=\omega_{csh}^s$ and $\omega_p=\omega_{gp}$, against nano-indentation measurements.

The Young modulus and the Poisson ratio of the anhydrous clinker is taken from nano-indentation tests by Acker [16], Velez et al. [72] as $E_a=135$GPa and $v_a=0.3$. We assume that portlandite is representative of crystalline hydrates. We retain as Haecker et al. [9] $E=42.3$GPa and $v=0.324$ for portlandite based on the measures of Holuj et al. [73], Monteiro and Chang [74].

Engineering model. To estimate the effective moduli of the hydration products for the engineering model, the procedure suggested by Pichler and Hellmich [48] is adapted. The hydrate properties are inferred from the experimental work of Helmuth and Turk [65] on mature cement pastes, for which the hydration degree is assumed equal to the maximum value $\alpha_{max}$ given by (11) since the samples have been covered with added water to ensure saturation during the 6 to 24 months curing. The $w/c$ ratio at casting time is not reported and is inferred from the final total water content to ignited weight ratio $w_t/c_i$ using (12). Numerous data points are available for initial $w/c$ close to 0.4, which is slightly above the critical $w/c$ value of 0.36 (see (11)) above which all the clinker can be hydrated if water is available from an external source. Hence the pastes of Helmuth and Turk [65] with initial $w/c=0.4$ should be close from almost pure hydration products, with a small amount of capillary pores $(f_{cp}(w/c=0.4,\alpha=1)=5.4\%$ and $f_h(w/c=0.4,\alpha=1)=94.6\%$). The reported values by Helmuth and Turk [65] with initial $w/c=0.4$ are a Young's modulus of $E=22.5$GPa and a shear modulus $\mu=8.69$GPa¹. These moduli have been measured on saturated pastes by dynamic measurements and should hence correspond to undrained moduli (see [46,75]). Using the engineering model presented in Section 3.2 and assuming a water bulk modulus of 2.3GPa for the computation of the homogenized undrained moduli, the inverse analysis provides $E_h=25.3$GPa and $v_h=0.29$, which corresponds to $k_h=20.1$GPa and $\mu_h=9.81$GPa.

### 4.4. Diffusion properties of the different phases

The anhydrous cement particles, the micro-sized and the nano-sized crystal hydrates particles and the elementary solid C-S-H particles are assumed impenetrable. The relative contribution of the capillary and gel pores remains to be detailed.

There is a divergence in literature about the value of the diffusion coefficient in capillary pores. In the multi-scale models of [13,17,19], the diffusion coefficient of a species in capillary pores is assumed equal to that of the same species in bulk water. On the other hand, based on an inverse analysis with simplified micromechanics based models, [51,52] have obtained diffusion coefficients in capillary pores 7 to 10 times smaller than in bulk water.

Molecular dynamics (MD) simulations on tobermorites and nuclear magnetic resonance (NMR) measures on cement pastes have evidenced that the diffusive transport in confined pores can be lower than in bulk water. But a distinction must be made between interlayer water, surface water and capillary or bulk water [76]. The auto-diffusion coefficient of interlayer water within the 9 to 14 Å layers of the crystalline structure of tobermorite, a C-S-H analogue, has been evaluated to 1.4 to $6.8 \times 10^{-11} \text{m}^2/\text{s}$ from MD simulations [76-79] and $2.6 \times 10^{-11} \text{m}^2/\text{s}$ from NMR experiments [80], which is about two orders of magnitude smaller than the value for bulk water equal to $2.3 \times 10^{-9} \text{m}^2/\text{s}$. The auto-diffusion coefficient of surface

---
¹ Portland cement 15754 of this reference, cured 7 months, with $w_t/c_i=0.457$.

adsorbed water, located within less than 1 nm to the C-S-H sur-
face, has been estimated from $4.5 \times 10^{-10}$ to $1.2 \times 10^{-9} \mathrm{m}^{2} / \mathrm{s}$
[76,80,79] i.e. 2 to 5 times less than for bulk water. In turn, MD
simulations in 6 nm pores between tobermorite sheets - which
roughly corresponds to the very finest capillary pores according
to the pore classification we have adopted - report auto-
diffusion coefficients of capillary water of $2 \times 10^{-9} \mathrm{m}^{2} / \mathrm{s}$ [76],
which is only slightly below that of bulk water.

For chloride ions associated with the surface, the diffusion coef-
ficient reported by Kalinichev et al. [77] from MD simulations is of
$3.8 \times 10^{-10} \mathrm{m}^{2} / \mathrm{s}$; while in a 6 nm pore, excluding surface, Zehtab
and Tarighat [79] found values ranging from 6.6 to
$7.6 \times 10^{-10} \mathrm{m}^{2} / \mathrm{s}$. A study by Nguyen and Amiri [81] based on the
electrical double layer (EDL) theory indicates that the coefficient
of diffusion of chloride ions can be affected in pores smaller than
2-3 nm, while this effect is negligible for larger pores.

Based on these results, it seems more appropriate to assume
that the diffusion coefficient in most capillary pores is close to that
in bulk solution ($D_{\text{bulk}} = 2.1 \times 10^{-9} \mathrm{m}^{2} / \mathrm{s}$ at $25^{\circ} \mathrm{C}$), and that the
slow-down effect rather takes place in gel pores. For both models,
an inverse analysis is carried out to determine the amount of this
slow-down.

For the engineering model, the diffusion coefficient of the
hydrates is inferred from the experimental data of Yu and Page
[82] obtained on Portland cement pastes. Since these pastes have
been cured from 3 to 9 months in saturated lime water, their
hydration degree is assumed equal to $\alpha_{\text{max}}$ when water is available
from external sources, given by (11). Hence, the paste with initial
ratio $w/c = 0.35$ and measured chloride diffusion coefficient
$1.00 \times 10^{-12} \mathrm{m}^{2} / \mathrm{s}$ should be close to almost pure hydrates. Accord-
ing to (9), this mature paste composition should be
$f_{h}=98.5\%, f_{a}=1.5\%$ and $f_{cp}=0$, from which the hydrate diffu-
sion coefficient $D_{h}$ is obtained by inverse analysis using (6) with
$D_{f}=D_{h}$ since $f_{cp}=0$. This yields $D_{h}=1.05 \times 10^{-12} \mathrm{m}^{2} / \mathrm{s}$, which cor-
responds to $D_{h}=5.04 \times 10^{-4} D_{\text{bulk}}$. The obtained value of chloride
diffusion coefficients for the hydrates is consistent with the value
$D_{h}=2 \times 10^{-12} \mathrm{m}^{2} / \mathrm{s}$ adopted by Walther et al. [13].

Similarly for the detailed model, the diffusion coefficient in gel
pores is obtained by inverse analysis from the same reference [82],
which yields $D_{\text{gp}}=0.0246 D_{\text{bulk}}$. The corresponding HD and LD-C-S-
H diffusion coefficients as upscaled from level 0 are
$D_{\text{hdcsh}}=4.4 \times 10^{-4} D_{\text{bulk}}$ and $D_{\text{ldcsh}}=1.6 \times 10^{-3} D_{\text{bulk}}$. This is consis-
tent with the order of magnitude of the C-S-H gel chloride diffusion
coefficient $D_{\text{csh}}=2.5 \times 10^{-3} D_{\text{bulk}}$ adopted by Garboczi and Bentz
[8] for numerical simulations, or for the tritiated water diffusion
coefficient found by inverse analysis by Bary and Béjaoui [17]
($D_{\text{hdcsh}}=3.7 \times 10^{-4} D_{\text{bulk}}$ and $D_{\text{ldcsh}}=1.5 \times 10^{-3} D_{\text{bulk}}$).

## 5. Results and discussion

The two models developed in Section 3 and 4 are assessed
against experimental results from the literature on the effective
coefficient of diffusion and the elastic moduli.

### 5.1. Young's modulus during hydration and at long-term

Mature paste The models are compared in Fig. 10 to experimen-
tal results from Helmuth and Turk [65] on fully hydrated pastes.
The experimental Young's and shear modulus have been deter-
mined from flexural and torsional natural frequencies measures
on thin slabs specimens. The range of $w/c$ is from 0.3 to 0.8 and
the paste samples were aged from 6 to 24 months. The experimen-
tal data reported by Helmuth and Turk [65] are given as a function
of the total water content to the ignited weight ratio $w_{t}/c_{i}$ at a late
stage of hydration. As explained in Section 4.1.1, the initial water to
cement ratio $w/c$ is deduced from $w_{t}/c_{i}$ by (12). Accordingly, the
degree of hydration used for the models in Fig. 10 corresponds to
the maximum value when external water is available, calculated
from (11). Fig. 10 also features a resonance frequency measure of
the Young's modulus by Ulm et al. [40] on a cement paste with
$w/c=0.5$ cured in water during 5 months.

The engineering model is in a good agreement with the exper-
imental data of Helmuth and Turk [65]. For this model the hydrate
moduli have been inferred from the same reference, but for
$w/c=0.4$ only. The detailed model provides a fair agreement with
the data of Helmuth and Turk [65] for $w/c>0.4$, but overestimates
these measures for low $w/c$ values. This discrepancy at low $w/c$
could be attributed to an overestimation of the actual hydration
degree by the ultimate value (11), or to an underestimation of
the ratio of LD-C-S-H to total C-S-H at low $w/c$ by relation (13).

![](./images/812713654637035521_13.jpg)

![](./images/812713654637035521_14.jpg)

Fig. 10. Assessment of modeled elastic moduli against experimental data on mature cement pastes by Helmuth and Turk [65] and Ulm et al. [40]. Thin full line: drained moduli for the detailed model.

![](./images/812713654637035521_15.jpg)

Fig. 11. Young's modulus during hydration estimated by model and experimental values by Haecker et al. [9] and Boumiz et al. [67]. Thin full line: drained moduli for the detailed model.

Hydrating paste. Next, the models are assessed in Fig. 11 against experimental data on the Young's modulus during hydration, at early age [67] using ultrasound pulse velocity and at later age [9] using a resonance frequency method.

The agreement with the data of Boumiz et al. [67] is satisfactory at early age for w/c ranging from 0.3 to 0.6, in particular for the detailed model.

However, at later age both models underestimate the Young's modulus measured by Haecker et al. [9], Ulm et al. [40], in particular for larger w/c ratios. Note that for a similar w/c ratio there is a divergence in the Young's modulus measured by [9,40] on one side and Helmuth and Turk [65] on the other side. An acknowledged limitation of the present models is their inability to reproduce these differences since the simple hydration model on which they rely does not take into account the precise cement composition.

Note that the experimental results used in Figs. 10 and 11 have been obtained from dynamic methods (ultrasound pulse velocity or resonance frequency) on water saturated samples. Given the high-frequency and the low permeability of cement paste, it is unlikely that the pore fluid pressures induced by these measurements can be dissipated by water escaping the sample. Hence the conditions can be assumed to be undrained. In Figs. 10 and 11, the model results hence correspond to undrained moduli issued from poromechanics (see [6,17,46,36,75]). At each scale, the homogenized undrained bulk modulus $k_{\text{hom}}^{\text{u}}$ and shear modulus $\mu_{\text{hom}}^{\text{u}}$ are deduced from the drained ones $k_{\text{hom}}$ and $\mu_{\text{hom}}$ - which are computed as described in Section 3 and Appendix A - by:

$$
k_{\text{hom}}^{\text{u}}=k_{\text{hom}}+Mb^{2} \quad ; \quad \mu_{\text{hom}}^{\text{u}}=\mu_{\text{hom}} \tag{19}
$$

where $b$ is the Biot coefficient and $M$ the Biot modulus [6]. When the solid phase is homogeneous with bulk modulus $k_{s}$, these poroelastic parameters are given by [6]:

$$
b=1-\frac{k_{\text{hom}}^{\text{d}}}{k_{s}} \quad ; \quad \frac{1}{M}=\frac{b-\phi}{k_{s}}+\frac{\phi}{k_{f}} \tag{20}
$$

where $\phi$ is the porosity at this scale and $k_{f}=2.3$GPa is the water bulk modulus.

### 5.2. Diffusion coefficient of cement paste

The ability of the models to reproduce the diffusion coefficient of chloride ions into Ordinary Portland Cement (OPC) pastes is then assessed against experimental data. An experimental database on the chloride diffusion coefficient of mature OPC paste is constituted from 12 literature references, featuring 70 data points (see Table 2) with w/c ratios ranging from 0.23 to 0.8. The effective coefficients of diffusion obtained experimentally are shown on Fig. 12 and scaled by the diffusion coefficient of chloride ions in bulk water $D_{\text{bulk}}=2.1 \times 10^{-9}$ at $25^{\circ} \mathrm{C}$ [83]. The experimental data exhibits an important scatter which may mainly be attributed to the curing conditions and the type of measurement (steady-state or non steady-state natural diffusion, or steady state migration). Since the experimental database encompasses various curing conditions (see Table 2), the models are represented both at $\alpha=\alpha_{\max }$ given by (11) and $\alpha=80 \% \alpha_{\max }$ to be representative of experimental conditions. Due to the two regimes for the ultimate hydration degree in the model of Powers and Brownyard [14] (see (11)), both models exhibit a break in curvature at the critical water to cement ratio $w/c=0.36$. This feature is a modeling artifact which is not supported by experimental data and could be overcome by resorting to a more detailed hydration model.

As explained in Section 4.2, the engineering model would strongly underestimate the diffusion coefficient at larger w/c ratios if the capillary pores were assumed spherical. This is a consequence of the very low aspect ratio of the spheroids used to model the hydrates, which hinders the capillary pore connectivity. To overcome this drawback, the aspect ratio of the capillary pores in the engineering model is calibrated to $\omega_{cp}=6$ based on the experimental data reported in Table 2. This fitting step is acknowledged as a limitation of the engineering model.

On the contrary, the detailed model is in good agreement with the experimental results from the literature (see Fig. 12), without any morphological adjustment. This asset of the detailed model over the engineering model likely lies in a finer description of the pore network into three types (gel, small and large capillary pores).

Finally, both models are assessed against experimental data during hydration. Due to the long characteristic time involved in the classical steady-state experiments, few experimental data are available on the diffusion coefficient on non-mature pastes. Caré [91] measured a hydration degree of $81 \%$ and a chloride diffusion coefficient of $D=5.65 \times 10^{-12} \mathrm{~m}^{2} / \mathrm{s}$ for $w/c=0.45$, where the detailed model predicts $D=5.59 \times 10^{-12} \mathrm{~m}^{2} / \mathrm{s}$ and the engineering model $D=6.78 \times 10^{-12} \mathrm{~m}^{2} / \mathrm{s}$. Using an electrically accelerated test procedure, Halamickova et al. [95] report diffusion

<table><caption>Table 2 Reference experimental measurements of the chloride diffusion coefficient in ordinary Portland cement pastes (average and [min–max] are provided when several values are available).</caption>
<thead>
<tr>
<th>Ref.</th>
<th>abr.</th>
<th>w/c</th>
<th>$D_{Cl^-}$ ($10^{-12}$m²/s)</th>
<th>T(°C)</th>
<th>curing conditions</th>
</tr>
</thead>
<tbody>
<tr>
<td>Page et al. [84]</td>
<td>P81</td>
<td>0.40</td>
<td>2.60 [1.99–2.96]</td>
<td>25</td>
<td>60 days in saturated Ca(OH)₂ sol.</td>
</tr>
<tr>
<td></td>
<td></td>
<td>0.50</td>
<td>4.47 [4.06–4.82]</td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td>0.60</td>
<td>12.4 [11.0–15.6]</td>
<td></td>
<td></td>
</tr>
<tr>
<td>Yu and Page [82]</td>
<td>Y91</td>
<td>0.35</td>
<td>1.00</td>
<td>25</td>
<td>3 to 9 months in saturated Ca(OH)₂ sol.</td>
</tr>
<tr>
<td></td>
<td></td>
<td>0.50</td>
<td>5.45</td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td>0.60</td>
<td>7.28</td>
<td></td>
<td></td>
</tr>
<tr>
<td>Ngala et al. [85]</td>
<td>N95</td>
<td>0.40</td>
<td>3.95 [3.65–4.35]</td>
<td>25</td>
<td>10 weeks in 0.035 mol NaOH sol.</td>
</tr>
<tr>
<td></td>
<td></td>
<td>0.50</td>
<td>7.80 [7.16–8.06]</td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td>0.60</td>
<td>12.6 [10.4–13.8]</td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td>0.70</td>
<td>21.5 [19.7–24.4]</td>
<td></td>
<td></td>
</tr>
<tr>
<td>Ngala and Page [86]</td>
<td>N97</td>
<td>0.40</td>
<td>4.06</td>
<td>25</td>
<td>10 weeks in 0.035 mol NaOH solution</td>
</tr>
<tr>
<td></td>
<td></td>
<td>0.50</td>
<td>7.84</td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td>0.60</td>
<td>12.7</td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td>0.70</td>
<td>21.4</td>
<td></td>
<td></td>
</tr>
<tr>
<td>Tang and Nilsson [87]</td>
<td>T93</td>
<td>0.40</td>
<td>2.9</td>
<td>–</td>
<td>–</td>
</tr>
<tr>
<td></td>
<td></td>
<td>0.60</td>
<td>9.4</td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td>0.80</td>
<td>21</td>
<td></td>
<td></td>
</tr>
<tr>
<td>MacDonald and Northwood [88]</td>
<td>Mc95</td>
<td>0.40</td>
<td>2.56 [2.35–2.78]</td>
<td>23</td>
<td>8 weeks at 100% of R.H.,</td>
</tr>
<tr>
<td></td>
<td></td>
<td>0.50</td>
<td>6.81 [6.41–7.28]</td>
<td></td>
<td>no saturation before testing</td>
</tr>
<tr>
<td></td>
<td></td>
<td>0.60</td>
<td>12.9 [12.3–13.8]</td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td>0.70</td>
<td>20.4 [17.7–21.9]</td>
<td></td>
<td></td>
</tr>
<tr>
<td>Castellote et al. [89]</td>
<td>C01</td>
<td>0.40</td>
<td>3.65</td>
<td>25</td>
<td>1 month in water +1 month in saturated Ca(OH)₂ sol.</td>
</tr>
<tr>
<td>Hornain et al. [90]</td>
<td>H95</td>
<td>0.55</td>
<td>11.3</td>
<td>20</td>
<td>60 days in water +6 days in saturated Ca(OH)₂ sol.</td>
</tr>
<tr>
<td>Caré [91]</td>
<td>C03</td>
<td>0.45</td>
<td>5.65</td>
<td>21</td>
<td>1 month at 45°C sealed with aluminum sheet,</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>vacuum saturation in alkaline solution before testing</td>
</tr>
<tr>
<td>Huang et al. [92]</td>
<td>H10</td>
<td>0.40</td>
<td>5.42</td>
<td>–</td>
<td>–</td>
</tr>
<tr>
<td></td>
<td></td>
<td>0.50</td>
<td>8.24</td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td>0.60</td>
<td>12.0</td>
<td></td>
<td></td>
</tr>
<tr>
<td>Sun et al. [93]</td>
<td>S11</td>
<td>0.23</td>
<td>1.03</td>
<td>25</td>
<td>60 days at &gt;95% of R.H.,</td>
</tr>
<tr>
<td></td>
<td></td>
<td>0.35</td>
<td>4.12</td>
<td></td>
<td>48 h vacuum water saturation before testing</td>
</tr>
<tr>
<td></td>
<td></td>
<td>0.53</td>
<td>10.6</td>
<td></td>
<td></td>
</tr>
<tr>
<td>Princigallo [94]</td>
<td>P12</td>
<td>0.27</td>
<td>0.95</td>
<td>23</td>
<td>420 days in 90% saturated NaCl sol.</td>
</tr>
<tr>
<td></td>
<td></td>
<td>0.30</td>
<td>1.38</td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td>0.33</td>
<td>1.51</td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

![](./images/812713654637035521_16.jpg)

Fig. 12. Chloride diffusivity as a function of water to cement ratio for a maximum degree of hydration: comparison to experimental data (see Table 2).

![](./images/812713654637035521_17.jpg)

Fig. 13. Chloride diffusivity during hydration as a function of water to cement ratio and experimental data by Halamickova et al. [95].

coefficients of OPC for $w/c=0.4$ and 0.5 and hydration degrees in the range $\alpha=0.45$ to 0.60. The difference in hydration degrees measured before and after the accelerated test, which lasts 24 to 48 h, is of 0.01. As illustrated in Fig. 13, the detailed model is in excellent agreement with these measures while the engineering model predicts a too early decrease of the diffusion coefficient during hydration. Although one should be cautious due to the scatter in experimental measurements of diffusion coefficients, the better performance of the detailed model is attributed to a finer representation of the pore space across the scales.

### 5.3. Discussion

An acknowledged limitation of the present multi-scale strat- egy is that microscale parameters difficult to obtain by direct experiments have been determined by inverse analysis. The

inferred values of the microscale parameters are inherently dependent on the model from which they are obtained. As such, they should be used with caution in other contexts. This remark likely holds for earlier models such as the diffusion coefficients in capillary pore adopted in Pivonka et al. [51], Damrong- wiriyanupap et al. [52], the diffusion coefficients at the C-S-H scale found by Bary and Béjaoui [17], Stora et al. [19], the solid C-S-H particles elastic moduli and C-S-H platelets aspect ratios in Sanahuja et al. [36], among others. For the present engineering model, this concerns the aspect ratios adopted for the hydrates and the capillary pores at level I. For the detailed model, the dif- fusion coefficient adopted in the gel pores, the elastic moduli of the solid C-S-H particles at level 0 as well as the aspect ratio of the gel pores and the LD-C-S-H gel particles at level Ia are likely dependent on the adopted representation of the microstructure. In particular, the coefficient of diffusion of chloride ions in gel pores obtained by inverse analysis from the present detailed model, equal to $5.3 \times 10^{-11} \mathrm{~m}^{2} / \mathrm{s}$, corresponds to the order of magnitude of the interlayer diffusion coefficients rather than that of near surface ones (see Section 4.4). This raises concerns on the validity of the representation of C-S-H gel as a mix of impervious solid bricks and gel pores adopted in the detailed model, which is likely still too simplistic with regards to the variety of shapes that C-S-H may exhibit [59].

However, the two models of microstructures considered in this paper have successfully passed the tests of elasticity and chloride diffusivity. To gain further confidence in them, additional tests would be their application to the diffusion of other species and to other physical properties such as the electrical conductivity or the permeability.

Future developments of the detailed model should rely on a more sophisticated hydration model in order to refine the dis- tinction between the different types of hydrates and to model blended cements, as recently investigated by Lavergne et al. [96]. This distinction would allow to tackle the effect of patholo- gies of cement paste such as leaching or carbonation on its effec- tive properties. In addition the chloride binding effect is not considered in the diffusivity problem. The chemical absorption of chloride ions by the formation of Friedel's and Kuzel's salt could also affect at long term the diffusion coefficient of cement paste.

## 6. Conclusion

A new paradigm to multiscale modelling is proposed in this work: instead of a model dedicated to the estimation of a single material property, we endeavoured to develop a unified multiscale model of both stiffness and diffusion coefficient of Portland cement paste based on the same microstructure description via a hierarchy of Eshelby-based homogenization schemes.

Such paradigm entails several assets. First assumptions on microstructure description have to be realistic from both the point of view of the pore network and of the solid skeleton, which is here made possible thanks to the ability of the self-consistent scheme to handle bi-continuity of the pore and solid phase. Second, microstructure parameters necessary to describe the morphology across the scales and the development of hydration are shared for the estimation of several material properties, which allows to cut down the number of model parameters required to bridge the gap between the macroscopic properties of cement and the physical chemistry of its hydration.

Two versions of the model have been developed: a detailed one and a simplified, engineering one. The two of them can suc- cessfully estimate both chloride diffusivity and elastic moduli of ordinary Portland cement paste during hydration as well as ulti- mate values for a wide range of water to cement ratio. The key to the detailed model is the consideration of three types of pores (gel, small and large capillary pores) at three scales to finely describe the connectivity of the pore network and the percolation of the solid phase. In turn the pragmatic engineering model relies on a very limited set of microstructure parameters and its out- puts can be computed efficiently. The two models perform simi- larly against experimental databases on diffusion and stiffness, except on the chloride diffusion properties at intermediate hydra- tion stages, where the detailed model provides a better agree- ment with experimental observations than the engineering model. Their ability to be transposed to the estimation of other physical properties such as resistivity, permeability and strength is an interesting prospect which remains to be assessed.

## Declaration of Competing Interest

The authors declare that they have no known competing finan- cial interests or personal relationships that could have appeared to influence the work reported in this paper.

## Acknowledgements

Financial support from the French National Research Agency (ANR) under the MODEVIE project is gratefully acknowledged.

## Appendix A. Self-consistent estimate of the diffusion and stiffness of a porous material with spheroidal particle shapes

### A.1. Diffusion

Basis. In what follows, it is convenient to introduce a basis $(\boldsymbol{E}_{1}(\boldsymbol{n}), \boldsymbol{E}_{2}(\boldsymbol{n}))$ for transverse isotropic symmetric second order tensor w.r.t. a direction given by a unit vector $\boldsymbol{n}$:
$$\boldsymbol{E}_{1}(\boldsymbol{n})=\boldsymbol{n} \otimes \boldsymbol{n} \quad ; \quad \boldsymbol{E}_{2}(\boldsymbol{n})=\boldsymbol{1}-\boldsymbol{n} \otimes \boldsymbol{n} \tag{A.1}$$
where $\boldsymbol{1}$ is the second order identity tensor. The tensors $\boldsymbol{n} \otimes \boldsymbol{n}$ and $\boldsymbol{1}-\boldsymbol{n} \otimes \boldsymbol{n}$ are orthogonal and idempotent for the dot product.

Eshelby tensor. Next, we consider a spheroidal inclusion in an isotropic matrix, and denote $\omega$ its aspect ratio (axial length divided by transverse length) and $\boldsymbol{n}$ the unit vector indicating the direction of its axis of revolution. For diffusion problems, the Eshelby tensor of such a spheroid can be expressed in the basis $(\boldsymbol{E}_{1}(\boldsymbol{n}), \boldsymbol{E}_{2}(\boldsymbol{n}))$ as:
$$\boldsymbol{S}(\boldsymbol{n}, \omega)=S_{1}(\omega) \boldsymbol{E}_{1}(\boldsymbol{n})+S_{2}(\omega) \boldsymbol{E}_{2}(\boldsymbol{n})$$
$$\text{with } \begin{cases}
S_{1}(\omega) & =1-2 S_{2}(\omega) \\
S_{2}(\omega) & =\frac{\omega^{2}}{\omega^{2}-1} \frac{1-g(\omega)}{2}
\end{cases} \tag{A.2}$$
where
$$g(\omega)=
\begin{cases}
\frac{\operatorname{arccosh}(\omega)}{\omega \sqrt{\omega^{2}-1}} & \text{ if } \omega>1 \text{ (prolate)} \\
\frac{\operatorname{arccos}(\omega)}{\omega \sqrt{1-\omega^{2}}} & \text{ if } \omega<1 \text{ (oblate)}
\end{cases} \tag{A.3}$$

Self-consistent estimate. We consider a two phase material with isotropic diffusion coefficients $D_{1}$ and $D_{2}$ and volume fractions $f_{1}+f_{2}=1$. The particles of each phase $i$ are modeled as spheroids of aspect ratios $\omega_{i}$. An isotropic distribution of spheroid orientation is assumed for both phases. In that case, the self-consistent esti- mate $D_{sc}$ of the effective diffusion coefficient is isotropic and owing to the properties of the basis $(\boldsymbol{E}_{1}, \boldsymbol{E}_{2})$, the transposition of (4) to dif- fusion problems amounts to:
$$\sum_{i=1}^{2} f_{i}\left(D_{i}-D_{s c}\right) \sum_{c=1}^{2}\left[\left(D_{s c}+S_{c}\left(\omega_{i}\right)\left[D_{i}-D_{s c}\right]\right)^{-1} \overline{\boldsymbol{E}_{c}(\boldsymbol{n})}\right]=0 \tag{A.4}$$

where $\bullet$ denotes the averaging operation over all orientations of $\boldsymbol{n}$.
For an isotropic distribution of orientations:
$$\overline{\boldsymbol{E}_{c}(\boldsymbol{n})}=m_{c} \boldsymbol{1} \quad \text{with} \quad m_{c}=c / 3 \quad(c=1,2) \tag{A.5}$$

The tensorial Eq. (A.4) can be projected on the direction $\boldsymbol{1}$ and reduces to the single scalar equation:
$$\sum_{i=1}^{2} f_{i}\left(D_{i}-D_{s c}\right) \sum_{c=1}^{2} m_{c}\left(D_{s c}+S_{c}\left(\omega_{i}\right)\right)\left[D_{i}-D_{s c}\right]^{-1}=0 \tag{A.6}$$

After rearrangement, (A.6) leads in the general case to a quartic polynomial in $D_{s c}$:
$$a D_{s c}^{4}+b D_{s c}^{3}+c D_{s c}^{2}+d D_{s c}+e=0 \tag{A.7}$$
which can be solved using Cardano's method as follows:
$$
\begin{aligned}
& p=\frac{8 a c-3 b^{2}}{8 a^{2}} \quad ; \quad q=\frac{b^{3}-4 a b c+8 a^{2} d}{8 a^{3}} \\
& \Delta_{1}=2 c^{3}-9 b c d+27 b^{2} e+27 a d^{2}-72 a c e \\
& \Delta_{0}=c^{2}-3 b d+12 a e \quad ; \quad \Phi=\arccos \left(\frac{\Delta_{1}}{2 \sqrt{\Delta_{0}^{3}}}\right) \\
& S=\frac{\operatorname{sign}(q)}{2} \sqrt{-\frac{2}{3} p+\frac{2}{3 a} \sqrt{\Delta_{0}} \cos (\Phi / 3)} \\
& D_{s c}=\frac{-b}{4 a}-S+\sqrt{S^{2}-\frac{p}{2}+\frac{q}{4 S}}
\end{aligned} \tag{A.8}
$$

### A.2. Elasticity
Walpole basis. Any transverse isotropic fourth order tensor $\mathbb{L}$ w.r. t. a direction given by a unit vector $\boldsymbol{n}$, with minor symmetries, can be decomposed in Walpole basis $\left(\mathbb{E}_{c}(\boldsymbol{n})\right)_{c=1, \ldots, 6}$ as $\mathbb{L}=\sum_{c=1}^{6} L_{c} \mathbb{E}_{c}(\boldsymbol{n})$ (see e.g. [18]). For example, the components in Walpole basis of the fourth order identity tensor $\mathbb{I}$, the spherical projector $\mathbb{J}$ and the deviatoric projector $\mathbb{K}$ are:
$$
\begin{aligned}
& \mathbb{I}=[1,1,1,1,0,0]^{W} \quad ; \\
& \mathbb{J}=[2 / 3,1 / 3,0,0,1 / 3,1 / 3]^{W} \\
& \mathbb{K}=[1 / 3,2 / 3,1,1,-1 / 3,-1 / 3]^{W}
\end{aligned} \tag{A.9}
$$

The tensors $\mathbb{J}$ and $\mathbb{K}$ are orthogonal and idempotent for the double contraction product.

The double contraction product and the inverse are expressed on the components in Walpole basis as:
$$
\begin{aligned}
\mathbb{L}: \mathbb{M}= & {\left[L_{1} M_{1}+2 L_{6} M_{5}, L_{2} M_{2}+2 L_{5} M_{6}, L_{3} M_{3},\right.} \\
& \left.L_{4} M_{4}, L_{5} M_{1}+L_{2} M_{5}, L_{6} M_{2}+L_{1} M_{6}\right]^{W} \\
\mathbb{L}^{-1}= & {\left[\frac{L_{2}}{\Delta}, \frac{L_{1}}{\Delta}, \frac{1}{L_{3}}, \frac{1}{L_{4}},-\frac{L_{5}}{\Delta},-\frac{L_{6}}{\Delta}\right]^{W} }
\end{aligned} \tag{A.10}
$$
with $\Delta=L_{1} L_{2}-2 L_{5} L_{6}$

For an isotropic distribution of orientations $\boldsymbol{n}$, the averages over all orientations $\boldsymbol{n}$ of the tensors of Walpole basis are isotropic and given by:
$$
\begin{aligned}
& \overline{\mathbb{E}_{c}(\boldsymbol{n})}=a_{c} \mathbb{J}+b_{c} \mathbb{K} \quad(c=1, \ldots, 6) \\
& a_{1}=2 a_{2}=a_{5}=a_{6}=\frac{2}{3} \quad ; \\
& a_{3}=a_{4}=0 \\
& b_{2}=2 b_{1}=-b_{5}=-b_{6}=\frac{2}{15} \quad ; \quad b_{3}=b_{4}=\frac{2}{5}
\end{aligned} \tag{A.11}
$$

Eshelby tensor. The Eshelby tensor $\mathbb{S}_{0}(\boldsymbol{n}, \omega)$ of a spheroidal inclusion of aspect ratio $\omega$ and axis orientated along $\boldsymbol{n}$, in an isotropic matrix of Poisson's ratio $v_{0}$ is transverse isotropic. Its components $\left[S_{0, c}(\omega)\right]_{c=1, \ldots, 6}$ in Walpole basis are expressed as a function of $S_{0, c}^{\prime}(\omega)=\left(1-v_{0}\right) S_{0, c}(\omega)$ which is given by:
$$
\begin{aligned}
S_{0}^{\prime}(\omega)= & {\left[F_{0}+2 F_{1},\left(1-v_{0}\right)\left(1-2 F_{0}\right)+4 F_{1},\right.} \\
& \left(3 / 2-2 v_{0}\right) F_{0}+F_{1},\left(1-v_{0}\right)\left(1-F_{0}\right)-4 F_{1}, \\
& \left.v_{0}\left(1-2 F_{0}\right)-2 F_{1}, v_{0} F_{0}-2 F_{1}\right]^{W}
\end{aligned} \tag{A.12}
$$
where, with the notation introduced in (A.3):
$$
\begin{aligned}
& F_{0}(\omega)=\frac{\omega^{2}[1-g(\omega)]}{2\left(\omega^{2}-1\right)} \quad ; \\
& F_{1}(\omega)=\frac{\omega^{2}\left[\left(2 \omega^{2}+1\right) g(\omega)-3\right]}{8\left(\omega^{2}-1\right)^{2}}
\end{aligned} \tag{A.13}
$$

Self-consistent estimate. We consider a two phase material with isotropic stiffness tensors $\mathbb{C}_{i}=3 k_{i} \mathbb{J}+2 \mu_{i} \mathbb{K}$ and volume fractions $f_{i}$. The particles of each phase $i$ are modeled as spheroids of aspect ratios $\omega_{i}$ and their distribution of orientation is isotropic. The self-consistent estimate $\mathbb{C}_{s c}$ of the effective diffusion coefficient is then isotropic and admits the decomposition $\mathbb{C}_{s c}=3 k_{s c} \mathbb{J}+2 \mu_{s c} \mathbb{K}$. By application of (A.11), the tensorial Eq. (4) can be projected onto the basis $(\mathbb{J}, \mathbb{K})$, and the self-consistent estimate of the effective moduli is the positive solution to the coupled system:
$$
\left\{\begin{array}{l}
\sum_{i=1}^{2} f_{i}\left(k_{i}-k_{s c}\right) \sum_{c=1}^{6} a_{c} A_{s c, c}^{i}=0 \\
\sum_{i=1}^{2} f_{i}\left(\mu_{i}-\mu_{s c}\right) \sum_{c=1}^{6} b_{c} A_{s c, c}^{i}=0
\end{array} \tag{A.14}\right.
$$
where $A_{s c, c}^{i}$ are the components in Walpole basis of the inverse of $\mathbb{I}+\mathbb{S}_{s c}\left(\boldsymbol{n}, \omega_{i}\right):\left(\frac{k_{i}}{k_{s c}} \mathbb{J}+\frac{\mu_{i}}{\mu_{s c}} \mathbb{K}-\mathbb{I}\right)$. These components, which are independent of $\boldsymbol{n}$, can be readily determined from (A.9), (A.10) and (A.12).

## Appendix B. Self-consistent approach to the percolation of a porous medium in both diffusion and elasticity

Let us consider a two-phase material comprising a pore space with zero stiffness and a solid phase with zero diffusion coefficient. The shapes of the solid particles and of the pores are accounted for by spheroids of aspects ratios $\omega_{s}$ and $\omega_{p}$. The aspect ratio $\omega$ here denotes the ratio of the axial to the transverse radii of the spheroids, so that $\omega>1$ corresponds to a prolate (elongated) particle, $\omega<1$ to an oblate (flat) particle and $\omega=1$ to a sphere. For each phase, we consider the case of an isotropic distribution of the orientation of the spheroids.

The resolution of (4) in the elastic case (see Appendix A.2) indicates that there is a so-called (elastic) percolation porosity $\phi_{e}$ above which the self-consistent estimate of the homogenized stiffness is zero. Similarly in diffusion problems (see Appendix A.1), there is a (diffusion) percolation porosity $\phi_{d}$ below which the self-consistent estimate of the homogenized diffusion coefficient is zero. The percolation porosity $\phi_{e}$ is representative of the solid phase connectivity, while $\phi_{d}$ is representative of the pore phase connectivity. These two percolation porosities are reported in Fig. B.14. Since $\phi_{d}<\phi_{e}$, bi-continuity of the solid and pore phases is accounted for in the porosity range $] \phi_{d}, \phi_{e}[$ [33]. At fixed solid aspect ratio, Fig. B.14a indicates that the pore connectivity increases with the elongation or the flattening of the pores; spherical pores lead to the poorest pore connectivity. There is an asymmetry in the effect of the shape of the solid phase on the pore connectivity: flat solid particles hinder fluid transport much more effectively than elongated ones. In turn, Fig. B.14b indicates that the solid phase connectivity follows the opposite trend: flat or elongated solid particles lead to a better solid connectivity than

![](./images/812713654637035521_18.jpg)

![](./images/812713654637035521_19.jpg)

Fig. B.14. Percolation porosities of the self-consistent estimates for a material comprising a non-diffusive solid and a diffusive pore space, as a function of the aspects ratio $\omega_s$ and $\omega_p$ of the spheroids representing the solid particles and pores: (a) diffusion percolation porosity $\phi_d$ (b) elastic percolation porosity $\phi_e$.

spherical ones, and flat pores reduce much more solid connectivity than elongated pores. However one should take care that $\phi_d \neq 1 - \phi_e$ upon phase interchange.

### References

[1] A. Ait-Mokhtar, O. Millet, Structure Design and Degradation Mechanisms in Coastal Environments, Wiley, 2015.

[2] O. Bernard, F.J. Ulm, E. Lemarchand, A multiscale micromechanics-hydration model for the early-age elastic properties of cement-based materials, Cem. Concr. Res. 33 (9) (2003) 1293-1309.

[3] H. Ma, D. Hou, Y. Lu, Z. Li, Two-scale modeling of the capillary network in hydrated cement paste, Constr. Build. Mater. 64 (2014) 11-21.

[4] A. Buchwald, Determination of the ion diffusion coefficient in moisture and salt loaded masonry materials by impedance spectroscopy, in: 3rd International Symposium Vienna, 475-482, 2000..

[5] T.C. Powers, Fundamental aspects of shrinkage of concrete, Revue des Matériaux 544 (1961) 79-85.

[6] L. Dormieux, D. Kondo, F.-J. Ulm, Microporomechanics, Wiley, 2006.

[7] D. Bentz, E. Garboczi, A digitized simulation model for microstructural development, Ceram. Trans. 16 (1991) 211-226.

[8] E.J. Garboczi, D.P. Bentz, Computer simulation of the diffusivity of cement- based materials, J. Mater. Sci. 27 (8) (1992) 2083-2092.

[9] C.J. Haecker, E.J. Garboczi, J.W. Bullard, R.B. Bohn, Z. Sun, S.P. Shah, T. Voigt, Modeling the linear elastic properties of Portland cement paste, Cem. Concr. Res. 35 (10) (2005) 1948-1960.

[10] K. van Breugel, Numerical simulation of hydration and microstructural development in hardening cement paste (I): theory, Cem. Concr. Res. 25 (1995) 319-331.

[11] L. Liu, W. Sun, G. Ye, H. Chen, Z. Qian, Estimation of the ionic diffusivity of virtual cement paste by random walk algorithm, Constr. Build. Mater. 28 (1) (2012) 405-413.

[12] H. Ma, D. Hou, Z. Li, Two-scale modeling of transport properties of cement paste: Formation factor, electrical conductivity and chloride diffusivity, Comput. Mater. Sci. 110 (2015) 270-280.

[13] E. Walther, M. Bogdan, R. Bennacer, C.D. Sa, Cement paste morphologies and effective diffusivity: using the Lattice Boltzmann method, Eur. J. Environ. Civil Eng. 20 (6) (2016) 667-679.

[14] T.C. Powers, T.L. Brownyard, Studies of the physical properties of hardened Portland cement paste, vol. 43, J. Am. Concr. Inst. (1947).

[15] A. Zaoui, Continuum micromechanics survey, J. Eng. Mech. 128 (8) (2002) 806-816.

[16] P. Acker, Micromechanical analysis of creep and shrinkage mechanisms, in: Z. B.F.-J. Ulm, F. Wittman (Eds.), Creep, shrinkage and durability mechanics of concrete and other quasi-brittle materials. 6th international conference concreep MIT, 15-26, 2001..

[17] B. Bary, S. Béjaoui, Assessment of diffusive and mechanical properties of hardened cement pastes using a multi-coated sphere assemblage model, Cem. Concr. Res. 36 (2006) 245-258.

[18] V. Buryachenko, Micromechanics of heterogeneous materials, Springer, US, 2007.

[19] E. Stora, B. Bary, Q.-C. He, On estimating the effective diffusive properties of hardened cement pastes, Transp. Porous Med. 73 (2008) 279-295.

[20] J. Eshelby, The determination of the elastic field of an ellipsoidal inclusion, Proc. R. Soc. Lond. 241 (1957) 376-392.

[21] S. Torquato, Random Heterogeneous Materials, Springer, New-York, 2002.

[22] J.-F. Barthélémy, Effective permeability of media with a dense network of long and micro fractures, Transp. Porous Media 76 (2009) 153-178.

[23] T. Mori, K. Tanaka, Average stress in matrix and average elastic energy of materials with misfitting inclusions, Acta Metall. 21 (5) (1973) 1605-1609.

[24] Y. Benveniste, A new approach to the application of Mori-Tanaka's theory in composite materials, Mech. Mater. 6 (1987) 147-157.

[25] A. Norris, A differential scheme for the effective moduli of composites, Mech. Mater. 4 (1985) 1-16.

[26] P. Ponte Castañeda, J.R. Willis, The effect of spatial distribution on the effective behavior of composite materials and cracked media, J. Mech. Phys. Solids 43 (12) (1995) 1919-1951.

[27] Q.-S. Zheng, D.-X. Du, An explicit and universal applicable estimate for the effective properties of multiphase composites which accounts for inclusion distribution, J. Mech. Phys. Solids 49 (2001) 2765-2788.

[28] R. Hill, A self-consistent mechanics of composite materials, J. Mech. Phys. Solids 13 (4) (1965) 213-222.

[29] B. Budiansky, On the elastic moduli of some heterogeneous materials, J. Mech. Phys. Solids 13 (1965) 223-227.

[30] J. Lin, W. Zhang, H. Chen, R. Zhang, L. Liu, Effect of pore characteristic on the percolation threshold and diffusivity of porous media comprising overlapping concave-shaped pores, Int. J. Heat Mass Transf. 138 (2019) 1333-1345.

[31] J. Lin, H. Chen, Measurement of continuum percolation properties of two- dimensional particulate systems comprising congruent and binary superellipses, Powder Technol. 347 (2019) 17-26.

[32] J. Lin, H. Chen, W. Xu, Geometrical percolation threshold of congruent cuboidlike particles in overlapping particle systems, Phys. Rev. E 98 (2018) 012134.

[33] A.G. Hunt, M. Sahimi, Transport Flow, Reaction in porous media: percolation scaling, critical-path analysis, and effective medium approximation, Rev. Geophys. 55 (4) (2017) 993-1078.

[34] J.-F. Thovert, V.V. Mourzenko, P.M. Adler, Percolation in three-dimensional fracture networks for arbitrary size and shape distributions, Phys. Rev. E 95 (2017) 042112.

[35] K. Meeks, J. Tencer, M.L. Pantoya, Percolation of binary disk systems: modeling and theory, Phys. Rev. E 95 (2017) 012118.

[36] J. Sanahuja, L. Dormieux, G. Chanvillard, Modelling elasticity of a hydrating cement paste, Cem. Concr. Res. 37 (10) (2007) 1427-1439.

[37] E. Hervé, A. Zaoui, n-layered inclusion-based micromechanical modelling, Int. J. Eng. Sci. 31 (1993) 1-10.

[38] T. Miloh, Y. Benveniste, A generalized self-consistent method for the effective conductivity of composites with ellipsoidal inclusions and cracked bodies, J. Appl. Phys. 63 (3) (1988) 789-796.

[39] G. Constantinides, F.-J. Ulm, The effect of two types of C-S-H on the elasticity of cement-based materials: Results from nanoindentation and micromechanical modeling, Cem. Concr. Res. 34 (1) (2004) 67-80.

[40] F.-J. Ulm, G. Constantinides, F.H. Heukamp, Is concrete a poromechanics materials? A multiscale investigation of poroelastic properties, Mater. Struct. 37 (1) (2004) 43-58.

[41] E. Stora, Q.-C. He, B. Bary, Influence of inclusion shapes on the effective linear elastic properties of hardened cement pastes, Cem. Concr. Res. 36 (2006) 1330-1344.

[42] C. Pichler, R. Lackner, H. Mang, A multiscale micromechanics model for the autogenous-shrinkage deformation of early-age cement-based materials, Eng. Fract. Mech. 74 (2007) 34-58.

[43] T. Honorio, B. Bary, F. Benboudjema, Multiscale estimation of ageing viscoelastic properties of cement-based materials: a combined analytical and numerical approach to estimate the behaviour at early age, Cem. Concr. Res. 85 (2016) 137-155.

[44] A. Atkinson, A.K. Nickerson, The diffusion of ions through water-saturated cement, J. Mater. Sci. 19 (1984) 3068-3078.

[45] F. Grondin, M. Bouasker, P. Mounanga, A. Khelidj, A. Perronnet, Physico- chemical deformations of solidifying cementitious systems: multiscale modelling, Mater. Struct. 43 (2010) 151-165.

[46] N. Venkovic, L. Sorelli, B. Sudret, T. Yalamas, R. Gagné, Uncertainty propagation of a multiscale poromechanics-hydration model for poroelastic properties of cement paste at early-age, Probabilistic Eng. Mech. 32 (2013) 5-20.

[47] B. Pichler, C. Hellmich, J. Eberhardsteiner, Spherical and acicular representation of hydrates in a micromechanical model for cement paste: Prediction of early-age elasticity and strength, Acta Mech. 203 (3-4) (2009) 137-162.

[48] B. Pichler, C. Hellmich, Upscaling quasi-brittle strength of cement paste and mortar: a multi-scale engineering mechanics model, Cem. Concr. Res. 41 (2011) 467-476.

[49] B. Pichler, C. Hellmich, J. Eberhardsteiner, J. Wasserbauer, P. Termkhajornkit, R. Barbarulo, G. Chanvillard, Effect of gel-space ratio and microstructure on strength of hydrating cementitious materials: an engineering micromechanics approach, Cem. Concr. Res. 45 (2013) 55-68.

[50] P. Termkhajornkit, Q.H. Vu, R. Barbarulo, S. Daronnat, G. Chanvillard,Dependence of compressive strength on phase assemblage in cement pastes: beyond gel-space ratio - Experimental evidence and micromechanical modeling, Cem. Concr. Res. 56 (2014) 1-11.

[51] P. Pivonka, C. Hellmich, D. Smith, Microscopic effects on chloride diffusivity of cement pastes - a scale-transition analysis, Cem. Concr. Res. 34 (12) (2004) 2251-2260.

[52] N. Damrongwiriyanupap, S. Scheiner, B. Pichler, C. Hellmich, Self-consistent channel approach for upscaling chloride diffusivity in cement pastes, Transp. Porous Med. 118 (3) (2017) 495-518.

[53] E. Stora, Q.-C. He, B. Bary, A mixed composite spheres assemblage model for the transport properties of random heterogeneous materials with high contrasts, J. Appl. Phys. 100 (8) (2006) 084910.

[54] B. Lothenbach, T. Matschei, G. Möschner, F.P. Glasser, Thermodynamic modelling of the effect of temperature on the hydration and porosity of Portland cement, Cem. Concr. Res. 38 (1) (2008) 1-18.

[55] H. Ranaivomanana, J. Verdier, A. Sellier, X. Bourbon, Toward a better comprehension and modeling of hysteresis cycles in the water sorption-desorption process for cement based materials, Cem. Concr. Res. 41 (8) (2011) 817-827.

[56] H. Ma, Z. Li, Realistic pore structure of Portland cement paste: experimental study and numerical simulation, Comput. Concr. 11 (4) (2013) 317-336.

[57] S. Béjaoui, B. Bary, Modeling of the link between microstructure and effective diffusivity of cement pastes using a simplified composite model, Cem. Concr. Res. 37 (2007) 469-480.

[58] G. Constantinides, F.-J. Ulm, The nanogranular nature of C-S-H, J. Mech. Phys. Solids 55 (2007) 64-90.

[59] R. Shahsavari, S.H. Hwang, Cement Based Materials, chap. Morphogenesis of Cement Hydrate: From Natural C-S-H to Synthetic C-S-H, IntechOpen, ISBN 978-1-78984-154-1, 2018..

[60] F.-J. Ulm, H.M. Jennings, Does C-S-H particle shape matter? A discussion of the paper "Modelling elasticity of a hydrating cement paste", by Julien Sanahuja, Luc Dormieux and Gilles Chanvillard. CCR 37 (2007) 1427-1439, Cem. Concr. Res. 38 (8) (2008) 1126-1129..

[61] J. Sanahuja, L. Dormieux, G. Chanvillard, A reply to the discussion does C-S-H particle shape matter? F.-J. Ulm and H. Jennings of the paper modelling elasticity of a hydrating cement paste, CCR 37 (2007), Cem. Concr. Res. 38 (8) (2008) 1130-1134..

[62] S. Garrault, Study of C-S-H growth on C3S surface during its early hydration, Mater. Struct. 38 (278) (2005) 435-442.

[63] T.C. Hansen, Physical structure of hardened cement paste. A classical approach, Matériaux et Constructions 19 (114) (1986) 422-436.

[64] F. Lin, C. Meyer, Hydration kinetics modeling of Portland cement considering the effects of curing temperature and applied pressure, Cem. Concr. Res. 39 (4) (2009) 255-265.

[65] R. Helmuth, D. Turk, Elastic moduli of hardened portland cement and tricalcium silicate pastes: effect of porosity, Portland Cement Association. Research and Development Laboratories, 1966.

[66] P.D. Tennis, H.M. Jennings, Model for two types of calcium silicate hydrate in the microstructure of Portland cement pastes, Cem. Concr. Res. 30 (6) (2000) 855-863.

[67] A. Boumiz, D. Sorrentino, C. Vernet, F. Cohen Tenoudji, Modelling the development of the elastic moduli as a function of the degree of hydration of cement pastes and mortars, in: Why does cement set? An interdisciplinary approach, Second RILEM workshop on hydration and setting, Dijon, France, 1997..

[68] J. Zhang, E.A. Weissinger, S. Peethamparan, G.W. Scherer, Early hydration and setting of oil well cement, Cem. Concr. Res. 40 (7) (2010) 1023-1033.

[69] J. Torrenti, F. Benboudjema, Mechanical threshold of cementitious materials at early age, Mater. Struct. 38 (2005) 299-304.

[70] J. Taplin, A method of following the hydration reaction in portland cement paste, Aust. J. Appl. Sci. 10 (3) (1959) 329-345.

[71] G. De Schutter, L. Tearwe, Degree of hydration-based description of mechanical properties of early age concrete, Mater. Struct. 29 (7) (1996) 335-344.

[72] K. Velez, S. Maximilien, D. Damidot, G. Fantozzi, F. Sorrentino, Determination by nanoindentation of elastic modulus and hardness of pure constituents of Portland cement clinker, Cem. Concr. Res. 31 (4) (2001) 555-561.

[73] F. Holuj, M. Drozdowski, M. Czajkowski, Brillouin spectrum of Ca(OH)2, Solid State Commun. 56 (1985) 1019-1021.

[74] P. Monteiro, C. Chang, The elastic moduli of calcium hydroxide, Cem. Concr. Res. 25 (1995) 1605-1609.

[75] O. Coussy, Mechanics and Physics of Porous Solids, John Wiley and Sons Ltd, 2010.

[76] L. Dengke, Z. Wanyu, H. Dongshuai, Z. Tiejun, Molecular dynamics study on the chemical bound, physical adsorbed and ultra-confined water molecules in the nano-pore of calcium silicate hydrate, Constr. Build. Mater. 151 (2017) 563-574.

[77] A.G. Kalinichev, J. Wang, R.J. Kirkpatrick, Molecular dynamics modeling of the structure, dynamics and energetics of mineral-water interfaces: Application to cement materials, Cem. Concr. Res. 37 (3) (2007) 337-347.

[78] S.S. Yoon, P. Monteiro, Molecular dynamics study of water molecules in interlayer of 14 å tobermorite, J. Adv. Concrete Technol. 11 (6) (2013) 180-188.

[79] B. Zehtab, A. Tarighat, Diffusion study for chloride ions and water molecules in C-S-H gel in nano-scale using molecular dynamics: Case study of tobermorite, Adv. Concr. Constr. 4 (4) (2016) 305-317.

[80] J.-P. Korb, P. McDonald, L. Montheilhet, A. Kalinichev, R. Kirkpatrick, Comparison of proton field-cycling relaxometry and molecular dynamics simulations for proton-water surface dynamics in cement-based materials, Cem. Concr. Res. 37 (3) (2007) 348-350.

[81] P.T. Nguyen, O. Amiri, Study of the chloride transport in unsaturated concrete: highlighting of electrical double layer, temperature and hysteresis effects, Constr. Build. Mater. 122 (2016) 284-293.

[82] S.W. Yu, C.L. Page, Diffusion in cementitious materials: I. Comparative study of chloride and oxygen diffusion in hydrated cement pastes, Cem. Concr. Res. 21 (1991) 581-588.

[83] E. Cussler, Diffusion: Mass Transfer in Fluid Systems, Cambridge University Press, 1984.

[84] C.L. Page, N.R. Short, A.E. Tarras, Diffusion of chloride ions in hardened cement pastes, Cem. Concr. Res. 11 (3) (1981) 395-406.

[85] V.T. Ngala, C.L. Page, L.J. Parrott, S.W. Yu, Diffusion in cementitious materials: II. Further investigations of chloride and oxygen diffusion in well-cured OPC and OPC/30%PFA pastes, Cem. Concr. Res. 25 (4) (1995) 819-826.

[86] V.T. Ngala, C.L. Page, Effects of carbonation on pore structure and diffusional properties of hydrated cement pastes, Cem. Concr. Res. 27 (7) (1997) 995-1007.

[87] L. Tang, L.-O. Nilsson, Rapid determination of the chloride diffusivity in concrete by applying an electric field, ACI Mater. J. 89 (1) (1993) 49-53.

[88] K.A. MacDonald, D.O. Northwood, Experimental measurements of chloride ion diffusion rates using a two-compartment diffusion cell: effects of material and test variables, Cem. Concr. Res. 25 (7) (1995) 1407-1416.

[89] M. Castellote, C. Alonso, C. Andrade, G. Chadbourn, C. Page, Oxygen and chloride diffusion in cement pastes as a validation of chloride diffusion coefficients obtained by steady-state migration tests, Cem. Concr. Res. 31 (2001) 1407-1416.

[90] H. Hornain, J. Marchand, V. Duhot, M. Moranville-Regourd, Diffusion in limestone filler of chloride blended cement ions pastes and mortars, Cem. Concr. Res. 25 (8) (1995) 1667-1678.

[91] S. Caré, Influence of aggregates on chloride diffusion coefficient into mortar, Cem. Concr. Res. 33 (2003) 1021-1028.

[92] X. Huang, J. Zheng, X. Zhou, Simple Analytical Solution for the Chloride Diffusivity of Cement Paste, Sci. Technol. Overseas Build. Mater. 32 (2) (2010) 4-6.

[93] G. Sun, Y. Zhang, W. Sun, Z. Liu, C. Wang, Multi-scale prediction of the effective chloride diffusion coefficient of concrete, Constr. Build. Mater. 25 (10) (2011) 3820-3831.

[94] A. Princigallo, Estimating the chloride transport in cement paste, Materiales de Construcción 62 (306) (2012) 151-161.

[95] P. Halamickova, R.J. Detwiler, D.P. Bentz, E.J. Garboczi, Water permeability and chloride diffusion in portland cement mortars: relationship to sand content and critical pore diameter, Cem. Concr. Res. 25 (1) (1995) 790-802.

[96] F. Lavergne, A. Ben Fraij, I. Bayane, J.F. Barthélémy, Estimating the mechanical properties of hydrating blended cementitious materials: An investigation based on micromechanics, Cem. Conc. Res. 104 (2018) 37-60.