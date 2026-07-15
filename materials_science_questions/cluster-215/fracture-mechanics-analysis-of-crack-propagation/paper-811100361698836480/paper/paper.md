Metal working

# Finite element analysis of formability of a few kinds of special steel sheets
Hirohiko Takuda, Hitoshi Fujimoto, Yoshito Kuroda and Natsuo Hatta

Deep drawing processes of various special steel sheets are simulated by the rigid-plastic finite element method. To predict the forming limit a criterion for ductile fracture is applied. From the histories of stress and strain in each element calculated by the finite element simulation, the fracture initiation site and the critical stroke are predicted by means of the ductile fracture criterion. The predictions so obtained are compared with experimental observations. The results show that the finite element analysis combined with the ductile frac- ture criterion is useful to predict the forming limit in a wide range of sheet steels.

Finite-Elemente-Analyse der Umformbarkeit einiger Edelstahl-Feinbleche. Mit der starr-plastischen FE-Methode wird das Tiefziehen verschiedener Edelstahlfeinbleche simuliert. Zur Vorausbestimmung der Grenzformänderung wird das Kriterium für duktilen Bruch angewendet. Aus der Entwicklung von Spannung und Formänderung in jedem Element, die sich mit der FE-Simulation berechnen ließ, kann man den Ort der Brucheinleitung und den kritischen Stich unter Zuhilfenahme des Bruchkriteriums vorausberechnen. Eine Über- prüfung der auf diese Weise erhaltenen Resultate mit Versuchsergebnissen zeigt, daß die Kombination der FE-Analyse mit dem Kriterium des duktilen Bruches zur Vorausberechnung der Grenzformänderung für eine breite Palette von Feinblechstählen herangezogen werden kann.

In recent years, due to the demand for higher functions in material, such as high strength and high corrosion resis- tivity, many steel sheets with special qualities have been developed and increasingly employed in various indus- tries. However, some special steel sheets are much inferior to ordinary steel sheets in formability. In order to find the forming method and conditions suitable for the special steel sheets, the forming limit, i.e. the fracture initiation in sheet forming processes has to be correctly predicted.

In sheet metal forming, the forming limit is generally determined by the onset of localized necking and predicted by the analyses of tensile instability or bifurcation phe- nomena [1...4]. However, the plastic properties of the special steel sheets are not so simple as those of the ordi- nary steel sheets. The effects of the material properties, such as the work-hardening exponent, $n$, and the normal anisotropy parameter, $r$, on the forming limit have not been clarified in detail. Besides, in case of special steel sheets with low ductility, fracture often occurs without any obvious necking or thinning phenomenon. Accordingly, the conventional approaches based on the tensile instability or bifurcation are not always suitable for the special steel sheets.

In the present study, the possibility of the prediction by another approach is examined. The forming limit, i.e. the fracture initiation is predicted not by the onset of localized necking, but by the occurrence of fracture itself. A crite- rion for ductile fracture is introduced in the finite element simulation. From the distributions and the histories of stress and strain calculated by the finite element simula- tion, the fracture initiation site and the critical stroke are predicted by means of the fracture criterion. The calcula- tions are carried out for axisymmetric deep drawing proc- esses of a few kinds of special steel sheets. The validity of the predictions is examined by comparing with the ex- perimental observations.

Professor Dr. Hirohiko Takuda; Dr. Hitoshi Fujimoto; Yoshito Kuroda; Professor Dr. Natsuo Hatta, Department of Energy Science and Tech- nology, Kyoto University, Kyoto, Japan.

## Materials
Materials used in the present study are three various spe- cial steel sheets, a Zn-coated hard steel sheet with a thick- ness of 0.7 mm, a type 430 stainless steel sheet with a thickness of 0.78 mm and a high strength steel sheet with a thickness of 1.0 mm, and they are expressed as materials A, B and C, respectively. The chemical compositions of the materials are indicated in table 1.

Table 1. Chemical compositions of materials (mass contents in %)
<table>
<thead>
<tr>
<th></th>
<th>C</th>
<th>Si</th>
<th>Mn</th>
<th>P</th>
<th>S</th>
<th>Ni</th>
<th>Cr</th>
<th>Al</th>
</tr>
</thead>
<tbody>
<tr>
<td>material A</td>
<td>0.04</td>
<td>0.01</td>
<td>0.22</td>
<td>0.014</td>
<td>0.017</td>
<td>–</td>
<td>–</td>
<td>0.025</td>
</tr>
<tr>
<td>material B</td>
<td>0.04</td>
<td>0.28</td>
<td>0.12</td>
<td>0.023</td>
<td>0.001</td>
<td>0.09</td>
<td>16.2</td>
<td>0.125</td>
</tr>
<tr>
<td>material C</td>
<td>0.15</td>
<td>0.23</td>
<td>1.86</td>
<td>0.015</td>
<td>0.002</td>
<td>–</td>
<td>–</td>
<td>0.029</td>
</tr>
</tbody>
</table>

Table 2. Tensile properties of materials
<table>
<thead>
<tr>
<th></th>
<th>material A</th>
<th>material B</th>
<th>material C</th>
</tr>
</thead>
<tbody>
<tr>
<td>tensile strength, MPa</td>
<td>748</td>
<td>488</td>
<td>672</td>
</tr>
<tr>
<td>elongation, %</td>
<td>2.3</td>
<td>27.3</td>
<td>22.2</td>
</tr>
<tr>
<td>$F$-value, MPa</td>
<td>858</td>
<td>829</td>
<td>1020</td>
</tr>
<tr>
<td>work-hardening exponent $n$</td>
<td>0.03</td>
<td>0.20</td>
<td>0.14</td>
</tr>
<tr>
<td>normal anisotropy parameter $r$</td>
<td>0.87</td>
<td>0.81</td>
<td>0.91</td>
</tr>
</tbody>
</table>

Table 3. Fracture strains in tensile direction, $\varepsilon_{1f}$, of materials in uniaxial and plane-strain tension tests
<table>
<thead>
<tr>
<th></th>
<th>material A</th>
<th>material B</th>
<th>material C</th>
</tr>
</thead>
<tbody>
<tr>
<td>$\varepsilon_{1f}$(uniaxial)</td>
<td>0.303</td>
<td>0.595</td>
<td>0.634</td>
</tr>
<tr>
<td>$\varepsilon_{1f}$(plane-strain)</td>
<td>0.130</td>
<td>0.336</td>
<td>0.285</td>
</tr>
</tbody>
</table>

Table 4. Material constants $a$ and $b$ in equation (2)
<table>
<thead>
<tr>
<th></th>
<th>material A</th>
<th>material B</th>
<th>material C</th>
</tr>
</thead>
<tbody>
<tr>
<td>$a$</td>
<td>– 0.132</td>
<td>0.020</td>
<td>– 0.098</td>
</tr>
<tr>
<td>$b$</td>
<td>0.063</td>
<td>0.217</td>
<td>0.152</td>
</tr>
</tbody>
</table>

398
steel research 68 (1997) No. 9

![](./images/811100361698836480_1.jpg)

Figure 1. Flow curves in uniaxial tension tests of materials A, B and C

The uniaxial tension tests were carried out in the directions of 0, 45 and 90° to rolling. The gauge length and width of the tensile specimens were 50 and 12.5 mm, respectively. Figure 1 shows the obtained true-stress/ true-strain curves of the materials. Table 2 indicates the tensile properties with the average values for the three directions. Here, the true stress-strain ($\sigma$-$\varepsilon$) relation was approximated by

$$
\sigma=F \varepsilon^{n}. \quad (1)
$$

![](./images/811100361698836480_2.jpg)

Figure 2. Specimen for plane-strain tension tests

The normal anisotropy parameter, $r$, was measured at the elongation of 15% for the materials B and C, and at 1% for the material A. There is much variety found between the properties of the materials.

## Ductile fracture criterion

Based on various hypotheses, some criteria for ductile fracture have been proposed [5]. The occurrence of ductile fracture is estimated in these criteria by the macroscopic stress and strain during forming. In this study, we employ the following criterion proposed by Oyane et al. [6]:

$$
\int_{0}^{\bar{\varepsilon}_{\mathrm{f}}}\left(\frac{\sigma_{\mathrm{m}}}{\bar{\sigma}}+a\right) \mathrm{d} \bar{\varepsilon}=b,
\tag{2}
$$

where $\bar{\varepsilon}_{\mathrm{f}}$ is the equivalent strain at which the fracture occurs, $\sigma_{\mathrm{m}}$ is the hydrostatic stress, $\bar{\sigma}$ is the equivalent stress, $\bar{\varepsilon}$ is the equivalent strain, and $a$ and $b$ are the material constants.

To determine the material constants $a$ and $b$ in equation (2) the destructive tests have to be operated under at least two types of stress conditions. Accordingly, in addition to the aforementioned uniaxial tension tests, the plane-strain tension tests were carried out, using the tensile specimen shown in figure 2. Table 3 shows the fracture strains in tensile direction, $\varepsilon_{1 \mathrm{f}}$, derived from the measured reductions of area in uniaxial and plane-strain tension tests.

When the normal anisotropy of sheet is considered in accordance with Hill's yield criterion [7], the ratios of the hydrostatic stress to the equivalent stress, $\sigma_{\mathrm{m}} / \bar{\sigma}$, and of the equivalent strain to the strain in tensile direction, $\bar{\varepsilon} / \varepsilon_{1}$, during uniform deformation at the uniaxial and plane-strain tension tests are given as:

### uniaxial

$$
\frac{\sigma_{\mathrm{m}}}{\bar{\sigma}}=\frac{1}{3} \sqrt{\frac{2(2+r)}{3(1+r)}},
$$

$$
\frac{\bar{\varepsilon}}{\varepsilon_{1}}=\sqrt{\frac{2(2+r)}{3(1+r)}} ;
\tag{3}
$$

### plain-strain

$$
\frac{\sigma_{\mathrm{m}}}{\bar{\sigma}}=\frac{1}{3} \sqrt{\frac{2(2+r)(1+2 r)}{3(1+r)}},
$$

$$
\frac{\bar{\varepsilon}}{\varepsilon_{1}}=\sqrt{\frac{2(2+r)(1+r)}{3(1+2 r)}}.
\tag{4}
$$

Provided that the relations of equations (3) and (4) are maintained until fracture initiation, the material constants $a$ and $b$ are approximately obtained from equations (2) to (4) and $\varepsilon_{1 \mathrm{f}}$ in table 3, as indicated in table 4.

![](./images/811100361698836480_3.jpg)

Figure 3. Schematic of axisymmetric deep drawing

## Experimental and simulation methods of deep drawing

For the sheets with the above-mentioned properties the cylindrical deep drawing tests using flat punches with a diameter of 40 mm are carried out. The profile radii of the punches, $r_{\mathrm{p}}$, are 2, 4, 8 and 20 (hemispherical) mm. The diameter and the profile radius of the die are 42.5 and 8 mm, respectively, figure 3. Circular blanks with various diameters with an interval of 1 mm are prepared, and both faces of the blanks are lubricated by a liquid with PTFE.

![](./images/811100361698836480_4.jpg)

(a) Material A
C.P.S. = 6 ~ 7 mm
(b) Material B
C.P.S. = 12 ~ 13 mm
(c) Material C
C.P.S. = 11 ~ 12 mm

Figure 4. Experimentally observed fractures in deep drawing for $d_0$
= 80 and $r_p$ = 2 mm

The blank holder force for each blank is given according
to Siebel's equation [8].

The above deep drawing tests are simulated by means of
the rigid-plastic finite element method [9]. The finite ele-
ment method is formulated on the basis of the plasticity
theory for a slightly compressible material, by modifying
Hill's yield criterion as

$$
\begin{aligned}
\overline{\sigma}= & \sqrt{\frac{3}{2(2+r)}\left\{r\left(\sigma_{R}-\sigma_{\theta}\right)^{2}+\left(\sigma_{\theta}-\sigma_{Z}\right)^{2}+\left(\sigma_{Z}-\sigma_{R}\right)^{2}\right\}} \\
& +3 \tau_{R Z}^{2}+g\left\{\frac{1}{1+2 r}\left(r \sigma_{R}+r \sigma_{\theta}+\sigma_{Z}\right)\right\}^{2},
\end{aligned}
\tag{5}
$$

where $g$ is a small positive constant (0.01 ~ 0.0001). In the
simulation, therefore, the normal anisotropy of sheet is
taken into consideration, while the axisymmetric deforma-
tion with no planar anisotropy is assumed. Meshing is
carried out also in the thickness direction using the solid
elements (figure 3). Literature [9] and [10] should be re-
ferred to for details of the simulation method. The coeffi-
cient of friction between the tools and the sheet is assumed
to be 0.1.

Then, Oyane's ductile fracture criterion is applied as
follows. Rewriting equation (2), one gets the integral,

$$
I=\frac{1}{b} \int_{0}^{\bar{\varepsilon}}\left(\frac{\sigma_{\mathrm{m}}}{\overline{\sigma}}+a\right) \mathrm{d} \bar{\varepsilon}.
\tag{6}
$$

Using the values of $\sigma_{m}$, $\overline{\sigma}$ and $d\bar{\varepsilon}$ obtained by the finite
element simulation and the material constants $a$ and $b$ in
table 4, the integral $I$ is calculated for each element and
each deformation step. The condition of fracture is satis-
fied when and where the integral $I$ amounts to 1.

## Results
Figure 4 gives examples of experimentally observed
fractures. This photograph shows the outsides of the mate-
rials A, B and C after fracture initiation in deep drawing
under the same conditions that the initial blank diameter,
$d_0$, is 80 mm and the punch profile radius, $r_p$, is 2 mm. The
fracture around the punch corner is observed in every case,
while the critical punch strokes, C.P.S., differ.

Figures 5 - 7 show the simulated results for the above
cases. The left part (a) of each figure shows the transition
of the blank profile with increase in the punch stroke, P.S.
The right part (b) shows the transition of the distribution of
the integral $I$. The horizontal and the vertical axes of figure

![](./images/811100361698836480_5.jpg)

Figure 5. a) Deformed meshes and b) distributions of integral $I$ in
deep drawing calculated for material A, $d_0$ = 80 mm and $r_p$ = 2 mm

![](./images/811100361698836480_6.jpg)

Figure 6. a) Deformed meshes and b) distributions of integral $I$ for
material B

![](./images/811100361698836480_7.jpg)

Figure 7. a) Deformed meshes and b) distributions of integral $I$ for
material C


![](./images/811100361698836480_8.jpg)

Figure 8. Comparison between calculated and measured distributions of sheet thickness at fracture initiation

fied at $P.S. = 6.3$ mm for the material A, $P.S. = 11.7$ mm for the material B and $P.S. = 10.2$ mm for the material C, which correspond to the measured critical strokes (figure 4) fairly well.

![](./images/811100361698836480_9.jpg)

Figure 10. Experimentally observed fracture in deep drawing for $d_0 = 77$ mm and $r_p$ = 8 mm

b indicate the initial radial position from the blank centre and the average value of $I$ in the thickness direction at the corresponding radial position, respectively. The integral $I$ around the punch corner amounts to 1, i.e., the condition of fracture is satis-

The thickness distributions at fracture initiation obtained by the calculation and the experiment for the above cases are indicated in figure 8. The localized thinning is observed at the fracture initiation site around the punch corner in every case. The calculated distributions are in good agreement with the measured ones. It is found that the critical thickness strain greatly depends upon the material, and that the fracture occurs at a small amount of thinning for the material A.

Again in figures 5, 6 and 7, it is observed from the transitions of the blank profile that the necking appears around the punch corner and the deformation is localized there. Therefore, the fact that the blank suffers a fracture during deep drawing can be predicted for the above cases even without the fracture criterion, though the critical punch stroke cannot be obtained.

![](./images/811100361698836480_10.jpg)

Figure 9. a) Deformed meshes and b) distributions of integral $I$ in deep drawing calculated for material A, $d_0 = 77$ mm and $r_p = 8$ mm

On the contrary, figure 9 illustrates the case where the fracture cannot be predicted without the ductile fracture criterion. Figure 9 shows the calculated result of deep drawing of the material A for $d_0 = 77$ mm and $r_p = 8$ mm. The transition of the blank profile (figure 9a) shows that the localized necking does not occur. If the fracture initiation should be judged only by the localized necking, it would be predicted that the blank is successfully drawn without any fracture. However, as figure 10 shows, actually the fracture occurs around the punch corner at the early stage of deep drawing without any obvious necking. On the other hand, figure 9b shows that the integral $I$ around the punch corner amounts to 1 at $P.S. = 11.0$ mm. It is found that the introduction of the ductile fracture criterion allows the prediction of forming limit even in no appearance of localized necking.

![](./images/811100361698836480_11.jpg)

Figure 11. Comparison between calculated and experimental limiting drawing ratios, $L.D.R.$, for various punch profile radii

The limiting drawing ratios, $L.D.R.$, predicted by assuming that the fracture occurs when and where the integral $I$ of equation (6) amounts to 1 are compared with the experimental ones en bloc in figure 11. The horizontal axis of this figure indicates the punch profile radius, $r_p$. The calculations were carried out also for the radii of 12 and 16 mm in addition to 2, 4, 8 and 20 mm. The ratio, $L.D.R.$, is defined as

Metal working

$$L.D.R. = d_{\text{max}}/d_{\text{p}}, \tag{7}$$

where $d_{\text{max}}$ is the maximum initial diameter of blank which is drawable without fracture, and $d_{\text{p}}$ is the punch diameter.

For the material A, the $L.D.R.$ shows the maximum value at $r_{\text{p}} = 4$ mm and remarkably decreases with increase in $r_{\text{p}}$. The $L.D.R.$ is almost constant, independent of $r_{\text{p}}$, for material B. For material C, the peak value of $L.D.R.$ is attained at $r_{\text{p}} = 8$ mm, while the influence of $r_{\text{p}}$ on $L.D.R.$ is not so remarkable as that for material A. The above relations between $L.D.R.$ and $r_{\text{p}}$ are obtained by the calculation as well as the experiment. While the calculated $L.D.R.$ is somewhat smaller than the experimental one, for the hemispherical punch ($r_{\text{p}} = 20$ mm) in particular, good agreements are recognized between the calculated and experimental results in almost all the cases.

## Conclusion

In this study, the formability of various special steel sheets in deep drawing processes has been analyzed by the rigid-plastic finite element simulatioin and the ductile fracture criterion. The comparison with the experimental results has shown that the forming limits for various sheets are successfully obtained by the present approach, even in no appearance of localized necking. The results have suggested that the application of the ductile fracture criterion allows the prediction of forming limit in a wide range of sheet steel forming processes.

## Acknowledgement

The authors would like to thank Nippon Steel Corporation for providing the steel sheets.

(A 01 278; received: 03. February 1997;
in completed form: 05. May 1997)

## References

[1] Swift, H.W.: J. Mech. Phys. Solids 1 (1952), p. 1/18.
[2] Marciniak, Z.; Kuczynski, K.: Intern. J. Mech. Sci. 9 (1967), p. 609/20.
[3] Stören, S.; Rice, J.R.: J. Mech. Phys. Solids 23 (1975), p. 421/41.
[4] Gotoh, M.: Eng. Fract. Mech. 21 (1985), p. 673/84.
[5] Clift, S.E.; Hartley, P.; Sturgess, C.E.N.; Rowe, G.W.: Intern. J. Mech. Sci. 32 (1990), p.1/17
[6] Oyane, M.; Sato, T.; Okimoto, K.; Shima, S.: J. Mech. Work. Technol. 4 (1980), p. 65/81.
[7] Hill, R.: The Mathematical Theory of Plasticity, Oxford University Press, Oxford, 1950, p. 318/21.
[8] Siebel, E.: Stahl u. Eisen 74 (1954), p. 155/58.
[9] Osakada, K.; Nakano, J.; Mori, K.: Intern. J. Mech. Sci. 24 (1982), p. 459/68.
[10] Mori, K.; Takuda, H.: Trans. NAMRI/SME 24 (1996), p. 143/48.