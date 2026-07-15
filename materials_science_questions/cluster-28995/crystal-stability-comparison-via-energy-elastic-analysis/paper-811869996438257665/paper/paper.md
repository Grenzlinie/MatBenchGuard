# $^4$He on a Single Graphene Sheet

M. C. Gordillo
Departamento de Sistemas Físicos, Químicos y Naturales. Facultad de Ciencias Experimentales, Universidad Pablo de Olavide, Carretera de Utrera, km 1, 41013 Sevilla, Spain

J. Boronat
Departament de Física i Enginyeria Nuclear, Universitat Politècnica de Catalunya, B4-B5 Campus Nord, 08034 Barcelona, Catalonia. Spain

(Received 17 October 2008; revised manuscript received 30 January 2009; published 27 February 2009)

The phase diagram of the first layer of $^4$He adsorbed on a single graphene sheet has been calculated by a series of diffusion Monte Carlo calculations including corrugation effects. Since the number of C-He interactions is smaller than in graphite, the binding energy of $^4$He atoms to graphene is reduced approximately 13.4 K per helium atom. Our results indicate that the phase diagram is qualitatively similar to that of helium on top of graphite. A two-dimensional liquid film on graphene is predicted to be metastable with respect to the commensurate solid but the difference in energy between both phases is very small, opening the possibility of such a liquid film to be experimentally observed.

DOI: 10.1103/PhysRevLett.102.085303

PACS numbers: 67.25.dp, 05.30.Jp, 67.80.bd, 68.90.+g

Graphite is a well-known form of carbon, made of two-dimensional carbon layers glued to each other by interactions of dispersion type in the $z$ direction, and separated by a distance of $3.35$ Å. Within each of those two-dimensional layers the carbon atoms are located in the nodes of a honeycomb lattice, each of them being bound to three others by covalent interactions. Even though it is well known that to exfoliate graphite is relatively easy, the isolation of a single and stable two-dimensional sheet of carbon by mechanical cleavage was only reported recently [1,2]. This structure is termed graphene and it has been predicted to be unstable since the thermal fluctuations would make the crystal structure collapse [3]. However, the experiments show that at least it is kinetically stable [2]. This singular material has already attracted the attention of the scientific community, basically for its novel electrical properties [4–7].

In this work, we are interested in graphene as a new adsorber. Since graphite is a set of graphene layers, one would expect a difference in the binding energy of the adsorbed species that could lead to a change in their phase diagram. We have carried out this analysis for $^4$He in the limit of zero temperature, and studied the differences between graphene and graphite. To this end, we have performed diffusion Monte Carlo simulations of a system of $^4$He atoms adsorbed on top of a variable number of graphene layers, ranging from one to eight. This last number was found to be an acceptable model for graphite, since all the properties calculated were similar for eight and nine layers within the error bars obtained from the simulation data. The layers were supposed to be parallel to each other, separated by the typical graphite distance, and stacked in the $A$-$B$-$A$-$B$ way characteristic of this compound. The helium densities were kept within the limits of a first layer ($<0.12$ Å$^{-2}$ [8]).

We used diffusion Monte Carlo (DMC) simulations because with them you can obtain the true ground state for bosonic systems, such as a set of $^4$He particles [9] in the limit of 0 K. However, for the technique to work we have to provide a reasonable approximation for the ground-state wave function, what it is called the trial function. That collects all the information known *a priori* about the system. In this work, we used as a first trial wave function

$$
\Phi(\mathbf{r}_1, \mathbf{r}_2, \ldots, \mathbf{r}_{\rm N}) = \prod_{i<j}\exp\left[-\frac{1}{2}\left(\frac{b_{\rm He-He}}{r_{ij}}\right)^5\right] \prod_i \Psi(z_i), \quad (1)
$$

that depends on the coordinates of the helium atoms $r_1$, $r_2$, ..., $r_N$, and where the first term is the usual Jastrow function depending on the helium interatomic distances $r_{ij}$, with $b_{\rm He-He}=3.07$ Å [9]. For the second part of the wave function ($\Psi(z)$), we followed Withlock and collaborators [10], and solved the one-dimensional Schrödinger equation describing a single helium atom moving along the axis perpendicular to the graphene layers ($z$) for an averaged C-He potential that neglected corrugation. The one-body ground-state wave function obtained, $\Psi(z)$, is displayed in Fig. 1. The He-He potential was taken from Ref. [11] while the individual C-He interactions were assumed to be of Lennard-Jones type [12]. This means that in our many-body calculations the effects of carbon corrugation in the C-He interaction are fully considered.

Obviously, the former trial function (1) is an adequate representation for a system with translational invariance, i.e., a liquid. To do simulations for a solid, we multiply the previous $\Phi(\mathbf{r}_1, \mathbf{r}_2, \ldots, \mathbf{r}_{\rm N})$ (1) by a term of the form

$$
\prod_i \exp\left\{-a\left[(x_i-x_{\rm site})^2+(y_i-y_{\rm site})^2\right]\right\}, \quad (2)
$$

where $x_{\rm site}$, $y_{\rm site}$ are the coordinates of the crystallographical positions around which the $^4$He atoms are localized

![](./images/811869996438257665_1.jpg)

FIG. 1. Solution for the one-body Schrödinger equation describing a single $^4$He atom under an averaged C-He interaction in the $x$, $y$ plane. $z$ indicates distance to such plane, located at $z = 0$.

and $a$ is a constant variationally optimized. These positions were different for each of the solid phases considered: a commensurate $\sqrt{3} \times \sqrt{3}$, of surface density $0.0636$ $\mathring{\text{A}}^{-2}$ [13], a commensurate structure (7/16) reported by Corboz and co-workers [14] ($\rho = 0.0835$ $\mathring{\text{A}}^{-2}$), and three commensurate structures suggested to appear in the experimental phase diagram of graphite in Ref. [15] (2/5, $\rho = 0.0763$ $\mathring{\text{A}}^{-2}$; 3/7, $\rho = 0.0818$ $\mathring{\text{A}}^{-2}$; 31/75 $\rho = 0.0789$ $\mathring{\text{A}}^{-2}$). We also considered several triangular incommensurate solids of different densities, obtained by varying the helium-helium distance in the $x$, $y$ plane on the (outer) graphene sheet. The optimal values of the parameter $a$ in Eq. (2) are $a = 0.31$ $\mathring{\text{A}}^{-2}$ for all the commensurate structures, and range from $a = 0.15$ to $0.77$ $\mathring{\text{A}}^{-2}$ in the case of the incommensurate triangular structures. The quality of the different trial functions to describe the system can be ascertained by looking at the energy variances of every single calculation, in all cases of the order of 0.01–0.02 K.

Figure 2 displays the energy per $^4$He atom as a function of the helium density for the liquid phase and for the number of graphene layers ($n$) considered. The corresponding densities were obtained by varying the number of helium atoms on top of a fixed simulation cell, a rectangle of $34.43 \times 34.08$ $\mathring{\text{A}}^{2}$. The use of a simulation cell with different size or form did not change the results. We can see that there is a very small but significant difference between the binding energy values for $n = 4$ and $n = 8$ ($-142.37 \pm 0.01$ K versus $-142.69 \pm 0.01$ K), for the density corresponding to the minimum energy, $0.044$ $\mathring{\text{A}}^{-2}$. This equilibrium density is nearly equal to the one for purely two-dimensional liquid $^4$He ($0.043$ $\mathring{\text{A}}^{-2}$) [16]. The energy differences between structures with the same densities for eight and nine carbon sheets are below the corresponding error bars and therefore $n = 8$ can be considered the graphite limit. We also found that the curves are similar to each other, up to the point to nearly collapse in one single function when the differences in the infinite-dilution limit are corrected. The energies of the liquid phase at the equilibrium density are shown in Table I. The infinite-dilution energies were obtained from fittings to third-degree polynomials in the density range $\rho < 0.02$ $\mathring{\text{A}}^{-2}$. The binding energy of a single atom for $n = 8$ is fully compatible with the experimental data [17,18], and slightly different from the path integral Monte Carlo calculations of Ref. [19] ($-143.09 \pm 0.27$ K versus $-141.64 \pm 0.01$ K for the present work), probably because of the different C-He interactions used.

![](./images/811869996438257665_2.jpg)

FIG. 2. Energy per atom versus the density for a liquid phase of helium atoms on top of one or several graphene sheets. Open squares, $n = 1$; full squares, $n = 2$; open circles, $n = 3$; full circles, $n = 4$; open triangles, $n = 8$.

In the scenario described above the liquid is not the most stable phase at $T = 0$ K. The energies of the liquid phase at equilibrium for different values of $n$ are given in Table I, and can be compared with the binding energy for the $\sqrt{3} \times \sqrt{3}$ commensurate structure. The simulation of the $\sqrt{3} \times \sqrt{3}$ solid phase has been performed using 120 atoms in a $44.27 \times 42.60$ $\mathring{\text{A}}^{2}$ cell. In the Table, we can see that in all cases, commensurate solids are more bound, but admittedly for very small margins. The ground state of $^4$He on top of any graphene compound is the $\sqrt{3} \times \sqrt{3}$ registered phase. This result is stable within plausible uncertainties ($\sim$5%) of the C-He interaction energy scale ($\varepsilon$): we have verified that the liquid would appear as the stable phase by decreasing much more the energy $\varepsilon$ (20%). Our description of the phase diagram agrees with the path integral Monte Carlo one of Pierce and Manousakis [19,20] for graphite. However, the small difference between the energies of the liquid and commensurate phases makes also plausible the scenario given by Greywall and Busch [8], with a liquid phase of density $\sim 0.04$ $\mathring{\text{A}}^{-2}$ as a very close metastable state. In the densities between two stable struc-

<table>
<caption>TABLE I. Energy per atom, in K, for several helium arrangements. $n$ indicates the number of graphene layers considered. See further explanation in the text.</caption>
<thead>
<tr>
<th>$n$</th>
<th>Infinite dilution</th>
<th>Liquid</th>
<th>$\sqrt{3} \times \sqrt{3}$</th>
<th>Incommensurate</th>
</tr>
</thead>
<tbody>
<tr>
<td>1</td>
<td>$-128.26 \pm 0.04$</td>
<td>$-129.221 \pm 0.009$</td>
<td>$-129.282 \pm 0.007$</td>
<td>$-126.6 \pm 0.2$</td>
</tr>
<tr>
<td>2</td>
<td>$-139.02 \pm 0.01$</td>
<td>$-139.96 \pm 0.01$</td>
<td>$-140.067 \pm 0.009$</td>
<td>$-137.3 \pm 0.2$</td>
</tr>
<tr>
<td>4</td>
<td>$-141.24 \pm 0.09$</td>
<td>$-142.37 \pm 0.01$</td>
<td>$-142.45 \pm 0.01$</td>
<td>$-139.7 \pm 0.2$</td>
</tr>
<tr>
<td>8</td>
<td>$-141.64 \pm 0.03$</td>
<td>$-142.69 \pm 0.01$</td>
<td>$-142.81 \pm 0.01$</td>
<td>$-140.0 \pm 0.2$</td>
</tr>
</tbody>
</table>

tures in a phase diagram, the system divides itself in patches of the coexisting phases. Those patches could be puddles of liquid or clusters of the $\sqrt{3} \times \sqrt{3}$ structure [19,20] surrounded by empty space.

The experimental phase diagram of the first layer of $^4$He on top of graphite indicates that at high enough density, the stable phase is an incommensurate triangular phase [8,15]. In between the $\sqrt{3} \times \sqrt{3}$ registered phase and the incommensurate one, different phases have been suggested [14,15,19], from a domain wall phase (DWP) to several commensurate structures of different densities. We performed DMC calculations to check the stability of these commensurate phases on top of graphene versus a triangular arrangement of the same density. The results are displayed in Table II. The DWP was not checked because in a DMC calculation the atoms in a wall have to be located in definite positions. Those positions have to be arbitrary (for instance, crossing the simulation cell diagonally or vertically, or in arrays of three atoms instead of two) since no experimental information is available. This means that the simulation results do not represent the DWP phase meaningfully, only giving the corresponding energies of a particular atom arrangement including a wall. Table II indicates that all the commensurate structures have energies per atom larger than the corresponding triangular phase of the same density. However, and except in the case of the 2/5 phase, the differences are within two error bars. This means that they could be metastable states that could be experimentally observed.

The phase diagram of $^4$He on top of a single graphene layer can be established with the help of Fig. 3. There, we show the energy per $^4$He atom as a function of the inverse of the surface density. The error bars of the incommensurate structure are noticeable larger than in the other cases, because they are not simply the statistical errors of the simulated energies, but the result of averaging over different positions of the helium crystallographical sites on top of the graphene layer. For each point in the figure, we performed four different calculations considering similar triangular helium lattices, but displaced a little with respect to each other and averaged the energy results. Thus, we took into account the incommensurability of solid $^4$He on top of graphene. The only stable commensurate solid should be in equilibrium with this triangular incommensurate structure. The limits of the coexistence phase should have to be determined by a double-tangent Maxwell construction. Since the commensurate phase is defined by a single density, we can only approximate the result by drawing a line from this point to the one in the triangular lattice energy curve that would result in the smallest pressure. This imperfect solution gives us that the $\sqrt{3} \times \sqrt{3}$ structure is in equilibrium with this triangular phase of $\sim 0.08$ $\mathrm{\AA}^{-2}$, in agreement with experimental data for graphite [8]. In between both equilibrium densities, there would be a coexistence zone formed by patches of both solids [19], forming a DWP. This entire picture for the phase diagram in the $n=1$ case is common to $n=2,4,8$. The energies per helium atom of the $\sqrt{3} \times \sqrt{3}$ phase and the triangular one at $0.08$ $\mathrm{\AA}^{-2}$ (equilibrium density), are given in Table I (Incommensurate). The main difference between graphene and graphite is then an offset of $\sim 13.4$ K in the binding energy of $^4$He to the different compounds.

All the above results for graphene and graphite were calculated without taking into account any three body C-He interaction. To include them, one can introduce the so-called McLachlan interaction between a carbon substrate represented by a semi-infinite slab and a couple of

<table>
<caption>TABLE II. Energy per atom, in K, for several commensurate helium structures. The results labeled “incommensurate” indicate the energies for a triangular phase of the same density as the one in the previous line.</caption>
<thead>
<tr>
<th>Compound</th>
<th>$\frac{2}{5}$</th>
<th>$\frac{31}{75}$</th>
<th>$\frac{3}{7}$</th>
<th>$\frac{7}{16}$</th>
</tr>
</thead>
<tbody>
<tr>
<td>Graphene</td>
<td>$-125.81 \pm 0.01$</td>
<td>$-126.50 \pm 0.02$</td>
<td>$-126.07 \pm 0.01$</td>
<td>$-125.89 \pm 0.01$</td>
</tr>
<tr>
<td>Graphene (incommensurate)</td>
<td>$-127 \pm 0.2$</td>
<td>$-126.8 \pm 0.2$</td>
<td>$-126.3 \pm 0.2$</td>
<td>$-126.0 \pm 0.2$</td>
</tr>
<tr>
<td>Graphite</td>
<td>$-139.25 \pm 0.01$</td>
<td>$-139.96 \pm 0.01$</td>
<td>$-139.54 \pm 0.01$</td>
<td>$-139.33 \pm 0.01$</td>
</tr>
<tr>
<td>Graphite (incommensurate)</td>
<td>$-140.5 \pm 0.2$</td>
<td>$-140.2 \pm 0.2$</td>
<td>$-139.7 \pm 0.2$</td>
<td>$-140.0 \pm 0.2$</td>
</tr>
<tr>
<td>Graphite (+ McLachlan)</td>
<td>$-138.75 \pm 0.03$</td>
<td>$-139.50 \pm 0.02$</td>
<td>$-139.02 \pm 0.01$</td>
<td>$-138.81 \pm 0.01$</td>
</tr>
<tr>
<td>Graphite (+ McLachlan incommensurate)</td>
<td>$-140.1 \pm 0.2$</td>
<td>$-139.6 \pm 0.2$</td>
<td>$-139.3 \pm 0.2$</td>
<td>$-138.9 \pm 0.2$</td>
</tr>
</tbody>
</table>

![](./images/811869996438257665_3.jpg)

FIG. 3. Energy versus the inverse of the density for helium on top of a single graphene layer. Full circles, liquid phase; open circles, incommensurate triangular lattice; open square, registered $\sqrt{3} \times \sqrt{3}$ phase. Where not displayed, error bars are of the same size or smaller than the symbols. The dashed line is the result of a third order polynomial fit to the incommensurate results.

helium atoms on top of it [21]. This means that the McLachlan term only can be applied meaningfully to graphite. The model of graphite used in our calculations is not a slab but a stack of graphene sheets, implying that the use of this term is only an approximation. In previous calculations [19,20,22], this term was found to favor the liquid versus the commensurate $\sqrt{3} \times \sqrt{3}$ structure. To check its influence on the energy of the system, we performed DMC calculations on the $\sqrt{3} \times \sqrt{3}$ and liquid phases on top of graphite in the same conditions given above. The binding energy for the commensurate solid was $-142.44 \pm 0.01$ K versus $-142.81 \pm 0.01$ K of Table I, i.e., a difference of 0.37 K. The density minimum for the liquid phase changed from $0.044 \mathring{A}^{-2}$ to $0.041 \mathring{A}^{-2}$, with a binding energy of $-142.49 \pm 0.01$ K versus the $-142.69 \pm 0.01$ K of Table I. This would mean that the liquid is the stable phase for $^4$He on top of graphite, but with a difference even smaller than in the above calculations. We also repeated the calculations including this term for all the registered phases suggested above. The results are given in Table II. We found that the McLachlan interaction change the binding energies but not the fact that they are metastable with respect to the incommensurate triangular phase. The results are not applicable to graphene, since the model of a thick carbon slab does not apply to that substrate.

Summarizing, we have performed diffusion Monte Carlo calculations of $^4$He adsorbed on graphene for the first time using an accurate He-He interatomic potential. Our results show that the ground state corresponds to a $\sqrt{3} \times \sqrt{3}$ commensurate solid. However, the difference in energy between a metastable liquid film and the solid is very tiny opening the possibility of observing experimentally a two-dimensional superfluid liquid phase. Other commensurate phases have also been studied and found to be metastable, both in graphene and graphite. The phase diagram of $^4$He on graphene is qualitatively equal to the one of $^4$He on graphite that we have obtained by adding graphene sheets up to $n=8$.

We acknowledge partial financial support from The Spanish Ministry of Education and Science (MEC), grants FIS2006-02356 and FIS2005-04181, Junta de Andalucía, grant P06-FQM-01869, and Generalitat de Catalunya, grant 2005GR-00779.

[1] K. S. Novoselov, A. K. Geim, S. V. Morozov, D. Jiang, Y. Zhang, S. V. Dubonos, I. V. Grigorieva, and A. A. Firsov, Science 306, 666 (2004).

[2] K. S. Novoselov, D. Jiang, F. Schedin, T. J. Booth, V. V. Khotkevich, S. V. Morozov, and A. K. Geim, Proc. Natl. Acad. Sci. U.S.A., 102, 10451 (2005).

[3] L. D. Landau and E. Lifshitz. Statistical Physics. (Pergamon, Oxford, 1980), part I.

[4] K. S. Novoselov, A. K. Geim, S. V. Morozov, D. Jiang, M. I. Katsnelson, I. V. Grigorieva, S. V. Dubonos, and A. A. Firsov, Nature (London) 438, 197 (2005).

[5] Y. Zhang, Y. Tan, H. L. Stormer, and P. Kim, Nature (London) 438, 201 (2005).

[6] C. Berger, Z. Song, T. Li, X. Li, A. Y. Ogbazghi, R. Feng, Z. Dai, A. N. Marchenkov, E. H. Conrad, P. N. First, and W. A. Heer, J. Phys. Chem. B 108, 19912 (2004).

[7] A. K. Geim and K. S. Novoselov, Nature Mater. 6, 183 (2007).

[8] D. S. Greywall and P. A. Busch, Phys. Rev. Lett. 67, 3535 (1991).

[9] J. Boronat and J. Casulleras, Phys. Rev. B 49, 8920 (1994).

[10] P. A. Whitlock, G. V. Chester, and B. Krishnamachari, Phys. Rev. B 58, 8704 (1998).

[11] R. A. Aziz, F. R. W McCourt, and C. C. K. Wong, Mol. Phys. 61, 1487 (1987).

[12] G. Stan and M. W. Cole, Surf. Sci. 395, 280 (1998).

[13] L. W. Bruch, M. W. Cole, and E. Zaremba, Physical Adsorption: Forces and Phenomena (Oxford University Press, Oxford, 1997).

[14] P. Corboz, M. Boninsegni, L. Pollet, and M. Troyer, Phys. Rev. B 78, 245414 (2008).

[15] D. S. Greywall, Phys. Rev. B 47, 309 (1993).

[16] S. Giorgini, J. Boronat, and J. Casulleras, Phys. Rev. B 54, 6099 (1996).

[17] D. Derry, D. Wenser, W. E. Carlos, and D. R. Frank, Surf. Sci. 87, 629 (1979).

[18] R. L. Elgin and D. L. Goodstein, Phys. Rev. A 9, 2657 (1974).

[19] M. E. Pierce and E. Manousakis, Phys. Rev. B 62, 5228 (2000).

[20] M. E. Pierce and E. Manousakis, Phys. Rev. Lett. 83, 5314 (1999).

[21] L. W. Bruch, Surf. Sci. 125, 194 (1983).

[22] J. M. Gottlieb and L. W. Bruch, Phys. Rev. B 48, 3943 (1993).