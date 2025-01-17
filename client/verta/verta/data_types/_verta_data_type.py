# -*- coding: utf-8 -*-

import abc

from ..external import six


@six.add_metaclass(abc.ABCMeta)
class _VertaDataType(object):
    """
    Base class for complex structured data types. Not for external use.

    """

    _TYPE_NAME = None
    _VERSION = None

    def __eq__(self, other):
        if type(self) is not type(other):
            return NotImplemented
        return self.__dict__ == other.__dict__

    def _as_dict_inner(self, data):
        return {
            "type": "verta.{}.{}".format(
                self._TYPE_NAME,
                self._VERSION,
            ),
            self._TYPE_NAME: data,
        }

    @abc.abstractmethod
    def _as_dict(self):
        raise NotImplementedError

    @staticmethod
    def _from_dict(d):
        # TODO: when we have v2 onwards, make sure old v are still supported

        # imports here to avoid circular import in Python 2
        # TODO: figure out if cls.__subclasses__() is robust to use
        from . import (
            ConfusionMatrix,
            DiscreteHistogram,
            FloatHistogram,
            Line,
            Matrix,
            Table,
        )

        SUBCLASSES = [
            ConfusionMatrix,
            DiscreteHistogram,
            FloatHistogram,
            Line,
            Matrix,
            Table,
        ]

        d_type = d["type"]
        for Subclass in SUBCLASSES:
            subclass_type = "verta.{}.{}".format(
                Subclass._TYPE_NAME,
                Subclass._VERSION,
            )
            if d_type == subclass_type:
                return Subclass._from_dict(d)

        raise ValueError("data type {} not recognized".format(d_type))
