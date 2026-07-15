![](./images/813251085438287872_1.jpg)

International Journal of Engineering Science 64 (2013) 23-36

Contents lists available at SciVerse ScienceDirect

International Journal of Engineering Science

journal homepage: www.elsevier.com/locate/ijengsci

![](./images/813251085438287872_2.jpg)

# Generalization of Maxwell homogenization scheme for elastic material containing inhomogeneities of diverse shape

![](./images/813251085438287872_3.jpg)

Igor Sevostianov $^{a,*}$, Albert Giraud $^{b}$

$^{a}$ Department of Mechanical and Aerospace Engineering, New Mexico State University, Las Cruces, NM 88003, USA
$^{b}$ Université de Lorraine/CNRS/CREGU, Georessources Laboratory, BP 40, 54501 Vandoeuvre-lès-Nancy, France

---

## ARTICLE INFO

**Article history:**
Received 4 December 2012
Accepted 24 December 2012
Available online 30 January 2013

**Keywords:**
Maxwell's method
Homogenization
Effective elastic properties
Multiphase composites

---

## ABSTRACT

The paper focuses on the reformulation of classical Maxwell's (1873) homogenization method for elastic composites. Maxwell's scheme that equates the far fields produced by a set of inhomogeneities and by a fictitious domain with unknown effective properties is re-written in terms of the compliance contribution tensors. Explicit formula for tensor of effective elastic compliances is derived for the case the ellipsoidal fictitious domain. The method is illustrated by four examples – material containing multiple identical spheroidal pores, material containing three families of inhomogeneities having different shapes and properties, material containing circular cracks that have preferential orientation with certain scatter, and material containing randomly oriented non-ellipsoidal (superspherical) pores.

© 2013 Elsevier Ltd. All rights reserved.

---

## 1. Introduction and background material

The present paper focuses on the development of a micromechanical model that allows one to calculate effective properties of heterogeneous materials containing inhomogeneities of diverse shape and/or properties. The problem of effective properties of heterogeneous materials belongs to classical problems of micromechanics and has more than a century long history. Detailed description of the existing approaches can be found in reviews of Hashin (1983) and Markov (2000). All the analytical methods can be subdivided on two main groups – exact solutions that include non-interaction approximation, variational bounds and solutions for periodic microstructures; and approximate schemes that aim at accounting for interactions between the inhomogeneities by placing *non-interacting* ones into some sort of effective environment. This can be done in different ways:

- *Effective media approaches* where a representative inhomogeneity, treated as a single one, is placed into homogeneous material possessing unknown effective properties. The following modifications of this approach have been developed in literature:
(1) In the *self-consistent scheme*, the inhomogeneity is embedded into material with effective properties tha can be found from the solution of a single inclusion problem. This scheme was first employed probably by Clausius (1879) and then developed in works of Bruggeman (1935) for effective conductivity; by Kröner (1958) for elastic properties of polycrystals and by Skorohod (1961), Hill (1965) and Budiansky (1965) for effective elastic properties of matrix composites.

---

* Corresponding author.
E-mail address: Igor@nmsu.edu (I. Sevostianov).

0020-7225/$ - see front matter © 2013 Elsevier Ltd. All rights reserved.
http://dx.doi.org/10.1016/j.ijengsci.2012.12.004

(2) The generalized self-consistent scheme first proposed by Kerner (1956) and then developed by Christensen and Loo (1979) differs from the self-consistent one in introducing an intermediate layer with the properties of the matrix between the inhomogeneity and the background homogeneous material.

(3) The differential scheme can be considered as an infinitesimal version of the self-consistent scheme. It was first proposed by Bruggeman (1935, 1937) and was further developed by Vavakin and Salganik (1975), McLaughlin (1977), and Zimmerman (1991). The scheme assumes that inhomogeneities are incrementally added to the material until the final volume fraction is reached. On each increment, a set of non-interacting inhomogeneities is added to the homogenized material with the properties determined at the previous step. As pointed out by McLaughlin (1977), the total concentration of inhomogeneities introduced to the matrix does not coincide with the volume concentration of the dispersed phase since certain fraction of the volume where "new" inhomogeneities are placed is already occupied by the "old" ones.

The above-mentioned schemes have the shortcoming that, in anisotropic cases, the type of the overall anisotropy and its orientation must be hypothesized a priori. In some cases (such as parallel inhomogeneities) this may be obvious; however, in general this is not a trivial matter. Another shortcoming is that these schemes assume that all the inhomogeneities are identical.

- In effective field approaches, each inhomogeneity, treated as an isolated one, is placed into the unaltered matrix material. The interactions between different inhomogeneities are accounted for by assuming that the external field acting on them differs from the remotely applied one. In the simplest version (Mori-Tanaka scheme), the mentioned field is taken as the average over the matrix and is the same for all inhomogeneities (Mori & Tanaka, 1973; Benveniste, 1986). In the more advanced Kanaun and Levin's (1994) method, the effective field can reflect the statistics of mutual positions of inhomogeneities. For multi-phase composites, fields acting on different families of inhomogeneities are different (Kanaun & Jeulin, 2001).
- Maxwell's (1873) scheme, that is probably the oldest method of homogenization, equates the far field produced by the considered set of inhomogeneities to the far field produced by a fictitious domain of certain shape that possesses unknown effective properties.

In his original work, Maxwell (1873) considered a large sphere with the unknown effective conductivity $k_{\text{eff}}$ embedded in the background material of conductivity $k_0$ and containing non-interacting small spheres of conductivity $k_1$ and volume fraction $c$. He calculated the far-field asymptotics of the perturbation of the externally applied electric field in two different

![](./images/813251085438287872_4.jpg)

Fig. 1. Scheme of Maxwell's homogenization method. Effective properties of a composite (a) are calculated by equating effects produced by set of inhomogeneities embedded in the matrix material (b) and by fictitious domain having yet unknown effective properties (c).

ways: (1) as a sum of far-fields generated by the small spheres, and (2) as the far-field generated by the large sphere. Equating the two (Fig. 1) yields the effective conductivity in the following form:

$$
k_{\mathrm{eff}}=k_{0} \frac{1+2 \Psi c}{1-\Psi c}
\tag{1.1}
$$

where $\Psi=(k_{1}-k_{0})/(k_{1}+2k_{0})$. This relation is non-linear in concentration of inhomogeneities. By comparison with periodic solution, Lord Rayleigh (1892) found that Maxwell's formula is accurate up to volume fractions as high as 0.4. As discussed by Mogilevskaya, Stolarski, and Crouch (2012) and by Sevostianov and Kachanov (2012a), the Maxwell's formula (6.5.1) has been misinterpreted and linearized with respect to $c$ that substantially worsened the accuracy of the method (see, for example, Jeffrey, 1973 & Markov, 2000):

$$
k_{\mathrm{eff}}=k_{0}(1+3 \Psi c)
\tag{1.2}
$$

This formula is sometimes erroneously identified with Maxwell's method itself (see, for example, the book of Milton, 2002). Moreover, in contrast with original Maxwell's result, formula (6.5.2) violates Hashin and Shtrikman (1962) bounds for the effective conductivity (Sevostianov & Kachanov, 2012a).

Seeking to improve the linearized Maxwell's formula (1.2), Jeffrey (1973) considered series expansion of the effective conductivity (in powers of $c$) and calculated the coefficient at the $c^{2}$-term:

$$
k_{\mathrm{eff}} / k_{0}=(1+3 \Psi c)+c^{2}\left(3 \Psi^{2}+\frac{3 \Psi^{3}}{4}+\frac{9 \Psi^{3}}{16} \frac{\alpha+2}{2 \alpha+3}+\frac{3 \Psi^{4}}{64}+\cdots\right)+o\left(c^{2}\right)
\tag{1.3}
$$

where $\alpha=k_{1}/k_{0}$. Fig. 2 compares Maxwell's original result (1.1) with the linearized version (1.2) and experimental data of Wong and Bollampally (1999) for (thermal) conductivity of epoxy containing particles of (a) silica ($\alpha=k_{1}/k_{0}=7.69$), (b) silica coated aluminum nitride (SCAN) ($\alpha=1128$), and (c) alumina ($\alpha=185$). The insets illustrate shapes of the ceramic particles. These plots also show results calculated by Jeffrey's formula (1.3) (for which the coefficients at $c^{2}$-term were taken from the plot in his paper as 1.89, 4.51, and 4.35 for silica, SCAN and alumina particles respectively) and the Hashin-Shtrikman bounds for conductivity (Hashin & Shtrikman, 1962). Note, that Jeffrey's results are closer to the original Maxwell's ones but still violate the bounds. Fig. 2 also illustrates importance of appropriate modeling of the shapes of inhomogeneities. Indeed, results for a composite with spherical silica particles coincide with experimental measurements up to the volume concentration of inhomogeneities 0.5. For SCAN and alumina particles having rather irregular shape, modeling them as spherical ones leads to acceptable agreement with experiment at the volume concentrations up to 0.2.

Recently Maxwell's scheme started to attract increasing attention. We mention the works of McCartney and Kelly (2008) and McCartney (2010) where the scheme was formulated for the elastic properties of a material containing either random or aligned ellipsoidal inhomogeneities of identical aspect ratios. Levin, Kanaun, and Markov (2012) applied Maxwell' scheme to find elastic, electric and poroelastic constants of a composite containing several families of ellipsoidal inhomogeneities. Note that, in the mentioned work, the authors also identify approach of Kuster and Toksöz (1974) widely used in geomechanics with Maxwell's scheme. This statement, however, requires a proof.

![](./images/813251085438287872_5.jpg)

Fig. 2. Effective thermal conductivity of epoxy matrix filled with (a) silica, (b) SCAN (silica coated aluminum nitride) and (c) alumina particles: predictions by Maxwell's formula (1.1), its linearized variant (1.2), Jeffrey formula (1.3) are compared with experimental data of Wong and Bollampally (1999) and with Hashin-Shtrikman bounds for thermal conductivity. Insets show shape of particles of each material used for reinforcement.

In the present work, we use Maxwell's approach to derive formulas for effective elastic properties of composite containing inhomogeneities of generally diverse shapes and of arbitrary orientation distribution. To this end, we reformulate Maxwell's assumptions using the concept of property contribution tensor (see review of Kachanov & Sevostianov, 2005). The results are specified for spheroidal particles, for which the final formulas can be obtained in closed explicit form. We also consider example of a material containing non-ellipsoidal pores, for which any other formulation of the Maxwell's scheme cannot be applied.

## 2. Property contribution tensors

In this section, we briefly outline the idea of property contribution tensors that has been first proposed by Kachanov, Tsukrov, and Shafiro (1994) for porous materials. For general composites, these tensors were discussed by Sevostianov and Kachanov (1999, 2002) We consider a homogeneous isotropic elastic material (matrix), with the compliance and stiffness tensors $\boldsymbol{S}^0$ and $\boldsymbol{C}^0$. It contains an inhomogeneity, of volume $V^*$, of a different material with the compliance and stiffness tensors $\boldsymbol{S}^1$ and $\boldsymbol{C}^1$. The contribution of the inhomogeneity to the overall strain, per representative volume $V$ (the extra strain, as compared to the homogeneous matrix) is given by the fourth-rank tensor $H$ - the compliance contribution tensor of the inhomogeneity - defined by

$$
\Delta \boldsymbol{\varepsilon}=\boldsymbol{H}: \boldsymbol{\sigma}^{\infty}
\tag{2.1}
$$

where $\boldsymbol{\sigma}^{\infty}$ is the "remotely applied" stress field, that, in absence of the inhomogeneity, would have been uniform within its site ("homogeneous boundary conditions", Hill, 1963; Hashin, 1983); a colon denotes contraction over two indices. Similarly, the stiffness contribution tensor $\boldsymbol{N}$, dual to $H$, can be introduced:

$$
\Delta \boldsymbol{\sigma}=\boldsymbol{N}: \boldsymbol{\varepsilon}^{\infty}
\tag{2.2}
$$

where $\boldsymbol{\varepsilon}^{\infty}$ is the "remotely applied" strain. In the general case, the $\boldsymbol{H}$- and $\boldsymbol{N}$-tensors are interrelated as follows (Sevostianov & Kachanov, 2007):

$$
\boldsymbol{N}=-\boldsymbol{C}^{0}: \boldsymbol{H}: \boldsymbol{C}^{0}, \text { or, equivalently, } \boldsymbol{H}=-\boldsymbol{S}^{0}: \boldsymbol{N}: \boldsymbol{S}^{0}
\tag{2.3}
$$

Relations (2.3) hold for any shape of the inhomogeneity and for any values of the elastic constants, including cases of anisotropy. In the case of the isotropic matrix,

$$
-N_{i j k l}=\lambda_{0}^{2} H_{m m n n} \delta_{i j} \delta_{k l}+\mu_{0}^{2} H_{i j k l}+\lambda_{0} \mu_{0}\left(\delta_{i j} H_{m m k l}+\delta_{k l} H_{m m i j}\right)
\tag{2.4}
$$

where $\lambda_{0}$ and $\mu_{0}$ are Lame constants of the matrix.

For an ellipsoidal inhomogeneity, $\boldsymbol{H}$- and $\boldsymbol{N}$-tensors are given by (Sevostianov and Kachanov, 1998, Sevostianov & Kachanov, 2002):

$$
H=\frac{V^{*}}{V}\left[\left(\boldsymbol{S}^{*}-\boldsymbol{S}^{0}\right)^{-1}+\boldsymbol{Q}\right]^{-1}, \quad N=\frac{V^{*}}{V}\left[\left(\boldsymbol{C}^{*}-\boldsymbol{C}^{0}\right)^{-1}+\boldsymbol{P}\right]^{-1}
\tag{2.5}
$$

where fourth rank Hill's (1965) tensor $\boldsymbol{P}$ is expressed in terms of Green's tensor $G_{i j}(\boldsymbol{x})$ for unbounded isotropic elastic media

$$
G_{i j}(\boldsymbol{x})=\frac{1}{16 \pi G_{0}\left(1-v_{0}\right) x}\left[\left(3-4 v_{0}\right) \delta_{i j}+x_{i} x_{j} / x^{2}\right]
\tag{2.6}
$$

by relation

$$
P_{i j k l}(x)=\nabla_{j} \int_{V^{*}} \nabla_{l} G_{i k}(x-\xi) d\left.\xi\right|_{(i j)(k l)}, \quad x \in V^{*}
\tag{2.7}
$$

where parenthesis $(i j)$ means symmetrization with respect to indices $i$ and $j$. For an ellipsoidal inhomogeneity, tensor $\boldsymbol{P}$ is related to Eshelby's tensor $\boldsymbol{s}$ by:

$$
P_{i j k l}=s_{i j m n} S_{m n k l}^{0}
\tag{2.8}
$$

Tensor $\boldsymbol{Q}$ entering expression (2.6) for compliance contribution tensor can be expressed in terms of tensor $\boldsymbol{P}$ as follows (Hill, 1965; Walpole, 1969):

$$
Q_{i j k l}=C_{i j m n}^{0}\left(J_{m n k l}-P_{m n r s} C_{r s k l}^{0}\right)
\tag{2.9}
$$

Here, $J_{i j k l}=\left(\delta_{i k} \delta_{l j}+\delta_{i l} \delta_{k j}\right) / 2$ and the inverse $X_{i j k l}^{-1}$ of a symmetric fourth-rank tensor $X_{i j k l}$ is defined by $X_{i j m n}^{-1} X_{m n k l}=\left(X_{i j m n} X_{m n k l}^{-1}\right)=J_{i j k l}$.

The sums $\sum_{m} \boldsymbol{H}^{(m)}$ and $\sum_{m} \boldsymbol{N}^{(m)}$ constitute the proper microstructural parameters in whose terms the effective elastic properties have to be expressed (Kachanov & Sevostianov, 2005). This explains the key role of the property contribution tensors: it is *them* that have to be summed, or averaged - and not other tensors such as Eshelby's or Hill's tensors. For

the ellipsoidal shapes, compliance and stiffness contribution tensors can be expressed in terms of the latter ones; for non-ellipsoidal shapes, this is not the case and computational efforts should be focused on $\boldsymbol{H}$- and $\boldsymbol{N}$-tensors, as far as the effective elastic properties are concerned.

As shown by Sevostianov and Kachanov (2011), property contribution tensors play yet another important role: the far-field asymptotics of the elastic fields generated by an inhomogeneity determines its contribution to the effective elastic properties and vice versa. The latter result, in particular, allows application compliance contribution tensor to reformulate Maxwell's homogenization scheme, as will be shown in the next section.

### 3. Maxwell scheme in terms of compliance contribution tensor

Since compliance contribution tensor describes not only the contribution of the inhomogeneities into effective elastic properties, but also the far-fields generated by them, we can rewrite the Maxwell's scheme in terms of this tensor. Indeed, let us cut a representative volume element of volume $V^{*}$ from a composite (see Fig. 1) and place it into the matrix material. Effect produced by this element is described either by the sum of compliance contribution tensors of the inhomogeneities $\frac{1}{V} \sum_{i} V_{i} \boldsymbol{H}_{i}$ or by compliance contribution tensor $\boldsymbol{H}_{\text {eff }}$ of the entire RVE considered as an individual inhomogeneity with homogenized unknown properties. Equating these two quantities we have the general equation for the Maxwell scheme:

$$
\frac{V^{*}}{V} \boldsymbol{H}_{\mathrm{eff}}=\frac{1}{V} \sum_{i} V_{i} \boldsymbol{H}_{\boldsymbol{i}}
\tag{3.1}
$$

The right hand side of the equation is known, however, the left hand side reflects combined effect (1) of overall properties of the RVE and (2) of its shape. The main challenge in solving (3.1) is the separation of these effects that can be done analytically only in the case of the ellipsoidal shape of the RVE. Situation is complicated by the fact that this shape is not known a priori and has to be determined from the right hand side as well. This issue is closely related to the problem of average shape of a set of inhomogeneities discussed by Sevostianov and Kachanov (2012b).

Remark. Even in the case of isotropic orientation distribution of inhomogeneities, the question about shape of the RVE is not trivial. Since we are considering fourth-rank tensors, this figure may be any one bounded by a fourth order surface described as a linear combination of tensors $\delta_{i j} \delta_{k l}$ and $\left(\delta_{i k} \delta_{l j}+\delta_{i l} \delta_{k j}\right) / 2$. Only in the case when all the inhomogeneities are randomly oriented, the shape of the RVE is supposed to be spherical. This problem deserves more detailed study that is out of the scope of the present work

For ellipsoidal shapes of inhomogeneities, Eq. (3.1) can be written with the account of (2.5) as

$$
\frac{V}{V^{*}}\left[\left(\boldsymbol{S}_{\mathrm{eff}}-\boldsymbol{S}_{\boldsymbol{0}}\right)^{-1}+\boldsymbol{Q}_{\mathrm{reg}}\right]=V\left[\sum_{i} V_{i} \boldsymbol{H}_{\boldsymbol{i}}\right]^{-1}
\tag{3.2}
$$

where $Q_{\text {reg }}$ is tensor defined by (2.9) that reflects effect of shape of the RVE. Note that the right hand side in (3.2) represents change in effective compliance $S_{\text {eff }}-S_{0}$ calculated in the framework of non interaction approximation (Kachanov \& Sevostianov, 2005). After the inversion, (3.2) yields

$$
\boldsymbol{S}_{\mathrm{eff}}=\boldsymbol{S}_{\boldsymbol{0}}+\left\{\left[\frac{1}{V^{*}} \sum_{i} V_{i} \boldsymbol{H}_{\boldsymbol{i}}\right]^{-1}-\boldsymbol{Q}_{\mathrm{reg}}\right\}^{-1}
\tag{3.3}
$$

Eq. (3.3) is valid for inhomogeneities of *diverse shape*. For ellipsoidal shapes it coincides with the equation obtained by Levin et al. (2012) in much lengthier way. Tensor $Q_{\text {reg }}$ is the quantity that describes the difference between Maxwell's scheme and non-interaction approximation. Since it may be anisotropic, the interaction between inhomogeneities in different directions may be different. In the simplest cases of randomly oriented inhomogeneities or strictly parallel identical inhomogeneities, tensor $Q_{\text {reg }}$ in the first approximation will coincide with either one for sphere or for a representative inhomogeneity respectively. Note that mutual positions of the centers of inhomogeneities can also be taken into account through the shape of the RVE domain (and, therefore, through the symmetry of the tensor $Q_{\text {reg }}$ ). This effect, however, produces only minor effect (see, for example, book of Kanaun \& Levin, 2008) and we do not discuss it here in detail. Expressions for components of tensor $Q$ corresponding to a spheroidal domain are given in the Appendix (formulas (A.7)). In the next section we illustrate expression (3.3) on several examples.

### 4. Examples

In this section we specify result (3.3) for several simple cases corresponding to different microstructures.

### 4.1. Identical randomly oriented spheroidal pores

Since the elastic stiffness tensors entering (3.30) are isotropic, it is easier to write them in the orthogonal form (Walpole, 1984) to simplify the process of tensors inversion:

$$
\boldsymbol{S}_{\boldsymbol{0}}=\frac{1}{3 K_{0}}\left(\frac{1}{3} \boldsymbol{\Pi}\right)+\frac{1}{2 G_{0}}\left(\boldsymbol{J}-\frac{1}{3} \boldsymbol{\Pi}\right) ; \quad \boldsymbol{S}_{\mathrm{eff}}=\frac{1}{3 K_{\mathrm{eff}}}\left(\frac{1}{3} \boldsymbol{\Pi}\right)+\frac{1}{2 G_{\mathrm{eff}}}\left(\boldsymbol{J}-\frac{1}{3} \boldsymbol{\Pi}\right)
\tag{4.1}
$$

RVE has spherical shape (see Sevostianov & Kachanov, 2012a) and tensor $\boldsymbol{Q}_{\mathrm{reg}}$ can be written in the following form

$$
\boldsymbol{Q}_{\mathrm{reg}}=3 K_{0} \varphi_{K}\left(\frac{1}{3} \boldsymbol{\Pi}\right)+2 G_{0} \varphi_{G}\left(\boldsymbol{J}-\frac{1}{3} \boldsymbol{\Pi}\right)
\tag{4.2}
$$

where

$$
\varphi_{K}=\frac{2}{3} \frac{1-2 v_{0}}{1-v_{0}}, \quad \varphi_{G}=\frac{1}{15} \frac{7-5 v_{0}}{1-v_{0}}
\tag{4.3}
$$

To calculate term $\frac{1}{V^{r}} \sum_{i} V_{i} \boldsymbol{H}_{\boldsymbol{i}}$ we first note that tensor $\boldsymbol{H}_{\boldsymbol{i}}$ is the same for all the pores and therefore the summation in this term can be replaced by integration over all possible orientations of the spheroids. The integral was evaluated in the work of Sevostianov, Kováčik, and Simančík (2006) and can be written as

$$
\frac{1}{V^{r}} \sum_{i} V_{i} \boldsymbol{H}_{\boldsymbol{i}}=p B\left(\frac{1}{3} \boldsymbol{\Pi}\right)+p C\left(\boldsymbol{J}-\frac{1}{3} \boldsymbol{\Pi}\right)
\tag{4.4}
$$

where $p$ is porosity and coefficients $B$ and $C$ are expressed in terms of the components of the compliance contribution tensor as follows

$$
B\left(\gamma, v_{0}\right)=\frac{2\left(1+v_{0}\right)}{1-2 v_{0}} \frac{38 h_{1}-h_{2}+44 h_{3}+2 h_{5}+8 h_{6}}{30}, \quad C\left(\gamma, v_{0}\right)=\frac{2 h_{1}+11 h_{2}-4 h_{3}+8 h_{5}+2 h_{6}}{15}
\tag{4.5}
$$

Coefficients $h_{i}$ are given in the Appendix (formulas (A.12)) as functions of the aspect ratio of the spheroid.

Combining formulas (4.1)-(4.4), we get

$$
\boldsymbol{S}_{\mathrm{eff}}=\boldsymbol{S}_{\boldsymbol{0}}+\frac{1}{3 K_{0}}\left(\frac{p B\left(\gamma, v_{0}\right)}{1-p B\left(\gamma, v_{0}\right) \varphi_{K}}\right)\left(\frac{1}{3} \boldsymbol{\Pi}\right)+\frac{1}{2 G_{0}}\left(\frac{p C\left(\gamma, v_{0}\right)}{1-p C\left(\gamma, v_{0}\right) \varphi_{G}}\right)\left(\boldsymbol{J}-\frac{1}{3} \boldsymbol{\Pi}\right)
\tag{4.6}
$$

and the final results for effective bulk and shear moduli are as follows:

$$
\frac{K_{\mathrm{eff}}}{K_{0}}=\frac{1-p B\left(\gamma, v_{0}\right) \varphi_{K}}{1+p B\left(\gamma, v_{0}\right)\left[1-\varphi_{K}\right]}, \quad \frac{G_{\mathrm{eff}}}{G_{0}}=\frac{1-p C\left(\gamma, v_{0}\right) \varphi_{G}}{1+p C\left(\gamma, v_{0}\right)\left[1-\varphi_{G}\right]}
\tag{4.7}
$$

It is interesting to compare thus obtained results with experimental data. For this aim we use results of Sevostianov et al. (2006) for Young's modulus of aluminum foams $\left(E_{\text {eff }}=1 / S_{111}^{\text {eff }}\right)$. For solid aluminum, $v_{0}=0.33$, $E_{0}=70 \mathrm{GPa}$ and the pores

![](./images/813251085438287872_6.jpg)

Fig. 3. Young's modulus of closed cell aluminum foam as predicted by various micromechanical schemes in comparison with experimental data of Sevostianov et al. (2006). Inset shows typical microstructural pattern of the material.

are modeled as spheroids with the aspect ratio 0.7. Note that the latter approximation is rather rough as can be seen in the inset of Fig. 3. Using relations between isotropic elastic constants, we get from (4.6) that

$$
\frac{1}{E_{\text {eff }}}=\frac{1}{E_{0}}\left[1+\frac{1-2 v_{0}}{3}\left(\frac{p B\left(\gamma, v_{0}\right)}{1-p B\left(\gamma, v_{0}\right) \varphi_{K}}\right)+\frac{2\left(1+v_{0}\right)}{3}\left(\frac{p C\left(\gamma, v_{0}\right)}{1-p C\left(\gamma, v_{0}\right) \varphi_{G}}\right)\right] \tag{4.8}
$$

Fig. 3 illustrates comparison of the Young's modulus calculated by generalized Maxwell's scheme with experimental measurements. For comparison, we calculate effective Young's modulus by various approximate schemes mentioned in the introduction as well. Results predicted by Maxwell's model coincide with the ones calculated by Kanaun and Levin scheme (see also discussion of Levin et al., 2012 on this subject) and are very close to calculations by Mori-Tanaka's scheme. However, the basic idea and the process of derivation of Maxwell's scheme is (a) simpler and more transparent than in the Kanaun-Levin variant of the effective field method (see book of Kanaun & Levin, 2008) and (b) does not lead to any inconsistencies for multiphase composites as Mori-Tanaka scheme (see Qui & Weng, 1990 & Ferrari, 1991).

Remark. Results of the present section can be easily generalized to the case of a material containing spheroidal inhomogeneities. For this goal components $h_{i}$ in formulas (4.5) has to be calculated by formula (A.10).

### 4.2. Several families of randomly oriented spheroidal inhomogeneities

This case is probably the most challenging one in the theory of effective properties – most of the theories lead to either inconsistent results or to systems of equations that cannot be solved analytically. Maxwell's method, in contrast, does not produce any complications of this sort. Indeed, tensor $\mathbf{Q}_{\text {reg }}$ is independent of the shape and properties of individual inhomogeneities and tensor $\frac{1}{V^{*}} \sum_{i} V_{i} \boldsymbol{H}_{i}$ is calculated in the framework of non-interaction approximation, where diversity of shapes and properties of inhomogeneities can be accounted for in a straightforward way.

Below we consider an example of a shale type rock (argillite) that represents clay mineral matrix containing three families of randomly oriented inhomogeneities that we model as oblate pores of aspect ratio 0.05, prolate calcite inhomogeneities of aspect ratio 10.0 and approximately spherical inhomogeneities of quartz (Fig. 4). Content of calcite particles in argillite varies from 0.20 to 0.27, content of quartz inclusions varies from 0.23 to 0.25, and porosity varies from 0.1 to 0.2. Young's moduli of clay, calcite and quartz are $E_{0}=3 \mathrm{GPa}, E_{c}=95 \mathrm{GPa}$, and $E_{q}=101 \mathrm{GPa}$, respectively. The Poisson's ratios are $v_{0}=0.3, v_{c}=0.27$, and $v_{q}=0.06$ (Shen, Shao, Kondo, & Gatmiri, 2012). Overall properties of this composite are isotropic as dictated by its microstructure so that tensor $\mathbf{Q}_{\text {reg }}$ can be calculated by (4.2). Formula (4.4) can be rewritten as

$$
\frac{1}{V^{*}} \sum_{i} V_{i} \boldsymbol{H}_{i}=\left(c_{p} B_{p}+c_{c} B_{c}+c_{q} B_{q}\right)\left(\frac{1}{3} \boldsymbol{I}\right)+\left(c_{p} C_{p}+c_{c} C_{c}+c_{q} C_{q}\right)\left(\boldsymbol{J}-\frac{1}{3} \boldsymbol{I}\right) \tag{4.9}
$$

![](./images/813251085438287872_7.jpg)

Fig. 4. Microstructure of a shale type rock (argillite): clay mineral matrix contains (CM) containes oblate pores (P), prolate calcite inhomogeneities (Cal) and inclusions of quartz (Q) of approximately spherical shape.

Where $c$ denotes partial volume concentration of each type of inhomogeneities and sub-indices $p$, $c$, and $q$ indicate pores, calcite inhomogeneities and quartz inhomogeneities respectively. Coefficients $B$ and $C$ in(4.9) have to be calculated by (4.5) with $h_i$ given by (A.10) for calcite and quartz inhomogeneities and by (A.12) for pores. Finally, effective bulk and shear moduli of the composite are given in the Maxwell's homogenization scheme by the following simple formulas

$$
\begin{aligned}
\frac{K_{\mathrm{eff}}}{K_{0}} & =\frac{1-\varphi_{K}\left(v_{0}\right)\left(c_{p} B_{p}+c_{c} B_{c}+c_{q} B_{q}\right)}{1+\left[1-\varphi_{K}\left(v_{0}\right)\right]\left(c_{p} B_{p}+c_{c} B_{c}+c_{q} B_{q}\right)} \\
\frac{G_{\mathrm{eff}}}{G_{0}} & =\frac{1-\varphi_{G}\left(v_{0}\right)\left(c_{p} C_{p}+c_{c} C_{c}+c_{q} C_{q}\right)}{1+\left[1-\varphi_{G}\left(v_{0}\right)\right]\left(c_{p} C_{p}+c_{c} C_{c}+c_{q} C_{q}\right)}
\end{aligned} \tag{4.10}
$$

Fig. 5 illustrates dependences of the bulk and shear moduli on the overall porosity at different levels of the volume fraction of calcite and fixed content of quartz 0.24.

### 4.3. Effect of orientation distribution of the inhomogeneities

As the last example, let us illustrate the applicability of Maxwell's scheme to a material containing non-spherical inhomogeneities with certain orientation distribution. Probably, the most transparent illustration can be provided by a material containing circular cracks with preferential orientation. Randomly oriented circular cracks are characterized by the crack density parameter introduced by Bristow (1960)

$$
\rho=\frac{1}{V} \sum a^{(k) 3} \tag{4.11}
$$

where $a^{(k)}$ is radius of the $k$th microcrack. In the cases of non-random crack orientations, parameter $\rho$ should be replaced by symmetric second rank crack density tensor (Kachanov, 1980)

$$
\alpha_{i j}=\frac{1}{V} \sum\left(a^{3} n_{i} n_{j}\right)^{(k)} \tag{4.12}
$$

where $n^{(k)}$ is a unit normal to $k$th microcrack. In the case of randomly oriented cracks, $\alpha_{i j}=(\rho / 3) \delta_{i j}$.

For calculation of the effective elastic properties of a microcracked material in the case of non-random crack orientations, yet another parameter of crack density is required – a fourth rank tensor. However, the dependence of the effective elastic moduli on this parameter is relatively weak, and can be neglected with sufficient accuracy (Kachanov, 1994). Then tensor $\frac{1}{V^{*}} \sum_{i} V_{i} \boldsymbol{H}_{\boldsymbol{i}}$ is replaced by

$$
\left[\frac{1}{V^{*}} \sum_{i} V_{i} \boldsymbol{H}_{\boldsymbol{i}}\right]_{i j k l} \approx \frac{4\left(1-v_{0}\right)}{3\left(2-v_{0}\right) G_{0}}\left(\delta_{i k} \alpha_{j l}+\delta_{i l} \alpha_{j k}+\delta_{j k} \alpha_{i l}+\delta_{j l} \alpha_{i k}\right) \tag{4.13}
$$

Note that while $V_i \to 0$ for the microcracks, some components of tensor $\boldsymbol{H}$ become infinite in this limit. Their product, however is finite and described by (4.13).

In the case of transverse isotropy, the crack density tensor reduces to two components $\alpha_{11}=\alpha_{22}$ and $\alpha_{33}$. We consider a set of circular microcracks that tend to be normal to $x_3$-axis with certain orientation scatter that may produce a significant impact on the values of $\alpha_{11}$ and $\alpha_{33}$. We describe the orientation distribution by the following function, containing scatter parameter $\lambda$ (see Sevostianov & Kachanov, 2009):

$$
P_{\lambda}(\varphi)=\frac{1}{2 \pi}\left[\left(\lambda^{2}+1\right) e^{-\lambda \varphi}+\lambda e^{-\lambda \pi / 2}\right] \tag{4.14}
$$

![](./images/813251085438287872_8.jpg)

Fig. 5. Normalized effective bulk and shear moduli of argillite as functions of porosity $c_p$ at three different volume concentrations $c_c$ of calcite and fixed content of quartz $c_q$ = 0.24.

Where $\varphi$ is the angle between normal to the crack surface and $x_3$-axis. The extreme cases of perfectly parallel and random orientations correspond to $\lambda = \infty$ and $\lambda = 0$, respectively. Fig. 6a shows orientational patterns that correspond to several values of $\lambda$. Components $\alpha_{11}$ and $\alpha_{33}$ are expressed in terms of $\rho$ given by (4.11) as follows:

$$
\alpha_{11}=\alpha_{22}=\frac{18-\lambda\left(\lambda^{2}+3\right) e^{-\lambda \pi / 2}}{6\left(\lambda^{2}+9\right)} \rho, \quad \alpha_{33}=\frac{\left(\lambda^{2}+3\right)\left(3+\lambda e^{-\lambda \pi / 2}\right)}{3\left(\lambda^{2}+9\right)} \rho
\tag{4.15}
$$

Fig. 6b and c illustrate dependences of $\alpha_{11}$ and $\alpha_{33}$ on $\lambda$ at several values of the crack density $\rho$.

We took the shape of the representative volume element for Maxwell's scheme as an oblate spheroid with the aspect ratio $\gamma$ determined by

$$
\gamma=\alpha_{11} / \alpha_{33}=\frac{18-\lambda\left(\lambda^{2}+3\right) e^{-\lambda \pi / 2}}{2\left(\lambda^{2}+3\right)\left(3+\lambda e^{-\lambda \pi / 2}\right)} \leqslant 1
\tag{4.16}
$$

Note again that the problem about the shape of the RVE is still open.

Calculation of the components of tensor $\mathbf{Q}_{\text {reg }}$ by formulas (A.7) with $\gamma$ taken from (4.16) yields the following relation for the components of the tensor of effective elastic compliances in terms of the crack density tensor.

$$
\begin{aligned}
S_{1111} & =S_{1111}^{0}+\phi \alpha_{11}\left[\frac{1-2 \phi \alpha_{33} q_{6}(\gamma)}{D}+\frac{1}{1-2 \phi \alpha_{11} q_{2}(\gamma)}\right] \\
S_{3333} & =S_{3333}^{0}+2 \phi \alpha_{33}\left[\frac{1-4 \phi \alpha_{11} q_{1}(\gamma)}{D}\right] \\
S_{1212} & =S_{1212}^{0}+\frac{1 \phi \alpha_{11}}{1-2 \phi \alpha_{11} q_{2}(\gamma)} ; \quad S_{1313}=S_{1313}^{0}+\frac{4 \phi\left(\alpha_{11}+\alpha_{33}\right)}{2-\phi q_{5}(\gamma)\left(\alpha_{11}+\alpha_{33}\right)} \\
S_{1133} & =S_{1133}^{0}+\frac{4 \phi^{2} \alpha_{11} \alpha_{33} q_{3}(\gamma)}{\Delta}
\end{aligned}
\tag{4.17}
$$

where

$$
\begin{aligned}
\phi & =\frac{2\left(4-v_{0}\right)}{3\left(2-v_{0}\right) G_{0}} ; \\
\Delta & =1-2 \phi\left(2 \alpha_{11} q_{1}(\gamma)+\alpha_{33} q_{6}(\gamma)\right)+8 \phi^{2} \alpha_{11} \alpha_{33}\left(q_{1}(\gamma) q_{6}(\gamma)-q_{3}(\gamma) q_{4}(\gamma)\right)
\end{aligned}
$$

Fig. 7 illustrates behavior the normalized effective elastic compliances as functions of the scatter parameter $\lambda$ at several values of the crack density $\rho$.

For the case of randomly oriented circular cracks when $\lambda$ in (4.14) approaches zero, shape of the RVE is spherical and overall properties are isotropic, bulk and shear moduli are expressed in terms of the scalar crack density parameter $\rho=(1 / V) \sum a_{i}^{3}$ ($a_i$ is $i$th crack radius and $V$ is the representative volume)

![](./images/813251085438287872_9.jpg)

Fig. 6. (a) Dependence of the orientation distribution function $P_{\lambda}$ on angle $\varphi$ at several values of $\lambda$ and the corresponding orientation patterns. (b, c) Dependence of the components of crack density tensor on scatter parameter $\lambda$ at different values of the overall crack density $\rho$.

![](./images/813251085438287872_10.jpg)

Fig. 7. Normalized effective elastic compliances as functions of the scatter parameter $\lambda$ at different values of the overall crack density$\rho$: (a) $S_{1111}/S_{1111}^0$; (b) $S_{3333}/S_{3333}^0$; (c) $S_{1212}/S_{1212}^0$; (d) $S_{1313}/S_{1313}^0$.

$$
\frac{K_{\mathrm{eff}}}{K_{0}}=\frac{1-\rho B_{c r} \varphi_{K}}{1+\rho B_{c r}\left[1-\varphi_{K}\right]} \quad \frac{G_{\mathrm{eff}}}{G_{0}}=\frac{1-\rho C_{c r} \varphi_{G}}{1+\rho C C_{c r}\left[1-\varphi_{G}\right]}
\tag{4.18}
$$

where coefficients $B_{cr}$ and $C_{cr}$ have been obtained by Bristow (1960) as

$$
B_{c r}=\frac{16}{9} \frac{1-v_{0}^{2}}{1-2 v_{0}} ; \quad C_{c r}=\frac{32}{45} \frac{\left(1-v_{0}\right)\left(5-v_{0}\right)}{2-v_{0}}
\tag{4.19}
$$

Fig. 8 illustrates comparison of the elastic moduli calculated by (4.18) with ones obtained by other micromechanical models discussed in the Introduction – self-consistent scheme, Mori–Tanak scheme (that coincides with the non-interaction approximation), differential scheme and Kanaun–Levin scheme.

![](./images/813251085438287872_11.jpg)

Fig. 8. Normalized effective (a) bulk and (b) shear moduli of a material containing randomly oriented microcracks as functions of scalar crack density parameter. Calculations are done by (1) Maxwell scheme (formulas 4.19), (2) differential scheme (Hashin, 1988), and (3) non-interaction approximation (Bristow, 1960) that coincides with Mori-Tanaka scheme.

### 4.4. Material containing superspherical pores

In this subsection, we illustrate how the Maxwell method formulated in terms of property contribution tensors (3.3) can be applied to a material containing non-ellipsoidal inhomogeneities. We consider a pore having a shape of a supersphere of unit radius $(x)^{2\alpha}+(y)^{2\alpha}+(z)^{2\alpha}=1$ and use approximate formulas for components of the compliance contribution tensor recently obtained by the authors (Sevostianov & Giraud, 2012). Example of this shape is shown in Fig. 9a for $\alpha=0.35$. Parameter $\alpha$ may be called concavity factor or a parameter of deviation from spherical shape. When $\alpha=1$, the supersphere is transformed to ordinary sphere. For $\alpha>0.5$, its shape is convex, for $\alpha<0.5$ it is concave. Concave superspherical pores are typical, for example for geomaterials and for sintered ceramics.

Components of the compliance contribution tensor for a concave superspherical pore have the following form

$$
\begin{aligned}
E_{0} H_{1111} & =\frac{3\left(1-v_{0}\right)\left(9+5 v_{0}\right)}{2\left(7-5 v_{0}\right)} \xi ; \quad E_{0} H_{1122}=-\frac{3\left(1-v_{0}\right)\left(1+5 v_{0}\right)}{2\left(7-5 v_{0}\right)} \xi \\
E_{0} H_{1212} & =\frac{15\left(1-v_{0}^{2}\right)}{2\left(7-5 v_{0}\right)} \xi
\end{aligned}
\tag{4.20}
$$

where microstructural parameter

$$
\xi=\frac{2 \pi \alpha^{3} \Gamma(3 / 2 \alpha)}{[\Gamma(1 / 2 \alpha)]^{3}}
\tag{4.21}
$$

describes pore shape. Then, for randomly oriented superspherical pores of total porosity $p$

$$
\frac{1}{V^{*}} \sum_{i} V_{i} \boldsymbol{H}_{i}=\frac{p \xi B}{3 K_{0}}\left(\frac{1}{3} \boldsymbol{I I}\right)+\frac{p \xi C}{2 G_{0}}\left(\boldsymbol{J}-\frac{1}{3} \boldsymbol{I I}\right)
\tag{4.22}
$$

where

$$
B=\frac{3}{2} \frac{1-v_{0}}{1-2 v_{0}} ; \quad C=\frac{15\left(1-v_{0}\right)}{7-5 v_{0}}
\tag{4.23}
$$

and effective elastic properties of the material are given by formulas similar to (4.7)

$$
\frac{K_{\text {eff }}}{K_{0}}=\frac{1-p \xi B \varphi_{K}}{1+p \xi B\left[1-\varphi_{K}\right]}, \quad \frac{G_{\text {eff }}}{G_{0}}=\frac{1-p \xi C \varphi_{G}}{1+p \xi C\left[1-\varphi_{G}\right]}
\tag{4.24}
$$

Fig. 9b illustrates behavior the effective moduli for different values of $\alpha$.

![](./images/813251085438287872_12.jpg)

Fig. 9. Normalized effective (a) bulk and (b) shear moduli of a material containing multiple randomly oriented superspherical pores calculated by (4.24) for different values of concavity factor $\alpha$. Figure (c) illustrates shape of a supersphere $(\alpha=0.35)$ and the ratio of the volumes of ordinary sphere $V_{0}$ and supersphere $V_{*}$ as a function of $\alpha$.

## 5. Concluding remarks

In this paper, we re-visited Maxwell's (1873) method of homogenization specifying it for effective elastic properties of composites. Maxwell's scheme that equates the far field produced by a set of inhomogeneities to the far field produced by a fictitious domain with unknown effective properties is re-written in terms of compliance contribution tensors according to recent results of Sevostianov and Kachanov (2011). Explicit formula for tensor of effective elastic compliances has been derived for the case when the shape of the fictitious domain can be chosen as ellipsoidal. The developed method is exceptionally convenient for calculation of the effective properties of multiphase heterogeneous materials. On one side it is simple enough to be used in applications (the final formulas are obtained in closed explicit form) and, at the same time, the method produces physically consistent results and shows good predictive accuracy. The approach is illustrated by four examples – material containing multiple identical spheroidal pores, material containing three families of inhomogeneities having different shapes and properties, material containing circular cracks that have preferential orientation with certain orientation scatter (this example is also supplemented by comparison with other micromechanical schemes for the case of randomly oriented microcracks), and material containing randomly-oriented non-ellipsoidal (concave superspherical) pores. Note, that presently this approach is the only one that allows to calculate effective properties of composites with non-ellipsoidal inhomogeneities.

## Acknowledgement

The financial support of Labex ANR-10-LABX-21 Ressources21 (Rare metal rough materials of 21th century) and New Mexico Space Grant Consortium is gratefully acknowledged.

## Appendix A

In this appendix we outline a convenient technique of analytic inversion and multiplication of $4^{\text{th}}$ rank tensors with transversely-isotropic symmetry. It is based on expressing tensors in “standard” tensor bases (Kunin, 1983; Walpole, 1984). In the case of the transversely isotropic elastic symmetry, the following basis is most convenient (Kanaun & Levin, 2008):

$$
\begin{aligned}
T_{ijkl}^{(1)} &= \theta_{ij}\theta_{kl}, \quad T_{ijkl}^{(2)} = (\theta_{ik}\theta_{lj} + \theta_{il}\theta_{kj} - \theta_{ij}\theta_{kl})/2, \quad T_{ijkl}^{(3)} = \theta_{ij}m_{k}m_{l}, \quad T_{ijkl}^{(4)} = m_{i}m_{j}\theta_{kl} \\
T_{ijkl}^{(5)} &= (\theta_{ik}m_{l}m_{j} + \theta_{il}m_{k}m_{j} + \theta_{jk}m_{l}m_{i} + \theta_{jl}m_{k}m_{i})/4, \quad T_{ijkl}^{(6)} = m_{i}m_{j}m_{k}m_{l}
\end{aligned} \tag{A.1}
$$

where $\theta_{ij} = \delta_{ij} - m_{i}m_{j}$ and $\boldsymbol{m} = m_{1}\boldsymbol{e}_{1} + m_{2}\boldsymbol{e}_{2} + m_{3}\boldsymbol{e}_{3}$ is a unit vector along the axis of transverse symmetry.

These tensors form a closed algebra with respect to the operation of (non-commutative) multiplication (contraction over two indices):

$$
\left(\boldsymbol{T}^{(\alpha)} \boldsymbol{T}^{(\beta)}\right)_{ijkl} = T_{ijpq}^{(\alpha)} T_{pqkl}^{(\beta)} \tag{A.2}
$$

Then the inverse of any fourth rank tensor $\boldsymbol{X}$, as well as the product $\boldsymbol{X}:\boldsymbol{Y}$ of two such tensors are readily found in the closed form, as soon as the representations in the basis

$$
\boldsymbol{X} = \sum_{k=1}^{6} X_{k} \boldsymbol{T}^{(k)}, \quad \boldsymbol{Y} = \sum_{k=1}^{6} Y_{k} \boldsymbol{T}^{(k)} \tag{A.3}
$$

are established. Indeed:

(a) inverse tensor $\boldsymbol{X}^{-1}$ defined by $X_{ijmn}^{-1} X_{mnkl} = \left(X_{ijmn} X_{mnkl}^{-1}\right) = J_{ijkl}$ is given by

$$
\boldsymbol{X}^{-1} = \frac{X_{6}}{2\Delta} T^{(1)} + \frac{1}{X_{2}} T^{(2)} - \frac{X_{3}}{\Delta} T^{(3)} - \frac{X_{4}}{\Delta} T^{(4)} + \frac{4}{X_{5}} T^{(5)} + \frac{2X_{1}}{\Delta} T^{(6)} \tag{A.4}
$$

where $\Delta = 2(X_{1}X_{6} - X_{3}X_{4})$.

(b) product of two tensors $\boldsymbol{X}:\boldsymbol{Y}$ (tensor with $ijkl$ components equal to $X_{ijmn}Y_{mnkl}$) is

$$
\boldsymbol{X}:\boldsymbol{Y} = (2X_{1}Y_{1} + X_{3}Y_{4})\boldsymbol{T}^{(1)} + X_{2}Y_{2}\boldsymbol{T}^{(2)} + (2X_{1}Y_{3} + X_{3}Y_{6})\boldsymbol{T}^{(3)} + (2X_{4}Y_{1} + X_{6}Y_{4})\boldsymbol{T}^{(4)} + \frac{1}{2}X_{5}Y_{5}\boldsymbol{T}^{(5)} + (X_{6}Y_{6} + 2X_{4}Y_{3})\boldsymbol{T}^{(6)} \tag{A.5}
$$

General transversely isotropic fourth-rank tensor, being represented in this basis

$$
\Psi_{ijkl} = \sum \psi_{m} T_{ijkl}^{m}
$$

has the following components:

$$
\begin{align*}
\psi_1 &= (\Psi_{1111} + \Psi_{1122})/2; \quad \psi_2 = 2\Psi_{1212}; \quad \psi_3 = \Psi_{1133}; \quad \psi_4 = \Psi_{3311}; \\
\psi_5 &= 4\Psi_{1313}; \quad \psi_6 = 4\Psi_{3333}
\end{align*}
\tag{A.6}
$$

Tensor $\boldsymbol{Q}$ given by (2.9), in the case of a spheroidal inhomogeneity ($a_1 = a_2 = a$) of aspect $\gamma = a/a_3$, has the following components (see, for example, Sevostianov & Kachanov, 2002):

$$
\begin{align*}
q_1 &= \mu[4\kappa - 1 - 2(3\kappa - 1)f_0 - 2f_1], \quad q_2 = 2\mu[1 - (2 - \kappa)f_0 - f_1] \\
q_3 &= q_4 = 2\mu[(2\kappa - 1)f_0 + 2f_1], \quad q_5 = 4\mu[f_0 + 4f_1], \quad q_6 = 8\mu[\kappa f_0 - f_1]
\end{align*}
\tag{A.7}
$$

where $\kappa = 1/[2(1 - v)]$ and functions $f_0$ and $f_1$ are given by

$$
f_0 = \frac{1 - g}{2(1 - \gamma^2)}, \quad f_1 = \frac{1}{4(1 - \gamma^2)^2}\left[(2 + \gamma^2)g - 3\gamma^2\right]
\tag{A.8}
$$

where

$$
g(\gamma) =
\begin{cases}
\frac{\gamma^2}{\sqrt{\gamma^2 - 1}} \arctan \sqrt{\gamma^2 - 1}, & \text{oblate spheroid, } \gamma \geqslant 1 \\
\frac{\gamma^2}{2\sqrt{1 - \gamma^2}} \ln \frac{1 + \sqrt{1 - \gamma^2}}{1 - \sqrt{1 - \gamma^2}}, & \text{prolate spheroid, } \gamma \leqslant 1
\end{cases}
\tag{A.9}
$$

Factors entering the representation of the compliance contribution tensor $\boldsymbol{H}$ of the spheroidal inhomogeneity with bulk and shear moduli $K_1$ and $G_1$, in terms of the tensor basis are given by (Sevostianov & Kachanov, 1999, 2002):

$$
\begin{align*}
h_1 &= \frac{1}{2\Delta}\left[\delta K_1 + \frac{4}{3}\delta G_1 + q_6\right]; \quad h_2 = \frac{1}{2\delta G + q_2}; \quad h_5 = \frac{4}{4\delta G_1 + q_5} \\
h_3 &= h_4 = -\frac{1}{\Delta}\left[\delta K - \frac{2}{3}\delta G + q_3\right]; \quad h_6 = \frac{2}{\Delta}\left[\delta K_1 + \frac{1}{3}\delta G_1 + q_1\right]
\end{align*}
\tag{A.10}
$$

where the following notations are used

$$
\begin{align*}
\delta K &= K_1 G_0/(K_0 - K_1); \quad \delta G = G_1 G_0/(G_0 - G_1) \\
\Delta &= 2\left[3\delta G \delta K + \delta K(q_1 + q_6 - 2q_3) + \frac{\delta G}{3}(4q_1 + q_6 + 4q_3) + G(q_1 q_6 - q_3^2)\right].
\end{align*}
\tag{A.11}
$$

In the case of spheroidal pores, (A.10) are reduced to (Sevostianov et al., 2006)

$$
\begin{align*}
h_1 &= \frac{\kappa(f_0 - f_1)}{2(4\kappa - 1)\left[2\kappa(f_0 - f_1) - (4\kappa - 1)f_0^2\right]}; \quad h_2 = \frac{1}{2\left[1 - (2 - \kappa)f_0 - \kappa f_1\right]}; \\
h_3 &= h_4 = \frac{-(2\kappa f_0 - f_0 + 2\kappa f_1)}{4(4\kappa - 1)\left[2\kappa(f_0 - f_1) - (4\kappa - 1)f_0^2\right]}; \\
h_5 &= \frac{4}{4[f_0 + 4\kappa f_1]}; \quad h_6 = \frac{4\kappa - 1 - 6\kappa f_0 + 2f_0 - 2\kappa f_1}{4(4\kappa - 1)\left[2\kappa(f_0 - f_1) - (4\kappa - 1)f_0^2\right]},
\end{align*}
\tag{A.12}
$$

where functions $f_0$ and $f_1$ are given by (A.8).

## References

Benveniste, Y. (1986). On the Mori-Tanaka method for cracked solids. *Mechanics Research Communications*, 13(4), 193-201.

Bristow, J. R. (1960). Microcracks, and the static and dynamic elastic constants of annealed heavily cold-worked metals. *British Journal of Applied Physics*, 11, 81-85.

Bruggeman, D. A. G. (1935). Berechnung verschiedener physikalisher Konstanten von heterogenen Substanzen. I. Dielectrizitätkonstanten und Leitfähigkeiten der Mischkörper aus isotropen Substanzen. *Ann Physik Leipzig*, 24, 636-679.

Bruggeman, D. A. G. (1937). Berechnung verschiedener physikalisher Konstanten von heterogenen Substanzen. III. Die elastische Konstanten der Quaiisotropen Mischkörper aus isotropen Substanzen. *Ann Physik Leipzig*, 29, 160-178.

Budiansky, B. (1965). On the elastic moduli of some heterogeneous materials. *Journal of the Mechanics and Physics of Solids*, 13, 223-227.

Christensen, R. C., & Loo, L. K. (1979). Solution for effective shear properties in three phase and cylinder models. *Journal of the Mechanics and Physics of Solids*, 27, 315-330.

Clausius, R. (1879). Die mechanische Behandlung der Elektricität, Vieweg. *Braunschweig*.

Ferrari, M. (1991). Asymmetry and high concentration limit of the Mori-Tanaka effective medium theory. *Mechanics of Materials*, 11, 251-256.

Hashin, Z. (1983). Analysis of composite materials - a survey. *Journal of Applied Mechanics*, 50, 481-505.

Hashin, Z. (1988). The differential scheme and its application to cracked materials. *Journal of the Mechanics and Physics of Solids*, 36, 719-734.

Hashin, Z., & Shtrikman, S. (1962). A variational approach to the theory of the effective magnetic permeability of multiphase materials. *Journal of Applied Physics*, 33, 3125-3131.

Hill, R. (1963). Elastic properties of reinforced solids: some theoretical principles. *Journal of the Mechanics and Physics of Solids*, 11, 357-372.

Hill, R. (1965). A self-consistent mechanics of composite materials. *Journal of the Mechanics and Physics of Solids*, 11, 357-372.

Jeffrey, D. J. (1973). Conduction through a random suspension of spheres. *Proceedings of Royal Society of London, A*, 335, 355-367.

Kachanov, M. (1980). Continuum model of medium with cracks. *Journal of Engineering Mechanics Division, ASCE*, 106, 1039-1051.

Kachanov, M. (1994). Elastic solids with many cracks and related problems. In J. Hutchinson & T. WuAdvances (Eds.). Applied Mechanics (vol. 30, pp. 256-426). Academic Press.

Kachanov, M., & Sevostianov, I. (2005). On quantitative characterization of microstructures and effective properties. International Journal of Solids and Structures, 42, 309-336.

Kachanov, M., Tsukrov, I., & Shafiro, B. (1994). Effective moduli of solids with cavities of various shapes. Applied Mechanics Reviews, 47(1), S151-S174.

Kanaun, S. K., & Jeulin, D. (2001). Elastic properties of hybrid composites by the effective field approach. Journal of the Mechanics and Physics of Solids, 49, 2339-2367.

Kanaun, S. K., & Levin, V. M. (1994). The self-consistent field method in mechanics of matrix composite materials. In K. Z. Markov (Ed.), Advances in mathematical modelling of composite materials (pp. 1-58). Singapoure: World Scientific Publ..

Kanaun, S. K., & Levin, V. M. (2008). Self-consistent methods for composites. Static Problems (vol. 1). Springer.

Kerner, E. H. (1956). The elastic and thermoelastic properties of composite media. Proceedings of the Physical Society B, 808-813.

Kröner, E. (1958). Berechnung der elastischen Konstanten des Vielkristalls aus den Konstanten des Einkristalls. Zeitschrift fur Physik, 151, 504-518.

Kunin, I. A. (1983). Elastic media with microstructure. Berlin: Springer Verlag.

Kuster, G. T., & Töksöz, M. N. (1974). Velocity and attenuation of seismic waves in two-phase media, I. Theoretical formulations. Geophysics, 39, 587-606.

Levin, V., Kanaun, S., & Markov, M. (2012). Generalized Maxwell's scheme for homogenization of poroelastic composites. International Journal of Engineering Science, 61, 75-86.

Markov, K. Z. (2000). Elementary micromechanics of heterogeneous media. In K. Z. Markov & L. Preziozi (Eds.), Heterogeneous media: Micromechanics modeling methods and simulations (pp. 1-62). Boston: Birkhauser.

Maxwell, J. C. (1873). A treatise on electricity and magnetism. Oxford: Clarendon Press.

McCartney, L. N. (2010). Maxwell's far-field methodology predicting elastic properties of multiphase composites reinforced with aligned transversely isotropic spheroids. Philosophical Magazine, 90, 4175-4207.

McCartney, L. N., & Kelly, A. (2008). Maxwell's far-field methodology applied to the prediction of properties of multi-phase isotropic particulate composites, In Proceedings of the Royal Society of London A, 464, 423-446.

McLaughlin, R. (1977). A study of the differential scheme for composite materials. International Journal of Engineering Science, 15, 237-244.

Milton, G. W. (2002). The theory of composites. Cambridge University Press.

Mogilevskaya, S. G., Stolarski, H. K., & Crouch, S. L. (2012). On Maxwell's concept of equivalemt inhomogeneity: when do the interactions matter? Journal of the Mechanics and Physics of Solids, 60, 391-417.

Mori, T., & Tanaka, K. (1973). Average stress in matrix and average elastic energy of materials with misfitting inclusions. Acta Metallurgica, 21, 571-574.

Qui, Y., & Weng, G. J. (1990). On the application of Mori-Tanaka's theory involving transversely isotropic spheroidal inclusions. International Journal of Engineering Science, 28, 1121-1137.

Rayleigh, Lord (1892). On the influence of obstacles arranged in rectangular order upon the volume properties of a medium. Philosophical Magazine, 34, 481-502.

Sevostianov, I., & Kachanov, M. (2012a). On differences between the non-interaction approximation and the "dilute limit" in theories of effective properties. International Journal of Engineering Science, 58, 124-128.

Sevostianov, I., & Kachanov, M. (2012b). Is the concept of "average shape" for a mixture of inclusions of diverse shapes legitimate? International Journal of Solids and Structures, 49, 3242-3254.

Sevostianov, I., & Giraud, A. (2012). On the compliance contribution tensor for a concave superspherical pore. International Journal of Fracture, 177, 199-206.

Sevostianov, I., & Kachanov, M. (1999). Compliance tensor of ellipsoidal inclusion. International Journal of Fracture, 96, L3-L7.

Sevostianov, I., & Kachanov, M. (2002). Explicit cross-property correlations for anisotropic two-phase composite materials. Journal of the Mechanics and Physics of Solids, 50, 253-282.

Sevostianov & Kachanov (2007). Relations between compliances of inhomogeneities having the same shape but different elastic constants. International Journal of Engineering Science, 45, 797-806.

Sevostianov, I., & Kachanov, M. (2009). Elastic and conductive properties of plasma-sprayed ceramic coatings in relation to their microstructure - an overview. Journal of Thermal Spray Technology, 18, 822-834.

Sevostianov, I., & Kachanov, M. (2011). Elastic fields generated by inhomogeneities: Far-field asymptotics, its shape dependence and relation to the effective elastic properties. International Journal of Solids and Structures, 48, 2340-2348.

Sevostianov, I., Kováčik, J., & Simančík, F. (2006). Elastic and electric properties of closed-cell aluminum foams cross-property connection. Materials Science and Engineering, A-420, 87-99.

Shen, W. Q., Shao, J. F., Kondo, D., & Gatmiri, B. (2012). A micro-macro model for clayey rocks with a plastic compressible porous matrix. International Journal of Plasticity, 36, 64-85.

Skorohod, V. V. (1961). Calculation of the effective isotropic moduli of disperse solid systems. Poroshkovaja Metallurgija (Powder Metallurgy), #1, 50-55 (in Russian).

Vavakin, A. S. & Salganik, R. L. (1975). Effective characteristics of nonhomogeneous media with isolated inhomogeneities. Mech. of Solids, 10, 65-75 (English transl. of Izvestia AN SSSR, Mekhanika Tverdogo Tela).

Walpole, L. J. (1969). On the overall elastic moduli of composite materials. Journal of the Mechanics and Physics of Solids, 17, 235-251.

Walpole, L. J. (1984). Fourth-rank tensors of the thirty-two crystal classes: Multiplication tables. Proceedings of the Royal Society London A, 391, 149-179.

Wong, C. P., & Bollampally, R. S. (1999). Thermal conductivity, elastic modulus, and coefficient of thermal expansion of polymer composites filled with ceramic particles for electronic packaging. Journal of Applied Polymer Science, 74, 3396-3403.

Zimmerman, R. W. (1991). Elastic moduli of a solid containing spherical inclusions. Mechanics of Materials, 12, 17-24.