Journal Pre-proofs

New Robust Self-Consistent Homogenization Schemes of Elasto-Viscoplastic
Polycrystals

Miroslav Zecevic, Ricardo A. Lebensohn

<table>
  <tr>
    <td>PII:</td>
    <td>S0020-7683(20)30205-5</td>
  </tr>
  <tr>
    <td>DOI:</td>
    <td>https://doi.org/10.1016/j.ijsolstr.2020.05.032</td>
  </tr>
  <tr>
    <td>Reference:</td>
    <td>SAS 10735</td>
  </tr>
  <tr>
    <td>To appear in:</td>
    <td>International Journal of Solids and Structures</td>
  </tr>
  <tr>
    <td>Received Date:</td>
    <td>14 February 2020</td>
  </tr>
  <tr>
    <td>Revised Date:</td>
    <td>15 April 2020</td>
  </tr>
  <tr>
    <td>Accepted Date:</td>
    <td>27 May 2020</td>
  </tr>
</table>

![](./images/812597125853478914_1.jpg)

Please cite this article as: M. Zecevic, R.A. Lebensohn, New Robust Self-Consistent Homogenization Schemes of Elasto-Viscoplastic Polycrystals, *International Journal of Solids and Structures* (2020), doi: https://doi.org/10.1016/j.ijsolstr.2020.05.032

This is a PDF file of an article that has undergone enhancements after acceptance, such as the addition of a cover page and metadata, and formatting for readability, but it is not yet the definitive version of record. This version will undergo additional copyediting, typesetting and review before it is published in its final form, but we are providing this version to give early visibility of the article. Please note that, during the production process, errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

© 2020 Published by Elsevier Ltd.

# New Robust Self-Consistent Homogenization Schemes of Elasto-Viscoplastic Polycrystals

Miroslav Zecevic* and Ricardo A. Lebensohn

Theoretical Division, Los Alamos National Laboratory, Los Alamos, NM, 87544, USA.

*Corresponding author: miroslav@lanl.gov

## Abstract

Three novel and robust homogenization schemes for polycrystals deforming in the elasto-viscoplastic regime are proposed, two of them of the self-consistent type and the other combining self-consistent and Mori-Tanaka methods. In addition, a non-incremental interaction equation for an elasto-viscoplastic inhomogeneity problem is also derived. Second moments of stress and strain field distributions within the grains are estimated using the algorithms developed for linear heterogeneous materials. A thorough description of the approximations, methodology and algorithms involved is given, and, using the case of a copper polycrystal, it is shown that the proposed methods obey the elastic and viscoplastic limits. The new homogenization schemes are then applied to the case of tension of stainless steel, including the prediction of intragranular averages and standard deviations of lattice strains. These predictions are compared to published experimental measurements and corresponding full-field polycrystal plasticity results. Acceptable agreement of the predicted grain-averaged lattice strains with both experiments and full-field results was observed, while the calculated standard deviations of lattice strains matched well only with the full-field predictions.

Keywords: Homogenization; Elastic-viscoplastic solids; Self-consistent method; Crystal plasticity

## 1 Introduction

Micromechanical fields developing during thermo-mechanical processing of polycrystalline materials are heterogeneous within the single crystal grains of the aggregate (e.g. Humphreys and Hatherly, 2012) and depend, in general, on crystallographic orientation and interaction with


neighbor grains. Understanding the evolution of these intragranular distributions is of great importance for the design of new materials and for safety of components in service (e.g. Fullwood et al., 2010; Verlinden et al., 2007), as well for identification of deformation mechanisms at single crystal level. Experimentally, internal distributions of micromechanical fields (e.g. stress and strain) can be measured using high-energy X-ray (e.g. Miller et al., 2008), or neutron diffraction techniques (e.g. Neil et al., 2010). These experimental methods can be complemented, for interpretation and cross-validation, by full-field crystal plasticity (CP) models, such as crystal plasticity finite element methods (CPFEM) (Dawson and Marin, 1997; Kalidindi et al., 1992; Roters et al., 2010, etc.) or crystal plasticity fast Fourier transform-based (CPFFT) methods (Lebensohn, 2001; Lebensohn et al., 2012, etc.; Michel et al., 1999; Moulinec and Suquet, 1998). These formulations are capable of simulating micromechanical fields with intragranular resolution. For example, Dawson et al. (2005) and Kanjarla et al. (2012) used CPFEM and CPFFT models, respectively, to study the evolution of intragranular lattice strain distributions and compared the predictions with the neutron diffraction measurements. Raabe et al. (2001) and Turner et al. (2012) compared local strain fields predicted by a CPFEM model with the experimental measurements taken on the surface of a polycrystalline specimen. Intragranular orientation fields predicted by CPFEM and CPFFT models were compared to the corresponding experimental EBSD measurements by Buchheit et al. (2005); Kalidindi et al. (2004); Quey et al. (2012); Quey et al. (2015) and by Lebensohn et al. (2008); Zecevic et al. (2018), respectively. High energy X-ray measurements of stresses in polycrystalline samples were compared with CPFEM predictions by Miller et al. (2008), while Pokharel et al. (2014) compared the measurements of local orientation fields with CPFFT model predictions.

In addition to computationally intensive full-field formulations, mean-field homogenization approaches are also quite successful in simulating mechanical behavior and microstructural evolution of polycrystalline materials (e.g. Lebensohn et al., 2007), at much lower computational cost. The self-consistent (SC) approach, originally proposed by Hershey (1954), for linear elastic materials, is one of the most commonly used homogenization methods to estimate the mechanical response behavior of polycrystals. For nonlinear aggregates (as those formed by grains deforming plastically), SC approximations differ in the procedure used to linearize the non-linear local mechanical behavior, to eventually make use of the linear SC theory.

In addition to the use in first-order SC homogenization of the first moments (grain averages) of micromechanical fields within the grains of a polycrystalline aggregate, specialized algorithms have been developed to enable the estimation of second moments (average fluctuations) of intragranular stress fields (Lebensohn et al., 2007; Liu, 2003) for linear or linearized behaviors. These algorithms are extensions of the original methodology for linear composites (Bobeth and Diener, 1987; Kreher, 1990). These estimates were used in combination with variational principles to formulate more accurate second-order linearizations, originally formulated for non-linear rigid-viscoplastic composites (Ponte Castañeda, 2002) later extended to viscoplastic polycrystals (Liu and Ponte Castañeda, 2004; Song and Ponte Castañeda, 2018) by treating polycrystalline aggregates as n-phase composites, with each grain orientation considered as a mechanical phase of the n-phase composite.

Using constitutive and kinematic relations between stresses, strains and rotations, these intragranular second moments of stress were in turn used to estimate second moments of lattice rotations, enabling the prediction of average intragranular misorientation evolution (Lebensohn et al., 2016; Zecevic et al., 2017). These algorithms were implemented within the context of the viscoplastic self-consistent (VPSC) approach, and used to predict thermo-mechanical behavior driven by intragranular misorientations, e.g. grain fragmentation (Zecevic et al., 2018) and recrystallization (Zecevic et al., 2019). Despite these enhanced capabilities, since elasticity is neglected in a rigid-viscoplastic approach, the aforementioned VPSC extension is still incapable of predicting evolution of lattice (elastic) strains during loading. In order to enable prediction of, e.g., intragranular averages and average fluctuations of elastic strain fields for direct comparison with lattice spacing measurements (e.g. diffraction peak broadening due to intragranular elastic heterogeneity), elasticity needs to be considered along with plasticity. This is the main focus and contribution of this paper, i.e. the formulation of novel and numerically stable SC homogenization schemes for elasto-viscoplastic polycrystals, including a robust estimation of average intragranular fluctuations of the micromechanical fields.

Different elastoplastic self-consistent methods have been proposed since the 1960's. In their pioneering work, Kröner (1961), and Budiansky and Wu (1961) (KBW) proposed the first elastoplastic self-consistent method. In KBW's approach, the interaction between the homogenized medium and the spherical inclusions representing elastoplastic grains—i.e.

Eshelby's inclusion problem (Eshelby, 1957), which can be considered as the basis of every SC approximation—was assumed to be elastic and thus overly stiff, resulting in an almost uniform strain rate over the aggregate. Weng (1981) has shown that this type of interaction is valid for the case of creep in metals. Hill (1965) proposed an incremental elastoplastic (rate-independent) self-consistent method. The stress rates in both the grains and the matrix were assumed linearly proportional to the corresponding total strain rate, where the linear relation was given by the instantaneous elastoplastic modulus. The Eshelby solution was used incrementally, with the Eshelby tensor defined based on the elastoplastic modulus of the matrix, thus taking into account both elastic and plastic interactions between the matrix and the inhomogeneity representing a grain. Berveiller and Zaoui (1978) proposed a computationally efficient simplified self-consistent method based on Hill's approach where the interaction law was based on the isotropic approximation of effective compliance. Hill's formulation was extended to finite strains (Iwakuma and Nemat-Nasser, 1984; Lipinski and Berveiller, 1989), and to account for thermal dilatation effects and full grain anisotropy (Turner and Tomé, 1994).

Hutchinson (1976) adopted Hill's incremental interaction law for the self-consistent homogenization of a rigid-viscoplastic polycrystal, which gave rise to the branch of rigid-viscoplastic self-consistent VPSC models mentioned in precedent paragraphs. Molinari et al. (1987) developed a non-incremental interaction law for purely viscoplastic constitutive behavior and used it within the context of self-consistent homogenization. The model was later further improved to consider the case of full anisotropy of the macroscopic tangent modulus by Lebensohn and Tomé (1993). The resulting VPSC code has found a wide variety of applications and underwent further improvements. The latter includes the calculation of intragranular second moments of stress, which allowed implementation of the aforementioned Ponte Castañeda et al.'s advanced second-order linearizations, and Zecevic et al.'s intragranular misorientation predictions. However, in order to capture elastic effects, including intragranular heterogeneity of elastic strain fields, the interplay between elasticity and viscoplasticity needs to be considered in the context of more complex elasto-viscoplastic self-consistent formulations.

Nemat-Nasser and Obata (1986) applied Hill's incremental formulation to the case of elasto-viscoplastic grain behavior. Non-linear single crystalline response was first linearized and the resulting elasto-viscoplastic modulus of the grain along with an analogous modulus defined for

the matrix were used within the Hill's incremental interaction law. On the other hand, an additive interaction law for elasto-viscoplastic polycrystals obtained by summation of purely elastic and non-incremental viscoplastic interaction laws was first proposed by Molinari et al. (1997). Molinari et al. (1997)'s interaction law was compared against full-field finite element calculations by Mercier et al. (2005), used within the context of self-consistent and Mori-Tanaka (Mori and Tanaka, 1973) homogenizations by Mercier and Molinari (2009), and implemented in the VPSC code by Wang et al. (2010), which they called EVPSC code. Recently, Jeong and Tomé (2019) proposed a variant of the EVPSC model/code based on the rigid-viscoplastic self-consistent formulation, where the effect of elasticity is introduced through a perturbation of the grain's viscoplastic constitutive response. The effect of the perturbation eigenstrain rate accounting for the elasticity is calculated using of Molinari et al. (1997)'s interaction equation.

Variational principles that include the estimation and use of intragranular second moments as part of the homogenization procedure for elasto-viscoplastic polycrystals have also been proposed in recent literature. Lahellec and Suquet (2007a, b) developed a general framework for homogenization (e.g. self-consistent) of nonlinear inelastic (e.g. elasto-viscoplastic) heterogeneous materials (composites, as well as polycrystals treated as $n$-phase composites) by extending variational formulations à-la Ponte Castañeda. First and second moments of stress in the individual phases of the inelastic composite were assumed the same as in a linear comparison thermo-elastic composite. Thermo-elastic properties of the comparison composite were calculated by minimizing the effective incremental potential of the nonlinear composite, derived using the incremental variational principles proposed by Ortiz and Stainier (1999). Further variations of the model proposed by Lahellec and Suquet (2007a) can be found in Brassart et al. (2012), Lahellec and Suquet (2013) and Agoras et al. (2016).

An alternative elasto-viscoplastic homogenization scheme based on the translated field method was proposed by Paquin et al. (1999). In this approach, the equilibrium and compatibility equations are transformed into a set of equations in terms of a modified Green's tensor (Kröner, 1990). The actual elasto-viscoplastic problem is decomposed into three sub-problems governed by integral equations: purely elastic, purely viscoplastic and translated problems, where the translated strain rate represents the strain rate field that accounts for the interaction between the purely elastic and viscoplastic constitutive behaviors. The translated field approach has been first

applied to polycrystals in (Paquin et al., 2001) and further extended by (Berbenni and Capolungo, 2015; Mareau and Berbenni, 2015; Sabar et al., 2002). Mercier et al. (2012) compared the translated field interaction law with the interaction law of Molinari et al. (1997).

In this paper, we formulate novel SC and SC combined with Mori-Tanaka schemes for elasto-viscoplastic polycrystals, including an estimation of average intragranular fluctuations of the micromechanical fields. Moreover, we propose a new non-incremental elasto-viscoplastic interaction law motivated by Hill's (1965) incremental elastoplastic interaction law. This interaction law is derived by directly applying Eshelby's equivalent inclusion method to the elasto-viscoplastic inhomogeneity problem. Consequently, the obtained interaction tensors appearing in the interaction equation depend on both elastic and viscoplastic properties of the matrix. This constitutes an improvement over Molinari et al.'s (1997) interaction equation, in which the elastic and viscoplastic interaction tensors are calculated completely separate, and dependent only on the elastic or viscoplastic properties of the matrix, respectively. Next, we develop three different numerically stable models for homogenization of non-linear elasto-viscoplastic polycrystals. The concentration tensors, used to defined localization relations and for the calculation of effective properties are rigorously derived from the corresponding interaction equations, which ensures good convergence of each proposed method. The preexisting elasto-viscoplastic self-consistent methods of Mercier and Molinari (2009) and Wang et al. (2010) are based on concentration tensors derived from the separate purely elastic and viscoplastic interaction equations, which is inconsistent with the elasto-viscoplastic interaction equation they adopted. Consequently, these methods may lead to numerical difficulties, especially during the elastoplastic transition, and poor overall convergence, as noted by Jeong and Tomé (2019). In addition, we investigate the feasibility of calculation of second moments of stress and strain fields in the grains in the context of the newly proposed models. The second moments of stress and strain are used only as output of the model, not as part of the homogenization procedure as, e.g. in Lahellec and Suquet (2007a, 2007b), and are compared with experiments and full-field predictions obtained with an elasto-viscoplastic FFT-based (EVPFFT) code (Kanjarla et al., 2012).

The developed models are first applied to compression of copper and compared to the purely elastic and viscoplastic self-consistent predictions. Results converge to elastic self-consistent

addition, all the grain variables are rotating with the lattice spin ensuring that all the quantities are in the same configuration and thus incremental objectivity is satisfied (Dunne and Petrinic, 2005; Miehe et al., 2010). By replacing the Eq. (8) into Eq. (7) and after regrouping of terms, we may write:

$$
\dot{\varepsilon}^{(r)}=M^{e v(r)}: \sigma^{(r), t+\Delta t}+\dot{\varepsilon}^{e v 0(r)},
\tag{9}
$$

where the moduli $M^{e v(r)}$ and $\dot{\varepsilon}^{e v 0(r)}$ are:

$$
M^{e v(r)}=\frac{1}{\Delta t} M^{e(r)}+M^{e w(r)}+M^{v(r)}
\tag{10}
$$

$$
\dot{\varepsilon}^{e v 0(r)}=\dot{\varepsilon}^{v 0(r)}-\frac{1}{\Delta t} M^{e(r)}: \sigma^{(r), t}.
\tag{11}
$$

### 2.1.2 Elasto-viscoplastic inhomogeneity: interaction equation and stress concentration tensors

We consider a problem of a linear (or linearized) elasto-viscoplastic inhomogeneity embedded in the linear (or linearized) elasto-viscoplastic matrix. We first consider the purely elastic and purely viscoplastic inhomogeneity and then define two approximations for the elasto-viscoplastic problem. In the following derivation we have temporarily neglected the effect of rigid rotation on the stress rate, i.e. $M^{e w(r)}=0$. This effect will be reintroduced in the section dealing with homogenization.

#### 2.1.2.1 Elastic inhomogeneity

An infinite matrix has linear elastic behavior defined by elastic compliance $M^{e}$. Let us assume there exists an ellipsoidal domain $r$ (inhomogeneity) within the matrix, which has linear elastic behavior defined by compliance $M^{e(r)}$, which differs from the matrix. Certain boundary conditions are applied to the matrix at infinity. Stress in the inhomogeneity can be calculated by invoking the Eshelby's equivalent inclusion approach (Eshelby, 1957; Mura, 2013). The inhomogeneity can be replaced by an equivalent ellipsoidal inclusion with the same properties as the matrix and an elastic eigenstrain rate $\dot{\varepsilon}^{e(r) *}$ and the following interaction equation is derived (see Lebensohn et al. (2007) for details):

$$
\dot{\varepsilon}^{e(r)}-\dot{E}^{e}=-\tilde{M}^{e(r)}:\left(\dot{\sigma}^{(r)}-\dot{\Sigma}\right),
\tag{12}
$$

where $\dot{E}^{e}$ and $\dot{\Sigma}$ are elastic strain rate and stress rate in the matrix and $\dot{\varepsilon}^{e(r)}$ and $\dot{\sigma}^{(r)}$ elastic strain rate and stress rate in the inhomogeneity. The elastic interaction tensor is given by:

$$
\tilde{M}^{e(r)}=\left(I-S^{e(r)}\right)^{-1}: S^{e(r)}: M^{e},
\tag{13}
$$

where $S^{e(r)}$ is the elastic Eshelby tensor.

The elastic stress rate concentration tensor, $\hat{B}^{e(r)}$, maps the macroscopic stress rate to local grain stress rate, resulting in the following localization equation:

$$
\dot{\sigma}^{(r)}=\hat{B}^{e(r)}: \dot{\Sigma},
\tag{14}
$$

where "^" over the concentration tensors denotes that it operates on the rates of stress. Expression for the stress rate concentration tensor is derived directly from the interaction equation:

$$
\hat{B}^{e(r)}=\left(M^{e(r)}+\tilde{M}^{e(r)}\right)^{-1}:\left(\tilde{M}^{e(r)}+M^{e}\right).
\tag{15}
$$

#### 2.1.2.2 Viscoplastic inhomogeneity

Consider an infinite linear (or linearized) viscoplastic matrix with constitutive behavior given by:

$$
\dot{E}^{v}=M^{v}: \Sigma+\dot{E}^{v 0},
\tag{16}
$$

where $\dot{E}^{v}$ and $\Sigma$ are viscoplastic strain rate and stress in the matrix and $M^{v}$ and $\dot{E}^{v 0}$ are viscoplastic compliance and viscoplastic back-extrapolated strain rate in the matrix. Let us assume there exists an ellipsoidal domain $r$ (inhomogeneity) within the matrix, which has constitutive behavior given by Eq. (2). Analogous to the elastic problem, the inhomogeneity can be replaced with an equivalent inclusion to which an additional viscoplastic eigenstrain rate has been applied and the following interaction equation is derived (Lebensohn and Tomé, 1993; Lebensohn et al., 2007; Molinari et al., 1987):

$$
\dot{\varepsilon}^{v(r)}-\dot{E}^{v}=-\tilde{M}^{v(r)}:\left(\sigma^{(r)}-\Sigma\right).
\tag{17}
$$

The viscoplastic interaction tensor, $\tilde{M}^{v(r)}$, is given by:

$$
\tilde{M}^{v(r)}=\left(I-S^{v(r)}\right)^{-1}: S^{v(r)}: M^{v},
\tag{18}
$$

where $S^{v(r)}$ is the viscoplastic Eshelby tensor.

The viscoplastic stress concentration tensors, $B^{v(r)}$ and $b^{v(r)}$, relate the local grain stress with the macroscopic stress through the following localization equation:

$$
\sigma^{(r)}=B^{v(r)}: \Sigma+b^{v(r)}, \tag{19}
$$

where the expressions for the stress concentration tensors are derived from the interaction equation and are given by Lebensohn et al. (2007):

$$
B^{v(r)}=\left[M^{v(r)}+\tilde{M}^{v(r)}\right]^{-1}:\left[\tilde{M}^{v(r)}+M^{v}\right], \tag{20}
$$

$$
b^{v(r)}=\left[M^{v(r)}+\tilde{M}^{v(r)}\right]^{-1}:\left[\dot{E}^{v 0}-\dot{\varepsilon}^{v 0(r)}\right]. \tag{21}
$$

#### 2.1.2.3 Elasto-viscoplastic inhomogeneity

Next, we consider an infinite elasto-viscoplastic matrix with constitutive behavior:

$$
\dot{E}=M^{e}: \dot{\Sigma}+M^{v}: \Sigma+\dot{E}^{v 0}. \tag{22}
$$

Within the matrix, there is an ellipsoidal inhomogeneity $r$ with constitutive behavior:

$$
\dot{\varepsilon}^{(r)}=M^{e(r)}: \dot{\sigma}^{(r)}+M^{v(r)}: \sigma^{(r)}+\dot{\varepsilon}^{v 0(r)}. \tag{23}
$$

Boundary conditions are applied to the matrix at infinity. In what follows, we consider two solutions to this problem.

##### 2.1.2.3.1 Interaction equation proposed by Molinari et al. (1997)

Molinari et al. (1997) have proposed the following interaction equation:

$$
\dot{\varepsilon}^{(r)}-\dot{E}=-\tilde{M}^{e(r)}:\left(\dot{\sigma}^{(r)}-\dot{\Sigma}\right)-\tilde{M}^{v(r)}:\left(\sigma^{(r)}-\Sigma\right). \tag{24}
$$

It is clear that the defined interaction law (to be denoted MAK97 in what follows) represents the sum of the purely elastic and purely viscoplastic interaction equations (Eqs. (12) and (17), respectively). The elastic and viscoplastic interaction tensors (and corresponding Eshelby tensors) were derived by considering separate purely elastic and viscoplastic inhomogeneity but are used for the coupled elasto-viscoplastic problem. By adopting the joint interaction law (Eq. 24), both elastic and viscoplastic interaction equations used for definition of the corresponding interaction tensors become invalid. Consequently, elastic and viscoplastic interaction tensors

stem from the equations which are no longer valid which is a contradiction caused by the adopted approximation.

The above interaction equation is a linear first-order differential equation in $\sigma^{(r)}$. Derivatives with respect to time can be approximated using the Euler backward method, given by Eq. (8) and $\dot{\Sigma}=(\Sigma^{t+\Delta t}-\Sigma^{t})/\Delta t$. By replacing the expressions for $\dot{E}$, $\dot{\varepsilon}^{(r)}$, $\dot{\Sigma}$ and $\dot{\sigma}^{(r)}$ (Eqs. (22-23 and 8)) into the interaction equation, we define the following elasto-viscoplastic stress concentration tensors:

$$
B^{e, v(r)}=\left[\frac{1}{\Delta t} M^{e(r)}+M^{v(r)}+\frac{1}{\Delta t} \widetilde{M}^{e(r)}+\widetilde{M}^{v(r)}\right]^{-1}:\left[\frac{1}{\Delta t} \widetilde{M}^{e(r)}+\widetilde{M}^{v(r)}+\frac{1}{\Delta t} M^{e}+M^{v}\right], \quad(25)
$$

$$
\begin{aligned}
& b^{e, v(r)}=\left[\frac{1}{\Delta t} M^{e(r)}+M^{v(r)}+\frac{1}{\Delta t} \widetilde{M}^{e(r)}+\widetilde{M}^{v(r)}\right]^{-1}:\left[\left(\frac{1}{\Delta t} \widetilde{M}^{e(r)}+\frac{1}{\Delta t} M^{e(r)}\right): \sigma^{(r) t}-\right. \\
& \left.\left(\frac{1}{\Delta t} M^{e}+\frac{1}{\Delta t} \widetilde{M}^{e(r)}\right): \Sigma^{t}+\dot{E}^{v 0}-\dot{\varepsilon}^{v 0(r)}\right].
\end{aligned}
$$

These stress concentration tensors will converge to the purely elastic stress concentration tensors if the viscoplastic compliance and the back-extrapolated strain rate of the inhomogeneity and matrix are set to zero. On the other hand, by setting the elastic compliance of the inhomogeneity and matrix to zero, the viscoplastic concentration tensors are retrieved. As time increment approaches zero, the stress concentration tensor $B^{e, v(r)}$ converges to the elastic limit, $B^{e(r)}$, while $b^{e, v(r)}$ converges to $\sigma^{(r) t}-B^{e(r)}: \Sigma^{t}$, so that the total stress converges to $\sigma^{(r) t}$. The concentration tensors given by Eqs. (25-26) naturally follow from the adopted additive interaction equation and are thus defined in terms of both elastic and viscoplastic properties, unlike the elastic and viscoplastic concentration tensors provided in (Mercier and Molinari, 2009; Wang et al., 2010), which are derived from completely separate elastic and viscoplastic interaction equations and are thus only functions of elastic or viscoplastic properties.

In addition to the stress concentration tensors, the stress rate concentration tensors, $\hat{B}^{e, v(r)}$ and $\hat{b}^{e, v(r)}$, can also be derived by using the following approximations for stress at the end of the time increment in the interaction equation, $\sigma^{(r) t+\Delta t}=\sigma^{(r) t}+\dot{\sigma}^{(r)} \Delta t$ and $\Sigma^{t+\Delta t}=\Sigma^{t}+\dot{\Sigma} \Delta t$. It turns out that:

$$
\hat{B}^{e, v(r)} \equiv B^{e, v(r)}, \quad(27)
$$

while $\hat{b}^{e, v(r)}$ is given by:

$$
\hat{b}^{e, v(r)}=\left[M^{e(r)}+M^{v(r)} \Delta t+\tilde{M}^{e(r)}+\tilde{M}^{v(r)} \Delta t\right]^{-1}:\left[-\tilde{M}^{v(r)}:\left(\sigma^{(r), t}-\Sigma^{t}\right)-M^{v(r)}: \sigma^{(r), t}+\right.
$$

$$
\left.M^{v}: \Sigma^{t}+\dot{E}^{v 0}-\dot{\varepsilon}^{v 0(r)}\right]. \tag{28}
$$

#### 2.1.2.3.2 Non-incremental elasto-viscoplastic interaction equation

After applying the Eshelby's equivalent inclusion method to the elasto-viscoplastic inhomogeneity, the constitutive relation in the equivalent inclusion is given by:

$$
\dot{\varepsilon}^{(r)}-\dot{\varepsilon}^{*(r)}=M^{e}: \dot{\sigma}^{(r)}+M^{v}: \sigma^{(r)}+\dot{E}^{v 0}, \tag{29}
$$

where $\dot{\varepsilon}^{*(r)}$ is the eigenstrain rate in the equivalent inclusion. By approximating the time derivatives of stress and regrouping the terms on the right hand side we get:

$$
\dot{\varepsilon}^{(r)}-\dot{\varepsilon}^{*(r)}=\left[M^{e} \frac{1}{\Delta t}+M^{v}\right]: \sigma^{(r)}-M^{e} \frac{1}{\Delta t}: \sigma^{(r), t}+\dot{E}^{v 0}. \tag{30}
$$

It is noted that the behavior of the inclusion (and matrix) is analogous to purely viscous material with the modulus given by, $M^{e} \frac{1}{\Delta t}+M^{v}$, and back-extrapolated strain rate given by $-M^{e} \frac{1}{\Delta t}: \sigma^{(r), t}+\dot{E}^{v 0}$. Similarly, as Hill utilized the incremental Eshelby solution with the elasto-plastic moduli (Hill, 1965), or as Nemat-Nasser and Obata utilized the same incremental Eshelby solution with the elasto-viscoplastic moduli (Nemat-Nasser and Obata, 1986), we use the non-incremental Eshelby's solution with the elasto-viscoplastic moduli (Lebensohn and Tomé, 1993; Molinari et al., 1987). According to Eshelby's solution, the eigenstrain rate in the equivalent inclusion is linearly related to the deviation of strain rate in the inclusion through the elasto-viscoplastic Eshelby tensor: $\dot{\varepsilon}^{*(r)}=S^{e v(r)^{-1}}:\left(\dot{\varepsilon}^{(r)}-\dot{E}\right)$, where the Eshelby tensor is a function of matrix's elasto-viscoplastic properties, $M^{e} \frac{1}{\Delta t}+M^{v}$, and the shape and orientation of the ellipsoid. Detailed derivation of the relation between the deviation in strain rate and eigenstrain rate is given in the Appendix A. By substituting the expression for eigenstrain rate into Eq. (30) and after some manipulation, following interaction equation is derived:

$$
\dot{\varepsilon}^{(r)}-\dot{E}=-\tilde{M}^{e v(r)}:\left(\sigma^{(r)}-\Sigma\right)+\frac{1}{\Delta t} \tilde{M}^{e e v(r)}:\left(\sigma^{(r), t}-\Sigma^{t}\right), \tag{31}
$$

where the interaction tensors are given by $\tilde{M}^{ev(r)}=\left(I-S^{ev(r)}\right)^{-1}: S^{ev(r)}:\left[M^{e} \frac{1}{\Delta t}+M^{v}\right]$ and
$\tilde{M}^{eev(r)}=\left(I-S^{ev(r)}\right)^{-1}: S^{ev(r)}: M^{e}$.

By setting the viscoplastic compliance and eigenstrain rate to zero, we retrieve the elastic interaction law. In addition, the viscoplastic interaction law is obtained by setting the elastic compliance to zero. After introducing an analogous approximation for derivatives in the MAK97 interaction law and after regrouping of the terms, we obtain:

$$
\dot{\varepsilon}^{(r)}-\dot{E}=-\left[\tilde{M}^{v(r)}+\frac{1}{\Delta t} \tilde{M}^{e(r)}\right]:\left(\sigma^{(r) t+\Delta t}-\Sigma^{t+\Delta t}\right)+\frac{1}{\Delta t} \tilde{M}^{e(r)}:\left(\sigma^{(r) t}-\Sigma^{t}\right). \tag{32}
$$

By comparing the two interaction laws (Eqs. (31) and (32)) we note the analogy between $\tilde{M}^{ev(r)}$ and $\tilde{M}^{v(r)}+\frac{1}{\Delta t} \tilde{M}^{e(r)}$. In addition, note the analogy between the $\tilde{M}^{eev(r)}$ and $\tilde{M}^{e(r)}$.

The elasto-viscoplastic stress concentration tensors derived from the interaction equation (Eq. 31) have similar form as the elastic or viscoplastic stress concentration tensors, with the appropriate use of elasto-viscoplastic quantities:

$$
B^{e v(r)}=\left[M^{e v,(r)}+\tilde{M}^{e v(r)}\right]^{-1}:\left[\tilde{M}^{e v(r)}+M^{e v}\right], \tag{33}
$$

$$
b^{e v(r)}=\left[M^{e v,(r)}+\tilde{M}^{e v(r)}\right]^{-1}:\left[\dot{E}^{e v 0}-\dot{\varepsilon}^{e v 0(r)}-\tilde{M}^{e e v(r)}:\left(-\sigma^{(r), t}+\Sigma^{t}\right) \frac{1}{\Delta t}\right]. \tag{34}
$$

### 2.1.3 Homogenization

After we have dealt with the single crystal constitutive response and the elasto-viscoplastic inhomogeneity problem, we can perform the homogenization of the polycrystal and derive the expressions for the effective properties. Three different homogenization procedures are considered: 1) Self-consistent homogenization based on MAK97 interaction law (SC-MAK97), 2) Mori-Tanaka homogenization based on MAK97 interaction law (MT-MAK97), and 3) Self-consistent homogenization based on non-incremental elasto-viscoplastic interaction equation (SC-EVPNI). These three alternative homogenization schemes are explained in what follows. The expressions for effective properties and the interaction and localization equations for each proposed method and for the EVPSC homogenization of Wang et al. (2010) are summarized in Fig. 1.

#### 2.1.3.1 Self-consistent homogenization based on MAK97 interaction law (SC-MAK97)

We adopt the MAK97 interaction law. The effective properties of the composite are derived from the equivalence of volume average of local strain rate and macroscopic strain rate, $\sum_{r} c^{(r)} \dot{\varepsilon}^{(r)}=\dot{E}$, where $c^{(r)}$ is the volume fraction of grain $r$. For the case in which all the ellipsoidal grains have the same shape and orientation, this also ensures the equivalence of volume averages of local stresses and stress rates with the corresponding macroscopic quantities. First, the elastic portion of the strain rate is considered: $\sum_{r} c^{(r)} \dot{\varepsilon}^{e(r)}=\dot{E}^{e}$ from where elastic effective properties are obtained:

$$
\bar{M}^{e}=\sum_{r} c^{(r)} M^{e(r)}: \hat{B}^{e, v(r)},
$$

$$
\bar{E}^{e 0}=\sum_{r} c^{(r)} M^{e(r)}: \hat{b}^{e, v(r)},
$$

where the stress rate concentration tensors are given by Eqs. (27) and (28). Second, from the equivalence $\sum_{r} c^{(r)} \dot{\varepsilon}^{v(r)}=\dot{E}^{v}$ viscoplastic effective properties are derived:

$$
\bar{M}^{v}=\sum_{r} c^{(r)} M^{v(r)}: B^{e, v(r)},
$$

$$
\bar{E}^{v 0}=\sum_{r} c^{(r)} M^{v(r)}: b^{e, v(r)}+\sum_{r} c^{(r)} \dot{\varepsilon}^{v 0(r)},
$$

where the stress concentration tensors are given by Eqs. (25) and (26). The derived elastic and viscoplastic effective properties represent properties of the homogeneous elasto-viscoplastic medium that has constitutive behavior equivalent to the averaged behavior of the actual heterogeneous composite. The presence of an additional term in the grain constitutive relation, arising from rigid rotation of the grain, results in an additional contribution to total effective properties:

$$
\bar{M}^{e w}=\sum_{r} c^{(r)} M^{e w(r)}: B^{e, v(r)},
$$

$$
\bar{E}^{e w 0}=\sum_{r} c^{(r)} M^{e w(r)}: b^{e, v(r)}.
$$

The expression for the total macroscopic strain rate is then:

$$
\dot{E}=\dot{E}^{e}+\dot{E}^{v}+\dot{E}^{e w}=\bar{M}^{e}: \dot{\Sigma}+\bar{E}^{e 0}+\bar{M}^{v}: \Sigma+\bar{E}^{v 0}+\bar{M}^{e w}: \Sigma+\bar{E}^{e w 0}.
$$

The defined effective properties are functions of the local grain properties and the matrix properties. In the self-consistent method, the matrix properties are enforced to be the effective

properties. We adopt the self-consistent homogenization and thus the stress concentration tensors given by Eqs. (25-28) become functions of the above derived effective properties since the matrix properties, $M^{v}$, $\dot{E}^{v}$ and $M^{e}$, are replaced by the corresponding effective properties given by Eqs. (35-38). In addition, the moduli $M^{e w(r)}$, $\bar{\dot{E}}^{e w 0}$, $\bar{M}^{e w}$ and $\bar{\dot{E}}^{e 0}$ need to be added next to the corresponding viscoplastic quantities in the expressions for stress concentration tensors (25-26). Consequently, expressions for the effective properties become implicit equations, which are solved iteratively using a fixed-point method (Fig. 1).

It is noted that the derived expressions for the effective properties are fundamentally different from those provided by Mercier and Molinari (2009); Wang et al. (2010), due to the difference in concentration tensors (Fig. 1). The inconsistency of the approach of Wang et al. (2010) is due to the fact that the grain stress is calculated from the MAK97 interaction equation (Eq. (24)), while the concentration tensors used for definition of effective properties come from purely elastic and visco-plastic interaction equations (Eqs. (15) and (20-21)) (Fig. 1). Therefore, the concentration tensors used for calculation of effective properties will not give the correct grain stress when applied to the macroscopic stress. Furthermore, the elastic and viscoplastic stress concentration tensors will result in two different (i.e. inconsistent) stress values. Consequently, the convergence of the method is slow as was noted by Jeong and Tomé (2019) and the condition $\sum_{r} c^{(r)} \dot{\varepsilon}^{(r)}=\dot{E}$ is difficult to achieve.

#### 2.1.3.2 Mori-Tanaka homogenization based on MAK97 interaction law (MT-MAK97)

In the previous section, self-consistency was enforced by requiring the equivalence of the properties of the matrix and the effective properties (Fig. 1). Here, we assume that the properties of the matrix are *not* equal to the effective properties of the aggregate. Consequently, first we need to approximate the matrix properties.

![](./images/812597125853478914_2.jpg)

Figure 1: Comparison between approximations, main equations and algorithms of the EVPSC formulation of Wang et al. (2010) and the 3 newly proposed homogenization methods for elasto-viscoplastic polycrystals: SC-MAK97, MT-MAK97 and SC-EVPNI. Expressions for the different interaction tensors $\tilde{M}^{e(r)}$, $\tilde{M}^{v(r)}$,$\tilde{M}^{ev(r)}$ and $\tilde{M}^{eev(r)}$ are given in the text.

Following the approach developed by Mercier and Molinari (2009), we assume that the elastic and viscoplastic properties of the matrix are completely independent of each other and can thus be decoupled. The elastic properties of the matrix are approximated by self-consistent homogenization of the purely elastic aggregate:

$$
M^{e}=\sum_{r} c^{(r)} M^{e(r)}: \hat{B}^{e(r)}, \tag{42}
$$

where the elastic stress rate concentration tensor is given by Eq. (15). The viscoplastic properties of the matrix are approximated by self-consistent homogenization of the purely viscoplastic aggregate:

$$
M^{v}=\sum_{r} c^{(r)} M^{v(r)}: B^{v(r)}, \tag{43}
$$

$$
\dot{E}^{v 0}=\sum_{r} c^{(r)} M^{v(r)}: b^{v(r)}+\sum_{r} c^{(r)} \dot{\varepsilon}^{v 0(r)}, \tag{44}
$$

where the viscoplastic stress concentration tensors are given by Eqs. (20-21). Thus, we have obtained the elastic and viscoplastic properties of the matrix. Next, each grain is assumed to be an inhomogeneity within the matrix, which has the calculated elastic and viscoplastic properties (Fig. 1). MAK97 interaction law is adopted and the stress concentration tensors can be calculated using the Eqs. (25-28), where for the matrix properties we use Eqs. (42-44). The presence of an additional term in the grain constitutive relation (Eq. (7)), arising from rigid rotation of the grain, results in an additional term $M^{e w(r)}$ added next to the $M^{v(r)}$ in concentration Eqs. (25-28). The elastic and viscoplastic effective properties of the composite are then derived from the equivalence of volume average of local strain rate and macroscopic strain rate and are formally the same as Eqs. (35-40) (Fig. 1). In the second part of the procedure, the properties of the matrix are known a priori and thus the final homogenization is of the Mori-Tanaka type, with no contribution of the matrix itself to volumetric averages (Benveniste, 1987; Mori and Tanaka, 1973). The proposed Mori-Tanaka method bears more resemblance to the EVPSC method of Wang et al. (2010), and to the self-consistent method of Mercier and Molinari (2009), than the SC-MAK97 method proposed in the previous section. However, the primary difference in comparison to Mercier and Molinari (2009) and Wang et al. (2010) lies in recognizing that the properties obtained by the separate ELSC and VPSC methods are *not* the effective properties for the elasto-viscoplastic problem, and in the derivation of the effective properties consistent with the adopted interaction equation. This was not the case in Mercier and Molinari (2009) and

Wang et al. (2010), where calculated SC elastic and viscoplastic properties were adopted as effective properties of the elasto-viscoplastic homogeneous medium. The Mori-Tanaka method proposed by Mercier and Molinari (2009) is not directly applicable to polycrystals and the effective properties would be calculated using the inconsistent concentration tensors.

#### 2.1.3.3 Self-consistent homogenization based on non-incremental elasto-viscoplastic interaction equation (SC-EVPNI)

We adopt the proposed non-incremental elasto-viscoplastic interaction law. By considering the equivalence of volume average of local strain rate and macroscopic strain rate, the following effective properties are obtained:

$$
\bar{M}^{e v}=\sum_{r} c^{(r)} M^{e v(r)}: B^{e v(r)}, \tag{45}
$$

$$
\bar{\dot{E}}^{e v 0}=\sum_{r} c^{(r)} M^{e v(r)}: b^{e v(r)}+\sum_{r} c^{(r)} \dot{\varepsilon}^{e v 0(r)}, \tag{46}
$$

where the stress concentration tensors are given by Eqs. (33-34) and the elasto-viscoplastic moduli are given by Eqs. (10-11). In addition to the elasto-viscoplastic effective properties, we also need the elastic effective compliance:

$$
\bar{M}^{e}=\sum_{r} c^{(r)} M^{e(r)}: B^{e v(r)}. \tag{47}
$$

Since we adopt the self-consistent homogenization, the matrix is forced to have the effective properties $(M^{e v}=\bar{M}^{e v}, \dot{E}^{e v 0}=\bar{\dot{E}}^{e v 0}$ and $M^{e}=\bar{M}^{e})$. The stress concentration tensors (Eqs. (33-34)) are thus functions of the effective properties, and the expressions for effective properties become implicit and have to be solved iteratively. As before, we use the fixed-point method to solve for the effective properties (Fig. 1).

### 2.2 Non-linear elasto-viscoplastic behavior

The previously derived homogenization schemes assume that each grain has linear elastic and viscoplastic behaviors. Single crystalline grains of metallic materials deform by dislocation glide on the available slip systems. Constitutive behavior of a single crystalline grain can be described by the viscoplastic power law:

$$
\dot{\varepsilon}^{v(r)}=\dot{\gamma}_{0} \sum_{s}\left(\frac{\left|\sigma^{(r)}: m^{s(r)}\right|}{\tau_{c}^{s(r)}}\right)^{n} \operatorname{sign}\left(\sigma^{(r)}: m^{s(r)}\right) m^{s(r)}, \tag{48}
$$

where $\dot{\gamma}_{0}$ is reference shear rate, $\tau_{c}^{s(r)}$ is resistance to slip of slip system $s$ and $n$ is the inverse of rate sensitivity. $m^{s(r)}=\frac{1}{2}\left(n^{s} \otimes b^{s}+b^{s} \otimes n^{s}\right)$ is the symmetric Schmid tensor of slip system $s$, where $n^{s}$ and $b^{s}$ are slip plane normal and slip direction of slip system $s$. The rate exponent $n$ is usually set to $n=10-100$ for metallic materials, resulting in highly non-linear viscoplastic behavior of the grains.

Both the self-consistent and Mori-Tanaka homogenization procedures are based on the Eshelby solution of the linear inhomogeneity embedded within a linear matrix. Therefore, in order to use the linear homogenization procedures for the non-linear composite, the non-linear viscoplastic response first has to be linearized. In what follows, we adopt the affine linearization procedure with the expressions for the viscoplastic compliance and back-extrapolated strain rate given by Masson et al. (2000), although other linearization schemes can be adopted (see Lebensohn et al., 2007):

$$
M^{v(r)}=n \dot{\gamma}_{0} \sum_{s}\left(\frac{\left|\sigma^{(r)}: m^{s(r)}\right|}{\tau_{c}^{s(r)}}\right)^{n-1} \frac{1}{\tau_{c}^{s(r)}} m^{s(r)} \otimes m^{s(r)},
\tag{49}
$$

$$
\dot{\varepsilon}^{v 0(r)}=(1-n) \dot{\gamma}_{0} \sum_{s}\left(\frac{\left|\sigma^{(r)}: m^{s(r)}\right|}{\tau_{c}^{s(r)}}\right)^{n} \operatorname{sign}\left(\sigma^{(r)}: m^{s(r)}\right) m^{s(r)}.
\tag{50}
$$

Therefore, by linearizing the local grain behavior, we can apply the linear homogenization procedures.

Due to the non-linearity of the problem, an additional iteration loop over local grain stresses is required (Lebensohn and Tomé, 1993; Lebensohn et al., 2007). First, starting with an initial guess for grain stresses, linearization of the grain's viscoplastic response is performed and moduli $M^{v(r)}$ and $\dot{\varepsilon}^{v 0(r)}$ are obtained. Next, we can utilize any of the developed homogenization procedures, obtain the effective behavior, and stress concentration tensors. The grain stresses coming from the homogenization procedure will not match with the initial guess for grain stresses, which was used for the linearization. Consequently, new guess for grain stresses is calculated, linearization is performed around this new guess and the homogenization is performed again. The iterative procedure continues until the grain stresses coming from homogenization match the grain stresses used for the linearization. The numerical procedure closely follows Lebensohn and Tomé (1993).

### 2.3 Second order moments of stress and strain rate within grains

We have calculated the second moments of stress and strain rate within the grains for the MT- MAK97, and for the SC-EVPNI methods. For the MT-MAK97, we have used two separate elastic and viscoplastic potentials in the derivation of expressions for second moments (Michel and Suquet, 2017). On the other hand, for the SC-EVPNI homogenization we have used one elasto-viscoplastic potential (Agoras et al., 2016). We conclude that the MT-MAK97 method produces physically correct results. On the other hand, the SC-EVPNI shows an unreasonable dependence of intragranular fluctuations on the time increment. Considering the similarities between the two proposed self-consistent methods, we conclude that it is likely that the SC- MAK97 will display similar behavior.

### 2.3.1 Calculation of second moments of stress from separate elastic and viscoplastic potentials

When dealing with purely elastic or viscoplastic behavior, the constitutive equations may be derived from purely elastic or viscoplastic potentials. However, for the case of combined elasto- viscoplastic deformation, two potentials are defined (Michel and Suquet, 2017). We define elastic and viscoplastic strain rate potentials for a grain as (Laws, 1973):

$$
w^{v(r)}=\frac{1}{2} \dot{\varepsilon}^{v}: L^{v(r)}: \dot{\varepsilon}^{v}+\dot{\varepsilon}^{v}: \sigma^{v 0(r)},\tag{51}
$$

$$
w^{e(r)}=\frac{1}{2} \dot{\varepsilon}^{e}: L^{e(r)}: \dot{\varepsilon}^{e}.\tag{52}
$$

The effective strain rate potentials are given by (Laws, 1973):

$$
W^{v}=\frac{1}{2} \dot{E}^{v}: \bar{L}^{v}: \dot{E}^{v}+\dot{E}^{v}: \bar{\Sigma}^{v 0}+\frac{1}{2} \sum_{r} c^{(r)} a^{v(r)}: \sigma^{v 0(r)},\tag{53}
$$

$$
W^{e}=\frac{1}{2} \dot{E}^{e}: \bar{L}^{e}: \dot{E}^{e},\tag{54}
$$

where $a^{v(r)}$ is the viscoplastic strain rate concentration tensor and $\sigma^{v 0(r)}=-L^{v(r)}: \dot{\varepsilon}^{v 0(r)}$. The second moments of elastic and viscoplastic strain rate are then:

$$
\left\langle\dot{\varepsilon}^{v} \otimes \dot{\varepsilon}^{v}\right\rangle^{(r)}=\frac{2}{c^{(r)}} \frac{\partial W^{v}}{\partial L^{v(r)}},\tag{55}
$$

$$
\left\langle\dot{\varepsilon}^{e} \otimes \dot{\varepsilon}^{e}\right\rangle^{(r)}=\frac{2}{c^{(r)}} \frac{\partial W^{e}}{\partial L^{e(r)}}.\tag{56}
$$


Considering the equivalence of the dual stress potential approach, the second moment of
viscoplastic strain rate is given by: $\langle\dot{\varepsilon}^{v} \otimes \dot{\varepsilon}^{v}\rangle^{(r)}=\frac{1}{c^{(r)}} M^{v(r)}:\left[(\Sigma \otimes \Sigma):: \frac{\partial \bar{M}^{v}}{\partial M^{v(r)}}\right]: M^{v(r)^{T}}+$
$\frac{2}{c^{(r)}} M^{v(r)}:\left[\Sigma: \frac{\partial \bar{E}^{v 0}}{\partial M^{v(r)}}\right]: M^{v(r)^{T}}+\frac{1}{c^{(r)}} M^{v(r)}:\left[\sum_{r} c^{(r)} \dot{\varepsilon}^{v 0(r)}: \frac{\partial b^{v(r)}}{\partial M^{v(r)}}\right]: M^{v(r)^{T}}+\dot{\varepsilon}^{v(r)} \otimes \dot{\varepsilon}^{v 0(r)}+$
$\dot{\varepsilon}^{v 0(r)} \otimes \dot{\varepsilon}^{v(r)}-\dot{\varepsilon}^{v 0(r)} \otimes \dot{\varepsilon}^{v 0(r)}$, where the derivatives of the effective properties can be found in
Lebensohn et al. (2007). Similar expression holds for second moment of elastic strain rate. The
centered second moments of viscoplastic and elastic strain rate are given by:

$$
\begin{aligned}
&\left\langle\delta \dot{\varepsilon}^{v} \otimes \delta \dot{\varepsilon}^{v}\right\rangle^{(r)}=\frac{2}{c^{(r)}} \frac{\partial W^{v}}{\partial L^{v(r)}}-\left(A^{v(r)}: \dot{E}^{v}\right) \otimes\left(A^{v(r)}: \dot{E}^{v}\right)-a^{v(r)} \otimes a^{v(r)}-\left(A^{(r)}: \dot{E}^{v}\right) \otimes a^{v(r)}- \\
&a^{v(r)} \otimes\left(A^{v(r)}: \dot{E}^{v}\right),
\end{aligned}
$$

$$
\left\langle\delta \dot{\varepsilon}^{e} \otimes \delta \dot{\varepsilon}^{e}\right\rangle^{(r)}=\frac{2}{c^{(r)}} \frac{\partial W^{e}}{\partial L^{e(r)}}-\left(A^{e(r)}: \dot{E}^{e}\right) \otimes\left(A^{e(r)}: \dot{E}^{e}\right),
$$

where $A^{v(r)}$ and $A^{e(r)}$ are viscoplastic and elastic strain rate concentration tensors. The elastic
and viscoplastic strain rate concentration tensors can be derived from the corresponding
interaction equations and are given by:

$$
A^{e(r)}=\left[L^{e(r)}+\tilde{L}^{e(r)}\right]^{-1}:\left[\tilde{L}^{e(r)}+\bar{L}^{e}\right],
$$

$$
A^{v(r)}=\left[L^{v(r)}+\tilde{L}^{v(r)}\right]^{-1}:\left[\tilde{L}^{v(r)}+\bar{L}^{v}\right],
$$

$$
a^{v(r)}=\left[L^{v(r)}+\tilde{L}^{v(r)}\right]^{-1}:\left[\Sigma^{v 0}-\sigma^{v 0(r)}\right],
$$

where $\Sigma^{v 0}=-\bar{L}^{v}: \dot{E}^{v 0}$. The effective properties and concentration tensors in the above
expressions will depend on the adopted homogenization approach. In previous work, a dual
stress potential formulation was used to derive the second moments of stress (Lebensohn et al.,
2007). However, for the case of combined elastic and viscoplastic deformation this leads to two
different estimates for second moment of stress, one coming from the elastic stress potential and
the other from the viscoplastic stress potential. Consequently, we have chosen to evaluate the
second moments of elastic and viscoplastic strain rate, which are two independent variables,
separately, and then calculate the consistent second moment of stress from the total second
moment of strain rate.

For the MT-MAK97, we adopt the following approach. It is assumed that the fluctuations of viscoplastic strain rate depend only on the viscoplastic properties. Therefore, in the expression for the centered second moments of viscoplastic strain rate (Eq. (57)), the self-consistent estimates of the macroscopic viscoplastic compliance and eigenstrain rate given by Eqs. (43-44) are used along with the purely viscoplastic strain rate concentration tensors. Similarly, we assume that the fluctuations of elastic strain rate (Eq. (58)) are defined only by elastic properties and thus we use the self-consistent estimate of macroscopic elastic compliance given by Eq. (42) and the purely elastic strain rate concentration tensors. Next, the centered second moment of total strain rate within the grain is calculated as:

$$
\langle\delta \dot{\varepsilon} \otimes \delta \dot{\varepsilon}\rangle^{(r)} \approx\left\langle\delta \dot{\varepsilon}^{v} \otimes \delta \dot{\varepsilon}^{v}\right\rangle^{(r)}+\left\langle\delta \dot{\varepsilon}^{e} \otimes \delta \dot{\varepsilon}^{e}\right\rangle^{(r)},
\tag{62}
$$

where we have neglected the cross-covariance terms $\langle\delta \dot{\varepsilon}^{v} \otimes \delta \dot{\varepsilon}^{e}\rangle^{(r)}$ and $\langle\delta \dot{\varepsilon}^{e} \otimes \delta \dot{\varepsilon}^{v}\rangle^{(r)}$.

Once the centered second moment of total strain rate is obtained, the consistent second moment of stress can be calculated as follows. The fluctuation of total strain rate from the mean grain value is related to fluctuation of stress and stress rate by: $\delta \dot{\varepsilon}=M^{v(r)}: \delta \sigma^{t+\Delta t}+M^{e(r)}: \delta \dot{\sigma}$. By substituting this expression into the expression for centered second moment of strain rate (Eq. (62)) and using backward Euler approximation for stress rate deviation, $\delta \dot{\sigma}=\frac{\delta \sigma^{t+\Delta t}-\delta \sigma^{t}}{\Delta t}$, following expression is derived:

$$
\begin{aligned}
&\langle\delta \dot{\varepsilon} \otimes \delta \dot{\varepsilon}\rangle^{(r)}=M^{v(r)}:\left\langle\delta \sigma^{t+\Delta t} \otimes \delta \sigma^{t+\Delta t}\right\rangle^{(r)}: M^{v(r)^{T}}+M^{e(r)}:\left[\left\langle\delta \sigma^{t+\Delta t} \otimes \delta \sigma^{t+\Delta t}\right\rangle^{(r)}+\right. \\
&\left.\left\langle\delta \sigma^{t} \otimes \delta \sigma^{t}\right\rangle^{(r)}-\left\langle\delta \sigma^{t+\Delta t} \otimes \delta \sigma^{t}\right\rangle^{(r)}-\left\langle\delta \sigma^{t} \otimes \delta \sigma^{t+\Delta t}\right\rangle^{(r)}\right]: M^{e(r)^{T}} \frac{1}{\Delta t^{2}}+ \\
&M^{v(r)}:\left[\left\langle\delta \sigma^{t+\Delta t} \otimes \delta \sigma^{t+\Delta t}\right\rangle^{(r)}-\left\langle\delta \sigma^{t+\Delta t} \otimes \delta \sigma^{t}\right\rangle^{(r)}\right]: M^{e(r)^{T}} \frac{1}{\Delta t}+ \\
&M^{e(r)}:\left[\left\langle\delta \sigma^{t+\Delta t} \otimes \delta \sigma^{t+\Delta t}\right\rangle^{(r)}-\left\langle\delta \sigma^{t} \otimes \delta \sigma^{t+\Delta t}\right\rangle^{(r)}\right]: M^{v(r)^{T}} \frac{1}{\Delta t},
\end{aligned}
\tag{63}
$$

where the transposition of fourth order tensors is defined as: $\left(M_{i j k l}\right)^{T}=M_{k l i j}$. In the above expression, the centered second moment of stress $\langle\delta \sigma^{t+\Delta t} \otimes \delta \sigma^{t+\Delta t}\rangle^{(r)}$ and the cross-covariance term $\langle\delta \sigma^{t+\Delta t} \otimes \delta \sigma^{t}\rangle^{(r)}$ are the only unknowns. In order to solve the problem, we introduce additional assumptions and write the two unknowns in terms of one unknown. For this let us assume that all the symmetric second-order tensors are represented as vectors while the symmetric fourth-order tensors are represented as matrices. There exists a linear mapping, $X$,

which maps the centered second moment of stress from time $t$ to the centered second moment of stress at time $t+\Delta t$:

$$
\langle\delta \sigma^{t+\Delta t} \otimes \delta \sigma^{t+\Delta t}\rangle^{(r)}=X \cdot\langle\delta \sigma^{t} \otimes \delta \sigma^{t}\rangle^{(r)} \cdot X^{T}. \tag{64}
$$

This statement is exact, since we can always solve 21 independent equations defined by Eq. (64) for 21 independent components of symmetric matrix $X$. We then further *assume* that the mapping holds pointwise:

$$
\langle\delta \sigma^{t+\Delta t} \otimes \delta \sigma^{t+\Delta t}\rangle^{(r)}=\langle\left(X \cdot \delta \sigma^{t}\right) \otimes\left(X \cdot \delta \sigma^{t}\right)\rangle^{(r)} \rightarrow \delta \sigma^{t+\Delta t}=X \cdot \delta \sigma^{t}. \tag{65}
$$

Therefore, it is assumed that each point in the distribution $\langle\delta \sigma^{t+\Delta t} \otimes \delta \sigma^{t+\Delta t}\rangle^{(r)}$ is obtained by mapping of the corresponding point from distribution $\langle\delta \sigma^{t} \otimes \delta \sigma^{t}\rangle^{(r)}$, with the map defined by $X$. The cross-covariance is then: $\langle\delta \sigma^{t+\Delta t} \otimes \delta \sigma^{t}\rangle^{(r)}=X \cdot\langle\delta \sigma^{t} \otimes \delta \sigma^{t}\rangle^{(r)}$. The adopted assumption implies strongest possible correlation between intragranular stress deviations from two consecutive time increments. This is fairly reasonable, since a material point which deviated from the mean in a certain way is expected to behave similarly in the next time increment.

The introduced assumption is actually not an approximation in the elastic region, but it is exact due to linearity of the elastic problem. In the viscoplastic limit (assuming no texture or hardening evolution), the assumption is again exact since the stress distribution does not change and we have $X_{i j}=\delta_{i j}$. On the other hand, for the combined elastic and viscoplastic deformation with evolution of texture and hardening, this is an approximation. By substituting $\delta \sigma^{t+\Delta t}=X \cdot \delta \sigma^{t}$ into Eq. (63), the only unknown becomes $X$ and the equation can be solved for it.

In the case of MT-MAK97 interaction equation, the viscoplastic and elastic properties of the matrix obtained by separate self-consistent homogenization schemes will be independent of the time increment, because both the purely elastic and viscoplastic stress concentration (Eqs. (15, 20-21)) are independent of the time increment. Consequently, there will be no unphysical dependence of the centered second moments of strain rate and stress on the time increment. Detailed discussion of time increment dependence is given in section 3.2.

### 2.3.2 Calculation of second moment of stress using one elasto-viscoplastic potential

By comparing the expressions for the effective properties of the SC-EVPNI homogenization (Eqs. (45-46)) and for the effective properties of purely viscoplastic self-consistent

homogenization (Eqs. (43-44)), we note that the expressions are formally the same. The difference is in the use of the elasto-viscoplastic compliance and back-extrapolated strain rate instead of the viscoplastic ones. Same is true for the stress concentration tensors (Eqs. (20-21)) and (33-34)), with one minor difference in the expression for $b^{ev(r)}$. Therefore, by analogy, we assume that the stress potential, $u^{ev(r)}$, governing the behavior of elasto-viscoplastic polycrystal has the same form as viscoplastic potential (Lebensohn et al., 2007):

$$
u^{e v(r)}=\frac{1}{2} \sigma: M^{e v(r)}: \sigma+\dot{\varepsilon}^{e v 0(r)}: \sigma,
\tag{66}
$$

where we have used the corresponding elasto-viscoplastic properties instead of the viscoplastic ones. By replacing the expressions for $M^{e v(r)}$ and $\dot{\varepsilon}^{e v 0(r)}$ given by Eqs. (10-11) into Eq. (66) and after rearranging we get:

$$
u^{e v(r)}=\frac{1}{2} \sigma: M^{v(r)}: \sigma+\dot{\varepsilon}^{v 0(r)}: \sigma+\frac{1}{2} \sigma: M^{e(r)}: \sigma \frac{1}{\Delta t}-\frac{1}{\Delta t}\left(M^{e(r)}: \sigma^{(r), t}\right): \sigma=u^{v(r)}+u^{e(r)},(67)
$$

where we have assumed $M^{e w(r)} \approx 0$, and $u^{v(r)}=\frac{1}{2} \sigma: M^{v(r)}: \sigma+\dot{\varepsilon}^{v 0(r)}: \sigma$ and $u^{e(r)}=$ $\frac{1}{2} \sigma: M^{e(r)}: \sigma \frac{1}{\Delta t}-\frac{1}{\Delta t}\left(M^{e(r)}: \sigma^{(r), t}\right): \sigma$. Therefore, the defined elasto-viscoplastic potential is a sum of purely elastic and viscoplastic stress potentials. The same expression for the stress potential was proposed by Agoras et al. (2016).

The expression for effective stress potential is given by:

$$
U^{e v}=\frac{1}{2} \Sigma: \bar{M}^{e v}: \Sigma+\bar{\dot{E}}^{e v 0}: \Sigma+\frac{1}{2} \sum_{r} c^{(r)} b^{e v(r)}: \dot{\varepsilon}^{e v 0(r)}.
\tag{68}
$$

Second moment of stress is then:

$$
\langle\sigma \otimes \sigma\rangle^{(r)}=\frac{2}{c^{(r)}} \frac{\partial U^{e v}}{\partial M^{e v(r)}}.
\tag{69}
$$

The derivatives of the effective potential, (Eq. (68)), turn out to be very dependent on the time increment, and as a result the calculated fluctuations of stress are also dependent on the time increment. The observed unphysical behavior is caused by the time increment dependence of the expressions for grain moduli (Eqs. (10-11)), stress concentration tensors (Eqs. (33-34)) and effective properties (Eqs. (45-46)), which will be analyzed in detail in section 3.2. We conclude


that the proposed self-consistent should not be used for the calculation of second order moments of strain rate or stress within the grains in combination with the approach outlined above.

## 3 Results and discussion

### 3.1 Interaction law verification

We simulate tension of a matrix with a spherical inhomogeneous domain using the two proposed interaction laws, i.e. MAK97's interaction law (section 2.1.2.3.1) and the newly proposed non-incremental elasto-viscoplastic interaction law (section 2.1.2.3.2). Both matrix and inhomogeneity are assumed to be copper single crystals with different random crystallographic orientations with the Bunge Euler angles given by: $g_m = [102.74^\circ, 119.56^\circ, 33.65^\circ]$ and $g_{inh} = [219.06^\circ, 36.21^\circ, 70.51^\circ]$, respectively. Single crystal elastic constants are $C_{11}=168.4\ GPa$, $C_{12}=121.4\ GPa$ and $C_{44}=75.4\ GPa$. Both matrix and inhomogeneity are assumed to deform by {111}<110> plastic slip with rate exponent $n=1$. Consequently, viscoplastic behavior is linear with compliance defined as $M^{v(r)}=\dot{\gamma}_0\sum_{s}\frac{1}{\tau_{c}^{s(r)}}m^{s(r)}\otimes m^{s(r)}$. We have chosen linear viscoplastic behavior because both interaction equations were derived under assumption of linear behavior of matrix and inhomogeneity. For the case of non-linear behavior, both interaction equations are only approximations. Tension at strain rate of 1.0 /s is applied to the matrix in direction $x_3$. Slip resistance of the matrix is set to $\tau_m=9.0\ MPa$, while three cases are considered for the slip resistance of the inhomogeneity: hard inclusion ($\tau_{inh}=10.0\tau_m$); soft inclusion ($\tau_{inh}=0.1\tau_m$); inclusion and matrix of the same strength ($\tau_{inh}=\tau_m$). Crystallographic orientation and the shape of the sphere are not updated.

![](./images/812597125853478914_3.jpg)

Figure 2: Stress-strain response of a spherical inhomogeneity embedded within a matrix under tension, predicted by the MAK97 interaction law, elasto-viscoplastic interaction law and the EVPFFT model. Both matrix and inhomogeneity are copper single crystals of different crystallographic orientation with linear viscoplastic behavior. Three different contrasts of slip resistance are considered.

Fig. 2 shows the predicted evolution with strain of the equivalent stress within the inhomogeneity, for each case. For each one of the considered cases, both interaction laws predict relatively similar stress state in the inhomogeneity. For the case with the hard inclusion, the elasto-viscoplastic interaction law predicts a slightly softer response in comparison to MAK97 interaction law. For reference, the mean stress in the inhomogeneity predicted by the elasto- viscoplastic FFT model (EVPFFT) (Lebensohn et al., 2012) is plotted for the small contrast case ($\tau_{inh} = \tau_{m}$). Large contrast between matrix and inhomogeneity in EVPFFT leads to convergence problems and spurious oscillations of the fields, and thus high contrast cases were not simulated using the full-field approach. A grid of $64^3$ voxels was used with the spherical inhomogeneity of radius of ~8 voxels placed in the center of unit cell, resulting in the inhomogeneity volume fraction of 0.0054 (Anglin et al., 2014). According to Anglin et al. (2014), further refinement of the grid would not affect the average values in the inhomogeneity. Both interaction laws are in good agreement with the EVPFFT predictions. In summary, similar predictions of the two interaction laws imply that the following relation between interaction tensors approximately

holds: $\tilde{M}^{e v(r), t+\Delta t} \approx \tilde{M}^{v(r)}+\frac{1}{\Delta t} \tilde{M}^{e(r)}$ and $\tilde{M}^{e(r)} \approx \tilde{M}^{e e v(r)}$. We note that Mercier et al. (2005) have thoroughly verified the MAK97 interaction law for variety of different cases. Among other tests, it was shown that the MAK97 interaction law accurately reproduces analytical solution of Hashin (1969) for a spherical inhomogeneity within an infinite matrix with linear incompressible isotropic viscoelastic constitutive behavior. In Appendix B, we show that the proposed non-incremental elasto-viscoplastic interaction law also reproduces the correct analytical solution in this simple case.

### 3.2 Compression of copper
We simulate compression of a copper polycrystal consisting of 500 spherical grains with random crystal lattice orientation, which deform by {111}<110> slip with the rate exponent $n=10$ and slip resistance $\tau_{0}=10.0 MPa$. The random crystallographic orientations are generated by randomly sampling three numbers $r_{i}$ in range 0 to 1, which are then transformed to Euler angles: $\varphi_{1}=2 \pi r_{1}, \phi=\arccos (2 r_{2}-1), \varphi_{2}=2 \pi r_{3}$ (Morawiec, 2004). The copper single crystal elastic constants are $C_{11}=170.2 GPa, \ C_{12}=114.9 GPa$ and $C_{44}=61.0 GPa$. The representative volume element is subjected to compression to true strain 0.003 in the direction $x_{3}$, with the applied strain rate of $\dot{\varepsilon}_{33}=-1.0 s^{-1}$. Stress free boundary conditions are applied in the lateral directions ($x_{1}$ and $x_{2}$), while the shear strain rate is forced to zero. Applied strain increment in the direction $x_{3}$ is $\Delta \varepsilon_{33}=-0.0001$. Small strain is considered, because different treatments of elasticity will have the largest effect in the elasto-plastic transition. Evolution of texture at large strains will not be affected by treatment of elasticity.

![](./images/812597125853478914_4.jpg)

Figure 3: Stress-strain response of copper polycrystal with random texture and spherical grains, predicted by SC-MAK97, MT-MAK97, SC-EVPNI and EVPSC model of Wang et al. (2010) for

rate exponents 10 and 50. ELSC and VPSC limits, and rigid-viscoplastic Taylor upper bound and Sachs lower bound are plotted as well.

Figure 3 compares the elastic and viscoplastic limits for the three proposed homogenization schemes with the elastic self-consistent (ELSC) and viscoplastic self-consistent (VPSC) results (Lebensohn et al., 2012). For reference, rigid-viscoplastic Taylor upper bound and Sachs lower bound predictions are included as well. Each one of the proposed homogenization schemes matches well with the elastic limit in the elastic region. In the plastic region, both SC-MAK97and SC-EVPNI result in a softer response than the viscoplastic limit. Similar trend was observed for the elasto-viscoplastic FFT model when compared to the viscoplastic FFT limit, though to lesser extent (Lebensohn et al., 2012). In the viscoplastic limit, the macroscopic stress rate is zero, meaning that the macroscopic elastic strain rate is zero as well. Consequently, the stress is determined by the viscoplastic effective properties, which appear to lead to softer response when elasticity is present and accounted for through the elasto-viscoplastic stress concentration tensors in the expressions for effective properties. In the MT-MAK97 result, this is not the case. The cause of the observed behavior is the complete decoupling of elasticity and viscoplasticity in the determination of the matrix properties. The MT-MAK97 effective viscoplastic properties result in the constitutive response only slightly softer than the response obtained by the VPSC (which cannot be observed on the Fig. 3). If these effective properties would next be assigned to the matrix as is the case in the self-consistent method, the effective behavior would become even softer and would converge to the SC-MAK97 case. Moreover, the effect of stress rotation on the results is practically negligible, and the macroscopic stress-strain curves are practically indistinguishable from the ones presented on Fig. 3 if $M^{ew(r)} = 0$. This is due to small magnitude of stress rate caused by rotation in comparison to the stress rate caused by straining, and due to randomness of the microstructure, which implies random local rotations. The EVPSC model of Wang et al. (2010) shows a bit sharper elastoplastic transition, and quickly converges to viscoplastic limit in the plastic region. It is also noted that the EVPSC model predicts stress higher than the viscoplastic limit, right after the elastoplastic transition. In addition, we note convergence difficulties in our implementation of the EVPSC model. With the increase of rate exponent $n$ the differences between the homogenization schemes increase because even small difference in grain stress state may lead to activation of different set of slip systems and thus different linearized viscoplastic compliance which in turn amplifies the effect.

![](./images/812597125853478914_5.jpg)

Figure 4: Evolution of transverse to longitudinal strain ratio with equivalent strain predicted by SC-MAK97, MT-MAK97, SC-EVPNI and EVPSC model of Wang et al. (2010)

![](./images/812597125853478914_6.jpg)

Figure 5: Effect of strain increment on the predicted stress-strain response of copper polycrystal for SC-MAK97, MT-MAK97 and SC-EVPNI.

Figure 4 shows the evolution of transverse to longitudinal strain ratio for the three proposed homogenization schemes and the EVPSC model of Wang et al. (2010). Predictions of each homogenization scheme are approximately the same. The transverse to longitudinal strain ratio starts at the value of 0.35, which corresponds to the effective Poisson ratio of an elastic copper polycrystal with random texture and spherical grain shape (Lebensohn et al., 2012). As the deformation progresses, polycrystal transitions from elastic to fully plastic regime and the transverse to longitudinal strain ratio evolves to the value of 0.5, indicating transition to incompressible plastic flow.

Figure 5 shows the effect of the strain increment on the stress-strain predictions for each one of the proposed homogenization methods. The evolution of the grain shape and texture is turned off in order to isolate the effects of strain increment on the homogenization method. SC-EVPNI displays the largest dependence of the response on the time increment, while SC-MAK97 displays somewhat weaker time increment dependence. In the case of MT-MAK97 interaction equation, the time increment dependence is almost negligible. The strain increment dependence is ultimately caused by the time increment dependence of the effective properties under constant applied strain rate. The sensitivity of the effective compliance on the time increment can be evaluated by taking the derivative with respect to the time increment:

$$
\frac{\partial \bar{M}^{v}}{\partial \Delta t}=\frac{\partial}{\partial \Delta t} \sum_{r} c^{(r)} M^{v(r)}: B^{e, v(r)}=\sum_{r} c^{(r)} M^{v(r)}: \frac{\partial B^{e, v(r)}}{\partial \Delta t},\tag{70}
$$

where we first consider the sensitivity of the viscoplastic compliance for SC-MAK97. Stress concentration tensor derived from MAK97 interaction law can also be derived by taking the derivative of the interaction equation with respect to the macroscopic stress, under assumption that grain stress is a function of macroscopic stress:

$$
B^{e, v(r)}=\frac{\partial \sigma^{(r)}}{\partial \Sigma}=\left[\frac{\partial \dot{\varepsilon}^{(r)}}{\partial \sigma^{(r)}}+\tilde{M}^{e(r)}: \frac{\partial \dot{\sigma}^{(r)}}{\partial \sigma^{(r)}}+\tilde{M}^{v(r)}\right]^{-1}:\left[\frac{\partial \dot{E}}{\partial \Sigma}+\tilde{M}^{e(r)}: \frac{\partial \dot{\Sigma}}{\partial \Sigma}+\tilde{M}^{v(r)}\right].\tag{71}
$$

In the above expression, we did not assume the actual form of local or macroscopic linear constitutive relations. The time increment sensitivity of stress concentration tensor is then given by:

$$
\begin{aligned}
\frac{\partial B^{e, v(r)}}{\partial \Delta t} & =\frac{\partial B^{e, v(r)}}{\partial\left(\frac{\partial \dot{\varepsilon}^{(r)}}{\partial \sigma^{(r)}}\right)} \frac{\partial\left(\frac{\partial \dot{\varepsilon}^{(r)}}{\partial \sigma^{(r)}}\right)}{\partial \Delta t}+\frac{\partial B^{e, v(r)}}{\partial\left(\frac{\partial \dot{\sigma}^{(r)}}{\partial \sigma^{(r)}}\right)} \frac{\partial\left(\frac{\partial \dot{\sigma}^{(r)}}{\partial \sigma^{(r)}}\right)}{\partial \Delta t}+\frac{\partial B^{e, v(r)}}{\partial\left(\frac{\partial \dot{E}}{\partial \Sigma}\right)} \frac{\partial\left(\frac{\partial \dot{E}}{\partial \Sigma}\right)}{\partial \Delta t}+\frac{\partial B^{e, v(r)}}{\partial\left(\frac{\partial \dot{\Sigma}}{\partial \Sigma}\right)} \frac{\partial\left(\frac{\partial \dot{\Sigma}}{\partial \Sigma}\right)}{\partial \Delta t}+ \\
& \frac{\partial B^{e, v(r)}}{\partial \tilde{M}^{e(r)}} \frac{\partial \tilde{M}^{e(r)}}{\partial \Delta t}+\frac{\partial B^{e, v(r)}}{\partial \tilde{M}^{v(r)}} \frac{\partial \tilde{M}^{v(r)}}{\partial \Delta t}.
\end{aligned}
\tag{72}
$$

Therefore, the time increment sensitivity directly stems from the adopted constitutive relations at grain and macroscopic level. Once we adopt Eq. (7) as our constitutive equation, we introduce time-increment dependence of the derivative $\frac{\partial \dot{\varepsilon}^{(r)}}{\partial \sigma^{(r)}}=\frac{1}{\Delta t} M^{e(r)}+M^{e w(r)}+M^{v(r)}$. In addition, analogous constitutive equation at the macroscopic level introduces time dependence of the derivative $\frac{\partial \dot{E}}{\partial \Sigma}=\frac{1}{\Delta t} \bar{M}^{e}+\bar{M}^{e w}+\bar{M}^{v}$. The dependence of the derivatives $\frac{\partial \dot{\sigma}^{(r)}}{\partial \sigma^{(r)}}$ and $\frac{\partial \dot{\Sigma}}{\partial \Sigma}$ on $\Delta t$ is determined by the adopted numerical approximation for the stress rate (Eq. 8). Similar analysis can be applied to the elastic effective compliance. For the SC-EVPNI case, similar analysis holds as well. The reduced dependence of the effective properties in the MT-MAK97 case is due to the fact that the matrix properties are independent of the time increment (Eqs. (42-44)) and are pre-calculated using the separate elastic and viscoplastic self-consistent methods. Consequently, we have that $\frac{\partial \tilde{M}^{e(r)}}{\partial \Delta t}=\frac{\partial \tilde{M}^{v(r)}}{\partial \Delta t}=0$ in Eq. (72). In addition, the derivative $\frac{\partial\left(\frac{\partial \dot{E}}{\partial \Sigma}\right)}{\partial \Delta t}$ will have the partials $\frac{\partial\left(\frac{\partial \dot{E}}{\partial \Sigma}\right)}{\partial \bar{M}^{v}} \frac{\partial \bar{M}^{v}}{\partial \Delta t}=\frac{\partial\left(\frac{\partial \dot{E}}{\partial \Sigma}\right)}{\partial \bar{M}^{v}} \frac{\partial \bar{M}^{v}}{\partial \Delta t}=\frac{\partial\left(\frac{\partial \dot{E}}{\partial \Sigma}\right)}{\partial \bar{M}^{v}} \frac{\partial \bar{M}^{v}}{\partial \Delta t}=0$. As a result, the time increment sensitivity is considerably reduced. The fact that the actual constitutive response is non-linear will amplify time increment sensitivity, since even small changes in local grain stress with $\Delta t$ may lead to activation of different set of slip systems for certain orientations and thus different linearized compliance.

![](./images/812597125853478914_7.jpg)

Figure 6: Stereographic projections of grain {111} planes color coded according to the corresponding equivalent isotropic spreads of the deviatoric strain rate distributions, predicted by MT-MAK97. Plots are provided for different strain levels during compression of copper polycrystal along with the viscoplastic limit (VPSC prediction).

Figure 6 shows the predictions of intragranular strain rate fluctuations for MT-MAK97. The simulation setup is identical as before, except that the evolution of the grain shape and texture is turned off. Strain rate fluctuations for different grains at each strain level are visualized by color coding the {111} stereographic projections of the grain crystallographic orientations according to the equivalent isotropic spread of the deviatoric strain rate distribution (Krog-Pedersen et al., 2009). The equivalent isotropic spread describes the magnitude of a distribution and it is defined as: $\overline{SD}'(\dot{\varepsilon}') = \sqrt{\prod_{i=1}^{5} SD_{i}'}$, where $SD_{i}' = \sqrt{\lambda_{i}'}$ is the principal standard deviation and $\lambda_{i}'$ is the principal variance (eigenvalue) of the deviatoric strain rate covariance matrix (Krog-Pedersen et al., 2009). The strain rate tensor is represented as six dimensional vector, where the first five components describe the deviatoric part while the sixth component is the hydrostatic part of the

strain rate tensor (Lequeu et al., 1987). In the elastic region, the strain rate fluctuations are identical in all the grains, which is in agreement with the predictions of the purely elastic self-consistent method (Lebensohn et al., 2004). As the polycrystal starts deforming plastically, the strain rate fluctuations increase in magnitude and become different for grains of different crystallographic orientation. Quickly after the elastoplastic transition, the strain rate fluctuations tend to the viscoplastic limit obtained by the viscoplastic self-consistent method.

![](./images/812597125853478914_8.jpg)

Figure 7: Stereographic projections of grain {111} planes color coded according to the corresponding equivalent isotropic spreads of the deviatoric stress distributions, predicted by MT-MAK97. Plots are provided for different strain levels during compression of copper polycrystal, along with the viscoplastic limit (VPSC prediction).

Stress fluctuations calculated from the corresponding strain rate fluctuations using the method outlined in section 2.3.1 are shown on Fig. 7 using analogous visualization method. As opposed to the strain rate fluctuations, the stress fluctuations evolve slower and continue evolving even

after the elastoplastic transition. Grains with the largest stress fluctuations reach their viscoplastic limit only at higher strain levels.

The elastic strain rate is proportional to the stress rate, which implies that a large increase in the stress fluctuation, in comparison to the previous increment values, leads to a large fluctuation of elastic strain rate in the current increment. Large stress fluctuation also implies a large viscoplastic strain rate fluctuation, which is linearly related to the stress fluctuation. Therefore, a large increase in the stress fluctuation leads to an unreasonably large fluctuation of total strain rate. Consequently, presence of elasticity limits the rate of change of stress fluctuations with time. Thus, the stress fluctuations of grains with largest variance are going to reach their viscoplastic limit at the latest stage. Shape of the distribution also plays a role. Grains that have very anisotropic stress distribution at the viscoplastic limit will converge to it slower. This is because the elastic stress distributions are more isotropic, implying a large change in stress along at least one direction, which has to occur at limited rate of change. With the increase of rate exponent $n$ the elastoplastic transition becomes sharper and the stress fluctuations in the viscoplastic limit become more anisotropic and increase in magnitude. In addition, the viscoplastic compliance of certain grains becomes almost singular due to smaller number of active slip systems. Consequently, Eq. (63) becomes increasingly difficult to solve and a solution may not even exist under the adopted assumptions. The approach for calculation of fluctuations is based on the linearized grain viscoplastic behavior. Consequently, for the highly non-linear viscoplastic behavior of the grain and for the singular viscoplastic compliances the method fails. We have found that values of $n$ between 1 and 10 work fine for the tested cases.

### 3.3 Tension of stainless steel

We simulate tension of stainless steel at the strain rate of 0.0008 /s (Kanjarla et al., 2012). In the simulations, the initial microstructure is represented by 500 spherical grains with random crystal lattice orientation. Glide on {111}<110> slip systems is assumed with the rate exponent $n=10$. We adopt Voce hardening law given by the following evolution equation for slip resistance:
$$
\tau_{c}^{s}=\tau_{0}+\left(\tau_{1}+\theta_{1}\left(\sum_{s} \gamma^{s}\right)\right)\left(1-\exp \left(-\sum_{s} \gamma^{s}\left|\frac{\theta_{0}}{\tau_{1}}\right|\right)\right)
$$
where $\tau_{0}$ and $\theta_{0}$ are initial slip resistance and initial hardening rate, $\theta_{1}$ is the asymptotic hardening rate and $\tau_{1}+\tau_{0}$ is the back-extrapolated slip resistance. The Voce hardening parameters were calibrated for each homogenization method separately and the values are reported in Table 1. Figure 8 compares the

![](./images/812597125853478914_9.jpg)

Figure 8: Comparison of experimental tensile stress-strain curve for stainless steel with the corresponding predictions obtained by SC-MAK97, MT-MAK97 and SC-EVPNI.

Due to plastic anisotropy of different grains, at the end of the elastoplastic transition the load transfer leads to the observed relaxation of transverse lattice strains for the subset of grains with {001} parallel to the transverse direction (Kanjarla et al., 2012). As was noted before, both of the proposed self-consistent homogenization schemes result in a softer response than the MT-MAK97 approach. More compliant matrix leads to a smaller variation of grain stresses within the polycrystal, and thus the difference in the viscoplastic properties of different grains has relatively small effect on the lattice strains. In Sachs' limit case, when stress in each grain is equal to the macroscopic stress, the difference in viscoplastic behavior will have no influence on the lattice strains, which would solely depend on the elastic properties of the grains and their lattice orientation. Therefore, we conclude that the more compliant behavior of the proposed self-consistent methods is responsible for the poor predictions of sharp changes of lattice strains at the onset of plasticity.

![](./images/812597125853478914_10.jpg)

Figure 9: Experimental and predicted longitudinal and transverse lattice strains for {001}, {011}
and {111} planes for tension of stainless steel. The predictions are calculated by SC-MAK97,
MT-MAK97 and SC-EVPNI.

![](./images/812597125853478914_11.jpg)

Figure 10: Experimental and predicted longitudinal and transverse lattice strains for {001},
{011} and {111} planes for tension of stainless steel. The predictions are calculated by SC-

MAK97, MT-MAK97 and SC-EVPNI. The interaction tensor in the two self-consistent method has been scaled for parameter $\alpha=0.25$.

Molinari and Tóth (1994), Molinari et al. (1997) and Tomé (1999) have introduced an adjustable parameter to the interaction law in order to make the matrix more compliant for the stiff secant linearization case. We adopt the same approach and introduce an adjustable parameter, $\alpha$, to the both interaction laws. MAK97 viscoplastic interaction tensor then becomes:

$$
\tilde{M}^{v(r), e f f}=\alpha \tilde{M}^{v(r)}. \tag{73}
$$

Therefore, the compliance of the matrix surrounding the inhomogeneity corresponds to the effective compliance scaled by parameter $\alpha$. Analogous modification of the elasto-viscoplastic interaction tensor is given by:

$$
\tilde{M}^{e v(r), e f f}=\left(I-S^{e v(r), e f f}\right)^{-1}: S^{e v(r), e f f}: \bar{M}^{e v, e f f}, \tag{74}
$$

where the matrix compliance corresponds to the modified effective compliance: $\bar{M}^{e v, e f f}=$ $\bar{M}^{v} \alpha+\bar{M}^{e} \frac{1}{\Delta t}$. Based on observations made in previous paragraph, we set $\alpha=0.25$ for the two proposed self-consistent homogenization schemes, resulting in stiffer matrix behavior. The stress strain curves are recalibrated and the longitudinal $\{011\}$ and transversal $\{001\}$ lattice strains are shown on Fig. 10. Both self-consistent methods capture the sharp change in the lattice strains well, verifying the hypothesis that the effective properties and thus the matrix are too compliant.

Figure 11 shows the predictions of MT-MAK97 for the standard deviations of lattice strains. Experimental results are plotted on a separate figure due to large discrepancy, while the EVPFFT predictions are shown on the same plot for comparison (Kanjarla et al., 2012). Standard deviation of longitudinal lattice strains is under-predicted by MT-MAK97 in comparison to the EVPFFT results. However, the trends are captured appropriately with the lattice strains in the longitudinal direction for the set of grains with the $\{001\}$ plane parallel to the loading direction having the largest dispersion. Subsets of grains with the $\{111\}$ or $\{011\}$ planes parallel to the longitudinal direction develop lower lattice strain standard deviations along the longitudinal direction of about the same magnitude. Transversal lattice strain standard deviations predicted by

the MT-MAK97 approach are in good agreement with the EVPFFT results. Large discrepancy between the EVPFFT simulations and experiment was attributed to the lack of explicit representation of the dislocation networks in CP models (Kanjarla et al., 2012). Significant portion of lattice strain fluctuations comes from the stress fields associated with individual dislocations, which cannot be simulated using the continuum crystal plasticity models (Kanjarla et al., 2012). Recently, Wang et al. (2017) proposed a crystal plasticity formulation based on transition state theory and were able to accurately reproduce measured lattice strain standard deviations. Possible further improvement would be combining of the method proposed here with the approach of Wang et al. (2017).

Longitudinal:

![](./images/812597125853478914_12.jpg)

Figure 11: Experimental and predicted longitudinal and transverse lattice strain standard deviations for {001}, {011} and {111} planes for tension of stainless steel. The predictions are calculated by MT-MAK97 and EVPFFT model (Kanjarla et al., 2012).

### 3.4 Compression of magnesium

We simulate compression of magnesium at the strain rate of 1.0 /s. Initial microstructure consists of 500 spherical grains with random lattice orientation. The rate sensitivity exponent is set to $n = 10$ and the grains are allowed to deform by basal, prismatic and pyramidal II <c+a> slip modes, with the ratio of slip resistances: 10.0-15.0-20.0, respectively. Elastic constants for magnesium at room temperature are: $C_{11}=0.5944\ GPa$, $C_{33}=0.616\ GPa$, $C_{12}=0.2561\ GPa$, $C_{13}=0.2144\ GPa$, $C_{44}=0.166\ GPa$ and $C_{66}=0.169\ GPa$ (Slutsky and Garland, 1957). Figure 12 shows the stress strain response and the relative activities of slip modes as predicted by the three proposed homogenization schemes. As was observed before, MT-MAK97 gives the hardest response, followed by SC-MAK97. As the deformation progresses, the easiest basal slip activates first followed by the prismatic slip. Finally, close to the end of elastoplastic transition, when the stress becomes high enough, the hardest pyramidal II <c+a> slip activates.

Figure 13 shows the predictions of intragranular stress fluctuations obtained with MT-MAK97. As was noted for fcc polycrystals, in the elastic region the stress fluctuations are approximately the same in each grain, which is in agreement with the predications of purely elastic self-consistent method. As the response becomes plastic, the intragranular stress fluctuations become heterogeneous over the polycrystal and start converging to their viscoplastic limit. As for the fcc polycrystal, we observe slower convergence of the largest intragranular stress fluctuations to their viscoplastic limit, which is even more pronounced for magnesium due to larger anisotropy of the stress distributions. In addition, small number of active slip systems results in almost singular viscoplastic compliances for certain grains which also affects the predictions for second moments of stress and may cause convergence problems in solution procedure for Eq. (63).

![](./images/812597125853478914_13.jpg)

Figure 12: Stress-strain response and relative activities of magnesium polycrystal under compression predicted by SC-MAK97, MT-MAK97 and SC-EVPNI.

![](./images/812597125853478914_14.jpg)

Figure 13: Stereographic projections of grain {0001} planes color coded according to the corresponding equivalent isotropic spreads of the deviatoric stress distributions, predicted by

MT-MAK97. Plots are provided for different strain levels during compression of magnesium polycrystal, along with the viscoplastic limit (VPSC prediction).

## 4 Conclusion

We presented three novel homogenization schemes for polycrystals deforming in the elasto-viscoplastic regime, two of them based on Molinari et al.'s MAK97 interaction law, but differing on the type of homogenization assumption, i.e. self-consistent (SC-MAK97) vs Mori-Tanaka (MT-MAK97), and the third one deriving from a newly proposed non-incremental elasto-viscoplastic interaction law (SC-EVPNI). The proposed models were applied to compression of copper, tension of stainless steel, and compression of magnesium. Predictions of the three methods of effective behavior and grain averages of micromechanical fields were found to be fairly similar and to tend to the purely elastic and viscoplastic limits. The three methods were found to be numerically stable and to converge to the same effective behavior, regardless of the adopted time increment. An approximate method for calculation of second moments of stress was also developed, and its implementation in the MT-MAK97 case was shown to produce the most robust results, while in the SC-EVPNI case it shows an unreasonable dependence of the intragranular fluctuations on the time increment. This time step dependence of second moment estimations in the SC-EVPNI case is attributed to the adopted approximation of the elasto-viscoplastic constitutive relation. MT-MAK97 predictions of lattice strain standard deviations were found to be in acceptable agreement with full-field predictions. However, both crystal plasticity-based main-field and full-field intragranular fluctuation estimations are significantly lower than the measured values, due to the lack of explicit consideration of internal elastic fields due to dislocation structures.

## Acknowledgements

This work was supported by Los Alamos National Laboratory's Laboratory-Directed Research and Development (LDRD) program, Project 20180441ER.

## Appendix A

Consider an infinite linear elasto-viscoplastic matrix with elastic and viscoplastic compliances, $M^e$ and $M^v$, and back-extrapolated strain rate $\dot{E}^{v0}$. There is an ellipsoidal inclusion, $V^{inc}$, within the matrix experiencing eigenstrain rate: $\dot{\varepsilon}^*(\mathbf{x}) = \dot{\varepsilon}^*$, for $\mathbf{x} \in V^{inc}$ and $\dot{\varepsilon}^*(\mathbf{x}) = 0$, for $\mathbf{x} \notin V^{inc}$.

Strain rate at material point $\mathbf{x}$ is given by:

$$
\dot{\varepsilon}(\mathbf{x}) = M^e:\dot{\sigma}(\mathbf{x}) + M^v:\sigma(\mathbf{x}) + \dot{E}^{v0} + \dot{\varepsilon}^*(\mathbf{x}) = \left(M^e \frac{1}{\Delta t} + M^v\right):\sigma(\mathbf{x}) - M^e \frac{1}{\Delta t}:\sigma^t(\mathbf{x}) + \dot{E}^{v0} + \dot{\varepsilon}^*(\mathbf{x}).
$$

From here the expression for stress at material point $\mathbf{x}$ is:

$$
\sigma(\mathbf{x}) = \left(M^e \frac{1}{\Delta t} + M^v\right)^{-1}:\left(\dot{\varepsilon}(\mathbf{x}) + M^e \frac{1}{\Delta t}:\sigma^t(\mathbf{x}) - \dot{E}^{v0} - \dot{\varepsilon}^*(\mathbf{x})\right).
$$

The deviation of strain rate with respect to average strain rate (which is the matrix value $\dot{E}$) at material point $\mathbf{x}$ belonging to the inclusion is (Lebensohn, 2001):

$$
\tilde{\dot{\varepsilon}}(\mathbf{x}) = -\int_{R^3} \Gamma(\mathbf{x} - \mathbf{x}'):[\varphi(\mathbf{x}') - \langle\varphi\rangle]dx',
$$

where $\Gamma(\mathbf{x} - \mathbf{x}')$ is the Green operator and $\varphi(\mathbf{x}')$ is the stress polarization field $\varphi(\mathbf{x}') = \sigma(\mathbf{x}') - L^0:\dot{\varepsilon}(\mathbf{x}')$. $L^0$ is the stiffness of reference linear viscous medium. By substituting expression for polarization field and the expression for stress at material point $\mathbf{x}'$ we obtain:

$$
\tilde{\dot{\varepsilon}}(\mathbf{x}) = -\int_{R^3} \Gamma(\mathbf{x} - \mathbf{x}'):\left[\left(M^e \frac{1}{\Delta t} + M^v\right)^{-1}:\left(\dot{\varepsilon}(\mathbf{x}') + M^e \frac{1}{\Delta t}:\sigma^t(\mathbf{x}') - \dot{E}^{v0} - \dot{\varepsilon}^*(\mathbf{x}')\right) - L^0:\dot{\varepsilon}(\mathbf{x}') - \left(\Sigma - L^0:\dot{E}\right)\right]dx'.
$$

After setting the stiffness of the reference linear viscous medium to match the matrix elasto-viscoplastic stiffness, $L^0 = \left(M^e \frac{1}{\Delta t} + M^v\right)^{-1}$, and after substituting the expression for stress in the matrix we get:

$$
\tilde{\dot{\varepsilon}}(\mathbf{x}) = -\int_{R^3} \Gamma(\mathbf{x} - \mathbf{x}'):\left[\left(M^e \frac{1}{\Delta t} + M^v\right)^{-1}:\left(M^e \frac{1}{\Delta t}:(\sigma^t(\mathbf{x}') - \Sigma^t) - \dot{\varepsilon}^*(\mathbf{x}')\right)\right]dx'.
$$

The average fluctuation in the inclusion is given by:

$$
\tilde{\dot{\varepsilon}} = \left(\frac{1}{V^{inc}} \int_{V^{inc}} \int_{V^{inc}} \Gamma(\mathbf{x}-\mathbf{x}')dx' dx\right):\left(M^e \frac{1}{\Delta t}+M^v\right)^{-1}:\dot{\varepsilon}^*-
$$

$$
\int_{V^{inc}} \int_{R^3} \Gamma(\mathbf{x}-\mathbf{x}'):\left(M^e \frac{1}{\Delta t}+M^v\right)^{-1}:\left(M^e \frac{1}{\Delta t}:\left(\sigma^t(\mathbf{x}')-\Sigma^t\right)\right) dx' dx.
$$

The second integral will be zero for purely elastic behavior: $\int_{R^3} \Gamma(\mathbf{x}-\mathbf{x}'):\left(\sigma^t(\mathbf{x}')-\Sigma^t\right)dx' = 0$, because the field $(\sigma^t(\mathbf{x}')-\Sigma^t)$ is divergence free (Michel et al., 2001). In addition, for purely viscoplastic behavior this integral will again be zero due to $M^e=0$. Consequently, we assume that the contribution of this integral is fairly small and thus can be neglected, resulting in the final expression:

$$
\tilde{\dot{\varepsilon}} = S^{ev}:\dot{\varepsilon}^*,
$$

where $S^{ev}$ is the elasto-viscoplastic Eshelby tensor defined as $S^{ev} = \frac{1}{V^{inc}} \int_{V^{inc}} \int_{V^{inc}} \Gamma(\mathbf{x}- \mathbf{x}')dx' dx \left(M^e \frac{1}{\Delta t}+M^v\right)^{-1}$. Note, that Nemat-Nasser and Obata (1986) used a similar approach but in the incremental form. In addition, they assumed the second integral to be $S^{ev}:M^e \frac{1}{\Delta t}:\left(\sigma^{t,inc}-\Sigma^t\right)$. This approximation in our case leads to incorrect behavior for purely elastic behavior, when this integral should be identically zero, and overly compliant behavior in viscoplastic regime.

## Appendix B

The linear incompressible constitutive behavior of inhomogeneity and matrix is given by:

$$
\dot{\varepsilon}^{(r)} = \frac{1}{2\mu^{e(r)}} \dot{\sigma}^{(r)} + \frac{1}{2\mu^{v(r)}} \sigma^{(r)}
$$

$$
\dot{E} = \frac{1}{2\mu^e} \dot{\Sigma} + \frac{1}{2\mu^v} \Sigma,
$$

where $\mu^{e(r)}$ and $\mu^e$ are the elastic shear moduli of inhomogeneity and matrix and $\mu^{v(r)}$ and $\mu^v$ are the viscous moduli of inhomogeneity and matrix, respectively. Since the behavior is incompressible, all the tensors are traceless and defined by 5 deviatoric components. By performing time discretization of stress, the constitutive relation in the matrix is given by: $\dot{E}=$

$$\left(\frac{1}{\Delta t} \frac{1}{2 \mu^{e}}+\frac{1}{2 \mu^{v}}\right) \Sigma-\frac{1}{\Delta t} \frac{1}{2 \mu^{e}} \Sigma^{t}$$, from where we can identify the elasto-viscoplastic modulus of matrix $$\frac{1}{2 \mu^{e v}}=\left(\frac{1}{\Delta t} \frac{1}{2 \mu^{e}}+\frac{1}{2 \mu^{v}}\right)$$. The integral of modified Green operator in this case is given by $$\frac{1}{v_{i n c}} \int_{V_{i n c}} \int_{V_{i n c}} \Gamma\left(\mathbf{x}-\mathbf{x}^{\prime}\right) d x^{\prime} d x=\frac{1}{5 \mu^{e v}} K$$, where we have used the matrix elasto-viscoplastic properties for reference medium and $$K_{i j k l}=\frac{1}{2}\left(\delta_{i k} \delta_{j l}+\delta_{i l} \delta_{j k}\right)-\frac{1}{3} \delta_{i j} \delta_{k l}$$ (Mercier and Molinari, 2009). Note that since we are dealing with space of symmetric deviatoric tensors, operator $K$ is identity tensor $K \equiv I$. The Eshelby tensor is then given by $$S^{e v}=\frac{1}{5 \mu^{e v}} I:\left(2 \mu^{e v} I\right)=\frac{2}{5} I$$. Next the interaction tensors are given by:

$$
\tilde{M}^{e v(r)}=\left(I-\frac{2}{5} I\right)^{-1}:\left(\frac{2}{5} I\right):\left(\frac{1}{2 \mu^{e v}} I\right)=\frac{1}{3 \mu^{e v}} I
$$

$$
\tilde{M}^{e e v(r)}=\left(I-\frac{2}{5} I\right)^{-1}:\left(\frac{2}{5} I\right):\left(\frac{1}{2 \mu^{e}} I\right)=\frac{1}{3 \mu^{e}} I.
$$

Finally, by replacing the interaction tensors into the interaction Eq. (31) we get:

$$
\dot{\varepsilon}^{(r)}-\dot{E}=-\frac{1}{3 \mu^{e v}} I:\left(\sigma^{(r)}-\Sigma\right)+\frac{1}{\Delta t} \frac{1}{3 \mu^{e}} I:\left(\sigma^{(r), t}-\Sigma^{t}\right).
$$

After substituting $$\frac{1}{\mu^{e v}}=\left(\frac{1}{\Delta t} \frac{1}{\mu^{e}}+\frac{1}{\mu^{v}}\right)$$ and regrouping:

$$
\dot{\varepsilon}^{(r)}-\dot{E}=-\frac{\dot{\sigma}^{(r)}-\dot{\Sigma}}{3 \mu^{e}}-\frac{\sigma^{(r)}-\Sigma}{3 \mu^{v}},
$$

which is exactly the same as Eq. (7) in (Mercier et al., 2005) and thus corresponds to analytical solution of Hashin (1969).

## References

Agoras, M., Avazmohammadi, R., Ponte Castañeda, P., 2016. Incremental variational procedure for elasto-viscoplastic composites and application to polymer- and metal-matrix composites reinforced by spheroidal elastic particles. International Journal of Solids and Structures 97-98, 668-686.

Anglin, B.S., Lebensohn, R.A., Rollett, A.D., 2014. Validation of a numerical method based on Fast Fourier Transforms for heterogeneous thermoelastic materials by comparison with analytical solutions. Computational Materials Science 87, 209-217.

Benveniste, Y., 1987. A new approach to the application of Mori-Tanaka's theory in composite materials. Mechanics of Materials 6, 147-157.

Berbenni, S., Capolungo, L., 2015. A Mori-Tanaka homogenization scheme for non-linear elasto-viscoplastic heterogeneous materials based on translated fields: An affine extension. Comptes Rendus Mecanique 343, 95-106.

Berveiller, M., Zaoui, A., 1978. An extension of the self-consistent scheme to plastically-flowing polycrystals. Journal of the Mechanics and Physics of Solids 26, 325-344.

Bobeth, M., Diener, G., 1987. Static Elastic and Thermoelastic Field Fluctuations in Multiphase Composites. J Mech Phys Solids 35, 137-149.

Brassart, L., Stainier, L., Doghri, I., Delannay, L., 2012. Homogenization of elasto-(visco) plastic composites based on an incremental variational principle. International Journal of Plasticity 36, 86-112.

Buchheit, T.E., Wellman, G.W., Battaile, C.C., 2005. Investigating the limits of polycrystal plasticity modeling. International Journal of Plasticity 21, 221-249.

Budiansky, B., Wu, T.T., 1961. Theoretical prediction of plastic strains of polycrystals. HARVARD UNIV CAMBRIDGE MASS.

Dawson, P.R., Boyce, D.E., Rogge, R.B., 2005. Correlation of diffraction peak broadening to crystal strengthening in finite element simulations. Mat Sci Eng a-Struct 399, 13-25.

Dawson, P.R., Marin, E.B., 1997. Computational mechanics for metal deformation processes using polycrystal plasticity, Advances in applied mechanics. Elsevier, pp. 77-169.

Dunne, F., Petrinic, N., 2005. Introduction to computational plasticity. Oxford University Press on Demand.

Eshelby, J.D., 1957. The Determination of the Elastic Field of an Ellipsoidal Inclusion, and Related Problems. Proceedings of the Royal Society of London Series a-Mathematical and Physical Sciences 241, 376-396.

Fullwood, D.T., Niezgoda, S.R., Adams, B.L., Kalidindi, S.R., 2010. Microstructure sensitive design for performance optimization. Prog Mater Sci 55, 477-562.

Hashin, Z., 1969. The inelastic inclusion problem. International Journal of Engineering Science 7, 11-36.

Hershey, A., 1954. The elasticity of an isotropic aggregate of anisotropic cubic crystals. Journal of Applied mechanics-transactions of the ASME 21, 236-240.

Hill, R., 1965. Continuum Micro-Mechanics of Elastoplastic Polycrystals. J Mech Phys Solids 13, 89-&.

Humphreys, F.J., Hatherly, M., 2012. Recrystallization and related annealing phenomena. Elsevier.

Hutchinson, J.W., 1976. Bounds and Self-Consistent Estimates for Creep of Polycrystalline Materials. Proceedings of the Royal Society of London Series a-Mathematical and Physical Sciences 348, 101-127.

Iwakuma, T., Nemat-Nasser, S., 1984. Finite Elastic Plastic-Deformation of Polycrystalline Metals. Proceedings of the Royal Society of London Series a-Mathematical Physical and Engineering Sciences 394, 87-119.

Jeong, Y., Tomé, C.N., 2019. Extension of the visco-plastic self-consistent model to account for elasto-visco-plastic behavior using a perturbed visco-plastic approach. Modelling and Simulation in Materials Science and Engineering 27, 085013.

Kalidindi, S.R., Bhattacharyya, A., Doherty, R.D., 2004. Detailed analyses of grain-scale plastic deformation in columnar polycrystalline aluminium using orientation image mapping and crystal plasticity models. Proceedings of the Royal Society of London. Series A: Mathematical, Physical and Engineering Sciences 460, 1935-1956.

Kalidindi, S.R., Bronkhorst, C.A., Anand, L., 1992. Crystallographic texture evolution in bulk deformation processing of FCC metals. J Mech Phys Solids 40, 537-569.

Kanjarla, A.K., Lebensohn, R.A., Balogh, L., Tomé, C.N., 2012. Study of internal lattice strain distributions in stainless steel using a full-field elasto-viscoplastic formulation based on fast Fourier transforms. Acta Materialia 60, 3094-3106.

Kreher, W., 1990. Residual-Stresses and Stored Elastic Energy of Composites and Polycrystals. J Mech Phys Solids 38, 115-128.

Krog-Pedersen, S., Bowen, J.R., Pantleon, W., 2009. Quantitative characterization of the orientation spread within individual grains in copper after tensile deformation. International Journal of Materials Research 100, 433-438.

Kröner, E., 1961. Zur plastischen verformung des vielkristalls. Acta Metallurgica 9, 155-161.

Kröner, E., 1990. Modified Green functions in the theory of heterogeneous and/or anisotropic linearly elastic media, Micromechanics and inhomogeneity. Springer, pp. 197-211.

Lahellec, N., Suquet, P., 2007a. On the effective behavior of nonlinear inelastic composites: I. Incremental variational principles. J Mech Phys Solids 55, 1932-1963.

Lahellec, N., Suquet, P., 2007b. On the effective behavior of nonlinear inelastic composites: II: A second-order procedure. J Mech Phys Solids 55, 1964-1992.

Lahellec, N., Suquet, P., 2013. Effective response and field statistics in elasto-plastic and elasto-viscoplastic composites under radial and non-radial loadings. International Journal of Plasticity 42, 1-30.

Laws, N., 1973. On the thermostatics of composite materials. J Mech Phys Solids 21, 9-17.

Lebensohn, R.A., 2001. N-site modeling of a 3D viscoplastic polycrystal using Fast Fourier Transform. Acta Materialia 49, 2723-2737.

Lebensohn, R.A., Brenner, R., Castelnau, O., Rollett, A.D., 2008. Orientation image-based micromechanical modelling of subgrain texture evolution in polycrystalline copper. Acta Materialia 56, 3914-3926.

Lebensohn, R.A., Kanjarla, A.K., Eisenlohr, P., 2012. An elasto-viscoplastic formulation based on fast Fourier transforms for the prediction of micromechanical fields in polycrystalline materials. International Journal of Plasticity 32-33, 59-69.

Lebensohn, R.A., Liu, Y., Ponte Castañeda, P., 2004. On the accuracy of the self-consistent approximation for polycrystals: comparison with full-field numerical simulations. Acta Materialia 52, 5347-5361.

Lebensohn, R.A., Tomé, C.N., 1993. A Self-Consistent Anisotropic Approach for the Simulation of Plastic-Deformation and Texture Development of Polycrystals - Application to Zirconium Alloys. Acta Metall Mater 41, 2611-2624.

Lebensohn, R.A., Tomé, C.N., Ponte Castañeda, P., 2007. Self-consistent modelling of the mechanical behaviour of viscoplastic polycrystals incorporating intragranular field fluctuations. Philos Mag 87, 4287-4322.

Lebensohn, R.A., Zecevic, M., Knezevic, M., McCabe, R.J., 2016. Average intragranular misorientation trends in polycrystalline materials predicted by a viscoplastic self-consistent approach. Acta Materialia 104, 228-236.

Lequeu, P., Gilormini, P., Montheillet, F., Bacroix, B., Jonas, J., 1987. Yield surfaces for textured polycrystals—I. Crystallographic approach. Acta Metallurgica 35, 439-451.

Lipinski, P., Berveiller, M., 1989. Elastoplasticity of micro-inhomogeneous metals at large strains. International Journal of Plasticity 5, 149-172.

Liu, Y., 2003. Macroscopic behavior, field fluctuations and texture evolution in viscoplastic polycrystals.

Liu, Y., Ponte Castañeda, P., 2004. Second-order theory for the effective behavior and field fluctuations in viscoplastic polycrystals. J Mech Phys Solids 52, 467-495.

Mareau, C., Berbenni, S., 2015. An affine formulation for the self-consistent modeling of elasto-viscoplastic heterogeneous materials based on the translated field method. International journal of Plasticity 64, 134-150.

Masson, R., Bornert, M., Suquet, P., Zaoui, A., 2000. An affine formulation for the prediction of the effective properties of nonlinear composites and polycrystals. J Mech Phys Solids 48, 1203-1227.

Mercier, S., Jacques, N., Molinari, A., 2005. Validation of an interaction law for the Eshelby inclusion problem in elasto-viscoplasticity. International Journal of Solids and Structures 42, 1923-1941.

Mercier, S., Molinari, A., 2009. Homogenization of elastic-viscoplastic heterogeneous materials: Self-consistent and Mori-Tanaka schemes. International Journal of Plasticity 25, 1024-1048.

Mercier, S., Molinari, A., Berbenni, S., Berveiller, M., 2012. Comparison of different homogenization approaches for elastic-viscoplastic materials. Modelling and Simulation in Materials Science and Engineering 20, 024004.

Michel, J., Moulinec, H., Suquet, P., 2001. A computational scheme for linear and non-linear composites with arbitrary phase contrast. International Journal for Numerical Methods in Engineering 52, 139-160.

Michel, J.C., Moulinec, H., Suquet, P., 1999. Effective properties of composite materials with periodic microstructure: a computational approach. Computer Methods in Applied Mechanics and Engineering 172, 109-143.

Michel, J.C., Suquet, P., 2017. Effective potentials in nonlinear polycrystals and quadrature formulae. Proc Math Phys Eng Sci 473, 20170213.

Miehe, C., Rosato, D., Frankenreiter, I., 2010. Fast estimates of evolving orientation microstructures in textured bcc polycrystals at finite plastic strains. Acta Materialia 58, 4911-4922.

Miller, M.P., Park, J.S., Dawson, P.R., Han, T.S., 2008. Measuring and modeling distributions of stress state in deforming polycrystals. Acta Materialia 56, 3927-3939.

Molinari, A., Ahzi, S., Kouddane, R., 1997. On the self-consistent modeling of elastic-plastic behavior of polycrystals. Mechanics of Materials 26, 43-62.

Molinari, A., Canova, G.R., Ahzi, S., 1987. A Self-Consistent Approach of the Large Deformation Polycrystal Viscoplasticity. Acta Metallurgica 35, 2983-2994.

Molinari, A., Tóth, L., 1994. Tuning a self consistent viscoplastic model by finite element results—I. Modeling. Acta Metall Mater 42, 2453-2458.

Morawiec, A., 2004. Orientations and Rotations. Computations in Crystallographic Textures. Berlin: Springer.

Mori, T., Tanaka, K., 1973. Average stress in matrix and average elastic energy of materials with misfitting inclusions. Acta metallurgica 21, 571-574.

Moulinec, H., Suquet, P., 1998. A numerical method for computing the overall response of nonlinear composites with complex microstructure. Computer Methods in Applied Mechanics and Engineering 157, 69-94.

Mura, T., 2013. Micromechanics of defects in solids. Springer Science & Business Media.

Neil, C.J., Wollmershauser, J.A., Clausen, B., Tomé, C.N., Agnew, S.R., 2010. Modeling lattice strain evolution at finite strains and experimental verification for copper and stainless steel using in situ neutron diffraction. International Journal of Plasticity 26, 1772-1791.

Nemat-Nasser, S., Obata, M., 1986. Rate-dependent, finite elasto-plastic deformation of polycrystals. Proceedings of the Royal Society of London. A. Mathematical and Physical Sciences 407, 343-375.

Ortiz, M., Stainier, L., 1999. The variational formulation of viscoplastic constitutive updates. Computer Methods in Applied Mechanics and Engineering 171, 419-444.

Paquin, A., Berbenni, S., Favier, V., Lemoine, X., Berveiller, M., 2001. Micromechanical modeling of the elastic–viscoplastic behavior of polycrystalline steels. International Journal of Plasticity 17, 1267-1302.

Paquin, A., Sabar, H., Berveiller, M., 1999. Integral formulation and self-consistent modelling of elastoviscoplastic behavior of heterogeneous materials. Archive of Applied Mechanics 69, 14-35.

Pokharel, R., Lind, J., Kanjarla, A.K., Lebensohn, R.A., Li, S.F., Kenesei, P., Suter, R.M., Rollett, A.D., 2014. Polycrystal Plasticity: Comparison Between Grain - Scale Observations of Deformation and Simulations. Annual Review of Condensed Matter Physics 5, 317-346.

Ponte Castañeda, P., 2002. Second-order homogenization estimates for nonlinear composites incorporating field fluctuations: I—theory. Journal of the Mechanics and Physics of Solids 50, 737-757.

Quey, R., Dawson, P.R., Driver, J.H., 2012. Grain orientation fragmentation in hot-deformed aluminium: Experiment and simulation. Journal of the Mechanics and Physics of Solids 60, 509-524.

Quey, R., Driver, J.H., Dawson, P.R., 2015. Intra-grain orientation distributions in hot-deformed aluminium: Orientation dependence and relation to deformation mechanisms. Journal of the Mechanics and Physics of Solids 84, 506-527.

Raabe, D., Sachtleber, M., Zhao, Z., Roters, F., Zaefferer, S., 2001. Micromechanical and macromechanical effects in grain scale polycrystal plasticity experimentation and simulation. Acta Materialia 49, 3433-3441.

Roters, F., Eisenlohr, P., Hantcherli, L., Tjahjanto, D.D., Bieler, T.R., Raabe, D., 2010. Overview of constitutive laws, kinematics, homogenization and multiscale methods in crystal plasticity finite-element modeling: Theory, experiments, applications. Acta Materialia 58, 1152-1211.

Sabar, H., Berveiller, M., Favier, V., Berbenni, S., 2002. A new class of micro-macro models for elastic-viscoplastic heterogeneous materials. International Journal of Solids and Structures 39, 3257-3276.

Slutsky, L.J., Garland, C.W., 1957. Elastic Constants of Magnesium from 4.2-Degrees-K to 300- Degrees-K. Physical Review 107, 972-976.

Song, D.W., Ponte Castañeda, P., 2018. Fully optimized second-order homogenization estimates for the macroscopic response and texture evolution of low-symmetry viscoplastic polycrystals. International Journal of Plasticity 110, 272-293.

Tomé, C.N., 1999. Self-consistent polycrystal models: a directional compliance criterion to describe grain interactions. Modelling and Simulation in Materials Science and Engineering 7, 723.

Turner, P.A., Tomé, C.N., 1994. A Study of Residual-Stresses in Zircaloy-2 with Rod Texture. Acta Metall Mater 42, 4143-4153.

Turner, T., Shade, P., Schuren, J., Groeber, M., 2012. The influence of microstructure on surface strain distributions in a nickel micro-tension specimen. Modelling and Simulation in Materials Science and Engineering 21, 015002.

Verlinden, B., Driver, J., Samajdar, I., Doherty, R.D., 2007. Thermo-mechanical processing of metallic materials. Elsevier.

Wang, H., Capolungo, L., Clausen, B., Tomé, C.N., 2017. A crystal plasticity model based on transition state theory. International Journal of Plasticity 93, 251-268.

Wang, H., Wu, P.D., Tomé, C.N., Huang, Y., 2010. A finite strain elastic-viscoplastic self-consistent model for polycrystalline materials. J Mech Phys Solids 58, 594-612.

Weng, G.J., 1981. Self-Consistent Determination of Time-Dependent Behavior of Metals. Journal of Applied Mechanics 48, 41-46.

Zecevic, M., Lebensohn, R.A., McCabe, R.J., Knezevic, M., 2018. Modeling of intragranular misorientation and grain fragmentation in polycrystalline materials using the viscoplastic self-consistent formulation. International Journal of Plasticity 109, 193-211.

Zecevic, M., Lebensohn, R.A., McCabe, R.J., Knezevic, M., 2019. Modelling recrystallization textures driven by intragranular fluctuations implemented in the viscoplastic self-consistent formulation. Acta Materialia 164, 530-546.

Zecevic, M., Pantleon, W., Lebensohn, R.A., McCabe, R.J., Knezevic, M., 2017. Predicting intragranular misorientation distributions in polycrystalline metals using the viscoplastic self-consistent formulation. Acta Materialia 140, 398-410.
