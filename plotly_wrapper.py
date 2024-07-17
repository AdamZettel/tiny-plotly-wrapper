# plotly_wrapper.py

import plotly.graph_objects as go
import numpy as np

class PlotlyWrapper:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(PlotlyWrapper, cls).__new__(cls)
            cls._instance.fig = go.Figure()
            cls._instance.figsize = (800, 600)  # Default figsize
        return cls._instance

    def plot(self, x, y, label='', color=None):
        self.fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name=label, line=dict(color=color)))

    def scatter(self, x, y, label='', color=None):
        self.fig.add_trace(go.Scatter(x=x, y=y, mode='markers', name=label, marker=dict(color=color)))

    def bar(self, x, height, label='', color=None):
        self.fig.add_trace(go.Bar(x=x, y=height, name=label, marker=dict(color=color)))

    def hist(self, x, bins=None, label='', color=None):
        self.fig.add_trace(go.Histogram(x=x, nbinsx=bins, name=label, marker=dict(color=color)))

    def plot_3d(self, x, y, z, label='', color=None):
        self.fig.add_trace(go.Scatter3d(x=x, y=y, z=z, mode='markers', name=label, marker=dict(color=color)))

    def xlabel(self, xlabel):
        self.fig.update_layout(xaxis_title=xlabel)

    def ylabel(self, ylabel):
        self.fig.update_layout(yaxis_title=ylabel)

    def title(self, title):
        self.fig.update_layout(title=title)

    def xlim(self, xmin, xmax):
        self.fig.update_xaxes(range=[xmin, xmax])

    def ylim(self, ymin, ymax):
        self.fig.update_yaxes(range=[ymin, ymax])

    def legend(self):
        self.fig.update_layout(showlegend=True)

    def set_size(self, width, height):
        self.figsize = (width * 100, height * 100)  # Converting to Plotly's pixel format

    def show(self):
        self.fig.update_layout(width=self.figsize[0], height=self.figsize[1])
        self.fig.show()
        # Reset the figure after showing it
        self.fig = go.Figure()
