# Build Stage
FROM maven:3.9-eclipse-temurin-17-alpine AS builder
WORKDIR /app
COPY pom.xml /src/app/
RUN mvn dependency:go-offline
COPY src ./src
RUN mvn package -DskipTests

# Production Stage
FROM eclipse-temurin:17-jre-alpine
RUN adduser --system --no-create-home appuser
RUN apk add --not-cache wget
WORKDIR /app
COPY --from=builder --chown=appuser:appuser /app/target/final-app-1.0.jar .
EXPOSE 8080
HEALTHCHECK --interval=30s --timeout=10s --start-period=15s --retries=3 \ CMD wget -q --spider http://localhost:8080/actuator/health || exit 1
CMD ["java", "-jar", "final-app-1.0.jar"]