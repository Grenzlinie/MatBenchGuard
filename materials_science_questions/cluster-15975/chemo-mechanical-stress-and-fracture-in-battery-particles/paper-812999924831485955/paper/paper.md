Accepted Manuscript

A large deformation elastic-viscoplastic model for lithium

Sooraj Narayan, Lallit Anand

![](./images/812999924831485955_1.jpg)

PII:
S2352-4316(18)30168-8
DOI:
https://doi.org/10.1016/j.eml.2018.08.006
Reference:
EML 398

To appear in:
Extreme Mechanics Letters

Received date: 24 July 2018
Revised date: 22 August 2018
Accepted date: 22 August 2018

Please cite this article as: S. Narayan, L. Anand, A large deformation elastic-viscoplastic model for lithium, Extreme Mechanics Letters (2018), https://doi.org/10.1016/j.eml.2018.08.006

This is a PDF file of an unedited manuscript that has been accepted for publication. As a service to our customers we are providing this early version of the manuscript. The manuscript will undergo copyediting, typesetting, and review of the resulting proof before it is published in its final form. Please note that during the production process errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

# A large deformation elastic-viscoplastic model for lithium

Sooraj Narayan and Lallit Anand*
Department of Mechanical Engineering
Massachusetts Institute of Technology
Cambridge, MA 02139, USA

August 22, 2018

## Abstract
An essential ingredient in modeling the response of lithium in an all-solid-state lithium battery in which a lithium metal anode is paired with a non-flammable inorganic solid electrolyte (SE), is a constitutive model for the large deformation elastic-viscoplastic response of lithium. Wang and Cheng (2017) have recently published indentation load-versus-depth data from their microindentation experiments conducted in an argon-filled glove box to study the viscoplastic behavior of lithium at room temperature. In this paper we report on a large deformation isotropic elastic-viscoplastic theory for modeling the response of lithium. We have implemented the theory as a user-material-subroutine in a finite element program, and the material parameters for the theory have been calibrated using the data from the microindentation experiments of Wang and Cheng. To exhibit the utility of our finite element simulation capability, we show results from two representative numerical simulations of relevance to modeling the mechanical interaction between a lithium anode and a SE: (a) flattening of an asperity on the surface of lithium when it is mechanically impressed by a flat ceramic SE; and (b) intrusion of lithium into a cavity on the surface of SE, when the SE is mechanically impressed into lithium with a flat surface.

Keywords: lithium; microindentation; viscoplasticity; finite element

## 1 Introduction
There is substantial ongoing world-wide research on all-solid-state lithium batteries, which have the potential to substantially improve the energy density, safety, and performance of battery systems for electric vehicles. The key components of such a battery are: (i) a pure metallic Li-anode, which has a high theoretical gravi- metric capacity of 3860 mAh/g, relative to a current generation graphitic anode, which has a capacity of only 372 mAh/g; and (ii) a non-flammable solid-electrolyte (SE) with high ionic conductivity $>rsim 10^{-3}\,\mathrm{S\,cm^{-1}}$, which also acts as the separator between the anode and the cathode. Non-flammable inorganic solid elec- trolytes, when paired with lithium metal anodes, could result in high energy density, yet safe rechargeable lithium batteries. Indeed, the successful incorporation of metallic lithium anodes in batteries is widely considered one of the major challenges in the design, manufacture, and operation of the next generation Li-battery based energy storage devices (Albertus et al., 2018).

A Li/SE interface is always present in any kind of solid-state battery, regardless of the cathode, and ensuring stable lithium plating and stripping at a Li/SE interface is of major importance for the realization of high-performance solid-state lithium batteries. A major obstacle in the operation of solid-state batteries — which must be overcome — is the redistribution of lithium and its intrusion into defects at the surface of the SE, and the subsequent growth of lithium through the electrolyte under charge-discharge cycles to cause a short-circuit.

*Tel.: +1-617-253-1635; E-mail address: anand@mit.edu

It is widely believed that lithium infiltration through the solid electrolyte may be prevented by utilizing high stiffness ceramic solid electrolytes, which will cause the deposited lithium to plastically deform and flow sideways at the Li/SE interface rather than intrude through the SE (cf., e.g., Monroe and Newman, 2005). Since the melting temperature of lithium is $\vartheta_m=453.5$ K, and since a room temperature of $\vartheta=298$ K is a high homologous temperature of $\vartheta/\vartheta_m=0.66$, the lithium is expected to deform viscoplastically and not in a rate-independent manner. The process of formation of intrusions of lithium into defects at the surface of the SE and their subsequent growth through the electrolyte to cause a short-circuit is often called "dendrite growth", but this process is not of the same nature as dendrite growth into liquid electrolytes. Lithium short-circuits through solid electrolytes occur through a fundamentally different process than through liquid electrolytes. The onset of lithium infiltration depends on the morphology of the surface of the SE, in particular the size and distribution of surface defects, the rate of lithium deposition at the Li/SE interface, the local stress state, and the viscoplastic deformation of the lithium (Porz et al., 2017; Aguesse et al., 2017). In any event, no matter what the SE, from a mechanics of materials perspective our understanding and modeling of the process of plating/stripping, redistribution, intrusion, and growth of lithium into SEs is far from complete. Much work needs to be done to develop a more complete understanding of the complex coupling between the mechanical properties of both the lithium and the SE, and battery performance.

An essential ingredient in modeling the redistribution of lithium and its intrusion into defects at the surface of the SE is a constitutive theory for the large deformation elastic-viscoplastic response of lithium. Since lithium is a very reactive and unstable material, experimental studies of its mechanical behavior are challenging. Indeed we are not aware of any reports of experimental studies in the literature on the elastic- viscoplastic response of the as-plated "mossy" lithium at a Li/SE interface. However, there have been somerecent reports of experimental studies on the mechanical behavior of other forms of lithium:

1. Wang and Cheng (2017) reported on their microindentation tests on pure lithium metal in an argon- filled glove box to study its viscoplastic behavior at a room temperature of $\vartheta\approx298$ K.$^{1}$ They conducted their microindentation experiments on commercial high-purity (99.9%) polycrystalline lithium rolled- foils, which were $750\mu$m thick.$^{2}$ The load-versus-indentation depth ($P$-$h$) curves that they obtained showed clear viscoplastic characteristics of lithium. Most of their indents were quite deep $\gtrsim5\mu$m, and the $P$-$h$ curves were relatively smooth with no strain-bursts. This indicates that multiple slip systems in one or more grains were activated during their microindentation experiments, although the grain size of the lithium in their experiments was not specified by the authors.

2. Xu et al. (2017) reported on their compression experiments on single crystalline, micron-dimensioned, lithium pillars using a nanomechanical instrument inside a SEM chamber. In their Fig. 1A they show engineering stress-strain curves at 298 K from compression experiments under a constant nominal strain-rate of $5\times10^{-3}$s$^{-1}$, on pillars with diameters ranging from $1.39\mu$m to $9.45\mu$m, and height- to-diameter ratios between 3:1 and 5:1. They defined the "yield strength" of their specimens in these experiments as the stress at which there was a first significant strain-burst; subsequent to such a strain- burst the engineering stress decreased sharply. This measure of the yield strength increases from 15 to 105 MPa as the pillar diameter decreases from 9.45 to $1.39\mu$m. In their Fig. 1B and C they show snapshots of a $1\mu$m diameter pillar during compression — the pillar was sheared off via a single slip offset. Their Fig. 1D and E shows SEM images of some representative lithium pillars deformed at room temperature, with characteristic sharp and localized slip traces. This size-dependent yield strength ofthe single crystal micropillars was 30 to 210 times larger than the reported yield strength of $\sim0.5$ MPa of bulk polycrystalline lithium at room temperature (Schultz, 2002). As discussed by Xu et al., a potential explanation for the size-dependent yield strength is a low initial dislocation density in their micropillar specimens, and that the high yield strength values reflect a dislocation-nucleation-governed plastic response.

3. Herbert and co-workers (Herbert and Hackney, 2018a; Herbert et al., 2018b,c) have recently reported on their nanoindentation experiments performed on high-purity 5 and $18\mu$m thick vapor-deposited

$^{1}$While the title of the paper by Wang and Cheng (2017) claims that they conducted "nanoindentation" experiments, most of their indents were quite deep $\gtrsim5\mu$m, and their experiments are therefore microindentation and not nanoindentation experi- ments.
$^{2}$Lithium has a bcc crystal structure, and is the least dense metal with a mass density of $0.534$ g/cm$^{3}$ under ambient conditions.

polycrystalline lithium films at 304 K. Most of their indents were $\lesssim 1000$ nm deep, within grain-interiors or near grain-boundaries, and their $P$-$h$ curves also showed strain-bursts. The estimates of the yield strength of lithium that these authors obtained from their nanoindentation experiments, was that it varied from 88 to 208 times higher than the nominal yield strength of polycrystalline lithium at room temperature — a range similar to that observed by Xu et al. (2017).

The experimental results from (i) the single crystal micropillar compression experiments by Xu et al. (2017), and (ii) the nanoindentation experiments at grain interiors by Herbert and co-workers (Herbert and Hackney, 2018a; Herbert et al., 2018b,c) both show substantial size-dependent plastic yield of lithium, possibly due to a dislocation-starved plastic deformation mechanism, when it is tested at the small scale. While these experimental results are interesting, it is not clear at present how they may be used to construct a practically useful continuum-level constitutive theory which may be used in the design of solid state batteries with lithium electrodes. Even the current generation of sophisticated strain-gradient single crystal plasticity theories (cf., e.g. Gurtin, 2002, 2008) are incapable of describing the small scale phenomena observed in the experiments of Xu et al. and Herbert et al.; perhaps a discrete-dislocation-type or a molecular-dynamics- type model might be able to reproduce some of these experimental results, but such models are at present of limited use in engineering design.

In contrast, the $P$-$h$ data from the microindentation experiments of Wang and Cheng (2017) is at larger length scale, and this data provides useful information that may be employed to construct and calibrate a continuum-level elastic-viscoplastic model for lithium. Wang and Cheng have indeed made an attempt towards this end, and proposed a one-dimensional strain- and strain-rate-dependent constitutive equation to describe the viscoplastic flow resistance of lithium, cf. their eq. (7). However, they confined their attention to modeling only the loading portion of their $P$-$h$ curves shown in Fig. 1(c) and (d) of their paper. Their model is incapable of reproducing the creep portion of the $P$-$h$ curves when the load is held constant.

It is the purpose of this brief paper to formulate a more complete three-dimensional large deformation elastic-viscoplastic theory for modeling the room temperature response of lithium. We have estimated the material parameters in our theory by conducting finite element simulations of microindentation using a user-material-subroutine (UMAT) implementation of our theory in Abaqus/Standard (Dassault Systèmes, V. 2017), and iteratively adjusting the material parameters to fit the $P$-$h$ curves from the microindentation experiments of Wang and Cheng. We show in Section 3 that when the material parameters are suitably calibrated, our model is able to satisfactorily reproduce all aspects of the $P$-$h$ curves reported by these authors. To show the utility of our finite element simulation capability, in Section 4 we present results from two representative simulations of relevance to modeling the mechanical interaction between a lithium anode and a SE: (a) flattening of an asperity on the surface of lithium when it is mechanically impressed by a ceramic SE; and (b) intrusion of lithium into a cavity on the surface of SE, when the SE is mechanically impressed into lithium with a flat surface. Finally, we close in Section 5 with some final remarks.

## 2 Theory

We limit our considerations to isothermal conditions and to circumstances under which the lithium may be adequately idealized to be an isotropic elastic-viscoplastic material. The large deformation theory considered below is based on the work by Anand and co-workers (Anand, 1982, 1985; Brown et al., 1989; Weber and Anand, 1990). The theory relates the following basic fields:³

³Notation: We use standard notation of modern continuum mechanics (Gurtin et al., 2010). Specifically: $\nabla$ and Div denote the gradient and divergence with respect to the material point $\mathbf{X}$ in the reference configuration, and $\Delta = \text{Div}\nabla$ denotes the referential Laplace operator; grad div, and div grad denote these operators with respect to the point $\mathbf{x} = \boldsymbol{\chi}(\mathbf{X}, t)$ in the deformed body; a superposed dot denotes the material time-derivative. Throughout, we write $\mathbf{F}^{e-1} = (\mathbf{F}^{e})^{-1}$, $\mathbf{F}^{e-\top} = (\mathbf{F}^{e})^{-\top}$, etc. We write $\text{tr}\,\mathbf{A}$, $\text{sym}\,\mathbf{A}$, $\text{skw}\,\mathbf{A}$, $\mathbf{A}_{0}$, and $\text{sym}_{0}\mathbf{A}$ respectively, for the trace, symmetric, skew, deviatoric, and symmetric-deviatoric parts of a tensor $\mathbf{A}$. Also, the inner product of tensors $\mathbf{A}$ and $\mathbf{B}$ is denoted by $\mathbf{A}:\mathbf{B}$, and the magnitude of $\mathbf{A}$ by $|\mathbf{A}| = \sqrt{\mathbf{A}:\mathbf{A}}$.

$\mathbf{x} = \boldsymbol{\chi}(\mathbf{X}, t),$
$\mathbf{F} = \nabla \boldsymbol{\chi},\quad J = \det \mathbf{F} > 0,$
$\mathbf{F} = \mathbf{F}^e \mathbf{F}^p,$
$\mathbf{F}^p,\quad J^p = \det \mathbf{F}^p = 1,$
$\mathbf{F}^e,\quad J^e = \det \mathbf{F}^e > 0,$
$\mathbf{F}^e = \mathbf{R}^e \mathbf{U}^e = \mathbf{V}^e \mathbf{R}^e,$
$\mathbf{U}^e = \sum_{\alpha=1}^3 \lambda_\alpha^e \mathbf{r}_\alpha^e \otimes \mathbf{r}_\alpha^e,$
$\mathbf{V}^e = \sum_{\alpha=1}^3 \lambda_\alpha^e \mathbf{l}_\alpha^e \otimes \mathbf{l}_\alpha^e$, where $\mathbf{l}_\alpha^e = \mathbf{R}^e \mathbf{r}_\alpha^e$,
$\mathbf{E}^e = \sum_{\alpha=1}^3 (\ln \lambda_\alpha^e) \mathbf{r}_\alpha^e \otimes \mathbf{r}_\alpha^e$,
$\mathbf{E}_{\mathrm{H}}^e \stackrel{\text{def}}{=} \mathbf{R}^e \mathbf{E}^e \mathbf{R}^{e \top} = \sum_{\alpha=1}^3 (\ln \lambda_\alpha^e) \mathbf{l}_\alpha^e \otimes \mathbf{l}_\alpha^e$,
$\mathbf{T} = \mathbf{T}^\top$,
$\mathbf{M}^e = J^e \mathbf{R}^{e \top} \mathbf{T} \mathbf{R}^e$,
$\mathbf{M}_0^e = \mathbf{M}^e - (1/3)(\mathrm{tr} \mathbf{M}^e)\mathbf{1}$,
$\psi$,
$S > 0$

motion;
deformation gradient;
multiplicative decomposition of $\mathbf{F}$;
plastic distortion;
elastic distortion;
polar decompositions of $\mathbf{F}^e$;
spectral decomposition of $\mathbf{U}^e$;
spectral decomposition of $\mathbf{V}^e$;
logarithmic elastic strain;
spatial logarithmic elastic strain;
Cauchy stress;
stress conjugate to logarithmic elastic strain $\mathbf{E}^e$;
deviatoric part of $\mathbf{M}^e$;
free energy per unit volume of intermediate space;
isotropic resistance to plastic flow,
an internal variable with units of stress.

### 2.1 Constitutive equations
1. **Free energy**: The free energy is taken to be given by,
$$
\psi = G |\mathbf{E}_0^e|^2 + \frac{1}{2} K |\mathrm{tr} \mathbf{E}^e|^2, \tag{2.1}
$$
where $G > 0$ and $K > 0$ are the elastic shear modulus and bulk modulus, respectively.

2. **Equation for the stress**: The stress $\mathbf{M}^e$ conjugate to the logarithmic elastic strain $\mathbf{E}^e = \ln \mathbf{U}^e$ is given by,⁴
$$
\mathbf{M}^e = \frac{\partial \psi}{\partial \mathbf{E}^e} = 2G \mathbf{E}_0^e + K(\mathrm{tr} \mathbf{E}^e)\mathbf{1}. \tag{2.2}
$$
The equivalent tensile stress which governs viscoplastic flow is defined by
$$
\bar{\sigma} \stackrel{\text{def}}{=} \sqrt{3/2} |\mathbf{M}_0^e|. \tag{2.3}
$$
The Cauchy stress $\mathbf{T}$ is given by
$$
\mathbf{T} = J^{e-1} \left[ 2G(\mathbf{E}_{\mathrm{H}}^e)_0 + K(\mathrm{tr} \mathbf{E}_{\mathrm{H}}^e)\mathbf{1} \right], \tag{2.4}
$$
where we have used the notation $\mathbf{E}_{\mathrm{H}}^e \stackrel{\text{def}}{=} \ln \mathbf{V}^e$ for the logarithmic elastic strain in the deformed body.

3. **Evolution equation for $\mathbf{F}^p$**: The evolution equation for the plastic distortion $\mathbf{F}^p$ is,
$$
\dot{\mathbf{F}}^p = \mathbf{D}^p \mathbf{F}^p, \tag{2.5}
$$
with the plastic stretching $\mathbf{D}^p$ given by
$$
\mathbf{D}^p = (3/2) \dot{\bar{\epsilon}}^p (\mathbf{M}_0^e / \bar{\sigma}), \tag{2.6}
$$
and the equivalent plastic shear strain-rate $\dot{\bar{\epsilon}}^p = \sqrt{2/3} |\mathbf{D}^p| \geq 0$ is taken to be given by a simple power-law form,
$$
\dot{\bar{\epsilon}}^p = \dot{\epsilon}_0 \left( \frac{\bar{\sigma}}{S} \right)^{1/m}. \tag{2.7}
$$
Here, $\dot{\epsilon}_0 > 0$ is a reference strain-rate, and $m \in (0, 1]$ is a strain-rate-sensitivity parameter.

⁴Since the elastic deformation of lithium is expected to be very small compared to its viscoplastic deformation, the use of a logarithmic measure of finite elastic strain is not necessary. However, we employ it here because it leads to an elegant time integration procedure for our constitutive theory (Weber and Anand, 1990).

4. Evolution equation for $S$: The flow resistance $S$ is taken to evolve according to

$$
\dot{S}=\left[H_{0}\left(1-\frac{S}{S^{*}}\right)^{a}\right] \dot{\bar{\epsilon}}^{p},
\tag{2.8}
$$

where $\{H_0, S^*, a\}$ are strain-hardening parameters, with $S^*$ representing a saturation value of $S$.

The evolution equations for $\mathbf{F}^p$ and $S$ need to be accompanied by initial conditions. Typical initial conditions presume that at time $t=0$,

$$
\mathbf{F}(\mathbf{X}, 0)=\mathbf{F}^{p}(\mathbf{X}, 0)=\mathbf{1}, \quad S(\mathbf{X}, 0)=S_{0},
\tag{2.9}
$$

so that by $\mathbf{F}=\mathbf{F}^{e} \mathbf{F}^{p}$ we also have $\mathbf{F}^{e}(\mathbf{X}, 0)=\mathbf{1}$.

To complete the constitutive model for a particular material the constitutive parameter/functions that need to be specified are

$$
\{G, K, \dot{\epsilon}_{0}, m, S_{0}, H_{0}, S^{*}, a\} \quad \text{or equivalently} \quad \{E, \nu, \dot{\epsilon}_{0}, m, S_{0}, H_{0}, S^{*}, a\},
$$

where $E$ and $\nu$ are the Young's modulus and Poisson's ratio, respectively, which are related to $G$ and $K$ by the standard relations of isotropic elasticity $E=9KG/(3K+G)$ and $\nu=(3K-2G)/(6K+2G)$, respectively.

## 3 Material parameters for lithium estimated from the microindentation experiments of Wang and Cheng

### 3.1 Elasticity parameters

The elastic constants of single crystal bcc lithium, as measured by ultrasonic pulse-echo techniques, are $C_{11}=13.42$, $C_{12}=11.3$, and $C_{44}=8.8\,\text{GPa}$ (Nash and Smith, 1959; Slotwinski and Trivisonno, 1968). The degree of departure from isotropy in the elastic response of a cubic crystal is often characterized by the **anisotropy ratio**, $AR \stackrel{\text{def}}{=} 2C_{44}/(C_{11}-C_{12})$; lithium has a very high anisotropy ratio of $AR=8.39$. Correspondingly, values of the direction-dependent Young's moduli also vary widely, e.g. $E_{<100>}=3.0\,\text{GPa}$ and $E_{<111>}=21.2\,\text{GPa}$. These values have been recently confirmed by density functional theory calculations performed by Xu et al. (2017). Herbert and Hackney (2018a) report that the Young's modulus for lithium estimated from their nanoindentation experiments on vapor deposited $5\mu\text{m}$ thick films —which are expected to be highly textured — was $E \approx 9.3\ \text{GPa}$, while that for $18\mu\text{m}$ thick films was $E \approx 8.2\ \text{GPa}$. These values compare with experimentally-measured values of $E \approx 5$ to $8\,\text{GPa}$ for bulk polycrystalline lithium at room temperature (cf., e.g., Schultz, 2002). In our own simulations of the $P$-$h$ curves obtained by Wang and Cheng for lithium, we have used

$$
E=5\,\text{GPa}, \quad \nu=0.3.
\tag{3.1}
$$

Our numerical experiments (not reported here) show that variations in the value of $E$ of the order of a few GPa had negligible influence on the simulated $P$-$h$ curves; the indentation response characteristics are dominated by the viscoplastic deformation of lithium. This relative insensitivity of simulated $P$-$h$ curves to values of $E$ has also been reported by Wang and Cheng.

### 3.2 Viscoplasticity parameters

We estimated the viscoplasticity parameters $\{\dot{\epsilon}_0, m, S_0, H_0, S^{*}, a\}$ in our theory by conducting finite element simulations of microindentation using a user-material-subroutine (UMAT) implementation of our large deformation elastic-viscoplasticity theory in Abaqus/Standard (Dassault Systèmes, V. 2017), and iteratively adjusting the material parameters to fit the $P$-$h$ curves from the microindentation experiments of Wang and Cheng (2017) shown in Fig 1. These experiments were conducted under two different load-controlled conditions, as described below.

The first set of experiments were conducted under constant indentation strain-rate conditions governed by $\dot{P}/P=c$ (a constant), so that $P=k\exp(ct)$ with the constants $c$ and $k$ given in Table 1. Once the


![](./images/812999924831485955_2.jpg)

Figure 1: Experimental load, P, versus indentation depth, h, curves: (a) at different values of $\dot{P}/P =$ constant; and (b) different values of $\dot{P} =$ constant. From Wang and Cheng (2017).

<table>
  <thead>
    <tr>
      <th>$c$, $\text{s}^{-1}$</th>
      <th>0.1</th>
      <th>0.3</th>
      <th>0.75</th>
      <th>1</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>k, mN</td>
      <td>0.0187</td>
      <td>0.0161</td>
      <td>0.0131</td>
      <td>0.009</td>
    </tr>
    <tr>
      <td>holding time, s</td>
      <td>10</td>
      <td>10</td>
      <td>10</td>
      <td>10</td>
    </tr>
    <tr>
      <td>unloading rate, $\text{mNs}^{-1}$</td>
      <td>1.18</td>
      <td>3.90</td>
      <td>12.36</td>
      <td>18.49</td>
    </tr>
  </tbody>
</table>

Table 1: Parameters for the first set of load-controlled microindentation experiments by Wang and Cheng (2017).

specified maximum load in each test was reached, it was held for 10 seconds, and this was followed by unloading at a rate listed in Table $1.^{5}$

With reference to Fig. 1(a), Wang and Cheng made the following observations: (i) Since the maximum depth in each test was larger than 8000 nm, reproducible $P$-$h$ curves were obtained in spite of a slight initial roughness of the surface of their specimens. (ii) The $P$-$h$ curves exhibit obvious rate-dependent characteristics; the load corresponding to the same depth (dashed lines in Fig. 1(a)) increases with the value of the imposed $\dot{P}/P$. (iii) The creep penetration depth during the holding period increases with the loading rate. (iv) The elastic recovery during the unloading is only a few tens of nanometers, and therefore the deformation during indentation is mainly viscoplastic.

The second set of experiments were conducted at constant loading rates $\dot{P} = c$ (a constant), with $c$ ranging from 0.196 to 3.92 mN/s to a maximum load of $P = 5.88$ mN. The subsequent holding period was set to 1 s in each indentation, and this was followed by unloading at a rate which was the negative of the loading rate. With reference to Fig. 1(b), Wang and Cheng made the following observations: (i) The $P$-$h$ curves exhibit obvious rate-dependent characteristics — the load corresponding to the same depth increases with the value of $\dot{P}$. (ii) The creep penetration depth during the holding period increases with the loading rate, and "noses" appeared at the initial part of the unloading curves. (iii) The elastic recovery during the unloading was again only few tens of nanometers, so that the deformation during indentation is mainly viscoplastic.

We used our constitutive model, as implemented in ABAQUS/Standard, to simulate the indentation experiments of Wang and Cheng shown in Fig. 1. Instead of carrying out full three-dimensional simulations of Berkovich indentation, consistent with the work of other researchers, we used an axisymmetric idealization. Specifically, we used a conical indenter with an included angle of $140.6^\circ$, which gives the same nominal contact area per unit depth as a Berkovich indenter; i.e. $A = 24.5h^2$, where $A$ is the nominal contact area and $h$ is the indentation depth. The finite element mesh used in our axisymmetric numerical simulations is shown in Fig. 2(a). The section of material modeled is $200\ \mu\text{m}$ tall and has a radius of $300\ \mu\text{m}$, which is of a sufficiently large size to minimize boundary effects for the $\lesssim 12\ \mu\text{m}$ indenter penetrations in the experiments. The block is meshed with 9375 Abaqus/CAX4H elements, and the mesh has a higher density of elements near the indenter tip where most of the deformation takes place. The mesh density was chosen such that at least 15 elements would contact the indenter (modeled as a rigid surface) at the lowest peak load of $\sim 6$ mN. The surface interaction between the lithium and the rigid conical indenter was modeled using Coulomb friction

$^{5}$The details of the experimental protocols followed in Wang and Cheng (2017) were kindly communicated to us by Mr. Yikai Wang from the University of Kentucky.

with a friction coefficient of 0.2. Fig. 2(b) shows a representative $P$-$h$ curve for $\dot{P}/P = 1\text{s}^{-1}$, while Fig. 2(c) and (d), respectively, show contours of equivalent plastic strain $\bar{\epsilon}^{p}$ and equivalent plastic strain-rate $\dot{\bar{\epsilon}}^{p}$ at the instant (i) marked on the $P$-$h$ curve in Fig. 2(b).

![](./images/812999924831485955_3.jpg)

Figure 2: (a) Finite element mesh for microindentation simulations. (b) $P$-$h$ curve for $\dot{P}/P = 1\text{s}^{-1}$. (c) Contours of equivalent plastic strain $\bar{\epsilon}^{p}$ at the instant (i) marked on the $P$-$h$ curve. (d) Contours of equivalent plastic strain-rate $\dot{\bar{\epsilon}}^{p}$ at the instant (i) marked on the $P$-$h$ curve. (e) Comparison of numerically predicted versus experimentally measured $P$-$h$ curves for different values of $\dot{P}/P = \text{constant}$. (f) Comparison of numerically predicted versus experimentally measured $P$-$h$ curves for different values of $\dot{P} = \text{constant}$. Solid lines are experimental data from Wang and Cheng and the dashed lines are numerical simulations. [Color online]

By carrying out several simulations and iteratively adjusting the values of the material parameters we obtained the results shown in Fig. 2(e) and (f). The elastic parameters used are given in eq. (3.1), and the viscoplastic material parameters used to obtain the numerically calculated $P$-$h$ curves are listed in Table 2. The material parameters were chosen to fit the constant $\dot{P}/P = c$ tests shown in Fig. 2(e) with the deeper indentations. This is because fewer microstructural and crystallographic effects come into play for the deeper indents, which is closer to the continuum plasticity approximation. The overall comparison of the numerically-calculated versus experimentally measured $P$-$h$ curves is quite good. The comparison shown in Fig. 2(f) for the shallower indents in the constant $\dot{P}$ tests is not as good as that shown in Fig. 2(e), however the calculated curves are still quite close to the experimentally-measured curves. Our heuristic procedure for calibration of the viscoplastic material parameters in our theory is briefly described in an Appendix A.

Fig. 3 shows the Cauchy or true-stress versus logarithmic or true-strain response of lithium to a strain of

<table>
<thead>
<tr>
<th>$\dot{\epsilon}_0$ s$^{-1}$</th>
<th>m</th>
<th>$S_0$ MPa</th>
<th>$H_0$ MPa</th>
<th>$S^*$ MPa</th>
<th>a</th>
</tr>
</thead>
<tbody>
<tr>
<td>0.05</td>
<td>0.18</td>
<td>2</td>
<td>40</td>
<td>8</td>
<td>1.8</td>
</tr>
</tbody>
</table>

Table 2: Estimated values for viscoplastic material parameters for lithium.

unity at different strain-rates in the range 0.1 to 1/s, predicted by the constitutive model using the material parameters in eq. (3.1) and Table 2 in a homogeneous simple compression or tension test. As is clear from this figure, lithium shows substantial strain-hardening and strain-rate sensitivity.$^6$

![](./images/812999924831485955_4.jpg)

Figure 3: Stress-strain response of lithium at different strain-rates. [Color online]

In the next section we show results from some representative numerical simulations obtained by using the finite element program Abaqus/Standard with our user-material-subroutine for elastic-viscoplasticity with material parameters calibrated for lithium.

## 4 Representative numerical simulations

In this section we show results from two representative numerical simulations of relevance to modeling the interaction between a lithium anode and a SE: (i) flattening of an asperity on the surface of lithium when it is mechanically impressed by a ceramic SE; and (ii) intrusion of lithium into a cavity on the surface of SE, when the SE is mechanically impressed into lithium with a flat surface.

### 4.1 Asperity flattening

Since the surface of the lithium in a cell may not always be perfectly flat, it is of interest to study the flattening of an asperity on the surface of lithium when it is mechanically impressed by a ceramic SE. The finite element mesh used in our numerical simulation of an asperity flattening process is shown in Fig. 4(a). This is a plane strain simulation. The section of lithium modeled is $20 \times 10\,\mu\text{m}$ with a truncated pyramidal-shaped asperity of height $2\,\mu\text{m}$, as shown in Fig. 4(a). The lithium is mechanically constrained on three sides by fixed rigid blocks, and the asperity is flattened by a rigid surface, moving at $2\,\mu\text{m/s}$, which is used to represent a ceramic SE. The block of lithium is meshed with 3078 Abaqus/CPE4H elements; the mesh has a higher density of elements in the asperity region where most of the deformation takes place. The surface interaction between the lithium and the rigid surface is modeled as frictionless. Fig. 4(b) shows the

$^6$We note that, as with any curve-fitting procedure with multiple material parameters, the values of the parameters listed in Table 2 are not unique. However, these material parameters are useful for predicting the response of lithium in engineering calculations for other geometries and boundary conditions, as long as the range of strains and strain-rates encountered in these circumstances are within that of the experiments from which the experimental data used to calibrate the material model was obtained.

force-deflection curve obtained in the asperity flattening simulation. We have marked instances (i) through (iv) on the force-deflection curve, and in Fig. 4(c) through (f) we show snapshots of the evolving asperity flattening process, and also the corresponding contours of the equivalent tensile plastic strain $\bar{\epsilon}^p$ at these selected four instances.

![](./images/812999924831485955_5.jpg)

Figure 4: (a) Finite element mesh for the asperity flattening simulation. (b) Force-deflection curve. (c) through (f) Deformed geometry and contour plots of the equivalent tensile plastic strain $\bar{\epsilon}^p$ at the instances (i) through (iv) marked in (b). [Color online]

### 4.2 Lithium intrusion

Of substantial interest is to study the intrusion of lithium into a cavity on the surface of a ceramic as the ceramic mechanically impresses the lithium. The finite element mesh used in our numerical simulation of a lithium intrusion process is shown in Fig. 5(a). This is a plane strain simulation. The lithium is modeled as $40 \times 20 \mu$m block, and the ceramic is also modeled as a $40 \times 20 \mu$m block but with a $5 \mu$m deep notch as shown in Fig. 5(a). The lithium and ceramic are mechanically constrained on three sides by fixed rigid blocks, and the right edge of the ceramic is moved at $2 \mu$m/s to the left to impress the ceramic onto the lithium. The block of lithium is meshed with 2450 Abaqus/CPE4H elements and the ceramic is meshed with 4554 Abaqus/CPE4 elements; the mesh has a higher density of elements in the cavity region where most of the deformation of the lithium takes place. The lithium is modeled using the elastic-viscoplastic model formulated in this paper, while the ceramic is modeled as an isotropic linear elastic material with $E=170$ GPa and $\nu=0.3$. Contact between all surfaces is modeled as frictionless. Fig. 5(b) shows the force deflection curve. We have marked instances (i) through (iv) on the force-deflection curve, and in Figs. 5(c) through (f) we show snapshots of evolving lithium intrusion process and also the corresponding contours of the equivalent tensile plastic strain $\bar{\epsilon}^p$ at these selected four instances (the ceramic does not deform plastically). Fig. 5(g) shows contour plots of the stress component $T_{22}$ in the ceramic at instance (iv) when the cavity is completely filled with the lithium. At this stage the stress in the ceramic has risen

to a level of 150 MPa. It is such a high tensile stress level at the root of the notch in the ceramic which can cause the ceramic to fracture.

![](./images/812999924831485955_6.jpg)

Figure 5: Finite element mesh for the lithium intrusion simulation. (b) Force-deflection curve. (c) through (f) Deformed geometry and contour plots of the equivalent tensile plastic strain $\bar{\epsilon}^p$ at the instances (i) through (iv) marked in (b). (g) The contour plots of the stress component $T_{22}$ (GPa) in the ceramic at instant (iv). [Color online]

## 5 Concluding remarks

We have formulated a large deformation isotropic elastic-viscoplastic theory for modeling the response of lithium. We have implemented the theory as a user-material-subroutine in the finite element program Abaqus/Standard, and the material parameters for the theory have been calibrated using the data from the microindentation experiments of Wang and Cheng (2017). The utility of our finite element simulation capability is demonstrated by showing results from two representative simulations of relevance to modeling the interaction between a lithium anode and a SE: (a) flattening of an asperity on the surface of lithium when it is mechanically impressed by a ceramic SE; and (b) intrusion of lithium into a cavity on the surface of SE, when the SE is mechanically impressed into lithium with a flat surface.

It would be useful to conduct an experimental program to check the predictive capabilities of our con- stitutive model and its numerical implementation, but we leave this task to others who have expertise in

conducting such experiments. An obvious need is to extend the theory to account for thermal effects. There is substantial previous work on modeling non-isothermal high-temperature viscoplasticity of metals (cf., e.g., Anand, 1982, 1985; Brown et al., 1989) which should provide theoretical guidance, but experimental data on the mechanical behavior of lithium as a function of temperature is also lacking in the literature.

Acknowledgements: A gift from Mercedes-Benz Research & Development North America, Inc. to carry out this research at MIT is gratefully acknowledged. Technical discussions regarding solid-state lithium batteries with Tobias Glossmann and Andreas Hintennach from Daimler, and Karen Thomas-Alyea from Samsung are also gratefully acknowledged.

## A Material parameter calibration procedure

In this appendix, we briefly describe our heuristic procedure for the calibration of the viscoplastic material parameters $\{\dot{\epsilon}_{0}, m, S_{0}, H_{0}, S^{*}, a\}$ in our theory from the results of the microindentation experiments of Wang and Cheng (2017). The reference strain-rate was assigned a value $\dot{\epsilon}_{0}=0.05 \mathrm{~s}^{-1}$, which lies just below the range 0.1 to $1 \mathrm{~s}^{-1}$ used in the constant indentation strain-rate experiments of Wang and Cheng. We held this value fixed throughout the fitting process. With the value of $\dot{\epsilon}_{0}$ fixed at $0.05 \mathrm{~s}^{-1}$, Fig. 6 shows how the $P$ - $h$ curves change as each of the remaining parameters $\{S_{0}, m, H_{0}, S^{*}, a\}$ is varied for a constant indentation strain-rate test of $\dot{P} / P=1 \mathrm{~s}^{-1}$. With the final values for $\{S_{0}, m, H_{0}, S^{*}, a\}$ listed in Table 2 as baseline values, for each parameter we have chosen to show $P$ - $h$ curves for three values — the final value listed in Table 2, and one smaller than and another larger than the final value. In Fig. 6(b), which shows the role of the variation of $m$, we have also shown the $P$ - $h$ curves for $\dot{P} / P=0.1 \mathrm{~s}^{-1}$ to highlight the role of the rate sensitivity parameter at a different rate. These curves provide insights on the role of each of the parameters in determining the shape of the $P$ - $h$ response, thereby aiding the curve fitting procedure.

![](./images/812999924831485955_7.jpg)

Figure 6: The effect of variation of the material parameters $\{S_{0}, m, H_{0}, S^{*}, a\}$ on the $P$ - $h$ response.

We started with reasonable estimates for the parameters $\{m, S_0, H_0, S^*, a\}$, shown in Table 3. Based on our experience in modeling high-temperature plasticity of metals, the initial guess for the strain-rate sensitivity parameter was taken as $m = 0.2$ (cf., Brown et al., 1989). Based on the yield stress value for Li reported by Schultz (2002), we took the initial value flow resistance as $S_0 = 0.5$ MPa. Further, we took the saturation value for the deformation resistance as $S^* = 2.5$ MPa, which is 5 times the initial value $S_0$. The hardening coefficient $H_0$ was chosen as $H_0 = 10$ MPa so that the deformation resistance $S$ reaches a value of $0.9S^*$ at an equivalent plastic strain of $\bar{\epsilon}^p = 0.5$. Further, based on our experience in modeling high-temperature plasticity of metals, the exponent $a$ in the evolution equation for $S$ was taken as $a = 1.4$ (cf., Brown et al., 1989).

<table>
  <thead>
    <tr>
      <th>$\dot{\epsilon}_0$ s$^{-1}$</th>
      <th>m</th>
      <th>$S_0$ MPa</th>
      <th>$H_0$ MPa</th>
      <th>$S^*$ MPa</th>
      <th>a</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0.05</td>
      <td>0.2</td>
      <td>0.5</td>
      <td>10</td>
      <td>2.5</td>
      <td>1.4</td>
    </tr>
  </tbody>
</table>

Table 3: Initial estimates for the values of the viscoplastic material parameters for Li.

![](./images/812999924831485955_8.jpg)

Figure 7: Comparison of the simulated $P$-$h$ curve using the initial estimate for the parameters against the experimental result for the $\dot{P}/P = 1$ s$^{-1}$ experiment.

Starting from the initial estimates in Table 3, we arrived at the final values of the material parameters listed in Table 2 by using the procedure described below:

(i) A simulation of the $P$-$h$ curve using the initial guess for the material parameters in Table 3 is plotted and compared against the experimental result for $\dot{P}/P = 1$ s$^{-1}$ in Fig. 7. The rising portion of the simulated curve lies well below the experimental result, and the amount of creep during the holding period is over-predicted. Fig. 6(a) shows that the shape of the ascending portions of the $P$-$h$ curves is most sensitive to the value of $S_0$, so as the first step in our curve-fitting procedure the value of $S_0$ was increased to approximately match the ascending portions of the experimentally measured $P$-$h$ curves from the different $\dot{P}/P = c$ experiments.

(ii) The next step was an attempt to fit the creep regions of the $P$-$h$ curves during the constant force stages of the experiments. Fig. 6(b) shows that the strain-rate sensitivity parameter $m$ controls the amount of creep and also the variation across the different loading rates. Accordingly the value of $m$ was then adjusted to approximate the $P$-$h$ curves during the holding creep stages of the $\dot{P}/P = c$ tests.

(iii) Next, guided by Fig. 6(c)-(e), the values of three remaining hardening parameters $\{H_0, S^*, a\}$ were adjusted so that the simulated $P$-$h$ curves better approached the complete experimentally-measured curves from the different $\dot{P}/P = c$ experiments.

(iv) With the new estimates for the parameters $\{m, S_0, H_0, S^*, a\}$, steps (i) through (iii) were repeated to improve the match of the numerically-simulated curves with the experimentally-measured curves.

(v) Once a reasonable set of values for the parameters $\{S_0, m, H_0, S^*, a\}$ was obtained by fitting the $P$-$h$ curves from the $\dot{P}/P=c$ experiments, these values were further tweaked slightly in order to also get a reasonable match with $P$-$h$ curves from the $\dot{P}=c$ experiments.

The final list of material parameters is shown in Table 2, and the final fit against the experimental data is shown in Fig. 2 (e) and (f).

Remark. We emphasize again that, as with any curve-fitting procedure with multiple material parameters, the values of the parameters listed in Table 2 are not unique.

## References

F. Aguesse, W. Manalastas, L. Buannic, J. M. Lopez del Amo, G. Singh, A. Llordes, and J. Kilner. Inves- tigating the dendritic growth during full cell cycling of garnet electrolyte in direct contact with Li metal. *ACS Applied Materials and Interfaces*, 9:3808–3816, 2017.

P. Albertus, S. Babinec, S. Litzelman, and A. Newman. Status and challenges in enabling the lithium metal electrode for high-energy and low-cost rechargeable batteries. *Nature Energy*, 3:16–21, 2018.

L. Anand. Constitutive equations for the rate-dependent deformation of metals at elevated temperatures. *ASME Journal of Engineering Materials and Technology*, 104:12–17, 1982.

L. Anand. Constitutive equations for hot-working of metals. *International Journal of Plasticity*, 1:213–231, 1985.

S. Brown, K. Kim, and L. Anand. An internal variable constitutive model for hot working of metals. *International Journal of Plasticity*, 5:95–130, 1989.

Dassault Systèmes. Abaqus FEA. Computer software, V. 2017.

M. E. Gurtin. A gradient theory of single-crystal viscoplasticity that accounts for geometrically necessary dislocations. *Journal of the Mechanics and Physics of Solids*, 50(1):5–32, 2002.

M. E. Gurtin. A finite-deformation, gradient theory of single-crystal plasticity with free energy dependent on densities of geometrically necessary dislocations. *International Journal of Plasticity*, 24(4):702–725, 2008.

M. E. Gurtin, E. Fried, and L. Anand. *The mechanics and thermodynamics of continua.* Cambridge Uni- versity Press, 2010.

E. Herbert and S. Hackney. Nanoindentation of high-purity vapor deposited lithium films: The elastic modulus. *Journal of Materials Research*, 30:1335–1346, 2018a.

E. Herbert, S. Hackney, V. Thole, N. Dudney, and P. Phani. Nanoindentation of high-purity vapor deposited lithium films: A mechanistic rationalization of diffusion-mediated flow. *Journal of Materials Research*, 30:1347–1360, 2018b.

E. Herbert, S. Hackney, V. Thole, N. Dudney, and P. Phani. Nanoindentation of high-purity vapor deposited lithium films: A mechanistic rationalization of the transition from diffusion to dislocation-mediated flow. *Journal of Materials Research*, 30:1361–1368, 2018c.

C. Monroe and J. Newman. The impact of elastic deformation on deposition kinetics at lithium/polymer interfaces. *Journal of the Electrochemical Society*, 152:A396–A404, 2005.

H. C. Nash and C. Smith. Single-crystal elastic constants of lithium. *Journal of Physics and Chemistry of Solids*, 9:113–118, 1959.

L. Porz, T. Swamy, B. W. Sheldon, D. Rettenwander, H. L. Fromling, T. Thaman, S. Berendts, R. Uecker, W. C. Carter, and Y.-M. Chiang. Mechanism of lithium metal penetration through inorganic solid elec- trolytes. *Advance d Energy Materials*, page 1701003, 2017.

R. Schultz. Measurement of young's modulus and yield strength of li. Technical Report FERMILAB-TM-2191; Fermi National Accelerator Laboratory: Batavia, IL, 2002.

T. Slotwinski and J. Trivisonno. Temperature dependence of the elastic constants of single crystal lithium. *Journal of Physics and Chemistry of Solids*, 30:1276-1279, 1968.

Y. Wang and Y. Cheng. A nanoindentaion study of the viscoplastic behavior of pure lithium. *Scripta Materialia*, 130:191-195, 2017.

G. Weber and L. Anand. Finite deformation constitutive equations, and a time integration procedure for isotropic, hyperelastic viscoplastic solids. *Computer Methods in Applied Mechanics and Engineering*, 79:173-202, 1990.

C. Xu, Z. Ahmad, A. Aranfara, V. Viswanathan, and J. Gree. Enhanced strength and temperature dependence of mechanical properties of li at small scales and its implications for li metal anodes. *Proceedings of the National Academy of Sciences*, 114:57-61, 2017.