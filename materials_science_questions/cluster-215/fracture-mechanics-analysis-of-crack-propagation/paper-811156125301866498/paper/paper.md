IOP Conference Series: Materials Science and Engineering

PAPER • OPEN ACCESS

# Investigation of limit state criteria for amorphous metals

To cite this article: A M Comanici et al 2016 IOP Conf. Ser.: Mater. Sci. Eng. 147 012100

View the article online for updates and enhancements.

This content was downloaded from IP address 197.231.179.174 on 23/07/2020 at 13:40

# Investigation of limit state criteria for amorphous metals

A M Comanici¹, A Sandovici² and P D Barsanescu¹

¹Mechanical Engineering, Mechatronics and Robotics Department, "Gheorghe Asachi"
Technical University of Iasi, Iasi, Romania
²Mathematics Department, "Gheorghe Asachi" Technical University of Iasi, Iasi, Romania

E-mail: ana.comanici@yahoo.com

**Abstract.** The name of amorphous metals is assigned to metals that have a non-crystalline structure, but they are also very similar to glass if we look into their properties. A very distinguished feature is the fact that amorphous metals, also known as metallic glasses, show a good electrical conductivity. The extension of the limit state criteria for different materials makes this type of alloy a choice to validate the new criterions. Using a new criterion developed for biaxial and triaxial state of stress, the results are investigated in order to determine the applicability of the mathematical model for these amorphous metals. Especially for brittle materials, it is extremely important to find suitable fracture criterion. *Mohr-Coulomb* criterion, which is permitting a linear failure envelope, is often used for very brittle materials. But for metallic glasses this criterion is not consistent with the experimental determinations. For metallic glasses, and other high-strength materials, *Rui Tao Qu* and *Zhe Feng Zhang* proposed a failure envelope modeling with an ellipse in σ-τ coordinates. In this paper this model is being developed for principal stresses space. It is also proposed a method for transforming σ-τ coordinates in principal stresses coordinates and the theoretical results are consistent with the experimental ones.

## 1. Introduction
In the past 30 years, there have been developed new high-strength materials such as amorphous metals (metallic glasses), nanocrystalline metals, and advanced technical ceramics.

All of these are brittle materials, which show a sudden failure, which in some cases can be catastrophic for structures. In particular, for this class of materials is extremely important to find fracture criterions that are able to predict critical loading conditions for complex state of stress.

First paper about a metallic glass has been published in 1960 [1] and presented a amorphous material called Au₇₅Si₂₅, produced by *Caltech*. These materials have a high importance for both scientific and commercial use due to their properties [2]-[4].

These types of metallic glasses are a category of alloys that presents a higher tensile yield strength, which also means a higher elastic strain limit by comparison with crystalline materials [2]. However, the experiments show a lower limit concerning their ductility.

Compared to other limit stress state theories, *Mohr-Coulomb* theory is more general and can be applied both to materials with ductile behavior, and brittle behavior.

Usually, for the materials that have very brittle behavior, a straight line approximates the limit stress state envelope. For this modeling, equivalent stress is calculated using the following equation:

$$\sigma_{eq} = \sigma_1 - K\sigma_3 \tag{1}$$

![](./images/811156125301866498_1.jpg)
Content from this work may be used under the terms of the Creative Commons Attribution 3.0 licence. Any further distribution of this work must maintain attribution to the author(s) and the title of the work, journal citation and DOI.
Published under licence by IOP Publishing Ltd

where

$$
K=\frac{\sigma_{L T}}{\sigma_{L C}} \tag{2}
$$

and $K$ is a constant of the material, expressed as the ratio of tensile limit stress and compression limit stress.

For ductile materials $\sigma_{LT} = \sigma_{LC}$, $K=1$ and *Mohr-Coulomb* theory is reduced to *Tresca* theory. *Tao R.* and *Feng Z.* showed that the *Mohr-Coulomb* linear theory does not give satisfactory results for metallic glasses. For this reason, the authors proposed the modeling of the limit stress state envelope with an ellipse in $\sigma$-$\tau$ coordinates.

This modeling was validated by experimental determinations for the $\text{Zr}_{65}\text{Fe}_5\text{Al}_{10}\text{Cu}_{20}$ metallic glass [5].

### 2. Elliptic failure envelope
Starting from the elliptical envelope equation in the coordinate system $\sigma$-$\tau$ (figure 1), in the paper [6] the authors expressed the ellipse equation depending on the principal stresses:

$$
\sigma_{eq}=\frac{1}{2\left(1-k_{ST}^{2}\right)}\left[\sigma_{1}+\sigma_{3}+\sqrt{\left(\sigma_{1}+\sigma_{3}\right)^{2}-4\left(1-k_{ST}^{2}\right)\left(\sigma_{1}\sigma_{3}+k_{ST}^{2}\sigma_{L}^{2}\right)}\right] \tag{3}
$$

where

$$
k_{S T}=\frac{\tau_{L}}{\sigma_{L T}} \tag{4}
$$

![](./images/811156125301866498_2.jpg)

![](./images/811156125301866498_3.jpg)

Figure 1. Mohr's limit stress state envelope (a) and its approximations with an arc of ellipse (b).

### 3. The transformation of coordinates
By cutting out a plate of constant thickness, that is in biaxial state of stress, an infinitesimal triangular prism (figure 2) and by doing the forces equilibrium, is obtained:

$$
egin{align}
\sigma &= \frac{\sigma_1 + \sigma_3}{2} + \frac{\sigma_1 - \sigma_3}{2}\cos2\theta \
\tau &= -\frac{\sigma_1 - \sigma_3}{2}\sin2\theta
\end{align}	ag{5}
$$

Mohr's circle equation is obtained by removing the angle θ from above relations.

![](./images/811156125301866498_4.jpg)

Figure 2. Infinitesimal triangular prism, cropped from a plate in biaxial stress state.

Knowing the coordinates of a point in σ-τ space, the question arises around the whereabouts of the coordinates in principal stresses space. As shown from the above equations, for this operation it is necessary to know the angle θ. If the angle is not known, the problem is solved for the elliptical envelope in the following.

Given the point $A(\sigma_0, \tau_0)$, with known coordinates, it is assumed without restricting the generality that the point A is at the interior of the failure envelope, where the safety factor is c = 1. It is placed on an ellipse concentric with the failure envelope. On this ellipse (drawn with dashed lines in figure 3), the safety factor is c> 1. For reasons of symmetry, of the two ellipses we retained only a quarter (figure 4).

The equation of the ellipse for which c=1 is:

$$
\frac{\sigma^{2}}{\sigma_{L}^{2}}+\frac{\tau^{2}}{\tau_{L}^{2}}=1 \tag{6}
$$

The ellipse containing point $A(\sigma_0,\tau_0)$ is likewise with the initial ellipse, and it is described by the following equation:

$$
\frac{\sigma^{2}}{\sigma_{A}^{2}}+\frac{\tau^{2}}{\tau_{A}^{2}}=1 \tag{7}
$$

with

$$
\begin{cases}
\sigma_{A}=k \sigma_{L} \\
\tau_{A}=k \tau_{L}
\end{cases} \tag{8}
$$

where $k$ is determined as imposing $A(\sigma_0,\tau_0)$ to belong to the ellipse (7):

$$
\frac{\sigma_{0}{ }^{2}}{k^{2} \sigma_{L}^{2}}+\frac{\tau_{0}{ }^{2}}{k^{2} \tau_{L}^{2}}=1 \tag{9}
$$

hence

$$
k=\sqrt{\frac{\sigma_{0}^{2}}{\sigma_{L}^{2}}+\frac{\tau_{0}^{2}}{\tau_{L}^{2}}}<1 \tag{10}
$$

![](./images/811156125301866498_5.jpg)

Figure 3. Limit stress state ellipse (full line) and concentric ellipse containing point A with known coordinates.

![](./images/811156125301866498_6.jpg)

Figure 4. Due to symmetry conditions, it is retained only a quarter of the system.

Figure 5 shows a quarter of the ellipse passing through A and *Mohr's* semicircle is tangent to the ellipse at this point. In this figure are noted:
- Q is center circle Q(a,0);
- (t) is the common tangent to the circle and ellipse;
- (n) is the QA line, which is normal to the tangent in point A (t ⊥ n).

![](./images/811156125301866498_7.jpg)

Figure 5. Ellipse quarter and *Mohr* semicircle, which are tangent in point A.

The equation of the tangent line to the ellipse in A is:

$$
\frac{\sigma \sigma_{0}}{\sigma_{A}^{2}}+\frac{\tau \tau_{0}}{\tau_{A}^{2}}=1 \tag{11}
$$

hence

$$
\tau=-\sigma \frac{\sigma_{0}}{\tau_{0}}\left(\frac{\tau_{A}}{\sigma_{A}}\right)^{2}+\frac{\tau_{A}^{2}}{\tau_{0}} \tag{12}
$$

It writes the slope of the line (t):

$$
m_{t}=-\frac{\sigma_{0}}{\tau_{0}}\left(\frac{\tau_{A}}{\sigma_{A}}\right)^{2} \tag{13}
$$

Since the lines (t) and (n) are mutually perpendicular, their slopes must meet the condition:

$$
(t) \perp(n) \Rightarrow m_{t} m_{n}=-1 \tag{14}
$$

Using this property, from equations (13) and (14), is written the slope for the line (n):

$$
m_{n}=\frac{\tau_{0}}{\sigma_{0}}\left(\frac{\sigma_{A}}{\tau_{A}}\right)^{2} \tag{15}
$$

The equation of the line (n) is:

$$
\tau-\tau_{0}=m_{n}\left(\sigma-\sigma_{0}\right) \tag{16}
$$

The centre of the circle, Q it is determined at the intersection of the Oσ axis with the line (n): {Q}=Oσ ∩ (n). Replacing point coordinates Q (σ=a and τ=0) in equation (16), results:

$$
a=\sigma_{0}\left(1-k_{S T}^{2}\right) \tag{17}
$$

where k<sub>ST</sub> is the report between the semi-major and semi-minor axis of the ellipse:

$$
k_{S T}=\frac{\tau_{A}}{\sigma_{A}}=\frac{\tau_{L}}{\sigma_{L}} \tag{18}
$$

Abscissa of the *Mohr* circle centre can be written according to the principal stresses (figure 5):

$$
a=\frac{\sigma_{1}+\sigma_{3}}{2} \tag{19}
$$

OAD triangle is used to determine the radius R = QA with Pythagorean theorem:

$$
R=\sqrt{\left(\sigma_{0}-a\right)^{2}+\tau_{0}^{2}} \tag{20}
$$

Results from equations (18) and (20):

$$
R=\sqrt{\sigma_{0}^{2} k_{S T}^{4}+\tau_{0}^{2}} \tag{21}
$$

*Mohr* circle radius can be expressed according to the principal stresses:

$$
R=\frac{\sigma_{1}-\sigma_{3}}{2} \tag{22}
$$

From equations (17), (20), (21) and (22), depending on the coordinates of point A we have the principal stresses:

$$
\sigma_{1}=\sigma_{0}\left[1-k_{S T}^{2}+\sqrt{k_{S T}^{4}+\left(\frac{\tau_{0}}{\sigma_{0}}\right)^{2}}\right]
\tag{23}
$$

and

$$
\sigma_{3}=\sigma_{0}\left[1-k_{S T}^{2}-\sqrt{k_{S T}^{4}+\left(\frac{\tau_{0}}{\sigma_{0}}\right)^{2}}\right]
\tag{24}
$$

Metallic glasses failure is dictated by shear and located on a very thin strip. The angle between this band and the load is usually much higher than 45° for tensile stress or slightly less than 45° at compression for the metallic glass strips. This angle is half of that formatted between normal (n) and Oσ axis (figure 6). The Mohr-Coulomb model with elliptical envelope can predict it and this represents a major advantage to the modified theory [5].

Conversely, if known coordinates in principal stresses space, the failure angle θ can be determined. For the tensile situation where σ₃=0 σ₁=σ<sub>LT</sub>. Substituting in equations (23) and (24), we determine the coordinates of the tangent point σ₀ and τ₀. The failure angle θ can be established with the relation:

$$
tg(2 \theta)=\frac{-\tau_{0}}{\sigma_{0}-a}
\tag{25}
$$

![](./images/811156125301866498_8.jpg)

Figure 6. Failure angle for metallic glasses strips under tensile state if stress (elliptic envelope).

The ratio in equation (23) and (24) has the following geometric significance (figure 3):

$$
tg \eta=\frac{\tau_{0}}{\sigma_{0}}
\tag{26}
$$

### 4. Verifications with experimental data
Metallic glasses are brittle materials. However, they have the tensile stress and compressive stress equal in module, which is in fact a feature of classic ductile materials. Table 1 presents the mechanical properties of metallic glass Zr₆₅Fe₅Al₁₀Cu₂₀ and the material coefficients, where σ<sub>y</sub> is 2.231 GPa.

**Table 1.** Experimental data [5] and values for K and $\mathrm{k_{ST}}^{A}$ for $\mathrm{Zr_{65}Fe_{5}Al_{10}Cu_{20}}$ metallic glass.

| $\tau_0$ [GPa] | $\sigma_0$ [GPa] | $\mathrm{k_{ST}}^{A}$ | K     |
|----------------|------------------|-----------------------|-------|
| 0.314          | 1.988            | 0.194                 | 0.976 |
| 0.468          | 1.748            | 0.289                 | 0.976 |
| 0.596          | 1.700            | 0.368                 | 0.976 |
| 0.665          | 1.477            | 0.410                 | 0.976 |
| 0.734          | 1.280            | 0.453                 | 0.976 |
| 0.748          | 1.088            | 0.461                 | 0.976 |
| 0.785          | 0.959            | 0.484                 | 0.976 |
| 0.822          | 0.696            | 0.508                 | 0.976 |
| 0.849          | 0.610            | 0.524                 | 0.976 |
| 0.878          | 0.513            | 0.542                 | 0.976 |
| 0.841          | 0.307            | 0.519                 | 0.976 |

where $\mathrm{k_{ST}}^{A}$ refers to the ellipse that contains the A point.

Table 2 shows the equivalent stresses calculated with the following criteria: classical *Mohr-Coulomb*, modified *Mohr-Coulomb* (with elliptic failure envelope) and respectively *von Mises*, for the material $\mathrm{Zr_{65}Fe_{5}Al_{10}Cu_{20}}$. They were also calculated the relative errors of equivalent stresses predicted with above criteria versus failure stress from experimental determinations. In addition, it is presented the failure angle $\theta$, for tensile stress of metallic glass strips.

**Table 2.** Equivalent stresses, errors and failure angle $\theta$ for $\mathrm{Zr_{65}Fe_{5}Al_{10}Cu_{20}}$.

| $\sigma_1$ [GPa] | $\sigma_3$ [GPa] | $\theta_T$ [deg] | $\sigma_{\text{eq MC}}$ [GPa] | $\sigma_{\text{eq MC mod}}$ [GPa] | $\sigma_{\text{eq vM}}$ [GPa] | $\mathrm{e_{MC}}$ [%] | $\mathrm{e_{MC\ mod}}$ [%] | $\mathrm{e_{vM}}$ [%] |
|------------------|------------------|------------------|-------------------------------|-----------------------------------|-------------------------------|-----------------------|-----------------------------|-----------------------|
| 2.236            | 1.591            | 51.687           | 0.683                         | 2.308                             | 1.994                         | 69.36                 | -3.46                       | 10.64                 |
| 2.093            | 1.112            | 53.659           | 1.007                         | 2.237                             | 1.813                         | 54.85                 | -0.28                       | 18.72                 |
| 2.108            | 0.832            | 55.547           | 1.297                         | 2.340                             | 1.839                         | 41.88                 | -4.89                       | 17.55                 |
| 1.938            | 0.518            | 55.255           | 1.432                         | 2.206                             | 1.738                         | 35.81                 | 1.13                        | 22.11                 |
| 1.796            | 0.237            | 54.846           | 1.565                         | 2.103                             | 1.690                         | 29.85                 | 5.74                        | 24.23                 |
| 1.639            | 0.074            | 53.608           | 1.567                         | 1.930                             | 1.603                         | 29.77                 | 13.47                       | 28.14                 |
| 1.551            | -0.082           | 53.003           | 1.631                         | 1.856                             | 1.593                         | 26.90                 | 16.79                       | 28.58                 |
| 1.358            | -0.325           | 51.152           | 1.675                         | 1.650                             | 1.547                         | 24.90                 | 26.02                       | 30.68                 |
| 1.308            | -0.423           | 50.584           | 1.720                         | 1.607                             | 1.563                         | 22.89                 | 27.97                       | 29.95                 |
| 1.253            | -0.529           | 49.871           | 1.769                         | 1.558                             | 1.585                         | 20.69                 | 30.16                       | 28.94                 |
| 1.070            | -0.621           | 47.811           | 1.676                         | 1.292                             | 1.481                         | 24.89                 | 42.11                       | 33.61                 |

From table 2, it is observed that the equivalent stresses predicted with the proposed model from this paper are affected by lower errors than those predicted by classical criteria. Also, the failure angles are close to the experimental data.

### 5. Conclusions
*Mohr-Coulomb* model with elliptic failure envelope, in $\sigma$-$\tau$ space, was proposed by *Rui Tao Qu* and *Zhe Feng Zhang* for metallic glasses. This model was implemented in the principal stress space in a previous work done by authors [6]. In this paper, we propose a method for transforming coordinates

from $\sigma$-$\tau$ space in the principal stress space. The model proposed by the authors predicts with much better accuracy the equivalent stress compared to classical criteria (von Mises and Mohr-Coulomb), for metallic glass $Zr_{65}Fe_5Al_{10}Cu_{20}$. In addition, the predicted failure angles are close to those experimentally determined.

## 6. References

[1] Klement W, Willens R H and Duwez P 1960 Non-crystallinestructure in solidifed Gold-Silicon alloys Nature **187** pp 869-870

[2] Telford M 2004 The case for bulk metallic glass Materials Today **7** pp 36 - 43

[3] Liu Y H, Wang G, Wang R J, Zhao D Q, Pan M X and Wang W H 2007 Super plastic bulk metallic glasses at room temperature Science **315** pp 1385-1388

[4] Guo H, Yan P. F, Wang Y B et al. 2007 Tensile ductility and necking of metallic glass Nature Materials **6** pp 735-739

[5] Tao R, Feng Z 2013 A universal fracture criterion for high-strength materials SCIENTIFIC REPORTS **3** pp 1117

[6] Comanici A M and Barsanescu P D 2016 Considerations on elliptical failure envelope associated to Mohr-Coulomb criterion IOP Conf. Series: Materials Science and Engineering ModTech conference June 2016

## Acknowledgments

This work was supported by Program - the Partnerships in priority areas - PN II developed with the support of MEN - UEFISCDI, project no. PN-II-PCCA-2013-4-0656, contract no. 59 / 2014.