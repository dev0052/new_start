FROM node:18-alpine
WORKDIR /docker/1
COPY package.json ./
RUN npm install
COPY . .
EXPOSE 8080
CMD ["node","server.js"]