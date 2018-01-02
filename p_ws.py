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
    def __init__(self, url_root, chapter = 0, url_terminal = None, curr_chapter = 1):
        self.root = url_root # Root address
        self.chapter = chapter # Optional address terminus
        self.term = url_terminal # Chapter integer
        self.curr_chapter = curr_chapter
        
        self.content = [] # Url Contents
        return
        
    def modify(self, url_root = None, chapter = None, url_terminal = None, curr_chapter = None):
        if url_root != None:
            self.root = url_root
        if url_terminal != None:
            self.term = url_terminal
        if chapter != None:
            self.chapter = chapter
        if curr_chapter != None:
            self.curr_chapter = curr_chapter
        return # Modifies attributes
    
    def extract_all(self, body_head, body_tail):
        #If no chapters specified
        if self.chapter == 0:
            response = ul.urlopen(url_root) # Get full source code
            full = response.read().decode('utf-8')
            for i in range(len(body_head)):
                try:
                    head = full.index(body_head[i]) # Fetch index of body_heat string
                except:
                    continue
            tail = full.index(body_tail) # Fetch index of body_tail string
            self.content.append(full[head, tail + len(body_tail)]) # Splicing and appending
            
        #If integer range specified    
        else:
            for i in range(self.curr_chapter, self.chapter + 1):
                response = ul.urlopen(self.root + str(i) + self.term) # Getting address and source code
                full = response.read().decode('utf-8')
                for j in range(len(body_head)):
                    try:
                        head = full.index(body_head[j]) # Fetch index of body_heat string
                    except(ValueError):
                        continue
                tail = full.index(body_tail) # Fetch index of body_tail string
                self.content.append(full[head:tail + len(body_tail)]) # Splicing and appending
                self.curr_chapter += 1
    
    def clean_all(self, html_flag = 0, ws_flag = 0, punct_flag = 0, strip_chinese = 1, html_markers = None, punct_markers = None):
        if html_flag == 1:
            self.clean_html(html_markers) # Removes html text modifiers listed in html_markers; default = all modifiers
        if ws_flag == 1:
            self.clean_ws() # Removes white spaces
        if punct_flag == 1:
            self.clean_punct(punct_markers) # Removes punctuation listed in punct_markers, default = all punctuation
        if strip_chinese == 1:
            self.strip_chinese()
        
    def clean_html(self, html_markers):
        if html_markers == None:
            for i in range(len(self.content)):
                self.content[i] = re.sub("[\<].*?[\>]", "", self.content[i], re.UNICODE) # Deletes all html text modifiers
                
        else: # Expect html_markers to be list
            for i in range(len(self.content)):
                for j in range(len(html_markers)):
                    self.content[i] = self.contents[i].replace(html_markers[j], "") # Deletes all modifiers listed in html_markers
        return        
        
    def clean_ws(self):
        for i in range(len(self.content)):
            regex = re.compile(r"\s+") # 
            self.content[i] = re.sub(regex, '', self.content[i], re.UNICODE)
        return

    def clean_punct(self, punct_markers):
        if punct_markers == None:
            for i in range(len(self.content)):
                self.content[i] = re.sub(r'[^\w\s]','',self.content[i], re.UNICODE)
                
        else: # Expect punct to be list
            for i in range(len(self.content)):
                for j in range(len(punct_markers)):
                    self.content[i] = self.content[i].replace(punct_markers[j], "")
        return
                
    def strip_chinese(self):
        for i in range(len(self.content)):
            regex = re.compile(u'[^\u4E00-\u97A5]')
            self.content[i] = regex.sub(r'',self.content[i])
            self.content[i] = re.sub("\s","",self.content[i])                   
    
    def to_utf8(self):
        return # will code if necessary
