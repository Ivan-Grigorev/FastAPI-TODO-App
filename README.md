# FastAPI To-Do App

## Project Description

This FastAPI To-Do application is created for **educational purposes** to help developers learn the basics of building APIs with FastAPI. The project demonstrates essential functionalities such as creating, reading, updating, and deleting to-do items, providing a practical understanding of RESTful API principles.

## Installation

To set up this project, you will need to install FastAPI along with all necessary dependencies. We recommend using the following command to ensure that everything installs correctly:

```bash
pip install "fastapi[standard]"
```

> **Note**: Make sure to include the quotes around `fastapi[standard]` to ensure compatibility across all terminals. This command installs FastAPI along with optional dependencies for enhanced functionality, including support for data validation, serialization, and more.

### Requirements

In addition to FastAPI, this project relies on the following Python packages:
- **SQLAlchemy**: For database interactions.
- **Pydantic**: For data validation and serialization.
- **Uvicorn**: ASGI server for running the FastAPI application.

You can find all required packages listed in the `requirements.txt` file, which can be installed with:

```bash
pip install -r requirements.txt
```

## Running the Application

To run the FastAPI application, you can use the following commands:

- For **development mode**, run:
  ```bash
  fastapi dev main.py
  ```

- For **production mode**, use:
  ```bash
  fastapi run main.py
  ```

However, please note that this application is primarily designed for **educational purposes**, and the production mode should be utilized with caution and only in appropriate environments.

## API Documentation

FastAPI provides an interactive API documentation interface, allowing you to test the endpoints directly in your browser. Access it at:

```
http://127.0.0.1:8000/docs
```

This interface will guide you through the available endpoints, making it easier to experiment with and learn from the application.

## License

This project is for educational purposes and is licensed under the terms specified in the [LICENSE](LICENSE) file.