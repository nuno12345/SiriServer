#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from datetime import date
import locale 
from plugin import *

class talkToMe(Plugin):   
        
    @register("de-DE", ".*Dein.*Status.*")
    @register("en-US", "Your Status.*")
    def ttm_uptime_status(self, speech, language):
        uptime = os.popen("uptime").read()
        if language == 'de-DE':
            self.say('Hier ist der Status:')
            self.say(uptime, ' ')
        else:
            self.say('Here is the status:')
            self.say(uptime, ' ')
        self.complete_request()

    @register("en-US", "ip address")
    def ttm_uptime_status(self, speech, language):
        uptime = os.popen("ifconfig").read()
        if language == 'en-US':
            self.say('Here is the status:')
            self.say(uptime, ' ')
        self.complete_request()


    @register("en-US", ".*restart server.*")
    def ttm_uptime_status(self, speech, language):
        if language == 'en-US':
            self.say('Server is restarting, please wait...')
	    uptime = os.popen("service siriserver restart").read()
        self.complete_request()

