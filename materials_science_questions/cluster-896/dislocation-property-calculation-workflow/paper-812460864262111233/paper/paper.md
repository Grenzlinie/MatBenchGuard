An atomistic study of the strength of an extended-dislocation barrier

This content has been downloaded from IOPscience. Please scroll down to see the full text.

1998 Modelling Simul. Mater. Sci. Eng. 6 9

(http://iopscience.iop.org/0965-0393/6/1/002)

View the table of contents for this issue, or go to the journal homepage for more

Download details:

IP Address: 139.184.14.159
This content was downloaded on 22/08/2015 at 02:48

Please note that terms and conditions apply.

# An atomistic study of the strength of an extended-dislocation barrier

M I Baskes†, R G Hoagland‡ and T Tsuji§

† Materials Reliability Department, Sandia National Laboratories, Livermore, CA 94551-0969, USA
‡ School of Mechanical and Materials Engineering, Washington State University, Pullman, WA 99164-2920, USA
§ Department of Mechanical Engineering, Shizuoka University, Hamamatsu 432, Japan

Received 20 July 1997, accepted for publication 8 October 1997

**Abstract.** The stress dependence of a lock consisting of a $\frac{1}{3}a[100]$ stair rod symmetrically located between two Shockley partials in face-centred cubic nickel was examined by atomistic simulation. The applied stress forced the partials into the stair rod. As the partials move into the lock with increasing strain, the separation distances are reasonably consistent with a linear elastic calculation of equilibrium separation except at the closest approach where the elastic calculation overestimates the separation. The overestimation is attributable to core overlap. The lock underwent several unstable transitions before becoming an inverted arrangement of its initial configuration. The sequence of transitions involves an asymmetric configuration at 2.3% strain containing an extrinsic fault, a transition at 4.8% strain that changes the stair rod to $\frac{1}{6}a[011]$, and a transition that inverts the lock at 6% strain with the stair rod becoming $\frac{1}{6}a[\overline{1}00]$. The evolution of the lock is not reversible.

## 1. Introduction

Reactions between extended dislocations in face-centred cubic (fcc) metals can form various barriers that are resistant to slip. Such barriers take the form of sessile dislocations. The Lomer–Cottrell lock is an example. A summary of the various forms has been given by Hirth [1]. The effectiveness of these barriers in blocking slip depends on their strength, i.e. the stress required to cause the barriers to decompose. Another important property is the way in which they decompose. For example, depending on the state of stress on the barrier, and the presence of other types of defects, the barrier may decompose into dislocations or, as has been suggested long ago by Cottrell [2], it may act as the nucleus of a crack. The decomposition of the barrier involves a transition in the arrangement of atoms within the core of the barrier, a process that does not lend itself to analysis by elasticity methods. Instead, alternative means, such as atomistic modelling, are better suited to examine the response of the core of the barrier to large stress, the origins of which can be from an applied long-range stress as well as from other dislocations near the barrier. Along similar lines, *Kurtz et al* [3] have reported the behaviour of an extended mixed dislocation in an atomistic model of aluminum. Large biaxial tensile stresses were applied that exerted no glide force on either partial. They found that one of the partials decomposed into a stair rod plus another partial at an elastic strain of 6%, resulting in a configuration rather similar to a Lomer–Cottrell barrier but with a large resolved shear stress on the new partial. As a

consequence, once formed, the new partial glides rapidly away. This reaction is not easily anticipated and, indeed, alternative paths seem possible.

In this paper we describe the results of a study of the behaviour of a lock that initially consists of a $\frac{1}{3}a[100]$ stair rod and two symmetrically-located Shockley partials on intersecting $\{111\}$ slip planes. The stair rod is the product of a reaction between two partials each associated with two extended dislocations on the intersecting slip planes as shown in figure 1. In this particular lock, application of a uniaxial stress in the $x$-direction forces the two partials into the stair rod providing the opportunity for producing a crack on a (100) plane. We find, however, that the barrier does not crack but, instead, passes through several configurations as the stress increases.

![](./images/812460864262111233_1.jpg)

Figure 1. A schematic diagram of the extended barrier examined in this study. The barrier consists of a $\frac{1}{3}a[100]$ stair rod at the intersection of two slip planes symmetrically located between two partials, B$\delta$ and D$\beta$. The stair rod is the result of a reaction between two Shockley partials $\delta$C and $\beta$A as shown in the top of the figure. The inset shows the corresponding orientation of the Thompson tetrahedron.

## 2. Numerical implementation

The coordinates for the model and orientation of the crystal are shown in figure 1. We adopt the convention defined by Hirth and Lothe [4] that a dislocation's positive sense vector is into the page, and, that the ordering of the Shockley partials on a slip plane viewed from outside the Thompson tetrahedron is Greek-Roman on the left and Roman-Greek on the right. The labels reverse to Roman-Greek and Greek-Roman when the slip plane is viewed from inside the tetrahedron. In our model the dislocation sense vector is parallel to the $[01\overline{1}]$ crystal direction. In figure 1 the Shockley partial on the left, on the (d) $=(111)$ slip plane, is $\text{B}\delta(\text{d})=\frac{1}{6}a[2\overline{1}\overline{1}]$ and the right partial is $\text{D}\beta(\text{b})=\frac{1}{6}a[211]$ on the (b) $=(1\overline{1}\overline{1})$ slip plane. The barrier is a $\beta\delta/\text{AC}=\frac{1}{3}a[100]$ stair rod symmetrically located on the line of intersection of the two slip planes, and separated from the two partials by intrinsic stacking faults. This configuration is the result of a reaction between two extended dislocations:

$\mathrm{BC}(\mathrm{d})=\frac{1}{2} a[10 \overline{1}]$ and $\mathrm{DA}(\mathrm{b})=\frac{1}{2} a[101]$. In the model all three dislocations, initially, are pure edge.

Relative to model coordinates, the elastic stiffness matrix is

$$
\left(\begin{array}{cccccc}
c_{11}^{\prime} & c_{12}^{\prime} & c_{12}^{\prime} & 0 & 0 & 0 \\
c_{12}^{\prime} & c_{22}^{\prime} & c_{23}^{\prime} & 0 & 0 & 0 \\
c_{12}^{\prime} & c_{23}^{\prime} & c_{22}^{\prime} & 0 & 0 & 0 \\
0 & 0 & 0 & c_{44}^{\prime} & 0 & 0 \\
0 & 0 & 0 & 0 & c_{55}^{\prime} & 0 \\
0 & 0 & 0 & 0 & 0 & c_{55}^{\prime}
\end{array}\right)
\tag{1}
$$

where

$$
\begin{aligned}
c_{11}^{\prime} &=c_{11} \\
c_{22}^{\prime} &=\left(c_{11}+c_{12}+c_{44}\right) / 2 \\
c_{12}^{\prime} &=c_{12} \\
c_{23}^{\prime} &=\left(c_{11}+c_{12}-c_{44}\right) / 2 \\
c_{44}^{\prime} &=\left(c_{11}-c_{12}+c_{44}\right) / 2 \\
c_{55}^{\prime} &=c_{44} .
\end{aligned}
$$

The model is cylindrical in shape with axis parallel to the dislocation lines and consists of two regions. The inner region, region 1, contains the movable atoms, and we employed diameters of 10–12 nm. Region 1 is surrounded by an outer ring containing atoms that remain fixed during relaxation toward an equilibrium configuration. We address the issue concerning the effects of the boundary conditions on the results in a following section. Periodic boundary conditions were employed along the cylinder axis.

Prior to relaxation, the dislocations were placed as follows: the stair rod at the origin $(0,0), \mathrm{D} \beta$ at $(2.78,1.84) \mathrm{nm}$, and $\mathrm{B} \delta$ at $(-2.78,1.96) \mathrm{nm}$. The relative positions for the Shockley partials were estimated from the equilibrium analysis for this lock by Jossang *et al* [5] described later. This barrier is identified as Lock (3) in the Jossang *et al* analysis and in Hirth and Lothe [4]. The slight asymmetry in the positions of the partials relative to the stair rod was prescribed simply to avoid metastable configurations. The displacement fields for these three dislocations were imposed on all the atoms in both regions in the model. This configuration was then relaxed either by molecular dynamics employing an energy quench or molecular statics using a conjugate gradient technique.

A uniaxial stress, $\sigma_{11}$ is applied parallel to the $x$-axis (the [100] crystal direction) by imposing a strain $\varepsilon_{11}$ while accommodating the Poisson contraction through the strains $\varepsilon_{22}$ and $\varepsilon_{33}$ given by (for this crystallographic orientation)

$$
\varepsilon_{22}=\varepsilon_{33}=-\frac{c_{12}^{\prime}}{c_{22}^{\prime}+c_{23}^{\prime}} \varepsilon_{11}.
\tag{2}
$$

The tensile strain was applied in small increments of 0.1 to $0.2 \%$, and the models relaxed after the application of each increment.

The EAM potential used to define the Ni–Ni interactions has been described by Angelo *et al* [6]. Some relevant properties that derive from this potential are given in table 1. We note that the surface energies are reasonably consistent with experiment but this property is difficult to measure and experimental data may not be reliable.

<table><caption>Table 1. Some physical properties associated with the Ni potential used in this study.</caption>
<tbody>
<tr>
<th>Property</th>
<td>Calculated</td>
<td>Experimental</td>
</tr>
<tr>
<th colspan="3">Elastic constants ($10^{11}$ Pa)</th>
</tr>
<tr>
<th>Stiffness coefficients $c_{11}$</th>
<td>2.464</td>
<td>2.465 [7]</td>
</tr>
<tr>
<th>$c_{12}$</th>
<td>1.473</td>
<td>1.473 [7]</td>
</tr>
<tr>
<th>$c_{44}$</th>
<td>1.248</td>
<td>1.247 [7]</td>
</tr>
<tr>
<th>Voight averages: Young’s modulus $E$</th>
<td>2.508</td>
<td>2.441</td>
</tr>
<tr>
<th>shear modulus $\mu$</th>
<td>0.992</td>
<td>0.947</td>
</tr>
<tr>
<th>Poisson’s ratio $\nu$</th>
<td>0.271</td>
<td>0.276</td>
</tr>
<tr>
<th>bulk modulus $B$</th>
<td>1.825</td>
<td>1.928</td>
</tr>
<tr>
<th>Crystal–vapour surface energies (J m$^{-2}$)</th>
<td></td>
<td>2.24 [8]</td>
</tr>
<tr>
<th></th>
<td></td>
<td>(polycryst. average)</td>
</tr>
<tr>
<th>{100}</th>
<td>2.060</td>
<td></td>
</tr>
<tr>
<th>{110}</th>
<td>2.350</td>
<td></td>
</tr>
<tr>
<th>{111}</th>
<td>1.928</td>
<td></td>
</tr>
<tr>
<th>Intrinsic stacking fault energy (mJ m$^{-2}$)</th>
<td>89</td>
<td>125 [4]</td>
</tr>
</tbody>
</table>

![](./images/812460864262111233_2.jpg)

Figure 2. The atomic configuration near the central portion of the model containing the barrier in the relaxed configuration. The locations of the stair rod and Shockley partial dislocations are indicated.

## 3. Results

The zero stress configuration of the central portion of the model that results after relaxation is shown in figure 2. Both partials remain at about 3.4 nm from the stair rod, which is consistent with the Peach–Koehler calculation of the equilibrium separation based on anisotropic elasticity by Jossang *et al* [5] given by

$$
r_{\mathrm{eq}}=\frac{G}{\gamma}. \tag{3}
$$

$G$ contains the elastic constants and the burgers vectors of the interacting dislocations. For our nickel potential $G$ has a value of $3.1 \times 10^{-10}$ N and $\gamma$ is the stacking fault energy.

The distance separating each partial from the stair rod is reduced by the application of stress, $\sigma_{11}$. The resolved glide force acting on each Shockley partial due to this uniaxial

![](./images/812460864262111233_3.jpg)

Figure 3. The distribution of the in-plane disregistry, divided by the magnitude of the Burgers vector, on the (111) slip plane containing the partial Bδ and the stair rod as a function of strain. The lengths of Burgers vector of the Shockley partials are 0.1437 nm. Thus, the location of Bδ may be defined where the disregistry is $b/2$. For example, at 0.5% strain, this places Bδ at about 2.7 nm from the origin. The abrupt disregistry change at the origin identifies the location of the stair rod.

![](./images/812460864262111233_4.jpg)

Figure 4. The strain dependence of the radial separation between the partials and the stair rod in figure 1. An elasticity prediction of the separation distance is shown for comparison.

stress, $F_{\rm gl}$, simply adds to the glide force components due to dislocation interactions and the stacking faults so that equation (3) becomes

$$
r_{\rm eq} = \frac{G}{\gamma - F_{\rm gl}}. \tag{4}
$$

![](./images/812460864262111233_5.jpg)

Figure 5. Strain dependence of the intrinsic and extrinsic stacking fault energies.

![](./images/812460864262111233_6.jpg)

Figure 6. New configurations after transitions that occur at strains of (a) 2.3%, (b) 4.8% and (c) 6%.

The equilibrium separation between the partials and the stair rod in the atomistic models was determined from the disregistry across the slip plane given by $\boldsymbol{u}^{+}-\boldsymbol{u}^{-}$, where the superscripts denote the displacement vectors of a pair of neighbouring atoms, one lying in a

plane above the slip plane, the other below. Figure 3 shows the disregistry along the (111) slip plane for various strain levels. At low strains, the stair rod and Shockley partial on this plane are distinct. The location on the slip plane provides a measure of its position. The equilibrium separation determined on this basis in the atomic models is compared with the prediction of equation (4) and the results plotted as a function of strain in figure 4. We see that the equilibrium separation decreases somewhat faster than the elasticity prediction with increasing strain. There are at least two explanations for this difference: (1) the stacking fault energy is stress dependent and (2) the cores of the dislocations overlap sufficiently to make the linear elastic prediction based on point dislocations inaccurate at small separations. There is evidence in favour of the latter explanation in the disregistry information in figure 3. At low applied strains, a distinct inflection in the disregistry is observed which clearly identifies the location of B$\delta$. However, at 2.0% strain the inflection is no longer distinct and the core of B$\delta$ appears to overlap that of the stair rod. We also examined the stress dependence of the stacking fault energy for both the intrinsic and extrinsic stacking faults, and these results are shown in figure 5. These results were obtained from models that contained a single intrinsic or extrinsic stacking fault and subject to a uniaxial strain perpendicular to the stacking fault plane. We find that the stacking fault energies are relatively insensitive to strain and, therefore, stress, except for large compression.

At an elastic strain of 2.3% the system undergoes a transition into another configuration whereby the Shockley partial on the left (B$\delta$(d) $= \frac{1}{6}a[2\overline{1}\overline{1}]$) passes through the stair rod, moving to a location approximately 1.05 nm on the other side of the stair rod, trailing an extrinsic fault as it leaves the stair rod. The new configuration is shown schematically in figure 6(a). B$\delta$ can now be regarded as composed of two Shockley partials, $\delta$C(d) $= \frac{1}{6}a[11\overline{2}]$ and $\delta$A(d) $= \frac{1}{6}[\overline{1}2\overline{1}]$ on adjacent (111) slip planes. Similarly, the partial, $\delta$C, that remains part of the stair rod can be regarded as composed of A$\delta$(d) $= \frac{1}{6}a[\overline{1}2\overline{1}]$ and B$\delta$(d) $= \frac{1}{6}a[2\overline{1}\overline{1}]$ on adjacent slip planes. In our models these two pairs of partials, defining the ends of the extrinsic fault, arranged themselves such that A$\delta$(d) was on the same slip plane as $\delta$A(d) and $\delta$B(d) on the adjacent plane shared by C$\delta$(d) as shown in figure 6(a). It seems plausible that any of the four legitimate alternative arrangements on the two slip planes are equally likely.

The lock configuration in figure 6(a) remains stable with increasing strain until, at a strain of about 4.8%, another transition occurs to the configuration shown in figure 6(b). During this second transition, the partial B$\delta$ escapes from the stair rod and, as it glides away, partially removes one of the two faults comprising the extrinsic fault leaving an intrinsic fault in its wake. The end of the extrinsic fault also moves further away from the stair rod. The stair rod has evolved to become A$\delta$ and $\beta$A, which is $\beta\delta = \frac{1}{6}a[011]$. We note that the two partials, $\delta$A and $\delta$C, that form the partial B$\delta$ at the end of the extrinsic fault were switched, relative to the slip planes on which they reside, in two calculations performed with different relaxation codes. Otherwise these two codes produced the same results. Except for slight differences in distances between dislocations, these two alternative configurations are structurally and energetically very similar and, therefore, equally likely. After the second transition, the partial B$\delta$, located at the end of the extrinsic fault, has moved about 4 nm from the stair rod. Also D$\beta$ has moved to within about 0.8 nm of the lock and continues to merge with the lock as strain increases.

A third transition occurs at 6% strain giving the configuration in figure 6(c). During this transition, D$\beta$ passes through the lock forming a symmetric arrangement of intrinsic and extrinsic faults shown in figure 6(c). The lock has now become A$\delta + $C$\beta = $AC/$\beta\delta = \frac{1}{3}a[\overline{1}00]$, the inverse of the stair rod at the beginning of straining. The Shockley partials

B$\delta$ and D$\beta$ at the ends of the extrinsic faults are, at this stage, about 5.5 nm from the lock. At this extension, model size becomes limiting and for this reason we did not pursue the calculation beyond this point.

## 4. Discussion

The behaviour of the barrier studied in this paper displays an interesting sequence of events in its evolution with increasing strain.

It is clear that this particular lock is a strong, effective barrier to slip. The first transition, at a tensile strain of 2.3% corresponds to a very large tensile stress of about 5.6 GPa, which is much larger than the yield strength of the strongest nickel alloys. However, such stresses might be encountered in very small volumes in the vicinity of a pile up or other types of stress concentrators. In addition, the barrier might be more easily defeated if it is already broken at some other location along its length so that the application of stress acts to unzip the lock, as described by Hirth and Lothe [6]. An examination of the unzipping process would require a much larger three-dimensional model than we have used in this study.

The first transition is asymmetric. We have analysed the net force on D$\beta$, and find that this partial is repelled more strongly away from the lock after the transition than before, a result which helps explain the asymmetry. Thus, the first transition could equally involve the adsorption and re-emission of either partial, but once one of the partials has managed to enter the lock, the other is prevented from doing so. After the first transition, the stair rod remains a $\frac{1}{3}a[100]$ stair rod.

The second transition involves a change in the stair rod, wherein it emits B$\delta$ changing into a less energetic $\frac{1}{6}a[011]$ stair rod. The third transition is perhaps the most remarkable. After the third transition is complete the lock has essentially inverted including changing the sign of the stair rod to $\frac{1}{3}a[100]$. It seems quite possible that this configuration could remain stable to modest additional increases in strain with the partials B$\delta$ and D$\beta$ moving away from the stair rod thereby increasing the length of the intrinsic fault in the process.

We find that the barrier does not serve as a nucleation site for crack formation as certainly seemed possible at the outset. Rather, the evolution involves the generation of extrinsic faults, which have a slightly higher energy than intrinsic faults, instead of the creation of a much more energetic free surface.

With increasing strain all of the transitions are abrupt rather than gradual, each transition corresponding to an instability. In addition, we find that the process is not reversible in the sense that the system does not retrace its steps on gradually removing the stress. For example, removing the strain, in small increments, leaves the unstressed lock in the symmetric configuration similar to that in figure 6(c), but with a smaller extension between the Shockley partials and the stair rod. This observation has implications for accumulation of damage in situations involving cyclic loading.

As a final matter, we consider the possible influence which the boundary conditions that we used may have had on the results. Even though the boundaries surrounding region 1 contain the equilibrium anisotropic linear elastic displacement field associated with the three dislocations, the relaxation of the cores creates an additional linear elastic field, the core field, that does not escape into the boundaries. The core field has no net dislocation content but it may be expanded into terms that represent volume dilatation, dipole, quadripole, and higher-order multipole source contributions [9]. The dominant term in this expansion, i.e. the displacement term with the lowest-order $r$-dependence, and, therefore, the longest range,

is the dilatation with a radial component of displacement given by

$$
u_{r}=\frac{\delta A}{2 \pi r} \tag{5}
$$

where $\delta A$ is the volume expansion, the dilatation, per unit length of dislocation. The boundary conditions require that this displacement be zero at the interface between movable and fixed regions, and, therefore, the tractions needed to accomplish this in an infinite solid produces a constant radial component of stress given by

$$
\sigma_{r r}=-\frac{E \delta A}{2 \pi R^{2}(1+v)} \tag{6}
$$

inside the movable region of radius $R$. We have used an isotropic approximation for purposes of obtaining an estimate of the magnitude of this stress. The dilatation can be written as $\delta A=\alpha b^{2}$. In situations where $\alpha$ has been measured or calculated in atomistic simulations, it is generally found to be of the order of unity or smaller (cf [10,11]). Assuming $\alpha=1$, for models with region 1 radii of 5.0 nm and 6.0 nm, the internal radial stress induced by fixed boundaries in our models is about $-64$ MPa and $-44$ MPa, respectively. These stresses are of the order of 1% of the applied stresses and, therefore, are not regarded as a serious influence on the outcome of the transitions that we observed. We also note, in passing, that we observed no difference in the behaviour of the 5.0 nm radius and 6.0 nm radius models.

## 5. Conclusions

(1) At low strains the separation between the Shockley partials and the stair rod in the original configuration is in agreement with a prediction based on linear elasticity, except for the smallest separation distances where the elasticity prediction overestimates the separation. The overestimate is attributable to a contribution to the interaction force from the dislocation cores, i.e. core overlap of the Shockley partials with the stair rod.

(2) An atomistic simulation of an extended barrier consisting of two symmetrically located Shockley partials and an $\frac{1}{3} a[100]$ stair rod in nickel responds to an increasing tensile stress by inverting in three distinct stages or transitions. The first transition, at 2.3% strain, produces an asymmetric configuration and extrinsic faults. The stacking faults persist through the second and final transitions and after the stress is removed, i.e. the evolution of the barrier with increasing stress is not reversible. The final transition leaves the configuration symmetric and the sign of the stair rod reversed. The evolution of the lock with increasing strain is not reversible.

## Acknowledgments

The authors would like to acknowledge the helpful discussions with J P Hirth and the support of this work by US Department of Energy, Office of Basic Energy Sciences, Division of Materials Research through grant DE-FG06-87ER45287 and under contract DE-AC04-94AL85000

## References

[1] Hirth J P 1983 *Physical Metallurgy* ed R W Cahn and P Haasen (Amsterdam: Elsevier) p 1239

[2] Cottrell A H 1958 *Trans. AIME* **212** 192

[3] Kurtz R J, Hoagland R G and Hirth J P 1995 *Micromechanics of Advanced Materials* ed S N G Chu *et al* (Warrendale, PA: The Minerals, Metals and Materials Society) p 37

[4] Hirth J P and Lothe J 1982 *Theory of Dislocations* 2nd edn (New York: Wiley)

[5] Jossang T, Hartley C S and Hirth J P 1965 *J. Appl. Phys.* **36** 2400

[6] Angelo J E, Moody N R and Baskes M I 1995 *Modelling Simul. Mater. Sci. Eng.* **3** 289

[7] Simons G and Wang H 1971 *Single Crystal Elastic Constants and Calculated Aggregate Properties* (Cambridge, MA: Massachusetts Institute of Technology)

[8] Tyson W R and Miller W A 1977 *Surf. Sci.* **62** 267

[9] Sinclair J E, Hirth J P, Gehlen P C and Hoagland R G 1978 *J. Appl. Phys.* **49** 3890

[10] Gehlen P C, Hirth J P, Hoagland R G and Kanninen M F 1972 *J. Appl. Phys.* **43** 3921

[11] Hoagland R G, Hirth J P and Gehlen P C 1976 *Phil. Mag.* **34** 413