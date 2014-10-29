#!/usr/bin/python 
#coding:utf-8 
 
import json 
import urllib2 
from urllib2 import URLError 
import sys 
 
class ZabbixTools: 
    def __init__(self): 
        self.url = 'http://lihuipeng.blog.51cto.com/zabbix/api_jsonrpc.php' 
        self.header = {"Content-Type":"application/json"} 
         
         
         
    def user_login(self): 
        data = json.dumps({ 
                           "jsonrpc": "2.0", 
                           "method": "user.login", 
                           "params": { 
                                      "user": "Admin", 
                                      "password": "lihuipeng" 
                                      }, 
                           "id": 0 
                           }) 
         
        request = urllib2.Request(self.url, data) 
        for key in self.header: 
            request.add_header(key, self.header[key]) 
     
        try: 
            result = urllib2.urlopen(request) 
        except URLError as e: 
            print "Auth Failed, please Check your name and password:", e.code 
        else: 
            response = json.loads(result.read()) 
            result.close() 
            #print response['result'] 
            self.authID = response['result'] 
            return self.authID 
         
    def host_get(self): 
        data = json.dumps({ 
                           "jsonrpc":"2.0", 
                           "method":"host.get", 
                           "params":{ 
                                     "output":["hostid","name"], 
                                     "filter":{"host":""} 
                                     }, 
                           "auth":self.user_login(), 
                           "id":1, 
                           }) 
         
        request = urllib2.Request(self.url, data) 
        for key in self.header: 
            request.add_header(key, self.header[key]) 
             
     
        try: 
            result = urllib2.urlopen(request) 
        except URLError as e: 
            if hasattr(e, 'reason'): 
                print 'We failed to reach a server.' 
                print 'Reason: ', e.reason 
            elif hasattr(e, 'code'): 
                print 'The server could not fulfill the request.' 
                print 'Error code: ', e.code 
        else: 
            response = json.loads(result.read()) 
            result.close() 
            print "Number Of Hosts: ", len(response['result']) 
            for host in response['result']: 
                print "Host ID:",host['hostid'],"Host Name:",host['name'] 
                 
    def hostgroup_get(self, hostgroupName): 
        data = json.dumps({ 
                           "jsonrpc":"2.0", 
                           "method":"hostgroup.get", 
                           "params":{ 
                                     "output": "extend", 
                                     "filter": { 
                                                "name": [ 
                                                         hostgroupName, 
                                                         ] 
                                                } 
                                     }, 
                           "auth":self.user_login(), 
                           "id":1, 
                           }) 
         
        request = urllib2.Request(self.url, data) 
        for key in self.header: 
            request.add_header(key, self.header[key]) 
              
        try: 
            result = urllib2.urlopen(request) 
        except URLError as e: 
            print "Error as ", e 
        else: 
            response = json.loads(result.read()) 
            result.close() 
            print "hostgroup : %s ------ id : %s" % (response['result'][0]['name'], response['result'][0]['groupid']) 
            self.hostgroupID = response['result'][0]['groupid'] 
            return response['result'][0]['groupid'] 
             
    def template_get(self, templateName): 
        data = json.dumps({ 
                           "jsonrpc":"2.0", 
                           "method": "template.get", 
                           "params": { 
                                      "output": "extend", 
                                      "filter": { 
                                                 "host": [ 
                                                          templateName, 
                                                          ] 
                                                 } 
                                      }, 
                           "auth":self.user_login(), 
                           "id":1, 
                           }) 
         
        request = urllib2.Request(self.url, data) 
        for key in self.header: 
            request.add_header(key, self.header[key]) 
              
        try: 
            result = urllib2.urlopen(request) 
        except URLError as e: 
            print "Error as ", e 
        else: 
            response = json.loads(result.read()) 
            result.close() 
            print "template : %s ------ id : %s" % (response['result'][0]['name'], response['result'][0]['templateid']) 
            self.templateID = response['result'][0]['templateid'] 
            return response['result'][0]['templateid'] 
                 
    def host_create(self, hostip, hostgroupName, templateName): 
        data = json.dumps({ 
                           "jsonrpc":"2.0", 
                           "method":"host.create", 
                           "params":{ 
                                     "host": hostip, 
                                     "interfaces": [ 
                                                        { 
                                                            "type": 1, 
                                                            "main": 1, 
                                                            "useip": 1, 
                                                            "ip": hostip, 
                                                            "dns": "", 
                                                            "port": "10050" 
                                                        } 
                                                    ], 
                                    "groups": [ 
                                                    { 
                                                        "groupid": self.hostgroup_get(hostgroupName) 
                                                    } 
                                               ], 
                                    "templates": [ 
                                                    { 
                                                        "templateid": self.template_get(templateName) 
                                                    } 
                                                  ], 
                                     }, 
                           "auth": self.user_login(), 
                           "id":1                   
        }) 
        request = urllib2.Request(self.url, data) 
        for key in self.header: 
            request.add_header(key, self.header[key]) 
              
        try: 
            result = urllib2.urlopen(request) 
        except URLError as e: 
            print "Error as ", e 
        else: 
            response = json.loads(result.read()) 
            result.close() 
            print "host : %s ------ id : %s" % (hostip, response['result']['hostids']) 
            self.hostid = response['result']['hostids'] 
            return response['result']['hostids'] 
         
                 
                 
if __name__ == "__main__": 
    if len(sys.argv) != 4: 
        print "Usage: %s ip hostgroupName templateName" % sys.argv[0] 
        sys.exit(1) 
         
    test = ZabbixTools() 
    test.host_create(sys.argv[1], sys.argv[2], sys.argv[2]) 