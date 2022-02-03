Examples
========

This page just provides some reference examples for different rst directives. For more visit https://thomas-cokelaer.info/tutorials/sphinx/rest_syntax.html


*italic*

**bold**

`link to google <http://google.com>`_

notes
-----

.. note:: This is an example of the note directive 

.. warning:: this is a warning 

Code Snippets
-------------

.. code:: c 

    #include <stdio.h>

    int main() {
        printf("Hello, World!");
        return 0;
    }


Images
-----

.. figure:: ../assets/images/logo.png

    using 'figure' directive instead of 'image' lets you add a caption 

Math 
----

.. math::

    n_{\mathrm{offset}} = \sum_{k=0}^{N-1} s_k n_k


Tables 
------

+------------+------------+-----------+
| Header 1   | Header 2   | Header 3  |
+============+============+===========+
| body row 1 | column 2   | column 3  |
+------------+------------+-----------+
| body row 2 | Cells may span columns.|
+------------+------------+-----------+
| body row 3 | Cells may  | - Cells   |
+------------+ span rows. | - contain |
| body row 4 |            | - blocks. |
+------------+------------+-----------+



=====  =====  ======
   Inputs     Output
------------  ------
  A      B    A or B
=====  =====  ======
False  False  False
True   False  True
=====  =====  ======