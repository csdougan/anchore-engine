# coding: utf-8

"""
    anchore_engine.services.policy_engine

    This is a policy evaluation service. It receives push-events from external systems for data updates and provides an api for requesting image policy checks  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: zach@anchore.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from anchore_engine.clients.policy_engine.generated.models.policy_evaluation_problem import PolicyEvaluationProblem  # noqa: F401,E501


class PolicyEvaluation(object):
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
        'user_id': 'str',
        'image_id': 'str',
        'tag': 'str',
        'bundle': 'object',
        'matched_mapping_rule': 'object',
        'matched_whitelisted_images_rule': 'object',
        'matched_blacklisted_images_rule': 'object',
        'result': 'object',
        'created_at': 'int',
        'last_modified': 'int',
        'final_action': 'str',
        'final_action_reason': 'str',
        'evaluation_problems': 'list[PolicyEvaluationProblem]'
    }

    attribute_map = {
        'user_id': 'user_id',
        'image_id': 'image_id',
        'tag': 'tag',
        'bundle': 'bundle',
        'matched_mapping_rule': 'matched_mapping_rule',
        'matched_whitelisted_images_rule': 'matched_whitelisted_images_rule',
        'matched_blacklisted_images_rule': 'matched_blacklisted_images_rule',
        'result': 'result',
        'created_at': 'created_at',
        'last_modified': 'last_modified',
        'final_action': 'final_action',
        'final_action_reason': 'final_action_reason',
        'evaluation_problems': 'evaluation_problems'
    }

    def __init__(self, user_id=None, image_id=None, tag=None, bundle=None, matched_mapping_rule=None, matched_whitelisted_images_rule=None, matched_blacklisted_images_rule=None, result=None, created_at=None, last_modified=None, final_action=None, final_action_reason=None, evaluation_problems=None):  # noqa: E501
        """PolicyEvaluation - a model defined in Swagger"""  # noqa: E501

        self._user_id = None
        self._image_id = None
        self._tag = None
        self._bundle = None
        self._matched_mapping_rule = None
        self._matched_whitelisted_images_rule = None
        self._matched_blacklisted_images_rule = None
        self._result = None
        self._created_at = None
        self._last_modified = None
        self._final_action = None
        self._final_action_reason = None
        self._evaluation_problems = None
        self.discriminator = None

        if user_id is not None:
            self.user_id = user_id
        self.image_id = image_id
        self.tag = tag
        self.bundle = bundle
        self.matched_mapping_rule = matched_mapping_rule
        self.matched_whitelisted_images_rule = matched_whitelisted_images_rule
        self.matched_blacklisted_images_rule = matched_blacklisted_images_rule
        self.result = result
        if created_at is not None:
            self.created_at = created_at
        if last_modified is not None:
            self.last_modified = last_modified
        self.final_action = final_action
        self.final_action_reason = final_action_reason
        if evaluation_problems is not None:
            self.evaluation_problems = evaluation_problems

    @property
    def user_id(self):
        """Gets the user_id of this PolicyEvaluation.  # noqa: E501

        Unique identifier (UUID) for the catalog user  # noqa: E501

        :return: The user_id of this PolicyEvaluation.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this PolicyEvaluation.

        Unique identifier (UUID) for the catalog user  # noqa: E501

        :param user_id: The user_id of this PolicyEvaluation.  # noqa: E501
        :type: str
        """

        self._user_id = user_id

    @property
    def image_id(self):
        """Gets the image_id of this PolicyEvaluation.  # noqa: E501


        :return: The image_id of this PolicyEvaluation.  # noqa: E501
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        """Sets the image_id of this PolicyEvaluation.


        :param image_id: The image_id of this PolicyEvaluation.  # noqa: E501
        :type: str
        """
        if image_id is None:
            raise ValueError("Invalid value for `image_id`, must not be `None`")  # noqa: E501

        self._image_id = image_id

    @property
    def tag(self):
        """Gets the tag of this PolicyEvaluation.  # noqa: E501


        :return: The tag of this PolicyEvaluation.  # noqa: E501
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this PolicyEvaluation.


        :param tag: The tag of this PolicyEvaluation.  # noqa: E501
        :type: str
        """
        if tag is None:
            raise ValueError("Invalid value for `tag`, must not be `None`")  # noqa: E501

        self._tag = tag

    @property
    def bundle(self):
        """Gets the bundle of this PolicyEvaluation.  # noqa: E501

        The bundle used for evaluation  # noqa: E501

        :return: The bundle of this PolicyEvaluation.  # noqa: E501
        :rtype: object
        """
        return self._bundle

    @bundle.setter
    def bundle(self, bundle):
        """Sets the bundle of this PolicyEvaluation.

        The bundle used for evaluation  # noqa: E501

        :param bundle: The bundle of this PolicyEvaluation.  # noqa: E501
        :type: object
        """
        if bundle is None:
            raise ValueError("Invalid value for `bundle`, must not be `None`")  # noqa: E501

        self._bundle = bundle

    @property
    def matched_mapping_rule(self):
        """Gets the matched_mapping_rule of this PolicyEvaluation.  # noqa: E501

        The bundle mapping rule that was evaluated to result in the evaluated policy and whitelists being selected  # noqa: E501

        :return: The matched_mapping_rule of this PolicyEvaluation.  # noqa: E501
        :rtype: object
        """
        return self._matched_mapping_rule

    @matched_mapping_rule.setter
    def matched_mapping_rule(self, matched_mapping_rule):
        """Sets the matched_mapping_rule of this PolicyEvaluation.

        The bundle mapping rule that was evaluated to result in the evaluated policy and whitelists being selected  # noqa: E501

        :param matched_mapping_rule: The matched_mapping_rule of this PolicyEvaluation.  # noqa: E501
        :type: object
        """
        if matched_mapping_rule is None:
            raise ValueError("Invalid value for `matched_mapping_rule`, must not be `None`")  # noqa: E501

        self._matched_mapping_rule = matched_mapping_rule

    @property
    def matched_whitelisted_images_rule(self):
        """Gets the matched_whitelisted_images_rule of this PolicyEvaluation.  # noqa: E501

        The trusted image entry matched if any  # noqa: E501

        :return: The matched_whitelisted_images_rule of this PolicyEvaluation.  # noqa: E501
        :rtype: object
        """
        return self._matched_whitelisted_images_rule

    @matched_whitelisted_images_rule.setter
    def matched_whitelisted_images_rule(self, matched_whitelisted_images_rule):
        """Sets the matched_whitelisted_images_rule of this PolicyEvaluation.

        The trusted image entry matched if any  # noqa: E501

        :param matched_whitelisted_images_rule: The matched_whitelisted_images_rule of this PolicyEvaluation.  # noqa: E501
        :type: object
        """
        if matched_whitelisted_images_rule is None:
            raise ValueError("Invalid value for `matched_whitelisted_images_rule`, must not be `None`")  # noqa: E501

        self._matched_whitelisted_images_rule = matched_whitelisted_images_rule

    @property
    def matched_blacklisted_images_rule(self):
        """Gets the matched_blacklisted_images_rule of this PolicyEvaluation.  # noqa: E501

        The image blacklist entry matched if any  # noqa: E501

        :return: The matched_blacklisted_images_rule of this PolicyEvaluation.  # noqa: E501
        :rtype: object
        """
        return self._matched_blacklisted_images_rule

    @matched_blacklisted_images_rule.setter
    def matched_blacklisted_images_rule(self, matched_blacklisted_images_rule):
        """Sets the matched_blacklisted_images_rule of this PolicyEvaluation.

        The image blacklist entry matched if any  # noqa: E501

        :param matched_blacklisted_images_rule: The matched_blacklisted_images_rule of this PolicyEvaluation.  # noqa: E501
        :type: object
        """
        if matched_blacklisted_images_rule is None:
            raise ValueError("Invalid value for `matched_blacklisted_images_rule`, must not be `None`")  # noqa: E501

        self._matched_blacklisted_images_rule = matched_blacklisted_images_rule

    @property
    def result(self):
        """Gets the result of this PolicyEvaluation.  # noqa: E501

        Object containing the evaluation result for the given policy and whitelists against the image  # noqa: E501

        :return: The result of this PolicyEvaluation.  # noqa: E501
        :rtype: object
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this PolicyEvaluation.

        Object containing the evaluation result for the given policy and whitelists against the image  # noqa: E501

        :param result: The result of this PolicyEvaluation.  # noqa: E501
        :type: object
        """
        if result is None:
            raise ValueError("Invalid value for `result`, must not be `None`")  # noqa: E501

        self._result = result

    @property
    def created_at(self):
        """Gets the created_at of this PolicyEvaluation.  # noqa: E501

        Epoch time on server of record creation  # noqa: E501

        :return: The created_at of this PolicyEvaluation.  # noqa: E501
        :rtype: int
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this PolicyEvaluation.

        Epoch time on server of record creation  # noqa: E501

        :param created_at: The created_at of this PolicyEvaluation.  # noqa: E501
        :type: int
        """

        self._created_at = created_at

    @property
    def last_modified(self):
        """Gets the last_modified of this PolicyEvaluation.  # noqa: E501

        Epoch time on server of last modification  # noqa: E501

        :return: The last_modified of this PolicyEvaluation.  # noqa: E501
        :rtype: int
        """
        return self._last_modified

    @last_modified.setter
    def last_modified(self, last_modified):
        """Sets the last_modified of this PolicyEvaluation.

        Epoch time on server of last modification  # noqa: E501

        :param last_modified: The last_modified of this PolicyEvaluation.  # noqa: E501
        :type: int
        """

        self._last_modified = last_modified

    @property
    def final_action(self):
        """Gets the final_action of this PolicyEvaluation.  # noqa: E501

        The overall outcome of the evaluation. STOP|GO|WARN  # noqa: E501

        :return: The final_action of this PolicyEvaluation.  # noqa: E501
        :rtype: str
        """
        return self._final_action

    @final_action.setter
    def final_action(self, final_action):
        """Sets the final_action of this PolicyEvaluation.

        The overall outcome of the evaluation. STOP|GO|WARN  # noqa: E501

        :param final_action: The final_action of this PolicyEvaluation.  # noqa: E501
        :type: str
        """
        if final_action is None:
            raise ValueError("Invalid value for `final_action`, must not be `None`")  # noqa: E501

        self._final_action = final_action

    @property
    def final_action_reason(self):
        """Gets the final_action_reason of this PolicyEvaluation.  # noqa: E501

        The reason for the final result  # noqa: E501

        :return: The final_action_reason of this PolicyEvaluation.  # noqa: E501
        :rtype: str
        """
        return self._final_action_reason

    @final_action_reason.setter
    def final_action_reason(self, final_action_reason):
        """Sets the final_action_reason of this PolicyEvaluation.

        The reason for the final result  # noqa: E501

        :param final_action_reason: The final_action_reason of this PolicyEvaluation.  # noqa: E501
        :type: str
        """
        if final_action_reason is None:
            raise ValueError("Invalid value for `final_action_reason`, must not be `None`")  # noqa: E501
        allowed_values = ["whitelisted", "blacklisted", "policy_evaluation"]  # noqa: E501
        if final_action_reason not in allowed_values:
            raise ValueError(
                "Invalid value for `final_action_reason` ({0}), must be one of {1}"  # noqa: E501
                .format(final_action_reason, allowed_values)
            )

        self._final_action_reason = final_action_reason

    @property
    def evaluation_problems(self):
        """Gets the evaluation_problems of this PolicyEvaluation.  # noqa: E501

        list of error objects indicating errors encountered during evaluation execution  # noqa: E501

        :return: The evaluation_problems of this PolicyEvaluation.  # noqa: E501
        :rtype: list[PolicyEvaluationProblem]
        """
        return self._evaluation_problems

    @evaluation_problems.setter
    def evaluation_problems(self, evaluation_problems):
        """Sets the evaluation_problems of this PolicyEvaluation.

        list of error objects indicating errors encountered during evaluation execution  # noqa: E501

        :param evaluation_problems: The evaluation_problems of this PolicyEvaluation.  # noqa: E501
        :type: list[PolicyEvaluationProblem]
        """

        self._evaluation_problems = evaluation_problems

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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PolicyEvaluation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other