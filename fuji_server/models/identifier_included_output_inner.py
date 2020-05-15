# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from fuji_server.models.base_model_ import Model
from fuji_server import util


class IdentifierIncludedOutputInner(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, content_identifier_included: str=None, content_identifier_active: bool=False):  # noqa: E501
        """IdentifierIncludedOutputInner - a model defined in Swagger

        :param content_identifier_included: The content_identifier_included of this IdentifierIncludedOutputInner.  # noqa: E501
        :type content_identifier_included: str
        :param content_identifier_active: The content_identifier_active of this IdentifierIncludedOutputInner.  # noqa: E501
        :type content_identifier_active: bool
        """
        self.swagger_types = {
            'content_identifier_included': str,
            'content_identifier_active': bool
        }

        self.attribute_map = {
            'content_identifier_included': 'content_identifier_included',
            'content_identifier_active': 'content_identifier_active'
        }
        self._content_identifier_included = content_identifier_included
        self._content_identifier_active = content_identifier_active

    @classmethod
    def from_dict(cls, dikt) -> 'IdentifierIncludedOutputInner':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The IdentifierIncluded_output_inner of this IdentifierIncludedOutputInner.  # noqa: E501
        :rtype: IdentifierIncludedOutputInner
        """
        return util.deserialize_model(dikt, cls)

    @property
    def content_identifier_included(self) -> str:
        """Gets the content_identifier_included of this IdentifierIncludedOutputInner.


        :return: The content_identifier_included of this IdentifierIncludedOutputInner.
        :rtype: str
        """
        return self._content_identifier_included

    @content_identifier_included.setter
    def content_identifier_included(self, content_identifier_included: str):
        """Sets the content_identifier_included of this IdentifierIncludedOutputInner.


        :param content_identifier_included: The content_identifier_included of this IdentifierIncludedOutputInner.
        :type content_identifier_included: str
        """

        self._content_identifier_included = content_identifier_included

    @property
    def content_identifier_active(self) -> bool:
        """Gets the content_identifier_active of this IdentifierIncludedOutputInner.


        :return: The content_identifier_active of this IdentifierIncludedOutputInner.
        :rtype: bool
        """
        return self._content_identifier_active

    @content_identifier_active.setter
    def content_identifier_active(self, content_identifier_active: bool):
        """Sets the content_identifier_active of this IdentifierIncludedOutputInner.


        :param content_identifier_active: The content_identifier_active of this IdentifierIncludedOutputInner.
        :type content_identifier_active: bool
        """

        self._content_identifier_active = content_identifier_active
