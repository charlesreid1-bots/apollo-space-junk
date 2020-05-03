FROM rainbowmindmachine/rainbowmindmachine:v23
MAINTAINER charles@charlesreid1.com

RUN git clone https://git.charlesreid1.com/bots/b-apollo.git /apollo
WORKDIR "/apollo/bot"
CMD ["/usr/bin/env","python","ApolloBotFlock.py"]

