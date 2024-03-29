# -*- coding: utf-8 -*-
from random import choice
import re
import glob
import shutil
import os
import urllib2
import time
import sys
from Screens.Screen import Screen
from enigma import *
from Config import *
from Language import _
from Tools.Directories import resolveFilename, SCOPE_PLUGINS

Directory = os.path.dirname(sys.modules[__name__].__file__)
MinStart = int(choice(range(59)))


def DownloadPlugin(link):
    try:
        req = urllib2.Request(link)
        req.add_header('User-Agent', "VAS14")
        response = urllib2.urlopen(req)
        link = response.read()
        response.close()
        Setting = open('/tmp/Plugin.zip', 'w')
        Setting.write(link)
        Setting.close()
        try:
            os.system("unzip -o /tmp/Plugin.zip -d  /usr/lib/enigma2/python/Plugins/Extensions")
        except:
            return
    except:
        return
    return True


def TimerControl():
    now = time.localtime(time.time())
    Ora = str(now[3]).zfill(2) + ':' + str(now[4]).zfill(2) + ':' + str(now[5]).zfill(2)
    Date = str(now[2]).zfill(2) + '-' + str(now[1]).zfill(2) + '-' + str(now[0])
    return '%s ora: %s' % (Date, Ora)


def StartSavingTerrestrialChannels():

    def ForceSearchBouquetTerrestrial():
        for file in sorted(glob.glob("/etc/enigma2/*.tv")):
            f = open(file, "r").read()
            x = f.strip().lower()
            if x.find('eeee0000') != -1:
                if x.find('82000') == -1 and x.find('c0000') == -1:
                    return file
                    break
        return

    def ResearchBouquetTerrestrial(search):
        for file in sorted(glob.glob("/etc/enigma2/*.tv")):
            f = open(file, "r").read()
            x = f.strip().lower()
            x1 = f.strip()
            if x1.find("#NAME") != -1:
                if x.lower().find((search.lower())) != -1:
                    if x.find('eeee0000') != -1:
                        return file
                        break
        return

    def SaveTrasponderService():
        TrasponderListOldLamedb = open(Directory + '/NGsetting/Temp/TrasponderListOldLamedb', 'w')
        ServiceListOldLamedb = open(Directory + '/NGsetting/Temp/ServiceListOldLamedb', 'w')
        Trasponder = False
        inTransponder = False
        inService = False
        try:
            LamedbFile = open('/etc/enigma2/lamedb')
            while True:
                line = LamedbFile.readline()
                if not line:
                    break
                if not (inTransponder or inService):
                    if line.find('transponders') == 0:
                        inTransponder = True
                    if line.find('services') == 0:
                        inService = True
                if line.find('end') == 0:
                    inTransponder = False
                    inService = False
                line = line.lower()
                if line.find('eeee0000') != -1:
                    Trasponder = True
                    if inTransponder:
                        TrasponderListOldLamedb.write(line)
                        line = LamedbFile.readline()
                        TrasponderListOldLamedb.write(line)
                        line = LamedbFile.readline()
                        TrasponderListOldLamedb.write(line)
                    if inService:
                        tmp = line.split(':')
                        ServiceListOldLamedb.write(tmp[0] + ":" + tmp[1] + ":" + tmp[2] + ":" + tmp[3] + ":" + tmp[4] + ":0\n")
                        line = LamedbFile.readline()
                        ServiceListOldLamedb.write(line)
                        line = LamedbFile.readline()
                        ServiceListOldLamedb.write(line)
            TrasponderListOldLamedb.close()
            ServiceListOldLamedb.close()
            if not Trasponder:
                os.system('rm -fr ' + Directory + '/NGsetting/Temp/TrasponderListOldLamedb')
                os.system('rm -fr ' + Directory + '/NGsetting/Temp/ServiceListOldLamedb')
        except:
            pass
        return Trasponder

    def CreateBouquetForce():
        WritingBouquetTemporary = open(Directory + '/NGsetting/Temp/TerrestrialChannelListArchive', 'w')
        WritingBouquetTemporary.write('#NAME terrestre\n')
        ReadingTempServicelist = open(Directory + '/NGsetting/Temp/ServiceListOldLamedb').readlines()
        for jx in ReadingTempServicelist:
            if jx.find('eeee') != -1:
                String = jx.split(':')
                WritingBouquetTemporary.write('#SERVICE 1:0:%s:%s:%s:%s:%s:0:0:0:\n' % (hex(int(String[4]))[2:], String[0], String[2], String[3], String[1]))
        WritingBouquetTemporary.close()

    def SaveBouquetTerrestrial():
        NameDirectory = ResearchBouquetTerrestrial('terr')
        if not NameDirectory:
            NameDirectory = ForceSearchBouquetTerrestrial()
        try:
            shutil.copyfile(NameDirectory, Directory + '/NGsetting/Temp/TerrestrialChannelListArchive')
            return True
        except:
            pass
        return

    Service = SaveTrasponderService()
    if Service:
        if not SaveBouquetTerrestrial():
            CreateBouquetForce()
        return True
    return


def TransferBouquetTerrestrialFinal():

    def RestoreTerrestrial():
        for file in os.listdir("/etc/enigma2/"):
            if re.search('^userbouquet.*.tv', file):
                f = open("/etc/enigma2/" + file, "r")
                x = f.read()
                if re.search("#NAME Digitale Terrestre", x, flags=re.IGNORECASE):
                    return "/etc/enigma2/" + file
        return

    try:
        TerrestrialChannelListArchive = open(Directory + '/NGsetting/Temp/TerrestrialChannelListArchive').readlines()
        DirectoryUserBouquetTerrestrial = RestoreTerrestrial()
        if DirectoryUserBouquetTerrestrial:
            TrasfBouq = open(DirectoryUserBouquetTerrestrial, 'w')
            for Line in TerrestrialChannelListArchive:
                if Line.lower().find('#name') != -1:
                    TrasfBouq.write('#NAME Digitale Terrestre\n')
                else:
                    TrasfBouq.write(Line)
            TrasfBouq.close()
            return True
    except:
        return False
    return

#added to keep iptv userbouquet.tv files, returns @list of files with "http" inside


def SearchIPTV():

	   iptv_list = []
	   for iptv_file in sorted(glob.glob("/etc/enigma2/userbouquet.*.tv")):
        usbq = open(iptv_file, "r").read()
        usbq_lines = usbq.strip().lower()
        if "http" in usbq_lines:
		  iptv_list.append(os.path.basename(iptv_file))

    	   if not iptv_list:
		return False
	   else:
		return iptv_list


def StartProcess(link, type, Personal):

    def LamedbRestore():
        try:

            TrasponderListNewLamedb = open(Directory + '/NGsetting/Temp/TrasponderListNewLamedb', 'w')
            ServiceListNewLamedb = open(Directory + '/NGsetting/Temp/ServiceListNewLamedb', 'w')
            inTransponder = False
            inService = False
            infile = open("/etc/enigma2/lamedb")
            while True:
                line = infile.readline()
                if not line:
                    break
                if not (inTransponder or inService):
                    if line.find('transponders') == 0:
                        inTransponder = True
                    if line.find('services') == 0:
                        inService = True
                if line.find('end') == 0:
                    inTransponder = False
                    inService = False
                if inTransponder:
                    TrasponderListNewLamedb.write(line)
                if inService:
                    ServiceListNewLamedb.write(line)
            TrasponderListNewLamedb.close()
            ServiceListNewLamedb.close()
            WritingLamedbFinal = open("/etc/enigma2/lamedb", "w")
            WritingLamedbFinal.write("eDVB services /4/\n")
            TrasponderListNewLamedb = open(Directory + '/NGsetting/Temp/TrasponderListNewLamedb').readlines()
            for x in TrasponderListNewLamedb:
                WritingLamedbFinal.write(x)
            try:
                TrasponderListOldLamedb = open(Directory + '/NGsetting/Temp/TrasponderListOldLamedb').readlines()
                for x in TrasponderListOldLamedb:
                    WritingLamedbFinal.write(x)
            except:
                pass
            WritingLamedbFinal.write("end\n")
            ServiceListNewLamedb = open(Directory + '/NGsetting/Temp/ServiceListNewLamedb').readlines()
            for x in ServiceListNewLamedb:
                WritingLamedbFinal.write(x)
            try:
                ServiceListOldLamedb = open(Directory + '/NGsetting/Temp/ServiceListOldLamedb').readlines()
                for x in ServiceListOldLamedb:
                    WritingLamedbFinal.write(x)
            except:
                pass
            WritingLamedbFinal.write("end\n")
            WritingLamedbFinal.close()
            return True
        except:
            return False

    def DownloadSettingAgg(link):
        try:
            req = urllib2.Request(link)
            req.add_header('User-Agent', "VAS14")
            response = urllib2.urlopen(req)
            link = response.read()
            response.close()
            Setting = open(Directory + '/NGsetting/Temp/listaE2.zip', 'w')
            Setting.write(link)
            Setting.close()
            if os.path.exists(Directory + "/NGsetting/Temp/listaE2.zip"):
                os.system("mkdir " + Directory + "/NGsetting/Temp/setting")
                try:
                    os.system("unzip " + Directory + "/NGsetting/Temp/listaE2.zip -d  " + Directory + "/NGsetting/Temp/setting")
                except:
                    pass
                os.system("mkdir " + Directory + "/NGsetting/Temp/enigma2")
                os.system("find " + Directory + "/NGsetting/Temp/setting -type f -print| sed 's/ /\" \"/g'| awk '{ str=$0; sub(/\.\//, \"\", str); gsub(/.*\//, \"\", str);print\"mv \" $0 \" " + Directory + "/NGsetting/Temp/enigma2/\"str }' | sh")
                if os.path.exists(Directory + "/NGsetting/Temp/enigma2/lamedb"):
                    return True
            return False
        except:
            return

    def SaveList(list):
        jw = open(resolveFilename(SCOPE_PLUGINS, 'Extensions/NGsetting/Moduli/NGsetting/SelectBack'), 'w')
        for dir, name in list:
            jw.write(dir + '---' + name + '\n')
        jw.close()

    def SavePersonalSetting():
        try:
            os.system('mkdir ' + Directory + '/NGsetting/SelectFolder')
            jw = open(resolveFilename(SCOPE_PLUGINS, 'Extensions/NGsetting/Moduli/NGsetting/Select'))
            jjw = jw.readlines()
            jw.close()
            count = 1
            list = []
            for x in jjw:
                try:
                    jx = x.split('---')
                    newfile = 'userbouquet.NgSetting' + str(count) + '.tv'
                    os.system('cp /etc/enigma2/' + jx[0] + ' /' + Directory + '/NGsetting/SelectFolder/' + newfile)
                    list.append((newfile, jx[1]))
                    count = count + 1
                except:
                    pass
            SaveList(list)
        except:
            return
        return True

    def TransferPersonalSetting():
        try:
            jw = open(resolveFilename(SCOPE_PLUGINS, 'Extensions/NGsetting/Moduli/NGsetting/SelectBack'))
            jjw = jw.readlines()
            jw.close()
            for x in jjw:
                try:
                    jx = x.split('---')
                    os.system("cp -rf " + Directory + '/NGsetting/SelectFolder/' + jx[0] + "  /etc/enigma2/")
                except:
                    pass
        except:
            pass
        return True

    def CreateUserbouquetPersonalSetting():
        try:
            jw = open(resolveFilename(SCOPE_PLUGINS, 'Extensions/NGsetting/Moduli/NGsetting/SelectBack'))
            jjw = jw.readlines()
            jw.close()
        except:
            pass
        jRewriteBouquet = open("/etc/enigma2/bouquets.tv")
        RewriteBouquet = jRewriteBouquet.readlines()
        jRewriteBouquet.close()
        WriteBouquet = open("/etc/enigma2/bouquets.tv", "w")
        Counter = 0
        for xx in RewriteBouquet:
            if Counter == 1:
                for x in jjw:
                    if x[0].strip() != '':
                        try:
                            jx = x.split('---')
                            WriteBouquet.write('#SERVICE 1:7:1:0:0:0:0:0:0:0:FROM BOUQUET "' + jx[0].strip() + '" ORDER BY bouquet\n')
                        except:
                            pass
                WriteBouquet.write(xx)
            else:
                WriteBouquet.write(xx)
            Counter = Counter + 1
        WriteBouquet.close()

    #added for IPTV
    def KeepIPTV():
	    	iptv_to_save = SearchIPTV()
		if iptv_to_save:

	      		for iptv in iptv_to_save:
		   		os.system("cp -rf /etc/enigma2/" + iptv + " " + Directory + "/NGsetting/Temp/enigma2/" + iptv)

    def TransferNewSetting():
        try:

	      #keep IPTV
	      KeepIPTV()

            os.system("rm -rf /etc/enigma2/lamedb")
            os.system("rm -rf /etc/enigma2/*.radio")
            os.system("rm -rf /etc/enigma2/*.tv")
            os.system("cp -rf " + Directory + "/NGsetting/Temp/enigma2/*.tv  /etc/enigma2/")
            os.system("cp -rf " + Directory + "/NGsetting/Temp/enigma2/*.radio  /etc/enigma2/")
            os.system("cp -rf " + Directory + "/NGsetting/Temp/enigma2/lamedb  /etc/enigma2/")
            if not os.path.exists("/etc/enigma2/blacklist"):
                os.system("cp -rf " + Directory + "/NGsetting/Temp/enigma2/blacklist /etc/enigma2/")
            if not os.path.exists("/etc/enigma2/whitelist"):
                os.system("cp -rf " + Directory + "/NGsetting/Temp/enigma2/whitelist /etc/enigma2/")
            os.system("cp -rf " + Directory + "/NGsetting/Temp/enigma2/satellites.xml /etc/tuxbox/")
        except:
            return
        return True
    Status = True
    if int(type) == 1:
        SavingProcessTerrestrialChannels = StartSavingTerrestrialChannels()
        os.system('cp -r /etc/enigma2/ ' + Directory + '/NGsetting/enigma2')
    if not DownloadSettingAgg(link):
        os.system('cp   ' + Directory + '/NGsetting/enigma2/* /etc/enigma2')
        os.system('rm -fr ' + Directory + '/NGsetting/enigma2')
        Status = False
    else:
        personalsetting = False
        if int(Personal) == 1:
            personalsetting = SavePersonalSetting()
        if TransferNewSetting():
            if personalsetting:
                if TransferPersonalSetting():
                    CreateUserbouquetPersonalSetting()
                    os.system('rm -fr ' + Directory + '/NGsetting/SelectFolder')
                    os.system('mv /usr/lib/enigma2/python/Plugins/Extensions/NGsetting/Moduli/NGsetting/SelectBack /usr/lib/enigma2/python/Plugins/Extensions/NGsetting/Moduli/NGsetting/Select')
            os.system('rm -fr ' + Directory + '/NGsetting/enigma2')
        else:
            os.system('cp   ' + Directory + '/NGsetting/enigma2/* /etc/enigma2')
            os.system('rm -fr ' + Directory + '/NGsetting/Temp/*')
            Status = False
        if int(type) == 1 and Status:
            if SavingProcessTerrestrialChannels:
                if LamedbRestore():
                    TransferBouquetTerrestrialFinal()
    os.system('rm -fr ' + Directory + '/NGsetting/Temp/*')# Delete all files and run a rescue reload
    return Status
