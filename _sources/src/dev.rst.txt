.. dev_signals:

=======
Signals
=======

*MatplotlibCurveWidget* provides the following PyQt signals:

``selectedIndicesUpdated[list, array]``: Update with selected points indices and list of selected points from lasso selector tool.

``xyposUpdated[float, float]``: Update the current mouse position in the figure data coordinate, represented by two float numbers for x and y positions.

.. _dev_slots:

=====
Slots
=====

*MatplotlibCurveWidget* provides the following PyQt slots:

Category I
----------

These slots are not exposed to the *Property Editor* column of *designer*:

.. automethod:: mpl4qt.widgets.mplcurvewidget.MatplotlibCurveWidget.add_curve
.. automethod:: mpl4qt.widgets.mplcurvewidget.MatplotlibCurveWidget.setLineID
.. automethod:: mpl4qt.widgets.mplcurvewidget.MatplotlibCurveWidget.setXData
.. automethod:: mpl4qt.widgets.mplcurvewidget.MatplotlibCurveWidget.setYData

Category II
-----------

These slots are exposed to the *Property Editor* column of *designer*:

.. automethod:: mpl4qt.widgets.mplcurvewidget.MatplotlibCurveWidget.setTightLayoutToggle
.. automethod:: mpl4qt.widgets.mplcurvewidget.MatplotlibCurveWidget.setFigureMTicksToggle
.. automethod:: mpl4qt.widgets.mplcurvewidget.MatplotlibCurveWidget.setFigureGridToggle
.. automethod:: mpl4qt.widgets.mplcurvewidget.MatplotlibCurveWidget.setLegendToggle
.. automethod:: mpl4qt.widgets.mplcurvewidget.MatplotlibCurveWidget.setLegendLocation
.. automethod:: mpl4qt.widgets.mplcurvewidget.MatplotlibCurveWidget.setFigureGridColor
.. automethod:: mpl4qt.widgets.mplcurvewidget.MatplotlibCurveWidget.setFigureWidth
.. automethod:: mpl4qt.widgets.mplcurvewidget.MatplotlibCurveWidget.setFigureHeight
.. automethod:: mpl4qt.widgets.mplcurvewidget.MatplotlibCurveWidget.setFigureDpi
.. automethod:: mpl4qt.widgets.mplcurvewidget.MatplotlibCurveWidget.setFigureXYlabelFont
.. automethod:: mpl4qt.widgets.mplcurvewidget.MatplotlibCurveWidget.setFigureXYticksFont
.. automethod:: mpl4qt.widgets.mplcurvewidget.MatplotlibCurveWidget.setFigureTitleFont
.. automethod:: mpl4qt.widgets.mplcurvewidget.MatplotlibCurveWidget.setFigureBgColor
.. automethod:: mpl4qt.widgets.mplcurvewidget.MatplotlibCurveWidget.setFigureXYticksColor
.. automethod:: mpl4qt.widgets.mplcurvewidget.MatplotlibCurveWidget.setLineColor
.. automethod:: mpl4qt.widgets.mplcurvewidget.MatplotlibCurveWidget.setMkEdgeColor
.. automethod:: mpl4qt.widgets.mplcurvewidget.MatplotlibCurveWidget.setMkFaceColor
.. automethod:: mpl4qt.widgets.mplcurvewidget.MatplotlibCurveWidget.setLineStyle
.. automethod:: mpl4qt.widgets.mplcurvewidget.MatplotlibCurveWidget.setMarkerStyle
.. automethod:: mpl4qt.widgets.mplcurvewidget.MatplotlibCurveWidget.setMarkerThickness
.. automethod:: mpl4qt.widgets.mplcurvewidget.MatplotlibCurveWidget.setLineLabel
.. automethod:: mpl4qt.widgets.mplcurvewidget.MatplotlibCurveWidget.setLineWidth
.. automethod:: mpl4qt.widgets.mplcurvewidget.MatplotlibCurveWidget.setMarkerSize
.. automethod:: mpl4qt.widgets.mplcurvewidget.MatplotlibCurveWidget.setFigureAutoScale
.. automethod:: mpl4qt.widgets.mplcurvewidget.MatplotlibCurveWidget.setFigureTitle
.. automethod:: mpl4qt.widgets.mplcurvewidget.MatplotlibCurveWidget.setFigureXlabel
.. automethod:: mpl4qt.widgets.mplcurvewidget.MatplotlibCurveWidget.setFigureYlabel
.. automethod:: mpl4qt.widgets.mplcurvewidget.MatplotlibCurveWidget.setXLimitMin
.. automethod:: mpl4qt.widgets.mplcurvewidget.MatplotlibCurveWidget.setXLimitMax
.. automethod:: mpl4qt.widgets.mplcurvewidget.MatplotlibCurveWidget.setYLimitMin
.. automethod:: mpl4qt.widgets.mplcurvewidget.MatplotlibCurveWidget.setYLimitMax


