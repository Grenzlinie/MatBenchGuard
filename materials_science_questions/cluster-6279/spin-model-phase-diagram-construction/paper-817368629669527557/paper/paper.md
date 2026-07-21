**ORDER, DISORDER, AND PHASE TRANSITION**
**IN CONDENSED SYSTEM**

# Phase Transitions and Critical Properties of the Heisenberg Antiferromagnetic Model on a Body-Centered Cubic Lattice with Second Nearest Neighbor Interaction

A. K. Murtazaevⁱ, D. R. Kurbanovaⁱ,*, and M. K. Ramazanovⁱ

ⁱInstitute of Physics, Dagestan Scientific Center, Russian Academy of Sciences, Makhachkala, 367015 Russia
*e-mail: d_kurbanova1990@mail.ru

Received April 26, 2019; revised May 28, 2019; accepted May 28, 2019

Abstract—Phase transitions and critical properties of the antiferromagnetic Heisenberg model on a body-centered cubic lattice are investigated by the Monte Carlo method, based on the replica algorithm with allowance of the interactions between the first and second nearest neighbors. Analysis is performed for intensity ratios $r$ of exchange interaction between the first and second nearest neighbors in the interval $0.0 \leq r \leq 1.0$. The phase diagram of the dependence of the critical temperature on the intensity of interaction of the second nearest neighbors is constructed. On this diagram, a region in which the transition from the antiferromagnetic to the paramagnetic phase is of the first order is detected. The entire set of the main static critical indices is calculated. It is shown that the universality class of the critical behavior is preserved in the interval $0.0 \leq r \leq 0.6$. It is found that the variation of the second nearest neighbor interaction intensity in the range $0.8 \leq r \leq 1.0$ leads to nonuniversal critical behavior.

DOI: 10.1134/S1063776119090103

## 1. INTRODUCTION

Magnetic systems with competing antiferromagnetic exchange interactions of the first and second nearest neighbors have been central objects of intense investigations in the physics of condensed media for more than two decades [1–3]. The existence of competing exchange interactions in magnetic materials can lead to rich variety of magnetic ordered states and phase transitions (PTs) between them. In addition, peculiarities in PTs at different ratios of the intensity of exchange interactions between the first and second nearest neighbors have not been investigated comprehensively [4, 5].

At present, the 2D Heisenberg model has been studied quite well, and almost all its properties are known [6–12]. This model can be used for describing magnetic structures of actual materials. For example, for low intensities $J_2$ of interactions between second nearest neighbors, this model correctly describes the properties of a copper oxide monolayer in Cu-based high-temperature oxide superconductors [6, 7], and for high values of $J_2$, it successfully described the properties of antiferromagnetic materials $\text{Li}_2\text{VISi}_2\text{O}_4$ and $\text{Li}_2\text{VOGeO}_4$ [8, 9]. The 2D Heisenberg model is most effective in describing Fe–As monolayers in $\text{LaOFeAs}$ [10, 11] and $\text{BaFe}_2\text{As}_2$ [12] Fe-based superconductors.

In contrast to the 2D case, the 3D antiferromagnetic Heisenberg model on a body-centered cubic (bcc) lattice with competing interactions [13–21] has as of yet been studied insufficiently. The number of publications devoted to analysis of the phase diagram and thermodynamic properties of the quantum antiferromagnetic Heisenberg model on a bcc lattice is scarce [13–16, 20, 21]. For this model, interesting results have been obtained. However, analysis of the classical Heisenberg model on a bcc lattice with competing interactions of the first and second nearest neighbors has not been performed, to our knowledge.

The interest in this model is also induced by the fact that the inclusion of the interaction of second nearest neighbors may lead to frustrations, which complicates the solution [17–21]. It is well known that many physical properties of frustrated systems differ significantly from the properties of nonfrustrated systems.

For this reason, we investigate in this study the PTs and critical properties of the classical antiferromagnetic Heisenberg model on a bcc lattice based on the Monte Carlo method for various ratios on the intensities of exchange interactions of the first and second nearest neighbors.

The results obtained by now are insufficient for determining the order of a PT and regularities of changes in the critical behavior of this model unambiguously, and these aspects remain unclear. Analysis of the antiferromagnetic Heisenberg model on a bcc lattice with competing interactions of the first and sec-

![](./images/817368629669527557_1.jpg)

Fig. 1. (Color online) (a) bcc lattice. Numbers denote four sublattices; (b) ordered AF1 and AF2 phases.

ond nearest neighbors based on modern methods and ideas provides answers to a number of questions asso- ciated with PTs as well as thermodynamic and critical properties of frustrated spin systems.

### 2. MODEL AND ANALYSIS
The antiferromagnetic Heisenberg model on a bcc lattice with interactions of the first and second nearest neighbors is described by Hamiltonian [13]

$$
H=-J_{1} \sum_{\langle i, j\rangle}\left(\mathbf{S}_{i} \cdot \mathbf{S}_{j}\right)-J_{2} \sum_{\langle i, l\rangle}\left(\mathbf{S}_{i} \cdot \mathbf{S}_{l}\right), \tag{1}
$$

where $|\mathbf{S}_{i}|$ is the three-component unit vector $\mathbf{S}_{i}=(S_{i}^{x}$, $S_{i}^{y}, S_{i}^{z})$. The first term in formula (1) describes the exchange interaction of the first nearest neighbors $(J_{1}<0)$, while the second term takes into account the interaction of the second nearest neighbors $(J_{2}<0)$. It is known that in this model, for $J_{2}=0$, the ground state is characterized by conventional antiferromagnetic ordering. Nonzero exchange interaction $J_{2}$ may dis turb this order and lead to the emergence of frustra- tions. A high value of $J_{2}$ leads to the formation of stripe structures.

The results obtained using the mean field theory indicate the existence of two phases with different spin orderings [22]. A transition between the Néel phase (AF1) and the collinear phase (AF2) is determined by ratio $J_{2}/J_{1}$ of the interaction intensities. For a bcc lat- tice, antiferromagnetic phase AF1 can be described using the standard two-sublattice system (like in the case of 2D model), which is characterized by wavevec- tors $(\pm\pi, 0, 0)$, $(0, \pm\pi, 0)$, and $(0, 0, \pm\pi)$, while, for describing antiferromagnetic phase AF2 with wavevector $(\pm\pi/2, \pm\pi/2, \pm\pi/2)$, we must introduce four sublattices. This model is shown schematically in Fig. 1a.

The AF1 phase corresponds to the state in which each spin has eight nearest neighbors with antiparallel ordering, and its six second nearest neighbors have parallel ordering (Fig. 1b). The AF2 phase can be described as two mutually penetrating simple cubic lattices, each of which has the antiferromagnetic ordering (see Fig. 1b) [14-16, 23].

At present, the PTs of frustrated spin systems based on the microscopic Hamiltonian are successfully investigated by the Monte Carlo (MC) method [24-27]. The MC methods make it possible to analyze physical properties of spin systems of almost any com- plexity. These methods form the basis of investigation of the entire class of spin systems and for calculation of critical indices for a wide spectrum of models. Here, we are using the replica exchange algorithm of the MC method [28], which is the most powerful tool for studying frustrated spin systems. This algorithm was described in greater detail in our earlier publication [29].

Calculations were performed for systems with peri- odic boundary conditions and linear sizes $2\times L\times L\times L=N$, $L=24-90$, where $L$ is measured in unit cell sizes. Ratio $r=|J_{2}/J_{1}|$ of intensities of interactions between first and second neighbors varies in the inter- val $0.0\leq r\leq1.0$. To bring the system to thermodynamic equilibrium, we omitted the nonequilibrium segment of length $\tau_{0}=4\times10^{5}$ MC steps per spin, which is sev- eral times larger than the length of the nonequilibrium segment. Thermodynamic parameters were averaged along the Markov chain of length $\tau=500\tau_{0}$ MC steps per spin.

### 3. RESULTS OF SIMULATION
For analyzing the temperature behavior of the heat capacity and susceptibility, we used expressions [30, 31]

$$
C=\left(NK^{2}\right)\left(\langle U^{2}\rangle-\langle U\rangle^{2}\right), \tag{2}
$$

$$
\chi=
\begin{cases}
(NK)\left(\langle M^{2}\rangle-\langle|M|\rangle^{2}\right), & T<T_{\mathrm{N}}, \\
(NK)\langle M^{2}\rangle, & T\geq T_{\mathrm{N}},
\end{cases} \tag{3}
$$

where $K=|J_{1}|/k_{\mathrm{B}}T$, $N$ is the number of particles, $T_{\mathrm{N}}$ is the critical temperature (here and below, temperature is given in the units of $|J_{1}|/k_{\mathrm{B}}$), $U$ is the internal energy, and $M$ is the sublattice magnetization.

Figures 2 and 3 show temperature dependences of the heat capacity and susceptibility obtained for $L=48$ for various values of $r$ (here and below, the statistical error does not exceed the size of the symbols used for plotting these dependences). It can be seen from the figures that clearly manifested peaks are observed on the temperature dependences of heat capacity $C$ and susceptibility $\chi$ for all values of $r$ near the critical tem- perature. With increasing $r$, these peaks are displaced towards lower temperatures, and an increase in $r$ leads to an increase in the absolute values of the susceptibil- ity peaks, which is due to enhancement of fluctuations

![](./images/817368629669527557_2.jpg)

Fig. 2. (Color online) Dependences of heat capacity $C/k_\text{B}$ on temperature $k_\text{B}T/|J_1|$ for different $r$ and $L = 48$.

![](./images/817368629669527557_3.jpg)

Fig. 3. (Color online) Dependences of susceptibility $\chi$ on temperature $k_\text{B}T/|J_1|$ for different $r$ and $L = 48$.

because of stronger competition between the first and second nearest neighbors.

To determine critical temperature $T_\text{N}$, we used the method of fourth-order Binder cumulants $U_L$ [32]:

$$
V_L = 1 - \frac{\langle U^4 \rangle_L}{3\langle U^2 \rangle_L^2}, \tag{4}
$$

$$
U_L = 1 - \frac{\langle M^4 \rangle_L}{3\langle M^2 \rangle_L^2}, \tag{5}
$$

where $V_L$ is the energy cumulant and $U_L$ is the magnetization cumulants.

Expressions (4) and (5) make it possible to determine critical temperature $T_\text{N}$ to a high degree of accuracy. It should be noted that the application of Binder's cumulants also allow one to successfully determine the PT order in the system. It is well known that for a second-order PT, the curves describing the temperature dependence of Binder cumulants $U_L$ have a clearly manifested point of intersection [32].

Figure 4 shows a typical temperature dependence of $U_L$ for $r = 0.6$ for different values of $L$. The figure demonstrates the accuracy of determining the critical temperature. It can be seen that a clearly manifested point of intersection ($T_\text{N} = 0.871(1)$) is observed in the critical region, which indicates a second-order PT. Critical temperatures for the remaining values of $r$ were determined analogously.

For more detailed analysis of the PT order, the histogram analysis of this MC method was also used [33, 34]. This method helps to reliably determine the PT order. The determination of the PT order using this method was described in detail in our earlier publications [26, 27].

For the model investigated here, for $r = 1.0$, it was shown in [35] that a first-order PT is observed for systems with small linear sizes ($L < 48$). According to the results obtained in [36] for the Ising model on the bcc lattice with $r = 0.7$, a first-order PT is observed for systems with small linear sizes ($L \leq 60$). However, for systems with large linear sizes ($L > 60$), a second-order PT occurs. Therefore, in analysis of PTs based on the histogram method, it is expedient to use systems with large linear sizes ($L > 60$). In this study, we consider systems with $L \geq 80$ for obtaining reliable results in constructing the energy distribution histogram.

Figure 5 shows the energy distribution histograms for $r = 2/3$ with linear sizes $L = 90$. The curves are

![](./images/817368629669527557_4.jpg)

Fig. 4. (Color online) Dependences of Binder cumulants $U_L$ on temperature $k_\text{B}T/|J_1|$ for $r = 0.6$.

![](./images/817368629669527557_5.jpg)

Fig. 5. (Color online) Histogram of the energy distribution for $r=2/3$ and $L=90$.

![](./images/817368629669527557_6.jpg)

Fig. 6. (Color online) Histogram of the energy distribution for $r=0.7$ and $L=80$.

plotted for the critical temperature $(T_{\rm N}=0.670(1))$ and near it. It can be seen that a clearly manifested peak indicating a second-order PT is observed for all temperatures.

Figure 6 shows the energy distribution histograms for a system with linear sizes $L=80$ for $r=0.7$. It can be seen that near the PT temperature $(T_{N}=0.7643)$, a bimodal energy distribution is observed in the system. The existence of a two-hump peak in the dependence of probability $W$ on energy $E/N$ is a characteristic feature of a first-order PT.

This is confirmed by the results represented in Fig. 7 that shows the temporal dynamics of variation of internal energy during computer simulation for a system with linear sizes $L=80$ for $r=0.7$. The number of MC steps per spin (NMCS) is laid along the ordinate axis. The results are given for three temperatures: at the PT point $(T_{\rm N}=0.7643)$ as well as above and below the critical temperature $(T=0.7700$ and $0.7630)$. It can be seen that there are two metastable energy levels $E_{1}=-1.0151$ and $E_{2}=-0.9969$ at the PT point. The system performs random fluctuations about these two energy states. Energies $E_{1}$ and $E_{2}$ correspond to the first and second peaks, respectively, on the energy distribution histogram (see Fig. 6). Such a behavior of the temporal dynamic of the internal energy variation confirms the existence of a first-order PT. An analogous behavior is observed in interval $2/3 < r \leq 0.75$.

Figure 8 shows the phase diagram of the dependence of critical temperature $T_{N}$ on the intensity of interaction of the second nearest neighbors $(r)$. It can be seen that as we approach point $r=2/3$ at which three phases coexist, the PT temperature decreases. In the given model for $r=2/3$, the system has the minimal PT temperature $k_{\rm B}T/J_{1}=0.670(1)$. It can be seen from the diagram that at point $r=2/3$, three different phases (antiferromagnetic AF1, paramagnetic PM, and antiferromagnetic AF2) intersect [15–18]. A transition from the AF1 to the AF2 phase in the given model is due to the change in the structure of the ground state. According to the results obtained on the basis of the mean field theory [22], the value of $r=2/3$ for the Heisenberg model on the bcc lattice with interactions of the first and second nearest neighbors is the classical transition point at which a PT from the AF1 to the AF2 phase occurs.

Our results obtained in this study show that in intervals $0.0 \leq r \leq 0.6$ and $0.8 \leq r \leq 1.0$, a second-order PT is observed. It is found that in interval $2/3 < r \leq 0.75$ (red color in Fig. 8), a transition from the antiferromagnetic to the paramagnetic phase occurs as a first-order PT. A more detailed analysis shows that for $r=2/3$, a second-order PT is observed. The diagram obtained for this model is qualitatively identical to the diagram for the 3D Ising model on a bcc lattice [37–39].

For calculating static critical indices of heat capacity $(\alpha)$, susceptibility $(\gamma)$, order parameter $(\beta)$, correlation radius $(v)$, and Fisher index $(\eta)$, relations of the finite size scaling (FSS) theory were used [40].

It follows from the FSS theory that the following relations hold for a system of size $L \times L \times L$ at $T=T_{\rm N}$ [40–42]:

$$
M \propto L^{-\beta / v}, \tag{6}
$$

$$
\chi \propto L^{\gamma / v}, \tag{7}
$$

$$
V_{n} \propto L^{1 / v} g_{V_{n}}, \tag{8}
$$

where $g_{V_{n}}$ is a certain constant; the role of $V_{n}$ can be played by

![](./images/817368629669527557_7.jpg)

Fig. 7. (Color online) Temporal dynamics of internal energy variation for different temperatures for $r = 0.7$ and $L = 80$.

$$
V_{n}=\frac{\left\langle M^{n} U\right\rangle}{\left\langle M^{n}\right\rangle}-\langle U\rangle, \quad n=1,2,3. \tag{9}
$$

These expressions were used in this study for determining $\beta$, $\gamma$, and v.

For approximating the temperature dependence of heat capacity on $L$, the following expression is used in practice:
$$
C_{\max }(L)=A_{1}-A_{2} L^{\alpha / v}, \tag{10}
$$
where $A_1$ and $A_2$ are certain coefficients.

Figure 9 shows on the log–log scale the characteristic dependences of parameters $V_n$ for $n = 1$, 2, 3 on linear sizes $L$ of the lattice for $r = 0.2$. It can be seen that all points on the graph lie on the straight lines to within the error. The dependences on the figure plotted using the least square method are parallel straight lines. The slopes of the straight lines determine the values of $1/v$. The values of v calculated in this way were used for determining the critical indices of heat capacity ($\alpha$), susceptibility ($\gamma$), and order parameter ($\beta$).

Figures 10 and 11 show on the log–log scale the characteristic dependences of magnetic order parameter $M$ and susceptibility $\chi$ on linear lattice sizes $L$ for $r = 0.2$. All points lie on straight lines to within the error. The slopes of these straight lines determine the values of $\beta/v$ and $\gamma/v$. Using this scheme, we determined the values for heat capacity $\alpha/v$ also. Static critical indices $\alpha$, $\beta$, and $\gamma$ were calculated with the help of data on v.

This procedure was used for calculating critical indices for values of $r = 1.0$, 0.9, 0.8, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1, and 0. All values of static critical indices obtained in this study are given in Table 1.

The procedure used in this study for determining Fisher index $\eta$ is worth special attention. Based on the relations between susceptibility $\chi$ and correlation radius $\xi$ [43]
$$
\chi \propto \xi^{\gamma / v}, \tag{11}
$$

![](./images/817368629669527557_8.jpg)

Fig. 8. (Color online) Phase diagram of the dependence of critical temperature on the intensity of interaction of the second nearest neighbors.

![](./images/817368629669527557_9.jpg)

Fig. 9. (Color online) Dependences of parameter $V_n$ on linear sizes $L$ of the system at $T=T_{\text{N}}$ for $r=0.2$.

as well as relation $\eta=2-\gamma/v$ connecting indices $\eta$ and v, we obtain

$$
\ln(\chi/\xi^{2})=c-\eta\ln\xi,\tag{12}
$$

where $c$ is a certain constant. For systems with finite sizes $(\xi=L)$ for $k_{\text{B}}T/|J_{1}|=k_{\text{B}}T_{\text{N}}/|J_{1}|$, we obtain

$$
\ln(\chi/L^{2})=c-\eta\ln L.\tag{13}
$$

Using this expression, we determined the value of Fisher index $\eta$. These results are also given in Table 1.

As follows from Table 1, almost all values of critical indices calculated here in interval $0.01\leq r\leq0.6$ coincide to within the error. This means that the system exhibits the universal critical behavior in this interval. It should be noted that the critical indices obtained in this study coincide to within the error with the corresponding values of critical indices for the nonfrustrated 3D Heisenberg model [44]. This is confirmed by the fact that in interval $0.0\leq r\leq0.6$, the model under investigation belongs to the same universality class of the critical behavior as the 3D Heisenberg model on a cubic lattice.

In interval $0.8\leq r\leq1.0$, the values of critical indices differ from the corresponding values from interval $0.0\leq r\leq0.6$. We can assume that upon an increase in the intensity of interaction of the second nearest neighbors, the class of universality of the critical behavior in the system changes. In addition, the indices in interval $0.8\leq r\leq1.0$ change with $r$. This suggests that a nonuniversal critical behavior is observed in this interval.

The results of this study can be used for describing specific antiferromagnetic materials (such as FeCr, FeAl, FeCo, etc.) with the bcc lattice.

![](./images/817368629669527557_10.jpg)

Fig. 10. (Color online) Dependence of order parameter $M$ on linear sizes $L$ of the system at $T=T_{\text{N}}$ for $r=0.2$.

## 4. CONCLUSIONS

Analysis of phase transitions and critical properties of the antiferromagnetic Heisenberg model on a body-centered cubic lattice with the interaction of the first and second nearest neighbors has been performed using the high-efficiency replica Monte Carlo algorithm. Based on the histogram method and the Binder cumulants method, the type of phase transitions has been analyzed for various values of interaction intensity of the second nearest neighbors. The phase diagram of the dependence of the critical temperature on the intensity of interaction of the second nearest method has been constructed. It is found that in interval $2/3<r\leq0.75$, the transition from the antiferro-

![](./images/817368629669527557_11.jpg)

Fig. 11. (Color online) Dependence of susceptibility $\chi$ on linear sizes $L$ of the system at $T=T_{\text{N}}$ for $r=0.2$.

<table>
<caption>Table 1. Values of critical indices for the 3D antiferromagnetic Heisenberg model on a body-centered cubic lattice</caption>
<thead>
<tr>
<th>$r$</th>
<th>$T_\mathrm{N}$</th>
<th>$v$</th>
<th>$\alpha$</th>
<th>$\beta$</th>
<th>$\gamma$</th>
<th>$\eta$</th>
<th>$\alpha + 2\beta + \gamma = 2$</th>
</tr>
</thead>
<tbody>
<tr>
<td>0.0</td>
<td>2.056(1)</td>
<td>0.70(1)</td>
<td>$-0.13(1)$</td>
<td>0.37(1)</td>
<td>1.39(1)</td>
<td>0.02(1)</td>
<td>2.0</td>
</tr>
<tr>
<td>0.1</td>
<td>1.873(1)</td>
<td>0.70(1)</td>
<td>$-0.12(1)$</td>
<td>0.36(1)</td>
<td>1.38(1)</td>
<td>0.03(1)</td>
<td>1.98</td>
</tr>
<tr>
<td>0.2</td>
<td>1.687(1)</td>
<td>0.70(1)</td>
<td>$-0.13(1)$</td>
<td>0.37(1)</td>
<td>1.39(1)</td>
<td>0.02(1)</td>
<td>2.0</td>
</tr>
<tr>
<td>0.3</td>
<td>1.494(1)</td>
<td>0.70(1)</td>
<td>$-0.12(1)$</td>
<td>0.36(1)</td>
<td>1.39(1)</td>
<td>0.02(1)</td>
<td>1.99</td>
</tr>
<tr>
<td>0.4</td>
<td>1.301(1)</td>
<td>0.70(1)</td>
<td>$-0.12(1)$</td>
<td>0.36(1)</td>
<td>1.38(1)</td>
<td>0.03(1)</td>
<td>1.98</td>
</tr>
<tr>
<td>0.5</td>
<td>1.094(1)</td>
<td>0.70(1)</td>
<td>$-0.12(1)$</td>
<td>0.37(1)</td>
<td>1.39(1)</td>
<td>0.02(1)</td>
<td>2.01</td>
</tr>
<tr>
<td>0.6</td>
<td>0.871(1)</td>
<td>0.71(1)</td>
<td>$-0.13(1)$</td>
<td>0.37(1)</td>
<td>1.38(1)</td>
<td>0.03(1)</td>
<td>1.99</td>
</tr>
<tr>
<td>0.8</td>
<td>0.975(1)</td>
<td>0.60(1)</td>
<td>0.21(4)</td>
<td>0.29(4)</td>
<td>1.24(4)</td>
<td>0.01(4)</td>
<td>2.03</td>
</tr>
<tr>
<td>0.9</td>
<td>1.152(1)</td>
<td>0.61(1)</td>
<td>0.18(2)</td>
<td>0.30(1)</td>
<td>1.22(2)</td>
<td>0.02(2)</td>
<td>2.0</td>
</tr>
<tr>
<td>1.0</td>
<td>1.316(1)</td>
<td>0.60(1)</td>
<td>0.17(2)</td>
<td>0.30(1)</td>
<td>1.21(2)</td>
<td>0.02(2)</td>
<td>1.98</td>
</tr>
<tr>
<td>Nonfrustrated</td>
<td>$-$</td>
<td>0.7112(5)</td>
<td>$-0.1336(15)$</td>
<td>0.3689(3)</td>
<td>1.3960(9)</td>
<td>0.0375(5)</td>
<td>$-$</td>
</tr>
<tr>
<td>Heisenberg model [44]</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

magnetic to paramagnetic phase in the given model occurs as a first-order transition.

We have calculated the values of all main static critical indices in intervals $0.0 \leq r \leq 0.6$ and $0.8 \leq r \leq 1.0$. It is shown that in the $0.0 \leq r \leq 0.6$ interval, the model exhibits the universal critical behavior and belongs to the same universality class as the 3D Heisenberg model. It is found that a change in the intensity of interaction of the second nearest neighbors in interval $0.8 \leq r \leq 1.0$ leads to a nonuniversal critical behavior.

## FUNDING
This study was supported by the Russian Foundation for Basic Research (project nos. 18-32-00391 mol-a, 19-02-00153 a, and 18-32-20098 mol-a-ved).

## REFERENCES
1. Introduction to Frustrated Magnetism: Materials, Experiments, Theory, Vol. 164 of Series in Solid-State Science, Ed. by C. Lacroix, P. Mendels, and F. Mila (Springer, Berlin, 2011).

2. S. Sachdev, *Quantum Phase Transitions*, 1st ed. (Cambridge Univ. Press, Cambridge, 2001).

3. H. T. Diep, *Frustrated Spin Systems* (World Scientific, Singapore, 2004).

4. D. P. Landau and K. Binder, *Monte Carlo Simulations in Statistical Physics* (Cambridge Univ. Press, Cambridge, 2000).

5. F. A. Kassan-Ogly, B. N. Filippov, A. K. Murtazaev, M. K. Ramazanov, and M. K. Badiev, J. Magn. Magn. Mater. **324**, 3418 (2012).

6. E. Dagotto and A. Moreo, Phys. Rev. Lett. **63**, 2148 (1989).

7. E. Manousakis, Rev. Mod. Phys. **63**, 1 (1991).

8. H. Rosner, R. R. P. Singh, W. H. Zheng, J. Oitmaa, and W. E. Pickett, Phys. Rev. B **67**, 014416 (2003).

9. J. Sirker, Zh. Weihong, O. P. Sushkov, and J. Oitmaa, Phys. Rev. B **73**, 184420 (2006).

10. Y. Kamihara, T. Watanabe, M. Hirano, and H. Hosono, J. Am. Chem. Soc. **130**, 3296 (2008).

11. H. H. Wen, G. Mu, L. Fang, H. Yang, and X. Zhu, Europhys. Lett. **82**, 17009 (2008).

12. M. Rotter, M. Tegel, and D. Johrendt, Phys. Rev. Lett. **101**, 107006 (2008).

13. R. Schmidt, J. Schulenburg, J. Richter, and D. D. Betts, Phys. Rev. B **66**, 224406 (2002).

14. J. Oitmaa and W. Zheng, Phys. Rev. B **69**, 064416 (2004).

15. K. Majumdar and T. Datta, J. Phys.: Condens. Matter **21**, 406004 (2009).

16. M. R. Pantic, D. V. Kapor, S. M. Radosevic, and P. M. Mali, Solid State Commun. **182**, 55 (2014).

17. J. Richter, P. Müller, A. Lohmann, and H.-J. Schmidt, Phys. Proc. **75**, 813 (2015).

18. P. Müller, J. Richter, A. Hauser, and D. Ihle, Eur. Phys. J. B **88**, 159 (2015).

19. D. J. J. Farnell, O. Götze, and J. Richter, Phys. Rev. B **93**, 235123 (2016).

20. Bin-Zhou Mi, Solid State Commun. **239**, 20 (2016).

21. Bin-Zhou Mi, Solid State Commun. **251**, 79 (2017).

22. J. S. Smart, *Effective Field Theories of Magnetism* (Saunders, Philadelphia, 1966).

23. J. R. Banavar, D. Jasnow, and D. P. Landau, Phys. Rev. B **20**, 3820 (1979).

24. H. Kawamura, J. Phys. Soc. Jpn. **61**, 1299 (1992).

25. A. Mailhot, M. L. Plumer, and A. Caille, Phys. Rev. B **50**, 6854 (1994).

26. M. K. Ramazanov and A. K. Murtazaev, JETP Lett. **103**, 460 (2016).

27. M. K. Ramazanov and A. K. Murtazaev, JETP Lett. **106**, 86 (2017).

28. A. Mitsutake, Y. Sugita, and Y. Okamoto, Biopolymers (Peptide Sci.) **60**, 96 (2001).

29. A. K. Murtazaev, M. K. Ramazanov, and M. K. Badiev, Phys. A (Amsterdam, Neth.) **507**, 210 (2018).

30. K. Binder and J.-Sh. Wang, J. Stat. Phys. **55**, 87 (1989).

31. P. Peczak, A. M. Ferrenberg, and D. P. Landau, Phys. Rev. B **43**, 6087 (1991).

32. K. Binder and D. W. Heermann, *Monte Carlo Simulation in Statistical Physics* (Springer, Berlin, 1988).

33. F. Wang and D. P. Landau, Phys. Rev. E **64**, 056101 (2001).

34. F. Wang and D. P. Landau, Phys. Rev. Lett. **86**, 2050 (2001).

35. A. K. Murtazaev, M. K. Ramazanov, D. R. Kurbanova, and M. K. Badiev, Phys. Solid State **60**, 1173 (2018).

36. A. K. Murtazaev, M. K. Ramazanov, D. R. Kurbanova, M. K. Badiev, and Ya. K. Abuev, Phys. Solid State **59**, 1103 (2017).

37. A. K. Murtazaev, M. K. Ramazanov, F. A. Kassan-Ogly, and D. R. Kurbanova, J. Exp. Theor. Phys. **120**, 110 (2015).

38. A. K. Murtazaev, M. A. Magomedov, and M. K. Ramazanov, JETP Lett. **107**, 259 (2018).

39. A. K. Murtazaev, M. K. Ramazanov, D. R. Kurbanova, M. A. Magomedov, and K. Sh. Murtazaev, Mater. Lett. **236**, 669 (2019).

40. A. Mailhot, M. L. Plumer, and A. Caille, Phys. Rev. B **50**, 6854 (1994).

41. P. Peczak, A. M. Ferrenberg, and D. P. Landau, Phys. Rev. B **43**, 6087 (1991).

42. A. K. Murtazaev, M. K. Ramazanov, and M. K. Badiev, Phys. B (Amsterdam, Neth.) 476, 1 (2015).

43. Ch. Holm and W. Janke, Phys. Rev. B **48**, 936 (1993).

44. M. Campostrini, M. Hasenbusch, A. Pelissetto, P. Rossi, and E. Vicari, Phys. Rev. B **65**, 144520 (2002).

Translated by N. Wadhwa

JOURNAL OF EXPERIMENTAL AND THEORETICAL PHYSICS Vol. 129 No. 5 2019