User Interface
--------------

User interaction is handled by the Host system. The device sends messages about button states to the host, which then sends display data back to the device. 

.. note:: This is a very basic diagram for the interface. The full design doc will include more detail including the bootloader image verification process.

.. uml:: ../../assets/diagrams/sequence.puml


Demo Mode 
---------

Up-Rev will be delivering the firmware with a demo mode that proves out the interfaces of the device. To exercise the requirements the user will walk through the following steps:

1. Power on the device, and confirm the LCD displays a welcome message 
2. Connect ethernet and confirm the device displays the IP assigned by DHCP 
3. Connect to the device using Polypacket over tcp 

.. code:: bash 
    
    pip3 install polypacket 
    polypacket -i fcd_demo.yml -c connect tcp:<ip of device>:8020 


4. Press buttons and confirm that events are sent to the polypacket screen. 
5. Test memory by writing data to the nonvolatile memory, and reading it back 

.. code:: bash 

    >>> mem_write addr: 0x00, data: hello world! 
    >>> memread addr: 0x00, len: 12 

    The response packet should include the data written in the mem_write packet.


6.  

