"""The HTTP API of Project One."""

from fastapi import FastAPI

app = FastAPI(title="Project One")


@app.get("/health")
def health() -> dict[str, str]:
    """Liveness probe."""
    return {"status": "ok"}


@app.get("/hello")
def hello(name: str = "world") -> dict[str, str]:
    """Greets the given name."""
    return {"message": f"Hello, {name}!"}
