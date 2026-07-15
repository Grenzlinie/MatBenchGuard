![](./images/811981200297033729_1.jpg)

Philosophical Magazine A

ISSN: 0141-8610 (Print) 1460-6992 (Online) Journal homepage: http://www.tandfonline.com/loi/tpha20

# Atomistic computation of the image force on
a dislocation in a bicrystal II. Case of a large
difference between the elastic moduli of the two
half-crystals

P. Beauchamp & J. Lépinoux

To cite this article: P. Beauchamp & J. Lépinoux (1998) Atomistic computation of the
image force on a dislocation in a bicrystal II. Case of a large difference between the
elastic moduli of the two half-crystals, Philosophical Magazine A, 77:3, 541-560, DOI:
10.1080/01418619808224068

To link to this article: http://dx.doi.org/10.1080/01418619808224068

![](./images/811981200297033729_2.jpg)
Published online: 12 Aug 2009.

![](./images/811981200297033729_3.jpg)
Submit your article to this journal ![](./images/811981200297033729_4.jpg)

![](./images/811981200297033729_5.jpg)
Article views: 24

![](./images/811981200297033729_6.jpg)
View related articles ![](./images/811981200297033729_7.jpg)

![](./images/811981200297033729_8.jpg)
Citing articles: 2 View citing articles ![](./images/811981200297033729_9.jpg)

Full Terms & Conditions of access and use can be found at
http://www.tandfonline.com/action/journalInformation?journalCode=tpha20

Download by: [University of Nebraska, Lincoln]
Date: 30 May 2016, At: 16:36

**PHILOSOPHICAL MAGAZINE A, 1998, VOL. 77, NO. 3, 541-560**

# Atomistic computation of the image force on a dislocation in a bicrystal
## II. Case of a large difference between the elastic moduli of the two half-crystals

By P. BEAUCHAMP and J. LÉPINOUX

Laboratoire de Métallurgie Physique (UMR 6630 CNRS), Université de Poitiers, BP 179, 86960 Futuroscope Cedex, France

[Received 13 May 1997 and accepted 22 June 1997]

## ABSTRACT
The behaviour of a dislocation in the vicinity of an interface between two half-crystals having notably different elastic moduli has previously been investigated by a computer simulation by Beauchamp and Lépinoux, who considered two half-crystals with similar elastic coefficients. The two half-crystals have a bcc structure with the same orientation and lattice parameter and are welded along the (100) plane, parallel to the $a_{0}[001]$ screw dislocation. Two interatomic potentials representing $\alpha$-iron have been used.

Detailed exploration of the Peierls valleys within $4 a_{0}$ from the interface has been performed by applying an external stress which balances both the local lattice friction and the long-range image force. It is found that the mean stresses of each valley follow approximately the stress curve determined by Pacheco and Mura on the basis of the continuous Peierls dislocation core, perturbed by the interface. The simulation presents, however, a stress peak which is lower and more extended.

Changes in the dislocation core have been observed as the dislocation approaches the interface; in the 'soft' medium the core tends to become slightly narrower, whereas it clearly widens in the 'hard' medium. This is because the effect of the applied stress is uniform throughout each half-crystal whereas the image force is stronger on the parts of the dislocation core close to the interface than on those farther away.

Systematic variations in the Peierls valleys amplitudes have been found; when the interface is approached from the 'soft' medium side, the amplitude increases whereas it decreases when approaching from the 'hard' side. The latter decrease is such that Peierls valleys completely disappear near the interface and an unstable zone forms on the 'hard' side. It has been possible to keep dislocations there, but only under a dissociated form compound of two partials having $b/2$ screw components. The stacking fault created, which is not normally stable in the bcc structure, is of the 'unstable fault' type to which Rice attributes a key role in the dislocation nucleation at a crack tip.

## § 1. INTRODUCTION
The plastic properties of materials composed of several constituents are strongly dependent on modifications to dislocation displacements due to the presence of interfaces. Many different physical processes are involved in the dislocation-interface interaction and a general understanding requires the precise study of each effect separately. Computer simulation may be a useful tool in this respect because it allows the desired reduction to simple situations. This technique is used to investi-

0141-8610/98 $12.00 © 1998 Taylor & Francis Ltd.

gate the image force on a dislocation, which arises from the difference between the elastic moduli of the two components of a bimaterial. After having considered the case where the elastic coefficients of the two half-crystals are not very different (Beauchamp and Lépinoux 1996, hereafter referred to as part I), we report here on bimaterials in which one component has elastic coefficients several times those of the other.

In a bicrystal compound of two welded halves having different elastic moduli, the image force on a dislocation results from the variations in the total strain energy stored in the solid, as the dislocation position relative to the interface is changed; the energy is larger when the dislocation is in the medium of larger elastic constants so that the force is everywhere directed from the 'hard' medium to the 'soft' medium. On a large scale, the image force is accurately described by linear elasticity (Head 1953a, b) but this approach leads to a $1/r$ divergence for the force on the dislocation. To overcome this difficulty, an arbitrary cut-off radius, $r_0$ is generally introduced but its actual value is highly uncertain. Consequently, important quantities such as the critical stress required to make the dislocation cross the interface, proportional to $1/r_0$, are undetermined by a factor of about ten. At the atomic level, where matter is no longer regarded as a continuum, the divergence disappears. It has been shown (part I) that atomistic simulation is able to give useful information in this region of few atomic distances from the interface where the continuum approach fails.

In part I of this work, it appeared convenient to distinguish between bicrystals according to whether the two components have similar or very different elastic moduli. In the first case, the lattice friction is everywhere larger than the image force so that all Peierls valleys remain stable positions for the dislocation even at the interface. Advantage has been taken of this situation to compute the total crystal strain energy for all these stable dislocation positions, from which the image force has been derived. In the second case, the image force erases the Peierls valleys in the neighbourhood of the interface and it is possible to study the dislocation in this region only by applying an external stress balancing the image force.

The investigation of the case where the elastic coefficients are not very different from one half-crystal to the other has resulted in some important information; the region where the computed image force differs notably from elasticity is a few interatomic distances wide and depends on the dislocation core extension. The stress required to move the dislocation from the 'soft' into the 'hard' medium, which becomes a maximum at the interface, has been found to be smaller than $\Delta\mu/10$ and the results of Pacheco and Mura (1969), based on the Peierls-Nabarro descrip- tion of the dislocation core agree, at least qualitatively, with the simulation. It is interesting to see how these conclusions are modified in the case of bicrystals formed of two halves having very different elastic moduli, which is the object of the present work. Particular attention is also paid to any changes in the dislocation core struc- ture, possible in such asymmetrical bimaterials.

## §2. THE COMPUTER MODEL

### 2.1. Construction of the bicrystal
The crystal structure, dislocation and interface are the same as in part I. We recall the choices made and the reasons for those.

In order to eliminate all effects except image forces, the two half-crystals have the same crystallographic structure with the same lattice parameter and same orientation

but with different elastic coefficients. This is realized through the convenient choice of interatomic potentials detailed below. A ⟨001⟩ screw dislocation in a cubic crystal has been considered because it is undissociated and the elastic field in the bimedium, needed to fix boundary conditions, is identical with the isotropic case (Hirth and Lothe 1982) and can be obtained using the image dislocation construction. A bcc crystal has been retained because, although ⟨001⟩ dislocations are not normally present in this structure, they frequently appear in the bcc-based B2 ordered com- pounds, cf. for instance Ball and Smallman (1966), Schulson and Teghtsoonian (1969) and Umakoshi and Yamaguchi (1981). The interface is along the (100) plane, parallel to the dislocation line.

### 2.2. Computation procedure
The interatomic force laws employed in this study are based on two potentials constructed to represent $\alpha$-iron: the pair potential of Johnson (1964) which has been used quite extensively for many different properties and defects in this metal; the $N$-body potential for $\alpha$-iron constructed by Cserti, Vitek and Tichy (1994) according to the procedure proposed by Finnis and Sinclair (1984) and developed by Ackland et al. (1987).

The chosen potential is used in its original form in medium (1). For medium (2), interactions are multiplied by the coefficient $\alpha$ which is the desired ratio of elastic moduli of medium (2) with respect to medium (1); $\alpha = \mu_2/\mu_1$.

Thus, for the bicrystal based on Johnson potential, the interactions are as follows: $V(r_{ij})$ for both atoms $i, j$ in medium (1); $\alpha V(r_{ij})$ for both atoms $i, j$ in medium (2); $[(1+\alpha)/2]V(r_{ij})$ for one atom in medium (1) and the other in medium (2). For the $N$-body potential, the energy of an atom $i$ can be written

$$
U_{i}=\sum_{k \neq i} V\left(r_{i k}\right)-\left(\sum_{k \neq i} \phi\left(r_{i k}\right)\right)^{1 / 2} \tag{1}
$$

(summations are over neighbours $k$ of atom $i$).

The same operation as for Johnson potential is applied to the pair part whereas, for the non-pair part, we use the following: $\phi(r_{ik})$ for both atoms in medium (1); $\alpha^2\phi(r_{jk})$ for both atoms in medium (2); $[(1+\alpha^2)/2]\phi(r_{jk})$ for one atom in medium (1) and the other in medium (2). Note that the choice made here for interactions between unlike atoms implies that the energy of the unrelaxed interface is exactly zero with the pure pair potential and very small with the $N$-body potential.

The two half-crystals having the bcc structure with the same lattice parameter $a_0=0.286$ nm are joined along the (100) plane, normal to the $x$ axis, and the screw dislocation, lying along [001], the $z$ axis, is parallel to the interface and situated at a distance $x$ from it. Medium (1) is placed on the left-hand side of the interface and is always taken as the medium of lower elastic moduli $\alpha > 1$.

The crystallite is compound of atomic rows parallel to [001] forming in the (001) plane a square lattice of edge length $h=a_0/2^{1/2}$. The origin atoms in each row have $Z$ coordinates alternately equal to zero or $b/2$ ($b$ is the Burgers vector of the screw dislocation equal to $a_0[001]$). The central region where displacements of atomic rows are allowed, is a square of size $20a_0 \times 20a_0$ along the $x$ and $y$ axes, containing 800 rows. The interface separates the crystallite in its middle, along the $y$ axis. Before introducing the dislocation, the crystal containing the interface is relaxed without any constraint; in particular volume changes are allowed, in order to eliminate all

short range or long-range stresses. Then the dislocation is introduced and the potential energy of the system minimized through a conjugate gradient procedure.

At the initial step of the relaxation procedure, the mobile atomic rows of the central region and the surrounding fixed rows have positions given by linear elasticity. For a screw dislocation along [001] in a cubic crystal, the anisotropic elastic field is identical with the isotropic case (Hirth and Lothe 1982) taking for the shear modulus $\mu$ the cubic shear constant $C_{44}$. Thus, in the bimaterial, the elastic field around the dislocation is obtained by the image dislocation construction (Head 1953a). When the dislocation is in medium (1), the elastic field is, in medium (1), the superposition of the fields of the real dislocation at position $x$ and of a virtual dislocation with Burgers vector $kb$, placed at image position $-x$ and, in medium (2), the field of a dislocation having Burgers vector $(1-k)b$, placed at the real dislocation position $x$; $k$ is the elastic mismatch defined by

$$
k=\frac{\mu_{2}-\mu_{1}}{\mu_{2}+\mu_{1}}. \tag{2}
$$

When the dislocation is in medium (2), the roles of media (1) and (2) are interchanged and $k$ is replaced by $-k$.

## §3. RESULTS

Before detailing the results obtained in the bicrystal, it is necessary to recall the main properties of the $a_{0}\langle 001\rangle$ screw dislocation in the homogeneous medium (part I). The dislocation configuration of interest of moving is characterized by a planar core extended along a $\{110\}$ dense plane. The core width, deduced from the localization of screw distortions along the $\{110\}$ glide plane, is around $3a_{0}$ with the $N$-body potential, which is about twice that of the pair potential $(1.6a_{0})$. If there is almost no edge component with the latter force law, a small component $(b_{x}=\pm 0.15a_{0}$; $b_{y}=\mp 0.26a_{0})$ appears with the former. There are two possible sites for the dislocation centre, which have been called 'diagonal' and 'square' according to whether it is placed at the middle of the diagonal segment $(a_{0}/2)\langle 110\rangle$ or at the centre of the square formed by four neighbouring rows. The responses of the dislocation to an applied stress are different depending on the site at which it lies which produces the complicated Peierls valleys computed in part I and represented in fig. 1. The Peierls valleys have been drawn by applying an external stress of type $\sigma_{yz}$ producing a force on the dislocation directed along the $x$ axis and, for each applied stress, the dislocation centre is defined as the centre of gravity of the arrows representing the few larger relative row displacements. The lattice friction is maximum at a 'square' site for the $N$-body potential and at a 'diagonal' site for the pair potential. The Peierls stresses are $0.0047\mu$ and $0.012\mu$ respectively.

In the bicrystal, a detailed exploration of the Peierls valleys has been performed in the region extending from $-4a_{0}$ to $+4a_{0}$ from the interface. At the initial step of a relaxation procedure, the dislocation is placed in the neighbourhood of a 'diagonal' site, $Na_{0}/2$ from the interface; an external stress $\sigma_{yz}$ is applied and the corresponding dislocation position determined, as it results from equilibration between the applied stress, the local lattice friction and the long-range image force.

![](./images/811981200297033729_10.jpg)

Representation of the Peierls valleys in the homogeneous crystal showing $(\sigma/\mu) \times 10^3$ as a function of the dislocation position (in $a_0$): (a) pair potential; (b) $N$-body potential.
The origin is on a 'square' site.

### 3.1. General behaviour of the dislocation core

#### 3.1.1. Pair potential
We first describe the evolutions in the dislocation core as the interface-disloca- tion distance is changed. The case chosen to exemplify the general core behaviour is the bicrystal $\alpha=2$ ($k=\frac{1}{3}$). Table 1 shows the core widths of dislocations maintained at 'diagonal' site positions under the appropriate applied stress. The core width is determined as the half-height width of the distribution along the direction in which the core extends, of the screw relative displacements across the glide plane. The

<table><caption>Table 1. Core extension (in $a_0$) as a function of the interface-dislocation separation for the pair potential. Negative distances correspond to the soft medium. The configuration type refers to the apparent extension of the core on relative displacement diagrams; it is given in units of elementary squares.</caption>
<tbody>
<tr>
<th>Interface-dislocation distance/$a_0$</th>
<td>$-2.5$</td>
<td>$-1.5$</td>
<td>$-0.5$</td>
<td>$0$</td>
<td>$0.5$</td>
<td>$1.5$</td>
<td>$2.5$</td>
</tr>
<tr>
<th>Core width/$a_0$</th>
<td>$1.77$</td>
<td>$1.77$</td>
<td>$1.68$</td>
<td>$1.94$</td>
<td>$2.83$</td>
<td>$2.83$</td>
<td>$1.77$</td>
</tr>
<tr>
<th>Configuration type</th>
<td>2C</td>
<td>2C</td>
<td>2C</td>
<td>4C</td>
<td>4C</td>
<td>4C</td>
<td>2C</td>
</tr>
</tbody>
</table>

importance of information in table 1 is that, when moving from the left to the right ('soft' medium to 'hard' medium), the core width first diminishes slightly, then increases notably after the interface has been crossed and finally decreases to a value close to the width in the homogeneous crystal. In table 1, the core configura- tions are labelled 2C or 4C; 2C refers to dislocations on a 'diagonal' site for which the large core distortions are localized mainly on the rectangle formed of two squares (the normal core in the homogeneous medium is of type 2C); designation 4C refers to the more extended core on a 'diagonal' site for which large distortions are spread over the rectangle formed of four adjacent squares along {110}.

Figure 2 displays isoenergy contours of the local dislocation strain energy, for two dislocations positioned at $-1.5a_0$ and $+1.5a_0$. The local strain energy attributed to the dislocation is computed on each atomic row as the difference between the energy of that row in the relaxed stressed crystal containing the dislocation and its energy in the stressed crystal free of dislocation. Then, an interpolation procedure is used to draw the isoenergy contours. The difference between the extensions of the two dislocations appears there clearly.

Note that at distances larger than $2.5a_0$, in either medium, the core extension $1.77a_0$ is a little larger than in the homogeneous crystal, $1.63a_0$. It has been checked that the small shift is due to the applied stress; in the homogeneous crystal, the dislocation core slightly extends under stress and this is accompanied by the appear- ance of a small edge components, $b_y=\pm0.17a_0$. A similar development of edge components is observed here as the core extends: for instance the 4C configuration of the dislocation positioned at $0.5a_0$ in the 'hard' medium exhibits displacements of $\pm0.24a_0$ and $\pm0.14a_0$ along $y$ and $x$ respectively, which represents a dilatation of about $0.15a_0/2^{1/2}$ and an edge dipole $(0.38a_0/2)[\overline{1}10]$ glissile in the (110) plane in which the core extends.

### 3.1.2. $N$-body potential
The results concerning the core widths obtained with the $N$-body potential are shown in table 2. The contraction-dilatation effect is more pronounced than with the pair potential and is quite obvious on the isoenergy contour plot of two dislocations placed at $\pm1.5a_0$ shown in fig. 3. The core shrinkage when approaching the interface in the 'soft' medium is here quite clear and is reflected in the transformation of the normal 4C type core into a 2C type. The core widening when the dislocation has passed into the 'hard' medium is spectacular and gives rise to a core extending over nine squares (9C) which is a real dissociation into two well defined partials of screw component $b/2$ (fig. 4) and of non-zero edge components as can be seen from the analysis of the distribution of relative displacements across the [110] plane on which

Table 2. Core extension (in $a_0$) as a function of the interface-dislocation separation for the $N$-body potential. Negative distances correspond to the soft medium. The configura- tion type refers to the apparent extension of the core on relative displacement dia- grams; it is given in units of elementary squares.

<table>
  <thead>
    <tr>
      <th>Interface-dislocation distance/$a_0$</th>
      <th>$-2.5$</th>
      <th>$-1.5$</th>
      <th>$-0.5$</th>
      <th>$0$</th>
      <th>$0.5$</th>
      <th>$1.5$</th>
      <th>$2.5$</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Core width/$a_0$</td>
      <td>1.77</td>
      <td>1.77</td>
      <td>1.68</td>
      <td>1.94</td>
      <td>2.83</td>
      <td>2.83</td>
      <td>1.77</td>
    </tr>
    <tr>
      <td>Configuration type</td>
      <td>4C</td>
      <td>2C</td>
      <td>2C</td>
      <td>4C</td>
      <td>9C</td>
      <td>5C</td>
      <td>4C</td>
    </tr>
  </tbody>
</table>

Fig. 2

![](./images/811981200297033729_11.jpg)

Isoenergy contours of the local strain energy for two dislocations positioned at $(a)-1.5a_0$ and $(b)+1.5a_0$ from the interface, using the Johnson pair potential; $\alpha=2$. (Distances are in $a_0/2$ units and energies in arbitrary units convenient for the graphical display.)

Fig. 3

![](./images/811981200297033729_12.jpg)

![](./images/811981200297033729_13.jpg)

Isoenergy contours of the local strain energy for two dislocations positioned at (a) $-1.5a_0$ and
(b) $+1.5a_0$ from the interface, using the $N$-body potential; $\alpha=2$ bicrystal. (Distances
are in $a_0/2$ units and energies in arbitrary units convenient for the graphical display.)

the core extends (fig. 4). Similarly to the pair potential, notable edge components
accompany the core extension.

The changes in the core width can qualitatively be understood on the basis of a
description of the core configuration in terms of continuous distribution of infinite-
simal dislocations, following Nabarro (1947). In a homogeneous crystal, the core
structure is established when two factors equilibrate: the mutual repulsion of infini-
tesimal dislocations on one hand and the restoring force opposing the creation of
any stacking fault on the other hand. In the presence of an interface, two additional
factors modify the core: the applied stress and the image force. The effect of the

Fig. 4

![](./images/811981200297033729_14.jpg)

Configuration 9C obtained with the N-body potential when the dislocation is initially positioned at $a_0/2$ in the 'hard' medium. (a) Conventional map of relative displacements along [001]. An arrow joining two neighbouring rows (length $a_0/2^{1/2}$) represents a relative displacement $b/4$. (b) Distribution of the screw component of the Burgers vector along the fault plane (110) (distances are in $a_0/2$ units). (c) In-plane relative displacements ((---), $x$ component: (——), $y$ component) along the trace of the $\{110\}$ plane in which the core extends (units $h = a_0/2^{1/2}$ along the core extension direction and $b$ for relative displacements).

applied stress is uniform throughout each medium, contrary to the image force rapidly decreasing with increasing distance to interface. The parts of the dislocation core close to interface feel more strongly the image force than those farther away; if the dislocation is in the 'soft' medium, the repulsion of the 'hard' medium is stronger on the core region close to the interface which produces the decrease of the core width. The effect is opposite when the dislocation is in the 'hard' medium and results in a core widening. Nabarro (1947) has given the solution, showing clearly the core widening, for a dislocation near the free surface of a solid, which corresponds to the limiting case $\alpha = \infty$ ($k = -1$). It is important to note that, contrary to the 'soft'

medium, the dislocation is in unstable equilibrium in the 'hard' medium. In the atomistic simulation, it is still possible to determine dislocation configurations in the 'hard' medium because they are stabilized by the lattice friction. Limitations to this effect are described in next section.

### 3.2. Peierls valleys in the interface region

#### 3.2.1. Pair potential
The results for the pair potential are gathered in fig. 5. Four bicrystals have been studied, characterized by $k=\frac{1}{3}, \frac{1}{2}, \frac{2}{3}$ and $\frac{9}{11}$, that is $\alpha=2,3,5$ and 10. The quantity plotted along the $y$ axis is $1 / k(\sigma / \mu)$ where $\sigma$ and $\mu$ are the local stress $\sigma_{y z}$ and local shear modulus $C_{44}$ respectively. It is recalled that such a stress field is realized by imposing a uniform strain $\varepsilon_{y z}$ throughout the bicrystal. The stress curves are normalized by $k$ to allow for comparison between different bicrystals.

Figure 5 shows that, far from the interface, the Peierls valleys are identical with those of the homogeneous medium and distortions of increasing importance appear when approaching the interface. A relatively minor effect is the shift in the point which can be regarded as the bottom of the valley, that is the medium stress point; it

Fig. 5
![](./images/811981200297033729_15.jpg)

![](./images/811981200297033729_16.jpg)

Applied stress maintaining the dislocation, as a function of its position: (a) $k=\frac{1}{3}$, $\alpha=2$;
(b) $k=\frac{1}{2}$, $\alpha=3$; (c) $k=\frac{2}{3}$, $\alpha=5$; (d) $k=\frac{9}{11}$, $\alpha=10$. Comparison of the simulation
using the pair potential and of the calculation of Pacheco and Mura (1969). Straight
segments of negative slope are meaningless and drawn only for graphical convenience.

may be displaced from the exact 'diagonal' site position at $Na_{0}/2$. At large $k$, part of
this shift is due to the interface displacement after relaxation.

More important is the evolution of valleys amplitude with distance to interface.
In the homogeneous medium, the Peierls stresses are the same in the $x$ and $-x$
directions, the maximum and minimum stresses of a given valley have the same
absolute value: $\tau_{\mathrm{P}}=\tau_{1}=-\tau_{2}$. In the bicrystal, the equality does not hold any
more because of the image force and each valley is characterized by its maximum
$\tau_{1}$ and minimum $\tau_{2}$. The effect that we describe here concerns the amplitude
$\Delta \tau=\tau_{1}-\tau_{2}$; some $a_{0}$ away from the interface, the valley amplitude is identical
with that of the homogeneous medium and, when approaching the interface from
the left ('soft' medium), $\Delta \tau$ increases whereas it decreases when approaching from
the right. The magnitude of this phenomenon is more important at large $k$ so that,
for $k>\frac{1}{3}(\alpha>2)$, there appears on the 'hard' side of the interface a zone where the
Peierls valleys vanish completely. In this region, dislocations can no longer be main-
tained in equilibrium. The unstable zone becomes wider as $k$ is raised and, at $k=\frac{9}{11}$,
no stable position can be found on the 'hard' side in the investigated area $4a_{0}$ wide.

However, at positions corresponding approximately to the valleys of this zone, there exists a small interval of applied stress for which the dislocation can be stabilized but in a widely dissociated form with the remaining partial in the 'soft' medium. This point is discussed in §4.

Some reasons can be found for the observed evolution of the amplitude of the Peierls valley amplitude. Figure 5 shows the dislocation position as a function of applied stress, that stress balancing the effect of lattice friction and image force. In the homogeneous crystal, let us call $\Delta x$ the distance between the middle of a valley and the point where the applied stress is maximum: $\tau_{\mathrm{P}}=\tau(\Delta x)=-\tau(-\Delta x)$, where $\Delta x$ is a fraction of $a_{0} / 2$, the valley's periodicity. Let us assume an image force varying with distance $x$ as $-\alpha / x$ (directed to the left, $\alpha>0$ ), so that the stress contribution opposing it is $\alpha / x$. In the 'soft' medium, the amplitude of the Peierls valleys is $\Delta \tau=\tau(\Delta x)-\tau(-\Delta x)=2 \tau_{\mathrm{P}}+(2 \alpha / x)(\Delta x / x)$ whereas, in the 'hard' medium, it becomes $\Delta \tau=\tau(\Delta x)-\tau(-\Delta x)=2 \tau_{\mathrm{P}}-(2 \alpha / x)(\Delta x / x)$. The effect changes sign from one medium to the other, increasing the amplitude of the Peierls valleys in the 'soft' medium and decreasing it in the 'hard' medium. The effect becomes more important as the interface is approached, which can account for the occurrence of the zone of instability on the right-hand side of the interface.

From the complicated stress curves, it is not easy to extract the effect of the image force. The investigation of bicrystals in which the two halves have close elastic moduli (part I) has revealed the relevance of the calculation by Pacheco and Mura (1969) based on the Peierls-Nabarro dislocation core, at least in the case of the dislocation investigated here which presents a planar core. The stress obtained by Pacheco and Mura is written

$$
\frac{\tau}{\mu}=\frac{\alpha}{\pi^{2}} \frac{b}{h}\left(\frac{1}{1+(x / h)^{2}}+\frac{\tan ^{-1}(x / h)}{x / h}\right). \tag{3}
$$

It has been drawn in fig. 5. Note that the ratio $b / h$ of the Burgers vector to the interplanar distance in the glide plane, here equal to $2^{1 / 2}$, does not appear in the original paper of Pacheco and Mura where it is implicitly set to unity. The agreement with the mean stress of each valley is not bad, particularly at the interface. Slightly apart from the interface, on both sides, the middle of the computed valleys is larger than the Pachecho-Mura curve as already noted in the case of bicrystals with small $k$. When comparing the different bicrystals the quantity $1 / k(\sigma / \mu)$ seems to increase with increasing $k$, a behaviour which is not predicted by the Pachecho-Mura model. This is particularly notable for the case $\alpha=10$; however, such an asymmetric bi medium may have special properties.

#### 3.2.2. $N$-body potential
The same area $8 a_{0}$ wide, centred on the interface, has been explored with the Finnis-Sinclair-type potential for $\alpha$-iron and two bicrystals have been studied corresponding to $k=\frac{1}{3}$ and $\frac{2}{3},(\alpha=2$ and 5). Overall, the main features described above remain although the Peierls valleys appear here somewhat more complicated because both 'diagonal' and 'square' sites are possible initial positions for the dislocation. The general level of stress is smaller than with the pair potential, as expected from the results of the homogeneous case (fig. 6).

Fig. 6

![](./images/811981200297033729_17.jpg)

Applied stress maintaining the dislocation, as a function of its position: (a) $k = \frac{1}{3}$, $\alpha = 2$;
(b) $k = \frac{2}{3}$, $\alpha = 5$; Comparison of the simulation using the $N$-body potential and of
the calculation of Pacheco and Mura (1969). Straight segments of negative slope are
meaningless and drawn only for graphical convenience.

Concerning the core extension, it is recalled that, in the homogeneous medium
under stress, this quantity is smaller on 'square' sites than on 'diagonal' sites, con-
trary to the pair potential. This probably explains that the tendency to core narrow-
ing in the 'soft' medium is reflected in the reduction of the 'diagonal' site valleys and
the increasing amplitude of the 'square' site valleys as the interface is approached.
This is true as long as the normal 4C core has not transformed into a 2C configura-
tion, with $k = \frac{1}{3}$, an important 'diagonal' site valley appears near the interface, the
core having transformed into a 2C configuration. An even narrower new core
configuration forms for $k = \frac{2}{3}$; the large core displacements are confined to a square
formed of four unit squares, the dislocation line lying almost at the central row

position (configuration 1C in fig. 7). In the 'hard' medium, where the core tends to widen, only the 'diagonal' site valleys of type 4C appears.

Figure 6 shows that the computed stresses compare well with the calculation of Pacheco and Mura. The amplitude of Peierls valleys is smaller than with the pair potential, as in the homogeneous medium, and the asymmetry introduced by the interface less visible than with this force law. The wider dislocation core extension with the $N$-body potential is the common origin of these two properties. For the same reason, the zone of instability is more extended for a fixed $k$ and it appears already at $k=\frac{1}{3}$. As in the case of small $k$ values, the stress at the interface is smaller than with the Johnson potential.

Fig. 7

![](./images/811981200297033729_18.jpg)

Configuration 1C ($N$-body potential; $k=\frac{2}{3}$; applied stress, $0.025\mu$). (a) relative displacements along Oz; (b) isoenergy contours. The initial dislocation position is at $a_0/2$ from the interface in the soft medium.

### 3.3. Comparison between image forces deduced from applied stresses and from energy calculations

Two possible approaches to the image force have been detailed in part I: one based on the application of an external stress maintaining the dislocation at a position, and the other based on the computation of the bicrystal strain energy as a function of the dislocation position. These two definitions do not cover exactly the same concept since the first is the stress maintaining the dislocation in a static equilibrium and the second is the stress necessary to move from one Peierls valley to the neighbouring Peierls valley by thermal activation. The consistency of these two approaches for large $k$ values has to be examined. For comparison, we need a case without any unstable zone and this limits the choice to the bicrystal $\alpha=2$ with the pair potential.

In the case of bicrystals characterized by a small value of $k$, there is a stable position for the dislocation in each Peierls valley, and the image force can be computed, by finite differences, from the strain energy stored in the bicrystal when the dislocation sits at these positions. This method is adapted to the bicrystals with large $k$ values in the following way: from the Peierls valley analysis using applied stresses presented above, it is possible to determine a medium point for each valley as the point where the stress has the mean value $\tau_{\mathrm{m}}=(\tau_{2}+\tau_{1})/2$. When this stress is applied, the strain energy $W$ of the dislocation is computed as the difference between the strain energy stored in the stressed solid containing a dislocation and the stressed solid free of dislocations. In this way, the contribution of the applied stress is eliminated. The image force $f_{x}$, or the equivalent stress $\sigma_{yz}$ between two neighbouring positions, is

$$
f_{x}=\sigma_{yz}b=-\frac{\Delta W}{\Delta x}. \tag{4}
$$

The energy of the dislocation, plotted in fig. 8, is calculated using the procedure detailed in §2.2.1 of part I and contains both contributions of the atomistic region

**Fig. 8**
![](./images/811981200297033729_19.jpg)

Variation in the dislocation energy with distance to interface. The dislocation positions at which the total strain energy is computed are the middles of the Peierls valleys. The energy unit is $\mu b^{2}/4\pi$. The reference energy is the energy of the dislocation at the interface.

Fig. 9

![](./images/811981200297033729_20.jpg)

Comparison of the two ways of approaching the image force on the dislocation: (———), applied stress maintaining the dislocation at its position; (----), gradient of the dislocation energy computed by finite differences from the energy values of fig. 8.

and of the surrounding elastic continuum. The energy is an increasing function of the dislocation abscissa whose shape is similar to those obtained for small $k$ values.

Comparison of the two approaches to image force is given in fig. 9. The stress $\sigma_{y z}$ deduced from energies at the middles of the Peierls valley has to be divided by the local shear modulus to be compared with the directly applied uniform strain. There is no ambiguity in the shear modulus value inside each medium and, at the interface, it has been set to the mean value, in accordance with our choice of interatomic potentials. The agreement can be regarded as satisfactory, keeping in mind that both definitions are not strictly equivalent.

## §4. DISSOCIATION OF THE DISLOCATION AT THE INTERFACE

It has been seen that, when approaching the interface from the right ('hard' medium), the decrease in the Peierls valleys amplitude is such that, for sufficiently large $k$, the valleys disappear completely. As the dislocation is initially placed in this region, it cannot be maintained there under any applied stress; it moves away in one medium or the other as minimization proceeds. However, as already mentioned, it is possible to find a narrow range of applied stresses for which the dislocation does not move away but instead undergoes a notable dissociation.

### 4.1. Formation of dissociated configurations

Largely dissociated configurations were first obtained by chance when trying to stabilize the dislocation in the region which later proved to be an unstable zone in the 'hard' medium. The Burgers vectors of the two partials have the same screw component $b / 2$ and opposite edge components; compare for instance the configuration extending on nine unit squares (9C) obtained with the $N$-body potential, in the bicrystal $\alpha=2$ (fig. 4), or the 16C configuration obtained with the pair potential in a bicrystal $\alpha=5$ (fig. 10). Note that one of the partials stays systematically in the

Fig. 10

![](./images/811981200297033729_21.jpg)

Configuration extending over 16 elementary squares (16C) obtained with the pair potential for a bicrystal $k=\frac{2}{3}(\alpha=5)$ under an applied stress $\sigma=0.08 \mu$. (a) relative displacements along Oz; (b) edge component along Ox (----) and along Oy (——).

'soft' medium, close to interface. The conditions under which such dissociated configurations occur have been systematically analysed.

In a bicrystal characterized by $k$, the dislocation is positioned, before relaxation, at a distance $d$ from the interface in the 'hard' medium, inside the zone of instability. The dissociated configuration forms when a stress $\alpha(k, d)=\mu \varepsilon(k, d)$ is applied, the interval of stress producing the dissociation being narrow, of the order of $\mu / 1000$; if the stress is lower, the dislocation escapes in the 'soft' medium and, if the stress is larger, the dislocation escapes in the 'hard' region. The numerical values of the imposed strain $\varepsilon(k, d)$ for few bicrystals and a number of initial dislocation positions $d$ have been found to follow the law $\varepsilon(k, d)=A k / d$ where $A$ is a constant of numerical value 0.095 for the pair potential and 0.09 for the $N$-body potential. This is to be compared with elasticity, where the relation between the (unstable) equilibrium dislocation position (in units of $b$) and the applied stress is written

$$
\varepsilon(k, d)=\frac{\sigma(k, d)}{\mu}=\frac{1}{4 \pi} \frac{k}{d}=0.0796 \frac{k}{d}. \tag{5}
$$

Thus dissociation occurs when, at the initial step of the energy minimization procedure, the dislocation is at the unstable equilibrium position given by elasticity. There is no net force on the dislocation which then is no longer inclined to move to the left or to the right. The tendency to dissociation can be explained on the same basis as the variations in core width (cf $\S 3.1$ ); the parts of the dislocation core close to the interface are more subject to image forces, directed to the left, and the parts of the core farther away in the 'hard' medium feel the applied stress more strongly and are pushed to the right.

The fact that the tendency to core widening is not realized by a simple extension of the core distribution but through formation of two well defined partials with screw component $b / 2$, although no stable stacking fault is known to exist in the bcc structure, can be explained by considering the $\gamma$ surface on $\{110\}$ planes; this

Fig. 11

![](./images/811981200297033729_22.jpg)

$\gamma$ surface on the (110) plane for the $N$-body potential. Positions are in $a_{0}/2^{1/2}$ and $a_{0}$ units along [110] and [001] respectively. Energies have been scaled to fit the range [0, 100] in arbitrary units.

surface represents the fault energies as a function of the displacement vector for all possible faults vectors $\mathbf{f}$ on $\{110\}$ planes. Figure 11 shows the $\gamma$ surface computed with the $N$-body potential, the faults being relaxed with respect to displacements normal to the fault plane. This surface is quite similar to that of the Johnson potential (Vitek 1968) with minima at $\mathbf{f}=\mathbf{0}$ and at the points related to origin by a lattice translation, and maximum at $\mathbf{f}=(a_{0}/2)[001]$. According to the analysis of strain localization and the critical step in nucleating a dislocation ahead of a crack by Rice (1992), it is seen that the maximum relative shear along [001] between two consecutive $(\overline{1}10)$ planes is $b/2$; because of the bcc symmetry reflected on the $\gamma$ surface, the line corresponding to displacements having a component $b/2$ along [001] is the location of the 'unstable faults' defined by Rice. Along this line, the fault energy is stationary with respect to displacements along the Burgers vector direction [001] and thus defines the maximum local shear; any larger shear is neces- sarily accomplished by forming and displacing a lattice dislocation.

The $\gamma$ surface also provides indications on the appearance and development of the edge components of the two partials. The energies of 'unstable faults' decrease from $\mathbf{f}=(a_{0}/2)[001]$ where it is maximum to $\mathbf{f}=(a_{0}/2)[111]$ (a bcc lattice transla- tion) where it vanishes (centre of the $\gamma$ surface in fig. 11). When a fault of some width forms near the interface in the 'hard' medium, the appearance of edge components along [110] of opposite sign on each partial reduces the stacking-fault energy and the energy gain may be larger than the energy loss associated with formation of the edge dipole. This effect is favoured as the faults extends, which is in agreement with the results of the simulation; fig. 12 shows the edge components as a function of the initial dislocation position, with the pair potential. The limiting case would be the complete dissociation of the $a_{0}[001]$ into two $(a_{0}/2)[111]$ crystal dislocations with complete disappearance of the fault. It has not occurred in the simulation; Peierls forces exist on the partials which limit their displacement and the edge components

Fig. 12

![](./images/811981200297033729_23.jpg)

Evolution of edge components as a function of the initial dislocation position, with the N-
body potential.

of the partials are not included in the boundary conditions, which artificially stops
the partials when approaching the limits of the atomistic region.

The discussion above indicates that the dislocation we have chosen, that is an
$a_0[001]$ screw dislocation in a bcc lattice, may be a case where the core extension has
particular importance because of the possibility of dissociation with a very low fault
energy. It is not sure that the type of well defined dissociation seen in the simulation
is a general property and partly for this reason the $(a_0/2)\langle 111\rangle$ screw dislocation
which is known not to dissociate easily has been subjected to similar investigations
(Beauchamp et al. 1996).

## §5. CONCLUSIONS

After having considered the case of bicrystals in which the two halves have
similar elastic coefficients (part I), the behaviour of a dislocation in the vicinity of
the interface between two crystals presenting notably different elastic moduli has
been investigated. In this case, the image force is larger than the lattice friction on the
dislocation in the neighbourhood of the interface.

A detailed exploration of the Peierls valleys has been performed in the region
extending from $-4a_0$ to $+4a_0$ from the interface. Changes in the dislocation core
have been observed as the dislocation approaches the interface; in the 'soft' medium
the core tends to become slightly narrower, whereas it clearly widens in the 'hard'
medium. This widening has been described by Nabarro (1947) when examining the
unstable equilibrium of a dislocation near a free surface. The reason for the core
width variation is to be found in the non-uniformity of the image force as opposed to
the uniformity of the applied stress.

The applied stress maintaining the dislocation at a given position and thus
opposing the local lattice friction and the long-range image force has been deter-
mined. It is found that the mean stresses of each valley follow approximately the
curve determined by Pacheco and Mura (1969) on the basis of a continuous disloca-
tion core perturbed by the interface, although the simulation presents a peak which is
lower and more extended than the latter curve of maximum $\tau_{\text{PM}}/\mu=2k/\pi^2$. In the
bicrystal where the 'hard' medium has elastic coefficients twice those of the 'soft'
medium, it has been possible to determine the image force from the values of the

strain energy stored in the solid as a function of dislocation position. The agreement with the mean stress of each Peierls valley is satisfactory, keeping in mind that the two quantities do not have exactly the same physical meanings.

Systematic variations in Peierls valleys amplitudes have been found; when the interface is approached from the 'soft' medium side, the amplitude increases whereas it decreases when approaching from the 'hard' side. This effect is more important at large $k$ and weaker, with the potential giving the wider dislocation core. The explanation invokes the variations in the curvature of the energy of the dislocation as a function of its position, which changes sign at the interface. The decrease in the amplitudes of the Peierls valleys in the 'hard' medium is such that they completely disappear and an unstable zone forms on the 'hard' side where no applied stress is able to maintain the dislocation.

In the unstable zone of the 'hard' side, it has been possible to fix the dislocation but only after it has dissociated into two partials having $b/2$ screw components. Examination of the $\gamma$ surface on $\{110\}$ plane shows that the stacking fault, which is not normally stable in the bcc structure, is of the 'unstable fault' type to which Rice (1992) attributes a key role in the dislocation nucleation at a crack tip. The observed development of edge components on the partials as the fault widens is linked to the eventual dissociation of the $a_{0}\langle 001\rangle$ screw dislocation into two perfect $(a_{0}/2)\langle 111\rangle$ dislocations. Because the geometry we have chosen makes the above dissociation possible with a decreasing stacking-fault energy between the partials, the present results may overestimate the core-widening effect.

From the results on both types of bicrystal, with small and large differences in the elastic moduli of the two halves, a general dislocation-interface interaction law can now be proposed, which is meant to be used in mesoscale studies such as the formation and stability of pile-ups at an interface. This model, which is to be detailed in a separate paper, is built on the total energy balance of the dissociated configuration, as a function of the stacking-fault energy and the average position versus the interface; preliminary results can be found in the paper by Beauchamp et al. (1996).

## REFERENCES

ACKLAND, G. J., TICHY, G., VITEK, V., and FINNIS, M. W., 1987, Phil. Mag. A, 56, 735.
BEAUCHAMP, P., and LÉPINOUX, J., 1996, Phil. Mag. A, 74, 919.
BEAUCHAMP, P., LÉPINOUX, J., LARDON, I., and KENTABLI, H., 1996, Stability of Materials, NATO Advanced Study Institute Series, edited by A. Gonis, P. E. A., Turchi and J. Kudrnovsky (Peplum Press), p. 651.
BALL, A., and SMALLMAN R. E., 1966, Acta metall., 14, 1517.
CSERTI, J., TICHY, G., and VITEK, V., 1994, Solid St. Phenom., 35-36, 545.
FINNIS, M. W., and SINCLAIR, J. E., 1984, Phil. Mag., 50, 45.
HEAD, A. K., 1953a, Phil. Mag., 44, 92; 1953b, Proc. phys. Soc. B, 66, 793.
HIRTH, J. P., and LOTHE, J., 1982, Theory of Dislocations (New York: Wiley).
JOHNSON, R. A., 1964, Phys. Rev. A, 134, 1329.
NABARRO, F. R. N., 1947, Proc. phys. Soc., 59, 256.
PACHECO, E. S., and MURA, T., 1969, J. Mech: Phys. Solids, 17, 163.
RICE, J. R., 1992, J. Mech. Phys. Solids, 40, 239.
SCHULSON, E. M., and TEGHTSOONIAN, E., 1969, Phil. Mag., 19, 155.
UMAKOSHI, Y., and YAMAGUCHI. M., 1981, Phil. Mag. A, 41, 573.
VITEK, V., 1968, Phil. Mag. 18, 773.