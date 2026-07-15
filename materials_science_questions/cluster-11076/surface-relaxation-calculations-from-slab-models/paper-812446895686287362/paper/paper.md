# Calculation of surface energies for low index planes of diamond

Timur Halicioglu

Department of Materials Science and Engineering, Stanford University, Stanford, California 94305, USA

Received 8 July 1991; accepted for publication 28 August 1991

Surface energies were estimated for diamond (100), (110) and (111) planes in $(1 \times 1)$ patterns, using a molecular dynamics technique. For comparison calculations were carried out considering two different recently developed model functions for carbon. Both functions produced comparable results and for completely equilibrated systems calculated surface energy values were found to decrease going from $(100) \rightarrow(110) \rightarrow(111)$, as anticipated. In all cases, a multilayer relaxation was found to be taking place during the equilibration procedure. Results indicate that for all three index planes, the top interlayer spacings contract while the second interlayer spacings exhibit an expansion. Percentage-wise the largest multilayer relaxation was found for the (111) surface.

Due to the increasing interest in diamond coatings and thin film industry today, a detailed understanding of energy- and structure-related properties of diamond surfaces is highly desired. Most of the experimental and theoretical studies in this area deal with the reconstructed (111) surface of diamond. While some investigations are available for the (100) plane, studies on the (110) plane are extremely scarce [1-7]. In this study, simulation calculations were carried out to investigate surface energy and structural features for these three low index planes of diamond. Calculations were performed employing a molecular dynamics technique based on model potential functions of carbon. For comparison, two different types of model functions, recently developed for carbon, were taken into consideration. The first potential is the Tersoff function which has 11 parameters and accurately describes many properties of the diamond crystal [8]. Furthermore, this function can also reproduce several properties of an individual basal plane of graphite. Using the Tersoff function the total potential energy of a system of $N$ particles is expressed as a sum over atomic sites of the form:

$$
E=\sum_{i}^{N} \Phi_{i}
\tag{1}
$$

with

$$
\Phi_{i}=\frac{1}{2} \sum_{j(\neq i)}^{N} f_{\mathrm{c}}\left(r_{i j}\right)\left[V_{\mathrm{R}}\left(r_{i j}\right)-b_{i j} V_{\mathrm{A}}\left(r_{i j}\right)\right],
\tag{2}
$$

where, $r_{i j}$ denotes the internuclear distance and $f_{\mathrm{c}}\left(r_{i j}\right)$ represents the cut-off function which is given by:

$$
f_{\mathrm{c}}\left(r_{i j}\right)=\left\{\begin{array}{c}
1 \quad \text { if } r_{i j}<R-D ; \\
\frac{1}{2}-\frac{1}{2} \sin \left[\frac{\pi}{2}\left(r_{i j}-D\right) / D\right] \\
\quad \text { if } R-D<r_{i j}<R+D ; \\
0 \quad \text { if } r_{i j}>R+D .
\end{array}\right.
\tag{3}
$$

The three-body part of the interactions is introduced via the function $b_{i j}$, while $V_{\mathrm{R}}$ and $V_{\mathrm{B}}$ represent repulsive and attractive parts, respectively. These functions were defined by Tersoff as:

$$
V_{\mathrm{R}}\left(r_{i j}\right)=A \exp \left(-\lambda_{1} r_{i j}\right),
$$

$$
V_{\mathrm{A}}\left(r_{i j}\right)=B \exp \left(-\lambda_{2} r_{i j}\right),
$$

$$
b_{i j}=\left(1+\beta^{n} \xi_{i j}^{n}\right)^{-1 / 2 n},
$$

$$
\xi_{i j}=\sum_{k(\neq i, j)}^{N} f_{\mathrm{c}}\left(r_{i k}\right) g\left(\theta_{i j k}\right) \exp \left[\lambda_{3}^{3}\left(r_{i j}-r_{i k}\right)^{3}\right],
$$

$$
g\left(\theta_{i j k}\right)=1+c^{2} / d^{2}-c^{2} /\left[d^{2}+\left(h-\cos \theta_{i j k}\right)^{2}\right].
$$

For carbon the Tersoff parameters are given as: $A = 1393.6$ eV, $B = 346.74$ eV, $\lambda_1 = 3.4879$ Å, $\lambda_2 = 2.2119$ Å, $\beta = 1.5724 \times 10^{-7}$, $n = 0.72751$, $c = 38049$, $d = 4.3484$, $h = -0.57058$, $R = 1.95$ Å and $D = 0.15$ Å.

The second potential used in this study is due to Brenner [9]. It is analytically similar to the Tersoff function given by eqs. (1) and (2). Brenner employed a different set of parameters for the function and successfully calculated various properties of diamond as well as the graphitic plane. Furthermore, this function was shown to produce acceptable results for some properties of small carbon clusters [10]. The same cut-off function (eq. (3)) was also employed by Brenner. Although analytically equivalent, functional forms for $b_{ij}$, $V_{\text{R}}$ and $V_{\text{A}}$ were defined somewhat differently by Brenner:

$$
V_{\text{R}}(r_{ij}) = \frac{D_{\text{e}}}{(S-1)} \exp\left[ -\beta\sqrt{2S}\left(r_{ij} - r_{\text{e}}\right) \right],
$$

$$
V_{\text{A}}(r_{ij}) = \frac{SD_{\text{e}}}{(S-1)} \exp\left[ -\beta\sqrt{2/S}\left(r_{ij} - r_{\text{e}}\right) \right],
$$

$$
b_{ij} = \left(1 + z_{ij}\right)^{-n},
$$

where,
$$
z_{ij} = \sum_{k(\neq i,j)}^{N} f_{\text{c}}(r_{ik}) g(\theta_{ijk}) \exp\left[ m(r_{ij} - r_{ik}) \right],
$$

$$
\begin{aligned}
g(\theta_{ijk}) &= \alpha\bigg\{ 1 + c^2/d^2 - c^2 \\
&\quad \bigg/ \left[ d^2 + \left(h + \cos \theta_{ijk}\right)^2 \right] \bigg\}.
\end{aligned}
$$

For carbon Brenner used the following set of values for the parameters: $D_{\text{e}} = 6.325$ eV, $r_{\text{e}} = 1.28$ Å, $\beta = 1.5$ Å$^{-1}$, $S = 1.29$, $n = 0.8047$, $\alpha = 0.0113$, $c = 19.0$, $d = 2.5$, $h = 1.0$, $m = 2.25$ Å$^{-1}$, $R = 2.1$ Å and $D = 0.2$ Å.

In this study, calculations were carried out using a molecular dynamics technique based on a modified Verlet algorithm [11]. The temperature of the system was scaled to 100 K throughout this study. In all cases, calculations were performed with a time step of $0.5 \times 10^{-17}$ s. For the first 5000 time steps the temperature of the system was rescaled to help the system reach equilibrium at the desired temperature. In general, equilibration runs were carried out up to 10 000 steps and averaged values for the energy and temperature were calculated for every 1000 time steps. In all cases the average value of the total energy remained constant during the equilibration period. The surface energy, $\gamma_{\text{e}}$, is calculated as;

$$
\gamma_{\text{e}} = \frac{E_{\text{s}} - E_{\text{b}}}{\mathscr{A}}
$$

where, $E_{\text{b}}$ represents the total energy for the bulk with no surface and $E_{\text{s}}$ is the total energy of the same system with an exposed surface. The total area of the exposed surface is denoted by $\mathscr{A}$. The value of $E_{\text{b}}$ was calculated considering periodic boundary conditions imposed on the system in all three directions ($x$, $y$, and $z$). In calculating $E_{\text{s}}$, on the other hand, the periodic boundary condition in one of the directions (i.e., $z$-direction) was removed to provide an exposed surface for the correctly oriented system producing the desired surface plane. Computational cells for simulating (100), (110) and (111) planes, contained 64, 96 and 128 carbon atoms, respectively. Due to the short range nature of potential functions employed in this study, increasing the size of the computational cell did not produce any change in the calculated energy values.

Surfaces were generated as an abrupt termination of the bulk for the desired plane. First, unrelaxed surface energies were calculated for all three index planes. In this case, all C-C distances were fixed and kept equal to bulk diamond C-C distances, and values of $E_{\text{s}}$ and $E_{\text{b}}$ were estimated for fixed positions of atoms. In calculating relaxed values for $E_{\text{s}}$ and $E_{\text{b}}$, on the other hand, the unrelaxed structures were employed as initial configurations and then, each atom in the system was permitted to move an equilibrate under the molecular dynamics code. In this case, average values for $E_{\text{s}}$ and $E_{\text{b}}$ were used to estimate surface energies. Relaxed and unrelaxed surface energies calculated using the Tersoff and Brenner functions are given in table 1 for three different index planes of diamond. Computational cell sizes in these calculations were chosen to satisfy minimum energy conditions for corresponding potential functions. While the Tersoff function

<table><caption>Table 1 Surface energies, $\gamma_{\mathrm{e}}$, for low index planes of diamond calculated before and after relaxation (at $\approx 100$ K) (calculations were carried out using Tersoff and Brenner potentials at their equilibrium lattice dimensions)</caption>
<tbody><tr><th></th><th>Index plane</th><th>$\gamma_{\mathrm{e}}$ (erg/cm²) unrelaxed</th><th>$\gamma_{\mathrm{e}}$ (erg/cm²) relaxed</th></tr>
<tr><td>Tersoff</td><td>(100)</td><td>7565</td><td>6639</td></tr>
<tr><td></td><td>(111)</td><td>4040</td><td>2772</td></tr>
<tr><td></td><td>(110)</td><td>4949</td><td>4028</td></tr>
<tr><td>Brenner</td><td>(100)</td><td>6161</td><td>5026</td></tr>
<tr><td></td><td>(111)</td><td>2662</td><td>1390</td></tr>
<tr><td></td><td>(110)</td><td>3261</td><td>2020</td></tr>
</tbody></table>

satisfactorily reproduces the value of the experimental lattice constant for diamond at low temperatures, the lattice constant produced by the Brenner function at the energy minimum is about 3% shorter [9].

Surface energy values calculated by the Tersoff function are, in general, larger than values calculated by the Brenner potential. In both cases, however, results exhibit the same trend, the energy for the (100) surface is the largest, while the (111) surface has the smallest energy, as anticipated (see table 1). Reported values for diamond surface energy for different index planes are rather scarce. An early calculation of surface energy based on the broken bond concept (i.e., considering only pair interactions) has produced 9820 and 5650 erg/cm² for unrelaxed (100) and (111) planes, respectively [12]. These values are higher than unrelaxed surface energy values calculated here using model functions. In another study, using a different model function Takai et al. [13] calculated unrelaxed surface energies for (100) and (111) faces as 9207 and 3387 erg/cm², while relaxed energies have been reported as 3338 and 829 erg/cm², respectively. For the (100) surface these energy values display considerable deviations from the values calculated here. For the (111) plane, however, reported surface energies seem to be somewhat more consistent with the present results. Most probably these discrepancies are due to differences in functional forms of potentials employed in different calculations. In an earlier study it has been shown that the type of interactions is quite important in surface energy calculations [14]. Using a MINDO procedure, the relaxed surface energy for the (111) plane with $(1\times 1)$ pattern, has been calculated by Verwoerd and Kok [15] as 3591 erg/cm² which is also somewhat higher than the results obtained here. In this study, however, only four carbon atoms (attached to 9 hydrogen atoms) have been used to model (111) surface layers.

After the equilibration, surfaces for (100), (110) and (111) planes, were found to be in $(1\times 1)$ patterns displaying almost no surface reconstruction. However, present calculations (using both the Tersoff and Brenner functions) indicate that a considerable amount of layer-by-layer relax-

<table><caption>Table 2 Multilayer relaxation results for low index surface planes of diamond ($\delta_{12}$, $\delta_{23}$ and $\delta_{34}$ denote interplanar spacings between the first and second, second and third, and third and fourth atomic layers parallel to the exposed surface)</caption>
<tbody><tr><th></th><th></th><th colspan="3">Tersoff</th><th colspan="3">Brenner</th></tr>
<tr><th></th><th></th><th>(100)</th><th>(110)</th><th>(111)</th><th>(100)</th><th>(110)</th><th>(111)</th></tr>
<tr><td>Before relaxation</td><td>$\delta_{12}$</td><td>0.892</td><td>1.261</td><td>0.515</td><td>0.869</td><td>1.229</td><td>0.502</td></tr>
<tr><td></td><td>$\delta_{23}$</td><td>0.892</td><td>1.261</td><td>1.544</td><td>0.869</td><td>1.229</td><td>1.505</td></tr>
<tr><td></td><td>$\delta_{34}$</td><td>0.892</td><td>1.261</td><td>0.515</td><td>0.869</td><td>1.229</td><td>0.502</td></tr>
<tr><td>After relaxation</td><td>$\delta_{12}$</td><td>0.750</td><td>1.120</td><td>0.310</td><td>0.590</td><td>1.070</td><td>0.220</td></tr>
<tr><td></td><td>$\delta_{23}$</td><td>0.910</td><td>1.270</td><td>1.610</td><td>0.950</td><td>1.280</td><td>1.630</td></tr>
<tr><td></td><td>$\delta_{34}$</td><td>0.890</td><td>1.260</td><td>0.510</td><td>0.850</td><td>1.229</td><td>0.470</td></tr>
<tr><td>Per cent change</td><td>$\delta_{12}$</td><td>$-15.9$</td><td>$-11.2$</td><td>$-39.8$</td><td>$-32.1$</td><td>$-12.9$</td><td>$-56.2$</td></tr>
<tr><td></td><td>$\delta_{23}$</td><td>$+2.0$</td><td>$+0.7$</td><td>$+4.3$</td><td>$+9.3$</td><td>$+4.2$</td><td>$+8.3$</td></tr>
<tr><td></td><td>$\delta_{34}$</td><td>$-0.2$</td><td>$-0.1$</td><td>$-0.9$</td><td>$-2.2$</td><td>$0.0$</td><td>$-6.3$</td></tr>
</tbody></table>

ation for all three index planes, takes place dur- ing the equilibration. In such a multilayer relax- ation process, interlayer distances $\delta_{12}$, $\delta_{23}$, ... (denoting, respectively, separations between the first and second, the second and third, ... layers parallel to the exposed surface) vary during the equilibration, while atoms within planes exhibit negligible lateral motion. Relaxed surfaces dis- play alternating contractions and expansions for the top interlayer spacings in all cases. The first three interplanar distances for (100), (110) and (111) index planes are given in table 2 for unre- laxed and relaxed cases. Also included in table 2 are percentage changes in top interlayer spacings during the relaxation. For the multilayer relax- ation, the Brenner function produced higher per- centage values than the Tersoff function. The largest per cent relaxation takes place at the first interplanar spacing, $\delta_{12}$, which, in all cases, dis- plays a shrinkage. The second interplanar spac- ing, $\delta_{23}$, on the other hand, exhibited a modest expansion. The change in the third interplanar spacing, $\delta_{34}$, was found to be very small for the Tersoff potential, while for the Brenner function some amount of shrinkage was calculated for the (111) and (100) cases. For the first interlayer spacing, $\delta_{12}$, of the (111) plane a contraction of $-54.1\%$ has been reported by Verwoerd and Kok [15] which is in good agreement with the present result obtained by the Brenner function. Furthermore, in another study, a contraction of approximately $-20\%$ in the first interplanar sep- aration for the relaxed (111) surface of diamond, has been reported by Snyder and Wasserman [16]. In their study, they employed an SCF method and the (111) surface structure has been repre- sented also using four carbon and nine hydrogen atoms.

In the case of an ideal $(1\times 1)$ surface formed as an abrupt termination of the bulk, there is only one type of interplanar spacing for the (100) and (110) index planes (see table 2). However, when the diamond lattice is terminated on a (111) plane, the geometry is somewhat different. In this case, the atomic layers come in pairs and are best considered as puckered layers of upper and lower atoms that give rise to two different interlayer spacings. For an ideal case, the first interlayer spacing, $\delta_{12}$, is just $\frac{1}{3}$ of the second interlayer spacing, $\delta_{23}$, which is equal to the nearest neigh- bor distance in the crystal. Present calculations indicate that during relaxation the smaller inter- layer spacings, $\delta_{12}$, (and to some degree $\delta_{34}$) shrinks, while, the larger $\delta_{23}$ expands further. The shrinkage of the interlayer spacings, in the case of the puckered layer, can be regarded as the formation of a graphite-like layer at the ex- posed (111) surface. This result is in partial agreement with several experimental reports which suggest a spontaneous graphitization of the (111) surface upon cleaning [1,17].

At the temperature that calculations were car- ried out no high degree reconstructions due to lateral atomic motions were found for any of the surface planes investigated here. Both functions employed in this study produced rather compara- ble results. In all cases, a contraction for $\delta_{12}$ and an expansion for $\delta_{23}$ were found. Neither func- tion produced a complete graphitic layer at the exposed (111) surface of diamond. According to the present results, the exposed (111) surface preserves its diamond-like puckered layer charac- ter after equilibration.

This work was supported by a grant from NASA Ames Research Center to Eloret Institute (NCC 2-297).

## References
[1] B.B. Pate, Surf. Sci. 165 (1986) 83.
[2] G.D. Kubiak and K. Kolasinski, Phys. Rev. B 39 (1989) 1381.
[3] E.C. Sowa, G.D. Kubiak, R.H. Stulen and M.A. Van Hove, J. Vac. Sci. Technol. A 6 (1988) 832.
[4] A.V. Hamza, G.D. Kubiak and R.H. Stulen, Surf. Sci. 206 (1988) L833.
[5] A.V. Hamza, G.D. Kubiak and R.H. Stulen, Surf. Sci. 237 (1990) 35.
[6] F. Bechstedt and D. Reichardt, Surf. Sci. 202 (1988) 58.
[7] F. Bechstedt and D. Reichardt, Surf. Sci. 202 (1988) 83.
[8] J. Tersoff, Phys. Rev. Lett. 61 (1988) 2879.
[9] D.W. Brenner, Mater. Res. Soc. Symp. Proc. 141 (1989) 59.
[10] T. Halicioglu, Chem. Phys. Lett. 179 (1991) 159.
[11] D.J. Evans and G.P. Morris, Comput. Phys. Rep. 1 (1984) 297.

[12] A.W. Adamson, Physical Chemistry of Surface, 5th ed. (Wiley, New York, 1990) p. 298.

[13] T. Takai, T. Halicioglu and W.A. Tiller, Surf. Sci. 164 (1985) 341.

[14] J.N. Schmit, Surf. Sci., 55 (1976) 589.

[15] W.S. Verwoerd and F.J. Kok, Surf. Sci. 80 (1979) 89.

[16] L.C. Snyder and Z. Wasserman, Surf. Sci. 71 (1978) 407.

[17] E. Gaigher and W.S. Verwoerd, Surf. Sci. 103 (1981) 338.