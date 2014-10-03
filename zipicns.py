#!/usr/bin/python2.7
import os.path
import sys
import re
import shutil
import os

class IconSet:

    def __init__(self, theme='hicolor', rootdir='/opt/local/share/icons'):
            print "hello world"
            self.target_theme = theme
            self.macPortsRootShare = rootdir
            if len(sys.argv) > 2:
                self.target_theme = sys.argv[2]
                
            if len(sys.argv) > 3:
                self.context = sys.argv[3]
            else:
                self.context = 'Applications'
                
    
    def parse_file(self, indexfile, targ_group):
        new_dict = {}
        nf = open(indexfile, 'r')
        try:
            new_dict = {}
            for line in nf:
                group_pat = re.search('((?<=^\[).*(?=\]))', line)
                if group_pat:
                    cur_gr = group_pat.group(1)
                if cur_gr == targ_group:
                    key_pat = re.search('(^[^=]+)\=(.*$)', line)
                    if key_pat:
                        new_dict[key_pat.group(1)] = key_pat.group(2)
        finally:
            nf.close()
        return new_dict
    
    def main(self, target_app):
        #if self.context:
        #    context = self.context
        self.target_app = target_app
        test_dict = self.parse_file(self.macPortsRootShare+'/'+self.target_theme+'/index.theme', 'Icon Theme')
        
        icns_set = '/var/tmp/'+self.target_app+'.iconset'
        
        if os.path.isdir(icns_set) is False:
            os.mkdir(icns_set)
        
        standard_sizes = []
        
        for d in test_dict['Directories'].split(','):
            test_dict2 = {}
            test_dict2 = self.parse_file(self.macPortsRootShare+'/'+self.target_theme+'/index.theme', d)
            
            if test_dict2['Context'] == self.context:
                testPath = self.macPortsRootShare + '/'+self.target_theme+'/' + d + '/'+self.target_app+'.png'
                
                if os.path.isfile(testPath):
                    img_size = int(test_dict2['Size'])
                    img_size2x = img_size / 2
                    
                    standard_sizes.append(img_size)
                    
                    shutil.copyfile(testPath, icns_set+'/icon_'+str(img_size)+'x'+str(img_size)+'.png')
                    print testPath, 'icon_'+str(img_size)+'x'+str(img_size)+'.png'
                    
                    if img_size2x in standard_sizes:
                        shutil.copyfile(testPath, icns_set+'/icon_'+str(img_size2x)+'x'+str(img_size2x)+'@2x.png')
                        print testPath, 'icon_'+str(img_size2x)+'x'+str(img_size2x)+'@2x.png'
                    
            
var1 = IconSet()

var1.main(sys.argv[1])

print "Theme", var1.target_theme
print "Context:", var1.context

exit()