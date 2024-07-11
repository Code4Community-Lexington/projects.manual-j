#### Project Kickoff: Explanations and Goals  
by April  
  
**What are we making?** A Manual-J calculator is a tool that takes in details about the layout and insulation of one's home and, given a design setpoint (max/min operable outdoor temps), outputs the required power capacity for an HVAC unit.  
  
**Why are we making it?** [Manual-J](https://www.acca.org/standards/technical-manuals/manual-j) is the name of a recognized ANSI standard. There are a number of software packages which can perform this calculation, including spreadsheets and mobile apps, but all require a subscription. The technical manual itself requires a call for a quote, clearly intended more for use by HVAC companies. However, the math behind the calculations are simple and a free-and-open-source solution could be used by anyone interested.  
  
**Why not leave it to HVAC companies?** Many companies when installing HVAC units will use rules of thumb and round up to the nearest, most available models. As many homes are switching from standard AC units to heat pumps, these overestimations are likely to continue, and this tool will give homeowners the ability to save money from a quick lookup of their home's needs.  
  
**Are there any free Manual-J Calculators?** There are actually, but they're all a nightmare to use. [Here](https://www.loadcalc.net/) is an online calculator that basically works as a spreadsheet where each possible option for insulation, window materials, etc is stuffed into a series of dropdown lists for which one must add the square footage of each surface type manually. This version only allows for two types of surfaces and gives confusing prompts such as "Door 2 NE: () sq. ft." to refer different parts of the home. **This project will focus much more on UI than on mathematics**. The ACCA has provided an abridged free spreadsheet that is somewhat more organized... for an excel spreadsheet. That is attached to this project under the name *MJ8ae*. I (April) will be looking through it to see if there are any big differences in how it calculates its loads from the basic formula for specific cases.
  
**How does the calculation work?** Our only concern is thermal leakage outside of the air-conditioned parts of the home. Under maximum conditions (say, 10 F in winter or 100 F in summer), thermal leakage will exactly match our HVAC unit's capacity in BTU's, meaning it will operate  
on a 100% duty cycle to maintain room temperature inside.  

Each unique type of surface on the exterior of the home (including the attic and the basement) will have an associated R-value rating its ability to insulate. Assuming simple conduction across a surface *i*: $\frac{\Delta Q_{i}}{A_{i}} = \frac{\Delta T}{R_{i}}$ where $\frac{\Delta Q_{i}}{A_{i}}$ is the heat loss per unit area, $R_{i}$ is the unique R-value to that surface, and $\Delta T$ is the temperature delta across the surface. In a detached home, that is the difference between the outdoor and indoor temperatures. But, for example, in an apartment, three of the four walls will have a temperature delta of effectively zero as they border air-conditioned rooms. These walls can be ignored for the purpose of this calculation.  

Thus, if an individual surface's contribution to the total heat loss is $\Delta Q_{i} = \frac{\Delta T}{R_{i}}\cdot A_{i}$ , then the total heat loss across all external surfaces can be found by $\Delta Q_{total} = \Delta T \cdot \sum\limits_{i} \frac{A_{i}}{R_{i}}$ . Pretty simple.  

One last note about R-values. When surfaces are in series (e.g. a double-paneled window) R-values of each individual ply can be summed together in the denominator of the above formula. When they're in parallel (e.g. a window surrounded by a brick wall), the total heat losses are summed up, just as we did above.  
  
**How do we find those R-values**  Insulation comes with an R-value, usually on the visible labeling where it's installed in homes (same for windows, usually). Unless the user was there when their home was installed or given some details by the builders, this might require a bit of guesswork, such as assuming the visible insulation used in the attic was also used in all the other walls whose insulation is not visibile. For other materials (floors, doors, wall exteriors), R-values can be either looked up or calculated based on material and thickness.  

To summarize, the following surfaces will need to be handled separately, along with their R-values (or material properties which can calculate R-value) and square-footage:  
- Wall Exteriors  
- Wall Insulation  
- Roof Exteriors  
- Roof Insulation  
- Ceilings  
- Doors  
- Glass Doors  
- Windows
- Sunlights (extra radiative heat condition)
- Floors
- Floor Insulation  
- Basements

That's a lot of information to prompt the user for, and it will need to be organized on our end before calculating. It would be best to have the user add individual items at a time, and prompt for more information based on how they answer, rather than combining every possible item into a spreadsheet. And maybe a checklist format will make sure the user doesn't forget to add, say, the attic into their calculation.  

**Next Steps:** I (April) plan to look more into these previously mentioned calculators to make sure my methods are accurate and to eventually set up a calculation function. The other things to tackle would be UI layout and the data structure to store all these inputs.   
