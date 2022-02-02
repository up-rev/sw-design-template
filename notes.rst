
This project is the template for a software design document. The project uses the ``Sphinx`` project to generate documents from markdown or Restructured text. This process will have a bit of a learning curve but it solves a lot of problems with our current process. 

We create design documents at the beginning of projects, and they are typically never seen again. They are not typically updated as the project evolves, and by the end of a project lifecycle they are no longer accurate to the project. This is largely because they are considered to be a planning tool, and not a part of the actual project. But if kept up-to-date, these documents contain a lot of very usefule information for the customer and for the software team if a project ever changes hands or comes back to us for updates. 

Using ``Sphinx`` provides a lot of benefits over Word docs that can solve these problems:

* **Accessibility and Project Evolution:**
    By keeping the design doc as plain text files allows it to live in the repo alongside the code for a project. This makes it more accessible and allows us to change it as the project evolves. The docs can be built by Jenkins, and changes now go through peer review in pull requests. At the end of a project it can be delivered to the customer to provide information on the development for any future improvements or maintanence. 

* **Flexibility:**
    At its core Sphinx is a templating tool. It has extensions for generating the documentation in a variety of formats including HTML, PDF, Docx, and confluence. This allows us to deliver docs to customers for whatever workflow they need. 

* **Effeciency:**
    While there is a slight learning curve to start, ``Sphinx`` removes a lot of the distractions of a Word processor. The author can focus on the relevant information and not get bogged down in the formatting and aesthetics of the document.,

Extensions
----------

Sphinx has a number of extensions which make documentation easier to keep up to date. A few that are demonstrated in this template are:

* **plantuml:** 
    plantuml is a modeling language used often in our design documents for sequence diagrams, timing diagrams, use cases, and flow charts. The typical workflow is to write the UML, generate an image, and insert it into our documentation. This is a pain point because if you ever change the diagram, you have to repeat those steps. With the ``Sphinx`` plantuml extension, we can just provide a path to the uml file, and it will render it into the document, so it is automatically updated when the UML is changed.  

* **drawio:**
    Another tool used for diagraming is `draw.io <http://draw.io>`_. Drawio is great for doing system diagrams and UI mockups (it has assets for all bootstrap design elements) This typically has a similar workflow of creating the diagram in their tool, exporting an image, and inserting it into the doc. But by using the VS code extension (or their desktop app) we can create `.dio.png` files. These are png image files which can be linked in our documents, but they contain the drawio data, so the diagram can still be edited directly. 