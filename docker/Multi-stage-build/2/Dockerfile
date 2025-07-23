# First Stage
FROM golang:1.22-alpine AS builder
WORKDIR /usr/src/app
COPY main.go .
RUN go build -o /usr/src/app/server

# Final Stage
FROM scratch
COPY --from=builder /usr/src/app/server /server
EXPOSE 8080
CMD [ "/server" ]