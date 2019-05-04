from fbchat import Client
from fbchat.models import *
import sms_handler

class ListenBot(Client):

    # For title of chat with person/group
    thread_name_mapping = {}
    # For name of person in group (if it's a group, you want name of group and
    # the person who sent the message)
    user_name_mapping = {}

    def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
        self.markAsDelivered(thread_id, message_object.uid)

        # If I sent the message, I don't want to be notified about it
        if author_id == self.uid:
            return

        text_to_send = ''

        if thread_id not in self.thread_name_mapping:
            thread_obj = self.fetchThreadInfo(thread_id)[thread_id]
            self.thread_name_mapping[thread_id] = thread_obj.name

        thread_name = self.thread_name_mapping[thread_id]
        text_to_send += f'{thread_name} - '

        # If it's a group, get person who sent it as well
        if thread_type == ThreadType.GROUP:
            if author_id not in self.user_name_mapping:
                user = self.fetchUserInfo(author_id)[author_id]
                self.user_name_mapping[author_id] = f'{user.first_name}'

            user_name = self.user_name_mapping[author_id]
            text_to_send += f'{user_name} - '

        text_to_send += message_object.text
        sms_handler.send_sms(text_to_send)
