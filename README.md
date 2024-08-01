
# `init_project`

`init_project` is a CLI tool designed to help developers quickly initialize a project structure with predefined directories and files. It simplifies the process of setting up a new project, ensuring consistency and saving time.

## Features

- 🚀Automatically creates a set of predefined directories.
- 🚀Adds specified files within each directory.
- 🚀Allows customization of file extensions.

## Installation

To install the `init_project` package, use `pip`:

```bash
pip install init_project
```

## Usage

After installing, you can use the `init_project` command to initialize your project structure. 

### Basic Usage

To create the project structure in the current directory with files having a `.py` extension, run:

```bash
init_project . py
```

### Specifying a Different Directory

To create the project structure in a specific directory (e.g., `/path/to/your/project`) with files having a `.js` extension, run:

```bash
init_project /path/to/your/project js
```

## Project Structure

The tool will create the following directory structure:

```
/path/to/your/project
│
├── controllers
│   └── __init__.ext
│
├── middlewares
│   └── __init__.ext
│
├── utils
│   └── __init__.ext
│
├── routers
│   └── __init__.ext
│
├── models
│   └── __init__.ext
│
├── configs
│   ├── __init__.ext
│   └── config.ext
│
└── services
    └── __init__.ext
```

Where `.ext` is the file extension you specified when running the `init_project` command.

## Development

### Setting Up for Development

To set up a development environment:

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/init_project.git
   cd init_project
   ```

2. Create and activate a virtual environment (optional but recommended):

   ```bash
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   ```

3. Install the package in editable mode with development dependencies:

   ```bash
   pip install -e .
   ```


## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.

### Reporting Issues

If you encounter any issues, please report them on the [issue tracker](https://github.com/Elijah57/init_project/issues).

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

