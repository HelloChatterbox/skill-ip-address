from chatterbox.util.internet import get_local_ip




from chatterbox.builder.skill_builder import SkillBuilder


def create_skill():
  s = SkillBuilder('IP address')
  s.get_utterance()
  s.speak_dialog([str('''my eye pea address is''')])
  s.add_code_line("self.speak(str(get_local_ip()), wait=True)")
  s.add_padatious_intent(name="intent_name2", samples=["what is your network address", "tell me your network address", "tell me your ip address", "whats your ip address", "what is your ip address", "whats your network address"])
  s.build_skill()