SW Design Template
==================

This project is the template for a software design document. The project uses ``Sphinx`` to generate documents from markdown or Restructured text. 

|

Using the Template
------------------

To use this template, create a new repo in the bitbucket project that it is intended for and name it <projec-name>-sw-design. Copy the contents of this template to the new project and begin changing it to meet the design needs of the project. The template pages provide instructions for each section as well as examples of the various features of restructed text and sphinx directives. 


Requirements 
-----------

The easiest way to build this project is to use the Devcontainer:

#. Open this project in VS Code 
#. Click the green "Remote Window" button in the bottom left corner 
#. Click "Reopen in Container"

This will pull the latest MrT Development container from docker hub and mount the project to it. The MrT development container has all of the dependencies and extensions installed. 

The tools and extensions can also be installed manually in WSL:

.. code:: bash 

    sudo apt install python3-pip texlive latexmk texlive-science texlive-formats-extra plantuml
    pip3 install sphinx sphinxcontrib-plantuml sphinx-rtd-theme




Building 
--------

The 2 most common use cases for building are HTML and pdf: 

.. code:: bash 

    make html

.. code:: bash 

    make latexpdf


The HTML format is good for presenting the documentation and hosting it on a server, and the pdf is better for delivering and distributing as a simple document


Project Structure
~~~~~~~~~~~~~~~~~

This project is structure to split up text files and assets.

.. code:: text

    ├── _templates
    ├── assets
    ├── pages
    │   ├── embedded
    │   │   ├── development.rst
    │   │   ├── embedded.rst
    │   │   ├── reusability.rst
    │   │   ├── estimates.rst
    │   │   └── risk.rst
    │   ├── mobile_app
    │   │   ├──mobile_app.rst
    │   │   ├── development.rst
    │   │   ├── ui.rst
    │   │   ├── estimates.rst
    │   │   └── risk.rst
    │   └── system.rst
    ├── index.rst
    └──conf.py

* **/assets**
    The assets folder contains various assets (images, diagrams, etc) for the doc. 

* **/pages**
    This directory and subdirectory contains all of the pages/content for the dock.

    * **/embedded** contains files for the embedded device component of the design.
    * **/mobile_app** contains files for the mobile app component of the design. 

* **/index.rst** 
    This is the 'main' document file. typically it contains a small write up about the document, and then a ``toctree`` (Table of Contents tree) which is what includes all of the other pages. 

* **/conf.py**
    This is the configuration file used by sphinx to set themes and include various extensions. This is also where the name of the document is set. 

* **/_templates**
    This just contains template overrides for the base RTD theme to improve color scheme and formatting


Guidelines
----------

Because no two projects are alike, there is no one size fits all template. Below are some Guidelines to make sure documentation is consistent and complete. 

#. All software components of the project must be documented 
#. All components must have a 'Development' section, complete with all of the information show in the example. If an item does not apply to the component, put N/A (do not remove items from the section)
    * Development Environment
    * Source Control 
    * List of all 3rd party libraries 
#. All embedded components must contain a 'Reusability' Section. 
    * List all devices connected to the MCU, and Indicate if there is an existing MrT module for it 
    * If there is not, check MrT to see if there are modules for any parts that perform the same function
    * IF there are any, provide a justification to why they are not being used.
#. All components that a user will interact with directly must contain a 'User Interface' Section. 
    * For IO based interface (LEDS/Buttons) the Section must document the various states indicated by the LED and the operation of the buttons 
    * For any GUI the section must contain Mockups for all of the views and screens that will be used in the GUI. 






