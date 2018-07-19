FROM nginx:latest
RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d/feed.conf
ENTRYPOINT ["nginx", "-g", "daemon off;"]
