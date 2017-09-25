import json
from haralyzer import HarParser, HarPage

with open('../har/naver_chungnamUni.har', 'r') as f:
	har_parser = HarParser(json.loads(f.read()))

print(har_parser.browser)