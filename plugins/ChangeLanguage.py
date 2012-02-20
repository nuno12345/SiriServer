#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from plugin import *

class ChangeLanguage(Plugin):
    @register("en-US", "change language to.*")
    @register("de-DE", "sprach andern um.*")
    @register("pt-PT", "mudar linguagem para.*")
    def ttm_uptime_status(self, speech, language):
	if language == "en-US":
		if (speech.count("portuguese") > 0):
        		self.say('Language changed to portuguese')
        		self.assistant.language = "pt-PT"
			self.complete_request()
                elif (speech.count("german") > 0):
                        self.say('Language changed to german')
                        self.assistant.language = "de-DE"
                        self.complete_request()
                elif (speech.count("french") > 0):
                        self.say('Language changed to french')
                        self.assistant.language = "fr-FR"
                        self.complete_request()
		else:
			self.say('Language not found')
			self.complete_request()
        
	elif language == "pt-PT":
                if (speech.count("ingles") > 0):
                        self.say('Linguagem mudada para ingles')
                        self.assistant.language = "en-US"
                        self.complete_request()
                elif (speech.count("alemao") > 0):
                        self.say('Linguagem mudada para alemao')
                        self.assistant.language = "de-DE"
                        self.complete_request()
                elif (speech.count("frances") > 0):
                        self.say('Linguagem mudada para frances')
                        self.assistant.language = "fr-FR"
                        self.complete_request()
                else:
                        self.say('Language not found')
                        self.complete_request()

