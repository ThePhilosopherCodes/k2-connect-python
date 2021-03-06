""" Handles subscription to webhook services"""
import requests
import os

from .json_builder import webhook_subscription

# https://api-sandbox.kopokopo.com/webhook-subscription
default_webhook_subscription_url = ""


class WebhookSubscription(object):
    def __init__(self,
                 webhook_sectret=None,
                 event_type=None,
                 url=default_url):
        """
        :param webhook_sectret: (access token) The secret provided by Kopo Kopo to use for accessing services
        :type webhook_sectret: str

        :param event_type: The event type for which the webhook is being created
        :type event_type: str

        :param url: The end point to which the webhook is to be sent (https://myawesomeapplication.com/destination)
        :type url: str
        """

        self.secret = webhook_sectret
        self.event_type = event_type
        self.url = url

        # check for values
        if self.secret is None:
            raise ValueError("No webhook_sectret is passed")
        elif self.url is None:
            raise ValueError("No url is passed")
        elif self.event_type is None:
            raise ValueError("No event type is passed")

    # create webhook subscription
    def create_subscription(self):
        # set request body
        payload = webhook_subscription(provided_event_type=self.event_type,
                                       provided_url=self.url,
                                       provided_webhook_secret=self.secret)

        # perform POST request
        subscription_response = requests.post(url=self.url, payload=payload)
        return subscription_response


# get subscription data loctaion
def location(response):
    subscription_data_location = response.headers.get('location')
    return subscription_data_location
