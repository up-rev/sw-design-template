User Interface
--------------


The device is controlled with the mode button, and the status is indicated by the LED. 

Button actions  
~~~~~~~~~~~~~~

.. uml:: ../../assets/diagrams/button.puml

LED states
~~~~~~~~~~

.. uml:: ../../assets/diagrams/led.puml

**Idle** 
    Device is in normal operating mode 

**Reading** 
    Device is taking a measurement. This takes 5 seconds and then returns to idle

**Pairing**
    Device is ready to pair with the mobile app 

**Low Battery** 
    Device battery is below 10%