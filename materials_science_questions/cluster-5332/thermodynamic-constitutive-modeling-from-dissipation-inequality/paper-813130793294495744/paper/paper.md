Accepted Manuscript

A Finite-Strain Constitutive Model for Anisotropic Shape Memory Alloys

A.R. Damanpack , M. Bodaghi , W.H. Liao

<table>
  <tr>
    <td>PII:</td>
    <td>S0167-6636(16)30277-0</td>
  </tr>
  <tr>
    <td>DOI:</td>
    <td>10.1016/j.mechmat.2017.05.012</td>
  </tr>
  <tr>
    <td>Reference:</td>
    <td>MECMAT 2745</td>
  </tr>
  <tr>
    <td>To appear in:</td>
    <td>Mechanics of Materials</td>
  </tr>
  <tr>
    <td>Received date:</td>
    <td>30 August 2016</td>
  </tr>
  <tr>
    <td>Revised date:</td>
    <td>31 May 2017</td>
  </tr>
  <tr>
    <td>Accepted date:</td>
    <td>31 May 2017</td>
  </tr>
</table>

![](./images/813130793294495744_1.jpg)

Please cite this article as: A.R. Damanpack , M. Bodaghi , W.H. Liao , A Finite-Strain Con-stitutive Model for Anisotropic Shape Memory Alloys, Mechanics of Materials (2017), doi: 10.1016/j.mechmat.2017.05.012

This is a PDF file of an unedited manuscript that has been accepted for publication. As a service to our customers we are providing this early version of the manuscript. The manuscript will undergo copyediting, typesetting, and review of the resulting proof before it is published in its final form. Please note that during the production process errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

### Highlights

- A 3D finite-stain constitutive model for asymmetry/anisotropy behaviors in SMAs.

- Simulation of self-accommodation, transformation, orientation and reorientation.

- Constitutive equations with symmetric tensors enhancing computational efficiency.

- Validation studies on behaviors of SMA 3D printed parts, wires and helical springs.

# A Finite-Strain Constitutive Model for Anisotropic Shape Memory Alloys

A. R. Damanpack, M. Bodaghi, W. H. Liao*

Smart Materials and Structures Laboratory, Department of Mechanical and Automation Engineering,
The Chinese University of Hong Kong, Shatin, N.T., Hong Kong, China

*Corresponding Author. Tel.: +852 3943 8341; fax: +852 2603 6002. E-mail address: whliao@cuhk.edu.hk

## Abstract
This paper presents a three-dimensional (3D) model to simulate self-accommodation, anisotropic martensitic transformation/orientation, reorientation of martensite variants, asymmetry in tension-compression and phase-change-dependent elastic properties in shape memory alloys (SMAs) within a finite-stain regime. The model is developed based on a multiplicative decomposition of the deformation gradient into elastic and inelastic parts by satisfying the second law of thermodynamics in sense of Clausius-Duhem inequality. The mathematical equations are derived in terms of symmetric tensors simplifying the constitutive relations. The finite-strain model is linearized into the small-strain regime preserving the materially non-linear feature. A description of the time-discrete form of the proposed model and its associated solution algorithm is presented. Numerical simulations of the mechanical behaviors of highly-textured NiTi 3D printed parts, wires and helical springs subjected to simple and complex loadings are performed and compared with experiments. Qualitative and quantitative correlation is observed between simulations and experiments to verify the predictive capabilities of the model and the solution procedure. It is also shown that the finite-strain modeling is essential for accurate prediction of SMA behaviors when deformations are prominent. Due to the absence of similar models in the specialized literature, this paper will fill a gap in the state of the art of this problem, and provide a computationally efficient tool for design and analysis of highly-textured SMA devices under complex loadings.

Keywords:
Shape memory alloys, Constitutive Modeling, Anisotropy, Tension-compression asymmetry, Finite strain

## 1. Introduction
Shape memory alloys (SMAs) are a particularly appealing and interesting class of smart materials capable of demonstrating large recoverable shape changes while producing hysteresis.

This unique behavior is a result of martensitic transformation/orientation/reorientation in response of stress and/or temperature changes introducing functional phenomenon of shape

memory effect (SME) and pseudo-elasticity (PE). The interesting characteristics of SMAs together with their good bio-compatibility have made them attractive for use in many fields from medicine to aeronautics, from automotive to aerospatial field, from civil to naval engineering.

As the understanding of SMA properties are getting deeper and deeper in material research community, the list of applications continues to expand. Through this expansion, a world-wide activity has been directed to properly reproduce SMA behaviors in a predictive modeling frame ranging from micro to macro scales. Phenomenological or macro models on the basis of macroscopic quantities to describe the estate of the SMA system are generally more popular and suitable for engineering structural analysis (Cisse *et al.*, 2016). They allow quick computations and compatibility with numerical methods such as finite element (FE) method in an efficient way. In the last three decades, a lot of researches have been dedicated to develop small-strain models for simulation of primary SMA features such as martensite transformation/orientation/reorientation and self-accommodation (Bodaghi *et al.*, 2014; Lagoudas *et al.*, 2012; Panico and Brinson, 2007; Raniecki and Lexcellent, 1994). For instance, motivated by the pioneer work of Panico and Brinson (2007) that treated transformation and reorientation as two different physical processes, Bodaghi *et al.* (2014) developed a robust three- dimensional (3D) small-strain model assuming the amount of martensite as scalar internal variable and the inelastic strain direction as directional internal variable. On the other hand, there have been less attempts at finite strain regime due to mathematical complexity. From a practical point of view, in many simple applications, for instance in pipe couplers or ribbon actuators, SMA devices experiences a small strain regime. However, in different types of applications, SMAs may experience large rotations and moderate or finite strains. For instance, self-expanding SMA stent as a common biomedical device undergoes large rotations combined with moderate

strains when it is inserted into the catheter and then blood vessel (Zhao *et al.*, 2011). In the following, some of finite-strain models existing in the literature for shape memory alloys are reviewed and discussed.

Most of finite-strain constitutive models have been introduced through extension of small-strain ones. Two approaches have been considered in finite-strain SMA theories: 1) multiplicative decomposition of the deformation gradient into elastic and inelastic components; 2) additive decomposition of the strain rate tensor into elastic and inelastic components. While it is rigorous mathematically, additive decomposition lacks the capability to incorporate typical continuum crystal plasticity. The multiplicative decomposition was in fact motivated by the deformation process in crystal plasticity, where the continuum deforms firstly plastically by shearing on lattice slip-planes, and subsequently the plastically deformed continuum is mapped by an elastic deformation gradient onto the current configuration. Adopting a multiplicative decomposition of the deformation gradient, Arghavani *et al.* (2010) developed the small-strain SMA model of Panico and Brinson (2007) into the finite strain regime. Müller and Bruhns (2006) extended the small-strain model proposed by Raniecki and Lexcellent (1994) into finite strain regime implementing an additive decomposition of the strain rate tensor into elastic and inelastic part. The model was able to describe the pseudo-elastic response of SMAs with thermo-mechanically coupled behavior.

In order to assess the potential applications of SMAs in advanced engineering and technologies, many attempts have been conducted to experimentally characterize the behaviors of SMAs over the past three decades. Experimental observations emphasized that SMAs may experience secondary features such as rhombohedral (R) phase transformation, rate-dependent cyclic deformation, transformation/reorientation-induced plasticity, anisotropic transformation

strain generation, asymmetric behavior in tension and compression and the differences between the elastic properties at different phases (Chemisky *et al.*, 2014; Dadbakhsh *et al.*, 2016; Frost *et al.*, 2016; Kan *et al.*, 2016; Mehrabi *et al.*, 2014; Nemat-Nasser and Guo, 2009; Sedlák *et al.*, 2012; Šittner *et al.* 2009a, 2009b; Saleeb *et al.*, 2015; Taillard *et al.*, 2008). For instance, Taillard *et al.* (2008) and Šittner *et al.* (2009a) showed that technological process of manufacturing introduced a strong texture and anisotropy into the SMA components affecting the phase transformation surface. Recently, Dadbakhsh *et al.* (2016) showed that selective laser melting (SLM) as a 3D metal-based printing process strongly oriented the fine austenite subgrains towards the building direction. This was the source of the anisotropy in thermo-mechanical behaviors of SMAs in elastic and inelastic regimes. Some comparisons between simulations with classical models and experiments showed that predictions were not in good correlations with experimental observations and needed to be improved (Šittner *et al.*, 2009a). In this respect, due to complicated behavior, a few scientific efforts have been focused to model asymmetry in tension-compression and anisotropic transformation features major in small-strain and minor in finite-strain regimes. For instance, in the small strain regime, Taillard *et al.* (2008) presented a constitutive model for pseudo-elastic anisotropic/asymmetric SMAs establishing the linearity between martensite volume fraction and equivalent transformation strain. Hartl *et al.* (2012) improved the 3D model originally developed by Lagoudas *et al.* (2012) introducing a constant back stress tensor to simulate anisotropic transformation strain and recovery. They showed that isotropic approximation was insufficient for anisotropy exhibited in an SMA component. Frost and his collogues proposed constitutive models with capability of realistic simulations of martensitic transformation/reorientation, R-phase transformation, asymmetry and anisotropy features, and martensite stabilization by deformation or evolution of transformation hysteresis

with temperature (Frost *et al.*, 2016; Sedlák *et al.*, 2012). Mehrabi *et al.* (2014) studied the effect of boundary condition on the mechanical behavior of pseudo-elastic NiTi SMAs using experimental investigation and 3D constitutive modeling. Results showed that anisotropic strain observed in the samples depended on the end boundary condition when martensitic transformation took place. Bodaghi *et al.* (2016) presented a bi-axial model to capture asymmetric and anisotropic strain generation in SMA rods and tubes under combined tension-torsion loading. Recently, a 3D model was developed by Chatziathanasiou *et al.* (2016) to simulate phase transformation and reorientation in SMAs subjected to non-proportional complex loading by considering thermo-mechanical coupling related to dissipation and latent heat. In finite strain regime, Thamburaja (2010) presented a finite-strain non-local model to simulate martensitic transformation with tension-compression asymmetry feature. Stupkiewicz and Petryk (2013) developed a finite strain model of pseudo-elasticity in SMAs considering the effects of tension-compression asymmetry and transversal isotropy of the surface of limit transformation strains.

The literature review indicates the lack of a comprehensive finite-strain constitutive model with capability of simulating martensitic transformation/orientation, self-accommodation, reorientation of martensite variants as the primary SMA features and anisotropic transformation strain generation and asymmetry in tension-compression as the secondary features. This paper aims at developing a robust 3D model to predict SMA behaviors with the mentioned features under multi-axial non-proportional loadings in the finite-strain regime. This is an extension of our small-strain isotropic/symmetric 3D model (Bodaghi *et al.*, 2014) to finite-strain regime with capability of simulation of anisotropic transformation and tension-compression asymmetric behaviors. Motivated by the work of Bodaghi *et al.* (2014), volume fractions of self-

accommodated and oriented martensite are selected as scalar internal variables while the preferred direction of oriented martensite variants is considered as a tensorial internal variable. The phenomenological constitutive model is developed within the framework of continuum thermodynamics of irreversible processes adopting the multiplicative decomposition of the deformation gradient into elastic and inelastic parts. A robust model is established in which all quantities are symmetric simplifying the constitutive relations. In order to replicate anisotropic transformation and asymmetry feature in tension-compression, the magnitude of preferred direction of oriented martensite is restricted using a well-known function introduced by Taillard *et al.* (2008). The proposed finite-strain model is then linearized to a simplified model appropriate for small-strain regimes. The time-discrete counterpart of the constitutive model is introduced integrating the evolution equation of martensitic variants reorientation by means of explicit forward-Euler scheme. Capabilities of the proposed model are demonstrated through several numerical simulations and comparisons with experimental results on highly-textured NiTi 3D printed parts, wires and springs reported by Dadbakhsh *et al.* (2016), Šittner *et al.* (2009a, 2009b) and Frost *et al.* (2016). In this respect, an in-house FE program is developed for solving boundary-value problems. It is numerically demonstrated that the model is capable of replicating the main features observed in experiments including martensitic transformation/orientation/reorientation, tension-compression asymmetry, anisotropic transformation strain generation and phase-change-dependent elastic properties. Furthermore, importance of finite-strain modeling is examined by implementing the present model with small-strain and small-strain-moderate-rotation assumptions and performing comparative study with experimental data. It is shown that considering finite-strain regime is essential to accurately predict SMA behaviors when deformations are prominent. Due to accuracy, the model is

expected to be a useful computational tool for design and analysis of highly-textured SMA structures under multi-axial complex loadings.

### 2. 3D Constitutive Model

In this section, a 3D finite-strain constitutive model is developed to describe primary and secondary features of polycrystalline SMAs within the framework of continuum thermodynamics with internal variables.

#### 2.1. Preliminaries

A 3D SMA body is assumed. A material point in the reference configuration occupies point $\boldsymbol{X}$ having reference temperature $T_{0}$. This material point then moves to a spatial point $\boldsymbol{x}$ while temperature changes to $T$. While the displacement vector, $\boldsymbol{u}$ , is assumed as $\boldsymbol{x}-\boldsymbol{X}$, the local changes in space of the motion are given by the deformation gradient as:

$$
\boldsymbol{F}=\frac{\partial \boldsymbol{x}}{\partial \boldsymbol{X}} \tag{1}
$$

The determinant (Jacobian) of the deformation gradient, $J=\operatorname{det}(\boldsymbol{F})$, presents the change of material volume through the deformation supposed to be positive.

The right and left Cauchy-Green deformation tensors can be written as:

$$
\boldsymbol{C}=\boldsymbol{F}^{T} \boldsymbol{F} \quad ; \quad \boldsymbol{b}=\boldsymbol{F} \boldsymbol{F}^{T} \tag{2}
$$

Since the deformation gradient $\boldsymbol{F}$ is not a suitable to measure the strain, the Green-Lagrange strain tensor, $\boldsymbol{E}$ , is adopted as:

$$
\boldsymbol{E}=\frac{1}{2}(\boldsymbol{C}-\boldsymbol{I}) \tag{3}
$$

and the velocity gradient tensor $\boldsymbol{l}$ is given by

$$
\boldsymbol{l}=\dot{\boldsymbol{F}} \boldsymbol{F}^{-1}
\tag{4}
$$

where $\boldsymbol{I}$ signifies the second-order identity tensor while the superposed dot represents the rate of change of the quantity.

The symmetric component of $\boldsymbol{l}$ represents the strain rate tensor $\boldsymbol{d}$ as:

$$
\boldsymbol{d}=\frac{1}{2}\left(\boldsymbol{l}+\boldsymbol{l}^{T}\right)
\tag{5}
$$

The rate of the Green-Lagrange strain tensor can be derived using Eqs. (2) and (3) as:

$$
\dot{\boldsymbol{E}}=\boldsymbol{F}^{T} \boldsymbol{d} \boldsymbol{F}
\tag{6}
$$

The second Piola-Kirchhoff stress tensor $\boldsymbol{S}$ can also be expressed in terms of the Cauchy stress $\boldsymbol{\sigma}$ as:

$$
\boldsymbol{S}=J \boldsymbol{F}^{-1} \boldsymbol{\sigma} \boldsymbol{F}^{-T}
\tag{7}
$$

A multiplicative decomposition of the deformation gradient $\boldsymbol{F}$ into an elastic part $\boldsymbol{F}_{e}$, characterized with respect to an middle configuration, and an inelastic part $\boldsymbol{F}_{i}$ related to the reference configuration is adopted as:

$$
\boldsymbol{F}=\boldsymbol{F}_{e} \boldsymbol{F}_{i}
\tag{8}
$$

Henceforth, the subscripts $e$ and $i$ stand for elastic and inelastic parts.

The elastic and inelastic Green tensors $\boldsymbol{C}_{e}$ and $\boldsymbol{C}_{i}$ are characterize from Eq. (2) as:

$$
\boldsymbol{C}_{e}=\boldsymbol{F}_{e}^{T} \boldsymbol{F}_{e} \quad ; \quad \boldsymbol{C}_{i}=\boldsymbol{F}_{i}^{T} \boldsymbol{F}_{i}
\tag{9}
$$

Using Eqs. (8) and (9), one obtains:

$$
\boldsymbol{C}_{e}=\boldsymbol{F}_{i}^{-T} \boldsymbol{C} \boldsymbol{F}_{i}^{-1}
\tag{10}
$$

The total martensite volume fraction at each material point can be written as:

$$
\xi=\xi_{S}+\xi_{T} \quad 0 \leq \xi_{S} \leq 1, \quad 0 \leq \xi_{T} \leq 1, \quad 0 \leq \xi \leq 1
\tag{11}
$$

where $\xi_{S}$ and $\xi_{T}$ represent volume fractions of stress-induced oriented martensite and temperature-induced self-accommodated martensite, respectively.

Experimental studies reveal that the martensitic phase transformation preserves volume of SMAs. Therefore, the isochoric conditions meet $\det(\boldsymbol{F}_{i})=1$. After taking the time derivative, one obtains:

$$tr(\boldsymbol{d}_{i})=tr(\dot{\boldsymbol{E}}_{i})=tr(\dot{\boldsymbol{C}}_{i})=0 \tag{12}$$

It means that traceless tensors of $\boldsymbol{d}_{i}$, $\dot{\boldsymbol{E}}_{i}$ and $\dot{\boldsymbol{C}}_{i}$ are deviatoric.

The self-accommodated martensite variants nucleate and grow inside the austenite producing no observable macroscopic transformation strain. In contrast, the oriented martensite causes a significant macroscopic strain. Due to this fact, the Green-Lagrange inelastic strain tensor $\boldsymbol{E}_{i}$ is assumed to characterize the average effect of oriented martensite so that its normal and direction represent volume fraction and preferred direction of oriented martensite. Considering $N$ to characterize the preferred direction of oriented martensite variants, $\boldsymbol{E}_{i}$ can be expressed as (Bodaghi *et al.*, 2014):

$$\boldsymbol{E}_{i}=\varepsilon_{m} \xi_{S} \boldsymbol{N} \tag{13}$$

in which $\varepsilon_{m}$ is considered as a material parameter.

Taking time derivative of Eq. (13) results in:

$$\dot{\boldsymbol{E}}_{i}=\varepsilon_{m}\left(\dot{\xi}_{S} \boldsymbol{N}+\xi_{S} \dot{\boldsymbol{N}}\right) \tag{14}$$

The above relation reveals that the inelastic strain evolution additively consists pure transformation/orientation of the parent phase $(\dot{\xi}_{S} \neq 0, \dot{\boldsymbol{N}}=\boldsymbol{0})$ and pure reorientation of

previously developed oriented martensite $(\xi_{S}=c t e, \dot{N} \neq \boldsymbol{0})$ . Also, comparing Eqs. (12) and (14) implies that $tr(N)=tr(\dot{N})=0$.

### 2.2. Helmholtz free energy function and constitutive relations
To satisfy the principle of material objectivity, the Helmholtz free energy has to depend on $F_{e}$ via $C_{e}$. It is also considered to be a function of martensite volume fraction and the temperature. It is formulated as:
$$\Psi\left(\boldsymbol{C}_{e}, T, \xi_{S}, \xi_{T}\right)=\frac{1}{\rho_{0}} \psi_{e}\left(\boldsymbol{C}_{e}, T\right)+\psi_{c 1}\left(T, \xi_{S}, \xi_{T}\right)+\psi_{c 2}\left(\xi_{S}\right) \tag{15}$$
where $\rho_{0}$ is the reference density. $\psi_{e}$ denotes a hyperelastic strain energy supposed to be an isotropic function of $C_{e}$. $\psi_{c 1}$ and $\psi_{c 2}$ represent respectively chemical and configurational energies.

Saint-Venant-Kirchhoff strain energy function is adopted as:
$$\psi_{e}\left(\boldsymbol{E}_{e}, T\right)=\frac{1}{2} \lambda \operatorname{tr}\left(\boldsymbol{E}_{e}\right)^{2}+\mu \operatorname{tr}\left(\boldsymbol{E}_{e}^{2}\right)-3 \bar{\kappa}\left(T-T_{0}\right) \operatorname{tr}\left(\boldsymbol{E}_{e}\right) \tag{16}$$
where $\lambda$ and $\mu$ are Lamè constants while $\bar{\kappa}$ is related to the thermal coefficient of expansion for the SMA material. They are assumed to be followed the Reuss model as:
$$\frac{1}{Z}=\frac{1}{Z^{A}}-\frac{\xi_{S}}{\Delta Z}, \Delta Z=\frac{Z^{A} Z^{M}}{Z^{M}-Z^{A}}, Z=\lambda, \mu, \bar{\kappa} \tag{17}$$
where superscripts $M$ and $A$ refer to the martensite and austenite, respectively.

Using Eq. (3) and (16), strain energy function can be rewritten as:
$$\begin{aligned}
\psi_{e}\left(\boldsymbol{C}_{e}, T, \xi_{S}\right)=\psi_{e}\left(\overline{\boldsymbol{C}}, T, \xi_{S}\right)= & \frac{1}{8} \lambda \operatorname{tr}(\overline{\boldsymbol{C}})^{2}+\frac{1}{4} \mu \operatorname{tr}\left(\overline{\boldsymbol{C}}^{2}\right)-\left(\frac{3}{4} \lambda+\frac{1}{2} \mu+\frac{3}{2} \bar{\kappa}\left(T-T_{0}\right)\right) \operatorname{tr}(\overline{\boldsymbol{C}}) \\
& +\frac{9}{2} \bar{\kappa}\left(T-T_{0}\right)+\frac{9}{8} \lambda+\frac{3}{4} \mu
\end{aligned} \tag{18}$$
where $\overline{\boldsymbol{C}}=\boldsymbol{C} \boldsymbol{C}_{i}^{-1}$.

In order to derive the thermo-dynamic dissipative forces, the second law of thermo dynamics in the framework of Clausius-Duhem inequality should be satisfied. It is formulated assuming the positiveness of the thermal dissipation as:

$$
D_{m}=\frac{1}{\rho_{0}} \boldsymbol{S}: \dot{\boldsymbol{E}}-(\dot{\Psi}+s \dot{T}) \geq 0
$$

(19)

where $s$ is the specific entropy.

Taking the time derivative of the Helmholtz free energy (15) and considering $\dot{\boldsymbol{E}}=\dot{\boldsymbol{C}} / 2$, the mechanical dissipation inequality (19) can be rewritten as:

$$
\begin{aligned}
\rho_{0} D_{m}= & \frac{1}{2}\left(\boldsymbol{S}-2 \frac{\partial \psi_{e}}{\partial \boldsymbol{C}}\right): \dot{\boldsymbol{C}}-\left(\frac{\partial \psi_{e}}{\partial \boldsymbol{C}_{i}}\right): \dot{\boldsymbol{C}}_{i}-\left(\frac{\partial \psi_{e}}{\partial \xi_{S}}+\rho_{0} \frac{\partial \psi_{c 1}}{\partial \xi_{S}}+\rho_{0} \frac{\partial \psi_{c 2}}{\partial \xi_{S}}\right) \dot{\xi}_{S}-\rho_{0}\left(\frac{\partial \psi_{c 1}}{\partial \xi_{T}}\right): \dot{\xi}_{T} \\
& -\left(\frac{\partial \psi_{e}}{\partial T}+\rho_{0} \frac{\partial \psi_{c 1}}{\partial T}+\rho_{0} s\right) \dot{T} \geq 0
\end{aligned}
$$

(20)

Moreover, by using the inelastic strain rate (14) as well as the property $\dot{\boldsymbol{E}}_{i}=\dot{\boldsymbol{C}}_{i} / 2$, inequality (20) results in

$$
\begin{aligned}
\rho_{0} D_{m}= & \frac{1}{2}\left(\boldsymbol{S}-2 \frac{\partial \psi_{e}}{\partial \boldsymbol{C}}\right): \dot{\boldsymbol{C}}-2 \varepsilon_{m} \frac{\partial \psi_{e}}{\partial \boldsymbol{C}_{i}}:\left(\boldsymbol{\xi}_{S} \dot{\boldsymbol{N}}\right)-\varepsilon_{m}\left(2 \frac{\partial \psi_{e}}{\partial \boldsymbol{C}_{i}}: \boldsymbol{N}+\frac{1}{\varepsilon_{m}} \frac{\partial \psi_{e}}{\partial \xi_{S}}+\frac{\rho_{0}}{\varepsilon_{m}} \frac{\partial \psi_{c 1}}{\partial \xi_{S}}+\frac{\rho_{0}}{\varepsilon_{m}} \frac{\partial \psi_{c 2}}{\partial \xi_{S}}\right) \dot{\xi}_{S} \\
& -\left(\rho_{0} \frac{\partial \psi_{c 1}}{\partial \xi_{T}}\right) \dot{\xi}_{T}-\left(\frac{\partial \psi_{e}}{\partial T}+\rho_{0} \frac{\partial \psi_{c 1}}{\partial T}+\rho_{0} s\right) \dot{T} \geq 0
\end{aligned}
$$

(21)

This inequality implies sufficient conditions for the second Piola-Kirchhoff stress tensor $\boldsymbol{S}$ and the entropy as:

$$
\begin{aligned}
& \boldsymbol{S}=2 \frac{\partial \psi_{e}}{\partial \boldsymbol{C}} \\
& s=-\frac{1}{\rho_{0}} \frac{\partial \psi_{e}}{\partial T}-\frac{\partial \psi_{c 1}}{\partial T}
\end{aligned}
$$

(22)

the residual inequality reads

$$
\rho_{0} D_{m}=-2 \varepsilon_{m} \frac{\partial \psi_{e}}{\partial \boldsymbol{C}_{i}}:\left(\boldsymbol{\xi}_{S} \dot{\boldsymbol{N}}\right)-\varepsilon_{m}\left(2 \frac{\partial \psi_{e}}{\partial \boldsymbol{C}_{i}}: \boldsymbol{N}+\frac{1}{\varepsilon_{m}} \frac{\partial \psi_{e}}{\partial \xi_{S}}+\frac{\rho_{0}}{\varepsilon_{m}} \frac{\partial \psi_{c 1}}{\partial \xi_{S}}+\frac{\rho_{0}}{\varepsilon_{m}} \frac{\partial \psi_{c 2}}{\partial \xi_{S}}\right) \dot{\xi}_{S}-\left(\rho_{0} \frac{\partial \psi_{c 1}}{\partial \xi_{T}}\right) \dot{\xi}_{T} \geq 0
$$

(23)

Derivation of $\psi_{e}$ with respect to $\boldsymbol{C}, \boldsymbol{C}_{i}, T$ and $\xi_{S}$ appeared in Eqs. (22) and (23) can be obtained from the strain energy function (18) after performing some mathematical manipulations as:

$$
\begin{aligned}
\frac{\partial \psi_{e}}{\partial \boldsymbol{C}}= & \frac{\partial \psi_{e}}{\partial \overline{\boldsymbol{C}}} \boldsymbol{C}_{i}^{-1} \\
\frac{\partial \psi_{e}}{\partial \boldsymbol{C}_{i}}= & -\frac{\partial \psi_{e}}{\partial \overline{\boldsymbol{C}}} \boldsymbol{C}_{i}^{-1} \overline{\boldsymbol{C}}=-\frac{\partial \psi_{e}}{\partial \overline{\boldsymbol{C}}} \boldsymbol{C} \boldsymbol{C}_{i}^{-1} \\
\frac{\partial \psi_{e}}{\partial T}= & -\frac{3}{2} \overline{\kappa} \boldsymbol{t r}\left(\boldsymbol{C} \boldsymbol{C}_{i}^{-1}\right)+\frac{9}{2} \overline{\boldsymbol{\kappa}} \\
\frac{\partial \psi_{e}}{\partial \xi_{S}}= & \Lambda=\left(\frac{1}{8} \boldsymbol{t r}\left(\boldsymbol{C} \boldsymbol{C}_{i}^{-1}\right)^{2}-\frac{3}{4} \boldsymbol{t r}\left(\boldsymbol{C} \boldsymbol{C}_{i}^{-1}\right)+\frac{9}{8}\right) \frac{d \lambda}{d \xi_{S}}+\left(\frac{1}{4} \boldsymbol{t r}\left(\boldsymbol{C} \boldsymbol{C}_{i}^{-1} \boldsymbol{C} \boldsymbol{C}_{i}^{-1}\right)-\frac{1}{2} \boldsymbol{t r}\left(\boldsymbol{C} \boldsymbol{C}_{i}^{-1}\right)+\frac{3}{4}\right) \frac{d \mu}{d \xi_{S}} \\
& +\frac{3}{2}\left(3-\boldsymbol{t r}\left(\boldsymbol{C} \boldsymbol{C}_{i}^{-1}\right)\right)\left(T-T_{0}\right) \frac{d \overline{\boldsymbol{\kappa}}}{d \xi_{S}}
\end{aligned}
$$

where
$$
\frac{\partial \psi_{e}}{\partial \overline{\boldsymbol{C}}}=\left(\frac{1}{4} \lambda \boldsymbol{t r}\left(\boldsymbol{C}_{i}^{-1} \boldsymbol{C}\right)-\frac{3}{2} \overline{\boldsymbol{\kappa}}\left(T-T_{0}\right)-\frac{3}{4} \lambda-\frac{1}{2} \mu\right) \boldsymbol{I}+\frac{1}{2} \mu \boldsymbol{C}_{i}^{-1} \boldsymbol{C}
$$

It is worthy to mention that, since $\boldsymbol{C}$ and $\boldsymbol{C}_{i}$ are symmetric tensors, $\frac{\partial \psi_{e}}{\partial \overline{\boldsymbol{C}}}$ and $\frac{\partial \psi_{e}}{\partial \boldsymbol{C}_{i}}$ become symmetric. It implies that the model would be symmetric simplifying the constitutive relations.

Introducing Eqs. $(22)_{1}$ and $(24)_{2}$, and dividing by $\varepsilon_{m}$, the mechanical dissipation inequality (23) reads:
$$
\frac{\rho_{0}}{\varepsilon_{m}} D_{m}=\left(\boldsymbol{S} \boldsymbol{C} \boldsymbol{C}_{i}^{-1}\right):\left(\dot{\xi}_{S} \dot{\boldsymbol{N}}\right)+\left(\boldsymbol{S} \boldsymbol{C} \boldsymbol{C}_{i}^{-1}: \boldsymbol{N}-\frac{1}{\varepsilon_{m}} \Lambda-\frac{\rho_{0}}{\varepsilon_{m}}\left(\frac{\partial \psi_{c 1}}{\partial \xi_{S}}+\frac{\partial \psi_{c 2}}{\partial \xi_{S}}\right)\right) \dot{\xi}_{S}-\frac{\rho_{0}}{\varepsilon_{m}} \frac{\partial \psi_{c 1}}{\partial \xi_{T}} \dot{\xi}_{T} \geq 0
$$

Next, the chemical and configurational energies are adopted as (Panico and Brinson, 2007):
$$
\begin{aligned}
& \psi_{c 1}=u_{0}^{A}-T s_{0}^{A}+\left(\xi_{S}+\xi_{T}\right) \Delta s_{0}\left(T-T_{0}\right)+c_{v}^{A}\left[\left(T-T_{0}\right)-T \ln \left(T / T_{0}\right)\right] \\
& \psi_{c 2}=\frac{1}{2} H_{S} \xi_{S}^{2}
\end{aligned}
$$

where $u_{0}$ and $s_{0}$ denote the specific internal energy and entropy at the equilibrium temperature $T_{0}$ while the specific entropy difference $\Delta s_{0}=s_{0}^{A}-s_{0}^{M}$ has been adopted. $c_{v}^{A}$ indicates the specific heat at constant volume for austenite phase. Furthermore, $H_{S}$ is associated to a material parameter that governs the initial hardening during martensitic transformation/orientation.

Derivation of $\psi_{c 1}$ and $\psi_{c 2}$ with respect to $T, \xi_{S}, \xi_{T}$ appeared in Eqs. (26) and $(22)_{2}$ are derived form Eq. (27) as:

$$
\begin{aligned}
& \frac{\partial \psi_{c 1}}{\partial \xi_{S}}=\Delta s_{0}\left(T-T_{0}\right) \quad ; \quad \frac{\partial \psi_{c 2}}{\partial \xi_{S}}=H_{S} \xi_{S} \\
& \frac{\partial \psi_{c 1}}{\partial \xi_{T}}=\Delta s_{0}\left(T-T_{0}\right) \\
& \frac{\partial \psi_{c 1}}{\partial T}=-s_{0}^{A}+\left(\xi_{S}+\xi_{T}\right) \Delta s_{0}-c_{v}^{A} \ln \left(T / T_{0}\right)
\end{aligned}
\tag{28}
$$

Finally, by substituting (28) into (22) and (26), one gets the state equations and the mechanical dissipation inequality as:

$$
\begin{aligned}
& \boldsymbol{S}=\left(\frac{1}{2} \lambda \operatorname{tr}\left(\boldsymbol{C}_{i}^{-1} \boldsymbol{C}\right)-\frac{3}{2} \lambda-3 \bar{\kappa}\left(T-T_{0}\right)-\mu\right) \boldsymbol{C}_{i}^{-1}+\mu \boldsymbol{C}_{i}^{-1} \boldsymbol{C} \boldsymbol{C}_{i}^{-1} \\
& s=\frac{1}{\rho_{0}}\left(\frac{3}{2} \bar{\kappa} \operatorname{tr}\left(\boldsymbol{C} \boldsymbol{C}_{i}^{-1}\right)-\frac{9}{2} \bar{\kappa}\right)+s_{0}^{A}-\left(\xi_{S}+\xi_{T}\right) \Delta s_{0}+c_{v}^{A} \ln \left(T / T_{0}\right)
\end{aligned}
\tag{29}
$$

and

$$
\frac{\rho_{0}}{\varepsilon_{m}} D_{m}=Q_{N}:\left(\xi_{S} \dot{\boldsymbol{N}}\right)+Q_{S} \dot{\xi}_{S}+Q_{T} \dot{\xi}_{T} \geq 0
\tag{30}
$$

where $Q_{N}, Q_{S}$ and $Q_{T}$ are thermo-dynamical dissipative forces associated to internal variables $\boldsymbol{N}, \xi_{S}, \xi_{T}$ defined as:

$$
\begin{aligned}
& Q_{N}=\left(\boldsymbol{S} \boldsymbol{C} \boldsymbol{C}_{i}^{-1}\right)^{D} \\
& Q_{S}=\left(\boldsymbol{S} \boldsymbol{C} \boldsymbol{C}_{i}^{-1}\right)^{D}: \boldsymbol{N}-\frac{1}{\varepsilon_{m}} \Lambda-C^{A}\left(T-T_{0}\right)-\bar{\sigma} \xi_{S} \\
& Q_{T}=-C^{A}\left(T-T_{0}\right)
\end{aligned}
\tag{31}
$$

in which the superscript $D$ signifies the deviatoric component of a tensor. Also the parameter $C^{A}=\rho_{0} \Delta s_{0} / \varepsilon_{m}$ may characterize the conventional slope of the transformation line to austenite in a geometrically linear phase diagram (Fig. 1), while $\bar{\sigma}=\rho_{0} H_{S} / \varepsilon_{m}$ is considered as a relative stress. In Eq. (31), the analogy of $\boldsymbol{S C C}_{i}^{-1}: \boldsymbol{N}=\left(\boldsymbol{S C C}_{i}^{-1}\right)^{D}: \boldsymbol{N}$ has been adopted due to the traceless property of $\boldsymbol{N}$. It should be mentioned that, while $Q_{N}$ is chosen to be the thermo-dynamic force conjugate with $\left(\xi_{S} \dot{\boldsymbol{N}}\right)$ (reorientation strain rate), the function of $Q_{N} \xi_{S}$ can be also assumed as the thermo-dynamic force associated with $\dot{\boldsymbol{N}}$. Both selections are equivalent since they satisfy the dissipation inequality (30), however, the first form allows computation of the


reorientation mechanism when simultaneously reverse phase transformation is completed
$(\xi_{S} \to 0)$.

![](./images/813130793294495744_2.jpg)

Fig. 1. Stress-temperature phase diagram of the model for a typical NiTi case $II$ ($M_{0}^{f},M_{0}^{s},A_{0}^{s},A_{0}^{f}$ are characteristic temperatures representing martensite start and finish, and austenite start and finish, respectively).

To satisfy the second law of thermo-dynamics during the martensite variant reorientation, the evolution equation for the reorientation strain $(\xi_{S}\dot{N})$ should be determined. It is considered that the component of $SC{C}_{i}^{-1}$ normal to the average direction of oriented martensite variants reorients the martensite variants. It is formulated as:

$$
\xi_{S} \dot{N}=\dot{\lambda}_{R}(\overline{\boldsymbol{I}}: \boldsymbol{m}) \tag{32}
$$

where $\boldsymbol{m}$ is unit tensor defined as:

$$
\boldsymbol{m}=\frac{\left(S C C_{i}^{-1}\right)^{D}}{\left\|\left(S C C_{i}^{-1}\right)^{D}\right\|} \tag{33}
$$

and $\dot{\lambda}_{R}$ is the consistency parameter while $\overline{\boldsymbol{I}}$ signifies the fourth-order projection tensor defined as:

$$
\overline{\boldsymbol{I}}=\hat{\boldsymbol{I}}^{D}-\boldsymbol{n} × \boldsymbol{n} \quad, \quad \boldsymbol{n}=\frac{N}{\|\boldsymbol{N}\|} \tag{34}
$$

where $\hat{\boldsymbol{I}}^{D}$ denotes fourth-order identity deviatoric tensor.

Introducing Eq. (32) into the mechanical dissipation inequality (30) yields:

$$
\frac{\rho_{0}}{\varepsilon_{m}} D_{m}=\left\|\left(\boldsymbol{S} \boldsymbol{C} \boldsymbol{C}_{i}^{-1}\right)^{D}\right\|\left(1-(\boldsymbol{m}: \boldsymbol{n})^{2}\right) \dot{\lambda}_{R}+Q_{S} \dot{\xi}_{S}+Q_{T} \dot{\xi}_{T} \geq 0 \tag{35}
$$

For the internal variables $N$, $\xi_{S}$ and $\xi_{T}$, the following limit functions are assumed:

$$
\begin{aligned}
&F_{R}=1-(\boldsymbol{m}: \boldsymbol{n})^{2}-Y_{R} \\
&F_{S}=Q_{S} \operatorname{sgn}\left(Q_{S}\right)-Y_{S}^{f / r}\left(\xi_{S},\|\boldsymbol{N}\|\right) \\
&F_{T}=Q_{T} \operatorname{sgn}\left(Q_{T}\right)-Y_{T}^{f / r}\left(\xi_{T}, \sigma_{v}\right)
\end{aligned} \tag{36}
$$

where the signum function is characterized as:

$$
\operatorname{sgn}(Q)= \begin{cases}1 & \text { if } Q>0 \\ 0 & \text { if } Q=0 \\ -1 & \text { if } Q<0\end{cases} \tag{37}
$$

Also, $Y_{R}$ denotes a constant yield value to trigger the reorientation mechanism while $Y_{S}^{f / r}$ and $Y_{T}^{f / r}$ govern the kinetics of stress- and temperature-induced forward/reverse phase transformations, respectively. Furthermore, parameter $\sigma_{v}$ signifies equivalent von Mises stress.

The model is finally completed by constraining the evolution of the internal variables via standard Kuhn-Tucker conditions as:

$$
\begin{aligned}
&F_{R} \leq 0, \dot{\lambda}_{R} \geq 0 \quad, \quad F_{R} \dot{\lambda}_{R}=0 \\
&F_{S} \leq 0, \dot{\xi}_{S}=o r \neq 0, \quad F_{S} \dot{\xi}_{S}=0 \\
&F_{T} \leq 0, \dot{\xi}_{T}=o r \neq 0, \quad F_{T} \dot{\xi}_{T}=0
\end{aligned} \tag{38}
$$


### 2.3. Kinetics

In order to describe $Y_{S}^{f / r}(\xi_{S},\|\boldsymbol{N}\|)$, an exponential form is adopted as:

$$
Y_{s}^{f / r}=
\begin{cases}
C_{0}^{f}-C_{1}^{f} \xi_{s} \ln (1-\xi_{s}+e^{-7})+D_{0}^{f}(1-\|\boldsymbol{N}\|) & \text { for } \dot{\xi}_{s}>0 \\
C_{0}^{r}-C_{1}^{r} \xi_{s} \ln (1-\xi_{s}+e^{-7})+\left(C^{A}\left(A_{0}^{s}-A_{0}^{f}\right)+\bar{\sigma}\right) \xi_{s}+D_{0}^{r}(1-\|\boldsymbol{N}\|) & \text { for } \dot{\xi}_{s}<0
\end{cases}
\tag{39}
$$

where $C_{0}^{f / r}$ and $C_{1}^{f / r}$ are constants that direct the kinetics of mechanically induced forward/reverse transformation/orientation in an exponential manner. The quantity $e^{-7}=0.001$ is considered in Eq. (39) to remove logarithmic singularity at the end/start of forward/reverse martensitic transformation/orientation. The constant coefficients $D_{0}^{f / r}$ adjust surface shape of anisotropic martensitic transformation/orientation $(\|\boldsymbol{N}\| \neq 1)$.

In order to replicate the transformation strain anisotropy of SMAs and the asymmetry behavior in tension-compression, the magnitude of $\boldsymbol{N}$, i.e., $\|\boldsymbol{N}\|$, is restricted using a function introduced by Taillard *et al.* (2008) as:

$$
\|\boldsymbol{N}\|=\frac{g(-1)}{\|\boldsymbol{D}: \boldsymbol{n}\| g\left(-I_{3}(\boldsymbol{D}: \boldsymbol{n})\right)}
\tag{40}
$$

where $\boldsymbol{D}: \boldsymbol{n}$ indicates a dilated tensor as a linear mapping of $\boldsymbol{n}$. The affine mapping $\boldsymbol{D}$ is given such as the Hill's hyper ellipsoid becomes a hyper sphere in the dilated stress space. The transformation tensor $\boldsymbol{D}$ can be expressed in the Voigt notation as:

$$
\boldsymbol{D}=\frac{1}{c}\left[\begin{array}{ll}
\boldsymbol{A} & \boldsymbol{0} \\
\boldsymbol{0} & \boldsymbol{B}
\end{array}\right]
\tag{41}
$$

where

$$
\boldsymbol{A}=\left[\begin{array}{lll}
A_{11} & A_{12} & A_{13} \\
A_{12} & A_{22} & A_{23} \\
A_{13} & A_{23} & A_{33}
\end{array}\right]
$$

$$
\boldsymbol{B}=\left[\begin{array}{ccc}
\sqrt{L} & 0 & 0 \\
0 & \sqrt{M} & 0 \\
0 & 0 & \sqrt{N}
\end{array}\right]
$$

$$
A_{11}=\frac{2 a}{3} \cos ^{2}(\theta)+\frac{2 b}{3} \sin ^{2}(\theta)+\frac{1}{3}
$$

$$
A_{12}=A_{13}=-\frac{a}{3} \cos ^{2}(\theta)-\frac{b}{3} \sin ^{2}(\theta)+\frac{1}{3}
$$

$$
A_{22}=A_{33}=\left(\frac{a}{6}+\frac{b}{2}\right) \cos ^{2}(\theta)\left(\frac{a}{2}+\frac{b}{6}\right) \sin ^{2}(\theta)+\frac{1}{3}
$$

$$
A_{23}=\left(\frac{a}{6}-\frac{b}{2}\right) \cos ^{2}(\theta)\left(-\frac{a}{2}+\frac{b}{6}\right) \sin ^{2}(\theta)+\frac{1}{3}
$$

$$
c=\sqrt{\frac{1}{2}\left[\left(A_{11}-A_{12}\right)^{2}+\left(A_{11}-A_{13}\right)^{2}+\left(A_{12}-A_{13}\right)^{2}\right]}
$$

(42)

in which $a, b, \theta, L, M$ and $N$ are considered as anisotropic parameters.

In Eq. (40), $I_{3}$ has a form similar to the third strain tensor invariant defined as:

$$
I_{3}(\boldsymbol{D}: \boldsymbol{n})=3 \sqrt{6} \frac{\operatorname{det}(\boldsymbol{D}: \boldsymbol{n})}{(\|\boldsymbol{D}: \boldsymbol{n}\|)^{3}}
$$

(43)

Also, the convex criterion of $g\left(I_{3}\right)$ has been adopted to describe the well-known tension-compression asymmetry as:

$$
g\left(I_{3}\right)=\cos \left(\frac{\cos ^{-1}\left(1-p\left(1-I_{3}\right)\right)}{3}\right)
$$

(44)

where the material parameter $p$ is chosen to fit the tension-compression asymmetric behavior.

This parameter ranges between 0 associated to the symmetric tension-compression behavior and 1 for the case of maximal tension-compression asymmetry when transformation strain in compression is a half of the strain in tension. The value of $p$ is determined using the maximum uniaxial transformation strains in pure tension, $\varepsilon_{L}^{t}$, and in pure compression, $\varepsilon_{L}^{c}$, as the solution of:


$$
p=\frac{1}{2}\left(1-\cos \left(3 \cos ^{-1}\left(\frac{\varepsilon_{L}^{c}}{\varepsilon_{L}^{t}}\right)\right)\right)
\tag{45}
$$

Eqs. (40)-(45) show that $\|N\|$ becomes a function of six anisotropic and one asymmetric parameters. Note that, tension-compression asymmetry may affect shear yield transformation through Eq. (40) (Taillard *et al.*, 2008).

Experimental results (Sedlák *et al.*, 2012; Šittner *et al.* 2009a, 2009b) usually revealed that the stress for initiation of martensitic orientation has a decreasing trend against increase in temperature as depicted in Fig. 1 by dash line. It may be associated to changes of mobility of twin boundaries with temperature. Experiments also showed that the stress/temperature hysteresis width is decreased by increasing temperature/stress in pseudo-elastic and thermal cycle loadings. These responses can be replicated by considering parameter $C_{0}^{f / r}$ as a decreasing linear function of the temperature as:

$$
\begin{aligned}
& C_{0}^{f}(T)= \begin{cases}\sigma^{s}-C^{M} M_{0}^{s}+C^{A} T_{0}+\left(C^{M}-C^{A}\right) T & \text { for } \quad T>M_{s}^{0} \\
\sigma^{s}-C^{0} M_{0}^{s}+C^{A} T_{0}+\left(C^{0}-C^{A}\right) T & \text { for } \quad T \leq M_{s}^{0}\end{cases} \\
& C_{0}^{r}(T)= \begin{cases}C^{A}\left(A_{0}^{f}-T_{0}\right) & \text { for } \quad T>M_{s}^{0} \\
C^{A}\left(A_{0}^{f}-M_{0}^{s}-T_{0}\right)+C^{0} M_{0}^{s}+\left(C^{A}-C^{0}\right) T & \text { for } \quad T \leq M_{s}^{0}\end{cases}
\end{aligned}
\tag{46}
$$

where $C^{M}$ and $C^{0}$ denote slope of the transformation line to martensite in a geometrically linear stress-temperature phase diagram for $T \geq M_{0}^{s}$ and $T<M_{0}^{s}$ as shown in Fig. 1. Furthermore, $\sigma^{s}$ indicates the minimum stress required to start martensitic orientation/transformation at $T=M_{0}^{s}$.

Finally, the kinetics of thermally induced forward/reverse phase transformations $Y_{T}^{f / r}$ is assumed via a linear approximation as (Panico and Brinson, 2007):

$$
Y_{T}^{f / r}\left(\xi_{T}, \sigma_{v}\right)= \begin{cases}C^{A}\left(M_{0}^{s}-M_{0}^{f}\right) \xi_{T} & \text { for } \quad \dot{\xi}_{T}>0 \\ C^{A}\left(A_{0}^{f}-M_{0}^{s}\right)+\sigma_{v}+\left(A_{0}^{s}-A_{0}^{f}\right) \xi_{T} & \text { for } \quad \dot{\xi}_{T}<0\end{cases}
\tag{47}
$$

The final form of the finite-strain SMA model is summarized in Table 1. It should be noted that $\overline{\lambda}_{R}$ introduced in Table 1 is equivalent with the non-negative consistency parameter $\lambda_{R}$.

**Table 1.** Finite-strain constitutive model in the time-continuous frame.

$$
\begin{aligned}
&\left\{ \boldsymbol{S} = \left( \frac{1}{2} \lambda(\xi_{S}) tr(\boldsymbol{C}_{i}^{-1} \boldsymbol{C}) - \frac{3}{2} \lambda(\xi_{S}) - 3 \overline{\kappa}(\xi_{S})(T-T_{0}) - \mu(\xi_{S}) \right) \boldsymbol{C}_{i}^{-1} + \mu(\xi_{S}) \boldsymbol{C}_{i}^{-1} \boldsymbol{C} \boldsymbol{C}_{i}^{-1} \right. \\
&\left\{
\begin{aligned}
\dot{\boldsymbol{n}} &= \dot{\overline{\lambda}}_{R} (\overline{\boldsymbol{I}} : \boldsymbol{m}) \\
\boldsymbol{n} &= \frac{\boldsymbol{N}}{\|\boldsymbol{N}\|} \\
\boldsymbol{m} &= \frac{(S \boldsymbol{C} \boldsymbol{C}_{i}^{-1})^{D}}{\left\|(S \boldsymbol{C} \boldsymbol{C}_{i}^{-1})^{D}\right\|} \\
F_{R} &= 1 - (\boldsymbol{m} : \boldsymbol{n})^{2} - Y_{R}
\end{aligned}
\right. \\
&\left\{
\begin{aligned}
\|\boldsymbol{N}\| &= \frac{g(-1)}{\|\boldsymbol{D} : \boldsymbol{n}\| g(-I_{3}(\boldsymbol{D} : \boldsymbol{n}))} \\
Q_{S} &= (\boldsymbol{S} \boldsymbol{C} \boldsymbol{C}_{i}^{-1})^{D} : \boldsymbol{N} - \frac{1}{\varepsilon_{m}^{f}} \Lambda - \boldsymbol{C}^{A}(T-T_{0}) - \overline{\sigma} \xi_{S} \\
F_{S} &= Q_{S} \, \text{sgn}(Q_{S}) - Y_{S}^{f/r}(\xi_{S},\|\boldsymbol{N}\|)
\end{aligned}
\right. \\
&\left\{
\begin{aligned}
Q_{T} &= -\boldsymbol{C}^{A}(T-T_{0}) \\
F_{T} &= Q_{T} \, \text{sgn}(Q_{T}) - Y_{T}^{f/r}(\xi_{T},\sigma_{v})
\end{aligned}
\right. \\
&\left\{
\begin{aligned}
F_{R} \leq 0 \ , \ \dot{\overline{\lambda}}_{R} \geq 0 \quad , \ F_{R} \dot{\overline{\lambda}}_{R} &= 0 \\
F_{S} \leq 0 \ , \ \dot{\xi}_{S} = or \neq 0 \ , \ F_{S} \dot{\xi}_{S} &= 0 \\
F_{T} \leq 0 \ , \ \dot{\xi}_{T} = or \neq 0 \ , \ F_{T} \dot{\xi}_{T} &= 0
\end{aligned}
\right.
\end{aligned}
$$

### 2.4. Linearization of the finite-strain model

In this section, the developed finite-strain SMA model is reformulated into the small strain regime preserving the materially non-linear behavior.

When the deformation gradient tensor, $\boldsymbol{F} = \nabla \boldsymbol{u} + \boldsymbol{I}$, approaches the identity tensor $\boldsymbol{I}$ or displacement gradients $\nabla \boldsymbol{u}$ become infinitesimal, the quadratic order of $\nabla \boldsymbol{u}$ can be neglected. In this case, the difference between the reference and the deformed configuration becomes

insignificant and the Green-Lagrange strain tensor $\boldsymbol{E}$ coincides to infinitesimal strain tensor $\boldsymbol{\varepsilon}$ defined as:

$$
\boldsymbol{\varepsilon}=\frac{1}{2}\left(\nabla \boldsymbol{u}+(\nabla \boldsymbol{u})^{T}\right) \tag{48}
$$

By following the linearized assumption, $\boldsymbol{C}_{i}^{-1}$ can be derived as:

$$
\boldsymbol{C}_{i}^{-1} \cong-2 \boldsymbol{\varepsilon}_{i}+\boldsymbol{I} \tag{49}
$$

By using $\boldsymbol{C} \cong-2 \boldsymbol{\varepsilon}+\boldsymbol{I}$ and the above equation, $\boldsymbol{C}_{e}$ can be linearized as:

$$
\boldsymbol{C}_{e}=\boldsymbol{C} \boldsymbol{C}_{i}^{-1} \cong 2\left(\boldsymbol{\varepsilon}-\boldsymbol{\varepsilon}_{i}\right)+\boldsymbol{I} \tag{50}
$$

By equating $\boldsymbol{C}_{e}$ from the above relation with its original definition as $\boldsymbol{C}_{e} \cong-2 \boldsymbol{\varepsilon}_{e}+\boldsymbol{I}$, one obtains:

$$
\boldsymbol{\varepsilon}=\boldsymbol{\varepsilon}_{e}+\boldsymbol{\varepsilon}_{i} \tag{51}
$$

This relation implies the general assumption of additivity of strains within the small deformation regime.

Regarding the stress measures, it can be easily demonstrated that:

$$
\boldsymbol{S} \cong \boldsymbol{\sigma} \tag{52}
$$

It means that the second Piola-Kirchhoff and Cauchy stress measures coalesce.

In a similar linearization way, the SMA constitutive model can be derived within the small strain regime, which is not presented here for the sake of brevity. The small-strain model is summarized in Table 2.

Table 2. Small-strain constitutive model in the time-continuous frame.

$$\boldsymbol{\sigma}=\lambda\left(\xi_{S}\right) \operatorname{tr}(\boldsymbol{\varepsilon}) \boldsymbol{I}+2 \mu\left(\xi_{S}\right)\left(\boldsymbol{\varepsilon}-\boldsymbol{\varepsilon}_{i}\right)-3 \overline{\boldsymbol{\kappa}}\left(\xi_{S}\right)\left(T-T_{0}\right)$$

$$
\left\{\begin{aligned}
\dot{\boldsymbol{n}} & =\dot{\overline{\lambda}}_{R}(\overline{\boldsymbol{I}}: \boldsymbol{m}) \\
\boldsymbol{n} & =\frac{\boldsymbol{N}}{\|\boldsymbol{N}\|} \\
\boldsymbol{m} & =\frac{\boldsymbol{\sigma}^{D}}{\left\|\boldsymbol{\sigma}^{D}\right\|} \\
F_{R} & =1-(\boldsymbol{m}: \boldsymbol{n})^{2}-Y_{R}
\end{aligned}\right.
$$

$$
\left\{\begin{aligned}
\|\boldsymbol{N}\| & =\frac{g(-1)}{\|\boldsymbol{D}: \boldsymbol{n}\| g\left(-I_{3}(\boldsymbol{D}: \boldsymbol{n})\right)} \\
Q_{S} & =\boldsymbol{\sigma}^{D}: \boldsymbol{N}-\frac{1}{\varepsilon_{m}} \Lambda-C^{A}\left(T-T_{0}\right)-\overline{\boldsymbol{\sigma}} \dot{\xi}_{S} \\
F_{S} & =Q_{S} \operatorname{sgn}\left(Q_{S}\right)-Y_{S}^{f / r}\left(\xi_{S},\|\boldsymbol{N}\|\right)
\end{aligned}\right.
$$

$$
\left\{\begin{aligned}
Q_{T} & =-C^{A}\left(T-T_{0}\right) \\
F_{T} & =Q_{T} \operatorname{sgn}\left(Q_{T}\right)-Y_{T}^{f / r}\left(\xi_{T}, \sigma_{v}\right)
\end{aligned}\right.
$$

$$
\left\{\begin{array}{l}
F_{R} \leq 0, \quad \dot{\overline{\lambda}}_{R} \geq 0 \quad, \quad F_{R} \dot{\overline{\lambda}}_{R}=0 \\
F_{S} \leq 0, \quad \dot{\xi}_{S}=o r \neq 0, \quad F_{S} \dot{\xi}_{S}=0 \\
F_{T} \leq 0, \quad \dot{\xi}_{T}=o r \neq 0, \quad F_{T} \dot{\xi}_{T}=0
\end{array}\right.
$$

### 2.5. Parameters identification

In this model, 24 material and kinetic parameters have been introduced including
$\lambda^{A}, \lambda^{M}, \mu^{A}, \mu^{M}, \bar{\kappa}^{A}, \bar{\kappa}^{M}, C^{A}, C^{M}, C^{0}, \sigma^{s}, \bar{\sigma}, \varepsilon_{L}(\varepsilon_{m}=\sqrt{\frac{3}{2}} \varepsilon_{L}^{t}), p, a, b, \theta, L, M, N, D_{0}^{f}, D_{0}^{r}, C_{1}^{f}, C_{1}^{r}$,
and $Y_{R}$. Lamè constants $\lambda^{A}, \lambda^{M}, \mu^{A}, \mu^{M}$ can be determined from uniaxial tests at martensite and
austenite phases. Also, $\bar{\kappa}^{A}, \bar{\kappa}^{M}$ can be specified through zero-stress thermal strain tests when
the material is pure austenite $(T \geq A_{0}^{f})$ and martensite $(T \leq M_{0}^{f})$. Three transformation lines of
$C^{0}, C^{M}, C^{A}$ and $\sigma^{s}$ can be determined by performing at least three uniaxial tests at $T<M_{0}^{s}$,
$T=M_{0}^{s}$ and $T>A_{0}^{s}$ in a loading and unloading manner. $\bar{\sigma}$ is set to approximately fit the plateau

slope in the stress-strain diagram while $C_{1}^{f}$ and $C_{1}^{r}$ are adopted to approximate smooth transitions. $\varepsilon_{L}^{t}$ and tension-compression asymmetric parameter of $p$ can be extracted from uniaxial tension and compression tests observing maximum transformation strain. $Y_{R}$ can be calibrated from a bi-axial normal-normal or normal-shear non-proportional test. Regarding to anisotropic parameters of $a, b, \theta, L, M, N$, six uniaxial normal and shear tests should be done by measuring maximum transformation strains. Using definition of strain as $\boldsymbol{E}_{i}=\varepsilon_{m} \xi_{S} \boldsymbol{n}\|\boldsymbol{N}\|$, where $\|\boldsymbol{N}\|$ is the function of $a, b, \theta, L, M, N$ via Eq.(40), a system of six equations are derived. By solving the system of questions, six anisotropic parameters can be determined. Finally, $D_{0}^{f}$ and $D_{0}^{r}$ are chosen to adjust surface shape of anisotropic martensitic transformation/orientation.

### 2.6. Time integration
The purpose behind developing constitutive models is to solve boundary value problems and simulate thermo-mechanical features of SMA structures. In this section, a general view of the numerical solution of the SMA model in both finite and small strain regimes is presented without concentrating on algorithmic problems. The key point is to impose an appropriate numerical time-integration method to the evolution equation of martensite variant reorientation. The non-linear material model is treated as a time-discrete strain-temperature-driven problem. The total time domain $[0, t]$ is divided into sub-increments and the evolutive problem is solved over the general interval $[^{n} t,^{n+1} t]$. Assuming the solution is known at time $^{n} t$ and $C($ or $\varepsilon)$ and $T$ at time $^{n+1} t$, the stress and the internal variables can be updated by solving the system of constitutive equations summarized in Tables 1 and 2.

The evolution equation for the preferred direction of martensite variants is discretized using the explicit forward-Euler integration rule as:

$$
{ }^{n+1} \boldsymbol{n}={ }^{n} \boldsymbol{n}+\Delta \overline{\lambda}_{R}\left({ }^{n} \overline{\boldsymbol{I}}:{ }^{n} \boldsymbol{m}\right)
\tag{53}
$$

in which

$$
\overline{\Delta} \lambda_{R}={ }^{n+1} \overline{\lambda}_{R}-{ }^{n} \overline{\lambda}_{R}
\tag{54}
$$

Eqs. (53) and (54) should be replaced with their counterparts in Tables 1 and 2. The solution of the time-discrete model is directed by implementing an elastic-predictor inelastic-corrector return-mapping algorithm details of which can be found in Bodaghi *et al.* (2014). First, an elastic trial state is checked while the internal variables stand constant. The trial values of the limit functions are calculated to investigate the admissibility of the trial state. If three limit functions become negative then the SMA behavior is elastic and the trial state is admissible. Otherwise, the step is inelastic and internal variables need to be updated through the solution of non-linear system of algebraic equations. This can be done implementing an iterative technique such as Newton-Raphson method. As the main objective of this article is to propose the constitutive model without considering algorithmic problems, the non-linear system of equations are solved using the function `fsolve` in the optimization toolbox of the $MATLAB^{\circledR}$ code.

## 3. Computational Results

In this section, extensive numerical results are presented to assess predictive capabilities of the developed SMA model in simulating experimental observations. In particular, Section 3.1 deals with a comparative study between present predictions and experimental data for uniaxial compression tests of NiTi parts manufactured by 3D printing SML process (Dadbakhsh *et al.*, 2016). In Section 3.2, some comparative studies between computational simulations and

experimental data (Šittner et al., 2009a, 2009b) on NiTi wires under uniaxial tension, combined tension-torsion and heating-cooling paths are presented. Finally, in Section 3.3, the model is applied to a real-world application by conducting simulations of an NiTi helical spring actuator subject to stretching and the results are compared to experiments (Frost et al., 2016). It should be mentioned that the thermo-mechanical behaviors of NiTi specimens under tensile, compressive and thermal loadings are simulated at the Gauss point level by assuming the uniform stress response corresponding to a given strain state. On the other, however, the numerical simulations of the NiTi wire under combined tension-torsion and of NiTi spring under tension require solution of boundary value problems since there are strain gradients within NiTi devices. To this end, in-house FE solutions are derived by computational programming through $MATLAB^{\circledR}$. The temperature field is also considered in a spatially homogeneous manner. Finally, in this work, $T_{0}$ is approximately considered as $(M_{s}^{0}+A_{f}^{0})/2$, which is consistent with experimental observations (Tong and Wayman, 1974).

### 3.1. Isothermal uniaxial compression tests of 3D printed NiTi parts
This section is dedicated to investigate the compression behavior of the 3D printed NiTi parts numerically and experimentally. The parts were oriented horizontal $(0^{\circ})$, at an angle $(45^{\circ})$, and vertical $(90^{\circ})$ on the SLM building plane (Dadbakhsh et al., 2016). Four SMA characteristic temperatures were determined by differential scanning calorimetric techniques as presented in Table 3 for case I. Details of the material characterization and 3D printing SLM process can be found in Dadbakhsh et al. (2016).

**Table 3.** Material parameters adopted from experiments.

<table>
<thead>
  <tr>
    <th>Parameter</th>
    <th>Case I</th>
    <th>Case II</th>
    <th>Unit</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>$M_0^f , M_0^s , A_0^s , A_0^f$</td>
    <td>-55, -8, -2, 23</td>
    <td>-24, -22, -17, -13</td>
    <td>$^\circ$C</td>
  </tr>
  <tr>
    <td>$\lambda^A , \lambda^M$</td>
    <td>6, 12</td>
    <td>29, 15</td>
    <td>GPa</td>
  </tr>
  <tr>
    <td>$\mu^A , \mu^M$</td>
    <td>4, 10</td>
    <td>19, 12</td>
    <td>GPa</td>
  </tr>
  <tr>
    <td>$\bar{\kappa}^A , \bar{\kappa}^M$</td>
    <td>-</td>
    <td>-0.1, -0.1</td>
    <td>MPa/$^\circ$C</td>
  </tr>
  <tr>
    <td>$C^A , C^M , C^0$</td>
    <td>4, 4, -0.5</td>
    <td>6, 4.8, -0.5</td>
    <td>MPa/$^\circ$C</td>
  </tr>
  <tr>
    <td>$C_1^f , C_1^r$</td>
    <td>60, 70</td>
    <td>20, 30</td>
    <td>MPa</td>
  </tr>
  <tr>
    <td>$\sigma^s , \overline{\sigma}$</td>
    <td>50, 120</td>
    <td>250, 40</td>
    <td>MPa</td>
  </tr>
  <tr>
    <td>$D_0^f , D_0^r$</td>
    <td>150, 0</td>
    <td>200, 200</td>
    <td>MPa</td>
  </tr>
  <tr>
    <td>$a, b, \theta$</td>
    <td>1.45, 1.45, 0</td>
    <td>1, 1, 0</td>
    <td>-</td>
  </tr>
  <tr>
    <td>$L, M, N$</td>
    <td>1, 0.5, 0.5</td>
    <td>1, 2.04, 2.04</td>
    <td>-</td>
  </tr>
  <tr>
    <td>$\varepsilon_L^t , p$</td>
    <td>0.057, 0</td>
    <td>0.055, 0.8</td>
    <td>-</td>
  </tr>
  <tr>
    <td>$Y_R$</td>
    <td>-</td>
    <td>0.155</td>
    <td>-</td>
  </tr>
</tbody>
</table>

![](./images/813130793294495744_3.jpg)

Fig. 2. Uniaxial compressive tests on 3D printed NiTi parts: simulations versus experiments (Dadbakhsh et al., 2016).

The simulations of isothermal uniaxial compression tests at room temperature ($T=20^\circ$C) are

compared with experiments in Fig. 2. The model material parameters of the 3D printed NiTi

parts have been calibrated to match experimental data and reported in Table 3 for case I. Note that quantities of $Y_R$, $\bar{\kappa}$ and $p$ remain unknown due to lack of data on multi-axial non-proportional loading test, thermal strain test and uniaxial tension test, respectively. Fig. 2 reveals that 3D printing leads to anisotropic behaviors in both elastic and inelastic domains. As it can be seen, while the model predicts the same elastic responses for all three printing directions, it captures well anisotropic martensitic transformation of textured 3D printed $NiTi$ parts.

### 3.2. Tension, torsion and thermal tests of NiTi wires

In this section, five classes of experimental results of tension, combined tension-torsion and thermal tests on thin $NiTi$ wires are adapted and simulated by the present model. Experimental data are exploited from Roundrobin website (Šittner *et al.*, 2009b). The mechanical behaviors of $NiTi$ wires were first fixed by a training process. The stress-free transformation temperatures were specified using differential scanning calorimetric techniques, which are listed in Table 1 for case $II$. The reader is refereed to the Roundrobin SMA modelling website and paper for more details on the material and experimental processes as well as other experimental data (Šittner *et al.*, 2009a, 2009b).

![](./images/813130793294495744_4.jpg)

Fig. 3. Uniaxial complete tensile tests on $NiTi$ wires at various temperatures: simulations versus experiments (Šittner *et al.*, 2009b).

![](./images/813130793294495744_5.jpg)

Fig. 4. Uniaxial partial tensile tests on NiTi wires at various temperatures: simulations versus experiments (Šittner et al., 2009b).

### 3.2.1. Isothermal uniaxial tensile tests

Figs. 3 and 4 illustrate experimental results and model predictions for uniaxial complete and partial tension tests done on NiTi wires in a strain-controlled mode at various constant temperatures $-20$, 20 and $40^{\circ}\text{C}$. In complete loading conditions, NiTi wires at low and high temperatures are loaded to get 8% strain and then unloaded, see Fig. 3. Regarding to partial loading, the austenitic NiTi wire at $-20^{\circ}\text{C}$ is first loaded to achieve 4% strain and then unloaded leading to a residual inelastic strain as shown in Fig. 4. In the next stage, the specimen is loaded up to 8% strain followed by unloading to zero stress. In a similar mode, the samples in high temperatures 20 and $40^{\circ}\text{C}$ are loaded but unloading stage at the first round is limited to 2% strain as depicted in Fig. 4. The experimental tensile tests as shown in Fig. 3 have been employed for material parameters calibration. The extracted quantitative material parameters of the NiTi wires are given in Table 3 for case $II$. Note that $\bar{\kappa}$, $Y_{R}$ and anisotropic and tension-compression asymmetric parameters of $p$ and $a,b,\theta,L,M,N,D_{0}^{f},D_{0}^{r}$ as mentioned in Table 3 would be extracted from the future tests on thermal strain and multi-axial tests. Figs. 3 and 4 reveal that the model is able to accurately simulate transformation of martensite at low

temperature $-20^\circ$C and higher temperatures 20 and $40^\circ$C in a smooth and gradual manner. As it can be seen, the present model allows for an accurate production of SMA features by capturing length of the transformation plateau or strain hysteresis width, stress hysteresis width, transformation-dependent elastic properties, internal hysteresis loop and pseudo-elastic response.

![](./images/813130793294495744_6.jpg)

Fig. 5. Thermal-cycling tests on NiTi wires under various pre-loads: simulations versus experiments (Šittner *et al.*, 2009b).

### 3.2.2. Thermal cycle tests

Numerical and experimental results associated with thermal cycling of NiTi wires under pre-loads 300,400,500MPa are illustrated in Fig. 5. The thermal expansion coefficient, $\bar{\kappa}$, as given in Table 3 for case $II$ has been calibrated using these experimental data. As it can be seen, the thermal hysteresis area and decrease of temperature hysteresis width with enhancing stress from 400 to 500MPa are accurately predicted by the model. Furthermore, it is observed that the model is able to evaluate the strain actuation at high applied stresses 400, 500MPa. In conjugation with low stress level 300MPa, the model results in a strain actuation due to austenite-martensite phase transformation whereas the sample experienced a weak inelastic strain from austenite-R phase transformation. To overcome this discrepancy, R-phase transformation as well as twins accommodation mechanism should be considered in the constitutive model (Šittner *et al.*, 2009a).

![](./images/813130793294495744_7.jpg)

Fig. 6. Thermo-mechanical recovering stress tests on NiTi wires at upper (a) and lower (b) stress plateau: simulations versus experiments (Šittner et al., 2009b).

### 3.2.3. Recovering stress tests

Fig. 6 explores comparison between the model simulations and experimental data related to thermo-mechanical recovering stress tests. The NiTi wire is first stretched at $T=20\ ^{\circ}\text{C}$, up to 2% strain at plateau followed by two thermal cycles $(20\ ^{\circ}\text{C}\longleftrightarrow100\ ^{\circ}\text{C})$ at fixed pre-strain state and then unloaded at $T=20\ ^{\circ}\text{C}$. The presented results in Fig. 6 reveal that the model is capable of capturing the transformation slopes in the stress-temperature space as well as the maximum recovery stress observed in experiments. Furthermore, it is seen that the experimental difference in stress-temperature response at the first and second heating is successfully replicated by the model.

![](./images/813130793294495744_8.jpg)

Fig. 7. Comparison between simulations and experiments (Šittner *et al.*, 2009b) for combined tension-torsion tests on *NiTi* wires at constant tensile stress 70MPa and various constant temperatures: (a) torque versus angular displacement; (b) axial strain versus angular displacement.

![](./images/813130793294495744_9.jpg)

Fig. 8. The counterpart of Fig. 7 for constant tensile stress $379 MPa$.

#### 3.2.4. Non-proportional combined tension-torsion tests

The non-proportional combined tension-torsion tests on the NiTi wire under low and high tensile stresses 70 and 379MPa at three temperatures 20, 35 and $40\ ^{\circ}\text{C}$ are simulated and compared with the experiments in Figs. 7 and 8. The NiTi wire of diameter 0.1 mm and 50 mm length is discretized using 2000 nine-node prism elements (200 elements through wire cross section). Also, three Gauss integration points are used to evaluate material integrals through the volume of each SMA element. This set of tests consists of isothermal loading paths, with symmetrical angular displacement cycles applied to the NiTi wire under a constant pre-load state. The boundary conditions at the upper base of the NiTi wire are assumed to be fully clamped while the lower base is subjected to a combined tension-torsion load. Spatially and temporally constant temperature field is assumed in all elements. The numerical and experimental results in terms of torque-angular displacement and axial strain-angular displacement are depicted in Figs. 7(a), 8(a) and 7(b), 8(b), respectively. It is worthy to note that $Y_R$ and $p,a,b,\theta,L,M,N,D_0^f,D_0^r$ as mentioned in Table 3 have been determined using experimental data presented in Fig. 7. Note that, although there is no tension-compression test to directly calibrate the asymmetry parameter of $p$, it has been found to be 0.8 since it affects shear yield transformation through Eq. (40). In order to emphasize the improvements of the new constitutive modeling, predictions of the proposed model ignoring anisotropy/asymmetry features known as an isotropic/symmetric model are also included in Figs. 7 and 8.

The results presented in Fig. 7(a) reveal that the model with properties of anisotropic transformation and tension-compression asymmetry replicates well the torque moment for initiation and completion of forward/reverse martensitic phase transformation, the plateau length in angular displacements in torsion and pseudo-elastic behavior. However, it is seen that the

symmetric/isotropic model overestimates the length of the transformation plateau and consequently underestimates the completion torque of forward/reverse transformation. This is due to the strong anisotropy of highly textured NiTi wires, which deforms the yield martensitic transformation surface affecting transformation strains. The preliminary conclusion drawn from Fig. 7(b) is highly coupling between tension and torsion so that a large transformation axial strain is induced by torsion and fully recovered upon the torsion removal. It is seen that the asymmetric/anisotropic model is able to accurately simulate the shear-induced axial strain and its maximum value at the end of torsional loading step. On the other hand, however, it is found that the model with symmetry/isotropy assumptions always overestimates the induced axial strain. For instance, the symmetric/isotropic model results in 50% error for maximum axial strain compared with experimental data. Finally, as it can be seen in Fig. 7, both experimental and numerical torque and axial strain are symmetric with respect to the angular displacement applied in two opposite direction. It means that, tension-compression asymmetry does not affect the behavior of *NiTi* SMAs under positive-negative shear loadings.

The material parameters calibrated using experimental data in Figs. 3, 5 and 7 have been used to replicate experiments presented in Figs. 8-10. A good qualitative agreement is obtained with the same material parameters for other set experiments.

Regarding to tests under high stress level, conclusions similar to those concluded from Fig. 7(a) as previously stated about effects of strong texture in the NiTi wire on transformation strain generation can be achieved from Fig. 8(a). Furthermore, Fig. 8(a) shows that the torque moment does not vanish when the angular displacement returns to the origin during the torsional unloading. It implies that an inelastic strain exists in the specimen under a high axial stress, which induces the torque moment. This feature of the NiTi wire is successfully followed by the

model. Comparing the results presented in Figs. 7(b) and 8(b) reveal that, while the axial strain induced in the NiTi wire under low pre-load always follows the angular displacement-controlled path, it just follows the first torsion cycle in the case of high pre-load. As it can be seen in Fig. 8(b), the shear-induced axial strain has an increasing-decreasing trend during applying the first torsion cycle while it may have increasing and/or decreasing trend in the subsequent torsional cycles depending on the temperature. It means that the stress-induced martensitic phase transformation as an initial mechanism of deformation at the first torsion step shifts into transformation/reorientation of martensite variants during further cycling. During this non-proportional bi-axial path when the material under constant normal stress experiences torsional unloading, reorientation occurs. In this case, while the amount of oriented martensite remains constant, its preferred direction is changed so that shear inelastic strain transforms to normal inelastic strain. Fig. 8(b) reveals that the changes in material behaviors predicted by the model with asymmetric/anisotropic properties are in excellent qualitative and quantitative correlation with experiments. On the other hand, it can be found that the symmetric/isotropic model may not capture the real path and lead to maximum 100% error from a quantitative point of view. Finally, the results presented in this section emphasis the fact that modeling of tension-compression asymmetry and anisotropic transformation strain generation are essential to accurately predict the SMA behavior.

### 3.3. NiTi helical spring under stretching

In order to check and demonstrate the model capability in a more complex geometry, response of a real SMA-based device, *i.e.*, an NiTi helical spring actuator, is simulated and compared with experiments. A helical spring was shape set from 0.2mm thin NiTi wire whose material

properties have been presented in Table 3 for case II. A typified 2.6-coil helical spring with initial length of 3.9mm and initial outer diameter being 3.2mm was tested. For the sake of simulations, a one-coil spring is considered in the FE model and meshed by 10000 nine-node prism elements (200 elements through wire cross section). The equivalent results for 2.6-coil spring are generated by multiplying factor 2.6. Also, three Gauss integration points are implemented to evaluate material integrals through each SMA element volume. The boundary conditions applied in the real experiment are simplified and replaced by traditional periodic boundary conditions associated with an infinite spring. It implies that cross-sections stand planar and normal to the longitudinal axis in the deformation process. The temperature field is also specified in a spatially homogeneous manner. One end of the spring is assumed to be held while another end is subject to a tensile load. To restrict untwisting of the spring, the cross-section center of the end edges is kept on the plane defined by initial position of this point and the spring axis allowing the wire cross-section rotation.

![](./images/813130793294495744_10.jpg)

Fig. 9. Comparison between simulation and experiment (Frost et al., 2016) for NiTi helical spring under loading-unloading: (a) force-stroke; (b) force-strain.

First, thanks to large deformation observed in the present structure, importance of the finite-strain modeling is examined. To this end, mechanical responses of NiTi helical spring at $20^\circ\text{C}$ under stretching are simulated considering small strain and small strain accompanied by moderate rotation assumptions and compared with experimental data and those from the finite strain model. It should be mentioned that, in the case of small strain and moderately large rotation, only non-linear terms associated to transverse displacement are reserved, whereas all other geometrical non-linearities are ignored. The results are presented in terms of force-stroke and force-strain in Figs. 9(a) and 9(b). The available experimental data are also included in Fig. 9(a). The spring is stretched to get 20 mm displacement and then the load is released. Fig. 9(a) shows that the finite strain model replicates well experimental results while the model with small strain and small strain-moderate rotation assumptions underestimates the experimental force. This is due to the fact that when strain field is assumed linear (small strain) or when non-linearity is just set on transverse displacement, the model underestimates the structural stiffness so that the computational force predicts less than experimental one. As it can be seen, while the finite-strain model results in 2 $N$ force similar to the experiment, the small-strain model and the model with small strain and moderately large rotation assumption predict 0.4 and 0.68 $N$ for force. Regarding to the measured strain, Fig. 9(b) shows that all three models predict similar force before $\varepsilon=1.4\%$. However, by loading beyond this strain, the force paths are separated and the models with finite-strain, small-strain-moderate-rotation and small-strain assumptions predict maximum, intermediate and minimum force. The models with different assumptions predict different behaviors when the strain gets to $3\%$. As it can be observed, while the models with small-strain and finite-strain assumptions let force develop in a smooth manner, the assumption of small strain accompanied with moderate rotation leads to slope change in force curve. It is

found that models with small-strain, small-strain-moderate-rotation and finite-strain assumptions predict 3.2, 3.3 and 7.8 % strain at the end of loading. The larger strain, the larger stress, or force. Finally, this comparative study reveals the finite-strain modeling is an essential tool to accurately predict SMA behaviors when deformations are prominent.

![](./images/813130793294495744_11.jpg)

Fig. 10. Force-stroke response of NiTi helical spring under three loading-unloading cycles: simulations versus experiments (Frost et al., 2016).

![](./images/813130793294495744_12.jpg)

Fig. 11. The deformed shape of the NiTi spring during loading at various strokes.

$^{1}$ Unit: $mm$

![](./images/813130793294495744_13.jpg)

Fig. 12. Distribution of oriented martensite volume fraction (a) and equivalent von Mises stress (b) of the NiTi spring throughout wire cross section in the spring center at various strokes during loading-unloading.

$^{1}$ Unit: $mm$

Numerical and experimental force-stroke response of the NiTi spring at $20^\circ$C under three loading-unloading cycles is illustrated in Fig. 10. The deformed shape of the spring during loading stage at strokes 0, 5, 10, 15 and 19.5 mm is demonstrated in Fig. 11. 2-D contour plots of the oriented martensite volume fraction and equivalent von Mises stress within the cross-section of the NiTi wire at middle spring length at various strokes during loading-unloading are presented in Fig. 12. The results presented in Fig. 10 reveal a good correlation of experimental and computational responses so as to verify the accuracy of the proposed constitutive model. As it can found from Figs. 10 and 11, the spring experiences a long plateau and then hardens by enhancing force needed to gain the maximum stroke. This behavior is associated with the martensitic transformation nature of the NiTi. When the spring is loaded, it experiences major shear stress acting on wire cross-section and minor normal stress parallel to the wire axis. Due to this fact, a uniform distribution of martensite volume fraction and equivalent stress in circumferential direction is observed in Fig. 12 until stroke 10 mm in loading stage. As it can be seen, the shear stress induces martensitic phase transformation concentrated near the surface of the NiTi spring. By further loading beyond $u=10\mathrm{mm}$, the spring experiences a large rotation and moderate strain so that axial stress becomes dominant, see Fig. 11. In this bending-like stage, the shear-induced martensite transformation as initial deformation mechanism shifts into martensite reorientation. Fig. 12 displays that the distribution of martensite volume fraction and equivalent stress changes from a radial variation to a layered variation along the wire radius. It is worthy to mention that the tension-compression asymmetry and anisotropic strain generation affects the neutral axis in loading and shifts it from the wire cross-section center towards the outer surface.


### 4. Conclusion

The aim of this paper was to propose a robust 3D constitutive model for highly-textured NiTi-based SMA polycrystalline within the finite-strain regime. A multiplicative decomposition of the deformation gradient into elastic and inelastic components was assumed based on continuum thermodynamics with internal variables. The finite-strain constitutive equations were extracted using the second law of thermo-dynamics in the sense of the Clausius-Duhem inequality. They were expressed in terms of symmetric tensors simplifying the constitutive relations. A small strain counterpart of the model was derived by linearizing the constitutive equations. The time-discrete counterpart of the proposed constitutive model was addressed by integrating the evolution of martensite reorientation by means of explicit forward-Euler scheme.

In order to validate the accuracy of the model as well as the solution procedure, experimental responses of highly-textured NiTi 3D printed parts, wires and helical springs subjected to simple and complex loadings were replicated. To this end, two boundary-value problems were solved implementing in-house FE programs. It was shown that the finite-strain model is capable of capturing the major phenomena observed in experiments as pseudo-elasticity, martensitic transformation/orientation, reorientation of martensite variants, tension-compression asymmetry, anisotropic inelastic strain generation and phase-change-dependent elastic properties.

Furthermore, influence of finite-strain modeling was assessed by considering small strain and small strain and moderately large rotation assumptions and comparing the results with the experiment on the helical spring under stretching. The comparison study revealed that finite-strain consideration is essential to accurately simulate SMAs when deformations are large. Due

to the absence of similar models in the specialized literature, it is expected that the proposed model to be useful and efficient for design and analysis of highly-textured SMA devices.

## Acknowledgements

The work described in this paper was supported by the Research Grants Council of the Hong Kong Special Administrative Region, China (Project No. CUHK14202016) and The Chinese University of Hong Kong (Project ID: 3132823).

## References

Arghavani, J., Auricchio, F., Naghdabadi, R., Reali, A., Sohrabpour, S., 2010. A 3D finite strain phenomenological constitutive model for shape memory alloys considering martensite reorientation. Continuum Mech. Thermodyn. 22, 345-362.

Bodaghi, M., Damanpack, A.R., Aghdam, M.M., Shakeri, M., 2014. A robust three-dimensional phenomenological model for polycrystalline SMAs: Analytical closed-form solutions. Int. J. Eng. Sci. 82, 1-21.

Bodaghi, M., Damanpack, A.R., Liao, W.H., 2016. A robust macroscopic model for normal-shear coupling, asymmetric and anisotropic behaviors of polycrystalline SMAs. Smart Mater. Struct. 25, 075019 (19pp).

Chemisky, Y., Chatzigeorgiou, G., Kumar, P., Lagoudas, D.C., 2014. A constitutive model for cyclic actuation of high-temperature shape memory alloys. Mech. Mater. 68, 120-136.

Chatziathanasiou, D., Chemisky, Y., Chatzigeorgiou, G., Meraghni, F., 2016. Modeling of coupled phase transformation and reorientation in shape memory alloys under non-proportional thermomechanical loading. Int. J. Plast. 82, 192-224.

Cisse, C., Zaki, W., Ben Zineb, T., 2016. A review of constitutive models and modeling techniques for shape memory alloys. Int. J. Plast. 76, 244-284.

Dadbakhsh, S., Vrancken, B., Kruth, J.P., Luyten, J., Van Humbeeck, J., 2016. Texture and anisotropy in selective laser melting of NiTi alloy. Mater. Sci. Eng. A 650, 225-232.

Frost, M., Benešová, B., Sedlák, P., 2016. A microscopically motivated constitutive model for shape memory alloys: Formulation, analysis and computations. Math. Mech. Solids. 21, 358-382.

Hartl, D.J., Solomou, A., Lagoudas, D.C, Saravanos, D., 2012. Phenomenological modeling of induced transformation anisotropy in shape memory alloy actuators. Proc. SPIE 8342, Behavior and Mechanics of Multifunctional Materials and Composites.

Kan, Q., Yu, C., Kang, G., Li, J., Yan, W., 2016. Experimental observations on rate-dependent cyclic deformation of super-elastic NiTi shape memory alloy. Mech. Mater. 97, 48-58.

Lagoudas, D.C., Hartl, D.J., Chemisky, Y., Machado, L., Popov, P., 2012. Constitutive model for the numerical analysis of phase transformation in polycrystalline shape memory alloys. Int. J. Plast. 32-33, 155-183.

Mehrabi, R., Kadkhodaei, M., Elahinia, M., 2014. Anisotropic behavior of superelastic NiTi shape memory alloys; an experimental investigation and constitutive modeling. Mech. Mater. 77, 110-124.

Müller, C., Bruhns, O., 2006. Athermodynamic finite-strain model for pseudoelastic shapememory alloys. Int. J. Plast. 22(9), 1658-1682.

Nemat-Nasser, S., Guo, W.G., 2009. Superelastic and cyclic response of NiTi SMA at various strain rates and temperatures. Mech. Mater. 38, 463-474.

Panico, M., Brinson, L., 2007. A three-dimensional phenomenological model for martensite reorientation in shape memory alloys. J. Mech. Phys. Solids. 55 (11), 2491-2511.

Raniecki, B., Lexcellent, C., 1994. RL-models of pseudoelasticity and their specifications for some shape memory alloys. Euro J. Mech. A/Solids. 13(1), 21-50.

Saleeb, A.F., Dhakal, B., Dilibal, S., Owusu-Danquah, J.S., Padula II, S.A., 2015. On the modeling of the thermo-mechanical responses of four different classes of NiTi-based shape memory materials using a general multi-mechanism framework. Mech. Mater. 80, 67-86.

Sedlák, P., Frost, M., Benešová, B., Ben Zineb, T., Šittner, P., 2012. Thermomechanical model for NiTi-based shape memory alloys including R-phase and material anisotropy under multi-axial loadings. Int. J. Plast. 39, 132-151.

Šittner, P., Heller, L., Pilch, J., Sedlák, P., Frost, M., Chemisky, Y., Duval, A., Piotrowski, B., Ben Zineb, T., Patoor, E., Auricchio, F., Morganti, S., Reali, A., Rio, G., Favier, D., Liu, Y., Gibeau, E., Lexcellent, C., Boubakar, L., Hartl, D., Oehler, S., Lagoudas, D.C., Van Humbeeck, J., 2009a. Roundrobin SMA Modeling. In: Šittner, P., Heller, L., Paidar, V., (Eds.), ESOMAT 2009 - The 8th European Symposium on Martensitic Transformations. EDP Sciences, p. 08001, http://dx.doi.org/10.1051/esomat/200908001.

Šittner, P., Pilch, J., Heller, L., 2009b. < http://ofm.fzu.cz/roundrobin-sma-modelling>.

Stupkiewicz, S., Petryk, H., 2013. A robust model of pseudoelasticity in shape memory alloys. Int. J. Numer. Method. Eng. 93,747-769.

Taillard, K., Arbab Chirani, S., Calloch, S., Lexcellent, C., 2008. Equivalent transformation strain and its relation with martensite volume fraction for isotropic and anisotropic shape memory alloys. Mech. Mater. 40, 151-170.

Thamburaja, P., 2010. A finite-deformation-based phenomenological theory for shape-memory alloys. Int. J. Plast. 26, 1195-1219.

Tong, H.C., Wayman, C.M., 1974. Characteristic temperatures and other properties of thermoelastic martensites. Acta. Metall. 22, 887-896.

Zhao, S., Gu, L., Froemming, S.R., 2011. Assessment of shape memory alloy stent deployment in a stenosed artery. Mech. Mater. Eng. Faculty Publ. Paper 59.