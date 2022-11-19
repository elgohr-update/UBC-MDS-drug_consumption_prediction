"""This script downloads data given a URL and local file path.
Usage: download_data.py --url=<url> --file_path=<file_path>
Options:
--url=<url>                 Takes in the url (this is a required option)
--file_path=<file_path>     Takes in the local file path (this is a required option)
""" 

from docopt import docopt
import pandas as pd
import os

def main(opt):
    data = pd.read_csv(opt["--url"], header=None)
    filepath = os.path.join(opt["--file_path"] , "drug_consumption.csv")
    data.to_csv(filepath, index = False)

if __name__ == '__main__':
    arguments = docopt(__doc__)
    main(arguments)
