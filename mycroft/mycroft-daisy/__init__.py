# Copyright 2016 Mycroft AI, Inc.
#
# This file is part of Mycroft Core.
#
# Mycroft Core is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Mycroft Core is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Mycroft Core.  If not, see <http://www.gnu.org/licenses/>.

from adapt.intent import IntentBuilder

from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger

__author__ = 'macikmir'

LOGGER = getLogger(__name__)


class DaisyFlowerSkill(MycroftSkill):
    def __init__(self):
        super(DaisyFlowerSkill, self).__init__(name="DaisyFlowerSkill")

    def initialize(self):
        who_are_you_intent = IntentBuilder("WhoAreYouIntent"). \
            require("WhoAreYouKeyword").build()
        self.register_intent(who_are_you_intent, self.handle_who_are_you_intent)

        how_are_you_intent = IntentBuilder("HowAreYouIntent"). \
            require("HowAreYouKeyword").build()
        self.register_intent(how_are_you_intent,
                             self.handle_how_are_you_intent)
       

    def handle_who_are_you_intent(self, message):
        self.speak_dialog("who.am.i",expect_response=False)
        somethingOnMind = self.get_response('something.on.mind')
        if somethingOnMind == "yes":
            userHasOnMind = self.get_response('whats.on.your.mind')
            userHasOnMind.replace('I', 'you', 1)
            self.speak(self.translate("i.am.sorry.to.hear") + " " + userHasOnMind,expect_response=False)
        else: 
            wantsPoem = self.get_response('do.you.want.poem')
            if wantsPoem == "yes":
                self.speak_dialog("speak.poem",expect_response=False)
            else: 
                self.speak_dialog("ok.talk.later",expect_response=False)

    def handle_how_are_you_intent(self, message):
        self.speak_dialog("how.are.you")


    def stop(self):
        pass


def create_skill():
    return DaisyFlowerSkill()
