# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Simulation/Input.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Simulation/Input
"""

from os import linesep
from logging import getLogger
from ._check import check_var, raise_
from ..Functions.get_logger import get_logger
from ..Functions.save import save
from ..Functions.copy import copy
from ..Functions.load import load_init_dict
from ..Functions.Load.import_class import import_class
from ._frozen import FrozenClass

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Simulation.Input.gen_input import gen_input
except ImportError as error:
    gen_input = error

try:
    from ..Methods.Simulation.Input.comp_axes import comp_axes
except ImportError as error:
    comp_axes = error


from ..Classes.ImportMatrixVal import ImportMatrixVal
from numpy import ndarray
from numpy import array, array_equal
from ._check import InitUnKnowClassError
from .ImportMatrix import ImportMatrix


class Input(FrozenClass):
    """Starting data of the simulation"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Simulation.Input.gen_input
    if isinstance(gen_input, ImportError):
        gen_input = property(
            fget=lambda x: raise_(
                ImportError("Can't use Input method gen_input: " + str(gen_input))
            )
        )
    else:
        gen_input = gen_input
    # cf Methods.Simulation.Input.comp_axes
    if isinstance(comp_axes, ImportError):
        comp_axes = property(
            fget=lambda x: raise_(
                ImportError("Can't use Input method comp_axes: " + str(comp_axes))
            )
        )
    else:
        comp_axes = comp_axes
    # save and copy methods are available in all object
    save = save
    copy = copy
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        time=None,
        angle=None,
        Nt_tot=2048,
        Nrev=1,
        Na_tot=2048,
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
            if "time" in list(init_dict.keys()):
                time = init_dict["time"]
            if "angle" in list(init_dict.keys()):
                angle = init_dict["angle"]
            if "Nt_tot" in list(init_dict.keys()):
                Nt_tot = init_dict["Nt_tot"]
            if "Nrev" in list(init_dict.keys()):
                Nrev = init_dict["Nrev"]
            if "Na_tot" in list(init_dict.keys()):
                Na_tot = init_dict["Na_tot"]
        # Set the properties (value check and convertion are done in setter)
        self.parent = None
        self.time = time
        self.angle = angle
        self.Nt_tot = Nt_tot
        self.Nrev = Nrev
        self.Na_tot = Na_tot

        # The class is frozen, for now it's impossible to add new properties
        self._freeze()

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        Input_str = ""
        if self.parent is None:
            Input_str += "parent = None " + linesep
        else:
            Input_str += "parent = " + str(type(self.parent)) + " object" + linesep
        if self.time is not None:
            tmp = self.time.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            Input_str += "time = " + tmp
        else:
            Input_str += "time = None" + linesep + linesep
        if self.angle is not None:
            tmp = self.angle.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            Input_str += "angle = " + tmp
        else:
            Input_str += "angle = None" + linesep + linesep
        Input_str += "Nt_tot = " + str(self.Nt_tot) + linesep
        Input_str += "Nrev = " + str(self.Nrev) + linesep
        Input_str += "Na_tot = " + str(self.Na_tot) + linesep
        return Input_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False
        if other.time != self.time:
            return False
        if other.angle != self.angle:
            return False
        if other.Nt_tot != self.Nt_tot:
            return False
        if other.Nrev != self.Nrev:
            return False
        if other.Na_tot != self.Na_tot:
            return False
        return True

    def as_dict(self):
        """Convert this object in a json seriable dict (can be use in __init__)"""

        Input_dict = dict()
        if self.time is None:
            Input_dict["time"] = None
        else:
            Input_dict["time"] = self.time.as_dict()
        if self.angle is None:
            Input_dict["angle"] = None
        else:
            Input_dict["angle"] = self.angle.as_dict()
        Input_dict["Nt_tot"] = self.Nt_tot
        Input_dict["Nrev"] = self.Nrev
        Input_dict["Na_tot"] = self.Na_tot
        # The class name is added to the dict for deserialisation purpose
        Input_dict["__class__"] = "Input"
        return Input_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        if self.time is not None:
            self.time._set_None()
        if self.angle is not None:
            self.angle._set_None()
        self.Nt_tot = None
        self.Nrev = None
        self.Na_tot = None

    def _get_time(self):
        """getter of time"""
        return self._time

    def _set_time(self, value):
        """setter of time"""
        if isinstance(value, str):  # Load from file
            value = load_init_dict(value)[1]
        if isinstance(value, ndarray):
            value = ImportMatrixVal(value=value)
        elif isinstance(value, list):
            value = ImportMatrixVal(value=array(value))
        elif value == -1:
            value = ImportMatrix()
        elif isinstance(value, dict):
            class_obj = import_class("pyleecan.Classes", value.get("__class__"), "time")
            value = class_obj(init_dict=value)
        check_var("time", value, "ImportMatrix")
        self._time = value

        if self._time is not None:
            self._time.parent = self

    time = property(
        fget=_get_time,
        fset=_set_time,
        doc=u"""Electrical time vector (no symmetry) to import

        :Type: ImportMatrix
        """,
    )

    def _get_angle(self):
        """getter of angle"""
        return self._angle

    def _set_angle(self, value):
        """setter of angle"""
        if isinstance(value, str):  # Load from file
            value = load_init_dict(value)[1]
        if isinstance(value, ndarray):
            value = ImportMatrixVal(value=value)
        elif isinstance(value, list):
            value = ImportMatrixVal(value=array(value))
        elif value == -1:
            value = ImportMatrix()
        elif isinstance(value, dict):
            class_obj = import_class(
                "pyleecan.Classes", value.get("__class__"), "angle"
            )
            value = class_obj(init_dict=value)
        check_var("angle", value, "ImportMatrix")
        self._angle = value

        if self._angle is not None:
            self._angle.parent = self

    angle = property(
        fget=_get_angle,
        fset=_set_angle,
        doc=u"""Electrical position vector (no symmetry) to import

        :Type: ImportMatrix
        """,
    )

    def _get_Nt_tot(self):
        """getter of Nt_tot"""
        return self._Nt_tot

    def _set_Nt_tot(self, value):
        """setter of Nt_tot"""
        check_var("Nt_tot", value, "int", Vmin=1)
        self._Nt_tot = value

    Nt_tot = property(
        fget=_get_Nt_tot,
        fset=_set_Nt_tot,
        doc=u"""Time discretization

        :Type: int
        :min: 1
        """,
    )

    def _get_Nrev(self):
        """getter of Nrev"""
        return self._Nrev

    def _set_Nrev(self, value):
        """setter of Nrev"""
        check_var("Nrev", value, "float", Vmin=0)
        self._Nrev = value

    Nrev = property(
        fget=_get_Nrev,
        fset=_set_Nrev,
        doc=u"""Number of rotor revolution (to compute the final time)

        :Type: float
        :min: 0
        """,
    )

    def _get_Na_tot(self):
        """getter of Na_tot"""
        return self._Na_tot

    def _set_Na_tot(self, value):
        """setter of Na_tot"""
        check_var("Na_tot", value, "int", Vmin=1)
        self._Na_tot = value

    Na_tot = property(
        fget=_get_Na_tot,
        fset=_set_Na_tot,
        doc=u"""Angular discretization

        :Type: int
        :min: 1
        """,
    )
