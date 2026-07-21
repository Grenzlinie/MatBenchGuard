# Ab initio calculations of energies and self-diffusion on flat and stepped surfaces of Al and their implications on crystal growth

Roland Stumpf* and Matthias Scheffler

Fritz-Haber-Institut der Max-Planck-Gesellschaft, Faradayweg 4-6, D-14195 Berlin-Dahlem, Germany

(Received 1 November 1994; revised manuscript received 16 October 1995)

Using density-functional theory we investigate properties of Al(111), Al(100), Al(110), and stepped Al(111) surfaces, including formation energies of surfaces, steps, adatoms, and vacancies. For adsorption and diffusion of Al on flat regions of Al(111) surfaces the hcp site is energetically slightly preferred over the fcc site. The energy barrier for self-diffusion on Al(111) is very low (0.04 eV). Close to either of the two sorts of close packed, monoatomic steps on Al(111), Al adatoms experience an indirect attraction of $\lesssim 0.1$ eV with the edge of the step, which has a range of several atomic spacings and is of electronic origin. At the lower step edge, an adatom attaches with no barrier at a low-energy fivefold coordinated site. Coming from the upper terrace, it incorporates into the step by an atomic exchange process, which has a barrier below 0.1 eV for both sorts of close-packed steps. The barrier for diffusion along the lower edge is 0.32 eV at the {100}-faceted step and 0.39 eV at the {111}-faceted step. Unexpectedly, the latter diffusion process proceeds by an exchange mechanism. Diffusion by an exchange mechanism is also found for the "easy" direction on the Al(110) surface, i.e., along the channels. We show that Al(110) is a model system for diffusion at the {111}-faceted step on Al(111) because of its similar local geometry. We estimate temperature ranges for different modes of homoepitaxial growth on Al(111). Of particular importance are the rather low barriers for diffusion across the descending steps and the rather high barriers for diffusion along the steps. We discuss island shapes on Al(111) during growth and in thermodynamic equilibrium. Depending on the temperature the growth shapes can be fractal, triangular, or hexagonal and mainly determined by kinetics; in equilibrium the island shape is hexagonal and determined by the different step formation energies. Many of these phenomena have been seen experimentally for other metals.

## I. INTRODUCTION

The morphology of a growing surface is governed by the microscopic adatom-surface interaction, especially at bind- ing sites and at transition states of surface diffusion. $^{1,2}$ If the rates for all relevant diffusion processes are known, the evo- lution of the surface during growth can be calculated. $^{3-6}$ Be cause of the computational effort required for a quantum- mechanical description of the microscopic interaction, several quasiclassical methods have been used in the past. $^{7-13}$ However, the reliability of these calculations is questionable, particularly because neither the influence of the kinetic energy operator for the electrons nor self-consistent rearrangements of the electron density are taken into account properly. The kinetic energy of the electrons largely deter- mines the nature of the chemical bond by splitting the elec- tronic energies into bonding and antibonding levels, or by influencing the charge distribution at metal surfaces, includ- ing the spill out of density into the vacuum and the reduction of the charge-density corrugation (Smoluchowski smoothing $^{14,15}$ ). All quantum-mechanical effects that are rel evant for chemisorption are taken into account in density- functional theory (DFT), to a high level of accuracy, when it is used together with the local-density approximation (LDA) of the exchange-correlation functional. $^{16}$

In this paper we report a rather extensive set of DFT-LDA calculations of adsorption and diffusion of Al adatoms on different surfaces of fcc aluminum, which extends work pre- sented earlier. $^{17,18}$ We even include comprehensively the dif fusion at steps in our study of Al(111). The role of steps in determining the growth morphology is well known. $^{19,20}$ We study Al because it is a prototype of a simple $s$-$p$ metal, hoping that the interpretation of any observation would be particularly clear and provide insights that are transferable to other systems.

Besides the flat (111), (100), and (110) surfaces, we also consider the two different close-packed steps on Al(111). These steps are called $\langle 110\rangle /\{100\}$ and $\langle 110\rangle /\{111\}$ accord ing to the step orientation, which is the $\langle 110\rangle$ direction, and the steepest microfacet at the edges (see Figs. 1 and 2 and Refs. 18,21,22). The influence of steps is of paramount im- portance for the description of growth processes. $^{6,20,23,24}$ In particular we wish to understand the experimentally estab- lished differences between these two sorts of steps on (111) surfaces of fcc metals. Their different geometries lead to dif- ferent formation energies, $^{22,23}$ to different diffusion mecha nisms and energy barriers, $^{25-27}$ and they also have different dipole moments. $^{28}$

Using the calculated diffusion barriers and estimated dif- fusion prefactors we estimate the temperature ranges for dif- ferent growth modes on Al(111). Our results on surface dif- fusion can be regarded as input for a theory $^{3-6}$ that solves for the rate equations that determine the evolving surface mor- phology during growth as a function of temperature.

The ultimate goal of this study is to better understand some of the observations made by scanning tunneling mi- croscopy (STM) recently like the reentrant layer-by-layer growth at low temperatures $^{29}$ or the temperature variation of the growth form of islands $^{25}$ at higher temperatures. This

![](./images/813197610692116481_1.jpg)

FIG. 1. Top and side view of the fcc (332) surface. The (332) surface has {111}-faceted steps and the number of atomic rows within the (111)-oriented terraces is six.

understanding might help to better control epitaxial growth and thus to get well ordered high films at lower temperatures,which is generally desirable. $^{30-32}$

The paper is organized as follows. First we give a short description of our $ab$ initio method and describe the technical aspects that make it particularly efficient for the calculation of large metallic systems. Section III describes differences in the formation energy of the two sorts of close-packed steps on Al(111). In Sec. IV we discuss the adatom- and step- induced dipole moments on Al(111), and connected to them, the work function differences between Al(111), Al(100), and Al(110). In Sec. V the surface self-diffusion is investigated, first on the flat Al(111) surface, then approaching a step, and finally at the step. Vacancy diffusion on the flat Al(111) sur- face is also considered. We compare self-diffusion on Al(110) with that on stepped Al(111); we also compare dif- fusion at the two different steps on Al(111). Using the calcu- lated diffusion barriers and estimated prefactors, we summa- rize in Sec. VI our understanding of the temperature dependence of atomic transport processes and of homoepi- taxial growth on Al(111). Appendix A contains some details of the computational method, in Appendix C we consider the regularities of surface self-diffusion on fcc metals, and so arrive at estimates of diffusion prefactors for self-diffusion on Al, and in Appendix B we present results for self- diffusion on Al(100).

![](./images/813197610692116481_2.jpg)

FIG. 2. Top and side view of the fcc (433) surface. The (433) surface has {100}-faceted steps and the number of atomic rows within the (111)-oriented terraces is seven.

## II. TOTAL-ENERGY CALCULATIONS

The computer code, FHI93CP, used in this study, is de- scribed in Appendix A and in Ref. 33. Here, we only sum- marize the essentials of the method, give an estimate of the numerical accuracy of our calclulations, and describe the atomic geometries we use to describe stepped surfaces.

### A. Essentials

We use density-functional theory $^{34}$ and treat the exchange-correlation functional in the local-density approximation. $^{35}$ The Kohn-Sham equations $^{34}$ are solved by a Car-Parrinello-like iterative scheme, $^{36}$ using the steepest descent approach $^{37}$ for wave-function updates. We use a fully separable $ab$ initio pseudopotential $^{38}$ for Al where the $d$ po tential is treated as local and $s$ and $p$ potentials are described by projection operators. The electronic wave functions are expanded in a plane-wave basis set with a kinetic energy cutoff of 8 Ry.

The Brillouin zone is sampled at special ${\bf k}$ points. $^{39}$ For the slab calculations we typically use one ${\bf k}$ point $^{39}$ in the irreducible quarter of the rectangular surface Brillouin zone. Because of the large size of our supercells-they comprise, depending on the problem, 140-560 atomic volumes-this is sufficient to give energy differences that are within 0.03 eV of those obtained by using two or four times the number of ${\bf k}$ points, according to tests we performed. For smaller super- cells up to $200\ {\bf k}$ points are used, depending on the size.

### B. Estimated numerical error

Our calculations result in a lattice constant of $3.98\ \mathring{A}$ for fcc Al. This is $1.7\%$ smaller than the experimental value of $4.05\ \mathring{A}.^{40}$ If $0.4\%$ expansion of the lattice due to zero-point vibrations $^{41}$ and $0.5\%$ thermal expansion $^{40}$ is substracted from the experimental lattice constant, then the calculated value only $0.8\%$ too small. The cohesive energy is 4.15 eV, which is 0.75 eV higher than the experimental one of $3.40\ \text{eV}.^{42}$ These errors in bulk results are within the expec- tations for a well-converged DFT-LDA calculation. The 8-Ry plane-wave cutoff was tested to be sufficient to converge adsorption energy differences to better than $\pm 0.02$ eV (see also Ref. 41).

We also tested the dependence of our results on system size. Here the slab thickness as well as the adsorbate- adsorbate and the step-step interactions are relevant. System size and ${\bf k}$-space-sampling effects are difficult to separate, because often a change of the size of the system implies different ${\bf k}$ sampling. Furthermore, the two effects are about equal in magnitude. We therefore cannot quantify the error introduced by system size effects separately. In order to re- duce errors from these two sources we always quote the mean value of calculations at different ${\bf k}$-point sampling and system size. This improves the accuracy because the varia- tions with system size and ${\bf k}$-space sampling are often oscil-

latory. We obtain an overall numerical accuracy of the energy differences given of $\leqslant 0.06$ eV, unless a different error margin is stated explicitly.

### C. Slab geometry
In order to describe an adatom on a crystal surface we use a slab in a supercell. The repeating slabs are isolated by $\gtrsim 8$ Å of vacuum spacing. To study "isolated" adsorbates, the distance between adatoms in neighboring cells is at least three nearest-neighbor spacings. This results in an adatom-adatom interaction energy below 0.03 eV.

In order to have more bulklike layers and to avoid artificial adsorbate-adsorbate interaction through the slab, we adsorb Al on only one side. This reduces the slab thickness necessary for the desired degree of accuracy. $^{41}$ Due to the unsymmetrical situation an artificial electric field perpendicular to the slab might arise. This field is compensated in our calculations as described in Ref. 41, by introducing a dipole layer in the vacuum region. For an Al adsorbate on an Al surface this field is always very small so that even in the uncompensated case the energy differences between different sites are practically unaffected.

For the calculation of adsorption on Al(111) we use five-layer slabs. Calculations with slabs of four, six, and seven layers show that even with a four-layer slab adsorption energy differences are accurately given, which means that they change by less than 0.03 eV when thicker slabs are used.

For Al(100) we find that the desired accuracy of 0.03 eV requires a slab thickness of at least six layers. The quantity most sensitive to the slab thickness is the energy barrier for exchange diffusion; for a five-layer slab this is lower by 0.25 eV or 66% than that of the six- and seven-layer-thick slabs (see Appendix B). We use a $4 \times 4$ surface cell for the calculations of self-diffusion on Al(100). For the Al(110) surface we used eight layers and a $3 \times 4$ surface cell. Relaxation of these slabs results in a 1% expansion for Al(111) and Al(100) and a 6% contraction for Al(110). The second layer relaxations are 0%, 0.5%, and 4%, respectively.

### D. Stepped surfaces
In this paper we treat the two densely packed steps on Al(111). One is called {111} faceted, the other {100} faceted (see Figs. 1 and 2 and Ref. 18). The {111} and {100} microfacets are the steepest ones and therefore give an unambiguous way of naming the steps. $^{21}$ We shall see, however, that the {111}-faceted steps are more closely related to the (110) surface. This similarity was already discovered by Nelson and Feibelman, $^{43}$ who show that the atomic relaxation at the Al(110) surface and at the $\langle 110\rangle /\{111\}$ step is very similar. We elaborate on this similarity by showing that self-diffusion on the Al(110) surface and at the {111}-faceted step have identical mechanisms and very similar diffusion barriers.

We use three different models of stepped Al(111) surfaces, the half-layer model, the vicinal surface model, and the triangular island model.

#### 1. Half layer
The half-layer model is constructed by removing half of the atoms of one surface layer of a (111) oriented slab. The remaining, grooved, surface has two steps, one being {111} and the other {100} faceted (see Figs. 1 and 2 and Ref. 18). We choose different sizes of the rectangular surface supercell to study the influence of finite-size effects. The width of the cell in the $[1 \overline{1} 0]$ direction is varied from three to four atoms and the width of the terrace in $[11 \overline{2}]$ direction is three to four atomic rows. All these systems give results that differ only by $\leqslant 0.05$ eV. One reason for this is the rapid screening of Al. The other reason is that quantum size effects are often unimportant for total-energy differences on stepped Al(111). $^{43,44}$

#### 2. Vicinal surface
The vicinal surfaces are realized as slabs of $(m,m,m-2)$ and of $(m+2,m,m)$ orientation. The $(m,m,m-2)$ surface consist of terraces of (111) orientation that are $m$ atomic rows wide and separated by $\{11 \overline{1}\}$ faceted steps. The $(m+2,m,m)$ surface has (111) terraces $m+1$ atomic rows wide, which are separated by {100}-faceted steps. $^{21}$ The relationship between the Miller indices of the vicinal surfaces and the constituent low-index facets becomes clear by doing the vector decompositions $(m,m,m-2)=(m-1)\times(111)+1\times(11\overline{1})$ and $(m+2,m,m)=m\times(111)+1\times(200)$. Note that conventionally common factors are removed from Miller indices, so that instead of (200) [which is the shortest reciprocal lattice vector in the (100) direction] the more familiar (100) is used and for even $m$ the common factor 2 is removed. Thus the Miller indices are $(m/2,m/2,m/2-1)$ and $(m/2+1,m/2,m/2)$.

We use only orientations with even $m$ because they can be accommodated in a monoclinic supercell, whereas for odd $m$ a triclinic supercell is required. The first surface (i.e., $m=2$) of the $(m,m,m-2)$ family is the $(220)\equiv(110)$ surface, for which the (111) terraces are so narrow that no surface atom has a (111)-like coordination. After some test calculations with the (221) surface $(m=4)$, we concentrated on the (332) surface $(m=6)$ for studying the properties of nearly isolated {111}-faceted steps. The (332) surface has (111) terraces that are six atomic rows wide (see Fig. 1). We used a $1 \times 4$ surface unit cell, which means that $6 \times 4$ atoms are exposed at the surface. This layer is repeated six times to build a slab containing 144 atoms per cell.

For studying the properties of nearly isolated {100}-faceted steps we used the (433) surface out of the $(m+2,m,m)$ family, which contains seven atomic rows of (111) orientation. With a $1 \times 4$ surface unit cell, we get $7 \times 4$ atoms exposed on each surface (see Fig. 2). Again, six layers were taken, which gives a slab containing 168 atoms per cell.

The adsorption calculations at the steps of the (221), (332), and (433) surfaces essentially reproduce the results of the grooved surfaces, which reflects the efficient screening at Al surfaces and is a good test for the numerical accuracy of our calculations.

The main advantage of using the vicinal surface systems is that they allow the investigation of long-range adsorbate-step interactions, which were found, for example, by Wang and Ehrlich in experiment; $^{45}$ for a given adsorbate-step distance the number of atoms in the cell is only slightly more than half of that required for the grooved slab geometry.

<table>
<caption>TABLE I. Surface, step, adatom, and vacancy formation energies for aluminum. The Al chemical potential is taken as the cohesive energy, i.e., 4.15 eV (Ref. 42). Thus, the adatom is considered to be taken from a bulk or kink site, and to calculate the vacancy formation energies the removed atom is assumed to gain the cohesive energy.</caption>
<thead>
<tr>
<th rowspan="2">System</th>
<th colspan="2">Surface and step formation</th>
<th>Adatom<br>formation</th>
<th>Vacancy<br>formation</th>
</tr>
<tr>
<th>(eV/atom)</th>
<th>(eV/Å²)</th>
<th>(eV)</th>
<th>(eV)</th>
</tr>
</thead>
<tbody>
<tr>
<td>Al(111)</td>
<td>0.48</td>
<td>0.070</td>
<td>1.05</td>
<td>0.67</td>
</tr>
<tr>
<td>Al(100)</td>
<td>0.56</td>
<td>0.071</td>
<td>0.38</td>
<td>0.65</td>
</tr>
<tr>
<td>Al(110)</td>
<td>0.89</td>
<td>0.080</td>
<td>0.26</td>
<td>0.12</td>
</tr>
<tr>
<td>⟨110⟩/{111} step</td>
<td>0.232</td>
<td>0.082</td>
<td>0.28</td>
<td>0.21</td>
</tr>
<tr>
<td>⟨110⟩/{100} step</td>
<td>0.248</td>
<td>0.088</td>
<td>0.25</td>
<td>0.24</td>
</tr>
</tbody>
</table>

### 3. Triangular islands

To calculate the small energy difference in step formation of the {111}- and the {100}-faceted step we use triangular adatom islands of different orientation.⁴⁶ In one orientation these islands are bounded by {111}-faceted steps, if rotated by 60° the steps have {110} microfacets. One problem for determining the step formation energy difference from the energies of differently oriented islands is that edges and corners of the triangles contribute to their energy difference. The two contributions can be disentangled by using islands of different size. The largest triangular islands we study consist of 21 atoms in a 8×7 Al(111) surface cell. At a slab thickness of four layers this gives 245 atoms per supercell.

## III. DIFFERENCES OF IDEAL {111}- AND {100}-FACETED STEPS

The average step formation energy we calculate by comparing the total energy of slabs with terrace stripes¹⁸ and of slabs with flat surfaces. We get a value of 0.24 eV per step atom for the average formation energy of close-packed steps on Al(111). Table I shows that this is about half of the energy required to create the Al(111) surface per surface atom, and that the step formation energy compares to the difference of the surface energies between Al(111) and the rougher (100) or (110) surfaces per atom.

The energy difference of the two step types can be obtained by investigating triangular islands adsorbed on Al(111), as these contain only one type of steps (see Fig. 3).

![](./images/813197610692116481_3.jpg)

FIG. 3. View at islands on a fcc (111) surface. The two differently oriented triangular islands have only one kind of step; the hexagonal island has both kinds of steps.

Comparing islands with 6, 10, 15, and 21 atoms we can extrapolate to the limit where the influence of the corner atoms is negligible. Table II lists the results for the total-energy differences of two triangles whose orientations differ by 60°, and hence have different step types. The data show the rapid convergence of this energy difference with island size. We separate these energy differences into an island-size-independent contribution from the three corner atoms and a contribution proportional to the number of true edge atoms by fitting to the results in Table II. Triangular islands with {111}-faceted steps are more favorable by 0.025 eV per corner and by 0.017 eV per true step atom than islands bounded by {100}-faceted steps. The energy differences are almost the same, whether the island atoms are relaxed or not. This small effect of relaxation shows that the step formation energy difference is an electronic effect and is not determined by a different step-induced atomic relaxation. It is interesting that our results cannot be estimated from simple embedded-atom or effective-medium theory⁹,¹⁰ or a bond-cutting model.⁴⁷ The reason is that the two different triangular islands have exactly the same number of bonds.

The step formation energy determines the equilibrium shape of large islands (Wulff construction).¹⁵ On Al(111) we expect in equilibrium hexagonally shaped islands, where the edges alternate between those with a {100} and those with a {111} microfacet. The {111}-faceted edges should be longer with a edge length ratio $L^{\langle 110 \rangle / \{ 100 \}}:L^{\langle 110 \rangle / \{ 111 \}}$ of 4:5. Effects of the vibrational or configurational entropy on this ratio, which might be important at higher temperatures, are not considered however.

<table>
<caption>TABLE II. Total-energy difference $\Delta E$ per edge atom of two triangular islands on a four-layer-thick Al(111) slab in eV. One island has only {111}- and the other one has only {100}-faceted steps. Four different island sizes are considered. Using a five-layer substrate changes the results by $<10\%$. The data in the rightmost column were obtained with the atoms of the islands relaxed. Relaxing more atoms does not change the energy differences significantly.</caption>
<thead>
<tr>
<th>No. of atoms</th>
<th>No. of edge atoms</th>
<th>Surf. cell</th>
<th>$\Delta E^{\text{unrelaxed}}$</th>
<th>$\Delta E^{\text{relaxed}}$</th>
</tr>
</thead>
<tbody>
<tr>
<td>6</td>
<td>6</td>
<td>6×5</td>
<td>0.025</td>
<td>0.029</td>
</tr>
<tr>
<td>10</td>
<td>9</td>
<td>6×5</td>
<td>0.019</td>
<td>0.021</td>
</tr>
<tr>
<td>15</td>
<td>12</td>
<td>6×6</td>
<td>0.017</td>
<td>0.018</td>
</tr>
<tr>
<td>21</td>
<td>15</td>
<td>8×7</td>
<td>0.017</td>
<td>0.018</td>
</tr>
</tbody>
</table>

TABLE III. Induced dipole moment $\mu$ of Al adsorbates on fcc and hcp sites of Al(111) at 1/16 ML coverage and of a step atom in {111}- and {100}-faceted steps on Al(111) in debye (Ref. 51). Positive $\mu$ means that the negative end of the dipole points into the vacuum. Results are given for the unrelaxed and relaxed substrate atoms. The numerical accuracy of the given values is $\pm 0.01$ D. The values are averages for slabs of five to seven layers thickness.

| System                | $\mu^{\text{unrelaxed}}$ | $\mu^{\text{relaxed}}$ |
|-----------------------|--------------------------|------------------------|
| fcc-site adatom       | 0.13                     | 0.30                   |
| hcp-site adatom       | 0.06                     | 0.24                   |
| {111}-faceted step    | $-0.01$                  | $-0.01$                |
| {100}-faceted step    | 0.045                    | 0.045                  |

It is interesting to note that such hexagonal islands have been observed experimentally by Bott, Michely, and Comsa $^{20,23}$ in their STM studies of growth and sputter removal of Pt(111). These experiments show that the $\{111\}$ microfacet is favored, which is what we predict for Al(111). There is a quantitative difference, since for Pt(111) the measured edge-length ratio is 0.66, i.e., $2:3$. The similarity to our results is more than what one would have expected, as, in general, Al and Pt behave quite differently.

### IV. WORK-FUNCTION DIFFERENCES AND INDUCED SURFACE DIPOLE MOMENTS

Our calculations of induced surface dipole moments and work-function differences at Al surfaces give results that cannot be explained by Smoluchowski smoothing alone, as was assumed before. $^{15,48}$

The first interesting observation is that the Al(111) surface and the Al(110) surface have about the same work function $\Phi$. We calculate $\Phi_{\text{Al(111)}}=\Phi_{\text{Al(110)}}=4.25$ eV, $^{49}$ the experiment finds $\Phi_{\text{Al(111)}}^{\text{exp}}=4.24$ eV and $\Phi_{\text{Al(110)}}^{\text{exp}}=4.28$ eV. $^{50}$ On Al(100) the work function is the highest, 4.50 eV calculated and 4.40 eV in experiment.

In line with this we find that steps on Al(111) do affect the work function only little. Table III lists the induced dipole moment $\mu$ per step atom. The $\{111\}$-faceted step induces practically no dipole ($\mu=-0.01$ D/step atom), the $\{100\}$-faceted step has a small dipole moment with the negative end pointing into the vacuum ($\mu=0.045$ D/step atom), which means that they increase the work function. Induced dipole moments translate into work-function changes $\Delta\Phi$ according to the Helmholtz equation

$$
\Delta\Phi=37.8\frac{\mu}{A}, \tag{1}
$$

with $\mu$ in D, $\Delta\Phi$ in eV, and the area $A$ per dipole in $\mathring{\text{A}}^{2}$. To give an example: if every third surface atom of a stepped Al(111) surface would belong to a $\{100\}$-faceted step, the work function would increase by 0.05 eV.

More noticeable dipole moments are found for threefold-coordinated Al adatoms (see Table III). An Al adatom on the hcp site has a dipole moment of 0.24 D. If there was an adlayer of those Al adatoms on Al(111) of, say, 1/10 monolayer coverage, the work function would increase by 0.13 eV.

The reported results on induced dipole moments and work-function differences contradict the traditional model of charge redistribution at rough metal surfaces and around protrusions on metal surfaces such as steps or adatoms. $^{15,48}$ This model is based on Smoluchowski smoothing. Smoluchowski smoothing is caused by the kinetic energy of the electrons, which is lower for a less corrugated charge density. The smoothing of the charge density lowers the work function for rougher surfaces. Surface protrusions should induce dipole moments with the positive end pointing towards the vacuum. The smoothing effect is often discussed in a nearly free electron picture. An example is the calculation by Ishida and Liebsch $^{52}$ of the induced dipole moment of steps on jellium. Indeed they find that steps reduce the work function. Extrapolating their results for a step on Al(111) one gets an induced dipole moment of about $-0.07$ D per step atom equivalent.

Why does the smoothing model fail for our more realistic calculation of Al(111) and in experiment? We only sketch an explanation here that will be published elsewhere. $^{53}$ The smoothing effect seems to be (over-) compensated by the attraction of electrons towards the less well screened potential around surface atoms on Al(110), step-edge atoms on Al(111), or adatoms on Al(111). These atoms are only sevenfold or threefold coordinated as compared to the ninefold-coordinated surface atoms and therefore they are less well screened. This effects a net transfer of electrons towards those undercoordinated atoms.

Having a possible explanation why the standard model fails in the case of the simple metal Al the remaining puzzle is why it seems to work for the transition metals. $^{48}$ To give an example, steps on Au(111) and Pt(111) show dipole moments between $-0.25$ D (Au) and $-0.6$ D (Pt) per step atom. $^{28}$ A comparison with the jellium calculations in Ref. 52 shows that for those steps the induced dipole moment is larger in magnitude than would be expected from the smoothing effect of the $s$-$p$-like electrons only. The additional negative dipole moment is likely caused by a polarization of the $d$ electrons of the step atoms. This would also explain why Au shows a smaller effect than Pt. Au has a filled $d$ shell, in Pt the Fermi level cuts the $d$ band and therefore it is easier to polarize the $d$ states.

We conclude that for the simple as well as for the transition metals significant modifications of the smoothing based model of induced surface dipole moments and work-function differences are necessary.

### V. AL ADATOMS ON FLAT AND STEPPED AL(111)

This section describes the total-energy surface for an Al adsorbate atom on the flat Al(111) surface and at the $\{100\}$- and $\{111\}$-faceted steps. This discussion is directly relevant for surface diffusion and crystal growth on Al(111). We will study how an Al adatom moves across the Al(111) surface, what happens when the adatom comes close to a step, how it attaches to the step coming from the lower side, and how it incorporates into the step by an atomic replacement process coming from the upper side.

#### A. Diffusion on flat Al(111)

The diffusion energy barrier (0.04 eV) for diffusion of an isolated Al adatom on the flat Al(111) surface is very small (see Table IV, Ref. 18, and Fig. 4; compare Table V). The hcp site is the stable binding site and the energies of bridge

<table>
<caption>TABLE IV. Total energies for an isolated Al adatom on Al(111) at fcc, bridge, hcp, and top sites and on the fcc or hcp site directly at the upper side of the {111}- and the {100}-faceted step. The energy zero is the energy of a free aluminum atom (Ref. 42). For the adsorption on the flat Al(111) surface also the adsorbate height is given with respect to the center of the top substrate layer.</caption>
<thead>
  <tr>
    <th>Site</th>
    <th>Coordination</th>
    <th>E (eV)</th>
    <th>h (Å)</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>fcc</td>
    <td>3</td>
    <td>−3.06</td>
    <td>2.11</td>
  </tr>
  <tr>
    <td>Bridge</td>
    <td>2</td>
    <td>−3.06</td>
    <td>2.09</td>
  </tr>
  <tr>
    <td>hcp</td>
    <td>3</td>
    <td>−3.10</td>
    <td>2.08</td>
  </tr>
  <tr>
    <td>top</td>
    <td>1</td>
    <td>−2.57</td>
    <td>2.12</td>
  </tr>
  <tr>
    <td>fcc on ⟨110⟩/{111} step</td>
    <td>3</td>
    <td>−3.18</td>
    <td></td>
  </tr>
  <tr>
    <td>hcp on ⟨110⟩/{100} step</td>
    <td>3</td>
    <td>−3.18</td>
    <td></td>
  </tr>
</tbody>
</table>

and fcc sites are almost degenerate.⁵⁴ The diffusion path between the hcp sites is the direct connection between adjacent hcp, bridge, and fcc sites.⁵⁵

### 1. Comparison of hcp and fcc site
The fact that the hcp site is the lowest energy binding site for low coverage is surprising. Compared to the fcc site, the hcp site is lower in energy by 0.04 eV, which is in good agreement with Feibelman's result of 0.03 eV.⁴⁴ Half of the energy difference exists already before the Al(111) substrate is relaxed, which shows that the fcc-hcp site energy difference is determined by the electronic structure.

The hcp and fcc sites both provide threefold coordination, but only the fcc site continues the $ABCABC$ stacking of the fcc crystal, whereas the hcp site belongs to an $ABCAC$ stacking. Does our result mean that Al prefers the hcp structure? Fortunately not. We find that the fcc-hcp-site energy difference is coverage dependent. Above 1/4 ML coverage the fcc site is more stable. To create a full monolayer of Al at the hcp position costs 0.05 eV per surface atom as compared to the fcc stacking. This energy is equal to the average formation energy of the three bulk stacking faults in the ⟨111⟩ direction as calculated by Hammer *et al*.⁶⁶

The reason for the different adsorption energy [and the different induced dipole moment (see Table III)] at the hcp and the fcc site at low coverage is unknown.

### 2. Comparison of bridge and threefold sites
The diffusion barrier of Al on Al(111) is so small because the threefold and the twofold coordinated sites have nearly the same binding energy. The fcc site and bridge site are even indistinguishable. This contradicts any simple coordination-number model.⁴⁷ One might guess that the rather favorable energy of the bridge site is a result of the substrate relaxation. Indeed, on the unrelaxed substrate the bridge site is energetically less favorable (but only by 0.07 eV) than the fcc site. If not only the substrate atoms but also the adsorbates are held at bulk nearest-neighbor spacings, the fcc site is favored by 0.13 eV over the bridge site. Still, this is much less than what a coordination number model would predict.

### 3. Al dimer on Al(111)
For a complete understanding of diffusion and growth it is essential to know about the binding energies of and the diffusion barriers for small aggregates of adatoms like dimers, trimers, etc. We calculate the energy of two Al adatoms sitting at neighboring hcp sites. The energy gain with respect to isolated adatoms is 0.58 eV. Thus the Al ad-dimer should be quite stable. If its diffusivity would be lower than that of the isolated Al adatom, the dimer could nucleate island formation.

![](./images/813197610692116481_4.jpg)

FIG. 4. Upper panel: total energy along the diffusion path on an Al(433) surface for the generalized coordinate $Q=X_1+X_2$ belonging to the two atoms labeled 1 and 2, which are involved in the exchange process for the across step diffusion. Middle panel: Top view of the Al adatom situated on top of the {100}-faceted step. The rectangle gives the range of $x$-$y$ coordinates at which atom 2 was set for finding the lowest-energy path (see also Fig. 2). Lower panel: Contour plot of the total energy of the system with the $x$-$y$ coordinate of atom No. 2 fixed at positions in a regular $4×4$ mesh in the rectangle in the medium panel (contour spacing 0.04 eV). All other coordinates of the adsorbates and the two top layers were relaxed. The dashed line connects equivalent points in the two figures, the dashed quarter circles indicate the in-step and the at-step position of atom No. 2.

<table>
 <caption>TABLE V. Comparison of calculated energy barriers (in eV) for surface self-diffusion on Al with those by embedded-atom calculations of Liu <i>et al.</i> (Ref. 57) for Al (two potentials were used there; both results deviate considerably from ours) and with experimentally determined barriers on other metal surfaces. The experimental results were determined using field ion microscopy. Values in brackets are believed to be less accurate, as they were obtained with an assumed value for the diffusion prefactor $D_0$. The symbols $\parallel$ and $\perp$ indicate a diffusion direction parallel or perpendicular to the channels of the (110) surface or to the step edge respectively.</caption>
 <thead>
  <tr>
   <th>Surface</th>
   <th>Al (this work)</th>
   <th colspan="2">Al$^{\text{a}}$</th>
   <th>Ni$^{\text{a,b}}$</th>
   <th>Rh$^{\text{c}}$</th>
   <th>Pt$^{\text{d,e}}$</th>
   <th>Ir$^{\text{f-i}}$</th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td>(111)</td>
   <td>0.04</td>
   <td>0.054</td>
   <td>0.074</td>
   <td></td>
   <td>0.16</td>
   <td>(0.12)</td>
   <td>0.27</td>
  </tr>
  <tr>
   <td>Vacancy at Al(111)</td>
   <td>0.56</td>
   <td></td>
   <td></td>
   <td></td>
   <td></td>
   <td></td>
   <td></td>
  </tr>
  <tr>
   <td>(100)</td>
   <td>0.35</td>
   <td>0.69</td>
   <td>0.25</td>
   <td></td>
   <td>0.63</td>
   <td>0.47</td>
   <td>0.84</td>
  </tr>
  <tr>
   <td>(110)$\parallel$</td>
   <td>0.33</td>
   <td>0.26</td>
   <td></td>
   <td>(0.45)</td>
   <td>0.60</td>
   <td>0.84</td>
   <td>0.80</td>
  </tr>
  <tr>
   <td>(110)$\perp$</td>
   <td>0.62</td>
   <td>0.30</td>
   <td>0.15</td>
   <td>(0.45)</td>
   <td></td>
   <td>0.78</td>
   <td>0.71</td>
  </tr>
  <tr>
   <td>$\langle 110 \rangle / \{ 111 \}$-step$\parallel$ or (332)$\parallel$</td>
   <td>0.42</td>
   <td>0.27</td>
   <td>0.24</td>
   <td>(0.45)</td>
   <td>0.64</td>
   <td>0.84</td>
   <td>(1.05)</td>
  </tr>
  <tr>
   <td>$\langle 110 \rangle / \{ 100 \}$-step$\parallel$ or (644)$\parallel$</td>
   <td>0.32</td>
   <td>0.20</td>
   <td>0.24</td>
   <td>(0.37)</td>
   <td>0.54</td>
   <td>0.69</td>
   <td>(0.96)</td>
  </tr>
  <tr>
   <td>Cohesive energy$^{\text{j}}$</td>
   <td></td>
   <td>3.39</td>
   <td></td>
   <td>4.44</td>
   <td>5.75</td>
   <td>5.84</td>
   <td>6.94</td>
  </tr>
  <tr>
   <td colspan="8">aReference 8.</td>
  </tr>
  <tr>
   <td colspan="8">bReference 58.</td>
  </tr>
  <tr>
   <td colspan="8">cReference 59.</td>
  </tr>
  <tr>
   <td colspan="8">dReference 60.</td>
  </tr>
  <tr>
   <td colspan="8">eReference 61.</td>
  </tr>
  <tr>
   <td colspan="8">fReference 62.</td>
  </tr>
  <tr>
   <td colspan="8">gReference 63.</td>
  </tr>
  <tr>
   <td colspan="8">hReference 64.</td>
  </tr>
  <tr>
   <td colspan="8">iReference 26.</td>
  </tr>
  <tr>
   <td colspan="8">jReference 65.</td>
  </tr>
 </tbody>
</table>

### B. Approaching the step
Table IV, Fig. 2 in Ref. 18, and Fig. 4 show that the Al adatom is attracted by the step on the lower as well as on the upper terrace. The attraction is similar for both sorts of steps. This attraction leads to an energy gain, compared to the flat Al(111) surface, of about 0.1 eV at the threefold sites directly at the upper step edge. The long-range adatom-step attraction is weaker on the lower terrace. Just in front of the step, however, the attraction gets very strong, so that any Al adatom will be funneled towards the step. Due to the adatom-step attraction the last two threefold sites before the step are no local minima any more.

The funneling of adatoms to the lower step edge has been discovered for Ir on Ir(111) (Ref. 45) and for Pt on Pt(111) (Ref. 23) experimentally. Thus the adatom-step attraction is a common phenomenon whose origin we would like to understand. The long-range nature of the attraction, i.e., the fact that the interaction distance is much larger than the bond length leaves three possible mechanisms: dipole-dipole interaction, elastic interaction, and interaction of adatom- and step-induced surface states.

(a) *Dipole-dipole interaction.* The interaction of the adatom and the step dipole is very weak compared to the adatom-step interaction energies. For the largest dipole moments (those for adatoms at the fcc site and for the {100} step, see Table III) the adatom-step dipole-dipole interaction energy is below 1 meV for distances larger than one nearest-neighbor spacing. Furthermore, the interaction would be *repulsive* in that case.

(b) *Elastic interaction.* We calculate the magnitude of the elastic interaction of the adsorbate-induced and the step-induced relaxation field by comparing the results of the full calculations, that contain the elastic interaction with constraint calculations that do not. To switch off the elastic interaction, the positions of the substrate atoms are frozen in while the adatom is put at different sites relative to the step. Only the adatom’s height is optimized. This way no adsorbate-induced relaxation field is present and no interaction with the step-induced relaxation field is possible. Our calculations show that within the accuracy of the calculations the long-range adsorbate step interaction does not change in the restricted calculation. Thus elastic effects are not the origin of the attractive adatom-step interaction. The fact that the adatom-step attraction is long range and not of elastic origin excludes the possibility that it can be reproduced with more simple bonding models like coordination number models⁴⁷ or effective medium and embedded atom.⁵⁷,⁶⁷

(c) *“Electronic” interaction.* As a consequence there remains only the possibility that the attractive interaction is caused by an interaction of adatom-induced and step-induced surface states or screening charge densities. Our conclusion gets some support by the beautiful STM measurements of adsorbate- and step-induced surface states on Cu(111) and Au(111).⁶⁸,⁶⁹

### C. Comparison of self-diffusion
on Al(110) and at the {111}-faceted step on Al(111)

Figure 5 shows five geometries that are important for diffusion on the Al(110) surface and at the {111}-faceted step on the Al(111) surface. We will compare adsorption and diffu-

![](./images/813197610692116481_5.jpg)

FIG. 5. Important adatom geometries on the (110) surface (top) and at the {111}-faceted step on a fcc(111) surface (bottom). The energies of these geometries are given in Table VI.

<table>
 <thead>
  <tr>
   <th>
   </th>
   <th colspan="2">
    Al(110)
   </th>
   <th>
    Al (331) a
   </th>
   <th>
    $\langle 110\rangle /\{ 111\}$ step
   </th>
   <th>
    $\langle 110\rangle /\{ 100\}$ step
   </th>
  </tr>
  <tr>
   <th>
   </th>
   <th>
    $E$
   </th>
   <th>
    $h$
   </th>
   <th>
    $E$
   </th>
   <th>
    $E$
   </th>
   <th>
    $E$
   </th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td>
    (a) Fivefold site
   </td>
   <td>
    $- 3.89$
   </td>
   <td>
    $1.33$
   </td>
   <td>
    $- 3.68$
   </td>
   <td>
    $- 3.87$
   </td>
   <td>
    $- 3.90$
   </td>
  </tr>
  <tr>
   <td>
    Diffusion
   </td>
   <td>
    $\Delta E$
   </td>
   <td>
   </td>
   <td>
    $\Delta E$
   </td>
   <td>
    $\Delta E$
   </td>
   <td>
    $\Delta E$
   </td>
  </tr>
  <tr>
   <td>
    (b) Long bridge
   </td>
   <td>
    $- 0.60$
   </td>
   <td>
    $1.58$
   </td>
   <td>
    $- 0.57$
   </td>
   <td>
    $- 0.48$
   </td>
   <td>
    $- 0.32$
   </td>
  </tr>
  <tr>
   <td>
    (c) Short bridge
   </td>
   <td>
    $- 1.06$
   </td>
   <td>
    $2.16$
   </td>
   <td>
    $- 1.21$
   </td>
   <td>
    $- 1.03$
   </td>
   <td>
    $- 1.15$
   </td>
  </tr>
  <tr>
   <td>
    (d) Exchange $\parallel$
   </td>
   <td>
    $- 0.33$
   </td>
   <td>
    $1.27$
   </td>
   <td>
   </td>
   <td>
    $- 0.39$
   </td>
   <td>
    $- 0.44$
   </td>
  </tr>
  <tr>
   <td>
    (e) Exchange $\perp$
   </td>
   <td>
    $- 0.62$
   </td>
   <td>
    $0.80$
   </td>
   <td>
   </td>
   <td>
    $- 0.76{({- 0.06})}$ b
   </td>
   <td>
    $- 0.80$
   </td>
  </tr>
 </tbody>
</table>
TABLE VI. Total energies $E$ for Al adatoms with respect to that of a free Al atom and energy barriers $\Delta E$ (both in eV) for sites with similar local geometry on the Al(110), the Al (331) surface, and at steps on Al(111) (compare Fig. 5) (Ref. 42). The results for the (331) surface may be compared to those for the $\langle 110\rangle /\{ 111\}$ step. For the adsorption on Al(110) we give also the height $h$ (in Å) above the relaxed, flat surface. As explained in the text, the exact barriers for exchange diffusion parallel to the step edge might be 0.04 eV higher than given in the table.

aCalculations by Feibelman (Ref. 44); for technical differences from our calculations see text and Ref. 44.
bIn parentheses we give the barrier for the descending diffusion.

sion for the two systems. This comparison will show that the nearest-neighbor environment of the adatom is the most important determinant for the energetics. Thus adsorption energies and diffusion barriers are similar on the (110) surface and at the $\{ 111\}$-faceted step (see Table VI).

### 1. Fivefold sites
At the two fivefold sites [Fig. 5 (a)] the adsorption energies are practically identical at step and surface. The binding at the fivefold sites is rather strong. Our calculated adsorption energy of Al at threefold sites on flat Al(111) is 20% or 0.78 eV smaller (Table IV) and the calculated Al bulk cohesive energy is only 7% or 0.27 eV larger.

### 2. Bridge sites
The twofold coordinated bridge sites, the short [Figs. 5(b)] and the long bridge [Figs. 5(c)], are possible saddle points for surface self-diffusion. The energies at comparable bridge sites on Al(110) and at the $\{ 111\}$-faceted step are again similar, which is a consequence of the same local geometry (see Table VI). Short and long bridge sites, however, have different energies that result in barriers that are about twice as high for the jump over the short bridge than over the long bridge. One reason for the difference in energy at sites with the same coordination is the height of the adatom above the surface.70 For example, at the long bridge on the (110) surface the Al adatom has a height of 1.58 Å , whereas at the short bridge the height equals 2.16 Å . Thus lower height means lower energy.

Another effect should be that Smoluchowski smoothing fills the valleys with electron density taken from the upper part of the rows or the step edge. For the short-bridge position, this would reduce the charge density around the adsorbate, while it would increase the embedding charge density for the long bridge position.

### 3. Comparison with Al (331)
Having seen the striking similarity of adsorption energies at the (110) surface and at the $\{ 111\}$-faceted step, it is no surprise that a system that lies between the two cases, namely the (331) surface, shows a very similar behavior.44 For this system Feibelman obtained energy differences between the Al adsorption at twofold and fivefold sites that are very close to ours (see Table VI). We expect that the agreement with our results would be within 0.05 eV if Feibelman would have included the adsorbate-induced relaxation of the substrate. The agreement of both studies is a most demanding test for the numerical accuracy of both calculations, since Feibelman used a rather different technique in his DFT-LDA calculations.

### 4. Exchange mechanisms for surface diffusion
The bridge sites we discussed before are not the lowest-energy transition states of surface self-diffusion on Al(110) and at the $\{ 111\}$-faceted steps on Al(111) (see Table VI). In each case exchange mechanisms of lower barriers exist. For diffusion perpendicular to the rows or steps, the barrier is reduced most dramatically, from 1.06 to 0.62 eV on Al(110), and from 1.03 to 0.76 eV across the ascending $\langle 110\rangle /\{ 111\}$ step. But also in the “easy” direction along the rows or steps the barrier is reduced; from 0.60 to 0.33 eV on Al(110) and from 0.48 to 0.39 eV at the step.

#### (a) Exchange diffusion along rows on Al(110) and parallel to $\langle 110\rangle /\{ 111\}$ steps on Al(111).
We will first discuss the exchange in the “easy” direction. Figure 5(d) sketches the symmetric configurations of the exchange paths for diffusion along the channels. In both cases, the Al(110) surface and the $\{ 111\}$-faceted step, two fivefold-coordinated Al adatoms form a bridge over a surface vacancy.71

To get some idea under which circumstances exchange configurations like these are favorable we try to estimate the barrier energy by assuming that the exchange geometry is constructed from its constituents, a surface vacancy and two fivefold-coordinated Al adatoms. We then compare this to the formation energy of one adatom on Al(110) or at the step.

On the Al(110) surface the vacancy formation energy $E_{(110)}^{vac}$ is 0.12 eV and the adatom formation energy $E_{(110)}^{ad}$ is 0.26 eV (see Table I). We then estimate the diffusion barrier as $E_{d} = E_{(110)}^{vac} + 2E_{(110)}^{ad} - E_{(110)}^{ad} = 0.38$ eV, close to the calculated value of 0.33 eV.

At the {111}-faceted step $E_{\text{step}}^{\text{vac}}=0.21$ eV and $E_{\text{step}}^{\text{ad}}=0.28$ eV. The estimated energy barrier is $E_d=E_{\text{step}}^{\text{vac}}+2E_{\text{step}}^{\text{ad}}-E_{\text{step}}^{\text{ad}}=0.49$ eV as compared to 0.48 eV in the full calculation.

A third mechanism for diffusion along the channels was proposed by Liu et al.⁸ They propose that the configurations of Fig. 5(e) are not only the lowest-energy saddle-point configurations for the diffusion perpendicular to the channels but also for the diffusion parallel. Our calculations show that this is not the case for Al (see Table VI). However, the proposed process could be the explanation for the near identity of the barrier for step parallel and perpendicular diffusion on Ni, Ir, and Pt surfaces (see Table V).

(b) Exchange diffusion perpendicular to the channels on Al(110) and to $\langle 110\rangle /\{111\}$ steps on Al(111). The energies of the saddle-point configurations for the perpendicular diffusion on Al(110) and at the step are again quite similar. They differ by 0.14 eV or about 20% of the barrier height (see Table VI).

We estimate on Al(110) the energy of the exchange configuration as before. During the exchange there are two neighboring fourfold-coordinated adatoms bridging a surface vacancy. The formation energy of the fourfold-coordinated adatoms we approximate by the formation energy of an adatom on Al(100), $E_{(100)}^{\text{ad}}=0.38$ eV (see Table I). This gives an estimated energy barrier of $E_{(110)}^{\text{vac}}+2E_{(100)}^{\text{ad}}-E_{(110)}^{\text{ad}}$ =0.62 eV, which equals exactly the energy barrier found in the full calculation.

The success of the simple approach to assemble the energy for the exchange configurations from the energies of its constituents exemplifies the importance of the local environment for binding on Al surfaces. It also shows that the bonding in exchange configurations can be energetically very similar to the bonding in equilibrium configurations, contrary to what was discussed before.⁴⁴,¹¹

### D. Comparison of adsorption and diffusion at the $\langle 110\rangle /\{111\}$ and the $\langle 110\rangle /\{100\}$ steps on Al(111)

The interaction of an Al adatom and close-packed steps on Al(111) at larger distances is very similar for the two sorts of steps. Directly at the step, however, we identify some important differences in adsorption energies and diffusion barriers and mechanisms.

The results given in Table VI show that the adsorption energies at the fivefold coordinated at-step sites is nearly the same, but that there is a small preference (0.03 eV) for the $\langle 110\rangle /\{100\}$ step. This energy difference is very small; however, it might obey a general rule. According to Nelson et al.,¹⁰ it is a consequence of the different step formation energies (see Table I). Adsorbing, e.g., an Al atom at the {100}-faceted step creates two {111}-faceted "microsteps" (the situation is reversed at the {111} step). The creation of {111} microsteps should be favorable, because {111}-faceted steps are favorable. Accordingly, the adsorption energies should differ by 2×0.017 eV, which is practically the value of 0.03 eV we find.

Unfortunately the same kind of reasoning does not work for {100}-faceted steps. To form a vacancy at the {100}-faceted step creates {111} microsteps and should be favorable. However, our results favor vacancy formation at the {111}-faceted step by 0.03 eV (see Table I).

### 1. Diffusion along the step

The mechanism for self-diffusion along the {100}-faceted step is "normal" hopping and not the exchange as on Al(110) or at the {111} step. This difference is an effect of the local geometry [see Figs. 4 and 5(b)]. An Al adatom has two neighbors at the long-bridge site on Al(110) and at the {111} step but it has four neighbors at the transition state of diffusion along the {100} step. The higher coordination lowers the barrier for hopping diffusion by about 0.2 eV. The calculated barrier height for exchange diffusion along the {100} step is about the same as in the two other systems.

In summary, diffusion along the {100} step has a barrier about 0.1 eV lower than along the {111} step and it is hopping diffusion. The different diffusion mechanisms should lead to different diffusion prefactors $D_0$. Barrier height and prefactor both affect the temperature dependence of crystal growth which we discuss in Sec. VI.

### 2. Diffusion across the step

For diffusion across the {111} and the {100} step we obtain exchange diffusion mechanisms with very similar energy barriers (see Fig. 2 in Ref. 18 and Fig. 4). For the diffusion across the step in the descending direction the energy barriers are very small (0.06 and 0.08 eV); in fact they are only marginally larger than for diffusion on flat Al(111).

The exchange path at the {100}-faceted step is geometrically quite different from that at the {111}-faceted step,⁷² as there is no mirror symmetry perpendicular to the step. We mapped out a two-dimensional total-energy surface, varying the x and y coordinates of the involved step atom (atom 2 in Fig. 4) on a 4×4 grid while relaxing all the other coordinates of the adsorbates and the two upper substrate layers. In addition we calculated the energy for four points along the apparent diffusion path. We then checked if all the atomic configurations were smoothly connected along the diffusion path or if some atomic coordinates change drastically between adjacent points. The results show that all coordinates vary smoothly, which confirms that the described path is physically relevant.

## VI. ATOMIC PROCESSES AND GROWTH OF AI(111) AT DIFFERENT TEMPERATURES

We will now use our results on surface diffusion and defect formation on stepped Al(111) surfaces to examine epitaxial growth of Al(111). The mode of growth is controlled by the interplay of the rate of deposition and the temperature-dependent rates of surface diffusion and defect creation. Without solving a system of rate equations we will estimate here the most important features of epitaxial growth on Al(111). An extended study using our results and employing, e.g., a Monte Carlo technique³,⁵,⁶ to solve the rate equations would be superior, however.

### A. Activation temperature

To discuss the temperature dependence of growth morphology, we define an activation temperature $T_d$ for each

<table>
<caption>TABLE VII. Diffusion prefactors $D_0$ (in cm²/s) from theory for Al (mean of the two values given in Ref. 8) and from experiment for Rh, Pt, and Ir surfaces. Values in brackets are considered to be less reliable. The (331) surface has {111}-faceted steps and the (311) surface has {100}-faceted steps. The column “mechanism” contains our assumptions about the mechanism of diffusion for every row, and the right column gives the diffusion prefactors that will be used in the temperature dependence of growth of Al(111).</caption>
<thead>
  <tr>
    <th>Surface</th>
    <th>Mechanism</th>
    <th colspan="2">Alª</th>
    <th>Rhᵇ</th>
    <th>Ptᶜ,ᵈ</th>
    <th>Irᵉ⁻ʰ</th>
    <th>Our choice</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>(111)</td>
    <td>Hopping</td>
    <td>$9×10^{-4}$</td>
    <td>$1.6×10^{-3}$</td>
    <td>$2×10^{-4}$</td>
    <td>$(3×10^{-4})$</td>
    <td>$9×10^{-5}$</td>
    <td>$2×10^{-4}$</td>
  </tr>
  <tr>
    <td>(100)</td>
    <td>Exchange</td>
    <td></td>
    <td>$4×10^{-2}$</td>
    <td>$(1×10^{-3})$</td>
    <td>$1.3×10^{-3}$</td>
    <td>$6×10^{-2}$</td>
    <td>$8×10^{-3}$</td>
  </tr>
  <tr>
    <td>(110)∥</td>
    <td>Exchange</td>
    <td></td>
    </td>
    <td>$3×10^{-1}$</td>
    <td>$8×10^{-3}$</td>
    <td>$6×10^{-2}$</td>
    <td>$1×10^{-2}$</td>
  </tr>
  <tr>
    <td>(110)⊥</td>
    <td>Exchange</td>
    <td>$6×10^{-2}$</td>
    <td>$2.4×10^{-2}$</td>
    <td></td>
    <td>$1×10^{-3}$</td>
    <td>$4×10^{-3}$</td>
    <td>$2×10^{-3}$</td>
  </tr>
  <tr>
    <td>(331)∥</td>
    <td>Exchange</td>
    <td></td>
    </td>
    <td>$1×10^{-2}$</td>
    <td>$4×10^{-4}$</td>
    <td></td>
    <td>$1×10^{-2}$</td>
  </tr>
  <tr>
    <td>(311)∥</td>
    <td>Hopping</td>
    <td>$2×10^{-3}$</td>
    <td>$6.7×10^{-3}$</td>
    <td>$2×10^{-3}$</td>
    <td>$(1×10^{-6})$</td>
    <td></td>
    <td>$5×10^{-4}$</td>
  </tr>
</tbody>
</table>

ªReference 8.
ᵇReference 59.
ᶜReference 60.
ᵈReference 61.
ᵉReference 62.
ᶠReference 63.
ᵍReference 64.
ʰReference 26.

considered atomic process above which the process takes place frequently enough to have an impact on growth. $T_d$ is dependent on the diffusion constant $D(T)$ and on the deposition rate.

$D(T)$ is given by
$$
D(T)=D_{0} \exp \left(-E_{d} / k_{B} T\right), \tag{2}
$$
where $E_d$ is the energy barrier (see Tables IV and VI) and $D_0$ the diffusion prefactor. $D_0$ can be recast as a product of the adatom attempt frequency $\nu_a$, the distance between neighboring adsorption sites $l$, and a dimensionality factor $n$ ($n=2,4$):
$$
D_{0}=\nu_{a} l^{2} / n. \tag{3}
$$

Transforming Eqs. (2) and (3) yields the temperature $T_d$ at which a diffusing adatom jumps to a neighboring site on average $\nu_j$ times per second,
$$
T_{d}=\frac{E_{d}}{k_{B}} \bigg/ \ln \frac{n D_{0}}{\nu_{j} l^{2}}. \tag{4}
$$

We assume a growth rate of 1/100 ML/s and estimate that at this growth rate an adatom jump rate of $\nu_j$=1/s is large enough in order for a deposited Al adatom to diffuse to a more stable site before other adatoms meet the first one and form an island nucleus. The prefactors $D_0$ we use to calculate the activation temperatures is listed in Table VII. They are based on calculations for Al surface diffusion and on experimental results for diffusion on Rh, Pt, and Ir surfaces.

Our estimates of the activation temperatures $T_d$ are listed in Table VIII. They should be accurate enough for the following qualitative discussion, even if $D_0$ and $\nu_j$ are not very accurate. $D_0$ and $\nu_j$ only enter logarithmically in Eq. (4).

### B. Temperature dependence of growth

We estimate the following temperature ranges for growth modes of Al on Al(111):

(i) For temperatures below 320 K the desorption of adatoms from steps is practically irrelevant (see, e.g., Fig. 4 and Table VIII). Thus adatoms captured at a step edge will stay and the island will grow. The kinetics of growth at temperatures below 320 K is therefore determined by the barriers for capture of Al adatoms at steps and their diffusion along steps.

(ii) Our calculations show that an Al dimer on Al(111) is bound by 0.58 eV and is therefore stable at temperatures below $\simeq 250$ K. If the mobility of the dimer is smaller than that of the single adatom it will serve as a nucleus for the

<table>
<caption>TABLE VIII. Energy barriers $E_d$ (in eV) for different self-diffusion and vacancy-formation processes on Al surfaces. From these barriers and from estimates of the pre-exponential $D_0$ in Eq. (2) (see Table VII) we calculate the temperatures $T_d$ at which these processes happen at a rate of 1/s per atom [see Eq. (4)]. Exchange processes are indicated. Note that the thermodynamical vacancy formation energies as given in Table I are lower than the vacancy formation barriers.</caption>
<thead>
  <tr>
    <th></th>
    <th>Adatom diffusion</th>
    <th>$E_d$ (eV)</th>
    <th>$T_d$ (K)</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td></td>
    <td>Flat Al(111)</td>
    <td>0.04</td>
    <td>$17\pm 10$</td>
  </tr>
  <tr>
    <td></td>
    <td>Flat Al(100) (exch.)</td>
    <td>0.35</td>
    <td>$135\pm 23$</td>
  </tr>
  <tr>
    <td></td>
    <td>Al(110) ∥ to rows (exch.)</td>
    <td>0.33</td>
    <td>$130\pm 23$</td>
  </tr>
  <tr>
    <td></td>
    <td>(110) ⊥ to rows (exch.)</td>
    <td>0.62</td>
    <td>$245\pm 34$</td>
  </tr>
  <tr>
    <td></td>
    <td>⟨110⟩/(111) step ∥ (exch.)</td>
    <td>0.42</td>
    <td>$155\pm 25$</td>
  </tr>
  <tr>
    <td></td>
    <td>⟨110⟩/(100) step ∥</td>
    <td>0.32</td>
    <td>$135\pm 23$</td>
  </tr>
  <tr>
    <td></td>
    <td>⟨110⟩/(111) step ⊥ descending (exch.)</td>
    <td>0.06</td>
    <td>$25\pm 12$</td>
  </tr>
  <tr>
    <td></td>
    <td>⟨110⟩/(100) step ⊥ descending (exch.)</td>
    <td>0.08</td>
    <td>$33\pm 13$</td>
  </tr>
  <tr>
    <td></td>
    <td>Other processes on Al(111)</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td>Vacancy diffusion on Al(111)</td>
    <td>0.56</td>
    <td>$240\pm 35$</td>
  </tr>
  <tr>
    <td></td>
    <td>Adatom desorption from step</td>
    <td>$\simeq 0.8$</td>
    <td>$\simeq 320$</td>
  </tr>
  <tr>
    <td></td>
    <td>Vacancy formation in ⟨110⟩/{100} step ᵃ</td>
    <td>$\simeq 0.8$</td>
    <td>$\simeq 320$</td>
  </tr>
  <tr>
    <td></td>
    <td>Vacancy formation in ⟨110⟩/{111} step ᵃ</td>
    <td>$\simeq 0.95$</td>
    <td>$\simeq 380$</td>
  </tr>
  <tr>
    <td></td>
    <td>Vacancy formation on flat surfaceᵇ</td>
    <td>$1.2-1.8$</td>
    <td>$490-730$</td>
  </tr>
</tbody>
</table>

ᵃEstimated energy barriers, assuming that the transition state is similar to that for bridge diffusion along the step (see Table VI).
ᵇThe assumed transition state for the higher of the two values is that for bridge diffusion across the step (see Table VI). The lower value corresponds to vacancy formation in the presence of another Al adsorbate.

growth of the next layer. In that case three-dimensional growth would occur whenever adatoms meet on growing is-lands at a substantial rate. $^{22}$

(iii) At temperatures below 25 K adatoms will not be able to cross close-packed steps in the descending direction and incorporate into growing islands at a substantial rate. This would induce three-dimensional growth (see Table VIII). At such low temperatures and given the large barriers for diffu-sion along the steps, island edges will be frayed and fractal. This increases the attempt frequency of adatoms to jump across the descending steps and might even reduce the barrier. $^{13,23}$ This and the possible transient mobility of Al adatoms, which gain energy while approaching the upper step edge, $^{6,30}$ might eventually allow for layer-by-layer growth at temperatures lower than 25 K.

(iv) For $25<T<155$ K the energy barriers of diffusion parallel to both close-packed steps will prevent diffusion par-allel to the steps. As a consequence we expect that islands will grow in a "hit-and-stick" fashion. Thus, the edges can-not equilibrate and fractal-shaped islands and a layer-by-layer growth mode should result.

(v) For $T>155$ K the step edges will be straight, as dif-fusion along the step is possible, and therefore the islands will be triangular or hexagonal. According to a simple model by Michely et al. $^{12,25}$ the different diffusion properties for atoms at the two kinds of step edges might become important for determination of the detailed growth form of the island. Growing islands will advance faster perpendicular to those steps with the lower adatom mobility. As a consequence the growth shape of the island would become more triangular, with the faster growing edges dissapearing. For Al(111) our results imply that at low temperature the diffusion along {111} steps is slower than along {100} steps $(\Delta E_{D}$ $=0.1$ eV). $^{73}$ This would lead to shorter $\{111\}$ edges. How ever, because the diffusion mechanism is different at the two steps, the diffusion prefactors will be different. This might reverse the growth speed anisotropy at higher temperatures, $^{74}$ so that island shapes will be closer to the equilibrium shape with shorter $\{100\}$ edges (see Sec. III).

(vi) Vacancy formation is an important annealing process at higher temperatures. We consider two mechanisms for va-cancy formation on Al(111).

The direct creation of vacancies on flat Al(111) occurs at a rate of one per second and surface atom at 730 K (see Table VIII). In the presence of Al adatoms vacancies are created at that rate already at 490 K. Adatoms can be provided either from deposition or by desorption from steps. The barriers of adatom formation are, however, very high so that the adatom assisted vacancy formation will not be important before the formation of the vacancies on the flat Al(111) starts at 730 K.

The vacancy creation at steps has the lowest barriers. At{100}-faceted steps vacancies will be created at rates of 1/s and step-atom already at 320 K. At a {111}-faceted steps this temperature is 380 K. These vacancies can migrate into the terrace and become "normal" surface vacancies. The barrier for vacancy migration is 0.56 eV, which gives an activation temperature of 240 K (see Tables V and VIII). Thus the onset temperature for vacancy generation at steps is 320 K. Va-cancy generation preferentially at steps was also observed on Pt(111). $^{22}$

## VII. CONCLUSION

In conclusion, we have presented results of accurate elec-tronic structure and total-energy calculations that reveal sev-eral phenomena directly relevant to the description of self-diffusion at Al surfaces and to crystal growth.

The three low-index surfaces of Al are quite different with regard to surface self-diffusion. The diffusion barriers for Al adatoms on $Al(111)(E_{d}=0.04$ eV) are much lower than on Al(100) and $Al(110)(E_{d}=0.33-0.62$ eV). For Al(100) and Al(110) atomic exchange mechanisms have lower barriers for surface self-diffusion than ordinary hopping. Exchange diffusion was found even in the direction parallel to the atomic rows on Al(110). The diffusion of surface vacancies was studied for the $Al(111)$ surface $(E_{d}=0.56$ eV).

Our calculations predict that Al adatoms on Al(111) are attracted towards the edge of close-packed steps by a long-range force, which most likely originates from an interaction of adatom- and step-induced surface states. Adatoms close to the lower step edge are funneled towards the step. The dif-fusion of an Al adatom from the upper to the lower terrace proceeds via replacement of a step atom by the on-terrace adatom. This is similar to that experimentally observed across step diffusion of W on on $Ir(111).^{27,45}$ The barrier for the exchange diffusion is small at both steps on Al(111), which leads to layer-by-layer growth down to very low tem-peratures.

On Al(111) the energy barrier for diffusion of an Al at-step adatom parallel to the step is much bigger than that perpendicular to the step in the descending direction. There-fore we expect fractal growth for a large temperature range. The mechanism for diffusion along the two kinds of steps is different. Along the {111}-faceted steps we find an atomic replacement mechanism similar to that for diffusion parallel to the rows on Al(110), along the {100}-faceted steps the hopping mechanism has the lowest-energy barrier. The dif-ferences in energy barrier and diffusion prefactor for diffu-sion along the two kinds of steps can lead to temperature-dependent growth forms of islands. In equilibrium adatom islands on Al(111) will have longer {111}-faceted than {100}-faceted steps (ratio 5:4) because of the difference in step formation energy. Examples where similar growth phenom-ena were observed experimentally are Pt on Pt(111) (Refs. 23and 25) and Au on $Ru(0001).^{75}$

Additionally to the energetics at Al surfaces we have dis-cussed the surface dipole moments induced by adatoms and steps on the Al(111) surface and, related to that, the work function differences of the low index surfaces of Al. Our results indicate that the commonly used model based on Smoluchowski smoothing alone $^{15}$ has to be modified.

## APPENDIX A: DETAILS OF THE METHOD AND THE COMPUTER CODE

In the following we describe in more detail the damped Newton dynamics procedure to relax atoms, the Fermi sur-face smoothing technique, and some technical improve-ments, which allow us to calculate large systems.

### 1. Atomic relaxations

In adsorption calculations we typically allow the Al ad-sorbate and the top two (111) layers or three (110) layers to

relax until all force components are smaller in magnitude than $0.04\ \text{eV}/\mathring{\text{A}}$ . We checked that relaxation of an additional layer leaves the adsorption-energy differences practically un- changed. The most important effect of the adsorbate-induced substrate relaxation is a reduction of barriers for bridge dif- fusion by $0.07 \pm 0.05\ \text{eV}$.

Our atomic geometry relaxation is based on *damped New- ton dynamics*. In a finite-difference form, the time evolution of any atomic coordinate $X$ is given by
$$
X^{\tau+1}=X^{\tau}+\eta_{X}(X^{\tau}-X^{\tau-1})+\delta_{X} F_{X}^{\tau}, \tag{A1}
$$
where $X^{\tau}$ is the coordinate at time step $\tau$ and $F_{X}^{\tau}$ the force on $X$ at time step $\tau$. The parameters $\eta_{X}$ and $\delta_{X}$ control the damping and the mass of the coordinate. The choice of those parameters is guided by the goal that this classical dynamics combine a fast movement of the atoms toward the next local minimum of the Born-Oppenheimer surface and avoid oscil- lations around it. We obtain fast convergence for Al surfaces with $\eta_{X}{\approx}0.6$ and $\delta_{X}{\approx}8$. This choice brings the calculations close to the aperiodic limit of a damped oscillator in classical mechanics. Increasing the damping coefficient $\eta_{X}$ improves the stability of the atomic relaxation process, reducing it al- lows for energy barriers to be overcome and so to escape from local minima. In its use of the knowledge of the history of displacements, the damped dynamics technique is similarto the conjugate-gradient technique. $^{76}$

Obviously the atomic geometry converges faster if larger displacements per time step are executed. The magnitude of useful displacements is restricted, however, by the efficiency with which the electronic wave functions converge to the electronic ground state of the new atomic coordinates after the displacement. We find it advantageous to have about eight purely electronic iterations after any atomic displace- ment. The time-consuming calculation of the atomic forces is not done in those purely electronic iterations. For all systems studied in this paper, about ten atomic relaxations are neces- sary to converge to the desired accuracy.

### 2. Fermi occupation
To stabilize the self-consistent calculations for the elec- trons and to improve $\mathbf{k}$-space integration, we smear out the Fermi surface. For this purpose the Kohn-Sham eigenstates of energy $\epsilon_{i}$ are occupied according to a Fermi distribution $f=f(\epsilon_{i},T^{\text{el}})$ with $k_{B}T^{\text{el}}=0.1\ \text{eV}$. Thus the free energy $F=E-T^{\text{el}}S$ at the electronic temperature $T^{\text{el}}$ is minimized instead of the total energy $E,^{41,76-78}$ where $S$ is the entropyof independent electrons, $^{65}$
$$
S=-2k_{B}\sum_{i}\left[f_{i}\ln f_{i}+(1-f_{i})\ln(1-f_{i})\right]. \tag{A2}
$$

This approach may cause some inaccuracies, since we really want results belonging to $T^{\text{el}}=0$. For the free energy at a given geometry the $T^{\text{el}}{\to}0$ limit can be easily obtained by evaluation of $E^{\text{zero}}{=}0.5(E{+}F){=}E{-}0.5T^{\text{el}}S.^{41,76,77}$ This value differs from $F(T^{\text{el}}{\to}0)$ only by terms that are third and higher order in $T^{\text{el}}$. For the optimization of the geometry the force $\partial E^{\text{zero}}/\partial X$ should be used which is, however, morecomplicated to evaluate. $^{79}$ For our choice of $k_{B}T^{\text{el}}=0.1\ \text{eV}$ the geometries and the total-energy differences are almost not affected. This was tested for the adsorption of Al on Al surfaces by using values of $0.05\ \text{eV}$ and $0.2\ \text{eV}$ for $k_{B}T^{\text{el}}$ and an increased number of $\mathbf{k}$ points.

A further approach to stabilize the way self-consistency is achieved is to reduce electron transfer between single- particle states in successive iterations. For this purpose ficti- tious eigenvalues after Pederson and Jackson $^{80}$ are intro duced. The occupation numbers are calculated directly from the fictitious eigenvalues according to Fermi occupation at $T^{\text{el}}$. These fictitious eigenvalues follow the as-calculated ei- genvalues in a sort of damped dynamics, so that both sets of eigenvalues will become identical when self-consistency is attained. This indirect approach of damping charge transfer oscillations is easier to implement than the more obvious one of damping the change in occupation numbers directly. The reason is that the occupation numbers are constrained to be in the range between 0 and 2, and their sum has to give the total number of electrons. For the eigenvalues no such con- straints exist.

### 3. Optimizations
The computer code used for this work is optimized for large atomic systems. The most important techniques are the following.

(i) One often encountered problem with large systems is the $1/G^{2}$ dependence of the electrostatic potential. Here $\mathbf{G}$ is a reciprocal-lattice vector. This dependence leads to long- wavelength charge-density oscillations, known as *charge sloshing* or $1/G^{2}$ instability. See, for example, Ref. 81. We deal with this problem by starting with a rather good initial density constructed by a superposition of contracted atomic charge densities. The contraction was done following Finnis, $^{82}$ where the radial atomic densities are multiplied by a Fermi function. The contraction anticipates most of the intra-atomic charge transfer that occurs upon building a solid from isolated atoms. The wave functions for the first step of the self-consistent iterations are obtained by diagonalizing of the Kohn-Sham Hamiltonian constructed from this approxi- mate density and within a reduced plane-wave basis $(E^{\text{cut}}{=}1.5{-}5$ Ry, depending on time and memory con- straints). Then, in the first $\hat{\tau}{<}8$ electronic iterations, the charge density $n(\mathbf{r})$ is linearly mixed as in "standard" self-consistent calculations:
$$
n^{\text{in, }\hat{\tau}+1}(\mathbf{r})=\alpha n^{\text{out, }\hat{\tau}}(\mathbf{r})+(1-\alpha)n^{\text{in, }\hat{\tau}}(\mathbf{r}). \tag{A3}
$$

The mixing coefficient $\alpha$ increases from $10\%$ to $100\%$ within these first eight time steps. By this procedure the charge sloshing was not initiated for the systems considered in this paper. In calculations of larger cells than those re- ported here we found the linear mixing in $\mathbf{r}$ space insuffi- cient. There charge-density sloshing could, however, be effi- ciently suppressed by a mixing in $\mathbf{G}$ space with a mixing coefficient $\alpha(G)$ that is smaller for smaller $G$.

(ii) The evaluation of the nonlocal part of the pseudopotential $^{38}$ dominates the computation time for large systems in traditional plane-wave-based electronic structure programs. We reduce this computational effort by taking ad- vantage of the translational symmetry of atomic positions within the supercell. $^{33}$ Without introducing any approxima

![](./images/813197610692116481_6.jpg)

FIG. 6. View at the three adsorption geometries considered for the Al self-diffusion on Al(100).

tion, this optimization typically reduces the number of opera- tions to calculate the nonlocal pseudopotential part for those atoms sitting on ideal lattice coordinates by a factor of ten.

(iii) For large systems the required computer memory rises as the square of the number of atoms, and is largely determined by the number of wave-function coefficients. We optimize memory usage in several ways. A simple steepest- descent update procedure for the wave functions is used, $^{83}$ thus only the wave-function coefficients of one iteration need to be stored. The wave-function coefficients and most of the other large arrays are stored in single precision; however, double precision is used for all floating point operations and for storing intermediate results.

(iv) Our computer code optimizes the data access in com- puters that use memory of different speed. The idea is that once data are transferred from slow memory to fast memory, e.g., from the disk to main memory, this data should be used as often as possible before it is moved back to the disk. This is accomplished by reordering loops or by blocking techniques. $^{33}$ The most important case where blocking is used is the orthogonalization of the wave functions. Instead of orthogonalizing just one wave function to those with lower index (the standard Gram-Schmidt procedure), we or- thogonalize a block of, say, 30 wave functions to those with lower index and then orthogonalize the wave functions within the block. In the case where only part of the wave functions at one $k$-point fit into main memory this procedure reduces the disk to memory data transfer by a factor up to 30.

An example of the efficiency of the code is the calculation of an Al slab with 350 atoms per unit cell in a supercell as large as 560 atomic volumes, and sampling the Brillouin zone at one special $k$ point. This leads to 28 000 plane waves and 560 electronic states, with an overall memory require- ment of 200 MB. The calculation takes about 25 h on an IBM/6000 370 RISC workstation with 64 MB main memory, if all atoms are at ideal lattice positions. If no atoms are at ideal sites, the time increases by a factor of 3. The time spent waiting for disk access during the calculation is below 30% and could be reduced further with the faster hard disks avail- able today.

### APPENDIX B: Al ON Al(100)

We add here our results for the adsorption and diffusion of Al on Al(100). Our study repeats that of Feibelman on the same system. $^{84}$ The main result of Feibelman's paper, which is the favorable energy barrier for an exchange diffusion mechanism, has been questioned recently. $^{8,85}$ We calculated the adsorption energies at the three sites that are important for the discussion of surface diffusion (see Fig. 6). Our re- sults confirm that the exchange diffusion mechanism has a lower barrier than the bridge diffusion mechanism. The agreement in adsorption energy differences of our results with those of Feibelman is again as excellent as in the other examples in this paper. However, this agreement with Feibel- man's results is obtained only if we use the same slab thick- ness as he did, i.e., five layers (see Table IX). The agreement would be even better, if we had not relaxed all atoms but only those that Feibelman had relaxed. However, while the numerical accuracy of both calculations agrees, it is most interesting to note that our calculations with six- and seven- layer slabs show a significant change of the energy of the exchange configuration. This change increases the barrier for diffusion by nearly a factor of 3 (see Table IX). A similar sensitivity of calculated energies with slab thickness was not found for any other system and we do not have an explana- tion for it. The energy of the exchange configuration also proved to be especially sensitive to changes in the value of the lattice constant and the $k$-point sampling.

TABLE IX. Adsorption energies (in eV) and heights (in bohr) for Al adsorbed on Al(100) at 1/16 ML coverage. The energy zero is the energy of an isolated, free Al atom. The considered configura- tions are pictured in Fig. 6. Results for slabs of different thickness are compared with those obtained by Feibelman (Ref. 84) who used a five-layer slab. He used the experimental lattice constant of 7.66 bohr and allowed only the adsorbate and its substrate neigh- bors to relax (see also Ref. 44). On the other hand, we use the theoretical lattice constant of 7.56 bohr, one special $k$ point in the surface Brillouin zone, and we allow the adsorbate and the upper two layers to relax. For the results labeled as "average" additional calculations with $4\ \mathbf{k}$ points and with an additional layer relaxed were considered as well. Energies are in eV, the adsorbate heights $h$ are in Å relative to the relaxed clean surface.

<table>
  <thead>
    <tr>
      <th></th>
      <th>Configuration</th>
      <th>$E$</th>
      <th>$\Delta E^{4-fold}$</th>
      <th>$h$</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Five layer (Ref. 84)</td>
      <td>Fourfold</td>
      <td>$-2.93$</td>
      <td></td>
      <td>1.72</td>
    </tr>
    <tr>
      <td></td>
      <td>Bridge</td>
      <td>$-2.28$</td>
      <td>0.65</td>
      <td>2.20</td>
    </tr>
    <tr>
      <td></td>
      <td>Exchange</td>
      <td>$-2.73$</td>
      <td>0.20</td>
      <td>0.90</td>
    </tr>
    <tr>
      <td>Five layer</td>
      <td>Fourfold</td>
      <td>$-3.68$</td>
      <td></td>
      <td>1.58</td>
    </tr>
    <tr>
      <td></td>
      <td>Bridge</td>
      <td>$-3.05$</td>
      <td>0.63</td>
      <td>1.91</td>
    </tr>
    <tr>
      <td></td>
      <td>Exchange</td>
      <td>$-3.55$</td>
      <td>0.13</td>
      <td>0.74</td>
    </tr>
    <tr>
      <td>Six layer</td>
      <td>Fourfold</td>
      <td>$-3.75$</td>
      <td></td>
      <td>1.70</td>
    </tr>
    <tr>
      <td></td>
      <td>Bridge</td>
      <td>$-3.12$</td>
      <td>0.63</td>
      <td>2.11</td>
    </tr>
    <tr>
      <td></td>
      <td>Exchange</td>
      <td>$-3.37$</td>
      <td>0.38</td>
      <td>0.91</td>
    </tr>
    <tr>
      <td>Seven layer</td>
      <td>Fourfold</td>
      <td>$-3.75$</td>
      <td></td>
      <td>1.73</td>
    </tr>
    <tr>
      <td></td>
      <td>Bridge</td>
      <td>$-3.07$</td>
      <td>0.69</td>
      <td>2.12</td>
    </tr>
    <tr>
      <td></td>
      <td>Exchange</td>
      <td>$-3.35$</td>
      <td>0.40</td>
      <td>0.98</td>
    </tr>
    <tr>
      <td>"Average"</td>
      <td>Fourfold</td>
      <td>$-3.77$</td>
      <td></td>
      <td>1.69</td>
    </tr>
    <tr>
      <td></td>
      <td>Bridge</td>
      <td>$-3.12$</td>
      <td>0.68</td>
      <td>2.09</td>
    </tr>
    <tr>
      <td></td>
      <td>Exchange</td>
      <td>$-3.42$</td>
      <td>0.35</td>
      <td>0.90</td>
    </tr>
  </tbody>
</table>

### APPENDIX C: UNIFORMITY IN SURFACE SELF-DIFFUSION ON METALS: ENERGY BARRIERS AND DIFFUSION MECHANISMS

We identify some common trends for self-diffusion on these different surfaces. The rule of thumb that diffusion bar-

riers scale with the cohesive energy is valid. The energy barriers for surface self-diffusion are lowest for the (111) surface, i.e., the close-packed surface. All other surfaces have diffusion barriers about 5 times higher. The diffusion barriers on these rougher surfaces vary by less than a factor of 3, even comparing different metals.

In both our calculations for Al and in most of the experiments, the barriers for diffusion in the channels of the (110) surface and along the {111}-faceted steps are nearly the same for the same metal (Table V). It is also found in theory and experiment that the energy barriers for diffusion along the {100} step are smaller than along the {111} step. Because of this similarity we speculate that the diffusion mechanism is the exchange [see Fig. 5(d)] for the diffusion along the {111}- faceted step and hoping for the diffusion along the {100}- faceted step for all metals considered.

Information about the diffusion mechanism is also con- tained in the diffusion prefactors $D_{0}$. Using semiempirical calculations, $D_{0}$ was evaluated for a series of metal surfaces. $^{8}$ In all cases the prefactor of an exchange process was larger than that of the normal hopping diffusion (see Table VII for Al). Also the experimentally determined $D_{0}$'s are larger in those cases where we expect exchange diffusion (see Table VII).

Thus we conclude that surface self-diffusion on Rh, Pt, and Ir is hopping diffusion on the (111) surface and along the {100}-faceted step, and it is exchange diffusion in all other cases considered.

*Present address: Sandia National Laboratories, Division 1114, Al- buquerque, NM 87 185-1413.
$^{1}$ G. Vineyard, J. Phys. Chem. Solids 3, 121 (1957).
$^{2}$ R. Gomer, Rep. Prog. Phys. 53, 917 (1990).
$^{3}$ J. A. Venables, G. D. T. Spiller, and M. Hanbücken, Rep. Prog. Phys. 47, 815 (1984).
$^{4}$ J. Villain, J. Phys. (France) I 1, 19 (1991); Z.-W. Lai and S. Das Sarma, Phys. Rev. Lett. 66, 2348 (1991); Hong Yan, ibid. 68,3048 (1992).
$^{5}$ S. Kenny, M. R. Wilby, A. K. Myers-Beaghton, and D. D. Vvedensky, Phys. Rev. B 46, 10 345 (1992).
$^{6}$ P. Šmilauer, M. R. Wilby, and D. D. Vvedensky, Phys. Rev. B 47,4119 (1993).
$^{7}$ K. D. Hammonds and R. M. Lynden-Bell, Surf. Sci. 278, 437(1992).
$^{8}$ C. L. Liu, J. M. Cohen, J. B. Adams, and A. F. Voter, Surf. Sci.253, 334 (1991).
$^{9}$ C.-L. Liu and J. B. Adams, Surf. Sci. 265, 262 (1992).
$^{10}$ R. C. Nelson, T. L. Einstein, S. V. Khare, and P. J. Rous, Surf. Sci.295, 462 (1993).
$^{11}$ L. B. Hansen, P. Stoltze, K. W. Jacobsen, and J. K. Nørskov, Phys. Rev. B 44, 6523 (1991); Surf. Sci. 289, 68 (1993).
$^{12}$ S. Liu, Z. Zhang, J. K. Nørskov, and H. Metiu, Phys. Rev. Lett.71, 2967 (1993).
$^{13}$ M. Villarba and H. Jonsson, Phys. Rev. B 49, 2208 (1994); Surf. Sci. 317, 15 (1994).
$^{14}$ R. Smoluchowski, Phys. Rev. 60, 661 (1941).
$^{15}$ A. Zangwill, Physics at Surfaces (Cambridge University Press,Cambridge, 1988).
$^{16}$ W. E. Pickett, Comput. Phys. Rep. 9, 117 (1989).
$^{17}$ M. Scheffler, J. Neugebauer, and R. Stumpf, J. Phys. Condens. Matter 5, A91 (1993); R. Stumpf and M. Scheffler, Surf. Sci.307-309, 501 (1994).
$^{18}$ R. Stumpf and M. Scheffler, Phys. Rev. Lett. 72, 254 (1994).
$^{19}$ M. Klaua and H. Bethge, Ultramicroscopy 17, 73 (1995).
$^{20}$ H. Bethge, in Kinetics of Ordering and Growth at Surfaces, edited by M. Lagally (Plenum, New York, 1990), p. 125.
$^{21}$ B. Lang, R. W. Joyner, and G. A. Somorjai, Surf. Sci. 30, 440(1972); M. A. van Hove and G. A. Somorjai, ibid. 92, 489(1980); D. R. Eisner and T. L. Einstein, ibid. 286, L559 (1993).
$^{22}$ T. Michely and G. Comsa, Surf. Sci. 256, 217 (1991); T. Michely,T. Land, U. Littmark, and G. Comsa, ibid. 272, 204 (1992).
$^{23}$ M. Bott, T. Michely, and G. Comsa, Surf. Sci. 272, 161 (1992).
$^{24}$ C.-L. Chen and T. T. Tsong, Phys. Rev. B 47, 15 852 (1993).
$^{25}$ T. Michely, M. Hohage, M. Bott, and G. Comsa, Phys. Rev. Lett.70, 3943 (1993).
$^{26}$ S. C. Wang and G. Ehrlich, Surf. Sci. 239, 301 (1990).
$^{27}$ S. C. Wang and G. Ehrlich, Phys. Rev. Lett. 67, 2509 (1991).
$^{28}$ K. Besocke, B. Krahl-Urban, and H. Wagner, Surf. Sci. 68, 39(1977).
$^{29}$ R. Kunkel, B. Poelsema, L. K. Verheij, and G. Comsa, Phys. Rev. Lett. 65, 733 (1990).
$^{30}$ W. F. Egelhoff, Jr. and I. Jacob, Phys. Rev. Lett. 62, 921 (1989).
$^{31}$ B. J. Hinch, R. B. Doak, and L. H. Dubois, Surf. Sci. 286, 261(1993).
$^{32}$ S. Oppo, V. Fiorentini, and M. Scheffler, Phys. Rev. Lett. 71,2437 (1993).
$^{33}$ R. Stumpf and M. Scheffler, Comput. Phys. Commun. 79, 447(1994).
$^{34}$ W. Kohn and L. J. Sham, Phys. Rev. 140, A1133 (1965).
$^{35}$ D. M. Ceperley and B. J. Alder, Phys. Rev. Lett. 45, 566 (1980) as parametrized by J. P. Perdew and A. Zunger, Phys. Rev. B 23,5048 (1981).
$^{36}$ R. Car and M. Parrinello, Phys. Rev. Lett. 55, 2471 (1985).
$^{37}$ A. Williams and J. Soler, Bull. Am. Phys. Soc. 32, 562 (1987).
$^{38}$ R. Stumpf, X. Gonze, and M. Scheffler (unpublished); X. Gonze, R. Stumpf, and M. Scheffler, Phys. Rev. B 44, 8503 (1991).
$^{39}$ H. J. Monkhorst and J. D. Pack, Phys. Rev. B 13, 5188 (1976).
$^{40}$ AIP Handbook, 3rd ed., edited by D. E. Gray (McGraw-Hill, New York, 1987).
$^{41}$ J. Neugebauer and M. Scheffler, Phys. Rev. B 46, 16 067 (1992).
$^{42}$ Cohesive and adsorption energies are given with respect to the energy of an isolated Al atom calculated in a large cell with the same 8-Ry cutoff. Adding the spin-polarization energy of0.15 eV to the so calculated free atom energy and comparing to the bulk energy per Al atom gives a cohesive energy of 4.15 eV. This is 0.75 eV higher than the experimental value (Ref. 65). This overbinding is a problem common to converged DFT-LDA calculations. Our cohesive energy result is within 0.01 eV of other recent DFT-LDA calculations using the Ceperley-Alder form for exchange and correlation [Ref. 41; Y.-M. Juan and E. Kaxiras, Phys. Rev. B 48, 14 944 (1993)]. It is widely accepted that adsorption energy differences for different sites are only weakly affected by this problem.
$^{43}$ J. S. Nelson and P. J. Feibelman, Phys. Rev. Lett. 68, 2188(1992).
$^{44}$ P. J. Feibelman, Phys. Rev. 69, 1568 (1992). The adsorption energies given in this paper are not directly comparable to ours

(see Ref. 42) because of the reference energy of the isolated atom. Apparently there is an inconsistency of this reference en- ergy caused by Feibelman’s Green’s-function technique; energy differences are comparable, however, and for these the main (but small) differences to our results arise because Feibelman did not include the adsorbate-induced relaxation of the Al (331) sub- strate.

$^{45}$S.C. Wang and G. Ehrlich, Phys. Rev. Lett. 70, 41 (1993).

$^{46}$The number of atoms and the $\mathbf{k}$-space integration is the same for both island orientations, which is essential for a high degree of error cancelation when comparing the energy of two orienta- tions. This is not the case if differently oriented vicinal surfaces are used for the determination of step energy differences.

$^{47}$“Simple bond-cutting” models assume that the energy per atom varies linearly with the atom’s coordination number. An im- proved version that takes the bond saturation into account makes this approach very similar to the effective-medium and embedded-atom methods [see, for example, I. J Robertson et al., Europhys. Lett. 15, 301 (1991); Phys. Rev. Lett. 70, 1944 (1993); M. Methfessel et al., Appl. Phys. A 55, 442 (1992)].

$^{48}$J. Hölzl and F. K. Schulte, in Solid Surface Physics, Springer Tracts in Modern Physics Vol. 85 (Springer, Berlin, 1979), pp. 1–100.

$^{49}$The values for the work functions were determined by averaging values for slabs of thickness five to seven layers for Al(111) and eight and nine layers for Al(110).

$^{50}$J. K. Grepstad, P. O. Gartland, and B. J. Slasvold, Surf. Sci. 57, 348 (1976).

$^{51}$A dipole moment of 1 D equals $0.208e$ Å, where $e$ is the elemen- tary charge.

$^{52}$H. Ishida and A. Liebsch, Phys. Rev. B 46, 7153 (1992).

$^{53}$A. P. Seitsonen and M. Scheffler (unpublished).

$^{54}$The energy difference between hcp, bridge, and fcc sites is very small. It is therefore important to check if the calculations are sufficiently accurate. We therefore performed several test calcu- lations, varying carefully all parameters that affect the accuracy. We used coverages from 1/12 to 1/56 ML, increased the number of $\mathbf{k}$ points from 1 to 4 and to 9, we used from 4 to 7 Al(111) layers, and we increased the plane-wave cutoff. The energy dif- ferences of different sites were very stable and the order of fcc and hcp sites never reversed at low coverage. We expect the difference between hcp and fcc sites to be accurate to within 0.02 eV. The relative accuracy for the bridge site is slighty worse.

$^{55}$The only marked maximum of the total-energy surface is at the atop site. The top site is 0.53 eV higher in energy than the hcp site. Interestingly, the height of the adatom at the atop site is only slightly larger than at the threefold sites (see Table IV). This is a consequence of the fact that bond length gets smaller when the coordination is lower (for the atop site we obtain a bond length of $2.51$ Å, which is 6% smaller than for the three- fold sites). Furthermore, we find that the adatom at the atop site introduces a strong substrate relaxation: the substrate atom be- low the adsorbate is lowered by $0.4$ Å. A similar substrate re- laxation was found in calculations for alkali-metal adsorbates on Al(111) (Refs. 41 and 56).

$^{56}$C. Stampfl, M. Scheffler, and H. Over, Phys. Rev. Lett. 69, 1532 (1992).

$^{57}$M. S. Daw and M. I. Baskes, Phys. Rev. B 29, 12 (1984).

$^{58}$R. T. Tung and W. R. Graham, Surf. Sci. 97, 73 (1980).

$^{59}$G. Ayrault and G. Ehrlich, J. Chem. Phys. 60, 281 (1974).

$^{60}$G. L. Kellogg, Surf. Sci. 246, 31 (1991).

$^{61}$D. W. Basset and P. R. Webber, Surf. Sci. 70, 520 (1978).

$^{62}$S. C. Wang and G. Ehrlich, Phys. Rev. Lett. 62, 2297 (1989).

$^{63}$T. T. Tsong and C.-L. Chen, Phys. Rev. B 43, 2007 (1991).

$^{64}$T. T. Tsong, Atom-Probe Field Ion Microscopy (Cambridge Uni- versity Press, Cambridge, 1990).

$^{65}$C. Kittel, Introduction to Solid State Physics, 6th ed. (Wiley, New York, 1986).

$^{66}$B. Hammer, K. W. Jacobsen, V. Milman, and M. C. Payne, J. Phys. Condens. Matter 4, 10 453 (1992).

$^{67}$K. W. Jacobsen, J. K. Nørskov, and M. J. Puska, Phys. Rev. B 35, 7423 (1987).

$^{68}$M. F. Crommie, C. P. Lutz, and D. Eigler, Nature 363, 524 (1993).

$^{69}$Y. Hasegawa and P. Avouris, Phys. Rev. Lett. 71, 1071 (1993).

$^{70}$The height is mostly determined by the local geometry and the length of atomic bonds. Bond lengths vary only slightly, with low coordinated atoms having shorter bonds.

$^{71}$At the (110) surface the two adatoms nearly sit on ideal fcc lattice positions, displaced by $0.08$ Å towards the vacancy and $0.05$ Å closer to the surface than for the “normal” fivefold site. At the step the corresponding displacements are similar.

$^{72}$There could be a nonsymmetric exchange path at the {111}- faceted step also. We did not calculate that path as the symmetric one has already such a low barrier that is at the limit of the accuracy of our calculations. Our conclusions therefore would not be affected by an additional diffusion process. No energeti- cally favorable symmetrical exchange path exists for the {100}- faceted step, as there the involved step atom would have to go over a top site.

$^{73}$The effective barrier for diffusion around the corner of an island is higher for adatoms coming from {100} steps than coming from {111} steps, which would favor growth perpendicular to {100} steps. The difference in barrier height is 0.03 eV, which is the difference in adsorption energy at the two types of steps (see Table I). Because of the larger barrier height difference of 0.1 eV for diffusion along the steps the effect of the corner diffusion anisotropy can be neglected.

$^{74}$We can estimate the temperature $T^{\text{cross}}$ at which diffusion along the two kinds of steps will proceed at the same rate. Transform- ing Eq. (2) into

$$
T^{\text{cross}}=k \frac{E_{d}^{\{111\} \|}-E_{d}^{\{110\} \|}}{\ln D_{0}^{\{100\} \|}-\ln D_{0}^{\{111\} \|}}
$$

and taking the values for $D_{0}$ and $E_{d}$ for the $\langle 110 \rangle / \{ 111 \}$ and $\langle 110 \rangle / \{ 100 \}$ step from Tables VII and VIII, we get $T^{\text{cross}} \simeq 400$ K. We expect that this value is rather inaccurate, however.

$^{75}$R. Q. Hwang et al., Phys. Rev. Lett. 67, 3279 (1991).

$^{76}$M. J. Gillan, J. Phys. Condens. Matter 1, 689 (1989).

$^{77}$A. de Vita and M. J. Gillan, J. Phys. C 3, 6225 (1991).

$^{78}$G. Kresse and J. Haffner, Phys. Rev. B 48, 13 115 (1993).

$^{79}$There exists a more elegant way to smear the occupation numbers around the Fermi energy introduced in M. Methfessel and A. T. Paxton, Phys. Rev. B 40, 3616 (1989). There the total energy is minimized so that the energies and forces do not have to be corrected. We do not use this method in this paper, however.

$^{80}$M. R. Pederson and K. A. Jackson, Phys. Rev. B 43, 7312 (1991).

$^{81}$K.-M. Ho, J. Ihm, and J. D. Joannopoulos, Phys. Rev. B 25, 4260 (1982); and T. A. Arias, M. C. Payne, and J. D. Joannopoulos,

ibid. 45, 1538 (1992).

$^{82}$M. W. Finnis, J. Phys. Condens. Matter 2, 331 (1990).

$^{83}$The gain in speed by using more sophisticated update techniques like the conjugate gradient approach (Ref. 76) would be small for large metallic systems, according to our experience.

$^{84}$P. J. Feibelman, Phys. Rev. Lett. 65, 729 (1990).

$^{85}$S. Debiaggi and A. Caro, J. Phys. Condens. Matter 4, 3905 (1992).