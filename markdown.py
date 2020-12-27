import re


def parseHeadings(current_line):
    '''headings, also count headings level dynamically (## -> h2)'''
    heading_match = re.match('(#+)', current_line)
    if heading_match is not None:
        heading_level = len(heading_match[1])
        return '<h{0}>{1}</h{0}>'.format(heading_level,
                                         current_line[heading_level+1:])
    else:
        return current_line


def parseListItems(current_line):
    ''' list item (* -> <li>) '''
    match = re.match(r'\* (.*)', current_line)
    if match:
        return '<li>' + match.group(1) + '</li>'
    else:
        return current_line


def sourroundListItems(all_lines):
    ''' surround list of <li> elements with <ul> and </ul> '''

    # Detect list lines and expand beginning & end to make next loop work
    list_item_lines = \
        [[False, 0]] \
        + [[bool(re.match('<li', line)), idx+1]
           for idx, line in enumerate(all_lines)] \
        + [[False, len(all_lines)+1]]

    # Insert beginnings & ends of lists
    is_list_opened = False
    insert_offset = 1
    for cur_idx in range(0, len(list_item_lines)-1):
        if(list_item_lines[cur_idx][0] != list_item_lines[cur_idx+1][0]):
            cur_spot = list_item_lines[cur_idx][1]
            if not is_list_opened:
                all_lines.insert(cur_spot, "<ul>")
                is_list_opened = True
            else:
                all_lines.insert(cur_spot + insert_offset, "</ul>")
                insert_offset + 2
                is_list_opened = False

    return all_lines


def parseParagraph(current_line):
    ''' if it's simply a paragraph '''
    match = re.match('<h|<ul|<li', current_line)
    if not match:
        return '<p>' + current_line + '</p>'
    else:
        return current_line


def parseStrong(current_line):
    ''' strong (__ -> <strong>) '''
    match = re.match('(.*)__(.*)__(.*)', current_line)
    if match:
        return match.group(1) \
            + '<strong>' + match.group(2) + '</strong>' \
            + match.group(3)
    else:
        return current_line


def parseEmphasized(current_line):
    ''' emphasized (_ -> <em>) '''
    match = re.match('(.*)_(.*)_(.*)', current_line)
    if match:
        return match.group(1) \
            + '<em>' + match.group(2) + '</em>' \
            + match.group(3)
    else:
        return current_line


def parse(markdown):
    ''' main parse function, that is converting a markdown file'''
    parsed_lines = \
        sourroundListItems([
            parseEmphasized(
                parseStrong(
                    parseParagraph(
                        parseListItems(
                            parseHeadings(current_line))))) for current_line in markdown.split('\n')])

    return ''.join((parsed_lines))