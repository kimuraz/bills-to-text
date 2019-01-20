install:
	@echo Installing bills-to-text
	@mkdir -p /opt/bills-to-text/imgs
	@apk add build-base python-dev py-pip jpeg-dev zlib-dev
	@apk add tesseract-ocr
	@pip install -r requirements.txt
	@rm requirements.txt


uninstall:
	@echo Uninstalling bills-to-text...
	@rm -rf /opt/bills-to-text
