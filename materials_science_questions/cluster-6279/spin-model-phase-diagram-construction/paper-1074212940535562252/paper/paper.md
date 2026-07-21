
# Emergent topological re-entrant phase transition in a generalized quasiperiodic modulated Su-Schrieffer-Heeger model

Xiao-Ming Wang, \( ^{1,2} \)  Shan-Zhong Li, \( ^{1,3} \)  and Zhi Li \( ^{1,2,†} \) 

 \( ^{1} \) Key Laboratory of Atomic and Subatomic Structure and Quantum Control (Ministry of Education), Guangdong Basic Research Center of Excellence for Structure and Fundamental Interactions of Matter, School of Physics, South China Normal University, Guangzhou 510006, China  
 \( ^{2} \) Guangdong Provincial Key Laboratory of Quantum Engineering and Quantum Materials, Guangdong-Hong Kong Joint Laboratory of Quantum Matter, Frontier Research Institute for Physics, South China Normal University, Guangzhou 510006, China  
(Dated: December 12, 2024)

We study the topological properties of the one-dimensional generalized quasiperiodic modulated Su-Schrieffer-Heeger model. The results reveal that topological re-entrant phase transition emerges. Through the analysis of a real-space winding number, we divide the emergent topological re-entrant phase transitions into two types. The first is the re-entrant phase transition from the traditional topological insulator phase into the topological Anderson insulator phase, and the second is the re-entrant phenomenon from one topological Anderson insulator phase into another topological Anderson insulator phase. These two types of re-entrant phase transition correspond to bounded and unbounded cases of quasiperiodic modulation, respectively. Furthermore, we verify the above topological re-entrant phase transitions by analyzing the Lyapunov exponent and bulk gap. Since Su-Schrieffer-Heeger models have been realized in various artificial systems (such as cold atoms, optical waveguide arrays, ion traps, Rydberg atom arrays, etc.), the two types of topological re-entrant phase transition predicted in this paper are expected to be realized in the near future.

## I. INTRODUCTION

Topological insulators (TI), as a system with unique transport properties, constitute one of the most important research directions in condensed matter physics and quantum computation  \( [1-24] \) . Previous studies have shown that the non-trivial edge states in topological systems feature good robustness, which ensures that the edge current can still maintain its original state in the case of weak disorder or defects. However, when disorder becomes very strong, the topological system will undergo Anderson phase transition  \( [25] \) . In other words, in the case of strong disorder, the topological edge current will be destroyed to make the topological system a gapless Anderson insulator, where the corresponding bulk states show the characteristics of localized states. In addition, recent studies have revealed that moderate disorder can achieve a transition from a trivial phase to a non-trivial phase, and this topological system induced by disorder is called topological Anderson insulator (TAI)  \( [26-44] \) .

In recent years, TAIs and its related fields have been greatly developed, and a series of milestone achievements have been scored. Theoretically, in addition to the standard TAI, the following systems have also been predicted:  \( Z_{2} \)  topological Anderson insulators [45], Topological Anderson amorphous insulator [46], Higher-order Topological Anderson Insulators [47, 48], Topological inverse Anderson insulator [49], etc [50, 51]. Besides, with the increasing popularity of non-Hermitian research [52–58], the study on TAI has gradually extended to non-Hermitian systems [59–62]. Experimentally, TAI has been realized in a variety of artificial systems, including ultra-cold atoms [63–65], photonic/phononic system [66–68], superconducting system [69], and electric circuits [70], etc.

Re-entrant phase transition (REPT), on the other hand, refers to the process in which the system starts from a phase and returns to the same phase by monotonically manipulating a certain parameter  \( [71] \) . Recently, the REPT of localized phase has been discovered in Aubry-André model  \( [72, 73] \) . Moreover, topological REPT has also been reported recently  \( [74] \) . So far, although there are many researches on TI and TAI, few work has been done on topological REPT in TI and TAI  \( [75] \) . This paper is devoted to the study of REPT phenomena in TI and TAI system.

There are two main findings in this paper. First, the generalized quasiperiodic modulation can induce topological REPTs in one-dimensional Su-Schrieffer-Heeger (SSH) model. Second, the emerged REPTs can be divided into two classes. In concrete terms, when the bounded (unbounded) structure quasiperiodic modulation has been selected, REPTs of TI→TAI (TAI→TAI) will emerge [see Fig. 1].

The rest of this paper is organized as follows. In sec. II, we briefly introduce the one-dimensional SSH model with generalized quasiperiodic modulation. In sec. III, under the condition of the bounded case, we discuss the first type of REPT by computing winding number, energy gap and Lyapunov exponent. In sec. IV, we discuss the unbounded case. The main results of this paper are summarized in sec. V.
 

(a) Topological phase transition

![](./images/1074212940535562252_1.jpg)

(b) Topological re-entrant phase transition

![](./images/1074212940535562252_2.jpg)

FIG. 1: Schematic diagram of quasiperiodic induced traditional topological phase transitions and topological REPT.

## II. MODEL AND KEY QUANTITIES

Let's start at the generalized quasiperiodic modulated SSH model. The corresponding Hamiltonian reads

 \[ H=\sum_{n=1}^{N}\left(t_{1}^{\prime}a_{n}^{\dagger}b_{n}+t_{2}a_{n+1}^{\dagger}b_{n}+\mathrm{H.c.}\right), \quad (1) \] 

where  \( a_{n} \)  ( \( b_{n} \) ) is the annihilation operator for the sublattice A (B) on n-th primitive cell. N is the total number of primitive cells.  \( t_{1}^{\prime} \)  and  \( t_{2} \)  denote the intracell and the intercell hopping strength, respectively. Here, we consider applying a generalized quasiperiodic modulation on the intracell hopping term [76], i.e.,

 \[ t_{1}^{^{\prime}}=t_{1}+\frac{\lambda\cos(2\pi\alpha n+\theta)}{1-b\cos(2\pi\alpha\mathfrak{n}+\theta)}, \quad (2) \] 

where  \( t_{1} \)  is the intracell hopping strength,  \( \lambda \)  is the strength of quasiperiodic modulation, b is the structure factor, which is the key parameter to control the quasiperiodic modulation bounded  \( (b < 1) \)  or unbounded  \( (b \geq 1) \) .  \( \theta \)  is an additional phase shift, and  \( \alpha \)  is an irrational number. When  \( \lambda = 0 \) , the Hamiltonian Eq. (1) reduces to the standard SSH model [77]. The system represents a trivial (non-trivial) topology under the condition of  \( t_{1} < t_{2} \)  ( \( t_{1} > t_{2} \) ). Without loss of generality, we set  \( t_{2} = 1 \)  as the energy unit. We take  \( \alpha = (\sqrt{5} - 1)/2 \)  and  \( \theta = 0 \) . In the numerical calculation, we choose the system size  \( N = L/2 = 610 \)  with L being the total lattice number. Such size is large enough for self-averaging and one can safely ignore the finite size effect (see Appendix A for details).

In this paper, since we are concerned with topological properties, we mainly discuss three quantities related to topological properties.
The first one is the winding number, which can well reflect the system's topological properties. Since the generalized quasiperiodic modulation breaks the translational symmetry, generally speaking, one can use the real-space winding number as the indicator to characterize the topological properties of a quasiperiodic topological system [78], which can be defined as

 \[ \nu=\frac{1}{L^{\prime}}\mathrm{T r}^{^{\prime}}(\Gamma\mathrm{Q}[\mathrm{Q},\mathrm{X}]). \quad (3) \] 

where  \( \mathbf{Q}=\sum_{j=1}^{N}(|j\rangle\langle j|-|\tilde{j}\rangle\langle\tilde{j}|) \)  is the corresponding open-boundary matrix and  \( |\tilde{j}\rangle=\Gamma^{-1}|j\rangle \) . One can directly obtain the matrix Q by solving the eigenequations  \( H|j\rangle=E_{j}|j\rangle \) , where  \( E_{j} \)  and  \( |j\rangle \)  correspond to the eigenenergies and eigenstates, respectively.  \( \Gamma=I_{N}\otimes\sigma_{z} \)  denotes the chiral symmetry operator with the identity matrix  \( I_{N} \)  and the Pauli matrix  \( \sigma_{z} \) . The key operator

 \[ \mathbf{X}=\begin{pmatrix}{{{1}}}&{{{0}}}&{{{0}}} &{{{0}}}&{{{}}&{{{\cdots}}}&{{{0}}}&{{{0}}} \\{{{0}}}&{{{1}}}&{{{0}}}&{{{0}}} &{{{\cdots}}}&{{{0}}} \\{{{0}}}&{{{0}}}&{{{2}}}&{{{0}}} &{{{\cdots}}}&{{{0}}}&{{{0}}} \\{{{0}}}&{{{ 0}}}&{{{0}}}}&{{{2}}}&{{{0}}}&{{{\cdots}}}&{{{0}}} \\{{{\vdots}}}&{{{\vdots}}}&{{\vdots}}&{{{\vdots}}} \\{{{0}}}&{{{0}}}&{{{ 0}}}&{{{0}}}}&{{{\cdots}}}&{{{N}}}&{{{0}}} \\{{{0}}}&{{{0}}}&{{{ 0}}}&{{{  ^{\circ}}}}&{{{\cdots}}}&{{{0}}}&{{{ N}}}\end{pmatrix} \quad (4) \] 

is the coordinate operator. The symbol  \( Tr^{'} \)  means the trace over the middle interval of the full lattice with the length  \( L^{'} = L/2 = N \)  (see Appendix A for details). For example, under the condition of the primitive cells' number N = 6. Since a primitive cell contains two sublattices, the total number of sites is 12. The corresponding matrix in Eq. (4) is a  \( 12 \times 12 \)  matrix. Then,  \( Tr^{'} \)  represents the trace of a  \( 6 \times 6 \)  submatrix formed by selecting the middle region of the original matrix (the region of rows  \( 4 - 9 \times \)  column  \( 4 - \theta \) ).

The second one is the bulk energy gap under the condition PBCs, i.e.,

 \[ \ln(\Delta E)=\ln(E_{N+1}-E_{N}), \quad (5) \] 

which can well exhibit the phase transition critical points in REPT process. Concretely speaking, for topological phase transition, the bulk gap closing and reopening will occur, whereas for localized phase transition, the corresponding bulk gap will close and not reopen.

The third one is the key indicator of localization transition—the Lyapunov exponent. For the model of Eq. (1), the corresponding wave function of zero mode  \( \psi = \{\psi_{1,A}, \psi_{1,B}, \psi_{2,A}, \psi_{2,B}, \ldots, \psi_{N,A}, \psi_{N,B}\}^{T} \) , which can be solved by the Schrödinger equation  \( H\psi = 0 \) . One can obtain the eigenequations  \( t_{2}\psi_{n,B} + t_{1,n+1}^{\prime}\psi_{n+1,B} = 0 \)  and  \( t_{1,n}^{\prime}\psi_{n,A} + t_{2}\psi_{n+1,A} = 0 \) . Then, the corresponding probability distribution of the zero mode wave function
 

reads

 \[ \begin{aligned}&\psi_{n,A}=(-1)^{n}\prod_{l=1}^{n}\frac{t_{1,l}^{\prime}}{t_{2}}\psi_{1,A},\\&\psi_{n,B}=(-1)^{n}\prod_{l=1}^{n}\frac{t_{2}}{t_{1,l+1}^{\prime}}\psi_{1,B}.\\ \end{aligned} \quad (6) \] 

Then, one can obtain the Lyapunov exponent  \( \gamma \)  of the zero mode for  \( N \to \infty \) , which is the inverse of the localization length [78, 79], i.e.,

 \[ \gamma=\max\left\{\lim_{N\to\infty}\frac{1}{N}\ln\psi_{N,A},\lim_{N\to\infty}\frac{1}{N}\ln\psi_{N,B}\right\}. \quad (7) \] 

By set  \( \psi_{1,A} = \psi_{1,B} = 1 \) , and by performing a straightforward calculation, one can obtain

 \[ \begin{aligned}\gamma&=\lim_{N\to\infty}\frac{1}{N}\ln\psi_{N,A}=\lim_{N\to\infty}\frac{1}{N}\ln\psi_{N,B}\\&=\left|\lim_{N\to\infty}\frac{1}{N}\sum_{l=1}^{N}\left(\ln|t_{2}|-\ln\left|t_{1,l}^{\prime}\right|\right)\right|.\end{aligned} \quad (8) \] 

Generally, if the Lyapunov exponent  \( \gamma > 0 \)  ( \( \gamma = 0 \) ), the corresponding wave function will have the characteristics of localization (extension).

Since the generalized quasiperiodic modulation can be distinguished as bounded (Sec. III) and unbounded (Sec. IV) cases, in the following sections, we will discuss these two typical cases, respectively.

## III. TOPOLOGICAL REPT FOR THE BOUNDED CASE

Let's start with the bounded case, i.e., the case where b < 1. Without loss of generality, we fix b = 0.9 to show how the topological properties of the system change with  \( \lambda \)  and  \( t_{1} \) . The corresponding results are shown in Fig. 2(a). We find that, unlike traditional topological phase transitions, topological REPT phenomena will occur in the range of parameter  \( t_{1} \in [0.7, 1] \)  for the model of Eq. (1). Taking  \( t_{1} = 0.8 \)  (red dashed line) as an example. One can see that topological REPT phenomenon will emerge as the quasiperiodic strength  \( \lambda \)  increases. Specifically, the system starts from a traditional TI phase. With the increase of  \( \lambda \) , the system first enters the trivial phase, and then enters the TAI phase. Finally, when the disorder strength completely dominates, the system will enter the trivial region due to Anderson localization. We refer to this phenomenon of re-entrant from traditional TI into TAI as the type-I of topological REPT.

Besides, the bulk energy gap under periodic boundary conditions (PBCs), a quantity commonly used to indicate critical points, is used here to verify again the emergence of topological REPT. The corresponding gap is plotted in Fig. 2(b). Here, we rescale the gap with  \( \ln \)  function for a more intuitive display. In other words, the red region in

![](./images/1074212940535562252_3.jpg)

FIG. 2: (a) The real-space winding number  \( \nu \)  as functions of  \( \lambda \)  and  \( t_{1} \) . The red dashed line corresponds to the line of  \( t_{1}=0.8 \) . (b) The bulk gap ( \( \Delta E \) ) as functions of  \( \lambda \)  and  \( t_{1} \) . (c) The winding number (red solid line) and Lyapunov exponent (black solid line) versus quasiperiodic strength  \( \lambda \)  with  \( t_{1}=0.8 \) . (d) The middle 200 eigenenergies versus  \( \lambda \)  with  \( t_{1}=0.8 \) . The emergence of topological zero modes are marked with red lines. Throughout, b=0.9.

the figure corresponds to the open bulk gap, while other colors all to the closed gap. As shown in the figure, the emergence of topological REPT is accompanied by the bulk gap's closing and reopening. Note that, the boundary in the upper right corner of Fig. 2(b) indicates the traditional Anderson phase transition due to the increase in quasiperiodic strength. This also shows that bulk gap is universal as a critical point. In other words, it is not only limited to determining the critical points of topological phase transitions, but can also be used to determine the critical points of other various types of phase transitions. It is not difficult to find that for Anderson phase transition, the energy gap will remain unchanged after closing and will never be opened again.

Furthermore, in Fig. 2(c), we show how the corresponding winding number and Lyapunov exponent of the system change with the  \( \lambda \) . The result confirms once again that topological REPT can emerge in the system. It is worth noting that during topological REPT, the Lyapunov exponent always tends to be zero at all critical points of topological phase transitions (i.e., where the winding number changes abruptly). This is because topological protected edge states will always appear when the system is in a nontrivial phase (TI or TAI). Since these edge states are localized in the vicinity of boundary, the wave function also exhibits exponential decay, i.e.,  \( \psi \propto e^{-\gamma n} \) . On the other hand, with the increase of
 

disorder, Anderson localization occurs in the system, and the corresponding wave function will be localized. The competition between the localized wave functions on the edge and in the middle of the atomic chain eventually causes the Lyapunov exponent corresponding to the critical point to approach zero. Fig. 2(d) shows the energy spectra corresponding to the middle 200 eigenvalues of the system. Similarly, through the appearance and disappearance of zero mode, one can find that topological REPT does emerge in the system.

To show the topological REPT phenomenon more clearly, we plot the density distribution of the wave function corresponding to the topological zero-mode bands (the 610-th and 611-th eigenenergies) in Fig. 3.

![](./images/1074212940535562252_4.jpg)

FIG. 3: Density distribution of the N-th and  \( N+1 \) -th eigenstates under the condition of  \( \lambda=0 \) , 0.5, 2.5, 2 (marked by green squares in Fig. 2). Throughout, we set  \( t_{1}=0.8 \) .

Fig. 3(a)-(d) correspond to the parameter values of the green square in Fig. 2(a), respectively. One can find that when the system is in the topological phase, the topological edge states will appear, while the edge states will not emerge in the trivial phase. Note that, because the reappearance of the topological or trivial phase are due to the localization properties caused by the strong quasiperiodic modulation, the corresponding wave function, which is of the localized state rather than the extended state [see Fig. 3(d)], is therefore different from that of the first trivial region. With the visualized density distribution mentioned here, we reconfirm our conclusion that topological REPT does emerge in the system.

## IV. TOPOLOGICAL REPT FOR THE UNBOUNDED CASE

Next, let's turn to the unbounded case, i.e., under the condition of  \( b \geq 1 \)  [80, 81]. Using winding number, we exhibit the corresponding topological phase diagram in the  \( t_{1}-\lambda \)  plane (see in Fig. 4). The results also exhibit that topological REPT emerges. In concrete terms, the system will first go from a trivial state to a TAI. Then, with the increase of quasiperiodic strength, the system will jump out of the TAI phase into a trivial phase. After that, it will enter the TAI phase again. Similarly, because the quasiperiodic strength will eventually dominate, the system will thus end up in a trivial localized phase. Note that, unlike type-I topological REPT (TI→TAI), in the unbounded case, both topological phases of the system are TAI phases induced by quasiperiodic modulation. We name this type of REPT from TAI into TAI as type-II topological REPT. For the unbounded case, we also analyze the energy gap, winding number, Lyapunov exponent and topological zero module respectively, and the results consistently prove that topological REPT can occur in the system.

![](./images/1074212940535562252_5.jpg)

![](./images/1074212940535562252_6.jpg)

![](./images/1074212940535562252_7.jpg)

![](./images/1074212940535562252_8.jpg)

FIG. 4: (a) The real-space winding number  \( \nu \)  as functions of  \( \lambda \)  and  \( t_{1} \) . The red dashed line corresponds to the line of  \( t_{1}=1.2 \) . (b) The bulk gap ( \( \Delta E \) ) as functions of  \( \lambda \)  and  \( t_{1} \) . (c) The winding number (red solid line) and Lyapunov exponent (black solid line) versus quasiperiodic strength  \( \lambda \)  with  \( t_{1}=1.2 \) . (d) The middle 200 eigenenergies versus  \( \lambda \)  with  \( t_{1}=1.2 \) . The emergence of topological zero modes are marked with red lines. Throughout,  \( b=1.5 \) .

For a more visualized presentation, we calculate the corresponding eigenstate wave functions under different quasiperiodic strengths. Specifically, the system first shows the trivial phase not yet being localized. Then,
 

with the increase of quasiperiodic intensity, we notice that the system begins to appear edge states, which is the evidence that the system has entered the topological phase. Subsequently, further increases of the quasiperiodic intensity pull the topological edge states back into the atomic chain, and this competition leads to the emergence of an intermediate state where the wave function structure is between the extended and localized states [see Fig. 5(c)]. After that, the edge state will appear again, which indicates that the system again enters the topological phase. Finally, because the localization properties prevail, the wave function of the system shows characteristics of the localized state. These visualized results are consistent with the analysis of the core physical quantities in Fig. 5, i.e., topological REPT emerges in the system.

![](./images/1074212940535562252_9.jpg)

FIG. 5: Density distribution of the N-th and  \( N+1 \) -th eigenstates under the condition of  \( \lambda=0 \) , 0.5, 1.5, 3, 3.5 (marked by green squares in Fig. 4). Throughout, we set  \( t_{1}=1.2 \) .

## V. CONCLUSIONS

In summary, we introduce generalized quasiperiodic modulation into the primitive intracellular coupling of SSH model and thus obtain topological REPT. In addition, for bounded and unbounded cases, we give the phase diagram of the system by calculating winding number, and verify the diagram by Lyaponov exponent, zero mode and wave function properties. The results show that the topological REPT from TI to TAI occurs in the bounded case, while the topological phase transition from TAI to TAI occurs in the unbounded case. The SSH model discussed in this paper has recently been experimentally realized in Rydberg atomic array system  \( [64] \) . On this basis, we only need to use Rydberg single point manipulation technology to modulate the intracellular coupling intensity  \( [82–85] \) , so as to realize the REPT phenomenon predicted in this paper. It is hoped that this paper can bring benefits to the research on topological characteristics of quasiperiodic systems, Rydberg atomic arrays and other related fields.

## VI. ACKNOWLEDGEMENTS

This work was supported by the National Key Research and Development Program of China (Grant No.2022YFA1405300), the National Natural Science Foundation of China (Grant No.12074180), the Guangdong Basic and Applied Basic Research Foundation (Grants No.2021A1515012350), and Open Fund of Key Laboratory of Atomic and Subatomic Structure and Quantum Control (Ministry of Education).

## Appendix A: FINITE SIZE EFFECT

In the numerical calculation, the total number of primitive cells we selected is 610, i.e., the atomic chain contains 1220 sites. It has been proved by many times of numerical calculation that, the size we chose can accurately show the characteristics of all the key quantities at a small computational cost. Taking the winding number as an example, we exhibit below the results of winding numbers with different sizes (see Fig. 6).

![](./images/1074212940535562252_10.jpg)

FIG. 6: Real-space winding number  \( \nu \)  as functions of  \( \lambda \) . The yellow dot, green solid, and blue dash lines are plotted to describe the system size with N = 200, N = 610, N = 987, respectively. In all cases, b = 1.5 and  \( t_{1} = 1.2 \) .
 

From the figure, it can be seen clearly that When the system size is small, the calculated winding number is not correct. However, when the size becomes larger, one can calculate the corresponding winding number more accurately. After test, we find that N = 610 is sufficient.

On the other hand, due to the introduction of quasi-periodic modulation, the translational symmetry of the system is broken. Therefore, we have to study the topological properties through the real-space winding number [78]. Since the calculation process is carried out for a finite size, the block effect of the matrix is revealed. The expression of winding number with different matrix block reads

 \[ \nu_{i}=\frac{1}{L_{i}}\mathrm{T r}_{i}(\Gamma\mathrm{Q}[\mathrm{Q},\mathrm{X}]), \quad (A1) \] 

where  \( \Gamma \) , Q, and X are matrices of  \( 2N \times 2N \) .  \( Tr_{i} \)  denote traces for different matrix blocks. Due to the finite-size effect, one needs to trace a part of the matrix (see Fig. 7). To demonstrate that region selection can indeed make a difference, we show winding numbers calculated by selecting different regions in Fig. 7.

![](./images/1074212940535562252_11.jpg)

FIG. 7: The winding number for N = 610 with different matrix traces.  \( \nu_{1} \)  ( \( \nu_{2} \) ) is the average of trace over the whole (half) matrix. The corresponding trace region are marked by red (blue) square box. The colored boxes are color-matched to the line in the winding number plot.

With a fixed primitive size N = 610, we show the case of trace with the whole matrix  \( (L) \)  and the half matrix blocks  \( (L/2) \) , respectively. It is not difficult to find that the winding number is best calculated using the trace of the central L/2 block. However, when we choose the trace of the whole matrix to calculate the winding number, there will be obvious errors in the result. This is because as a topology marker, the edge elements of the diagonal matrix in Eq. (A1) lead to inaccurate results.

[1] J. Wang and S. C. Zhang, Topological states of condensed matter, Nat. Mater. 16, 1062 (2017).

[2] M. He, H. Sun, and Q. L. He, Topological insulator: Spintronics and quantum computations, Front. Phys. 14,

[see Fig. 7(b)]. Therefore, as in previous studies [26, 27], in main text, we also select the central L/2 region to calculate the winding number.

Appendix B: TOPOLOGICAL PHASE DIAGRAM FOR THE BOUNDED TO UNBOUNDED CASE

The expression of the quasiperiodic modulation we introduce is,

 \[ t_{1}^{^{\prime}}=t_{1}+\frac{\lambda\cos(2\pi\alpha n+\theta)}{1-b\cos(2\pi\alpha\underline{n}+\theta)}, \quad (B1) \] 

One can find that the denominators of the quasiperiodic modulation term always converge for b < 1, and diverge for  \( b \geq 1 \) . These two different types of quasiperiodic modulation are often referred to as bounded and unbounded cases [81, 86]. As we all know, the change of the structure of quasiperiodic modulation will lead to changes in the corresponding topological properties, therefore there will be two different types of topological REPTs [74, 75] (see Fig. 8). The figure below shows how the phase diagram changes from bounded to unbounded case. It is not difficult to see that b = 1 is the critical point from type-I topological REPT to type-II topological REPT. One can also see that the increase of the value of b will cause the REPT region to move towards the larger  \( \lambda \)  direction. Therefore, when the value of b is fairly large, the REPT phenomenon cannot be seen in the relatively weak quasiperiodic region [see Fig. 8(f)].

![](./images/1074212940535562252_12.jpg)

FIG. 8: (a), (b), and (c) correspond to bounded systems with b = 0, 0.5, and 0.9, respectively. (d), (e), and (f) correspond to unbounded systems with b = 1.5, 2, and 5, respectively.

43401 (2019).

[3] A. Bansil, H. Lin, and T. Das, Colloquium: Topological band theory, Rev. Mod. Phys. 88, 021004 (2016).

[4] H. Weng, X. Dai, and Z. Fang, Exploration and pre-
 

diction of topological electronic materials based on first-principles calculations, MRS Bull. 39, 849 (2014).

[5] P. Liu, J. R. Williams, and J. J. Cha, Topological nanomaterials, Nat. Rev. Mater. 4, 479 (2019).

[6] D. Pesin and A. H. MacDonald, Spintronics and pseudospintronics in graphene and topological insulators, Nat. Mater. 11, 409 (2012).

[7] D. Hsieh, D. Qian, L. Wray, Y. Xia, Y. S. Hor, R. J. Cava, and M. Z. Hasan, A topological Dirac insulator in a quantum spin Hall phase, Nature (London) 452, 970 (2008).

[8] L. Fu and C. L. Kane, Topological insulators with inversion symmetry, Phys. Rev. B 76, 045302 (2007).

[9] D. Hsieh, Y. Xia, D. Qian, L. Wray, J. H. Dil, F. Meier, J. Osterwalder, L. Patthey, J. G. Checkelsky, N. P. Ong, A. V. Fedorov, H. Lin, A. Bansil, D. Grauer, Y. S. Hor, R. J. Cava, and M. Z. Hasan, A tunable topological insulator in the spin helical Dirac transport regime, Nature (London) 460, 1101 (2009).

[10] T. H. Hsieh, H. Lin, J. Liu, W. Duan, A. Bansil, and L. Fu, Topological crystalline insulators in the SnTe material class, Nat. Commun. 3, 982 (2012).

[11] B. A. Bernevig, T. L. Hughes, and S.-C. Zhang, Quantum spin Hall effect and topological phase transition in HgTe quantum wells, Science 314, 1757 (2006).

[12] Y. Li, P. Chen, G. Zhou, J. Li, J. Wu, B.-L. Gu, S. B. Zhang, and W. Duan, Dirac Fermions in Strongly Bound Graphene Systems, Phys. Rev. Lett. 109, 206802 (2012).

[13] C. Weeks, J. Hu, J. Alicea, M. Franz, and R. Wu, Engineering a Robust Quantum Spin Hall State in Graphene via Adatom Deposition, Phys. Rev. X 1, 021001 (2011).

[14] K.-H. Jin and S.-H. Jhi, Proximity-induced giant spin-orbit interaction in epitaxial graphene on a topological insulator, Phys. Rev. B 87, 075442 (2013).

[15] Q.-X. Lv, Y.-X. Du, Z.-T. Liang, H.-Z. Liu, J.-H. Liang, L.-Q. Chen, L.-M. Zhou, S.-C. Zhang, D.-W. Zhang, B.-Q. Ai, H. Yan, and S.L. Zhu, Measurement of Spin Chern Numbers in Quantum Simulated Topological Insulators, Phys. Rev. Lett. 127, 136802 (2021).

[16] F. Mei, Q. Guo, Y.-F. Yu, L. Xiao, S.-L. Zhu, and S. Jia, Digital Simulation of Topological Matter on Programmable Quantum Processors, Phys. Rev. Lett. 125, 160503 (2020).

[17] X. Tan, D.-W. Zhang, Z. Yang, J. Chu, Y.-Q. Zhu, D. Li, X. Yang, S. Song, Z. Han, Z. Li, Y. Dong, H.-F. Yu, H. Yan, S.-L. Zhu, and Y. Yu, Experimental Measurement of the Quantum Metric Tensor and Related Topological Phase Transition with a Superconducting Qubit, Phys. Rev. Lett. 122, 210401 (2019).

[18] M. Z. Hasan and C. L. Kane, Colloquium: Topological insulators, Rev. Mod. Phys. 82, 3045 (2010).

[19] X.-L. Qi and S.-C. Zhang, Topological insulators and superconductors, Rev. Mod. Phys. 83, 1057 (2011).

[20] R. S. K. Mong and V. Shivamoggi, Edge states and the bulk boundary correspondence in Dirac Hamiltonians, Phys. Rev. B 83, 125109 (2011).

[21] K. Yatsugi, T. Yoshida, T. Mizoguchi, Y. Kuno, H. Iizuka, Y. Tadokoro, and Y. Hatsugai, Observation of bulk-edge correspondence in topological pumping based on a tunable electric circuit, Commun. Phys. 5, 180 (2022).

[22] S. Chen, L. Bu, C. Pan, C. Hou, F. Baronio, P. Grelu, and N. Akhmediev, Modulation instability–rogue wave correspondence hidden in integrable systems, Commun.

Phys. 5, 297 (2022).

[23] Y. Hasegawa, Unifying speed limit, thermodynamic uncertainty relation and Heisenberg principle via bulk-boundary correspondence, Nat. Commun. 14, 2828 (2023).

[24] D.-W. Zhang, Y.-Q. Zhu, Y. X. Zhao, H. Yan, and S.-L. Zhu, Topological quantum matter with cold atoms, Adv. Phys. 67, 253 (2019).

[25] P. W. Anderson, Absence of diffusion in certain random lattices, Phys. Rev. 109, 1492 (1958).

[26] L.-Z. Tang, S.-N. Liu, G.-Q. Zhang, and D.-W. Zhang, Topological Anderson insulators with different bulk states in quasiperiodic chains, Phys. Rev. A 105, 063327 (2022).

[27] Z. Lu, Z. Xu, and Y. Zhang, Exact mobility edges and topological Anderson insulating phase in a slowly varying quasiperiodic model, Ann. Phys. 534, 2200203 (2022).

[28] J. Li, R.-L. Chu, J. K. Jain, and S.-Q. Shen, Topological Anderson insulator, Phys. Rev. Lett. 102, 136806 (2009).

[29] C. W. Groth, M. Wimmer, A. R. Akhmerov, J. Tworzydło, and C. W. J. Beenakker, Theory of the topological anderson insulator, Phys. Rev. Lett. 103, 196805 (2009).

[30] A. Yamakage, K. Nomura, K.-I. Imura, and Y. Kuramoto, Disorder-induced multiple transition involving  \( Z_{2} \)  topological insulator, J. Phys. Soc. Jpn. 80, 053703 (2011).

[31] Y. Xing, L. Zhang, and J. Wang, Topological Anderson insulator phenomena, Phys. Rev. B 84, 035110 (2011).

[32] H. Jiang, L. Wang, Q.-F. Sun, and X. C. Xie, Numerical study of the topological Anderson insulator in HgTe/CdTe quantum wells, Phys. Rev. B 80, 165316 (2009).

[33] Y.-Y. Zhang, R.-L. Chu, F.-C. Zhang, and S.-Q. Shen, Localization and mobility gap in the topological Anderson insulator, Phys. Rev. B 85, 035107 (2012).

[34] G.-Q. Zhang, L.-Z. Tang, L.-F. Zhang, D.-W. Zhang, and S. L. Zhu, Connecting topological Anderson and Mott insulators in disordered interacting fermionic systems, Phys. Rev. B 104, L161118 (2021).

[35] S. N. Liu, G. Q. Zhang, L. Z. Tang, and D.-W. Zhang, Topological Anderson insulators induced by random binary disorders, Phys. Lett. A 104, 128004 (2022).

[36] J. Song, H. Liu, H. Jiang, Q.-f. Sun, and X. Xie, Dependence of topological Anderson insulator on the type of disorder, Phys. Rev. B 85, 195125 (2012).

[37] L. Chen, Q. Liu, X. Lin, X. Zhang, and X. Jiang, Disorder dependence of helical edge states in HgTe/CdTe quantum wells, New J. Phys. 14, 043028 (2012).

[38] J. Song and E. Prodan, AIII and BDI topological systems at strong disorder, Phys. Rev. B 89, 224203 (2014).

[39] H.-C. Hsu and T.-W. Chen, Topological Anderson insulating phases in the long-range Su-Schrieffer-Heeger model, Phys. Rev. B 102, 205425 (2020).

[40] L. Lin, Y. Ke, and C. Lee, Real-space representation of the winding number for a one-dimensional chiral-symmetric topological insulator, Phys. Rev. B 103, 224208 (2021).

[41] Z.-Q. Zhang, B.-L. Wu, J. Song, and H. Jiang, Topological Anderson insulator in electric circuits, Phys. Rev. B 100, 184202 (2019).

[42] X. Shi, I. Kiorpelidis, R. Chaunsali, V. Achilleos, G. Theocharis, and J. Yang, Disorder-induced topological phase transition in a one-dimensional mechanical system,
 

Phys. Rev. Res. 3, 033012 (2021).

[43] D. Bagrets, K. W. Kim, S. Barkhofen, S. De, J. Sperling, C. Silberhorn, A. Altland, and T. Micklitz, Probing the topological Anderson transition with quantum walks, Phys. Rev. Res. 3, 023183 (2021).

[44] S. Huang, Y.-Q. Zhu, Z. Li, Emergent non-Abelian Thouless pumping induced by the quasiperiodic disorder, Phys. Rev. A 109, 052213 (2024).

[45] X. Cui, R.-Y. Zhang, Z.-Q. Zhang, and C. T. Chan, Photonic  \( Z_{2} \)  Topological Anderson Insulators, Phys. Rev. Lett. 129, 043902 (2022).

[46] X. Cheng, T. Qu, L. Xiao, S. Jia, J. Chen, and L. Zhang, Topological Anderson amorphous insulator, Phys. Rev. B 108, L081110 (2023).

[47] W. Zhang, D. Zou, Q. Pei, W. He, J. Bao, H. Sun, and X. Zhang, Experimental Observation of Higher-Order Topological Anderson Insulators, Phys. Rev. Lett. 126, 146802 (2021).

[48] Y.-B. Yang, K. Li, L.-M. Duan, and Y. Xu, Higher-order topological Anderson insulators, Phys. Rev. B 103, 085408 (2021).

[49] Z.-W. Zuo, J.-R. Lin, and D. Kang, Topological inverse Anderson insulator, Phys. Rev. B 110, 085157 (2024).

[50] R. Chen, X.-X. Yi, and B. Zhou, Four-dimensional topological Anderson insulator with an emergent second Chern number, Phys. Rev. B 108, 085306 (2023).

[51] T. Peng, C.-B. Hua, R. Chen, D.-H. Xu, and B. Zhou, Topological Anderson insulators in an Ammann-Beenker quasicrystal and a snub-square crystal, Phys. Rev. B 103, 085307 (2021).

[52] R. El-Ganainy, K. G. Makris, M. Khajavikhan, Z. H. Musslimani, S. Rotter, and D. N. Christodoulides, Non-Hermitian physics and PT symmetry, Nat. Phys. 14, 11 (2018).

[53] Y. Ashida, Z. Gong, and M. Ueda, Non-Hermitian Physics, Adv. Phys. 69, 3 (2020).

[54] D.-W. Zhang, Y.-L. Chen, G.-Q. Zhang, L.-J. Lang, Z. Li, and S.-L. Zhu, Skin superfluid, topological Mott insulators, and asymmetric dynamics in an interacting non-Hermitian Aubry-André-Harper model, Phys. Rev. B 101, 235150 (2020).

[55] E. J. Bergholtz, J. C. Budich, and F. K. Kunst, Exceptional topology of non-Hermitian systems, Rev. Mod. Phys. 93, 015005 (2021).

[56] N. Okuma and M. Sato, Non-Hermitian topological phenomena: A review, Annu. Rev. Condens. Matter Phys. 14, 83 (2023).

[57] A. Li, H. Wei, M. Cotrufo, W. Chen, S. Mann, X. Ni, B. Xu, J. Chen, J. Wang, S. Fan, C.-W. Qiu, A. Alú, and L. Chen, Exceptional points and non-Hermitian photonics at the nanoscale, Nat. Nanotechnol. 18, 706 (2023).

[58] R. Lin, T. Tai, L. Li, and C.H. Lee, Topological non-Hermitian skin effect, Front. Phys. 18, 53605 (2023).

[59] D.-W Zhang, L. Z. Tang, L. J. Lang, H. Yan, and S. L. Zhu, Non-Hermitian topological Anderson insulators, Sci. China-Phys. Mech. Astron. 63, 267062 (2020).

[60] Q. Lin, T. Li, L. Xiao, K. Wang, W. Yi, and P. Xue, Observation of non-Hermitian topological Anderson insulator in quantum dynamics, Nat. Commun. 13, 3229 (2022).

[61] H. F. Liu, Z. X. Su, Z. Q. Zhang, and H. Jiang, Topological Anderson insulator in two-dimensional non-Hermitian systems, Chin. Phys. B 29, 050502 (2020).

[62] L. Z. Tang, L. F. Zhang, G. Q. Zhang, and D.-W. Zhang,

Topological Anderson insulators in two-dimensional non-Hermitian disordered systems, Phys. Rev. A 101, 063612 (2020).

[63] L. B. Shao, S. L. Zhu, L. Sheng, D. Y. Xing, and Z. D. Wang, Realizing and Detecting the Quantum Hall Effect without Landau Levels by Using Ultracold Atoms, Phys. Rev. Lett. 101, 246810 (2008).

[64] E. J. Meier, F. A. An, A. Dauphin, M. Maffei, P. Massignan, T. L. Hughes, and B. Gadway, Observation of the topological Anderson insulator in disordered atomic wires, Science 362, 929 (2018).

[65] D.-W. Zhang, Y.-Q. Zhu, Y.X. Zhao, H. Yan, and S.-L. Zhu, Topological quantum matter with cold atoms, Adv. Phys. 67, 253 (2018).

[66] S. Stützer, Y. Plotnik, Y. Lumer, P. Titum, N. H. Lindner, M. Segev, M.C. Rechtsman, and A. Szameit, Photonic topological Anderson insulators, Nature (London) 560, 461 (2018).

[67] G.-G. Liu, Y. Yang, X. Ren, H. Xue, X. Lin, Y.-H. Hu, H. X. Sun, B. Peng, P. Zhou, Y. Chong, and B. Zhang, Topological Anderson Insulator in Disordered Photonic Crystals, Phys. Rev. Lett. 125, 133603 (2020).

[68] F. Zangeneh-Nejad and R. Fleury, Disorder-induced signal filtering with topological metamaterials, Adv. Mater. 32, 2001034 (2020).

[69] X. Li, H. Xu, J. Wang, L.-Z. Tang, D.-W. Zhang, C.

Yang, T. Su, C. Wang, Z. Mi, W. S, X. Liang, M. Chen, C. Li, Y. Zhang, K. Linghu, J. Han, W. Liu, Y. Feng, P. Liu, G. Xue, J. Zhang, Y. Jin, S.-L. Zhu, H. Yu, S. P. Zhao, and Q.-K. Xue, Mapping the topology-localization phase diagram with quasiperiodic disorder using a programmable superconducting simulator, Phys. Rev. Res. 6, L042038 (2024).

[70] W. Zhang, D. Zou, Q. Pei, W. He, J. Bao, H. J. Sun, and X. Zhang, Experimental Observation of Higher-Order Topological Anderson Insulators, Phys. Rev. Lett. 126, 146802 (2021).

[71] H. Fujii, T. Okamoto, T. Shigeoka, and N. Iwata, Reentrant ferromagnetism observed in  \( SmMn2Ge2 \) , Solid State Commun. 53, 715 (1985).

[72] S. Aubry and G. André, Analyticity breaking and Anderson localization in incommensurate lattices, Ann. Israel Phys. Soc 3, 18 (1980).

[73] S. Roy, T. Mishra, B. Tanatar, and S. Basu, Reentrant Localization Transition in a Quasiperiodic Chain, Phys. Rev. Lett. 126, 106803 (2021).

[74] M. Tezuka and N. Kawakami, Reentrant topological transitions in a quantum wire/superconductor system with quasiperiodic lattice modulation, Phys. Rev. B 85, 140508(R) (2012).

[75] Z. Lu, Y. Zhang, and Z. Xu, Reentrant Localization Transitions in a Topological Anderson Insulator: A Study of a Generalized Su-Schrieffer-Heeger Quasicrystal, Front. Phys. 20, 024204 (2025).

[76] S. Ganeshan, J. H. Pixley, and S. Das Sarma, Nearest Neighbor Tight Binding Models with an Exact Mobility Edge in One Dimension, Phys. Rev. Lett. 114, 146601 (2015).

[77] W. P. Su, J. R. Schrieffer, and A. J. Heeger, Soliton excitations in polyacetylene, Phys. Rev. B 22, 2099 (1980).

[78] I. Mondragon-Shem, T. L. Hughes, J. Song, and E. Prodan, Topological Criticality in the Chiral-Symmetric AIII Class at Strong Disorder, Phys. Rev. Lett. 113, 046802 (2014).
 

[79] J. A. Scales and E. S. Van Vleck, Lyapunov exponents and localization in randomly layered media, J. Comput. Phys. 133, 27 (1997).

[80] T. Liu, X. Xia, S. Longhi, and L. Sanchez-Palencia, Anomalous mobility edges in one-dimensional quasiperiodic models, SciPost Phys. 12, 27 (2022).

[81] Y.-C. Zhang and Y.-Y. Zhang, Lyapunov exponent, mobility edges, and critical region in the generalized Aubry-André model with an unbounded quasiperiodic potential, Phys. Rev. B 105, 174206 (2022).

[82] G. Semeghini, H. Levine, A. Keesling, S. Ebadi, T. T. Wang, D. Bluvstein, R. Verresen, H. Pichler, M. Kalinowski, R. Samajdar et al., Probing topological spin liquids on a programmable quantum simulator, Science 374, 1242 (2021).

[83] D. Bluvstein, H. Levine, G. Semeghini, T. T. Wang, S. Ebadi, M. Kalinowski, A. Keesling, N. Maskara, H. Pichler, M. Greiner, V. Vuletić, and M. D. Lukin, A quantum processor based on coherent transport of entangled atom arrays, Nature (London) 604, 451 (2022).

[84] D. Bluvstein, S. J. Evered, A. A. Geim, S. H. Li, H. Zhou, T. Manovitz, S. Ebadi, M. Cain, M. Kalinowski, D. Hangleiter, J. P. B. Ataides, N. Maskara, I. Cong, X. Gao, P. S. Rodriguez, T. Karolyshyn, G. Semeghini, M. J. Gullans, M. Greiner, V. Vuletić, and M. D. Lukin, Logical quantum processor based on reconfigurable atom arrays, Nature (London) 626, 58 (2024).

[85] T. Manovitz, S. H. Li, S. Ebadi, R. Samajdar, A. A. Geim, S. J. Evered, D. Bluvstein, H. Zhou, N. U. Koyluoglu, J. Feldmeier, P. E. Dolgirev, N. Maskara, M. Kalinowski, S. Sachdev, D. A. Huse, M. Greiner, V. Vuletić, M. D. Lukin, Quantum coarsening and collective dynamics on a programmable quantum simulator, arXiv: 2407.03249.

[86] B. Simon and T. Spencer, Trace class perturbations and the absence of absolutely continuous spectra, Commun. Math. Phys. 125, 113 (1989).
 
