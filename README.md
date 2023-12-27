# steal-metamask-vault
vault extractor on **chrome & brave browser**. For more detailed information, you can read [my blog post](https://sobhan.hashnode.dev/security-exploration-of-metamask-introducing-and-using-the-metamaskvaultextractor-script) dedicated to this project.
## Server

### Usage
1. Install the required packages using `pip install -r requirements.txt`.
2. Run `python server.py` on your server.
3. The server will be running at **http://0.0.0.0:5000/**.

## Client

### Usage
1. Install the required packages using `pip install -r requirements.txt`.
2. Update the **token** variable in **client.py** with your authentication token.
3. Update the **url** variable in **client.py** with the IP address and port of your server.
4. Run `python client.py` on your local machine.
#### The client will upload .log files from Chrome and Brave browsers to the server.

## Contribution
Contributions to this project are highly appreciated. You can contribute by submitting pull requests or by reporting issues and suggestions for improvement. You can also ask your questions in the Issues section.

## Contact
- For more information, you can visit [my website](http://sobhan.hashnode.dev).
- For questions and suggestions, you can contact me via email: xd3vman@gmail.com
