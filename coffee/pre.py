"""
Pre-process a syllabus (class schedule) file. 

"""
import logging
logging.basicConfig(format='%(levelname)s:%(message)s',
                    level=logging.INFO)
log = logging.getLogger(__name__)


def process(raw):
    """
    Line by line processing of syllabus file.  Each line that needs
    processing is preceded by 'head: ' for some string 'head'.  Lines
    may be continued if they don't contain ':'.  If # is the first
    non-blank character on a line, it is a comment ad skipped. 
    """

    cooked = []
    for line in raw:
        log.debug("Line: {}".format(line))
        line = line.strip()

        if len(line) == 0 or line[0] == '#':
            log.debug("Skipping line...")
            continue
        
        parts = line.split(';')
        log.debug("appending entry...")
        cooked.append({'address':parts[0] , 'description':parts[1]})

    return cooked


def main():
    f = open("data/restaurants.txt")
    parsed = process(f)
    print(parsed)


if __name__ == "__main__":
    main()