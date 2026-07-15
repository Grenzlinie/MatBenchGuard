# Neural Scaling Laws Surpass Chemical Accuracy for the Many-Electron Schrödinger Equation

Du Jiang$^{1,2\dagger}$, Xuelan Wen$^{1*\dagger}$, Yixiao Chen$^{1}$, Ruichen Li$^{1,2}$, Weizhong Fu$^{1,2}$,
Hung Q. Pham$^{1}$, Ji Chen$^{2*}$, Di He$^{2*}$, William A. Goddard III$^{3*}$, Liwei Wang$^{2*}$,
Weiluo Ren$^{1*}$

$^{1\ast}$ByteDance Seed.
$^{2\ast}$Peking University.
$^{3\ast}$California Institute of Technology.

*Corresponding author(s). E-mail(s): wxl@bytedance.com; ji.chen@pku.edu.cn;
dihe@pku.edu.cn; wag@caltech.edu; wanglw@pku.edu.cn; renweiluo@bytedance.com;
$^\dagger$These authors contributed equally to this work.

## Abstract
We demonstrate, for the first time, that neural scaling laws can deliver near-exact solutions to the many-electron Schrödinger equation across a broad range of realistic molecules. This progress is enabled by the Lookahead Variational Algorithm (LAVA), an effective optimization scheme that systematically translates increased model size and computational resources into greatly improved energy accuracy for neural network wavefunctions. Across all tested cases, including benzene, the absolute energy error exhibits a systematic power-law decay with respect to model capacity and computation resources. The resulting energies not only surpass the 1 kcal/mol "chemical-accuracy" threshold but also achieve 1 kJ/mol subchemical accuracy. Beyond energies, the scaled-up neural network also yields better wavefunctions with improved physical symmetries, alongside accurate electron densities, dipole moments, and other important properties. Our approach offers a promising way forward to addressing many long-standing challenges in quantum chemistry. For instance, we improve energetic properties for systems such as the potential energy curve of nitrogen dimer as dissociation is approached and the cyclobutadiene automerization reaction barrier, producing definitive benchmarks, particularly in regimes where experimental data are sparse or highly uncertain. We also shed light on the decades-old puzzle of the cyclic ozone stability with highly accurate calculations for the cyclic-to-open ozone barrier. These results provide near-exact reference calculations with unprecedented accuracy, universal reliability and practical applicability, establishing a foundation for AI-driven quantum chemistry.

## 1 Main
The many-electron Schrödinger equation lies at the foundation of quantum chemistry and condensed matter physics, providing a first-principles framework for understanding the quantum nature of the physical world. Despite its central importance, no general-purpose method has come close to solving it exactly for realistic systems. Instead, practical quantum chemistry has long relied on the cancellation of large and often uncontrolled

errors to reach the so-called "chemical accuracy"-typically defined as energy errors within 1 kcal/-mol for relevant energy differences. This scheme, however, comes with several significant limitations, including poor performance in predicting observables beyond relative energies and a lack of systematic error control. For instance, the widely used Density Functional Theory (DFT) can predict qualitatively incorrect electron densities [1], undermining its reliability for density-derived properties, such as dipole moments and polarizabilities. Correlated wavefunction methods, on the other hand, depend on error cancellation due to steep computational scaling and slow basis-set convergence [2, 3], compromising their reliability in complex problems. These limitations underscore the need for a more accurate and reliable solution that delivers cancellation-free, high-accuracy energies and other observables for realistic systems.

Neural network-based quantum Monte Carlo (NNQMC) has emerged as a promising *ab initio* wavefunction theory to this challenge [4-6]. Unlike other machine learning approaches in quantum chemistry that rely on precomputed labeled data (e.g., DFT energies) [7, 8], NNQMC obtains the target quantum state directly through unsupervised optimization, without requiring any reference data. In particular, the full many-body wavefunction is modeled with highly expressive neural networks, providing access to accurate total energies, high-quality wavefunctions, and derived observables including electron and spin densities. Recent progress has improved energy accuracy as well as computational efficiency, highlighting its potential as a next-generation quantum chemistry framework [9-14]. Nonetheless, NNQMC has not yet come meaningfully close to the exact solutions of the Schrödinger equation as molecular systems increase in size and complexity. This is partly because default-sized neural networks lack sufficient representational capacity for larger systems, while simply increasing the network size rarely leads to proportional improvements in accuracy due to optimization challenges.

In this work, we train neural-network wavefunctions that, for the first time, deliver near-exact solutions to the many-electron Schrödinger equation for realistic systems with up to 12 atoms, achieving accuracy on par with experimental uncertainty. The resulting absolute energies surpass traditional "chemical accuracy" to approach the 1 kJ/mol regime, thereby enabling definitive relative energies without relying on error cancellation. Additionally, these solutions provide accurate many-body wavefunctions, which in turn produce benchmark-quality physical observables including electron density and dipole moments. This capability is made possible by two key innovations. First, we introduce the Lookahead Variational Algorithm (LAVA), an optimization scheme that combines variational and projective frameworks, offering better performance over existing schemes in NNQMC, such as Variational Monte Carlo (VMC) with stochastic reconfiguration [15] and Wasserstein Quantum Monte Carlo (WQMC) [16]. Second, we present the first systematic study of neural scaling laws [17] in *ab initio* quantum chemistry, showing that total energy errors decrease systematically and predictably by simply scaling up neural network model capacity and computational resources. Together, these advances position our approach uniquely within quantum chemistry, offering near-exact total energies and wavefunctions at the full configuration interaction (FCI) accuracy and complete basis set (CBS) limit at the same time.

Through this approach, we address several long-standing challenges in quantum chemistry, demonstrating its universal accuracy, flexibility, and ability to provide definitive benchmarks. Firstly, we establish a high-quality benchmark for cyclobutadiene's transition barrier, aligned with refined experimental data as well as the best estimates from coupled cluster (CC) and configuration interaction (CI) methods. Secondly, we study the potential energy curve (PEC) of diatomic molecules, which governs the vibrational levels critical for astrophysical models of planetary and stellar atmospheres [18]. In particular, we focus on nitrogen dimer and present a new PEC benchmark that surpasses previous experiment-based references in both accuracy and reliability. Thirdly, we reassess the metastability of the cyclic ozone, helping to provide a definitive answer to a long-standing controversy [19]. Collectively, these findings confirm our approach as a new standard of accuracy for predictive quantum chemistry.

2

## 2 Results

### 2.1 Scale Toward Exact Solutions with LAVA

In this section, we present a systematic study of neural scaling laws that achieve beyond-chemical-accuracy solutions to the Schrödinger equation. We demonstrate that neural network-based solutions systematically approach exact results with increasing model capacity and training compute. Notably, the convergence curve of absolute energy error follows a robust power-law decay, and the same convergence behavior is consistently observed across diverse molecular systems.

Although scaling laws have reshaped various domains of Artificial Intelligence [25–32], their application within quantum science remains underexplored [33]. More critically, the benefit of scaling up neural-network wavefunctions appears limited: energy improvement tends to saturate well before reaching exactness, hinting at an inability to fully exploit the capacity of large neural networks. To overcome this bottleneck, we introduce LAVA, an improved optimization framework for neural network wavefunctions that combines variational Monte Carlo updates with a projective step inspired by imaginary time evolution (Fig. 1a). This two-step procedure is effective for eluding local minima during the neural network training process, which is crucial for achieving asymptotic exactness as the neural network ansatz scales up. In practice, LAVA significantly improves stability during the training process and accuracy at the end of training, resulting in better wavefunctions and energies. See Section 4.2 and Supplementary Note 1.1 for algorithmic details.

LAVA scales predictably and robustly to deliver accurate solutions beyond chemical accuracy. In pursuing systematic improvement towards exactness, our approach offers several key advantages. Most notably, LAVA requires little heuristic tuning or chemical intuition, making it effectively a "fool-proof" process. Moreover, LAVA avoids the prohibitive scaling with excitation order inherent to traditional methods such as coupled cluster theory, offering a significantly more efficient route to high accuracy. These advantages are sketched in the main panel of Fig. 1b.

To demonstrate the effectiveness of neural scaling laws, we provide a range of quantitative evidence, as illustrated in Fig. 2. We examine the absolute energy of representative organic molecules, for which highly accurate experimental benchmarks (via total atomization energy) and theoretical references (W4 theory) are available. Our energy estimates not only surpass chemical accuracy but also fall within experimental uncertainty, a more stringent criterion for accuracy. Fig. 2a illustrates how neural scaling laws enable such accuracy, using benzene as a representative example. Specifically, the energy error decays following a power-law relation as the number of parameters in the neural network increases. In addition, we observe a linear relation between energy and variance as neural networks scale up (See Supplementary Note 3). Accordingly, we adopt an energy-variance extrapolation scheme (Section 4.4), which yields our best energy estimate, LAVA with Scaling-law Extrapolation (LAVA-SE).

In all tested cases, we consistently achieve total energy accuracy at sub-kJ/mol level using LAVA-SE together with a robust and reproducible scaling pattern of LAVA (Fig. 2b). Remarkably, our results align closely with those of the W4 protocol, a CC-based composite procedure extrapolated to the all-electron CCSDTQ5/CBS energy, offering kJ/mol or even "semi-spectroscopic" accuracy for thermochemistry [22]. With LAVA, applying neural scaling laws alone suffices to surpass the sub-kJ/mol threshold, without the need for ad hoc corrections. Note that this level of accuracy is achieved without relying on any error cancellation, offering a direct and absolute measure of proximity to the exact solution of the Schrödinger equation.

We further assess the efficiency and practicality of our approach from two complementary perspectives, related to other scaling behaviors that emerge as we scale up our calculations. First we demonstrate that LAVA can maintain favorable convergence speed across both strongly or weakly correlated regimes, taking nitrogen molecule dissociation curve as a representative case in Fig. 2c. Specifically, in order to approach the exact solution (using the LAVA-SE as a reference), the computation scaling with respect to computational runtime remains close to linear with minor

3

![](./images/1159463098931740672_1.jpg)

Fig. 1 Scaling Up LAVA-Optimized Neural Network Wavefunctions Toward Exactness. a. Upper:
The many-electron wavefunction is modeled by a massively parameterized neural network and optimized with
LAVA or neural network-based variational Monte Carlo (NNVMC). Middle: A conceptual energy landscape illus-
trates LAVA's better convergence behavior throughout the training process, compared to NNVMC, which only
considers energy-based losses. Lower: LAVA combines both the gradient of an energy-based loss and a projection-
derived direction via the Lookahead algorithm. b. Main panel: By scaling up the network size and computation
resources, LAVA achieves systematic and fool-proof improvements in accuracy, surpassing chemical accuracy and
approaching exact solutions. In contrast, traditional computational methods, such as coupled cluster and configu-
ration interaction, suffer from steep computational scaling and resource bottlenecks, due to various issues such as
basis set limitations, exploded determinant growth, and steep scaling with higher excitations. Inset: A schematic
plot of different quantum chemistry methods in terms of accuracy and system size. Notably, LAVA is able to
achieve more accurate energy results than previous NNVMC works with the same neural network size.

fluctuations along the whole curve (Fig. 2c lower
panel). As a comparison, couple cluster (CC)
theory exhibit significant deterioration in conver-
gence scaling in the strongly correlated regime [24]
(Fig. 2c upper panel). Moreover, LAVA's scalabil-
ity can further benefit from parallel computing,
whereas CC cannot (see Supplementary Note 2.2).
Second, we examine LAVA's performance as the
molecular size increases. These results demon-
strate that our approach is able to maintain
chemical accuracy with a relatively low computa-
tional scaling ($N_e^{5.2}$, where $N_e$ denotes the number
of electrons), as shown in Fig. 2d. By comparison,
CCSD(T) scales as $N_e^7$, while achieving chemical
accuracy may require even higher-order excita-
tions, which impose steeper, if not impractical,
scalings.

In the following sections, we address a range
of practical chemical challenges using scaled-up
neural-network wavefunctions. When a variational
guarantee is preferred, we report energies from our
largest network; otherwise, we use the extrapo-
lated LAVA-SE results.

4

![](./images/1159463098931740672_2.jpg)

![](./images/1159463098931740672_3.jpg)

![](./images/1159463098931740672_4.jpg)

![](./images/1159463098931740672_5.jpg)

Fig. 2 Neural scaling laws enable breakthrough performance. a. LAVA delivers near-exact ground state energy for benzene as neural networks scale up. The neural scaling law here is described by $E-E_{\text{expt}} \propto N_p^{-0.52}$, where $E$ denotes LAVA energies, $E_{\text{expt}}$ denotes experiment-derived reference [20], $N_p$ is the number of parameters in the neural networks. We also include energies from NNVMC [9] and CCSD(T)/CBS [21] for comparison. b. Upper: Absolute energy errors of LAVA-SE, CCSDTQ5/CBS level W4-theory [22], CCSD(T)/CBS level W2-theory [22], and NNVMC. LAVA-SE is more accurate than 1 kJ/mol thresholds (purple shade), aligning closely with highly accurate W4 theory. Experimental references are based on atomization energies from ATcT (Active Thermochemical Tables) [22] and absolute atom energies from Chakravorty et al. [23]. Specifically, for atom F, we use our variationally lower result since it is more reliable. Details are in Supplementary Note 4.1. NNVMC uses LapNet [9] with the default model size. Lower: Neural scaling laws of LAVA on the same molecules, showing error reduction with model size in power-law trends. See Supplementary Note 2 for details. c. Cost scaling exponents for $N_2$ as LAVA increases model size and CC methods increase excitation orders. For CC, data from Chan et al. [24] shows that CC's computational effort scales as a power-law trend relative to $1/(E_{\text{CC}}-E_{\text{FCI}})$ under cc-pVDZ basis set. For LAVA, the total GPU time cost scales as a power-law relative to $1/(E_{\text{LAVA}}-E_{\text{SE}})$, where $E_{\text{SE}}$ denotes the LAVA-SE result. LAVA maintains a nearly constant exponent along the $N_2$ dissociation curve, while CC's performance deteriorates in the strongly correlated region. d. LAVA GPU hours as the number of electrons $N_e$ increases, with increasing model size for better accuracy. With model size fixed, runtime scales as $N_e^{2.1}$ (dotted lines). To ensure chemical accuracy, runtime scales as $N_e^{5.3}$ (the solid line).

5

### 2.2 Definitive Benchmarks beyond Experimental Limitations

The scarcity of high-quality experimental data remains a key bottleneck in quantum chemistry, limiting both the development of exchange-correlation (XC) functionals in DFT and the validation of advanced wavefunction methods. For unstable or non-equilibrium geometries, it is challenging to perform thermochemical experiments to measure their energies and observables. In such cases, it is particularly valuable to have highly accurate *ab initio* methods to fill the gaps. LAVA is well-suited for these challenging regimes, offering a reliable and systematically improvable alternative that serves as a critical complement to experimental data.

As a first demonstration, we study the reaction barrier associated with the automerization of cyclobutadiene ($\text{C}_4\text{H}_4$), a long-standing challenge in quantum chemistry due to its multireference character. To date, neither experimentally derived benchmarks nor theoretical predictions can reliably determine the reaction barrier between the rectangular ($D_{2\text{h}}$) minimum and the square ($D_{4\text{h}}$) transition state. The experimental estimate gave a lower bound of 1.6 kcal/mol and an upper bound of 10 kcal/mol, while various theoretical predictions range from 3 to 20 kcal/mol [5, 21, 34–37], as illustrated in Fig. 3a. Here, we establish a definitive benchmark for this transition barrier (9.2 kcal/mol), obtained from LAVA-SE for both $D_{2\text{h}}$ and $D_{4\text{h}}$ states. This result is derived from a sequence of scaled-up neural network wavefunctions and does not rely on error cancellation. To further validate our result, we establish consensus with improved experimental estimates and the most accurate predictions from different theoretical frameworks, as shown by the star symbols in Fig. 3a. For experimental data, we refined the previous rough estimate to a more precise value of 9.9 kcal/mol (See Supplementary Note 6). This new estimate agrees well with LAVA and may align even more closely under alternative computational settings during refinement [38]. On the theoretical side, we leverage the systematic improvability of the CC and selected CI families to obtain their best estimates, which are CCSDTQ/AVTZ [34] and HCI(20e, 172o)/cc-pVTZ extrapolated to the FCI limit [36], respectively. Notably, the best estimates from NNQMC, CC, and selected CI—three fundamentally different theoretical approaches—agree with each other within 0.3 kcal/mol, suggesting convergence to the exact reaction barrier. This consistency highlights LAVA’s ability to deliver accurate and reliable solutions for challenging electronic structure problems.

Next, we demonstrate LAVA on the potential energy curve of the nitrogen dimer, a prototypical and long-standing challenge due to its multireference character, and establish a new benchmark, $\text{MLR}_3(9)$, that surpasses the previous standard $\text{MLR}_4(6,8)$ in accuracy. The previous benchmark, labeled as $\text{MLR}_4(6,8)$ in Fig. 3.b, was fitted to experimental vibrational levels $v=0-19$ [39]. These vibrational levels provide a high-accuracy energy benchmark only in the near-equilibrium region, corresponding to bond lengths $r$ between 0.9 to 1.5 Å (gray shaded region). There are few experimental results for vibrational levels $v$=20-25 [40], albeit with a high uncertainty. Measuring higher vibrational levels is challenging because the nitrogen dimer becomes unstable in the near-dissociation region.

Different fitting schemes also give large discrepancies in this region. As shown in the inset of Fig. 3, $\text{EMO}_2(6)$ and $\text{MLR}_4(6,8)$ differ by 3.4 kcal/mol in the near-dissociation region, where experimental benchmarks are unavailable. Details of fitting analytic PECS from experimental vibrational levels are given in Supplementary Note 7 and Le Roy et al. [39]. At the intermediate region, $\text{MLR}_4(6,8)$ also shows significant disagreements with multi-reference correlated calculations [41] and previous NNQMC studies [6, 21, 42–44].

We now provide a definitive benchmark to resolve these discrepancies by performing LAVA calculations across various bond lengths. Furthermore, we fit an analytic potential curve in the Morse/long-range form [39], namely $\text{MLR}_3(9)$, based on LAVA data points which also reproduce the experimental vibrational levels $v$=0-19. Details on this fitting procedure are given in the Supplementary Note 7. This new benchmark $\text{MLR}_3(9)$ retains the accuracy of the previous benchmark $\text{MLR}_4(6,8)$ [39] for the near-equilibrium region (0.9 Å $< r <$ 1.5 Å) and the fully dissociation limit($r > 4.0$ Å), while improving the reliability around the near dissociation region. In addition, $r_{12}$-MR-ACPF [41, 45], an explicitly correlated multireference method with

6

![](./images/1159463098931740672_6.jpg)

![](./images/1159463098931740672_7.jpg)

Fig. 3 Definitive LAVA benchmarks complement experiments. a. Upper: Reaction barriers of $C_4H_4$ derived from experiment and different theoretical methods. Bars represent the spread of reported values, corresponding to each line, within each method family. Stars indicate the improved experimental estimate and the best estimates from systematically improvable theories, namely CCSDTQ/aug-cc-pVTZ in CC, HCI/cc-pVTZ extrapolated to the FCI limit in selected CI, and LAVA in NNQMC. The dashed line shows the value predicted by LAVA, highlighting the consistency among those stars. Lower: Power-law scaling trends between the number of parameters $N_p$ and energy difference $E - E_{SE}$, where $E_{SE}$ are scaling-law extrapolation results. b. Upper main panel: The ground-state potential energy curve of $N_2$ dissociation. The analytic potential functions, namely $MLR_3(9)$, $MLR_4(6,8)$, and $EMO_2(6)$, are fitted from vibrational levels $v = 0 - 19$. Upper inset: PECs fitted from different analytic function forms and parameters show a large discrepancy at long bond lengths. Lower main panel: The energy difference between two ab initio calculations and three fitted analytic PECs. $MLR_3(9)$, the surrogate model of LAVA, is the new recommended benchmark. The $r_{12}$-MR-ACPF result is shifted together so that its results match high-fidelity experimental data in the equilibrium region (the shaded area).

FCI/CBS accuracy, perfectly aligns with our new benchmark $MLR_3(9)$ within 1 kJ/mol difference, after shifting down by about 5 mHa. However, $r_{12}$-MR-ACPF exhibits exponential scaling with respect to the size of reference space. This computational complexity necessitates careful optimization of both the reference space and basis set, thereby restricting its practical application to small molecular systems. Together, the reproduction of both the available experimental vibrational levels and the relative energies from $r_{12}$-MR-ACPF confirms the accuracy and reliability of our newly fitted benchmark $MLR_3(9)$ curve.

Collectively, the cases in this section demonstrate the reliability and versatility of our approach. It not only resolves long-standing discrepancies between experimental measurements and theoretical predictions but also provides definitive benchmarks when experiments or conventional theories fall short, thereby establishing a new standard for future benchmark studies.

### 2.3 Metastability of Ozone's Ring-Minimum Species

Ozone plays a critical role in atmospheric chemistry. A long-standing puzzle, however, is the metastability of cyclic ozone, which has been predicted by various theoretical studies, from early

![](./images/1159463098931740672_8.jpg)

![](./images/1159463098931740672_9.jpg)

![](./images/1159463098931740672_10.jpg)

![](./images/1159463098931740672_11.jpg)

Fig. 4 Analysis of ozone bent-cyclic isomerization reaction. a. A conceptual diagram for $O_3$ potential energy surfaces of $^1A'$, $^1A''$, $^3A''$, and $^2^1A'$ in isosceles triangle geometries, based on XMS-CASPT2 predictions [46, 47]. b. Summary of calculated energy barriers of $O_3$ isomerization reaction from ring-minimum species to open-ring minimum since 1972. Our LAVA-SE estimate, denoted by the purple star, is consistent with most high-accuracy results in the last decade. c. Neural scaling laws for OM, TS, RM configurations of ozone, respectively, showing clear power-law decay between energy error and network size. The energy error is calculated with respect to LAVA-SE. d. Evolution of wavefunction spatial symmetry as the number of parameters increases for the TS configuration. $\sigma_h$ is the expectation of the horizontal reflection operator. With the default network size, LAVA produces a contaminated state as a superposition of $^1A'$ state (weight 0.18) and $^1A''$ state (weight 0.81). Enlarged networks yield a pure $^1A''$ state, which is 3 kcal/mol lower in energy compared to the contaminated one. For validation purpose, we also generate symmetry-enforced LAVA results for $^1A'$ and $^1A''$, visualizing their natural orbitals with the lowest two occupation numbers that occ > 0.1.

ab initio work to modern coupled-cluster and mul- tireference methods, since the 1970s [19, 48-60]. Nonetheless, direct experimental evidence remains absent, casting uncertainty on these theoretical predictions.

Here, we tackle this problem by studying the reaction barrier that connects three critical struc- tures, namely the open-ring minimum (OM) (the lowest energy configuration), the equilateral ring minimum (RM, i.e., cyclic ozone), and the tran- sition state (TS) between OM and RM. Fig. 4a illustrates the highly complex potential energy surfaces of $O_3$ spanning those species. These sur- faces feature numerous intersections, including crossings between states of different spin multiplic- ities and $C_{2v}$ spatial symmetries. Such complex- ity presents a significant challenge for electronic structure methods, as accurate modeling requires careful treatment of spin and spatial symmetry constraints and degeneracies. Despite extensive theoretical efforts over the past half a century, estimates of the barrier height remain far from consensus, differing by more than 15 kcal/mol. Leveraging neural scaling laws, LAVA predicts a reaction barrier of 24.9 kcal/mol as shown in

8

Fig. 4c. Although slightly lower than most values reported from high-accuracy methods in the past decade (Fig. 4b), this result still supports the kinetic stability of RM, even when accounting for the tunneling effect [55].

Additional evidence further supports the accuracy and reliability of our results. To begin with, the predictions of LAVA regarding the energy and geometry of OM are in excellent agreement with experimental results [61] (See Supplementary Note 8.1). Furthermore, neural scaling laws enable the emergence of physical symmetries without applying explicit constraints to wavefunctions. As the model size increases, the neural network wavefunction recovers the correct spin multiplicity and spatial symmetry. Take TS as a showcase, LAVA guides the neural network wavefunctions toward the correct $^3\mathrm{A}''$ ground state without any constraints (see Supplementary Note 8.6). Additionally, when we enforce singlet spin symmetry using a penalty-based method [10], LAVA identifies the $^1\mathrm{A}''$ ground state, as evidenced by the improved spatial symmetry depicted in Fig. 4d.

Overall, such a capability of scaling up towards the correct ground state is essential for reliable ground-state characterization in strongly correlated regimes, where multiple near-degenerate states often engage in competition.

### 2.4 Beyond Energies
Beyond accurate absolute energies, LAVA also produces near-exact wavefunctions in the CBS limit, benefiting from its first-quantized nature. Consequently, it delivers FCI/CBS-quality physical observables including electron densities and dipole moments. Conventional quantum chemistry methods, by contrast, remain limited by the finite basis set approximation, despite decades of effort toward developing systematically improvable basis sets [64]. While relative energies tend to converge rapidly with basis set size [65, 66], the convergence behavior of electron densities and density-derived properties toward the CBS limit remains less well understood [63, 67].

We assess LAVA's performance on dipole moments, a critical property reflecting molecular charge distribution and polarity. Specifically, we compare LAVA predictions with highly accurate references from spectroscopy experiments [62] (Fig. 5a). Across all the molecules examined,
![](./images/1159463098931740672_12.jpg)

Fig. 5 LAVA delivers reliable dipole moments.
a. Dipole moments $\mu$ derived from our wavefunctions match experimental values $\mu_{\text{expt}}$ [62]. For comparison, CCSD(T)/CBS results from Hait and Head-Gordon [63] are also visualized, which fall out of the experimental range for NO, O₃, and F₂O₂. For all molecules, the SCAN density functional results [63] fail to match experimental references. b. Basis set convergence of dipole moment of F₂O₂ for HF and coupled-cluster methods, together with experimental benchmark and LAVA estimates for comparison. Dipole moments in Debyes are plotted against correlated-consistent basis sets (cc-pVXZ) and augmented counterparts (aug-cc-pVXZ) for $\text{X} = \text{D, T, Q, 5}$. CBS extrapolation scheme follows Supplementary Note 6.2. The missing points indicate calculations infeasible with available computational resources. Results of coupled-cluster methods exhibit strong basis set dependence and severe memory bottlenecks, while LAVA achieves experimental-level accuracy.

LAVA shows excellent agreement with experimental data, falling within the bounds of experimental uncertainty. In contrast, CCSD(T)/CBS results deviate from these bounds for molecules with significant multireference character (see Supplementary Table 17), namely O₃ and F₂O₂. One could, in principle, move beyond CCSD(T)/CBS to CCSDT(Q)/CBS for better accuracy, but such

calculations are computationally intractable due to the steep scaling of coupled cluster methods. Moreover, dipole moments are notoriously sensitive to the choice of basis set and converge slowly toward the CBS limit. Fig. 5b exemplifies this behavior for $F_2O_2$, where neither CCSD nor CCSD(T) reaches experimental accuracy when extrapolated along either the correlated-consistent basis set sequence (cc-pVXZ) or its augmented counterpart (aug-cc-pVXZ). Memory demand grows rapidly with increasing basis set size, emerging as the computational bottleneck: CPU-based PySCF [68] is limited to the aVTZ basis set, while GPU-accelerated ByteQC [69] can accommodate the larger aV5Z basis set. Notably, LAVA also produces more accurate energy than CC-based composite theory W4 for molecules with strong multireference character, as discussed Supplementary Note 4.3.

Moreover, with scaled-up neural networks, LAVA is also able to produce high-quality electron densities [70]. Together with benchmark-quality energies, this provides critical reference data for developing better density-functional approximations that seek to recover the exact energy from the exact density [1].

## 3 Discussion

This study demonstrates how LAVA-powered neural scaling laws can systematically and practically approach exact solutions to many-electron Schrödinger equations. We generate high-quality benchmarks for various molecules, overcoming the issues of uncertainties and inaccuracies in experimental data. Additionally, we confirm the metastability of ring-minimum ozone from a theoretical perspective.

We are now able to provide FCI/CBS quality wavefunctions with an attractive computational scaling. This enables the creation of a reliable benchmark dataset of both energies and densities, complementing scarce experimental references. Such datasets can facilitate data-driven development of next-generation XC functionals in DFT and rigorous validation of other state-of-the-art wavefunction methods, opening new chapters in high-accuracy quantum chemistry and its applications. Besides its favorable computational scaling and embarrassingly parallelism, LAVA also benefits from other recent algorithmic progresses in the field of NNQMC [12, 13, 71], which further reduce the computational cost significantly. Moreover, with rapid advances in AI hardware and optimization techniques, we anticipate that this approach will become increasingly practical and scalable, enabling broader applications to larger systems in quantum chemistry and beyond.

Overall, the synergy of AI and quantum chemistry offers a powerful route to solving complex electronic structure problems with near-exact solutions, unlocking transformative applications in catalysis, materials science, and drug discovery. While challenges remain, neural scaling laws establish a robust foundation for advancing accuracy and scalability across increasingly complex systems in *ab initio* quantum chemistry.

## 4 Methods

### 4.1 Variational Optimization Framework

In this work, we focus on the time-independent electronic Schrödinger equation within the Born-Oppenheimer approximation:
$$
\hat{H}\psi(x_1,...,x_N) = E\psi(x_1,...,x_N), \tag{1}
$$

$$
\begin{aligned}
\hat{H} =& -\frac{1}{2} \sum_i \Delta_i + \sum_{i>j} \frac{1}{|\mathbf{r}_i - \mathbf{r}_j|} \\
&- \sum_{iI} \frac{Z_I}{|\mathbf{r}_i - \mathbf{R}_I|} + \sum_{I>J} \frac{Z_I Z_J}{|\mathbf{R}_I - \mathbf{R}_J|},
\end{aligned} \tag{2}
$$

where for the $i$-th electron ($i \in \{1,2,\cdots,N\}$), $x_i = \{\mathbf{r}_i, \sigma_i\}$ consists of the coordinate of electron $\mathbf{r}_i \in \mathbb{R}^3$ and its spin $\sigma_i \in \{1,-1\}$, and for the $I$-th nucleus ($I \in \{1,2,\cdots,M\}$), we denote the charge as $Z_I$ and its fixed position as $\mathbf{R}_I$. Obeying the spin-statistics theorem, a many-electron wavefunction is antisymmetric under an exchange of electrons.

As an *ab initio* method, variational Monte Carlo (VMC) directly solves the following optimization problem to approximate the ground state

of a many-electron quantum system:
$$
\begin{aligned}
\min _{\theta} \quad & \frac{\left\langle\psi_{\theta}|\hat{H}| \psi_{\theta}\right\rangle}{\left\langle\psi_{\theta} \mid \psi_{\theta}\right\rangle}, \\
\text { s.t. } \quad & \psi\left(\cdots, x_{i}, \cdots, x_{j}, \cdots\right) \\
& =-\psi\left(\cdots, x_{j}, \cdots, x_{i}, \cdots\right), \\
& \forall i, j \in\{1,2, \cdots, N\},
\end{aligned} \quad (3)
$$
and $\theta$ are ansatz parameters for representing neural network wavefunction $\psi_{\theta}$. VMC uses Monte Carlo methods to evaluate the expected value of the total energy
$$
\begin{aligned}
E_{\mathrm{tot}} & =\frac{\left\langle\psi_{\theta}|\hat{H}| \psi_{\theta}\right\rangle}{\left\langle\psi_{\theta} \mid \psi_{\theta}\right\rangle}=\int \frac{\hat{H} \psi_{\theta}(x)}{\psi_{\theta}(x)} \frac{\psi_{\theta}^{2}(x)}{\left\langle\psi_{\theta} \mid \psi_{\theta}\right\rangle} \mathrm{d} x \\
& =\mathbb{E}_{x \sim p}\left[E_{L}\right],
\end{aligned} \quad (4)
$$
where $p(x)=\frac{\psi_{\theta}^{2}(x)}{\left\langle\psi_{\theta} \mid \psi_{\theta}\right\rangle}$ and $E_{L}=\frac{\hat{H} \psi_{\theta}(x)}{\psi_{\theta}(x)}$ is so-called local energy. Variational optimization is then performed to find the best approximation of the ground state wavefunction in the ansatz space.

From another perspective, solving the ground state of the time-independent Schrödinger equation can be seen as finding the lowest eigenstate of the Hermitian operator $\hat{H}$, which can be achieved by the power method [72]. By repeatedly applying a propagator to an arbitrary trial state $\psi$, one can eventually get the ground state $\psi_{0}$, as long as $\psi$ and $\psi_{0}$ are not orthogonal. The propagator can be any operator that decays all the other eigenstates of the Hamiltonian $\hat{H}$ while retaining the one with the lowest eigenvalue. When we use the exponential form $e^{-\tau\left(\hat{H}-E_{T}\right)}$ as propagator, the power method is equivalent to imaginary time evolution under the Wick-rotated Schrödinger equation [73]. Here, $E_{T}<0$ is a scalar close to the ground state energy for normalization.

We consider the linear propagator
$$
\hat{U}(\tau)=1-\tau\left(\hat{H}-E_{T}\right). \tag{5}
$$

For the finite time inteval $\tau$, as $n \tau \rightarrow+\infty$, where integer $n$ is the number of time steps, we have $\psi_{0} \propto \hat{U}^{n}(\tau) \psi$.

From the perspective of the power method, VMC can be deemed as an alternating application of two operators: the propagator to evolve towards the ground state, and a projection operator that maps the propagated state back to the ansatz space. Given an ansatz space parametrized by $\theta \in \Omega$, where $\Omega$ is the parameter space, we define the projection operator $\hat{P}_{\mathcal{D}_{1}, \mathcal{D}_{2}}(\theta, \eta)$ that projects an arbitrary wavefunction $\phi$ to the ansatz space in the vicinity of $\theta$, with radius $\eta$, while keeping the projected wavefunction normalized, under parameter space metric $\mathcal{D}_{1}$ and Hilbert space metric $\mathcal{D}_{2}$:
$$
\hat{P}_{\mathcal{D}_{1}, \mathcal{D}_{2}}(\theta, \eta) \phi=\sqrt{\frac{\left\langle\psi_{\theta} \mid \psi_{\theta}\right\rangle}{\left\langle\psi_{\theta^{*}} \mid \psi_{\theta^{*}}\right\rangle}} \psi_{\theta^{*}}, \tag{6}
$$
where
$$
\theta^{*}=f_{\mathcal{D}_{1}, \mathcal{D}_{2}}(\theta, \eta) \phi \triangleq \underset{\substack{\theta^{\prime} \in \Omega \\ \mathcal{D}_{1}\left(\theta, \theta^{\prime}\right) \leq \eta}}{\arg \min } \mathcal{D}_{2}\left(\phi, \psi_{\theta^{\prime}}\right). \tag{7}
$$

In the case of VMC with natural gradient descent (or stochastic reconfiguration), $\mathcal{D}_{1}$ is the metric induced by the quantum geometric tensor $\mathcal{F}$, and $\mathcal{D}_{2}$ is the Kullback-Leibler (KL) divergence.

At step $n$, the iteration of VMC, starting from parameters $\theta_{n}$, can be written as
$$
\begin{aligned}
\theta_{n+1} & =\theta_{n}+\eta_{n} g, \\
g & =\lim _{\tau \rightarrow 0+} \frac{f_{\mathcal{F}, \mathrm{KL}}\left(\theta_{n}, \eta_{n} \tau\right) \hat{U}(\tau) \psi_{\theta_{n}}-\theta_{n}}{\eta_{n} \tau},
\end{aligned} \tag{8}
$$
where $\eta_{n}$ is the learning rate, which can vary with the iteration.

Neural network-based variational Monte Carlo [6, 74, 75] utilizes a neural network-based ansatz to parameterize the many-body wavefunction, enabling the accurate capture of complex electronic correlations that are often challenging for traditional quantum chemistry methods. Following Li et al. [9], we use the LapNet ansatz and the Forward Laplacian computational framework.

Instead of directly minimizing total energy, we develop the Lookahead Variational Algorithm (LAVA) for optimization, which is described in more detail below.

## 4.2 LAVA : the Lookahead Variational Algorithm
LAVA is designed to optimize parameterized wavefunctions by combining the principles of imaginary time evolution (ITE) and variational optimization. We describe LAVA's implementation in Algorithm 1. Inspired by the Lookahead algorithm [76],

our approach calculates the Lookahead direction in Hilbert space following the discretized ITE trajectory (Algorithm 1 line 6-12) and updates the variational ansatz through a projection mechanism ensuring that optimization remains confined to the variational manifold (Algorithm 1 line 13-14).

From this perspective, LAVA "looks ahead" at the space of iteratively propagated states. Instead of directly using the projected propagation for the next step, in iteration $n$, LAVA first constructs temporary state $\psi_{\text{temp}}$ as

$$
\psi_{\text{temp}}=\hat{P}_{\mathcal{F},\text{KL}}(\theta_{n},\eta_{\text{temp}})\hat{U}(\tau_{\text{temp}})\psi_{\theta_{n}},\qquad(9)
$$

where $\theta_{n}$ denotes the current parameters, and $\eta_{\text{temp}}$, $\tau_{\text{temp}}$ are the projection radius and the small time interval used in this intermediate step, respectively.

From this intermediate $\psi_{\text{temp}}$, LAVA moves along a Lookahead direction:

$$
\Delta\psi=-\tau\hat{H}(\psi_{\text{temp}}+\psi_{\theta_{n}})+2\tau E_{T}\psi_{\theta_{n}}.\qquad(10)
$$

Since

$$
\Delta\psi\propto\frac{1}{2E_{T}}\hat{H}(\psi_{\text{temp}}+\psi_{\theta_{n}})-\psi_{\theta_{n}},\qquad(11)
$$

to get $\psi_{\theta_{n+1}}$, LAVA applies a projection operator $\hat{P}_{\mathcal{F},\text{SM}_{1}}(\theta_{n},\eta)$ on

$$
\psi'=\frac{1}{E_{T}}\hat{H}(\psi_{\theta_{\text{temp}}}+\psi_{\theta_{n}}).\qquad(12)
$$

For this projection $\hat{P}_{\mathcal{F},\text{SM}_{1}}(\theta_{n},\eta)$, we use $L_{1}$ score matching (SM):

$$
\text{SM}_{1}(\phi,\psi;p)=\mathbb{E}_{x\sim p}[\parallel\nabla_{x}\ln|\phi(x)|-\nabla_{x}\ln|\psi(x)|\parallel_{1}].
\qquad(13)
$$

Then,

$$
\psi_{\theta_{n+1}}=\hat{P}_{\mathcal{F},\text{SM}_{1}}(\theta_{n},\eta)\psi'.\qquad(14)
$$

For the actual implementation, our projected propagation uses natural gradient descent with Kronecker-Factored Approximate Curvature (known as KFAC) [77], in which a block-diagonal $\mathcal{F}_{\text{KFAC}}$ approximates the quantum geometric tensor $\mathcal{F}$. At iteration $n$, LAVA first performs a VMC step to get intermediate parameters $\theta_{\text{temp}}$:

$$
\begin{aligned}
\theta_{\text{temp}}&=\theta_{n}-\eta_{\text{temp}}\mathcal{F}_{\text{KFAC}}^{-1}g,\\
g&=\mathbb{E}_{x\sim\psi_{\theta_{n}}^{2}}\left[\left(E_{L}(x)-E_{\text{tot}}\right)\nabla_{\theta_{n}}\ln|\psi_{\theta_{n}}(x)|\right],
\end{aligned}\qquad(15)
$$

where $E_{\text{tot}}$ is the average total energy and $\eta_{\text{temp}}$ is the learning rate for this intermediate step. An unnormalized temporary state $\psi'$ is calculated by

$$
\psi'=-\hat{H}\left(\psi_{\theta_{\text{temp}}}\sqrt{\frac{\langle\psi_{\theta_{n}}|\psi_{\theta_{n}}\rangle}{\langle\psi_{\theta_{\text{temp}}}|\psi_{\theta_{\text{temp}}}\rangle}}+\psi_{\theta_{n}}\right).
\qquad(16)
$$

The gradient direction of LAVA then follows

$$
\begin{aligned}
g_{n}&=\nabla_{\theta_{n}}\text{SM}_{1}(\psi',\psi_{\theta_{n}};\psi_{\theta_{\text{temp}}}^{2})\\
&=\mathbb{E}_{x\sim\psi_{\theta_{\text{temp}}}^{2}}\left[\langle f(x),\nabla_{\theta_{n}}\nabla_{r}\ln|\psi_{\theta_{n}}(x)|\rangle\right],
\end{aligned}\qquad(17)
$$

$$
f(x)=-\text{sgn}\left(\nabla_{r}\ln\left|\frac{\psi'(x)}{\psi_{\theta_{n}}(x)}\right|\right).\qquad(18)
$$

LAVA feeds the gradient into the Adam-KFAC optimizer to update the parameters. Unlike Izadi et al. [78], we directly apply Adam [79] to KFAC preconditioned gradient:

$$
\theta_{n+1}=\theta_{n}-\text{Adam}(\mathcal{F}_{\text{KFAC}}^{-1}g_{n}).\qquad(19)
$$

### 4.3 Neural Scaling Laws

The central premise of our scaling laws establishes that, with LAVA, the energy error of trained models decays following a power law trend with respect to the number of neural network parameters $N_{p}$ governing expressivity:

$$
E-E_{0}=\alpha N_{p}^{-\beta},\qquad(20)
$$

where $\alpha$ and $\beta$ are system-dependent variables and $E_{0}$ is the exact ground state energy. We monotonically increase network width and the number of determinants during this scaling-up process. For 11 systems with reliable experimental benchmarks, the average $r^{2}$ of ordinary least squares (OLS) regression on a logarithmic scale is larger than 0.95, and residual diagnostics (White test, $p>0.2$) reveals no significant heteroscedasticity. For the details, see Supplementary Note 2.

12

```plaintext
\documentclass{article}
\setlength{\emergencystretch}{5em}
\usepackage[pass,paperwidth=50cm]{geometry}
\usepackage{breakurl}
\pagestyle{empty}
\usepackage{amsmath,algorithm,algorithmic}
\begin{document}

\begin{algorithm}[H]
\caption{LAVA}
\begin{algorithmic}[1]
\REQUIRE initial parameters $\theta$, samples $\{x^{(i)}\}_{i=1}^B$
\STATE $n \leftarrow 0$
\STATE $m_0 \leftarrow 0$
\STATE $v_0 \leftarrow 0$
\WHILE{$n \leq N$}
    \STATE update $x^{(i)}$ by sampling from $\frac{\psi_\theta^2}{\langle \psi_\theta | \psi_\theta \rangle}$
    \STATE $E_L(x^{(i)}) \leftarrow \frac{\hat{H} \psi_\theta(x^{(i)})}{\psi_\theta(x^{(i)})}$
    \STATE $E_{\text{tot}} \leftarrow \frac{1}{B} \sum_{i=1}^B E_L(x^{(i)})$
    \STATE $g \leftarrow \frac{1}{B} \sum_{i=1}^B \left( E_L(x^{(i)}) - E_{\text{tot}} \right) \nabla_\theta \ln | \psi_\theta(x^{(i)}) |$
    \STATE $\theta_{\text{temp}} \leftarrow \theta - \eta_{\text{temp}} \mathcal{F}_{\text{KFAC}}^{-1} g$
    \STATE update $x^{(i)}$ by sampling from $\frac{\psi_{\theta_{\text{temp}}}^2}{\langle \psi_{\theta_{\text{temp}}} | \psi_{\theta_{\text{temp}}} \rangle}$
    \STATE $C \leftarrow \sqrt{\frac{\langle \psi_\theta | \psi_\theta \rangle}{\langle \psi_{\theta_{\text{temp}}} | \psi_{\theta_{\text{temp}}} \rangle}}$
    \STATE $E_L'(x^{(i)}) \leftarrow \frac{\hat{H} \left( \psi_\theta(x^{(i)}) + C \psi_{\theta_{\text{temp}}}(x^{(i)}) \right)}{\psi_\theta(x^{(i)})}$
    \STATE $g \leftarrow -\frac{1}{B} \sum_{i=1}^B \left\langle \text{sgn}(E_L'(x^{(i)})) \text{sgn}(\nabla_{r^{(i)}} E_L'(x^{(i)})), \nabla_\theta \nabla_{r^{(i)}} \ln | \psi_\theta(x^{(i)}) | \right\rangle$
    \STATE $\theta \leftarrow \theta - \text{Adam}\left( \mathcal{F}_{\text{KFAC}}^{-1} g \right)$
    \STATE $n \leftarrow n + 1$
\ENDWHILE
\RETURN $\theta$, $\{x^{(i)}\}_{i=1}^B$
\end{algorithmic}
\end{algorithm}

We also observe the scaling laws of local energy variance $V = \langle (\hat{H} - E)^2 \rangle$:
$$
V = \alpha_v N_p^{-\beta_v}, \tag{21}
$$
where $\alpha_v$ and $\beta_v$ are system-dependent variables. Under the zero-variance principle of quantum Monte Carlo, our estimated energy approximates the exact ground state energy $E_0$ as $V \to 0$. Since variance estimation requires no exact reference data, unlike error measurement, verifying the relationship is possible for any system where LAVA calculations are available. We confirmed this relationship across various molecular systems by linear regression on a logarithmic scale, and the average $r^2$ is larger than 0.97. Still, OLS is used since the White test shows $p > 0.2$. The detailed results are in Supplementary Note 2, and model architectures and training scheme are listed in Supplementary Note 1.1.

\section{4.4 Extrapolation Scheme}
For practically trained models, we empirically observed the following relationship between local energy variance and energy:
$$
E = kV + b, \tag{22}
$$
where $k$ and $b$ are system-dependent variables. This relationship is similar to variance-energy extrapolation in Fu et al. [80], which utilizes training data of a fixed model instead of optimized networks of different capacities.

Since theoretically $\lim_{V \to 0} E = E_0$ and empirically $\lim_{N_p \to +\infty} V = 0$, we follow Fu et al. [80] and use $b$ as our asymptotic estimates. For various molecular systems, residual diagnostics (White test, $p > 0.2$) support the use of ordinary least squares regression, and the average OLS $r^2$ for linear regression lines is greater than 0.99. For systems with experimental reference values, the errors in our extrapolation fall within the experimental uncertainty. Combining neural scaling

\end{document}
```

laws and extrapolation enables the estimation of threshold computational resources to reach sub-kJ/mol accuracy.

Data Availability. All data supporting the findings of this study are available within the Supplementary Information.

Acknowledgements. We thank Chenyang Li, Xuefei Xu, Yinan Shu, Donald G. Truhlar for the insight discussion. We thank Zigeng Huang, Qiming Sun, Xiaojie Wu, and the rest of the ByteDance Seed Group for their inspiring ideas and encouragement. We also thank Hang Li for his guidance and support. L.W. is supported by National Science and Technology Major Project (2022ZD0114902) and National Science Founda- tion of China (NSFC92470123, NSFC62276005). D.H. is supported by National Science Founda- tion of China (NSFC62376007). W.A.G. thanks the US NSF (CBET 231117) for support. J.C. is supported by the National Key R&D Program of China (2021YFA1400500) and National Science Foundation of China (12334003).

Competing interests. The authors declare no competing interests.

## References

[1] Michael G. Medvedev, Ivan S. Bushmarinov, Jianwei Sun, John P. Perdew, and Kon- stantin A. Lyssenko. Density functional the- ory is straying from the path toward the exact functional. Science, 355(6320):49–52, Jan- uary 2017. ISSN 1095-9203. doi: 10.1126/ science.aah5975. URL http://dx.doi.org/10. 1126/science.aah5975.

[2] Keld L Bak, Poul Jørgensen, Jeppe Olsen, Trygve Helgaker, and Jürgen Gauss. Coupled-cluster singles, doubles and triples (CCSDT) calculations of atomization ener- gies. Chemical Physics Letters, 317(1-2):116–122, 2000.

[3] Kirk A Peterson, David Feller, and David A Dixon. Chemical accuracy in ab initio thermochemistry and spectroscopy: current strategies and future challenges. Theoretical Chemistry Accounts, 131(1):1079, 2012.

[4] Giuseppe Carleo and Matthias Troyer. Solv- ing the quantum many-body problem with artificial neural networks. Science, 355(6325):602–606, 2017.

[5] Jan Hermann, Zeno Schätzle, and Frank Noé. Deep-neural-network solu- tion of the electronic Schrödinger equation. Nature Chemistry, 12(10):891–897, October 2020. ISSN 1755-4349. doi: 10.1038/s41557-020-0544-y. URL https://doi.org/10.1038/s41557-020-0544-y.

[6] David Pfau, James S. Spencer, Alexan- der G. D. G. Matthews, and W. M. C. Foulkes. Ab initio solution of the many-electron schrödinger equation with deep neural networks. Physical Review Research, 2(3), September 2020. ISSN 2643-1564. doi: 10.1103/physrevresearch. 2.033429. URL http://dx.doi.org/10.1103/PhysRevResearch.2.033429.

[7] He Li, Zun Wang, Nianlong Zou, Meng Ye, Runzhang Xu, Xiaoxun Gong, Wenhui Duan, and Yong Xu. Deep-learning density func- tional theory hamiltonian for efficient ab ini- tio electronic-structure calculation. Nature Computational Science, 2(6):367–377, 2022.

[8] Anand Chandrasekaran, Deepak Kamal, Rohit Batra, Chiho Kim, Lihua Chen, and Rampi Ramprasad. Solving the electronic structure problem with machine learning. npj Computational Materials, 5(1):22, 2019.

[9] Ruichen Li, Haotian Ye, Du Jiang, Xue- lan Wen, Chuwei Wang, Zhe Li, Xiang Li, Di He, Ji Chen, Weiluo Ren, and Liwei Wang. A computational framework for neural network-based variational Monte Carlo with Forward Laplacian. Nat Mach Intell, 6(2):209–219, February 2024. ISSN 2522-5839. doi: 10.1038/s42256-024-00794-x. URL https://www.nature.com/articles/ s42256-024-00794-x. Publisher: Nature Publishing Group.

[10] Zhe Li, Zixiang Lu, Ruichen Li, Xuelan Wen, Xiang Li, Liwei Wang, Ji Chen, and Weiluo Ren. Spin-symmetry-enforced solu- tion of the many-body Schrödinger equation

with a deep neural network. *Nature Computational Science*, 4(12):910-919, December 2024. ISSN 2662-8457. doi: 10.1038/s43588-024-00730-4. URL https://doi.org/10.1038/s43588-024-00730-4.

[11] David Pfau, Simon Axelrod, Halvard Suterud, Ingrid von Glehn, and James S. Spencer. Accurate computation of quantum excited states with neural networks. *Science*, 385(6711), August 2024. ISSN 1095-9203. doi: 10.1126/science.adn0137. URL http://dx.doi.org/10.1126/science.adn0137.

[12] Michael Scherbela, Nicholas Gao, Philipp Grohs, and Stephan Günnemann. Accurate ab-initio neural-network solutions to large-scale electronic structure problems. *arXiv preprint arXiv:2504.06087*, 2025.

[13] Weizhong Fu, Ryunosuke Fujimaru, Ruichen Li, Yuzhi Liu, Xuelan Wen, Xiang Li, Kenta Hongo, Liwei Wang, Tom Ichibha, Ryo Maezono, et al. Local pseudopotential unlocks the true potential of neural network-based quantum monte carlo. *arXiv preprint arXiv:2505.19909*, 2025.

[14] Adam Foster, Zeno Schätzle, P Bernát Szabó, Lixue Cheng, Jonas Köhler, Gino Cassella, Nicholas Gao, Jiawei Li, Frank Noé, and Jan Hermann. An ab initio foundation model of wavefunctions that accurately describes chemical bond breaking. *arXiv preprint arXiv:2506.19960*, 2025.

[15] Sandro Sorella. Generalized Lanczos algorithm for variational quantum monte carlo. *Phys. Rev. B*, 64:024512, Jun 2001. doi: 10.1103/PhysRevB.64.024512. URL https://link.aps.org/doi/10.1103/PhysRevB.64.024512.

[16] Kirill Neklyudov, Jannes Nys, Luca Thiede, Juan Felipe Carrasquilla Alvarez, qiang liu, Max Welling, and Alireza Makhzani. Wasserstein quantum monte carlo: A novel approach for solving the quantum many-body Schrödinger equation. In *Thirty-seventh Conference on Neural Information Processing Systems*, 2023. URL https://openreview.net/forum?id=pjSzKhSrfs.

[17] Jared Kaplan, Sam McCandlish, Tom Henighan, Tom B Brown, Benjamin Chess, Rewon Child, Scott Gray, Alec Radford, Jeffrey Wu, and Dario Amodei. Scaling laws for neural language models. *arXiv preprint arXiv:2001.08361*, 2020.

[18] Jonathan Tennyson, Sergei N Yurchenko, Ahmed F Al-Refaie, Emma J Barton, Katy L Chubb, Phillip A Coles, S Diamantopoulou, Maire N Gorman, Christian Hill, Aden Z Lam, et al. The ExoMol database: molecular line lists for exoplanet and other hot atmospheres. *Journal of Molecular Spectroscopy*, 327:73-94, 2016.

[19] Peter G. Burton and M. Dawn Harvey. Theoretical evidence for metastable cyclic ozone. *Nature*, 266(5605):826-827, April 1977. ISSN 1476-4687. doi: 10.1038/266826a0. URL http://dx.doi.org/10.1038/266826a0.

[20] Srinivasan Parthiban and Jan M. L. Martin. Fully ab initio atomization energy of benzene via Weizmann-2 theory. *The Journal of Chemical Physics*, 115(5):2051-2054, August 2001. ISSN 0021-9606. doi: 10.1063/1.1385363. URL https://doi.org/10.1063/1.1385363. .eprint: https://pubs.aip.org/aip/jcp/article-pdf/115/5/2051/19065141/2051_1_online.pdf.

[21] Weiluo Ren, Weizhong Fu, Xiaojie Wu, and Ji Chen. Towards the ground state of molecules via diffusion monte carlo on neural networks. *Nature Communications*, 14(1):1860, Apr 2023. ISSN 2041-1723. doi: 10.1038/s41467-023-37609-3. URL https://doi.org/10.1038/s41467-023-37609-3.

[22] Amir Karton, Shauli Daon, and Jan M. L. Martin. W4-11: A high-confidence benchmark dataset for computational thermochemistry derived from first-principles W4 data. *Chemical Physics Letters*, 510(4):165-178, 2011. ISSN 0009-2614. doi: https://doi.org/10.1016/j.cplett.2011.05.007. URL https://www.sciencedirect.com/science/article/pii/S0009261411005616.

[23] Subhas J. Chakravorty, Steven R. Gwaltney, Ernest R. Davidson, Farid A. Parpia,

15

and Charlotte Froese p Fischer. Ground- state correlation energies for atomic ions with3 to 18 electrons. Phys. Rev. A, 47:3649-3670, May 1993. doi: 10.1103/PhysRevA.47.3649. URL https://link.aps.org/doi/10.1103/ PhysRevA.47.3649.

[24] Garnet Kin-Lic Chan, Mihály Kállay, and Jürgen Gauss. State-of-the-art density matrix renormalization group and cou- pled cluster theory studies of the nitrogen binding curve. The Journal of Chemical Physics, 121(13):6110-6116, October 2004. ISSN 0021-9606. doi: 10.1063/1.1783212. URL https://doi.org/10.1063/1.1783212. eprint: https://pubs.aip.org/aip/jcp/article- pdf/121/13/6110/19201294/6110_1_online.pdf.

[25] Yasaman Bahri, Ethan Dyer, Jared Kaplan, Jaehoon Lee, and Utkarsh Sharma. Explain- ing neural scaling laws. Proceedings ofthe National Academy of Sciences, 121(27): e2311878121, 2024. doi: 10.1073/pnas.2311878121. URL https://www.pnas.org/ doi/abs/10.1073/pnas.2311878121.

[26] Joel Hestness, Sharan Narang, Newsha Ardalani, Gregory Diamos, Heewoo Jun, Has- san Kianinejad, Md. Mostofa Ali Patwary, Yang Yang, and Yanqi Zhou. Deep learning scaling is predictable, empirically, 2017. URL https://arxiv.org/abs/1712.00409.

[27] Tom Henighan, Jared Kaplan, Mor Katz, Mark Chen, Christopher Hesse, Jacob Jack- son, Heewoo Jun, Tom B. Brown, Prafulla Dhariwal, Scott Gray, Chris Hallacy, Ben- jamin Mann, Alec Radford, Aditya Ramesh, Nick Ryder, Daniel M. Ziegler, John Schul- man, Dario Amodei, and Sam McCandlish. Scaling laws for autoregressive generativemodeling, 2020. URL https://arxiv.org/abs/2010.14701.

[28] Tom B. Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared Kaplan, Pra- fulla Dhariwal, Arvind Neelakantan, Pranav Shyam, Girish Sastry, Amanda Askell, Sand- hini Agarwal, Ariel Herbert-Voss, Gretchen Krueger, Tom Henighan, Rewon Child, Aditya Ramesh, Daniel M. Ziegler, Jeffrey Wu, Clemens Winter, Christopher Hesse, Mark Chen, Eric Sigler, Mateusz Litwin, Scott Gray, Benjamin Chess, Jack Clark, Christopher Berner, Sam McCandlish, Alec Radford, Ilya Sutskever, and Dario Amodei. Language models are few-shot learners, 2020. URL https://arxiv.org/abs/2005.14165.

[29] Jared Kaplan, Sam McCandlish, T. J. Henighan, Tom B. Brown, Benjamin Chess, Rewon Child, Scott Gray, Alec Radford, Jeff Wu, and Dario Amodei. Scaling laws for neu- ral language models. ArXiv, abs/2001.08361,2020. URL https://api.semanticscholar.org/ CorpusID:210861095.

[30] Jordan Hoffmann, Sebastian Borgeaud, Arthur Mensch, Elena Buchatskaya, Trevor Cai, Eliza Rutherford, Diego de Las Casas, Lisa Anne Hendricks, Johannes Welbl, Aidan Clark, Tom Hennigan, Eric Noland, Katie Millican, George van den Driess- che, Bogdan Damoc, Aurelia Guy, Simon Osindero, Karen Simonyan, Erich Elsen, Jack W. Rae, Oriol Vinyals, and Lau- rent Sifre. Training compute-optimal large language models, 2022. URL https://arxiv.org/abs/2203.15556.

[31] Xiaohua Zhai, Alexander Kolesnikov, Neil Houlsby, and Lucas Beyer. Scaling vision transformers. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), pages12104-12113, June 2022.

[32] Mitchell A Gordon, Kevin Duh, and Jared Kaplan. Data and parameter scaling laws for neural machine translation. In Marie- Francine Moens, Xuanjing Huang, Lucia Spe- cia, and Scott Wen-tau Yih, editors, Pro- ceedings of the 2021 Conference on Empiri- cal Methods in Natural Language Processing, pages 5915-5922, Online and Punta Cana, Dominican Republic, November 2021. Associ- ation for Computational Linguistics. doi: 10.18653/v1/2021.emnlp-main.478. URL https://aclanthology.org/2021.emnlp-main.478/.

[33] Max Geier, Khachatur Nazaryan, Timothy Zaklama, and Liang Fu. Self-attention neural

network for solving correlated electron prob- lems in solids. Phys. Rev. B, 112:045119, Jul 2025. doi: 10.1103/qxc3-bkc7. URL https://link.aps.org/doi/10.1103/qxc3-bkc7.

[34] Enzo Monino, Martial Boggio-Pasqua, Anthony Scemama, Denis Jacquemin, and Pierre-François Loos. Reference energies for cyclobutadiene: Automerization and excited states. The Journal of Physical Chemistry A, 126(28):4664-4679, July 2022. ISSN 1520-5215. doi: 10.1021/acs.jpca.2c02480. URL http://dx.doi.org/10.1021/acs.jpca.2c02480.

[35] Dmitry I. Lyakh, Victor F. Lotrich, and Rod-ney J. Bartlett. The 'tailored' CCSD(T) description of the automerization of cyclobutadiene. Chemical Physics Letters, 501(4-6):166-171, January 2011. ISSN 0009-2614. doi: 10.1016/j.cplett.2010.11.058. URL http://dx.doi.org/10.1016/j.cplett.2010.11.058.

[36] Duy-Khoi Dang, Joshua A. Kammraad, and Paul M. Zimmerman. Advances in paral-lel heat bath configuration interaction. The Journal of Physical Chemistry A, 127(1):400-411, December 2022. ISSN 1520-5215. doi: 10.1021/acs.jpca.2c07949. URL http://dx.doi.org/10.1021/acs.jpca.2c07949.

[37] Jeffrey Hatch, Alan E. Rask, Duy-Khoi Dang, and Paul M. Zimmerman. Many-body basis set amelioration method for incremental full configuration interaction. The Journal of Physical Chemistry A, 129(16):3743-3753,April 2025. ISSN 1520-5215. doi: 10.1021/acs.jpca.5c01521. URL http://dx.doi.org/10.1021/acs.jpca.5c01521.

[38] David W. Whitman and Barry K. Carpen-ter. Limits on the activation parameters for automerization of cyclobutadiene-1,2-d2. Journal of the American Chemical Society,104(23):6473-6474, November 1982. ISSN 1520-5126. doi: 10.1021/ja00387a065. URL http://dx.doi.org/10.1021/ja00387a065.

[39] Robert J Le Roy, Yiye Huang, and Calvin Jary. An accurate analytic potential function for ground-state $N_2$ from a direct-potential-fit analysis of spectroscopic data. The Journal of chemical physics, 125(16), 2006.

[40] Russ R. Laher and Forrest R. Gilmore. Improved fits for the vibrational and rota-tional constants of many states of nitrogen and oxygen. Journal of Physical and Chemi-cal Reference Data, 20(4):685-712, July 1991. ISSN 1529-7845. doi:10.1063/1.555892. URL http://dx.doi.org/10.1063/1.555892.

[41] Robert J. Gdanitz. Accurately solving the electronic Schrödinger equation of atoms and molecules using explicitly correlated (r12-)MR-CI: the ground state potential energy curve of $N_2$. Chemical Physics Letters,283(5-6):253-261, February 1998. ISSN 0009-2614. doi: 10.1016/s0009-2614(97)01392-4. URL http://dx.doi.org/10.1016/S0009-2614(97)01392-4.

[42] Leon Gerard, Michael Scherbela, Philipp Marquetand, and Philipp Grohs. Gold-standard solutions to the schrödinger equation using deep learning: How much physics do we need? In Alice H. Oh, Alekh Agarwal, Danielle Belgrave, and Kyunghyun Cho, editors, Advances in Neural Informa-tion Processing Systems, 2022. URL https://openreview.net/forum?id=nX-gReQ0OT.

[43] Nicholas Gao and Stephan Günnemann. Neu-ral Pfaffians: Solving many many-electron Schrödinger equations. Advances in Neural Information Processing Systems, 37:125336-125369, 2024.

[44] Nicholas Gao and Stephan Günnemann. Gen-eralizing neural wave functions. arXiv preprint arXiv:2302.04168, 2023.

[45] Jesús R. Flores and Robert J. Gdanitz. Accurately solving the electronic schrödinger equation of small atoms and molecules using explicitly correlated (r12-)mr-ci. viii. valence excited states of methylene (ch2). The Jour-nal of Chemical Physics, 123(14), October 2005. ISSN 1089-7690. doi: 10.1063/1.2055207. URL http://dx.doi.org/10.1063/1.2055207.

[46] Zoltan Varga, Yuliya Paukku, and Don-ald G. Truhlar. Potential energy surfaces for $O+O_2$ collisions. The Journal of Chemi-cal Physics, 147(15):154312, October 2017.


ISSN 0021-9606. doi: 10.1063/1.4997169.
URL https://doi.org/10.1063/1.4997169.
_eprint: https://pubs.aip.org/aip/jcp/article-
pdf/doi/10.1063/1.4997169/15538054/154312_1_online.pdf

[47] Yinan Shu, Zoltan Varga, Dayou Zhang, and Donald G. Truhlar. ChemPotPy: A Python Library for Analytic Representations of Potential Energy Surfaces and Diabatic Potential Energy Matrices. The Journal of Physical Chemistry A, 127(45):9635-9640, November 2023. ISSN 1089-5639. doi: 10.1021/acs.jpca.3c05899. URL https://doi.org/10.1021/acs.jpca.3c05899. Publisher: American Chemical Society.

[48] James S. Wright. Theoretical evidence for a stable form of cyclic ozone, and its chemical consequences. Canadian Journal of Chemistry, 51(1):139-146, January 1973. ISSN 1480-3291. doi: 10.1139/v73-020. URL http://dx.doi.org/10.1139/v73-020.

[49] Shingkuo Shih, Robert J. Buenker, and Sigrid D. Peyerimhoff. Theoretical investigation of the cyclic conformer of ozone. Chemical Physics Letters, 28(4):463-470, October 1974. ISSN 0009-2614. doi: 10.1016/0009-2614(74)80080-1. URL http://dx.doi.org/10.1016/0009-2614(74)80080-1.

[50] Lawrence B Harding and William A Goddard III. Ab initio theoretical results on the stability of cyclic ozone. The Journal of Chemical Physics, 67(5):2377-2379, 1977.

[51] Sotiris S. Xantheas, Gregory J. Atchity, Stephen T. Elbert, and Klaus Ruedenberg. Potential energy surfaces of ozone. I. The Journal of Chemical Physics, 94(12):8054-8069, June 1991. ISSN 1089-7690. doi: 10.1063/1.460140. URL http://dx.doi.org/10.1063/1.460140.

[52] Antonio Banichevich and Sigrid D. Peyerimhoff. Theoretical study of the ground and excited states of ozone in its symmetric nuclear arrangement. Chemical Physics, 174(1):93-109, July 1993. ISSN 0301-0104. doi: 10.1016/0301-0104(93)80054-d. URL http://dx.doi.org/10.1016/0301-0104(93)80054-D.

[53] Gregory J. Atchity and Klaus Ruedenberg. Global potential energy surfaces for the lowest two $1A'$ states of ozone. Theoretical Chemistry Accounts: Theory, Computation, and Modeling (Theoretica Chimica Acta), 96(3):176-194, August 1997. ISSN 1432-2234. doi: 10.1007/s002140050220. URL http://dx.doi.org/10.1007/s002140050220.

[54] Zheng-Wang Qu, H Zhu, and Reinhard Schinke. Infrared spectrum of cyclic ozone: A theoretical investigation. The Journal of chemical physics, 123(20), 2005.

[55] Jien-Lian Chen and Wei-Ping Hu. Theoretical prediction on the thermal stability of cyclic ozone and strong oxygen tunneling. Journal of the American Chemical Society, 133(40):16045-16053, September 2011. ISSN 1520-5126. doi: 10.1021/ja203428x. URL http://dx.doi.org/10.1021/ja203428x.

[56] Daniel Theis, Joseph Ivanic, Theresa L. Windus, and Klaus Ruedenberg. The transition from the open minimum to the ring minimum on the ground state and on the lowest excited state of like symmetry in ozone: A configuration interaction study. The Journal of Chemical Physics, 144(10), March 2016. ISSN 1089-7690. doi: 10.1063/1.4942019. URL http://dx.doi.org/10.1063/1.4942019.

[57] Jeffery S Boschen, Daniel Theis, Klaus Ruedenberg, and Theresa L Windus. Correlation energy extrapolation by many-body expansion. The Journal of Physical Chemistry A, 121(4):836-844, 2017.

[58] Alan D. Chien, Adam A. Holmes, Matthew Otten, C. J. Umrigar, Sandeep Sharma, and Paul M. Zimmerman. Excited states of methylene, polyenes, and ozone from heat-bath configuration interaction. The Journal of Physical Chemistry A, 122(10):2714-2722, February 2018. ISSN 1520-5215. doi: 10.1021/acs.jpca.8b01554. URL http://dx.doi.org/10.1021/acs.jpca.8b01554.

[59] Eugenio Vitale, Ali Alavi, and Daniel Kats. FCIQMC-tailored distinguishable cluster approach. Journal of Chemical Theory and Computation, 16(9):5621-5634, July
18

2020. ISSN 1549-9626. doi: 10.1021/acs.jctc.0c00470. URL http://dx.doi.org/10.1021/acs.jctc.0c00470.

[60] Zoltan Varga, Yinan Shu, Jiaxin Ning, and Donald G Truhlar. Diabatic potential energy surfaces and semiclassical multi-state dynamics for fourteen coupled $^3\Lambda'$ states of $O_3$. Electronic Structure, 4(4):047002, November 2022. ISSN 2516-1075. doi: 10.1088/2516-1075/ac94ac. URL http://dx.doi.org/10.1088/2516-1075/ac94ac.

[61] Gerhard Herzberg. Molecular spectra and molecular structure. Vol. 3: Electronic spectra and electronic structure of polyatomic molecules. Van Nostrand, 1966.

[62] Russell Johnson. Computational chemistry comparison and benchmark database http://cccbdb.nist.gov/ doi:10.18434/t47c7z. Technical report, 04 2018.

[63] Diptarka Hait and Martin Head-Gordon. How accurate is density functional theory at predicting dipole moments? an assessment using a new database of 200 benchmark values. Journal of Chemical Theory and Computation, 14(4):1969–1981, April 2018. ISSN 1549-9618. doi: 10.1021/acs.jctc.7b01252. URL https://doi.org/10.1021/acs.jctc.7b01252. Publisher: American Chemical Society.

[64] Thom H. Dunning. Gaussian basis sets for use in correlated molecular calculations. I. the atoms boron through neon and hydrogen. The Journal of Chemical Physics, 90(2):1007–1023, January 1989. ISSN 1089-7690. doi: 10.1063/1.456153. URL http://dx.doi.org/10.1063/1.456153.

[65] David Feller, Kirk A. Peterson, and J. Grant Hill. On the effectiveness of CCSD(T) complete basis set extrapolations for atomization energies. The Journal of Chemical Physics, 135(4), July 2011. ISSN 1089-7690. doi: 10.1063/1.3613639. URL http://dx.doi.org/10.1063/1.3613639.

[66] Amir Karton. Effective basis set extrapolations for CCSDT, CCSDT(Q), and CCSDTQ correlation energies. The Journal of Chemical Physics, 153(2), July 2020. ISSN 1089-7690. doi: 10.1063/5.0011674. URL http://dx.doi.org/10.1063/5.0011674.

[67] Diptarka Hait, Yu Hsuan Liang, and Martin Head-Gordon. Too big, too small, or just right? a benchmark assessment of density functional theory for predicting the spatial extent of the electron density of small chemical systems. The Journal of Chemical Physics, 154(7), February 2021. ISSN 1089-7690. doi: 10.1063/5.0038694. URL http://dx.doi.org/10.1063/5.0038694.

[68] Qiming Sun, Xing Zhang, Samragni Banerjee, Peng Bao, Marc Barbry, Nick S. Blunt, Nikolay A. Bogdanov, George H. Booth, Jia Chen, Zhi-Hao Cui, Janus J. Eriksen, Yang Gao, Sheng Guo, Jan Hermann, Matthew R. Hermes, Kevin Koh, Peter Koval, Susi Lehtola, Zhendong Li, Junzi Liu, Narbe Mardirossian, James D. McClain, Mario Motta, Bastien Mussard, Hung Q. Pham, Artem Pulkin, Wirawan Purwanto, Paul J. Robinson, Enrico Ronca, Elvira R. Sayfutyarova, Maximilian Scheurer, Henry F. Schurkus, James E. T. Smith, Chong Sun, Shi-Ning Sun, Shiv Upadhyay, Lucas K. Wagner, Xiao Wang, Alec White, James Daniel Whitfield, Mark J. Williamson, Sebastian Wouters, Jun Yang, Jason M. Yu, Tianyu Zhu, Timothy C. Berkelbach, Sandeep Sharma, Alexander Yu. Sokolov, and Garnet Kin-Lic Chan. Recent developments in the pjscp¿yj/scp¿scf program package. The Journal of Chemical Physics, 153(2), July 2020. ISSN 1089-7690. doi: 10.1063/5.0006074. URL http://dx.doi.org/10.1063/5.0006074.

[69] Zhen Guo, Zigeng Huang, Qiaorui Chen, Jiang Shao, Guangcheng Liu, Hung Q. Pham, Yifei Huang, Changsu Cao, Ji Chen, and Dingshun Lv. ByteQC: GPU-accelerated quantum chemistry package for large-scale systems. WIREs Computational Molecular Science, 15(3):e70034, 2025. doi: 10.1002/wcms.70034. e70034 CMS-1169.R1.

[70] Lixue Cheng, P Bernát Szabó, Zeno Schätzle, Derk P Kooi, Jonas Köhler, Klaas JH Gies- bertz, Frank Noé, Jan Hermann, Paola Gori- Giorgi, and Adam Foster. Highly accurate real-space electron densities with neural net- works. *The Journal of Chemical Physics*, 162 (3), 2025.

[71] Ruojing Peng and Garnet Kin Chan. An analysis of first-and second-order optimiza- tion algorithms in variational monte carlo. *arXiv preprint arXiv:2502.19576*, 2025.

[72] G.H. Golub and C.F. Van Loan. *Matrix Computations*. Johns Hopkins Studies in the Mathematical Sciences. Johns Hopkins Uni- versity Press, 2013. ISBN 978-1-4214-0794-4. URL https://books.google.co.jp/books?id=X5YfsuCWpxMC.

[73] Anthony Zee. *Quantum Field Theory in a Nutshell: Second Edition*. Princeton Univer- sity Press, February 2010. ISBN 978-1-4008-3532-4. Google-Books-ID: n8Mmbjtco78C.

[74] Ingrid von Glehn, James S Spencer, and David Pfau. A self-attention ansatz for ab- initio quantum chemistry. In *The Eleventh International Conference on Learning Repre- sentations*, 2023. URL https://openreview.net/forum?id=xveTeHIVlF7j.

[75] Zeno Schätzle, PB Szabó, Matěj Mezera, Jan Hermann, and Frank Noé. Deepqmc: An open-source software suite for variational optimization of deep-learning molecular wave functions. *The Journal of Chemical Physics*, 159(9), 2023.

[76] Michael R. Zhang, James Lucas, Geoffrey Hinton, and Jimmy Ba. *Lookahead opti- mizer: k steps forward, 1 step back*. Curran Associates Inc., Red Hook, NY, USA, 2019.

[77] James Martens and Roger Grosse. Optimiz- ing neural networks with kronecker-factored approximate curvature. In *Proceedings of the 32nd International Conference on Inter- national Conference on Machine Learning - Volume 37*, ICML'15, page 2408-2417. JMLR.org, 2015.

[78] Mohammad Rasool Izadi, Yihao Fang, Robert L. Stevenson, and Lizhen Lin. Opti- mization of graph neural networks with nat- ural gradient descent. *2020 IEEE Interna- tional Conference on Big Data (Big Data)*, pages 171-179, 2020. URL https://api.semanticscholar.org/CorpusID:221266818.

[79] Diederik P. Kingma and Jimmy Ba. Adam: A method for stochastic optimization. *CoRR*, abs/1412.6980, 2014. URL https://api.semanticscholar.org/CorpusID:6628106.

[80] Weizhong Fu, Weiluo Ren, and Ji Chen. Variance extrapolation method for neural- network variational monte carlo. *Machine Learning: Science and Technology*, 5(1):015016, jan 2024. doi: 10.1088/2632-2153/ad1f75. URL https://dx.doi.org/10.1088/2632-2153/ad1f75.

# Supplementary Information

## Contents

1  Look-Ahead Variational Algorithm (LAVA)  2
1.1  Schema and hyperparameters  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2
1.2  Energy comparison against VMC . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2

2  Neural scaling laws  3
2.1  Comparison against scaling of VMC  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3
2.2  Discussion on embarrassingly parallel computing  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3

3  Extrapolation  6

4  Total atomization energy  7
4.1  How to derive abs. energy benchmark from TAE experiments . . . . . . . . . . . . . . . . . . . . . . . . . 7
4.2  Atomic energies . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7
4.3  Discrepancy between experimental and theoretical thermochemistry  . . . . . . . . . . . . . . . . . . . . . 7
4.4  Absolute energies for benzene  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8
4.5  Absolute energies for molecules from W4-11 dataset  . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8

5  Polyene chains  10

6  Cyclobutadiene automerization barrier  10
6.1  Experimental barrier with large uncertainty  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11
6.2  Complete basis set extrapolation  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11
6.3  Available experimental observables of cyclobutadiene . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11
6.4  Comparison of cyclobutadiene automerization barrier from various theoretical methods  . . . . . . . . . . . 12

7  New benchmark for $N_2$ potential energy curve  14
7.1  Solving effective radial Schrödinger equation  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14
7.2  Fitting analytic potential function $V(r)$  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14
7.3  Expanded Morse oscillator function $V_{\text{EMO}}(r)$  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14
7.4  Morse/long-range potential function $V_{\text{MLR}}(r)$  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15
7.5  Low-lying vibrational levels for $v$=0-19  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16
7.6  High-lying vibrational levels for $v$=20-61  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16
7.7  LAVA scaling laws across the PEC . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17

8  $O_3$ reaction barrier  18
8.1  Optimized geometries from various theoretical methods . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18
8.2  Energy landscape based on different PESs  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18
8.3  Half-life estimation  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21
8.4  Oxygen tunneling  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21
8.5  LAVA scaling laws for ozone  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22
8.6  Improve spin symmetry and spatial symmetry of wavefunctions by scaling up network size  . . . . . . . . . . . 22

9  Dipole moments and TAE for multireference molecules  23
9.1  Multireference diagnostics  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23
9.2  Dipole moment  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23


### Supplementary Note 1. Look-Ahead Variational Algorithm (LAVA)

Now we illustrate in detail the effectiveness of our LAVA-based approach. First, as an optimization framework, LAVA achieves much better accuracy, especially for systems challenging for QMC calculations. For instance, for systems involving heavier atoms, such as Sulfor and Chlorine, NNQMC approaches struggle due to the large number of inner electrons. Nonetheless, LAVA can achieve significant accuracy improvement and successfully reach chemical accuracy.

The same holds for strongly correlated systems such as $\text{O}_3$. We directly compare LAVA and NNVMC in Supplementary Note 1.2.

### Supplementary Note 1.1 Schema and hyperparameters

All reported algorithms were implemented in JAX [3]. The LAVA distributed calculations used A800 GPUs. The hyperparameters are in Table S1. In particular, for benzene, we use 2 MCMC blocks to ensure good mixing. For large networks, we observed that for certain systems, 3e5 iterations are not sufficient for good convergence, so we increased it to 4e5 or 5e5 if local energy variance at least decreased by half during the last 5e4 iterations. As for denoting network configurations, we use 4-tuples that consist of depth, width, the number of attention heads, and the number of determinants in the following sections.

#### Supplementary Table 1 | Default hyperparameters.

<table>
  <thead>
    <tr>
      <th colspan="2">Parameter</th>
      <th>Value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="9">Training</td>
      <td>Optimizer</td>
      <td>Adam-KFAC</td>
    </tr>
    <tr>
      <td>Optimizer for intermediate steps</td>
      <td>KFAC</td>
    </tr>
    <tr>
      <td>Iterations</td>
      <td>3e5</td>
    </tr>
    <tr>
      <td>Batch size</td>
      <td>4096</td>
    </tr>
    <tr>
      <td>$\eta$ at iteration $t$</td>
      <td>$5\text{e-}4/\left(1+\frac{t}{t_{\text{delay}}}\right)$</td>
    </tr>
    <tr>
      <td>$\eta_{\text{temp}}$ at iteration $t$</td>
      <td>$5\text{e-}3\cdot\min\left\{1,\frac{t}{t_{\text{warmup}}}\right\}/\left(1+\frac{\max\{t,t_{\text{warmup}}\}}{t_{\text{delay}}}\right)$</td>
    </tr>
    <tr>
      <td>Learning rate decay $t_{\text{delay}}$</td>
      <td>1e4</td>
    </tr>
    <tr>
      <td>Linear warmup iterations $t_{\text{warmup}}$</td>
      <td>1e5</td>
    </tr>
    <tr>
      <td>Local energy clipping</td>
      <td>5.0</td>
    </tr>
    <tr>
      <td rowspan="2">Inference</td>
      <td>Iterations for energy evaluation</td>
      <td>3e4</td>
    </tr>
    <tr>
      <td>Iterations for dipole evaluation</td>
      <td>1e6</td>
    </tr>
    <tr>
      <td rowspan="4">Pretraining</td>
      <td>Optimizer</td>
      <td>LAMB</td>
    </tr>
    <tr>
      <td>Iterations</td>
      <td>2e4</td>
    </tr>
    <tr>
      <td>Basis set</td>
      <td>aug-cc-pVDZ</td>
    </tr>
    <tr>
      <td>Learning rate</td>
      <td>3e-4</td>
    </tr>
    <tr>
      <td rowspan="3">MCMC</td>
      <td>Decorrelation steps</td>
      <td>30</td>
    </tr>
    <tr>
      <td>Proposal standard deviation</td>
      <td>0.02</td>
    </tr>
    <tr>
      <td>Blocks</td>
      <td>1</td>
    </tr>
    <tr>
      <td rowspan="4">KFAC</td>
      <td>Norm constraint</td>
      <td>$1\text{e-}7\cdot\left(\min\left\{1,\frac{t}{t_{\text{warmup}}}\right\}/\left(1+\frac{\max\{t,t_{\text{warmup}}\}}{t_{\text{delay}}}\right)\right)^2$</td>
    </tr>
    <tr>
      <td>Damping</td>
      <td>1e-3</td>
    </tr>
    <tr>
      <td>Momentum</td>
      <td>0</td>
    </tr>
    <tr>
      <td>Covariance moving average decay</td>
      <td>0.95</td>
    </tr>
    <tr>
      <td rowspan="6">Adam-KFAC</td>
      <td>Norm constraint</td>
      <td>1e-6</td>
    </tr>
    <tr>
      <td>Damping</td>
      <td>5e-3</td>
    </tr>
    <tr>
      <td>Momentum decay rate $\beta_1$</td>
      <td>0.9</td>
    </tr>
    <tr>
      <td>Squared gradients decay rate $\beta_2$</td>
      <td>0.99</td>
    </tr>
    <tr>
      <td>$\epsilon$</td>
      <td>1e-10</td>
    </tr>
    <tr>
      <td>Covariance moving average decay</td>
      <td>0.95</td>
    </tr>
  </tbody>
</table>

### Supplementary Note 1.2 Energy comparison against VMC

For the LAVA ablation study, we compared energy results with default settings for several systems. LapNet baseline for NNVMC optimization uses default hyperparameters as described in [38], except for the number of iterations, which is increased to 1e6 (specifically 1.35e6 for benzene) so as to make the total computational time costs similar. In the following sections, we refer to the LapNet

baseline as NNVMC. For both methods, we use the default network, denoted as (4,256,4,32), with 256 hidden dimensions, 4 atten- tion heads, 4 layers, and 32 determinants (in particular 64 determinants for ozone open-ring minimum species). Results are shown in Table S2. LAVA performs significantly better in absolute energy compared to the NNVMC baseline with comparable time costs.

Supplementary Table 2 | LAVA vs. NNVMC energy results with similar time costs.

<table>
  <thead>
    <tr>
      <th>Molecule</th>
      <th>LAVA (Ha)</th>
      <th>NNVMCᵃ(Ha)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Cyclobutadiene (Rectangle)</td>
      <td>−154.686 06(3)</td>
      <td>−154.684 13(4)</td>
    </tr>
    <tr>
      <td>Cyclobutadiene (Square)</td>
      <td>−154.669 53(3)</td>
      <td>−154.667 97(5)</td>
    </tr>
    <tr>
      <td>O₃</td>
      <td>−225.435 57(3)</td>
      <td>−225.434 33(5)</td>
    </tr>
    <tr>
      <td>SO₂</td>
      <td>−548.657 02(8)</td>
      <td>−548.6484(1)</td>
    </tr>
    <tr>
      <td>Cl₂</td>
      <td>−920.3889(2)</td>
      <td>−920.3832(2)</td>
    </tr>
    <tr>
      <td>F₂O₂</td>
      <td>−349.844 15(6)</td>
      <td>−349.8336(1)</td>
    </tr>
    <tr>
      <td>Benzene</td>
      <td>−232.246 89(5)</td>
      <td>−232.243 88(6)</td>
    </tr>
  </tbody>
</table>

ᵃ LapNet is used as the baseline.

Supplementary Note 2. Neural scaling laws

The second important component of our approach is the neural scaling laws towards exactness, which is universal across all the tested systems. As investigated in detail in artificial intelligence literature, neural scaling laws state that with larger model size and compute resources, the performance of deep neural networks improves predictably following a power law. In the main text, we have demonstrated such a phenomenon among a number of systems with reliable experimental benchmarks. And the scaling law of our LAVA-based approach is significantly more efficient than the couple-cluster method in terms of approaching exactness.

Moreover, across all the neural scaling law patterns, we discovered a simple but evident linear relationship between the energy expectation and the local energy variance of different neural network wavefunctions, which can be used to devise a straightforward extrapolation scheme. We discuss the scheme in Supplementary Note 3. The extrapolated energies are denoted as $E_{SE}$.

As mentioned in Method, we also have general power-law scaling trends between local energy variance $\text{Var}[E_L]$ and the number of parameters $N_p$. For systems without any reliable experimental reference, we can evaluate scaling laws by checking linear relationships between $\ln |E - E_{SE}|$ or $\ln \text{Var}[E_L]$ with $\ln N_p$. In Fig. S1 and Fig. S2, we first take benzene as an example, and afterwards illustrate probability distributions of $r^2$ statistics and power-law exponents for all systems involved in our scaling laws calculations.

Supplementary Note 2.1 Comparison against scaling of VMC

Fig. S3 and Fig. S4 demonstrate the distinct power-law scaling behavior of LAVA compared to NNVMC. LAVA exhibits clear power-law scaling trends across both test systems, cyclobutadiene and ozone equilibrium, indicating that its accuracy improves sys- tematically and efficiently as computational resources increase. In contrast, NNVMC shows significantly worse power-law scaling on the cyclobutadiene system, and, notably, fails to achieve a good power-law scaling on the ozone equilibrium (open-ring mini- mum) geometry. This comparison highlights LAVA's superiority over NNVMC in consistent systematic improvability via power-law scaling.

Supplementary Note 2.2 Discussion on embarrassingly parallel computing

LAVA benefits significantly from parallel computing due to its largely independent and homogeneous operations (e.g., matrix multi- plications and element-wise functions), which can be efficiently distributed across many processors using data parallelism. In contrast, coupled cluster (CC) methods are not naturally parallelizable and constrained by inherent sequential dependencies in their iterative equations and severe communication overhead for redistributing high-dimensional intermediate tensors. CC's strict synchroniza- tion requirements, sensitivity to numerical approximations, and irregular computation patterns fundamentally limit parallel speedup, making scalability beyond modest problem sizes challenging. Guo et al [16] recently developed ByteQC, a GPU-accelerated quan- tum chemistry package featuring CCSD and CCSD(T) modules. In mean-field calculations, electron repulsion integrals (ERIs) with $\mathcal{O}(N^4)$ scaling and tensor contractions between rank-6 tensors in CCSD(T) energy calculations grow rapidly in size with increasing system size $N$, exceeding CPU/GPU memory capacity. Consequently, data transfers between disk and CPU/GPU memory emerge as a bottleneck for large systems, impeding parallelization.

Supplementary Figure 1 | Power-law scaling trends between energy difference $E-E_{\text{SE}}$ and the number of parameters $N_p$.

![](./images/1159463098931740672_13.jpg)

![](./images/1159463098931740672_14.jpg)

![](./images/1159463098931740672_15.jpg)

![](./images/1159463098931740672_16.jpg)

Supplementary Figure 3 | LAVA vs. NNVMC scaling-up performance for rectangular cyclobutadiene.

![](./images/1159463098931740672_17.jpg)


**Supplementary Figure 4** | LAVA vs. NNVMC scaling-up performance for open-minimum ozone.

![](./images/1159463098931740672_18.jpg)

### Supplementary Note 3. Extrapolation

For all LAVA calculations, we universally observe that

$$
E \approx kV + \hat{E}_0, \tag{1}
$$

given results $E$ and $V$ from optimized models of different scales. The zero-variance principle directly shows that $E_0 \approx \hat{E}_0$. We take benzene as an example and illustrate this relationship and corresponding $r^2$ statistics in Fig. S5. Some similar variance-energy linear relationships in VMC are reported in previous works such as Hu et al [24], Iqbal et al [25], Kwon et al [31, 32], Moreno et al [42], Taddei et al [51], and Fu et al [12]. Although there is no clear reason for the existence of this linear relationship [31, 32], Fu et al [12] has provided some sufficient and necessary conditions for further understanding.

**Supplementary Figure 5** | LAVA scaling law extrapolation for benzene.

![](./images/1159463098931740672_19.jpg)

### Supplementary Note 4. Total atomization energy

### Supplementary Note 4.1 How to derive abs. energy benchmark from TAE experiments

Based on experimental and W4 total atomization energy (TAE) reference value $\Delta E_{\text{TAE}}$ from Karton et al [29] and absolute atom energies from Chakravorty et al [5], the absolute energy of a molecule is given derived by $\sum_I E_I - \Delta E_{\text{TA}}$, where $\{ E_I \}_{I=1}^M$ are absolute atom energies of all $M$ constituent atoms in the molecule. As described by Karton et al [29], ATcT [47] provides $\text{TAE}_0$ reference values, namely zero-point inclusive, relativistic, DBOC (Diagonal Born-Oppenheimer Correction) total atomization energies at absolute zero temperature. With thermodynamic correction based on translational, rotational, and vibrational partition functions, one can obtain the TAE at the temperature of experimental conditions or the room temperature 298 K. W4 theory also subtracts the non-electronic contributions from $\text{TAE}_0$ and provides zero-point exclusive, non-relativistic, clamped-nuclei $\text{TAE}_e$ for direct comparison with electronic structure calculations [29].

### Supplementary Note 4.2 Atomic energies

For the elements in period 2, LAVA-SE results perfectly agree with the experiment-derived atomic energies [5] within 0.1 mHa difference, as shown in Table S3. We use the experiment-derived atomic energies to calculate the W2.2, W4, and experiment-derived molecular absolute energies in Table S6.

#### Supplementary Table 3 | Atomic energies from various methods in Hartrees.

<table>
  <thead>
    <tr>
      <th>Molecule</th>
      <th>DMC[48] (Ha)</th>
      <th>FermiNet[43] (Ha)</th>
      <th>NNVMCᵃ (Ha)</th>
      <th>LAVA-SE (Ha)</th>
      <th>Expt. Derived[5] (Ha)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>C</td>
      <td>−37.844 46(6)</td>
      <td>−37.844 71(5)</td>
      <td>−37.844 811</td>
      <td>-37.8449</td>
      <td>−37.8450</td>
    </tr>
    <tr>
      <td>N</td>
      <td>−54.588 67(8)</td>
      <td>−54.588 82(6)</td>
      <td>−54.589 029</td>
      <td>-54.5891</td>
      <td>−54.5892</td>
    </tr>
    <tr>
      <td>O</td>
      <td>−75.0654(1)</td>
      <td>−75.066 55(7)</td>
      <td>−75.066 989</td>
      <td>-75.0672</td>
      <td>−75.0673</td>
    </tr>
    <tr>
      <td>F</td>
      <td>−99.7318(1)</td>
      <td>−99.7329(1)</td>
      <td>−99.733 559</td>
      <td>-99.7339</td>
      <td>−99.7339</td>
    </tr>
  </tbody>
</table>

ᵃ LapNet is used as the baseline.

For the elements in period 3, in contrast, the atomic energies of LAVA's lowest variational energies of the (4, 512, 8, 128) network configuration are lower than those derived from the experiment, as shown in Table S4 and Fig. S6. Because LAVA obeys the variational principle, we suggest using LAVA results as the new benchmark.

#### Supplementary Table 4 | LAVA's lowest variational energies for third-row atoms.

<table>
  <thead>
    <tr>
      <th>Molecule</th>
      <th>LAVA (Ha)</th>
      <th>Expt. Derived[5] (Ha)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Ne</td>
      <td>−128.937 943(7)</td>
      <td>−128.9376</td>
    </tr>
    <tr>
      <td>Na</td>
      <td>−162.255 09(9)</td>
      <td>−162.2546</td>
    </tr>
    <tr>
      <td>Mg</td>
      <td>−200.053 59(1)</td>
      <td>−200.0530</td>
    </tr>
    <tr>
      <td>Al</td>
      <td>−242.346 87(2)</td>
      <td>−242.3460</td>
    </tr>
    <tr>
      <td>Si</td>
      <td>−289.359 43(2)</td>
      <td>−289.3590</td>
    </tr>
    <tr>
      <td>P</td>
      <td>−341.259 25(2)</td>
      <td>−341.2590</td>
    </tr>
    <tr>
      <td>S</td>
      <td>−398.110 87(3)</td>
      <td>−398.1100</td>
    </tr>
    <tr>
      <td>Cl</td>
      <td>−460.150 45(4)</td>
      <td>−460.1480</td>
    </tr>
    <tr>
      <td>Ar</td>
      <td>−527.544 07(5)</td>
      <td>−527.5400</td>
    </tr>
  </tbody>
</table>

### Supplementary Note 4.3 Discrepancy between experimental and theoretical thermochemistry

Since LAVA is variational, it is theoretically guaranteed to give upper bounds of ground state energies. For third-row atoms and certain molecules, we observed that LAVA's best variational energies are lower than experimental-derived reference values, as plotted in Fig. S6, which indicates that LAVA's absolute energy results are more reliable for such systems.

In particular, there are several cases where experimental measurements and theoretical prediction have discrepancy, such as $\text{N}_2\text{H}_4$ (hydrazine) [11], cis-$\text{N}_2\text{H}_2$ (diazene), and $\text{F}_2\text{O}_2$ (dioxygen difluoride). LAVA shows consensus with composite methods, such as G4 and W4 theory, suggesting the experimental measurements from the 1960s might need re-evaluation. [2, 59].

Feller *et. al.* proposed the overly optimistic determination of the vaporization enthalpy of $\text{N}_2\text{H}_4$ to cause the discrepancy between experiments and theories [11].

Supplementary Figure 6 | LAVA's lowest variational energies for studied atoms and molecules.

![](./images/1159463098931740672_20.jpg)

### Supplementary Note 4.4 Absolute energies for benzene
Table S5 provides the results plotted in the main text Fig. 2a. Network configurations are given in 4-tuples that describe network depth, total hidden channels, the number of attention heads, and the number of determinants in sequence.

Supplementary Table 5 | Scaling law results of Benzene. Network configurations are given in the format of (depth, width, the number of attention heads, the number of determinants).

<table>
  <thead>
    <tr>
      <th>Network configuration</th>
      <th>$N_p$</th>
      <th>$E$ (Ha)</th>
      <th>$\text{Var}[E_L]$ ($\text{Ha}^2$)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>(4,64,2,16)</td>
      <td>257 474</td>
      <td>$-232.2321(1)$</td>
      <td>0.3665(2)</td>
    </tr>
    <tr>
      <td>(4,96,2,24)</td>
      <td>549 026</td>
      <td>$-232.239\ 94(6)$</td>
      <td>0.1972(2)</td>
    </tr>
    <tr>
      <td>(4,128,4,32)</td>
      <td>949 122</td>
      <td>$-232.244\ 22(6)$</td>
      <td>0.1304(1)</td>
    </tr>
    <tr>
      <td>(4,256,4,32)</td>
      <td>2 879 618</td>
      <td>$-232.246\ 89(5)$</td>
      <td>0.070 33(6)</td>
    </tr>
    <tr>
      <td>(4,408,4,48)</td>
      <td>7 115 954</td>
      <td>$-232.248\ 77(3)$</td>
      <td>0.046 18(5)</td>
    </tr>
    <tr>
      <td>(4,512,8,64)</td>
      <td>11 329 794</td>
      <td>$-232.249\ 47(3)$</td>
      <td>0.032 62(3)</td>
    </tr>
    <tr>
      <td>(8,512,8,128)</td>
      <td>22 633 986</td>
      <td>$-232.250\ 25(2)$</td>
      <td>0.023 18(3)</td>
    </tr>
    <tr>
      <td>LAVA-SE</td>
      <td>\</td>
      <td>$-232.2510$</td>
      <td>0.0</td>
    </tr>
  </tbody>
</table>

### Supplementary Note 4.5 Absolute energies for molecules from W4-11 dataset
Table S6 lists the absolute energies of molecules in the main text Fig. 2b. We use $\text{TAE}_e$ values for W2.2 and W4 from W4-11 dataset [29]. The experiment-derived absolute energies are corrected by the non-electronic contributions from W4 theory, $\text{TAE}_0$ -$\text{TAE}_e$, to obtain the experimentally derived $\text{TAE}_e$ that is directly comparable to LAVA absolute energies. We also illustrate different types of scaling laws in Fig. S7 and variance-energy extrapolation in Fig. S8.


### Supplementary Table 6 | Absolute energies in Hartrees.

<table>
  <thead>
    <tr>
      <th>Molecule</th>
      <th>W2.2 Derived (Ha)</th>
      <th>W4 Derived (Ha)</th>
      <th>NNVMC⁽ᵃ⁾ (Ha)</th>
      <th>LAVA-SE (Ha)</th>
      <th>Expt. Derived (Ha)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>HF</td>
      <td>−100.4597</td>
      <td>−100.4597</td>
      <td>−100.4595</td>
      <td>−100.4597</td>
      <td>−100.4596</td>
    </tr>
    <tr>
      <td>N₂</td>
      <td>−109.5419</td>
      <td>−109.5425</td>
      <td>−109.5413</td>
      <td>−109.5424</td>
      <td>−109.5424</td>
    </tr>
    <tr>
      <td>O₂</td>
      <td>−150.3260</td>
      <td>−150.3270</td>
      <td>−150.3245</td>
      <td>−150.3272</td>
      <td>−150.3272</td>
    </tr>
    <tr>
      <td>C₂H₄</td>
      <td>−78.5889</td>
      <td>−78.5889</td>
      <td>−78.5872</td>
      <td>−78.5885</td>
      <td>−78.5888</td>
    </tr>
    <tr>
      <td>F₂</td>
      <td>−199.5287</td>
      <td>−199.5299</td>
      <td>−199.5274</td>
      <td>−199.5303</td>
      <td>−199.5300</td>
    </tr>
    <tr>
      <td>HN₃</td>
      <td>−164.7948</td>
      <td>−164.7963</td>
      <td>−164.7916</td>
      <td>−164.7961</td>
      <td>−164.7959</td>
    </tr>
    <tr>
      <td>O₃</td>
      <td>−225.4316</td>
      <td>−225.4367</td>
      <td>−255.4304</td>
      <td>−225.4368</td>
      <td>−225.4371</td>
    </tr>
  </tbody>
</table>

⁽ᵃ⁾ LapNet is used as the baseline.

---

### Supplementary Figure 7 | Power-law scaling trends for molecules from the W4-11 dataset.

![](./images/1159463098931740672_21.jpg)

---

### Supplementary Figure 8 | Variance-energy extrapolation for molecules from W4-11 dataset.

![](./images/1159463098931740672_22.jpg)

Supplementary Note 5. Polyene chains

Supplementary Figure 9 | Power-law scaling trends for polyene chains.

![](./images/1159463098931740672_23.jpg)

Supplementary Figure 10 | Variance-energy extrapolation for polyene chains.

![](./images/1159463098931740672_24.jpg)

For polyene chains, Fig. S9 illustrates scaling laws and Fig. S10 illustrates variance-energy extrapolation. The neural scaling law $E - E_0 = \alpha N_p^{-\beta}$ enables us to evaluate the threshold resources required to achieve a target energy accuracy, e.g., chemical accuracy. In practice, instead of directly inverting the error-parameters power-law relationship for evaluation, we combine variance-parameters power-law scaling $V = \alpha_v N_p^{-\beta_v}$ and extrapolation relationships, which are empirically better supported, to get a revised estimation:

$$
N_p^* = \left( \frac{\alpha_v}{V - \Delta V} \right)^{1/\beta_v}, \tag{2}
$$

$$
\Delta V = (E - E_{\text{SE}} + \Delta E)/k, \tag{3}
$$

where $N_p^*$ is the estimated number of parameters required for target accuracy $\Delta E$. Relying on the excellent accuracy of the extrapolation, here we use $E - E_{\text{SE}}$ to estimate the current error. To get a reasonable network setting with $N_p^*$ parameters, we modify the number of network hidden channels $N_C$ and determinants $N_{\text{dets}}$ while maintaining $2048N_{\text{dets}} = N_C^2$ as default. The GPU hours required to optimize this network can be deemed an approximation of threshold computational costs that avails a priori resource allocation for high-accuracy calculations. To alleviate the influence of multi-host communications, the calculations for time estimation in the main text Fig. 2d were performed on a single 8×A800 server.

Supplementary Note 6. Cyclobutadiene automerization barrier

In this section, we provide a better estimate of the cyclobutadiene automerization barrier. We found that the best estimates of different theoretical predictions reach consensus with each other and also exhibit excellent agreement with our improved estimate of the experimental barrier.

10

### Supplementary Note 6.1 Experimental barrier with large uncertainty

Whitman *et. al.* estimated a 1.6-10 kcal/mol automerization barrier based on the trapping reaction between cyclobutadiene and methyl (Z)-3-cyanoacrylate, whose reaction network was given in the Fig. 1 of Whitman and Carpenter [55]. They measured $\Delta H_{\text{automerization}}^{\ddagger} - \Delta H_{\text{trapping}}^{\ddagger} = 1.6$ kcal/mol. The lower bound of 1.6 kcal/mol was obtained by setting $\Delta H_{\text{trapping}}^{\ddagger}$ to zero. The upper limit 10 kcal/mol was estimated by assuming $\Delta H_{\text{trapping}}^{\ddagger}$ is less than $\Delta H^{\ddagger} = 8.3$ kcal/mol, which is measured from cyclopentadiene-benzoquinone Diels-Alder reaction in $\text{CCl}_4$ solution.

In order to obtain a better estimate of $\Delta H_{\text{trapping}}^{\ddagger}$, we first optimized the structures of reactant, product, and transition state at the B3LYP-D3BJ/aug-cc-pVTZ level. We then calculated the zero-point energy of these structures at the same level of theory. Then, we calculated single-point CCSD(T) energies using cc-pVTZ and cc-pVQZ basis sets and extrapolated the CCSD(T) energies to the complete basis limit, as described in Supplementary Note 6.2. The resulting $\Delta H_{\text{automerization}}^{\ddagger}$ is 9.9 kcal/mol, which is in good agreement with the estimated upper limit in Whitman and Carpenter [55].

### Supplementary Note 6.2 Complete basis set extrapolation

Therefore, we follow the two-point extrapolation scheme proposed in Halkier et al [19] for Dunning's correlation-consistent series of Gaussian basis sets. The extrapolated HF energy is written as

$$
E_{\infty}^{\mathrm{HF}}=E_{n}^{\mathrm{HF}}-\frac{E_{n}^{\mathrm{HF}}-E_{n+1}^{\mathrm{HF}}}{1-e^{-B}},
\tag{4}
$$

where $B$ is a constant number 1.637 and $n$ is the $\zeta$ cardinality for basis set.

The extrapolated correlation energy follow the formula [18]

$$
E_{\infty}^{\mathrm{corr}}=\frac{n^{3} E_{n}^{\mathrm{corr}}-m^{3} E_{m}^{\mathrm{corr}}}{n^{3}-m^{3}},
\tag{5}
$$

where $n$ and $m$ are the $\zeta$ cardinality for basis sets, usually $n=m+1$.

### Supplementary Note 6.3 Available experimental observables of cyclobutadiene

We further calculated total atomization energy, heat of formation, and ionization potential of cyclobutadiene, where experimental measurements are available. LAVA shows perfect agreement with experiments.

LAVA predicts total atomization energy of 820.46 kcal/mol, which is in good agreement with 820.38 and 820.72 kcal/mol at the CCSD(T) and CCSDT(Q)level. [1].

In addition, LAVA predicts an heat of formation $\Delta_{f} H_{0}^{\circ}(\mathrm{C}_{4} \mathrm{H}_{4})=104.7$ kcal/mol for $2 \mathrm{C}_{2} \mathrm{H}_{2} \rightarrow \mathrm{C}_{4} \mathrm{H}_{4}$, where the zero point energy correction 4.83 kcal.mol/mol at CCSD(T)/cc-pVTZ level is taken from Wu et al [56]. This is good agreement with CCSDT(Q)/CBS prediction of $104.2 \pm 1.0$ kcal/mol[56] and experimental values of $102.3 \pm 3.8$ kcal/mol.[10]

Finally, LAVA-SE predicts an ionization potential of 8.165 eV, which is in excellent agreement with the experimental measurement of 8.16±0.03 eV[30]. In contrast, the theoretical value from various CC-based composite methods reported by ATcT (8.023–8.078 eV)[47] lies outside the experimental uncertainty range.

Table S7 provides the LAVA results plotted in the main text Fig. 3a. Network configurations are given in 4-tuples that describe network depth, total hidden channels, the number of attention heads, and the number of determinants in sequence. Fig. S11 illustrates scaling laws and Fig. S12 shows the variance-energy extrapolation.

### Supplementary Table 7 | Absolute energies, first ionization potential, and automerization barrier of cyclobutadiene from LAVA. Network configurations are given in the format of (depth, width, the number of attention heads, the number of determinants).

<table>
<thead>
<tr>
<th>Network configuration</th>
<th>Rectangular (Ha)</th>
<th>Rectangular anion (Ha)</th>
<th>Square (Ha)</th>
<th>IP1 (eV)</th>
<th>Barrier (kcal/mol)</th>
</tr>
</thead>
<tbody>
<tr>
<td>(4,64,2,16)</td>
<td>−154.680 93</td>
<td>−154.380 83</td>
<td>−154.663 87</td>
<td>8.166</td>
<td>10.70</td>
</tr>
<tr>
<td>(4,96,2,16)</td>
<td>−154.682 52</td>
<td>−154.382 54</td>
<td>−154.665 85</td>
<td>8.163</td>
<td>10.46</td>
</tr>
<tr>
<td>(4,128,4,16)</td>
<td>−154.683 92</td>
<td>−154.383 82</td>
<td>−154.6671</td>
<td>8.166</td>
<td>10.56</td>
</tr>
<tr>
<td>(4,192,4,32)</td>
<td>−154.685 77</td>
<td>−154.385 69</td>
<td>−154.669 46</td>
<td>8.166</td>
<td>10.23</td>
</tr>
<tr>
<td>(4,256,4,32)</td>
<td>−154.686 06</td>
<td>−154.386 12</td>
<td>−154.669 53</td>
<td>8.162</td>
<td>10.37</td>
</tr>
<tr>
<td>(4,384,4,64)</td>
<td>−154.686 74</td>
<td>−154.386 59</td>
<td>−154.671 28</td>
<td>8.167</td>
<td>9.70</td>
</tr>
<tr>
<td>(4,512,8,128)</td>
<td>−154.687 03</td>
<td>−154.386 82</td>
<td>−154.671 92</td>
<td>8.169</td>
<td>9.48</td>
</tr>
<tr>
<td>(4,1024,16,256)</td>
<td>−154.687 34</td>
<td>\</td>
<td>−154.672 28</td>
<td>\</td>
<td>9.45</td>
</tr>
<tr>
<td>LAVA-SE</td>
<td>−154.687 487</td>
<td>−154.387 417</td>
<td>−154.672 434</td>
<td>8.165</td>
<td>9.44</td>
</tr>
</tbody>
</table>

Supplementary Figure 11 | Power-law scaling trends for cyclobutadiene. From left to right, the absolute energy of rectangular cyclobutadiene, the absolute energy of square cyclobutadiene, and the first ionization potential of rectangular cyclobutadiene.

![](./images/1159463098931740672_25.jpg)

Supplementary Figure 12 | Variance-energy extrapolation for cyclobutadiene. From left to right, the absolute energy of rectangular cyclobutadiene, the absolute energy of square cyclobutadiene, and the first ionization potential of rectangular cyclobutadiene.

![](./images/1159463098931740672_26.jpg)

Notably, the first ionization potential (IP1) remains accurate even with the smallest network (4,64,2,16), exhibiting only minor fluctuations as network size increases. In contrast, the automerization barrier shows initial fluctuations but decreases significantly when scaling from network size (4,256,4,32) to (4,384,4,64).

Supplementary Note 6.4 Comparison of cyclobutadiene automerization barrier from various theoretical methods

Traditional quantum chemistry methods based on second quantization suffer from inherent difficulty in describing the multireferential character of the transition state, while experimentalists can hardly capture the highly unstable transition states. Previous calculations, as listed in Table S8, have not achieved a consensus. The perfect agreement between LAVA, the best estimates of systematically improvable methods, and improved experiments suggests that LAVA can serve as the benchmark for studying transition states and reaction kinetics.

<table>
<caption>Supplementary Table 8 | Reaction barrier of cyclobutadiene in kcal/mol from references.</caption>
<tbody>
<tr>
<th>CC[41]</th>
<td>6-31+G(d)</td>
<td>aug-cc-pVDZ</td>
<td>aug-cc-pVTZ</td>
<td>aug-cc-pVQZ</td>
</tr>
<tr>
<th>CCSD</th>
<td>8.31</td>
<td>8.80</td>
<td>9.88</td>
<td>10.10</td>
</tr>
<tr>
<th>CC3</th>
<td>6.59</td>
<td>6.89</td>
<td>7.88</td>
<td>8.06</td>
</tr>
<tr>
<th>CCSDT</th>
<td>7.26</td>
<td>7.64</td>
<td>8.68</td>
<td>8.86</td>
</tr>
<tr>
<th>CC4</th>
<td>7.40</td>
<td>7.78</td>
<td>8.82</td>
<td>9.00</td>
</tr>
<tr>
<th>CCSDTQ</th>
<td>7.51</td>
<td>7.89</td>
<td>8.93</td>
<td>9.11</td>
</tr>
<tr>
<th>CC[40]</th>
<td></td>
<td>cc-pVDZ</td>
<td>cc-pVTZ</td>
<td></td>
</tr>
<tr>
<th>CCSD</th>
<td></td>
<td>21.0</td>
<td>23.2</td>
<td></td>
</tr>
<tr>
<th>CCSD(T)</th>
<td></td>
<td>15.8</td>
<td>18.3</td>
<td></td>
</tr>
<tr>
<th>CR-CCSD(T)</th>
<td></td>
<td>18.3</td>
<td>\</td>
<td></td>
</tr>
<tr>
<th>ΛCCSD(T)</th>
<td></td>
<td>16.8</td>
<td>19.2</td>
<td></td>
</tr>
<tr>
<th>MRPT[41]</th>
<td>6-31+G(d)</td>
<td>aug-cc-pVDZ</td>
<td>aug-cc-pVTZ</td>
<td>aug-cc-pVQZ</td>
</tr>
<tr>
<th>CASPT2(4,4)</th>
<td>6.56</td>
<td>6.87</td>
<td>7.77</td>
<td>7.93</td>
</tr>
<tr>
<th>SC-NEVPT2(4,4)</th>
<td>7.95</td>
<td>8.31</td>
<td>9.23</td>
<td>9.42</td>
</tr>
<tr>
<th>PC-NEVPT2(4,4)</th>
<td>7.95</td>
<td>8.33</td>
<td>9.24</td>
<td>9.41</td>
</tr>
<tr>
<th>CASPT2(12,12)</th>
<td>7.24</td>
<td>7.53</td>
<td>8.51</td>
<td>8.71</td>
</tr>
<tr>
<th>SC-NEVPT2(12,12)</th>
<td>7.10</td>
<td>7.32</td>
<td>8.29</td>
<td>8.51</td>
</tr>
<tr>
<th>SC-NEVPT2(12,12)</th>
<td>7.12</td>
<td>7.33</td>
<td>8.28</td>
<td>8.49</td>
</tr>
<tr>
<th>MRCC[40]</th>
<td></td>
<td>cc-pVDZ</td>
<td>cc-pVTZ</td>
<td></td>
</tr>
<tr>
<th>TCCSD</th>
<td></td>
<td>9.4</td>
<td>12.9</td>
<td></td>
</tr>
<tr>
<th>SUCCSD</th>
<td></td>
<td>7.0</td>
<td>8.7</td>
<td></td>
</tr>
<tr>
<th>BWUCCSD(a.c)</th>
<td></td>
<td>6.5</td>
<td>7.6</td>
<td></td>
</tr>
<tr>
<th>BWUCCSD(i.c)</th>
<td></td>
<td>6.2</td>
<td>7.4</td>
<td></td>
</tr>
<tr>
<th>MkCCSD</th>
<td></td>
<td>7.8</td>
<td>9.1</td>
<td></td>
</tr>
<tr>
<th>RMRCCSD</th>
<td></td>
<td>10.4</td>
<td>13.0</td>
<td></td>
</tr>
<tr>
<th>TCCSD(T)</th>
<td></td>
<td>4.6</td>
<td>7.0</td>
<td></td>
</tr>
<tr>
<th>SUCCSD(T)</th>
<td></td>
<td>4.8</td>
<td>5.9</td>
<td></td>
</tr>
<tr>
<th>BWUCCSD(T)(a.c)</th>
<td></td>
<td>6.1</td>
<td>7.0</td>
<td></td>
</tr>
<tr>
<th>BWUCCSD(T)(i.c)</th>
<td></td>
<td>5.7</td>
<td>6.8</td>
<td></td>
</tr>
<tr>
<th>MkCCSD(T)</th>
<td></td>
<td>7.8</td>
<td>8.9</td>
<td></td>
</tr>
<tr>
<th>RMRCCSD(T)</th>
<td></td>
<td>7.2</td>
<td>9.5</td>
<td></td>
</tr>
<tr>
<th>Select CI</th>
<td></td>
<td>cc-pVDZ</td>
<td>cc-pVTZ</td>
<td></td>
</tr>
<tr>
<th>iFCI [21]</th>
<td></td>
<td>7.55</td>
<td>8.43</td>
<td></td>
</tr>
<tr>
<th>FCI 4-point extrapolation [8]</th>
<td></td>
<td></td>
<td>9.21</td>
<td></td>
</tr>
<tr>
<th>NNQMC</th>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<th>PauliNet[22]</th>
<td></td>
<td>9.9 ± 0.6 (250 steps)</td>
<td>7.7 ± 0.6 (375 steps)</td>
<td></td>
</tr>
<tr>
<th>FermiNet-VMC[49]</th>
<td></td>
<td>10.3 ± 0.1 (2 × 10⁵ steps)</td>
<td></td>
<td></td>
</tr>
<tr>
<th>FermiNet-VMC[46]</th>
<td></td>
<td>9.22(1 × 10⁵ steps)</td>
<td>9.41 (5 × 10⁵ steps)</td>
<td></td>
</tr>
<tr>
<th>FermiNet-DMC[46]</th>
<td></td>
<td>9.73(1 × 10⁵ steps)</td>
<td>9.98 (5 × 10⁵ steps)</td>
<td></td>
</tr>
</tbody>
</table>


### Supplementary Note 7. New benchmark for $\mathbf{N_2}$ potential energy curve

The potential energy curve (PEC) of $\text{N}_2$ is widely studied by various theoretical methods. The most commonly used benchmarks are theoretical $\text{r}_{12}$-MR-ACPF of Gdanitz [13] and analytic PECs fitted from experimental spectroscopic data [36]. Le Roy et al [36] fitted the ground-state PEC based on vibrational levels up to $v$=19, covering bond lengths $r$ between 0.9 and 1.5 Å.[36] At the fully dissociation limit $r > 4$ Å, the behavior of the analytic fitting function is governed by the experimentally measured dissociation energy $D_e$ and Morse long-range (MLR) function. However, these analytic potential functions show large uncertainty within the nearly dissociation region $2$ Å $< r < 4$ Å as shown in the Fig. 2 of Le Roy et al [36]. At $r = 2.2$ Å, the discrepancy between $\text{MLR}_4(6,8)$ and $\text{EMO}_2(6)$ is $1210\ \text{cm}^{-1}$, namely 3.4 kcal/mol, as shown in the inset of our main text Fig. 3b. Within the gray shaded region, where experimental vibrational levels are available, LAVA perfectly aligns with $\text{MLR}_4(6,8)$. At the stretched bond length ($r = 1.5 - 3$ Å), the certainty of LAVA remains the same as the equilibrium bond length, suggesting the reliability of LAVA across the entire PEC. The previous theoretical SOTA $\text{r}_{12}$-MR-ACPF perfectly agree with LAVA but shift up by about 6 mHa due to the finite basis set limitation. Since LAVA is based on first quantization, it is not limited by a finite basis set as the second-quantized methods are. Therefore, LAVA might have advantages over second-quantized methods in chemical systems where the size of the finite basis set plays an important role, such as transition metal complexes, excited states[44], and positronic chemistry [4].

First, we fitted various EMO and MLR curves using the 1221 experimental data points from Le Roy et al [36] and software dPotFit [34]. Then, we calculated the vibrational energy levels of these fitted curves using software LEVEL [35]. Finally, we chose the fitted curve that agrees best with our LAVA prediction, especially within the nearly dissociation region. Therefore, we retain the high accuracy of the original $\text{MLR}_4(6,8)$ curve around the equilibrium region between 0.9 and 1.5 Å while improving the reliability at the nearly dissociation region between 1.8 and 3.0 Å.

### Supplementary Note 7.1 Solving effective radial Schrödinger equation

The vibrational $v$ and rotational $J$ energy levels can be obtained by solving the effective radial Schrödinger equation:

$$
\left\{ -\frac{\hbar^2}{2\mu} \frac{d^2}{dr^2} + V(r) + \frac{\hbar^2 J(J+1)}{2\mu r^2} \right\} \psi_{v,J}(r) = E_{v,J} \psi_{v,J}(r) \tag{6}
$$

where $V$ is the total effective adiabatic internuclear potential, $\mu$ is the reduced mass of two atoms forming $\text{N}_2$; the last term on the left-hand-side $\frac{\hbar^2 J(J+1)}{2\mu r^2}$ is called the nonadiabatic centrifugal term.

The reference isotopologue is $^{14,14}\text{N}_2$, labled by $\alpha = 1$. For the other isotopologues $^{14,15}\text{N}_2$ and $^{15,15}\text{N}_2$, Le Roy et al [36] used adiabatic correction term $\Delta V^\alpha$ and nonadiabatic correction term $g^\alpha$ for isotopologue $\alpha$.

$$
\left\{ -\frac{\hbar^2}{2\mu_\alpha} \frac{d^2}{dr^2} + \left[ V^{(1)}(r) + \Delta V^{(\alpha)}(r) \right] + \frac{\hbar^2 J(J+1)}{2\mu_\alpha r^2} \left[ 1 + g^{(\alpha)}(r) \right] \right\} \psi_{v,J}(r) = E_{v,J} \psi_{v,J}(r) \tag{7}
$$

### Supplementary Note 7.2 Fitting analytic potential function $V(r)$

Le Roy et al [36] used 1221 spectroscopic data points of $^{14,14}\text{N}_2$, $^{14,15}\text{N}_2$, and $^{15,15}\text{N}_2$ from Raman and electric quadrupole vibration-rotation experiments of $^{14,14}\text{N}_2$, $^{14,15}\text{N}_2$, and $^{15,15}\text{N}_2$. One can obtain the theoretical prediction of vibrational $v$ and rotational $J$ data by plugging the analytic potential function $V(r)$ into equations 6 and 7, and then comparing the experimental and theoretical results. The quality of the analytic potential function fit is defined by the dimensionless root mean square deviation $\overline{dd}$:

$$
\overline{dd} \equiv \left\{ \frac{1}{N} \sum_{i=1}^N \left[ \frac{y_{\text{calc}}(i) - y_{\text{obs}}(i)}{u(i)} \right]^2 \right\}^{1/2} \tag{8}
$$

where $N$ is the number of experimental data, $u(i)$ is the estimated experimental uncertainties given in Table I of Le Roy et al [36], $y_{\text{calc}}(i)$ and $y_{\text{obs}}(i)$ are the calculated and experimental values, respectively. $\overline{dd}$ value reflects the difference between prediction and experiments is $\overline{dd}$ times of the estimated experimental uncertainties. The smaller the $\overline{dd}$ value, the better the fit.

### Supplementary Note 7.3 Expanded Morse oscillator function $\boldsymbol{V_{\text{EMO}}(r)}$

One expression of the $V(r)$ term in eq 6 is "expanded Morse oscillator" (EMO) function:

$$
V_{\text{EMO}}(r) = D_e \left[ 1 - e^{-\phi(r)(r - r_e)} \right]^2 \tag{9}
$$

where $D_e$ is the dissociation energy, $r_e$ is the equilibrium distance, and $\phi(r)$ is a power series expansion,

$$
\phi(r) = \phi_{\text{EMO}}(r) = \sum_{i=0}^N \phi_i y_p(r)^i \tag{10}
$$

14

and

$$
y_{p}(r)=\frac{r^{p}-r_{e}^{p}}{r^{p}+r_{e}^{p}}
\tag{11}
$$

$\text{EMO}_2(6)$ is the upper bound of various fitted functions in Fig. 2 of [36] as well as Fig. 3b of this work. $\text{EMO}_2(6)$ uses $N=6$ in eq.10 and $p=2$ in eq.11. The coefficients $\phi_0$ to $\phi_6$ are listed in Table S9.

### Supplementary Note 7.4 Morse/long-range potential function $V_{\text{MLR}}(r)$

$V_{\text{EMO}}(r)$ decays exponentially at large $r$, while the realistic PEC decays in inverse power at the long range. To incorporate the correct asymptote behavior, Le Roy et al [36] proposed the Morse/long-range (MLR) potential form:

$$
V_{\mathrm{MLR}}(r)=D_{e}\left\{1-\left(\frac{r_{e}}{r}\right)^{n}\left[\frac{1+R_{\mathrm{m}, \mathrm{n}} / r^{m-n}}{1+R_{\mathrm{m}, \mathrm{n}} / r_{e}^{m-n}}\right] e^{-\phi(r) y_{p}(r)}\right\}^{2}
\tag{12}
$$

$$
\phi(r)=\phi_{\mathrm{MLR}}(r)=\left[1-y_{p}(r)\right] \sum_{i=0}^{N} \phi_{i} y_{p}(r)^{i}+y_{p}(r) \phi_{\infty}
\tag{13}
$$

$$
\phi_{\infty}=\ln \frac{2 D_{e}\left(r_{e}\right)^{n}}{C_{n}\left[1+R_{m, n} / r_{e}^{m-n}\right]}
\tag{14}
$$

MLR function in eq. 12 resembles the Morse function form in eq. 9. Unlike the EMO function, the MLR function is simplified to two long-range inverse-power terms $V_{\mathrm{MLR}}(r) \approx D_{e}-\frac{C_{6}}{r^{6}}-\frac{C_{8}}{r^{8}}$ when $r \rightarrow \infty$ when $n=6$ and $m=8$. Therefore, $C_{n}, R_{m, n}, D_{e}$, and $r_{e}$ determine the asymptotic behavior of MLR function, together with $\phi_{i}$ and $p$ values affect the shape of intermediate distances.

Le Roy et al [36] recommended $\text{MLR}_4(6,8)$ as the best fit, indicating $p=4$, $N_S=6$, and $N_L=8$ in the following equations:

$$
\phi_{\mathrm{EMO}}(r)=\sum_{i=0}^{N_{S}} \phi_{i} y_{p}(r)^{i} \text { for } r \leq r_{e}
\tag{15}
$$

$$
\phi_{\mathrm{EMO}}(r)=\sum_{i=0}^{N_{L}} \phi_{i} y_{p}(r)^{i} \text { for } r>r_{e}
\tag{16}
$$

The reasons for using mixed exponent polynomial orders $(N_{s} \neq N_{L})$ were discussed in detail in Le Roy et al [36]. In the later works of the Le Roy group, they used $N_{s}=N_{L}$ to avoid discontinuity at $r=r_{e}$. Following the notation in Le Roy et al [36], we label the models by $\text{MLR}_p(N)$ or $\text{EMO}_p(N)$ when $N_{s}=N_{L}$, and $\text{MLR}_p(N_{S}, N_{L})$ when $N_{s} \neq N_{L}$. $\text{MLR}_3(9)$ refers to an MLR potential with the same exponent polynomial of order $N_{s}=N_{L}=N=9$ together with the expansion variable $y_{3}(r)=\frac{r^{3}-r_{e}^{3}}{r^{3}+r_{e}^{3}}$. Small $p$ value leads to a gradual change of PEC around $r=r_{e}$ while a large $p$ value indicates a sharper change. Parameters to define $\text{MLR}_3(9)$ and $\text{MLR}_4(6,8)$ curves and the difference $\overline{d d}$ between the experimental and calculated vibrational levels are listed in Table S9.

#### Supplementary Table 9 | Parameters to define the $\text{MLR}_4(6,8)$, $\text{MLR}_3(9)$, and $\text{EMO}_2(6)$ curves for the $X^{1}\Sigma_{g}^{+}$ state of $\text{N}_2$.

<table>
  <thead>
    <tr>
      <th>Potential function</th>
      <th>$\text{MLR}_4(6,8)$</th>
      <th>$\text{MLR}_3(9)$</th>
      <th>$\text{EMO}_2(6)$</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>$D_e$/cm⁻¹</td>
      <td colspan="3">79845</td>
    </tr>
    <tr>
      <td>$r_e$/Å</td>
      <td colspan="3">1.097679</td>
    </tr>
    <tr>
      <td>$C_6$/(cm⁻¹·Å⁶)</td>
      <td colspan="2">$1.16×10^5$</td>
      <td>\</td>
    </tr>
    <tr>
      <td>$R_{8,6}$/Å²</td>
      <td colspan="2">5.5</td>
      <td>\</td>
    </tr>
    <tr>
      <td>$\phi_0$</td>
      <td>−2.344 145 47</td>
      <td>3.125 518</td>
      <td>2.689 598</td>
    </tr>
    <tr>
      <td>$\phi_1$</td>
      <td>−0.972 469</td>
      <td>−1.338 651</td>
      <td>0.332 343</td>
    </tr>
    <tr>
      <td>$\phi_2$</td>
      <td>−1.561 777</td>
      <td>−1.926 378</td>
      <td>0.665 061</td>
    </tr>
    <tr>
      <td>$\phi_3$</td>
      <td>−1.136</td>
      <td>−1.053 483</td>
      <td>0.729 573</td>
    </tr>
    <tr>
      <td>$\phi_4$</td>
      <td>−1.3963</td>
      <td>−1.088 594</td>
      <td>1.157 254</td>
    </tr>
    <tr>
      <td>$\phi_5$</td>
      <td>−0.819</td>
      <td>0.253 611</td>
      <td>2.824 968</td>
    </tr>
    <tr>
      <td>$\phi_6$</td>
      <td>−0.45</td>
      <td>0.767 715</td>
      <td>12.341 291</td>
    </tr>
    <tr>
      <td>$\phi_7$</td>
      <td>−3.36</td>
      <td>−1.929 323</td>
      <td>\</td>
    </tr>
    <tr>
      <td>$\phi_8$</td>
      <td>2.1</td>
      <td>1.583 792</td>
      <td>\</td>
    </tr>
    <tr>
      <td>$\phi_9$</td>
      <td>\</td>
      <td>15.210 659</td>
      <td>\</td>
    </tr>
    <tr>
      <td>$\overline{dd}$</td>
      <td>1.44</td>
      <td>1.42</td>
      <td>1.43</td>
    </tr>
  </tbody>
</table>
15

### Supplementary Note 7.5 Low-lying vibrational levels for $v$=0-19

$v$=0-19 are included in 1221 experimental data points when fitting analytic potential functions. In Table S10, we listed the vibrational levels $G_v - G_0$ and rotational constants $B$ of experiment, $\text{MLR}_4(6,8)$, and $\text{MLR}_3(9)$. The new benchmark $\text{MLR}_3(9)$ gives slightly smaller RMSD in vibrational levels and the small RMSD in rotational constants than the old benchmark $\text{MLR}_4(6,8)$, suggesting $\text{MLR}_3(9)$ is superior to $\text{MLR}_4(6,8)$ in reproducing experimental results.

### Supplementary Table 10 | Vibrational levels $G_v - G_0$ and rotational constants $B$ from experiments for the $X^1\Sigma_g^+$ state of $\text{N}_2$, and the errors of $\text{MLR}_4(6,8)$ and $\text{MLR}_3(9)$ curves compared to experiments[33].

<table>
  <thead>
    <tr>
      <th rowspan="2">Level</th>
      <th colspan="3">$G_v - G_0(\text{cm}^{-1})$</th>
      <th colspan="3">$B(\text{cm}^{-1})$</th>
    </tr>
    <tr>
      <th>Experiment</th>
      <th>$\text{MLR}_4(6,8)$</th>
      <th>$\text{MLR}_3(9)$</th>
      <th>Experiment</th>
      <th>$\text{MLR}_4(6,8)$</th>
      <th>$\text{MLR}_3(9)$</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>1.9896</td>
      <td>0.0000</td>
      <td>0.0000</td>
    </tr>
    <tr>
      <td>1</td>
      <td>2329.91</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>1.9722</td>
      <td>0.0000</td>
      <td>0.0000</td>
    </tr>
    <tr>
      <td>2</td>
      <td>4631.17</td>
      <td>0.01</td>
      <td>0.02</td>
      <td>1.9547</td>
      <td>0.0001</td>
      <td>0.0001</td>
    </tr>
    <tr>
      <td>3</td>
      <td>6903.72</td>
      <td>0.03</td>
      <td>0.04</td>
      <td>1.9372</td>
      <td>0.0001</td>
      <td>0.0001</td>
    </tr>
    <tr>
      <td>4</td>
      <td>9147.54</td>
      <td>0.05</td>
      <td>0.06</td>
      <td>1.9196</td>
      <td>0.0001</td>
      <td>0.0001</td>
    </tr>
    <tr>
      <td>5</td>
      <td>11362.59</td>
      <td>0.05</td>
      <td>0.07</td>
      <td>1.9020</td>
      <td>0.0002</td>
      <td>0.0002</td>
    </tr>
    <tr>
      <td>6</td>
      <td>13548.81</td>
      <td>0.05</td>
      <td>0.07</td>
      <td>1.8843</td>
      <td>0.0003</td>
      <td>0.0003</td>
    </tr>
    <tr>
      <td>7</td>
      <td>15706.18</td>
      <td>0.04</td>
      <td>0.06</td>
      <td>1.8665</td>
      <td>0.0003</td>
      <td>0.0003</td>
    </tr>
    <tr>
      <td>8</td>
      <td>17834.62</td>
      <td>0.03</td>
      <td>0.05</td>
      <td>1.8487</td>
      <td>0.0004</td>
      <td>0.0004</td>
    </tr>
    <tr>
      <td>9</td>
      <td>19934.09</td>
      <td>0.01</td>
      <td>0.04</td>
      <td>1.8307</td>
      <td>0.0005</td>
      <td>0.0005</td>
    </tr>
    <tr>
      <td>10</td>
      <td>22004.52</td>
      <td>0.00</td>
      <td>0.03</td>
      <td>1.8128</td>
      <td>0.0005</td>
      <td>0.0005</td>
    </tr>
    <tr>
      <td>11</td>
      <td>24045.86</td>
      <td>-0.01</td>
      <td>0.03</td>
      <td>1.7947</td>
      <td>0.0005</td>
      <td>0.0006</td>
    </tr>
    <tr>
      <td>12</td>
      <td>26058.03</td>
      <td>0.00</td>
      <td>0.05</td>
      <td>1.7766</td>
      <td>0.0006</td>
      <td>0.0006</td>
    </tr>
    <tr>
      <td>13</td>
      <td>28040.94</td>
      <td>0.03</td>
      <td>0.07</td>
      <td>1.7584</td>
      <td>0.0006</td>
      <td>0.0006</td>
    </tr>
    <tr>
      <td>14</td>
      <td>29994.52</td>
      <td>0.08</td>
      <td>0.10</td>
      <td>1.7402</td>
      <td>0.0005</td>
      <td>0.0006</td>
    </tr>
    <tr>
      <td>15</td>
      <td>31918.65</td>
      <td>0.13</td>
      <td>0.14</td>
      <td>1.7219</td>
      <td>0.0004</td>
      <td>0.0005</td>
    </tr>
    <tr>
      <td>16</td>
      <td>33813.23</td>
      <td>0.17</td>
      <td>0.17</td>
      <td>1.7035</td>
      <td>0.0003</td>
      <td>0.0004</td>
    </tr>
    <tr>
      <td>17</td>
      <td>35678.10</td>
      <td>0.17</td>
      <td>0.16</td>
      <td>1.6851</td>
      <td>-0.0002</td>
      <td>0.0002</td>
    </tr>
    <tr>
      <td>18</td>
      <td>37513.11</td>
      <td>0.08</td>
      <td>0.08</td>
      <td>1.6666</td>
      <td>-0.0005</td>
      <td>0.0000</td>
    </tr>
    <tr>
      <td>19</td>
      <td>39318.06</td>
      <td>-0.19</td>
      <td>-0.11</td>
      <td>1.6480</td>
      <td>-0.0010</td>
      <td>-0.0003</td>
    </tr>
    <tr>
      <td>RMSD</td>
      <td>0.00</td>
      <td>0.18</td>
      <td>0.08</td>
      <td>0.0000</td>
      <td>0.0004</td>
      <td>0.0004</td>
    </tr>
  </tbody>
</table>

---

### Supplementary Note 7.6 High-lying vibrational levels for $v$=20-61

At dissociation limit, $v_D \approx 60.8$ $\text{MLR}_4(6,8)$ $v_D \approx 59.3$ $\text{MLR}_3(9)$. These $v_D$ values suggest that $\text{MLR}_4(6,8)$ and $\text{MLR}_3(9)$ support 61 and 59 vibrational levels, respectively. Differences in low-lying levels are negligible (less than 0.1 cm-1 for $v$ =0 to 19), but significant for high-lying levels up to 304 cm-1 at $v$ =49 as shown in Fig. S13.

### Supplementary Figure 13 | The difference between $\text{MLR}_3(9)$ and $\text{MLR}_4(6,8)$ for all vibrational levels up to the dissociation limit.

![](./images/1159463098931740672_27.jpg)

### Supplementary Note 7.7 LAVA scaling laws across the PEC

We tested the scaling laws of LAVA across the PEC using four network configurations: (4,96,2,16), (4,128,4,16), (4,256,4,32), and (4,512,8,128). In Fig. S14, we plot the variance of LAVA against the number of network parameters. The variance consistently decreases to nearly $10^{-3}$ Ha² across all bond distances, indicating that LAVA maintains similar accuracy across different bond lengths. Fig. S15 presents power-law scaling of $E - E_{\text{SE}}$ against total GPU hours. To describe the nearly dissociation regime more accurately, we supplemented the dataset of bond lengths ranging from 2.034 to 2.825 Å with results from the (1024,16,256) network. For the PEC shown in the main text Fig. 3b, we adopted the LAVA results from the largest network employed for each specific bond length since the number of data points is not sufficient for reliable extrapolation. But still, in the main text Fig. 2c, we roughly evaluate efficiency scaling across the PEC based on power-law scaling trends between $E - E_{\text{SE}}$ and time costs since we only investigate a qualitative trend of scaling exponent instead of accurate quantitative results of efficiency scaling order.

### Supplementary Figure 14 | Power-law scaling trends of Variance vs. Number of parameters.

![](./images/1159463098931740672_28.jpg)

![](./images/1159463098931740672_29.jpg)

## Supplementary Note 8. $O_3$ reaction barrier

### Supplementary Note 8.1 Optimized geometries from various theoretical methods
As shown in Table S11, the geometries of open minimum (OM), ring minimum (RM), and transition state (TS) calculated at different levels of theory differ significantly from one another. Starting from XMS-CASPT2-optimized geometries by perturbing angles and bond lengths, we performed a rough scan of the $O_3$ potential energy surface using (4,256,4,16) LAVA network configuration. Among the methods tested, only LAVA perfectly reproduces the experimental OM geometry. XMS-CASPT2 shows much better agreement with LAVA than CASSCF does: CASSCF overestimates the bond lengths of OM, RM, and TS, as well as the bond angle of TS; XMS-CASPT2 overestimates the bond angle of OM and underestimates the bond angle of TS.

### Supplementary Note 8.2 Energy landscape based on different PESs
Different methods show good consistency in the relative energy of RM-OM but diverge significantly in the relative energy of TS-RM. We identified three sources of these discrepancies.
First, some studies searched for the transition state geometry under $C_{2v}$ symmetry[52], others used low $C_s$ symmetry[53], and still others imposed no spatial symmetry restrictions. Given that $^1A_1$ and $^1A_2$ PESs cross near the TS, studies enforcing $C_{2v}/C_s$ symmetry found the TS on $^1A_1$/$^1A'$ PES, whereas those without spatial symmetry constraints found the energetically lower cross point between $^1A_1$ and $^1A_2$ surfaces (CP1 in Table S11) as the TS.
Second, the quality of the potential energy surfaces (PESs)—particularly their curvature—is strongly dependent on the theoretical method. CASSCF PESs differ significantly from CASPT2 PESs, whereas CASPT2 PESs show good agreement with LAVA for the critical structures listed in Table S11. For CASSCF and MRCISD+Q, the structures of TS and CP1 are different by about 4 °, [6] while those from XMS-CASPT2 and MMVMC are nearly identical.
Third, even for the same spin state and geometry, significant discrepancies persist across different theoretical methods. In Table S12, variations of ~ 0.6 eV arise in the TS-OM relative energy among methods when using the CASSCF geometry and singlet state. Ghanem et al [14] calculated these energy gaps using CCSD(T), CCSDT, CCSDT(Q), CCSDTQ, CCSDTQ(P), , with results summarized in Table S12. The RM-OM energy converges at the CCSDT(Q) level, but the TS-RM energy continues oscillating strongly even at the CCSDTQ(P) level. In addition, enlarging the basis set from VDZ to VQZ increases the barrier height, degrading the CC results. These abnormal behaviors suggest that single-reference coupled cluster theory struggles to accurately describe the TS. Different multireference methods also show a large discrepancy in predicting the TS - RM barrier, as shown in the main text Fig. 4b.
In short, the example of ozone demonstrates LAVA's capability to find the ground state of molecules with complex electronic structures. It is a black-box and systematically improvable. It doesn't require users' chemical intuition to choose active space, nor need any presumption on the ground state characters (such as singlet or triplet, open-shell singlet or closed-shell singlet).


Supplementary Table 11 | Critical structures optimized at different levels of theory.

<table>
<thead>
<tr>
<th rowspan="2">Theory</th>
<th colspan="2">OM</th>
</tr>
<tr>
<th>$R_{OO}$</th>
<th>$\angle OOO$</th>
</tr>
</thead>
<tbody>
<tr>
<td>CASSCF [52]</td>
<td>1.292</td>
<td>116.5</td>
</tr>
<tr>
<td>B3LYP[6]</td>
<td>1.256</td>
<td>118.2</td>
</tr>
<tr>
<td>XMS-CASPT2[53]ª</td>
<td>1.268</td>
<td>119.4</td>
</tr>
<tr>
<td>LAVA ᵇ</td>
<td>1.278</td>
<td>116.8</td>
</tr>
<tr>
<td>Experiment[23]</td>
<td>1.278</td>
<td>116.8</td>
</tr>
<tr>
<th rowspan="2">Theory</th>
<th colspan="2">RM</th>
</tr>
<tr>
<th>$R_{OO}$</th>
<th>$\angle OOO$</th>
</tr>
<tr>
<td>CASSCF [52]</td>
<td>1.466</td>
<td>60.0</td>
</tr>
<tr>
<td>B3LYP[6]</td>
<td>1.432</td>
<td>60.0</td>
</tr>
<tr>
<td>XMS-CASPT2[53]ª</td>
<td>1.425</td>
<td>60.0</td>
</tr>
<tr>
<td>LAVA ᵇ</td>
<td>1.426</td>
<td>59.9</td>
</tr>
<tr>
<th rowspan="2">Theory</th>
<th colspan="2">TS</th>
</tr>
<tr>
<th>$R_{OO}$</th>
<th>$\angle OOO$</th>
</tr>
<tr>
<td>CASSCF [52]</td>
<td>1.424</td>
<td>84.1</td>
</tr>
<tr>
<td>B3LYP[6]</td>
<td>1.381</td>
<td>77.9</td>
</tr>
<tr>
<td>XMS-CASPT2[53]ª</td>
<td>1.390</td>
<td>81.0</td>
</tr>
<tr>
<td>LAVA ᵇ</td>
<td>1.390</td>
<td>84.0</td>
</tr>
<tr>
<th rowspan="2">Theory</th>
<th colspan="2">Cross pointᶜ</th>
</tr>
<tr>
<th>$R_{OO}$</th>
<th>$\angle OOO$</th>
</tr>
<tr>
<td>CASSCF(18,12)/aug-cc-pVTZ [6]</td>
<td>1.416</td>
<td>80.3</td>
</tr>
<tr>
<td>MRCISD+Q(18,12)/aug-cc-pVTZ[6]</td>
<td>1.416</td>
<td>79.7</td>
</tr>
<tr>
<td>XMS-CASPT2[53]</td>
<td>1.391</td>
<td>80.9</td>
</tr>
<tr>
<td>LAVAᵇ</td>
<td>1.394</td>
<td>80.9</td>
</tr>
</tbody>
</table>

ª XMS-CASPT2 energies are corrected by CCSDT(Q) energies by dynamical scaled external correlation (DSEC) at critical structures.[53]
ᵇ We performed a rough scan of the PES using (4,256,4,16) LAVA network configuration.
ᶜ Cross point between $^1A_1$ and $^1A_2$ surfaces that on the RM side. Denoted as CP1 in Chen and Hu [6].


Supplementary Table 12 | Geometry effect to relative energies for $^1A'$ state. Relative energies of TS with respect to OM, RM with respect to OM,
and TS with respect to RM. Energies are in eV.

<table>
  <thead>
    <tr>
      <th>Theory</th>
      <th>TS-OM</th>
      <th>RM-OM</th>
      <th>TS-RM</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Single-point energy</td>
      <td colspan="3">CASSCF geometry[52]</td>
    </tr>
    <tr>
      <td>CCSD(T)/VDZ [14]</td>
      <td>2.55</td>
      <td>1.38</td>
      <td>1.18</td>
    </tr>
    <tr>
      <td>CCSDT/VDZ [14]</td>
      <td>2.49</td>
      <td>1.39</td>
      <td>1.09</td>
    </tr>
    <tr>
      <td>CCSDT(Q)/VDZ [14]</td>
      <td>2.27</td>
      <td>1.46</td>
      <td>0.80</td>
    </tr>
    <tr>
      <td>CCSDTQ/VDZ [14]</td>
      <td>2.34</td>
      <td>1.44</td>
      <td>0.90</td>
    </tr>
    <tr>
      <td>CCSDTQ(P)/VDZ [14]</td>
      <td>2.29</td>
      <td>1.45</td>
      <td>0.84</td>
    </tr>
    <tr>
      <td>CCSD(T)/VTZ [14]</td>
      <td>2.66</td>
      <td>1.23</td>
      <td>1.43</td>
    </tr>
    <tr>
      <td>CCSDT/VTZ [14]</td>
      <td>2.60</td>
      <td>1.25</td>
      <td>1.36</td>
    </tr>
    <tr>
      <td>CCSDT(Q)/VTZ [14]</td>
      <td>2.35</td>
      <td>1.32</td>
      <td>1.02</td>
    </tr>
    <tr>
      <td>CCSD(T)/VQZ [14]</td>
      <td>2.72</td>
      <td>1.27</td>
      <td>1.45</td>
    </tr>
    <tr>
      <td>CCSDT/VQZ [14]</td>
      <td>2.67</td>
      <td>1.29</td>
      <td>1.38</td>
    </tr>
    <tr>
      <td>CCSDT(Q)/VQZ [14]</td>
      <td>2.40</td>
      <td>1.37</td>
      <td>1.03</td>
    </tr>
    <tr>
      <td>CASSCF(18,12)/VQZ[52]</td>
      <td>2.32</td>
      <td>1.33</td>
      <td>0.99</td>
    </tr>
    <tr>
      <td>SHCI(18,90)/VTZ [7]</td>
      <td>2.41</td>
      <td>1.30</td>
      <td>1.11</td>
    </tr>
    <tr>
      <td>FCIQMC(18,39)-Tailored Coupled Cluster/VTZ [54]</td>
      <td>2.43</td>
      <td>1.29</td>
      <td>1.14</td>
    </tr>
    <tr>
      <td>Adaptive shift FCIQMC [54]/VQZ</td>
      <td>2.44</td>
      <td>1.36</td>
      <td>1.08</td>
    </tr>
    <tr>
      <td>CASSCF(18,12)/VQZ</td>
      <td>2.37</td>
      <td>1.32</td>
      <td>1.05</td>
    </tr>
    <tr>
      <td>NEVPT2(18,12)/VQZ</td>
      <td>2.47</td>
      <td>1.27</td>
      <td>1.20</td>
    </tr>
    <tr>
      <td>Single-point energy</td>
      <td colspan="3">XMS-CASPT2 geometry[53]</td>
    </tr>
    <tr>
      <td>XMS-CASPT2 [53] a</td>
      <td>2.42</td>
      <td>1.19</td>
      <td>1.23</td>
    </tr>
    <tr>
      <td>CASSCF(18,12)/VQZ</td>
      <td>2.18</td>
      <td>1.35</td>
      <td>0.83</td>
    </tr>
    <tr>
      <td>NEVPT2(18,12)/VQZ</td>
      <td>2.22</td>
      <td>1.24</td>
      <td>0.98</td>
    </tr>
    <tr>
      <td>LAVAb</td>
      <td>2.27</td>
      <td>1.36</td>
      <td>0.91</td>
    </tr>
    <tr>
      <td>Single-point energy</td>
      <td colspan="3">LAVA geometry</td>
    </tr>
    <tr>
      <td>CASSCF(18,12)/VQZ</td>
      <td>2.36</td>
      <td>1.37</td>
      <td>0.99</td>
    </tr>
    <tr>
      <td>NEVPT2(18,12)/VQZ</td>
      <td>2.40</td>
      <td>1.26</td>
      <td>1.14</td>
    </tr>
    <tr>
      <td>LAVA-SE</td>
      <td>2.47</td>
      <td>1.37</td>
      <td>1.10</td>
    </tr>
  </tbody>
</table>

$^{a}$ XMS-CASPT2 energies are corrected by CCSDT(Q) energies by dynamical scaled external correlation (DSEC) at critical structures.[53]
$^{b}$ LAVA results from (4,512,8,64) network configuration.

Supplementary Table 13 | Geometry effect on relative energies for triplet. Relative energies of TS with respect to OM, RM with respect to OM, and TS with respect to RM. Energies are in eV.

<table>
  <thead>
    <tr>
      <th>Theory</th>
      <th>TS-OM</th>
      <th>RM-OM</th>
      <th>TS-RM</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Single-point energy</td>
      <td colspan="3">CASSCF geometry[52]</td>
    </tr>
    <tr>
      <td>CASSCF(18,12)/VQZ</td>
      <td>1.90</td>
      <td>1.36</td>
      <td>0.54</td>
    </tr>
    <tr>
      <td>NEVPT2(18,12)/VQZ</td>
      <td>1.77</td>
      <td>1.29</td>
      <td>0.48</td>
    </tr>
    <tr>
      <td>LAVAª</td>
      <td>1.82</td>
      <td>1.36</td>
      <td>0.46</td>
    </tr>
    <tr>
      <td>Single-point energy</td>
      <td colspan="3">XMS-CASPT2 geometry[53]</td>
    </tr>
    <tr>
      <td>CASSCF(18,12)/VQZ</td>
      <td>2.09</td>
      <td>1.38</td>
      <td>0.83</td>
    </tr>
    <tr>
      <td>NEVPT2(18,12)/VQZ</td>
      <td>1.87</td>
      <td>1.26</td>
      <td>0.98</td>
    </tr>
    <tr>
      <td>LAVAª</td>
      <td>1.93</td>
      <td>1.35</td>
      <td>0.58</td>
    </tr>
    <tr>
      <td>Single-point energy</td>
      <td colspan="3">LAVA geometry</td>
    </tr>
    <tr>
      <td>CASSCF(18,12)/VQZ</td>
      <td>2.50</td>
      <td>1.40</td>
      <td>1.10</td>
    </tr>
    <tr>
      <td>NEVPT2(18,12)/VQZ</td>
      <td>2.22</td>
      <td>1.27</td>
      <td>0.95</td>
    </tr>
    <tr>
      <td>LAVA-SE</td>
      <td>2.08</td>
      <td>1.36</td>
      <td>0.72</td>
    </tr>
  </tbody>
</table>

ª LAVA results from (4,512,8,64) network configuration.

### Supplementary Note 8.3 Half-life estimation
In classical mechanics, chemical reactions can only occur at energies exceeding the reaction barrier. Classical reaction rates can be estimated using the Arrhenius equation. Currently, calculating vibrational frequencies with LAVA remains computationally prohibitive. Thus, we adopted the thermochemistry correction based on the geometries and vibrational frequencies (summarized in Table S14) at XMS-CASPT2 level by Varga et al [53], given that XMS-CASPT2 shows good agreement with LAVA for critical structures at Table S11. As for electronic energies, we used the LAVA-SE energies based on LAVA-optimized geometries, as listed in Table S14. Half-lives are calculated from the rate constants assuming first-order reactions. Rate constants and half lives from classical mechanics are provided in Table S15, labeled as TST (Conventional transition state theory).

Supplementary Table 14 | Parameters to calculate half-life.

<table>
  <thead>
    <tr>
      <th>Energy component</th>
      <th>OM</th>
      <th>TS</th>
      <th>RM</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Vibrational frequencies (cm⁻¹)[53]</td>
      <td>1130,756,730</td>
      <td>929,590,1005i</td>
      <td>1259,1259,1121</td>
    </tr>
    <tr>
      <td>LAVA-SE electronic energy (Ha)</td>
      <td>-225.4368</td>
      <td>-225.3459</td>
      <td>-225.3864</td>
    </tr>
  </tbody>
</table>

### Supplementary Note 8.4 Oxygen tunneling
In quantum mechanics, however, chemical reactions can occur at energies below the reaction barrier via quantum-mechanical tunneling (QMT). QMT results in reaction rates significantly faster than predicted by Arrhenius behavior and is characterized by unusually large kinetic isotope effects (KIEs). Tunneling effects are well-known and particularly pronounced in reactions involving hydrogen or proton transfer, as well as those with high barriers. Additionally, several experiments have observed pronounced heavy-atom tunneling in ring-opening reactions. For example, Datta et al [9] theoretically predicted rapid carbon tunneling in the ring opening of cyclopropylcarbinyl radical, which was later confirmed by experiments [15]. Using canonical variational transition-state theory (CVT) with the small-curvature tunneling (SCT) approximation, the theoretical predictions from Gonzalez-James et al [15] achieved excellent agreement with experimental results. More recently, Zhou et al [57] experimentally observed oxygen tunneling in both the oxygen-oxygen bond breaking reaction of cyclic beryllium peroxide to form linear dioxide and ring-closure reactions of beryllium ozonide complexes. The latter reaction [58] bear strong similarities to the ring-opening of cyclic ozone, and Zhou et al [58] demonstrated that QMT dominates the oxygen-oxygen bond breaking in beryllium peroxide.

Chen and Hu [6] quantified QMT of the ring-opening reaction of cyclic ozone using canonical variational theory (CVT). They employed two approaches to evaluate the microcanonical optimized multidimensional tunneling ($\mu$OMT) correction: one at continuous energy levels (the conventional method) and another at quantized reactant states (the QRST method). To isolate the QMT effect, We took the difference between their CVT/$\mu$OMT-QRST and CVT results in Table 3 of ref.[6] as the QMT effect, and multiplied it onto our TST results as LAVA's predictions of QMT results. Rate constants and half-lives from QMT are provided in Table S15, labeled as TST (transition state theory).


Supplementary Table 15 | Rate constants and half-life derived from LAVA-SE results.

<table>
  <thead>
    <tr>
      <th rowspan="2">$T$(K)</th>
      <th colspan="2">Rate constants ($\text{s}^{-1}$)</th>
      <th colspan="2">Half-life (s)</th>
    </tr>
    <tr>
      <th>TST</th>
      <th>CVT/$\mu$OMT-QRST</th>
      <th>TST</th>
      <th>CVT/$\mu$OMT-QRST</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>100</td>
      <td>$5.6 \times 10^{-36}$</td>
      <td>$1.2 \times 10^{-7}$</td>
      <td>$1.2 \times 10^{35}$</td>
      <td>$5.6 \times 10^{6}$</td>
    </tr>
    <tr>
      <td>200</td>
      <td>$3.3 \times 10^{-11}$</td>
      <td>$5.3 \times 10^{-4}$</td>
      <td>$2.1 \times 10^{10}$</td>
      <td>$1.3 \times 10^{3}$</td>
    </tr>
    <tr>
      <td>300</td>
      <td>$7.3 \times 10^{-3}$</td>
      <td>$1.3 \times 10^{0}$</td>
      <td>$9.5 \times 10^{1}$</td>
      <td>$5.5 \times 10^{-1}$</td>
    </tr>
  </tbody>
</table>

Supplementary Note 8.5 LAVA scaling laws for ozone

Fig. S16 gives scaling laws of the variance of local energy with respect to the number of parameters for different ozone geometries, while Fig. S17 shows the variance-energy extrapolation.

Supplementary Figure 16 | Power-law scaling trends for ozone.

![](./images/1159463098931740672_30.jpg)

Supplementary Figure 17 | Variance-energy extrapolation for ozone.

![](./images/1159463098931740672_31.jpg)

Supplementary Note 8.6 Improve spin symmetry and spatial symmetry of wavefunctions by scaling up network size

As illustrated by the XMS-CASPT2 PESs in Fig. 4c, the lowest-energy singlet state switches from $1^1\mathrm{A}'$ to $1^1\mathrm{A}''$ near the TS, and the state crossing point almost overlaps with the TS (Table S11). Additionally, the conical intersection between $1^1\mathrm{A}'$ and $2^1\mathrm{A}'$ states also lies closely to the TS. With the (4,256,4,16) network size, we observed state contamination between $1^1\mathrm{A}'$ and $1^1\mathrm{A}''$, indicated by the $\sigma_h = -0.62$ in Table S16. Despite the complex electronic structure of the TS, LAVA converges straightforwardly to the correct spatial symmetry with $\sigma_h = -1.00$ as the model size increases to (4,512,8,128).

A similar trend applies to spin symmetry. The CASSCF TS lies near the crossing point between $1^1\mathrm{A}'$ and $1^3\mathrm{A}''$ states. A singlet state should have an expectation value of the total angular momentum operator $\langle \hat{S}^2 \rangle$ that equals 0, while a triplet should have a value of 2. The (4,256,4,16) network gives an $\langle \hat{S}^2 \rangle$ value of 1.30, suggesting severe spin contamination in the LAVA wavefunction (Table S16). Scaling up the model to (4,512,8,128) —without imposing symmetry constraints or a penalty loss term[39]—ultimately yields a nearly pure triplet state with $\langle \hat{S}^2 \rangle$ value of 1.85.

Supplementary Table 16 | Expectation values of spatial and spin symmetries as the network scales up.

<table>
  <thead>
    <tr>
      <th>Network
configuration</th>
      <th colspan="2">Spatial symmetry at XMS-CASPT2 TS</th>
      <th colspan="2">Spin symmetry at CASSCF TS</th>
    </tr>
    <tr>
      <th></th>
      <th>$\sigma_h$</th>
      <th>Energy (Ha)</th>
      <th>$\langle\hat{S}^2\rangle$</th>
      <th>Energy (Ha)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>(4,256,4,16)</td>
      <td>$-0.62$</td>
      <td>$-225.3523$</td>
      <td>$1.30$</td>
      <td>$-225.3664$</td>
    </tr>
    <tr>
      <td>(4,512,8,128)</td>
      <td>$-1.00$</td>
      <td>$-225.3572$</td>
      <td>$1.85$</td>
      <td>$-225.3725$</td>
    </tr>
  </tbody>
</table>

Supplementary Note 9. Dipole moments and TAE for multireference molecules

Supplementary Note 9.1 Multireference diagnostics

We use coupled cluster $\mathcal{T}1$[37], $D1$[27], and $\% \text{TAE}_{e}[(\text{T})]$ diagnostics [28] to quantify the multireferential character of tested molecules. Lee and Taylor [37] used the criteria of $\mathcal{T}1 > 0.02$ and Janssen and Nielsen [27] used $D1 > 0.05$ to indicate non-negligible multireferential characters.

Karton et al [28] quantified the multireferential character using $\% \text{TAE}_{e}[(\text{T})]$:

$$
\% \text{TAE}_{e}[(\text{T})] = 100 \times \frac{\text{TAE}_{e}[\text{CCSD}(\text{T})] - \text{TAE}_{e}[\text{CCSD}]}{\text{TAE}_{e}[\text{CCSD}(\text{T})]} \tag{17}
$$

A $\% \text{TAE}_{e}[(\text{T})]$ value below $2\%$ indicates systems are dominated by dynamical correlation; $2$–$5\%$ indicates mild nondynamical correlation; $5$–$10\%$indicates moderate nondynamical correlation; and values in excess of $10\%$ indicate severe nondynamical correlation. Multireference diagnostics values taken from Karton et al [29] are listed in Table S17.

Supplementary Table 17 | Multireference diagnostics for molecules in Fig. 5a.

<table>
  <thead>
    <tr>
      <th>Molecule</th>
      <th>$\mathcal{T}1$ diagnostic</th>
      <th>$D1$ diagnostic</th>
      <th>$\% \text{TAE}_{e}[(\text{T})]$</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>$\text{CH}_3\text{COOH}$</td>
      <td>$0.02$</td>
      <td>$0.05$</td>
      <td>$2.0$</td>
    </tr>
    <tr>
      <td>$\text{HN}_3$</td>
      <td>$0.02$</td>
      <td>$0.05$</td>
      <td>$5.6$</td>
    </tr>
    <tr>
      <td>$\text{NO}$</td>
      <td>$0.02$</td>
      <td>$0.05$</td>
      <td>$6.2$</td>
    </tr>
    <tr>
      <td>$\text{F}_2\text{O}_2$</td>
      <td>$0.03$</td>
      <td>$0.09$</td>
      <td>$16.9$</td>
    </tr>
    <tr>
      <td>$\text{O}_3$</td>
      <td>$0.03$</td>
      <td>$0.08$</td>
      <td>$17.4$</td>
    </tr>
  </tbody>
</table>

Supplementary Note 9.2 Dipole moment

Hait and Head-Gordon [17] recommended combining the SCF component at the aug-cc-pCVQZ level with correlated component—estimated via extrapolation from aug-cc-pCVQZ and aug-cc-pCVTZ basis sets—to obtain a practically useful estimate of $\mu$ when expensive aug-cc-pCV5Z calculations are not affordable. For $\text{HN}_3$ and $\text{O}_3$, we adopt the CCSD(T)/CBS results from Hait and Head-Gordon [17]. For molecules not included in their work, we use the largest available basis sets from the Basis Set Exchange website[45] as the CBS limit of HF calculations, namely cc-pV6Z, aug-cc-pV6Z, and aug-cc-pCV5Z. For CCSD and CCSD(T), we use VQ,5Z and VD,TZ basis set pairs, respectively, to estimate the CBS limit for the correlated component in Table S18.

Owing to the slow basis set convergence of post-HF methods, Hait and Head-Gordon [17] employed the two-point extrapolation scheme from Halkier et al [20], which reproduces accurate (approximately $0.2\%$ error) for small molecules—yielding results comparable to quintuple-zeta quality from triple- and quadruple-zeta calculations.

$$
\mu_{\infty}^{\text{corr}} = \frac{n^3 \mu_n^{\text{corr}} - m^3 \mu_m^{\text{corr}}}{n^3 - m^3}, \tag{18}
$$

where $n$ and $m$ is the $\zeta$ cardinality for basis set.

Dipole moments calculated by post-HF methods are highly sensitive to the choice of basis set. The inclusion of augmented functions (denoted as "aug-") is critical for obtaining reliable dipole moments with relatively small basis sets. However, the addition of diffuse functions rapidly renders coupled-cluster calculations intractable due to their high computational scaling. For $\text{F}_2\text{O}_2$ molecules, both the diffuse and high-angular-momentum basis functions are critical to obtain an accurate dipole moment comparable to experimental results. In Table S18, the CCSD/CBS dipole moment remains $0.04$ Debye from the experimental value. While CCSD(T)/CBS holds promise for reproducing the experimental results. However, its prohibitive $\mathcal{O}(N^7)$ computational scaling renders all-electron CCSD(T) calculations with the aug-cc-pVTZ and aug-cc-pCVTZ basis sets unfeasible.

In contrast, as shown in Fig. 5a, LAVA yields highly accurate dipole moments, highlighting its advantage of delivering FCI/CBS-quality results, benefiting from its first-quantized ansatz. Fig. S18 further demonstrates that the dipole moment results of $\text{F}_2\text{O}_2$ rapidly converge to the experimental range as the network scales up.

Supplementary Table 18 | Coupled cluster calculations of the dipole moment of F₂O₂, reported in Debyes.

<table>
  <thead>
    <tr>
      <th>Theory</th>
      <th>Hartree-Fockᵃ</th>
      <th>CCSDᵃ</th>
      <th>CCSD(T)ᵇ</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>cc-pVDZ</td>
      <td>1.37</td>
      <td>1.19</td>
      <td>1.20</td>
    </tr>
    <tr>
      <td>cc-pVTZ</td>
      <td>1.49</td>
      <td>1.29</td>
      <td>1.28</td>
    </tr>
    <tr>
      <td>cc-pVQZ</td>
      <td>1.51</td>
      <td>1.33</td>
      <td>OOMᶜ</td>
    </tr>
    <tr>
      <td>cc-pV5Z</td>
      <td>1.52</td>
      <td>1.36</td>
      <td>OOM</td>
    </tr>
    <tr>
      <td>cc-pV6Z</td>
      <td>1.52</td>
      <td>OOM</td>
      <td>OOM</td>
    </tr>
    <tr>
      <td>CBS limit</td>
      <td>1.52</td>
      <td>1.37</td>
      <td>1.30</td>
    </tr>
    <tr>
      <td>(3,4)</td>
      <td></td>
      <td>1.35</td>
      <td>N/A</td>
    </tr>
    <tr>
      <td>aug-cc-pVDZ</td>
      <td>1.52</td>
      <td>1.41</td>
      <td>1.40 (with ccecp) ᵈ</td>
    </tr>
    <tr>
      <td>aug-cc-pVTZ</td>
      <td>1.52</td>
      <td>1.36</td>
      <td>1.38 (with ccecp)</td>
    </tr>
    <tr>
      <td>aug-cc-pVQZ</td>
      <td>1.52</td>
      <td>1.36</td>
      <td>OOM</td>
    </tr>
    <tr>
      <td>aug-cc-pV5Z</td>
      <td>1.51</td>
      <td>1.36</td>
      <td>OOM</td>
    </tr>
    <tr>
      <td>aug-cc-pV6Z</td>
      <td>1.51</td>
      <td>OOM</td>
      <td>OOM</td>
    </tr>
    <tr>
      <td>CBS limit</td>
      <td>1.51</td>
      <td>1.36</td>
      <td>1.37</td>
    </tr>
    <tr>
      <td>aug-cc-pCVDZ</td>
      <td>1.52</td>
      <td>1.41</td>
      <td>1.44</td>
    </tr>
    <tr>
      <td>aug-cc-pCVTZ</td>
      <td>1.52</td>
      <td>1.36</td>
      <td>OOM</td>
    </tr>
    <tr>
      <td>aug-cc-pCVQZ</td>
      <td>1.52</td>
      <td>1.36</td>
      <td>OOM</td>
    </tr>
    <tr>
      <td>aug-cc-pCV5Z</td>
      <td>1.51</td>
      <td>1.36</td>
      <td>OOM</td>
    </tr>
    <tr>
      <td>CBS limit</td>
      <td>1.51</td>
      <td>1.36</td>
      <td>N/A</td>
    </tr>
    <tr>
      <td>LAVA</td>
      <td colspan="3">1.40 ± 0.01</td>
    </tr>
    <tr>
      <td>Experiment</td>
      <td colspan="2">1.44 ± 0.04</td>
      <td>[26]</td>
    </tr>
  </tbody>
</table>

ᵃ Calculations performed on ByteQC [16] with GPU-accelerated HF and CCSD modules. The GPU-accelerated CCSD(T) module is not available.
ᵇ Calculations performed on PySCF v2.9.0.[50]
ᶜ OOM = out of memory on Intel(R) Xeon(R) Platinum 8336C CPU @ 2.30GHz, 980 GB memory.
ᵈ All-electron calculations ran out of memory.

Supplementary Figure 18 | F₂O₂ dipole results of different networks.

![](./images/1159463098931740672_32.jpg)

References

[1] Bakowies D (2019) Estimating systematic error and uncertainty in ab initio thermochemistry. I. atomization ener- gies of hydrocarbons in the ATOMIC(hc) protocol. Journal of Chemical Theory and Computation 15(10):5230–5251. doi:10.1021/acs.jctc.9b00343, URL http://dx.doi.org/10.1021/acs.jctc.9b00343

[2] Bond D (2009) Computational methods in organic thermochemistry. 4. enthalpies and Gibbs energies of formation of the cis- and trans-diazenes. The Journal of Physical Chemistry A 113(4):719–725. doi:10.1021/jp807308u, URL http://dx.doi. org/10.1021/jp807308u

[3] Bradbury J, Frostig R, Hawkins P, et al (2018) JAX: composable transformations of Python+NumPy programs. URL http: //github.com/google/jax

[4] Cassella G, Foulkes WMC, Pfau D, et al (2024) Neural network variational monte carlo for positronic chemistry. Nature Com- munications 15(1). doi:10.1038/s41467-024-49290-1, URL http://dx.doi.org/10.1038/s41467-024-49290-1

[5] Chakravorty SJ, Gwaltney SR, Davidson ER, et al (1993) Ground-state correlation energies for atomic ions with 3 to 18 electrons. Physical Review A 47(5):3649–3670. doi:10.1103/physreva.47.3649, URL http://dx.doi.org/10.1103/physreva.47. 3649

[6] Chen JL, Hu WP (2011) Theoretical prediction on the thermal stability of cyclic ozone and strong oxygen tunneling. Jour- nal of the American Chemical Society 133(40):16045–16053. doi:10.1021/ja203428x, URL http://dx.doi.org/10.1021/ ja203428x

[7] Chien AD, Holmes AA, Otten M, et al (2018) Excited states of methylene, polyenes, and ozone from heat-bath configuration interaction. The Journal of Physical Chemistry A 122(10):2714–2722. doi:10.1021/acs.jpca.8b01554, URL http://dx.doi. org/10.1021/acs.jpca.8b01554

[8] Dang DK, Kammeraad JA, Zimmerman PM (2022) Advances in parallel heat bath configuration interaction. The Journal of Phys- ical Chemistry A 127(1):400–411. doi:10.1021/acs.jpca.2c07949, URL http://dx.doi.org/10.1021/acs.jpca.2c07949

[9] Datta A, Hrovat DA, Borden WT (2008) Calculations predict rapid tunneling by carbon from the vibrational ground state in the ring opening of cyclopropylcarbinyl radical at cryogenic temperatures. Journal of the American Chemical Society 130(21):6684–6685. doi:10.1021/ja801089p, URL http://dx.doi.org/10.1021/ja801089p

[10] Fattahi A, Lis L, Tian Z, et al (2006) The heat of formation of cyclobutadiene. Angewandte Chemie International Edition 45(30):4984–4988. doi:10.1002/anie.200600839, URL http://dx.doi.org/10.1002/anie.200600839

[11] Feller D, Bross DH, Ruscic B (2017) Enthalpy of formation of $N_2H_4$ (hydrazine) revisited. The Journal of Physical Chemistry A 121(32):6187–6198. doi:10.1021/acs.jpca.7b06017, URL http://dx.doi.org/10.1021/acs.jpca.7b06017

[12] Fu W, Ren W, Chen J (2024) Variance extrapolation method for neural-network variational monte carlo. Machine Learning: Science and Technology 5(1):015016. doi:10.1088/2632-2153/ad1f75, URL https://dx.doi.org/10.1088/2632-2153/ ad1f75

[13] Gdanitz RJ (1998) Accurately solving the electronic Schrödinger equation of atoms and molecules using explicitly correlated ($r_{12}$-)MR-CI: the ground state potential energy curve of $N_2$. Chemical Physics Letters 283(5–6):253–261. doi:10.1016/s0009-2614(97)01392-4, URL http://dx.doi.org/10.1016/S0009-2614(97)01392-4

[14] Ghanem K, Guther K, Alavi A (2020) The adaptive shift method in full configuration interaction quantum monte carlo: Devel- opment and applications. J Chem Phys 153(22):224115

[15] Gonzalez-James OM, Zhang X, Datta A, et al (2010) Experimental evidence for heavy-atom tunneling in the ring-opening of cyclopropylcarbinyl radical from intramolecular $^{12}C/^{13}C$ kinetic isotope effects. Journal of the American Chemical Society 132(36):12548–12549. doi:10.1021/ja1055593, URL http://dx.doi.org/10.1021/ja1055593

[16] Guo Z, Huang Z, Chen Q, et al (2025) ByteQC: GPU-accelerated quantum chemistry package for large-scale systems. WIREs Computational Molecular Science 15(3):e70034. doi:10.1002/wcms.70034, e70034 CMS-1169.R1

[17] Hait D, Head-Gordon M (2018) How accurate is density functional theory at predicting dipole moments? An assess- ment using a new database of 200 benchmark values. Journal of Chemical Theory and Computation 14(4):1969–1981. doi:10.1021/acs.jctc.7b01252, URL http://dx.doi.org/10.1021/acs.jctc.7b01252

[18] Halkier A, Helgaker T, Jørgensen P, et al (1998) Basis-set convergence in correlated calculations on Ne, $N_2$, and $H_2O$. Chemical Physics Letters 286(3-4):243–252. doi:10.1016/s0009-2614(98)00111-0

25

[19] Halkier A, Helgaker T, Jørgensen P, et al (1999) Basis-set convergence of the energy in molecular Hartree-Fock calculations. Chemical Physics Letters 302(5-6):437–446. doi:10.1016/s0009-2614(99)00179-7

[20] Halkier A, Klopper W, Helgaker T, et al (1999) Basis-set convergence of the molecular electric dipole moment. The Journal of Chemical Physics 111(10):4424–4430. doi:10.1063/1.480036, URL http://dx.doi.org/10.1063/1.480036

[21] Hatch J, Rask AE, Dang DK, et al (2025) Many-body basis set amelioration method for incremental full configuration interaction. The Journal of Physical Chemistry A 129(16):3743–3753. doi:10.1021/acs.jpca.5c01521, URL http://dx.doi.org/10.1021/acs.jpca.5c01521

[22] Hermann J, Schätzle Z, Noé F (2020) Deep-neural-network solution of the electronic Schrödinger equation. Nature Chemistry 12(10):891–897. doi:10.1038/s41557-020-0544-y, URL https://doi.org/10.1038/s41557-020-0544-y

[23] Herzberg G (1966) Molecular spectra and molecular structure. Vol. 3: Electronic spectra and electronic structure of polyatomic molecules. Van Nostrand

[24] Hu WJ, Becca F, Parola A, et al (2013) Direct evidence for a gapless $Z_2$ spin liquid by frustrating Néel antiferromagnetism. Phys Rev B 88:060402. doi:10.1103/PhysRevB.88.060402, URL https://link.aps.org/doi/10.1103/PhysRevB.88.060402

[25] Iqbal Y, Hu WJ, Thomale R, et al (2016) Spin liquid nature in the heisenberg $J_1-J_2$ triangular antiferromagnet. Phys Rev B 93:144411. doi:10.1103/PhysRevB.93.144411, URL https://link.aps.org/doi/10.1103/PhysRevB.93.144411

[26] Jackson RH (1962) 884. The microwave spectrum, structure, and dipole moment of dioxygen difluoride. Journal of the Chemical Society (Resumed) p 4585. doi:10.1039/jr9620004585, URL http://dx.doi.org/10.1039/JR9620004585

[27] Janssen CL, Nielsen IM (1998) New diagnostics for coupled-cluster and Møller–Plesset perturbation theory. Chemical Physics Letters 290(4-6):423–430. doi:10.1016/s0009-2614(98)00504-1, URL http://dx.doi.org/10.1016/S0009-2614(98)00504-1

[28] Karton A, Rabinovich E, Martin JML, et al (2006) W4 theory for computational thermochemistry: In pursuit of confident sub-kJ/mol predictions. The Journal of Chemical Physics 125(14). doi:10.1063/1.2348881, URL http://dx.doi.org/10.1063/1.2348881

[29] Karton A, Daon S, Martin JML (2011) W4-11: A high-confidence benchmark dataset for computational thermochemistry derived from first-principles W4 data. Chemical Physics Letters 510(4):165–178. doi:https://doi.org/10.1016/j.cplett.2011.05.007, URL https://www.sciencedirect.com/science/article/pii/S0009261411005616

[30] Kohn DW, Chen P (1993) Vibrational structure in the photoelectron spectrum of cyclobutadiene as a probe of structure. Journal of the American Chemical Society 115(7):2844–2848. doi:10.1021/ja00060a035, URL http://dx.doi.org/10.1021/ja00060a035

[31] Kwon Y, Ceperley DM, Martin RM (1993) Effects of three-body and backflow correlations in the two-dimensional electron gas. Phys Rev B 48:12037–12046. doi:10.1103/PhysRevB.48.12037, URL https://link.aps.org/doi/10.1103/PhysRevB.48.12037

[32] Kwon Y, Ceperley DM, Martin RM (1998) Effects of backflow correlation in the three-dimensional electron gas: Quantum monte carlo study. Phys Rev B 58:6800–6806. doi:10.1103/PhysRevB.58.6800, URL https://link.aps.org/doi/10.1103/PhysRevB.58.6800

[33] Laher RR, Gilmore FR (1991) Improved fits for the vibrational and rotational constants of many states of nitrogen and oxygen. Journal of Physical and Chemical Reference Data 20(4):685–712. doi:10.1063/1.555892, URL http://dx.doi.org/10.1063/1.555892

[34] Le Roy RJ (2017) dPotFit: A computer program to fit diatomic molecule spectral data to potential energy functions. Journal of Quantitative Spectroscopy and Radiative Transfer 186:179–196. doi:10.1016/j.jqsrt.2016.06.002, URL http://dx.doi.org/10.1016/j.jqsrt.2016.06.002

[35] Le Roy RJ (2017) LEVEL: A computer program for solving the radial Schrödinger equation for bound and quasibound levels. Journal of Quantitative Spectroscopy and Radiative Transfer 186:167–178. doi:10.1016/j.jqsrt.2016.05.028, URL http://dx.doi.org/10.1016/j.jqsrt.2016.05.028

[36] Le Roy RJ, Huang Y, Jary C (2006) An accurate analytic potential function for ground-state $N_2$ from a direct-potential-fit analysis of spectroscopic data. The Journal of Chemical Physics 125(16). doi:10.1063/1.2354502, URL http://dx.doi.org/10.1063/1.2354502

26

[37] Lee TJ, Taylor PR (2009) A diagnostic for determining the quality of single-reference electron correlation methods. International Journal of Quantum Chemistry 36(S23):199–207. doi:10.1002/qua.560360824, URL http://dx.doi.org/10.1002/qua.560360824

[38] Li R, Ye H, Jiang D, et al (2024) A computational framework for neural network-based variational Monte Carlo with Forward Laplacian. Nat Mach Intell 6(2):209–219. doi:10.1038/s42256-024-00794-x, URL https://www.nature.com/articles/s42256-024-00794-x, publisher: Nature Publishing Group

[39] Li Z, Lu Z, Li R, et al (2024) Spin-symmetry-enforced solution of the many-body Schrödinger equation with a deep neural network. Nature Computational Science 4(12):910–919. doi:10.1038/s43588-024-00730-4, URL https://doi.org/10.1038/s43588-024-00730-4

[40] Lyakh DI, Lotrich VF, Bartlett RJ (2011) The ‘tailored’ CCSD(T) description of the automerization of cyclobutadiene. Chemical Physics Letters 501(4–6):166–171. doi:10.1016/j.cplett.2010.11.058, URL http://dx.doi.org/10.1016/j.cplett.2010.11.058

[41] Monino E, Boggio-Pasqua M, Scemama A, et al (2022) Reference energies for cyclobutadiene: Automerization and excited states. The Journal of Physical Chemistry A 126(28):4664–4679. doi:10.1021/acs.jpca.2c02480, URL http://dx.doi.org/10.1021/acs.jpca.2c02480

[42] Moreno JR, Carleo G, Georges A, et al (2022) Fermionic wave functions from neural-network constrained hidden states. Proceedings of the National Academy of Sciences 119(32):e2122059119. doi:10.1073/pnas.2122059119, URL https://www.pnas.org/doi/abs/10.1073/pnas.2122059119, https://www.pnas.org/doi/pdf/10.1073/pnas.2122059119

[43] Pfau D, Spencer JS, Matthews AGDG, et al (2020) Ab initio solution of the many-electron Schrödinger equation with deep neural networks. Physical Review Research 2(3). doi:10.1103/physrevresearch.2.033429, URL http://dx.doi.org/10.1103/PhysRevResearch.2.033429

[44] Pfau D, Axelrod S, Sutterud H, et al (2024) Accurate computation of quantum excited states with neural networks. Science 385(6711). doi:10.1126/science.adn0137, URL http://dx.doi.org/10.1126/science.adn0137

[45] Pritchard BP, Altarawy D, Didier B, et al (2019) New basis set exchange: An open, up-to-date resource for the molecular sciences community. Journal of Chemical Information and Modeling 59(11):4814–4820. doi:10.1021/acs.jcim.9b00725, URL http://dx.doi.org/10.1021/acs.jcim.9b00725

[46] Ren W, Fu W, Wu X, et al (2023) Towards the ground state of molecules via diffusion monte carlo on neural networks. Nature Communications 14(1):1860. doi:10.1038/s41467-023-37609-3, URL https://doi.org/10.1038/s41467-023-37609-3

[47] Ruscic B, Bross DH (2024) Active thermochemical tables (ATcT) values based on ver. 1.202 of the thermochemical network, argonne national laboratory, lemont, illinois

[48] Seth P, Ríos PL, Needs RJ (2011) Quantum monte carlo study of the first-row atoms and ions. The Journal of Chemical Physics 134(8). doi:10.1063/1.3554625, URL http://dx.doi.org/10.1063/1.3554625

[49] Spencer JS, Pfau D, Botev A, et al (2020) Better, faster fermionic neural networks. doi:10.48550/ARXIV.2011.07125, URL https://arxiv.org/abs/2011.07125

[50] Sun Q, Zhang X, Banerjee S, et al (2020) Recent developments in the PySCF program package. The Journal of Chemical Physics 153(2). doi:10.1063/5.0006074, URL http://dx.doi.org/10.1063/5.0006074

[51] Taddei M, Ruggeri M, Moroni S, et al (2015) Iterative backflow renormalization procedure for many-body ground-state wave functions of strongly interacting normal Fermi liquids. Phys Rev B 91:115106. doi:10.1103/PhysRevB.91.115106, URL https://link.aps.org/doi/10.1103/PhysRevB.91.115106

[52] Theis D, Ivanic J, Windus TL, et al (2016) The transition from the open minimum to the ring minimum on the ground state and on the lowest excited state of like symmetry in ozone: A configuration interaction study. The Journal of Chemical Physics 144(10). doi:10.1063/1.4942019, URL http://dx.doi.org/10.1063/1.4942019

[53] Varga Z, Paukku Y, Truhlar DG (2017) Potential energy surfaces for $O + O_2$ collisions. The Journal of Chemical Physics 147(15). doi:10.1063/1.4997169, URL http://dx.doi.org/10.1063/1.4997169

[54] Vitale E, Alavi A, Kats D (2020) FCIQMC-tailored distinguishable cluster approach. Journal of Chemical Theory and Computation 16(9):5621–5634. doi:10.1021/acs.jctc.0c00470, URL http://dx.doi.org/10.1021/acs.jctc.0c00470

27

[55] Whitman DW, Carpenter BK (1982) Limits on the activation parameters for automerization of cyclobutadiene-1,2-d2. Jour- nal of the American Chemical Society 104(23):6473–6474. doi:10.1021/ja00387a065, URL http://dx.doi.org/10.1021/ ja00387a065

[56] Wu JIC, Mo Y, Evangelista FA, et al (2012) Is cyclobutadiene really highly destabilized by antiaromaticity? Chemical Com- munications 48(67):8437. doi:10.1039/c2cc33521b, URL http://dx.doi.org/10.1039/c2cc33521b

[57] Zhou Y, Fang W, Wang L, et al (2023) Quantum tunneling in peroxide O–O bond breaking reaction. Journal of the American Chemical Society 145(16):8817–8821. doi:10.1021/jacs.3c02750, URL http://dx.doi.org/10.1021/jacs.3c02750

[58] Zhou Y, Fan W, Tang J, et al (2024) Heavy-atom tunneling in ring-closure reactions of beryllium ozonide complexes. Journal of the American Chemical Society 146(39):26719–26725. doi:10.1021/jacs.4c06137, URL http://dx.doi.org/10.1021/ jacs.4c06137

[59] Çiftcioğlu GA, Trindle C (2013) Computational estimates of thermochemistry and p$K_a$ values of cyclopropenyl imine super- bases. International Journal of Quantum Chemistry 114(6):392–399. doi:10.1002/qua.24576, URL http://dx.doi.org/10. 1002/qua.24576
<br>