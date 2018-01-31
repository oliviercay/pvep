# -*-coding:Utf-8 -*

import analysis.xml as x_an
import analysis.csv as c_an
import argparse

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-e", "--extension", help="""Type of file to analyse. Is it a CSV or an XML?""")
    parser.add_argument("-d","--datafile",help="""CSV file containing pieces of information about the members of parliament""")
    return parser.parse_args()

if __name__ == '__main__':
    args = parse_arguments()
    datafile = args.datafile
    if args.extension == 'xml':
        x_an.launch_analysis(datafile)
    elif args.extension == 'csv':
        c_an.launch_analysis(datafile)
