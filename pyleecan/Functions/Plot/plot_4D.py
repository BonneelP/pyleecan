# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

from ...Functions.init_fig import init_fig
from ...definitions import config_dict

FONT_NAME = config_dict["PLOT"]["FONT_NAME"]
COLORMAP = config_dict["PLOT"]["COLOR_DICT"]["COLOR_MAP"]
FONT_SIZE_TITLE = config_dict["PLOT"]["FONT_SIZE_TITLE"]
FONT_SIZE_LABEL = config_dict["PLOT"]["FONT_SIZE_LABEL"]
FONT_SIZE_LEGEND = config_dict["PLOT"]["FONT_SIZE_LEGEND"]


def plot_4D(
    Xdata,
    Ydata,
    Zdata,
    Sdata,
    x_min=None,
    x_max=None,
    y_min=None,
    y_max=None,
    z_min=None,
    z_max=None,
    title="",
    xlabel="",
    ylabel="",
    zlabel="",
    xticks=None,
    yticks=None,
    xticklabels=None,
    yticklabels=None,
    fig=None,
    ax=None,
    is_logscale_x=False,
    is_logscale_y=False,
    is_logscale_z=False,
    is_disp_title=True,
    type="scatter",
    save_path=None,
    is_show_fig=None,
):
    """Plots a 4D graph

    Parameters
    ----------
    Xdata : ndarray
        array of x-axis values
    Ydata : ndarray
        array of y-axis values
    Zdata : ndarray
        array of z-axis values
    Sdata : ndarray
        array of 4th axis values
    colormap : colormap object
        colormap prescribed by user
    x_min : float
        minimum value for the x-axis (no automated scaling in 3D)
    x_max : float
        maximum value for the x-axis (no automated scaling in 3D)
    y_min : float
        minimum value for the y-axis (no automated scaling in 3D)
    y_max : float
        maximum value for the y-axis (no automated scaling in 3D)
    z_min : float
        minimum value for the z-axis (no automated scaling in 3D)
    z_max : float
        maximum value for the z-axis (no automated scaling in 3D)
    title : str
        title of the graph
    xlabel : str
        label for the x-axis
    ylabel : str
        label for the y-axis
    zlabel : str
        label for the z-axis
    xticks : list
        list of ticks to use for the x-axis
    fig : Matplotlib.figure.Figure
        existing figure to use if None create a new one
    ax : Matplotlib.axes.Axes object
        ax on which to plot the data
    is_logscale_x : bool
        boolean indicating if the x-axis must be set in logarithmic scale
    is_logscale_y : bool
        boolean indicating if the y-axis must be set in logarithmic scale
    is_logscale_z : bool
        boolean indicating if the z-axis must be set in logarithmic scale
    is_disp_title : bool
        boolean indicating if the title must be displayed
    type : str
        type of 3D graph : "stem", "surf", "pcolor" or "scatter"
    save_path : str
        full path including folder, name and extension of the file to save if save_path is not None
    is_show_fig : bool
        True to show figure after plot
    """

    # Set figure/subplot
    if is_show_fig is None:
        is_show_fig = True if fig is None else False

    # Set figure if needed
    if fig is None and ax is None:
        (fig, ax, _, _) = init_fig(fig=None, shape="rectangle")

    is_3d = False
    if type != "scatter":
        is_3d = True

    # Plot
    if type == "scatter":
        c = ax.scatter(
            Xdata,
            Ydata,
            c=Zdata,
            s=Sdata,
            marker="s",
            cmap=COLORMAP,
            vmin=z_min,
            vmax=z_max,
        )
        clb = fig.colorbar(c, ax=ax)
        clb.ax.set_title(zlabel, fontsize=FONT_SIZE_LEGEND, fontname=FONT_NAME)
        clb.ax.tick_params(labelsize=FONT_SIZE_LEGEND)
        for l in clb.ax.yaxis.get_ticklabels():
            l.set_family(FONT_NAME)
        if xticks is not None:
            ax.xaxis.set_ticks(xticks)
            ax.set_xticklabels(xticklabels)
        if yticks is not None:
            ax.yaxis.set_ticks(yticks)
            ax.set_yticklabels(yticklabels)

    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)

    if is_logscale_x:
        ax.xscale("log")

    if is_logscale_y:
        ax.yscale("log")

    if is_disp_title:
        ax.set_title(title)

    if is_3d:
        for item in (
            [ax.xaxis.label, ax.yaxis.label, ax.zaxis.label]
            + ax.get_xticklabels()
            + ax.get_yticklabels()
            + ax.get_zticklabels()
        ):
            item.set_fontsize(FONT_SIZE_LABEL)
    else:
        for item in (
            [ax.xaxis.label, ax.yaxis.label]
            + ax.get_xticklabels()
            + ax.get_yticklabels()
        ):
            item.set_fontsize(FONT_SIZE_LABEL)
            item.set_fontname(FONT_NAME)
    ax.title.set_fontsize(FONT_SIZE_TITLE)
    ax.title.set_fontname(FONT_NAME)

    if save_path is not None:
        fig.savefig(save_path)
        plt.close()

    if is_show_fig:
        fig.show()
