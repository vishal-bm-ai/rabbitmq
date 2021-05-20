RABBITMQ_NODE_PORT=5673 
RABBITMQ_SERVER_START_ARGS="-rabbitmq_management listener [{port,15673}]
-rabbitmq_mqtt tcp_listeners [1884]
-rabbitmq_stomp tcp_listeners [61614]"
RABBITMQ_NODENAME=hare rabbitmq-server

-rabbitmq_prelaunch prelaunch [25674]


docker run -d \
    --name="rabbit1" \
    --hostname="rabbit1"\
    -e RABBITMQ_ERLANG_COOKIE="secret string" \
    -e RABBITMQ_NODENAME="rabbit1" \
    --volume={pwd}/rabbitmq.config:/etc/rabbitmq/rabbitmq.config \
    --volume=(pwd)/definitions.json:/etc/rabbitmq/definitions.json \
    --publish="4369:4369" \
    --publish="5671:5671" \
    --publish="5672:5672" \
    --publish="15671:15671" \
    --publish="15672:15672" \
    --publish="25672:25672" \
    rabbitmq:3-management

celery -A parallelism_poc worker --loglevel=INFO --concurrency=1 -n worker1@%h -Q parallelism

docker exec -it cluster_rabbit1_1 rabbitmqctl list_queues name consumers
