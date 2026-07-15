# Nesting in the Evaluation of System Readiness for Complex Systems of Emerging Technologies

Michael Knaggs, Dennis Harkreader, Alfred Unione, John Oelfke, John Ramsey, Dale Keairns, Brian Sauser, *IEEE Senior Member*, and Bradley Atwater

Abstract—This paper analyzes the impact of nesting assumptions on the calculated system readiness for an integrated complex system that includes multiple subsystem components. In particular, it focuses on the net impact of calculating the system readiness of a subsystem of technology components; calculating an equivalent technology readiness level (TRL) for the subsystem treated as a single component technology; and including this TRL and subsystem interfaces in a Systems Readiness Assessment (SRA) for a larger system. The SRA methodology used in this evaluation has been demonstrated previously in several Department of Defense (DoD) applications and recently in a DOE application. The process for converting an SRL to a single equivalent TRL is based on methodology described in a handbook on SRA applications issued by the National Security Agency.

The analysis concludes that nesting assumptions can have a significant impact on the estimated readiness of a larger system. However, the analysis also concludes that equality, equivalence, and consistency in the identification and aggregation of technologies into technology subsystems (parity) can be used to provide consistent and comparable evaluations of system readiness that are needed in the development of complex system designs and for effectively tracking progress toward system readiness goals. The result is a potentially powerful and pragmatic approach for focusing management attention on critical elements of the R&D life cycle and supporting decisions on R&D investments.

Index Terms— Systems Readiness Level (SRL); Technology Readiness Level (TRL); Integration Readiness Level (IRL); Advanced Combustion and Carbon Capture (ACCC) system

## I. INTRODUCTION

System Readiness Assessment (SRA) methods have been demonstrated to be useful for understanding the development status of complex systems of emerging technologies in Department of Defense (DoD) [1-3] and Department of Energy (DOE) [4] applications. SRA methods provide a basis for assessing the current readiness of systems under development, a basis for tracking progress of system development, and a means of identifying critical and lagging component technologies that impact system readiness [5]. One aspect of SRA methodology that can impact the resulting projections of system readiness is the level at which component technologies are defined. The decision on where to draw the boundaries for complex integrated systems that include multiple components is important to the conduct of an SRA [6]. Nesting—the treatment of a subsystem of components as a single component technology in an SRA evaluation—is often used. An advanced technology that includes multiple components may be treated as a subsystem with these components evaluated as a single measure of technology readiness [7]. Nesting is also used where a legacy technology consisting of multiple contributing technologies is used in an SRA evaluation.

Nesting could have considerable value for SRA applications in complex DOE energy systems such as commercial-scale demonstrations of advanced energy systems in which significant investments are required to scale technologies and integrate them into larger systems. SRA is typically used to estimate progress toward achieving the objectives of such demonstrations of integrated emerging technologies as part of the design of larger systems [8]. When a technology that is part of a larger system is itself composed of contributing technology components that are under development, it is often convenient to treat the set of contributing technologies as a single subsystem and a single component in the larger system SRA. By extension, nesting can also be used to compare emerging technologies for use in system applications for which design choices have not yet been made for integrating emerging and legacy technologies. An SRA would be performed for each technology subsystem that would then be treated as a single component in an otherwise identical system. Such a comparison could be useful for decision-making when comparing two subsystems.

---

KeyLogic Systems, Inc.'s contributions to this work were funded by the National Energy Technology Laboratory under the Mission Execution and Strategic Analysis contract (DE-FE0025912) for support services.

Michael Knaggs is with the Department of Energy at the National Energy Technology Laboratory, Morgantown, WV 26505 USA (email: michael.knaggs@netl.doe.gov)

Dennis Harkreader is with KeyLogic Systems, Inc., Morgantown, WV 26505 USA (email: dennis.harkreader@netl.doe.gov)

Alfred Unione is with KeyLogic Systems, Inc., Morgantown, WV 26505 USA (email: aunione@keylogic.com)

John Oelfke is with KeyLogic Systems, Inc., Morgantown, WV 26505 USA (email: joelfke@keylogic.com)

John Ramsey is with KeyLogic Systems, Inc., Morgantown, WV 26505 USA (email: jramsey@keylogic.com)

Dale Kearns is with Deloitte, Inc., Pittsburgh, PA 15220 USA (email: dale.keairns@netl.doe.gov)

Brian Sauser is with the Jim McNatt Institute for Logistics Research at the University of North Texas, Denton, TX 76203 USA (email: brian.sauser@unt.edu)

Bradley Atwater is with Lockheed Martin Rotary & Mission Systems, Moorestown, NJ 08057 USA (bradley.t.atwater@lmco.com)

978-1-5090-4623-2/17/$31.00 ©2017 IEEE
978-1-5090-4623-2/17/$31.00 ©2017 IEEE

## II. DEFINING THE NESTING PROCESS

Nesting is a process for tiered treatment of technology components in an evaluation of system readiness. The nesting process treats a subset of component technologies in a system or subsystem as a single entity in the SRL calculation. In the nesting process, the set of technology components comprising the subsystem is carefully identified, the TRL for each component in the subsystem is estimated, and the IRL for each internal¹ technology interface is estimated.

An SRL for the subsystem is calculated and converted to an equivalent TRL for the subsystem so it can be treated as a single component technology. IRLs are then estimated for each identified² interface between the subsystem and the rest of the system, and an SRL calculation is performed for the full system with the subsystem treated as a single component technology. Graphical examples of the nesting process are shown in Figures 1 and 2. Figure 1 shows a generic system composed of eight (8) component technologies, while Figure 2 shows the same system with four (4) technologies treated as a single technology component (nested).

![](./images/813130752106430466_1.jpg)

Figure 1. Composite SRL Calculation without Nested Subsystem

![](./images/813130752106430466_2.jpg)

Figure 2. Composite SRL Calculation with Nested Subsystem

In the nesting process, each of the technology components comprising the nested subsystem are evaluated in terms of their current level of technology development, or TRL, and the maturity of their interfaces with other technology components, or IRLs. At this point, a (System Readiness Level) SRL for the subsystem is calculated and converted to an equivalent TRL as if the entire subsystem were a single component (Figure 2, ETRLₐ). In this way a single TRL for the subsystem is calculated, and with the maturities of the interfaces between the subsystem and the other component technologies characterized (IRLₐ,₅, IRLₐ,₆), an SRL for the full system is calculated.

## III. WHEN NESTING IS POTENTIALLY BENEFICIAL

Nesting is most effective when the principles and methods of SRA are incorporated into a multi-tiered technology development process for complex system applications.

For advanced energy systems, nesting provides a capability to focus on the development of core technologies—such as alternative-fueled combustion turbines or carbon capture processes—and develop them to an adequate level of technology readiness prior to integrating them into the design of a commercial-scale demonstration project. The Government Accountability Office's current best practices guide for technology readiness assessment, based on historical data on cost and schedule compliance for systems projects, concluded that emerging technologies should not be integrated with system designs prior to reaching the prototype stage of technology maturity (TRL=7). Nesting provides an opportunity to streamline the design development process where the functional basis for technology performance can be validated in subsystem tests and used to support more efficient full system design development.

Where a commercial-scale application includes multiple subsystems of mature technologies for which a high state of technology readiness has already been achieved, these legacy subsystems can be treated as single component technologies in an SRA. Used in this way, the nesting process simplifies the mathematics of the system readiness model, while increasing the focus on less mature technologies or interfaces.

For major first-of-a-kind technology-driven projects in which Critical Technology Elements (CTE) comprising multiple emerging core technologies have been identified,³ nesting provides a basis for assessing CTE technology readiness and treating it as a single technology component in the overall system SRA.

## IV. AN EXAMPLE OF NESTED SRL CALCULATION FOR ADVANCED FOSSIL ENERGY TECHNOLOGY

An example of the nesting process for an advanced fossil energy technology highlights both the value of nesting as an analytical convenience and the problems that can result from its use. This example considers a power plant that includes an advanced technology that provides the functions of

---
¹ Internal interfaces consist of those interfaces that involve only the technologies that are considered part of the subsystem.
² External interfaces consist of those interfaces that involve only the technologies that are external to the subsystem. Each external interface is defined between the subsystem (treated as a single entity) and a specific external technology.
³ *DOD Technology Readiness Assessment Deskbook*, Updated July 2009, defines a technology element as critical when "the system being acquired depends on this technology element to meet operational requirements (with acceptable development cost and schedule and with acceptable production and operation costs) and if the technology element or its application is either new or novel, or in an area that poses major technological risk during design or demonstration."

combustion and carbon capture in a single integrated process.
This Advanced Combustion and Carbon Capture (ACCC) system could be incorporated into advanced power plant system designs to achieve highly efficient carbon capture to meet DOE's carbon management objectives for new plant systems.
A digraph⁴ of the total power system, with components of the ACCC included, is shown in Figure 3⁵.

![](./images/813130752106430466_3.jpg)

Figure 3. Digraph of ACCC Subsystem

To implement the nesting process, we must first perform an SRL calculation for the subsystem. A digraph was developed defining the subsystem boundaries such that only components specific to the functioning of the ACCC are included. This digraph, shown in Figure 3, was used to calculate a composite SRL score for the ACCC subsystem. In addition, the digraph in Figure 4 was used to identify all interfaces between the ACCC subsystem and the rest of the power plant system that must be characterized and scored in a nested composite SRL model of the plant system.

![](./images/813130752106430466_4.jpg)

Figure 4. Digraph of Power Plant System including Advanced Combustion/Carbon Capture (ACCC) Technology

The SRL calculation for the ACCC subsystem—including component SRL contributions and the composite SRL score— is shown in Figure 5. The NSA handbook recommended using an SRL Translation Model that translates composite SRL values (between 0 and 1) to whole numbers consistent with
TRL and IRL scaling for ease of interpretation. The SRL Translation Model utilizes the architecture of an SRA model (i.e., the relationship of active nodes and edges in the IRL matrix and TRL vector) to translate SRL scores into a set of ETRL score ranges. In a nested SRA calculation, the ETRL functions in the same way as a TRL does, and the maturity of its interfaces with other system technology components can then be used to calculate the SRL for the system.

![](./images/813130752106430466_5.jpg)

Figure 5. SRL Model and Composite SRL (SRLc) Calculation for ACCC Subsystem

The ACCC composite SRL score of 0.28 from Table I maps to an equivalent TRL score of 4 for the ACCC subsystem.

<table>
  <thead>
    <tr>
      <th colspan="7">TABLE I</th>
    </tr>
    <tr>
      <th colspan="7">SRL TRANSLATION TABLE SPECIFIC TO THE ACCC SUBSYSTEM</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>TRL²</td>
      <td>IRL²</td>
      <td>Composite SRL Score @ TRL Level</td>
      <td>Lower Composite SRL Range (Midpoint between Levels)</td>
      <td>Composite SRL Range for ETRL</td>
      <td>ETRL¹</td>
    </tr>
    <tr>
      <td>9</td>
      <td>9</td>
      <td>1.000</td>
      <td>0.912</td>
      <td>0.912 - 1.000</td>
      <td>9</td>
    </tr>
    <tr>
      <td>8</td>
      <td>8</td>
      <td>0.824</td>
      <td>0.743</td>
      <td>0.743 - 0.911</td>
      <td>8</td>
    </tr>
    <tr>
      <td>7</td>
      <td>7</td>
      <td>0.663</td>
      <td>0.592</td>
      <td>0.592 - 0.742</td>
      <td>7</td>
    </tr>
    <tr>
      <td>6</td>
      <td>6</td>
      <td>0.520</td>
      <td>0.456</td>
      <td>0.456 - 0.591</td>
      <td>6</td>
    </tr>
    <tr>
      <td>5</td>
      <td>5</td>
      <td>0.392</td>
      <td>0.337</td>
      <td>0.337 - 0.455</td>
      <td>5</td>
    </tr>
    <tr>
      <td>4</td>
      <td>4</td>
      <td>0.281</td>
      <td>0.234</td>
      <td>0.234 - 0.336</td>
      <td>4</td>
    </tr>
    <tr>
      <td>3</td>
      <td>3</td>
      <td>0.186</td>
      <td>0.147</td>
      <td>0.147 - 0.233</td>
      <td>3</td>
    </tr>
    <tr>
      <td>2</td>
      <td>2</td>
      <td>0.108</td>
      <td>0.077</td>
      <td>0.077 - 0.146</td>
      <td>2</td>
    </tr>
    <tr>
      <td>1</td>
      <td>1</td>
      <td>0.046</td>
      <td>0.000</td>
      <td>0.000 - 0.076</td>
      <td>1</td>
    </tr>
    <tr>
      <td colspan="6">ETRL³ = 4</td>
    </tr>
    <tr>
      <td colspan="6">1 – Process based on SRL Translation Model defined in NSA System Readiness Assessment (SRA) Engineering Handbook (27 June 2014); here defined as the Equivalent TRL (ETRL)</td>
    </tr>
    <tr>
      <td colspan="6">2 – Range mapping model assumes that all subsystem technologies have the same TRL (1st column) and their interfaces have the same IRL (2nd column)</td>
    </tr>
    <tr>
      <td colspan="6">3 – Based on Best Estimate Composite SRL = .28 calculated for ACCC Subsystem (Figure C)</td>
    </tr>
  </tbody>
</table>

⁴ Old Dominion University's Computer Science Department defines digraph as “…short for directed graph, and it is a diagram composed of points called vertices (nodes) and arrows called arcs going from a vertex to a vertex.” Digraphs are useful for expressing the essential features of a system or engineering flow sheet that are relevant to an SRL calculation. For purposes of describing technologies that are combined in power systems or other system applications, each node is a distinct technology and each edge an interface between that technology and another. The direction of the edge is also important since some interfaces are unidirectional (e.g., steam flow to a turbine) while others are bi-directional (e.g., a sensor/control circuit).

⁵ Digraphs are useful in SRA calculations for complex power plant systems and subsystems. Once a system or subsystem is represented as a digraph, the digraph can immediately be transformed into a vector of TRLs (nodes) and a matrix of IRLs (edges and their nodal connectedness). Given the vector of TRLs and the matrix of IRLs, values for each can be determined, and through matrix multiplication, component SRLs and a composite SRL calculated.

Figure 6 shows how the ACCC is treated as a single technology in an advanced power system SRL model. Components that have been nested in a single equivalent technology (TRL3) are no longer shown directly in the model (highlighted rows 4–9). A composite SRL for the system is calculated using a single equivalent TRL for the ACCC and IRL for each of the characterized interfaces shown in Figure 4. Notably, since the ACCC has not been demonstrated as part of a larger power production process, the equivalent IRL in the nested SRL model is scored quite low. A composite SRL score of 0.51 for the power plant system is calculated using the nested SRL model in Figure 6.

![](./images/813130752106430466_6.jpg)

Figure 6. SRL Calculation for Advanced Power System with Nested ACCC

For comparison, a composite SRL calculation was made for the advanced power system in which the ACCC was not treated as a single nested subsystem. In this SRL calculation, the ACCC components were considered as separate technologies. Their individual interfaces with other advanced power system technologies (marked E in Figure 3) were modeled and scored using the same assumptions with respect to interface maturity. Figure 7 shows the composite SRL model for the un-nested system. A composite SRL score of 0.42 was calculated.

![](./images/813130752106430466_7.jpg)

Figure 7. SRA Model for Composite Un-nested Advanced Fossil Power System

The difference in SRL scores between the nested (Figure 6) and not nested (Figure 7) models could be significant if system readiness is used as part of a technology “stage gate” approach to project funding. Hence, it is reasonable to ask what caused the difference. Table II shows that the differences in calculated scores may be traceable to the number of technologies and interfaces included in each model. Notably, the number of nodes and edges included in the nested model are significantly fewer than those included in the un-nested model. This loss of nodes and edges in the graph suggests that—from a mathematical viewpoint—these are different systems that should produce different composite scores, even with the same assumptions.

A sensitivity evaluation was performed to better understand why the nested and un-nested models produced significantly different composite SRLs. A version of the un-nested SRL model was evaluated assuming that all of the internal interfaces (i.e., the IRLs for interfaces 3-4, 3-5, 3-6, 5-6, 6-7, 3-8, 7-8 and 7-9) and internal technologies (i.e., TRLs 4, 5, and 6) of the ACCC were fully mature⁶. The composite SRL score for this sensitivity model was comparable to the nested SRL model result, suggesting that the nesting process introduced simplifications from the full system SRL model that tended to push the composite SRL score higher due to a reduction in the number of technologically less mature components and component interfaces that were included in the calculation. The sensitivity calculation also shows that if the ACCC subsystem were developed as a core technology to a high state of maturity, its contribution to the full system SRL score would be correctly assessed with the nested model.

## V. HOW NESTING CAN BE EFFECTIVELY USED

The above analysis shows that nesting can significantly affect measured composite SRL scores. However, the above analysis does not reflect the reality of how technologies destined for use in complex system applications are technologically matured. For most system applications, core technologies are developed independent of the final system application up to a certain point of maturity. For the ACCC example shown, it is reasonable to assume that the ACCC subsystem would be tested independently and its component technologies and internal interfaces matured to the maximum extent possible using independent (subsystem) tests and demonstrations. Therefore, a nested model of the total power system may in fact provide a more useful assessment of system readiness for evaluating progress and proposed R&D investments.

Figure 8 illustrates a set of subsystems for an advanced power system with carbon capture such that the system can be thought of as an integrated set of subsystems. Both the carbon capture subsystem and its interfaces with other subsystems are identified in Figure 8. This figure points to a consistent method of defining the hierarchy of system elements (e.g., technology, component, subsystem, system, etc.) in which elements at each level can be nested to assess the readiness of elements at the next level with a fully nested model used to assess system readiness for the intended application.

![](./images/813130752106430466_8.jpg)

Figure 8. Consistently Defined Subsystems for Advanced Fossil Energy Power System

Enforcing such a hierarchy during the readiness assessment process (achieving parity) leads to consistent estimates of system readiness with the added advantage that the system readiness models can be used to drill down and uncover key vulnerabilities in the technological maturity of lower-level elements (for example, a high level of system dependence on a single technology at an early stage of technology maturation). Achieving parity also enables comparison of systems in which one or more subsystems or technology components are changed or modified. This provides a ready basis for comparing several emerging technologies that could be used in the same system application. This capability can be useful when planning investments in technology maturation, comparing technologies for systems applications, and identifying key areas that require additional R&D focus and resources.

## VI. CONCLUSION

Nesting, the treatment of a subsystem of components as a single component technology in an SRA evaluation, is often used where a technology—that itself consists of multiple contributing technologies—is under development for use in a system application. Nesting of components can significantly impact calculated component SRL scores, and this fact must be considered when developing system SRL models to avoid introducing misleading conclusions. Careful attention to development of system architecture and use of parity in the development of system, subsystem, and component hierarchies can result in SRA models that are effective for understanding subsystem and component technology development needs and for tracking technology development progress. SRA models designed with consistent hierarchy and parity protocols can be used to compare the system readiness of alternative designs intended for the same application, and are a potentially useful tool for assessing alternative technology developments in DOE programs.

However, how subsystem boundaries in a system are defined and how the ‘technologies’ within a system are selected is important when using nesting as part of a tiered system readiness approach. Further testing and sensitivity analysis are needed to determine how variations in the way the boundaries are set at the system, subsystem, and technology component levels affect the impact of nesting on SRL scores (e.g., what happens to the nested SRL when changes are made to the boundaries of the system to either include or exclude one or more of the interfacing technologies).

## REFERENCES

[1] B. Sauser, J. Ramirez-Marquez, R. Magnaye, and W. Tan, "System Maturity Indices for Decision Support in the Defense Acquisition Process," presented at the Defense Acquisition Research Symposium, Monterey, CA, 2008.

[2] N. Azizian, D. Rico, S. Sarkani, and T. Mazzuchi, "The current state of DOD's technology readiness assessment (TRA) practice and its impact on system quality and program outcome," presented at the Conference on System Engineering Research, Hoboken, NJ, 2010.

[3] A. Tetlay and P. John, "Determining the Lines of System Maturity, System Readiness and Capability Readiness in the System Development Lifecycle," in *Conference on Systems Engineering Research*, Loughborough University (UK), 2009.

[4] M. Knaggs, J. Ramsey, A. Unione, D. Harkreader, J. Oelfke, D. Keairns, *et al.*, "Application of systems readiness level methods in advanced fossil energy applications," in *Conference on Systems Engineering Research*, Hoboken, NJ, 2014, pp. 497-506.

[5] B. Sauser, J. Ramirez-Marquez, R. Magnaye, and W. Tan, "A Systems Approach to Expanding the Technology Readiness Level within Defense Acquisition," *International Journal of Defense Acquisition Management*, vol. 1, pp. 39-58, 2008.

[6] M. Austin, J. Zakar, D. York, L. Pettersen, and E. Duff, "A Systems Approach to the Transition of Emergent Technologies into Operational Systems – Herding the Cats, the Road to Euphoria and Planning for Success " presented at the International Conference of the International Council on Systems Engineering, Netherlands, 2008.

[7] B. Atwater and J. Udzdzinski, "Wholistic Sustainment Maturity: The Extension of System Readiness Methodology across all Phases of the Lifecycle of a Complex System," in *Procedia Computer Science*, 2014, pp. 601-609.

[8] E. Forbes, R. Volkert, P. Gentile, and K. Michaud, "Implementation of a Methodology Supporting a Comprehensive System-of-Systems Maturity Analysis for Use by the Littoral Compact Ship Mission Module Program," in *Acquisition Research Symposium*, Monterey, CA, 2009.

## DISCLAIMER

"This report was prepared as an account of work sponsored by an agency of the United States Government. Neither the United States Government nor any agency thereof, nor any of their employees, makes any warranty, express or implied, or assumes any legal liability or responsibility for the accuracy, completeness, or usefulness of any information, apparatus, product, or process disclosed, or represents that its use would not infringe privately owned rights. Reference herein to any specific commercial product, process, or service by trade name, trademark, manufacturer, or otherwise does not necessarily constitute

or imply its endorsement, recommendation, or favoring by the United
States Government or any agency thereof. The views and opinions of
authors expressed herein do not necessarily state or reflect those of the
United States Government or any agency thereof."