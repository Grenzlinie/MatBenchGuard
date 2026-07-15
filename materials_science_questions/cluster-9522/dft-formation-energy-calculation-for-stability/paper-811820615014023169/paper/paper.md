![](./images/811820615014023169_1.jpg)

Short- and long-range orders in Fe-Cr: A Monte Carlo study

C. Pareige, C. Domain, and P. Olsson

Citation: *Journal of Applied Physics* **106**, 104906 (2009); doi: 10.1063/1.3257232
View online: http://dx.doi.org/10.1063/1.3257232
View Table of Contents: http://scitation.aip.org/content/aip/journal/jap/106/10?ver=pdfcov
Published by the AIP Publishing

---

### Articles you may be interested in
**Absence of long-range chemical ordering in equimolar FeCoCrNi**
Appl. Phys. Lett. **100**, 251907 (2012); 10.1063/1.4730327

**Calculation of proper energy barriers for atomistic kinetic Monte Carlo simulations on rigid lattice with chemical and strain field long-range effects using artificial neural networks**
J. Chem. Phys. **132**, 074507 (2010); 10.1063/1.3298990

**Long-range order on the atomic scale induced at CoFeB/MgO interfaces**
J. Appl. Phys. **105**, 073701 (2009); 10.1063/1.3100044

**Are there stable long-range ordered Fe 1 - x Cr x compounds?**
Appl. Phys. Lett. **92**, 141904 (2008); 10.1063/1.2907337

**Long-range order and short-range order study on CoCrPt/Ti films by synchrotron x-ray scattering and extended x-ray absorption fine structure spectroscopy**
J. Appl. Phys. **91**, 7182 (2002); 10.1063/1.1448799

---

![](./images/811820615014023169_2.jpg)

# Short- and long-range orders in Fe–Cr: A Monte Carlo study

C. Pareige, $^{1,a)}$ C. Domain, $^{2}$ and P. Olsson $^{2}$

$^{1}$ Groupe de Physique des Matériaux, Université et INSA de Rouen, UMR 6634 CNRS-Avenue de l'Université BP 12, 76801 Saint Etienne du Rouvray, France
$^{2}$ Département Matériaux et Mécanique des Composants, EDF R&D, Les Renardières, F-77250 Moret sur Loing, France

(Received 9 July 2009; accepted 24 September 2009; published online 20 November 2009)

Atomistic kinetic Monte Carlo simulations based on the two-band semiempirical cohesive model for Fe–Cr have revealed a body centered tetragonal $Fe_{14}Cr$ ordered compound at very low temperatures. Density functional theory calculations have shown that this structure is more stable than the $Fe_{15}Cr$ compound reported in literature. The study of short-range order, at higher temperatures, has shown that short-range order is not only characterized by the existence of Fe–Cr correlations in the two first neighbor shells but also by the existence of Cr–Cr correlations in the seventh and eighth neighbor shells corresponding to characteristic lengths of the ordered compound. The comparison of these results to neutron diffuse scattering experiments has shown that these characteristic lengths are observed in the experiments. Nevertheless, it appears that a larger spectrum of correlation lengths must exist in the experimental alloy. A Fourier transform of the atomic configuration has shown that the $\alpha$ phase is short-range ordered in the two-phase region. © 2009 American Institute of Physics.

[doi:10.1063/1.3257232]

## I. INTRODUCTION

High-Cr ferritic and ferritic-martensitic steels of technological interest for structural components of fusion or fission nuclear reactors (Gen IV) contain, in most cases, between 6 and 14 at. % of Cr. This is essentially due to the mechanical properties, the response to radiation, and the corrosion resistance these alloys exhibit. $^{1}$ Thus, in the past few years, binary Fe–Cr model alloys have been at the focus of a large amount of basic research; see the recent review by Malerba et al. $^{2}$ Below the Curie temperature, depending on the Cr concentration, two behaviors are observed. At low-Cr concentrations, the alloys exhibit a short-range order (SRO) tendency $^{3-7}$ whereas at a larger Cr content, phase separation is observed. $^{8-10}$ This behavior is due to the complex heat of mixing of the alloy, which undergoes a change in sign from negative at low-Cr concentration to positive for higher concentration. The negative sign of the heat of mixing indicates a tendency for the formation of intermetallic (IM) compounds. Density functional theory (DFT) calculations and Monte Carlo simulations using the cluster expansion (CE) approach have identified some IM compounds as being possibly stable. $^{11-14}$ When the temperature increases, only SRO is observed in the $\alpha$ region. Recent Monte Carlo simulations in the concentration dependent model (CDM) approximation $^{3}$ and with the two-band model $^{15}$ (2BM) approximation $^{16}$ have shown that the $\alpha$ phase still exhibits a SRO in the two-phase region.

Using atomistic kinetic Monte Carlo (AKMC) simulations (Sec. II), we have characterized the ordered compound formed in the case of 2BM approximation (Sec. III). Because the correlation lengths of the ordered phase are larger then the first and second neighbor shells, we show that an accurate characterization of the SRO exhibited in the $\alpha$ phase implies the study of the SRO parameters up to larger neighbor shells. A comparison of the radial scattering intensity, calculated from the Fourier transform of the atomic configuration, to the neutron diffuse scattering intensity experiments $^{6}$ for the same alloy and at the same temperature, is shown very useful to get information about the correlation lengths observed in the short-range ordered $\alpha$ phase (Sec. IV). In Sec. V, we describe the SRO exhibited by the $\alpha$ phase inside the two-phase region.

## II. METHODOLOGY

In this work, we use AKMC simulations in the 2BM approximation, $^{15}$ as well as some DFT calculations. The AKMC simulations were performed with the LAKIMOCA code, based on the residence time algorithm. $^{17}$ The simulated crystal is constructed on a rigid bcc lattice with periodic boundary conditions. One vacancy is introduced into the simulation box. The size of the box is equal to $64a_{0}$ ($a_{0}$ =2.8553 Å). The vacancy diffusion is determined by the calculation of the eight (bcc lattice) probabilities of first nearest neighbor (nn) jumps. This probability is given by the following equation:

$$
\Gamma_{X,V}=\nu\exp\left(-\frac{E_{\text{mig}}^{X}+\Delta E/2}{kT}\right), \tag{1}
$$

where $X$ is the jumping atom and $\nu$ is the attempt frequency $(6×10^{12}\ \text{s}^{-1})$. The migration energies $E_{\text{mig}}^{X}$ given by the 2BM potentials are 0.65 eV for Fe and 0.52 eV for a single Cr atom in Fe, in good agreement with ab initio predictions. $^{18}$ $\Delta E$ is the energy difference of the system due to the vacancy jump, calculated using the 2BM potential based on projector augmented wave (PAW) ab initio

$^{a)}$Author to whom correspondence should be addressed. Electronic mail: cristelle.pareige@univ-rouen.fr.

![](./images/811820615014023169_3.jpg)

FIG. 2. (Color online) 3D distribution of Cr atoms in the alloy Fe-6.25 at. % Cr aged at 250 K for $4 \times 10^{13}$ s (V=18.1×18.1 ×1.5 nm³). Different variants (translation and orientation variants) of a long-range ordered phase appear clearly. The distribution of the atoms, which are inside the small box drown in the image, is shown Fig. 3.

$$
\mathrm{H}=\begin{pmatrix}
2 & 1 & 0 \\
\overline{1} & 2 & 0 \\
0 & 0 & 3
\end{pmatrix}. \tag{4}
$$

In this ordered structure, two Cr atoms in "first neighbor" position are separated by 6.2 Å (this corresponds to the seventh coordination shell) and Cr atoms in "second neighbor" position are placed at 6.4 Å (this corresponds to the eighth coordination shell), as it is expected by the DFT calculations of the present work. The Fe₁₅Cr compound described by Erhart *et al.*¹² is base-centered monoclinic. Whereas that cell is different than the one described here, it is important to note that its lattice vectors correspond to vectors of the seventh neighbor shell: This means that Cr-Cr pairs are separated by 6.2 Å as we find in this work. In the structure described by Nguyen-Manh *et al.*,¹³,¹⁴ the Cr-Cr correlations are observed in the sixth coordination shell (at 5.7 Å) and the Cr sublattice is simple cubic. Considering the long-ranged pair interaction shown in Fig. 1, we can explain the higher stability of the structure proposed by Erhart *et al.*¹² than the one proposed by Nguyen-Manh *et al.*¹³,¹⁴ We also see that the Fe₁₄Cr structure found through thermal aging using the 2BM fulfills the criteria of energy minimization with respect to the long- ranged Cr-Cr pair repulsion. Moreover, an *ab initio* comparison of enthalpies of formation for these different structures, see Table I, shows that the Fe₁₄Cr compound here presented is significantly more stable than the Fe₁₅Cr IM. Also, a slight modification of the Fe₁₅Cr IM, in line with increasing the Cr-Cr distances, has been investigated. This modified Fe₁₅Cr is created from that of Nguyen-Manh by translating every other line of Cr atoms in the simple cubic sublattice one lattice parameter. The Cr-Cr distances become then sixth, respectively, eighth nn for the modified Fe₁₅Cr IM; see Fig. 4. This configuration is shown to be more stable than the one proposed by Nguyen-Manh. These predictions render the discussion of the influence of a particular IM around this concentration rather moot. It seems obvious that many more simple transformations can be performed that should negligibly change the stability of the alloy. Thus real binary alloys, aged for extreme time spans at low temperatures, should consist of superpositions or domains of IMs, and effectively be more similar to disordered alloys than long- range ordered ones.

<table>
<caption>TABLE I. The enthalpies of solution for several IM compounds.</caption>
<thead>
  <tr>
    <th rowspan="2">Configuration</th>
    <th rowspan="2">at. % Cr</th>
    <th>H</th>
    <th>H</th>
  </tr>
  <tr>
    <th>(meV)</th>
    <th>(meV)ᵃ</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>Fe15Cr–6 nb</td>
    <td>6.25</td>
    <td>−6.47ᵇ/−5.82ᶜ</td>
    <td>−5.87</td>
  </tr>
  <tr>
    <td>Fe15Cr–S2ᶜ</td>
    <td>6.25</td>
    <td>−9.1ᶜ</td>
    <td>…</td>
  </tr>
  <tr>
    <td>Fe15Cr–6/8 nn</td>
    <td>6.25</td>
    <td>…</td>
    <td>−8.55</td>
  </tr>
  <tr>
    <td>Fe14Cr–7/8 nn</td>
    <td>6.67</td>
    <td>…</td>
    <td>−10.2</td>
  </tr>
</tbody>
<tfoot>
  <tr>
    <td colspan="4">ᵃThis work.</td>
  </tr>
  <tr>
    <td colspan="4">ᵇReferences 13 and 14.</td>
  </tr>
  <tr>
    <td colspan="4">ᶜReference 12.</td>
  </tr>
</tfoot>
</table>

### IV. SRO

To characterize the SRO, three different tools have been used in this work.

(1) *The SRO parameter.* Because Cr-Cr correlations exist in the seventh and eighth neighbor shells in the IM compound, an accurate description of the SRO has been done up to these coordination shells. The definition used

![](./images/811820615014023169_4.jpg)

FIG. 3. (Color online) 3D distribution of Cr atoms (black) and Fe atoms (gray) in an ordered domain of the Fe₁₄Cr compound obtained with the 2BM approximation. The volume corresponds to the small volume drawn (Fig. 2). (a) Projection in the (001) plane. The bcc cell of the lattice (—) and the bct cell (—) of the ordered phase are drawn. (b) Cr and Fe atoms in the bct cell. The cell contains 30 atoms.

![](./images/811820615014023169_5.jpg)

FIG. 4. (Color online) A low energy Fe₁₅Cr alloy composition. Cr atoms are in black while Fe atoms are in gray.

![](./images/811820615014023169_6.jpg)

FIG. 5. (Color online) RDF of Cr atoms in the Fe-6.25 at. % Cr aged at 500 and 773 K. For comparison, the RDF of Cr atoms calculated in the alloy aged at 250 K for $4\times 10^{13}$ s has been plotted.

for the SRO parameter is the classical definition introduced by Cowley $^{26}$ as follows:

$$
\alpha_{\mathrm{Cr}}^{(i)}=1-\frac{P_{\mathrm{Fe}}^{(i)}}{\left(1-X_{\mathrm{Cr}}\right)},\qquad(5)
$$

where $\alpha_{\mathrm{Cr}}^{(i)}$ is the SRO parameter for the $i$th shell of a Cr atom, $P_{\mathrm{Fe}}^{(i)}$ is the probability to observe an Fe atom in the $i$th shell of the Cr atoms, and $X_{\mathrm{Cr}}$ is the Cr concentration in the alloy. A negative value is associated with local order (a probability to observe Fe-Cr pairs higher than in the random state) whereas a positive value indicates unmixing. Some authors use a specific SRO parameter $\beta$ for the bcc lattice defined by

$$
\beta=\frac{8 \alpha_{\mathrm{Cr}}^{(1)}+6 \alpha_{\mathrm{Cr}}^{(2)}}{14}.\qquad(6)
$$

(2) The radial distribution function (RDF) of the Cr atoms is calculated as follows:

$$
g(r)=\frac{1}{X_{\mathrm{Cr}}} \sum_{i=1}^{N_{\mathrm{Cr}}} \sum_{j=1}^{N(r)} \frac{\sigma\left(r_{i}-r_{j}\right)}{N_{\mathrm{Cr}} N(r)},\qquad(7)
$$

where $N_{\mathrm{Cr}}$ denotes the total number of Cr atoms of the alloy, $r_{i}$ is their position, $N(r)$ is the number of possible $r_{j}$ vectors for a given distance $r$, and $\sigma(r_{i}-r_{j})$ is equal to 1 if the site $(r_{i}-r_{j})$ is occupied by a Cr atom or to 0 if it is an Fe atom. $g(r)$ is calculated up to $r=14.3$ Å.

(3) The 3D Fourier transform of the volume, which gives access to the distribution of the scattering intensity in the reciprocal lattice and to the radial scattering intensity.

The Fe-6.25 at. % Cr alloy has been aged at 500 and 773 K. Figure 5 shows the evolution of the RDF with temperature. For comparison, the RDF calculated at 250 K, in the long-range ordered alloy, is also plotted. Whereas the curve obtained at 250 K clearly reveals Cr-Fe correlations up to the sixth neighbors and Cr-Cr correlations for the seventh and eighth coordination shells (accordingly with the cell of the IM compound), at 500 and 773 K, the RDFs indicate that long-range order does not exist anymore. Indeed, although strong Fe-Cr correlations still exist up to the third shell, these correlations become less important for both the fourth and fifth neighbor shells. Cr-Cr correlations appear in the sixth coordination shell. A maximum still exists for the seventh and eighth coordination shells but it is clearly less marked and long-range distance correlations have disappeared. These results indicate that the existence domain in the temperature of the IM compound is small (if it exists, see discussion of the previous paragraph). Even at 500 K, which is a low temperature, only SRO remains. It appears very difficult to obtain experimental evidence of the existence of such a phase.

![](./images/811820615014023169_7.jpg)

FIG. 6. (Color online) Value of the SRO parameter for the eight first neighbor shells in function of the Cr concentration of the alloy at 773 K. The SRO parameter $\beta$ is also plotted.

Figure 6 presents the concentration dependence of the SRO parameters up to the eighth neighbor shell at 773 K. Only alloys lying in the $\alpha$ one-phase region have been considered. At this temperature, the minimum of the SRO parameter $\beta$ lies around 5 at. %. As the comparison of the evolution of $\beta$ obtained by AKMC on rigid lattice with the 2BM to the experimental results and to the results obtained with the other simulation models has already been done in Ref. 27, we will not focus on this point. Because of the dependence of the entropy with both concentration and temperature, $^{3}$ the maximum SRO is not reached. In good agreement with the observations made in the previous paragraph on the Fe-6.25 at. % Cr alloy, at high temperature, strong Cr-Fe correlations remain up to the third neighbor shell in the entire concentration domain studied. It is interesting to note that $\alpha_{\mathrm{Cr}}^{(1)}$ is less negative than $\alpha_{\mathrm{Cr}}^{(2)}$ and $\alpha_{\mathrm{Cr}}^{(3)}$, Cr-Fe correlations being stronger in the third shell for Cr concentration higher than 5%. Moreover, for the higher Cr concentration, $\alpha_{\mathrm{Cr}}^{(1)}$ shows an important increase indicating that $\alpha_{\mathrm{Cr}}^{(1)}$ is more sensitive to the Cr concentration change than the other parameters. This indicates a trend to easily form Cr-Cr pairs in the first shell when the Cr concentration increases than in the second and third shells. The 2BM potential must favor the formation of $\alpha'$ subcritical nuclei. This is in good agreement with the results of Klaver, $^{28}$ which reveal similar tendencies between DFT calculations and the 2BM potential. This behavior of the three first SRO param-

![](./images/811820615014023169_8.jpg)

FIG. 7. Radial scattering intensity as a function of the scattering vector $K$ $=2\pi/r$ $\text{\AA}^{-1}$ in an Fe-5 at. % Cr aged at 700 K.

eters is not observed by Erhart et al. $^{3}$ with CDM. In their case, the SRO parameter is stronger in the first shell and lower in the third shell.

Concerning the seventh and the eighth shells, for all concentrations, the SRO parameters are positive. They reach a maximum between $5.5\%$ and $6.25\%$. In the entire concentration range the SRO is characterized by Cr–Cr correlations in the seventh and eighth shells. The accurate characterization and description of the SRO in this system is not given if only the two first shells are considered. For the interatomic potentials we used, it is necessary to calculate the SRO parameters up to the seventh and eighth neighbors. It should be the same in the case of the compound described by Erhart et al. $^{12}$ With CE, the Cr atoms being in sixth neighbor in the compound $\text{Fe}_{15}\text{Cr}$ described by Nguyen-Manh et al., $^{13,14}$ the SRO parameters should probably be calculated at least up to the sixth shell.

In order to check if the SRO, observed in thermally aged alloys by Monte Carlo simulation in the 2BM approximation, is representative of the SRO observed experimentally, we calculated the radial scattering intensity and compare it to the neutron diffuse scattering results obtained by Mirebeau et al. $^{6}$ for an Fe–5 at. % Cr alloy aged at 700 K. Figure 7 shows the scattering intensity as a function of the scattering vector $K$ obtained by Fourier transform of the atomic configuration obtained by thermal aging of the same alloy aged at the same temperature by MC simulations. A reinforcement of the scattering intensity is clearly observed at a $K$ value of $K_{m}=1.12$ $\text{\AA}^{-1}$. The scattering intensity can be written in the usual way as $^{6}$

$$
\begin{aligned}
I(\vec{K})= & I_{\mathrm{inc}}+X_{\mathrm{Cr}}(1-X_{\mathrm{Cr}})(b_{\mathrm{Cr}}-b_{\mathrm{Fe}})^{2}\left[1+\sum_{i}N_{i}\alpha_{i}\right. \\
& \left.\times \frac{\sin(Kr_{i})}{Kr_{i}}\right],
\end{aligned} \tag{8}
$$

where $I_{\mathrm{inc}}$ is the incoherent scattering; $X_{\mathrm{Cr}}$ is the Cr concentration of the alloy; $\alpha_{i}$, $N_{i}$, and $r_{i}$ are, respectively, the SRO parameter, the coordination number, and the radius of the $i$th coordination shell; and $b_{\mathrm{Cr}}$ and $b_{\mathrm{Fe}}$ are the scattering lengths. In this work, they have been taken equal to 1 and 0, respectively. In case of dilute alloy (when one correlation length $r_{nm}$ exists), the correlation length can be deduced from the value of the scattering vector $K_{m}$ by

$$
K_{m}=\frac{S\times 2\pi}{r_{nm}} \quad \text{with} \quad S=1.23. \tag{9}
$$

The value $1.23\times 2\pi$ $\text{\AA}^{-1}$ corresponds to the position of the first maximum of the sin (u)/u function for a value of $r_{nm}$ =1 Å. When the concentration of the alloy increases, a shift of the signal toward the smaller values of $K$ is observed. As a first approximation, it can be considered that the value of the $S$ factor also decreases to reach a value between 1.2 and 1.1. If we consider this interval [1.1–1.2] for $S$, correlation distances that belong to the interval [6.2–6.7 Å] are found. This corresponds to the seventh (6.2 Å) and eighth (6.4 Å) neighbor shells, in very good agreement with the results discussed before. This validates the use of this approximation. Experimentally Mirebeau et al. $^{6}$ observed a diffuse scattering in a larger interval of $K$ values: The experimental diffuse scattering intensity exhibits a plateau within an interval of about [0.9–1.9 $\text{\AA}^{-1}$]. There is no singular maximum, as is observed in Fig. 6; thus the shape of the experimental signal is not well reproduced by the simulations. Nevertheless, it is important to note that the value of $K_{m}$ obtained in the present work belongs to the experimental interval. The difference observed could be due to concentration inhomogeneity of the sample analyzed by neutron scattering, but it is unlikely. It should rather be due to the existence of a larger spectrum of correlation lengths in the experimental alloy than in the simulated one. A convolution of peaks associated with different correlation distances could give such a shape of the scattering intensity. The existence of different correlation lengths can have various origins. For example, SRO observed in the real alloy could exhibit characteristic lengths corresponding to a larger number of different neighbor shells than only for two close shells as is the case in this work. The observation of only these two kinds of correlation lengths in the Monte Carlo simulations can be due to the rigid lattice approximation and to the absence of vibrational entropy. The fact that the 2BM potential has been shown to exhibit a large number of low energy ordered structures when relaxation from the rigid bcc lattice is allowed $^{27}$ can indicate that a larger spectrum of correlation lengths could be observed at high temperatures with this model. Another explanation concerns some characteristic distances, which could be due to the presence of SRO domains, which may contribute to the scattering intensity signal for the lower value of $K$. Finding an explanation to this experimental observation should be very useful to improve the models.

The 3D distribution of the scattering intensity is presented Fig. 8. The diffuse scattering is isotropic and forms spheres around the fundamental reflections. This shows that the Cr–Cr correlations appear isotropic at this temperature.

## V. SRO AND PRECIPITATION

An alloy Fe–9 at. % Cr has been aged at 773 K. At this temperature, this alloy is inside the two-phase region as it is shown in Fig. 9 where $\alpha'$ precipitates are observed. Figure 10 presents the Fourier transform of the configuration of Fig.

![](./images/811820615014023169_9.jpg)

FIG. 8. (Color online) 3D distribution of the scattering intensity for the alloy Fe-5 at. % Cr aged at 700 K.

9 in the (001)* plane of the reciprocal lattice and the radial scattering intensity as a function of the scattering vector for the same configuration and for shorter aging time.

At long aging times, two signals are clearly visible [Figs. 10(a) and 10(c)]: A small angle scattering intensity, which is related to the precipitation of the $\alpha'$ phase (this signal corresponds to the signal obtained during small angle neutron scattering (SANS) experiments), and a diffuse scattering intensity, which is the signature of the SRO already observed in the $\alpha$ one-phase domain. It is a clear evidence that the $\alpha'$ precipitates of Fig. 9 are embedded in a short-range ordered $\alpha$ phase. This is in good agreement with the results of Erhart et al. $^{3}$ and Bonny et al. $^{16}$ It has to be noted that, as in the case of experiments, for more supersaturated alloys, the diffuse scattering intensity can be difficult to distinguish because of the small angle scattering signal.

At short aging time, the radial scattering intensity shows only one signal, which corresponds to the presence of SRO [Fig. 10(b)]. No small angle scattering is observed, signifying that no precipitation has occurred.

These results indicate that, in the case of slightly supersaturated alloys, ordering precedes precipitation of the $\alpha'$ phase (because in slightly supersaturated alloys ordering only involves short diffusion distances, contrary to the case of phase separation).

![](./images/811820615014023169_10.jpg)

FIG. 9. (Color online) 3D distribution of atoms in the Fe-9 at. % Cr aged at 773 K in an 18 nm simulation box for $1.3×10^{4}$ s. Only atoms that are inside a sphere of radius equal to 0.7 nm, which contains at least 30% of Cr, are visualized.

![](./images/811820615014023169_11.jpg)

FIG. 10. (Color online) (a) Fourier transform of the configuration of Fig. 9 (Fe-9 at. % Cr aged for $1.3×10^{4}$ s at 773 K) in the (001)* plane. (b) Radial scattering intensity as a function of the scattering vector $K$ =$2\pi/r$ $\text{\AA}^{-1}$ in the same alloy at short aging time (after 15 s). (c) Radial scattering intensity at long aging time (after $1.3×10^{4}$ s), corresponding to the Fourier transform (a).

Figure 11 presents the time evolution of the SRO parameters in the same alloy. Whereas there is also evidence that short-range ordering occurs before phase separation (decrease in the SRO parameters of the second up to the fifth shell followed by an increase due to the positive contribution of the appearance of the $\alpha'$ precipitates), this figure reveals that the first SRO parameter is positive even in the very early stage of aging. This means that Cr-Cr correlations exist in the first coordination shell as soon as the aging begins. This positive value of the first SRO is the signature that the alloy is placed into the miscibility gap. Indeed, these positive correlations between Cr atoms are probably due to the formation of subcritical nuclei during the incubation time before nucleation of the $\alpha'$ phase. The presence of these subcritical nuclei explains the less negative value of the second SRO parameter. This is consistent with the work of Erhart et al. $^{3}$ and of Bonny et al. $^{16}$ Because the higher the Cr concentration is, the higher the number and the size of nuclei is, Bonny et al. observed that even the second SRO parameter is positive in the very early stage of aging in alloys, which contain between 12 and 18 at. % Cr.

## VI. CONCLUSION

In this paper, we have investigated long- and short-range orderings in the low-Cr concentration Fe-Cr alloys using AKMC simulations based on the 2BM approximation.

![](./images/811820615014023169_12.jpg)

FIG. 11. (Color online) Time evolution of the SRO parameters up to the eighth neighbor shell in the Fe-9 at. % Cr aged at 773 K.

Up to ambient temperature, an IM compound $Fe_{14}Cr$ is found. Its structure is based on a bct cell: $a$=$b$=6.4 Å and $c$=8.6 Å. In this structure, Cr atoms are placed in seventh and in eighth neighbors of a Cr atom. The stability of this structure is validated by DFT calculations showing it to be more stable than previously proposed IMs around this con- centration range. The long-ranged repulsive interaction be- tween Cr atoms in Fe, as here predicted by DFT, can explain the different stabilities for these ordered compounds.

At higher temperatures, only SRO remains. The RDF of Cr atoms and the scattering intensity, obtained by Fourier transform of the atomic configurations, are very useful tools to give an accurate description of the SRO. It has been shown that the SRO is not only characterized by the exis- tence of Fe-Cr correlations in the two first shells but also by the existence of Cr-Cr correlations in the seventh and the eighth neighbor shells corresponding to characteristic lengths equal to 6.2 and 6.4 Å. These correlations are precursor of the Cr-Cr correlations of the long-range ordered phase. The comparison of the radial scattering intensity to the neutron diffuse scattering experiments, for the same alloy and at the same temperature, has shown a qualitatively good agree- ment: The characteristic lengths found in this work are ob- served in the experiments. Nevertheless, it appears that a larger spectrum of correlation lengths must exist in the ex- perimental alloy.

The radial scattering intensity has also been used to show that SRO still exists in the $\alpha$ phase inside the miscibil- ity gap, accordingly with the previous work of Erhart $et$ $al.^{3}$ and of Bonny $et$ $al.^{16}$ Short-range ordering takes place before phase separation occurs. When $\alpha'$ precipitates appear, they are embedded in a short-range ordered matrix. In the studied alloy, Cr-Cr correlations have been revealed in the first neighbor shell whereas the opposite behavior (Fe-Cr corre- lations) is observed in the $\alpha$ one-phase region. These positive correlations between Cr atoms reveal the formation of sub- critical nuclei during the incubation time before nucleation of the $\alpha'$ precipitates.

## ACKNOWLEDGMENTS
This work has been done using Computer-time Grant No. 2005014 of the Centre de Ressources Informatiques de Haute Normandie (CRIHAN). This work is a part of the research program of the EDF-CNRS joint laboratory EM2VM (Study and Modeling of the Microstructure for Ag- ing of Materials). This work has been partially supported by the European Commission within the project GETMAT un- der Grant Agreement No. FP7-212175.

$^{1}$E. Little, J. Nucl. Mater. 87, 11 (1979); E. A. Little and D. A. Stow, ibid. 87, 25 (1979); E. A. Little and D. A. Stow, Met. Sci. 14, 89 (1980); E. A. Little, R. Bullough, and M. H. Wood, Proc. R. Soc. London, Ser. A 372, 565 (1980); N. Singh and J. H. Evans, J. Nucl. Mater. 226, 277 (1995); F. A. Garner, M. B. Toloczko, and B. H. Sencer, ibid. 276, 123 (2000).
$^{2}$L. Malerba, A. Caro, and J. Wallenius, J. Nucl. Mater. 382, 112 (2008).
$^{3}$P. Erhart, A. Caro, M. S. de Caro, and B. Sadigh, Phys. Rev. B 77, 134206 (2008).
$^{4}$M. Hennion, J. Phys. F: Met. Phys. 13, 2351 (1983).
$^{5}$M. Y. Lavrentiev, R. Drautz, D. Nguyen-Manh, T. P. C. Klaver, and S. L. Dudarev, Phys. Rev. B 75, 014208 (2007).
$^{6}$I. Mirebeau, M. Hennion, and G. Parette, Phys. Rev. Lett. 53, 687 (1984).
$^{7}$P. Olsson, I. A. Abrikosov, L. Vitos, and J. Wallenius, J. Nucl. Mater. 321, 84 (2003).
$^{8}$M. Miller, J. Hyde, M. Hetherington, A. Cerezo, G. Smith, and C. Elliott, Acta Metall. Mater. 43, 3385 (1995).
$^{9}$F. Bley, Acta Metall. Mater. 40, 1505 (1992).
$^{10}$S. Novy, P. Pareige, and C. Pareige, J. Nucl. Mater. 384, 96 (2009).
$^{11}$D. Nguyen-Manh, M. Lavrentiev, and S. Dudarev, J. Comput.-Aided Mater. Des. 14, 159 (2007).
$^{12}$P. Erhart, B. Sadigh, and A. Caro, Appl. Phys. Lett. 92, 141904 (2008).
$^{13}$D. Nguyen-Manh, M. Lavrentiev, and S. Dudarev, Comp. Mater. Sci. 44, 1 (2008).
$^{14}$D. Nguyen-Manh, M. Lavrentiev, and S. L. Dudarev, C. R. Phys. 9, 379 (2008).
$^{15}$P. Olsson, J. Wallenius, C. Domain, K. Nordlund, and L. Malerba, Phys. Rev. B 72, 214119 (2005); 74, 229906 (2006).
$^{16}$G. Bonny, D. Terentyev, L. Malerba, and D. Van Neck, Phys. Rev. B 79, 104207 (2009).
$^{17}$W. M. Young and E. W. Elcock, Proc. Phys. Soc. London 89, 735 (1966).
$^{18}$P. Olsson, C. Domain, and J. Wallenius, Phys. Rev. B 75, 014110 (2007).
$^{19}$G. Kresse and D. Joubert, Phys. Rev. B 59, 1758 (1999).
$^{20}$G. Kresse and J. Hafner, J. Phys.: Condens. Matter 6, 8245 (1994); Phys. Rev. B 47, 558 (1993); G. Kresse and J. Furthmüller, Comput. Mater. Sci. 6, 15 (1996).
$^{21}$J. P. Perdew, K. Burke, and M. Ernzerhof, Phys. Rev. Lett. 77, 3865 (1996).
$^{22}$S. M. Vosko, L. Wilk, and M. Nusair, Can. J. Phys. 58, 1200 (1980).
$^{23}$H. J. Monkhorst and J. D. Pack, Phys. Rev. B 13, 5188 (1976).
$^{24}$T. P. C. Klaver, P. Olsson, and M. W. Finnis, Phys. Rev. B 76, 214110 (2007).
$^{25}$P. Olsson, T. P. C. Klaver, and C. Domain, Phys. Rev. B (submitted).
$^{26}$M. Cowley, Phys. Rev. 77, 669 (1950).
$^{27}$G. Bonny, R. Pasianot, L. Malerba, A. Caro, P. Olsson, and M. Lavrentiev, J. Nucl. Mater. 385, 268 (2009).
$^{28}$T. P. C. Klaver, personal communication, Workshop Fe-Cr, Genoa (30 March 2009).