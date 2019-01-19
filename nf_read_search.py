#!/usr/bin/env python
import re
import pytesseract
from PIL import Image

bill = pytesseract.image_to_string(Image.open('nf2.jpg'))

total = 0
date = None
for line in bill.split('\n'):
    print('Search on {}'.format(line))

    match_total = re.search('(total).{0,}R(\$|S|s) {0,}(\d{1,5}(,|\.)\d{2})', line, re.I)
    match_date = re.search('(\d{2}/\d{2}/\d{2,4})', line, re.I)

    if match_total:
        total = match_total.group(3)
    if match_date:
        date = match_date.group()
    

print('Total {}'.format(total))
print('Date {}'.format(date))
