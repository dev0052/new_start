FROM node:18-alpine
WORKDIR /docker/Simple-Build
# generally WORKDIR has a conventional choise which is "/app", and "/usr/src/app"
COPY package*.json ./
RUN npm install
COPY . .
EXPOSE 8080
CMD ["node","server.js"]