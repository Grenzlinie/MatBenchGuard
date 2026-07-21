# The Effects of Free Edge Interaction-Induced Knotting on the Buckling of Monolayer Graphene

Hao-Yu Zhang$^{\rm a}$, Jin-Wu Jiang$^{\rm a, \ast}$, Tienchong Chang$^{\rm a}$, Xingming Guo$^{\rm a}$, Harold S. Park$^{\rm b}$

$^{\rm a}$Shanghai Institute of Applied Mathematics and Mechanics, Shanghai Key Laboratory of Mechanics in Energy Engineering, Shanghai University, Shanghai 200072, People's Republic of China
$^{\rm b}$Department of Mechanical Engineering, Boston University, Boston, MA 02215, USA

## Abstract

Edge effects play an important role for many properties of graphene. While most works have focused on the effects from isolated free edges, we present a novel knotting phenomenon induced by the interactions between a pair of free edges in graphene, and investigate its effect on the buckling of monolayer graphene. Upon compression, the buckling of graphene starts gradually in the form of two buckling waves from the warped edges. The collision of these two buckling waves results in the creation of a knot structure in graphene. The knot structure enables the buckled graphene to exhibit two unique post-buckling characteristics. First, it induces a five-fold increase in graphene's mechanical stiffness during the buckling process. Second, the knotted structure enables graphene to exhibit a mechanically stable post-buckling regime over a large (3%) compressive strain regime, which is significantly larger than the critical buckling strain of about 0.5%. The combination of these two effects enables graphene to exhibit an unexpected post-buckling stability that has previously not been reported. We predict that numerical simulations or experiments should observe two distinct stress strain relations for the buckling of identical graphene samples, due to the characteristic randomness in the formation process of the knot structure.

Keywords: Buckling, Edge Effect, Knotting Effect, Graphene

## 1. Introduction

Graphene is a quasi two-dimensional (2D) honeycomb lattice structure that exhibits extremely high in-plane stiffness [1] but very small bending stiffness [2-5]. The quasi 2D nature of graphene is the origin for many of the interesting phenomena involving graphene, including edge effects and buckling instability, which are of relevance to the present work.

For the buckling instability, Euler buckling theory [6] states that the critical compression strain, above which graphene is buckled, is inversely proportional to the in-plane stiffness $C_{11}$ and is proportional to the bending stiffness $D$; i.e., $\epsilon_c \propto D/C_{11}$. According to Euler buckling theory, the critical strain for graphene is very small. Consequently, the buckling process can be induced by very weak external disturbances such as thermal expansion [7]. As a result of the buckling phenomenon, graphene is bent or folded with a finite curvature, which can be used to manipulate many physical properties in graphene [8]. As a result, the buckling of graphene has attracted intensive research interest in past few years [9-20]. Besides graphene, a group of other quasi 2D materials, eg. ${\rm MoS}_2$ or black phosphorus, also have small critical buckling strains because the bending stiffnesses for these atomically thin materials are also very small [21, 22].

As another result of graphene's 2D nature, edge effects play an important role on its physical properties. Based on the Brenner atomic potential [23] and the finite element method, it was demonstrated that graphene's free edges can become warped due to the compressive edge stress [24]. The warping amplitude decays exponentially from the edge into the center; i.e., the height ($z$) of the warped configuration is $z \propto e^{y/l_c}$ with $l_c$ as the critical penetration depth. The critical penetration depth can be viewed as the size of the warped edge region. For narrow graphene nanoribbons, the size of the edge region can be comparable to or larger than the central region.

If the size of the edge region in graphene nanoribbons is sufficiently large, the free edges dominate most of graphene's physical properties. Edge reconstructions have been observed experimentally [25], which can be attributed to the thermal energy localized by the edge vibrations [26, 27]. Edge vibrations were also found to be responsible for the larger energy dissipation in graphene nanomechanical resonators [28, 29]. It was found that edge effects are the dominant factor for the friction between neighboring nanotubes in multi-wall carbon nanotubes [30], and a piece of graphene can be driven from a softer regime to the stiffer regime due to the edge effect [31]. While we have listed just a few examples here, free edges also have a strong effect on other physical properties in graphene (for review, see eg. Ref. [32]).

Although edge effects on the mechanical properties in graphene have been extensively studied, the edge effect on buckling has not been examined to-date. Furthermore, free

---
*Corresponding author
Email address: jiangjinwu@shu.edu.cn (Jin-Wu Jiang)

Preprint submitted to Journal of the Mechanics and Physics of Solids
September 25, 2021

edges almost always are present in pairs. However, in the aforementioned works, each free edge makes an independent contribution to those mechanical properties in graphene. If the width of the graphene is comparable with twice the critical penetration depth $l_c$, there should be a strong correlation and interactions between the pair of free edges. The effect from a pair of correlated edges on the mechanical properties of graphene has not been studied yet. We thus investigate the effect from a pair of correlated edges on the buckling phenomenon in graphene.

In this paper, we investigate the buckling process for graphene with a pair of free edges. Different from the usual abrupt buckling mode, we find that graphene is gradually buckled starting from the free edges if the two edges are warped in opposite directions. The gradual buckling is due to the formation of a knot structure that results from the collision of the buckling waves from the two edges. There are four major features brought by the knotting effect. (1) Graphene with knotted structure has a much higher mechanical stiffness than graphene without knotting during the buckling process. (2) It is more difficult to buckle narrower graphene nanoribbons with the knotted structure as the knot is stronger in narrower graphene. (3) As a result of the randomness in the knotting phenomenon, we predict that numerical simulations or experiments should observe two different buckling processes even for identical graphene samples with free edges. (4) The knot is formed by the collision of buckling waves from the two free edges, and the knot structure will be unknotted if the compressive strain is larger than a critical unknotting strain value. After unknotting, all graphene with different boundary conditions have the same final buckled structure.

## 2. Simulation details
The interaction between carbon atoms in graphene is described by the second generation Brenner potential [23]. For stretching or compression, the edges of the graphene in the strain direction, i.e. the +x and -x edges in Fig. 1 (a), have prescribed motion in the strain direction only, while free boundary conditions (FBC) are used in the out-of-plane direction. Before tension or compression, the system is thermalized to a targeted pressure and temperature within the NPT (i.e. the particles number N, the pressure P and the temperature T of the system are constant) ensemble for 200 ps. The Nosé-Hoover [33, 34] thermostat is used for maintaining constant temperature and pressure. After thermalization, graphene is stretched or compressed in the x-direction in Fig. 1 (a) by uniformly deforming the simulation box in this direction, while the structure is allowed to be fully relaxed in lateral directions during mechanical loading. The standard Newton equations of motion are integrated in time using the velocity Verlet algorithm with a time step of 1 fs. Molecular dynamics (MD) simulations are performed using the publicly available simulation code LAMMPS [35, 36]. The OVITO package was used for visualization [37].

![](./images/867772220561162704_1.jpg)

Figure 1: (Color online) Warped configuration at 1 K of a free edge in graphene of dimension $30 \times 80$ Å. Half of the system is shown in the figure, while the other half (with another warped edge) is not shown. (a) Perspective view of the warped edge. The warped shape is described by the function $z(x, y)=z_0+A \sin (\pi x / L) e^{-y / l_c}$. (b) z-position for atoms at $y=y_{\text {min }}$. (c) z-position for atoms at the middle plane $x=15$ Å. The color is with respective to the z-position of each atom. Graphene is compressed or stretched in the x-direction.

![](./images/867772220561162704_2.jpg)

Figure 2: (Color online) Potential energy for graphene nanoribbon described by $\mathbf{R} = \frac{1-\eta}{2}\mathbf{R}_{-} + \frac{1+\eta}{2}\mathbf{R}_{+}$, in which $\eta$ is an evolving parameter. Two lower insets correspond to $\eta = \pm 1$, while the top inset is the structure for $\eta = 0$.

![](./images/867772220561162704_3.jpg)

Figure 3: (Color online) Temperature dependence for the flipping probability of one isolated warped edge in a graphene nanoribbon of dimension $30 \times 80$ Å.

## 3. An isolated edge
### 3.1. Warped Configuration
It has been demonstrated that free edges are warped due to the compressive edge stress in graphene [24]. A typical warped edge configuration is illustrated in Fig. 1 (a). The dimension of the graphene is $30 \times 80$ Å. The two ends in the x-direction are fixed, while FBC is applied in the y-direction. Only half of the system is shown, while the other warped edge is not displayed. The structure is relaxed at 1.0 K. The warping amplitude decays exponentially from the free edge into the center. Fig. 1 (b) and (c) show that the height (z) of each atom can be well described by the function $z(x, y) = z_0 + A \sin(\pi x/L)e^{-y/l_c}$, where $L = 30$ Å is the length of graphene along the x-direction. Fitting parameter $A$ is the warping amplitude, and $l_c = 7.3$ Å is the critical penetration depth of the warping edge.

An isolated free edge can be warped either in the +z or -z direction, whose structures are denoted by $\eta = \pm 1$ in Fig. 2, and whose corresponding configurations are displayed as the two lower insets in the figure. Fig. 2 shows that these two warping configurations have the same potential energy, as they are symmetric with respective to the z=0 plane. It means that the probability for an isolated free edge to warp in the +z direction is the same as -z direction.

### 3.2. Thermally Induced Flipping of the Warped Edge
While the results in Fig. 2 were for a single temperature, it is intuitive that as temperature increases, the thermal vibration energy may become large enough to flip the warping direction of the free edge; i.e., the +z-warping edge can be flipped into the -z-warping edge, and vice versa. To determine the critical temperature, we plot in Fig. 3 the potential energy curve for the graphene structure evolved by parameter $\eta$. The fact that we are computing an energy landscape implies that these, and subsequent potential energy surface calculations are performed at 0 K. The graphene configuration with $\eta = -1$ corresponds to the structure shown in the left bottom inset (denoted by $\mathbf{R}_{-}$), where the edge is warped downward. Only half of the structure is shown, while the other half (not shown in the inset) remains unchanged during the $\eta$ evolution. The configuration with $\eta =$ +1 corresponds to the structure shown in the right bottom inset (denoted by $\mathbf{R}_{+}$), where the free edge is warped upward. A general graphene configuration is determined by parameter $\eta$ following the formula, $\mathbf{R} = \frac{1-\eta}{2}\mathbf{R}_{-} + \frac{1+\eta}{2}\mathbf{R}_{+}$. The top inset displays the graphene configuration corresponding to $\eta = 0$.

From the potential energy curve, the two configurations with $\eta = \pm 1$ are two stable states with the same potential; i.e., this is a bistable system. The atomic color is with respective to the z-coordinate of each atom. The potential barrier between configurations $\eta = \pm 1$ is $\Delta V = V_{\eta=0} - V_{\eta=-1} = 0.117$ eV. The number of atoms in the warped edge regime is $N_E = 4 \times (W \times l_c / s_0) = 4 \times (24.0 \times 7.3 / 10.48) = 64$, where $s_0 = 10.48$ Å$^2$ is the area for one cell containing four carbon atoms. The potential energy barrier per atom is thus about $\Delta V/N_E = 1.83$ meV/atom. The probability to overcome this energy barrier at finite temperature T is proportional to $e^{-\Delta V/k_B T}$, so the critical temperature can be extracted as $T_C = \Delta V/k_B = 18.3$ K. This critical temperature means that, for $T > T_C$, the free edge can be driven from configuration with $\eta = -1$ to the configuration with $\eta = 1$ purely by the thermal vibrations, so these two configurations can switch between each other by thermal vibrations.

To verify the above potential barrier argument, we perform MD simulations for the warped free edge in a graphene nanoribbon of dimension $30 \times 80$ Å. We ran 50 simulations for this graphene sample at each temperature. Each simulation is performed using a different random velocity distribution, while all other simulation conditions remain unchanged. The warping direction of the free edge is flipped in many of the simulations, based upon which the flipping probability is calculated. Fig. 3 shows the temperature dependence for the flipping probability of one isolated warped edge. The warping direction of the free edge can be flipped by thermal vibrations for temperatures above 20 K. It means that the thermal vibrations for $T > 20.0$ K are able to overcome the potential energy barrier of the warped free edge in Fig. 2, resulting in the flipping of the warped free

![](./images/867772220561162704_4.jpg)

Figure 4: (Color online) Structure of a pair of free edges at 1 K. (a) PBC case. Graphene is flat, with PBC in the y-direction. (b) FBC-1 case. The two edges are warped in the opposite direction. (c) FBC+1 case. The two edges are warped in the same direction.

edge. In contrast, there is almost no flipping of the warped free edge for temperatures below 20 K, which is very close to the critical temperature of 18.3 K for the warped edge in Fig. 2.

## 4. A Pair of Edges and the Knotting Effect

### 4.1. Structure for Interacting Edge Pair

We have discussed above the structure of an isolated free edge, but free edges normally show up in pairs, which we now consider. Fig. 4 shows three different configurations for a graphene nanoribbon of dimensions $30 \times 80$ Å where the two shorter edges are free, and where the two longer edges are fixed. Fig. 4 (a) shows that graphene at 1 K has a flat configuration if periodic boundary conditions (PBC) are applied in the y-direction. Fig. 4 (b) and (c) illustrate two possible edge structures for FBC along the y-direction. The warping directions of the pair of edges are in opposite directions in Fig. 4 (b), which will be referred to as the FBC-1 configuration; while the warping of the pair of free edges is in the same direction in Fig. 4 (c), which is referred to as the FBC+1 configuration.

### 4.2. Knotting Effect on Buckling

#### 4.2.1. Identification of Knotting Effect from Stress-Strain Relationship

A thin plate (like graphene) will buckle under a sufficiently large compressive loading [6]. The buckling phenomenon is typically described in two stages. First, external work is done to compress the plate, and the energy is accumulated as compressive strain energy in the plate. The planar structure for graphene is kept in this process. Second, after the compressive strain reaches a critical value $\epsilon_{c}$, and graphene's planar structure becomes unstable, buckling happens abruptly, where the compressive energy inside the planar structure is fully converted into the bending energy of the buckled structure. The value of the critical buckling strain can be determined by equating the compressive strain energy of the plate just prior to buckling and the bending energy in the buckled structure.

We note one important condition in the Euler buckling theory is that the plate is in a planar configuration at the beginning of the mechanical compression. As a result, there is no bending energy in graphene during the pre-buckling stage. However, for graphene with FBC, the free edge is warped into the non-planar shape $z(x, y)=z_{0}+A \sin (\pi x / L) e^{-y / l_{c}}$, so the bending energy coexists with the compressive energy in graphene even in the pre-buckling stage with $\epsilon<\epsilon_{c}$. As a result, the buckling process may be quite different due to the warped free edges in graphene.

We thus simulate the compressive response of graphene with length $L=30$ Å in the x-direction and width $W=80$ Å in the y-direction. Fig. 5 compares the stress-strain curves at 1.0 K for graphene with PBC, FBC-1, and FBC+1 configurations. For graphene with PBC, the stress-strain curve is as expected; i.e., the curve changes its slope at the critical buckling strain $\epsilon_{c}=0.0052$, at which point the structure is buckled abruptly.

![](./images/867772220561162704_5.jpg)

Figure 5: (Color online) Stress-strain curves for the compression of a graphene nanoribbon of dimension $30 \times 80$ Å at 1.0 K.

There are two different stress-strain curves (red and blue lines) in Fig. 5 corresponding to the buckling of graphene with FBC. Graphene with FBC+1 configuration has a similar stress-strain relation as the PBC configuration. However, there are several distinct features in the stress-strain relation of the FBC-1 case. First, the slope of the stress-strain curve changes gradually before the critical unknotting strain $\epsilon_{u}=0.0336$, indicating a gradual buckling mode of the graphene. Different from the standard critical buckling strain $\epsilon_{c}$, $\epsilon_{u}$ is a new critical strain, above which the knot structure is unknotted as shown in the following. Second, the achievable stresses are larger for the FBC-1 case, which indicates that graphene with FBC-1 configuration has a much higher mechanical stiffness during the buckling process. Third, for strain $\epsilon>\epsilon_{u}$, the stress-strain curve of FBC-1 case jumps down and coincides with the PBC and FBC+1 cases. The distinct stress-strain relation indicates some novel effects in the buckling of graphene with FBC-1 configuration, two of which we highlight now.

4

![](./images/867772220561162704_6.jpg)

Figure 6: (Color online) Width dependence for the S factor of graphene buck- ling at 1.0 K. The length of the graphene is 30 Å.

First, to provide a quantitative description for the buckling process, we compute the S factor based on the stress-strain curve. The S factor is useful in capturing the buckling effect on the stiffness of the material [38], and is defined as $S = \frac{Y_f}{Y_i}$, with $Y_i$ and $Y_f$ as the Young's modulus before and after buck- ling at the critical strain $\epsilon_c$, respectively. The S factor is usually smaller than 1, because the stiffness is reduced by buckling. Fig. 6 shows the S factor for the buckling of graphene with width $W \in [20, 1000]$ Å. The S factor for graphene with PBC configuration is the lowest one, about 0.2, so the stiffness is greatly reduced by the buckling of graphene with PBC. The S factor is also width independent for graphene with PBC. The S factor in graphene with FBC-1 case is the largest one among all of the three configurations. In particular, the S factor for FBC-1 is close to 1 for narrow graphene with widths $W < 50$ Å, which suggests that the stiffness of the graphene with FBC-1 is essen- tially unaffected by buckling. In other words, the mechanical stiffness for graphene with FBC-1 configuration is nearly five times larger than the stiffness of graphene with PBC. For wide graphene with width $W > 80$ Å, the edge effect becomes neg- ligible and the S factors for graphene with PBC, FBC-1, and FBC+1 configurations are quite similar.

Second, as can be seen in Figs. 5 and 6, the knotting effect enables graphene to show a fairly stable, post-buckling regime whose duration of about 3% compressive strain as seen in Fig. 5 is nearly 6 times larger than the elastic strain that graphene un- dergoes before buckling. Therefore, not only can graphene sus- tain significantly more compressive strain after buckling due to the knotting, it is also very mechanically stable, particularly if the width is smaller than about 80 Å, as shown in Fig. 6. To- gether, these effects demonstrate a new post-buckling stability in graphene that has not previously been reported.

### 4.2.2. Illustrating the Knotting Effect During Buckling

According to the above discussions based on the stress- strain relations, free edges can enhance graphene's ability to resist buckling, particularly in graphene with the FBC-1 con- figuration. To explicitly disclose the differences in the buck-

![](./images/867772220561162704_7.jpg)

Figure 7: (Color online) MD snapshot for the buckling processes at 1.0 K of graphene with dimension $30 \times 80$ Å. Left: graphene with PBC. Right: graphene with FBC+1. Middle: graphene with FBC-1. The knot in graphene with FBC-1 configuration is depicted by the black arrow.

ling process, we show in Fig. 7 some typical MD snapshots for the buckling process of graphene at 1 K with PBC, FBC-1, and FBC+1 configurations. For graphene with PBC (left), the structure is buckled abruptly at strain $\epsilon_c = 0.0052$. For graphene with FBC+1 (right), the buckling starts from the two free warped edges. The edge buckling waves propagate into the interior region. Graphene is buckled after these two buck- ling waves meet in the central region at almost the same critical strain as PBC case (i.e., $\epsilon_c = 0.0052$). The buckled structure for FBC+1 case after $\epsilon > 0.02$ is the same as PBC case in the left panel, which explains why graphene with PBC and FBC+1 con- figurations have similar stress-strain curves just after the critical buckling strain in Fig. 5.

For graphene with the FBC-1 configuration (middle), the structure also buckles gradually, starting with the propagation of waves propagating in from the free warped edges. However, different from the FBC+1 case, a stable knot structure is formed in the center of the graphene sheet after the collision of these two edge buckling waves at strain of 0.006. Upon application of additional force, the knot propagates towards one of the free ends. This knotting configuration enhances the structure's me- chanical stiffness during buckling; i.e., higher stress is observed for FBC-1 in Fig. 5. The knotting structrue is unknotted at the critical unknotting strain $\epsilon_{u}=0.0336$, leading to the final buck- led structure. This final buckled structure is the same as the buckled structure for graphene with PBC and FBC+1 configu- rations. Hence, all of these three stress-strain relations in Fig. 5 fall onto one curve after $\epsilon > \epsilon_{u}$.

### 4.2.3. Potential Energy Analysis for Knotting Effect

We now provide a potential energy analysis for the knotting effect on the graphene buckling. Fig. 8 shows the potential en- ergy curve for a knotting configuration at strain $\epsilon = 0.02$; i.e.,
5

![](./images/867772220561162704_8.jpg)

Figure 8: (Color online) The potential energy curve of a knotting configuration at strain $\epsilon = 0.02$ for graphene of dimension $30 \times 80$ $\mathring{\text{A}}$. Graphene with FBC-1 configuration is compressed and a a knot is formed at strain $\epsilon = 0.02$. The configuration is evolved by parameter $\eta$ via $\mathbf{R} = \frac{1-\eta}{2}\mathbf{R}_{-} + \frac{1+\eta}{2}\mathbf{R}_{+}$, where $\mathbf{R}_{\pm}$ corresponds to the two configurations in the lower insets, denoted by $\eta = \pm 1$.

the graphene with FBC-1 configuration is compressed and a knot is formed at strain $\epsilon = 0.02$. The x-axis $\eta$ evolves the structure via $\mathbf{R} = \frac{1-\eta}{2}\mathbf{R}_{-} + \frac{1+\eta}{2}\mathbf{R}_{+}$. The structure with $\eta = -1$ corresponds to the structure shown in the left bottom inset ($\mathbf{R}_{-}$), which is the knotting structure. Only half of the structure is displayed here, as the other half is not changed during the evolving process. The graphene configuration with $\eta = +1$ corresponds to the structure shown in the right bottom inset ($\mathbf{R}_{+}$), which is a more stable structure with lower potential energy. This is the structure after the knot is unknotted. The top inset illustrates the configuration with $\eta = 0$. After the knot is unknotted, the structure transforms from $\mathbf{R}_{\eta=-1}$ to $\mathbf{R}_{\eta=0}$. For unknotting to occur, external work needs to be done to overcome the potential energy barrier $\Delta V = V_{\eta=0} - V_{\eta=-1}$.

The potential energy curve of the knotting at different strains $\epsilon$ is displayed in Fig. 9. Fig. 9 (a) shows that the potential energy curve becomes higher for larger strain, when the applied compression is smaller than 0.033. In particular, the potential energy barrier $\Delta V$ in Fig. 10 increases with increasing compression, so that it becomes more difficult to unknot the knot by applying strain. Fig. 9 (b) shows a quite different situation when the applied compressive strain is larger than 0.033, in which the potential energy curve decreases for increasing compression. In particular, Fig. 10 shows that the potential energy barrier $\Delta V$ drops rapidly, and becomes almost zero at $\epsilon = 0.03358$, so the structure can be deformed easily from the configuration with $\eta = -1$ to the configuration with $\eta = 1$. According to this $\eta$-potential argument, the knotting will be unknotted at strain $\epsilon = 0.03358$, which is exactly the same as the critical unknotting strain $\epsilon_{u}$ determined by the stress-strain curve from MD simulations in Fig. 5.

### 4.3. Parametric Effects on Knotting
We now perform a parametric analysis of the knotting effect, specifically taking into account the effects of graphene width, temperature, and orientation.

![](./images/867772220561162704_9.jpg)

Figure 9: (Color online) Potential energy curve of the knotting at different compressive strains $\epsilon$ for graphene of dimension $30 \times 80$ $\mathring{\text{A}}$. (a) Strain is smaller than 0.033. The potential energy curve becomes higher for larger strain. (b) Strain is larger than 0.033. The potential energy curve becomes lower for increasing strain.

![](./images/867772220561162704_10.jpg)

Figure 10: (Color online) The potential barrier $\Delta V$ for knotting at different compressive strains.

![](./images/867772220561162704_11.jpg)

Figure 11: (Color online) Stress-strain for graphene of width (a) $60$ Å, (b) $80$ Å,
and (c) $200$ Å. (d) The difference between the stress of the FBC-1 case and PBC
case at the critical unknotting strain $\epsilon_{u}$.

Fig. 11 shows the width dependence of the knotting effect
on the buckling of graphene with length $L = 30$ Å. Fig. 11 (d)
shows that the difference $(\Delta\sigma)$ between the maximum achiev-
able stress after buckling for the FBC-1 case and the other two
cases becomes smaller as the graphene width increases, and that
the knotting effect is negligible in graphene with width $200$ Å.
We can assume that graphene is divided into three regions: the
two warped edge regions of width $l_{\text{eff}}$ and one central region
of width $W - 2l_{\text{eff}}$, with $l_{\text{eff}}$ as the effective thickness for each
edge region and $W$ as the total width. The stress difference
$\Delta\sigma$ can be described by the formula, $\Delta\sigma = 2(l_{\text{eff}}/W)\Delta\sigma_{E}$, with
$\Delta\sigma_{E}$ as the stress difference at the same strain between the edge
region and the central region. From Fig. 11 (d), we have the
fitted coefficient $2l_{\text{eff}}\Delta\sigma_{E} = 165.2$. Using $l_{c} = 7.3$ Å as the
effective thickness, i.e., $l_{\text{eff}} = l_{c} = 7.3$ Å, it can be determined
that $\Delta\sigma_{E} = 11.3$ GPa. This value is slightly larger but close to
the stress difference (8.7 GPa) for graphene of $20$ Å in width,
which is dominated by the two edge regions. The two warped
edge regions cause the buckling to be gradual for small widths,
in contrast to the abrupt buckling of the central region for wider
graphene.

Fig. 12 shows the temperature dependence of the knotting
effect on the buckling of graphene with dimension $30 \times 80$ Å.
In Fig. 12 (a), the knotting structure in graphene with FBC-
1 configuration is unknotted at the critical unknotting strain
$\epsilon_{u} = 0.032$ at 20 K. The critical unknotting strain decreases to
$\epsilon_{u} = 0.0305$ at 40 K as shown in Fig. 12 (b), which indicates that
the knotting structure is easier to be unknotted at higher temper-
ature. It is because, at higher temperature, the thermal vibration
energy is larger, so it is easier to overcome the potential energy
barrier (in Fig. 10) of the knotting. Fig. 12 (c) shows the relation
between temperature and the unknotting strain, which discloses
an exponential decay of the unknotting strain with the increase

![](./images/867772220561162704_12.jpg)

Figure 12: (Color online) Temperature effect on the knotting phenomenon for
graphene of dimension $30 \times 80$ Å. The stress-strain relation for graphene at
temperature (a) 20 K and (b) 40 K. (c) The temperature dependence for the
unknotting strain, at which the knotting for graphene with FBC-1 configuration
is unknotted.

![](./images/867772220561162704_13.jpg)

Figure 13: (Color online) Stress-strain for the compression of graphene along the zigzag orientation at 1.0 K. The dimension of the system is $30 \times 80$ Å.

of temperature.

Finally, we discuss orientation effects on the knotting. In the above, we have discussed the knotting effect on the buckling of graphene which is compressed along the armchair orientation. Fig. 13 shows that the knotting phenomenon can also be found in the buckling of graphene that is compressed along the zigzag orientation. This figure has similar features as that for the armchair graphene shown in Fig. 5. The buckling process of graphene with FBC+1 configuration is similar as the buckling of graphene with PBC configuration. For graphene with FBC-1 configuration, the stress is obviously higher than the other two cases due to the knotting phenomenon.

### 4.4. Randomness for Knotting Phenomenon

#### 4.4.1. Width Dependence for Randomness

We have previously shown that for a free edge pair, each edge can be warped in the $\pm z$ direction, resulting in the FBC-1 or FBC+1 configuration shown in Fig. 4. The warping direction of each isolated free edge can be either in the +z or -z direction with the same probability, because these two types of warped edges have the same potential energy. On the one hand, if there is no coupling between the two free edges, a pair of free edges with FBC-1 configuration or FBC+1 configuration have the same potential energy, so the probabilities for the FBC-1 and the FBC+1 configurations are the same. On the other hand, if there is coupling between the two free edges, it is possible that graphene with FBC-1 configuration will have a different potential from the FBC+1 configuration, so the probability for FBC-1 and FBC+1 configurations will be different.

Indeed, Fig. 14 (a) shows that the probabilities for FBC-1 and FBC+1 configurations are width dependent at 1.0 K in graphene with FBC in the y-direction; i.e., with a pair of free edges in the y-direction. In this set of calculations, we perform thermalization for graphene with FBC in the y-direction within the NPT ensemble for 200 ps. The initial graphene structure is accompanied by a pair of free edges, but both edges are not warped at the initial stage. After thermalization, we find that

![](./images/867772220561162704_14.jpg)

Figure 14: (Color online) Probability for FBC-1 and FBC+1 cases. (a) Width dependence for the probability of FBC-1 and FBC+1 cases in graphene with length $L = 30$ Å at 1.0 K. (b) The width dependence for the potential difference, $\Delta V = V_{\text{FBC}-1} - V_{\text{FBC}+1}$, between graphene with FBC-1 and FBC+1 configurations.

![](./images/867772220561162704_15.jpg)

Figure 15: (Color online) Stress-strain for the compression of graphene at 1.0 K. FBC is applied in the y-direction. The dimension is $30 \times 80$ Å. The stress strain relation for graphene with FBC-1 configuration fall into the same curve, while the stress strain relation for graphene with FBC+1 configuration fall into another curve.

both free edges are warped and the pair of free edges are either in the FBC-1 configuration or the FBC+1 configuration. We performed 100 simulations for the same graphene at each width, but with different initial random velocity distribution. After thermalization, we counted the number of the structure with FBC-1 configuration and the FBC+1 configuration, and the corresponding probabilities were calculated. We find that for narrow graphene, the probability for structure with FBC-1 configuration is obviously larger than the structure with FBC+1 configuration. This difference decreases with increasing width, and vanishes for width above $50$ Å.

The above probability results can be analyzed in terms of the potential energy difference between the structure with FBC-1 and FBC+1 configurations. Fig. 14 (b) shows the potential energy difference $\Delta V = V_{\text{FBC-1}} - V_{\text{FBC+1}}$ for graphene of different width. It shows that the potential for the FBC-1 configuration is lower than FBC+1 configuration especially for narrow graphene, which is the reason for the larger probability of graphene with FBC-1 than FBC+1 configuration in narrow graphene. For wide graphene, the potential difference becomes very small, so the probabilities for FBC-1 and FBC+1 configurations are almost the same. For wide graphene, two warped free edges are far from each other, so they can be regarded as isolated warped edges. As we know from Fig. 2, the potential energy is independent of the warping direction (upward or downward) in an isolated free edge, so the potential energy difference between FBC-1 and FBC+1 is almost zero for wide graphene, leading to the same probability of FBC-1 and FBC+1 configurations in wide graphene.

The importance of the randomness is that most atomistic simulation studies start with a flat ideal initial graphene sheet with FBC, which will be thermalized to a stable structure at finite temperature. The resulting stable structure can be either FBC-1 or FBC+1 configuration with certain probability, which is width dependent as illustrated in Fig. 14 (a). Furthermore, Fig. 15 shows that the stress strain relations for all graphene with the FBC-1 configuration fall into one curve; while the stress strain relations for all graphene with the FBC+1 configuration fall into another curve. There is obvious difference between these two groups of stress-strain curves, which indicates that numerical simulations should obtain two different stress-strain relations for the same graphene, provided the free edges are not pre-warped in the initial structure.

![](./images/867772220561162704_16.jpg)

Figure 16: (Color online) Temperature dependence for the probability of FBC-1 and FBC+1 cases in graphene of width $W = 20$ Å. (a) The probability for FBC-1 configuration is always larger than FBC+1 configuration. (b) The z-position for the two warped edges, which shows the correlated flipping exhibited by the two edges, i.e. when one edge flips its warping direction, the other edge will flip its warping direction simultaneously.

### 4.4.2. Temperature Dependence for Randomness
We showed in Fig. 14 (a) that graphene with width $W = 20$ Å has a larger probability in the FBC-1 configuration than the FBC+1 configuration. We also showed in Fig. 3 that an isolated warped free edge has larger probability to flip its warping direction at higher temperatures. Hence, it is natural to anticipate that the structure with FBC-1 configuration may be driven into the FBC+1 configuration by thermal vibrations at higher temperatures. In other words, it is expected that, for graphene with $W = 20$ Å, the probability of FBC-1 case will be reduced and becomes closer to the probability of FBC+1 case, if the temperature is increased. In this set of simulations, we initialized the velocity of the system with 50 different random velocity distributions for each temperature. The system was thermalized to its

9

thermally stable structure within the NPT ensemble for 200 ps. After thermalization, both free edges in graphene are warped, and they are either in the FBC-1 configuration or in the FBC+1 configuration. The numbers for FBC-1 and FBC+1 cases were collected and their probabilities were calculated accordingly.

In Fig. 16 (a), the probability for graphene with FBC-1 configuration is always larger than graphene with FBC+1 configuration in the whole temperature range. For low temperatures, it is reasonable that the probability for graphene with FBC-1 configuration is larger than FBC+1 configuration, because we know that the potential for FBC-1 is lower than FBC+1 for graphene of width $W = 20$ Å in Fig. 14 (b). However, it is surprising that the probability for graphene with FBC-1 configuration is still larger than graphene with FBC+1 configuration at higher temperatures. This surprising result is attributed to the correlated flipping exhibited by the two free edges in Fig. 16 (b), which displays the z-position for the two warped free edges. As can be seen, when the warping direction of one free edge is flipped, the warping direction of the other free edge also flips simultaneously. This correlated flipping mechanism maintains the FBC-1 configuration, which ensures the larger probability for the FBC-1 configuration even at higher temperatures.

### 5. Conclusion
In conclusion, we have demonstrated a novel knotting phenomena induced by the interaction between free edges during the compression of graphene. The knotting phenomenon has substantial effects on the mechanical properties of buckled graphene, in particular significantly elevating the stress that can be sustained during the buckling process, which results in a higher mechanical stiffness than graphene without knotting, and in enabling graphene to exhibit a stable post-buckling regime where the amount of strain that can be sustained is significantly larger than the pre-buckling elastic strain. The knotting process was shown to be most probable for narrow graphene ribbons at lower temperatures. Overall, we have shown that edge effects, which have previously been shown to cause undesired instabilities on the mechanical response of graphene, can be utilized to give surprising enhancements in mechanical performance.

### 6. Acknowledgements
The work is supported by the Recruitment Program of Global Youth Experts of China, the National Natural Science Foundation of China (NSFC) under Grant Nos. 11504225, 11472163, 11425209, and the start-up funding from Shanghai University. HSP acknowledges the support of the Mechanical Engineering department at Boston University.

### References
[1] Lee, C., Wei, X., Kysar, J.W., Hone, J.. Measurement of the elastic properties and intrinsic strength of monolayer graphene. Science 2008;321:385.
[2] Ou-Yang., Z.C., bin Su, Z., Wang, C.L.. Coil formation in multishell carbon nanotubes: Competition between curvature elasticity and interlayer adhesion. Physical Review Letters 1997;78(21):4055.
[3] Tu, Z.C., Ou-Yang, Z.C.. Single-walled and multiwalled carbon nanotubes viewed as elastic tubes with the effective youngs moduli dependent on layer number. Physical Review B 2002;65:233407.
[4] Arroyo, M., Belytschko, T.. Finite crystal elasticity of carbon nanotubes based on the exponential cauchy-born rule. Physical Review B 2004;69:115415.
[5] Lu, Q., Arroyo, M., Huang, R.. Elastic bending modulus of monolayer graphene. Journal of Physics D: Applied Physics 2009;42:102002.
[6] Timoshenko, S., Woinowsky-Krieger, S.. Theory of Plates and Shells, 2nd ed. McGraw-Hill, New York; 1987.
[7] Bao, W., Miao, F., Chen, Z., Zhang, H., Jang, W., Dames, C., et al. Controlled ripple texturing of suspended graphene and ultrathin graphite membranes. Nature Nanotechnology 2009;4:562-566.
[8] Cong, C., Yu, T.. Enhanced ultra-low-frequency interlayer shear modes in folded graphene layers. Nature Communications 2014;5:4709.
[9] Lu, Q., Huang, R.. Nonlinear mechanics of single-atomic-layer graphene sheets. International Journal of Applied Mechanics 2009;1(3):443-467.
[10] Patrick, W.J.. Buckling of graphene layers supported by rigid substrates. Journal of Computational and Theoretical Nanoscience 2010;7(11):2338-2348.
[11] Sakhaee-Pour, A.. Elastic buckling of single-layered graphene sheet. Computational Materials Science 2009;45(2):266-270.
[12] Pradhan, S.C., Murmu, T.. Small scale effect on the buckling of single-layered graphene sheets under biaxial compression via nonlocal continuum mechanics. Computational Materials Science 2009;47(1):268-274.
[13] Pradhan, S.C.. Buckling of single layer graphene sheet based on nonlocal elasticity and higher order shear deformation theory. Physics Letters, Section A: General, Atomic and Solid State Physics 2009;373(45):4182-4188.
[14] Frank, O., Tsoukleri, G., Parthenios, J., Papagelis, K., Riaz, I., Jalil, R., et al. Compression behavior of single-layer graphenes. ACS Nano 2010;4(6):3131-3138.
[15] Farajpour, A., Mohammadi, M., Shahidi, A.R., Mahzoon, M.. Axisymmetric buckling of the circular graphene sheets with the nonlocal continuum plate model. Physica E: Low-dimensional Systems and Nanostructures 2011;43(10):1820-1825.
[16] Tozzini, V., Pellegrini, V.. Reversible hydrogen storage by controlled buckling of graphene layers. Journal of Physical Chemistry C 2011;115(51):25523-25528.
[17] Rouhi, S., Ansari, R.. Atomistic finite element model for axial buckling and vibration analysis of single-layered graphene sheets. Physica E: Low-dimensional Systems and Nanostructures 2012;44(4):764-772.
[18] Giannopoulos, G.I.. Elastic buckling and flexural rigidity of graphene nanoribbons by using a unique translational spring element per interatomic interaction. Computational Materials Science 2012;53(1):388-395.
[19] Neek-Amal, M., Peeters, F.M.. Effect of grain boundary on the buckling of graphene nanoribbons. Applied Physics Letters 2012;100(10):101905.
[20] Shen, H.., Xu, Y.., Zhang, C... Graphene: Why buckling occurs? Applied Physics Letters 2013;102(13):131905.
[21] Jiang, J.W.. The buckling of single-layer $\text{mos}_2$ under uniaxial compression. Nanotechnology 2014;25:355402.
[22] Jiang, J.W.. Graphene versus $\text{mos}_2$: A short review. Front Phys 2015;10:106801.
[23] Brenner, D.W., Shenderova, O.A., Harrison, J.A., Stuart, S.J., Ni, B., Sinnott, S.B.. A second-generation reactive empirical bond order (REBO) potential energy expression for hydrocarbons. Journal of Physics: Condensed Matter 2002;14:783-802.
[24] Shenoy, V.B., Reddy, C.D., Ramasubramaniam, A., Zhang, Y.W.. Edge-stress-induced warping of graphene sheets and nanoribbons. Physical Review Letters 2008;101(24):245501.
[25] Gass, M.H., Bangert, U., Blel och, A.L., Wang, P., Nair, R.R., Geim, A.K.. Free-standing graphene at atomic resolution. Nature Nanotechnology 2008;3:676-681.
[26] Jia, X., Hofmann, M., Meunier, V., Sumpter, B.G., Campos-Delgado, J., Romo-Herrera, J.M., et al. Controlled formation of sharp zigzag and armchair edges in graphitic nanoribbons. Science 2009;323:1701.
[27] Engelund, M., Furst, J.A., Jauho, A.P., Brandbyge, M.. Localized edge

10

vibrations and edge reconstruction by joule heating in graphene nanostructures. Physical Review Letters 2010;104:036807.

[28] Kim, S.Y., Park, H.S.. The importance of edge effects on the intrinsic loss mechanisms of graphene nanoresonators. Nano Letters 2009;9(3):969-974.

[29] Jiang, J.W., Wang, J.S.. Why edge effects are important on the intrinsic loss mechanisms of graphene nanoresonators. Journal of Applied Physics 2012;111(5):054314.

[30] Guo, Z., Chang, T., Guo, X., Gao, H.. Thermal-induced edge barriers and forces in interlayer interaction of concentric carbon nanotubes. Physical Review Letters 2011;107(10):105502.

[31] Chang, T., Zhang, H., Guo, Z., Guo, X., Gao, H.. Nanoscale directional motion towards regions of stiffness. Physical Review Letters 2015;114(1):015504.

[32] Castro Neto, A.H., Guinea, F., Peres, N.M.R., Novoselov, K.S., Geim, A.K.. The electronic properties of graphene. Rev Mod Phys 2009;81(1):109-162.

[33] Nose, S.. A unified formulation of the constant temperature molecular dynamics methods. Journal of Chemical Physics 1984;81(1):511.

[34] Hoover, W.G.. Canonical dynamics: Equilibrium phase-space distributions. Physical Review A 1985;31(3):1695.

[35] Plimpton, S.J.. Fast parallel algorithms for short-range molecular dynamics. Journal of Computational Physics 1995;117:1-19.

[36] Lammps, . http://wwwcssandiagov/~sjlimp/lammpshtml 2012;.

[37] Stukowski, A.. Visualization and analysis of atomistic simulation data with ovito - the open visualization tool. Modelling and Simulation in Materials Science and Engineering 2010;18:015012.

[38] Coulais, C., Overvelde, J.T., Lubbers, L.A., Bertoldi, K., van Hecke, M.. Discontinuous buckling of wide beams and metabeams. Physical Review Letters 2015;115(4):044301.