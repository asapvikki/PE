import json
with open('a.json') as json_file:
	data = json.load(json_file)
	ans = data["Records"][0]["s3"]["bucket"]["arn"]
print(ans)
