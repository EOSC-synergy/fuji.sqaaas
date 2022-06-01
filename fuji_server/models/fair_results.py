# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from fuji_server.models.base_model_ import Model
#from fuji_server.models.object import Object  # noqa: F401,E501
from fuji_server import util
from fuji_server.models.any_of_fair_results_results_items import AnyOfFAIRResultsResultsItems

class FAIRResults(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, test_id: str=None, request: Dict=None, timestamp: datetime=None, expiry_timestamp: datetime=None, metric_specification: str=None, metric_version: str=None, software_version: str=None, total_metrics: int=None, results: List[AnyOfFAIRResultsResultsItems]=None):  # noqa: E501
        """FAIRResults - a model defined in Swagger

        :param test_id: The test_id of this FAIRResults.  # noqa: E501
        :type test_id: str
        :param request: The request of this FAIRResults.  # noqa: E501
        :type request: Dict
        :param timestamp: The timestamp of this FAIRResults.  # noqa: E501
        :type timestamp: datetime
        :param expiry_timestamp: The expiry_timestamp of this FAIRResults.  # noqa: E501
        :type expiry_timestamp: datetime
        :param metric_specification: The metric_specification of this FAIRResults.  # noqa: E501
        :type metric_specification: str
        :param metric_version: The metric_version of this FAIRResults.  # noqa: E501
        :type metric_version: str
        :param software_version: The software_version of this FAIRResults.  # noqa: E501
        :type software_version: str
        :param total_metrics: The total_metrics of this FAIRResults.  # noqa: E501
        :type total_metrics: int
        :param results: The results of this FAIRResults.  # noqa: E501
        :type results: List[AnyOfFAIRResultsResultsItems]
        """
        self.swagger_types = {
            'test_id': str,
            'request': Dict,
            'timestamp': datetime,
            'expiry_timestamp': datetime,
            'metric_specification': str,
            'metric_version': str,
            'software_version': str,
            'total_metrics': int,
            'results': List[AnyOfFAIRResultsResultsItems]
        }

        self.attribute_map = {
            'test_id': 'test_id',
            'request': 'request',
            'timestamp': 'timestamp',
            'expiry_timestamp': 'expiry_timestamp',
            'metric_specification': 'metric_specification',
            'metric_version': 'metric_version',
            'software_version': 'software_version',
            'total_metrics': 'total_metrics',
            'results': 'results'
        }
        self._test_id = test_id
        self._request = request
        self._timestamp = timestamp
        self._expiry_timestamp = expiry_timestamp
        self._metric_specification = metric_specification
        self._metric_version = metric_version
        self._software_version = software_version
        self._total_metrics = total_metrics
        self._results = results

    @classmethod
    def from_dict(cls, dikt) -> 'FAIRResults':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The FAIRResults of this FAIRResults.  # noqa: E501
        :rtype: FAIRResults
        """
        return util.deserialize_model(dikt, cls)

    @property
    def test_id(self) -> str:
        """Gets the test_id of this FAIRResults.


        :return: The test_id of this FAIRResults.
        :rtype: str
        """
        return self._test_id

    @test_id.setter
    def test_id(self, test_id: str):
        """Sets the test_id of this FAIRResults.


        :param test_id: The test_id of this FAIRResults.
        :type test_id: str
        """

        self._test_id = test_id

    @property
    def request(self) -> Dict:
        """Gets the request of this FAIRResults.


        :return: The request of this FAIRResults.
        :rtype: Dict
        """
        return self._request

    @request.setter
    def request(self, request: Dict):
        """Sets the request of this FAIRResults.


        :param request: The request of this FAIRResults.
        :type request: Dict
        """

        self._request = request

    @property
    def timestamp(self) -> datetime:
        """Gets the timestamp of this FAIRResults.


        :return: The timestamp of this FAIRResults.
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp: datetime):
        """Sets the timestamp of this FAIRResults.


        :param timestamp: The timestamp of this FAIRResults.
        :type timestamp: datetime
        """

        self._timestamp = timestamp

    @property
    def expiry_timestamp(self) -> datetime:
        """Gets the expiry_timestamp of this FAIRResults.


        :return: The expiry_timestamp of this FAIRResults.
        :rtype: datetime
        """
        return self._expiry_timestamp

    @expiry_timestamp.setter
    def expiry_timestamp(self, expiry_timestamp: datetime):
        """Sets the expiry_timestamp of this FAIRResults.


        :param expiry_timestamp: The expiry_timestamp of this FAIRResults.
        :type expiry_timestamp: datetime
        """

        self._expiry_timestamp = expiry_timestamp

    @property
    def metric_specification(self) -> str:
        """Gets the metric_specification of this FAIRResults.


        :return: The metric_specification of this FAIRResults.
        :rtype: str
        """
        return self._metric_specification

    @metric_specification.setter
    def metric_specification(self, metric_specification: str):
        """Sets the metric_specification of this FAIRResults.


        :param metric_specification: The metric_specification of this FAIRResults.
        :type metric_specification: str
        """

        self._metric_specification = metric_specification

    @property
    def metric_version(self) -> str:
        """Gets the metric_version of this FAIRResults.


        :return: The metric_version of this FAIRResults.
        :rtype: str
        """
        return self._metric_version

    @metric_version.setter
    def metric_version(self, metric_version: str):
        """Sets the metric_version of this FAIRResults.


        :param metric_version: The metric_version of this FAIRResults.
        :type metric_version: str
        """

        self._metric_version = metric_version

    @property
    def software_version(self) -> str:
        """Gets the software_version of this FAIRResults.


        :return: The software_version of this FAIRResults.
        :rtype: str
        """
        return self._software_version

    @software_version.setter
    def software_version(self, software_version: str):
        """Sets the software_version of this FAIRResults.


        :param software_version: The software_version of this FAIRResults.
        :type software_version: str
        """

        self._software_version = software_version

    @property
    def total_metrics(self) -> int:
        """Gets the total_metrics of this FAIRResults.


        :return: The total_metrics of this FAIRResults.
        :rtype: int
        """
        return self._total_metrics

    @total_metrics.setter
    def total_metrics(self, total_metrics: int):
        """Sets the total_metrics of this FAIRResults.


        :param total_metrics: The total_metrics of this FAIRResults.
        :type total_metrics: int
        """

        self._total_metrics = total_metrics

    @property
    def results(self) -> List[AnyOfFAIRResultsResultsItems]:
        """Gets the results of this FAIRResults.


        :return: The results of this FAIRResults.
        :rtype: List[AnyOfFAIRResultsResultsItems]
        """
        return self._results

    @results.setter
    def results(self, results: List[AnyOfFAIRResultsResultsItems]):
        """Sets the results of this FAIRResults.


        :param results: The results of this FAIRResults.
        :type results: List[AnyOfFAIRResultsResultsItems]
        """

        self._results = results