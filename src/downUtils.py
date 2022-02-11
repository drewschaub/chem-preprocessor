import os
import urllib

def fetchData(dataFile, dataURL, dataPath):
    """fetches remote datafiles from URLs and saves in local datapath
    
    Path works for local path manipulation to ensure compatiability across
    operating sytems, but does not work for URLs. urllib is used for URLs
    and so uses strings, as opposed to Path objects.

    Args:
        dataFile (string): filename
        dataURL (string): root data URL
        dataPath (Path): local data path

    """
    os.makedirs(dataPath, exist_ok=True)
    dataFilepath = Path(dataPath, dataFile)
    fulldataURL = dataURL + dataFile
    urllib.request.urlretrieve(fulldataURL, dataFilepath)