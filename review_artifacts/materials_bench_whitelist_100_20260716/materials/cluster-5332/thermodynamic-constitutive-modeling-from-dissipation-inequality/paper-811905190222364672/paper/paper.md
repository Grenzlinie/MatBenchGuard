# Simple Model for Directional Distortional Hardening in Metal Plasticity within Thermodynamics

Heidi P. Feigenbaum¹ and Yannis F. Dafalias²

**Abstract:** Directional distortion, observed in many experiments on various types of metals, refers to the formation of a region of high curvature (sharpening) on the yield surface approximately in the direction of loading, and a region of low curvature (flattening) approximately in the opposite direction. Constitutive modeling of directional distortion was recently presented by the writers where an evolving fourth-order tensor-valued internal variable was introduced. In the current paper a much simpler mathematical formulation describing directional distortional hardening is presented without the use of a fourth-order tensor, in conjunction with kinematic and isotropic hardening. Two versions of the model in ascending level of complexity follow similar lines of development, which include derivation of all hardening rules on the basis of conditions sufficient to satisfy the thermodynamic dissipation inequality. As a tradeoff for its simplicity the present model does not fit experimental data as well as the model with the evolving fourth-order tensor, but it still captures the salient features of directional distortion in a rather satisfactory way.

**DOI:** 10.1061/(ASCE)0733-9399(2008)134:9(730)

**CE Database subject headings:** Plasticity; Elastoplasticity; Yield; Thermal factors; Anisotropy.

## Introduction

In the field of continuum mechanics it has long been recognized that plastic deformations may induce anisotropy in materials that are initially isotropic. For metals such anisotropy is due to the development of internal stresses and texture formation because of preferred orientations of grains in a polycrystal, among other reasons. The macroscopic manifestation of metal anisotropy takes the form of translation and shape distortion of the yield surface in stress space, modeled by kinematic and distortional hardening, respectively.

In particular “directional distortion” is a distortion of the shape of the yield surface such that a region of high curvature (sharpening) develops roughly in the direction of loading while a region of lower curvature (flattening) develops in the opposite direction (see Fig. 1). This observation has been seen in numerous experiments on various types of metals including, but not limited to, those by Phillips et al. (1975), Naghdi et al. (1958), McComb (1960), Wu and Yeh (1991), and Boucher et al. (1995). In general, directional distortion of the yield surface is observed when a relatively sensitive definition of yield is used. For example, Phillips et al. (1975), Wu and Yeh (1991), and Boucher et al. (1995) define yield by offset strains of $3×10^{-6}$, $5×10^{-6}$, and $4×10^{-5}$ as definitions of yield, respectively.

The modeling of directional distortion has been addressed at various degrees of success by Voyiadjis and Foroozesh (1990), Ortiz and Popov (1983), François (2001), Kurtyka and Zyczkowski (1996), and Wei-Ching Yeh and Pan (1996), among others. The model by François is the only one to include directional distortion within the context of thermodynamics, however, the format of the yield function for that model is fundamentally different than the one proposed in this paper.

The present paper introduces a constitutive theory for metal plasticity that includes the development of anisotropy through kinematic and directional distortional hardening, supplemented by the classical isotropic hardening. The proposed hardening rules arise from sufficient conditions to satisfy the laws of thermodynamics, so that energy transfer during plastic work may be tracked; in addition they guarantee saturation levels of anisotropy. The derivation distinguishes between energy dissipated and energy stored or released as part of the recoverable plastic free energy (not the elastic part). This derivation will give rise to evanescent-memory type hardening rules, which allows for saturation of developing anisotropy. These issues were also recently addressed by Feigenbaum and Dafalias (2007), albeit with a formulation which was more complex and included a fourth-order tensor-valued evolving internal variable. The present model formulation is simpler and makes no use of a fourth-order tensor, thus, as a tradeoff for its simplicity it does not fit experimental data as well as the aforementioned work, in particular the flattening of the yield surface, but it still captures the salient features of directional distortion in a rather satisfactory way.

Once the basic theory is presented, several examples in comparison with available experimental data of distorted yield surfaces will show some of the practical capabilities of the model, as well as some of its weaknesses. Two different versions of the model within the same basic structure of the theory will be presented and compared. A comparison of the present model simulations of yield surface shapes with the ones obtained by the

¹Assistant Professor, Dept. of Mechanical Engineering, Northern Arizona Univ., P.O. Box 15600, Flagstaff, AZ 86011 (corresponding author). E-mail: hf38@nau.edu

²Professor, Dept. of Civil and Environmental Engineering, Univ. of California, Davis CA 95616; Dept. of Mechanics, Faculty of Applied Mathematical and Physical Science, National Technical Univ. of Athens, Zographou, 15780 Hellas.

Note. Associate Editor: George Z. Voyiadjis. Discussion open until February 1, 2009. Separate discussions must be submitted for individual papers. The manuscript for this paper was submitted for review and possible publication on November 15, 2007; approved on February 14, 2008. This paper is part of the *Journal of Engineering Mechanics*, Vol. 134, No. 9, September 1, 2008. ©ASCE, ISSN 0733-9399/2008/9-730-738/$25.00.

![](./images/811905190222364672_1.jpg)

Fig. 1. Example of directional distortion of yield surface for loading in pure tension. Note two subsequent yield surfaces have the same final stress point in tension, but translation of center of directionally distorted yield surface is less than that with kinematic hardening.

aforementioned more complete, and also more complex, recently proposed model by Feigenbaum and Dafalias (2007) will be discussed.

In terms of notation, henceforth all second-order tensors will be denoted by bold face in direct notation, e.g., $\boldsymbol{m}$. No bold face symbols will be used when indexed components of tensors are used. The proposed constitutive model is confined to small deformations. The stress tensor is denoted by $\boldsymbol{\sigma}$ and the linearized strain tensor is denoted by $\boldsymbol{\varepsilon}$. As usual the strain tensor is decomposed additively into elastic and plastic parts, $\boldsymbol{\varepsilon}=\boldsymbol{\varepsilon}^{e}+\boldsymbol{\varepsilon}^{p}$, and the elastic constitutive law will be assumed linear and isotropic.

## Model with Direction of Distortion Based on Backstress Tensor ($\boldsymbol{\alpha}$-Model)

The proposed yield function takes the form
$$
f=\frac{3}{2}\left[1-\left(\boldsymbol{n}_{r}: \boldsymbol{\alpha}\right) c\right](s-\boldsymbol{\alpha}):(s-\boldsymbol{\alpha})-k^{2}=0
\tag{1}
$$
where $c$ is a scalar-valued internal variable; $s$ is the deviatoric part of the stress tensor; $\boldsymbol{\alpha}$ is the deviatoric backstress tensor; $k$ represents the size of the yield surface; and $\boldsymbol{n}_{r}$ is a unit traceless radial tensor ( $\operatorname{tr} \boldsymbol{n}_{r}=0, \boldsymbol{n}_{r}: \boldsymbol{n}_{r}=1$ ) given by
$$
\boldsymbol{n}_{r}=\frac{s-\boldsymbol{\alpha}}{|s-\boldsymbol{\alpha}|}
\tag{2}
$$

The above yield surface will begin as the von Mises hypersphere, since $\boldsymbol{\alpha}$ and $c$ are initially zero. As plastic loading occurs the yield surface will change size, location, and shape as $k, \boldsymbol{\alpha}$, and $c$ evolve. The trace-type scalar multiplier, $\boldsymbol{n}_{r}: \boldsymbol{\alpha}$, is responsible for the directional distortion. This can be intuitively understood if one observes that the trace $\boldsymbol{n}_{r}: \boldsymbol{\alpha}$ is an inner product between the tensors $\boldsymbol{n}_{r}$ and $\boldsymbol{\alpha}$, thus, it measures the projection of $\boldsymbol{\alpha}$ along the different unit directions $\boldsymbol{n}_{r}$, which can vary from $|\boldsymbol{\alpha}|$ to $-|\boldsymbol{\alpha}|$ passing through zero. Such variation affects the value of the "radius" $s-\boldsymbol{\alpha}$ associated with a specific direction $\boldsymbol{n}_{r}$ because $k$ is the same for any direction, therefore, inducing a corresponding directional shape distortion. Thus, the direction of distortion is determined only by the stress and the backstress $\boldsymbol{\alpha}$, and consequently the model in Eq. (1) will henceforth be referred to as the $\boldsymbol{\alpha}$ model. This formulation has been chosen because experimental evidence suggests that the region of high curvature develops roughly along the direction of the backstress. An illustration of the above distortion mechanism achieved by the introduction of the term $1-\left(\boldsymbol{n}_{r}: \boldsymbol{\alpha}\right) c$ is shown in Fig. 1. In this figure $\sigma$ is normal stress and $\tau$ is shear stress both of which are normalized by the initial yield stress, $\sigma_{y}$, the loading is pure tension, and the current stress point is $s$. If at any time $\boldsymbol{\alpha}$ returns to zero, then the von Mises yield surface is recovered. Note that $\boldsymbol{n}_{r}$ will never be zero as long as the yield surface has some size, i.e., there is some elastic region, and $\boldsymbol{\alpha}: \boldsymbol{n}_{r}$ will only be zero at two discrete stress points in two dimension (2D), or a curve in 3D, etc. Also the necessary positiveness of the $1-\left(\boldsymbol{n}_{r}: \boldsymbol{\alpha}\right) c$ term will be examined in detail later.

For simplicity, only rate-independent plasticity will be considered. In addition, as is typical with metal plasticity, the associative flow rule will be used
$$
\dot{\boldsymbol{\varepsilon}}^{p}=\lambda \frac{\partial f}{\partial \boldsymbol{\sigma}}=\lambda\left|\frac{\partial f}{\partial \boldsymbol{\sigma}}\right| \boldsymbol{n}
\tag{3}
$$
where $\dot{\boldsymbol{\varepsilon}}^{p}=$ rate of plastic strain; $\lambda=$ loading index (alias plastic multiplier); and $\boldsymbol{n}=$ unit traceless tensor ( $\operatorname{tr} \boldsymbol{n}=0, \boldsymbol{n}: \boldsymbol{n}=1$ ) which is "normal" to the yield surface. Clearly $\boldsymbol{n} \neq \boldsymbol{n}_{r}$, in general. Based on the analytical expression of the yield surface given by Eq. (1), the following expression is obtained for the gradient $\partial f / \partial \boldsymbol{\sigma}$ :
$$
\frac{\partial f}{\partial \boldsymbol{\sigma}}=\frac{3}{2}|s-\boldsymbol{\alpha}|\left\{\left[2-\left(\boldsymbol{n}_{r}: \boldsymbol{\alpha}\right) c\right] \boldsymbol{n}_{r}-c \boldsymbol{\alpha}\right\}
\tag{4}
$$

When the associative flow rule is used, as is the case here, it is important to have the shape of the yield surface modeled accurately because small deviations in shape may result in large deviations in the normal to the yield surface (i.e., $\partial f / \partial \boldsymbol{\sigma}$ ) and thus the plastic strain rate direction.

The model now needs evolution laws for $k, \boldsymbol{\alpha}$, and $c$. Following the procedure outlined by Dafalias et al. (2002) and Feigenbaum and Dafalias (2007) the hardening rules arise strictly on the basis of sufficient conditions for satisfaction of the second law of thermodynamics, in conjunction with a few simple and plausible assumptions about energy storage and release in the material.

It is assumed that free energy, $\psi$, decomposes into elastic and plastic parts as follows:
$$
\psi=\psi_{e}+\psi_{p}.
\tag{5}
$$

With this relation and assuming isothermal processes, the second law of thermodynamics directly leads to the dissipation inequality by standard methods, which states that the net energy dissipated due to the difference of the plastic work rate and the rate of the plastic part of the free energy must be nonnegative, i.e.
$$
\boldsymbol{\sigma}: \dot{\boldsymbol{\varepsilon}}^{p}-\rho \dot{\psi}_{p} \geq 0,
\tag{6}
$$
where $\dot{\psi}_{p}=$ rate of the plastic free energy, and $\rho$ is density. Adding and subtracting $\boldsymbol{\alpha}: \dot{\boldsymbol{\varepsilon}}^{p}$ and noting that $\boldsymbol{\sigma}: \dot{\boldsymbol{\varepsilon}}^{p}=s: \dot{\boldsymbol{\varepsilon}}^{p}$ results in
$$
(s-\boldsymbol{\alpha}): \dot{\boldsymbol{\varepsilon}}^{p}+\boldsymbol{\alpha}: \dot{\boldsymbol{\varepsilon}}^{p}-\rho \dot{\psi}_{p} \geq 0.
\tag{7}
$$

Substituting into the first term of Eq. (7) the flow rule expression Eq. (3) one obtains
JOURNAL OF ENGINEERING MECHANICS © ASCE / SEPTEMBER 2008 / 731
J. Eng. Mech. 2008.134:730-738.

$$3 \lambda|s-\boldsymbol{\alpha}|^{2}\left[1-\left(\boldsymbol{n}_{r}: \boldsymbol{\alpha}\right) c\right]+\boldsymbol{\alpha}: \dot{\boldsymbol{\varepsilon}}^{p}-\rho \dot{\psi}_{p} \geq 0\qquad(8)$$

Because of Eq. (1) the foregoing expression Eq. (8) can be rewritten as
$$2 k^{2} \lambda+\boldsymbol{\alpha}: \dot{\boldsymbol{\varepsilon}}^{p}-\rho \dot{\psi}_{p} \geq 0\qquad(9)$$

Now an explicit expression for $\psi_{p}$ is needed. This requires assumptions about energy storage in the material. The plastic free energy, $\psi_{p}$, will be additively decomposed into parts associated with isotropic, kinematic, and distortional hardening. The following decomposition of $\psi_{p}$ is proposed:
$$\psi_{p}=\psi_{p}^{\text {iso }}+\psi_{p}^{\text {ani }} ; \quad \psi_{p}^{\text {ani }}=\psi_{p}^{\text {kin }}-\psi_{p}^{\text {dis }}\qquad(10)$$
where $\psi_{p}^{iso }, \psi_{p}^{ani }, \psi_{p}^{kin }$ , and $\psi_{p}^{dis }$ are isotropic, anisotropic, kinematic, and distortional parts of the plastic free energy. Observe that the anisotropic part is assumed to decompose into kinematic and distortional parts, along the corresponding hardening assumptions.

A very important point must now be discussed. The subtraction, instead of addition, of $\psi_{p}^{dis }$ from $\psi_{p}^{kin }$ in order to obtain the overall anisotropic part $\psi_{p}^{ani }$ of the plastic free energy, was motivated by the need to fit experimental data in conjunction with plausible expectations for a limit on the level of anisotropy development. Within the present model formulation this subtraction was found necessary in order to satisfy two important requirements. First, the directionality of the distortion must correspond to experimental findings, namely the region of high curvature must be approximately in the direction of loading and the region of flattening on the opposite side. Second, the distortional variable $c$ must reach a finite limit, in other words the c cannot evolve forever and its value is expected to reach a saturation level. The details of how these two requirements are connected to the evolution law for the $c$ in conjunction with the necessity to subtract rather than add the $\psi_{p}^{dis }$ in Eq. (10) will be presented when such evolution law for $c$ is formulated.

At present an attempt will be made to physically justify the energetic message implied by the foregoing subtraction of the distortional part from the kinematic part of the plastic free energy in Eq. (10). Energetically, the subtraction of $\psi_{p}^{dis }$ may be understood to imply that the material releases energy while distortion of the yield surface occurs, in contrast to $\psi_{p}^{kin }$ and $\psi_{p}^{iso }$ which store energy as the yield surface changes location and size, respectively. This energy release can possibly be explained as follows. During plastic deformation it is known that the material crystal grains rearrange themselves into preferred orientations, which is the underlying main microscopic mechanism for the macroscopic manifestation of yield surface distortion. Such readjustment of the grain aggregates results into releasing developed intergranular stresses, which results in a lower energy state and reduction of the plastic free energy; hence, the subtraction of the distortional part in Eq. (10). To the contrary, the isotropic and kinematic hardening mechanisms store energy by the increase of dislocation and residual intergranular stress densities during plastic deformation, hence, their contribution to the increase of the plastic free energy. The specific format of Eq.(10) was chosen to suggest that the energy released in the distortion process is taken away from energy that would otherwise be stored during the backstress (intergranular stress) development. This correlates well with the geometrical observation in stress space that when directional distortion occurs, in order to be on the same stress point the "center" of the yield surface moves a shorter distance in stress space (smaller magnitude of backstress) than what it would have moved had directional distortion not taken place, as it can be seen in the graphs of Fig. 1. It must be noted that in general the kinematic hardening is associated with both intergranular stress development and grain orientation, but mainly with the former. Thus, the foregoing suggestion of associating kinematic hardening only with intergranular stress is a simplification that must be viewed with prudence for a more in depth microscopic analysis.

Next, specific expressions for $\psi_{p}^{iso }, \psi_{p}^{kin }$ , and $\psi_{p}^{dis }$ need to be assumed. Following Dafalias et al. (2002), we assume the existence of thermodynamic conjugates to each of the internal variables and furthermore, that each part of the plastic free energy is only a function of these conjugates, i.e., $\psi_{p}^{iso }=\hat{\psi}_{p}^{iso }(k_{c})$ , $\psi_{p}^{kin }=\hat{\psi}_{p}^{kin }(\alpha_{c})$ , and $\psi_{p}^{dis }=\hat{\psi}_{p}^{dis }(c_{c})$ , where $k_{c}, \alpha_{c}$ , and $c_{c}$ are thermodynamic conjugates to $k, \alpha$ , and $c$ , respectively. For $\psi_{p}^{iso }$ , $\psi_{p}^{kin }$ , and $\psi_{p}^{dis }$ the following is assumed:
$$\psi_{p}^{\text {iso }}=\frac{\kappa_{1}}{2 \rho} k_{c}^{2} ; \quad \psi_{p}^{\text {kin }}=\frac{a_{1}}{2 \rho} \boldsymbol{\alpha}_{c}: \boldsymbol{\alpha}_{c} ; \quad \psi_{p}^{\text {dis }}=\frac{c_{1}}{2 \rho} c_{c}^{2}\qquad(11)$$
where $\kappa_{1}, a_{1}$ , and $c_{1}$ are nonnegative material constants. Based on the definition of a thermodynamic conjugate and the above functions, $k, \alpha$ , and $c$ are given by
$$k=\rho \frac{\partial \psi_{p}^{\text {iso }}}{\partial k_{c}}=\kappa_{1} k_{c} ; \quad \boldsymbol{\alpha}=\rho \frac{\partial \psi_{p}^{\text {kin }}}{\partial \boldsymbol{\alpha}_{c}}=a_{1} \boldsymbol{\alpha}_{c} ; \quad c=\rho \frac{\partial \psi_{p}^{\text {dis }}}{\partial c_{c}}=c_{1} c_{c} \quad(12)$$

After writing Eq. (10) in terms of Eqs. (11) one can take the rate of the resulting expression for $\psi_{p}$ using the chain rule and the Eqs. (12) in the process, and substitute this rate into the dissipation inequality Eq. (8) to obtain
$$\begin{aligned}
& \lambda\left\{\frac{3}{2}|s-\boldsymbol{\alpha}|^{2}\left[1-\left(\boldsymbol{n}_{r}: \boldsymbol{\alpha}\right) c\right]+k^{2}\right\}+\boldsymbol{\alpha}: \dot{\boldsymbol{\varepsilon}}^{p}-\frac{1}{\kappa_{1}} k \dot{k}-\frac{1}{a_{1}} \boldsymbol{\alpha}: \dot{\boldsymbol{\alpha}}+\frac{1}{c_{1}} c \dot{c} \\
& \quad \geq 0
\end{aligned}\qquad(13)$$

Notice that the term added to $k^{2}$ inside the braces also equals $k^{2}$  according to Eq. (1) [i.e, the first term of Eq. (13) equals $\lambda 2 k^{2}$ ], but it was purposefully kept as is in order to derive appropriate evolution equations for both $k$ and $c$ .

Sufficient conditions are needed to ensure the satisfaction of inequality (13). Again drawing upon what was done in Dafalias et al. (2002) and Feigenbaum and Dafalias (2007), it certainly would be sufficient to split the inequality into three parts, associated with $k, \alpha$ , and $c$ , correspondingly, and require satisfaction of each partindependently, as follows:
$$\lambda k^{2}-\frac{1}{\kappa_{1}} k \dot{k} \geq 0\qquad(14)$$

$$\boldsymbol{\alpha}: \dot{\boldsymbol{\varepsilon}}^{p}-\frac{1}{a_{1}} \boldsymbol{\alpha}: \dot{\boldsymbol{\alpha}} \geq 0\qquad(15)$$

$$\frac{3}{2} \lambda|s-\boldsymbol{\alpha}|^{2}\left[1-\left(\boldsymbol{n}_{r}: \boldsymbol{\alpha}\right) c\right]+\frac{1}{c_{1}} c \dot{c} \geq 0.\qquad(16)$$

One may interpret the above inequalities as requiring a positive dissipation for each one of three independent mechanisms associated with $k, \alpha$ , and $c$ , although the copresence of $\alpha$ and $c$ in the third inequality of Eq.(16) shows that there is still a degree of coupling between them. This coupling will be eliminated in the next section. The following equations and the ensuing expressions for the rates of $k$ and $\alpha$ are sufficient conditions to ensure thesatisfaction of inequalities (14) and (15)

732 / JOURNAL OF ENGINEERING MECHANICS © ASCE / SEPTEMBER 2008
J. Eng. Mech. 2008.134:730-738.

$$
\lambda k-\frac{1}{\kappa_{1}} \dot{k}=\lambda \kappa_{2} k^{2} \Rightarrow \dot{k}=\lambda \kappa_{1} k\left(1-\kappa_{2} k\right) \tag{17}
$$

$$
\dot{\boldsymbol{\varepsilon}}^{p}-\frac{1}{a_{1}} \dot{\boldsymbol{\alpha}}=\lambda\left|\frac{\partial f}{\partial \boldsymbol{\sigma}}\right| a_{2} \boldsymbol{\alpha} \Rightarrow \dot{\boldsymbol{\alpha}}=\lambda\left|\frac{\partial f}{\partial \boldsymbol{\sigma}}\right| a_{1}\left(\boldsymbol{n}-a_{2} \boldsymbol{\alpha}\right) \tag{18}
$$

where $\kappa_{2}$ and $a_{2}$ are again nonnegative material constants and the flow rule, Eq. (3), was used for $\dot{\boldsymbol{\varepsilon}}^{p}$. The evolution laws for both $k$ and $\boldsymbol{\alpha}$ are of the evanescent memory type. Observe that in regards to model constants one has achieved the maximum possible simplicity for nonlinear variations, i.e., two constants for each one of the two internal variables $k$ and $\boldsymbol{\alpha}$. In essence the second constant (with subscript 2) is associated with the limit of the variable and the first constant (with subscript 1) is related to the pace at which this limit is approached. This simplicity is an important feature if the model is to be proved useful.

In order to achieve a similar evanescent memory type hardening rule (evolution rate equation) for $c$ as well as searching for a simple condition which guarantees that Eq. (16) is always satisfied, the following relation is proposed:

$$
-\frac{3}{2} \lambda|\boldsymbol{s}-\boldsymbol{\alpha}|^{2}\left(\boldsymbol{n}_{r}: \boldsymbol{\alpha}\right) c+\frac{1}{c_{1}} c \dot{c}=-\frac{3}{2} \lambda|\boldsymbol{s}-\boldsymbol{\alpha}|^{2} c_{2} c^{2} \Rightarrow
$$

$$
\dot{c}=\frac{3}{2} \lambda c_{1}|\boldsymbol{s}-\boldsymbol{\alpha}|^{2}\left[\left(\boldsymbol{n}_{r}: \boldsymbol{\alpha}\right)-c_{2} c\right] \tag{19}
$$

where $c_{2}=$ nonnegative material constant. In order for Eq. (19) to satisfy Eq. (16) it is straightforward to show that the condition

$$
c_{2} c^{2} \leq 1, \quad \forall c. \tag{20}
$$

must be necessarily satisfied during any process. Note that although inequality (20) necessarily follows, the fact that the relation Eq. (19) was a sufficient but not necessary proposition, renders inequality (20) only a sufficient condition for the satisfaction of the key inequality (16) in conjunction with Eq. (19). One may observe that inequality (20) requires continuous monitoring in the process of plastic deformation during which the quantity $c$ evolves according to Eq. (19) in order to ensure satisfaction of thermodynamics, a rather inconvenient aspect of modeling. However, in a later section it will be shown that a simple constraint on the values of constants involved in Eqs. (18) and (19) will suffice to guarantee the satisfaction of Eq. (20).

Comparison of Eqs. (17) and (19), both for scalar-valued quantities, reveals an important difference. The evolution law for $k$, Eq. (17), is a typical evolution law for a scalar internal variable, and as such it does not take into account the direction of loading. Therefore, once $k$ has reached its saturation value, it will remain at that value for all additional loading or unloading. On the other hand, the evolution law for $c$, Eq. (19), is a truly novel element of the present development because it is an evolution law for a scalar internal variable which reverses sign upon reversal of loading direction via the term $\boldsymbol{n}_{r}: \boldsymbol{\alpha}$ since the $\boldsymbol{n}_{r}$ changes sign. Stated in a more general way and not just for loading reversals, Eq. (19) accounts for the direction of loading via the term $\boldsymbol{n}_{r}: \boldsymbol{\alpha}$. Thus even if $c$ has reached its saturation value, upon change of loading direction $c$ will unsaturate before beginning to evolve again. Clearly the evolution law for $c$ expressed by Eq. (19) follows an Armstrong-Frederick evanescent memory type hardening rule, and therefore $c$ will approach a finite limit in monotonic loading.

Note also that if the distortional free energy $\psi_{p}^{\text {dis }}$ in Eq. (10) was added rather than subtracted, the hardening rule for $c$ would be the same as in Eq. (19) except all the signs would be reversed. Thus the first term in the brackets would be negative $(-\boldsymbol{n}_{r}: \boldsymbol{\alpha})$ and the second term would be positive $(+c_{2} c)$. The first term being negative implies that $c$ evolves in the direction $-\boldsymbol{n}_{r}: \boldsymbol{\alpha}$ for straight-ahead loading before any reversal. In stress space, this would imply geometrically that the region of high curvature and the region of flattening are opposite to what is observed experimentally. The second term of Eq. (19) being positive means that $c$ would continuously evolve without a limit. These two facts motivated the idea of distortional hardening being associated with release rather than storage of free plastic energy, hence the subtraction rather than addition of $\psi_{p}^{\text {dis }}$ in Eq. (10).

Finally to complete the constitutive description one needs to specify the loading index $\lambda$ which enters the flow rule given by Eq. (3) and the hardening (rate) rules given by Eqs. (17)-(19). This is accomplished by imposing the necessary consistency condition $\dot{f}=0$ which yields $\lambda$ as

$$
\lambda=\left\langle\frac{1}{K_{p}} \frac{\partial f}{\partial \boldsymbol{\sigma}}: \dot{\boldsymbol{\sigma}}\right\rangle \tag{21}
$$

with plastic modulus $K_{p}$ given by

$$
\begin{gathered}
K_{p}=2 \kappa_{1} k^{2}\left(1-\kappa_{2} k\right)+a_{1}\left|\frac{\partial f}{\partial \boldsymbol{\sigma}}\right|\left(\frac{\partial f}{\partial \boldsymbol{\sigma}}+\frac{3}{2} c|\boldsymbol{s}-\boldsymbol{\alpha}|^{2} \boldsymbol{n}_{r}\right): \\
\left(\boldsymbol{n}-a_{2} \boldsymbol{\alpha}\right)+\frac{9}{4} c_{1}|\boldsymbol{s}-\boldsymbol{\alpha}|^{4}\left(\boldsymbol{n}_{r}: \boldsymbol{\alpha}\right)\left[\left(\boldsymbol{n}_{r}: \boldsymbol{\alpha}\right)-c_{2} c\right] \tag{22}
\end{gathered}
$$

where the expression for $\partial f / \partial \boldsymbol{\sigma}$ is given by Eq. (4).

## Model with Direction of Distortion Based on Directional Tensor (r Model)

One criticism one might raise for the present model is that distor- tional hardening is coupled with kinematic hardening, while the underlying physics would imply an uncoupled consideration. To alleviate this problem the following alternative formulation of the yield function is suggested:

$$
f=\frac{3}{2}\left[1-\left(\boldsymbol{n}_{r}: \boldsymbol{r}\right)\right](\boldsymbol{s}-\boldsymbol{\alpha}):(\boldsymbol{s}-\boldsymbol{\alpha})-k^{2}=0 \tag{23}
$$

where $\boldsymbol{r}$ is a second-order tensor-valued directional distortional hardening internal variable. Notice that Eq. (23) has the same format as Eq. (1) with $\boldsymbol{r}$ instead of $\boldsymbol{\alpha}$, but notice that $\boldsymbol{r}$ is dimensionless. By introducing $\boldsymbol{r}$ in Eq. (23) the scalar quantity $\boldsymbol{n}_{r}: \boldsymbol{r}$ is completely responsible for directional distortion, therefore, kine- matic hardening has been decoupled from distortional hardening. This allows greater flexibility in modeling by allowing the mod- eler to separately control the distortion and translation of the yield surface. The model in Eq. (23) will henceforth be referred to as the $\boldsymbol{r}$ model [as opposed to the $\boldsymbol{\alpha}$ model in Eq. (1)].

The question now arises of how to formulate the evolution law for $\boldsymbol{r}$. Following the same procedure used in the previous section, all hardening rules for this alternative formulation will arise from sufficient conditions to satisfy the laws of thermodynamics. The form of the dissipation inequality in Eq. (7) will be the starting point. Notice that $\dot{\boldsymbol{\varepsilon}}^{p}$ appears in this inequality. As in the $\boldsymbol{\alpha}$ model, the $\boldsymbol{r}$ model will use the associative flow rule, Eq. (3), with $\partial f / \partial \boldsymbol{\sigma}$ given by

$$
\frac{\partial f}{\partial \boldsymbol{\sigma}}=\frac{3}{2}|\boldsymbol{s}-\boldsymbol{\alpha}|\left\{\left[2-\left(\boldsymbol{n}_{r}: \boldsymbol{r}\right)\right] \boldsymbol{n}_{r}-\boldsymbol{r}\right\}
\tag{24}
$$

Substituting this into the dissipation inequality (7) yields
$$
\lambda\left\{k^{2}+\frac{3}{2}|\boldsymbol{s}-\boldsymbol{\alpha}|^{2}\left[1-\left(\boldsymbol{n}_{r}: \boldsymbol{r}\right)\right]\right\}+\boldsymbol{\alpha}: \dot{\boldsymbol{\varepsilon}}^{p}-\rho \dot{\psi}_{p} \geq 0
\tag{25}
$$

Notice that the term added to $k^{2}$ inside the \{\} , also equals $k^{2}$ according to Eq. (23), i.e., the first term of Eq. (25) equals $\lambda 2 k^{2}$, but it was purposefully kept separated in two parts in order to derive evolution equations for both $k$ and $\boldsymbol{r}$.

Now, assumptions about energy storage in the material during the plastic deformation process will be required in order to have an explicit expression for $\psi_{p}$. It is assumed that $\psi_{p}$ can be additionally decomposed into parts that correspond to the isotropic, kinematic, and distortional hardening mechanisms. The form for the decomposition will be the same as that in the last section, i.e., $\psi_{p}$ is given by Eq. (10). So again $\psi_{p}^{\text {dis }}$ is subtracted from $\psi_{p}^{\text {kin }}$ in order to obtain the overall anisotropic part $\psi_{p}^{\text {ani }}$ of the plastic free energy, dictated again by the need to fit experimental data in conjunction with plausible expectations for the level of anisotropy development. A physical justification of this subtraction was presented in the last section in the discussion following Eq. (10).

Next, specific expressions for $\psi_{p}^{\text {iso }}, \psi_{p}^{\text {kin }}$, and $\psi_{p}^{\text {dis }}$ need to be assumed. Following the procedure in the previous section, we assume the existence of thermodynamic conjugates to each of the internal variables and that each part of the plastic free energy is only a function of these conjugates, i.e., $\psi_{p}^{\text {iso }}=\hat{\psi}_{p}^{\text {iso }}\left(k_{c}\right)$, $\psi_{p}^{\text {kin }}=\hat{\psi}_{p}^{\text {kin }}\left(\boldsymbol{\alpha}_{c}\right)$, and $\psi_{p}^{\text {dis }}=\hat{\psi}_{p}^{\text {dis }}\left(\boldsymbol{r}_{c}\right)$, where $k_{c}, \boldsymbol{\alpha}_{c}$, and $\boldsymbol{r}_{c}$ are the thermodynamic conjugates to $k, \boldsymbol{\alpha}$, and $\boldsymbol{r}$, respectively. The same simple isotropic functions as in Eqs. $(11)_{1}$ and $(11)_{2}$ are assumed for $\psi_{p}^{\text {iso }}$ and $\psi_{p}^{\text {kin }}$, while the following expression is assumed for $\psi_{p}^{\text {dis }}$ in lieu of Eq. $(11)_{3}$ :
$$
\psi_{p}^{\mathrm{dis}}=\frac{\rho_{1}}{2 \rho} \boldsymbol{r}_{c}: \boldsymbol{r}_{c}
\tag{26}
$$
where $\rho_{1}=$ nonnegative material constants. Based on the definition of a thermodynamic conjugate and Eq. (26), $\boldsymbol{r}$ is given by the following:
$$
\boldsymbol{r}=\rho \frac{\partial \psi_{p}^{\mathrm{dis}}}{\partial \boldsymbol{r}_{c}}=\rho_{1} \boldsymbol{r}_{c}
\tag{27}
$$

Finally writing Eq. (10) in terms of Eqs. (11) and (26), one can take the rate of the resulting expression for $\psi_{p}$ using the chain rule and Eqs. (12) and (27) in the process, and substitute this rate into the dissipation inequality to obtain
$$
\lambda\left\{k^{2}+\frac{3}{2}|\boldsymbol{s}-\boldsymbol{\alpha}|^{2}\left[1-\left(\boldsymbol{n}_{r}: \boldsymbol{r}\right)\right]\right\}+\boldsymbol{\alpha}: \dot{\boldsymbol{\varepsilon}}^{p}-\rho \dot{\psi}_{p} \geq 0
\tag{28}
$$

As in the previous section, it will be sufficient to split inequality (28) into three parts: one associated with $k$, one associated with $\boldsymbol{\alpha}$, and now one associated with $\boldsymbol{r}$, and require satisfaction of each part independently. The parts associated with $k$ and $\boldsymbol{\alpha}$ are given in inequalities (14) and (15), respectively, and the part associated with $\boldsymbol{r}$ is
$$
\frac{3}{2} \lambda|\boldsymbol{s}-\boldsymbol{\alpha}|^{2}\left[1-\left(\boldsymbol{n}_{r}: \boldsymbol{r}\right)\right]+\frac{1}{\rho_{1}} \boldsymbol{r}: \dot{\boldsymbol{r}} \geq 0
\tag{29}
$$

Sufficient conditions to satisfy inequalities (14) and (15) are given in Eqs. (17) and (18), respectively, and thus the evolution laws for $k$ and $\boldsymbol{\alpha}$ are the same as in the last section. The sufficient conditions to satisfy inequality (29) is
$$
\begin{gathered}
-\frac{3}{2} \lambda|\boldsymbol{s}-\boldsymbol{\alpha}|^{2}\left(\boldsymbol{n}_{r}: \boldsymbol{r}\right)+\frac{1}{\rho_{1}} \boldsymbol{r}: \dot{\boldsymbol{r}}=-\frac{3}{2} \lambda|\boldsymbol{s}-\boldsymbol{\alpha}|^{2} \rho_{2} \boldsymbol{r}: \boldsymbol{r} \Rightarrow \\
\dot{\boldsymbol{r}}=\frac{3}{2} \lambda \rho_{1}|\boldsymbol{s}-\boldsymbol{\alpha}|^{2}\left(\boldsymbol{n}_{r}-\rho_{2} \boldsymbol{r}\right)
\end{gathered}
\tag{30}
$$
where $\rho_{2}=$ nonnegative constant. In order for inequality (29) to be satisfied by Eq. (30) the following condition is necessary:
$$
\rho_{2}(\boldsymbol{r}: \boldsymbol{r}) \leq 1, \quad \forall \boldsymbol{r}
\tag{31}
$$

Comparison of Eq. (18) with Eq. (30) shows that the hardening rules of the two second-order tensors, $\boldsymbol{\alpha}$ and $\boldsymbol{r}$, have the same format, but $\boldsymbol{\alpha}$ evolves in the direction of $\boldsymbol{n}$ while $\boldsymbol{r}$ evolves in the direction of $\boldsymbol{n}_{r}$, which in general are not the same as can be seen at the point $s^{\prime}$ in Fig. 1. The hardening rule for $\boldsymbol{r}$ is also of the evanescent memory type and therefore uses the minimum number of two constants for a nonlinear hardening rule and approaches a finite limit. Given the evolution of $\boldsymbol{r}$ one must monitor the satisfaction of inequality (31); however, it will be shown in the section for limits that a rather simple condition on the constant $\rho_{2}$ will suffice to satisfy Eq. (31) for any value of $\boldsymbol{r}$.

Finally to complete the constitutive description one needs to specify the loading index $\lambda$ which enters the flow rule given by Eq. (3) and the hardening (rate) rules given by Eqs. (17), (18), and (30). This is accomplished by imposing the necessary consistency condition $\dot{f}=0$ which yields $\lambda$ as given in Eq. (21) with plastic modulus $K_{p}$ given by
$$
\begin{aligned}
K_{p}= & 2 \kappa_{1} k^{2}\left(1-\kappa_{2} k\right)+a_{1}\left|\frac{\partial f}{\partial \boldsymbol{\sigma}}\right|^{2}\left(1-a_{2} \boldsymbol{\alpha}: \boldsymbol{n}\right) \\
& +\frac{9}{4} \rho_{1}|\boldsymbol{s}-\boldsymbol{\alpha}|^{4}\left(1-\rho_{2} \boldsymbol{r}: \boldsymbol{n}_{r}\right)
\end{aligned}
\tag{32}
$$
where the expression for $\partial f / \partial \boldsymbol{\sigma}$ is given by Eq. (24).

## Limits, Positiveness, and Convexity

In this section the limiting values attained by the internal variables are addressed, based on which constraints on the model constants are obtained in order to satisfy the thermodynamic requirements and the positiveness of the yield surface expression. In addition the convexity of the distorted yield surface is discussed.

### Limits

Since the hardening rules for all internal variables of both models are of the evanescent memory type, the variables reach finite limits. These limits can be found by setting the rate equations equal to zero. By setting the rate Eqs. (17) and (18) equal to zero, one obtains the following:
$$
k^{l}=\frac{1}{\kappa_{2}}
\tag{33}
$$
$$
\boldsymbol{\alpha}^{l}=\frac{1}{a_{2}} \boldsymbol{n}^{l}
\tag{34}
$$
where $k^{l}$ and $\boldsymbol{\alpha}^{l}$ are the limits of $k$ and $\boldsymbol{\alpha}$, respectively, and $\boldsymbol{n}^{l}$ represents the normal to the limit stress point under a given load path.

734 / JOURNAL OF ENGINEERING MECHANICS © ASCE / SEPTEMBER 2008
J. Eng. Mech. 2008.134:730-738.

Addressing first the $\boldsymbol{\alpha}$ model, setting the rate Eq. (19) equal to zero one finds that the limit of $c$ is given by

$$
c^{l}=\frac{\boldsymbol{n}_{r}^{l}: \boldsymbol{\alpha}^{l}}{c_{2}}=\frac{\boldsymbol{n}_{r}^{l}: \boldsymbol{n}^{l}}{a_{2} c_{2}} \tag{35}
$$

Clearly $c$ cannot reach its limit until $\boldsymbol{\alpha}$ has reached its own. The question is now raised about the relationship between $\boldsymbol{n}_{r}^{l}$ and $\boldsymbol{n}^{l}$ for the $\boldsymbol{\alpha}$ model. At the limit stress point, substitution of the limit value for $\boldsymbol{\alpha}$ given by Eq. (34) in Eq. (4) after some straightforward algebra yields

$$
\frac{\partial f}{\partial \boldsymbol{\sigma}^{l}}=\left|\frac{\partial f}{\partial \boldsymbol{\sigma}^{l}}\right| \boldsymbol{n}^{l}=3\left|\boldsymbol{s}^{l}-\boldsymbol{\alpha}^{l}\right|\left\{\left[2-\frac{c^{l}}{a_{2}}\left(\boldsymbol{n}_{r}^{l}: \boldsymbol{n}^{l}\right)\right] \boldsymbol{n}_{r}^{l}-\frac{c^{l}}{a_{2}} \boldsymbol{n}^{l}\right\} \tag{36}
$$

The above equation can be solved for $|\partial f / \partial \boldsymbol{\sigma}^{l}|$ if one first multiplies both members by $\boldsymbol{n}^{l}$ and then takes the trace of the product observing that $\boldsymbol{n}^{l}: \boldsymbol{n}^{l}=1$, to obtain

$$
\left|\frac{\partial f}{\partial \boldsymbol{\sigma}^{l}}\right|=3\left|\boldsymbol{s}^{l}-\boldsymbol{\alpha}^{l}\right|\left\{\left[2-\frac{c^{l}}{a_{2}}\left(\boldsymbol{n}_{r}^{l}: \boldsymbol{n}^{l}\right)\right]\left(\boldsymbol{n}_{r}^{l}: \boldsymbol{n}^{l}\right)-\frac{c^{l}}{a_{2}}\right\} \tag{37}
$$

It takes some algebra to show that after substitution of Eq. (37) in Eq. (36) one can obtain

$$
\begin{aligned}
{\left[2-\frac{c^{l}}{a_{2}}\left(\boldsymbol{n}_{r}^{l}: \boldsymbol{n}^{l}\right)\right] \boldsymbol{n}_{r}^{l}-\frac{c^{l}}{a_{2}} \boldsymbol{n}^{l} } & =\left\{\left[2-\frac{c^{l}}{a_{2}}\left(\boldsymbol{n}_{r}^{l}: \boldsymbol{n}^{l}\right)\right]\left(\boldsymbol{n}_{r}^{l}: \boldsymbol{n}^{l}\right)-\frac{c^{l}}{a_{2}}\right\} \boldsymbol{n}^{l} \\
& \Rightarrow \boldsymbol{n}_{r}^{l}=\left(\boldsymbol{n}_{r}^{l}: \boldsymbol{n}^{l}\right) \boldsymbol{n}^{l}
\end{aligned} \tag{38}
$$

Given that $\boldsymbol{n}_{r}^{l}$ and $\boldsymbol{n}^{l}$ are unit tensors, it follows form the last equation that either $\boldsymbol{n}_{r}^{l}=\boldsymbol{n}^{l}$ or $\boldsymbol{n}_{r}^{l}=-\boldsymbol{n}^{l}$ thus, $(\boldsymbol{n}_{r}^{l}: \boldsymbol{n}^{l})^{2}=1$ always. Substitution of this last value into Eq. (37) and imposing the requirement that $|\partial f / \partial \boldsymbol{\sigma}^{l}| \geq 0$, it follows that

$$
\left(\boldsymbol{n}_{r}^{l}: \boldsymbol{n}^{l}\right)-\frac{c^{l}}{a_{2}} \geq 0 \tag{39}
$$

Clearly the case of $\boldsymbol{n}_{r}^{l}=-\boldsymbol{n}^{l}$ will violate the above inequality since the material constant $a_{2}$ and $c^{l}$ are positive. Thus, necessarily one has $\boldsymbol{n}_{r}^{l}=\boldsymbol{n}^{l}$ and therefore $\boldsymbol{n}_{r}^{l}: \boldsymbol{n}^{l}=1$ and the above inequality can be simplified to $c^{l} \leq a_{2}$. Substituting $\boldsymbol{n}_{r}^{l}=\boldsymbol{n}^{l}$ into the limit of $c$ in Eq. (35) gives

$$
c^{l}=\frac{1}{a_{2} c_{2}} \tag{40}
$$

thus inequality (39) can be simplified to $c_{2} a_{2}^{2} \geq 1$.

The evolution law for $c$ given in Eq. (19) allows for $c$ to increase towards its positive limit and decrease if upon reversal of loading the $\boldsymbol{n}_{r}: \boldsymbol{\alpha}<0$. Thus, conceivably the $c$ may eventually reach a negative value as long as the $\boldsymbol{n}_{r}: \boldsymbol{\alpha}<0$, but since the $\boldsymbol{\alpha}$ evolves towards alignment with $\boldsymbol{n}_{r}$, soon the $\boldsymbol{n}_{r}: \boldsymbol{\alpha}$ becomes positive and the $c$ resumes increasing again towards its limit value. The negative value that $c$ may acquire remains far from reaching an absolute value greater than its limit value. In other words it is unlikely that $c^{2}$ will ever be greater than $(c^{l})^{2}$ and in all numerical tests it has in fact been found that $c^{2} \leq(c^{l})^{2}$ for all time. Using $c^{2} \leq(c^{l})^{2}$, the requirement in Eq. (20) can be simplified to

$$
c_{2}\left(c^{l}\right)^{2} \leq 1 \Rightarrow \frac{c_{2}}{\left(c_{2} a_{2}\right)^{2}} \leq 1 \Rightarrow c_{2} a_{2}^{2} \geq 1 \tag{41}
$$

Notice that this is the same requirement on $c_{2}$ and $a_{2}$ necessary to make $|\partial f / \partial \boldsymbol{\sigma}^{l}| \geq 0$.

Subsequently addressing the $\boldsymbol{r}$ model, the limits to internal variables can be found by setting the rate Eqs. (17), (18), and (30) equal to zero. The resulting limits for $k$ and $\boldsymbol{\alpha}$ are the same as those given in Eqs. (33) and (34), respectively, and the limit for $\boldsymbol{r}$ is given by

$$
\boldsymbol{r}^{l}=\frac{1}{\rho_{2}} \boldsymbol{n}_{r}^{l} \tag{42}
$$

The constraint given in Eq. (31) must be satisfied by the maximum of $\boldsymbol{r}: \boldsymbol{r}$. Since $\boldsymbol{r}$ evolves along $\boldsymbol{n}_{r}$ according to Eq. (30) and $\boldsymbol{n}_{r}$ changes direction as soon as the loading direction changes, the maximum of $\boldsymbol{r}: \boldsymbol{r}$ is given by $\boldsymbol{r}^{l}: \boldsymbol{r}^{l}$. Thus, upon substitution of the limit of $\boldsymbol{r}$ given in Eq. (42) in the thermodynamic constraint of Eq. (31), the latter reduces to

$$
\rho_{2}\left(\boldsymbol{r}^{l}: \boldsymbol{r}^{l}\right) \leq 1 \Rightarrow \frac{1}{\rho_{2}} \leq 1 \Rightarrow 1<\rho_{2} \tag{43}
$$

### Positiveness

Rearrangement of the yield function expression given by Eq. (1) for the $\boldsymbol{\alpha}$ model yields $[1-(\boldsymbol{n}_{r}: \boldsymbol{\alpha})c]|\boldsymbol{s}-\boldsymbol{\alpha}|^{2}=k^{2}$, with the obvious requirements that

$$
1-\left(\boldsymbol{n}_{r}: \boldsymbol{\alpha}\right) c>0 \tag{44}
$$

The minimum of the left hand side of the inequality Eq. (44) is reached at the limit and is given by

$$
1-\left(\boldsymbol{n}_{r}^{l}: \boldsymbol{\alpha}^{l}\right) c^{l}=1-\frac{\boldsymbol{n}_{r}^{l}: \boldsymbol{n}^{l}}{c_{2} a_{2}^{2}}=1-\frac{1}{c_{2} a_{2}^{2}}>0 \tag{45}
$$

Inequality (45) places the same constraint on $c_{2}$ and $a_{2}$ as inequality (41) does, which was required for thermodynamics and $|\partial f / \partial \boldsymbol{\sigma}^{l}| \geq 0$.

Similarly, for the $\boldsymbol{r}$ model a rearrangement of the yield function expression (23) yields $[1-(\boldsymbol{n}_{r}: \boldsymbol{r})]|\boldsymbol{s}-\boldsymbol{\alpha}|^{2}=k^{2}$, with the obvious requirements that

$$
1-\left(\boldsymbol{n}_{r}: \boldsymbol{r}\right)>0 \tag{46}
$$

The minimum of this term is reached at the limit and is given by

$$
1-\frac{1}{\rho_{2}}>0 \tag{47}
$$

Inequality (47) places the same constraint on $\rho_{2}$ as inequality (43) does, which was required for satisfaction of the thermodynamic requirement.

### Convexity

Strict convexity requires proof that the Hessian matrix of second derivatives with regard to stress for the yield surface expressions given in Eqs. (1) and (23) for the two versions of the model, is positive definite. The complexity of Hessian matrix renders intractable such proof in closed analytical form, even for the limit case. Thus, it is not tractable to prove convexity but only to check it either by numerical calculation of the positive definiteness of the Hessian or, simply, by plotting the yield surfaces at different stages of loading. So far, and for the constants chosen to fit the data, the yield surfaces were easily found to be convex, in fact very far from becoming nonconvex. It must also be mentioned that the assumption of associative flow rule does not have as a prerequisite the convexity of the yield surface. It is the Drucker's or Illiushin's postulates which, once assumed, require convexity and normality simultaneously for the yield surface. Overall the issues of positive dissipation and positive terms $1-(\boldsymbol{n}_{r}: \boldsymbol{\alpha})c$ in the $\boldsymbol{\alpha}$ model and $1-(\boldsymbol{n}_{r}: \boldsymbol{r})$ in the $\boldsymbol{r}$ model are fundamental require-

---

JOURNAL OF ENGINEERING MECHANICS © ASCE / SEPTEMBER 2008 / 735

J. Eng. Mech. 2008.134:730-738.

![](./images/811905190222364672_2.jpg)

Fig. 2. $\alpha$ model with evolving $c$ compared to torsion experiments by Wu and Yeh (1991). First, second, third, and fourth subsequent yield surfaces resulted from strain controlled loading with final values $\gamma$=0.19, 0.38, 0.49, and 1.03%, respectively. Lines represent proposed constitutive model and discrete points represent experimental data.

ments of physics and mathematics, respectively, while convexity is related to assumed postulates and principles of very important but not fundamental nature.

## Comparison with Experimental Data

In order to show the effectiveness of the model, its simulations will be compared to experimentally found yield points. Figs. 2–5 show experimental data from Wu and Yeh (1991). These experiments were performed on thin-walled tubes of annealed 304 stainless steel. The data in Figs. 2 and 4 were obtained using a strain controlled procedure and loading in torsion (shear). For Figs. 3 and 5 the data were obtained using a stress controlled procedure with loading in combination with tension and torsion. Wu and Yeh defined yield as an offset equal to $5\mu$.

Fig. 6 shows experimental data from Boucher et al. (1995). These experiments were performed on thin-walled tubes of aluminium alloy AU4G T4 (2024). The tubes were loaded using stress control in combination with tension and torsion (shear) and yield was defined by an offset equal to $4×10^{-5}$. Fig. 6 shows loading and unloading in nonproportional path (path is given by $O$-$A$-$B$-$C$ as shown in the figure).

To fit these experiments, the two versions of the model were implemented numerically using the procedure outlined by Bardet and Choucair (1991). This procedure essentially takes loading increments of stress, strain, or combinations of the two and converts them into increments of stress only. Using this procedure, the numerical loading conditions exactly matched those from the experiment, and each increment of load is converted into stress increments. Once the stress increment is obtained, incremental changes of strain and internal variables are calculated using the associative flow rule [Eq. (3) with either Eq. (4) or (24)], the hardening rules, along with the standard calculations for loading index and plastic modulus. The numerical procedure solves the rate equations by an explicit method, and thus small steps were used to ensure convergence and good accuracy.

![](./images/811905190222364672_3.jpg)

Fig. 3. $\alpha$ model with evolving $c$ compared to stress controlled combined tension-torsion experiments by Wu and Yeh (1991). Loading path was proportional with $\sigma$=$\tau$. Lines represent proposed constitutive model and discrete points represent experimental data.

![](./images/811905190222364672_4.jpg)

Fig. 4. $r$ model compared to torsion experiments by Wu and Yeh (1991). First, second, third, and fourth subsequent yield surfaces resulted from strain controlled loading with final values $\gamma$=0.19, 0.38, 0.49, and 1.03%, respectively. Lines represent proposed constitutive model and discrete points represent experimental data.

![](./images/811905190222364672_5.jpg)

Fig. 5. $r$ model compared to stress controlled combined tension-torsion experiments by Wu and Yeh (1991). Loading path was proportional with $\sigma$=$\tau$. Lines represent proposed constitutive model and discrete points represent experimental data.

736 / JOURNAL OF ENGINEERING MECHANICS © ASCE / SEPTEMBER 2008

J. Eng. Mech. 2008.134:730-738.

![](./images/811905190222364672_6.jpg)

Fig. 6. $\boxed{\alpha}$ model with fixed $c$ compared to stress controlled combined tension and shear experiments by Boucher et al. (1995). Specimens were loaded in pure tension, unloaded some, then loaded in pure torsion. Load path is shown in figure as $O$-$A$-$B$-$C$. Computed initial yield surface (...); experiential initial yield points (*); computed first subsequent yield surface (---); experiential first subsequent yield points ($\bullet$); computed second subsequent yield surface (- - -); experiential second subsequent yield points ($	riangle$).

Table 1 shows the plastic material parameters used to obtain the model fitting in Figs. 2–5, and the elastic constants given by Wu and Yeh (1991). To determine the plastic material parameters, first experimental data were fit using only Armstrong–Frederick kinematic hardening along with isotropic hardening, then the amount of kinematic hardening was reduced (the limit value was increased and the rate of saturation slowed) to allow for distortion to be added. Finally, both the parameters associated with kinematic hardening ($a_1$ and $a_2$) as well as those associated with distortion ($c_1$ and $c_2$ or $\rho_1$ and $\rho_2$) were adjusted, using the constraint in Eqs. (41) or (43) as a guide. Thus the material parameters are not necessarily optimal for the material, but rather a relatively good fit for the data shown in Figs. 2–5. It was also observed that the use of a constant value of $c$ gave very good results compared to the choice of a variable $c$ (this can also be detected from the large difference of the numerical values of $c_1$ and $c_2$ in Table 1, with $c_2$ associated with the limit and $c_1$ with the pace of evolution). The constant value of $c$ still allows for the directional distortional feature of the $\boxed{\alpha}$ model and can be viewed as a special case that is even simpler than those presented in this paper. Clearly, there are some flaws in the way the models fit the data. Since the Wu and Yeh (1991) data in Figs. 2 and 4 were fit using strain control, it was much more difficult to match the stress points, which can be seen in these figures. With both the $\boxed{\alpha}$ and $\boxed{r}$ models, the simulations fit the region of high curvature relatively well, but they do not show sufficient flattening in the opposite direction, whereas the experiments do. The same relative success of fitting the data is shown in Fig. 6 where the data from Boucher et al. (1995) are simulated by using the $\boxed{\alpha}$ model in its simplest form of a constant $c$=0.019 MPa$^{-1}$. For this more complex loading path the fitting of the data may be considered satisfactory given the extreme simplicity of the model used. For a better fitting of data with regard to the flattening portion of the yield surface the reader is referred to the work by Feigenbaum and Dafalias (2007) where the use of a fourth-order evolving tensor-valued internal variable in the yield surface expression in conjunction with the directional quantity $\boldsymbol{n}_r$:$\boxed{\alpha}$, which is also used in the present development, allows for greater flexibility in matching the data points, but also introduces a quite more complex model.

Also, it appears that the $\boxed{r}$ model does not necessarily do a better job in fitting the experimental data than the $\boxed{\alpha}$ model. However, the additional degrees of freedom in using a directional tensor $\boxed{r}$, independent of the backstress $\boxed{\alpha}$, may improve predictions for other material, other loading paths, or for complex stress-strain data (e.g., cyclic plasticity), in addition to the theoretical advantage of decoupling residual stress development from directional distortion.

### Conclusion and Discussion

The present paper introduces a complete theory for metal plasticity that includes the development of anisotropy through kinematic and directional distortional hardening, supplemented by the classical isotropic hardening. The directional distortion of the yield surface (the development of a region of high curvature in approximately the direction of loading and a flattening on the opposite side) was modeled by either a scalar internal variable $c$ in conjunction with the back stress $\boxed{\alpha}$ in the so-called $\boxed{\alpha}$ model version, or a second-order tensor internal variable $\boxed{r}$ in the $\boxed{r}$ model version.

The evolution law for $c$ is such as to allow for $c$ to change upon reversal of loading and its evolution to depend on the direction of loading via the scalar quantity $\boldsymbol{n}_r$:$\boxed{\alpha}$. Basically the rate equation for $c$ is of the evanescent memory type requiring two constants, and does not seem to have been proposed before for a scalar-valued variable. Most scalar evolution laws are similar to those given for $k$, where the evolution of $k$ does not depend on the direction of loading and reaches a saturation level for ever after. In the $\boxed{r}$ model the second-order tensor $\boxed{r}$ allows for the decoupling between kinematic and directional distortional hardening which gives the modeler more flexibility. Again this model requires two more constants than a classical kinematic/isotropic hardening model, associated with the evanescent memory type rate equation for $\boxed{r}$.

All hardening rules for these models came from conditions sufficient to satisfy the dissipation inequality (second law of thermodynamics) so that energy transfer during plastic work may be tracked. The derivation distinguished between energy dissipated and energy stored or released as parts of the plastic free energy. We assumed that this stored or released plastic free energy could be decomposed into parts associated with isotropic, kinematic, and directional distortional hardening. Based on experimental observations and the given mathematical constructs, we proposed that the material releases, rather than stores, energy as distortion of the yield surface occurs (directional distortional hardening),

<table>
<caption>Table 1. Material Constants Used in Figs. 2–5</caption>
<thead>
<tr>
<th>
</th>
<th>
$\boxed{\alpha}$ model
</th>
<th>
$\boxed{r}$ model
</th>
</tr>
</thead>
<tbody>
<tr>
<td>
$E$
</td>
<td>
196,687 MPa
</td>
<td>
196,687 MPa
</td>
</tr>
<tr>
<td>
$\nu$
</td>
<td>
0.28
</td>
<td>
0.28
</td>
</tr>
<tr>
<td>
$k_0$
</td>
<td>
128 MPa
</td>
<td>
128 MPa
</td>
</tr>
<tr>
<td>
$\kappa_1$
</td>
<td>
6,000 MPa$^2$
</td>
<td>
6,000 MPa$^2$
</td>
</tr>
<tr>
<td>
$\kappa_2$
</td>
<td>
0.012 MPa$^{-1}$
</td>
<td>
0.012 MPa$^{-1}$
</td>
</tr>
<tr>
<td>
$a_1$
</td>
<td>
17,000 MPa
</td>
<td>
18,000 MPa
</td>
</tr>
<tr>
<td>
$a_2$
</td>
<td>
0.012 MPa$^{-1}$
</td>
<td>
0.01 MPa$^{-1}$
</td>
</tr>
<tr>
<td>
$c_1$
</td>
<td>
0.01 MPa$^{-3}$
</td>
<td>
—
</td>
</tr>
<tr>
<td>
$c_2$
</td>
<td>
10,001 MPa$^2$
</td>
<td>
—
</td>
</tr>
<tr>
<td>
$\rho_1$
</td>
<td>
—
</td>
<td>
1.9 MPa$^{-1}$
</td>
</tr>
<tr>
<td>
$\rho_2$
</td>
<td>
—
</td>
<td>
1.3
</td>
</tr>
</tbody>
</table>

JOURNAL OF ENGINEERING MECHANICS © ASCE / SEPTEMBER 2008 / 737

J. Eng. Mech. 2008.134:730-738.

while the material stores energy as the yield surface changes lo- cation (kinematic hardening) and size (isotropic hardening). The physics of this proposition was given a plausible interpretation following Eq. (10). For the particularly simple case of the $\boxed{\alpha}$ model with a constant $c$ no question of storing or releasing energy arises, but the $c$ still plays its distortion inducing role in a passive way. The derivation gave rise to evanescent-memory type hard- ening rules (evolution laws) for scalar and tensor-valued internal variables, which allows for saturation of developing anisotropy by the limits imposed on the variables during monotonic loading, but also allows desaturation upon loading reversals. An exception was the isotropic hardening variable whose evolution law, which also arises from thermodynamics, correctly yields, a monotonically increasing response until it reaches a saturation value forever after.

Of practical importance is the minimum possible number of material constants associated with the nonlinear evolution of each internal variable (two constants for each internal variable). In es- sence the model adds to a typical isotropic and nonlinear kine- matic hardening model, the directional distortion characteristics, and it does it in the simplest possible way by adding only two additional material constants for the rate equation of evolution (distortional directional hardening) of $c$ or $\boldsymbol{r}$. Such simplicity and practicality is enhanced by the fact that thermodynamic condi- tions impose only one very mild inequality restriction [Eqs. (41) or (43)], which was found to be easily satisfied for real cases. In this respect the present models simulations were compared to experimental data on yield surfaces, and while the model clearly has some limitations in fitting the data, overall it captured the distorted shape of the yield surface.

Work in progress is aiming to use the directional distortional hardening model presented here as well as that presented in Feigenbaum and Dafalias (2007), not only to address the distorted shape of a yield surface, but also to simulate the stress-strain curves obtained by monotonic and cyclic loading, a task which is of significantly greater difficulty.

### Notation
The following symbols are used in this paper:

$a_1$, $a_2$ = material parameters associated with evolution of $\boxed{\alpha}$;
$c$ = scalar-valued distortional model parameter;
$c_c$ = thermodynamic conjugate to $c$;
$c^l$ = limit value of $c$;
$c_1$, $c_2$ = material parameters associated with evolution of backstress;
$f$ = yield function;
$K_p$ = plastic modulus;
$k$ = internal variable representing size of yield surface;
$k_c$ = thermodynamic conjugate to $k$;
$k^l$ = limit value of $k$;
$\boxed{n}$ = outward unit normal to yield surface;
$\boxed{n}^l$ = limit value of $\boxed{n}$ in given loading path;
$\boxed{n}_r$ = unit traceless radial tensor that goes along direction $s-\boxed{\alpha}$;
$\boxed{n}_r^l$ = limit value of $\boxed{n}_r$ in given loading path;
$\boldsymbol{r}$ = second-order tensor-value directional distortional internal variable;
$\boldsymbol{r}_c$ = thermodynamic conjugate to $\boldsymbol{r}$;
$\boldsymbol{r}^l$ = limit value of $\boldsymbol{r}$;
$\boldsymbol{s}$ = devatoric part of stress tensor;
$\boxed{\alpha}$ = deviatoric part of backstress tensor;
$\boxed{\alpha}_c$ = thermodynamic conjugate to $\boxed{\alpha}$;
$\boxed{\alpha}^l$ = limit value of $\boxed{\alpha}$;
$\boxed{\varepsilon}$ = linearized strain tensor;
$\boxed{\varepsilon}^e$, $\boxed{\varepsilon}^p$ = elastic and plastic parts of linearized strain tensor, respectively;
$\kappa_1$, $\kappa_2$ = material parameters associated with evolution of $k$;
$\lambda$ = loading index;
$\rho$ = density;
$\rho_1$, $\rho_2$ = material parameters associated with evolution of $\boldsymbol{r}$;
$\boxed{\sigma}$ = Cauchy stress;
$\psi$ = free energy;
$\psi_p^{\text{ani}}$ = anisotropic part of plastic free energy;
$\psi_p^{\text{dis}}$ = distortional part of plastic free energy;
$\psi_e$, $\psi_p$ = elastic and plastic parts of free energy, respectively;
$\psi_p^{\text{iso}}$ = isotropic part of plastic free energy; and
$\psi_p^{\text{kin}}$ = kinematic part of plastic free energy.

### References
Bardet, J. P., and Choucair, W. (1991). “A linearized integration technique for incremental constitutive equations.” *Int. J. Numer. Analyt. Meth. Geomech.*, 15, 1–19.

Boucher, M., Cayla, P., and Cordebois, J. P. (1995). “Experimental stud- ies of yield surfaces of aluminum alloy and low carbon steel under complex biaxial loadings.” *Eur. J. Mech. A/Solids*, 14(1), 1–17.

Dafalias, Y. F., Schick, D., and Tsakmakis, C. (2002). “A simple model for describing yield surface evolution.” *Lecture note in applied and computational mechanics*, K. Hutter and H. Baaser, eds., Springer, Berlin, 169–201.

Feigenbaum, H. P., and Dafalias, Y. F. (2007). “Directional distortional hardening in metal plasticity within thermodynamics.” *Int. J. Solids Struct.*, 44, 7526–7542.

François, M. (2001). “A plasticity model with yield surface distortion for nonproportional loading.” *Int. J. Plast.*, 17, 703–717.

Kurtyka, T., and Zyczkowski, M. (1996). “Evolution equations for distor- tional plastic hardening.” *Int. J. Plast.*, 12(2), 191–203.

McComb, H. G. (1960). “Some experiments concerning subsequent yield surfaces in plasticity.” *Rep. No. D-396*, National Aeronautics and Space Adminstration, Washington, D.C.

Naghdi, P. M., Essenburg, F., and Koff, W. (1958). “An experimental study of initial and subsequent yield surfaces in plasticity.” *J. Appl. Mech.*, 25(2), 201–209.

Ortiz, M., and Popov, P. E. (1983). “Distortional hardening rules for metal plasticity.” *J. Eng. Mech.*, 109(4), 1042–1057.

Phillips, A., Tang, J.-L., and Ricciuti, M. (1975). “Some new observa- tions on yield surfaces.” *Acta Mech.*, 20, 23–39.

Voyiadjis, G. Z., and Foroozesh, M. (1990). “Anisotropic distortional yield model.” *J. Appl. Mech.*, 57, 537–547.

Wei-Ching Yeh, C.-D. H., and Pan, W.-F. (1996). “An endochronic theory accounting for deformation induced anisotropy of metals under biax- ial load.” *Int. J. Plast.*, 12(8), 987–1004.

Wu, H. C., and Yeh, W. C. (1991). “On the experimental determination of yield surfaces and some results of annealed 304 stainless steel.” *Int. J. Plast.*, 7, 803–826.