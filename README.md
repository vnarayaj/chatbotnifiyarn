1) enable docker on yarn
a) Yarn>config>settings> docker runtime>enabled
b) yarn.nodemanager.container-executor.class=org.apache.hadoop.yarn.server.nodemanager.LinuxContainerExecutor
c) yarn.nodemanager.runtime.linux.docker.default-container-network=bridge
d) yarn.nodemanager.runtime.linux.docker.allowed-container-networks=host,none,bridge
e) yarn.nodemanager.linux-container-executor.nonsecure-mode.local-user=dockeruser
f) yarn.nodemanager.runtime.linux.docker.privileged-containers.acl=root,dockeruser,ubuntu,yarn
g) enable yarn.nodemanager.runtime.linux.docker.privileged-containers.allowed
h) Enable Launching Privileged Containers in yarn
i) restart yarn
   



2) Install local docker repo
a) docker run -d -p 6666:5000 --restart=always --name registry -v /mnt/registry:/var/lib/registry registry:2 
b) add {"insecure-registries": ["localhost:6666"]} to /etc/docker/daemon.json
c) restart docker  (service docker restart)
d) In yarn set Docker Trusted Registries to localhost:6666 and restart yarn

3) git clone https://github.com/vnarayaj/chatbotnifiyarn.git

4) cd chatbotnifiyarn. unzip starspace_embedding.tsv.zip

5) cd chatbotnifiyarn/thread_embeddings_by_tags

6) cat embed.* >>emb.tar

7) tar -xvf emb.tar


8) build docker image 
cd chatbotnifiyarn
docker build -t nlp_image .

9) tag the image 
docker tag nlp_image:latest localhost:6666/nlp_image:latest

10) push the image into the local repository 
docker push localhost:6666/nlp_image:latest

11) edit Yarnfile to change /Downloads/chatbotnifiyarn  to the location where you cloned the project

12) curl -X POST -H "Content-Type: application/json" http://localhost:8088/app/v1/services?user.name=ubuntu -d @Yarnfile

13) curl http://localhost:8088/app/v1/services/nlp-service?user.name=ubuntu | python -m json.tool    
- get the ip address and telnet <ip address> 5000 to verify that the container is up and listenning on port 5000

14) install nifi (nifi.apache.org). cd /root/nifi-1.8.0/conf and edit nifi.properties 
nifi.web.http.port=9090
start nifi
/root/nifi-1.8.0/bin
export JAVA_HOME=/usr/jdk64/jdk1.8.0_112
./nifi.sh start

15) connect to http://<nifi host>:9090 and upload the template (nifibot.xml). Create a new dataflow from the template

12) Talk to @BotFather in Telegram. The command "/newbot" will create a bot for you. 
You will be prompted to enter a name and a username for your bot. After that, you will be given a token.

13) open the nifi flow and open the InvokeHTTP processor that has Remote URL like https://api.telegram.org/bot642016628:AAEI7IHimEhyBiNG30G_RqWKZxsE5cjJRkg/getUpdates?offset=${update_id}
change the 642016628:AAEI7IHimEhyBiNG30G_RqWKZxsE5cjJRkg to the token from your bot


14) start the nifi flow. Open the telegram messenger and interact with your bot
