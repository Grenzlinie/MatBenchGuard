# On the contribution of the electronuclear reaction to the photonuclear production of Mo-99 and other radioisotopes

A. Tsechanski$^{\rm a}$, D. Fedorchenko$^{\rm b,*}$, V. Starovoitova$^{\rm c}$

$^{\rm a}$ Ben-Gurion University of the Negev, Department of Nuclear Engineering, P.O. Box 653, Beer-Sheva, 84105, Israel
$^{\rm b}$ National Science Center Kharkov Institute of Physics and Technology, 1 Akademicheskaya St, Kharkov, 61108, Ukraine
$^{\rm c}$ Division of Physical and Chemical Sciences, Department of Nuclear Sciences and Applications International Atomic Energy Agency, PO Box 100, 1400, Vienna, Austria

---

## ARTICLE INFO

**Keywords:**
Electron accelerator
Electronuclear reaction
Photonuclear reaction
Mo-99 production
Monte Carlo simulation

---

## ABSTRACT

We used Monte Carlo simulations to estimate contribution of the electronuclear (e$^-$,e$'$n) reaction to the one-stage approach photonuclear production of $^{99}$Mo. Two types of targets were considered, and it was shown that in case of a thick (2 cm) target, electronuclear yield is two orders of magnitude lower than the photonuclear one. However, in case of a thin target electronuclear yield becomes comparable to the photonuclear or even exceeds it. For a 1 mm thick $^{100}$Mo target contribution of the $^{99}$Mo yield is about 20%, while for a 0.1 mm thick target this contribution exceeds 70%. We have shown that photonuclear yields of the radioisotopes produced in thin targets could be greatly underestimated if electronuclear reactions are not taken into consideration.

---

### 1. Introduction

The metastable nuclear isomer $^{99{\rm m}}$Tc is by far the most widely used radioisotope (RI) in nuclear medicine (NM). Its low energy isomeric decay $\gamma$-quanta (I$_\gamma$ = 140.5 keV, T$_{1/2}$ = 6.0 h) are ideally suited for the high-quality SPECT imaging in conjunction with low radiation doses to patients. For this reason, $^{99{\rm m}}$Tc is used in approximately 85% of diagnostic procedures in NM with more than 40 million of them performed globally on an annual basis (Eckelman, 2009). Its short physical (6.0 h) and biological (1 day) half-lives allows for the performance of diagnostic procedures with minimum radiation exposure to the patient. It is equally important that the precursor of $^{99{\rm m}}$Tc, $^{99}$Mo, has a half-life of 66 h, facilitating its transport and distribution over long distances.

Until recently, the dominant technology for the production of $^{99}$Mo was based on irradiation of highly enriched, weapons grade ($\approx$ 93% $^{235}$U) uranium (HEU) targets in dedicated high-flux research reactors. This implies transporting of the weapons grade uranium from national defense stockpiles (tens kg per year) both domestically and internationally. Such shipments put nuclear non-proliferation at risk and endanger nuclear safety in general. For this reason, the USA administration began supporting alternative $^{99}$Mo production methods which do not involve HEU.

Over the last decade, several of such methods have been proposed and discussed (National Research Council, 2009; Report of the Task Force; Lidsky and Lanza, 1996). The most developed one is based on the neutron capture process (n, $\gamma$) on a $^{98}$Mo (isotopic abundance 24.13%) target thus producing the $^{99}$Mo. The main disadvantages of this approach are: 1) a need for a high flux nuclear reactor, 2) low specific activity of the produced $^{99}$Mo, and as a result, 3) a need for a new concept $^{99}$Mo/$^{99{\rm m}}$Tc generator because of the much lower specific activity of the product and the need to separate $^{98}$Mo from $^{99}$Mo (Report of the Task Force).

Among the accelerator-based $^{99}$Mo production methods, one of the most promising technique is based on the photoneutron process, i.e. the ($\gamma$, n) reaction (Report of the Task Force; Bennett et al., 1999; Davydov and Mareskin, 1994; Diamond, 1999; Fujiwara et al., 2017; Berger and Seltzer, 1970; Seltzer and Berger, 1973; Ross et al., 2010; Tsechanski, 2017). In this process, natural Mo or its heaviest stable isotope, $^{100}$Mo (isotopic abundance of 9.63%), is irradiated by bremsstrahlung photons from an electron accelerator according to the $^{100}$Mo($\gamma$, n)$^{99}$Mo reaction.

The source of the $\gamma$-radiation in this case is high energy electron beam irradiating a metal target (converter). The converter should be chosen from the high-Z metals, such as tungsten, tantalum, natural or depleted uranium, in order to maximize the bremsstrahlung yield. In such a case, the $^{100}$Mo target has to be placed as close as possible to the source of the bremsstrahlung photons (converter). However, because of relatively low efficiency of the bremsstrahlung production and due to considerable self-absorption of the produced bremsstrahlung in the high-Z body of the converter, the setup must be cooled by distilled water under pressure. Unfortunately, this increases the distance

---

* Corresponding author.
E-mail address: D.Fedorchenko@gmail.com (D. Fedorchenko).

https://doi.org/10.1016/j.radphyschem.2020.109108
Received 12 June 2020; Received in revised form 9 July 2020; Accepted 12 July 2020
Available online 06 August 2020
0969-806X/ © 2020 Elsevier Ltd. All rights reserved.

![](./images/812581486606680065_1.jpg)
![](./images/812581486606680065_2.jpg)
![](./images/812581486606680065_3.jpg)

between the converter and the target thus decreasing the efficiency of $^{99}$Mo production. The photoneutron process described here is a well- known so-called "two-stage" approach in which, during the first stage, the bremsstrahlung photons are generated in the converter, and during the second stage, these photons cause photonuclear reactions in the target.

An alternative "one-stage" approach has been investigated and de- scribed in works (Tsechanski, 2017; Tsechanski et al., 2016, 2019; Fedorchenko and Tsechanski, 2019) for the photoneutron production of RIs. Unlike the two-stage approach, the one-stage approach combines the converter and the target which maximizes the yield. The dis- advantage of the one-stage approach is its relatively higher thermal load, which might be an issue for some targets.

According to the one-stage approach, production and accumulation of $^{99}$Mo is carried out in the Mo-target/converter itself, located in the target assembly inside the electron accelerator. Therefore, intense flux of the high energy bremsstrahlung photons and neutrons (many MeV's energy range) will be found around the target assembly outside the accelerator. These high energy bremsstrahlung photons can be used to produce some other very important radioisotopes via the (γ,n), (γ,p) or other photonuclear reactions on the corresponding additional targets placed in the vicinity of the $^{99}$Mo target assembly. For example, an external target of the lightest stable isotope of xenon, $^{124}$Xe, may be used in such a way to produce $^{123}$I via the (γ,n) reaction on $^{124}$Xe at the same time as the primary radioisotope $^{99}$Mo is produced in the one- stage setup. Moreover, some short-lived positron emitters like $^{18}$F, $^{15}$O, $^{13}$N, and $^{11}$C can also be produced simultaneously for use in Positron Emission Tomography (PET). This can be accomplished via the (γ,n) reaction as well, by placing an external target from an appropriate stable isotope adjacent to the accelerator target assembly.

Along with the aforementioned advantages of the one-stage ap- proach in the photonuclear production of RIs, there is another very important and unique feature that can be implemented exclusively in the one-stage approach. This feature is the possible contribution of the electronuclear reaction.

Direct irradiation of the molybdenum production target by the electron beam causes not only the (γ,n) photonuclear reactions, but also the so-called electronuclear reactions. In the case of electronuclear re- action incident electrons interact with the nuclei directly, without producing any bremsstrahlung photons. In particular, this leads to an additional $^{99}$Mo production channel in molybdenum target from the $^{100}$Mo(e$^-$,e$^-$n)$^{99}$Mo reaction.

The experimental data on the electronuclear reactions are rather sparse. Namely, EXFOR database (Zerkin and Pritychenko, 2018) con- tains only three data points for the (e$^-$,e$^-$n) reaction on natural mo- lybdenum. The corresponding data for both electronuclear and photo- nuclear reactions extracted from the paper (Batii et al., 1987) are presented in Table 1.

As it could be seen from Table 1, cross sections for electronuclear reactions for beam energies in 150–200 MeV region are about two or- ders of magnitude smaller than those for photonuclear. From the gen- eral theoretical consideration (Budnev et al., 1975) it follows that $\sigma_{el}/\sigma_{ph} \sim \alpha = 1/137$, where $\alpha$ is the fine-structure constant, so the re- lationship between the cross sections should also be preserved for the lower energies commonly used for the RI production. As an example one could consider the photonuclear and the electronuclear cross sections for $^{63}$Cu extracted from EXFOR database (Zerkin and Pritychenko, 2018) shown in Fig. 1. While the photonuclear cross section exhibits typical resonance behavior (the Giant Dipole Re- sonance peak) for photon energies in the 12–20 MeV region and drops sharply for higher energies, the electronuclear cross section mono- tonically increases as the incident electron energy grows. We can expect the similar qualitative behavior for the $^{100}$Mo cross sections around the GDR peak energies.

<table>
<caption>Table 1<br>Photonuclear and electronuclear cross sections for $^{99}$Mo production on natural molybdenum (Batii et al., 1987).</caption>
<thead>
  <tr>
    <th>Beam energy, MeV</th>
    <th>$\sigma_{ph}$, mb</th>
    <th>$\sigma_{el}$, mb</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>150</td>
    <td>6.5</td>
    <td>0.16</td>
  </tr>
  <tr>
    <td>200</td>
    <td>6.3</td>
    <td>0.17</td>
  </tr>
  <tr>
    <td>225</td>
    <td>6.4</td>
    <td>0.21</td>
  </tr>
</tbody>
</table>

![](./images/812581486606680065_4.jpg)

Fig. 1. The experimental photonuclear (γ,n) (Varlamov et al., 2016) and elec- tronuclear (e$^-$,e$^-$n) (Martins et al., 1984) cross sections for $^{63}$Cu.

![](./images/812581486606680065_5.jpg)

Fig. 2. The experimental electronuclear (e$^-$,e$^-$n) cross section (Martins et al., 1984) and the GEANT4 electron absorption (e$^-$,abs) cross section for $^{63}$Cu.

One should keep in mind that in the case of electronuclear reactions, electrons are the <i>primary</i> particles, in contrast to the photonuclear re- actions, with bremsstrahlung photons being the <i>secondary</i> particles. Therefore, even though electronuclear cross-section is lower than the photonuclear one, the density of the <i>primary</i> electrons at the entrance to the target/converter is significantly higher than the density of the <i>sec- ondary</i> bremsstrahlung photons. Moreover, all the electrons that bom- bard the target are monoenergetic. In contrast, the photon spectrum of the bremsstrahlung radiation is continuous ranging from zero to the kinetic energy of the electrons, with a significant fraction of the photons having the energy below the threshold of the photonuclear reaction.

All these considerations lead to the assumption that a small cross- section of the electro-nuclear reaction can be to some extent compen- sated by a significantly larger electron flux bombarding the target. The

goal of this paper is to estimate the yields of the electronuclear reac- tions and compare them to the yields of the photonuclear production routes. We will consider $^{99}$Mo as an example, keeping in mind that this can be applied to the production of other RIs.

Some estimates of electronuclear reaction yields were already per- formed by Kharashvili and Degtiarenko (Kharashvili and Degtiarenko, 2015; Degtiarenko and Kharashvili, 2016). They simulated and mea- sured contribution of electronuclear reactions using 2.25 and 3.36 GeV electron beams incident on thin foils of Al, Cu, Nb, Pb, and stainless steel. A significant contribution of the electronuclear reactions to neu- tron production and the resulting material activation was demon- strated. In this paper we will consider electronuclear and photonuclear interaction of 30-50 MeV electron beams, which are more common for RI production than several GeVs, using both thick and thin $^{100}$Mo tar- gets. Such setup is often used for studies of $^{99}$Mo production using electron accelerators. We will show the results of the Monte Carlo si- mulations of the relative contributions of the $^{100}$Mo($\gamma$,n)$^{99}$Mo and the $^{100}$Mo(e$^-$,e$'$n)$^{99}$Mo channels performed with the GEANT4 simulation toolkit.

## 2. Simulation software

To simulate the $^{99}$Mo production in the $^{100}$Mo target we used GEANT4 software package version 10.6. p1 (Agostinelli et al., 2003; Allison et al., 2006, 2016). This software toolkit for Monte Carlo si- mulations of particle transport was developed and maintained by the CERN collaboration. The toolkit is actually represented by a collection of C++ classes covering all aspects of particle transport in various media. These aspects, in particular, include an impressive set of phy- sical models for various particles and energy ranges with the ability of flexible configuration for a specific task. For the purposes of the current research the most important model to implement was the electro- nuclear reaction model (Wellisch et al., 2003), which is unique to GEANT4. Among the other commonly used Monte Carlo transport codes only FLUKA (Ferrari et al., 2005; Böhlen et al., 2014) supports elec- tronuclear reaction simulation.

The standard model for photonuclear reaction in GEANT4 uses parameterization of the measured cross sections for about 50 nuclei for the photoabsorption cross section calculation (Wellisch et al., 2003) and the Bertini cascade model for generation of the final state (Wright and Kelsey, 2015). However, this model has considerable discrepancies with the experimental data for energies below 50 MeV (Shin, 2015; Quintieri et al., 2017). Another option for simulation of photonuclear reaction is the LEND model (Allison et al., 2016) that uses evaluated data from ENDF/B-VII database (Chadwick et al., 2011) for incident neutrons and photons. This model provides more accurate results, but unfortunately supports a very limited set of nuclei. We adopted the LEND model for the simulation of photonuclear reactions within the framework of the current paper.

Implementation of the electronuclear reactions within GEANT4 uses the equivalent photon approximation (EPA) (Wellisch et al., 2003; Kossov, 2002). This approach is based on the fact that electronuclear interaction for relatively low energies could be described in the terms of one-photon exchange. In this sense electronuclear interaction is close to photonuclear, with virtual photons defining the interaction properties instead of real photons in the latter case. Consequently, within the EPA electrons are replaced with a flux of equivalent photons of specific spectral distribution (Budnev et al., 1975). The final state of the elec- tronuclear reaction is sampled using the Bertini cascade model (Allison et al., 2016; Wright and Kelsey, 2015).

There are no experimental data for the electronuclear cross sections on molybdenum below 150 MeV to evaluate the model used by GEANT4 for 10-50 MeV region, so we used the available data for $^{63}$Cu isotope for evaluation. The electron absorption (e$^-$, abs) calculated with GEANT4 is shown in Fig. 2, together with the experimental data for the (e$^-$,e$'$n) reaction from (Martins et al., 1984). The model dependence qualitatively resembles the behavior of the experimental cross section curve for the (e$^-$,e$'$n) reaction. However, the model (e$^-$,abs) cross section curve is higher and steeper, which can be ex- plained by the contribution from the other channels such as (e$^-$,e$^-$'p), (e$^-$,e$^-$'2n), (e$^-$,e$^-$'2p), etc. This contribution increases as the incident electron energy grows, as additional reaction channels open.

![](./images/812581486606680065_6.jpg)

Fig. 3. The photon and the electron absorption cross sections for $^{100}$Mo used by GEANT4.

The GEANT4 model cross sections for photon ($\gamma$, abs) and electron (e$^-$,abs) absorption processes resulting in $^{100}$Mo are shown in Fig. 3. The photon absorption cross section is essentially the same as given by the ENDF/B-VII database (Chadwick et al., 2011). The model electro- nuclear cross section for $^{100}$Mo is quite similar to the electronuclear cross section for $^{63}$Cu isotope (Fig. 2).

## 3. Simulations of $^{99}$Mo production

### 3.1. Thick target simulations

To estimate the relative contribution of electronuclear and photo- nuclear reactions to $^{99}$Mo production we carried out simulations of a cylindrical $^{100}$Mo converter/production target irradiated by the elec- tron beam (one-stage approach). The dimensions of the target were chosen based on the considerations presented in our previous works (Fedorchenko and Tsechanski, 2019; Tsechanski et al., 2019). Namely, the thickness of the cylindrical$^{100}$Mo converter/target was 20 mm ($\approx$ 2 radiation lengths (RL) for electrons in molybdenum), and its radius was 3.85 mm. Assuming that $^{100}$Mo has the same density as natural Mo ($\rho$ = 10.22 g/cm$^3$), this yielded a 9.518 g target. During the simulations the $^{100}$Mo converter/target was irradiated by a monochromatic electron pencil beam with energies ranging from 30 to 50 MeV in 5 MeV incre- ments.

Fig. 4 shows the results of the GEANT4 simulations of the $^{99}$Mo yield per primary electron separately for photonuclear and electronuclear reactions. As can be seen from Fig. 4, the yield of the electronuclear reaction is almost two orders of magnitude smaller than the corre- sponding photonuclear yield at all energies under consideration, which matches with the ratio of the cross-sections.

However, one should note that the electronuclear and photonuclear yields of $^{99}$Mo were calculated as averaged over the entire volume of the 2 cm long $^{100}$Mo converter/target cylinder. It should be remembered that the primary electron beam flux at the entrance to the converter/ target will be by far much higher than the corresponding brems- strahlung photon flux, since these photons have a pronounced buildup. For example, in case of 30-50 MeV electron beams, this buildup can extend up to $\sim$ 2/3 of the corresponding CSDA range, i.e. 5.6-7.3 mm in

![](./images/812581486606680065_7.jpg)

Fig. 4. $^{99}$Mo yield per primary electron for photonuclear and electronuclear reactions.

the case of Mo metal (see Fig. 2 or Table 4 in (Tsechanski et al., 2016)). In other words, the primary electron beam flux drops much faster throughout the target than the bremsstrahlung flux does. It follows that in thinner targets a significantly larger contribution of the electro- nuclear reaction should be expected than that in thicker targets, shown in Fig. 4.

To compare the electronuclear and photonuclear yields in the tar- gets of different thicknesses, we have carried out the GEANT4 calcu- lations of the $^{99}$Mo yield distributions along the length of the 20 mm long $^{100}$Mo target bombarded by the beams of monoenergetic electrons with energies of (30-50) MeV. The calculation bin width along the target length was 1 mm. Fig. 5 represents the electronuclear $^{99}$Mo yield distribution along the length of the 20 mm long $^{100}$Mo target and Fig. 6 represents its photonuclear $^{99}$Mo yield distribution counterpart.

As the monoenergetic electron beam hits a $^{100}$Mo target, the elec- trons' flux and energy are both at their maximum at the very target entrance and start dropping as the beam penetrates through. Hence, the electronuclear cross section is also at its maximum directly at the target entrance (see Fig. 3), which in turn corresponds to the maximum electronuclear yield. And indeed, this is clearly seen in Fig. 5. The high energy electrons passing through the target material undergo interac- tions with the electric fields of the nuclei and decelerate very rapidly, radiating bremsstrahlung photons and scattering from their original direction. As a result, both the electron flux and energy decrease very quickly as the beam penetrates into the target.

The electron penetration depth is described by the CSDA range, which is the continuous-slowing-down approximation of the average path length. The electron CSDA ranges for electrons extracted from the ESTAR database (Berger et al., 2005) are presented in Table 2. As can be seen in Fig. 5, the electronuclear production yield of $^{99}$Mo decreases relatively quickly and, to a first approximation, almost linearly from maximum value at the entrance to the about two orders of magnitude lower values at the depth corresponding to the CSDA range.

![](./images/812581486606680065_8.jpg)

Fig. 5. $^{99}$Mo electronuclear yield distribution along the depth of a 20 mm thick $^{100}$Mo target. Calculation bin width 1 mm.

![](./images/812581486606680065_9.jpg)

Fig. 6. $^{99}$Mo photonuclear yield distribution along the depth of a 20 mm thick $^{100}$Mo target. Calculation bin width 1 mm.

<table>
<caption>Table 2<br>CSDA range for molybdenum (Berger et al., 2005).</caption>
<thead>
<tr>
<th>Energy MeV</th>
<th>30</th>
<th>35</th>
<th>40</th>
<th>45</th>
<th>50</th>
</tr>
</thead>
<tbody>
<tr>
<td>$r_{0}$, cm</td>
<td>1.254</td>
<td>1.369</td>
<td>1.472</td>
<td>1.565</td>
<td>1.651</td>
</tr>
</tbody>
</table>

In contrast to the monotonously decreasing nature of the electro- nuclear production yield of $^{99}$Mo in Fig. 5, its photonuclear counterpart curve (Fig. 6) demonstrates the pronounced buildup. The main con- tributor to this buildup is the well-known behavior of the brems- strahlung efficiency curves (for the Mo target case see, for example, Fig. 2 of (Tsechanski et al., 2016)). This behavior is characterized by a rapid rise of the bremsstrahlung efficiency in the shower regime up to the maxima and a much slower drop-off thereafter. After the maxima, the curve is dominated by the broad-beam attenuation of the brems- strahlung. However, the $^{99}$Mo photonuclear yield distribution curves shown in Fig. 6 are obviously determined not only by the brems- strahlung efficiency of $^{100}$Mo target, but also by the energy distribution of the bremsstrahlung photons and by the GDR cross section behavior of $^{100}$Mo (see Fig. 3). For this reason, the buildup location of the $^{99}$Mo photonuclear yield distribution curve in Fig. 6 is slightly different from the bremsstrahlung efficiency buildup for a molybdenum target from (Tsechanski et al., 2016).

Comparison of the electronuclear (Fig. 5) and photonuclear (Fig. 6) yields shows that the former has a significant effect only in the first few millimeters of the target. Fig. 7 shows the ratio of the electronuclear reaction yield to the photonuclear one and one can see that in the first millimeter of the target this ratio exceeds 0.2-0.24 (depending on the electron beam energy), but rapidly decreases to less than 0.01-0.02 at about 1 cm into the target. The rapid drop-off of the ratio as a function of the target depth, compared to the almost linear decrease of elec- tronuclear yield (Fig. 5), is governed by the rapid growth of the bremsstrahlung efficiency and the consequent increase of the photo- nuclear reactions' intensity.

The results obtained for the yield of the $^{100}$Mo(e$^-$,e$^-$n)$^{99}$Mo reac- tion in the one-stage setup confirm the limited contribution of this process to the total yield of $^{99}$Mo in the thick target. The yield can be slightly improved by increasing the beam energy, as the electronuclear cross sections exhibit gradual growth with the energy of the incident electron. However, this effect will be to some extent compensated by

![](./images/812581486606680065_10.jpg)

Fig. 7. Ratio of the electronuclear reaction yield to the photonuclear one along the 20 mm thick $^{100}$Mo target. Calculation bin width 1 mm.

the accompanying growth of the photonuclear $^{99}$Mo production resulting from the increased number of bremsstrahlung photons with energies around the GDR resonance.

A more serious objection against the usage of high energy electron beams is the high heat load into the production target. According to Fig. 8, showing the results of the energy deposition calculations in the 20 mm thick $^{100}$Mo target, it follows that around a half of beam energy is deposited into the target. As beam energy increases, target cooling becomes a serious engineering problem, which is usually solved by splitting the solid target into a set of thin disks cooled by water or helium (Diamond et al., 2014).

### 3.2. Thin target simulations

We demonstrated that the impact of electronuclear reaction is significant for relatively thin targets irradiated by the direct electron beam. This could be the first disk in the multi-disk production target (Mang'era et al., 2015), or thin foils often used for estimation of the $^{99}$Mo yield (Starovoitova et al., 2014). In case of a thin target, neglecting the electronuclear route could result in the significant underestimate of the $^{99}$Mo production.

To evaluate the effect of electronuclear production of the $^{99}$Mo in the thin target we considered a single 1 mm thick disk with the radius of 3.85 mm made of $^{100}$Mo. As in the case of the thick target it was irradiated by the 30-50 MeV zero-radius electron beam. Both electronuclear and photonuclear yields simulated along the target are presented in Figs. 9 and 10, correspondingly. The calculation bin width along the target thickness was 0.1 mm.

It can be seen that the electron flux and the average electron energy do not considerably change as we go deeper into the target. This results in a flat-sloped, almost linear, $^{99}$Mo yield distribution (Fig. 9). In contrast to the electron flux, the number of bremsstrahlung photons increases as thickness increases, due to the buildup effect. In the first approximation this growth could be regarded as linear, and due to the almost constant electron energy all these bremsstrahlung photons have the same spectrum. As a result, we have the linear growth of $^{99}$Mo production (Fig. 10).

![](./images/812581486606680065_11.jpg)

Fig. 8. Energy deposition in the 20 mm thick $^{100}$Mo target.

![](./images/812581486606680065_12.jpg)

Fig. 9. $^{99}$Mo electronuclear yield distribution along the depth of a 1 mm thick $^{100}$Mo target. Calculation bin width 0.1 mm.

![](./images/812581486606680065_13.jpg)

Fig. 10. $^{99}$Mo photonuclear yield distribution along the depth of a 1 mm thick $^{100}$Mo target. Calculation bin width 0.1 mm.

Different behavior of the electronuclear and photonuclear yield distributions results in a rather thin frontal layer of the target where electronuclear production of $^{99}$Mo dominates. Fig. 11 shows the upper limit for the thickness of this layer to be 0.15-0.2 mm depending on the beam energy. It follows that in case of thin targets, such as foils, neglecting the contribution from the electronuclear reaction could lead to the substantial errors if thick production target estimates are used. Fig. 12 shows that even for a 1 mm thick $^{100}$Mo target contribution of the $^{100}$Mo(e$^-$,e$'$n)$^{99}$Mo reaction exceeds 20%, while for a 0.1 mm target one can expect this contribution to be up to 70%.

### 4. Conclusions

In this paper we examined the contribution of the $^{100}$Mo(e$^-$,e$'$n)$^{99}$Mo electronuclear reaction to the one-stage photonuclear production of $^{99}$Mo. Monte Carlo simulations performed with the GEANT4 simulation toolkit demonstrated that in case of a thick target this contribution is about two orders of magnitude lower than the one from the photonuclear reaction $^{100}$Mo($\gamma$,n)$^{99}$Mo. However, the situation is very different for the direct irradiation of sub-mm thick foils. For example, in

![](./images/812581486606680065_14.jpg)

Fig. 11. Ratio of the electronuclear yield of $^{99}$Mo to the photonuclear one along the depth of a 1 mm thick $^{100}$Mo target. Calculation bin width 0.1 mm.

![](./images/812581486606680065_15.jpg)

Fig. 12. Fraction of the electronuclear yield of $^{99}$Mo as a function of the target thickness. Calculation bin width 1 mm.

case of a 1 mm thick target, contribution of electronuclear $^{99}$Mo yield reaches about 20%, and in case of a 0.1 mm thick target, it exceeds 70%. In this case, corrections to account for the electronuclear production route are necessary to obtain accurate estimates of $^{99}$Mo yields. This applies to other radioisotopes obtained by the photonuclear routes on thin targets.

CRediT authorship contribution statement

A. Tsechanski: Conceptualization, Validation, Writing - original draft. D. Fedorchenko: Methodology, Software, Investigation, Visualization. V. Starovoitova: Conceptualization, Validation, Writing - review & editing.

Declaration of competing interest

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

References

Agostinelli, S., Allison, J., Amako, K., Apostolakis, J., Araujo, H., Arce, P., Asai, M., Axen, D., Banerjee, S., Barrand, G., et al., 2003. Geant4—a simulation toolkit. Nucl. Instrum. Methods Phys. Res. Sect. A Accel. Spectrom. Detect. Assoc. Equip. 506 (3), 250-303. https://doi.org/10.1016/S0168-9002(03)01368-8.

Allison, J., Amako, K., Apostolakis, J., Araujo, H., Arce Dubois, P., Asai, M., Barrand, G., Capra, R., Chauvie, S., Chytracek, et al., 2006. Geant4 developments and applications. IEEE Trans. Nucl. Sci. 53 (1), 270-278. https://doi.org/10.1109/TNS.2006.869826.

Allison, J., Amako, K., Apostolakis, J., Arce, P., Asai, M., Aso, T., Bagli, E., Bagulya, A., Banerjee, S., Barrand, G., et al., 2016. Recent developments in Geant4. Nucl. Instrum. Methods Phys. Res. Sect. A Accel. Spectrom. Detect. Assoc. Equip. 835, 186-225. https://doi.org/10.1016/j.nima.2016.06.125.

Batii, V.G., Vladimirov, Y.V., Rakivnenko, Y.N., Ranyuk, Y.N., Rastrepin, O.A., Skakun, E.A., 1987. Radionuclide accumulation for photo-and electron disintegration of nuclei in the A ~90 region. Sov. Atom. Energy 63 (6), 899-903. https://doi.org/10.1007/BF01126101.

Bennett, R.G., Christian, J.D., Petti, D.A., Terry, W.K., Grover, S.B., 1999. A system of 99mTc production based on distributed electron accelerators and thermal separation. Nucl. Technol. 126 (1), 102-121. https://doi.org/10.13182/NT99-A2961.

Berger, M.J., Seltzer, S.M., 1970. Bremsstrahlung and photoneutrons from thick tungsten and tantalum targets. Phys. Rev. C 2 (2), 621-631. https://doi.org/10.1103/PhysRevC.2.621.

Berger, M., Coursey, J., Zucker, M., Chang, J., 2005. ESTAR, PSTAR, and ASTAR: Computer Programs for Calculating Stopping-Power and Range Tables for Electrons, Protons, and Helium Ions. http://physics.nist.gov/Star, version 2.0.1.

Böhlen, T.T., Cerutti, F., Chin, M.P.W., Fassò, A., Ferrari, A., Ortega, P.G., Mairani, A., Sala, P.R., Smirnov, G., Vlachoudis, V., 2014. The FLUKA code: developments and challenges for high energy and medical applications. Nucl. Data Sheets 120, 211-214. https://doi.org/10.1016/j.nds.2014.07.049.

Budnev, V.M., Ginzburg, I.F., Meledin, G.V., Serbo, V.G., 1975. The two-photon particle production mechanism. Physical problems. Applications. Equivalent photon approximation. Phys. Rep. 15 (4), 181-282. https://doi.org/10.1016/0370-1573(75)90009-5.

Chadwick, M.B., Herman, M., Obložinský, P., Dunn, M.E., Danon, Y., Kahler, A.C., Smith, D.L., Pritchenko, B., Arbanas, G., Arcilla, R., et al., 2011. ENDF/B-VII.1 nuclear data for science and technology: cross sections, covariances, fission product yields and decay data. Nucl. Data Sheets 112 (12), 2887-2996. https://doi.org/10.1016/j.nds.2011.11.002.

Davydov, M.G., Mareskin, S.A., 1994. Preparation of 99Mo and 99mTc in electron accelerators. Radiochemistry 35 (5), 569-573.

Degtiarenko, P., Kharashvili, G., 2016. Contribution of the direct electronuclear processes to thin target activation. In: 12th Meeting of Task-Force on Shielding Aspects of Accelerators. Targets and Irradiation Facilities, pp. 284-290.

Diamond, W.T., 1999. A radioactive ion beam facility using photofission. Nucl. Instrum. Methods Phys. Res. Sect. A Accel. Spectrom. Detect. Assoc. Equip. 432 (2), 471-482. https://doi.org/10.1016/S0168-9002(99)00492-1.

W. Diamond, V. Nagarkal, M. de Jong, C. Regier, L. Lin, D. Ullrich, Production of Molybdenum-99 Using Electron Beams, US Patent No. 20140348284A1 (Nov. 2014).

Eckelman, W.C., 2009. Unparalleled contribution of technetium-99m to medicine over 5 decades. JACC. Cardiovascular imaging 2 (3), 364-368. https://doi.org/10.1016/j.jcmg.2008.12.013.

Fedorchenko, D.V., Tsechanski, A., 2019. Photoneutronic aspects of the molybdenum-99 production by means of electron linear accelerators. Nucl. Instrum. Methods Phys. Res. Sect. B Beam Interact. Mater. Atoms 438, 6-13. https://doi.org/10.1016/j.nimb.2018.10.018.

Ferrari, A., Sala, P.R., Fassò, A., Ranft, J., Fluka, Oct. 2005. A multi-particle transport code (Program version 2005). Tech. rep. https://doi.org/10.2172/877507.

Fujiwara, M., Nakai, K., Takahashi, N., Hayakawa, T., Shizuma, T., Miyamoto, S., Fan, G.T., Takemoto, A., Yamaguchi, M., Nishimura, M., 2017. Production of medical 99mTc isotope via photonuclear reaction. Phys. Part. Nucl. 48 (1), 124-133. https://doi.org/10.1134/S1063779617010075.

Kharashvili, G., Degtiarenko, P., 2015. Activation by 2.25 and 3.36 GeV electrons: comparison of measurements with FLUKA calculations. In: 12th Meeting of Task-Force on Shielding Aspects of Accelerators. Targets and Irradiation Facilities, pp. 149-155.

Kossov, M., 2002. Approximation of photonuclear interaction cross-sections. Eur. Phys. J. A (EPJ A), - Hadrons Nucl. 14 (3), 377-392. https://doi.org/10.1140/epja/i2002-10008-x.

Lidsky, L., Lanza, R., 1996. Application of Advanced Technology Accelerators to Isotope Production. Massachusetts Institute of Technology, Idaho National Engineering Laboratory Annual Report FY-96.

Mang'era, K., Ogbomo, K., Zriba, R., Fitzpatrick, J., Brown, J., Pellerin, E., Barnard, J., Saunders, C., de Jong, M., 2015. Processing and evaluation of linear accelerator-produced 99Mo/99mTc in Canada. J. Radioanal. Nucl. Chem. 305 (1), 79-85. https://doi.org/10.1007/s10967-015-3997-5.

Martins, M.N., Hayward, E., Lamaze, G., Maruyama, X.K., Schima, F.J., Wolynec, E., 1984. Experimental test of the bremsstrahlung cross section. Phys. Rev. C 30 (6), 1855-1860. https://doi.org/10.1103/PhysRevC.30.1855.

National Research Council, 2009. Medical Isotope Production without Highly Enriched Uranium. The National Academies Press, Washington, DC. https://doi.org/10.17226/12569.

Quintieri, L., Pia, M.G., Augelli, M., Saracco, P., Capogni, M., Guarnieri, G., 2017. Quantification of the validity of simulations based on Geant4 and FLUKA for photonuclear interactions in the high energy range. EPJ Web Conf. 153, 06023. https://doi.org/10.1051/epjconf/201715306023.

Report of the Task Force on Alternatives for Medical Isotope Production — TRIUMF : Canada's Particle Accelerator Centre. https://www.triumf.ca/report-medical-isotope-production.

Ross, C., Galea, R., Saull, P., Davidson, W., Brown, P., Brown, D., Harvey, J., Messina, G., Wassenaar, R., De Jong, M., 2010. Using the $^{100}$Mo photoneutron reaction to meet Canada's requirement for $^{99}$mTc. Phys. Can. 66 (1), 19-24.

Seltzer, S.M., Berger, M.J., 1973. Photoneutron production in thick targets. Phys. Rev. C 7 (2), 858-861. https://doi.org/10.1103/PhysRevC.7.858.

Shin, J.W., 2015. A data-based photonuclear reaction model for GEANT4. Nucl. Instrum. Methods Phys. Res. Sect. B Beam Interact. Mater. Atoms 358, 194-200. https://doi.org/10.1016/j.nimb.2015.06.034.

Starovoitova, V.N., Tchelidze, L., Wells, D.P., 2014. Production of medical radioisotopes with linear accelerators. Appl. Radiat. Isot. 85, 39-44. https://doi.org/10.1016/j.apradiso.2013.11.122.

Tsechanski, A., 2017. Molybdenum-converter Based Electron Linear Accelerator and Method for Producing Radioisotopes, US Patent No. 9721691B2. EU Patent No. EP2748825B1 (2017).

Tsechanski, A., Bielajew, A.F., Archambault, J.P., Mainegra-Hing, E., 2016. Electron ac- celerator-based production of molybdenum-99: bremsstrahlung and photoneutron generation from molybdenum vs. tungsten. Nucl. Instrum. Methods Phys. Res. Sect. B Beam Interact. Mater. Atoms 366, 124-139. https://doi.org/10.1016/j.nimb.2015.10.057.

Tsechanski, A., Fedorchenko, D., Starovoitova, V., Galperin, A., 2019. Converter opti- mization for photonuclear production of Mo-99. Nucl. Instrum. Methods Phys. Res. Sect. B Beam Interact. Mater. Atoms 461, 118-123. https://doi.org/10.1016/j.nimb.2019.09.038.

Varlamov, V.V., Davydov, A.I., Makarov, M.A., Orlin, V.N., Peskov, N.N., 2016. Reliability of the data on the cross sections of the partial photoneutron reaction for 63,65Cu and 80Se nuclei. Bull. Russ. Acad. Sci. Phys. 80 (3), 317-324. https://doi.org/10.3103/S1062873816030333.

Wellisch, J.P., Kossov, M., Degtyarenko, P., Mar. 2003. Electro and Gamma Nuclear Physics in Geant4, Tech. Rep. JLAB-ACC-03-17; DOE/40150-3165; Nucl-Th/0306012. Thomas Jefferson National Accelerator Facility, Newport News, VA (US).

Wright, D.H., Kelsey, M.H., 2015. The Geant4 Bertini cascade. Nucl. Instrum. Methods Phys. Res. Sect. A Accel. Spectrom. Detect. Assoc. Equip. 804, 175-188. https://doi.org/10.1016/j.nima.2015.09.058.

Zerkin, V.V., Pritychenko, B., 2018. The experimental nuclear reaction data (EXFOR): extended computer database and Web retrieval system. Nucl. Instrum. Methods Phys. Res. Sect. A Accel. Spectrom. Detect. Assoc. Equip. 888, 31-43. https://doi.org/10.1016/j.nima.2018.01.045.