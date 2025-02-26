# coding: utf-8

"""
    Obstacle Detection Result

    This is the REST API endpoint specification for processing the results of the obstacle detection process. For the obstacle detection module see [this repository](https://github.com/karolyartur/obstacle-detection).   # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Result(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'header': 'Header',
        'position': 'Position',
        'size': 'float',
        'velocity': 'Velocity'
    }

    attribute_map = {
        'header': 'header',
        'position': 'position',
        'size': 'size',
        'velocity': 'velocity'
    }

    def __init__(self, header=None, position=None, size=None, velocity=None):  # noqa: E501
        """Result - a model defined in Swagger"""  # noqa: E501
        self._header = None
        self._position = None
        self._size = None
        self._velocity = None
        self.discriminator = None
        self.header = header
        self.position = position
        self.size = size
        self.velocity = velocity

    @property
    def header(self):
        """Gets the header of this Result.  # noqa: E501


        :return: The header of this Result.  # noqa: E501
        :rtype: Header
        """
        return self._header

    @header.setter
    def header(self, header):
        """Sets the header of this Result.


        :param header: The header of this Result.  # noqa: E501
        :type: Header
        """
        if header is None:
            raise ValueError("Invalid value for `header`, must not be `None`")  # noqa: E501

        self._header = header

    @property
    def position(self):
        """Gets the position of this Result.  # noqa: E501


        :return: The position of this Result.  # noqa: E501
        :rtype: Position
        """
        return self._position

    @position.setter
    def position(self, position):
        """Sets the position of this Result.


        :param position: The position of this Result.  # noqa: E501
        :type: Position
        """
        if position is None:
            raise ValueError("Invalid value for `position`, must not be `None`")  # noqa: E501

        self._position = position

    @property
    def size(self):
        """Gets the size of this Result.  # noqa: E501

        nominal size of the obstacle in meters  # noqa: E501

        :return: The size of this Result.  # noqa: E501
        :rtype: float
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this Result.

        nominal size of the obstacle in meters  # noqa: E501

        :param size: The size of this Result.  # noqa: E501
        :type: float
        """
        if size is None:
            raise ValueError("Invalid value for `size`, must not be `None`")  # noqa: E501

        self._size = size

    @property
    def velocity(self):
        """Gets the velocity of this Result.  # noqa: E501


        :return: The velocity of this Result.  # noqa: E501
        :rtype: Velocity
        """
        return self._velocity

    @velocity.setter
    def velocity(self, velocity):
        """Sets the velocity of this Result.


        :param velocity: The velocity of this Result.  # noqa: E501
        :type: Velocity
        """
        if velocity is None:
            raise ValueError("Invalid value for `velocity`, must not be `None`")  # noqa: E501

        self._velocity = velocity

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(Result, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Result):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
