#Find
		self.blockButtonList = []
		
#Add
		if app.ENABLE_HIDE_OBJECTS:
			self.VisibleButtonList = []

#Find
			self.pvpModeButtonDict[player.PK_MODE_FREE] = GetObject("pvp_free")
		
#Add
			if app.ENABLE_HIDE_OBJECTS:
				for bl in xrange(5):
					self.VisibleButtonList.append(GetObject("vsble" + str(bl)))
					
#Find
		self.alwaysShowNameButtonList[1].SAFE_SetEvent(self.__OnClickAlwaysShowNameOffButton)
			
#Add
		if app.ENABLE_HIDE_OBJECTS:	
			for bl in xrange(5):
				self.VisibleButtonList[bl].SetToggleUpEvent(lambda arg=bl: self.SetVisibleFunc(arg))
				self.VisibleButtonList[bl].SetToggleDownEvent(lambda arg=bl: self.SetVisibleFunc(arg))
				
#Add this Func
	if app.ENABLE_HIDE_OBJECTS:		
		def SetVisibleFunc(self, index):
			mylist = [background.PART_TREE, background.PART_CLOUD, background.PART_WATER, background.PART_OBJECT, background.PART_TERRAIN]
			background.SetVisiblePart(mylist[index], not background.IsVisiblePart(mylist[index]))
			for bl in xrange(5):
				if background.IsVisiblePart(mylist[bl]):
					self.VisibleButtonList[bl].SetUp()
				else:
					self.VisibleButtonList[bl].Down()