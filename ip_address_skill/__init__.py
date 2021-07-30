from chatterbox.skills.core import ChatterboxSkill
from chatterbox.skills.core import intent_file_handler
from chatterbox_utils.internet import get_local_ip


class IpSkill(ChatterboxSkill):
    @intent_file_handler('ip.intent')
    def handle_intent_name2Intent(self, message):
        self.speak_dialog("ip_address", expect_response=False, wait=True)
        self.speak(get_local_ip(), wait=True)


def create_skill():
    return IpSkill()
