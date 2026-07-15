# THE FIRST PRINCIPLES STUDY ON LIGHT EMITTING PROPERTIES OF SEMICONDUCTING METAL SILICIDES

KENJI YAMAGUCHI, KAZUKI MIZUSHIMA, and KOICHI SASSA
Central Research Institute, Mitsubishi Materials Corporation, Omiya, Saitama 330-8508, Japan

## ABSTRACT

Semiconducting metal silicides are potential candidates of silicon-based light emitting materials. In order to carry out screening of the candidates, we calculated the oscillator strength between the valence and excited states near the band gap for various silicides. The electronic states were obtained by the full-potential linear augmented-plane-wave method (FLAPW) based on the local density approximation (LDA). The results show $Ru_2Si_3$ and $Ca_2Si$ have direct gap at $\Gamma$ point, but the values of the oscillator strength across the gap are evaluated to be zero. Among the indirect gap semiconductors, $\beta$-FeSi$_2$, OsSi, and $OsSi_2$ have several peaks and valleys facing each other near the band gap. Among the combinations, we obtained the biggest value of oscillator strength 0.3 at X point for OsSi with the transition energy of 0.42 eV.

## INTRODUCTION

To date, there are many studies on thermoelectric properties of semiconducting metal silicides [1]. Optical properties of some silicides are studied also, these days. In the studies, such applications as silicon-based light emission or detection, and also photovoltaics are considered. Although little is known at this moment about light emitting properties of semiconducting metal silicides, the recent successful fabrication of a $\beta$-FeSi$_2$ light emitting diode (LED) demonstrated potential capability of silicides as the silicon-based light emitting materials [2]. In this study we investigate optical properties of various silicides in order to examine their capability of light emission.

The $\beta$-FeSi$_2$ is the most extensively studied semiconducting metal silicide. In one of the studies, the band gap energy was determined by optical absorption to be 0.76 eV for indirect gap and 0.87 eV for direct gap [3]. In the other optical experimental studies, $\beta$-FeSi$_2$ was found to have only a direct gap with the value of 0.83 eV [4] also. Thus the type (direct or indirect) of the gap of $\beta$-FeSi$_2$ is still controversial. In the theoretical work, Clark *et al.* [5] showed that the shape of band structure near the gap is sensitive to lattice strain and they suggested that the type of the gap depends on the fabrication methods of the samples.

For $CrSi_2$ [6], $ReSi_2$ [7], and $MnSi_{1.7}$ [8], optical measurements revealed that they have indirect band gap with the values of 0.35 eV, 0.12 eV, and 0.6 eV, respectively. For $Ir_3Si_5$ [9], optical measurements also revealed that it has a direct gap with the value of 1.5 eV.

In the literatures band gap values are available for such silicides as $Ru_2Si_3$ (0.9 eV) [1], OsSi (0.34 eV) [10], $OsSi_2$ (1.4 eV) [10], $Os_2Si_3$ (2.3 eV) [10], MnSi (0.6 eV) [11], $LaSi_2$ (0.19 eV) [11], $Mg_2Si$ (0.75 eV) [11], $Ca_2Si$ (1.9 eV) [11], and $BaSi_2$ (0.48 eV) [11]. These

215
Mat. Res. Soc. Symp. Proc. Vol. 579 © 2000 Materials Research Society

values were determined by the temperature dependence of electric conductivity at the intrinsic region. However the type of each silicide is not given in the literatures [1,10,11].

In the theoretical works, $Ru_2Si_3$ was characterized as a direct semiconductor with the gap of 0.45 eV [12], and $OsSi_2$ was as an indirect one with the gap of 0.95 eV [13].

In this study, we consider such silicides as $\beta$-FeSi$_2$, CrSi$_2$, ReSi$_2$, Ru$_2$Si$_3$, OsSi, OsSi$_2$, MnSi, LaSi$_2$, Ir$_3$Si$_5$, Mg$_2$Si, Ca$_2$Si, and BaSi$_2$. These silicides are chosen because that are known as semiconducting metal silicides, and both of the crystal structure and atomic configuration are available in the literatures as listed in Table I [14-25].

**Table I Data of semiconducting metal silicides.**
<table>
  <thead>
    <tr>
      <th>Silicides</th>
      <th>Structure</th>
      <th>Gap (eV)</th>
      <th>Type</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>$\beta$-FeSi₂</td>
      <td>Cmca [14]</td>
      <td>0.76 / 0.87 [3]</td>
      <td>Indirect / Direct</td>
    </tr>
    <tr>
      <td>CrSi₂</td>
      <td>P6₂22 [15]</td>
      <td>0.35 [6]</td>
      <td>Indirect</td>
    </tr>
    <tr>
      <td>ReSi₂</td>
      <td>Immm [16]</td>
      <td>0.12 [7]</td>
      <td>Indirect</td>
    </tr>
    <tr>
      <td>Ru₂Si₃</td>
      <td>Pbcn [17]</td>
      <td>0.9 [1]</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>OsSi</td>
      <td>P2₁3 [18]</td>
      <td>0.34 [10]</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>OsSi₂</td>
      <td>Cmca [19]</td>
      <td>1.8 [10]</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>MnSi</td>
      <td>P2₁3 [20]</td>
      <td>0.6 [11]</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>LaSi₂</td>
      <td>I4₁/amd [21]</td>
      <td>0.19 [11]</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>Ir₃Si₅</td>
      <td>P2₁/2 [22]</td>
      <td>1.56 [9]</td>
      <td>Direct</td>
    </tr>
    <tr>
      <td>Mg₂Si</td>
      <td>Fm3m [23]</td>
      <td>0.6 [11]</td>
      <td>Indirect</td>
    </tr>
    <tr>
      <td>Ca₂Si</td>
      <td>Pnma [24]</td>
      <td>1.9 [11]</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>BaSi₂</td>
      <td>Pnma [25]</td>
      <td>0.48 [11]</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>

## CALCULATION PROCEDURES

We calculated electronic band structure of each silicide by using the full-potential lin- earized augmented-plane-wave method (FLAPW) based on the local density approxima- tion (LDA) for exchange and correlation interactions. We adopted the WIEN97 code [26] to perform the calculations. In the muffin-tin spheres (MTS), the scalar relativistic cal- culations were performed. For silicon and alkaline-earth metals valence electrons were considered up to d-states, and for transition elements valence electrons were considered up to f-states. To achieve convergence of total energy of $\beta$-FeSi$_2$, 50 to 100 linearized aug- mented plane waves per atom were needed. The irreducible k-points were sampled from about 50 points equally spaced in the Brillouin zone. We chose a slightly smaller value for the radius of MTS compared to half of the nearest neighbor distance.

In order to examine light emitting property of each silicide, we estimated the values of oscillator strength across the band gap within the electric dipole approximation.

The applicability of this calculation procedures was tested in the calculations for CrSi$_2$. The calculated values of oscillator strength for CrSi$_2$ were consistent with that of the augmented spherical wave method (ASW) [27]. We obtained the values of 0.203 at M point and 0.0189 at L point, while the ASW values were reported to be 0.22 at M point and 0.0201 at L point [27].

# RESULTS AND DISCUSSIONS

The results of electronic band structure calculations are compiled in Table II. Although $ReSi_2$, $MnSi$, $LaSi_2$, and $BaSi_2$ were reported to be small-gap semiconductors in experimental studies, the underestimation of band gap by LDA caused the closure of the gap for these silicides in our calculations.

Table II Results of electronic band structure calculations.

<table>
  <thead>
    <tr>
      <th rowspan="2">Silicides</th>
      <th rowspan="2">Gap (eV)</th>
      <th rowspan="2">Type</th>
      <th rowspan="2">VBM</th>
      <th rowspan="2">CBM</th>
      <th colspan="3">Oscillator Strength</th>
    </tr>
    <tr>
      <th>k-point</th>
      <th>Transition Energy (eV)</th>
      <th>Value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="2">$\beta$-FeSi₂</td>
      <td rowspan="2">0.600</td>
      <td rowspan="2">Indirect</td>
      <td rowspan="2">$\Gamma$-Z</td>
      <td rowspan="2">Y</td>
      <td>Y</td>
      <td>0.660</td>
      <td>0</td>
    </tr>
    <tr>
      <td>($\Gamma$-Z)/4</td>
      <td>0.738</td>
      <td>0</td>
    </tr>
    <tr>
      <td rowspan="2">CrSi₂</td>
      <td rowspan="2">0.303</td>
      <td rowspan="2">Indirect</td>
      <td rowspan="2">L</td>
      <td rowspan="2">M</td>
      <td>L</td>
      <td>0.452</td>
      <td>0.0189</td>
    </tr>
    <tr>
      <td>M</td>
      <td>0.673</td>
      <td>0.201</td>
    </tr>
    <tr>
      <td>ReSi₂</td>
      <td></td>
      <td>Metal</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Ru₂Si₃</td>
      <td>0.430</td>
      <td>Direct</td>
      <td>$\Gamma$</td>
      <td>$\Gamma$</td>
      <td>$\Gamma$</td>
      <td>0.430</td>
      <td>0</td>
    </tr>
    <tr>
      <td>OsSi</td>
      <td>0.390</td>
      <td>Indirect</td>
      <td>$\Gamma$-R</td>
      <td>X</td>
      <td>X</td>
      <td>0.422</td>
      <td>0.299</td>
    </tr>
    <tr>
      <td rowspan="2">OsSi₂</td>
      <td rowspan="2">0.720</td>
      <td rowspan="2">Indirect</td>
      <td rowspan="2">$\Gamma$-Z</td>
      <td rowspan="2">Y</td>
      <td>$\Gamma$</td>
      <td>0.951</td>
      <td>0</td>
    </tr>
    <tr>
      <td>Y</td>
      <td>0.783</td>
      <td>0</td>
    </tr>
    <tr>
      <td>MnSi</td>
      <td></td>
      <td>Metal</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>LaSi₂</td>
      <td></td>
      <td>Metal</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td rowspan="2">Ir₃Si₅</td>
      <td rowspan="2">0.986</td>
      <td rowspan="2">Indirect</td>
      <td rowspan="2">$\Gamma$-Y</td>
      <td rowspan="2">Y-C</td>
      <td>(Y-C)/2</td>
      <td>1.009</td>
      <td>0.0048</td>
    </tr>
    <tr>
      <td>($\Gamma$-Y)/2</td>
      <td>1.076</td>
      <td>2.7E-5</td>
    </tr>
    <tr>
      <td>Mg₂Si</td>
      <td>0.170</td>
      <td>Indirect</td>
      <td>$\Gamma$</td>
      <td>X</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Ca₂Si</td>
      <td>0.290</td>
      <td>Direct</td>
      <td>$\Gamma$</td>
      <td>$\Gamma$</td>
      <td>$\Gamma$</td>
      <td>0.290</td>
      <td>0</td>
    </tr>
    <tr>
      <td>BaSi₂</td>
      <td></td>
      <td>Metal</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>

As shown in Fig. 1 and Fig. 2, $Ru_2Si_3$ and $Ca_2Si$ are characterized to be direct gap semiconductors and the gaps are placed at $\Gamma$ points. For $Ru_2Si_3$ our result is consistent with another theoretical work [12]. Unfortunately, for both of $Ru_2Si_3$ and $Ca_2Si$, it was predicted that the direct transitions between conduction band minimum (CBM) and valence band maximum (VBM) at $\Gamma$ points are forbidden, i.e. the calculated values of oscillator strength across the band gap were zero.

For $CrSi_2$ and $Mg_2Si$, the obtained electronic band structures are similar with that of the earlier theoretical works [15,27,28]. These are indirect semiconductors, and furthermore they are not direct-like, i.e. there is no facing peak of valence band and valley of conduction band near the band gap.

The electronic band structures show that $\beta$-FeSi₂ (Fig. 3), OsSi (Fig. 4), OsSi₂ (Fig. 5), and $Ir_3Si_5$ (Fig. 6) are also indirect gap semiconductors. To our knowledge, this is the first time to mention the type of semiconductors for OsSi, $Ca_2Si$, and $Ir_3Si_5$ theoretically.

Because $Ir_3Si_5$ has very large unit cell and the Brillouin zone is small, direct transition would be allowed rather easier at finite temperature. Therefore, we examined the oscillator strength between CBM and VBM at half way along the line from Y to C, and from $\Gamma$ to Y, near the indirect band gap. But the predicted values of the oscillator strength are at most $4.8×10^{-3}$ at half way along the line from Y to C.

![](./images/811671275939299328_1.jpg)
Fig .1 Electronic band structure of $Ru_2Si_3$.

![](./images/811671275939299328_2.jpg)
Fig .2 Electronic band structure of $Ca_2Si$.

![](./images/811671275939299328_3.jpg)
Fig .3 Electronic band structure of $\beta$-FeSi$_2$.

![](./images/811671275939299328_4.jpg)
Fig .4 Electronic band structure of OsSi.

![](./images/811671275939299328_5.jpg)
Fig .5 Electronic band structure of $OsSi_2$.

![](./images/811671275939299328_6.jpg)
Fig .6 Electronic band structure of $Ir_3Si_5$.

Among the indirect gap semiconducting silicides, $\beta$-FeSi$_2$, OsSi, and OsSi$_2$ have several peaks and valleys facing each other near the band gap.

For $\beta$-FeSi$_2$, it was predicted that the transitions between CBM and VBM at Y point and at a general point along $\Lambda$ line are both forbidden. This result conflicts with the ASW result reported by Eppenga [29]. Eppenga mentioned that the transition at halfway along $\Gamma$ and Z (along $\Lambda$ line) is allowed and the oscillator strength is 0.01. This conflict comes from the simulation method, i.e. FLAPW or ASW, because the calculations were based on the same atomic configuration. In ASW, potential and electron density are treated within the muffin-tin approximation, while those are treated with realistic non-spherical components in FLAPW. Thus, in general, FLAPW is theoretically more rigorous than ASW. Therefore we believe that the light emission from $\beta$-FeSi$_2$, observed in the experiments [2], is originated with the indirect transition, or the direct transition with the help of mechanisms as magnetic dipole, electric quadrupole, and higher order moments. So that the $\beta$-FeSi$_2$ might have a long luminescent life time.

For OsSi$_2$ it was predicted that the transitions between CBM and VBM at $\Gamma$ and Y points are forbidden, also. In contrast, for OsSi, the value of oscillator strength between CBM and VBM at X point was evaluated to be 0.3. Although the value is about one order smaller than that of typical direct gap zinc-blende crystals [30], the OsSi was predicted to be the most feasible candidate for a light emitting silicide in this work. The transition energy was evaluated to be 0.42 eV which is in the range of infrared light. For CBM and VBM at X point, the normalized probability densities of electrons in MTS are listed in Table III. For both CBM and VBM, electrons are mostly localized at Os site and the states are composed of mainly d symmetry, and slightly p symmetry. Therefore, the dipole transition at X point might occur mainly at Os site through p-d transition.

Table III The normalized probability densities of electrons for OsSi in MTS for CBM and VBM at X point.

<table>
  <thead>
    <tr>
      <th colspan="2">OsSi (X)</th>
      <th>Total</th>
      <th>s</th>
      <th>p</th>
      <th>d</th>
      <th>f</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="2">CBM</td>
      <td>Os</td>
      <td>0.76</td>
      <td>0.01</td>
      <td>0.01</td>
      <td>0.74</td>
      <td>0</td>
    </tr>
    <tr>
      <td>Si</td>
      <td>0.09</td>
      <td>0.02</td>
      <td>0.04</td>
      <td>0.03</td>
      <td></td>
    </tr>
    <tr>
      <td rowspan="2">VBM</td>
      <td>Os</td>
      <td>0.71</td>
      <td>0.01</td>
      <td>0.03</td>
      <td>0.67</td>
      <td>0</td>
    </tr>
    <tr>
      <td>Si</td>
      <td>0.14</td>
      <td>0.02</td>
      <td>0.07</td>
      <td>0.05</td>
      <td></td>
    </tr>
  </tbody>
</table>

## CONCLUSIONS

In this study, we examined the electronic structures of semiconducting metal silicides based on the first principles calculations. To examine the potential capability of the silicides as silicon-based light emitting materials, we calculated the values of oscillator strength of interband transition. In our results, Ru$_2$Si$_3$ and Ca$_2$Si have the direct gaps at $\Gamma$ points, however the transitions are forbidden. Among the examined silicides, OsSi was predicted to be the most feasible light emitting material. The oscillator strength between CBM and VBM at X point was evaluated to be 0.3 with the transition energy of 0.42 eV.

Even if the band transition is forbidden within the electric dipole approximation, the band transition may occur with the help of such mechanisms as magnetic dipole, electric quadrupole, and higher order transitions. However, in general, contribution of such effects to the oscillator strength is small.

At last we comment that this study does not deny the feasible capability of efficient light emission in silicides with the help of defects and other mechanisms.

## ACKNOWLEDGEMENTS
We thank Prof. C. Ambrosch-Draxl of Univ. Graz for useful comments.

## REFERENCES
1. C.B. Vining, in *Proceedings of the 9th International Conference on Thermoelectrics*, edited by C.B. Vining (California Institute of Technology, Pasadena 1991), p. 249.
2. D. Leong, M. Harry, K.J. Reeson, and K.P. Homewood, Nature, **387**, 686 (1997).
3. H. Lange, W. Henrion, B. Selle, G.-U. Reinsperger, G. Oertel, and H. von Känel, Appl. Surf. Sci. **102**, 169 (1996).
4. M. Tanaka, Y. Kumagai, T. Suemasu, and F. Hasegawa, Jpn. J. Appl. Phys. **36**, 3620 (1997).
5. S.J. Clark, H.M. Al-Allack, S. Brand, and R.A. Abram, Phys. Rev. B **58**, 10389 (1998).
6. M.C. Bost and J.E. Mahan, J. Appl. Phys. **63**, 839 (1988).
7. R.G. Long, M.C. Bost, and J.E. Mahan, Thin Solid Films **162**, 29 (1988).
8. M.C. Bost and J.E. Mahan, J. Vac. Sci. Technol. B **4**, 1336 (1986).
9. H. Lange, W. Henrion, E. Jahne, M. Giehler, O. Günther, and J. Schumann, Mat. Res. Soc. Proc. **320**, 479 (1994).
10. G.V. Samsonov, *Plenum Press Hand Books of High-Temperature Materials No. 2 - Properties Index*, (Plenum, New York, 1964).
11. L. Schellenberg, H.F. Braun, and J. Muller, J. Less-Common Met. **144**, 341 (1988).
12. W. Wolf, G. Bihlmayer, and S. Blügel, Phys. Rev. B **55**, 6918 (1997).
13. A.B. Filonov, D.B. Migas, V.L. Shaposhnikov, N.N. Dorozhkin, V.E. Borisenko, and H. Lange, Appl. Phys. Lett. **70**, 976 (1997).
14. P.Y. Dusausoy, J. Protas, R. Wandji, and B. Roques, Acta Cryst. B **27**, 1209 (1971).
15. L.F. Mattheiss, Phys. Rev. B **43**, 12549 (1991).
16. T. Siegrist, F. Hulliger, and G. Travaglini, J. Less-Common Met. **92**, 119 (1983).
17. D.J. Poutcharovsky and E. Parthe, Acta Cryst. B **30**, 2692 (1974).
18. W.L. Korst, L.N. Finnie, and A.W. Searcy, J. Phys. Chem. **61**, 1541 (1957).
19. I. Engström, Acta Chem. Scandinavica, **24**, 2117 (1970).
20. B. Lebech, J. Bernhard, and T. Freltoft, J. Phys. : Condens. Mat. **1**, 6105 (1989).
21. G. Brauer and H. Haag, Zeitschrift fuer Anorg. Alleg. Chem. **267**, 198 (1952).
22. I. Engström, T. Lindsten, and E. Zdansky, Acta Chem. Scandinavica, Series A, **41 A**, 237 (1987).
23. J.G. Barlock and L.F. Mondolfo, Zeitschrift fuer Met. **66**, 605 (1975).
24. G. Bruzzone and Franceschi, J. Less-Common Met. **57**, 210 (1978).
25. H. Schäfer, K.H. Janzen, and A. Weiss, Angewandte Chem. Internat. ed. **2**, 393 (1963).
26. P. Blaha, K. Schwarz, and J. Luitz, WIEN97, *A Full Potential Linearized Augmented Plane Wave Package for Calculating Crystal Properties*, (Karlheinz Schwarz, Techn. Univ. Wien, Vienna 1999); Updated version of P. Blaha, K. Schwarz, P. Sorantin, and S. B. Trickey, Comp. Phys. Commun. **59**, 399, (1990).
27. M.P.C.M. Krijn and R. Eppenga, Phys. Rev. B, **44**, 9042 (1991).
28. F. Aymerich and G. Mula, Phys. Stat. Sol. (b), **42**, 697 (1970).
29. R. Eppenga, J. Appl. Phys. **68**, 3027 (1990).
30. H.W.A.M. Rompa, R. Eppenga, and M.F.H. Schuurmans, Physica, **145B**, 5 (1987).

220