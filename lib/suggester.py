import requests

class ActivitySuggester:
    url = "https://bored-api.appbrewery.com/random"
    def suggest(self):
        response = self._make_request_to_api()
        print("response ->", response)
        return f"Why not: {response['activity']}"

    def _make_request_to_api(self):
        response = requests.get(self.url)
        if response.status_code != 200:
            print("invalid status code from server:", response.status_code)
            return response.content
        return response.json()

def main():
    try:
        activity = ActivitySuggester()
        print(activity.suggest())
    except Exception as err:
        print(err)


main()

