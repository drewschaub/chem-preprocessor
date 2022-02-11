import gzip
import os
import tarfile
import urllib
from pathlib import Path

def fetchData(dataFile, dataURL, dataPath, extract=False):
    """fetches remote datafiles from URLs and saves in local datapath
    
    Path works for local path manipulation to ensure compatiability across
    operating sytems, but does not work for URLs. urllib is used for URLs
    and so uses strings, as opposed to Path objects.

    Args:
        dataFile (string): filename
        dataURL (string): root data URL
        dataPath (Path): local data path
        extract (Boolean): option to extract tarfiles
        extractType (string): specify compression type: ['gunzip', 'tar']

    """
    os.makedirs(dataPath, exist_ok=True)
    dataFilepath = Path(dataPath, dataFile)
    fulldataURL = dataURL + dataFile
    urllib.request.urlretrieve(fulldataURL, dataFilepath)

    if extract:
        compressedFile  = dataFilepath
        while compressedFile.suffix in {'.tar', '.gz', '.zip'}:
            decompressedFile = compressedFile.with_suffix('')

        if compressedFile.suffix == 'tgz':
            tgzFile = tarfile.open(compressedFile)
            tgzFile.extractall(path=dataPath)
            tgzFile.close()

        if compressedFile.suffix == 'gz':
            blockSize=65536

            input = gzip.GzipFile(compressedFile, 'wb').read()
            input.close()

            output = open(decompressedFile, 'wb')
            output.write(input)
            output.close()