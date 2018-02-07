# -*-coding:Utf-8 -*

"""
============================================
  Analyse Woman / Man balance in Politics
============================================
"""

import argparse
import logging as lg
import re
import analysis.xml as x_an
import analysis.csv as c_an

def parse_arguments():
    """ Arguments parsing """
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--datafile", help="""CSV file containing pieces of
        information about the members of parliament""")
    parser.add_argument("-v", "--verbose", action='store_true', help="""Make the application
        talk!""")
    parser.add_argument("-p", "--byparty", action='store_true', help="""displays a graph for each
        political party""")
    parser.add_argument("-i", "--info", action='store_true', help="""information about the file""")
    parser.add_argument("-n", "--displaynames", action='store_true', help="""displays the names of
        all the mps""")
    parser.add_argument("-s", "--searchname", help="""search for a mp name""")
    parser.add_argument("-I", "--index", help="""displays information about the Ith mp""")
    parser.add_argument("-g", "--groupfirst", help="""displays a graph groupping all the 'g'
        biggest political parties""")
    parser.add_argument("-a", "--byage", help="""displays a graph for the MPs splitted between
        those who are over and those who are under the value of --byage""")
    return parser.parse_args()

if __name__ == '__main__':
    """
    Main instructions to run
    """
    args = parse_arguments()
    if args.verbose:
        lg.basicConfig(level=lg.DEBUG)
    try:
        datafile = args.datafile
        if not datafile:
            raise Warning('You must indicate a datafile!')
        else:
            res = re.search(r'^.+\.(\D{3})$', args.datafile)
            try:
                extension = res.group(1)
            except:
                raise Warning('The file name is incorrect')
            try:
                if extension == 'xml':
                    x_an.launch_analysis(datafile)
                elif extension == 'csv':
                    c_an.launch_analysis(datafile, args.byparty, args.info, args.displaynames,
                                         args.searchname, args.index, args.groupfirst, args.byage)
                else:
                    raise Warning('The extension must be xml or csv')
            except FileNotFoundError:
                lg.error("Ow :( The file was not found.")
            finally:
                lg.info('#################### Analysis is over ######################')
    except Warning as exception:
        lg.warning(exception)
