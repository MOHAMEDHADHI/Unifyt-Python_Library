# Contributing to Unifyt

Thank you for your interest in contributing to Unifyt! This document provides guidelines and instructions for contributing.

## Code of Conduct

Be respectful and inclusive. We welcome contributions from everyone.

## How to Contribute

### Reporting Bugs

If you find a bug, please open an issue with:
- A clear description of the problem
- Steps to reproduce
- Expected vs actual behavior
- Your environment (Python version, OS, etc.)

### Suggesting Features

Feature requests are welcome! Please:
- Check if the feature already exists or is planned
- Describe the use case clearly
- Explain why it would be useful

### Contributing Code

1. **Fork the repository**
   ```bash
   git clone https://github.com/yourusername/unifyt.git
   cd unifyt
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install development dependencies**
   ```bash
   pip install -e ".[dev]"
   ```

4. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

5. **Make your changes**
   - Write clear, documented code
   - Follow the existing code style
   - Add tests for new functionality
   - Update documentation as needed

6. **Run tests**
   ```bash
   pytest tests/
   ```

7. **Check code quality**
   ```bash
   # Format code
   black unifyt/ tests/
   isort unifyt/ tests/
   
   # Lint
   flake8 unifyt/
   
   # Type check
   mypy unifyt/
   ```

8. **Commit your changes**
   ```bash
   git add .
   git commit -m "Add feature: description"
   ```

9. **Push and create a pull request**
   ```bash
   git push origin feature/your-feature-name
   ```

## Development Guidelines

### Code Style

- Follow PEP 8
- Use type hints
- Write docstrings for all public APIs
- Keep functions focused and small
- Use meaningful variable names

### Testing

- Write tests for all new features
- Maintain or improve code coverage
- Test edge cases
- Use descriptive test names

### Documentation

- Update docstrings
- Add examples for new features
- Update user guide if needed
- Keep API reference current

### Commit Messages

- Use clear, descriptive messages
- Start with a verb (Add, Fix, Update, etc.)
- Reference issues when applicable

## Project Structure

```
unifyt/
├── unifyt/              # Main package
│   ├── __init__.py
│   ├── quantity.py     # Quantity class
│   ├── unit.py         # Unit class
│   ├── dimensions.py   # Dimension class
│   ├── unit_registry.py
│   └── context.py
├── tests/              # Test suite
├── examples/           # Example scripts
├── docs/               # Documentation
└── setup.py           # Package configuration
```

## Testing

Run the full test suite:
```bash
pytest tests/ -v
```

Run with coverage:
```bash
pytest tests/ --cov=unifyt --cov-report=html
```

Run specific tests:
```bash
pytest tests/test_quantity.py
pytest tests/test_quantity.py::TestQuantityCreation
```

## Documentation

Build documentation locally:
```bash
cd docs
# Add your documentation build commands here
```

## Release Process

(For maintainers)

1. Update version in `setup.py` and `unifyt/__init__.py`
2. Update `CHANGELOG.md`
3. Create a git tag
4. Build and upload to PyPI

## Questions?

Feel free to open an issue for any questions about contributing.

## License

By contributing, you agree that your contributions will be licensed under the MIT License.
