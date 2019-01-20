#!/usr/bin/env python
import base64
import io
import pytesseract
import re

from PIL import Image


def get_bill_info(base64_img):
    img_string = base64_img
    img = io.BytesIO(base64.b64decode(img_string))
    bill_image = Image.open(img)
    bill_image.show()
    bill = { 'total': 0, 'date': None }

    for line in pytesseract.image_to_string(bill_image).split('\n'):
        match_total = re.search('(total).{0,}R(\$|S|s) {0,}(\d{1,5}(,|\.)\d{2})', line, re.I)
        match_date = re.search('(\d{2}/\d{2}/\d{2,4})', line, re.I)

        if match_total:
            bill['total']= match_total.group(3)
        if match_date:
            bill['date'] = match_date.group()
    return bill
