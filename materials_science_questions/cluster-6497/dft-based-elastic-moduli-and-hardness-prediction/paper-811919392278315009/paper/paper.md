A study of the size-dependent elastic properties of ZnO nanowires and nanotubes

This article has been downloaded from IOPscience. Please scroll down to see the full text article.

2008 Nanotechnology 19 285710

(http://iopscience.iop.org/0957-4484/19/28/285710)

View the table of contents for this issue, or go to the journal homepage for more

Download details:
IP Address: 130.63.180.147
The article was downloaded on 03/08/2013 at 12:18

Please note that terms and conditions apply.

# A study of the size-dependent elastic properties of ZnO nanowires and nanotubes

J Hu, X W Liu and B C Pan

Hefei National Laboratory for Physical Sciences at Microscale, and Department of Physics,
University of Science and Technology of China, Hefei, Anhui 230026,
People's Republic of China

Received 31 January 2008, in final form 6 May 2008
Published 3 June 2008
Online at stacks.iop.org/Nano/19/285710

## Abstract
We present our calculations of the Young's modulus of ZnO nanowires and nanotubes by using the empirical Buckingham-type potential. Our results indicate that the Young's moduli of ZnO nanowires increase as the diameters decrease, and the Young's moduli of ZnO nanotubes increase as the thicknesses decrease. Furthermore, we find that such size-dependent elastic properties mainly arise from the lateral facets of the nanowires and nanotubes. In particular, for a ZnO nanotube with a thin wall, the Coulomb interaction between the ions of the outer and inner atomic layers plays an important role in the Young's moduli of the surface atomic layers.

## 1. Introduction
Since the discovery of carbon nanotubes (NTs) in 1991 [1], nanomaterials have attracted much attention due to their potential applications in electronic and optoelectronic devices [2]. Usually, when nanomaterials, such as nanotubes, nanowires, nanobelts, and so on, act as the building blocks of a nanodevice, they will probably be deformed to some extent. So, it is necessary for us to gain knowledge of the mechanical properties of nanomaterials. Previous studies have revealed that most nanomaterials showed size-dependent mechanical properties [3-10]. The mechanisms of such mechanical properties have also been discussed. For example, the surface tension in Ag and Pd nanowires (NWs) [6], the corner stiffness in Au NWs [7] and the nonlinear response of the cores in Cu NWs [9] were proposed to be responsible for the size-dependent elastic properties of these metallic NWs.

Nanometer-scale ZnO is an important nanomaterial [11, 12]. In recent years, a great variety of ZnO nanostructures have been synthesized [13-16], and the structural, electric, optical and piezoelectric as well as mechanical properties have been investigated experimentally. As regards mechanical properties, it was found that the measured bending moduli of ZnO nanobelts (NBs) were related to the growth-direction-dependent aspect ratio and the stacking faults [17-19]; another measurement [20] indicated that the bending moduli of ZnO NBs were independent of their surface-to-volume ratio. For ZnO NWs, it was found that when their diameters were in the range from 17 to 550 nm, the measured Young's moduli [23] increased as the diameter decreased, and the values of these Young's moduli were all larger than the bulk value.

On the theoretical side, the Young's moduli of NBs were predicted to be dependent on their lateral dimensions, since the surface-stress-induced internal compressive stress played an important role in the change of the Young's modulus [21, 22]. As for the ZnO NWs, the elastic modulus evaluated by linear elasticity theory [24] showed that their modulus decreased on decreasing the diameter $(D)$ when $D > 20$ nm, and moreover, the predicted modulus of the ZnO NWs would be lower than the bulk modulus. This seems inconsistent with the common view in which a one-dimensional nanostructure is usually stiffer than the related bulk materials. On the other hand, the mechanical properties of the ZnO nanotubes, which possess more lateral facets than the same sized ZnO nanowire, have not been studied.

Investigation and understanding of the mechanical properties of both ZnO nanowires and ZnO nanotubes are valuable for their potential application. In this work, we study the elastic properties of ZnO NWs and NTs systematically, based on classic molecular dynamical simulations. It is revealed that the Young's moduli of ZnO NWs and NTs depend on their diameters and wall thicknesses, respectively. Moreover, the computed Young's moduli of these nanosystems are all higher than that of bulk ZnO. Investigation of single atomic layers of both types of nanomaterial reveals that the surface layers are stiffened significantly. We propose that the

stiffened feature of the surfaces correlates with the contraction of the surface atoms of an NW or an NT.

## 2. Computational details

As shown in section 3, the systems we consider contain a lot of atoms. Because of this, it is difficult for us to study their elastic properties at the level of density functional theory. Instead, atomic simulations based on an empirical potential are sufficient for our calculations. In this work, a Buckingham-type interatomic potential

$$
U\left(r_{i j}\right)=\frac{q_{i} q_{j}}{r_{i j}}+A \exp \left(-\frac{r_{i j}}{\rho}\right)-\frac{C}{r_{i j}^{6}}
\tag{1}
$$

is adopted. Here, $U$ is the pair potential energy contributed by the interaction between the $i$th and $j$th ions with a distance of $r_{i j}$, $q_{i}$ is the charge of the $i$th ion, and the parameters of $A$, $\rho$ and $C$ for ZnO are given in [21]. The first term in equation (1) describes the long-range Coulomb interactions between two ions, and the second and the third terms represent their short-range interactions. To handle the long-range Coulomb interactions, we utilize the corrected Ewald summation [25, 26] to reduce the computational demand as well as to enhance the computational efficiency.

Using this potential model, the optimal lattice constants of wurtzite ZnO are evaluated to be $a=3.265$ Å, $c/a=1.579$, and $u=0.3882$, which are consistent with the experimental values $a=3.250$ Å, $c/a=1.602$ and $u=0.3825$.¹ On the other hand, since there exist surfaces in each NW and NT, it is necessary to validate this classic potential for handling the surfaces of ZnO. For this purpose, the nonpolar (10$\overline{1}$0) and (11$\overline{2}$0) surfaces are selected for our testing. Our calculated surface energies of both relaxed surfaces are 1.14 and $1.19\ \text{J}\ \text{m}^{-2}$, respectively, which are consistent with those (1.15 and $1.25\ \text{J}\ \text{m}^{-2}$) obtained from local density approximation (LDA) calculations [27].

The elastic property of a system can be represented by the Young's modulus ($Y$). Conventionally, to calculate $Y$ of either an NW or an NT, one respectively loads certain compressive and tensile strains ($\epsilon$) on the system along its axial direction. We thus obtain the total energy of the system as a function of the loaded strains. Then the energy curve, $U(\epsilon)$, is fitted with a cubic polynomial. Inserting the fitted polynomial into the following expression

$$
Y=\frac{1}{\Omega_{0}}\left(\frac{\partial^{2} U}{\partial \epsilon^{2}}\right)_{\epsilon=0},
\tag{2}
$$

we finally evaluate the Young's modulus, $Y$, of this system. In the above expression, $\Omega_{0}$ is the equilibrium volume. In this work, the applied $\epsilon$ range is from $-2.5\%$ to $2.5\%$, with an increment of $0.5\%$. Applying this method to bulk ZnO, we obtain the Young's modulus of bulk ZnO along the [0001] direction (i.e. the $c$ axis) to be 173.86 GPa, which is consistent with a recent experiment value (180 GPa) [19]. Such agreement supports this classic potential being suitable for calculations of the Young's modulus of ZnO.

Alternatively, the Young's modulus can also be evaluated from the viral stress [21]

$$
\sigma^{\alpha \beta}=\frac{1}{2 \Omega} \sum_{i} \sum_{j \neq i} f_{i j}^{\alpha} r_{i j}^{\beta},
\tag{3}
$$

where $\Omega$ is the volume of the system, $f_{ij}$ and $r_{ij}$ are the force and distance between ions $i$ and $j$ respectively, and the indices $\alpha$ and $\beta$ denote the Cartesian components. Because the loaded strains are along the axial direction (commonly along the $z$ axis in Cartesian coordinates) in our calculation, only the element $\sigma^{zz}$ is nonzero. For convenience, $\sigma^{zz}$ is written as $\sigma$ in the remainder of this paper. In terms of $\sigma$, the Young's modulus of the nanosystem along the axial direction is evaluated by

$$
Y=\left(\frac{\partial \sigma}{\partial \epsilon}\right)_{\epsilon=0}.
\tag{4}
$$

Using this scheme, $Y$ of bulk ZnO along the [0001] direction is predicted to be 173.27 GPa, almost the same as that obtained from the $U$-$\epsilon$ response.

To understand the calculated Young's modulus of a particular nanosystem, we decompose the viral stress expressed in formula (3) as follows:

$$
\sigma=\sum_{k} \frac{\Omega_{k}}{\Omega} \sigma_{k}
\tag{5}
$$

with

$$
\sigma_{k}=\frac{1}{2 \Omega_{k}} \sum_{i=1}^{N_{k}} \sum_{j \neq i} f_{i j}^{z} r_{i j}^{z}.
\tag{6}
$$

Here, $\sigma_k$ is the viral stress of the $k$th substructure in the whole system. $N_k$ and $\Omega_k$ are respectively the number of ions and the effective volume of the $k$th substructure, with requirements of $\sum N_k=N$ and $\sum \Omega_k=\Omega$. From equations (4) and (6), the Young's modulus of the $k$th substructure ($Y_k$), such as the surface(s) in an NW or an NT, can be evaluated. According to this, we can find the contribution of the particular substructures to the mechanical behaviors of the NW or the NT.

## 3. Atomic structures of NWs and NTs

In the experiments, ZnO NWs and NTs grew mainly along the [0001] direction, with lateral (10$\overline{1}$0) facets [13, 16]. Thus, a ZnO NW or NT produced usually showed a hexagonal cross section. According to this experimental information, we generate NWs and NTs from a bulk ZnO along the [0001] direction,as displayed in figure 1, where the radii of the NWs and NTs are also shown. In our calculations, five NWs with different radii, ranging from 8.707 to $47.887$ Å as listed in table 1, are considered. For the NTs, two types of structure are taken into account. In the first type of NT, the inner radii (7.618 Å) are fixed and the outer radii increase from 15.237 to $54.417$ Å with an increment of $9.795$ Å; these are denoted as

---
¹ Usually, the calculated lattice constants in theoretical studies cannot match the experimental ones exactly. However, this may not significantly affect the properties of the system considered. For example, the elastic properties are sensitive to the shape of the total energy curve around its equilibrium, but independent of the equilibrium position.

![](./images/811919392278315009_1.jpg)

Figure 1. The top view of atomic structures of ZnO NWs and NTs.
The $x$, $y$ and $z$ axes are along the [11$\bar{2}$0], [10$\bar{1}$0] and [0001]
directions, respectively. For the NWs, $R_{\rm in} = 0$.

Table 1. Structure parameters of ZnO NWs. Three periodic
supercells along the axial direction are used.

<table>
<thead>
<tr>
<th></th>
<th>Radius (Å)</th>
<th>Number of atoms</th>
</tr>
</thead>
<tbody>
<tr>
<td>NW-1</td>
<td>8.707</td>
<td>324</td>
</tr>
<tr>
<td>NW-2</td>
<td>18.502</td>
<td>1296</td>
</tr>
<tr>
<td>NW-3</td>
<td>28.297</td>
<td>2916</td>
</tr>
<tr>
<td>NW-4</td>
<td>38.092</td>
<td>5184</td>
</tr>
<tr>
<td>NW-5</td>
<td>47.887</td>
<td>8100</td>
</tr>
</tbody>
</table>

Table 2. Structure parameters of ZnO NTs. Three periodic
supercells along the axial direction are used.

<table>
<thead>
<tr>
<th></th>
<th>Type</th>
<th>Outer radius (Å)</th>
<th>Inner radius (Å)</th>
<th>Wall thickness (Å)</th>
<th>Number of atoms</th>
</tr>
</thead>
<tbody>
<tr>
<td rowspan="5">A</td>
<td>NT-A-1</td>
<td>15.237</td>
<td>7.618</td>
<td>7.619</td>
<td>756</td>
</tr>
<tr>
<td>NT-A-2</td>
<td>25.032</td>
<td>7.618</td>
<td>17.414</td>
<td>2160</td>
</tr>
<tr>
<td>NT-A-3</td>
<td>34.827</td>
<td>7.618</td>
<td>27.209</td>
<td>4212</td>
</tr>
<tr>
<td>NT-A-4</td>
<td>44.622</td>
<td>7.618</td>
<td>37.004</td>
<td>6912</td>
</tr>
<tr>
<td>NT-A-5</td>
<td>54.417</td>
<td>7.618</td>
<td>46.799</td>
<td>10260</td>
</tr>
<tr>
<td rowspan="4">B</td>
<td>NT-B-1</td>
<td>54.417</td>
<td>46.798</td>
<td>7.619</td>
<td>3348</td>
</tr>
<tr>
<td>NT-B-2</td>
<td>54.417</td>
<td>37.003</td>
<td>17.414</td>
<td>6048</td>
</tr>
<tr>
<td>NT-B-3</td>
<td>54.417</td>
<td>27.208</td>
<td>27.209</td>
<td>8100</td>
</tr>
<tr>
<td>NT-B-4</td>
<td>54.417</td>
<td>17.413</td>
<td>37.004</td>
<td>9504</td>
</tr>
</tbody>
</table>

type A; in the second type of NT, the outer radii are fixed at
54.417 Å and the inner radii increase from 17.413 to 46.798 Å;
these are denoted as type B. Here, the wall thicknesses of
the NTs range between 7.619 and 46.799 Å. The detailed
structural parameters of the NTs are listed in table 2.

## 4. Stabilities and Young's modulus of ZnO nanowires

First, we optimize each NW considered to achieve its
equilibrium. As shown in figure 2, the axial lattice constants
of the resulting NW-1 and NW-2 listed in table 1 are larger by
about 1.0% and 0.5% respectively than the value along the $c$
direction in bulk ZnO, whereas the axial lattice constants of
the other NWs are almost equal to that in the case of bulk ZnO.
These calculations indicate that a ZnO NW elongates along its
axial direction when its radius is smaller than 28 Å; moreover,
the smaller the NW is, the larger the elongation of the
NW is.

![](./images/811919392278315009_2.jpg)

Figure 2. The residual axial strains of ZnO NWs as a function of
radius. The residual axial strain is defined as the proportion of the
change of lattice constant with respective to the corresponding bulk
value.

![](./images/811919392278315009_3.jpg)

Figure 3. Total energies per Zn–O pair of NWs as a function of
radius. The plotted energies are all relative to the energy of bulk
ZnO.

Figure 3 shows the total energies of these NWs. It is
evident that the total energies of NWs increase as the radius
decreases, and all of the total energies are higher than that of
bulk ZnO. This implies that the smaller NWs are less stable.
We point out that unlike the case of carbon nanotubes, no
curvature effect of the lateral facets of the NWs contributes to
the relative stabilities of the NWs, because the lateral facets are
flat. However, examining the structural feature of the NWs, we
can observe that the surface area in a unit cell for a ZnO NW
correlates with the diameter of the NW. These finite surfaces
are different from the infinite one. Our calculation reveals that
the surface energies of the facets in NWs (from NW-1 to NW-5)
are 1.22, 1.18, 1.17, 1.16 and 1.16 J m$^{-2}$, respectively, which
increase as the surface area decreases. Clearly, for a larger
NW, its surface energy will approach that of an infinite surface.
These size-dependent surface energies mainly contribute to the
relative stabilities of the NWs, as mentioned above.

Now, we turn to the elastic properties of ZnO NWs.
The Young's modulus ($Y$) values obtained from equations (2)
and (4) are plotted in figure 4, where the two different methods
give nearly the same results. It can be seen from figure 4 that
$Y$ increases monotonically as the radius decreases. This size-
dependent trend is consistent with the previous experimental
measurement [23]. Of the evaluated Young's moduli, the
Young's modulus of the smallest nanowire (NW-1) is as large
as 213 GPa and that of the largest ZnO nanowire (NW-5)

![](./images/811919392278315009_4.jpg)

Figure 4. The Young's modulus of ZnO NWs as a function of radius.
The filled and open circles are obtained from equations (2) and (4),
respectively. The horizontal dotted line stands for the Young's
modulus of bulk ZnO along the [0001] direction.

decreases to 183 GPa. When the size of a ZnO nanowire
becomes large enough, its Young's modulus should approach
the bulk value. On the other hand, the fact that all the values
of $Y$ are higher than the bulk value demonstrates that the ZnO
NWs are stiffer than the bulk ZnO, and such stiffness is more
remarkable for smaller NWs.

Now we turn our attention to the Young's modulus of
each atomic layer, including the layer consisting of surface
atoms in the ZnO nanowires. According to the viral stress
expressed in equations (5) and (6), the Young's modulus
of each atomic layer with hexagonal cross section (seen in
figure 1) is calculated; the values are displayed in figure 5.
Strikingly, the Young's moduli of the surface layers of all
NWs considered are considerably larger than the bulk value
of $Y$, implying that the surfaces of the NWs are significantly
stiffened. Furthermore, the Young's modulus of surfaces
increases as the radius of the corresponding NW decreases,
evidently exhibiting a size-dependent feature. For the interior
atomic layers of the NWs considered, the values of their
Young's moduli depend on the diameter of the NW. In the
case of NW-1, the Young's moduli of the interior atomic layers
are lower than the bulk value, which means that the interior
layers of NW-1 are softer with respect to bulk ZnO; for NW-2,
the respective Young's moduli are almost the same as the bulk
value; as the diameter of an NW becomes larger, the Young's
moduli of their interior atomic layers are slightly stiffer than
bulk ZnO. We emphasize that the variation (stiffening and
softening) of the Young's moduli of the interior atomic layers
of the ZnO NWs above are not significant except for NW-1.
So, the lateral facets of a ZnO NW are critically responsible
for the enhancement of the mechanical property of the NWs.

The different stiffening or softening behaviors of the
different atomic layers shown in figure 5 can be related to the
differences of the atomic structures. In a ZnO NW, the surface
atoms contract towards the core due to the reduction of their
neighboring coordinates. This results in shorter interatomic
bond lengths in the lateral facets, exhibiting a compressive
strain there. Furthermore, the compressive strain in a small
NW is greater with respect to that in a large NW. In contrast,
the bond lengths between atoms in the interior atomic layers of
a small sized nanowire like NW-1 or NW-2 are slightly longer
than that of bulk ZnO due to the axial elongations, as shown
in figure 2. Consider a simple system consisting of two atoms,
in which the two atoms interact with each other. It is known
that a loaded compressive strain around the equilibrium of the
two-atom system makes a larger stress than a loaded tensile
strain with the same amplitude. According to (4) and (6), a
compressive strain causes a larger increment of the Young's
modulus than a tensile strain. Note that the interaction between
any two atoms in a particular NW can be similarly described
by such a two-atom model. Combining this with the structural
features in the atomic layers as mentioned above, we can
conclude that the stiffening at surfaces of all the NWs has
originated from the compressive strain of the surfaces, and that
the softening at interior atomic layers of NW-1 has stemmed
from their tensile strain.

![](./images/811919392278315009_5.jpg)

Figure 5. The symbols represent the Young's modulus of each
atomic layer of the ZnO NWs with different radius. The atomic
layers are recorded from the outermost layer to the innermost layer.
The horizontal dashed and dashed-dotted lines are the Young's
modulus of NW-5 and bulk ZnO along the [0001] direction,
respectively.

(This figure is in colour only in the electronic version)

## 5. Stabilities and Young's modulus of ZnO nanotubes

A ZnO NT is another kind of nanometer-scale ZnO material.
Unlike the multiwalled carbon nanotube, the synthesized
ZnO nanotube not only has a periodic structure along its
axial direction but also characterizes the feature of a finite
crystal [15, 16], which is the so-called single-crystal nanotube.
Just as was done for the ZnO NWs, the ZnO NTs considered
are also fully relaxed. Similarly, the axial lattice constants of
NT-A-1 and NT-B-1 expand by about 1.0% with respect to
the corresponding bulk value. The calculated total energies
of these ZnO NTs (figure 6) indicate that their stabilities are
all less than that of bulk ZnO. This is not surprising because
the inner and outer surfaces in an NT contribute to a higher
energy. Moreover, we find that the total energy increases as
the thickness of the tube decreases. These results are similar to
those for ZnO NWs.

The Young's moduli of these ZnO NTs are calculated; they
are plotted in figure 7. From figure 7, we can observe several
aspects exhibited in the curves: (1) the values of $Y$ are very
close if the thicknesses of two types of NT are same, even
if their radii are very different; (2) the values of $Y$ increase
monotonically as the wall thicknesses decrease, and (3) all the
$Y$ values of the tubes are higher than the bulk value.

![](./images/811919392278315009_6.jpg)

Figure 6. Total energies per Zn-O pair of NTs as a function of wall thickness with respect to the energy of bulk ZnO.

![](./images/811919392278315009_7.jpg)

Figure 7. The Young's modulus of ZnO NTs as a function of the wall thickness. The horizontal dotted line represents the Young's modulus of bulk ZnO along the [0001] direction.

We speculate that these size-dependent elastic properties have also originated from the surface stiffness. To demonstrate our speculation, we calculate the Young's modulus of each atomic layer in a ZnO NT. The results indicate that the Young's moduli of either the outer walls or the inner walls are significantly higher than the bulk value as well as higher than the values of $Y$ of the corresponding NTs, which implies that both the outer and the inner walls of ZnO NTs are indeed stiffened. However, it should be pointed out that the Young's moduli of the outer and inner walls of both types of NT show different size-dependent behaviors, as displayed in figure 8. For the NTs of type A, the Young's moduli of outer walls firstly increase slightly and then decrease slowly as the thicknesses of the walls increase, whereas the Young's moduli of the inner walls increase largely. In contrast to type A, the Young's moduli of both outer and inner walls in the thin NTs of type B increase sharply as the wall thicknesses increase; when the thicknesses of the NTs are larger than about $17\ \mathring{\text{A}}$, the Young's moduli increase slowly; and finally, when the thicknesses are larger than about $27\ \mathring{\text{A}}$, the Young's modulus of the outer (inner) wall increases (decreases) slightly. Additionally, for any NT, the outer wall is stiffer than the inner wall.

![](./images/811919392278315009_8.jpg)

Figure 8. The Young's modulus of the outer and inner walls of ZnO NTs as a function of wall thickness.

To understand these behaviors, we also examine the atomic structures of the outer and inner surfaces of the NTs. We find that, similar to the case of the NWs, the surface atoms of each NT contract to its wall center, which leads to shorter interatomic bond lengths at the lateral facets with respect to bulk ZnO. Moreover, the interatomic bond lengths of the outer walls are slightly shorter than that of inner walls. This variation of the bond lengths in the surfaces is responsible for the stiffened surfaces and for the different stiffness between the outer wall and the inner wall for each NT. However, variation of the Young's modulus of either outer or inner walls cannot be interpreted only by the structural features mentioned above. Therefore, there must be other reasons that are responsible for these behaviors. It is known that the ionicity of ZnO is remarkable, so the long-range Coulomb interactions between ions in ZnO are pronounced. For NT-A-1 in table 2, the wall thickness and the inner radius are only 7.619 and $7.618\ \mathring{\text{A}}$, respectively, and therefore the Coulomb interactions between the outer and inner walls as well as the Coulomb interactions between the facets of an inner wall are all significant. Our calculation indicates that these interactions decrease the values of $Y$ of both surfaces of a tube effectively. As the radius of the tube increases, the thickness of a type-A NT increases, and the surface area of the outer wall of the tube becomes large. In this case, the long-range interaction between the outer and inner walls as well as between the lateral facets of the outer wall will decrease. Consequently, the Young's modulus of the inner wall increases and the Young's modulus of the outer wall decreases slightly. Similarly, such a Coulomb interaction also play an important role in the ZnO NTs of type B. For NT-B-1, the wall thickness is the same as for NT-A-1. However, the surface areas of both outer and inner walls of NT-B-1 are much larger than those of NT-A-1, which results in much stronger interaction between the outer and inner walls in NT-B-1 than in NT-A-1. Consequently, the Young's moduli of the outer and inner walls of NT-B-1 are significantly lower than those of NT-A-1. As the inner radius of a tube of type B decreases, the values of $Y$ of the outer and inner walls of each NT will increase due to the increasingly weak long-range interaction between the outer and inner walls. However, when the inner radius is reduced to about $17\ \mathring{\text{A}}$, the interactions between facets of inner wall become strong, resulting in a drop of the $Y$ of the inner wall.

### 6. Summary

In summary, by using an empirical Buckingham-type potential, we evaluate the Young's moduli of ZnO nanowires and nanotubes. We find that the Young's moduli of ZnO nanowires increase as the diameter decreases, and the Young's moduli of ZnO nanotubes increase on decreasing the wall thickness. Through decomposing the Young's modulus of a whole nanowire or a nanotube into atomic layers, we find that the size-dependent elastic properties of nanowires and nanotubes mainly arise from the stress-induced surface stiffening. In addition, we find that for a ZnO nanotube with a thin wall, the Coulomb interaction between the outer and inner surfaces plays an important role in the Young's moduli of the surface atomic layers.

### Acknowledgments

This work is supported by the University of Science and Technology of China, the Chinese Academy of Science, National Science Foundation of China (Grant Nos NSFC10574115 and NSFC50721091). B C Pan is grateful for the support of the National Basic Research Program of China (2006CB922000). The HP-LHPC of USTC is acknowledged for computational support.

### References

[1] Iijima S 1991 *Nature* **354** 56
[2] Xia Y, Yang P, Sun Y, Wu Y, Mayers B, Gates B, Yin Y, Kim F and Yan H 2003 *Adv. Mater.* **15** 353
[3] Broughton J Q, Meli C A, Vashishta P and Kalia R K 1996 *Phys. Rev. B* **56** 611

[4] Li X X, Ono Y, Wang Y L and Esashi M 2003 *Appl. Phys. Lett.* **83** 3081
[5] Nilsson S G, Borrise X and Montelius L 2004 *Appl. Phys. Lett.* **85** 3555
[6] Cuenot S, Fretigny C, Demoustier-Champagne S and Nysten B 2004 *Phys. Rev. B* **69** 165410
[7] Diao J K, Gall K, Dunn M L and Mech L 2004 *Phys. Solids* **52** 1935
[8] Zhou L G and Huang H C 2004 *Appl. Phys. Lett.* **84** 1940
[9] Liang H Y, Upmanyu M and Huang H C 2005 *Phys. Rev. B* **71** 241403(R)
[10] Lee B and Rudd R E 2007 *Phys. Rev. B* **75** 041305(R)
Lee B and Rudd R E 2007 *Phys. Rev. B* **75** 195328
[11] Wnag Z L and Song J H 2006 *Science* **312** 242
[12] Zhao M H, Wang Z L and Mao S X 2004 *Nano Lett.* **4** 587
[13] Wang Z L 2004 *J. Phys.: Condens. Matter* **16** R829
[14] Sun Y, Riley D J and Ashfold M N R 2006 *J. Phys. Chem. B* **110** 15186
[15] Mensah S L, Kayastha V K, Ivanov I N, Geohegan D B and Yap Y K 2007 *Appl. Phys. Lett.* **90** 113108
[16] Zhang G Q, Adachi M, Ganjil S, Nakamura A, Temmyo J and Matsui Y 2007 *Japan. J. Appl. Phys.* **46** L730
[17] Bai X D, Gao P X, Wang Z L and Wang E G 2003 *Appl. Phys. Lett.* **82** 4806
[18] Mai W J and Wang Z L 2006 *Appl. Phys. Lett.* **89** 073112
[19] Lucas M, Mai W J, Yang R S, Wang Z L and Riedo E 2007 *Nano Lett.* **7** 1314
[20] Ni H and Li X D 2006 *Nanotechnology* **17** 3591
[21] Kulkarni A J, Zhou M and Ke F J 2005 *Nanotechnology* **16** 2749
[22] Kulkarni A J and Zhou M 2006 *Acta Mech. Sin.* **22** 217
[23] Chen C Q, Shi Y, Zhang Y S, Zhu J and Yan Y J 2006 *Phys. Rev. Lett.* **96** 075505
[24] Wang G F and Li X D 2007 *Appl. Phys. Lett.* **91** 231912
[25] Brodka A and Grzybowski A 2002 *J. Chem. Phys.* **117** 8208
[26] Brodka A and Sliwinski P 2004 *J. Chem. Phys.* **120** 5518
[27] Meyer B and Marx D 2003 *Phys. Rev. B* **67** 035403