# -*-coding:Utf-8 -*

import analysis.xml as x_an
import analysis.csv as c_an
import argparse
import logging as lg

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-e", "--extension", help="""Type of file to analyse. Is it a CSV or an XML?""")
    parser.add_argument("-d","--datafile",help="""CSV file containing pieces of information about the members of parliament""")
    parser.add_argument("-v", "--verbose", action='store_true', help="""Make the application talk!""")
    parser.add_argument("-p","--byparty",action='store_true',help="displays a graph for each political party")
    return parser.parse_args()

if __name__ == '__main__':
    args = parse_arguments()
    if args.verbose:
        lg.basicConfig(level=lg.DEBUG)
    try:
        datafile = args.datafile
        extension = args.extension
        if not datafile :
            raise Warning('You must indicate a datafile!')
        elif not extension:
            raise Warning('You must indicate an extension')
        else:
            try:
                if extension == 'xml':
                    x_an.launch_analysis(datafile)
                elif extension == 'csv':
                    c_an.launch_analysis(datafile, args.byparty)
            except FileNotFoundError as e:
                lg.error("Ow :( The file was not found.")
            finally:
                lg.info('#################### Analysis is over ######################')
    except Warning as e:
        lg.warning(e)
        
