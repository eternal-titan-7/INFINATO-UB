
FROM ultroidteam/ultroid:0.0.3
#RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
#    dpkg -i ./google-chrome-stable_current_amd64.deb; apt -fqqy install && \
#    rm ./google-chrome-stable_current_amd64.deb
#RUN wget -O chromedriver.zip http://chromedriver.storage.googleapis.com/$(curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE)/chromedriver_linux64.zip  && \
#    unzip chromedriver.zip chromedriver -d /usr/bin/ && \
#    rm chromedriver.zip
RUN curl --silent --location https://deb.nodesource.com/setup_15.x | bash -
RUN apt-get install -y nodejs
RUN git clone https://github.com/coolfoolunidentifiedhacker/INFINATO-UB.git /root/INFINATO/
RUN git clone https://github.com/1Danish-00/glitch_me.git && pip install -e ./glitch_me
WORKDIR /root/INFINATO/

RUN pip3 install -r requirements.txt
RUN pip3 install --upgrade pip
RUN npm install -g npm@7.11.2 -g
RUN npm install
RUN npm run build