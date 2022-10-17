Reusability
----------- 

..  Mandatory Section for any embedded components

This section contains all of the peripheral parts in this subsystem and details about how well they align with Up-Rev's Reusability intitiative. 

.. If we are using a component that does not have an existing MrT module, check the library for existing alternatives that perform a similar function. document the alternatives and provide a note on why they are not being used. 

============ ==============    ===================  =========================================
Reusability Matrix
---------------------------------------------------------------------------------------------
**part**     **MrT Module**    **MrT Alternative**  **Notes**  
============ ==============    ===================  =========================================
STM32WB55    yes                n/a
HTS221       yes                n/a
LIS2DH12     No                 LSM6D               LSM6D does not have enough resolution 
                                                    for application          
============ ==============    ===================  =========================================


The table below is used to evaluate any new parts as candidates for creating a new module in MrT

..  Any part identified above as not having an MrT module must be added to the table below. Indicate is a new module is being created for that part, and give a reason why that choice was made.

============ ========================   =======================================================
New Module Candidates
-----------------------------------------------------------------------------------------------
**Part**     **Creating New Module?**   **Reason**  
============ ========================   =======================================================
LIS2DH12     No                         Existing source code is provided by ST and it is not 
                                        likely to be used again    
============ ========================   =======================================================

