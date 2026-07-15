# Effective elasticity of a medium with many parallel fractures

Filip P. Adamus

Department of Earth Sciences, Memorial University of Newfoundland, St. John's, NL A1C 5S7 Canada. E-mail: adamusfp@gmail.com

Received 2021 July 27; in original form 2021 April 2

## SUMMARY
We consider an alternative way of obtaining the effective elastic properties of a cracked medium. Similarly, to the popular linear-slip model, we assume flat, parallel fractures, and long wavelengths. However, we do not treat fractures as weakness planes of displacement discontinuity. In contrast to the classical models, we represent fractures by a thin layer embedded in the background medium. In other words, we follow the Schoenberg-Douma matrix formalism for Backus averaging, but we relax the assumptions of infinite weakness and marginal thickness of a layer so that it does not correspond to the linear-slip plane. To represent the properties of a fracture, we need a fourth-order elasticity tensor and a thickness parameter. The effective tensor becomes more complicated, but it may describe a higher concentration of parallel cracks more accurately. Apart from the derivations of the effective elasticity tensors, we perform numerical experiments in which we compare the performance of our approach with a linear-slip model in the context of highly fractured media. Our model becomes pertinent if filled-in or empty cracks occupy more than one per cent of the effective medium.

Key words: Elasticity and anelasticity; Seismic anisotropy; Theoretical seismology; Microstructure.

## 1 INTRODUCTION
The influence of cracks on the elastic properties of a medium has been a topic of interest for numerous researchers. There are various models used to describe the effective elasticity parameters of a fractured material. Some authors assume short wavelength compared to the cracked structure so that crack-pore microgeometry and the properties of a fluid are essential (e.g. O'Connell & Budiansky 1977). Others often focus on long wavelengths that are more suitable for seismic frequencies (e.g. Garbin & Knopoff 1973). Further, models differ depending on the shape of cracks assumed. If they are ellipsoidal (Eshelby 1957; Nishizawa 1982; Hudson 1994), the analysis usually becomes quite complicated (Hudson 1981). In practice, however, the aspect ratio of cracks is typically low. Also, the details of their microstructure are often neglected in the seismic fracture-detection studies. Therefore, cracks are not rarely described as flat (see Kachanov 1992), which is a useful simplification, since in some cases the results do not change very much compared to the ellipsoidal shapes (Hudson 1981; Schoenberg & Douma 1988; Thomsen 1995). Flat fractures may be planar (Schoenberg 1980), elliptical (Hudson 1980) or irregular (Gretchka et al. 2006). Moreover, cracks can be distributed randomly (Hudson 1980), can be aligned (Thomsen 1995) or parallel (Schoenberg & Douma 1988). In this paper, we consider long-wave, effective elasticity of a medium that corresponds to the background rock with parallel sets of flat fractures. Due to long-wavelength assumption, our investigation is pertinent—but not limited—to seismic studies.

There are three widely investigated, effective models that assume long wavelength and flat fractures (Cui et al. 2017). These are the linear-slip model, penny-shaped crack model and the combined model. Below, we shortly describe each of them.

The linear-slip stands for the fracture interface across which the traction vector is continuous, but the displacement is not (Schoenberg 1980). The displacement discontinuity linearly depends on traction. This relation is governed by the second-order tensor, which authors often refer to as the excess fracture compliance. Schoenberg & Douma (1988) are first to use the linear-slip concept in modelling the effective elasticity. Their work is based on Backus (1962) average, in which the aforementioned discontinuity corresponds to an infinitely weak and thin, horizontal layer. The work of Schoenberg & Douma (1988) was further developed by Schoenberg & Sayers (1995) that considered any orientation of linear-slip interfaces, not only the horizontal one. Another, but penny-shaped crack model was proposed by Garbin & Knopoff (1973) and then further developed by Hudson (1980). They use scattering formalism, where circular cracks are treated as scatterers. Cracks can be either aligned in one direction or randomly distributed. The expressions of Garbin & Knopoff (1973) are accurate to the first order in the concentration of cracks, whereas the expressions of Hudson (1980) to the second order. The second-order expressions correspond to the interactions between cracks that are not included in the linear-slip model. The penny-shaped model is complicated but accounts for the microstructure properties. The combined model is tantamount to the linear-slip one, but additionally relates the micro characteristics to the

---

© The Author(s) 2021. Published by Oxford University Press on behalf of The Royal Astronomical Society.

interface. Such a model was shown, for instance, by Hudson et al. (1996). The authors use scattering formalism and assume that circular cracks are aligned and parallel. This way, they obtain the excess fracture compliance related to cracks' properties. Subsequently, this second-order tensor can be used in the linear-slip model (Hudson & Liu 1999).

In this paper, we propose another long-wave model in which cracks are flat. However, we assume a neither planar nor circular shape. Herein, we treat fractures as sets of thin parallel layers. We follow the approach of Schoenberg & Douma (1988), where they use the matrix formalism based on the Backus average. As opposed to the aforementioned authors, we do not assume that layers corresponding to fractures are infinitely weak and thin. In other words, we abandon the linear-slip description. In this way, the properties of fractures are represented by fourth-order elasticity tensor and layer thickness, instead of excess fracture compliance only. In the text, we refer to this method as the generalized Schoenberg-Douma approach or, simply, the generalized approach. The linear slip model of Schoenberg & Douma (1988) can be extended to viscoelastic (Chichinina & Obolentseva 2009) or poroelastic (Rubino et al. 2015) media. Analogously, the extension can be made to the generalized method. However, due to the complexity of expressions, we focus on the elastic effects only. Thus, we assume that fractures are filled with solidified material. The properties of the filling material affect the elasticity parameters of the crack.

The main advantage of the generalized approach over the linear-slip model is that a high concentration of cracks is explicitly taken into account. The relaxation of infinite weakness and marginal thickness of cracks allows the representation of the elastic properties of a medium with many parallel fractures or the background rock with harder inclusions. The main body of the paper is dedicated to the comparison between the two aforementioned approaches. A heavily fractured medium was also considered in the combined models. Therein, the high concentration of cracks is described by, for instance, crack density parameter. In the rest part of the paper, we discuss the generalized approach and the combined models in the context of the effective elasticity of a medium with many parallel fractures.

## 2 GENERALIZED SCHOENBERG-DOUMA APPROACH

Elastic properties of parallel layers can be accurately approximated by the effective stiffness parameters of a homogeneous medium, assuming a sufficiently long wavelength. To obtain these effective parameters, consider a well-known Voigt's representation of a fourth-order elasticity tensor of arbitrary anisotropy,

$$
\boldsymbol{C}_{i}=\begin{bmatrix}
c_{11_{i}} & c_{12_{i}} & c_{13_{i}} & c_{14_{i}} & c_{15_{i}} & c_{16_{i}} \\
c_{12_{i}} & c_{22_{i}} & c_{23_{i}} & c_{24_{i}} & c_{25_{i}} & c_{26_{i}} \\
c_{13_{i}} & c_{23_{i}} & c_{33_{i}} & c_{34_{i}} & c_{35_{i}} & c_{36_{i}} \\
c_{14_{i}} & c_{24_{i}} & c_{34_{i}} & c_{44_{i}} & c_{45_{i}} & c_{46_{i}} \\
c_{15_{i}} & c_{25_{i}} & c_{35_{i}} & c_{45_{i}} & c_{55_{i}} & c_{56_{i}} \\
c_{16_{i}} & c_{26_{i}} & c_{36_{i}} & c_{46_{i}} & c_{56_{i}} & c_{66_{i}}
\end{bmatrix}.
\tag{1}
$$

Such a matrix describes the elastic properties of the $i$th thin layer. The above parameters can also be represented by three matrices proposed by Helbig & Schoenberg (1987),

$$
\boldsymbol{M}_{i}=\begin{bmatrix}
c_{11_{i}} & c_{12_{i}} & c_{16_{i}} \\
c_{12_{i}} & c_{22_{i}} & c_{26_{i}} \\
c_{16_{i}} & c_{26_{i}} & c_{66_{i}}
\end{bmatrix}, \quad \boldsymbol{N}_{i}=\begin{bmatrix}
c_{33_{i}} & c_{34_{i}} & c_{35_{i}} \\
c_{34_{i}} & c_{44_{i}} & c_{45_{i}} \\
c_{35_{i}} & c_{45_{i}} & c_{55_{i}}
\end{bmatrix}, \quad \boldsymbol{P}_{i}=\begin{bmatrix}
c_{13_{i}} & c_{14_{i}} & c_{15_{i}} \\
c_{23_{i}} & c_{24_{i}} & c_{25_{i}} \\
c_{36_{i}} & c_{46_{i}} & c_{56_{i}}
\end{bmatrix}.
\tag{2}
$$

These $3 \times 3$ matrices allow one to homogenize a stack of thin layers having arbitrary anisotropy, using process analogous to Backus (1962) average. Assume that layers are horizontal, and the $x_3$-axis denotes depth. The elasticity parameters of a homogenized, long-wave equivalent medium are

$$
\boldsymbol{N}_{e}=\overline{\left(\boldsymbol{N}_{i}^{-1}\right)}^{-1},
\tag{3}
$$

$$
\boldsymbol{P}_{e}=\overline{\left(\boldsymbol{P}_{i} \boldsymbol{N}_{i}^{-1}\right)} \overline{\left(\boldsymbol{N}_{i}^{-1}\right)}^{-1},
\tag{4}
$$

$$
\boldsymbol{M}_{e}=\overline{\boldsymbol{M}_{i}-\boldsymbol{P}_{i} \boldsymbol{N}_{i}^{-1} \boldsymbol{P}_{i}^{T}}+\overline{\boldsymbol{P}_{i} \boldsymbol{N}_{i}^{-1}} \overline{\left(\boldsymbol{N}_{i}^{-1}\right)}^{-1} \overline{\boldsymbol{N}_{i}^{-1} \boldsymbol{P}_{i}^{T}},
\tag{5}
$$

where bar denotes the average and $^{T}$ stands for a transpose. The average is weighted by the layer thickness. The above derivations are identical to the ones of Helbig & Schoenberg (1987), Schoenberg & Douma (1988) and Schoenberg & Muir (1989). For simplicity, throughout the paper, we assume density-scaled parameters.

We denote the relative thickness of a layer as $h_{i}$, where $i \in \{1, \dots, n\}$ and $\sum_{i=1}^{n} h_{i}=1$; thus, a medium is composed of numerous layers of various relative thicknesses. Some of these layers correspond to the background (host) medium, whereas the rest to the set of thin and long parallel fractures that are filled with a solidified material. Since the average is commutative in the layer order and associative (Schoenberg & Muir 1989), we can use these properties to fold the set of fractures into a single layer of total relative thickness $h_{f}$ and obtain its effective stiffnesses. Analogously, we treat the background medium of total relative thickness $1-h_{f}$. Below, we rewrite expressions (3)-(5) in terms of background and fracture elasticities, indexed by letter $b$ and $f$, respectively.

$$
\boldsymbol{N}_{e}=\left(\left(1-h_{f}\right) \boldsymbol{N}_{b}^{-1}+h_{f} \boldsymbol{N}_{f}^{-1}\right)^{-1}=\left(\left(1-h_{f}\right) \boldsymbol{N}_{b}^{-1}+\boldsymbol{Z}\right)^{-1},
\tag{6}
$$

![](./images/811965239498113024_1.jpg)

Figure 1. The illustration of commutative and associative properties of Helbig & Schoenberg (1987) average. The first column depicts the original layered medium, where grey colour denotes fractures filled with solidified material having different elastic properties. Subsequently, the layer sequence is interleaved so that fractures are cumulated in the upper part of the medium. Then, the effective parameters corresponding to fractures and background are obtained, respectively. In the last column, the effective parameters for the homogenized medium are calculated. The intermediate steps have no influence on the final results but are useful in the evaluation of the fracture's effect.

$$
\boldsymbol{P}_{e}=\left(\left(1-h_{f}\right) \boldsymbol{P}_{b} \boldsymbol{N}_{b}^{-1}+h_{f} \boldsymbol{P}_{f} \boldsymbol{N}_{f}^{-1}\right) \boldsymbol{N}_{e},
\tag{7}
$$

$$
\boldsymbol{M}_{e}=\left(1-h_{f}\right)\left(\boldsymbol{M}_{b}-\boldsymbol{P}_{b} \boldsymbol{N}_{b}^{-1} \boldsymbol{P}_{b}^{T}\right)+h_{f}\left(\boldsymbol{M}_{f}-\boldsymbol{P}_{f} \boldsymbol{N}_{f}^{-1} \boldsymbol{P}_{f}^{T}\right)+\left(\left(1-h_{f}\right) \boldsymbol{P}_{b} \boldsymbol{N}_{b}^{-1}+h_{f} \boldsymbol{P}_{f} \boldsymbol{N}_{f}^{-1}\right) \boldsymbol{N}_{e}\left(\left(1-h_{f}\right) \boldsymbol{N}_{b}^{-1} \boldsymbol{P}_{b}^{T}+h_{f} \boldsymbol{N}_{f}^{-1} \boldsymbol{P}_{f}^{T}\right),
\tag{8}
$$

where $\boldsymbol{Z}$ is a so-called fracture system compliance matrix (Schoenberg & Douma 1988; Schoenberg & Sayers 1995; Schoenberg & Helbig 1997). We illustrate the homogenization procedure used to obtain expressions (6)-(8) in Fig. 1. Note that these expressions are the generalizations of Schoenberg & Douma (1988) derivation. The aforementioned authors assumed that the thickness of a system of fractures is marginal $(h_{f} \to 0)$ and that fractures are infinitely weak $(\boldsymbol{M}_{f}, \boldsymbol{N}_{f}, \boldsymbol{P}_{f} \to 0)$. Upon introduction of such assumptions expressions (6)-(8) reduce to their results, namely,

$$
\boldsymbol{N}_{e} \approx\left(\boldsymbol{N}_{b}^{-1}+h_{f} \boldsymbol{N}_{f}^{-1}\right)^{-1}=\left(\boldsymbol{N}_{b}^{-1}+\boldsymbol{Z}\right)^{-1},
\tag{9}
$$

$$
\boldsymbol{P}_{e} \approx \boldsymbol{P}_{b} \boldsymbol{N}_{b}^{-1}\left(\boldsymbol{N}_{b}^{-1}+\boldsymbol{Z}\right)^{-1},
\tag{10}
$$

$$
\boldsymbol{M}_{e} \approx \boldsymbol{M}_{b}-\boldsymbol{P}_{b} \boldsymbol{N}_{b}^{-1} \boldsymbol{P}_{b}^{T}+\boldsymbol{P}_{b} \boldsymbol{N}_{b}^{-1}\left(\boldsymbol{N}_{b}^{-1}+\boldsymbol{Z}\right)^{-1} \boldsymbol{N}_{b}^{-1} \boldsymbol{P}_{b}^{T}.
\tag{11}
$$

Let us discuss the physical meaning of expressions (9)-(11). The effect of fractures is expressed by $\boldsymbol{Z}$ only, which stands for the excess compliance caused by total displacement discontinuity (total linear slip) across weakness planes (Schoenberg & Douma 1988). Thus, extremely thin layers are treated as planar discontinuities. The average of a background medium with a set of horizontal weakness planes becomes a particular case of a more general theory of Schoenberg & Sayers (1995), where planes of linear slip may have any orientation. Specifically, consider an equation of Schoenberg & Sayers (1995) that describes a background medium with one set of parallel weakness planes,

$$
s_{i j k \ell}=s_{i j k \ell_{b}}+s_{i j k \ell_{f}}=s_{i j k \ell_{b}}+\frac{1}{4}\left(Z_{i k} n_{\ell} n_{j}+Z_{j k} n_{\ell} n_{i}+Z_{i \ell} n_{k} n_{j}+Z_{j \ell} n_{k} n_{i}\right),
\tag{12}
$$

where $i, j, k, \ell \in\{1,2,3\}$, $s_{i j k \ell}$ denotes the compliances in a tensorial notation, and $n_{i}$ indicates the orientation of the planar slip. Note that if we insert vector $\boldsymbol{n}=[0,0,1]$, then we obtain the same result as from expressions (9)-(11). It is evident that in expressions (6)-(8), neither marginal thickness nor infinite weakness of a layer corresponding to fractures is assumed. Thus, expressions (6)-(8) are the generalizations of (9)-(11). In this generalized approach, we do not follow the theory of linear-slip excess compliances presented by Schoenberg & Sayers (1995). We treat a set of parallel fractures as thin and weak layers that does not have to be infinitely thin and weak but are allowed to be so. We believe that the aforementioned relaxation of linear-slip assumptions (no marginal thickness and infinite weakness) can be useful while willing to describe the effective elastic properties of a medium heavily cracked by weak fractures or a medium that contains few harder inclusions.

The physical meaning of the generalized approach can be extended to the influence of the set of parallel layers of any thickness and stiffness embedded in the background medium. Note that it depends on more unknowns than Schoenberg-Douma approximation; thus, it becomes more complicated. The influence of the fractures (or set of layers of any stiffness) is governed by thickness $h_{f}$ and three matrices $\boldsymbol{M}_{f}, \boldsymbol{Z}$, and $\boldsymbol{P}_{f}$ (instead of $\boldsymbol{Z}$ only). Note that these three matrices represent a fourth-order elasticity tensor.

## 3 EXAMPLES OF EFFECTIVE ELASTICITY TENSORS

Let us consider quite a general example of a folded orthotropic layer of relative thickness $h_f$ embedded in an orthotropic background medium of relative thickness $h_b=1-h_f$. We assume that tensors of both folded layer and background medium are expressed in a natural coordinate system. The elasticity parameters of a layer are

$$
\boldsymbol{M}_{f}=\left[\begin{array}{ccc}
f_{11} & f_{12} & 0 \\
f_{12} & f_{22} & 0 \\
0 & 0 & f_{66}
\end{array}\right], \quad \boldsymbol{P}_{f}=\left[\begin{array}{ccc}
f_{13} & 0 & 0 \\
f_{23} & 0 & 0 \\
0 & 0 & 0
\end{array}\right],
\tag{13}
$$

$$
\boldsymbol{N}_{f}=\left[\begin{array}{ccc}
f_{33} & 0 & 0 \\
0 & f_{44} & 0 \\
0 & 0 & f_{55}
\end{array}\right]=\left[\begin{array}{ccc}
h_{f} Z_{N}^{-1} & 0 & 0 \\
0 & h_{f} Z_{T_{p}}^{-1} & 0 \\
0 & 0 & h_{f} Z_{T_{q}}^{-1}
\end{array}\right],
\tag{14}
$$

where $f_{i j}$ stand for stiffnesses of a folded layer representing parallel fractures. Subscript $_{N}$ denotes normal fracture system compliance, whereas $_{T_{p}}$ and $_{T_{q}}$ tangential compliances that, for horizontal layers, correspond to the $x_{2}$ and $x_{1}$ directions, respectively (see, Schoenberg \& Douma 1988). We assume neither marginal thickness nor infinite weakness of layers. To define the relative thickness of the folded layer, we use parameter $h_f$. Now, we need to introduce a new parameter that could refer to the relative weakness of the embedded layer. We propose

$$
w_{i j} \equiv 1-\frac{f_{i j}}{c_{i j_{b}}}, \quad i, j \in\{1, \ldots, 6\},
\tag{15}
$$

where $c_{i j_{b}}$ are stiffnesses of a background medium. Weakness $w_{i j}$ is positive when the folded layer's elastic properties are weaker than the background, and negative when they are larger (we do not count unusual cases of negative stiffnesses). Infinitely weak layer (meaning that its stiffnesses are close to zero) gives $w_{i j} \rightarrow 1$. Note that if all $w_{i j}=0$, then there is no distinction between background and folded layer. A stiffness tensor describing the elastic properties of a background medium with a set of parallel layers is

$$
\boldsymbol{C}^{\text {eff }}=\left[\begin{array}{cc}
\boldsymbol{c}_{1} & 0 \\
0 & \boldsymbol{c}_{2}
\end{array}\right],
\tag{16}
$$

where

$$
\boldsymbol{c}_{1}=\left[\begin{array}{ccc}
c_{11_{b}}\left(1-h_{f} w_{11}-h_{b} \frac{c_{13_{b}}^{2}}{c_{11_{b}} c_{33_{b}}} w_{13} \hat{\delta}_{N}\right) & c_{12_{b}}\left(1-h_{f} w_{12}-h_{b} \frac{c_{13_{b}} c_{23_{b}}}{c_{12_{b}} c_{33_{b}}} w_{13} w_{23} \hat{\delta}_{N}\right) & c_{13_{b}}\left(1-w_{13} \hat{\delta}_{N}\right) \\
c_{12_{b}}\left(1-h_{f} w_{12}-h_{b} \frac{c_{13_{b}} c_{23_{b}}}{c_{12_{b}} c_{33_{b}}} w_{13} w_{23} \hat{\delta}_{N}\right) & c_{22_{b}}\left(1-h_{f} w_{22}-h_{b} \frac{c_{23_{b}}^{2}}{c_{22_{b}} c_{33_{b}}} w_{23} \hat{\delta}_{N}\right) & c_{23_{b}}\left(1-w_{23} \hat{\delta}_{N}\right) \\
c_{13_{b}}\left(1-w_{13} \hat{\delta}_{N}\right) & c_{23_{b}}\left(1-w_{23} \hat{\delta}_{N}\right) & c_{33_{b}}\left(1-w_{33} \hat{\delta}_{N}\right)
\end{array}\right]
\tag{17}
$$

and

$$
\boldsymbol{c}_{2}=\left[\begin{array}{ccc}
c_{44_{b}}\left(1-w_{44} \hat{\delta}_{T_{p}}\right) & 0 & 0 \\
0 & c_{55_{b}}\left(1-w_{55} \hat{\delta}_{T_{q}}\right) & 0 \\
0 & 0 & c_{66_{b}}\left(1-h_{f} w_{66}\right)
\end{array}\right].
\tag{18}
$$

We define

$$
0 \leq \hat{\delta}_{N} \equiv \frac{Z_{N} c_{33_{b}}}{1+Z_{N} c_{33_{b}}-h_{f}} \leq 1,
\tag{19}
$$

$$
0 \leq \hat{\delta}_{T_{p}} \equiv \frac{Z_{T_{p}} c_{44_{b}}}{1+Z_{T_{p}} c_{44_{b}}-h_{f}} \leq 1,
\tag{20}
$$

$$
0 \leq \hat{\delta}_{T_{q}} \equiv \frac{Z_{T_{q}} c_{55_{b}}}{1+Z_{T_{q}} c_{55_{b}}-h_{f}} \leq 1.
\tag{21}
$$

Coefficients $\hat{\delta}_{N}, \hat{\delta}_{T_{p}}$, and $\hat{\delta}_{T_{q}}$ are similar to deltas shown in Schoenberg \& Helbig (1997). The essential difference is the presence of $h_f$ in our expressions, which makes them more general. To indicate the above, we use hats over our parameters. If $h_{f} \rightarrow 0$ and $w_{i j} \rightarrow 1$, then matrix (16) represents the effective elasticity based on linear-slip theory. If we only assume the infinite weakness of folded layer, meaning that $h_{f} \nrightarrow 0$ and $w_{i j} \rightarrow 1$, then the effective stiffnesses become weaker as compared to the stiffnesses based on linear-slip assumptions. For instance, $c_{66}^{\text {eff }}=c_{66_{b}}\left(1-h_{f}\right)$, whereas for linear-slip, $c_{66}^{\text {eff }}=c_{66_{b}}$; it means that greater thickness of the folded layer, $h_f$, is responsible for the weakening of the effective medium. Note that to describe the infinitely weak folded layer that corresponds to thick cavity or very soft inclusion, we need only four parameters: $Z_{N}, Z_{T_{p}}, Z_{T_{q}}$, and $h_f$ (see Appendix A). On the other hand, if we set $h_{f} \rightarrow 0$ and $w_{i j} \nrightarrow 1$, than the relaxed infinite weakness of the folded layer makes the effective medium stronger.

So far, we have discussed an example of an effective tensor corresponding to horizontal fractures embedded in a background medium. What if parallel fractures are not horizontal, but have a different orientation? What if there are more sets of fractures? We propose to follow

1822
F. P. Adamus

the recipe presented in the last section of Schoenberg & Muir (1989). To model first set of fractures, we rotate the background medium to a desired coordinate system, then we calculate the effective parameters and rotate this tensor back. We repeat the process for other sets of fractures, where the background is the previously obtained effective medium. The above-mentioned procedure can be summarized as follows.

(i) Rotate background medium, $C_b$, using Bond transformation: $C_b^{\mathrm{rot}} = A^T C_b A$, where $A$ is the $6 \times 6$ transformation matrix (see e.g. Slawinski 2020, Chapter 5).
(ii) Add fractures: perform Backus average using expressions (3)-(5) to get rotated effective tensor $C_{\mathrm{eff}}^{\mathrm{rot}}$.
(iii) Rotate $C_{\mathrm{eff}}^{\mathrm{rot}}$ back to obtain the desired effective tensor: $C^{\mathrm{eff}} = A^T C_{\mathrm{eff}}^{\mathrm{rot}} A$.
(iv) To insert more sets of parallel fractures, repeat steps (i)-(iii) using $C^{\mathrm{eff}}$ in place of $C_b$.

Note that the interaction between sets of fractures is neglected. To our knowledge, the consideration of such interaction in the context of the Backus average has not been proposed by the researchers yet. Nevertheless, some effective models include interactions among fractures, as well described by Kachanov & Sevostianov (2018). Following the procedure of Schoenberg & Muir (1989), we obtain the effective tensor that corresponds to the orthotropic background medium with a set of orthotropic layers normal to the $x_1$-axis, namely,

$$
\boldsymbol{c}_{1}^{(1)}=\left[\begin{array}{ccc}
c_{11_{b}}\left(1-w_{11}^{33} \hat{\delta}_{N}^{(1)}\right) & c_{12_{b}}\left(1-w_{12}^{23} \hat{\delta}_{N}^{(1)}\right) & c_{13_{b}}\left(1-w_{13} \hat{\delta}_{N}^{(1)}\right) \\
c_{12_{b}}\left(1-w_{12}^{23} \hat{\delta}_{N}^{(1)}\right) & c_{22_{b}}\left(1-h_{f} w_{22}-h_{b} \frac{c_{12_{b}}^{2}}{c_{22_{b}} c_{11_{b}}} w_{12}^{23} \hat{\delta}_{N}^{(1)}\right) & c_{23_{b}}\left(1-h_{f} w_{23}^{12}-h_{b} \frac{c_{13_{b}} c_{12_{b}}}{c_{23_{b}} c_{33_{b}}} w_{13} w_{12}^{23} \hat{\delta}_{N}^{(1)}\right) \\
c_{13_{b}}\left(1-w_{13} \hat{\delta}_{N}^{(1)}\right) & c_{23_{b}}\left(1-h_{f} w_{23}^{12}-h_{b} \frac{c_{13_{b}} c_{12_{b}}}{c_{23_{b}} c_{33_{b}}} w_{13} w_{12}^{23} \hat{\delta}_{N}^{(1)}\right) & c_{33_{b}}\left(1-h_{f} w_{33}^{11}-h_{b} \frac{c_{13_{b}}^{2}}{c_{11_{b}} c_{33_{b}}} w_{13} \hat{\delta}_{N}^{(1)}\right)
\end{array}\right]
\label{22}
$$

and

$$
\boldsymbol{c}_{2}^{(1)}=\left[\begin{array}{ccc}
c_{44_{b}}\left(1-h_{f} w_{44}^{66}\right) & 0 & 0 \\
0 & c_{55_{b}}\left(1-w_{55} \hat{\delta}_{T_{q}}^{(1)}\right) & 0 \\
0 & 0 & c_{66_{b}}\left(1-w_{66}^{44} \hat{\delta}_{T_{p}}^{(1)}\right)
\end{array}\right],
\label{23}
$$

where

$$
w_{k \ell}^{i j}=1-\frac{f_{i j}}{c_{k \ell_{b}}}, \quad \text { for } \quad(i, j) \neq(k, \ell), \quad \text { where } \quad i, j, k, \ell \in\{1, \ldots, 6\}
\label{24}
$$

and

$$
0 \leq \hat{\delta}_{N}^{(1)} \equiv \frac{Z_{N} c_{11_{b}}}{1+Z_{N} c_{11_{b}}-h_{f}} \leq 1,
\label{25}
$$

$$
0 \leq \hat{\delta}_{T_{p}}^{(1)} \equiv \frac{Z_{T_{p}} c_{66_{b}}}{1+Z_{T_{p}} c_{66_{b}}-h_{f}} \leq 1,
\label{26}
$$

$$
0 \leq \hat{\delta}_{T_{q}}^{(1)} \equiv \frac{Z_{T_{q}} c_{55_{b}}}{1+Z_{T_{q}} c_{55_{b}}-h_{f}} \leq 1.
\label{27}
$$

Herein, subscripts $T_{p}$ and $T_{q}$ correspond to tangential compliances in horizontal $(x_{2})$ and vertical $(x_{3})$ directions, respectively. Schoenberg & Helbig (1997) denote them as $_{T_{p}}=_{H}$ and $_{T_{q}}=_{V}$. Superscript $^{(1)}$ indicates that the $x_1$-axis is normal to the set of embedded layers.

If fractures are normal to the $x_2$-axis, then we get

$$
\boldsymbol{c}_{1}^{(2)}=\left[\begin{array}{ccc}
c_{11_{b}}\left(1-h_{f} w_{11}-h_{b} \frac{c_{12_{b}}^{2}}{c_{11_{b}} c_{22_{b}}} w_{13}^{12} \hat{\delta}_{N}^{(2)}\right) & c_{12_{b}}\left(1-w_{12}^{13} \hat{\delta}_{N}^{(2)}\right) & c_{13_{b}}\left(1-h_{f} w_{13}^{12}-h_{b} \frac{c_{12_{b}} c_{23_{b}}}{c_{13_{b}} c_{22_{b}}} w_{12}^{13} w_{23} \hat{\delta}_{N}^{(2)}\right) \\
c_{12_{b}}\left(1-w_{12}^{13} \hat{\delta}_{N}^{(2)}\right) & c_{22_{b}}\left(1-w_{22}^{33} \hat{\delta}_{N}^{(2)}\right) & c_{23_{b}}\left(1-w_{23} \hat{\delta}_{N}^{(2)}\right) \\
c_{13_{b}}\left(1-h_{f} w_{13}^{12}-h_{b} \frac{c_{12_{b}} c_{23_{b}}}{c_{13_{b}} c_{22_{b}}} w_{12}^{13} w_{23} \hat{\delta}_{N}^{(2)}\right) & c_{23_{b}}\left(1-w_{23} \hat{\delta}_{N}^{(2)}\right) & c_{33_{b}}\left(1-h_{f} w_{33}^{22}-h_{b} \frac{c_{23_{b}}^{2}}{c_{22_{b}} c_{33_{b}}} w_{23} \hat{\delta}_{N}^{(2)}\right)
\end{array}\right]
\label{28}
$$

and

$$
\boldsymbol{c}_{2}^{(2)}=\left[\begin{array}{ccc}
c_{44_{b}}\left(1-w_{44} \hat{\delta}_{T_{p}}^{(2)}\right) & 0 & 0 \\
0 & c_{55_{b}}\left(1-h_{f} w_{55}^{66}\right) & 0 \\
0 & 0 & c_{66_{b}}\left(1-w_{66}^{55} \hat{\delta}_{T_{q}}^{(2)}\right)
\end{array}\right],
\label{29}
$$

where

$$
0 \leq \hat{\delta}_{N}^{(2)} \equiv \frac{Z_{N} c_{22_{b}}}{1+Z_{N} c_{22_{b}}-h_{f}} \leq 1,
\label{30}
$$

$$
0 \leq \hat{\delta}_{T_{p}}^{(2)} \equiv \frac{Z_{T_{p}} c_{44_{b}}}{1+Z_{T_{p}} c_{44_{b}}-h_{f}} \leq 1,
\label{31}
$$

$$
0 \leq \hat{\delta}_{T_{q}}^{(2)} \equiv \frac{Z_{T_{q}} c_{66_{b}}}{1+Z_{T_{q}} c_{66_{b}}-h_{f}} \leq 1.
\tag{32}
$$

Herein, subscripts $T_{p}$ and $T_{q}$ correspond to tangential compliances in vertical $(x_{3})$ and horizontal $(x_{1})$ directions, respectively. Superscript $^{(2)}$ indicates the normal to the set of embedded layers.

An example of effective tensor that corresponds to two sets of orthotropic layers normal to the $x_{1}$-axis and the $x_{2}$-axis that are embedded in the orthotropic background medium is complicated to present analytically. One of possible ways to obtain such a tensor is to treat coefficients of matrices $c_{1}^{(1)}$ and $c_{2}^{(1)}$ as background parameters and substitute them inside matrices $c_{1}^{(2)}$ and $c_{2}^{(2)}$.

All the examples discussed above can be easily reduced to cases of higher symmetry. For instance, if the background medium and folded layer are transversely isotropic with the $x_{3}$ symmetry axis (VTI), then $c_{11_{b}}=c_{22_{b}}, c_{13_{b}}=c_{23_{b}}, c_{44_{b}}=c_{55_{b}}, c_{11_{b}}=c_{12_{b}}+c_{66_{b}}$, and $w_{11}=w_{22}, w_{13}=w_{23}, w_{44}=w_{55}, w_{11}=w_{12}+w_{66}$. There are infinitely many examples of other effective tensors, which depend on the number of folded layers, their orientations and symmetry classes, and the symmetry class of the original background medium. These examples can be easily derived using expressions (6)-(8) and rotations of the coordinate system.

## 4 NUMERICAL EXPERIMENTS

Let us discuss what may be the influence of thickness and stiffnesses of the folded layer that are neglected in the effective elasticity tensor obtained using linear-slip assumptions. To do so, we consider numerical experiments in which we focus on the relative error,
$$
\mathrm{err}=\frac{\left\|\left(\boldsymbol{C}_{b}-\boldsymbol{C}_{l}^{\mathrm{eff}}\right)-\left(\boldsymbol{C}_{b}-\boldsymbol{C}^{\mathrm{eff}}\right)\right\|_{2}}{\left\|\boldsymbol{C}_{b}-\boldsymbol{C}_{l}^{\mathrm{eff}}\right\|_{2}} \times 100 \%=\frac{\left\|\Delta_{l}-\Delta\right\|_{2}}{\left\|\Delta_{l}\right\|_{2}} \times 100 \%,
\tag{33}
$$
where subscript $l$ indicates the linear-slip approximation, and $\boldsymbol{C}_{b}$ denotes the background elasticity tensor. In the error above, we try to understand the discrepancy between linear-slip and generalized approach in estimating the influence of fractures. Therefore, to separate this influence from the background rock, we consider $\Delta_{l}$ not $\boldsymbol{C}_{l}^{\text {eff }}$ in the denominator. We assume that the values of the background matrix $\boldsymbol{C}_{b}$ are known. We use a VTI background stiffness matrix from Schoenberg & Helbig (1997), namely,
$$
\boldsymbol{C}_{b}=\left[\begin{array}{cccccc}
10 & 4 & 2.5 & 0 & 0 & 0 \\
4 & 10 & 2.5 & 0 & 0 & 0 \\
2.5 & 2.5 & 6 & 0 & 0 & 0 \\
0 & 0 & 0 & 2 & 0 & 0 \\
0 & 0 & 0 & 0 & 2 & 0 \\
0 & 0 & 0 & 0 & 0 & 3
\end{array}\right].
\tag{34}
$$

To describe the influence of cracks, in Schoenberg-Douma approximation, we need the excess fracture compliance $3 \times 3$ matrix $\boldsymbol{Z}=h_{f} \boldsymbol{N}_{f}^{-1}$ only. Hence, in general, we require the maximum number of six independent compliances or, equivalently, six independent stiffnesses, and one thickness parameter (both matrices are symmetric). However, to obtain the generalized formulas, apart from $\boldsymbol{Z}$, we need $3 \times 3$ matrices $\boldsymbol{M}_{f}, \boldsymbol{P}_{f}$, and thickness $h_{f}\left(\boldsymbol{P}_{f}\right.$ is not symmetric). It gives the maximum number of twenty-one independent elasticity parameters (if the folded layer is generally anisotropic) and one thickness coefficient. In the numerical experiments, we assume that values of $\boldsymbol{Z}$ are the same for both approaches. In other words, $\boldsymbol{Z}$ does not influence $e r r$.

We assume one set of parallel fractures with a normal directed towards the $x_{1}$-axis. Herein, to manipulate the overall elastic properties of the folded layer easily and to understand its influence on err better, we also assume that the background and folded layer's stiffnesses are proportional. Hence, in our example, the fractures-same as the background-have VTI symmetry. We introduce,
$$
\boldsymbol{C}_{f}=k \boldsymbol{C}_{b},
\tag{35}
$$
where $k$ is a scalar denoting hardness of the folded layer and $\boldsymbol{C}_{f}$ is a $6 \times 6$ matrix that consists of fracture stiffnesses $f_{i j}$ (previously described by matrices $\boldsymbol{N}_{f}=h_{f} \boldsymbol{Z}^{-1}, \boldsymbol{M}_{f}$, and $\boldsymbol{P}_{f}$ ). Factor $k$ is helpful, since one parameter governs all twenty-one stiffnesses of $\boldsymbol{C}_{f}$. Also, the simplicity of $k$ can be physically justified when the folded layer is weak, and the exact values of specific stiffnesses do not matter so much. Hardness $k$ can be understood as a simplification and an alternative to the previously defined weaknesses $w_{i j}$, where $k=1-w_{i j}$. In the context of the above expressions, the parameters needed for the fracture description in Scohenberg-Douma approximation are
$$
\boldsymbol{Z}=h_{f}\left[\begin{array}{lll}
f_{33} & f_{34} & f_{35} \\
f_{34} & f_{44} & f_{45} \\
f_{35} & f_{45} & f_{55}
\end{array}\right]^{-1}=\frac{h_{f}}{k}\left[\begin{array}{lll}
c_{33_{b}} & c_{34_{b}} & c_{35_{b}} \\
c_{34_{b}} & c_{44_{b}} & c_{45_{b}} \\
c_{35_{b}} & c_{45_{b}} & c_{55_{b}}
\end{array}\right]^{-1}=\frac{h_{f}}{k}\left[\begin{array}{ccc}
1 / 6 & 0 & 0 \\
0 & 1 / 2 & 0 \\
0 & 0 & 1 / 2
\end{array}\right].
\tag{36}
$$

In the generalized formulation, we also have the same two unknowns that describe the fractures (see Appendix B). Hence, the error depends only on the relative thickness $h_{f}$ and hardness $k$. Below, we perform numerical experiments in which we manipulate the values of $h_{f}$ and $k$, so that either one or two of the linear-slip assumptions are relaxed. Specifically, we relax $k \rightarrow 0$, then $h_{f} \rightarrow 0$, and lastly, we relax them both. We check the influence of the aforementioned relaxations on the relative error (33) and wave phenomena.

![](./images/811965239498113024_2.jpg)

Figure 2. Dashed line illustrates the relative error, err, as a function of hardness, k, of folded layer. Thickness is fixed, $h_f = 10^{-5}$; hence, values of $\boldsymbol{Z}$ diminish when k grows. The axes are presented in a logarithmic scale.

Let us make a brief comment on the volatility of $\boldsymbol{Z}$. As we see in expression (36), $\boldsymbol{Z}$ depends on hardness and thickness of fractures. In the inverse problems, it might be difficult to estimate its values precisely, especially when the layer is very thin and weak (linear-slip theory). If, say $h_f = 10^{-12}$, then it does not really matter—in terms of marginal differences in the absolute values—if $k = 100h_f$ or $k = 0.01h_f$, still k is very small, but its influence on $\boldsymbol{Z}$ is enormous. Hence, if fractures are very thin and weak, a small change in their compliances makes $\boldsymbol{Z}$ almost impossible to estimate (if we know the elastic properties of the effective medium, but do not know the background). Therefore, to make our experiments more realistic, we do not allow $h_f$ and k to be smaller than $10^{-6}$.

### 4.1 Relaxation of infinite weakness assumption

In this example, we fix a very small thickness $h_f = 10^{-5}$ and allow k to grow. Note that when k increases, $\boldsymbol{Z}$ becomes smaller. Marginal $h_f$ and growing k corresponds to the relaxation of the infinite weakness assumption of the linear-slip theory. In this way, we wish to isolate the influence of the hardness of the folded layer on err. Specifically, we check how much one can be wrong when in forward modelling assumes infinite weakness and marginal thickness of the folded layer, but the former assumption is incorrect. The results are illustrated in Fig. 2.

We see that the relaxation of the infinite weakness assumption has quite a substantial effect on the results. Let us think of extremely thin parallel inclusions that are ten times weaker than the background medium. The above-mentioned physical example corresponds to $k = 0.1$, for which err is around seven per cent. Note that the error remains above one per cent even for the inclusions seventy times weaker than the surroundings. Thus, despite the complexity of expressions (6)-(8), the application of these generalized equations might be worth consideration if fractures are not extremely weak. Matrix $\boldsymbol{Z}$ can have very low values if k is much larger than $h_f$, which corresponds to the right part of Fig. 2.

### 4.2 Relaxation of marginal thickness assumption

Herein, we follow the infinite weakness assumption of the linear-slip theory. Thus, we fix a very small value of $k = 10^{-5}$. However, we relax the assumption of marginal thickness; therefore, we allow $h_f$ to grow. Note that as thickness increases, so do values of matrix $\boldsymbol{Z}$. Physically, minimal value of k and growing $h_f$ may correspond to empty cavities or very soft inclusions embedded in the host medium. In this numerical experiment, we expect to isolate the effect of relative thickness $h_f$ on err. Precisely, we examine how much one can be wrong when in forward modelling assumes the linear-slip deformation, but the assumption of marginal thickness is incorrect. The results are depicted in Fig. 3.

The influence of $h_f$ on the error seems to be quite significant and similar to the impact of k (compare Figs 2 and 3). Let us think of parallel cavities that take one per cent of the effective medium's space and which stiffnesses are extremely weak. The aforementioned scenario corresponds to $h_f = 0.01$ for which err is close to one per cent. The error becomes even more substantial for greater thicknesses of the folded layer. Again, the application of the generalized equations might be worth consideration if $h_f$ is substantial. The situation of large $h_f$ and extremely weak layer corresponds to very substantial values of $\boldsymbol{Z}$.

![](./images/811965239498113024_3.jpg)

Figure 3. Dashed line illustrates the relative error, err, as a function of relative thickness, $h_f$, of folded layer. Hardness is fixed, $k=10^{-5}$; hence, values of $\boldsymbol{Z}$ increase when $h_f$ grows. The axes are presented in a logarithmic scale.

![](./images/811965239498113024_4.jpg)

Figure 4. Cumulative influence of growing $k$ and $h_f$ on the relative error, err, illustrated in both hardness and relative thickness domains. Solid lines correspond to three scenarios of $k/h_f$ ratios ($\boldsymbol{Z}$ is fixed). Light grey, dark grey and black colours stand for $k/h_f=10$, $k/h_f=1$ and $k/h_f=0.5$, respectively. In general, larger $k$ and/or $h_f$ augment the error. For reference purposes, dashed-line depicts the growth of a single factor only; either $k$ (curve taken from Fig. 2) or $h_f$ (curve taken from Fig. 3). The axes are presented in a logarithmic scale.

### 4.3 Relaxation of both assumptions

In this experiment, we choose specific values of $\boldsymbol{Z}$ so that $k$ and $h_f$ are both allowed to grow. Hence, we relax both assumptions of linear-slip deformation. We want realistic values of excess compliance matrix; therefore, we choose $k/h_f=10$, $k/h_f=1$ and $k/h_f=0.5$ to get

$$
\boldsymbol{Z}_{10}=\begin{bmatrix}
1/60 & 0 & 0 \\
0 & 1/20 & 0 \\
0 & 0 & 1/20
\end{bmatrix}, \quad
\boldsymbol{Z}_{1}=\begin{bmatrix}
1/6 & 0 & 0 \\
0 & 1/2 & 0 \\
0 & 0 & 1/2
\end{bmatrix}, \quad
\boldsymbol{Z}_{05}=\begin{bmatrix}
1/3 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1
\end{bmatrix}, \tag{37}
$$

respectively. Having the above parameters set, we consider three scenarios of fractured media. In the context of the linear-slip method, $\boldsymbol{Z}_{10}$ corresponds to a moderately cracked material, since $\|\Delta_{I}\|_{2} \approx 1.8\left[\mathrm{km}^{2} \mathrm{~s}^{2}\right]$. Such an excess compliance matrix is similar to the one considered by Schoenberg & Helbig (1997). Matrices $\boldsymbol{Z}_{1}$ and $\boldsymbol{Z}_{05}$ indicate a substantial and very strong effect of fractures, respectively. In Fig. 4, we illustrate the cumulative influence of growing $k$ and $h_f$ on the relative error.

![](./images/811965239498113024_5.jpg)

Figure 5. Quadrants of slowness surfaces (in s km⁻¹) presented in three axis planes. Black colour denotes the linear-slip results, whereas grey stands for the generalized approach. Solid line depicts quasi-P wave slownesses. Dashed line denotes slownesses of quasi-S wave. Elliptical dashed curve describes quasi S wave with polarization normal to the plane. Charts expressed in polar coordinates.

The results indicate that, in a majority of $k$ and $h_f$ combinations, the larger hardness and thickness of a folded layer augment the relative error between the linear-slip and generalized approaches. The exception is the case of $k/h_f=10$. For instance, if $k=0.1$ and $h_f=0.01$, then err $\approx 6.95$ per cent. On the other hand, in Fig. 2, $k=0.1$ corresponds to $h_f=10^{-5}$ and err $\approx 7.21$ per cent . Hence, despite larger $h_f$ the error has decreased slightly. Such decrease does not happen if the dashed line from the right-hand part of Fig. 2 or 3 is compared to the curves corresponding to ratios $k/h_f=1$ or $k/h_f=0.5$, as shown in Fig. 4. Further, the error viewed at a specific hardness value (Fig. 4a) is greater for $k/h_f=0.5$ than for $k/h_f=1$, and larger for $k/h_f=1$ than for $k/h_f=10$, as expected. Naturally, the opposite relationship can be noted when comparing the errors in the relative thickness domain (Fig. 4b).

Additionally, let us exemplify the impact of the error—caused by the relaxation of the infinite weakness and marginal thickness assumptions—on the wave phenomena. To illustrate the discrepancy between the two approaches better, we assume substantial hardness and thickness of the folded layer, namely, $k=h_f=0.04$. In Fig. 5, we show quadrants of the slowness surfaces in the $x_3x_1$ , $x_3x_2$ and $x_1x_2$ planes. The relative error, err $=4.85$ per cent, has the largest impact on quasi-$P$ wave propagating in the $x_2$-axis direction. The discrepancy between phase velocities reaches $52\ \text{m}\ \text{s}^{-1}$ . Further, quasi-$S$ wave with polarization parallel to the axis-plane in which wave propagates is the most influenced in the $x_3x_2$-plane (up to $30.8\ \text{m}\ \text{s}^{-1}$ of a discrepancy). Quasi-$S$ wave with displacement direction normal to the wave propagation plane is the most impacted in the $x_3$-axis and the $x_2$-axis (up to $26.8\ \text{m}\ \text{s}^{-1}$ of discrepancy). Hence, the discrepancy between the linear-slip and

generalized method is non-negligible in the context of possible measurement errors and seems to be the largest in the plane parallel to the orientation of fractures.

To sum up, in general, the larger the hardness and/or thickness of the layer of interest, the greater the error. Based on our examples, hardness $k$ and relative thickness $h_f$ seem to have similar contributions to 'err'. We believe that the linear-slip theory is relatively accurate if fractures of the effective medium take less than one per cent of its space and are at least a hundred times weaker than the background. Otherwise, we recommend using the generalized approach. The number of parameters used in our method can be greatly reduced by introducing scaling factor $k$, as presented in the numerical experiments and exemplified in Appendix B.

## 5 COMPARISON WITH OTHER APPROACHES

So far, we have discussed the generalized approach in the context of the linear-slip theory only. In this section, we compare it to the models that take into account the micro properties, such as the concentration of cracks. First, let us consider the penny-shaped crack models proposed by Hudson (1980) and Hudson & Liu (1999). As we have already discussed in Section 1, these models were derived based on the scattering formalism. The concentration of scatterers (cracks) is represented by the crack density parameter, $e$. The intrinsic limitation of the scattering approach is that scatterers must be diluted (Keller 1960). Hence, the parameter responsible for the concentration of cracks, $e$, cannot be large. This is a significant drawback compared to the generalized Schoenberg-Douma model since $h_f$ has no such limitation. Hudson models are derived for isotropic background and involve second rank tensor $\overline{\boldsymbol{U}}$ that represents the elastic properties of fractures. Following the works of Hudson, we consider isotropic background, cracks with normal towards the $x_3$-axis, and rotationally invariant $\overline{\boldsymbol{U}}$ and $\boldsymbol{Z}$ (meaning that $Z_{T_p}=Z_{T_q}=Z_T$). The elasticity parameters of the linear-slip model are tantamount to the parameters shown in Hudson (1980) and Hudson & Liu (1999). Specifically, using the linear-slip model, we get

$$
\boldsymbol{C}=\begin{bmatrix}
c_{11_b}\left(1-\frac{c_{12_b}^2}{c_{11_b}^2}\delta_N\right) & c_{12_b}\left(1-\frac{c_{12_b}^2}{c_{11_b}^2}\delta_N\right) & c_{12_b}(1-\delta_N) & 0 & 0 & 0 \\
c_{12_b}\left(1-\frac{c_{12_b}^2}{c_{11_b}^2}\delta_N\right) & c_{11_b}\left(1-\frac{c_{12_b}^2}{c_{11_b}^2}\delta_N\right) & c_{12_b}(1-\delta_N) & 0 & 0 & 0 \\
c_{12_b}(1-\delta_N) & c_{12_b}(1-\delta_N) & c_{11_b}(1-\delta_N) & 0 & 0 & 0 \\
0 & 0 & 0 & c_{44_b}(1-\delta_T) & 0 & 0 \\
0 & 0 & 0 & 0 & c_{44_b}(1-\delta_T) & 0 \\
0 & 0 & 0 & 0 & 0 & c_{44_b}
\end{bmatrix},
\tag{38}
$$

where $c_{11_b}=c_{12_b}+2c_{44_b}$, and

$$
\delta_N=\frac{Z_N c_{11_b}}{1+Z_N c_{11_b}}, \quad \delta_T=\frac{Z_{T_q} c_{44_b}}{1+Z_{T_q} c_{44_b}}.
\tag{39}
$$

To obtain Hudson models, we insert either (see expressions 51-54 of Hudson 1980)

$$
Z_N=\frac{\frac{c_{11_b}}{c_{44_b}} e \overline{U}_{33}+O\left(e^2\right)}{c_{11_b}\left(1-\frac{c_{11_b}}{c_{44_b}} e \overline{U}_{33}-O\left(e^2\right)\right)}, \quad Z_T=\frac{e \overline{U}_{11}+O\left(e^2\right)}{c_{44_b}\left(1-e \overline{U}_{11}-O\left(e^2\right)\right)},
\tag{40}
$$

or (see expression 8 of Hudson & Liu 1999)

$$
Z_N=\frac{e \overline{U}_{33}}{c_{44_b}}+\Theta\left(e^2\right), \quad Z_T=\frac{e \overline{U}_{11}}{c_{44_b}}+\Theta\left(e^2\right),
\tag{41}
$$

inside of $\boldsymbol{C}$. Both $O(e^2)$ and $\Theta(e^2)$ are second-order terms in crack density, responsible for the crack interactions. Hence, penny-shaped crack models, up to the first order in $e$, can be treated as linear-slip models with parameters related to cracks' specific microstructure (we call them combined models). Assuming that cracks are infinitely weak-by means of Eshelby theory-components $\overline{U}_{11}$ and $\overline{U}_{33}$ can be related to the background stiffnesses (Eshelby 1957; Budiansky & O'Connell 1976; Hudson & Liu 1999),

$$
\overline{U}_{11}=\frac{16 c_{11_b}}{3\left(3 c_{11_b}-2 c_{44_b}\right)}, \quad \overline{U}_{33}=\frac{4 c_{11_b}}{3\left(c_{11_b}-c_{44_b}\right)}.
\tag{42}
$$

As indicated by Sayers & Kachanov (1991), second terms in the models of Hudson are not sufficient to account for higher concentration of cracks. From $e>0.2$ they start to exhibit meaningless behaviour (the aforementioned limitation of the scattering approach). Most of the combined approaches neglect the second-order terms. Some of them do not assume interactions among cracks (non-interaction approximation), which is accurate for small (or, in some cases, moderate) concentrations of cracks only (Kachanov & Sevostianov 2018). The other methods, such as the self-consistent, differential, or Mori-Tanaka schemes, tend to overestimate the impact of cracks on the effective stiffness (Kachanov 1992). As shown by simulations of Saenger et al. (2006), the differential method seems to provide the best results for a high concentration of cracks. In the aforementioned schemes, density parameter $e$ can be replaced by second and fourth-order tensors that cover all orientation distributions of cracks in a unified way (Kachanov 1992). Below, for simplicity, we focus on $e$ only.

The upside of the combined models is their ability to relate micro properties of cracks to excess fracture compliance $\boldsymbol{Z}$. Also, under certain conditions, they allow expressing $\boldsymbol{Z}$ in terms of the background stiffnesses (expression 42). However, we need to emphasize their

main downside in the context of heavily cracked media. The combined models assume that cracks are flat, meaning that their aspect ratio is very small ($\alpha \to 0$). To relate micro properties to the linear-slip, the volume fraction occupied by cracks, $\phi_f$, must be also very small that is tantamount to $h_f \to 0$ assumed by Schoenberg & Douma (1988). Crack density combines both $\alpha$ and $\phi_f$, namely,

$$
e = \frac{3\phi_f}{4\pi\alpha}. \tag{43}
$$

However, if the aspect ratio occurs to be small but not infinitely small, then a large number of $e$ implies a significant value of $\phi_f$. In turn, large $\phi_f$ is tantamount to a significant $h_f$ that violates the assumption underlying the linear-slip theory. Therefore, the value of $e$ seems to be limited intrinsically.

The generalized method seems to be more adequate in describing media with many parallel fractures than combined approaches since a large concentration of cracks corresponds to large $h_f$ that does not violate the generalized method's assumptions. Perhaps, it is possible to utilize both parameters $e$ and $h_f$ jointly. In a particular case of flat but infinitely weak fractures (with no marginal thickness of the folded layer), we may use the Eshelby theory to express $\boldsymbol{Z}$ in terms of background elasticities and density parameter as it is done in the combined approaches. In other words, we conjecture that

$$
Z_N = \frac{4c_{11_b} e}{3c_{44_b} \left(c_{11_b} - c_{44_b}\right)}, \quad Z_T = \frac{16c_{11_b} e}{3c_{44_b} \left(3c_{11_b} - 2c_{44_b}\right)} \tag{44}
$$

can be inserted inside matrices obtained using the generalized method (where $w_{ij} = 1$ and $h_f > 0$). This conjecture needs to be verified by experimental studies.

To sum up, a higher concentration of cracks can be either described by a density parameter or by $h_f$, depending on whether the combined model or generalized method is used, respectively. Both methods give different effective elasticity parameters. For instance, if background is isotropic and cracks are aligned along the axis, $e$ influences five independent effective stiffnesses (matrix 38), whereas $h_f$ influences six stiffnesses (simplified matrix (16)). Moreover, $e$ is accurate for small numbers only, whereas $h_f$ has no limitations. Perhaps it is possible to combine micro properties with a particular case of the generalized approach employing the Eshelby theory.

## 6 CONCLUSIONS

We have presented an alternative way of computing the effective elasticity tensor corresponding to a medium with parallel sets of fractures that are filled with a solidified material. We have discussed a traditional Schoenberg–Douma method that is based on the linear-slip approximation. Further, we have shown a generalization of their approach and examined if consideration of more complicated expressions might be useful in the context of the approximation accuracy. The significant difference between the two aforementioned approaches is that the generalization considers thickness and additional (to $\boldsymbol{Z}^{-1}$) elastic properties of the layer that corresponds to the system of parallel fractures. We believe that no assumption of linear-slip deformation in the generalized expressions can be useful while describing the effective elastic properties of a medium that is heavily fractured or contains a few harder inclusions.

In case material includes numerous empty cavities, our model simplifies so that the additional elastic properties of the folded layer are not taken into account (see Appendix A). However, in such a case, our approach still differs from a traditional linear-slip method since the thickness parameter ($h_f$) is considered. Another simplification to our model is possible if we assume that the scaled background stiffnesses describe the elasticity of fractures. This way, only two additional parameters—thickness $h_f$ and scaling factor $k$—are needed to consider the influence of parallel fractures (see Appendix B). The linear-slip model can be simplified in a similar manner.

Numerical experiments have exposed that in forward problems, the consideration of parallel fractures intensity (equivalently, relative thickness $h_f$ of the folded layer) and its additional elasticity parameters might be essential. We believe that also in the inverse problems, where we expect a heavily cracked medium, the generalized equations shown in this paper might be worth considering. It seems that the linear-slip approximation is quite accurate if fractures of the effective medium take less than one per cent of its space and are at least a hundred times weaker than the background. If the fractures take more space or are harder, we recommend using the generalized Schoenberg–Douma approach that does not neglect the intensity of inclusions.

Other possible methods that take into account the high concentration of cracks are the combined, penny-shaped crack models. These approaches take into consideration the density and microstructure of cracks. The drawback of these methods is that they are limited intrinsically to the diluted concentration of cracks, and they are quite complicated. Also, their parameter responsible for the intensity of cracks ($e$) affects less number of the effective stiffnesses compared to the analogous parameter presented in the generalized approach ($h_f$). A combination of penny-shaped crack models with the generalized method seems possible. In this way, cracks are described by the background elasticities, density parameter and $h_f$.

Note that the generalized Schoenberg–Douma method is suitable for the computation of long-wave effective elasticity of any medium composed of parallel layers. Naturally, this approach is not limited to a very thin layer embedded in the background medium, which was the focus of this paper.

## ACKNOWLEDGEMENTS

We wish to acknowledge discussions with Michael A. Slawinski. Also, we thank Elena Patarini for the graphical support. The research was done in the context of The Geomechanics Project partially supported by the Natural Sciences and Engineering Research Council of Canada, grant 202259.

## DATA AVAILABILITY

The data that support the findings of this study are available from the corresponding author upon reasonable request.

## CONFLICT OF INTEREST

The author has no conflict of interest to declare.

## REFERENCES

Backbus, G. E., 1962. Long-wave elastic anisotropy produced by horizontal layering, *J. geophys. Res.*, **67**(11), 4427–4440, doi.org/10.1029/JZ067i011p04427.

Budiansky, B. & O'Connell, R. J., 1976. Elastic moduli of a cracked solid, *Int. J. Solids Struct.*, **12**(2), 81–97, doi.org/10.1016/0020-7683(76)90044-5.

Chichinina, T. & Obolentseva, I., 2009. Generalization of Schoenberg's linear slip model to attenuative media: Physical modeling versus theory, in *79th Annual International Meeting*, SEG, Expanded Abstracts, pp. 3451–3457.

Cui, X., Lines, L., Krebes, E. S. & Peng, S., 2017. *Seismic Forward Modeling of Fractures and Fractured Medium Inversion*, 1st edn, Springer.

Eshelby, J. D., 1957. The determination of the elastic field of an ellipsoidal inclusion and related problems, *Proc. R. Soc. A*, **241**(1226), 376–396, doi.org/10.1098/rspa.1957.0133.

Garbin, H. D. & Knopoff, L., 1973. The compressional modulus of a material permeated by a random distribution of circular cracks, *Q. Appl. Math.*, **30**(4), 454–464.

Grechka, V., Vasconcelos, I. & Kachanov, M., 2006. The influence of crack shape on the effective elasticity of fractured rocks, *Geophysics*, **71**(5), D153–D160.

Helbig, K. & Schoenberg, M., 1987. Anomalous polarization of elastic waves in transversely isotropic media, *J. acoust. Soc. Am.*, **81**(5), 1235–1245.

Hudson, J. A., 1980. Overall properties of a cracked solid, *Math. Proc. Camb. Phil. Soc.*, **88**(2), 371–384.

Hudson, J. A., 1981. Wave speeds and attenuation of elastic waves in material containing cracks, *Geophys. J. R. astr. Soc.*, **64**(1), 133–150, doi.org/10.1111/j.1365-246X.1981.tb02662.x.

Hudson, J. A., 1994. Overall properties of a material with inclusions or cavities, *J. geophys. Int.*, **117**(2), 555–561, doi.org/10.1111/j.1365-246X.1994.tb03952.x.

Hudson, J. A. & Liu, E., 1999. Effective elastic properties of heavily faulted structures, *Geophysics*, **64**(2), 479–485.

Hudson, J. A., Liu, E. & Crampin, S., 1996. Transmission properties of a plane fault, *J. geophys. Int.*, **125**(2), 559–566, doi.org/10.1111/j.1365-246X.1996.tb00018.x.

Kachanov, M., 1992. Effective elastic properties of cracked solids: critical review of some basic concepts, *Appl. Mech. Rev.*, **45**(8), 304–335.

Kachanov, M. & Sevostianov, I., 2018. *Micromechanics of Materials, with Applications*, Springer.

Keller, J. B., 1960. Wave Propagation in Random Media, Tech. Rep. EM-164, New York University, Institute of Mathematical Sciences Division of Electromagnetic Research.

Nishizawa, O., 1982. Seismic velocity anisotropy in a medium containing oriented cracks—transversely isotropic case, *J. Phys. Earth*, **30**(4), 331–347.

O'Connell, R. J. & Budiansky, B., 1977. Viscoelastic properties of fluid-saturated cracked solids, *J. geophys. Res.*, **82**(36), 5719–5736, doi.org/10.1029/JB082i036p05719.

Rubino, J. G., Castromán, G. A., Müller, T. M., Monachesi, L. B., Zyserman, F. I. & Holliger, K., 2015. Including poroelastic effects in the linear slip theory, *Geophysics*, **80**(2), 1–6.

Saenger, E. H., Kruger, O. S. & Shapiro, S., 2006. Effective elastic properties of fractured rocks: dynamic vs. static considerations, *Int. J. Fract.*, **139**(3), 569–576.

Sayers, C. & Kachanov, M., 1991. A simple technique for finding effective elastic constants of cracked solids for arbitrary crack orientation statistics, *Int. J. Solids Struct.*, **7**(6), 671–680.

Schoenberg, M., 1980. Elastic wave behavior across linear slip interfaces, *J. acoust. Soc. Am.*, **68**(5), 1516–1521.

Schoenberg, M. & Douma, J., 1988. Elastic wave propagation in media with parallel fractures and aligned cracks, *Geophys. Prospect.*, **36**(6), 571–590.

Schoenberg, M. & Helbig, K., 1997. Orthorhombic media: modeling elastic wave behavior in a vertically fractured earth, *Geophysics*, **62**(6), 1954–1974.

Schoenberg, M. & Muir, F., 1989. A calculus for finely layered anisotropic media, *Geophysics*, **54**(5), 581–589.

Schoenberg, M. & Sayers, C. M., 1995. Seismic anisotropy of fractured rock, *Geophysics*, **60**(1), 204–211.

Slawinski, M. A., 2020. *Waves and Rays in Elastic Continua*, 4th edn, World Scientific, Singapore.

Thomsen, L., 1995. Elastic anisotropy due to aligned cracks in porous rock, *Geophys. Prospect.*, **43**(6), 805–829.

## APPENDIX A: EFFECTIVE ELASTICITY WITH WEAKNESS ASSUMPTION ONLY

Consider an effective tensor that corresponds to the orthotropic background medium with a set of orthotropic layers normal to the $x_1$-axis. Layers are folded into one medium representing fractures. If we assume infinite weakness of the folded layer, but not its marginal thickness, then matrices (22) and (23) are simplified. We get

$$
\boldsymbol{C}^{\text{eff}} = \begin{bmatrix} c_1 & 0 \\ 0 & c_2 \end{bmatrix}, \tag{A1}
$$

where

$$
\boldsymbol{c}_{1}=\left[\begin{array}{ccc}
c_{11_{b}}\left(1-\hat{\delta}_{N}\right) & c_{12_{b}}\left(1-\hat{\delta}_{N}\right) & c_{13_{b}}\left(1-\hat{\delta}_{N}\right) \\
c_{12_{b}}\left(1-\hat{\delta}_{N}\right) & c_{22_{b}} h_{b}\left(1-\frac{c_{12_{b}}^{2}}{c_{22_{b}} c_{11_{b}}} \hat{\delta}_{N}\right) & c_{23_{b}} h_{b}\left(1-\frac{c_{13_{b}} c_{12_{b}}}{c_{23_{b}} c_{33_{b}}} \hat{\delta}_{N}\right) \\
c_{13_{b}}\left(1-\hat{\delta}_{N}\right) & c_{23_{b}} h_{b}\left(1-\frac{c_{13_{b}} c_{12_{b}}}{c_{23_{b}} c_{33_{b}}} \hat{\delta}_{N}\right) & c_{33_{b}} h_{b}\left(1-\frac{c_{13_{b}}^{2}}{c_{11_{b}} c_{33_{b}}} \hat{\delta}_{N}\right)
\end{array}\right],
\tag{A2}
$$

$$
\boldsymbol{c}_{2}=\left[\begin{array}{ccc}
c_{44_{b}} h_{b} & 0 & 0 \\
0 & c_{55_{b}}\left(1-\hat{\delta}_{V}\right) & 0 \\
0 & 0 & c_{66_{b}}\left(1-\hat{\delta}_{H}\right)
\end{array}\right],
\tag{A3}
$$

and

$$
\hat{\delta}_{N}=\frac{Z_{N} c_{11_{b}}}{h_{b}+Z_{N} c_{11_{b}}}, \quad \hat{\delta}_{V}=\frac{Z_{V} c_{55_{b}}}{h_{b}+Z_{V} c_{55_{b}}}, \quad \hat{\delta}_{H}=\frac{Z_{H} c_{66_{b}}}{h_{b}+Z_{H} c_{66_{b}}}.
\tag{A4}
$$

Excess fracture compliance that corresponds to displacement in normal, vertical, and horizontal direction is denoted by $Z_{N}$, $Z_{V}$, and $Z_{H}$, respectively. The elastic properties of a background medium are described by $c_{i j_{b}}$, whereas $h_{b}$ stands for the relative thickness of such medium. The description of fractures needs only four parameters; $Z_{N}, Z_{V}, Z_{H}$ and $h_{b}$. Thickness $h_{b} \in(0,1]$ is the only coefficient that distinguishes the above matrices from the linear-slip description. If $h_{b}=1$ than we get effective elasticity consistent with theory of Schoenberg & Douma (1988) or Schoenberg & Sayers (1995).

## APPENDIX B: EFFECTIVE ELASTICITY WITH SCALING FACTOR $k$

Again, consider an effective tensor that corresponds to the orthotropic background with an embedded set of orthotropic fractures normal to the $x_{1}$-axis. Assume that the elastic properties of folded fractures are equal to the scaled background stiffnesses. In other words, we invoke expression (35), namely, $C_{f}=k C_{b}$, where $k$ is a scalar that relates $6 \times 6$ matrices describing fractures and the background, respectively. Due to the assumption above, the effective tensor represented by matrices (22) and (23) requires a lower number of parameters. To show it, first, we rewrite the weaknesses

$$
w_{i j}=1-k, \quad w_{k l}^{i j}=1-k c_{i j_{b}} / c_{k l_{b}}
\tag{B1}
$$

and the excess compliances

$$
Z_{N}=\frac{h_{f}}{c_{33_{b}} k}, \quad Z_{T_{p}}=\frac{h_{f}}{c_{44_{b}} k}, \quad Z_{T_{q}}=\frac{h_{f}}{c_{55_{b}} k}.
\tag{B2}
$$

Subsequently, we insert expressions (B1) and (B2) into matrices (22) and (23) to obtain

$$
\boldsymbol{C}^{\mathrm{eff}}=\left[\begin{array}{cccccc}
c_{11} & c_{12} & c_{13} & 0 & 0 & 0 \\
c_{12} & c_{22} & c_{23} & 0 & 0 & 0 \\
c_{13} & c_{23} & c_{33} & 0 & 0 & 0 \\
0 & 0 & 0 & c_{44} & 0 & 0 \\
0 & 0 & 0 & 0 & c_{55} & 0 \\
0 & 0 & 0 & 0 & 0 & c_{66}
\end{array}\right],
\tag{B3}
$$

where

$$
c_{11}=\frac{c_{11_{b}} c_{33_{b}} k}{c_{11_{b}} h_{f}+c_{33_{b}} k-c_{33_{b}} h_{f} k},
\tag{B4}
$$

$$
c_{22}=h_{f} k\left(c_{22_{b}}-\frac{c_{23_{b}}^{2}}{c_{33_{b}}}\right)+\left(1-h_{f}\right)\left(c_{22_{b}}-\frac{c_{12_{b}}^{2}}{c_{11_{b}}}\right)+\frac{c_{11_{b}} c_{33_{b}} k\left(\frac{c_{12_{b}}\left(1-h_{f}\right)}{c_{11_{b}}}+\frac{c_{23_{b}} h_{f}}{c_{33_{b}}}\right)^{2}}{c_{11_{b}} h_{f}+c_{33_{b}} k-c_{33_{b}} h_{f} k},
\tag{B5}
$$

$$
c_{33}=h_{f} k\left(c_{11_{b}}-\frac{c_{13_{b}}^{2}}{c_{33_{b}}}\right)+\left(1-h_{f}\right)\left(c_{33_{b}}-\frac{c_{13_{b}}^{2}}{c_{11_{b}}}\right)+\frac{c_{11_{b}} c_{33_{b}} k\left(\frac{c_{13_{b}}\left(1-h_{f}\right)}{c_{11_{b}}}+\frac{c_{13_{b}} h_{f}}{c_{33_{b}}}\right)^{2}}{c_{11_{b}} h_{f}+c_{33_{b}} k-c_{33_{b}} h_{f} k},
\tag{B6}
$$

$$
c_{12}=\frac{c_{12_{b}} c_{33_{b}} k+c_{11_{b}} c_{23_{b}} h_{f} k-c_{12_{b}} c_{33_{b}} h_{f} k}{c_{11_{b}} h_{f}+c_{33_{b}} k-c_{33_{b}} h_{f} k},
\tag{B7}
$$

$$
c_{13}=\frac{c_{13_{b}} k\left(c_{33_{b}}+c_{11_{b}} h_{f}-c_{33_{b}} h_{f}\right)}{c_{11_{b}} h_{f}+c_{33_{b}} k-c_{33_{b}} h_{f} k},
\tag{B8}
$$

$$
c_{23}=h_{f} k\left(c_{12_{b}}-\frac{c_{13_{b}} c_{23_{b}}}{c_{33_{b}}}\right)+\left(1-h_{f}\right)\left(c_{23_{b}}-\frac{c_{12_{b}} c_{13_{b}}}{c_{11_{b}}}\right)+\frac{c_{11_{b}} c_{33_{b}} k\left(\frac{c_{13_{b}}\left(1-h_{f}\right)}{c_{11_{b}}}+\frac{c_{13_{b}} h_{f}}{c_{33_{b}}}\right)\left(\frac{c_{12_{b}}\left(1-h_{f}\right)}{c_{11_{b}}}+\frac{c_{23_{b}} h_{f}}{c_{33_{b}}}\right)}{c_{11_{b}} h_{f}+c_{33_{b}} k-c_{33_{b}} h_{f} k}, \tag{B9}
$$

$$
c_{44}=c_{44_{b}}-c_{44_{b}} h_{f}+c_{66_{b}} h_{f} k, \tag{B10}
$$

$$
c_{55}=\frac{c_{55_{b}} k}{h_{f}+k-h_{f} k}, \tag{B11}
$$

$$
c_{66}=\frac{c_{66_{b}} c_{44_{b}} k}{c_{66_{b}} h_{f}+c_{44_{b}} k-c_{44_{b}} h_{f} k}. \tag{B12}
$$

The effective elasticity matrix (B3) is described by the background stiffnesses $c_{i j_{b}}$ and only two additional parameters $k$ and $h_{f}$ that are responsible for the set of parallel fractures.