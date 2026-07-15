# Thermoelectric properties of monolayer $MSe_2$ (M = Zr, Hf): low lattice thermal conductivity and a promising figure of merit

This content has been downloaded from IOPscience. Please scroll down to see the full text.

2016 Nanotechnology 27 375703

(http://iopscience.iop.org/0957-4484/27/37/375703)

View [the table of contents for this issue](), or go to the [journal homepage]() for more

Download details:

IP Address: 207.162.240.147
This content was downloaded on 10/08/2016 at 06:10

Please note that [terms and conditions apply]().

# Thermoelectric properties of monolayer $MSe_2$ ($M = \text{Zr}$, Hf): low lattice thermal conductivity and a promising figure of merit

Guangqian Ding¹, G Y Gao¹, Zhishuo Huang², Wenxu Zhang² and Kailun Yao¹

¹ School of Physics and Wuhan National High Magnetic Field Center, Huazhong University of Science and Technology, Wuhan 430074, People's Republic of China
² State Key Laboratory of Electronic Thin Films and Integrated devices, University of Electronic Science and Technology of China, Chengdu 610054, People's Republic of China

E-mail: guoying_gao@mail.hust.edu.cn

Received 18 April 2016, revised 16 June 2016
Accepted for publication 1 July 2016
Published 3 August 2016

![](./images/811172489257287681_1.jpg)

## Abstract
Monolayer transition-metal dichalcogenides (TMDCs) $MX_2$ ($M = \text{Mo}$, W, Zr, Hf, etc; X = S, Se, Te) have become well-known in recent times for their promising applications in thermoelectrics and field effect transistors. In this work, we perform a systematic study on the thermoelectric properties of monolayer $ZrSe_2$ and $HfSe_2$ using first-principles calculations combined with Boltzmann transport equations. Our results point to a competitive thermoelectric figure of merit (close to 1 at optimal doping) in both monolayer $ZrSe_2$ and $HfSe_2$, which is markedly higher than previous explored monolayer TMDCs such as $MoS_2$ and $MoSe_2$. We also reveal that the higher figure of merits arise mainly from their low lattice thermal conductivity, and this is partly due to the strong coupling of acoustic modes with low frequency optical modes. It is found that the figure of merits can be better optimized in $n$-type than in $p$-type. In particular, the performance of $HfSe_2$ is superior to $ZrSe_2$ at a higher temperature. Our results suggest that monolayer $ZrSe_2$ and $HfSe_2$ with lower lattice thermal conductivity than usual monolayer TMDCs are promising candidates for thermoelectric applications.

Keywords: thermoelectric, TMDC, phonon, monolayer

(Some figures may appear in colour only in the online journal)

## 1. Introduction
Two-dimensional monolayer materials have attracted great interest in recent years due to their novel physical and chemical properties [1–3]. The weak van der Waals interaction between atomic layers in these bulk crystals, e.g., phosphorus, $MoS_2$, and $WSe_2$, paves the way to their monolayer structures both theoretically and experimentally [2, 4, 5]. It has been proposed that low-dimensional materials could have better thermoelectric performance than their bulk due to the diverse scattering mechanism for phonons [6–8]. Researching the thermoelectric response of low-dimensional materials has become a hot topic in the science community. The efficiency of thermoelectric devices, which can directly convert heat into electricity, is characterized by the dimensionless figure of merit $ZT = S^2\sigma T/\kappa$. Here, $S$ is the Seebeck coefficient, $\sigma$ the electrical conductivity, and $\kappa$ the thermal conductivity including both electronic ($\kappa_e$) and lattice ($\kappa_l$) contributions. The electrical conductivity and electrical thermal conductivity are, in many cases, related by the Wiedemann-Franz law:$\kappa_e = L\sigma T$, where $L$ is the Lorentz number, $2.4 \times 10^{-8} \text{J}^2\text{K}^{-2}\text{C}^{-2}$ for free electrons [9, 10].

There are some recent reports on the thermoelectric properties of TMDCs monolayers [11–15]. Specifically, Kumar *et al* reported a low optimized $ZT$ of about 0.1 at 1200 K in monolayer $MoSe_2$ [13]. For the typical monolayer $MoS_2$, a value of about 0.11 at 500 K was reported by Jin *et al* [11]. Only monolayer $WSe_2$ exhibited a better result of about

0.7 at high temperature [13]. It was confirmed that such a low $ZT$ is mainly caused by high $\kappa_{l}$. For example, the $\kappa_{l}$ in monolayer $MoS_{2}$ can be as large as $100\,\text{Wm}^{-1}\text{K}^{-1}$ at room temperature, and in $WSe_{2}$ is also higher than $40\,\text{Wm}^{-1}\text{K}^{-1}$ [11, 13]. To our surprise, we find all these explored mono- layer TMDCs correspond to the $2\text{H-MoS}_{2}$ type crystal structure. The TMDCs usually crystallize into two different structural types. One is the hexagonal $2\text{H-MoS}_{2}$ type while the other is the trigonal $1\text{T-CdI}_{2}$ type [16]. Those with $\text{CdI}_{2}$ type are typically represented by $M =$ Ti, Zr, Hf, etc. Yum- nam et al recently confirmed that the $\kappa_{l}$ of bulk Zr and Hf based TMDCs are almost 15 times lower than those of W and Mo based TMDCs, which is due to the strong hybridization of low lying optical modes with acoustic modes [17]. Most recently, similar behavior was also found in $\text{CdI}_{2}$ type monolayer $\text{ZrS}_{2}$. Lv et al reported a low $\kappa_{l}$ of $3.29\,\text{Wm}^{-1}\text{K}^{-1}$ and an optimized $ZT$ of 1.6 at 300 K in monolayer $\text{ZrS}_{2}$ [15], which are much better than those values for $\text{MoS}_{2}$ type monolayers. The studies point out that monolayer TMDCs with $\text{CdI}_{2}$ type structure are expected to realize much lower $\kappa_{l}$ and enhanced $ZT$.

To address the lack of thermoelectric investigation on $\text{CdI}_{2}$ type monolayer TMDCs, we set out to calculate the thermoelectric properties of monolayer $\text{ZrSe}_{2}$ and $\text{HfSe}_{2}$ by using first-principles calculations combined with Boltzmann transport equations, which have not so far been explored. Guo et al systematically studied the electronic structures of monolayer TMDCs, and showed that monolayer $\text{ZrS}_{2}$, $\text{HfS}_{2}$, $\text{ZrSe}_{2}$, and $\text{HfSe}_{2}$ are semiconductors with indirect band gaps while $\text{ZrTe}_{2}$ and $\text{HfTe}_{2}$ are metals [18]. We choose $\text{ZrSe}_{2}$ and $\text{HfSe}_{2}$ for their moderate band gaps of 0.45 eV and 0.61 eV, respectively. In the following, both electronic and phononic transport properties will be presented, and finally used for the prediction of $ZT$.

## 2. Computational methods

We first perform the structural optimization of monolayer $\text{ZrSe}_{2}$ and $\text{HfSe}_{2}$, within the framework of density function theory using projector-augmented-wave (PAW) pseudopo- tentials [19] and Perdew-Burke-Ernzerhof (PBE) exchange correlation functionals [20] as implemented in VASP [21]. The plane-wave energy cutoff is chosen as $286\,\text{eV}$-$30\%$ above the maximum recommended values for these atoms. We use a $15 \times 15 \times 1$ Monkhorst-Pack $k$-point grid. In order to avoid the interaction with periodic images, a $15\,\mathring{\text{A}}$ thickness of vacuum slab is added along the $z$-axis. Figures 1(a) and (b) show the top and side views of mono- layer $M\text{Se}_{2}$. We next calculate the electronic structure based on the optimized unit cell, and the Brillouin zone path is set according to the in-plane symmetry in the bulk ($\Gamma$-M-K-$\Gamma$) as shown in figure 1(c). Note that the hybrid density functional tends to overestimate the band gaps in these systems, as tested by Guo et al [18]. We therefore did not consider it in the calculations.

![](./images/811172489257287681_2.jpg)

Figure 1. (a) Top and (b) side views of monolayer $\text{MX}_{2}$ in $\text{CdI}_{2}$ type, where green and blue balls represent the M and X atoms, respectively. (c) The unit cell and corresponding Brillouin zone path with high-symmetry points at $\Gamma(0, 0, 0)$, M (0.5, 0, 0), K (1/3, 1/ 3, 0).

The electronic transport properties are found using Boltzmann transport theory and relaxation time approximation (RTA) as implemented in BoltzTraP [22], which allow us to calculate the $S$, $\sigma$ as well as $\kappa_{e}$. However, the RTA greatly limits the prediction of $ZT$ because $\sigma$ and $\kappa_{e}$ are calculated with relaxation time $\tau$ ($\sigma/\tau$ and $\kappa_{e}/\tau$). A possible routine is to use a constant relaxation time extracted from experiments, however, its accuracy is questionable. Here, we adopt the deformation potential theory based on the effective mass approximation to estimate $\tau$ [23, 24]:

$$
\mu = \frac{e\hbar^{3}C_{2D}}{k_{B}Tm^{*}m_{d}E_{l}^{2}},
$$

$$
\tau = \frac{\mu m^{*}}{e},
$$

where $m^{*}$ is the effective mass for the conveyor direction, $m_{d}$ is the average effective mass defined by $m_{d} = \sqrt{m_{l}^{*}m_{t}^{*}}$, $C_{2D}$ is the effective elastic modulus, and $E_{l}$ is the deformation potential constant. All obtained parameters are listed in table 1. It is worth noting that we consider that the carriers are mainly scattered by acoustic phonons. Thus, the calculated carrier mobility is the upper limit and the predicted relaxation time may be a little higher than its real value.

To obtain $\kappa_{l}$ and related phonon quantities, we use the phonon Boltzmann transport equation based on an adaptive smearing approach to the conservation of energy [25] and on an iterative solution method [26], as implemented in ShengBTE [27]. As boundary scattering only dominates in very low temperatures, the scattering probabilities from the phonon and isotope disorder are mainly considered in this method. Required inputs include descriptions of the second and third order interatomic force constants (IFCs) in the crystal structure. We calculate these IFCs by using $5 \times 5 \times 1$ supercells. The second order IFCs are obtained by Phonopy [28], and for the third order IFCs, we impose a cut-off so as to include interactions up to the third nearest neighbors.

<table>
<caption>Table 1. The elastic modulus, effective mass, deformation potential constant, carrier mobility and predicted relaxation time for hole and electron of monolayer ZrSe₂ and HfSe₂ at room temperature.</caption>
<thead>
<tr>
<th></th>
<th>Carriers</th>
<th>$C_{2\text{D}}$<br>(Jm⁻²)</th>
<th>$m_{\Gamma-M}^{*}$<br>$(m_{\text{e}})$</th>
<th>$m_{M-K}^{*}$<br>$(m_{\text{e}})$</th>
<th>$E_{l}$<br>(eV)</th>
<th>$\mu$<br>($10^{3}$ cm² V⁻¹ s⁻¹)</th>
<th>$\tau$<br>($10^{-12}$ s)</th>
</tr>
</thead>
<tbody>
<tr>
<td>ZrSe₂</td>
<td>hole</td>
<td>97.11</td>
<td>−0.55</td>
<td>−0.46</td>
<td>0.79</td>
<td>11.99</td>
<td>3.7</td>
</tr>
<tr>
<td></td>
<td>electron</td>
<td>97.11</td>
<td>2.03</td>
<td>0.22</td>
<td>1.25</td>
<td>0.98</td>
<td>1.1</td>
</tr>
<tr>
<td>HfSe₂</td>
<td>hole</td>
<td>99.97</td>
<td>−0.55</td>
<td>−0.47</td>
<td>0.82</td>
<td>11.34</td>
<td>3.5</td>
</tr>
<tr>
<td></td>
<td>electron</td>
<td>99.97</td>
<td>3.10</td>
<td>0.18</td>
<td>1.08</td>
<td>0.79</td>
<td>1.4</td>
</tr>
</tbody>
</table>

## 3. Results and discussion

### 3.1. Electronic structure

Bulk ZrSe₂ and HfSe₂ belong to the CdI₂ type TMDCs with the space group $P$-$3m1$ (164) and a trigonal unit cell consisting of three atoms, one Zr (Hf) and two Se. Each layer comprises a Se-Zr (Hf)-Se sandwich-like atomic sequence and has an inversion center between the layers, which are coupled with weak van der Waals interactions. The layered structures pave the way to the monolayer systems and their two-dimensional thin films are also successfully prepared experimentally [29, 30]. The optimized lattice parameters are $3.79\ \mathring{\text{A}}$ for monolayer ZrSe₂ and $3.76\ \mathring{\text{A}}$ for HfSe2, which are very close to their bulk values and compatible with the values from previous literature [18].

Calculated electronic structures of monolayer ZrSe₂ and HfSe₂ are shown in figure 2. Both are semiconductors with indirect band gaps of 0.53 eV and 0.68 eV, respectively, which is in good agreement with previous reports [18]. It is interesting to make a comparison with MoS₂ type monolayers. Due to the difference in crystal symmetry (the two Se atoms are mirror-inverted in MoS₂ type, while they have an inversion center in CdI₂ type), previous MoS₂ type monolayers, e.g., MoSe₂ and WSe₂, are all direct gap semiconductors with wide gaps of 1.44 eV and 1.56 eV, respectively [13]. It is known such a large gap is not beneficial to the optimization of thermoelectric performance, as a heavy doping is needed to achieve the optimal performance of the materials. A carrier density of $\sim10^{19}\ \text{cm}^{-3}$ is commonly regarded as a better concentration for the optimal $ZT$ [10]. Indeed, it is found that this value in monolayer MoSe₂ and WSe₂ can be as large as $\sim10^{21}\ \text{cm}^{-3}$ [13]. On the other side, to maximum $ZT$, the power factors ($\sigma S^{2}$) should be large. A large gap usually has low carrier concentration which can guarantee a large $S$ but also a low $\sigma$. It is believed that narrow band gap semiconductors are more favorable to achieve this.

![](./images/811172489257287681_3.jpg)

Figure 2. Calculated band structures of monolayer (a) ZrSe₂ and (b) HfSe₂. The dashed lines represent the Fermi level, and the arrows point out the extremes of conduction and valence bands. Calculated band gaps are 0.53 eV and 0.68 eV for monolayer ZrSe₂ and HfSe₂, respectively.

### 3.2. Electronic transport

In figure 3, we present the calculated $S$ for the two materials at different temperatures of 400 K, 600 K, 800 K and 1000 K. At first glance, there is not much difference in $S$ for monolayer ZrSe₂ and HfSe₂. An obvious bipolar effect is found in both $p$-type and $n$-type at higher temperatures and low carrier concentrations. As the temperature increases, the peaks of $S$ decline quickly and shift to higher carrier concentrations, which can be attributed to the excited electrons at high temperatures. For a promising $ZT$, the $S$ is usually larger than $200\ \mu\text{V}\ \text{K}^{-1}$ [17, 31]. We find both monolayer ZrSe₂ and HfSe₂ display a high $S$ (larger than $200\ \mu\text{V}\ \text{K}^{-1}$) within a reasonable substantial range of carrier concentrations, regardless of $p$-type or $n$-type. Due to the higher effective mass of electrons, $n$-type $S$ is somewhat superior to that of $p$-type. The optimal $n$-type $S$ at 600 K for monolayer ZrSe₂ and HfSe₂ are $540\ \mu\text{V}\ \text{K}^{-1}$ and $660\ \mu\text{V}\ \text{K}^{-1}$, respectively; higher $S$ values are thus found in HfSe₂.

We depict the power factors in figure 4 with the relaxation time $\tau(\sigma S^{2}/\tau)$. As can be seen, the $n$-type power factors are almost two times higher than the $p$-type ones, which indicates better thermoelectric performance may be obtained from $n$-type doping. For $p$-type, the power factors show a small difference for monolayer ZrSe₂ and HfSe₂, while HfSe₂ exhibits higher values than ZrSe₂ in $n$-type. The power factors

![](./images/811172489257287681_4.jpg)

Figure 3. Calculated Seebeck coefficients for both the p-type and n-type of monolayer (a) ZrSe₂ and (b) HfSe₂ as a function of carrier concentration. Temperatures at 400 K, 600 K, 800 K and 1000 K are considered.

![](./images/811172489257287681_5.jpg)

Figure 4. Power factors as a function of carrier concentration for both p-type and n-type.

also show weak temperature dependence in the optimal carrier concentration range $(10^{19}$-$10^{20}\ \text{cm}^{-3})$, indicating the promising adaptability of the thermoelectric device to temperature. In comparison with previous monolayers MoSe₂ and WSe₂, we find no significant difference in their electronic transport, as their power factors are very similar. Specifically, the $n$-type power factor of monolayer MoSe₂ at 600 K is $\sim 1 \times 10^{11}\ \text{Wm}^{-1}\text{K}^{-2}\text{s}^{-1}$ (carrier density $10^{20}\ \text{cm}^{-3}$) [13], and it is $\sim 1.2 \times 10^{11}\ \text{Wm}^{-1}\text{K}^{-2}\text{s}^{-1}$ in monolayer ZrSe₂. As stated above, the main difference of thermoelectric transport properties between MoS₂ and CdI₂ type TMDCs lies in their thermal effect, and thus it is next interesting to investigate the phononic transport in monolayer ZrSe₂ and HfSe₂. Besides this, it seems like that bulk ZrSe₂ and HfSe₂ with smaller band gaps exhibit higher power factors than their monolayers and reach their optimal values in lower carrier concentrations [17].

### 3.3. Phononic transport

Figure 5(a) shows the calculated phonon spectrums along high-symmetry lines. Interestingly, the phonon spectrums of monolayer ZrSe₂ and HfSe₂ are very distinct from MoS₂ type monolayers. First, the maximum frequencies of the acoustic modes markedly drop to lower values, e.g., 3.7 THz in ZrSe₂ and 3.2 THz in HfSe₂, while they are 5.4 THz in MoSe₂ [13] and 4.8 THz in WSe₂ [13], and even higher at 7.5 THz in MoS₂ [11]. Such lower frequencies suggest the low group velocities of acoustic modes in monolayer ZrSe₂ and HfSe₂. As acoustic modes contribute almost $\sim 80\%$ of $\kappa_l$, thus lower $\kappa_l$ in these two monolayers are expected. The computed group velocities close to $\Gamma$ for the TA (TA')/LA acoustic modes are 425 (1762)/2505 $\text{m}\ \text{s}^{-1}$ for ZrSe₂ and 516 (1622)/2271 $\text{m}\ \text{s}^{-1}$ for HfSe₂, which are very close to those in conventional good thermoelectric materials [32, 33]. Another obvious distinction is that the acoustic modes and optical modes are strongly coupled in monolayer ZrSe₂ and HfSe₂, while there is a wide gap in MoS₂ type monolayers [11, 13]. These modes gathering in a narrower frequency range will increase the scattering rate of phonons and also account for the low $\kappa_l$.

The calculated $\kappa_l$ of monolayer ZrSe₂ and HfSe₂ are shown in figure 5(b). As is expected, our results point to a remarkably low $\kappa_l$ in these two monolayers. The $\kappa_l$ at 300 K are $1.2\ \text{Wm}^{-1}\text{K}^{-1}$ for ZrSe₂ and $1.8\ \text{Wm}^{-1}\text{K}^{-1}$ for HfSe₂, respectively, comparable to those of some popular thermoelectric materials, e.g., Bi₂Te₃ and PbTe [32, 33]. Nevertheless, in MoS₂ type monolayers, the $\kappa_l$ can be as high as dozens [11, 13]. Due to the heavier element with lower frequency in monolayer ZrSe₂ and HfSe₂, the room temperature $\kappa_l$ is also somewhat lower than the recently reported $3.2\ \text{Wm}^{-1}\text{K}^{-1}$ for monolayer ZrS₂ [15]. Despite the many similar group velocities, it can be extracted that monolayer ZrSe₂ instead exhibit lower $\kappa_l$ with respect to HfSe₂. Here, we attribute this mainly to their different phonon scattering rates. As shown in figure 6, the phonon scattering rates of ZrSe₂ are obviously higher than those of HfSe₂, especially in acoustic

![](./images/811172489257287681_6.jpg)

Figure 5. Calculated phonon dispersion relations along high symmetry directions (a); lattice thermal conductivity from 300 K to 1000 K (b); normalized $\kappa_l$ integration with respect to phonon mean free path at room temperature (c).

![](./images/811172489257287681_7.jpg)

Figure 6. Calculated phonon scattering rates for both acoustic and optical modes at 300 K, where the blue and red stars denote monolayer ZrSe₂ and HfSe₂, respectively.

![](./images/811172489257287681_8.jpg)

Figure 7. Evaluated figure of merit of monolayer ZrSe₂ and HfSe₂ for both p-type and n-type. For comparison, the solid red squares denote the previous results of monolayer MoSe₂ at 600 K [13], open red squares of monolayer WSe₂ at 600 K [13], and solid green squares of MoS₂ at 400 K [11].

modes. The average acoustic scattering rate is $1.14\ \mathrm{ps}^{-1}$ for ZrSe₂ while only $0.44\ \mathrm{ps}^{-1}$ for HfSe₂. Higher scattering rates usually come from the anharmonic of the crystal or a large number of allowed three-phonon processes [34]. One can also find that the coupling between acoustic and optical modes is a little stronger in ZrSe₂.

We also present the room temperature cumulative $\kappa_l$ as a function of phonon mean free paths (MFPs) in figure 5(c) in order to discuss the size effect. Significantly short phonon MFPs are observed: all relevant MFPs almost lie below 300 nm, comparable to those in good thermoelectric materials [32, 33]. Calculated MFPs for 50% $\kappa_l$ accumulation are 12 nm for ZrSe₂ and 31 nm for HfSe₂, which also account for the lower $\kappa_l$ in ZrSe₂. The intrinsically short MFPs for ZrSe₂ limit the potential for further reducing $\kappa_l$. Specifically, to reduce $\kappa_l$ significantly below its intrinsic value would require nanostructures with characteristic sizes below $\sim$10 nm.

### 3.4. Figure of merit

We are now in a position to evaluate $ZT$ according to electronic and phononic transport coefficients. As shown in figure 7, the optimal $ZT$ values are found in moderate temperatures for monolayer ZrSe₂ and HfSe₂, and about 0.87 in p-type doping and 0.95 in n-type doping. Available theoretical results of monolayer MoS₂ at 400 K [11] and monolayer Mo(W)Se₂ at 600 K [13] are also presented for comparison. Our results point to an obviously higher $ZT$ in monolayer ZrSe₂ and HfSe₂ due to their much lower $\kappa_l$. Importantly, these optimal $ZT$ values correspond to the best doping concentrations around $\sim$$10^{19}\ \mathrm{cm}^{-3}$, unlike MoS₂ type monolayers in which those shift nearly to $\sim$$10^{21}\ \mathrm{cm}^{-3}$ [11, 13]. Further, there is a slight depression of $ZT$ at higher temperature, indicating the best thermoelectric response is at moderate temperatures. It is quite evident that n-type doping is superior to p-type across the whole range of temperatures.

Before conclusion, it is worth noting the following facts.
(1) Although thermoelectric properties of monolayer TMDCs are widely reported theoretically, experimental realizations are still lacking. Since two-dimensional TMDCs have been successfully prepared [29, 30], it is feasible to realize their thermoelectric response experimentally. (2) Our results, together with the recent report on monolayer $ZrS_2$ [15], highlight the promising thermoelectric performance of $CdI_2$ type monolayer TMDCs. (3) It should be noted that theoretical optimal $ZT$ is not the intrinsic performance of the material, which needs to be realized by reasonable doping. For example, the optimal $ZT$ of $\sim0.99$ in $Bi_2Te_3$ is in fact obtained by alloying with other dopants [10]. A reasonable number of impurities can effectively increase the transport electrons and also introduce scattering to phonons, and as a result be responsible for the enhanced thermoelectric performance.

## 4. Conclusion
In summary, we have explored the thermoelectric properties of $CdI_2$ type monolayer $ZrSe_2$ and $HfSe_2$. We show that the power factors are compatible with $MoS_2$ type TMDCs monolayers. Importantly, we find much low lattice thermal conductivity in monolayer $ZrSe_2$ and $HfSe_2$ due to the low group velocities and high scattering rates, compared to $MoS_2$ type monolayers. As a result, the higher optimal figure of merits are achieved in monolayer $ZrSe_2$ and $HfSe_2$. What is more, because of their narrower band gaps, the optimal figure of merits can be easily realized by a reasonable doping level of $\sim10^{19}\mathrm{cm}^{-3}$ at moderate temperature. It is also evident that better thermoelectric performance can be achieved by $n$-type doping, which is comparable to those of some popular thermoelectric materials. Our results indicate the multiple thermoelectric transport effects in monolayer TMDCs and also their promising thermoelectric applications.

## Acknowledgments
This work was supported by the National Natural Science Foundation of China under Grant Nos. 11474113, by the Natural Science Foundation of Hubei Province under Grant No. 2015CFB419, and by the Fundamental Research Funds for the Central Universities under Grant No. HUST: 2015TS019. W Zhang would like to acknowledge the support from '863'-project (2015AA03130102).

## References
[1] Naguib M, Mochalin V N, Barsoum M W and Gogotsi Y 2014 25th anniversary article: MXenes: a new family of two-dimensional materials *Adv. Mater.* **26** 992-1005

[2] Xu K, Wang Z, Du X, Safdar M, Jiang C and He J 2013 Atomic-layer triangular WSe2 sheets: synthesis and layer-dependent photoluminescence property *Nanotechnology* **24** 465705

[3] Rao C N, Sood A K, Subrahmanyam K S and Govindaraj A 2009 Graphene: the new two-dimensional nanomaterial *Angewandte Chemie* **48** 7752-77

[4] Li H, Zhang Q, Yap C C R, Tay B K, Edwin T H T, Olivier A and Baillargeat D 2012 From bulk to monolayer $MoS_2$: evolution of raman scattering *Adv. Funct. Mater.* **22** 1385-90

[5] Xie Y, Zhang L, Zhu Y, Liu L and Guo H 2015 Photogalvanic effect in monolayer black phosphorus *Nanotechnology* **26** 455202

[6] He J, Kanatzidis M G and Dravid V P 2013 High performance bulk thermoelectrics via a panoscopic approach *Mater. Today.* **16** 166-76

[7] Zhang J, Liu H J, Cheng L, Wei J, Liang J H, Fan D D, Shi J, Tang X F and Zhang Q J 2014 Phosphorene nanoribbon as a promising candidate for thermoelectric applications *Sci. Rep.* **4** 6452

[8] Park K H, Martin P N and Ravaioli U 2016 Electronic and thermal transport study of sinusoidally corrugated nanowires aiming to improve thermoelectric efficiency *Nanotechnology* **27** 035401

[9] Scheidemantel T J, Ambrosch-Draxl C, Thonhauser T, Badding J V and Sofo J O 2003 Transport coefficients from first-principles calculations *Phys. Rev. B* **68** 125210

[10] Snyder G J and Toberer E 2008 Complex thermoelectric materials *Nat. Mater.* **7** 105-14

[11] Jin Z, Liao Q, Fang H, Liu Z, Liu W, Ding Z, Luo T and Yang N 2015 A revisit to high thermoelectric performance of single-layer $MoS_2$ *Sci. Rep.* **5** 18342

[12] Ghosh K and Singisetti U 2015 Thermoelectric transport coefficients in mono-layer $MoS_2$ and $WSe_2$: role of substrate, interface phonons, plasmon, and dynamic screening *J. Appl. Phys.* **118** 135711

[13] Kumar S and Schwingenschlögl U 2015 Thermoelectric response of bulk and monolayer $MoSe_2$ and $WSe_2$ *Chem. Mater.* **27** 1278-84

[14] Li W, Carrete J and Mingo N 2013 Thermal conductivity and phonon linewidths of monolayer $MoS_2$ from first principles *Appl. Phys. Lett.* **103** 253103

[15] Lv H Y, Lu W J, Shao D F, Lu H Y and Sun Y P 2016 Strain-induced enhancement of thermoelectric performance in a $ZrS_2$ monolayer *J. Mater. Chem. C* **4** 4538-45

[16] Zhang W, Huang Z, Zhang W and Li Y 2014 Two-dimensional semiconductors with possible high room temperature mobility *Nano. Res.* **7** 1731-7

[17] Yumnam G, Pandey T and Singh A K 2015 High temperature thermoelectric properties of Zr and Hf based transition metal dichalcogenides: a first principles study *J. Chem. Phys.* **143** 234704

[18] Guo H, Lu N, Wang L, Wu X and Zeng X C 2014 Tuning electronic and magnetic properties of early transition-metal dichalcogenides via tensile strain *J. Phys. Chem. C* **118** 7242-9

[19] Blöchl P E 1994 Projector augmented-wave method *Phys. Rev. B* **50** 17953

[20] Perdew J P, Burke K and Ernzerhof M 1996 Generalized gradient approximation made simple *Phys. Rev. Lett.* **77** 3865

[21] Kresse G and Furthmüller J 1996 Efficient iterative schemes for *ab initio* total-energy calculations using a plane-wave basis set *Phys. Rev. B* **54** 11169-86

[22] Madsen G K H and Singh D J 2006 BoltzTraP. A code for calculating band-structure dependent quantities *Comput. Phys. Commun.* **175** 67-71

[23] Takagi S-I, Toriumi A, Iwase M and Tango H 1994 On the universality of inversion layer mobility in Si MOSFET's: Part I-Effects of substrate impurity concentration *IEEE Trans. Electr. Dev.* **41** 2357

[24] Zhang L-C, Qin G, Fang W-Z, Cui H-J, Zheng Q-R, Yan Q-B and Su G 2016 Tinselenidene: two-dimensional auxetic material with ultralow lattice thermal conductivity and ultrahigh hole mobility *Sci. Rep.* **6** 19830

[25] Li W, Mingo N, Lindsay L, Broido D A, Stewart D A and Katcho N A 2012 Thermal conductivity of diamond nanowires from first principles *Phys. Rev. B* **85** 195436

[26] Li W, Lindsay L, Broido D A, Stewart D A and Mingo N 2012 Thermal conductivity of bulk and nanowire Mg₂SiₓSn₁₋ₓ alloys from first principles *Phys. Rev. B* **86** 174307

[27] Li W, Carrete J, A Katcho N and Mingo N 2014 ShengBTE: a solver of the Boltzmann transport equation for phonons *Comput. Phys. Commun.* **185** 1747–58

[28] Togo A, Oba F and Tanaka I 2008 First-principles calculations of the ferroelastic transition between rutile-type and CaCl₂-type SiO₂ at high pressures *Phys. Rev. B* **78** 134106

[29] Sargar A M, Patil N S, Mane S R, Gawale S N and Bhosale P N 2009 Electrochemical synthesis and characterisation of ZrSe₂ thin films *Int. J. Electrochem. Sci.* **4** 887–94

[30] Yue R *et al* 2014 HfSe₂ thin films: 2D transition metal dichalcogenides grown by molecular beam epitaxy *ACS Nano* **9** 474–80

[31] Sun J and Singh D J 2016 Thermoelectric properties of Mg₂(Ge,Sn): model and optimization of *ZT* *Phys. Rev. Applied* **5** 024006

[32] Hellman O and Broido D A 2014 Phonon thermal transport in Bi₂Te₃ from first principles *Phys. Rev. B* **90** 134309

[33] Qiu B, Bao H, Zhang G, Wu Y and Ruan X 2012 Molecular dynamics simulations of lattice thermal conductivity and spectral phonon mean free path of PbTe: bulk and nanostructures *Comput. Mater. Sci.* **53** 278–85

[34] Carrete J, Mingo N and Curtarolo S 2014 Low thermal conductivity and triaxial phononic anisotropy of SnSe *Appl. Phys. Lett.* **105** 101907