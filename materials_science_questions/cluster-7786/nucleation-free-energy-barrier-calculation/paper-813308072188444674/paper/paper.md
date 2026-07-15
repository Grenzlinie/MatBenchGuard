# Observation and modeling of polycrystalline grain formation in $Ge_2Sb_2Te_5$

Geoffrey W. Burr', Pierre Tchoulfian, Teya Topuria, Clemens Nyffeler, Kumar Virwani, Alvaro Padilla, Robert M. Shelby, Mona Eskandari', Bryan Jackson, and Bong-Sub Lee'

Citation: *J. Appl. Phys.* **111**, 104308 (2012); doi: 10.1063/1.4718574
View online: http://dx.doi.org/10.1063/1.4718574
View Table of Contents: http://aip.scitation.org/toc/jap/111/10
Published by the American Institute of Physics

---

## Articles you may be interested in
Nanoscale nuclei in phase change materials: Origin of different crystallization mechanisms of Ge2Sb2Te5 and AgInSbTe
*J. Appl. Phys.* **115**, 063506063506 (2014); 10.1063/1.4865295

Crystallization dynamics of nitrogen-doped Ge2Sb2Te5
*J. Appl. Phys.* **105**, 104902104902 (2009); 10.1063/1.3126501

Distribution of nanoscale nuclei in the amorphous dome of a phase change random access memory
*J. Appl. Phys.* **104**, 071907071907 (2014); 10.1063/1.4865586

---

![](./images/813308072188444674_1.jpg)

![](./images/813308072188444674_2.jpg)

# Observation and modeling of polycrystalline grain formation in $Ge_2Sb_2Te_5$

Geoffrey W. Burr, $^{1,a)}$ Pierre Tchoulfian, $^{1}$ Teya Topuria, $^{1}$ Clemens Nyffeler, $^{1}$
Kumar Virwani, $^{1}$ Alvaro Padilla, $^{1}$ Robert M. Shelby, $^{1}$ Mona Eskandari, $^{1,b)}$
Bryan Jackson, $^{1}$ and Bong-Sub Lee $^{2,c)}$

$^{1}$IBM Almaden Research Center, 650 Harry Road, San Jose, California 95120, USA
$^{2}$Department of Materials Science and Engineering and the Coordinated Science Laboratory,
University of Illinois at Urbana-Champaign, 1304 West Green Street, Urbana, Illinois 61801, USA

(Received 23 September 2011; accepted 18 April 2012; published online 21 May 2012)

The relationship between the polycrystalline nature of phase change materials (such as $Ge_2Sb_2Te_5$) and the intermediate resistance states of phase change memory (PCM) devices has not been widely studied. A full understanding of such states will require knowledge of how polycrystalline grains form, how they interact with each other at various temperatures, and how the differing electrical (and thermal) characteristics within the grains and at their boundaries combine through percolation to produce the externally observed electrical (and thermal) characteristics of a PCM device. We address the first of these tasks (and introduce a vehicle for the second) by studying the formation of fcc polycrystalline grains from the as-deposited amorphous state in undoped $Ge_2Sb_2Te_5$. We perform ex situ transmission electron microscopy membrane experiments and then match these observations against numerical simulation. Ramped-anneal experiments show that the temperature ramp-rate strongly influences the median grain size. By truncating such ramped-anneal experiments at various peak temperatures, we convincingly demonstrate that the temperature range over which these grains are established is quite narrow. Subsequent annealing at elevated temperature appears to change these established distributions of grain sizes only slightly. Our numerical simulator—which models nuclei formation through classical nucleation theory and then tracks the subsequent time- and temperature-dependent growth of these grains—can match these experimental observations of initial grain distributions and crystallization temperature both qualitatively and quantitatively. These simulations show that the particular narrow temperature range over which crystallization occurs shifts as a function of temperature ramp-rate, which allows us to quantify the lower portions of the time-temperature-transformation map for $Ge_2Sb_2Te_5$. Future experiments and extensions of the simulator to investigate temperature-dependent interactions between neighboring grains, and to study nucleation from within the melt-quenched amorphous state, are discussed. © 2012 American Institute of Physics. [http://dx.doi.org/10.1063/1.4718574]

## I. INTRODUCTION

Phase change memory (PCM) is enabled by the large re- sistance contrast between the crystalline and amorphous states of a phase change material. $^{1-3}$ Since PCM potentially offers advantages in speed, endurance, and scalability, it has become one of the emerging non-volatile memory candidates being considered for storage class memory $^{4}$ and possibly even for replacing NAND Flash. $^{5}$ The large resistance con trast of PCM also opens up the possibility of multi-level cells (MLC), in which more than one bit is stored in each physical device. However, the potential of MLC has been constrained by the phenomenon of resistance drift, $^{6-8}$ where relaxation of the amorphous state after quenching causes device resis- tances to increase slowly over time.

Theoretical explanations of resistance drift $^{9-13}$ have focussed on physical mechanisms (defect annihilation, etc.) at work within the amorphous plug. Less well appreciated are the implications of the fact that the crystalline portions of a PCM device will be composed of a random distribution of polycrystalline grains, each separated from the next by a thin grain boundary, whose physical properties are assumably very similar to those of the amorphous phase. $^{14}$ The previ ously unsuspected role of polycrystalline grains in the aggre- gate thermal properties of PCM materials has recently begun to receive attention. $^{15,16}$

In the context of the aggregate electrical properties, this new insight into the nature of the intermediate resistance states in PCM devices (e.g., those states between full RESET and full SET) can help explain a large number of previously confusing observations about PCM devices and resistance drift. The observation that the drift coefficient varies stochas- tically from shot-to-shot within the same device $^{8,14}$ can be attributed to the re-randomization of the grain distribution af- ter each programming event, while the observed "telegraph- like noise" $^{17,18}$ may come from the changes in percolation current pathways as these ultra-thin boundaries between grains evolve subtly over time. Since this evolution depends on the balance of surface and volume energies at both crystalline-amorphous and polycrystal-polycrystal bounda- ries, it is not surprising to find a correspondence between the

$^{a)}$Electronic address: gwburr@us.ibm.com.
$^{b)}$Current address: Department of Materials Science and Engineering, Stanford University, Stanford, California 94305, USA.
$^{c)}$Current address: Invensas Corp., 2702 Orchard Parkway, San Jose, California 95134, USA.

activation energies of crystallization and resistance drift, $^{10}$ nor to find that pressure can affect resistance drift $^{19}$ through its impact on these surface energies. The large number of polycrystalline grain boundaries participating in the aggregate device resistance provides a source for the "multiexcitations" associated with the Meyer-Neldel rule behavior observed in PCM devices. $^{10,12}$ And finally, polycrystalline grains provide a plausible explanation for why non-zero resistance drift is observed even in lower-resistance intermediate states, where the vast majority of the electrical current must clearly be passing around (and not through) a tiny, residual amorphous plug. $^{7,8,14}$ On the other hand, however, this insight discards little from the published physical explanations that connect drift with the relaxation of the amorphous phase-it is just that the "effective amorphous thickness" discussed in many of these papers may in fact be residing within the mostly contiguous amorphous plug, or at the grain boundaries between polycrystalline grains, or both.

This discussion illustrates the importance of improving upon our understanding of polycrystalline grains: how they are created, how they interact with each other at various temperatures, and how the grains and their boundaries combine through percolation to produce the externally observed electrical and thermal characteristics of a PCM device. While grain size can be roughly inferred from the width of x-ray diffraction peaks, $^{20}$ more direct evidence over smaller regions can be obtained with transmission electron microscopy (TEM).

The crystallization process in $Ge_{2}Sb_{2}Te_{5}$ has been studied with TEM by a number of authors, $^{16,21-26}$ but only for fairly low-temperature, isothermal anneals in extremely thick, uncapped samples subject to oxidation. In fact, the crystal-growth process in such thick films has been shown to occur in two distinct steps, $^{21,22}$ driven by grains that quickly become much wider than they are thick. As they grow large, these grains then show noticeable distortions of the crystalline lattice. $^{22,23,27}$ These distortions have been attributed to the large (6%) volume difference between the amorphous and crystalline phases. $^{28}$ While a number of these in situ TEM studies have captured the crystallization process in progress, it has also been shown that the electron beam itselfcan readily induce crystallization. $^{29}$

Researchers have typically attempted to analyze such measurements using the Johnson-Mehl-Avrami-Kolmogorov (JMAK) formalism, $^{21,30}$ and estimates have been made for steady-state nucleation and growth rates $^{22,31-33}$ using both TEM and Atomic Force Microscopy (AFM). Unfortunately, later studies have shown that the JMAK formalism cannot adequately describe the nucleation and growth in phase change materials such as $Ge_{2}Sb_{2}Te_{5}$, and that only classical nucleation theory can predict such observed phenomena as incubation $^{34}$ and the effects of priming. $^{35}$ In addition to nucleation rate, Privitera et al. $^{33}$ also analyzed grain size distributions during the first stages of crystallization over a small range of various low-temperature isothermal anneals.

In contrast to the films studied by TEM, a typical PCM device contains a thin (30-60nm) layer of $Ge_{2}Sb_{2}Te_{5}$ (or other phase change material) which is well protected from oxidation by encapsulation. This phase change material is then crystallized during fabrication by an extended iso-thermal anneal, but at a temperature $(200^{\circ}C-400^{\circ}C)$ where the crystallization process is too rapid to be observed in progress.

In this paper, we study the formation of fcc polycrystalline grains from the as-deposited amorphous state in $Ge_{2}Sb_{2}Te_{5}$ with a combination of ex situ TEM membrane experiments and numerical simulations of nucleation and growth using classical nucleation theory. Capped films are used to prevent oxidation of the $Ge_{2}Sb_{2}Te_{5}$. Although post crystallization ex situ examination precludes observation of crystallization in progress, it does allow for precise temperature control and greatly reduces the worry of electron-beam-induced effects. Also, since the membranes were TEM-ready, no damage associated with TEM specimen preparation was incurred. We show, using ramped-anneal experiments, that PCM materials annealed at high temperatures actually complete their crystallization during the ramp up to that anneal temperature. Thus, it is this ramp-rate (typically not reported or even noted) which is actually more important in determining the polycrystalline grain structure than the peak anneal duration and temperature which are dutifully reported.

Our numerical simulator-which models nuclei formation through classical nucleation theory and then tracks the subsequent time- and temperature-dependent growth of these grains-can match these experimental observations of grain distributions and crystallization temperature both qualitatively and quantitatively, providing a map of the lower portions of the time-temperature-transformation (TTT) map. The prospect and importance of future TEM-membrane experiments and extensions of the simulator, for investigating the temperature-dependent interactions between neighboring grains as well as nucleation from within the melt-quenched amorphous state, are discussed.

## II. TEM MEMBRANE EXPERIMENTS

Physical vapor deposition was used to prepare thin films of $Ge_{2}Sb_{2}Te_{5}$ (GST) encapsulated in SiN on TEM membrane samples in an sputtering deposition tool (AJA International). Several different types of membranes were used, composed of either silicon or SiN thinned down to thicknesses of 9 nm,15 nm or 30 nm within 1-9 small windows on the sample.These windows ranged in area from nine $100\ \mu m\times 100\ \mu m$ apertures up to a single $500\ \mu m\times 500\ \mu m$ window. Before deposition, a 100W (RF) argon-ion mill was performed to clean the surface of the membrane. A first layer of 5 nm of SiN was deposited from a silicon target under a mixed nitrogen-argon atmosphere (0.27 Pa, Ar 40 sccm flow, $N_{2}$ 10 sccm), followed by 30 nm of GST deposited under argon atmosphere (0.27 Pa, Ar 40 sccm flow) with a DC power of 10 W on the compound GST sputter-target. Finally, a 15 nm SiN capping layer was added, using the same deposition conditions as the first layer, to prevent oxidation of the GST film during annealing or measurement. All depositions were carried out at room temperature without breaking vacuum, resulting in amorphous-as-deposited samples with minimal exposure to oxygen. Typically, three membranes and one witness sample (an un-patterned silicon wafer) were deposited simultaneously. Rutherford back-scattering results on samples

![](./images/813308072188444674_3.jpg)

deposited under identical conditions have shown a composi-
tion of $Ge_{21.2}Sb_{28.4}Te_{50.4}.^{36}$

Two annealing tools were used to perform ramped-anneals
under controlled conditions. A rapid thermal anneal (RTA) tool
(AllWin21 AccuThermo W810) was used to perform both fast
ramp anneals (from $40\,^{\circ}\text{C}$ to $220\,^{\circ}\text{C}$ under helium flow with a
heating rate of $380\,^{\circ}\text{C}/\text{min}$, as well as moderate ramped
anneals (nitrogen flow from $130\,^{\circ}\text{C}$ to $220\,^{\circ}\text{C}$ at $7.5\,^{\circ}\text{C}/\text{min}$).
For slow ramps, a Lindberg furnace was used to ramp in a con-
trolled manner from 100 to $220\,^{\circ}\text{C}$ under nitrogen flow at
$0.17\,^{\circ}\text{C}/\text{min}$. Using the numerical simulator introduced later in
the paper, we calculate that the thermal time-constant by which
the center of the membrane responds to temperature changes
at the edge of the membrane is $<25$ ms, even for our largest
membrane ($500\times 500\,\mu\text{m}^{2}$, 15 nm of SiN). Thus even for the
fastest temperature rates ($380\,^{\circ}\text{C}/\text{min}$), the entire membrane
should differ in temperature by no more than $0.15\,^{\circ}\text{C}$. After
these anneals, each sample was imaged in an JEOL 2010F
TEM operating at 200 keV.

The left side of Figure 1 shows the grain distributions as
indicated by bright-field TEM imaging through three TEM
membranes after ramped-anneals at widely varying rates,
ranging from $380\,^{\circ}\text{C}/\text{min}$ down to $0.17\,^{\circ}\text{C}/\text{min}$. As is typical
in such TEM images, a number of the grains stand out as
darker, being oriented with respect to the incoming beam
and collection system such that the diffraction contrast is
particularly high. Diffraction analysis (not shown) reveals
that most of these films are in the fcc crystalline phase,
although a small part of the film, particularly for the slowest
anneal, appears to have already crystallized into the more
stable hexagonal phase. $^{37}$ Similar behavior has been reported
by other researchers for GST-based materials. $^{23}$

In order to quantify the grain size distributions in these
images, we used an open source image manipulation software
tool (ImageJ, $^{38}$ together with the particle size analyzer macro $^{39}$).
After removing high-frequency noise with a median filter, a sim-
ple threshold operation (no “watershedding”) performed on
each $2048\times 2048$ pixel image assigned pixels into discrete and
contiguous “dark” grains, representing approximately 12%-14%
of the total image area. Some contrast variation exists between
white and grey among the non-dark grains, but not enough for
reliable size extraction. A minimum diameter value of 10 nm
and circularity of 0.1 (set low in order to preserve non-circular
grains) were used to reject artifacts.

The resulting table of grain areas for each image was
sorted in order of decreasing area and plotted as a cumulative
distribution function (CDF)—e.g., fraction of area covered
as a function of the number of grains. As shown in Figure

![](./images/813308072188444674_4.jpg)

FIG. 1. TEM (left) and simulated (right) grain images for three different
ramp-rates (380, 7.5, and $0.17\,^{\circ}\text{C}/\text{min}$). All images are shown at the same
scale, each corresponding to an area of $886\text{nm}\times 886\text{nm}$. For the fast ramp,
a 15 nm SiN membrane (Ted Pella, Inc.) was used, for the medium ramp a
9 nm amorphous silicon membrane (TEM windows, SimPore, Inc.), and for
the long ramp, a 30 nm SiN membrane (SPI). In the grain images from our
classical nucleation theory simulator, yellow represents a crystalline voxel
and brown a grain boundary.

![](./images/813308072188444674_5.jpg)

FIG. 2. Cumulative distribution of area covered by polycrystalline grains,
from largest to smallest, according to image analysis of (a) the TEM images
from Figure 1 and (b) the grain sizes obtained directly from simulation. For
each simulated ramp-rate, ten different simulations with different random
seeds were run. Large grains will lead to a steep curve, while numerous
small grains will result in a much more gentle curve.

<table><caption>Table I. Median grain area and effective diameter, as obtained from the slope of the inset plots in Figure 2, for both the TEM and simulated grain images in Figure 1. For the simulations, the median grain area was computed for each instance separately and then averaged across the ten simulations run at the same ramp-rate.</caption>
<tbody><tr><th></th><td>From TEM</td><td>From simulation</td></tr>
<tr><th>380 °C/min</th><td>497 nm² (25.2 nm)</td><td>579 nm² (27.1 nm)</td></tr>
<tr><th>7.5 °C/min</th><td>918 nm² (34.2 nm)</td><td>1188 nm² (38.9 nm)</td></tr>
<tr><th>0.17 °C/min</th><td>1552 nm² (44.5 nm)</td><td>1601 nm² (45.1 nm)</td></tr>
</tbody></table>

2(a), these plots all rise monotonically. However, a TEM image with a few large grains will be associated with a very steep grain-CDF curve, while an image with many small grains will give rise to much more gentle CDF. Since the “dark” grains covered only a portion of each TEM image, we have normalized from this subset of the image up to 100% of the area. Thus if, within the 12% of the image occupied by dark grains, the 20 largest grains could account for half of this territory (e.g., 6% of the total image), we assume that the largest $(20 \times (100/12) \sim )$ 167 grains (of all types of diffraction contrast) would similarly account for 50% of the entire image. This requires only that the distribution of sizes among “dark” grains is representative of the distribution over all the grains. This is an entirely reasonable assumption, since which grains were “dark” depended strongly on the particular effectively-random specimen tilt, and since all diffraction patterns were distributed isotropically in angle.

We define the “median” grain-size by the inverse of the slope of each curve as it passes through 50%—this is the median grain in the sense that half of the area is covered by larger grains, and half by smaller grains. Table I tabulates the area and effective diameter of this median grain for the three different ramp-rates. Table I and Figure 2(a) quantify what is visually clear from the left side of Figure 1: the median grain size after an anneal increases as the ramp-rate of the anneal decreases (slows down), and it takes fewer grains to cover 50% of the area.

Thus even as an isothermal anneal at some temperature above 200 °C begins, the sample is mostly likely already crystallized, with an average grain-size that depends on the rate of the temperature ramp. As has long been known from measurements of resistance vs. temperature characteristics, crystallization occurs rapidly within a narrow temperature range centered around the so-called “crystallization temperature” $T_{c}^{40,41}$ In addition, the value of $T_{c}$ is itself known to be a function of the ramp-rate.⁴⁰ The knowledge we add here is that different ramp-rates lead not only to different temperatures at which crystallization occurs but also different grain size distributions.

Figure 3(a) shows measured resistance vs. temperature characteristics for anneals driven through the full crystallization process, as well as some anneals which were truncated at various peak temperatures. Here, the same deposition of GST and encapsulating SiN described earlier was performed on silicon wafer pieces pre-patterned with a pair of underlying, large-area aluminum pads. The bottom SiN layer was omitted in order to allow electrical contact to the GST, and large portions of the pads were masked during deposition. The gap between the two 10 mm wide pads, where current is forced to pass through the heated $Ge_{2}Sb_{2}Te_{5}$, was 1 mm in size. Since the oven used for these experiments is not as reliable as those used in the earlier experiments, the ramp-rates in these scans vary from 67 °C–96 °C/min. Since the cooling rate is somewhat slower than this heating rate, a truncated ramp actually lingers within a few degrees of the peak temperature for 20–40 s, as shown in Figure 3(b). Note also that films deposited at different points in time are roughly, but not completely, repeatable in terms of crystallization temperature, differing by approximately 5–10 °C. Some of this variability may be due to the poor repeatability of this particular oven.

The left side of Figure 4 shows TEM images from various membrane samples (with deposition conditions identical to those used in Figure 1) after undergoing truncated anneals in the same oven used for the experiments of Figure 3.

![](./images/813308072188444674_6.jpg)

FIG. 3. (a) Resistance vs. temperature, and (b) temperature vs. time for experimental truncated ramp-anneals. For comparison, part (b) also includes, plotted in red squares, the piecewise-linear temperature-vs-time trajectory used for numerical simulation of the 146 °C truncated anneal.

![](./images/813308072188444674_7.jpg)

FIG. 4. TEM (left) grain images for five different peak temperatures (138, 143, 148, 150, and 152 °C), and simulated (right) grain images at every 2 °C between 142 and 150 °C, using temperature-time trajectories similar to the one shown in Figure 3. Except for the TEM of the still-amorphous sample (truncated at 138 °C) which shows a 90nm × 90nm region, all images are shown at the same scale, corresponding to an area of 886 nm × 886 nm. A slight sample-to-sample non-repeatability of ramp profile, ramp-rate (67–96 °C/min), and precise crystallization temperature due to stoichiometry fluctuations may be why the membranes with anneals truncated at 143 °C and 148 °C both appear to be only slightly crystallized. In the grain images from our classical nucleation theory simulator, yellow represents a crystalline voxel, brown a grain boundary, and cyan a voxel which is still amorphous (for which sub-critical nucleation is tracked).

A truncated anneal that peaked at 138 °C appears to leave the sample in a completely amorphous state, while a truncated anneal that briefly reached 152 °C has fully crystallized the sample. Although there is noticeable sample-to-sample variation in exact crystallization temperature, clearly crystallization is taking place in a temperature range of approximately 12–15 °C.

### III. IMPLEMENTATION OF CLASSICAL NUCLEATION THEORY SIMULATOR

The numerical simulator described here for modeling nucleation and growth of $Ge_2Sb_2Te_5$ through classical nucleation theory combines the approaches of Senkader and Wright³⁴ with that of Salinga.⁴² The formation of a spherical (or hemi-spherical) crystalline nucleus requires a free energy,

$$
\Delta G(n)=f(\theta)\left[4 \pi r^{2}(n) \sigma-n \Delta g\right], \tag{1}
$$

where $n$ is the number of GST "monomers" (unit cells) in the nucleus, $r(n)$ is its radius, $\sigma$ is the surface energy density between amorphous and crystalline phases, and $\Delta g$ is the bulk free energy difference (per monomer) between amorphous and crystalline. The relationship between the volume of a nuclei and the number of "monomers" it contains is fixed by the effective monomer volume, $v_m$. Here, as in Ref. 34, we use $v_m=2.9 × 10^{-28} \text{m}^3$.

The parameter,

$$
f(\theta)=2-3 \cos (\theta)+\cos ^{3}(\theta) / 4, \tag{2}
$$

describes the effects of the "spherical cap" model, where the tiny crystalline nucleus can reduce its free energy of formation by nestling against an interface or defect ("heterogeneous nucleation"), as parameterized by the interface or "wetting" angle, $\theta.^{42,43}$ Note that Eq. (1) is a reduced form, with no mention of the reduced surface energy between the nucleus and interface, because this second surface energy can itself be specified in terms of $\theta$ and the primary crystalline-amorphous $\sigma.^{42}$ To model the increase in the bulk free energy difference between amorphous and crystalline at temperatures far below the melting point $T_m$, we have obtained the best results with the Hoffmann model,⁴²

$$
\Delta g=\Delta H_{f} v_{m} \frac{T_{m}-T}{T_{m}} \frac{T}{T_{m}}, \tag{3}
$$

where $T$ is absolute temperature and $\Delta H_{f}$ is the enthalpy of fusion at the melting point $(6.1 × 10^{8} \text{J/m}^3$ for GST).³⁴

As in Ref. 34, we track a histogram of sub-critical nuclei of varying size $n$ by simultaneously solving a large set of rate equations for nucleus growth and decay over each timestep. For instance, the pool of nuclei of size $n$ can lose population by having nuclei grow to size $n+1$ (at gain rate $\Gamma_g^n$), gain population by having nuclei of size $n+1$ lose one monomer (at decay rate $\Gamma_d^{n+1}$), and similarly exchange population with the pool of nuclei of size $n-1$. These rates depend exponentially upon the free energy $\Delta G(n)$ from Eq. (1),

$$
\Gamma_{g}^{n}=q(\theta) c_{g}(n) \gamma \exp \left(\frac{-\Delta G(n)}{2 k_{B} T}\right), \tag{4}
$$

$$
\Gamma_{d}^{n+1}=q(\theta) c_{l}(n+1) \gamma \exp \left(\frac{\Delta G(n+1)}{2 k_{B} T}\right), \tag{5}
$$

where $k_B$ is Boltzmann's constant, and $q(\theta)=(1-\cos (\theta)) / 2$ quantifies the effect of a spherical cap. As the area of the outer shell of the nucleus grows larger, the number of places where the single monomer addition (deletion) events being tracked by these rate equations could occur increases, as quantified by

$$
c_{g}(n)=c_{l}(n+1)=4 \pi(3 n / 4 \pi)^{\frac{2}{3}}. \tag{6}
$$

Finally, the jump attempt rate $\gamma$ is an extremely important parameter, being tied to the viscosity $\eta$ and nearest-neighbor distance $\lambda$ (0.299 nm in $\mathrm{Ge}_{2} \mathrm{Sb}_{2} \mathrm{Te}_{5}$ (Ref. 34)) as
$$
\gamma=\frac{k_{B} T}{3 \pi \lambda^{3} \eta}. \quad(7)
$$

As in Ref. 42, we model the temperature dependence of viscosity as an exponential with activation energy $E_{a}$ for temperatures below the glass transition temperature $T_{g}$, and with the Vogel-Fulcher-Tammann equation above it,
$$
\eta= \begin{cases}\eta_{0} \exp \left(\frac{-E_{a}}{k_{B} T}\right) & T \leq T_{g} \\ \eta_{1} \exp \left(\frac{-D T_{f v}}{T-T_{f v}}\right) & T>T_{g},\end{cases}
\quad(8)
$$
as is appropriate for a fragile glass-former such as $\mathrm{Ge}_{2} \mathrm{Sb}_{2} \mathrm{Te}_{5}$ and other phase-change materials. $^{42}$ Here, $D$ and the proximity of $T_{f v}$ to $T_{g}$ control the fragility (e.g., how steeply the viscosity drops at temperatures just above $T_{g}$ ), while $\eta_{0}$ and $\eta_{1}$ are chosen simply to force the two regimes to meet at $T_{g}$.

Although there are some minor differences in the equations and models, to this point our description of sub-critical nucleation $^{35}$ is quite similar to the work of Ref. 34. However, there are three areas where our implementation differs significantly from this earlier approach. First, after critical nucleation has occurred and a nucleus is much more likely to grow than shrink, we track its evolution using a growth velocity $v_{g}$ evaluated consistently from Eqs. (4) and (5),
$$
v_{g}(n)=v_{m} \frac{\Gamma_{G}-\Gamma_{D}}{4 \pi r^{2}(n)}, \quad(9)
$$
up to values of $n=20000$, where this velocity tends to saturate. This reduces the coding demands on tracking very large histograms and allows the grain to grow asymmetrically in the presence of spatially inhomogeneous temperature distributions.

Within the simulation code, these super-critical nuclei (or, equivalently, polycrystalline grains) grow by propagating independently tracked local spherical wavefronts in all the crystal-growth-front voxels at the boundaries of the grain. Once a crystal-growth-front voxel is fully covered by these wavefronts, and all of its 26 neighboring voxels are also at least partially crystallized, the voxel becomes a fully crystalline cell and no further growth is tracked for it. Note that here we evaluate Eqs. (4) and (5) with $\theta=180^{\circ}$, akin to assuming that a large grain, although it may have originally been nurtured by a defect or interface, is now propagating through the bulk of the phase change material where only homogeneous nucleation can occur.

Second, we adjust the low temperature viscosity (using $E_{a}$ and $\eta_{0}$ ) so that the growth velocities that the simulation evaluates according to Eq. (9) exactly match those measured by AFM in the temperature regime between $115^{\circ} \mathrm{C}$ and $145^{\circ} \mathrm{C} .{ }^{44,45}$ Note that viscosity (Eq. (8)) affects $v_{g}$ (Eq. (9)) through the influence of $\gamma$ (Eq. (7)) on $\Gamma_{g}$ and $\Gamma_{d}$ (Eqs. (4) and (5)). Then we adjust the high temperature viscosity (through $\eta_{1}, D$, and $T_{f v}$ ) so that growth velocities around $450{ }^{\circ} \mathrm{C}$ are high enough to explain the fast crystallization speed observed in the optical measurements. $^{28,46,47}$ This also allows the nucleation rate to drop back down at temperatures just below melting, as has been demonstrated experimentally. $^{48}$

Although the full evolution of the rate equations inside the simulator is required to evaluate the dynamic and history-dependent $^{35}$ nucleation rate, for the purposes of tuning parameters between runs we can roughly quantify the nucleation by the steady-state nucleation rate,
$$
I_{s s}=\left(4 / v_{m}\right) \gamma n_{c}^{2 / 3} Z \exp \left(-\frac{\Delta G_{c}}{k_{B} T}\right), \quad(10)
$$
where $n_{c}=f(\theta) \frac{32 \pi}{3} v_{m}^{2} \sigma^{3} \Delta g^{-3}$ and $\Delta G_{c}=f(\theta) \frac{16 \pi}{3} v_{m}^{2} \sigma^{3} \Delta g^{-2}$ are the critical nuclei size and the free energy barrier at this nuclei size, while the Zeldovich factor is $Z=\sqrt{\Delta g /\left(6 \pi k_{B} T n_{c}\right)} .^{34}$

The resulting curves for growth velocity $v_{g}$ and steady-state nucleation rate $I_{s s}$ are shown as a function of temperature in Figure 5. The technological attractiveness of phase change memory is immediately apparent: the growth velocity, $v_{g}$, changes by 16 orders of magnitude over a range of just a few hundred degrees Celsius. This massive change in crystallization speed is what allows phase change materials to switch in the $<100$ ns regime during operation, yet be able to offer ten-year data lifetimes even at temperatures above $100^{\circ} \mathrm{C} .^{3,41}$

The third, and probably most significant difference between our implementation and those of previous work, is that we track a unique histogram of sub-critical nuclei at each and every phase-change voxel within an electro-thermal simulator-which itself is capable of modeling both electrical device $^{49}$ and optical characterization $^{46}$ experiments. This means that we can model heterogeneous nucleation using classical nucleation theory and then follow the resulting evolution of the super-critical polycrystalline grain

![](./images/813308072188444674_8.jpg)

FIG. 5. Crystal growth velocity, $v_{g}$, and steady-state nucleation rate, $I_{s s}$, as a function of temperature. The inset replots $v_{g}$ on a linear scale in the high temperature regime. Both the melting temperature $T_{m}$ and glass transition temperature $T_{g}$ are shown. Symbols at lower left show low-temperature crystal growth velocities obtained experimentally with AFM measurements. $^{44}$

even in environments with large temperature gradients. By defining the differing (but not well-known) electrical and thermal properties of the grains and their boundaries, we can also evaluate the effective electrical and thermal characteristics (resistance, effective thermal conductivity) due to percolation effects. Example applications include modeling the crystallization induced by an optically heated laser spot³⁵ or the SET operation within a PCM device.

In addition to those parameters mentioned already, other parameters we can obtain directly from the literature include $T_m$ $=627\,^\circ\text{C},^{34}E_a=2.3$ eV,⁴⁴ and $T_g=155\,^\circ\text{C}.^{44}$ Those parameters we deduce by fitting the low and high temperature growth velocities as discussed above include $\eta(T_g)=1.6510^8$ Pa s, $D=24.25$, and $T_{fv}=120\,^\circ\text{C}$. Heterogeneous nucleation ($\theta=90^\circ$) is assumed to occur at the GST-SiN interfaces, with homogeneous nucleation ($\theta=180^\circ$) everywhere else. Finally, after successive simulations performed at various $\sigma$ values, $\sigma=0.060$ J/m² provided the best match to grain sizes shown in Figure 2.

While it is slightly surprising that the viscosity at $T_g$ is significantly lower than the value typically associated with the glass transition ($10^{12}$ Pa s), we have observed that by moving $\lambda$, $\Delta H_f$, and $v_m$ slightly away from their reported literature values, we can use a significantly larger value of $\eta(T_g)$ yet still obtain temperature dependencies for $v_g$ that are similar to those shown in Figure 5. This is not unreasonable, since measurements of these literature parameters appear to be associated with fairly significant error bars. We have also observed that these nucleation simulations tend to be extremely sensitive to changes in one variable: for instance, modifying $\sigma$ from 0.060 to 0.055 (or 0.065) changes the predicted median grain-size after a $7.5^\circ\text{C}/\text{min}$ ramp-anneal from 38.9 nm to 17.2 nm (or 73.7 nm). That said, it is also clear that a number of different parameter *sets* can produce $v_g$ and $I_{ss}$ curves resembling those in Figure 5, each of which invariably leads to grain size predictions very similar to those shown in Figure 2.

It is quite likely that the particular value of $\sigma$ which matches with our results is closely associated with the local stress environment present in our membrane films. By constraining the volume change associated with crystallization, the SiN capping layer introduces different local stresses than would be present for an uncapped film, particularly as crystallization proceeds. In thicker films, it is even possible that the heterogeneous crystallization of boundary layers could modify the effective $\sigma$ or other parameters that then govern the ensuing crystallization of the remainder of the film. This points out both the importance of using a capped membrane configuration so as to more closely correspond to the encapsulated electronic PCM devices of future interest, and the danger of having only data from uncapped films to draw upon for low-temperature velocities.⁴⁴,⁴⁵ However, capping layers tend to have a smaller influence on crystallization behavior (compare the uncapped and capped results for undoped $\text{Ge}_2\text{Sb}_2\text{Te}_5$ films in Refs. 36 and 47) than either doping or material composition. Given the observed strong sensitivity of crystallization behavior to the $\sigma$ parameter, it is likely that the changes in $\sigma$ for an uncapped film would be modest.

## IV. SIMULATIONS OF POLYCRYSTAL NUCLEATION AND GROWTH

At the right side of Figures 1 and 4, and in Figure 2(b), we show the results of simulated ramp-anneals using our classical nucleation theory simulator. For the truncated-anneal simulation, piecewise-linear temperature trajectories similar to the one shown in Figure 3(b) were used to mimic the temperature exposure experienced by the membranes. Since, as shown in Figure 2(b) and Table I, the predicted distributions of grain sizes are quantitatively very similar to those seen in the TEM images, the simulated grain images shown in Figure 1 are visually quite similar to those measured with TEM.

In order to eliminate numerical artifacts and to permit even un-physically rapid anneals to be simulated, the usual thermal diffusion code was bypassed. Instead, the isotropic temperature at each timestep of a simulated temperature ramp was directly and instantaneously updated throughout the simulation. Thus, the slight self-heating from the exothermic crystallization process, which would otherwise be correctly modeled, was also effectively disabled. These simulations span $204\times 204\times 43$ voxels of size $5\,\text{nm}\times 5\,\text{nm}\times 2.5\,\text{nm}$, of which 475 212 (corresponding to $\sim995\,\text{nm}\times 995\,\text{nm}\times 30\,\text{nm}$) are modeled as GST cells. Heterogeneous nucleation is tracked in the 79 202 GST voxels in contact with either SiN on top or bottom (with $\theta=90^\circ$), and homogeneous nucleation is implemented elsewhere ($\theta=180^\circ$). At the lateral simulation boundaries, the interfaces between GST and the surrounding "air" were modeled with $\theta=180^\circ$.

Only the topmost layer of phase-change voxels from the center $886\,\text{nm}\times 886\,\text{nm}$ is shown in Figures 1 and 4—here yellow represents a crystalline voxel and brown a grain boundary. In order to show these grain boundaries clearly, each voxel is mapped to $3\times 3$ pixels for display purposes, with the outer ring of these pixels assigned based on whether the laterally neighboring voxel shares the same grain "ID" generated at the instant of critical nucleation. In this way, even a single-voxel polycrystalline grain results in one yellow pixel surrounded by a ring of brown pixels.

Although only the topmost layer is shown, other layers within the simulation were visually very similar, and produced grain-size distribution plots indistinguishable from those shown in Figure 2(b). We also tried volume-weighting the simulated grain ID information, counting areas only where a grain occupied more than half the 30 nm thickness, as an analogue to those grains with significant diffraction contrast in the TEM images. Even in this case, almost all of the grain-size distributions were effectively identical to Figure 2(b), including the inset plot identifying the size of the median grain. Only the topmost 5% of the volume-weighted grain-size distribution volume weighting was markedly different, since simulation grid-cells where no grain occupied more than half the thickness were randomly assigned a grain-ID.

Figure 4 shows that the same temperature-time trajectories explored experimentally in our truncated-ramp-anneal experiments also lead to partial crystallization in simulation. However, it is possible with simulation to explore a much
![](./images/813308072188444674_9.jpg)

wider range of temperature ramp-rates than is feasible exper-
imentally. We have summarized the results of many different
ramp-rate simulations in Figure 6. Here, we plot, on a curve
of temperature vs. time spent within $1\ ^{\circ}\text{C}$ of that temperature,
curves representing various observations of fractional crys-
tallization. This main curve here is effectively the TTT plot
for $\text{Ge}_{2}\text{Sb}_{2}\text{Te}_{5}$ according to our simulation. There are eight
curves, corresponding to crystal fractions of $10^{-6}$, $10^{-5}$,
$10^{-4}$, 0.1%, 1%, 10%, 50%, and 99%. Along the top, the
horizontal axis is also described in terms of linear ramp-rate.
Each simulation is run at constant ramp-rate, thus providing
the data points which share the same time-at-temperature
(same horizontal position in the main graph). From this plot,
it is clear that each ramp-rate is associated with a particular,
fairly narrow temperature range—within which the entire
crystallization process occurs.

The insets in Figure 6 detail this crystallization process as
it occurs within the simulator for a ramp-rate of $81\ ^{\circ}\text{C}/\text{min}$,
corresponding to the rate used during the resistance vs. tem-
perature measurements shown in Figure 3. At upper right, the
evolution of the crystal fraction is shown as a function of tem-
perature. The appearance of the first crystal growth voxels
(roughly similar to the first critical nucleation) and the appear-
ance of the first fully crystallized voxels are indicated. Note
that the threshold monomer size for converting a voxel from a
“sub-critical nuclei” cell to a “crystal-growth” cell is inten-
tionally set somewhat larger than the critical nucleus size
($n\geq13$). This is because nuclei that are at or slightly over the
critical nucleus size do have a non-zero chance of shrinking
back over this threshold, even though it is more likely that
they will continue to grow.

Also shown at the middle right of Figure 6 is the simu-
lated resistance during the $81\ ^{\circ}\text{C}/\text{min}$ simulation. Here, two
electrodes were added to the simulation and the resistance
through the GST film was computed by solving Laplace’s
equation, evolving the voltage mesh with a three-
dimensional alternating-direction-implicit (ADI) finite-
difference solver until Kirchoff’s current law was satisfied at

![](./images/813308072188444674_10.jpg)

FIG. 6. The TTT diagram for $\text{Ge}_{2}\text{Sb}_{2}\text{Te}_{5}$ according to numerical simulations, showing the temperature and time-at-temperature combinations where crystal frac-
tion reaches $10^{-6}$, $10^{-5}$, $10^{-4}$, 0.1%, 1%, 10%, 50%, and 99%. The top horizontal axis shows the corresponding linear ramp-rate in $^{\circ}\text{C}/\text{min}$. The use of a con-
stant, rate-independent $T_{g}$ in the simulations means that this TTT diagram becomes inherently less accurate as the ramp-rate increases. The inset plots at upper
right show the evolution of the simulated crystal fraction and device resistance as a function of temperature for a simulation run at a constant ramp-rate of
$81\ ^{\circ}\text{C}/\text{min}$. Insets at upper left show the evolution of the aggregate population of sub-critical nuclei at four different temperatures; insets at lower left illustrate the
distribution of partially established grains at five different temperature/time points, during this same simulation.

each node. The Douglas-Gunn ADI scheme $^{50,51}$ was used with variable timesteps in order to maintain stability for this 3-D mesh.

The electrical transition on log-coordinates (the logarithmic midpoint between SET and RESET) closely corresponds to the change in crystal fraction on linear coordinates. Although some researchers have observed that the linear electrical transition can appear to occur "before" the optical transition, $^{52}$ the midpoint on a log-resistance plot of the electrical transition is reached at very close to 50% crystal fraction.

The inset to the resistance plot shows a 350 nm wide cross-section through the film when the simulation was passing through $158\,^\circ\text{C}$. This image clearly shows that while most nuclei have started at a SiN-GST interface, there are in fact a few grains which must have nucleated in the bulk of the film, away from the interfaces. The spherical cap model greatly increases the likelihood of nucleation for the small number of monomers located at an interface. However, there are many more bulk monomers, each with a much smaller (but non-zero) chance of nucleation. These two effects counterbalance each other to a certain extent, enough so that some bulk, homogeneous nucleation can be observed with these parameters.

The inset plot in the upper center portion of Figure 6 shows the aggregate nucleus histogram (population vs. nucleus size) at four temperatures during the $81\,^\circ\text{C/min}$ simulation. At $100\,^\circ\text{C}$, there are a few nuclei containing ten monomers. However, even though the critical nucleus size is quite small (8 monomers in the bulk and around 4 monomers at the interfaces), the chances that any nuclei will grow much larger is extremely unlikely at low temperatures. As the temperature increases to $140\,^\circ\text{C}$, the critical nucleus size decreases only slightly, but the rate at which monomers attempt to grow $(\Gamma_g)$ increases significantly. Thus more nuclei begin to exceed the critical nucleus, and some actually get converted within the code into crystal growth cells. Note that when a crystal growth cell contains a growing grain that is smaller than the size of the voxel, the proportionally smaller monomer population in the remainder of the voxel continues to be tracked for sub-critical nucleation. As the temperature continues to increase, more and more nucleation occurs, and finally the consumption of available material becomes so significant that the overall sub-critical nucleus population left in the amorphous state drops noticeably. Soon afterwards, the entire simulated volume is fully crystallized.

The evolution of the grains from $156\,^\circ\text{C}$ through full crystallization at $160\,^\circ\text{C}$ is shown in the inset figures at the lower left of Figure 6. Clearly, the largest grains tend to be those that nucleated early and had the time to grow into the surrounding phase change material before critical nucleation could occur there. When the ramp-rate is very fast, there are many small grains (both experimentally and according to simulation) because the neighboring material began to nucleate "faster" than the growth velocity could propagate the edge of the nearby older grain. Once neighboring grains contact each other, the surface energy of importance changes from the crystalline-to-amorphous value of $\sigma$ to something much lower, allowing large polycrystalline grains to slowly consume area at the expense of smaller ones. This interaction is not yet implemented in our simulation code.

The trend in grain size with ramp-rate shown in Figure 1 occurs because faster ramps mean that crystallization occurs at higher temperature, combined with the obvious difference in the slopes of the $v_g$ and $I_{ss}$ curves in the regime below $T_g$ in Figure 5. Although the crystal velocity increases exponentially as temperature increases, the exponential increase in nucleation rate is even steeper. (While the nucleation within the code is dynamic, it scales quite closely to the steady-state rate $I_{ss}$ shown in Figure 5.) Fast ramps mean that the sample gets to higher temperature before crystallization has a chance to complete, and since the increase in nucleation rate with temperature outpaces the increase in growth rate, new grains are nucleating faster than the old grains can consume their surroundings. As a result, the average grain size is smaller for these fast ramps. The only simulation run which did not show a strong trend of grain size changing with ramp-rate was one where $v_g$ and $I_{ss}$ had very similar (exponential) slopes below $T_g$, which we could only bring about by significantly altering the shape of the bulk free energy difference $\Delta g$ (Eq. (3)).

## V. FURTHER DISCUSSION

While our nucleation simulation shows an admirable correspondence with the observed experimental behavior, there are still a number of physical interactions which will need to be included before real PCM device operation can be accurately modeled. In particular, once the polycrystalline grains grow large enough to touch each other, the present simulation code makes no further changes. However, the experimentally measured resistance of the phase change film in Figure 3 clearly continues to drop. In simulation, the resistance quickly saturates to a fully "SET" resistance. While some of the experimentally-observed decrease is due to temperature-dependent resistivity (already included in the simulation code), much of it is permanent-leading to significant hysteretic changes in both electrical and thermal resistance at room temperature after cooling. $^{32,53}$

This resistance change cannot be due solely to significant changes in grain size, as we show in Figure 7. Here, three membranes were annealed to $220\,^\circ\text{C}$ at a rate of $7.5\,^\circ\text{C/min}$ (same rate as the center image from Figure 1) but then held at $220\,^\circ\text{C}$ for 3, 30, or 300 min before cooling and TEM measurement. The plot of fractional area covered by the largest grains includes all four membranes which experienced exactly the same rate, differing only in holding time. Here, it is clear that the number of grains is not changing significantly, but rather that the largest grains are growing slightly in size, assumably at the expense of smaller grains.

Another consideration is that it may be the exact equivalent-amorphous-thickness of the grain boundaries, and not the average grain-size, which dominates changes in resistance after the polycrystalline grains consume all the unclaimed amorphous material. This is an important consideration for future study, since the establishment of intermediate resistance states in PCM materials is likely dominated by

![](./images/813308072188444674_11.jpg)

FIG. 7. TEM grain images and cumulative distribution of area covered by poly crystalline grains, from largest to smallest, for membrane samples exposed to 3, 30, or 300 min of additional annealing at 220 °C after a ramp-rate of 7.5 °C/min. All images are shown at the same scale and correspond to an area of 886 nm × 886 nm. The cumulative distribution for 7.5 °C/min from Figure 2, corresponding to no additional annealing at 220 °C, is also shown for comparison.

exactly how these polycrystalline grains and their boundaries change, in the regions “next to” some residual amorphous plug, in ways that lead to significant changes in effective device resistance. Neither of these effects can be modeled by our code at this time, although the difficulty of implementation is negligible compared to the uncertainty concerning the physics governing these grain boundaries. Further experimental work, which could readily be performed with TEM membranes, is highly warranted.

What is not of much interest, from a device perspective, is additional study into the initial grain distribution produced during a temperature ramp. This includes the changes in first crystallization for both thinner and thicker films, due to the increased role of heterogeneous nucleation in thinner films and the change in local stress induced by the first stages of crystallization in thicker films. These effects are physically intriguing and are readily amenable to study but are not particularly relevant to the operation of PCM devices. Instead, in PCM devices, recrystallization occurs over small volumes in the presence of large temperature gradients and pre-existing crystalline-amorphous boundaries.

The present study has been extremely useful as a rigorous cross-check between experiment and simulation, and as an indicator that the ramp-rate of an anneal is as important as (if not more important than) the anneal temperature and duration. However, any PCM device integrated in a CMOS (Complementary Metal-Oxide Semiconductor) fab will likely experience long anneals at temperatures close to 400 °C, at which point the PCM material will have crystallized into the more stable hexagonal crystalline form.

This raises the question of whether the simulation code ought to be modified to handle the hexagonal crystalline form and the conversion between fcc and hexagonal. Fortunately, while the hexagonal crystalline phase is indeed more stable than the fcc,29,37,54 the fcc version is the one responsible for the active switching observed in devices.55 In fact, even amorphous material in contact with the hexagonal phase has been observed to recrystallize directly into the fcc crystalline phase,56 implying that only the fcc crystalline phase needs to be simulated within PCM devices.

One consideration for future work is modeling the observed increase in crystallization temperature and decrease in the grain size with nitrogen or oxygen doping.47,57,58 Although experimental papers on doped-GST usually discuss a change in the nucleation behavior, the present work shows that a decrease in just $v_g$ could readily explain both the changes in crystallization temperature and grain size. It is well known that doping tends to reduce crystal growth speed at high temperatures.47 What would be needed to seed an extension of the present study would be careful measurements of the low-temperature growth velocities in doped GST films, similar to the work of Refs. 44 and 45. Changes in crystallization temperature observed upon decreasing the thickness of the film41,59 are more problematic to explain, since most of the nucleation observed in our simulation already occurs near an interface. Before attempting to match such experiments, it will be critical to be sure that they are not unduly affected by surface oxidation, incomplete area coverage of sputtered material, inadvertent asymmetries in heating environment, or differences in deposition stoichiometry first.

Another complication is the experimental observation that faster ramps tend to lead to sharp increases in crystallization temperature.31,60,61 While the results of Ref. 61 are clouded by the unexplained disparity between measured resistivities during different ramp-rates at temperatures far below $T_c$, the literature data summarized there clearly show that $T_c$ has been observed to increase sharply as ramp-rates climb above 100 °C/min. However, our simulator (Figure 6) would predict that $T_c$ should linger below 200 °C until the ramp-rate is increased significantly further.

This difference between experimental observation and our simulation probably arises because the glass transition itself should really depend on the temperature ramp-rate. In contrast, we are currently using a single, rate-independent value for $T_g$ in all of our simulations. In actuality, the glass transition should occur at a higher temperature when the temperature change is rapid. Since this would push out the steep increase in the $v_g$ and $I_{ss}$ curves in Figure 5 for very fast ramp-rates, it is quite conceivable that one could reach higher temperatures before the delayed glass transition and the associated sharp increases in crystal growth velocity and nucleation rate finally set in, triggering rapid crystallization.

Since this delayed-glass-transition effect during heating can only show up during extremely rapid crystallization from the amorphous in the absence of any nearby crystalline material, it is not all that useful to be able to simulate it precisely. However, it does raise the question of how recently melted, undercooled-liquid amorphous material cools through the glass transition, and how it undergoes structural relaxation to the fully amorphous phase over time.44,62 These questions are critical to the understanding of how melted-quenched amorphous material differs from the as-deposited amorphous state,63 how the polycrystalline grains just outside (and those nucleated within) an amorphous plug evolve

during various quench trajectories, and how this relaxation over time of the amorphous phase (located in the plug and at the grain boundaries) relates to the externally observed phe- nomena of resistance drift.

All of these are extremely interesting and highly rele- vant topics for future work. One convenient vehicle for studying many of these topics are TEM membranes similar to those introduced in this work. Local optical heating followed by rapid quenching could provide the thermal environments discussed above, resulting in crystalline- amorphous distributions which could be observed with TEM and then matched to simulation. The difficulty here will be that these temperature distributions will necessarily vary rap- idly as a function of radial position within the focussed laser beam used for heating, complicating the post-analysis prob- lem considerably.

## VI. CONCLUSIONS
We have studied the formation of fcc polycrystalline grains from the as-deposited amorphous state in undoped GST, by combining *ex situ* TEM membrane experiments with numerical simulation. Our ramped-anneal experiments showed that temperature ramp-rate strongly influences the median grain size, which we attributed to the difference between the exponential temperature dependence (activation energies) of crystal growth velocity $v_g$ and nucleation rate $I_{ss}$ below the glass transition temperature $T_g$. By truncating ramped-anneal experiments at various peak temperatures, we convincingly demonstrated that, at a given heating ramp- rate, the temperature range over which these GST grains are established is quite narrow.

Our numerical simulator—which models nuclei forma- tion through classical nucleation theory and then tracks the subsequent time- and temperature-dependent growth of these grains—was able to match these experimental observations of initial grain distributions and crystallization temperature both qualitatively and quantitatively. These simulations allowed us to quantify the lower portions of the TTT map for $Ge_2Sb_2Te_5$.

This work represents a first step towards understanding the crucial relationship between the polycrystalline nature of phase change materials and the intermediate resistance states of PCM devices, with impact on long-term data retention, predictable device operation, and long-term resistance drift. Future experiments and extensions of the simulator to inves- tigate the temperature-dependent interactions between neigh- boring grains, and to study nucleation from within the melt- quenched amorphous state, were discussed.

## ACKNOWLEDGMENTS
The authors would like to thank Charles T. Rettner for help with the ramp-anneals, Rohit Shenoy for helpful discus- sions, Dean Pearson and Mark Jurich for help with the sputter- depositions, and Luisa Bozano and Elizabeth Fedde for their help in coordinating and facilitating P.T.'s and C.N.'s intern- ships at IBM Almaden. B. L. was supported by the National Science Foundation under Award No. DMR 07-06267.

$^{1}$G. W. Burr, B. N. Kurdi, J. C. Scott, C. H. Lam, K. Gopalakrishnan, and R. S. Shenoy, *IBM J. Res. Dev.* **52**, 449 (2008).
$^{2}$S. Raoux, G. W. Burr, M. J. Breitwisch, C. T. Rettner, Y.-C. Chen, R. M. Shelby, M. Salinga, D. Krebs, S.-H. Chen, H.-L. Lung *et al.*, *IBM J. Res. Dev.* **52**, 465 (2008).
$^{3}$G. W. Burr, M. J. Breitwisch, M. Franceschini, D. Garetto, K. Gopalak- rishnan, B. Jackson, B. Kurdi, C. Lam, L. A. Lastras, A. Padilla *et al.*, *J. Vac. Sci. Technol. B* **28**, 223 (2010); e-print arxiv.org/abs/1001.1164.
$^{4}$R. Freitas and W. Wilcke, *IBM J. Res. Dev.* **52**, 439 (2008).
$^{5}$K. Kim, *Tech. Dig. - Int. Electron Devices Meet.*, **2010**, 1.1.
$^{6}$A. Pirovano, A. L. Lacaita, F. Pellizzer, S. A. Kostylev, A. Benvenuti, and R. Bez, *IEEE Trans. Electron Devices* **51**, 714 (2004).
$^{7}$D. Ielmini, A. L. Lacaita, and D. Mantegazza, *IEEE Trans. Electron Devi- ces* **54**, 308 (2007).
$^{8}$M. Boniardi, D. Ielmini, S. Lavizzari, A. L. Lacaita, A. Redaelli, and A. Pirovano, *IEEE Trans. Electron Devices* **57**, 2690 (2010).
$^{9}$S. Braga, A. Cabrini, and G. Torelli, *Appl.Phys. Lett.* **94**, 092112 (2009).
$^{10}$D. Ielmini, M. Boniardi, A. L. Lacaita, A. Redaelli, and A. Pirovano, *Microelectron. Eng.* **86**, 1942 (2009).
$^{11}$S. Lavizzari, D. Ielmini, D. Sharma, and A. L. Lacaita, *IEEE Trans. Elec- tron Devices* **56**, 1078 (2009).
$^{12}$S. D. Savransky and A. Yelon, *Phys. Status Solidi A* **207**, 627 (2010).
$^{13}$J. Im, E. Cho, D. Kim, H. Horii, J. Ihm, and S. Han, *Curr. Appl. Phys.* **11**, e82 (2011).
$^{14}$G. W. Burr, A. Padilla, M. Franceschini, B. Jackson, D. G. Dupouy, C. T. Rettner, K. Gopalakrishnan, R. Shenoy, and J. Karidis, in *ACTEMT: Work- shop on the Application of Communication Theory to Emerging Memory Technologies*, IEEE GlobeCom 2010 (IEEE, 2010).
$^{15}$Z. J. Li, J. Lee, J. P. Reifenberg, M. Asheghi, R. G. D. Jeyasingh, H. S. P. Wong, and K. E. Goodson, *IEEE Electron Devices Lett.* **32**, 961 (2011).
$^{16}$J. Lee, Z. J. Li, J. P. Reifenberg, S. Lee, R. Sinclair, M. Asheghi, and K. E. Goodson, *J. Appl. Phys.* **109**, 084902 (2011).
$^{17}$D. Fugazza, D. Ielmini, S. Lavizzari, and A. Lacaita, in *IEEE International Reliability Physics Symposium* (IEEE, 2010), pp. 743-749.
$^{18}$G. F. Close, U. Frey, M. Breitwisch, H. L. Lung, C. Lam, C. Hagleitner, and E. Eleftheriou, *Tech. Dig. - Int. Electron Devices Meet., 2010*, 29.5.
$^{19}$M. Mitra, Y. Jung, D. S. Gianola, and R. Agarwal, *Appl.Phys. Lett.* **96**, 222111 (2010).
$^{20}$C. Krill and R. Birringer, *Philos. Mag.* **A 77**, 621 (1998).
$^{21}$T. H. Jeong, M. R. Kim, H. Seo, S. J. Kim, and S. Y. Kim, *J. Appl. Phys.* **86**, 774 (1999).
$^{22}$J. A. Kalb, C. Y. Wen, F. Spaepen, H. Dieker, and M. Wuttig, *J. Appl. Phys.* **98**, 054902 (2005).
$^{23}$S. A. Song, W. Zhang, H. S. Jeong, J. G. Kim, and Y. J. Kim, *Ultramicro- scopy* **108**, 1408 (2008).
$^{24}$P. La Fata, F. Torrisi, S. Lombardo, G. Nicotra, R. Puglisi, and E. Rimini, *J. Appl. Phys.* **105**, 083546 (2009).
$^{25}$Y. Choi and Y. K. Lee, *Appl. Phys. Lett.* **96**, 041910 (2010).
$^{26}$S. Lombardo, E. Rimini, M. G. Grimaldi, and S. Privitera, *Microelectron. Eng.* **87**, 294 (2010).
$^{27}$E. Rimini, R. Debastiani, E. Carria, M. G. Grimaldi, G. Nicotra, C. Bon- giorno, and C. Spinella, in *MRS 2009* (MRS, 2009), pp. 149-154.
$^{28}$V. Weidenhof, I. Friedrich, S. Ziegler, and M. Wuttig, *J. Appl. Phys.* **86**, 5879 (1999).
$^{29}$B. J. Kooi, W. M. G. Groot, and J. T. M. De Hosson, *J. Appl. Phys.* **95**, 924 (2004).
$^{30}$G. Ruitenberg, A. K. Petford-Long, and R. C. Doole, *J. Appl. Phys.* **92**, 3116 (2002).
$^{31}$J. Gonzalez-Hernandez, E. F. Prokhorov, Y. V. Vorobiev, E. Morales-San- chez, A. Mendoza-Galvan, S. A. Kostylev, Y. I. Gorobets, V. N. Zakharch- enko, and R. V. Zakharchenko, *J. Vac. Sci. Technol. A* **19**, 1623 (2001).
$^{32}$S. Privitera, C. Bongiorno, E. Rimini, R. Zonca, A. Pirovano, and R. Bez, in *MRS 2003* (MRS, 2003), vol. 803, p. HH1.4.
$^{33}$S. Privitera, S. Lombardo, C. Bongiorno, E. Rimini, and A. Pirovano, *J. Appl. Phys.* **102**, 013516 (2007).
$^{34}$S. Senkader and C. D. Wright, *J. Appl. Phys.* **95**, 504 (2004).
$^{35}$B.-S. Lee, G. W. Burr, R. M. Shelby, S. Raoux, C. T. Rettner, S. N. Bogle, K. Darmawikarta, S. G. Bishop, and J. R. Abelson, *Science* **326**, 980 (2009).
$^{36}$A. Debunne, K. Virwani, A. Padilla, G. W. Burr, A. J. Kellock, V. R. Deline, R, M. Shelby, and B. Jackson, *J. Electrochem. Soc.* **158**, H965 (2011).
$^{37}$B. J. Kooi and J. T. M. De Hosson, *J. Appl. Phys.* **92**, 3584 (2002).
$^{38}$See http://rsbweb.nih.gov/ij/ to download ImageJ.

![](./images/813308072188444674_12.jpg)

$^{39}$See http://code.google.com/p/psa-macro/ to download the PSA macro.

$^{40}$I. Friedrich, V. Weidenhof, W. Njoroge, P. Franz, and M. Wuttig, J. Appl. Phys. 87, 4130 (2000).

$^{41}$S. Raoux, J. L. Jordan-Sweet, and A. J. Kellock, J. Appl. Phys. 103, 114310 (2008).

$^{42}$M. Salinga, "Phase change materials for non-volatile electronic memo- ries," Ph.D. dissertation (RWTH Aachen, 2008).

$^{43}$J. W. Christian, Theory of Transformations in Metals and Alloys, 2nd ed. (Pergamon, New York, 1975).

$^{44}$M. Salinga, J. Kalb, M. Klein, T. Sontheimer, F. Spaepen, and M. Wuttig, in EPCOS 2007 (2007). Available at www.epcos.org.

$^{45}$J. Kalb, F. Spaepen, and M. Wuttig, Appl. Phys. Lett. 84, 5240 (2004).

$^{46}$G. W. Burr, M. Salinga, S. Raoux, R. M. Shelby, and M. Wuttig, in Mate- rials Research Society Spring Meeting (MRS, 2008).

$^{47}$R. M. Shelby and S. Raoux, J. Appl. Phys. 105, 104902 (2009).

$^{48}$J. A. Kalb, F. Spaepen, and M. Wuttig, J. Appl. Phys. 98, 054910 (2005).

$^{49}$Y. C. Chen, C. T. Rettner, S. Raoux, G. W. Burr, S. H. Chen, R. M. Shelby, M. Salinga, W. P. Risk, T. D. Happ, G. M. McClelland et al., Tech. Dig. - Int. Electron Devices Meet., 2006, S30P3.

$^{50}$J. Douglas, Jr., and J. E. Gunn, Numer. Math. 6, 428 (1964).

$^{51}$T.-Y. Wang and C. C.-P. Chen, IEEE Trans. Comput.-Aided Des. 21, 1434 (2002).

$^{52}$D. H. Kim, F. Merget, M. Laurenzis, P. H. Bolivar, and H. Kurz, J. Appl. Phys. 97, 083538 (2005).

$^{53}$H. K. Lyeo, D. G. Cahill, B. S. Lee, J. R. Abelson, M. H. Kwon, K. B. Kim, S. G. Bishop, and B. K. Cheong, Appl. Phys. Lett. 89, 151904 (2006).

$^{54}$E. T. Kim, J. Y. Lee, and Y. T. Kim, Phys. Status Solidi A 206, 2542 (2009).

$^{55}$J.-B. Park, G.-S. Park, H.-S. Baik, J.-H. Lee, H. Jeong, and K. Kim, J. Electrochem. Soc. 154, H139 (2007).

$^{56}$R. De Bastiani, E. Carria, S. Gibilisco, A. Mio, C. Bongiorno, F. Piccinelli, M. Bettinelli, A. R. Pennisi, M. G. Grimaldi, and E. Rimini, J. Appl. Phys. 107, 113521 (2010).

$^{57}$H. Seo, T. H. Jeong, J. W. Park, C. Yeon, S. J. Kim, and S. Y. Kim, Jpn. J. Appl. Phys. Part 1 39, 745 (2000).

$^{58}$S. Privitera, E. Rimini, and R. Zonca, Appl. Phys. Lett. 85, 3044 (2004).

$^{59}$X. Q. Wei, L. P. Shi, T. C. Chong, R. Zhao, and H. K. Lee, Jpn. J. Appl. Phys. Part 1 46, 2211 (2007).

$^{60}$N. Kato, I. Konomi, Y. Seno, and T. Motohiro, Appl. Surf. Sci. 244, 281 (2005).

$^{61}$Y. Choi, M. Jung, and Y. K. Lee, Electrochem. Solid-State Lett. 12, F17 (2009).

$^{62}$J. A. Kalb, M. Wuttig, and F. Spaepen, J. Mater. Res. 22, 748 (2007).

$^{63}$J. S. Wei and F. X. Gan, Thin Solid Films 441, 292 (2003).

![](./images/813308072188444674_13.jpg)