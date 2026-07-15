# Modeling Abnormal Strain States in Ferroelastic Systems: The Role of Point Defects

Dong Wang, $^{1,2}$ Yunzhi Wang, $^{1,2,*, \dagger}$ Zhen Zhang, $^{1}$ and Xiaobing Ren $^{1,3,*, \ddagger}$

$^{1}$Center for Computational Study of Microstructure Evolution in Materials and Multi-Disciplinary Materials Research Center, Frontier Institute of Science and Technology, State Key Laboratory for Mechanical Behavior of Materials, Xi'an Jiaotong University, Xi'an 710049, China  
$^{2}$Department of Materials Science and Engineering, The Ohio State University, 2041 College Road, Columbus, Ohio 43210, USA  
$^{3}$Ferroic Physics Group, National Institute for Materials Science, Tsukuba, 305-0047, Ibaraki, Japan

(Received 12 July 2010; revised manuscript received 27 September 2010; published 11 November 2010)

Recent experiments have revealed a rich variety of strain states in doped ferroelastic systems. We study the origin of two abnormal strain states; precursory tweed and strain glass, and their relationship with the well-known austenite and martensite (the para- and ferroelastic states). A Landau free energy model is proposed, which assumes that point defects alter the global thermodynamic stability of martensite and create local lattice distortions that interact with the strain order parameters and break the symmetry of the Landau potential. Phase field simulations based on the model have predicted all the important signatures of a strain glass found in experiment. Moreover, the generic "phase diagram" constructed from the simulation results shows clearly the relationships among all the strain states, which agrees well with experimental measurements.

DOI: 10.1103/PhysRevLett.105.205702
PACS numbers: 64.70.K-, 62.20.D-, 64.70.P-, 81.30.Kf

Ferroelastic materials, are generally characterized by two distinct strain states, a strain-disordered paraelastic state (known as the parent phase or austenite) at high temperature and a long-range strain-ordered ferroelastic state (known as martensite) at low temperature. Point defects have been known to play a central role in altering and controlling the properties of ferroelastic materials [1]. In addition to the well-known paraelastic and ferroelastic strain states, it was found that point defects can generate two abnormal strain states: a "precursory strain state" (or tweed) characterized by a cross-hatched nanosized strain domain structure [2,3] imbedded in a dynamically disor- dered paraelastic matrix [4] and a new strain-glass state that is a frozen state of local strain order [5-8], a ferroe- lastic analogue to ferroelectric relaxors [9] and cluster spin glasses [10,11].

Recent experimental studies have yielded strikingly similar "phase diagrams" of strain states for many different doped ferroelastic systems [12-14]. An example is given in Fig. 1(a) for a Fe-doped TiNi system [12]. It describes clearly the relationships among all the strain states in fer- roelastic systems and shows the following generic features: (i) at a critical doping level $x_{c}$ there exists a rather abrupt crossover from a normal martensitic transition (MT) $(x < x_{c})$ to a strain-glass transition (SGT) $(x > x_{c})$; (ii) a precursory strain state appears below a temperature $T_{nd }$ , which is well above the $M_{s}$ (MT start temperature) or $T_{g}$ (SGT temperature); (iii) both $M_{s}$ and $T_{g}$ decrease with increasing defect content while $T_{nd }$ decreases at low defect content but increases at high defect content. This generic phase diagram could serve as an experimental validation of any theory proposed to explain the relationship among different strain states in ferroelastic systems.

The nature of the precursory strain state (tweed) has been an interesting topic for decades, because it is neither a fully disordered strain state like an ideal austenite nor a fully ordered strain state like the poly-twinned martensite. The recent discovery of strain glass, a frozen disordered strain state, has added a new facet to the "nonideal" strain states. A number of theoretical studies have attempted to elucidate the nature of tweed [15,16] and strain glass [17-19] states and insights have been gained from the established theories of spin glass [11,20]. It was proposed that these nonideal strain states are caused by concentra- tion fluctuation of random point defects, which result in a spatial fluctuation in $M_{s}$ [called local transition tempera ture fluctuation effect (LTTE)]. At very high defect con- centrations, it could also be possible that the tweed persists upon cooling without transforming into martensite, i.e., freezing into a strain glass [17-19]. However, character- ized by an isotropic or non-symmetry-breaking effect of point defects, the LTTE has yet to be shown able to reproduce the above-mentioned generic phase diagram of the strain states.

In this Letter we propose an alternative model assuming the following two roles played by the point defects: (i) they change the stability of martensite globally rather than lo- cally [called global transition temperature effect (GTTE) hereafter]; (ii) they produce local lattice distortions that interact with the strain order parameters and break the symmetry of the Landau potential [called local field effect (LFE) hereafter]. Through phase field simulations [16,21,22] we show that this model not only reproduces the crossover from martensite to strain glass at $x > x_{c}$ , but also captures all the important features of the generic phase diagram [see Fig. 1(b)], such as the relatively low crossover

![](./images/811704079318253568_1.jpg)

FIG. 1 (color online). (a) Experimental phase diagram of ${\rm Ti}_{50}{\rm Ni}_{50-x}{\rm Fe}_{x}$ system (from Ref. [12]). $R_s$ and $M_s$ denote the transformation start temperatures of $R$ and B19$^\prime$ martensites, $T_{\rm nd}$ is the start temperature of static nanodomains, $T_g$ is the strain-glass transition temperature. (b) The calculated phase diagram. $M_s$, $T_{\rm nd}$, and $T_g$ are determined in Fig. 4.

defect concentration $x_c$ and the weak composition dependence of $T_g$.

For simplicity we consider a single crystal undergoing a generic improper square to rectangle (2-D) MT [16,21]. The Landau free energy without point defects is described by

$$
\begin{aligned}
f_{\mathrm{ch}}\left(\eta_{i=1,2}\right)= & \frac{A_{1}}{2} \sum_{i=1,2} \eta_{i}^{2}-\frac{A_{2}}{4} \sum_{i=1,2} \eta_{i}^{4}+\frac{A_{3}}{4}\left(\sum_{i=1,2} \eta_{i}^{2}\right)^{2} \\
& +\frac{A_{4}}{6}\left(\sum_{i=1,2} \eta_{i}^{2}\right)^{3},
\end{aligned}
\tag{1}
$$

where $\eta_{i}(\mathbf{r})$ ($i=1$, 2) are the long-range order (lro) parameters characterizing the two orientation variants of the martensitic phase and $A_{1}-A_{4}$ are the expansion coefficients. The effect of point defects on the overall matensitic transition temperature of the system (i.e., the GTTE) can be characterized by making the leading term coefficient, $A_{1}$, dependent on defect concentration, e.g., $A_{1}=A_{1}^{0}[T-T^{0}(c)]$, and $T^{0}(c)=T^{00}+b c$, where $T$ is temperature, $T^{00}$ is the critical transition temperature without defect, $T^{0}(c)$ describes the critical transition temperature at defect concentration $c$, and $b$ characterizes the GTTE strength. In the numerical simulations, $c$ is defined as a dimensionless average defect concentration measured in terms of area fraction. The coefficients in the Landau polynomial are normalized by the typical transformation "chemical" driving force $\Delta f=1.85 \times 10^{6} \mathrm{~J} / \mathrm{m}^{3}$ [23] and their values used in the simulations are $A_{1}{ }^{0}=0.05\left(T-T^{0}\right), A_{2}=30$, $A_{3}=19$ and $A_{4}=10$.

The LFE [13,24] caused by point defects is described by $f_{L}(\mathbf{r})=\sum_{i, j=1,2 ; m=1,3,5} \eta_{i}^{\text {local }}(\mathbf{r}) \eta_{j}^{m}(\mathbf{r})$, where $\eta_{i}^{\text {local }}(\mathbf{r})$ ($i=1$, 2), describe local fields associated with the static point defects. The possible physical origin of the LFE (e.g., lattice distortion caused by the point defect) is shown schematically in Fig. 2(a) and the corresponding effects on the Landau free energy curves are shown in Figs. 2(b) and 2(c). For comparison, the normal Landau free energy and its temperature dependence in a defect-free crystal described by Eq. (1) is shown in Fig. 2(d). As readily seen from Figs. 2(b) and 2(c), the introduction of LFE results in a local symmetry-breaking of the Landau free energy curves. Note that this local symmetry-breaking effect from point defects exists at all temperatures and we will show that it is responsible for the appearance of the two abnormal strain states: precursory tweed and strain glass.

According to the gradient thermodynamics [25] and phase field micro-elasticity theory [26,27], the total free energy of an arbitrary nonuniform system can be written as

$$
F=\int d^{2} r\left[\frac{\beta}{2} \sum_{i=1,2}\left(\nabla \eta_{i}\right)^{2}+f_{\mathrm{ch}}\left(\eta_{1}, \eta_{2}\right)+f_{L}\right]+E_{\mathrm{el}}, \quad (2)
$$

where the first term in the square bracket is the nonlocal gradient energy term with $\beta$ ( $=4.5$ in dimensionless unit) being the gradient energy coefficient and $E_{\mathrm{el}}$ is the coherency elastic strain energy. By assuming that the product and parent phases have the same elastic modulus, a close form of $E_{\mathrm{el}}$ was derived [26,27] and the detailed formulations for MTs can be found in literature [16,21,27]. Without loosing generality, an elastically isotropic media was considered in this study, which has a shear modulus $G=40 \mathrm{GPa}$ and a Poisson ratio $\nu=0.3$. The interfacial

![](./images/811704079318253568_2.jpg)

FIG. 2 (color online). The schematic picture of local Landau potential (LP) around point defect. (a) The local lattice distortions caused by a doped point defect (black dot). (b), (c), and (d) show the LP corresponding to the three different locations. The curved arrows indicate the change of local LP with lowering temperature.

energy between the austenite and martensite was assume to be $\gamma=0.05 \mathrm{~J} / \mathrm{m}^{2}$, which yields a length scale $l_{o}=0.94 \mathrm{~nm}$.

Microstructure evolution during martensitic and strainglass transitions are obtained by solving the stochastic time-dependent Ginsburg-Landau equation

$$
\frac{d \eta_{p}(\mathbf{r}, t)}{d t}=-M \frac{\delta F}{\delta \eta_{p}(\mathbf{r}, t)}+\xi_{p}(\mathbf{r}, t), \quad p=1,2, \quad(3)
$$

where $M$ is the kinetic coefficient (assumed to be unity) and $\xi(\mathbf{r}, t)$ is the Langevin noise term. The system size in the simulations is $256 l_{0} \times 256 l_{0}$ (i.e., $240 \mathrm{~nm} \times 240 \mathrm{~nm}$ ). Periodical boundary conditions were applied.

Results obtained upon cooling from austenite at different defect concentrations $(c=0-0.2)$ are shown in Figs. 3. In the case of $c=0.0$, the system transformed into martensite with a typical poly-twinned microstructure within a narrow temperature range. At low defect concentrations $(c=0.025-0.05)$, randomly distributed nanodomains of martensite (tweed) first developed and then transformed into a long-range ordered strain state upon further cooling. When the defect concentration further increases $(c=0.075-0.2)$, the randomly distributed nanodomains no longer transformed into a long-range ordered poly-twinned microstructure upon cooling and remained stable. This is consistent with the experimental observation [5] that beyond a critical defect concentration, normal MT is replaced by SGT. The martensitic domain size decreases gradually as defect concentration increases.

![](./images/811704079318253568_3.jpg)

FIG. 3. Strain states with different defect concentrations at different temperatures. Gray describes the parent phase; white and black colors describe the two martensitic variants.

To further confirm that the system undergoes a freezing transition at high defect concentration and to determine the SGT temperature, a zero-field cooling or field cooling (ZFC/ FC) calculation was carried out for the system with $c=$ 0.125 (i.e., in the strain-glass regime). The results are shown in Fig. 4(a). With the decrease in temperature, the gap between the ZFC and FC curves increases gradually, indicating a continuous breaking of ergodicity. This is a direct evidence of a freezing process during the SGT. The simulated ZFC/FC curves in Fig. 4(a) are similar to the ZFC/FC curves obtained experimentally for $\mathrm{Ti}_{48.5} \mathrm{Ni}_{51.5}$ strain glass [6]. Furthermore, a normal MT (at $c=0.0$ ) is found to be associated with a jump at $M_{s}$ in the ZFC/FC curve together with large strain [Fig. 4(a)] and followed by a separation in the ZFC/FC curves at a lower temperature. This also agrees well with experimental ZFC/FC measurement of normal MT [28]. The separation of ZFC/FC reflects that the polytwinned martensitic structure is also nonergodic [29].

Note that the peak position in ZFC curve was defined as the glass transition temperature $T_{g}[6,10]$ while the branching point between ZFC and FC curves was referred to as the static nano strain domains formation start temperature $T_{\text {nd }}[12,13]$, a temperature at which ergodicity starts to break. Figure 4(b3) shows the determination of $T_{g}$ and $T_{\text {nd }}$ according to the ZFC/FC curves obtained from the simulations. The martensite (including nanosized domains) volume fraction curve and heat capacity curve are also shown in Figs. 4(b1) and 4(b2), where the heat

![](./images/811704079318253568_4.jpg)

FIG. 4 (color online). (a) ZFC/FC curves of normal martensitic transformation $(c=0.0)$ and strain-glass transition $(c=0.125)$. (b) Correlation among different characteristics of a strain-glass transition. (b1) Volume fraction of martensitie domains (nanosize for high defect concentrations). (b2) Heat capacity. (b3) ZFC/FC curves. (c) The heat capacity and martensite volume fraction curves at different defect concentrations. The arrows indicate the transition temperatures $(M_{s}$ or $T_{g})$ and $T_{nd}$.

205702-3

capacity was calculated through $C=-T(\partial^{2}F/\partial T^{2})$. As the dash lines show, one can easily determine $T_{g}$ by the heat capacity peak temperature and $T_{\text{nd}}$ by the martensite (including nanosized domains) volume fraction ($\sim 3\%$). According to the transition temperatures in Fig. 4(c), a phase diagram including austenite, matrensite, precursory strain state and strain glass is established in Fig. 1(b), which is in excellent agreement with the experimentally measured phase diagrams for $\text{Ti}_{50}\text{Ni}_{50-x}\text{Fe}_{x}$ [Fig. 1(a)] and $\text{Ti}_{50}\text{Ni}_{50+x}$ systems [12,13].

According to the phase diagram, the SGT can be understood readily. At high temperatures ($T>T_{\text{nd}}$), there exist only dynamic nano strain-domains in the system. When the temperature is lowered to $T<T_{\text{nd}}$, some dynamic nano strain-domains start to freeze and the system starts to lose ergodicity. When the temperature further decreases to $T<T_{g}$, the nanodomains are fully developed and completely frozen. The ergodicity of the system is completely broken and the system becomes a strain glass. The opposite dependence of $T_{\text{nd}}$ and $T_{g}$ on defect concentration in the strain-glass composition range can be attributed to the competition between the LFE and the GTTE. While the GTTE stabilizes the parent phase in our simulation (or Ti-Ni-Fe system [12]) and hence decreases $M_{s}$, $T_{g}$ and $T_{\text{nd}}$, the LFE promotes the formation or freezing of local strain ordering (i.e., nanodomains) but prevents the formation of long-range ordered martensitic twins.

In these 2D simulations, the real mole fraction of defect concentration $x$ (at. $\%$) can be calculated through the dimensionless concentration, $c$, through the relation, $x=ca_{0}^{2}/(l_{0}^{2})$ [16], where $l_{0}$ (0.94 nm) is the length scale and $a_{0}$ is the lattice parameter. Considering Ni-Ti system [1] where $a_{0}\sim 0.3$ nm for the B2 phase, the mole fraction $x$ is $\sim 0.1c$. Thus, one can see from Fig. 1(b) that the critical defect concentration $x_{c}$ is as low as $\sim 1.2\%$ in our simulation, being consistent with the experimental observations [12-14].

In summary, our model assumes that the role of point defects or dopants in a ferroelastic system is to create a randomly distributed local field that breaks the symmetry of the Landau potential, together with a change of the global stability of the martensite. Computer simulations based on this model reproduces all the experimentally observed strain states in defect-containing ferroelastic systems, including the abnormal strain states of precursory tweed and strain glass. Based on the results, a generic phase diagram that describes the relationships among different strain states was established and it shows excellent agreement with the one determined recently by experiment.

The authors thank Y. Wang at NIMS and N. Zhou and Y. Gao at OSU for useful discussions and acknowledge the support of National Natural Science Foundation of China (50720145101, 50771079), Scholarship Council (2008628062), National Basic Research Program (2010CB631003) and 111 Project of China (D. Wang); the U.S. National Science Foundation under grant DMR1008349 and NASA under grant NNX08AB49A (Y. Wang); and KAKENHI of Japan (X. Ren).

*Corresponding author.
†wang.363@osu.edu
‡REN.Xiaobing@nims.go.jp

[1] E. K. H. Salje *Phase Transitions in Ferroelastic and Coelastic Materials* (Cambridge University Press, Cambridge, England, 1990); K. Otsuka *et al.*, Prog. Mater. Sci. **50**, 511 (2005).
[2] S. M. Shapiro *et al.*, Phys. Rev. Lett. **57**, 3199 (1986).
[3] D. Shindo *et al.*, MRS Bull. **27**, 121 (2002).
[4] X. Ren *et al.*, Philos. Mag. **90**, 141 (2010).
[5] S. Sarkar, X. Ren, and K. Otsuka, Phys. Rev. Lett. **95**, 205702 (2005).
[6] Y. Wang *et al.*, Phys. Rev. B **76**, 132201 (2007).
[7] X. Ren *et al.*, MRS Bull. **34**, 838 (2009).
[8] Y. Wang, X. Ren, and K. Otsuka, Phys. Rev. Lett. **97**, 225703 (2006).
[9] G. A. Samara, J. Phys. Condens. Matter **15**, R367 (2003).
[10] J. A. Mydosh, *Spin Glasses* (Taylor & Francis, London, 1993).
[11] D. Sherrington *et al.*, Phys. Rev. Lett. **35**, 1792 (1975).
[12] D. Wang *et al.*, Acta Mater. **58**, 6206 (2010).
[13] Z. Zhang *et al.*, Phys. Rev. B **81**, 224102 (2010).
[14] Y. Zhou *et al.*, Acta Mater. **58**, 5433 (2010).
[15] S. Kartha *et al.*, Phys. Rev. Lett. **67**, 3630 (1991).
[16] S. Semenovskaya *et al.*, Acta Mater. **45**, 4367 (1997).
[17] P. Lloveras *et al.*, Phys. Rev. Lett. **100**, 165707 (2008).
[18] P. Lloveras *et al.*, Phys. Rev. B **80**, 054107 (2009).
[19] R. Vasseur and T. Lookman, Phys. Rev. B **81**, 094107 (2010).
[20] D. Sherrington, J. Phys. Condens. Matter **20**, 304213 (2008).
[21] Y. Wang *et al.*, Acta Mater. **45**, 759 (1997).
[22] N. Zhou *et al.*, Acta Mater. **55**, 5369 (2007).
[23] J. K. Allafi *et al.*, Smart Materials and Structures **14**, S192 (2005).
[24] A. P. Levanyuk and A. Sigov, *Defects and Structural Phase Transitions* (Gordon and Breach Science, New York, 1988).
[25] J. W. Cahn *et al.*, J. Chem. Phys. **28**, 258 (1958).
[26] A. G. Khachaturyan *et al.*, Sov. Phys. Solid State **11**, 118 (1969).
[27] A. G. Khachaturyan, *Theory of Structural Transformations in Solids* (John Wiley & Sons, New York, 1983).
[28] Y. Wang, Ph.D. thesis, dissertation, Xi'an Jiao Tong University, 2008.
[29] J. P. Sethna, *Statistical Mechanics: Entropy, Order Parameters, and Complexity* (Oxford University Press, New York, 2006).
205702-4