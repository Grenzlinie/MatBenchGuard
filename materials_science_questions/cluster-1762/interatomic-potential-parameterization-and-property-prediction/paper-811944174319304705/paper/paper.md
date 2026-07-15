![](./images/811944174319304705_1.jpg)

Available online at www.sciencedirect.com

![](./images/811944174319304705_2.jpg)

Chemical Physics Letters 453 (2008) 167-172

![](./images/811944174319304705_3.jpg)

www.elsevier.com/locate/cplett

# The mechanism of the displacive phase transition in vanadium dioxide

## Scott M. Woodley

Davy Faraday Research Laboratory, 3rd Floor, Kathleen Lonsdale Building, Gower Street, University College London, London WC1E 6BT, United Kingdom

Received 12 December 2007; in final form 7 January 2008
Available online 11 January 2008

### Abstract

The mechanism of the displacive phase transition in $\mathrm{VO}_{2}$ is unravelled through mapping of the *free energy* over the space spanned by two soft phonon modes. These modes crucially describe two independent Peierls distortions along chains of edge-sharing $\mathrm{VO}_{6}$ octahedra, which transform the tetragonal into the monoclinic phases on cooling. Calculation of potential energy employs our successful model of interatomic potentials, as current *ab-initio* calculations are intractable. The free energy is calculated within the quasi-harmonic approximation with thorough sampling of the Brillouin zone. Main experimentally observed features of this first order transition are reproduced, including the critical temperature.

© 2008 Elsevier B.V. All rights reserved.

## 1. Introduction

The material vanadium dioxide undergoes a first order phase transition, from a high temperature metallic phase (labelled R) to a low temperature semiconducting phase (labelled $M_{1}$). The underlying atomic and electronic transformations remain a topic of lively debate. The critical phase transition temperature, $T_{\mathrm{c}}$, was first reported in 1959 [1] to be around 340 K upon cooling, whereas upon heating the conductivity measurements indicated the onset of a phase change at around 335 K. More recently, as there is a rapid transition between the two phases, $\mathrm{VO}_{2}$ was selected as an ideal candidate for direct imaging (and diffraction) using 4D ultra-fast electron microscopy with combined spatial and temporal resolutions [2]. The critical temperature, $T_{\mathrm{c}}$, is also tuneable over a wide range by doping, for example, with tungsten, and so the study of $\mathrm{VO}_{2}$ is interesting not only from the fundamental point of view, but also for potential applications, as thermochromics, temperature sensing devices, as modulators and polarisers of submillimetre wave radiation, as an optical data storage medium, and as variable reflectance mirrors.

Complementing experimental studies, since 1959, there have been numerous computational studies [3-9], particularly at an electronic level, with the aim of addressing the cause of the transition [10] and whether the low temperature phase is a Mott-Hubbard [4], spin-Peierls [11,12] or an ordinary band (Peierls) [13,14] insulator. In this Letter, a computational study of the $\mathrm{VO}_{2}$ phase transition, on an atomistic level, is reported. Even though no explicit redistribution of the electrons near the Fermi level has been modelled, we were still able to gain new insight into the mechanism of this displacive transition from our simulations and, remarkably, to predict a reasonable value (compared with that observed) for $T_{\mathrm{c}}$ from our free energy calculations.

Both the $\mathrm{R}$ and $\mathrm{M}_{1}$ phase of $\mathrm{VO}_{2}$ can be visualized as being constructed from $\mathrm{VO}_{6}$ octahedra; along the $c$ direction (see Fig. 1) the octahedra are edge sharing and form parallel one-dimensional (1D) chains, and the remaining oxygen vertices are corner shared, so that the 1D chains are interconnected. The more symmetrical (tetragonal as opposed to monoclinic), high temperature phase, $\mathrm{R}$, adopts the rutile structure, which has one unique $\mathrm{V}-\mathrm{V}$ distance, $D_{\mathrm{M}}$, between neighbouring vanadium atoms. To obtain the low temperature monoclinic phase, $M_{1}$, the rutile phase is distorted and characterized by alternating short and long $\mathrm{V}-\mathrm{V}$ nearest neighbour separation distances, $D_{\mathrm{S}}$ and $D_{\mathrm{L}}$,

E-mail address: Scott.Woodley@ucl.ac.uk

0009-2614/$ - see front matter © 2008 Elsevier B.V. All rights reserved.
doi:10.1016/j.cplett.2008.01.018

![](./images/811944174319304705_4.jpg)

Fig. 1. Two phases of VO₂: (a) rutile phase where the monoclinic unit cell is indicated using a broken grey line, and where arrows indicate atom displacements for one of the phonon eigenvectors; (b) Monoclinic phase where the larger balls represent the cations and sticks connecting cations indicate a short V–V distance.

along the 1D chains (Peierls distortion). In addition, the ions are no longer collinear on the c-axis: as discussed below, for simple electrostatic reasons V–V pairs in one chain rotate as a direct consequence of Peierls distortion along neighbouring chains [15]. The rotations have been proposed as a direct cause of electron and spin localization and used in the argument in support of the Mott-Hubbard nature of the transition. As a consequence of defining a monoclinic unit cell containing four vanadium cations (and eight oxygen anions) that form segments from two parallel chains, there are four equivalent ways to draw the structure of the low temperature phase (begin alternating sequences with a short V–V distance in both, one or the other, and neither chains). Thus, there are four different, but equivalent, directions in which the atoms can be displaced in order to obtain M₁ from the rutile structure.

On applying a small uniaxial pressure along the (110) direction of the rutile phase, it has been reported [16] that only half of the 1D chains undergo a Peierls distortion (with V–V pairs in the other chains rotating). This monoclinic phase, labelled M₂, can also be obtained by doping VO₂ with very small quantities of chromium (V₁₋ₓCrₓO₂, x > 0.003) [17]. The distortion from R to M₁ can be described as the superposition of the distortions required to go from R to two equivalent M₂ structures with equal weight. As there is a total of four equivalent M₂ structures, there are four equivalent M₁ structures.

In this Letter, we report a model for VO₂, from which we are able to; (a) gain new insight into the mechanism of the R to M phase transition and (b) calculate the critical temperature.

## 2. Order parameters: defining the potential energy surface

To compute the lattice energy, we assume it is sufficient to include only two-body interactions between ions. As typically employed for modelling oxides at the atomistic level, the Buckingham potential is used to describe the short-range interactions, V–O and O–O, and the Shell Model is used for the oxygen anions [18]. To model both phases of pure VO₂, R and M₁, it is important to reproduce the qualitative difference in the interatomic V–V distances along the 1D chains. To provide the driving force for the observed Peierls distorted chains, a Morse potential is used for the metal–metal interactions of the vanadium cations.

<table>
<caption>Table 1<br>Interatomic potentials parameters, where the harmonic spring constant between each oxygen shell, Oᵟ⁻, and core, Oᶜ⁺, pair is 9.85 keV Å⁻², and the charges are q = 2.2|e|, c = 0.12|e| and s = 1.22|e|</caption>
<thead>
<tr>
<th>Interaction</th>
<th>A(eV)</th>
<th>ρ (Å)</th>
<th>C (eV Å⁶)</th>
</tr>
</thead>
<tbody>
<tr>
<td>Vᵠ⁺–Oᵟ⁻</td>
<td>15585.5</td>
<td>0.1941</td>
<td>27.25</td>
</tr>
<tr>
<td>Oᵟ⁻–Oᵟ⁻</td>
<td>23090.8</td>
<td>0.2342</td>
<td>29.80</td>
</tr>
<tr>
<td></td>
<td>D (eV)</td>
<td>α (Å⁻¹)</td>
<td>rₒ (Å)</td>
</tr>
<tr>
<td>Vᵠ⁺–Vᵠ⁺</td>
<td>0.5270</td>
<td>11.720</td>
<td>2.620</td>
</tr>
</tbody>
</table>

For details of derivation see Ref. [20].

The parameters of the interatomic potentials are given in Table 1.

As implemented within the General Utilities Lattice Package, (GULP) [19], standard optimisation techniques were employed to minimize the lattice energy by relaxing the structural parameters. The maximum difference between simulated and observed lattice parameters of the R and $M_1$ phases of $VO_2$ was within 2.7%, and the difference in the lattice energy between the two phases was predicted to be 0.024 eV per $VO_2$ formula unit [20].

From the derivatives of the lattice energy, the phonon structure for both phases can be calculated [21]. In our model, the high temperature phase, R, sits within a shallow energy minimum and has two phonon modes that become soft upon distortion towards phase M, whereby the main movement is that of the vanadium ions (Peierls distortion). The direction of these modes, as found by diagonalisation of the dynamical matrix, may not be ideal for our purpose: at R these modes are degenerate and therefore a more suitable choice can be made. First we determined directions of the shallowest ascent on the energy landscape spanned by these two soft modes near R. Careful search along a circular path, a short distance from R, revealed two such orthogonal directions, which we label $\mathbf{e}_1$ and $\mathbf{e}_2$. Using arrows to indicate the direction and magnitude of atomic displacements, one of these vibrational modes is shown in Fig. 1a. Clearly, half of the chains undergo a Peierls distortion, whilst in the other chains the vanadium ions move in an orthogonal direction to the chains. The two different distortions are coupled so that vanadium ions in neighbouring chains avoid each other. The second mode is simply the reverse: chains that previously did not undergo Peierls distortions now do and vice versa. More importantly, breaking symmetry along the initial lowest energy path has created $M_2$ rather than $M_1$ phase.

The two phonon eigenvectors, $\mathbf{e}_1$ and $\mathbf{e}_2$ can be defined using fractional coordinates with respect to a monoclinic cell. We define order parameters [22], $L_1$ and $L_2$, to be the magnitude of the distortion along vectors $\mathbf{e}_1$ and $\mathbf{e}_2$. Note that the high temperature phase, R, is now defined as $L_1 = L_2 = 0$, and the low temperature phase, $M_1$, is a minimum on the energy landscape in the direction $|L_1| = |L_2| > 0$.

Choosing values for $L_1$ and $L_2$, and relaxing only the lattice parameters and positions of the shells on the oxygen anions (during lattice vibrations, the shells are assumed to move/relax instantaneously, thus, including electronic polarization effects), we have mapped the lattice energy from R and out beyond the four equivalent $M_1$ phases, as shown in the upper panel of Fig. 2. As expected, coordinates of the global minima, $(L_1, L_2)$, represent the four low temperature phases, and the lattice energy surface rises rapidly further out (where the Peierls distortion is beyond that observed). As mentioned above, R is located within a very shallow basin on top of the central hill. In the discussion that immediately follows, it is instructive to consider all points within this basin (accessible, or ergodic, region of R) to represent the high temperature, rutile phase.

As well as mapping the lattice energy we also map the volume and lattice parameters for the monoclinic cell as a function of $L_1$ and $L_2$, and thus gain an insight into, or predict, the mechanism of the displacive phase transition. From the map of the volume landscape, shown in Fig. 3, we see that immediately outside the ergodic region of R the volume drops dramatically. Thereafter there is a gradual and continuous increase in the volume in all directions. Looking more closely, the ascent is steepest in the directions through $M_1$ and least steep in the directions through $M_2$. We find the dramatic reduction in the unit cell volume during the phase change, from R to M, to arise from the large contraction in $c$, which is accompanied by a smaller expansion in $a$; see upper panels of Fig. 3. The displacive phase transition from R to M essentially requires a large contraction along, and an expansion perpendicular to, the 1D edge sharing octahedra chains, which gradually reverts upon further increase of the Peierls distortion.

Consider the direct structural transformation between two equivalent $M_2$ phases, in which $L_1 = 0$ in one and $L_2 = 0$ in the other. This transition passes through an inversion point ($L_1 = L_2$, or $M_1$). The unit cell volume and $c$ (a measure of the period length of the chains) have a minimum at $M_1$ and a maximum at $M_2$, whereas for $a$ (a measure of the period length between chains), it is the reverse: maximum at $M_1$ and minimum at $M_2$. For $b$ (which has a component of both $a$ and $c$), we predict a local minimum for both $M_1$ and $M_2$.

Upon adding the zero point energy contribution to the lattice energy surface, there are three qualitative changes: there is no longer a local minimum at the centre. Each of the four equivalent global minima splits into two equivalent minima on the internal energy landscape, i.e. the magnitude of the Peierls distortion along the two neighbouring 1D chains for the low temperature phase is predicted to be slightly different. As either chain is just as likely to have a smaller distortion ($L_1 > L_2$ or $L_2 > L_1$), averaging, or as an effect of disorder, will of course give $L_1 = L_2$. Finally, there is a discontinuity in the landscape, separating R from M: the central region representing the high temperature phase, and the outer region – the low temperature phase. Thus, the displacive phase transition, R to M, is a first order phase transition.

## 3. Critical temperature: obtained from free energy calculations

For a quasi-harmonic model, the phonon free energy of a set of harmonic vibrations, $\omega_k$, is defined by the standard expression [22]:

$$
k_{\mathrm{B}} T \sum_{k} \ln \left[2 \sinh \left(\frac{\hbar \omega_{k}}{2 k_{\mathrm{B}} T}\right)\right] \tag{1}
$$

where $T$ is the temperature; $k_{\mathrm{B}}$ is the Boltzmann constant and $\hbar$ is the reduced Planck constant. By excluding the

![](./images/811944174319304705_5.jpg)

Fig. 2. Lattice energy and free energy ($T=0$ K) landscapes (eV per monoclinic unit cell) landscape with contours shown beneath, as a function of order parameters $L_1$ and $L_2$ (see text).

contribution of the soft modes to the summation, we have calculated the corresponding free energy, which, in Fig. 4, is mapped over $(L_1, L_2)$ for several temperatures (the total free energy is then the integral over an ergodic region on this landscape). Note that in our summation we use $8\times8\times8$ Monkhorst-Pack grid [23] in the first Brillouin zone. By choosing not to extend the map too far beyond $\text{M}_1$, as we did in Fig. 2, we have increased the resolution and highlighted that at low temperatures, for example 10 K, the global minimum, $\text{M}_1$, on this free energy surface is slightly off the symmetry lines $|L_1|=|L_2|$, and the local minimum within the local region of R, is actually a continuous ring, centred at $L_1=L_2=0$. The ergodic region of R is a ring, or annulus. Thus, if R could be obtained at lower temperatures, we predict that R is not a static, perfect rutile phase ($L_1=L_2=0$) but contains very small Peierls distortions that average out to give the appearance of a perfect rutile phase. At higher temperatures, the diameter of the inner radius of the annulus decreases, until it eventually disappears.

Following the approach of Landau's theory of second order phase transition, consider a single order parameter example where the $T=0$ free energy landscape is a simple 1D double well potential. The two local minima represent the degenerate low temperature phases and the local maximum the high temperature phase. At higher temperatures, the height of the central hill decreases. At the temperature when the double well disappears, $T$ is the critical phase transition temperature, $T_\text{c}$, see for example Ref. [22]. The free energy landscapes for $\text{VO}_2$ are much more complex, however, a similar trend with respect to $T$ is found, and a similar approach for predicting $T_\text{c}$ can be applied. In Fig. 4, with respect to the outer monoclinic region, we can see that the ergodic region of R lowers with increasing $T$. Also, the two local regions for each $\text{M}_1$ (seen clearly on the contour maps for $T=10$, 100 and 200 K) merge into

![](./images/811944174319304705_6.jpg)

Fig. 3. Lattice parameters (Å) and unit cell volume ($\text{\AA}^3$) landscapes with contours shown beneath, as a function of order parameters $L_1$ and $L_2$ (see text).

![](./images/811944174319304705_7.jpg)

Fig. 4. Free energy landscapes (eV per monoclinic unit cell) at various temperatures, $T$, with contours shown beneath, as a function of order parameters $L_1$
and $L_2$ but with a range reduced by one third from that used in Fig. 2 (see text).

![](./images/811944174319304705_8.jpg)

Fig. 5. Difference in the free energy for the rutile and monoclinic phases at various temperatures.

one ergodic region (V-shaped valley) as $T$ increases beyond 200 K. Plotting, as a function of temperature, the difference in the local minima for each phase, R and $M_1$, on the surfaces shown in Fig. 4, we predict a critical phase temperature of approximately 300 K, see Fig. 5.

### 4. Conclusion

From a simple interatomic potential model, the transition between the low temperature phase, R, and high temperature phase, $M_1$, is predicted to be of first order, $T_c=300$ K compared to 340 K observed. Moreover, the mechanism is shown to be one of contracting the 1D chains along which Peierls distortions occur (and expanding the crystal structure perpendicular to the direction of these chains) and that half the chains are likely to distort slightly out of phase. From the free energy calculations, we predict that the low temperature monoclinic $M_1$ phase has a small component of $M_2$, i.e. the extent of the Peierls distortions in the chains varies between neighbouring chains. As well as investigating the thermodynamic properties of $VO_2$, we are currently improving our interatomic potential model to include an explicit account of Jahn Teller distortions about the open shell cations. Furthermore, the method is developed to relax the structures under the constraint of certain eigenvector displacements to be frozen.

### Acknowledgements

This work was supported by EPSRC (portfolio grant EP/D504872). Molecular graphics was produced using software provided by Accelrys, and the figures were created using Gnuplot. I warmly acknowledge key discussions about this work with colleagues Christian Schön (Max- Planck Institute, Stuttgart), Makondelele Netsianda and Phuti Ngoepe (University of Limpopo, South Africa), and Alexey Sokol, Richard Catlow and Sir John Meurig Thomas (DFRL).

### References

[1] F.J. Morin, Phys. Rev. Lett. 3 (1959) 34.
[2] M.S. Grinolds, V.A. Lobastov, J. Weissenrieder, H.A. Zewai, Proc. Natl. Acad. Sci. USA 103 (2006) 18427.
[3] J.B. Goodenough, J. Solid State Chem. 3 (1971) 490.
[4] A. Zylbersztejn, N.F. Mott, Phys. Rev. B 11 (1975) 4383.
[5] N.F. Mott, Metal-Insulator Transitions, Taylor & Francis, London, 1990.
[6] R.M. Wentzcovitch, W.W. Schulz, P.B. Allen, Phys. Rev. Lett. 72 (1994) 3389.
[7] V. Eyert, Ann. Phys. Leipzig 11 (2002) 9.
[8] S. Biermann, A. Poteryaev, A.I. Lichtenstein, A. Georges, Phys. Rev. Lett. 94 (2005) 026404.
[9] T.C. Koethe et al., Phys. Rev. Lett. 97 (2006) 116402.
[10] M. Imada, A. Fujimori, Y. Tokura, Rev. Mod. Phys. 70 (1998) 1039.
[11] D. Paquet, P. Leroux-Hugon, Phys. Rev. B 22 (1980) 5284.
[12] J. Shi, R. Bruinsma, A.R. Bishop, Synth. Met. 41 (1991) 3527.
[13] D. Adler, H. Brooks, Phys. Rev. B 155 (1967) 826.
[14] J.B. Goodenough, Phys. Rev. 117 (1960) 1442.
[15] See, for example M.D.B. Marezio, J.P. McWhan, P.D. Dernier, Phys. Rev. B 5 (1972) 2541.
[16] J.P. Pouget, H. Launois, J.P. D'Haenens, P. Merender, T.M. Rice, Phys. Rev. Lett. 35 (1975) 873.
[17] J.P. Pouget, H. Launois, T.M. Rice, P. Dernier, A. Gossard, G. Villeneuve, P. Hagenmuller, Phys. Rev. B 10 (1974) 1801.
[18] See, for example C.R.A. Catlow, W.C. MackrodtComputer Modelling of Solids, Lecture Notes in Physics, vol. 166, Springer, Berlin, 1982.
[19] J.D. Gale, A.L. Rohl, Mol. Simul. 29 (2003) 291.
[20] M. Netsianda, P.E. Ngoepe, C.R.A. Catlow, S.M. Woodley, Chem. Mat., in press.
[21] See, for example M.T. Dove, Introduction to Lattice Dynamics, University Press, Cambridge, 1993.
[22] M.T. Dove, Am. Mineral. 82 (1997) 213.
[23] H.J. Monkhorst, J.D. Pack, Phys. Rev. B 13 (1976) 5188.