![](./images/813122362563100672_1.jpg)
1359-6454(95)00436-X
Acta mater. Vol. 44, No. 8, pp. 3049-3058, 1996
Copyright © 1996 Acta Metallurgica Inc.
Published by Elsevier Science Ltd
Printed in Great Britain. All rights reserved
1359-6454/96 $15.00 + 0.00

# QUASI-CLEAVAGE PROCESSES DRIVEN BY DISLOCATION PILEUPS

T. ZHU, W. YANG and T. GUO

Department of Engineering Mechanics, Tsinghua University, Beijing 100084, China

(Received 23 June 1995; in revised form 21 November 1995)

Abstract—The present paper explores quasi-cleavage processes driven by dislocation pileups against a Dislocation Free Zone (DFZ). The nanoscopic growth of the main crack consists of sequences of nanocrack formation in DFZ and its subsequent linkage with the main crack. Under mode I loading, the equilibrium locations of individual dislocations and the equilibrium number of dislocations are determined by a minimum energy requirement. Three possible responses are revealed: cleavage without dislocation emission, cleavage after emitting certain amount of dislocations, and cleavage suppressed by incessant dislocation emissions. Accurate dislocations/FEM calculation indicates the emergence of a tensile stress peak ahead of the crack tip, as the dislocations pile up against the DFZ. The stress peak location and the number of emitted dislocations lead to a Crack Tip Opening Angle (CTOA) which is invariant during crack growth. Fracture resistance curves are obtained for quasi-statically growing cracks under the constant CTOA criterion. Copyright © 1996 Acta Metallurgica Inc.

## 1. INTRODUCTION

Recent experiments [1, 2] have revealed a mechanism of quasi-cleavage fracture: it proceeds by forming a nanocrack in the Dislocation Free Zone (DFZ) of large elastic distortion and then by linking the nanocrack with the main crack. Both experiments and previous theoretical analyses [1–6] suggest that this quasi-cleavage process is driven by dislocation pileups against the DFZ. DFZ plays an important role in the brittle versus ductile response of material, see Ohr [7]. It forms ahead of the main crack and translates as the crack propagates. Rice and Thomson [8] divided various materials into two groups: the intrinsically brittle materials in which cleavage occurs prior to any dislocation emissions, and the intrinsically ductile ones in which cleavage is prevented by dislocation emissions. However, the experiments of St. John [9], Lii et al. [3], Zielinski et al. [4], Huang and Gerbrich [5] and Marsh et al. [6] established that dislocation emission from sharp cleavage cracks do not necessarily guarantee ductile behavior in a cleavage solid. Consequently, a quasi-cleavage process emerges as an intermediate failure mechanism between the two extremes of cleavage and dislocation emission.

Dislocation generation at a crack tip involves two successive stages: the dislocation nucleation at the crack tip and the dislocation motion away from the crack tip. Two groups of brittle materials exist. The materials in the first group have high barriers to dislocation emission, such as the ones studied by Rice and Thomson [8]. The materials in the second group have low dislocation mobilities. The nucleated dislocations cannot escape from the crack tip region rapidly, and their back stresses suppress further dislocation emissions [10, 11]. Accordingly, the brittle versus ductile response is not only controlled by the nucleation event, but also by the mobility of the emitted dislocation from the crack tip.

A quasi-cleavage process driven by dislocation pileups can be envisaged as follows. The background resistance to dislocation motion comes from the lattice stress, see Chiao and Clarke [12], in the absence of other more stringent barriers such as grain boundaries, second phase particles and brittle–ductile interfaces [11]. Upon loading, dislocations emit from the crack tip and come to rest at locations where the corresponding driving forces are balanced by the lattice friction. These dislocations are inversely piled up as an array along a slip plane. A DFZ will be formed between the crack tip and the dislocation pileup. The DFZ restores the elasticity in the crack tip region, while the plastic deformation around it shields the applied stress intensity factor, e.g. see Yang [13]. This inner elastic cell is highly distorted [1, 2], and contains many microscopic defects to initiate a nanocrack. The TEM in-situ observation [1, 2] showed that the nanocrack is nucleated in the highly stressed DFZ and then linked to the main crack. The sequence repeats itself under increased loading. The quasi-cleavage proceeds as step-by-step nanoscopic crack growth. Combining this mechanism with another mechanism of dislocation confinement of non-penetrating barriers, see Hsia et al. [11], one gets a complete picture on quasi-cleavage processes relating to dislocation mobility.

The present paper aims at providing a mechanics description of the above mentioned quasi-cleavage

processes, under a mode I loading. Attention will be focused on several key aspects in a quasi-cleavage process, such as the lattice friction influence on DFZ formation, nanocrack initiation in the DFZ and the computational resistance curve. Most existing crack/dislocation calculations relate to mode II and mode III cases, only a few calculations of discrete dislocations under mode I loading have been performed. Brede [14] provided a computer simulation of dynamic dislocation emission which has captured most of the phenomena for the brittle-ductile transition in Si. However, this makes his model appropriate to the high applied loading rate, which is not a necessary requirement for cleavage driven by dislocation pileups. Several important phenomena of quasi-cleavage processes were revealed through the static crack/dislocation computations by the Minnesota research group [3–6]. Their mechanics model, however, suffers from two difficulties. Firstly, they approximated the pileup ahead of the DFZ by a superdislocation and several single or mini-dislocations, which is a simplification for the dislocation pileups. Secondly, they removed the stress field singularity at the crack tip to shift the stress maximum away from the crack tip. Birnbaum prompted a query that it might be an artifact of the simulation, see Lii et al. [3].

The plan of the paper is as follows. First we shall provide the equilibrium locations of individual dislocations, under given mode I loading, given lattice resistance and number of dislocations. The actual equilibrium number of dislocations will be determined from a minimum energy requirement proposed in this paper. The competition between cleavage and continued dislocation emission in the DFZ will be evaluated next. Three possible responses emerge: cleavage without dislocation emission, cleavage after a certain amount of dislocation emissions and cleavage suppressed by incessant dislocation emissions, all depending upon the interplay between the intrinsic fracture toughness and the lattice resistance to dislocation emission. Accurate mechanics analysis (without the ad hoc assumption to remove the crack tip singularity) reveals the formation of a tensile stress peak ahead of the crack tip as the dislocations pile up against the DFZ. We will show that the intensity and the width of this tensile stress peak are sufficient to nucleate a nanocrack under a Griffith criterion for quasi-brittle materials. Under certain circumstances, we show that the crack growth is accomplished by the consecutive linkages of the nanocracks, rather than the extension of the main crack. The spacing of the stress peak, and the blunting of crack tip by dislocation emissions, give rise to a critical Crack Tip Opening Angle (CTOA) to dictate the quasi-cleavage processes. The constant CTOA criterion enables us to extend the present analysis to the case of a quasi-statically growing crack, and a fracture resistance curve is obtained. The asymptote of this curve may serve as an indication for the apparent macroscopic fracture toughness, $K_{\text{IC}}$.

## 2. EQUILIBRIUM DISTRIBUTION OF DISLOCATION ARRAYS
Consider a plane strain, semi-infinite crack in the $x_1$-$x_2$ plane, as shown in Fig. 1. The crack tip situates at the origin, and the crack plane (which is also assumed as the cleavage plane) occupies the negative $x_1$-axis. A pair of symmetric slip systems emanate from the crack tip, and span an angle of $\alpha$ to the $x_1$-axis. In all calculations to follow, we will take $\alpha = 45^\circ$. Edge dislocations are regarded as straight line defects which may slide on slip planes.

The crack configuration is remotely loaded by a symmetric mode I stress intensity factor $K^{\text{app}}$, the equilibrium locations of the dislocations are denoted by $h_i$, $i = 1, 2, \dots, n$, and sequenced by the emission order. The integer $n$ is the equilibrium number of discrete dislocations in one arm of the symmetric slip planes.

### 2.1. Equilibrium locations of discrete dislocations
We first determine the equilibrium distribution of edge dislocations on a pair of symmetric slip planes, under a given dislocation number $n$. The driving force on a dislocation at $h_i$ in the presence of a crack and other dislocations at $h_j$ ($j = 1, \dots, i-1, i+1, \dots, n$) has been studied by Lin and Thomson [15]. It consists of three parts: the force due to the applied stress intensity factor, the image force and the interaction force due to other dislocations within a cracked body. The total driving force on the dislocation is summed as
$$
F_i = F_i^\text{K} + F_i^\text{image} + F_i^\text{inter} \tag{1}
$$
where
$$
F_i^\text{K} = \frac{K^{\text{app}}b}{2\sqrt{2\pi h_i}} \sin \alpha \cos \frac{\alpha}{2}
$$
$$
F_i^\text{image} = -\frac{\mu b^2}{4\pi(1 - \nu)h_i}
$$

![](./images/813122362563100672_2.jpg)

Fig. 1. Schematic illustration of the symmetric crack/dislocation configuration.

![](./images/813122362563100672_3.jpg)

Fig. 2. Equilibrium distribution of dislocations indicates an inverse pileup against DFZ. The ordinate is the line density of dislocation pileup divided by the average density, and the abscissa is the distance from the crack tip measured along the slip plane.

$$
F_{i}^{\mathrm{inter}}=\sum_{j=1, j \neq i}^{n} F_{i j}^{\mathrm{inter}} \tag{2}
$$

where $\mu$ denotes the shear modulus, $v$ the Poisson's ratio, and $b$ the length of Burgers vector. The last expression in equation (2) sums over the interactions of other dislocations to the $i$th dislocation, with $F_{i j}^{\text {inter }}$ being the interacting force on the $i$th dislocation by the $j$th dislocation pair (under the symmetric two-arm configuration). Detailed expression of $F_{i j}^{\text {inter }}$ is given by equation (A7) in the Appendix.

At an equilibrium configuration, the driving force on each dislocation is balanced by the lattice friction resistance $\sigma_{\mathrm{f}} b$. Applying this condition to each dislocation leads to $n$ equations to solve the $n$ unknown dislocation locations. Under prescribed values of the applied stress intensity factor $K^{\text {app }}$ and the friction stress $\sigma_{\mathrm{f}}$, this nonlinear equation system is solved by a dynamic relaxation scheme to determine the equilibrium locations of dislocations.

Figure 2 shows the equilibrium distribution of discrete dislocations for different levels of $K^{\mathrm{app}} / \mu \sqrt{ } b$ as 0.98, 1.13 and 1.26, where the lattice friction is fixed at $\sigma_{\mathrm{f}} / \mu=0.003$. The distribution of dislocations is expressed as the line density $\left(h_{i+1}-h_{i}\right)^{-1}$ divided by the average density $n / h_{n}$. Figure 2 demonstrates that the dislocations are indeed in the form of an inverse pileup. The least radius of DFZ, defined as the distance between the last emitted dislocation and the crack tip, decreases as $K^{\text {app }}$ increases. When $\sigma_{\mathrm{f}} / \mu=0.001$, the size of DFZ declines from $380 b$ at $K^{\text {app }}=0.6 \mu \sqrt{ } b$ to $125 b$ at $K^{\text {app }}=1.0 \mu \sqrt{ } b$; and when $\sigma_{\mathrm{f}} / \mu=0.002$, it declines from $280 b$ at $K^{\text {app }}=0.6 \mu \sqrt{ } b$ to $95 b$ at $K^{\text {app }}=1.0 \mu \sqrt{ } b$.

### 2.2. Equilibrium number of discrete dislocations

The evolution of the dislocation configuration is envisaged as threading motions of dislocation lines driven under a minimum energy requirement, as discussed by Hsia *et al.* [11]. This concept allows us to evaluate the equilibrium number of discrete dislocations by comparing the sum of the elastic strain energy and the total frictional work during dislocation threading. The importance of the energy consumption by friction was appreciated by Chiao and Clarke [12] in the investigation for materials with high friction stress. The central argument of minimum energy approach is as follows: in the presence of $(n-1)$ dislocations, if the total energy (including the work consumed by the movement of all dislocations) under a prescribed loading decreases by emitting an additional dislocation on the slip plane, then the state with $n$ dislocations is energetically preferable. In order to determine the equilibrium number of dislocations, we need to evaluate the total energy for different $n$ values. The $n$ value corresponding to the energy minimum is the equilibrium number of discrete dislocations. In certain cases, the total energy keeps declining as $n$ increases, until the existing dislocation pileup rejects any further dislocation emission. We take the maximum allowable $n$ value as the equilibrium number of dislocations in those cases.

The total energy consists of: (1) the self energy of the dislocations, $W_{\text {self }}$; (2) the self energy of the crack tip stress field, $W_{K}$; (3) the interaction energy between the dislocation stress field and the $K^{\text {app }}$ field, $W_{K-\mathrm{d}}$; (4) the interaction energy among various dislocation fields in a cracked continuum, $W_{\mathrm{d}-\mathrm{d}}$; (5) the surface energy to create dislocation ledges, $W_{\text {ledge }}$; and (6) the work consumed by the resisting friction stress, $W_{\text {lattice }}$. The total energy of the system containing $2 n$ dislocations on the symmetric slip planes can be summed as

$$
\begin{aligned}
W_{\text {total }}=W_{\text {self }}+W_{K} & +W_{K-\mathrm{d}} \\
& +W_{\mathrm{d}-\mathrm{d}}+W_{\text {ledge }}+W_{\text {lattice }}. \quad (3)
\end{aligned}
$$

The self energy of the crack tip field is unchanged by introducing additional dislocations, and thus irrelevant to the energy minimization process. The expressions for the other terms in equation (3) are listed as follows

$$
W_{\text {self }}=2 \sum_{i=1}^{n} \frac{\mu b^{2}}{4 \pi(1-v)} \ln \frac{h_{i}}{r_{\text {cutoff }}}
$$

$$
W_{K-\mathrm{d}}=-2 \sum_{i=1}^{n} \frac{K^{\mathrm{app}}}{\sqrt{2 \pi}} b \sqrt{h_{i}} \sin \alpha \cos \frac{\alpha}{2}
$$

$$
W_{\mathrm{d}-\mathrm{d}}=\sum_{i=2}^{n} \sum_{j=1}^{i-1} \int_{r_{\text {cutoff }}}^{h_{i}} F_{i j}^{\text {inter }} \mathrm{d} h
$$

$$
W_{\text {ledge }}=2 n \gamma b
$$

$$
W_{\text {lattice }}=2 \sum_{i=1}^{n} \sigma_{\mathrm{f}}\left(h_{i}-r_{\text {cutoff }}\right),
\tag{4}
$$

where $r_{\text {cutoff }}$ denotes the equivalent cutoff core radius required to initiate a dislocation near the crack tip. The derivations of the $W_{\text {self }}, W_{K-\mathrm{d}}$ and $W_{\text {edge }}$ terms in equations (4) follow the procedure by Hsia et al. [11]. The $W_{\text {lattice }}$ term sums over the consumption of individual dislocations above and below the crack extension line. The expression of the $W_{\mathrm{d}-\mathrm{d}}$ term needs some explanation: it is composed by summing all interaction energies between any dislocation (labeled by $i$) and the dislocations ahead of it (sequenced as $j=1, \ldots, i-1)$. Each contribution of the interaction energy is evaluated as the work of moving the $i$ th dislocation from the cutoff core distance from the crack tip to its equilibrium position, while the other dislocations remain at their equilibrium locations.

Figure 3 shows the total energy as a function of $n$ for a given lattice friction under different applied loads. The minimum points in Fig. 3 correspond to the equilibrium number of dislocations under the prescribed values of applied stress intensity factor $K^{\text {app }}$ and the friction stress $\sigma_{\mathrm{f}}$. Under a fixed lattice frictional resistance (say $\sigma_{\mathrm{f}} / \mu=0.002$ ), the equilibrium number of dislocations increases as $K^{\text {app }}$ increases, as one observes from various curves in Fig. 3 for $K^{\text {app }} / \mu \sqrt{ } b=0.600,0.640$ and 0.685 . Repeated use of the minimum energy principle leads to the equilibrium dislocation number versus applied stress intensity factor curves for different values of lattice friction, as shown in Fig. 4. The lattice resistance stress $\sigma_{\mathrm{f}}$ may range from $0.0005 \mu$ to $0.01 \mu$. In drawing Fig. 4, we take $\sigma_{\mathrm{f}} / \mu=0.001,0.002,0.004$, in a feasible range for quasi-cleavage processes. To conclude this section, we remark that the resistance to dislocation motion has been considered as a dry friction in the present calculation, though in many cases the friction is velocity dependent. Brede [14] proposed an elegant model to include shielding dynamics. The calculation demonstrated dramatic effects of kinetics confinement on dislocation emission. The present approach, though using a dynamic relaxation method to facilitate the numerical convergence, only aims at the equilibrium locations and the number of the dislocations. The dislocation number estimated by the minimum energy approach represents an upper bound of $n$ for a dislocation emission process.

![](./images/813122362563100672_4.jpg)

Fig. 3. Total energy as a function of dislocation number $n$, $\sigma_{\mathrm{f}} / \mu=0.002$.

![](./images/813122362563100672_5.jpg)

Fig. 4. Equilibrium dislocation number versus applied stress intensity factor $K^{\text {app }}$ curves for different lattice frictions.

## 3. STRESS DISTRIBUTION AHEAD OF THE BLUNTED CRACK TIP

Dislocations emitted from the crack tip have two effects on the crack tip stress field. First, they exert a back stress onto the crack tip and thereby shield the crack tip from the applied loading. Second, they blunt the crack tip and thereby reduce the tensile stress at the crack tip. In this section, we explore the stress distribution ahead of the crack tip. The next two subsections approximate the back stress induced by the dislocation pileups by the dislocation self stress plus a stress due to an effective shielding stress intensity factor. More accurate calculations considering blunted crack tip and discrete dislocation arrays will be explored in Section 3.3 by the finite element method.

### 3.1. Effective $K$ field approach

A dislocation ahead of a sharp crack tip sends a back stress to the crack tip vicinity. In an effective $K$ field approach, the back stress of a symmetric dislocation pileup pair is characterized by a shielding stress intensity factor, $K^{\text {shield }}$

$$
K^{\text{shield}} = \sum_{i=1}^{n} \frac{3\mu b}{\sqrt{2\pi h_{i}}(1 - v)} \sin \alpha \cos \frac{\alpha}{2}. \tag{5}
$$

The shielding effect of those dislocations would reduce the stress intensity factor presiding at the crack tip to $K^{\text{tip}}$

$$
K^{\text{tip}} = K^{\text{app}} - K^{\text{shield}}. \tag{6}
$$

The cleavage within the DFZ is dictated by $K^{\text{tip}} \geqslant K^{\text{intrinsic}}$, the latter represents the intrinsic fracture toughness of a dislocation free material.

Figure 5 shows the relation between the near tip stress intensity factors and the applied stress intensity factor, under different lattice friction stresses $\sigma_{\text{f}} = 0.001, 0.002, 0.004$. For a given lattice friction stress, the variation of $K^{\text{tip}}$ can be divided into three stages: $K^{\text{tip}}$ is identical to $K^{\text{app}}$ before dislocation emission; $K^{\text{tip}}$ continues to increase with $K^{\text{app}}$ after exceeding $K^{\text{emit}}$, the near tip stress intensity factor for dislocation emission, until it reaches the maximum value $K_{\text{max}}^{\text{tip}}$; $K^{\text{tip}}$ declines under further increase of $K^{\text{app}}$. The $K^{\text{tip}}$ versus $K^{\text{app}}$ curve in Fig. 5 is the upper envelope of the actual curve. The actual $K^{\text{tip}}$ curve drops at certain $K^{\text{app}}$ values by emitting a dislocation, and then climbs up rapidly before the emission of the next dislocation. Hirsch and Roberts discussed this zigzag curve in detail [16].

Denote $K^{\text{intrinsic}}$ as the intrinsic fracture toughness of a dislocation free solid. Different relationships among $K^{\text{intrinsic}}$, $K^{\text{emit}}$ and $K_{\text{max}}^{\text{tip}}$ result in three different responses. If $K^{\text{intrinsic}}$ is less than $K^{\text{emit}}$, the crack tip would be cleaved without dislocation emission; if $K^{\text{intrinsic}} > K_{\text{max}}^{\text{tip}}$, cleavage would be suppressed by incessant dislocation emissions; if $K^{\text{emit}} < K^{\text{intrinsic}} < K_{\text{max}}^{\text{tip}}$, cleavage would occur after a certain amount of dislocation emissions. The distinction among the above three near tip responses relies upon the interplay between the intrinsic fracture toughness and the lattice resistance to dislocation emission. The last category defines the quasi-cleavage processes studied in the present paper.

![](./images/813122362563100672_6.jpg)

Fig. 5. Near tip effective stress intensity factor $K^{\text{tip}}$ versus applied stress intensity factor $K^{\text{app}}$ curves. The hollow circles represent the $K^{\text{emit}}$ values, and the triangles indicate the $K_{\text{max}}^{\text{tip}}$ values.

### 3.2. Estimates on the blunting effect

For simplicity, we approximate the blunted crack tip by a notch with rounded tip of radius $\rho = nb \sin \alpha$. The stress field near the notch tip is composed of the stress field by the applied loading $\sigma_{ij}^{K}$ and the back stress field due to dislocation pileups. The latter can be further divided into two parts: the self stress field $\sigma_{ij}^{\text{d}}$ that corresponds to the infinite medium dislocation solution and the notch negation stress field $\sigma_{ij}^{\text{d-n}}$ that arises from the stress field to cancel the crack surface traction

$$
\sigma_{ij} = \sigma_{ij}^{K} + \sigma_{ij}^{\text{d}} + \sigma_{ij}^{\text{d-n}}. \tag{7}
$$

This subsection estimates the notch related stress fields, $\sigma_{ij}^{K}$ and $\sigma_{ij}^{\text{d-n}}$, through the effective $K$ fields. Along the positive $x_1$-axis, the tensile stress components of $\sigma_{ij}^{K}$ and $\sigma_{ij}^{\text{d-n}}$ are given by

$$
\sigma_{22}^{K} = \frac{2K^{\text{app}}}{\sqrt{\pi(\rho + 2x_1)}} \left(1 + \frac{\rho}{\rho + 2x_1}\right),
$$

$$
\sigma_{22}^{\text{d-n}} = -\frac{2K^{\text{shield}}}{\sqrt{\pi(\rho + 2x_1)}} \left(1 + \frac{\rho}{\rho + 2x_1}\right). \tag{8}
$$

The solution of dislocation self stress field $\sigma_{ij}^{\text{d}}$ in an infinite medium is given by

$$
\sigma_{22}^{\text{d}}(x_1) = \sum_{i=1}^{n} \sigma_{22}^{(i)}(x_1; h_i) \tag{9}
$$

where the detailed expression of $\sigma_{22}^{(i)}(x_1; h_i)$, which represents the self stress field for a symmetric dislocation pair of distance $h_i$ from the crack tip, has been derived in equation (A8) of the Appendix.

### 3.3. Accurate evaluation of stress distribution by FEM

The stress distribution near the DFZ is essential to understanding the step-by-step quasi-cleavage crack growth. It was noticed by Shastry et al. [17] that the effective $K$ field is invalid when the DFZ size is small, and the nonlocal effect of dislocation shielding should be considered.

As a departure from the effective $K$ field approach, we present an accurate evaluation of the stress distribution by FEM. The computation is conducted for the blunting crack configuration containing symmetric arrays of discrete dislocations. The inner 8 layers of the finite element mesh of a side notched disc configuration are shown in Fig. 6. The actual grid contains a total of 1709 quadrilateral elements (arranged in 45 layers) and 1792 nodes. A highly refined grid is laid out within a region around the notch. Traction due to the remote field $K^{\text{app}}$ is imposed on the outer boundary whose distance to the crack tip is chosen to be about $10,000b$. The negatives of dislocation stresses in infinite medium $(-\sigma_{ij}^{\text{d}})$ are

![](./images/813122362563100672_7.jpg)

Fig. 6. Finite element mesh for the notch/discrete dislocation calculation. Only the inner eight layers of the mesh are shown. The complete mesh contains 45 layers of elements focused at the notch tip.

### 3.4. Patterns of crack growth
As mentioned above, the stress distribution along the crack extension line exhibits two peaks. As the remote loading increases, the first peak reduces while the second peak intensifies. Bonds will break when the peak stress exceeds a certain bond breaking stress $\sigma_{\text{cr}}$, leading to microscopic defects. Two patterns of defect growth exist: (1) the crack extends from the notch tip; and (2) a nanocrack forms ahead of the notch tip, and coalesces to the main crack. The actual pattern of crack growth will be selected by the stability of the above two defect patterns, according to the Griffith fracture criterion.

First, we consider the nanoscopic crack extension from the notch tip. The amount of crack extension, termed $a_{\text{notch}}$, is determined as the segment length along which the tensile stress $\sigma_{22}\left(x_{1}, 0 ; K^{\text{app}}\right)$ exceeds $\sigma_{\text{cr}}$. The stress intensity for the crack extension from the notch tip, $K^{\text{notch}}$, is given by

applied to the surfaces of blunted crack to restore the free surface condition. The stress distribution derived from the finite element analysis combining with the stress field of dislocations in an infinite medium provides an accurate stress distribution in front of the blunted crack tip. Figures 7(a) and 7(b) show the evolution of hoop stresses along the extension line from the blunted crack tip, for $\sigma_{\mathrm{t}} / \mu=0.002$ and 0.006 , respectively. As the applied loading $K^{\text{app}}$ increases, more dislocations are emitted under the energy minimum requirement and inversely piled up against the DFZ. These pileup dislocations change the stress distribution. It is shown in Fig. 7(a) that the stress distributions evaluated by the effective $K$ field estimate (shown by the dot-dashed curves) agree to the detailed FEM calculation of discrete dislocations (shown by the solid curves) at a distance of $350 \sim 400 b$ away from the notch tip. Nevertheless, the effective $K$ field estimates differ substantially from the detailed FEM calculation within a region of several notch widths. In contrast to the effective $K$ field estimates, the FEM calculations do not predict the hoop stress peaks at the notch tip when the applied loading is high. Instead, both Figs 7(a) and (b) indicate that the stress immediately ahead of the blunted tip reduces with increased loading, while a stress peak develops in the DFZ. This stress peak becomes more pronounced for larger value of $\sigma_{\mathrm{t}} / \mu$, as one compares the peak heights from Figs 7(a) and (b), where only the FEM calculations are plotted. The present FEM/discrete dislocation calculation is able to predict a hoop stress peak away from the notch tip, without an ad hoc removal of near tip singularity [3-6].

![](./images/813122362563100672_8.jpg)

Fig. 7. Hoop stress distribution along the extension line of the notch tip. (a) $\sigma_{\mathrm{t}} / \mu=0.002$; (b) $\sigma_{\mathrm{t}} / \mu=0.006$. In the top graph, the solid curves are an FEM calculation, and the dashed curves are the effective $K$ field estimates.

$$K^{\mathrm{notch}}=\sqrt{\frac{2}{\pi}} \int_{0}^{a_{\mathrm{notch}}} \frac{\sigma_{22}\left(x_{1}, 0 ; K^{\mathrm{app}}\right)}{\sqrt{a_{\mathrm{notch}}-x_{1}}} \mathrm{~d} x_{1}. \quad(10)$$

In deriving the above expression, we assume a geometry of semi-infinite crack in an otherwise infinite medium. The tensile stress at the notch tip is released by the negating tractions along newly exposed crack faces of length $a_{\text {notch }}$. Before the emission of the first dislocation, $K^{\text {notch }}$ calculated from equation (10) equals the applied stress intensity factor $K^{\text {app }}$.

We next consider the formation of a nanocrack under the second stress peak. The nanocrack has a length $2 a_{\text {nano }}$, which is determined as the segment length along which the tensile stress $\sigma_{22}\left(x_{1}, 0 ; K^{\text {app }}\right)$ exceeds $\sigma_{\mathrm{cr}}$, and centers at the location $x_{1}=x_{\text {peak }}$ where the hoop stress $\sigma_{22}$ peaks. Under a prescribed $\sigma_{\mathrm{cr}}$, the stress intensity factor for the nanocrack in the DFZ is
$$K^{\text {nano }}=\mu \sqrt{\frac{a_{\text {nano }}}{\pi}} \int_{-1}^{1} \sqrt{(1-s) /(1+s)} \tilde{\sigma}\left(s ; K^{\text {app }}\right) \mathrm{d} s(11)$$
where
$$\tilde{\sigma}\left(s ; K^{\mathrm{app}}\right)=\sigma_{22}\left(\left(x_{1}-x_{\text {peak }}\right) / a_{\text {nano }}, 0 ; K^{\mathrm{app}}\right) / \mu(12)$$
is the dimensionless normal traction near the nucleation site of the nanocrack. The above expressions use a standard formula of stress intensity factor for a central crack in an infinite medium with prescribed crack face traction. Formula (11) omits the interaction between the main crack and the nanocrack, as argued by Lii et al. [3].

We next discuss the variations of $K^{\text {notch }}$ and $K^{\text {nano }}$ with respect to the applied stress intensity factor $K^{\text {app }}$. The $K^{\text {notch }}$ versus $K^{\text {app }}$ curve follows the qualitative trend described in Section 3.1. As $K^{\text {app }}$ increases, $K^{\text {notch }}$ first increases linearly and then levels off as dislocations emit from the crack tip. Under a certain value of $K^{\text {app }}, K^{\text {notch }}$ reaches the maximum value (denoted as $K_{\max }^{\text {notch }}$ ) and decreases under further loading. The $K^{\text {nano }}$ versus $K^{\text {app }}$ curve, on the other hand, dominates the fracture response at higher $K^{\text {app }}$ values. $K^{\text {nano }}$ is identically zero under low applied load. It shoots up when the second stress peak in the DFZ is formed. As $K^{\text {app }}$ increases further, the height of the stress peak increases but $a_{\text {nano }}$ might decrease. As a manifestation of the two opposite tendencies, the $K^{\text {nano }}$ versus $K^{\text {app }}$ curve exhibits a maximum. This maximum value of $K^{\text {nano }}$ is denoted by $K_{\max }^{\text {nano }}$, it corresponds to the largest possible stress intensity factor to initiate a nanocrack during the loading process. Figure 8 shows the variations of $K^{\text {notch }}$ and $K^{\text {nano }}$ with respect to the applied stress intensity factor $K^{\text {app }}$ under a prescribed value of $\sigma_{\mathrm{f}} / \mu=0.006$. For this particular case, one observes that $K_{\max }^{\text {nano }}$ is higher than $K_{\max }^{\text {notch }}$, indicating the crack growth pattern may be dictated by the formation and the linkage of nanocracks.

![](./images/813122362563100672_9.jpg)
Fig. 8. Variations of $K^{\text {notch }}$ and $K^{\text {nano }}$ as the applied stress intensity factor $K^{\text {app }}$ increases, $\sigma_{\mathrm{f}} / \mu=0.006$.

Using the Griffith fracture criterion, one can determine the stability of a specific crack growth pattern
$$G=\frac{1-v}{2 \mu} K^{2}=2 \gamma\qquad(13)$$
where $G$ represents the energy release rate. The stress intensity factor $K$ in equation (13) can be either $K^{\text {notch }}$ or $K^{\text {nano }}$. The surface energy term in equation (13) is scaled by
$$\gamma=\beta \mu b.\qquad(14)$$

The factor $\beta$ ranges from 0.03 to 0.3 , and was estimated for many materials by Rice and Thomson [8]. For example, $\beta=0.052$ for $\mathrm{Si}, \beta=0.117$ for $\mathrm{Al}$, $\beta=0.168$ for $\mathrm{Cu}, \beta=0.208$ for $\mathrm{Au}$ and $\beta=0.267$ for $\mathrm{Na}$. The smaller the $\beta$ value, the more cleavable the material.

When the value of $\beta$ is small, $K^{\text {notch }}$ may reach the critical value first and the cleavage starts from the notch tip. The notch tip cleavage prevails when $\beta<\beta_{\text {notch }}$, with
$$\beta_{\text {notch }}=\frac{1-v^{2}}{4 \mu^{2} b} K_{\max }^{\text {notch }^{2}}.\qquad(15)$$

Under a higher value of $\beta$, namely $\beta \geqslant \beta_{\text {notch }}$, the crack extension from the notch tip of the main crack cannot satisfy the Griffith criterion (13). As $K^{\text {app }}$ increases and dislocations pile up against the DFZ, the stress intensity factor for the nanocrack, $K^{\text {nano }}$, may eventually reach the critical value if the $\beta$ value of the material falls below
$$\begin{aligned}
\beta_{\text {nano }}= & \frac{(1-v) a_{\text {nano }}}{4 \pi b} \\
& \times\left\{\int_{-1}^{1} \sqrt{(1-s) /(1+s)} \tilde{\sigma}\left(s, K^{\text {app }}\right) \mathrm{d} s\right\}^{2}. \\
& (16)
\end{aligned}$$

For the case that $K^{\text {nano }}$ is higher than $K_{\max }^{\text {notch }}$, an

intermediate range of $\beta$ exists such that $\beta_{\text{notch}} \leqslant \beta \leqslant \beta_{\text{nano}}$. A nanocrack will form ahead of the notch under a prescribed $\sigma_{\text{cr}}$ provided that

$$
K_{\text{nano}}^{\max } \geqslant 2 \sqrt{\frac{\beta}{1-v}} \mu \sqrt{b} \tag{17}
$$

and the nanocrack inside the DFZ will coalesce to the main crack. This cracking pattern is consistent with the experimental observation [1,2]. As a representative calculation, we take the material parameters of $\sigma_{\mathrm{f}} / \mu=0.006$, $\sigma_{\mathrm{cr}} / \mu=0.06$ and $v=0.3$. A nanocrack will be formed in the DFZ provided $\beta \geqslant \beta_{\text{notch}}=0.051$ and $\beta<\beta_{\text{nano}}=0.055$. As the applied loading $K^{\text{app}}$ reaches $1.82 \mu \sqrt{ } b$, $K^{\text{nano}}$ will be $0.56 \mu \sqrt{ } b$ and a nanocrack of half-length of $a_{\text{nano}}=17 b$ will form and coalesce to the main crack.

### 4. TOUGHENING DURING QUASI-STATIC CRACK GROWTH

We next consider the toughening during the step-by-step crack growth in a quasi-cleavage process. A crack wake configuration containing parallel arrays of discrete dislocations is proposed to explore the relation between shielding dislocations and the resistance curve. Assume that the crack moves quasi-statically through the medium, emitting $2n$ dislocations along the symmetric slip planes emanating from the current crack tip and then advancing a characteristic distance $\Delta a$ by linking a nanocrack formed ahead of it. By the analysis from the preceding section, we have

$$
\Delta a=x_{\text{peak}}+a_{\text{nano}}. \tag{18}
$$

The above crack growth amount, and the blunting width of crack tip by dislocation emissions, give rise to a critical Crack Tip Opening Angle (CTOA) to dictate the quasi-cleavage processes. Namely,

$$
\text{CTOA}=2 \tan ^{-1} \frac{n b \sin \alpha}{\Delta a}. \tag{19}
$$

The main crack will propagate under a constant CTOA furnished by the above formula. Figure 9 gives a schematic configuration for the crack tip dislocation emissions and their accumulation within the wake during the step-by-step crack growth. The experimental observation of Zielinski *et al.* [4] for Fe-2wt%Si showed that the cleavage crack left 3.5 slip traces of residual dislocations for every 100 nm crack growth, with an average of 18.6 dislocations per trace.

![](./images/813122362563100672_10.jpg)

Fig. 9. Schematics of quasi-static crack growth with symmetric arrays of dislocations left in the wake. Crack extends at a constant value of CTOA.

We now proceed to estimate the fracture resistance curve. As the crack tip advances, the driving force on the existing dislocations would drop. If the drop of the driving force on a previously emitted dislocation exceeds $2 \sigma_{\mathrm{f}} b$, the dislocation will move back to the crack surface. Because of the lattice friction, only a small fraction of emitted dislocations will retreat back to the cleavage surfaces. Their effect will be omitted in the subsequent analysis. The dislocations left behind in the wake exert shielding forces on the crack. For a crack to grow, the applied loading has to increase continuously. The toughness increment by the quasi-static crack growth is estimated here by a simple model that omits the interactions among various dislocation arrays. Under this assumption, the number, as well as the spacing, of dislocations on every slip trace is identical to the results we reported for the initiation of a quasi-cleavage process. The effect of the loading increment on the current crack tip is completely canceled by the effect from the shielding dislocations in the wake.

The constant CTOA criterion enables us to derive a fracture resistance curve. Crack advances at a constant value of $K^{\text{tip}}$ to cleave the DFZ, and at a constant value of CTOA to emit more dislocations and to shield the current crack tip. Suppose that the crack grows an increment of $\Delta a$ at each step, and has advanced $m$ steps since initiation. The applied stress intensity factor, $K^{\text{app}}$, to maintain the quasi-static crack growth would consist of two parts: the stress intensity factor for crack initiation, $K^{\text{init}}$, plus the effective shielding contributions from all subsequently emitted dislocation arrays. $K^{\text{init}}$ is defined implicitly as the specific $K^{\text{app}}$ value that nucleates the first nanocrack ahead of the main crack. That is, at

$$
K^{\text{app}}=K^{\text{init}}, \text{ one has } K^{\text{nano}}=2 \sqrt{\frac{\beta}{1-v}} \mu) \sqrt{b}. \tag{20}
$$

The shielding influences may be estimated by the effective $K$-field, see Section 3.1. The global shielding is contributed from dislocations on the parallel slip planes ($m$ planes above and $m$ planes below the crack extension line), with $n$ dislocations on each slip plane. The contribution from the symmetric dislocation arrays emitted from the current crack tip has already been included in the $K^{\text{init}}$ term. To summarize, one has

$$
K^{\text{app}}=K^{\text{init}}+\sum_{i=1}^{m} \sum_{j=1}^{n} K^{\text{shield}}(r_{i j}, \theta_{i j}). \tag{21}
$$

In equation (21), $K^{\text{shield}}(r, \theta)$ represents the shielding

![](./images/813122362563100672_11.jpg)

Fig. 10. Fracture resistance curve for a quasi-cleavage process. $\sigma_{\mathrm{f}} / \mu=0.006$, $\sigma_{\mathrm{cr}} / \mu=0.06$ and $\beta=0.055$.

stress intensity factor by a pair of symmetric dislocations locating at the polar coordinates $(r, \pm \theta)$ measured from the current crack tip, and its functional form is derived in equation (A10) of the Appendix. $r_{i j}$ and $\theta_{i j}$ are the radius and angle of the $i$ th dislocation on the $j$ th slip plane, given by

$$
r_{i j}=\sqrt{j^{2} \Delta a^{2}-2 j \Delta a h_{i} \cos \alpha+h_{i}^{2}},
$$

$$
\theta_{i j}=\tan ^{-1} \frac{h_{i} \sin \alpha}{h_{i} \cos \alpha-j \Delta a}. \tag{22}
$$

Figure 10 shows a typical fracture resistance curve as the crack grows, where we use the parameters of $\sigma_{\mathrm{f}} / \mu=0.006, \sigma_{\mathrm{cr}} / \mu=0.06$ and $\beta=0.055$ to plot it. The nucleation of the nanocrack occurs when the main crack blunts up to about $19 b$. The asymptote of this curve may serve as an apparent value of the macroscopic fracture toughness, $K_{\mathrm{IC}}$. Significant toughening has been achieved by consecutive emissions of dislocation arrays.

## 5. CONCLUDING REMARKS

A quasi-cleavage fracture mechanism driven by dislocation pileups has been proposed here under an accurate mechanics analysis of the first principle type. We are able to find the number and the distribution of dislocations emitted from the crack tip. Those dislocations pile up inversely against the DFZ ahead of the blunted crack tip. For materials with high lattice resistance, discrete dislocation evaluation and finite element analysis indicate that the stress peak may shift to some distances away from the notch tip as dislocations pile up. This stress peak shift leads to the nucleation of a nanocrack and its coalescence to the macroscopic crack. The prediction of the present model is consistent with the recent TEM in-situ observation by Chen et al. [1] and by Zhang et al. [2] that the nanocrack is preferably nucleated inside the DFZ.

For a quasi-statically moving crack, our analysis has revealed that the dislocations in the plastic wake exhibit a large shielding effect. A higher load has to be applied to drive the crack to grow at constant $K^{\text {tip }}$ and constant CTOA values. The asymptote of the fracture resistant curve may serve as an indication of the macroscopic fracture toughness.

Acknowledgements-The authors acknowledge the support to this research project by the National Natural Science Foundation of China and by the State Education Commission of China.

## REFERENCES

1. Q. Chen, W. Chu and C. Hsiao, Scripta metall. mater. 30, 1355 (1994).
2. Y. Zhang, Y. Wang, W. Chu and C. Hsiao, Scripta metall. mater. 31, 279 (1994).
3. M.-J. Lii, X.-F. Chen, Y. Katz and W. W. Gerberich, Acta metall. mater. 38, 2435 (1990).
4. W. Zielinski, M. J. Lii and W. W. Gerberich, Acta metall. mater. 40, 2861 (1992).
5. H. Huang and W. W. Gerberich, Acta metall. mater. 40, 2873 (1992).
6. P. G. Marsh, W. Zielinski, H. Huang and W. W. Gerberich, Acta metall. mater. 40, 2883 (1992).
7. S. M. Ohr, Mater. Sci. Engng 72, 1 (1985).
8. J. R. Rice and R. Thomson, Phil. Mag. 29, 73 (1974).
9. C. St. John, Phil. Mag. 32, 1193 (1975).
10. K. J. Hsia and A. S. Argon, Mater. Sci. Engng A176, 111 (1994).
11. K. J. Hsia, Z. Suo and W. Yang, J. Mech. Phys. Solids 42, 877 (1994).
12. Y.-H. Chiao and D. R. Clarke, Acta metall. 37, 203 (1989).
13. W. Yang, Microscopic and Macroscopic Fracture Mechanics. Defence Industry Press, in Chinese (1995).
14. M. Brede, Acta metall. mater. 41, 211 (1993).
15. I. H. Lin and R. Thomson, Acta metall. 34, 187 (1986).
16. P. B. Hirsch and S. G. Roberts, Phil. Mag. A64, 55 (1991).
17. V. Shastry, P. M. Anderson and R. Thomson, J. Mater. Res. 9, 812 (1994).
18. Z. Suo, Int. J. Solids Struct. 25, 1133 (1989).

## APPENDIX

### Stress Field for a Sharp Crack Interacting with a Pair of Symmetric Dislocations

The interaction between a sharp crack and dislocations has been extensively studied by Lin and Thomson [15]. In this Appendix, we complement their results by providing the complete stress field for a symmetric pair of dislocations interacted with a sharp crack. Our derivation consists of a simplified version from the work of Suo [18] for singularities interacting with interfaces and cracks.

We adopted complex potentials $\Phi(z)$ and $\Omega(z)$. Stress components are derived from

$$
\sigma_{11}+\sigma_{22}=2(\Phi(z)+\overline{\Phi(z)}) \tag{A1}
$$

$$
\sigma_{22}+i \sigma_{12}=\overline{\Phi(z)}+\Omega(z)+(\bar{z}-z) \Phi^{\prime}(z). \tag{A2}
$$

The solution is built on the superposition of two solutions. One corresponds to the infinite medium dislocation solution (labeled by a subscript "0") and the other arises from the stress field to negate the crack surface traction (labeled by a subscript "1")

$$\Phi(z)=\Phi_{0}(z)+\Phi_{1}(z)$$

$$\Omega(z)=\Omega_{0}(z)+\Omega_{1}(z). \tag{A3}$$

The potentials for a pair of dislocations at $s$ and $\bar{s}$ in an infinite plane can be written as

$$\Phi_{0}(z ; s)=\frac{B}{z-s}+\frac{\bar{B}}{\bar{z}-\bar{s}}$$

$$\Omega_{0}(z ; s)=\frac{\bar{B}}{z-s}+\frac{B(\bar{s}-s)}{(z-s)^{2}}+\frac{B}{z-\bar{s}}+\frac{\bar{B}(s-\bar{s})}{(z-\bar{s})^{2}} \quad(\mathrm{~A} 4)$$

where
$$B=\frac{\mu}{4 \pi(1-v) \mathrm{i}}\left(b_{1}+i b_{2}\right). \tag{A5}$$
$b_{1}$ and $b_{2}$ arc the Burgers vector components in $x_{1}$ and $x_{2}$ directions, respectively.

The potentials due to the negating stress are derived as

$$
\begin{aligned}
\Omega_{1}(z ; s) & =\bar{\Phi}_{1}(z ; s)=-\frac{1}{2}\left\{\frac{\bar{B}}{\bar{z}-\bar{s}}+\frac{B}{z-s}+\frac{\bar{B}}{z-s}+\frac{B}{z-\bar{s}}\right. \\
& +\frac{B(\bar{s}-s)}{(z-s)^{2}}+\frac{\bar{B}(s-\bar{s})}{(z-\bar{s})^{2}}+\frac{1}{\sqrt{z}}\left[\frac{\bar{B} \sqrt{\bar{s}}}{\bar{s}-z}+\frac{B \sqrt{s}}{s-z}\right. \\
& +\frac{\bar{B} \sqrt{s}}{s-z}+\frac{B \sqrt{\bar{s}}}{\bar{s}-z}-\frac{B(\bar{s}-s)}{2 \sqrt{s}} \frac{s+z}{(s-z)^{2}} \\
& \left.\left.+\frac{\bar{B}(\bar{s}-s)}{2 \sqrt{\bar{s}}} \frac{\bar{s}+z}{(\bar{s}-z)^{2}}\right]\right\}.
\end{aligned}
$$

Substituting equations (A4) and (A6) into (A3), and then into (A1) and (A2), we obtain the stress field of a pair of symmetric dislocations at $s$ and $\bar{s}$.

Listed below are some results used in the text of the present paper.

(1) Interaction force on one dislocation due to a symmetric dislocation pair. Consider the interaction force on a dislocation at $z_{i}=h_{i} \mathrm{e}^{i \alpha}$ due to a pair of symmetric dislocations at $s_{j}=h_{j} \mathrm{e}^{i \alpha}$ and $\bar{s}_{j}$. In the presence of a sharp crack, this interaction force is

$$
\begin{aligned}
F_{i j}^{\text {inter }}=\operatorname{Im}\left\{\mathrm { e } ^ { 2 i \alpha } \right. & {\left[\left(\bar{z}_{i}-z_{i}\right) \frac{\mathrm{d}}{\mathrm{d} z_{i}} \Phi\left(z_{i} ; s_{j}\right)\right.} \\
& \left.\left.+\Omega\left(z_{i} ; s_{j}\right)-\Phi\left(z_{i} ; s_{j}\right)\right]\right\}
\end{aligned}
$$

which furnishes a formula in the last expression of equation (2) in the text.

(2) Dislocation self stress along the crack extension line.
Consider the hoop stress along the crack extension line induced by the self stress of a symmetric dislocation pair at $s_{i}=h_{i} \mathrm{e}^{i \alpha}$ and $\bar{s}_{i}$. It can be written as

$$\sigma_{22}^{(i)}\left(x_{1} ; h_{i}\right)=\operatorname{Re}\left[\bar{\Phi}_{0}\left(x_{1} ; s_{i}\right)+\Omega_{0}\left(x_{1} ; s_{i}\right)\right] \quad \text { (A8) }$$

where $\bar{\Phi}_{0}\left(x_{1} ; s_{i}\right)$ and $\Omega_{0}\left(x_{1} ; s_{i}\right)$ can be evaluated from equation (A4), with $s$ replaced by $s_{i}$. Equations (A4) and (A8) help the evaluation of equation (9) in the text.

(3) $K$ field shielding by a symmetric pair of dislocations.
We conclude this appendix by a formula of $K$ field shielding due to a pair of dislocations at $s$ and $\bar{s}$. The part of the dislocation stress field that cancels the crack surface traction (denoted by a subscript "1") possesses the square root singularity near the crack tip. Therefore,

$$K^{\text {shield }}=-2 \sqrt{2 \pi} \lim _{x_{1} \rightarrow 0^{+}} \sqrt{x_{1}} \Phi_{1}\left(x_{1}\right). \quad \text { (A9) }$$

If the locations of the symmetric dislocation pair are at $s=r \mathrm{e}^{i \theta}$ and $\bar{s}(\theta \neq \alpha$ if the dislocation pair does not emit from the current crack tip), one obtains

$$
\begin{aligned}
K^{\text {shield }}= & \frac{\mu b}{(1-v)} \sqrt{\frac{2}{\pi r}} \\
& \cos \frac{\theta}{2}\left[\sin \alpha+\sin \frac{\theta}{2} \cos \left(\frac{3}{2} \theta-\alpha\right)\right], \quad(\mathrm{A} 10)
\end{aligned}
$$

where the Burgers vector is assumed to align with the slip plane. The above expression can be used in equation (21) in the text. For the special case of $\theta=\alpha$, equation (A10) is reduced to equation (5) in the text.