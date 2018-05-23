///Add
#ifdef HIDE_OBJECTS
PyObject * backgroundIsVisiblePart(PyObject * poSelf, PyObject * poArgs)
{
	int ePart;
	if (!PyTuple_GetInteger(poArgs, 0, &ePart))
		return Py_BadArgument();

	if (ePart>=CMapOutdoor::PART_NUM)
		return Py_BuildException("ePart(%d)<background.PART_NUM(%d)", ePart, CMapOutdoor::PART_NUM);
	
	CPythonBackground& rkBG = CPythonBackground::Instance();
	CMapOutdoor& rkMap = rkBG.GetMapOutdoorRef();

	return Py_BuildValue("i", rkMap.IsVisiblePart(ePart));
}
#endif
//Find
		{ "SetVisiblePart",						backgroundSetVisiblePart,					METH_VARARGS },

///Add
		#ifdef HIDE_OBJECTS
		{ "IsVisiblePart",						backgroundIsVisiblePart,					METH_VARARGS },
		#endif