# Crossover between tetrahedral and hexagonal structures in liquid water

Osvaldo Chara $^{1}$, Andrés N. McCarthy $^{*,2}$, J. Raúl Grigera

Instituto de Física de Líquidos y Sistemas Biológicos (IFLYSIB), CONICET - Universidad Nacional de La Plata, Argentina

---

## ARTICLE INFO

**Article history:**
Received 18 July 2010
Received in revised form 24 November 2010
Accepted 25 November 2010
Available online 30 November 2010
Communicated by C.R. Doering

**Keywords:**
Water structure
Two-state model
Water radial distribution function
components

---

## ABSTRACT

It is widely accepted that liquid water structure is comprised of two closely interweaved components; i.e. tetrahedral (low density) and hexagonal (high density) structures. The relative amount of these components is temperature and pressure dependent. We propose an order parameter, based on the radial distribution function, that quantifies the relative structural composition at any defined temperature and pressure, thus establishing the crossover point in structural dominance. At 300 K this point lies close to 2 kbar, pressure at which water looses most of its 'anomalous' properties.

© 2010 Elsevier B.V. All rights reserved.

---

## 1. Introduction

The peculiar physical properties of water have for very long been recognized, being these particularities associated in general terms with its unique structure. From the seminal work of Bernal and Fowler [1] many suggestions on the structure of water and its behavior have been proposed [2].

Hall [3], based on ultrasonic experiments, supported the interpretation given by Bernal and Fowler of a two-state model, according to which low and high density structures are closely interweaved in water. Four decades later, further support for this model was given [4–7]. Subsequent studies have reinforced this concept, showing also its role on the phase transition of water [8].

Changes in temperature and pressure modify the properties of water. This can be interpreted as a consequence of changes in the ratio between high and low density structures, induced by the changes in thermodynamical conditions.

The changes in water properties with temperature and pressure have been extensively shown through various experimental approaches [9–19]. Those results show that the so-called 'anomalies' of water are gradually lost as temperature and pressure increase, moving towards a regime of a simple liquid. These changes establish that a region of intermediate behavior exists, for both increasing temperature and pressure.

Although temperature effects on the behavior of water have been extensively addressed [16–19], studies of the effect of pressure on the dynamical and structural properties of water are much less abundant. Nevertheless, available data appears to be sufficient to establish a pressure transition within the range of 1 to 3 kbar [20,21].

Considering water bulk in terms of the coexistence of two distinct structures (i.e. an open tetrahedral structure and a more compact hexagonal one), this transition may be interpreted in terms of the change in dominance of one structure over the other. Although this perspective has already been addressed, we still lack a robust quantitative parameter to characterize such a transition.

In this work we present the development of an order parameter that defines the crossover between low and high density dominance in liquid water.

We have used this parameter to analyze the radial distribution functions of water under various temperature and pressure conditions, using Argon as a reference for simple liquid behavior. The data analyzed was produced through Molecular Dynamic simulations.

## 2. Methods

We carried out all Molecular Dynamic (MD) simulations using the GROMACS 4.0.4 package [22]. Water molecules were constrained using the SETTLE algorithm [23]. For the calculation of electrostatic forces we applied the Reaction Field method, with a cut-off radius of 1.4 nm, as well as for Lennard-Jones interactions. As starting configurations for water we used several replicas of 216 SPC/E water [24] molecule box equilibrated at 300 K and 1 bar. The system consisted of a cubic simulation box containing

---

* Corresponding author.
E-mail address: amccarthy@iflysib.unlp.edu.ar (A.N. McCarthy).
1 Also at Center for Information Services and High Performance Computing, Dresden University of Technology, 01062 Dresden, Germany.
2 Also at Depto. Cs. Biológicas, Fac. Cs. Exactas, Universidad Nacional de La Plata, Argentina.
0375-9601/$ – see front matter © 2010 Elsevier B.V. All rights reserved.
doi:10.1016/j.physleta.2010.11.061

![](./images/811702141252009984_1.jpg)
![](./images/811702141252009984_2.jpg)

![](./images/811702141252009984_3.jpg)

Fig. 1. Evolution of $g(r)$ with pressure, at ambient temperature, as obtained through molecular dynamic simulations of the SPC/E water model. Inset: $g(r)$ of water at 1 bar (continuous curve), at 10 kbar (dotted curve) and liquid argon (dashed curve). Pressure appears to modify the $g(r)$ of water, resembling that of argon (see text main body).

a total of 1728 water molecules. All replicas were first simulated during 2 ns, allowing for a complete equilibration of every pressure and temperature condition. Production data was collected during a complete nanosecond (1 ns) after equilibration. All replicas were weakly coupled to a thermal and hydrostatic bath, in order to work within the isothermal-isobaric ensemble [25].

## 3. Results and discussion

In order to characterize the changes in water structure with pressure and temperature (and, hence, sensibly explain the experimentally observed changes in behavior), a number of molecular dynamic simulations were performed under various conditions, with pressure and temperature ranging from 1 bar to 10 kbar, and from 93 K to 373 K. Structure was evaluated through the oxygen-oxygen radial distribution function, $g(r)$, which bears the advantage of having been amply studied through X-ray and neutron diffraction [12,17].

Fig. 1 shows the evolution of $g(r)$ with pressure, at ambient temperature, as obtained through molecular dynamic simulations of the SPC/E water model. In general terms, each $g(r)$ peak shows the preferential position of the successive neighboring water coordination spheres.

The classical shape of the $g(r)$ of water at 1 bar may be observed both in the far plane of Fig. 1, and in its inset (black curve), highlighting that the position of the second peak typically reveals the tetrahedric component of the structure of water under these conditions. This contrasts with the position of the second peak of liquid argon $g(r)$, which reveals the presence of a simple (hexagonal) structure (Fig. 1 inset, gray curve). Nevertheless, as pressure increases, the second peak becomes attenuated, finally being replaced by a valley.

Additionally, two further changes may be described: the appearance of a shoulder to the right of the first peak and the closing in of the low pressure third peak, which finally results in the new second peak. Pressure appears to modify the $g(r)$ of water, resembling that of argon (Fig. 1 inset, light gray curve).

In order to transform the above qualitative observations into quantitative structural information we use a two-state model to interpret each obtained $g(r)$. The model expresses the coexistence of two interweaved hydration contributions; i.e. an open tetrahedral structure and a more compact hexagonal one.

Both contributions are treated qualitatively in the same way, taking into explicit account for each contribution the first three hydration spheres, whilst the fourth sphere on is implicitly considered for both structures.

Thus, each hydration contribution is modeled as a first asymmetric distribution representing the first hydration sphere, and two subsequent symmetric distributions representing the second and third hydration spheres.

In both cases, the first hydration sphere is modeled through a Freundlich distribution. For the tetrahedral and hexagonal contributions, the second and third hydration layers are modeled using a Gaussian distribution. Finally, all fourth and subsequent layers are modeled through a sigmoidal function.

The sum of all explicit and implicit coordination contributions is what we call the $G$ function, which may be explicitly defined as:

$$
G(r)=\sum_{j=1}^{2} \sum_{i=2}^{3}\left(f_{1}^{j}(r)+g_{i}^{j}(r)\right)+S(r)
\tag{1}
$$

where $f_{j}^{i}(r)$ stands for the asymmetric Freundlich distribution, $g_{j}^{i}(r)$ stands for the symmetric Gaussian distribution, $S(r)$ stands for the coordination spheres implicitly accounted for, $i$ subscript denotes the coordination sphere order, and $j$ superscript denotes the tetrahedric or hexagonal contribution.

The general explicit form of these functions is:

$$
f_{1}^{j}(z)=a^{j} z^{b^{j}} z^{-c^{j}} \quad \text { with } \begin{cases}z=r & \forall r \geqslant 0 \\ z=r_{0} & \forall r<0\end{cases}
\tag{2}
$$

$$
g_{i}^{j}(r)=\frac{A_{i}^{j}}{\omega_{i}^{j} \sqrt{\pi / 2}} e^{-2 \frac{\left(r-\mu_{i}^{j}\right)^{2}}{\omega_{i}^{j^{2}}}}
\tag{3}
$$

$$
S(r)=\frac{V r^{n}}{K^{n}+r^{n}}
\tag{4}
$$

where $A_{i}^{j}, \omega_{i}^{j}, \mu_{i}^{j}, a^{j}, b^{j}, c^{j}, r_{0}, V, K$ and $n$ are all the parameters involved.

Fig. 2 shows the tetrahedral (black curves) and hexagonal (gray curves) components of the $G$ function. Inset of Fig. 2 shows both the $g(r)$ obtained from simulation (dots) and the complete $G$ function (dash-dot curve).

The correctness of the $G$ function may be ultimately assessed through its ability to rebuild the $g(r)$ provided by molecular dynamic simulations.

The $G$ function was fitted to the $g(r)$ data obtained for water at every temperature and pressure conditions simulated (for details of the fitting algorithm see supplementary material). The same fitting procedure was applied to the $g(r)$ data calculated for liquid Argon.

For every simulated condition the fitting procedure converged successfully, exemplified by Fig. 2 inset.

The proposed model was thus validated, and consequently allows for its use in the quantification of the two coexisting structures, enabling the study of changes induced by pressure and temperature upon the relative contribution of these structures.

To quantify these structure changes in fluid, an order parameter is naturally desirable. Many parameters have consequently been proposed, the more relevant of which may be briefly summarized as follows:

The translational order parameter $t$, proposed by Truskett et al. [26], measures the tendency of pairs of molecules to adopt preferential separations, vanishing for an ideal gas, and adopting large

![](./images/811702141252009984_4.jpg)

Fig. 2. Complete G function and its components. The G function (dash-dot black curve) fitted to the g(r) calculated from MD data of SPC/E water model. Tetrahedral structural contributions are represented by $f_{1}^{t}$ (first coordination sphere, dotted black curve), $g_{2}^{t}$ (second coordination sphere, continuous black curve) and $g_{3}^{t}$ (third coordination sphere, dashed black curve). Hexagonal structural contributions are represented by $f_{1}^{h}$ (first coordination sphere, dotted grey curve), $g_{2}^{h}$ (second coordination sphere, continuous grey curve) and $g_{3}^{h}$ (third coordination sphere, dashed grey curve). S represents the fourth sphere on, for both structural contributions (continuous light gray curve). Inset: g(r) obtained from MD simulation (dots) and the G function (dash-dot curve).

values for a crystal. This parameter gives an idea of structure in a general sense. Nevertheless, in order to discriminate the nature of the structure, the use of other parameters is required.

Steinhardt et al. [27] defined the Q3 parameter whilst Naberukhin et al. [28,29] proposed the use of T parameter, both being capable of testing tetrahedrality.

As discussed by Chau and Hardwick (1998) [30], Q3 suffers from two drawbacks. First, one can obtain the tetrahedral value for Q3 only when the configuration is of a certain pyramidal shape. Second, its value for a tetrahedral configuration is not a limiting value, which in some cases could result in a mean value near tetrahedrality, although the configurations would be far from tetrahedral. The other parameter, T [28,29], also has two main drawbacks: given that each evaluation requires the calculation of ten distances it is expensive in computer time; likewise, it is difficult to connect its value to the configurational geometry.

In order to solve the aforementioned drawbacks, Chau and Hardwick [30] proposed the parameter S, which is composed of two parts, $S_{g}$ and $S_{k}$. The first part, $S_{g}$, is used to test for tetrahedral angles, and its value can be mapped to the configurational geometry. The second part, $S_{k}$, is the variance in the radial distance from the central vertex to the other four vertices. The parameter S has the advantage that it can tell us how distorted the polyhedron is, and in what way. A drawback of S is that it is difficult to connect the value of $S_{k}$ to the geometry of the configuration.

In an extensive and detailed study, Errington and Debenedetti [31] used a rescaled version of the parameter S (which they call q) to study the changes in structure of the SPC/E water model under various temperature and pressure conditions. Here the authors show a bimodal distribution for this order parameter, suggesting that each water molecule and its four nearest neighbors present a transient arrangement [32-34] which can be described as being predominantly structured (and 'ice-like') or unstructured.

All the aforementioned parameters are constructed upon the knowledge of the position of every oxygen atom in water bulk. This can only be achieved through computational studies of water models; i.e. MD or Monte Carlo simulations. Additionally, all the discussed parameters that evaluate tetrahedrality only take explicitly into account the first coordination sphere.

![](./images/811702141252009984_5.jpg)

Fig. 3. The dimensionless parameter $P_{r}$ of SPC/E water model at 300 K as a function of pressure (P, kbar). The crossover point is defined by the pressure at which $P_{r}=0$.

We propose a new order parameter ($P_{r}$) which is capable of evaluating structure beyond the first coordination sphere. Furthermore, this parameter requires only of the knowledge of the probability density function for the position of water oxygens. Such information may be obtained by both computational and experimental studies. The parameter $P_{r}$ is defined as:

$$
P_{r}=\frac{C^{t}-C^{h}}{C^{t}+C^{h}} \tag{5}
$$

with

$$
C^{t}=\frac{A_{1}^{t}}{w_{1}^{t}}+\frac{A_{2}^{t}}{w_{2}^{t}} \tag{6}
$$

$$
C^{h}=\frac{A_{1}^{h}}{w_{1}^{h}}+\frac{A_{2}^{h}}{w_{2}^{h}} \tag{7}
$$

where $A_{i}^{j}$ is proportional to the area under the Gaussian component i of the tetrahedral ($j=t$) and hexagonal ($j=h$) contribution respectively, and $w_{i}^{j}$ gives a measure of the dispersion of the corresponding Gaussian component.

Fig. 3 shows the $P_{r}$ at 300 K as a function of pressure. A monotonically decreasing behavior from 1 bar to 10 kbar may be entirely appreciated.

The actual limiting values of $P_{r}$ go from 0.2 at 1 bar to $-0.38$ at 10 kbar.

The same analysis was applied to the radial distribution functions of liquid argon produced from a number of molecular dynamic simulations performed under various pressure conditions, ranging from 60 bar to 180 bar, obtaining values of $P_{r}$ within the range of $-0.43$ to $-0.46$. This is close to the limiting value found for water. Hence, although from a mathematical point of view $1>P_{r}>-1$, the extreme values (1 and $-1$) are found only in pure tetrahedral and hexagonal structures; i.e. in crystals. In opposition, the liquid state may be regarded as a closely interweaved coexistence of different structures, eventually showing a dominance of one over the rest.

The value of $P_{r}$ becomes negative at pressures above 2.3 kbar. This point marks the crossover between the prevalence of tetrahedral and hexagonal structures.

The calculated crossover point agrees fairly well with the transition of water properties observed experimentally, such as rota-

![](./images/811702141252009984_6.jpg)

Fig. 4. Dependence of the crossover point with temperature (closed black circles).
The points under 243 K belong to the supercooled region of the SPC/E water model.
HDL shows the region in which the prevalent structure corresponds to the hexago-
nal coordination state, which is structurally compatible with a high density condi-
tion of water. The region that corresponds to the predominance of the tetrahedric
structure has been denoted as LDL, and is structurally compatible with the lower
density condition of water. The open circle indicates the critical point. The Widom
line can be observed for temperatures above the critical point (black line). The
coexistence line is represented by the broken line. The crossover points at tempera-
tures below the critical point were fitted with a non-linear curve (black non-linear
curve).

tional and translational diffusion [20,35], viscosity [21], and inelas-
tic X-ray diffraction [36,37].

In order to analyze the temperature dependence of the cross-
over point, further simulations were performed at temperatures
ranging from 93 K to 373 K.

Within the region comprised between 243 K and 373 K,
a monotonically decreasing behavior of this parameter with the
increase in temperature becomes apparent. Such an observation
comes as a reasonable expectation when we take into considera-
tion that temperature holds a destructive effect upon the tetrahe-
dral structure of water.

These results, together with this last interpretation, are in good
agreement with the changes in water structure observed by Erring-
ton and Debenedetti [31].

Additionally, we have calculated the crossover points for dif-
ferent temperatures, including points in the supercooled range.
The results are shown in Fig. 4. The calculated points define a
crossover curve separating two regions. The region in which the
prevalent structure corresponds to a hexagonal coordination has
been indicated as HDL (high density liquid [38]), which is struc-
turally compatible with the high density condition of water, whilst
the denomination of LDL (low density liquid [38]) was used for
the region that corresponds to the predominance of tetrahedric
structure, which in turn is structurally compatible with the lower
density condition of water. The results obtained agree qualitatively
with such a behavior as expected for supercooled water [38,39].

The obtained crossover data shows a critical point $(T_{c},P_{c})$ between a linear and a non-linear regime. The linear regime corre-
sponds to the so-called 'Widom line' [38], which at lower temper-
atures can be extrapolated as a coexistence region (broken line in
Fig. 4).

The line connecting the different points can be regarded as a
frontier that delimitates structural prevalence (full curve). When
crossing the Widom line along an isobar at $P<P_{c}$ (path a), a tran-
sition from the HDL to LDL is obtained, resulting in qualitative
changes in behavior of structural and dynamical properties. How-
ever, when an isobar with $P>P_{c}$ (path b) is followed, continuous
changes are observed in both structural and dynamical properties
of water.

From the previous results, the critical point may be estimated at
$T_{c}=268$ K and $P_{c}=3.5$ kbar. This value is very much within the
order of that obtained for the TIP5P $(T_{c}=217$ K; $P_{c}=3.5$ kbar)
and ST2 $(T_{c}=246$ K; $P_{c}=1.86$ kbar) water models, which were
calculated using the changes in compressibility and diffusion coef-
ficient [38]. This result is likewise consistent with those obtained
by Kumar et al. [40]. The behavior of these two properties come
within the so-called 'water anomalies'.

4. Conclusions

Based on a two-state model for liquid water, we have explicitly
taken into account the first three coordination spheres for both the
tetrahedral and hexagonal structural contributions. We thus elab-
orated the G function in order to reproduce the oxygen-oxygen
probability density function. This function has shown a remarkable
ability to recreate this probability function at every temperature
and pressure condition tested. The data provided by our model was
used for the elaboration of a structural order parameter $(P_{r})$ that
allows us to define a structural crossover point which establishes
the change in prevalence between the tetrahedral and hexagonal
structural contributions with pressure and temperature. The pro-
posed parameter has two further advantages. Namely, that it is
able to quantify structural contributions beyond the first coordi-
nation sphere and that it may be applied to the study of computa-
tionally or experimentally obtained $g_{r}$ functions. We may conclude
that the increase in both pressure and temperature induce an in-
crease in the hexagonal structural contribution in detriment of the
tetrahedral one.

Acknowledgements

The authors thank S.A. Grigera and L.A. Pugnaloni for useful
discussions. This work was partially supported by the National Re-
search Council of Argentina (CONICET, PIP-112-200801-03247), the
National University of La Plata and the National Agency for the
Promotion of Science and Technology (ANPCyT, PICT-1564). O.C.
and J.R.G. are members of the Research Career of the CONICET,
Argentina. A.N.McC. is member of the Research Career of the Re-
search Council of the Buenos Aires Province (CICPBA), Argentina.

References

[1] J.D. Bernal, R.H. Fowler, J. Chem. Phys. 1 (1933) 515.
[2] H.J.C. Berendsen, in: E. Cole (Ed.), Water Structure in Theoretical and Experi-
mental Biophysics, Marcel Dekker, 1967 (Chapter 1).
[3] L. Hall, Phys. Rev. 73 (1948) 775.
[4] A. Geiger, H.E. Stanley, Phys. Rev. Lett. 49 (1982) 1749.
[5] C.M. Davis, T.A. Litovitz, J. Chem. Phys. 42 (1990) 2563.
[6] C.M. Davis, D. Bradley, J. Chem. Phys. 45 (1990) 2461.
[7] M.C. Bellissent-Funel, J. Teixeira, L.J. Bosio, J. Chem. Phys. 87 (1990) 2231.
[8] O. Mishima, H. Stanley, Nature 396 (1998) 329.
[9] E.W. Castner, Y.J. Chang, Y.C. Chu, G.E. Walrafen, J. Chem. Phys. 102 (1995) 653.
[10] C.J. Montrose, J.A. Bucaro, J. Marshall-Coakley, T.A. Litovitz, J. Chem. Phys. 60
(1974) 5025.
[11] W. Danninger, G. Zundel, J. Chem. Phys. 74 (1981) 2779.
[12] J. Yeixeira, S.H. Chen, M.-C. Bellissent-Funel, J. Mol. Liq. 48 (1991) 111.
[13] R. Laenen, C. Rauscher, A. Laubereau, Phys. Rev. Lett. 80 (1998) 2622.
[14] S. Woutersen, U. Emmerichs, H.J. Bakker, Science 278 (1997) 658.
[15] H.K. Nienhuys, S. Woutersen, R.A. van Santen, H.J. Bakker, J. Phys. Chem. 111
(1999) 1494.
[16] G.M. Gale, G. Gallot, F. Hache, N. Lascoux, S. Bratos, J.C. Leicknam, Phys. Rev.
Lett. 82 (1999) 1068.
[17] A.H. Narten, M.D. Danford, H.A. Levy, Faraday Discuss. 43 (1967) 97.
[18] A.K. Soper, F. Bruni, M.A. Ricci, J. Chem. Phys. 106 (1997) 247.
[19] K. Modig, B.G. Pfrommer, B. Halle, Phys. Rev. Lett. 90 (2003) 075502.
[20] F.X. Prielmeier, E.W. Lang, R.J. Speedy, H.D. Lüdemann, Phys. Rev. Lett. 59
(1987) 1128.

[21] R.A. Horne, D.S. Johnson, J. Phys. Chem. 70 (1966) 2182.

[22] D. van der Spoel, E. Lindahl, B. Hess, G. Groenhof, A.E. Mark, H.J.C. Berendsen, J. Comput. Chem. 26 (2005) 1701.

[23] S. Miyamoto, P.A. Kollman, J. Comput. Chem. 13 (1992) 952.

[24] H.J.C. Berendsen, J.R. Grigera, T.P. Straatsma, J. Phys. Chem. 91 (1987) 6269.

[25] H.J.C. Berendsen, J.P.M. Postma, A. DiNola, J.R. Haak, J. Chem. Phys. 81 (1984) 3684.

[26] T.M. Truskett, S. Torquato, P.G. Debenedetti, Phys. Rev. E 62 (2000) 993.

[27] P.J. Steinhardt, D.R. Nelson, M. Ronchetti, Phys. Rev. B 28 (1983) 784.

[28] Y.U.I. Naberukhin, V.P. Voloshin, N.N. Medvedev, Molec. Phys. 73 (1991) 917.

[29] M. Kiselev, M. Poxleitner, J. Seitz-Beywl, K. Heinzinger, Z. Naturf. A 48 (1993) 806.

[30] P.L. Chau, A.J. Hardwick, Molec. Phys. 93 (1998) 511.

[31] J.R. Errington, P.G. Debenedetti, Nature 409 (2001) 318.

[32] E. Shiratani, M. Sasai, J. Chem. Phys. 108 (1998) 3264.

[33] F. Sciortino, P.H. Poole, H.E. Stanley, S. Havlin, Phys. Rev. Lett. 64 (1990) 1686.

[34] F. Sciortino, A. Geiger, H.E. Stanley, Nature 354 (1991) 218.

[35] L.A. Wolf, J. Chem. Soc., Faraday Trans. 71 (1975) 784.

[36] Y.Q. Cai, et al., Phys. Rev. Lett. 94 (2005) 025502.

[37] A. Cunsolo, F. Formisano, C. Ferrero, F. Bencivenga, S. Finet, J. Chem. Phys. 131 (2009) 194502.

[38] L. Xu, P. Kumar, S. V Buldyrev, S.H. Chen, P.H. Poole, F. Sciortino, H.E. Stanley, PNAS 102 (2005) 16562.

[39] G. Franzese1, H. Stanley, J. Phys.: Condens. Matter 19 (2007) 205126.

[40] P. Kumar, S.V. Buldyrev, S.R. Becker, P.H. Poole, F.W. Starr, H.E. Stanley, PNAS 105 (2007) 9575.