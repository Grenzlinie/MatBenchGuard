# Temperature dependence of exciton–phonon-induced sidebands in arbitrary carbon nanotubes

Evgeny Bobkin* and Ermin Malic

Institut für Theoretische Physik, Nichtlineare Optik und Quantenelektronik, Technische Universität Berlin, Hardenbergstr. 36, 10623 Berlin, Germany

Received 29 April 2011, revised 8 September 2011, accepted 13 September 2011
Published online 7 October 2011

Keywords carbon nanotubes, density matrix theory, excitons, phonons, side band

* Corresponding author: e-mail evgeny.bobkin@tu-berlin.de, Phone: +49 30 314 22848, Fax: +49 30 314 29617

We present a microscopic approach based on the many-body density matrix formalism for the study of exciton–phonon-induced features in absorption spectra of carbon nanotubes with an arbitrary chiral angle and diameter. The introduction of excitonic wave functions already containing the influence of the Coulomb interaction allows us to focus on the contribution of phonons. We observe the formation of pronounced sidebands on both sides of the zero-phonon line. We study the behaviour of exemplary nanotubes belonging to the two semiconducting and one metallic family with respect to the spectral weight transfer from the zero-phonon line to the exciton–phonon sidebands at different temperatures.

© 2011 WILEY-VCH Verlag GmbH & Co. KGaA, Weinheim

## 1 Introduction
Carbon based nanostructures with low dimensionality have novel and unique optical and electronic properties with a rich application potential [1–3]. Besides graphene as a perfect two-dimensional structure [2, 4], carbon nanotubes (CNTs) with diameters in the range of 1 nm have attracted a great interest both in fundamental research and industry [1, 2]. They are ideal systems for the theoretical study of linear and nonlinear optics and ultrafast relaxation dynamics in one-dimensional structures. A thorough microscopic understanding of their optical and electronic properties is a crucial prerequisite for exploiting their application potential.

Several theoretical and experimental studies have reported the importance of excitons in CNTs reporting large excitonic binding energies in the range of 300–400 meV in semiconducting nanotubes [5–11]. Even for metallic nanotubes, where the screening effects are strong, binding energies around 100 meV have been observed [12] and theoretically confirmed [13–16]. Recent experimental papers have also observed the formation of exciton–phonon driven sidebands in the absorption spectra of semiconducting tubes [17–21]. Perebeinos et al. [22] performed calculations based on the *ab initio* evolution of the Bethe–Salpether equation combined with the Su-Schrieffer-Heeger model on the formation of phonon sidebands and investigated the exciton–phonon coupling strength as a function of the diameter in semiconducting CNTs.

In this work, we study the exciton–phonon-induced sidebands for arbitrary CNTs. In particular, we focus on the temperature dependence of the spectral weight transfer from the zero-phonon line to the sidebands due to the coupling with the $\Gamma$-LO phonons. We choose a microscopic approach based on excitonic wave functions [23], which already contain the significant contribution of the Coulomb interaction and allow us to focus on the microscopic description of the phonon-driven sidebands.

## 2 Theoretical model
Our model is based on the following Hamilton operator: $\mathcal{H} = \mathcal{H}_{\text{free}} + \mathcal{H}_{\text{phonon}} + \mathcal{H}_{\text{light-matter}} + \mathcal{H}_{\text{carrier}} + \mathcal{H}_{\text{carrier-phonon}}$, describing the free electrons, the free phonon system, the semi-classical electron–light interaction in the $\boldsymbol{A} \cdot \boldsymbol{p}$ approximation [24], the screened electron–electron coupling, and the electron–phonon interaction, respectively. The electronic band structure is calculated within the tight-binding approximation combined with a zone-folding method [3]. The phonon matrix elements are taken from DFT calculations in Ref. [25]. The Coulomb and electron–light matrix elements are calculated within tight-binding Bloch functions [26, 27, 11].

© 2011 WILEY-VCH Verlag GmbH & Co. KGaA, Weinheim

Having determined the Hamilton operator including the dispersion relations and all coupling elements, we can evaluate the dynamics of an arbitrary microscopic quantity $\mathcal{O}(t)$ within the Heisenberg equation of motion $-i\hbar\partial_t\mathcal{O}(t)=[\mathcal{H},\mathcal{O}]_{-}(t)$. Considering a two band system with one valence ($v$) and one conduction band ($c$), we derive the CNT-Bloch equation for the microscopic polarization $p_{\mathbf{k}}=\langle a_{\mathbf{c}\mathbf{k}}^{+}a_{\mathbf{v}\mathbf{k}}\rangle$ and the occupation probabilities in the valence band $\rho_{\mathbf{k}}^{\mathrm{v}}=\langle a_{\mathbf{v}\mathbf{k}}a_{\mathbf{v}\mathbf{k}}\rangle$ and the conduction band $\rho_{\mathbf{k}}^{\mathrm{c}}=\langle a_{\mathbf{c}\mathbf{k}}^{+}a_{\mathbf{c}\mathbf{k}}\rangle$ [28]. Here, $a_{l\mathbf{k}}$ and $a_{l\mathbf{k}}^{+}$ are the fermionic annihilation and creation operators in the band $l$ and the momentum $\boldsymbol{k}$, respectively. Within the linear optics with a weak optical excitation, the conduction band is assumed to be empty, i.e. $\rho_{\mathbf{k}}^{\mathrm{c}}(t)\approx0$, while the valence band is full, i.e. $\rho_{\mathbf{k}}^{\mathrm{v}}(t)\approx1$. Here, we take into account only the linear terms in polarization $p_{\mathbf{k}}(t)$ and the vector potential $A(t)$ yielding

$$
\begin{aligned}
\partial_{t} p_{\mathbf{k}}(t)=& \frac{-i \varepsilon_{\mathbf{k}}^{\mathrm{cv}}}{\hbar}+\Omega_{\mathbf{k}}(t)-\gamma p_{\mathbf{k}}(t) \\
&-\frac{\mathrm{i}}{\hbar} \sum_{l, \mathbf{q}}\left[g_{\mathbf{q}} S_{\mathbf{k}, \mathbf{q}}^{l c}-g_{\mathbf{q}} S_{\mathbf{k}-\mathbf{q}, \mathbf{q}}^{v l}\right. \\
&\left.+g_{\mathbf{q}}^{*} S_{\mathbf{k}-\mathbf{q}, \mathbf{q}}^{c l *}-g_{\mathbf{q}}^{*} S_{\mathbf{k}, \mathbf{q}}^{l v *}\right]
\end{aligned}
\tag{1}
$$

The equations of motion couple to the phonon-assisted quantities $S_{\mathbf{k},\mathbf{q}}^{l_{1}l_{2}}=\langle a_{l_{1}\mathbf{k}+\mathbf{q}}^{+}a_{l_{2}\mathbf{k}}b_{\mathbf{q}}\rangle$, which need to be determined in a separate equations of motion. In a many-particle system containing the electron-electron interaction, the microscopic polarization $p_{\mathbf{k}}(t)$ is determined by the renormalized band structure $\varepsilon_{\mathbf{k}}^{\mathrm{cv}}=[\varepsilon_{\mathbf{k}}^{\mathrm{c}}-\varepsilon_{\mathbf{k}}^{\mathrm{v}}]-\sum_{\mathbf{k}'}V_{\mathrm{ren}}(\mathbf{k},\mathbf{k}')$ containing the repulsive terms of the Coulomb contribution [29]. The Rabi frequency $\Omega_{\mathbf{k}}(t)=(e_{0}/m_{0})M_{\mathbf{k}}^{\mathrm{cv}}A(t)+(i/\hbar)\sum_{\mathbf{k}'}V_{\mathrm{exc}}(\mathbf{k},\mathbf{k}')p_{\mathbf{k}'}(t)$ includes the attractive excitonic contribution [15, 29, 30]. Here, $e$ is the elementary charge, $m_{\mathrm{e}}$ the vacuum electron mass, and $M_{\mathbf{k}}^{\mathrm{cv}}$ the optical matrix elements [26, 27, 33] oriented along the tube axis.

Since the excitonic effects are essential for understanding the electronic properties of CNTs and since it is numerically very demanding to describe both Coulomb and the electron-phonon interaction, we transform the Bloch equation into an excitonic basis by introducing the $n$th excitonic transition amplitude $P_{n}$ as a new quantity [26]:

$$
p_{\mathbf{k}}=\sum_{n} \Psi_{n \mathbf{k}} P_{n},
\tag{2}
$$

with the excitonic wave functions $\Psi_{n\mathbf{k}}$, where $n$ denotes the excitonic transitions. Within the new basis set, we also introduce the new phonon-assisted densities $T_{n\mathbf{k}}$ and $R_{n\mathbf{k}}$ with
$$
S_{\mathbf{k}, \mathbf{q}}=\sum_{n} \Psi_{n \mathbf{k}+\mathbf{q} / 2} T_{n,-\mathbf{q}} ;
$$
$$
S_{\mathbf{k}, \mathbf{q}}^{*}=\sum_{n} \Psi_{n \mathbf{k}+\mathbf{q} / 2} R_{n, \mathbf{q}},
$$
which describe phonon-induced interband processes. The intraband contributions are negligible within the limit of linear optics.

Inserted into Eq. (1), we obtain the new simplified Bloch equation:

$$
\begin{aligned}
i \hbar \partial_{t} P_{n}(t)=& \varepsilon_{n} P_{n}(t)-A_{n}(t)-i \hbar \gamma P_{n}(t) \\
&+\sum_{n^{\prime} \mathbf{q}} g_{n n^{\prime}}(\mathbf{q})\left\{T_{n^{\prime} \mathbf{q}}(t)+R_{n^{\prime} \mathbf{q}}(t)\right\}.
\end{aligned}
\tag{3}
$$

Here, $\varepsilon_{n}$ denotes the excitonic energy band structure and the effective carrier-light coupling is given by $A_{n}(t)=i\hbar(e/m_{\mathrm{e}})\sum_{\mathbf{k}}\Psi_{n\mathbf{k}}^{*}A(t)M_{\mathbf{k}}^{\mathrm{cv}}$ and the effective exciton-phonon matrix elements determined by

$$
g_{n n^{\prime}}(\mathbf{q})=\sum_{\mathbf{k}} \Psi_{n \mathbf{k}}^{*}\left(\Psi_{n^{\prime} \mathbf{k}+\mathbf{q} / 2}-\Psi_{n^{\prime} \mathbf{k}-\mathbf{q} / 2}\right)\left|g_{\mathbf{q}}\right|.
\tag{4}
$$

The excitonic polarization amplitudes $P_{n}$ in Eq. (3) couple to the LO-phonon driven effective densities $R_{n\mathbf{q}}$ and $T_{n\mathbf{q}}$. The corresponding equations of motion read:

$$
\begin{aligned}
i \hbar \partial_{t} T_{n \mathbf{q}}(t)=& \left(\varepsilon_{n \mathbf{q}}+\hbar \omega_{\mathrm{LO}}\right) T_{n \mathbf{q}}(t)-i \hbar \gamma_{\mathrm{s}} T_{n \mathbf{q}}(t) \\
&+\left(1+N_{\mathbf{q}}\right) \sum_{n^{\prime}} g_{n n^{\prime}}(\mathbf{q}) P_{n^{\prime}}(t),
\end{aligned}
\tag{5}
$$

$$
\begin{aligned}
i \hbar \partial_{t} R_{n \mathbf{q}}(t)=& \left(\varepsilon_{n \mathbf{q}}-\hbar \omega_{\mathrm{LO}}\right) R_{n \mathbf{q}}(t)-i \hbar \gamma_{\mathrm{s}} R_{n \mathbf{q}}(t) \\
&+N_{\mathbf{q}} \sum_{n^{\prime}} g_{n n^{\prime}}(\mathbf{q}) P_{n^{\prime}}(t),
\end{aligned}
\tag{6}
$$

with the phonon-renormalized excitonic energy $\varepsilon_{n\mathbf{q}}$ and the I-LO phonon energy $\hbar\omega_{\mathrm{LO}}$. The phonon occupation density $N_{\mathbf{q}}=\langle b_{\mathbf{q}}^{+}b_{\mathbf{q}}\rangle$ is treated within the bath approximation and is therefore represented by the Bose-Einstein distribution. The new set of Eqs. (3),(5) and (6) already contains the excitonic contributions via the new basis functions allowing us to focus on the exciton-phonon interaction. Since the most spectral weight is concentrated in the first excitonic transition [15], we evaluate Eq. (2) within the one-exciton limit, i.e. $n=1$. Then, the excitonic wave function is proportional to the stationary distribution of the microscopic polarization $p_{\mathbf{k}}$ in the reciprocal space and can therefore be determined by numerically solving the equation of motion for $p_{\mathbf{k}}$.

Figure 1 illustrates the square of the absolute value of the excitonic wave function for three exemplary nanotubes [(20,0), (21,0) and (19,0)] representing the three CNT families [31]. The pronounced oscillations of the wave functions reflect the behaviour of the stationary excitonic distribution of the microscopic polarization. The maximal value for $|\Psi(k)|^{2}$ is reached for a vanishing wave momentum corresponding to the transition at the band minimum at the $\Gamma$ point. Furthermore, the smaller the tube diameter, the stronger is the Coulomb interaction and the larger is the square of the wave function.

## 3 Results
By evaluating the CNT-Bloch equation for the microscopic polarization, cp. Eq. (3), we are able to

![](./images/813371728628547585_1.jpg)

Figure 1 (online colour at: www.pss-b.com) Square value of the excitonic wave function of the metallic (21,0), and the +1 and the −1 semiconducting (19, 0) and (20, 0) tube corresponding to the first excitonic transition $E_{11}$.

calculate the absorption coefficient

$$
\alpha(\omega)=\omega \operatorname{Im} \chi(\omega) \propto \sum_{\mathbf{k}} \operatorname{Re} \frac{\left\{p_{\mathbf{k}}(\omega) M_{\mathbf{k}}^{\mathrm{vc}}\right\}}{\{\omega A(\omega)\}},
\tag{7}
$$

with the optical susceptibility $\chi(\omega)$ containing the frequency- and temperature-dependent optical properties of the investigated nanotube. Figure 2 illustrates the absorption spectrum of the exemplary metallic (21,0) and the semiconducting (19,0) CNT at room temperature and at 700 K, respectively. It contains the microscopically calculated exciton and phonon features. The zero-phonon line is characterized by a symmetric Lorentzian peak. At room temperature, we find one pronounced phonon sideband at the higher energy side of the zero-phonon line. At higher temperatures, the phonon occupation increases enabling phonon absorption processes. As a result, at 700 K we observe two sidebands located 200 meV on both sides of the zero-phonon line corresponding to the energy of the LO-phonons. The formation of sidebands is ascribed to the strong exciton–phonon coupling. The strongly pronounced peak on the higher energy side arises from the phonon emission, which occurs at all temperatures, since it is determined by $(1+N_{\mathbf{q}})$, cp. Eq. (5). In contrast, the less pronounced sideband at the lower energy side is assigned to the phonon absorption, which is proportional to $N_{\mathbf{q}}$, cp. Eq. (6) and therefore vanishes at low temperatures. Our calculations suggest that semiconducting and metallic tubes show a similar exciton–phonon coupling resulting in comparable phonon replica in the absorption spectrum.

The coupling strength of the exciton–phonon interaction causes (i) a transfer of the spectral weight from the zero-phonon line to the side peaks and (ii) a polaron shift of some tens of meV, which depends on the diameter of the nanotube. We observe an increase of the coupling with a decreasing diameter. This behaviour can be understood by comparing the exciton–phonon matrix elements $g_{nn'}(\mathbf{q})$ for CNTs with a different diameter. The coupling strength is determined by the electron–phonon matrix element [cp. Eq. (4)], which explicitly depends on the diameter $(\propto 1/d)$, and the excitonic wave function, which implicitly contains the diameter dependence via the included Coulomb interaction. As shown in Fig. 1, the maximal value of $|\Psi(k)|^{2}$ decreases for tubes with a large diameter.

The transfer of the spectral weight from the zero-phonon line to the sidebands shows a strong temperature dependence, cp. Fig. 3. The lower-energy sideband does not occur up to a temperature of about 500 K. Then, it strongly increases reaching values of about 5–10% at 2500 K of the spectral weight of the zero-phonon line. The most pronounced sideband is observed for the (19,0) CNT, which has the smallest diameter. The higher-energy side peak already occurs at $T=0$ K, since it arises from the processes of

![](./images/813371728628547585_2.jpg)

Figure 2 (online colour at: www.pss-b.com) Absorption spectrum of an exemplary metallic and semiconducting CNT containing the microscopically included exciton and phonon features at two different temperatures. The phonon-induced sidebands are observed at 200 meV below and above the zero-phonon line, which corresponds to the energy of the longitudinal optical phonons.

![](./images/813371728628547585_3.jpg)

Figure 3 (online colour at: www.pss-b.com) The temperature dependence of the spectral weight transfer from the zero-phonon line to the sidebands for the semiconducting (19,0) and (20,0) tube (belonging to the +1 and the −1 CNT family [31]) and the metallic (21,0) tube computed based on (a) absorption coefficient $\alpha(\omega)$. In (b), $\omega \alpha(\omega)$ illustrates shortly that the crossing in (a) arises from the prefactor in Eq. (7). Solid (dashed) lines correspond to the sideband at the lower $\omega_{n}-\omega_{\mathrm{LO}}$ (higher $\omega_{n}+\omega_{\mathrm{LO}}$) energy side.

the phonon emission. Interestingly, the values for the spectral weight transfer for the lower- and higher-energy sidebands cross at a certain temperature, cp. Fig. 3a. Our calculations reveal that this effect is due to the $1/\omega$-prefactor in the absorption coefficient, cp. Eq. (7). Figure 3b illustrates that in the case of $\omega\alpha(\omega)$ no crossing occurs. Note that the exciton dissociation expected at high temperatures [32] might modify to some extent the temperature dependence of the phonon-induced sidebands. We expect a weaker coupling of phonons with free carriers and a smaller spectral weight transfer from the zero-phonon line to the sidebands [22].

## 4 Conclusions
We have presented a theoretical study of the temperature-dependence of sidebands in the exciton-phonon absorption spectra of semiconducting and metallic nanotubes. Our approach is based on the many-body density matrix framework yielding microscopic CNT-Bloch equations, which can be applied to a CNT with an arbitrary chiral angle and a wide range of diameters. We observed that the exciton–phonon coupling leads to the formation of pronounced phonon sidebands on both sides of the zero-phonon line. The transfer of the spectral weight shows a strong temperature dependence. Furthermore, nanotubes with a smaller diameter show a strong exciton–phonon coupling resulting in more pronounced sidebands.

### Acknowledgements
We acknowledge financial support by the Deutsche Forschungsgesellschaft through SFB 658. Furthermore, we thank A. Knorr for fruitful discussions.

### References
[1] A. Jorio, G. Dresselhaus, and M. S. Dresselhaus, Carbon Nanotubes: Advanced Topics in the Synthesis, Structure, Properties and Applications, first ed. (Springer, Berlin, 2007).

[2] F. Bonaccorso, Z. Sun, T. Hasan, and A. C. Ferrari, Nature Photonics **4**(9), 611–622 (2010).

[3] S. Reich, C. Thomsen, and J. Maultzsch, Carbon Nanotubes: Basic Concepts and Physical Properties, first ed. (Wiley-VCH Verlag, Weinheim, 2004).

[4] T. Winzer, A. Knorr, and E. Malic, Nano Lett. **10**(12), 4839–4843 (2010).

[5] J. Maultzsch, R. Pomraenke, S. Reich, E. Chang, D. Prezzi, A. Ruini, E. Molinari, M. S. Strano, C. Thomsen, and C. Lienau, Phys. Rev. B **72**(24), 241402 (2005).

[6] F. Wang, G. Dukovic, L. E. Brus, and T. F. Heinz, Science **308**(5723), 838–841 (2005).

[7] V. Perebeinos, J. Tersoff, and P. Avouris, Phys. Rev. Lett. **92**(25), 257402 (2004).

[8] E. Chang, G. Bussi, A. Ruini, and E. Molinari, Phys. Rev. B **72**(19), 195423 (2005).

[9] Z. Wang, D. Psiachos, R. F. Badilla, and S. Mazumdar, J. Phys.: Condens. Matter **21**(9), 095009 (2009).

[10] E. Malic, M. Hirschulz, S. Reich, and A. Knorr, Phys. Status Solidi RRL **3**(6), 196–198 (2009).

[11] M. Hirschulz, F. Milde, E. Malic, S. Butscher, C. Thomsen, S. Reich, and A. Knorr, Phys. Rev. B **77**(3), 035403 (2008).

[12] F. Wang, D. J. Cho, B. Kessler, J. Deslippe, P. J. Schuck, S. G. Louie, A. Zettl, T. F. Heinz, and Y. R. Shen, Phys. Rev. Lett. **99**(22), 227401 (2007).

[13] C. D. Spataru, S. Ismail-Beigi, L. X. Benedict, and S. G. Louie, Phys. Rev. Lett. **92**(7), 077402 (2004).

[14] J. Deslippe, C. D. Spataru, D. Prendergast, and S. G. Louie, Nano Lett. **7**(6), 1626–1630 (2007).

[15] E. Malic, J. Maultzsch, S. Reich, and A. Knorr, Phys. Rev. B **82**(3), 035433 (2010).

[16] E. Malic, J. Maultzsch, S. Reich, and A. Knorr, Phys. Rev. B **82**(11), 115439 (2010).

[17] F. Plentz, H. B. Ribeiro, A. Jorio, M. S. Strano, and M. A. Pimenta, Phys. Rev. Lett. **95**(24), 247401 (2005).

[18] O. N. Torrens, M. Zheng, and J. M. Kikkawa, Phys. Rev. Lett. **101**(15), 157401 (2008).

[19] Y. Murakami, B. Lu, S. Kazaoui, N. Minami, T. Okubo, and S. Maruyama, Phys. Rev. B **79**(19), 195407 (2009).

[20] G. Yu, Q. Liang, Y. Jia, and J. Dong, J. Appl. Phys. **107**(2), 024314 (2010).

[21] S. Berciaud, C. Voisin, H. Yan, B. Chandra, R. Caldwell, Y. Shan, L. E. Brus, J. Hone, and T. F. Heinz, Phys. Rev. B **81**(4), 041414 (2010).

[22] V. Perebeinos, J. Tersoff, and P. Avouris, Phys. Rev. Lett. **94**(2), 027402 (2005).

[23] T. Östreich, N. Donlagic, C. Wöhler, and K. Schönhammer, Phys. Status Solidi B **206**, 205–217 (1998).

[24] H. Haug and S. W. Koch, Quantum Theory of the Optical and Electronic Properties of Semiconductors, fourth ed. (World Scientific Publishing, Singapore, 2005).

[25] S. Piscanec, M. Lazzeri, J. Robertson, A. C. Ferrari, and F. Mauri, Phys. Rev. B **75**(3), 035427 (2007).

[26] A. Grüneis, R. Saito, G. G. Samonidze, T. Kimura, M. A. Pimenta, A. Jorio, A. G. S. Filho, G. Dresselhaus, and M. S. Dresselhaus, Phys. Rev. B **67**(16), 165402 (2003).

[27] E. Malic, M. Hirschulz, F. Milde, A. Knorr, and S. Reich, Phys. Rev. B **74**(19), 195431 (2006).

[28] E. Malic, M. Hirschulz, F. Milde, Y. Wu, J. Maultzsch, T. F. Heinz, A. Knorr, and S. Reich, Phys. Status Solidi B **244**(11), 4240–4243 (2007).

[29] E. Malic, M. Hirschulz, F. Milde, M. Richter, J. Maultzsch, S. Reich, and A. Knorr, Phys. Status Solidi B **245**, 2155–2158 (2008).

[30] E. Malic, E. Bobkin, T. Winzer, C. Köhler, T. Watermann, M. Hirschulz, and A. Knorr, Proc. SPIE **7937**, 79371R (2011).

[31] C. Thomsen and S. Reich, Raman scattering in carbon nanotubes, in: Light Scattering in Solids IX, Topics in Applied Physics (Springer, Berlin, 2006).

[32] P. May, H. Telg, G. Zhong, J. Robertson, C. Thomsen, and J. Maultzsch, Phys. Rev. B **82**, 195412 (2010).

[33] E. Malic, M. Hirschulz, F. Milde, Y. Wu, J. Maultzsch, T. Heinz, A. Knorr, and S. Reich, Phys. Rev. B **77**, 045432 (2008).