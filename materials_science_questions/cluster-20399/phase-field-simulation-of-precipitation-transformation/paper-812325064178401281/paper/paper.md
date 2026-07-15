Atomistic simulation of precipitation hardening in α-iron: influence of precipitate shape and
chemical composition

This content has been downloaded from IOPscience. Please scroll down to see the full text.

2005 Modelling Simul. Mater. Sci. Eng. 13 35

(http://iopscience.iop.org/0965-0393/13/1/003)

View the table of contents for this issue, or go to the journal homepage for more

Download details:

IP Address: 128.111.121.42
This content was downloaded on 06/10/2013 at 06:36

Please note that terms and conditions apply.

# Atomistic simulation of precipitation hardening in $\alpha$-iron: influence of precipitate shape and chemical composition

Christopher Kohler$^{1}$, Peter Kizler$^{2}$ and Siegfried Schmauder$^{1}$

$^{1}$ Institut für Materialprüfung, Werkstoffkunde und Festigkeitslehre (IMWF), Universität Stuttgart, Pfaffenwaldring 32, D-70569 Stuttgart, Germany
$^{2}$ Materialprüfungsanstalt (MPA) Universität Stuttgart, Pfaffenwaldring 32, D-70569 Stuttgart, Germany

E-mail: christopher.kohler@mpa.uni-stuttgart.de

Received 19 August 2004, in final form 20 October 2004
Published 18 November 2004
Online at stacks.iop.org/MSMSE/13/35

## Abstract
Classical molecular dynamics simulations of the interaction of edge dislocations with precipitates in $\alpha$-iron are performed. The critical resolved shear stress (CRSS) is determined for various morphologies of precipitates: pure copper and nickel precipitates, ordered and unordered copper/nickel precipitates, copper and nickel precipitates with substitutional iron atoms, copper precipitates of ellipsoidal shape, and copper precipitates with nickel shells. The dependence of the CRSS on the nature of the precipitate is explained by considering the Burgers vector distribution within the precipitates. It is shown that, except for the ordered precipitates, chemical inhomogeneities of the precipitates lower the CRSS with respect to the precipitates consisting of the pure phases.

## 1. Introduction
Precipitation hardening is an important issue in real materials, ranging from the classical case of steels containing precipitates due to thermal loading or irradiation, covering design in novel technical alloys of Al or Cu and including Ni-base superalloys.

To be able to model the mechanical behaviour of such materials, e.g. the strengthening, starting from basic physical principles, would provide a valuable tool for materials science, and help in understanding the changes in yield strength and other properties and tailoring alloys towards desired properties.

Molecular dynamics (MD) simulation is an important method used in the study of the interaction between dislocations and precipitates during plastic deformation. In particular, contrary to continuum methods (see [1] and references therein), MD is also able to describe the pinning behaviour with precipitates of new compositions. However, until now this method has been applied only to a few cases. In the case of spherical bcc Cu precipitates in bcc Fe, the interaction of edge dislocations with precipitates was studied in [2–5].


![](./images/812325064178401281_1.jpg)

Figure 1. Schematic illustration of the simulation cell.

two edge dislocations and a precipitate was considered without external load. In [3] the critical resolved shear stress (CRSS) was determined for various radii and distances of the precipitates. The temperature dependence of the CRSS and the influence of the phase transformation of the precipitates from bcc to fcc was studied in [5]. While in [2,3,5] dislocations with Burgers vector $a_0/2$ $\langle 111 \rangle$, glide plane $\{110\}$, and glide direction $\langle 111 \rangle$ were considered (as in this work), dislocations with glide plane $\{112\}$ were used to study pinning effects in [4].

The scope of this paper differs from those of the previous investigations in that we concentrate on the influence of the geometry and the chemical composition of the precipitates on the CRSS. In particular, in addition to Cu precipitates we study the effect of the inclusion of Ni and substitutional Fe atoms.

This paper is organized as follows. In section 2 we describe the simulation method and the detection of the dislocations. In section 3 we present the simulation results. Finally, in section 4 we give a summary and a discussion of the results.

## 2. Simulation method

In this paper, classical MD simulations are employed to investigate the dynamics of dislocations. In order to model the interatomic interactions of Fe, Ni and Cu, embedded-atom method (EAM) potentials are used [6]. The total energy for this potential form is given by

$$
E_{\mathrm{EAM}}=\sum_{i}\left[F_{i}\left(\bar{\rho}_{i}\right)+\frac{1}{2} \sum_{j \neq i} \phi_{i j}\left(r_{i j}\right)\right]. \tag{1}
$$

Here, $F_i$ is the embedding energy function, which gives the energy of atom $i$ in the background electron density $\bar{\rho}_{i}=\sum_{j \neq i} \rho_{j}\left(r_{i j}\right)$, with the atomic electron density functions $\rho_j$, and $\phi_{i j}$ is the pair interaction energy of atoms $i$ and $j$ while $r_{i j}$ is the distance between atoms $i$ and $j$. For Fe we have used the potential functions given in [7] and for Cu and Ni we have used the functions given in [8]. The functions $\phi_{i j}$ for the Fe-Cu, the Fe-Ni and the Cu-Ni interactions are taken from [9-11].

The starting configuration of the simulations is similar to the one used in [2-5] and is shown schematically in figure 1. The simulation cell consists of a block of bcc Fe atoms containing a precipitate and an edge dislocation. We use a simulation box of fixed size with side lengths $L_x=19.7$ nm, $L_y=9.73$ nm and $L_z=19.7$ nm. The precipitate is generated by substituting Fe atoms by Cu and Ni atoms within a given region.

<table><caption>Table 1. The lattice constant $a_0$, cohesive energy $E_c$, and shear modulus $G$ for Fe, Cu and Ni in the bcc structure and for CuNi in the B2 structure. All values are obtained from the EAM potentials at $T=0$ K.</caption>
<thead>
<tr>
<th></th>
<th>Fe</th>
<th>Cu</th>
<th>Ni</th>
<th>CuNi</th>
</tr>
</thead>
<tbody>
<tr>
<td>$a_0$ (Å)</td>
<td>2.867</td>
<td>2.881</td>
<td>2.812</td>
<td>2.872</td>
</tr>
<tr>
<td>$E_c$ (eV)</td>
<td>4.280</td>
<td>3.494</td>
<td>4.372</td>
<td>3.963</td>
</tr>
<tr>
<td>$G$ (GPa)</td>
<td>69.760</td>
<td>21.842</td>
<td>24.110</td>
<td>28.822</td>
</tr>
</tbody>
</table>

![](./images/812325064178401281_2.jpg)

Figure 2. (a) Shear modulus and (b) lattice constant in the equatorial plane of a spherical bcc Cu precipitate of radius 1.25 nm in $\alpha$-Fe. The greyscales are linear.

In this paper, coherent precipitates are considered; that is, the atoms of the precipitates are located at the lattice sites of the bcc structure. While $\alpha$-Fe crystallizes in the bcc structure, the bcc phases of Cu and Ni are unstable. The bcc structure of Cu and Ni precipitates, however, is stabilized by the surrounding $\alpha$-Fe matrix in the case of small precipitates as investigated here. Table 1 provides the lattice constant, the shear modulus, and the cohesive energy for pure bcc Fe, Cu and Ni, as well as for B2 CuNi obtained from the EAM potentials. Note that as far as the lattice constants and the cohesive energies are concerned, the values of Fe lie in between the ones for Cu and Ni. Note also that the shear modulus of Cu and Ni are nearly equal but well below the one for Fe.

The local shear modulus (obtained from the second derivatives of the energy function (1) with respect to the atom positions) and the local lattice constant (obtained from averages of nearest neighbour distances) of the relaxed structure of a Cu precipitate in Fe is given in figure 2, where a slice through the equatorial plane of the precipitate is shown. It can be seen that both distributions are inhomogeneous and anisotropic. The ideal values of the shear modulus and the lattice constant for bcc Cu are mainly found at the boundary of the precipitate. Within the precipitate, the shear modulus and the lattice constant are different from the values of ideal bcc Cu. This can be explained by the presence of small displacements of the atoms in the precipitate away from the bcc structure, which can be considered as the onset of a structure modification to a close packed fcc structure.

A dislocation in the starting configuration of the model in figure 1 is generated by removing three (111) lattice half planes corresponding to a Burgers vector of magnitude $b=a_0/2\langle 111\rangle$ and deforming a part of the block of atoms in such a way that the crystal closes up. The atom positions are then rescaled in the $x$ direction by $1-\alpha b/2L_x$, where $\alpha=0.95$ has been adjusted in order to minimize the stress in the $x$ direction.

Periodic boundary conditions are applied in the $x$ and $z$ directions. Thus, the configuration consists effectively of an infinite number of parallel infinitely long dislocations interacting with

![](./images/812325064178401281_3.jpg)

**Figure 3.** Detection of dislocations: (a) atoms in the $(11\overline{2})$ plane in $\alpha$-Fe with an edge dislocation;
the glide plane is shown as a dashed line, (b) disregistry along the glide plane, (c) BVD,
(d) visualization of the BVD in the glide plane; the white colour depicts high values of the BVD.

infinite rows of precipitates, where the distance of the precipitates equals the length $L_z$ of the
simulation box in the $z$ direction. In the $y$ direction, four layers of atoms at the boundaries
(shaded regions in figure 1) are constrained to move only in the $x$ and $z$ directions during the
simulations.

In this paper, only glide planes cutting the centre of the precipitate are considered.
The effect of different glide plane heights will be discussed in a separate paper.

In order to apply an external shear stress, forces are applied at the upper and lower surfaces
in the $-x$ and $+x$ directions to the atoms of the constrained boundary layers in such a way that
an external shear stress $\sigma_{xy}$ results. The simulations are performed at a constant temperature of
300 K using a Nosé–Hoover thermostat [12] with a timestep of 0.5 fs. The finite temperature
means that an activation energy for dislocation motion due to the vibration of atoms is included
in the simulations.

The dislocation line is detected by using a geometrical algorithm described in [13]: for
each $(11\overline{2})$ lattice plane in the $z$ direction (see figure 3(a)) we determine the disregistry of
the atoms, that is, the relative displacement across the glide plane. After interpolation of
the displacements, the derivative of this function is computed resulting in the Burgers vector
distribution (BVD). Figures 3(b) and (c) show the smoothed disregistry and BVD for the
edge dislocation in $\alpha$-Fe shown in figure 3(a). The corresponding atomic configuration has

![](./images/812325064178401281_4.jpg)

Figure 4. Critical resolved shear stress $\tau_c$ for Cu, Ni and ordered CuNi precipitates of different radii as well as for a random CuNi precipitate and a void of radius 1.25 nm.

been obtained by equilibrating a start configuration similar to the one described above for a temperature of 300 K and averaging the atom trajectories for a time of 1 ps in order to remove temperature fluctuations accompanying the atomic movements. Figure 3(d) shows the BVD for all $(11\overline{2})$ planes of the configuration, that is, for the complete glide plane. This means that this representation of the BVD is useful to determine the position of the dislocation within a precipitate if the BVD has several maxima.

The CRSS of the interaction between a dislocation and a precipitate is determined in the following way. In a first simulation, a small external shear stress is applied such that the dislocation attains a stable equilibrium state within the precipitate. Then, in a series of simulations, the external shear stress is increased stepwise until the dislocation detaches from the precipitate. For a given external shear stress, the sample is equilibrated for about 20 ps. The stress increments were chosen to be smaller for stresses close to the CRSS with a final shear stress increment of 8 MPa, which determines the accuracy of the CRSS. The final strain rate is about $10^7\ \text{s}^{-1}$. The typical time to reach the CRSS was about 100 ps. By applying this quasi-static method, the CRSS of the system is determined while inertial and drag effects are not included.

## 3. Simulation results

### 3.1. Variation of precipitate size

The influence of the size of the precipitates on the CRSS has been investigated by choosing spherical precipitates of different radii. In the starting configuration, Fe atoms within a given radius are substituted by Cu or Ni atoms. Three types of precipitates with different radii are considered here: bcc Cu and Ni precipitates, as well as ordered CuNi precipitates possessing a B2 structure (o-Cu$_{50}$Ni$_{50}$). The values of the CRSS for these precipitates are plotted in figure 4. In all cases, the CRSS increases with increasing precipitate radius. However, in the case of the Cu precipitate, the CRSS increases nearly linearly in the range of radii considered, while for the Ni precipitate a strong increase in the range between 1 and 1.25 nm can be observed. For the ordered CuNi precipitates, the CRSSs are found to be higher than for the cases of pure

![](./images/812325064178401281_5.jpg)

Figure 5. BVD within the glide plane just below the CRSS. The displayed area is 6 nm × 7.5 nm.
The location of the precipitate is indicated by a white circle.

Cu and Ni precipitates. This is to be expected since the cutting of the ordered precipitates creates antiphase boundaries possessing an additional energy. However, we find that for small radii, $r = 0.5$ nm, and for large radii, $r = 1.5$ nm, the values for Cu and Ni precipitates are acquired, respectively. For the radius 1.25 nm, we have also studied the CRSS of a precipitate consisting of a random distribution of an equal number of Cu and Ni atoms on the bcc lattice sites (r-Cu₅₀Ni₅₀). In this case, the CRSS is smaller than in the case of pure Cu, pure Ni and ordered CuNi precipitates. The CRSS for a void of radius $r = 1.25$ nm is also given in figure 4. The void has a larger CRSS than the Cu and Ni precipitate, which is consistent with the results of [3]. Note that the void possesses nearly the same CRSS as the ordered CuNi precipitate.

In order to understand the different behaviours of the CRSS of Cu and Ni precipitates for different radii, it is instructive to consider the BVD within the glide plane for the critical loading situation, that is, for an applied shear stress just below the CRSS. For precipitates of radii $r = 1$ and 1.25 nm, the visualization of the BVDs at this load is shown in figure 5. It can be seen that, first, the dislocations are mainly located at the boundaries of the precipitates, that is, at the Fe/precipitate interface and, secondly, that the dislocation lines are not continuously distributed within the precipitates; their location may jump for different $(11\bar{2})$ planes from the left to the right Fe/Cu phase boundary. A measure of the bowing out of the dislocation lines between the precipitates, and correspondingly a measure of the CRSS, is the critical opening angle of the dislocation lines, that is, the angle between the dislocation segments close to the precipitate.

![](./images/812325064178401281_6.jpg)

Figure 6. Critical resolved shear stress $\tau_{c}$ for ellipsoidal Cu precipitates and a cylindrical precipitate, all with circular cross section of diameter 2.5 nm.

Considering the Cu precipitates in figures 5(a) and (d), it is seen that the dislocations are predominantly located at the right boundary of the precipitate, while in some planes there are sections of the dislocations also remaining at the left boundary. This situation does not change significantly with the size of the precipitates. For Ni precipitates, the BVD is different: for the precipitate with radius $r=1.25$ nm, the dislocation is located at the left phase boundary while for the precipitate of radius $r=1$ nm its location has moved to the right boundary. Since a dislocation located at the left side phase boundary of the precipitate has a smaller opening angle, which means a higher CRSS, the different positions of the dislocations at the Ni precipitates explains the difference in the CRSS between the precipitates with radii $r=1.25$ and 1 nm. For the ordered CuNi precipitates the location of the dislocation within the precipitates is not as sharp as in the case of Cu and Ni. However, the BVD is significantly higher at the left boundary for both radii resulting in a high CRSS in both cases.

### 3.2. Variation of precipitate shape

We have also investigated the influence of the shape of the precipitates on the CRSS in the case of Cu precipitates. For these simulations, we have chosen the precipitates to be ellipsoids with the half axes in the $[1\overline{1}0]$ direction and perpendicular to the $(1\overline{1}0)$ glide plane being varied. Within the glide plane, the cut through the precipitate is always given as a disc with radius 1.25 nm. The half axis of the precipitate perpendicular to the glide plane has been varied from 0.25 nm (corresponding to a double layer of atoms, which is cut by the dislocation between these atom layers) to 2 nm (corresponding to a prolate ellipsoid). The extreme case of a long cylinder with the same radius of 1.25 nm has also been considered. The resulting CRSSs are plotted in figure 6. For small values of the varying half axis, the CRSS attains a value of about 130 MPa while for large half axes of the ellipsoidal Cu precipitates, the CRSS of the cylinder (248 MPa) is almost attained. Within the considered range, the CRSS increases nearly linearly with increasing half axis of the ellipsoidal Cu precipitates. The small deviations from linearity can be attributed to deviations of the shapes of the precipitate atom clusters from ideal ellipsoids. It can be seen that the overall variation of the CRSS with changing shape and invariant circular cut surface amounts to 100 MPa.

![](./images/812325064178401281_7.jpg)

Figure 7. Critical resolved shear stress $\tau_c$ for Cu and Ni precipitates with Fe atoms of different concentrations.

### 3.3. Variation of Fe concentration

Real precipitates do not consist of pure Cu or Ni but also contain a certain amount of Fe atoms [14]. In order to determine the effect of substitutional Fe atoms in Cu and Ni precipitates, we have simulated precipitates with different concentrations of Fe atoms in Cu and Ni precipitates of radius $r = 1.25$ nm (corresponding to 700 precipitate atoms). The Fe atoms are substituted randomly with a prescribed probability to meet different Fe concentrations. The CRSS for Cu and Ni precipitates containing 0–100% Fe atoms is depicted in figure 7. It can be seen that the behaviour of Cu and Ni precipitates with Fe atoms is quite different. In the case of Cu precipitates, the decrease of the CRSS with increasing Fe concentration is small for low Fe concentration. However, for Ni precipitates, even a small number of Fe atoms results in a large decrease in the CRSS.

This can again be understood by considering the BVD in the critical loading state just below the stress where the dislocation detaches from the precipitate. Figure 8 shows the BVD for the case of 25% Fe atoms. In the case of the $\text{Fe}_{25}\text{Cu}_{75}$ precipitate, the dislocation is located mainly at the right phase boundary and within the right half of the precipitate. In some planes, dislocation fragments located at the left boundary of the Cu precipitate in figure 5(a) have moved inside the precipitate or to the right phase boundary. In the case of the Ni precipitate, the situation is different. While the dislocation is located mostly at the left phase boundary of the Ni precipitate (figure 5(b)), the dislocation has penetrated the $\text{Fe}_{25}\text{Ni}_{75}$ precipitate and detaches from the right-hand phase boundary (figure 8(b)). The dislocation is thus concentrated completely close to the right phase boundary, which means a high opening angle and a small CRSS.

### 3.4. Shell structure of precipitates

There is experimental [14, 15] evidence, that in Fe alloys containing Cu and Ni, precipitates possess a Cu core with an outer Ni shell. In order to study the influence of the thickness of the Ni shell on the CRSS, we have simulated a series of precipitates with Ni shells ranging from thickness zero (pure Cu precipitate) to maximum thickness (pure Ni precipitate), where the total radius of the precipitates is chosen to be $r = 1.25$ nm. The CRSS for these precipitates is shown in figure 9.

![](./images/812325064178401281_8.jpg)

Figure 8. BVD within the glide plane for (a) the $Fe_{25}Cu_{75}$ and (b) the $Fe_{25}Ni_{75}$ precipitate. Both precipitates have a radius of 1.25 nm.

![](./images/812325064178401281_9.jpg)

Figure 9. Critical resolved shear stress $\tau_{c}$ for Cu precipitates with a Ni shell as a function of the radius of the Cu core. The radius of the precipitates is chosen to be $r=1.25$ nm.

It can be seen that the CRSS is generally much lower than the values obtained by linear interpolation between the CRSSs of the Cu and Ni precipitates. Thus, the shell structure leads to a decrease in the CRSS. However, there exists an intermediate maximum of the CRSS for a Cu core radius of $r=0.6$ nm.

This behaviour of the CRSS can be understood by considering the BVD in the critical state. Figure 10 shows the BVD for selected radii of the inner Cu core. In the case of no inner Cu core (that is, a pure Ni precipitate) the BVD is shown in figure 5(b). The dislocation for this configuration is located mainly at the left phase boundary of the precipitate. For a small inner Cu core, it can be seen in figure 10(a) that the stable position of the dislocation is now mostly located at the right phase boundary of the precipitate with only few planes with dislocation fragments at the left phase boundary. This means a high opening angle of the dislocation with an ensuing low CRSS. For the Cu core radius $r=0.6$ nm, it can be seen from figure 10(b) that the situation has changed drastically. The stable position of the dislocation is now at the left phase boundary of the Cu core yielding a small opening angle with an accompanying higher CRSS. For the slightly higher core radius of $r=0.65$ nm, however,

![](./images/812325064178401281_10.jpg)

Figure 10. BVD within the glide plane for four different radii of the Cu core of the Cu/Ni precipitates. The position of the core and the shell are indicated by white circles.

the stable position of the dislocation is again at the right phase boundary of the precipitate (figure 10(c)), which means that the location of the dislocation at the left phase boundary is unstable against increasing the radius of the Cu core. For a core radius of $r=1$ nm, it can be seen from figure 10(d) that the stable position of the dislocation is now at the right phase boundary of the Cu core leading to a smaller opening angle and an increase of the CRSS. If the radius of the Cu core approaches $r=1.25$ nm, corresponding to a pure Cu precipitate, there are more stable positions of dislocations at the left phase boundary (see figure 5(a)) leading to a further increase in the CRSS.

### 4. Conclusions

In this paper, we have presented results of MD simulations of the dislocation-precipitate interaction, where the CRSS for an edge dislocation cutting an infinite row of precipitates with distances $L=19.7$ nm has been determined for various shapes and chemical compositions of precipitates.

Compared to the properties of Cu precipitates, it has been shown that Ni precipitates behave somewhat differently. In particular, the CRSS of Ni precipitates is very sensitive to the presence of Fe or Cu atoms. Generally, the CRSS is lower for chemically inhomogeneous precipitates than for chemically pure precipitates except for the case of ordered precipitates where order hardening gives rise to an increase in the CRSS.

We have also shown here that the precipitate/matrix interface, together with the particle sizes involved, play important roles in the dislocation pinning mechanism in that the pinned dislocation lines are predominantly located in the interface regions. This seems to be a consequence of the tendency of the Cu and Ni precipitates to undergo a structure modification into the fcc structure inside the precipitate while the boundary region can still be considered a bcc structure.

In order to investigate the dislocations, we have considered the BVD in the glide plane, which seems to be a rather powerful method in cases where the dislocation line cannot be clearly located but is spread out over a region.

Aiming towards practical applications of MD simulations in materials science, the critical shear stress as derived from the present simulations can be transformed into the critical flow stress by multiplication by the Schmid factor of approximately 3 [16]. However, it should be kept in mind that the present simulations assume a regular and even distribution of obstacles: in

real steels, the sizes of the precipitates are not identical [17,18], nor are their mutual distances, nor will dislocations typically hit precipitates at the same moment. Attractive forces between dislocations and precipitates can additionally alter the dislocation dynamics. As demonstrated already for non-shearable precipitates [19], also in the present case the disorder among the precipitates can reduce the strengthening effect by 50% and more, as compared to the regular cases with equidistant particles of identical size and shape [20]. Details will be published separately.

## Acknowledgment
This work was supported by the Bundesministerium für Wirtschaft und Arbeit (BMWA) under grant No 1501228.

## References
[1] Nembach E 1997 *Particle Strengthening of Metals and Alloys* (New York: Wiley)
[2] Nedelcu S, Kizler P, Schmauder S and Moldovan N 2000 *Modelling Simul. Mater. Sci. Eng.* **8** 181
[3] Osetsky Y N, Bacon D J and Mohles V 2003 *Phil. Mag.* **83** 3623
[4] Fukuta T, Akahoshi Y and Harada S 2003 *29 MPA-Seminar* 55
[5] Bacon D J and Osetsky Y N 2004 *J. Nucl. Mater.* **329-333** 1233
[6] Daw M S and Baskes M I 1984 *Phys. Rev. B* **29** 6443
[7] Simonelli G, Pasianot R and Savino E J 1993 *Mater. Res. Soc. Proc.* **291** 567
[8] Voter A F 1993 *Los Alamos Unclassified Technical Report* 93-3901, Los Alamos National Laboratory
[9] Ludwig M, Farkas D, Pedraza D and Schmauder S 1998 *Modelling Simul. Mater. Sci. Eng.* **6** 19
[10] Vailhe C and Farkas D 1998 *Mater. Sci. Eng. A* **258** 26
[11] Clinedinst J and Farkas D 1997 *Nanophase and Nanocomposite Materials II. Symp. Mater. Res. Soc.* **457** p 315
[12] Nosé S 1984 *J. Chem. Phys.* **81** 511
[13] Schroll R, Vitek V and Gumbsch P 1998 *Acta Mater.* **46** 903
[14] Miller M K, Pareige P and Burke M G 2000 *Mater. Charact.* **44** 235
[15] Hättestrand M, Nilsson J-O, Stiller K, Liu P and Andersson M 2004 *Acta Mater.* **52** 1023
[16] Kocks U F 1970 *Metall. Trans.* **1** 1121
[17] Binkele P and Schmauder S 2003 *Z. Metallkd.* **94** 858
[18] Schmauder S and Binkele P 2002 *Comput. Mater. Sci.* **24** 42
[19] Mohles V and Fruhstorfer B 2002 *Acta Mater.* **50** 2503
[20] Kizler P, Binkele P, Kohler C and Schmauder S 2004 *Scientific Report* Materialprüfungsanstalt (MPA) Universität Stuttgart, June 2004 (in German)