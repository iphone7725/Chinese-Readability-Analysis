import tensorflow as tf
import numpy as np
import time as tic
import xlrd as xl
import xlwt as xlw
import urllib.request as ul
import re

# Defines the webstring class, which fetches strings from the web based on specified inputs

# Define class web_string which stores Chinese string
# Attributes: url, chapters (optional), contents

class c_webstring:
    
    # Initialize Object
    def init(self, url_root, url_terminal = None, chapters = 0, curr_chapter = 0):
        self.root = url_root # Root address
        self.chapter = chapter # Optional address terminus
        self.term = url_terminal # Chapter integer
        self.curr_chapter = curr_chapter
        
        self.content = [] # Url Contents
        return
        
    def modify(self, url_root = None, url_terminal = None, chapters = None, curr_chapter = None):
        if url_root != None:
            self.root = url_root
        if url_terminal != None:
            self.term = url_terminal
        if chapters != None:
            self.chapter = chapter
        if curr_chapter != None:
            self.curr_chapter = curr_chapter
        return # Modifies attributes
    
    def extract_all(self, body_head, body_tail):
        #If no chapters specified
        if self.chapter == 0:
            full = ul.urlopen(url_root) # Get full source code
            head = full.index(body_head) # Fetch index of body_heat string
            tail = full.index(body_tail) # Fetch index of body_tail string
            self.content.append(full[head, tail + len(body_tail)]) # Splicing and appending
            
        #If integer range specified    
        else:
            for i in range(self.curr_chapter, self.chapter):
                try: 
                    full = ul.urlopen(entry_string.root + i + entry_string.term) # Getting address and source code
                    head = full.index(body_head) # Fetch index of body_heat string
                    tail = full.index(body_tail) # Fetch index of body_tail string
                    self.contents.append(full[head, tail + len(body_tail)]) # Splicing and appending
                except:
                    print("Unspecified error, check url names and page text encoding")
    
    def clean_all(self, html_flag = 1, ws_flag = 1, punct_flag = 1, html_markers = None, punct_markers = None):
        if html_flag == 1:
            clean_html(self, html_markers) # Removes html text modifiers listed in html_markers; default = all modifiers
        if ws_flag == 1:
            clean_ws(self) # Removes white spaces
        if punct_flag == 1:
            clean_punct(self, punct_markers) # Removes punctuation listed in punct_markers, default = all punctuation
        
    def clean_html(self, html_markers):
        if html_markers == None:
            for i in range(len(self.contents)):
                self.contents[i] = re.sub("[\<].*?[\>]", "", self.contents[i], re.UNICODE) # Deletes all html text modifiers
                
        else: # Expect html_markers to be list
            for i in range(len(self.contents)):
                for j in range(len(html_markers)):
                    self.contents[i] = self.contents[i].replace(html_markers[j], "") # Deletes all modifiers listed in html_markers
        return        
        
    def clean_ws(self):
        for i in range(len(self.contents)):
            regex = re.compile(r"\s+") # 
            self.contents[i] = re.sub(regex, '', sentence, re.UNICODE)
        return

    def clean_punct(self, punct_markers):
        if punct_markers == None:
            for i in range(len(self.contents)):
                self.contents[i] = re.sub(r'[^\w\s]','',self.contents[i], re.UNICODE)
                
        else: # Expect punct to be list
            for i in range(len(self.contents)):
                for j in range(len(punct_markers)):
                    self.contents[i] = self.contents[i].replace(punct_markers[j], "")
        return
                
    def to_utf8(self):
        return # will code if necessary
