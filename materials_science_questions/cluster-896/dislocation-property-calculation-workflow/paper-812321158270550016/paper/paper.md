# Shape Effects in the Interaction Between an Edge Dislocation and an Elliptical Inhomogeneity
L. Stagni and R. Lizzio*
Istituto di Fisica, Facoltà di Ingegneria, Università di Roma, I-00185 Roma, Italy

Received 12 October 1982/Accepted 30 December 1982

Abstract. The plane elasticity problem of the interaction between an edge dislocation and an elliptical inhomogeneity is solved, and the image glide-force on dislocation is computed. Contour plots of the force exterted by either an elliptic hole (crack) or a rigid elliptical inhomogeneity show that force is stronger for more elongated shapes, and that in some cases dislocation trapping effects undergo drastic changes even for slight shape variations. The general case is investigated by means of angular plots of force. They show increasing oscillatory angular depence on increasing both elongation and shear moduli difference.

PACS: 61.70.G, 46.30.C, 62.20

The interaction between an edge dislocation and a circular inhomogeneity has been extensively investi- gated in the past years [1-3]. Edge dislocations near sharp or elliptical cracks have also been considered [4,5]. However, the general case of the interaction with an elliptical inhomogeneity has not yet been confronted (a solution was found for the screw dislo- cation companion problem [6]). This model may be considered as a basic one in the investigation of inhomogeneities' shape effects on the elasto-plastic behavior of materials. For instance, it may help de- termine the best shape of fiber cross-section in order to improve the performances of a composite material, or estimate the effect of slight deviations from the ideal shape on the product quality. More in general, it may allow us to get an insight into the interplay between shape and material constant difference. The elasticity solution of the problem is performed in Sect. 1 on the basis of a recent work [7]. Results of computer calculations, selected to display the effect of shape on the image glide-force on dislocation, are recorded and discussed in Sect. 2. The important special cases of void (crack) and rigid inhomogeneity are examined in detail.

## 1. The Elasticity Problem Solution
General formulas yielding the perturbative elastic field produced by an elliptical inhomogeneity have been recorded in [7]. Here, the unperturbed field is engen- dered by an edge dislocation with Burgers vector $\boldsymbol{B}=(B_{x}, B_{y})$ , located at $z_{0}=r_{0} \exp (\mathrm{i} \varphi_{0})$ , or $\zeta_{0}=\varrho_{0} \exp (\mathrm{i} \theta_{0})$ , near the inhomogeneity (Fig. 1). The complex potentials representing this field may be written as
$$\begin{aligned}
\varphi_{*}(\zeta)= & R \gamma \log \left[\left(\zeta-\zeta_{0}\right)\left(\zeta-m / \zeta_{0}\right) / \zeta\right] \\
\eta_{*}(\zeta)= & R \bar{\gamma} \log \left[\left(\zeta-\zeta_{0}\right)\left(\zeta-m / \zeta_{0}\right) / \zeta\right] \\
& +R \gamma \frac{\zeta\left(1 / \zeta+m \zeta-\bar{\zeta}_{0}-m / \bar{\zeta}_{0}\right)}{\left(\zeta-\zeta_{0}\right)\left(\zeta-m / \zeta_{0}\right)},
\end{aligned}\qquad(1)$$
where
$$\zeta=\varrho \mathrm{e}^{\mathrm{i} \theta}$$

$$\gamma=G_{1}\left(B_{y}-\mathrm{i} B_{x}\right) / \pi R\left(\kappa_{1}+1\right)$$

$$\kappa_{1}= \begin{cases}3-4 v_{1} & \text { for plane strain } \\ \left(3-v_{1}\right) /\left(1+v_{1}\right) & \text { for plane stress }\end{cases}$$

$$m=(a-b)/(a+b)$$

$$R=(a+b)/2.$$
$a$ and $b$ are denoting the ellipse's semi-axes, and $G_{1}$ and v, matrix shear modulus and Poisson's ratio, re- spectively (subscript 1 refers to matrix, and subscript

---
* Work supported by the Gruppo Nazionale di Struttura della Materia del C.N.R., Roma, Italy

![](./images/812321158270550016_1.jpg)

Fig. 1. (a) Edge dislocation near an elliptic inhomogeneity. (b) Mapping onto the plane deprived of the circle $\varrho=\sqrt{m}$

2 to inhomogeneity). An important role in the pre- sent problem is played by the shear moduli ratio $\Gamma=G_{2} / G_{1}$

The $k$-positive Laurent's expansion coefficient of the functions (1) for $m / \varrho_{0} \leqq \varrho \leqq \varrho_{0}$ are, respectively;

$$
\begin{aligned}
& A_{k}=-R \gamma \zeta_{0}^{-k} / k \\
& B_{k}=R \gamma\left[\mathrm{e}^{-2 \mathrm{i} \alpha} / k+M\left(\varrho_{0}, \theta_{0}\right)\right] \zeta_{0}^{-k}
\end{aligned} \quad(k=1,2,3 \ldots),
$$

where
$$
\begin{aligned}
& \alpha=\arctan \left(B_{y} / B_{x}\right) \\
& M\left(\varrho_{0}, \theta_{0}\right)=\left(\varrho_{0}^{2}-1\right)\left(1-m \mathrm{e}^{2 \mathrm{i} \theta_{0}}\right) /\left(\varrho_{0}^{2} \mathrm{e}^{2 \mathrm{i} \theta_{0}}-m\right).
\end{aligned}
$$

By introducing the values of these coefficients as input of a general computer subprogram [7], we are now able to evaluate any quantity related to the elastic field in the dislocated heterogeneous plane. In particular, we are interested in the glide component of the image force on dislocation, as the elasto-plastic properties of a solid directly depend on dislocation glide motion. The image force $f(f_{x}, f_{y})$ per unit length of dislocation line may be calculated through the well-known Peach- Koehler formula [8], which yields

$$
\begin{aligned}
f_{x}-\mathrm{i} f_{y}= & B|\gamma|\left[\frac{\Phi_{p}\left(\zeta_{0}\right)+\overline{\Phi_{p}\left(\zeta_{0}\right)}}{\gamma}\right. \\
& \left.+\frac{\overline{\omega\left(\zeta_{0}\right)} \Phi_{p}^{\prime}\left(\zeta_{0}\right)+\psi_{p}^{\prime}\left(\zeta_{0}\right)}{\bar{\gamma} \omega^{\prime}\left(\zeta_{0}\right)}\right],
\end{aligned}
$$

where
$$
\omega(\zeta)=R(\zeta+m / \zeta)
$$

$$
\Phi_{p}(\zeta)=\varphi_{p}^{\prime}(\zeta) / \omega^{\prime}(\zeta)
$$

and $\varphi_{p}(\zeta)$ and $\psi_{p}(\zeta)$ are the perturbative potentials. The glide component of this force is soon calculated as the inner product $f \cdot B / B$.

## 2. Results

The special cases of the elliptic hole $(\Gamma=0)$ and rigid elliptical inhomogeneity $(\Gamma=\infty)$, for which very simple resolutive formulas are available [7], are considered first. Indeed, they are of remarkable practical interest, and may serve as a basis of comparison in a general approach.

For a fruitful discussion, it is essential to bear in mind the image force fields around circular inhomogeneities $(m=0)$. Therefore, Fig. 2 shows glide equiforce contours around a circular hole and a rigid disk, for plane strain $(v_{1}=0.1)$ and Burgers vector directed along the $x$-axis $(B_{y}=0)$. Then, Figs. 3 and 4 show the modifications of these contours when the inhomogeneity deviates from circularity, by stretching either in the $x$(glide)- or in the $y$(climb)-direction (here and in the following the term "stretching" in used in a purely geometrical sense). In particular, Fig. 3b and d refer to slit (Griffith) cracks, and Fig. 4b and d to rigid lines. In

![](./images/812321158270550016_2.jpg)

Fig. 2a and b. Contour plots of the dimensionless glide force on dislocation $(B_{y}=0)$ around a circular hole (a), and a rigid disk (b)

![](./images/812321158270550016_3.jpg)

Fig. 3a-d. Contour plots of the dimensionless glide force on dislocation $(B_{y}=0)$ around an elliptic hole. (a) $m=0.5$, (b) $m=1$ (crack), (c) $m=-0.5$, (d) $m=-1$ (crack)

![](./images/812321158270550016_4.jpg)

Fig. 4a-d. Contour plots of the dimensionless glide force on dislocation $(B_{y}=0)$ around rigid elliptical inhomogeneity. (a) $m=-0.5$, (b) $m=1$ (rigid line), (c) $m=-0.5$, (d) $m=-1$ (rigid line)

all graphs, dotted and point-dotted lines represent loci of *unstable* and *stable* glide equilibrium, respectively (the $y$-axis is always a locus of equilibrium), and the force is expressed in units of $B|\gamma|$.

Even at the first glance, shape effects appear rather substantial. The salient features may be summarized as follows:
(i) force intensity increases with stretching over most of the region near the inhomogeneity;
(ii) new equilibrium curves, or important modifi- cations of the initial ones, set up with stretching.

With regard to the latter feature, it is to be noted that a strong anisotropy arises. Actually when stretching occurs in the glide direction, an appreciable modifi- cation of the equilibrium curves is observable only for a hole (in the form of a new loop pointing toward the crack tip, see Fig. 3b), and only for strong elongations ($m\lesssim0.6$). On the contrary, when stretching occurs in the climb direction drastic changes of the equilibrium loci take place near both a hole and a rigid particle, and, as also shown by contours not recorded here, as soon as the shape deviates from the perfectly circular one ($m\lesssim0.01$). Around a hole (Fig. 3c and d) a new bell-shaped stable-equilibrium curve appears at the sides of the $y$-axis, while around a rigid particle (Fig. 4c and d) the initially unstable-equilibrium curve trans- forms into a loop (thus partly "stable"). As a con- sequence, we may at least suspect no negligible errors to be introduced (e.g., in fiber-reinforced composite design) by neglecting small deviations from circularity.

In order to discuss shape effects in the general case, we have selected a number of graphs (Figs. 5 and 6) showing the angular dependence of the glide force at a fixed distance from the ellipse's center ($r_0/R=5$), for plane strain ($v_1=v_2=0.3$) and $B_y=0$. Figure 5 refers to soft inhomogeneities ($\Gamma<1$), while Fig. 6 to hard ones ($\Gamma>1$). Point-dotted curves show the force exter- ted by circular inhomogeneities, and stretching in the climb direction is represented by negative values of the shape parameter $m$.

It is observed that, as expected, the force vanishes for $m=\pm1$ (a line inhomogeneity can exist only as either a crack or a rigid line). However, it would be wrong to infer a general monotonic lowering of glide force on increasing stretching. This could be assumed true only for $\Gamma$ near to 1 (Figs. 5a and b and 6a and b). When $\Gamma$ decisively differs from unity (Figs. 5c and d and 6c and d) the situation is more complex. For a circular inhomogeneity the curves maintain themselves rather smooth, whereas those for $m\neq0$ show noticeable oscil- lations. The amplitude of these oscillations increases with stretching, and, as a rule, this leads to the appearance of new equilibrium positions. Force in- tensity also increases with stretching, except in an angular range around $\varphi_0=0$ (which gets narrower on

![](./images/812321158270550016_5.jpg)

Fig. 5. Angular dependence of the dimension- less glide force on dislocation, $F_{g}$, around a soft elliptical inhomogeneity ($r_0/R=5$)

![](./images/812321158270550016_6.jpg)

approaching the limiting cases $\Gamma=0$ and $\Gamma=\infty)$. To sum up, a gradual shift is observable from the condition of force decreasing with stretching (small shear moduli difference) to that of force with oscillatory angular dependence and increasing with stretching (large shear moduli difference).

### 3. Conclusions
The shape of an inhomogeneity appears to be an important factor in determining dislocation glide motion. In particular, deductions based on the knowledge of the modulus effect for a given shape may no longer hold even for slight deviations from this shape. Less critical, yet evident, is the influence of material constant difference on shape effects. These results may be directly applicable to phenomena which involve dislocation rearrangement in the absence of external loading (e.g., annealing treatments). To some extent, they may also suggest how inhomogeneities' shape affects the behavior of an externally stressed solid. On this line, we are planning in the immediate to extend the model by the introduction of tractions at infinity.
Among other investigations suggested by the present results, we first point out the interaction of elliptical inhomogeneities with more general line singularities. This has important applications in the description of plastic zones near defects or inhomogeneities, and may be regarded as a generalization of the work by Vitek and Hirth [9]. The observed sensibility of dislocation trapping to inhomogeneity shape makes also interesting to consider possible feedback effects (because of shape variations produced by loading), though these should be properly treated by nonlinear elasticity. Finally, the resolution of problems involving geometrical forms other than elliptical, and three-dimensional geometries, may be stimulated by the present work.

### References
1. J. Dundurs, T. Mura: J. Mech. Phys. Solids 12, 177 (1964)
2. R.D. List: Proc. Cambridge Philos. Soc. 65, 823 (1969)
3. L. Stagni, R. Lizzio: J. Appl. Phys. 52, 1104 (1981)
4. A.C. Gangadharan, J. Dundurs: Indian J. Technol. 11, 410 (1973)
5. V. Vitek: J. Mech. Phys. Solids 24, 67 (1976)
6. G.P. Sendeckyj: J. Res. Nat. Bur. Stand. 73A, 546 (1969)
7. L. Stagni: J. Appl. Math. Phys. (ZAMP) 33, 315 (1982)
8. L. Landau, E. Lifshitz: *Theory of Elasticity* (Pergamon Press, London 1970) p.133
9. V. Vitek, J.P. Hirth: Scr. Metall. 11, 339 (1977)