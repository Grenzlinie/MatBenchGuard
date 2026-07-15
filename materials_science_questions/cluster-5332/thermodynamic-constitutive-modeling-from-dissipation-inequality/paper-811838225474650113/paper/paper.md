![](./images/811838225474650113_1.jpg)

# Experimental and theoretical investigation of a polymer subjected to cyclic loading conditions

A. Ramkumar $^{a}$, K. Kannan $^{a,*}$, R. Gnanamoorthy $^{b}$

$^{a}$ Department of Mechanical Engineering, Indian Institute of Technology Madras, Chennai 600 036, India
$^{b}$ Indian Institute of Information Technology, Design and Manufacturing (IIITD&M Kancheepuram), Indian Institute of Technology Madras Campus, Chennai 600 036, India

---

### ARTICLE INFO

**Article history:**
Received 3 July 2009
Accepted 13 July 2009
Available online 19 August 2009

Communicated by K.R. Rajagopal

**Keywords:**
Dissipation
Polymer
Viscoelasticity
Stress relaxation
Cyclic loading
Thermodynamical framework
Constitutive equation

---

### ABSTRACT

There are many machine components made of polymeric materials, such as gears, which are subjected to cyclic loading conditions. To design such components, it is necessary to arrive at a suitable mathematical model that can describe the mechanical response of polymeric materials. In this paper, we derive a mathematical model for rate-type solids using thermodynamical framework developed by Rajagopal and Srinivasa (K.R. Rajagopal, A.R. Srinivasa, A thermodynamic frame work for rate type fluid model, Journal of Non-Newtonian Fluid Mechanics 88 (2000) 207–227) (also see Section 5 of Kannan and Rajagopal (K. Kannan, K.R. Rajagopal, A thermomechanical framework for the transition of a viscoelastic liquid to a viscoelastic solid, Mathematics and Mechanics of Solids 9 (2004) 37–59)), which was used by Rajagopal and Srinivasa to derive a mathematical model for isotropic, rate-type liquids. Uniaxial cyclic loading and stress relaxation experiments were conducted. The predictions of the model agreed well with the experimental data.

© 2009 Elsevier Ltd. All rights reserved.

---

## 1. Introduction

Machine components made of polymers have several advantages, namely, good strength to weight ratio, operate with reduced noise emanations, and exhibit good resistance to environmental conditions compared to that of metals. Their fields of applications, however, are rather limited owing to the lack of 'strength' and 'stiffness'. These materials dissipate part of the mechanical energy in the thermal form, and because of its poor thermal diffusivity, one can observe a significant rise in temperature when these materials are subjected to cyclic loading. Such a situation arises in gears made of plastics. The gear tooth experiences cyclic loading during service and dissipates heat, which results in the loss of 'strength'. Eventually, a stage will be reached where a gear tooth cannot support the load, and fail before the designed service life. Therefore, it is essential to predict the temperature rise (or the amount of dissipated energy) to prevent the premature failure of the components. To that end, we mathematically model plastics as viscoelastic solid. Such an approach obviates the need for performing full scale experiments to design components made of plastics. This paper describes the derivation of an appropriate model for a polymer based on a thermodynamic framework, and prediction of its mechanical response. The effect of temperature on mechanical response of the polymer is not included in this model. However, one can calculate the amount of dissipated energy using such models.

Numerous studies have contributed to the development of mathematical formulations and numerical methods, allowing precise simulation of behavior of viscoelastic materials. Boukamel et al. [1] presented a model to simulate the

---

* Corresponding author. Tel.: +91 44 2257 4708.
E-mail addresses: ramkumar3.a@tcs.com (A. Ramkumar), krishnakannan@iitm.ac.in (K. Kannan), gmoorthy@iiitdm.ac.in (R. Gnanamoorthy).

0020-7225/$ - see front matter © 2009 Elsevier Ltd. All rights reserved.
doi:10.1016/j.ijengsci.2009.07.002
![](./images/811838225474650113_2.jpg)

### Nomenclature

| Symbol | Definition |
|--------|------------|
| $a_0$ | original cross-sectional area of the test specimen |
| $f_z$ | the component of force along $z$-direction |
| $t$ | time |
| $\kappa_R(B)$ | reference configuration |
| $\kappa_t(B)$ | current configuration |
| $X_{\kappa_R}$ | a position in the reference configuration |
| $x$ | a position in the current configuration |
| $\boldsymbol{v}$ | the velocity of a particle |
| $\boldsymbol{F}_{\kappa_R}$ | deformation gradient tensor |
| $\boldsymbol{F}_{\kappa_{p(t)}}$ | a mapping from $\kappa_{p(t)}(B)$ to $\kappa_t(B)$ |
| $\boldsymbol{G}$ | a mapping from $\kappa_R(B)$ to $\kappa_{p(t)}(B)$ |
| $\boldsymbol{L}$ | velocity gradient tensor |
| $\boldsymbol{D}$ | symmetric part of velocity gradient tensor |
| $\boldsymbol{B}_{\kappa_R}$ | left Cauchy-Green stretch tensor defined with respect to $\kappa_R(B)$ |
| $\boldsymbol{B}_{\kappa_{p(t)}}$ | left Cauchy-Green stretch tensor defined with respect to $\kappa_{p(t)}(B)$ |
| $\mathrm{I}_{\kappa_R}, \mathrm{II}_{\kappa_R}, \mathrm{III}_{\kappa_R}$ | principal invariants of $\boldsymbol{B}_{\kappa_R}$ |
| $\mathrm{I}_{\kappa_{p(t)}}, \mathrm{II}_{\kappa_{p(t)}}, \mathrm{III}_{\kappa_{p(t)}}$ | principal invariants of $\boldsymbol{B}_{\kappa_{p(t)}}$ |
| $B(t)$ | component of the left Cauchy-Green stretch tensor |
| $\boldsymbol{C}_{\kappa_R}$ | right Cauchy-Green stretch tensor defined with respect to $\kappa_R(B)$ |
| $p$ | Lagrange multiplier |
| $\boldsymbol{T}$ | Cauchy stress tensor |
| $T_{ZZ}$ | a component of stress tensor |
| $\lambda$ | stretch along loading direction |
| $\rho$ | density of the material |
| $\xi$ | rate of dissipation per unit volume |
| $\psi$ | Helmholtz potential per unit mass |
| $\boldsymbol{q}$ | heat flux vector |
| $r$ | radiant heating |
| $\varepsilon$ | internal energy |
| $\boldsymbol{b}$ | specific body force |
| $\beta$ | a constant associated with the model |
| $\mu_1$ | shear modulus associated with the model |
| $\mu_2$ | shear modulus associated with the model |
| $v$ | viscosity associated with the model |

thermomechanical behavior of viscoelastic elastomers under large strain. A formulation was proposed with a generalization to large strain of the Poynting-Thompson rheological model. Authors demonstrated the capability of the model by conducting cyclic shearing experiments on a two piece elastomer-steel specimens. Holzapfel and Reiter [2] formulated a constitutive equation based on a four-parameter viscoelastic model and performed numerical simulations of thermomechanical processes for linear viscoelastic solids. The basic local governing equations of thermoelasticity were formulated based on an additive decomposition of the mechanical work rate into a reversible part and the dissipative part. The authors presented numerical simulations of the behavior of viscoelastic material through selected examples. Simulations were performed using an implicit time integration method and the standard isoparametric finite element concept to discretize the time and position dependent thermodynamic state variables.

In particular, a number of studies focusing on simulation of mechanical response of soft biological tissues are reported. Nasseri et al. [3] studied the viscoelastic response of soft biological tissues by conducting a series of rheological tests. In that study, a model that uses a multi mode upper convected Maxwell model with variable viscosities and time constants along with Mooney hyperelastic response was developed and used for predictions. The model was found capable of predicting the experimental data reasonably well. Yang et al. [4] investigated the time dependant responses of porcine esophagus tissue using stress relaxation and cyclic tests and predicted its viscoelastic response using Fung's quasilinear viscoelastic model (QLV). The model was found to predict the cyclic peak stress and the hysterisis but under estimates the valley stress. Anand and Rajagopal [5] developed a viscoelastic fluid model for the flow of blood within the thermodynamic framework consisting of four independent parameters that characterizes the elasticity, the viscosity of the plasma, the formation of rouleaus and their effect on the viscosity of blood, and the shear thinning that takes place during the flow. The model was found to be capable of predicting exceptionally well the steady flow and oscillatory flow experimental data.

The dissipative nature of the viscoelastic materials results in internal heat generation, and therefore, temperature evolution takes place in a material. This thermo-viscoelastic coupling phenomenon was reported by several authors. Tauchert [6] presented a consistent thermodynamic approach to the solution of problems in coupled thermo-viscoelasticity, and

illustrated the interaction between the thermal and deformation fields in a viscoelastic media. A coupled energy equation was used to calculate the transient and steady state temperature distributions in a thin-walled tube subjected to torsional oscillations. Young [7] studied the one-dimensional forced vibration analysis of a thermo-viscoelastic rod taking in to account the temperature dependency of mechanical properties and the resulting thermomechanical coupling effects. The author used the finite difference formulation to predict the steady state response of the material without taking in to account the initial transient behavior and performed simulation for Lockheed solid propellant. Sridhar et al. [8] developed a finite element procedure to estimate the temperature rise during cyclic loading of hyperelastic materials. A transient heat conduction analysis was carried out to estimate the temperature rise for different time steps in rubber-like materials using Galerkin's formulations. The authors presented a numerical example and found that the computed temperature values for various load steps agree closely with the experimental results reported in the literature. Kaliske and Rothert [9] proposed a three-dimensional viscoelastic approach to solve problems involving small and large strains. Authors used generalized Maxwell's model as the underlying constitutive structure and implemented finite element method to simulate the time dependant deformations of rubber-like structures.

It is important to note that a thermodynamical framework encompassing a larger class of materials, namely materials with implicit constitutive equations, has been developed (see [10-12]). Such models are rich, in that a wider variety of phenomenon can be studied using such models. In the present study, however, simulation of the stress relaxation and strain controlled cyclic response of a viscoelastic material (polyamide 6) using a non-linear, three-dimensional viscoelastic model is undertaken using a model derived from a thermodynamic framework (see [13]). The material is assumed to be isotropic and incompressible. Such a model has explicit constitutive equation for stress tensor.

## 2. Experimental

### 2.1. Materials and processing

Polyamide 6 has been one of the commonly used engineering plastics and is known for its wide range of applications. Polyamide 6 (PA6) has been extensively used in electronics, consumer products and engineering parts. Bearings, gears, bushings are some of the load bearing applications where PA6 find its presence. Test specimens were fabricated according to ASTM D638 (TYPE 4) standard by injection molding process. Gauge length of the specimen is 25 mm. The die is designed in such a way that the provisions for gate and the ejector pin are not located in the gauge section. Polyamide pellets were dried at 333 K for 4 h in a hot air oven to remove the moisture. The injection moulding was carried out in a Macfield injection molding machine at an injection pressure of 125 MPa and a temperature of 513 K with the mould temperature of 308 K.

### 2.2. Test methodology

Stress relaxation tests and a displacement controlled cyclic loading test were conducted using the injection moulded polyamide 6 samples to demonstrate the capability of the model. Prior to testing, PA6 specimens were dried at 333 K for 2 h in a hot air oven to relieve the internal stresses. Fig. 1 shows the photograph of the test sample along with the extensometer. During stress relaxation tests, the specimens were subjected to a linear ramp loading, followed by holding the cross-head at constant displacement. The cross-head displacement, extensometer opening distance, and the force were recorded as a

![](./images/811838225474650113_3.jpg)

Fig. 1. Photograph of ASTM D638 (TYPE 4) specimen along with an extensometer.

<table>
<caption>Table 1 Test conditions followed for the stress relaxation tests.</caption>
<thead>
<tr>
<th>Specimen no.</th>
<th>Strain</th>
<th>Stretch rate (s<sup>−1</sup>)</th>
<th>Cross-head velocity (mm/min)</th>
<th>Permanent strain experience</th>
</tr>
</thead>
<tbody>
<tr>
<td>1</td>
<td>0.05</td>
<td>0.0325</td>
<td>100</td>
<td>No</td>
</tr>
<tr>
<td>2</td>
<td>0.06</td>
<td>0.0423</td>
<td>120</td>
<td>No</td>
</tr>
<tr>
<td>3</td>
<td>0.07</td>
<td>0.0325</td>
<td>100</td>
<td>No</td>
</tr>
<tr>
<td>4</td>
<td>0.07</td>
<td>0.0176</td>
<td>50</td>
<td>No</td>
</tr>
<tr>
<td>5</td>
<td>0.08</td>
<td>0.0008</td>
<td>2.4</td>
<td>No</td>
</tr>
<tr>
<td>6</td>
<td>0.09</td>
<td>0.0325</td>
<td>100</td>
<td>Yes</td>
</tr>
</tbody>
</table>

function of time. Six tests at different strain levels and cross-head velocity were conducted, and the details of which are summarized in Table 1. After a stress relaxation experiment, the specimen is unloaded and allowed to recover at room conditions. Given sufficient time, some samples recover its original dimension. Only the samples which resulted in zero permanent strain in the specimen were considered. The specimens that were expected to exhibit a longer recovery period were annealed at 333 K for 1 h to accelerate the recovery process. The specimens that did not exhibit a complete recovery were discarded. In another experiment, displacement controlled axial cyclic loading tests were conducted using MTS servo hydraulic test machine. Specimens were subjected to cyclic loading condition with a peak strain of 0.06 and a strain ratio of 0.1 at a frequency of 0.4 Hz using ramp signal (linear increase). An extensometer was used to record the deformation in the gauge section of the specimen. The same procedure was adopted for all the specimens with regard to the recovery process.

### 3. Theory

#### 3.1. Kinematics

Let $\kappa_R(B)$ denote the reference configuration and $\kappa_t(B)$ denote the current configuration of a viscoelastic solid of interest (see Fig. 2). The motion $\boldsymbol{\chi}_{\kappa R}$ is a mapping that, at time $t$, assigns to each position $\boldsymbol{X}_{\kappa_R}$ in the reference configuration, a corresponding position $\boldsymbol{x}$ in the current configuration, i.e.,
$$
\boldsymbol{x}=\boldsymbol{\chi}_{\kappa_{R}}\left(\boldsymbol{X}_{\kappa_{R}}, t\right). \tag{1}
$$

Henceforth, for simplicity, we shall drop the argument $B$ in $\kappa_R(B)$, $\kappa_t(B)$, and so forth.

The velocity of a particle is defined through
$$
\boldsymbol{v}=\frac{\partial \boldsymbol{\chi}_{\kappa R}}{\partial t}. \tag{2}
$$

The deformation gradient $\boldsymbol{F}_{\kappa R}$, the left and right Cauchy-Green stretch tensors $\boldsymbol{B}_{\kappa_R}$ and $\boldsymbol{C}_{\kappa_R}$ are defined through
$$
\boldsymbol{F}_{\kappa R}:=\frac{\partial \boldsymbol{\chi}_{\kappa R}}{\partial \boldsymbol{X}_{\kappa R}}, \quad \boldsymbol{B}_{\kappa_{R}}=\boldsymbol{F}_{\kappa_{R}} \boldsymbol{F}_{\kappa_{R}}^{T} \quad \text { and } \quad \boldsymbol{C}_{\kappa_{R}}=\boldsymbol{F}_{\kappa_{R}}^{T} \boldsymbol{F}_{\kappa_{R}}. \tag{3}
$$

The principal invariants of $\boldsymbol{B}_{\kappa_R}$ are
$$
\mathrm{I}_{\kappa_{R}}=\operatorname{tr}\left(\boldsymbol{B}_{\kappa_{R}}\right), \quad \mathrm{II}_{\kappa_{R}}=\frac{1}{2}\left\{\left[\operatorname{tr}\left(\boldsymbol{B}_{\kappa_{R}}\right)\right]^{2}-\operatorname{tr}\left(\boldsymbol{B}_{\kappa_{R}}^{2}\right)\right\} \quad \text { and } \quad \mathrm{III}_{\kappa_{R}}=\operatorname{det}\left(\boldsymbol{B}_{\kappa_{R}}\right). \tag{4}
$$

![](./images/811838225474650113_4.jpg)

Fig. 2. Schematic diagram illustrating the notion of various configurations related to a viscoelastic material.

The left and the right Cauchy-Green stretch tensors associated with the tensor $\boldsymbol{F}_{\kappa_{p(t)}}$, i.e., the mapping between the tangent spaces at the appropriate points belonging to the configurations $\kappa_{p(t)}$ and $\kappa_{t}$ are defined through

$$
\boldsymbol{B}_{\kappa_{p(t)}}=\boldsymbol{F}_{\kappa_{p(t)}} \boldsymbol{F}_{\kappa_{p(t)}}^{T} \quad \text { and } \quad \boldsymbol{C}_{\kappa_{p(t)}}=\boldsymbol{F}_{\kappa_{p(t)}}^{T} \boldsymbol{F}_{\kappa_{p(t)}},
$$

respectively.

Accordingly, the principal invariants of the tensor $\boldsymbol{B}_{\kappa_{p(t)}}$ are denoted by $\mathrm{I}_{\kappa_{p(t)}}, \mathrm{II}_{\kappa_{p(t)}}$ and $\mathrm{III}_{\kappa_{p(t)}}$, and are defined through

$$
\mathrm{I}_{\kappa_{p(t)}}=\operatorname{tr}\left(\boldsymbol{B}_{\kappa_{p(t)}}\right), \quad \mathrm{II}_{\kappa_{p(t)}}=\frac{1}{2}\left\{\left[\operatorname{tr}\left(\boldsymbol{B}_{\kappa_{p(t)}}\right)\right]^{2}-\operatorname{tr}\left(\boldsymbol{B}_{\kappa_{p(t)}}^{2}\right)\right\} \quad \text { and } \quad \mathrm{III}_{\kappa_{p(t)}}=\operatorname{det}\left(\boldsymbol{B}_{\kappa_{p(t)}}\right).
$$

The mapping $\boldsymbol{G}$ is defined through

$$
\boldsymbol{G}=\boldsymbol{F}_{\kappa_{R} \rightarrow \kappa_{p(t)}}=\boldsymbol{F}_{\kappa_{p(t)}}^{-1} \boldsymbol{F}_{\kappa_{R}}
$$

and the velocity gradient $\boldsymbol{L}$ and the mapping $\boldsymbol{L}_{\kappa_{p(t)}}$ are defined through

$$
\boldsymbol{L}=\left.\dot{\boldsymbol{F}}_{\kappa_{R}}\right|_{\boldsymbol{X}_{\kappa_{R}}=\mathrm{const}} \boldsymbol{F}_{\kappa_{R}}^{-1} \quad \text { and } \quad \boldsymbol{L}_{\kappa_{p(t)}}=\dot{\boldsymbol{G}} \boldsymbol{G}^{-1}.
$$

The symmetric parts of $\boldsymbol{L}$ and $\boldsymbol{L}_{\kappa_{p(t)}}$ are defined through

$$
\boldsymbol{D}=\frac{1}{2}\left[\boldsymbol{L}+\boldsymbol{L}^{T}\right] \quad \text { and } \quad \boldsymbol{D}_{\kappa_{p(t)}}=\frac{1}{2}\left[\boldsymbol{L}_{\kappa_{p(t)}}+\boldsymbol{L}_{\kappa_{p(t)}}^{T}\right].
$$

The upper convected Oldroyd derivative of $\boldsymbol{B}_{\kappa_{p(t)}}$ is defined through

$$
\stackrel{\nabla}{\boldsymbol{B}}_{\kappa_{p(t)}}=\dot{\boldsymbol{B}}_{\kappa_{p(t)}}-\boldsymbol{L} \boldsymbol{B}_{\kappa_{p(t)}}-\boldsymbol{B}_{\kappa_{p(t)}} \boldsymbol{L}^{T}=-2 \boldsymbol{F}_{\kappa_{p(t)}} \boldsymbol{D}_{\kappa_{p(t)}} \boldsymbol{F}_{\kappa_{p(t)}}^{T}.
$$

Assuming the material to be incompressible, i.e., we require that

$$
\operatorname{det}\left(\boldsymbol{B}_{\kappa_{p(t)}}\right)=1 \quad \text { and } \quad \operatorname{tr}[\boldsymbol{L}]=0.
$$

### 3.2. Balance equations

For the sake of completeness, the balance equations are briefly described.

As usual, all the balance equations are formulated for arbitrary sub-parts of a body, and by assuming continuity of integrand, one arrives at balance equations in the local form. In this section, the balance equations in the local form are presented.

#### 3.2.1. Mass balance

The balance of mass for a material with no inter conversion of constituents is given through

$$
\frac{\partial \rho}{\partial t}+\operatorname{div}(\rho \boldsymbol{v})=0,
$$

where $\rho$ is the local density of a material. The mass balance equation is represented in Eulerian form. If a material is incompressible, then the above equation reduces to that of $\operatorname{div}(\boldsymbol{v})=0$.

#### 3.2.2. Linear momentum balance

The balance of linear momentum in Eulerian form is given through

$$
\rho\left(\frac{\partial \boldsymbol{v}}{\partial t}+[\operatorname{grad}(\boldsymbol{v})] \boldsymbol{v}\right)=\operatorname{div}\left(\boldsymbol{T}^{T}\right)+\rho \boldsymbol{b},
$$

where $\boldsymbol{T}$ is Cauchy stress tensor and $\boldsymbol{b}$ is specific body force.

#### 3.2.3. Angular momentum balance

One can show that the consequence of balance of angular momentum, in the absence of body couples, leads to

$$
\boldsymbol{T}=\boldsymbol{T}^{T},
$$

i.e., the Cauchy stress tensor is symmetric.

#### 3.2.4. Balance of energy

One can show that balance of energy in the local form leads to

$$
\rho \dot{\varepsilon}+\operatorname{div}(\boldsymbol{q})=\boldsymbol{T} \cdot \boldsymbol{D}+\rho r,
$$

where $\varepsilon$ is the internal energy, $\boldsymbol{q}$ is the heat flux vector, and $r$ is the radiant heating.

### 3.3. Constitutive equations

In addition to balance equations, one has to propose additional set of equations called constitutive equations to 'close' the balance equations. Depending on the class of material under consideration, constitutive equations are proposed by relating appropriate variables. The functional form of constitutive equations are determined such that the second law of thermodynamics, material symmetry, frame-indifference and other constraints, if any, are met.

In this paper, we shall obtain constitutive equations for homogeneous, isotropic viscoelastic solids subject to homothermal process, i.e., every point belonging to such a material is at a uniform temperature. Further, we shall assume that this material is incompressible. Here, we use the framework developed by Rajagopal and Srinivasa [14] to develop constitutive equations for viscoelastic solids. In this framework, one specifies how a material stores energy and dissipates energy, the functional form being constrained by the requirements of frame-indifference and material symmetry. A viscoelastic solid is modeled as a one-parameter family of elastic material with respect to an evolving configuration $\kappa_{p(t)}$, and an elastic solid with respect to the reference configuration $\kappa_{R}$. The evolving configuration is akin to microstructural rearrangement of polymer molecules that occurs during deformation. To determine the stress at any point $\boldsymbol{x}$ in the current configuration, one needs to know where $\kappa_{p(t)}$ is. It turns out that, there are infinity of evolution equations that describe how $\kappa_{p(t)}$ evolves. We, further, assume that $\kappa_{p(t)}$ evolves in such a way that the rate of dissipation function is maximized. Such a mathematical model obtained using this framework can describe the mechanical response of an isotropic viscoelastic solid.

We shall only present the constraint of the second law of thermodynamics on constitutive equation for the stress tensor, and refer the reader to Rajagopal and Srinivasa [14] for a more detailed description of thermodynamical framework.

#### 3.3.1. Second law of thermodynamics

For a body undergoing a thermomechanical process, second law of thermodynamics is introduced in the following form (see [14]):

$$
\xi = \boldsymbol{T} \cdot \boldsymbol{D} - \rho \dot{\psi}, \tag{16}
$$

where $\psi$ is Helmholtz potential per unit mass, $\rho$ is the density of the material and $\xi$ is the rate of dissipation per unit volume.

Helmholtz potential per unit mass and the rate of dissipation per unit volume, $\xi$, of the solid are defined as follows:

$$
\psi = \frac{\mu_1}{2\rho}(\text{tr}(\boldsymbol{B}_{\kappa_{p(t)}})-3) + \frac{\mu_2}{2\rho}(\text{tr}(\boldsymbol{B}_{\kappa_{R}})-3), \tag{17}
$$

where $\mu_1$ and $\mu_2$ are the material constants and

$$
\xi = 2v(\boldsymbol{D}_{\kappa_{p(t)}} \cdot \boldsymbol{B}_{\kappa_{p(t)}} \boldsymbol{D}_{\kappa_{p(t)}})^{\beta}, \tag{18}
$$

where $v$ is the viscosity and $\beta$ is a constant. The above definition for the rate of dissipation guarantees that it will always be non-negative. Further, it is zero whenever $\boldsymbol{D}_{\kappa_{p(t)}} = \boldsymbol{0}$.

By substituting $\psi$ in to the above equation, one arrives at

$$
\begin{aligned}
2v(\boldsymbol{D}_{\kappa_{p(t)}} \cdot \boldsymbol{B}_{\kappa_{p(t)}} \boldsymbol{D}_{\kappa_{p(t)}})^{\beta} &= \boldsymbol{T} \cdot \boldsymbol{D} - \rho \left\{ \frac{\mu_1}{2\rho} \left( 2\boldsymbol{B}_{\kappa_{p(t)}} \cdot (\boldsymbol{D} - \boldsymbol{D}_{\kappa_{p(t)}}) \right) + \frac{\mu_2}{2\rho} 2\boldsymbol{B}_{\kappa_{R}} \cdot \boldsymbol{D} \right\} \\
&= \left( \boldsymbol{T} - \mu_1 \boldsymbol{B}_{\kappa_{p(t)}} - \mu_2 \boldsymbol{B}_{\kappa_{R}} \right) \cdot \boldsymbol{D} + \mu_1 \boldsymbol{B}_{\kappa_{p(t)}} \cdot \boldsymbol{D}_{\kappa_{p(t)}}.
\end{aligned} \tag{19}
$$

One way to satisfy the above equation, i.e., a sufficient condition, is to let the stress tensor to be

$$
\boldsymbol{T} = -p\boldsymbol{I} + \mu_1 \boldsymbol{B}_{\kappa_{p(t)}} + \mu_2 \boldsymbol{B}_{\kappa_{R}}, \tag{20}
$$

where $p$ is the Lagrange multiplier, which is introduced as a result of incompressibility constraint, i.e., Eq. (11).

As a result of the above equation, Eq. (19) becomes

$$
2v(\boldsymbol{D}_{\kappa_{p(t)}} \cdot \boldsymbol{B}_{\kappa_{p(t)}} \boldsymbol{D}_{\kappa_{p(t)}})^{\beta} = \mu_1 \boldsymbol{B}_{\kappa_{p(t)}} \cdot \boldsymbol{D}_{\kappa_{p(t)}}. \tag{21}
$$

To determine the stress at any point in the current configuration $\kappa_{p(t)}$ (see Fig. 2), one needs to know how $\kappa_{p(t)}$ is evolving. To that end, Eq. (21) provides a constraint on the tensors $\boldsymbol{B}_{\kappa_{p(t)}}$ and $\boldsymbol{D}_{\kappa_{p(t)}}$. It is clear from Eq. (10) that if $\boldsymbol{D}_{\kappa_{p(t)}}$ is related to $\boldsymbol{B}_{\kappa_{p(t)}}$ through a function of type $\boldsymbol{D}_{\kappa_{p(t)}} = \boldsymbol{f}(\boldsymbol{B}_{\kappa_{p(t)}})$, where $\boldsymbol{f}$ is some known tensor valued function, then $\boldsymbol{B}_{\kappa_{p(t)}}$ can be computed as a function of time. However, the function $\boldsymbol{f}$ has to satisfy two constraints, one of which is Eq. (21) and the other is the incompressibility constraint $\text{tr}(\boldsymbol{D}_{\kappa_{p(t)}}) = 0$. Obviously, many functions can be arrived at, which satisfies these constraints. By assuming that $\boldsymbol{B}_{\kappa_{p(t)}}$ evolves in such a way that it maximizes the rate of dissipation, we pick an evolution equation from infinitely many choices. To that end, we maximize the rate of dissipation subject to the constraints equations (11) and (21), i.e.,

$$
\phi = \xi + \lambda_1 \left( 2v(\boldsymbol{D}_{\kappa_{p(t)}} \cdot \boldsymbol{B}_{\kappa_{p(t)}} \boldsymbol{D}_{\kappa_{p(t)}})^{\beta} - \mu_1 \boldsymbol{B}_{\kappa_{p(t)}} \cdot \boldsymbol{D}_{\kappa_{p(t)}} \right) + \lambda_2 \text{tr}(\boldsymbol{D}_{\kappa_{p(t)}}), \tag{22}
$$

where $\lambda_1$ and $\lambda_2$ are Lagrange multipliers.

One can show that by letting $\frac{\partial \phi}{\partial \boldsymbol{F}_{\kappa_{p(t)}}}=0$, using Eq. (10) and the fact that the material behaves like an isotropic material with respect to the configuration $\kappa_{p(t)}$, i.e., we can set $\boldsymbol{F}_{\kappa_{p(t)}}=\boldsymbol{V}_{\kappa_{p(t)}}$, where $\boldsymbol{V}_{\kappa_{p(t)}}$ is left stretch tensor associated with $\boldsymbol{F}_{\kappa_{p(t)}}$, one arrives at the following evolution equation for $\boldsymbol{B}_{\kappa_{p(t)}}$:

$$
\stackrel{\nabla}{\boldsymbol{B}}_{\kappa_{p(t)}}=2\left\{\left(\frac{\mu_{1}}{2 v}\right)^{1 /(2 \beta-1)}\left[\operatorname{tr}\left(\boldsymbol{B}_{\kappa_{p(t)}}\right)-\frac{9}{\operatorname{tr}\left(\boldsymbol{B}_{\kappa_{p(t)}}^{-1}\right)}\right]^{\frac{1-\beta}{(2 \beta-1)}}\right\} \times\left[\frac{3}{\operatorname{tr}\left(\boldsymbol{B}_{\kappa_{p(t)}}^{-1}\right)} \boldsymbol{I}-\boldsymbol{B}_{\kappa_{p(t)}}\right].\tag{23}
$$

Further, we can show that the above equation, which describes the evolution equation for configuration $\kappa_{p(t)}$ maximizes the rate of dissipation for $\beta>0.5$ (see [13]). Eqs. (20) and (23) describe the constitutive equation for the stress tensor. Eqs. (12), (13), (20) and (23) form the governing equations for a homogeneous, isotropic, incompressible viscoelastic solid. In addition to governing equations, one need to supply suitable boundary and initial conditions.

It is noteworthy to mention that if the elastic deformation is 'small', i.e., $\left\|B_{\kappa_{p(t)}}-I\right\|=o(\varepsilon), \varepsilon \ll 1$, and by setting $\beta=1$, one recovers the three-dimensional form of standard linear solid (see [13]), which on specialization to one dimension, one recovers the constitutive equation of a standard linear solid derived from mechanical analogs. Karra and Rajagopal [15] showed that it is possible to construct many three-dimensional models for viscoelastic materials, all of which reduce to the same one-dimensional form if $\left\|B_{\kappa_{p(t)}}-I\right\|=o(\varepsilon), \varepsilon \ll 1$. Table 1 indicates that the total strain undergone by the specimen is small and is clear that 'small' elastic deformation condition is met. This, however, implies that while the model developed in this paper fits the experimental data very well (see Figs. 3 and 4), it may be inadequate to describe the mechanical response of the same material under general three-dimensional loading conditions.

## 4. An application of the developed model for prediction of viscoelastic response of polyamide 6

In general, one need to solve the full system of governing equations, i.e., a system of partial differential equations (PDE's), to obtain the mechanical response, which is quite cumbersome. Instead, one could adopt a semi-inverse approach, in that the

![](./images/811838225474650113_5.jpg)

Fig. 3. Measured and simulated values for force as a function of time for stress relaxation test.

![](./images/811838225474650113_6.jpg)

Fig. 4. Measured and simulated values for force as a function of time for cyclic loading test.

motion is guessed, and the stress response is computed. Such an approach, for uniaxial deformation, obviates the need for solving PDE's.

### 4.1. Mechanical behavior of polyamide 6 under uniaxial loading conditions

The components of deformation gradient tensor in Cartesian co-ordinates are given by

$$
\left[\boldsymbol{F}_{\kappa_{R}}\right]=\left(\begin{array}{lll}
\frac{\partial x}{\partial X} & \frac{\partial x}{\partial Y} & \frac{\partial x}{\partial Z} \\
\frac{\partial y}{\partial X} & \frac{\partial y}{\partial Y} & \frac{\partial y}{\partial Z} \\
\frac{\partial z}{\partial X} & \frac{\partial z}{\partial Y} & \frac{\partial z}{\partial Z}
\end{array}\right),
\tag{24}
$$

where $(X,Y,Z)$ represents the position occupied by a particle in the reference configuration $\kappa_{R}$, and $(x,y,z)$ represents the position occupied the same particle at time $t$.

The motion for uniaxial deformation is given through

$$
\begin{aligned}
& z=\lambda(t) Z, \\
& x=\frac{1}{\sqrt{\lambda(t)}} X, \\
& y=\frac{1}{\sqrt{\lambda(t)}} Y,
\end{aligned}
\tag{25}
$$

where $\lambda(t)$ (ratio of current length to the original length) represents stretch at time $t$.

Accordingly, the components of deformation gradient tensor $\boldsymbol{F}_{\kappa_{R}}$, the left Cauchy-Green stretch tensor $\boldsymbol{B}_{\kappa_{R}}$ and the velocity gradient $\boldsymbol{L}$, respectively, are given through

$$
\left[\boldsymbol{F}_{\kappa_{R}}\right]=\operatorname{diag}\left\{\frac{1}{\sqrt{\lambda(t)}}, \frac{1}{\sqrt{\lambda(t)}}, \lambda(t)\right\},
\tag{26}
$$

$$
\left[\boldsymbol{B}_{\kappa_{R}}\right]=\operatorname{diag}\left\{\frac{1}{\lambda(t)}, \frac{1}{\lambda(t)}, \lambda^{2}(t)\right\}
\tag{27}
$$

and

$$
[\boldsymbol{L}]=\operatorname{diag}\left\{\frac{-1}{2} \frac{\dot{\lambda}}{\lambda(t)}, \frac{-1}{2} \frac{\dot{\lambda}}{\lambda(t)}, \frac{\dot{\lambda}}{\lambda(t)}\right\}.
\tag{28}
$$

We shall assume that the components of the tensor $\boldsymbol{B}_{\kappa_{P(t)}}$ to have the structure similar to that of the tensor $\boldsymbol{B}_{\kappa_{R}}$, i.e.,

$$
\left[\boldsymbol{B}_{\kappa_{P(t)}}\right]=\operatorname{diag}\left\{\frac{1}{\sqrt{B(t)}}, \frac{1}{\sqrt{B(t)}}, B(t)\right\}.
\tag{29}
$$

It is evident from Eqs. (26)-(29) that the requirement of incompressibility are met, i.e., Eq. (11) is automatically met. Note that the components of $\boldsymbol{F}_{\kappa_{R}}, \boldsymbol{B}_{\kappa_{R}}, \boldsymbol{B}_{\kappa_{P(t)}}$, and $\boldsymbol{L}$ are functions of time only because the uniaxial deformation is a homogeneous deformation.

Substituting Eqs. (27) and (29) in Eq. (20), the components of stress tensor turn out to be

$$
[\boldsymbol{T}]=-p[\boldsymbol{I}]+\mu_{1} \operatorname{diag}\left\{\frac{1}{\sqrt{B(t)}}, \frac{1}{\sqrt{B(t)}}, B(t)\right\}+\mu_{2} \operatorname{diag}\left\{\frac{1}{\lambda(t)}, \frac{1}{\lambda(t)}, \lambda^{2}(t)\right\}.
\tag{30}
$$

Since the lateral surfaces of the specimen are traction-free, one can show that $T_{x x}=T_{y y}=0$, i.e., one can use this condition to obtain the Lagrange multiplier $p$, i.e.,

$$
p=\frac{\mu_{1}}{\sqrt{B(t)}}+\frac{\mu_{2}}{\lambda(t)}.
\tag{31}
$$

By substituting Eq. (31) in Eq. (30) and rearranging the terms, one arrives at $T_{z z}$ component of the stress tensor, i.e.,

$$
T_{Z Z}=\mu_{1}\left(B(t)-\frac{1}{\sqrt{B(t)}}\right)+\mu_{2}\left(\lambda^{2}(t)-\frac{1}{\lambda(t)}\right).
\tag{32}
$$

Given the Cauchy stress tensor $\boldsymbol{T}$, the total force can be calculated using

$$
\boldsymbol{f}=\operatorname{det}\left(\boldsymbol{F}_{\kappa_{R}}\right) \boldsymbol{T} \boldsymbol{F}_{\kappa_{R}}^{-T} \boldsymbol{N} a_{0},
\tag{33}
$$

where $a_{0}$ is the original area of cross-section of the specimen. The component of force acting along the z-direction is given through

**Table 2**
Optimized values associated with the parameters of the model.

<table>
<thead>
<tr>
<th>Parameters</th>
<th>Optimized values</th>
</tr>
</thead>
<tbody>
<tr>
<td>$\mu_1$ (MPa)</td>
<td>129.1267</td>
</tr>
<tr>
<td>$\mu_2$ (MPa)</td>
<td>70.3011</td>
</tr>
<tr>
<td>$v$ (MPa s)</td>
<td>12.4878</td>
</tr>
<tr>
<td>$\beta$</td>
<td>0.5666</td>
</tr>
</tbody>
</table>

$$
f_{z}=a_{0} \frac{\mathrm{T}_{z z}}{\lambda(t)}. \tag{34}
$$

Substituting Eqs. (28) and (29) in Eq. (23), we arrive at the evolution equation for the configuration $\kappa_{p(t)}$, i.e.,

$$
\frac{d B(t)}{d t}=2\left[\frac{\mu_{1}}{2 v}\right]^{\frac{1}{(2 \beta-1)}}\left[\frac{2+B(t) \sqrt{B(t)}}{\sqrt{B(t)}}-\frac{9 B(t)}{2 B(t) \sqrt{B(t)}+1}\right]^{\frac{(1-\beta)}{(2 \beta-1)}} \times\left[\frac{3 B(t)}{2 B(t) \sqrt{B(t)}+1}-B(t)\right]+2 B(t) \frac{\dot{\lambda}}{\lambda}. \tag{35}
$$

Substituting Eq. (29) in Eq. (23), one arrives at three equations that are consistent with each other, implying that the assumption made about the components of the tensor $\boldsymbol{B}_{\kappa_{p(t)}}$ is correct.

### 4.2. Simulation

Recall that two types of experiment were performed, namely, stress relaxation and mechanical response of an uniaxial test specimen subjected to strain controlled cyclic loading with a strain ratio of 0.1. During the first experiment, the cross-head is moved with a constant velocity of 2.4, 50, 100 and 120 mm/min, until the strain in the test section of the specimen reaches 0.08, 0.07, 0.07, and 0.06, respectively. Once the corresponding values of strain are reached, the movement of the cross-head is stopped, and the force is measured as a function of time (stress relaxation). During the second experiment, a fresh uniaxial test specimen is subjected to cyclic loading in the strain controlled mode, and the force required for such a deformation is measured. The stretch undergone by the test section of a specimen is computed using the readings from an extensometer (see Fig. 1).

For a given loading history, which for uniaxial extension corresponds to that of a given cross-head movement, i.e., a given $\lambda(t)$, one need to solve Eqs. (32), (34) and (35) together with the initial condition $B(0)=1$ for Eq. (35) to obtain force as a function of time.

The parameters $\mu_{1}, \mu_{2}, v$, and $\beta$ are determined by minimizing the error function, which is defined through

$$
\Phi=100 \sqrt{\frac{1}{N} \sum_{i=1}^{N}\left(1-\frac{f_{z, p r e}^{(i)}}{f_{z, \exp }^{(i)}}\right)^{2}},\tag{36}
$$

where $N$ is the total number of experimental data points, $f_{z, p r e}^{(i)}$ represents the predicted $z$ component of force corresponding to the $i^{\text {th }}$ data point, and $f_{z, \exp }^{(i)}$ represents the measured force. A combined optimization is performed for all sets of data, i.e., for stress relaxation and cyclic loading. The optimized parameters are listed in Table 2.

## 5. Results and discussion

The best fitted parameters of the viscoelastic model are summarized in Table 2. Fig. 3 shows the variation of experimental and the predicted forces with respect to time for various stretch rates and strain levels. The model is shown to be able to predict the experimental data very well with the overall error of less than 7%. It can be seen that the model predicts the general shape of the force time curve and was able to catch the peak forces, but slightly over estimates the relaxation part for 0.07strain by 10%.One striking feature of the model is that it was able to predict the crossover phenomenon observed between the test conducted at 0.07strain at stretch rate of $0.0325 \mathrm{~s}^{-1}$ and the test conducted at $0.0176 \mathrm{~s}^{-1}$, but at slightly greater time.

To predict the response of the model to cyclic loading conditions the same evolution equation was solved except that the stretch rate $\dot{\lambda}$ and the stretch history term $\lambda(t)$ were replaced by appropriate rate and ramp function (for stretch), respectively. Fig. 4 shows the experimental and predicted force time variation for 20 cycles. The model was found to predict the experimental forces very well but slightly overestimates the forces during first two cycles by less than 12%. The predicted forces were found to closely match the experimental forces in the subsequent cycles.

When a viscoelastic material is subjected to strain controlled, fatigue loading with a positive mean strain, one can observe that during the initial cycles, there is relaxation of the mean stress. However, the stress amplitude does not seem to change. Even though the peak and the valley stresses are positive during initial cycles, one can observe the plot approaching a state of complete stress reversal as the test proceeds. This phenomenon is shown in Fig. 4, i.e., a shift of peak and valley force values towards negative side. The model was found to be capable of capturing this important feature of the viscoelastic material.

### 6. Conclusions

In the present study, a viscoelastic model based on thermodynamic framework was derived and was used to simulate the mechanical responses of a polymer. The stress relaxation behavior and the strain controlled fatigue behavior of polyamide 6 was simulated using MATLAB® and the model was found to be able to capture the peak forces and reproduce the trends observed in the experimental data. This study will serve as an initial step towards predicting the heat dissipation in plastic machine components subjected to complex state of stresses. Therefore, instead of performing expensive full scale experiments, such a model can be used, to predict the hysteresis heating of components made of plastics. For complex geometries, prediction of heat generation can be done by incorporating this model in a commercial finite element package.

### References

[1] A. Boukamel, S. Meo, O. Debordes, M. Jaeger, A thermo-viscoelastic model for elastomeric behavior and its numerical application, Archive of Applied Mechanics 71 (2001) 785-801.

[2] G.A. Holzapfel, G. Reiter, Fully coupled thermomechanical behaviour of viscoelastic solids treated with finite elements, International Journal of Engineering Science 33 (1995) 1037-1058.

[3] S. Nasseri, L.E. Bilston, N. Phan-Thien, Viscoelastic properties of pig kidney in shear, experimental results and modelling, Rheologica Acta 41 (2002) 180-192.

[4] W. Yang, T.C. Fung, K.S. Chian, C.K. Chong, Viscoelasticity of esophageal tissue and application of a QLV model, Journal of Biomechanical Engineering 128 (2006) 909-916.

[5] M. Anand, K.R. Rajagopal, A shear-thinning viscoelastic fluid model for describing the flow of blood, International Journal of Cardiovascular Medicine and Science 4 (2004) 59-68.

[6] T.R. Tauchert, Heat generation in a viscoelastic solid, Acta Mechanica 3 (1967) 385-396.

[7] R.W. Young, Thermo-mechanical response of a viscoelastic rod driven by a sinusoidal displacement, International Journal of Solids and Structures 13 (1977) 925-936.

[8] S. Sridhar, N. Siva Prasad, K.N. Seetharamu, Estimation of temperature in rubber-like materials using non-linear finite element analysis based on strain history, Finite Elements in Analysis and Design 31 (1999) 281-294.

[9] M. Kaliske, H. Rothert, Formulation and implementation of three-dimensional viscoelasticity at small and finite strains, Computational Mechanics 19 (1997) 228-239.

[10] K.R. Rajagopal, A.R. Srinivasa, On the response of non-dissipative solids, Proceedings of the Royal Society A 463 (2007) 357-367.

[11] K.R. Rajagopal, A.R. Srinivasa, On the thermodynamics of fluids defined by implicit constitutive equations, Zeitschrift fur Angewandte Mathematik und Physik 59 (2008) 715-729.

[12] K.R. Rajagopal, A.R. Srinivasa, On a class of non-dissipative materials that are not hyperelastic, Proceedings of the Royal Society A 465 (2009) 493-500.

[13] K. Kannan, K.R. Rajagopal, A thermomechanical framework for the transition of a viscoelastic liquid to a viscoelastic solid, Mathematics and Mechanics of Solids 9 (2004) 37-59.

[14] K.R. Rajagopal, A.R. Srinivasa, A thermodynamic frame work for rate type fluid model, Journal of Non-Newtonian Fluid Mechanics 88 (2000) 207-227.

[15] S. Karra, K.R. Rajagopal, Development of three dimensional constitutive theories based on lower dimensional experimental data, Applications of Mathematics 54 (2009) 147-176.