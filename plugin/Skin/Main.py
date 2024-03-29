# -*- coding: utf-8 -*-

from Screens.Screen import Screen
from Components.Pixmap import Pixmap

skin = """
<screen name="NGsettingE2" position="center,center" size="875,550" title="Main Menu" backgroundColor="#ff000000" flags="wfNoBorder" >
	<eLabel position="10,0" size="865,45" backgroundColor="#10101010" zPosition="0" />
	<eLabel position="10,0" size="1,45"   backgroundColor="#20202020" zPosition="0" />
	<eLabel position="10,0" size="865,1"  backgroundColor="#20202020" zPosition="0" />

	<ePixmap position="762,405" size="250,170" pixmap="~/Panel/logo.png" zPosition="5" alphaTest="blend" />
	<ePixmap position="330,4" size="300,40" pixmap="~/Panel/autosetting.png" zPosition="2" alphaTest="blend" />

	<!-- Text Maintain -->
	<widget name="text" position="10,52" size="243,440" font="Regular;25" horizontalAlignment="left" foregroundColor="#808080" backgroundColor="#10202020" transparent="1" zPosition="1" />

	<!-- Clock -->
	<widget source="global.CurrentTime" render="Label" position="690,10" size="230,30" font="Regular;24"  zPosition="2" foregroundColor="#404040" backgroundColor="#202020" horizontalAlignment="center" transparent="1">
		<convert type="ClockToText">Format %H:%M:%S</convert>
	</widget>

	<!-- Panel Menu SettingMan -->
	<eLabel position="10,50" size="240,440" backgroundColor="#10101010" zPosition="0" />
	<eLabel position="10,50" size="1,440" backgroundColor="#20303030" zPosition="0" />
	<eLabel position="10,50" size="240,1" backgroundColor="#20303030" zPosition="0" />

	<!-- Lists -->
	<widget name="A" position="6,52" size="243,400" foregroundColor="#707070" foregroundColorSelected="#ffffff" backgroundColor="#272e43" backgroundColorSelected="#272e43"
		scrollbarMode="showNever" selectionPixmap="~/Panel/slider.png"
		backgroundPixmap="~/Panel/sliderb.png"
		enableWrapAround="1"  transparent="1" zPosition="5" />

	<!-- Panel Setting Lists -->
	<eLabel position="255,50"  size="620,330" backgroundColor="#10101010" zPosition="0" />
	<eLabel position="255,50"  size="1,330"   backgroundColor="#303030"   zPosition="0" />
	<eLabel position="255,50"  size="620,1"   backgroundColor="#303030"   zPosition="0" />

	<!-- Lists -->
	<widget name="B"  position="257,52" size="617,315" scrollbarMode="showNever" enableWrapAround="1" transparent="1" zPosition="5"
		foregroundColor="#5dafff" foregroundColorSelected="#ffffff" backgroundColor="#303030" backgroundColorSelected="#002f72"
		selectionPixmap="~/Panel/slider35.png"
		backgroundPixmap="~/Panel/sliderp.png" />


	<!-- Panel Info -->
	<eLabel position="255,385"  size="620,105" backgroundColor="#10101010" zPosition="0" />
	<eLabel position="255,385"  size="1,105"   backgroundColor="#303030"   zPosition="0" />
	<eLabel position="255,385"  size="620,1"   backgroundColor="#303030"   zPosition="0" />

	<!-- Setting Installed Text / Update -->
	<widget position="270,405" size="200,24" name="Key_Green" font="Regular;20" horizontalAlignment="left" foregroundColor="#808080" backgroundColor="#101010" zPosition="1" transparent="1" />
	<widget position="440,405" size="410,31" name="namesat"  font="Regular;20" horizontalAlignment="left" foregroundColor="#ffffff" backgroundColor="#101010" transparent="1" zPosition="3" />

	<widget position="270,440" size="610,31" name="dataDow"     font="Regular;20" horizontalAlignment="left" foregroundColor="#808080" backgroundColor="#101010" transparent="1" zPosition="3" />
	<!--widget position="290,440" size="410,31" name="data"     font="Regular;20" horizontalAlignment="left" foregroundColor="#808080" backgroundColor="#101010" transparent="1" zPosition="3" /-->

	<!-- Lcn Green Button -->
	<widget  position="25,350" size="30,30"  name="Green" pixmap="~/Panel/greenpanel.png" zPosition="2" alphaTest="blend" />
	<widget  position="60,349" size="200,24" name="Key_Lcn" font="Regular;20" horizontalAlignment="left" foregroundColor="#808080" backgroundColor="#101010" zPosition="1" transparent="1" />

	<!-- Personal Yellow Button -->
	<widget  position="25,385" size="30,30"  name="Yellow" pixmap="~/Panel/yellowpanel.png" zPosition="2" alphaTest="blend" />
	<widget  position="60,384" size="200,24" name="Key_Personal" font="Regular;20" horizontalAlignment="left" foregroundColor="#808080" backgroundColor="#101010" zPosition="1" transparent="1" />

	<!-- AutoUpdate Blue Button -->
	<widget  position="25,420" size="30,30"  name="Blue" pixmap="~/Panel/bluepanel.png" zPosition="2" alphaTest="blend" />
	<widget  name="autotimer" position="60,419" size="200,30"  font="Regular;20" horizontalAlignment="left" foregroundColor="#808080" backgroundColor="#101010" transparent="1" zPosition="3" />

	<!-- Exit Button -->
	<ePixmap position="25,455" size="30,30" pixmap="~/Panel/redpanel.png" zPosition="2" alphaTest="blend" />
	<widget  position="60,454" size="200,24" name="Key_Red" font="Regular;20" horizontalAlignment="left" foregroundColor="#808080" backgroundColor="#101010" zPosition="1" transparent="1" />
</screen>"""
