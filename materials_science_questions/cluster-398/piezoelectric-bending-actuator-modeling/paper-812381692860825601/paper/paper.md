# Mixed Analytical and Numerical Design Method for Piezoelectric Transformers
A.M. Sánchez, M. Sanz¹, R. Prieto, J. A. Oliver and J. A. Cobos

Universidad Politécnica de Madrid (UPM)
División de Ingeniería Electrónica (DIE)
José Gutiérrez Abascal, 2
28006 Madrid SPAIN
Tel: 34-91-411 75 17 Fax: 34-91-564 59 66
e-mail: almudena@upmdie.upm.es

**Abstract** - Analytical models are widely used for Piezoelectric Transformers (PTs) design. In this paper, the additional usefulness of Finite Element Analysis (FEA) for PT design will be shown. With FEA it is possible to optimize the PT design not only by maximizing the energy transference, but cleaning the working frequency range of spurious modes (geometrical 2D/3D effects). Besides, FEA tools allow studying other interesting aspects of the PT design such as the manufacturing tolerances or the influence of the fixing layer on the PT performance (which is a critical design point). A mixed analytical and numerical design method for PT is proposed.

## I. INTRODUCTION

Nowadays Piezoelectric Transformers (PTs) become, in some applications, an alternative to the magnetic transformers for power supplies, when the system miniaturization, high voltage conversion ratio, higher isolation voltages and low EMI content are critical design points [1-3]. In this paper, the design stages of a PT will be shown, using a specific example: a PT for an AC/DC converter of a mobile phone battery charger. The PT works in thickness mode, as it is shown in Figure 1.

![](./images/812381692860825601_1.jpg)

Figure 1. Multi-layer PT structure and electrodes.

Analytical equations which describe the PT behavior are difficult to solve as a 3D system [4]. So a simplification is done, considering the vibration of the PT in only one direction, the thickness direction, although displacements in other directions may exist. Resultant model is a one dimension (1D) model. With an analytical 1D model, it is possible to select the type of material, number of layers, thickness of each layer, area, interleaving of the electrodes, but not the geometry. Therefore, it is necessary to use Finite Element Analysis (FEA) tools, in order to take into account two dimension/three dimension (2D/3D) effects to select the geometry for an optimum design. The main goal in PT geometrical design is that the working frequency range (between resonance and anti-resonance) must be free of spurious modes. The spurious modes make the PT vibrate in different and non-desired directions, which implies a reduction in the PT efficiency. Apart from avoiding spurious modes, another design goal is to obtain a high electromechanical coupling coefficient ($k_{eff}$), in order to maximize the efficiency of the conversion and power transference, as can be deduced from the following equation:

$$
\frac{Power}{Volume} \propto k_{eff}^{2} \cdot \varepsilon \cdot f \tag{1}
$$

where $\varepsilon$ is the material permittivity and $f$ the vibration frequency.

## II. DESIGN STAGES

In this section, a method for PTs design is described, combining analytical and numerical results. The method is validated with several PTs designs for the same converter specifications (universal input voltage, output voltage is 12V and output power is 10W), without loss of generality.

The power that a PT can transfer depends on the material type and area. Total thickness of the transformer is selected according with the specified working frequency. By selecting the number of layers of the primary and the secondary side of the PT, the voltage ratio is fixed [5]. All of these constructive parameters can be selected with an analytical 1D model and most of the designers stop at this stage. But it is possible to go further with FEA. This way, geometry or shape is selected in order to reduce the spurious modes at the working frequency range. Manufacturing tolerances must be taken into account in the design process because they may induce new spurious modes. Finally, as the PT is not an isolated component, it must be fixed in a PCB. As will be shown in section E, this is a very critical design point.

![](./images/812381692860825601_2.jpg)

Figure 2. Design parameters of a PT

---
¹ Currently she is assistant professor at Universidad Carlos III de Madrid

0-7803-7754-0/03/$17.00 ©2003 IEEE

![](./images/812381692860825601_3.jpg)

Figure 9. Global converter schematic.

![](./images/812381692860825601_4.jpg)

Figure 10. PT1 converter waveforms. Gate-source voltages (Vgs), output power (Pout), PT1 input current (Ipt) and PT1 input voltage (Vpt).

![](./images/812381692860825601_5.jpg)

Figure 11. PT2 converter waveforms. Gate-source voltages (Vgs), output power (Pout), PT1 input current (Ipt) and PT1 input voltage (Vpt).

### C. 2D/3D Design. Geometry Selection

With 1D analysis, it can be determined the thickness of each layer and the total area. But there are a lot of geometric possibilities for the PT dimensioning, such as a disc, ring, plate, etc. FEA tools are useful to distribute the area in a correct geometry, that is to implement the 1D design in a proper 3D design. So, as an example of 2D/3D design, a ring shape for PT2 is selected, similar to the one of Figure 23. The aim is to show how critical can be the selection of the internal and external diameters ($\phi_{\text{in}}$ and $\phi_{\text{out}}$) of the ring, keeping the area as a constant. Interleaving of electrodes (which consists on placing the secondary electrodes between the primary ones) is used in order to improve the PT electrical performance, as it is explained in [9].

FEA tool selected is ATILA$^\circledR$ [10], because it is specially developed for the simulation of the electromechanical coupling in 2D/3D of piezoelectric materials. As it was seen in Figure 5, PT ring presents axial symmetry (being z the symmetry axis). Therefore, 2D and not 3D analyses are done in order to reduce the computing time, since no important different results are obtained, as will be analyzed later.

The result of a modal analysis with FEA tool is $k_{\text{eff}}$ as a function of frequency. So, modal analyses have been made for two different diameters selection: PT2a with $\phi_{\text{out}}$=19.73mm and $\phi_{\text{in}}$=11.61mm and PT2b with $\phi_{\text{out}}$=24.97mm and $\phi_{\text{in}}$=19.21mm. It is very useful because it allows to test whether the working frequency range is free of spurious modes or the $k_{\text{eff}}$ of thickness mode is high enough (around 40%), because $k_{\text{eff}}$ depends not only on the material properties but on the specific geometry.

As shown in Figure 12, diameters in PT2a are not appropriate, since there are many spurious modes close to the resonance frequency. On the contrary, for PT2b the selection of diameters is right because the working frequency range is clean of spurious modes (Figure 13). Besides PT2b $k_{\text{eff}}$ is higher than PT2a $k_{\text{eff}}$, due to the reduction of the spurious modes close to the resonance. It is necessary to emphasize that finding the correct diameter is not an easy task: for the same area, more than five combinations of $\phi_{\text{out}}$ and $\phi_{\text{in}}$ have been analyzed and only one, PT2b, fulfils the requirements.

Other useful information from FEA is electric field and stress distribution, which limits the PT power density [11]. It is also possible to extract graphics of the displacement for each frequency, which is suitable to understand the PTs mechanical behavior. It is shown in Figure 14 that PT2b vibration between resonance and anti-resonance frequency consists on a compression and expansion along PT thickness (Z axis), that is the first order of thickness mode.

![](./images/812381692860825601_6.jpg)

Figure 12. $k_{\text{eff}}$ vs resonance frequency. PT2a design.

![](./images/812381692860825601_7.jpg)

Figure 13. $k_{\text{eff}}$ vs resonance frequency. PT2b design.

![](./images/812381692860825601_8.jpg)

Figure 14. Axial View of the PT2b vibration in thickness mode.
Discontinuous line represents the initial structure, without deformation and
continuous line represents the deformed structure by applying a voltage to
the primary side.

FEA results have been validated with measurements in real
samples. If the selection of diameters is bad, the PT input
impedance for the open circuit condition presents spurious
modes (Figure 15). But if the selection of diameters is right
the input impedance is free of spurious modes (Figure 16).

All the previous PTs designs have a symmetry axis, so 2D
analyses can be developed. 3D analyses have no symmetry
restrictions in the structure to analyze but the time to define
and solve the problem is longer than in a 2D analysis. 3D
study has the advantage of being the most accurate. Therefore
a 3D harmonic analysis of the PT2b has been done to be
compared with the 2D one. The main result of the harmonic
analysis is a graph of impedance as a function of the selected
frequencies, as it is shown in Figure 17.

![](./images/812381692860825601_9.jpg)

Figure 15. Input impedance vs frequency. Bad PT design.

![](./images/812381692860825601_10.jpg)

Figure 16. Input impedance vs frequency. Good PT design.

![](./images/812381692860825601_11.jpg)

Figure 17. Input impedance vs frequency. Comparison between PT2b 2D and
3D results.

It is deduced from Figure 17, that 2D and 3D impedance
curves are very similar. However, maximum and minimum
impedance values are more accurate in a 3D analysis.
Regarding the solving time, it goes from a few minutes in 2D
to several hours in 3D analysis, using a Pentium IV with
256MB of RAM.

Therefore, 2D or 3D analyses will be chosen depending on
the specific design requirements. In general, it is advisable to
take advantage of the symmetries to simplify the problem.

### D. Manufacturing Tolerances Influence on the PT
Performance

PT working frequency range must not be sensitive to
dimension changes caused by the manufacturing tolerances.
The manufacturing of Pz26 material presents tolerances about
$\pm 3\%$ for the thickness of each layer, $\phi_{in}$ and $\phi_{out}$. Several
combinations of tolerances have been tested for the PT2b
design; some of them have influence and other not. For
example, considering a tolerance of $-3\%$ in thickness and $\phi_{in}$
and $+3\%$ in $\phi_{out}$, there is a reduction in $k_{eff}$, comparing with
the nominal case, and also a spurious mode appears close to
the resonance (Figure 18).

An optimum design must not be sensitive to these
tolerances. In addition to that, it would be necessary to warn
the PT manufacturer about the critical dimensions.

![](./images/812381692860825601_12.jpg)

Figure 18. $k_{eff}$ vs resonance frequency. Tolerances influence on PT2b.

### E. Fixing Layer Influence on the PT Performance

Fixing the PT to the PCB is a difficult point, because the vibration of the PT can be perturbed, modifying its electrical performance. Fixing can also be used to provide a path for thermal dissipation. Anyway, it is necessary that the fixing method ensures the mechanical robustness of the converter. Three different ways have been tested:

- With a thermal glue at the bottom part. It is very simple but the drawback is that efficiency drops dramatically, because PT natural vibration is not allowed.
- Using clips or screws. This method keeps efficiency almost constant, especially if a thermally conductive foam is also used for fixing [12]. But, in this particular case, it is not easy to access to the electrodes for soldering the wires.
- Adding a fixing layer, as a belt, to the PT. This fixing method is the one selected because it makes easier the connection to the PCB with thermal glue and the soldering of wires if the electrodes are placed in the fixing belt. It also has the advantage of providing a thermal path. The main drawback is that it is very sensitive to the spurious modes. So, FEA modal analyses are mandatory in the fixing belt design.

PT2b design is selected in order to study the fixing layer influence. Vibration figures with the fixing layer free and glued are grouped in Table II. If the fixing layer is left free a spurious mode appears near the anti-resonance frequency, inducing a wrong movement, and the $k_{eff}$ is reduced too (Figure 19). But these problems disappear if the fixing belt is glued, because PT vibrates in thickness mode and the resonance frequency has no spurious in its vicinity (Figure 20), as it was desired.

It is also interesting to study the effect on the PT of the fixing layer position. FEA result of PT with glued central fixing layer has been compared with the result of the fixing layer moved to a lateral position (Figure 21).

With the lateral fixing layer a new spurious mode appears near the resonance frequency (Figure 22). This justifies why, in general, the fixing layer must be placed in the area of minimum displacement near the node points, which for this specific design is placed in the middle of its thickness (Figure 1).

![](./images/812381692860825601_13.jpg)

Figure 19. $k_{eff}$ vs resonance frequency. Free central fixing layer.

![](./images/812381692860825601_14.jpg)

Figure 20. $k_{eff}$ vs resonance frequency. Glued central fixing layer.

<table>
<caption>TABLE II AXIAL VIEW OF THE PT VIBRATION AT THE RESONANCE AND ANTI-RESONANCE FREQUENCIES.</caption>
<tr>
<td></td>
<td></td>
<td>Resonance Frequency (369kHz)</td>
<td>Anti-resonance Frequency (420kHz)</td>
</tr>
<tr>
<td>![](./images/812381692860825601_15.jpg)</td>
<td>![](./images/812381692860825601_16.jpg)</td>
<td>![](./images/812381692860825601_17.jpg)</td>
<td>![](./images/812381692860825601_18.jpg)</td>
</tr>
<tr>
<td></td>
<td></td>
<td>Resonance Frequency (373kHz)</td>
<td>Anti-resonance Frequency (469kHz)</td>
</tr>
<tr>
<td>![](./images/812381692860825601_19.jpg)</td>
<td>![](./images/812381692860825601_20.jpg)</td>
<td>![](./images/812381692860825601_21.jpg)</td>
<td>![](./images/812381692860825601_22.jpg)</td>
</tr>
</table>

![](./images/812381692860825601_23.jpg)

Figure 21. PT ATILA mesh with a glued lateral fixing layer.

![](./images/812381692860825601_24.jpg)

Figure 22. $k_{eff}$ vs resonance frequency. Glued lateral fixing layer.

Finally, a 3D view of the PT2b design with the proper fixing layer is presented in Figure 23.

![](./images/812381692860825601_25.jpg)

Figure 23. 3D view of the designed PT.

### III. CONCLUSIONS

In this paper, a design method for PT has been proposed and validated. This procedure consists on a combination of analytical and numerical design. It takes into account not only 1D effects (with analytical models), but 2D/3D effects (with FEA tools). Shape, tolerances and fixing of the PT are the main 2D/3D effects that must not be forgotten in the design process. It consists of the following stages:

- Topology selection
- Analytical Modeling and Design
- 2D/3D Design. Geometry Selection
- Manufacturing Tolerances Influence on the PT Performance
- Fixing Layer Influence on the PT Performance

Since PTs design is a complex task, this method makes possible an optimization before manufacturing it, reducing the time and cost of the process.

The method has been successfully applied to several examples of PTs design, with good results both at component and converter level. This design method is also useful to achieve ZVS, suppressing the inductor of the converter. Inductor increases significantly the total volume of the converter, as can be seen in Figure 24 [13]. Both PT and inductor have a similar size, when PT has not been designed to achieve ZVS. It is pending to build the magnetic-less converter with PT2b to validate its performance.

![](./images/812381692860825601_26.jpg)

Figure 24. Photograph of the power converter. PT and magnetic component are highlighted

### IV. REFERENCES

[1] T. Zaitsu, O. Ohnishi, T. Inoue, M. Shoyama, T. Ninomiya, F.C. Lee and G.C. Hua, "Piezoelectric transformer operating in thickness extensional vibration and its application to switching converter", Proc. of IEEE Power Electronics Specialists Conference (PESC '94), vol.1, pp. 585-589, 1994.

[2] O. Ohnishi, H. Kishie, A. Iwamoto, Y. Sasaki, T. Zaitsu, and T. Inoue, "Piezoelectric ceramic transformer operating in thickness extensional vibration mode for power supply", Proc. of IEEE Ultrasonics Symposium, vol.1, pp. 483-488, 1992.

[3] Eddy Wells, "Comparing magnetic and piezoelectric transformer approaches in CCFL applications." Analog Applications Journal. Issue: Q1, 2002. Available: http://www.ti.com/sc/analogapps

[4] A. Iula,, N. Lamberti and M. Pappalardo, "An approximated 3-D model of cylinder-shaped piezoceramic elements for transducer design", IEEE Transactions on Ultrasonics, Ferroelectrics and Frequency Control, vol.45, Issue: 4, pp.1056 -1064, July 1998.

[5] C. Y. Lin "Design and Analysis of Piezoelectric Transformer converters", Thesis VPEC, July 1997.

[6] J.A. Oliver, R. Prieto, M. Sanz, J.A. Cobos, and J. Uceda, "1D Modeling of Multi-layer piezoelectric transformers", Proc. of IEEE Power Electronics Specialists Conference, (PESC'01), vol.4, pp. 2097-2102, 2001.

[7] Ferroperm Piezoceramics A/S Catalog. Available: http://www.ferroperm-piezo.com

[8] M. Sanz, P. Alou, R. Prieto, J.A. Cobos and J. Uceda, "Comparison of different alternatives to drive Piezoelectric Transformers", Proc. of IEEE Applied Power Electronics Conference (APEC'02), vol. 1, pp. 358-364, 2002.

[9] M. Sanz, P. Alou, J.A. Oliver, R. Prieto, J.A. Cobos and J. Uceda, "Interleaving of electrodes in Piezoelectric Transformers", Proc. of IEEE Power Electronics Specialist Conference (PESC'02), vol. 2, pp. 567-572, 2002.

[10] ATILA®. Available: http://www.cedrat.com/software/atila/atila.htm

[11] A.M. Flynn and S.R. Sanders, "Fundamental limits on energy transfer and circuit considerations for piezoelectric transformers", IEEE Transactions on Power Electronics, vol. 17, pp. 8-14, January 2002.

[12] E. M. Baker, W. Huang, D. Y. Chen and F. C. Lee "A Novel Thermally Conductive Mounting Technique for Piezoelectric Transformer", Proc. of CPES Power Electronics Seminar, pp.231-233, 2002.

[13] J. Navas, T. Bove, J.A. Cobos, F. Nuño and K. Brebol, "Miniaturised battery charger using piezoelectric transformers", Proc. of IEEE Applied Power Electronics Conference (APEC'01), vol. 1, pp. 492-496, 2001

846