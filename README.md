# Docker Worker Demo

A small FastAPI service packaged with Docker. This project demonstrates building an image, running a container, exposing an HTTP port, and checking application health.

## Requirements

- Docker Desktop (or Docker Engine) running
- `curl` (for the example requests)

## Build the image

```bash
docker build -t worker-demo:1.0 .
```

## Run the container

```bash
docker run -d --name worker-1 -p 8000:8000 worker-demo:1.0
```

Check that it is running:

```bash
docker ps
docker logs worker-1
```

## Try the API

Health check:

```bash
curl http://localhost:8000/health
```

Submit a sample task:

```bash
curl -X POST http://localhost:8000/tasks \
  -H "Content-Type: application/json" \
  -d '{"task_name":"meter-data-processing"}'
```

The response includes the container hostname and process ID so you can see which worker handled the request.

Interactive API documentation is available at http://localhost:8000/docs.

## Useful Docker commands

```bash
docker ps
docker inspect worker-1
docker logs worker-1
docker stop worker-1
docker start worker-1
docker rm -f worker-1
```

## Project files

- `main.py` — FastAPI health and task endpoints
- `requirements.txt` — Python dependencies
- `Dockerfile` — image build instructions and container health check
- `.dockerignore` — excludes local files from the build context

## Next steps

This is a learning demo, not a production task-processing system. The task endpoint currently returns a response immediately; it does not use a durable queue. A future iteration can add a supervisor, a queue, worker lifecycle management, concurrency limits, and quarantine handling.
