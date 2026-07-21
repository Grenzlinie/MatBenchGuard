![](./images/812403711962775553_1.jpg)

Surface Science 371 (1997) 445-454

![](./images/812403711962775553_2.jpg)

# Island structure evolution during chemical vapor deposition

D.P. Adams *, T.M. Mayer, E. Chason, B.K. Kellerman, B.S. Swartzentruber

Sandia National Laboratories, P.O. Box 5800, Albuquerque, NM 87185-1413, USA

Received 25 March 1996; accepted for publication 17 July 1996

## Abstract

Scanning tunneling microscopy (STM) and Monte Carlo simulations are used to investigate the development of island structure during low-pressure, chemical vapor deposition (CVD) of metal onto clean Si(100) substrates. For Fe growth via $Fe(CO)_5$ pyrolysis, STM shows that precursor molecules initially decompose at Si dangling bond sites. The nucleation rate is strongly dependent on substrate temperature with rapid decomposition at $200^\circ$C and zero reaction at room temperature (for exposures as large as 100 L). At later stages STM shows that island structure is dominated by differential reaction probabilities. A small barrier to decomposition on Fe compared with Si leads to large clusters and a nonlinear growth rate. This autocatalytic growth behavior is also reflected in the measured island size distributions. Kinetic Monte Carlo simulations confirm that chemical reaction kinetics influence Fe film growth, while precursor molecule diffusion does not play a major role in the evolution of island structure. Using simulations, we also demonstrate how CVD film structure can differ from that developed during solid-source molecular beam epitaxy.

**Keywords**: Chemical vapor deposition; Growth; Iron; Nucleation; Scanning tunneling microscopy; Silicon

## 1. Introduction

Chemical vapor deposition (CVD) is currently used for the construction of a number of components and devices which require selective-area-growth or conformal deposition [1,2]. This includes metallization for integrated circuits, mechanical coatings and diode laser arrays. Yet, despite its importance for various commercial applications the development of film microstructure and morphology during CVD is not well understood.

In the past, most atomic level studies of thin film growth kinetics and structure have focused on a different, yet simpler technique - solid-source molecular beam epitaxy (MBE) [3-5]. In particular, a great deal is now known about low-temperature MBE, wherein the system is far-from-equilibrium. For low temperature growth it is well established that monomers often diffuse across a surface, until they: (1) find existing islands and become incorporated at the edge of a cluster; (2) find other diffusing monomers and nucleate a new island; or (3) become trapped at a defect. Hence, the diffusion rate and the deposition rate largely determine the distribution of island sizes [6]. In practice, the morphology and location of islands are studied in order to determine the details of film growth kinetics. Using this procedure the roles of anisotropic diffusion, anisotropic sticking and step-edge barriers have been identified for MBE growth [4,7].

It is not surprising that CVD has received comparatively less attention considering the complex

* Corresponding author. Fax: +1 505 844 5470.

0039-6028/97/$17.00 Copyright © 1997 Elsevier Science B.V. All rights reserved
PII S0039-6028(96)01005-9

nature of this growth technique. In many cases CVD is influenced by a number of kinetic processes other than adatom diffusion. This may include transport of large molecules to the substrate or film, adsorption, surface-chemical reactions as well as gas-phase reactions [2,8]. In addition, CVD is often complicated by numerous chemical species. In some systems precursor molecules, fragments of decomposition reactions and other adsorbates, ini- tially introduced as part of the carrier gas, attach to a film surface. Recently, scanning tunneling microscopy (STM) has been used to study CVD by probing kinetics on an atom-by-atom basis [9-16]. For example, several groups have success- fully monitored the configurations of adsorbed precursor species [15], the nucleation sites and the effects of reaction on changing local surface structure [16]. STM has also been useful for initiating chemical reactions locally on the surface using low energy electrons [17-23]. Nevertheless, despite much progress very few studies have sys- tematically analyzed the evolution of CVD island structure.

The goal of the present work is to determine how various chemical kinetic processes affect film structure during CVD. In particular, we are inter- ested in the development of island structure during the early stages of heterolayer growth. We expect that film structure should, in this case, be influ- enced by the competition between various kinetic processes. During heterolayer CVD nucleation of clusters can occur by one of many processes and may be site dependent. Growth is likely influenced by different reaction rates at substrate lattice sites versus existing clusters.

In this paper we describe results from experi- ments and simulations involving thermal decompo- sition (pyrolysis) of $Fe(CO)_{5}$ on clean $Si(100)$ substrates. We choose this system for several reasons. First, carbonyl precursor gases are useful for depositing metal because of the low decomposi- tion temperature and the high vapor pressures at room temperatures (e.g. 27 Torr for $FeCO_{5}$ ). Furthermore, the pyrolysis of $Fe(CO)_{5}$ on Si serves as an excellent model CVD system, for many studies have addressed $Fe(CO)_{5}$ reaction chemistry and Fe layers have been grown by a variety of techniques [24-28]. Of importance to this work previous thermal CVD experiments demonstrate that crystalline Fe films can be grown on Si without significant impurity incorporation [29]. We limit our investigation to growth at $\sim 100-200^{\circ} C$ , because negligible amounts of C and O are incor- porated into Fe films at these temperatures. A few details of Fe cluster nucleation and growth are discussed in a previous publication [24]. In that work, we identify the nucleation sites and find evidence for autocatalytic growth. In the present study, we include a more complete analysis of structure evolution with discussion of measured island size distributions. Also, results from numer- ous kinetic Monte Carlo simulations are presented. These are used to aid in understanding the $Fe(CO)_{5}$ system and should be useful in studies of more complicated CVD processes. Simulations address the roles of various chemical kinetic processes and include the effects of changing temperature.

## 2. Experiment
All experiments are conducted within an ion- pumped, ultrahigh vacuum system (base pres- sures $=6 ×10^{-11}$ Torr). Virginia Semiconductor, n-type (P), $Si(100)$ samples are first heated to1250°C in vacuo and scanned using a variable-temperature scanning tunneling microscope [30] to ensure a clean, well-ordered starting surface. Substrates are then equilibrated for one hour at a fixed temperature between 30 and $215^{\circ} C$ . Temperatures are calibrated in a separate experi- ment by placing a W/WRe thermocouple junction into a 0.008 in. diameter hole drilled in the side of a Si sample.

For CVD a Pyrex bottle containing freshly- distilled $Fe(CO)_{5}$ is loaded onto the vacuum system. The volume between the source and a UHV leak valve is then evacuated and the carbonyl is given an additional freeze pump to remove impurities. After warming to room temperature, a well-controlled partial pressure of $Fe(CO)_{5}$ is intro duced into the vacuum system for CVD growth. One of two different pressures is selected: $1 ×10^{-8}$

or $5 \times 10^{-8}$ Torr, as measured using an uncalibrated ion gauge. Note, the liquid carbonyl is covered at all times to avoid photolytic decomposition to $\mathrm{Fe}_{2}(\mathrm{CO})_{9}$ and is kept cold in liquid nitrogen when not in use.

Several Fe films are also grown onto clean Si(100) substrates by physical vapor deposition (PVD) in order to better understand CVD growth. PVD involves Fe evaporation from a hot filament at a rate of $0.1 \AA \mathrm{min}^{-1}$. This rate was chosen in order to closely match the CVD growth rate at $165^{\circ} \mathrm{C}$ and $1 \times 10^{-8}$ Torr, $\sim 0.1$ monolayer (ML)/100 s. We use similar deposition rates and the same growth temperatures in order to eliminate the modification to island structure that would arise from different Fe adatom diffusion lengths (assuming that for CVD the mobility of Fe atoms is not enhanced by the decomposition event). Direct comparisons of CVD and PVD film structure therefore reveal information about chemical kinetic processes.

Island structure is probed by STM after quenching to room temperature. We deem images suitable for analysis if Si dimer rows and steps are also clearly resolved. This helps to eliminate images which show anomalous structural features, thus improving the accuracy in measuring cluster sizes. Individual clusters are traced onto a transparent sheet by hand and scanned for analysis. Note, all images used for measurement are taken using a sample bias of $-2.5 \mathrm{~V}$ and a current of $0.15 \mathrm{nA}$. No change in the size and shape of islands is detected when using different biases, over a range from -3.0 to $+3.0 \mathrm{~V}$.

Kinetic Monte Carlo simulations [31] are also used to investigate CVD kinetics and island structure evolution. Simulations involve a $256 \times 256$ square lattice starting surface. Since steps have little effect on nucleation for Fe CVD [24], starting surfaces used for simulation are a single terrace. Several activation energies associated with the $\mathrm{Fe}(\mathrm{CO})_{5} / \mathrm{Si}$ system are included in order to accurately simulate Fe CVD. We set the activation energy for pentacarbonyl decomposition on Fe equal to $0.14 \mathrm{eV}$ [32], unless mentioned otherwise. Also, the barrier to $\mathrm{Fe}(\mathrm{CO})_{5}$ desorption from the $\mathrm{Si}(100)$ surface is $0.35 \mathrm{eV}$ [33].

## 3. Results and discussion

### 3.1. Nucleation and growth of islands during Fe CVD

Typical STM images of submonolayer Fe films grown by CVD are shown in Figs. 1c and 1d. In these images the clusters formed as a result of a 0.5 and a $5.0 \mathrm{~L} \mathrm{Fe}(\mathrm{CO})_{5}$ exposure can be seen as bright features or "bumps" on the surface. For all biases tested clusters appear rounded and compact; however, individual atoms within clusters cannot be resolved. From STM we also find that deposition of small amounts of Fe does not have a dramatic effect on the Si surface structure; neighboring areas of uncovered Si maintain a $(2 \times 1)$ reconstruction. Si dimer rows, in addition to steps, are still resolvable at all coverages studied.

Based on our work here and previous studies [29,32], the clusters shown by STM are Fe and not contamination. In this work, X-ray photoelectron spectroscopy does not show any evidence

![](./images/812403711962775553_3.jpg)

Fig. 1. $310 \times 310 \AA^{2}$ STM images of Fe layers grown onto clean $\mathrm{Si}(100)$ by physical vapor deposition ((a) and (b)) and chemical vapor deposition ((c) and (d)). $\mathrm{Fe}(\mathrm{CO})_{5}$ exposures are $0.5 \mathrm{~L}(\mathrm{c})$ and $5.0 \mathrm{~L}(\mathrm{~d})$. $T_{\text {growth }}=215^{\circ} \mathrm{C}$.

of C or O contamination during CVD. This is found for all growth temperatures. Also, Fe cover- ages measured using heavy ion backscattering spectrometry (HIBS) [34] after growth are in excellent agreement with STM. Typically film cov- erages measured from STM images are within a factor of three to HIBS measurements made over much larger areas, $\sim 4 ~mm^{2}$. Furthermore, addi tional observations made using STM indicate that the clusters are not weakly-bound fragments of the decomposition reaction, including CO. Specifically, we do not find a change in the size, shape or location of clusters during long, post-growth anneals at the deposition temperature. Changes in tip-substrate bias also do not lead to desorption or motion of individual clusters. We understand the absence of various $Fe(CO)_{x}$ species and $CO$ as being due to significant desorption at the growth temperature. This is consistent with previous work that indicates CO has a very low sticking coefficient on clean $Si$ [35]. $Fe(CO)_{5}$ is known to desorb from $Si$ and $Fe$ substrates at temperatures of $-130^{\circ} C$ [33] and $\sim 40-50^{\circ} C$ [36], respectively.

Knowing that clean Fe films are deposited during pyrolysis, we find several trends in island structure beginning at the earliest stages of depos- ition. First, analysis of CVD films reveals that Fe(CO), precursor molecules do not preferentially decompose at Si step sites. Instead, clusters develop with an equal or greater probability on Si terraces, as shown in Fig. Ic. Most likely nucleation occurs at dangling bond sites. These observations are interesting, for they conflict with traditional expla- nations of chemical reactivity at defects. Defects such as steps are often assumed to be sites of strong bonding and enhanced chemical reactivity. Many systems, particularly catalytic reactions on metal surfaces, show evidence for high reaction rates on rough surfaces [37].

In addition, the rate of nucleation, or $Fe(CO)_{5}$  decomposition onto $Si$ , is sensitive to temperature, consistent with a thermal CVD process. This rate is directly measured by STM using images such as those in Figs. Ic and 1d. In Fig.2 the cluster density is plotted versus exposure for four different growth temperatures, covering a range of $\sim 200^{\circ} C$ . This plot shows that small exposures $(\sim 2 ~L)$ result in substantial nucleation and growth onto existing clusters at higher temperatures. At temperatures $\sim 100^{\circ} C$ , very few nuclei form for a $2 ~L$ exposure. However, no reaction is observed at $30^{\circ} C$ even after lengthy exposures $(\sim 100 ~L)$ .

![](./images/812403711962775553_4.jpg)

Fig. 2. Plot of average cluster density versus exposure for four different temperatures. Zero growth is found at $30^{\circ} C$ for large exposures while rapid nucleation occurs at $215^{\circ} C$ , characteristic of a thermal CVD process.

STM also indicates that Fe cluster growth during CVD is unlike that for PVD. A comparison of island structures, shown in Fig. 1, indicates thatrelatively large clusters develop during $Fe(CO)_{5}$  pyrolysis (Figs. Ic and 1d) compared with PVD(Figs. la and 1b). These results are summarized for all samples in Fig. 3. Note, we examine islandgrowth by comparing films of identical coverage; this removes the temperature dependence for nucle-

![](./images/812403711962775553_5.jpg)

Fig. 3. Plot of average cluster size (expressed in $\AA^{2}$ ) versus coverage for CVD and PVD growth. CVD is characterized by large cluster sizes compared with PVD growth. Comparisons are made for equal areal coverages. Note, each data point is taken from a separate growth experiment. The lines are guides to the eye.

ation during CVD, indicated in Fig. 2. Also, evi- dence of large cluster growth during CVD is reflected in the distributions of cluster sizes shown in Fig. 4. The tails of distributions extend to large sizes for increased $Fe(CO)_5$ exposure [38].

Based on the STM data we explain the differ- ences in island structure during Fe CVD compared with PVD as being due to chemical kinetic pro- cesses. Specifically, the dominant kinetic process affecting Fe island structure during CVD is prefe- rential decomposition (i.e. growth) at existing clus- ters. Carbonyl molecules arriving on top or at the edge of an existing island, either by direct impinge- ment or possibly surface diffusion, have a higher reaction probability than precursor molecules interacting with Si substrate sites. Additional evi- dence of preferred growth can be found in STM measurements of the barrier to decomposition on Si. Using the lowest coverage data in Fig. 2, we extract an activation energy for decomposition onto Si of 0.40 eV. This is $\sim 2.5$ times larger than that previously measured for reaction on Fe.

An explanation based on site-specific chemical reactions is consistent with observations made during the growth of thicker Fe films. Previous work involving laser-assisted deposition as well as pyrolysis on Si indicates that Fe CVD is autocata- lytic [32,39,40]. In these works the film growth rate is shown to increase over time. A nonlinear growth rate is explained in terms of an incubation period, during which nuclei are assumed to form on the substrate, followed by rapid, linear growth. In our work STM observations of Fe CVD growth also show this behavior. Films grown to thick- nesses of a few ML exhibit rapid cluster growth followed by coalescence. Fig. 5 shows a $310 \times$  $310 \AA^{2}$ image of a film surface after 3 ML of Fe growth. From STM we see that the film has large "grains" and a rough surface morphology.

In passing, we note that two different atomistic processes can be used to explain the difference in activation energy for thermal decomposition on Fe versus Si. One explanation of preferential growth onto clusters involves an increased residence time [41] for carbonyl molecules adsorbed to Fe com- pared to bare Si surfaces. This model is consistent with two sets of experiments which show that $Fe(CO)_5$ desorbs at a higher temperature from Fe than from Si [33,36]. Alternatively, the difference in dissociation reaction rates could be due to chemisorption whereby ligand exchange is more favorable at metal sites. In this description the "sticking coefficients" for adsorption onto Fe and Si are similar.

In general, the measured cluster size distribu- tions for Fe CVD also reflect the autocatalytic nature of this system and show several trends. As mentioned previously the tails of distributions extend to large sizes for increased carbonyl expo- sure. This is found for different temperatures and growth pressures and is readily explained by prefe- rential decomposition kinetics. In addition, nearly all distributions are decreasing functions of size. No well-defined peak in the distribution is found.

![](./images/812403711962775553_6.jpg)

Fig. 4. Distributions of island sizes formed during Fe CVD growth at $165^{\circ} C$. Plots show the number of clusters, $n(a, \theta)$, of size $a$, for different coverages, $\theta$. Bin size is $80 \AA^{2}$.

![](./images/812403711962775553_7.jpg)

Fig. 5. $310 \times 310 \AA^{2}$ STM image of a 3 ML thick Fe film. Islands have coalesced into a continuous film having a rough surface morphology and a variety of grain sizes.

This results from continued nucleation and indi- cates a small critical nucleus size. We point out however that a few questions remain concerning scatter in the data. Specifically, a few higher- coverage distributions show evidence for a "peak" away from the origin, located in the second bin. Presently, we expect that the difficulty in measuring small cluster sizes at higher coverages may affect the accuracy of this data set, possibly giving rise to a false peak. Nevertheless, in Section 3.2 we address the likelihood that other processes (e.g. second-order nucleation) affect Fe CVD structure.

### 3.2. Monte Carlo simulations of CVD growth and comparison to the $Fe(CO)_5$/Si system

Kinetic Monte Carlo simulations have been completed in order to gain a better understanding of $Fe(CO)_5$ pyrolysis and to shed light on island structure evolution for more complicated CVD systems. In the simulations we allow for a certain number of kinetic processes as described below. However, we do not incorporate metal atom diffu- sion. For all simulations one atom forms a stable cluster, and metal atoms are not allowed to detach from clusters. In general, we consider only chemical kinetic processes.

The first set of simulations are used to test the roles of differential reaction probabilities and desorption. Typical results are shown in Fig. 6, where we compare growth by PVD (Figs. 6a and 6b) with CVD (Figs. 6c and 6d) for the case of no molecular diffusion. For these simulations we include the activation barriers to decomposition on Si and Fe measured from experiments, 0.4 and 0.14 eV, and assume a constant sticking coefficient of $10^{-1}$ for all temperatures. In general, these particular simulations match closely to experiment; CVD results in larger islands compared with that formed during PVD. This difference in average island size becomes more apparent at higher cover- ages. Also, the average size of islands is similar to that of experiment. Although individual atoms within clusters cannot be identified, we estimate from STM images that clusters formed during PVD consist of ~1-4 atoms whereas CVD films of equal coverage (~0.25 ML) have ~1-20 atoms. These approximate sizes are found for simulations as shown in Figs. 6b and 6d. Other features of these simulations that are similar to experiment include the general shape of cluster size distribu- tions. As shown in Fig. 7, distributions are decreas- ing functions of size [42]. This results because a larger number of small islands continue to nucleate

![](./images/812403711962775553_8.jpg)

Fig. 6. Simulated PVD ((a) and (b)) and CVD ((c)-(f)) island structures at two different coverages. Films displayed in (c) and (d) result from desorption and site-dependent chemical reac- tions. The island structure shown in (e) and (f) is also affected by molecular diffusion, $E_{diff }=0.07 eV$.

![](./images/812403711962775553_9.jpg)

Fig. 7. Results from Monte Carlo simulations. Distributions of cluster sizes for CVD growth affected by site-specific chemical reactivity and desorption (no molecular diffusion).

while existing islands grow. If continuous nucle-
ation of new islands did not occur then the small
islands would disappear due to coarsening and a
peak in this distribution would be observed. Also,
as in experiments the tails of distributions extend
to larger sizes with increased exposure - a result
of preferential decomposition at existing clusters.
In summary, the many similarities between experi-
ment and simulations confirm that site-specific
chemical reactions and desorption affect Fe island
structure.

Although these previous simulations appear to
match the experimental data well we also consider
the effects of changing temperature. First, we study
the effects of temperature for growth involving
only adsorption and site-specific chemical reac-
tions. Using the parameters characteristic of
Fe(CO)₅ pyrolysis on Si, additional simulations
predict that the island structure is weakly depen-
dent on substrate temperature. The general shape
of the predicted cluster size distribution does not
change with temperature. This is consistent with
experiments. On the other hand, average cluster
size is predicted to change slightly as shown in
Fig. 8a. Although the experimental average cluster
size data does not show a temperature dependence,
we expect that this can readily be explained by the
limited range of temperatures used in this study.
In Fig. 3 we show data that covers only a 50°C
change. According to simulations this should result
in average cluster sizes that differ by ~1 atom or
less. This is most likely undetectable for the STM
experiments due to the relatively large error associ-
ated with measuring substrate temperature and
island size.

We point out that the effects of temperature on
structure are nevertheless interesting, considering
the more familiar trends found for MBE growth.
To reiterate, many MBE systems are characterized
by enhanced diffusion lengths and large clusters at
higher temperatures. From simulations of CVD
growth dominated by desorption and differential
reaction probabilities, we find larger clusters can
develop with decreasing substrate temperature.
Essentially this trend is due to changing reaction
rates. As the temperature is lowered the rate of
reaction on the substrate decreases faster than for
growth on existing metal clusters. This structure-
temperature relationship is similar to that found
for MBE systems affected by site-exchange pro-
cesses [43].

![](./images/812403711962775553_10.jpg)

Fig. 8. Results from Monte Carlo simulations. Plots of average
cluster size versus coverage for CVD growth. (a) Results from
simulations allowing desorption and site-dependent chemical
reactions but no molecular diffusion. (b) Results from simula-
tions allowing desorption, site-dependent chemical reactions
and precursor molecule diffusion. These figures demonstrate
that larger clusters develop at lower substrate temperatures.
Also plotted in these figures is the average cluster size for PVD
growth (○).

In addition to studying the effects of temperature
on structure, we have also considered the effects
of several transport processes that could influence
Fe CVD growth. In all simulations discussed pre-
viously in this paper, precursor molecules either
react upon adsorption or return promptly to the
gas phase. In principle though, molecules could
physisorb and diffuse across the surface before
reacting. Certainly it is conceivable that Fe(CO)₅
precursor molecules would remain on a Si surface

long enough to affect structure considering the desorption activation energy (0.35 eV).

A potential effect of precursor molecule diffusion involves collision and mutual decomposition of two mobile, physisorbed species to form a stable nucleus. We first consider this mechanism, because similar processes are active in other growth sys- tems, e.g. MBE. Also, if present during CVD, this second-order process would dramatically change the statistical characteristics of the island ensemble; second-order nucleation would lead to a well- defined, peaked size distribution. However, based on calculated growth rates we dismiss this as a possible mechanism affecting Fe CVD. For a sce- nario in which two molecules must collide on the surface to form a stable nucleus, growth rates are estimated from the steady-state coverage of adsorbed $Fe(CO)_5$ molecules. This coverage is cal- culated to be $7 \times 10^{4} cm^{-2}$ or $1 \times 10^{-10}$ ML at $165^{\circ} C$. For nucleation occurring by a second-order kinetic process, the decomposition rate is estimated to be $2.5 \times 10^{-5} cm^{-2} ~s^{-1}$ (assuming a value of $E_{diff }=0.2 E_{des }$ or $0.07 eV$ ). This predicted rate of growth is much less than that measured in experiments.

On the other hand, it is conceivable that precur- sor molecule diffusion is playing a different role during Fe layer growth. Physisorbed, weakly- bound molecules could potentially "carry" metal atoms across a surface, thus providing a pathway for decomposition at favorable sites. This mech- anism is more plausible than the previously discussed second-order kinetic process, since nucleation does not depend on the likelihood that two molecules will collide. Simulations verify that molecular diffusion can, in principle, have a sig- nificant combinative effect on structure, provided that desorption and site-specific chemical reactions also affect growth. This is demonstrated in Figs.6e and 6f using an arbitrary value for the diffusion activation energy equal to $0.2 E_{des }$ , or $0.07 eV$ , and the same reaction probabilities for $Fe(CO)_{5}$ as before. In general, the addition of molecular diffu- sion leads to much larger cluster sizes. This is also clearly indicated for different temperatures as shown in Fig. 8.

However, comparing the simulated island struc- tures to the STM data we conclude that molecular diffusion is not playing a dominant role during Fe CVD. Several arguments can be made against this kinetic process being significant. First, as was pointed out earlier the average size of simulated clusters closely matches that of experiment when considering only differential reaction probabilities and adsorption. In contrast, the predicted island structure resulting from the addition of significant molecular diffusion is very different. Islands affected by molecular diffusion are predicted to be on the order of hundreds of atoms in size, while STM indicates that Fe clusters actually contain~1-20 atoms [44]. Also, it is apparent from simulations that the addition of significant molecu- lar diffusion leads to a strong temperature depen- dence. As shown in Fig. $8 ~b$ a $50^{\circ} C$ change in growth temperature results in simulated cluster sizes that differ by hundreds of atoms. This would easily be detected by STM. Furthermore, it is difficult to envision molecular diffusion being important considering the relatively small spacing between Fe islands shown by STM. As indicated in Fig. 1 clusters are typically spaced by tens of angströms for $0.2 ML$ thick films. Simulations show that islands would be spaced by hundreds- thousands of angstroms if precursor molecule diffusion were significant.

Finally, we point out that simulations provide additional information about the shape of cluster size distributions. In general, these show the addi- tion of precursor molecule diffusion does not give rise to a well-defined, peaked size distribution for systems affected by first-order nucleation processes. This is tested for a range of different activation barriers for reaction and for molecular diffusion. Instead, we find a decreasing island size distribu- tion for all scenarios studied here by simulations. Therefore, we conclude that if a well-defined peak develops during Fe CVD, this can only be explained by kinetic processes not considered in this discussion. If real, this may potentially be due to processes such as site-poisoning which tie up reactive substrate sites during deposition [45].

## 4. Conclusions

In summary, STM provides several details con- cerning both the nucleation and growth of clusters

during Fe CVD. First, we find that nucleation does not occur preferentially at step sites as for other CVD systems. Instead, clusters readily form on (100) terraces, most likely at dangling bond sites. Also, STM indicates that Fe island structure is dominated by chemical reaction kinetics. Specifically, CVD films are affected by preferential dissociation of precursor molecules on existing Fe clusters (an autocatalytic effect). This conclusion is made from comparisons of CVD and PVD films grown at identical temperatures and similar metal atom deposition rates. Evidence for autocatalytic growth is also found in measured cluster size distributions. In general, distributions are decreasing functions of size with tails extending to larger sizes for increased exposure. Kinetic Monte Carlo simulations of Fe CVD closely match experiments when considering only adsorption and differential reaction probabilities.

Simulations also demonstrate several interesting trends in island structure evolution that may be of interest to future studies of other CVD systems. Most importantly, we find structure-temperature relationships that differ from low temperature MBE growth. Specifically, CVD affected by desorption and site-dependent chemical reactions develops larger average cluster sizes at lower substrate temperatures. This results because as the temperature is lowered the rate of reaction on the substrate surface decreases faster than for decomposition onto existing clusters. Also, we show that the combination of molecular diffusion with these two other chemical kinetic processes can lead to more dramatic differences in island structure for a given change in temperature. For systems having mobile, physisorbed precursor molecules, islands can grow even larger at lower temperatures, because the desorption rate decreases faster than the diffusion rate. In other words, a precursor molecule has a greater chance of diffusing to, and preferentially reacting with, existing clusters at lower temperatures, because this weakly-bound species is more likely to remain on the surface for longer periods of time.

## Acknowledgements

The authors greatly appreciate discussions with D. Chrzan and G.S. Bales. We also thank J. Banks and J.A. Knapp for the HIBS measurements. This work was supported by the US Department of Energy under contract DE-AC04-94AL85000.

## References

[1] W.L. Gladfelter, Chem. Mater. 5 (1993) 1372.
[2] J.R. Creighton and J.E. Parmeter, Crit. Rev. Solid State Mater. Sci. 18 (1993) 175.
[3] J.A. Stroscio and D.T. Pierce, Phys. Rev. B 49 (1994) 8522.
[4] M.D. Johnson, C. Orme, A.W. Hunt, D. Graff, J. Sudijono, L.M. Sander and B.G. Orr, Phys. Rev. Lett. 72 (1994) 116.
[5] D.D. Chambliss and K.E. Johnson, Phys. Rev. B 50 (1994) 5012.
[6] Y.W. Mo, J. Kleiner, M.B. Webb and M.G. Lagally, Phys. Rev. Lett. 66 (1991) 1998.
[7] R.Q. Hwang, J. Schröder, C. Günther and R.J. Behm, Phys. Rev. Lett. 67 (1991) 3279.
[8] G.S. Bales, A.C. Redfield and A. Zangwill, Phys. Rev. Lett. 62 (1989) 776.
[9] J.J. Boland, Phys. Rev. Lett. 67 (1991) 1539; Surf. Sci. 261 (1992) 17; Phys. Rev. B 44 (1991) 1383.
[10] M.J. Bronikowski, Y.J. Wang, M.T. Mcellistrem and R.J. Hamers, Surf. Sci. 298 (1993) 50.
[11] D.S. Lin, E.S. Hirschorn, T.C. Chiang, R. Tsu, D. Lubben and J.E. Greene, Phys. Rev. B 45 (1992) 3494.
[12] L. Kipp, R.D. Bringans, D.K. Biegelsen, L.-E. Swartz and R.F. Hicks, Phys. Rev. B 5448 (1994) 50.
[13] Y. Wang, M.J. Bronikowski and R.J. Hamers, Surf. Sci. 311 (1994) 64.
[14] J. Winterlin and Ph. Avouris, J. Chem. Phys. 100 (1994) 687.
[15] Y.W. Mo, J. Vac. Sci. Technol. B 12 (1994) 2231.
[16] Y. Wang, M.J. Bronikowski and R.J. Hamers, J. Phys. Chem. 98 (1994) 5966.
[17] B.J. McIntyre, M. Salmeron and G.A. Somarjai, Science 265 (1994) 1415.
[18] G. Dujardin, R.E. Walkup and Ph. Avouris, Science 255 (1992) 1232.
[19] F. Bozso and Ph. Avouris, Mater. Res. Soc. Symp. Proc. 158 (1990) 201.
[20] R.M. Silver, E.E. Ehrichs and A.L. de Lozanne, Appl. Phys. Lett. 51 (1987) 247.
[21] M.A. McCord, D.P. Kern and T.H.P. Chang, J. Vac. Sci. Technol. B 6 (1988) 1877.
[22] R.S. Becker, G.S. Higashi, Y.J. Chabal and A.J. Becker, Phys. Rev. Lett. 65 1917 (1990).
[23] T.-C. Shen, C. Wang, G.C. Abeln, J.R. Tucker, J.W. Lyding, Ph. Avouris and R.E. Walkup, Science 268 (1995) 1590.
[24] D.P. Adams, L.L. Tedder, T.M. Mayer, B.S. Swartzentruber and E. Chason, Phys. Rev. Lett. 74 (1995) 5088.
[25] J.R. Swanson, C.M. Friend and Y.J. Chabal, J. Chem. Phys. 87 (1987) 5028.

[26] C.E. Bartosch, J.A. Stroscio and W. Ho, in: Proceedings of the Symposium on Beam-Induced Chemical Processes (Materials Research Society, Pittsburgh, 1986) Vol. 67; N.S. Gluck, Z. Ying, C.E. Bartosch and W. Ho, J. Chem. Phys. 86 (1987) 4957.

[27] R.R. Kunz, T.E. Allen and T.M. Mayer, J. Vac. Sci. Technol. B 5 (1987) 1427.

[28] M.A. McCord and D.D. Awschalom, Appl. Phys. Lett. 57 (1990) 2153.

[29] J.S. Foord and R.B. Jackman, Chem. Phys. Lett. 112 (1984) 190.

[30] B.S. Swartzentruber, Y.W. Mo, M.B. Webb and M.G. Lagally, J. Vac. Sci. Technol. A 8 (1990) 210.

[31] E. Chason and B.W. Dodson, J. Vac. Sci. Technol. A 9 (1991) 1545.

[32] R.R. Kunz and T.M. Mayer, J. Vac. Sci. Technol. B 6 (1988) 1557.

[33] J.S. Foord and R.B. Jackman, Surf. Sci. 171 (1986) 197.

[34] J.A. Knapp and B.L. Doyle, Nucl. Instrum. Methods Phys. Res. B 45 (1990) 143.

[35] J.P. Chamberlain, J.L. Clemons, A.J. Pounds and H.P. Gillis, Surf. Sci. 301 (1994) 105.

[36] J.S. Foord and R.B. Jackman, Surf. Sci. 209 (1989) 151.

[37] G.A. Somorjai, Surf. Sci. 300 (1994) 849.

[38] For the distributions bin size is set in $\mathring{\text{A}}^2$ according to the smallest average cluster size probed by STM. As shown in Fig. 3 this is on the order of $80\ \mathring{\text{A}}^2$ for both CVD and PVD experiments.

[39] B.K. Kellerman, E. Chason, D.P. Adams and T.M. Mayer, to be published.

[40] D.J. Ehrlich, R.M. Osgood, Jr. and T.F. Deutsch, J. Vac. Sci. Technol. 21 (1982) 23.

[41] J.A. Venables, G.D.T. Spiller and M. Hanbucken, Rep. Prog. Phys. 47 (1984) 399, and references therein.

[42] In this work we have not attempted to fit the shape of STM-measured size distributions. Note, the trends in distribution shape develop independent of decomposition activation energy, even for $E_{\text{act}}(\text{Si})/E_{\text{act}}(\text{Fe})$ as high as 50.

[43] J.A. Meyer and R.J. Behm, Surf. Sci. 322 (1995) L275.

[44] We emphasize that the barrier to diffusion (0.07 eV) is chosen arbitrarily for simulations in order to test for large diffusion effects. Certainly a larger barrier would lead to island structures that more closely approximate the STM data.

[45] D.P. Adams, T.M. Mayer and B.S. Swartzentruber, Appl. Phys. Lett. 68 (1996) 2210.