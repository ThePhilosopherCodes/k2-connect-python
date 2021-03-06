"""Handles creation of getters and setters for decomposition of result payloads"""


class PaymentResult(object):
    def __init__(self,
                 payment_result_status=None,
                 payment_result_id=None):
        """
        :param payment_result_status:
        :param payment_result_id:
        :param payment_result_error_code:
        :param payment_result_error_description:
        """
        self._payment_result_status = payment_result_status
        self._payment_result_id = payment_result_id

    # payment_result_status
    @property
    def payment_result_status(self):
        return self._payment_result_status

    @payment_result_status.setter
    def payment_result_status(self, value):
        self._payment_result_status = value

    # payment_result_id
    @property
    def payment_result_id(self):
        return self._payment_result_id

    @payment_result_id.setter
    def payment_result_id(self, value):
        self._payment_result_id = value


