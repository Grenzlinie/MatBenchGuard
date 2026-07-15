![](./images/813258483888553985_1.jpg)

Available online at www.sciencedirect.com

SciVerse ScienceDirect

www.elsevier.com/locate/jmbbm

![](./images/813258483888553985_2.jpg)

Research paper

# Influence of statistical size effects on the plastic deformation of coronary stents

J.A. Grogan*, S.B. Leen, P.E. McHugh

Biomechanics Research Centre (BMEC), Mechanical and Biomedical Engineering, College of Engineering and Informatics, NUI, Galway, Ireland

## ARTICLE INFO

Article history:
Received 5 September 2012
Received in revised form
13 December 2012
Accepted 17 December 2012
Available online 2 January 2013

Keywords:
Finite elements
Crystal plasticity
Metallic microstructures
Stents

## ABSTRACT

The dimensions of coronary stent struts are similar to those of the metallic grains of their constituent alloys. This means that statistical size effects (SSEs), which are evident in polycrystals with few grains through their dimensions, can have detrimental effects on the mechanical performance of stent struts undergoing large plastic deformation. Current trends in coronary stent design are towards thinner struts, potentially increasing the influence of SSEs. In order to maintain adequate device performance with decreasing strut thickness, it is therefore important to assess the role of SSEs in the plastic deformation of stents. In this study, finite element modelling and crystal plasticity theory are used to investigate SSEs in the deformation of struts in tension and bending. The relationships between SSEs and microstructure morphology, alloy strain hardening behaviour and secondary phases are also investigated. It is predicted that reducing the number of grains through the strut cross section and increasing the number of grains along the strut length have detrimental effects on mechanical performance. The magnitudes of these effects are predicted to be independent of the uniformity of the studied microstructures, but dependent on alloy strain hardening behaviour. It is believed that model predictions will aid in identifying a lower bound on suitable strut thicknesses in coronary stents for a range of alloys and microstructures.

© 2012 Elsevier Ltd. All rights reserved.

### 1. Introduction

Coronary stents are small tubular scaffolds that are used in the treatment of atherosclerosis. The struts of these stents have widths and thicknesses on the order of $100\,\mu\text{m}$, and are similar in size to the metallic grains of typical stent materials, such as stainless steel (316L) and cobalt chromium (L605). In the development of coronary stents there is a trend towards reduced strut thickness, which is driven by (i) the favourable performance of stents with thinner struts in a number of clinical trials (Kastrati et al., 2001; Pache et al., 2003), (ii) a desire for increased device flexibility and (iii) the availability of high strength alloys, such as cobalt and platinum chromium.

Due to the small size of coronary stent struts, their mechanical behaviour can differ markedly from that of larger components consisting of the same material (Murphy et al., 2003; Weiss et al., 2009). This difference can be attributed to a number of well-known size effects in miniaturised polycrystals. In order to ensure reliable stent performance and to determine whether further reductions in strut dimensions are feasible, it is important to assess how these size effects influence overall device behaviour.

*Corresponding author.
E-mail address: j.grogan1@nuigalway.ie (J.A. Grogan).

1751-6161/$ - see front matter © 2012 Elsevier Ltd. All rights reserved.
http://dx.doi.org/10.1016/j.jmbbm.2012.12.008

### 1.1. Size effects in metallic components

As detailed in Geers et al. (2006), size effects arising from the miniaturisation of metallic components can be classified as (i) statistical size effects, (ii) intrinsic size effects, (iii) strain gradient effects and (iv) surface constraint effects.

Statistical size effects (SSEs) arise when the geometric dimensions of polycrystals approach those of their metallic grains. These effects can result in the overall mechanical behaviour of the polycrystal being heavily influenced by the behaviour of relatively few grains, as observed in the studies of Murphy et al. (2003), Janssen et al. (2006), Weiss et al. (2009) and Keller et al. (2011). Intrinsic size effects are related to intrinsic length scales within the metallic microstructure, such as the Burgers vector length, grain size and grain boundary width. An example is the Hall-Petch relationship, which predicts an increase in specimen strength with decreasing grain size (Armstrong et al., 1962; Jain et al., 2008; Lim et al., 2011). Strain gradient effects are related to the absolute size of a specimen and arise from the development of geometrically necessary dislocations (GND) in the crystallographic lattice. These effects typically lead to strengthening of specimens with smaller dimensions (Fleck et al., 1994; Stölken and Evans, 1998; Haque and Saif, 2003; Geers et al., 2006; Zhang et al., 2007). Surface constraint effects are related to ability of dislocations to glide out of the surfaces of miniaturised components (Arzt, 1998; Bayley et al., 2007; Keller et al., 2010, 2012) and can lead to either strengthening or weakening with miniaturisation, depending on the surface condition.

SSEs are of particular interest in the development of coronary stents, due to the similarity in strut and grain dimensions and the current trend towards thinner struts. Due to SSEs, decreasing polycrystal dimensions for a fixed grain size typically leads to reduced strength and ductility in metallic components, as their overall mechanical behaviour tends towards that of a single metallic grain. SSEs have been observed in a range of metals, including aluminium (Klein et al., 2001; Raulea et al., 2001; Gau et al., 2007; Lederer et al., 2010), brass (Kals and Eckstein, 2000; Gau et al., 2007), copper and copper alloys (Klein et al., 2001; Khatibi et al., 2005), iron and steel (Murphy et al., 2003; Weiss et al., 2009; Lim et al., 2011) and silver (Chen and Ngan, 2011). Due to the important role of SSEs in determining the mechanical performance of thin polycrystals and, in the case of coronary stents, their relevance in the determination of minimum strut sizes, the focus of this study is to assess how SSEs affect the plastic deformation of coronary stents.

### 1.2. Computer modelling of statistical size effects

It is difficult to experimentally determine the influence of SSEs alone on polycrystal plasticity, as changing specimen to grain size ratios will naturally introduce other size effects. Computational modelling is therefore an attractive method of gaining further insight into their influence on polycrystal deformation. In investigating these size effects through computational modelling a number of approaches have been taken. The first approach focuses on homogenised modelling of the polycrystal aggregate, facilitated through the development of material constitutive laws with dependence of flow stress on ratios of grain size to specimen size. The second focuses on explicitly modelling the mechanical behaviour of individual crystals in the aggregate through continuum plasticity models, single crystal plasticity models or gradient enhanced single crystal plasticity models.

Using the first approach, Kim et al. (2007), Lai et al. (2008) and Yun et al. (2010) updated a previously developed Hall-Petch type relationship (Armstrong, 1961) to describe flow stress in sheets in tension as a function of applied strain and the volume ratio of surface grains to internal grains. Their approach assumed surface grains to be 'weaker' than internal grains following the work of Engel and Eckstein (2002). Model predictions in these studies showed good agreement with a range of experiments in terms of true stress-strain behaviour, although the chosen modelling approach is somewhat empirical in nature. Molotnikov et al. (2008) used a similar approach in developing a constitutive model, with flow stress again depending on the ratio of surface to internal grains. In this case a more physical stress evolution law was employed, based on the models of Estrin et al. (1998) and Toth et al. (2002).

Using the second approach, Chan et al. (2010) studied the deformation of pure copper polycrystals in compression through explicit modelling of individual grains with different stress-strain behaviours using an isotropic continuum plasticity theory. Predictions showed agreement with corresponding compression experiments in terms of true stress-strain behaviour, although the method used did not account for anisotropy (or orientation dependence) in the plastic deformation of individual grains. Savage et al. (2004), Murphy et al. (2006) and Harewood and McHugh (2007) modelled the deformation of polycrystals through explicitly modelling each grain using single crystal plasticity theory (Asaro and Rice, 1977; Peirce et al., 1983) and finite element simulations. These studies focused on the influence of SSEs on the ductility of stainless steel (316L) struts of fixed aspect ratio, with good agreement achieved between predictions of strut ductility and the experiments of Murphy et al. (2003). Wang et al. (2009) and Cao et al. (2009) used a similar approach to study necking in thin 316L films and showed the ability of such modelling to capture decreases in flow stress due to reductions in the number of grains through specimen dimensions. Liang-ying et al. (2007) and Fülöp et al. (2006) used similar models in predicting the influences of SSEs in Al foils, predicting reductions in flow stress tension in foils with decreasing numbers of grains through their thickness. The latter study also predicted reduced normalised force in bending for foils with fewer grains through the thickness.

Geers et al. (2006), Bayley et al. (2007), Hoefnagels et al. (2008) and Keller et al. (2012) have studied the interaction of SSEs and other size effects in aluminium and nickel foils using gradient enhanced crystal plasticity finite element modelling, based on modified versions of a model proposed by Evers et al. (2004). This approach has given important insights into competitive interactions between SSEs, which induce weakening behaviour and strain gradient effects, which promote strengthening. Geers et al. (2006) have predicted that a synergistic relationship exists between SSEs and other size effects in certain loading cases, while

the modelling approach of Keller et al. (2012) predicted strengthening in cases where average grain sizes were increased to be greater than the specimen thickness and also a dependence of the magnitude of SSEs on absolute grain size.

### 1.3. Study aims
The goal of this study is to use finite element analysis and single crystal plasticity theory to predict the influence of SSEs on coronary stent strut performance: (i) across a range of different materials, (ii) in struts with a range of thicknesses and lengths for a fixed grain size, (iii) for regular and random microstructures, and (iv) for alloy microstructures with and without precipitates. The influence of SSEs is predicted for both tensile and bending loading conditions, consistent with typical stent loading conditions in deployment. Since coronary stent struts are often subject to large plastic deformation in service, SSEs are investigated in struts undergoing deformation up to, and beyond, the point of $\epsilon_u$ (strain at maximum supported load; ASM International, 2002).

The results of this study will be useful in the on-going development of coronary stents, as SSEs are quantified in stent struts for a range of materials. This is important since a variety of materials are now under consideration for stent applications (O'Brien and Carroll, 2009). Results are also of interest in the general study of miniaturised polycrystals, as the majority of previously mentioned experimental and computational studies have only focused on SSEs in a single material. Model predictions will aid in the identification of minimum suitable strut sizes in stents for a given combination of alloy and microstructure, in particular when used in conjunction with previously developed safe design charts (Savage et al., 2004; Harewood and McHugh, 2007; Harewood et al., 2011). Results will also prove useful in the design of novel bioabsorbable metallic stents, where previous studies have predicted a relatively high strut fracture risk (Grogan et al., 2011, 2012) without accounting for SSEs and where alloy, microstructure and strut thickness may need to be judiciously chosen for optimal mechanical and corrosion performance.

## 2. Single crystal theory
Simulations performed in this work are based on the assumptions of finite deformation kinematics and incorporate both elastic and plastic constitutive laws. The fundamental kinematical basis of the crystal plasticity constitutive theory used in this work, as discussed in detail in McGarry et al. (2004), is given by the multiplicative decomposition of the deformation gradient, $\mathbf{F}$, into elastic, $\mathbf{F}^e$, and plastic, $\mathbf{F}^p$, parts:

$$
\mathbf{F} = \mathbf{F}^e \cdot \mathbf{F}^p \tag{1}
$$

where rigid body motions are typically considered to be included in $\mathbf{F}^e$, although they could be included in either, or both, decomposed tensors. In rate form, $\mathbf{F}$ leads to the spatial velocity tensor, $\mathbf{L}$, defined as

$$
\mathbf{L} = \dot{\mathbf{F}} \cdot \mathbf{F}^{-1} \tag{2}
$$

where $(\bullet)$ refers to a time derivative. The symmetric part of $\mathbf{L}$ yields the rate of deformation tensor $\mathbf{D}=sym(\mathbf{L})$ and the skew-symmetric part yields the spin tensor, $\mathbf{W}=skew(\mathbf{L})$. An additive decomposition of $\mathbf{L}$ is obtained by substituting Eq. (1) into Eq. (2) as follows:

$$
\begin{aligned}
\mathbf{L} &= \dot{\mathbf{F}} \cdot \mathbf{F}^{-1} = \left(\dot{\mathbf{F}}^e \cdot \mathbf{F}^p + \mathbf{F}^e \cdot \dot{\mathbf{F}}^p\right) \cdot \mathbf{F}^{-1} \\
&= \dot{\mathbf{F}}^e \cdot \mathbf{F}^p \cdot \mathbf{F}^{p^{-1}} \cdot \mathbf{F}^{e^{-1}} + \mathbf{F}^e \cdot \dot{\mathbf{F}}^p \cdot \mathbf{F}^{p^{-1}} \cdot \mathbf{F}^{e^{-1}} \\
&= \mathbf{L}^e + \mathbf{L}^p
\end{aligned} \tag{3}
$$

where $\mathbf{L}^e = \dot{\mathbf{F}}^e \cdot \mathbf{F}^{e^{-1}}$ and $\mathbf{L}^p = \mathbf{F}^e \cdot \dot{\mathbf{F}}^p \cdot \mathbf{F}^{p^{-1}} \cdot \mathbf{F}^{e^{-1}}$. From this, on taking the symmetric part, an additive decomposition of the rate of deformation tensor can be identified as follows:

$$
\begin{aligned}
\mathbf{D} &= \mathbf{D}^e + \mathbf{D}^p \\
\mathbf{D}^e &= sym(\mathbf{L}^e) \\
\mathbf{D}^p &= sym(\mathbf{L}^p)
\end{aligned} \tag{4}
$$

Interpreting rate of deformation as a finite strain rate measure results in an additive decomposition of the strain rate into finite elastic and plastic parts.

In this study elasticity is described using an elastic strain energy density potential (DS Simulia, 2010). Elasticity is considered linear and isotropic in terms of finite deformation quantities, namely the Cauchy stress and the Lagrangian strain, with the assumption of small elastic strains. This common assumption in elastic-plastic material descriptions (Belytschko et al., 2000) is deemed an appropriate simplification in the context of this study, as plastic strains are observed to exceed elastic strains by many orders of magnitude.

Plasticity is described using a rate-dependent crystal plasticity theory, which follows from that presented by Huang (1991) and Peirce et al. (1983), and which has been employed in previous studies such as those of Savage et al. (2004) and Harewood and McHugh (2007). In crystal plasticity theory massive dislocation motion on a crystal slip system is represented as a plastic shear strain or 'plastic slip' in the slip direction. This plastic slip is related to $\mathbf{F}^p$ in terms of rates through the following equation:

$$
\dot{\mathbf{F}}^p \cdot \mathbf{F}^{p^{-1}} = \sum_\alpha \dot{\gamma}^{(\alpha)} \mathbf{s}_\alpha \mathbf{m}_\alpha \tag{5}
$$

where $\dot{\gamma}^{(\alpha)}$ is the plastic slip rate on slip system $\alpha$, $\mathbf{s}_\alpha$ and $\mathbf{m}_\alpha$ are unit vectors defining slip direction and slip normal, respectively, for slip system $\alpha$, and the summation runs over all slip systems active at a given material point.

Plastic slip is assumed to follow Schmidt's law, with the rate of plastic shear strain,$\dot{\gamma}^{(\alpha)}$, along a crystallographic slip system, $\alpha$, assumed to depend on the Schmidt resolved shear stress, $\tau^{(\alpha)}$, acting on that system. In this study the plastic shear strain rate is related to the resolved shear stress through the following power-law rate-dependent relationship:

$$
\dot{\gamma}^{(\alpha)} = \dot{a} sgn\left(\tau^{(\alpha)}\right) \left\{ \frac{\left|\tau^{(\alpha)}\right|}{g^{(\alpha)}} \right\}^n \tag{6}
$$

where $\dot{a}$ and $n$ are the reference strain rate and rate sensitivity exponent, respectively and $g^{(\alpha)}$ is the slip system strain hardness, which is determined by integration of the following evolution equation:

$$
\dot{g}^{(\alpha)} = \sum_\alpha h_{\alpha \beta} \left| \dot{\gamma}^{(\beta)} \right| \tag{7}
$$

where $h_{\alpha \beta}$ are the strain hardening moduli; $h_{\alpha \alpha}$ and $h_{\alpha \beta} (\alpha \neq \beta)$ are the self and latent hardening moduli respectively. In this study Taylor isotropic hardening is assumed where the self and latent hardening moduli are considered equal.

Strain hardening on each slip system is described by the following hardness function, as defined by Peirce et al. (1983):

$$
g(\gamma_{\alpha})=g_{0}+\left(g_{\infty}-g_{0}\right) \tanh \left|\frac{h_{0} \gamma_{\alpha}}{g_{\infty}-g_{0}}\right|
\tag{8}
$$

where $g_{0}$ and $g_{\infty}$ are the initial and maximum slip system hardness respectively and $h_{0}$ is the initial slip system strain hardening modulus $(\partial g / \partial \gamma_{\alpha}$ when $\gamma_{\alpha}=0)$. The hardening moduli, $h_{\alpha \alpha}$ and $h_{\alpha \beta}$, can be determined through differentiation:

$$
h_{\alpha \alpha}=h_{\alpha \beta}=h\left(\gamma_{\alpha}\right)=\frac{d g\left(\gamma_{\alpha}\right)}{d \gamma_{\alpha}}=h_{0} \operatorname{sech}^{2}\left|\frac{h_{0} \gamma_{\alpha}}{g_{\infty}-g_{0}}\right|
\tag{9}
$$

The quantity, $\gamma_{\alpha}$, is the accumulated slip, which is a measure of total crystallographic plastic strain at a given point and is defined as follows:

$$
\gamma_{\alpha}=\sum_{\alpha} \int_{0}^{t}\left|\dot{\gamma}^{(\alpha)}\right| d t
\tag{10}
$$

where $t$ is the time and the summation is over all active slip systems at a point. The materials modelled in this study have a face-centred-cubic (FCC) crystalline structure, with slip systems $\{111\}\langle 110\rangle$.

The crystal plasticity theory constitutive behaviour described here is implemented for use with the Abaqus/ Standard FE code (DS SIMULIA, USA) by means of a user- defined material subroutine (UMAT; Huang, 1991).

## 3. Methods

A comprehensive set of simulations are performed to char- acterise the influence of SSEs on the deformation of thin struts. Struts are represented using a 2-D geometry due to the previously documented computational expense of 3-D mod- elling of aggregates using single crystal plasticity theory (McGarry et al., 2007), and the confirmed predictive capability of similar 2-D polycrystal models (Savage et al., 2004; Harewood and McHugh, 2007), relative to the experiments of Murphy et al. (2003). A generalised plane-strain behaviour is assumed in the out of plane dimension, as per Harewood and McHugh (2006). Despite the use of a 2-D geometry, each metallic grain is assigned a uniformly distributed random 3-D lattice orientation in all simulations (i.e. the plastic slip computation at each integration point considers slip on all 12 slip planes, each of which can be orientated in 3-D), resulting in a texture-less microstructure. While texture will, in general, strongly influence SSEs, it is assumed that the annealing process, which coronary stent tubing undergoes during manufacture (Poncin and Proft, 2003), removes tex- tures introduced during prior cold-working treatments. Although relatively little has been reported on textures in annealed stents, this assumption is based on reports of 'weak' textures in annealed stent tubing (Weiss and Meissner, 2006) and the possibility of attaining 'weak' tex- tures in 316L with appropriate annealing conditions (Chowdhury et al., 2005).

### 3.1. Model generation

The simulations performed in this study are divided into a number of sets, as detailed in Table 1. Within these sets, SSEs are characterised for struts: (i) loaded in tension, (ii) loaded in bending, and (iii) with different microstructure morphologies.

The required geometries, microstructures and associated finite element meshes for each setare generated using a custom-written Python script, with a flowchart for the

![](./images/813258483888553985_3.jpg)

Fig. 1 - Algorithm for the python script developed in this work for the automated generation of meshed microstructure geometries through the Abaqus/CAE geometry kernel.

<table>
<caption>Table 1 - Details on each set of FE simulations performed in this study over a range of strut lengths (l), thicknesses (t) and grain diameters (d).</caption>
<thead>
<tr>
<th>Set</th>
<th>Material</th>
<th>l/d</th>
<th>t/d</th>
<th>Loading</th>
<th>Precipitates</th>
<th>Grain geometry</th>
</tr>
</thead>
<tbody>
<tr>
<td>1</td>
<td>316L, A, B</td>
<td>1.7, 5, 16.8, 33.6, 67.2, 134.5</td>
<td>1.5, 5, 10, 16.8, 25.2</td>
<td>Tension</td>
<td>No</td>
<td>Regular</td>
</tr>
<tr>
<td>1</td>
<td>L605</td>
<td>134.5</td>
<td>1.5, 5, 10, 16.8</td>
<td>Tension</td>
<td>No</td>
<td>Regular</td>
</tr>
<tr>
<td>2</td>
<td>316L</td>
<td>2-50</td>
<td>1.5, 5, 10</td>
<td>Bending</td>
<td>No</td>
<td>Regular</td>
</tr>
<tr>
<td>3</td>
<td>316L</td>
<td>134.5</td>
<td>1.5, 5, 10, 16.8, 25.2</td>
<td>Tension</td>
<td>No</td>
<td>Random</td>
</tr>
<tr>
<td>3</td>
<td>316L</td>
<td>16.8</td>
<td>1.5, 5, 10, 16.8</td>
<td>Tension</td>
<td>Yes</td>
<td>Regular</td>
</tr>
</tbody>
</table>

generation procedure shown in Fig. 1. The script allows the automated generation and meshing of strut geometries with a range of lengths (l) and thicknesses (t) (see Fig. 2(a)) and with varying degrees of microstructure uniformity, following the method of Fritzen et al. (2008). For the random microstructures, Voronoi tessellation vertex co-ordinates are obtained for a given random point seed distribution using the QHULL software package (Barber et al., 1996).

Two degrees of microstructure uniformity are considered, a highly regular microstructure, with grain geometries taking the form of hexagons, and a random microstructure, based on a Poisson-Voronoi tessellation. The tessellation is obtained by generating point seed coordinates using a uniform distribution random number generator, without constraint on the minimum distance between two neighbouring point seeds. For both random and regular microstructures the grain diameter (d), as shown in Fig. 2(c), is determined from the average grain area ($G_a$) according to

$$
d = \sqrt{\frac{2G_a}{3\sqrt{3}}} \tag{11}
$$

which corresponds to the side length of a regular hexagon with area $G_a$. Resulting strut geometries and microstructures are shown in Fig. 2(a) and (b), with a typical grain diameter distribution for the random microstructure shown in Fig. 3. This distribution arises naturally when no constraints are placed on point seed distances in the generation process and is not specifically representative of any experimentally observed microstructure.

![](./images/813258483888553985_4.jpg)

Fig. 2 – (a) 2D representations of the struts with random and regular micro-structures. Thickness (t) is 30 $\mu$m and length (l) is 100 $\mu$m. (b) Struts with random and regular microstructures with thickness 60 $\mu$m and length 200 $\mu$m. (c) A single hexagonal grain of diameter $d$ showing the FE mesh used in this study. (d) Precipitate distribution in the FE mesh. Precipitates are shown in black and are included at all grain triple points.

![](./images/813258483888553985_5.jpg)

Fig. 3 – Grain diameter (d) probability distribution for a typical random microstructure used in this study. $\bar{d}$ is the mean grain diameter and is equal to 5.95 $\mu$m.

Each strut is meshed using reduced integration quadratic generalised plane strain elements (CPEG8R, four integration points and eight nodes) with an average of 96 elements per grain, as shown in Fig. 2(c). The resulting ratio of element size to grain size is equivalent to that of Harewood and McHugh (2006), who have shown its suitability in predicting $\epsilon_u$ in a mesh dependence study based on crystal plasticity simulations similar to the type performed here.

As part of the generation procedure, precipitates are inserted at grain triple points for some of the generated geometries, as shown in Fig. 2(d). The area fraction (4.2%) and size $(1 \times 2\ \mu\text{m}^2)$ of the precipitates are within the range of those reported in annealed L605 stent tubing (Poncin et al., 2005). Since no details of precipitate spacing distributions are given in that study, a regular dispersion is assumed by placing precipitates at grain triple-points only.

Two different loading conditions are considered, uniaxial tension and pure bending. Tensile loading of each strut is simulated as shown in Fig. 4(a). All nodes on the left-most edge of each strutare fixed in the 'x' direction, resulting in a symmetry condition on this edge, while the bottom left and right nodes are fixed in the 'y' direction. To simulate uniaxial tension all nodes on the right edge are displaced an equal distance in the 'x' direction through the use of linear equation constraints. Bending of the struts is simulated as shown in Fig. 4(b). The left edge of the strut is fixed in the 'x' direction, while the bottom left node is fixed in the 'y' direction. A reference node, R1, is rotated about point R2 in Fig. 4(b), with the rotation of the node transferred to the strut through its connexion via rigid beams to all nodes on the right edge.

### 3.2. Material model calibration

SSEs are investigated for four different materials, namely stainless steel 316L, cobalt chromium L605, and two comparator materials, A and B. Materials A and B are arbitrary materials which have similar elastic properties, yield stress

and UTS to 316L, but have lower and higher $\epsilon_u$ respectively. The inclusion of these materials allows the investigation of the dependence of SSEs on single crystal strain hardening behaviour.

All studied materials are assumed to have a FCC crystal structure. A reference strain rate, $\dot{a}$, of $0.0106\ \text{s}^{-1}$ and rate sensitivity exponent, $n$, of 50 are assumed in describing the rate dependence of the plasticity of each material. These values are the same as those used in the study of Harewood and McHugh, 2007 for 316L struts and lead to a relatively rate-independent material behaviour. This is consistent with the room-temperature behaviour of most metals and also ensures a reasonable computational expense. The elastic constants used for each material are given in Table 2. Due to a lack of experimental data on the composition of precipitates in L605 tubing, their behaviour is assumed to be linear elastic, with a Young's modulus of 700 GPa, consistent with that of tungsten carbide (Connolly and McHugh, 1999).

Calibration of the material constants for the crystal plasticity model requires a knowledge of the parameters, $g_0$, $g_\infty$ and $h_0$ from Eq. (8). These parameters are determined by matching predicted yield stress, UTS and $\epsilon_u$ with those reported by Murphy et al. (2003) for stent struts of thickness $150\ \mu\text{m}$ and length 4.0 mm. In order to replicate the geometry of these samples as closely as possible, calibration is carried out using struts with the largest thickness $(150\ \mu\text{m})$ and length (0.8 mm) permitted by available computational resources. Grains are modelled as regular hexagons of diameter $5.95\ \mu\text{m}$, based on grain size data in Murphy et al. (2003).

The resulting values of $g_0$, $g_\infty$ and $h_0$ are shown in Table 2, with the final engineering stress-strain curves of the model and experiment observed to be in excellent agreement, as shown in Fig. 5(a) and Table 3. In addition to 316L, a similar calibration is carried out for L605, based on macroscopic stress-strain data presented in Teague et al. (2004). A grain diameter of $10.0\ \mu\text{m}$ is used in this case, consistent with that reported in Teague et al. (2004). Predicted and experimentally observed stress-strain curves are shown for L605 in Fig. 5(a) and Table 3.

Following calibration, two further material behaviours A and B are generated based on an appropriate choice of $g_0$, $g_\infty$ and $h_0$, leading to materials with, respectively, lower and higher $\epsilon_u$ than 316L. Stress-strain curves for each material are compared to that of 316L in Fig. 5(b), while the adopted values of $g_0$, $g_\infty$ and $h_0$ parameters for all the materials studied are shown in Table 2.

![](./images/813258483888553985_6.jpg)

Fig. 4 - Boundary conditions used for (a) uniaxial tension and (b) pure bending. In (a) and (b) left and right strutedges are kept straight through the application of boundary conditions and linear multi-point constraints. (a) A displacement in the 'x' direction is applied to the right edge to simulate a tensile test. (b) A clock-wise rotation is applied to control node R1 about point R2 to simulate pure bending.

### 3.3. Simulation details

Three sets of simulations are used to characterise SSEs in the studied struts, as detailed in Table 1. In Set 1, SSEs are investigated in struts loaded in tension and consisting each of four materials, 316L, L605, A and B. In these simulations, strut lengths range from 0.01 mm to 0.8 mm and thicknesses range from $9\ \mu\text{m}$ to $150\ \mu\text{m}$, with a subset of these dimensions used for L605, as detailed in Table 1. The average grain diameter for struts consisting of 316L, A and B is $5.95\ \mu\text{m}$, with a diameter of $10.0\ \mu\text{m}$ used for the L605 struts. In this set, and all others, five simulations are performed for each material and combination of thicknesses and lengths, corresponding to five different random lattice orientations.

In Set 2, SSEs are investigated for 316L struts subject to pure bending. The simulated struts have lengths from 0.2 mm to 0.6 mm, thicknesses from 60 to $150\ \mu\text{m}$, and thickness to grain diameter ratios of 1.5-10.0. In Set 3 the influence of microstructure morphology on SSEs is investigated for a subset of the 316L strut dimensions simulated in Set 1, see Table 1. Simulations are conducted for microstructures with regular and random morphologies, with and without precipitates.

<table>
<caption>Table 2 - Elastic properties and single crystal hardening parameters for materials A and B, stainless steel 316L, cobalt chromium L605, and tungsten carbide precipitates.</caption>
<thead>
<tr>
<th>Material</th>
<th>Young's modulus (GPA)</th>
<th>Poisson's ratio</th>
<th>$g_0$ (MPa)</th>
<th>$g_\infty$ (MPa)</th>
<th>$h_0$ (MPa)</th>
</tr>
</thead>
<tbody>
<tr>
<td>Material A</td>
<td>190</td>
<td>0.28</td>
<td>140</td>
<td>300</td>
<td>440</td>
</tr>
<tr>
<td>Material B</td>
<td>190</td>
<td>0.28</td>
<td>140</td>
<td>800</td>
<td>150</td>
</tr>
<tr>
<td>316L</td>
<td>190</td>
<td>0.28</td>
<td>140</td>
<td>380</td>
<td>260</td>
</tr>
<tr>
<td>L605</td>
<td>243</td>
<td>0.3</td>
<td>200</td>
<td>660</td>
<td>400</td>
</tr>
<tr>
<td>Precipitates</td>
<td>700</td>
<td>0.3</td>
<td>–</td>
<td>–</td>
<td>–</td>
</tr>
</tbody>
</table>

In total 650 simulations are performed over the three sets considered. Simulations are performed on between one and six Intel Xeon hex-core processors on an SGI Altix HPC cluster at the Irish Centre for High Performance Computing, requiring over 50,000 CPU hours.

![](./images/813258483888553985_7.jpg)

Fig. 5 - (a) Selected points from stress-strain curves for 150 μm thick 316L struts as tested by Murphy et al. (2003) and L605 rods tested by Teague et al. (2004). Calibrated FE model stress-strain curves are also shown for each material. (b) Stress-strain curves for 316L and two comparison materials, A and B, given by simulated tensile testing of 150 μm thick and 800 μm long struts.

<table>
<caption>Table 3 - Predicted and experimentally observed yield stress, UTS and $\epsilon_u$ values based on simulations performed here and experiments on 316L struts and L605 rods by Murphy et al. (2003) and Teague et al. (2004) respectively.</caption>
<thead>
<tr>
<th>Material</th>
<th colspan="3">Predicted</th>
<th colspan="3">Experimental</th>
</tr>
<tr>
<th></th>
<th>Yield stress (MPa)</th>
<th>UTS (MPa)</th>
<th>$\epsilon_u$</th>
<th>Yield stress (MPa)</th>
<th>UTS (MPa)</th>
<th>$\epsilon_u$</th>
</tr>
</thead>
<tbody>
<tr>
<td>316L</td>
<td>400</td>
<td>716</td>
<td>0.33</td>
<td>400</td>
<td>713</td>
<td>0.33</td>
</tr>
<tr>
<td>L605</td>
<td>550</td>
<td>1103</td>
<td>0.4</td>
<td>550</td>
<td>1118</td>
<td>0.39</td>
</tr>
</tbody>
</table>

## 4. Results

### 4.1. Set 1—SSEs in uniaxial tension

Fig. 6 shows the predicted influence of the number of grains through the dimensions of a 316L strut on its mechanical behaviour in tension. In Fig. 6(a) FE contour plots of maximum principal logarithmic strain ($\epsilon_{mp}$) are shown for struts of the same length and grain size but different thickness in tension. The formation of shear bands is evident in both struts. The development of necking is more pronounced in the thinner strut at $\epsilon_u$ (26% and 32% in the thinner and thicker struts, respectively). Fig. 6(b) shows a selection of predicted engineering stress-strain curves for struts of the same length and grain size. Both UTS and $\epsilon_u$, circled, are reduced with decreasing thickness. Fig. 6(c) shows the predicted reduction in $\epsilon_u$ in struts of fixed grain size and with increasing length and decreasing thickness. Saturation, or 'levelling-off' in $\epsilon_u$ values is evident for each thickness with increasing length.

Fig. 7 shows the predicted influence of single crystal strain hardening behaviour on the deformation of struts with different numbers of grains through their dimensions. Fig. 7(a) shows FE contour plots of $\epsilon_{mp}$ in struts consisting of material A, which has a relatively low 'bulk' $\epsilon_u$, see Fig. 5(b), and material B, which has a relatively high 'bulk' $\epsilon_u$. Necking is more pronounced in material B at $\epsilon_u$ (13% for A and 37% for B). Fig. 7(b) shows the predicted dependence of $\epsilon_u$ on thickness and length in struts with a fixed grain size, for different materials. The $\epsilon_u$ of material B has a greater dependence on both thickness and length than it does in materials A and 316L, shown in Fig. 6(c). The degree of scatter in $\epsilon_u$ (given by the size of error bars on each data point) predicted for material B is somewhat greater than that in materials A and 316L for a given strut size.

In order to aid in the interpretation of results shown in Figs. 6(c) and 7(b) it is useful to describe the predicted SSEs in terms of the following power-law model:

$$
\bar{\epsilon}_{u}=\bar{\epsilon}_{u, 0}\left(\frac{d}{l}\right)^{(\beta d / t)} \tag{12}
$$

where $\bar{\epsilon}_{u}$ is the mean value of $\epsilon_u$ for struts of a given size, taken over a number of different lattice orientations (five in this study), $\bar{\epsilon}_{u, 0}$ is the mean value of $\epsilon_u$ for single crystals ($l/d$=1.0, $t/d$=1.0) of the material, again taken over a number different lattice orientations, and $\beta$ is a fitting parameter.

![](./images/813258483888553985_8.jpg)

Fig. 6 - (a) FE contour plots of max principal logarithmic strain in struts of the same length (l) with five and 10 grains through their thickness (t). (b) Predicted engineering stress-strain curves for struts with increasing number of grains through the thickness and a length of 0.8 mm. UTS and $\epsilon_u$ are circled. (c) $\epsilon_u$ for struts with increasing numbers of grains through their thickness and length. Error bars represent one standard deviation, with five struts simulated for each data point. Fit lines are given by Eq. (12).

In using this model to describe the results shown in both Figs. 6(c) and 7(b), a suitable value for $\beta$ can be found by the following averaging, derived in Appendix A:

$$
\beta=\frac{\sum_{j=1}^{3} \sum_{i=1}^{n}\left[\log _{\left(d_{i} / l_{i}\right)}\left(\frac{\bar{\tau}_{u, i}}{\bar{\tau}_{u, 0, j}}\right)\right]\left(\frac{t_{i}}{d_{i}}\right)}{3n} \tag{13}
$$

where summation is over the $n$ data points for each of the three materials (j) in Figs. 6(c) and 7(b). The resulting predictions from Eq. (12) are shown in Figs. 6(c) and 7(b), based on a value of $\beta=0.37$. The $R^2$ coefficient for the fit of Eq. (12) to the data (0.946) is determined conventionally, as follows:

$$
R^{2}=1-\frac{\sum_{i=1}^{n}\left(y_{i}-f_{i}\right)^{2}}{\sum_{i=1}^{n}\left(y_{i}-\bar{y}\right)^{2}} \tag{14}
$$

where $y$ and $f$ are the respective $\bar{\tau}_u$ predictions from the FE simulations and Eq. (12) and $\bar{y}$ is the mean of all $\bar{\tau}_u$ predictions shown in Figs. 6(c) and 7(b). Due to its simplicity and accuracy, Eq. (12) gives a number of insights into the synergistic roles of modifying strut thickness and length for a fixed grain size on $\epsilon_u$. In particular, Eq. (12) shows that increasing the length reduces $\epsilon_u$ according to a power-law type behaviour, with the extent of this reduction scaling linearly with $\bar{\tau}_{u,0}$. This is evident in Fig. 7(c), where material B is subject
to somewhat more pronounced SSEs than material A. Eq. (12) also shows that as the thickness increases and the strut dence of $\epsilon_u$ on length is quickly diminished.

Fig. 8 shows a direct comparison of the predicted reduction in $\epsilon_u$ with decreasing thickness for 316L and L605. This comparison is of interest in the context of coronary stent design, as it allows a comparison of the performance of both materials for a given strut thickness, while also taking their different average grain diameters into account. A very similar quantitative and qualitative dependence of $\epsilon_u$ on strut thickness is predicted for both materials in this case.

### 4.2. Set 2—SSEs in bending

Figs. 9 and 10 show simulation results for struts in bending. Fig. 9(a) shows FE contour plots of $\varepsilon_{mp}$ in struts of the same thickness and length but different grain sizes loaded in pure

![](./images/813258483888553985_9.jpg)

![](./images/813258483888553985_10.jpg)

Fig. 7 - (a) FE contour plots of max principal logarithmic strain in struts with the same dimensions and grain diameters but consisting of materials A and B. (b) $\epsilon_{u}$ for struts with increasing numbers of grains through their thickness and length for materials A and B. Error bars represent one standard deviation, with five struts simulated for each data point. Fit lines are given by Eq. (12).

bending. In the struts with 1.5 grains through the thickness the deformation is quite inhomogeneous, deviating considerably from the typical constant curvature arc taken by a beam of homogeneous material. However, in the strut with 10 grains through the thickness, the bending deformation is far more regular. Shear bands are predicted to form on the inner and outer edges of the latter strut, but not in the former.

Fig. 9(b) shows a selection of moment-curvature curves for struts of increasing thickness and with two different grain sizes. Moment refers to the reaction moment on RP1 in Fig. 4(b), while curvature, $\kappa$, is given by

$$
\kappa = \frac{\theta}{l} \tag{15}
$$

where $\theta$ is the angle of rotation of RP1 about RP2. This can be regarded as a measure of average curvature along the length of the strut; however as shown in Fig. 9(a), due to the inhomogeneous deformation of some struts, local curvatures may deviate from this value somewhat. Fig. 9(b) shows that, as expected, thicker struts support greater moments and have lower curvatures at maximum moment ($\kappa_{u}$).

![](./images/813258483888553985_11.jpg)

Fig. 8 - $\epsilon_{u}$ in struts of increasing thickness and with material properties and microstructures that are representative of 316L and L605. Error bars represent one standard deviation, with five struts tested for each data point. Power law best fits are included for illustrative purposes.

Fig. 10(a) shows predicted $\kappa_{u}$ for struts of increasing thickness and increasing number of grains through the thickness. As thickness is increased a corresponding reduction in $\kappa_{u}$ is predicted. This result shows good agreement with that previously reported in the simulations of Harewood and McHugh (2007) for 316L struts in bending. However, as seen in Fig. 10(a), the influence of SSEs in bending is not immediately apparent, with similar $\kappa_{u}$ values predicted for each strut of a given thickness, regardless of grain diameter. This is due to $\kappa_{u}$ predictions being heavily influenced by a geometrical effect, brought about by changing the strut's thickness to length ratio. This continuum effect is not due to changes in specimen to grain size ratio, but is solely due to the use of curvature as a measure of deformation. When results are instead considered in terms of maximum surface strain ($\epsilon_{s}$), given by

$$
\epsilon_{s} = \frac{\kappa_{u}t}{2} \tag{16}
$$

the results no longer depend on the ratio of strut thickness to length and the influence of SSEs becomes apparent, as shown in Fig. 10(b).

Fig. 10(b) shows predicted $\epsilon_{s}$ for a combination of strut lengths, thicknesses and grain sizes. Similar SSEs are predicted in bending to those observed in tension, with $\epsilon_{s}$ decreasing with increasing length and increasing with increasing thickness, for a given grain size. The magnitude of the predicted SSEs in bending is somewhat less than in

![](./images/813258483888553985_12.jpg)

![](./images/813258483888553985_13.jpg)

Fig. 9 - (a) FE contour plots of max principal logarithmic strain struts of the same dimensions but different grain diameter (d) subject to pure bending. (b) Predicted moment-curvature curves for a selection of struts of increasing thicknesses and with two different grain diameters.

tension and considerable scatter in $\epsilon_{s}$ is predicted for struts with few grains through their dimensions.

### 4.3. Set 3—influence of microstructure morphology on SSEs

Fig. 11 shows the influence of microstructure morphology on predicted SSEs. FE contour plots of $\varepsilon_{mp}$ are shown in Fig. 11(a) for struts with the same thickness and length but with regular and random microstructures of the same average grain diameter, calculated using Eq. (11). Similar degrees of necking are noted in both microstructures at $\epsilon_{u}$ (24% and 26% in the respective regular and random microstructures), although a more pronounced post-$\epsilon_{u}$ necking is observed in the random microstructure.

The dependence of $\epsilon_{u}$ on thickness for each microstructure type is shown in Fig. 11(b). Both microstructures lead to very similar $\epsilon_{u}$ for a given thickness, both in terms of magnitude and scatter. In addition, model predictions for both sets of microstructures show good qualitative and quantitative agreement with the experimental results of

![](./images/813258483888553985_14.jpg)

![](./images/813258483888553985_15.jpg)

Fig. 10 - Predicted $\kappa_{u}$ for (a) struts with increasing thickness and grain diameters, with a fixed length of 0.6 mm, and (b) $\epsilon_{s}$ in struts with increasing thickness and lengths and fixed grain diameter. Error bars represent one standard deviation, with five struts tested for each data point shown. Power law best fits are included for illustrative purposes.

Murphy et al. (2003), based on tensile testing of thin 316L struts of fixed grain diameter and decreasing thickness. Predictions are also in general agreement with the results of Murphy et al. (2006), although mean $\epsilon_{u}$ values are under-estimated. This may be due to differences in absolute grain sizes between the two experiments or the over-estimation of the extent of SSEs due to the use of a 2-D rather than 3-D modelling approach, as discussed subsequently.

Fig. 12 shows the influence of precipitates on predicted SSEs. FE contour plots of $\varepsilon_{mp}$ are shown in Fig. 12(a) for struts of the same thickness, length and lattice orientations but for microstructures with, and without, precipitates. The addition of precipitates is predicted to lead to more pronounced necking following $\epsilon_{u}$ for a given applied strain. Fig. 12(b)

![](./images/813258483888553985_16.jpg)

Fig. 11 - (a) FE contour plots of max principal logarithmic strain in struts with the same dimensions and grain diameters but with regular and random grain geometries. (b) $\epsilon_u$ for increasing thickness to grain diameter ratio for both random and regular microstructures. The experimental results of Murphy et al. (2003, 2006) are also included. A power law best fit for the data from Murphy et al. (2003) is included for illustrative purposes.

![](./images/813258483888553985_17.jpg)

Fig. 12 - (a) FE contour plots of max principal logarithmic strain in struts with the same dimensions and grain diameters but with and without precipitates. (b) $\epsilon_u$ in struts of increasing thickness and fixed grain diameter and length. Error bars represent one standard deviation, with five struts tested for each data point. Power law best fits are included for illustrative purposes.

shows the predicted influence of precipitate inclusion on the dependence of $\epsilon_u$ on thickness for a given grain size. The inclusion of precipitates leads to a reduction in the predicted magnitude of $\epsilon_u$, however a similar dependence of $\epsilon_u$ on thickness is evident in both microstructures.

## 5. Discussion

A comprehensive numerical investigation of SSEs in 2-D struts is performed over a range of strut sizes, microstructures and materials. Results are discussed in terms of: (i) the roles of $t/d$ and $l/d$ ratios in SSEs, (ii) the role of bulk material properties in SSEs, (iii) the role of SSEs in bending, (iv) accounting for SSEs in stent design and (v) morphology and UTS.

### 5.1. The role of $t/d$ and $l/d$ ratios in SSEs

This study gives a number of new insights into the role of SSEs in strut plasticity. While it has been shown in previous computational studies that for a fixed grain size decreasing the thickness of a strut reduces its $\epsilon_u$ (Savage et al., 2004), the predictions of this study show that the strut's length also has an influence on $\epsilon_u$. It is predicted that the $\epsilon_u$ of struts in tension decreases according to a power-law with an increasing number of grains along the strut length. For struts with single grains through the thickness the mechanism for this decrease is a

'weakest-link' effect, with the overall $\epsilon_u$ of the strut depending largely on the strength and $\epsilon_u$ of the grain most preferably orientated for slip along its length. Increasing the number of grains along the strut length increases the probability of there being a grain with low resistance to slip, until inevitably the strut is guaranteed to contain a grain with the smallest possible resistance to slip for a given set of material properties.

Although the mechanism for $l/d$ ratio effects is conceptually simple, the identification of a power-law dependence of $\epsilon_u$ on $l/d$ ratio and a critical $l/d$ ratio above which these effects are negligible in this study is important. As shown in Fig. 6(c), it is predicted that changing the $l/d$ ratio from 20 to 40 leads to a 37% reduction in predicted failure strain for a $t/d$ ratio of 1.5, and a 21% reduction for a $t/d$ ratio of 5.0. Similarly in bending, as shown in Fig. 10(b), there is a clear dependence of maximum surface strain on $l/d$ ratio for ratios up to 100.

These critical ratios are surprising, given that they are noticeably higher than $l/d$ ratios used in many computational studies on size effects, e.g. Bayley et al. (2007), Fülöp et al. (2006), Murphy et al. (2006), Harewood and McHugh (2007), Hoefnagels et al. (2008); Chan et al. (2010), Keller et al. (2012) and even some experimental studies, e.g. Gau et al. (2007). This suggests that few computational studies are correctly accounting for the important effect of $l/d$ ratio when attempting to predict $t/d$ ratio effects or other micro-structure related size effects. Based on the predictions of this study, it is recommended that in computational and experimental studies on size effects a minimum $l/d$ ratio of 40 in tension and 100 in bending is used to negate $l/d$ ratio effects in struts with few grains through their thickness.

As is evident from Fig. 6(c), increasing the number of grains through the strut thickness is predicted to reduce the extent of the $l/d$ ratio effect, again according to a power law behaviour. The mechanism for this change is that the average strength of several grains through the thickness, rather than that of a single grain, now controls theweakest-link effect. While again this concept is quite simple, it should be noted that (i) to the authors' knowledge the individual contributions of $l/d$ and $t/d$ ratio effects to the overall SSE have not previously been identified, as is done here in Eq. (12), and (ii) it does not account for all features predicted by the single crystal models, such as increased necking prior to UTS in material with higher bulk $\epsilon_u$.

The importance of knowing the contributions of both $t/d$ and $l/d$ ratio effects is evident in stent design. It is often the case that components of the stent geometry are small enough that both $t/d$ and $l/d$ ratio effects are apparent ($t/d$<20, $l/d$<100). If the grain size is changed for a fixed geometry, then both $t/d$ and $l/d$ ratios will change, and will do so to different extents. To account for this, the individual contributions of the $t/d$ and $l/d$ ratio effects to the overall SSE must be known. Hence, to the authors' knowledge this is the first study that allows the effects of changing grain size on SSEs in stent components with low $t/d$ and $l/d$ ratios to be predicted.

### 5.2. The role of bulk material properties in SSEs

As shown in Fig. 7(b) and Eq. (12), it is predicted that $\epsilon_u$ scales linearly with bulk $\epsilon_u$ for struts of a given size and microstructure. This means that the role of SSEs can be predicted for a wide range of FCC metals based on the results of this study and also implies that materials with similar bulk $\epsilon_u$ are susceptible to similar SSEs, despite differences in bulk UTS. This implication is important in terms of stent design. The higher UTS of L605 has facilitated the development of struts with thicknesses significantly less than those typical in 316L stents. L605 stents with struts of thickness as low as 60 $\mu$m have been developed, e.g. PRO-Kinetic, while 316L struts have typically been on the order of 130-140 $\mu$m, e.g. CYPHER, Liberté. Murphy et al. (2003) have shown that for 316L such a reduction leads to >32% (relative) decrease in $\epsilon_u$. Since no similar experimental studies on size effects in L605 have been reported, the predictions of this study give an important insight into how such a reduction in dimensions may affect L605 strut performance. As shown in Fig. 8, it is predicted that L605 is susceptible to similar SSEs to 316L, despite its higher strength. Since SSEs are likely to be a major contributor to overall size effects for struts of this size and since L605 struts are thinner than 316L struts, this finding is of importance in highlighting the need for further investigation of size effects in L605, as part of safe stent design. Overall, this suggests that care should be taken when using 'bulk' material data in the design of L605 stents to ensure conservatism under large plastic deformations due to tension and bending (see Harewood et al., 2011).

### 5.3. The role of SSEs in bending

In this study, surface strain, $\epsilon_s$, has been identified as a quantity that gives new insights into the influence of SSEs in bending. As shown in Fig. 10(b), SSEs in bending are predicted to lead to reductions in $\epsilon_s$ with increasing $l/d$ ratio and $t/d$ ratio. In identifying the underlying mechanism of the SSEs in bending, it remains unclear as to whether strut behaviour is controlled by an average of grain properties through the thickness or whether it depends more strongly on the behaviour of surface grains. Due to the use of $\epsilon_s$ in quantifying the role of SSEs in bending, it is possible to identify the individual contributions of geometrical effects and SSEs to changes in strut performance with changing dimensions. This identification of individual contributions is important in the analysis of stent performance.

As an example, decreasing the thickness of a 330 $\mu$m long 316L strut with grain area 92 $\mu$m$^2$ from 120 $\mu$m to 60 $\mu$m leads to a 100% improvement in maximum curvature due to geometric effects, based on Eq. (16). However, once the negative effects of SSEs are included, based on Fig. 10(b), the improvement drops to 74%. The ability to account for both geometric effects and SSEs in this way makes the results of this study very useful in determining the trade-off in performance in bending between reducing absolute strut thickness and $t/d$ ratio.

### 5.4. Accounting for SSEs in stent design

In addition to the application of the results of this study to stent design discussed above, it is possible to incorporate results directlyinto a previously developed multi-scale design

framework to allow SSEs to be accounted for in stent design in a very general manner.

In this study, the macroscopic failures of straight struts in tension and pure bending are investigated. At this macroscopic level, stent geometries can be considered to be made up of combinations of straight and curved members subject to combi- nations of tensile and bending loading. In previous studies Harewood and McHugh (2007) and Harewood et al. (2011) presented a framework to allow failure risks in real stent geometries in complex loading scenarios to be predicted, based on the results of simulations on straight struts in tension and bending similar to those performed here. The simulations used in the development of the framework used a fixed grain size, fixed strut aspect ratios and were based on a single material (316L). The results of this study allow the predictions of this framework to be extended to designs with different grains sizes and strut aspect ratios and also allow the assessment of a range of materials, both already in use in stents (316L, L605) and prospective materials such as bioabsorbable alloys. Predictive capabilities can be further enhanced through incorporating similar microstructural modelling approaches for characterising stent performance under cyclic loading (Sweeney et al., 2012).

### 5.5. Morphology and UTS
The similarity in predictions for both regular and random microstructures in terms of $\epsilon_{u}$ in Fig. 11(b) is a somewhat surprising result, as the number of grains through the thick- ness in certain regions can be somewhat lower than those in the equivalent regular microstructure. However, this result is in agreement with the findings of Savage et al. (2004) for struts with relatively many (>12) grains through their thickness and Bayley et al. (2007) with fewer grains through the thickness. In explaining the observed similarity, it seems for the random microstructure there is a relatively low probability of a grain that is preferably orientated for slip coinciding with a region with relatively few grains through the thickness.

The introduction of precipitates to the microstructure, which is based on observations of precipitates in L605 stent tubing (Poncin et al., 2005), albeit with simplified distribution, geometry and mechanical properties, leads to a reduction in predicted $\epsilon_{u}$, as shown in Fig. 12(b). This is attributed to the tendency of the precipitates to encourage the formation of early strain localisation as shown in Fig. 12(a). However, the introduction of the precipitates is observed to have relatively little effect on overall SSEs.

It is predicted that SSEs also influence strut UTS, although to a lesser extent than $\epsilon_{u}$. The results of Fig. 6(b) show that the effect on UTS is only noticeable when there are quite few (<5.0) grains through the strut thickness. This may explain the observations of Murphy et al. (2003), who reported no significant reduction in UTS in struts with decreasing thick- ness and fixed grain size, as the minimum number of grains through the strut thickness in that study was 10.0.

### 5.6. Study limitations
This study focuses on 2-D microstructures, essentially with columnar grains extruded through the strut width (w). How- ever, the microstructure of coronary stent struts typically consists of equiaxed austenitic grains. It is likely that the use of a 2-D rather than 3-D representation of the stent strut microstructure, for the same single crystal elastic and plastic properties, will lead to differences in predicted $\epsilon_{u}$ and UTS values due to (i) additional constraints on the deformation of grains arising from the use of generalised plane strain conditions and (ii) the presence of fewer grains through w in 2-D simulations. An insight into the extent of such differences for a fixed grain size and one value of w can be found in McGarry et al. (2007). 2-D simulations were found to over-estimate UTS by 3.4% relative to 3-D simulations and underestimate $\epsilon_{u}$ by 11.2% (in relative terms). 2-D simulations were also reported to undergo earlier shear-band formation and have greater dependence on crystallographic orientation.

Thus, for a given strut thickness the 2-D simulations of this study may over-estimate UTS values and under-estimate $\epsilon_{u}$ relative to an equivalent 3-D simulation, that uses the same single crystal elastic and plastic properties. Notwith- standing differences due to additional constraints, 2-D simu- lations may also over-estimate the role of t/d ratio effects relative to 3-D simulations, as the total number of grains in the cross-section, and not just the thickness, will be impor- tant in the latter. However, such differences, if present, in $\epsilon_{u}$ and the extent of SSEs are likely to decrease as the total number of grains through w in the 3-D simulations approaches one, which is the number inherently assumed by 2-D simulations. Based on the assumption that the total number of grains in the cross-section, 'd²/(tw)', controls the extent of SSEs in 3-D, insights into any discrepancies that may be present between 2-D and 3-D predictions for different 'd/w' ratios could be gained from Eq. (12), by replacing the 'd/t' term in the exponent with 'd²/(tw)' for the 3-D case.

This study focuses on 'first-order' (Geers et al., 2006) size effects in polycrystalline struts and does not account for higher order size effects resulting from changing absolute grain or specimen sizes, nor does it account for free surface effects. These effects can often play a significant role in determining the mechanical behaviour of components, which may exceed or act in synergy with the SSEs (Geers et al., 2006; Keller et al., 2012). Accounting for such effects would require the use of a strain gradient based crystal plasticity models (Evers et al., 2004; Kuroda and Tvergaard, 2008), which would be a very useful addition to what is presented in this work.

A detailed investigation into necking and post-UTS beha- viours of the struts simulated in this study, such as that of Ghosh, 1977, is not presented here. However, such studies have been carried out in McGarry et al. (2007) and Wang et al. (2009), based on similar 2-D and 3-D crystal plasticity models. A more detailed investigation into the influence of SSEs on strut necking behaviour would be beneficial, and in particular would facilitate the implementation of explicit material fail- ure models, such as the void growth model of Rice and Tracey (1969). Thiswould be of particular relevance in the vicinity of precipitates (Kadkhodapour et al., 2011).

## 6. Conclusions
Statistical size effects (SSEs) arise in microscale metallic components, such as coronary stent struts, when their

dimensions approach those of the metallic grains in their underlying microstructure. In this study, the influence of SSEs on the mechanical behaviour of coronary stent struts in bending and tension is assessed through a comprehensive set of finite element simulations based on single crystal plasticity theory. A range of strut thickness (t) and strut length (l) to grain diameter (d) ratios (t/d and l/d) are considered for a range of materials. The primary findings of this study are as follows:

- As regards the effects of l/d ratio, in tension, increasing the l/d ratio is predicted to lead to a reduction in strain at UTS according to a power-law behaviour. Based on the predictions of this study it is recommended that computational and experimental studies use a minimum l/d ratio of 40 in tension and 100 in bending to negate l/d ratio effects in studies on size effects in struts with few grains through their thickness.
- For t/d and l/d ratios below 10.0 and 40.0 respectively in tension and 10.0 and 100.0 in bending it is important to establish the individual contributions of t/d and l/d ratios to the overall SSE. This is achieved in this study through the development of a simple power-law model in this study. Knowledge of these individual contributions is very useful in analysing stent components where both t/d and l/d ratios are usually quite low.
- The strain at UTS in tension for struts of a given t/d and l/d ratio is predicted to scale linearly with bulk strain at UTS. This finding makes the results of this study applicable to the study of SSEs in many FCC metals.
- L605 and 316L are predicted to be subject to similar size effects in tension, despite the higher UTS of L605. This finding is of interest in modern thin-strut stent design, and suggests that size effects are a concern in L605 stent design and development.
- It is predicted that in bending increasing l/d ratios and reducing t/d ratios reduce maximum surface strain. Through the use of the measure 'surface strain' it is possible to compare the extents of geometric effects and SSEs for struts in bending. This makes the results of this study very useful in determining the trade-off in performance in bending between reducing absolute strut thickness and t/d ratio.
- Precipitates and micro-structure regularity have little influence on predicted size effects. This result is of significant interest for future modelling studies, as it facilitates the use of more easily constructed micro-structure geometries.
- Predictions of this study can be used with frameworks previously established in Harewood and McHugh (2007) to predict failure risks in a range of stent geometries, consisting of different materials and microstructures, subject to combined tensile and loading conditions.

## Acknowledgements

The authors would like to acknowledge the provision of computational resources and support by the SFI funded ICHEC and project funding through an ICRSET fellowship through the EMBARK initiative (J. Grogan).

## Appendix A

The derivation of Eq. (13) from Eq. (12) is given as follows:

For each data point:
$$
\bar{\epsilon}_{u}=\bar{\epsilon}_{u, 0}\left(\frac{d}{l}\right)^{(\beta d / t)} \tag{A1}
$$

Solving for $\beta$:
$$
\log \left(\frac{\bar{\epsilon}_{u}}{\bar{\epsilon}_{u, 0}}\right)=\left[\frac{\beta d}{t}\right] \log \left(\frac{d}{l}\right) \tag{A2}
$$

$$
\beta=\left[\frac{\log \left(\frac{\bar{\epsilon}_{u}}{\bar{\epsilon}_{u, 0}}\right)}{\log \left(\frac{d}{l}\right)}\right]\left(\frac{t}{d}\right)=\left[\log _{(d / l)}\left(\frac{\bar{\epsilon}_{u}}{\bar{\epsilon}_{u, 0}}\right)\right]\left(\frac{t}{d}\right) \tag{A3}
$$

The averaged value of $\beta$ over all three sets of $n$ data points is then given by:
$$
\beta=\frac{\sum_{j=1}^{3} \sum_{i=1}^{n} \beta_{i, j}}{3 n}=\frac{\sum_{j=1}^{3} \sum_{i=1}^{n}\left[\log _{\left(d_{i} / l_{i}\right)}\left(\frac{\bar{\epsilon}_{u, i}}{\bar{\epsilon}_{u, 0, j}}\right)\right]\left(\frac{t_{i}}{d_{i}}\right)}{3 n} \tag{A4}
$$

## REFERENCES

Armstrong, R.W., 1961. On size effects in polycrystal plasticity. Journal of the Mechanics and Physics of Solids 9, 196-199.

Armstrong, R., Codd, I., Douthwaite, R.M., Petch, N.J., 1962. The plastic deformation of polycrystalline aggregates. Philosophical Magazine 7, 45-58.

Asaro, R.J., Rice, J.R., 1977. Strain localization in ductile single crystals. Journal of the Mechanics and Physics of Solids 25, 309-338.

ASM International, 2002. Atlas of Stress-Strain Curves. ASM International, OH, USA.

Arzt, E., 1998. Size effects in materials due to microstructural and dimensional constraints: a comparative review. Acta Materialia 46, 5611-5626.

Barber, C., Bradford, D., Dobkin, P., Huhdanpaa, H., 1996. The Quickhull algorithm for convex hulls. ACM Transactions on Mathematical Software 22, 469-483.

Bayley, C.J., Brekelmans, W.A.M., Geers, M.G.D., 2007. A three-dimensional dislocation field crystal plasticity approach applied to miniaturized structures. Philosophical Magazine 87, 37-41.

Belytschko, T., Liu, W.K., Moran, B., 2000. Nonlinear Finite Elements for Continua and Structures. John Wiley and Sons Ltd., Chichester, UK.

Cao, J., Zhuang, W., Wang, S., Ho, K., Zhang, N., Lin, J., Dean., T.A., 2009. An integrated crystal plasticity FE system for microforming simulation. Journal of Multiscale Modeling 01, 107.

Chan, W.L., Fu, M.W., Lu, J., Liu, J.G., 2010. Modeling of grain size effect on micro deformation behavior in micro-forming of pure copper. Materials Science and Engineering: A 527, 6638-6648.

Chen, X.X., Ngan, A.H.W., 2011. Specimen size and grain size effects on tensile strength of Ag microwires. Scripta Materialia 64, 717-720.

Chowdhury, S.G., Das, S., Ravikumar, B., 2005. Twinning-induced sluggish evolution of texture during recrystallization in AISI

316L stainless steel after cold rolling. Metallurgical and Material Transactions A 37, 2349-2359.

Connolly, P., McHugh, P.E., 1999. Fracture modelling of WC-Co hardmetals using crystal plasticity theory and the Gurson model. Fatigue and Fracture of Engineering: Materials and Structures 22, 77-86.

DS Simulia, 2010. Abaqus 6.10 Theory Manual. DS SIMULIA Corp., Providence, RI, USA.

Engel, U., Eckstein, R., 2002. Microforming-from basic research to its realization. Journal of Materials Processing Technology 125-126, 35-44.

Estrin, Y., Tóth, L.S., Molinari, A., Bréchet, Y., 1998. A dislocation-based model for all hardening stages in large strain deformation. Acta Materialia 46, 5509-5522.

Evers, L., Brekelmans, W.A., Geers, M.G., 2004. Scale dependent crystal plasticity framework with dislocation density and grain boundary effects. International Journal of Solids and Structures 41, 5209-5230.

Fleck, N.A., Muller, G.M., Ashby, M.F., Hutchinson, J.W., 1994. Strain gradient plasticity: theory and experiment. Acta Metallurgica et Materialia 42, 475-487.

Fritzen, F., Böhlke, T., Schnack., E., 2008. Periodic three-dimensional mesh generation for crystalline aggregates based on Voronoi tessellations. Computational Mechanics 43, 701-713.

Fülöp, T., Brekelmans, W.A.M., Geers, M.G.D., 2006. Size effects from grain statistics in ultra-thin metal sheets. Journal of Materials Processing Technology 174, 233-238.

Gau, J., Principe, C., Wang, J., 2007. An experimental study on size effects on flow stress and formability of aluminium and brass microforming. Journal of Materials Processing Technology 184, 42-46.

Geers, M.G.D., Brekelmans, W.A.M., Jansen, P.J.M., 2006. Size effects in miniaturized polycrystalline FCC samples: strengthening versus weakening. International Journal of Solids and Structures 43, 7304-7321.

Ghosh, A.K., 1977. Tensile instability and necking in materials with strain hardening and strain-rate hardening. Acta Metallurgica 25, 1413-1424.

Grogan, J.A., O'Brien, B.J., Leen, S.B., McHugh, P.E., 2011. A corrosion model for bioabsorbable metallic stents. Acta Biomaterialia 7, 3523-3533.

Grogan, J.A., Leen, S.B., McHugh, P.E.., 2012. Comparing coronary stent material performance on a common geometric platform through simulated bench-testing. Journal of the Mechanical Behavior of Biomedical Materials 12, 129-138.

Haque, M.A., Saif, M.T.A., 2003. Strain gradient effect in nanoscale thin films. Acta Materialia 51, 3053-3061.

Harewood, F., Grogan, J., McHugh, P.E., 2011. A multiscale approach to failure assessment in deployment for cardiovascular stents. Journal of Multiscale Modelling 2, 1-22.

Harewood, F.J., McHugh, P.E., 2006. Investigation of finite element mesh independence in rate dependent materials. Computational Materials Science 37, 442-453.

Harewood, F.J., McHugh, P.E., 2007. Modeling of size dependent failure in cardiovascular stent struts under tension and bending. Annals of Biomedical Engineering 35, 1539-1553.

Hoefnagels, J.P.M., Janssen, P.J.M., Keijser, T.H.D., Geers, M.G.D., 2008. First-order size effects in the mechanics of miniaturized components. Applied Mechanics and Materials 14, 183-192.

Huang, Y., 1991. A User-Material Subroutine Incorporating Single Crystal Plasticity In The Abaqus Finite Element Program, Harvard University Report, MECH 178.

Jain, A., Duygulu, O., Brown, D.W., Tom, C.N., Agnew, S.R., 2008. Grain size effects on the tensile properties and deformation mechanisms of a magnesium alloy, AZ31B, sheet. Materials Science and Engineering: A 486, 545-555.

Janssen, P.J.M., de Keijser, H., Geers, M.G.D., 2006. An experimental assessment of grain size effects in the uniaxial straining of thin Al sheet with a few grains across the thickness. Materials Science and Engineering: A 419, 238-248.

Kadkhodapour, J., Butz, A., Ziaei-rad, S., Schmauder, S., 2011. A micro mechanical study on failure initiation of dual phase steels under tension using single crystal plasticity model. International Journal of Plasticity 27, 1103-1125.

Kals, T., Eckstein, R., 2000. Miniaturization in sheet metal working. Journal of Materials Processing Technology 103, 95-101.

Kastrati, A., Mehilli, J., Dirschinger, J., Dotzer, F., Schühlen, S., Neumann, F.J., Fleckenstein, M., Pfafferott, C., Seyfarth, M., Schömig, A., 2001. Intracoronary stenting and angiographic results: strut thickness effect on restenosis outcome (ISAR-STEREO) Trial. Circulation 103, 2816-2821.

Keller, C., Hug, E., Feaugas, X., 2011. Microstructural size effects on mechanical properties of high purity nickel. International Journal of Plasticity 27, 635-654.

Keller, C., Hug, E., Habraken, A.M., Duchene, L., 2012. Finite element analysis of the free surface effects on the mechanical behavior of thin nickel polycrystals. International Journal of Plasticity 29, 155-172.

Keller, C., Hug, E., Retoux, R., Feaugas, X., 2010. Mechanics of Materials TEM study of dislocation patterns in near-surface and core regions of deformed nickel polycrystals with few grains across the cross section. Mechanics of Materials 42, 44-54.

Khatibi, G., Betzwar-Kotas, A., Groger, V., Weiss, B., 2005. A study of the mechanical and fatigue properties of metallic microwires. Fatigue and Fracture of Engineering Materials and Structures 28, 723-733.

Kim, G.Y., Ni, J., Koc, M., 2007. Modeling of the size effects on the behavior of metals in microscale deformation. Journal of Manufacturing Science and Engineering 129, 470-477.

Klein, M., Hadrboletz, A., Weiss, B., Khatibi, G., 2001. The " size effect " on the stress-strain, fatigue and fracture properties of thin metallic foils. Materials Science and Engineering: A 321, 924-928.

Kuroda, M., Tvergaard, V., 2008. On the formulations of higher-order strain gradient crystal plasticity models. Journal of the Mechanics and Physics of Solids 56, 1591-1608.

Lai, X., Peng, L., Hu, P., Lan, S., Ni, J., 2008. Material behavior modelling in micro/meso-scale forming process with considering size/scale effects. Computational Materials Science 43, 1003-1009.

Lederer, M., Gröger, V., Khatibi, G., Weiss, B., 2010. Size dependency of mechanical properties of high purity aluminium foils. Materials Science and Engineering: A 527, 590-599.

Liang-ying, S.I., Cheng, L.U., Tieu, K., Xiang-hua, L.I.U., 2007. Simulation of polycrystalline aluminum tensile test with crystal plasticity finite element method. Transactions of the Nonferrous Metals Society of China 17, 1412-1416.

Lim, H., Lee, M.G., Kim, J.H., Adams, B.L., Wagoner, R.H., 2011. Simulation of polycrystal deformation with grain and grain boundary effects. International Journal of Plasticity 27, 1328-1354.

McGarry, J.P., O'Donnell, B.P., McHugh, P.E., McGarry, J.G., 2004. Analysis of the mechanical performance of a cardiovascular stent design based on micromechanical modelling. Computational Materials Science 31, 421-438.

McGarry, J.P., O'Donnell, B.P., McHugh, P.E., O'Cearbhaill, E., McMeeking, R.M., 2007. Computational examination of the effect of material inhomogeneity on the necking of stent struts under tensile loading. Journal of Applied Mechanics 74, 978-989.

Molotnikov, A., Lapovok, R., Davies, C.H.J., Cao, W., Estrin, Y., 2008. Size effect on the tensile strength of fine-grained copper. Scripta Materialia 59, 1182-1185.

Murphy, B.P., Savage, P., McHugh, P.E., Quinn, D.F., 2003. The stress-strain behavior of coronary stent struts is size dependent. Annals of Biomedical Engineering 31, 686-691.

Murphy, B.P., Cuddy, H., Harewood, F.J., Connolley, T., McHugh, P.E., 2006. The influence of grain size on the ductility of micro-scale stainless steel stent struts. Journal of Materials Science: Materials in Medicine 17, 1-6.

O'Brien, B., Carroll, W., 2009. The evolution of cardiovascular stent materials and surfaces in response to clinical drivers: a review. Acta Biomaterialia 5, 945-958.

Pache, J., Kastrati, A., Mehilli, J., Schuhlen, H., Dotzer, F., Hausleiter, J., Fleckenstein, M., et al., 2003. Intracoronary stenting and angiographic results: strut thickness effect on restenosis outcome (ISAR-STEREO-2) trial. Journal of the American College of Cardiology 41, 1283-1288.

Peirce, D., Asaro, R.J., Needleman, A., 1983. Material rate dependence and localized deformation in crystalline solids. Acta Metallurgica 31, 1951-1976.

Poncin, P., Gruez, B.,Missillier, P., Comte-Gaz, P., 2005. L605 precipitates and their effect onstent applications. In: Proceedings of the Materials & Processes for Medical Devices Conference. 14-16 November, ASM International, Boston, MA, US, pp. 85-90.

Poncin, P., Proft, J., 2003. Stent tubing: understanding the desired attributes. In: Proceedings of the Materials & Processes for Medical Devices Conference. 8-10 September, ASM International, Boston, MA, US, pp. 253-259.

Raulea, L., Goijaerts, A., Govaert, L., Baaijens, F., 2001. Size effects in the processing of thin metal sheets. Journal of Materials Processing Technology 115, 44-48.

Rice, J.R., Tracey, D.M., 1969. On the ductile enlargement of voids in triaxial stress fields. Journal of the Mechanics and Physics of Solids 17, 201-217.

Savage, P., O' Donnell, B.P., McHugh, P.E., Murphy, B., Quinn, D.F., 2004. Coronary stent strut size dependent stress-strain response investigated using micromechanical finite element models. Annals of Biomedical Engineering 32, 202-211.

Stölken, J.S., Evans, A.G., 1998. A microbend test method for measuring the plasticity length scale. Acta Materialia 46, 5109-5115.

Sweeney, C.A., McHugh, P.E., McGarry, J.P., Leen, S.B., 2012. Micromechanical methodology for fatigue in cardiovascular stents. International Journal of Fatigue 44, 202-216.

Teague, J., Cerreta, E., Stout, M., 2004. Tensile properties and microstructure of Haynes 25 alloy after aging at elevated temperatures for extended times. Metallurgical and Materials Transactions A 35, 2767-2781.

Toth, L.S., Molinari, A., Estrin, Y., 2002. Strain hardening at large strains as predicted by dislocation based polycrystal plasticity model. Journal of Engineering Materials and Technology 124, 71.

Wang, S., Zhuang, W., Balint, D.S., Lin, J., 2009. A crystal plasticity study of the necking of micro-films under tension. Journal of Multiscale Modelling 01, 331.

Weiss, S., Meissner, A., Fischer, A., 2009. Microstructural changes within similar coronary stents produced from two different austenitic steels. Journal of the Mechanical Behavior of Biomedical Materials 2, 210-216.

Weiss, S., Meissner, A., 2006. Ermüdung und Mikrostruktur von koronaren Stents. Materialwissenschaft und Werkstofftechnik 37, 755-761.

Yun, W., Peilong, D., Zhenying, X., Hua, Y., Jiangping, W., Jingjing, W., 2010. A constitutive model for thin sheet metal in micro-forming considering first order size effects. Materials and Design 31, 1010-1014.

Zhang, F., Saha, R., Huang, Y., Nix, W., Hwang, K., Qu, S., Li, M., 2007. Indentation of a hard film on a soft substrate: Strain gradient hardening effects. International Journal of Plasticity 23, 25-43.