FROM alpine:latest
RUN apk update && \
	apk --no-cache add wget ca-certificates && \
	update-ca-certificates && \
	cd /sbin && \
	wget "https://s3.amazonaws.com/ml-sreracha/sreracha" && \
	chmod +x /sbin/sreracha
EXPOSE 80                                                                                                     
USER root
ENTRYPOINT /sbin/sreracha