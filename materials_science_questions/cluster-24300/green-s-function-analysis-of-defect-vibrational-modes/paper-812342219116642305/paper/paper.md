# A Reconstruction Procedure for Microwave Nondestructive Evaluation Based on a Numerically Computed Green's Function

Salvatore Caorsi, Member, IEEE, Andrea Massa, Matteo Pastorino, Senior Member, IEEE, Andrea Randazzo, and Andrea Rosani

**Abstract**—This paper describes a new microwave diagnostic tool for nondestructive evaluation. The approach, developed in the spatial domain, is based on the numerical computation of the inhomogeneous Green's function in order to fully exploit all the available *a priori* information of the domain under test. The heavy reduction of the computational complexity of the proposed procedure (with respect to standard procedures based on the free-space Green's function) is also achieved by means of a customized hybrid-coded genetic algorithm. In order to assess the effectiveness of the method, the results of several simulations are presented and discussed.

**Index Terms**—Genetic algorithms, Green's function, imaging processing, imaging systems, material characterization.

## I. INTRODUCTION
N MANY tomographic approaches, in which electromagnetic waves are used to inspect dielectrics, the inversion procedures are developed in the spatial domain (as opposed to spectral domain). In practical applications, the main interest is usually represented by the inspection of inhomogeneous scatterers of arbitrary (bounded) cross sections (e.g., in microwave nondestructive testing and evaluation (NDT/NDE) [1]–[7]). In very few cases, the objects under test are weak enough to allow the practical use of simplified [8], [9] or closed-form solutions [10].

Recently, the development of reconstruction procedures for microwave tomography has been addressed by resorting to the numerical discretization of the integral equations of the inverse scattering problem. The Fredholm equation of the first kind (i.e., the data equation governing the relation among the scattering potential, the total electric field inside the body, and the scattered electric field at the receivers) results, as it is well known, in a highly nonlinear and ill-posed inverse problem. The discretized version of this equation is affected by a severe ill conditioning. The problem's solution is generally addressed by associating to the data equation the so-called *state equation*, i.e., the equation relating the incident and total fields inside the scatterer. A suitable functional is constructed (often arbitrarily), whose minimization corresponds to the attempt of fulfilling as much as possible the state and data equations. To this end, the authors in [11]–[13] proposed the application of global optimization approaches, and in particular, the use of a hybrid-coded genetic algorithm (GA) [11]. Due to its flexibility, a GA is able to deal with integer as well as real variables at the same time and does not require either differentiability or continuity of the cost function to be minimized. However, as it is well known, the main drawback of such very appealing methods (simple to be implemented, robust, and insensitive to details of the cost function) is the high computational load. Although the continuous increase in the computational power of new computers tends to alleviate this problem, a pixel representation of the cross section of an unknown complex object is still a difficult task.

However, the GA presents other advantages over several deterministic techniques. It allows the simple and straightforward insertion of *a priori* information into the model. The exploitation of *a priori* information is very important in practical applications, allowing a reduction of the search space sampled by the optimization procedure and, consequently, an increase of the convergence rate of the iterative process.

An example is represented by the NDE problem considered in the present paper. In this case, the object to be detected is only a defect in an otherwise known object. Consequently, the inverse scattering problem is notably simplified, and the use of a GA for the retrieval of some characteristic parameters of the defect (position, dimensions, orientation, etc.) is convenient. In this framework, the main novelty of the proposed approach lies in the use of the Green's function for the unperturbed geometry, which can be numerically computed offline and once for all. As a result, only the space region occupied by the defect is the "investigation area" considered during the minimization process, and the chromosomes of the GA (coding the problem unknowns) become greatly shortened, allowing a significant reduction of the computational burden.

The paper is organized as follows: In Section II, the mathematical formulation of the proposed approach is presented. Section III gives a description of the optimization procedure based on a customized genetic algorithm, pointing out the key points of its application to the NDE framework. Finally, in Section IV, selected numerical results, concerning both noiseless and noisy environments as well as lossy and lossless investigation domains, are reported in order to show the capabilities and current limitations of the method in providing accurate defect localizations and reconstructions.

Manuscript received June 15, 2003; revised April 2, 2004.
S. Caorsi is with the Department of Electronics, University of Pavia, Pavia I-27100, Italy (e-mail: caorsi@ele.unipv.it).
A. Massa and A. Rosani are with the Department of Information and Communication Technologies (DIT), University of Trento, Trento I-38050, Italy (e-mail: andrea.massa@ing.unitn.it).
M. Pastorino and A. Randazzo are with the Department of Biophysical and Electronic Engineering (DIBE), University of Genoa, Genova I-16145, Italy (e-mail: pastorino@dibe.unige.it).
Digital Object Identifier 10.1109/TIM.2004.831446

![](./images/812342219116642305_1.jpg)

Fig. 1. Computed inhomogeneous Green's function for a point source located at the center of the host medium characterized by (a) $\sigma_I = 0.0, \varepsilon_I = 1.0$ (free-space Green's function); (b) $\sigma_I = 0.0, \varepsilon_I = 2.0$; (c) $\sigma_I = 0.25$ S/m, $\varepsilon_I = 2.0$; and (d) $\sigma_I = 0.50$ S/m, $\varepsilon_I = 2.0$.

## II. MATHEMATICAL FORMULATION

Let us consider an investigation area $S$ modeled by a scattering potential $\gamma$, given by

$$
\gamma(\mathbf{r})=\left(j \omega \mu_{0}\right)^{-1}\left\{\left[\sigma(\mathbf{r})-\sigma_{e}\right]+j \omega \varepsilon_{e}[\varepsilon(\mathbf{r})-1]\right\} \quad(1)
$$

where $(\sigma, \varepsilon)$ and $(\sigma_{e}, \varepsilon_{e})$ are the conductivities and relative dielectric permittivities inside and outside $S$, respectively. The region $S$ is illuminated by a set of transverse-magnetic (TM) incident fields $\mathbf{E}_{i}^{\text{inc}}(\mathbf{r}), i=1, \ldots, I$. The scattered data are collected in $M$ measurement points (arranged around the object under test) $\mathbf{E}_{i,j}^{\text{scat}}(\mathbf{r}_{j}), i=1, \ldots, I, j=1, \ldots, M$. The inverse problem can be recast as an optimization problem, where a functional is to be minimized [11], as follows:

$$
\begin{aligned}
\Im\left\{\gamma(\mathbf{r}), E_{i}^{\text{tot}}(\mathbf{r})\right\}=\Im_{\text{Data}}\left\{\gamma(\mathbf{r}), E_{i}^{\text{tot}}(\mathbf{r})\right\} & \\
+\Im_{\text{State}}\left\{\gamma(\mathbf{r}), E_{i}^{\text{tot}}(\mathbf{r})\right\} & \quad(2)
\end{aligned}
$$

being

$$
\Im_{\text{Data}}\left\{\gamma(\mathbf{r}), E_{i}^{\text{tot}}(\mathbf{r})\right\}=\frac{\left\|\mathcal{L}_{2}\left\{\gamma(\mathbf{r}), \mathbf{E}_{i}^{\text{tot}}(\mathbf{r})\right\}-\mathbf{E}_{i,j}^{\text{scat}}\left(\mathbf{r}_{j}\right)\right\|^{2}}{\left\|\mathbf{E}_{i,j}^{\text{scat}}\left(\mathbf{r}_{j}\right)\right\|^{2}}
$$

and

$$
\Im_{\text{State}}\left\{\gamma(\mathbf{r}), E_{i}^{\text{tot}}(\mathbf{r})\right\}=\frac{\left\|\mathcal{L}_{1}\left\{\gamma(\mathbf{r}), \mathbf{E}_{i}^{\text{tot}}(\mathbf{r})\right\}+\mathbf{E}_{i}^{\text{inc}}(\mathbf{r})\right\|^{2}}{\left\|\mathbf{E}_{i}^{\text{inc}}(\mathbf{r})\right\|^{2}}
$$

where $\mathcal{L}_{1}\left\{\gamma(\mathbf{r}), \mathbf{E}_{i}^{\text{tot}}(\mathbf{r})\right\}$ and $\mathcal{L}_{2}\left\{\gamma(\mathbf{r}), \mathbf{E}_{i}^{\text{tot}}(\mathbf{r})\right\}$ are nonlinear operators whose unknown functions are $\gamma=\gamma\{\varepsilon(\mathbf{r}), \sigma(\mathbf{r})\}$ (which, in NDE applications, contains the information on the unknown defect) and $\mathbf{E}_{i}^{\text{tot}}(\mathbf{r}), i=1, \ldots, I$. These operators are defined in details in [11]-[13] for the case in which the kernel is the free space Green's function [14]. In this paper, a numerically computed Green's function for the unperturbed configuration (the configuration without the defect) is considered. The Green's function satisfies the following equation:

$$
\Gamma\left(\frac{\mathbf{r}}{\mathbf{r}^{\prime}}\right)=\Gamma_{0}\left(\frac{\mathbf{r}}{\mathbf{r}^{\prime}}\right)+\iint_{S} \gamma_{I}(\mathbf{x}) \Gamma\left(\frac{\mathbf{x}}{\mathbf{r}^{\prime}}\right) \Gamma_{0}\left(\frac{\mathbf{r}}{\mathbf{x}}\right) d \mathbf{x} \quad(3)
$$

where $\Gamma(\mathbf{r}/\mathbf{r}')$ is the inhomogeneous Green's function, $\Gamma_{0}(\mathbf{r}/\mathbf{r}')$ is the free-space Green's function, and $\gamma_I(\mathbf{r})=(j\omega\mu_0)^{-1}\{[\sigma_I(\mathbf{r})-\sigma_e]+j\omega\varepsilon_e[\varepsilon_I(\mathbf{r})-1]\}$ is the scattering potential of the unperturbed geometry. Equation (3) can be solved offline and once for all by means of the moment method. As an example of these computations, Fig. 1 shows the amplitudes of the inhomogeneous Green's function for a point source located at the center of the investigation domain and in correspondence with different host medium configurations [two-dimensional (2-D) case].

After discretization of the continuous model, $\Im\{\gamma(\mathbf{r}), \mathbf{E}_{i}^{\text{tot}}(\mathbf{r})\}$ (2) is minimized by means of a suitable GA-based procedure [15] able to efficiently exploit the features of the proposed approach.

![](./images/812342219116642305_2.jpg)

Fig. 2. Reconstruction of a void crack in a lossy host medium $(\sigma_I = 0.25$ S/m, $\varepsilon_I = 2.0)$. SNR = 25 dB.

## III. GA-BASED PROCEDURE

Due to the numerical knowledge of the Green's function for the unperturbed scenario, let us model the defect by means of a differential scattering potential $\tilde{\gamma}$, defined as $\tilde{\gamma}(\mathbf{r})=\gamma(\mathbf{r})-\gamma_{I}(\mathbf{r})$, which completely describes the dielectric profile of the investigation domain and whose support is limited to the crack area (on the contrary, in [11], the whole dielectric configuration of the investigation domain is unknown). Then, by defining a suitable parameterization of the defect shape, the set of unknown crack parameters can be suitably represented by means of a small subset of discrete variables $\tilde{\gamma}(\mathbf{r}) \Rightarrow(\ell_{j}, j=1, \ldots, J)$, being $\ell_{j}$ the $j$ th defect discrete descriptor. Consequently, the arising unknown array results in a variable-length hybrid-encoded "individual" obtained by concatenating the code of discrete and real-valued parameters [11], as follows:

$$
\left\{\tilde{\gamma}(\mathbf{r}), \mathbf{E}_{i}^{\mathrm{tot}}(\mathbf{r})\right\} \Rightarrow\left\{\ell_{j}, j=1, \ldots, J ; \mathbf{E}_{i}^{\mathrm{tot}}(\mathbf{r})\right\}. \quad (4)
$$

In order to obey the mathematical properties of the array unknown representation (relation (4)), suitable GA operators are considered. Binary tournament selection [16] and real/bi- nary double-point crossover [15], [17] are used for the selection and the crossover, respectively. The mutation is performed with probability $P_{m}$ on an individual and consists in perturbing one element of its genetic sequence. If the element is a discrete variable, it is changed randomly in a limited set of values. Otherwise, the mutation rule proposed in [11] is adopted. In particular, for the simulations performed in this paper, we assumed a population of $P=20$ individuals, a threshold value for the convergence of functional (2) given by $\Im_{\mathrm{th}}=10^{-5}$, and a maximum number of iterations equal to 200 (the iterative process is stopped when $\Im \leq \Im$ th or when the maximum number of iterations has been reached). Finally, the probability $P_{m}$ is assumed to be equal to 0.4.

## IV. NUMERICAL VALIDATION

In order to assess the effectiveness of the proposed approach (in the following indicated by IGA), pointing out its efficiency by a computational point of view, some numerical simulations have been performed. In this section, selected numerical results are presented in order to demonstrate the following two main features of the approach:

1) the accuracy in the crack detection and estimation
2) the reduction of the computational load with respect to the use of the method (namely, the FGA) presented in [11].

As far as the test case is concerned, a 2-D scenario is taken into account where a void crack lies in a square (side: $0.8 \lambda_{0}$ ) homogeneous host medium. Fig. 2 shows the reconstruction of a square crack $0.2 \lambda_{0}$ sided inside a lossy host medium $(\sigma_{I}=$ 0.25 S/m, $\varepsilon_I=2.0$) during the iterative reconstruction process (SNR = 25 dB). It can be observed that the location of the center of the defect is accurate in both cases (IGA and FGA). As far as the area estimation is concerned, slight differences in the final reconstruction, i.e., at the convergence iteration $k$ (iteration number) $=K^{*}$, occur. In particular, we obtained $K_{\mathrm{FGA}}^{*}=200$ and $K_{\mathrm{IGA}}^{*}=106$. For completeness, Fig. 2(a) and (e) show the original and the best initial trial configurations, respectively.

The imaging capabilities of the two approaches are rather different for higher values of the conductivity of the host medium. Fig. 3 shows the images of the reconstructed distributions at different iterations in the case in which $\varepsilon_I=2.0$, $\sigma_I=0.5$ S/m, and SNR = 25 dB. The position of the defect is accurately estimated, and its area slightly underestimated when the IGA is used [Fig. 3(l)]. On the contrary, the final result reached by

![](./images/812342219116642305_3.jpg)

Fig. 3. Reconstruction of a void crack in a lossy host medium ($\sigma_I = 0.25$ S/m, $\varepsilon_I = 2.0$). SNR = 25 dB. The original geometry is the one reported in Fig. 2(a).

the FGA [Fig. 3(e)] is very poor for the location as well as for the shape reconstruction, even after a large number of iterations ($K^*_{\text{FGA}} = 200$ and $K^*_{\text{IGA}} = 165$). Consequently, it can be preliminarily inferred that the IGA procedure produces better results than the FGA approach (it should be noted that, although the threshold value is reached for $K^*_{\text{IGA}} = 165$, a quite accurate location is obtained even with a reduced number of iterations, e.g., for $k = 60$). This statement is clearly confirmed and generalized by the results obtained by performing an exhaustive set of numerical simulations varying the environment conditions (the values of the SNR in the range between 2.5 and 50 dB) and the dielectric characteristics of the host medium (in particular, its conductivity between 0.1 and 1.0 S/m). Due to the stochastic nature of the optimization algorithm, a set of ten simulations has been carried out for each scenario under test. The initial trial population is randomly chosen so that the final average result is independent from the starting configuration. It should be noted that ten simulations are not sufficient to provide the complete statistics of the stochastic procedure. However, they have been found to represent an acceptable compromise between the need for accurately assessing the reconstruction process and the required computational saving.

Moreover, in order to quantitatively evaluate the effectiveness of the IGA method in comparison with the FGA approach, the following two error figures have been defined:

$$
\delta_{c}=\frac{\sqrt{(x-\hat{x})^{2}-(y-\hat{y})^{2}}}{d_{\max }} \times 100
\tag{5}
$$

$$
\delta_{a}=\left| \frac{A-\hat{A}}{A} \right| \times 100
\tag{6}
$$

where $(x, y)$ and $(\hat{x}, \hat{y})$ are actual and estimated coordinates of the center of the crack, respectively; $d_{\text{max}}$ is the maximum error in defining the crack center; and $A$ and $\hat{A}$ are the actual and estimated crack areas, respectively. In particular, $\hat{A}$ is given by $\hat{A} = wl$, where $w$ and $l$ are the linear dimensions of the searched (rectangular) defect. Consequently, the unknown parameters (4) are represented by $w, l, \hat{x}, \hat{y}$, and the orientation angle with respect to the horizontal axis.

Fig. 4 shows a three-dimensional color-level representation of $\delta_c$ and $\delta_a$. As preliminarily drawn from Figs. 2 and 3, the IGA approach generally outperforms the FGA method, especially in the estimation of the crack area and in correspondence with a more realistic industrial environment (where small values of the SNR generally arise). In particular, it can be observed that $\{\delta_a\}_{\text{IGA}} \leq 50$ when in general $\{\delta_a\}_{\text{FGA}} > 50$. However, as expected, the errors are far less for small values of the electric conductivity of the host medium.

Finally, in order to quantify the computational effectiveness of the proposed approach, the following parameter is evaluated:

$$
\Delta_{\text{conv}} = \frac{K^*_{\text{FGA}} - K^*_{\text{IGA}}}{K^*_{\text{FGA}}} \times 100
\tag{7}
$$

and the obtained results are reported in Fig. 5. The plot clearly indicates that the convergence rate of the IGA is generally greater than that of the FGA. As expected, the differences increase in correspondence with lower SNR values and for lossy host regions. Moreover, in the case in which there is a difference in the assumed property and the actual one, the errors can be significantly larger. As an example, in the case in which $\varepsilon_{\text{actual}} = \varepsilon_I + \Delta\varepsilon$, $\sigma_{\text{actual}} = \sigma_I$, with $\varepsilon_I = 2.0$ and $\sigma_I = 0.25$ S/m, the following results have been obtained (SNR = 15 dB): $\{\delta_c\}_{\text{IGA}} = 1.07\%$ for $\Delta\varepsilon = 0$ (exact estimation of the actual property), $\{\delta_c\}_{\text{IGA}} = 1.18\%$ for $\Delta\varepsilon = 0.4$ (+20% error), and $\{\delta_c\}_{\text{IGA}} = 2.20\%$ for $\Delta_{\varepsilon} = 0.6$ (+30% error).

![](./images/812342219116642305_4.jpg)

Fig. 4. Errors in the crack reconstruction for different SNR values and for different conductivities of the host medium ($\sigma_{I}$): (a) $\delta_{c}(\text{FGA})$, (b) $\delta_{c}(\text{IGA})$, (c) $\delta_{a}(\text{FGA})$, and (d) $\delta_{a}(\text{IGA})$.

![](./images/812342219116642305_5.jpg)

Fig. 5. Reconstruction of a void crack in a lossy host medium (noisy environment)—converge rate estimation.

For completeness, in order to give an idea of the time saving allowed by the IGA method, Table I gives the statistics of the time required for each iteration of the optimization procedure (the total CPU time can be approximately obtained by multiplying by $K^{*}$). For comparison purposes, the values for the FGA approach are reported, as well. These results represent the average values obtained in the previous simulations, which have been performed by using a PC Pentium III 733 MHz with 128 MB RAM. As can be observed, it results that, on an average, an iteration of the IGA took approximately two fifths of the time necessary for the FGA iterative step.

<table>
<caption>TABLE I<br>Statistics of the CPU Time Required for Each Iteration of the Minimization Procedure</caption>
<tr>
<td></td>
<td>FGA</td>
<td>IGA</td>
</tr>
<tr>
<td>Minimum Value [sec]</td>
<td>2.00</td>
<td>0.40</td>
</tr>
<tr>
<td>Average Value [sec]</td>
<td>3.36</td>
<td>1.35</td>
</tr>
<tr>
<td>Maximum Value [sec]</td>
<td>3.88</td>
<td>1.70</td>
</tr>
</table>

### V. CONCLUSION AND FUTURE DEVELOPMENTS

An innovative approach for crack detection in a known host medium has been presented. In order to fully exploit the knowledge of the scenario under test, a new formulation based on the numerical computation of the Green's function for the unperturbed configuration has been proposed. Moreover, the new formulation requires the definition of a customized minimization procedure based on a genetic algorithm, which results in heavy computational saving. This fact, confirmed by several numerical simulations, clearly indicates a possibility for the quasi-real-time implementation of the proposed technique in real-world monitoring of industrial processes. To this end, further improvements and generalizations are mandatory. Let us consider the extension to more general crack shapes (and, consequently, the need for more complete and complicated crack parameterizations), the possibility of dealing with multiple defects in the same host medium, or (in some specific industrial

applications) the increase of the resolution capabilities. In this framework, the authors are currently involved in developing different software tools and experimental apparatus.

## REFERENCES

[1] R. Zoughi, *Microwave Nondestructive Testing and Evaluation*, The Netherlands: Kluwer, 2000.

[2] G. C. Giakos et al., “Noninvasive imaging for the new century,” *IEEE Instrum. Meas. Mag.*, vol. 2, pp. 32–35, June 1999.

[3] J. C. Bolomey and N. Joachimowicz, “Dielectric metrology via microwave tomography: Present and future,” in *Materials Research Society Symp. Proc.*, vol. 347, 1994, pp. 259–265.

[4] M. Tabib-Azar, “Applications of an ultra high resolution evanescent microwave imaging probe in the nondestructive testing of materials,” *Mater. Eval.*, vol. 59, pp. 70–78, Jan. 2001.

[5] S. J. Lockwood and H. Lee, “Pulse-Echo microwave imaging for NDE of civil structures: Image reconstruction, enhancement, and object recog- nition,” *Int. J. Imaging Syst. Technol.*, vol. 8, pp. 407–412, 1997.

[6] R. J. King and P. Stiles, “Microwave nondestructive evaluation of com- posites,” in *Review of Progress in Quantitative Nondestructive Evalua- tion*. New York: Plenum, 1984, vol. 3, pp. 1073–81.

[7] K. Meyer, K. J. Langenberg, and R. Schneider, “Microwave imaging of defects in solids,” in *Proc. 21st Annual Review of Progress in Quantita- tive NDE*, Snowmass Village, CO, July 31–Aug. 5, 1994.

[8] Y. M. Wang and W. C. Chew, “An iterative solution of two-dimensional electromagnetic inverse scattering problem,” *Int. J. Imaging Syst. Technol.*, vol. 1, no. 1, pp. 100–108, 1989.

[9] W. C. Chew and Y. M. Wang, “Reconstruction of two-dimensional per- mittivity using the distorted Born iterative method,” *IEEE Trans. Med. Imag.*, vol. 9, pp. 218–225, June 1990.

[10] D. Colton and R. Kress, *Inverse Acoustic and Electromagnetic Scat- tering*. New York: Springer-Verlag, 1998.

[11] S. Caorsi, A. Massa, and M. Pastorino, “A crack identification mi- crowave procedure based on a genetic algorithm for nondestructive testing,” *IEEE Trans. Antennas Propagat.*, vol. 49, pp. 1812–1820, Dec. 2001.

[12] S. Caorsi, A. Massa, M. Pastorino, and F. Righini, “Crack detection in lossy two-dimensional structures by means of a microwave imaging ap- proach,” *Int. J. Applied Electromagnetics Mechanics*, vol. 11, no. 4, pp. 233–244, 2000.

[13] M. Pastorino, A. Massa, and S. Caorsi, “A global optimization technique for microwave nondestructive evaluation,” *IEEE Trans. Instrum. Meas.*, pp. 666–673, Aug. 2002.

[14] D. S. Jones, *The Theory of Electromagnetism*. Oxford, U.K.: Perg- amon, 1964.

[15] D. E. Goldberg, *Genetic Algorithms in Search, Optimization, and Ma- chine Learning*. Reading, MA: Addison-Wesley, 1989.

[16] J. M. Johnson and Y. Rahmat-Samii, “Genetic algorithms in engineering electromagnetics,” *IEEE Trans. Antennas Propagat. Mag.*, vol. 39, pp. 7–26, Apr. 1997.

[17] S. Caorsi, A. Massa, and M. Pastorino, “A computational technique based on a real-coded genetic algorithm for microwave imaging pur- poses,,” *IEEE Trans. Geosci. Remote Sensing*, vol. 38, pp. 1697–1708, July 2000.

![](./images/812342219116642305_6.jpg)

Salvatore Caorsi (M’99) received the “laurea” de- gree in electronic engineering from the University of Genoa, Genoa, Italy, in 1973.

He has been a Full Professor of Electromagnetic Compatibility at the Department of Electronics, University of Pavia, Pavia, Italy since 1994. He also teaches the course on antennas at the University of Genoa. His primary activities focus on applications of electromagnetic fields to telecommunications, artificial vision and remote sensing, biology, and medicine. In particular, he is working on a research project concerning human hazard to electromagnetic exposure, numerical methods for solving electromagnetic problems, wave interaction in the presence of nonlinear media, inverse scattering and microwave imaging, and electromagnetic compatibility.

Prof. Caorsi is the Past President and founding Member of the Inter-Univer- sity Research Center for the Interactions Between Electromagnetic Fields and Biological Systems (ICEmB).

![](./images/812342219116642305_7.jpg)

Andrea Massa received the “laurea” degree in elec- tronic engineering and the Ph.D. degree in electronics and computer science from the University of Genoa, Genoa, Italy, in 1992 and 1996, respectively.

He was an Assistant Professor of Electromagnetic Fields at the Department of Biophysical and Elec- tronic Engineering, University of Genoa, from 1997 to 1999, teaching the university course of Electro- magnetic Fields 1. Since 2000, he has been Associate Professor at the University of Trento, Trento, Italy, and he is currently also the Director of the ELEDI- ALab (Electromagnetic Diagnostics Laboratory) at the University of Trento. His research work since 1992 has been principally on electromagnetic direct and inverse scattering, microwave imaging, optimization techniques, wave propaga- tion in the presence of nonlinear media, and wireless communication and appli- cations of electromagnetic fields to telecommunications, medicine, and biology.

Prof. Massa is a Member of the Progress in Electromagnetic Research Sym- posium (PIERS) Technical Committee and of the Inter-University Research Center for the Interactions Between Electromagnetic Fields and Biological Systems (ICEmB).

![](./images/812342219116642305_8.jpg)

Matteo Pastorino (M’90–SM’96) received the “laurea” degree in electronic engineering and the Ph.D. degree in electronics and computer sciencefrom the University of Genoa, Genoa, Italy, in 1987 and 1992, respectively.

He is currently an Associate Professor of Electro- magnetic Fields at the Department of Biophysical and Electronic Engineering, University of Genoa, where he is in charge of the Applied Electromag- netics Group and Vice-Director of the department. He teaches the university courses of Electromagnetic Fields and Antennas and Remote Sensing. His main research interests are in the field of electromagnetic direct and inverse scattering, microwave imaging, wave propagation in the presence of nonlinear media, and analytical and numerical methods in electromagnetism.

Prof. Pastorino is Member of the IEEE Instrumentation and Measurement Technical Committee on Imaging Systems and of the Società Italiana di Elet- tromagnetismo (SIEM).

![](./images/812342219116642305_9.jpg)

Andrea Randazzo received the “laurea” degree in telecommunication engineering from the University of Genoa, Genoa, Italy, in 2001. He is currently working toward the Ph.D. degree in space science and engineering with the Applied Electromagnetics Group, Department of Biophysical and Electronic Engineering (DIBE), University of Genoa.

His primary research interests are in the field of electromagnetic scattering (both direct and inverse) and numerical methods for microwave nondestruc- tive evaluations and imaging.

![](./images/812342219116642305_10.jpg)

Andrea Rosani received the “laurea” degree in telecommunication engineering from the University of Trento, Trento, Italy, in 2002. He is currently working toward the Master’s degree in telecommu- nication engineering at the same university.

He is a member of the RP Technical Staff at the Department of Information and Communication Technologies (DIT), University of Trento, and coordinates the technical activities of the Evaluation & Monitoring in Industrial Processes Research Program. His main interests are in the framework of electromagnetic inverse scattering and quality engineering.