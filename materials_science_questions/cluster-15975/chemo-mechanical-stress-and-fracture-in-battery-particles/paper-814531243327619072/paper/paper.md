![](./images/814531243327619072_1.jpg)

# Phase-field model for the two-phase lithiation of silicon

Fangliang Gao, Wei Hong*

Department of Aerospace Engineering, Iowa State University, Ames, IA 50011, USA

![](./images/814531243327619072_2.jpg)

## ARTICLE INFO

**Article history:**
Received 3 January 2016
Received in revised form
30 March 2016
Accepted 13 April 2016
Available online 19 April 2016

**Keywords:**
Lithiation
Phase-field model
Silicon anode
Fracture

## ABSTRACT

As an ideal anode material, silicon has the highest lithium-ion capacity in theory, but the broader application is limited by the huge volumetric strain caused by lithium insertion and extraction. To better understand the physical process and to resolve the related re-liability issue, enormous efforts have been made. Recent experiments observed sharp reaction fronts in both crystalline and amorphous silicon during the first lithiation half-cycle. Such a concentration profile indicates that the process is likely to be reaction lim-ited. Based on this postulation, a phase-field model is developed and implemented into a finite-element code to simulate the coupled large inelastic deformation and motion of the reaction front in a silicon electrode. In contrast to most existing models, the model treats both volumetric and deviatoric inelastic deformation in silicon as a direct consequence of the lithiation at the reaction front. The amount of deviatoric deformation is determined by using the recently developed kinetic model of stress-induced anisotropic reaction. By considering the role of stress in the lithiation process, this model successfully recovers the self-limiting phenomenon of silicon electrodes, and relates it to the local geometry of electrodes. The model is also used to evaluate the energy-release rate of the surface crack on a spherical electrode, and the result suggests a critical size of silicon nanoparticles to avert fracture. As examples, the morphology evolution of a silicon disk and a Si nanowire during lithiation are also investigated.

© 2016 Elsevier Ltd. All rights reserved.

## 1. Introduction

Lithium (Li) ion batteries have revolutionized the means of energy storage for portable electronics and electric vehicles in the past decades. The demand for even higher energy density has been constantly driving the development of new electrode ma-terials of higher capacity (Armand and Tarascon, 2008). Capable of attaining 4200 mAh g⁻¹ in theory (Cui et al., 2012; Obrovac and Christensen, 2004; Weydanz et al., 1999). Silicon (Si) is naturally an attractive candidate of the anode material (Tarascon and Armand, 2001; Goodenough and Kim, 2010; Li et al., 1999; Beaulieu et al., 2001; Limthongkul et al., 2003; Chan et al., 2008; Magasinski et al., 2010). However, the lithiation of Si is usually accompanied by a large volumetric expansion (up to ~270% for fully lithiated Si) (Beaulieu et al., 2001; Obrovac et al., 2004), and the consequent mechanical failure is believed to be the main cause of the capacity deterioration during cycling (Christensen and Newman, 2006; Liu et al., 2011; Lee et al., 2012; Zhao et al., 2012a). The intriguing phenomena in the Li-Si system have recently attracted a large volume of experimental and theoretical studies on the stress development and evolution during lithiation and delithiation processes (Bower et al., 2011; Brassart and Suo, 2013; Christensen and Newman, 2006; Cui et al., 2013; Liu et al., 2011, 2012a; Sethuramana et al., 2010a).

* Corresponding author.
E-mail address: whong@iastate.edu (W. Hong).

http://dx.doi.org/10.1016/j.jmps.2016.04.020
0022-5096/© 2016 Elsevier Ltd. All rights reserved.

During lithiation, at least three processes take place in Si: the electrochemical reaction between Si and Li, the migration of Li, and the elastic and inelastic deformation. The three processes are intrinsically coupled. For example, when a Li ion is migrating through the lithiated Si, each step can be regarded as a lithiation/delithiation reaction. Earlier studies are mostly built upon the coupled Li diffusion and elastic deformation, and focus on the diffusion-induced stress (e.g. Christensen and Newman, 2006; Zhang et al., 2007; Cheng and Verbrugge, 2009; Golmon et al., 2010; DeLuca et al., 2011; Ryu et al., 2011; Grantab and Shenoy, 2012; Haftbaradaran et al., 2010, 2011; Gao and Zhou, 2011). The results have demonstrated the size and rate dependencies of the reaction-induced stress field and the backward effect of stress to the diffusion or reaction rate. It has also been realized that it is impossible for the large volume expansion of Si during lithiation to be accommodated solely by elastic deformation. More recent development of theories often includes the considerations of finite-strain elastic-plastic deformation and reaction kinetics (Bower et al., 2011; Cui et al., 2012, Chen et al., 2014). With the Li migration described as Fickian diffusion, all the aforementioned models would predict a single-phase process, in which Si is lithiated gradually throughout the entire thickness. However, recent experimental observations show that the initial lithiation of Si, either crystalline (c-Si) or amorphous (a-Si), exhibits a two-phase process: the material is divided into the unreacted and the resultant phases by a clear reaction front, through which the Li concentration changes sharply (Limthongkul et al., 2003; Li et al., 2000; Liu et al., 2012a, 2012b; McDowell et al., 2013; Sun et al., 2013; Wang et al., 2013). Similar phenomena are often observed in processes limited by reactions at the interface (Bai and Bazant, 2014). Approaches taken to model the two-phase lithiation of Si include the introduction of a composition-dependent diffusivity with very low value in the unlithiated Si phase (Liu et al., 2011, 2012b), and explicitly addressing the reaction-induced discontinuities at the reaction front ( Zhao et al., 2012a; Cui et al., 2013). While both approaches results in the separated phases and related phenomena similar to those observed, the mathematical difficulties such as the numerical stiffness caused by the large difference in time scales and the tracking of moving boundaries have limited the computation to lower dimensions or relatively simple geometries.

Another point of interest in the lithiation process is the inelastic deformation associated with reaction. If Si undergoes isotropic volume expansion during lithiation, the large volume expansion across the reaction front could never be accommodated elastically. An approach often taken is to allow plastic flow in the resultant $Li_xSi$ (and in an intermediate state) when the stress exceeds a critical level, namely the yield strength (Brassart and Suo, 2013; Cui et al., 2013; Chen et al., 2014). However, to match experimental results, the yield strength needs to be taken as composition and kinetics dependent (Brassart and Suo, 2013), and the value is much lower than that of mechanical stress-induced yielding (Zhao et al., 2011). Moreover, recent observations (Pharr et al., 2014) showed a clear dependence of the resultant stress on the rate of lithiation, which does not fit into the existing framework of stress-induced plastic flow. Alternatively, a recently proposed model suggests that the lithiation reaction alone could result in anisotropic inelastic deformation, even when the reacting Si is amorphous (Hong, 2015). Because of the mismatch-induced deviatoric stress, the reaction with anisotropic deformation at certain orientation is experiencing higher driving force and is thus faster. In the process of two-phase lithiation, although the precise nature of the deformation mechanism in the reaction front is less conclusive, the consequence is significant to the stress development in Si anodes. It is evident that: (a) inelastic deformation with finite deviatoric component is present in the resultant immediately after the reaction front, and (b) such inelastic deformation is very different from the conventional defect-mediated plasticity in other materials and in the resultant $Li_xSi$ out of the reaction front.

Built upon the kinetic model of anisotropic reaction (Hong, 2015), this paper abandons plastic flow at the reaction front and seeks an alternative approach to modeling the two-phase lithiation process of Si. By incorporating the kinetic model into a field theory with coupled reaction and elastic deformation, the structural evolution and stress redistribution can be computed in complex geometries. The backward effect of mechanical constraints and stress field to the reaction can also be revealed. To circumvent the difficulty of distinguishing between reaction and diffusion as in the kinetic model (Hong, 2015), the current paper will start by postulating the process to be reaction-limited, and the composition in each phase homogeneous. By using a phase-field method with a scalar phase field varying continuously from the reactant phase (pure Si) to the resultant phase ($Li_xSi$), the moving reaction front is represented by the transition region with certain characteristic thickness. Phase-field methods are widely used in modeling reaction, phase transition, and morphological evolution (Karma and Rappel, 1998; Boettinger et al., 2002; Chen, 2002). In contrast to the approach of solving the coupled diffusion and elastic-plastic deformation problem (Anand, 2012), which has also been applied in studying Li electrode materials (Di Leo et al., 2014; Chen et al., 2014), here a reaction-limited process is taken to be the starting point, and the phase field variable is used just as a means of tracking the reaction front, similar as that in modeling liquid-phase electrochemical reactions (Guyer et al., 2004a, 2004b).

It should be admitted that the reaction-limited process is only an assumption, which is applicable to relatively small samples or the early lithiation sage of a large sample. Even though the migration of Li in lithiated layer is relatively fast, it will ultimately become the limiting mechanism. In those cases, a fully couple diffusion-reaction model will have to be used to represent the true physical process.

## 2. The model

### 2.1. Phase field for the state of charge

In contrast to the existing models that consider concurrent diffusion and reaction (Brassart and Suo, 2013; Zhao et al.,

2012b), the current model only considers the reaction kinetics and is thus only applicable to the reaction-limited two-phase lithiation, which is often observed during the first lithiation of crystalline and amorphous Si (Limthongkul et al., 2003; Li et al., 2000; Liu et al., 2012a, 2012b; McDowell et al., 2013; Sun et al., 2013; Wang et al., 2013). The chemical lithiation reaction under consideration is (Zhao et al., 2012a; McDowell et al., 2012, 2013)

$$x \mathrm{Li}+\mathrm{Si} \rightarrow \mathrm{Li}_{x} \mathrm{Si}. \tag{1}$$

It is assumed that the availability of Li ions is abundant and the kinetic process is limited by the reaction (1) in the narrow reaction front. Such an assumption is generally true for nanostructured electrodes (McDowell et al., 2013; Wang et al., 2013) given the relatively high diffusivity in $\mathrm{Li}_{x} \mathrm{Si}$ (Zhao et al., 2012a).

To differentiate between the reactant and resultant phases, we introduce a continuous scalar phase field $\phi(\mathbf{X}, t)$, which varies from $\phi=0$ in the reactant (pure Si) to $\phi=1$ in the resultant $(\mathrm{Li}_{x} \mathrm{Si})$. The separated phases are enabled mathematically through a double-well energy function

$$W_{\mathrm{DW}}(\phi)=16 w_{0} \phi^{2}(1-\phi)^{2}, \tag{2}$$

With $w_{0}$ being the height of the artificial energy barrier. The finite thickness of the phase boundary is regulated through the commonly invoked gradient energy

$$W_{\mathrm{G}}(\phi)=k|\nabla \phi|^{2}. \tag{3}$$

The competition between the two energies, $W_{\mathrm{DW}}$ and $W_{\mathrm{G}}$, determines a length scale $l_{0}=\sqrt{k / w_{0}}$, which measures the characteristic thickness of the phase boundary, i.e. the reaction zone. In equilibrium, neither energy function contributes to the thermodynamics of the homogeneous phases, and the excess energy per unit area of the transition zone, $\sim k^{2} / w_{0}$, acts as the interface energy of the $\mathrm{Si}-\mathrm{Li}_{x} \mathrm{Si}$ phase boundary.

Here, neither the double-well energy function nor the energy barrier carries any physical significance. They are introduced, in conjunction with the gradient energy $W_{\mathrm{G}}$, just to form the relatively sharp interface between the unreacted and resultant phases. In the current paper, the mathematical more challenging kinetics-induced sharp reaction front is replaced by a thermodynamically stable interface between co-existing phases. As $W_{\mathrm{DW}}$ and $W_{\mathrm{G}}$ take non-zero values only at the interface, they do not alter the physics of either phases, or contributes to the motion of a straight reaction front between two phases. It should also be noted that amorphous Si often follows a two-step lithiation process, and the distribution of Li concentration is much more gradual without a sharp phase boundary during the second step (Wang et al., 2013). Such a two-step process can also be modeled within the same framework (e.g. by extending the energy function over a larger range of $\phi$). For simplicity and clarity of presentation, in this paper, we limit the description to only two-phase lithiation, which is applicable to crystalline Si and the first step of amorphous Si.

The driving force of the reaction is characterized by energy function $W_{\mathrm{EC}}(\phi)$, which is defined as the change in the electrochemical free energy per unit volume of unconstrained Si associated with lithiation to state $\phi$ from the reference. For simplicity, we further assume the electrochemical potential of the Li ions to be constant throughout the lithiation process, and consequently, $W_{\mathrm{EC}}$ is linear in the Li concentration:

$$W_{\mathrm{EC}}(\phi)=-\zeta \frac{\xi}{\chi}. \tag{4}$$

Here $\xi$ represents the local composition of the partially lithiated $\mathrm{Si}$, i.e. the value of $\xi$ in $\mathrm{Li}_{\xi} \mathrm{Si}$. In the absence of elastic stress, $\zeta$ is the sole electrochemical driving force for the reaction, and a positive value of $\zeta$ drives lithiation (increase in $\phi$). Physically, the linearity assumption corresponds to the case when the entropic driving force over a Li ion is negligible compared to the electrostatic driving force, and the latter is proportional to the Li concentration.

As the phase field variable $\phi$ explicitly appears only in the artificial energy functions to capture the separated phases, its correlation to the local state of charge or the Li-ion concentration is more or less arbitrary. Here, the state of charge is interpolated between the unreacted and the resultant states through an interpolation function $f: \xi / x=f(\phi)$. The interpolation requires $f(0)=0$ and $f(1)=1$. In order not to alter the equilibrium compositions of either phase, the interpolation function $f$ takes vanishing derivatives on both ends, and a practical choice $f(\phi)=3 \phi^{2}-2 \phi^{3}$ is taken here. Such an approach is equivalent to the direct interpolation of the electrochemical free energy between the reactant and resultant phases, a practice commonly taken in phase-field models of electrochemical reactions (e.g. Guyer et al., 2004a, 2004b).

### 2.2. Deformation and mechanical equilibrium

It is well-known that the Lithiation process of Si involves large volume expansion, and thus stress is almost inevitable, especially when a geometric constraint is present. Despite the large inelastic deformation, we still regard both the reacting $\mathrm{Si}$ and the resultant $\mathrm{Li}_{x} \mathrm{Si}$ as continua. To track the deformation, imagine a field of markers attached to the relatively immobile $\mathrm{Si}$ atoms, identified through their coordinates $\mathbf{X}$ in the reference state at time $t=0$. The continuum motion of these markers throughout the reaction is then captured by the mapping from $\mathbf{X}$ to the current coordinates $\mathbf{y}: \mathbf{X} \rightarrow \mathbf{y}(\mathbf{X}, t)$, and the corresponding field of deformation by the deformation gradient

![](./images/814531243327619072_3.jpg)

Fig. 1. Multiplicative decomposition of the deformation gradient tensor at each material particle. This intermediate state, which could be achieved by relaxing a material particle elastically from the current state, may not correspond a continuous field of deformation, as the inelastic deformation between particles may not be compatible.

$$
F_{i K}(\mathbf{X}, t)=\frac{\partial y_{i}(\mathbf{X}, t)}{\partial X_{K}}. \tag{5}
$$

The deformation of a material particle consists of the contributions from both the reaction and the elasticity. Following the common practice in the context of finite deformation, we decompose the deformation gradient in a multiplicative manner

$$
F_{i K}=F_{m^{\prime} K}^{\mathrm{i}} F_{i m^{\prime}}^{\mathrm{e}}, \tag{6}
$$

where $\mathbf{F}^{\mathrm{i}}$ is the inelastic part caused by reaction and $\mathbf{F}^{\mathrm{e}}$ the elastic part. As illustrated by Fig. 1, the inelastic deformation gradient can be imagined as that from the reference state to an intermediate state, achieved by elastically relaxing the deformed particle after isolating it from the surrounding material. The intermediate state, indicated by the primed indices, does not necessarily correspond to a continuum state with compatible displacements.

Assuming linear elasticity, we write the elastic energy of a material particle in term of the Green-Lagrange strain tensor $\mathbf{E}=\frac{1}{2}\left(\mathbf{F}^{\mathrm{e} T} \cdot \mathbf{F}^{\mathrm{e}}-\mathbf{I}\right)$:

$$
W_{\mathrm{E}}(\phi, \mathbf{E})=J^{\mathrm{i}} w_{\mathrm{E}}=J^{\mathrm{i}}\left[\frac{\lambda}{2}\left(E_{m^{\prime} m^{\prime}}\right)^{2}+\mu E_{m^{\prime} n^{\prime}} E_{m^{\prime} n^{\prime}}\right], \tag{7}
$$

with $\lambda$ and $\mu$ being the lamé parameters, which may be composition dependent in general (Hertzberg et al., 2011). The reaction-induced volumetric expansion factor, $J^{\mathrm{i}}=\operatorname{det} \mathbf{F}^{\mathrm{i}}$, maps the energy density in the intermediate state $w_{\mathrm{E}}$ to the reference configuration.

The total potential energy of the Si-Li system is the integration of all energy functions over the entire domain $\Omega$:

$$
\Pi[\mathbf{y}, \phi]=\int_{\Omega}\left(W_{\mathrm{DW}}+W_{\mathrm{G}}+W_{\mathrm{EC}}+W_{\mathrm{E}}\right) d V. \tag{8}
$$

It is assumed that there is no externally applied mechanical load, and the electrochemical potential of Li ions is accounted for through $W_{\mathrm{EC}}$. In a state of known inelastic deformation, $\mathbf{F}^{\mathrm{i}}(\mathbf{X}, t)$, the equilibrium condition can be calculated by minimizing $\Pi$. The variation of $\Pi$ respect to $\mathbf{y}$ yields the mechanical equilibrium equation of the familiar form

$$
\frac{\partial S_{i K}}{\partial X_{K}}=0, \tag{9}
$$

where

$$
S_{i K}=\frac{\partial W_{\mathrm{E}}}{\partial F_{i m^{\prime}}^{\mathrm{e}}} H_{k m^{\prime}}^{\mathrm{i}}=H_{k m}^{\mathrm{i}} J^{\mathrm{i}}\left(\lambda E_{n^{\prime} n^{\prime}} F_{i m^{\prime}}^{\mathrm{e}}+2 \mu E_{m^{\prime} n^{\prime}} F_{i n^{\prime}}^{\mathrm{e}}\right) \tag{10}
$$

is the nominal stress, and $\mathbf{H}^{\mathrm{i}}=\left(\mathbf{F}^{\mathrm{i}}\right)^{-1}$ is the inverse of the inelastic deformation gradient. The variation of $\Pi$ respect to $\phi$ yields the coexisting states of reaction equilibrium, $\phi=0$ and $\phi=1$, as prescribed by the phase-field model.

### 2.3. Reaction kinetics

To study the inelastic deformation in an non-equilibrium process, let us further decompose $\mathbf{F}^\mathrm{i}$ into the volumetric and deviatoric parts, $\mathbf{F}^\mathrm{i} = \sqrt[3]{j^\mathrm{i}} \hat{\mathbf{F}}^\mathrm{i}$. The reaction-induced volumetric expansion $j^\mathrm{i}$ is a deterministic function of the local state of charge. Here for simplicity, $j^\mathrm{i}$ is assumed to be linear in $\xi$:

$$
j^{\mathrm{i}}=1+\theta \frac{\xi}{\chi}=1+\theta f(\phi),
\tag{11}
$$

where $\theta$ is the volumetric strain of the resultant $\mathrm{Li}_x\mathrm{Si}$ with respect to the reacting $\mathrm{Si}$ in a stress free state.

In a general non-equilibrium process, the laws of thermodynamics only dictate the reaction to be on the direction of lowering the total potential energy. The detailed kinetic relation between the speed of reaction measured in $\dot{\phi}$ and the energetic driving force $\delta\Pi/\delta\phi$ depends on the material behavior. For simplicity, here in this paper the linear kinetic relation with constant mobility $m$ is assumed:

$$
\dot{\phi}=-m \frac{\delta \Pi}{\delta \phi}.
\tag{12}
$$

Substituting the energy functions (2), (3), (4), and (7) into (12), we obtain the explicit form of the evolution equation

$$
\frac{\dot{\phi}}{m}=\frac{2 k \partial^{2} \varphi}{\partial X_{K} \partial X_{K}}-32 w_{0} \phi(1-\phi)(1-2 \phi)+\zeta \frac{\mathrm{d} f}{\mathrm{~d} \phi}-\left(w_{\mathrm{E}}-J^{\mathrm{i}} \sigma_{\mathrm{m}}\right) \theta \frac{\mathrm{d} f}{\mathrm{~d} \phi}
\tag{13}
$$

The first term on the right-hand side of Eq. (13) is the contribution from the gradient energy, the second that from the double-well energy, the third that from the electrochemical driving force, and the last from elastic driving force, in which $\sigma_{\mathrm{m}}=\frac{1}{3 j^{\mathrm{i}}} \frac{\partial W_{\mathrm{E}}}{\partial F_{i j}^{\mathrm{e}}} F_{i j}^{\mathrm{e}}$ is the mean stress measured in the intermediate state. The reaction rate is $\dot{\phi}$ independent of the stress deviator. Here for simplicity, a scalar mobility $m$ is taken to represent the orientation-independent reaction rate. If needed, it can be extended to an anisotropic tensor to account for the effect of crystalline orientation on reaction kinetics.

The deviatoric part of inelastic deformation $\hat{\mathbf{F}}^{\mathrm{i}}$, on the other hand, is often dependent on the then-current stress condition as well as the history of reaction. Even for amorphous Si, the presence of anisotropic driving forces, such as a deviatoric stress component, may lead to resultants of anisotropic deformation. While the theoretical framework could take any kinetic relation, the model taken in this paper closely follows Hong (2015).

Consider a few Si atoms forming a cluster. If the cluster is small enough, the deformation upon Li insertion can be anisotropic. For simplicity, we assume the local characteristic strain $\varepsilon^l$ of this microscopic transformation to be linear in the local state of charge $f(\phi)$, and further write it into a function of the phase field $\phi$: $\varepsilon^l = \varepsilon_0^l f(\phi)$, where $\varepsilon_0^l$ is the characteristic strain in the resultant phase. In the absence of deviatoric stress, the orientation of such deformations is randomly taken, so that the macroscopic strain exhibits isotropy after averaging. However, when a non-negligible stress deviator

$$
\tau_{i j^{\prime}}=\frac{1}{J^{\mathrm{i}}} \frac{\partial W_{\mathrm{E}}}{\partial F_{k i^{\prime}}^{\mathrm{e}}} F_{k j^{\prime}}^{\mathrm{e}}-\sigma_{\mathrm{m}} \delta_{i j^{\prime}}
\tag{14}
$$

is present, the free-energy has more reduction for transformation at particular orientations. Associated with the change in $\phi$, the excess energy reduction per unit reference volume, due to the deviatoric stress is given by $j^\mathrm{i} (\mathbf{Q} \cdot \boldsymbol{\tau} \cdot \mathbf{Q}^\mathrm{T}): \varepsilon_0^l \mathrm{d}f/\mathrm{d}\phi$, where $\mathbf{Q}$ is the rotation matrix of the local orientation. The reduction in total free energy, on the other hand, is given by $-\delta\Pi/\delta\phi$.

It is assumed that the partition of reactions follows a probability density proportional to the electro-chemo-mechanical driving force, namely the energy reduction caused by the reaction at a particular orientation. Integrating over the contributions from all orientations, we arrive at the kinetic relation for the deviatoric part of the inelastic strain rate (Hong, 2015)

$$
\dot{e}_{i^{\prime} j^{\prime}}^{\mathrm{i}}=-\alpha \frac{\mathrm{d} f}{\mathrm{~d} \phi} \dot{\phi} \frac{J^{\mathrm{i}} \tau_{i^{\prime} j^{\prime}}}{\delta \Pi / \delta \phi},
\tag{15}
$$

where $\alpha$ is a kinetic factor related to the local transformation strain $\varepsilon_0^l$, and characterizes the relative rate of the deviatoric transformation with respect to reaction rate. Instead of a material parameter, $\alpha$ is set by the actual lithiation rate. A fast reaction with $\alpha \approx 0$ would solely induce volumetric change, while a slow reaction with larger $\alpha$ relaxes the deviatoric stress faster. Applying the linear kinetics relation for the isotropic part of reaction, Eq. (12), the deviatoric kinetic equation is further reduced to

$$
\dot{e}_{i^{\prime} j^{\prime}}^{\mathrm{i}}=\alpha m \frac{\mathrm{d} f}{\mathrm{~d} \phi} J^{\mathrm{i}} \tau_{i^{\prime} j^{\prime}}.
\tag{16}
$$

The kinetic relation (15) resembles that of a viscous fluid, of which the deviatoric strain rate $\dot{\mathbf{e}}^{\mathrm{i}}$ is proportional to the stress deviator $\boldsymbol{\tau}$. A major difference between kinetic model (16) and a Newtonian fluid lies in the dependence on the reaction process. As the coefficient $\mathrm{d} f / \mathrm{d} \phi$ vanishes in both the pure reactant phase and the resultant phase, the inelastic deviatoric deformation is activated only at the interfacial layer, where the reaction is taking place and $\mathrm{d} f / \mathrm{d} \phi \neq 0$. Except for the contribution from the subsequent stress redistribution, the deviatoric strain rate does not affect the rate of reaction (13) directly.

In this paper, the deviatoric inelastic deformation $\hat{\mathbf{F}}^{\mathrm{i}}$ is used as the internal variables to characterize the state of reaction and to store the deformation history. Written in the intermediate configuration, and consisting of only the symmetric part, the deviatoric inelastic strain rate $\dot{\mathbf{e}}^{\mathrm{i}}$ is related to the changing rate of $\hat{\mathbf{F}}^{\mathrm{i}}$ as

$$
\dot{e}_{i^{\prime} j^{\prime}}^{\mathrm{i}}=\frac{1}{2}\left(\dot{\hat{F}}_{i^{\prime} K}^{\mathrm{i}} \hat{H}_{K j^{\prime}}^{\mathrm{i}}+\dot{\hat{F}}_{j^{\prime} K}^{\mathrm{i}} \hat{H}_{K i^{\prime}}^{\mathrm{i}}\right).
$$

As a local rigid-body rotation involves no composition change, separating it into elastic and inelastic part is unnecessary and nonphysical. By enforcing zero spin rate for inelastic deformation, i.e. The symmetry of $\hat{\mathbf{F}}^{\mathrm{i}} \hat{\mathbf{H}}^{\mathrm{i}}$, we can write out the evolution equation of the internal variables $\hat{\mathbf{F}}^{\mathrm{i}}$ directly as

$$
\dot{\hat{F}}_{i^{\prime} K}^{\mathrm{i}}=\dot{e}_{i^{\prime} j^{\prime}}^{\mathrm{i}} \hat{F}_{j^{\prime} K}^{\mathrm{i}}=\alpha m \frac{\mathrm{d} f}{\mathrm{~d} \phi} J^{\mathrm{i}} \tau_{i^{\prime} j^{\prime}} \hat{F}_{j^{\prime} K}^{\mathrm{i}}.
$$

At every material point, the ordinary differential equation (ODE) (18) serves as the governing equation for the evolution of the internal variables $\hat{\mathbf{F}}^{\mathrm{i}}$.

### 2.4. Material parameters and numerical implementation

Eqs. (9), (13), and (18) constitute a partial differential system for the phase field $\phi(\mathbf{X}, t)$, the displacement field $\mathbf{y}(\mathbf{X}, t)$, and the field of internal variables $\hat{\mathbf{F}}^{\mathrm{i}}(\mathbf{X}, t)$. Normalizing all lengths by the characteristic thickness of the interface $l_{0}$, all stresses and energy densities by Young's modulus $Y$, and time by $1 / m Y$, we can rewrite the governing equations in a dimensionless form as

$$
\dot{\phi}=\bar{w}_{0}\left[\frac{2 \partial^{2} \phi}{\partial \bar{X}_{K} \partial \bar{X}_{K}}-32 \phi(1-\phi)(1-2 \phi)\right]+\left(\bar{\zeta}-\bar{w}_{\mathrm{E}} \theta+J^{\mathrm{i}} \bar{\sigma}_{\mathrm{m}} \theta\right) 6 \phi(1-\phi),
$$

$$
\frac{\partial \bar{s}_{i K}}{\partial \bar{X}_{K}}=0,
$$

$$
\dot{\hat{F}}_{i^{\prime} K}^{\mathrm{i}}=6 \alpha \phi(1-\phi) J^{\mathrm{i}} \bar{\tau}_{i^{\prime} j^{\prime}} \hat{F}_{j^{\prime} K}^{\mathrm{i}},
$$

in which the symbols with overlines are the dimensionless counterparts of the corresponding physical quantities, e.g. $\bar{\sigma}_{\mathrm{m}}=\sigma_{\mathrm{m}} / Y$.

After normalization, the system contains three dimensionless parameters: the kinetic parameter $\alpha$, Poisson's ratio $\nu$, and the dimensionless measure of the interface energy $\bar{w}_{0}=w_{0} / Y$. In the following calculations, we will assume Poisson's ratio to be composition independent and take the representative value of $\mathrm{Si}, \nu=0.2$. The interface energy between $\mathrm{Si}$ and $\mathrm{Li}_{x} \mathrm{Si}$ has never been reported, and is practically difficult to measure. By using a representative value of the surface energy of ceramics $\sim 1 \mathrm{~J} \mathrm{~m}^{-2}$, the modulus of $\mathrm{Si} \sim 80 \mathrm{GPa}$ (Hertzberg et al., 2011), and the interface thickness $\sim 1.25 \mathrm{~nm}$ (Kim et al., 2014), we estimate the dimensionless interface energy to be $\bar{w}_{0} \sim 0.01$. The kinetic parameter $\alpha$ is left as a fitting parameter to match the deviatoric stress levels with experiments.

The dimensionless equations (19)-(21) are converted to the equivalent weak forms, and implemented into a finiteelement code through the commercial software COMSOL Multiphysics 4.3b. Computations have been carried out in 2D plane-strain, axisymmetric, and 3D domains. The phase-field variable $\phi$ is discretized with linear Lagrange elements, while the displacement field is interpolated to a second order. The internal state variables $\hat{\mathbf{F}}^{\mathrm{i}}$, and the corresponding ODEs of them, are solved and stored over the Gauss points of each element. An implicit scheme is adopted for time integrations.

## 3. Results and discussion

### 3.1. Lithiation of a constrained thin-film

As a first numerical example, we calculated the stress development in a biaxially constrained thin Si film during li- thiation. By comparing the model predictions to the abundant experimental measurements (Nadimpalli et al., 2013; Se- thuraman et al., 2010a, 2010b; Zhao et al., 2012b), we will extract the dimensionless kinetic parameter $\alpha$ for later simula tions. A typical average stress response during lithiation includes a rapid growth of compressive stress and then a level off of the stress till delithiation starts (Zhao et al., 2012b). With similar experiment set-up, Pharr et al. (2014) observed the monotonic increase of measured bi-axial stress with lithiation rate, which shows rate-sensitive inelasticity cannot be ex- plained by existing models. (The reactive flow model suggest a decrease of stress instead.) Also many models attribute this inelastic deformation to plasticity, but the yielding strength of silicon and Si-Li alloy under pure mechanical load is actually much higher than the plateau stress observed in experiment (Zhao et al., 2011). By introducing a kinetic model for ani- sotropic reactions, Hong (2015) proposes an alternative mechanism for the stress evolution without the need of invoking reaction-dependent plasticity, although a homogeneous state of deformation was assumed in the analysis. Recent studies have shown that the first lithiation process of Si exhibits a sharp reaction front, even for films as thin as 20 nm (McDowell et al., 2013; Wang et al., 2013). Such observations justify the basic assumptions of the current model.

Here, we assume both the deformation and the Li-ion concentration to be 1D fields, and set the $X_{1}$-axis through the film thickness. The boundary conditions on the Si-electrolyte interface are taken to be traction free $s_{11}=s_{21}=s_{31}=0$, and in the Li-rich phase $\phi=1$. Taking a representative composition $Li_{2}Si$ for the Li-rich phase (McDowell et al., 2013; Wang et al., 2012; Zhao et al., 2012b), we adopt the volumetric strain $\theta \approx 1.4$. The electrochemical driving force $\zeta$ is estimated from the po tential response to be $\zeta=0.05 Y_{0}$ (or $\sim 0.5$ eV per Si atom of volume $\Omega \approx 2 \times 10^{-29} ~m^{3}$ ) in the reference state (Sethuraman et al., 2010a, 2012). Notice that the resultant is not necessarily a thermodynamic equilibrium phase, its composition could vary from case to case and depend on kinetic processes as shown by experiments (McDowell et al., 2013; Sun et al., 2013; Wang et al., 2013). Therefore in the numerical calculations, we picked the compositions according to the corresponding experiments.

As expected, the result exhibits a step-like phase-field profile with a sharp reaction front moving from the electrode surface towards the pristine Si. In the non-lithiated phase where $\phi=0$, the stress is uniformly zero. In the lithiated phase behind the reaction front, where $\phi=1$, a close-to-uniform biaxial compressive stress is developed due to the large volume expansion induced by Li insertion. As plasticity is neglected and the only inelastic deformation is associated with reaction, the stress remains constant once lithiated. Fig. 2 plots the dimensionless compressive stress in the film $\sigma_{film } / Y_{0}$ as a function of the kinetic parameter $\alpha$, which describes the relative rate of the deviatoric inelastic deformation. As the deviatoric de- formation always relieves the mechanical driving force, and a faster deformation rate better relaxes the biaxial stress, the compressive stress in the lithiated phase is a monotonic decreasing function of $\alpha$. The trend that a higher compressive stress appears in the resultant phase in processes at a higher reaction rate (or smaller $\alpha$ ) agrees qualitatively with experimental observations (Pharr et al., 2014). Taking the representative values $\sigma_{film } \approx 1 GPa$ (Zhao et al., 2012b) and $Y=Y_{0} \approx 80 GPa$, from Fig. 2, we estimate the dimensionless kinetic parameter $\alpha$ under similar experimental conditions to be approximately 0.2.

Furthermore, by comparing the calculated Li flux to the experimental measurement (Zhao et al., 2012b), we can narrow down the range of the characteristic time $1 / m Y$ to be on the order of 1 s. The corresponding mobility is approximately

![](./images/814531243327619072_4.jpg)

Fig. 2. Biaxial compressive stress in the lithiated phase as a function of the kinetic parameter $\alpha$. Faster deviatoric deformation caused by anisotropic reaction relaxes the lateral compression caused by volume expansion of lithiation, and the stress is a monotonic decreasing function of $\alpha$. The stress is normalized by Young's modulus. By comparing to representative stress levels reported in the literature, we estimate the dimensionless kinetic parameter $\alpha$ to be approximately 0.2.

![](./images/814531243327619072_5.jpg)

Fig. 3. (a) Evolution of the radius of the Si core $r_c$ and the outer radius of the lithiated shell $r_s$ with dimensionless time $\tau$. Both radii are normalized by the interface characteristic length $l_0$. The inset sketches the axisymmetric model with an original partial radius $R$, which is taken to be $35l_0$ in this example. Under a relatively low driving force $\zeta$, the lithiation process slows down gradually due to the hydrostatic stress built up in the core. The lithiation stops at an equilibrium core size $r_{ce}$. (b) Relative equilibrium core size $r_{ce}/R$ as a function of the normalized particle size $R/l_0$ when the driving force $\zeta$ is kept constant. (c) Hoop stress distribution at $\tau=40$. The white and black contour line indicate the location of the reaction front and the original particle surface respectively. (d) Mean stress evolution. The horizontal axis $r/l_0$ is the dimensionless radial axis in the current configuration. The compressive stress near the reaction zone increases when the front gets deeper into the particle.

$0.01\ \text{GPa}^{-1}\text{s}^{-1}$. This parameter only provides a reference for the comparing between the model predictions and experimental results, and does not participate in any of the numerical calculation.

### 3.2. Lithiation of a spherical particle

To overcome the brittleness of bulk Si, various types of nano-structured Si electrodes have been proposed and tested (Liao et al., 2011; Liu et al., 2012b; McDowell et al., 2012, 2013; Sun et al., 2013; Wang et al., 2013). An interesting self-limiting phenomenon was also discovered recently in the lithiation of nanometer-sized Si electrode (McDowell et al., 2012; Liu et al., 2013): under a constant voltage, only part of the Si electrode of certain geometries can be lithiated.

Here, as a demonstration of the current model, we calculate the lithiation process of a spherical Si particle. The resultant phase is taken to be $\text{Li}_{3.75}\text{Si}$ as in the experiments, and the volumetric strain of the resultant is taken to be $\theta\approx2.7$ in this case (Beaulieu et al., 2001). We also adopt a composition-dependent Young's modules to describe the significant softening of $\text{Li}_\xi\text{Si}$ at high Li concentrations (Hertzberg et al., 2011). For simplicity, the Young's modules is set to be constant at 80 GPa within $0<\xi<2$ and then decreased linearly to 12 GPa for $\xi=3.75$. A traction-free boundary condition is prescribed on the outer surface of the particle. As the initial condition, the entire particle is of pure Si with $\phi=0$.

As illustrated by the inset of Fig. 3a, the axisymmetric computational domain encompasses a quarter of the cross section. A spherical particle of radius $R=35l_0$ before lithiation is lithiated from its outer surface under a constant applied driving force. In this example, the applied driving force $\zeta=0.15Y_0$ (or 1.5 eV per Si atom). Only the first lithiation process which exhibits a clear reaction front is modeled. The reaction front divides the domain into a pristine Si core with current radius $r_c$ and a shell of $\text{Li}_{3.75}\text{Si}$ with the outer radius $r_s$. The evolution of $r_c$ and $r_s$ during lithiation is then plotted as a function of the dimensionless time $\tau$ in Fig. 3a.

Initially, a thin layer of the Si is lithiated, the outer radius $r_s$ increases due to the lithiation-induced volume expansion, and the core radius $r_c$ recedes with the reaction front. Just as in the constrained 1D lithiation case in Section 3.1, the lithiated shell is initially under compression in the circumferential direction. The compressive hoop stress directs the reaction-induced inelastic deformation to elongate along the radial direction after the reaction front. However, as the reaction front is pushed further inwards, the hoop stress in the outer layer of the lithiated shell gradually decreases. This is due to the convex nature of the spherical particle, and the newly lithiated layer expands and pushes the outer layer outwards. With the smaller radius set by the reaction-induced inelastic deformation, the hoop stress in the outer layer gradually transitions from compressive to tensile, as shown by Fig. 3c. On the other hand, the tensile hoop stress in the outer layer of the lithiated shell brings additional compression to the region near the reaction front, as shown by Fig. 3d. The increased compression, in turn, would counterbalance the electrochemical driving force and slowdown the lithiation process, as inferred by Eq. (13). When the reaction proceeds deeper, the hydrostatic compression increases and retards the lithiation further. Under a relatively low electrochemical driving force, the lithiation process will be stopped ultimately and the entire system reaches an equilibrium. Such a self-limiting process agrees well with experimental observations (McDowell et al., 2012; Liu et al., 2013). A comparison between the lithiation of a thin film and that of a spherical particle clearly indicates the geometry dependence of the stress development and the self-limiting mechanism: the tensile stress in the lithiated shell and the self-limiting process usually take place on a sample with a convex surface.

The numerical results also suggest a size dependence of the equilibrium core radius $r_{ce}$ under the same electrochemical driving force. As shown by Fig. 3b, the normalized equlibrium core radius $r_{ce}/R$ increases monotonically with the particle size and then plateaus at a relatively large particle size. This prediction agrees qualitatively with the observation of McDowell et al. (2012) that a larger particle tends to have a relatively larger portion of non-lithiated part. In the case of a large particle, the transition zone near the reaction front is negligible when compared to the volume of the entire particle, and the particle size becomes the only length scale in the system. The equlibrium core size naturally scales with it. On the other hand, when the particle is small, the excess energy of the reaction front (similar as an interface energy which favors smaller core size) becomes more important. As a result, the relative size of the remaining core is smaller when the particle itself is small.

The state of stress not only explains the self-limiting phenomenon of lithiation, but also plays a key role in the fracture of Si electrodes. In general, the insertion of Li ions causes volume expansion and induces compressive stress, while extraction of Li ions during delithiation results in tensile stress and makes the electrode prone to fracture. If the lithiation of Si particle is a single-phase process with gradually varying Li concentration, the hoop stress should always be compressive (Cheng and Verbrugge, 2009), and thus a spherical particle should not fracture during lithiation. For a two-phase lithiation process, as shown by the numerical simulations, the hoop stress of the lithiated shell on a convex surface gradually turns to tensile during lithiation, and is then prone to fracture as seen in various experiments (Ryu et al., 2011; McDowell et al., 2012).

### 3.3. Fracture of si electrode in lithiation

The detailed information of the stress distribution given by the numerical model also allows us to study the fracture property of Si electrodes during lithiation and delithiation processes. Here as an example, we will further investigate the possibility of fracture in a spherical particle during the first lithiation process. As illustrated by Fig. 4a, the numerical model

![](./images/814531243327619072_6.jpg)

Fig. 4. (a) Schematic of half of the axisymmetric model for a spherical particle with a pre-existing surface crack of depth $a$. The original Si particle has radius $R=30l_0$, and the partially lithiated particle has a Si core of radius $r_c$ and a lithiated shell of outer radius $r_s$. (b) Normalized energy release rate as a function of the relative crack depth $a/R$, at various lithiation extents, indicated by the relative sizes of the core $r_c/R$. $G_{max}$ is the upper bound of the energy release rate that could be reached of cracks of any sizes.

![](./images/814531243327619072_7.jpg)

Fig. 5. Normalized maximum energy release rate of particles with different sizes $R/l_0$. The dash line shows a representative value of the fracture energy $\Gamma$, and intersects with the energy-release-rate curve at a critical radius $R^*$. For Si particles smaller than the critical size, fracture can be averted.

is almost identical to that in Section 3.2, expect the pre-existing surface crack of depth $a$ and a relatively high driving force ($\sim$3.5 eV per Si atom) so that the entire particle can be lithiated.

For simplicity, the simulation is carried out in two sequentially coupled steps. In the first step, the deformation field and reaction is solved simultaneously without considering the crack, just as the example in Section 3.2. The simulation is interrupted at various stages of charge, followed by the analysis of the second step, in which the crack is introduced by releasing the displacement boundary condition on the corresponding boundary. The modified deformation field is recalculated due to the introduction of the crack, but the Li-ion distribution is fixed at the result obtained from the first step. The effect of the crack to the lithiation process is neglected and only the stress concentration due to the presence of the crack is considered. By definition, the elastic energy release rate $G$ is evaluated approximately by calculating the reduction in the elastic energy associated with a small change in the crack area:

$$
G \approx-\frac{\Delta \int W_{\mathrm{E}} d V}{\pi a \Delta a}, \tag{22}
$$

where $\Delta \int W_{\mathrm{E}} d V$ is the change in the elastic energy, integrated over the hemisphere. The calculated dimensionless energy release rate, $G / l_{0} Y_{0}$, is plotted as a function of the dimensionless crack depth $a / R$ in Fig. 4b, for various lithiation depths (or states of charge).

As shown by Fig. 4b, the energy release rate is non-monotonic with respect to the crack depth. For a certain lithiation depth, only relatively shallow cracks (shallower than the reaction front) have positive energy release rate. This is because only the outer layer of the lithiated shell is experiencing a tensile hoop stress. Naturally, a further lithiated sample can have a deeper crack and thus a larger $G$. The maximum energy release rate $G_{\max }$ could be identified on the curve of the fully

![](./images/814531243327619072_8.jpg)

Fig. 6. Mises stress evolution during lithiation. Stress $\sigma_{\text {Mises }}$ was normalized by $Y_{0}$ : (a)-(d) are snapshots taken at dimensionless time $=100,250,600$, and 2000, respectively. The white lines are the contour lines of $\phi=0.5$, which shows the reaction front separating the lithiated part and the remaining pristine Si part.

![](./images/814531243327619072_9.jpg)

Fig. 7. Dimensionless mean stress evolution during lithiation: (a)-(d) are snapshot taken at $\tau$=100, 250, 600, and 2000, respectively.

lithiated state (under a large enough driving force). The value $G_{\text{max}}$ then represents the upper bound of the fracture driving force this particle can ever experience. If $G_{\text{max}}$ is smaller than the fracture energy $\Gamma$ of the material, the particle should be safe against all possible flaws and would never fracture during lithiation.

The same computation has been carried out over particles of various sizes, and the resulting $G_{\text{max}}$ is plotted as a function of the particle radius in Fig. 5. As expected, larger particles could experience higher driving force for fracture. From the monotonic relation between $G_{\text{max}}$ and $R$, one can determine the critical particle size $R^*$ to avert fracture. Here by taking a dimensionless fracture energy $\Gamma/l_0Y_0=0.1$, which corresponds to a dimensional value of approximately $10\ \text{J/m}^2$ (Pharr et al., 2013) by using material parameters as indicated in Section 2.4, we estimate the critical radius for particles against fracture to be $28l_0$ (or $\sim35$ nm). While the existence of the critical size agrees with experimental observations, the reported critical sizes are usually larger (Liu et al., 2012b; McDowell et al., 2012). It should be noted that our estimation is on the conservative side, as the safety requirement of averting cracks of all sizes may not be necessary. Pre-existing flaws or cracks are usually much smaller than the nanometer-sized particles. The larger reported values of critical particle size are likely to be due to either smaller pre-existing flaws or that the particle was not fully lithiated.

Here, the Griffith criterion is used under the assumptions that the process is governed by stress redistribution caused by the reaction-induced inelastic deformation, and linear elastic fracture mechanics is applicable. However, the actual physical process may also involves other effects of the lithium-ion insertion, such as corrosion and embrittlement, which have not been accounted for in the present model.

### 3.4. Lithiation of a circular disk

To demonstrate the power of the model in handling complex geometries, we will simulate the lithiation process of a cylindrical Si disk as one more numerical example, similar as the sample in the experiment by Wang et al. (2013). The cross section of the sample is modeled in an axisymmetric domain. The bottom of the disk is constrained to have zero

![](./images/814531243327619072_10.jpg)

Fig. 8. State of charge as a function of the dimensionless charging time $\tau$. The four circles, (a)-(d), correspond to the four states at which the snapshots of Fig. 6 or Fig. 7 are taken. The result shows an obvious self-limiting phenomenon.

![](./images/814531243327619072_11.jpg)

Fig. 9. (a-c) Cross-sectional Lithiation profiles a Si nanowire at different stages. The shade indicates the phase-field $\phi$. The shape of the entire cross section before lithiation is shown by the inset of (a). (d-f) Corresponding mean stress profiles.

displacement, and set to be impermeable for Li ions. The Li ions are only allowed to get into the disk through its top and lateral surface, where $\phi=1$ and $\theta \approx 1.8$ are set to represent the resultant phase, $Li_{2.5}Si$. While the actual experimental condition with constant total current (Wang et al., 2013) is difficult to apply in this model, a constant electrochemical driving force $\zeta=0.07Y_{0}$ is used as a timely approximate.

The calculated morphology evolution and stress distribution are plotted in Fig. 6, in which the deformation is shown to scale and the reaction front is indicated by the white contour line at $\phi=0.5$. The distributions of the mean stress in the corresponding states are shown in Fig. 7. Initially, the Si sample is lithiated through all exposed surfaces, forming a lithiated shell of nearly uniform thickness as in the 1D case. While the lithiation in the middle of the top surface is still uniform, the process near the outer rim soon becomes different. Due to the convex geometry of the disk near the rim, the lithiation process is similar to that of a spherical particle. The stress in the outer layer of the lithiated phase turns into tensile as it is pushed outwards by the newly lithiated material. The tensile hoop stress induces more compression near the reaction front, as shown by Fig. 7, and significantly retards the lithiation process. As a result, the propagation of the reaction front is slower at the rim region. Under a relatively low driving force, a non-lithiated part of annulus shape could remain. Just like that in a spherical particle, the self-limiting effect caused by the convex geometry of the sample would also slow down and even- tually stop the overall charging process, as shown by the state-of-charge plot in Fig. 8.

By comparing the result to that of a diffusion-limited model (Wang et al., 2013), it can be seen that even though the overall dome-like shape of the lithiated state looks similar, the detailed lithiation processes and the stress distributions are very different. One major difference is in the shape of the remaining non-lithiated region: the diffusion-limited model predicts a simply connected disk region in the middle of the sample, while our model predicts an annulus ring.

Although the current model does not account for plasticity, the resulting Mises stress distribution already shows where plastic deformation is likely to take place. Due to the constraint at the base of the sample, a concentration of the Mises stress appears at the vicinity of the lower edge, as shown by Fig. 6. Consequently, if plastic deformation is allowed, significant plastic shear or slip is likely to occur near the lower rim, and the sample will expand laterally at the base, just as observed in the experiment (Wang et al., 2013).

### 3.5. Lithiation of an electrode with complex geometry

The examples above all suggests a correlation between the lithiation process and the convexity of the local geometry. To better illustrate the effect of geometry, let us consider an example with both convex and concave surfaces. A nanowire of Si with a cross-shape cross section is lithiated from the surface, as sketched in the inset of Fig. 9a. Only a quarter of the cross section is modeled in a plane-strain setup, with symmetry boundary condition applied correspondingly. The overall size of the cross section is approximately $100l_0$ ($\sim$125 nm), and the edges are rounded with a radius of curvature of $8l_0$ ($\sim$10 nm). The material properties and the electrochemical driving force are taken to be the same as the example in Section 3.4. The resulting evolution process of the lithiated and non-lithiated phases is shown in Fig. 9a-c, and the corresponding mean stress distributions are shown in Fig. 9d and e.

The lithiation process in a sample relatively complex geometry exhibits three stages. In the early stage, as shown by Fig. 9a and d, the reaction everywhere is close to that on a flat surface. The constraints posed by the surface profile slightly affects the reaction rate through the mean-stress field (Fig. 9d). A slightly higher compression builds up near the concave region due to the space limitation for volume expansion, and slows down the reaction. The resultant layer is thus thicker in the convex regions in this stage, as shown by Fig. 9a. In the second stage, as the reaction front travels deeper into the bulk, the stress in the outer layer of the resultant turns into tension over the convex regions, as shown by Fig. 9d. Subsequently, the compressive stress in the unreacted core will retard the lithiation process locally. This effect is the same as that observed over spherical particles as discussed in Section 3.2. In this stage, however, such effect would not occur over concave regions. Instead, the same effect from geometric constraint prevails over concave regions just as in the early stage. In the third stage, when major part of the sample has been lithiated, and the remaining parts are isolated as shown by Fig. 9c, all remaining parts ultimately become convex. In this stage, tensile stress builds up over the surface of the entire sample, and the remaining unreacted parts are all under compression. The compression may cause the self-limiting effect which prevents further lithiation, if the electrochemical driving force is relatively low.

Generally, over convex regions such as the top and right corner of the cross section, when pushed outward by the newly lithiated Si, the outer layer of the lithiated phase experiences a transition from compressive to tensile mean stress. The tensile stress in the outer layer induces a compression in the non-lithiated phase, which retards its reaction, and ultimately results in a Si core which cannot be further lithiated due to the self-limiting mechanism. Over concave regions, the outer layer remains compressive even when the lithiated phase is relatively thick. However, due to the large deformation associated with the lithiation process, the distinction in local convexity may change over time. Therefore, there is no quantitative relation between the surface curvature and the rate of lithiation or the self-limiting effect. All remaining unreacted regions will ultimately become convex. After that, the stress at the reaction front ultimately becomes compressive, and limits the lithiation of the unreacted cores.

## 4. Conclusions

By postulating the two-phase lithiation process of Si electrode to be a reaction-limited process, a phase-field model is developed in the current paper. A continuous phase field is introduced to distinguish the pristine Si from the lithiated part, and the transition zone in between is used to track the moving reaction front. In contrast to most existing models, the inelastic deformation at the reaction front is considered as a natural consequence of the lithiation reaction, instead of the post-reaction plasticity. For this purpose, the recently developed theory of deviatoric-stress-induced anisotropic reaction is incorporated in the model. Such an approach allows one to separate the reaction-induced inelastic deformation at the reaction front from the regular stress-induced plasticity far away. The model has been implemented into a finite element code through the commercial software COMSOL Multiphysics, and is capable of simulating the co-evolution of the lithiation process and the accompanied elastic and inelastic deformation. Several numerical examples have been studied to illustrate the application of the model. In the constrained 1D lithiation case of a Si film, the results demonstrate a kinetics-dependent plateau stress in the lithiated part, and is used to determine a kinetic parameter by comparing to experiments. Through the spherical particle example, the model recovers the size-dependent self-limiting phenomenon as observed in experiments, and suggests it to be originated from the convexity of the sample geometry. By analyzing the stress evolution and calculating the elastic energy release rate of a pre-existing surface crack, the model is also used to determine the critical size to suppress crack propagation in Si nanoparticles. In the example of a Si disk, while the morphological change is consistent with existing models, the shape of the non-lithiated zone of a partially lithiated disk differs dramatically from that predicted by previous works: because of the self-limiting effect from the convex edges, the remaining Si exhibits the shape of an annulus. Such a unique phenomenon, once observed in experiments, would strongly support the validity of the current model. Finally, to illustrate the effect of local geometry, a Si nanowire with a cross section containing both convex and concave parts is studied. While the convex part further confirms the self-limiting effect, the concave part initially experiences slight retardation in reaction due to the geometric constraint. However, as lithiation proceeds, all remaining unreacted parts of a sample will ultimately become convex and will exhibit the self-limiting effect to certain extent. The lithiation of Si aside, the model is generally applicable to other material systems, in which phase transformations or solid-state chemical reactions are accompanied by large anisotropic inelastic deformation.

### References

Anand, L., 2012. A Cahn-Hilliard-type theory for species diffusion coupled with large elastic-plastic deformations. J. Mech. Phys. Solids 60, 1983-2002.

Armand, M., Tarascon, J.-M., 2008. Building better batteries. Nature 451, 652-657.

Bai, P., Bazant, M.Z., 2014. Charge transfer kinetics at the solid-solid interface in porous electrodes. Nat. Commun. 5, 3585.

Beaulieu, L.Y., Eberman, K.W., Turner, R.L., Krause, L.J., Dahn, J.R., 2001. Electrochemical and solid state letters: colossal reversible volume changes in lithium alloys. Electrochem. Solid-State Lett. 4 (9), A137-A140.

Boettinger, W.J., Warren, J.A., Beckermann, C., Karma, A., 2002. Phase-field simulation of solidification 1. Annu. Rev. Mater. Res. 32 (1), 163-194.

Bower, A.F., Guduru, P.R., Sethurman, V.A., 2011. A finite strain model of stress, diffusion, plastic flow, and electrochemical reactions in a lithium-ion half-cell. J. Mech. Phys. Solids 59, 804-828.

Brassart, L., Suo, Z.G., 2013. Reactive flow in solids. J. Mech. Phys. Solids 61, 61-77.

Chan, C.K., Peng, H.L., Liu, G., McIlwrath, K., Zhang, X.F., Huggins, R.A., Cui, Y., 2008. High-performance lithium battery anodes using silicon nanowires. Nat. Nanotechnol. 3, 31-35.

Chen, L.Q., 2002. Phase-field models for microstructure evolution. Annu. Rev. Mater. Res. 32 (1), 113-140.

Chen, L., Fan, F., Hong, L., Chen, J., Li, Y.Z., Zhang, S.L., Zhu, T., Chen, L.Q., 2014. A phase-field model coupled with large elasto-plastic deformation: application to lithiated silicon electrodes. J. Electrochem. Soc. 161, F3164-F3172.

Cheng, Y.T., Verbrugge, M.W., 2009. Evolution of stress within a spherical insertion electrode particle under potentiostatic and galvanostatic operation. J. Power Sources 190, 453-460.

Christensen, J., Newman, J., 2006. Stress generation and fracture in lithium insertion materials. J. Solid State Electrochem. 10, 293-319.

Cui, Z.W., Gao, F., Qu, J.M., 2012. A finite deformation stress-dependent chemical potential and its applications to lithium-ion batteries. J. Mech. Phys. Solids 60, 1280-1295.

Cui, Z.W., Gao, F., Qu, J.M., 2013. Interface-reaction controlled diffusion in binary solids with applications to lithiation of silicon in lithium-ion batteries. J. Mech. Phys. Solids 61, 293-310.

Di Leo, C.V., Rejovitzky, E., Anand, L., 2014. A Cahn-Hilliard-type phase-field theory for species diffusion coupled with large elastic deformations: application to phase-separating Li-ion electrode materials. J. Mech. Phys. Solids 70, 1-29.

DeLuca, C.M., Maute, K., Dunn, M.L., 2011. Effects of electrode particle morphology on stress generation in silicon during lithium insertion. J. Power Sources 196, 9672-9681.

Gao, Y.F., Zhou, M., 2011. Strong stress-enhanced diffusion in amorphous lithium alloy nanowire electrodes. J. Appl. Phys. 109, 014310.

Golmon, S., Maute, V., Lee, S.H., Dunn, M.L., 2010. Stress generation in silicon particles during lithium insertion. Appl. Phys. Lett. 97, 033111.

Goodenough, J.B., Kim, Y., 2010. Challenges for rechargeable Li batteries. Chem. Mater. 22, 587-603.

Grantab, R., Shenoy, V.B., 2012. Pressure-gradient dependent diffusion and crack propagation in lithiated silicon nanowires. J. Electrochem. Soc. 159, A584-A591.

Guyer, J.E., Boettinger, W.J., Warren, J.A., McFadden, G.B., 2004a. Phase field modeling of electrochemistry. I. Equilibrium. Phys. Rev. E 69 (2), 21603.

Guyer, J.E., Boettinger, W.J., Warren, J.A., McFadden, G.B., 2004b. Phase field modeling of electrochemistry. II. Kinetics. Phys. Rev. E 69 (2), 021604.

Haftbaradaran, H., Gao, H.J., Curtin, W.A., 2010. A surface locking instability for atomic intercalation into a solid electrode. Appl. Phys. Lett. 96, 091909.

Haftbaradaran, H., Song, J., Curtin, W.A., Gao, H.J., 2011. Continuum and atomistic models of strongly coupled diffusion, stress, and solute concentration. J. Power Sources 196, 361-370.

Hertzberg, B., Benson, J., Yushin, G., 2011. Ex-situ depth-sensing indentation measurements of electrochemically produced Si-Li alloy films. Electrochem. Comm. 13, 818-821.

Hong, W., 2015. A kinetic model for anisotropic reactions in amorphous solids. Extrem. Mech. Lett.

Karma, A., Rappel, W.J., 1998. Quantitative phase-field modeling of dendritic growth in two and three dimensions. Phys. Rev. E 57 (4), 4323.

Kim, S.P., Datta, D., Shenoy, V.B., 2014. Atomistic mechanisms of phase boundary evolution during initial lithiation of crystalline silicon. J. Phys. Chem. C 118, 17247-17253.

Lee, S.W., McDowell, M.T., Berla, L.A., Nix, W.D., Cui, Y., 2012. Fracture of crystalline silicon nanopillars during electrochemical lithium insertion. Proc. Natl. Acad. Sci. USA 109, 4080-4085.

Li, H., Huang, X.J., Chen, L.Q., Wu, Z.G., Liang, Y., 1999. A high capacity Nano- Si composite anode material for lithium rechargeable batteries. Electrochem. Solid-State Lett. 2, 547-549.

Li, H., Huang, X., Chen, L., Zhou, G., Zhang, Z., Yu, D., Mo, Y., Pei, N., 2000. The crystal structural evolution of nano-Si anode caused by lithium insertion and extraction at room temperature. Solid State Ion. 135, 181-191.

Liao, H.W., Karki, K., Zhang, Y., Cumings, J., Wang, Y.H., 2011. Interfacial mechanics of carbon Nanotube@Amorphous-Si coaxial nanostructures. Adv. Mater. 23, 4318-4322.

Limthongkul, P., Jang, Y.I., Dudney, N.J., Chiang, Y.M., 2003. Electrochemically-driven solid-state amorphization in lithium-silicon alloys and implications for lithium storage. Acta Mater. 51, 1103-1113.

Liu, X.H., Zheng, H., Zhong, L., Huang, S., Karki, K., Zhang, L.Q., Liu, Y., Kushima, A., Liang, W.T., Wang, J.W., Cho, J.-H., Epstein, E., Dayeh, S.A., Picraux, S.T., Zhu, T., Li, J., Sullivan, J.P., Cumings, J., Wang, C., Mao, S.X., Ye, Z.Z., Zhang, S., Huang, J.Y., 2011. Anisotropic swelling and fracture of silicon nanowires during lithiation. Nano Lett. 11, 3312-3318.

Liu, X.H., Wang, J.W., Huang, S., Fan, F., Huang, X., Liu, Y., Krylyuk, S., Yoo, J., Dayeh, S.A., Davydov, A.V., Mao, S.X., Picraux, S.T., Zhang, S., Li, J., Zhu, T., Huang, J.Y., 2012a. In situ atomic-scale imaging of electrochemical lithiation in silicon. Nat. Nanotechnol. 7, 749-756.

Liu, X.H., Zhong, L., Huang, S., Mao, S.X., Zhu, T., Huang, J.Y., 2012b. Size-dependent fracture of silicon nanoparticles during lithiation. ACS Nano 6, 1522-1531.

Liu, X.H., Fan, F.F., Yang, H., Zhang, S.L., Huang, J.Y., Zhu, T., 2013. Self-limiting lithiation in silicon nanowires. ACS Nano 7, 1495-1503.

Magasinski, A., Dixon, P., Hertzberg, B., Kvit, A., Ayala, J., Yushin, G., 2010. High-performance lithium-ion anodes using a hierarchical bottom-up approach. Nat. Mater. 9, 353-358.

McDowell, M.T., Lee, S.W., Harris, J.T., Korgel, B.A., Wang, C.M., Nix, W.D., Cui, Y., 2013. In situ TEM of two-phase lithiation of amorphous silicon nanospheres. Nano Lett. 13, 758-764.

McDowell, M.T., Ryu, I., Lee, S.W., Wang, C.M., Nix, W.D., Cui, Y., 2012. Studying the kinetics of crystalline silicon nanoparticle lithiation with in situ transmission electron microscopy. Adv. Mater. 24, 6034-6041.

Nadimpalli, S.P.V., Sethuraman, V.A., Bucci, G., Srinivasan, V., Bower, A.F., Guduru, P.R., 2013. On plastic deformation and fracture in Si films during electrochemical lithiation/delithiation cycling. J. Electrochem. Soc. 160, A1885-A1893.

Obrovac, M.N., Christensen, L., 2004. Structural changes in silicon anodes during lithium insertion/extraction. Electrochem. Solid-State Lett. 7, A93-A96.

Pharr, M., Suo, Z.G., Vlassak, J.J., 2013. Measurements of the fracture energy of lithiated silicon electrodes of Li-ion batteries. NanoLett 13, 5570-5577.

Pharr, M., Suo, Z.G., Vlassak, J.J., 2014. Variation of stress with charging rate due to strain-rate sensitivity of silicon electrodes of Li-ion batteries. J. Power Sources 270, 569-575.

Ryu, I., Choi, J.W., Cui, Y., Nix, W.D., 2011. Size-dependent fracture of Si nanowire battery anodes. J. Mech. Phys. Solids 59, 1717-1730.

Sethuramana, V.A., Chon, M.J., Shimshak, M., Srinivasan, V., Guduru, P.R., 2010a. In situ measurements of stress evolution in silicon thin films during electrochemical lithiation and delithiation. J. Power Sources 195, 5062-5066.

Sethuraman, V.A., Srinivasan, V., Bower, A.F., Guduru, P.R., 2010b. In situ measurements of stress-potential coupling in lithiated silicon. J. Electrochem. Soc. 157, A1253-A1261.

Sethuraman, V.A., Winkle, N.V., Abraham, D.P., Bower, A.F., Guduru, P.R., 2012. Real-time stress measurements in lithium-ion battery negative-electrodes. J.

Power Sources 206, 334–342.

Sun, C.F., Karki, K., Jia, Z., Liao, H.W., Zhang, Y., Li, T., Qi, Y., Cumings, J., Rubloff, G.W., Wang, Y.H., 2013. A beaded-string silicon anode. ACS Nano 7, 2717–2724.

Tarascon, J.M., Armand, M., 2001. Issues and challenges facing rechargeable lithium batteries. Nature 414, 359–367.

Wang, J.W., Liu, X.H., Zhao, K., Palmer, A., Patten, E., Burton, D., Mao, S.X., Suo, Z.G., Huang, J.Y., 2012. Sandwich-lithiation and longitudinal crack in amorphous silicon coated on carbon nanofibers. ACS Nano 6, 9158–9167.

Wang, J.W., He, Y., Fan, F., Liu, X.H., Xia, S., Liu, Y., Harris, C.T., Li, H., Huang, J.Y., Mao, S.X., Zhu, T., 2013. Two-phase electrochemical lithiation in amorphous silicon. Nano Lett. 13, 709–715.

Weydanz, W.J., Wohlfahrt-Mehrens, M., Huggins, R.A., 1999. A room temperature study of the binary lithium–silicon and the ternary lithium–chromium–silicon system for use in rechargeable lithium batteries. J. Power Sources 81–82, 237–242.

Zhang, X., Shyy, W., Sastry, A.M., 2007. Numerical simulation of intercalation-induced stress in Li-ion battery electrode particles. J. Electrochem. Soc. 154, A910–A916.

Zhao, K.J., Wang, W.L., Gregoire, J., Pharr, M., Suo, Z.G., Vlassak, J.J., Kaxiras, E., 2011. Lithium-assisted plastic deformation of silicon electrodes in lithium-ion batteries: a first-principles theoretical study. Nano Lett. 11, 2962–2967.

Zhao, K.J., Pharr, M., Wan, Q., Wang, W.L., Kaxiras, E., Vlassak, J.J., Suo, Z.G., 2012a. Concurrent reaction and plasticity during initial lithiation of crystalline silicon in lithium-ion batteries. J. Electrochem. Soc. 159, A238–A243.

Zhao, K.J., Tritsaris, G.A., Pharr, M., Wang, W.L., Okeke, O., Suo, Z.G., Vlassak, J.J., Kaxiras, E., 2012b. Reactive flow in silicon electrodes assisted by the insertion of lithium. Nano Lett. 12, 4397–4403.