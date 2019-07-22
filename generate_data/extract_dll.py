def Imported_DLL_and_API(pe):
    dlls = []
    apis = []
    try:
        temp = pe.DIRECTORY_ENTRY_IMPORT
    except:
        return dlls, apis

    for i in temp:
        if i.dll: dlls.append(str(i.dll.upper(), encoding="utf8"))
        for j in i.imports:
            if j.name: apis.append(str(j.name.upper(), encoding="utf8"))

    return dlls, apis