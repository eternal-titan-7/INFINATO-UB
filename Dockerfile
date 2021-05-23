
FROM programmingerror/ultroid:v0.0.2

ENV TZ=Asia/Kolkata
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN apt-get autoremove --purge

RUN git clone https://github.com/coolfoolunidentifiedhacker/INFINATO-UB.git /root/INFINATO/

WORKDIR /root/INFINATO/

RUN pip3 install -r requirements.txt
RUN npm install -g npm@7.12.1 -g
RUN npm install
RUN npm run build