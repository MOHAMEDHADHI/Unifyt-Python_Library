#!/bin/bash
# Validate project structure and code quality

echo "=== Unifyt Project Validation ==="
echo ""

# Check Python syntax
echo "1. Checking Python syntax..."
python -m py_compile unifyt/*.py 2>/dev/null && echo "   ✓ Core library syntax OK" || echo "   ✗ Syntax errors in core library"
python -m py_compile tests/*.py 2>/dev/null && echo "   ✓ Tests syntax OK" || echo "   ✗ Syntax errors in tests"
python -m py_compile examples/*.py 2>/dev/null && echo "   ✓ Examples syntax OK" || echo "   ✗ Syntax errors in examples"

# Check imports
echo ""
echo "2. Checking imports..."
python -c "import unifyt" 2>/dev/null && echo "   ✓ Package imports successfully" || echo "   ✗ Import errors"
python -c "from unifyt import Quantity, Unit, constants, utils" 2>/dev/null && echo "   ✓ Main exports OK" || echo "   ✗ Export errors"

# Check file structure
echo ""
echo "3. Checking file structure..."
[ -f "unifyt/__init__.py" ] && echo "   ✓ unifyt/__init__.py exists" || echo "   ✗ Missing unifyt/__init__.py"
[ -f "unifyt/quantity.py" ] && echo "   ✓ unifyt/quantity.py exists" || echo "   ✗ Missing unifyt/quantity.py"
[ -f "unifyt/unit.py" ] && echo "   ✓ unifyt/unit.py exists" || echo "   ✗ Missing unifyt/unit.py"
[ -f "unifyt/constants.py" ] && echo "   ✓ unifyt/constants.py exists" || echo "   ✗ Missing unifyt/constants.py"
[ -f "unifyt/utils.py" ] && echo "   ✓ unifyt/utils.py exists" || echo "   ✗ Missing unifyt/utils.py"

# Check documentation
echo ""
echo "4. Checking documentation..."
[ -f "README.md" ] && echo "   ✓ README.md exists" || echo "   ✗ Missing README.md"
[ -f "GETTING_STARTED.md" ] && echo "   ✓ GETTING_STARTED.md exists" || echo "   ✗ Missing GETTING_STARTED.md"
[ -f "docs/user_guide.md" ] && echo "   ✓ User guide exists" || echo "   ✗ Missing user guide"
[ -f "docs/api_reference.md" ] && echo "   ✓ API reference exists" || echo "   ✗ Missing API reference"

# Check tests
echo ""
echo "5. Checking tests..."
[ -f "tests/test_quantity.py" ] && echo "   ✓ Quantity tests exist" || echo "   ✗ Missing quantity tests"
[ -f "tests/test_unit.py" ] && echo "   ✓ Unit tests exist" || echo "   ✗ Missing unit tests"
[ -f "tests/test_constants.py" ] && echo "   ✓ Constants tests exist" || echo "   ✗ Missing constants tests"

# Check examples
echo ""
echo "6. Checking examples..."
[ -f "examples/basic_usage.py" ] && echo "   ✓ Basic usage example exists" || echo "   ✗ Missing basic usage"
[ -f "examples/complete_demo.py" ] && echo "   ✓ Complete demo exists" || echo "   ✗ Missing complete demo"

# Count files
echo ""
echo "7. Project statistics..."
echo "   Python files: $(find . -name "*.py" -not -path "./.venv/*" -not -path "./venv/*" | wc -l)"
echo "   Test files: $(find tests -name "test_*.py" | wc -l)"
echo "   Example files: $(find examples -name "*.py" | wc -l)"
echo "   Documentation files: $(find . -name "*.md" | wc -l)"

echo ""
echo "=== Validation Complete ==="
