# parse an iframe tag and extract the YT URL
import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    # check there's an iframe, if not return None
    if re.search(r"<iframe(.+)?><\/iframe>", s):
        # parse the URL and create groups with ()s
        full_url = re.search(r"(http(s)?:\/\/(www\.)*youtube\.com\/embed\/)([a-zA-Z0-9_]+)", s)
        if full_url:
            # return the new URL
            return("https://youtu.be/" + full_url.group(4))
    else:
        return(None)


if __name__ == "__main__":
    main()
