# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Post/PostPlot.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Post/PostPlot
"""

from os import linesep
from logging import getLogger
from ._check import check_var, raise_
from ..Functions.get_logger import get_logger
from ..Functions.save import save
from ..Functions.copy import copy
from ..Functions.load import load_init_dict
from ..Functions.Load.import_class import import_class
from .PostMethod import PostMethod

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Post.PostPlot.run import run
except ImportError as error:
    run = error


from ._check import InitUnKnowClassError


class PostPlot(PostMethod):
    """Post-processing to do a plot which is a method of Output or other class if attribute is not None"""

    VERSION = 1

    # cf Methods.Post.PostPlot.run
    if isinstance(run, ImportError):
        run = property(
            fget=lambda x: raise_(
                ImportError("Can't use PostPlot method run: " + str(run))
            )
        )
    else:
        run = run
    # save and copy methods are available in all object
    save = save
    copy = copy
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        method=None,
        name="[]",
        param_list=-1,
        param_dict=-1,
        save_format="png",
        init_dict=None,
        init_str=None,
    ):
        """Constructor of the class. Can be use in three ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for pyleecan type, -1 will call the default constructor
        - __init__ (init_dict = d) d must be a dictionnary with property names as keys
        - __init__ (init_str = s) s must be a string
        s is the file path to load

        ndarray or list can be given for Vector and Matrix
        object or dict can be given for pyleecan Object"""

        if init_str is not None:  # Load from a file
            init_dict = load_init_dict(init_str)[1]
        if init_dict is not None:  # Initialisation by dict
            assert type(init_dict) is dict
            # Overwrite default value with init_dict content
            if "method" in list(init_dict.keys()):
                method = init_dict["method"]
            if "name" in list(init_dict.keys()):
                name = init_dict["name"]
            if "param_list" in list(init_dict.keys()):
                param_list = init_dict["param_list"]
            if "param_dict" in list(init_dict.keys()):
                param_dict = init_dict["param_dict"]
            if "save_format" in list(init_dict.keys()):
                save_format = init_dict["save_format"]
        # Set the properties (value check and convertion are done in setter)
        self.method = method
        self.name = name
        self.param_list = param_list
        self.param_dict = param_dict
        self.save_format = save_format
        # Call PostMethod init
        super(PostPlot, self).__init__()
        # The class is frozen (in PostMethod init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        PostPlot_str = ""
        # Get the properties inherited from PostMethod
        PostPlot_str += super(PostPlot, self).__str__()
        PostPlot_str += 'method = "' + str(self.method) + '"' + linesep
        PostPlot_str += 'name = "' + str(self.name) + '"' + linesep
        PostPlot_str += (
            "param_list = "
            + linesep
            + str(self.param_list).replace(linesep, linesep + "\t")
            + linesep
        )
        PostPlot_str += "param_dict = " + str(self.param_dict) + linesep
        PostPlot_str += 'save_format = "' + str(self.save_format) + '"' + linesep
        return PostPlot_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from PostMethod
        if not super(PostPlot, self).__eq__(other):
            return False
        if other.method != self.method:
            return False
        if other.name != self.name:
            return False
        if other.param_list != self.param_list:
            return False
        if other.param_dict != self.param_dict:
            return False
        if other.save_format != self.save_format:
            return False
        return True

    def as_dict(self):
        """Convert this object in a json seriable dict (can be use in __init__)"""

        # Get the properties inherited from PostMethod
        PostPlot_dict = super(PostPlot, self).as_dict()
        PostPlot_dict["method"] = self.method
        PostPlot_dict["name"] = self.name
        PostPlot_dict["param_list"] = (
            self.param_list.copy() if self.param_list is not None else None
        )
        PostPlot_dict["param_dict"] = (
            self.param_dict.copy() if self.param_dict is not None else None
        )
        PostPlot_dict["save_format"] = self.save_format
        # The class name is added to the dict for deserialisation purpose
        # Overwrite the mother class name
        PostPlot_dict["__class__"] = "PostPlot"
        return PostPlot_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.method = None
        self.name = None
        self.param_list = None
        self.param_dict = None
        self.save_format = None
        # Set to None the properties inherited from PostMethod
        super(PostPlot, self)._set_None()

    def _get_method(self):
        """getter of method"""
        return self._method

    def _set_method(self, value):
        """setter of method"""
        check_var("method", value, "str")
        self._method = value

    method = property(
        fget=_get_method,
        fset=_set_method,
        doc=u"""Full path of the plot method to call except Output (ex: "plot_2D_Data", "mag.meshsolution.plot_contour")

        :Type: str
        """,
    )

    def _get_name(self):
        """getter of name"""
        return self._name

    def _set_name(self, value):
        """setter of name"""
        check_var("name", value, "str")
        self._name = value

    name = property(
        fget=_get_name,
        fset=_set_name,
        doc=u"""Name of the plot to use when saving the figure after plotting

        :Type: str
        """,
    )

    def _get_param_list(self):
        """getter of param_list"""
        return self._param_list

    def _set_param_list(self, value):
        """setter of param_list"""
        if type(value) is int and value == -1:
            value = list()
        check_var("param_list", value, "list")
        self._param_list = value

    param_list = property(
        fget=_get_param_list,
        fset=_set_param_list,
        doc=u"""Dictionnary of parameters to pass to the plot method when executing it

        :Type: list
        """,
    )

    def _get_param_dict(self):
        """getter of param_dict"""
        return self._param_dict

    def _set_param_dict(self, value):
        """setter of param_dict"""
        if type(value) is int and value == -1:
            value = dict()
        check_var("param_dict", value, "dict")
        self._param_dict = value

    param_dict = property(
        fget=_get_param_dict,
        fset=_set_param_dict,
        doc=u"""Dictionnary of parameters to pass to the plot method when executing it

        :Type: dict
        """,
    )

    def _get_save_format(self):
        """getter of save_format"""
        return self._save_format

    def _set_save_format(self, value):
        """setter of save_format"""
        check_var("save_format", value, "str")
        self._save_format = value

    save_format = property(
        fget=_get_save_format,
        fset=_set_save_format,
        doc=u"""File format extension ("png", "svg", "eps") in which to save the figure. The PostPlot automatically saves the figure in the results folder. The user can specify a different folder by specifying "save_path"=path_str or not save the figure by specifying "save_path"=None in param_dict, if the plot_method enables it.

        :Type: str
        """,
    )
