![](./images/813377556907556864_1.jpg)

Comparison between ZEP and PMMA resists for nanoscale electron beam lithography experimentally and by numerical modeling

Kirill Koshelev, Mohammad Ali Mohammad, Taras Fito, Kenneth L. Westra, Steven K. Dew, and Maria Stepanova

Citation: *Journal of Vacuum Science & Technology B* **29**, 06F306 (2011); doi: 10.1116/1.3640794
View online: http://dx.doi.org/10.1116/1.3640794
View Table of Contents: http://scitation.aip.org/content/avs/journal/jvstb/29/6?ver=pdfcov
Published by the AVS: Science & Technology of Materials, Interfaces, and Processing

---

Articles you may be interested in
[Experimental verification of achieving vertical sidewalls for nanoscale features in electron-beam lithography](http://)
J. Vac. Sci. Technol. B **32**, 06F510 (2014); 10.1116/1.4901171

[Study of multilayer systems in electron beam lithography](http://)
J. Vac. Sci. Technol. B **31**, 06F407 (2013); 10.1116/1.4827813

[Developer-free direct patterning of PMMA/ZEP 520A by low voltage electron beam lithography](http://)
J. Vac. Sci. Technol. B **29**, 06F303 (2011); 10.1116/1.3634017

[Simulation of electron beam lithography of nanostructures](http://)
J. Vac. Sci. Technol. B **28**, C6C48 (2010); 10.1116/1.3497019

[Low voltage electron beam lithography in PMMA](http://)
J. Vac. Sci. Technol. B **17**, 1366 (1999); 10.1116/1.590762

---

![](./images/813377556907556864_2.jpg)

# Comparison between ZEP and PMMA resists for nanoscale electron beam lithography experimentally and by numerical modeling

Kirill Koshelev
Department of Electrical and Computer Engineering, University of Alberta, Edmonton, Alberta T6G 2V4, Canada and National Institute for Nanotechnology NRC, 11421 Saskatchewan Drive, Edmonton, Alberta T6G2M9, Canada

Mohammad Ali Mohammad
Department of Electrical and Computer Engineering, University of Alberta, Edmonton, Alberta T6G 2V4, Canada

Taras Fito
Department of Electrical and Computer Engineering, University of Alberta, Edmonton, Alberta T6G 2V4, Canada and National Institute for Nanotechnology NRC, 11421 Saskatchewan Drive, Edmonton, Alberta T6G 2M9, Canada

Kenneth L. Westra and Steven K. Dew
Department of Electrical and Computer Engineering, University of Alberta, Edmonton, Alberta T6G 2V4, Canada

Maria Stepanova⁽ᵃ⁾
Department of Electrical and Computer Engineering, University of Alberta, Edmonton, Alberta T6G 2V4, Canada and National Institute for Nanotechnology NRC, 11421 Saskatchewan Drive, Edmonton, Alberta T6G 2M9, Canada

(Received 13 July 2011; accepted 28 August 2011; published 22 September 2011)

A modern alternative to the positive-tone PMMA resist is the ZEP 520A (Nippon Zeon) brand co-polymer resist, which offers a higher sensitivity and etch durability for electron beam lithography. However, the molecular mechanisms are not entirely understood, and the relative performance of two resists for various process conditions of nanofabrication is not readily predictable. The authors report a thorough experimental comparison of the performance of PMMA 950k and ZEP 520A resists in MIBK:IPA, ZED, and IPA:water developers. Interestingly, ZEP resist performance was found to depend significantly on the developer. ZED developer increases the sensitivity, whereas IPA:water optimizes line edge roughness and conceivably the resolution at the expense of sensitivity. The authors also describe two alternative numerical models, one assuming an enhancement of the main chain scission in ZEP as a result of electronic excitations in side groups, and another without such enhancement. In the second case, the differences in ZEP and PMMA resists performance are attributed to their different interaction with the developers. Using both approaches, the authors parameterize the respective models of ZEP development by fitting numerical results to the experimental resist morphologies, and analyze the outcomes. © 2011 American Vacuum Society. [DOI: 10.1116/1.3640794]

## I. INTRODUCTION

One of the most efficient and established techniques for creating deep submicron patterns is electron beam lithography (EBL). A focused beam of electrons interacting with a layer of radiation sensitive material (resist) induces chemical changes, such as chain scissioning in positive tone polymer resists. The fragmented resist material from exposed regions is then removed by dissolution in a suitable solvent (developer). Polymethylmethacrylate (PMMA) is well-known as the industry standard, high-resolution, positive-tone resist for EBL. The EBL exposure and processing mechanisms of PMMA are well understood and a large number of usage options have been developed. Processing techniques such as for example ultrasonic agitation or cold development have enabled patterning up to 10 nm resolution employing PMMA.¹⁻³ However, PMMA has a relatively low sensitivity and poor etch resistance. To meet the growing needs in direct-write fabrication of large arrays of smaller, denser nanostructures, solutions employing other resists are addressed increasingly often.⁴⁻⁷

A modern alternative to PMMA is another positive-tone resist, ZEP (a 1:1 copolymer of $\alpha$-chloromethacrylate and $\alpha$-methylstyrene), which has been developed as a highly sensitive, stable, and durable positive-tone resist.⁸ In comparison to PMMA, in ZEP the side groups are substituted with a chlorine atom and a phenyl group (Fig. 1).

Compared with PMMA, ZEP exhibits a 2–10 times greater sensitivity depending on the exposure and development conditions.⁴,⁸⁻¹¹ The greatest sensitivity improvements have been reported with lower voltages and xylene based developers;⁸⁻¹¹ moderate sensitivity improvements were reached using amyl acetate,¹¹ and the least sensitivity improvements have been observed using hexyl acetate.⁴,⁹ At present, n-amyl acetate (ZED) is considered as the standard developer for ZEP resists.¹² Further qualities of ZEP include

⁽ᵃ⁾Electronic mail: maria.stepanova@nrc-cnrc.gc.ca


high stability – no resolution loss has been reported when developing exposed ZEP after a period of 6 months.⁸ In addition, the plasma etch durability of ZEP is known to be 2–4 times higher compared to PMMA for $C_2F_6$ and $SF_6$ gases.⁸,¹³ Despite these advantages of ZEP over PMMA, it has been reported that ZEP has comparable or inferior resolution and line edge roughness (LER) compared to PMMA.⁸,¹⁰ To compensate for this shortcoming, resolution enhancement techniques developed with PMMA such as cold development have been applied to ZEP with a favorable impact on resolution and LER improvements at the cost of reduced sensitivity.⁴,¹⁴

Whereas many EBL exposure and development optimization studies have been conducted for PMMA, processing strategies for ZEP are much less abundant; as well, the understanding of the molecular mechanisms determining ZEP performance is very far from complete. The observed sensitivity increase of ZEP in comparison to PMMA has been attributed to the presence of the chlorine group, whereas the presence of the phenyl group is expected to enhance the etch durability.⁸ A more detailed understanding of ZEP resist properties is, however, extremely challenging. The inductive effect of chlorine atoms (partial withdrawal of valence electrons from the main chain)⁶ may facilitate the chain scission in ZEP. It was also hypothesized¹⁵ that ionization of chlorine by electron impact could lead to main-chain scission. The role of phenyl group in the performance of ZEP resist is not yet entirely clear; in addition to increasing the etch durability,⁸ the phenyl group may also play a role in the dissociation of the main-chain in the presence of the chlorine group.

Furthermore, in most applications different developers and development durations are employed for PMMA and ZEP, which challenges the comparison of the resists. In addition to hypothetical differences in the mechanism of main-chain scission, various rates of dissolution in different developers may also be a factor. In order to fully realize the potential of ZEP resists, the understanding of its properties needs to be improved.

The purpose of this research is to understand the exposure and development of ZEP 520A resist and compare these to PMMA 950k, both experimentally and by numerical modeling. For this purpose, we conduct EBL exposure and development of both resists using identical conditions wherever possible. We report a thorough comparison of the performance of PMMA and ZEP in MIBK:IPA 1:3, ZED-N50, and IPA:water 7:3 developers. In order to interpret the experimental results, we extended our simulation tool reported earlier for PMMA¹⁶ to include exposure and development of ZEP resist. We describe two hypothetical models of ZEP exposure, one assuming an enhancement of the main chain scission in ZEP as a result of electronic impact onto some of the side groups, and another without such enhancement. In the second case, the differences in ZEP and PMMA resists performance are attributed only to their different interactions with the developers. Using both approaches, we parameterize the respective models of ZEP development by fitting numerical results to the experimental resist morphologies, and analyze the outcomes.

## II. EXPERIMENT
Silicon substrates were spin coated with 55–63 nm thick ZEP-520A and PMMA 950k resist layers. Sets of periodic grating patterns of various pitches and increasing doses were patterned at 3–30 keV exposure voltage (Raith 150 and $150^{TWO}$). A wide array of periodic gratings with progressively increasing doses has been employed to identify the applicable dose windows within which quality gratings can be fabricated. Initially, the ZEP samples were developed in ZED-N50 (n-amyl acetate) for 30 s and rinsed in MIBK for 20 s. The selection of developer, rinse, and development duration was based on the standard procedures provided by the resist manufacturer and also in use by the scientific community. The experiments done with these conditions were used to generate Fig. 2(a) which compares the applicable dose windows of PMMA and ZEP for 3–30 keV exposure voltages. The PMMA data used in Fig. 2(a) was taken from our previous work¹⁷,¹⁸ using compatible experimental conditions. From Fig. 2(a), we estimate a 3.7–4.1 times sensitivity increase and a 3–7 times dose window decrease using ZEP compared to PMMA.

In order to better understand the development of ZEP, we decided to test MIBK as the developer instead of the rinse/stopper. Using 10 keV exposure and 30 s development in MIBK showed that 30 nm half-pitch gratings could be patterned at approximately 63 pC/cm, which is almost the same dose required for developing ZEP in ZED-N50 and rinsing in MIBK. The fact that MIBK could be used as a developer for ZEP at comparable sensitivity and development time was surprising but not entirely unexpected considering that MIBK is a very strong developer for PMMA and both PMMA and ZEP are polymeric resists with many similarities as seen in Fig. 1. Therefore, to proceed with a detailed comparison of ZEP and PMMA development, we developed both ZEP and PMMA for 2–20 s in ZED-N50, MIBK:IPA 1:3, and IPA:$H_2O$ 7:3 for 10 keV exposures. The samples developed in ZED-N50 and MIBK:IPA 1:3 were rinsed in IPA for 20 s, whereas the samples developed in IPA:$H_2O$ 7:3 were not rinsed at all. Using MIBK:IPA 1:3 and IPA:$H_2O$ 7:3 as developers for ZEP and using ZED-N50 as a developer for PMMA, especially for such short development durations is unique to our study. The data from this study was used to generate Fig. 2(b) and Fig. 3 in which the applicable dose windows as well as top-view grating morphologies of ZEP and PMMA resists are compared

$$
\mathrm{\left[
\begin{array}{c}
\mathrm{H_2C-C^{CH_3}} \\
\mathrm{O-C^{O}_{CH_3}}
\end{array}
\right]_n}
\quad
\mathrm{\left[
\begin{array}{c}
\mathrm{C_{6}H_5-C^{CH_3}-CH_2-C^{Cl}-CH_2} \\
\mathrm{O-C^{O}_{CH_3}}
\end{array}
\right]_n}
$$

FIG. 1. (left) PMMA and (right) ZEP polymer structures.

![](./images/813377556907556864_3.jpg)

FIG. 2. Comparison of the applicable dose windows for fabricating 35 nm half-pitch gratings in PMMA and ZEP resists at room temperature: (a) employing a 1:3 MIBK:IPA developer for PMMA and ZED-N50 developer for ZEP and various exposure voltages; (b) employing various developers and 10 keV exposure voltage. The bars show the range of doses for which quality grating patterns can be fabricated. All development was carried out for 5 s except for PMMA in ZED-N50 (2 s).

for ZED-N50, MIBK:IPA 1:3, and IPA: H₂O 7:3 developers. The sensitivity of PMMA remains nearly constant for the developers discussed, whereas ZEP shows a significant variation in sensitivity and dose window. Using IPA: H₂O 7:3 provides the highest resolution and lowest line edge roughness (LER) at the expense of reduced sensitivity. Further discussion is given in Sec. IV.

### III. MODELING
#### A. Model of electron-resist interaction

In order to better understand the properties of ZEP resist, we have extended our model of electron beam exposure of positive-tone resist (initially PMMA) reported recently.¹⁶,¹⁹ In brief, the positive-tone resist response is represented by main-chain C-C bond breaking through the impact of primary and secondary electrons, as well as those backscattered from the substrate. For a point source of primary electrons traveling a distance z in the resist, the probability of lateral broadening through elastic scattering can be described by the diffusion approximation,²⁰⁻²²

$$
P(z,\rho)\rho d\rho = \frac{3\lambda}{z^3}\exp\left(-\frac{3\lambda\rho^2}{2z^3}\right)\rho d\rho, \tag{1}
$$

where z is depth, $\rho$ is the lateral coordinate, and $\lambda$ is the elastic transport mean free path.²³ When traveling in the resist, primary electrons undergo inelastic collisions producing bond scissions and generating secondary electrons. The latter in turn produce further scissions and next-generation electrons, and so on. A widely used approach represents the exposure by a spatial distribution function (point spread function) of deposited energy in the form²⁰,²¹

$$
F(z,\rho) = \int_{0}^{\infty}f(|\rho-\rho_1|,E(z,\rho_1))P(z,\rho_1)\rho_1d\rho_1. \tag{2}
$$

![](./images/813377556907556864_4.jpg)

FIG. 3. Top-view SEM micrographs of 35 nm half-pitch PMMA and ZEP gratings exposed with 10 keV electrons and developed in ZED-N50, MIBK:IPA 1:3, and IPA:water 7:3 developers. The doses and minimum gap-widths achieved for each combination are noted. All samples are precoated with a 6 nm chromium anti-charging layer.

In our model¹⁶,¹⁹ we employ a similar form, however, instead of the point spread function of deposited energy, we consider the yield of main chain scission for a positive tone resist. We believe that computing the yield of bond scission directly without mapping the distributions of deposited energy avoids the well-known uncertainties related to the conversion of deposited energy into the scission yield,¹⁷,¹⁹ and also facilitates accounting for molecular properties of the material, which is important for the present extension of the model from PMMA to ZEP. In this work, we compute the three dimensional (3D) distributions of the probability of the main chain scission in PMMA and ZEP employing Eq. (2), where $E(z,\rho)$ is the energy of primary electrons at point $\{ z,\rho \}$, and $f(\rho,E)$ is the radial distribution of the scission probability including the impact of secondary and higher generation electrons. Adopting this partition, we simplify the task of finding a 3D distribution function of scission probability events in resist to a layer-by-layer computation.

Distinct from our previous work^{16,19} where equations of kinetic transport theory were employed to compute the radial distribution of the yield of scission $f(\rho,E)$, in the present work we have implemented a modified Monte Carlo simulation approach^{24} to compute the scission yields without mapping the distributions of deposited energy. To calculate the radial distribution of the scission probability, a point "primary" electron source with a particular energy and fixed direction in an appropriate resist is employed. These "primary" electrons generate scissions in the resist as well as produce secondary and higher generation electrons.

Secondary electrons undergo elastic and inelastic collisions as they travel in the resist. We describe elastic processes by a screened Rutherford elastic collision cross section.^{24} For the inelastic scattering events, we employ the Gryzinsky cross section^{25} as described in Refs. 16 and 19. Elastic scattering events formally involve a single moving electron, which changes only its direction but not its energy. Inelastic scattering processes are binary collision events, where a secondary electron is generated, and which are accompanied by inelastic energy losses. Accordingly, the energy of the electron before the collision, reduced by the ionization energy, is split into two generally unequal parts among two resulting electrons. The electron with greater energy is conventionally considered as "scattered," whereas the one with less energy is seen as "generated secondary" as a result of an inelastic collision. Inelastic collision events can only take place if the energy of the initial electron before the collision is greater than the energy of ionization.

The inelastic ionization losses depend on the structure of the resist. All electrons in the material are categorized into core electrons of particular shell and valence electrons.^{19} Valence electrons are in turn split into a group responsible for the main-chain bond breaking, and all other valence electrons.

Scattering events for each kind of collision, elastic or inelastic, and group of electrons are described by a cross section with particular parameters specified for the group. In the case of inelastic collisions, an important parameter is the appropriate shell binding energy or ionization energy $U_i$, where $i$ denotes the group of electrons. The ionization energy accounts for the inelastic loss of electron energy under this particular scattering event. Effective parameters that describe elastic collisions are the density, atomic weight, and atomic number of a particular resist.^{19} The total cross section employed in this work is,

$$
\begin{aligned}
\mu(E)=& \sum_{i} N_{i} \sigma_{i}(E)=N_{Rutherford} \sigma_{Rutherford}(E) \\
& +N_{Gryzinsky, 1 s-s h e l l} \sigma_{Gryzinsky, 1 s-s h e l l}(E)+\ldots, \quad(3)
\end{aligned}
$$

where $N_i$ is the number density of electrons for the corresponding cross section, and $\sigma_i(E)$ is an appropriate cross section for elementary elastic (Rutherford) or inelastic (Gryzinsky) scattering events. The number density of electrons is

$$
N_{i}=\frac{k_{i} \rho N_{A}}{M}, \quad(4)
$$

where $k_i$ is a number of electrons from a given group per monomer of the resist involved in a particular scattering process, $\rho$ is density of the resist, $N_A$ is Avogadro's number, and finally $M$ denotes the molar mass of a monomer.

The resulting 3D distribution of the yield of scission per monomer of the resist, computed using Eq. (2) for a point source of electrons in a resist of a given thickness, is then convolved with the writing pattern of interest. The contribution to scission from electrons backscattered from the substrate is described employing similar concepts. Further details of the model and a basic validation for PMMA are given in Refs. 16 and 19.

In this paper we compare two positive-tone resists, PMMA and ZEP. Parameters adopted for the calculation, the elementary processes considered, specification of the corresponding groups of electrons, and the number of electrons in each group for two resists are presented in Tables I, II, and III. For simplicity, all of the possible inelastic processes in the material are reduced, e.g., in the case of PMMA, to four ionization collisions, namely collisions with carbon and oxygen core electrons, collisions with valence electrons involved in main chain C-C bonding, and finally collisions with all other valence electrons. Knocking out a valence electron that has been involved in an intra-molecular binding is interpreted as the bond scission event. The binding energies (ionization energies) $U_i$ for core electrons and electrons in the main-chain bonds are available in the literature.^{19,26} For other valence electrons, the parameter $U_i$ has been fitted so that the total inelastic stopping power reproduces well the Bethe stopping power^{27} of electrons at 30 keV energy. The

<table>
<caption>Table I. Model parameters for PMMA resist, inelastic collisions.</caption>
<thead>
<tr>
<th>Elementary collision processes involving various groups of electrons</th>
<th>Number of electrons per monomer, $k_i$</th>
<th>$U_i$ (eV)</th>
</tr>
</thead>
<tbody>
<tr>
<td>Oxygen core 1s electrons</td>
<td>4</td>
<td>538^{19}</td>
</tr>
<tr>
<td>Carbon core 1s electrons</td>
<td>10</td>
<td>228^{19}</td>
</tr>
<tr>
<td>Valence electrons in main-chain C-C bonds^{a}</td>
<td>4</td>
<td>3.5^{19}</td>
</tr>
<tr>
<td>Other valence electrons</td>
<td>36</td>
<td>16.52^{b}</td>
</tr>
</tbody>
<tfoot>
<tr>
<td colspan="3">^{a}Inelastic collision events with this group of electrons are interpreted as resulting in main chain bond scission in PMMA (see Ref. 16 and 19).</td>
</tr>
<tr>
<td colspan="3">^{b}The average ionization potential is chosen to fit the total inelastic stopping power to the Bethe stopping power (see Ref. 27) at 30 keV.</td>
</tr>
</tfoot>
</table>

<table>
<caption>Table II. Model 1 parameters for ZEP resist, inelastic collisions.</caption>
  <thead>
    <tr>
      <th>Elementary collision processes involving various groups of electrons</th>
      <th>Number of electrons per monomer, $k_i$</th>
      <th>$U_i$ (eV)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Oxygen core 1s electrons</td>
      <td>4</td>
      <td>$538^{19}$</td>
    </tr>
    <tr>
      <td>Carbon core 1s electrons</td>
      <td>26</td>
      <td>$228^{19}$</td>
    </tr>
    <tr>
      <td>Chlorine core 1s electrons</td>
      <td>2</td>
      <td>$2808^{28}$</td>
    </tr>
    <tr>
      <td>Chlorine core 2s electrons</td>
      <td>2</td>
      <td>$286^{28}$</td>
    </tr>
    <tr>
      <td>Chlorine core 2p electrons</td>
      <td>6</td>
      <td>$219^{28}$</td>
    </tr>
    <tr>
      <td>Valence electrons in main-chain C-C bonds$^{\text{a}}$</td>
      <td>$8^{\text{a}}$</td>
      <td>$3.5^{\text{a}}$</td>
    </tr>
    <tr>
      <td>Collisions with valence electrons in side groups inducing remote bond scissions in the main chain$^{\text{b}}$</td>
      <td>$38^{\text{b}}$</td>
      <td>$3.5^{\text{b}}$</td>
    </tr>
    <tr>
      <td>Other collisions with valence electrons</td>
      <td>40</td>
      <td>$16^{\text{c}}$</td>
    </tr>
  </tbody>
</table>

$^{\text{a}}$Inelastic collision events with this group of electrons are interpreted as resulting in main chain bond scission. The number of electrons takes into account 8 main-chain C-C bond electrons per ZEP monomer.
$^{\text{b}}$These collisions are also interpreted as inducing a remote dissociation of C-C bonds in the main chain. The number of electrons can be interpreted as 30 valence electrons of phenyl side group and an effective upper estimate of 8 valence electrons of chlorine group. The corresponding ionization potential $U_i$ is adopted equal to that for regular main chain scission process.
$^{\text{c}}$The average ionization potential for other valence electrons is chosen to fit the total inelastic stopping power to the Bethe stopping power (see Ref. 27) at 30 keV.

model parameters employed to describe the inelastic colli-sions of electrons in PMMA are given in Table I. A similar approach to model main chain scission in PMMA has been employed elsewhere. $^{16,19}$

The major distinction between ZEP and PMMA is that the former contains a phenyl group and a chlorine atom (see Fig. 1). The chlorine introduces additional scattering events with core electrons from its inner shells. $^{28}$ In addition to this differ-ence, we have also explored a hypothesis that the collisions with valence electrons in the phenyl side group and chlorine group could result in a remote scission of the bonds in the main chain of ZEP. The parameters adopted in this model, denoted here as the ZEP Model 1, are given in Table II. For comparison, we have also considered a ZEP exposure model without the enhanced bond scission (ZEP Model 2). In this second model, only inelastic collisions with valence electrons involved in main chain C-C bonds lead to the chain scission, as occurs in PMMA. The corresponding model parameters can be found in Table III.

Figure 4(a) shows an example of the computed yield of the main-chain scission per monomer in a PMMA layer on a silicon substrate for a periodic grating with a 70 nm pitch exposed with three representative voltages using the doses from the applicable windows shown in Fig. 2(a). For ZEP, Figs. 4(b) and 4(c) illustrate the predictions by Models 1 and 2, respectively, for similar conditions of exposure; whereas Figs. 5(a) and 5(b) show how the ratio of the nominal yields of main chain scission predicted by ZEP Models 1 and 2 depends on the location in the grating pattern.

### B. Modeling of ZEP development

In order to explore development of exposed ZEP, we employed our dissolution model described in detail else-where, $^{16,17}$ which has already proven to work well for PMMA. $^{16,18}$ In brief, during dissolution the resist-developer interface is moving with the rate

$$
v(\mathbf{r})=\frac{D(\mathbf{r})}{L}, \tag{5}
$$

where $L$ is the resist shrinkage depth and $D(\mathbf{r})$ denotes the effective diffusion coefficient at the interface location $\mathbf{r}$,

<table>
<caption>Table III. Model 2 parameters for ZEP resist, inelastic collisions.</caption>
  <thead>
    <tr>
      <th>Elementary collision processes involving various groups of electrons</th>
      <th>Number of electrons per monomer involved, $k_i$</th>
      <th>$U_i$ (eV)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Oxygen core 1s electrons</td>
      <td>4</td>
      <td>538</td>
    </tr>
    <tr>
      <td>Carbon core 1s electrons</td>
      <td>26</td>
      <td>228</td>
    </tr>
    <tr>
      <td>Chlorine core 1s electrons</td>
      <td>2</td>
      <td>$2808^{28}$</td>
    </tr>
    <tr>
      <td>Chlorine core 2s electrons</td>
      <td>2</td>
      <td>$286^{28}$</td>
    </tr>
    <tr>
      <td>Chlorine core 2p electrons</td>
      <td>6</td>
      <td>$219^{28}$</td>
    </tr>
    <tr>
      <td>Valence electrons in main-chain C-C bonds$^{\text{a}}$</td>
      <td>$8^{\text{a}}$</td>
      <td>$3.5^{\text{a}}$</td>
    </tr>
    <tr>
      <td>Other valence electrons</td>
      <td>78</td>
      <td>$16^{\text{b}}$</td>
    </tr>
  </tbody>
</table>

$^{\text{a}}$Inelastic collision events with this group of electrons are interpreted as resulting in main chain bond scission. The number of electrons takes into account 8 main-chain C-C bond electrons per ZEP monomer.
$^{\text{b}}$The average ionization potential is chosen to fit the total inelastic stopping power to the Bethe (see Ref. 27) stopping power at 30 keV.

![](./images/813377556907556864_5.jpg)

FIG. 4. Computed lateral distributions of the average nominal yield of main chain scissions per monomer in (a) PMMA, (b) ZEP Model 1, and (c) ZEP Model 2 for a periodic 70 nm pitch grating, exposed with 3 keV, 10 keV, and 30 keV voltages, for exposure doses from the applicable windows identified experimentally in PMMA [see Fig. 2(a)]. The plots are taken at half-depth of 55 nm thick resist layers on a silicon substrate.

$$
D(\mathbf{r})=\left\langle\frac{\beta}{n^{a}}\right\rangle, \quad \alpha(\mathbf{r})= \begin{cases}1+\langle n\rangle / n_{0}, & \langle n\rangle<n_{0} \\ 2, & \langle n\rangle \geq n_{0}\end{cases}. \quad (6)
$$

In this equation, $n$ stands for polymer fragment length measured in basic units corresponding to two main-chain C-C atoms. According to this definition, an MMA monomer corresponds to $n=1$. For a strictly alternating copolymer, one nominal monomer unit of ZEP corresponds to $n=2$, whereas ZEP fragments corresponding to $n=1$ and other odd $n$ numbers represent averaged kinetic properties of two possible formulations each. In the future, the model can be upgraded by distinguishing the composition of small ZEP fragments. The averaging in Eq. (6) is performed over the local distribution of the fragment size of the exposed resist, $\beta$ is a constant coefficient, and $n_{0}$ represents a characteristic fragment size at which the chain entanglement regime is reached. $^{16,17}$ The 3D spatial distribution of the resist fragments over size is derived from the corresponding main chain scission yield profiles as described in Ref. 16. The development process is represented by a sequence of discrete dissolution steps with time $\delta t$ required to dissolve a resist layer of thickness $\delta L$ at location $\mathbf{r}$ determined by $\delta t=2 L \delta L / D(\mathbf{r})$. The simulation provides the location of the three-dimensional resist-development interface as a function of development time.

![](./images/813377556907556864_6.jpg)

FIG. 5. (a) Ratio of the nominal scission yields from two ZEP models, ZEP-1/ZEP-2, for a 70 nm pitch grating exposed in a 60 nm thick resist layer with 10 keV electrons. (b) Plots of the ratio of scission yields from two ZEP models, ZEP-1/ZEP-2 for the same conditions as in (a) in the top, middle, and at the bottom of the resist layer.

In this model, the interaction between developer and resist can be characterized by two parameters, $\beta$ and $n_{0}$. In this work, we estimate these parameters by fitting the predicted development profiles to experimental data from Sec. II. As the objective function for the fitting, the following expression was chosen,

$$
\Delta=\sqrt{\frac{1}{N} \sum^{N}\left(L_{\exp }-L_{\mathrm{mod}}\right)^{2}}, \quad (7)
$$

where $L_{\exp }$ and $L_{\mathrm{mod}}$ are experimentally determined and predicted trench widths, respectively, and $N$ denotes the number of experimental points for the given conditions, which varied from 11 to 24. One can expect that the dissolution parameters $\beta$ and $n_{0}$ should not depend on the details of the exposure geometry, such as the grating pitch. Thus, in order to check the consistency of our ZEP models, we performed individual fitting for two different pitches for each of the developers considered. This involved 50 and 70 nm pitches for ZED and 60 and 70 nm pitches for IPA:water and MIBK:IPA mixtures, see also Table IV. The value of the deviation $\Delta$ was also employed as a control parameter. The fitting results are presented in Table IV.

TABLE IV. Fitting results for two scission models for ZEP. The parameters $n_0$ and $\beta$ for two ZEP development models were evaluated by fitting the numerical results to the experimentally determined widths of trenches in developed ZEP resist, employing the deviation $\Delta$ defined by Eq. (7) as the objective function. For each developer, independent fitting procedures were performed for different grating pitches.

| Developer   | Grating Pitch | ZEP Model 1                          | ZEP Model 2                          |
|-------------|---------------|--------------------------------------|--------------------------------------|
|             |               | $n_0$ | $\beta$, nm²/s | $\Delta$, nm | $n_0$ | $\beta$, nm²/s | $\Delta$, nm |
| ZED         | 50 nm         | 32    | 7300           | 1.5          | 140   | 90000          | 1            |
| ZED         | 70 nm         | 29    | 10500          | 3            | 680   | $4.3\cdot10^6$  | 2.5          |
| IPA:water   | 60 nm         | 1.9   | 200            | 9            | 11    | 1400           | 4            |
| IPA:water   | 70 nm         | 1.6   | 140            | 14           | 48    | 35000          | 5            |
| MIBK:IPA    | 60 nm         | 8.7   | 960            | 2.5          | 38    | 9300           | 1.5          |
| MIBK:IPA    | 70 nm         | 7.0   | 1100           | 3            | 170   | $3.3\cdot10^5$  | 2            |

## IV. DISCUSSION

Comparing the experimentally observed applicable dose windows of PMMA 950k resist developed in an MIBK:IPA mixture and ZEP 520A resist developed in ZED solvent for various exposure voltages from Fig. 2(a), it is possible to estimate the sensitivity ratio using the minimum dose required for clearance. From Fig. 2(a), we obtain a 3.7–4.1 times better sensitivity using ZEP with a somewhat stronger sensitivity improvement tending to occur at lower voltages. These observations are in accordance with earlier reports in literature. $^{9,11}$ In addition, we observe that the applicable dose window of ZEP is 3–7 times smaller than for PMMA for each exposure voltage, i.e., the process for ZEP is less robust than that for PMMA.

Furthermore, our experiments revealed that (1) ZEP can be successfully developed for very short times of only 5 s, and (2) ZEP can be developed in developers usually employed for PMMA, such as MIBK, MIBK:IPA 1:3, and IPA:water 7:3. Similarly, PMMA can be developed in ZEP’s developer ZED-N50. Comparing the development of 10 keV exposed PMMA and ZEP resists in ZED-N50, MIBK:IPA 1:3, and IPA: $\text{H}_2\text{O}$ 7:3 developers [Fig. 2(b)], we observe that ZEP shows a significant variation in both sensitivity and applicable dose windows, whereas the performance of PMMA is less dependent on the formulation of the developer. Thus, PMMA’s sensitivity is nearly constant for the three developers discussed. The most pronounced sensitivity improvement of 20% was achieved for PMMA developed in IPA:$\text{H}_2\text{O}$ 7:3 in comparison to MIBK:IPA 1:3, which could be expected. $^{29}$ However, ZEP becomes approximately 12 times less sensitive and at the same time exhibits a significantly larger applicable dose window when developed in IPA:$\text{H}_2\text{O}$ 7:3 in comparison to ZED-N50.

Next, the grating morphologies shown in Fig. 3 demonstrate that the best resolution and line edge roughness (LER) are also obtained for ZEP development in IPA:$\text{H}_2\text{O}$ 7:3 as compared to all other resist/developer combinations studied. This significant improvement comes at the expense of a much lower sensitivity. However, ZEP also shows a better resolution and LER improvement when developed in MIBK:IPA 1:3, with a sensitivity increased by a factor of 2 compared to IPA:$\text{H}_2\text{O}$ 7:3. The best sensitivity is obtained for development of ZEP in ZED-N50, as one could expect; however, in this case the LER is clearly poorer than for all other resist/developer combinations studied.

The strong dependence of all aspects of the ZEP resist performance on the developer which we observed experimentally is entirely unexpected, and very different from the behaviors of PMMA. This suggests a unique interaction between ZEP and the developers studied. Generally, it is widely adopted that ZEP is a much more complex resist than PMMA. That is why special care should be taken to explain its behavior theoretically. From a theoretical point of view, one of the most intriguing questions is which particular mechanism provides ZEP with its high sensitivity in some developers. There are at least two possible mechanisms for the sensitivity increase. One evident hypothesis is that the scission of the main chain of ZEP could be enhanced, for example, as a result of electron impact onto some of side groups. $^{15}$ Although appealing because of its relative simplicity, this approach seems to be challenged by significant variation of the ZEP sensitivity with the developer that we observe experimentally. This raises a question of whether the complex chemical composition of ZEP, which includes a chlorine group and a phenyl group, could result in a selectivity of the dissolution process because of a unique physicochemical interaction of the ZEP resist with developers. Our experiments with three different developers strongly support the idea that the dissolution process plays an important role in ZEP performance.

In the present paper, we have explored numerical models representing both approaches. To describe a possibly higher scission rate of the ZEP main chain, we have considered that remote bond breaking could occur upon electron impact onto some of the side groups (ZEP Model 1). Technically, this model provides a greater nominal yield of main chain scissions. As it can be seen from Figs. 4(a) and 4(b), the predicted main-chain scission yield per monomer in ZEP Model 1 is approximately 10 times higher than that of PMMA at similar conditions. This is even higher than the experimentally observed 3.7–4.1 times increase in sensitivity, which is attributable to an approximately 2.4 times difference in nominal monomer sizes of ZEP and PMMA. The predicted ratio of scission yields for ZEP Model 1 and PMMA showed a very weak dependency on the exposure voltage. One can conclude that Model 1 provides sufficient enhancement of the scission of the main chain to explain the observed high sensitivity of ZEP resist when it is developed in ZED-N50.

Another model which we have explored (ZEP Model 2) does not involve any special enhancement of the scissions. In this model, the main chain scission mechanism is similar to that for PMMA. The corresponding nominal yield of scission [Fig. 4(c)] is approximately twice that of PMMA, because of the difference in the size of the monomeric units in PMMA and ZEP. In comparison to Model 1, Model 2 predicts an approximately 5 times lower yield of scissions. It can also be seen in Figs. 5(a) and 5(b) that the ratio of the local scission probabilities predicted by Models 1 and 2 for a grating pattern is nonuniform and depends on the location.

From the results obtained with Model 1 representing a case of strong enhancement of main-chain scissions in ZEP, and Model 2 without the enhancement, one can predict that the conceivable sensitivity of ZEP to exposure can vary from approximately 5 times larger than in PMMA to about the same as in PMMA.

Although the main-chain scission yield plays an extremely important role in determining the sensitivity of positive tone resists, considering the scission yield alone does not explain the strong dependence of ZEP sensitivity on the developer. Actually, the interaction of the exposed resist with the solvent which takes place during the develop- ment process would ultimately define the performance. This interaction could either enhance or inhibit the sensitivity depending on the formulation of the developer. We therefore also explored the compatibility of both ZEP scission models with the observed development profiles, employing a model of resist dissolution described in Sec. III B.

In Table IV it can be seen that ZEP Model 1 works reason- ably well for ZED and MIBK:IPA developers, showing com- patible values of the parameters $\beta$ and $n_{0}$ for different grating pitches as well as reasonable levels of the deviation $\Delta$. The examples of computed development profiles for 70 nm pitch gratings presented in Figs. 6(a) and 6(c) illustrate the success- ful performance of ZEP Model 1 for ZED and MIBK:IPA developers. However, ZEP Model 1 failed to describe devel- opment in IPA:water solvent, as demonstrated by high values of the deviation $\Delta$ in Table IV. The corresponding develop ment profile which provides the best fit to experimental trench width [Fig. 6(b)] is too shallow and does not exhibit clearance, although quality gratings were observed experi- mentally at similar conditions. For ZEP Model 2, no satisfac- tory results were obtained for any of the three developers. As can be seen in Table IV, the values of $\beta$ parameter differ by 30 times for slightly different pitches of gratings, which is inconsistent.

To summarize, our simulations of dissolution of exposed ZEP resist employing Model 1 were successful to match the experimental data for ZEP-N50 and MIBK:IPA developers, but not for IPA:water developer. Simply speaking, in the case of IPA:water developer, Model 1 resulted in too strong frag- mentation at experimentally relevant doses, requiring unrealis- tically low mobility coefficients $\beta$ to achieve a matching trench width. This might indicate that Model 1 overestimates the enhancement of the main-chain scission, speaking rather in favor of Model 2. Simulations employing the latter, how- ever, did not work well for any of the developers. Trying to understand the reason, it should be noted that the compatibility depends on at least two different factors, the scission model and the kinetic dissolution model. Although the overall better performance of Model 1 may indicate that some enhancement of the main-chain scission is present in ZEP, one cannot rule out a possibility of other mechanisms of scission enhance- ment, or even no enhancement at all as assumed in our Model 2. In the latter case, the kinetic dissolution model (5,6) should be modified. Thus, our approach to describe the dissolution based on the Flory-Huggins theory $^{30}$ may require a more so phisticated accounting for the differences in the formulations and molecular sizes in the resist fragments and solvent mix- tures, as well as a further extension to describe the interaction of water and other solvents with polar groups in ZEP. Future research of temperature dependence of ZEP sensitivity using various developers, both numerically and experimentally, will also be helpful to clarify the role of the dissolution process in the performance of ZEP resist.

![](./images/813377556907556864_7.jpg)

FIG. 6. Cross-sections of 3D ZEP resist profiles (white, ZEP; black, no ZEP) computed using Model 1 for 70 nm pitch gratings, exposed with 10 keV electrons and developed during 10 s in (a) ZED developer, exposure dose 130 pC/cm, (b) IPA:water developer, exposure dose 1600 pC/cm, and (c) MIBK:IPA developer, dose 500 pC/cm. The doses correspond to approxi- mately the middle of the experimentally determined applicable dose win- dows for the conditions given.

## V. CONCLUSIONS

If the EBL conditions are properly optimized, ZEP resist performance may exceed that of PMMA. ZEP performance

depends significantly on the developer. ZED developer increases the sensitivity, whereas IPA:water mixture opti- mizes LER and conceivably the resolution at the expense of a loss in sensitivity. Interestingly, MIBK:IPA 1:3 mixture seems to be a very good developer for ZEP and quite adequate if sensitivity is not an issue. IPA:water 7:3 develop- ment provides the best resolution and line edge roughness for both ZEP and PMMA, however, the sensitivity decreases dramatically.

Out of two alternative models of EBL exposure in ZEP, one assuming an enhancement of the main chain scission in ZEP, and another without such enhancement, the first shows a better compatibility with our experiments employing ZED and MIBK:IPA developers. Although this indicates that an enhancement of the main-chain scission in ZEP may take place, other results suggest that an alternative interpretation attributing the ZEP resist performance mostly to its interac- tion with developers, cannot be ruled out yet.

The IPA:water developer is the most promising for usage of ZEP as an ultrahigh resolution resist. However, under- standing the behavior of ZEP in IPA:water mixture is a chal- lenge. The available models do not seem to work well for this mixture. Further effort, both theoretically and experi- mentally, is required to improve the understanding of ZEP interaction with IPA:water mixture so that the potential of high resolution nanofabrication using ZEP is fully realized.

## ACKNOWLEDGMENTS
The authors would like to acknowledge the University of Alberta NanoFab, NINT Electron Microscopy group, and the support of NINT-NRC, NSERC, Alberta Innovates, and iCORE.

$^{1}$W. Chen and H. Ahmed, J. Vac. Sci. Technol. B 11, 2519 (1993).
$^{2}$W. Hu, G. H. Bernstein, K. Sarveswaran, and M. Lieberman, J. Vac. Sci. Technol. B 22, 1716 (2004).
$^{3}$B. Cord, J. Lutkenhaus, and K. K. Berggren, J. Vac. Sci. Technol. B 25, 2016 (2007).
$^{4}$L. Ocola and A. Stein, J. Vac. Sci. Technol. B 24, 3061 (2006).
$^{5}$H. Yang, A. Jin, Q. Luo, C. Gu, and Z. Cui, Microelectron. Eng. 84, 1109 (2007).
$^{6}$T. Ishii and K. Shigenara, in *Hybrid Nanocomposites for Nanotechnology: Electronic, Optical, Magnetic and Biomedical Applications* (Springer, New York, 2009), Chap. 9, p. 394.
$^{7}$T. Kozawa and S. Tagawa, Jpn. J. Appl. Phys. 49, 030001 (2010).
$^{8}$T. Nishida, M. Notomi, R. Iga, and T. Tamamura, Jpn. J. Appl. Phys. 31, 4508 (1992).
$^{9}$H. Namatsu, M. Nagase, K. Kurihara, K. Iwadate, and K. Murase, Microelectron. Eng. 27, 71 (1995).
$^{10}$D. M. Tanenbaum, C. W. Lo, M. Isaacson, H. G. Craighead, M. J. Rooks, K. Y. Lee, W. S. Huang, and T. H. P. Chang, J. Vac. Sci. Technol. B 14, 3829 (1996).
$^{11}$H. Wang, L. Fan, A. Jin, Q. Luo, C. Gu, and Z. Cui, Proc. 1st IEEE-NEMS, 60501014, 391 (2006).
$^{12}$ZEON Corporation Electronic Materials Division, ZEP520A Technical Report, ver. 2, Oct. 2010, available from http://www.zeonchemicals.com/pdfs/ZEP520A.pdf (Last accessed 9 July 2011).
$^{13}$M. A. Mohammad, S. K. Dew, M. Stepanova, and K. Westra, unpublished material, University of Alberta, 2011.
$^{14}$H. Wang, G. M. Laws, S. Milicic, P. Boland, A. Handugan, M. Pratt, T. Eschrich, S. Myhajlenko, J. A. Allgair, and B. Bunday, J. Vac. Sci. Technol. B 25, 102 (2007).
$^{15}$H. Ikeura-Sekiguchi, T. Sekiguchi, and M. Koikea, J. Electron Spectrosc. Relat. Phenom. 144-147, 453 (2005).
$^{16}$M. Stepanova, T. Fito, Z. Szabó, K. Alti, A. P. Adeyenuwo, K. Koshelev, M. Aktary, and S. K. Dew, J. Vac. Sci. Technol. B 28, C8C48 (2010).
$^{17}$M. A. Mohammad, T. Fito, J. Chen, S. Buswell, M. Aktary, S. K. Dew, and M. Stepanova, in *Lithography (INTECH Croatia 2010)*, Chap. 16, pp. 318, available at http://www.intechopen.com/books/show/title/lithography (Last accessed 9 July 2011).
$^{18}$M. A. Mohammad, T. Fito, J. Chen, S. Buswell, M. Aktary, M. Stepanova, and S. K. Dew, Microelectron. Eng. 87, 1107 (2010).
$^{19}$M. Aktary, M. Stepanova, and S. K. Dew, J. Vac. Sci. Technol. B 24, 768 (2006).
$^{20}$N. Glezos, I. Raptis, D. Tsoukalas, and M. Hatzakis, J. Vac. Sci. Technol. B 10, 2606 (1992).
$^{21}$I. Raptis, N. Glezos, and M. Hatzakis, J. Vac. Sci. Technol. B 11, 2754 (1993).
$^{22}$B. K. Paul, Microelectron. Eng. 49, 233 (1999).
$^{23}$D. Liljequist, F. Salvat, R. Mayol, and J. D. Martinez, J. Appl. Phys. 65, 2431 (1989); ibid., 66, 2768 (1989).
$^{24}$D. C. Joy, *Monte Carlo Modeling for Electron Microscopy and Microanalysis* (Oxford University Press, Oxford, 1995).
$^{25}$M. Gryzinsky, Phys. Rev. 138, 336 (1965).
$^{26}$N. Samoto and R. Shimizu, J. Appl. Phys 54, 3855 (1983).
$^{27}$D. C. Joy and S. Luo, Scanning, 11, 176 (1989).
$^{28}$R. E. Watson and A. J. Freeman, Phys. Rev. 123, 521 (1961).
$^{29}$S. Yasin, D. G. Hasko, and H. Ahmed, Microelectron. Eng. 61-62, 753 (2002).
$^{30}$P. J. Flory, *Principles of Polymer Chemistry* (Cornell University Press, Ithaca, NY, 1953).