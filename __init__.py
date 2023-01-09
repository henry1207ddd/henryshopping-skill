from mycroft import MycroftSkill, intent_file_handler


class Henryshopping(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('henryshopping.intent')
    def handle_henryshopping(self, message):
        self.speak_dialog('henryshopping')


def create_skill():
    return Henryshopping()

