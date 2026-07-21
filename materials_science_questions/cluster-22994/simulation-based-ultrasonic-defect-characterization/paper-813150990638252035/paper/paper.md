# Simulation of Ultrasonic Surface Waves with Multi-Gaussian and Point Source Beam Models

Xinyu Zhao$^{a,b}$, Lester W. Schmerr Jr.$^{a}$, Alexander Sedov$^{c}$, and Xiongbing Li$^{a}$

$^{a}$ Center for NDE, Iowa State University, Ames, IA, 50011, USA
$^{b}$ Dept. of Mechanical Eng., Beijing Institute of Technology, Beijing, 100081, China
$^{c}$ Dept. of Mechanical Eng., Lakehead University, Thunder Bay, ON, Canada

**Abstract.** In the past decade, multi-Gaussian beam models have been developed to solve many complicated bulk wave propagation problems. However, to date those models have not been extended to simulate the generation of Rayleigh waves. Here we will combine Gaussian beams with an explicit high frequency expression for the Rayleigh wave Green function to produce a three-dimensional multi-Gaussian beam model for the fields radiated from an angle beam transducer mounted on a solid wedge. Simulation results obtained with this model are compared to those of a point source model. It is shown that the multi-Gaussian surface wave beam model agrees well with the point source model while being computationally much more efficient.

**Keywords:** Ultrasonic Beam Model, Rayleigh Wave, Gaussian Beam, Point Source
**PACS:** 43.35

## INTRODUCTION

Rayleigh waves propagating in an elastic surface are commonly used for the near surface flaw detection and material characterization. Recently, a three-dimensional point source model for the surface beam simulation was developed using a Rayleigh wave Green function with high frequency asymptotics[1]. This point source model requires a significant amount of numerical effort to evaluate the integral over the transducer surface, so it is time-consuming. Multi-Gaussian beam models have been proved its outstanding capability in both computational efficiency and accuracy, and widely used in many complicated bulk wave simulations [2-5]. However, to date, multi-Gaussian beam models have not been extended to simulate the generation of Rayleigh waves. In this study, we combine the Gaussian beam with the Rayleigh wave Green function to produce an analytic expression of the multi-Gaussian beam model for surface wave simulations. Also some numerical comparisons of the point source model to the multi-Gaussian beam model are presented and discussed.

## GREEN FUNCTION FOR HIGH FREQUENCY RAYLEIGH WAVE

Consider a transducer placed on a Lucite wedge and radiating Rayleigh waves into a solid specimen. The free surface is described by the $\left(x_{1}, x_{2}\right)$ coordinates and the $x_{3}$ axis is taken normal to the free surface into the underlying solid as shown in Fig. 1.

![](./images/813150990638252035_1.jpg)

**FIGURE 1.** Schematic diagram of an angle beam transducer radiating Rayleigh waves into a solid specimen.

---

40th Annual Review of Progress in Quantitative Nondestructive Evaluation
AIP Conf. Proc. 1581, 556-562 (2014); doi: 10.1063/1.4864869
© 2014 AIP Publishing LLC 978-7354-1211-8/$30.00

If the pressure at the interface between the wedge and the underlying solid is known, then using an integral representation of Green's function for high frequency Rayleigh waves, the velocity components, $v_i(\mathbf{x})$, at any point, $\mathbf{x}$, in the underlying solid can be obtained as [6]

$$
v_{i}\left(\mathbf{x}\right)=\frac{-i \omega}{4 P c_{R 2}} \frac{\exp (i \pi / 4)}{\sqrt{2 \pi k_{R 2}}} \int_{S} p\left(\mathbf{x}_{\mathbf{s}}, \omega\right) G_{3 i}\left(\mathbf{x}, \mathbf{x}_{\mathbf{s}}\right) \frac{\exp \left(i k r_{2}\right)}{\sqrt{r_{2}}} d S\left(\mathbf{x}_{\mathbf{s}}\right)
\tag{1}
$$

where $\omega$ is the angular frequency, $S\left(\mathbf{x}_{\mathbf{s}}\right)$ is the area between the wedge and the specimen surface, $c_{R 2}, k_{R 2}$ are the wave speed and wave number of Rayleigh waves in the solid specimen, and $r_{2}=\sqrt{\left(x_{1}-x_{s 1}\right)^{2}+\left(x_{2}-x_{s 2}\right)^{2}}$ indicates the horizontal distance from any point under the wedge $\mathbf{x}_{\mathbf{s}}(x_{s 1}, x_{s 2}, 0)$ to the calculation position $\mathbf{x}(x_1, x_2, 0)$. $P$ is a "power flow" term defined as

$$
P=\frac{1}{2} \rho_{2} c_{R 2} \int_{0}^{+\infty}\left(\left|\widehat{v}_{n 1}\right|^{2}+\left|\widehat{v}_{n 2}\right|^{2}\right) d x_{3}
\tag{2}
$$

and $G_{ij}\left(\mathbf{x},\mathbf{x}_{\mathbf{s}}\right)$ are components of the three-dimensional Green function term for high frequency Rayleigh waves given by

$$
G_{i j}\left(\mathbf{x}, \mathbf{x}_{\mathbf{s}}\right)=p_{i}^{*}\left(\mathbf{x}_{s}\right) p_{j}(\mathbf{x})
\tag{3}
$$

where $(\ )^{*}$ denotes the complex conjugate and the "polarization" terms are given as

$$
\mathbf{p}\left(x_{3}\right)=\left\{\begin{array}{c}
\widehat{v}_{n 1}\left(x_{3}\right) \frac{\left(x_{1}-x_{s 1}\right)}{r_{2}} \\
\widehat{v}_{n 1}\left(x_{3}\right) \frac{\left(x_{2}-x_{s 2}\right)}{r_{2}} \\
i \widehat{v}_{n 2}\left(x_{3}\right)
\end{array}\right\}, \mathbf{p}\left(x_{s 3}\right)=\left\{\begin{array}{c}
\widehat{v}_{n 1}\left(x_{s 3}\right) \frac{\left(x_{1}-x_{s 1}\right)}{r_{2}} \\
\widehat{v}_{n 1}\left(x_{s 3}\right) \frac{\left(x_{2}-x_{s 2}\right)}{r_{2}} \\
i \widehat{v}_{n 2}\left(x_{s 3}\right)
\end{array}\right\}
\tag{4}
$$

Both the power and polarization terms are given in terms of the $\widehat{v}_{n 1}\left(x_{3}\right), \widehat{v}_{n 2}\left(x_{3}\right)$ functions. These functions are just proportional to the ordinary two-dimensional surface wave modal functions shown in many textbooks [7]

$$
\begin{aligned}
\widehat{v}_{n 1}\left(x_{3}\right) & =\exp \left(-\alpha_{n 1} x_{3}\right)-\frac{\left(2 c_{s 2}^{2}-c_{R 2}^{2}\right)}{2 c_{2}^{2}} \exp \left(-\alpha_{n 2} x_{3}\right) \\
\widehat{v}_{n 2}\left(x_{3}\right) & =\frac{c_{R 2} \alpha_{n 1}}{\omega} \exp \left(-\alpha_{n 1} x_{3}\right)-\frac{\omega}{c_{R 2} \alpha_{n 2}} \frac{\left(2 c_{s 2}^{2}-c_{R 2}^{2}\right)}{2 c_{s 2}^{2}} \exp \left(-\alpha_{n 2} x_{3}\right)
\end{aligned}
\tag{5}
$$

where $\alpha_{n 1}=\omega \sqrt{\frac{1}{c_{R 2}}-\frac{1}{c_{p 2}^{2}}}, \alpha_{n 2}=\omega \sqrt{\frac{1}{c_{R 2}}-\frac{1}{c_{s 2}^{2}}}$, $c_{p 2}, c_{s 2}$ are the P-wave and S-wave speed in the solid specimen.

# POINT SOURCE MODEL FOR RAYLEIGH WAVES

Recently, a point source model for Rayleigh waves has been developed [1], using a modified Rayleigh integral [8] to obtain the pressure under the wedge as

$$
p\left(\mathbf{x}_{s}, \omega\right)=\frac{-i \omega p_{0}}{2 \pi \rho_{1} c_{p 1}^{2}} \rho_{2} c_{s 2} T \int_{S_{T}} K_{p}\left(\theta_{p}\right) \frac{\exp \left(i k_{p 1} r_{1}\right)}{r_{1}} d S
\tag{6}
$$

where $\rho_{1}$, $c_{p 1}$ and $\rho_{2}$, $c_{s 2}$ are the densities and P-wave speeds in the Lucite wedge and the solid specimen, respectively. $T$ is the transmission coefficient, and $K_{p}\left(\theta_{p}\right)$ is the P-wave directivity function.

Placing the pressure expression of Eq. (6) into the Green function of Eq. (1), and using the method of stationary phase approximation, the point source model for Rayleigh waves can been given as [1]

$$
\begin{aligned}
v_{i}(\mathbf{x})= & \frac{-i k_{R 2} \rho_{2} c_{s 2} v_{0}}{4 P \cos \theta} \frac{\exp (i \pi / 4)}{\sqrt{2 \pi k_{R 2}}} \\
& \times \int_{S_{T}} T K_{p}\left(\theta_{p}\right) p_{3}^{*}(0) p_{i}\left(x_{3}\right) \frac{\exp \left(i k_{p 1} r_{10}+i k_{R 2} r_{20}\right)}{\sqrt{r_{20}+r_{10} \sin \theta}} d S_{T}
\end{aligned}
\tag{7}
$$

where $r_{10}$ is the distance from the element center to the incident point at interface between the wedge and the specimen. $r_{20}$ is the distance from the incident point to the calculation point. The angle $\theta$ is the incident angle for Rayleigh wave generation and $S_{T}$ denotes the area of the transducer surface.

# MULTI-GAUSSIAN BEAM MODEL FOR RAYLEIGH WAVES

In order to get an analytic solution for Rayleigh waves, we express the pressure under the wedge with a multi-Gaussian beam model as [9]

$$
\begin{aligned}
p\left(\mathbf{x}_{s}, \omega\right)= & \rho_{2} c_{s 2} v_{0}(\omega) T \exp \left(i k_{p 1} r_{10}\right) \exp \left(i k_{R 2} x_{s 1}\right) \\
& \times \sum_{r=1}^{10} \frac{A_{r}}{1+i B_{r} x_{3} / D_{R}} \exp \left(i M_{1} \frac{x_{s 1}^{2}}{2}\right) \exp \left(i M_{2} \frac{x_{s 2}^{2}}{2}\right)
\end{aligned}
\tag{8}
$$

where $A_{r}, B_{r}$ are ten complex coefficients used in later simulations, some details of the multi-Gaussian beam model and these coefficients can be found in ref.[9]. Here $M_{1}, M_{2}$ terms can be expressed as

$$
M_{1}=\frac{k_{p 1} \cos ^{2} \theta}{r_{10}-i D_{R} / B_{r}}, \quad M_{2}=\frac{k_{p 1}}{r_{10}-i D_{R} / B_{r}}
\tag{9}
$$

with $D_{R}=k_{p 1} a_{1}^{2} / 2$ defined as Rayleigh distance, and $a_{1}$ is the radius of the circular transducer.

In Eq.(1) we replace $1 / \sqrt{r_{2}}$ term with $1 / \sqrt{x_{1}}$ whereas in the exponential phase term we keep higher order terms, giving

$$
\frac{\exp \left(i k_{R 2} r_{2}\right)}{\sqrt{r_{2}}} \approx \frac{1}{\sqrt{x_{1}}} \exp \left(i k_{R 2}\left(x_{1}+\frac{x_{2}^{2}}{2 x_{1}}+\frac{x_{s 2}^{2}}{2 x_{1}}-x_{s 1}-\frac{x_{2} x_{s 2}}{x_{1}}\right)\right)
\tag{10}
$$

Substitute Eq. (8) and (10) into the Eq.(1), and the surface integral term can be simplified as

$$
\begin{aligned}
& \int_{S_{P}} \exp \left(i k_{R 2} x_{s 1}\right) \exp \left(i M_{1} \frac{x_{s 1}^{2}}{2}\right) \exp \left(i M_{2} \frac{x_{s 2}^{2}}{2}\right) \frac{\exp \left(i k_{R 2} r\right)}{\sqrt{r}} d S\left(\mathbf{x}_{\mathbf{s}}\right) \\
& =\frac{\exp \left(i k_{R 2} x_{1}+i k_{R 2} \frac{x_{2}^{2}}{2 x_{1}}\right)}{\sqrt{x_{1}}} \\
& \quad \times \int_{S_{P}} \exp \left(i M_{1} \frac{x_{s 1}^{2}}{2}\right) \exp \left(i \frac{M_{2}+k_{R 2} / x_{1}}{2} x_{s 2}^{2}-\frac{i k_{R 2} x_{2}}{x_{1}} x_{s 2}\right) d x_{s 1} d x_{s 2} \\
& =\frac{\exp \left(i k_{R 2} x_{1}+i k_{R 2} \frac{x_{2}^{2}}{2 x_{1}}\right)}{\sqrt{x_{1}}} \sqrt{\frac{2 i \pi}{M_{1}}} \sqrt{\frac{2 i \pi}{M_{2}+k_{R 2} / x_{1}}} \exp \left(\frac{-i k_{R 2}^{2}\left(\frac{x_{2}}{x_{1}}\right)^{2}}{2\left(M_{2}+k_{R 2} / x_{1}\right)}\right) \\
& =\frac{2 i \pi \exp \left(i k_{R 2} x_{1}\right)}{\sqrt{M_{1}} \sqrt{M_{2} x_{1}+k_{R 2}}} \exp \left(i k_{R 2} \frac{x_{2}^{2}}{2}\left(\frac{M_{2}}{M_{2} x_{1}+k_{R 2}}\right)\right)
\end{aligned}
\tag{12}
$$

Then after some algebra, a multi-Gaussian beam model for Rayleigh waves can be given as

$$
\begin{aligned}
v_{i}(\mathbf{x})= & \frac{\rho_{2} c_{s 2} v_{0} k_{R 2} \exp (i \pi / 4) T}{4 P} \sqrt{\frac{2 \pi}{k_{R 2}}} \exp \left(i k_{p 1} r_{10}+i k_{R 2} x_{1}\right) \\
& \times p_{3}^{*}(0) p_{i}\left(x_{3}\right) \sum_{r=1}^{10} \frac{\left(-i D_{R} / B_{r}\right) A_{r}}{z_{1}-i D_{R} / B_{r}} \frac{\exp \left(\frac{i k_{R 2} M_{2} x_{2}^{2}}{2\left(M_{2} x_{1}+k_{R 2}\right)}\right)}{\sqrt{M_{1}} \sqrt{M_{2} x_{1}+k_{R 2}}}
\end{aligned}
\tag{13}
$$

## SIMULATIONS

In this part, the surface beam fields radiating from an angle beam transducer will be simulated by both of the point source model (PSM) and the multi-Gaussian beam (MGB) model. The specific transducer used in the simulations is an angle beam transducer with a 6mm radius circular element and 5MHz center frequency. The P-wave speed and incident angle for Lucite wedge are 2.7 mm/µs and 71.63 degrees, and the surface wave speed in aluminum specimen is 2.845 mm/µs. The origin is selected as the incident point on the specimen surface as shown in Fig. 1.

![](./images/813150990638252035_2.jpg)

**FIGURE 2.** Comparisons of on-axis magnitudes of velocity fields. Solid lines – PSM, dashed lines – MGB model.

The one-dimensional on-axis magnitudes of velocity fields on specimen surface are shown in Fig. 2. When using the PSM, the circular transducer surface should be divided into many small elements. However, for some calculating points under the wedge, the condition with fixed incident angle of 71.63 degree cannot be satisfied for all divided elements, so the calculation points with $0{<}x_1{<}20$ mm are not displayed for the PSM case. It can be seen that the velocity fields calculated by the MGB model agree well with the PSM results. Both methods show that the $v_1$ and $v_3$ components play a dominant role and the $v_2$ component is very small and is identically zero along the refracted central axis ray of the transducer. This means that the main energy of the surface wave is in the $x_1$-$x_3$ plane .

![](./images/813150990638252035_3.jpg)

**FIGURE 3.** Comparisons of off-axis magnitudes of velocity fields at $x_1 = 50$mm. Solid lines – PSM, dashed lines – MGB model.

The one-dimensional off-axis magnitudes of velocity fields at $x_1 = 50$mm on specimen surface are shown in Fig. 2. It can be seen that the velocity fields calculated with the MGB method agree with the PSM results in the main beam energy region of $-15$mm$< x_2{<}15$ mm , while some small deviations can be found for $x_2{<}-15$ and $x_2 >15$ region.

![](./images/813150990638252035_4.jpg)

FIGURE 4. Comparisons of two-dimensional magnitudes of the velocity fields on specimen surface.

The two-dimensional magnitudes of velocity fields on specimen surface are shown in Fig. 4. Here the beam patterns given by the MGB method show good agreement to those found with the PSM.

![](./images/813150990638252035_5.jpg)

FIGURE 5. Comparisons of magnitudes of the velocity fields in the depth direction at $x_1$= 50 and $x_2$ = 0.m Solid lines – PSM, dashed lines – MGB model.

Figure 5 shows the comparisons of the velocity magnitudes in the thickness direction of the specimen. Good agreement can also be found for the two methods. It can be seen from these plots that the main energy of Rayleigh waves is concentrated on the near surface of the specimen within essentially one wave length.

The computational efficiency was also compared for the two methods. Here two-dimension velocity amplitudes were calculated for 200×200 points to evaluate the computational times. For the PSM method the circular element was divided into 200 sector units in order to obtain high accuracy. The calculation times of the PSM and MGB model were 126.0 seconds and 2.6 seconds, respectively.

# SUMMARY AND CONCLUSIONS

In this study, a multi-Gaussian beam model for Rayleigh waves was developed to calculate the beam fields radiating from an angle beam wedge transducer. The accuracy and computational efficiency of the multi-Gaussian model was verified by comparing with the more exact point source method. This new model extends the multi- Gaussian beam model approach from bulk waves to surface wave fields.

# ACKNOWLEDGMENTS

This work was supported for L.W. Schmerr by the National Science Foundation Industry/University Cooperative Research Center program at the Center for NDE, Iowa State University. A. Sedov wishes to acknowledge support by the Natural Sciences and Engineering Research Council of Canada. X.Y. Zhao and X.B. Li wish to acknowledge support by the National Natural Science Foundation of China (Grant No. 51105033, 61271356).

# REFERENCES

1. L. W. Schmerr and A. Sedov, "Ultrasonic Beam Models for the Generation of Surface Waves and Plate Waves with Angle Beam Transducers" in Review of Progress in Quantitative Nondestructive Evaluation, **30A**, American Institute of Physics, Melville, N.Y., 2011, pp.771-777.
2. J. J. Wen and M. A. Breazeale, *J. Acoust. Soc. Amer.* **83**, 1752-1756 (1988).
3. M. Spies, *NDT&E International* **33**, 155-162 (2000).
4. X. Y. Zhao and T. Gang, *Ultrasonics* **49**, 126-130 (2009).
5. R. J. Huang, L. W. Schmerr and A. Sedov, *Res. Nondestr. Eval.* **18**, 193-220 (2007).
6. K. Aki and P. G. Richards, Quantitative Seismology -Theory and Methods, Vol.1, W.H. Freeman and Co., San Francisco, CA., (1980).
7. J. L. Rose, Ultrasonic Waves in Solid Media, Cambridge University Press, U.K., (1999).
8. L. W. Schmerr, Fundamentals of Ultrasonic Nondestructive Evaluation - A Modeling Approach, Plenum Press, New York, N.Y., (1998).
9. L. W. Schmerr and S. J. Song, Ultrasonic Nondestructive Evaluation Systems - Models and Measurements, Springer, New York, N.Y (2007).

AIP Conference Proceedings is copyrighted by AIP Publishing LLC (AIP). Reuse of AIP content is subject to the terms at: http://scitation.aip.org/termsconditions. For more information, see http://publishing.aip.org/authors/rights-and-permissions.