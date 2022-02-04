Instructions
============

This project is the template for a software design document. The project uses ``Sphinx`` to generate documents from markdown or Restructured text. 


Using the Template
------------------

To use this template, fork/copy this repo into the Bitbucket project it is intended for. Then change it to meet the design needs of the project. The template pages provide examples and some Instructions on what information is needed. Make sure to follow the guidelines below and reference the `ENG-SW Design review.xlsx` checklist from sharepoint

.. note:: After copying the template you can remove this README file and replace it with one for the project


Guidelines
~~~~~~~~~~

Because no two projects are alike, there is no one size fits all template. Below are some Guidelines to make sure documentation is consistent and complete. 

#. All software components of the project must be documented 
#. All components must have a 'Development' section, complete with all of the information show in the example. If an item does not apply to the component, put N/A (do not remove items from the section)
    * Development Environment
    * Source Control 
    * List of all 3rd party libraries 
#. All embedded components must contain a 'Reusability' Section. 
    * List all devices connected to the MCU, and Indicate if there is an existing MrT module for it 
    * If there is not, check MrT to see if there are modules for any parts that perform the same function
    * If there are any, provide a justification to why they are not being used.
#. All components that a user will interact with directly must contain a 'User Interface' Section. 
    * For IO based interface (LEDS/Buttons) the Section must document the various states indicated by the LED and the operation of the buttons 
    * For any GUI the section must contain Mockups for all of the views and screens that will be used in the GUI. 


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




Building 
--------

Requirements 
~~~~~~~~~~~~

The easiest way to build this project is to use the Devcontainer:

#. Open this project in VS Code 
#. Click the green "Remote Window" button in the bottom left corner 
#. Click "Reopen in Container"

.. epigraph:: This will pull the latest uprev/sphinx image from docker hub, run it, and mount the project to it. This container has all of the required tools for building the project, and the VS Code extensions for creating diagrams and charts. 

The tools and extensions can also be installed manually in WSL:

.. code:: bash 

    sudo apt install python3-pip texlive latexmk texlive-science texlive-formats-extra plantuml
    pip3 install sphinx sphinxcontrib-plantuml sphinx-rtd-theme


Build Commands 
~~~~~~~~~~~~~~

The 2 most common use cases for building are HTML and pdf: 

.. code:: bash 

    make html

.. code:: bash 

    make latexpdf


The HTML format is good for presenting the documentation and hosting it on a server, and the pdf is better for delivering and distributing as a simple document




Why Sphinx?
-----------

Using ``Sphinx`` provides a lot of benefits over Word docs:


* **Accessibility and Project Evolution:**
    By keeping the design doc as plain text files allows it to live in the repo alongside the code for a project. This makes it more accessible and allows us to change it as the project evolves. The docs can be built by Jenkins, and changes now go through peer review in pull requests. At the end of a project it can be delivered to the customer to provide information on the development for any future improvements or maintanence. 

* **Visibility of design changes:**
    because the document is kept in source control, any changes to the design are subjected to reviews through pull requests. 

* **Flexibility:**
    At its core Sphinx is a templating tool. It has extensions for generating the documentation in a variety of formats including HTML, PDF, Docx, and confluence. This allows us to deliver docs to customers for whatever workflow they need. 

* **Effeciency:**
    While there is a slight learning curve to start, ``Sphinx`` removes a lot of the distractions of a Word processor. The author can focus on the relevant information and not get bogged down in the formatting and aesthetics of the document. `Sphinx` projects are structures like a software project, and everything can be done in a text editor. This is a more natural workflow for a software team. 

* **Cleaner Integration:**
    The traditional workflow requires a lot of tools that are not integrated. Powerpoint, drawio, lucidchart, plantuml, etc. It’s a lot of copy/pasting images and the sources for the diagrams are discarded. Sphinx has extensions which makes connects these tools and links directly to source materials. See below for more information on these extensions.

Extensions
~~~~~~~~~~

Sphinx has a number of extensions which make documentation easier to keep up to date. A few that are demonstrated in this template are:

* **plantuml:** 
    plantuml is a modeling language used often in our design documents for sequence diagrams, timing diagrams, use cases, and flow charts. The typical workflow is to write the UML, generate an image, and insert it into our documentation. This is a pain point because if you ever change the diagram, you have to repeat those steps. With the ``Sphinx`` plantuml extension, we can write the uml inline, or link to a `.puml` file, and it will render it into the document.

* **drawio:**
    Another tool used for diagraming is  the `draw.io extension for VS Code <https://marketplace.visualstudio.com/items?itemName=hediet.vscode-drawio>`_. Drawio is great for doing system diagrams and UI mockups (it has assets for all bootstrap design elements). File created with the `.dio.png` extension are png image files which can be linked in our documents, but they contain the drawio data, so the diagram can still be edited directly. 



.. the line below just forces a new page in the pdf rendering.

.. raw:: latex

    \newpage