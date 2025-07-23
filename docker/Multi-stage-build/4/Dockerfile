FROM node:18-alpine
WORKDIR /usr/src/app
COPY package*json /usr/src/app
RUN npm install
COPY . .
RUN apk add --no-cache curl
HEALTHCHECK --interval=15s --timeout=5s --retries=3 CMD curl -f http://localhost:3000/healthz || exit 1
CMD [ "node","server.js" ]