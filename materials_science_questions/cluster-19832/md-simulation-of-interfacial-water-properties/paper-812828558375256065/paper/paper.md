PAPER
View Article Online
View Journal | View Issue

![](./images/812828558375256065_1.jpg)

Cite this: Phys. Chem. Chem. Phys.,
2018, 20, 30492

Received 1st October 2018,
Accepted 19th November 2018

DOI: 10.1039/c8cp06126b

rsc.li/pccp

# Molecular features of hydration layers probed by atomic force microscopy

Zhengqing Zhang, $^{a}$ Seol Ryu, $^{b}$ Yoonho Ahn $^{* c}$ and Joonkyung Jang $^{* a}$

Structurally-ordered layers of water are universally formed on a solid surface in aqueous solution or under ambient conditions. Although such hydration layers are commonly probed via atomic force microscopy (AFM), the current understanding on how the hydration layers manifest themselves in an AFM experiment is far from complete. By using molecular dynamics simulation, we investigate the hydration layers on a hydrophilic or hydrophobic surface probed by a nanoscale tip. We study the density and molecular orientation of water, the free energy, and the force on the tip by varying the tip-surface distance. The force-distance curve oscillates due to the transition between the mono-, bi-, and tri-layers of water confined between the tip and the surface. If both the tip and the surface are hydrophobic, water confined between the tip and the surface evaporates due to the dewetting transition, giving a hydrophobic force without oscillation. The periodicity of oscillation in the force differs from the structural periodicity of water. With a close proximity of the tip, the molecular dipoles align parallel to the surface, regardless of whether the tip and the surface are hydrophilic or hydrophobic.

## Introduction

Water molecules are layered in the form of a solvation shell around an ion or a protein dissolved in aqueous solution. Under ambient conditions or in solution, a solid surface is naturally covered by multilayers of water adsorbed from the surroundings. $^{1}$ Such hydration layers on a solid surface play key roles in the wetting properties of the surface $^{2-5}$ and the freezing process involving heterogeneous nucleation. $^{6}$ Given their ubiquity and technological importance, the physicochemical properties of hydration layers on surfaces, known to be ordered and solid-like, $^{7-9}$ need to be understood at the molecular level.

The water structure on a substrate or between substrates can be revealed by X-ray or neutron reflectivity. $^{10-12}$ More frequently, however, the hydration layers and liquid-solid interfaces in general are probed by using atomic force microscopy (AFM). With the help of frequency-modulated AFM (FM AFM), one can measure the force on a probing tip with tens of pN resolution, and the tip-surface distance with 0.1 nm resolution. $^{13-15}$ If an AFM tip approaches a surface within a distance of 1 nm, a force oscillating with varying tip-surface distance is often recorded. $^{16-19}$ If the period of oscillation in the force-distance curve matches the molecular diameter of water, the oscillation is attributed to the transition between well-defined hydration layers such as the mono-, bi-, and tri-layers of water confined between the tip and the surface. $^{20}$

Currently, exactly how the hydration layers are manifested in an oscillatory force in an AFM experiment is rather controver- sial. Kaggwa et $a .^{19}$ found an oscillatory force-distance curve with a period of 0.25-0.29 nm for a hydrophilic surface. On the other hand, the force measured for a hydrophobic surface lacked oscillation with varying distance, irrespective of whether the probing tip is hydrophilic or hydrophobic. By contrast, Suzuki et $a .^{21}$ reported a force oscillating with a 0.25 nm period for the hydration layers formed on hydrophobic graphite. Similarly, Schlesinger and Sivan $^{22}$ reported a 0.5 nm oscillation in the force for hydration layers on a hydrophobic surface. Moreover, Gelb and Lynden-Bell $^{23}$ reported oscillating forces in their simu lation of an AFM experiment probing the hydration layers formed on a model hydrophobic surface.

Given the varied experimental results on the presence and period of an oscillatory force probed by AFM, a theoretical or simulation study might clarify exactly how the hydration layers manifest themselves in the force in AFM. The classical Derjaguin-Landau-Verwey-Overbeek (DLVO) theory $^{24}$ had to be modified to describe experimental AFM forces. Moreover, this continuum model cannot give any molecular details and insights. Kjellander $^{25}$ derived a theory for the pair correlation function, which predicts the oscillatory density profile and force of fluid trapped in a narrow slit. Amano et $a .^{26}$ developed a statistical mechanical theory that extracts the liquid structure from the force-distance curve measured in the surface force

$^{a}$ Department of Nanoenergy Engineering, Pusan National University, Busan 46241, South Korea. E-mail: jkang@pusan.ac.kr
$^{b}$ Department of Chemistry, Chosun University, Gwangju 61452, Republic of Korea
$^{c}$ School of Liberal Arts, Korea University of Technology and Education, Cheonan 31253, Republic of Korea. E-mail: yhahn@koreatech.ac.kr

30492 | Phys. Chem. Chem. Phys., 2018, 20, 30492-30501
This journal is @ the Owner Societies 2018

apparatus. These theories, however, are derived for simple liquids of spherical particles without long-ranged electrostatic interactions. Chialvo et al. $^{27}$ carried out molecular dynamics (MD) simulations to study liquid water confined between graphene plates, which is not the geometry relevant to AFM.

Herein, we use MD simulation to realistically model and reveal the molecular features of the AFM force curves. The previous MD simulations focused on the hydration layers grown on hydrophilic surfaces such as MgO, CaF₂, aluminum oxide, and muscovite. $^{28-31}$ The present study, by contrast, considers the tip and the surface, both of which can be hydrophilic gold (Au) or hydrophobic carbon (C). By calculating the free energy, we identify the metastable, stable, and transition states existing in the approach (retraction) of an AFM tip toward (from) a surface. The force-distance curves oscillate due to the transitions between tri-, bi-, and mono-layers of water regardless of the tip and the surface. The force on the C surface probed by the C tip, however, lacks oscillation because water evaporates between the tip and the surface due to the dewetting transition. We find the difference between the period of oscillation in the force and the structural period shown in the density.

## Results and discussion
### Water density distribution
We first investigate the hydration layers grown on a surface virtually isolated from a tip (which lies 5 nm above the surface). Fig. 1 (top) shows the density of water $\rho$ vs. the height from the surface $Z$ for the C (hydrophobic) and Au (hydrophilic) surfaces. With increasing $Z$, $\rho$ rises from zero, oscillates with a decreasing amplitude, and eventually levels off to a constant for $Z > 12$ Å. The densities of water far from the hydrophilic and hydrophobic surfaces both converge to the experimental density of bulk water (1.00 g cm⁻³). The density for the Au surface (squares) has three peaks at $Z = 3.0$, 5.6, and 9.3 Å. These peaks are 3.1 Å apart from each other (on average), which roughly matches the molecular diameter of water ($\sim$3.0 Å). $^{20,32}$ These peaks therefore originate from the first, second, and third layer of water on the Au surface. Hydration layers also develop on the hydrophobic C surface, giving rise to two peaks with density at $Z = 4.0$ and 7.0 Å (circles). Overall, the peaks of the density above the C surface are shorter and broader than those for the Au surface, because the hydration layers on the C surface are less ordered. The zero density at $Z = 3.0$ Å (at which $\rho$ peaks for the Au surface) indicates that there is a depletion layer of water near this hydrophobic surface. The thickness of the depletion layer is estimated as the difference between the locations of the first peaks of the Au and C surfaces, 1 Å. The depletion layer is also visible in the snapshot illustrated in the right inset of Fig. 1 (top). Consequently, the water layers, compared to those on the Au surface, are less closely packed on the hydrophobic C surface.

![](./images/812828558375256065_2.jpg)

Fig. 1 Density of water $\rho$ vs. the height from the surface $Z$. Shown in the top are the densities above the Au (squares) and C (circles) surfaces virtually isolated from tips ($D = 5$ nm). Shown in the middle and bottom are the local densities of water for the tips and surfaces separated by $D = 1.56$ nm. Here, $\rho$ is calculated by averaging over molecules below the tip (inside the box drawn in the left inset of the middle panel). In the middle, $\rho$ is plotted vs. $Z$ for the Au surface probed by the Au (triangles) or C (stars) tip. In the bottom, $\rho$ is plotted for the C surface interacting with the Au (circles) or C (squares) tip. Lines serve as a visual guide only.

The density profile for the positioning Au or C tip 1.56 nm above the Au (C) surface is shown in the middle (bottom) of Fig. 1. Here, the peaks of $\rho$ near the surface are similar to those found for the isolated surface shown in the top panel. Now, $\rho$ also peaks near the tip. Owing to the sharp curvature of the tip, the peaks of $\rho$ near the tip are not as sharp or high as those found near the flat surface, especially near the hydrophobic C tip. These densities are the local densities of water molecules below the tip (inside the box drawn in the left inset, middle of Fig. 1). If all the molecules are included in calculating the densities, the majority of molecules not lying below the tip dominate and the resulting $\rho$ has no peak near the tip (not shown here).

Using MD simulation, Chialvo *et al.*³³ found that the density of water confined between graphene sheets is given by the product of densities from the isolated sheets on the left and right, a sort of Kirkwood superposition approximation.³³ We checked this superposition approximation by calculating the product of the densities of the isolated surface and the tip. The superposition approximation reproduced the positions, but not the heights, of the peaks in the density profiles shown in Fig. 1 (middle and bottom).

Free energy and force

Having seen that both the surface and the tip are layered with water molecules separately, we investigate the case where a tip is close to a surface. In particular, we unravel the stable and metastable structures of the hydration layers in the approach (retreat) of the tip toward (from) the surface. By calculating the potential of mean force (PMF) *vs.* the distance $D$ between the tip and surface (see the inset of the middle, Fig. 1), we estimate the relative stabilities of various (meta)stable configurations and the free energy barriers existing between these configurations. Moreover, the gradient of the PMF curve gives the average force measured in an AFM experiment.

Fig. 2 (top) plots the PMF *vs.* $D$ for the Au surface probed by the Au (broken line) or C (solid line) tip. In both cases, the PMF oscillates with changing $D$, giving rise to multiple minima. The minima in PMF are marked by circles with labels (m, b, t, c′, m′, and b′) and their snapshots are shown in the right of Fig. 2. Depending on the tip, the PMF for the Au surface shows different locations of the extrema and amplitudes of oscillation.

![](./images/812828558375256065_3.jpg)

Fig. 2 Profiles of PMF and force for the Au surface probed by the Au or C tip. The PMF (top) and force (bottom) are plotted *vs.* the distance between the tip and surface, $D$. The minima of the PMF and the zeros of the force correspond to the (meta)stable configurations marked as circles with labels m, b, t, c′, m′, and b′. The snapshots of the (meta)stable configurations are shown in the right.

With the Au tip above the Au surface, the PMF shows three minima-, m, b, and t, which, respectively, correspond to the mono-, bi-, and tri-layers of water sandwiched between the tip and the surface. The monolayer configuration, m, is by far the most stable, lower in energy than those (b and t) of the bi- and tri-layers by 53.4 and 64.8 $k_\text{B}T$, respectively. We define the period of oscillation in the PMF (or force) curve as the distance between two neighboring minima. The PMF for the Au tip above the Au surface has a period of oscillation of 3 Å on average, as the distances between t and b and between b and m are 2.7 and 3.3 Å, respectively. By moving the tip toward the surface from the trilayer configuration t, $D = 11.3$ Å, the PMF faces a free energy barrier of 2.8 $k_\text{B}T$ at $D = 9.8$ Å, followed by the minimum at the bilayer configuration b ($D = 8.0$ Å). With shortening $D$ further, another free energy barrier of 20.8 $k_\text{B}T$ appears at $D = 7.0$ Å, followed by the monolayer configuration m. The high barrier for the transition from the bi- to mono-layer (b to m) indicates that even the second layer strongly adheres to the hydrophilic Au surface. Further decreasing $D$ from m steeply increases the PMF. Hence, the monolayer cannot be displaced to enable contact of the tip with the surface.

The PMF of the Au surface probed by the C tip has two minima at the mono- and bi-layer configurations, m′ and b′, respectively. The minimum at the trilayer configuration is missing, because the third layer is ill-defined, presumably due to the presence of the hydrophobic C tip nearby. Instead, the PMF has a new minimum at $D = 2.9$ Å (denoted as c′) where the tip contacts the surface. The hydrophobic C tip, by displacing the monolayer of water, directly contacts the Au surface. One can also see two minima near c′ at $D = 3.8$ and $4.6$ Å resulting from the layering of water molecules at the acute ($\sim$45°) wedge made by the tip and the surface. The $D$ values of the mono- and bi-layer configurations, m′ and b′, respectively, are shifted by 0.7 and 0.8 Å toward values larger than those with the Au tip, m and b: the hydrophobic C tip creates a depletion layer around it and therefore a larger $D$ value is needed to accommodate the mono- and bi-layers of water between the tip and the surface. Owing to the round curvature of the C tip, the shifts in $D$ are slightly smaller than the thickness of the depletion layer found for the flat C surface above (=1 Å). The period of oscillation in the PMF, defined as the distance between m′ and b′, is 2.8 Å, slightly smaller than that found for the Au tip (=3.3 Å). Unlike with the Au tip, the bilayer configuration b′ is more stable than the monolayer configuration m′ (lower in free energy by 1.6 $k_\text{B}T$) with the C tip. The transition from b′ to m′ faces a barrier of 6.5 $k_\text{B}T$ at $D = 7.7$ Å. The transition from the monolayer (m′) to the tip contact (c′) encounters double barriers amounting to 28.1 and 5.6 $k_\text{B}T$ in height. Table 1 lists all the free energy barriers existing in the approach (decreasing $D$) and retreat (increasing $D$) of the tip for all combinations of the tip and surface.

By taking the numerical gradients of the PMF curves, we obtain the force–distance curves, as shown in the bottom of Fig. 2.

Table 1 Free energy barriers of the transitions between the (meta)stable configurations in the PMF curves. For each combination of the tip and the surface, we list the free energy barriers (in units of $k_BT$) during the approach (retreat) of the tip. No and infinite barriers are represented as 0 and $\infty$, respectively

| Free energy barrier | Trilayer $\leftrightarrow$ bilayer | Bilayer $\leftrightarrow$ monolayer | Monolayer $\leftrightarrow$ tip contact |
|---------------------|------------------------------------|-------------------------------------|----------------------------------------|
| Au subs./Au tip     | 2.8 (14.2)                         | 20.8 (74.1)                         | $\infty$ (0)                           |
| Au subs./C tip      | 6.5 (4.8)                          | 28.1 (5.0), 5.6 (5.3)               |                                        |
| C subs./Au tip      | 5.6 (7.0)                          | $\infty$ (0)                        |                                        |
| C subs./C tip       |                                    |                                     |                                        |

Each force curve oscillates with the same number of extrema as in the corresponding PMF curve. Note, however, that at the $D$ values giving the extrema in the PMF curves, the forces are zero: the (meta)stable configurations in the PMF, m, b, t, c', m', and b', appear on the zeros of the forces. Consequently, each force curve has minima at the $D$ values larger than those of the PMF curve. Table 2 lists the $D$ values at the force and PMF minima for all the combinations of the tip and the surface. The minima of each force are located at $D$ values consistently larger by 0.2-1.0 Å than those of the related PMF.

The force on the Au tip probing the Au surface (broken lines) has three attractive wells with depths of 90, 523, and 2528 pN near the tri-, bi-, and mono-layer configurations, t, b, and m, respectively. The repulsive peaks with heights of 151 and 1734 pN are found at $D$ = 10.2 and 7.4 Å, respectively. We define the amplitude of oscillation in the force near a (meta)-stable configuration as the difference between the maximum and minimum nearest to that particular (meta)stable configuration: e.g., the amplitude of oscillation at b is calculated as the difference between the maximum on the left, 1734 pN, and the minimum right to b, $-$523 pN (=2257 pN). Table 3 lists the amplitudes of oscillation in the force for all the combinations of the tip and the surface.

With the C tip above the Au surface, the greatest attractive force of 1007 pN is found at the contact of the tip with the surface (c'), along with two attractive wells with depths of 232 and 95 pN near the mono- and bi-layer configurations, m' and b', respectively. The amplitudes of oscillation in the force for the bi- and mono-layer configurations and for the contact of the tip are, respectively, 539, 2080, and 1797 pN (Table 2). These amplitudes are smaller than those found for the Au tip (2258 and 4262 pN for the bi- and mono-layers, respectively).

<table>
<caption>Table 2 Distances between the tip and the surface, $D$ values, at the minima of the PMF and force (in units of Å)</caption>
<thead>
<tr>
<th>$D$</th>
<th></th>
<th>Trilayer</th>
<th>Bilayer</th>
<th>Monolayer</th>
<th>Contact of the tip and the surface</th>
</tr>
</thead>
<tbody>
<tr>
<td>Au subs./Au tip</td>
<td>PMF</td>
<td>11.3</td>
<td>8.0</td>
<td>5.3</td>
<td></td>
</tr>
<tr>
<td></td>
<td>Force</td>
<td>12.2</td>
<td>8.6</td>
<td>6.1</td>
<td></td>
</tr>
<tr>
<td>Au subs./C tip</td>
<td>PMF</td>
<td></td>
<td>8.9</td>
<td>6.1</td>
<td>2.9</td>
</tr>
<tr>
<td></td>
<td>Force</td>
<td></td>
<td>9.4</td>
<td>7.1</td>
<td>3.1</td>
</tr>
<tr>
<td>C subs./Au tip</td>
<td>PMF</td>
<td></td>
<td>8.6</td>
<td>5.5</td>
<td></td>
</tr>
<tr>
<td></td>
<td>Force</td>
<td></td>
<td>9.1</td>
<td>6.0</td>
<td></td>
</tr>
<tr>
<td>C subs./C tip</td>
<td>PMF</td>
<td></td>
<td>9.8</td>
<td></td>
<td>3.2</td>
</tr>
<tr>
<td></td>
<td>Force</td>
<td></td>
<td>10.8</td>
<td></td>
<td>3.7</td>
</tr>
</tbody>
</table>

Table 3 Amplitudes of oscillation in the force. For every combination of the tip and the surface, we list the amplitude of oscillation in the force (in pN) near each (meta)stable configuration

| Amplitude of oscillation | Trilayer | Bilayer | Monolayer | Tip contact |
|--------------------------|----------|---------|-----------|-------------|
| Au subs./Au tip          | 241      | 2258    | 4262      |             |
| Au subs./C tip           | 539      | 2080    |           | 1797        |
| C subs./Au tip           | 348      | 528     |           |             |
| C subs./C tip            | 115      |         |           | 779         |

There are double wells between the contact, c', and the mono- layer, m', configurations. As mentioned above, these wells arise from the layering of molecules at the wedge made by the tip and the surface.

The greatest attractive force in the force-distance curve is called the pull-off force$^{34}$ and it is a measure of the adhesive strength of the tip to the surface. With the Au tip, for example, the pull-off force is found near m, where the PMF also has the deepest minimum. The greatest attractive force in this case matches the most stable state in the PMF curve. With the C tip however, the force is most attractive near c' (tip contact), but the bilayer configuration b' is the most stable. Therefore, the pull-off force is not necessarily found at the most stable configuration. In addition, as pointed out above, the $D$ value of the minimum in the force is consistently larger (by 0.2-1.0 Å) than that of the corresponding (meta)stable configuration appearing in the PMF.

We also point out that the period of oscillation in the force does not exactly match the period of oscillation in the related PMF. Table 4 lists and compares the periods of oscillation in the PMF and force curves. The period of oscillation in the PMF can be larger or smaller than that of the corresponding force, differing in magnitude by $\leq$ 0.9 Å. On the other hand, we find that the period of oscillation in the PMF directly matches the structural periodicity of confined water: the peaks of density are at the same locations as the minima of the PMF. Therefore, the periodicity of the force does not necessarily match the structural periodicity shown in the profiles of the density and PMF.

The forces found for the Au surface (Fig. 2) are the hydration forces needed to remove the hydration layers adsorbed on a hydrophilic surface. The hydration force is usually purely repulsive due to the difficulty in removing the hydration layers strongly adsorbed on a hydrophilic surface. The present hydra- tion forces, however, alternate between attraction and repul- sion with decreasing $D$ until they eventually become repulsive

<table>
<caption>Table 4 Periods of oscillation in the PMF (force) curves. For each combination of the tip and the surface, we list the period of oscillation defined as the distance between two neighboring (meta)stable configurations (in units of Å)</caption>
<thead>
<tr>
<th>Oscillation period</th>
<th>Trilayer $\leftrightarrow$ bilayer</th>
<th>Bilayer $\leftrightarrow$ monolayer</th>
<th>Monolayer $\leftrightarrow$ tip contact</th>
</tr>
</thead>
<tbody>
<tr>
<td>Au subs./Au tip</td>
<td>3.3 (3.6)</td>
<td>2.7 (2.5)</td>
<td></td>
</tr>
<tr>
<td>Au subs./C tip</td>
<td></td>
<td>2.8 (2.4)</td>
<td>3.1 (4.0)</td>
</tr>
<tr>
<td>C subs./Au tip</td>
<td></td>
<td>3.1 (3.1)</td>
<td></td>
</tr>
</tbody>
</table>

![](./images/812828558375256065_4.jpg)

Fig. 3 Profiles of PMF and force for the C surface probed by the Au or C tip. The PMF (top) and force (bottom) are plotted vs. D. The minima of the PMF and the zeros of the force correspond to (meta)stable configurations denoted by circles with labels m, b, c', and b'. The snapshots corresponding to the (meta)stable configurations are shown on the right. Shown as the inset at the top is the geometry of the Au tip at $D=3.96$ Å along with four water molecules stuck in the dimples of the end of the tip (drawn as red spheres).

at very small $D$ values. This alternating behavior was also reported in a previous MD simulation $^{28,29}$ and in an AFM experiment on a mica surface. $^{22}$

We move on to investigate the hydration layers on the hydrophobic C surface probed by the Au or C tip (Fig. 3). When probed by the Au tip, the PMF (broken line) oscillates with decreasing $D$ from 8.6 to $5.5$ Å, due to the transition from the bilayer to the monolayer (marked by b and m, respectively). The period of oscillation is $3.1$ Å, which is similar to that found for the Au surface. The monolayer configuration, m, is marginally more stable (by $1.4\ k_{B}T$) than the bilayer configuration, b. The transition from the bilayer to monolayer configuration is separated by a free energy barrier of $5.6\ k_{B}T$. Decreasing $D$ beyond m indefinitely increases the PMF and therefore the monolayer cannot be removed from the surface. This is rather unexpected as the hydration layer on a hydrophobic surface should be easy to remove. It turns out that four water molecules are stuck in the dimples at the end of the Au tip (drawn as the red spheres in the inset). These molecules block an approach of the tip below $D=4.0$ Å.

By contrast, the PMF with the C tip shows no oscillation. With decreasing $D$, the PMF reaches a shallow dip ($1.4\ k_{B}T$ in depth) at $D=9.8$ Å (denoted as b' at the top of Fig. 3). This distance matches the bilayer of water sandwiched between the tip and the surface. Upon decreasing $D$ further, the PMF reaches a short barrier of $0.9\ k_{B}T$ in height at $D=8.6$ Å. Upon reducing $D$ more, water molecules confined between the tip and the surface evaporate. This phenomenon is kind of a liquid-to- vapor phase transition under hydrophobic confinement called the dewetting transition. Consequently, the PMF monotonically decreases with reducing $D$ and reaches the deepest minimum ($43\ k_{B}T$ in depth) at $D=3.2$ Å, where the tip contacts the surface. Unlike with the Au tip, the metastable state with the monolayer configuration is completely missing. The bilayer configuration b' also has a very shallow $(<k_{B}T)$ dip that can easily be escaped via thermal fluctuation. Only the contact of the tip with the surface, $c'$, remains as a stable configuration robust to thermal fluctuation.

The force vs. $D$ for the C surface probed by the Au tip (bottom of Fig. 3) oscillates with the (meta)stable configura- tions, m and b, appearing on the zeros of the force. Again, the minima of the force are shifted to the right (by $0.5$ Å on average) from those of the PMF. As $D$ reduces, the force reaches a shallow (50 pN in depth) attractive well at $D=9.1$ Å. Upon decreasing $D$ further, the force becomes repulsive with a barrier of 298 pN in height at $D=7.7$ Å, followed by the greatest attractive (pull-off) force of 229 pN at $D=6.0$ Å. From there on, the force steeply increases and becomes repulsive with decreas- ing $D$. As listed in Table 3, the amplitudes of oscillation in the force near the mono- and bi-layer configurations are 528 and 348 pN, respectively. These values are at least a few times smaller than the amplitudes found for the Au surfaces probed by the Au (4262 and 2258 pN for m and b, respectively) and C(2080 and 539 pN for m' and b', respectively) tips (see Table 2).

On the other hand, the force on the C tip probing the C surface is largely attractive for relatively large $D$ values $(\sim 10$ Å). The force has a broad and deep attractive well of 709 pN in depth near the contact of the tip with the surface $(c')$. With decreasing $D$, the force reaches a shallow well of 45 pN in depth at $D=10.8$ Å, just right of the bilayer configuration (b'). Upon reducing $D$ further, the force reaches a barrier of 70 pN at $D=$ $9.0$ Å, just left of the bilayer configuration (b'). After that point, the force decreases down to the minimum at $D=3.7$ Å. The force in this case is a hydrophobic force that attracts two hydrophobic objects in water. The present hydrophobic force is used a tip with a radius $<1$ nm. The location of the minimum $3.7$ Å and the range of the present force $(\sim 10$ Å) are close to the experimental findings. The present force (709 pN) is much stronger than the experimental force (17 pN), however. This can be understood by noting that the present tip and the surface are C while the experimental tip and surface are made of hexamethyl- disilazane. This organic material (whose contact angle $=89^{\circ}$ ) is less hydrophobic than the present $C^{35}$ (whose contact angle $=108^{\circ}$ ) and therefore gives a weaker hydrophobic force.

Kinoshita et al. $^{36}$ developed a statistical mechanical theory, which, for a simple liquid, dissects the PMF between two hard- sphere solutes into the contributions due to entropy and enthalpy. In this way, they could tell whether the attraction between nonpolar solutes in water is driven or opposed by entropy. Unfortunately, the present simulation method does not

allow such an analysis. Presumably, the hydrophobic force in the present simulation is entropy driven as an entropically-opposed hydrophobic interaction was found for a rather special case of a ligand-cavity geometry. Ishida et al. $^{37}$ experimentally measured the hydrophobic force for a tip interacting with a surface made of the same material. In the case where the tip and surface materials have the same contact angles as that of the present C surface $(=108^{\circ})$, their pull-off force $(0.3 ~N ~m^{-1})$ is comparable with our calculation $(0.7 ~N ~m^{-1})$. The present hydrophobic force is much shorter in range $(<1.0 ~nm)$, however, than that found in their experiment $(\sim 20.0 ~nm)$, due to the fact that the tip radius of their experiment $(4-15 \mu m)$ is much larger than that of our simulation $(1.0 ~nm)$.

All the forces examined in this study, except for the $C$ tip above the $C$ surface, oscillate with varying $D$ because of the presence of hydration layers, formed even on the hydrophobic C surface. By contrast, Kaggwa et al. $^{19}$ reported oscillatory forces for a hydrophilic surface only and not for a hydrophobic surface, regardless of whether the probing tip is hydrophilic or hydro- phobic. Our results agree with Suzuki et al. $^{21}$ and Schlesinger et al., $^{22}$ who reported oscillatory forces for hydrophobic surfaces. We have seen above that the amplitudes of oscillation in the present force for the hydrophobic (C) surface are much smaller than those for the Au surface (Table 3). Also, the experimental force measured by Kaggwa et al. $^{19}$ is much smaller than the present one. Therefore, the amplitudes of oscillation in the force of Kaggwa et al. $^{19}$ for a hydrophobic surface should be much smaller and hardly detectable. We also note that the FM-AFM experiments by Suzuki et al. $^{21}$ and Schlesinger employed stiffer tips with smaller oscillations than those used in the experiment of Kaggwa et al. $^{19}$ It is well known that a smaller amplitude of an oscillating tip gives an improved signal-to-noise ratio inFM-AFM. $^{21}$

### Local density profile
As shown in Fig. 4, the local density of water vs. $D$ plot clearly illustrates the change in the number of hydration layers. With reducing $D$, the density decreases for both the Au (top) and C(bottom) surfaces, regardless of the tip. Except for the case where both the tip and the surface are $C$ , the density vs. $D$ plot illustrates multi-steps corresponding to the transitions between the mono-, bi-, and tri-layers of water. With decreasing $D$ , the density for the Au tip placed above the Au surface (drawn as triangles) steps down at $D=7.2 \AA$ , due to the transition from the bi- to mono-layer. The transition from the trilayer to bilayer does not appear as a discrete step (which should be near $10 \AA$ ). With decreasing $D$ from $7.2 \AA$ , the density steps down near D = 4.5 A, signaling the removal of the monolayer. The decrease in the density cannot continue down to the contact of the tip with the surface but stops at $D=4.0 \AA$ .

The local density vs. $D$ for the $C$ tip above the Au surface(drawn as stars at the top of Fig. 4) undergoes more steps. With reducing $D$ , the density steps down at $D=8.5 \AA$ , signifying the transition from the bi- to mono-layer. Upon further decreasing $D$ , this step is followed by a plateau and another step at $D=5.5 \AA$ . The step at $D=5.5 \AA$ indicates the removal of the monolayer.

![](./images/812828558375256065_5.jpg)

Fig. 4 Density profiles for all the combinations of the simulated tip and surface. At the top, the local density of water is plotted vs. $D$ for the Au surface probed by the Au (triangles) or C (stars) tip (top). Shown in the bottom are the densities vs. $D$ for the $C$ surfaces interacting with the Au(circles) and $C$ (squares) tips. Lines serve as a visual guide only.

The plateau between $D=8.5$ and $5.5 \AA$ is attributed to the transition state (the local maximum in PMF) lying between the bi- and mono-layers (shown in Fig. 2). Another plateau between $D=5.5$ and $2.9 \AA$ arises from the transition state between the monolayer and the contact of the tip shown in Fig. 2 (top).

For the $C$ surface probed by the Au tip (Fig. 4, bottom), the density steps down at $7.8 \AA$ with decreasing $D$ , arising due to the transition from the bi- to mono-layer. The other step near D = 4.5 A signals displacement of the monolayer. Due to the ever increasing free energy with decreasing $D$ from the monolayer configuration $m$ (Fig. 3, top), the decrease in the density is discontinued at $D=3.8 \AA$ . Finally, when both the tip and the surface are hydrophobic $C$ , the density shows a single deep step originating from the evaporation of the bilayer (dewetting transition).

Amano et al. $^{38,39}$ developed a quantitative theory that relates the force on a probe with the liquid density. The theory, however, was derived for the ideal case where the liquid is made of simple spherical molecules and the probe is a single liquid molecule. Nonetheless, Amano et al. $^{38,39}$ in agreement with the present work, observed that the peak locations of the density and force do not match with each other and the zeros of the force correspond to the (meta)stable states of the layered water.

Using MD simulation, Watkins et al. $^{28,29}$ identified three water layers with hexagonal lattice structure on a hydrophilic surface. In the MD simulation of a carbon nanotube tip interacting with a hydrophilic surface, Argyris et al. $^{30}$ found two layers of water on the surface and a single hydration layer around the tip. The MD simulation performed by Kobayashi et al. $^{31}$ reported three hydration layers on a muscovite surface, as found in the X-ray measurement of Cheng et al. $^{40}$ Similarly, we have shown above that two and three layers of water develop on the hydrophobic and hydrophilic surfaces, respectively. The hydration layers also formed around the present AFM tip. We also found that water molecules are packed more compactly on the hydrophilic surface, in agreement with the MD simulations of Sendner et al. $^{41}$ and Hu et al. $^{42}$

Using AFM experiments and MD simulations, Argyris et al. $^{43}$ found that two layers of water formed on a hydrophilic surface interacting with a hydrophilic tip. The second hydration layer was less ordered than the first one. In their MD simulation, Hu et al. $^{42}$ studied the effects of changing the hydrophobicity of the surface on the amplitude of oscillation in the AFM tip. The distance between the peaks of the density profile of water was $\sim 3.0$ Å for both the hydrophilic and hydrophobic surfaces. He et al. found that water molecules are closer to the hydrophilic surface than to the hydrophobic surface. A large attractive force was observed for the case where a hydrophobic (diamond) tip approaches the hydrophobic surface. All these findings of the previous studies agree with the present results. Neither of these previous studies, however, considered the effects of changing the wettability of the tip.

## Orientation distribution

The present tip and the surface nonspecifically interact (through van der Waals interactions) with water molecules. The hydrophilicity of the surface or the tip originates from the isotropic interaction between a water molecule and a solid atom. There are other hydrophilic surfaces (such as mica) that form specific hydrogen bonds with water molecules. Water molecules will then form a specific or preferential orientation near such a surface. It is unclear whether a specific or preferential molecular orientation of water exists for the present surfaces nonspecifically interacting with water molecules. In light of this question, we study the molecular orientation of water confined between each tip and the surface simulated in the present work. Above the monolayer distance from the surface, water molecules are randomly oriented, just as in the bulk water. On the other hand, the molecular orientation within the monolayer distance from the surface is biased. The molecular dipoles in the first hydration layer on the Au surface illustrate two pronounced orientations at $\theta=96^{\circ}$ ($\cos\theta=-0.1$) and $60^{\circ}$ ($\cos\theta=0.5$), as shown at the top of Fig. 5 ($D=50$ Å). This preferential orientation of water qualitatively agrees with the previous *ab initio* and classical MD studies. $^{44-46}$ On the C surface isolated from a tip ($D=50$ Å, bottom of Fig. 5), water molecules in the first layer are mainly oriented at $\theta=87^{\circ}$ ($\cos\theta=0.05$), meaning the dipoles are nearly parallel to the surface. This biased orientation quantitatively agrees with that previously found for water near a hydrophobic surface (a methyl-terminated gold surface). $^{47}$

We have seen that the present C and Au surfaces induce biased molecular orientation in the first hydration layers. We now study how the preferential molecular orientation is influenced by an approaching tip. In Fig. 5, the distribution of the dipolar orientation is plotted for $D=12$, 9, and 6 Å, which approximately accord with the configurations of the tri-, bi-, and mono-layers, respectively. With decreasing $D$ from 50 to 12 and 9 Å, the dipolar orientation does not change much: the double-humped distribution of the orientation for the Au surface (top of Fig. 5) remains nearly unchanged. It is only with the C tip above the Au surface (top right of Fig. 5) that the minor peak at $\theta=60^{\circ}$ ($\cos\theta=0.5$) slightly rises by shrinking the main peak at $\theta=96^{\circ}$ ($\cos\theta=-0.1$). With decreasing $D$ from 9 to 6 Å, the molecular orientation significantly changes (except for the C tip above the C surface where the monolayer does not exist). The double-humped distribution of the orientation vanishes for the Au surface. Instead, the distribution of the orientation is singly peaked at $\theta=96^{\circ}$ ($\cos\theta=-0.1$) with the Au tip or at $\theta=90^{\circ}$ ($\cos\theta=0$) with the C tip. With the Au tip above the C surface as well (bottom left of Fig. 5), the orientation is more sharply peaked at $\theta=90^{\circ}$ ($\cos\theta=0.0$). In short, with a close proximity of a tip, the molecular dipoles near a surface align parallel to the surface, irrespective of whether the surface is Au or C. This behavior can be understood by noting that such a tip vertically confines and squeezes the water molecules below the tip. Consequently, the water molecules below the tip tend to reduce their volume along the surface normal by aligning their H–O–H planes parallel, instead of perpendicular, to the surface. Similarly, a recent MD simulation reported a biased molecular orientation of water induced by the confinement between flat surfaces. $^{48}$ The molecular reorientation of water induced by a closely approaching tip might not be detected by AFM. Instead, a spectroscopic technique sensitive to the molecular orientation seems necessary. For example, the pump-probe infrared spectroscopy performed by Tan et al. $^{49,50}$ showed that the orientational motion of water in a reverse micelle is substantially slower than in bulk water and is dependent on the size of the micelle.

## Simulation methods

We simulated four combinations of the tip and the surface: the C or Au tip above the C or Au surface. For each combination, a hemispherical tip above a flat surface was immersed in a liquid made of 8342 water (H₂O) molecules. We constructed hemispherical tips with radii of 1.0 nm, and the solid surfaces were made of two layers of Au or C atoms. The tips and surfaces were carved out from the face-centered cubic (FCC) lattice of C or Au with the lattice parameters of 3.567 and 4.078 Å, respectively. We used a dense FCC lattice of C (Au) to model a hydrophobic (hydrophilic) tip or the surface.

We employed the extended simple point charge model (SPC/E) to simulate water molecules. $^{51}$ The long-ranged Coulomb interactions between the point charges were handled using the particle-particle particle-mesh method. $^{52}$ The non-bonded interactions between C and O, between C and Au, and between Au and O atoms were described by the Lennard-Jones (LJ) potentials combined with the Lorentz-Berthelot mixing rule. $^{53}$ All the LJ

![](./images/812828558375256065_6.jpg)

Fig. 5 Effects of confinement on the molecular orientation. Plotted in each panel is the distribution of the polar angle $\theta$ between the molecular dipoles of water and the surface normal, $P(\cos\theta)$. Only the molecules in the first hydration layers on each surface are included in calculating the distribution. Shown at the top are the distributions for the Au surfaces with the Au (a) and C (b) tips. In the bottom left and right, the distribution of orientation is shown for the C surface probed by the Au (c) or C (d) tip, respectively. For each combination of the tip and surface, $P(\cos\theta)$ is plotted by varying $D$ as 50, 12, 9, and $6\ \text{\AA}$, which correspond to the configurations of an isolated surface, a trilayer, a bilayer and a monolayer, respectively. Lines are drawn for visual guide only. In each panel, a snapshot of the system and the molecule(s) with the orientation(s) at the peak(s) of $P(\cos\theta)$s are drawn for reference.

parameters were taken from our previous work. $^{35,54,55}$ For the LJ interaction between atoms i and j, we used the following length and energy parameters, $\sigma_{ij}$ (Å) and $\varepsilon_{ij}$ (kcal mol$^{-1}$), respectively: $\sigma_{\text{AuAu}} = 2.6290$, $\varepsilon_{\text{AuAu}} = 5.290$; $\sigma_{\text{cc}} = 3.214$, $\varepsilon_{\text{cc}} = 0.0708$; $\sigma_{\text{oo}} = 3.1660$, $\varepsilon_{\text{oo}} = 0.1553$; $\sigma_{\text{AuC}} = 2.9215$, $\varepsilon_{\text{AuC}} = 0.6120$; $\sigma_{\text{AuO}} = 2.8975$, $\varepsilon_{\text{AuO}} = 0.9064$; $\sigma_{\text{co}} = 3.1900$, $\varepsilon_{\text{co}} = 0.1049$. Both the LJ and Coulomb interactions were truncated at $12\ \text{\AA}$. The MD trajectories were propagated using the velocity Verlet algorithm$^{53}$ with a time step of 2.0 fs. Both the tip and the surface were fixed in simulations. $^{56}$ We treated water molecules as rigid bodies by using the SHAKE algorithm. $^{57}$ We used the triclinic simulation boxes with $a = b = 49.94\ \text{\AA}$, $c = 100\ \text{\AA}$, and $\alpha = \beta = \gamma = 90^\circ$ and with $a = b = 57.68\ \text{\AA}$, $c = 100\ \text{\AA}$, $\alpha = \beta = 90^\circ$, and $\gamma = 120^\circ$ for the C and Au surfaces, respectively. Periodic boundary conditions were applied in all three directions. Each system was equilibrated by running a 1.5 ns-long MD simulation by using the Nosé-Hoover thermostat$^{58,59}$ to set temperature $T$ to 300 K. We then ran a 4 ns-long MD simulation by using the Nosé-Hoover barostat and thermostat$^{58,59}$ to fix pressure $P$ and $T$ to 1 atm and 300 K, respectively. The final configurations of MD simulations were used as the initial conditions for the following free energy calculations.

We calculated the PMF by running restrained MD simulations$^{60}$ with $P$ and $T$ set to 1 atm and 300 K, respectively. $^{58,59}$ Using the umbrella sampling, $^{61}$ we constructed the PMF vs. $D$ plot. $D$ was restrained to a series of target values ranging from 15.6 to $2.6\ \text{\AA}$ with a decrement of $0.2\ \text{\AA}$ by imposing a harmonic bias potential. Namely, 66 windows were used to achieve sufficient overlaps between the neighboring histograms. In each window, we ran a 4.0 ns MD simulation and discarded the initial 0.2 ns for equilibration. We used the vFEP$^{62,63}$ method with the Jacobian correction to extract the PMF. In calculating the density profiles, the $Z$ coordinates of water molecules were binned into $0.2\ \text{\AA}$-thick slabs and each average was obtained by taking 900 configurations from a 3.8 ns-long MD simulation. All the MD simulations were run by using the LAMMPS$^{64}$ and PLUMED$^{65}$ packages.

## Conclusions

By using all-atom MD simulations, we uncovered the molecular details of the hydration layers probed by a nanoscale tip commonly used in AFM. By considering four distinct combinations

of the tip (Au or C) and the surface (Au or C) with the same and opposite wettabilities, we investigated the free energy and force on the tip by varying the tip-surface distance. Both the free energy and force oscillated owing to the transitions between tri-, bi-, and mono-layers of water. These oscillations existed even for the hydrophobic C surface. With the tip and the surface made of hydrophobic C however, the bilayer of water became unstable with a close proximity of the tip due to the dewetting transition. Consequently, the AFM results showed a relatively long-ranged attractive force without oscillation. The force measured by AFM could not determine the thermodynamic stabilities of various (meta)stable configurations appearing in the free energy profile. The greatest attractive force (pull-off force) did not always match the most stable configuration, let alone the mismatch in the locations of the minima of the force and the PMF. Also, the period of oscillation in the force was consistently larger by 0.2-1.0 Å than the structural periodicity found in the free energy curve. Although the present C and Au surfaces nonspecifically interact with water molecules, the molecular orientation of water was not uniform near the surface. With a close approach of a tip especially, water molecules oriented their H-O-H planes parallel to the surface to reduce their vertical heights, regardless of whether the tip and the surface are hydrophilic Au or hydrophobic C.

The prior studies focused on how the wettability of the surface affects AFM. Here, we have shown that the hydrophobicity of the tip also significantly affects the presence and the magnitude of the oscillation in the force measured in AFM. Our work shows that in contrast to the experiment by Kaggwa et al., $^{19}$ even a hydrophobic tip experiences the oscillatory force due to the hydration layers on a hydrophilic surface. Only when both the tip and surface are hydrophobic do the hydration layers disappear, giving a non-oscillatory force in AFM. The propensity in the molecular orientation of water confined between the nonpolar tip and surface is interesting as well, which calls for a further study by using a spectroscopic probe. The present results provide fundamental molecular insights on the force measured by AFM.

## Conflicts of interest

There are no conflicts to declare.

## Acknowledgements

This study was supported by the National Research Foundation Grants funded by the Korean Government (MSIP, NRF-2014R1A4A1001690 and NRF-2018R1A2A2A05019776).

## References

1 A. Calò, N. Domingo, S. Santos and A. Verdaguer, *J. Phys. Chem. C*, 2015, **119**, 8258-8265.

2 P. Ball, *Chem. Rev.*, 2008, **108**, 74-108.

3 D. Bonn, J. Eggers, J. Indekeu, J. Meunier and E. Rolley, *Rev. Mod. Phys.*, 2009, **81**, 739-805.

4 P. Jungwirth, B. J. Finlayson-Pitts and D. J. Tobias, *Chem. Rev.*, 2006, **106**, 1137-1139.

5 C. Hoose and O. Möhler, *Atmos. Chem. Phys.*, 2012, **12**, 9817-9854.

6 J. D. Atkinson, B. J. Murray, M. T. Woodhouse, T. F. Whale, K. J. Baustian, K. S. Carslaw, S. Dobbie, D. O'sullivan and T. L. Malkin, *Nature*, 2012, **498**, 355-358.

7 Y. Leng and P. T. Cummings, *J. Chem. Phys.*, 2006, **124**, 074711.

8 S. Meng, L. Xu, E. Wang and S. Gao, *Phys. Rev. Lett.*, 2002, **89**, 176104.

9 X. Lin and A. Groß, *Surf. Sci.*, 2012, **606**, 886-891.

10 G. Evmenenko, S. Dugan, J. Kmetko and P. Dutta, *Langmuir*, 2001, **17**, 4021-4024.

11 P. Geissbühler, P. Fenter, E. DiMasi, G. Srajer, L. Sorensen and N. Sturchio, *Surf. Sci.*, 2004, **573**, 191-203.

12 E. Perret, K. Nygård, D. K. Satapathy, T. E. Balmer, O. Bunk, M. Heuberger and J. F. Van Der Veen, *J. Synchrotron Radiat.*, 2010, **17**, 465-472.

13 B. Kim, Q. Kim, S. Kwon, S. An, K. Lee, M. Lee and W. Jhe, *Phys. Rev. Lett.*, 2013, **111**, 246102.

14 Y. Seo, H. Choe and W. Jhe, *Appl. Phys. Lett.*, 2003, **83**, 1860-1862.

15 B. Kim, S. Kwon, H. Mun, S. An and W. Jhe, *Sci. Rep.*, 2014, **4**, 6499.

16 T. Arai, K. Sato, A. Iida and M. Tomitori, *Sci. Rep.*, 2017, **7**, 4054.

17 E. T. Herruzo, H. Asakawa, T. Fukuma and R. Garcia, *Nanoscale*, 2013, **5**, 2678-2685.

18 K. Miyazawa, N. Kobayashi, M. Watkins, A. L. Shluger, K.-i. Amano and T. Fukuma, *Nanoscale*, 2016, **8**, 7334-7342.

19 G. B. Kaggwa, P. C. Nalam, J. I. Kilpatrick, N. D. Spencer and S. P. Jarvis, *Langmuir*, 2012, **28**, 6589-6594.

20 R. M. Pashley and J. N. Israelachvili, *J. Colloid Interface Sci.*, 1984, **101**, 511-523.

21 K. Suzuki, N. Oyabu, K. Kobayashi, K. Matsushige and H. Yamada, *Appl. Phys. Express*, 2011, **4**, 125102.

22 I. Schlesinger and U. Sivan, *Langmuir*, 2017, **33**, 2485-2496.

23 L. Gelb and R. Lynden-Bell, *Phys. Rev. B: Condens. Matter Mater. Phys.*, 1994, **49**, 2058-2066.

24 L. S. Dorobantu, S. Bhattacharjee, J. M. Foght and M. R. Gray, *Langmuir*, 2009, **25**, 6968-6976.

25 R. Kjellander and S. Sarman, *J. Chem. Soc., Faraday Trans.*, 1991, **87**, 1869-1881.

26 K.-i. Amano, E. Tanaka, K. Kobayashi, H. Onishi, N. Nishi and T. Sakka, *Surf. Sci.*, 2015, **641**, 242-246.

27 A. A. Chialvo, L. Vlcek and P. T. Cummings, *J. Phys. Chem. C*, 2013, **117**, 23875-23886.

28 M. Watkins, M. L. Berkowitz and A. L. Shluger, *Phys. Chem. Chem. Phys.*, 2011, **13**, 12584-12594.

29 M. Watkins and A. L. Shluger, *Phys. Rev. Lett.*, 2010, **105**, 196101.

30 D. Argyris, P. D. Ashby and A. Striolo, *ACS Nano*, 2011, **5**, 2215-2223.

31 K. Kobayashi, Y. Liang, K.-i. Amano, S. Murata, T. Matsuoka, S. Takahashi, N. Nishi and T. Sakka, *Langmuir*, 2016, **32**, 3608-3616.

32 P. Schatzberg, *J. Phys. Chem.*, 1967, **71**, 4569-4570.

33 A. A. Chialvo and L. Vlcek, *J. Phys. Chem. C*, 2016, **120**, 7553-7561.

34 J. Jang, J. Sung and G. C. Schatz, *J. Phys. Chem. C*, 2007, **111**, 4648-4654.

35 Z. Zhang, H. Kim, M. Y. Ha and J. Jang, *Phys. Chem. Chem. Phys.*, 2014, **16**, 5613-5621.

36 M. Kinoshita and T. Hayashi, *Phys. Chem. Chem. Phys.*, 2017, **19**, 25891-25904.

37 N. Ishida, Y. Kusaka and H. Ushijima, *Langmuir*, 2012, **28**, 13952-13959.

38 K.-i. Amano, K. Suzuki, T. Fukuma, O. Takahashi and H. Onishi, *J. Chem. Phys.*, 2013, **139**, 224710.

39 K.-i. Amano, Y. Liang, K. Miyazawa, K. Kobayashi, K. Hashimoto, K. Fukami, N. Nishi, T. Sakka, H. Onishi and T. Fukuma, *Phys. Chem. Chem. Phys.*, 2016, **18**, 15534-15544.

40 L. Cheng, P. Fenter, K. Nagy, M. Schlegel and N. Sturchio, *Phys. Rev. Lett.*, 2001, **87**, 156103.

41 C. Sendner, D. Horinek, L. Bocquet and R. R. Netz, *Langmuir*, 2009, **25**, 10768-10781.

42 X. Hu, W. Nanney, K. Umeda, T. Ye and A. Martini, *Langmuir*, 2018, **34**, 9627-9633.

43 D. Argyris, A. Phan, A. Striolo and P. D. Ashby, *J. Phys. Chem. C*, 2013, **117**, 10433-10444.

44 J. Le, A. Cuesta and J. Cheng, *J. Electroanal. Chem.*, 2018, **819**, 87-94.

45 K. Raghavan, K. Foster, K. Motakabbir and M. Berkowitz, *J. Chem. Phys.*, 1991, **94**, 2110-2117.

46 K. J. Schweighofer, X. Xia and M. L. Berkowitz, *Langmuir*, 1996, **12**, 3747-3752.

47 J. M. Devi, *Prog. Nat. Sci.: Mater. Int.*, 2014, **24**, 405-411.

48 A. Alex, A. K. Nagesh and P. Ghosh, *RSC Adv.*, 2017, **7**, 3573-3584.

49 H.-S. Tan, I. R. Piletic, R. E. Riter, N. E. Levinger and M. Fayer, *Phys. Rev. Lett.*, 2005, **94**, 057405.

50 H.-S. Tan, I. R. Piletic and M. Fayer, *J. Chem. Phys.*, 2005, **122**, 174501.

51 H. Berendsen, J. Grigera and T. Straatsma, *J. Phys. Chem.*, 1987, **91**, 6269-6271.

52 P. S. Crozier, R. L. Rowley and D. Henderson, *J. Chem. Phys.*, 2001, **114**, 7513-7517.

53 P. M. T. Allen and D. J. Tildesley, *Computer Simulation of Liquids*, Clarendon Press, Oxford, 1987.

54 Z. Zhang, M. Y. Ha and J. Jang, *Nanoscale*, 2017, **9**, 16200-16204.

55 H. Kim, B. Smit and J. Jang, *J. Phys. Chem. C*, 2012, **116**, 21923-21931.

56 H. Kamberaj, R. Low and M. Neal, *J. Chem. Phys.*, 2005, **122**, 224114.

57 J.-P. Ryckaert, G. Ciccotti and H. J. Berendsen, *J. Comput. Phys.*, 1977, **23**, 327-341.

58 W. G. Hoover, *Phys. Rev. A: At., Mol., Opt. Phys.*, 1985, **31**, 1695-1697.

59 S. Nosé, *J. Chem. Phys.*, 1984, **81**, 511-519.

60 B. Reischl, M. Watkins and A. S. Foster, *J. Chem. Theory Comput.*, 2012, **9**, 600-608.

61 G. M. Torrie and J. P. Valleau, *J. Comput. Phys.*, 1977, **23**, 187-199.

62 T.-S. Lee, B. K. Radak, A. Pabis and D. M. York, *J. Chem. Theory Comput.*, 2013, **9**, 153-164.

63 T.-S. Lee, B. K. Radak, M. Huang, K.-Y. Wong and D. M. York, *J. Chem. Theory Comput.*, 2014, **10**, 24-34.

64 S. Plimpton, *J. Comput. Phys.*, 1995, **117**, 1-19.

65 G. A. Tribello, M. Bonomi, D. Branduardi, C. Camilloni and G. Bussi, *Comput. Phys. Commun.*, 2014, **185**, 604-613.