# DGS curve evaluation applied to ultrasonic phased array testing

M Certo, G Nardoni, P Nardoni, M Feroldi and D Nardoni

Submitted 02.02.10
Accepted 06.03.10

The application of phased array to the ultrasonic testing of components such as forged or plate products, with the longitudinal wave arranged in a sectorial scan centred at zero degrees, can be very attractive because of the possibility, due to the electronic sectorial scan of the ultrasonic beam, of producing a complete and documented volume inspection with a fewer number of scan lines than with using a standard probe. The problem is that, in this inspection technique, defect estimation is carried out, normally, by the use of a Distance Gain Size (DGS $^{\dagger}$ ) set of curves $^{[1,4,5]}$. Such curves are easily available for standard probes of circular shape, but not for phased array probes whose active area is a function of the number of active elements chosen and which can be strongly rectangular. In order to avoid such difficulty, we have developed a computer model that is capable of generating the DGS curves from an input of the actual phased array parameters. This computer model has been assessed using some calibration blocks containing flat- bottomed holes. The results are very encouraging, showing good performance when defects are in the far field of the actual probe configuration, while in the near-field region the generated DGS curves lead to a defect overestimation.

## 1. Introduction

This paper reports on the theory $^{[2,3,4]}$ developed to describe the amplitude of echoes produced by flat circular reflectors centred on the probe axis, normal to the beam and at different distances. Then the results of the experimental assessment of the program code, implemented using such a theoretical model, are presented. This paper is restricted to consider only a zero degree beam in order to present initial evidence of the influence of probe geometry on the DGS curve. The experimental work is carried out using some calibration blocks containing flat-bottomed holes. The results have been compared with those obtained using a standard probe.

## 2. Theory of the model for the generation of DGS curves

Figure 1 shows the probe-reflector geometry, where it is assumed that the probe will produce a normal ultrasonic beam and the reflector disk is centred on the probe acoustical axis and normal to it. The active surface of the linear probe is discretised in small rectangular elements according to its phased array structure (in particular, the j-index denotes the j-th phased array element). The disk reflector, due to its circular shape, is discretised according to the radial axis (m-index) and to the angular axis (n-index).

![](./images/811794764151128064_1.jpg)

Figure 1. Probe and flat circular reflector geometry for model implementation

The phased array modelling described here is restricted to a zero degree phased array probe with all the elements being excited simultaneously to generate a zero degree beam. Note that at this stage there is no modelling of delay laws to produce an angled beam or a sectorial scan.

The arrow denoted by $\rho_{j, k, m, n}$ in Figure 1 indicates the path of the ultrasonic field produced by the $(j, k)$ probe element on the surface of the $(m, n)$ reflector element, where $\rho_{j, k, m, n}$ is the distance between the two elements. If $A_{j, k, m, n}$ represents the amplitude of such an ultrasonic field, then the total field $C_{m, n}$ produced on the $(m, n)$ disk element is the summation of the ultrasonic field produced by all the probe elements, that is:

$$
C_{m, n}=\sum_{j, k} A_{j, k, m, n} \ldots \ldots \ldots \ldots \ldots \ldots \ldots \ldots \ldots \ldots(1)
$$

where the elementary field $A_{j, k, m, n}$ is expressed by the equation:

$$
A_{j, k, m, n}=\frac{w_{j, k, m, n} e^{-\frac{2 \pi f}{c} \rho_{j, k, m, n}}}{\rho_{j, k, m, n}} \Delta x \Delta y \Delta \rho_{m} \Delta \theta \ldots \ldots \ldots \ldots(2)
$$

and where:
$w_{j, k, m, n}$ is a suitable weighting function, which takes account also of a finite signal bandwidth;
$f$ is the probe frequency;
$c$ is the ultrasound velocity;
$\rho_{j, k, m, n}=\sqrt{\left(x_{j, k}-x_{m, n}\right)^{2}+\left(y_{j, k}-y_{m, n}\right)^{2}+z^{2}}$ where the $j, k$ index denotes the coordinate over the probe surface, while the $m, n$ index denotes the coordinate over the disk surface;
$\Delta x$ and $\Delta y$ are the linear sizes of the discretised probe element;
$\Delta \rho_{m}$ and $\Delta \theta$ are the radial and angular sizes of the discretised reflector disk element of index $m$.

Using the reciprocity theorem, we can express the signal received by the probe due to back reflection by the $(m, n)$ reflector disk element as the square of the incident field $C_{m, n}$ so that the total signal $S$ back reflected by the disk reflector is the summation over the $(m, n)$ index of $C_{m, n}^{2}$:

$$
S=\left|\sum_{m, n} C_{m, n}{ }^{2}\right| \ldots \ldots \ldots \ldots \ldots \ldots \ldots \ldots \ldots \ldots(3)
$$

where $S$ is taken as the modulus of complex value resulting from the summation. The weighting function $w_{j, k, m, n}$ has been assumed,

---

M Certo, G Nardoni, P Nardoni, M Feroldi and D Nardoni are with the I&T Nardoni Institute, Via della Cascina Pontevica n. 21, 25010 Folzano- Brescia, Italy. Tel: +39 (0)30 266582/2160757; Fax: +39 (0)30 2667429;
Email: nardoni@numerica.it; Web: www.nardoni.it

$^{\dagger}$ In some countries DGS is referred to as AVG

with heuristic criteria, as:
$$
w_{j, k, m, n}=\left(\frac{z}{\rho_{j, k, m, n}}\right)^{4} \ldots \ldots \ldots \ldots \ldots \ldots \ldots \ldots(4)
$$
where $\frac{z}{\rho_{j, k, m, n}}$ is the cosine of the incident angle on both the (j,k)-th discretised probe element and the (m,n)-th discretised reflecting element.

Equations (1), (2), (3) and (4) have been used to implement a computer program, written in Visual Basic 8.00, which accepts as input the phased array probe parameters and produces as output the numerical value, expressed in dB and normalised with respect to the maximum value, of the amplitude $S$ as a function of distance and the diameter of the reflector disk. Figure 2 shows the user interface of the program. The actual probe parameters are entered into the text box on the left-hand side. When the button labelled 'Compute' is pressed, the program starts the computation and the results are shown in the right-hand side. When computation is finished, the results are displayed in both numerical and graphical formats. The results can also be saved on a disk file which can be opened in an application such as MS Excel in order to generate the graphs showing the DGS curves in the usual format.

![](./images/811794764151128064_2.jpg)

Figure 2. Example of user interface for the program for DGS curve computation

![](./images/811794764151128064_3.jpg)

Figure 3. Schematic and experimental presentation of near field and far field of the ultrasonic beam generated by a standard transducer⁵⁾. The interaction between the spherical waves, generated by the probe edges, and the planar ones are the origin, as illustrated in the left-end diagram, of the non-uniformity pattern in the near zone

Table 1. Comparison of experimental tests results obtained with a standard probe B2S and phased array probes with two-element configuration

<table>
<thead>
<tr>
<th>Back-wall depth [mm]</th>
<th>Flat-bottomed hole depth [mm]</th>
<th>Diameter [mm]</th>
<th colspan="2">Standard probe B2S</th>
<th colspan="2">32-element phased array</th>
<th colspan="2">16-element phased array</th>
</tr>
<tr>
<th></th>
<th></th>
<th></th>
<th>Estimated diameter [mm]</th>
<th>dB increment with respect to back wall</th>
<th>Estimated diameter [mm]</th>
<th>dB increment with respect to back wall</th>
<th>Estimated diameter [mm]</th>
<th>dB increment with respect to back wall</th>
</tr>
</thead>
<tbody>
<tr>
<td>545</td>
<td>520</td>
<td>9</td>
<td>10</td>
<td>+20</td>
<td>10</td>
<td>+19</td>
<td></td>
<td></td>
</tr>
<tr>
<td>527</td>
<td>502</td>
<td>6</td>
<td>6</td>
<td>+28</td>
<td>6</td>
<td>+29</td>
<td></td>
<td></td>
</tr>
<tr>
<td>100</td>
<td>90</td>
<td>3</td>
<td>3.2</td>
<td>+25</td>
<td>5.9</td>
<td>+26</td>
<td>3.8</td>
<td>+21</td>
</tr>
<tr>
<td>100</td>
<td>85</td>
<td>5</td>
<td>6</td>
<td>+14</td>
<td>9.8</td>
<td>+17</td>
<td>7</td>
<td>+11</td>
</tr>
</tbody>
</table>

## 3. Computer model assessment
A first assessment of the implemented computer model was carried out comparing DGS curves of a standard commercial transducer 2 MHz - 24 mm diameter, see Figure 4, with the equivalent prediction of our model, see Figure 5. Some small discrepancy is present for the larger disk reflector in the near-field region (see Figure 3) but this is due to the different probe geometry. In fact, the commercial probe is circular while our prediction refers to a square probe of an equivalent size, 18 mm, to obtain the same near-field length. In all other cases the correspondence is excellent.

A second assessment has been carried out generating two sets of DGS curves: one for a 32-element 1.4 mm-pitch phased array probe working at 2.25 MHz and the other for a similar probe but with 16 elements.

Based on these DGS phased array diagrams, represented in Figures 6 and 7, a programme of experimental tests has been carried

![](./images/811794764151128064_4.jpg)

Figure 4. DGS curve for standard probe B2S

DGS curve for a square probe 18 x 18 mm operating at 2 MHz
longitudinal wave (equivalent to a circular probe of 24 mm diameter)

![](./images/811794764151128064_5.jpg)

Figure 5. DGS curve of a square standard probe equivalent to the previous one

![](./images/811794764151128064_6.jpg)

Figure 6. Experimental test results using DGS curve traced according to the mathematical model with 32-element phased array probe, 1.4 mm pitch, 2.25 MHz

![](./images/811794764151128064_7.jpg)

Figure 7. DGS curve for a 16-element phased array probe, 1.4 mm pitch working at 2.25 MHz

out. The test blocks used for these tests are cylindrical steel bars with diameters of 80 and 100 mm (see Figure 8) containing flat-bottomed holes (FBH) drilled into the circular undersides of the bars so that their ends are horizontal circles, while the probes are placed on the top circular faces of the bars (see Figure 9). The lengths of the blocks and the sizes of FBH are indicated in Table 1.

In the same Table are represented the estimated values determined with a standard B2S probe using a standard DGS curve and estimated values determined with a phased array probe using a DGS phased array curve traced by the proposed mathematical model in order to compare the results.

Looking at Table 1 and also Figure 6, we can observe that in the probe far field, regardless of whether it is a standard probe or a phased array probe, size estimations are quite good and comparable with each other, while if we work in the near field, in the case of the 32-element phased array probe and the last two defects, we have a mismatch consisting of an over-sizing of approximately a factor of 2.

This behaviour can be explained by taking into account that the near-field region is complex and not able to be simplified into a mathematical model but only by experimental methods (see Figure 3).

Looking at Table 1 and also Figure 7, we can observe that, with the 16-element probe, the two defects of lower depth are now estimated with a sufficient precision due to the fact that the probe near-field length is less than the defect depth.

![](./images/811794764151128064_8.jpg)

Figure 8. Some test blocks used for the experimental tests

![](./images/811794764151128064_9.jpg)

Figure 9. Schematic of test blocks illustrating the position of FBH and probe

## 4. Conclusions
The possibility to generate, by means of a computer model, a set of DGS curves for a complex probe such as a phased array probe, whose geometry changes with active element configuration, enables us to apply such a probe in the inspection of forged components and plate, based on a DGS curve for the estimation of defect severity.

Experimental verification has demonstrated that accuracy is quite good if defects are in the far-field region of the probe. If a defect is detected in the near-field region then, in order to avoid a defect over-estimation, it must be re-examined using a fewer number of active elements in order to reposition the defect in the probe far field.

Further work on enhancing the model is still in progress. The objectives are: (1) to increase the model accuracy prediction in the near-field region; and (2) to take account of probe focusing capabilities. Further work is foreseen for the future in order to expand the model also to side-drilled holes (SDH) as a reference calibration for defects in order to enhance precision of size estimation with angled probes and the DAC curve method.

## 5. Bibliography
1. V V Klyuev and G V Zusman, Nondestructive Testing and Diagnostics Handbook, Russian Society for Non-Destructive Testing and Technical Diagnostics, Moscow, Russia, Metrix Instrument Co, Houston, USA, 2004.
2. R S Sharpe, Ed, Research Techniques in Nondestructive Testing, Vol IV, Academic Press, London, 1980.
3. L Filipczynski, Z Pawlowski and J Wehr, Ultrasonic Methods of Testing Materials, Butterworths, London, 1966.
4. A S Birks and R E Green, Nondestructive Testing Handbook, Second Edition, ASNT, 1991.
5. J Krautkramer and H Krautkramer, Ultrasonic Testing of Materials, Springer-Verlag, 1990.