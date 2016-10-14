import os
from googleapiclient.discovery import build
from oauth2client.client import flow_from_clientsecrets
from oauth2client.file import Storage
from oauth2client.tools import run_flow
from googleapiclient import errors
import httplib2

__author__ = 'anugnes'


def generate_google_service(settings):
    """Authenticate using stored credentials and return a service instance for Gmail"""

    path = os.path.dirname(os.path.abspath(__file__))

    client_secret_file = path + settings['client_secret_file']
    oauth_scope = settings['oauth_scope']
    storage = Storage(path + settings['storage'])

    # Start the OAuth flow to retrieve credentials
    flow = flow_from_clientsecrets(client_secret_file, scope=oauth_scope)
    http = httplib2.Http()

    # Try to retrieve credentials from storage or run the flow to generate them
    credentials = storage.get()
    if credentials is None or credentials.invalid:
        credentials = run_flow(flow, storage, http=http)

    http = credentials.authorize(http)
    service = build('gmail', 'v1', http=http)

    return service


def send_message(service, user_id, message):
    """Send an email message.

    Args:
      service: Authorized Gmail API service instance.
      user_id: User's email address. The special value "me"
      can be used to indicate the authenticated user.
      message: Message to be sent.

    Returns:
      Sent Message.
    """
    try:
        message = (service.users().messages().send(userId=user_id, body=message)
                   .execute())
        print 'Message Id: %s' % message['id']
        return message
    except errors.HttpError, error:
        print 'An error occurred: %s' % error
