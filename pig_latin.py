def translate(text):
    if len(text.split(' ')) > 1:
        text_list = []
        for i in text.split(' '):
            text_list.append(translate(i))
        return ' '.join(text_list)

    if text[0] in ['a', 'e', 'i', 'o', 'u'] or text[:2] in ['xr', 'yt']:
        return text + 'ay'

    elif text[:3] in ['squ', 'sch', 'thr']:
        return text[3:] + text[:3] + 'ay'

    elif text[:2] in ['ch', 'rh', 'hr', 'qu', 'th']:
        return text[2:] + text[:2] + 'ay'

    else:
        return text[1:] + text[0] + 'ay'
