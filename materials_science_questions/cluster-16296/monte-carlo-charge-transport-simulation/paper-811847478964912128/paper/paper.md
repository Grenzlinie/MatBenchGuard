# High-mobility heterostructures based on InAs and InSb: A Monte Carlo study

H. Rodilla, T. González, D. Pardo, and J. Mateos${}^{\text{a)}}$

Departamento de Física Aplicada, Universidad de Salamanca, Plaza de la Merced s/n, 37008 Salamanca, Spain

Received 24 February 2009; accepted 17 April 2009; published online 4 June 2009

In this work, by means of Monte Carlo simulations, two different narrow band gap semiconductors, InAs and InSb, and their associated heterostructures, AlSb/InAs and AlInSb/InSb, have been studied. The parameters for the bulk simulations have been optimized in order to correctly reproduce the experimental mobility values. For the correct simulation of the heterostructures, roughness scattering has been included in the model, and its strength has been adjusted to achieve a good agreement with the experimentally measured mobility. © 2009 *American Institute of Physics*.

[DOI: 10.1063/1.3132863]

## I. INTRODUCTION

In “traditional” high electron mobility transistors (HEMTs), the highest cutoff frequencies have been achieved by using high In content (up to 70%) InGaAs channels (with an AlInAs barrier). In the past years, semiconductors with narrower band gap have been used for the channel of HEMTs in order to achieve much higher electron mobilities (thanks to a lower effective mass). Heterostructures with narrow band gap semiconductors such as AlSb/InAs and AlInSb/InSb (so-called Sb-based heterojunctions) have thus become a great option for improving the performance of HEMTs in high-speed, low-noise, and low-power applications and so increase their possibilities of being used for military and space applications with ultra low-power requirements. ${}^{1\text{--}10}$ Even if Sb-based 2-dimensional electron gas channels suffer from a degradation due to the roughness of the heterojunction (mainly due to the nonmaturity of the technology and the presence of defects), both InAs and InSb channels provide much higher values of mobility than those obtained in the fastest InP based heterojunctions. ${}^{4,10}$

In Sb-based HEMTs, due to the extremely high mobility of narrow band gap semiconductors, electron transport can easily become ballistic (or at least quasiballistic) when the gate length is reduced to submicron length. Under these conditions, the classic drift-diffusion or hydrodynamic models, traditionally used for device simulation and design, are not valid anymore. The most adequate technique is the Monte Carlo (MC) method, ${}^{11}$ able to account for ballistic transport and provide not only static results but also the dynamic and noise behavior of the devices. MC simulations are an exceptionally useful tool for the optimization of the transistors from a physical point of view, taking as a basis the knowledge of the internal microscopic processes.

A first step for the MC simulation of Sb-HEMTs is the adequate simulation of bulk InAs and InSb and their corresponding heterojunctions. However, in spite of increasing efforts being dedicated to the improvement of the fabrication of Sb-based HEMTs, few studies based on detailed microscopic simulations have been published, ${}^{8,12}$ and the numerous parameters needed for the MC simulations are not well established at all. Therefore, not only a thorough bibliographic search is necessary, but also a process of fine adjustment of the individual parameters is needed in order to verify their influence and obtain satisfactory values for them. As the technology for the fabrication Sb-based heterostructures is far from being advanced, a key parameter for reproducing the properties of electron transport in the channel is the amount of roughness scattering.

The aim of this work is the study of the transport properties in bulk InSb, InAs, and their associated heterostructures by means of the accurate adaptation of MC simulators. A key parameter for the simulation of the heterostructures is the roughness of the interface. The choice of the value of the roughness parameter that provides a good agreement with the experimental results will give us important information about the ideality of the interfaces and will pave the way for the MC study of advanced Sb-HEMTs.

This article is organized as follows. In Sec. II the parameters for the simulation of bulk semiconductors are presented, and the electron transport in bulk InAs, InSb, AlSb, and ${\text{Al}}_{0.15}{\text{In}}_{0.85}\text{Sb}$ is studied. Then, in Sec. III, AlSb/InAs and ${\text{Al}}_{0.15}{\text{In}}_{0.85}\text{Sb/InSb}$ heterostructures are simulated. The involved parameters are fine tuned by adjusting the strength of roughness scattering, thus allowing obtaining a good agreement with experimental mobilities of real samples. Finally, in Sec. IV, the main conclusions of this work are drawn.

## II. BULK SEMICONDUCTORS

The first step for the simulation of devices based in narrow band gap semiconductors is to define correct parameters for the MC models of bulk materials and their corresponding heterostructures. For this sake, a thorough bibliographic study has been performed. Since the interest on these high-mobility semiconductors is recent and the technology not

${}^{\text{a)}}$Electronic mail: javierm@usal.es

<table><caption>TABLE I. Bulk semiconductor parameters.</caption>
<tbody>
<tr>
<td>Symbol</td>
<td colspan="3">InSb</td>
<td colspan="3">InAs</td>
<td colspan="3">AlSb</td>
</tr>
<tr>
<td>Density (Kg/m³)</td>
<td colspan="3">5790</td>
<td colspan="3">5667</td>
<td colspan="3">4260</td>
</tr>
<tr>
<td>Sound velocity (m/s)</td>
<td colspan="3">4060</td>
<td colspan="3">4282</td>
<td colspan="3">4250</td>
</tr>
<tr>
<td>Static dielectric constant</td>
<td colspan="3">15.68</td>
<td colspan="3">12.25</td>
<td colspan="3">10.24</td>
</tr>
<tr>
<td>Optic dielectric constant</td>
<td colspan="3">17.65</td>
<td colspan="3">15.15</td>
<td colspan="3">12.04</td>
</tr>
<tr>
<td>Band gap (eV)</td>
<td colspan="3">0.18</td>
<td colspan="3">0.354</td>
<td colspan="3">1.615</td>
</tr>
<tr>
<td>Lattice parameter (Å)</td>
<td colspan="3">6.479</td>
<td colspan="3">6.058</td>
<td colspan="3">6.135</td>
</tr>
<tr>
<td>Optical phonon energy (eV)</td>
<td colspan="3">24.4</td>
<td colspan="3">30.0</td>
<td colspan="3">36.0</td>
</tr>
<tr>
<td></td>
<td>$\Gamma$</td>
<td>$L$</td>
<td>$X$</td>
<td>$\Gamma$</td>
<td>$L$</td>
<td>$X$</td>
<td>$\Gamma$</td>
<td>$L$</td>
<td>$X$</td>
</tr>
<tr>
<td>Effective mass ($m^*/m_0$)</td>
<td>0.014</td>
<td>0.220</td>
<td>0.130</td>
<td>0.023</td>
<td>0.29</td>
<td>0.64</td>
<td>0.14</td>
<td>0.70</td>
<td>0.53</td>
</tr>
<tr>
<td>No parabolicity coef. (eV⁻¹)</td>
<td>5.72</td>
<td>5.72</td>
<td>5.72</td>
<td>1.39</td>
<td>0.54</td>
<td>0.90</td>
<td>5.72</td>
<td>5.72</td>
<td>5.72</td>
</tr>
<tr>
<td>Energy from $\Gamma$ valley (eV)</td>
<td>0.0</td>
<td>0.76</td>
<td>0.46</td>
<td>0.0</td>
<td>1.1</td>
<td>1.6</td>
<td>0.0</td>
<td>−0.09</td>
<td>−0.68</td>
</tr>
<tr>
<td>Acoustic def. pot. (eV)</td>
<td>5.96</td>
<td>5.96</td>
<td>5.96</td>
<td>5.93</td>
<td>7.23</td>
<td>9.02</td>
<td>2.20</td>
<td>2.20</td>
<td>2.20</td>
</tr>
<tr>
<td>Optic def. pot. (eV)</td>
<td>0.0</td>
<td>2.5</td>
<td>0.0</td>
<td>0.0</td>
<td>2.3</td>
<td>0.0</td>
<td>0.0</td>
<td>1.0</td>
<td>0.0</td>
</tr>
<tr>
<td>Intervalley def. pot. ($10^{10}$ eV/m)</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>from $\Gamma$ to</td>
<td>0.0</td>
<td>5.0</td>
<td>5.0</td>
<td>0.0</td>
<td>5.6</td>
<td>6.3</td>
<td>0.0</td>
<td>1.0</td>
<td>1.0</td>
</tr>
<tr>
<td>from $L$ to</td>
<td>5.0</td>
<td>5.0</td>
<td>10.0</td>
<td>5.6</td>
<td>6.3</td>
<td>5.6</td>
<td>1.0</td>
<td>1.0</td>
<td>1.0</td>
</tr>
<tr>
<td>from $X$ to</td>
<td>5.0</td>
<td>10.0</td>
<td>5.0</td>
<td>6.3</td>
<td>5.6</td>
<td>3.4</td>
<td>1.0</td>
<td>1.0</td>
<td>1.0</td>
</tr>
<tr>
<td>Intervalley phonon energy (meV)</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>from $\Gamma$ to</td>
<td>0.0</td>
<td>19.9</td>
<td>19.9</td>
<td>0.0</td>
<td>17.4</td>
<td>19.2</td>
<td>0.0</td>
<td>36.0</td>
<td>36.0</td>
</tr>
<tr>
<td>from $L$ to</td>
<td>19.9</td>
<td>19.9</td>
<td>19.9</td>
<td>17.4</td>
<td>19.2</td>
<td>17.4</td>
<td>36.0</td>
<td>36.0</td>
<td>36.0</td>
</tr>
<tr>
<td>from $X$ to</td>
<td>19.9</td>
<td>19.9</td>
<td>19.9</td>
<td>19.2</td>
<td>17.4</td>
<td>19.3</td>
<td>36.0</td>
<td>36.0</td>
<td>36.0</td>
</tr>
</tbody>
</table>

completely mature (mainly for InSb), big discrepancies are found when looking for simulation parameters. This is espe- cially critical for MC simulations, where not only macro- scopic parameters are necessary but also those related to scattering rates. Therefore, to correctly choose the values better reproducing the experimental results, the bibliographic revision $^{12-25}$ has been followed by the fine adjustment of the MC simulation parameters.

In the simulations, in addition to the narrow band gap semiconductors, InAs and InSb, the materials commonly used to form the heterostructure barrier, AlSb and Al₀.₁₅In₀.₈₅Sb, respectively, need also to be considered. Table I shows the MC simulation parameters used for InSb, InAs, and AlSb. For all of them three nonparabolic spherical val- leys ($\Gamma$, $L$, and $X$) are considered to form the conduction band in the model. As can be observed, both InSb and InAs have a narrow direct band gap with very small electron ef- fective masses in the bottom of $\Gamma$ valley (0.014 and 0.023, respectively). On the other hand, AlSb has a wide indirect band gap with the lowest valley placed in the $\Delta$ direction, exhibiting a high effective mass (0.14). We will also call it $X$ valley even if it is not exactly placed on the $X$ point. In the case of Al₀.₁₅In₀.₈₅Sb (used as barrier material for InSb), the simulation parameters have been obtained by linear interpo- lation between those of InSb and AlSb, providing a direct band gap semiconductor with $m_{\Gamma}$=0.033 and a band gap of 0.395 eV, somewhat larger than that of InSb (0.18 eV).

Simulation parameters have been adjusted by means of a single particle MC simulator $^{26,27}$ properly adapted to be used for narrow band gap semiconductors. For example, impact ionization mechanisms have been implemented in the model since they may play a very important role in this kind of semiconductors. Indeed, impact ionization appears for elec- tron energies lower than those necessary for intervalley transfer, thus practically avoiding the saturation of the $I$-$V$ curves of devices fabricated with narrow band gap semiconductors. $^{4,6-8}$ Impact ionization has been introduced in our single particle MC by means of the Keldysh expres- sion, the probability per unit time of having an impact ion- ization event being $P(E)=S[(E-E_{\rm th})/E_{\rm th}]^2$ for $E$>$E_{\rm th}$ and 0 otherwise, $^{19,28,29}$ with $E$ the electron energy and $E_{\rm th}$ a threshold energy ($E_{\rm th}$=$1.08E_{\rm gap}$, $^{12}$ $E_{\rm gap}$ being the energy gap of the semiconductor). Since the value of the proportionality factor of impact ionization $S$ is not known, three values have been considered in the simulations ($S$=0, $0.5\times10^{12}$, and $1\times10^{12}$ s⁻¹) in order to analyze the relevance of this pro- cess.

The velocity-field curves obtained for undoped InAs, InSb, AlSb, and Al₀.₁₅In₀.₈₅Sb are shown in Fig. 1(a). As observed in the figure, InAs and InSb offer not only remarkably high mobilities ($\mu$=28 000 cm²/V s and $\mu$=67 000 cm²/V s, respectively) but also very large peak velocities. However, while the values of mobility do not de- pend on the amount of impact ionization processes, the val- ues of the peak velocity do so. The maximum velocity in- creases with higher $S$ since $\Gamma$ valley population is raised by the more frequent impact ionization events [Fig. 1(b)]. Also, as a consequence of a higher impact ionization probability, the maximum electron velocity is shifted to higher electric fields. The problem is that no complete experimental data of velocity-field characteristics exist for these materials so that the correct value for $S$ cannot be exactly estimated.

Regarding the materials for the heterostructure barriers, the electron mobility of AlSb is really small,

![](./images/811847478964912128_1.jpg)

FIG. 1. (Color online) (a) Electron velocity and (b) $\Gamma$ valley occupation vs electric field in InSb (green), InAs (black), AlSb (red), and $Al_{0.15}In_{0.85}Sb$ (blue) calculated with different parameters of impact ionization probability.

$\mu=525$ $cm^{2}/V$ s, while that of $Al_{0.15}In_{0.85}Sb$ is still significantly high, $\mu=9400$ $cm^{2}/V$ s (even if much smaller than in InSb).

## III. SB-BASED HETEROSTRUCTURES

Once the bulk semiconductors have been studied, the next step is to analyze the related heterostructures. AlSb and AlInSb are commonly chosen as barrier materials for InAs and InSb channels, respectively, due to their similar lattice constant. In the case of the AlSb/InAs heterojunction, an extremely large conduction band offset $(\Delta E_{c}=1.35$ $eV^{6})$ provides an excellent carrier confinement in the channel (together with very high mobility and peak electron velocity at low electric field). On the other hand, the lack of a wide band gap semiconductor with similar lattice constant to that of InSb leads to the use of $Al_{x}In_{1-x}Sb$ as barrier material. The higher $x$, the larger the conduction band discontinuity but also the lattice mismatch. Therefore a tradeoff value must be chosen for the Al content in the barrier. In our simulations we use a typical value found in the literature, $x=0.15.^{10}$ For this value of $x$ the conduction band offset is not very large

![](./images/811847478964912128_2.jpg)

FIG. 2. (Color online) Simulated heterostructure.

$(\Delta E_{c}=0.18$ $eV^{10})$ so that the sheet electron concentration in the channel is much lower than in the AlSb/InAs heterojunction. $^{8}$

In order to perform a proper comparison, the same geometry has been used for both heterojunctions (Fig. 2): a buffer of wide band gap material of 800 nm followed by a narrow band gap channel of 15 nm and a 25 nm thick wide band gap barrier material. Electrons are introduced by a $\delta$-doping of $\delta=5\times 10^{12}$ $cm^{-2}$, 10 nm far from the channel. The negative charge that appears at the semiconductor-air interface is accounted for in the simulation by means of a fixed surface charge density $\sigma$. Since the value of $\sigma$ is not known because it depends on the fabrication process, in our simulations we have used three different values, $\sigma=0$, $-2\times 10^{12}$, and $-4\times 10^{12}$ $cm^{-2}$.

The main characteristics of AlSb/InAs and $Al_{0.15}In_{0.85}Sb$/InSb heterostructures have been compared by using a 2D MC simulator self-consistently coupled with a 2D Poisson solver $^{30,31}$ adequately modified to correctly model such heterostructures. For example, a correct injection at the contacts, where the channel transport can easily become ballistic (or at least quasiballistic), is essential for an accurate simulation. In order to adequately inject (and extract) electrons into the channel, the simulated electrodes are placed vertically extending across the heterolayer. Usually, the profiles of potential assigned to these electrodes and concentration to be injected correspond to those that would appear along the heterostructure if real top electrodes were used, previously calculated from an initial simulation at equilibrium with contacts at the top. $^{32}$ However, the very large conduction band offset at the AlSb/InAs heterostructure makes difficult the obtention of the correct injection profile since the carrier interchange between the $\delta$-doping region and the channel is blocked. In such a situation, the injection conditions fix the electron distribution within the device and top-contact simulation becomes useless to obtain correct injection profiles. In order to correctly set the injection conditions, we have initially performed a self-consistent Schrödinger–Poisson simulation, $^{33}$ which indicates a complete electron confinement in the channel. This result allows restricting the injection to the channel. Once this is known, to achieve consistent injection conditions, the initial top-contact simulation used for calculating the injection profiles has been modified by using lateral contacts whose injection conditions are iteratively updated with the values obtained at the center of the

![](./images/811847478964912128_3.jpg)

FIG. 3. (Color online) (a) Conduction band and (b) concentration profiles for three values of surface charge, $\sigma$=0, $-2\times10^{12}$, and $-4\times10^{12}$ cm$^{-2}$ in the AlSb/InAs heterostructure. The position of the $\delta$-doped layer and the surface charge $\sigma$ are shown by vertical lines, while the shaded regions represent the channel.

sample until reaching convergence. The update is made ev- ery 5 ps (50 000 iterations of 0.1 fs). After around ten itera- tions the profiles converge, thus providing the correct injec- tion conditions. In the case of the $Al_{0.15}In_{0.85}Sb/InSb$ heterostructure, the conduction band offset is smaller, allow- ing carrier interchange between the barrier and the channel, and thus being possible to obtain the correct injection pro- files with the standard top-contact simulation.

Once the problems related to electron injection have been solved, MC simulations provide the conduction band and concentration profiles shown in Figs. 3 and 4 for both heterojunctions, calculated for the three values of surface charge considered. As observed, the attractive force of the $\delta$-doping layer (counteracted in part by the top surface charge) increases the electron concentration near the upper heterojunction. In AlSb/InAs, due to the total confinement of electrons in the channel, the sheet electron density in the channel, $n_{S}$, decreases as $\sigma$ becomes more negative, follow- ing the charge neutrality condition $n_{S}=\delta+\sigma$. In the case of the $Al_{0.15}In_{0.85}Sb/InSb$ heterostructure, not all the electrons are confined in the channel so that $n_{Stot}=n_{S}+n_{Sb}=\delta+\sigma$, $n_{Sb}$ being the sheet electron density of electrons in the barrier layer. Both $n_{S}$ and $n_{Sb}$ decrease when $\sigma$ is more negative, but $n_{Sb}$ is reduced to a higher extent so that the percentage of electrons in the channel increases [the dependences of $n_{S}$ and $n_{Sb}$ with $-\sigma$ are shown in the inset of Fig. 4(b)].

The mobilities of the two heterostructures have been ob- tained by first calculating the resistance of samples with in- creasing length and then determining the square resistance of the heterojunctions, $R_{\square}$ (Ref. 34) (it is just the slope of the resistance versus length plot). Then the mobility is extracted from the simple formula $R_{\square}=1/qn_{Stot}\mu$.

The mobility obtained for the AlSb/InAs heterojunction as a function of $n_{S}$ is shown in Fig. 5. Values exceeding 60 000 cm$^{2}$/V s have been obtained, much higher than bulk mobility, and increasing with $n_{S}$. This dependence is ex- pected due to the effect of degeneracy, which reduces the number of scattering mechanisms. The mobilities obtained with MC simulations are also much higher than those mea- sured experimentally. The complete confinement of electrons in the channel allows directly comparing our results with the experimental Hall measurements in Refs. 4, 7, and 35-37. In order to reduce the mobility and correctly reproduce the ex- perimental results, the effect of interface roughness in the heterojunctions has been introduced in our 2D MC simulator. There are detailed models of roughness scattering, which consider the dependence of the probability on the electron wave vector. $^{38,39}$ In our case, as first approximation we have implemented a more simple global model in which a given fraction of electron reflections at the heterojunction is treated as diffusive (instead of specular). Every time an electron reaches the surface, the diffusive or specular character of the

![](./images/811847478964912128_4.jpg)

FIG. 4. (Color online) (a) Conduction band and (b) concentration profiles for three values of surface charge, $\sigma$=0, $-2\times10^{12}$, and $-4\times10^{12}$ cm$^{-2}$ in the $Al_{0.15}In_{0.85}Sb/InSb$ heterostructure. The position of the $\delta$-doped layer and the surface charge $\sigma$ are shown by vertical lines, while the shaded regions represent the channel. The inset of (b) shows the dependencies of $n_{S}$ and $n_{Sb}$ vs $-\sigma$.

![](./images/811847478964912128_5.jpg)

FIG. 5. (Color online) Channel mobility vs $n_S$ calculated in the AlSb/InAs heterostructure compared with bulk InAs mobility and experimental results (Refs. 4, 7, and 36–38).

reflection is determined by means of a random number. Sur- face roughness has been considered in both heterojunctions of the channel. Previous works on AlSb/InAs quantum wells without $\delta$-doped layer indicate that the strongest relevance of heterojunction roughness lies on the bottom interface. $^{40}$ On the contrary, in our case, the $\delta$-doped layer increases carrier concentration near the top heterojunction, and the surface roughness scattering with this interface becomes critical. Two cases have been simulated, 1% and 2% of diffusive interactions with the surface, the latter providing a very good agreement of the MC mobility with experimental values (both in magnitude and dependence on $n_S$).

In the $Al_{0.15}In_{0.85}Sb$/InSb heterostructure, as mentioned before, part of the electrons moves through the barrier mate- rial (parasitic channel). These slower electrons degrade the value of the overall heterostructure mobility. In this case, in order to compare with experimental Hall measurements, we have calculated the value of the channel mobility by extract- ing from the simulation the current flowing just through the channel. In Fig. 6 this mobility is plotted versus $\sigma$. Surpris- ingly, for the lower values of $\sigma$ (0 and $-2\times10^{12}$ cm$^{-2}$), when the population of the $Al_{0.15}In_{0.85}Sb$ barrier is higher, the channel mobility takes values much lower than that of bulk InSb. We attribute these low values to noncompletely correct injection conditions, leading to anomalous current loops near the contacts, which affect the values of the ex- tracted resistances (mainly for the shortest samples). For the highest value of $\sigma$, when fewer electrons are present in the $Al_{0.15}In_{0.85}Sb$ barrier, these current loops are almost inexis- tent, and the calculated value of the mobility is much more reliable, around 79 000 cm$^2$/V s (higher than that of bulk material, as expected). The problems associated to current loops originated by contact injection when there is a signifi- cant electron concentration in the barrier layer are not of worrying importance since in practice, the heterolayer is de- signed to avoid that parasitic channel.

![](./images/811847478964912128_6.jpg)

FIG. 6. (Color online) Channel mobility as a function of $\sigma$ in the $Al_{0.15}In_{0.85}Sb$/InSb heterostructure compared with bulk InSb mobility. The value of $n_S$ in each case is also indicated.

![](./images/811847478964912128_7.jpg)

FIG. 7. (Color online) Concentration profile of the optimized $Al_{0.15}In_{0.85}Sb$/InAs heterostructure.

The previous results confirm that the design of the $Al_{0.15}In_{0.85}Sb$/InSb heterostructure is not adequate, leading to the presence of a significant parasitic channel caused by a too high $\delta$-doping. Therefore, this heterostructure must be optimized. In order to compare our simulations with one of the few experimental data available, $^{10}$ the $\delta$-doping plane has been moved closer to the (20 nm thick) channel, with just 5 nm of separation, and the charge density has been de- creased to a value of $\delta=1\times10^{12}$ cm$^{-2}$. Figure 7 shows the concentration profile of this heterostructure when consider- ing $\sigma=-0.1\times10^{12}$ cm$^{-2}$ (value that provides the best agree- ment with the experimental $n_S$). In this case many of the electrons (63%) are confined in the channel, where the mo- bility is around $\mu=76$ 000 cm$^2$/V s, similar to that obtained in the nonoptimized heterostructure for the highest value of $\sigma$ (Fig. 6). To correctly reproduce the experimental results of Hall mobility ($\mu_H$=23 800 cm$^2$/V s), $^{10}$ the percentage of diffusive scatterings associated to the heterojunction rough- ness must be increased to 7%, possibly indicating that the quality of the (novel) technological process used to fabricate the sample is poorer than in the case of InAs heterojunctions.

### IV. CONCLUSIONS

Bulk InAs and InSb and their respective heterostruc- tures, AlSb/InAs and $Al_{0.15}In_{0.85}Sb$/InSb, have been studied by means of MC simulations as a first step for the design and optimization on Sb-based HEMTs. Appropriate values for the simulation parameters of the involved semiconductors have been obtained. Experimental bulk mobilities have been re- produced by simulations ($\mu$=28 000 cm$^2$/V s for InAs and $\mu$=67 000 cm$^2$/V s for InSb). The transport properties of the heterostructures have been properly simulated and the

experimental mobilities reproduced by adequately adjusting the amount of roughness scattering at the heterojunction, showing that the technological quality of the InSb interface must still be much improved.

We have confirmed that the large conduction band offset of the AlSb/InAs heterostructure allows a complete confinement of carriers in the channel, thus becoming an attractive option for a new generation of ultrafast HEMTs. On the contrary, in spite of the huge mobility of InSb, electron confinement in the channel of the $Al_{0.15}In_{0.85}Sb/InSb$ heterostructure is very poor, thus hindering the possibility of being used for the fabrication of classical HEMTs. Instead, high performance metal-oxide-semiconductor-HEMTs (MOS-HEMTs) could be fabricated by depositing an adequate insulator on the top of the InSb channel.

## ACKNOWLEDGMENTS
This work has been partially supported by the Dirección General de Investigación (MEC, Spain) and FEDER through Project No. TEC2007-61259/MIC and by the Consejería de Educación of the Junta de Castilla y León (Spain) through Project No. SA019A08.

$^{1}$Y. C. Chou, M. D. Lange, B. R. Bennett, J. B. Boos, J. M. Yang, N. A. Papanicolaou, C. H. Lin, L. J. Lee, P. S. Nam, A. L. Gutierrez, D. S. Farkas, R. S. Tsai, M. Wojtowicz, T. P. Chin, and A. K. Oki, Tech. Dig. - Int. Electron Devices Meet. 2007, 617.
$^{2}$C.-Y. Chang, H.-T. Hsu, E. Y. Chang, C.-I. Kuo, S. Datta, M. Radosavljevic, Y. Miyamoto, and G.-W. Huang, IEEE Electron Device Lett. 28, 856 (2007).
$^{3}$M. Malmkvist, E. Lefebvre, M. Borg, L. Desplanque, X. Wallart, G. Dambrine, S. Bollaert, and J. Grahn, IEEE Trans. Microwave Theory Tech. 56, 2685 (2008).
$^{4}$W. Kruppa, B. Boos, B. R. Bennett, N. A. Papanicolaou, D. Park, and R. Bass, IEEE Trans. Electron Devices 54, 1193 (2007).
$^{5}$J. B. Hacker, J. Bergman, G. Nagy, G. Sullivan, C. Kadow, H.-K. Lin, A. C. Gossard, M. Rodwell, and B. Brar, IEEE MTT-S Int. Microwave Symp. Dig. 2005, 1029.
$^{6}$C. R. Bolognesi, M. W. Dvorak, and D. H. Chow, IEEE Trans. Electron Devices 46, 826 (1999).
$^{7}$J. Bergman, G. Nagy, G. Sullivan, B. Brar, C. Kadow, H.-K. Lin, A. Gossard, and M. Rodwell, Proceedings of the International Conference on Indium Phosphide and Related Materials, Santa Barbara, CA, 2003.
$^{8}$J. M. S. Orr, P. D. Buckle, M. Fearn, G. Giavaras, P. J. Wilding, C. J. Bartlett, M. T. Emeny, L. Buckle, J. H. Jefferson, and T. Ashley, J. Appl. Phys. 99, 083703 (2006).
$^{9}$G. R. Nash, M. K. Haigh, H. R. Hardaway, L. Buckle, A. D. Andreev, N. T. Gordon, S. J. Smith, M. T. Emeny, and T. Ashley, Appl. Phys. Lett. 88, 051107 (2006).
$^{10}$J. M. S. Orr, P. D. Buckle, M. Fearn, P. J. Wilding, C. J. Bartlett, M. T. Emeny, L. Buckle, and T. Ashley, Semicond. Sci. Technol. 21, 1408 (2006).
$^{11}$C. Jacoboni and P. Lugli, The Monte Carlo Method for Semiconductor Device Simulation (Springer-Verlag, New York, 1989).
$^{12}$D. C. Herbert, P. A. Childs, R. A. Abram, G. C. Crow, and M. Walmsley, IEEE Trans. Electron Devices 52, 1072 (2005).
$^{13}$O. Madelung, Semiconductors: Data Handbook (Springer, Berlin, 2004).
$^{14}$Ö. Özbaş and M. Akarsu, Turk. J. Phys. 26, 283 (2002).
$^{15}$E. Sijerčić, K. Mueller, and B. Perjčinović, Solid-State Electron. 49, 1414 (2005).
$^{16}$http://www.ioffe.ru/SVA/NSM/Semicond/
$^{17}$I. Vurgaftman, J. R. Meyer, and L. R. Ram-Mohan, J. Appl. Phys. 89, 5815 (2001).
$^{18}$http://www.research.ibm.com/DAMOCLES/html_files/numerics.html
$^{19}$M. V. Fischetti, IEEE Trans. Electron Devices 38, 634 (1991).
$^{20}$K. Brennan and K. Hess, Solid-State Electron. 27, 347 (1984).
$^{21}$Z. Dobrovolskis, K. Grigoras, and A. Krotkus, Appl. Phys. A: Solids Surf. A48, 245 (1989).
$^{22}$D. Matz, Phys. Rev. 168, 843 (1968).
$^{23}$C. Bocchi, A. Bosacchi, C. Ferrari, S. Franchi, P. Franzosi, R. Magnanini, and L. Nasi, J. Cryst. Growth 165, 8 (1996).
$^{24}$G. Theodorou and G. Tsegas, Phys. Rev. B 61, 10782 (2000).
$^{25}$E. R. Glaser, B. R. Bennett, B. V. Shanabrook, and R. Magno, Appl. Phys. Lett. 68, 3614 (1996).
$^{26}$T. González, D. Pardo, L. Varani, and L. Reggiani, Appl. Phys. Lett. 63, 84 (1993).
$^{27}$T. González, D. Pardo, L. Varani, and L. Reggiani, Appl. Phys. Lett. 63, 3040 (1993).
$^{28}$B. G. Vasallo, J. Mateos, D. Pardo, and T. González, J. Appl. Phys. 94, 4096 (2003).
$^{29}$B. G. Vasallo, J. Mateos, D. Pardo, and T. González, J. Appl. Phys. 95, 8271 (2004).
$^{30}$J. Mateos, T. González, D. Pardo, V. Hoel, and A. Cappy, Semicond. Sci. Technol. 14, 864 (1999).
$^{31}$J. Mateos, T. González, D. Pardo, V. Hoel, and A. Cappy, IEEE Trans. Electron Devices 47, 1950 (2000).
$^{32}$J. Mateos, T. González, D. Pardo, P. Tadyszak, F. Danneville, and A. Cappy, IEEE Trans. Electron Devices 44, 2128 (1997).
$^{33}$Simulator created by O. Schuler and D. Théron.
$^{34}$S. K. Ghandhi, VLSI Fabrication Principles, Silicon and Gallium Arsenide (Wiley, New York, 1994).
$^{35}$B. Brar, G. Nagy, J. Bergman, G. Sullivan, P. Rowell, H. K. Lin, M. Dahlstrom, C. Kadow, and M. Rodwell, Proceedings of the IEEE Lester Eastman Conference on High Performance Devices, Newark, DE, 6-8 August 2002.
$^{36}$R. Tsai, M. Barsky, J. B. Boos, B. R. Bennett, J. Lee, N. A. Papanicolaou, R. Magno, C. Namba, P. H. Liu, D. Park, R. Grundbacher, and A. Gutiérrez, Proceedings of the IEEE Gallium Arsenide Integrated Circuit (GaAs IC) Symposium, 2003.
$^{37}$B. R. Bennett, R. Magno, J. B. Boos, W. Kruppa, and M. G. Ancona, Solid-State Electron. 49, 1875 (2005).
$^{38}$C. R. Bolognesi, H. Kroemer, and J. H. English, Appl. Phys. Lett. 61, 213 (1992).
$^{39}$A. Gold, Phys. Rev. B 35, 723 (1987).
$^{40}$G. Tuttle, H. Kroemer, and J. H. English, J. Appl. Phys. 67, 3032 (1990).

Journal of Applied Physics is copyrighted by the American Institute of Physics (AIP).
Redistribution of journal material is subject to the AIP online journal license and/or AIP copyright. For more information, see http://ojps.aip.org/japo/japcr/jsp