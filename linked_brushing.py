# File: linked_brushing.py
#
# Example from bokeh web page:
# https://bokeh.pydata.org/en/latest/docs/user_guide/quickstart.html#userguide-quickstart
# 
# The example demonstrates linked brushing by sharing
# a ColumnDataSource between two plots
#
import numpy as np
from bokeh.plotting import *
from bokeh.models import ColumnarDataSource

# prepare some data
N = 300
x = np.linspace(0, 4*np.pi, N)
y0 = np.sin(x)
y1 = np.cos(x)

# output to static HTML file
output_file("linked_brushing.html")

# Create a column data source for the plots to share
source = ColumnDataSource(data=dict(x=x, y0=y0, y1=y1))

TOOLS = "pan,wheel_zoom,box_zoom,reset,save,box_select,lasso_select"

# create a new plot and a renderer
left = figure(tools=TOOLS, width=350, height=350, title=None)
left.circle('x','y1', source=source)

# create another new plot and add a renderer
right = figure(tools=TOOLS, width=350, height=350, title=None)
right.circle('x','y1', source=source)

# put the subplots in a gridplot
p = gridplot([[left,right]])

# show the results
show(p)