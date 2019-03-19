# File: linked_panning.py
# 
# Example from bokeh web page:
# https://bokeh.pydata.org/en/latest/docs/user_guide/quickstart.html#userguide-quickstart
# Example demonstrating linked panning. Here changing
# one range of a plot causes the other plots to update
# 
# The toolbar is hidden, but the plots can still be panned.
# Click and drag, and see how their ranges are linked together

import numpy as np

from bokeh.layouts import gridplot
from bokeh.plotting import figure, output_file, show

# prepare some data
N = 100
x = np.linspace(0,4*np.pi, N)
y0 = np.sin(x)
y1 = np.cos(x)
y2 = np.sin(x) + np.cos(x)

# output to static HTML file
output_file("linked_panning.html")

# create a new plot
s1 = figure(width=250, plot_height=250, title=None)
s1.circle(x, y0, size=10, color="navy", alpha=0.5)

# create an additional plot and share both ranges
s2 = figure(width=250, height=250, x_range=s1.x_range, y_range=s1.y_range, title=None)
s2.triangle(x, y1, size=10, color="firebrick", alpha=0.5)

# create a third additional plot, sharing ranges with previouso ones
s3 = figure(width=250, height=250, x_range=s1.x_range, title=None)
s3.square(x,y2, size=10, color="olive", alpha=0.5)

# putthe subplots in a gridplot
p = gridplot([[s1,s2, s3]], toolbar_location=None)
# show results
show(p)