# This is a simple scraper designed to mass download deepfake images from https://thispersondoesnotexist.com

import urllib.request
import time  # Used for the sleep function.
import random

def download_from_thispersondoesnotexist(file_index_number):
    opener = urllib.request.build_opener()

    # They seem to block the normal user agent to stop bots.
    # So the header is modified to pass.
    opener.addheaders = [('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)')]
    urllib.request.install_opener(opener)

    # The image is currently served here.
    # The image seems to be randomized from their backend.
    # Filename format: Deepfake_TPDNE_NUMBER.jpg
    filename = 'Deepfake_TPDNE_'+file_index_number+'.jpg'
    target_url = "https://thispersondoesnotexist.com/image"

    # Download it.
    urllib.request.urlretrieve(target_url, filename)
    # Report to console.
    print("Downloaded: " + filename)


if __name__ == "__main__":
    # If the script dies reboot with whatever number you are on. Last image as 131 so type in 131 when you start again.
    for x in range(1913, 2000):  # Loop for 2000 times: range(0, 2000)
        time.sleep(0.75)  # Wait in between calls.
        download_from_thispersondoesnotexist(str(x+1))
        #if x % 10 == 0:
            #time.sleep(random.randint(1, 10))  # Random Wait
