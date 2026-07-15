# MNDO STUDY ON INFRARED SPECTRA OF SILICATES

Nozomu UCHIDA

Department of Chemistry, Nagaoka University of Technology, Nagaoka 940-21, Japan

Masahiro SHINMEI

Department of Chemistry, Faculty of Education, Mie University, Tsu 514, Japan

Received 1 July 1989
Revised manuscript received 13 March 1990

The semi-empirical molecular orbital method MNDO was applied to the interpretation of the infrared (IR) spectra of silicates. Force constants and transition dipoles were obtained numerically in the course of the calculation. The vibrational frequencies and the normal vibrational modes were calculated from the force constants with the standard GF matrix method. The reliability of MNDO method was tested for the molecules and anions $SiH_{4}$, $SiF_{4}$, $Si(OH)_{4}$, $SiO_{4}^{4-}$, $Si_{2}O_{7}^{6-}$ and $Si_{2}OF_{6}$. Then, the theoretical IR spectra of the clusters, $H_{6}Si_{3}O_{9}$, $H_{8}Si_{3}O_{10}$, $H_{8}Si_{4}O_{12}$, $H_{12}Si_{6}O_{18}$, $H_{18}Si_{8}O_{25}$ and $H_{24}Si_{11}O_{34}$ were calculated and the assignment of the experimental IR spectra of several silicates was discussed.

## 1. Introduction

Vibration spectroscopy is a powerful tool for the investigation of silicate chemistry. Many experimental and theoretical studies on infrared (IR) and Raman spectra for minerals, glasses and liquids of silica and silicates have been performed and their findings were reviewed by Lazarev [1] and McMillan [2]. Nevertheless, some questions in interpretation of the experimental spectra have remained due to the complexity of the silicate structure.

Based on random network models of $SiO_{2}$, $GeO_{2}$ and $BeF_{2}$ glasses, Bell and co-workers [3] calculated the vibration frequency spectra and IR absorption spectra by using a nearest neighbor harmonic force field and a point charge model. To interpret the frequency spectra, they classified the vibrational modes in six types as (i) bond-bending, (ii) bond-stretching and (iii) bond-rocking of bridging oxygen, (iv) the vibration associated with the motion of cation (Si, Ge or Be), (v) stretching of non-bridging oxygen and (vi) bending of non-bridging oxygen. They interpreted that the vibrations at about $400\ \mathrm{cm}^{-1}$ and at about $1050\ \mathrm{cm}^{-1}$ were type (iii) and type (ii) vibrations, respectively. Theoretical Raman and IR spectra were constructed for some silicate anion model clusters by Furukawa and co-workers [4]. They simplified the calculation by treating the stretching and bending force constants between the nearest neighbor atoms and estimated the Raman and IR absorption intensities from the displacement vectors of the atoms in each vibrational mode under some assumptions.

On the other hand, one of the fundamental approaches to the interpretation of IR spectra is the application of the quantum chemical procedure. Gibbs and co-workers estimated the bond lengths, bond angle and force constants of silicates by means of ab initio molecular orbital method [5]. Recently, Hess and co-workers determined the force constants and vibrational frequencies of the molecules $SiF_{4}$ and $H_{4}SiO_{4}$ by ab initio molecular orbital calculation [6].

The purpose of this paper is to obtain a general interpretation of the IR spectra of silicates. We applied the semi-empirical SCF-MO MNDO method [7] to large silicate clusters and derived theoretical IR spectra of silicates. Values of sec-

0022-3093/90/$03.50 © 1990 - Elsevier Science Publishers B.V. (North-Holland)

ond derivatives of the energy, i.e. the force con- stants and the first derivatives of the dipole mo- ment with respect to the geometry of the clusters, were calculated. The vibrational frequencies, nor- mal vibration modes and the relative intensities of absorption were derived from these values. The reliability of the theoretical IR spectra was ex- amined in comparison with the experimental data of small clusters, $SiH_{4}, SiF_{4}, Si(OH)_{4}, SiO_{4}^{4-}$ and Si,O -. Then, the IR spectra of larger clusters, HSi3O, HSi4O12, H12Si6O18, HSi3O10, $H_{18} Si_{8} O_{25}$ and $H_{24} Si_{11} O_{34}$ were calculated and assumed to be models of silicate structure.

## 2. Calculation

### 2.1. Vibrational analysis

When the total energy of a molecule is defined as a function of molecular geometry, the force acting upon the $i$ th coordinate, i.e. the energy gradient $(f_{i})$ and the force constant $(f_{i j})$ in the molecule, are given by
$$f_{i}=\partial E / \partial R_{i},\qquad(1)$$

$$\begin{aligned}
f_{i j} & =\partial f_{i} / \partial R_{j} \\
& =\partial^{2} E / \partial R_{i} \partial R_{j},
\end{aligned}\qquad(2)$$
where $E$ is the total energy, and $R_{i}(i=1,2,...$ ,3N; N the number of atoms) is the nuclear coor- dinate.

If an atom vibrates around the equilibrium position in the molecule according to the Hooke's law, the relation between the force constants and the vibrational frequency is expressed as
$$4 \pi^{2} \nu^{2} a_{i}=\sum_{\substack{j \neq i}}^{3 N} f_{i j}^{\prime} a_{j} \quad(i=1,2, \ldots, 3 N),\qquad(3)$$
where $f_{i j}^{\prime}$ is the mass weighted force constant, $a_{i}$  and $a_{j}$ are the displacements from the equilibrium position of $i$ th and $j$ th coordinates, respectively, and $\nu$ is the vibrational frequency. These linear algebraic equations for $a_{i}(i=1,2,..., 3 N)$ can be treated as a secular equation and the frequen- cies and normal vibration modes of the molecule are obtained by the standard GF formalism [8].

In this paper, the semi-empirical self consistent field molecular orbital (SCF-MO) method MNDO[7] was applied to obtain the optimized geometry and the force constants. The geometries of the clusters were optimized using the Davidon- Fletcher-Powell [9] procedures. Using Cartesian coordinates, the first derivatives of the energy were calculated analytically and the second de- rivatives numerically by finite displacement.Verwoerd [10] pointed out that the MINDO/3[11] program gives more reliable results than MNDO for silicon-containing molecules. How- ever, since adaptable atoms pairs are restricted in the MINDO/3 method from its definition, we used the more flexible method, MNDO.

The intensity of the $i$ th band, $A_{i}$ , which is the integrated absorbance, is given by
$$A_{i}=\frac{1}{x l} \int_{i \text { th band }} \ln \left(I_{0} / I\right) \mathrm{d} \nu,\qquad(4)$$
where $x$ is the sample concentration and $l$ is the path length. In the mechanical and electrical harmonic approximation, $A_{i}$ is written as
$$A_{i}=\frac{N \pi g_{i}}{3 c^{2}}\left|\frac{\partial M}{\partial Q_{i}}\right|^{2},\qquad(5)$$
where $N$ is Avogadro's number, $c$ is the velocity of light in vacuum, $g_{i}$ is the degeneracy of the normal vibration mode $Q_{i}, M$ is the molecular dipole moment and $\partial M / \partial Q_{i}$ is a transition mo ment. Since $N \pi g_{i} / 3 c^{2}$ can be regarded as a con stant, $|\partial M / \partial Q_{i}|^{2}$ is proportional to the relative intensity of the $i$ th band.

The transition moments were obtained from the first derivatives of the molecular dipole mo- ment and the normal vibration mode. The first derivatives of the dipole moment were obtained numerically by using finite displacement in Carte- sian coordinates. A line spectrum and its relative intensity can be drawn from the obtained frequen- cies and transition dipole moment values.

The absolute values of calculated frequencies have some systematic discrepancies from experi- mental ones as discussed in section 3.2. Dewar and co-workers [12] discussed the reliability of this vibrational analysis for molecules which contain H, B, C, N, O, F, S and CI. They showed that the

![](./images/812398954569269249_1.jpg)

Fig. 1. Schematic structures of the clusters used in this work

errors can be reduced by using a simple correction function. In this study, however, our discussion is on the basis of relative position and relative inten- sity of the theoretical spectra.

### 2.2. Clusters
The schematic structures of the clusters used in this work are shown in fig. 1. The parameters of initial geometries were selected based on the ex- perimental values. The geometries were fully opti- mized and then the vibrational analyses were per- formed.

Computations were performed utilizing a HITAC M-680H system and S-810/10 system at Hokkaido University Computer Center. The molecular orbital program package MOPAC ver- sion 3.00 [13] was used for MNDO calculations. Computational time was about 20900 s for the vibrational analysis of $H_{24}Si_{11}O_{34}$.

## 3. Reliability of the method

### 3.1. Geometry
The geometries of $SiH_{4}, SiF_{4}, Si(OH)_{4}, SiO_{4}^{4-}$, $Si_{2}OF_{6}$ and $Si_{2}O_{7}^{6-}$ are summarized in table 1 along with the experimental data. Optimized structures of $SiH_{4}, SiF_{4}$ and $SiO_{4}^{4-}$ have $T_{d}$ sym metry and that of $Si(OH)_{4}$ has $S_{4}$ symmetry. The symmetry group of $Si(OH)_{4}$ differs from $D_{2 d}$ used in the calculation of Hess et al. [6]. No imaginary frequency appeared in the present calculation.

<table><caption>Table 1
Computed geometry parameters of $SiH_{4}, SiF_{4}, Si(OH)_{4}, SiO_{4}^{4-}, Si_{2}OF_{6}$ and $Si_{2}O_{7}^{6-}$ along with experimental data in parentheses</caption>
<tbody>
<tr>
<td>
</td>
<td>
Bond length (Å)
</td>
<td>
</td>
<td>
Bond angle (deg)
</td>
</tr>
<tr>
<td>
$SiH_{4}$
</td>
<td>
Si-H 1.434 (1.48, ref. [14])
</td>
<td>
</td>
<td>
</td>
</tr>
<tr>
<td>
$SiF_{4}$
</td>
<td>
Si-F 1.584 (1.54, ref. [15])
</td>
<td>
</td>
<td>
</td>
</tr>
<tr>
<td>
$Si(OH)_{4}$
</td>
<td>
Si-O 1.654
</td>
<td>
</td>
<td>
Si-O-H 123.9
</td>
</tr>
<tr>
<td>
</td>
<td>
O-H 0.930
</td>
<td>
</td>
<td>
</td>
</tr>
<tr>
<td>
$SiO_{4}^{4-}$
</td>
<td>
Si-O 1.711 (1.62, ref. [16])
</td>
<td>
</td>
<td>
</td>
</tr>
<tr>
<td>
$Si_{2}O_{7}^{6-}$
</td>
<td>
Si-O 1.769 (1.626, ref. [17])
</td>
<td>
twist
</td>
<td>
Si-O-Si 180.0 (133-180, ref. [17])
</td>
</tr>
<tr>
<td>
</td>
<td>
(central)
</td>
<td>
</td>
<td>
60.1
</td>
</tr>
<tr>
<td>
</td>
<td>
Si-O 1.698 (1.626, ref. [17])
</td>
<td>
</td>
<td>
</td>
</tr>
<tr>
<td>
</td>
<td>
(peripheral)
</td>
<td>
</td>
<td>
</td>
</tr>
<tr>
<td>
$Si_{2}OF_{6}$
</td>
<td>
Si-O 1.610 (1.580, ref. [18])
</td>
<td>
</td>
<td>
Si-O-Si 180.0 (155.7, ref. [18])
</td>
</tr>
<tr>
<td>
</td>
<td>
Si-F 1.587 (1.554, ref. [18])
</td>
<td>
twist
</td>
<td>
56.3 (34.6, ref. [18])
</td>
</tr>
</tbody>
</table>

![](./images/812398954569269249_2.jpg)

Fig. 2. Potential curve of Si-O-Si bonding as a function of bond angle in $Si_{2}OF_{6}$.

As a whole, the optimized geometry parameters show good agreement with the experimental val- ues except for Si-O-Si bond angle. The Si-O-Si bond angle becomes $180^{\circ}$ and $D_{3 d}$ symmetry was obtained for $Si_{2}O_{7}^{6-}$ and $Si_{2}OF_{6}$ in this calcula tion and differs from the experimental results.

The calculated potential curve of Si-O-Si bond angle of $Si_{2}OF_{6}$ is shown in fig. 2. The curve has a rather flat bottom and has minimum at $180.0^{\circ}$. Edward and Fowler [19] discussed this problem in detail with respect to MINDO/3, MNDO and some ab initio methods and mentioned that Si- O-Si angle is extremely flexible and that the en- ergy barrier to linearity is very low. Thus, the Si-O-Si linkage is difficult to predict accurately by the MNDO approximation.

### 3.2. Vibrational spectra
The theoretical line spectra of $SiH_{4}, SiF_{4}$, $Si(OH)_{4}, SiO_{4}^{4-}$ and $Si_{2}O_{7}^{6-}$ are shown in fig. 3 along with experimental IR spectra. The experi-

![](./images/812398954569269249_3.jpg)

Fig. 3. Theoretical IR line spectra of small clusters, (a) $SiH_{4}$,
(b) $SiF_{4}$, (c) $Si(OH)_{4}$, (d) $SiO_{4}^{4-}$ and (e) $Si_{2}O_{7}^{6-}$. Experimental
spectra of $SiH_{4}$ (ref. [20], transformed from transmittance to
absorbance), $SiF_{4}$ (present study), $SiO_{4}^{4-}$ (ref. [1], transformed
from transmittance to absorbance) and $Si_{2}O_{7}^{6-}$ (ref. [21]) are
superimposed. Frequencies of IR active vibrations of $SiF_{4}$
(present study) are indicated on the horizontal axis. The unit of
vertical axis is arbitrary.

mental spectra of orthosilicate $(SiO_{4}^{4-})$ and pyrosilicate $(Si_{2}O_{7}^{6-})$ are represented by that of $\gamma$-$CaSiO_{4}$ and rankinite $(CaSi_{2}O_{7})$, respectively.

The tetrahedral clusters $SiH_{4}$, $SiF_{4}$ and $SiO_{4}^{4-}$ have four vibrational frequencies and two of them are IR active. $Si_{2}O_{7}^{6-}$, which should have $C_{2}$ symmetry as shown in table $1(Si-O-Si<180^{\circ})$, showed two degenerate vibrations due to their $D_{3d}$ symmetry $(Si-O-Si=180^{\circ})$.

The force constants of Si-O bondstretching and O-Si-O bond-bending are calculated as follows:
6 mdyn/Å for Si-O bond-stretching in $Si(OH)_{4}$,
7 mdyn/Å for Si-O bond-stretching in $SiO_{4}^{4-}$,
0.4 mdyn/Å for O-Si-O bond-bending in $Si(OH)_{4}$.

Although the force constant of O-Si-O bond-bending has a similar magnitude to that used in previous studies [4,22,23], those of Si-O bond-stretching is rather greater than previous ones. The reason for this difference is thought to be as follows. The MNDO method was designed to reproduce the experimental values of heat of formation, geometric parameters, ionization potential and dipole moment of a ground state molecule by parametrization in which the effect of the electron correlation was counted. However, the effect was not taken into account when the atomic distance was out of equilibrium, so that the shape of the potential curve of bond-stretching was observed to be sharper than the experimental one as observed in the ab initio calculations which use the Hartree-Fock approximation [24]. As a result, the force constants of the bond-stretching become larger. This tendency is also observed in the result of Dewar et al. [12].

## 4. Silicates

### 4.1. $\alpha$- and $\beta$-CaSiO$_{3}$

Theoretical line spectra of $H_{6}Si_{3}O_{9}$ (ring-form structure, fig. 1(g)) and of $H_{8}Si_{3}O_{10}$ (chain-form structure, fig. 1(j)) are shown in fig. 4 along with the experimental spectra (solid line) of $\alpha$-CaSiO$_{3}$ for fig. 4(a) and of $\beta$-CaSiO$_{3}$ for fig. 4(b). The $\alpha$-CaSiO$_{3}$ has a three-membered ring structure and $\beta$-CaSiO$_{3}$ has a chain structure. The specific feature common to the spectra of $H_{6}Si_{3}O_{9}$ and $\alpha$-CaSiO$_{3}$ is the strong absorptions at about 720-750 $cm^{-1}$ in comparison with the spectra of $H_{8}Si_{3}O_{10}$ and $\beta$-CaSiO$_{3}$. The absorption at 725

![](./images/812398954569269249_4.jpg)

Fig. 4. Theoretical IR spectra of (a) $H_{6}Si_{3}O_{9}$ (b) $H_{8}Si_{3}O_{10}$; experimentally obtained spectra (present study) of $\alpha$- and $\beta$-CaSiO₃ are superimposed.

$\mathrm{cm}^{-1}$ in the spectrum of $\alpha$-CaSiO₃ has been assigned to the vibration associated with the endocyclic Si-O-Si stretching. On the other hand, the normal vibrational modes of the strong absorptions at 748.2 and $749.9\ \mathrm{cm}^{-1}$ in the theoretical spectra are shown in fig. 5, where the ring vibration within the ring plane is clearly shown.

The vibrations associated with the ring form structure are also found in the theoretical spectrum of cyclic $H_{8}Si_{4}O_{12}$ (fig. 6(a)). However, their relative intensities are weaker than that of three-membered ring structure of $\mathrm{SiO}_{4}$, $H_{6}Si_{3}O_{9}$, and the frequencies shift toward low wave numbers. In the case of cyclic $H_{12}Si_{6}O_{18}$, no vibration associated with the ring form structure appeared (fig. 6(b)) and the profile almost converged to that of $H_{8}Si_{3}O_{10}$ having the chain structure (fig. 4(b)).

![](./images/812398954569269249_5.jpg)

Fig. 5. Vibrational modes associated with the ring structure at (a) 748.2 and (b) $749.9\ \mathrm{cm}^{-1}$.

![](./images/812398954569269249_6.jpg)

Fig. 6. Theoretical IR spectra of (a) $H_{8}Si_{4}O_{12}$ and (b) $H_{12}Si_{6}O_{18}$. $\circ$, the vibration associated with the ring structure.

### 4.2. Silica glass

Theoretical spectra of $H_{18}Si_{8}O_{25}$ (fig. 1(k)) and $H_{24}Si_{11}O_{34}$ (fig. 1(l)) is shown in fig. 7 along with the experimental spectrum of silica glass. The bond angles of $\mathrm{Si}^{2}-\mathrm{O}^{3}-\mathrm{Si}^{6}$ and $\mathrm{Si}^{6}-\mathrm{O}^{7}-\mathrm{Si}^{10}$ become

![](./images/812398954569269249_7.jpg)

Fig. 7. Theoretical IR spectra of $H_{18}Si_{8}O_{25}$ and $H_{24}Si_{11}O_{34}$ with experimentally obtained spectrum of silica glass.

168.7 and $175.4^{\circ}$, respectively, in the optimized structure of $\mathrm{H}_{24} \mathrm{Si}_{11} \mathrm{O}_{34}$.

We regard these clusters as models of silica glass since they contain $\mathrm{SiO}_{4}$ units which are surrounded by four $\mathrm{SiO}_{4}$ units, and have no rigid periodicity. Here, we roughly classified the $\mathrm{SiO}_{4}$ units in the silica glass or these two clusters as follows: the $\mathrm{SiO}_{4}$ unit having $\mathrm{OH}$ groups is a surface one and the unit surrounded by four $\mathrm{SiO}_{4}$ units is a bulk one. Following this classification, we assume that the $\mathrm{SiO}_{4}$ units of $\mathrm{Si}^{2}$ and $\mathrm{Si}^{6}$ in $\mathrm{H}_{18} \mathrm{Si}_{8} \mathrm{O}_{25}$ and $\mathrm{Si}^{2}, \mathrm{Si}^{6}$ and $\mathrm{Si}^{10}$ in $\mathrm{H}_{24} \mathrm{Si}_{11} \mathrm{O}_{34}$ are the bulk ones and others are surface ones. Especially, the unit of $\mathrm{Si}^{6}$ in $\mathrm{H}_{24} \mathrm{Si}_{11} \mathrm{O}_{34}$ is connected to two bulk $\mathrm{SiO}_{4}$ units, so it represents a deeper bulk $\mathrm{SiO}_{4}$ unit than other bulk units.

Both theoretical spectra are composed of three strong absorptions in the high wave number range and three medium ones in the low wave number range. All of these absorptions are associated with the vibration of the bulk $\mathrm{SiO}_{4}$ units described above, i.e. $\mathrm{Si}^{2}$ and $\mathrm{Si}^{6}$ in $\mathrm{H}_{18} \mathrm{Si}_{8} \mathrm{O}_{25}$ and $\mathrm{Si}^{2}, \mathrm{Si}^{6}$ and $\mathrm{Si}^{10}$ in $\mathrm{H}_{24} \mathrm{Si}_{11} \mathrm{O}_{34}$. The clusters are large enough to represent the $\mathrm{SiO}_{2}$ glass system, since two theoretical spectra are almost identical in profile and the contribution of the unit of $\mathrm{Si}^{6}$ to vibrational modes in $\mathrm{H}_{24} \mathrm{Si}_{11} \mathrm{O}_{34}$ is comparable to other bulk ones.

The modes of the three vibrations in the low wave number range consists of the deformation vibrations and those in the high wave number range consist of the stretching ones. Bell et al. [3(a)] interpreted these vibrations on the basis of the motion of bridging oxygen. However, we tried to interpret them in detail in view of the vibration of tetrahedral $\mathrm{SiO}_{4}$ unit. Examples of the vibrational modes of $\mathrm{SiO}_{4}$ units are shown in fig 8. They can be assigned to the slightly deformed $\mathrm{F}_{2}$ vibrations of deformation and of stretching of $\mathrm{T}_{\mathrm{d}}$ symmetry. Actually, the profiles of the spectra in fig. 7 suggest an analogy with the IR spectrum of a molecule having $\mathrm{T}_{\mathrm{d}}$ symmetry. The basic profile of IR spectrum of silica glass is considered to be governed by the local $\mathrm{T}_{\mathrm{d}}$ symmetry of the most primitive structural unit $\mathrm{SiO}_{4}$, in spite of the random network structure of the glass.

![](./images/812398954569269249_8.jpg)

Fig. 8. Examples of vibrational modes of $\mathrm{SiO}_{4}$ units of $\mathrm{Si}^{2}, \mathrm{Si}^{6}$ and $\mathrm{Si}^{10}$ of the cluster shown in fig. 1(l).

In fig. 7(b), three medium absorptions of the theoretical spectrum in the low wave number range agree well with the experimental absorption band while three strong ones in the high wave number range are shifted to high wave number relative to the experimental absorption band. This shift is due to force constants of $\mathrm{Si}-\mathrm{O}$ stretching calculated by MNDO method being slightly greater than those in earlier works, as described in section 3.2.

On the basis of the above interpretation, the vibrational frequencies of IR active absorptions are governed by the $\mathrm{Si}-\mathrm{O}$ stretching and $\mathrm{O}-\mathrm{Si}-\mathrm{O}$ bending; thus, the effect of the error in representing the $\mathrm{Si}-\mathrm{O}-\mathrm{Si}$ linkage in this analysis is thought to be negligible.

The absorption in the middle wave number range in the theoretical spectrum of $\mathrm{SiO}_{2}$ calculated by Furukawa et al. [4] did not appear in this study. This difference is considered to be due to the difference of the method of estimating the absorption intensity.

According to the above classification, all $\mathrm{SiO}_{4}$ units in the smaller clusters $\mathrm{Si}(\mathrm{OH})_{4}$ and $\mathrm{H}_{8} \mathrm{Si}_{3} \mathrm{O}_{10}$ are the surface ones. In the theoretical spectrum of $\mathrm{Si}(\mathrm{OH})_{4}$ (fig. 3(c)), there are three absorptions associated with the deformation vibration of $\mathrm{SiO}_{4}$ unit at 329.3, 329.4 and $367.2 \mathrm{~cm}^{-1}$; however, the three medium absorptions at 884.7, 884.8 and $895.4 \mathrm{~cm}^{-1}$ are associated with the motion of $\mathrm{OH}$ groups and the absorptions associated with the stretching vibration of the $\mathrm{SiO}_{4}$ unit (1067.3, 1088.9 and $1089.1 \mathrm{~cm}^{-1}$ ) are rather weak. On the other hand, although there are only two strong absorptions in the high wave number range (1282.6 and $1306.2 \mathrm{~cm}^{-1}$ ) in the theoretical spectrum of $\mathrm{H}_{8} \mathrm{Si}_{3} \mathrm{O}_{10}$ (fig. 4(b)), the profile is similar to that of $\mathrm{H}_{24} \mathrm{Si}_{11} \mathrm{O}_{34}$.

It seems that the spectrum patterns calculated for increasing cluster size are converging to that of

$H_{24}Si_{11}O_{34}$ and the presence of $SiO_4$ units surrounded by four $SiO_4$ units is necessary to represent the spectrum of $SiO_2$ glass.

## 5. Summary
(1) The calculated geometries of molecules containing Si by the MNDO method is in fairly good agreement with the experimentally observed geometries except for the bond angle of Si-O-Si linkage. As has already been pointed out, the Si-O-Si angle, calculated by MNDO, is $\sim 180^\circ$.

(2) Theoretical vibrational spectra for small molecules containing Si were compared with the experimentally obtained ones. The absolute values of the theoretically obtained frequencies contained some systematic errors. However, the relative relations among frequencies and intensities are useful for theoretical interpretation of observed IR spectra.

(3) The characteristic IR absorption of $\alpha$- $CaSiO_3$ at about $720\ cm^{-1}$ is assigned to the vibration associated with the three-membered ring of $SiO_4$ units. The intensity of the absorption caused by ring structure decreases with an increase of the number of ring members.

(4) The IR absorption spectrum of silica glass was found to reflect the local $T_d$ symmetry of $SiO_4$ units.

This work was supported by a Grant-in-Aid (no. 6260452) for Scientific Research in Priority Areas, New Functionality Materials-Design, Preparation and Control, by the Ministry of Education, Science and Culture, Japan. Further, the authors wish to express their gratitude to Dr. J.J.P. Stewart of USAF Academy and professors T. Yokokawa and T. Maekawa of Hokkaido University for their helpful suggestions regarding the interpretation of the output of force calculations. Finally, the authors would like to thank Prof. S. Sakka for his kind advice to complete this manuscript.

## References
[1] A.N. Lazarev, Vibrational Spectra and Structure of Silicates (Consultants Bureau, New York, London, 1972).
[2] P. McMillan, Am. Mineral. 69 (1984) 622.
[3] (a) R.J. Bell, P. Dean and D.C. Hibbins-Butler, J. Phys. C 4 (1971) 1215;
(b) R.J. Bell and D.C. Hibbins-Butler, J. Phys. C 9 (1976) 1171.
[4] T. Furukawa, K.E. Fox and W.B. White, J. Chem. Phys. 75 (1981) 3226.
[5] G.V. Gibbs, Am. Mineral. 67 (1982) 421.
[6] A.C. Hess, P.F. McMillan and M. O'Keefe, J. Chem. Phys. 90 (1986) 5661.
[7] M.J.S. Dewar and W. Thiel, J. Am. Chem. Soc. 99 (1977) 4899;
M.J.S. Dewar, M.L. McKee and H.S. Rzepa, J. Am. Chem. Soc. 100 (1978) 3607;
M.J.S. Dewar, E.F. Healy, J.J.P. Stewart, J.E. Friendheim and G.L. Grady, Organometallics 5 (1986) 375.
[8] (a) E.B. Willson, J.C. Decius and P.C. Cross, Molecular Vibrations (McGraw-Hill, New York, 1955);
(b) J.J.P. Stewart, S.R. Bosco and W.R. Carper, Spectrochim. Acta A42 (1986) 13.
[9] R. Fletcher and M.J.D. Powell, Comput. J. 6 (1963) 163;
W.C. Davidon, Comput. J. 10 (1968) 406.
[10] W.S. Verwoerd, J. Comput. Chem. 3 (1982) 445.
[11] R.C. Bingham, M.J.S. Dewar and D.H. Lo, J. Am. Chem. Soc. 97 (1975) 1285.
[12] M.J.S. Dewar, G.P. Ford, M.L. McKee, H.S. Rzepa, W. Thiel and Y. Yamaguchi, J. Mol. Struct. 43 (1978) 135.
[13] J.J.P. Stewart, private communication.
[14] G.R. Wilkinson and M.K. Wilson, J. Chem. Phys. 44 (1966) 3867.
[15] L. Pauling, The Nature of the Chemical bonds (Cornell Univ. Press, 1966)).
[16] W.G. Wyckoff and S.B. Hendricks, Z. Kristallogr. 66 (1927) 73;
C.M. Midgley, Acta Crystallogr. 5 (1952) 307;
I.R. Krstanovic, Acta Crystallogr. 11 (1958) 896;
D.W. Cruickshank, Acta Crystallogr. 17 (1964) 685;
D.K. Smith, A. Majumdar and F. Ordway, Acta Crystallogr. 18 (1965) 787;
D.J. Segal, R.P. Santoro and R.E. Newnham, Z. Kristallogr. 123 (1966) 73.
[17] W.H. Zachariasen, Z. Kristallogr. 73 (1930) 1;
T. Ito and J. West, Z. Kristallogr. 83 (1932) 1;
J.B. Smith, Acta Crystallogr. 6 (1953) 9;
G. Johansson, Acta Crystallogr. 12 (1959) 522;
G.A. Barclay and E.G. Cox, Z. Kristallogr. 113 (1960) 23;
A. Pabst, Z. Kristallogr. 115 (1961) 307;
O. Gabrielson, Arkiv Mineral. Geol. 3 (1963) 141.
[18] W. Airey, C. Glidewell, D.W.H. Rankin, A.G. Robietti, G.M. Sheldrick and W.J. Cruickshank, Trans. Faraday Soc. 66 (1970) 551.

[19] A.H. Edwards and W.B. Fowler, J. Phys. Chem. Soc. 46 (1985) 841.

[20] W.B. Steward and H.H. Nielsen, Phys. Rev. 47 (1935) 828.

[21] J. Heicklen and V. Knight, Spectrochim. Acta 20 (1964) 295.

[22] B.D. Saksena, Trans. Faraday Soc. 57 (1961) 242.

[23] S. Brawer, Phys. Rev. B11 (1975) 3731.

[24] (a) R.G. Body, D.S. McClure and E. Clementi, J. Chem. Phys. 49 (1968) 4916;
(b) W. Meyer and P. Pulay, J. Chem. Phys. 56 (1972) 2109.