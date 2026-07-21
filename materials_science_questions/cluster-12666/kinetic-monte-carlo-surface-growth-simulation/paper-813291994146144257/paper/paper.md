PHYSICAL REVIEW B 86, 085402 (2012)

Origin of the bimodal island size distribution in ultrathin films of para-hexaphenyl on mica

L. Tumbek, $^{1}$ C. Gleichweit, $^{1}$ K. Zojer, $^{2}$ and A. Winkler $^{1, *}$

$^{1}$ Institute of Solid State Physics, Graz University of Technology, Petersgasse 16, A-8010 Graz, Austria
$^{2}$ Institute of Theoretical Physics, Graz University of Technology, Petersgasse 16, A-8010 Graz, Austria

(Received 20 February 2012; revised manuscript received 11 May 2012; published 1 August 2012)

Ultrathin films of para-hexaphenyl (6P) were prepared on freshly cleaved and sputter-amorphized mica(001) by physical vapor deposition. Ex situ atomic force microscopy (AFM) revealed a bimodal island size distribution for the films on both surfaces. On freshly cleaved mica long needlelike islands exist, which are surrounded by small crystallites. On the sputter-amorphized substrates, large dendritic islands exist which are again surrounded by small, compact islands. We could prove by thermal desorption spectroscopy that the small islands are the result of adsorbate-induced subsequent nucleation, when the films were exposed to air. In case of the freshly cleaved mica, islands grow on a wetting layer in vacuum. This layer dewets and forms the small islands upon venting, due to the adsorption of water. In the case of the amorphous mica substrate an equilibrium exists between the islands and a two-dimensional gas phase in the sub-monolayer regime. Again, the latter phase nucleates after venting. In a particular coverage range, islands due to nucleation during deposition and subsequent nucleation coexist on the substrate, leading to the bimodal island size distribution. Kinetic Monte Carlo (KMC) simulations were performed to model the nucleation process after venting on the sputter-modified mica substrate. The density of the subsequently nucleated islands just depends on the initial coverage and the critical island size. A critical cluster size of $i=7$ molecules was determined for $6P$ on amorphized mica, by comparing the KMC results with the AFM images in case of adsorbate-induced nucleation. Furthermore, the experimentally obtained island size distributions could be well reproduced by KMC simulations.

DOI: 10.1103/PhysRevB.86.085402
PACS number(s): 68.55.A–, 81.15.Aa, 68.37.Ps, 68.43.Vx

## I. INTRODUCTION

Understanding the fundamental processes in the formation of organic thin films is of utmost importance for the application in organic electronic devices. In particular, the morphology of the organic films plays a crucial role for their electrical and electro-optical properties. $^{1,2}$ Frequently used organic molecules, like oligoacenes or oligophenylenes, are of rodlike shape; such molecules can be arranged in thin films either predominantly parallel or normal to the substrate surface. For the application as active layers in organic field effect transistors the films should be composed of standing molecules, because the charge carrier transport will mainly occur along the direction of the $\pi-\pi$ bonds. $^{3}$ On the other hand, the fluorescence emission of rodlike organic molecules will be most intense normal to the long molecular axis, requiring molecule orientation parallel to the substrate for organic light-emitting diodes. $^{4}$ It has been shown that the preferred orientation of rodlike organic molecules in the film can be significantly influenced by a change of the chemical and/or geometrical composition of the substrate. Typically, on contaminated and/or rough surfaces films composed of upright-oriented molecules will be dominant, whereas on clean, reactive surfaces the molecules in the film will be forced to lie parallel to the surface, even for thicker films. $^{5}$ In particular, the molecule orientation in the first layer will usually determine the molecule orientation in the whole film. $^{6}$

A frequently investigated model system for organic thin film growth is para-hexaphenyl $(6P)$ on mica(001). The advantage of mica as a substrate is the easy production of very flat and clean single-crystal surfaces by simply cleaving a thin sheet of mica and installing it immediately into the evaporation chamber. The rodlike $6P$ molecules form extremely long needles on a freshly cleaved mica surface, which are composed of lying molecules. These needles could be used as optical nanofibers. $^{7}$ On the other hand, it has been shown that sputter amorphization of a mica surface, or the contamination of the surface with a sub-monolayer of carbon, leads to a totally different film formation, where dendritic islands appear which are composed of standing molecules. $^{8}$

A special feature of very thin $6P$ films on mica, in the case of needle formation on the freshly cleaved mica, $^{8-11}$ as well as of dendritic island formation on sputter-amorphized mica, $^{12}$ is the frequent appearance of an extremely bimodal island size distribution. A similar bimodal distribution was also observed for $6P$ on titanium oxide. $^{13}$ Between the large islands many small islands (clusters) are distributed. Moreover, around the large islands a zone exists which is denuded of small clusters. It has been suggested that for the needle/cluster bimodal distribution on the freshly cleaved mica the needle growth is governed by the agglomeration of pre-existing clusters. An elastic strain-induced process has been proposed as the driving force. $^{9}$ Clusters of the size of up to 140 000 molecules were assumed to have sufficient mobility to agglomerate into the needlelike islands. This assumption was supported by the observation that the needles were indeed not uniform, but actually composed of individual clusters. $^{9,14}$

In this work we reexamine the initial $6P$ growth of needlelike islands on freshly cleaved mica and compare the data with the bimodal island size distribution, as obtained

Published by the American Physical Society under the terms of the Creative Commons Attribution 3.0 License. Further distribution of this work must maintain attribution to the author(s) and the published article's title, journal citation, and DOI.

1098-0121/2012/86(8)/085402(11)
085402-1
Published by the American Physical Society

on the sputter-modified mica surface, using *ex situ* atomic force microscopy (AFM). In addition to that, we apply thermal desorption spectroscopy (TDS), which allows us to identify a possible wetting layer and its influence on the film formation. It turns out, that the small $6P$ islands (clusters) on both, the freshly cleaved and the sputter-modified mica surface, are the result of subsequent nucleation, when the $6P$-covered mica surface is exposed to air for *ex situ* AFM investigations. Thus, the frequently observed bimodal island size distribution is the combined result of nucleation and growth during deposition and subsequent nucleation caused most probably by water adsorption after venting the vacuum chamber, which we call adsorbate-induced nucleation. For the modeling of the latter type of nucleation process we have carried out kinetic Monte Carlo (KMC) simulations.

## II. EXPERIMENTAL DETAILS

Ultrathin films of $6P$ were deposited on muscovite mica(001) samples in an ultrahigh vacuum (UHV) chamber by physical vapor deposition (PVD) from a glass Knudsen cell. The mica(001) samples $(10 \times 10 \times {\sim 0.01\ \mathrm{mm}}^{3})$ were prepared by cleaving a mica sheet with the help of adhesive tape in air and immediately installed into the UHV chamber. The base pressure of the vacuum chamber after bake-out was $1 \times 10^{-10}$ mbar, but typically the experiments were performed without baking the system, resulting in a working pressure of about $2 \times 10^{-8}$ mbar. We have experimentally verified that the film growth was, within experimental error, the same in both vacuum regimes. The mica sheets were attached to a steel plate via tantalum wires, which was heated resistively. The temperature was controlled by a Ni-NiCr thermocouple spot welded to the back of the steel plate. This allowed a controlled heating of the steel plate and hence of the mica sample for TDS, typically with heating rates of 1 K/s. With additional $\mathrm{LN}_{2}$ cooling, the temperature of the steel plate could be varied between 100 K and 1000 K. Unfortunately, a considerable temperature difference existed between the front mica surface and the heating plate, due to the low heat conductivity of mica normal to the (001) plane.¹⁵ However, a calibration of the temperature can be performed by comparing the multilayer peak maximum of desorbing $6P$ from mica with that from the tantalum wires, as described in more detail elsewhere.⁸ For TDS a multiplexed quadrupole mass spectrometer (QMS) (0–500 amu) was used. In addition to the mass of the $6P$ molecules ($m=458.6$ amu), typically the mass $m=61$ amu was measured, because this showed the largest signal of the cracking pattern in the QMS. Furthermore, it was verified that no cracking of the $6P$ molecules occurred at the surface.

For the quantitative determination of the $6P$ film thickness a quartz microbalance was used which was positioned next to the sample. The reliability of this device was checked in two ways: (a) by comparing with corresponding AFM images of sub-monolayer films of standing molecules and (b) by TDS, as outlined in more detail elsewhere.⁸ For the modification of the mica surface to obtain exclusively layers with standing $6P$ molecules, the surface was sputtered for about 10 min by $\mathrm{Ar}^{+}$ ions with 500 eV at an argon partial pressure of $5 \times 10^{-5}$ mbar. Auger electron spectroscopy (AES) and x-ray photoelectron spectroscopy (XPS) were applied to check the chemical composition of the mica substrate. After the *in situ* preparation and characterization of the $6P$ films on mica, the samples were investigated *ex situ* by AFM in the tapping mode (Nanosurf, EasyScan2).

## III. KINETIC MONTE CARLO SIMULATION

Kinetic Monte Carlo simulations are frequently applied to study various aspects of epitaxial film growth. In nearly all known studies the particles, which are assumed to be pointlike, can occupy specific lattice sites and move between these sites with specific hopping rates. Although in our case the particles are rodlike entities, we chose to apply the well-established computational techniques of pointlike particles. We justify our choice of pointlike entities for the KMC simulations as follows: First, the elongated molecules are oriented upright in the condensed islands and therefore occupy single adsorption sites in the $6P$(001) plane. Second, the distance between the islands, which is on the order of micrometers, is much larger than the size of the (anisotropic) molecules. Third, the isotropic island distribution (on the sputter-modified substrate) and the irregular dendritic shape of the islands show that the diffusion behavior of the anisotropic, lying molecules can be sufficiently well approximated by the diffusion of pointlike particles. We are only aware of one KMC study where dimer particles were allowed to occupy lattice sites in lying and standing configurations.¹⁶ However, the consideration of all possible conformations in the nucleation process of extended oligomers and the (unknown) energy barriers involved would make KMC simulations exceedingly time consuming and most probably of little physical significance.

Our simulations are based on the approach of Bales and Chrzan,¹⁷ which we extended by considering also reversible aggregation by including the critical island size $i$ as a parameter of the simulations, in the spirit of Li and Evans.¹⁸ The simulations were performed on a square lattice, where each lattice site can contain one molecule.¹⁹ Because we investigate the system in the sub-monolayer regime, we do not regard molecules hopping into a second layer. Monomers can diffuse at a rate $h_{1}=v\mathrm{exp}(-\frac{Q}{kT})$, where $Q$ is the energy barrier for surface diffusion, $\nu$ is the hopping frequency, $k$ the Boltzmann constant, and $T$ the substrate temperature. This rate also applies for particles having neighbors in the nearest-neighbor cells, as long as the size of the island does not exceed the critical nucleus size $i$. As soon as an island reaches this size, aggregation is irreversible, meaning that the particles cannot detach anymore from the island, but may diffuse along the edge. In the classical solid-on-solid model the edge hopping rate is described by $h_{n}=v\mathrm{exp}(-\frac{Q+nE}{kT})$, where $n$ is the number of in-plane nearest neighbors ($n=1$–4) and $E$ is the nearest-neighbor binding energy. In our simulations we do not consider the binding of the molecules to the substrate when they diffuse along the island rim. This is justified because the bonding of the standing molecules to the mica substrate via one H atom is negligible, compared to the bonding between the many C atoms between parallel arranged $6P$ molecules. It is, of course, not known how exactly diffusion along the island rim proceeds, but for the final stability of the incorporated molecules only the bonds between the molecules will be of

relevance. Thus, we describe the hopping rate along the rim of the islands by $h_n = v\exp(-\frac{nE}{kT})$. Furthermore, a flux $F$ of impinging particles can be applied which corresponds to adsorption. We do not allow for desorption.

When referring to KMC, the so-called BKL algorithm of Bortz, Kalos, and Lebowitz, $^{20}$ originally proposed for simulating the Ising spin system, is commonly applied. Their way of keeping track of the possible event types that exist in a system (the so-called $n$-fold way) can be applied in our simple model. Namely, there are only a small number of different classes of sites a particle can belong to, depending on the number of neighbor particles. Each particle belonging to the class $j$ hops at a rate $\Gamma_j$. By choosing a random number, first an event class is selected and then one event of that class is executed, meaning that the particle is moved. A time-saving algorithm for updating the event list is essential. In short, this is done by recalculating the events of the neighboring particles only, using an inverse list that keeps track of where to find the events of a specific particle in the event lists. $^{21}$ The time is then incremented by a stochastic variable $\Delta t = -\frac{\ln(r)}{\Gamma_{\text{tot}}}$, where $r \in (0,1)$ is a random number, $\Gamma_{\text{tot}} = \sum_j n_j \Gamma_j$ is the total rate, and $n_j$ is the number of events of class $j$.

Our partially reversible approach leads to the well-known problem of stiffness (Ref. 22 and references therein), which in our case refers to the separation of time scales between monomer diffusion processes and edge hopping. Most of the computational time is used for calculating the diffusion processes of particles that may be far away from any nucleation site. The monomer density in our case can be quite high, while still only very few islands form. This is because the local nucleation probability scales with $dN_{\text{isl}}/dt \sim N_1^{i+1}$, $^{23}$ where $N_{\text{isl}}$ denotes the number of islands and $N_1$ is the monomer density.

Although our KMC formalism is constructed to simulate nucleation processes during the impingement of monomers, in this work we mainly apply the formalism to simulate the adsorbate-induced subsequent nucleation process. In this case we assume that initially a specific amount of immobile monomers exists on the surface (in the sub-monolayer coverage range), which are randomly distributed. With the start of the KMC simulation the monomers are allowed to become mobile with a specific diffusion probability and the number of monomers and islands is computed as a function of time and critical island size, until all monomers are incorporated in the islands. We could show that in this case the actual values of $E$ and $Q$ just influence the shape of the formed islands and only effect the simulation time. It turns out that only the critical island size and the monomer density determine the final island density.

## IV. RESULTS AND DISCUSSION

In Fig. 1 typical AFM images are shown for $6P$ films grown under appropriate growth conditions on freshly cleaved mica(001) [Fig. 1(a)] and on sputter-modified mica [Fig. 1(b)]. Figures 1(c) and 1(d) show selected cross sections as indicated in Figs. 1(a) and 1(b). In both cases a clear bimodal island size distribution can be observed. However, this film morphology can only be seen in a special coverage range, when deposited at a particular surface temperature. For the freshly cleaved mica surface this phenomenon was investigated in detail by Kankate et al., $^{10}$ but it was also observed by others. $^{8,9,11}$ Generally, at low coverage only small clusters exist; in a medium coverage range clusters and needles coexist, whereas at higher coverage, when the needle density is already quite high, the density of the small clusters vanishes. With respect to the substrate temperature, the needle length, width, and height increase with temperature. Due to the overlapping of the denuded zones with increasing number density of the long needles, the total number density of the small clusters decreases with increasing coverage.

While the needlelike island formation on the freshly cleaved (anisotropic) mica surface could be rationalized by a strain-induced agglomeration of the small crystallites, where the wetting layer should play an important role, $^{9}$ this scenario cannot explain the quite similar bimodal island size distribution on the sputter-modified mica surface [Fig. 1(b)]. In this case, no wetting layer exists and the irregular, dendritic shape of the large and small islands demonstrates that the sputtered mica surface is isotropic. This is also supported by the lack of a regular LEED pattern in case of the sputtered surface. $^{8}$

### A. $6P$ on freshly cleaved mica

Before we focus on the $6P$ layer growth on the sputter-modified surface we present some illustrative experimental results for the initial growth of $6P$ on the freshly cleaved mica. As outlined previously, $^{24}$ TDS is a powerful method to get insight into the energetics of organic thin films. In particular, one can distinguish between molecules in a strongly bound wetting layer and the more weakly bound molecules in the three-dimensional (3D) islands. In Fig. 2(a) (curve a) a $6P$ desorption spectrum from the freshly cleaved mica surface is shown, obtained after deposition of an amount equivalent to 10-Hz frequency change at the quartz microbalance. The high-temperature peak at about 535 K can be attributed to the wetting layer, whereas the large peak at 490 K corresponds to desorption from the needlelike islands. $^{8}$ At a lower deposited amount, equivalent to a quartz frequency change of 2 Hz, only the wetting layer is observed [Fig. 2(a), curve b]. We have calibrated our experimental setup for $6P$ deposition with AFM, where we could attribute a quartz frequency change of 16 Hz to a saturated monolayer of standing molecules on the sputter-modified mica surface. Assuming that the molecule packing in this layer is close to that in the $6P(001)$ crystal plane, 1 ML of standing molecules equals $4.4 \times 10^{14}$ $6P$ molecules/cm$^2$, equivalent to a mean height of 2.6 nm. Correspondingly, the coverage of a densely packed layer of flat-lying molecules (wetting layer) corresponds to $5.8 \times 10^{13}$ $6P$ molecules/cm$^2$, or a mean height of 0.35 nm. This fits quite well to the 2 Hz needed to saturate the wetting layer (0.32 nm mean thickness) [Fig. 2(a), curve b].

Interestingly, the ex situ AFM image of the 2-Hz film did not show a uniform, unstructured film, as one would expect for a wetting layer, but showed instead many small, slightly elongated islands, with a mean diameter of about 50 nm and a mean height of about 5 nm [Fig. 2(b)]. The size of these islands is similar to that as frequently observed for the small clusters in the bimodal films obtained at higher total coverage. $^{9-11}$ From


![](./images/813291994146144257_1.jpg)

FIG. 1. (Color online) (a) AFM image $(4 \times 4\ \mu\text{m})$ for $6P$ on a freshly cleaved mica(001) surface. Deposition temperature, 400 K; deposition rate, 0.06 ML/min; deposited amount, 0.62 ML (standing monolayer equivalents). (b) AFM image $(8 \times 8\ \mu\text{m})$ for $6P$ on a sputtered mica(001) surface. Deposition temperature, 400 K; deposition rate, 0.07 ML/min; deposited amount, 0.18 ML. (c) Cross section along the line as indicated in (a), demonstrating different heights of the needles and clusters. (d) Cross section along the line as indicated in (b), demonstrating the same heights for the large and small islands, consisting of one layer of standing molecules.

the height and height distribution we can reason that in this case the islands are again composed of flat-lying molecules. The evaluation of Fig. 2(b) with respect to the total coverage by integrating over all islands gives a mean height of $0.4 \pm 0.1$ nm, in good agreement with the expected saturated wetting layer. (Actually, the somewhat too high value for the mean height can be rationalized, because no tip deconvolution for the AFM image was made). The answer to this puzzling result was found, when after the AFM measurement the sample was again installed into the vacuum chamber and a TDS was

![](./images/813291994146144257_2.jpg)

FIG. 2. (Color online) (a) Thermal desorption spectra of $6P$ (mass 61 amu) on freshly cleaved mica(001), deposited at room temperature. Curve a: deposited amount, 10 Hz (1.6 nm mean thickness); curve b: deposited amount, 2 Hz (0.32 nm mean thickness); curve c: deposited amount, 2 Hz, but afterwards exposed to air and evacuated again before desorption. (b) AFM image $(1 \times 1\ \mu\text{m})$ of $6P$ on freshly cleaved mica. Deposition temperature, 400 K; deposition rate, 0.05 nm/min; deposited amount, 2 Hz; equivalent to 0.32 nm mean thickness.

![](./images/813291994146144257_3.jpg)

FIG. 3. Multiplexed thermal desorption spectra of water ($m =$ 18 amu) after the deposition of 2-Hz equivalents of $6P$ on the freshly cleaved mica, prior to venting the vacuum chamber (a) and after venting and reevacuation (b).

performed after a proper vacuum was achieved [Fig. 2(a), curve c]. The desorption spectrum is now significantly changed in comparison to curve b. There is nearly no material desorbing in the temperature regime of the wetting layer, but a considerable amount desorbs in a temperature range which is characteristic for desorption from 3D islands. In addition, quite some $6P$ desorbs already at low temperature between 350 K and 430 K. However, the total amount of desorbing $6P$ molecules before and after venting the vacuum system is nearly the same. From this result we have to draw the conclusion that the energetics, and hence the morphology of the wetting layer, have changed dramatically upon venting the vacuum system. The reason for this behavior is most probably the adsorption of water. Indeed, multiplexed mass spectrometry clearly shows increased water desorption in case of the reinstalled sample, compared to that prior to venting, as shown in Fig. 3, but no significant desorption of oxygen was observed. Thus, we have to assume that adsorbed water weakens the bonding between the flat-lying $6P$ molecules in the wetting layer and the mica substrate, which increases the mobility of the molecules and allows the nucleation of islands by dewetting. Consequently, at higher coverage, where already needlelike islands have formed above the wetting layer in vacuum, again after venting the remaining molecules in the wetting layer will postnucleate and thus lead to the bimodal island size distribution. The molecules which exist in the vicinity of the needles will be predominantly incorporated in the needles upon venting, thus leading to the denuded zone for the small clusters.

### B. $6P$ on sputter-modified mica

Now we turn to the $6P$ layer growth on the sputter-modified mica surface in the sub-monolayer coverage regime. As shown in Fig. 1(b) and in our previous work, $^{12}$ also in this case a bimodal island size distribution can be observed in a certain coverage range, where both the large and small islands are composed of standing molecules, as verified by AFM [Fig. 1(d)]. The large islands exhibit a dendritic shape,

![](./images/813291994146144257_4.jpg)

FIG. 4. (Color online) Large-scale AFM images ($32 \times 32\ \mu$m) for $6P$ on sputter-modified mica(001) surfaces. Deposition temperature, 400 K; deposition rate, 0.08 ML/min; deposited amount: (a) 0.036 ML, (b) 0.04 ML, (c) 0.077 ML, (d) 0.147 ML. The small islands are hardly visible in this representation.

whereas the small islands are more compact. In Figs. 4(a)-4(d) and Figs. 5(a)-5(d) we present large-scale ($32 \times 32\ \mu$m) and smaller-scale ($8 \times 8\ \mu$m, $2 \times 2\ \mu$m) AFM images of such films, respectively, for different total coverage in the sub-monolayer regime, in order to figure out the coverage-dependent development of the large and small islands. The

![](./images/813291994146144257_5.jpg)

FIG. 5. (Color online) Small-scale AFM images for $6P$ on sputter-modified mica(001) surfaces. Deposition temperature, 400 K; deposition rate, 0.08 ML/min; deposited amount: (a) 0.014 ML, (b) 0.03 ML, (c) 0.036 ML, (d) 0.04 ML.

![](./images/813291994146144257_6.jpg)

FIG. 6. (Color online) AFM images $(8 \times 8\ \mu\text{m})$ for different coverages of 6P grown on sputter-modified mica(001) at 400 K, with a deposition rate of 0.1 ML/min: (a) 0.18 ML, (b) 0.47 ML, (c) 0.94 ML.

large-scale AFM images [Figs. 4(a)–4(d)], in which the small islands are rarely visible, show a continuous increase of the large island density between 0.04 and 0.15 ML, demonstrating that in this coverage range the system is in the nucleation regime. Below 0.04 ML no large islands exist. Between about 0.1 and 0.6 ML the system is in the aggregation regime, where the island density remains nearly constant and only the island size increases [Figs. 6(a) and 6(b)], before coalescence starts above 0.7 ML [Fig. 6(c)].

AFM images with higher resolution $(2 \times 2\ \mu\text{m})$ show the small islands too, which can be observed already before the large islands develop [Figs. 5(a) and 5(b)]. For larger coverage, small and large islands coexist, showing a denuded zone next to the large islands [Figs. 5(d) and 6(a)]. In Fig. 5(c) we can just see the onset of the formation of some large islands. As long as no large islands exist, the density of the small islands increases with the evaporated amount. However, as soon as large islands start to nucleate, the local density of the small islands between the large islands (and outside the denuded zones) decreases again. The number density of the small and large islands as a function of the total coverage is plotted in Fig. 7. This behavior resembles the general coverage dependence of island and monomer densities for diffusion-limited aggregation (DLA).$^{25}$ Thus, we again speculate that the small islands are not formed during deposition, but are rather the result of nucleation of the monomers in the 2D gas phase when the sample is exposed to air. This assumption is again corroborated by TDS performed before and after venting the vacuum chamber. While before venting only a single desorption peak around 480 K is observed for a 2-Hz film (Fig. 8), after venting and reevacuation again a broad desorption peak appears between 350 K and 450 K, which is accompanied by water desorption, in addition to a peak at 500 K. Why the main desorption peak has even moved to somewhat higher temperature upon venting is not clear at the moment.

Finally, we had a closer look at the TDS for very low coverage with respect to a possible strongly bound wetting layer on the sputter-modified surface. However, down to the coverage of 0.01 ML we observed only a single desorption peak around 480 K (Fig. 9). This single peak also shows up for higher sub-monolayer coverage, when already the bimodal island size distribution exists, and also for multilayer coverage. Thus, we have to assume that the desorption process is the same in the whole coverage range, that is, for desorption from the monomer phase and desorption from condensed islands.

![](./images/813291994146144257_7.jpg)

FIG. 7. (Color online) Coverage dependence of the small and large island density for 6P on sputter-modified mica. The lines are to guide the eye.

![](./images/813291994146144257_8.jpg)

FIG. 8. (Color online) Thermal desorption spectra of 6P (mass 61 amu) on sputter-modified mica(001), deposited at room temperature. (a) Deposited amount, 2 Hz (0.32 nm mean thickness); (b) deposited amount, 2 Hz, but afterwards exposed to air and evacuated again before desorption.

![](./images/813291994146144257_9.jpg)

FIG. 9. (Color online) Series of TDS for very small 6P coverage on sputter-modified mica. The deposited amount in monolayers is given in the inset.

Based on these findings we explain the AFM images and TD spectra of sub-monolayer 6P films, deposited on sputtered mica at and below 400 K as follows: At very low coverage (<0.04 ML) the molecule density is too small to form nuclei during deposition. Thus, the molecules exist most likely as flat-lying monomers on the surface, forming a 2D gas phase. When heating the surface during TDS the molecules become more mobile and start to form nuclei of standing molecules. With further temperature increase the standing molecules then desorb from the rim of these islands. Such a desorption mechanism has to be assumed; otherwise the desorption peak would not be at the same temperature as for the multilayer. This is the case for 6P on the freshly cleaved mica, where the flat-lying molecules at low coverage desorb at a higher temperature.

However, if the sputtered mica surface, when covered with <0.04 ML 6P, is exposed to air, the adsorption of water apparently initiates nucleation of the molecules in the 2D gas phase. This could be accomplished either by a lowering of the adsorption and/or diffusion energy, and/or by a decrease of the activation energy for nucleation (smaller critical island size, lower attachment barrier). For higher coverage ($\Theta > 0.04$ ML) the nucleation already starts during deposition under vacuum conditions, leading to a quasiequilibrium between the islands and the 2D gas phase. The latter will again nucleate upon venting, resulting in the bimodal island size distribution. At even higher 6P coverage the distance between the islands becomes so small that most of the monomers are already incorporated in the existing islands either during deposition or at the latest after venting (see Fig. 6). Actually, we have shown in a recent paper that for the nucleation of 6P on mica, the attachment limitation indeed plays an even larger role than the diffusion limitation. $^{26}$

To corroborate the above-made assumptions we compare the number density, morphology, island size, and capture zone distribution of the large 6P islands in the aggregation regime with that of the small 6P islands in the low coverage regime. From Fig. 4(d) ($\Theta = 0.147$ ML) we obtain a density of the large islands, which are clearly dendritic, of $N = 0.12\ \mu\text{m}^{-2}$, equivalent to a mean island separation of $2.9\ \mu\text{m}$. In contrast, the small islands [Fig. 5(b)] are of compact shape and exhibit a maximum island density of $34\ \mu\text{m}^{-2}$ at $\Theta \approx 0.03$ ML, just before nucleation starts, equivalent to a mean island separation of $0.17\ \mu\text{m}$. From the very different features of the small and large islands in terms of density and morphology, one can safely assume that their physical origin is quite different. We have also measured the island size distributions (ISDs) for the large [Fig. 10(a)] and small islands [Fig. 10(b)]. In order to describe the distributions we have fitted the data by a function as used for ISD in case of DLA, proposed by Amar and Family, $^{27}$

$$
f_{p}(u)=C_{p} u^{p} \exp \left(-p a_{p} u^{\frac{1}{a_{p}}}\right), \tag{1}
$$

with $u = s/S$, where $s$ is the island size and $S$ the average island size. $C_{p}$ and $a_{p}$ are $p$-dependent constants. $^{12}$ The value $p$, which stands for the critical island size in DLA, is, however, a mere fitting parameter in the case of adsorbate-induced subsequent nucleation. Unfortunately, the statistics is very poor, due to the limited number of islands and the errors which are made in processing the AFM images. Nevertheless, there seems to be a significant difference between the ISD for the large islands, with $p \approx 2$, and the small islands with $p \approx 1$. The value of $p = 2$ agrees reasonably well with our previously obtained value of $i=3 \pm 1 .^{12}$

Furthermore, we have evaluated the same AFM images [Figs. 4(d) and 5(b)] with respect to their capture zone

![](./images/813291994146144257_10.jpg)

FIG. 10. (Color online) (a) Size distribution of the large 6P islands on sputter-modified mica(001) after deposition of 0.147 ML at 400 K, as measured with ex situ AFM at room temperature. The curveis a fit according to the function as proposed by Amar and Family $^{27}$ for ISD, with $p=2$. A typical island morphology is shown in the inset. (b) Size distribution of the small 6P islands on sputter-modified mica (001) after deposition of 0.03 ML at 400 K, as measured with ex situ AFM at room temperature. The curve is a fit according to the function as proposed by Amar and Family $^{27}$ for ISD, with $p=1$. A typical island morphology is shown in the inset.

![](./images/813291994146144257_11.jpg)
![](./images/813291994146144257_12.jpg)

FIG. 11. (Color online) (a) Voronoi tesselation for the island distribution of Fig. 4(d) (large islands). (b) Capture zone distribution obtained by averaging over four AFM images of the film corresponding to Fig. 4(d). The curves are the scaling functions of Eq. (2) with parameter $i = 0$ through 4. The best fit yields $i \approx 2$.

distributions (CZDs). Pimpinelli and Einstein $^{28}$ proposed an expression for the CZD in the following form:
$$
P_{\beta}(s)=a_{\beta} s^{\beta} \exp \left(-b_{\beta} s^{2}\right), \tag{2}
$$
with $s = v/V$, with $v$ the Voronoi polygon size, $V$ the mean value of $v$, $a_{\beta}$ and $b_{\beta}$ are constants fixed by normalization and unit-mean conditions, respectively, and $\beta = i + 2.^{29,30}$ Again, only for nucleation during deposition the value $i$ stand for the critical island size, but should be seen as a mere parameter for the adsorbate-induced subsequent nucleation. The Voronoi tessellation and the CZD are shown in Figs. 11(a) and 11(b) for the large islands and in Figs. 12(a) and 12(b) for the small islands. The best fit of Eq. (2) to the CZD yields $i \approx 2$ for the large islands and $i \approx 1$ for the small islands, in good agreement with the result obtained from the ISD.

### C. KMC simulations of adsorbate-induced subsequent nucleation
KMC simulations were applied for adsorbate-induced subsequent nucleation, in order to understand this process in more detail and to get information on the critical island size involved.
As outlined above, at the beginning a specific amount of particles is randomly deposited on a square lattice with $1000 \times 1000$ lattice sites, which should be immobile for $t < 0$, but should become mobile for $t \geqslant 0$. Proper surface diffusion energies $Q$ and edge diffusion energies $E$ were assumed, and the same $v$ was taken for surface and edge diffusion. If the edge diffusion energy is set to a high value, rim diffusion is suppressed and the islands grow with a fractal-like shape according to the hit-and-stick mechanism. Figure 13 shows the results for adsorbate-induced subsequent nucleation of a monomer film with initial coverage $\Theta = 0.03$ ML and a critical island size $i = 7$, for vanishing edge hopping ($E \gg$) [Fig. 13(a)] and with edge hopping, by taking $E = Q = 0.05$ eV and $v = 10^{13}$ s$^{-1}$ [Fig. 13(b)]. The used value for $Q$ was inspired by MD calculation. $^{31}$ In the latter case the islands were already quite compact at the end of the simulation, that is, when the last monomers were incorporated in the islands. The important result is, however, that the island density depends only weakly on the shape of the islands (fractal vs compact). A comparison of several simulations with and without island edge hopping

![](./images/813291994146144257_13.jpg)
![](./images/813291994146144257_14.jpg)

FIG. 12. (Color online) (a) Voronoi tesselation for the island distribution of Fig. 5(b) (small islands). (b) Capture zone distribution obtained by averaging over four AFM images of the film corresponding to Fig. 5(b). The curves are the scaling functions of Eq. (2) with parameter $i = 0$ through 4. The best fit yields $i \approx 1$.

![](./images/813291994146144257_15.jpg)

FIG. 13. Comparison of KMC simulations for adsorbate-induced subsequent nucleation without edge hopping (a) and with edge hopping, where $E = Q = 0.05$ eV (b). Lattice sites, $1000 \times 1000$; initial coverage, 0.03 ML.

yields that the island density is only about 10% larger in the case of compact islands. These findings are similar to the results by Bales and Chrzan¹⁷ on the influence of the island morphology on the island density. Similarly, the influence of the island morphology on the scaling of the ISD²⁵ and CZD³² was found to be of minor importance. Since the KMC simulations including edge diffusion need about 50 times more computer time, compared to that for the hit-and-stick scenario, most simulations were done without edge diffusion, if not stated otherwise.

However, the island density depends strongly on the critical island size. In Fig. 14 KMC simulations are presented for $\Theta = 0.03$ ML, taking into account island compacting by edge diffusion, with $i = 6$ [Fig. 14(a)] and $i = 7$ [Fig. 14(b)] and compared with the AFM image ($1 \times 1\ \mu$m) of a $6P$ film with 0.03 ML coverage [Fig. 14(c)]. Assuming a lattice constant of 1 nm for our simulations, which is a reasonable compromise for the distance between $6P$ molecules in the 2D gas phase (Van der Waals dimensions: $0.65 \times 2.6$ nm) and in the condensed phase of the standing molecules [lattice vectors $0.6 \times 0.8$ nm of the herringbone structure in the $6P(001)$ plane], the KMC simulation and the AFM images can be quantitatively compared. According to AFM an island density of $N = 35 \pm 5\ \mu$m⁻² can be determined, the KMC simulations yield an island density of $N = 36 \pm 4\ \mu$m⁻² for $i = 7$, whereas $i = 6$ would yield $N = 114 \pm 10\ \mu$m⁻² and $i = 8$ yields only $N = 12 \pm 3\ \mu$m⁻². This shows that a critical island size of $i = 7$ describes the experimental results best. The

![](./images/813291994146144257_16.jpg)

FIG. 14. (Color online) Comparison of KMC simulations for island densities as a result of adsorbate-induced subsequent nucleation (initial coverage, 0.03 ML; $1000 \times 1000$ lattice sites) with an AFM image of $6P$ on amorphous mica. (a) KMC, critical island size $i = 6$; (b) KMC, critical island size $i = 7$; (c) AFM image ($1 \times 1\ \mu$m); coverage, 0.03 ML.

![](./images/813291994146144257_17.jpg)

FIG. 15. Island density as a function of the critical island size, for different initial coverages (0.02–0.1 ML), obtained by KMC for adsorbate-induced subsequent nucleation. No edge diffusion was considered.

island densities as a function of the critical island size in the range of $i = 3$–8 are compiled in Fig. 15, for initial monomer coverages between 0.02 and 0.1 ML. For these simulations no edge diffusion was considered. In Fig. 16 the same data set is plotted versus the initial monomer coverage, which shows a linear dependence between $\ln N$ and $\ln\Theta$. By using a trial function in the form

$$
N(i,\Theta) = c \cdot \Theta^{\alpha(i)} e^{\beta(i)} \tag{3}
$$

we could successfully fit the obtained island densities in the range of $i = 3$–8 and $\Theta = 0.02$–0.1 ML with the parameters $c = 4 \times 10^4$, $\alpha(i) = 0.436i$ and $\beta(i) = 0.538i$.

In addition, we have also determined the evolution of the island density and the change of the monomer density with time. An example is presented in Fig. 17 for an initial coverage of 0.03 ML and various critical island sizes $i$. For these calculations we have again assumed an attempt frequency $\nu = 10^{13}$ s⁻¹, a diffusion energy $Q = 0.05$ eV and $T = 300$ K. As expected, the time increases for adsorbate-induced subsequent nucleation with increasing $i$, but it is in all cases much faster

![](./images/813291994146144257_18.jpg)

FIG. 16. Logarithm of the island density, $\ln N$, versus the logarithm of the coverage, $\ln\Theta$, for various critical island size ($i=3$-$8$), obtained by KMC for adsorbate-induced subsequent nucleation. No edge diffusion was considered.

than the time elapsed in the experiments between venting the vacuum chamber and the AFM measurements.

Finally, ISDs for simulated island films were determined for various critical island sizes. Two exemplary distributions are shown in Fig. 18(a) for $i=5$ and in Fig. 18(b) for $i=7$. It turns out that the distributions depend only weakly on the critical island size, and can be roughly described according to Eq. (1) with $p=1.5\pm0.5$. Thus, the calculated ISD is close to that as experimentally determined for adsorbate-induced subsequent nucleation, with $p\approx1$. It is clear that the meaning of the fit parameter $p$ in Eq. (1) for adsorbate-induced subsequent nucleation is quite different to that for "normal" nucleation during particle deposition, where $p$ directly represents the critical island size $i$. Actually, we could show for comparison, that our simulations for nucleation *during particle deposition*, by assuming a particular critical island size $i$, indeed lead to ISDs which could be well described by Eq. (1), as depicted in Fig. 18(c). For this simulation we assumed, as in the paper by Li and Evans, $^{33}$ a critical island size $i=3$, a ratio of the edge hopping rate $h_1$ to the deposition rate $F$, $h_1/F=10^6$, and a coverage of 0.1 ML.

![](./images/813291994146144257_19.jpg)

FIG. 17. Time development of the monomer (dashed lines) and island density (solid lines) for adsorbate-induced subsequent nucleation as a function of the critical island size $i$. Initial coverage, 0.03 ML; attempt frequency, $\nu=10^{13}$ s$^{-1}$; diffusion energy, $Q=0.05$ eV.

![](./images/813291994146144257_20.jpg)

FIG. 18. (Color online) Island size distribution for KMC-simulated island films resulting from adsorbate-induced subsequent nucleation, with $i=5$ (a) and $i=7$ (b); initial coverage, 0.03 ML. Fit curves according to the function by Amar and Family, $^{27}$ with fit parameters $p=1$, 2. For comparison an ISD from KMC-simulated nucleation during deposition is shown (c), assuming $i=3$. This demonstrates the very good agreement with the function of Amar and Family with fit parameter $p=3$.

## V. SUMMARY AND CONCLUSIONS

The bimodal ISD, which is frequently observed when a sub-monolayer of $6P$ is deposited on muscovite mica, has been investigated in detail. On the freshly cleaved mica(001) surface the films are composed of needlelike islands, which are surrounded by small crystallites, exhibiting a denuded zone around the needles. Both, the large islands and the small crystallites are composed of lying molecules. On a sputter-

amorphized mica surface the island formation is drastically changed. In this case dendritic islands are formed, which are again surrounded by small islands, also exhibiting a denuded zone. However, the small and large islands are now composed of standing molecules. Nevertheless, we could demonstrate, by combining AFM and TDS, that in both cases the small islands do not exist after deposition in vacuum. They are rather the result of adsorbate-induced nucleation after venting the vacuum system. In the case of the freshly cleaved mica surface a wetting layer dewets, and in the case of the sputtered mica surface a 2D gas phase nucleates after venting. Most probably the adsorption of water on the mica surface is responsible for the subsequent nucleation process. Due to this coadsorption the molecule/substrate bond energy is reduced, leading to decreased barriers for surface diffusion and/or for the attachment of the monomers at the rim of the islands. In addition, also a change of the critical island size, due to the adsorption of water, might be responsible for the subsequent nucleation. Thus, if for a particular coverage already some islands have developed during deposition under vacuum conditions, either above a wetting layer or in quasiequilibrium with a 2D gas phase, a second type of island will appear after venting due to adsorbate-induced subsequent nucleation, leading to the bimodal ISD.

We have applied kinetic Monte Carlo simulations; in particular to simulate the adsorbate-induced subsequent nucleation process, by assuming that an initially immobile monomer phase becomes mobile at the moment of venting. It turns out that the island density, due to subsequent nucleation, is just a function of the critical island size and the initial monomer coverage. A comparison of KMC simulations with AFM images for $6P$ on amorphized mica resulted in a critical island size of $i=7$ molecules. Furthermore, the ISD as determined from AFM images could be well reproduced by the KMC simulations.

## ACKNOWLEDGMENT

This work was financially supported by the Austrian Science Fund (FWF), Project No. 23530.

$^{*}$Corresponding author: a.winkler@tugraz.at

$^{1}$H. Klauk (editor), *Organic Electronics: Materials, Manufacturing and Applications* (Wiley-VHC Verlag, Weinheim, 2006).

$^{2}$C. Wöll (editor), *Physical and Chemical Aspects of Organic Electronics* (Wiley-VHC Verlag, Weinheim, 2009).

$^{3}$D. Braga and G. Horowitz, *Adv. Mater.* **21**, 1473 (2009).

$^{4}$H. Yanagi and S. Okamoto, *Appl. Phys. Lett.* **71**, 2563 (1997).

$^{5}$T. Haber, S. Muellegger, A. Winkler, and R. Resel, *Phys. Rev. B* **74**, 045419 (2006).

$^{6}$R. Resel, *Thin Solid Films* **433**, 1 (2003).

$^{7}$F. Balzer, V. G. Bordo, A. C. Simonsen, and H.-G. Rubahn, *Phys. Rev. B* **67**, 115408 (2003).

$^{8}$P. Frank, G. Hlawacek, O. Lengyel, A. Satka, C. Teichert, R. Resel, and A. Winkler, *Surf. Sci.* **601**, 2152 (2007).

$^{9}$C. Teichert, G. Hlawacek, A. Y. Andreev, H. Sitter, P. Frank, A. Winkler, and N. S. Sariciftci, *App. Phys. A* **82**, 665 (2006).

$^{10}$L. Kankate, F. Balzer, H. Niehus, and H. G. Rubahn, *J. Chem. Phys.* **128**, 084709 (2008).

$^{11}$A. Andreev, C. Teichert, G. Hlawacek, H. Hope, R. Resel, D. M. Smilgies, H. Sitter, and N. S. Sariciftci, *Org. Electron.* **5**, 23 (2004).

$^{12}$T. Potocar, S. Lorbek, D. Nabok, Q. Shen, L. Tumbek, G. Hlawacek, P. Puschnig, C. Ambrosch-Draxl, C. Teichert, and A. Winkler, *Phys. Rev. B* **83**, 075423 (2011).

$^{13}$S. Berkebile, G. Koller, G. Hlawacek, C. Teichert, F. P. Netzer, and M. G. Ramsey, *Surf. Sci. Lett.* **600**, 313 (2006).

$^{14}$H. Plank, R. Resel, H. Sitter, A. Andreev, N. S. Sariciftci, G. Hlawacek, C. Teichert, A. Thierry, and B. Lotz, *Thin Solid Films* **443**, 108 (2003).

$^{15}$A. S. Gray and C. Uher, *J. Mater. Sci.* **12**, 959 (1977).

$^{16}$D. Choudhary, P. Clancy, R. Shetty, and F. Escobedo, *Adv. Funct. Mater.* **16**, 1768 (2006).

$^{17}$G. S. Bales and D. C. Chrzan, *Phys. Rev. B* **50**, 6057 (1994).

$^{18}$M. Li and J. W. Evans, *Surf. Sci.* **546**, 127 (2003).

$^{19}$C. Ratsch and J. A. Venables, *J. Vac. Sci. Technol. A* **21**, S96 (2003).

$^{20}$A. B. Bortz, M. H. Kalos, and J. L. Lebowitz, *J. Comp. Phys.* **17**, 10 (1975).

$^{21}$T. P. Schulze, *Phys. Rev. E* **65**, 036704 (2002).

$^{22}$A. Chatterjee and D. Vlachos, *J. Comput.-Aided Mater. Des.* **14**, 253 (2007).

$^{23}$J. A. Venables and H. Brune, *Phys. Rev. B* **66**, 195404 (2002).

$^{24}$A. Winkler, *Springer Proc. Phys.* **129**, 29 (2009).

$^{25}$J. G. Amar, F. Family, and P.-M. Lam, *Phys. Rev. B* **50**, 8781 (1994).

$^{26}$L. Tumbek and A. Winkler, *Surf. Sci.* **606**, L55 (2012).

$^{27}$J. G. Amar and F. Family, *Phys. Rev. Lett.* **74**, 2066 (1995).

$^{28}$A. Pimpinelli and T. L. Einstein, *Phys. Rev. Lett.* **99**, 226102 (2007).

$^{29}$M. Li, Y. Han, and J. W. Evans, *Phys. Rev. Lett.* **104**, 149601 (2010).

$^{30}$A. Pimpinelli and T. L. Einstein, *Phys. Rev. Lett.* **104**, 149602 (2010).

$^{31}$G. Hlawacek, P. Puschnig, P. Frank, A. Winkler, C. Ambrosch-Draxl, and C. Teichert, *Science* **321**, 108 (2008).

$^{32}$P. A. Mulheran and J. A. Blackman, *Phys. Rev. B* **53**, 10261 (1996).

$^{33}$M. Li and J. W. Evans, *Multiscale Model. Simul.* **3**, 629 (2005).