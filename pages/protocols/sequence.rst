Sequence Diagram
================

Include Sequence diagrams that illustrate the transactions between components of the system. With `Plantuml <https://plantuml.com/sequence-diagram>`_ you can add these directly in the document or specify and external `.puml` file to render

.. uml::

    @startuml
    participant Participant as Foo
    actor       Actor       as Foo1
    boundary    Boundary    as Foo2
    control     Control     as Foo3
    entity      Entity      as Foo4
    database    Database    as Foo5
    collections Collections as Foo6
    queue       Queue       as Foo7
    Foo -> Foo1 : To actor 
    Foo -> Foo2 : To boundary
    Foo -> Foo3 : To control
    Foo -> Foo4 : To entity
    Foo -> Foo5 : To database
    Foo -> Foo6 : To collections
    Foo -> Foo7: To queue
    Foo7 -> 00 : Back to Actor
    @enduml