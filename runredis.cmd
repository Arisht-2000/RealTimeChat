REM This script runs a Redis container using Docker.
REM It maps port 6379 on the host to port 6379 on the container.
REM The container is named "chatApp-redis" and will be removed after it stops.
REM Ensure Docker is installed and running before executing this script.
REM To run this script, save it as runredis.cmd and execute it in a command prompt.
REM You can stop the container by pressing Ctrl+C in the command prompt.
@echo off
docker run -d --rm -p 6379:6379 --name chatApp-redis redis:7
if %errorlevel% neq 0 (
    echo Failed to start Redis container. Please check Docker installation and try again.
    exit /b %errorlevel%
)
echo Redis container is running. You can connect to it on port 6379.
echo To stop the container, press Ctrl+C in this command prompt.
echo To remove the container, run: docker rm chatApp-redis
echo To view logs, run: docker logs chatApp-redis
echo To access the Redis CLI, run: docker exec -it chatApp-redis redis-cli
pause
REM End of script
exit /b 0