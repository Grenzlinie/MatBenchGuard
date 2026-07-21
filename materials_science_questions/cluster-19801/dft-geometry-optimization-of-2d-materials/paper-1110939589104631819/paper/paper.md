# Topological blocking at the Bi(111) surface due to surface relaxation

Kazuki Koie, $^{1,2}$ Rikako Yaguchi, $^{1}$ and Yuki Fuseya $^{1,3}$

$^{1}$ Department of Engineering Science, University of Electro-Communications, Tokyo 182-8585, Japan
$^{2}$ Department of Physics, Kobe University, Kobe, Japan
$^{3}$ Department of Physics, Kobe University, Kobe 657-8501, Japan

(Dated: March 24, 2025)

The topological characteristics of Bi and its alloys with Sb have fueled intense debate since the prediction of three-dimensional topological insulators. However, a definitive resolution has not been reached to date. Here, we provide theoretical evidence that surface relaxation conceals the underlying bulk topology of pure Bi. Using density functional theory calculations for thin Bi(111) films (up to 17 bilayers), we first demonstrate a substantial inter-bilayer expansion near the surface. Motivated by this finding, we extend our analysis to thick Bi(111) films (up to 250 bilayers) incorporating relaxation layers, within the framework of a relativistic empirical tight-binding model. Our results reveal that these relaxation layers topologically block the emergence of surface states and significantly suppress the one-particle spectrum of surface states, thereby obscuring the experimental identification of Bi's topological properties. This phenomenon, which we term "topological blocking", provides crucial insights into the long-standing difficulty of observing surface states of Bi(111) at the $\bar{M}$ point. Furthermore, it establishes a framework for understanding and predicting the topological behavior in systems where surface relaxation disrupts the bulk-edge correspondence.

Since its prediction as a topological insulator, bismuth (Bi) alloyed with antimony (Sb) has gained attention in the study of topological materials [1]. The surface states of Bi and BiSb have been intensively explored both experimentally [2-12] and theoretically [13-17], yet their precise topological nature remains unclear. A fundamental question centers around the surface states at the $\bar{M}$ point in the (111)-surface Brillouin zone (corresponds to the $L$ point in the bulk Brillouin zone), with profound implications for topological characterization.

Theoretically, various studies have consistently reached the same conclusions [15, 18-24]. For pure bulk Bi, the conduction band at the $L$ point is symmetric, whereas the valence band is antisymmetric, indicating a trivial $Z_2$ topological invariant [1]. (We denote this band order as $L_s/L_a$.) All density-functional-theory (DFT) support this band order. When pure Bi is topologically trivial, the two surface states (S1 and S2) cross linearly (i.e., zero-gap Dirac-like surface state) at the $\bar{M}$ point, as confirmed by numerical [1, 13] and analytical [16] studies. (It is worth noting that the existence condition for topological surface states at the $\bar{M}$ point in Bi is opposite to that of ordinary topological insulators, where the nontrivial topology is manifested by the presence of Dirac-like surface states [16, 17].) In contrast, if Bi is topologically nontrivial, a finite gap opens between the two surface states. Alternatively, gap opening can occur by the interference between opposite surface states [25-29]. According to such interference scenario, a sizable surface gap can appear even when Bi is topologically trivial [16, 17], suggesting a surface-sensitive topological nature of Bi.

Experimentally, however, a clear division persists. Angle-resolved photoemission spectroscopy (ARPES) measurements often indicate a nontrivial topology of Bi, as evidenced by a surface gap at the $\bar{M}$ point [8, 10-12], except for a few reports (e.g., [9]). In contrast, scanning tunneling microscopy and transport studies suggest a trivial topology supported by a signature for the higher-order topology in Bi [30, 31], which is nothing but evidence for the trivial $Z_2$ topology. Thus, the evidence for the higher-order topology deepens the discrepancy in interpretation. Hereafter, we use the term "trivial" or "nontrivial" to indicate the lowest-order topology characterized by the $Z_2$ topological invariance.

A key reason for the abovementioned discrepancy may be attributed to the remarkable sensitivity of the topology of Bi to the lattice constant. Only a change of approximately 0.4% in the lattice constant is sufficient to invert the bands at the $L$ point, triggering a topological transition from trivial to nontrivial [15]. For example, a strain-induced topological transition has been demonstrated in ultrathin Bi(111) on $Bi_2Te_3$(111) substrate [32]. Furthermore, temperature-driven topological transitions owing to thermal lattice distortion have been shown in ARPES measurements [33].

In this study, we revealed a pronounced expansion of inter-bilayer distance near the surface of Bi(111), and such an expanded surface layer topologically prevents surface states from appearing. These insights into the elusive topological characteristics of Bi represent a critical step toward resolving the outstanding debate mentioned above.

In general, the interlayer distance can be changed by surface relaxation [38]. To examine how surface relaxation occurs in Bi, we investigated the lattice displacement in Bi(111) films using DFT with the BAND software from the Amsterdam Modeling Suite [39, 40]. Structural optimization was performed using a fast inertial relaxation engine [41] with the Perdew-Burke-Ernzerhof

![](./images/1110939589104631819_1.jpg)

FIG. 1. (a) Inter-bilayer spacing of Bi(111) film for 3-17 bilayer (BL) as a function of the distance $z$ from the surface computed using DFT with structural optimization. The inter-bilayer spacing of bulk Bi is 2.35 Å[34, 35]. (b) Energy eigenvalues of 100-BL Bi(111) based on the Liu-Allen model with surface potential [36, 37] for $\Delta d=0$.

exchange-correlation functional from LibXC [42], double-zeta-polarized basis sets, and numerical orbitals with a small frozen core. Relativistic effects were incorporated using the zeroth-order regular approximation (ZORA) [43]. Figure 1(a) shows inter-bilayer spacing $d$ as a function of the distance $z$ from the surface for various film thicknesses (3-17 bilayers—BL), incorporating the ZORA scalar relativistic effects. (We have confirmed that for thin bilayers, the results obtained with scalar relativistic effects qualitatively agree with those obtained using fully relativistic spin-orbit coupling.) Near the surface, inter-bilayer spacing expands by up to 6% relative to central layer spacing $d_0$, averaging $\Delta d/d_0 \sim 3\%$ across approximately five surface bilayers, while the atoms remain fixed along the in-plane direction. Such a significant inter-bilayer expansion for Bi(111) films is consistent with the previous reports [32, 34, 44]. Figure 1(a) clearly demonstrates that the inter-bilayer expansion behavior converges for thicknesses exceeding 11 BL. This convergence is reasonable, as the relaxation layer has a thickness of 5 BL. Consequently, the properties of the relaxation layer should remain robust in much thicker films.

Prior to discussing the main findings of this work, we briefly outline the surface states of Bi(111). Figure 1(b) presents the eigenvalues for a 100-BL Bi(111) film without inter-bilayer modulation, calculated based on the Liu-Allen relativistic empirical tight-binding model [16, 36, 37, 45], exhibiting exceptional agreement with experimental results for Bi. We employed the surface potential introduced by Saito *et al.* [36, 37], being consistent with ARPES measurements [8-10, 46-48]. Consistent with other DFT results [15, 18-24], the Liu-Allen model identifies pure Bi as topologically *trivial*, characterized by the $L_s/L_a$ configuration. The surface states S1 and S2 merge into the valence band at the $\bar{\Gamma}$ point and reside within the bulk bandgap at the $\bar{M}$ point. The overall dispersion of the surface states remains qualitatively unchanged even when the bulk band at the $L$-point is inverted due to the inter-bilayer expansion, suggesting that inter-bilayer expansion near the surface does not lead to an immediately discernible modification of the surface states. However, a profound alteration, obscured in the eigenvalue plot, emerges upon examining the wavefunction characteristics or the one-particle spectral function.

![](./images/1110939589104631819_2.jpg)

FIG. 2. (a) Illustration of film considering surface relaxation with expanded inter-bilayer spacing ($\Delta d/d_0>0$) for $z \leq m_{\text{sur}}$. (b) Probability distribution $|\psi(z)|^2$ with surface relaxation ($n_{\text{tot}}=100$ and $m_{\text{sur}}=10$) near the surface ($z \leq 20$ BL) of surface state S1. Entire range plot $1 \leq z \leq 100$ BL is given for surface states (c) S1 and (d) S2.

To examine the effects of surface relaxation, we considered a Bi(111) film with a total thickness of $n_{\text{tot}}$ BL, where the inter-bilayer distance was relaxed for $m_{\text{sur}}$ BL on one side of the surface, and the remaining inter-bilayer distance is unchanged from the bulk value, as depicted in Fig. 2(a). Figure 2 (b)-(d) shows $\Delta d$-dependences of probability distribution $|\psi(z)|^2$ of $n_{\text{tot}}=100$ with $m_{\text{sur}}=10$ for surface states S1 [Fig. 2(c)] and S2 [Fig. 2(d)], where $d_0$ is the inter-bilayer spacing for bulk used in the Liu-Allen model. (Using the general relationship between interatomic matrix element $V$ and its distance $V \propto d^{-2}$ [45], we estimated the changes in $\Delta d$ using $\Delta d/d_0=(1+\Delta V/V_0)^{-1/2}-1$.) In addition, $|\psi(z)|^2$ for S1 near the surface with $z \leq 20$ BL is shown in Fig. 2 (b). There is a characteristic value for the inter-bilayer spacing, $\Delta d_c$, at which the spatial distribution of $|\psi(z)|^2$ undergoes a drastic transformation, indicated by the vertical dashed lines. (The origin of $\Delta d_c$ will be elucidated in a later discussion, where $\Delta d_c/d_0=0.34$ % will be determined.) For $\Delta d \lesssim \Delta d_c$, the wavefunction exists on both surfaces, $z=1$ and 100 BL. In contrast, when $\Delta d \gtrsim \Delta d_c$, the wavefunction shifts beneath the surface layer, demonstrating that the surface states effectively migrate below the relaxation layer. Thus, the relaxation layer acts as a barrier that prevents the surface state from appearing,

![](./images/1110939589104631819_3.jpg)

FIG. 3. Spatial one-particle spectrum $A(\boldsymbol{k}_{\parallel},z,\varepsilon)$ of 100-BL Bi(111) with surface relaxation ($n_{\text{tot}}=100$ and $m_{\text{sur}}=10$) for (a) $\Delta d/d_0=0.2\%$ (surface layers are trivial) and (b) $\Delta d/d_0=3\%$ (surface layers are nontrivial).

effectively blocking its manifestation at the surface.

The following spatial one-particle spectral function, $A(\boldsymbol{k}_{\parallel},z,\varepsilon)$, can provide further insights into this blocking effect:

$$
A(\boldsymbol{k}_{\parallel},z,\varepsilon)=-\frac{1}{\pi}\text{Tr}_{z}\text{Im}G^{R}(\boldsymbol{k}_{\parallel},z,\varepsilon), \tag{1}
$$

where $G^{R}(\boldsymbol{k}_{\parallel},z,\varepsilon)=\left[\varepsilon-\mathcal{H}(\boldsymbol{k}_{\parallel},z)+i\Sigma''\right]^{-1}$ is the retarded Green function, $\Sigma''$ denotes the imaginary part of the self-energy, and $\text{Tr}_{z}$ is the trace over $G^{R}$ for a particular $z$-th BL of interest [37]. The spatial one-particle spectrum at the $\bar{M}$ point is shown in Fig. 3 for $\Delta d/d_0=0.2\%$ [Fig. 3(a)] and $\Delta d/d_0=3\%$ [Fig. 3(b)] with $\Sigma''=0.03$ eV. For $\Delta d/d_0=0.2\%$ ($<\Delta d_c/d_0$), surface states S1 and S2 are observed on both surfaces at $z=1$ and 100 BL. By contrast, for $\Delta d/d_0=3\%$ ($>\Delta d_c/d_0$), S1 and S2 exist on one side of the surface ($z=100$ BL) but not on the other side ($z=1$ BL). This result clearly indicates that the relaxation layer of $z=1$-$10$ BL blocks the two surface states only for $\Delta d/d_0=3\%$, and does not for $\Delta d/d_0=0.2\%$. The absence of a surface state blocked by the relaxation layer results in the absence of photoemission intensity.

A comparison of one-particle spectra at the surface ($z=1$ BL) between relaxed ($\Delta d/d_0=3\%$) and unrelaxed ($\Delta d=0$) surface layers is shown in Fig. 4 for thickness $n_{\text{tot}}$ varying from 100 to 250 and keeping $m_{\text{sur}}=10$. The impact of the blocking can be estimated using the blocking ratio, which is the ratio of one-particle spectra with and without relaxed layers. The blocking ratio of the peak intensity is 0.49 for a 100 BL and 0.50 for 150-250-BL films, indicating that the effect is independent of the film thickness. Therefore, the blocking persists even in thick Bi(111) slabs. Although the peak position remains detectable with $m_{\text{sur}}=10$, the intensity of the surface states is substantially weaker than that of the bulk state. Consequently, the blocking hinders the detection of the surface states of Bi(111), masking evidence of the topological nature of Bi.

![](./images/1110939589104631819_4.jpg)

FIG. 4. One-particle spectra at $\bar{M}$ point with and without surface expansion. The total thickness, $n_{\text{tot}}$, varies from 100 to 250, whereas the thickness of the surface relaxation layer is set to $m_{\text{sur}}=10$. The blocking ratio is 0.49 for a 100-BL film and 0.50 for a 150-250-BL film.

![](./images/1110939589104631819_5.jpg)

FIG. 5. Energy shift at $L$ point of bulk Bi as a function of inter-bilayer expansion $\Delta d=d-d_0$ using the Liu-Allen model [45].

Let us now elucidate why the relaxation layer obstructs the emergence of surface states only for $\Delta d \gtrsim \Delta d_c$. Figure 5 presents the energy shift of the conduction and valence bands at the $L$ point of bulk Bi as a function of $\Delta d$. As $\Delta d$ increases, $|E_g|$ decreases linearly, leading to a band inversion at $\Delta d_c/d_0 = 0.34\%$ ($\Delta V_c/V_0 = -0.68\%$). This band inversion drives a transition in the three-dimensional $Z_2$ topological invariants $(\nu_0; \nu_1\nu_2\nu_3)$ from $(0; 000)$ to $(1; 111)$, signifying a transition from a trivial to a nontrivial topology [1, 13]. In general, such a topological transition becomes less evident as the film thickness decreases, at least when considering the energy profile of the surface states [16, 17]. However, its signature persists as a crossover in the wave function distribution $|\psi(z)|^2$ (Fig. 2). Remarkably, this crossover in the relaxation layer (white dashed lines in Fig. 2) occurs at nearly the same position as the bulk band inversion point $\Delta d_c/d_0 = 0.34$ %. This striking agreement strongly suggests that the qualitative change in $|\psi(z)|^2$, and the resultant blocking effect, originates from the topological transition.

For the trivial $L_s/L_a$ configuration, it has been analytically shown that two Dirac-like surface states must exist within the bandgap at the $\bar{M}$ point [16]. In contrast, for the nontrivial $L_a/L_s$ configuration, surface states are strictly prohibited at the $\bar{M}$ point. This prohibition underlies the observed blocking effect, whereby the emergence of surface states is suppressed when $\Delta d \gtrsim \Delta d_c$.

Conseqently, the blocking effect is inherently rooted in the topological properties of Bi. For $\Delta d \gtrsim \Delta d_c$, the relaxation layer effectively acquires the characteristics of a topologically nontrivial state, leading to the supression of surface states. This mechanism constitutes the essence of the "topolgical blocking effect".

While our results mainly consider $m_{\rm sur} = 10$, we checked that the topological blocking persists for thinner relaxation layers, such as $m_{\rm sur} = 5$. As inter-bilayer expansion $\Delta d$ varies as a function of $z$, as shown in Fig. 1(a), the uniform $\Delta d$ values in our analysis may slightly overestimate topological blocking. However, experimental observations report an inter-bilayer expansion of approximately $\Delta d/d_0 = 2$–3% [32, 34], which is substantially larger than critical threshold $\Delta d_c/d_c = 0.34\%$ and is enough to induce the topological transition. Thus, the observed topological blocking mechanism is highly plausible and relevant to real systems.

Owing to restrictions on computational resources, we combined DFT for structural optimization and the tight-binding method for obtaining the probability distribution and spatial one-particle spectrum. The DFT-based computation of $A(\boldsymbol{k}_\parallel, z, \varepsilon)$ with structural optimization may allow to verify topological blocking directly. This verification will be explored in future work.

In conclusion, we have unveiled a novel mechanism that can obscure a material's topological nature: the topological blocking effect.

The key findings of this study are as follows: (i) A pronounced inter-bilayer expansion was observed near the surface of Bi(111) films. (ii) The relaxation layer effectively blocked the emergence of surface states and significantly suppressed the one-particle spectrum of surface states in Bi(111). (iii) The blocking effect occurs only for $\Delta d \gtrsim \Delta d_c$, where the boundary value of $\Delta d_c$ exhibits remarkable agreement with the topological transition point for the bulk Bi. Based on these findings, we conclude that the blocking effect originates from the nontrivial topological nature in the relaxation layer. Thus, even if the bulk of material possesses the topologically trivial character, its topological signature at the surface can be masked by the topological blocking effect within the relaxation layer. This blocking effect persisted even in thick slabs, complicating the experimental identification of topologically trivial nature in Bi. This results in a spontaneous breaking of the bulk–edge correspondence.

Our proposal that surface relaxation can lead to the spontaneous breaking of the bulk–edge correspondence is not limited to Bi but can be broadly applied to other systems. Conventional bulk–edge correspondence assumes that the crystal structure near the surface remains identical to that of the bulk. However, it is well-established that the surface undergoes structural modifications, such as surface relaxation and reconstruction, deviating from the bulk crystal structure [38, 49]. This fundamental mismatch challenges the validity of the bulk–edge correspondence in real systems. Surface relaxation does not universally disrupt the bulk–edge correspondence. In some cases, surface relaxation may leave the band structure qualitatively unchanged. However, in many topological materials, such as Sb, PbTe, and SnTe [50], the bulk band structure is poised near a topological transition. In such systems, even modest surface relaxation can induce a qualitative change in the electronic structure, thereby breaking the bulk–edge correspondence. Bismuth is an exemplary material for observing this phenomenon because of its small band gap and large inter-bilayer expansion.

The abovementioned insights can lead to establish a crucial framework for interpreting experimental data where the bulk–edge correspondence alone may be insufficient, thus paving the way for a deeper understanding of the topological properties of materials with surface relaxation effects.

We thank Y. Asaka for the fruitful discussions. This work was supported by the Japan Society for the Promotion of Science [Grants No. 23H00268, 23H04862 and 22K18318].

[1] L. Fu and C. L. Kane, Topological insulators with inversion symmetry, Phys. Rev. B 76, 045302 (2007).
[2] D. Hsieh, D. Qian, L. Wray, Y. Xia, Y. S. Hor, R. J.

Cava, and M. Z. Hasan, A topological dirac insulator in a quantum spin hall phase, Nature **452**, 970 (2008).

[3] D. Hsieh, Y. Xia, L. Wray, D. Qian, A. Pal, J. H. Dil, J. Osterwalder, F. Meier, G. Bihlmayer, C. L. Kane, Y. S. Hor, R. J. Cava, and M. Z. Hasan, Observation of un- conventional quantum spin textures in topological insu- lators, Science **323**, 919 (2009).

[4] T. Hirahara, Y. Sakamoto, Y. Saisyu, H. Miyazaki, S. Kimura, T. Okuda, I. Matsuda, S. Mu- rakami, and S. Hasegawa, Topological metal at the surface of an ultrathin $bi_{1-x}sb_x$ alloy film, Phys. Rev. B **81**, 165422 (2010).

[5] A. Nishide, A. A. Taskin, Y. Takeichi, T. Okuda, A. Kak- izaki, T. Hirahara, K. Nakatsuji, F. Komori, Y. Ando, and I. Matsuda, Direct mapping of the spin-filtered sur- face bands of a three-dimensional quantum spin hall in- sulator, Phys. Rev. B **81**, 041309 (2010).

[6] H. Guo, K. Sugawara, A. Takayama, S. Souma, T. Sato, N. Satoh, A. Ohnishi, M. Kitaura, M. Sasaki, Q.-K. Xue, and T. Takahashi, Evolution of surface states in $bi_{1-x}sb_x$ alloys across the topological phase transition, Phys. Rev. B **83**, 201104 (2011).

[7] F. Nakamura, Y. Kousa, A. A. Taskin, Y. Takeichi, A. Nishide, A. Kakizaki, M. D'Angelo, P. Lefevre, F. Bertran, A. Taleb-Ibrahimi, F. Komori, S.-i. Kimura, H. Kondo, Y. Ando, and I. Matsuda, Topological tran- sition in $bi_{1-x}sb_x$ studied as a function of sb doping, Phys. Rev. B **84**, 235308 (2011).

[8] Y. Ohtsubo, L. Perfetti, M. O. Goerbig, P. L. Fevre, F. Bertran, and A. Taleb-Ibrahimi, Non-trivial surface-band dispersion on bi(111), New Journal of Physics **15**, 033041 (2013).

[9] H. M. Benia, C. Straßer, K. Kern, and C. R. Ast, Surface band structure of $bi_{1-x}sb_x$(111), Phys. Rev. B **91**, 161406 (2015).

[10] S. Ito, B. Feng, M. Arita, A. Takayama, R.-Y. Liu, T. Someya, W.-C. Chen, T. Iimori, H. Namatame, M. Taniguchi, C.-M. Cheng, S.-J. Tang, F. Komori, K. Kobayashi, T.-C. Chiang, and I. Matsuda, Proving nontrivial topology of pure bismuth by quantum confine- ment, Phys. Rev. Lett. **117**, 236402 (2016).

[11] Y. Ohtsubo and S. Kimura, Topological phase transition of single-crystal bi based on empirical tight-binding cal- culations, New Journal of Physics **18**, 123015 (2016).

[12] Y. Fukushima, K. Kawaguchi, K. Kuroda, M. Ochi, H. Tanaka, A. Harasawa, T. Iimori, Z. Zhao, S. Tani, K. Yaji, S. Shin, F. Komori, Y. Kobayashi, and T. Kondo, Spin-polarized saddle points in the topological surface states (2023), arXiv:2303.17816 [cond-mat.mtrl-sci].

[13] J. C. Y. Teo, L. Fu, and C. L. Kane, Surface states and topological invariants in three-dimensional topological insulators: Application to $bi_{1-x}sb_x$, Phys. Rev. B **78**, 045426 (2008).

[14] H.-J. Zhang, C.-X. Liu, X.-L. Qi, X.-Y. Deng, X. Dai, S.-C. Zhang, and Z. Fang, Electronic structures and surface states of the topological insulator $bi_{1-x}sb_x$, Phys. Rev. B **80**, 085307 (2009).

[15] I. Aguilera, C. Friedrich, and S. Blügel, Elec- tronic phase transitions of bismuth under strain from relativistic self-consistent $gw$ calculations, Phys. Rev. B **91**, 125129 (2015).

[16] Y. Fuseya and H. Fukuyama, Analytical so- lutions for the surface states of $bi_{1-x}sb_x$, J. Phys. Soc. Jpn. **87**, 044710 (2018).

[17] I. Aguilera, H.-J. Kim, C. Friedrich, G. Bihlmayer, and S. Blügel, $z_2$ topology of bismuth, Phys. Rev. Materials **5**, L091201 (2021).

[18] L. G. Ferreira, Relativistic band structure calculation for bismuth, Journal of Physics and Chemistry of Solids **28**, 1891 (1967).

[19] L. G. Ferreira, Band structure calculation for bismuth: Comparison with experiment, Journal of Physics and Chemistry of Solids **29**, 357 (1968).

[20] S. Golin, Band structure of bismuth: Pseudopotential approach, Phys. Rev. **166**, 643 (1968).

[21] X. Gonze, J.-P. Michenaud, and J.-P. Vigneron, Ab initio calculations of bismuth properties, including spin-orbit coupling, Physica Scripta **37**, 785 (1988).

[22] X. Gonze, J.-P. Michenaud, and J.-P. Vigneron, First- principles study of as, sb, and bi electronic properties, Phys. Rev. B **41**, 11827 (1990).

[23] A. B. Shick, J. B. Ketterson, D. L. Novikov, and A. J. Freeman, Electronic structure, phase stabil- ity, and semimetal-semiconductor transitions in bi, Phys. Rev. B **60**, 15484 (1999).

[24] I. Timrov, T. Kampfrath, J. Faure, N. Vast, C. R. Ast, C. Frischkorn, M. Wolf, P. Gava, and L. Perfetti, Ther- malization of photoexcited carriers in bismuth investi- gated by time-resolved terahertz spectroscopy and ab ini- tio calculations, Phys. Rev. B **85**, 155139 (2012).

[25] B. Zhou, H.-Z. Lu, R.-L. Chu, S.-Q. Shen, and Q. Niu, Finite size effects on helical edge states in a quantum spin-hall system, Phys. Rev. Lett. **101**, 246807 (2008).

[26] J. Linder, T. Yokoyama, and A. Sudbø, Anomalous finite size effects on surface states in the topological insulator $bi_2se_3$, Phys. Rev. B **80**, 205401 (2009).

[27] H.-Z. Lu, W.-Y. Shan, W. Yao, Q. Niu, and S.- Q. Shen, Massive dirac fermions and spin physics in an ultrathin film of topological insulator, Phys. Rev. B **81**, 115407 (2010).

[28] S.-Q. Shen, *Topological Insulators* (Springer-Verlag Berlin Heidelberg, 2012).

[29] H. Ozawa, A. Yamakage, M. Sato, and Y. Tanaka, Topological phase transition in a topological crys- talline insulator induced by finite-size effects, Phys. Rev. B **90**, 045309 (2014).

[30] F. Schindler, Z. Wang, M. G. Vergniory, A. M. Cook, A. Murani, S. Sengupta, A. Y. Kasumov, R. Deblock, S. Jeon, I. Drozdov, H. Bouchiat, S. Guéron, A. Yazdani, B. A. Bernevig, and T. Neupert, Higher-order topology in bismuth, Nature Physics **14**, 918 (2018).

[31] H. Appel, J. R. Lith, F. de Llanos, and F. Maciá, Evidence for higher order topology in bi and bi0.92sb0.08, Nature Communications **12**, 4420 (2021).

[32] T. Hirahara, N. Fukui, T. Shirasawa, M. Yamada, M. Aitani, H. Miyazaki, M. Matsunami, S. Kimura, T. Takahashi, S. Hasegawa, and K. Kobayashi, Atomic and electronic structure of ultrathin bi(111) films grown on $bi_2te_3$(111) substrates: Evidence for a strain-induced topological phase transition, Phys. Rev. Lett. **109**, 227401 (2012).

[33] Y. Ohtsubo, Y. Yamashita, J. Kishi, S. Ideta, K. Tanaka, H. Yamane, J. E. Rault, P. L. Fèvre, F. Bertran, and S. Kimura, Temperature- driven modification of surface electronic struc- ture on bismuth, a topological border material, Journal of Physics D: Applied Physics **52**, 254002 (2019).

[34] H. Mönig, J. Sun, Y. M. Koroteev, G. Bihlmayer,

J. Wells, E. V. Chulkov, K. Pohl, and P. Hof-mann, Structure of the (111) surface of bismuth: Leed analysis and first-principles calculations, Phys. Rev. B **72**, 085410 (2005).

[35] P. Hofmann, The surfaces of bismuth: Structural and electronic properties, Progress in Surface Science **81**, 191 (2006).

[36] K. Saito, H. Sawahata, T. Komine, and T. Aono, Tight-binding theory of surface spin states on bismuth thin films, Phys. Rev. B **93**, 041301 (2016).

[37] Y. Asaka, T. Kikuchi, and Y. Fuseya, Long-range perme-ation of wave function and superficial surface state due to strong quantum size effects in topological bi/bisb het-erojunctions, Phys. Rev. B **106**, 245303 (2022).

[38] H. L. Davis, J. B. Hannon, K. B. Ray, and E. W. Plum-mer, Anomalous interplanar expansion at the (0001) sur-face of be, Phys. Rev. Lett. **68**, 2632 (1992).

[39] G. te Velde and E. J. Baerends, Precise density-functional method for periodic structures, Phys. Rev. B **44**, 7888 (1991).

[40] BAND 2021.1 (SCM, Theoretical Chemistry, Vrije Universiteit, Amsterdam, The Netherlands), https://www.scm.com/.

[41] E. Bitzek, P. Koskinen, F. Gähler, M. Moseler, and P. Gumbsch, Structural relaxation made simple, Phys. Rev. Lett. **97**, 170201 (2006).

[42] J. P. Perdew, K. Burke, and M. Ernzerhof, Gen-eralized gradient approximation made simple, Phys. Rev. Lett. **77**, 3865 (1996).

[43] E. van Lenthe, A. Ehlers, and E.-J. Baerends, Geometry optimizations in the zero order regular approximation for relativistic effects, The Journal of Chemical Physics **110**, 8943 (1999), https://pubs.aip.org/aip/jcp/article-pdf/110/18/8943/19297774/894_1.pdf.

[44] Y. M. Koroteev, G. Bihlmayer, E. V. Chulkov, and S. Blügel, First-principles investigation of struc-tural and electronic properties of ultrathin bi films, Phys. Rev. B **77**, 045428 (2008).

[45] Y. Liu and R. E. Allen, Electronic structure of the semimetals bi and sb, Phys. Rev. B **52**, 1566 (1995).

[46] C. R. Ast and H. Höchst, Electronic structure of a bis-muth bilayer, Phys. Rev. B **67**, 113102 (2003).

[47] Y. M. Koroteev, G. Bihlmayer, J. E. Gayone, E. V. Chulkov, S. Blügel, P. M. Echenique, and P. Hof-mann, Strong spin-orbit splitting on bi surfaces, Phys. Rev. Lett. **93**, 046403 (2004).

[48] T. Hirahara, T. Nagao, I. Matsuda, G. Bihlmayer, E. V. Chulkov, Y. M. Koroteev, P. M. Echenique, M. Saito, and S. Hasegawa, Role of spin-orbit coupling and hy-bridization effects in the electronic structure of ultrathin bi films, Phys. Rev. Lett. **97**, 146803 (2006).

[49] K. Oura, M. Katayama, A. V. Zotov, V. G. Lifshits, and A. A. Saranin, *Surface Science: An Introduction* (Springer Berlin, Heidelberg, 2003).

[50] T. H. Hsieh, H. Lin, J. Liu, W. Duan, A. Bansil, and L. Fu, Topological crystalline insulators in the snte ma-terial class, Nature Communications **3**, 982 (2012).